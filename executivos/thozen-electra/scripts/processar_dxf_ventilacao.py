#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Processa DXF de Ventilação Mecânica (Thozen Electra)
Extrai quantitativos completos: ventiladores, dutos, grelhas, dampers, automação
"""

import ezdxf
import sys
from pathlib import Path
from collections import defaultdict
import re

def analisar_blocos(doc):
    """Identifica blocos (ventiladores, grelhas, dampers)"""
    blocos = defaultdict(int)
    blocos_detalhados = []
    
    msp = doc.modelspace()
    
    for entity in msp.query('INSERT'):
        nome_bloco = entity.dxf.name
        blocos[nome_bloco] += 1
        
        # Capturar atributos do bloco
        atributos = {}
        if entity.has_attrib:
            for attrib in entity.attribs:
                atributos[attrib.dxf.tag] = attrib.dxf.text
        
        blocos_detalhados.append({
            'nome': nome_bloco,
            'posicao': (entity.dxf.insert.x, entity.dxf.insert.y),
            'layer': entity.dxf.layer,
            'atributos': atributos
        })
    
    return blocos, blocos_detalhados

def analisar_textos(doc):
    """Extrai textos (especificações, legendas, memorial)"""
    textos = []
    
    msp = doc.modelspace()
    
    # TEXT e MTEXT
    for entity in msp.query('TEXT MTEXT'):
        texto = entity.dxf.text if entity.dxftype() == 'TEXT' else entity.text
        textos.append({
            'texto': texto,
            'layer': entity.dxf.layer,
            'posicao': (entity.dxf.insert.x, entity.dxf.insert.y) if entity.dxftype() == 'TEXT' else (entity.dxf.insert.x, entity.dxf.insert.y),
            'tipo': entity.dxftype()
        })
    
    return textos

def analisar_dutos(doc):
    """Calcula metragem de dutos (POLYLINEs)"""
    dutos = {
        'polylines': [],
        'linhas': [],
        'metragem_total': 0.0
    }
    
    msp = doc.modelspace()
    
    # LWPOLYLINEs
    for entity in msp.query('LWPOLYLINE'):
        comprimento = 0.0
        try:
            pontos = list(entity.get_points('xy'))
            
            # Calcular comprimento
            for i in range(len(pontos) - 1):
                p1 = pontos[i]
                p2 = pontos[i + 1]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                comprimento += (dx**2 + dy**2)**0.5
            
            dutos['polylines'].append({
                'layer': entity.dxf.layer,
                'comprimento': comprimento,
                'num_pontos': len(pontos)
            })
            dutos['metragem_total'] += comprimento
        except:
            pass
    
    # POLYLINEs antigas
    for entity in msp.query('POLYLINE'):
        comprimento = 0.0
        try:
            vertices = entity.vertices
            pontos = [(v.dxf.location.x, v.dxf.location.y) for v in vertices]
            
            # Calcular comprimento
            for i in range(len(pontos) - 1):
                p1 = pontos[i]
                p2 = pontos[i + 1]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                comprimento += (dx**2 + dy**2)**0.5
            
            dutos['polylines'].append({
                'layer': entity.dxf.layer,
                'comprimento': comprimento,
                'num_pontos': len(pontos)
            })
            dutos['metragem_total'] += comprimento
        except:
            pass
    
    # LINEs
    for entity in msp.query('LINE'):
        try:
            start = entity.dxf.start
            end = entity.dxf.end
            comprimento = ((end.x - start.x)**2 + (end.y - start.y)**2 + (end.z - start.z)**2)**0.5
            
            dutos['linhas'].append({
                'layer': entity.dxf.layer,
                'comprimento': comprimento
            })
            dutos['metragem_total'] += comprimento
        except:
            pass
    
    return dutos

def identificar_equipamentos(blocos_detalhados, textos):
    """Identifica ventiladores, dampers, sensores via blocos e textos"""
    equipamentos = {
        'ventiladores': [],
        'dampers_corta_fogo': [],
        'dampers_motorizados': [],
        'grelhas': [],
        'difusores': [],
        'sensores': [],
        'clp': [],
        'outros': []
    }
    
    # Palavras-chave para classificação
    keywords = {
        'ventiladores': ['vent', 'fan', 'exaustor', 'insufl'],
        'dampers_corta_fogo': ['damper', 'registro', 'corta-fogo', 'cf', 'fire'],
        'dampers_motorizados': ['motor', 'atuador', 'eletrico'],
        'grelhas': ['grelha', 'grill', 'grade'],
        'difusores': ['difusor', 'diffuser', 'saida'],
        'sensores': ['sensor', 'transmissor', 'medidor', 'pressao'],
        'clp': ['clp', 'plc', 'controlador', 'automacao']
    }
    
    # Classificar blocos
    for bloco in blocos_detalhados:
        nome = bloco['nome'].lower()
        classificado = False
        
        for categoria, palavras in keywords.items():
            if any(palavra in nome for palavra in palavras):
                equipamentos[categoria].append(bloco)
                classificado = True
                break
        
        if not classificado:
            equipamentos['outros'].append(bloco)
    
    return equipamentos

def extrair_especificacoes_tecnicas(textos):
    """Busca especificações técnicas (m³/h, Pa, CV, kW, etc.)"""
    specs = {
        'vazao': [],
        'pressao': [],
        'potencia': [],
        'diametro': [],
        'temperaturas': [],
        'outras': []
    }
    
    # Regex para valores numéricos com unidades
    patterns = {
        'vazao': r'(\d+[\.,]?\d*)\s*(m[³3]/h|m3/h|cmh)',
        'pressao': r'(\d+[\.,]?\d*)\s*(pa|pascal|mmca)',
        'potencia': r'(\d+[\.,]?\d*)\s*(cv|hp|kw|w)',
        'diametro': r'[øØΦ]?\s*(\d+)\s*(mm|cm|m|\"|\'\')',
        'temperaturas': r'(\d+[\.,]?\d*)\s*[°º]c'
    }
    
    for texto_obj in textos:
        texto = texto_obj['texto'].lower()
        
        for categoria, pattern in patterns.items():
            matches = re.findall(pattern, texto, re.IGNORECASE)
            if matches:
                specs[categoria].extend([
                    {
                        'valor': m[0],
                        'unidade': m[1] if len(m) > 1 else '',
                        'texto_completo': texto_obj['texto'],
                        'layer': texto_obj['layer']
                    }
                    for m in matches
                ])
    
    return specs

def main():
    dxf_path = Path('projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf')
    
    print(f"\n🔍 Processando DXF: {dxf_path.name}")
    print(f"📦 Tamanho: {dxf_path.stat().st_size / (1024*1024):.1f} MB\n")
    
    try:
        doc = ezdxf.readfile(dxf_path)
        print("✅ DXF carregado com sucesso")
        print(f"📐 Versão DXF: {doc.dxfversion}")
        print(f"📊 Layers: {len(doc.layers)}\n")
        
        # 1. Analisar blocos
        print("=" * 80)
        print("📦 BLOCOS (Equipamentos)")
        print("=" * 80)
        blocos, blocos_detalhados = analisar_blocos(doc)
        
        print(f"Total de blocos: {sum(blocos.values())}")
        print(f"Tipos únicos: {len(blocos)}\n")
        
        print("Top 20 blocos mais frequentes:")
        for nome, qtd in sorted(blocos.items(), key=lambda x: -x[1])[:20]:
            print(f"  • {nome}: {qtd}x")
        
        # 2. Analisar textos
        print("\n" + "=" * 80)
        print("📝 TEXTOS (Especificações)")
        print("=" * 80)
        textos = analisar_textos(doc)
        print(f"Total de textos: {len(textos)}\n")
        
        # 3. Extrair especificações técnicas
        print("🔧 Especificações técnicas encontradas:")
        specs = extrair_especificacoes_tecnicas(textos)
        
        for categoria, valores in specs.items():
            if valores:
                print(f"\n  {categoria.upper()}:")
                for spec in valores[:10]:  # Primeiros 10
                    print(f"    - {spec['valor']} {spec['unidade']} | Layer: {spec['layer']}")
                    print(f"      Texto: {spec['texto_completo'][:100]}")
                if len(valores) > 10:
                    print(f"    ... e mais {len(valores) - 10} ocorrências")
        
        # 4. Analisar dutos
        print("\n" + "=" * 80)
        print("🔩 DUTOS (Metragem)")
        print("=" * 80)
        dutos = analisar_dutos(doc)
        
        print(f"POLYLINEs: {len(dutos['polylines'])}")
        print(f"LINEs: {len(dutos['linhas'])}")
        print(f"Metragem total bruta: {dutos['metragem_total']:.2f} m")
        
        # Agrupar por layer
        metragem_por_layer = defaultdict(float)
        for polyline in dutos['polylines']:
            metragem_por_layer[polyline['layer']] += polyline['comprimento']
        for linha in dutos['linhas']:
            metragem_por_layer[linha['layer']] += linha['comprimento']
        
        print("\nMetragem por layer (top 15):")
        for layer, metragem in sorted(metragem_por_layer.items(), key=lambda x: -x[1])[:15]:
            print(f"  • {layer}: {metragem:.2f} m")
        
        # 5. Identificar equipamentos
        print("\n" + "=" * 80)
        print("⚙️ EQUIPAMENTOS CLASSIFICADOS")
        print("=" * 80)
        equipamentos = identificar_equipamentos(blocos_detalhados, textos)
        
        for categoria, itens in equipamentos.items():
            if itens:
                print(f"\n{categoria.upper().replace('_', ' ')}: {len(itens)}")
                # Mostrar detalhes dos primeiros 5
                for item in itens[:5]:
                    print(f"  • {item['nome']} | Layer: {item['layer']}")
                    if item['atributos']:
                        print(f"    Atributos: {item['atributos']}")
                if len(itens) > 5:
                    print(f"  ... e mais {len(itens) - 5} itens")
        
        # 6. Salvar relatório detalhado
        output_dir = Path('executivo/thozen-electra/analise-dxf')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        relatorio_path = output_dir / 'relatorio-extracao-completo.txt'
        
        with open(relatorio_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("RELATÓRIO DE EXTRAÇÃO DXF — VENTILAÇÃO MECÂNICA THOZEN ELECTRA\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("1. BLOCOS\n")
            f.write("-" * 80 + "\n")
            for nome, qtd in sorted(blocos.items(), key=lambda x: -x[1]):
                f.write(f"{nome}: {qtd}x\n")
            
            f.write("\n2. BLOCOS DETALHADOS (primeiros 100)\n")
            f.write("-" * 80 + "\n")
            for bloco in blocos_detalhados[:100]:
                f.write(f"\nBloco: {bloco['nome']}\n")
                f.write(f"  Posição: ({bloco['posicao'][0]:.2f}, {bloco['posicao'][1]:.2f})\n")
                f.write(f"  Layer: {bloco['layer']}\n")
                if bloco['atributos']:
                    f.write(f"  Atributos: {bloco['atributos']}\n")
            
            f.write("\n3. TEXTOS (primeiros 200)\n")
            f.write("-" * 80 + "\n")
            for texto in textos[:200]:
                f.write(f"\nLayer: {texto['layer']}\n")
                f.write(f"Texto: {texto['texto']}\n")
            
            f.write("\n4. ESPECIFICAÇÕES TÉCNICAS\n")
            f.write("-" * 80 + "\n")
            for categoria, valores in specs.items():
                if valores:
                    f.write(f"\n{categoria.upper()}:\n")
                    for spec in valores:
                        f.write(f"  {spec['valor']} {spec['unidade']} — {spec['texto_completo']}\n")
            
            f.write("\n5. DUTOS — METRAGEM POR LAYER\n")
            f.write("-" * 80 + "\n")
            for layer, metragem in sorted(metragem_por_layer.items(), key=lambda x: -x[1]):
                f.write(f"{layer}: {metragem:.2f} m\n")
            
            f.write("\n6. EQUIPAMENTOS CLASSIFICADOS\n")
            f.write("-" * 80 + "\n")
            for categoria, itens in equipamentos.items():
                f.write(f"\n{categoria.upper()}: {len(itens)}\n")
                for item in itens:
                    f.write(f"  • {item['nome']} | Layer: {item['layer']} | Pos: ({item['posicao'][0]:.2f}, {item['posicao'][1]:.2f})\n")
                    if item['atributos']:
                        f.write(f"    {item['atributos']}\n")
        
        print(f"\n✅ Relatório detalhado salvo em: {relatorio_path}")
        
        # 7. Resumo executivo
        print("\n" + "=" * 80)
        print("📊 RESUMO EXECUTIVO")
        print("=" * 80)
        print(f"Blocos totais: {sum(blocos.values())}")
        print(f"Textos: {len(textos)}")
        print(f"Metragem de dutos: {dutos['metragem_total']:.2f} m")
        print(f"Ventiladores identificados: {len(equipamentos['ventiladores'])}")
        print(f"Dampers corta-fogo: {len(equipamentos['dampers_corta_fogo'])}")
        print(f"Dampers motorizados: {len(equipamentos['dampers_motorizados'])}")
        print(f"Grelhas: {len(equipamentos['grelhas'])}")
        print(f"Sensores: {len(equipamentos['sensores'])}")
        
        # Retornar dados para análise posterior
        return {
            'blocos': blocos,
            'blocos_detalhados': blocos_detalhados,
            'textos': textos,
            'specs': specs,
            'dutos': dutos,
            'equipamentos': equipamentos,
            'metragem_por_layer': dict(metragem_por_layer)
        }
        
    except Exception as e:
        print(f"❌ Erro ao processar DXF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    dados = main()
    print("\n✅ Processamento concluído!")
