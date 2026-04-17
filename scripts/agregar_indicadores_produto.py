#!/usr/bin/env python3
"""Phase 20b — Agregador v2 de indicadores de produto.

Combina:
- indicadores-produto/*.json (meu pipeline: 48 indicadores novos/redundantes)
- indices-executivo/*.json (base existente: estruturais validados, PUs, detalhes)
- padroes-classificados-consolidado.json (AC/UR/padrão)

Gera:
- base/indicadores-produto-agregados.json
  - indicadores_globais: stats cross-projeto
  - indicadores_por_padrao: stats segmentado
  - projeto_matrix: matriz projeto × indicador
  - outliers: projetos > p90 ou < p10 em cada indicador
  - densidades_agregadas: indicadores derivados (pontos elétricos total, louças total)
  - abc_analysis: top itens por macrogrupo
  - pus_validados: PUs dos acabamentos/esquadrias (de indices-executivo)
  - correlacoes: correlações entre indicadores cross-projeto

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
IDX_DIR = BASE / "indices-executivo"
PAD_FILE = BASE / "padroes-classificados-consolidado.json"
OUT = BASE / "indicadores-produto-agregados.json"

# Mapeamento indicator_name (meu pipeline) → override de indices-executivo.indices_estruturais
IDX_OVERRIDE_MAP = {
    # meu_pipeline_name → indices_executivo_key (mais confiável)
    "concreto_m3_por_m2_ac": "concreto_m3_por_m2_ac",
    "aco_kg_por_m2_ac": None,  # indices_executivo tem aco_total_kg, preciso calc aco/AC
    "forma_m2_por_m2_ac": "forma_m2_por_m2_ac",
    "taxa_aco_kg_por_m3": "aco_kg_por_m3_concreto",
}


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


def load_all_data():
    """Carrega indicadores-produto, indices-executivo, padrões."""
    pad = _load_json(PAD_FILE)
    pad_map = {p["projeto"]: p for p in pad.get("projetos", []) if p.get("projeto")}

    projetos = {}
    for jp in sorted(IND_DIR.glob("*.json")):
        d = _load_json(jp)
        if d and d.get("slug"):
            projetos[d["slug"]] = {"ind_produto": d}

    for jp in sorted(IDX_DIR.glob("*.json")):
        d = _load_json(jp)
        slug = d.get("projeto") or jp.stem
        if slug not in projetos:
            projetos[slug] = {}
        projetos[slug]["ind_executivo"] = d
        projetos[slug]["padrao_info"] = pad_map.get(slug, {})

    return projetos


def merge_indicadores(proj_data: dict) -> dict:
    """Combina indicadores do meu pipeline com indices-executivo.

    Preferência: indices-executivo quando disponível e mais confiável.
    Retorna {indicator_name: valor}
    """
    merged = {}

    # 1. Do meu pipeline
    ip = proj_data.get("ind_produto", {})
    for name, info in ip.get("indicadores", {}).items():
        if info.get("valor") is not None:
            merged[name] = info["valor"]

    # 2. Overrides de indices-executivo (estruturais validados)
    ix = proj_data.get("ind_executivo", {})
    est = ix.get("indices_estruturais") or {}
    ac = ix.get("ac") or ip.get("ac_m2") or 0
    if est:
        if est.get("concreto_m3_por_m2_ac"):
            merged["concreto_m3_por_m2_ac"] = est["concreto_m3_por_m2_ac"]
        if est.get("aco_total_kg") and ac and ac > 0:
            merged["aco_kg_por_m2_ac"] = round(est["aco_total_kg"] / ac, 4)
        if est.get("forma_m2_por_m2_ac"):
            merged["forma_m2_por_m2_ac"] = est["forma_m2_por_m2_ac"]
        if est.get("aco_kg_por_m3_concreto"):
            merged["taxa_aco_kg_por_m3"] = est["aco_kg_por_m3_concreto"]
        if est.get("estacas_qtd") and ac and ac > 0:
            merged["estacas_qtd_por_m2_ac"] = round(est["estacas_qtd"] / ac, 6)

    return merged


def compute_densidades_agregadas(merged: dict) -> dict:
    """Indicadores derivados que somam categorias relacionadas."""
    out = {}
    # Pontos elétricos total (luz + tomada + AR_COND) por UR — proxy de sofisticação
    total_el = sum(merged.get(k, 0) or 0 for k in [
        "pontos_iluminacao_por_ur", "tomadas_por_ur", "luminarias_por_ur",
        "ar_condicionado_pontos_por_ur",
    ])
    if total_el > 0:
        out["pontos_eletricos_total_por_ur"] = round(total_el, 2)

    # Louças total por UR
    total_louca = sum(merged.get(k, 0) or 0 for k in [
        "bacias_sanitarias_por_ur", "lavatorios_por_ur", "cubas_por_ur", "chuveiros_por_ur",
    ])
    if total_louca > 0:
        out["loucas_total_por_ur"] = round(total_louca, 2)

    # Taxa acabamentos (revestimentos + pintura) por AC
    total_acab = sum(merged.get(k, 0) or 0 for k in [
        "porcelanato_ceramica_m2_por_m2_ac", "contrapiso_m2_por_m2_ac",
        "pintura_interna_m2_por_m2_ac", "pintura_externa_m2_por_m2_ac",
        "rodape_m_por_m2_ac",
    ])
    if total_acab > 0:
        out["acabamentos_total_m2_por_m2_ac"] = round(total_acab, 2)

    # Taxa revestimento fachada + pintura ext
    fach = (merged.get("revestimento_fachada_m2_por_m2_ac", 0) or 0) + \
           (merged.get("pintura_externa_m2_por_m2_ac", 0) or 0)
    if fach > 0:
        out["fachada_total_m2_por_m2_ac"] = round(fach, 2)

    # Esquadrias total (portas + janelas) por UR
    esq = (merged.get("portas_un_por_ur", 0) or 0) + (merged.get("janelas_un_por_ur", 0) or 0)
    if esq > 0:
        out["esquadrias_total_un_por_ur"] = round(esq, 2)

    return out


def main():
    print("Loading all data sources...", flush=True)
    projetos = load_all_data()
    print(f"  {len(projetos)} projects combined", flush=True)

    # Merge indicadores por projeto
    for slug, pd in projetos.items():
        merged = merge_indicadores(pd)
        derived = compute_densidades_agregadas(merged)
        merged.update(derived)
        pd["merged_indicadores"] = merged

    # Collect all indicator names
    all_names = set()
    for pd in projetos.values():
        all_names.update(pd.get("merged_indicadores", {}).keys())
    all_names = sorted(all_names)
    print(f"  {len(all_names)} unique indicators (merged)", flush=True)

    # Padrões
    padroes = sorted(set(
        (pd.get("padrao_info", {}).get("padrao")
         or pd.get("ind_produto", {}).get("padrao")
         or "desconhecido")
        for pd in projetos.values()
    ))
    print(f"  Padroes: {padroes}", flush=True)

    print("\nGlobal stats...", flush=True)
    indicadores_globais = {}
    for name in all_names:
        values = []
        fontes = []
        for slug, pd in projetos.items():
            v = pd.get("merged_indicadores", {}).get(name)
            if v is not None and isinstance(v, (int, float)) and v > 0:
                values.append(v)
                fontes.append(slug)
        s = stats(values)
        if s:
            s["projetos_fonte"] = fontes
            indicadores_globais[name] = s

    print("\nStats per padrao...", flush=True)
    ind_por_padrao = {}
    for pad in padroes:
        projs = [(s, pd) for s, pd in projetos.items()
                 if (pd.get("padrao_info", {}).get("padrao")
                     or pd.get("ind_produto", {}).get("padrao")
                     or "desconhecido") == pad]
        if not projs:
            continue
        ind_por_padrao[pad] = {"n_projetos": len(projs), "indicadores": {}}
        for name in all_names:
            vs = [pd.get("merged_indicadores", {}).get(name) for _, pd in projs]
            vs = [v for v in vs if v is not None]
            s = stats(vs)
            if s:
                ind_por_padrao[pad]["indicadores"][name] = s
        n_ind = len(ind_por_padrao[pad]["indicadores"])
        print(f"  {pad:<15} {len(projs):>3} projetos, {n_ind} indicadores", flush=True)

    # Project matrix
    print("\nProject matrix...", flush=True)
    projeto_matrix = []
    for slug, pd in projetos.items():
        ip = pd.get("ind_produto") or {}
        ix = pd.get("ind_executivo") or {}
        pi = pd.get("padrao_info") or {}
        row = {
            "slug": slug,
            "padrao": pi.get("padrao") or ip.get("padrao") or "desconhecido",
            "ac_m2": ix.get("ac") or ip.get("ac_m2") or 0,
            "ur": ix.get("ur") or ip.get("ur") or 0,
            "total_r$": ix.get("total") or 0,
            "rsm2": ix.get("rsm2") or 0,
        }
        for name in all_names:
            row[name] = pd.get("merged_indicadores", {}).get(name)
        projeto_matrix.append(row)

    # Outliers: projetos > p90 ou < p10 em cada indicador
    print("\nOutliers...", flush=True)
    outliers_por_indicador = {}
    for name, g in indicadores_globais.items():
        if g["n"] < 10:
            continue
        p10, p90 = g["p10"], g["p90"]
        high = []
        low = []
        for slug, pd in projetos.items():
            v = pd.get("merged_indicadores", {}).get(name)
            if v is None:
                continue
            if v > p90:
                high.append({"slug": slug, "valor": v, "ratio_p90": round(v / p90, 2) if p90 else None})
            elif v < p10 and v > 0:
                low.append({"slug": slug, "valor": v, "ratio_p10": round(v / p10, 2) if p10 else None})
        if high or low:
            outliers_por_indicador[name] = {
                "acima_p90": sorted(high, key=lambda x: -x["valor"])[:10],
                "abaixo_p10": sorted(low, key=lambda x: x["valor"])[:10],
            }

    # ABC analysis (dos indices-executivo.curva_abc)
    print("\nABC analysis...", flush=True)
    abc_por_mg = {}  # macrogrupo → lista de itens top agregados cross-projeto
    for slug, pd in projetos.items():
        ix = pd.get("ind_executivo") or {}
        abc = ix.get("curva_abc") or {}
        for mg, info in abc.items():
            abc_por_mg.setdefault(mg, []).extend([
                {"projeto": slug, **it} for it in info.get("itens", [])
            ])
    # Resumo ABC: top 10 descriptions por MG
    abc_summary = {}
    for mg, lst in abc_por_mg.items():
        # Agrupa por descrição canônica
        from collections import defaultdict
        by_desc = defaultdict(lambda: {"n_projetos": 0, "total_r$_agregado": 0, "pcts": []})
        for it in lst:
            desc = str(it.get("desc") or "")[:80]
            by_desc[desc]["n_projetos"] += 1
            by_desc[desc]["total_r$_agregado"] += it.get("total", 0) or 0
            if it.get("pct"):
                by_desc[desc]["pcts"].append(it["pct"])
        # Converter e ordenar por total
        top = []
        for desc, info in by_desc.items():
            if info["n_projetos"] < 2:
                continue
            pct_med = round(statistics.median(info["pcts"]), 3) if info["pcts"] else 0
            top.append({
                "desc": desc,
                "n_projetos": info["n_projetos"],
                "total_r$_agregado": round(info["total_r$_agregado"], 2),
                "pct_med_do_mg": pct_med,
            })
        top.sort(key=lambda x: -x["total_r$_agregado"])
        abc_summary[mg] = top[:15]

    # PUs validados de indices-executivo.acabamentos_pus e esquadrias_detail
    print("\nPUs validados...", flush=True)
    pus = {
        "porcelanato_pu_m2": [], "ceramica_pu_m2": [], "contrapiso_pu_m2": [],
        "forro_gesso_pu_m2": [], "chapisco_pu_m2": [], "reboco_pu_m2": [],
        "pintura_parede_pu_m2": [], "laminado_pu_m2": [], "rodape_pu_m": [],
        "aluminio_pu_m2": [], "guarda_corpo_pu_m": [], "porta_corta_fogo_pu_un": [],
        "elevador_pu_un": [],
    }
    for slug, pd in projetos.items():
        ix = pd.get("ind_executivo") or {}
        ap = ix.get("acabamentos_pus") or {}
        ed = ix.get("esquadrias_detail") or {}
        sd = ix.get("sistemas_especiais_detail") or {}
        for k in ("porcelanato_pu_m2", "ceramica_pu_m2", "contrapiso_pu_m2",
                  "forro_gesso_pu_m2", "chapisco_pu_m2", "reboco_pu_m2",
                  "pintura_parede_pu_m2", "laminado_pu_m2", "rodape_pu_m"):
            v = ap.get(k)
            if v and v > 0:
                pus[k].append({"slug": slug, "valor": v})
        if ed.get("aluminio", {}).get("pu_m2"):
            pus["aluminio_pu_m2"].append({"slug": slug, "valor": ed["aluminio"]["pu_m2"]})
        if ed.get("guarda_corpo", {}).get("pu_m"):
            pus["guarda_corpo_pu_m"].append({"slug": slug, "valor": ed["guarda_corpo"]["pu_m"]})
        if ed.get("portas_corta_fogo", {}).get("pu_un"):
            pus["porta_corta_fogo_pu_un"].append({"slug": slug, "valor": ed["portas_corta_fogo"]["pu_un"]})
        if sd.get("elevadores", {}).get("pu_un"):
            pus["elevador_pu_un"].append({"slug": slug, "valor": sd["elevadores"]["pu_un"]})
    # Stats dos PUs
    pus_stats = {}
    for k, lst in pus.items():
        if not lst:
            continue
        s = stats([x["valor"] for x in lst])
        if s:
            s["amostras"] = lst[:20]
            pus_stats[k] = s

    # Correlações entre indicadores (Pearson, n>=10)
    print("\nCorrelacoes...", flush=True)
    correlacoes = {}
    indicators_with_n = [(n, g["n"]) for n, g in indicadores_globais.items() if g["n"] >= 10]
    indicators_with_n.sort(key=lambda x: -x[1])
    top_inds = [n for n, _ in indicators_with_n[:15]]
    for i, n1 in enumerate(top_inds):
        for n2 in top_inds[i + 1:]:
            pairs = []
            for _, pd in projetos.items():
                v1 = pd.get("merged_indicadores", {}).get(n1)
                v2 = pd.get("merged_indicadores", {}).get(n2)
                if v1 and v2:
                    pairs.append((v1, v2))
            if len(pairs) < 10:
                continue
            xs = [p[0] for p in pairs]
            ys = [p[1] for p in pairs]
            mx = statistics.mean(xs)
            my = statistics.mean(ys)
            num = sum((x - mx) * (y - my) for x, y in pairs)
            dx = (sum((x - mx) ** 2 for x in xs)) ** 0.5
            dy = (sum((y - my) ** 2 for y in ys)) ** 0.5
            if dx > 0 and dy > 0:
                r = num / (dx * dy)
                if abs(r) > 0.5:
                    correlacoes[f"{n1} ~ {n2}"] = {"r": round(r, 3), "n": len(pairs)}
    correlacoes = dict(sorted(correlacoes.items(), key=lambda x: -abs(x[1]["r"]))[:30])

    # Insights automáticos por projeto
    print("\nInsights automaticos...", flush=True)
    insights_por_projeto = {}
    for slug, pd in projetos.items():
        pi = pd.get("padrao_info") or {}
        padrao = pi.get("padrao") or pd.get("ind_produto", {}).get("padrao") or "desconhecido"
        merged = pd.get("merged_indicadores", {})
        ref_pad = ind_por_padrao.get(padrao, {}).get("indicadores", {})

        flags = []  # lista de insights
        for name, v in merged.items():
            if v is None or not isinstance(v, (int, float)) or v <= 0:
                continue
            ref = ref_pad.get(name)
            if not ref or ref.get("n", 0) < 5:
                continue
            med = ref.get("mediana")
            p25, p75 = ref.get("p25"), ref.get("p75")
            p10, p90 = ref.get("p10"), ref.get("p90")
            if not all([med, p25, p75, p10, p90]):
                continue
            # Classifica desvio
            if v > p90:
                flags.append({
                    "tipo": "fora_alto",
                    "indicador": name,
                    "valor": round(v, 4),
                    "mediana_pad": round(med, 4),
                    "delta_pct": round((v / med - 1) * 100, 1) if med else None,
                    "texto": f"{name}: {v:.3f} esta {(v/med-1)*100:+.0f}% vs mediana {padrao}",
                })
            elif v < p10:
                flags.append({
                    "tipo": "fora_baixo",
                    "indicador": name,
                    "valor": round(v, 4),
                    "mediana_pad": round(med, 4),
                    "delta_pct": round((v / med - 1) * 100, 1) if med else None,
                    "texto": f"{name}: {v:.3f} esta {(v/med-1)*100:+.0f}% vs mediana {padrao}",
                })
        flags.sort(key=lambda x: abs(x.get("delta_pct") or 0), reverse=True)
        insights_por_projeto[slug] = {
            "padrao": padrao,
            "n_flags": len(flags),
            "top_flags": flags[:8],
        }

    # Padrão statistics: comparação cross-padrão (qual indicador mais diferencia padrões?)
    print("\nDiferenciadores de padrao...", flush=True)
    diferenciadores = []
    for name in all_names:
        medianas = {}
        for pad, pd_info in ind_por_padrao.items():
            m = pd_info.get("indicadores", {}).get(name, {}).get("mediana")
            if m:
                medianas[pad] = m
        if len(medianas) < 2:
            continue
        # Ratio max/min entre padrões
        valores = list(medianas.values())
        if min(valores) > 0:
            ratio = max(valores) / min(valores)
            if ratio > 1.5:
                diferenciadores.append({
                    "indicador": name,
                    "ratio_max_min": round(ratio, 2),
                    "medianas_por_padrao": {k: round(v, 4) for k, v in medianas.items()},
                })
    diferenciadores.sort(key=lambda x: -x["ratio_max_min"])

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos_total": len(projetos),
        "n_indicadores_unicos": len(all_names),
        "padroes": padroes,
        "nomes_indicadores": all_names,
        "indicadores_globais": indicadores_globais,
        "indicadores_por_padrao": ind_por_padrao,
        "projeto_matrix": projeto_matrix,
        "outliers_por_indicador": outliers_por_indicador,
        "abc_summary": abc_summary,
        "pus_stats": pus_stats,
        "correlacoes": correlacoes,
        "insights_por_projeto": insights_por_projeto,
        "diferenciadores": diferenciadores[:20],
    }

    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT}", flush=True)
    print(f"  {len(indicadores_globais)} indicadores globais", flush=True)
    print(f"  {len(ind_por_padrao)} padroes", flush=True)
    print(f"  {len(outliers_por_indicador)} indicadores com outliers", flush=True)
    print(f"  {len(abc_summary)} macrogrupos na ABC", flush=True)
    print(f"  {len(pus_stats)} PUs de referencia", flush=True)
    print(f"  {len(correlacoes)} correlacoes |r| > 0.5", flush=True)
    print(f"  {len(insights_por_projeto)} projetos com insights", flush=True)
    print(f"  {len(diferenciadores[:20])} diferenciadores de padrao (top 20)", flush=True)


if __name__ == "__main__":
    main()
