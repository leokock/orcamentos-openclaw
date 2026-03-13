#!/usr/bin/env python3
"""
Script para extração completa de quantitativos estruturais do IFC Oxford (Mussi)
Gera relatório detalhado com volumes de concreto, áreas de forma e especificações
"""

import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.shape
from collections import defaultdict
import json

print("🔧 Iniciando processamento do IFC estrutural Oxford...")

# Carregar arquivo IFC
ifc_path = "/Users/leokock/orcamentos/projetos/mussi-oxford/02. PROJETO ESTRUTURAL/EST 260305/IFC 260305/EST_OXFORD600.12.11.2025.ifc"
print(f"📂 Carregando: {ifc_path}")
ifc = ifcopenshell.open(ifc_path)
print(f"✅ IFC carregado: {ifc.schema} | {len(ifc.by_type('IfcProduct'))} produtos")

# Estruturas de dados
dados = {
    'lajes': [],
    'vigas': [],
    'pilares': [],
    'fundacao': [],
    'escadas': [],
    'rampas': []
}

stats = {
    'total_concreto_m3': 0,
    'total_formas_m2': 0,
    'por_pavimento': defaultdict(lambda: {'concreto': 0, 'formas': 0, 'elementos': 0}),
    'por_tipo': defaultdict(lambda: {'quantidade': 0, 'concreto': 0, 'formas': 0})
}

def extrair_pavimento(elemento):
    """Extrai nome do pavimento do elemento"""
    try:
        # Tentar pegar do ContainedInStructure
        for rel in elemento.ContainedInStructure:
            if rel.RelatingStructure.is_a("IfcBuildingStorey"):
                return rel.RelatingStructure.Name or "SEM_PAVIMENTO"
    except:
        pass
    
    # Tentar pegar de Psets
    try:
        psets = ifcopenshell.util.element.get_psets(elemento)
        for pset_name, pset_data in psets.items():
            if 'Storey' in str(pset_data):
                return str(pset_data.get('Storey', 'SEM_PAVIMENTO'))
            if 'Level' in str(pset_data):
                return str(pset_data.get('Level', 'SEM_PAVIMENTO'))
    except:
        pass
    
    return "SEM_PAVIMENTO"

def extrair_material(elemento):
    """Extrai informações de material (fck, etc)"""
    try:
        psets = ifcopenshell.util.element.get_psets(elemento)
        material_info = {}
        
        for pset_name, pset_data in psets.items():
            if 'concreto' in pset_name.lower() or 'concrete' in pset_name.lower():
                material_info['fck'] = pset_data.get('fck') or pset_data.get('Fck') or pset_data.get('ResistenciaCaracteristica')
            if 'aço' in pset_name.lower() or 'aco' in pset_name.lower() or 'steel' in pset_name.lower():
                material_info['categoria_aco'] = pset_data.get('Categoria') or pset_data.get('Category')
        
        # Tentar do material associado
        if hasattr(elemento, 'HasAssociations'):
            for assoc in elemento.HasAssociations:
                if assoc.is_a('IfcRelAssociatesMaterial'):
                    mat = assoc.RelatingMaterial
                    if hasattr(mat, 'Name'):
                        material_info['material_name'] = mat.Name
        
        return material_info
    except:
        return {}

def calcular_volume_area(elemento):
    """Calcula volume e área de forma do elemento"""
    try:
        # Tentar pegar quantidades do IFC
        for definition in elemento.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                prop_set = definition.RelatingPropertyDefinition
                if prop_set.is_a('IfcElementQuantity'):
                    volume = None
                    area = None
                    
                    for quantity in prop_set.Quantities:
                        if quantity.is_a('IfcQuantityVolume'):
                            if 'volume' in quantity.Name.lower() or 'concreto' in quantity.Name.lower():
                                volume = quantity.VolumeValue
                        elif quantity.is_a('IfcQuantityArea'):
                            if 'forma' in quantity.Name.lower() or 'surface' in quantity.Name.lower():
                                area = quantity.AreaValue
                    
                    if volume or area:
                        return volume, area
        
        # Se não encontrou, tentar calcular da geometria
        # (mais pesado, só se necessário)
        return None, None
    except Exception as e:
        return None, None

print("\n📊 Processando elementos estruturais...")

