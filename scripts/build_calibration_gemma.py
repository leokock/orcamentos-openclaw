#!/usr/bin/env python3
"""Fase 18b - Rebuild calibration-condicional-padrao.json usando labels Gemma.

Substitui a estratificacao por bucket rsm2 (proxy circular) pela
classificacao semantica Gemma (fase 18). Para cada classe
(economico/medio/medio-alto/alto/luxo), agrega medianas por macrogrupo
dos projetos que o Gemma classificou naquela classe E que tem ac+total
validos no indices-executivo.
"""
from __future__ import annotations

import json
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import consulta_similares as cs
from consulta_similares import CALIBRATION_KEY_TO_MG

BASE = Path.home() / "orcamentos-openclaw" / "base"
CONS = BASE / "padroes-classificados-consolidado.json"
IDX_DIR = BASE / "indices-executivo"
OUT = BASE / "calibration-condicional-padrao.json"


def stats_of(values):
    if not values:
        return None
    s = sorted(values)
    n = len(s)
    return {
        "n": n,
        "min": round(s[0], 2),
        "p10": round(s[int(n * 0.1)], 2),
        "p25": round(s[int(n * 0.25)], 2),
        "mediana": round(statistics.median(s), 2),
        "media": round(statistics.mean(s), 2),
        "p75": round(s[int(n * 0.75)], 2),
        "p90": round(s[min(int(n * 0.9), n - 1)], 2),
        "max": round(s[-1], 2),
    }


def main():
    cons = json.loads(CONS.read_text(encoding="utf-8"))
    slug_to_padrao = {
        p["projeto"]: p["padrao"] for p in cons["projetos"] if p["padrao"] != "insuficiente"
    }
    print(f"Projetos com label Gemma: {len(slug_to_padrao)}")
    print(f"Distribuição: {dict(Counter(slug_to_padrao.values()))}")

    projs_by_padrao: dict[str, list] = {
        k: [] for k in ["economico", "medio", "medio-alto", "alto", "luxo"]
    }
    for p in sorted(IDX_DIR.glob("*.json")):
        slug = p.stem
        padrao = slug_to_padrao.get(slug)
        if not padrao:
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not (d.get("ac") and d.get("total")):
            continue
        d["_slug"] = slug
        projs_by_padrao[padrao].append(d)

    print("\nProjetos com ac+total>0 por classe:")
    for k, v in projs_by_padrao.items():
        print(f"  {k:<12} {len(v)}")

    MG_LIST = list(CALIBRATION_KEY_TO_MG.values())
    per_class_mg = {}
    for classe, lst in projs_by_padrao.items():
        per_mg = {mg: [] for mg in MG_LIST}
        for pr in lst:
            try:
                vm = cs.valores_macrogrupos_v2([pr], pr["ac"])
                for mg, data in vm.items():
                    if mg in per_mg:
                        rsm2 = data.get("rsm2_mediano") or 0
                        if rsm2 > 0:
                            per_mg[mg].append(rsm2)
            except Exception:
                pass
        per_class_mg[classe] = {mg: stats_of(vs) for mg, vs in per_mg.items() if vs}

    print(f"\n{'='*70}")
    print("TOTAL R$/m² mediano por classe (Gemma labels)")
    print(f"{'='*70}")
    totals = {}
    for classe in ["economico", "medio", "medio-alto", "alto", "luxo"]:
        mgs = per_class_mg.get(classe, {})
        if not mgs:
            continue
        total = sum(s["mediana"] for s in mgs.values() if s)
        totals[classe] = round(total, 0)
        n_proj = len(projs_by_padrao[classe])
        print(f"\n### {classe.upper()} (n={n_proj} projetos, "
              f"{len(mgs)} MGs, total={total:,.0f} R$/m²)")
        for mg in [
            "Supraestrutura", "Esquadrias", "Pisos", "Pintura",
            "Sistemas Especiais", "Climatização", "Fachada", "Instalações"
        ]:
            s = mgs.get(mg)
            if s:
                print(f"  {mg:<22}  median={s['mediana']:>7,.0f}  n={s['n']:>3}")

    out = {
        "generated_at": cons["generated_at"],
        "fonte": "labels Gemma semantico (fase 18) cruzados com indices-executivo ac+total>0",
        "metodo": "gemma_semantic_labels (phase 18)",
        "n_projetos_por_classe": {k: len(v) for k, v in projs_by_padrao.items()},
        "total_rsm2_mediano_por_classe": totals,
        "por_padrao_mg": per_class_mg,
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nsaved: {OUT}")


if __name__ == "__main__":
    main()
