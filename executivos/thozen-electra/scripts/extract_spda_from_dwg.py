#!/usr/bin/env python3.11
"""
Extrator de quantitativos de SPDA a partir de arquivos DWG
Tentativa de leitura direta ou conversão para análise
"""

import os
import sys
from pathlib import Path

def analyze_spda_structure(dwg_files):
    """
    Analisa a estrutura do SPDA baseado nos nomes dos arquivos
    e na estrutura típica de edifícios
    """
    
    structure = {
        'pavimentos': [],
        'total_pavimentos': 0,
        'pavimentos_tipo': 0,
        'tem_casa_maquinas': False,
        'tem_lazer': False,
        'garagens': []
    }
    
    for dwg in dwg_files:
        filename = os.path.basename(dwg)
        
        if 'TÉRREO' in filename:
            structure['pavimentos'].append({'nivel': 'Térreo', 'tipo': 'terreo', 'arquivo': filename})
        elif 'G1' in filename:
            structure['pavimentos'].append({'nivel': '2º Pav G1', 'tipo': 'garagem', 'arquivo': filename})
            structure['garagens'].append('G1')
        elif 'G2' in filename:
            structure['pavimentos'].append({'nivel': '3º Pav G2', 'tipo': 'garagem', 'arquivo': filename})
            structure['garagens'].append('G2')
        elif 'G3' in filename:
            structure['pavimentos'].append({'nivel': '4º Pav G3', 'tipo': 'garagem', 'arquivo': filename})
            structure['garagens'].append('G3')
        elif 'G4' in filename:
            structure['pavimentos'].append({'nivel': '5º Pav G4', 'tipo': 'garagem', 'arquivo': filename})
            structure['garagens'].append('G4')
        elif 'G5' in filename:
            structure['pavimentos'].append({'nivel': '6º Pav G5', 'tipo': 'garagem', 'arquivo': filename})
            structure['garagens'].append('G5')
        elif 'LAZER' in filename:
            structure['pavimentos'].append({'nivel': '7º Pav Lazer', 'tipo': 'lazer', 'arquivo': filename})
            structure['tem_lazer'] = True
        elif '08º PAVTO. TIPO' in filename:
            structure['pavimentos'].append({'nivel': '8º Pav Tipo', 'tipo': 'tipo', 'arquivo': filename})
        elif '09º~31º' in filename and '23x' in filename:
            structure['pavimentos'].append({'nivel': '9º~31º Pav Tipo (23x)', 'tipo': 'tipo_repetido', 'repetições': 23, 'arquivo': filename})
            structure['pavimentos_tipo'] = 23
        elif 'CASA DE MÁQUINAS' in filename:
            structure['pavimentos'].append({'nivel': 'Casa de Máquinas', 'tipo': 'casa_maquinas', 'arquivo': filename})
            structure['tem_casa_maquinas'] = True
    
    structure['total_pavimentos'] = len(structure['pavimentos']) + structure['pavimentos_tipo'] - 1
    
    return structure

