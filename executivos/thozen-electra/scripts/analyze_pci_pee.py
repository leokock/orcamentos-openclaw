#!/usr/bin/env python3.11
"""Analyze PCI Elétrico (PEE) DXF files for fire detection/alarm systems."""

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

# PCI-related block keywords
PCI_BLOCK_PATTERNS = {
    'detector_fumaca': ['DETECT', 'FUMAÇA', 'FUMACA', 'SMOKE', 'DF'],
    'detector_temperatura': ['TEMP', 'CALOR', 'HEAT', 'DT'],
    'acionador_manual': ['ACION', 'MANUAL', 'BREAK', 'GLASS', 'PULL', 'AM'],
    'sirene': ['SIRENE', 'ALARME', 'SIREN', 'HORN', 'STROBE', 'AV'],
    'central_alarme': ['CENTRAL', 'PAINEL', 'PANEL', 'FACP'],
    'iluminacao_emergencia': ['EMERG', 'EXIT', 'SAIDA', 'SAÍDA', 'IE', 'LUZ'],
    'hidrante': ['HIDR', 'ABRIGO', 'MANGOT', 'HYDRANT', 'HID'],
    'extintor': ['EXTIN', 'PQS', 'CO2', 'ABC', 'EXT'],
    'sprinkler': ['SPKR', 'SPRINK', 'BICO', 'SPK'],
    'sinalizacao': ['PLACA', 'SINAL', 'E5', 'E6', 'E7', 'ROTA', 'SIGN'],
}

# PCI-related layer patterns
PCI_LAYER_KEYWORDS = ['ALARM', 'DETECT', 'FIRE', 'PCI', 'EMERG', 'SAIDA', 'EXIT', 
                       'SIRENE', 'CENTRAL', 'HIDRA', 'EXTIN', 'SPK', 'INCEND', 'INCÊND']


def get_entity_length(entity):
    """Calculate length of geometric entities."""
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
        elif dxftype == 'ARC':
            radius = entity.dxf.radius
            angle = math.radians(entity.dxf.end_angle - entity.dxf.start_angle)
            if angle < 0:
                angle += 2 * math.pi
            return abs(radius * angle)
    except:
        pass
    return 0.0


def classify_block(block_name):
    """Classify a block by PCI category."""
    upper = block_name.upper()
    for category, patterns in PCI_BLOCK_PATTERNS.items():
        for pat in patterns:
            if pat in upper:
                return category
    return None


def is_pci_layer(layer_name):
    """Check if layer is PCI-related."""
    upper = layer_name.upper()
    return any(kw in upper for kw in PCI_LAYER_KEYWORDS)


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
        'layers': {},
        'blocks': defaultdict(lambda: defaultdict(int)),
        'block_totals': defaultdict(int),
        'eletrodutos_length': 0.0,
        'texts': [],
    }
    
    layer_entity_counts = defaultdict(lambda: defaultdict(int))
    
    for entity in msp:
        try:
            dxftype = entity.dxftype()
            layer = entity.dxf.layer if hasattr(entity.dxf, 'layer') else '0'
            layer_entity_counts[layer][dxftype] += 1
            
            # Count cable/conduit length on certain layers
            if dxftype in ('LINE', 'LWPOLYLINE', 'ARC'):
                length = get_entity_length(entity)
                if length > 0:
                    upper_layer = layer.upper()
                    # Eletrodutos/cabos em layers E- ou com FIRE/ALARM
                    if any(kw in upper_layer for kw in ['E-', 'ELEC', 'FIRE', 'ALARM', 'CABO', 'WIRE', 'CONDUIT']):
                        result['eletrodutos_length'] += length
            
            elif dxftype == 'INSERT':
                block_name = entity.dxf.name
                category = classify_block(block_name)
                if category:
                    result['blocks'][category][block_name] += 1
                    result['block_totals'][category] += 1
            
            elif dxftype in ('TEXT', 'MTEXT'):
                try:
                    text = entity.dxf.text if dxftype == 'TEXT' else (entity.text if hasattr(entity, 'text') else '')
                    if text:
                        upper = text.upper()
                        if any(kw in upper for kw in ['DETECT', 'ALARM', 'SIRENE', 'EMERG', 'INCÊND', 'INCEND', 
                                                       'SAÍDA', 'SAIDA', 'EXIT', 'HIDRA', 'EXTIN', 'SPK']):
                            result['texts'].append(text.strip()[:150])
                except:
                    pass
        except:
            pass
    
    # Store layer info
    for layer_name, entities in layer_entity_counts.items():
        result['layers'][layer_name] = {
            'total': sum(entities.values()),
            'entities': dict(entities),
            'is_pci': is_pci_layer(layer_name),
        }
    
    result['blocks'] = {k: dict(v) for k, v in result['blocks'].items()}
    result['block_totals'] = dict(result['block_totals'])
    
    # Print summary
    if result['block_totals']:
        print(f"    PCI blocks: {result['block_totals']}")
    
    return result


