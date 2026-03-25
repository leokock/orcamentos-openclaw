#!/usr/bin/env python3.11
"""
Extrai quantitativos arquitetônicos de arquivos IFC
"""
import sys
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.shape
from collections import defaultdict
from pathlib import Path

def get_element_properties(element):
    """Extrai todas as propriedades de um elemento"""
    props = {}
    
    # Propriedades nativas
    if hasattr(element, 'Name') and element.Name:
        props['Name'] = element.Name
    if hasattr(element, 'Description') and element.Description:
        props['Description'] = element.Description
    
    # Property Sets
    for definition in getattr(element, 'IsDefinedBy', []):
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a('IfcPropertySet'):
                for prop in property_set.HasProperties:
                    if prop.is_a('IfcPropertySingleValue'):
                        props[prop.Name] = prop.NominalValue.wrappedValue if prop.NominalValue else None
    
    # Quantidades
    for definition in getattr(element, 'IsDefinedBy', []):
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a('IfcElementQuantity'):
                for quantity in property_set.Quantities:
                    if quantity.is_a('IfcQuantityLength'):
                        props[f"Qty_{quantity.Name}"] = quantity.LengthValue
                    elif quantity.is_a('IfcQuantityArea'):
                        props[f"Qty_{quantity.Name}"] = quantity.AreaValue
                    elif quantity.is_a('IfcQuantityVolume'):
                        props[f"Qty_{quantity.Name}"] = quantity.VolumeValue
                    elif quantity.is_a('IfcQuantityCount'):
                        props[f"Qty_{quantity.Name}"] = quantity.CountValue
    
    return props

def extract_spaces(ifc_file):
    """Extrai espaços (ambientes) com áreas"""
    spaces = []
    
    for space in ifc_file.by_type('IfcSpace'):
        props = get_element_properties(space)
        
        # Pegar área e nome do espaço
        space_data = {
            'Name': props.get('Name', 'Sem nome'),
            'LongName': props.get('LongName', ''),
            'Description': props.get('Description', ''),
            'Type': 'Space',
        }
        
        # Buscar áreas nas quantidades
        for key, value in props.items():
            if 'area' in key.lower() or 'área' in key.lower():
                space_data['Area_m2'] = value
                break
        
        # Pegar pavimento
        for rel in getattr(space, 'Decomposes', []):
            if rel.is_a('IfcRelAggregates'):
                container = rel.RelatingObject
                if container.is_a('IfcBuildingStorey'):
                    space_data['Storey'] = container.Name
        
        spaces.append(space_data)
    
    return spaces

def extract_storeys(ifc_file):
    """Extrai pavimentos e suas áreas"""
    storeys = []
    
    for storey in ifc_file.by_type('IfcBuildingStorey'):
        props = get_element_properties(storey)
        
        storey_data = {
            'Name': props.get('Name', storey.Name),
            'Elevation': storey.Elevation if hasattr(storey, 'Elevation') else None,
        }
        
        # Calcular área total do pavimento somando espaços
        total_area = 0
        spaces_count = 0
        for rel in getattr(storey, 'IsDecomposedBy', []):
            for element in rel.RelatedObjects:
                if element.is_a('IfcSpace'):
                    spaces_count += 1
                    space_props = get_element_properties(element)
                    for key, value in space_props.items():
                        if 'area' in key.lower() and isinstance(value, (int, float)):
                            total_area += value
                            break
        
        storey_data['Total_Area_m2'] = total_area
        storey_data['Spaces_Count'] = spaces_count
        
        storeys.append(storey_data)
    
    return sorted(storeys, key=lambda x: x['Elevation'] or 0)

def extract_coverings(ifc_file):
    """Extrai revestimentos (pisos, paredes, forros)"""
    coverings = []
    
    for covering in ifc_file.by_type('IfcCovering'):
        props = get_element_properties(covering)
        
        covering_data = {
            'Name': props.get('Name', 'Sem nome'),
            'Type': covering.PredefinedType if hasattr(covering, 'PredefinedType') else 'Unknown',
            'Description': props.get('Description', ''),
            'Material': '',
            'Area_m2': None,
        }
        
        # Buscar material
        if hasattr(covering, 'HasAssociations'):
            for assoc in covering.HasAssociations:
                if assoc.is_a('IfcRelAssociatesMaterial'):
                    mat = assoc.RelatingMaterial
                    if mat.is_a('IfcMaterial'):
                        covering_data['Material'] = mat.Name
                    elif mat.is_a('IfcMaterialLayerSetUsage'):
                        covering_data['Material'] = mat.ForLayerSet.LayerSetName if mat.ForLayerSet else ''
        
        # Buscar área
        for key, value in props.items():
            if 'area' in key.lower() or key.startswith('Qty_'):
                if isinstance(value, (int, float)):
                    covering_data['Area_m2'] = value
                    break
        
        # Pegar pavimento
        for rel in getattr(covering, 'ContainedInStructure', []):
            if rel.is_a('IfcRelContainedInSpatialStructure'):
                container = rel.RelatingStructure
                if container.is_a('IfcBuildingStorey'):
                    covering_data['Storey'] = container.Name
        
        coverings.append(covering_data)
    
    return coverings

def extract_doors_windows(ifc_file):
    """Extrai portas e janelas"""
    openings = []
    
    for element in ifc_file.by_type('IfcDoor') + ifc_file.by_type('IfcWindow'):
        props = get_element_properties(element)
        
        opening_data = {
            'Type': 'Door' if element.is_a('IfcDoor') else 'Window',
            'Name': props.get('Name', element.Name),
            'Description': props.get('Description', ''),
            'Width': None,
            'Height': None,
        }
        
        # Extrair dimensões
        for key, value in props.items():
            if 'width' in key.lower() or 'largura' in key.lower():
                opening_data['Width'] = value
            elif 'height' in key.lower() or 'altura' in key.lower():
                opening_data['Height'] = value
        
        # Pegar pavimento
        for rel in getattr(element, 'ContainedInStructure', []):
            if rel.is_a('IfcRelContainedInSpatialStructure'):
                container = rel.RelatingStructure
                if container.is_a('IfcBuildingStorey'):
                    opening_data['Storey'] = container.Name
        
        openings.append(opening_data)
    
    return openings

