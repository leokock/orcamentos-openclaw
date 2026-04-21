#!/usr/bin/env python3.11
"""
Extração de dados do DWG de Ventilação Mecânica - Thozen Electra
"""

import sys
import os

def extract_with_strings(dwg_path):
    """Extrai informações usando strings do arquivo DWG"""
    import subprocess
    
    print(f"📄 Processando: {dwg_path}")
    print(f"📏 Tamanho: {os.path.getsize(dwg_path) / 1024 / 1024:.2f} MB\n")
    
    # Extrair strings relevantes
    patterns = [
        ("Ventiladores/Exaustores", r"(ventilador|exaustor|insuflador|fan)"),
        ("Potências", r"([0-9]+[.,][0-9]+\s*(CV|HP|kW|W))"),
        ("Vazões", r"([0-9]+[.,][0-9]+\s*(m3/h|m³/h|CMH))"),
        ("Pressões", r"([0-9]+[.,][0-9]+\s*(Pa|mmCA))"),
        ("Dutos", r"(duto|duct|Ø\s*[0-9]+)"),
        ("Diâmetros", r"(Ø|diametro|diameter)\s*[0-9]+"),
        ("Grelhas", r"(grelha|grade|grille)"),
        ("Dampers", r"(damper|registro)"),
        ("Escadas", r"(escada|stair|E[-_]?[0-9]+)"),
        ("Quadros", r"(Q[A-Z0-9\-_]+|quadro)"),
        ("Cabos", r"([0-9]+x[0-9]+|cabo)"),
    ]
    
    results = {}
    
    for label, pattern in patterns:
        cmd = f"strings -n 4 '{dwg_path}' | grep -iE '{pattern}' | sort -u"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
            lines = [l.strip() for l in output.split('\n') if l.strip()]
            if lines:
                results[label] = lines
        except:
            results[label] = []
    
    return results

def extract_layer_info(dwg_path):
    """Tenta extrair informações de layers"""
    import subprocess
    
    cmd = f"strings -n 5 '{dwg_path}' | grep -iE '^[A-Z_]+(VENT|DUTO|ESCADA)' | sort -u"
    try:
        output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        return [l.strip() for l in output.split('\n') if l.strip()]
    except:
        return []

def extract_numeric_data(dwg_path):
    """Extrai dados numéricos estruturados"""
    import subprocess
    
    # Procurar por padrões numéricos comuns em projetos de ventilação
    patterns = {
        "Diâmetros (mm)": r"\b[0-9]{2,4}\s*mm\b",
        "Vazões (m³/h)": r"\b[0-9]+[.,]?[0-9]*\s*m[3³]/h\b",
        "Potências (CV/kW)": r"\b[0-9]+[.,]?[0-9]*\s*(CV|kW)\b",
        "RPM": r"\b[0-9]{3,5}\s*RPM\b",
    }
    
    results = {}
    for label, pattern in patterns.items():
        cmd = f"strings -n 5 '{dwg_path}' | grep -ioE '{pattern}' | sort -u"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
            lines = [l.strip() for l in output.split('\n') if l.strip()]
            if lines:
                results[label] = lines
        except:
            results[label] = []
    
    return results

def main():
    dwg_path = "projetos/thozen-electra/projetos/12 ESCADA VENTILACAO MECANICA/DWG/RA_EVM_LEGAL_PROJETO_R05.dwg"
    
    if not os.path.exists(dwg_path):
        print(f"❌ Arquivo não encontrado: {dwg_path}")
        return 1
    
    print("=" * 80)
    print("EXTRAÇÃO DE DADOS - VENTILAÇÃO MECÂNICA")
    print("=" * 80)
    print()
    
    # Método 1: Strings com padrões
    print("🔍 MÉTODO 1: Busca por padrões\n")
    results = extract_with_strings(dwg_path)
    
    for label, items in results.items():
        if items:
            print(f"\n📋 {label}:")
            for item in items[:20]:  # Limitar a 20 itens por categoria
                print(f"   • {item}")
    
    # Método 2: Layers
    print("\n" + "=" * 80)
    print("🔍 MÉTODO 2: Layers identificados\n")
    layers = extract_layer_info(dwg_path)
    if layers:
        for layer in layers[:30]:
            print(f"   • {layer}")
    else:
        print("   (nenhum layer identificado)")
    
    # Método 3: Dados numéricos estruturados
    print("\n" + "=" * 80)
    print("🔍 MÉTODO 3: Dados numéricos estruturados\n")
    numeric_data = extract_numeric_data(dwg_path)
    
    for label, items in numeric_data.items():
        if items:
            print(f"\n📊 {label}:")
            for item in items[:15]:
                print(f"   • {item}")
    
    print("\n" + "=" * 80)
    print("✅ Extração concluída!")
    print("=" * 80)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
