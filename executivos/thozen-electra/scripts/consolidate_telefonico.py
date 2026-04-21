#!/usr/bin/env python3.11
"""
Consolida dados extraídos de IFC e gera quantitativos por tipo
Projeto: Thozen Electra - Instalações Telefônicas
"""

import json
import re
from collections import defaultdict
from pathlib import Path

def load_raw_data():
    """Carrega dados brutos do JSON"""
    with open('output/thozen-electra-telefonico-raw.json', 'r') as f:
        return json.load(f)

def classify_element(element):
    """Classifica elemento com base em nome, tipo e propriedades"""
    nome = element.get('nome', '').upper()
    obj_type = element.get('object_type', '').upper()
    desc = element.get('descricao', '') or ''
    desc = str(desc).upper()
    
    # Texto de busca unificado
    search = f"{nome} {obj_type} {desc}"
    
    # Classificações por palavras-chave
    if 'RJ45' in search or 'RJ-45' in search:
        return 'PONTO_DADOS', extract_description(element)
    
    if 'RJ11' in search or 'RJ-11' in search:
        return 'PONTO_VOZ', extract_description(element)
    
    if 'CAIXA' in search and '4X4' in search:
        return 'CAIXA_4X4', extract_description(element)
    
    if 'CAIXA' in search and '4X2' in search:
        return 'CAIXA_4X2', extract_description(element)
    
    if 'CAIXA' in search and 'SOBREPOR' in search:
        return 'CAIXA_SOBREPOR', extract_description(element)
    
    if 'PLACA' in search:
        if 'CEGA' in search:
            return 'PLACA_CEGA', extract_description(element)
        elif '4X4' in search:
            return 'PLACA_4X4', extract_description(element)
        elif '4X2' in search:
            return 'PLACA_4X2', extract_description(element)
        else:
            return 'PLACA', extract_description(element)
    
    if 'SUPORTE' in search and 'CAIXA' in search:
        if '4X4' in search:
            return 'SUPORTE_4X4', extract_description(element)
        elif '4X2' in search:
            return 'SUPORTE_4X2', extract_description(element)
    
    if 'MÓDULO' in search or 'MODULO' in search:
        if 'RJ45' in search:
            return 'MODULO_RJ45', extract_description(element)
        elif 'RJ11' in search:
            return 'MODULO_RJ11', extract_description(element)
        else:
            return 'MODULO', extract_description(element)
    
    if 'CONECTOR' in search:
        if 'RJ45' in search:
            return 'CONECTOR_RJ45', extract_description(element)
        elif 'RJ11' in search:
            return 'CONECTOR_RJ11', extract_description(element)
    
    if 'ELETRODUTO' in search or 'CONDUITE' in search:
        diameter = extract_diameter(search)
        return 'ELETRODUTO', f"Eletroduto {diameter}" if diameter else extract_description(element)
    
    if 'ELETROCALHA' in search or 'CALHA' in search:
        dims = extract_dimensions(search)
        return 'CALHA', f"Calha {dims}" if dims else extract_description(element)
    
    if 'CABO' in search or 'CABEAMENTO' in search:
        if 'CAT6A' in search or 'CAT 6A' in search:
            return 'CABO_CAT6A', extract_description(element)
        elif 'CAT6' in search or 'CAT 6' in search:
            return 'CABO_CAT6', extract_description(element)
        elif 'CAT5E' in search or 'CAT 5E' in search:
            return 'CABO_CAT5E', extract_description(element)
        else:
            return 'CABO', extract_description(element)
    
    if 'RACK' in search:
        return 'RACK', extract_description(element)
    
    if 'PATCH PANEL' in search or 'PATCH-PANEL' in search:
        return 'PATCH_PANEL', extract_description(element)
    
    if 'QUADRO' in search or 'DG' in search or 'DISTRIBUIDOR' in search:
        return 'QUADRO_TELECOM', extract_description(element)
    
    if 'SWITCH' in search or 'HUB' in search:
        return 'SWITCH', extract_description(element)
    
    # Outros não classificados
    return 'OUTROS', extract_description(element)

def extract_description(element):
    """Extrai descrição legível do elemento"""
    nome = element.get('nome', '')
    obj_type = element.get('object_type', '')
    
    # Tentar extrair tipo de família (formato "Familia:Tipo:ID")
    if ':' in nome:
        parts = nome.split(':')
        if len(parts) >= 2:
            familia = parts[0]
            tipo = parts[1]
            return f"{familia} - {tipo}"
    
    # Tentar obj_type
    if ':' in obj_type:
        parts = obj_type.split(':')
        if len(parts) >= 2:
            return f"{parts[0]} - {parts[1]}"
    
    # Fallback
    return nome or obj_type or 'N/A'

def extract_diameter(text):
    """Extrai diâmetro de eletroduto"""
    match = re.search(r'(\d+)\s*MM', text)
    if match:
        return f"Ø{match.group(1)}mm"
    return None

def extract_dimensions(text):
    """Extrai dimensões de calha"""
    match = re.search(r'(\d+)\s*[Xx]\s*(\d+)', text)
    if match:
        return f"{match.group(1)}x{match.group(2)}mm"
    return None