def extract_slabs(ifc_file):
    """Extrai lajes (pisos e forros estruturais)"""
    slabs = []
    
    for slab in ifc_file.by_type('IfcSlab'):
        props = get_element_properties(slab)
        
        slab_data = {
            'Name': props.get('Name', 'Sem nome'),
            'Type': slab.PredefinedType if hasattr(slab, 'PredefinedType') else 'Unknown',
            'Description': props.get('Description', ''),
            'Area_m2': None,
            'Volume_m3': None,
        }
        
        # Buscar quantidades
        for key, value in props.items():
            if 'area' in key.lower() and isinstance(value, (int, float)):
                slab_data['Area_m2'] = value
            elif 'volume' in key.lower() and isinstance(value, (int, float)):
                slab_data['Volume_m3'] = value
        
        # Pegar pavimento
        for rel in getattr(slab, 'ContainedInStructure', []):
            if rel.is_a('IfcRelContainedInSpatialStructure'):
                container = rel.RelatingStructure
                if container.is_a('IfcBuildingStorey'):
                    slab_data['Storey'] = container.Name
        
        slabs.append(slab_data)
    
    return slabs

def main(ifc_path):
    print(f"\n🏗️  Processando: {Path(ifc_path).name}")
    print("=" * 80)
    
    ifc_file = ifcopenshell.open(ifc_path)
    
    # Extrair dados
    storeys = extract_storeys(ifc_file)
    spaces = extract_spaces(ifc_file)
    coverings = extract_coverings(ifc_file)
    openings = extract_doors_windows(ifc_file)
    slabs = extract_slabs(ifc_file)
    
    # Exibir resumo
    print(f"\n📊 RESUMO:")
    print(f"  • Pavimentos: {len(storeys)}")
    print(f"  • Espaços/Ambientes: {len(spaces)}")
    print(f"  • Revestimentos: {len(coverings)}")
    print(f"  • Portas/Janelas: {len(openings)}")
    print(f"  • Lajes: {len(slabs)}")
    
    # Pavimentos
    print(f"\n🏢 PAVIMENTOS:")
    for storey in storeys:
        print(f"\n  {storey['Name']} (cota {storey['Elevation']:.2f}m)")
        print(f"    Área total: {storey['Total_Area_m2']:.2f} m²")
        print(f"    Espaços: {storey['Spaces_Count']}")
    
    # Espaços por pavimento
    print(f"\n🚪 ESPAÇOS POR PAVIMENTO:")
    spaces_by_storey = defaultdict(list)
    for space in spaces:
        storey = space.get('Storey', 'Sem pavimento')
        spaces_by_storey[storey].append(space)
    
    for storey, storey_spaces in sorted(spaces_by_storey.items()):
        print(f"\n  {storey}:")
        total = 0
        for space in storey_spaces:
            area = space.get('Area_m2', 0)
            total += area or 0
            print(f"    • {space['Name']}: {area:.2f} m²" if area else f"    • {space['Name']}: (sem área)")
        print(f"    TOTAL: {total:.2f} m²")
    
    # Revestimentos por tipo
    print(f"\n🎨 REVESTIMENTOS:")
    coverings_by_type = defaultdict(list)
    for covering in coverings:
        ctype = covering['Type']
        coverings_by_type[ctype].append(covering)
    
    for ctype, type_coverings in sorted(coverings_by_type.items()):
        print(f"\n  {ctype}:")
        total_area = 0
        for covering in type_coverings:
            area = covering.get('Area_m2')
            if area:
                total_area += area
                material = covering.get('Material', 'Sem material')
                print(f"    • {covering['Name']} ({material}): {area:.2f} m²")
        if total_area > 0:
            print(f"    TOTAL: {total_area:.2f} m²")
    
    # Esquadrias
    print(f"\n🪟 ESQUADRIAS:")
    openings_by_type = defaultdict(list)
    for opening in openings:
        otype = opening['Type']
        openings_by_type[otype].append(opening)
    
    for otype, type_openings in sorted(openings_by_type.items()):
        print(f"\n  {otype}s: {len(type_openings)} unidades")
        for opening in type_openings[:10]:  # Mostrar até 10
            w = opening.get('Width')
            h = opening.get('Height')
            dims = f"{w:.2f}x{h:.2f}m" if (w and h) else "(sem dimensões)"
            print(f"    • {opening['Name']} {dims}")
        if len(type_openings) > 10:
            print(f"    ... e mais {len(type_openings)-10}")
    
    # Lajes
    print(f"\n🏗️  LAJES:")
    slabs_by_storey = defaultdict(list)
    for slab in slabs:
        storey = slab.get('Storey', 'Sem pavimento')
        slabs_by_storey[storey].append(slab)
    
    for storey, storey_slabs in sorted(slabs_by_storey.items()):
        print(f"\n  {storey}:")
        for slab in storey_slabs:
            area = slab.get('Area_m2')
            vol = slab.get('Volume_m3')
            info = f"Área: {area:.2f} m²" if area else "Sem área"
            if vol:
                info += f" | Volume: {vol:.2f} m³"
            print(f"    • {slab['Name']} ({slab['Type']}): {info}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 extract_ifc_architecture.py <caminho_ifc>")
        sys.exit(1)
    
    main(sys.argv[1])