# LAJES
print("  → Lajes...")
lajes = ifc.by_type("IfcSlab")
for laje in lajes:
    pavimento = extrair_pavimento(laje)
    volume, area = calcular_volume_area(laje)
    material = extrair_material(laje)
    
    dados['lajes'].append({
        'id': laje.GlobalId,
        'nome': laje.Name or f"Laje_{laje.id()}",
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area,
        'material': material
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Lajes']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Lajes']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Lajes']['quantidade'] += 1

print(f"    ✓ {len(lajes)} lajes processadas")

# VIGAS
print("  → Vigas...")
vigas = ifc.by_type("IfcBeam")
for viga in vigas:
    pavimento = extrair_pavimento(viga)
    volume, area = calcular_volume_area(viga)
    material = extrair_material(viga)
    
    dados['vigas'].append({
        'id': viga.GlobalId,
        'nome': viga.Name or f"Viga_{viga.id()}",
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area,
        'material': material
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Vigas']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Vigas']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Vigas']['quantidade'] += 1

print(f"    ✓ {len(vigas)} vigas processadas")

# PILARES
print("  → Pilares...")
pilares = ifc.by_type("IfcColumn")
for pilar in pilares:
    pavimento = extrair_pavimento(pilar)
    volume, area = calcular_volume_area(pilar)
    material = extrair_material(pilar)
    
    dados['pilares'].append({
        'id': pilar.GlobalId,
        'nome': pilar.Name or f"Pilar_{pilar.id()}",
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area,
        'material': material
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Pilares']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Pilares']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Pilares']['quantidade'] += 1

print(f"    ✓ {len(pilares)} pilares processados")

# FUNDAÇÃO
print("  → Fundação...")
fundacao = ifc.by_type("IfcFooting") + ifc.by_type("IfcPile")
for elem in fundacao:
    tipo = "Bloco/Sapata" if elem.is_a("IfcFooting") else "Estaca"
    pavimento = extrair_pavimento(elem)
    volume, area = calcular_volume_area(elem)
    material = extrair_material(elem)
    
    dados['fundacao'].append({
        'id': elem.GlobalId,
        'nome': elem.Name or f"{tipo}_{elem.id()}",
        'tipo': tipo,
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area,
        'material': material
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Fundação']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Fundação']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Fundação']['quantidade'] += 1

print(f"    ✓ {len(fundacao)} elementos de fundação processados")

# ESCADAS E RAMPAS
print("  → Escadas e rampas...")
escadas = ifc.by_type("IfcStair") + ifc.by_type("IfcStairFlight")
for escada in escadas:
    pavimento = extrair_pavimento(escada)
    volume, area = calcular_volume_area(escada)
    
    dados['escadas'].append({
        'id': escada.GlobalId,
        'nome': escada.Name or f"Escada_{escada.id()}",
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Escadas']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Escadas']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Escadas']['quantidade'] += 1

rampas = ifc.by_type("IfcRamp") + ifc.by_type("IfcRampFlight")
for rampa in rampas:
    pavimento = extrair_pavimento(rampa)
    volume, area = calcular_volume_area(rampa)
    
    dados['rampas'].append({
        'id': rampa.GlobalId,
        'nome': rampa.Name or f"Rampa_{rampa.id()}",
        'pavimento': pavimento,
        'volume_m3': volume,
        'area_forma_m2': area
    })
    
    if volume:
        stats['total_concreto_m3'] += volume
        stats['por_pavimento'][pavimento]['concreto'] += volume
        stats['por_tipo']['Rampas']['concreto'] += volume
    if area:
        stats['total_formas_m2'] += area
        stats['por_pavimento'][pavimento]['formas'] += area
        stats['por_tipo']['Rampas']['formas'] += area
    
    stats['por_pavimento'][pavimento]['elementos'] += 1
    stats['por_tipo']['Rampas']['quantidade'] += 1

print(f"    ✓ {len(escadas)} escadas e {len(rampas)} rampas processadas")

# Salvar JSON intermediário
json_output = "/Users/leokock/orcamentos/projetos/mussi-oxford/oxford-ifc-dados-brutos.json"
with open(json_output, 'w', encoding='utf-8') as f:
    json.dump({
        'dados': dados,
        'stats': {
            'total_concreto_m3': stats['total_concreto_m3'],
            'total_formas_m2': stats['total_formas_m2'],
            'por_pavimento': dict(stats['por_pavimento']),
            'por_tipo': dict(stats['por_tipo'])
        }
    }, f, indent=2, ensure_ascii=False)

print(f"\n✅ Dados brutos salvos em: {json_output}")
print(f"\n📈 RESUMO GERAL:")
print(f"   Concreto total: {stats['total_concreto_m3']:.2f} m³")
print(f"   Formas total: {stats['total_formas_m2']:.2f} m²")
print(f"   Pavimentos identificados: {len(stats['por_pavimento'])}")
print(f"   Tipos de elemento: {len(stats['por_tipo'])}")
