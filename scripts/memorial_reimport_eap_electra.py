#!/usr/bin/env python3
"""
Reimportar EAP do Electra Towers com códigos qualificados corretos.

Problema original: Células tinham código relativo (01, 02...) em vez de qualificado (UC.Célula).
Fix: Construir códigos qualificados em runtime a partir da hierarquia.

Hierarquia do Memorial:
  N1 (UC):       código = "01", "02"
  N2 (Célula):   código = "01.01", "01.02", "02.01", "02.02"
  N3 (Etapa):    código = "01.01.001", "02.03.002"
  N4 (Subetapa): código = "01.01.001.001", "02.03.002.003"
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

TIMEOUT = 15
MAX_RETRIES = 3

def req(method, url, **kwargs):
    kwargs['timeout'] = TIMEOUT
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.request(method, url, **kwargs)
            return resp
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if attempt == MAX_RETRIES - 1:
                raise
            print(f"  ⚠️ Timeout, retry {attempt+1}...", flush=True)
            time.sleep(2)

# ============================================================
# AUTH
# ============================================================
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

# ============================================================
# STEP 1: LIMPAR ITENS EXISTENTES
# ============================================================
print("🗑️  Limpando itens existentes do orçamento...", flush=True)

# Deletar de baixo pra cima (folhas primeiro) pra evitar FK violations
for level in [4, 3, 2, 1]:
    resp = req('DELETE',
        f"{SUPABASE_URL}/rest/v1/budget_items?budget_id=eq.{BUDGET_ID}&level=eq.{level}",
        headers=headers)
    if resp.status_code in [200, 204]:
        try:
            deleted = len(resp.json()) if resp.text.strip() else 0
        except:
            deleted = 0
        print(f"  ✅ Level {level}: {deleted} itens removidos", flush=True)
    else:
        print(f"  ⚠️ Level {level}: {resp.status_code} - {resp.text[:200]}", flush=True)

print("", flush=True)

# ============================================================
# STEP 2: CARREGAR EAP E IMPORTAR COM CÓDIGOS QUALIFICADOS
# ============================================================
print("📂 Carregando eap.json...", flush=True)
with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)

# Buscar CPUs do cliente para vincular
print("🔍 Buscando CPUs do catálogo do cliente...", flush=True)
cpus_response = req('GET',
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,description&client_id=eq.{CLIENT_ID}&project_id=is.null&limit=1000",
    headers=headers)
cpus_by_desc = {}
for c in cpus_response.json():
    cpus_by_desc[c['description']] = c['id']
print(f"✅ {len(cpus_by_desc)} CPUs disponíveis\n", flush=True)

def create_item(parent_id, code, name, level, sequence, is_leaf=False, composicao_id=None):
    """Criar um item no orçamento"""
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
    
    # Só folhas (N4) podem ter unit/quantity/unit_price
    if is_leaf:
        payload.update({
            "unit": "VB",
            "quantity": 0,
            "unit_price": 0
        })
    
    resp = req('POST', f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers, json=payload)
    
    if resp.status_code in [200, 201]:
        return resp.json()[0]['item_id']
    else:
        print(f"    ❌ Erro {code} ({name}): {resp.status_code} - {resp.text[:200]}", flush=True)
        return None

print("📊 Importando EAP com códigos qualificados...\n", flush=True)
total = 0
errors = 0

for uc_idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_code = uc['codigo'].zfill(2)  # "01", "02"
    print(f"━━━ UC {uc_code}: {uc['nome']} ━━━", flush=True)
    
    uc_id = create_item(
        parent_id=None,
        code=uc_code,
        name=uc['nome'],
        level=1,
        sequence=uc_idx
    )
    
    if not uc_id:
        errors += 1
        continue
    total += 1
    
    for cel_idx, cel in enumerate(uc.get('celulas', [])):
        # Código qualificado: UC.Célula (ex: "01.01", "02.03")
        cel_code_raw = cel['codigo'].zfill(2)
        cel_code = f"{uc_code}.{cel_code_raw}"
        
        cel_id = create_item(
            parent_id=uc_id,
            code=cel_code,
            name=cel['nome'],
            level=2,
            sequence=cel_idx
        )
        
        if not cel_id:
            errors += 1
            continue
        total += 1
        print(f"  N2 {cel_code}: {cel['nome']}", flush=True)
        
        for et_idx, et in enumerate(cel.get('etapas', [])):
            # Etapa: código original é "XX.YYY" (ex: "01.001")
            # Qualificado: "UC.Célula.Sequência" (ex: "02.03.001")
            et_code_raw = et['codigo']  # ex: "01.001"
            # Extrair a parte da etapa (depois do ponto)
            et_parts = et_code_raw.split('.')
            if len(et_parts) >= 2:
                et_seq = et_parts[-1]  # "001"
            else:
                et_seq = str(et_idx + 1).zfill(3)
            et_code = f"{cel_code}.{et_seq}"
            
            et_id = create_item(
                parent_id=cel_id,
                code=et_code,
                name=et['nome'],
                level=3,
                sequence=et_idx
            )
            
            if not et_id:
                errors += 1
                continue
            total += 1
            
            for sub_idx, sub in enumerate(et.get('subetapas', [])):
                # Subetapa: código original "XX.YYY.ZZZ" (ex: "01.001.001")
                sub_parts = sub['codigo'].split('.')
                if len(sub_parts) >= 3:
                    sub_seq = sub_parts[-1]  # "001"
                else:
                    sub_seq = str(sub_idx + 1).zfill(3)
                sub_code = f"{et_code}.{sub_seq}"
                
                # Tentar vincular CPU pela descrição
                cpu_id = cpus_by_desc.get(sub['nome'])
                
                sub_id = create_item(
                    parent_id=et_id,
                    code=sub_code,
                    name=sub['nome'],
                    level=4,
                    sequence=sub_idx,
                    is_leaf=True,
                    composicao_id=cpu_id
                )
                
                if sub_id:
                    total += 1
                else:
                    errors += 1

    print(f"  ✅ UC {uc_code} completa\n", flush=True)

# ============================================================
# RESUMO
# ============================================================
print("=" * 60, flush=True)
print(f"✅ IMPORTAÇÃO CONCLUÍDA!", flush=True)
print(f"   Itens importados: {total}", flush=True)
print(f"   Erros: {errors}", flush=True)
print(f"=" * 60, flush=True)
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}", flush=True)
