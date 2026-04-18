#!/usr/bin/env python3
"""Phase 20e — Analise financeira dos orcamentos executivos.

Gera analises cross-projeto a partir de indices-executivo/*.json:
- Distribuicao % de custo por macrogrupo x padrao (Curva S)
- Split MO x Material por MG x padrao
- Custo Indireto (CI) / Total por padrao
- Regressao R$/m² em funcao de AC, UR, padrao
- Top/bottom quartil de eficiencia por padrao
- Fachada: envidracada vs convencional
- Sistemas especiais: elevador PU x n_torres/pavimentos
- Instalacoes eletricas/hidro rsm2 cross-padrao

Saidas:
- base/analise-financeira-agregada.json
- base/analise-financeira-cartesian.xlsx
- base/ANALISE-FINANCEIRA-RESUMO.md

Uso: python scripts/analise_financeira_executivos.py
"""
from __future__ import annotations

import json
import math
import statistics
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
IDX_DIR = BASE / "indices-executivo"
PAD_FILE = BASE / "padroes-classificados-consolidado.json"
OUT_JSON = BASE / "analise-financeira-agregada.json"
OUT_XLSX = BASE / "analise-financeira-cartesian.xlsx"
OUT_MD = BASE / "ANALISE-FINANCEIRA-RESUMO.md"

# ─── Canonicalizacao de macrogrupos ─────────────────────────────────
# Os 147 nomes variados mapeiam pra ~18 MG canonicos
MG_CANON = [
    ("Gerenciamento", ["gerenciamento", "ger. tec", "ger tec", "gerenciament"]),
    ("Movimentacao de Terra", ["mov", "terra", "terraplan", "movimenta"]),
    ("Infraestrutura", ["infraestrutura", "fundac", "contenc", "estaca", "baldram"]),
    ("Supraestrutura", ["supraestrutura", "estrutura de concreto"]),
    ("Alvenaria", ["alvenaria", "vedac", "divisori"]),
    ("Impermeabilizacao", ["impermeab", "tratament"]),
    ("Instalacoes Hidrossanitarias", ["hidros", "hidraul", "drenagem"]),
    ("Instalacoes Eletricas", ["eletric", "telefon", "logic", "comunica", "automaca"]),
    ("Instalacoes Preventivas", ["preventiv", "pci", "spda", "glp"]),
    ("Instalacoes Gerais", ["instalac", "instalações"]),
    ("Climatizacao", ["climat", "exaust", "ar condic"]),
    ("Revestimentos Parede", ["rev. int. parede", "rev.int.parede", "rev int parede",
                              "revestimentos internos em paredes", "reboco interno",
                              "revestimentos internos de parede", "revestimentos e acabamentos internos em parede",
                              "revestimentos argamassados parede", "acabamentos em parede",
                              "acabamentos internos em parede", "revestimentos ceramicos",
                              "rev. int parede", "rev parede"]),
    ("Revestimentos Teto", ["teto", "forro"]),
    ("Pisos e Pavimentacoes", ["piso", "pavimenta", "contrapiso"]),
    ("Pintura Interna", ["pintura interna", "sistemas de pintura interna"]),
    ("Pintura Geral", ["pintura", "pinturas", "sistema de pintura"]),
    ("Esquadrias", ["esquadri", "vidro", "ferragen"]),
    ("Loucas e Metais", ["louc", "metai"]),
    ("Fachada", ["fachada", "pintura externa", "pintura de fachada"]),
    ("Cobertura", ["cobertura"]),
    ("Sistemas Especiais", ["especia", "equipament", "outros sistemas"]),
    ("Servicos Complementares", ["complementa", "imprevisto", "contingenc"]),
]


def norm(s: str) -> str:
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def canonize_mg(raw: str) -> str:
    r = norm(raw).strip().lstrip("0123456789. ")
    for canon, keywords in MG_CANON:
        for kw in keywords:
            if kw in r:
                return canon
    return "Outros"


def _load(p: Path) -> dict:
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


AC_MIN_VALIDO = 1000  # abaixo disso, AC provavelmente é só 1 UR (R$/m² explode)
RSM2_MAX_VALIDO = 10000  # acima disso, provavelmente AC errado


