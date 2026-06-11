"""Monta xlsx final de precificação 3-fontes (1 por disciplina) + Resumo + README.

Portado de ~/openclaw/scripts/alfa_precificar_step7_montar_v2.py.
Mudanças:
  - parametrizado por --slug, --out-tag (default 'banco-de-dados'), --proj-ref-label
  - schema do quantitativo detectado via SCHEMAS (REGRA #3 ou legacy)
  - aceita ausência de fontes Aquos ou Internet (entrega só Cartesian se for o caso)
  - paths via precificar_common helpers

Layout xlsx (34 cols quando schema REGRA #3, 32-34 quando legacy):
  header original (10 REGRA #3 / 8 PCI legacy / 6 SAN-TEL legacy)
  + 5 Aquos azul + 5 Internet verde + 6 Cartesian laranja + 3 Subtotais (fórmula Excel)

Cores:
  Aquos = 0000FF (azul)
  Internet = 008000 (verde)
  Cartesian = D86A00 (laranja) com fundo FFF2E5
  Confiança 'baixa' → fundo FFFF00 (amarelo)
"""
from __future__ import annotations

import argparse
import json
import unicodedata
from datetime import date
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from precificar_common import (
    SCHEMAS, detect_schema, discover_disciplinas, executivo_dir,
    quantitativos_xlsx, tmp_dir, precificacao_out_dir,
)

TODAY = date.today().isoformat()


def norm_conf(c):
    if not c:
        return "sem-match"
    s = str(c).lower().strip()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    mapping = {"alta": "alta", "media": "média", "baixa": "baixa",
               "sem": "sem-match", "sem-match": "sem-match"}
    return mapping.get(s, s)


def load_resolved(path: Path):
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {int(r["alfa_id"]): r for r in data}


def load_internet(path: Path):
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  ERRO ao ler {path.name}: {e}")
        return {}
    out = {}
    for r in data:
        out[int(r["alfa_id"])] = r
    return out


def to_float(x):
    try:
        v = float(x)
        if v != v:
            return None
        return v
    except (ValueError, TypeError):
        return None


