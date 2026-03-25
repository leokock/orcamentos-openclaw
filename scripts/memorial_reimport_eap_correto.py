#!/usr/bin/env python3
"""
Re-importar EAP com hierarquia correta
Estrutura: UC → Celula → Etapa → Subetapa
Códigos: 01 → 01.001 → 01.001.001 → 01.001.001.001
"""
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
            elif method == 'DELETE':
                return requests.delete(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if attempt == MAX_RETRIES - 1:
                print(f"    ❌ Falhou após {MAX_RETRIES} tentativas", flush=True)
                return None
            print(f"    ⚠️ Timeout, retry {attempt+1}...", flush=True)
            time.sleep(2)

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

# 1. DELETAR ITENS EXISTENTES
print("🗑️ Deletando itens existentes...", flush=True)
delete_response = request_with_retry('DELETE',
    f"{SUPABASE_URL}/rest/v1/budget_items?budget_id=eq.{BUDGET_ID}",
    headers=headers)

if delete_response and delete_response.status_code in [200, 204]:
    print("✅ Itens deletados\n", flush=True)
else:
    print(f"⚠️ Erro ao deletar: {delete_response.status_code if delete_response else 'timeout'}\n", flush=True)

# 2. CARREGAR JSON
print("📂 Carregando EAP...", flush=True)
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# Buscar CPUs
cpus_response = request_with_retry('GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,description&client_id=eq.{CLIENT_ID}&project_id=is.null",
    headers=headers)
cpus_by_desc = {c['description']: c['id'] for c in cpus_response.json()}
print(f"✅ {len(cpus_by_desc)} CPUs disponíveis\n", flush=True)

# 3. IMPORTAR COM CÓDIGOS HIERÁRQUICOS
total_imported = 0

def import_recursive(parent_id, items, level, parent_code=""):
    """Importa recursivamente com códigos hierárquicos"""
    global total_imported
    
    level_map = {1: "UC", 2: "Celula", 3: "Etapa", 4: "Subetapa"}
    
    for idx, item in enumerate(items):
        # Construir código hierárquico
        if level == 1:
            # UC: "01", "02"
            code = item['codigo']
        elif level == 2:
            # Celula: "01.001", "01.002"
            code = f"{parent_code}.{item['codigo']}"
        elif level == 3:
            # Etapa: "01.001.001", formato com 3 dígitos
            seq = str(idx + 1).zfill(3)
            code = f"{parent_code}.{seq}"
        elif level == 4:
            # Subetapa: "01.001.001.001"
            seq = str(idx + 1).zfill(3)
            code = f"{parent_code}.{seq}"
        else:
            code = item['codigo']
        
        is_leaf = (level == 4)
        cpu_id = cpus_by_desc.get(item['nome']) if is_leaf else None
        
        payload = {
            "budget_id": BUDGET_ID,
            "parent_id": parent_id,
            "code": code,
            "name": item['nome'],
            "description": item['nome'],
            "level": level,
            "sequence": idx + 1,
            "is_leaf": is_leaf,
            "composicao_id": cpu_id,
            "total_price": 0
        }
        
        # Só subetapas têm custo
        if is_leaf:
            payload.update({
                "unit": "VB",
                "quantity": 0,
                "unit_price": 0
            })
        
        response = request_with_retry('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers, json=payload)
        
        if response and response.status_code in [200, 201]:
            item_id = response.json()[0]['item_id']
            total_imported += 1
            
            # Log a cada 50 itens
            if total_imported % 50 == 0:
                print(f"  ✅ {total_imported} itens importados...", flush=True)
            
            # Recursão para filhos
            if 'celulas' in item:
                import_recursive(item_id, item['celulas'], level + 1, code)
            elif 'etapas' in item:
                import_recursive(item_id, item['etapas'], level + 1, code)
            elif 'subetapas' in item:
                import_recursive(item_id, item['subetapas'], level + 1, code)
        else:
            print(f"  ⚠️ Erro {level_map.get(level)} {code}: {response.status_code if response else 'timeout'}", flush=True)

# Importar UCs
print("📊 Importando EAP com hierarquia correta...\n", flush=True)

for idx, uc in enumerate(eap_data['unidades_construtivas']):
    print(f"  → UC {uc['codigo']}: {uc['nome']}", flush=True)
    
    response = request_with_retry('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers,
        json={
            "budget_id": BUDGET_ID,
            "parent_id": None,
            "code": uc['codigo'],
            "name": uc['nome'],
            "description": uc['nome'],
            "level": 1,
            "sequence": idx + 1,
            "is_leaf": False,
            "total_price": 0
        })
    
    if response and response.status_code in [200, 201]:
        uc_id = response.json()[0]['item_id']
        total_imported += 1
        
        # Importar filhos
        import_recursive(uc_id, uc['celulas'], 2, uc['codigo'])
        
        print(f"    ✅ UC {uc['codigo']} completa", flush=True)
    else:
        print(f"    ❌ Erro UC {uc['codigo']}: {response.status_code if response else 'timeout'}", flush=True)

print(f"\n{'='*70}")
print(f"✅ IMPORTAÇÃO CONCLUÍDA!")
print(f"{'='*70}")
print(f"📊 Total: {total_imported} itens importados")
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/cdff0592-fb3c-4c13-9516-efde6b56b336")
print(f"{'='*70}")
