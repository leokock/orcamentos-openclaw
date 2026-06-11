"""Pool Aquos/projeto-ref (Fonte 1): extrai (desc, unit, price) de planilhas-ref do projeto-referência.

Portado de ~/openclaw/scripts/alfa_precificar_step1_preprocess.py (só a parte de load_aquos).
Mudanças vs original:
  - parametrizado por --proj-ref-dir + lista de planilhas por disciplina
  - função importável: extract_pool_aquos(xlsx_path, sheet='PREÇO', header_row=7)
  - heurística pra encontrar coluna de descrição/unidade/preço

A planilha de referência tem aba "PREÇO" ou "Preço Unitário" com layout:
  - row 7+ tem dados
  - cols: [vazio | vazio | Descrição | Unidade | Custo Unitário | ...]
Se header não estiver na row 7, tenta auto-detect.

Output: tmp/aquos-pool-{disc}.json com lista [{desc, unit, price, desc_norm, unit_norm}]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import openpyxl

from precificar_common import norm_text, norm_unit, tmp_dir


def _detect_header(ws, max_search_rows=15):
    """Acha row do header procurando 'descri' + 'preço/custo unit' no mesmo row."""
    for row_idx in range(1, min(max_search_rows + 1, ws.max_row + 1)):
        cells = [str(c.value or "").lower() for c in ws[row_idx]]
        has_desc = any("descri" in c or "item" in c or "material" in c for c in cells)
        has_price = any("preç" in c or "preco" in c or "custo" in c or "valor unit" in c for c in cells)
        if has_desc and has_price:
            return row_idx
    return None


def _find_cols(ws, header_row):
    """Retorna dict {desc: idx, unit: idx, price: idx} (1-indexed)."""
    cols = {"desc": None, "unit": None, "price": None}
    for c_idx, cell in enumerate(ws[header_row], start=1):
        v = str(cell.value or "").lower().strip()
        if cols["desc"] is None and ("descri" in v or v in ("item", "material")):
            cols["desc"] = c_idx
        elif cols["unit"] is None and ("unid" in v or v in ("un", "und")):
            cols["unit"] = c_idx
        elif cols["price"] is None and ("preç" in v or "preco" in v or "custo unit" in v or "valor unit" in v):
            cols["price"] = c_idx
    return cols


def extract_pool_aquos(xlsx_path: Path, sheet: str | None = None):
    """Extrai pool Aquos. Retorna lista de dicts {desc, unit, price, desc_norm, unit_norm}.

    Tenta sheet 'PREÇO' (case-insensitive) por default, ou usa o nome passado.
    Se não achar header automaticamente, usa row 7 (default do Aquos Blue Haven).
    """
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    target = sheet
    if target is None:
        for s in wb.sheetnames:
            if "preç" in s.lower() or "preco" in s.lower() or "unit" in s.lower():
                target = s
                break
        if target is None:
            target = wb.sheetnames[0]
    ws = wb[target]

    header_row = _detect_header(ws) or 7
    cols = _find_cols(ws, header_row)
    if cols["desc"] is None or cols["price"] is None:
        # fallback aos índices fixos do Aquos Blue Haven (cols 3=C desc, 4=D unit, 5=E price)
        cols = {"desc": 3, "unit": 4, "price": 5}

    items = []
    for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
        if not row:
            continue
        try:
            desc = row[cols["desc"] - 1]
            unit = row[cols["unit"] - 1] if cols["unit"] else None
            price = row[cols["price"] - 1]
        except IndexError:
            continue
        if not desc or price is None:
            continue
        try:
            price_f = float(price)
        except (ValueError, TypeError):
            continue
        if price_f <= 0:
            continue
        items.append({
            "desc": str(desc).strip(),
            "unit": str(unit or "").strip(),
            "price": price_f,
            "desc_norm": norm_text(desc),
            "unit_norm": norm_unit(unit),
        })
    return items


def main():
    ap = argparse.ArgumentParser(description="Extrai pool Aquos/projeto-ref de planilha")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--xlsx", required=True, help="Path da planilha-ref")
    ap.add_argument("--disc", required=True, help="Disciplina (pci/sanitario/telecom/...)")
    ap.add_argument("--sheet", help="Nome da aba (default: auto-detect PREÇO)")
    args = ap.parse_args()

    xlsx_path = Path(args.xlsx)
    if not xlsx_path.exists():
        raise SystemExit(f"Não encontrei {xlsx_path}")

    pool = extract_pool_aquos(xlsx_path, sheet=args.sheet)
    out = tmp_dir(args.slug) / f"aquos-pool-{args.disc}.json"
    out.write_text(json.dumps(pool, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  {args.disc}: {len(pool)} itens precificados -> {out.name}")


if __name__ == "__main__":
    main()
