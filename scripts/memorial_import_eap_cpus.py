#!/usr/bin/env python3
"""
Importar EAP + CPUs no projeto Thozen Electra
Seguindo regras de escopo: memorial-import-scoping.md
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
CLIENT_ID = "2297582c-660c-45c8-9c3a-84aea1b5ac01"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

TIMEOUT = 15
MAX_RETRIES = 3

def request_with_retry(method, url, **kwargs):
    """Request com retry"""
    kwargs['timeout'] = TIMEOUT
    for attempt in range(MAX_RETRIES):
        try:
            if method == 'GET':
                return requests.get(url, **kwargs)
            elif method == 'POST':
                return requests.post(url, **kwargs)
            elif method == 'PATCH':
                return requests.patch(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt == MAX_RETRIES - 1:
                raise
            print(f"    ⚠️ Timeout, retry {attempt+1}/{MAX_RETRIES}...", flush=True)
            time.sleep(2)

# Autenticar
print("🔐 Autenticando...", flush=True)
auth = request_with_retry(
    'POST',
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)
token = auth.json().get('access_token')
print("✅ Autenticado\n", flush=True)

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Carregar JSONs
print("📂 Carregando arquivos...", flush=True)
with open('executivo/thozen-electra/cpus.json', 'r') as f:
    cpus_data = json.load(f)
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

print(f"✅ {len(cpus_data)} CPUs, {len(eap_data['unidades_construtivas'])} UCs\n", flush=True)

# ============================================================
# 1. IMPORTAR/VERIFICAR CPUs NO CATÁLOGO DO CLIENTE
# ============================================================
print("🔧 Verificando CPUs no catálogo do cliente...", flush=True)

# Buscar CPUs existentes
existing_cpus_response = request_with_retry(
    'GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,code&client_id=eq.{CLIENT_ID}&project_id=is.null",
    headers=headers
)

existing_cpus = {c['code']: c['id'] for c in existing_cpus_response.json()}
print(f"  → {len(existing_cpus)} CPUs já no catálogo do cliente", flush=True)

# Detectar tipo de insumo/CPU
def normalizar_grupo(texto):
    return texto.strip() if texto else ""

# Criar mapa de CPUs a importar
cpu_map = {}
new_cpus = 0
batch = []
batch_size = 50

import hashlib

for idx, cpu in enumerate(cpus_data):
    codigo_original = cpu['codigo']
    
    # Gerar código curto (hash dos primeiros 40 chars da descrição + índice)
    if len(codigo_original) > 50:
        hash_base = codigo_original[:40] + str(idx)
        codigo = "CPU_" + hashlib.md5(hash_base.encode()).hexdigest()[:10].upper()
    else:
        codigo = codigo_original
    
    # Se já existe, mapear ID
    if codigo in existing_cpus:
        cpu_map[codigo_original] = existing_cpus[codigo]
        continue
    
    # Adicionar ao batch
    batch.append({
        "code": codigo,
        "description": cpu['descricao'][:255],  # Truncar descrição também
        "unit": cpu['unidade'],
        "unit_direct_cost_cents": int(float(cpu['custo_total']) * 100),
        "client_id": CLIENT_ID,
        "project_id": None,
        "is_active": True,
        "budget_type": "executivo",
        "source": "catalog"
    })
    
    # Mapear código original → código curto para vinculação
    cpu_map[codigo_original] = None  # Será preenchido após insert
    
    # Enviar batch
    if len(batch) >= batch_size:
        print(f"  🔧 Importando batch de {len(batch)} CPUs...", flush=True)
        response = request_with_retry(
            'POST',
            f"{SUPABASE_URL}/rest/v1/composicoes",
            headers=headers,
            json=batch
        )
        
        if response.status_code in [200, 201]:
            # Mapear código curto gerado → ID
            returned_items = response.json()
            for i, item in enumerate(returned_items):
                # Encontrar CPU original correspondente pelo índice do batch
                original_idx = new_cpus + i
                if original_idx < len(cpus_data):
                    codigo_original = cpus_data[original_idx]['codigo']
                    cpu_map[codigo_original] = item['id']
            
            new_cpus += len(batch)
            print(f"    ✅ {new_cpus} CPUs importadas", flush=True)
        else:
            print(f"    ⚠️ Erro: {response.status_code} - {response.text[:200]}", flush=True)
        
        batch = []

# Último batch
if batch:
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/composicoes",
        headers=headers,
        json=batch
    )
    if response.status_code in [200, 201]:
        returned_items = response.json()
        for i, item in enumerate(returned_items):
            original_idx = new_cpus + i
            if original_idx < len(cpus_data):
                codigo_original = cpus_data[original_idx]['codigo']
                cpu_map[codigo_original] = item['id']
        new_cpus += len(batch)

print(f"✅ {new_cpus} novas CPUs importadas\n", flush=True)

# ============================================================
# 2. IMPORTAR ESTRUTURA EAP
# ============================================================
print("📊 Importando estrutura EAP...", flush=True)

# Mapeamento level string → integer
level_map = {
    "unidade_construtiva": 1,
    "celula": 2,
    "etapa": 3,
    "subetapa": 4
}

def import_eap_level(parent_id, items, level_name, seq_start=0):
    """Importa recursivamente os níveis da EAP"""
    count = 0
    for idx, item in enumerate(items):
        # Tentar mapear CPU pelo código
        composicao_id = cpu_map.get(item['codigo']) if level_name == 'subetapa' else None
        
        payload = {
            "budget_id": BUDGET_ID,
            "parent_id": parent_id,
            "code": item['codigo'],
            "description": item['nome'],
            "level": level_map[level_name],  # Converter para integer
            "sequence": seq_start + idx,
            "unit": "VB",
            "quantity": 0,
            "unit_price": 0,
            "total_price": 0,
            "is_leaf": level_name == 'subetapa',
            "composicao_id": composicao_id
        }
        
        response = request_with_retry(
            'POST',
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json=payload
        )
        
        if response.status_code in [200, 201]:
            item_id = response.json()[0]['item_id']
            count += 1
            
            # Recursão para níveis filhos
            if 'celulas' in item:
                count += import_eap_level(item_id, item['celulas'], 'celula')
            elif 'etapas' in item:
                count += import_eap_level(item_id, item['etapas'], 'etapa')
            elif 'subetapas' in item:
                count += import_eap_level(item_id, item['subetapas'], 'subetapa')
        else:
            print(f"  ⚠️ Erro ao importar {level_name} {item['codigo']}: {response.status_code}", flush=True)
    
    return count

total_items = 0
for idx, uc in enumerate(eap_data['unidades_construtivas']):
    print(f"  → Importando UC {uc['codigo']}: {uc['nome']}", flush=True)
    
    uc_payload = {
        "budget_id": BUDGET_ID,
        "parent_id": None,
        "code": uc['codigo'],
        "description": uc['nome'],
        "level": 1,  # UC = level 1
        "sequence": idx,
        "unit": "VB",
        "quantity": 0,
        "unit_price": 0,
        "total_price": 0,
        "is_leaf": False
    }
    
    response = request_with_retry(
        'POST',
        f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers,
        json=uc_payload
    )
    
    if response.status_code in [200, 201]:
        uc_id = response.json()[0]['item_id']
        total_items += 1
        total_items += import_eap_level(uc_id, uc['celulas'], 'celula')
        print(f"    ✅ UC {uc['codigo']} completa", flush=True)
    else:
        print(f"    ❌ Erro: {response.status_code} - {response.text[:200]}", flush=True)

print(f"\n✅ {total_items} itens EAP importados\n", flush=True)

# ============================================================
# RESUMO FINAL
# ============================================================
print("="*60)
print("✅ IMPORTAÇÃO CONCLUÍDA!")
print("="*60)
print(f"🔧 CPUs: {new_cpus} novas, {len(existing_cpus)} reutilizadas")
print(f"📊 Itens EAP: {total_items}")
print(f"\n🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
print("="*60)
