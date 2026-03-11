#!/usr/bin/env python3.11
"""
IFC Hidrossanitário Extractor - Extrai quantitativos de instalações hidrossanitárias de arquivos IFC.

Uso:
  python3.11 scripts/ifc_hidrossanitario.py <caminho_ifc>
"""
import sys
from pathlib import Path
from collections import defaultdict

try:
    import ifcopenshell
    import ifcopenshell.util.element
except ImportError:
    print("ERRO: ifcopenshell não instalado. Execute: pip3.11 install ifcopenshell", file=sys.stderr)
    sys.exit(1)


def extrair_hidrossanitario(caminho_ifc):
    """Extrai dados de instalações hidrossanitárias de um arquivo IFC."""
    
    if not Path(caminho_ifc).exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_ifc}")
    
    print(f"Analisando IFC: {caminho_ifc}\n")
    ifc = ifcopenshell.open(caminho_ifc)
    
    # Informações gerais
    project = ifc.by_type('IfcProject')[0] if ifc.by_type('IfcProject') else None
    schema = ifc.schema
    
    # Elementos hidrossanitários (compatível com IFC2X3 e IFC4)
    # IFC2X3 usa classes genéricas, IFC4+ tem classes específicas
    
    # Tentar IFC4 primeiro, fallback para IFC2X3
    try:
        pipe_segments = ifc.by_type('IfcPipeSegment')  # IFC4+
    except:
        pipe_segments = []
    
    try:
        pipe_fittings = ifc.by_type('IfcPipeFitting')  # IFC4+
    except:
        pipe_fittings = []
    
    # Classes genéricas (IFC2X3)
    flow_segments = ifc.by_type('IfcFlowSegment')  # Tubulações genéricas (IFC2X3)
    flow_fittings = ifc.by_type('IfcFlowFitting')  # Conexões genéricas (IFC2X3)
    flow_terminals = ifc.by_type('IfcFlowTerminal')  # Terminais
    
    # Elementos de distribuição (base genérica)
    dist_flow_elements = ifc.by_type('IfcDistributionFlowElement')
    
    # Equipamentos específicos (podem não existir em IFC2X3)
    try:
        sanitary_terminals = ifc.by_type('IfcSanitaryTerminal')
    except:
        sanitary_terminals = []
    
    try:
        valves = ifc.by_type('IfcValve')
    except:
        valves = []
    
    try:
        pumps = ifc.by_type('IfcPump')
    except:
        pumps = []
    
    try:
        tanks = ifc.by_type('IfcTank')
    except:
        tanks = []
    
    # Consolidar tubulações (IFC4 IfcPipeSegment + IFC2X3 IfcFlowSegment)
    all_pipe_segments = list(pipe_segments) + list(flow_segments)
    
    # Análise de tubulações por tipo/sistema
    tubulacoes_por_sistema = defaultdict(lambda: {'quantidade': 0, 'comprimento_total': 0.0})
    
    for pipe in all_pipe_segments:
        # Tentar identificar o sistema (água fria, esgoto, etc)
        sistema = "Não especificado"
        
        # Buscar propriedades
        for rel in pipe.IsDefinedBy:
            if rel.is_a('IfcRelDefinesByProperties'):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a('IfcPropertySet'):
                    for prop in prop_def.HasProperties:
                        if prop.Name in ['System', 'SystemType', 'PipeSystemType', 'Sistema']:
                            if hasattr(prop, 'NominalValue'):
                                sistema = str(prop.NominalValue.wrappedValue)
                        elif prop.Name in ['Length', 'Comprimento']:
                            if hasattr(prop, 'NominalValue'):
                                comprimento = float(prop.NominalValue.wrappedValue)
                                tubulacoes_por_sistema[sistema]['comprimento_total'] += comprimento
        
        # Buscar quantidades
        comprimento = 0.0
        for rel in pipe.IsDefinedBy:
            if rel.is_a('IfcRelDefinesByProperties'):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a('IfcElementQuantity'):
                    for quantity in prop_def.Quantities:
                        if quantity.is_a('IfcQuantityLength'):
                            comprimento = quantity.LengthValue
                            tubulacoes_por_sistema[sistema]['comprimento_total'] += comprimento
                            break
        
        tubulacoes_por_sistema[sistema]['quantidade'] += 1
    
    # Análise de equipamentos sanitários
    equipamentos = defaultdict(int)
    for terminal in sanitary_terminals:
        tipo = terminal.Name or terminal.ObjectType or "Não especificado"
        equipamentos[tipo] += 1
    
    # Análise de conexões (IFC4 + IFC2X3)
    all_fittings = list(pipe_fittings) + list(flow_fittings)
    conexoes_por_tipo = defaultdict(int)
    for fitting in all_fittings:
        tipo = fitting.Name or fitting.ObjectType or "Conexão genérica"
        conexoes_por_tipo[tipo] += 1
    
    # Pavimentos (para distribuição)
    pavimentos = ifc.by_type('IfcBuildingStorey')
    dados_pavimentos = []
    for pav in sorted(pavimentos, key=lambda p: p.Elevation if hasattr(p, 'Elevation') else 0):
        dados_pavimentos.append({
            'nome': pav.Name or "Sem nome",
            'elevacao': round(pav.Elevation, 2) if hasattr(pav, 'Elevation') else 0.0
        })
    
    resultado = {
        'nome_projeto': project.Name if project else "Sem nome",
        'schema': schema,
        'num_entidades': len(list(ifc)),
        'pavimentos': dados_pavimentos,
        'tubulacoes': {
            'total_segmentos': len(all_pipe_segments),
            'comprimento_total': sum(s['comprimento_total'] for s in tubulacoes_por_sistema.values()),
            'por_sistema': dict(tubulacoes_por_sistema)
        },
        'conexoes': {
            'total': len(all_fittings),
            'por_tipo': dict(conexoes_por_tipo)
        },
        'equipamentos': {
            'sanitarios': dict(equipamentos),
            'total_sanitarios': len(sanitary_terminals),
            'total_terminais': len(flow_terminals),
            'valvulas': len(valves),
            'bombas': len(pumps),
            'reservatorios': len(tanks)
        },
        'elementos_brutos': {
            'pipe_segments_ifc4': len(pipe_segments),
            'pipe_fittings_ifc4': len(pipe_fittings),
            'flow_segments_ifc2x3': len(flow_segments),
            'flow_fittings_ifc2x3': len(flow_fittings),
            'flow_terminals': len(flow_terminals),
            'sanitary_terminals': len(sanitary_terminals),
            'dist_flow_elements': len(dist_flow_elements),
            'valves': len(valves),
            'pumps': len(pumps),
            'tanks': len(tanks)
        }
    }
    
    return resultado


