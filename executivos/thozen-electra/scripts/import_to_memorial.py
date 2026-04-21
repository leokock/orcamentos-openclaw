#!/usr/bin/env python3
"""
Script de importação de dados do Electra Towers para o Memorial Cartesiano
"""
import json
import os
import requests
from datetime import datetime

# Carregar credenciais
SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
SUPABASE_ANON = os.getenv('MEMORIAL_SUPABASE_ANON')
MEMORIAL_EMAIL = os.getenv('MEMORIAL_EMAIL')
MEMORIAL_PASSWORD = os.getenv('MEMORIAL_PASSWORD')

PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"

def get_auth_token():
    """Autenticar e obter JWT"""
    response = requests.post(
        f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
        headers={
            "apikey": SUPABASE_ANON,
            "Content-Type": "application/json"
        },
        json={
            "email": MEMORIAL_EMAIL,
            "password": MEMORIAL_PASSWORD
        }
    )
    response.raise_for_status()
    return response.json()['access_token']

def import_insumos(token, insumos_data):
    """Importar insumos para a tabela insumos"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    print(f"📦 Importando {len(insumos_data)} insumos...")
    
    # Primeiro, verificar quais insumos já existem
    existing_response = requests.get(
        f"{SUPABASE_URL}/rest/v1/insumos?select=descricao,id",
        headers=headers
    )
    existing_insumos = {item['descricao']: item['id'] for item in existing_response.json()}
    
    insumos_map = {}  # Mapear descrição -> ID (para usar nas CPUs depois)
    new_count = 0
    
    for insumo in insumos_data:
        descricao = insumo['descricao']
        
        if descricao in existing_insumos:
            insumos_map[descricao] = existing_insumos[descricao]
            continue
        
        # Inserir novo insumo
        payload = {
            "descricao": descricao,
            "unidade": insumo['unidade'],
            "preco_base": float(insumo['custo_unitario']),
            "grupo": insumo.get('grupo'),
            "subgrupo": insumo.get('subgrupo'),
            "tipo": "material"  # ou "mao_de_obra", "equipamento"
        }
        
        try:
            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/insumos",
                headers=headers,
                json=payload
            )
            if response.status_code in [200, 201]:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    insumos_map[descricao] = result[0]['id']
                    new_count += 1
            else:
                print(f"⚠️ Erro ao inserir insumo '{descricao}': {response.status_code} - {response.text}")
        except Exception as e:
            print(f"⚠️ Exceção ao inserir insumo '{descricao}': {e}")
    
    print(f"✅ {new_count} insumos novos inseridos, {len(existing_insumos)} já existiam")
    return insumos_map

def import_composicoes(token, cpus_data, insumos_map):
    """Importar composições (CPUs) e seus insumos"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    print(f"🏗️ Importando {len(cpus_data)} composições...")
    
    # Verificar composições existentes
    existing_response = requests.get(
        f"{SUPABASE_URL}/rest/v1/composicoes?select=descricao,id&project_id=eq.{PROJECT_ID}",
        headers=headers
    )
    existing_cpus = {item['descricao']: item['id'] for item in existing_response.json()}
    
    new_count = 0
    
    for cpu in cpus_data:
        descricao = cpu['descricao']
        
        if descricao in existing_cpus:
            continue
        
        # Inserir nova composição
        payload = {
            "project_id": PROJECT_ID,
            "codigo": cpu.get('codigo', descricao[:20]),
            "descricao": descricao,
            "unidade": cpu['unidade'],
            "custo_total": float(cpu.get('custo_total', 0))
        }
        
        try:
            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/composicoes",
                headers=headers,
                json=payload
            )
            
            if response.status_code not in [200, 201]:
                print(f"⚠️ Erro ao inserir CPU '{descricao}': {response.status_code}")
                continue
            
            result = response.json()
            if not isinstance(result, list) or len(result) == 0:
                continue
                
            cpu_id = result[0]['id']
            new_count += 1
            
            # Inserir insumos da composição
            for insumo_item in cpu.get('insumos', []):
                insumo_desc = insumo_item['descricao']
                insumo_id = insumos_map.get(insumo_desc)
                
                if not insumo_id:
                    continue
                
                item_payload = {
                    "composicao_id": cpu_id,
                    "insumo_id": insumo_id,
                    "quantidade": float(insumo_item.get('quantidade', 1)),
                    "custo_unitario": float(insumo_item.get('custo_unitario', 0))
                }
                
                requests.post(
                    f"{SUPABASE_URL}/rest/v1/composicoes_items",
                    headers=headers,
                    json=item_payload
                )
        
        except Exception as e:
            print(f"⚠️ Exceção ao inserir CPU '{descricao}': {e}")
    
    print(f"✅ {new_count} composições novas inseridas, {len(existing_cpus)} já existiam")

def main():
    print("🚀 Iniciando importação para Memorial Cartesiano - Electra Towers")
    print("=" * 70)
    
    # Autenticar
    print("🔐 Autenticando...")
    token = get_auth_token()
    print("✅ Token obtido")
    
    # Carregar dados
    print("\n📂 Carregando dados locais...")
    with open('insumos.json', 'r') as f:
        insumos_data = json.load(f)
    
    with open('cpus.json', 'r') as f:
        cpus_data = json.load(f)
    
    print(f"   - {len(insumos_data)} insumos carregados")
    print(f"   - {len(cpus_data)} composições carregadas")
    
    # Importar em ordem
    print("\n" + "=" * 70)
    insumos_map = import_insumos(token, insumos_data)
    
    print("\n" + "=" * 70)
    import_composicoes(token, cpus_data, insumos_map)
    
    print("\n" + "=" * 70)
    print("✅ Importação concluída!")

if __name__ == '__main__':
    main()
