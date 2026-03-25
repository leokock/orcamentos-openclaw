#!/usr/bin/env python3.11
"""
Extrai quantitativos de projetos Telefônico/Telecomunicações de DXFs.
Dados extraídos:
  1. Diâmetros de eletrodutos (textos com ø)
  2. Dimensões de caixas de passagem / calhas
  3. Metragens de cabos (polylines em layers de conduite)
  4. Equipamentos de salas técnicas (racks, patch panels)
  5. Blocos / componentes (contagem)
"""
import sys
import re
import json
import math
import ezdxf
from pathlib import Path
from collections import Counter, defaultdict

def extract_polyline_length(entity):
    """Calculate total length of a POLYLINE or LWPOLYLINE entity."""
    try:
        if entity.dxftype() == 'LWPOLYLINE':
            points = list(entity.get_points(format='xy'))
        elif entity.dxftype() == 'POLYLINE':
            points = [(v.dxf.location.x, v.dxf.location.y) for v in entity.vertices]
        else:
            return 0.0
        
        total = 0.0
        for i in range(len(points) - 1):
            dx = points[i+1][0] - points[i][0]
            dy = points[i+1][1] - points[i][1]
            total += math.sqrt(dx*dx + dy*dy)
        
        # If closed, add closing segment
        if hasattr(entity.dxf, 'flags') and entity.dxf.flags & 1:  # closed flag
            dx = points[0][0] - points[-1][0]
            dy = points[0][1] - points[-1][1]
            total += math.sqrt(dx*dx + dy*dy)
        elif entity.dxftype() == 'LWPOLYLINE' and entity.closed:
            dx = points[0][0] - points[-1][0]
            dy = points[0][1] - points[-1][1]
            total += math.sqrt(dx*dx + dy*dy)
            
        return total
    except Exception:
        return 0.0

def extract_line_length(entity):
    """Calculate length of a LINE entity."""
    try:
        start = entity.dxf.start
        end = entity.dxf.end
        dx = end.x - start.x
        dy = end.y - start.y
        return math.sqrt(dx*dx + dy*dy)
    except Exception:
        return 0.0

def classify_block(name):
    """Classify a block reference by its component type."""
    name_lower = name.lower()
    
    if 'cotovelo' in name_lower and 'eletroduto' in name_lower:
        return 'Cotovelo Eletroduto'
    elif 'caixa de passagem' in name_lower:
        return 'Caixa de Passagem'
    elif 'caixa 4x2' in name_lower:
        if 'câmera' in name_lower or 'camera' in name_lower:
            return 'Caixa 4x2 - Câmera'
        elif 'interfone' in name_lower:
            return 'Caixa 4x2 - Interfone'
        elif 'controle de acesso' in name_lower:
            return 'Caixa 4x2 - Controle de Acesso'
        elif 'informática' in name_lower or 'rj45' in name_lower:
            return 'Caixa 4x2 - Dados/Telefone'
        else:
            return 'Caixa 4x2 - Outros'
    elif 'caixa 4x4' in name_lower:
        if 'informática' in name_lower or 'rj45' in name_lower:
            return 'Caixa 4x4 - Dados/Telefone'
        else:
            return 'Caixa 4x4 - Outros'
    elif 'quadro de distribuição' in name_lower or 'rack' in name_lower:
        return 'Rack/Quadro Distribuição'
    elif 'simbologia conduíte' in name_lower:
        if 'múltiplo' in name_lower:
            return 'Conduíte Múltiplo (símbolo)'
        elif 'subindo' in name_lower:
            return 'Conduíte Vertical - Sobe'
        elif 'descendo' in name_lower:
            return 'Conduíte Vertical - Desce'
        else:
            return 'Conduíte (símbolo)'
    elif 'simbologia condutores telecom' in name_lower:
        if 'cftv' in name_lower:
            return 'Condutor CFTV'
        elif 'utp' in name_lower:
            return 'Condutor UTP'
        elif 'cci' in name_lower:
            return 'Condutor CCI'
        elif 'cordplast' in name_lower:
            return 'Condutor Cordplast'
        elif 'fibra' in name_lower:
            return 'Condutor Fibra Óptica'
        else:
            return 'Condutor Telecom (outros)'
    elif 'bucha terminal' in name_lower:
        return 'Bucha Terminal'
    elif 'conector box' in name_lower:
        return 'Conector Box/Arruela'
    elif 'placa' in name_lower and 'cega' in name_lower:
        return 'Placa Cega'
    elif 'sensor' in name_lower:
        return 'Sensor'
    elif 'intercomunicador' in name_lower:
        return 'Intercomunicador'
    elif '_ifc' in name_lower or '_dwg' in name_lower:
        return None  # skip xref blocks
    else:
        return f'Outros: {name[:60]}'

