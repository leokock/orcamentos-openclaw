#!/usr/bin/env python3.11
"""
Extrai quantitativos de ar-condicionado de arquivo DWG
"""
import ezdxf
import sys
from collections import defaultdict
import re

def extrair_quantitativos_ac(dwg_path):
    """Extrai dados de ar-condicionado do DWG"""
    
    print(f"🔍 Processando: {dwg_path}\n")
    
    try:
        doc = ezdxf.readfile(dwg_path)
    except Exception as e:
        print(f"❌ Erro ao abrir DWG: {e}")
        return
    
    msp = doc.modelspace()
    
    # Estruturas para organizar dados
    equipamentos = []
    tubulacoes = []
    textos_encontrados = []
    blocos_encontrados = defaultdict(int)
    layers = set()
    
    print("=" * 80)
    print("📋 LAYERS DISPONÍVEIS")
    print("=" * 80)
    for layer in doc.layers:
        print(f"  - {layer.dxf.name}")
        layers.add(layer.dxf.name)
    
    print("\n" + "=" * 80)
    print("🔎 ENTIDADES NO MODELSPACE")
    print("=" * 80)
    
    # Contadores por tipo
    tipos = defaultdict(int)
    
    for entity in msp:
        tipos[entity.dxftype()] += 1
        
        # Extrair textos (podem conter especificações)
        if entity.dxftype() == 'TEXT':
            texto = entity.dxf.text.strip()
            layer = entity.dxf.layer
            if texto and len(texto) > 1:
                textos_encontrados.append({
                    'texto': texto,
                    'layer': layer,
                    'posicao': (entity.dxf.insert.x, entity.dxf.insert.y)
                })
        
        elif entity.dxftype() == 'MTEXT':
            texto = entity.text.strip()
            layer = entity.dxf.layer
            if texto and len(texto) > 1:
                textos_encontrados.append({
                    'texto': texto,
                    'layer': layer,
                    'posicao': (entity.dxf.insert.x, entity.dxf.insert.y)
                })
        
        # Extrair blocos (podem representar equipamentos)
        elif entity.dxftype() == 'INSERT':
            nome_bloco = entity.dxf.name
            layer = entity.dxf.layer
            blocos_encontrados[f"{nome_bloco} (layer: {layer})"] += 1
        
        # Extrair linhas/polylines (podem ser tubulações)
        elif entity.dxftype() in ['LINE', 'LWPOLYLINE', 'POLYLINE']:
            layer = entity.dxf.layer
            # Filtrar layers que podem conter tubulações de AC
            if any(kw in layer.upper() for kw in ['AC', 'COND', 'FRIG', 'AR', 'CLIMA', 'HVAC', 'TUB']):
                if entity.dxftype() == 'LINE':
                    comprimento = entity.dxf.start.distance(entity.dxf.end)
                    tubulacoes.append({
                        'layer': layer,
                        'comprimento_mm': comprimento,
                        'tipo': 'LINE'
                    })
                elif entity.dxftype() in ['LWPOLYLINE', 'POLYLINE']:
                    # Calcular comprimento total da polyline
                    try:
                        comp = 0
                        pontos = list(entity.get_points())
                        for i in range(len(pontos) - 1):
                            p1 = pontos[i]
                            p2 = pontos[i+1]
                            dx = p2[0] - p1[0]
                            dy = p2[1] - p1[1]
                            comp += (dx**2 + dy**2)**0.5
                        tubulacoes.append({
                            'layer': layer,
                            'comprimento_mm': comp,
                            'tipo': entity.dxftype()
                        })
                    except:
                        pass
    
    print("\n📊 Resumo de entidades:")
    for tipo, qtd in sorted(tipos.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tipo}: {qtd}")
    
    print("\n" + "=" * 80)
    print("🏷️  BLOCOS ENCONTRADOS (possíveis equipamentos)")
    print("=" * 80)
    for nome, qtd in sorted(blocos_encontrados.items(), key=lambda x: x[1], reverse=True):
        print(f"  {qtd}x {nome}")
    
    print("\n" + "=" * 80)
    print("📝 TEXTOS RELEVANTES (filtrados)")
    print("=" * 80)
    
    # Filtrar textos que podem ser relevantes para AC
    keywords = ['BTU', 'KW', 'TR', 'SPLIT', 'VRF', 'COND', 'EVAP', 'AC', 'AR', 
                'CLIMA', 'FRIG', 'DRENO', 'ELETRICA', 'CABO', 'POTENCIA', 
                'CAPACIDADE', 'PAVIMENTO', 'SALA', 'QUARTO', 'AMBIENTE']
    
    textos_relevantes = []
    for item in textos_encontrados:
        texto = item['texto'].upper()
        if any(kw in texto for kw in keywords) or any(c.isdigit() for c in texto):
            textos_relevantes.append(item)
    
    # Agrupar por layer
    textos_por_layer = defaultdict(list)
    for item in textos_relevantes[:200]:  # Limitar para não poluir
        textos_por_layer[item['layer']].append(item['texto'])
    
    for layer in sorted(textos_por_layer.keys()):
        print(f"\n  Layer: {layer}")
        for texto in textos_por_layer[layer][:20]:  # Máx 20 por layer
            print(f"    - {texto}")
    
    print("\n" + "=" * 80)
    print("🔧 TUBULAÇÕES (layers relacionados a AC)")
    print("=" * 80)
    
    if tubulacoes:
        # Agrupar por layer
        tub_por_layer = defaultdict(list)
        for tub in tubulacoes:
            tub_por_layer[tub['layer']].append(tub['comprimento_mm'])
        
        for layer, comprimentos in sorted(tub_por_layer.items()):
            total_mm = sum(comprimentos)
            total_m = total_mm / 1000
            print(f"  Layer: {layer}")
            print(f"    Segmentos: {len(comprimentos)}")
            print(f"    Total: {total_m:.2f} m")
    else:
        print("  ⚠️  Nenhuma tubulação identificada nos layers esperados")
    
    print("\n" + "=" * 80)
    print("✅ EXTRAÇÃO CONCLUÍDA")
    print("=" * 80)
    
    # Tentar identificar equipamentos a partir de textos
    print("\n" + "=" * 80)
    print("🔍 ANÁLISE DE EQUIPAMENTOS (baseado em textos)")
    print("=" * 80)
    
    equipamentos_identificados = []
    for item in textos_encontrados:
        texto = item['texto'].upper()
        # Padrões comuns
        if 'BTU' in texto or 'TR' in texto or 'KW' in texto:
            equipamentos_identificados.append({
                'texto': item['texto'],
                'layer': item['layer'],
                'pos': item['posicao']
            })
    
    if equipamentos_identificados:
        print(f"\n  Encontrados {len(equipamentos_identificados)} possíveis equipamentos:")
        for eq in equipamentos_identificados[:30]:
            print(f"    - {eq['texto']} (layer: {eq['layer']})")
    else:
        print("  ⚠️  Nenhum equipamento identificado automaticamente")
        print("  💡 Verifique os textos acima manualmente")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 extrair_ar_condicionado_dwg.py <arquivo.dwg>")
        sys.exit(1)
    
    extrair_quantitativos_ac(sys.argv[1])
