#!/usr/bin/env python3
"""
Importação do orçamento executivo Thozen Electra no Memorial Cartesiano via Supabase
Versão 2 - Schema correto descoberto
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv
from datetime import datetime

# Carregar .env.sensitive
load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')
PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"

# ============================================================
# 1. AUTENTICAÇÃO
# ============================================================
print("🔐 Autenticando no Supabase...")
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)

token = auth_response.json().get('access_token')
print(f"✅ Autenticado")

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# ============================================================
# 2. CARREGAR ARQUIVOS JSON
# ============================================================
print("\n📂 Carregando arquivos JSON...")

with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)
print(f"✅ Insumos: {len(insumos_data)}")

with open('executivo/thozen-electra/cpus.json', 'r') as f:
    cpus_data = json.load(f)
print(f"✅ CPUs: {len(cpus_data)}")

with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)
print(f"✅ EAP: {len(eap_data['unidades_construtivas'])} UCs")

# ============================================================
# 3. CRIAR OU BUSCAR TORRE
# ============================================================
print("\n🏗️ Verificando torres do projeto...")
towers_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/project_towers?select=*&project_id=eq.{PROJECT_ID}",
    headers=headers
)

existing_towers = towers_response.json()

if not existing_towers:
    print("⚠️ Criando torre 'Embasamento'...")
    tower_payload = {
        "project_id": PROJECT_ID,
        "tower_name": "Embasamento",
        "tower_number": 1,
        "created_at": datetime.utcnow().isoformat()
    }
    tower_response = requests.post(
        f"{SUPABASE_URL}/rest/v1/project_towers",
        headers=headers,
        json=tower_payload
    )
    if tower_response.status_code in [200, 201]:
        tower_id = tower_response.json()[0]['tower_id']
        print(f"✅ Torre criada: {tower_id}")
    else:
        print(f"❌ Erro ao criar torre: {tower_response.status_code}")
        print(tower_response.text)
        sys.exit(1)
else:
    tower_id = existing_towers[0]['tower_id']
    print(f"✅ Usando torre existente: {tower_id}")

# ============================================================
# 4. CRIAR OU BUSCAR ORÇAMENTO
# ============================================================
print("\n💰 Verificando orçamento do projeto...")
budgets_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/budgets?select=*&project_id=eq.{PROJECT_ID}",
    headers=headers
)

existing_budgets = budgets_response.json()

if not existing_budgets:
    print("⚠️ Criando novo orçamento...")
    budget_payload = {
        "project_id": PROJECT_ID,
        "tower_id": tower_id,
        "name": "Orçamento Executivo - Electra Towers",
        "status": "draft",
        "budget_type": "executivo",
        "created_at": datetime.utcnow().isoformat()
    }
    budget_response = requests.post(
        f"{SUPABASE_URL}/rest/v1/budgets",
        headers=headers,
        json=budget_payload
    )
    if budget_response.status_code in [200, 201]:
        budget_id = budget_response.json()[0]['budget_id']
        print(f"✅ Orçamento criado: {budget_id}")
    else:
        print(f"❌ Erro ao criar orçamento: {budget_response.status_code}")
        print(budget_response.text)
        sys.exit(1)
else:
    budget_id = existing_budgets[0]['budget_id']
    print(f"✅ Usando orçamento existente: {budget_id}")

# ============================================================
# 5. IMPORTAR INSUMOS
# ============================================================
print(f"\n📦 Importando insumos...")

# Buscar insumos existentes
existing_insumos_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/insumos?select=id,code&project_id=eq.{PROJECT_ID}",
    headers=headers
)

existing_insumos = {}
if existing_insumos_response.status_code == 200:
    existing_insumos = {i['code']: i['id'] for i in existing_insumos_response.json()}
    print(f"  → {len(existing_insumos)} já cadastrados")

insumo_id_map = {}
imported = 0
skipped = 0

for i, insumo in enumerate(insumos_data):
    codigo = insumo['codigo']
    
    if codigo in existing_insumos:
        insumo_id_map[codigo] = existing_insumos[codigo]
        skipped += 1
        continue
    
    # price_cents = custo_unitario * 100 (converter R$ para centavos)
    price_cents = int(float(insumo['custo_unitario']) * 100)
    
    payload = {
        "code": codigo,
        "description": insumo['descricao'],
        "unit": insumo['unidade'],
        "price_cents": price_cents,
        "project_id": PROJECT_ID,
        "is_active": True,
        "budget_type": "executivo",
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/insumos",
        headers=headers,
        json=payload
    )
    
    if response.status_code in [200, 201]:
        insumo_id = response.json()[0]['id']
        insumo_id_map[codigo] = insumo_id
        imported += 1
        if imported % 100 == 0:
            print(f"  → {imported} importados...")
    else:
        print(f"⚠️ Erro no insumo {codigo}: {response.status_code}")

print(f"✅ {imported} novos, {skipped} reutilizados")

# ============================================================
# 6. IMPORTAR CPUs
# ============================================================
print(f"\n🔧 Importando CPUs...")

# Buscar CPUs existentes
existing_cpus_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,code&project_id=eq.{PROJECT_ID}",
    headers=headers
)

existing_cpus = {}
if existing_cpus_response.status_code == 200:
    existing_cpus = {c['code']: c['id'] for c in existing_cpus_response.json()}
    print(f"  → {len(existing_cpus)} já cadastradas")

cpu_id_map = {}
cpu_imported = 0
cpu_skipped = 0

# Criar mapa de descrição → ID insumo (para vincular CPUs)
insumo_desc_map = {}
for codigo, insumo_id in insumo_id_map.items():
    # Buscar descrição original
    for ins in insumos_data:
        if ins['codigo'] == codigo:
            insumo_desc_map[ins['descricao']] = insumo_id
            break

for cpu in cpus_data:
    codigo = cpu['codigo']
    
    if codigo in existing_cpus:
        cpu_id_map[codigo] = existing_cpus[codigo]
        cpu_skipped += 1
        continue
    
    # unit_direct_cost_cents = custo_total * 100
    cost_cents = int(float(cpu['custo_total']) * 100)
    
    payload = {
        "code": codigo,
        "description": cpu['descricao'],
        "unit": cpu['unidade'],
        "unit_direct_cost_cents": cost_cents,
        "project_id": PROJECT_ID,
        "is_active": True,
        "budget_type": "executivo",
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/composicoes",
        headers=headers,
        json=payload
    )
    
    if response.status_code in [200, 201]:
        cpu_id = response.json()[0]['id']
        cpu_id_map[codigo] = cpu_id
        
        # Inserir insumos da CPU
        cpu_insumos = []
        for insumo in cpu.get('insumos', []):
            insumo_desc = insumo['descricao']
            if insumo_desc in insumo_desc_map:
                cpu_insumos.append({
                    "composicao_id": cpu_id,
                    "insumo_id": insumo_desc_map[insumo_desc],
                    "coefficient": insumo['quantidade'],
                    "created_at": datetime.utcnow().isoformat()
                })
        
        if cpu_insumos:
            insumos_response = requests.post(
                f"{SUPABASE_URL}/rest/v1/composicoes_items",
                headers=headers,
                json=cpu_insumos
            )
            if insumos_response.status_code not in [200, 201]:
                print(f"⚠️ Erro ao vincular insumos da CPU {codigo}")
        
        cpu_imported += 1
        if cpu_imported % 100 == 0:
            print(f"  → {cpu_imported} importadas...")
    else:
        print(f"⚠️ Erro na CPU {codigo}: {response.status_code}")

print(f"✅ {cpu_imported} novas, {cpu_skipped} reutilizadas")

# ============================================================
# 7. IMPORTAR EAP
# ============================================================
print(f"\n📋 Importando estrutura EAP...")

def import_eap_level(parent_id, items, level_name, sequence_start=0):
    """Importa recursivamente os níveis da EAP"""
    count = 0
    for idx, item in enumerate(items):
        payload = {
            "budget_id": budget_id,
            "parent_id": parent_id,
            "code": item['codigo'],
            "description": item['nome'],
            "level": level_name,
            "sequence": sequence_start + idx,
            "unit": "VB",
            "quantity": 0,
            "unit_price": 0,
            "total_price": 0,
            "is_leaf": False,
            "created_at": datetime.utcnow().isoformat()
        }
        
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json=payload
        )
        
        if response.status_code in [200, 201]:
            item_id = response.json()[0]['item_id']
            count += 1
            
            # Recursão
            if 'celulas' in item:
                count += import_eap_level(item_id, item['celulas'], 'celula')
            elif 'etapas' in item:
                count += import_eap_level(item_id, item['etapas'], 'etapa')
            elif 'subetapas' in item:
                count += import_eap_level(item_id, item['subetapas'], 'subetapa')
        else:
            print(f"⚠️ Erro {level_name} {item['codigo']}: {response.status_code}")
    
    return count

total_items = 0
for idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_payload = {
        "budget_id": budget_id,
        "parent_id": None,
        "code": uc['codigo'],
        "description": uc['nome'],
        "level": "unidade_construtiva",
        "sequence": idx,
        "unit": "VB",
        "quantity": 0,
        "unit_price": 0,
        "total_price": 0,
        "is_leaf": False,
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers,
        json=uc_payload
    )
    
    if response.status_code in [200, 201]:
        uc_id = response.json()[0]['item_id']
        total_items += 1
        total_items += import_eap_level(uc_id, uc['celulas'], 'celula')
        print(f"  → UC {uc['codigo']} importada")
    else:
        print(f"⚠️ Erro UC {uc['codigo']}: {response.status_code}")
        print(response.text)

print(f"✅ {total_items} itens EAP importados")

# ============================================================
# 8. RESUMO
# ============================================================
print("\n" + "="*60)
print("✅ IMPORTAÇÃO CONCLUÍDA!")
print("="*60)
print(f"📦 Insumos: {imported} novos")
print(f"🔧 CPUs: {cpu_imported} novas")
print(f"📋 Itens EAP: {total_items}")
print(f"\n🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
print("="*60)
