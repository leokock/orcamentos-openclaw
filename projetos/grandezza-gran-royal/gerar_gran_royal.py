#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - Gran Royal Residence (Grandezza)
Balneário Piçarras/SC
"""

import sys
import os

# Adicionar path do script original
sys.path.insert(0, os.path.expanduser("~/clawd/orcamento-parametrico/scripts"))
from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO - GRAN ROYAL RESIDENCE
# ============================================================================

GRAN_ROYAL_DADOS = {
    "Nome": "Grandezza — Gran Royal Residence",
    "Código": "GRAN-ROYAL",
    "Cidade": "Balneário Piçarras/SC",
    "AC": 5225.33,
    "UR": 30,
    "UC": 0,         # Unidades comerciais
    "NP": 19,
    "NPT": 14,       # 6º ao 19º pavimento
    "NPG": 2,        # Garagens (subsolo + térreo)
    "ELEV": 2,
    "VAG": 31,
    "AT": 499.80,
    "NS": 1,          # 1 subsolo
    "Prazo": 30,      # Estimado 30 meses
    "CUB": 3019.26    # CUB SC fev/2026 (R8-N)
}

# ============================================================================
# BRIEFING - 25 PERGUNTAS RESPONDIDAS
# ============================================================================

GRAN_ROYAL_BRIEFING = {
    "Q1": "Hélice Contínua",        # CONFIRMADO - SPT indica impenetrável ~39,6m
    "Q2": "Maciça",                  # CONFIRMADO - Projeto estrutural fck 25 MPa
    "Q3": "Cortina de estacas",      # CONFIRMADO - Parede diafragma 40cm (mais próximo: cortina)
    "Q4": "1",                       # CONFIRMADO - 1 subsolo
    "Q5": "Alto",                    # CONFIRMADO - 3Q ~95m², porcelanato, litoral, lazer completo
    "Q6": "Alumínio anodizado",      # ESTIMADO - Padrão para alto padrão litoral SC
    "Q7": "Porcelanato padrão",      # CONFIRMADO - Identificado nas plantas de arquitetura
    "Q8": "Alvenaria",               # CONFIRMADO - Sistema misto concreto armado + alvenaria
    "Q9": "Gesso liso",              # ESTIMADO - Padrão alto padrão
    "Q10": "Misto",                  # ESTIMADO - Projeto de fachada existe (SKP+DWG), provável misto
    "Q11": "Empreitada",             # ESTIMADO - 19 pavimentos, padrão de mercado
    "Q12": "Básica",                 # CONFIRMADO - Cobertura com reservatório, não habitável completa
    "Q13": "Gás individual",         # CONFIRMADO - GLP central 6×P-190 (760kg)
    "Q14": "Básico",                 # ESTIMADO - Pasta automação vazia, mas alto padrão sugere básico
    "Q15": "Sem",                    # ESTIMADO - Não identificado nos projetos
    "Q16": "Completo",               # CONFIRMADO - Piscina, academia, gourmet, kids, pet, playground
    "Q17": "Básico",                 # ESTIMADO - Não detalhado nos projetos
    "Q18": "Básico",                 # ESTIMADO - Padrão para áreas comuns
    "Q19": "30",                     # ESTIMADO - 19 pavimentos, porte médio
    "Q20": "Litoral SC",             # CONFIRMADO - Balneário Piçarras
    "Q21": "Não",                    # ESTIMADO - Não identificado no projeto elétrico
    "Q22": "Não",                    # ESTIMADO - Não identificado
    "Q23": "Não",                    # ESTIMADO - Não identificado
    "Q24": "Não",                    # ESTIMADO - Não identificado
    "Q25": "Sim"                     # CONFIRMADO - Ventilação mecânica no PPCI (pressurização)
}

# ============================================================================
# GERAR PLANILHA
# ============================================================================

if __name__ == "__main__":
    output_dir = os.path.expanduser("~/orcamentos/projetos/grandezza-gran-royal/analise")
    os.makedirs(output_dir, exist_ok=True)
    
    calibration_stats_path = os.path.expanduser(
        "~/clawd/orcamento-parametrico/calibration-stats.json"
    )
    
    output_path = os.path.join(output_dir, "gran-royal-parametrico-v1.xlsx")
    
    print("=" * 70)
    print("ORÇAMENTO PARAMÉTRICO - GRAN ROYAL RESIDENCE")
    print("Grandezza Construtora | Balneário Piçarras/SC")
    print("=" * 70)
    print()
    print(f"AC: {GRAN_ROYAL_DADOS['AC']} m²")
    print(f"UR: {GRAN_ROYAL_DADOS['UR']} unidades")
    print(f"CUB: R$ {GRAN_ROYAL_DADOS['CUB']:.2f} (SC fev/2026)")
    print()
    
    gerar_planilha(output_path, GRAN_ROYAL_DADOS, GRAN_ROYAL_BRIEFING, calibration_stats_path)
    
    print()
    print(f"✅ Planilha gerada: {output_path}")
