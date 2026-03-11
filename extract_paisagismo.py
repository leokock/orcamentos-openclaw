#!/usr/bin/env python3
"""
Extrai quantitativos da disciplina Paisagismo do projeto Parador AG7
"""

import ezdxf
import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Diretório dos DWGs
DWG_DIR = Path.home() / "Library/CloudStorage/GoogleDrive-leonardo@cartesianengenharia.com/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/AG7 Incorporadora/Arquivos recebidos/2026.03.10 - Projetos Autodoc/24. Paisagismo/04. Executivo/DWG"

# Arquivos principais (sem duplicatas)
ARQUIVOS_PRINCIPAIS = [
    "PAR-PAI-EX-0010-IM-IMP-R01.dwg",  # Implantação versão mais recente
    "PAR-PAI-EX-0020-IM-IMP-R00.dwg",  # Implantação
    "PAR-PAI-EX-0030-IM-IMP-R00.dwg",  # Implantação
    "PAR-PAI-EX-0040-TO-DUI-R00.dwg",  # Detalhe irrigação
    "PAR-PAI-EX-0050-TO-COBE-R00.dwg", # Detalhe cobertura
    "PAR-PAI-EX-0060-TO-N01-R00.dwg",  # Detalhe técnico
    "PAR-PAI-EX-0070-TO-COBE-R00.dwg", # Detalhe cobertura
    "PAR-PAI-EX-0110-IM-IMP-R00.dwg",  # Implantação
    "PAR-PAI-EX-1001-BA-COR-R00.dwg"   # Banco de dados/cortes
]

def extrair_textos_dwg(dwg_path):
    """Extrai todos os textos do DWG (TEXT, MTEXT, ATTRIB)"""
    textos = []
    try:
        doc = ezdxf.readfile(dwg_path)
        msp = doc.modelspace()
        
        # TEXT entities
        for text in msp.query('TEXT'):
            if text.dxf.text.strip():
                textos.append({
                    'tipo': 'TEXT',
                    'texto': text.dxf.text.strip(),
                    'layer': text.dxf.layer
                })
        
        # MTEXT entities
        for mtext in msp.query('MTEXT'):
            if mtext.text.strip():
                textos.append({
                    'tipo': 'MTEXT',
                    'texto': mtext.text.strip(),
                    'layer': mtext.dxf.layer
                })
        
        # ATTRIB in INSERT (blocos com atributos)
        for insert in msp.query('INSERT'):
            if insert.has_attrib:
                for attrib in insert.attribs:
                    if attrib.dxf.text.strip():
                        textos.append({
                            'tipo': 'ATTRIB',
                            'texto': attrib.dxf.text.strip(),
                            'layer': attrib.dxf.layer,
                            'tag': attrib.dxf.tag,
                            'bloco': insert.dxf.name
                        })
        
    except Exception as e:
        print(f"Erro ao ler {dwg_path.name}: {e}")
    
    return textos

def contar_blocos(dwg_path):
    """Conta blocos (mudas, elementos decorativos)"""
    blocos = defaultdict(int)
    try:
        doc = ezdxf.readfile(dwg_path)
        msp = doc.modelspace()
        
        for insert in msp.query('INSERT'):
            nome_bloco = insert.dxf.name
            blocos[nome_bloco] += 1
            
    except Exception as e:
        print(f"Erro ao contar blocos em {dwg_path.name}: {e}")
    
    return dict(blocos)

