#!/usr/bin/env python3.11
"""
Extrator de quantitativos de instalações telefônicas/lógicas (IFC)
Projeto: Thozen Electra
"""

import ifcopenshell
import os
import sys
from pathlib import Path
from collections import defaultdict
import json

def extract_telecom_data(ifc_file):
    """Extrai dados de instalações telefônicas de um arquivo IFC"""
    
    try:
        ifc = ifcopenshell.open(ifc_file)
    except Exception as e:
        print(f"❌ Erro ao abrir {ifc_file}: {e}", file=sys.stderr)
        return None
    
    filename = Path(ifc_file).name
    
    data = {
        'arquivo': filename,
        'pavimento': extract_floor_name(filename),
        'pontos_logicos': [],
        'cabos': [],
        'eletrodutos': [],
        'calhas': [],
        'quadros': [],
        'racks': [],
        'patch_panels': [],
        'tomadas_rj45': [],
        'equipamentos': []
    }
    
    # Detectar esquema IFC
    schema = ifc.wrapped_data.schema
    
    # Buscar todos os elementos relevantes (compatível IFC2X3 e IFC4)
    # 1. Pontos lógicos (outlets, data points)
    try:
        for element in ifc.by_type('IfcOutlet'):
            info = extract_element_info(element, 'ponto_logico')
            if info:
                data['pontos_logicos'].append(info)
    except RuntimeError:
        pass  # IfcOutlet não existe no IFC2X3
    
    # 2. Cabos
    try:
        for element in ifc.by_type('IfcCableSegment'):
            info = extract_cable_info(element)
            if info:
                data['cabos'].append(info)
    except RuntimeError:
        pass
    
    # 3. Eletrodutos
    try:
        for element in ifc.by_type('IfcPipeSegment'):
            # Verificar se é eletroduto (não hidráulico)
            info = extract_conduit_info(element)
            if info and is_telecom_conduit(info):
                data['eletrodutos'].append(info)
    except RuntimeError:
        pass
    
    # 4. Calhas
    try:
        for element in ifc.by_type('IfcCableCarrierSegment'):
            info = extract_tray_info(element)
            if info:
                data['calhas'].append(info)
    except RuntimeError:
        # Em IFC2X3 pode estar como IfcCableCarrierFittingType
        pass
    
    # 5. Quadros/DGs
    try:
        for element in ifc.by_type('IfcElectricDistributionBoard'):
            info = extract_element_info(element, 'quadro')
            if info:
                data['quadros'].append(info)
    except RuntimeError:
        pass
    
    # 6. Equipamentos diversos (racks, switches, etc)
    try:
        for element in ifc.by_type('IfcFlowTerminal'):
            info = extract_element_info(element, 'equipamento')
            if info and is_telecom_equipment(info):
                data['equipamentos'].append(info)
    except RuntimeError:
        pass
    
    # Buscar por propriedades customizadas - Proxy elements (comum em IFC2X3)
    try:
        for element in ifc.by_type('IfcBuildingElementProxy'):
            info = extract_element_info(element, 'proxy')
            if info and is_telecom_related(info):
                classify_proxy_element(info, data)
    except RuntimeError:
        pass
    
    # Buscar produtos genéricos de distribuição
    try:
        for element in ifc.by_type('IfcDistributionElement'):
            info = extract_element_info(element, 'distribuicao')
            if info and is_telecom_related(info):
                classify_proxy_element(info, data)
    except RuntimeError:
        pass
    
    # Buscar anotações e símbolos (podem conter pontos lógicos)
    try:
        for element in ifc.by_type('IfcAnnotation'):
            info = extract_element_info(element, 'anotacao')
            if info and is_telecom_related(info):
                data['pontos_logicos'].append(info)
    except RuntimeError:
        pass
    
    return data

def extract_floor_name(filename):
    """Extrai nome do pavimento do nome do arquivo"""
    if 'TÉRREO' in filename:
        return 'TÉRREO'
    elif 'G1' in filename:
        return 'G1 (2º PAVTO)'
    elif 'G2' in filename:
        return 'G2 (3º PAVTO)'
    elif 'G3' in filename:
        return 'G3 (4º PAVTO)'
    elif 'G4' in filename:
        return 'G4 (5º PAVTO)'
    elif 'G5' in filename:
        return 'G5 (6º PAVTO)'
    elif 'LAZER' in filename:
        return 'LAZER (7º PAVTO)'
    elif 'TIPO' in filename:
        return 'TIPO (8º~31º PAVTO - 24x)'
    elif 'MÁQUINAS' in filename:
        return 'CASA DE MÁQUINAS'
    return 'N/A'

