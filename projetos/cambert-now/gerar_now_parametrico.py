#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - NOW RESIDENCE
Adaptado do script calibrado da Cartesian Engenharia
"""

import sys
import os

# Adiciona o path do script original
sys.path.insert(0, '/Users/leokock/clawd/orcamento-parametrico/scripts')

from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO NOW RESIDENCE
# ============================================================================

NOW_DADOS = {
    "Nome": "NOW Residence",
    "Código": "NOW-RES",
    "Cidade": "Itajaí/SC",
    "AC": 13054.00,  # Área construída coberta total
    "UR": 136,  # Unidades residenciais (sem ático)
    "UC": 2,  # Unidades comerciais (térreo)
    "NP": 24,  # Total de pavimentos
    "NPT": 17,  # Pavimentos tipo
    "NPG": 3,  # Pavimentos garagem
    "ELEV": 3,  # Elevadores
    "VAG": 110,  # Vagas de garagem
    "AT": 1160.00,  # Área terreno estimada
    "NS": 3,  # Número de subsolos
    "Prazo": 36,  # Prazo estimado em meses
    "CUB": 3150.00  # CUB SC mar/2026 (estimativa)
}

# ============================================================================
# BRIEFING DO NOW RESIDENCE
# ============================================================================

NOW_BRIEFING = {
    "Q1": "Estaca Franki",  # Tipo de Fundação (provável, 3 subsolos em centro urbano)
    "Q2": "Protendida",  # Tipo de Laje (mista protendida + armado)
    "Q3": "Cortina de estacas",  # Contenção (3 subsolos em terreno urbano centro)
    "Q4": "3+",  # Subsolos
    "Q5": "Alto",  # Padrão de Acabamento (piso madeira, porcelanato, lazer completo)
    "Q6": "Alumínio anodizado",  # Esquadria
    "Q7": "Porcelanato padrão",  # Piso
    "Q8": "Misto",  # Vedação (alvenaria + drywall)
    "Q9": "Gesso liso",  # Forro
    "Q10": "Misto",  # Fachada (tijolinho + ripado + peitoril)
    "Q11": "Empreitada",  # MO Fachada
    "Q12": "Completa",  # Cobertura Habitável (ático)
    "Q13": "Gás individual",  # Aquecimento
    "Q14": "Básico",  # Automação
    "Q15": "Sem",  # Energia (solar)
    "Q16": "Completo",  # Lazer (piscina + academia + salões + etc)
    "Q17": "Elaborado",  # Paisagismo
    "Q18": "Completo",  # Mobiliário
    "Q19": "36",  # Prazo
    "Q20": "Litoral SC",  # Região (Itajaí/SC)
    "Q21": "Sim",  # Gerador
    "Q22": "Não",  # Subestação
    "Q23": "Não",  # Fotovoltaicas
    "Q24": "Não",  # Carro Elétrico
    "Q25": "Sim"  # Pressurização
}

# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    output_path = "/Users/leokock/orcamentos/projetos/cambert-now/now-residence-parametrico.xlsx"
    calibration_stats_path = "/Users/leokock/clawd/orcamento-parametrico/calibration-stats.json"
    
    print("=" * 70)
    print("GERANDO ORÇAMENTO PARAMÉTRICO - NOW RESIDENCE")
    print("=" * 70)
    print()
    print(f"Projeto: {NOW_DADOS['Nome']}")
    print(f"Área Construída: {NOW_DADOS['AC']:,.2f} m²")
    print(f"Unidades: {NOW_DADOS['UR']} UR + {NOW_DADOS['UC']} UC")
    print(f"Padrão: {NOW_BRIEFING['Q5']}")
    print(f"CUB Base: R$ {NOW_DADOS['CUB']:,.2f}/m²")
    print()
    
    gerar_planilha(output_path, NOW_DADOS, NOW_BRIEFING, calibration_stats_path)
    
    print()
    print("=" * 70)
    print("CONCLUÍDO!")
    print("=" * 70)
    print(f"Arquivo salvo em:")
    print(f"  {output_path}")
    print()
