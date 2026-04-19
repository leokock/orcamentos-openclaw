#!/usr/bin/env python3
"""Fase 9 — Regras textuais via Qwen.

Traduz as descobertas quantitativas (Fases 5-7) em regras if-then textuais
em PT-BR, acionáveis por orçamentistas humanos.

Input: correlacoes-controladas.json, regressao-rsm2.json, anti-padroes.json,
       analise-enriquecida-agregada.json

Output: analises-cross-projeto/regras-produto/REGRAS-PRODUTO.md
"""
from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "regras-produto"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_MD = OUT_DIR / "REGRAS-PRODUTO.md"
OUT_JSON = OUT_DIR / "regras-estruturadas.json"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:14b"


def call_qwen(prompt: str, timeout: int = 180) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": 1500,
            "num_ctx": 8192,
        },
    }, timeout=timeout)
    r.raise_for_status()
    return r.json().get("response", "").strip()


def carregar_achados():
    """Carrega achados quantitativos das Fases 5-7."""
    corr = json.loads((BASE / "correlacoes-controladas.json").read_text(encoding="utf-8"))
    regr = json.loads((BASE / "regressao-rsm2.json").read_text(encoding="utf-8"))
    anti = json.loads((BASE / "anti-padroes.json").read_text(encoding="utf-8"))
    agg = json.loads((BASE / "analise-enriquecida-agregada.json").read_text(encoding="utf-8"))
    return corr, regr, anti, agg


def gerar_narrativa_regra(regra: dict, qwen: bool = True) -> str:
    """Pede pro Qwen escrever explicação PT-BR de 1 regra específica."""
    if not qwen:
        return f"{regra['regra']}\n\nEvidência: {regra['evidencia']}"

    prompt = f"""Você é consultor senior de orçamento de construção civil da Cartesian Engenharia.

Reescreva a regra abaixo como **recomendação acionável em PT-BR (1-2 parágrafos curtos)** que um orçamentista pode aplicar hoje.

Seja direto. Explique:
1. Quando aplicar a regra
2. Qual o ajuste a fazer
3. Por que (evidência resumida)

REGRA ORIGINAL:
{regra['regra']}

EVIDÊNCIA:
{regra['evidencia']}

FORÇA: {regra['forca']}

RESPOSTA (PT-BR, direto, sem rodeios, sem repetir o título):"""

    try:
        resp = call_qwen(prompt)
        return resp[:2000]
    except Exception as e:
        return f"[falha qwen: {e}] | {regra['regra']} — {regra['evidencia']}"


def construir_secoes(corr, regr, anti, agg):
    """Constrói seções do MD estruturado."""
    secoes = []

    # 1. Regras de cliente (Fase 7)
    regras_cliente = anti.get("regras_detectadas", [])
    secoes.append({
        "titulo": "Regras de Cliente (ajustes aprendidos)",
        "subtitulo": f"Derivadas da análise de {len(anti.get('outliers_positivos', [])) + len(anti.get('outliers_negativos', []))} outliers da regressão multivariada",
        "regras": regras_cliente,
    })

    # 2. Regras regionais (derivadas da regressão)
    coefs = {c["feature"]: c["coef"] for c in regr.get("coeficientes", [])}
    regras_reg = []
    for feat, coef in coefs.items():
        if feat.startswith("cub_regiao_") and abs(coef) > 300:
            reg_nome = feat.replace("cub_regiao_", "")
            regras_reg.append({
                "regra": f"IF região = {reg_nome} THEN ajustar {coef:+.0f} R$/m² vs baseline (SC-BC)",
                "evidencia": f"Coef regressão = R$ {coef:+.0f}/m². Baseline é SC-BC.",
                "forca": "alta" if abs(coef) > 700 else "média",
            })
    secoes.append({
        "titulo": "Regras Regionais (CUB)",
        "subtitulo": "Derivadas dos coeficientes da regressão Fase 6 (baseline: SC-BC)",
        "regras": regras_reg,
    })

    # 3. Regras de padrão
    regras_pad = []
    for feat, coef in coefs.items():
        if feat.startswith("padrao_") and abs(coef) > 300:
            pad_nome = feat.replace("padrao_", "")
            regras_pad.append({
                "regra": f"IF padrão = {pad_nome} THEN ajustar {coef:+.0f} R$/m² vs baseline (alto)",
                "evidencia": f"Coef regressão = R$ {coef:+.0f}/m². Baseline é padrão alto.",
                "forca": "alta" if abs(coef) > 1500 else "média",
            })
    secoes.append({
        "titulo": "Regras de Padrão Construtivo",
        "subtitulo": "Derivadas dos coeficientes da regressão Fase 6 (baseline: padrão alto)",
        "regras": regras_pad,
    })

    # 4. Regras de correlação parcial (Fase 5) — causais
    regras_causais = []
    parciais = corr.get("correlacoes", {}).get("correlacoes_parciais", {})

    # Economia de escala real
    ac_rsm2_reg = parciais.get("ac_m2 ~ rsm2 | cub_regiao")
    if ac_rsm2_reg:
        regras_causais.append({
            "regra": "Economia de escala real mas leve (controlando região)",
            "evidencia": f"r parcial = {ac_rsm2_reg.get('r_parcial')} (n={ac_rsm2_reg.get('n')}). Projetos maiores TÊM R$/m² um pouco menor mesmo dentro da mesma região.",
            "forca": "média",
        })

    # Supra% não causa R$/m² alto
    supra_rsm2 = parciais.get("mg_pct_supraestrutura ~ rsm2 | cub_regiao")
    if supra_rsm2 and abs(supra_rsm2.get("r_parcial", 1)) < 0.1:
        regras_causais.append({
            "regra": "Supraestrutura% ≠ preditor de R$/m² alto",
            "evidencia": f"r parcial = {supra_rsm2.get('r_parcial')} (NULO). Correlação simples era artefato regional. NÃO usar supra% pra estimar preço.",
            "forca": "alta",
        })

    # Gerenciamento%
    ger_rsm2 = parciais.get("mg_pct_gerenciamento ~ rsm2 | cub_regiao")
    if ger_rsm2 and abs(ger_rsm2.get("r_parcial", 1)) < 0.2:
        regras_causais.append({
            "regra": "Gerenciamento% alto ≠ projeto caro",
            "evidencia": f"r parcial = {ger_rsm2.get('r_parcial')}. Projetos EPCM (gerenciamento concentrado) não são intrinsecamente caros. Preço alto vem de escopo/região/especificação, não da estrutura de orçamento.",
            "forca": "alta",
        })

    secoes.append({
        "titulo": "Regras Causais (Controle de Confundidores)",
        "subtitulo": "Derivadas de correlações parciais Fase 5 — refutam correlações aparentes",
        "regras": regras_causais,
    })

    # 5. Regras de economia de escala heterogênea (stratificação)
    strat = corr.get("correlacoes", {}).get("correlacoes_stratificadas", {}).get("ac_m2 ~ rsm2", {})
    regras_escala = []
    for regiao, info in strat.items():
        r = info.get("r", 0)
        if abs(r) > 0.3 and info.get("n", 0) >= 10:
            direcao = "aumentar AC reduz R$/m²" if r < 0 else "aumentar AC aumenta R$/m²"
            regras_escala.append({
                "regra": f"IF região = {regiao} THEN {direcao}",
                "evidencia": f"r = {r:+.2f} (n={info['n']}). Economia de escala forte/moderada.",
                "forca": "média" if info["n"] < 15 else "alta",
            })
    if regras_escala:
        secoes.append({
            "titulo": "Regras de Economia de Escala (por região)",
            "subtitulo": "Heterogêneas — só algumas regiões têm efeito escala",
            "regras": regras_escala,
        })

    return secoes


