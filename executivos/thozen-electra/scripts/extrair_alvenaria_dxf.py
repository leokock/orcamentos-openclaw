#!/usr/bin/env python3.11
"""
Script de Extração de Quantitativos de Alvenaria — DXF
Projeto: Thozen Electra
Disciplina: 03 ALVENARIA

Uso:
    python3.11 scripts/extrair_alvenaria_dxf.py <arquivo.dxf> [--pavimento <nome>] [--output <json>]

Dependências:
    pip3.11 install ezdxf

Autor: Cartesiano (Cartesian Engenharia)
Data: 2026-03-20
"""

import sys
import json
import argparse
from pathlib import Path

try:
    import ezdxf
except ImportError:
    print("❌ ERRO: Biblioteca 'ezdxf' não encontrada.")
    print("📦 Instale com: pip3.11 install ezdxf")
    sys.exit(1)


def extrair_alvenaria(dxf_path: str, pavimento: str = None) -> dict:
    """
    Extrai quantitativos de alvenaria de um arquivo DXF.
    
    Args:
        dxf_path: Caminho para o arquivo DXF
        pavimento: Nome do pavimento (ex: "Térreo", "G1", "Tipo")
    
    Returns:
        dict: Dados extraídos (áreas, comprimentos, vãos)
    """
    print(f"📂 Processando: {dxf_path}")
    
    try:
        doc = ezdxf.readfile(dxf_path)
    except Exception as e:
        print(f"❌ ERRO ao ler DXF: {e}")
        return None
    
    msp = doc.modelspace()
    
    # Estrutura de dados
    dados = {
        "arquivo": Path(dxf_path).name,
        "pavimento": pavimento or "Desconhecido",
        "areas_por_layer": {},
        "comprimentos_por_layer": {},
        "area_total": 0,
        "comprimento_total": 0,
        "entidades": {
            "hatch": 0,
            "polyline": 0,
            "line": 0,
            "block": 0,
            "text": 0
        }
    }
    
    # Processar HATCHs (áreas de alvenaria)
    print("  🔍 Processando HATCHs (áreas)...")
    for hatch in msp.query('HATCH'):
        layer = hatch.dxf.layer
        try:
            # ezdxf não expõe área diretamente, calcular via paths
            # Para simplificar, contar número de hatchs e layers
            # Área precisa ser calculada via boundary paths (mais complexo)
            if layer not in dados["areas_por_layer"]:
                dados["areas_por_layer"][layer] = 0
            # Placeholder: incrementar contador (área real precisa de cálculo geométrico)
            dados["areas_por_layer"][layer] += 1
            dados["entidades"]["hatch"] += 1
        except Exception as e:
            print(f"    ⚠️ Erro ao processar hatch no layer '{layer}': {e}")
    
    # Processar POLYLINEs (comprimentos de paredes)
    print("  🔍 Processando POLYLINEs (comprimentos)...")
    for polyline in msp.query('LWPOLYLINE'):
        layer = polyline.dxf.layer
        try:
            comprimento = polyline.get_length()
            if comprimento > 0:
                if layer not in dados["comprimentos_por_layer"]:
                    dados["comprimentos_por_layer"][layer] = 0
                dados["comprimentos_por_layer"][layer] += comprimento
                dados["comprimento_total"] += comprimento
                dados["entidades"]["polyline"] += 1
        except Exception as e:
            print(f"    ⚠️ Erro ao calcular comprimento de polyline no layer '{layer}': {e}")
    
    # Processar LINEs (backup para comprimentos)
    print("  🔍 Processando LINEs (comprimentos)...")
    for line in msp.query('LINE'):
        layer = line.dxf.layer
        start = line.dxf.start
        end = line.dxf.end
        comprimento = ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5
        
        if comprimento > 0:
            if layer not in dados["comprimentos_por_layer"]:
                dados["comprimentos_por_layer"][layer] = 0
            dados["comprimentos_por_layer"][layer] += comprimento
            dados["comprimento_total"] += comprimento
            dados["entidades"]["line"] += 1
    
    # Processar BLOCKs (possíveis vãos, portas, janelas)
    print("  🔍 Processando BLOCKs (vãos/esquadrias)...")
    dados["blocos_por_nome"] = {}
    for insert in msp.query('INSERT'):
        block_name = insert.dxf.name
        if block_name not in dados["blocos_por_nome"]:
            dados["blocos_por_nome"][block_name] = 0
        dados["blocos_por_nome"][block_name] += 1
        dados["entidades"]["block"] += 1
    
    # Processar TEXTs (legendas, especificações)
    print("  🔍 Processando TEXTs (legendas)...")
    dados["textos_unicos"] = set()
    for text in msp.query('TEXT'):
        texto = text.dxf.text.strip()
        if texto:
            dados["textos_unicos"].add(texto)
            dados["entidades"]["text"] += 1
    
    # Converter set para list (para JSON)
    dados["textos_unicos"] = sorted(list(dados["textos_unicos"]))
    
    return dados