def load_projects() -> list:
    """Carrega todos os projetos com seus dados executivos + padrão."""
    pad = _load(PAD_FILE)
    pad_map = {p["projeto"]: p for p in pad.get("projetos", []) if p.get("projeto")}

    projs = []
    for f in sorted(IDX_DIR.glob("*.json")):
        d = _load(f)
        slug = d.get("projeto") or f.stem
        pi = pad_map.get(slug, {})
        ac = d.get("ac") or 0
        rsm2 = d.get("rsm2") or 0
        # Flag de validade: AC minima + rsm2 em faixa razoavel
        ac_valid = ac >= AC_MIN_VALIDO
        rsm2_valid = 500 <= rsm2 <= RSM2_MAX_VALIDO if rsm2 else False
        projs.append({
            "slug": slug,
            "ac": ac,
            "ur": d.get("ur") or 0,
            "total": d.get("total") or 0,
            "rsm2": rsm2,
            "ac_valid": ac_valid,
            "rsm2_valid": rsm2_valid,
            "padrao": pi.get("padrao", "desconhecido"),
            "macrogrupos": d.get("macrogrupos") or {},
            "disciplinas": d.get("disciplinas") or {},
            "split": d.get("split_mo_material") or {},
            "ci": d.get("ci_detalhado") or {},
            "fachada": d.get("fachada_detail") or {},
            "sist_esp": d.get("sistemas_especiais_detail") or {},
            "instal": d.get("instalacoes_breakdown") or {},
            "esq": d.get("esquadrias_detail") or {},
            "ac_pus": d.get("acabamentos_pus") or {},
            "lm": d.get("loucas_metais_detail") or {},
        })
    return projs


def distribuicao_mg_por_padrao(projs: list) -> dict:
    """% de cada MG no total, agregado por padrao."""
    por_padrao = defaultdict(lambda: defaultdict(list))
    for p in projs:
        if not p["total"] or p["total"] <= 0:
            continue
        canon_vals = defaultdict(float)
        for mg_raw, info in p["macrogrupos"].items():
            if isinstance(info, dict):
                v = info.get("valor") or 0
            else:
                v = info or 0
            if v > 0:
                canon_vals[canonize_mg(mg_raw)] += v
        for canon, v in canon_vals.items():
            pct = v / p["total"] * 100
            por_padrao[p["padrao"]][canon].append(pct)

    # Stats por padrão
    out = {}
    for padrao, mgs in por_padrao.items():
        out[padrao] = {}
        for canon, pcts in mgs.items():
            s = stats(pcts)
            if s:
                out[padrao][canon] = s
    return out


def rsm2_por_mg_por_padrao(projs: list) -> dict:
    """R$/m² de cada MG canônico por padrão."""
    por_padrao = defaultdict(lambda: defaultdict(list))
    for p in projs:
        if not p["ac_valid"]:
            continue
        canon_vals = defaultdict(float)
        for mg_raw, info in p["macrogrupos"].items():
            if isinstance(info, dict):
                v = info.get("valor") or 0
            else:
                v = info or 0
            if v > 0:
                canon_vals[canonize_mg(mg_raw)] += v
        for canon, v in canon_vals.items():
            por_padrao[p["padrao"]][canon].append(v / p["ac"])

    out = {}
    for padrao, mgs in por_padrao.items():
        out[padrao] = {}
        for canon, vals in mgs.items():
            s = stats(vals)
            if s:
                out[padrao][canon] = s
    return out


def split_mo_material(projs: list) -> dict:
    """% MO e % Material por disciplina canônica, por padrão."""
    por_padrao = defaultdict(lambda: defaultdict(lambda: {"mo": [], "mat": []}))
    for p in projs:
        for mg_raw, info in p["split"].items():
            if not isinstance(info, dict):
                continue
            mo = info.get("mo_pct")
            mat = info.get("material_pct")
            if mo is None and mat is None:
                continue
            canon = canonize_mg(mg_raw)
            if mo is not None:
                por_padrao[p["padrao"]][canon]["mo"].append(mo * 100 if mo <= 1 else mo)
            if mat is not None:
                por_padrao[p["padrao"]][canon]["mat"].append(mat * 100 if mat <= 1 else mat)

    out = {}
    for padrao, mgs in por_padrao.items():
        out[padrao] = {}
        for canon, d in mgs.items():
            mo_s = stats(d["mo"]) if d["mo"] else None
            mat_s = stats(d["mat"]) if d["mat"] else None
            if mo_s or mat_s:
                out[padrao][canon] = {"mo_pct": mo_s, "material_pct": mat_s}
    return out


