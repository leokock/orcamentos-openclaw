#!/usr/bin/env python3.11
"""
Script de Extração de Quantitativos de Alvenaria — DXF v2
Projeto: Thozen Electra
Disciplina: 03 ALVENARIA

Melhorias v2:
- Filtra apenas layers relevantes (A-WALL)
- Calcula área real de HATCHs via boundary paths
- Processa LWPOLYLINEs e POLYLINEs

Uso:
    python3.11 scripts/extrair_alvenaria_dxf_v2.py <arquivo.dxf> [--pavimento <nome>] [--output <json>]

Autor: Cartesiano (Cartesian Engenharia)
Data: 2026-03-20
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List
import math

try:
    import ezdxf
    from ezdxf.math import Vec2
except ImportError:
    print("❌ ERRO: Biblioteca 'ezdxf' não encontrada.")
    print("📦 Instale com: pip3.11 install ezdxf")
    sys.exit(1)


# Layers relevantes para alvenaria
LAYERS_ALVENARIA = [
    'A-WALL',  # Paredes
    'ALV',      # Alvenaria (padrão genérico)
    'ALVENARIA',
    'PAREDE',
    'WALL'
]

LAYERS_VAOS = [
    'A-DOOR',   # Portas
    'A-GLAZ',   # Vidros/janelas
    'PORTA',
    'JANELA',
    'DOOR',
    'WINDOW'
]


def layer_match(layer_name: str, patterns: List[str]) -> bool:
    """Verifica se layer corresponde a algum padrão."""
    layer_upper = layer_name.upper()
    return any(pattern.upper() in layer_upper for pattern in patterns)


def calcular_area_polyline(points: List) -> float:
    """Calcula área de polígono via fórmula de Shoelace."""
    if len(points) < 3:
        return 0
    
    try:
        area = 0
        n = len(points)
        for i in range(n):
            j = (i + 1) % n
            p1 = points[i]
            p2 = points[j]
            # Extrair coordenadas (pode ser tuple ou Vec2)
            x1 = p1[0] if isinstance(p1, (tuple, list)) else p1.x
            y1 = p1[1] if isinstance(p1, (tuple, list)) else p1.y
            x2 = p2[0] if isinstance(p2, (tuple, list)) else p2.x
            y2 = p2[1] if isinstance(p2, (tuple, list)) else p2.y
            area += (x1 * y2) - (x2 * y1)
        return abs(area) / 2
    except Exception as e:
        print(f"    ⚠️ Erro ao calcular área: {e}")
        return 0


def calcular_comprimento_polyline(points: List) -> float:
    """Calcula comprimento total de polyline."""
    if len(points) < 2:
        return 0
    
    try:
        comp = 0
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            # Extrair coordenadas
            x1 = p1[0] if isinstance(p1, (tuple, list)) else p1.x
            y1 = p1[1] if isinstance(p1, (tuple, list)) else p1.y
            x2 = p2[0] if isinstance(p2, (tuple, list)) else p2.x
            y2 = p2[1] if isinstance(p2, (tuple, list)) else p2.y
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            comp += dist
        return comp
    except Exception as e:
        print(f"    ⚠️ Erro ao calcular comprimento: {e}")
        return 0


def extrair_alvenaria(dxf_path: str, pavimento: str = None) -> dict:
    """
    Extrai quantitativos de alvenaria de um arquivo DXF.
    
    Args:
        dxf_path: Caminho para o arquivo DXF
        pavimento: Nome do pavimento (ex: "Térreo", "G1", "Tipo")
    
    Returns:
        dict: Dados extraídos
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
        "area_alvenaria_m2": 0,
        "comprimento_paredes_m": 0,
        "areas_por_layer": {},
        "comprimentos_por_layer": {},
        "vaos": {
            "portas": 0,
            "janelas": 0
        },
        "entidades": {
            "hatch": 0,
            "polyline": 0,
            "lwpolyline": 0,
            "line": 0,
            "insert": 0
        }
    }
    
    # Processar HATCHs (áreas de alvenaria)
    print("  🔍 HATCHs (áreas)...")
    for hatch in msp.query('HATCH'):
        layer = hatch.dxf.layer
        
        # Filtrar apenas layers relevantes
        if not layer_match(layer, LAYERS_ALVENARIA):
            continue
        
        dados["entidades"]["hatch"] += 1
        
        try:
            # Tentar extrair boundary paths e calcular área
            for path in hatch.paths:
                if hasattr(path, 'vertices'):
                    area = calcular_area_polyline(path.vertices)
                    if area > 0:
                        if layer not in dados["areas_por_layer"]:
                            dados["areas_por_layer"][layer] = 0
                        dados["areas_por_layer"][layer] += area
                        dados["area_alvenaria_m2"] += area
        except Exception as e:
            print(f"    ⚠️ Erro ao processar hatch no layer '{layer}': {e}")
    
    # Processar LWPOLYLINEs (comprimentos de paredes)
    print("  🔍 LWPOLYLINEs (comprimentos)...")
    for lwpoly in msp.query('LWPOLYLINE'):
        layer = lwpoly.dxf.layer
        
        # Filtrar apenas layers relevantes
        if not layer_match(layer, LAYERS_ALVENARIA):
            continue
        
        dados["entidades"]["lwpolyline"] += 1
        
        try:
            # Extrair vértices
            vertices = list(lwpoly.get_points())
            comp = calcular_comprimento_polyline(vertices)
            
            if comp > 0:
                if layer not in dados["comprimentos_por_layer"]:
                    dados["comprimentos_por_layer"][layer] = 0
                dados["comprimentos_por_layer"][layer] += comp
                dados["comprimento_paredes_m"] += comp
        except Exception as e:
            print(f"    ⚠️ Erro ao processar lwpolyline no layer '{layer}': {e}")
    
    # Processar POLYLINEs (fallback)
    print("  🔍 POLYLINEs (comprimentos)...")
    for poly in msp.query('POLYLINE'):
        layer = poly.dxf.layer
        
        if not layer_match(layer, LAYERS_ALVENARIA):
            continue
        
        dados["entidades"]["polyline"] += 1
        
        try:
            vertices = [v.dxf.location for v in poly.vertices]
            comp = calcular_comprimento_polyline(vertices)
            
            if comp > 0:
                if layer not in dados["comprimentos_por_layer"]:
                    dados["comprimentos_por_layer"][layer] = 0
                dados["comprimentos_por_layer"][layer] += comp
                dados["comprimento_paredes_m"] += comp
        except Exception as e:
            print(f"    ⚠️ Erro ao processar polyline no layer '{layer}': {e}")
    
    # Processar LINEs (paredes lineares)
    print("  🔍 LINEs (comprimentos)...")
    for line in msp.query('LINE'):
        layer = line.dxf.layer
        
        if not layer_match(layer, LAYERS_ALVENARIA):
            continue
        
        dados["entidades"]["line"] += 1
        
        try:
            start = line.dxf.start
            end = line.dxf.end
            comp = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            
            if comp > 0:
                if layer not in dados["comprimentos_por_layer"]:
                    dados["comprimentos_por_layer"][layer] = 0
                dados["comprimentos_por_layer"][layer] += comp
                dados["comprimento_paredes_m"] += comp
        except Exception as e:
            print(f"    ⚠️ Erro ao processar line no layer '{layer}': {e}")
    
    # Processar INSERTs (blocos de portas/janelas)
    print("  🔍 INSERTs (vãos)...")
    for insert in msp.query('INSERT'):
        layer = insert.dxf.layer
        name = insert.dxf.name.upper()
        
        dados["entidades"]["insert"] += 1
        
        if 'DOOR' in name or 'PORTA' in name:
            dados["vaos"]["portas"] += 1
        elif 'WINDOW' in name or 'JANELA' in name or 'GLAZ' in name:
            dados["vaos"]["janelas"] += 1
    
    return dados