def extract_element_info(element, tipo):
    """Extrai informações básicas de um elemento IFC"""
    info = {
        'tipo': tipo,
        'guid': element.GlobalId,
        'nome': getattr(element, 'Name', 'N/A'),
        'descricao': getattr(element, 'Description', 'N/A'),
        'tag': getattr(element, 'Tag', 'N/A'),
        'object_type': getattr(element, 'ObjectType', 'N/A'),
        'propriedades': {}
    }
    
    # Extrair propriedades customizadas
    if hasattr(element, 'IsDefinedBy'):
        for definition in element.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                prop_set = definition.RelatingPropertyDefinition
                if prop_set.is_a('IfcPropertySet'):
                    for prop in prop_set.HasProperties:
                        if prop.is_a('IfcPropertySingleValue'):
                            info['propriedades'][prop.Name] = str(prop.NominalValue.wrappedValue) if prop.NominalValue else 'N/A'
    
    return info

def extract_cable_info(element):
    """Extrai informações específicas de cabos"""
    info = extract_element_info(element, 'cabo')
    
    # Tentar obter comprimento
    if hasattr(element, 'Quantities'):
        for qty_rel in element.Quantities:
            if qty_rel.is_a('IfcRelDefinesByProperties'):
                qty_set = qty_rel.RelatingPropertyDefinition
                if qty_set.is_a('IfcElementQuantity'):
                    for qty in qty_set.Quantities:
                        if qty.is_a('IfcQuantityLength'):
                            info['comprimento'] = qty.LengthValue
    
    # Verificar tipo de cabo (CAT5e, CAT6, CAT6A, fibra)
    nome_upper = info['nome'].upper()
    desc_upper = info['descricao'].upper()
    obj_type_upper = info['object_type'].upper()
    
    search_text = f"{nome_upper} {desc_upper} {obj_type_upper}"
    
    if 'CAT6A' in search_text or 'CAT 6A' in search_text:
        info['categoria'] = 'CAT6A'
    elif 'CAT6' in search_text or 'CAT 6' in search_text:
        info['categoria'] = 'CAT6'
    elif 'CAT5E' in search_text or 'CAT 5E' in search_text:
        info['categoria'] = 'CAT5E'
    elif 'FIBRA' in search_text or 'FIBER' in search_text or 'FO' in search_text:
        info['categoria'] = 'FIBRA ÓPTICA'
    else:
        info['categoria'] = 'N/A'
    
    return info

def extract_conduit_info(element):
    """Extrai informações de eletrodutos"""
    info = extract_element_info(element, 'eletroduto')
    
    # Tentar obter comprimento e diâmetro
    if hasattr(element, 'Quantities'):
        for qty_rel in element.Quantities:
            if qty_rel.is_a('IfcRelDefinesByProperties'):
                qty_set = qty_rel.RelatingPropertyDefinition
                if qty_set.is_a('IfcElementQuantity'):
                    for qty in qty_set.Quantities:
                        if qty.is_a('IfcQuantityLength'):
                            info['comprimento'] = qty.LengthValue
    
    # Tentar extrair diâmetro do nome ou propriedades
    import re
    for text in [info['nome'], info['descricao'], info['object_type']]:
        match = re.search(r'(\d+)\s*mm', text, re.IGNORECASE)
        if match:
            info['diametro'] = f"{match.group(1)}mm"
            break
    
    if 'diametro' not in info:
        info['diametro'] = 'N/A'
    
    return info

def extract_tray_info(element):
    """Extrai informações de calhas/eletrocalhas"""
    info = extract_element_info(element, 'calha')
    
    # Tentar obter comprimento
    if hasattr(element, 'Quantities'):
        for qty_rel in element.Quantities:
            if qty_rel.is_a('IfcRelDefinesByProperties'):
                qty_set = qty_rel.RelatingPropertyDefinition
                if qty_set.is_a('IfcElementQuantity'):
                    for qty in qty_set.Quantities:
                        if qty.is_a('IfcQuantityLength'):
                            info['comprimento'] = qty.LengthValue
    
    # Extrair dimensões
    import re
    for text in [info['nome'], info['descricao'], info['object_type']]:
        match = re.search(r'(\d+)\s*x\s*(\d+)', text)
        if match:
            info['largura'] = f"{match.group(1)}mm"
            info['altura'] = f"{match.group(2)}mm"
            break
    
    return info

