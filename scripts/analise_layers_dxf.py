#!/usr/bin/env python3.11
"""
Análise de Layers em DXF
Identifica layers relevantes para extração de quantitativos

Uso: python3.11 scripts/analise_layers_dxf.py <arquivo.dxf>
"""

import sys
from pathlib import Path
from collections import defaultdict

try:
    import ezdxf
except ImportError:
    print("❌ pip3.11 install ezdxf")
    sys.exit(1)


def analisar_layers(dxf_path: str):
    print(f"📂 {Path(dxf_path).name}\n")
    
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    # Contar entidades por layer
    stats = defaultdict(lambda: {
        'HATCH': 0,
        'LWPOLYLINE': 0,
        'POLYLINE': 0,
        'LINE': 0,
        'INSERT': 0,
        'TEXT': 0,
        'MTEXT': 0
    })
    
    for entity in msp:
        etype = entity.dxftype()
        layer = entity.dxf.layer
        if etype in stats[layer]:
            stats[layer][etype] += 1
    
    # Ordenar por relevância (layers com HATCH primeiro)
    layers_sorted = sorted(stats.items(), 
                          key=lambda x: (x[1]['HATCH'], x[1]['LWPOLYLINE'], x[1]['LINE']), 
                          reverse=True)
    
    print("📊 LAYERS (ordenados por relevância):\n")
    print(f"{'LAYER':<50} {'HATCH':>8} {'LWPOLY':>8} {'POLY':>8} {'LINE':>8} {'INSERT':>8}")
    print("=" * 100)
    
    for layer, counts in layers_sorted[:30]:  # Top 30
        print(f"{layer:<50} {counts['HATCH']:>8} {counts['LWPOLYLINE']:>8} "
              f"{counts['POLYLINE']:>8} {counts['LINE']:>8} {counts['INSERT']:>8}")
    
    print(f"\n📈 Total de layers: {len(stats)}")
    
    # Sugestão de layers relevantes
    print("\n💡 LAYERS SUGERIDOS PARA ALVENARIA (com HATCH > 0):")
    for layer, counts in layers_sorted:
        if counts['HATCH'] > 0 and 'WALL' in layer.upper():
            print(f"  ✓ {layer} ({counts['HATCH']} hatchs)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3.11 scripts/analise_layers_dxf.py <arquivo.dxf>")
        sys.exit(1)
    
    analisar_layers(sys.argv[1])