def imprimir_resumo(dados):
    """Imprime resumo formatado."""
    print(f"{'='*60}")
    print(f"EXTRAÇÃO DE DADOS HIDROSSANITÁRIOS - IFC")
    print(f"{'='*60}")
    print(f"Projeto: {dados['nome_projeto']}")
    print(f"Schema: {dados['schema']}")
    print(f"Entidades totais: {dados['num_entidades']:,}")
    print()
    
    print(f"PAVIMENTOS: {len(dados['pavimentos'])} níveis")
    for pav in dados['pavimentos']:
        print(f"  {pav['nome']} (elev: {pav['elevacao']:.2f}m)")
    print()
    
    print(f"TUBULAÇÕES:")
    print(f"  Segmentos totais: {dados['tubulacoes']['total_segmentos']}")
    print(f"  Comprimento total: {dados['tubulacoes']['comprimento_total']:.2f} m")
    if dados['tubulacoes']['por_sistema']:
        print(f"  Por sistema:")
        for sistema, info in dados['tubulacoes']['por_sistema'].items():
            print(f"    {sistema}: {info['quantidade']} segmentos, {info['comprimento_total']:.2f}m")
    print()
    
    print(f"CONEXÕES:")
    print(f"  Total: {dados['conexoes']['total']}")
    if dados['conexoes']['por_tipo']:
        print(f"  Por tipo:")
        for tipo, qtd in sorted(dados['conexoes']['por_tipo'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"    {tipo}: {qtd}")
    print()
    
    print(f"EQUIPAMENTOS:")
    print(f"  Sanitários: {dados['equipamentos']['total_sanitarios']}")
    if dados['equipamentos']['sanitarios']:
        for tipo, qtd in dados['equipamentos']['sanitarios'].items():
            print(f"    {tipo}: {qtd}")
    print(f"  Terminais (flow): {dados['equipamentos']['total_terminais']}")
    print(f"  Válvulas/Registros: {dados['equipamentos']['valvulas']}")
    print(f"  Bombas: {dados['equipamentos']['bombas']}")
    print(f"  Reservatórios: {dados['equipamentos']['reservatorios']}")
    print()
    
    print(f"ELEMENTOS BRUTOS (para debug):")
    for elem, qtd in dados['elementos_brutos'].items():
        print(f"  {elem}: {qtd}")
    print(f"{'='*60}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 scripts/ifc_hidrossanitario.py <caminho_ifc>")
        sys.exit(1)
    
    caminho_ifc = sys.argv[1]
    
    try:
        dados = extrair_hidrossanitario(caminho_ifc)
        imprimir_resumo(dados)
        
        # Salvar JSON
        import json
        json_path = Path(caminho_ifc).with_suffix('.hidrossanitario.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"\nDados salvos em: {json_path}")
        
    except Exception as e:
        print(f"ERRO: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