def formatar_relatorio(dados: dict, quiet: bool = False) -> str:
    """Formata relatório de extração."""
    if not dados:
        return "❌ Nenhum dado extraído."
    
    lines = []
    
    if not quiet:
        lines.append("=" * 80)
        lines.append(f"📊 RELATÓRIO — {dados['pavimento'].upper()}")
        lines.append("=" * 80)
        lines.append(f"📁 Arquivo: {dados['arquivo']}")
        lines.append(f"🏢 Pavimento: {dados['pavimento']}")
        lines.append("")
    
    # Área total
    lines.append(f"📐 ÁREA TOTAL DE ALVENARIA: {dados['area_alvenaria_m2']:.2f} m²")
    
    if dados['areas_por_layer']:
        lines.append("\n  Detalhamento por layer:")
        for layer, area in sorted(dados['areas_por_layer'].items(), key=lambda x: -x[1]):
            lines.append(f"    • {layer:40s} {area:10.2f} m²")
    
    # Comprimento total
    lines.append(f"\n📏 COMPRIMENTO TOTAL DE PAREDES: {dados['comprimento_paredes_m']:.2f} m")
    
    if dados['comprimentos_por_layer']:
        lines.append("\n  Detalhamento por layer:")
        for layer, comp in sorted(dados['comprimentos_por_layer'].items(), key=lambda x: -x[1]):
            lines.append(f"    • {layer:40s} {comp:10.2f} m")
    
    # Vãos
    if dados['vaos']['portas'] or dados['vaos']['janelas']:
        lines.append(f"\n🚪 VÃOS:")
        lines.append(f"  • Portas: {dados['vaos']['portas']} un")
        lines.append(f"  • Janelas: {dados['vaos']['janelas']} un")
    
    # Entidades processadas
    if not quiet:
        lines.append(f"\n🔢 ENTIDADES PROCESSADAS:")
        lines.append(f"  • HATCHs: {dados['entidades']['hatch']}")
        lines.append(f"  • LWPOLYLINEs: {dados['entidades']['lwpolyline']}")
        lines.append(f"  • POLYLINEs: {dados['entidades']['polyline']}")
        lines.append(f"  • LINEs: {dados['entidades']['line']}")
        lines.append(f"  • INSERTs: {dados['entidades']['insert']}")
    
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extrai quantitativos de alvenaria de DXF")
    parser.add_argument("dxf_file", help="Arquivo DXF de entrada")
    parser.add_argument("--pavimento", default=None, help="Nome do pavimento")
    parser.add_argument("--output", default=None, help="Arquivo JSON de saída")
    parser.add_argument("--quiet", action="store_true", help="Modo silencioso")
    
    args = parser.parse_args()
    
    # Extrair dados
    dados = extrair_alvenaria(args.dxf_file, args.pavimento)
    
    if not dados:
        sys.exit(1)
    
    # Salvar JSON
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        if not args.quiet:
            print(f"\n💾 Dados salvos em: {args.output}")
    
    # Exibir relatório
    print(formatar_relatorio(dados, args.quiet))


if __name__ == "__main__":
    main()
