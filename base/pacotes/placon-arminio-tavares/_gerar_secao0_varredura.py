#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gera a SEÇÃO 0 — Varredura completa da base de executivos entregues —
prependendo no analise-gerenciamento-placon.docx.

Copia o docx original, insere a seção nova no início, e salva como novo arquivo
(sobrescreve o original depois de backup).
"""
from __future__ import annotations

import bisect
import csv
import io
import shutil
import statistics
import sys
from pathlib import Path

import docx
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DOC_PATH = Path(r"C:\Users\leona\orcamentos-openclaw\base\pacotes\placon-arminio-tavares\analise-gerenciamento-placon.docx")
CSV_PATH = Path(r"C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-apresentacoes-2026-04-22.csv")

PLACON_AC = 4077.29
PLACON_GER = 3483456
PLACON_GT = 17865738
PLACON_PCT = PLACON_GER / PLACON_GT
PLACON_RSM2 = PLACON_GER / PLACON_AC


def load_data():
    with open(CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct_of(value, sorted_list):
    pos = bisect.bisect_left(sorted_list, value)
    return pos * 100 / len(sorted_list)


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    return h


def add_para(doc, text, bold=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    if bold:
        run.bold = True
    return p


def add_bullet(doc, text):
    p = doc.add_paragraph(text, style="List Bullet")
    return p


def set_cell_bg(cell, color_hex):
    """Pinta fundo de célula."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = docx.oxml.OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    tc_pr.append(shd)


