#!/usr/bin/env python3.11
"""
Análise detalhada de textos do DXF de Exaustão
Foca em extrair especificações técnicas completas
"""

import ezdxf
import re
from pathlib import Path
from collections import defaultdict

def extrair_numero(texto, contexto=""):
    """Extrai números de um texto"""
    # Padrões comuns: 1.234,56 ou 1234.56
    padroes = [
        r'(\d{1,3}(?:\.\d{3})*(?:,\d+)?)',  # BR: 1.234,56
        r'(\d+(?:\.\d+)?)',  # US: 1234.56
    ]
    for padrao in padroes:
        match = re.search(padrao, texto)
        if match:
            numero_str = match.group(1).replace('.', '').replace(',', '.')
            try:
                return float(numero_str)
            except:
                pass
    return None

def analisar_textos_detalhado(dxf_path):
    """Análise detalhada de todos os textos do DXF"""
    
    print(f"🔧 Carregando DXF: {dxf_path}")
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    # Categorias de dados
    dados = {
        'exaustores': [],
        'vazoes': [],
        'potencias': [],
        'dutos_especificacoes': [],
        'dimensoes': [],
        'quantidades': [],
        'especificacoes_gerais': [],
        'todos_textos': []
    }
    
    print("\n📝 Extraindo e categorizando textos...\n")
    
    for text_entity in msp.query('TEXT MTEXT'):
        try:
            texto = text_entity.dxf.text if text_entity.dxftype() == 'TEXT' else text_entity.text
            texto_limpo = texto.strip()
            texto_upper = texto_limpo.upper()
            
            if not texto_limpo or len(texto_limpo) < 2:
                continue
            
            dados['todos_textos'].append(texto_limpo)
            
            # EXAUSTORES
            if any(kw in texto_upper for kw in ['EXAUSTOR', 'TCV', 'VENTILADOR', 'FAN']):
                dados['exaustores'].append(texto_limpo)
            
            # VAZÃO
            if any(kw in texto_upper for kw in ['M³/H', 'M3/H', 'CMH', 'VAZÃO', 'VAZAO']):
                numero = extrair_numero(texto_limpo)
                dados['vazoes'].append({
                    'texto': texto_limpo,
                    'valor': numero
                })
            
            # POTÊNCIA
            if any(kw in texto_upper for kw in ['KW', 'CV', 'HP', 'POTÊNCIA', 'POTENCIA']):
                numero = extrair_numero(texto_limpo)
                dados['potencias'].append({
                    'texto': texto_limpo,
                    'valor': numero
                })
            
            # DUTOS - especificações
            if 'DUTO' in texto_upper:
                dados['dutos_especificacoes'].append(texto_limpo)
            
            # DIMENSÕES (Ø, DN, largura x altura)
            if any(kw in texto_upper for kw in ['Ø', 'DN', 'MM', 'CM']):
                dados['dimensoes'].append(texto_limpo)
            
            # QUANTIDADES (UN, PÇ, QTD)
            if any(kw in texto_upper for kw in ['UN', 'PÇ', 'QTD', 'QUANTIDADE']):
                dados['quantidades'].append(texto_limpo)
            
        except Exception as e:
            continue
    
    # Análise de frequências
    print("="*70)
    print("📊 RESULTADOS DA ANÁLISE")
    print("="*70)
    
    print(f"\n🔧 EXAUSTORES ({len(dados['exaustores'])} menções):")
    for texto in sorted(set(dados['exaustores']))[:20]:
        print(f"   • {texto}")
    
    print(f"\n💨 VAZÕES ({len(dados['vazoes'])} menções):")
    vazoes_com_valor = [v for v in dados['vazoes'] if v['valor']]
    for v in sorted(vazoes_com_valor, key=lambda x: x['valor'] or 0, reverse=True)[:15]:
        print(f"   • {v['texto']} → {v['valor']:.0f} m³/h" if v['valor'] and v['valor'] > 100 else f"   • {v['texto']}")
    
    print(f"\n⚡ POTÊNCIAS ({len(dados['potencias'])} menções):")
    potencias_com_valor = [p for p in dados['potencias'] if p['valor']]
    for p in sorted(potencias_com_valor, key=lambda x: x['valor'] or 0, reverse=True)[:15]:
        if p['valor'] and p['valor'] > 0.1:
            print(f"   • {p['texto']} → {p['valor']:.2f} kW")
    
    print(f"\n📏 DUTOS - Especificações ({len(set(dados['dutos_especificacoes']))} únicas):")
    for texto in sorted(set(dados['dutos_especificacoes']))[:15]:
        print(f"   • {texto}")
    
    print(f"\n📐 DIMENSÕES ({len(set(dados['dimensoes']))} únicas):")
    for texto in sorted(set(dados['dimensoes']))[:20]:
        print(f"   • {texto}")
    
    print(f"\n🔢 QUANTIDADES ({len(set(dados['quantidades']))} únicas):")
    for texto in sorted(set(dados['quantidades']))[:15]:
        print(f"   • {texto}")
    
    # Buscar padrões específicos
    print(f"\n🔍 PADRÕES ESPECÍFICOS:")
    
    # Buscar tabela de equipamentos
    textos_numericos = []
    for t in dados['todos_textos']:
        if re.search(r'\d', t) and len(t) < 50:
            textos_numericos.append(t)
    
    # Agrupar textos similares
    freq_textos = defaultdict(int)
    for t in dados['todos_textos']:
        if len(t) < 100:  # Ignorar textos muito longos
            freq_textos[t] += 1
    
    print(f"\n   📋 Textos mais frequentes (possíveis tags/legendas):")
    for texto, freq in sorted(freq_textos.items(), key=lambda x: -x[1])[:15]:
        if freq > 1:
            print(f"      • {texto} (x{freq})")
    
    return dados

