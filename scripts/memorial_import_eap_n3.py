#!/usr/bin/env python3
"""
Importar EAP do Electra Towers até N3 (sem subetapas).
N1=UC, N2=Célula, N3=Etapa. CPUs serão vinculadas manualmente.
"""
import os, json, requests
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"
PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"

# AUTH
print("🔐 Autenticando...", flush=True)
auth = requests.post(f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}, timeout=15)
token = auth.json()['access_token']
headers = {
    "apikey": ANON_KEY, "Authorization": f"Bearer {token}",
    "Content-Type": "application/json", "Prefer": "return=representation"
}
print("✅ Autenticado\n", flush=True)

# CARREGAR EAP
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# PREPARAR ITENS ATÉ N3
all_items = []

for uc_idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_code = uc['codigo'].zfill(2)
    all_items.append({
        "code": uc_code, "name": uc['nome'], "level": 1,
        "sequence": uc_idx, "parent_code": None
    })
    
    for cel_idx, cel in enumerate(uc.get('celulas', [])):
        cel_code = f"{uc_code}.{cel['codigo'].zfill(2)}"
        all_items.append({
            "code": cel_code, "name": cel['nome'], "level": 2,
            "sequence": cel_idx, "parent_code": uc_code
        })
        
        for et_idx, et in enumerate(cel.get('etapas', [])):
            et_parts = et['codigo'].split('.')
            et_seq = et_parts[-1] if len(et_parts) >= 2 else str(et_idx + 1).zfill(3)
            et_code = f"{cel_code}.{et_seq}"
            all_items.append({
                "code": et_code, "name": et['nome'], "level": 3,
                "sequence": et_idx, "parent_code": cel_code,
                "is_leaf": False  # Não é folha — CPUs serão adicionadas como N4 manualmente
            })

print(f"📋 {len(all_items)} itens preparados (N1-N3)\n", flush=True)

# IMPORTAR POR LEVEL
code_to_id = {}

for level in [1, 2, 3]:
    level_items = [it for it in all_items if it['level'] == level]
    
    batch = []
    for item in level_items:
        parent_id = code_to_id.get(item.get('parent_code')) if item.get('parent_code') else None
        payload = {
            "budget_id": BUDGET_ID,
            "parent_id": parent_id,
            "code": item['code'],
            "name": item['name'],
            "description": item['name'],
            "level": level,
            "sequence": item['sequence'],
            "is_leaf": item.get('is_leaf', False),
            "total_price": 0
        }
        batch.append(payload)
    
    print(f"  Level {level}: importando {len(batch)} itens...", flush=True)
    
    resp = requests.post(f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers, json=batch, timeout=60)
    
    if resp.status_code in [200, 201]:
        for j, ret in enumerate(resp.json()):
            if j < len(level_items):
                code_to_id[level_items[j]['code']] = ret['item_id']
        print(f"  ✅ Level {level}: {len(resp.json())} itens", flush=True)
    else:
        print(f"  ❌ Level {level}: {resp.status_code} - {resp.text[:200]}", flush=True)

print(f"\n{'='*60}", flush=True)
print(f"✅ IMPORTAÇÃO CONCLUÍDA! (até N3)", flush=True)
print(f"   N1 (UCs): {len([i for i in all_items if i['level']==1])}", flush=True)
print(f"   N2 (Células): {len([i for i in all_items if i['level']==2])}", flush=True)
print(f"   N3 (Etapas): {len([i for i in all_items if i['level']==3])}", flush=True)
print(f"   Total: {len(all_items)}", flush=True)
print(f"{'='*60}", flush=True)
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}", flush=True)
