#!/usr/bin/env python3
"""
Importação robusta com timeout, retry e batch
"""
import os, sys, json, requests, time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')
PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

TIMEOUT = 10  # segundos
MAX_RETRIES = 3

def request_with_retry(method, url, **kwargs):
    """Request com retry e timeout"""
    kwargs['timeout'] = TIMEOUT
    for attempt in range(MAX_RETRIES):
        try:
            if method == 'GET':
                return requests.get(url, **kwargs)
            elif method == 'POST':
                return requests.post(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt == MAX_RETRIES - 1:
                raise
            print(f"    ⚠️ Timeout, retry {attempt+1}/{MAX_RETRIES}...", flush=True)
            time.sleep(2)

# Autenticar
print("🔐 Autenticando...", flush=True)
auth_response = request_with_retry(
    'POST',
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)
token = auth_response.json().get('access_token')
print("✅ Autenticado\n", flush=True)

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Carregar JSONs
print("📂 Carregando arquivos...", flush=True)
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)
with open('executivo/thozen-electra/cpus.json', 'r') as f:
    cpus_data = json.load(f)
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

print(f"✅ {len(insumos_data)} insumos, {len(cpus_data)} CPUs, {len(eap_data['unidades_construtivas'])} UCs\n", flush=True)

# ============================================================
# INSUMOS (BATCH)
# ============================================================
print("📦 Importando insumos em batches de 50...", flush=True)

# Buscar existentes (global, sem filtro de projeto)
existing = request_with_retry(
    'GET',
    f"{SUPABASE_URL}/rest/v1/insumos?select=id,code&limit=10000",
    headers=headers
).json()
existing_codes = {i['code']: i['id'] for i in existing}
print(f"  → {len(existing_codes)} já cadastrados", flush=True)

insumo_map = {}
new_count = 0
batch = []
batch_size = 50

for i, insumo in enumerate(insumos_data):
    codigo = insumo['codigo']
    
    if codigo in existing_codes:
        insumo_map[codigo] = existing_codes[codigo]
        continue
    
    batch.append({
        "code": codigo,
        "description": insumo['descricao'],
        "type": "material",
        "unit": insumo['unidade'],
        "price_cents": int(float(insumo['custo_unitario']) * 100),
        "is_active": True,
        "budget_type": "executivo",
        "origin_system": "import",
        "source": "catalog"
    })
    
    # Enviar batch quando atingir o tamanho
    if len(batch) >= batch_size:
        response = request_with_retry(
            'POST',
            f"{SUPABASE_URL}/rest/v1/insumos",
            headers=headers,
            json=batch
        )
        
        if response.status_code in [200, 201]:
            for item in response.json():
                insumo_map[item['code']] = item['id']
            new_count += len(batch)
            print(f"  → {new_count} importados...", flush=True)
        else:
            print(f"  ⚠️ Erro no batch: {response.status_code}", flush=True)
        
        batch = []

# Enviar último batch
if batch:
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/insumos",
        headers=headers,
        json=batch
    )
    if response.status_code in [200, 201]:
        for item in response.json():
            insumo_map[item['code']] = item['id']
        new_count += len(batch)

print(f"✅ {new_count} novos insumos\n", flush=True)

# Criar mapa descrição → ID
desc_to_id = {}
for ins in insumos_data:
    if ins['codigo'] in insumo_map:
        desc_to_id[ins['descricao']] = insumo_map[ins['codigo']]

# ============================================================
# CPUs (BATCH)
# ============================================================
print("🔧 Importando CPUs em batches de 50...", flush=True)

existing = request_with_retry(
    'GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,code&limit=10000",
    headers=headers
).json()
existing_cpus = {c['code']: c['id'] for c in existing}
print(f"  → {len(existing_cpus)} já cadastradas", flush=True)

cpu_map = {}
new_cpus = 0
batch = []

