#!/usr/bin/env python3.11
"""Analyze PEE DXF files - refined classification."""

import ezdxf
import json
import math
import re
from collections import defaultdict, Counter
from pathlib import Path

DXF_DIR = Path("/Users/leokock/orcamentos/executivos/thozen-electra/dxf-pci/eletrico")

FILES = {
    "PEE01_Terreo_TA": '348 - PEE 01 [22] rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO [T. A].dxf',
    "PEE02_Terreo_TB": '348 - PEE 02 [22] rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO [T. B].dxf',
    "PEE03_G1_TA": '348 - PEE 03 [22] rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1 [T. A].dxf',
    "PEE04_G1_TB": '348 - PEE 04 [22] rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1 [T. B].dxf',
    "PEE05_G2_TA": '348 - PEE 05 [22] rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2 [T. A].dxf',
    "PEE06_G2_TB": '348 - PEE 06 [22] rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2 [T. B].dxf',
    "PEE07_G3_TA": '348 - PEE 07 [22] rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3 [T. A].dxf',
    "PEE08_G3_TB": '348 - PEE 08 [22] rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3 [T. B].dxf',
    "PEE09_G4_TA": '348 - PEE 09 [22] rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4 [T. A].dxf',
    "PEE10_G4_TB": '348 - PEE 10 [22] rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4 [T. B].dxf',
    "PEE11_G5_TA": '348 - PEE 11 [22] rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5 [T. A].dxf',
    "PEE12_G5_TB": '348 - PEE 12 [22] rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5 [T. B].dxf',
    "PEE13_Lazer_TA": '348 - PEE 13 [22] rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER [T. A].dxf',
    "PEE14_Lazer_TB": '348 - PEE 14 [22] rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER [T. B].dxf',
    "PEE15_Tipo_TA": '348 - PEE 15 [22] rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO (24x) [T. A].dxf',
    "PEE16_Tipo_TB": '348 - PEE 16 [22] rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO (24x) [T. B].dxf',
    "PEE17_CM_TA": '348 - PEE 17 [22] rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS [T. A].dxf',
    "PEE18_CM_TB": '348 - PEE 18 [22] rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS [T. B].dxf',
}

# More specific patterns to avoid false positives
def classify_block_specific(block_name):
    """Stricter classification."""
    upper = block_name.upper()
    
    # Exclude generic electrical components
    if any(x in upper for x in ['COTOVELO', 'ELETRODUTO', 'CAIXA 4X2', 'CONDUTOR', 'CONDUIT', 'ELBOW']):
        # Unless it specifically mentions PCI equipment
        if not any(x in upper for x in ['DETECTOR', 'ALARME', 'EMERGENCIA', 'INCENDIO', 'EMERGÊNCIA', 'INCÊNDIO']):
            return None
    
    # Specific equipment patterns
    if any(x in upper for x in ['DETECTOR DE FUMAÇA', 'DETECTOR DE FUMACA', 'SMOKE DETECTOR']):
        return 'detector_fumaca'
    if any(x in upper for x in ['DETECTOR DE TEMPERATURA', 'DETECTOR DE CALOR', 'HEAT DETECTOR']):
        return 'detector_temperatura'
    if any(x in upper for x in ['ACIONADOR MANUAL', 'BOTOEIRA DE ALARME', 'BREAK GLASS', 'PULL STATION']):
        return 'acionador_manual'
    if any(x in upper for x in ['SIRENE', 'AVISADOR', 'HORN', 'STROBE']):
        return 'sirene_alarme'
    if any(x in upper for x in ['CENTRAL DE ALARME', 'PAINEL DE INCENDIO', 'FACP']):
        return 'central_alarme'
    if any(x in upper for x in ['ILUMINAÇÃO DE EMERGÊNCIA', 'ILUMINACAO DE EMERGENCIA', 'BLOCO DE ILUMINAÇÃO', 
                                 'BLOCO DE ILUMINACAO', 'LUZ DE EMERGENCIA', 'EXIT SIGN']):
        return 'iluminacao_emergencia'
    if any(x in upper for x in ['HIDRANTE', 'ABRIGO DE MANGUEIRA', 'MANGOTINHO']):
        return 'hidrante'
    if any(x in upper for x in ['EXTINTOR']):
        return 'extintor'
    if any(x in upper for x in ['SPRINKLER', 'BICO DE SPRINKLER', 'SPK']):
        return 'sprinkler'
    if any(x in upper for x in ['PLACA DE SAÍDA', 'PLACA DE SAIDA', 'SINALIZAÇÃO DE EMERGÊNCIA', 
                                 'SINALIZACAO DE EMERGENCIA', 'ROTA DE FUGA']):
        return 'sinalizacao_emergencia'
    
    return None


