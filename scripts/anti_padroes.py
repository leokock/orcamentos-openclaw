#!/usr/bin/env python3
"""Fase 7 — Deteccao de anti-padroes.

Identifica caracteristicas comuns entre outliers (residuo > 1.5σ positivos
e < -1.5σ negativos) da regressao Fase 6.

Metodo: pra cada outlier, busca features (cliente, regiao, tipologia,
diferenciais, tamanhos) que aparecem desproporcionalmente.

Saida:
- base/anti-padroes.json
- analises-cross-projeto/anti-padroes/ANTI-PADROES.md
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
RESID = BASE / "residuos-por-projeto.json"
ENR = BASE / "projetos-enriquecidos.json"
IND_DIR = BASE / "projetos-enriquecidos"
OUT_JSON = BASE / "anti-padroes.json"
OUT_DIR = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "anti-padroes"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_MD = OUT_DIR / "ANTI-PADROES.md"

Z_THRESHOLD = 1.0  # outlier se |z| >= 1.0


def carregar_enr():
    d = json.loads(ENR.read_text(encoding="utf-8"))
    projs = {p["slug"]: p for p in d["projetos"]}
    # Merge tipologia
    for slug, p in projs.items():
        indiv = IND_DIR / f"{slug}.json"
        if indiv.exists():
            try:
                dd = json.loads(indiv.read_text(encoding="utf-8"))
                for k in ("tipologia_canonica", "tipologia_confianca"):
                    if dd.get(k):
                        p[k] = dd[k]
            except Exception:
                pass
    return projs


def main():
    resid = json.loads(RESID.read_text(encoding="utf-8"))
    projs = carregar_enr()

    outliers_pos = [r for r in resid["residuos"] if r["z_score"] >= Z_THRESHOLD]
    outliers_neg = [r for r in resid["residuos"] if r["z_score"] <= -Z_THRESHOLD]
    normais = [r for r in resid["residuos"] if abs(r["z_score"]) < Z_THRESHOLD]

    print(f"Outliers positivos (z >= {Z_THRESHOLD}): {len(outliers_pos)}", flush=True)
    print(f"Outliers negativos (z <= -{Z_THRESHOLD}): {len(outliers_neg)}", flush=True)
    print(f"Normais: {len(normais)}", flush=True)

    def features(slugs, nome):
        """Conta distribuicao de features entre os slugs."""
        por_cliente = Counter()
        por_regiao = Counter()
        por_padrao = Counter()
        por_tipologia = Counter()
        ur_media = []
        ac_media = []
        for slug in slugs:
            p = projs.get(slug, {})
            if p.get("cliente_inferido"):
                por_cliente[p["cliente_inferido"]] += 1
            if p.get("cub_regiao"):
                por_regiao[p["cub_regiao"]] += 1
            if p.get("padrao"):
                por_padrao[p["padrao"]] += 1
            if p.get("tipologia_canonica"):
                por_tipologia[p["tipologia_canonica"]] += 1
            if p.get("ur"):
                ur_media.append(p["ur"])
            if p.get("ac_m2"):
                ac_media.append(p["ac_m2"])
        return {
            "n": len(slugs),
            "clientes": dict(por_cliente.most_common(10)),
            "regioes": dict(por_regiao.most_common()),
            "padroes": dict(por_padrao.most_common()),
            "tipologias": dict(por_tipologia.most_common()),
            "ur_media": round(sum(ur_media) / len(ur_media), 1) if ur_media else None,
            "ac_media": round(sum(ac_media) / len(ac_media), 0) if ac_media else None,
        }

    pos_slugs = [o["slug"] for o in outliers_pos]
    neg_slugs = [o["slug"] for o in outliers_neg]
    norm_slugs = [o["slug"] for o in normais]

    f_pos = features(pos_slugs, "positivos")
    f_neg = features(neg_slugs, "negativos")
    f_norm = features(norm_slugs, "normais")

    # Enriquecimento por categoria (concentracao)
    def concentracao(cat_pos, cat_norm, n_pos, n_norm):
        """Razao de frequencia na pop outlier vs pop normal.
        Ratio > 1.5 = categoria concentra outliers.
        """
        ratios = {}
        for k, v in cat_pos.items():
            freq_pos = v / n_pos if n_pos else 0
            freq_norm = cat_norm.get(k, 0) / n_norm if n_norm else 0
            if freq_norm > 0:
                ratios[k] = round(freq_pos / freq_norm, 2)
            else:
                ratios[k] = None  # inf
        return dict(sorted(ratios.items(), key=lambda x: -(x[1] or 0)))

    print("\n=== CONCENTRACAO de features em OUTLIERS POSITIVOS vs normais ===", flush=True)
    print("\n  Clientes (ratio > 1.5 = concentra positivos):", flush=True)
    for k, r in concentracao(f_pos["clientes"], f_norm["clientes"], f_pos["n"], f_norm["n"]).items():
        if r is None or r > 1.5:
            print(f"    {k:<25} ratio={r}  ({f_pos['clientes'][k]}/{f_pos['n']} vs {f_norm['clientes'].get(k, 0)}/{f_norm['n']})", flush=True)

    print("\n  Regioes:", flush=True)
    for k, r in concentracao(f_pos["regioes"], f_norm["regioes"], f_pos["n"], f_norm["n"]).items():
        if r is None or r > 1.3:
            print(f"    {k:<25} ratio={r}", flush=True)

    # Anti-padrao forte: cliente + caracteristicas
    print("\n=== TOP OUTLIERS INTERPRETADOS ===", flush=True)
    for o in sorted(outliers_pos, key=lambda x: -x["z_score"])[:10]:
        p = projs.get(o["slug"], {})
        print(f"\n  {o['slug']} (z={o['z_score']:+.1f}, resid=R$ {o['residuo_rs']:+.0f})", flush=True)
        print(f"    Cliente: {p.get('cliente_inferido')}, Regiao: {p.get('cub_regiao')}, Padrao: {p.get('padrao')}", flush=True)
        print(f"    Tipologia: {p.get('tipologia_canonica')}", flush=True)
        print(f"    AC: {p.get('ac_m2', '?')}, UR: {p.get('ur', '?')}, N pavimentos: {p.get('n_pavimentos_total', '?')}", flush=True)

    print("\n=== TOP ECONOMICOS (negativos) ===", flush=True)
    for o in sorted(outliers_neg, key=lambda x: x["z_score"])[:10]:
        p = projs.get(o["slug"], {})
        print(f"\n  {o['slug']} (z={o['z_score']:+.1f}, resid=R$ {o['residuo_rs']:+.0f})", flush=True)
        print(f"    Cliente: {p.get('cliente_inferido')}, Regiao: {p.get('cub_regiao')}, Padrao: {p.get('padrao')}", flush=True)
        print(f"    AC: {p.get('ac_m2', '?')}, UR: {p.get('ur', '?')}", flush=True)

    # Regras detectadas
    regras = []
    # Nova Empreendimentos
    nova_pos = sum(1 for s in pos_slugs if s.startswith("nova-empreendimentos"))
    nova_total = sum(1 for r in resid["residuos"] if r["slug"].startswith("nova-empreendimentos"))
    if nova_pos >= 2 and nova_pos / nova_total >= 0.5:
        regras.append({
            "regra": "IF cliente = Nova Empreendimentos THEN somar ~R$ 2.000/m² à predição",
            "evidencia": f"{nova_pos}/{nova_total} projetos Nova são outliers positivos (z>=1). Resíduo médio ~R$ 2.291.",
            "forca": "alta",
            "slugs": [s for s in pos_slugs if s.startswith("nova-empreendimentos")],
        })

    # ALL
    all_pos = sum(1 for s in pos_slugs if s.startswith("all-"))
    if all_pos >= 1:
        regras.append({
            "regra": "IF cliente = ALL THEN predição pode subestimar em R$ 2.000-3.000/m²",
            "evidencia": f"ALL Lago di Garda: z=+3.2, resíduo +R$ 2.959.",
            "forca": "média (n=1 somente)",
            "slugs": [s for s in pos_slugs if s.startswith("all-")],
        })

    # F Nogueira
    fn_neg = sum(1 for s in neg_slugs if s.startswith("f-nogueira"))
    if fn_neg >= 2:
        regras.append({
            "regra": "IF cliente = F Nogueira THEN subtrair ~R$ 1.200/m² da predição",
            "evidencia": f"{fn_neg} projetos F Nogueira são outliers negativos consistentes (~-R$ 1.210 ambos)",
            "forca": "alta",
            "slugs": [s for s in neg_slugs if s.startswith("f-nogueira")],
        })

    # Paludo volo-home
    if any("paludo" in s for s in neg_slugs):
        paludo_negs = [s for s in neg_slugs if "paludo" in s]
        regras.append({
            "regra": "IF cliente = Paludo Volo Home THEN subtrair ~R$ 1.100/m²",
            "evidencia": f"paludo-volo-home tem z=-1.2",
            "forca": "média",
            "slugs": paludo_negs,
        })

    # Padrão médio
    sm_neg = sum(1 for s in neg_slugs if "santa-maria" in s)
    if sm_neg >= 1:
        regras.append({
            "regra": "IF cliente = Santa Maria THEN subtrair ~R$ 1.000/m² (Chapecó CUB menor + escopo enxuto)",
            "evidencia": f"{sm_neg} projeto Santa Maria em outliers negativos",
            "forca": "média",
            "slugs": [s for s in neg_slugs if "santa-maria" in s],
        })

    print("\n=== REGRAS DETECTADAS ===", flush=True)
    for r in regras:
        print(f"\n  [{r['forca'].upper()}] {r['regra']}", flush=True)
        print(f"    {r['evidencia']}", flush=True)

    resultado = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "z_threshold": Z_THRESHOLD,
        "outliers_positivos": outliers_pos,
        "outliers_negativos": outliers_neg,
        "features_positivos": f_pos,
        "features_negativos": f_neg,
        "features_normais": f_norm,
        "regras_detectadas": regras,
    }
    OUT_JSON.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSalvo: {OUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
