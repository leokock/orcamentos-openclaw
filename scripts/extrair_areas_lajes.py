#!/usr/bin/env python3.11
"""
Extração de áreas calculando a partir das lajes (IfcSlab)
"""

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.element
import ifcopenshell.util.shape
from collections import defaultdict

# Abrir arquivo IFC
print("Abrindo arquivo IFC...")
ifc_file = ifcopenshell.open('projetos/arminio-tavares/PLA_ARM_ARQ_EP_R06.ifc')

# Configurar geometria
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

# Pegar todos os slabs (lajes)
slabs = ifc_file.by_type('IfcSlab')
print(f"Encontradas {len(slabs)} lajes no modelo")

# Agrupar por pavimento
areas_por_pavimento = defaultdict(float)
slabs_por_pavimento = defaultdict(list)

for slab in slabs:
    try:
        # Pegar o pavimento da laje
        storey = ifcopenshell.util.element.get_container(slab)
        if storey and storey.is_a('IfcBuildingStorey'):
            storey_name = storey.Name
            
            # Tentar pegar área das propriedades
            area = 0.0
            for definition in slab.IsDefinedBy or []:
                if definition.is_a('IfcRelDefinesByProperties'):
                    prop_set = definition.RelatingPropertyDefinition
                    if prop_set.is_a('IfcElementQuantity'):
                        for quantity in prop_set.Quantities:
                            if quantity.is_a('IfcQuantityArea'):
                                if 'NetArea' in quantity.Name or 'GrossArea' in quantity.Name or 'Area' in quantity.Name:
                                    area = quantity.AreaValue
                                    break
            
            if area > 0:
                areas_por_pavimento[storey_name] += area
                slabs_por_pavimento[storey_name].append({
                    'nome': slab.Name or 'sem nome',
                    'area': area
                })
    except Exception as e:
        continue

# Mostrar resultados
print("\n" + "="*80)
print("ÁREAS POR PAVIMENTO (calculadas a partir das lajes)")
print("="*80)

storeys = ifc_file.by_type('IfcBuildingStorey')
area_total = 0.0

for storey in sorted(storeys, key=lambda s: s.Elevation):
    storey_name = storey.Name
    area = areas_por_pavimento.get(storey_name, 0.0)
    num_slabs = len(slabs_por_pavimento.get(storey_name, []))
    
    if area > 0:
        print(f"{storey_name:30} | {area:10.2f} m² | ({num_slabs} lajes)")
        area_total += area

print("="*80)
print(f"{'ÁREA TOTAL':30} | {area_total:10.2f} m²")
print("="*80)

# Se ainda não conseguiu áreas, tentar método alternativo via Property Sets
if area_total == 0:
    print("\n⚠️  Nenhuma área encontrada nas lajes.")
    print("Tentando extrair de Property Sets gerais...")
    
    # Tentar pegar áreas de outros elementos ou property sets do building
    building = ifc_file.by_type('IfcBuilding')[0]
    
    for definition in building.IsDefinedBy or []:
        if definition.is_a('IfcRelDefinesByProperties'):
            prop_set = definition.RelatingPropertyDefinition
            print(f"\nProperty Set: {prop_set.Name}")
            
            if prop_set.is_a('IfcPropertySet'):
                for prop in prop_set.HasProperties:
                    if hasattr(prop, 'NominalValue') and prop.NominalValue:
                        print(f"  {prop.Name}: {prop.NominalValue.wrappedValue}")

print("\n✓ Análise concluída")