def buscar_tabela_equipamentos(dxf_path):
    """Busca tabela de equipamentos/legenda técnica"""
    
    print("\n\n" + "="*70)
    print("🔍 BUSCANDO TABELA DE EQUIPAMENTOS/LEGENDA")
    print("="*70 + "\n")
    
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    # Coletar textos com posição
    textos_com_pos = []
    for text_entity in msp.query('TEXT MTEXT'):
        try:
            texto = text_entity.dxf.text if text_entity.dxftype() == 'TEXT' else text_entity.text
            if text_entity.dxftype() == 'TEXT':
                x, y = text_entity.dxf.insert.x, text_entity.dxf.insert.y
            else:
                x, y = text_entity.dxf.insert.x, text_entity.dxf.insert.y
            
            textos_com_pos.append({
                'texto': texto.strip(),
                'x': x,
                'y': y
            })
        except:
            continue
    
    # Ordenar por posição Y (de cima pra baixo) e depois X (esquerda pra direita)
    textos_com_pos.sort(key=lambda t: (-t['y'], t['x']))
    
    # Buscar região com informações técnicas (onde aparecem palavras-chave)
    regioes_interesse = []
    for i, t in enumerate(textos_com_pos):
        texto_upper = t['texto'].upper()
        if any(kw in texto_upper for kw in ['TCV', 'EXAUSTOR', 'VAZÃO', 'POTÊNCIA', 'RPM', 'MOTOR']):
            # Pegar contexto (10 textos antes e 20 depois)
            contexto = textos_com_pos[max(0, i-10):min(len(textos_com_pos), i+20)]
            regioes_interesse.append({
                'indice': i,
                'contexto': contexto,
                'texto_chave': t['texto']
            })
    
    # Exibir regiões de interesse
    print(f"✅ Encontradas {len(regioes_interesse)} regiões com informações técnicas\n")
    
    for idx, regiao in enumerate(regioes_interesse[:3], 1):  # Limitar a 3 regiões
        print(f"--- REGIÃO {idx} (próximo a: '{regiao['texto_chave']}') ---\n")
        for t in regiao['contexto']:
            if t['texto']:
                print(f"   {t['texto']}")
        print()

if __name__ == "__main__":
    dxf_path = Path("projetos/thozen-electra/dxf-exaustao/RA_CHU_EXE_PROJETO_R00.dxf")
    
    if not dxf_path.exists():
        print(f"❌ Arquivo não encontrado: {dxf_path}")
        exit(1)
    
    dados = analisar_textos_detalhado(dxf_path)
    buscar_tabela_equipamentos(dxf_path)
    
    print("\n" + "="*70)
    print("✅ Análise concluída!")
    print("="*70)