def build_xlsx(slug: str, disc_idx: int, disc_slug: str, out_dir: Path,
               proj_ref_label: str = "Aquos"):
    """Monta xlsx pra 1 disciplina. Retorna stats dict."""
    print(f"\n=== {disc_slug.upper()} ===")
    tmp = tmp_dir(slug)
    qpath = quantitativos_xlsx(slug, disc_idx, disc_slug)
    if not qpath.exists():
        print(f"  WARNING: {qpath} não existe.")
        return None
    schema_key = detect_schema(disc_slug, qpath)
    schema = SCHEMAS[schema_key]
    qty_col = schema["qty_col_idx"]

    alfa_wb = openpyxl.load_workbook(qpath, data_only=True)
    src_ws = alfa_wb["Consolidado"]

    aquos = load_resolved(tmp / f"match-aquos-resolved-{disc_slug}.json")
    cart = load_resolved(tmp / f"match-cartesian-resolved-{disc_slug}.json")
    internet = load_internet(tmp / f"internet-{disc_slug}.json")
    print(f"  Aquos: {len(aquos)} | Internet: {len(internet)} | Cartesian: {len(cart)}")

    out_wb = openpyxl.Workbook()
    out_ws = out_wb.active
    out_ws.title = "Precificacao"

    header_orig = [cell.value for cell in src_ws[1]]
    aq = proj_ref_label
    new_cols_aquos = [
        f"Item {aq} Casado", f"Unidade {aq}", f"Preço {aq} (R$)",
        f"Confiança {aq}", f"Justificativa {aq}",
    ]
    new_cols_internet = [
        "Preço Internet (R$)", "Loja Internet", "URL Internet",
        "Observação Internet", "Data Pesquisa",
    ]
    new_cols_cartesian = [
        "Item Cartesian Casado", "Unidade Cartesian", "Preço Cartesian (R$)",
        "Obra de Referência", "Confiança Cartesian", "Justificativa Cartesian",
    ]
    new_cols_subtotais = [
        f"Subtotal {aq} (R$)", "Subtotal Internet (R$)", "Subtotal Cartesian (R$)",
    ]
    full_header = header_orig + new_cols_aquos + new_cols_internet + new_cols_cartesian + new_cols_subtotais
    out_ws.append(full_header)

    H = len(header_orig)
    AQ_BASE = H + 1
    AQ_PRICE_COL = AQ_BASE + 2
    AQ_CONF_COL = AQ_BASE + 3
    INT_BASE = AQ_BASE + 5
    INT_PRICE_COL = INT_BASE
    CT_BASE = INT_BASE + 5
    CT_PRICE_COL = CT_BASE + 2
    CT_CONF_COL = CT_BASE + 4
    SUB_AQ_COL = CT_BASE + 6
    SUB_INT_COL = SUB_AQ_COL + 1
    SUB_CT_COL = SUB_AQ_COL + 2

    blue = Font(name="Arial", color="0000FF")
    green = Font(name="Arial", color="008000")
    orange = Font(name="Arial", color="D86A00")
    bold = Font(name="Arial", bold=True)
    bold_blue = Font(name="Arial", color="0000FF", bold=True)
    bold_green = Font(name="Arial", color="008000", bold=True)
    bold_orange = Font(name="Arial", color="D86A00", bold=True)
    yellow_fill = PatternFill("solid", start_color="FFFF00")
    cart_block_fill = PatternFill("solid", start_color="FFF2E5")
    currency_fmt = 'R$ #,##0.00;[Red]-R$ #,##0.00;-'

    n_aq = {"alta": 0, "média": 0, "baixa": 0, "sem-match": 0}
    n_ct = {"alta": 0, "média": 0, "baixa": 0, "sem-match": 0}
    n_internet = 0
    n_total = 0
    sum_aq = sum_int = sum_ct = 0.0

    for row_idx, row in enumerate(src_ws.iter_rows(min_row=2, values_only=True), start=2):
        if not row or not any(row):
            continue
        n_total += 1
        out_row = list(row)
        a = aquos.get(row_idx) or {}
        i = internet.get(row_idx) or {}
        c = cart.get(row_idx) or {}

        a_desc = a.get("matched_desc") or ""
        a_unit = a.get("matched_unit") or ""
        a_price = a.get("matched_price")
        a_conf = norm_conf(a.get("confidence") or "sem-match")
        a_reason = a.get("reasoning") or ""
        n_aq[a_conf] = n_aq.get(a_conf, 0) + 1

        i_price = i.get("preco_internet")
        i_loja = i.get("loja") or ""
        i_url = i.get("url") or ""
        i_obs = i.get("observacao") or ""
        if i_price is not None:
            n_internet += 1

        c_desc = c.get("matched_desc") or ""
        c_unit = c.get("matched_unit") or ""
        c_price = c.get("matched_price")
        c_obra = c.get("obra_nome") or ""
        c_conf = norm_conf(c.get("confidence") or "sem-match")
        c_reason = c.get("reasoning") or ""
        n_ct[c_conf] = n_ct.get(c_conf, 0) + 1

        qty_raw = out_row[qty_col - 1] if qty_col - 1 < len(out_row) else None
        qty = to_float(qty_raw) or 0.0
        ap = to_float(a_price)
        ip = to_float(i_price)
        cp = to_float(c_price)
        if ap is not None:
            sum_aq += qty * ap
        if ip is not None:
            sum_int += qty * ip
        if cp is not None:
            sum_ct += qty * cp

        out_row += [
            a_desc, a_unit, ap, a_conf, a_reason,
            i_price, i_loja, i_url, i_obs, (TODAY if i else ""),
            c_desc, c_unit, cp, c_obra, c_conf, c_reason,
            None, None, None,  # placeholders pros subtotais
        ]
        out_ws.append(out_row)
        r = out_ws.max_row
        ql = get_column_letter(qty_col)
        al = get_column_letter(AQ_PRICE_COL)
        il = get_column_letter(INT_PRICE_COL)
        cl = get_column_letter(CT_PRICE_COL)
        out_ws.cell(row=r, column=SUB_AQ_COL).value = (
            f'=IF(AND(ISNUMBER({ql}{r}),ISNUMBER({al}{r})),{ql}{r}*{al}{r},"")'
        )
        out_ws.cell(row=r, column=SUB_INT_COL).value = (
            f'=IF(AND(ISNUMBER({ql}{r}),ISNUMBER({il}{r})),{ql}{r}*{il}{r},"")'
        )
        out_ws.cell(row=r, column=SUB_CT_COL).value = (
            f'=IF(AND(ISNUMBER({ql}{r}),ISNUMBER({cl}{r})),{ql}{r}*{cl}{r},"")'
        )

    # Header styling
    for col_idx in range(1, len(full_header) + 1):
        cell = out_ws.cell(row=1, column=col_idx)
        cell.font = bold
        if AQ_BASE <= col_idx < AQ_BASE + 5:
            cell.font = bold_blue
        elif INT_BASE <= col_idx < INT_BASE + 5:
            cell.font = bold_green
        elif CT_BASE <= col_idx < CT_BASE + 6:
            cell.font = bold_orange
            cell.fill = cart_block_fill
        elif col_idx == SUB_AQ_COL:
            cell.font = bold_blue
        elif col_idx == SUB_INT_COL:
            cell.font = bold_green
        elif col_idx == SUB_CT_COL:
            cell.font = bold_orange
            cell.fill = cart_block_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Body styling
    for r in range(2, out_ws.max_row + 1):
        ap_cell = out_ws.cell(row=r, column=AQ_PRICE_COL)
        if ap_cell.value not in (None, ""):
            ap_cell.font = blue
            ap_cell.number_format = currency_fmt
        ip_cell = out_ws.cell(row=r, column=INT_PRICE_COL)
        if ip_cell.value not in (None, ""):
            ip_cell.font = green
            ip_cell.number_format = currency_fmt
        cp_cell = out_ws.cell(row=r, column=CT_PRICE_COL)
        if cp_cell.value not in (None, ""):
            cp_cell.font = orange
            cp_cell.number_format = currency_fmt
        for col_idx in range(CT_BASE, CT_BASE + 6):
            out_ws.cell(row=r, column=col_idx).fill = cart_block_fill
        out_ws.cell(row=r, column=SUB_AQ_COL).number_format = currency_fmt
        out_ws.cell(row=r, column=SUB_INT_COL).number_format = currency_fmt
        out_ws.cell(row=r, column=SUB_CT_COL).number_format = currency_fmt
        out_ws.cell(row=r, column=SUB_CT_COL).fill = cart_block_fill
        for conf_col in (AQ_CONF_COL, CT_CONF_COL):
            cf = out_ws.cell(row=r, column=conf_col)
            if cf.value == "baixa":
                cf.fill = yellow_fill

    # Widths
    widths = {}
    for col_idx, name in enumerate(full_header, start=1):
        ln = max(12, min(50, len(str(name)) + 2))
        widths[col_idx] = ln
    for col_idx, name in enumerate(full_header, start=1):
        n = str(name).lower()
        if any(k in n for k in ("item", "descri", "desc", "justif", "obs", "url", "obra")):
            widths[col_idx] = max(widths[col_idx], 40)
        if "preço" in n or "preco" in n:
            widths[col_idx] = 18
    for col_idx, w in widths.items():
        out_ws.column_dimensions[get_column_letter(col_idx)].width = w
    out_ws.freeze_panes = "A2"

    # Resumo
    resumo = out_wb.create_sheet("Resumo")
    rows = [
        ("Disciplina", disc_slug),
        ("Data", TODAY),
        ("", ""),
        ("Total de itens", n_total),
        ("", ""),
        (f"Match {aq} — alta", n_aq.get("alta", 0)),
        (f"Match {aq} — média", n_aq.get("média", 0)),
        (f"Match {aq} — baixa", n_aq.get("baixa", 0)),
        (f"Sem match {aq}", n_aq.get("sem-match", 0)),
        (f"Cobertura {aq} (%)",
         f"{round(100 * (n_aq['alta'] + n_aq['média'] + n_aq['baixa']) / max(1, n_total), 1)}%"),
        ("", ""),
        ("Itens com preço internet", n_internet),
        ("Cobertura internet (%)", f"{round(100 * n_internet / max(1, n_total), 1)}%"),
        ("", ""),
        ("Match Cartesian — alta", n_ct.get("alta", 0)),
        ("Match Cartesian — média", n_ct.get("média", 0)),
        ("Match Cartesian — baixa", n_ct.get("baixa", 0)),
        ("Sem match Cartesian", n_ct.get("sem-match", 0)),
        ("Cobertura Cartesian (%)",
         f"{round(100 * (n_ct['alta'] + n_ct['média'] + n_ct['baixa']) / max(1, n_total), 1)}%"),
        ("", ""),
        (f"Subtotal {aq} (R$)", round(sum_aq, 2)),
        ("Subtotal Internet (R$)", round(sum_int, 2)),
        ("Subtotal Cartesian (R$)", round(sum_ct, 2)),
    ]
    for row in rows:
        resumo.append(row)
    for r in range(1, resumo.max_row + 1):
        resumo.cell(row=r, column=1).font = bold
    resumo.column_dimensions["A"].width = 30
    resumo.column_dimensions["B"].width = 18

    out_path = out_dir / f"precificacao-{disc_slug}.xlsx"
    out_wb.save(out_path)
    print(f"  saved: {out_path.name}")
    return {
        "disc": disc_slug, "total": n_total,
        "aq_alta": n_aq["alta"], "aq_media": n_aq["média"], "aq_baixa": n_aq["baixa"], "aq_sem": n_aq["sem-match"],
        "ct_alta": n_ct["alta"], "ct_media": n_ct["média"], "ct_baixa": n_ct["baixa"], "ct_sem": n_ct["sem-match"],
        "internet": n_internet,
        "sum_aq": round(sum_aq, 2), "sum_int": round(sum_int, 2), "sum_ct": round(sum_ct, 2),
    }


