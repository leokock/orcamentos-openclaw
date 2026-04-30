#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Paramétrico: Studios Balneário Camboriú (viabilidade)
Shell delivery — apenas paredes perimetrais + banheiros
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_template_dinamico import gerar_planilha

# Dados do projeto
DADOS = {
    "Nome": "Studios BC — Viabilidade",
    "Código": "STUDIOS-BC",
    "Cidade": "Balneário Camboriú/SC",
    "AC": 20280.00,       # 1.716 + 5.148 + 13.416
    "UR": 280,            # 280 studios ~30m²
    "UC": 0,              # comerciais
    "NP": 16,             # total pavimentos
    "NPT": 12,            # lazer + tipos (16 - 1 térreo - 3 garagens)
    "NPG": 4,             # térreo + G1-G3
    "ELEV": 2,            # premissa Leo
    "VAG": 220,           # estimativa (6.864m² garagem / ~31m² por vaga)
    "AT": 1200,           # estimativa (terreno BC padrão)
    "NS": 0,              # sem subsolo
    "Prazo": 36,          # meses
    "CUB": 3028.45,       # CUB SC mar/2026
}

# Briefing — premissas baseadas no render + informações do Leo
BRIEFING = {
    "Q1": "Hélice Contínua",       # Fundação — padrão BC
    "Q2": "Cubetas",                # Laje — Leo confirmou
    "Q3": "Não",                    # Contenção — sem subsolo
    "Q4": "0",                      # Subsolos — Leo confirmou
    "Q5": "Alto",                   # Padrão — fachada render indica alto
    "Q6": "Alto desempenho",        # Esquadria — pele de vidro no render
    "Q7": "Porcelanato padrão",     # Piso — áreas comuns (studios = shell)
    "Q8": "Alvenaria",             # Vedação
    "Q9": "Gesso liso",            # Forro — áreas comuns
    "Q10": "Misto",                 # Fachada — tijolo aparente + pele de vidro
    "Q11": "Empreitada",           # MO Fachada
    "Q12": "Não",                   # Cobertura habitável
    "Q13": "Gás individual",       # Aquecimento
    "Q14": "Mínimo",               # Automação — studios
    "Q15": "Sem",                   # Energia solar
    "Q16": "Completo",             # Lazer — piscina na fachada, BC padrão
    "Q17": "Básico",               # Paisagismo
    "Q18": "Sem",                   # Mobiliário — shell delivery
    "Q19": "36",                    # Prazo — Leo confirmou
    "Q20": "Litoral SC",           # Região — BC
    "Q21": "Sim",                   # Gerador — padrão BC
    "Q22": "Não",                   # Subestação
    "Q23": "Não",                   # Fotovoltaicas
    "Q24": "Não",                   # Carro elétrico
    "Q25": "Sim",                   # Pressurização — 16 andares
}

output_dir = os.path.expanduser("~/clawd/orcamento-parametrico/parametricos")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "studios-bc-parametrico-v1.xlsx")
calibration_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "calibration-stats.json"
)

print("=" * 70)
print("PARAMÉTRICO: STUDIOS BALNEÁRIO CAMBORIÚ — VIABILIDADE")
print("=" * 70)
gerar_planilha(output_path, DADOS, BRIEFING, calibration_path)
print(f"\nArquivo: {output_path}")
print()

# ============================================================================
# ANÁLISE: CUSTO POR TIPO DE ÁREA (Lazer+Tipos vs Garagem)
# ============================================================================
# O paramétrico calcula R$/m² médio da AC total.
# Para viabilidade, o amigo precisa de custo separado:
# - Lazer + Tipos: custo cheio
# - Garagem (térreo + G1-G3): custo reduzido (~55-65% do médio)
#
# Além disso: ENTREGA SHELL nos studios
# Sem: layout interno, pisos, forro, pintura interna, louças/metais (nos aptos)
# Com: paredes perimetrais, banheiro, fachada, estrutura, instalações base

from gerar_template_dinamico import (
    MEDIANAS_BASE_DEZ23, FAIXAS_BASE_DEZ23, CUB_BASE_HISTORICO, BRIEFING as BRIEFING_QUESTOES
)

cub_atual = DADOS["CUB"]
fator_cub = cub_atual / CUB_BASE_HISTORICO

