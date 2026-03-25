#!/usr/bin/env python3
"""
Descobre o schema real das tabelas do Supabase do Memorial
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

# Autenticar
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)

token = auth_response.json().get('access_token')
headers = {"apikey": ANON_KEY, "Authorization": f"Bearer {token}"}

# Tabelas a investigar
tables = ['budgets', 'budget_items', 'composicoes', 'composicoes_items', 'insumos', 'project_towers']

print("🔍 Descobrindo schema das tabelas...\n")

for table in tables:
    print(f"📋 {table}")
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/{table}?select=*&limit=1",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json()
        if data:
            fields = list(data[0].keys())
            print(f"   Campos: {', '.join(fields)}")
        else:
            print(f"   (tabela vazia)")
    else:
        print(f"   ❌ Erro {response.status_code}: {response.text[:100]}")
    print()
