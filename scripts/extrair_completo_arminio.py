#!/usr/bin/env python3.11
"""
Extração completa de dados do IFC Arminio Tavares para orçamento paramétrico
"""

import ifcopenshell
import ifcopenshell.util.element
from collections import defaultdict
import json

# Abrir arquivo IFC
print("Abrindo arquivo IFC...")
ifc_file = ifcopenshell.open('projetos/arminio-tavares/PLA_ARM_ARQ_EP_R06.ifc')

# === 1. DADOS BÁSICOS ===
project = ifc_file.by_type('IfcProject')[0]
building = ifc_file.by_type('IfcBuilding')[0]
storeys = ifc_file.by_type('IfcBuildingStorey')

print("\n" + "="*80)
print(f"PROJETO: {project.Name}")
print("="*80)

# === 2. PROPERTY SETS ===
props = {}
for definition in building.IsDefinedBy or []:
    if definition.is_a('IfcRelDefinesByProperties'):
        prop_set = definition.RelatingPropertyDefinition
        if prop_set.is_a('IfcPropertySet'):
            for prop in prop_set.HasProperties:
                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                    props[prop.Name] = prop.NominalValue.wrappedValue

# === 3. PAVIMENTOS E ÁREAS ===
pavimentos = []
subsolos = []
tipos = []
tecnicos = []

for storey in sorted(storeys, key=lambda s: s.Elevation):
    nome = storey.Name
    elev = storey.Elevation / 1000  # mm para m
    
    pav_info = {
        'nome': nome,
        'elevacao': elev,
        'tipo': 'outros'
    }
    
    if 'SUBSOLO' in nome.upper() or 'SM' in nome.upper():
        pav_info['tipo'] = 'subsolo'
        subsolos.append(pav_info)
    elif any(x in nome.upper() for x in ['BARRILETE', 'MÁQUINA', 'RESERVAT', 'COBERTURA', 'CASA']):
        pav_info['tipo'] = 'tecnico'
        tecnicos.append(pav_info)
    elif 'PAVIMENTO' in nome.upper() and any(str(i) in nome for i in range(2, 20)):
        pav_info['tipo'] = 'tipo'
        tipos.append(pav_info)
    
    pavimentos.append(pav_info)

num_subsolos = len(subsolos)
num_pav_tipo = len(tipos)
num_pav_total = len(pavimentos)

print(f"\nPAVIMENTOS:")
print(f"  Total: {num_pav_total}")
print(f"  Subsolos: {num_subsolos}")
print(f"  Pavimentos Tipo: {num_pav_tipo}")
print(f"  Técnicos: {len(tecnicos)}")

# === 4. CONTAGEM DE UNIDADES (via portas de apartamento) ===
doors = ifc_file.by_type('IfcDoor')
unidades_estimadas = 0

# Contar portas em pavimentos tipo
for door in doors:
    storey = ifcopenshell.util.element.get_container(door)
    if storey:
        if any(storey.Name == p['nome'] for p in tipos):
            # Considerar portas de entrada de apartamento
            if door.Name and any(x in door.Name.upper() for x in ['AP', 'UNID', 'ENTRADA', 'P01', 'P1']):
                unidades_estimadas += 1

# Se não achou portas marcadas, estimar por área
if unidades_estimadas == 0:
    # Estimar 2 unidades por andar (padrão para terreno 486m²)
    unidades_estimadas = num_pav_tipo * 2

print(f"\nUNIDADES:")
print(f"  Estimadas: {unidades_estimadas} unidades")

# === 5. ELEVADORES ===
elevadores = 0
flow_terminals = ifc_file.by_type('IfcFlowTerminal')

# Procurar por elementos que possam ser elevadores
for elem in ifc_file.by_type('IfcBuildingElementProxy'):
    if elem.Name and 'ELEV' in elem.Name.upper():
        elevadores += 1

# Estimar se não achou: 1 elevador por torre para edifício até 16 pavimentos
if elevadores == 0:
    if num_pav_tipo <= 8:
        elevadores = 1
    elif num_pav_tipo <= 16:
        elevadores = 2
    else:
        elevadores = 3

