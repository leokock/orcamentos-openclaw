#!/usr/bin/env python3.11
"""
Processar DXF de Exaustão - Thozen Electra
Extrai quantitativos de exaustores, dutos, coifas e instalações elétricas.
"""

import ezdxf
import sys
from collections import defaultdict
from pathlib import Path

def extrair_quantitativos_exaustao(dxf_path):
    """
    Processa DXF e extrai:
    - Exaustores (blocos com vazão/potência)
    - Dutos (POLYLINEs e LINEs)
    - Coifas (blocos)
    - Grelhas (blocos)
    - Especificações (textos)
    """
    
    print(f"🔧 Carregando DXF: {dxf_path}")
    try:
        doc = ezdxf.readfile(dxf_path)
    except Exception as e:
        print(f"❌ Erro ao ler DXF: {e}")
        sys.exit(1)
    
    msp = doc.modelspace()
    
    # Estruturas para armazenar dados
    resultados = {
        'exaustores': [],
        'coifas': [],
        'dutos_horizontal': 0,
        'dutos_vertical': 0,
        'dutos_detalhes': [],
        'grelhas': [],
        'blocos_interesse': defaultdict(int),
        'textos_especificacoes': [],
        'textos_vazao': [],
        'textos_potencia': [],
        'instalacao_eletrica': [],
        'layers': set()
    }
    
    print("\n📊 Analisando entidades do DXF...\n")
    
    # ==== 1. PROCESSAR BLOCOS ====
    print("🔍 Processando BLOCOS (exaustores, coifas, grelhas)...")
    for insert in msp.query('INSERT'):
        nome_bloco = insert.dxf.name.upper()
        layer = insert.dxf.layer
        resultados['layers'].add(layer)
        
        # Identificar exaustores
        if any(kw in nome_bloco for kw in ['EXAUST', 'VENTIL', 'FAN', 'MOTOR']):
            resultados['blocos_interesse'][nome_bloco] += 1
            resultados['exaustores'].append({
                'nome': nome_bloco,
                'layer': layer,
                'posicao': (insert.dxf.insert.x, insert.dxf.insert.y)
            })
        
        # Identificar coifas
        elif any(kw in nome_bloco for kw in ['COIFA', 'HOOD', 'CAPT', 'CHURR']):
            resultados['blocos_interesse'][nome_bloco] += 1
            resultados['coifas'].append({
                'nome': nome_bloco,
                'layer': layer,
                'posicao': (insert.dxf.insert.x, insert.dxf.insert.y)
            })
        
        # Identificar grelhas
        elif any(kw in nome_bloco for kw in ['GRELHA', 'GRID', 'VENT', 'GRADE']):
            resultados['blocos_interesse'][nome_bloco] += 1
            resultados['grelhas'].append({
                'nome': nome_bloco,
                'layer': layer,
                'posicao': (insert.dxf.insert.x, insert.dxf.insert.y)
            })
    
    print(f"   → {len(resultados['exaustores'])} exaustores identificados")
    print(f"   → {len(resultados['coifas'])} coifas identificadas")
    print(f"   → {len(resultados['grelhas'])} grelhas identificadas")
    
    # ==== 2. PROCESSAR TEXTOS ====
    print("\n🔍 Processando TEXTOS (especificações, vazão, potência)...")
    for text_entity in msp.query('TEXT MTEXT'):
        try:
            texto = text_entity.dxf.text if text_entity.dxftype() == 'TEXT' else text_entity.text
            texto_upper = texto.upper()
            layer = text_entity.dxf.layer
            resultados['layers'].add(layer)
            
            # Vazão (m³/h)
            if 'M³/H' in texto_upper or 'M3/H' in texto_upper or 'CMH' in texto_upper:
                resultados['textos_vazao'].append({
                    'texto': texto,
                    'layer': layer,
                    'posicao': (text_entity.dxf.insert.x, text_entity.dxf.insert.y) if text_entity.dxftype() == 'TEXT' else (0, 0)
                })
            
            # Potência (CV, HP, kW)
            elif any(kw in texto_upper for kw in ['CV', 'HP', 'KW', 'POTÊNCIA', 'POTENCIA']):
                resultados['textos_potencia'].append({
                    'texto': texto,
                    'layer': layer
                })
            
            # Especificações gerais
            elif any(kw in texto_upper for kw in ['EXAUST', 'DUTO', 'CHAPA', 'GALV', 'INOX', 'Ø', 'DN']):
                resultados['textos_especificacoes'].append({
                    'texto': texto,
                    'layer': layer
                })
            
            # Instalação elétrica
            elif any(kw in texto_upper for kw in ['QUADRO', 'DISJUNTOR', 'CABO', 'MM²', 'AWG', 'CONTATOR']):
                resultados['instalacao_eletrica'].append({
                    'texto': texto,
                    'layer': layer
                })
        
        except Exception as e:
            continue
    
    print(f"   → {len(resultados['textos_vazao'])} textos com vazão")
    print(f"   → {len(resultados['textos_potencia'])} textos com potência")
    print(f"   → {len(resultados['textos_especificacoes'])} textos com especificações")
    print(f"   → {len(resultados['instalacao_eletrica'])} textos de instalação elétrica")
    
    # ==== 3. PROCESSAR DUTOS (POLYLINEs e LINEs) ====
    print("\n🔍 Processando DUTOS (POLYLINEs e LINEs)...")
    
    for polyline in msp.query('LWPOLYLINE POLYLINE'):
        layer = polyline.dxf.layer
        resultados['layers'].add(layer)
        
        # Filtrar layers relevantes (dutos)
        if any(kw in layer.upper() for kw in ['DUTO', 'DUCT', 'EXAUST', 'VENTIL']):
            comprimento = 0
            try:
                pontos = list(polyline.vertices())
                for i in range(len(pontos) - 1):
                    p1 = pontos[i]
                    p2 = pontos[i + 1]
                    dx = p2[0] - p1[0]
                    dy = p2[1] - p1[1]
                    dz = 0
                    if len(p1) > 2 and len(p2) > 2:
                        dz = p2[2] - p1[2]
                    comp_segmento = (dx**2 + dy**2 + dz**2)**0.5
                    comprimento += comp_segmento
                
                # Classificar horizontal vs vertical
                # Vertical: predominância de mudança em Z ou layer com 'PRUM', 'VERT'
                eh_vertical = 'PRUM' in layer.upper() or 'VERT' in layer.upper()
                
                if eh_vertical:
                    resultados['dutos_vertical'] += comprimento
                else:
                    resultados['dutos_horizontal'] += comprimento
                
                resultados['dutos_detalhes'].append({
                    'layer': layer,
                    'comprimento': comprimento,
                    'tipo': 'vertical' if eh_vertical else 'horizontal'
                })
            
            except Exception as e:
                continue
    
    # Processar LINEs também (linhas simples de duto)
    for line in msp.query('LINE'):
        layer = line.dxf.layer
        resultados['layers'].add(layer)
        
        if any(kw in layer.upper() for kw in ['DUTO', 'DUCT', 'EXAUST', 'VENTIL']):
            try:
                start = line.dxf.start
                end = line.dxf.end
                dx = end[0] - start[0]
                dy = end[1] - start[1]
                dz = end[2] - start[2]
                comprimento = (dx**2 + dy**2 + dz**2)**0.5
                
                eh_vertical = 'PRUM' in layer.upper() or 'VERT' in layer.upper() or abs(dz) > abs(dx) and abs(dz) > abs(dy)
                
                if eh_vertical:
                    resultados['dutos_vertical'] += comprimento
                else:
                    resultados['dutos_horizontal'] += comprimento
                
                resultados['dutos_detalhes'].append({
                    'layer': layer,
                    'comprimento': comprimento,
                    'tipo': 'vertical' if eh_vertical else 'horizontal'
                })
            
            except Exception as e:
                continue
    
    print(f"   → Duto horizontal: {resultados['dutos_horizontal']:.2f} m")
    print(f"   → Duto vertical: {resultados['dutos_vertical']:.2f} m")
    print(f"   → {len(resultados['dutos_detalhes'])} segmentos processados")
    
    # ==== 4. RESUMO DE LAYERS ====
    print(f"\n📂 {len(resultados['layers'])} layers identificados:")
    layers_relevantes = [l for l in resultados['layers'] if any(kw in l.upper() for kw in ['EXAUST', 'DUTO', 'VENT', 'CHURR'])]
    for layer in sorted(layers_relevantes)[:20]:  # Top 20
        print(f"   • {layer}")
    
    return resultados