def custo_indireto_por_padrao(projs: list) -> dict:
    """CI/Total por padrão."""
    por_padrao = defaultdict(list)
    for p in projs:
        ci = p["ci"]
        tot = p["total"]
        if not ci or not tot or tot <= 0:
            continue
        ci_soma = 0
        for k, v in ci.items():
            if isinstance(v, dict):
                ci_soma += v.get("valor") or 0
            elif isinstance(v, (int, float)):
                ci_soma += v
        if ci_soma > 0:
            pct = ci_soma / tot * 100
            por_padrao[p["padrao"]].append({"slug": p["slug"], "pct": round(pct, 2), "ci_total": round(ci_soma, 2)})

    out = {}
    for pad, lst in por_padrao.items():
        if not lst:
            continue
        s = stats([x["pct"] for x in lst])
        if s:
            out[pad] = {"stats_pct": s, "amostras": lst}
    return out


def quartis_eficiencia(projs: list) -> dict:
    """Top/bottom quartil de R$/m² no mesmo padrão (menor = mais eficiente)."""
    por_padrao = defaultdict(list)
    for p in projs:
        if p["rsm2_valid"] and p["ac_valid"]:
            por_padrao[p["padrao"]].append((p["rsm2"], p["slug"], p["ac"], p["ur"]))

    out = {}
    for pad, lst in por_padrao.items():
        if len(lst) < 8:
            continue
        lst.sort()
        n = len(lst)
        q1 = n // 4
        top = [{"slug": s, "rsm2": round(r, 2), "ac": ac, "ur": ur} for r, s, ac, ur in lst[:q1]]
        bottom = [{"slug": s, "rsm2": round(r, 2), "ac": ac, "ur": ur} for r, s, ac, ur in lst[-q1:]]
        med = statistics.median([r for r, _, _, _ in lst])
        out[pad] = {
            "n_projetos": n,
            "mediana_rsm2": round(med, 2),
            "top_quartil_eficientes": top,  # menor R$/m²
            "bottom_quartil_caros": bottom,
            "ratio_caro_eficiente": round(bottom[-1]["rsm2"] / top[0]["rsm2"], 2) if top[0]["rsm2"] > 0 else None,
        }
    return out


def fachada_analysis(projs: list) -> dict:
    """Fachada envidracada vs convencional."""
    com_envidracada = []
    sem_envidracada = []
    for p in projs:
        if not p["ac"] or not p["fachada"]:
            continue
        # Detecta pele de vidro
        pele = 0
        conv = 0
        for k, v in p["fachada"].items():
            if not isinstance(v, dict):
                continue
            val = v.get("valor") or 0
            if "vidro" in norm(k) or "pele" in norm(k):
                pele += val
            else:
                conv += val
        total_fach = pele + conv
        if total_fach <= 0:
            continue
        rsm2 = total_fach / p["ac"]
        rec = {
            "slug": p["slug"], "padrao": p["padrao"], "ac": p["ac"],
            "fach_total": round(total_fach, 0),
            "fach_rsm2": round(rsm2, 2),
            "pele_pct": round(pele / total_fach * 100, 1) if total_fach else 0,
        }
        if pele > conv:
            com_envidracada.append(rec)
        else:
            sem_envidracada.append(rec)
    return {
        "com_envidracada": sorted(com_envidracada, key=lambda x: -x["fach_rsm2"]),
        "sem_envidracada": sorted(sem_envidracada, key=lambda x: -x["fach_rsm2"]),
        "stats_envidracada_rsm2": stats([x["fach_rsm2"] for x in com_envidracada]),
        "stats_convencional_rsm2": stats([x["fach_rsm2"] for x in sem_envidracada]),
    }


