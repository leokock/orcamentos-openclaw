#!/usr/bin/env python3.11
"""
Extrai strings legíveis de arquivos DWG
Busca por padrões técnicos relevantes para sistemas de exaustão
"""
import sys
import re
from pathlib import Path

def extract_dwg_strings(dwg_path, min_length=4):
    """Extrai strings ASCII legíveis do arquivo DWG"""
    strings_found = []
    
    with open(dwg_path, 'rb') as f:
        data = f.read()
    
    # Regex para strings ASCII imprimíveis
    pattern = rb'[\x20-\x7E]{' + str(min_length).encode() + rb',}'
    matches = re.findall(pattern, data)
    
    for match in matches:
        try:
            text = match.decode('ascii')
            strings_found.append(text)
        except:
            pass
    
    return strings_found

def filter_technical_strings(strings_list):
    """Filtra strings relevantes para sistema de exaustão"""
    patterns = [
        r'(?i)(exaust|ventil|coifa|duto|grelha)',
        r'(?i)(motor|vazão|vazao|m3/h|m³/h|cfm)',
        r'(?i)(potência|potencia|cv|kw|hp|rpm)',
        r'(?i)(diâmetro|diametro|ø|DN|bitola)',
        r'(?i)(cabo|quadro|qd|circuito|fase)',
        r'(?i)(chapa|aço|galv|inox)',
        r'(\d+\s*mm|\d+\s*cm|\d+\s*m)',
        r'(\d+[\.,]\d+\s*(kw|cv|hp))',
        r'(DN\s*\d+|Ø\s*\d+)',
        r'(\d+[\.,]\d+\s*m3/h)',
        r'(#\s*\d+\s*AWG|#\d+)',
    ]
    
    relevant = {}
    
    for s in strings_list:
        for pattern in patterns:
            if re.search(pattern, s, re.IGNORECASE):
                # Classificar por categoria
                cat = 'GERAL'
                if re.search(r'(?i)(motor|potência|potencia|cv|kw|rpm)', s):
                    cat = 'MOTOR/POTÊNCIA'
                elif re.search(r'(?i)(vazão|vazao|m3/h|cfm)', s):
                    cat = 'VAZÃO'
                elif re.search(r'(?i)(duto|diâmetro|diametro|ø|DN)', s):
                    cat = 'DUTOS'
                elif re.search(r'(?i)(cabo|quadro|circuito|fase)', s):
                    cat = 'ELÉTRICA'
                elif re.search(r'(?i)(coifa|grelha|chapa)', s):
                    cat = 'EQUIPAMENTOS'
                
                if cat not in relevant:
                    relevant[cat] = []
                if s not in relevant[cat]:
                    relevant[cat].append(s)
                break
    
    return relevant

def main():
    if len(sys.argv) < 2:
        print("Uso: python3.11 extract_dwg_text.py <arquivo.dwg>")
        sys.exit(1)
    
    dwg_path = sys.argv[1]
    
    if not Path(dwg_path).exists():
        print(f"Erro: arquivo não encontrado: {dwg_path}")
        sys.exit(1)
    
    print(f"Processando: {dwg_path}\n")
    
    # Extrair strings
    all_strings = extract_dwg_strings(dwg_path, min_length=3)
    print(f"Total de strings encontradas: {len(all_strings)}\n")
    
    # Filtrar relevantes
    relevant = filter_technical_strings(all_strings)
    
    # Exibir por categoria
    for cat, items in sorted(relevant.items()):
        print(f"\n{'='*60}")
        print(f"  {cat}")
        print('='*60)
        for item in sorted(set(items)):
            print(f"  {item}")
    
    # Estatísticas
    print(f"\n{'='*60}")
    print(f"RESUMO:")
    print(f"  Strings totais: {len(all_strings)}")
    print(f"  Strings relevantes: {sum(len(v) for v in relevant.values())}")
    print(f"  Categorias: {len(relevant)}")
    print('='*60)

if __name__ == '__main__':
    main()