def get_entity_length(entity):
    """Calculate length."""
    try:
        dxftype = entity.dxftype()
        if dxftype == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            return math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
        elif dxftype == 'LWPOLYLINE':
            points = list(entity.get_points(format='xy'))
            total = sum(math.sqrt((points[i+1][0] - points[i][0])**2 + 
                                   (points[i+1][1] - points[i][1])**2)
                        for i in range(len(points) - 1))
            if entity.closed and len(points) > 2:
                total += math.sqrt((points[0][0] - points[-1][0])**2 + 
                                    (points[0][1] - points[-1][1])**2)
            return total
    except:
        pass
    return 0.0


def analyze_dxf(filepath, key):
    """Analyze a single DXF file."""
    print(f"\n  {key}...")
    
    try:
        doc = ezdxf.readfile(filepath)
    except Exception as e:
        print(f"    ERROR: {e}")
        return None
    
    msp = doc.modelspace()
    
    result = {
        'blocks_pci': defaultdict(lambda: defaultdict(int)),
        'block_totals_pci': defaultdict(int),
        'all_blocks': Counter(),  # All block names for inspection
        'layers': defaultdict(int),
    }
    
    for entity in msp:
        try:
            dxftype = entity.dxftype()
            layer = entity.dxf.layer if hasattr(entity.dxf, 'layer') else '0'
            result['layers'][layer] += 1
            
            if dxftype == 'INSERT':
                block_name = entity.dxf.name
                result['all_blocks'][block_name] += 1
                
                category = classify_block_specific(block_name)
                if category:
                    result['blocks_pci'][category][block_name] += 1
                    result['block_totals_pci'][category] += 1
        except:
            pass
    
    result['blocks_pci'] = {k: dict(v) for k, v in result['blocks_pci'].items()}
    result['block_totals_pci'] = dict(result['block_totals_pci'])
    result['all_blocks'] = dict(result['all_blocks'])
    result['layers'] = dict(result['layers'])
    
    if result['block_totals_pci']:
        print(f"    PCI: {result['block_totals_pci']}")
    else:
        print(f"    No PCI equipment found with strict matching")
    
    return result


def main():
    print("="*60)
    print("PEE Analysis v2 - Strict Equipment Matching")
    print("="*60)
    
    results = {}
    all_blocks_global = Counter()
    
    for key, filename in FILES.items():
        filepath = DXF_DIR / filename
        if filepath.exists():
            results[key] = analyze_dxf(str(filepath), key)
            if results[key]:
                all_blocks_global.update(results[key]['all_blocks'])
        else:
            results[key] = None
    
    # Show all unique block names for manual inspection
    print("\n" + "="*60)
    print("ALL UNIQUE BLOCK NAMES (top 100 by frequency)")
    print("="*60)
    
    for bn, count in all_blocks_global.most_common(100):
        # Shorten
        short = bn.split(' - ')[0] if ' - ' in bn else bn[:80]
        # Check if it looks PCI-related
        upper = bn.upper()
        tags = []
        if any(x in upper for x in ['DETECT', 'FUMAÇA', 'FUMACA', 'SMOKE']):
            tags.append('DETECT')
        if any(x in upper for x in ['ALARM', 'SIRENE', 'AVISADOR']):
            tags.append('ALARM')
        if any(x in upper for x in ['EMERG', 'SAÍDA', 'SAIDA', 'EXIT']):
            tags.append('EMERG')
        if any(x in upper for x in ['INCEND', 'INCÊND', 'FIRE']):
            tags.append('FIRE')
        if any(x in upper for x in ['HIDRA', 'MANGOT']):
            tags.append('HIDR')
        if any(x in upper for x in ['EXTIN']):
            tags.append('EXT')
        
        tag_str = f" [{'/'.join(tags)}]" if tags else ""
        print(f"  [{count:4d}x] {short}{tag_str}")
    
    # Consolidate PCI items found
    print("\n" + "="*60)
    print("PCI EQUIPMENT FOUND (strict matching)")
    print("="*60)
    
    total_pci = defaultdict(int)
    for key, data in results.items():
        if data:
            for cat, count in data['block_totals_pci'].items():
                total_pci[cat] += count
    
    if total_pci:
        print(f"\n  Total across all files:")
        for cat, count in sorted(total_pci.items()):
            print(f"    {cat}: {count}")
    else:
        print("\n  No PCI equipment matched with strict patterns.")
        print("  Check block names above to identify actual equipment symbols.")
    
    # Save JSON
    output = {
        'source': 'PEE DXF Analysis v2',
        'files': {key: data['block_totals_pci'] if data else None for key, data in results.items()},
        'totals': dict(total_pci),
        'all_blocks_sample': dict(all_blocks_global.most_common(200)),
    }
    
    output_path = Path("/Users/leokock/orcamentos/executivos/thozen-electra/quantitativos/pci-pee-analise-v2.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nJSON saved: {output_path}")


if __name__ == '__main__':
    main()