for cpu in cpus_data:
    codigo = cpu['codigo']
    
    if codigo in existing_cpus:
        cpu_map[codigo] = existing_cpus[codigo]
        continue
    
    batch.append({
        "code": codigo,
        "description": cpu['descricao'],
        "unit": cpu['unidade'],
        "unit_direct_cost_cents": int(float(cpu['custo_total']) * 100),
        "is_active": True,
        "budget_type": "executivo",
        "source": "import"
    })
    
    if len(batch) >= batch_size:
        response = request_with_retry(
            'POST',
            f"{SUPABASE_URL}/rest/v1/composicoes",
            headers=headers,
            json=batch
        )
        
        if response.status_code in [200, 201]:
            for item in response.json():
                cpu_map[item['code']] = item['id']
            new_cpus += len(batch)
            print(f"  → {new_cpus} importadas...", flush=True)
        
        batch = []

if batch:
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/composicoes",
        headers=headers,
        json=batch
    )
    if response.status_code in [200, 201]:
        for item in response.json():
            cpu_map[item['code']] = item['id']
        new_cpus += len(batch)

print(f"✅ {new_cpus} novas CPUs", flush=True)

# Vincular insumos às CPUs
print("🔗 Vinculando insumos às CPUs...", flush=True)
vinculacoes = []

for cpu in cpus_data:
    if cpu['codigo'] not in cpu_map:
        continue
    
    cpu_id = cpu_map[cpu['codigo']]
    for ins in cpu.get('insumos', []):
        if ins['descricao'] in desc_to_id:
            vinculacoes.append({
                "composicao_id": cpu_id,
                "insumo_id": desc_to_id[ins['descricao']],
                "coefficient": ins['quantidade']
            })

# Enviar vinculações em batches
print(f"  → {len(vinculacoes)} vinculações a processar", flush=True)
for i in range(0, len(vinculacoes), 100):
    batch = vinculacoes[i:i+100]
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/composicoes_items",
        headers=headers,
        json=batch
    )
    if i % 500 == 0:
        print(f"  → {i} vinculações processadas...", flush=True)

print(f"✅ Vinculações concluídas\n", flush=True)

# ============================================================
# EAP
# ============================================================
print("📋 Importando estrutura EAP...", flush=True)

def import_level(parent_id, items, level_name, seq_start=0):
    count = 0
    for idx, item in enumerate(items):
        response = request_with_retry(
            'POST',
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json={
                "budget_id": BUDGET_ID,
                "parent_id": parent_id,
                "code": item['codigo'],
                "description": item['nome'],
                "level": level_name,
                "sequence": seq_start + idx,
                "unit": "VB",
                "quantity": 0,
                "unit_price": 0,
                "total_price": 0,
                "is_leaf": False
            }
        )
        
        if response.status_code in [200, 201]:
            item_id = response.json()[0]['item_id']
            count += 1
            
            if 'celulas' in item:
                count += import_level(item_id, item['celulas'], 'celula')
            elif 'etapas' in item:
                count += import_level(item_id, item['etapas'], 'etapa')
            elif 'subetapas' in item:
                count += import_level(item_id, item['subetapas'], 'subetapa')
    
    return count

total = 0
for idx, uc in enumerate(eap_data['unidades_construtivas']):
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers,
        json={
            "budget_id": BUDGET_ID,
            "parent_id": None,
            "code": uc['codigo'],
            "description": uc['nome'],
            "level": "unidade_construtiva",
            "sequence": idx,
            "unit": "VB",
            "quantity": 0,
            "unit_price": 0,
            "total_price": 0,
            "is_leaf": False
        }
    )
    
    if response.status_code in [200, 201]:
        uc_id = response.json()[0]['item_id']
        total += 1
        total += import_level(uc_id, uc['celulas'], 'celula')
        print(f"  → UC {uc['codigo']} importada", flush=True)

print(f"✅ {total} itens EAP\n", flush=True)

# ============================================================
# RESUMO
# ============================================================
print("="*60)
print("✅ IMPORTAÇÃO CONCLUÍDA!")
print("="*60)
print(f"📦 Insumos: {new_count} novos")
print(f"🔧 CPUs: {new_cpus} novas")
print(f"📋 Itens EAP: {total}")
print(f"\n🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
print("="*60)
