#!/usr/bin/env python3
"""
Corrigir tipos dos insumos importados
"""
import os, sys, json, requests
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
headers = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Carregar insumos do JSON
with open('executivo/thozen-electra/insumos.json', 'r') as f:
    insumos_data = json.load(f)

print(f"📦 {len(insumos_data)} insumos a verificar\n")

# Mapear grupo → tipo correto (trim espaços)
tipo_map = {
    "Serviço Terceiros": "servico",
    "Mão de obra": "mao_de_obra",
    "Equipamentos": "equipamento",
    # Todos os outros → material
}

def normalizar_grupo(texto):
    """Remove espaços extras"""
    return texto.strip() if texto else ""

def detectar_tipo(insumo):
    """Detecta o tipo correto do insumo"""
    grupo = normalizar_grupo(insumo.get('grupo', ''))
    subgrupo = normalizar_grupo(insumo.get('subgrupo', ''))
    descricao = insumo['descricao'].upper()
    
    # Por grupo
    if grupo in tipo_map:
        return tipo_map[grupo]
    
    # Por palavras-chave na descrição
    if any(kw in descricao for kw in ['PEDREIRO', 'SERVENTE', 'ENCARREGADO', 'MESTRE', 'OFICIAL', 'AJUDANTE']):
        return "mao_de_obra"
    
    if any(kw in descricao for kw in ['BETONEIRA', 'VIBRADOR', 'SERRA', 'GUINCHO', 'ANDAIME']):
        return "equipamento"
    
    # Default: material
    return "material"

# Agrupar insumos por tipo correto
updates_por_tipo = {}
for insumo in insumos_data:
    tipo_correto = detectar_tipo(insumo)
    if tipo_correto not in updates_por_tipo:
        updates_por_tipo[tipo_correto] = []
    updates_por_tipo[tipo_correto].append(insumo['codigo'])

print("📊 Distribuição por tipo:")
for tipo, codigos in updates_por_tipo.items():
    print(f"  {tipo}: {len(codigos)} insumos")
print()

# Atualizar em lote
for tipo, codigos in updates_por_tipo.items():
    print(f"🔧 Atualizando {len(codigos)} insumos para tipo '{tipo}'...", flush=True)
    
    # Processar em batches de 100
    batch_size = 100
    for i in range(0, len(codigos), batch_size):
        batch = codigos[i:i+batch_size]
        
        # Montar filtro: code.in.(code1,code2,...)
        codes_filter = ','.join(batch)
        
        response = requests.patch(
            f"{SUPABASE_URL}/rest/v1/insumos?code=in.({codes_filter})",
            headers=headers,
            json={"type": tipo},
            timeout=30
        )
        
        if response.status_code in [200, 204]:
            print(f"  ✅ Batch {i//batch_size + 1}/{(len(codigos)-1)//batch_size + 1}", flush=True)
        else:
            print(f"  ❌ Erro no batch: {response.status_code}\n{response.text}", flush=True)

print("\n✅ Tipos corrigidos!")