def process_dxf(dxf_path):
    """Process a single DXF file and return extracted data."""
    doc = ezdxf.readfile(str(dxf_path))
    msp = doc.modelspace()
    
    result = {
        'arquivo': Path(dxf_path).name,
        'eletrodutos': [],          # diâmetros encontrados
        'eletrodutos_resumo': {},    # contagem por diâmetro
        'caixas_passagem': [],       # dimensões de CPs
        'ambientes': [],             # nomes de ambientes
        'equipamentos': [],          # racks, DGs, etc
        'componentes': {},           # contagem de blocos classificados
        'conduit_layers': {},        # comprimento por layer de conduite
        'textos_relevantes': [],     # textos com info técnica
        'total_polylines_conduit': 0,
        'total_comprimento_conduit_mm': 0.0,
    }
    
    # Regex for conduit diameters
    re_diam = re.compile(r'(\d+)\s*x\s*ø\s*([\d\s¼½¾⅛⅜⅝⅞/"]+)', re.IGNORECASE)
    re_cp_dim = re.compile(r'\((\d+)\s*x\s*(\d+)\s*x?\s*(\d+)?\s*cm\)', re.IGNORECASE)
    
    diameter_counter = Counter()
    
    # Process all entities
    for entity in msp:
        etype = entity.dxftype()
        layer = entity.dxf.layer if hasattr(entity.dxf, 'layer') else ''
        
        # --- TEXT / MTEXT ---
        if etype in ('TEXT', 'MTEXT'):
            text = entity.dxf.text if etype == 'TEXT' else entity.text
            text = text.strip()
            if not text:
                continue
            
            # Conduit diameters
            m = re_diam.search(text)
            if m:
                qty = m.group(1)
                diam = m.group(2).strip()
                key = f"{qty}xø{diam}"
                diameter_counter[key] += 1
                direction = ''
                if 'sobe' in text.lower():
                    direction = 'Sobe'
                elif 'desce' in text.lower():
                    direction = 'Desce'
                result['eletrodutos'].append({
                    'spec': key,
                    'texto_original': text,
                    'direcao': direction,
                    'layer': layer
                })
            
            # Junction box dimensions
            m_cp = re_cp_dim.search(text)
            if m_cp:
                dims = f"{m_cp.group(1)}x{m_cp.group(2)}"
                if m_cp.group(3):
                    dims += f"x{m_cp.group(3)}"
                dims += "cm"
                result['caixas_passagem'].append({
                    'dimensao': dims,
                    'texto_original': text,
                    'layer': layer
                })
            
            # Equipment labels
            text_lower = text.lower()
            if any(kw in text_lower for kw in ['rack', 'd.g.', 'dg ', 'quadro', 'patch']):
                result['equipamentos'].append({
                    'descricao': text,
                    'layer': layer
                })
            
            # Room names (from G-____-____-TEXT layer)
            if 'TEXT' in layer and not re_diam.search(text) and not text.startswith('*') and not text.startswith('\\f'):
                if len(text) > 2 and not text.replace(' ','').isdigit():
                    result['ambientes'].append(text)
            
            # Other relevant technical text
            if any(kw in text_lower for kw in ['sensor', 'intercomunicador', 'motor', 'sinalizador', 'câmera', 'antena', 'telemetria']):
                result['textos_relevantes'].append({
                    'texto': text,
                    'layer': layer
                })
        
        # --- BLOCK REFERENCES ---
        elif etype == 'INSERT':
            block_name = entity.dxf.name
            classified = classify_block(block_name)
            if classified:
                result['componentes'][classified] = result['componentes'].get(classified, 0) + 1
        
        # --- POLYLINES on conduit layers ---
        elif etype in ('POLYLINE', 'LWPOLYLINE', 'LINE'):
            conduit_layers = ['E-POWR-CNDT-OTLN', 'E-DATA-____-OTLN', 
                            '-0-ELETROWATTS - E - Eletrodutos _ Teto_Parede']
            if layer in conduit_layers:
                if etype == 'LINE':
                    length = extract_line_length(entity)
                else:
                    length = extract_polyline_length(entity)
                
                if length > 0:
                    result['conduit_layers'][layer] = result['conduit_layers'].get(layer, 0) + length
                    result['total_polylines_conduit'] += 1
                    result['total_comprimento_conduit_mm'] += length
    
    # Summary
    result['eletrodutos_resumo'] = dict(diameter_counter.most_common())
    
    # Deduplicate ambientes
    result['ambientes'] = list(dict.fromkeys(result['ambientes']))
    
    return result

