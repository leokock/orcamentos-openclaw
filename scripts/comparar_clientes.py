#!/usr/bin/env python3
"""Phase 20k — Comparador de 2 clientes: estrutura detalhada.

Compara distribuicao % MG, PUs, esquadrias, estrutural, qualitativa.

Uso:
    python scripts/comparar_clientes.py --a paludo --b nova-empreendimentos
    python scripts/comparar_clientes.py --a paludo --b nova --output base/comparacao.md

Saida:
    base/comparacoes-clientes/{a}-vs-{b}.json
    base/comparacoes-clientes/{a}-vs-{b}.md
"""
from __future__ import annotations

import argparse
import json
import statistics
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
IDX_DIR = BASE / "indices-executivo"
OUT_DIR = BASE / "comparacoes-clientes"
OUT_DIR.mkdir(parents=True, exist_ok=True)


MG_CANON = [
    ("Gerenciamento", ["gerenciamento", "ger. tec", "ger tec", "gerenciament"]),
    ("Mov Terra", ["mov", "terra", "terraplan"]),
    ("Infraestrutura", ["infraestrutura", "fundac", "contenc", "estaca", "baldram"]),
    ("Supraestrutura", ["supraestrutura", "estrutura de concreto"]),
    ("Alvenaria", ["alvenaria", "vedac", "divisori"]),
    ("Impermeabilizacao", ["impermeab", "tratament"]),
    ("Hidrossanitaria", ["hidros", "hidraul", "drenagem"]),
    ("Eletrica", ["eletric", "telefon", "logic", "comunica", "automaca"]),
    ("Preventiva", ["preventiv", "pci", "spda", "glp"]),
    ("Instal Geral", ["instalac"]),
    ("Climatizacao", ["climat", "exaust"]),
    ("Rev Parede", ["rev. int. parede", "rev.int.parede", "revestimentos internos em paredes",
                    "revestimentos internos de parede", "revestimentos argamassados parede",
                    "acabamentos em parede", "acabamentos internos em parede", "revestimentos ceramicos"]),
    ("Rev Teto", ["teto", "forro"]),
    ("Pisos", ["piso", "pavimenta", "contrapiso"]),
    ("Pint Interna", ["pintura interna"]),
    ("Pintura Geral", ["pintura", "pinturas"]),
    ("Esquadrias", ["esquadri", "vidro", "ferragen"]),
    ("Loucas", ["louc", "metai"]),
    ("Fachada", ["fachada", "pintura externa"]),
    ("Cobertura", ["cobertura"]),
    ("Sist Especiais", ["especia", "equipament"]),
    ("Complementares", ["complementa", "imprevisto", "contingenc"]),
]


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def canonize(raw):
    r = norm(raw).strip().lstrip("0123456789. ")
    for canon, kws in MG_CANON:
        for kw in kws:
            if kw in r:
                return canon
    return "Outros"