def sist_especiais(projs: list) -> dict:
    """Sistemas especiais: elevador qtd, PU, por escala."""
    elev = []
    gerador = []
    piscina = []
    for p in projs:
        s = p["sist_esp"]
        if not s:
            continue
        if s.get("elevadores"):
            e = s["elevadores"]
            if e.get("qtd") and e.get("pu_un"):
                elev.append({
                    "slug": p["slug"], "padrao": p["padrao"], "ac": p["ac"],
                    "qtd": e["qtd"], "pu_un": round(e["pu_un"], 0),
                    "valor": round(e.get("valor", 0), 0),
                })
        if s.get("gerador") and s["gerador"] and (isinstance(s["gerador"], dict) and s["gerador"].get("valor") or isinstance(s["gerador"], (int, float))):
            g = s["gerador"] if isinstance(s["gerador"], dict) else {"valor": s["gerador"]}
            gerador.append({
                "slug": p["slug"], "padrao": p["padrao"],
                "valor": round(g.get("valor", 0), 0),
            })
        if s.get("piscina"):
            pi = s["piscina"] if isinstance(s["piscina"], dict) else {"valor": s["piscina"]}
            if (pi.get("valor") or 0) > 0:
                piscina.append({
                    "slug": p["slug"], "padrao": p["padrao"],
                    "valor": round(pi.get("valor", 0), 0),
                })
    return {
        "elevadores": sorted(elev, key=lambda x: -x["pu_un"]),
        "elevador_pu_stats": stats([x["pu_un"] for x in elev]),
        "gerador_valor_stats": stats([x["valor"] for x in gerador]),
        "piscina_valor_stats": stats([x["valor"] for x in piscina]),
        "n_com_gerador": len(gerador),
        "n_com_piscina": len(piscina),
    }


def regressao_rsm2(projs: list) -> dict:
    """Regressao linear simples R$/m² = a + b*AC + c*UR + padrao dummies."""
    # Filtra projetos com dados completos
    valid = [p for p in projs if p["rsm2_valid"] and p["ac_valid"]]
    if len(valid) < 10:
        return {"error": "insuficiente"}

    # Correlacoes individuais
    xs_ac = [p["ac"] for p in valid]
    xs_ur = [p["ur"] for p in valid if p["ur"]]
    ys = [p["rsm2"] for p in valid]

    def pearson(xs, ys):
        if len(xs) != len(ys) or len(xs) < 2:
            return None
        mx, my = statistics.mean(xs), statistics.mean(ys)
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        dx = (sum((x - mx) ** 2 for x in xs)) ** 0.5
        dy = (sum((y - my) ** 2 for y in ys)) ** 0.5
        return num / (dx * dy) if dx > 0 and dy > 0 else None

    r_ac = pearson(xs_ac, ys)
    # Só UR: pareia com rsm2
    pairs_ur = [(p["ur"], p["rsm2"]) for p in valid if p["ur"] and p["ur"] > 0]
    r_ur = pearson([p[0] for p in pairs_ur], [p[1] for p in pairs_ur]) if len(pairs_ur) > 2 else None

    # Mediana por padrão (efeito categorico)
    por_pad = defaultdict(list)
    for p in valid:
        por_pad[p["padrao"]].append(p["rsm2"])
    mediana_por_pad = {k: round(statistics.median(v), 2) for k, v in por_pad.items()}

    return {
        "n_projetos": len(valid),
        "correlacao_rsm2_vs_ac": round(r_ac, 3) if r_ac is not None else None,
        "correlacao_rsm2_vs_ur": round(r_ur, 3) if r_ur is not None else None,
        "mediana_rsm2_por_padrao": mediana_por_pad,
        "interpretacao": {
            "ac_effect": ("Negativa: projetos maiores tendem a R$/m² menor (economia de escala)"
                         if r_ac is not None and r_ac < -0.2
                         else "Positiva: projetos maiores sao mais caros/m² (complexidade)"
                         if r_ac is not None and r_ac > 0.2
                         else "Neutra: escala nao afeta significativamente R$/m²"),
        },
    }


