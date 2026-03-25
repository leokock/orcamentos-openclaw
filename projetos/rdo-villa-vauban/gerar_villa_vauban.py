#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - Villa Vauban (RDO)
Florianópolis/SC - Estreito
"""

import sys
import os

# Adicionar path do script original
sys.path.insert(0, os.path.expanduser("~/clawd/orcamento-parametrico/scripts"))
from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO - VILLA VAUBAN (RDO)
# ============================================================================

VILLA_VAUBAN_DADOS = {
    "Nome": "RDO — Villa Vauban",
    "Código": "VLV-VAUBAN",
    "Cidade": "Florianópolis/SC (Estreito)",
    "AC": 25000.00,       # ⚠️ ESTIMADO — sem quadro de áreas oficial
                           # Referência: ~147 UR × 120m² priv, 3 subsolos, 19 pav
                           # Faixa provável: 22.000-30.000 m²
    "UR": 147,             # ESTIMADO — 11 un/pav × 13 pav tipo + coberturas
    "UC": 2,               # CONFIRMADO — 2 lojas no térreo
    "NP": 19,              # CONFIRMADO
    "NPT": 13,             # CONFIRMADO — 4º ao 16º PAV (tipodif + 11 regulares + 1 tipo16)
    "NPG": 4,              # 3 subsolos + garagem embasamento
    "ELEV": 3,             # ESTIMADO — porte do projeto (147 UR, 19 pav) sugere 3
    "VAG": 79,             # CONFIRMADO — extraído de cálculo PPCI ventilação (79×300=23.700m³/h)
    "AT": 1500.00,         # ⚠️ ESTIMADO — terreno urbano Floripa, sem dado oficial
    "NS": 3,               # CONFIRMADO — 3 subsolos
    "Prazo": 30,           # CONFIRMADO — informado pelo Leo
    "CUB": 3019.26         # CUB SC fev/2026 (R8-N) — mar/2026 não disponível ainda
}

# ============================================================================
# BRIEFING - 25 PERGUNTAS RESPONDIDAS
# ============================================================================

VILLA_VAUBAN_BRIEFING = {
    "Q1": "Hélice Contínua",        # CONFIRMADO — projeto estrutural
    "Q2": "Cubetas",                 # CONFIRMADO — "nervurada e=30cm" = Cubetas no script
    "Q3": "Cortina de estacas",      # CONFIRMADO — parede diafragma 73 lamelas 40cm
    "Q4": "3",                       # CONFIRMADO — 3 subsolos
    "Q5": "Alto",                    # CONFIRMADO — informado pelo Leo
    "Q6": "Alumínio anodizado",      # CONFIRMADO — alumínio anodizado grafite (fachada)
    "Q7": "Porcelanato padrão",      # ESTIMADO — alto padrão Floripa, sem confirmação
    "Q8": "Alvenaria",               # ESTIMADO — sem dado, padrão de mercado
    "Q9": "Gesso liso",              # ESTIMADO — alto padrão, sem confirmação
    "Q10": "Cerâmica/Pastilha",      # CONFIRMADO — pastilhas Atlas 3 cores
    "Q11": "Empreitada",             # ESTIMADO — 19 pav, porte grande
    "Q12": "Completa",               # ESTIMADO — ático + cobertura dedicada
    "Q13": "Gás individual",         # CONFIRMADO — gás natural, passagem, exaustão forçada
    "Q14": "Básico",                 # ESTIMADO — alto padrão sugere básico
    "Q15": "Sem",                    # ESTIMADO — nada identificado nos projetos
    "Q16": "Completo",               # ESTIMADO — piscina, SPA, prainha, fitness, salões
    "Q17": "Básico",                 # ESTIMADO — sem dado
    "Q18": "Básico",                 # ESTIMADO — sem dado
    "Q19": "30",                     # CONFIRMADO — Leo
    "Q20": "Capital Floripa",        # CONFIRMADO — Estreito, Florianópolis
    "Q21": "Sim",                    # CONFIRMADO — sala gerador 15,82m²
    "Q22": "Sim",                    # CONFIRMADO — subestação 44,11m²
    "Q23": "Não",                    # ESTIMADO — nada identificado
    "Q24": "Não",                    # ESTIMADO — nada identificado
    "Q25": "Sim"                     # ESTIMADO — TRRF 120min + 19 pav, provável pressurização
}

# ============================================================================
# GERAR PLANILHA
# ============================================================================

if __name__ == "__main__":
    output_dir = os.path.expanduser("~/orcamentos/projetos/rdo-villa-vauban/analise")
    os.makedirs(output_dir, exist_ok=True)

    calibration_stats_path = os.path.expanduser(
        "~/clawd/orcamento-parametrico/calibration-stats.json"
    )

    output_path = os.path.join(output_dir, "villa-vauban-parametrico-v1.xlsx")

    print("=" * 70)
    print("ORÇAMENTO PARAMÉTRICO - VILLA VAUBAN (RDO)")
    print("Florianópolis/SC (Estreito)")
    print("=" * 70)
    print()
    print(f"AC: {VILLA_VAUBAN_DADOS['AC']} m² (ESTIMADO)")
    print(f"UR: {VILLA_VAUBAN_DADOS['UR']} unidades (ESTIMADO)")
    print(f"Subsolos: {VILLA_VAUBAN_DADOS['NS']}")
    print(f"Vagas: {VILLA_VAUBAN_DADOS['VAG']}")
    print(f"CUB: R$ {VILLA_VAUBAN_DADOS['CUB']:.2f} (SC fev/2026)")
    print()

    gerar_planilha(output_path, VILLA_VAUBAN_DADOS, VILLA_VAUBAN_BRIEFING, calibration_stats_path)

    print()
    print(f"✅ Planilha gerada: {output_path}")
