#!/usr/bin/env python3
"""
Duplicar os 835 insumos do catálogo global para o projeto Thozen
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

# Autenticar
print("🔐 Autenticando...", flush=True)
auth = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD},
    timeout=10
).json()

token = auth['access_token']
headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}
print("✅ Autenticado\n", flush=True)

# Carregar insumos do JSON
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)

print(f"📦 {len(insumos_data)} insumos a duplicar para o projeto Thozen\n", flush=True)

# Detectar tipo correto (copiar lógica do script anterior)
def normalizar_grupo(texto):
    return texto.strip() if texto else ""

tipo_map = {
    "Serviço Terceiros": "servico",
    "Mão de obra": "mao_de_obra",
    "Equipamentos": "equipamento",
}

def detectar_tipo(insumo):
    grupo = normalizar_grupo(insumo.get('grupo', ''))
    descricao = insumo['descricao'].upper()
    
    if grupo in tipo_map:
        return tipo_map[grupo]
    
    if any(kw in descricao for kw in ['PEDREIRO', 'SERVENTE', 'ENCARREGADO', 'MESTRE', 'OFICIAL', 'AJUDANTE']):
        return "mao_de_obra"
    
    if any(kw in descricao for kw in ['BETONEIRA', 'VIBRADOR', 'SERRA', 'GUINCHO', 'ANDAIME']):
        return "equipamento"
    
    return "material"

# Inserir em batches de 50
batch_size = 50
total_criados = 0
batch = []

for i, insumo in enumerate(insumos_data):
    batch.append({
        "code": insumo['codigo'],
        "description": insumo['descricao'],
        "type": detectar_tipo(insumo),
        "unit": insumo['unidade'],
        "price_cents": int(float(insumo['custo_unitario']) * 100),
        "project_id": PROJECT_ID,
        "client_id": CLIENT_ID,
        "is_active": True,
        "budget_type": "executivo",
        "origin_system": "import",
        "source": "planilha_executivo"
    })
    
    if len(batch) >= batch_size:
        print(f"🔧 Inserindo batch {(i//batch_size)+1}/{(len(insumos_data)-1)//batch_size + 1}...", flush=True)
        
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/insumos",
            headers=headers,
            json=batch,
            timeout=30
        )
        
        if response.status_code in [200, 201]:
            total_criados += len(batch)
            print(f"  ✅ {total_criados}/{len(insumos_data)}", flush=True)
        else:
            print(f"  ⚠️ Erro: {response.status_code}", flush=True)
            print(f"  {response.text[:200]}", flush=True)
            # Tentar inserir 1 por 1 neste batch
            for item in batch:
                r = requests.post(
                    f"{SUPABASE_URL}/rest/v1/insumos",
                    headers=headers,
                    json=item,
                    timeout=10
                )
                if r.status_code in [200, 201]:
                    total_criados += 1
        
        batch = []

# Último batch
if batch:
    print(f"🔧 Inserindo último batch...", flush=True)
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/insumos",
        headers=headers,
        json=batch,
        timeout=30
    )
    if response.status_code in [200, 201]:
        total_criados += len(batch)

print(f"\n✅ {total_criados} insumos criados para o projeto Thozen!")
print(f"🔗 https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