def instalacoes_breakdown(projs: list) -> dict:
    """Eletricas/Hidrossanitarias/Preventivas rsm2 por padrao."""
    por_padrao = defaultdict(lambda: defaultdict(list))
    for p in projs:
        if not p["instal"]:
            continue
        for k, info in p["instal"].items():
            if not isinstance(info, dict):
                continue
            rsm2 = info.get("rsm2")
            if rsm2 and rsm2 > 0:
                por_padrao[p["padrao"]][k].append(rsm2)

    out = {}
    for pad, disc in por_padrao.items():
        out[pad] = {}
        for k, vals in disc.items():
            s = stats(vals)
            if s:
                out[pad][k] = s
    return out


def top_projetos(projs: list) -> dict:
    """Top/Bottom geral."""
    with_rsm2 = [p for p in projs if p["rsm2_valid"] and p["ac_valid"]]
    with_rsm2.sort(key=lambda x: x["rsm2"])
    with_ac = [p for p in projs if p["ac"] and p["ac"] > 0]
    with_ac.sort(key=lambda x: -x["ac"])
    return {
        "top_10_mais_eficientes_rsm2": [{"slug": p["slug"], "padrao": p["padrao"], "rsm2": p["rsm2"], "ac": p["ac"]}
                                        for p in with_rsm2[:10]],
        "top_10_mais_caros_rsm2": [{"slug": p["slug"], "padrao": p["padrao"], "rsm2": p["rsm2"], "ac": p["ac"]}
                                    for p in with_rsm2[-10:][::-1]],
        "top_10_maiores_ac": [{"slug": p["slug"], "padrao": p["padrao"], "ac": p["ac"], "rsm2": p["rsm2"]}
                              for p in with_ac[:10]],
    }


def main():
    print("Loading projects...", flush=True)
    projs = load_projects()
    print(f"  {len(projs)} projects loaded", flush=True)

    print("Distribuicao % MG por padrao...", flush=True)
    dist_mg = distribuicao_mg_por_padrao(projs)

    print("R$/m2 por MG por padrao...", flush=True)
    rsm2_mg = rsm2_por_mg_por_padrao(projs)

    print("Split MO x Material...", flush=True)
    split_mo = split_mo_material(projs)

    print("Custo Indireto por padrao...", flush=True)
    ci = custo_indireto_por_padrao(projs)

    print("Quartis de eficiencia...", flush=True)
    quartis = quartis_eficiencia(projs)

    print("Fachada envidracada vs convencional...", flush=True)
    fachada = fachada_analysis(projs)

    print("Sistemas especiais...", flush=True)
    sist = sist_especiais(projs)

    print("Regressao R$/m²...", flush=True)
    regr = regressao_rsm2(projs)

    print("Instalacoes breakdown...", flush=True)
    instal = instalacoes_breakdown(projs)

    print("Top/bottom projetos...", flush=True)
    top = top_projetos(projs)

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len(projs),
        "n_com_total": sum(1 for p in projs if p["total"] > 0),
        "n_com_rsm2": sum(1 for p in projs if p["rsm2"] > 0),
        "distribuicao_mg_por_padrao": dist_mg,
        "rsm2_por_mg_por_padrao": rsm2_mg,
        "split_mo_material": split_mo,
        "custo_indireto_por_padrao": ci,
        "quartis_eficiencia": quartis,
        "fachada_analysis": fachada,
        "sistemas_especiais": sist,
        "regressao_rsm2": regr,
        "instalacoes_breakdown": instal,
        "top_bottom_projetos": top,
    }

    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT_JSON}", flush=True)
    print(f"  {len(dist_mg)} padroes na distribuicao MG", flush=True)
    print(f"  {len(quartis)} padroes com quartis", flush=True)
    print(f"  {len(fachada['com_envidracada'])} projetos com fachada envidracada, {len(fachada['sem_envidracada'])} convencional", flush=True)
    print(f"  {len(sist['elevadores'])} projetos com elevador PU", flush=True)
    print(f"  Regressao: n={regr.get('n_projetos')}, r_ac={regr.get('correlacao_rsm2_vs_ac')}", flush=True)


if __name__ == "__main__":
    main()