def is_telecom_conduit(info):
    """Verifica se eletroduto é de telecomunicações"""
    search_text = f"{info['nome']} {info['descricao']} {info['object_type']}".upper()
    
    telecom_keywords = ['TELECOM', 'TELEFON', 'LÓGICA', 'LOGICA', 'DADOS', 'VOZ', 'CFTV', 'REDE']
    
    return any(keyword in search_text for keyword in telecom_keywords)

def is_telecom_equipment(info):
    """Verifica se equipamento é de telecomunicações"""
    search_text = f"{info['nome']} {info['descricao']} {info['object_type']}".upper()
    
    telecom_keywords = ['RACK', 'SWITCH', 'PATCH', 'DG', 'DISTRIBUIDOR', 'ROUTER', 'HUB', 'TELECOM', 'TELEFON']
    
    return any(keyword in search_text for keyword in telecom_keywords)

def is_telecom_related(info):
    """Verifica se elemento proxy é relacionado a telecomunicações"""
    search_text = f"{info['nome']} {info['descricao']} {info['object_type']}".upper()
    
    # Buscar por palavras-chave
    for key, value in info['propriedades'].items():
        search_text += f" {key} {value}".upper()
    
    telecom_keywords = ['TELECOM', 'TELEFON', 'LÓGICA', 'LOGICA', 'DADOS', 'VOZ', 'CFTV', 'REDE', 'RJ45', 'CAT6', 'CAT5', 'FIBRA']
    
    return any(keyword in search_text for keyword in telecom_keywords)

def classify_proxy_element(info, data):
    """Classifica elemento proxy em categoria apropriada"""
    search_text = f"{info['nome']} {info['descricao']} {info['object_type']}".upper()
    
    if 'RACK' in search_text:
        data['racks'].append(info)
    elif 'PATCH' in search_text:
        data['patch_panels'].append(info)
    elif 'QUADRO' in search_text or 'DG' in search_text:
        data['quadros'].append(info)
    elif 'RJ45' in search_text or 'TOMADA' in search_text:
        data['tomadas_rj45'].append(info)
    else:
        data['equipamentos'].append(info)

def main():
    ifc_dir = Path('projetos/thozen-electra/projetos/10 TELEFONICO/IFC')
    
    if not ifc_dir.exists():
        print(f"❌ Diretório não encontrado: {ifc_dir}", file=sys.stderr)
        sys.exit(1)
    
    ifc_files = sorted(ifc_dir.glob('*.ifc'))
    
    if not ifc_files:
        print(f"❌ Nenhum arquivo IFC encontrado em {ifc_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"📁 Processando {len(ifc_files)} arquivos IFC...\n")
    
    all_data = []
    
    for ifc_file in ifc_files:
        print(f"⚙️  Processando: {ifc_file.name}")
        data = extract_telecom_data(str(ifc_file))
        if data:
            all_data.append(data)
            # Resumo rápido
            print(f"   ├─ Pontos lógicos: {len(data['pontos_logicos'])}")
            print(f"   ├─ Cabos: {len(data['cabos'])}")
            print(f"   ├─ Eletrodutos: {len(data['eletrodutos'])}")
            print(f"   ├─ Calhas: {len(data['calhas'])}")
            print(f"   ├─ Quadros: {len(data['quadros'])}")
            print(f"   ├─ Racks: {len(data['racks'])}")
            print(f"   ├─ Equipamentos: {len(data['equipamentos'])}")
            print(f"   └─ Tomadas RJ45: {len(data['tomadas_rj45'])}\n")
    
    # Salvar JSON com todos os dados
    output_file = 'output/thozen-electra-telefonico-raw.json'
    os.makedirs('output', exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Dados extraídos salvos em: {output_file}")
    print(f"📊 Total de pavimentos processados: {len(all_data)}")

if __name__ == '__main__':
    main()
