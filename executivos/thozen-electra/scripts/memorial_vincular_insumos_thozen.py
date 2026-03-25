#!/usr/bin/env python3
"""
Vincular os 835 insumos importados ao projeto Thozen Electra
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
    "Content-Type": "application/json"
}
print("✅ Autenticado\n", flush=True)

# Carregar códigos dos insumos importados
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)

codigos = [ins['codigo'] for ins in insumos_data]
print(f"📦 {len(codigos)} insumos a vincular ao projeto Thozen\n", flush=True)

# Atualizar em batches de 100
batch_size = 100
total_atualizados = 0

for i in range(0, len(codigos), batch_size):
    batch = codigos[i:i+batch_size]
    
    # Filtro: code.in.(INS_00001,INS_00002,...)
    codes_filter = ','.join(batch)
    
    print(f"🔧 Batch {i//batch_size + 1}/{(len(codigos)-1)//batch_size + 1} ({len(batch)} insumos)...", flush=True)
    
    response = requests.patch(
        f"{SUPABASE_URL}/rest/v1/insumos?code=in.({codes_filter})",
        headers=headers,
        json={
            "project_id": PROJECT_ID,
            "client_id": CLIENT_ID,
            "source": "planilha_executivo"  # Marcar origem
        },
        timeout=30
    )
    
    if response.status_code in [200, 204]:
        total_atualizados += len(batch)
        print(f"  ✅ {total_atualizados}/{len(codigos)}", flush=True)
    else:
        print(f"  ❌ Erro: {response.status_code}", flush=True)
        print(f"  {response.text[:200]}", flush=True)

print(f"\n✅ {total_atualizados} insumos vinculados ao projeto Thozen!")
print(f"🔗 Verifique em: https://cliente.cartesianengenharia.com/admin/projects/{PROJECT_ID}")
