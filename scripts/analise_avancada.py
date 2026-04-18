#!/usr/bin/env python3
"""Phase 20g — Analises avancadas cross-projeto.

1. Analise por CLIENTE (top 20 clientes, stats intra-cliente)
2. CLUSTERIZACAO por assinatura de % MG (k-means simples)
3. COMPLEXIDADE vs padrao (qualitative.phase1, macrogrupos n)
4. PARAMETRICO x EXECUTIVO (pros pacotes disponiveis)
5. ANALISE QUALITATIVA (padroes_identificados, fora_da_curva, observacoes)

Saidas:
- base/analise-avancada-agregada.json
- base/analise-avancada-cartesian.xlsx (com 10 abas)
- base/ANALISE-AVANCADA-RESUMO.md

Uso: python scripts/analise_avancada.py
"""
from __future__ import annotations

import json
import math
import statistics
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
IDX_DIR = BASE / "indices-executivo"
PAD_FILE = BASE / "padroes-classificados-consolidado.json"
PAR_DIR = BASE / "pacotes"
OUT_JSON = BASE / "analise-avancada-agregada.json"

# Map canonical client names (manual — melhora cluster por cliente)
CLIENTE_CANON = [
    (["chiquetti"], "Chiquetti & Dalvesco"),
    (["pass-e"], "Pass-e"),
    (["ck"], "CK"),
    (["amalfi"], "Amalfi"),
    (["mussi"], "Mussi Empreendimentos"),
    (["nova-empreendimentos", "nova empre"], "Nova Empreendimentos"),
    (["cn-brava"], "CN Brava"),
    (["santa-maria"], "Santa Maria"),
    (["f-nogueira"], "F. Nogueira"),
    (["paludo"], "Paludo"),
    (["mtf"], "MTF"),
    (["muller"], "Muller"),
    (["neuhaus"], "Neuhaus"),
    (["santo-andre"], "Santo Andre"),
    (["mendes"], "Mendes Empreendimentos"),
    (["grupo-duo"], "Grupo DUO"),
    (["grandezza"], "Grandezza"),
    (["viva4"], "Viva4"),
    (["blue-heaven"], "Blue Heaven"),
    (["all-"], "ALL"),
    (["brasin"], "Brasin"),
    (["thozen"], "Thozen"),
    (["adore"], "Adore"),
    (["arthen"], "Arthen"),
    (["xpcon"], "XPcon"),
    (["homeset"], "Homeset"),
    (["brava"], "Brava Construtora"),
    (["buildsales"], "BuildSales"),
    (["placon"], "Placon"),
    (["fonseca"], "Fonseca"),
    (["fg-"], "FG"),
    (["etr-"], "ETR"),
    (["gdi-"], "GDI"),
    (["terrassa"], "Terrassa"),
    (["as-ramos"], "AS Ramos"),
    (["bellei"], "Bellei"),
    (["cartesian"], "Cartesian"),
    (["h-"], "H Empreendimentos"),
    (["estilo-cond"], "Estilo Condominios"),
    (["lotisa"], "Lotisa"),
    (["libra"], "Libra Concept"),
    (["hacasa"], "Hacasa"),
]


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def canon_cliente(slug: str) -> str:
    s = norm(slug)
    for prefixes, name in CLIENTE_CANON:
        for pref in prefixes:
            if s.startswith(pref):
                return name
    # Fallback: primeiro token
    parts = slug.split("-")
    return parts[0].title() if parts else "Outros"


MG_CANON = [
    ("Gerenciamento", ["gerenciamento", "ger. tec", "ger tec"]),
    ("Movimentacao de Terra", ["mov", "terra", "terraplan"]),
    ("Infraestrutura", ["infraestrutura", "fundac", "contenc", "estaca", "baldram"]),
    ("Supraestrutura", ["supraestrutura", "estrutura de concreto"]),
    ("Alvenaria", ["alvenaria", "vedac", "divisori"]),
    ("Impermeabilizacao", ["impermeab", "tratament"]),
    ("Instalacoes Hidrossanitarias", ["hidros", "hidraul", "drenagem"]),
    ("Instalacoes Eletricas", ["eletric", "telefon", "logic", "comunica", "automaca"]),
    ("Instalacoes Preventivas", ["preventiv", "pci", "spda", "glp"]),
    # Genérico de Instalacoes (orcamentos menos detalhados) - vem antes das específicas não cobertas
    ("Instalacoes Gerais", ["instalac", "instalações"]),
    ("Climatizacao", ["climat", "exaust"]),
    ("Revestimentos Parede", ["rev. int. parede", "rev.int.parede", "rev int parede",
                              "revestimentos internos em paredes",
                              "revestimentos internos de parede", "revestimentos e acabamentos internos em parede",
                              "revestimentos argamassados parede", "acabamentos em parede",
                              "acabamentos internos em parede", "revestimentos ceramicos",
                              "rev. int parede", "rev parede"]),
    ("Revestimentos Teto", ["teto", "forro"]),
    ("Pisos e Pavimentacoes", ["piso", "pavimenta", "contrapiso"]),
    ("Pintura Interna", ["pintura interna", "sistemas de pintura interna"]),
    # Pintura generica (quando nao especifica int/ext)
    ("Pintura Geral", ["pintura", "pinturas", "sistema de pintura"]),
    ("Esquadrias", ["esquadri", "vidro", "ferragen"]),
    ("Loucas e Metais", ["louc", "metai"]),
    ("Fachada", ["fachada", "pintura externa"]),
    ("Cobertura", ["cobertura"]),
    ("Sistemas Especiais", ["especia", "equipament", "outros sistemas"]),
    ("Servicos Complementares", ["complementa", "imprevisto", "contingenc"]),
]


