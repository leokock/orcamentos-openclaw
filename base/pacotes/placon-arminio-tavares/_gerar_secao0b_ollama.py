#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gera a SEÇÃO 0-B — Varredura com modelos locais (Gemma/Qwen) —
adicionando ao analise-gerenciamento-placon.docx.

Insere após a seção 0 (varredura heurística), antes da análise Placon.
"""
from __future__ import annotations

import csv
import io
import shutil
import sys
from pathlib import Path

import docx
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DOC_PATH = Path(r"C:\Users\leona\orcamentos-openclaw\base\pacotes\placon-arminio-tavares\analise-gerenciamento-placon.docx")
MERGED_CSV = Path(r"C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-merged-2026-04-22.csv")
PASS2_CSV = Path(r"C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-gemma-2026-04-22.csv")

PLACON_AC = 4077.29
PLACON_GER = 3483456
PLACON_GT = 17865738
PLACON_PCT = PLACON_GER / PLACON_GT * 100
PLACON_RSM2 = PLACON_GER / PLACON_AC


def f(v):
    if v is None or v == '':
        return None
    try:
        return float(v)
    except Exception:
        return None


def percentiles(vals, pcts=(25, 50, 75, 85, 90)):
    if not vals:
        return {p: None for p in pcts}
    sv = sorted(vals)
    out = {}
    for p in pcts:
        if len(sv) == 1:
            out[p] = sv[0]
            continue
        k = (len(sv) - 1) * p / 100
        lo = int(k); hi = min(lo + 1, len(sv) - 1)
        out[p] = sv[lo] + (sv[hi] - sv[lo]) * (k - lo)
    return out


def pct_rank(value, sv):
    if not sv:
        return None
    import bisect
    return bisect.bisect_left(sv, value) * 100 / len(sv)


def load_merged():
    rows = []
    with open(MERGED_CSV, encoding='utf-8') as fp:
        for r in csv.DictReader(fp):
            rows.append({
                'source': r['source'],
                'cliente': r['cliente'],
                'projeto': r['projeto'],
                'ger': f(r['ger']),
                'gt': f(r['gt']),
                'ac': f(r['ac']),
                'pct': f(r['pct']),
                'rsm2': f(r['rsm2']),
            })
    return rows


def load_pass2_stats():
    total = ok = rejeitado = 0
    if not PASS2_CSV.is_file():
        return total, ok, rejeitado
    with open(PASS2_CSV, encoding='utf-8') as fp:
        for r in csv.DictReader(fp):
            total += 1
            if r.get('status') == 'ok' and not r.get('suspeito'):
                ok += 1
            else:
                rejeitado += 1
    return total, ok, rejeitado


def set_cell_bg(cell, color_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = docx.oxml.OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    tc_pr.append(shd)


def build():
    rows = load_merged()
    pass2_total, pass2_ok, pass2_rej = load_pass2_stats()

    heur = [r for r in rows if r['source'] == 'heuristica']
    ollama = [r for r in rows if r['source'] == 'ollama']

    all_pcts = sorted([r['pct'] for r in rows if r['pct']])
    all_rsm2 = sorted([r['rsm2'] for r in rows if r['rsm2']])

    p_pct = percentiles(all_pcts)
    p_rsm2 = percentiles(all_rsm2)

    sub_ac = [r for r in rows if r['ac'] and 3000 <= r['ac'] <= 6000]
    p_pct_sub = percentiles([r['pct'] for r in sub_ac if r['pct']])
    p_rsm2_sub = percentiles([r['rsm2'] for r in sub_ac if r['rsm2']])

    placon_pct_rank = pct_rank(PLACON_PCT, all_pcts)
    placon_rsm2_rank = pct_rank(PLACON_RSM2, all_rsm2)

    # Backup
    backup = DOC_PATH.with_suffix('.bak2.docx')
    shutil.copy2(DOC_PATH, backup)
    print(f'Backup: {backup}')

    doc = Document(str(DOC_PATH))

    # Create a new tmp doc with just the section we want, then append to current
    # Strategy: append at end (user can move); simpler than mid-insertion

    h = doc.add_heading('SEÇÃO 0-B — Varredura com modelos locais (Gemma/Qwen)', level=1)

    doc.add_paragraph(
        f'Esta seção amplia a base comparativa da Seção 0 usando modelos locais '
        f'(Qwen 2.5 14B via Ollama) para ler planilhas que a heurística openpyxl '
        f'da primeira passada não conseguiu interpretar. Custo em tokens Claude: ZERO.'
    )

    doc.add_heading('Metodologia', level=2)
    doc.add_paragraph(
        f'Primeira passada (heurística openpyxl): extraiu {len(heur)} Grand Totals de 162 xlsx varridos '
        f'— conseguiu ler abas com padrão rígido de totalização.'
    )
    doc.add_paragraph(
        f'Segunda passada (Qwen 2.5 14B local): 30 xlsx candidatos processados '
        f'(dos 99 com abas promissoras identificadas), {pass2_ok} retornaram valores válidos, '
        f'{pass2_rej} foram rejeitados (extração ruidosa ou fora de range plausível).'
    )
    doc.add_paragraph(
        'Economia estimada: 30 planilhas × ~5k tokens de contexto = ~150k tokens de Opus 4.7 '
        'economizados (~R$ 12 em custo de API, com câmbio $1 = R$ 5,3). Tempo do pipeline '
        'local: ~20 minutos, CPU+GPU do Windows.'
    )

    doc.add_heading('Base combinada', level=2)
    doc.add_paragraph(
        f'TOTAL: {len(rows)} projetos = {len(heur)} heurística + {len(ollama)} Ollama'
    )

    # Tabela percentis
    doc.add_heading('Percentis atualizados — Gerenciamento', level=2)
    table = doc.add_table(rows=6, cols=3)
    table.style = 'Light Grid Accent 1'
    hdr = table.rows[0].cells
    hdr[0].text = 'Percentil'
    hdr[1].text = '% sobre total geral'
    hdr[2].text = 'R$/m²'
    for c in hdr:
        set_cell_bg(c, 'D9E1F2')
    for i, p in enumerate([25, 50, 75, 85, 90], start=1):
        row = table.rows[i].cells
        row[0].text = f'P{p}'
        row[1].text = f'{p_pct[p]:.2f}%' if p_pct.get(p) else '—'
        row[2].text = f'R$ {p_rsm2[p]:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') if p_rsm2.get(p) else '—'

    doc.add_heading(f'Subset AC 3.000-6.000 m² (similar Placon, n={len(sub_ac)})', level=2)
    if sub_ac:
        table2 = doc.add_table(rows=6, cols=3)
        table2.style = 'Light Grid Accent 1'
        hdr = table2.rows[0].cells
        hdr[0].text = 'Percentil'
        hdr[1].text = '% sobre total geral'
        hdr[2].text = 'R$/m²'
        for c in hdr:
            set_cell_bg(c, 'D9E1F2')
        for i, p in enumerate([25, 50, 75, 85, 90], start=1):
            row = table2.rows[i].cells
            row[0].text = f'P{p}'
            row[1].text = f'{p_pct_sub[p]:.2f}%' if p_pct_sub.get(p) else '—'
            row[2].text = f'R$ {p_rsm2_sub[p]:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') if p_rsm2_sub.get(p) else '—'

    doc.add_heading('Posição do Placon na base combinada', level=2)
    ac_fmt = f'{PLACON_AC:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    ger_fmt = f'{PLACON_GER:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    gt_fmt = f'{PLACON_GT:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    rsm2_fmt = f'{PLACON_RSM2:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    doc.add_paragraph(
        f'Placon: AC = {ac_fmt} m² | Gerenciamento = R$ {ger_fmt} | '
        f'Total = R$ {gt_fmt} | % = {PLACON_PCT:.2f}% | R$/m² = {rsm2_fmt}'
    )
    if placon_pct_rank is not None:
        doc.add_paragraph(f'Placon está em P{placon_pct_rank:.0f} de % Gerenciamento sobre total geral.')
    if placon_rsm2_rank is not None:
        doc.add_paragraph(f'Placon está em P{placon_rsm2_rank:.0f} de R$/m² de Gerenciamento.')

    # Top projetos da base Ollama
    doc.add_heading('Projetos adicionados pela segunda passada (Ollama)', level=2)
    if ollama:
        table3 = doc.add_table(rows=len(ollama) + 1, cols=5)
        table3.style = 'Light Grid Accent 1'
        hdr = table3.rows[0].cells
        hdr[0].text = 'Cliente'
        hdr[1].text = 'Projeto'
        hdr[2].text = 'AC (m²)'
        hdr[3].text = '% Ger'
        hdr[4].text = 'R$/m²'
        for c in hdr:
            set_cell_bg(c, 'D9E1F2')
        for i, r in enumerate(sorted(ollama, key=lambda x: -(x['pct'] or 0)), start=1):
            row = table3.rows[i].cells
            row[0].text = r['cliente'][:20]
            row[1].text = r['projeto'][:25]
            row[2].text = f'{r["ac"]:,.0f}'.replace(',', '.') if r['ac'] else '—'
            row[3].text = f'{r["pct"]:.2f}%' if r['pct'] else '—'
            row[4].text = f'R$ {r["rsm2"]:,.0f}'.replace(',', '.') if r['rsm2'] else '—'

    doc.add_heading('Recomendação atualizada', level=2)
    # Compare old position vs new
    doc.add_paragraph(
        f'Base anterior (análise original): mediana ~13,18% | P75 ~15,74%.'
    )
    doc.add_paragraph(
        f'Base combinada nova: mediana (P50) = {p_pct[50]:.2f}% | P75 = {p_pct[75]:.2f}% | P85 = {p_pct[85]:.2f}%.'
    )

    doc.save(str(DOC_PATH))
    print(f'Docx atualizado: {DOC_PATH}')

    return {
        'n_total': len(rows),
        'n_heur': len(heur),
        'n_ollama': len(ollama),
        'p_pct': p_pct,
        'p_rsm2': p_rsm2,
        'placon_pct_rank': placon_pct_rank,
        'placon_rsm2_rank': placon_rsm2_rank,
    }


if __name__ == '__main__':
    stats = build()
    print(f'\n=== STATS ===')
    for k, v in stats.items():
        print(f'  {k}: {v}')
