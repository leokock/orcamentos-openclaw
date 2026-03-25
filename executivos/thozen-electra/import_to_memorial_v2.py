#!/usr/bin/env python3
"""
Script de importação de dados do Electra Towers para o Memorial Cartesiano
Versão 2: com batches, retry e melhor tratamento de erros
"""
import json
import os
import requests
from time import sleep

# Configurações
SUPABASE_URL = os.getenv('MEMORIAL_SUPABASE_URL')
SUPABASE_ANON = os.getenv('MEMORIAL_SUPABASE_ANON')
MEMORIAL_EMAIL = os.getenv('MEMORIAL_EMAIL')
MEMORIAL_PASSWORD = os.getenv('MEMORIAL_PASSWORD')

PROJECT_ID = "cdff0592-fb3c-4c13-9516-efde6b56b336"
BATCH_SIZE = 50  # Processar em lotes de 50
TIMEOUT = 30  # Timeout de 30s por request

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
        },
        timeout=TIMEOUT
    )
    response.raise_for_status()
    return response.json()['access_token']

def safe_request(method, url, headers, **kwargs):
    """Request com retry e tratamento de erros"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            kwargs['timeout'] = TIMEOUT
            response = requests.request(method, url, headers=headers, **kwargs)
            return response
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                print(f"   ⏳ Timeout, tentando novamente ({attempt + 1}/{max_retries})...")
                sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                print(f"   ⚠️ Erro de conexão, tentando novamente ({attempt + 1}/{max_retries})...")
                sleep(2 ** attempt)
            else:
                raise

def import_insumos_batch(token, batch_insumos, existing_insumos):
    """Importar um lote de insumos"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    insumos_map = {}
    new_count = 0
    
    for insumo in batch_insumos:
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
            "tipo": "material"
        }
        
        try:
            response = safe_request(
                'POST',
                f"{SUPABASE_URL}/rest/v1/insumos",
                headers=headers,
                json=payload
            )
            
            if response.status_code in [200, 201]:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    insumos_map[descricao] = result[0]['id']
                    existing_insumos[descricao] = result[0]['id']
                    new_count += 1
        except Exception as e:
            print(f"   ⚠️ Erro ao inserir '{descricao[:50]}...': {e}")
    
    return insumos_map, new_count

def import_insumos(token, insumos_data):
    """Importar insumos em batches"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}"
    }
    
    print(f"📦 Importando {len(insumos_data)} insumos em lotes de {BATCH_SIZE}...")
    
    # Buscar insumos existentes
    print("   Buscando insumos existentes...")
    try:
        existing_response = safe_request(
            'GET',
            f"{SUPABASE_URL}/rest/v1/insumos?select=descricao,id",
            headers=headers
        )
        existing_insumos = {item['descricao']: item['id'] for item in existing_response.json()}
        print(f"   ✅ {len(existing_insumos)} insumos já existem no sistema")
    except Exception as e:
        print(f"   ⚠️ Erro ao buscar insumos existentes: {e}")
        existing_insumos = {}
    
    # Processar em batches
    total_new = 0
    all_insumos_map = {}
    
    for i in range(0, len(insumos_data), BATCH_SIZE):
        batch = insumos_data[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (len(insumos_data) + BATCH_SIZE - 1) // BATCH_SIZE
        
        print(f"   Processando lote {batch_num}/{total_batches}...")
        batch_map, batch_new = import_insumos_batch(token, batch, existing_insumos)
        
        all_insumos_map.update(batch_map)
        total_new += batch_new
        
        if batch_new > 0:
            print(f"      ✅ {batch_new} novos inseridos neste lote")
        
        sleep(0.5)  # Pequeno delay entre batches
    
    print(f"✅ Total: {total_new} insumos novos inseridos")
    return all_insumos_map

def import_composicoes_batch(token, batch_cpus, insumos_map, existing_cpus):
    """Importar um lote de composições"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    new_count = 0
    
    for cpu in batch_cpus:
        descricao = cpu['descricao']
        
        if descricao in existing_cpus:
            continue
        
        payload = {
            "project_id": PROJECT_ID,
            "codigo": cpu.get('codigo', descricao[:20]),
            "descricao": descricao,
            "unidade": cpu['unidade'],
            "custo_total": float(cpu.get('custo_total', 0))
        }
        
        try:
            response = safe_request(
                'POST',
                f"{SUPABASE_URL}/rest/v1/composicoes",
                headers=headers,
                json=payload
            )
            
            if response.status_code not in [200, 201]:
                continue
            
            result = response.json()
            if not isinstance(result, list) or len(result) == 0:
                continue
            
            cpu_id = result[0]['id']
            existing_cpus[descricao] = cpu_id
            new_count += 1
            
            # Inserir insumos da composição (limitando a 20 por CPU pra não travar)
            for insumo_item in cpu.get('insumos', [])[:20]:
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
                
                safe_request(
                    'POST',
                    f"{SUPABASE_URL}/rest/v1/composicoes_items",
                    headers=headers,
                    json=item_payload
                )
        
        except Exception as e:
            print(f"   ⚠️ Erro ao inserir CPU '{descricao[:50]}...': {e}")
    
    return new_count