# Calcular fator briefing por macrogrupo
from gerar_template_dinamico import MACROGRUPOS

def calc_fator_briefing(macrogrupo, briefing_respostas):
    fator = 1.0
    for q in BRIEFING_QUESTOES:
        num = q["num"]
        afeta = q["afeta"]
        resp = briefing_respostas.get(num)
        if resp is None:
            continue
        if macrogrupo in afeta:
            f = q["fatores"].get(macrogrupo, {}).get(resp, 1.0)
            fator *= f
        elif "TODOS" in afeta:
            f = q["fatores"].get("TODOS", {}).get(resp, 1.0)
            fator *= f
    return fator

print("=" * 70)
print("CUSTOS POR MACROGRUPO (R$/m² AC)")
print("=" * 70)

total_rsm2 = 0
custos_macro = {}
for mg in MACROGRUPOS:
    base = MEDIANAS_BASE_DEZ23[mg]
    fb = calc_fator_briefing(mg, BRIEFING)
    ajustado = base * fator_cub * fb
    custos_macro[mg] = ajustado
    total_rsm2 += ajustado
    print(f"  {mg:25s}: R$ {ajustado:>8.2f}/m²  (fator CUB={fator_cub:.4f}, briefing={fb:.4f})")

print(f"\n  {'TOTAL':25s}: R$ {total_rsm2:>8.2f}/m²")
print(f"  CUB Ratio: {total_rsm2/cub_atual:.2f}")
total_abs = total_rsm2 * DADOS["AC"]
print(f"  Custo Total: R$ {total_abs:,.2f}")

# ============================================================================
# DISTRIBUIÇÃO POR TIPO DE ÁREA
# ============================================================================
area_garagem = 1716 + 5148  # 6.864 m²
area_lazer_tipos = 13416    # m²
ac_total = 20280

# Macrogrupos que incidem MENOS na garagem (peso relativo)
# Garagem: estrutura + instalações básicas, sem acabamento
# Peso garagem por macrogrupo (0 a 1, onde 1 = incide igual, <1 = incide menos)
peso_garagem = {
    "Gerenciamento":       0.80,   # rateio proporcional, ligeiramente menor
    "Mov. Terra":          1.00,   # igual
    "Infraestrutura":      1.00,   # fundação é pra tudo
    "Supraestrutura":      0.85,   # laje garagem é mais simples
    "Alvenaria":           0.30,   # quase nenhuma (só periferia)
    "Impermeabilização":   0.60,   # impermeabilização de garagem
    "Instalações":         0.40,   # só hidráulica básica + elétrica iluminação
    "Sist. Especiais":     0.15,   # elevadores passam mas pouco
    "Climatização":        0.05,   # quase zero (exaustão mecânica)
    "Rev. Int. Parede":    0.10,   # não tem
    "Teto":                0.05,   # sem forro
    "Pisos":               0.20,   # piso industrial/polido
    "Pintura":             0.30,   # pintura básica garagem
    "Esquadrias":          0.05,   # portão, quase nada
    "Louças e Metais":     0.00,   # zero
    "Fachada":             0.30,   # parte da fachada
    "Complementares":      0.20,   # sinalização, rampa
    "Imprevistos":         0.80,   # proporcional
}

# Custo ponderado garagem
custo_gar_m2 = sum(custos_macro[mg] * peso_garagem[mg] for mg in MACROGRUPOS)
custo_gar_total = custo_gar_m2 * area_garagem

# Custo residual para lazer+tipos
custo_total = total_rsm2 * ac_total
custo_lt_total = custo_total - custo_gar_total
custo_lt_m2 = custo_lt_total / area_lazer_tipos

print("\n" + "=" * 70)
print("DISTRIBUIÇÃO POR TIPO DE ÁREA (ENTREGA COMPLETA)")
print("=" * 70)
print(f"  Garagem (6.864 m²):      R$ {custo_gar_m2:>8.2f}/m²  |  Total: R$ {custo_gar_total:>12,.2f}")
print(f"  Lazer+Tipos (13.416 m²): R$ {custo_lt_m2:>8.2f}/m²  |  Total: R$ {custo_lt_total:>12,.2f}")
print(f"  Média AC (20.280 m²):    R$ {total_rsm2:>8.2f}/m²  |  Total: R$ {custo_total:>12,.2f}")
print(f"  Ratio Gar/Tipos: {custo_gar_m2/custo_lt_m2*100:.0f}%")

