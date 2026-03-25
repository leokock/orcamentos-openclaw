#!/usr/bin/env python3.11
"""
Extração de dados do arquivo IFC da obra Arminio Tavares
Para alimentar o briefing paramétrico
"""

import ifcopenshell
import json
from collections import defaultdict

# Abrir arquivo IFC
ifc_file = ifcopenshell.open('projetos/arminio-tavares/PLA_ARM_ARQ_EP_R06.ifc')

# Dados do projeto
project = ifc_file.by_type('IfcProject')[0]
building = ifc_file.by_type('IfcBuilding')[0]
storeys = ifc_file.by_type('IfcBuildingStorey')

print("=" * 80)
print(f"PROJETO: {project.Name}")
print(f"EDIFICAÇÃO: {building.Name}")
print("=" * 80)

# Organizar pavimentos
pavimentos = []
for storey in sorted(storeys, key=lambda s: s.Elevation):
    pavimentos.append({
        'nome': storey.Name,
        'elevacao': storey.Elevation,
        'descricao': storey.LongName or storey.Name
    })

print(f"\nNÚMERO DE PAVIMENTOS: {len(pavimentos)}")
print("\nPAVIMENTOS:")
for p in pavimentos:
    print(f"  {p['nome']:30} | Elevação: {p['elevacao']:8.2f}mm | {p['descricao']}")

# Extrair áreas por pavimento usando QuantityAreas
areas_por_pavimento = {}
area_total = 0.0

for storey in storeys:
    storey_name = storey.Name
    area_pavimento = 0.0
    
    # Procurar por espaços (IfcSpace) neste pavimento
    spaces = []
    for rel in storey.IsDecomposedBy or []:
        for obj in rel.RelatedObjects:
            if obj.is_a('IfcSpace'):
                spaces.append(obj)
    
    # Somar áreas dos espaços
    for space in spaces:
        # Procurar por quantidade de área
        for definition in space.IsDefinedBy or []:
            if definition.is_a('IfcRelDefinesByProperties'):
                prop_set = definition.RelatingPropertyDefinition
                if prop_set.is_a('IfcElementQuantity'):
                    for quantity in prop_set.Quantities:
                        if quantity.is_a('IfcQuantityArea'):
                            if 'Area' in quantity.Name or 'GSA' in quantity.Name or 'NetFloorArea' in quantity.Name:
                                area_pavimento += quantity.AreaValue
    
    if area_pavimento > 0:
        areas_por_pavimento[storey_name] = area_pavimento
        area_total += area_pavimento

print(f"\nÁREAS POR PAVIMENTO:")
for nome, area in areas_por_pavimento.items():
    print(f"  {nome:30} | {area:10.2f} m²")

print(f"\nÁREA TOTAL: {area_total:.2f} m²")

# Tentar extrair informações adicionais
print("\n" + "=" * 80)
print("INFORMAÇÕES ADICIONAIS DO PROJETO")
print("=" * 80)

# Endereço
if building.BuildingAddress:
    addr = building.BuildingAddress
    print(f"ENDEREÇO: {addr.AddressLines[0] if addr.AddressLines else 'N/A'}")
    print(f"LATITUDE: {addr.Country}")
    print(f"LONGITUDE: {addr.Region}")

# Contar tipos de elementos
print("\nTIPOS DE ELEMENTOS NO MODELO:")
element_types = defaultdict(int)
for element in ifc_file.by_type('IfcElement'):
    element_types[element.is_a()] += 1

for elem_type, count in sorted(element_types.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"  {elem_type:40} | {count:5} unidades")

# Salvar dados em JSON para uso posterior
dados_extraidos = {
    'projeto': project.Name,
    'edificacao': building.Name,
    'num_pavimentos': len(pavimentos),
    'pavimentos': pavimentos,
    'areas_por_pavimento': areas_por_pavimento,
    'area_total_m2': area_total,
    'data_extracao': '2026-03-09'
}

with open('projetos/arminio-tavares/dados_ifc.json', 'w', encoding='utf-8') as f:
    json.dump(dados_extraidos, f, indent=2, ensure_ascii=False)

print(f"\n✓ Dados salvos em: projetos/arminio-tavares/dados_ifc.json")
