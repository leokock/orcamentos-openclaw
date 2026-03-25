#!/usr/bin/env python3
"""
Teste de autenticação e listagem de projetos no Memorial Cartesiano (Supabase)
"""
import os
import sys
import json
import requests
from dotenv import load_dotenv

# Carregar .env.sensitive
load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

if not all([SUPABASE_URL, ANON_KEY, EMAIL, PASSWORD]):
    print("❌ Erro: Variáveis de ambiente não encontradas em .env.sensitive", file=sys.stderr)
    sys.exit(1)

# 1. Autenticar e obter JWT
print("🔐 Autenticando...")
auth_response = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={
        "apikey": ANON_KEY,
        "Content-Type": "application/json"
    },
    json={
        "email": EMAIL,
        "password": PASSWORD
    }
)

if auth_response.status_code != 200:
    print(f"❌ Erro na autenticação: {auth_response.status_code}", file=sys.stderr)
    print(auth_response.text, file=sys.stderr)
    sys.exit(1)

auth_data = auth_response.json()
token = auth_data.get('access_token')
print(f"✅ Token obtido: {token[:50]}...")

# 2. Listar projetos (sem especificar colunas para ver o schema)
print("\n📋 Listando projetos...")
projects_response = requests.get(
    f"{SUPABASE_URL}/rest/v1/projects?select=*&order=created_at.desc&limit=5",
    headers={
        "apikey": ANON_KEY,
        "Authorization": f"Bearer {token}"
    }
)

if projects_response.status_code != 200:
    print(f"❌ Erro ao listar projetos: {projects_response.status_code}", file=sys.stderr)
    print(projects_response.text, file=sys.stderr)
    sys.exit(1)

projects = projects_response.json()
print(f"✅ {len(projects)} projetos encontrados:\n")

# Debug: ver estrutura do primeiro projeto
if projects:
    print("🔍 Campos disponíveis no projeto:", list(projects[0].keys()))
    print()

for p in projects:
    # Tentar vários campos possíveis
    nome = p.get('name') or p.get('project_name') or p.get('title') or 'Sem nome'
    print(f"  • {nome} (ID: {p['id'][:8]}...)")

# 3. Procurar projeto "Electra" ou "Thozen"
print("\n🔍 Procurando projeto Electra/Thozen...")
nome_field = 'name' if 'name' in projects[0] else 'project_name' if 'project_name' in projects[0] else 'title'
electra_projects = [p for p in projects if 'electra' in str(p.get(nome_field, '')).lower() or 'thozen' in str(p.get(nome_field, '')).lower()]

if electra_projects:
    print(f"✅ {len(electra_projects)} projeto(s) encontrado(s):")
    for p in electra_projects:
        nome = p.get(nome_field, 'Sem nome')
        print(f"  • {nome} (ID: {p['id']})")
else:
    print("⚠️ Nenhum projeto Electra/Thozen encontrado — precisamos criar!")

# Salvar token para uso posterior
with open('output/memorial_token.txt', 'w') as f:
    f.write(token)
print("\n💾 Token salvo em output/memorial_token.txt")