def canonize_mg(raw):
    r = norm(raw).strip().lstrip("0123456789. ")
    for canon, kws in MG_CANON:
        for kw in kws:
            if kw in r:
                return canon
    return "Outros"


def _load(p):
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
        "mediana": round(statistics.median(vs), 4),
        "media": round(statistics.mean(vs), 4),
        "max": round(vs[-1], 4),
        "dp": round(statistics.stdev(vs), 4) if n > 1 else 0,
        "cv": round(statistics.stdev(vs) / statistics.mean(vs), 3) if n > 1 and statistics.mean(vs) > 0 else 0,
    }


def load_projects():
    pad = _load(PAD_FILE)
    pad_map = {p["projeto"]: p for p in pad.get("projetos", []) if p.get("projeto")}
    projs = []
    for f in sorted(IDX_DIR.glob("*.json")):
        d = _load(f)
        slug = d.get("projeto") or f.stem
        pi = pad_map.get(slug, {})
        ac = d.get("ac") or 0
        rsm2 = d.get("rsm2") or 0
        projs.append({
            "slug": slug,
            "cliente": canon_cliente(slug),
            "ac": ac,
            "ur": d.get("ur") or 0,
            "total": d.get("total") or 0,
            "rsm2": rsm2,
            "padrao": pi.get("padrao", "desconhecido"),
            "macrogrupos": d.get("macrogrupos") or {},
            "qualitative": d.get("qualitative") or {},
            "ac_valid": ac >= 1000,
            "rsm2_valid": bool(rsm2 and 500 <= rsm2 <= 10000),
        })
    return projs


# ═══════════════════════════════════════════════════════════════════════
# 1. ANALISE POR CLIENTE
# ═══════════════════════════════════════════════════════════════════════
def analise_por_cliente(projs):
    por_cliente = defaultdict(list)
    for p in projs:
        por_cliente[p["cliente"]].append(p)

    out = []
    for cliente, plist in por_cliente.items():
        n = len(plist)
        if n < 1:
            continue
        # Projetos válidos pra R$/m²
        validos = [p for p in plist if p["rsm2_valid"] and p["ac_valid"]]
        rsm2s = [p["rsm2"] for p in validos]
        acs = [p["ac"] for p in plist if p["ac"] > 0]
        padroes = Counter(p["padrao"] for p in plist)
        rec = {
            "cliente": cliente,
            "n_projetos": n,
            "n_validos_rsm2": len(validos),
            "rsm2_mediana": round(statistics.median(rsm2s), 2) if rsm2s else None,
            "rsm2_min": round(min(rsm2s), 2) if rsm2s else None,
            "rsm2_max": round(max(rsm2s), 2) if rsm2s else None,
            "ac_total": round(sum(acs), 0) if acs else 0,
            "ac_medio": round(sum(acs) / len(acs), 0) if acs else 0,
            "padrao_dominante": padroes.most_common(1)[0][0] if padroes else "?",
            "padroes_mix": dict(padroes),
            "projetos": [{"slug": p["slug"], "padrao": p["padrao"], "ac": p["ac"], "rsm2": p["rsm2"]}
                         for p in plist],
        }
        out.append(rec)
    out.sort(key=lambda x: -x["n_projetos"])
    return out


# ═══════════════════════════════════════════════════════════════════════
# 2. CLUSTERIZACAO por assinatura % MG
# ═══════════════════════════════════════════════════════════════════════
def extrair_assinatura(p):
    """Assinatura = vetor de % MG canônicos no total."""
    if not p.get("total") or p["total"] <= 0:
        return None
    canon_vals = defaultdict(float)
    for raw, info in p["macrogrupos"].items():
        v = info.get("valor") if isinstance(info, dict) else info
        if v and v > 0:
            canon_vals[canonize_mg(raw)] += v
    if not canon_vals:
        return None
    total = sum(canon_vals.values())
    return {k: v / total * 100 for k, v in canon_vals.items()} if total > 0 else None


