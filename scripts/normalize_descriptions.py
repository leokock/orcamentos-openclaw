#!/usr/bin/env python3
"""Phase 10 v2 — Normalização via hash de token-set.

Versão rápida: em vez de SequenceMatcher O(n²) por bucket, usa hash canônico
do conjunto de tokens-chave pra agrupar. Roda em ~30s vs dias do v1.

Algoritmo:
1. Canonicalizar descrição: lowercase, sem acento, sem números
2. Extrair top 3-5 tokens não-stopword mais longos
3. Ordenar tokens alfabeticamente e hashear
4. Descrições com mesmo hash = mesmo cluster

Saídas:
- base/itens-normalizados.json  — catálogo de clusters
- base/itens-pus-agregados.json — PUs por cluster
"""
from __future__ import annotations

import json
import re
import statistics
import time
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
ITENS_DIR = BASE / "itens-detalhados"
OUT_NORM = BASE / "itens-normalizados.json"
OUT_PUS = BASE / "itens-pus-agregados.json"


STOPWORDS = {
    "de", "da", "do", "e", "em", "para", "com", "no", "na", "dos", "das",
    "uma", "um", "ou", "por", "ao", "aos", "a", "o", "as", "os",
    "kg", "m", "m2", "m3", "mm", "cm", "un", "und", "gl", "vb", "pc", "pç",
    "incluindo", "conforme", "sem", "ate", "até",
    "total", "subtotal", "valor",
}


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def canonicalize(desc: str) -> str:
    if not desc:
        return ""
    s = strip_accents(desc.lower())
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\b\d+([,\.]\d+)?\b", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def token_hash_key(canon: str) -> str:
    """Retorna hash canônico das top 4 palavras mais longas (ordenadas)."""
    tokens = [t for t in canon.split() if t not in STOPWORDS and len(t) > 2]
    if not tokens:
        return ""
    tokens.sort(key=lambda t: -len(t))
    top = tokens[:4]
    top.sort()
    return "|".join(top)


VERBA_UNITS = {"vb", "vg", "gl", "global", "verba"}


def is_verba(it) -> bool:
    un = (it.get("unidade") or "").strip().lower()
    if un in VERBA_UNITS:
        return True
    qtd = it.get("qtd")
    if isinstance(qtd, (int, float)) and qtd == 1:
        pu = it.get("pu")
        total = it.get("total")
        if isinstance(pu, (int, float)) and isinstance(total, (int, float)):
            if pu > 1000 and abs(pu - total) < pu * 0.01:
                return True
    return False


def main():
    t0 = time.time()
    print("loading itens-detalhados...")
    all_items = []
    n_jsons = 0
    n_verbas_skipped = 0
    for jp in sorted(ITENS_DIR.glob("*.json")):
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            continue
        n_jsons += 1
        slug = jp.stem
        for aba in d.get("abas", []):
            for it in aba.get("itens", []):
                desc = it.get("descricao")
                if not desc or not isinstance(desc, str) or len(desc) < 4:
                    continue
                if is_verba(it):
                    n_verbas_skipped += 1
                    continue
                canon = canonicalize(desc)
                if not canon or len(canon) < 3:
                    continue
                key = token_hash_key(canon)
                if not key:
                    continue
                all_items.append({
                    "slug": slug,
                    "desc": desc.strip()[:200],
                    "key": key,
                    "un": it.get("unidade"),
                    "qtd": it.get("qtd"),
                    "pu": it.get("pu"),
                    "total": it.get("total"),
                })
    print(f"  {n_jsons} projetos, {len(all_items)} itens em {time.time()-t0:.1f}s  ({n_verbas_skipped} verbas filtradas)")

    print("\nagrupando por hash canônico...")
    t1 = time.time()
    clusters: dict[str, list] = defaultdict(list)
    for it in all_items:
        clusters[it["key"]].append(it)
    print(f"  {len(clusters)} clusters em {time.time()-t1:.1f}s")

    cluster_list = []
    for key, items in clusters.items():
        slugs = list({it["slug"] for it in items})
        repr_desc = max(items, key=lambda x: len(x["desc"]))["desc"]
        cluster_list.append({
            "key": key,
            "desc_representativa": repr_desc,
            "n_ocorrencias": len(items),
            "n_projetos": len(slugs),
            "slugs": sorted(slugs)[:30],
            "unidades_observadas": list({it["un"] for it in items if it.get("un")})[:5],
            "_items": items,
        })

    cluster_list.sort(key=lambda c: -c["n_ocorrencias"])

    print(f"\ntop 15 clusters por ocorrência:")
    for c in cluster_list[:15]:
        print(f"  {c['n_ocorrencias']:>5}x  {c['desc_representativa'][:70]:<70}  ({c['n_projetos']} projetos)")

    print("\naggregating PUs...")
    t2 = time.time()
    pus_agg = []
    for i, c in enumerate(cluster_list[:10000]):
        pus = [float(it["pu"]) for it in c["_items"]
               if it.get("pu") and isinstance(it["pu"], (int, float)) and it["pu"] > 0]
        if len(pus) < 3:
            continue
        pus.sort()
        mean = statistics.mean(pus)
        stdev = statistics.stdev(pus) if len(pus) > 1 else 0
        pus_agg.append({
            "cluster_id": i,
            "key": c["key"],
            "desc": c["desc_representativa"][:120],
            "n_projetos": c["n_projetos"],
            "n_observacoes": len(pus),
            "pu_min": round(pus[0], 2),
            "pu_p10": round(pus[int(len(pus)*0.1)], 2) if len(pus) >= 10 else round(pus[0], 2),
            "pu_p25": round(pus[int(len(pus)*0.25)], 2) if len(pus) >= 4 else round(pus[0], 2),
            "pu_mediana": round(statistics.median(pus), 2),
            "pu_p75": round(pus[int(len(pus)*0.75)], 2) if len(pus) >= 4 else round(pus[-1], 2),
            "pu_p90": round(pus[int(len(pus)*0.9)], 2) if len(pus) >= 10 else round(pus[-1], 2),
            "pu_max": round(pus[-1], 2),
            "pu_media": round(mean, 2),
            "cv": round(stdev / mean, 3) if mean > 0 else 0,
            "unidades": list({it["un"] for it in c["_items"] if it.get("un")})[:3],
        })
    pus_agg.sort(key=lambda x: -x["n_observacoes"])
    print(f"  {len(pus_agg)} PUs agregados com ≥3 obs em {time.time()-t2:.1f}s")

    print("\ntop 15 PUs mais observados:")
    for p in pus_agg[:15]:
        print(f"  {p['n_observacoes']:>4}x {p['desc'][:55]:<55} med=R${p['pu_mediana']:>9.2f} cv={p['cv']*100:>5.0f}%")

    OUT_NORM.write_text(
        json.dumps({
            "n_clusters": len(cluster_list),
            "n_itens_raw": len(all_items),
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "clusters": [{k: v for k, v in c.items() if k != "_items"} for c in cluster_list[:10000]],
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n{OUT_NORM} ({OUT_NORM.stat().st_size // 1024} KB)")

    OUT_PUS.write_text(
        json.dumps({
            "n_clusters_com_pu": len(pus_agg),
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "pus_agregados": pus_agg,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"{OUT_PUS} ({OUT_PUS.stat().st_size // 1024} KB)")

    print(f"\nTOTAL: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
