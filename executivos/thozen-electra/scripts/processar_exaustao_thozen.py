#!/usr/bin/env python3.11
"""
Processa DWG/DXF de exaustão do Thozen Electra.
Extrai: exaustores, dutos, coifas, grelhas, especificações elétricas.
"""

import ezdxf
from ezdxf import recover
import sys
from pathlib import Path
import json

def extrair_dados_exaustao(arquivo_dwg):
    """Extrai dados do sistema de exaustão."""
    print(f"\n{'='*70}")
    print(f"Processando: {arquivo_dwg}")
    print(f"{'='*70}\n")
    
    dados = {
        'arquivo': str(arquivo_dwg),
        'exaustores': [],
        'coifas': [],
        'dutos': {'horizontal': 0, 'vertical': 0, 'detalhes': []},
        'grelhas': [],
        'textos': [],
        'blocos': [],
        'especificacoes_eletricas': [],
        'observacoes': []
    }
    
    try:
        # Tentar abrir DWG (ezdxf suporta R2000+)
        print("🔄 Tentando abrir DWG com ezdxf.readfile()...")
        try:
            doc = ezdxf.readfile(arquivo_dwg)
            print("✅ Arquivo aberto com sucesso!")
        except Exception as e:
            print(f"⚠️ Falha na leitura normal: {e}")
            print("🔄 Tentando modo de recuperação...")
            doc, auditor = recover.readfile(arquivo_dwg)
            print(f"✅ Arquivo recuperado! Erros: {auditor.error_count}, Avisos: {auditor.warning_count}")
        
        msp = doc.modelspace()
        
        # Versão do DWG
        print(f"\n📄 Versão DWG: {doc.dxfversion}")
        print(f"📦 Total de entidades: {len(list(msp))}")
        
        # 1. TEXTOS — Buscar especificações técnicas
        print("\n" + "="*70)
        print("1. ANALISANDO TEXTOS (ESPECIFICAÇÕES)")
        print("="*70)
        
        textos_encontrados = []
        keywords = ['exaustor', 'coifa', 'duto', 'm³/h', 'cv', 'rpm', 'vazão', 
                    'motor', 'ventilador', 'churrascq', 'grelha', 'diâmetro', 
                    'ø', 'pressão', 'db', 'filtro', 'cabo', 'quadro', 'potência']
        
        for entidade in msp.query('TEXT MTEXT'):
            texto = entidade.dxf.text.lower() if hasattr(entidade.dxf, 'text') else ''
            
            # Filtrar textos relevantes
            if any(kw in texto for kw in keywords):
                info = {
                    'texto': entidade.dxf.text if hasattr(entidade.dxf, 'text') else '',
                    'camada': entidade.dxf.layer,
                    'tipo': entidade.dxftype()
                }
                textos_encontrados.append(info)
                dados['textos'].append(info)
                print(f"  📝 [{info['camada']}] {info['texto'][:100]}")
        
        print(f"\n✅ Total de textos relevantes: {len(textos_encontrados)}")
        
        # 2. BLOCOS — Buscar exaustores, coifas, grelhas
        print("\n" + "="*70)
        print("2. ANALISANDO BLOCOS (EQUIPAMENTOS)")
        print("="*70)
        
        blocos_encontrados = {}
        for entidade in msp.query('INSERT'):
            nome_bloco = entidade.dxf.name.lower()
            
            if nome_bloco not in blocos_encontrados:
                blocos_encontrados[nome_bloco] = 0
            blocos_encontrados[nome_bloco] += 1
            
            # Classificar blocos por tipo
            info = {
                'nome': entidade.dxf.name,
                'posicao': (entidade.dxf.insert.x, entidade.dxf.insert.y),
                'camada': entidade.dxf.layer,
                'rotacao': entidade.dxf.rotation if hasattr(entidade.dxf, 'rotation') else 0
            }
            
            # Tentar obter atributos do bloco
            if entidade.has_attrib:
                info['atributos'] = {}
                for attrib in entidade.attribs:
                    info['atributos'][attrib.dxf.tag] = attrib.dxf.text
            
            dados['blocos'].append(info)
            
            # Classificar
            if any(x in nome_bloco for x in ['exaust', 'ventilador', 'motor']):
                dados['exaustores'].append(info)
                print(f"  🌀 EXAUSTOR: {info['nome']} (camada: {info['camada']})")
                if 'atributos' in info:
                    for k, v in info['atributos'].items():
                        print(f"      └─ {k}: {v}")
            
            elif any(x in nome_bloco for x in ['coifa', 'captador', 'hood']):
                dados['coifas'].append(info)
                print(f"  🏠 COIFA: {info['nome']} (camada: {info['camada']})")
                if 'atributos' in info:
                    for k, v in info['atributos'].items():
                        print(f"      └─ {k}: {v}")
            
            elif any(x in nome_bloco for x in ['grelha', 'grade', 'veneziana']):
                dados['grelhas'].append(info)
                print(f"  🪟 GRELHA: {info['nome']} (camada: {info['camada']})")
        
        print(f"\n📊 Resumo de blocos:")
        for nome, qtd in sorted(blocos_encontrados.items(), key=lambda x: -x[1])[:20]:
            print(f"  • {nome}: {qtd}x")
        
        # 3. POLYLINES — Buscar dutos
        print("\n" + "="*70)
        print("3. ANALISANDO POLYLINES (DUTOS)")
        print("="*70)
        
        dutos_horizontal = 0
        dutos_vertical = 0
        
        for entidade in msp.query('LWPOLYLINE POLYLINE LINE'):
            camada = entidade.dxf.layer.lower()
            
            # Filtrar camadas de dutos (típico: "DUTO", "EXAUSTÃO", etc.)
            if any(x in camada for x in ['duto', 'exaust', 'ventilacao', 'ar']):
                # Calcular comprimento
                if entidade.dxftype() == 'LINE':
                    start = entidade.dxf.start
                    end = entidade.dxf.end
                    dx = end.x - start.x
                    dy = end.y - start.y
                    dz = end.z - start.z if hasattr(end, 'z') else 0
                    comprimento = (dx**2 + dy**2 + dz**2)**0.5
                    
                    # Classificar horizontal vs vertical (tolerância 10°)
                    angulo_vertical = abs(dz / (comprimento + 0.001))
                    
                    if angulo_vertical > 0.98:  # > 78° da horizontal = vertical
                        dutos_vertical += comprimento
                        tipo = 'vertical'
                    else:
                        dutos_horizontal += comprimento
                        tipo = 'horizontal'
                    
                    info = {
                        'tipo': tipo,
                        'comprimento': round(comprimento / 1000, 2),  # mm → m
                        'camada': entidade.dxf.layer,
                        'start': (round(start.x, 2), round(start.y, 2)),
                        'end': (round(end.x, 2), round(end.y, 2))
                    }
                    dados['dutos']['detalhes'].append(info)
                    
                    print(f"  🔧 Duto {tipo}: {info['comprimento']:.2f}m (camada: {info['camada']})")
                
                else:  # POLYLINE/LWPOLYLINE
                    # Aproximação: soma dos segmentos
                    try:
                        pontos = list(entidade.get_points())
                        comprimento_total = 0
                        for i in range(len(pontos) - 1):
                            p1 = pontos[i]
                            p2 = pontos[i+1]
                            dx = p2[0] - p1[0]
                            dy = p2[1] - p1[1]
                            dz = (p2[2] - p1[2]) if len(p2) > 2 and len(p1) > 2 else 0
                            comp = (dx**2 + dy**2 + dz**2)**0.5
                            comprimento_total += comp
                        
                        dutos_horizontal += comprimento_total  # Simplificação
                        
                        info = {
                            'tipo': 'polyline',
                            'comprimento': round(comprimento_total / 1000, 2),
                            'camada': entidade.dxf.layer,
                            'pontos': len(pontos)
                        }
                        dados['dutos']['detalhes'].append(info)
                        print(f"  🔧 Duto polyline: {info['comprimento']:.2f}m (camada: {info['camada']}, {info['pontos']} pontos)")
                    except Exception as e:
                        print(f"  ⚠️ Erro ao processar polyline: {e}")
        
        dados['dutos']['horizontal'] = round(dutos_horizontal / 1000, 2)  # mm → m
        dados['dutos']['vertical'] = round(dutos_vertical / 1000, 2)
        
        print(f"\n📏 Total de dutos:")
        print(f"  • Horizontal: {dados['dutos']['horizontal']:.2f} m")
        print(f"  • Vertical: {dados['dutos']['vertical']:.2f} m")
        print(f"  • TOTAL: {dados['dutos']['horizontal'] + dados['dutos']['vertical']:.2f} m")
        
        # 4. ESPECIFICAÇÕES ELÉTRICAS — Buscar em textos
        print("\n" + "="*70)
        print("4. ANALISANDO ESPECIFICAÇÕES ELÉTRICAS")
        print("="*70)
        
        keywords_eletrico = ['cv', 'kw', 'cabo', 'quadro', 'disjuntor', 'contator', 
                             'motor', 'ampere', 'volt', 'trifásico', '220v', '380v']
        
        for txt in dados['textos']:
            if any(kw in txt['texto'].lower() for kw in keywords_eletrico):
                dados['especificacoes_eletricas'].append(txt)
                print(f"  ⚡ {txt['texto'][:80]}")
        
        print(f"\n✅ Total de specs elétricas: {len(dados['especificacoes_eletricas'])}")
        
        # RESUMO FINAL
        print("\n" + "="*70)
        print("📊 RESUMO DA EXTRAÇÃO")
        print("="*70)
        print(f"  🌀 Exaustores identificados: {len(dados['exaustores'])}")
        print(f"  🏠 Coifas identificadas: {len(dados['coifas'])}")
        print(f"  🪟 Grelhas identificadas: {len(dados['grelhas'])}")
        print(f"  🔧 Metragem de dutos horizontal: {dados['dutos']['horizontal']:.2f} m")
        print(f"  🔧 Metragem de dutos vertical: {dados['dutos']['vertical']:.2f} m")
        print(f"  📝 Textos técnicos relevantes: {len(dados['textos'])}")
        print(f"  ⚡ Especificações elétricas: {len(dados['especificacoes_eletricas'])}")
        print("="*70)
        
        return dados
        
    except Exception as e:
        print(f"\n❌ ERRO ao processar arquivo: {e}")
        import traceback
        traceback.print_exc()
        dados['observacoes'].append(f"ERRO: {str(e)}")
        return dados


if __name__ == '__main__':
    dwg_path = Path('projetos/thozen-electra/projetos/13 CHURRASQUEIRA EXAUSTAO/DWG/RA_CHU_EXE_PROJETO_R00.dwg')
    
    if not dwg_path.exists():
        print(f"❌ Arquivo não encontrado: {dwg_path}")
        sys.exit(1)
    
    dados = extrair_dados_exaustao(dwg_path)
    
    # Salvar JSON
    output_json = Path('output/thozen-electra-exaustao-dados-r00.json')
    output_json.parent.mkdir(exist_ok=True)
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Dados salvos em: {output_json}")
