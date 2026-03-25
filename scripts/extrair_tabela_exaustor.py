#!/usr/bin/env python3.11
"""
Extração da tabela técnica do exaustor TCV 710
"""

import ezdxf
import re
from pathlib import Path

def extrair_tabela_completa(dxf_path):
    """Extrai todos os dados da tabela de especificação do exaustor"""
    
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    # Coletar TODOS os textos com posição
    textos = []
    for text_entity in msp.query('TEXT MTEXT'):
        try:
            texto = text_entity.dxf.text if text_entity.dxftype() == 'TEXT' else text_entity.text
            texto = texto.strip()
            
            if not texto:
                continue
            
            if text_entity.dxftype() == 'TEXT':
                x, y = text_entity.dxf.insert.x, text_entity.dxf.insert.y
            else:
                x, y = text_entity.dxf.insert.x, text_entity.dxf.insert.y
            
            textos.append({
                'texto': texto,
                'x': round(x, 2),
                'y': round(y, 2)
            })
        except:
            continue
    
    # Ordenar por Y (de cima pra baixo) depois X (esquerda pra direita)
    textos.sort(key=lambda t: (-t['y'], t['x']))
    
    # Buscar início da tabela (onde está "ESPECIFICAÇÃO EXAUSTOR")
    indice_inicio = None
    for i, t in enumerate(textos):
        if 'ESPECIFICAÇÃO EXAUSTOR' in t['texto'].upper():
            indice_inicio = i
            break
    
    if not indice_inicio:
        print("❌ Tabela de especificação não encontrada")
        return
    
    print("="*80)
    print("📋 TABELA DE ESPECIFICAÇÃO DO EXAUSTOR - DADOS COMPLETOS")
    print("="*80 + "\n")
    
    # Extrair ~150 linhas após "ESPECIFICAÇÃO EXAUSTOR" (toda a tabela)
    tabela = textos[indice_inicio:indice_inicio+150]
    
    # Campos-chave que queremos capturar
    campos_interesse = [
        'VAZÃO', 'VAZAO', 'M³/H', 'M3/H',
        'PRESSÃO', 'PRESSAO', 'MMCA', 'PA',
        'POTÊNCIA', 'POTENCIA', 'KW', 'CV', 'HP',
        'ROTAÇÃO', 'ROTACAO', 'RPM',
        'RENDIMENTO',
        'NÍVEL', 'NIVEL', 'DB',
        'MOTOR',
        'VOLTAGEM', 'TENSÃO', 'TENSAO',
        'CORRENTE', 'AMPERES',
        'DIÂMETRO', 'DIAMETRO',
        'ROTOR', 'IMPELIDOR'
    ]
    
    dados_extraidos = {}
    buffer_contexto = []
    
    print("📊 EXTRAÇÃO LINHA POR LINHA:\n")
    
    for t in tabela:
        linha = t['texto']
        print(f"   {linha}")
        
        # Detectar campos relevantes
        linha_upper = linha.upper()
        for campo in campos_interesse:
            if campo in linha_upper:
                # Armazenar com contexto
                if campo not in dados_extraidos:
                    dados_extraidos[campo] = []
                dados_extraidos[campo].append(linha)
    
    # ==== RESUMO ESTRUTURADO ====
    print("\n\n" + "="*80)
    print("📝 RESUMO ESTRUTURADO - ESPECIFICAÇÕES TÉCNICAS")
    print("="*80 + "\n")
    
    # Reorganizar dados
    print("🔧 **EQUIPAMENTO:**")
    print("   • Modelo: TCV 710")
    print("   • Fabricante: BERLINER LUFT")
    print("   • Quantidade: 08 UN")
    print("   • Tipo: Exaustor centrífugo com pás voltadas para trás")
    print("   • Acionamento: COM INVERSOR DE FREQUÊNCIA (obrigatório)")
    
    print("\n💨 **VAZÃO:**")
    if 'VAZÃO' in dados_extraidos or 'VAZAO' in dados_extraidos or 'M³/H' in dados_extraidos:
        vazoes = dados_extraidos.get('VAZÃO', []) + dados_extraidos.get('VAZAO', []) + dados_extraidos.get('M³/H', [])
        for v in vazoes[:10]:
            print(f"   • {v}")
    
    print("\n📊 **PRESSÃO:**")
    if 'PRESSÃO' in dados_extraidos or 'PRESSAO' in dados_extraidos or 'MMCA' in dados_extraidos:
        pressoes = dados_extraidos.get('PRESSÃO', []) + dados_extraidos.get('PRESSAO', []) + dados_extraidos.get('MMCA', [])
        for p in pressoes[:10]:
            print(f"   • {p}")
    
    print("\n⚡ **POTÊNCIA:**")
    if 'POTÊNCIA' in dados_extraidos or 'POTENCIA' in dados_extraidos or 'KW' in dados_extraidos:
        potencias = dados_extraidos.get('POTÊNCIA', []) + dados_extraidos.get('POTENCIA', []) + dados_extraidos.get('KW', [])
        for p in potencias[:10]:
            print(f"   • {p}")
    
    print("\n🔄 **ROTAÇÃO:**")
    if 'ROTAÇÃO' in dados_extraidos or 'ROTACAO' in dados_extraidos or 'RPM' in dados_extraidos:
        rotacoes = dados_extraidos.get('ROTAÇÃO', []) + dados_extraidos.get('ROTACAO', []) + dados_extraidos.get('RPM', [])
        for r in rotacoes[:10]:
            print(f"   • {r}")
    
    print("\n⚙️ **MOTOR:**")
    if 'MOTOR' in dados_extraidos:
        for m in dados_extraidos['MOTOR'][:10]:
            print(f"   • {m}")
    
    print("\n🔊 **NÍVEL DE RUÍDO:**")
    if 'NÍVEL' in dados_extraidos or 'NIVEL' in dados_extraidos or 'DB' in dados_extraidos:
        ruidos = dados_extraidos.get('NÍVEL', []) + dados_extraidos.get('NIVEL', []) + dados_extraidos.get('DB', [])
        for r in ruidos[:10]:
            print(f"   • {r}")
    
    # Buscar dados numéricos específicos
    print("\n\n" + "="*80)
    print("🔢 DADOS NUMÉRICOS IDENTIFICADOS")
    print("="*80 + "\n")
    
    for t in tabela:
        linha = t['texto']
        # Buscar padrões numéricos
        if re.search(r'\d+[.,]\d+', linha) or (re.search(r'\d+', linha) and any(kw in linha.upper() for kw in ['KW', 'CV', 'M³/H', 'RPM', 'MMCA', 'DB', 'PA', '%'])):
            print(f"   • {linha}")
    
    return dados_extraidos

def buscar_dimensoes_churrasqueiras(dxf_path):
    """Busca dimensões e quantidades de churrasqueiras"""
    
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    print("\n\n" + "="*80)
    print("🍖 CHURRASQUEIRAS - DIMENSÕES E QUANTIDADES")
    print("="*80 + "\n")
    
    for text_entity in msp.query('TEXT MTEXT'):
        try:
            texto = text_entity.dxf.text if text_entity.dxftype() == 'TEXT' else text_entity.text
            texto_upper = texto.upper()
            
            if 'CHURRASQUEIRA' in texto_upper and ('ABERTURA' in texto_upper or 'QUANTIDADE' in texto_upper or 'CM' in texto_upper):
                print(f"   • {texto.strip()}")
        except:
            continue

if __name__ == "__main__":
    dxf_path = Path("projetos/thozen-electra/dxf-exaustao/RA_CHU_EXE_PROJETO_R00.dxf")
    
    if not dxf_path.exists():
        print(f"❌ Arquivo não encontrado")
        exit(1)
    
    extrair_tabela_completa(dxf_path)
    buscar_dimensoes_churrasqueiras(dxf_path)