def format_report(data, floor_name):
    """Format extraction data as markdown report."""
    lines = [f"# Extração Telefônico — {floor_name}\n"]
    lines.append(f"**Arquivo:** `{data['arquivo']}`\n")
    
    # 1. Eletrodutos
    lines.append("## 1. Eletrodutos (Diâmetros)\n")
    if data['eletrodutos_resumo']:
        lines.append("| Especificação | Qtd ocorrências |")
        lines.append("|---|---|")
        for spec, count in sorted(data['eletrodutos_resumo'].items(), key=lambda x: -x[1]):
            lines.append(f"| {spec} | {count} |")
        
        # Vertical routing
        sobe = [e for e in data['eletrodutos'] if e['direcao'] == 'Sobe']
        desce = [e for e in data['eletrodutos'] if e['direcao'] == 'Desce']
        if sobe or desce:
            lines.append(f"\n*Eletrodutos verticais:* {len(sobe)} sobem, {len(desce)} descem")
    else:
        lines.append("*Nenhum diâmetro de eletroduto encontrado nos textos.*")
    
    # 2. Caixas de Passagem
    lines.append("\n## 2. Caixas de Passagem / Calhas\n")
    if data['caixas_passagem']:
        cp_counter = Counter(cp['dimensao'] for cp in data['caixas_passagem'])
        lines.append("| Dimensão | Qtd |")
        lines.append("|---|---|")
        for dim, count in cp_counter.most_common():
            lines.append(f"| {dim} | {count} |")
    else:
        lines.append("*Nenhuma caixa de passagem com dimensão encontrada.*")
    
    # 3. Comprimentos de cabos/conduits
    lines.append("\n## 3. Metragens de Conduits (Polylines)\n")
    if data['conduit_layers']:
        total_m = data['total_comprimento_conduit_mm'] / 1000.0
        lines.append(f"**Total de polylines em layers de conduit:** {data['total_polylines_conduit']}")
        lines.append(f"**Comprimento total estimado:** {total_m:.1f} m\n")
        lines.append("| Layer | Comprimento (m) |")
        lines.append("|---|---|")
        for layer, length in data['conduit_layers'].items():
            lines.append(f"| {layer} | {length/1000:.1f} |")
        lines.append("\n> ⚠️ Comprimentos em unidades do DWG (presumido mm). Verificar escala do desenho.")
    else:
        lines.append("*Nenhuma polyline em layers de conduit encontrada.*")
    
    # 4. Componentes (blocos)
    lines.append("\n## 4. Componentes (Blocos)\n")
    if data['componentes']:
        lines.append("| Componente | Qtd |")
        lines.append("|---|---|")
        for comp, count in sorted(data['componentes'].items(), key=lambda x: -x[1]):
            if not comp.startswith('Outros:'):
                lines.append(f"| {comp} | {count} |")
        # Outros
        outros = {k: v for k, v in data['componentes'].items() if k.startswith('Outros:')}
        if outros:
            lines.append(f"\n*Blocos não classificados:* {len(outros)} tipos")
    else:
        lines.append("*Nenhum bloco de componente encontrado.*")
    
    # 5. Equipamentos / Salas Técnicas
    lines.append("\n## 5. Equipamentos / Salas Técnicas\n")
    if data['equipamentos']:
        for eq in data['equipamentos']:
            lines.append(f"- {eq['descricao']}")
    else:
        lines.append("*Nenhum equipamento técnico identificado.*")
    
    # 6. Ambientes
    lines.append("\n## 6. Ambientes Identificados\n")
    if data['ambientes']:
        for amb in data['ambientes'][:30]:
            lines.append(f"- {amb.strip()}")
    
    # 7. Textos técnicos relevantes
    if data['textos_relevantes']:
        lines.append("\n## 7. Outros Equipamentos / Sensores\n")
        seen = set()
        for t in data['textos_relevantes']:
            if t['texto'] not in seen:
                lines.append(f"- {t['texto']}")
                seen.add(t['texto'])
    
    return '\n'.join(lines)