print(f"\nELEVADORES:")
print(f"  Estimados: {elevadores} elevadores")

# === 6. VAGAS (estimativa via área de subsolo) ===
area_terreno = props.get('SM-Terreno Área', 486.4)
area_subsolo_total = area_terreno * num_subsolos  # Assumir TO 100% nos subsolos

# Estimativa: 12.5m² por vaga (vaga + circulação)
vagas_estimadas = int((area_subsolo_total * 0.7) / 12.5)  # 70% da área útil para vagas

print(f"\nVAGAS:")
print(f"  Área Subsolo: {area_subsolo_total:.2f} m²")
print(f"  Estimadas: {vagas_estimadas} vagas")

# === 7. ÁREAS ESTIMADAS ===
ca = props.get('SM-Coeficiente de Aproveitamento', 5.7)
area_construida = area_terreno * ca

to_torre = props.get('SM-T.O.Torre(%)', 0.364)
area_proj_torre = area_terreno * to_torre

# Perímetro estimado (assumir forma retangular otimizada)
import math
# Otimizar para retângulo áureo aproximado
largura_torre = math.sqrt(area_proj_torre / 1.5)
comprimento_torre = area_proj_torre / largura_torre
perimetro_torre = 2 * (largura_torre + comprimento_torre)

print(f"\nÁREAS:")
print(f"  Terreno: {area_terreno:.2f} m²")
print(f"  Construída Total: {area_construida:.2f} m²")
print(f"  Projeção Torre: {area_proj_torre:.2f} m²")
print(f"  Perímetro Torre (estimado): {perimetro_torre:.2f} m")
print(f"  Área Subsolo: {area_subsolo_total:.2f} m²")

# === 8. SALVAR DADOS ===
dados_parametrico = {
    # Identificação
    'nome_projeto': 'PLACON - ARMÍNIO TAVARES',
    'cliente': 'PLACON EMPREENDIMENTOS IMOBILIÁRIOS LTDA',
    'cidade': 'Florianópolis',
    'estado': 'SC',
    'regiao': 'Capital Floripa',
    
    # Dados do programa
    'AC': area_construida,
    'UR': unidades_estimadas,
    'NP': num_pav_total,
    'NPT': num_pav_tipo,
    'ELEV': elevadores,
    'VAG': vagas_estimadas,
    'AT': area_terreno,
    'APT': area_proj_torre,
    'PPT': perimetro_torre,
    'NS': num_subsolos,
    'AS': area_subsolo_total,
    
    # Property Sets extraídos
    'altura_pav_padrao': props.get('SM-Altura Pavimento Padrão Pref.', 3060) / 1000,
    'to_torre': to_torre,
    'ca': ca,
    'zoneamento': props.get('SM-Zoneamento', 'ARM-12.5'),
    
    # Pavimentos
    'pavimentos': pavimentos,
    'num_subsolos': num_subsolos,
    'num_pav_tipo': num_pav_tipo,
    'num_pav_total': num_pav_total
}

with open('projetos/arminio-tavares/dados_parametrico.json', 'w', encoding='utf-8') as f:
    json.dump(dados_parametrico, f, indent=2, ensure_ascii=False)

print(f"\n✓ Dados salvos em: projetos/arminio-tavares/dados_parametrico.json")

# === 9. RESUMO PARA ORÇAMENTO ===
print("\n" + "="*80)
print("RESUMO PARA ORÇAMENTO PARAMÉTRICO")
print("="*80)
print(f"Área Construída: {area_construida:,.0f} m²")
print(f"Unidades: {unidades_estimadas} un")
print(f"Pavimentos Tipo: {num_pav_tipo}")
print(f"Subsolos: {num_subsolos}")
print(f"Elevadores: {elevadores}")
print(f"Vagas: {vagas_estimadas}")
print(f"Área/Unidade: {area_construida/unidades_estimadas:.1f} m²")
print("="*80)