def load_cliente(prefixo):
    projs = []
    pn = norm(prefixo)
    for f in sorted(IDX_DIR.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        slug = d.get("projeto") or f.stem
        if norm(slug).startswith(pn):
            projs.append(d)
    return projs


def stats_mg_pct(projs):
    por_mg = defaultdict(list)
    for d in projs:
        total = d.get("total") or 0
        if not total:
            continue
        vals = defaultdict(float)
        for k, v in (d.get("macrogrupos") or {}).items():
            val = v.get("valor") if isinstance(v, dict) else (v or 0)
            if val and val > 0:
                vals[canonize(k)] += val
        for c, v in vals.items():
            por_mg[c].append(v / total * 100)
    return {k: round(statistics.median(v), 2) for k, v in por_mg.items() if v}


def stats_pus(projs):
    pus = defaultdict(list)
    for d in projs:
        ap = d.get("acabamentos_pus") or {}
        for k, v in ap.items():
            if v and isinstance(v, (int, float)) and v > 0:
                pus[k].append(v)
    return {k: {"n": len(v), "mediana": round(statistics.median(v), 2)} for k, v in pus.items()}


def stats_estruturais(projs):
    agr = defaultdict(list)
    for d in projs:
        ie = d.get("indices_estruturais") or {}
        ac = d.get("ac") or 0
        if ie.get("concreto_m3_por_m2_ac"):
            agr["concreto_m3_por_m2_ac"].append(ie["concreto_m3_por_m2_ac"])
        if ie.get("aco_kg_por_m3_concreto"):
            agr["taxa_aco_kg_por_m3"].append(ie["aco_kg_por_m3_concreto"])
        if ie.get("aco_total_kg") and ac > 0:
            agr["aco_kg_por_m2_ac"].append(ie["aco_total_kg"] / ac)
        if ie.get("forma_m2_por_m2_ac"):
            agr["forma_m2_por_m2_ac"].append(ie["forma_m2_por_m2_ac"])
    return {k: {"n": len(v), "mediana": round(statistics.median(v), 4)} for k, v in agr.items()}


def stats_qualitativa(projs):
    cats = Counter()
    alertas = []
    revisoes = []
    fora_curva = []
    padroes = Counter()
    for d in projs:
        q = d.get("qualitative", {}) or {}
        slug = d.get("projeto", "")
        for obs in q.get("observacoes_orcamentista") or []:
            if isinstance(obs, dict):
                cat = obs.get("categoria", "sem_cat")
                cats[cat] += 1
                if cat == "alerta":
                    alertas.append({"slug": slug, "contexto": obs.get("contexto", ""),
                                    "observacao": obs.get("observacao", "")[:250]})
                elif cat == "revisao":
                    revisoes.append({"slug": slug, "contexto": obs.get("contexto", ""),
                                     "observacao": obs.get("observacao", "")[:250]})
        for fc in q.get("fora_da_curva") or []:
            if isinstance(fc, dict):
                fora_curva.append({"slug": slug, "item": fc.get("item", "")[:60],
                                   "motivo": fc.get("motivo", "")[:250]})
        for pat in q.get("padroes_identificados") or []:
            if isinstance(pat, str):
                padroes[pat[:80]] += 1
    return {
        "categorias": dict(cats),
        "alertas": alertas,
        "revisoes": revisoes,
        "fora_curva": fora_curva,
        "padroes_top10": dict(padroes.most_common(10)),
    }


def comparar(cli_a_nome, prefixo_a, cli_b_nome, prefixo_b):
    proj_a = load_cliente(prefixo_a)
    proj_b = load_cliente(prefixo_b)

    def base_info(projs):
        rsm2s = [p.get("rsm2") for p in projs if p.get("rsm2")]
        acs = [p.get("ac") for p in projs if p.get("ac")]
        totals = [p.get("total") for p in projs if p.get("total")]
        n_itens = [p.get("qualitative", {}).get("phase1_extraction", {}).get("total_itens", 0) for p in projs]
        return {
            "n_projetos": len(projs),
            "projetos": [p.get("projeto") for p in projs],
            "rsm2_mediana": round(statistics.median(rsm2s), 2) if rsm2s else None,
            "ac_total": sum(acs),
            "ac_mediana": round(statistics.median(acs), 0) if acs else None,
            "total_acumulado_r$": sum(totals),
            "total_mediana_r$": round(statistics.median(totals), 0) if totals else None,
            "n_itens_mediana": round(statistics.median(n_itens), 0) if n_itens else None,
        }

    return {
        "data": datetime.now().isoformat(timespec="seconds"),
        "cliente_a": {
            "nome": cli_a_nome,
            "info": base_info(proj_a),
            "dist_mg_pct": stats_mg_pct(proj_a),
            "pus": stats_pus(proj_a),
            "estruturais": stats_estruturais(proj_a),
            "qualitativa": stats_qualitativa(proj_a),
        },
        "cliente_b": {
            "nome": cli_b_nome,
            "info": base_info(proj_b),
            "dist_mg_pct": stats_mg_pct(proj_b),
            "pus": stats_pus(proj_b),
            "estruturais": stats_estruturais(proj_b),
            "qualitativa": stats_qualitativa(proj_b),
        },
    }


def gerar_md(r, out_path):
    a = r["cliente_a"]
    b = r["cliente_b"]
    na = a["nome"]
    nb = b["nome"]
    lines = [f"# Comparativo: {na} vs {nb}", "", f"**Gerado:** {r['data']}", ""]

    # Sumario
    lines += ["## Sumario executivo", "", "| Metrica | " + na + " | " + nb + " | Delta |", "|---|---:|---:|---:|"]
    ai = a["info"]; bi = b["info"]
    def row(metric, va, vb, fmt=None):
        if va is not None and vb is not None and isinstance(va, (int, float)) and isinstance(vb, (int, float)):
            delta = vb - va
            delta_pct = (delta / va * 100) if va else 0
            if fmt == "rs":
                lines.append(f"| {metric} | R$ {va:,.0f} | R$ {vb:,.0f} | {delta_pct:+.1f}% |")
            else:
                lines.append(f"| {metric} | {va:,.0f} | {vb:,.0f} | {delta_pct:+.1f}% |")
        else:
            lines.append(f"| {metric} | {va} | {vb} | — |")
    row("N projetos", ai["n_projetos"], bi["n_projetos"])
    row("AC total (m²)", ai["ac_total"], bi["ac_total"])
    row("AC mediana (m²)", ai["ac_mediana"], bi["ac_mediana"])
    row("Total acumulado", ai["total_acumulado_r$"], bi["total_acumulado_r$"], "rs")
    row("R$/m² mediana", ai["rsm2_mediana"], bi["rsm2_mediana"], "rs")
    row("N itens/projeto (med)", ai["n_itens_mediana"], bi["n_itens_mediana"])
    lines.append("")

    # Distribuicao MG
    lines += ["## Distribuicao % Macrogrupo (mediana)", "", f"| MG | {na} % | {nb} % | Diff pp |", "|---|---:|---:|---:|"]
    all_mgs = set(a["dist_mg_pct"].keys()) | set(b["dist_mg_pct"].keys())
    rows_mg = [(mg, a["dist_mg_pct"].get(mg, 0), b["dist_mg_pct"].get(mg, 0)) for mg in all_mgs]
    rows_mg.sort(key=lambda x: -abs(x[2] - x[1]))
    for mg, va, vb in rows_mg:
        diff = vb - va
        lines.append(f"| {mg} | {va:.1f}% | {vb:.1f}% | {diff:+.1f}pp |")
    lines.append("")

    # Indices estruturais
    lines += ["## Indices estruturais", "", f"| Indicador | {na} | {nb} |", "|---|---:|---:|"]
    all_e = set(a["estruturais"].keys()) | set(b["estruturais"].keys())
    for k in sorted(all_e):
        av = a["estruturais"].get(k, {})
        bv = b["estruturais"].get(k, {})
        lines.append(f"| {k} | {av.get('mediana', '-')} (n={av.get('n', 0)}) | {bv.get('mediana', '-')} (n={bv.get('n', 0)}) |")
    lines.append("")

    # PUs
    lines += ["## Preços unitários acabamentos", "", f"| PU | {na} | {nb} |", "|---|---:|---:|"]
    all_pus = set(a["pus"].keys()) | set(b["pus"].keys())
    for k in sorted(all_pus):
        av = a["pus"].get(k, {})
        bv = b["pus"].get(k, {})
        amed = f"R$ {av['mediana']:,.2f} (n={av['n']})" if av else "—"
        bmed = f"R$ {bv['mediana']:,.2f} (n={bv['n']})" if bv else "—"
        lines.append(f"| {k} | {amed} | {bmed} |")
    lines.append("")

    # Qualitativa
    for grupo, cd in [(na, a), (nb, b)]:
        q = cd["qualitativa"]
        lines += [f"## Qualitativa — {grupo}", "",
                  f"- **Categorias de observações:** {q['categorias']}",
                  f"- **Total:** {len(q['alertas'])} alertas, {len(q['revisoes'])} revisões, {len(q['fora_curva'])} fora-da-curva",
                  ""]
        if q["alertas"]:
            lines.append("**Alertas:**")
            for x in q["alertas"][:5]:
                lines.append(f"- `{x['slug']}` | {x['contexto']}: {x['observacao']}")
            lines.append("")
        if q["revisoes"]:
            lines.append("**Revisões:**")
            for x in q["revisoes"][:5]:
                lines.append(f"- `{x['slug']}` | {x['contexto']}: {x['observacao']}")
            lines.append("")
        if q["fora_curva"]:
            lines.append("**Fora da curva:**")
            for x in q["fora_curva"][:10]:
                lines.append(f"- `{x['slug']}` | {x['item']} -> {x['motivo']}")
            lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="prefixo do cliente A (ex: paludo)")
    ap.add_argument("--b", required=True, help="prefixo do cliente B (ex: nova-empreendimentos)")
    ap.add_argument("--nome-a", default=None)
    ap.add_argument("--nome-b", default=None)
    ap.add_argument("--output", default=None)
    args = ap.parse_args()

    na = args.nome_a or args.a.title()
    nb = args.nome_b or args.b.title()
    r = comparar(na, args.a, nb, args.b)

    out_json = OUT_DIR / f"{args.a}-vs-{args.b}.json"
    out_json.write_text(json.dumps(r, indent=2, ensure_ascii=False), encoding="utf-8")
    out_md = Path(args.output) if args.output else OUT_DIR / f"{args.a}-vs-{args.b}.md"
    gerar_md(r, out_md)
    print(f"Salvo: {out_json}", flush=True)
    print(f"Salvo: {out_md}", flush=True)


if __name__ == "__main__":
    main()
