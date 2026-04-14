#!/usr/bin/env python3
"""Gera catálogo único de todos os índices da base Cartesian.

Output: base/INDICES-CATALOGO.xlsx + base/INDICES-CATALOGO.md

10 abas no Excel:
1. LEIA_ME — mapa das abas
2. PROJETOS — 126 projetos com padrão Gemma
3. CALIBRACAO_GLOBAL — 18 MGs global
4. CALIBRACAO_CONDICIONAL — 18 MGs × 5 padrões Gemma
5. INDICES_DERIVADOS_V2 — 29 índices derivados
6. INDICES_ESTRUTURAIS — consumos físicos + segmentos + instalações + ci + produto
7. PUS_CROSS_V1 — 1.740 clusters com lista de projetos
8. PUS_CROSS_V2 — 4.210 clusters sem lista (mais cobertura)
9. CURVA_ABC_MASTER — 126 projetos (n itens, valor total)
10. CROSS_INSIGHTS_GEMMA — flatten dos insights Gemma

Uso:
    python scripts/gerar_catalogo_indices.py
"""
from __future__ import annotations

import glob
import json
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_XLSX = BASE / "INDICES-CATALOGO.xlsx"
OUT_MD = BASE / "INDICES-CATALOGO.md"

# Styles
DARK = "2C3E50"
ACCENT = "2980B9"
ORANGE = "E67E22"
GREEN = "27AE60"
PURPLE = "8E44AD"
RED = "C0392B"
GRAY = "7F8C8D"
GREEN_BG = "E8F5E9"
ORANGE_BG = "FFF3E0"

THIN = Border(
    left=Side(style="thin", color="CCCCCC"),
    right=Side(style="thin", color="CCCCCC"),
    top=Side(style="thin", color="CCCCCC"),
    bottom=Side(style="thin", color="CCCCCC"),
)

ABA_COLORS = {
    "LEIA_ME": GREEN,
    "PROJETOS": ACCENT,
    "CALIBRACAO_GLOBAL": ORANGE,
    "CALIBRACAO_CONDICIONAL": ORANGE,
    "INDICES_DERIVADOS_V2": PURPLE,
    "INDICES_ESTRUTURAIS": PURPLE,
    "PUS_CROSS_V1": RED,
    "PUS_CROSS_V2": RED,
    "CURVA_ABC_MASTER": GRAY,
    "CROSS_INSIGHTS_GEMMA": GRAY,
}


def _load_json(p: Path) -> dict | list:
    if not p.exists():
        print(f"  [warn] não existe: {p}")
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  [warn] falha lendo {p}: {e}")
        return {}


def load_sources() -> dict:
    print("Carregando fontes...")
    s = {
        "calibration": _load_json(BASE / "calibration-indices.json"),
        "condicional": _load_json(BASE / "calibration-condicional-padrao.json"),
        "master": _load_json(BASE / "base-indices-master-2026-04-13.json"),
        "pus_v1": _load_json(BASE / "base-pus-cartesian.json"),
        "pus_v2": _load_json(BASE / "itens-pus-agregados.json"),
        "padroes": _load_json(BASE / "padroes-classificados-consolidado.json"),
    }
    # Carregar indices-executivo dos 126
    exec_dir = BASE / "indices-executivo"
    idx_exec = {}
    if exec_dir.exists():
        for p in sorted(exec_dir.glob("*.json")):
            try:
                d = json.loads(p.read_text(encoding="utf-8"))
                idx_exec[p.stem] = d
            except Exception:
                pass
    s["indices_exec"] = idx_exec
    print(f"  calibration: {len(s['calibration'].get('por_macrogrupo', {}) if isinstance(s['calibration'], dict) else {})} MGs")
    print(f"  condicional: {len(s['condicional'].get('por_padrao_mg', {}) if isinstance(s['condicional'], dict) else {})} buckets de padrão")
    print(f"  derivados_v2: {len(s['master'].get('indices_derivados_v2', {}) if isinstance(s['master'], dict) else {})}")
    print(f"  pus_v1: {len(s['pus_v1']) if isinstance(s['pus_v1'], dict) else 0}")
    print(f"  pus_v2: {len(s['pus_v2'].get('pus_agregados', []) if isinstance(s['pus_v2'], dict) else [])}")
    print(f"  indices-executivo: {len(idx_exec)} projetos")
    print(f"  padroes_gemma: {len(s['padroes'].get('projetos', []) if isinstance(s['padroes'], dict) else [])} classificados")
    return s


def style_header(cell, color: str = DARK):
    cell.font = Font(bold=True, color="FFFFFF", size=9, name="Arial")
    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = THIN


def write_headers(ws, row: int, headers: list[str], widths: list[int]):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row, i, h)
        style_header(c)
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def write_row(ws, row: int, values: list, number_formats: dict[int, str] | None = None):
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


def _num(v):
    """Return value if numeric else None."""
    if isinstance(v, (int, float)):
        return v
    return None


def _round(v, n=4):
    return round(v, n) if isinstance(v, (int, float)) else None


# =============================================================================
# ABA 1: LEIA_ME
# =============================================================================

