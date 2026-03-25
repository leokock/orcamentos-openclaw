#!/usr/bin/env python3
"""Importar apenas UC 02 (que travou)"""
import os, sys, json, requests, time
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

CLIENT_ID = "2297582c-660c-45c8-9c3a-84aea1b5ac01"
BUDGET_ID = "3dc996e6-7bdd-4523-80c4-bb391cf7060d"

TIMEOUT = 20
MAX_RETRIES = 3

def request_with_retry(method, url, **kwargs):
    kwargs['timeout'] = TIMEOUT
    for attempt in range(MAX_RETRIES):
        try:
            if method == 'POST':
                return requests.post(url, **kwargs)
            elif method == 'GET':
                return requests.get(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if attempt == MAX_RETRIES - 1:
                print(f"    ❌ Falhou após {MAX_RETRIES} tentativas", flush=True)
                return None
            print(f"    ⚠️ Timeout, retry {attempt+1}...", flush=True)
            time.sleep(3)

# Auth
print("🔐 Autenticando...", flush=True)
auth = request_with_retry('POST', f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD})
token = auth.json()['access_token']
print("✅ Autenticado\n", flush=True)

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Carregar EAP
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# Buscar CPUs
cpus_response = request_with_retry('GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,description&client_id=eq.{CLIENT_ID}&project_id=is.null",
    headers=headers)
cpus_by_desc = {c['description']: c['id'] for c in cpus_response.json()}
print(f"✅ {len(cpus_by_desc)} CPUs disponíveis\n", flush=True)

level_map = {"celula": 2, "etapa": 3, "subetapa": 4}

def import_level(parent_id, items, level_name, seq=0):
    count = 0
    for idx, item in enumerate(items):
        is_subetapa = (level_name == 'subetapa')
        cpu_id = cpus_by_desc.get(item['nome']) if is_subetapa else None
        
        payload = {
            "budget_id": BUDGET_ID,
            "parent_id": parent_id,
            "code": item['codigo'],
            "name": item['nome'],
            "description": item['nome'],
            "level": level_map[level_name],
            "sequence": seq + idx,
            "is_leaf": is_subetapa,
            "composicao_id": cpu_id,
            "total_price": 0
        }
        
        if is_subetapa:
            payload.update({"unit": "VB", "quantity": 0, "unit_price": 0})
        
        response = request_with_retry('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers, json=payload)
        
        if response and response.status_code in [200, 201]:
            item_id = response.json()[0]['item_id']
            count += 1
            
            if 'celulas' in item:
                count += import_level(item_id, item['celulas'], 'celula')
            elif 'etapas' in item:
                count += import_level(item_id, item['etapas'], 'etapa')
            elif 'subetapas' in item:
                count += import_level(item_id, item['subetapas'], 'subetapa')
        elif response:
            print(f"  ⚠️ Erro {item['codigo']}: {response.status_code}", flush=True)
        else:
            print(f"  ⚠️ Timeout {item['codigo']}", flush=True)
    
    return count

# Importar UC 02
print("📊 Importando UC 02...", flush=True)
uc = eap_data['unidades_construtivas'][1]  # UC 02

response = request_with_retry('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
    headers=headers,
    json={
        "budget_id": BUDGET_ID,
        "parent_id": None,
        "code": uc['codigo'],
        "name": uc['nome'],
        "description": uc['nome'],
        "level": 1,
        "sequence": 1,
        "is_leaf": False,
        "total_price": 0
    })

if response and response.status_code in [200, 201]:
    uc_id = response.json()[0]['item_id']
    total = 1 + import_level(uc_id, uc['celulas'], 'celula')
    print(f"\n✅ {total} itens UC 02 importados!")
else:
    print(f"❌ Erro ao importar UC 02")
