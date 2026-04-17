#!/usr/bin/env python3
"""Phase 20b — Agrega indicadores de produto cross-projeto.

Lê indicadores-produto/{slug}.json (126 projetos) e calcula
estatísticas percentis para cada indicador, globais e por padrão.

Saída: base/indicadores-produto-agregados.json

Uso:
    python scripts/agregar_indicadores_produto.py
"""
from __future__ import annotations

import json
import statistics
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
IND_DIR = BASE / "indicadores-produto"
OUT = BASE / "indicadores-produto-agregados.json"


def _load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def stats(values):
    vs = [v for v in values if isinstance(v, (int, float)) and v > 0]
    if not vs:
        return None
    vs.sort()
    n = len(vs)
    return {
        "n": n,
        "min": round(vs[0], 4),
        "p10": round(vs[int(n * 0.1)], 4) if n > 10 else round(vs[0], 4),
        "p25": round(vs[int(n * 0.25)], 4) if n > 4 else round(vs[0], 4),
        "mediana": round(statistics.median(vs), 4),
        "media": round(statistics.mean(vs), 4),
        "p75": round(vs[int(n * 0.75)], 4) if n > 4 else round(vs[-1], 4),
        "p90": round(vs[int(n * 0.9)], 4) if n > 10 else round(vs[-1], 4),
        "max": round(vs[-1], 4),
        "dp": round(statistics.stdev(vs), 4) if n > 1 else 0,
        "cv": round(statistics.stdev(vs) / statistics.mean(vs), 3) if n > 1 and statistics.mean(vs) > 0 else 0,
    }


def main():
    print("Loading project indicators...")
    projetos = []
    for jp in sorted(IND_DIR.glob("*.json")):
        d = _load_json(jp)
        if d:
            projetos.append(d)
    print(f"  {len(projetos)} projects loaded")

    all_indicator_names = set()
    for p in projetos:
        all_indicator_names.update(p.get("indicadores", {}).keys())
    all_indicator_names = sorted(all_indicator_names)
    print(f"  {len(all_indicator_names)} unique indicators found")

    padroes = sorted(set(p.get("padrao", "desconhecido") for p in projetos))
    print(f"  Padroes: {padroes}")

    print("\nComputing global stats...")
    indicadores_globais = {}
    for ind_name in all_indicator_names:
        values = []
        projetos_com = []
        for p in projetos:
            ind = p.get("indicadores", {}).get(ind_name)
            if ind and ind.get("valor") is not None:
                values.append(ind["valor"])
                projetos_com.append(p["slug"])
        s = stats(values)
        if s:
            s["projetos_fonte"] = projetos_com
            indicadores_globais[ind_name] = s
            print(f"  {ind_name:<45} n={s['n']:>3}  med={s['mediana']:>10.4f}  cv={s['cv']:.3f}")

    print("\nComputing stats per padrao...")
    indicadores_por_padrao = {}
    for padrao in padroes:
        projs_padrao = [p for p in projetos if p.get("padrao") == padrao]
        if not projs_padrao:
            continue
        indicadores_por_padrao[padrao] = {"n_projetos": len(projs_padrao), "indicadores": {}}
        for ind_name in all_indicator_names:
            values = [
                p["indicadores"][ind_name]["valor"]
                for p in projs_padrao
                if ind_name in p.get("indicadores", {}) and p["indicadores"][ind_name].get("valor") is not None
            ]
            s = stats(values)
            if s:
                indicadores_por_padrao[padrao]["indicadores"][ind_name] = s

        n_ind = len(indicadores_por_padrao[padrao]["indicadores"])
        print(f"  {padrao:<15} {len(projs_padrao):>3} projetos, {n_ind} indicadores")

    print("\nBuilding project matrix...")
    projeto_matrix = []
    for p in projetos:
        row = {
            "slug": p["slug"],
            "padrao": p.get("padrao", ""),
            "ac_m2": p.get("ac_m2", 0),
            "ur": p.get("ur", 0),
            "n_indicadores": p.get("n_indicadores_extraidos", 0),
        }
        for ind_name in all_indicator_names:
            ind = p.get("indicadores", {}).get(ind_name)
            row[ind_name] = ind["valor"] if ind else None
        projeto_matrix.append(row)

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos_total": len(projetos),
        "n_indicadores_unicos": len(all_indicator_names),
        "padroes": padroes,
        "nomes_indicadores": all_indicator_names,
        "indicadores_globais": indicadores_globais,
        "indicadores_por_padrao": indicadores_por_padrao,
        "projeto_matrix": projeto_matrix,
    }

    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT}")
    print(f"  {len(indicadores_globais)} indicadores globais")
    print(f"  {len(indicadores_por_padrao)} padroes")


if __name__ == "__main__":
    main()
