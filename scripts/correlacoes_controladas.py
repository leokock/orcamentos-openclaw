#!/usr/bin/env python3
"""Fase 5 — Correlacoes controladas + stratificadas + PCA + clustering.

Responde perguntas como:
- Economia de escala (AC vs R$/m²) sobrevive ao controle por CUB-regiao?
- Gerenciamento alto causa R$/m² alto ou e so correlacao espuria?
- Quais 4-5 componentes explicam 80% da variacao nos 49 indicadores?
- Quais clusters emergem do dendrograma (alternativa a K-means)?

Saidas:
- base/correlacoes-controladas.json
- analises-cross-projeto/correlacoes-controladas/ (Excel + MD)
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from scipy import stats
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

BASE = Path.home() / "orcamentos-openclaw" / "base"
ENR_FILE = BASE / "projetos-enriquecidos.json"
IDX_DIR = BASE / "indices-executivo"
PROD_DIR = BASE / "indicadores-produto"
OUT_JSON = BASE / "correlacoes-controladas.json"
OUT_DIR = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "correlacoes-controladas"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def carregar_df():
    """Constroi DataFrame com 131 projetos + colunas relevantes."""
    enr = json.loads(ENR_FILE.read_text(encoding="utf-8"))
    projetos = enr["projetos"]

    # Merge com tipologia dos arquivos individuais
    ind_dir = BASE / "projetos-enriquecidos"
    for p in projetos:
        indiv = ind_dir / f"{p['slug']}.json"
        if indiv.exists():
            try:
                d = json.loads(indiv.read_text(encoding="utf-8"))
                for k in ("tipologia_canonica", "tipologia_confianca"):
                    if d.get(k):
                        p[k] = d[k]
            except Exception:
                pass

    # Adiciona indicadores produto + macrogrupos
    for p in projetos:
        slug = p["slug"]
        # Indicadores produto
        prod_f = PROD_DIR / f"{slug}.json"
        if prod_f.exists():
            try:
                pd_ = json.loads(prod_f.read_text(encoding="utf-8"))
                for name, info in pd_.get("indicadores", {}).items():
                    v = info.get("valor") if isinstance(info, dict) else info
                    if v is not None:
                        p[f"ind_{name}"] = v
            except Exception:
                pass

        # Macrogrupos % do total
        idx_f = IDX_DIR / f"{slug}.json"
        if idx_f.exists():
            try:
                d = json.loads(idx_f.read_text(encoding="utf-8"))
                total = d.get("total") or 0
                if total > 0:
                    from collections import defaultdict
                    mg_canon = defaultdict(float)
                    for k, v in (d.get("macrogrupos") or {}).items():
                        val = v.get("valor") if isinstance(v, dict) else (v or 0)
                        if val and val > 0:
                            canon = _canonize_mg(k)
                            mg_canon[canon] += val
                    for c, v in mg_canon.items():
                        p[f"mg_pct_{c.lower().replace(' ', '_')}"] = round(v / total * 100, 2)
            except Exception:
                pass

    df = pd.DataFrame(projetos)
    return df


def _canonize_mg(raw):
    import unicodedata
    r = str(raw or "").lower()
    r = unicodedata.normalize("NFKD", r)
    r = "".join(c for c in r if unicodedata.category(c) != "Mn")
    r = r.strip().lstrip("0123456789. ")
    mapa = [
        ("Gerenciamento", ["gerenciamento", "ger. tec", "ger tec"]),
        ("Supraestrutura", ["supraestrutura", "estrutura de concreto"]),
        ("Infraestrutura", ["infraestrutura", "fundac", "contenc", "estaca", "baldram"]),
        ("Alvenaria", ["alvenaria", "vedac", "divisori"]),
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
        ("Mov Terra", ["mov", "terra", "terraplan"]),
        ("Impermeabilizacao", ["impermeab", "tratament"]),
    ]
    for canon, kws in mapa:
        for kw in kws:
            if kw in r:
                return canon
    return "Outros"


def correlacao_pearson(x, y):
    """Pearson r + p-value. Ignora NaN."""
    pairs = [(xi, yi) for xi, yi in zip(x, y) if not (pd.isna(xi) or pd.isna(yi))]
    if len(pairs) < 3:
        return None
    xs, ys = zip(*pairs)
    try:
        r, p = stats.pearsonr(xs, ys)
        return {"r": round(r, 3), "p": round(p, 4), "n": len(pairs)}
    except Exception:
        return None


def correlacao_parcial(df, x, y, z_col):
    """r(X, Y | Z) — correlacao parcial.

    Residualizacao: fit OLS de X sobre Z e Y sobre Z; correlaciona residuos.
    Z_col pode ser categorica (converte via dummies).
    """
    sub = df[[x, y, z_col]].dropna()
    if len(sub) < 5:
        return None
    try:
        # Dummies pra Z categorica (string ou object)
        if sub[z_col].dtype.kind in ("O", "U", "S"):  # object, unicode, string
            z_dummies = pd.get_dummies(sub[z_col], drop_first=True).astype(float)
            if z_dummies.shape[1] == 0:
                return None
        elif sub[z_col].dtype.kind == "f" or sub[z_col].dtype.kind == "i":
            z_dummies = sub[[z_col]].astype(float)
        else:
            # Fallback: tenta como categoria
            z_dummies = pd.get_dummies(sub[z_col].astype(str), drop_first=True).astype(float)
            if z_dummies.shape[1] == 0:
                return None

        # Residualiza X sobre Z
        z_mat = z_dummies.values
        z_mat_aug = np.column_stack([np.ones(len(z_mat)), z_mat])
        x_vals = sub[x].astype(float).values
        y_vals = sub[y].astype(float).values

        beta_x, *_ = np.linalg.lstsq(z_mat_aug, x_vals, rcond=None)
        beta_y, *_ = np.linalg.lstsq(z_mat_aug, y_vals, rcond=None)
        res_x = x_vals - z_mat_aug @ beta_x
        res_y = y_vals - z_mat_aug @ beta_y

        r, p = stats.pearsonr(res_x, res_y)
        return {"r_parcial": round(r, 3), "p": round(p, 4), "n": len(sub), "controle": z_col}
    except Exception as e:
        return {"erro": str(e)[:100]}


def analisar_correlacoes(df):
    """Roda baterias de correlacoes: simples, parciais, stratificadas."""
    numericas = [c for c in df.columns if df[c].dtype in ("float64", "int64")
                 and df[c].notna().sum() >= 20]

    # Foca em variáveis-chave
    vars_chave = [
        "ac_m2", "ur", "total_rs", "rsm2",
        "concreto_m3_m2_ac", "taxa_aco_kg_m3", "forma_m2_m2_ac",
        "mg_pct_supraestrutura", "mg_pct_gerenciamento", "mg_pct_esquadrias",
        "mg_pct_fachada", "mg_pct_hidrossanitaria", "mg_pct_eletrica",
    ]
    vars_chave = [v for v in vars_chave if v in numericas]

    resultados = {
        "correlacoes_simples": {},
        "correlacoes_stratificadas": {},
        "correlacoes_parciais": {},
    }

    # 1. Correlacoes simples entre vars-chave
    for i, v1 in enumerate(vars_chave):
        for v2 in vars_chave[i + 1:]:
            r = correlacao_pearson(df[v1], df[v2])
            if r and abs(r["r"]) > 0.2 and r["n"] >= 20:
                resultados["correlacoes_simples"][f"{v1} ~ {v2}"] = r

    # 2. Correlacoes stratificadas por cub_regiao
    #    r(ac, rsm2) dentro de cada regiao
    pares_importantes = [("ac_m2", "rsm2"), ("ac_m2", "total_rs"),
                         ("mg_pct_gerenciamento", "rsm2"),
                         ("mg_pct_supraestrutura", "rsm2"),
                         ("taxa_aco_kg_m3", "rsm2")]
    for par in pares_importantes:
        v1, v2 = par
        if v1 not in df.columns or v2 not in df.columns:
            continue
        chave = f"{v1} ~ {v2}"
        resultados["correlacoes_stratificadas"][chave] = {}
        for regiao in df["cub_regiao"].dropna().unique():
            sub = df[df["cub_regiao"] == regiao]
            if len(sub) < 5:
                continue
            r = correlacao_pearson(sub[v1], sub[v2])
            if r:
                resultados["correlacoes_stratificadas"][chave][regiao] = r

    # 3. Correlacoes parciais — r(AC, rsm2 | cub_regiao)
    for par in pares_importantes:
        v1, v2 = par
        if v1 not in df.columns or v2 not in df.columns:
            continue
        key = f"{v1} ~ {v2} | cub_regiao"
        r = correlacao_parcial(df, v1, v2, "cub_regiao")
        if r and "erro" not in r:
            resultados["correlacoes_parciais"][key] = r
            # Comparar com simples
            r_simples = correlacao_pearson(df[v1], df[v2])
            if r_simples:
                resultados["correlacoes_parciais"][key]["r_simples_comparacao"] = r_simples["r"]
                resultados["correlacoes_parciais"][key]["delta_r"] = round(r["r_parcial"] - r_simples["r"], 3)

        # Tambem parcial controlando por padrao
        key_pad = f"{v1} ~ {v2} | padrao"
        r_pad = correlacao_parcial(df, v1, v2, "padrao")
        if r_pad and "erro" not in r_pad:
            resultados["correlacoes_parciais"][key_pad] = r_pad

    return resultados, numericas


def pca_analise(df, vars_cols):
    """PCA sobre indicadores numericos — 5 primeiros componentes."""
    X = df[vars_cols].dropna(thresh=int(len(vars_cols) * 0.7))  # projs com 70%+ dos campos
    if len(X) < 20 or X.shape[1] < 5:
        return {"erro": "dados insuficientes", "n": len(X), "cols": X.shape[1]}

    X_filled = X.fillna(X.median())
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_filled)

    n_comp = min(5, X.shape[1], len(X) - 1)
    pca = PCA(n_components=n_comp)
    X_pca = pca.fit_transform(X_scaled)

    componentes = []
    for i, var_exp in enumerate(pca.explained_variance_ratio_):
        # Top 5 vars que mais pesam no componente
        loadings = pca.components_[i]
        top_idx = np.argsort(np.abs(loadings))[::-1][:8]
        top_vars = [{"variavel": vars_cols[j], "loading": round(float(loadings[j]), 3)}
                    for j in top_idx]
        componentes.append({
            "componente": f"PC{i+1}",
            "variancia_explicada": round(float(var_exp), 3),
            "variancia_acumulada": round(float(np.sum(pca.explained_variance_ratio_[:i+1])), 3),
            "top_variaveis": top_vars,
        })

    return {
        "n_projetos_usados": len(X),
        "n_variaveis": X.shape[1],
        "variaveis_usadas": vars_cols,
        "componentes": componentes,
    }


def clusterizar(df, vars_cols):
    """Clustering hierarquico (Ward) sobre assinatura % MG."""
    mg_cols = [c for c in df.columns if c.startswith("mg_pct_")]
    if len(mg_cols) < 5:
        return {"erro": "poucas colunas MG"}

    X = df[["slug"] + mg_cols].dropna(thresh=int(len(mg_cols) * 0.7))
    if len(X) < 10:
        return {"erro": "poucos projetos"}

    slugs = X["slug"].tolist()
    X_vals = X[mg_cols].fillna(0).values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_vals)

    Z = linkage(X_scaled, method="ward")
    labels_4 = fcluster(Z, t=4, criterion="maxclust")
    labels_6 = fcluster(Z, t=6, criterion="maxclust")

    # Agrupa projetos por label
    clusters_4 = defaultdict(list)
    clusters_6 = defaultdict(list)
    for slug, l4, l6 in zip(slugs, labels_4, labels_6):
        clusters_4[int(l4)].append(slug)
        clusters_6[int(l6)].append(slug)

    return {
        "n_projetos_usados": len(X),
        "metodo": "hierarquico ward",
        "colunas_usadas": mg_cols,
        "clusters_4": {f"cluster_{k}": sorted(v) for k, v in clusters_4.items()},
        "clusters_6": {f"cluster_{k}": sorted(v) for k, v in clusters_6.items()},
    }


def main():
    print("Carregando dados...", flush=True)
    df = carregar_df()
    print(f"  {len(df)} projetos, {len(df.columns)} colunas", flush=True)

    print("\n=== CORRELACOES ===", flush=True)
    corr_res, numericas = analisar_correlacoes(df)
    print(f"  Correlacoes simples |r|>0.2: {len(corr_res['correlacoes_simples'])}", flush=True)
    print(f"  Stratificadas por cub_regiao: {sum(len(v) for v in corr_res['correlacoes_stratificadas'].values())} grupos", flush=True)
    print(f"  Parciais: {len(corr_res['correlacoes_parciais'])}", flush=True)

    # Print correlacoes importantes
    print("\n  TOP correlacoes simples:", flush=True)
    sorted_simples = sorted(corr_res["correlacoes_simples"].items(),
                             key=lambda x: -abs(x[1]["r"]))[:10]
    for pair, r in sorted_simples:
        print(f"    {pair:<60} r={r['r']:+.3f}  p={r['p']:.4f}  n={r['n']}", flush=True)

    print("\n  STRATIFICADAS AC vs rsm2:", flush=True)
    for regiao, r in corr_res["correlacoes_stratificadas"].get("ac_m2 ~ rsm2", {}).items():
        print(f"    {regiao:<25} r={r['r']:+.3f}  p={r['p']:.4f}  n={r['n']}", flush=True)

    print("\n  PARCIAIS (controle):", flush=True)
    for par, r in corr_res["correlacoes_parciais"].items():
        delta = r.get("delta_r")
        delta_str = f"  Δ={delta:+.3f}" if delta is not None else ""
        print(f"    {par:<50} r_parcial={r['r_parcial']:+.3f}  n={r['n']}{delta_str}", flush=True)

    print("\n=== PCA ===", flush=True)
    # Vars pra PCA: indicadores produto + MG%
    vars_pca = [c for c in df.columns
                if (c.startswith("ind_") or c.startswith("mg_pct_"))
                and df[c].notna().sum() >= 20]
    pca_res = pca_analise(df, vars_pca[:30])  # limite 30 vars pra scale
    if "erro" not in pca_res:
        for comp in pca_res["componentes"]:
            print(f"  {comp['componente']}: var explicada {comp['variancia_explicada']:.1%} (acum {comp['variancia_acumulada']:.1%})", flush=True)
            for tv in comp["top_variaveis"][:3]:
                print(f"    {tv['variavel']:<40} loading={tv['loading']:+.3f}", flush=True)

    print("\n=== CLUSTERING HIERARQUICO (Ward) ===", flush=True)
    clust_res = clusterizar(df, None)
    if "erro" not in clust_res:
        print(f"  {clust_res['n_projetos_usados']} projetos", flush=True)
        print(f"  4 clusters:", flush=True)
        for cn, slugs in clust_res["clusters_4"].items():
            print(f"    {cn}: {len(slugs)} projetos — ex: {slugs[:3]}", flush=True)

    # Salva tudo
    out = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len(df),
        "correlacoes": corr_res,
        "pca": pca_res,
        "clustering": clust_res,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"\nSalvo: {OUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