def gerar_relatorio_markdown(resultados, output_path):
    """Gera relatório markdown com os dados extraídos"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Extração - DXF Exaustão Thozen Electra\n\n")
        f.write("**Fonte:** `projetos/thozen-electra/dxf-exaustao/RA_CHU_EXE_PROJETO_R00.dxf`\n")
        f.write("**Processado em:** 2026-03-20\n\n")
        f.write("---\n\n")
        
        # ==== EXAUSTORES ====
        f.write("## 1. Exaustores\n\n")
        if resultados['exaustores']:
            f.write(f"**Quantidade total:** {len(resultados['exaustores'])} UN\n\n")
            f.write("| # | Bloco | Layer | Posição (X, Y) |\n")
            f.write("|---|-------|-------|----------------|\n")
            for i, ex in enumerate(resultados['exaustores'], 1):
                f.write(f"| {i} | {ex['nome']} | {ex['layer']} | ({ex['posicao'][0]:.2f}, {ex['posicao'][1]:.2f}) |\n")
        else:
            f.write("⚠️ Nenhum exaustor identificado via blocos.\n")
        
        f.write("\n### Especificações de Vazão\n\n")
        if resultados['textos_vazao']:
            for t in resultados['textos_vazao'][:10]:  # Limitar a 10
                f.write(f"- **{t['texto']}** (layer: `{t['layer']}`)\n")
        else:
            f.write("⚠️ Nenhum texto com vazão encontrado.\n")
        
        f.write("\n### Especificações de Potência\n\n")
        if resultados['textos_potencia']:
            for t in resultados['textos_potencia'][:10]:
                f.write(f"- **{t['texto']}** (layer: `{t['layer']}`)\n")
        else:
            f.write("⚠️ Nenhum texto com potência encontrado.\n")
        
        # ==== COIFAS ====
        f.write("\n---\n\n## 2. Coifas\n\n")
        if resultados['coifas']:
            f.write(f"**Quantidade total:** {len(resultados['coifas'])} UN\n\n")
            f.write("| # | Bloco | Layer | Posição (X, Y) |\n")
            f.write("|---|-------|-------|----------------|\n")
            for i, c in enumerate(resultados['coifas'], 1):
                f.write(f"| {i} | {c['nome']} | {c['layer']} | ({c['posicao'][0]:.2f}, {c['posicao'][1]:.2f}) |\n")
        else:
            f.write("⚠️ Nenhuma coifa identificada via blocos.\n")
        
        # ==== DUTOS ====
        f.write("\n---\n\n## 3. Dutos\n\n")
        f.write(f"**Metragem horizontal:** {resultados['dutos_horizontal']:.2f} m\n\n")
        f.write(f"**Metragem vertical:** {resultados['dutos_vertical']:.2f} m\n\n")
        f.write(f"**Metragem total:** {resultados['dutos_horizontal'] + resultados['dutos_vertical']:.2f} m\n\n")
        
        if resultados['dutos_detalhes']:
            # Agrupar por layer
            dutos_por_layer = defaultdict(lambda: {'horizontal': 0, 'vertical': 0})
            for d in resultados['dutos_detalhes']:
                dutos_por_layer[d['layer']][d['tipo']] += d['comprimento']
            
            f.write("### Detalhamento por Layer\n\n")
            f.write("| Layer | Horizontal (m) | Vertical (m) | Total (m) |\n")
            f.write("|-------|----------------|--------------|------------|\n")
            for layer, dados in sorted(dutos_por_layer.items()):
                total = dados['horizontal'] + dados['vertical']
                f.write(f"| {layer} | {dados['horizontal']:.2f} | {dados['vertical']:.2f} | {total:.2f} |\n")
        else:
            f.write("⚠️ Nenhum duto identificado.\n")
        
        # ==== GRELHAS ====
        f.write("\n---\n\n## 4. Grelhas de Ventilação\n\n")
        if resultados['grelhas']:
            f.write(f"**Quantidade total:** {len(resultados['grelhas'])} UN\n\n")
            f.write("| # | Bloco | Layer | Posição (X, Y) |\n")
            f.write("|---|-------|-------|----------------|\n")
            for i, g in enumerate(resultados['grelhas'], 1):
                f.write(f"| {i} | {g['nome']} | {g['layer']} | ({g['posicao'][0]:.2f}, {g['posicao'][1]:.2f}) |\n")
        else:
            f.write("⚠️ Nenhuma grelha identificada via blocos.\n")
        
        # ==== INSTALAÇÃO ELÉTRICA ====
        f.write("\n---\n\n## 5. Instalação Elétrica Associada\n\n")
        if resultados['instalacao_eletrica']:
            for t in resultados['instalacao_eletrica'][:20]:
                f.write(f"- {t['texto']} (layer: `{t['layer']}`)\n")
        else:
            f.write("⚠️ Nenhuma especificação elétrica identificada.\n")
        
        # ==== ESPECIFICAÇÕES GERAIS ====
        f.write("\n---\n\n## 6. Especificações Técnicas Gerais\n\n")
        if resultados['textos_especificacoes']:
            f.write("Textos relevantes encontrados:\n\n")
            for t in resultados['textos_especificacoes'][:30]:
                f.write(f"- {t['texto']} (layer: `{t['layer']}`)\n")
        else:
            f.write("⚠️ Nenhuma especificação geral identificada.\n")
        
        # ==== RESUMO BLOCOS ====
        f.write("\n---\n\n## 7. Resumo de Blocos Identificados\n\n")
        if resultados['blocos_interesse']:
            f.write("| Bloco | Quantidade |\n")
            f.write("|-------|------------|\n")
            for nome, qtd in sorted(resultados['blocos_interesse'].items(), key=lambda x: -x[1]):
                f.write(f"| {nome} | {qtd} |\n")
        
        # ==== LAYERS ====
        f.write("\n---\n\n## 8. Layers Relevantes\n\n")
        layers_relevantes = [l for l in resultados['layers'] if any(kw in l.upper() for kw in ['EXAUST', 'DUTO', 'VENT', 'CHURR'])]
        for layer in sorted(layers_relevantes):
            f.write(f"- {layer}\n")
        
        f.write("\n---\n\n*Relatório gerado automaticamente por `scripts/processar_dxf_exaustao.py`*\n")
    
    print(f"\n✅ Relatório salvo em: {output_path}")

if __name__ == "__main__":
    dxf_path = Path("projetos/thozen-electra/dxf-exaustao/RA_CHU_EXE_PROJETO_R00.dxf")
    output_path = Path("projetos/thozen-electra/dxf-exaustao/relatorio-extracao.md")
    
    if not dxf_path.exists():
        print(f"❌ Arquivo não encontrado: {dxf_path}")
        sys.exit(1)
    
    resultados = extrair_quantitativos_exaustao(dxf_path)
    gerar_relatorio_markdown(resultados, output_path)
    
    print("\n" + "="*60)
    print("📊 RESUMO GERAL")
    print("="*60)
    print(f"Exaustores: {len(resultados['exaustores'])} UN")
    print(f"Coifas: {len(resultados['coifas'])} UN")
    print(f"Grelhas: {len(resultados['grelhas'])} UN")
    print(f"Dutos horizontal: {resultados['dutos_horizontal']:.2f} m")
    print(f"Dutos vertical: {resultados['dutos_vertical']:.2f} m")
    print(f"Dutos TOTAL: {resultados['dutos_horizontal'] + resultados['dutos_vertical']:.2f} m")
    print("="*60)
