#!/usr/bin/env python3
"""Aplica cenário MODERADO no paramétrico Placon (decisão Leo 23/04/2026).

Cenário moderado = 9 overrides adicionais em Gerenciamento, economia ~R$ 395k,
Gerenciamento-alvo: R$ 3.089k (17,3% do total, R$ 758/m²).
"""
import sys
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

sys.stdout.reconfigure(encoding="utf-8")

XLSX = Path.home() / "orcamentos-openclaw" / "base" / "pacotes" / "placon-arminio-tavares" / "parametrico-placon-arminio-tavares.xlsx"

OVERRIDE_FILL = PatternFill(start_color="FFF3E0", end_color="FFF3E0", fill_type="solid")
OVERRIDE_FONT = Font(bold=True, size=9, color="E67E22", name="Arial")

# (row, col_pu, novo_pu, nota)
OVERRIDES_PU = [
    (4,  500_000, "Projetos — override Leo (de R$ 650k, base Cartesian P75)"),
    (5,  150_000, "Consultorias — override Leo (de R$ 180k)"),
    (7,  280_000, "Taxas e seguros — override Leo (de R$ 380k, P75 histórico 1,13%)"),
    (13, 3_000,   "Almoxarife mês — override Leo (de R$ 3.377)"),
    (16, 110_000, "EPCs — override Leo (de R$ 150k)"),
    (19, 40_000,  "Op. inicial — override Leo (de R$ 55k)"),
    (20, 110_000, "Inst. provisórias — override Leo (de R$ 160k)"),
    (21, 8_500,   "Desp. consumo mês — override Leo (de R$ 11.500)"),
]


def main():
    print(f"[info] abrindo {XLSX.name}")
    wb = load_workbook(XLSX)
    ws = wb["Gerenciamento"]

    print("[info] aplicando overrides de PU (cenário moderado):")
    for row, novo_pu, nota in OVERRIDES_PU:
        desc = ws.cell(row, 2).value
        pu_antigo = ws.cell(row, 5).value
        print(f"  r{row} | {desc:30s} | PU {pu_antigo} -> {novo_pu}")
        c = ws.cell(row, 5, novo_pu)
        c.number_format = '#,##0.00'
        c.font = OVERRIDE_FONT
        c.fill = OVERRIDE_FILL

    # r14 Limpeza — especial (muda qtd e desc)
    print("  r14 | Limpeza obra | qtd 48 -> 24, desc '2×prazo' -> '1×24m+reforço', PU 2.500 -> 3.125")
    ws.cell(14, 2, "1×24m + reforço 6m")
    ws.cell(14, 3, 24)  # quebra a fórmula antiga, usa valor fixo
    ws.cell(14, 3).number_format = '#,##0'
    pu14 = ws.cell(14, 5, 3125)
    pu14.number_format = '#,##0.00'
    pu14.font = OVERRIDE_FONT
    pu14.fill = OVERRIDE_FILL

    # Atualiza nota no topo
    nota_topo = ("OVERRIDES Leo 23/04 (cenário MODERADO): Projetos 500k, Consultorias 150k, "
                 "Taxas 280k, Almoxarife 3k/mês, Limpeza 75k, EPCs 110k, OpIn 40k, InstProv 110k, "
                 "DespCons 8,5k/mês. Ger-alvo: R$ 3.089k (17,3%, R$ 758/m²).")
    ws.cell(2, 1, nota_topo)
    ws.cell(2, 1).font = Font(italic=True, size=8, color="E67E22", name="Arial")

    wb.save(XLSX)
    print(f"[ok] xlsx salvo")


if __name__ == "__main__":
    main()