def build_aba_leia_me(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("LEIA_ME")
    ws.sheet_properties.tabColor = ABA_COLORS["LEIA_ME"]

    ws["A1"] = "CATÁLOGO DE ÍNDICES CARTESIAN — Base V2 consolidada"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:D1")

    ws["A2"] = f"Gerado em {datetime.now().isoformat(timespec='seconds')} via scripts/gerar_catalogo_indices.py"
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:D2")

    ws["A4"] = "PARA QUE SERVE"
    ws["A4"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    ws["A5"] = ("Catálogo navegável de TODOS os índices da base Cartesian. "
                "Use filtros e ordenação por coluna pra encontrar índices por categoria, "
                "faixa de valores, número de projetos que contribuem, etc.")
    ws.merge_cells("A5:D5")
    ws["A5"].alignment = Alignment(wrap_text=True, vertical="top")

    ws["A7"] = "MAPA DAS ABAS"
    ws["A7"].font = Font(bold=True, size=11, color=DARK, name="Arial")

    write_headers(ws, 9, ["#", "Aba", "N linhas", "Descrição", "Fonte"],
                  [4, 26, 10, 60, 40])

    n_projs = len(sources["indices_exec"])
    pm_count = len(sources["calibration"].get("por_macrogrupo", {})) if isinstance(sources["calibration"], dict) else 0
    cond = sources["condicional"] if isinstance(sources["condicional"], dict) else {}
    n_cond = sum(len(v) for v in (cond.get("por_padrao_mg", {}) or {}).values()) if cond else 0
    n_der = len(sources["master"].get("indices_derivados_v2", {})) if isinstance(sources["master"], dict) else 0
    n_pus_v1 = len(sources["pus_v1"]) if isinstance(sources["pus_v1"], dict) else 0
    n_pus_v2 = len(sources["pus_v2"].get("pus_agregados", [])) if isinstance(sources["pus_v2"], dict) else 0

    abas_info = [
        ("1", "LEIA_ME", 1, "Este mapa + schema + exemplos de uso", "-"),
        ("2", "PROJETOS", n_projs, "126 projetos da base com padrão Gemma, AC, UR, R$/m², cidade", "padroes-classificados + indices-executivo"),
        ("3", "CALIBRACAO_GLOBAL", pm_count, "18 macrogrupos globais (stats sem segmentação de padrão)", "calibration-indices.json"),
        ("4", "CALIBRACAO_CONDICIONAL", n_cond, "18 MGs × 5 padrões Gemma (economico/medio/medio-alto/alto/luxo) — fonte primária pós-fase 18b", "calibration-condicional-padrao.json"),
        ("5", "INDICES_DERIVADOS_V2", n_der, "29 índices derivados: PU insumos, custo por MG, splits MO/Material, curva ABC", "base-indices-master.json:indices_derivados_v2"),
        ("6", "INDICES_ESTRUTURAIS", 35, "Consumos físicos (concreto m³/m², aço kg/m³), produto, instalações %, ci %, segmentos por porte", "calibration-indices.json:{estruturais,produto,instalacoes,ci,por_segmento}"),
        ("7", "PUS_CROSS_V1", n_pus_v1, "1.740 clusters de PU cross-projeto COM lista de obras fonte (fase 10 v1)", "base-pus-cartesian.json"),
        ("8", "PUS_CROSS_V2", n_pus_v2, "4.210 clusters de PU cross-projeto (fase 10 v2 hash-based, SEM lista de obras)", "itens-pus-agregados.json"),
        ("9", "CURVA_ABC_MASTER", 126, "Curva ABC consolidada por projeto — n itens, itens A, valor total", "base-indices-master.json:curva_abc_master"),
        ("10", "CROSS_INSIGHTS_GEMMA", 0, "Insights Gemma cross-projeto: famílias, índices sugeridos, lacunas, outliers, padrões comuns", "base-indices-master.json:cross_insights"),
    ]
    for i, (num, aba, n, desc, fonte) in enumerate(abas_info, start=10):
        write_row(ws, i, [num, aba, n, desc, fonte])

    ws["A22"] = "SCHEMA DAS COLUNAS NUMÉRICAS"
    ws["A22"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    schema = [
        ("n", "Número de projetos ou observações que contribuíram pro cálculo"),
        ("min / max", "Valores extremos observados"),
        ("p10 / p25 / p75 / p90", "Percentis (p10 = 10% dos projetos abaixo desse valor)"),
        ("mediana", "Valor central (p50) — é o que usamos como 'valor típico'"),
        ("media", "Média aritmética — pode ser puxada por outliers, menos robusta que mediana"),
        ("cv", "Coeficiente de variação (desvio/média). <0.3 é confiável, >0.5 é volátil"),
        ("projetos_fonte", "[só PUS_CROSS_V1] lista de slugs das obras que bancam esse índice"),
    ]
    write_headers(ws, 24, ["Coluna", "Significado"], [20, 80])
    for i, (col, desc) in enumerate(schema, start=25):
        write_row(ws, i, [col, desc])

    ws["A33"] = "EXEMPLOS DE FILTROS ÚTEIS"
    ws["A33"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    exemplos = [
        ("PUs robustos de concreto", "Aba PUS_CROSS_V2 → filtro 'key' contém 'concreto' + 'n_projetos' ≥ 10 + 'cv' < 0.3"),
        ("Esquadrias alto vs luxo", "Aba CALIBRACAO_CONDICIONAL → filtro 'padrao' IN ('alto','luxo') + 'macrogrupo' = 'Esquadrias'"),
        ("Quais obras bancam porcelanato?", "Aba PUS_CROSS_V1 → filtro 'descricao' contém 'porcelanato' → coluna 'projetos_fonte'"),
        ("Projetos alto padrão", "Aba PROJETOS → filtro 'padrao_gemma' = 'alto' → ordenar por 'rsm2' desc"),
        ("Índices derivados mais confiáveis", "Aba INDICES_DERIVADOS_V2 → ordenar 'n' desc → ignorar entries com n<5"),
        ("MGs com mais desvio por padrão", "Aba CALIBRACAO_CONDICIONAL → calcular coluna p90-p10 → ordenar desc"),
    ]
    write_headers(ws, 35, ["Pergunta", "Como responder"], [35, 75])
    for i, (q, r) in enumerate(exemplos, start=36):
        write_row(ws, i, [q, r])

    ws["A44"] = "GAPS CONHECIDOS"
    ws["A44"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    gaps = [
        "PUS_CROSS_V2 (4.210 clusters) NÃO tem lista de projetos — use PUS_CROSS_V1 (1.740) quando precisar rastrear obras",
        "Alguns MGs em CALIBRACAO_CONDICIONAL têm n<3 pro bucket — script paramétrico cai no fallback global × PADRAO_MULTIPLIERS",
        "custo_por_ur nos derivados tem apenas n=2 — baixa confiança",
        "Classe 'luxo' em CALIBRACAO_CONDICIONAL tem 0 projetos (Gemma não encontrou luxo na base Cartesian)",
        "Campos disciplinas/indices_consumo/split_mo_material dentro de cada indices-executivo/*.json estão majoritariamente vazios — dados agregados estão nos arquivos calibration*",
    ]
    for i, g in enumerate(gaps, start=45):
        ws.cell(i, 1, f"• {g}").font = Font(size=9, name="Arial")
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=5)

    ws["A52"] = "COMO REGENERAR ESTE CATÁLOGO"
    ws["A52"].font = Font(bold=True, size=11, color=DARK, name="Arial")
    ws["A53"] = "cd ~/orcamentos-openclaw && python scripts/gerar_catalogo_indices.py"
    ws["A53"].font = Font(name="Consolas", size=9)
    ws["A53"].fill = PatternFill(start_color="F5F5F5", end_color="F5F5F5", fill_type="solid")


# =============================================================================
# ABA 2: PROJETOS
# =============================================================================

def build_aba_projetos(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("PROJETOS")
    ws.sheet_properties.tabColor = ABA_COLORS["PROJETOS"]

    ws["A1"] = "PROJETOS DA BASE CARTESIAN (126 executivos)"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:K1")
    ws["A2"] = "Labels Gemma via fase 18 classificação semântica | AC/total via indices-executivo"
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:K2")

    headers = ["slug", "padrao_gemma", "confianca", "ac_m2", "ur", "total_rs",
               "rsm2", "m2_por_ur", "rs_por_ur", "cidade", "fonte"]
    widths = [36, 14, 11, 12, 8, 16, 12, 12, 14, 18, 28]
    write_headers(ws, 4, headers, widths)

    # Cross-ref: padroes consolidado + indices-executivo
    padroes_dict = {}
    cons = sources["padroes"] if isinstance(sources["padroes"], dict) else {}
    for p in cons.get("projetos", []):
        padroes_dict[p["projeto"]] = p

    rows = []
    for slug, idx in sorted(sources["indices_exec"].items()):
        padrao_entry = padroes_dict.get(slug, {})
        ac = idx.get("ac") or padrao_entry.get("ac") or 0
        ur = idx.get("ur") or padrao_entry.get("ur") or 0
        total = idx.get("total") or padrao_entry.get("total") or 0
        rsm2 = (total / ac) if ac and total else 0
        m2_por_ur = (ac / ur) if ac and ur else 0
        rs_por_ur = (total / ur) if total and ur else 0
        rows.append((
            slug,
            padrao_entry.get("padrao", "—"),
            padrao_entry.get("confianca", "—"),
            round(ac, 2) if ac else 0,
            int(ur) if ur else 0,
            round(total, 0) if total else 0,
            round(rsm2, 2) if rsm2 else 0,
            round(m2_por_ur, 2) if m2_por_ur else 0,
            round(rs_por_ur, 0) if rs_por_ur else 0,
            idx.get("cidade", "") or padrao_entry.get("cidade", ""),
            padrao_entry.get("metodo", "gemma_semantico"),
        ))

    fmts = {4: '#,##0.00', 5: '#,##0', 6: '"R$" #,##0', 7: '"R$" #,##0.00',
            8: '#,##0.0', 9: '"R$" #,##0'}
    for i, row in enumerate(rows, start=5):
        write_row(ws, i, list(row), number_formats=fmts)

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 3: CALIBRACAO_GLOBAL
# =============================================================================

def build_aba_calibracao_global(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("CALIBRACAO_GLOBAL")
    ws.sheet_properties.tabColor = ABA_COLORS["CALIBRACAO_GLOBAL"]

    ws["A1"] = "CALIBRAÇÃO GLOBAL — 18 macrogrupos (sem segmentação de padrão)"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:L1")
    ws["A2"] = "Stats agregadas de todos os 126 projetos da base. Para calibração condicional por padrão, ver aba CALIBRACAO_CONDICIONAL."
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:L2")

    headers = ["macrogrupo", "n", "min", "p10", "p25", "mediana", "media",
               "p75", "p90", "max", "unidade", "fonte"]
    widths = [24, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 32]
    write_headers(ws, 4, headers, widths)

    cal = sources["calibration"] if isinstance(sources["calibration"], dict) else {}
    pm = cal.get("por_macrogrupo", {}) or {}

    # Mapeamento key do JSON -> nome limpo
    MG_NAME_MAP = {
        "Gerenciamento_rsm2": "Gerenciamento",
        "Mov.Terra_rsm2": "Movimentação de Terra",
        "Infraestrutura_rsm2": "Infraestrutura",
        "Supraestrutura_rsm2": "Supraestrutura",
        "Alvenaria_rsm2": "Alvenaria",
        "Impermeabilização_rsm2": "Impermeabilização",
        "Instalações_rsm2": "Instalações",
        "Sist.Especiais_rsm2": "Sistemas Especiais",
        "Climatização_rsm2": "Climatização",
        "Rev.Int.Parede_rsm2": "Rev. Interno Parede",
        "Teto_rsm2": "Teto",
        "Pisos_rsm2": "Pisos",
        "Pintura_rsm2": "Pintura",
        "Esquadrias_rsm2": "Esquadrias",
        "Louças_rsm2": "Louças e Metais",
        "Fachada_rsm2": "Fachada",
        "Complementares_rsm2": "Complementares",
        "Imprevistos_rsm2": "Imprevistos",
    }

    fmts = {i: '"R$" #,##0.00' for i in [3, 4, 5, 6, 7, 8, 9, 10]}
    fmts[2] = '#,##0'

    row_idx = 5
    for key, nome in MG_NAME_MAP.items():
        stats = pm.get(key)
        if not isinstance(stats, dict):
            continue
        write_row(ws, row_idx, [
            nome,
            int(stats.get("n", 0)),
            _round(stats.get("min"), 2),
            _round(stats.get("p10"), 2),
            _round(stats.get("p25"), 2),
            _round(stats.get("mediana"), 2),
            _round(stats.get("media"), 2),
            _round(stats.get("p75"), 2),
            _round(stats.get("p90"), 2),
            _round(stats.get("max"), 2),
            "R$/m²",
            "calibration-indices.json",
        ], number_formats=fmts)
        row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 4: CALIBRACAO_CONDICIONAL
# =============================================================================

def build_aba_calibracao_condicional(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("CALIBRACAO_CONDICIONAL")
    ws.sheet_properties.tabColor = ABA_COLORS["CALIBRACAO_CONDICIONAL"]

    ws["A1"] = "CALIBRAÇÃO CONDICIONAL POR PADRÃO GEMMA (Fase 18b)"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:M1")
    ws["A2"] = "Medianas por macrogrupo condicionadas à classe Gemma (economico/medio/medio-alto/alto/luxo). Fonte primária da calibração pós-fase 18b."
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:M2")

    headers = ["padrao", "macrogrupo", "n", "min", "p10", "p25", "mediana",
               "media", "p75", "p90", "max", "unidade", "fonte"]
    widths = [14, 24, 6, 12, 12, 12, 12, 12, 12, 12, 12, 10, 28]
    write_headers(ws, 4, headers, widths)

    cond = sources["condicional"] if isinstance(sources["condicional"], dict) else {}
    por_padrao = cond.get("por_padrao_mg", {}) or {}

    PADROES_ORDEM = ["economico", "medio", "medio-alto", "alto", "luxo"]
    fmts = {i: '"R$" #,##0.00' for i in [4, 5, 6, 7, 8, 9, 10, 11]}
    fmts[3] = '#,##0'

    row_idx = 5
    for padrao in PADROES_ORDEM:
        mgs = por_padrao.get(padrao, {})
        for mg in sorted(mgs.keys()):
            stats = mgs.get(mg)
            if not isinstance(stats, dict):
                continue
            write_row(ws, row_idx, [
                padrao,
                mg,
                int(stats.get("n", 0)),
                _round(stats.get("min"), 2),
                _round(stats.get("p10"), 2),
                _round(stats.get("p25"), 2),
                _round(stats.get("mediana"), 2),
                _round(stats.get("media"), 2),
                _round(stats.get("p75"), 2),
                _round(stats.get("p90"), 2),
                _round(stats.get("max"), 2),
                "R$/m²",
                "calibration-condicional-padrao.json",
            ], number_formats=fmts)
            row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 5: INDICES_DERIVADOS_V2
# =============================================================================

def build_aba_derivados(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("INDICES_DERIVADOS_V2")
    ws.sheet_properties.tabColor = ABA_COLORS["INDICES_DERIVADOS_V2"]

    ws["A1"] = "29 ÍNDICES DERIVADOS V2 — PUs de insumos, custos por MG, splits"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:N1")
    ws["A2"] = "Derivados pelo script gerar_novos_indices.py cruzando base-pus-cartesian.json com indices-executivo/*.json"
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:N2")

    headers = ["nome", "descricao", "n", "min", "p10", "p25", "mediana",
               "media", "p75", "p90", "max", "cv", "unidade", "fonte"]
    widths = [32, 50, 6, 12, 12, 12, 12, 12, 12, 12, 12, 8, 10, 28]
    write_headers(ws, 4, headers, widths)

    master = sources["master"] if isinstance(sources["master"], dict) else {}
    der = master.get("indices_derivados_v2", {}) or {}

    # Inferir unidade pelo nome
    def _infer_unit(nome: str) -> str:
        n = nome.lower()
        if "rsm2" in n or "_por_m2" in n: return "R$/m²"
        if "_por_ur" in n: return "R$/UR"
        if "por_aco" in n or "por_concreto" in n: return "ratio"
        if "pu_" in n and "mediano" in n:
            if "kg" in n or "aco" in n: return "R$/kg"
            if "_m3" in n or "concreto" in n: return "R$/m³"
            if "_m2" in n or "impermeab" in n or "porcelanato" in n or "bloco" in n or "forma" in n or "pintura" in n: return "R$/m²"
            return "R$/un"
        if "_pct" in n: return "%"
        return "—"

    fmts = {3: '#,##0'}
    for i in [4, 5, 6, 7, 8, 9, 10, 11]:
        fmts[i] = '#,##0.0000'
    fmts[12] = '0.000'

    row_idx = 5
    for nome, stats in der.items():
        if not isinstance(stats, dict):
            continue
        desc = stats.get("descricao", nome)
        unit = _infer_unit(nome)
        write_row(ws, row_idx, [
            nome,
            desc,
            int(stats.get("n", 0)),
            _round(stats.get("min"), 4),
            _round(stats.get("p10"), 4),
            _round(stats.get("p25"), 4),
            _round(stats.get("mediana"), 4),
            _round(stats.get("media"), 4),
            _round(stats.get("p75"), 4),
            _round(stats.get("p90"), 4),
            _round(stats.get("max"), 4),
            _round(stats.get("cv"), 3),
            unit,
            "base-indices-master-2026-04-13.json",
        ], number_formats=fmts)
        row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 6: INDICES_ESTRUTURAIS
# =============================================================================

def build_aba_estruturais(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("INDICES_ESTRUTURAIS")
    ws.sheet_properties.tabColor = ABA_COLORS["INDICES_ESTRUTURAIS"]

    ws["A1"] = "ÍNDICES ESTRUTURAIS / PRODUTO / INSTALAÇÕES / CI / SEGMENTOS"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:N1")
    ws["A2"] = "Consumos físicos (concreto m³/m², aço kg/m³), índices de produto (AC/UR), breakdown de instalações e CI, e segmentação por porte"
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:N2")

    headers = ["categoria", "nome", "n", "min", "p10", "p25", "mediana",
               "media", "p75", "p90", "max", "unidade", "fonte"]
    widths = [16, 36, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 28]
    write_headers(ws, 4, headers, widths)

    cal = sources["calibration"] if isinstance(sources["calibration"], dict) else {}

    # Categorias (ordem) + key no JSON + unidade
    SECOES = [
        ("Estruturais", "estruturais", {
            "concreto_m3_por_m2_ac": "m³/m²",
            "aco_kg_por_m3_concreto": "kg/m³",
            "aco_kg_por_m2_ac": "kg/m²",
            "forma_m2_por_m2_ac": "m²/m²",
        }),
        ("Produto", "produto", {
            "ac_por_ur": "m²/UR",
            "custo_por_ur": "R$/UR",
            "cub_ratio": "ratio",
            "burn_rate_mensal": "R$/mês",
            "elevador_pu_un": "R$/un",
        }),
        ("Instalações %", "instalacoes", {
            "hidrossanitarias_pct_total": "%",
            "eletricas_pct_total": "%",
            "preventivas_pct_total": "%",
            "gas_pct_total": "%",
            "telecom_pct_total": "%",
        }),
        ("Custos Indiretos %", "ci", {
            "projetos_consultorias_pct_total": "%",
            "taxas_licencas_pct_total": "%",
            "equipe_adm_pct_total": "%",
            "epcs_pct_total": "%",
            "equipamentos_carga_pct_total": "%",
            "ensaios_pct_total": "%",
            "canteiro_pct_total": "%",
        }),
        ("Segmento por porte", "por_segmento", {
            "pequeno_lt8k_rsm2": "R$/m²",
            "medio_8k_15k_rsm2": "R$/m²",
            "grande_15k_25k_rsm2": "R$/m²",
            "extra_gt25k_rsm2": "R$/m²",
        }),
    ]

    fmts = {3: '#,##0'}
    for i in [4, 5, 6, 7, 8, 9, 10, 11]:
        fmts[i] = '#,##0.0000'

    row_idx = 5
    for categoria, secao_key, nomes_unids in SECOES:
        secao = cal.get(secao_key, {}) or {}
        for nome, unidade in nomes_unids.items():
            stats = secao.get(nome)
            if not isinstance(stats, dict):
                continue
            write_row(ws, row_idx, [
                categoria,
                nome,
                int(stats.get("n", 0)),
                _round(stats.get("min"), 4),
                _round(stats.get("p10"), 4),
                _round(stats.get("p25"), 4),
                _round(stats.get("mediana"), 4),
                _round(stats.get("media"), 4),
                _round(stats.get("p75"), 4),
                _round(stats.get("p90"), 4),
                _round(stats.get("max"), 4),
                unidade,
                "calibration-indices.json",
            ], number_formats=fmts)
            row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 7: PUS_CROSS_V1 (com projetos fonte)
# =============================================================================

def build_aba_pus_v1(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("PUS_CROSS_V1")
    ws.sheet_properties.tabColor = ABA_COLORS["PUS_CROSS_V1"]

    ws["A1"] = "PUs CROSS-PROJETO V1 — 1.740 clusters COM lista de obras fonte"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:M1")
    ws["A2"] = "Fase 10 v1. Cada cluster tem lista de slugs das obras que contribuíram (coluna 'projetos_fonte')."
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:M2")

    headers = ["categoria", "chave", "descricao", "unidade", "n_proj",
               "n_obs", "min", "p25", "mediana", "p75", "max", "cv", "projetos_fonte"]
    widths = [22, 36, 50, 8, 7, 7, 10, 10, 10, 10, 10, 8, 70]
    write_headers(ws, 4, headers, widths)

    pus_v1 = sources["pus_v1"] if isinstance(sources["pus_v1"], dict) else {}

    fmts = {i: '"R$" #,##0.00' for i in [7, 8, 9, 10, 11]}
    fmts[5] = '#,##0'
    fmts[6] = '#,##0'
    fmts[12] = '0.000'

    # Ordenar por categoria depois chave pra ficar navegável
    items = []
    for key, cluster in pus_v1.items():
        if not isinstance(cluster, dict):
            continue
        items.append((cluster.get("categoria", ""), key, cluster))
    items.sort(key=lambda x: (x[0], x[1]))

    row_idx = 5
    for categoria, _key, cluster in items:
        projs = cluster.get("projetos", []) or []
        projs_str = "; ".join(projs[:20])  # Truncate to first 20 to avoid cell overflow
        if len(projs) > 20:
            projs_str += f"  …(+{len(projs) - 20})"
        if len(projs_str) > 500:
            projs_str = projs_str[:497] + "..."

        write_row(ws, row_idx, [
            categoria,
            cluster.get("chave", ""),
            (cluster.get("descricao", "") or "")[:200],
            cluster.get("unidade", ""),
            int(cluster.get("n_projetos", 0)),
            int(cluster.get("n_observacoes", 0)),
            _round(cluster.get("min"), 2),
            _round(cluster.get("p25"), 2),
            _round(cluster.get("mediana"), 2),
            _round(cluster.get("p75"), 2),
            _round(cluster.get("max"), 2),
            _round(cluster.get("cv"), 3),
            projs_str,
        ], number_formats=fmts)
        row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 8: PUS_CROSS_V2 (mais clusters, sem projetos)
# =============================================================================

def build_aba_pus_v2(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("PUS_CROSS_V2")
    ws.sheet_properties.tabColor = ABA_COLORS["PUS_CROSS_V2"]

    ws["A1"] = "PUs CROSS-PROJETO V2 — 4.210 clusters (fase 10 v2)"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:O1")
    ws["A2"] = "Fase 10 v2 com hash-based clustering semântico. MAIS clusters que V1 (melhor cobertura), SEM lista de projetos."
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:O2")

    headers = ["cluster_id", "key (tokens)", "descricao", "unidades", "n_proj", "n_obs",
               "pu_min", "pu_p10", "pu_p25", "pu_mediana", "pu_p75", "pu_p90", "pu_max", "pu_media", "cv"]
    widths = [9, 38, 50, 12, 7, 7, 10, 10, 10, 11, 10, 10, 10, 10, 8]
    write_headers(ws, 4, headers, widths)

    pus_v2 = sources["pus_v2"] if isinstance(sources["pus_v2"], dict) else {}
    agregados = pus_v2.get("pus_agregados", []) or []

    fmts = {i: '"R$" #,##0.00' for i in [7, 8, 9, 10, 11, 12, 13, 14]}
    fmts[5] = '#,##0'
    fmts[6] = '#,##0'
    fmts[15] = '0.000'

    # Ordenar por n_projetos desc (robustez) depois cluster_id
    items = sorted(agregados, key=lambda c: (-c.get("n_projetos", 0), c.get("cluster_id", 0)))

    row_idx = 5
    for cluster in items:
        unidades = cluster.get("unidades") or []
        un_str = ",".join(unidades[:3]) if isinstance(unidades, list) else str(unidades)
        write_row(ws, row_idx, [
            int(cluster.get("cluster_id", 0)),
            cluster.get("key", ""),
            (cluster.get("desc", "") or "")[:200],
            un_str[:20],
            int(cluster.get("n_projetos", 0)),
            int(cluster.get("n_observacoes", 0)),
            _round(cluster.get("pu_min"), 2),
            _round(cluster.get("pu_p10"), 2),
            _round(cluster.get("pu_p25"), 2),
            _round(cluster.get("pu_mediana"), 2),
            _round(cluster.get("pu_p75"), 2),
            _round(cluster.get("pu_p90"), 2),
            _round(cluster.get("pu_max"), 2),
            _round(cluster.get("pu_media"), 2),
            _round(cluster.get("cv"), 3),
        ], number_formats=fmts)
        row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 9: CURVA_ABC_MASTER
# =============================================================================

def build_aba_curva_abc(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("CURVA_ABC_MASTER")
    ws.sheet_properties.tabColor = ABA_COLORS["CURVA_ABC_MASTER"]

    ws["A1"] = "CURVA ABC MASTER — 126 projetos consolidados"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:F1")

    master = sources["master"] if isinstance(sources["master"], dict) else {}
    cabc = master.get("curva_abc_master", {}) if isinstance(master, dict) else {}
    n_projs = cabc.get("n_projetos", 0)
    n_itens_totais = cabc.get("n_itens_totais", 0)

    ws["A2"] = (f"{n_projs} projetos × {n_itens_totais:,} itens. "
                f"'n_a' = quantos itens representam 80% do custo. Curva A compacta = projeto concentrado em poucos itens.")
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:F2")

    headers = ["slug", "status", "n_itens", "n_a", "pct_a", "valor_total_rs"]
    widths = [38, 10, 10, 10, 10, 18]
    write_headers(ws, 4, headers, widths)

    projs = cabc.get("projetos", []) or []

    fmts = {3: '#,##0', 4: '#,##0', 5: '0.0%', 6: '"R$" #,##0'}

    for i, p in enumerate(sorted(projs, key=lambda x: x.get("slug", "")), start=5):
        n_it = p.get("n_itens", 0) or 0
        n_a = p.get("n_a", 0) or 0
        pct_a = (n_a / n_it) if n_it else 0
        write_row(ws, i, [
            p.get("slug", ""),
            p.get("status", ""),
            int(n_it),
            int(n_a),
            pct_a,
            round(p.get("valor_total", 0) or 0, 0),
        ], number_formats=fmts)

    ws.freeze_panes = "A5"


# =============================================================================
# ABA 10: CROSS_INSIGHTS_GEMMA
# =============================================================================

def build_aba_cross_insights(wb: Workbook, sources: dict) -> None:
    ws = wb.create_sheet("CROSS_INSIGHTS_GEMMA")
    ws.sheet_properties.tabColor = ABA_COLORS["CROSS_INSIGHTS_GEMMA"]

    ws["A1"] = "CROSS INSIGHTS GEMMA — análises cross-projeto"
    ws["A1"].font = Font(bold=True, size=14, color=DARK, name="Arial")
    ws.merge_cells("A1:D1")
    ws["A2"] = "Gerados via Gemma analisando todos os projetos da base. Cada seção extrai um aspecto diferente."
    ws["A2"].font = Font(italic=True, size=9, color="666666", name="Arial")
    ws.merge_cells("A2:D2")

    headers = ["secao", "tipo", "campo", "conteudo"]
    widths = [22, 14, 22, 100]
    write_headers(ws, 4, headers, widths)

    master = sources["master"] if isinstance(sources["master"], dict) else {}
    cross = master.get("cross_insights", {}) or {}

    row_idx = 5
    for secao_nome, secao_data in cross.items():
        if not isinstance(secao_data, dict):
            continue
        parsed = secao_data.get("parsed", {})
        if not isinstance(parsed, dict):
            parsed = {}

        # parsed tem tipicamente 1 key que é uma lista de items
        for key, value in parsed.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        for subk, subv in item.items():
                            write_row(ws, row_idx, [
                                secao_nome,
                                key,
                                subk,
                                str(subv)[:300],
                            ])
                            row_idx += 1
                    else:
                        write_row(ws, row_idx, [secao_nome, key, "", str(item)[:300]])
                        row_idx += 1
            elif isinstance(value, dict):
                for subk, subv in value.items():
                    write_row(ws, row_idx, [secao_nome, key, subk, str(subv)[:300]])
                    row_idx += 1
            else:
                write_row(ws, row_idx, [secao_nome, key, "", str(value)[:300]])
                row_idx += 1

    ws.freeze_panes = "A5"


# =============================================================================
# MD MAPA
# =============================================================================

def write_md_mapa(sources: dict) -> None:
    n_projs = len(sources["indices_exec"])
    pm = sources["calibration"].get("por_macrogrupo", {}) if isinstance(sources["calibration"], dict) else {}
    pm_count = len(pm)
    cond = sources["condicional"] if isinstance(sources["condicional"], dict) else {}
    n_cond = sum(len(v) for v in (cond.get("por_padrao_mg", {}) or {}).values()) if cond else 0
    n_der = len(sources["master"].get("indices_derivados_v2", {}) if isinstance(sources["master"], dict) else {})
    n_pus_v1 = len(sources["pus_v1"]) if isinstance(sources["pus_v1"], dict) else 0
    n_pus_v2 = len(sources["pus_v2"].get("pus_agregados", []) if isinstance(sources["pus_v2"], dict) else [])

    md = f"""# Catálogo de Índices Cartesian

_Gerado em {datetime.now().isoformat(timespec='seconds')} via `scripts/gerar_catalogo_indices.py`_

## O que é

Catálogo navegável de **todos os índices** da base Cartesian V2 (pós-fase 19). Consolida em um único arquivo Excel o que estava espalhado em 5+ JSONs. Permite filtrar, ordenar e cross-referenciar índices por categoria, robustez estatística (n_projetos, cv) e faixa de valores.

**Planilha:** [INDICES-CATALOGO.xlsx](INDICES-CATALOGO.xlsx) — {OUT_XLSX.stat().st_size // 1024 if OUT_XLSX.exists() else '?'} KB, 10 abas

## Mapa das 10 abas

| # | Aba | N linhas | Fonte primária | Descrição |
|---|---|---|---|---|
| 1 | LEIA_ME | 1 | — | Este mapa + schema + exemplos de filtros |
| 2 | PROJETOS | {n_projs} | padroes-classificados + indices-executivo | 126 projetos com padrão Gemma, AC, UR, R$/m² |
| 3 | CALIBRACAO_GLOBAL | {pm_count} | calibration-indices.json | 18 macrogrupos global (sem segmentação de padrão) |
| 4 | CALIBRACAO_CONDICIONAL | {n_cond} | calibration-condicional-padrao.json | 18 MGs × 5 padrões Gemma (economico→luxo) — fonte primária fase 18b |
| 5 | INDICES_DERIVADOS_V2 | {n_der} | base-indices-master.json:indices_derivados_v2 | 29 derivados: PU insumos, custo por MG, splits MO/Material |
| 6 | INDICES_ESTRUTURAIS | ~35 | calibration-indices.json | Consumos físicos (concreto, aço, fôrma), produto, instalações %, CI %, segmentos por porte |
| 7 | **PUS_CROSS_V1** | **{n_pus_v1}** | base-pus-cartesian.json | **1.740 clusters COM lista de obras fonte** |
| 8 | PUS_CROSS_V2 | {n_pus_v2} | itens-pus-agregados.json | **4.210 clusters** (mais cobertura) — SEM lista de obras |
| 9 | CURVA_ABC_MASTER | 126 | base-indices-master.json:curva_abc_master | Curva ABC por projeto (n itens, n curva A, valor total) |
| 10 | CROSS_INSIGHTS_GEMMA | varia | base-indices-master.json:cross_insights | Análises Gemma: famílias, lacunas, outliers, padrões, índices sugeridos |

## Schema das colunas numéricas

Convenção usada em todas as abas estatísticas:

- **`n`** — número de projetos ou observações que contribuíram
- **`min` / `max`** — extremos observados
- **`p10` / `p25` / `p75` / `p90`** — percentis
- **`mediana` (p50)** — valor típico (é o que a calibração V2 usa)
- **`media`** — aritmética (pode ser puxada por outliers)
- **`cv`** — coeficiente de variação (`<0.3` confiável, `>0.5` volátil)
- **`projetos_fonte`** — _só em PUS_CROSS_V1_ — lista de slugs separados por `;`

## Exemplos de filtros úteis

### 1. PUs robustos de concreto
Aba **PUS_CROSS_V2** → filtrar `key` contém "concreto" + `n_projetos ≥ 10` + `cv < 0.3`

### 2. Esquadrias: alto vs luxo
Aba **CALIBRACAO_CONDICIONAL** → filtrar `padrao ∈ {{alto, luxo}}` + `macrogrupo = Esquadrias`

### 3. Quais obras bancam o PU mediano de porcelanato?
Aba **PUS_CROSS_V1** → filtrar `descricao` contém "porcelanato" → coluna `projetos_fonte`

### 4. Projetos alto padrão
Aba **PROJETOS** → filtrar `padrao_gemma = alto` → ordenar por `rsm2` desc

### 5. Índices derivados mais confiáveis
Aba **INDICES_DERIVADOS_V2** → ordenar `n` desc → ignorar `n<5`

### 6. MGs com maior dispersão por padrão
Aba **CALIBRACAO_CONDICIONAL** → calcular `p90-p10` → ordenar desc

## Gaps conhecidos

- **PUS_CROSS_V2 (4.210 clusters) NÃO tem lista de projetos** — usa hash-based clustering (fase 10 v2) que não preservou fontes. Quando precisar rastrear obras, use **PUS_CROSS_V1 (1.740)** que tem a lista completa.
- Alguns MGs em **CALIBRACAO_CONDICIONAL** têm `n<3` pro bucket — script paramétrico cai no fallback global × PADRAO_MULTIPLIERS nesses casos
- **`custo_por_ur`** nos derivados tem apenas `n=2` — baixa confiança estatística
- Classe **`luxo`** em CALIBRACAO_CONDICIONAL tem 0 projetos (Gemma não encontrou luxo real na base Cartesian — ver fase 18)
- Campos `disciplinas` / `indices_consumo` / `split_mo_material` dentro de cada `indices-executivo/{{slug}}.json` estão majoritariamente vazios — os dados agregados estão nos arquivos `calibration-*`

## Como regenerar

```bash
cd ~/orcamentos-openclaw
python scripts/gerar_catalogo_indices.py
```

Sem argumentos — lê dinamicamente todos os JSONs da base e regenera `INDICES-CATALOGO.xlsx` + este MD. Deve rodar depois de qualquer update na base (nova calibração, novo projeto processado, nova fase Gemma).

## JSONs fonte

- `base/calibration-indices.json` — 18 MGs global + produto + estruturais + instalações + ci + segmentos
- `base/calibration-condicional-padrao.json` — 18 MGs × 5 padrões (fase 18b, fonte primária)
- `base/base-indices-master-2026-04-13.json` — consolidado 322 KB (derivados + curva ABC + cross insights)
- `base/itens-pus-agregados.json` — 4.210 clusters V2 (fase 10 v2)
- `base/base-pus-cartesian.json` — 1.740 clusters V1 com lista de projetos
- `base/padroes-classificados-consolidado.json` — labels Gemma fase 18 (125/126 projetos)
- `base/indices-executivo/*.json` — 126 arquivos por projeto
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"MD mapa salvo: {OUT_MD}")


def main():
    print("=" * 70)
    print("GERANDO CATÁLOGO DE ÍNDICES CARTESIAN")
    print("=" * 70)

    sources = load_sources()

    wb = Workbook()
    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    print("\nConstruindo abas...")
    build_aba_leia_me(wb, sources)
    print("  [1/10] LEIA_ME")
    build_aba_projetos(wb, sources)
    print("  [2/10] PROJETOS")
    build_aba_calibracao_global(wb, sources)
    print("  [3/10] CALIBRACAO_GLOBAL")
    build_aba_calibracao_condicional(wb, sources)
    print("  [4/10] CALIBRACAO_CONDICIONAL")
    build_aba_derivados(wb, sources)
    print("  [5/10] INDICES_DERIVADOS_V2")
    build_aba_estruturais(wb, sources)
    print("  [6/10] INDICES_ESTRUTURAIS")
    build_aba_pus_v1(wb, sources)
    print("  [7/10] PUS_CROSS_V1 (1.740)")
    build_aba_pus_v2(wb, sources)
    print("  [8/10] PUS_CROSS_V2 (4.210)")
    build_aba_curva_abc(wb, sources)
    print("  [9/10] CURVA_ABC_MASTER")
    build_aba_cross_insights(wb, sources)
    print("  [10/10] CROSS_INSIGHTS_GEMMA")

    print(f"\nSalvando {OUT_XLSX}...")
    wb.save(str(OUT_XLSX))
    size_kb = OUT_XLSX.stat().st_size // 1024
    print(f"  salvo ({size_kb} KB)")

    write_md_mapa(sources)

    print("\nCatalogo gerado com sucesso")


if __name__ == "__main__":
    main()