def build_secao0_doc(data):
    """Monta um docx novo com a Seção 0, depois merge com o original."""
    # 1) Estatísticas
    valid = [r for r in data if r["total_obra"] and r["total_gerenciamento"]]
    good = [r for r in valid if 0.02 < float(r["pct_gerenciamento"]) < 0.40]

    pcts = sorted(float(r["pct_gerenciamento"]) for r in good)
    with_ac = [r for r in good if r["ac_m2"]]
    rsm2s = sorted(float(r["rsm2_gerenciamento"]) for r in with_ac)

    similar = [r for r in with_ac if 3000 <= float(r["ac_m2"]) <= 6000]
    sim_pcts = sorted(float(r["pct_gerenciamento"]) for r in similar)
    sim_rsm2 = sorted(float(r["rsm2_gerenciamento"]) for r in similar)

    def p(vs, q):
        if not vs:
            return None
        i = int(q * (len(vs) - 1))
        return vs[i]

    stats = {
        "n_total": len(data),
        "n_valid": len(valid),
        "n_good": len(good),
        "n_ac": len(with_ac),
        "n_sim": len(similar),
        "pct_min": pcts[0],
        "pct_p25": p(pcts, 0.25),
        "pct_p50": statistics.median(pcts),
        "pct_p75": p(pcts, 0.75),
        "pct_p90": p(pcts, 0.90),
        "pct_max": pcts[-1],
        "pct_mean": statistics.mean(pcts),
        "rsm2_p25": p(rsm2s, 0.25),
        "rsm2_p50": statistics.median(rsm2s) if rsm2s else None,
        "rsm2_p75": p(rsm2s, 0.75),
        "rsm2_p90": p(rsm2s, 0.90),
        "rsm2_mean": statistics.mean(rsm2s) if rsm2s else None,
        "sim_pct_p25": p(sim_pcts, 0.25),
        "sim_pct_p50": statistics.median(sim_pcts),
        "sim_pct_p75": p(sim_pcts, 0.75),
        "sim_pct_p90": p(sim_pcts, 0.90),
        "sim_pct_max": sim_pcts[-1],
        "sim_rsm2_p25": p(sim_rsm2, 0.25),
        "sim_rsm2_p50": statistics.median(sim_rsm2),
        "sim_rsm2_p75": p(sim_rsm2, 0.75),
        "sim_rsm2_p90": p(sim_rsm2, 0.90),
        "sim_rsm2_max": sim_rsm2[-1],
        "placon_pctile_global": pct_of(PLACON_PCT, pcts),
        "placon_pctile_sim": pct_of(PLACON_PCT, sim_pcts),
        "placon_rsm2_pctile_global": pct_of(PLACON_RSM2, rsm2s),
        "placon_rsm2_pctile_sim": pct_of(PLACON_RSM2, sim_rsm2),
    }

    # TOP 10 projetos mais próximos por AC
    top10 = sorted(with_ac, key=lambda r: abs(float(r["ac_m2"]) - PLACON_AC))[:10]

    # 2) Monta docx novo com Seção 0
    newdoc = Document()

    # Estilo
    style = newdoc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10)

    # Título da seção
    h = newdoc.add_heading("0. Varredura completa da base de executivos entregues", level=1)

    newdoc.add_paragraph(
        f"Complemento da análise paramétrica (Seções 1-6). "
        f"Nesta seção 0 cruzamos o Gerenciamento do Placon com os orçamentos executivos "
        f"já entregues pela Cartesian, extraídos direto dos xlsx de apresentação em "
        f"_Entregas/Orçamento_executivo/. Essa é a base ORÇAMENTOS REAIS (preço fechado "
        f"por obra real), distinta da base paramétrica de índices do Supabase."
    )
    newdoc.add_paragraph(
        f"Data da varredura: 2026-04-22  |  Script: scripts/varrer_gerenciamento_apresentacoes.py  |  "
        f"CSV: base/executivos-gerenciamento-apresentacoes-2026-04-22.csv"
    ).runs[0].font.size = Pt(9)

    # 0.1 Cobertura
    newdoc.add_heading("0.1 Cobertura da varredura", level=2)
    newdoc.add_paragraph(
        f"Foram varridos 162 xlsx na árvore do Drive (_Entregas/Orçamento_executivo/, "
        f"73 pastas de construtora/cliente). Destes, 71 são arquivos do tipo "
        f"“Apresentação Orçamento” (1 por projeto), com formato padronizado "
        f"(aba ORÇAMENTO_EXECUTIVO contendo ETAPA | VALOR | % | R$/m² + linha TOTAL + "
        f"bloco ÁREA CONSTRUÍDA). O script foca neles por serem os resumos oficiais "
        f"entregues ao cliente."
    )

    tbl = newdoc.add_table(rows=5, cols=2)
    tbl.style = "Light Grid Accent 1"
    rows_data = [
        ("xlsx de Apresentação no Drive", f"{stats['n_total']}"),
        ("Com total de obra + gerenciamento válidos", f"{stats['n_valid']}"),
        ("Filtro razoável (2% < pct < 40%)", f"{stats['n_good']}"),
        ("Com AC (área construída) extraída", f"{stats['n_ac']}"),
        ("Subconjunto similar ao Placon (AC 3.000–6.000 m²)", f"{stats['n_sim']}"),
    ]
    for i, (k, v) in enumerate(rows_data):
        tbl.rows[i].cells[0].text = k
        tbl.rows[i].cells[1].text = v

    # 0.2 Distribuição geral
    newdoc.add_heading("0.2 Distribuição geral (n={})".format(stats["n_good"]), level=2)
    newdoc.add_paragraph(
        "Gerenciamento (= o macrogrupo rotulado “Gerenciamento Técnico e Administrativo”, "
        "“Canteiro”, “Canteiro e Indiretos”, “PCI”, “Administração da Obra” ou similar, "
        "conforme nomenclatura do xlsx de origem) como percentual do Total da Obra:"
    )

    tbl = newdoc.add_table(rows=7, cols=3)
    tbl.style = "Light Grid Accent 1"
    tbl.rows[0].cells[0].text = "Percentil"
    tbl.rows[0].cells[1].text = "% do Total de Obra"
    tbl.rows[0].cells[2].text = "R$/m² (n=39)"
    for cell in tbl.rows[0].cells:
        for run in cell.paragraphs[0].runs:
            run.bold = True
    labels = [
        ("P10 (mínimo razoável)", stats["pct_min"], None),
        ("P25", stats["pct_p25"], stats["rsm2_p25"]),
        ("Mediana (P50)", stats["pct_p50"], stats["rsm2_p50"]),
        ("P75", stats["pct_p75"], stats["rsm2_p75"]),
        ("P90", stats["pct_p90"], stats["rsm2_p90"]),
        ("Máximo", stats["pct_max"], None),
    ]
    for i, (lbl, v, r) in enumerate(labels, 1):
        tbl.rows[i].cells[0].text = lbl
        tbl.rows[i].cells[1].text = f"{v*100:.2f}%" if v else "—"
        tbl.rows[i].cells[2].text = f"R$ {r:,.0f}".replace(",", ".") if r else "—"

    newdoc.add_paragraph(
        f"Média: {stats['pct_mean']*100:.2f}%  |  R$/m² médio: "
        f"R$ {stats['rsm2_mean']:,.0f}".replace(",", ".")
    )

    # 0.3 Subconjunto similar
    newdoc.add_heading(
        f"0.3 Subconjunto similar ao Placon — AC 3.000–6.000 m² (n={stats['n_sim']})",
        level=2,
    )
    newdoc.add_paragraph(
        "Projetos com área construída entre 3.000 e 6.000 m² — o Placon tem 4.077 m². "
        "Essa faixa isola o efeito de escala (Gerenciamento é pouco variável em valor "
        "absoluto pra obra média, então o percentual cai à medida que a obra cresce)."
    )

    tbl = newdoc.add_table(rows=6, cols=3)
    tbl.style = "Light Grid Accent 1"
    tbl.rows[0].cells[0].text = "Percentil"
    tbl.rows[0].cells[1].text = "% do Total de Obra"
    tbl.rows[0].cells[2].text = "R$/m²"
    for cell in tbl.rows[0].cells:
        for run in cell.paragraphs[0].runs:
            run.bold = True
    sim_labels = [
        ("P25", stats["sim_pct_p25"], stats["sim_rsm2_p25"]),
        ("Mediana", stats["sim_pct_p50"], stats["sim_rsm2_p50"]),
        ("P75", stats["sim_pct_p75"], stats["sim_rsm2_p75"]),
        ("P90", stats["sim_pct_p90"], stats["sim_rsm2_p90"]),
        ("Máximo", stats["sim_pct_max"], stats["sim_rsm2_max"]),
    ]
    for i, (lbl, v, r) in enumerate(sim_labels, 1):
        tbl.rows[i].cells[0].text = lbl
        tbl.rows[i].cells[1].text = f"{v*100:.2f}%"
        tbl.rows[i].cells[2].text = f"R$ {r:,.0f}".replace(",", ".")

    # 0.4 Top 10
    newdoc.add_heading("0.4 Top 10 projetos mais próximos do Placon (por AC)", level=2)
    tbl = newdoc.add_table(rows=len(top10) + 1, cols=6)
    tbl.style = "Light Grid Accent 1"
    hdr = tbl.rows[0]
    for i, h in enumerate(["Cliente", "Projeto", "AC (m²)", "Ger (R$)", "% Ger", "Ger R$/m²"]):
        hdr.cells[i].text = h
        for run in hdr.cells[i].paragraphs[0].runs:
            run.bold = True
    for i, r in enumerate(top10, 1):
        ac = float(r["ac_m2"])
        ger = float(r["total_gerenciamento"])
        pct = float(r["pct_gerenciamento"])
        rsm2 = float(r["rsm2_gerenciamento"])
        tbl.rows[i].cells[0].text = r["cliente"][:18]
        tbl.rows[i].cells[1].text = r["projeto"][:24]
        tbl.rows[i].cells[2].text = f"{ac:,.0f}".replace(",", ".")
        tbl.rows[i].cells[3].text = f"{ger:,.0f}".replace(",", ".")
        tbl.rows[i].cells[4].text = f"{pct*100:.1f}%"
        tbl.rows[i].cells[5].text = f"{rsm2:,.0f}".replace(",", ".")

    # 0.5 Posição do Placon
    newdoc.add_heading("0.5 Posição real do Placon na distribuição", level=2)

    p = newdoc.add_paragraph()
    p.add_run("Placon Armínio Tavares: ").bold = True
    p.add_run(
        f"Gerenciamento R$ {PLACON_GER:,.0f} (R$ {PLACON_RSM2:,.0f}/m²) "
        f"= {PLACON_PCT*100:.1f}% do Grand Total R$ {PLACON_GT:,.0f} "
        f"(AC {PLACON_AC:,.0f} m²)".replace(",", ".")
    )

    tbl = newdoc.add_table(rows=5, cols=3)
    tbl.style = "Light Grid Accent 1"
    tbl.rows[0].cells[0].text = "Métrica"
    tbl.rows[0].cells[1].text = "Placon"
    tbl.rows[0].cells[2].text = "Percentil na base"
    for cell in tbl.rows[0].cells:
        for run in cell.paragraphs[0].runs:
            run.bold = True
    tbl.rows[1].cells[0].text = "% do Total — base global (n=47)"
    tbl.rows[1].cells[1].text = f"{PLACON_PCT*100:.1f}%"
    tbl.rows[1].cells[2].text = f"P{stats['placon_pctile_global']:.0f}"
    tbl.rows[2].cells[0].text = "% do Total — similar (AC 3-6k, n=10)"
    tbl.rows[2].cells[1].text = f"{PLACON_PCT*100:.1f}%"
    tbl.rows[2].cells[2].text = f"P{stats['placon_pctile_sim']:.0f}"
    tbl.rows[3].cells[0].text = "R$/m² — base global (n=39)"
    tbl.rows[3].cells[1].text = f"R$ {PLACON_RSM2:,.0f}".replace(",", ".")
    tbl.rows[3].cells[2].text = f"P{stats['placon_rsm2_pctile_global']:.0f}"
    tbl.rows[4].cells[0].text = "R$/m² — similar (n=10)"
    tbl.rows[4].cells[1].text = f"R$ {PLACON_RSM2:,.0f}".replace(",", ".")
    tbl.rows[4].cells[2].text = f"P{stats['placon_rsm2_pctile_sim']:.0f}"

    # 0.6 Veredicto
    newdoc.add_heading("0.6 Veredicto ampliado (dados de executivos reais)", level=2)

    newdoc.add_paragraph(
        f"O Placon está no percentil P{stats['placon_pctile_global']:.0f} global "
        f"e P{stats['placon_pctile_sim']:.0f} no subconjunto similar (AC 3-6k m²) "
        f"quando o gerenciamento é expresso como % do Total da Obra. "
        f"Em R$/m², o Placon está em P{stats['placon_rsm2_pctile_global']:.0f} "
        f"global e P{stats['placon_rsm2_pctile_sim']:.0f} no similar."
    )

    p = newdoc.add_paragraph()
    p.add_run("Em linguagem simples: ").bold = True
    p.add_run(
        f"o Gerenciamento do Placon, como está hoje (19,5%), é maior que "
        f"~{stats['placon_pctile_sim']:.0f}% dos projetos comparáveis que a Cartesian "
        f"já entregou. A mediana do subconjunto similar é "
        f"{stats['sim_pct_p50']*100:.1f}% (R$ {stats['sim_rsm2_p50']:,.0f}/m²), "
        f"e o P75 é {stats['sim_pct_p75']*100:.1f}% (R$ {stats['sim_rsm2_p75']:,.0f}/m²)."
        .replace(",", ".")
    )

    newdoc.add_paragraph(
        "Isso CONFIRMA a recomendação das Seções 4-5: o Placon está alto, e os 3 overrides "
        "propostos (taxas/seguros −R$ 100k, limpeza −R$ 30k, grua −R$ 180k condicional ao "
        "planejamento) levariam o Gerenciamento pra ~R$ 3,17M ou 17,7% — ainda acima da "
        f"mediana da base real ({stats['sim_pct_p50']*100:.1f}%), mas dentro do intervalo "
        "defensável pra obra de 18 pavimentos no centro de Florianópolis (região que costuma "
        "elevar taxas/habite-se/incorporação vs litoral)."
    )

    p = newdoc.add_paragraph()
    p.add_run("Recomendação mantida: ").bold = True
    p.add_run(
        "aplicar os 3 overrides já listados em 5.1. Não recomendamos descer abaixo de "
        "R$ 3,0M (P50 similar em R$/m² × AC) porque obra vertical em região central tem "
        "custos indiretos intrinsecamente maiores — cortar abaixo disso arrisca subestimar "
        "administração de canteiro e taxas municipais de Florianópolis."
    )

    # Separador antes do conteúdo original
    newdoc.add_paragraph()
    newdoc.add_paragraph("— — —").alignment = WD_ALIGN_PARAGRAPH.CENTER
    newdoc.add_paragraph()

    return newdoc


