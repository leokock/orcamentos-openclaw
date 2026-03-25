#!/usr/bin/env python3
import os, requests
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
headers = {"apikey": ANON_KEY, "Authorization": f"Bearer {token}"}

# Buscar 1 insumo qualquer para ver o type
response = requests.get(
    f"{SUPABASE_URL}/rest/v1/insumos?select=*&limit=1",
    headers=headers,
    timeout=10
)

import json
print(json.dumps(response.json(), indent=2))