if __name__ == '__main__':
    dxf_dir = Path("/Users/leokock/orcamentos/executivos/thozen-electra/quantitativos/telefonico/dxf")
    out_dir = Path("/Users/leokock/orcamentos/executivos/thozen-electra/quantitativos/telefonico")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Map files to floor names
    floor_map = {
        'T02': '01° Pavto. Térreo [T.A]',
        'T03': '01° Pavto. Térreo [T.B]',
        'T04': '02° Pavto. G1 [T.A]',
        'T05': '02° Pavto. G1 [T.B]',
        'T06': '03° Pavto. G2 [T.A]',
        'T07': '03° Pavto. G2 [T.B]',
        'T08': '04° Pavto. G3 [T.A]',
        'T09': '04° Pavto. G3 [T.B]',
        'T10': '05° Pavto. G4 [T.A]',
        'T11': '05° Pavto. G4 [T.B]',
        'T12': '06° Pavto. G5 [T.A]',
        'T13': '06° Pavto. G5 [T.B]',
        'T14': '07° Pavto. Lazer [T.A]',
        'T15': '07° Pavto. Lazer [T.B]',
        'T16': '08°~31° Pavto. Tipo (24x) [T.A]',
        'T17': '08°~31° Pavto. Tipo (24x) [T.B]',
        'T18': 'Casa de Máquinas [T.A]',
        'T19': 'Casa de Máquinas [T.B]',
    }
    
    all_data = {}
    consolidated = defaultdict(lambda: Counter())
    total_conduit_length = 0.0
    total_polylines = 0
    
    dxf_files = sorted(dxf_dir.glob("*.dxf"))
    print(f"Encontrados {len(dxf_files)} arquivos DXF\n")
    
    for dxf_file in dxf_files:
        # Extract Txx code
        match = re.search(r'T(\d{2})', dxf_file.name)
        if not match:
            print(f"⚠️ Não consegui identificar código T em: {dxf_file.name}")
            continue
        
        t_code = f"T{match.group(1)}"
        floor_name = floor_map.get(t_code, t_code)
        
        print(f"📄 Processando {t_code}: {floor_name}...")
        
        try:
            data = process_dxf(dxf_file)
            all_data[t_code] = data
            
            # Write individual report
            report = format_report(data, floor_name)
            report_file = out_dir / f"extracao_{t_code.lower()}.md"
            report_file.write_text(report, encoding='utf-8')
            print(f"   ✅ Salvo: {report_file.name}")
            
            # Consolidate
            for spec, count in data['eletrodutos_resumo'].items():
                consolidated['eletrodutos'][spec] += count
            for cp in data['caixas_passagem']:
                consolidated['caixas_passagem'][cp['dimensao']] += 1
            for comp, count in data['componentes'].items():
                if not comp.startswith('Outros:'):
                    consolidated['componentes'][comp] += count
            total_conduit_length += data['total_comprimento_conduit_mm']
            total_polylines += data['total_polylines_conduit']
            
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            import traceback
            traceback.print_exc()
    
    # Write consolidated report
    print(f"\n📊 Gerando relatório consolidado...")
    
    cons_lines = ["# Quantitativos Telefônico — Consolidado\n"]
    cons_lines.append(f"**Projeto:** Thozen Electra Towers — Rubens Alves")
    cons_lines.append(f"**Disciplina:** Telecomunicações (Telefônico)")
    cons_lines.append(f"**Arquivos processados:** {len(all_data)} DXFs")
    cons_lines.append(f"**Torres:** A e B\n")
    
    # Eletrodutos consolidado
    cons_lines.append("## 1. Eletrodutos — Resumo por Diâmetro\n")
    cons_lines.append("| Especificação | Total ocorrências |")
    cons_lines.append("|---|---|")
    for spec, count in consolidated['eletrodutos'].most_common():
        cons_lines.append(f"| {spec} | {count} |")
    
    # Caixas consolidado
    cons_lines.append("\n## 2. Caixas de Passagem — Resumo\n")
    cons_lines.append("| Dimensão | Total |")
    cons_lines.append("|---|---|")
    for dim, count in consolidated['caixas_passagem'].most_common():
        cons_lines.append(f"| {dim} | {count} |")
    
    # Conduit lengths
    cons_lines.append("\n## 3. Comprimento Total de Conduits\n")
    cons_lines.append(f"- **Polylines totais:** {total_polylines}")
    cons_lines.append(f"- **Comprimento total estimado:** {total_conduit_length/1000:.1f} m")
    cons_lines.append("\n> ⚠️ Valores em unidades do DWG — verificar escala (provável mm)")
    
    # Componentes consolidado
    cons_lines.append("\n## 4. Componentes — Resumo\n")
    cons_lines.append("| Componente | Total |")
    cons_lines.append("|---|---|")
    for comp, count in consolidated['componentes'].most_common():
        cons_lines.append(f"| {comp} | {count} |")
    
    # Per-floor summary
    cons_lines.append("\n## 5. Resumo por Pavimento\n")
    cons_lines.append("| Pavimento | Eletrodutos | CPs | Componentes | Conduit (m) |")
    cons_lines.append("|---|---|---|---|---|")
    for t_code in sorted(all_data.keys(), key=lambda x: int(x[1:])):
        d = all_data[t_code]
        floor = floor_map.get(t_code, t_code)
        n_elet = sum(d['eletrodutos_resumo'].values())
        n_cp = len(d['caixas_passagem'])
        n_comp = sum(v for k, v in d['componentes'].items() if not k.startswith('Outros:'))
        conduit_m = d['total_comprimento_conduit_mm'] / 1000
        cons_lines.append(f"| {floor} | {n_elet} | {n_cp} | {n_comp} | {conduit_m:.1f} |")
    
    cons_file = out_dir / "consolidado_telefonico.md"
    cons_file.write_text('\n'.join(cons_lines), encoding='utf-8')
    print(f"✅ Consolidado salvo: {cons_file}")
    
    # Also save raw JSON
    json_file = out_dir / "dados_brutos_telefonico.json"
    # Convert Counters to dicts for JSON
    json_data = {}
    for t_code, data in all_data.items():
        json_data[t_code] = data
    json_file.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✅ JSON bruto salvo: {json_file}")
    
    print(f"\n🎉 Extração concluída! {len(all_data)} pavimentos processados.")
