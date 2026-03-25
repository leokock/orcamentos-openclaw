#!/usr/bin/env python3
"""Teste de importação de 1 insumo para debug"""
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
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD},
    timeout=10
)
token = auth_response.json().get('access_token')
print("✅ Autenticado")

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Carregar 1 insumo de teste
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)

insumo = insumos_data[0]
print(f"\n📦 Testando insumo: {insumo['descricao']}")

payload = {
    "code": insumo['codigo'],
    "description": insumo['descricao'],
    "type": "material",
    "unit": insumo['unidade'],
    "price_cents": int(float(insumo['custo_unitario']) * 100),
    "is_active": True,
    "budget_type": "executivo",
    "origin_system": "import",
    "source": "catalog"  # Insumos globais do catálogo
}

print(f"\n📤 Payload:")
print(json.dumps(payload, indent=2))

response = requests.post(
    f"{SUPABASE_URL}/rest/v1/insumos",
    headers=headers,
    json=payload,
    timeout=10
)

print(f"\n📥 Response status: {response.status_code}")
print(f"📥 Response body:")
print(response.text)

if response.status_code in [200, 201]:
    print("\n✅ Sucesso!")
else:
    print("\n❌ Erro!")