def import_composicoes(token, cpus_data, insumos_map):
    """Importar composições em batches"""
    headers = {
        "apikey": SUPABASE_ANON,
        "Authorization": f"Bearer {token}"
    }
    
    print(f"🏗️ Importando {len(cpus_data)} composições em lotes de {BATCH_SIZE}...")
    
    # Buscar CPUs existentes
    print("   Buscando composições existentes...")
    try:
        existing_response = safe_request(
            'GET',
            f"{SUPABASE_URL}/rest/v1/composicoes?select=descricao,id&project_id=eq.{PROJECT_ID}",
            headers=headers
        )
        existing_cpus = {item['descricao']: item['id'] for item in existing_response.json()}
        print(f"   ✅ {len(existing_cpus)} composições já existem no projeto")
    except Exception as e:
        print(f"   ⚠️ Erro ao buscar composições existentes: {e}")
        existing_cpus = {}
    
    # Processar em batches
    total_new = 0
    
    for i in range(0, len(cpus_data), BATCH_SIZE):
        batch = cpus_data[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (len(cpus_data) + BATCH_SIZE - 1) // BATCH_SIZE
        
        print(f"   Processando lote {batch_num}/{total_batches}...")
        batch_new = import_composicoes_batch(token, batch, insumos_map, existing_cpus)
        
        total_new += batch_new
        
        if batch_new > 0:
            print(f"      ✅ {batch_new} novas inseridas neste lote")
        
        sleep(0.5)
    
    print(f"✅ Total: {total_new} composições novas inseridas")

def main():
    print("🚀 Importação para Memorial Cartesiano - Electra Towers")
    print("=" * 70)
    
    # Autenticar
    print("🔐 Autenticando...")
    try:
        token = get_auth_token()
        print("✅ Token obtido")
    except Exception as e:
        print(f"❌ Erro na autenticação: {e}")
        return
    
    # Carregar dados
    print("\n📂 Carregando dados locais...")
    try:
        with open('insumos.json', 'r') as f:
            insumos_data = json.load(f)
        
        with open('cpus.json', 'r') as f:
            cpus_data = json.load(f)
        
        print(f"   - {len(insumos_data)} insumos carregados")
        print(f"   - {len(cpus_data)} composições carregadas")
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return
    
    # Importar
    print("\n" + "=" * 70)
    try:
        insumos_map = import_insumos(token, insumos_data)
        print(f"   📌 {len(insumos_map)} insumos mapeados")
    except Exception as e:
        print(f"❌ Erro ao importar insumos: {e}")
        return
    
    print("\n" + "=" * 70)
    try:
        import_composicoes(token, cpus_data, insumos_map)
    except Exception as e:
        print(f"❌ Erro ao importar composições: {e}")
        return
    
    print("\n" + "=" * 70)
    print("✅ Importação concluída!")

if __name__ == '__main__':
    main()
