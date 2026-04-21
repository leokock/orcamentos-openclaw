#!/usr/bin/env python3.11
"""Deep-dive analysis of DXF text annotations and block names to understand content."""

import ezdxf
import json
import re
from collections import defaultdict, Counter
from pathlib import Path

DXF_DIR = Path("/Users/leokock/orcamentos/executivos/thozen-electra/dxf-pci/civil")

FILES = {
    "IGC01_Terreo_TA": '348 - IGC 01 [08] rev.00 - 01° PAVTO. TÉRREO (T.A).dxf',
    "IGC02_Terreo_TB": '348 - IGC 02 [08] rev.00 - 01° PAVTO. TÉRREO (T.B).dxf',
    "IGC05_Lazer_TA": '348 - IGC 05 [08] rev.00 - 07° PAVTO. LAZER (T.A).dxf',
    "IGC07_Tipo_TA": '348 - IGC 07 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.A).dxf',
    "IGC08_Tipo_TB": '348 - IGC 08 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.B).dxf',
}


def analyze_texts(filepath, label):
    """Extract ALL text from DXF to understand what the project is about."""
    print(f"\n{'='*60}")
    print(f"{label}: {Path(filepath).name}")
    print(f"{'='*60}")
    
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()
    
    all_texts = []
    block_names = Counter()
    
    for entity in msp:
        dxftype = entity.dxftype()
        
        if dxftype in ('TEXT', 'MTEXT'):
            try:
                if dxftype == 'TEXT':
                    text = entity.dxf.text
                else:
                    text = entity.text if hasattr(entity, 'text') else ''
                if text and text.strip():
                    all_texts.append(text.strip())
            except:
                pass
        
        elif dxftype == 'INSERT':
            block_names[entity.dxf.name] += 1
    
    # Print all unique texts
    print(f"\n  ALL TEXT ANNOTATIONS ({len(all_texts)} total):")
    unique_texts = Counter(all_texts)
    for text, count in unique_texts.most_common(80):
        # Clean MTEXT formatting
        clean = re.sub(r'\\[A-Za-z][^;]*;', '', text)
        clean = re.sub(r'\{|\}', '', clean)
        clean = clean.strip()
        if clean:
            print(f"    [{count}x] {clean[:120]}")
    
    # Print block names (simplified)
    print(f"\n  BLOCK NAMES ({len(block_names)} unique):")
    for bn, count in block_names.most_common(30):
        # Extract the meaningful part
        short = bn.split(' - ')[0] if ' - ' in bn else bn
        print(f"    [{count}x] {short[:100]}")
    
    # Check for any PCI-related content
    pci_keywords = ['INCENDIO', 'INCÊNDIO', 'HIDRANTE', 'EXTINTOR', 'SPRINKLER', 
                    'ALARME', 'MANGOTINHO', 'SPK', 'COMBATE', 'SHP', 'SHAFT']
    gas_keywords = ['GÁS', 'GAS', 'COBRE', 'PEX', 'MEDIDOR', 'REGULADOR', 
                    'FECHO RÁPIDO', 'ESFERA', 'ERMU', 'CANALIZ']
    
    pci_found = []
    gas_found = []
    
    for text in all_texts:
        upper = text.upper()
        for kw in pci_keywords:
            if kw in upper:
                pci_found.append(text[:100])
                break
        for kw in gas_keywords:
            if kw in upper:
                gas_found.append(text[:100])
                break
    
    print(f"\n  PCI-related texts found: {len(pci_found)}")
    for t in list(set(pci_found))[:10]:
        print(f"    - {t}")
    
    print(f"\n  GAS-related texts found: {len(gas_found)}")
    for t in list(set(gas_found))[:10]:
        print(f"    - {t}")
    
    # Check layer names in title block / annotations for project info
    for entity in doc.modelspace():
        if entity.dxftype() in ('TEXT', 'MTEXT'):
            try:
                text = entity.dxf.text if entity.dxftype() == 'TEXT' else (entity.text if hasattr(entity, 'text') else '')
                if text:
                    upper = text.upper()
                    if any(kw in upper for kw in ['PROJETO', 'DISCIPLINA', 'TÍTULO', 'TITULO', 'PRANCHA', 'IGC', 'REVISÃO']):
                        clean = re.sub(r'\\[A-Za-z][^;]*;', '', text)
                        clean = re.sub(r'\{|\}', '', clean)
                        print(f"\n  TITLE/PROJECT TEXT: {clean[:200]}")
            except:
                pass


for label, filename in FILES.items():
    filepath = DXF_DIR / filename
    if filepath.exists():
        analyze_texts(str(filepath), label)
