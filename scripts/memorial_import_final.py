#!/usr/bin/env python3
"""
Importação FINAL do orçamento executivo Electra Towers
Versão otimizada com batches e progresso detalhado
"""
import os, sys, json, requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')
PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

# Autenticar
print("🔐 Autenticando...", flush=True)
auth_response = requests.post(
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
# INSUMOS
# ============================================================
print("📦 Importando insumos...", flush=True)

# Buscar existentes
existing = requests.get(
    f"{SUPABASE_URL}/rest/v1/insumos?select=id,code&project_id=eq.{PROJECT_ID}",
    headers=headers
).json()
existing_codes = {i['code']: i['id'] for i in existing}
print(f"  → {len(existing_codes)} já cadastrados", flush=True)

insumo_map = {}
new_count = 0

for i, insumo in enumerate(insumos_data):
    codigo = insumo['codigo']
    
    if codigo in existing_codes:
        insumo_map[codigo] = existing_codes[codigo]
        continue
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/insumos",
        headers=headers,
        json={
            "code": codigo,
            "description": insumo['descricao'],
            "unit": insumo['unidade'],
            "price_cents": int(float(insumo['custo_unitario']) * 100),
            "project_id": PROJECT_ID,
            "is_active": True,
            "budget_type": "executivo"
        }
    )
    
    if response.status_code in [200, 201]:
        insumo_map[codigo] = response.json()[0]['id']
        new_count += 1
        if new_count % 100 == 0:
            print(f"  → {new_count} importados...", flush=True)

print(f"✅ {new_count} novos insumos\n", flush=True)

# Criar mapa descrição → ID para vincular CPUs
desc_to_id = {}
for ins in insumos_data:
    if ins['codigo'] in insumo_map:
        desc_to_id[ins['descricao']] = insumo_map[ins['codigo']]

# ============================================================
# CPUs
# ============================================================
print("🔧 Importando CPUs...", flush=True)

existing = requests.get(
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,code&project_id=eq.{PROJECT_ID}",
    headers=headers
).json()
existing_cpus = {c['code']: c['id'] for c in existing}
print(f"  → {len(existing_cpus)} já cadastradas", flush=True)

cpu_map = {}
new_cpus = 0

for i, cpu in enumerate(cpus_data):
    codigo = cpu['codigo']
    
    if codigo in existing_cpus:
        cpu_map[codigo] = existing_cpus[codigo]
        continue
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/composicoes",
        headers=headers,
        json={
            "code": codigo,
            "description": cpu['descricao'],
            "unit": cpu['unidade'],
            "unit_direct_cost_cents": int(float(cpu['custo_total']) * 100),
            "project_id": PROJECT_ID,
            "is_active": True,
            "budget_type": "executivo"
        }
    )
    
    if response.status_code in [200, 201]:
        cpu_id = response.json()[0]['id']
        cpu_map[codigo] = cpu_id
        
        # Vincular insumos
        cpu_insumos = []
        for ins in cpu.get('insumos', []):
            if ins['descricao'] in desc_to_id:
                cpu_insumos.append({
                    "composicao_id": cpu_id,
                    "insumo_id": desc_to_id[ins['descricao']],
                    "coefficient": ins['quantidade']
                })
        
        if cpu_insumos:
            requests.post(
                f"{SUPABASE_URL}/rest/v1/composicoes_items",
                headers=headers,
                json=cpu_insumos
            )
        
        new_cpus += 1
        if new_cpus % 100 == 0:
            print(f"  → {new_cpus} importadas...", flush=True)

print(f"✅ {new_cpus} novas CPUs\n", flush=True)

# ============================================================
# EAP
# ============================================================
print("📋 Importando estrutura EAP...", flush=True)

def import_level(parent_id, items, level_name, seq_start=0):
    count = 0
    for idx, item in enumerate(items):
        response = requests.post(
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
    response = requests.post(
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
