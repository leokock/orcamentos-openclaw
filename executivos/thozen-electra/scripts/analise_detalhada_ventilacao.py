#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Análise detalhada de equipamentos de ventilação
Foca em identificar ventiladores, especificações, vazões
"""

import ezdxf
from pathlib import Path
from collections import defaultdict
import re

def buscar_layers_ventilacao(doc):
    """Lista todos os layers relacionados à ventilação"""
    layers_vent = []
    for layer in doc.layers:
        nome = layer.dxf.name.lower()
        if any(keyword in nome for keyword in ['vent', 'pressur', 'bit', 'eng', 'insufl', 'exaust']):
            layers_vent.append(layer.dxf.name)
    return layers_vent

def analisar_blocos_por_layer(doc, layers_alvo):
    """Analisa blocos em layers específicos"""
    blocos_por_layer = defaultdict(list)
    
    msp = doc.modelspace()
    for entity in msp.query('INSERT'):
        layer = entity.dxf.layer
        if layer in layers_alvo:
            atributos = {}
            if entity.has_attrib:
                for attrib in entity.attribs:
                    atributos[attrib.dxf.tag] = attrib.dxf.text
            
            blocos_por_layer[layer].append({
                'nome': entity.dxf.name,
                'posicao': (entity.dxf.insert.x, entity.dxf.insert.y),
                'atributos': atributos
            })
    
    return blocos_por_layer

def analisar_textos_por_layer(doc, layers_alvo):
    """Extrai textos em layers específicos"""
    textos_por_layer = defaultdict(list)
    
    msp = doc.modelspace()
    for entity in msp.query('TEXT MTEXT'):
        layer = entity.dxf.layer
        if layer in layers_alvo:
            texto = entity.dxf.text if entity.dxftype() == 'TEXT' else entity.text
            textos_por_layer[layer].append({
                'texto': texto,
                'posicao': (entity.dxf.insert.x, entity.dxf.insert.y) if entity.dxftype() == 'TEXT' else (entity.dxf.insert.x, entity.dxf.insert.y)
            })
    
    return textos_por_layer

def identificar_escadas(textos, blocos):
    """Identifica escadas pressurizadas pelo projeto"""
    escadas = []
    
    # Buscar blocos de escada
    for bloco in blocos:
        nome = bloco['nome'].lower()
        if 'escada' in nome or 'stair' in nome or 'esc-' in nome:
            escadas.append(bloco)
    
    # Buscar textos mencionando escada
    escadas_textos = []
    for texto_obj in textos:
        texto = texto_obj['texto'].lower()
        if 'escada' in texto:
            escadas_textos.append(texto_obj)
    
    return escadas, escadas_textos

def buscar_especificacoes_ventiladores(textos):
    """Busca especificações técnicas completas de ventiladores"""
    specs = []
    
    for texto_obj in textos:
        texto = texto_obj['texto']
        
        # Padrões de especificação
        # Vazão: m³/h, m3/h, CMH
        vazao_match = re.search(r'(\d+[\.,]?\d*)\s*(m[³3]/h|cmh)', texto, re.IGNORECASE)
        
        # Pressão: Pa, mmCA
        pressao_match = re.search(r'(\d+[\.,]?\d*)\s*(pa|mmca|pascal)', texto, re.IGNORECASE)
        
        # Potência: CV, HP, kW
        potencia_match = re.search(r'(\d+[\.,]?\d*)\s*(cv|hp|kw)', texto, re.IGNORECASE)
        
        # RPM
        rpm_match = re.search(r'(\d+)\s*rpm', texto, re.IGNORECASE)
        
        # Diâmetro de dutos
        diametro_match = re.search(r'[øØΦ]\s*(\d+)', texto)
        
        if any([vazao_match, pressao_match, potencia_match, rpm_match, diametro_match]):
            spec = {
                'texto_completo': texto,
                'vazao': vazao_match.groups() if vazao_match else None,
                'pressao': pressao_match.groups() if pressao_match else None,
                'potencia': potencia_match.groups() if potencia_match else None,
                'rpm': rpm_match.group(1) if rpm_match else None,
                'diametro': diametro_match.group(1) if diametro_match else None,
            }
            specs.append(spec)
    
    return specs

def main():
    dxf_path = Path('projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf')
    
    print("🔍 Análise Detalhada — Ventilação Mecânica Thozen Electra\n")
    print("=" * 80)
    
    doc = ezdxf.readfile(dxf_path)
    
    # 1. Identificar layers de ventilação
    print("\n1️⃣ LAYERS DE VENTILAÇÃO")
    print("-" * 80)
    layers_vent = buscar_layers_ventilacao(doc)
    print(f"Encontrados {len(layers_vent)} layers:\n")
    for layer in sorted(layers_vent):
        print(f"  • {layer}")
    
    # 2. Analisar blocos em layers de ventilação
    print("\n2️⃣ BLOCOS EM LAYERS DE VENTILAÇÃO")
    print("-" * 80)
    blocos_vent = analisar_blocos_por_layer(doc, layers_vent)
    
    for layer, blocos in sorted(blocos_vent.items(), key=lambda x: -len(x[1])):
        print(f"\n📍 Layer: {layer} ({len(blocos)} blocos)")
        
        # Agrupar por tipo
        tipos = defaultdict(int)
        for bloco in blocos:
            tipos[bloco['nome']] += 1
        
        for tipo, qtd in sorted(tipos.items(), key=lambda x: -x[1])[:10]:
            print(f"    • {tipo}: {qtd}x")
            
            # Mostrar atributos do primeiro bloco desse tipo
            exemplo = next(b for b in blocos if b['nome'] == tipo)
            if exemplo['atributos']:
                print(f"      Atributos: {exemplo['atributos']}")
    
    # 3. Analisar textos em layers de ventilação
    print("\n3️⃣ TEXTOS EM LAYERS DE VENTILAÇÃO")
    print("-" * 80)
    textos_vent = analisar_textos_por_layer(doc, layers_vent)
    
    for layer, textos in sorted(textos_vent.items(), key=lambda x: -len(x[1])):
        print(f"\n📍 Layer: {layer} ({len(textos)} textos)")
        
        # Mostrar primeiros 20 textos únicos
        textos_unicos = list(set(t['texto'] for t in textos))
        for texto in textos_unicos[:20]:
            print(f"    • {texto}")
    
    # 4. Buscar especificações técnicas
    print("\n4️⃣ ESPECIFICAÇÕES TÉCNICAS ENCONTRADAS")
    print("-" * 80)
    
    todos_textos = []
    for textos in textos_vent.values():
        todos_textos.extend(textos)
    
    specs = buscar_especificacoes_ventiladores(todos_textos)
    
    print(f"\nTotal de especificações: {len(specs)}\n")
    
    # Agrupar por tipo
    specs_vazao = [s for s in specs if s['vazao']]
    specs_pressao = [s for s in specs if s['pressao']]
    specs_potencia = [s for s in specs if s['potencia']]
    specs_rpm = [s for s in specs if s['rpm']]
    
    print(f"📊 Vazões encontradas: {len(specs_vazao)}")
    for spec in specs_vazao[:10]:
        print(f"  • {spec['vazao'][0]} {spec['vazao'][1]} — {spec['texto_completo'][:100]}")
    
    print(f"\n📊 Pressões encontradas: {len(specs_pressao)}")
    for spec in specs_pressao[:10]:
        print(f"  • {spec['pressao'][0]} {spec['pressao'][1]} — {spec['texto_completo'][:100]}")
    
    print(f"\n📊 Potências encontradas: {len(specs_potencia)}")
    for spec in specs_potencia[:10]:
        print(f"  • {spec['potencia'][0]} {spec['potencia'][1]} — {spec['texto_completo'][:100]}")
    
    print(f"\n📊 RPMs encontrados: {len(specs_rpm)}")
    for spec in specs_rpm[:10]:
        print(f"  • {spec['rpm']} RPM — {spec['texto_completo'][:100]}")
    
    # 5. Buscar escadas
    print("\n5️⃣ IDENTIFICAÇÃO DE ESCADAS PRESSURIZADAS")
    print("-" * 80)
    
    todos_blocos = []
    for blocos in blocos_vent.values():
        todos_blocos.extend(blocos)
    
    escadas_blocos, escadas_textos = identificar_escadas(todos_textos, todos_blocos)
    
    print(f"\n📐 Blocos de escada: {len(escadas_blocos)}")
    for bloco in escadas_blocos[:10]:
        print(f"  • {bloco['nome']} @ ({bloco['posicao'][0]:.2f}, {bloco['posicao'][1]:.2f})")
    
    print(f"\n📝 Textos mencionando escada: {len(escadas_textos)}")
    textos_escada_unicos = list(set(t['texto'] for t in escadas_textos))
    for texto in textos_escada_unicos[:20]:
        print(f"  • {texto}")
    
    # 6. Analisar metragem em layers de ventilação
    print("\n6️⃣ METRAGEM DE DUTOS (LAYERS DE VENTILAÇÃO)")
    print("-" * 80)
    
    msp = doc.modelspace()
    metragem_por_layer = defaultdict(float)
    
    for entity in msp.query('LWPOLYLINE'):
        if entity.dxf.layer in layers_vent:
            try:
                pontos = list(entity.get_points('xy'))
                comprimento = 0.0
                for i in range(len(pontos) - 1):
                    p1 = pontos[i]
                    p2 = pontos[i + 1]
                    comprimento += ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
                metragem_por_layer[entity.dxf.layer] += comprimento
            except:
                pass
    
    for entity in msp.query('LINE'):
        if entity.dxf.layer in layers_vent:
            try:
                start = entity.dxf.start
                end = entity.dxf.end
                comprimento = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5
                metragem_por_layer[entity.dxf.layer] += comprimento
            except:
                pass
    
    print("\nMetragem por layer:")
    for layer, metragem in sorted(metragem_por_layer.items(), key=lambda x: -x[1]):
        print(f"  • {layer}: {metragem:.2f} m")
    
    # Salvar relatório
    output_dir = Path('executivo/thozen-electra/analise-dxf')
    output_path = output_dir / 'analise-ventilacao-detalhada.txt'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("ANÁLISE DETALHADA — VENTILAÇÃO MECÂNICA THOZEN ELECTRA\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("1. LAYERS DE VENTILAÇÃO\n")
        f.write("-" * 80 + "\n")
        for layer in sorted(layers_vent):
            f.write(f"{layer}\n")
        
        f.write("\n2. BLOCOS POR LAYER\n")
        f.write("-" * 80 + "\n")
        for layer, blocos in sorted(blocos_vent.items()):
            f.write(f"\nLayer: {layer} ({len(blocos)} blocos)\n")
            tipos = defaultdict(int)
            for bloco in blocos:
                tipos[bloco['nome']] += 1
            for tipo, qtd in sorted(tipos.items(), key=lambda x: -x[1]):
                f.write(f"  {tipo}: {qtd}x\n")
        
        f.write("\n3. ESPECIFICAÇÕES TÉCNICAS\n")
        f.write("-" * 80 + "\n")
        for spec in specs:
            f.write(f"\nTexto: {spec['texto_completo']}\n")
            if spec['vazao']:
                f.write(f"  Vazão: {spec['vazao'][0]} {spec['vazao'][1]}\n")
            if spec['pressao']:
                f.write(f"  Pressão: {spec['pressao'][0]} {spec['pressao'][1]}\n")
            if spec['potencia']:
                f.write(f"  Potência: {spec['potencia'][0]} {spec['potencia'][1]}\n")
            if spec['rpm']:
                f.write(f"  RPM: {spec['rpm']}\n")
        
        f.write("\n4. METRAGEM DE DUTOS\n")
        f.write("-" * 80 + "\n")
        for layer, metragem in sorted(metragem_por_layer.items(), key=lambda x: -x[1]):
            f.write(f"{layer}: {metragem:.2f} m\n")
    
    print(f"\n✅ Relatório salvo em: {output_path}")
    print("\n✅ Análise concluída!")

if __name__ == '__main__':
    main()
