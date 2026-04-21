#!/usr/bin/env python3.11
"""
Script para extrair dados de ventilação mecânica do projeto Thozen Electra.
Tenta processar DWG → DXF usando ferramentas disponíveis.
"""

import os
import sys
import subprocess
from pathlib import Path

# Caminhos
PROJETO_DIR = Path("executivo/thozen-electra")
FONTES_DIR = PROJETO_DIR / "fontes"
DXF_DIR = PROJETO_DIR / "dxf-ventilacao"
DWG_FILE = FONTES_DIR / "RA_EVM_LEGAL_PROJETO_R05.dwg"

def tentar_conversao_dwg_para_dxf():
    """Tenta converter DWG → DXF usando ferramentas disponíveis."""
    
    print(f"🔍 Procurando conversor DWG → DXF...")
    
    # Lista de conversores possíveis
    conversores = [
        # ODA File Converter (TeighaFileConverter)
        {
            "cmd": ["TeighaFileConverter"],
            "check": lambda: subprocess.run(["which", "TeighaFileConverter"], 
                                          capture_output=True).returncode == 0
        },
        # dwg2dxf (se instalado)
        {
            "cmd": ["dwg2dxf"],
            "check": lambda: subprocess.run(["which", "dwg2dxf"], 
                                          capture_output=True).returncode == 0
        },
        # LibreCAD (via command line, se disponível)
        {
            "cmd": ["librecad"],
            "check": lambda: subprocess.run(["which", "librecad"], 
                                          capture_output=True).returncode == 0
        },
    ]
    
    for conv in conversores:
        if conv["check"]():
            print(f"✅ Encontrado: {conv['cmd'][0]}")
            return conv["cmd"][0]
    
    print("❌ Nenhum conversor DWG → DXF encontrado no sistema")
    print("\n💡 Soluções possíveis:")
    print("1. Instalar ODA File Converter: https://www.opendesign.com/guestfiles/oda_file_converter")
    print("2. Solicitar ao projetista a versão DXF do arquivo")
    print("3. Usar AutoCAD/LibreCAD para exportar manualmente")
    return None

def tentar_extrair_via_strings():
    """Tenta extrair informações básicas do DWG via strings (fallback)."""
    
    print("\n🔧 Tentando extração via strings (método de fallback)...")
    
    try:
        # Extrair strings do arquivo binário
        result = subprocess.run(
            ["strings", str(DWG_FILE)],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Comando 'strings' falhou")
            return None
        
        texto = result.stdout
        linhas = texto.split('\n')
        
        # Procurar padrões relevantes
        padroes_relevantes = {
            "ventilador": [],
            "pressao": [],
            "vazao": [],
            "damper": [],
            "grelha": [],
            "duto": [],
            "escada": [],
        }
        
        for linha in linhas:
            linha_lower = linha.lower()
            for palavra_chave in padroes_relevantes.keys():
                if palavra_chave in linha_lower and len(linha.strip()) > 3:
                    padroes_relevantes[palavra_chave].append(linha.strip())
        
        # Salvar resultado
        output_file = DXF_DIR / "extração-strings.txt"
        DXF_DIR.mkdir(exist_ok=True, parents=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=== EXTRAÇÃO VIA STRINGS ===\n")
            f.write(f"Arquivo: {DWG_FILE}\n")
            f.write(f"Data: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n\n")
            
            for palavra, ocorrencias in padroes_relevantes.items():
                if ocorrencias:
                    f.write(f"\n## {palavra.upper()} ({len(ocorrencias)} ocorrências)\n")
                    for i, oc in enumerate(set(ocorrencias[:50]), 1):  # Limitar a 50 únicas
                        f.write(f"{i}. {oc}\n")
        
        print(f"✅ Extração salva em: {output_file}")
        print(f"📊 Total de strings encontradas: {len(linhas)}")
        for palavra, ocorrencias in padroes_relevantes.items():
            if ocorrencias:
                print(f"   - {palavra}: {len(set(ocorrencias))} únicas")
        
        return output_file
    
    except Exception as e:
        print(f"❌ Erro na extração via strings: {e}")
        return None

def main():
    print("=" * 70)
    print("EXTRAÇÃO DE DADOS — VENTILAÇÃO MECÂNICA — THOZEN ELECTRA")
    print("=" * 70)
    
    # Verificar se arquivo existe
    if not DWG_FILE.exists():
        print(f"❌ Arquivo não encontrado: {DWG_FILE}")
        sys.exit(1)
    
    print(f"\n📄 Arquivo: {DWG_FILE.name}")
    print(f"📦 Tamanho: {DWG_FILE.stat().st_size / 1024 / 1024:.2f} MB")
    
    # Tentar conversão
    conversor = tentar_conversao_dwg_para_dxf()
    
    if conversor:
        print(f"\n⚠️ Conversor encontrado: {conversor}")
        print("⚠️ A conversão automática não está implementada neste script.")
        print("⚠️ Execute manualmente ou solicite a versão DXF ao projetista.")
    else:
        # Fallback: extração via strings
        resultado = tentar_extrair_via_strings()
        
        if resultado:
            print(f"\n✅ Extração concluída!")
            print(f"📝 Verifique o arquivo: {resultado}")
            print("\n⚠️ ATENÇÃO:")
            print("   - Esta extração é LIMITADA (apenas strings de texto)")
            print("   - NÃO contém geometria, blocos ou quantitativos precisos")
            print("   - Para extração completa, é necessário converter DWG → DXF")
        else:
            print("\n❌ Não foi possível extrair dados do arquivo.")
    
    print("\n" + "=" * 70)
    print("PRÓXIMOS PASSOS:")
    print("=" * 70)
    print("1. Solicitar ao projetista Rubens Alves a versão DXF do arquivo")
    print("2. OU instalar ODA File Converter para conversão local")
    print("3. Aguardar conversão para processar com ezdxf (extração completa)")
    print("=" * 70)

if __name__ == "__main__":
    main()
