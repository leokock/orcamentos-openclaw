#!/usr/bin/env python3.11
"""
Extrai dados de um arquivo IFC para orçamento paramétrico
"""
import ifcopenshell
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
    for pav in pavimentos:
        nome = pav.Name or "Sem nome"
        elevacao = pav.Elevation or 0
        dados_pavimentos.append({
            'nome': nome,
            'elevacao': elevacao
        })
        print(f"  - {nome} (elevação: {elevacao:.2f}m)")
    
    # Extrair áreas de espaços (IfcSpace)
    espacos = ifc.by_type('IfcSpace')
    print(f"\n=== ESPAÇOS ({len(espacos)}) ===")
    
    areas_por_pavimento = defaultdict(float)
    area_total = 0.0
    
    for espaco in espacos:
        # Tentar extrair área
        area = 0.0
        for definition in espaco.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                if property_set.is_a('IfcPropertySet'):
                    for prop in property_set.HasProperties:
                        if prop.Name in ['Area', 'NetFloorArea', 'GrossFloorArea']:
                            if hasattr(prop, 'NominalValue'):
                                area = float(prop.NominalValue.wrappedValue)
                                break
        
        # Tentar calcular área por representação geométrica se não encontrou
        if area == 0.0 and hasattr(espaco, 'Representation') and espaco.Representation:
            # Para simplificar, vou tentar usar IfcQuantityArea se disponível
            for rel in espaco.IsDefinedBy:
                if rel.is_a('IfcRelDefinesByProperties'):
                    if rel.RelatingPropertyDefinition.is_a('IfcElementQuantity'):
                        for quantity in rel.RelatingPropertyDefinition.Quantities:
                            if quantity.is_a('IfcQuantityArea') and 'Area' in quantity.Name:
                                area = quantity.AreaValue
                                break
        
        # Encontrar pavimento do espaço
        pavimento_nome = "Sem pavimento"
        for rel in espaco.Decomposes:
            if rel.is_a('IfcRelAggregates'):
                relating = rel.RelatingObject
                if relating.is_a('IfcBuildingStorey'):
                    pavimento_nome = relating.Name or "Sem nome"
                    break
        
        if area > 0:
            areas_por_pavimento[pavimento_nome] += area
            area_total += area
    
    print(f"\n=== ÁREAS POR PAVIMENTO ===")
    for pav, area in sorted(areas_por_pavimento.items()):
        print(f"  {pav}: {area:.2f} m²")
    print(f"\nÁREA TOTAL: {area_total:.2f} m²")
    
    # Extrair unidades residenciais
    print(f"\n=== ANÁLISE DE UNIDADES ===")
    # Tentar identificar apartamentos
    apartamentos = [e for e in espacos if 'APT' in (e.Name or '').upper() or 'APTO' in (e.Name or '').upper()]
    print(f"Possíveis unidades identificadas: {len(apartamentos)}")
    
    # Retornar dados estruturados
    return {
        'nome_projeto': project.Name,
        'num_pavimentos': len(pavimentos),
        'pavimentos': dados_pavimentos,
        'area_total': area_total,
        'areas_por_pavimento': dict(areas_por_pavimento),
        'num_unidades_detectadas': len(apartamentos),
        'num_espacos': len(espacos)
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 extrair_dados_ifc.py <caminho_ifc>")
        sys.exit(1)
    
    caminho = sys.argv[1]
    dados = extrair_dados_ifc(caminho)
    
    print(f"\n{'='*50}")
    print(f"RESUMO PARA ORÇAMENTO PARAMÉTRICO")
    print(f"{'='*50}")
    print(f"Projeto: {dados['nome_projeto']}")
    print(f"Número de pavimentos: {dados['num_pavimentos']}")
    print(f"Área total: {dados['area_total']:.2f} m²")
    print(f"Unidades detectadas: {dados['num_unidades_detectadas']}")
