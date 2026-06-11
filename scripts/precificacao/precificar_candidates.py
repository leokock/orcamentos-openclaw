"""Fuzzy candidates (top-5 por item Alfa) sobre Aquos e Cartesian pools.

Unifica steps 1+6 dos scripts originais:
  - alfa_precificar_step1_preprocess.py — fuzzy contra pool Aquos
  - alfa_precificar_step6_cartesian_candidates.py — fuzzy contra pool Cartesian

Lê:
  - executivos/[slug]/0X-{disc}/quantitativos-{disc}.xlsx (aba `Consolidado`)
  - tmp/aquos-pool-{disc}.json
  - tmp/cartesian-pool.json

Gera:
  - tmp/match-aquos-candidates-{disc}.csv (top-5 fuzzy Aquos)
  - tmp/match-cartesian-candidates-{disc}.csv (top-5 fuzzy Cartesian)
  - tmp/items-aquos-{disc}.json (chunks pro subagent codex)
  - tmp/items-cartesian-{disc}.json (chunks pro resolver heurístico/subagent)
  - tmp/items-internet-{disc}.json (chunks pro subagent web search — sem candidatos, só itens Alfa)
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import openpyxl
from rapidfuzz import fuzz, process

from precificar_common import (
    norm_text, norm_unit, units_compatible,
    tmp_dir, quantitativos_xlsx, detect_schema, SCHEMAS,
)


def load_alfa_consolidado(xlsx_path: Path, schema_key: str) -> list[dict]:
    """Lê aba `Consolidado` do quantitativo da disciplina. Retorna lista de dicts."""
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    if "Consolidado" not in wb.sheetnames:
        raise ValueError(f"Aba 'Consolidado' não encontrada em {xlsx_path.name}")
    ws = wb["Consolidado"]
    schema = SCHEMAS[schema_key]
    desc_cols = schema["desc_cols"]
    unit_col = schema["unit_col_idx"]
    qty_col = schema["qty_col_idx"]
    extra_cols = schema.get("extra_cols", [])
    rows = []
    for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if not row or not any(row):
            continue
        try:
            desc_parts = [str(row[c - 1] or "").strip() for c in desc_cols if c - 1 < len(row)]
            desc_main = " ".join(p for p in desc_parts if p).strip()
            # contexto extra (pavimento, grupo, sistema) NÃO entra no desc_norm pra match,
            # mas é incluído na desc_extra pra LLM saber do contexto.
            extras = [str(row[c - 1] or "").strip() for c in extra_cols if c - 1 < len(row)]
            extras = [e for e in extras if e]
            unit = str(row[unit_col - 1] or "").strip() if unit_col - 1 < len(row) else ""
            qty = row[qty_col - 1] if qty_col - 1 < len(row) else None
        except (IndexError, TypeError):
            continue
        if not desc_main:
            continue
        rows.append({
            "row": i,
            "item": desc_main,
            "item_contexto": " · ".join(extras) if extras else "",
            "unidade": unit,
            "qtd_total": qty,
            "desc_norm": norm_text(desc_main),
            "unidade_norm": norm_unit(unit),
        })
    return rows


def find_top_k(alfa_item: dict, pool: list[dict], top_k: int = 5, pool_extra_fields=None):
    """Top-k pool candidates por token_set_ratio com filtro unit compat."""
    alfa_norm = alfa_item["desc_norm"]
    alfa_unit = alfa_item["unidade_norm"]
    compat = [p for p in pool if units_compatible(alfa_unit, p.get("unit_norm", ""))]
    if not compat:
        compat = pool
    choices = {i: p["desc_norm"] for i, p in enumerate(compat)}
    matches = process.extract(alfa_norm, choices, scorer=fuzz.token_set_ratio, limit=top_k)
    out = []
    for _, score, idx in matches:
        p = compat[idx]
        cand = {
            "desc": p["desc"],
            "unit": p["unit"],
            "price": p["price"],
            "score": round(score, 1),
        }
        for f in pool_extra_fields or []:
            cand[f] = p.get(f, "")
        out.append(cand)
    while len(out) < top_k:
        out.append({"desc": "", "unit": "", "price": "", "score": 0,
                    **{f: "" for f in pool_extra_fields or []}})
    return out


def write_candidates_csv(out_path: Path, alfa_rows, pool, source_name: str, extra_fields):
    cand_cols = []
    for i in range(1, 6):
        cand_cols.append(f"cand{i}_desc")
        cand_cols.append(f"cand{i}_unit")
        cand_cols.append(f"cand{i}_price")
        for f in extra_fields:
            cand_cols.append(f"cand{i}_{f}")
        cand_cols.append(f"cand{i}_score")
    base = ["alfa_id", "alfa_desc", "alfa_unit", "alfa_qtd"]
    with open(out_path, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.writer(fp, delimiter=";")
        w.writerow(base + cand_cols)
        for r in alfa_rows:
            cands = find_top_k(r, pool, pool_extra_fields=extra_fields)
            row = [r["row"], r["item"], r["unidade"], r.get("qtd_total")]
            for c in cands:
                row.extend([c["desc"], c["unit"], c["price"]])
                for f in extra_fields:
                    row.append(c.get(f, ""))
                row.append(c["score"])
            w.writerow(row)


def write_items_json(out_path: Path, alfa_rows, pool, extra_fields):
    """JSON pra subagent resolver: alfa_id + alfa_desc + alfa_unit + alfa_qtd + top-5 candidates."""
    items = []
    for r in alfa_rows:
        cands = find_top_k(r, pool, pool_extra_fields=extra_fields) if pool else []
        items.append({
            "alfa_id": r["row"],
            "alfa_desc": r["item"],
            "alfa_unit": r["unidade"],
            "alfa_qtd": r.get("qtd_total"),
            "candidates": cands,
        })
    out_path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(items)


def run_disciplina(slug: str, disc_idx: int, disc_slug: str, has_cartesian=True):
    """Gera todos os artefatos pra uma disciplina."""
    print(f"\n=== {disc_slug.upper()} ===")
    tmp = tmp_dir(slug)
    qpath = quantitativos_xlsx(slug, disc_idx, disc_slug)
    if not qpath.exists():
        print(f"  WARNING: {qpath} não existe, pulando.")
        return None
    schema_key = detect_schema(disc_slug, qpath)
    print(f"  schema detectado: {schema_key}")

    alfa = load_alfa_consolidado(qpath, schema_key)
    print(f"  Alfa items: {len(alfa)}")

    # Aquos
    aquos_pool_file = tmp / f"aquos-pool-{disc_slug}.json"
    if aquos_pool_file.exists():
        aquos_pool = json.loads(aquos_pool_file.read_text(encoding="utf-8"))
        print(f"  Aquos pool: {len(aquos_pool)}")
        write_candidates_csv(tmp / f"match-aquos-candidates-{disc_slug}.csv", alfa, aquos_pool, "aquos", [])
        write_items_json(tmp / f"items-aquos-{disc_slug}.json", alfa, aquos_pool, [])
    else:
        print(f"  (sem pool Aquos pra {disc_slug} — pulando match Aquos)")

    # Cartesian
    if has_cartesian:
        cart_pool_file = tmp / "cartesian-pool.json"
        if cart_pool_file.exists():
            cart_pool = json.loads(cart_pool_file.read_text(encoding="utf-8"))
            print(f"  Cartesian pool: {len(cart_pool)}")
            write_candidates_csv(
                tmp / f"match-cartesian-candidates-{disc_slug}.csv",
                alfa, cart_pool, "cartesian",
                ["obra_nome", "source", "date"],
            )
            write_items_json(
                tmp / f"items-cartesian-{disc_slug}.json",
                alfa, cart_pool,
                ["obra_nome", "source", "date"],
            )
        else:
            print(f"  (sem cartesian-pool.json — pulando match Cartesian)")

    # Internet: só lista de itens Alfa, sem candidates (subagent vai buscar)
    items_internet = [{
        "alfa_id": r["row"],
        "alfa_desc": r["item"],
        "alfa_contexto": r.get("item_contexto", ""),
        "alfa_unit": r["unidade"],
        "alfa_qtd": r.get("qtd_total"),
    } for r in alfa]
    (tmp / f"items-internet-{disc_slug}.json").write_text(
        json.dumps(items_internet, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Internet items chunk: {len(items_internet)}")

    return len(alfa)


def main():
    ap = argparse.ArgumentParser(description="Gera top-5 candidates fuzzy por item Alfa")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--disciplinas", help="lista 'pci,sanitario,telecom' ou 'auto'")
    args = ap.parse_args()

    from precificar_common import discover_disciplinas
    if args.disciplinas in (None, "auto"):
        discs = discover_disciplinas(args.slug)
    else:
        from precificar_common import executivo_dir
        # auto-detect idx pelo nome de pasta
        base = executivo_dir(args.slug)
        wanted = [s.strip() for s in args.disciplinas.split(",")]
        discs = []
        for w in wanted:
            for sub in base.iterdir() if base.exists() else []:
                if sub.is_dir() and sub.name.endswith(f"-{w}"):
                    idx = int(sub.name.split("-")[0])
                    discs.append((idx, w))
                    break
    print(f"Disciplinas: {discs}")

    for idx, disc in discs:
        run_disciplina(args.slug, idx, disc)


if __name__ == "__main__":
    main()
