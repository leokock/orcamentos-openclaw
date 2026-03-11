#!/usr/bin/env python3.11
"""
Extrai dados de um arquivo IFC para orçamento paramétrico - v2
Tenta extrair áreas de lajes e outros elementos construtivos
"""
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.shape
import sys
from collections import defaultdict

def extrair_dados_ifc(caminho_ifc):
    """Extrai dados relevantes do IFC"""
    print(f"Abrindo arquivo IFC: {caminho_ifc}")
    ifc = ifcopenshell.open(caminho_ifc)
    
    # Informações básicas do projeto
    project = ifc.by_type('IfcProject')[0]
    print(f"\n=== PROJETO ===")
    print(f"Nome: {project.Name}")
    
    # Extrair pavimentos (IfcBuildingStorey)
    pavimentos = ifc.by_type('IfcBuildingStorey')
    print(f"\n=== PAVIMENTOS ({len(pavimentos)}) ===")
    
    dados_pavimentos = []
    for pav in sorted(pavimentos, key=lambda p: p.Elevation or 0):
        nome = pav.Name or "Sem nome"
        elevacao = pav.Elevation or 0
        dados_pavimentos.append({
            'nome': nome,
            'elevacao': elevacao / 100.0  # Converter de cm para m
        })
        print(f"  - {nome} (elevação: {elevacao/100.0:.2f}m)")
    
    # Tentar extrair áreas de lajes
    print(f"\n=== ANÁLISE DE LAJES ===")
    lajes = ifc.by_type('IfcSlab')
    print(f"Total de lajes: {len(lajes)}")
    
    areas_lajes_por_pav = defaultdict(list)
    
    for laje in lajes:
        # Encontrar pavimento da laje
        pavimento_nome = "Sem pavimento"
        for rel in laje.ContainedInStructure:
            if rel.is_a('IfcRelContainedInSpatialStructure'):
                relating = rel.RelatingStructure
                if relating.is_a('IfcBuildingStorey'):
                    pavimento_nome = relating.Name or "Sem nome"
                    break
        
        # Tentar extrair área da laje
        area = 0.0
        
        # Método 1: Procurar em quantidades
        for rel in laje.IsDefinedBy:
            if rel.is_a('IfcRelDefinesByProperties'):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a('IfcElementQuantity'):
                    for quantity in prop_def.Quantities:
                        if quantity.is_a('IfcQuantityArea'):
                            area = quantity.AreaValue
                            break
                elif prop_def.is_a('IfcPropertySet'):
                    for prop in prop_def.HasProperties:
                        if prop.Name in ['Area', 'NetArea', 'GrossArea']:
                            if hasattr(prop, 'NominalValue'):
                                area = float(prop.NominalValue.wrappedValue)
                                break
            if area > 0:
                break
        
        if area > 0:
            areas_lajes_por_pav[pavimento_nome].append(area)
    
    # Consolidar áreas por pavimento
    print(f"\n=== ÁREAS ESTIMADAS POR PAVIMENTO (baseado em lajes) ===")
    areas_por_pavimento = {}
    area_total_lajes = 0.0
    
    for pav, areas in sorted(areas_lajes_por_pav.items()):
        area_pav = sum(areas)
        areas_por_pavimento[pav] = area_pav
        area_total_lajes += area_pav
        print(f"  {pav}: {area_pav:.2f} m² ({len(areas)} lajes)")
    
    print(f"\nÁREA TOTAL (lajes): {area_total_lajes:.2f} m²")
    
    # Tentar contar paredes para estimar unidades
    print(f"\n=== ANÁLISE DE ELEMENTOS ===")
    paredes = ifc.by_type('IfcWall')
    print(f"Paredes: {len(paredes)}")
    
    portas = ifc.by_type('IfcDoor')
    print(f"Portas: {len(portas)}")
    
    janelas = ifc.by_type('IfcWindow')
    print(f"Janelas: {len(janelas)}")
    
    # Pavimentos tipo (excluindo subsolo, térreo, cobertura, barrilete, etc)
    pavimentos_tipo = [p for p in dados_pavimentos 
                       if 'º PAVIMENTO' in p['nome'] 
                       and not any(x in p['nome'].upper() for x in ['SUBSOLO', 'BARRILETE', 'COBERTURA', 'CASA', 'RESERV'])]
    
    num_pavimentos_tipo = len(pavimentos_tipo)
    
    # Retornar dados estruturados
    return {
        'nome_projeto': project.Name,
        'num_pavimentos_total': len(pavimentos),
        'num_pavimentos_tipo': num_pavimentos_tipo,
        'pavimentos': dados_pavimentos,
        'area_total_lajes': area_total_lajes,
        'areas_por_pavimento': areas_por_pavimento,
        'num_paredes': len(paredes),
        'num_portas': len(portas),
        'num_janelas': len(janelas)
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 extrair_dados_ifc_v2.py <caminho_ifc>")
        sys.exit(1)
    
    caminho = sys.argv[1]
    dados = extrair_dados_ifc(caminho)
    
    print(f"\n{'='*60}")
    print(f"RESUMO PARA ORÇAMENTO PARAMÉTRICO")
    print(f"{'='*60}")
    print(f"Projeto: {dados['nome_projeto']}")
    print(f"Total de pavimentos: {dados['num_pavimentos_total']}")
    print(f"Pavimentos tipo: {dados['num_pavimentos_tipo']}")
    print(f"Área total (lajes): {dados['area_total_lajes']:.2f} m²")
    print(f"Elementos: {dados['num_paredes']} paredes, {dados['num_portas']} portas, {dados['num_janelas']} janelas")
