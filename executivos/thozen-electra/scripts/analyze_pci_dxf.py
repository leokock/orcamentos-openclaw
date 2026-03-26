#!/usr/bin/env python3.11
"""Analyze PCI Civil DXF files from Electra Towers to extract quantities."""

import ezdxf
import json
import math
import os
import re
from collections import defaultdict
from pathlib import Path

DXF_DIR = Path("/Users/leokock/orcamentos/executivos/thozen-electra/dxf-pci/civil")

# Files to analyze (dot versions only)
FILES = {
    "IGC01_Terreo_TA": '348 - IGC 01 [08] rev.00 - 01° PAVTO. TÉRREO (T.A).dxf',
    "IGC02_Terreo_TB": '348 - IGC 02 [08] rev.00 - 01° PAVTO. TÉRREO (T.B).dxf',
    "IGC03_Garagem_TA": '348 - IGC 03 [08] rev.00 - 02°~06° PAVTO. GARAGEM 01~05 (T.A).dxf',
    "IGC04_Garagem_TB": '348 - IGC 04 [08] rev.00 - 02°~06° PAVTO. GARAGEM 01~05 (T.B).dxf',
    "IGC05_Lazer_TA": '348 - IGC 05 [08] rev.00 - 07° PAVTO. LAZER (T.A).dxf',
    "IGC06_Lazer_TB": '348 - IGC 06 [08] rev.00 - 07° PAVTO. LAZER (T.B).dxf',
    "IGC07_Tipo_TA": '348 - IGC 07 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.A).dxf',
    "IGC08_Tipo_TB": '348 - IGC 08 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.B).dxf',
}

# PCI-related keywords for layer identification
PCI_LAYER_KEYWORDS = [
    'TUBO', 'PIPE', 'FG', 'INC', 'SHP', 'HIDRA', 'HIDR', 'SPKR', 'SPRINK',
    'PCI', 'INCENDIO', 'INCÊNDIO', 'FIRE', 'MANGOT', 'EXTIN', 'VALV', 'REG',
    'PLACA', 'SINAL', 'ABRIGO', 'ALARME', 'DETECTOR', 'BOMBA', 'RESERV',
    'CANALIZ', 'PRESSURIZ', 'SHAFT', 'COLUNA', 'RAMAL', 'SUBIDA', 'DESCIDA',
    'REDE', 'CONEXA', 'JOELHO', 'TE_', 'LUVA', 'COTOV', 'REGISTRO'
]