def euclidean(v1: dict, v2: dict, keys: list) -> float:
    return math.sqrt(sum((v1.get(k, 0) - v2.get(k, 0)) ** 2 for k in keys))


def kmeans_simples(vectors: list, k: int, max_iter: int = 50) -> list:
    """K-means sem dependências externas. Retorna lista de cluster_id por vetor."""
    if not vectors:
        return []
    # Set de keys comuns
    all_keys = set()
    for v in vectors:
        all_keys.update(v.keys())
    keys = sorted(all_keys)

    # Inicializa centroides aleatoriamente (determinístico usando seed)
    import random
    random.seed(42)
    centroides = [dict(v) for v in random.sample(vectors, min(k, len(vectors)))]

    for it in range(max_iter):
        # Assign
        labels = []
        for v in vectors:
            dists = [euclidean(v, c, keys) for c in centroides]
            labels.append(dists.index(min(dists)))
        # Update
        new_cents = []
        for ki in range(k):
            members = [vectors[i] for i, l in enumerate(labels) if l == ki]
            if not members:
                new_cents.append(centroides[ki])
                continue
            cent = {key: sum(m.get(key, 0) for m in members) / len(members) for key in keys}
            new_cents.append(cent)
        # Check convergence
        delta = sum(euclidean(a, b, keys) for a, b in zip(centroides, new_cents))
        centroides = new_cents
        if delta < 0.01:
            break

    return labels, centroides


def clusterizacao(projs):
    vectors = []
    proj_refs = []
    for p in projs:
        sig = extrair_assinatura(p)
        if sig and sum(sig.values()) > 50:  # pelo menos 50% coberto
            vectors.append(sig)
            proj_refs.append(p)
    if len(vectors) < 10:
        return {"error": "insuficiente"}

    # Tenta 4 clusters (corresponde aproximadamente a 4 padrões)
    labels, centroides = kmeans_simples(vectors, k=4)

    clusters = defaultdict(list)
    for i, lab in enumerate(labels):
        p = proj_refs[i]
        clusters[lab].append({
            "slug": p["slug"],
            "padrao_original": p["padrao"],
            "cliente": p["cliente"],
            "ac": p["ac"],
            "rsm2": p["rsm2"],
        })

    # Caracteriza cada cluster
    cluster_info = {}
    for lab, members in clusters.items():
        # Nome do cluster baseado no centroide (top 3 MGs)
        cent = centroides[lab]
        top_mgs = sorted(cent.items(), key=lambda x: -x[1])[:5]
        # Padrão dominante
        padroes = Counter(m["padrao_original"] for m in members)
        pad_dom = padroes.most_common(1)[0][0] if padroes else "?"
        # Escala media
        acs = [m["ac"] for m in members if m["ac"] > 0]
        rsm2s = [m["rsm2"] for m in members if 500 <= (m["rsm2"] or 0) <= 10000]
        cluster_info[f"cluster_{lab}"] = {
            "n_projetos": len(members),
            "padrao_dominante": pad_dom,
            "padroes_mix": dict(padroes),
            "ac_mediano": round(statistics.median(acs), 0) if acs else None,
            "rsm2_mediano": round(statistics.median(rsm2s), 2) if rsm2s else None,
            "top_mgs_centroide": [{"mg": mg, "pct": round(pct, 2)} for mg, pct in top_mgs],
            "membros": members,
        }
    return cluster_info


# ═══════════════════════════════════════════════════════════════════════
# 3. COMPLEXIDADE
# ═══════════════════════════════════════════════════════════════════════
def complexidade_por_padrao(projs):
    """Complexidade aproximada = n_abas + n_macrogrupos + n_itens, por padrão."""
    por_padrao = defaultdict(lambda: {"abas": [], "itens": [], "mgs": []})
    for p in projs:
        q = p.get("qualitative", {}) or {}
        ph1 = q.get("phase1_extraction", {}) or {}
        n_abas = ph1.get("n_abas") or 0
        n_itens = ph1.get("total_itens") or 0
        n_mgs = len(p.get("macrogrupos", {}))
        if n_abas:
            por_padrao[p["padrao"]]["abas"].append(n_abas)
        if n_itens:
            por_padrao[p["padrao"]]["itens"].append(n_itens)
        if n_mgs:
            por_padrao[p["padrao"]]["mgs"].append(n_mgs)

    out = {}
    for pad, d in por_padrao.items():
        out[pad] = {
            "n_abas_med": round(statistics.median(d["abas"]), 1) if d["abas"] else None,
            "n_itens_med": round(statistics.median(d["itens"]), 0) if d["itens"] else None,
            "n_mgs_med": round(statistics.median(d["mgs"]), 1) if d["mgs"] else None,
            "n_projetos_amostra": len(d["abas"]),
        }
    return out


