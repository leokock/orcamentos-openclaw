#!/usr/bin/env python3
"""
Extrai quantitativos elétricos de PDFs do projeto Parador AG7
"""

import pdfplumber
import json
import re
from pathlib import Path
from collections import defaultdict

# Configurações
PDF_DIR = Path.home() / "Library/CloudStorage/GoogleDrive-leonardo@cartesianengenharia.com/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/AG7 Incorporadora/Arquivos recebidos/2026.03.10 - Projetos Autodoc/15. Eletrico/04. Executivo/PDF"
OUTPUT_FILE = Path.home() / "orcamentos/projetos/parador-ag7/disciplinas/eletrico.json"

# Padrões para identificação
PATTERNS = {
    'eletroduto': [
        re.compile(r'(?:eletroduto|tubulação|conduíte).*?(\d+)\s*mm', re.IGNORECASE),
        re.compile(r'Ø\s*(\d+)', re.IGNORECASE),
        re.compile(r'φ\s*(\d+)', re.IGNORECASE),
    ],
    'cabo': [
        re.compile(r'cabo.*?(\d+(?:[,\.]\d+)?)\s*mm[²2]', re.IGNORECASE),
        re.compile(r'#\s*(\d+(?:[,\.]\d+)?)\s*mm[²2]', re.IGNORECASE),
        re.compile(r'(\d+(?:[,\.]\d+)?)\s*mm[²2]', re.IGNORECASE),
    ],
    'tomada': [
        re.compile(r'\bTUG\b', re.IGNORECASE),
        re.compile(r'tomada', re.IGNORECASE),
        re.compile(r'ponto.*?força', re.IGNORECASE),
    ],
    'luz': [
        re.compile(r'\bTUE\b', re.IGNORECASE),
        re.compile(r'iluminação', re.IGNORECASE),
        re.compile(r'ponto.*?luz', re.IGNORECASE),
        re.compile(r'\bPL\b'),
    ],
    'quadro': [
        re.compile(r'\bQD[A-Z0-9-]*\b', re.IGNORECASE),
        re.compile(r'quadro.*?(?:distrib|elétrico|força|luz)', re.IGNORECASE),
        re.compile(r'painel.*?elétrico', re.IGNORECASE),
    ],
}

