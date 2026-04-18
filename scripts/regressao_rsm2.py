#!/usr/bin/env python3
"""Fase 6 — Regressao multivariada R$/m² ~ AC + cub_regiao + padrao + tipologia.

Usa OLS (Ordinary Least Squares) com dummies pra categoricas. Mede R², coeficientes,
intervalos de confianca e residuos (pra Fase 7).

Saidas:
- base/regressao-rsm2.json (coeficientes + stats)
- base/residuos-por-projeto.json (resíduo de cada projeto, pra Fase 7)
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

BASE = Path.home() / "orcamentos-openclaw" / "base"
ENR_FILE = BASE / "projetos-enriquecidos.json"
IND_DIR = BASE / "projetos-enriquecidos"
OUT_COEFS = BASE / "regressao-rsm2.json"
OUT_RESIDUOS = BASE / "residuos-por-projeto.json"


def carregar_df():
    enr = json.loads(ENR_FILE.read_text(encoding="utf-8"))
    projetos = enr["projetos"]
    # Merge tipologia
    for p in projetos:
        indiv = IND_DIR / f"{p['slug']}.json"
        if indiv.exists():
            try:
                d = json.loads(indiv.read_text(encoding="utf-8"))
                for k in ("tipologia_canonica", "tipologia_confianca"):
                    if d.get(k):
                        p[k] = d[k]
            except Exception:
                pass
    return pd.DataFrame(projetos)


def rodar_regressao(df: pd.DataFrame, features_cat: list, target: str = "rsm2"):
    """OLS com dummies pra categoricas + log AC."""
    sub = df[df[target].notna() & (df[target] > 500) & (df[target] < 10000)].copy()
    sub = sub[sub["ac_m2"].notna() & (sub["ac_m2"] >= 1000)]
    if len(sub) < 30:
        return {"erro": f"amostra pequena: n={len(sub)}"}

    # Prepara features
    sub["log_ac"] = np.log(sub["ac_m2"])
    X_num = sub[["log_ac"]].values

    # Dummies
    X_parts = [X_num]
    feature_names = ["log_ac"]
    for cat in features_cat:
        if cat not in sub.columns:
            continue
        dummies = pd.get_dummies(sub[cat].fillna("_missing"), prefix=cat, drop_first=True)
        if dummies.shape[1] > 0:
            X_parts.append(dummies.values.astype(float))
            feature_names.extend(dummies.columns.tolist())

    X = np.hstack(X_parts)
    y = sub[target].values.astype(float)
    slugs = sub["slug"].tolist()

    # OLS
    reg = LinearRegression()
    reg.fit(X, y)
    y_pred = reg.predict(X)
    r2 = r2_score(y, y_pred)
    residuals = y - y_pred

    # Bootstrap IC 95% dos coeficientes
    n_boot = 300
    rng = np.random.default_rng(42)
    coefs_boot = np.zeros((n_boot, len(feature_names) + 1))  # +1 for intercept
    for b in range(n_boot):
        idx = rng.integers(0, len(X), len(X))
        r = LinearRegression()
        r.fit(X[idx], y[idx])
        coefs_boot[b, 0] = r.intercept_
        coefs_boot[b, 1:] = r.coef_

    coefs_lower = np.percentile(coefs_boot, 2.5, axis=0)
    coefs_upper = np.percentile(coefs_boot, 97.5, axis=0)

    # Monta saida
    coefs_info = []
    coefs_info.append({
        "feature": "intercept",
        "coef": round(float(reg.intercept_), 2),
        "ic_95_low": round(float(coefs_lower[0]), 2),
        "ic_95_high": round(float(coefs_upper[0]), 2),
    })
    for i, name in enumerate(feature_names):
        coefs_info.append({
            "feature": name,
            "coef": round(float(reg.coef_[i]), 2),
            "ic_95_low": round(float(coefs_lower[i + 1]), 2),
            "ic_95_high": round(float(coefs_upper[i + 1]), 2),
            "significativo": bool((coefs_lower[i + 1] * coefs_upper[i + 1]) > 0),  # mesmo sinal
        })

    # Residuos por projeto
    residuos_info = []
    std_resid = np.std(residuals)
    for slug, y_real, y_p, resid in zip(slugs, y, y_pred, residuals):
        z = (resid / std_resid) if std_resid > 0 else 0
        residuos_info.append({
            "slug": slug,
            "rsm2_real": round(float(y_real), 2),
            "rsm2_previsto": round(float(y_p), 2),
            "residuo_rs": round(float(resid), 2),
            "residuo_pct": round(float(resid / y_real * 100), 2),
            "z_score": round(float(z), 2),
        })

    return {
        "n_projetos": len(sub),
        "r2": round(float(r2), 4),
        "rmse": round(float(np.sqrt(np.mean(residuals ** 2))), 2),
        "mae": round(float(np.mean(np.abs(residuals))), 2),
        "std_residuo": round(float(std_resid), 2),
        "coeficientes": coefs_info,
        "residuos": residuos_info,
        "features_usadas": feature_names,
    }


def main():
    df = carregar_df()
    print(f"Base: {len(df)} projetos", flush=True)

    print("\n=== REGRESSAO R$/m² ~ log(AC) + cub_regiao + padrao + tipologia ===", flush=True)
    result = rodar_regressao(df, ["cub_regiao", "padrao", "tipologia_canonica"])

    if "erro" in result:
        print(f"ERRO: {result['erro']}", flush=True)
        return

    print(f"\nn = {result['n_projetos']}", flush=True)
    print(f"R² = {result['r2']:.4f}", flush=True)
    print(f"RMSE = R$ {result['rmse']}/m²", flush=True)
    print(f"MAE = R$ {result['mae']}/m²", flush=True)

    print(f"\n=== COEFICIENTES (|efeito| > R$ 100/m²) ===", flush=True)
    coefs = sorted(result["coeficientes"], key=lambda c: -abs(c["coef"]))
    for c in coefs:
        if abs(c["coef"]) > 100 or c["feature"] == "intercept":
            sig = "*" if c.get("significativo") else " "
            print(f"  {sig} {c['feature']:<45} {c['coef']:+9.2f}  IC95: [{c['ic_95_low']:+.0f}, {c['ic_95_high']:+.0f}]", flush=True)

    # Top outliers (Fase 7 preview)
    print(f"\n=== TOP 10 RESIDUOS POSITIVOS (projetos MAIS CAROS que o esperado) ===", flush=True)
    resids_pos = sorted(result["residuos"], key=lambda r: -r["residuo_rs"])[:10]
    for r in resids_pos:
        print(f"  {r['slug']:<35} real=R$ {r['rsm2_real']:>6.0f}  prev=R$ {r['rsm2_previsto']:>6.0f}  resid=R$ {r['residuo_rs']:+.0f} ({r['residuo_pct']:+.1f}%, z={r['z_score']:+.1f})", flush=True)

    print(f"\n=== TOP 10 RESIDUOS NEGATIVOS (projetos MAIS BARATOS que o esperado) ===", flush=True)
    resids_neg = sorted(result["residuos"], key=lambda r: r["residuo_rs"])[:10]
    for r in resids_neg:
        print(f"  {r['slug']:<35} real=R$ {r['rsm2_real']:>6.0f}  prev=R$ {r['rsm2_previsto']:>6.0f}  resid=R$ {r['residuo_rs']:+.0f} ({r['residuo_pct']:+.1f}%, z={r['z_score']:+.1f})", flush=True)

    # Salva
    OUT_COEFS.write_text(json.dumps({
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": result["n_projetos"],
        "r2": result["r2"],
        "rmse": result["rmse"],
        "mae": result["mae"],
        "std_residuo": result["std_residuo"],
        "features_usadas": result["features_usadas"],
        "coeficientes": result["coeficientes"],
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    OUT_RESIDUOS.write_text(json.dumps({
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": result["n_projetos"],
        "std_residuo": result["std_residuo"],
        "residuos": result["residuos"],
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nSalvo: {OUT_COEFS}", flush=True)
    print(f"Salvo: {OUT_RESIDUOS}", flush=True)


if __name__ == "__main__":
    main()
