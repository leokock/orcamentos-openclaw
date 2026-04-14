#!/usr/bin/env python3
"""Phase 10 — Normalização e fuzzy-match de descrições cross-projeto.

Lê todos os itens-detalhados/*.json (333.751 itens), normaliza descrições
e usa fuzzy matching pra agrupar itens similares cross-projeto.

Produz:
- base/itens-normalizados.json  — catálogo unificado
- base/itens-canonicos.json     — mapeamento descricao_raw → chave canônica

Algoritmo:
1. Canonicalizar: lowercase, remover acentos, normalizar whitespace,
   remover números isolados, tokens comuns
2. Gerar chave hash das top palavras-chave
3. Fuzzy match (SequenceMatcher) agrupa variações
4. Cluster final: {chave_canonica: {descricao_representativa, n_occurencias, slugs}}
"""
from __future__ import annotations

import json
import re
import time
import unicodedata
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
ITENS_DIR = BASE / "itens-detalhados"
OUT_NORM = BASE / "itens-normalizados.json"
OUT_CANON = BASE / "itens-canonicos.json"
OUT_PUS = BASE / "itens-pus-agregados.json"


STOPWORDS = {
    "de", "da", "do", "e", "em", "para", "com", "no", "na", "dos", "das",
    "uma", "um", "ou", "por", "ao", "aos", "a", "o", "as", "os",
    "kg", "m", "m2", "m3", "mm", "cm", "un", "und", "gl", "vb", "pç", "pc",
    "incluindo", "conforme", "com", "sem",
}

FUZZY_THRESHOLD = 0.85


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def canonicalize(desc: str) -> str:
    if not desc:
        return ""
    s = strip_accents(desc.lower())
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\b\d+[,\.]?\d*\b", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    tokens = [t for t in s.split() if t not in STOPWORDS and len(t) > 1]
    return " ".join(tokens[:10])


def first_word_key(canon: str) -> str:
    toks = canon.split()
    if not toks:
        return "__empty__"
    return toks[0][:12]


def main():
    t0 = time.time()
    print("loading itens-detalhados...")
    all_items = []
    for jp in sorted(ITENS_DIR.glob("*.json")):
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        slug = jp.stem
        for aba in d.get("abas", []):
            for it in aba.get("itens", []):
                desc = it.get("descricao")
                if not desc or not isinstance(desc, str) or len(desc) < 4:
                    continue
                canon = canonicalize(desc)
                if not canon or len(canon) < 3:
                    continue
                all_items.append({
                    "slug": slug,
                    "aba": aba.get("nome", ""),
                    "desc": desc.strip()[:200],
                    "canon": canon[:200],
                    "un": it.get("unidade"),
                    "qtd": it.get("qtd"),
                    "pu": it.get("pu"),
                    "total": it.get("total"),
                })
    print(f"  {len(all_items)} itens lidos em {time.time()-t0:.1f}s")

    print("\nagrupando por primeira palavra...")
    t1 = time.time()
    by_first: dict[str, list] = defaultdict(list)
    for it in all_items:
        by_first[first_word_key(it["canon"])].append(it)
    print(f"  {len(by_first)} buckets em {time.time()-t1:.1f}s")
    print(f"  top 10 buckets: {sorted([(k, len(v)) for k, v in by_first.items()], key=lambda x: -x[1])[:10]}")

    print("\nfuzzy clustering dentro de cada bucket...")
    t2 = time.time()

    clusters: list[dict] = []

    for first_word, items in by_first.items():
        if len(items) < 2:
            continue

        bucket_clusters: list[dict] = []
        for it in items:
            best_score = 0
            best_cluster = None
            for c in bucket_clusters:
                score = SequenceMatcher(None, it["canon"], c["canon_ref"]).ratio()
                if score > best_score:
                    best_score = score
                    best_cluster = c
            if best_cluster and best_score >= FUZZY_THRESHOLD:
                best_cluster["items"].append(it)
                best_cluster["n"] += 1
                if it["slug"] not in best_cluster["slugs"]:
                    best_cluster["slugs"].append(it["slug"])
            else:
                bucket_clusters.append({
                    "canon_ref": it["canon"],
                    "desc_representativa": it["desc"],
                    "items": [it],
                    "n": 1,
                    "slugs": [it["slug"]],
                })
        clusters.extend(bucket_clusters)

    clusters.sort(key=lambda c: -c["n"])
    print(f"  {len(clusters)} clusters criados em {time.time()-t2:.1f}s")
    print(f"  top 10 clusters por ocorrência:")
    for c in clusters[:10]:
        print(f"    {c['n']:>5}x  {c['desc_representativa'][:60]:<60}  ({len(c['slugs'])} projetos)")

    print("\nsalvando...")
    catalog = {
        "n_clusters": len(clusters),
        "n_items_raw": len(all_items),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "clusters": [
            {
                "id": i,
                "canon_ref": c["canon_ref"],
                "desc_representativa": c["desc_representativa"],
                "n_ocorrencias": c["n"],
                "n_projetos": len(c["slugs"]),
                "slugs": c["slugs"][:20],
                "unidades_observadas": list(set(it["un"] for it in c["items"] if it.get("un")))[:5],
            }
            for i, c in enumerate(clusters[:5000])
        ],
    }
    OUT_NORM.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")

    canonico = {}
    for i, c in enumerate(clusters):
        for it in c["items"]:
            key = f"{it['slug']}::{it['desc'][:80]}"
            canonico[key] = {"cluster_id": i, "canon_ref": c["canon_ref"]}

    OUT_CANON.write_text(json.dumps(canonico, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\naggregating PUs by cluster...")
    t3 = time.time()
    import statistics
    pus_agg = []
    for i, c in enumerate(clusters[:3000]):
        pus = [float(it["pu"]) for it in c["items"]
               if it.get("pu") and isinstance(it["pu"], (int, float)) and it["pu"] > 0]
        if not pus:
            continue
        pus_agg.append({
            "cluster_id": i,
            "desc": c["desc_representativa"][:100],
            "n_projetos": len(c["slugs"]),
            "n_observacoes": len(pus),
            "pu_min": min(pus),
            "pu_p25": statistics.quantiles(pus, n=4)[0] if len(pus) >= 4 else min(pus),
            "pu_mediana": statistics.median(pus),
            "pu_p75": statistics.quantiles(pus, n=4)[2] if len(pus) >= 4 else max(pus),
            "pu_max": max(pus),
            "pu_media": statistics.mean(pus),
            "pu_cv": (statistics.stdev(pus) / statistics.mean(pus)) if len(pus) > 1 and statistics.mean(pus) > 0 else 0,
        })
    pus_agg.sort(key=lambda x: -x["n_observacoes"])
    OUT_PUS.write_text(
        json.dumps({"n_clusters": len(pus_agg), "generated_at": datetime.now().isoformat(timespec="seconds"),
                    "pus_agregados": pus_agg}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\ndone in {time.time() - t0:.1f}s")
    print(f"  clusters: {len(clusters)}")
    print(f"  PUs agregados: {len(pus_agg)}")
    print(f"  top 5 PUs mais observados:")
    for p in pus_agg[:5]:
        print(f"    {p['n_observacoes']:>4}x {p['desc'][:50]:<50} med={p['pu_mediana']:.2f} cv={p['pu_cv']*100:.0f}%")
    print(f"\nsaidas:")
    print(f"  {OUT_NORM}")
    print(f"  {OUT_CANON}")
    print(f"  {OUT_PUS}")


if __name__ == "__main__":
    main()
