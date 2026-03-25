#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Análise de IFC Hidrossanitário - Arminio Tavares
Extrai dados quantitativos de instalações hidráulicas
"""

import ifcopenshell
import ifcopenshell.util.element
from collections import defaultdict
import json

def analisar_ifc_hidro(ifc_path):
    """Analisa IFC hidrossanitário e extrai quantidades"""
    
    print(f"Carregando IFC: {ifc_path}")
    ifc_file = ifcopenshell.open(ifc_path)
    
    # Estatísticas
    stats = {
        "info": {},
        "elementos": {},
        "tubulacoes": {},
        "conexoes": {},
        "equipamentos": {},
        "sistemas": defaultdict(int)
    }
    
    # Informações do projeto
    project = ifc_file.by_type("IfcProject")[0]
    stats["info"]["nome"] = project.Name if project.Name else "N/A"
    stats["info"]["descricao"] = project.Description if project.Description else "N/A"
    
    # Contar elementos por tipo
    tipos_elementos = [
        "IfcPipeSegment",          # Tubos
        "IfcPipeFitting",          # Conexões de tubos
        "IfcFlowTerminal",         # Terminais (torneiras, ralos, etc)
        "IfcSanitaryTerminal",     # Louças sanitárias
        "IfcValve",                # Válvulas
        "IfcPump",                 # Bombas
        "IfcTank",                 # Reservatórios
        "IfcWasteTerminal",        # Terminais de esgoto
        "IfcDistributionPort",     # Portas de distribuição
        "IfcFlowController",       # Controladores de fluxo
        "IfcFlowFitting",          # Acessórios de fluxo
        "IfcDistributionElement",  # Elementos de distribuição
        "IfcBuildingStorey"        # Pavimentos
    ]
    
    for tipo in tipos_elementos:
        try:
            elementos = ifc_file.by_type(tipo)
            if len(elementos) > 0:
                stats["elementos"][tipo] = len(elementos)
                print(f"  • {tipo}: {len(elementos)} elementos")
        except:
            pass
    
    # Analisar tubulações
    tubos = ifc_file.by_type("IfcPipeSegment")
    if tubos:
        comprimentos = []
        diametros = defaultdict(float)
        sistemas = defaultdict(int)
        
        for tubo in tubos:
            # Tentar extrair comprimento
            for definition in tubo.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name in ['Length', 'NominalLength']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    comprimentos.append(prop.NominalValue.wrappedValue)
                            elif prop.Name in ['Diameter', 'NominalDiameter']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    diam = prop.NominalValue.wrappedValue
                                    diametros[diam] += 1
            
            # Sistema (água fria, quente, esgoto, etc)
            if hasattr(tubo, 'ObjectType') and tubo.ObjectType:
                sistemas[tubo.ObjectType] += 1
        
        if comprimentos:
            stats["tubulacoes"]["comprimento_total_m"] = sum(comprimentos)
            stats["tubulacoes"]["qtd_segmentos"] = len(comprimentos)
        
        if diametros:
            stats["tubulacoes"]["diametros"] = dict(diametros)
        
        if sistemas:
            stats["sistemas"] = dict(sistemas)
    
    # Analisar conexões
    conexoes = ifc_file.by_type("IfcPipeFitting")
    if conexoes:
        tipos_conexao = defaultdict(int)
        
        for conexao in conexoes:
            if hasattr(conexao, 'ObjectType') and conexao.ObjectType:
                tipos_conexao[conexao.ObjectType] += 1
        
        stats["conexoes"]["total"] = len(conexoes)
        if tipos_conexao:
            stats["conexoes"]["tipos"] = dict(tipos_conexao)
    
    # Analisar terminais/louças
    louças = []
    try:
        louças.extend(ifc_file.by_type("IfcSanitaryTerminal"))
    except:
        pass
    
    try:
        louças.extend(ifc_file.by_type("IfcFlowTerminal"))
    except:
        pass
    
    if louças:
        tipos_loucas = defaultdict(int)
        
        for louça in louças:
            if hasattr(louça, 'ObjectType') and louça.ObjectType:
                tipos_loucas[louça.ObjectType] += 1
            elif hasattr(louça, 'Name') and louça.Name:
                tipos_loucas[louça.Name] += 1
        
        stats["equipamentos"]["louças_terminais"] = len(louças)
        if tipos_loucas:
            stats["equipamentos"]["tipos"] = dict(tipos_loucas)
    
    # Analisar reservatórios
    reservatorios = ifc_file.by_type("IfcTank")
    if reservatorios:
        volumes = []
        
        for res in reservatorios:
            for definition in res.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    if property_set.is_a('IfcPropertySet'):
                        for prop in property_set.HasProperties:
                            if prop.Name in ['Volume', 'NominalVolume', 'GrossVolume']:
                                if hasattr(prop, 'NominalValue') and prop.NominalValue:
                                    volumes.append(prop.NominalValue.wrappedValue)
        
        stats["equipamentos"]["reservatorios"] = len(reservatorios)
        if volumes:
            stats["equipamentos"]["volume_total_L"] = sum(volumes)
    
    # Analisar bombas
    bombas = ifc_file.by_type("IfcPump")
    if bombas:
        stats["equipamentos"]["bombas"] = len(bombas)
    
    return stats

if __name__ == "__main__":
    ifc_path = "/Users/leokock/orcamentos/projetos/arminio-tavares/ifc-hidro-temp.ifc"
    
    print("=" * 80)
    print("ANÁLISE DE IFC HIDROSSANITÁRIO - ARMINIO TAVARES")
    print("=" * 80)
    print()
    
    try:
        stats = analisar_ifc_hidro(ifc_path)
        
        print()
        print("=" * 80)
        print("RESUMO DA ANÁLISE")
        print("=" * 80)
        print()
        
        print("INFO DO PROJETO:")
        for k, v in stats["info"].items():
            print(f"  • {k}: {v}")
        print()
        
        if stats["elementos"]:
            print("ELEMENTOS ENCONTRADOS:")
            for tipo, qtd in stats["elementos"].items():
                print(f"  • {tipo.replace('Ifc', '')}: {qtd}")
            print()
        
        if stats["tubulacoes"]:
            print("TUBULAÇÕES:")
            for k, v in stats["tubulacoes"].items():
                if k == "diametros":
                    print(f"  • Diâmetros:")
                    for diam, qtd in sorted(v.items()):
                        print(f"    - {diam}mm: {qtd} segmentos")
                elif isinstance(v, float):
                    print(f"  • {k}: {v:.2f}")
                else:
                    print(f"  • {k}: {v}")
            print()
        
        if stats["sistemas"]:
            print("SISTEMAS:")
            for sistema, qtd in stats["sistemas"].items():
                print(f"  • {sistema}: {qtd} elementos")
            print()
        
        if stats["conexoes"]:
            print("CONEXÕES:")
            for k, v in stats["conexoes"].items():
                if k == "tipos":
                    print(f"  • Tipos de conexões:")
                    for tipo, qtd in sorted(v.items(), key=lambda x: x[1], reverse=True):
                        print(f"    - {tipo}: {qtd}")
                else:
                    print(f"  • {k}: {v}")
            print()
        
        if stats["equipamentos"]:
            print("EQUIPAMENTOS:")
            for k, v in stats["equipamentos"].items():
                if k == "tipos":
                    print(f"  • Tipos:")
                    for tipo, qtd in sorted(v.items(), key=lambda x: x[1], reverse=True)[:10]:
                        print(f"    - {tipo}: {qtd}")
                elif isinstance(v, (int, float)):
                    print(f"  • {k}: {v:.0f}")
                else:
                    print(f"  • {k}: {v}")
            print()
        
        # Salvar em JSON
        output_json = "/Users/leokock/orcamentos/projetos/arminio-tavares/analise-hidro.json"
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Análise salva em: {output_json}")
        
        # Verificar se é realmente hidro
        total_elementos = sum(stats["elementos"].values()) if stats["elementos"] else 0
        
        if total_elementos == 0:
            print()
            print("⚠️ ATENÇÃO: Nenhum elemento hidrossanitário encontrado no IFC!")
            print("   Este arquivo pode ser da estrutura ou outra disciplina.")
        
    except Exception as e:
        print(f"❌ Erro ao analisar IFC: {e}")
        import traceback
        traceback.print_exc()
