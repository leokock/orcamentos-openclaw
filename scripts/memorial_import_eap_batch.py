#!/usr/bin/env python3
"""
Importar EAP do Electra Towers em batch (poucos requests grandes).
Muito mais rápido que loop de POSTs individuais.
"""
import os, sys, json, requests
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"
CLIENT_ID = "2297582c-660c-45c8-9c3a-84aea1b5ac01"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

# AUTH
print("🔐 Autenticando...", flush=True)
auth = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD},
    timeout=15
)
token = auth.json()['access_token']

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}
print("✅ Autenticado\n", flush=True)

# LIMPAR ORÇAMENTO
print("🗑️  Limpando orçamento...", flush=True)
for lvl in [4, 3, 2, 1]:
    requests.delete(
        f"{SUPABASE_URL}/rest/v1/budget_items?budget_id=eq.{BUDGET_ID}&level=eq.{lvl}",
        headers=headers,
        timeout=30
    )
print("✅ Orçamento limpo\n", flush=True)

# CARREGAR EAP
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# Buscar CPUs
cpus_resp = requests.get(
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,description&client_id=eq.{CLIENT_ID}&project_id=is.null&limit=1000",
    headers=headers,
    timeout=30
)
cpus_by_desc = {c['description']: c['id'] for c in cpus_resp.json()}
print(f"🔧 {len(cpus_by_desc)} CPUs disponíveis\n", flush=True)

# PREPARAR TODOS OS ITENS EM MEMÓRIA
all_items = []
code_to_temp_id = {}
temp_id_counter = 1

def add_item(parent_temp_id, code, name, level, sequence, is_leaf=False, composicao_id=None):
    global temp_id_counter
    temp_id = f"temp_{temp_id_counter}"
    temp_id_counter += 1
    
    item = {
        "_temp_id": temp_id,
        "_parent_temp_id": parent_temp_id,
        "budget_id": BUDGET_ID,
        "code": code,
        "name": name,
        "description": name,
        "level": level,
        "sequence": sequence,
        "is_leaf": is_leaf,
        "composicao_id": composicao_id,
        "total_price": 0
    }
    
    if is_leaf:
        item.update({"unit": "VB", "quantity": 0, "unit_price": 0})
    
    all_items.append(item)
    code_to_temp_id[code] = temp_id
    return temp_id

print("📋 Preparando estrutura em memória...", flush=True)

for uc_idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_code = uc['codigo'].zfill(2)
    uc_temp_id = add_item(None, uc_code, uc['nome'], 1, uc_idx)
    
    for cel_idx, cel in enumerate(uc.get('celulas', [])):
        cel_code_raw = cel['codigo'].zfill(2)
        cel_code = f"{uc_code}.{cel_code_raw}"
        cel_temp_id = add_item(uc_temp_id, cel_code, cel['nome'], 2, cel_idx)
        
        for et_idx, et in enumerate(cel.get('etapas', [])):
            et_parts = et['codigo'].split('.')
            et_seq = et_parts[-1] if len(et_parts) >= 2 else str(et_idx + 1).zfill(3)
            et_code = f"{cel_code}.{et_seq}"
            et_temp_id = add_item(cel_temp_id, et_code, et['nome'], 3, et_idx)
            
            for sub_idx, sub in enumerate(et.get('subetapas', [])):
                sub_parts = sub['codigo'].split('.')
                sub_seq = sub_parts[-1] if len(sub_parts) >= 3 else str(sub_idx + 1).zfill(3)
                sub_code = f"{et_code}.{sub_seq}"
                cpu_id = cpus_by_desc.get(sub['nome'])
                add_item(et_temp_id, sub_code, sub['nome'], 4, sub_idx, is_leaf=True, composicao_id=cpu_id)

print(f"✅ {len(all_items)} itens preparados\n", flush=True)

# IMPORTAR EM BATCHES POR LEVEL (pra respeitar FK)
print("📊 Importando por level...\n", flush=True)
temp_to_real_id = {}

for level in [1, 2, 3, 4]:
    level_items = [it for it in all_items if it['level'] == level]
    if not level_items:
        continue
    
    # Resolver parent_id baseado nos temp IDs
    batch_payload = []
    for item in level_items:
        payload = {k: v for k, v in item.items() if not k.startswith('_')}
        
        # Resolver parent
        if item['_parent_temp_id']:
            payload['parent_id'] = temp_to_real_id[item['_parent_temp_id']]
        else:
            payload['parent_id'] = None
        
        batch_payload.append(payload)
    
    # POST batch
    print(f"  Level {level}: importando {len(batch_payload)} itens...", flush=True)
    
    # Dividir em sub-batches se necessário (Supabase tem limite)
    BATCH_SIZE = 200
    for i in range(0, len(batch_payload), BATCH_SIZE):
        sub_batch = batch_payload[i:i+BATCH_SIZE]
        
        resp = requests.post(
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json=sub_batch,
            timeout=60
        )
        
        if resp.status_code in [200, 201]:
            returned = resp.json()
            # Mapear temp_id → item_id real
            for j, ret_item in enumerate(returned):
                original_idx = i + j
                if original_idx < len(level_items):
                    temp_id = level_items[original_idx]['_temp_id']
                    temp_to_real_id[temp_id] = ret_item['item_id']
            print(f"    ✅ Sub-batch {i//BATCH_SIZE + 1}: {len(returned)} itens", flush=True)
        else:
            print(f"    ❌ Erro: {resp.status_code} - {resp.text[:200]}", flush=True)
    
    print(f"  ✅ Level {level} completo\n", flush=True)

print("=" * 60, flush=True)
print(f"✅ IMPORTAÇÃO CONCLUÍDA!", flush=True)
print(f"   Total: {len(all_items)} itens", flush=True)
print(f"=" * 60, flush=True)
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}", flush=True)
