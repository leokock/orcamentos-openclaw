#!/usr/bin/env python3
"""
Analisar estrutura correta de um orçamento no Memorial
para entender como importar a EAP corretamente
"""
import os, requests, json
from dotenv import load_dotenv

load_dotenv('.env.sensitive')

SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
ANON_KEY = os.getenv('MEMORIAL_SUPABASE_ANON')
EMAIL = os.getenv('MEMORIAL_EMAIL')
PASSWORD = os.getenv('MEMORIAL_PASSWORD')

# Autenticar
auth = requests.post(
    f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
    headers={"apikey": ANON_KEY, "Content-Type": "application/json"},
    json={"email": EMAIL, "password": PASSWORD},
    timeout=10
).json()

token = auth['access_token']
headers = {'apikey': ANON_KEY, 'Authorization': f'Bearer {token}'}

print("🔍 Analisando estrutura de orçamentos existentes...\n")

# 1. Buscar um orçamento que tenha itens
response = requests.get(
    f"{SUPABASE_URL}/rest/v1/budgets?select=budget_id,name,project_id&limit=10",
    headers=headers,
    timeout=10
)

budgets_data = response.json()
if isinstance(budgets_data, list):
    budgets = budgets_data
else:
    print(f"Erro: {budgets_data}")
    exit(1)

print(f"📊 {len(budgets)} orçamentos encontrados\n")

# Pegar o primeiro com itens
budget_with_items = None
for budget in budgets:
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/budget_items?select=item_id&budget_id=eq.{budget['budget_id']}",
        headers=headers,
        timeout=10
    )
    count = len(response.json())
    if count > 10:
        budget_with_items = budget
        print(f"✅ Orçamento selecionado: {budget['name']} ({count} itens)")
        break

if not budget_with_items:
    print("❌ Nenhum orçamento com itens encontrado")
    exit(1)

budget_id = budget_with_items['budget_id']

# 2. Analisar hierarquia completa
print(f"\n📋 Estrutura hierárquica:\n")

response = requests.get(
    f"{SUPABASE_URL}/rest/v1/budget_items?select=*&budget_id=eq.{budget_id}&order=code,sequence",
    headers=headers,
    timeout=10
)

items = response.json()

# Agrupar por level
by_level = {}
for item in items:
    level = item['level']
    if level not in by_level:
        by_level[level] = []
    by_level[level].append(item)

for level in sorted(by_level.keys()):
    items_at_level = by_level[level]
    print(f"Level {level}: {len(items_at_level)} itens")
    
    # Mostrar 3 exemplos
    for item in items_at_level[:3]:
        parent_info = ""
        if item['parent_id']:
            parent = next((i for i in items if i['item_id'] == item['parent_id']), None)
            if parent:
                parent_info = f" (parent: {parent['code']})"
        
        print(f"  - {item['code']}: {item['name'][:50]}{parent_info}")
    
    if len(items_at_level) > 3:
        print(f"  ... (+{len(items_at_level) - 3} itens)")
    print()

# 3. Analisar um item folha (subetapa)
print("\n🔍 Exemplo de item FOLHA (subetapa com CPU):\n")
leaf_items = [i for i in items if i.get('is_leaf') and i.get('composicao_id')]

if leaf_items:
    item = leaf_items[0]
    print(f"Code: {item['code']}")
    print(f"Name: {item['name']}")
    print(f"Level: {item['level']}")
    print(f"Parent ID: {item['parent_id']}")
    print(f"Composição ID: {item['composicao_id']}")
    print(f"Unit: {item.get('unit', 'N/A')}")
    print(f"Quantity: {item.get('quantity', 'N/A')}")
    print(f"Unit Price: {item.get('unit_price', 'N/A')}")
    print(f"Total Price: {item.get('total_price', 'N/A')}")
    print(f"Is Leaf: {item.get('is_leaf')}")
    print(f"Sequence: {item.get('sequence')}")
else:
    print("Nenhum item folha encontrado com CPU")

# 4. Verificar códigos duplicados
print("\n🔍 Verificando duplicações de código:\n")
codes = [i['code'] for i in items]
duplicates = [c for c in set(codes) if codes.count(c) > 1]

if duplicates:
    print(f"⚠️ {len(duplicates)} códigos duplicados:")
    for code in duplicates[:10]:
        matching = [i for i in items if i['code'] == code]
        print(f"  - '{code}': {len(matching)} ocorrências")
        for m in matching:
            print(f"    → Level {m['level']}: {m['name'][:40]}")
else:
    print("✅ Nenhum código duplicado")

# 5. Salvar estrutura completa
with open('output/memorial_structure_example.json', 'w') as f:
    json.dump({
        'budget': budget_with_items,
        'items': items[:50],  # Primeiros 50 itens
        'stats': {
            'total': len(items),
            'by_level': {str(k): len(v) for k, v in by_level.items()},
            'has_duplicates': len(duplicates) > 0
        }
    }, f, indent=2, ensure_ascii=False)

print(f"\n✅ Estrutura salva em output/memorial_structure_example.json")
