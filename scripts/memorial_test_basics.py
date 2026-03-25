#!/usr/bin/env python3
"""Teste básico de criação de torre e orçamento"""
import os, sys, json, requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')
PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"

print("🔐 Autenticando...")
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD}
)
token = auth_response.json().get('access_token')
print(f"✅ Token obtido")

headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# Buscar torres
print("\n🏗️ Buscando torres...")
towers = requests.get(
    f"{SUPABASE_URL}/rest/v1/project_towers?select=*&project_id=eq.{PROJECT_ID}",
    headers=headers
).json()

if not towers:
    print("⚠️ Criando torre Embasamento...")
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/project_towers",
        headers=headers,
        json={"project_id": PROJECT_ID, "tower_name": "Embasamento", "tower_number": 1}
    )
    if response.status_code in [200, 201]:
        tower_id = response.json()[0]['tower_id']
        print(f"✅ Torre criada: {tower_id}")
    else:
        print(f"❌ Erro: {response.status_code}\n{response.text}")
        sys.exit(1)
else:
    tower_id = towers[0]['tower_id']
    print(f"✅ Torre existente: {tower_id}")

# Buscar orçamento
print("\n💰 Buscando orçamento...")
budgets = requests.get(
    f"{SUPABASE_URL}/rest/v1/budgets?select=*&project_id=eq.{PROJECT_ID}",
    headers=headers
).json()

if not budgets:
    print("⚠️ Criando orçamento...")
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/budgets",
        headers=headers,
        json={
            "project_id": PROJECT_ID,
            "tower_id": tower_id,
            "name": "Orçamento Executivo - Electra Towers",
            "status": "draft",
            "budget_type": "executivo"
        }
    )
    if response.status_code in [200, 201]:
        budget_id = response.json()[0]['budget_id']
        print(f"✅ Orçamento criado: {budget_id}")
    else:
        print(f"❌ Erro: {response.status_code}\n{response.text}")
        sys.exit(1)
else:
    budget_id = budgets[0]['budget_id']
    print(f"✅ Orçamento existente: {budget_id}")

print(f"\n✅ Pronto! Torre: {tower_id}, Orçamento: {budget_id}")