def main():
    print("="*60)
    print("Analyzing PEE (Projeto Elétrico de Emergência) DXF files")
    print("="*60)
    
    results = {}
    
    for key, filename in FILES.items():
        filepath = DXF_DIR / filename
        if filepath.exists():
            results[key] = analyze_dxf(str(filepath), key)
        else:
            print(f"\n  {key}: FILE NOT FOUND")
            results[key] = None
    
    # Consolidate
    print("\n" + "="*60)
    print("CONSOLIDATION SUMMARY")
    print("="*60)
    
    # Group by UC
    consolidation = {
        'embasamento': {
            'terreo': {'files': ['PEE01_Terreo_TA', 'PEE02_Terreo_TB'], 'rep': 1},
            'g1': {'files': ['PEE03_G1_TA', 'PEE04_G1_TB'], 'rep': 1},
            'g2': {'files': ['PEE05_G2_TA', 'PEE06_G2_TB'], 'rep': 1},
            'g3': {'files': ['PEE07_G3_TA', 'PEE08_G3_TB'], 'rep': 1},
            'g4': {'files': ['PEE09_G4_TA', 'PEE10_G4_TB'], 'rep': 1},
            'g5': {'files': ['PEE11_G5_TA', 'PEE12_G5_TB'], 'rep': 1},
            'lazer': {'files': ['PEE13_Lazer_TA', 'PEE14_Lazer_TB'], 'rep': 1},
            'cm': {'files': ['PEE17_CM_TA', 'PEE18_CM_TB'], 'rep': 1},
        },
        'torre_a': {
            'tipo': {'files': ['PEE15_Tipo_TA'], 'rep': 24},
        },
        'torre_b': {
            'tipo': {'files': ['PEE16_Tipo_TB'], 'rep': 24},
        },
    }
    
    total_equipment = defaultdict(int)
    uc_totals = {}
    
    for uc_name, uc_data in consolidation.items():
        print(f"\n  {uc_name.upper()}:")
        uc_equipment = defaultdict(int)
        
        for pav_name, pav_data in uc_data.items():
            rep = pav_data['rep']
            pav_equipment = defaultdict(int)
            
            for file_key in pav_data['files']:
                data = results.get(file_key)
                if data:
                    for cat, count in data['block_totals'].items():
                        pav_equipment[cat] += count
            
            if pav_equipment:
                print(f"    {pav_name} (×{rep}):")
                for cat, count in sorted(pav_equipment.items()):
                    total = count * rep
                    print(f"      {cat}: {count}/prancha × {rep} = {total}")
                    uc_equipment[cat] += total
        
        print(f"    SUBTOTAL {uc_name}: {dict(uc_equipment)}")
        uc_totals[uc_name] = dict(uc_equipment)
        for cat, count in uc_equipment.items():
            total_equipment[cat] += count
    
    print(f"\n  TOTAL GERAL:")
    for cat, count in sorted(total_equipment.items()):
        print(f"    {cat}: {count}")
    
    # Get all block names for reference
    print("\n" + "="*60)
    print("ALL PCI BLOCK NAMES (across all files)")
    print("="*60)
    
    all_blocks = defaultdict(lambda: defaultdict(int))
    for key, data in results.items():
        if data:
            for cat, blocks in data['blocks'].items():
                for bn, count in blocks.items():
                    all_blocks[cat][bn] += count
    
    for cat in sorted(all_blocks.keys()):
        print(f"\n  {cat}:")
        for bn, count in sorted(all_blocks[cat].items(), key=lambda x: -x[1])[:10]:
            # Shorten block name
            short = bn.split(' - ')[0] if ' - ' in bn else bn[:80]
            print(f"    [{count}x] {short}")
    
    # Sample texts
    print("\n" + "="*60)
    print("SAMPLE PCI-RELATED TEXTS")
    print("="*60)
    all_texts = []
    for key, data in results.items():
        if data and data['texts']:
            all_texts.extend(data['texts'])
    
    unique_texts = Counter(all_texts)
    for text, count in unique_texts.most_common(30):
        clean = re.sub(r'\\[A-Za-z][^;]*;', '', text)
        clean = re.sub(r'\{|\}', '', clean).strip()
        if clean:
            print(f"  [{count}x] {clean[:100]}")
    
    # Save JSON
    output = {
        'source': 'PEE (PCI Elétrico)',
        'files': {},
        'consolidation': uc_totals,
        'totals': dict(total_equipment),
        'all_block_names': {cat: dict(blocks) for cat, blocks in all_blocks.items()},
    }
    
    for key, data in results.items():
        if data:
            output['files'][key] = {
                'block_totals': data['block_totals'],
                'eletrodutos_length_raw': data['eletrodutos_length'],
            }
    
    output_path = Path("/Users/leokock/orcamentos/executivos/thozen-electra/quantitativos/pci-pee-analise.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nJSON saved to: {output_path}")


if __name__ == '__main__':
    main()