def extract_info_from_pdf(pdf_path):
    """Extrai informações de um PDF"""
    print(f"  Processando: {pdf_path.name}")
    
    result = {
        'arquivo': pdf_path.name,
        'eletrodutos': defaultdict(int),
        'cabos': defaultdict(int),
        'pontos_luz': 0,
        'pontos_tomada': 0,
        'quadros': set()
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Extrai texto da página
                text = page.extract_text() or ""
                
                # Extrai tabelas
                tables = page.extract_tables()
                
                # Processa texto completo
                for line in text.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Eletrodutos
                    for pattern in PATTERNS['eletroduto']:
                        matches = pattern.findall(line)
                        for match in matches:
                            try:
                                diametro = int(match)
                                if 10 <= diametro <= 200:  # Filtro razoável
                                    result['eletrodutos'][f"Ø{diametro}mm"] += 1
                            except:
                                pass
                    
                    # Cabos
                    for pattern in PATTERNS['cabo']:
                        matches = pattern.findall(line)
                        for match in matches:
                            try:
                                secao = match.replace(',', '.')
                                secao_float = float(secao)
                                if 1.5 <= secao_float <= 240:  # Filtro razoável
                                    result['cabos'][f"{secao}mm²"] += 1
                            except:
                                pass
                    
                    # Pontos de luz
                    for pattern in PATTERNS['luz']:
                        if pattern.search(line):
                            result['pontos_luz'] += 1
                            break
                    
                    # Pontos de tomada
                    for pattern in PATTERNS['tomada']:
                        if pattern.search(line):
                            result['pontos_tomada'] += 1
                            break
                    
                    # Quadros
                    for pattern in PATTERNS['quadro']:
                        matches = pattern.findall(line)
                        for match in matches:
                            if isinstance(match, str):
                                result['quadros'].add(match[:30])
                
                # Processa tabelas
                for table in tables:
                    if not table:
                        continue
                    for row in table:
                        if not row:
                            continue
                        row_text = ' '.join([str(cell) for cell in row if cell])
                        
                        # Procura padrões nas tabelas também
                        for pattern in PATTERNS['eletroduto']:
                            matches = pattern.findall(row_text)
                            for match in matches:
                                try:
                                    diametro = int(match)
                                    if 10 <= diametro <= 200:
                                        result['eletrodutos'][f"Ø{diametro}mm"] += 1
                                except:
                                    pass
        
        return result
        
    except Exception as e:
        print(f"    ❌ Erro: {e}")
        return None

def consolidate_results(all_results):
    """Consolida resultados"""
    consolidated = {
        'eletrodutos': defaultdict(int),
        'cabos': defaultdict(int),
        'pontos_luz': 0,
        'pontos_tomada': 0,
        'quadros': set()
    }
    
    for result in all_results:
        if not result:
            continue
        
        for k, v in result['eletrodutos'].items():
            consolidated['eletrodutos'][k] += v
        
        for k, v in result['cabos'].items():
            consolidated['cabos'][k] += v
        
        consolidated['pontos_luz'] += result['pontos_luz']
        consolidated['pontos_tomada'] += result['pontos_tomada']
        consolidated['quadros'].update(result['quadros'])
    
    return consolidated

def main():
    print("=" * 70)
    print("EXTRAÇÃO DE QUANTITATIVOS ELÉTRICOS - PARADOR AG7 (via PDF)")
    print("=" * 70)
    print()
    
    # Lista PDFs (sem duplicados _1, _2)
    pdf_files = [f for f in PDF_DIR.glob("*.pdf") if not re.search(r'_\d+\.pdf$', f.name)]
    print(f"📄 Encontrados {len(pdf_files)} arquivos PDF para processar\n")
    
    # Processa
    all_results = []
    for i, pdf_file in enumerate(sorted(pdf_files), 1):
        print(f"[{i}/{len(pdf_files)}]", end=" ")
        result = extract_info_from_pdf(pdf_file)
        if result:
            all_results.append(result)
    
    print(f"\n✅ Processados {len(all_results)} arquivos com sucesso\n")
    
    # Consolida
    consolidated = consolidate_results(all_results)
    
    # Prepara output
    output = {
        "disciplina": "Elétrico",
        "fonte": "15. Eletrico/04. Executivo (extraído de PDFs)",
        "data_extracao": "2026-03-11",
        "total_arquivos_processados": len(all_results),
        "observacao": "Quantitativos extraídos por análise de texto dos PDFs. Números representam ocorrências identificadas nos desenhos.",
        "categorias": [
            {
                "nome": "Eletrodutos",
                "items": [
                    {"descricao": f"Eletroduto {diam}", "quantidade": qtd, "unidade": "ocorrências"}
                    for diam, qtd in sorted(consolidated['eletrodutos'].items(), 
                                           key=lambda x: int(re.search(r'\d+', x[0]).group()))
                ]
            },
            {
                "nome": "Cabos e Condutores",
                "items": [
                    {"descricao": f"Cabo {secao}", "quantidade": qtd, "unidade": "ocorrências"}
                    for secao, qtd in sorted(consolidated['cabos'].items(),
                                            key=lambda x: float(re.search(r'[\d.]+', x[0]).group()))
                ]
            },
            {
                "nome": "Pontos de Luz",
                "items": [
                    {"descricao": "Pontos de iluminação", "quantidade": consolidated['pontos_luz'], "unidade": "un"}
                ] if consolidated['pontos_luz'] > 0 else []
            },
            {
                "nome": "Pontos de Tomada",
                "items": [
                    {"descricao": "Pontos de tomada/força", "quantidade": consolidated['pontos_tomada'], "unidade": "un"}
                ] if consolidated['pontos_tomada'] > 0 else []
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
    
    # Salva
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    # Exibe resumo
    print("=" * 70)
    print("RESUMO DOS QUANTITATIVOS EXTRAÍDOS")
    print("=" * 70)
    
    if consolidated['eletrodutos']:
        print(f"\n📁 Eletrodutos:")
        for diam in sorted(consolidated['eletrodutos'].keys(), 
                          key=lambda x: int(re.search(r'\d+', x).group())):
            print(f"   • {diam}: {consolidated['eletrodutos'][diam]} ocorrências")
    
    if consolidated['cabos']:
        print(f"\n🔌 Cabos:")
        for secao in sorted(consolidated['cabos'].keys(),
                           key=lambda x: float(re.search(r'[\d.]+', x).group())):
            print(f"   • {secao}: {consolidated['cabos'][secao]} ocorrências")
    
    if consolidated['pontos_luz']:
        print(f"\n💡 Pontos de Luz: {consolidated['pontos_luz']}")
    
    if consolidated['pontos_tomada']:
        print(f"🔌 Pontos de Tomada: {consolidated['pontos_tomada']}")
    
    if consolidated['quadros']:
        print(f"\n📊 Quadros Elétricos ({len(consolidated['quadros'])}):")
        for quadro in sorted(consolidated['quadros']):
            print(f"   • {quadro}")
    
    print(f"\n✅ Arquivo salvo em:")
    print(f"   {OUTPUT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    main()
