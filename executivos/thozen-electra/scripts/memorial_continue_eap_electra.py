#!/usr/bin/env python3
"""
Continuar importação da EAP Electra Towers.
Verifica o que já existe e importa apenas o que falta.
"""
import os, sys, json, requests, time
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"
CLIENT_ID = "2297582c-660c-45c8-9c3a-84aea1b5ac01"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

TIMEOUT = 30  # Mais timeout
MAX_RETRIES = 5

def req(method, url, **kwargs):
    kwargs['timeout'] = TIMEOUT
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.request(method, url, **kwargs)
            return resp
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if attempt == MAX_RETRIES - 1:
                raise
            wait = (attempt + 1) * 3
            print(f"  ⚠️ Timeout, aguardando {wait}s...", flush=True)
            time.sleep(wait)

# AUTH
print("🔐 Autenticando...", flush=True)
auth = req('POST', f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD})
token = auth.json()['access_token']

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}
print("✅ Autenticado\n", flush=True)

# Carregar EAP
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# Buscar itens existentes para saber onde parou
print("🔍 Verificando itens existentes...", flush=True)
existing_response = req('GET',
    f"{SUPABASE_URL}/rest/v1/budget_items?budget_id=eq.{BUDGET_ID}&select=item_id,code,level&limit=1000",
    headers=headers)
existing_items = existing_response.json()
existing_codes = {item['code']: item['item_id'] for item in existing_items}
print(f"✅ {len(existing_codes)} itens já existem\n", flush=True)

# Buscar CPUs
cpus_response = req('GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,description&client_id=eq.{CLIENT_ID}&project_id=is.null&limit=1000",
    headers=headers)
cpus_by_desc = {c['description']: c['id'] for c in cpus_response.json()}

def create_item(parent_id, code, name, level, sequence, is_leaf=False, composicao_id=None):
    if code in existing_codes:
        return existing_codes[code]
    
    payload = {
        "budget_id": BUDGET_ID,
        "parent_id": parent_id,
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
        payload.update({"unit": "VB", "quantity": 0, "unit_price": 0})
    
    resp = req('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers, json=payload)
    
    if resp.status_code in [200, 201]:
        item_id = resp.json()[0]['item_id']
        existing_codes[code] = item_id
        return item_id
    else:
        print(f"    ❌ Erro {code}: {resp.status_code} - {resp.text[:150]}", flush=True)
        return None

print("📊 Continuando importação...\n", flush=True)
total_new = 0
total_skipped = 0

for uc_idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_code = uc['codigo'].zfill(2)
    
    uc_id = create_item(None, uc_code, uc['nome'], 1, uc_idx)
    if uc_code in existing_codes and uc_id:
        pass  # UC já existe
    elif uc_id:
        total_new += 1
    else:
        continue
    
    print(f"━━━ UC {uc_code}: {uc['nome']} ━━━", flush=True)
    
    for cel_idx, cel in enumerate(uc.get('celulas', [])):
        cel_code_raw = cel['codigo'].zfill(2)
        cel_code = f"{uc_code}.{cel_code_raw}"
        
        if cel_code in existing_codes:
            cel_id = existing_codes[cel_code]
            total_skipped += 1
        else:
            cel_id = create_item(uc_id, cel_code, cel['nome'], 2, cel_idx)
            if cel_id:
                total_new += 1
                print(f"  + N2 {cel_code}: {cel['nome']}", flush=True)
            else:
                continue
        
        for et_idx, et in enumerate(cel.get('etapas', [])):
            et_parts = et['codigo'].split('.')
            et_seq = et_parts[-1] if len(et_parts) >= 2 else str(et_idx + 1).zfill(3)
            et_code = f"{cel_code}.{et_seq}"
            
            if et_code in existing_codes:
                et_id = existing_codes[et_code]
                total_skipped += 1
            else:
                et_id = create_item(cel_id, et_code, et['nome'], 3, et_idx)
                if et_id:
                    total_new += 1
                else:
                    continue
            
            for sub_idx, sub in enumerate(et.get('subetapas', [])):
                sub_parts = sub['codigo'].split('.')
                sub_seq = sub_parts[-1] if len(sub_parts) >= 3 else str(sub_idx + 1).zfill(3)
                sub_code = f"{et_code}.{sub_seq}"
                
                if sub_code in existing_codes:
                    total_skipped += 1
                    continue
                
                cpu_id = cpus_by_desc.get(sub['nome'])
                sub_id = create_item(et_id, sub_code, sub['nome'], 4, sub_idx, is_leaf=True, composicao_id=cpu_id)
                if sub_id:
                    total_new += 1
        
        # Pequena pausa entre células pra não sobrecarregar
        time.sleep(0.5)
    
    print(f"  ✅ UC {uc_code} processada\n", flush=True)

print("=" * 60, flush=True)
print(f"✅ IMPORTAÇÃO CONCLUÍDA!", flush=True)
print(f"   Novos itens: {total_new}", flush=True)
print(f"   Já existiam: {total_skipped}", flush=True)
print(f"=" * 60, flush=True)
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}", flush=True)
