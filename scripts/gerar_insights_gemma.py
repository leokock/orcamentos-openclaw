#!/usr/bin/env python3
"""Phase 20d — Insights qualitativos por projeto via Gemma.

Para cada projeto, envia resumo dos indicadores + desvios vs benchmark
ao Gemma e recebe análise narrativa curta (3-4 frases).

Pipeline retomável:
- Fila em base/phase20-insights-queue.json
- Output em base/indicadores-produto/{slug}.insight.txt

Uso:
    python scripts/gerar_insights_gemma.py
    python scripts/gerar_insights_gemma.py --slug thozen-mirador
    python scripts/gerar_insights_gemma.py --limit 10
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
IND_DIR = BASE / "indicadores-produto"
AGG_FILE = BASE / "indicadores-produto-agregados.json"
QUEUE = BASE / "phase20-insights-queue.json"
LOG = BASE / "phase20-insights.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"


def _load_json(p: Path):
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_prompt(slug: str, projeto_data: dict, agg: dict) -> str:
    """Prompt narrativo curto — pede Gemma pra comentar o projeto."""
    merged = projeto_data.get("merged_indicadores", {})
    padrao = projeto_data.get("padrao", "desconhecido")
    ac = projeto_data.get("ac_m2") or 0
    ur = projeto_data.get("ur") or 0
    rsm2 = projeto_data.get("rsm2") or 0

    # Descobre quais indicadores estão fora da faixa p25-p75 vs benchmark do padrão
    ind_por_pad = agg.get("indicadores_por_padrao", {}).get(padrao, {}).get("indicadores", {})
    desvios = []
    for name, v in merged.items():
        if v is None or not isinstance(v, (int, float)):
            continue
        ref = ind_por_pad.get(name)
        if not ref or ref.get("n", 0) < 5:
            continue
        p25, p75, med = ref.get("p25"), ref.get("p75"), ref.get("mediana")
        if p25 and p75 and med:
            if v < p25:
                desvios.append(f"{name}={v:.2f} (abaixo, mediana {med:.2f})")
            elif v > p75:
                desvios.append(f"{name}={v:.2f} (acima, mediana {med:.2f})")

    desvios_txt = "\n".join(f"- {d}" for d in desvios[:10]) if desvios else "- sem desvios relevantes"

    # Top 5 indicadores principais
    top_inds = sorted(merged.items(), key=lambda x: -(x[1] or 0))[:5]
    top_txt = "\n".join(f"- {k}: {v:.3f}" for k, v in top_inds if v)

    return f"""Você é um analista de orçamento de construção civil. Comente em PT-BR, 3 frases curtas, o projeto abaixo.

Projeto: {slug}
Padrão construtivo: {padrao}
Área construída: {ac:.0f} m²
Unidades residenciais: {ur}
R$/m²: {rsm2:.0f}

Indicadores principais:
{top_txt}

Desvios vs benchmark {padrao}:
{desvios_txt}

Escreva 3 frases curtas:
1. Caracterize o projeto (padrão, escala).
2. Comente o desvio mais relevante (se houver).
3. Sugira uma otimização ou destaque positivo.

Máximo 80 palavras. Português direto, sem rodeios."""


def call_gemma(prompt: str, timeout: int = 120) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "top_p": 0.95,
            "num_predict": 250,
            "num_ctx": 2048,
        },
    }, timeout=timeout)
    r.raise_for_status()
    return r.json().get("response", "").strip()


def log_event(e: dict):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue(agg: dict) -> dict:
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    slugs = [p["slug"] for p in agg.get("projeto_matrix", [])]
    q = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "phase": "phase20-insights",
        "items": {s: {"status": "pending"} for s in slugs},
    }
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    return q


def save_queue(q: dict):
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def get_project_data(slug: str, agg: dict) -> dict:
    """Extrai dados do projeto do agregado."""
    for p in agg.get("projeto_matrix", []):
        if p.get("slug") == slug:
            return p
    return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default=None)
    ap.add_argument("--limit", type=int, default=None, help="limit to first N projects")
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    agg = _load_json(AGG_FILE)
    if not agg:
        print("ERROR: aggregated file not found. Run agregar first.")
        return

    q = init_queue(agg)
    pending = [s for s, v in q["items"].items()
               if v["status"] == "pending" or (args.retry_failed and v["status"] == "failed")]

    if args.slug:
        pending = [args.slug]
    if args.limit:
        pending = pending[:args.limit]

    print(f"Processing {len(pending)} projects", flush=True)
    t0 = time.time()

    for i, slug in enumerate(pending, start=1):
        proj = get_project_data(slug, agg)
        if not proj:
            print(f"[{i}] {slug}: no data, skip", flush=True)
            q["items"][slug] = {"status": "skipped"}
            continue
        # Busca merged_indicadores
        merged = {k: v for k, v in proj.items()
                  if k not in ("slug", "padrao", "ac_m2", "ur", "total_r$", "rsm2")
                  and v is not None}
        proj["merged_indicadores"] = merged

        prompt = build_prompt(slug, proj, agg)
        t_start = time.time()
        try:
            resp = call_gemma(prompt, timeout=90)
            el = time.time() - t_start
            # Salva no JSON do projeto
            proj_file = IND_DIR / f"{slug}.json"
            if proj_file.exists():
                pdata = json.loads(proj_file.read_text(encoding="utf-8"))
                pdata["insight_gemma"] = resp
                pdata["insight_ts"] = datetime.now().isoformat(timespec="seconds")
                proj_file.write_text(json.dumps(pdata, indent=2, ensure_ascii=False), encoding="utf-8")
            q["items"][slug] = {"status": "done", "duration_s": round(el, 1)}
            log_event({"slug": slug, "status": "done", "duration_s": round(el, 1)})
            elapsed_total = time.time() - t0
            eta = elapsed_total * (len(pending) - i) / i if i > 0 else 0
            print(f"[{i}/{len(pending)}] {slug}: {el:.1f}s | total {elapsed_total/60:.1f}min eta {eta/60:.1f}min", flush=True)
            print(f"  > {resp[:120]}", flush=True)
        except Exception as e:
            err = str(e)[:150]
            q["items"][slug] = {"status": "failed", "error": err}
            log_event({"slug": slug, "status": "failed", "error": err})
            print(f"[{i}/{len(pending)}] {slug}: FAIL {err}", flush=True)
        save_queue(q)

    done = sum(1 for v in q["items"].values() if v["status"] == "done")
    failed = sum(1 for v in q["items"].values() if v["status"] == "failed")
    print(f"\nTotal done: {done}, failed: {failed}", flush=True)


if __name__ == "__main__":
    main()