def write_readme(out_dir: Path, stats: list[dict], slug: str, proj_ref_label: str):
    readme = out_dir / "README-precificacao.md"
    aq = proj_ref_label
    with open(readme, "w", encoding="utf-8") as f:
        f.write(f"# Precificação {slug} — README (3 fontes)\n\n")
        f.write(f"**Data:** {TODAY}\n\n")
        f.write(f"Pacote de precificação com 3 fontes simultâneas, gerado pelo Cartesiano:\n\n")
        f.write("## Metodologia\n\n")
        f.write(f"1. **{aq} (azul)**: referência de empreendimento similar — match fuzzy contra planilha PREÇO da obra-referência.\n")
        f.write("2. **Internet (verde)**: preço de varejo BR (Leroy, Telhanorte, Mercado Livre etc.), pesquisado por subagent com WebSearch.\n")
        f.write("3. **Cartesian (laranja)**: preço pago em obras anteriores da Cartesian (MongoDB `purchase_orders_items` + `resources`), match fuzzy + heurística determinística.\n\n")
        f.write("## Estatísticas\n\n")
        f.write(f"| Disciplina | Total | {aq} (alta/média/baixa/sem) | Internet | Cartesian (alta/média/baixa/sem) |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for s in stats:
            aqcell = f"{s['aq_alta']}/{s['aq_media']}/{s['aq_baixa']}/{s['aq_sem']}"
            ctcell = f"{s['ct_alta']}/{s['ct_media']}/{s['ct_baixa']}/{s['ct_sem']}"
            f.write(f"| {s['disc']} | {s['total']} | {aqcell} | {s['internet']} | {ctcell} |\n")
        total_total = sum(s["total"] for s in stats)
        total_ct = sum(s["ct_alta"] + s["ct_media"] + s["ct_baixa"] for s in stats)
        f.write(f"\n**Cobertura Cartesian global:** {total_ct}/{total_total} = ")
        f.write(f"{round(100 * total_ct / max(1, total_total), 1)}%\n\n")
        f.write("**Subtotais (R$):**\n\n")
        f.write(f"| Disciplina | {aq} | Internet | Cartesian |\n")
        f.write("|---|---:|---:|---:|\n")
        for s in stats:
            f.write(f"| {s['disc']} | R$ {s['sum_aq']:,.2f} | R$ {s['sum_int']:,.2f} | R$ {s['sum_ct']:,.2f} |\n")
        f.write("\n## Como usar\n\n")
        f.write(f"- **Preço {aq} (R$)** (azul): referência do empreendimento {aq}.\n")
        f.write("- **Preço Internet (R$)** (verde): preço de varejo BR (snapshot da data acima).\n")
        f.write("- **Preço Cartesian (R$)** (laranja): preço pago em obra real (PO) ou orçado (resources) — ver coluna **Obra de Referência**.\n")
        f.write(f"- **Confiança {aq} / Cartesian**: alta=match seguro, média=match parcial, baixa=match incerto (fundo amarelo), sem-match=sem equivalente.\n")
        f.write("- **Subtotal**: `Qtd × Preço`. Vazio quando algum falta.\n\n")
        f.write("## Pontos de atenção\n\n")
        f.write("- Itens marcados 'baixa' (fundo amarelo) merecem revisão humana — match incerto.\n")
        f.write(f"- O pool Cartesian é dominado por obras com dados densos no BI (LUMIS, Voss, ATLANTIA, etc.). Obras sem `purchase_orders_items` foram representadas via `resources` (orçamento).\n")
        f.write("- Itens com unidade muito específica podem ter pego candidatos genéricos.\n\n")
        f.write("## Pipeline (rastreabilidade)\n\n")
        f.write("Scripts em `scripts/precificacao/`:\n")
        f.write("- `precificar_orchestrate.py` — orquestrador CLI (entrypoint)\n")
        f.write("- `precificar_dump_mongo.py` — coleta MongoDB Cartesian\n")
        f.write("- `precificar_pool_cartesian.py` / `precificar_pool_aquos.py` — pools por fonte\n")
        f.write("- `precificar_candidates.py` — fuzzy top-5\n")
        f.write("- `precificar_resolver_cartesian.py` — heurística determinística (Cartesian)\n")
        f.write("- `precificar_resolver_subagent.py` — subagent codex (Aquos + Internet)\n")
        f.write("- `precificar_montar.py` — montagem do xlsx final (este script)\n\n")
        f.write(f"Arquivos intermediários em `executivos/{slug}/_tmp/precificacao/`:\n")
        f.write("- `cartesian-pool.json` — pool unificado\n")
        f.write(f"- `aquos-pool-{{disc}}.json` — pool {aq} por disciplina\n")
        f.write("- `match-{aquos,cartesian}-candidates-{disc}.csv` — top-5 fuzzy\n")
        f.write("- `match-{aquos,cartesian}-resolved-{disc}.json` — match escolhido\n")
        f.write("- `internet-{disc}.json` — preços Internet por item\n")
    print(f"\nREADME: {readme}")


def main():
    ap = argparse.ArgumentParser(description="Monta xlsx finais de precificação")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--proj-ref-label", default="Aquos", help="Nome do projeto-referência pros headers")
    ap.add_argument("--out-tag", default="banco-de-dados",
                    help="Sufixo da pasta destino: XX-precificacao-<TAG>")
    args = ap.parse_args()

    out_dir = precificacao_out_dir(args.slug, args.out_tag)
    print(f"Output dir: {out_dir}")
    discs = discover_disciplinas(args.slug)
    stats = []
    for idx, disc in discs:
        s = build_xlsx(args.slug, idx, disc, out_dir, args.proj_ref_label)
        if s:
            stats.append(s)
    write_readme(out_dir, stats, args.slug, args.proj_ref_label)
    print("\nDONE.")


if __name__ == "__main__":
    main()
