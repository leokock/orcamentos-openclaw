#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - Arthen Arboris
Baseado no template dinâmico da Cartesian
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório scripts ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gerar_template_dinamico import gerar_planilha

# ========== DADOS DO PROJETO ==========
ROZZO_DADOS = {
    'nome_projeto': 'Arthen Arboris',
    'cliente': 'Arthen Engenharia e Construções Ltda',
    'endereco': 'Ruas 418 e 420 (Lotes 1031, 1032, 1033, 1034), Bairro Morretes, Itapema/SC',
    'cidade': 'Itapema',
    'estado': 'SC',
    'data_base': 'Abril/2026',
    
    # Dados extraídos do memorial descritivo
    'AC': 12472.98,  # m² - Área Total Construída
    'UR': 90,         # unidades residenciais
    'UC': 8,          # unidades comerciais
    'NP': 20,         # pavimentos totais (térreo + 3 subsol + tipo dif + 14 tipos + rooftop + cob)
    'NPT': 14,        # pavimentos tipo
    'NPD': 1,         # pavimento tipo diferenciado
    'ELEV': 2,        # elevadores
    'VAG': 99,        # vagas
    'AT': 1008.00,    # m² - Área do Terreno
    'NS': 3,          # subsolos (G1, G2, G3)
    'NPE': 4,         # pav. embasamento (térreo + 3 garagens)
    
    # CUB Abril/2026 (usar valor atual ou estimado)
    'cub_database': 3150.00,  # R$/m² CUB/SC Abril 2026 (estimativa)
}

# ========== BRIEFING (25 PERGUNTAS) ==========
ROZZO_BRIEFING = {
    # 🔴 ALTO IMPACTO
    'Q1_fundacao': 'Hélice contínua',  # Confirmado memorial
    'Q2_laje': 'Mista',                # Confirmado memorial
    'Q3_contencao': 'Não',             # Conservador - não confirmado
    'Q4_subsolos': 3,                  # Confirmado (G1, G2, G3)
    'Q5_padrao': 'Standard',           # Médio padrão (memorial)
    
    # 🟡 MÉDIO IMPACTO
    'Q6_esquadria': 'Pintura eletrostática',  # Confirmado memorial
    'Q7_piso': 'Porcelanato',          # Confirmado memorial
    'Q8_vedacao': 'Alvenaria',         # Confirmado memorial
    'Q9_forro': 'Gesso acartonado',    # Confirmado memorial
    'Q10_fachada': 'Textura + pintura', # Conservador
    'Q11_mo_fachada': 'Equipe própria', # Padrão
    
    # 🟢 BAIXO IMPACTO
    'Q12_cobertura_habitavel': 'Completa',  # Rooftop completo
    'Q13_aquecimento': 'Gás individual',    # Padrão SC
    'Q14_automacao': 'Básico',              # Padrão
    'Q15_energia': 'Sem',                   # Não mencionado
    'Q16_lazer': 'Completo',                # Rooftop + piscina + academia
    'Q17_paisagismo': 'Básico',             # Padrão
    'Q18_mobiliario': 'Básico',             # Padrão
    'Q19_prazo': 30,                        # meses - estimativa conservadora
    'Q20_regiao': 'Litoral SC',             # Itapema/SC
    
    # ⚡ INFRAESTRUTURA TÉCNICA
    'Q21_gerador': False,          # Não mencionado
    'Q22_subestacao': False,       # Não mencionado
    'Q23_fotovoltaica': False,     # Não mencionado
    'Q24_carro_eletrico': False,   # Não mencionado
    'Q25_pressurizacao': True,     # Provável (escada enclausurada mencionada)
}

# ========== GERAR PLANILHA ==========
if __name__ == '__main__':
    output_path = str(Path.home() / "orcamentos" / "parametricos" / "arthen-arboris" / "arthen-arboris-parametrico-v1.xlsx")
    
    print(f"🏗️  Gerando orçamento paramétrico: {ROZZO_DADOS['nome_projeto']}")
    print(f"📊 Dados principais:")
    print(f"   - AC: {ROZZO_DADOS['AC']:,.2f} m²")
    print(f"   - UR: {ROZZO_DADOS['UR']} unidades")
    print(f"   - Pavimentos: {ROZZO_DADOS['NP']} ({ROZZO_DADOS['NPT']} tipos)")
    print(f"   - Padrão: {ROZZO_BRIEFING['Q5_padrao']}")
    print(f"   - CUB: R$ {ROZZO_DADOS['cub_database']:,.2f}/m²")
    print()
    
    try:
        gerar_planilha(
            output_path=output_path,
            dados_projeto=ROZZO_DADOS,
            briefing_respostas=ROZZO_BRIEFING,
            calibration_stats_path=str(Path.home() / "orcamentos-openclaw" / "archive" / "v1-pre-fase19" / "raiz-mar-2026" / "calibration-stats.json")
        )
        print(f"✅ Planilha gerada: {output_path}")
    except Exception as e:
        print(f"❌ Erro ao gerar planilha: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