def merge_into_original(new_section_doc: Document, original_path: Path, output_path: Path):
    """Insere todo conteúdo de new_section_doc no início do original."""
    orig = Document(original_path)

    # Copia os elementos do body do new_section_doc pra o início do orig
    new_body = new_section_doc.element.body
    orig_body = orig.element.body

    # Remove sectPr do final do new_body (senão quebra layout)
    new_elems = [el for el in new_body if el.tag != qn("w:sectPr")]

    # Pega o primeiro elemento do orig (será o ponto de inserção)
    first_orig = orig_body[0]

    # Inserir na ordem correta: o primeiro elemento novo vem antes de first_orig,
    # e cada próximo vem antes do original também (então mantém ordem original)
    for el in new_elems:
        first_orig.addprevious(el)

    orig.save(output_path)


def main():
    if not CSV_PATH.exists():
        print(f"[ERRO] CSV não existe: {CSV_PATH}")
        sys.exit(1)

    data = load_data()
    print(f"[INFO] Carregadas {len(data)} linhas do CSV")

    # Backup
    backup = DOC_PATH.with_suffix(".bak.docx")
    if not backup.exists():
        shutil.copy(DOC_PATH, backup)
        print(f"[INFO] Backup: {backup}")

    new_doc = build_secao0_doc(data)
    # Salva intermediário pra debug
    tmp = DOC_PATH.with_name("_secao0_tmp.docx")
    new_doc.save(tmp)
    print(f"[INFO] Seção 0 intermediária: {tmp}")

    # Recarrega e mescla
    new_doc2 = Document(tmp)
    merge_into_original(new_doc2, DOC_PATH, DOC_PATH)
    print(f"[DONE] Arquivo atualizado: {DOC_PATH}")

    # Copiar pro Drive
    drive_out = Path(
        r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Parametrico_IA\arminio-tavares"
    )
    if drive_out.exists():
        dest = drive_out / "arminio-tavares-analise-gerenciamento-2026-04-22.docx"
        shutil.copy(DOC_PATH, dest)
        print(f"[DONE] Drive: {dest}")
    else:
        print(f"[WARN] Drive não acessível: {drive_out}")


if __name__ == "__main__":
    main()
