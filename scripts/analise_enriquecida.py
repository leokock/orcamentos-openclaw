#!/usr/bin/env python3
"""Fase 4 — Analise estratificada com metadados enriquecidos.

Usa projetos-enriquecidos.json (que tem cub_regiao + tipologia_canonica)
pra fazer analises que antes nao eram possiveis:

1. Benchmarks estratificados por (cub_regiao, padrao, tipologia)
2. Distribuicao % MG por combinacao
3. R$/m² por combinacao
4. Identificacao de clusters geograficos
5. Correlacoes controladas por regiao

Saida:
- base/analise-enriquecida-agregada.json
- analises-cross-projeto/benchmarks-estratificados/*.md
- analises-cross-projeto/benchmarks-estratificados/SUMARIO.md
"""
from __future__ import annotations

import json
import statistics
import unicodedata
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
ENR_FILE = BASE / "projetos-enriquecidos.json"
IDX_DIR = BASE / "indices-executivo"
OUT_JSON = BASE / "analise-enriquecida-agregada.json"
BENCH_DIR = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "benchmarks-estratificados"
BENCH_DIR.mkdir(parents=True, exist_ok=True)


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


MG_CANON = [
    ("Gerenciamento", ["gerenciamento", "ger. tec", "ger tec"]),
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


def canonize(raw):
    r = norm(raw).strip().lstrip("0123456789. ")
    for canon, kws in MG_CANON:
        for kw in kws:
            if kw in r:
                return canon
    return "Outros"


def stats(values):
    vs = [v for v in values if isinstance(v, (int, float)) and v > 0]
    if not vs:
        return None
    vs.sort()
    n = len(vs)
    return {
        "n": n,
        "min": round(vs[0], 4),
        "p25": round(vs[int(n * 0.25)], 4) if n > 4 else round(vs[0], 4),
        "mediana": round(statistics.median(vs), 4),
        "media": round(statistics.mean(vs), 4),
        "p75": round(vs[int(n * 0.75)], 4) if n > 4 else round(vs[-1], 4),
        "max": round(vs[-1], 4),
        "cv": round(statistics.stdev(vs) / statistics.mean(vs), 3) if n > 1 and statistics.mean(vs) > 0 else 0,
    }


def carregar_dados():
    enr = json.loads(ENR_FILE.read_text(encoding="utf-8"))
    projetos = enr["projetos"]
    # Carrega indices-executivo pra puxar macrogrupos
    mg_por_projeto = {}
    for p in projetos:
        slug = p["slug"]
        f = IDX_DIR / f"{slug}.json"
        if not f.exists():
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            mgs = d.get("macrogrupos") or {}
            if mgs:
                canon_vals = defaultdict(float)
                total = d.get("total") or 0
                for k, v in mgs.items():
                    val = v.get("valor") if isinstance(v, dict) else (v or 0)
                    if val and val > 0:
                        canon_vals[canonize(k)] += val
                if total > 0:
                    mg_por_projeto[slug] = {
                        "vals": dict(canon_vals),
                        "pcts": {c: round(v / total * 100, 2) for c, v in canon_vals.items()},
                        "total": total,
                    }
        except Exception:
            pass
    return projetos, mg_por_projeto


def analisar_combinacao(projetos_lista, mg_por_projeto, nome_combo):
    """Analisa um subconjunto de projetos (ex: SC-BC + alto + residencial_vertical_alto)."""
    if not projetos_lista:
        return None
    result = {
        "nome": nome_combo,
        "n_projetos": len(projetos_lista),
        "slugs": [p["slug"] for p in projetos_lista],
    }

    # Stats escala/financeiro
    rsm2s = [p.get("rsm2") for p in projetos_lista if p.get("rsm2") and 500 <= p["rsm2"] <= 10000]
    acs = [p.get("ac_m2") for p in projetos_lista if p.get("ac_m2") and p["ac_m2"] >= 1000]
    totais = [p.get("total_rs") for p in projetos_lista if p.get("total_rs")]
    urs = [p.get("ur") for p in projetos_lista if p.get("ur") and p["ur"] > 0]

    result["rsm2_stats"] = stats(rsm2s)
    result["ac_stats"] = stats(acs)
    result["total_stats"] = stats(totais)
    result["ur_stats"] = stats(urs)

    # Stats estruturais (indices_estruturais)
    conc = [p.get("concreto_m3_m2_ac") for p in projetos_lista if p.get("concreto_m3_m2_ac")]
    taxa = [p.get("taxa_aco_kg_m3") for p in projetos_lista if p.get("taxa_aco_kg_m3")]
    forma = [p.get("forma_m2_m2_ac") for p in projetos_lista if p.get("forma_m2_m2_ac")]
    result["concreto_stats"] = stats(conc)
    result["taxa_aco_stats"] = stats(taxa)
    result["forma_stats"] = stats(forma)

    # Distribuicao % MG (mediana)
    mg_pcts = defaultdict(list)
    for p in projetos_lista:
        mg = mg_por_projeto.get(p["slug"])
        if mg and mg.get("pcts"):
            for c, pct in mg["pcts"].items():
                mg_pcts[c].append(pct)
    result["mg_pct_med"] = {c: round(statistics.median(v), 2) for c, v in mg_pcts.items() if v}

    # Clientes top
    clientes = Counter(p["cliente_inferido"] for p in projetos_lista)
    result["top_clientes"] = dict(clientes.most_common(5))

    return result


def main():
    print("Carregando dados...", flush=True)
    projetos, mg_por_projeto = carregar_dados()
    print(f"  {len(projetos)} projetos enriquecidos", flush=True)
    print(f"  {len(mg_por_projeto)} com macrogrupos", flush=True)

    # ── Combinacoes principais ──
    resultado = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len(projetos),
        "combinacoes": {},
    }

    # Por CUB regiao
    print("\n=== POR CUB REGIAO ===", flush=True)
    por_regiao = defaultdict(list)
    for p in projetos:
        if p.get("cub_regiao"):
            por_regiao[p["cub_regiao"]].append(p)

    for regiao, lista in sorted(por_regiao.items(), key=lambda x: -len(x[1])):
        if len(lista) >= 3:  # mínimo pra stats significativo
            info = analisar_combinacao(lista, mg_por_projeto, regiao)
            resultado["combinacoes"][f"regiao::{regiao}"] = info
            rsm2 = info.get("rsm2_stats", {})
            print(f"  {regiao:<25} n={len(lista):>3}  R$/m² med={rsm2.get('mediana', 'N/D') if rsm2 else 'N/D'}", flush=True)

    # Por (cub_regiao, padrao)
    print("\n=== POR (REGIAO, PADRAO) ===", flush=True)
    por_reg_pad = defaultdict(list)
    for p in projetos:
        if p.get("cub_regiao") and p.get("padrao") not in (None, "desconhecido"):
            por_reg_pad[(p["cub_regiao"], p["padrao"])].append(p)

    for (reg, pad), lista in sorted(por_reg_pad.items(), key=lambda x: -len(x[1])):
        if len(lista) >= 3:
            info = analisar_combinacao(lista, mg_por_projeto, f"{reg} | {pad}")
            resultado["combinacoes"][f"regiao_padrao::{reg}::{pad}"] = info
            rsm2 = info.get("rsm2_stats", {})
            print(f"  {reg:<20} {pad:<15} n={len(lista):>3}  R$/m² med={rsm2.get('mediana', 'N/D') if rsm2 else 'N/D'}", flush=True)

    # Por (cub_regiao, padrao, tipologia) — se tipologia disponivel
    print("\n=== POR (REGIAO, PADRAO, TIPOLOGIA) ===", flush=True)
    por_reg_pad_tip = defaultdict(list)
    com_tipol = 0
    for p in projetos:
        if p.get("tipologia_canonica"):
            com_tipol += 1
            if p.get("cub_regiao") and p.get("padrao") not in (None, "desconhecido"):
                por_reg_pad_tip[(p["cub_regiao"], p["padrao"], p["tipologia_canonica"])].append(p)
    print(f"  projetos com tipologia_canonica: {com_tipol}", flush=True)

    for (reg, pad, tip), lista in sorted(por_reg_pad_tip.items(), key=lambda x: -len(x[1])):
        if len(lista) >= 3:
            info = analisar_combinacao(lista, mg_por_projeto, f"{reg} | {pad} | {tip}")
            resultado["combinacoes"][f"reg_pad_tip::{reg}::{pad}::{tip}"] = info
            rsm2 = info.get("rsm2_stats", {})
            print(f"  {reg:<18} {pad:<12} {tip[:30]:<30} n={len(lista):>3}", flush=True)

    # Por cliente (top 15)
    print("\n=== POR CLIENTE (top 15) ===", flush=True)
    por_cliente = defaultdict(list)
    for p in projetos:
        por_cliente[p["cliente_inferido"]].append(p)

    top_clientes = sorted(por_cliente.items(), key=lambda x: -len(x[1]))[:15]
    for cli, lista in top_clientes:
        if len(lista) >= 2:
            info = analisar_combinacao(lista, mg_por_projeto, f"cliente::{cli}")
            resultado["combinacoes"][f"cliente::{cli}"] = info
            rsm2 = info.get("rsm2_stats", {})
            print(f"  {cli:<30} n={len(lista):>3}  R$/m² med={rsm2.get('mediana', 'N/D') if rsm2 else 'N/D'}", flush=True)

    OUT_JSON.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT_JSON}", flush=True)
    print(f"Total combinacoes analisadas: {len(resultado['combinacoes'])}", flush=True)


if __name__ == "__main__":
    main()
