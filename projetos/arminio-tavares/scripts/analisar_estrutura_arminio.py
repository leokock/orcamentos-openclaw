#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Análise de IFC Estrutural - Arminio Tavares
Extrai dados quantitativos da estrutura para calibrar orçamento paramétrico
"""

import ifcopenshell
import ifcopenshell.util.element
from collections import defaultdict
import json

def analisar_ifc_estrutural(ifc_path):
    """Analisa IFC estrutural e extrai quantidades"""
    
    print(f"Carregando IFC: {ifc_path}")
    ifc_file = ifcopenshell.open(ifc_path)
    
    # Estatísticas
    stats = {
        "info": {},
        "elementos": {},
        "volumes": {},
        "areas": {},
        "materiais": defaultdict(float),
        "pavimentos": {},
        "fundacao": {},
        "estrutura": {}
    }
    
    # Informações do projeto
    project = ifc_file.by_type("IfcProject")[0]
    stats["info"]["nome"] = project.Name if project.Name else "N/A"
    stats["info"]["descricao"] = project.Description if project.Description else "N/A"
    
    # Contar elementos por tipo
    tipos_elementos = [
        "IfcColumn",           # Pilares
        "IfcBeam",             # Vigas
        "IfcSlab",             # Lajes
        "IfcWall",             # Paredes estruturais
        "IfcFooting",          # Sapatas
        "IfcPile",             # Estacas
        "IfcReinforcingBar",   # Barras de armadura
        "IfcReinforcingMesh",  # Telas de armadura
        "IfcBuildingStorey"    # Pavimentos
    ]
    
    for tipo in tipos_elementos:
        elementos = ifc_file.by_type(tipo)
        stats["elementos"][tipo] = len(elementos)
        print(f"  • {tipo}: {len(elementos)} elementos")
    
    # Analisar pilares
    pilares = ifc_file.by_type("IfcColumn")
    if pilares:
        volumes_pilares = []
        for pilar in pilares:
            # Tentar extrair propriedades
            for definition in pilar.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name == 'Volume' or prop.Name == 'NetVolume':
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    volumes_pilares.append(prop.NominalValue.wrappedValue)
        
        if volumes_pilares:
            stats["volumes"]["pilares_m3"] = sum(volumes_pilares)
            stats["volumes"]["pilares_qtd"] = len(volumes_pilares)
    
    # Analisar vigas
    vigas = ifc_file.by_type("IfcBeam")
    if vigas:
        volumes_vigas = []
        for viga in vigas:
            for definition in viga.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name == 'Volume' or prop.Name == 'NetVolume':
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    volumes_vigas.append(prop.NominalValue.wrappedValue)
        
        if volumes_vigas:
            stats["volumes"]["vigas_m3"] = sum(volumes_vigas)
            stats["volumes"]["vigas_qtd"] = len(volumes_vigas)
    
    # Analisar lajes
    lajes = ifc_file.by_type("IfcSlab")
    if lajes:
        areas_lajes = []
        volumes_lajes = []
        tipos_laje = defaultdict(int)
        
        for laje in lajes:
            # Tipo de laje
            if hasattr(laje, 'ObjectType') and laje.ObjectType:
                tipos_laje[laje.ObjectType] += 1
            
            # Propriedades
            for definition in laje.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name in ['Area', 'NetArea', 'GrossArea']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    areas_lajes.append(prop.NominalValue.wrappedValue)
                            elif prop.Name in ['Volume', 'NetVolume']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    volumes_lajes.append(prop.NominalValue.wrappedValue)
        
        if areas_lajes:
            stats["areas"]["lajes_m2"] = sum(areas_lajes)
        if volumes_lajes:
            stats["volumes"]["lajes_m3"] = sum(volumes_lajes)
        stats["estrutura"]["tipos_laje"] = dict(tipos_laje)
    
    # Analisar fundação
    estacas = ifc_file.by_type("IfcPile")
    sapatas = ifc_file.by_type("IfcFooting")
    
    if estacas:
        stats["fundacao"]["tipo"] = "Estacas"
        stats["fundacao"]["qtd_estacas"] = len(estacas)
        
        # Tentar extrair volumes
        volumes_estacas = []
        for estaca in estacas:
            for definition in estaca.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name in ['Volume', 'NetVolume']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    volumes_estacas.append(prop.NominalValue.wrappedValue)
        
        if volumes_estacas:
            stats["fundacao"]["volume_m3"] = sum(volumes_estacas)
    
    elif sapatas:
        stats["fundacao"]["tipo"] = "Sapatas"
        stats["fundacao"]["qtd_sapatas"] = len(sapatas)
    
    # Analisar pavimentos
    pavimentos = ifc_file.by_type("IfcBuildingStorey")
    stats["pavimentos"]["total"] = len(pavimentos)
    stats["pavimentos"]["lista"] = []
    
    for pav in pavimentos:
        pav_info = {
            "nome": pav.Name if pav.Name else "N/A",
            "elevation": pav.Elevation if hasattr(pav, 'Elevation') else None
        }
        stats["pavimentos"]["lista"].append(pav_info)
    
    # Resumo de volumes totais
    if stats["volumes"]:
        total_concreto = 0
        for key, val in stats["volumes"].items():
            if key.endswith("_m3"):
                total_concreto += val
        stats["volumes"]["total_concreto_m3"] = round(total_concreto, 2)
    
    return stats

if __name__ == "__main__":
    ifc_path = "/Users/leokock/orcamentos/projetos/arminio-tavares/PLA_ARM_EST_AP_IFC_REV08.ifc"
    
    print("=" * 80)
    print("ANÁLISE DE IFC ESTRUTURAL - ARMINIO TAVARES")
    print("=" * 80)
    print()
    
    try:
        stats = analisar_ifc_estrutural(ifc_path)
        
        print()
        print("=" * 80)
        print("RESUMO DA ANÁLISE")
        print("=" * 80)
        print()
        
        print("INFO DO PROJETO:")
        for k, v in stats["info"].items():
            print(f"  • {k}: {v}")
        print()
        
        print("ELEMENTOS ESTRUTURAIS:")
        for tipo, qtd in stats["elementos"].items():
            if qtd > 0:
                print(f"  • {tipo.replace('Ifc', '')}: {qtd}")
        print()
        
        if stats["fundacao"]:
            print("FUNDAÇÃO:")
            for k, v in stats["fundacao"].items():
                print(f"  • {k}: {v}")
            print()
        
        if stats["volumes"]:
            print("VOLUMES DE CONCRETO:")
            for k, v in stats["volumes"].items():
                if isinstance(v, float):
                    print(f"  • {k}: {v:.2f} m³")
                else:
                    print(f"  • {k}: {v}")
            print()
        
        if stats["areas"]:
            print("ÁREAS:")
            for k, v in stats["areas"].items():
                print(f"  • {k}: {v:.2f} m²")
            print()
        
        if stats["pavimentos"]:
            print(f"PAVIMENTOS: {stats['pavimentos']['total']}")
            print()
        
        # Salvar em JSON
        output_json = "/Users/leokock/orcamentos/projetos/arminio-tavares/analise-estrutura.json"
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Análise salva em: {output_json}")
        
    except Exception as e:
        print(f"❌ Erro ao analisar IFC: {e}")
        import traceback
        traceback.print_exc()