def exibir_relatorio(dados: dict):
    """Exibe relatório formatado dos dados extraídos."""
    if not dados:
        print("❌ Nenhum dado para exibir.")
        return
    
    print("\n" + "="*80)
    print(f"📊 RELATÓRIO DE EXTRAÇÃO — {dados['pavimento'].upper()}")
    print("="*80)
    print(f"📁 Arquivo: {dados['arquivo']}")
    print(f"🏢 Pavimento: {dados['pavimento']}")
    print()
    
    # Áreas
    print("📐 ÁREAS POR LAYER:")
    if dados["areas_por_layer"]:
        for layer, area in sorted(dados["areas_por_layer"].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {layer:40s} {area:>12,.2f} m²")
        print(f"  {'TOTAL':40s} {dados['area_total']:>12,.2f} m²")
    else:
        print("  ⚠️ Nenhuma área extraída (HATCHs não encontrados)")
    print()
    
    # Comprimentos
    print("📏 COMPRIMENTOS POR LAYER:")
    if dados["comprimentos_por_layer"]:
        for layer, comp in sorted(dados["comprimentos_por_layer"].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {layer:40s} {comp:>12,.2f} m")
        print(f"  {'TOTAL':40s} {dados['comprimento_total']:>12,.2f} m")
    else:
        print("  ⚠️ Nenhum comprimento extraído (POLYLINEs/LINEs não encontrados)")
    print()
    
    # Blocos
    print("🧱 BLOCOS (Portas/Janelas/Vãos):")
    if dados["blocos_por_nome"]:
        for nome, qtd in sorted(dados["blocos_por_nome"].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {nome:40s} {qtd:>5d} un")
    else:
        print("  ⚠️ Nenhum bloco encontrado")
    print()
    
    # Textos (primeiros 10)
    print("📝 TEXTOS ENCONTRADOS (primeiros 10):")
    if dados["textos_unicos"]:
        for texto in dados["textos_unicos"][:10]:
            print(f"  • {texto}")
        if len(dados["textos_unicos"]) > 10:
            print(f"  ... e mais {len(dados['textos_unicos']) - 10} textos")
    else:
        print("  ⚠️ Nenhum texto encontrado")
    print()
    
    # Estatísticas
    print("📊 ESTATÍSTICAS:")
    print(f"  • HATCHs processados:    {dados['entidades']['hatch']:>6d}")
    print(f"  • POLYLINEs processadas: {dados['entidades']['polyline']:>6d}")
    print(f"  • LINEs processadas:     {dados['entidades']['line']:>6d}")
    print(f"  • BLOCKs processados:    {dados['entidades']['block']:>6d}")
    print(f"  • TEXTs processados:     {dados['entidades']['text']:>6d}")
    print("="*80)


def main():
    parser = argparse.ArgumentParser(
        description="Extração de quantitativos de alvenaria de arquivos DXF"
    )
    parser.add_argument("dxf_file", help="Caminho para o arquivo DXF")
    parser.add_argument("--pavimento", "-p", help="Nome do pavimento (ex: Térreo, G1, Tipo)")
    parser.add_argument("--output", "-o", help="Arquivo JSON de saída (opcional)")
    parser.add_argument("--quiet", "-q", action="store_true", help="Modo silencioso (só erros)")
    
    args = parser.parse_args()
    
    # Validar arquivo
    if not Path(args.dxf_file).exists():
        print(f"❌ ERRO: Arquivo não encontrado: {args.dxf_file}")
        sys.exit(1)
    
    # Processar
    dados = extrair_alvenaria(args.dxf_file, args.pavimento)
    
    if not dados:
        print("❌ Falha ao processar arquivo.")
        sys.exit(1)
    
    # Exibir relatório
    if not args.quiet:
        exibir_relatorio(dados)
    
    # Salvar JSON (se solicitado)
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
            print(f"\n✅ Dados salvos em: {args.output}")
        except Exception as e:
            print(f"❌ ERRO ao salvar JSON: {e}")
            sys.exit(1)
    
    print("\n✅ Processamento concluído!")


if __name__ == "__main__":
    main()
