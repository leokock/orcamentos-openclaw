#!/usr/bin/env python3
"""Phase 11 — Curvas ABC individual + consolidada.

Para cada projeto, calcula a curva ABC:
- A: primeiros 20% dos itens que representam 80% do valor
- B: próximos 30% dos itens = 15% do valor
- C: últimos 50% dos itens = 5% do valor

Salva curva ABC por projeto em `base/curvas-abc/{projeto}.json`
E gera `base/curva-abc-master.json` consolidando tudo.
"""
from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
ITENS_DIR = BASE / "itens-detalhados"
OUT_DIR = BASE / "curvas-abc"
OUT_DIR.mkdir(parents=True, exist_ok=True)
MASTER_OUT = BASE / "curva-abc-master.json"


def classify_abc(items: list[dict]) -> list[dict]:
    """Classifica itens por A/B/C baseado em valor cumulativo."""
    items_with_total = [
        it for it in items
        if it.get("total") and isinstance(it["total"], (int, float)) and it["total"] > 0
    ]
    items_with_total.sort(key=lambda x: -x["total"])

    total_sum = sum(it["total"] for it in items_with_total)
    if total_sum == 0:
        return []

    cumulative = 0
    classified = []
    for i, it in enumerate(items_with_total):
        cumulative += it["total"]
        pct = cumulative / total_sum
        if pct <= 0.80:
            cls = "A"
        elif pct <= 0.95:
            cls = "B"
        else:
            cls = "C"
        classified.append({
            "rank": i + 1,
            "descricao": (it.get("descricao") or "")[:100],
            "unidade": it.get("unidade"),
            "qtd": it.get("qtd"),
            "pu": it.get("pu"),
            "total": it["total"],
            "pct_acumulado": round(pct, 4),
            "classe": cls,
        })
    return classified


def process_project(slug: str) -> dict:
    jp = ITENS_DIR / f"{slug}.json"
    if not jp.exists():
        return {"slug": slug, "status": "no_data"}

    try:
        d = json.loads(jp.read_text(encoding="utf-8"))
    except Exception as e:
        return {"slug": slug, "status": "error", "error": str(e)}

    all_items = []
    for aba in d.get("abas", []):
        for it in aba.get("itens", []):
            all_items.append(it)

    classified = classify_abc(all_items)
    if not classified:
        return {"slug": slug, "status": "empty"}

    a_items = [c for c in classified if c["classe"] == "A"]
    b_items = [c for c in classified if c["classe"] == "B"]
    c_items = [c for c in classified if c["classe"] == "C"]

    total = sum(c["total"] for c in classified)
    result = {
        "projeto": slug,
        "n_itens": len(classified),
        "valor_total": round(total, 2),
        "n_a": len(a_items),
        "n_b": len(b_items),
        "n_c": len(c_items),
        "pct_a": round(len(a_items) / len(classified) * 100, 1),
        "valor_a": round(sum(c["top"] for c in a_items), 2) if False else round(sum(c["total"] for c in a_items), 2),
        "top_50_itens": classified[:50],
    }

    (OUT_DIR / f"{slug}.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return {"slug": slug, "status": "done",
            "n_itens": len(classified), "n_a": len(a_items),
            "valor_total": total}


def main():
    t0 = time.time()
    projetos = [p.stem for p in sorted(ITENS_DIR.glob("*.json"))]
    print(f"processing {len(projetos)} projects -> {OUT_DIR}")

    results = []
    for i, slug in enumerate(projetos, 1):
        r = process_project(slug)
        results.append(r)
        if r["status"] == "done":
            print(f"[{i}/{len(projetos)}] {slug:<45} itens={r['n_itens']:>5} A={r['n_a']:>3} total={r.get('valor_total',0):>15,.0f}".replace(",", "."), flush=True)

    master = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len([r for r in results if r["status"] == "done"]),
        "n_itens_totais": sum(r.get("n_itens", 0) for r in results if r["status"] == "done"),
        "valor_total_base": sum(r.get("valor_total", 0) for r in results if r["status"] == "done"),
        "projetos": [{k: v for k, v in r.items() if k != "top_50_itens"} for r in results],
    }
    MASTER_OUT.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")

    print()
    print(f"total: {int(time.time() - t0)}s")
    print(f"master: {MASTER_OUT}")


if __name__ == "__main__":
    main()