# ============================================================================
# AJUSTE SHELL DELIVERY (redução nos studios)
# ============================================================================
# Studios = 280 un × 30m² = 8.400 m² de área privativa
# Shell: sem pisos, sem forro, sem pintura interna, sem louças/metais
# Mantém: estrutura, instalações base (pontos), paredes perimetrais + banheiro, fachada
area_shell = 280 * 30  # 8.400 m²
frac_shell = area_shell / ac_total  # ~41%

# Itens economizados no shell (% do macrogrupo que se economiza, aplicado à fração shell)
economia_shell = {
    "Rev. Int. Parede":  0.60,  # economiza 60% do rev. interno (mantém banheiro + periferia)
    "Teto":              0.80,  # economiza 80% do forro (mantém banheiro)
    "Pisos":             0.80,  # economiza 80% dos pisos (mantém banheiro)
    "Pintura":           0.60,  # economiza 60% da pintura (mantém periferia)
    "Louças e Metais":   0.70,  # economiza 70% (mantém cubas banheiro mínimas)
    "Alvenaria":         0.30,  # economiza 30% (sem paredes internas do layout)
}

economia_total_m2 = 0
print("\n" + "=" * 70)
print("AJUSTE SHELL DELIVERY (desconto por entrega sem acabamento interno)")
print("=" * 70)
for mg, perc in economia_shell.items():
    economia_mg = custos_macro[mg] * perc * frac_shell
    economia_total_m2 += economia_mg
    print(f"  {mg:25s}: -R$ {economia_mg:>6.2f}/m² ({perc*100:.0f}% de {custos_macro[mg]:.2f} × {frac_shell*100:.0f}% AC)")

total_shell_m2 = total_rsm2 - economia_total_m2
custo_total_shell = total_shell_m2 * ac_total

# Redistribuir shell para garagem e tipos
custo_gar_shell_total = custo_gar_total  # garagem não muda
custo_lt_shell_total = custo_total_shell - custo_gar_shell_total
custo_lt_shell_m2 = custo_lt_shell_total / area_lazer_tipos

print(f"\n  Economia total shell: R$ {economia_total_m2:.2f}/m² AC")
print(f"  Novo R$/m² AC (shell): R$ {total_shell_m2:.2f}/m²")

print("\n" + "=" * 70)
print("RESULTADO FINAL — SHELL DELIVERY")
print("=" * 70)
print(f"  Garagem (6.864 m²):      R$ {custo_gar_m2:>8.2f}/m²")
print(f"  Lazer+Tipos (13.416 m²): R$ {custo_lt_shell_m2:>8.2f}/m²  (com desconto shell)")
print(f"  Média AC (20.280 m²):    R$ {total_shell_m2:>8.2f}/m²")
print(f"  Custo Total: R$ {custo_total_shell:>12,.2f}")
print(f"  Ratio Gar/Tipos: {custo_gar_m2/custo_lt_shell_m2*100:.0f}%")

print("\n" + "=" * 70)
print("COMPARAÇÃO COM PREMISSA DO CLIENTE")
print("=" * 70)
premissa_lt = 4000
premissa_gar = 2400
premissa_total = premissa_lt * area_lazer_tipos + premissa_gar * area_garagem
print(f"  Premissa cliente:")
print(f"    Lazer+Tipos: R$ {premissa_lt:,.2f}/m²")
print(f"    Garagem:     R$ {premissa_gar:,.2f}/m²")
print(f"    Total:       R$ {premissa_total:>12,.2f}")
print(f"\n  Paramétrico (shell):")
print(f"    Lazer+Tipos: R$ {custo_lt_shell_m2:,.2f}/m²  ({(custo_lt_shell_m2/premissa_lt-1)*100:+.1f}%)")
print(f"    Garagem:     R$ {custo_gar_m2:,.2f}/m²  ({(custo_gar_m2/premissa_gar-1)*100:+.1f}%)")
print(f"    Total:       R$ {custo_total_shell:>12,.2f}  ({(custo_total_shell/premissa_total-1)*100:+.1f}%)")
print()
