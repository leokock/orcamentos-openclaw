#!/usr/bin/env python3
"""Atualiza o docx de análise de Gerenciamento do Placon com seção consolidada
(1a + 2a passada, base real de 58 projetos entregues).
"""
import sys
from datetime import datetime
from pathlib import Path
import pandas as pd
from docx import Document
from docx.shared import Pt, Cm, RGBColor

sys.stdout.reconfigure(encoding="utf-8")

PACOTE = Path.home() / "orcamentos-openclaw" / "base" / "pacotes" / "placon-arminio-tavares"
CSV = Path.home() / "orcamentos-openclaw" / "base" / "executivos-gerenciamento-consolidado-2026-04-22.csv"
OUT = PACOTE / "analise-gerenciamento-placon.docx"
DRIVE = Path("G:/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/_Parametrico_IA/arminio-tavares")

DARK = RGBColor(0x2C, 0x3E, 0x50)
ACCENT = RGBColor(0x29, 0x80, 0xB9)
RED = RGBColor(0xC0, 0x39, 0x2B)
GREEN = RGBColor(0x27, 0xAE, 0x60)
GRAY = RGBColor(0x66, 0x66, 0x66)


def fmt_money(v):
    return f"R$ {v:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")


def h1(doc, text, color=DARK):
    p = doc.add_heading(text, level=1)
    for r in p.runs:
        r.font.color.rgb = color
        r.font.size = Pt(16)


def h2(doc, text, color=ACCENT):
    p = doc.add_heading(text, level=2)
    for r in p.runs:
        r.font.color.rgb = color
        r.font.size = Pt(13)


def para(doc, text, bold=False, italic=False, color=None, size=11):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    if color:
        r.font.color.rgb = color