# ═══════════════════════════════════════════════════════════════════════
# 4. PARAMETRICO x EXECUTIVO
# ═══════════════════════════════════════════════════════════════════════
def parametrico_x_executivo(projs):
    """Compara paramétrico (nos 4 pacotes disponíveis) com executivo."""
    out = []
    if not PAR_DIR.exists():
        return out
    for pkg_dir in sorted(PAR_DIR.iterdir()):
        if not pkg_dir.is_dir():
            continue
        slug = pkg_dir.name
        # Procura o executivo correspondente
        exec_proj = next((p for p in projs if p["slug"] == slug or p["slug"].startswith(slug)), None)
        # Procura paramétrico V2/V3
        par_files = list(pkg_dir.glob("*parametrico*.xlsx")) + list(pkg_dir.glob("*PARAMETRICO*.json"))
        par_file = par_files[0] if par_files else None
        # Procura log/config que tenha total estimado
        cfg_files = list(pkg_dir.glob("*config*.json")) + list(pkg_dir.glob("*briefing*.md"))
        out.append({
            "pacote": slug,
            "executivo_encontrado": exec_proj["slug"] if exec_proj else None,
            "executivo_total": exec_proj["total"] if exec_proj else None,
            "executivo_rsm2": exec_proj["rsm2"] if exec_proj else None,
            "executivo_ac": exec_proj["ac"] if exec_proj else None,
            "parametrico_files": [str(f.name) for f in par_files[:5]],
            "config_files": [str(f.name) for f in cfg_files[:3]],
        })
    return out


# ═══════════════════════════════════════════════════════════════════════
# 5. ANALISE QUALITATIVA
# ═══════════════════════════════════════════════════════════════════════
def analise_qualitativa(projs):
    categorias_obs = Counter()
    itens_fora_curva = Counter()
    padroes_top = Counter()
    motivos_fora_curva = []

    for p in projs:
        q = p.get("qualitative", {}) or {}
        # Observações categorizadas
        for obs in q.get("observacoes_orcamentista", []) or []:
            cat = obs.get("categoria") if isinstance(obs, dict) else None
            if cat:
                categorias_obs[cat] += 1
        # Padrões identificados
        for pat in q.get("padroes_identificados", []) or []:
            if isinstance(pat, str):
                padroes_top[pat[:60]] += 1
        # Fora da curva
        for fc in q.get("fora_da_curva", []) or []:
            if isinstance(fc, dict):
                item = fc.get("item", "")[:60]
                if item:
                    itens_fora_curva[item] += 1
                motivo = fc.get("motivo")
                if motivo:
                    motivos_fora_curva.append({
                        "slug": p["slug"], "padrao": p["padrao"],
                        "item": item, "motivo": motivo[:200],
                    })

    return {
        "categorias_observacoes": dict(categorias_obs.most_common(20)),
        "itens_fora_curva_recorrentes": dict(itens_fora_curva.most_common(25)),
        "padroes_identificados_top": dict(padroes_top.most_common(25)),
        "motivos_fora_curva_amostra": motivos_fora_curva[:30],
        "total_observacoes": sum(categorias_obs.values()),
        "total_fora_curva": sum(itens_fora_curva.values()),
    }


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
def main():
    print("Loading projects...", flush=True)
    projs = load_projects()
    print(f"  {len(projs)} projects", flush=True)

    print("1. Analise por cliente...", flush=True)
    clientes = analise_por_cliente(projs)
    print(f"   {len(clientes)} clientes unicos", flush=True)

    print("2. Clusterizacao por assinatura MG...", flush=True)
    clusters = clusterizacao(projs)
    print(f"   {len(clusters)} clusters", flush=True)

    print("3. Complexidade por padrao...", flush=True)
    comp = complexidade_por_padrao(projs)

    print("4. Parametrico x Executivo...", flush=True)
    par_ex = parametrico_x_executivo(projs)
    print(f"   {len(par_ex)} pacotes", flush=True)

    print("5. Analise qualitativa...", flush=True)
    qual = analise_qualitativa(projs)
    print(f"   {qual['total_observacoes']} observacoes, {qual['total_fora_curva']} fora da curva", flush=True)

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len(projs),
        "analise_por_cliente": clientes,
        "clusters": clusters,
        "complexidade_por_padrao": comp,
        "parametrico_x_executivo": par_ex,
        "qualitativa": qual,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
