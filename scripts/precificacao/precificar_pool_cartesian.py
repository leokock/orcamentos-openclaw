"""Pool Cartesian (Fonte 3): consolida preços históricos da Cartesian.

Portado de ~/openclaw/scripts/alfa_precificar_step5_cartesian_pool.py.
Mudanças vs original:
  - parametrizado por --slug (paths vão pra executivos/[slug]/_tmp/precificacao/cartesian-raw/)
  - aceita --dump-dir alternativo (pra reusar dump existente)
  - sem hardcode de paths alfa-colinas

Lê dumps JSON do MongoDB Cartesian (coletados via precificar_dump_mongo.py):
  - purchase_orders_items_full.json (preço pago real em OCs)
  - resources_batch*.json (orçamento estimado por obra)
  - buildings.json (mapa obra_id → nome+company)

Dedupe por (desc_norm, unit_norm) priorizando PO sobre resources, data mais recente.
Output: tmp/cartesian-pool.json + cartesian-pool-stats.txt
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from precificar_common import norm_text, norm_unit, tmp_dir


def load_mcp_result(path: Path):
    """MCP outputs are {result: "JSON_string"} — parse twice if needed."""
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    if isinstance(data, dict) and "result" in data:
        return json.loads(data["result"])
    return data


def safe_float(x):
    if x is None:
        return None
    try:
        v = float(x)
        if v != v:  # NaN
            return None
        return v
    except (ValueError, TypeError):
        return None


def build_pool(dump_dir: Path):
    """Lê dumps e produz (pool deduplicado, stats dict)."""
    buildings_file = dump_dir / "buildings.json"
    po_file = dump_dir / "purchase_orders_items_full.json"
    resources_files = sorted(dump_dir.glob("resources_batch*.json"))

    if not buildings_file.exists():
        raise FileNotFoundError(f"buildings.json não encontrado em {dump_dir}")
    if not po_file.exists():
        raise FileNotFoundError(f"purchase_orders_items_full.json não encontrado em {dump_dir}")

    print(f"Reading {buildings_file.name}")
    buildings = json.loads(buildings_file.read_text(encoding="utf-8"))
    if isinstance(buildings, dict) and "result" in buildings:
        buildings = json.loads(buildings["result"])
    building_map = {b["id"]: b for b in buildings}
    print(f"  -> {len(buildings)} obras mapeadas\n")

    candidates = []
    skipped = {"no_desc": 0, "no_price": 0, "zero_price": 0, "no_building": 0}

    def add_item(desc, unit, price, building_id, date, source):
        if not desc:
            skipped["no_desc"] += 1
            return
        p = safe_float(price)
        if p is None:
            skipped["no_price"] += 1
            return
        if p <= 0:
            skipped["zero_price"] += 1
            return
        if not building_id:
            skipped["no_building"] += 1
            return
        b = building_map.get(building_id)
        obra_nome = b["name"] if b else f"(obra {building_id[:8]})"
        company = b.get("company", "") if b else ""
        desc_norm = norm_text(desc)
        unit_norm = norm_unit(unit)
        if not desc_norm:
            skipped["no_desc"] += 1
            return
        candidates.append({
            "desc": str(desc).strip(),
            "unit": str(unit or "").strip(),
            "price": p,
            "obra_id": building_id,
            "obra_nome": obra_nome,
            "company": company,
            "source": source,
            "date": date[:10] if isinstance(date, str) and len(date) >= 10 else (date or ""),
            "desc_norm": desc_norm,
            "unit_norm": unit_norm,
        })

    # Source 1: purchase_orders_items (preço pago real)
    print(f"Reading {po_file.name}")
    po_items = load_mcp_result(po_file)
    print(f"  -> {len(po_items)} purchase_orders_items raw")
    for item in po_items:
        add_item(
            item.get("resource_description"),
            item.get("unit_of_measure"),
            item.get("unit_price"),
            item.get("building_id"),
            item.get("date") or item.get("created_at") or "",
            "po_items",
        )

    # Source 2: resources (orçamento)
    for rf in resources_files:
        print(f"Reading {rf.name}")
        items = load_mcp_result(rf)
        print(f"  -> {len(items)} resources raw")
        for item in items:
            add_item(
                item.get("description"),
                item.get("unit_of_measure"),
                item.get("unit_price"),
                item.get("building_id"),
                item.get("measurement_date") or "",
                "resources",
            )

    print(f"\n  raw candidatos: {len(candidates)}")
    for k, v in skipped.items():
        print(f"    skipped {k}: {v}")

    # Dedupe por (desc_norm, unit_norm). Priority: po_items > resources.
    bucket = {}
    for c in candidates:
        key = (c["desc_norm"], c["unit_norm"])
        existing = bucket.get(key)
        if existing is None:
            bucket[key] = c
            continue
        if existing["source"] == "resources" and c["source"] == "po_items":
            bucket[key] = c
        elif existing["source"] == c["source"] and c["date"] > existing["date"]:
            bucket[key] = c
    pool = sorted(bucket.values(), key=lambda x: (x["desc_norm"], x["unit_norm"]))
    print(f"  pool deduplicado: {len(pool)}")

    # Stats
    by_obra = {}
    by_unit = {}
    for c in pool:
        by_obra[c["obra_nome"]] = by_obra.get(c["obra_nome"], 0) + 1
        by_unit[c["unit_norm"] or "(empty)"] = by_unit.get(c["unit_norm"] or "(empty)", 0) + 1

    stats = {
        "raw_count": len(candidates),
        "deduped_count": len(pool),
        "skipped": skipped,
        "top_obras": sorted(by_obra.items(), key=lambda kv: -kv[1])[:20],
        "by_unit": sorted(by_unit.items(), key=lambda kv: -kv[1])[:20],
    }
    return pool, stats


def write_outputs(pool, stats, out_dir: Path):
    pool_file = out_dir / "cartesian-pool.json"
    stats_file = out_dir / "cartesian-pool-stats.txt"
    pool_file.write_text(json.dumps(pool, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  -> {pool_file}")

    lines = [
        f"Total candidates raw: {stats['raw_count']}",
        f"Total candidates deduped: {stats['deduped_count']}",
        "",
        "Top 20 obras por nº de candidatos:",
    ]
    for k, v in stats["top_obras"]:
        lines.append(f"  {v:5d}  {k}")
    lines.append("")
    lines.append("Distribuição por unidade (top 20):")
    for k, v in stats["by_unit"]:
        lines.append(f"  {v:5d}  {k}")
    stats_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"  stats -> {stats_file}")
    return pool_file


def main():
    ap = argparse.ArgumentParser(description="Constrói pool Cartesian a partir de dumps MongoDB")
    ap.add_argument("--slug", required=True, help="Slug do projeto (define out dir)")
    ap.add_argument("--dump-dir", help="Path alternativo pra dumps (default: tmp/cartesian-raw/)")
    args = ap.parse_args()

    out_dir = tmp_dir(args.slug)
    dump_dir = Path(args.dump_dir) if args.dump_dir else out_dir / "cartesian-raw"
    if not dump_dir.exists():
        raise SystemExit(f"Dump dir não encontrado: {dump_dir}. Rode precificar_dump_mongo.py primeiro.")

    pool, stats = build_pool(dump_dir)
    write_outputs(pool, stats, out_dir)


if __name__ == "__main__":
    main()