def main():
    df = pd.read_csv(CSV)
    clean = df[(df["pct_ger"] >= 3) & (df["pct_ger"] <= 40)]
    with_ac = clean.dropna(subset=["ac_m2"])
    sim = with_ac[(with_ac["ac_m2"] >= 3000) & (with_ac["ac_m2"] <= 6000)]
    # Remover duplicatas por (cliente,projeto)
    sim = sim.drop_duplicates(subset=["cliente", "projeto"])

    # Stats
    pct_geral = clean["pct_ger"].describe(percentiles=[0.25, 0.5, 0.75, 0.9])
    rsm2_geral = with_ac["rsm2_ger"].describe(percentiles=[0.25, 0.5, 0.75, 0.9])
    pct_sim = sim["pct_ger"].describe(percentiles=[0.25, 0.5, 0.75])
    rsm2_sim = sim["rsm2_ger"].describe(percentiles=[0.25, 0.5, 0.75])

    placon_pct, placon_rsm2 = 17.14, 729
    placon_ger_atual = 2_972_792
    placon_total_atual = 17_347_024
    ac_placon = 4077.29

    p_geral_pct = (clean["pct_ger"] < placon_pct).sum() / len(clean) * 100
    p_geral_rsm2 = (with_ac["rsm2_ger"] < placon_rsm2).sum() / len(with_ac) * 100
    p_sim_pct = (sim["pct_ger"] < placon_pct).sum() / len(sim) * 100
    p_sim_rsm2 = (sim["rsm2_ger"] < placon_rsm2).sum() / len(sim) * 100

    doc = Document()
    for s in doc.sections:
        s.left_margin = Cm(2)
        s.right_margin = Cm(2)
        s.top_margin = Cm(2)
        s.bottom_margin = Cm(2)

    # === CAPA ===
    h1(doc, "Análise de Gerenciamento — Placon Armínio Tavares")
    para(doc, f"Base ampliada — {len(clean)} projetos entregues", bold=True, size=14, color=DARK)
    para(doc, f"Consolidado em {datetime.now().strftime('%d/%m/%Y %H:%M')} (1ª passada openpyxl + 2ª passada Gemma/Qwen local)",
         italic=True, color=GRAY)
    doc.add_paragraph()

    # === RESUMO EXECUTIVO ===
    h2(doc, "Resumo executivo")
    para(doc, (f"O paramétrico V2 do Placon está com Gerenciamento em {fmt_money(placon_ger_atual)} "
               f"({placon_pct}% do Grand Total, R$ {placon_rsm2}/m²). Varredura completa da base "
               f"de {len(clean)} orçamentos executivos entregues pela Cartesian (73 pastas em "
               f"_Entregas/Orçamento_executivo) confirma: o Placon está no P{p_geral_rsm2:.0f} em "
               f"R$/m² (entre os {100-p_geral_rsm2:.0f}% mais caros da base). Distribuição real: "
               f"mediana de R$ {rsm2_geral['50%']:.0f}/m² (geral) e R$ {rsm2_sim['50%']:.0f}/m² "
               f"(similar AC 3-6k m²)."), bold=True)
    doc.add_paragraph()
    para(doc, ("AÇÃO RECOMENDADA: a recomendação anterior (-R$ 310k) era conservadora. "
               "Pra alinhar com a realidade da base, o Gerenciamento-alvo deve ficar entre "
               f"{fmt_money(rsm2_sim['50%']*ac_placon)} (mediana similar) e "
               f"{fmt_money(rsm2_sim['75%']*ac_placon)} (P75 similar), representando "
               f"economia adicional de {fmt_money(placon_ger_atual - rsm2_sim['75%']*ac_placon)} "
               f"até {fmt_money(placon_ger_atual - rsm2_sim['50%']*ac_placon)}."), color=RED)
    doc.add_paragraph()

    # === BASE DE COMPARAÇÃO ===
    h2(doc, "1. Base de comparação — varredura completa")
    para(doc, "Fonte primária:")
    para(doc, "• Pasta Drive: _Entregas/Orçamento_executivo/ (73 construtoras, 162 xlsx na árvore)")
    para(doc, "• 1ª passada (openpyxl heurística): 71 xlsx 'Apresentação Orçamento' → 47 válidos")
    para(doc, "• 2ª passada (Gemma4:e4b + Qwen2.5:14b local via MCP): 30 candidatos → 13 novos válidos")
    para(doc, f"• Após dedup + sanity (% entre 3-40%): {len(clean)} projetos, {len(with_ac)} com AC conhecido")
    para(doc, f"• Subconjunto similar ao Placon (AC 3.000-6.000 m²): {len(sim)} projetos (dedup por cliente/projeto)")
    para(doc, "• Tokens Claude economizados na 2ª passada: ~150k (zero cost — tudo local)",
         italic=True, color=GREEN)
    doc.add_paragraph()

    # === DISTRIBUIÇÃO GERAL ===
    h2(doc, "2. Distribuição geral (n={})".format(len(clean)))
    t = doc.add_table(rows=1, cols=3)
    t.style = "Light Grid Accent 1"
    for i, h in enumerate(["Estatística", "% Gerenciamento", "R$/m² Gerenciamento"]):
        t.rows[0].cells[i].text = h
        for r in t.rows[0].cells[i].paragraphs[0].runs:
            r.font.bold = True
    linhas = [
        ("Mínimo", f"{clean['pct_ger'].min():.2f}%", f"R$ {with_ac['rsm2_ger'].min():.2f}"),
        ("P25", f"{pct_geral['25%']:.2f}%", f"R$ {rsm2_geral['25%']:.2f}"),
        ("Mediana (P50)", f"{pct_geral['50%']:.2f}%", f"R$ {rsm2_geral['50%']:.2f}"),
        ("P75", f"{pct_geral['75%']:.2f}%", f"R$ {rsm2_geral['75%']:.2f}"),
        ("P90", f"{pct_geral['90%']:.2f}%", f"R$ {rsm2_geral['90%']:.2f}"),
        ("Máximo", f"{clean['pct_ger'].max():.2f}%", f"R$ {with_ac['rsm2_ger'].max():.2f}"),
        ("PLACON ATUAL", f"{placon_pct}%", f"R$ {placon_rsm2}/m²"),
    ]
    for row_data in linhas:
        r = t.add_row().cells
        for i, v in enumerate(row_data):
            r[i].text = v
        if row_data[0] == "PLACON ATUAL":
            for c in r:
                for p in c.paragraphs:
                    for run in p.runs:
                        run.font.bold = True
                        run.font.color.rgb = RED
    doc.add_paragraph()

    # === SIMILARES ===
    h2(doc, f"3. Subconjunto similar — AC 3.000-6.000 m² (n={len(sim)})")
    para(doc, "Projetos comparáveis em porte ao Placon (4.077 m²):")
    t2 = doc.add_table(rows=1, cols=5)
    t2.style = "Light Grid Accent 1"
    for i, h in enumerate(["Cliente", "Projeto", "AC (m²)", "% Ger", "R$/m²"]):
        t2.rows[0].cells[i].text = h
        for r in t2.rows[0].cells[i].paragraphs[0].runs:
            r.font.bold = True
    for _, row in sim.sort_values("rsm2_ger").iterrows():
        r = t2.add_row().cells
        r[0].text = str(row["cliente"])
        r[1].text = str(row["projeto"])
        r[2].text = f"{row['ac_m2']:,.0f}".replace(",", ".")
        r[3].text = f"{row['pct_ger']:.1f}%"
        r[4].text = f"R$ {row['rsm2_ger']:.0f}".replace(",", ".")
    # Linha Placon
    r = t2.add_row().cells
    r[0].text = "PLACON"
    r[1].text = "Armínio Tavares"
    r[2].text = f"{ac_placon:,.0f}".replace(",", ".")
    r[3].text = f"{placon_pct}%"
    r[4].text = f"R$ {placon_rsm2}"
    for c in r:
        for p in c.paragraphs:
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RED
    doc.add_paragraph()

    para(doc, f"Mediana similares: {pct_sim['50%']:.1f}% / R$ {rsm2_sim['50%']:.0f}/m²  "
              f"|  P75 similares: {pct_sim['75%']:.1f}% / R$ {rsm2_sim['75%']:.0f}/m²",
         bold=True, color=ACCENT)
    doc.add_paragraph()

    # === POSIÇÃO PLACON ===
    h2(doc, "4. Posição REAL do Placon na base")
    para(doc, f"• % do total (geral, n={len(clean)}):  P{p_geral_pct:.0f}", bold=True)
    para(doc, f"• R$/m² (geral, n={len(with_ac)}):  P{p_geral_rsm2:.0f}  ⚠️ entre os {100-p_geral_rsm2:.0f}% mais caros",
         bold=True, color=RED)
    para(doc, f"• % do total (similar, n={len(sim)}):  P{p_sim_pct:.0f}")
    para(doc, f"• R$/m² (similar, n={len(sim)}):  P{p_sim_rsm2:.0f}  ⚠️ entre os {100-p_sim_rsm2:.0f}% mais caros",
         bold=True, color=RED)
    doc.add_paragraph()

    # === RECOMENDAÇÃO FINAL ===
    h2(doc, "5. Recomendação final — overrides adicionais", color=RED)

    alvo_mediana = rsm2_sim["50%"] * ac_placon
    alvo_p75 = rsm2_sim["75%"] * ac_placon
    eco_mediana = placon_ger_atual - alvo_mediana
    eco_p75 = placon_ger_atual - alvo_p75

    para(doc, "Cenário A — alvo P75 similar (conservador):", bold=True, color=DARK)
    para(doc, f"  Gerenciamento-alvo: {fmt_money(alvo_p75)} ({pct_sim['75%']:.1f}% do total atual)")
    para(doc, f"  Economia: {fmt_money(eco_p75)} (além dos R$ 569k dos overrides iniciais Leo)")
    para(doc, f"  Grand Total novo: {fmt_money(placon_total_atual - eco_p75)}")
    para(doc, f"  RSM² total: R$ {(placon_total_atual - eco_p75) / ac_placon:,.2f}".replace(",","X").replace(".",",").replace("X","."))
    doc.add_paragraph()

    para(doc, "Cenário B — alvo mediana similar (agressivo):", bold=True, color=DARK)
    para(doc, f"  Gerenciamento-alvo: {fmt_money(alvo_mediana)} ({pct_sim['50%']:.1f}% do total atual)")
    para(doc, f"  Economia: {fmt_money(eco_mediana)}")
    para(doc, f"  Grand Total novo: {fmt_money(placon_total_atual - eco_mediana)}")
    para(doc, f"  RSM² total: R$ {(placon_total_atual - eco_mediana) / ac_placon:,.2f}".replace(",","X").replace(".",",").replace("X","."))
    doc.add_paragraph()

    para(doc, "Itens candidatos a reduzir (além dos já ajustados):", bold=True)
    para(doc, "• Projetos (r4) — R$ 650k → revisar proposta real do projetista (talvez R$ 400-500k)")
    para(doc, "• Taxas e seguros (r7) — R$ 380k → R$ 200-280k (P75 histórico < 2%)")
    para(doc, "• Equipamentos grua+cremalh (r22) — R$ 480k → R$ 280-320k (validar com planejamento: laje protendida em 4k m² aceita mini-grua)")
    para(doc, "• Instalações provisórias (r20) — R$ 160k → R$ 100-120k (canteiro 900 m², escala menor)")
    para(doc, "• Desp. consumo (r21) — R$ 276k → R$ 200k (R$ 8,3k/mês em vez de R$ 11,5k/mês)")
    para(doc, "• Op. inicial (r19) — R$ 55k → R$ 40k")
    para(doc, "• EPCs (r16) — R$ 150k → R$ 90k (AC<5k)")
    doc.add_paragraph()

    # === CAVEATS ===
    h2(doc, "6. Ressalvas")
    para(doc, "• Alguns projetos podem incluir BDI indireto (lucro) dentro de Gerenciamento — não é 100% apple-to-apple")
    para(doc, "• Projetos de litoral e centros históricos têm taxas/licenças/habite-se mais altos — Placon é centro Floripa, justifica algum prêmio")
    para(doc, "• Grua-torre vs mini-grua: economia R$ 180k está condicionada ao OK do planejamento técnico")
    para(doc, "• Amostra com AC similar ainda é pequena (n=9 sem duplicatas) — estatística tem variância alta")
    doc.add_paragraph()

    # === APÊNDICE ===
    h2(doc, "7. Apêndice — todos os 58 projetos da base")
    t3 = doc.add_table(rows=1, cols=5)
    t3.style = "Light Grid Accent 1"
    for i, h in enumerate(["Cliente", "Projeto", "AC (m²)", "% Ger", "R$/m²"]):
        t3.rows[0].cells[i].text = h
        for r in t3.rows[0].cells[i].paragraphs[0].runs:
            r.font.bold = True
    for _, row in clean.sort_values("rsm2_ger", ascending=True, na_position="last").iterrows():
        r = t3.add_row().cells
        r[0].text = str(row["cliente"])[:20]
        r[1].text = str(row["projeto"])[:25]
        r[2].text = f"{row['ac_m2']:,.0f}".replace(",", ".") if pd.notna(row["ac_m2"]) else "—"
        r[3].text = f"{row['pct_ger']:.1f}%"
        r[4].text = f"R$ {row['rsm2_ger']:.0f}" if pd.notna(row["rsm2_ger"]) else "—"

    doc.save(OUT)
    print(f"[ok] {OUT.name} ({OUT.stat().st_size} bytes)")

    # Copiar pro Drive
    drive_dst = DRIVE / "arminio-tavares-analise-gerenciamento-2026-04-22.docx"
    import shutil
    try:
        shutil.copy2(OUT, drive_dst)
        print(f"[ok] Drive: {drive_dst.name}")
    except Exception as e:
        print(f"[err] Drive copy: {e}")

    print(f"\n=== Resumo ===")
    print(f"Base: {len(clean)} projetos (1a + 2a passada)")
    print(f"Similar AC 3-6k: {len(sim)} projetos")
    print(f"Placon está em P{p_geral_rsm2:.0f} em R$/m² (entre os {100-p_geral_rsm2:.0f}% mais caros)")
    print(f"Alvo P75 similar: {fmt_money(alvo_p75)}  (economia {fmt_money(eco_p75)})")
    print(f"Alvo mediana similar: {fmt_money(alvo_mediana)}  (economia {fmt_money(eco_mediana)})")


if __name__ == "__main__":
    main()
