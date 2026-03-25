#!/usr/bin/env python3.11
"""
Análise heurística de arquivo DWG para sistema de exaustão
Busca por padrões numéricos e técnicos
"""
import sys
import re
from collections import Counter

def extract_numeric_patterns(dwg_path):
    """Extrai padrões numéricos do DWG"""
    with open(dwg_path, 'rb') as f:
        data = f.read()
    
    # Converter para string tratável
    text = data.decode('latin-1', errors='ignore')
    
    patterns = {
        'diametros': re.findall(r'(?:DN|Ø|diâmetro|diametro)[\s:=]?(\d+)', text, re.IGNORECASE),
        'vazoes': re.findall(r'(\d+[\.,]?\d*)\s*(?:m3/h|m³/h|CMH)', text, re.IGNORECASE),
        'potencias': re.findall(r'(\d+[\.,]?\d*)\s*(?:CV|kW|HP)', text, re.IGNORECASE),
        'rpm': re.findall(r'(\d+)\s*RPM', text, re.IGNORECASE),
        'dimensoes_mm': re.findall(r'(\d{2,4})\s*(?:mm|MM)', text, re.IGNORECASE),
        'quantidades': re.findall(r'(?:QTD|QTDE|QT)[\s:=]?(\d+)', text, re.IGNORECASE),
        'cabos_awg': re.findall(r'#\s*(\d+)\s*AWG', text, re.IGNORECASE),
        'cabos_mm2': re.findall(r'(\d+[\.,]?\d*)\s*mm²', text, re.IGNORECASE),
        'voltagens': re.findall(r'(\d{3})\s*V', text, re.IGNORECASE),
    }
    
    return patterns

def count_keywords(dwg_path):
    """Conta palavras-chave técnicas"""
    with open(dwg_path, 'rb') as f:
        data = f.read()
    
    text = data.decode('latin-1', errors='ignore').upper()
    
    keywords = [
        'EXAUSTOR', 'MOTOR', 'VENTILADOR',
        'DUTO', 'TUBULACAO', 'TUBULAÇÃO',
        'COIFA', 'GRELHA', 'DAMPER',
        'QUADRO', 'CABO', 'CIRCUITO',
        'CHURRASQUEIRA', 'CHURRASQ',
        'VAZÃO', 'VAZAO', 'M3/H',
        'CV', 'KW', 'HP', 'RPM',
        'INOX', 'GALVANIZADO', 'GALV',
    ]
    
    counts = {kw: text.count(kw) for kw in keywords}
    return {k: v for k, v in counts.items() if v > 0}

def main():
    if len(sys.argv) < 2:
        print("Uso: python3.11 analyze_dwg_binary.py <arquivo.dwg>")
        sys.exit(1)
    
    dwg_path = sys.argv[1]
    
    print(f"Analisando: {dwg_path}\n")
    print("="*70)
    
    # Padrões numéricos
    patterns = extract_numeric_patterns(dwg_path)
    
    print("\n📊 PADRÕES NUMÉRICOS ENCONTRADOS:\n")
    
    for category, values in patterns.items():
        if values:
            print(f"\n{category.upper().replace('_', ' ')}:")
            counter = Counter(values)
            for value, count in counter.most_common(10):
                print(f"  {value} → {count}x")
    
    # Palavras-chave
    print("\n" + "="*70)
    print("\n🔍 PALAVRAS-CHAVE TÉCNICAS:\n")
    
    keywords = count_keywords(dwg_path)
    for kw, count in sorted(keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"  {kw}: {count}x")
    
    print("\n" + "="*70)

if __name__ == '__main__':
    main()