def main():
    print("Carregando achados...", flush=True)
    corr, regr, anti, agg = carregar_achados()

    print("Construindo seções...", flush=True)
    secoes = construir_secoes(corr, regr, anti, agg)
    total_regras = sum(len(s["regras"]) for s in secoes)
    print(f"  {len(secoes)} seções, {total_regras} regras totais", flush=True)

    # Gera narrativas via Qwen
    print(f"\nGerando narrativas via Qwen (~{total_regras}×15s = ~{total_regras*15//60}min)...", flush=True)
    for s in secoes:
        for i, regra in enumerate(s["regras"]):
            t0 = time.time()
            regra["narrativa_ptbr"] = gerar_narrativa_regra(regra, qwen=True)
            print(f"  [{s['titulo'][:30]:<30}] {i+1}/{len(s['regras'])} ({time.time()-t0:.1f}s)", flush=True)

    # Gera MD final
    lines = [
        "# Regras de Produto — Conhecimento Acionável Cartesian",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Modelo narrativa:** qwen2.5:14b (local)",
        f"**Base estatística:** {total_regras} regras derivadas das Fases 5-7",
        "",
        "**O que tem aqui:** regras if-then testáveis que emergem das análises quantitativas, "
        "traduzidas em linguagem acionável pra reunião comercial e orçamentação.",
        "",
        "**Como usar:** antes de fechar paramétrico/executivo novo, revisar as regras aplicáveis "
        "ao projeto (cliente, região, padrão). Ajuste as estimativas conforme indicado.",
        "",
        "---",
        "",
    ]

    for i, s in enumerate(secoes, start=1):
        lines.append(f"## {i}. {s['titulo']}")
        lines.append("")
        lines.append(f"*{s['subtitulo']}*")
        lines.append("")

        for j, regra in enumerate(s["regras"], start=1):
            forca = regra.get("forca", "média")
            emoji = "🟢" if forca == "alta" else "🟡" if forca == "média" else "⚪"
            lines.append(f"### {i}.{j} {emoji} {regra['regra']}")
            lines.append("")
            lines.append(f"**Força:** {forca}")
            lines.append("")
            lines.append(f"**Evidência:** {regra['evidencia']}")
            lines.append("")
            narrativa = regra.get("narrativa_ptbr", "")
            if narrativa and not narrativa.startswith("[falha"):
                lines.append("**Recomendação prática:**")
                lines.append("")
                lines.append("> " + narrativa.replace("\n", "\n> "))
                lines.append("")

        lines.append("---")
        lines.append("")

    # Legenda
    lines.extend([
        "## Legenda",
        "",
        "- 🟢 **Alta** — n ≥ 10 ou coeficiente > R$ 1.000/m² ou |r| ≥ 0.5",
        "- 🟡 **Média** — n entre 3-9 ou coeficiente entre R$ 500-1.000",
        "- ⚪ **Baixa** — n < 3 ou evidência indireta",
        "",
        "## Procedência das evidências",
        "",
        "- **Fase 5 (correlações controladas):** `base/correlacoes-controladas.json`",
        "- **Fase 6 (regressão):** `base/regressao-rsm2.json`",
        "- **Fase 7 (anti-padrões):** `base/anti-padroes.json`",
        "- **Validação final (Fase 11):** `analises-cross-projeto/simulador/arthen-arboris.md`",
    ])

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    OUT_JSON.write_text(json.dumps({
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "total_regras": total_regras,
        "secoes": secoes,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nSalvo: {OUT_MD}", flush=True)
    print(f"Salvo: {OUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
