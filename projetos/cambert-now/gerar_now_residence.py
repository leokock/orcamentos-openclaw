#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - NOW Residence
Cambert Empreendimentos / Itajaí-SC
"""

import sys
import os

# Adiciona o path do script gerador
sys.path.insert(0, os.path.expanduser('~/clawd/orcamento-parametrico/scripts'))

from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO NOW RESIDENCE
# ============================================================================

NOW_DADOS = {
    "Nome": "NOW Residence",
    "Código": "NOW-CAM",
    "Cidade": "Itajaí/SC",
    "AC": 13054.00,  # m² (área construída total)
    "UR": 136,  # Unidades residenciais
    "UC": 2,  # Unidades comerciais (2 salas térreo)
    "NP": 24,  # Total pavimentos (3 garagens + térreo + lazer + 17 tipos + ático + cobertura)
    "NPT": 17,  # Pavimentos tipo
    "NPG": 3,  # Pavimentos garagem
    "ELEV": 3,  # Elevadores (2 sociais + 1 emergência)
    "VAG": 110,  # Vagas
    "AT": 1500.00,  # m² (área terreno estimada — centro Itajaí)
    "NS": 3,  # Número de subsolos (3 garagens)
    "Prazo": 36,  # meses (estimativa padrão)
    "CUB": 3200.00  # CUB SC mar/2026 (estimativa — R$ 3.200/m²)
}

# ============================================================================
# BRIEFING NOW RESIDENCE (25 perguntas)
# ============================================================================

NOW_BRIEFING = {
    # Q1-Q10: Dados fornecidos no brief
    "Q1": "Estaca hélice contínua",  # Tipo Fundação (provável, 3 subsolos)
    "Q2": "Mista",  # Tipo Laje (armado + protendido confirmado memorial)
    "Q3": "Cortina de estacas",  # Contenção (3 subsolos, centro Itajaí)
    "Q4": "3+",  # Subsolos (3 garagens)
    "Q5": "Alto",  # Padrão (studios + 2 dorms com suíte, lazer completo, centro Itajaí)
    "Q6": "Alumínio anodizado",  # Esquadria (confirmado memorial)
    "Q7": "Porcelanato padrão",  # Piso (confirmado laminado no memorial, mas porcelanato é mais comum)
    "Q8": "Alvenaria",  # Vedação (alvenaria blocos cerâmicos + drywall)
    "Q9": "Gesso liso",  # Forro (padrão alto)
    "Q10": "Misto",  # Fachada (tijolinho + ripado + reboco/textura confirmado)
    
    # Q11-Q18: Defaults razoáveis para padrão alto
    "Q11": "Empreitada",  # MO Fachada (padrão mercado)
    "Q12": "Completa",  # Cobertura Habitável (provável, padrão alto)
    "Q13": "Gás individual",  # Aquecimento (padrão residencial vertical SC)
    "Q14": "Básico",  # Automação (CFTV + interfone, sem full automation)
    "Q15": "Sem",  # Energia solar (não mencionado no projeto)
    "Q16": "Completo",  # Lazer (confirmado: academia, piscina, salões, pet, crossfit, etc)
    "Q17": "Básico",  # Paisagismo (deck, espaço zen, área verde mencionados)
    "Q18": "Básico",  # Mobiliário (padrão alto, mas não decorado)
    
    # Q19-Q25: Dados técnicos
    "Q19": "36",  # Prazo (36 meses estimativa padrão)
    "Q20": "Litoral SC",  # Região (Itajaí/SC)
    "Q21": "Sim",  # Gerador (provável, padrão alto + 3 elevadores)
    "Q22": "Não",  # Subestação (não mencionado)
    "Q23": "Não",  # Fotovoltaicas (não mencionado)
    "Q24": "Não",  # Carro Elétrico (não mencionado)
    "Q25": "Sim",  # Pressurização (3 elevadores + 24 pavimentos, provável)
}

# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    output_dir = os.path.expanduser("~/orcamentos/projetos/cambert-now")
    output_path = os.path.join(output_dir, "NOW-Residence-Orcamento-Parametrico.xlsx")
    
    calibration_stats_path = os.path.expanduser(
        "~/clawd/orcamento-parametrico/calibration-stats.json"
    )
    
    print("=" * 80)
    print("GERAÇÃO DE ORÇAMENTO PARAMÉTRICO - NOW RESIDENCE")
    print("=" * 80)
    print()
    print(f"Projeto: {NOW_DADOS['Nome']}")
    print(f"Localização: {NOW_DADOS['Cidade']}")
    print(f"Área Construída: {NOW_DADOS['AC']:,.2f} m²")
    print(f"Unidades: {NOW_DADOS['UR']} apartamentos + {NOW_DADOS['UC']} comerciais")
    print(f"Pavimentos: {NOW_DADOS['NP']} ({NOW_DADOS['NPT']} tipo)")
    print(f"CUB Base: R$ {NOW_DADOS['CUB']:,.2f}/m²")
    print()
    print("Gerando planilha...")
    print()
    
    try:
        gerar_planilha(
            output_path=output_path,
            dados_projeto=NOW_DADOS,
            briefing_respostas=NOW_BRIEFING,
            calibration_stats_path=calibration_stats_path
        )
        
        print()
        print("=" * 80)
        print("✓ ORÇAMENTO PARAMÉTRICO GERADO COM SUCESSO!")
        print("=" * 80)
        print(f"Arquivo: {output_path}")
        print()
        print("PRÓXIMOS PASSOS:")
        print("1. Abrir a planilha no Excel/LibreOffice")
        print("2. Revisar aba PAINEL (KPIs principais)")
        print("3. Validar aba ALERTAS (verificar semáforos)")
        print("4. Ajustar briefing se necessário (aba BRIEFING)")
        print("5. Gerar relatório de memória (usar template)")
        print()
        
    except Exception as e:
        print()
        print("=" * 80)
        print("✗ ERRO AO GERAR PLANILHA")
        print("=" * 80)
        print(f"Erro: {e}")
        print()
        import traceback
        traceback.print_exc()
        sys.exit(1)