def extrair_quantitativos():
    """Extrai quantitativos de paisagismo"""
    
    dados = {
        "disciplina": "Paisagismo",
        "fonte": "24. Paisagismo/04. Executivo",
        "data_extracao": "2026-03-11",
        "arquivos_processados": [],
        "categorias": [
            {"nome": "Plantio", "items": []},
            {"nome": "Irrigação", "items": []},
            {"nome": "Pisos Externos", "items": []},
            {"nome": "Elementos Decorativos", "items": []}
        ]
    }
    
    # Processar cada arquivo
    for arquivo in ARQUIVOS_PRINCIPAIS:
        dwg_path = DWG_DIR / arquivo
        
        if not dwg_path.exists():
            print(f"Arquivo não encontrado: {arquivo}")
            continue
            
        print(f"\nProcessando: {arquivo}")
        dados["arquivos_processados"].append(arquivo)
        
        # Extrair textos
        textos = extrair_textos_dwg(dwg_path)
        print(f"  - {len(textos)} textos encontrados")
        
        # Contar blocos
        blocos = contar_blocos(dwg_path)
        print(f"  - {len(blocos)} tipos de blocos encontrados")
        
        # Analisar conteúdo
        for texto_info in textos:
            texto = texto_info['texto'].upper()
            layer = texto_info.get('layer', '').upper()
            
            # Identificar mudas/plantas
            if any(palavra in texto for palavra in ['MUDA', 'PLANTA', 'ÁRVORE', 'PALMEIRA', 'ARBUSTO', 'FORRAÇÃO']):
                # Tentar extrair quantidade
                match = re.search(r'(\d+)\s*(?:UN|UND|UNID)', texto)
                qtd = int(match.group(1)) if match else 1
                
                item = {
                    "descricao": texto_info['texto'],
                    "quantidade": qtd,
                    "unidade": "UN",
                    "fonte": arquivo,
                    "layer": layer
                }
                
                # Adicionar na categoria correta
                if not any(i['descricao'] == item['descricao'] for i in dados["categorias"][0]["items"]):
                    dados["categorias"][0]["items"].append(item)
            
            # Identificar irrigação
            if any(palavra in texto for palavra in ['IRRIGAÇÃO', 'GOTEJADOR', 'ASPERSOR', 'TUBULAÇÃO', 'MANGUEIRA']):
                match = re.search(r'(\d+(?:,\d+)?)\s*(?:M|ML|METROS)', texto)
                qtd = float(match.group(1).replace(',', '.')) if match else 0
                
                if qtd > 0 or 'IRRIGAÇÃO' in layer:
                    item = {
                        "descricao": texto_info['texto'],
                        "quantidade": qtd if qtd > 0 else None,
                        "unidade": "m" if qtd > 0 else None,
                        "fonte": arquivo,
                        "layer": layer
                    }
                    
                    if not any(i['descricao'] == item['descricao'] for i in dados["categorias"][1]["items"]):
                        dados["categorias"][1]["items"].append(item)
            
            # Identificar pisos/pavimentação
            if any(palavra in texto for palavra in ['PISO', 'PAVIMENTO', 'DECK', 'CONCRETO', 'PEDRA', 'GRAMA']):
                match = re.search(r'(\d+(?:,\d+)?)\s*(?:M2|M²|M^2)', texto)
                qtd = float(match.group(1).replace(',', '.')) if match else 0
                
                if qtd > 0 or 'PISO' in layer:
                    item = {
                        "descricao": texto_info['texto'],
                        "quantidade": qtd if qtd > 0 else None,
                        "unidade": "m²" if qtd > 0 else None,
                        "fonte": arquivo,
                        "layer": layer
                    }
                    
                    if not any(i['descricao'] == item['descricao'] for i in dados["categorias"][2]["items"]):
                        dados["categorias"][2]["items"].append(item)
        
        # Analisar blocos para elementos decorativos e mudas
        for nome_bloco, quantidade in blocos.items():
            # Ignorar blocos técnicos
            if any(x in nome_bloco.upper() for x in ['XREF', 'VIEWPORT', 'TITLE', '_FRAME']):
                continue
            
            # Elementos decorativos (bancos, luminárias, etc)
            if any(palavra in nome_bloco.upper() for palavra in ['BANCO', 'LUMINARIA', 'LIXEIRA', 'FONTE', 'ESCULTURA', 'BICICLETARIO']):
                item = {
                    "descricao": nome_bloco,
                    "quantidade": quantidade,
                    "unidade": "UN",
                    "fonte": arquivo,
                    "tipo": "bloco"
                }
                
                if not any(i['descricao'] == item['descricao'] for i in dados["categorias"][3]["items"]):
                    dados["categorias"][3]["items"].append(item)
            
            # Mudas (se estiver em bloco)
            elif any(palavra in nome_bloco.upper() for palavra in ['MUDA', 'PLANTA', 'ARVORE', 'PALMEIRA']):
                item = {
                    "descricao": nome_bloco,
                    "quantidade": quantidade,
                    "unidade": "UN",
                    "fonte": arquivo,
                    "tipo": "bloco"
                }
                
                if not any(i['descricao'] == item['descricao'] for i in dados["categorias"][0]["items"]):
                    dados["categorias"][0]["items"].append(item)
    
    return dados

def main():
    print("Iniciando extração de quantitativos de Paisagismo...")
    print(f"Diretório: {DWG_DIR}\n")
    
    # Extrair dados
    dados = extrair_quantitativos()
    
    # Criar diretório de saída
    output_dir = Path.home() / "orcamentos/projetos/parador-ag7/disciplinas"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Salvar JSON
    output_file = output_dir / "paisagismo.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Extração concluída!")
    print(f"Arquivo salvo: {output_file}")
    print(f"\nResumo:")
    print(f"  Arquivos processados: {len(dados['arquivos_processados'])}")
    for cat in dados['categorias']:
        print(f"  {cat['nome']}: {len(cat['items'])} items")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
