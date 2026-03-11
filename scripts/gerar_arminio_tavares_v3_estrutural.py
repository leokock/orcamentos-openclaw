#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - Arminio Tavares (PLACON)
Versão 3 - Ajustado com Dados Estruturais do IFC
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from gerar_template_dinamico import gerar_planilha
from datetime import datetime

# Dados do Projeto Arminio Tavares (CORRIGIDOS + IFC ESTRUTURAL)
ARMINIO_DADOS = {
    "Nome": "Arminio Tavares",
    "Cliente": "PLACON",
    "Localização": "Rua Dr. Armínio Tavares - Centro - Florianópolis/SC",
    "AC": 7996.45,           # Área Construída
    "UR": 45,                # Unidades
    "NP": 15,                # Pavimentos Tipo
    "NPT": 22,               # Pavimentos Totais (2 sub + 16 pav + 4 técnicos)
    "NS": 2,                 # Subsolos
    "ELEV": 2,               # Elevadores
    "VAG": 50,               # Vagas
    "AT": 486.40,            # Área Terreno
    "AS": 1314.20,           # Área Subsolos
    "APT": None,             # Área Projeção Torre
    "PPT": None,             # Perímetro Projeção Torre
    "Prazo": 30,             # meses
    "CUB": 3150.00,          # R$/m² mar/2026
    "Data-base": "mar/2026",
    # Dados estruturais do IFC
    "Volume_Concreto_m3": 1599.24,
    "Consumo_Concreto_L_m2": 200
}

# Respostas do Briefing (25 variáveis) - ATUALIZADO COM LAJE MACIÇA
ARMINIO_BRIEFING = {
    # Alto Impacto
    "Q1": "Estacas Escavadas",        # Fundação (centro Floripa)
    "Q2": "Maciça",                    # Tipo de Laje (CORRIGIDO do IFC estrutural)
    "Q3": "Cortina de concreto",       # Contenção (2 subsolos)
    "Q4": "2",                         # Nº Subsolos
    "Q5": "Alto Padrão",               # Acabamento (PLACON)
    
    # Médio Impacto
    "Q6": "Alumínio Anodizado",        # Esquadrias
    "Q7": "Porcelanato",               # Piso
    "Q8": "Alvenaria",                 # Vedação
    "Q9": "Gesso liso",                # Forro
    "Q10": "Textura + Pintura",        # Fachada
    "Q11": "Equipe própria",           # MO Fachada
    "Q12": "Não",                      # Cobertura Habitável
    "Q13": "Gás individual",           # Aquecimento
    "Q14": "Básico",                   # Automação
    "Q15": "Sem",                      # Energia Solar
    "Q16": "Completo",                 # Lazer (piscina + academia)
    "Q17": "Básico",                   # Paisagismo
    "Q18": "Sem",                      # Mobiliário
    "Q19": "30",                       # Prazo (meses)
    "Q20": "Capital Floripa",          # Região
    
    # Infraestrutura Técnica
    "Q21": "Sim",                      # Gerador
    "Q22": "Não",                      # Subestação
    "Q23": "Não",                      # Placas Fotovoltaicas
    "Q24": "Sim",                      # Infra Carro Elétrico
    "Q25": "Sim"                       # Pressurização Escada
}

if __name__ == "__main__":
    # Diretório de saída
    output_dir = os.path.expanduser("~/parametrico/output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Arquivo de saída
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    output_path = os.path.join(output_dir, f"Arminio-Tavares-Parametrico-v3-estrutural-{timestamp}.xlsx")
    
    # Caminho para calibration-stats.json
    calibration_stats_path = os.path.expanduser("~/parametrico/calibration-stats.json")
    
    print("=" * 80)
    print("ORÇAMENTO PARAMÉTRICO - ARMINIO TAVARES (PLACON)")
    print("Versão 3 - Ajustado com Dados Estruturais do IFC")
    print("=" * 80)
    print()
    print("DADOS DO PROJETO:")
    print(f"  • Área Construída: {ARMINIO_DADOS['AC']:,.2f} m²")
    print(f"  • Unidades: {ARMINIO_DADOS['UR']}")
    print(f"  • Pavimentos: {ARMINIO_DADOS['NPT']} totais ({ARMINIO_DADOS['NP']} tipo)")
    print(f"  • Subsolos: {ARMINIO_DADOS['NS']} ({ARMINIO_DADOS['AS']:,.2f} m²)")
    print(f"  • CUB mar/2026: R$ {ARMINIO_DADOS['CUB']:,.2f}/m²")
    print()
    print("DADOS ESTRUTURAIS (IFC):")
    print(f"  • Volume de Concreto: {ARMINIO_DADOS['Volume_Concreto_m3']:,.2f} m³")
    print(f"  • Consumo: {ARMINIO_DADOS['Consumo_Concreto_L_m2']} L/m²")
    print(f"  • Tipo de Laje: Maciça h=20cm (C40)")
    print()
    
    # Gera planilha
    gerar_planilha(output_path, ARMINIO_DADOS, ARMINIO_BRIEFING, calibration_stats_path)
    
    print()
    print("=" * 80)
    print(f"✓ Planilha gerada: {output_path}")
    print("=" * 80)
