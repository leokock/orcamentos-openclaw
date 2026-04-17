#!/usr/bin/env python3
"""Phase 20c — Gera planilha de Análise de Produto Cartesian.

Lê indicadores-produto-agregados.json e gera Excel com 11 abas:
LEIA_ME, PROJETOS, CUSTO_POR_MG, ESTRUTURAL, ELETRICA, HIDRO,
ALVENARIA_REVEST, ESQUADRIAS_LOUCAS, DIVERSOS, MATRIZ_PROJETOS, BENCHMARKS

Uso:
    python scripts/gerar_planilha_analise_produto.py
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

BASE = Path.home() / "orcamentos-openclaw" / "base"
AGG_FILE = BASE / "indicadores-produto-agregados.json"
COND_FILE = BASE / "calibration-condicional-padrao.json"
OUT_XLSX = BASE / "analise-produto-cartesian.xlsx"

DARK = "2C3E50"
ACCENT = "2980B9"
ORANGE = "E67E22"
GREEN = "27AE60"
PURPLE = "8E44AD"
RED = "C0392B"
GRAY = "7F8C8D"
TEAL = "16A085"

THIN = Border(
    left=Side(style="thin", color="CCCCCC"),
    right=Side(style="thin", color="CCCCCC"),
    top=Side(style="thin", color="CCCCCC"),
    bottom=Side(style="thin", color="CCCCCC"),
)

GREEN_FILL = PatternFill(start_color="E8F8E0", end_color="E8F8E0", fill_type="solid")
YELLOW_FILL = PatternFill(start_color="FFF9E6", end_color="FFF9E6", fill_type="solid")
RED_FILL = PatternFill(start_color="FDECEC", end_color="FDECEC", fill_type="solid")

ABA_COLORS = {
    "LEIA_ME": GREEN,
    "PROJETOS": ACCENT,
    "CUSTO_POR_MG": ORANGE,
    "ESTRUTURAL": PURPLE,
    "ELETRICA": TEAL,
    "HIDRO": ACCENT,
    "ALVENARIA_REVEST": ORANGE,
    "ESQUADRIAS_LOUCAS": PURPLE,
    "DIVERSOS": GRAY,
    "MATRIZ_PROJETOS": RED,
    "BENCHMARKS": GREEN,
}

DISCIPLINE_TABS = {
    "ESTRUTURAL": {
        "title": "Indicadores Estruturais",
        "prefixes": ["concreto_", "aco_", "forma_", "escoramento_", "taxa_aco_"],
    },
    "ELETRICA": {
        "title": "Indicadores Elétricos",
        "prefixes": ["pontos_iluminacao_", "tomadas_", "quadros_eletricos_", "luminarias_", "eletroduto_", "pontos_eletricos_total_"],
    },
    "HIDRO": {
        "title": "Indicadores Hidrossanitários",
        "prefixes": ["pontos_agua_", "pontos_esgoto_", "tubulacao_total_", "registros_", "ralos_"],
    },
    "ALVENARIA_REVEST": {
        "title": "Alvenaria, Revestimentos e Pintura",
        "prefixes": ["alvenaria_", "blocos_", "chapisco_", "reboco_", "contrapiso_", "porcelanato_", "revestimento_fachada_", "pintura_"],
    },
    "ESQUADRIAS_LOUCAS": {
        "title": "Esquadrias e Louças/Metais",
        "prefixes": ["portas_", "janelas_", "vidros_", "guarda_corpo_", "bacias_", "lavatorios_", "cubas_", "chuveiros_"],
    },
    "DIVERSOS": {
        "title": "Diversos",
        "prefixes": ["forro_", "elevadores_", "hidrantes_", "sprinklers_", "cobertura_", "drywall_", "manta_", "cristalizacao_"],
    },
}


def _load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def style_header(cell, color=DARK):
    cell.font = Font(bold=True, color="FFFFFF", size=9, name="Arial")
    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = THIN


def style_subheader(cell, color=ACCENT):
    cell.font = Font(bold=True, color=color, size=10, name="Arial")
    cell.alignment = Alignment(horizontal="left", vertical="center")


def write_headers(ws, row, headers, widths, color=DARK):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row, i, h)
        style_header(c, color)
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def write_row(ws, row, values, number_formats=None):
    for i, v in enumerate(values, start=1):
        c = ws.cell(row, i, v)
        c.font = Font(size=9, name="Arial")
        c.border = THIN
        if number_formats and i in number_formats:
            c.number_format = number_formats[i]
        elif isinstance(v, float):
            c.number_format = "#,##0.00"
        elif isinstance(v, int):
            c.number_format = "#,##0"


def get_indicators_for_tab(all_names, prefixes):
    return [n for n in all_names if any(n.startswith(p) for p in prefixes)]


def build_leia_me(wb, data):
    ws = wb.create_sheet("LEIA_ME")
    ws.sheet_properties.tabColor = ABA_COLORS["LEIA_ME"]

    ws["A1"] = "ANÁLISE DE PRODUTO — Indicadores Quantitativos Cartesian"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:E1")

    ws["A2"] = f"Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} · {data['n_projetos_total']} projetos · {data['n_indicadores_unicos']} indicadores"
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:E2")

    ws["A4"] = "PARA QUE SERVE"
    ws["A4"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    ws["A5"] = ("Permite avaliar a qualidade do PRODUTO (empreendimento) comparando indicadores "
                "quantitativos (un/m, m/m, kg/m) contra benchmarks de projetos similares da base Cartesian. "
                "Exemplo: 'esse projeto tem 42 pontos de iluminacao por UR - e alto ou baixo pra alto padrao?'")
    ws.merge_cells("A5:E5")
    ws["A5"].alignment = Alignment(wrap_text=True, vertical="top")

    ws["A7"] = "LEGENDA DE CORES (conditional formatting)"
    ws["A7"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    legend = [
        ("Verde", "Dentro da faixa normal (p25-p75)", GREEN_FILL),
        ("Amarelo", "Atencao (p10-p25 ou p75-p90)", YELLOW_FILL),
        ("Vermelho", "Fora da faixa (<p10 ou >p90)", RED_FILL),
    ]
    for i, (label, desc, fill) in enumerate(legend, start=8):
        c = ws.cell(i, 1, label)
        c.fill = fill
        c.font = Font(size=9, name="Arial")
        ws.cell(i, 2, desc).font = Font(size=9, name="Arial")

    ws["A12"] = "MAPA DAS ABAS"
    ws["A12"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    write_headers(ws, 14, ["#", "Aba", "Descricao"], [4, 22, 60])
    abas = [
        ("1", "LEIA_ME", "Este guia"),
        ("2", "PROJETOS", f"{data['n_projetos_total']} projetos com padrao, AC, UR"),
        ("3", "CUSTO_POR_MG", "R$/m por macrogrupo x padrao (fonte: calibracao V2)"),
        ("4", "ESTRUTURAL", "Concreto, aco, forma, escoramento por m AC"),
        ("5", "ELETRICA", "Pontos, tomadas, luminarias, eletroduto por UR/m"),
        ("6", "HIDRO", "Pontos agua/esgoto, tubulacao, registros por UR/m"),
        ("7", "ALVENARIA_REVEST", "Alvenaria, revestimentos, pisos, pintura por m AC"),
        ("8", "ESQUADRIAS_LOUCAS", "Portas, janelas, vidros, loucas por UR/m"),
        ("9", "DIVERSOS", "Forro, impermeabilizacao, elevadores, cobertura"),
        ("10", "MATRIZ_PROJETOS", "Tabela cruzada: todos os projetos x todos os indicadores"),
        ("11", "BENCHMARKS", "Faixas verde/amarelo/vermelho por indicador por padrao"),
    ]
    for i, (num, aba, desc) in enumerate(abas, start=15):
        write_row(ws, i, [num, aba, desc])

    ws["A28"] = "SEGMENTACAO POR PADRAO"
    ws["A28"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    for i, pad in enumerate(data.get("padroes", []), start=29):
        n_pad = data.get("indicadores_por_padrao", {}).get(pad, {}).get("n_projetos", 0)
        flag = " (amostra pequena)" if n_pad < 10 else ""
        ws.cell(i, 1, f"- {pad}: {n_pad} projetos{flag}").font = Font(size=9, name="Arial")

    ws["A36"] = "LIMITACOES DESTA VERSAO (v1 - classificador local keyword-based)"
    ws["A36"].font = Font(bold=True, size=11, color=RED, name="Arial")
    limits = [
        "- Classificacao baseada em keywords locais (nao Gemma). Ver base/indicadores-produto/ pros JSONs originais.",
        "- Alguns indicadores sofrem overcount por duplicacao entre abas (CPU + Insumos + disciplina).",
        "  Suspeitos: portas/UR, janelas/UR, bacias/UR, ralos/UR - muitas vezes 10-30x o esperado.",
        "- Projetos com apenas abas de macrogrupo (sem itens detalhados) retornam 0 indicadores.",
        "- Indicadores estruturais (concreto, aco, taxa_aco) batem com calibracao V2 existente.",
        "- Proxima iteracao: refinamento de regras + passe Gemma seletivo para itens ambiguos.",
    ]
    for i, txt in enumerate(limits, start=37):
        c = ws.cell(i, 1, txt)
        c.font = Font(size=9, name="Arial")
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=5)
        c.alignment = Alignment(wrap_text=True, vertical="top")

    ws["A45"] = "COMO REGENERAR"
    ws["A45"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    cmds = [
        "python -X utf8 scripts/extrair_indicadores_produto.py      # extracao por projeto",
        "python -X utf8 scripts/agregar_indicadores_produto.py      # estatisticas cross-projeto",
        "python -X utf8 scripts/gerar_planilha_analise_produto.py   # este Excel",
    ]
    for i, cmd in enumerate(cmds, start=46):
        c = ws.cell(i, 1, cmd)
        c.font = Font(name="Consolas", size=9)
        c.fill = PatternFill(start_color="F5F5F5", end_color="F5F5F5", fill_type="solid")
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=5)

    ws.column_dimensions["A"].width = 15
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 50
    ws.column_dimensions["E"].width = 50


def build_projetos(wb, data):
    ws = wb.create_sheet("PROJETOS")
    ws.sheet_properties.tabColor = ABA_COLORS["PROJETOS"]

    headers = ["Projeto", "Padrao", "AC (m)", "UR", "N Indicadores"]
    widths = [30, 14, 14, 8, 16]
    write_headers(ws, 1, headers, widths)

    matrix = data.get("projeto_matrix", [])
    for i, p in enumerate(sorted(matrix, key=lambda x: (x.get("padrao", ""), -(x.get("ac_m2") or 0))), start=2):
        nf = {3: "#,##0.00", 4: "#,##0"}
        write_row(ws, i, [
            p["slug"],
            p.get("padrao", ""),
            p.get("ac_m2") or None,
            p.get("ur") or None,
            p.get("n_indicadores", 0),
        ], nf)

    ws.auto_filter.ref = f"A1:E{len(matrix) + 1}"
    ws.freeze_panes = "A2"


def build_custo_por_mg(wb, data):
    ws = wb.create_sheet("CUSTO_POR_MG")
    ws.sheet_properties.tabColor = ABA_COLORS["CUSTO_POR_MG"]

    cond = _load_json(COND_FILE)
    if not cond:
        ws["A1"] = "Dados de calibracao condicional nao encontrados"
        return

    headers = ["Padrao", "Macrogrupo", "n", "min", "p25", "mediana", "p75", "max", "CV"]
    widths = [14, 35, 6, 12, 12, 12, 12, 12, 8]
    write_headers(ws, 1, headers, widths)

    nf = {i: "#,##0.00" for i in range(4, 9)}
    nf[9] = "0.000"
    row = 2
    por_padrao = cond.get("por_padrao_mg", {})
    for padrao in sorted(por_padrao.keys()):
        mgs = por_padrao[padrao]
        if not isinstance(mgs, dict):
            continue
        for mg_name, s in sorted(mgs.items()):
            if not isinstance(s, dict):
                continue
            write_row(ws, row, [
                padrao, mg_name,
                s.get("n", 0),
                s.get("min"), s.get("p25"), s.get("mediana"),
                s.get("p75"), s.get("max"), s.get("cv"),
            ], nf)
            row += 1

    if row > 2:
        ws.auto_filter.ref = f"A1:I{row - 1}"
    ws.freeze_panes = "A2"


def build_discipline_tab(wb, tab_name, tab_config, data):
    ws = wb.create_sheet(tab_name)
    ws.sheet_properties.tabColor = ABA_COLORS.get(tab_name, GRAY)

    ind_names = get_indicators_for_tab(data.get("nomes_indicadores", []), tab_config["prefixes"])
    if not ind_names:
        ws["A1"] = "Nenhum indicador encontrado para esta disciplina"
        return

    ws["A1"] = tab_config["title"]
    ws["A1"].font = Font(bold=True, size=12, color=DARK, name="Arial")
    ws.merge_cells("A1:J1")

    headers = ["Indicador", "n", "min", "p10", "p25", "mediana", "p75", "p90", "max", "CV"]
    widths = [45, 6, 10, 10, 10, 12, 10, 10, 10, 8]
    nf_stats = {i: "#,##0.0000" for i in range(3, 10)}
    nf_stats[10] = "0.000"

    row = 3
    padroes = data.get("padroes", [])
    for padrao in padroes:
        style_subheader(ws.cell(row, 1, f"> {padrao.upper()}"), ACCENT)
        pad_data = data.get("indicadores_por_padrao", {}).get(padrao, {})
        n_proj = pad_data.get("n_projetos", 0)
        ws.cell(row, 2, f"({n_proj} projetos)").font = Font(italic=True, size=8, color="999999", name="Arial")
        row += 1
        write_headers(ws, row, headers, widths, ACCENT if padrao in ("alto", "medio-alto") else ORANGE)
        row += 1

        pad_indicators = pad_data.get("indicadores", {})
        any_rows = False
        for ind_name in ind_names:
            s = pad_indicators.get(ind_name)
            if not s:
                continue
            any_rows = True
            display_name = ind_name.replace("_por_", "/").replace("_m2_", " m2/").replace("_", " ")
            write_row(ws, row, [
                display_name,
                s.get("n", 0),
                s.get("min"), s.get("p10"), s.get("p25"),
                s.get("mediana"), s.get("p75"), s.get("p90"),
                s.get("max"), s.get("cv"),
            ], nf_stats)
            row += 1
        if not any_rows:
            ws.cell(row, 1, "(sem dados)").font = Font(italic=True, size=8, color="999999", name="Arial")
            row += 1
        row += 1

    row += 1
    style_subheader(ws.cell(row, 1, "> VALORES POR PROJETO"), DARK)
    row += 1

    proj_headers = ["Projeto", "Padrao", "AC (m)"] + [
        n.replace("_por_", "/").replace("_m2_", " m2/").replace("_", " ")[:30]
        for n in ind_names
    ]
    proj_widths = [28, 12, 12] + [14] * len(ind_names)
    write_headers(ws, row, proj_headers, proj_widths, DARK)
    row += 1

    nf_proj = {i: "#,##0.0000" for i in range(4, 4 + len(ind_names))}
    nf_proj[3] = "#,##0.00"

    matrix = data.get("projeto_matrix", [])
    first_data_row = row
    for p in sorted(matrix, key=lambda x: (x.get("padrao", ""), -(x.get("ac_m2") or 0))):
        vals = [p["slug"], p.get("padrao", ""), p.get("ac_m2")]
        for ind_name in ind_names:
            vals.append(p.get(ind_name))
        write_row(ws, row, vals, nf_proj)
        row += 1
    last_data_row = row - 1

    globais = data.get("indicadores_globais", {})
    for col_offset, ind_name in enumerate(ind_names):
        col_letter = get_column_letter(4 + col_offset)
        s = globais.get(ind_name)
        if not s:
            continue
        data_range = f"{col_letter}{first_data_row}:{col_letter}{last_data_row}"
        p25 = s.get("p25", 0)
        p75 = s.get("p75", 0)
        p10 = s.get("p10", 0)
        p90 = s.get("p90", 0)
        ws.conditional_formatting.add(data_range, CellIsRule(
            operator="between", formula=[str(p25), str(p75)], fill=GREEN_FILL))
        ws.conditional_formatting.add(data_range, CellIsRule(
            operator="lessThan", formula=[str(p10)], fill=RED_FILL))
        ws.conditional_formatting.add(data_range, CellIsRule(
            operator="greaterThan", formula=[str(p90)], fill=RED_FILL))

    ws.freeze_panes = "A3"


def build_matriz_projetos(wb, data):
    ws = wb.create_sheet("MATRIZ_PROJETOS")
    ws.sheet_properties.tabColor = ABA_COLORS["MATRIZ_PROJETOS"]

    all_names = data.get("nomes_indicadores", [])
    headers = ["Projeto", "Padrao", "AC (m)", "UR"] + [
        n.replace("_por_", "/").replace("_m2_", " m2/").replace("_", " ")[:25]
        for n in all_names
    ]
    widths = [28, 12, 12, 8] + [13] * len(all_names)
    write_headers(ws, 1, headers, widths)

    nf = {i: "#,##0.0000" for i in range(5, 5 + len(all_names))}
    nf[3] = "#,##0.00"
    nf[4] = "#,##0"

    matrix = data.get("projeto_matrix", [])
    for i, p in enumerate(sorted(matrix, key=lambda x: (x.get("padrao", ""), x["slug"])), start=2):
        vals = [p["slug"], p.get("padrao", ""), p.get("ac_m2"), p.get("ur")]
        for ind_name in all_names:
            vals.append(p.get(ind_name))
        write_row(ws, i, vals, nf)

    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(matrix) + 1}"
    ws.freeze_panes = "C2"


def build_benchmarks(wb, data):
    ws = wb.create_sheet("BENCHMARKS")
    ws.sheet_properties.tabColor = ABA_COLORS["BENCHMARKS"]

    ws["A1"] = "BENCHMARKS - Faixas de Referencia por Indicador e Padrao"
    ws["A1"].font = Font(bold=True, size=12, color=DARK, name="Arial")
    ws.merge_cells("A1:J1")

    headers = ["Indicador", "Padrao", "n", "< p10", "p10-p25", "p25-p75", "p75-p90", "> p90", "Mediana", "CV"]
    widths = [40, 14, 6, 12, 12, 16, 12, 12, 12, 8]
    write_headers(ws, 3, headers, widths)

    nf = {i: "#,##0.0000" for i in range(4, 10)}
    nf[10] = "0.000"

    row = 4
    all_names = data.get("nomes_indicadores", [])
    padroes = data.get("padroes", [])

    for ind_name in all_names:
        for padrao in padroes:
            s = data.get("indicadores_por_padrao", {}).get(padrao, {}).get("indicadores", {}).get(ind_name)
            if not s or s.get("n", 0) < 3:
                continue
            display_name = ind_name.replace("_por_", "/").replace("_m2_", " m2/").replace("_", " ")
            p10 = s.get("p10")
            p25 = s.get("p25")
            p75 = s.get("p75")
            p90 = s.get("p90")
            write_row(ws, row, [
                display_name, padrao, s["n"],
                p10, f"{p10}-{p25}",
                f"{p25}-{p75}",
                f"{p75}-{p90}",
                p90, s.get("mediana"), s.get("cv"),
            ], nf)
            row += 1

    if row > 4:
        ws.auto_filter.ref = f"A3:J{row - 1}"
    ws.freeze_panes = "A4"


def main():
    print("Loading aggregated indicators...", flush=True)
    data = _load_json(AGG_FILE)
    if not data:
        print(f"ERROR: {AGG_FILE} not found or empty", flush=True)
        return

    print(f"  {data['n_projetos_total']} projects, {data['n_indicadores_unicos']} indicators", flush=True)

    wb = Workbook()
    wb.remove(wb.active)

    print("Building tabs...", flush=True)
    build_leia_me(wb, data); print("  LEIA_ME OK", flush=True)
    build_projetos(wb, data); print("  PROJETOS OK", flush=True)
    build_custo_por_mg(wb, data); print("  CUSTO_POR_MG OK", flush=True)

    for tab_name, tab_config in DISCIPLINE_TABS.items():
        build_discipline_tab(wb, tab_name, tab_config, data)
        print(f"  {tab_name} OK", flush=True)

    build_matriz_projetos(wb, data); print("  MATRIZ_PROJETOS OK", flush=True)
    build_benchmarks(wb, data); print("  BENCHMARKS OK", flush=True)

    wb.save(str(OUT_XLSX))
    print(f"\nSalvo: {OUT_XLSX}", flush=True)


if __name__ == "__main__":
    main()
