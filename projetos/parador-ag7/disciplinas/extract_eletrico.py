#!/usr/bin/env python3
"""
Extrai quantitativos elétricos de arquivos DWG/DXF do projeto Parador AG7
"""

import ezdxf
import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Configurações
DWG_DIR = Path.home() / "Library/CloudStorage/GoogleDrive-leonardo@cartesianengenharia.com/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/AG7 Incorporadora/Arquivos recebidos/2026.03.10 - Projetos Autodoc/15. Eletrico/04. Executivo/DWG"
OUTPUT_FILE = Path.home() / "orcamentos/projetos/parador-ag7/disciplinas/eletrico.json"

# Padrões para identificação
PATTERNS = {
    'eletroduto': re.compile(r'(?:eletroduto|conduite|tubulação).*?(\d+).*?mm', re.IGNORECASE),
    'cabo': re.compile(r'cabo.*?(\d+(?:,\d+)?)\s*mm', re.IGNORECASE),
    'tomada': re.compile(r'tomada|TUG|ponto.*?tomada', re.IGNORECASE),
    'luz': re.compile(r'luz|iluminação|TUE|ponto.*?luz', re.IGNORECASE),
    'quadro': re.compile(r'quadro|QD|painel.*?elétrico', re.IGNORECASE),
}

def extract_text_from_entity(entity):
    """Extrai texto de uma entidade DXF"""
    try:
        if entity.dxftype() == 'TEXT':
            return entity.dxf.text
        elif entity.dxftype() == 'MTEXT':
            return entity.text
        elif entity.dxftype() == 'ATTRIB':
            return entity.dxf.text
    except:
        pass
    return None

def analyze_dwg(file_path):
    """Analisa um arquivo DWG e extrai quantitativos"""
    print(f"Processando: {file_path.name}")
    
    result = {
        'arquivo': file_path.name,
        'eletrodutos': defaultdict(float),
        'cabos': defaultdict(int),
        'pontos_luz': 0,
        'pontos_tomada': 0,
        'quadros': []
    }
    
    try:
        # Tenta ler o arquivo
        try:
            doc = ezdxf.readfile(str(file_path))
        except ezdxf.DXFError:
            print(f"  ⚠️  Não foi possível ler {file_path.name} - pode ser formato DWG nativo")
            return None
            
        msp = doc.modelspace()
        
        # Processa todas as entidades
        for entity in msp:
            # Extrai texto
            text = extract_text_from_entity(entity)
            if not text:
                continue
                
            text = text.strip()
            
            # Identifica eletrodutos
            match = PATTERNS['eletroduto'].search(text)
            if match:
                diametro = match.group(1)
                # Tenta extrair comprimento da linha
                if entity.dxftype() in ['LINE', 'POLYLINE', 'LWPOLYLINE']:
                    try:
                        length = entity.dxf.length if hasattr(entity.dxf, 'length') else 0
                        result['eletrodutos'][f"{diametro}mm"] += length
                    except:
                        result['eletrodutos'][f"{diametro}mm"] += 1  # Conta como ponto
            
            # Identifica cabos
            match = PATTERNS['cabo'].search(text)
            if match:
                secao = match.group(1)
                result['cabos'][f"{secao}mm²"] += 1
            
            # Identifica pontos de luz
            if PATTERNS['luz'].search(text):
                result['pontos_luz'] += 1
            
            # Identifica pontos de tomada
            if PATTERNS['tomada'].search(text):
                result['pontos_tomada'] += 1
            
            # Identifica quadros
            if PATTERNS['quadro'].search(text):
                result['quadros'].append(text[:50])  # Limita a 50 chars
        
        return result
        
    except Exception as e:
        print(f"  ❌ Erro ao processar {file_path.name}: {e}")
        return None

