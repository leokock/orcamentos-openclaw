#!/usr/bin/env python3
"""
Importação do orçamento executivo Thozen Electra no Memorial Cartesiano via Supabase
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

if not all([SUPABASE_URL, ANON_KEY, EMAIL, PASSWORD]):
    print("❌ Erro: Variáveis de ambiente não encontradas em .env.sensitive", file=sys.stderr)
    sys.exit(1)

# ============================================================
# 1. AUTENTICAÇÃO
# ============================================================
print("🔐 Autenticando no Supabase...")
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)

if auth_response.status_code != 200:
    print(f"❌ Erro na autenticação: {auth_response.status_code}", file=sys.stderr)
    print(auth_response.text, file=sys.stderr)
    sys.exit(1)

token = auth_response.json().get('access_token')
print(f"✅ Autenticado com sucesso")

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
print(f"✅ Insumos: {len(insumos_data)} itens")

with open('executivo/thozen-electra/cpus.json', 'r') as f:
    cpus_data = json.load(f)
print(f"✅ CPUs: {len(cpus_data)} composições")

with open('executivo/thozen-electra/eap.json', 'r') as f:
    eap_data = json.load(f)
print(f"✅ EAP: {len(eap_data['unidades_construtivas'])} UCs")

# ============================================================
# 3. VERIFICAR TORRES DO PROJETO (OPCIONAL - PULANDO POR ENQUANTO)
# ============================================================
print("\n🏗️ Torres: pulando verificação por enquanto (pode ser configurado depois no Memorial)")
default_tower_id = None

# ============================================================
# 4. CRIAR OU BUSCAR ORÇAMENTO
# ============================================================
print("\n💰 Verificando orçamento do projeto...")
budgets_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/budgets?select=*&project_id=eq.{PROJECT_ID}",
    headers=headers
)

if budgets_response.status_code != 200:
    print(f"❌ Erro ao buscar orçamentos: {budgets_response.status_code}", file=sys.stderr)
    sys.exit(1)

existing_budgets = budgets_response.json()

if not existing_budgets:
    print("⚠️ Nenhum orçamento encontrado — criando novo...")
    budget_payload = {
        "project_id": PROJECT_ID,
        "name": "Orçamento Executivo - Thozen Electra",
        "description": "Orçamento importado de planilha executiva R00",
        "created_at": datetime.utcnow().isoformat()
    }
    budget_response = requests.post(
        f"{SUPABASE_URL}/rest/v1/budgets",
        headers=headers,
        json=budget_payload
    )
    if budget_response.status_code in [200, 201]:
        budget_id = budget_response.json()[0]['id']
        print(f"✅ Orçamento criado: ID {budget_id}")
    else:
        print(f"❌ Erro ao criar orçamento: {budget_response.status_code}", file=sys.stderr)
        print(budget_response.text, file=sys.stderr)
        sys.exit(1)
else:
    budget_id = existing_budgets[0]['id']
    print(f"✅ Orçamento existente: ID {budget_id}")

# ============================================================
# 5. IMPORTAR INSUMOS
# ============================================================
print(f"\n📦 Importando {len(insumos_data)} insumos...")

# Verificar insumos existentes para evitar duplicatas
existing_insumos_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/insumos?select=id,code,description",
    headers=headers
)

if existing_insumos_response.status_code == 200:
    existing_insumos = {i['code']: i['id'] for i in existing_insumos_response.json()}
    print(f"✅ {len(existing_insumos)} insumos já cadastrados na base")
else:
    existing_insumos = {}
    print("⚠️ Não foi possível buscar insumos existentes — continuando sem validação de duplicatas")

insumo_id_map = {}  # Mapear código → ID do Supabase
imported_count = 0
skipped_count = 0

for insumo in insumos_data:
    codigo = insumo['codigo']
    
    # Se já existe, reutilizar ID
    if codigo in existing_insumos:
        insumo_id_map[codigo] = existing_insumos[codigo]
        skipped_count += 1
        continue
    
    # Inserir novo insumo
    insumo_payload = {
        "code": codigo,
        "description": insumo['descricao'],
        "unit": insumo['unidade'],
        "unit_price": insumo['custo_unitario'],
        "category": insumo.get('grupo', 'Sem grupo'),
        "subcategory": insumo.get('subgrupo', ''),
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/insumos",
        headers=headers,
        json=insumo_payload
    )
    
    if response.status_code in [200, 201]:
        insumo_id = response.json()[0]['id']
        insumo_id_map[codigo] = insumo_id
        imported_count += 1
        if imported_count % 50 == 0:
            print(f"  → {imported_count} insumos importados...")
    else:
        print(f"⚠️ Erro ao importar insumo {codigo}: {response.status_code}", file=sys.stderr)

print(f"✅ Insumos importados: {imported_count} novos, {skipped_count} reutilizados")

# ============================================================
# 6. IMPORTAR CPUs (COMPOSIÇÕES)
# ============================================================
print(f"\n🔧 Importando {len(cpus_data)} CPUs...")

existing_cpus_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/composicoes?select=id,code",
    headers=headers
)

if existing_cpus_response.status_code == 200:
    existing_cpus = {c['code']: c['id'] for c in existing_cpus_response.json()}
    print(f"✅ {len(existing_cpus)} CPUs já cadastradas na base")
else:
    existing_cpus = {}

cpu_id_map = {}
cpu_imported = 0
cpu_skipped = 0

for cpu in cpus_data:
    codigo = cpu['codigo']
    
    # Se já existe, reutilizar
    if codigo in existing_cpus:
        cpu_id_map[codigo] = existing_cpus[codigo]
        cpu_skipped += 1
        continue
    
    # Inserir nova CPU
    cpu_payload = {
        "code": codigo,
        "description": cpu['descricao'],
        "unit": cpu['unidade'],
        "total_cost": cpu['custo_total'],
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/composicoes",
        headers=headers,
        json=cpu_payload
    )
    
    if response.status_code in [200, 201]:
        cpu_id = response.json()[0]['id']
        cpu_id_map[codigo] = cpu_id
        
        # Inserir insumos da CPU
        cpu_insumos = []
        for insumo in cpu.get('insumos', []):
            # Buscar ID do insumo (pela descrição, pois código pode não bater)
            insumo_desc = insumo['descricao']
            insumo_id = None
            
            # Tentar achar por descrição exata
            for ins_codigo, ins_id in insumo_id_map.items():
                if insumos_data[[i for i, x in enumerate(insumos_data) if x['codigo'] == ins_codigo][0]]['descricao'] == insumo_desc:
                    insumo_id = ins_id
                    break
            
            if not insumo_id:
                # Insumo não encontrado — pular
                continue
            
            cpu_insumos.append({
                "composicao_id": cpu_id,
                "insumo_id": insumo_id,
                "quantity": insumo['quantidade'],
                "unit_cost": insumo['custo_unitario'],
                "total_cost": insumo['custo_total']
            })
        
        # Inserir insumos em batch
        if cpu_insumos:
            insumos_response = requests.post(
                f"{SUPABASE_URL}/rest/v1/composicoes_items",
                headers=headers,
                json=cpu_insumos
            )
            if insumos_response.status_code not in [200, 201]:
                print(f"⚠️ Erro ao importar insumos da CPU {codigo}: {insumos_response.status_code}")
        
        cpu_imported += 1
        if cpu_imported % 50 == 0:
            print(f"  → {cpu_imported} CPUs importadas...")
    else:
        print(f"⚠️ Erro ao importar CPU {codigo}: {response.status_code}")

print(f"✅ CPUs importadas: {cpu_imported} novas, {cpu_skipped} reutilizadas")

# ============================================================
# 7. IMPORTAR EAP (ESTRUTURA DE ORÇAMENTO)
# ============================================================
print(f"\n📋 Importando estrutura EAP...")

def import_eap_level(parent_id, items, level_name):
    """Importa recursivamente os níveis da EAP"""
    count = 0
    for item in items:
        payload = {
            "budget_id": budget_id,
            "parent_id": parent_id,
            "code": item['codigo'],
            "description": item['nome'],
            "level": level_name,
            "unit": "VB",  # Verba (padrão para itens de EAP sem quantidade)
            "quantity": 0,
            "unit_price": 0,
            "total_price": 0,
            "created_at": datetime.utcnow().isoformat()
        }
        
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json=payload
        )
        
        if response.status_code in [200, 201]:
            item_id = response.json()[0]['id']
            count += 1
            
            # Recursão para níveis filhos
            if 'celulas' in item:
                count += import_eap_level(item_id, item['celulas'], 'celula')
            elif 'etapas' in item:
                count += import_eap_level(item_id, item['etapas'], 'etapa')
            elif 'subetapas' in item:
                count += import_eap_level(item_id, item['subetapas'], 'subetapa')
        else:
            print(f"⚠️ Erro ao importar {level_name} {item['codigo']}: {response.status_code}")
    
    return count

# Importar UCs (raiz)
total_items = 0
for uc in eap_data['unidades_construtivas']:
    uc_payload = {
        "budget_id": budget_id,
        "parent_id": None,
        "code": uc['codigo'],
        "description": uc['nome'],
        "level": "unidade_construtiva",
        "unit": "VB",
        "quantity": 0,
        "unit_price": 0,
        "total_price": 0,
        "created_at": datetime.utcnow().isoformat()
    }
    
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/budget_items",
        headers=headers,
        json=uc_payload
    )
    
    if response.status_code in [200, 201]:
        uc_id = response.json()[0]['id']
        total_items += 1
        
        # Importar células
        total_items += import_eap_level(uc_id, uc['celulas'], 'celula')
        
        print(f"  → UC {uc['codigo']} importada")
    else:
        print(f"⚠️ Erro ao importar UC {uc['codigo']}: {response.status_code}")

print(f"✅ EAP completa importada: {total_items} itens")

# ============================================================
# 8. RESUMO FINAL
# ============================================================
print("\n" + "="*60)
print("✅ IMPORTAÇÃO CONCLUÍDA COM SUCESSO!")
print("="*60)
print(f"📦 Insumos: {imported_count} novos, {skipped_count} reutilizados")
print(f"🔧 CPUs: {cpu_imported} novas, {cpu_skipped} reutilizadas")
print(f"📋 Itens EAP: {total_items}")
print(f"🏗️ Projeto: {PROJECT_ID}")
print(f"💰 Orçamento: {budget_id}")
print("="*60)
print(f"\n🔗 Acesse: https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