# Red color indices in AutoCAD (color 1 = red, also near-reds)
RED_COLORS = {1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# Block name patterns for equipment
EQUIPMENT_PATTERNS = {
    'hidrante': ['HIDR', 'ABRIGO', 'MANGOT', 'MANGUEIRA', 'HYDRANT'],
    'extintor': ['EXTIN', 'PQS', 'CO2', 'ABC', 'EXTINGUISH'],
    'valvula': ['VALV', 'REG', 'RETENC', 'GAVETA', 'GLOBO', 'GOVERNO', 'VALVE'],
    'sinalizacao': ['PLACA', 'SINAL', 'E5', 'E6', 'E7', 'ROTA', 'SAIDA', 'EXIT', 'EMERGENCIA'],
    'detector': ['DETECT', 'ALARME', 'SENSOR', 'ACION', 'CENTRAL', 'SIRENE'],
    'sprinkler': ['SPKR', 'SPRINK', 'BICO', 'CHUVEIRO'],
    'conexao': ['JOELHO', 'TE_', 'LUVA', 'COTOV', 'CURVA', 'REDUCAO', 'UNIAO', 'FLANGE', 'NIPLE'],
    'bomba': ['BOMBA', 'PUMP', 'MOTOR', 'PRESSUR'],
}

# Diameter patterns in text
DIAMETER_PATTERN = re.compile(r'(?:Ø|DN|ø|φ|Φ)\s*(\d+(?:\.\d+)?)', re.IGNORECASE)
DIAMETER_PATTERN2 = re.compile(r'(\d+(?:\.\d+)?)\s*(?:mm|")', re.IGNORECASE)


def get_entity_length(entity):
    """Calculate length of LINE, LWPOLYLINE, POLYLINE, ARC entities."""
    try:
        dxftype = entity.dxftype()
        if dxftype == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            dx = end.x - start.x
            dy = end.y - start.y
            dz = end.z - start.z if hasattr(end, 'z') and hasattr(start, 'z') else 0
            return math.sqrt(dx**2 + dy**2 + dz**2)
        
        elif dxftype == 'LWPOLYLINE':
            # Get all points
            points = list(entity.get_points(format='xy'))
            total = 0.0
            for i in range(len(points) - 1):
                dx = points[i+1][0] - points[i][0]
                dy = points[i+1][1] - points[i][1]
                total += math.sqrt(dx**2 + dy**2)
            # Check if closed
            if entity.closed and len(points) > 2:
                dx = points[0][0] - points[-1][0]
                dy = points[0][1] - points[-1][1]
                total += math.sqrt(dx**2 + dy**2)
            return total
        
        elif dxftype == 'POLYLINE':
            points = [(v.dxf.location.x, v.dxf.location.y) for v in entity.vertices]
            total = 0.0
            for i in range(len(points) - 1):
                dx = points[i+1][0] - points[i][0]
                dy = points[i+1][1] - points[i][1]
                total += math.sqrt(dx**2 + dy**2)
            if entity.is_closed and len(points) > 2:
                dx = points[0][0] - points[-1][0]
                dy = points[0][1] - points[-1][1]
                total += math.sqrt(dx**2 + dy**2)
            return total
        
        elif dxftype == 'ARC':
            radius = entity.dxf.radius
            start_angle = math.radians(entity.dxf.start_angle)
            end_angle = math.radians(entity.dxf.end_angle)
            angle = end_angle - start_angle
            if angle < 0:
                angle += 2 * math.pi
            return abs(radius * angle)
        
        elif dxftype == 'CIRCLE':
            return 2 * math.pi * entity.dxf.radius
        
    except Exception as e:
        return 0.0
    return 0.0


def is_pci_layer(layer_name, layer_color=None):
    """Check if layer is PCI-related by name or color."""
    upper = layer_name.upper()
    for kw in PCI_LAYER_KEYWORDS:
        if kw in upper:
            return True
    if layer_color is not None and layer_color in RED_COLORS:
        return True
    return False


def classify_block(block_name):
    """Classify a block INSERT by its name."""
    upper = block_name.upper()
    for category, patterns in EQUIPMENT_PATTERNS.items():
        for pat in patterns:
            if pat in upper:
                return category
    return None


def extract_diameter_from_text(text):
    """Extract diameter from text annotation."""
    match = DIAMETER_PATTERN.search(text)
    if match:
        return float(match.group(1))
    match = DIAMETER_PATTERN2.search(text)
    if match:
        return float(match.group(1))
    return None


def analyze_dxf(filepath):
    """Analyze a single DXF file."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {os.path.basename(filepath)}")
    print(f"{'='*60}")
    
    try:
        doc = ezdxf.readfile(filepath)
    except Exception as e:
        print(f"  ERROR reading file: {e}")
        return None
    
    msp = doc.modelspace()
    
    # Build layer color map
    layer_colors = {}
    for layer in doc.layers:
        try:
            layer_colors[layer.dxf.name] = layer.dxf.color
        except:
            pass
    
    # Results structure
    result = {
        'layers': {},
        'pci_layers': {},
        'tubulacao': {
            'total_length': 0.0,
            'by_layer': {},
            'by_entity_type': defaultdict(float),
        },
        'blocos': {
            'all': defaultdict(int),
            'classified': defaultdict(lambda: defaultdict(int)),
        },
        'textos': {
            'diametros': [],
            'especificacoes': [],
            'notas': [],
        },
        'entity_counts': defaultdict(int),
    }
    
    # Count entities per layer
    layer_entity_counts = defaultdict(lambda: defaultdict(int))
    
    for entity in msp:
        try:
            dxftype = entity.dxftype()
            layer = entity.dxf.layer if hasattr(entity.dxf, 'layer') else '0'
            result['entity_counts'][dxftype] += 1
            layer_entity_counts[layer][dxftype] += 1
            
            # Get entity color (entity color or layer color)
            entity_color = None
            try:
                entity_color = entity.dxf.color if hasattr(entity.dxf, 'color') and entity.dxf.color != 256 else layer_colors.get(layer)
            except:
                entity_color = layer_colors.get(layer)
            
            layer_color = layer_colors.get(layer)
            is_pci = is_pci_layer(layer, layer_color) or (entity_color is not None and entity_color in RED_COLORS)
            
            # Process geometric entities for length
            if dxftype in ('LINE', 'LWPOLYLINE', 'POLYLINE', 'ARC', 'CIRCLE'):
                length = get_entity_length(entity)
                if length > 0:
                    if is_pci:
                        result['tubulacao']['total_length'] += length
                        if layer not in result['tubulacao']['by_layer']:
                            result['tubulacao']['by_layer'][layer] = {'length': 0.0, 'count': 0, 'color': layer_color}
                        result['tubulacao']['by_layer'][layer]['length'] += length
                        result['tubulacao']['by_layer'][layer]['count'] += 1
                        result['tubulacao']['by_entity_type'][dxftype] += length
            
            # Process INSERT blocks
            elif dxftype == 'INSERT':
                block_name = entity.dxf.name
                result['blocos']['all'][block_name] += 1
                category = classify_block(block_name)
                if category:
                    result['blocos']['classified'][category][block_name] += 1
            
            # Process text entities
            elif dxftype in ('TEXT', 'MTEXT'):
                try:
                    if dxftype == 'TEXT':
                        text = entity.dxf.text
                    else:
                        text = entity.text if hasattr(entity, 'text') else entity.dxf.text
                    
                    if text:
                        # Check for diameter annotations
                        diam = extract_diameter_from_text(text)
                        if diam:
                            result['textos']['diametros'].append({
                                'text': text.strip()[:100],
                                'diameter': diam,
                                'layer': layer,
                            })
                        
                        # Check for material specs
                        upper_text = text.upper()
                        if any(kw in upper_text for kw in ['GALVAN', 'FERRO', 'AÇO', 'COBRE', 'CPVC', 'PPR', 'PVC', 'SCHEDULE', 'SCH', 'NBREU', 'DIN', 'ABNT']):
                            result['textos']['especificacoes'].append({
                                'text': text.strip()[:200],
                                'layer': layer,
                            })
                        
                        # PCI-related notes
                        if any(kw in upper_text for kw in ['INCÊNDIO', 'INCENDIO', 'HIDRANTE', 'EXTINTOR', 'SPRINKLER', 'ALARME', 'PRESSUR', 'MANGOT', 'SHP', 'SPK']):
                            result['textos']['notas'].append({
                                'text': text.strip()[:200],
                                'layer': layer,
                            })
                except:
                    pass
        except Exception as e:
            pass
    
    # Store layer info
    for layer_name, entities in layer_entity_counts.items():
        color = layer_colors.get(layer_name)
        total = sum(entities.values())
        info = {
            'color': color,
            'total_entities': total,
            'entity_types': dict(entities),
            'is_pci': is_pci_layer(layer_name, color),
        }
        result['layers'][layer_name] = info
        if info['is_pci']:
            result['pci_layers'][layer_name] = info
    
    # Convert defaultdicts
    result['blocos']['all'] = dict(result['blocos']['all'])
    result['blocos']['classified'] = {k: dict(v) for k, v in result['blocos']['classified'].items()}
    result['tubulacao']['by_entity_type'] = dict(result['tubulacao']['by_entity_type'])
    result['entity_counts'] = dict(result['entity_counts'])
    
    # Print summary
    print(f"\n  Total layers: {len(result['layers'])}")
    print(f"  PCI layers identified: {len(result['pci_layers'])}")
    print(f"  Total tubulação length (raw units): {result['tubulacao']['total_length']:.2f}")
    
    if result['pci_layers']:
        print(f"\n  PCI Layers:")
        for ln, info in sorted(result['pci_layers'].items()):
            print(f"    - {ln} (color={info['color']}, entities={info['total_entities']})")
    
    if result['tubulacao']['by_layer']:
        print(f"\n  Tubulação by layer:")
        for ln, info in sorted(result['tubulacao']['by_layer'].items(), key=lambda x: -x[1]['length']):
            print(f"    - {ln}: {info['length']:.2f} units ({info['count']} entities, color={info['color']})")
    
    if result['blocos']['classified']:
        print(f"\n  Equipment blocks:")
        for cat, blocks in sorted(result['blocos']['classified'].items()):
            total = sum(blocks.values())
            print(f"    {cat}: {total} total")
            for bn, count in sorted(blocks.items(), key=lambda x: -x[1])[:5]:
                print(f"      - {bn}: {count}")
    
    if result['textos']['diametros']:
        print(f"\n  Diameter annotations: {len(result['textos']['diametros'])}")
        diams = set(d['diameter'] for d in result['textos']['diametros'])
        print(f"    Diameters found: {sorted(diams)}")
    
    return result


def determine_unit_scale(results):
    """Try to determine the unit scale from drawing analysis."""
    # Look at typical pipe lengths and dimensions
    # A typical floor has ~50-200m of piping
    # If values are in mm, raw would be 50000-200000
    # If values are in cm, raw would be 5000-20000
    # If values are in m, raw would be 50-200
    
    # Check typical LINE lengths in PCI layers
    all_lengths = []
    for key, data in results.items():
        if data and data['tubulacao']['total_length'] > 0:
            all_lengths.append(data['tubulacao']['total_length'])
    
    if not all_lengths:
        return 1.0, 'unknown'
    
    avg = sum(all_lengths) / len(all_lengths)
    
    # Heuristic: typical floor PCI pipe ~30-300m
    if avg > 100000:  # likely mm
        return 0.001, 'mm'
    elif avg > 1000:  # likely cm
        return 0.01, 'cm'
    elif avg > 10:  # likely m (already good)
        return 1.0, 'm'
    else:  # very small, maybe m with small floor
        return 1.0, 'm'


def main():
    results = {}
    
    for key, filename in FILES.items():
        filepath = DXF_DIR / filename
        if filepath.exists():
            result = analyze_dxf(str(filepath))
            results[key] = result
        else:
            print(f"\nFILE NOT FOUND: {filename}")
            results[key] = None
    
    # Determine units
    scale, unit = determine_unit_scale(results)
    print(f"\n{'='*60}")
    print(f"UNIT DETECTION: Likely {unit} (scale to meters: {scale})")
    print(f"{'='*60}")
    
    # Also check block names across all files
    print(f"\n{'='*60}")
    print(f"ALL UNIQUE BLOCK NAMES (across all files)")
    print(f"{'='*60}")
    all_blocks = defaultdict(int)
    for key, data in results.items():
        if data:
            for bn, count in data['blocos']['all'].items():
                all_blocks[bn] += count
    
    for bn, count in sorted(all_blocks.items(), key=lambda x: -x[1])[:50]:
        cat = classify_block(bn) or ''
        print(f"  {bn}: {count} {f'[{cat}]' if cat else ''}")
    
    # All unique layers across files
    print(f"\n{'='*60}")
    print(f"ALL UNIQUE LAYERS (across all files)")
    print(f"{'='*60}")
    all_layers = {}
    for key, data in results.items():
        if data:
            for ln, info in data['layers'].items():
                if ln not in all_layers:
                    all_layers[ln] = {'color': info['color'], 'total': 0, 'is_pci': info['is_pci'], 'files': []}
                all_layers[ln]['total'] += info['total_entities']
                all_layers[ln]['files'].append(key)
    
    for ln, info in sorted(all_layers.items(), key=lambda x: -x[1]['total'])[:60]:
        pci_tag = ' [PCI]' if info['is_pci'] else ''
        print(f"  {ln} (color={info['color']}, entities={info['total']}, files={len(info['files'])}){pci_tag}")
    
    # Consolidation
    print(f"\n{'='*60}")
    print(f"CONSOLIDATION SUMMARY")
    print(f"{'='*60}")
    
    consolidation = {
        'embasamento': {
            'terreo': {'ta': 'IGC01_Terreo_TA', 'tb': 'IGC02_Terreo_TB', 'rep': 1},
            'garagem': {'ta': 'IGC03_Garagem_TA', 'tb': 'IGC04_Garagem_TB', 'rep': 5},
            'lazer': {'ta': 'IGC05_Lazer_TA', 'tb': 'IGC06_Lazer_TB', 'rep': 1},
        },
        'torre_a': {
            'tipo': {'ta': 'IGC07_Tipo_TA', 'rep': 24},
        },
        'torre_b': {
            'tipo': {'tb': 'IGC08_Tipo_TB', 'rep': 24},
        },
    }
    
    total_pipe_m = 0.0
    total_equipment = defaultdict(int)
    
    for uc_name, uc_data in consolidation.items():
        print(f"\n  {uc_name.upper()}:")
        uc_pipe = 0.0
        uc_equip = defaultdict(int)
        
        for pav_name, pav_data in uc_data.items():
            rep = pav_data['rep']
            pav_pipe = 0.0
            pav_equip = defaultdict(int)
            
            for tower_key in ['ta', 'tb']:
                if tower_key in pav_data:
                    file_key = pav_data[tower_key]
                    data = results.get(file_key)
                    if data:
                        pipe_raw = data['tubulacao']['total_length']
                        pipe_m = pipe_raw * scale
                        pav_pipe += pipe_m
                        
                        for cat, blocks in data['blocos']['classified'].items():
                            cat_total = sum(blocks.values())
                            pav_equip[cat] += cat_total
            
            pav_pipe_total = pav_pipe * rep
            uc_pipe += pav_pipe_total
            
            for cat, count in pav_equip.items():
                uc_equip[cat] += count * rep
            
            print(f"    {pav_name}: {pav_pipe:.2f}m/prancha × {rep} = {pav_pipe_total:.2f}m")
            if pav_equip:
                for cat, count in sorted(pav_equip.items()):
                    print(f"      {cat}: {count}/prancha × {rep} = {count * rep}")
        
        total_pipe_m += uc_pipe
        for cat, count in uc_equip.items():
            total_equipment[cat] += count
        
        print(f"    SUBTOTAL {uc_name}: {uc_pipe:.2f}m tubulação")
    
    print(f"\n  TOTAL GERAL:")
    print(f"    Tubulação: {total_pipe_m:.2f}m")
    for cat, count in sorted(total_equipment.items()):
        print(f"    {cat}: {count}")
    
    # Save JSON
    output_dir = Path("/Users/leokock/orcamentos/executivos/thozen-electra/quantitativos")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    json_output = {
        'unit_detected': unit,
        'scale_to_meters': scale,
        'files': {},
        'consolidation': {},
        'totals': {
            'tubulacao_m': total_pipe_m,
            'equipment': dict(total_equipment),
        },
        'all_blocks': dict(all_blocks),
        'all_layers': {ln: {'color': info['color'], 'total': info['total'], 'is_pci': info['is_pci']} for ln, info in all_layers.items()},
    }
    
    for key, data in results.items():
        if data:
            # Serialize for JSON (remove non-serializable)
            json_output['files'][key] = {
                'tubulacao': {
                    'total_raw': data['tubulacao']['total_length'],
                    'total_m': data['tubulacao']['total_length'] * scale,
                    'by_layer': {ln: {'length_raw': info['length'], 'length_m': info['length'] * scale, 'count': info['count'], 'color': info['color']} for ln, info in data['tubulacao']['by_layer'].items()},
                    'by_entity_type': {k: v * scale for k, v in data['tubulacao']['by_entity_type'].items()},
                },
                'blocos': {
                    'classified': data['blocos']['classified'],
                    'all_count': len(data['blocos']['all']),
                },
                'textos': data['textos'],
                'pci_layers': list(data['pci_layers'].keys()),
                'entity_counts': data['entity_counts'],
            }
    
    # Build consolidation summary for JSON
    for uc_name, uc_data in consolidation.items():
        uc_result = {'pavimentos': {}, 'total_tubulacao_m': 0.0, 'total_equipment': {}}
        for pav_name, pav_data in uc_data.items():
            rep = pav_data['rep']
            pav_pipe = 0.0
            pav_equip = defaultdict(int)
            for tower_key in ['ta', 'tb']:
                if tower_key in pav_data:
                    file_key = pav_data[tower_key]
                    data = results.get(file_key)
                    if data:
                        pav_pipe += data['tubulacao']['total_length'] * scale
                        for cat, blocks in data['blocos']['classified'].items():
                            pav_equip[cat] += sum(blocks.values())
            
            uc_result['pavimentos'][pav_name] = {
                'pipe_per_floor_m': pav_pipe,
                'repetitions': rep,
                'pipe_total_m': pav_pipe * rep,
                'equipment_per_floor': dict(pav_equip),
                'equipment_total': {cat: count * rep for cat, count in pav_equip.items()},
            }
            uc_result['total_tubulacao_m'] += pav_pipe * rep
            for cat, count in pav_equip.items():
                uc_result['total_equipment'][cat] = uc_result['total_equipment'].get(cat, 0) + count * rep
        
        json_output['consolidation'][uc_name] = uc_result
    
    json_path = output_dir / 'pci-dxf-analise.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, ensure_ascii=False, indent=2)
    print(f"\nJSON saved to: {json_path}")
    
    return json_output


if __name__ == '__main__':
    main()