def consolidate_results(all_results):
    """Consolida os resultados de todos os arquivos"""
    
    consolidated = {
        'eletrodutos': defaultdict(float),
        'cabos': defaultdict(int),
        'pontos_luz': 0,
        'pontos_tomada': 0,
        'quadros': set()
    }
    
    for result in all_results:
        if not result:
            continue
            
        # Soma eletrodutos
        for diametro, comprimento in result['eletrodutos'].items():
            consolidated['eletrodutos'][diametro] += comprimento
        
        # Soma cabos
        for secao, quantidade in result['cabos'].items():
            consolidated['cabos'][secao] += quantidade
        
        # Soma pontos
        consolidated['pontos_luz'] += result['pontos_luz']
        consolidated['pontos_tomada'] += result['pontos_tomada']
        
        # Adiciona quadros (sem duplicatas)
        consolidated['quadros'].update(result['quadros'])
    
    return consolidated

def main():
    print("=" * 60)
    print("EXTRAÇÃO DE QUANTITATIVOS ELÉTRICOS - PARADOR AG7")
    print("=" * 60)
    print()
    
    # Lista todos os arquivos DWG (sem duplicados _1)
    dwg_files = [f for f in DWG_DIR.glob("*.dwg") if not f.name.endswith("_1.dwg")]
    print(f"Encontrados {len(dwg_files)} arquivos DWG para processar\n")
    
    # Processa cada arquivo
    all_results = []
    for dwg_file in sorted(dwg_files):
        result = analyze_dwg(dwg_file)
        if result:
            all_results.append(result)
    
    print(f"\n✅ Processados {len(all_results)} arquivos com sucesso\n")
    
    # Consolida resultados
    consolidated = consolidate_results(all_results)
    
    # Prepara output JSON
    output = {
        "disciplina": "Elétrico",
        "fonte": "15. Eletrico/04. Executivo",
        "data_extracao": "2026-03-11",
        "total_arquivos_processados": len(all_results),
        "categorias": [
            {
                "nome": "Eletrodutos",
                "items": [
                    {"descricao": diametro, "quantidade": round(comprimento, 2), "unidade": "m"}
                    for diametro, comprimento in sorted(consolidated['eletrodutos'].items())
                ]
            },
            {
                "nome": "Cabos e Condutores",
                "items": [
                    {"descricao": secao, "quantidade": quantidade, "unidade": "un"}
                    for secao, quantidade in sorted(consolidated['cabos'].items())
                ]
            },
            {
                "nome": "Pontos de Luz",
                "items": [
                    {"descricao": "Ponto de iluminação", "quantidade": consolidated['pontos_luz'], "unidade": "un"}
                ]
            },
            {
                "nome": "Pontos de Tomada",
                "items": [
                    {"descricao": "Ponto de tomada", "quantidade": consolidated['pontos_tomada'], "unidade": "un"}
                ]
            },
            {
                "nome": "Quadros Elétricos",
                "items": [
                    {"descricao": quadro, "quantidade": 1, "unidade": "un"}
                    for quadro in sorted(consolidated['quadros'])
                ]
            }
        ]
    }
    
    # Garante que o diretório existe
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Salva JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print("=" * 60)
    print("RESUMO DOS QUANTITATIVOS")
    print("=" * 60)
    print(f"\n📁 Eletrodutos:")
    for diametro, comprimento in sorted(consolidated['eletrodutos'].items()):
        print(f"   • {diametro}: {comprimento:.2f} m")
    
    print(f"\n🔌 Cabos:")
    for secao, quantidade in sorted(consolidated['cabos'].items()):
        print(f"   • {secao}: {quantidade} un")
    
    print(f"\n💡 Pontos de Luz: {consolidated['pontos_luz']}")
    print(f"🔌 Pontos de Tomada: {consolidated['pontos_tomada']}")
    print(f"📊 Quadros Elétricos: {len(consolidated['quadros'])}")
    
    print(f"\n✅ Arquivo salvo em: {OUTPUT_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    main()