def estimate_spda_quantities(structure):
    """
    Estima quantitativos de SPDA baseado na estrutura do edifício
    e nas normas NBR 5419
    """
    
    # Altura estimada do edifício
    # Térreo + 5 garagens + Lazer + 24 tipos (1 + 23 repetições) + Casa de Máquinas = 32 pavimentos
    # Altura estimada: ~2.7m pé-direito garagem, ~2.5m pé-direito tipo, ~4m casa de máquinas
    altura_estimada = (5 * 2.7) + (24 * 2.5) + 4 + 3  # térreo ~3m
    
    # Número de descidas (conforme NBR 5419 - mínimo 2 descidas para edifícios)
    # Regra geral: 1 descida a cada 20m de perímetro, mas vamos assumir estrutura retangular típica
    # Para edifício de ~80-100m de altura, geralmente 4-6 descidas
    num_descidas = 4  # Estimativa conservadora
    
    # Captores no topo
    # Tipo Franklin (hastes) ou gaiola de Faraday
    # Para cobertura plana típica de ~400m², múltiplos captores tipo Franklin
    num_captores_franklin = 6  # Estimativa
    
    # Hastes de aterramento
    # Mínimo 1 por descida, geralmente 2-3 por descida
    num_hastes_aterramento = num_descidas * 2
    
    # Cabo de descida
    # Cabo de cobre nu 35mm² ou 50mm² (NBR 5419)
    metragem_cabo_descida = num_descidas * altura_estimada * 1.1  # +10% para trajeto não linear
    
    # Cabo de interligação (anéis equipotenciais)
    # Anel a cada 20m de altura ou a cada 4-5 pavimentos
    num_aneis = int(altura_estimada / 20) + 1
    perimetro_estimado = 120  # metros (edifício retangular típico)
    metragem_cabo_anel = num_aneis * perimetro_estimado
    
    # Malha de aterramento
    # Malha horizontal + hastes verticais
    area_malha = 200  # m² estimado
    
    # Conexões e acessórios
    num_conexoes = num_descidas * 30  # ~30 conexões por descida
    num_caixas_inspecao = num_descidas * 2  # 2 caixas por descida
    
    quantities = {
        'captores': {
            'captor_franklin': {'qtd': num_captores_franklin, 'un': 'un', 'spec': 'Captor tipo Franklin, h=0.6m, aço inox'},
        },
        'descidas': {
            'cabo_descida': {'qtd': round(metragem_cabo_descida, 1), 'un': 'm', 'spec': 'Cabo de cobre nu 50mm²'},
            'num_descidas': num_descidas,
        },
        'aterramento': {
            'hastes': {'qtd': num_hastes_aterramento, 'un': 'un', 'spec': 'Haste cobreada 5/8" x 2.4m'},
            'malha_cabo': {'qtd': area_malha * 5, 'un': 'm', 'spec': 'Cabo de cobre nu 50mm² (malha)'},
        },
        'equipotencializacao': {
            'cabo_anel': {'qtd': round(metragem_cabo_anel, 1), 'un': 'm', 'spec': 'Cabo de cobre nu 35mm² (anéis equipotenciais)'},
            'num_aneis': num_aneis,
        },
        'conexoes': {
            'conector_parafuso': {'qtd': num_conexoes, 'un': 'un', 'spec': 'Conector parafuso fendido bronze'},
            'caixa_inspecao': {'qtd': num_caixas_inspecao, 'un': 'un', 'spec': 'Caixa de inspeção 300x300mm'},
        },
        'premissas': {
            'altura_edificio': round(altura_estimada, 1),
            'num_descidas': num_descidas,
            'num_aneis': num_aneis,
            'num_pavimentos': structure['total_pavimentos'],
        }
    }
    
    return quantities

if __name__ == '__main__':
    dwg_path = 'projetos/thozen-electra/projetos/11 SPDA/DWG/'
    dwg_files = [os.path.join(dwg_path, f) for f in os.listdir(dwg_path) if f.endswith('.dwg')]
    dwg_files.sort()
    
    print("=== ANÁLISE ESTRUTURA SPDA - THOZEN ELECTRA ===\n")
    
    structure = analyze_spda_structure(dwg_files)
    
    print(f"Total de pavimentos: {structure['total_pavimentos']}")
    print(f"Pavimentos tipo (repetidos): {structure['pavimentos_tipo']}")
    print(f"Garagens: {len(structure['garagens'])}")
    print(f"Tem lazer: {structure['tem_lazer']}")
    print(f"Tem casa de máquinas: {structure['tem_casa_maquinas']}")
    print("\nPavimentos identificados:")
    for pav in structure['pavimentos']:
        rep = f" ({pav['repetições']}x)" if 'repetições' in pav else ""
        print(f"  - {pav['nivel']}{rep}")
    
    print("\n=== QUANTITATIVOS ESTIMADOS ===\n")
    
    quantities = estimate_spda_quantities(structure)
    
    print("PREMISSAS:")
    print(f"  - Altura estimada do edifício: {quantities['premissas']['altura_edificio']}m")
    print(f"  - Número de descidas: {quantities['premissas']['num_descidas']}")
    print(f"  - Número de anéis equipotenciais: {quantities['premissas']['num_aneis']}")
    print(f"  - Total de pavimentos: {quantities['premissas']['num_pavimentos']}")
    
    print("\nCAPTORES:")
    for item, data in quantities['captores'].items():
        print(f"  - {data['spec']}: {data['qtd']} {data['un']}")
    
    print("\nDESCIDAS:")
    for item, data in quantities['descidas'].items():
        if isinstance(data, dict):
            print(f"  - {data['spec']}: {data['qtd']} {data['un']}")
    
    print("\nATERRAMENTO:")
    for item, data in quantities['aterramento'].items():
        print(f"  - {data['spec']}: {data['qtd']} {data['un']}")
    
    print("\nEQUIPOTENCIALIZAÇÃO:")
    for item, data in quantities['equipotencializacao'].items():
        if isinstance(data, dict):
            print(f"  - {data['spec']}: {data['qtd']} {data['un']}")
    
    print("\nCONEXÕES E ACESSÓRIOS:")
    for item, data in quantities['conexoes'].items():
        print(f"  - {data['spec']}: {data['qtd']} {data['un']}")
    
    print("\n⚠️  ATENÇÃO: Quantitativos ESTIMADOS baseados em premissas típicas.")
    print("    Para quantitativos precisos, é necessário processar os arquivos DWG.")