def consolidate_by_floor(data):
    """Consolida dados por pavimento e tipo"""
    consolidated = {}
    
    for floor_data in data:
        pavimento = floor_data['pavimento']
        if pavimento == 'N/A':
            # Tentar extrair do nome do arquivo
            arquivo = floor_data['arquivo']
            if 'TÉRREO' in arquivo or 'T01' in arquivo:
                pavimento = 'TÉRREO'
            elif 'G1' in arquivo or 'T02' in arquivo:
                pavimento = 'G1 (2º PAVTO)'
            elif 'G2' in arquivo or 'T03' in arquivo:
                pavimento = 'G2 (3º PAVTO)'
            elif 'G3' in arquivo or 'T04' in arquivo:
                pavimento = 'G3 (4º PAVTO)'
            elif 'G4' in arquivo or 'T05' in arquivo:
                pavimento = 'G4 (5º PAVTO)'
            elif 'G5' in arquivo or 'T06' in arquivo:
                pavimento = 'G5 (6º PAVTO)'
            elif 'LAZER' in arquivo or 'T07' in arquivo:
                pavimento = 'LAZER (7º PAVTO)'
            elif 'TIPO' in arquivo or 'T08' in arquivo:
                pavimento = 'TIPO (8º~31º PAVTO - 24x)'
            elif 'MÁQUINAS' in arquivo or 'T09' in arquivo:
                pavimento = 'CASA DE MÁQUINAS'
        
        if pavimento not in consolidated:
            consolidated[pavimento] = {
                'arquivo': floor_data['arquivo'],
                'categorias': defaultdict(lambda: defaultdict(int)),
                'elementos': defaultdict(list)
            }
        
        # Processar todos os elementos
        all_elements = (
            floor_data.get('pontos_logicos', []) +
            floor_data.get('cabos', []) +
            floor_data.get('eletrodutos', []) +
            floor_data.get('calhas', []) +
            floor_data.get('quadros', []) +
            floor_data.get('racks', []) +
            floor_data.get('patch_panels', []) +
            floor_data.get('tomadas_rj45', []) +
            floor_data.get('equipamentos', [])
        )
        
        for element in all_elements:
            categoria, descricao = classify_element(element)
            consolidated[pavimento]['categorias'][categoria][descricao] += 1
            consolidated[pavimento]['elementos'][categoria].append({
                'descricao': descricao,
                'tag': element.get('tag', 'N/A'),
                'guid': element.get('guid', 'N/A')
            })
    
    return consolidated

def generate_summary(consolidated):
    """Gera resumo por categoria"""
    summary = defaultdict(lambda: defaultdict(int))
    
    for pavimento, data in consolidated.items():
        for categoria, items in data['categorias'].items():
            for desc, qty in items.items():
                summary[categoria][desc] += qty
    
    return summary

def print_report(consolidated, summary):
    """Imprime relatório consolidado"""
    print("\n" + "="*80)
    print("RELATÓRIO CONSOLIDADO - INSTALAÇÕES TELEFÔNICAS/LÓGICAS")
    print("Projeto: Thozen Electra")
    print("="*80 + "\n")
    
    # Resumo geral
    print("📊 RESUMO GERAL\n")
    
    for categoria in sorted(summary.keys()):
        items = summary[categoria]
        total = sum(items.values())
        print(f"\n{categoria.replace('_', ' ')} - Total: {total} unidades")
        print("-" * 60)
        for desc, qty in sorted(items.items(), key=lambda x: -x[1]):
            print(f"  {desc:<50} {qty:>5} un")
    
    print("\n" + "="*80)
    print("📋 QUANTITATIVOS POR PAVIMENTO")
    print("="*80 + "\n")
    
    # Ordem dos pavimentos
    ordem_pavimentos = [
        'TÉRREO',
        'G1 (2º PAVTO)',
        'G2 (3º PAVTO)',
        'G3 (4º PAVTO)',
        'G4 (5º PAVTO)',
        'G5 (6º PAVTO)',
        'LAZER (7º PAVTO)',
        'TIPO (8º~31º PAVTO - 24x)',
        'CASA DE MÁQUINAS'
    ]
    
    for pavimento in ordem_pavimentos:
        if pavimento not in consolidated:
            continue
        
        data = consolidated[pavimento]
        print(f"\n▸ {pavimento}")
        print(f"  Arquivo: {data['arquivo']}")
        print()
        
        for categoria in sorted(data['categorias'].keys()):
            items = data['categorias'][categoria]
            total = sum(items.values())
            print(f"  {categoria.replace('_', ' ')}: {total} un")
            for desc, qty in sorted(items.items(), key=lambda x: -x[1])[:5]:  # Top 5
                print(f"    • {desc[:45]:<45} {qty:>3} un")
        print()

def save_detailed_json(consolidated, summary):
    """Salva JSON detalhado"""
    output = {
        'projeto': 'Thozen Electra - Instalações Telefônicas',
        'data_extracao': '2026-03-20',
        'resumo_geral': {cat: dict(items) for cat, items in summary.items()},
        'por_pavimento': {}
    }
    
    for pavimento, data in consolidated.items():
        output['por_pavimento'][pavimento] = {
            'arquivo': data['arquivo'],
            'quantitativos': {cat: dict(items) for cat, items in data['categorias'].items()}
        }
    
    with open('output/thozen-electra-telefonico-consolidado.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print("\n✅ Dados consolidados salvos em: output/thozen-electra-telefonico-consolidado.json")

def main():
    print("⚙️  Carregando dados brutos...")
    data = load_raw_data()
    
    print("🔄 Consolidando por pavimento...")
    consolidated = consolidate_by_floor(data)
    
    print("📊 Gerando resumo...")
    summary = generate_summary(consolidated)
    
    # Imprimir relatório
    print_report(consolidated, summary)
    
    # Salvar JSON
    save_detailed_json(consolidated, summary)

if __name__ == '__main__':
    main()
