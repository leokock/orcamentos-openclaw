#!/usr/bin/env python3
"""
Corrigir escopo dos 835 insumos importados: global → catálogo do cliente Thozen
Seguindo o guia: memorial-import-scoping.md
"""
import os, sys, json, requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

CLIENT_ID = "2297582c-660c-45c8-9c3a-84aea1b5ac01"  # Thozen

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
    "Content-Type": "application/json"
}
print("✅ Autenticado\n", flush=True)

# Carregar códigos dos insumos importados
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)

codigos = [ins['codigo'] for ins in insumos_data]
print(f"📦 {len(codigos)} insumos a mover para catálogo do cliente Thozen\n", flush=True)

# Verificar duplicatas antes de mover (importante!)
print("🔍 Verificando duplicatas no catálogo do cliente...", flush=True)
response = requests.get(
    f"{SUPABASE_URL}/rest/v1/insumos?select=code&client_id=eq.{CLIENT_ID}&project_id=is.null",
    headers=headers,
    timeout=30
)

codigos_existentes = {i['code'] for i in response.json()}
duplicatas = set(codigos) & codigos_existentes

if duplicatas:
    print(f"⚠️ {len(duplicatas)} códigos já existem no catálogo do cliente!", flush=True)
    print(f"   Exemplos: {list(duplicatas)[:5]}", flush=True)
    print("\n❌ Abortando para evitar conflitos.", flush=True)
    print("   Solução: renomear duplicatas antes de mover.\n", flush=True)
    sys.exit(1)

print("✅ Nenhuma duplicata encontrada\n", flush=True)

# Atualizar em batches de 100
# SQL: UPDATE insumos SET client_id = '...', source = 'catalog', project_id = null WHERE code IN (...)
batch_size = 100
total_atualizados = 0

for i in range(0, len(codigos), batch_size):
    batch = codigos[i:i+batch_size]
    
    # Filtro: code.in.(INS_00001,INS_00002,...)
    codes_filter = ','.join(batch)
    
    print(f"🔧 Batch {i//batch_size + 1}/{(len(codigos)-1)//batch_size + 1} ({len(batch)} insumos)...", flush=True)
    
    response = requests.patch(
        f"{SUPABASE_URL}/rest/v1/insumos?code=in.({codes_filter})&client_id=is.null&project_id=is.null&origin_system=eq.import",
        headers=headers,
        json={
            "client_id": CLIENT_ID,
            "source": "catalog",
            "project_id": None,
            "updated_at": datetime.utcnow().isoformat()
        },
        timeout=30
    )
    
    if response.status_code in [200, 204]:
        total_atualizados += len(batch)
        print(f"  ✅ {total_atualizados}/{len(codigos)}", flush=True)
    else:
        print(f"  ⚠️ Erro: {response.status_code}", flush=True)
        print(f"  {response.text[:300]}", flush=True)

print(f"\n{'='*60}")
print(f"✅ {total_atualizados} insumos movidos para catálogo do cliente Thozen!")
print(f"{'='*60}")
print(f"\nVerificação:")
print(f"  SELECT count(*) FROM insumos")
print(f"  WHERE client_id = '{CLIENT_ID}' AND project_id IS NULL;")
print(f"\n🔗 https://cliente.cartesianengenharia.com/admin/projects/cdff0592-fb3c-4c13-9516-efde6b56b336")
