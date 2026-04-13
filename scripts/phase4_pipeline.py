#!/usr/bin/env python3
"""Phase 4c — Gemma analysis sobre composicoes-raw.

Para cada um dos ~22 projetos com composições extraídas, monta um compact
view dos top 30 itens por valor e pergunta ao Gemma:

1. Distribuição estimada % material / MO / equipamento por categoria
2. Top 5 insumos críticos (que se variarem afetam o orçamento)
3. Padrões cross-aba (ex: "escoramento metálico aparece em laje protendida")

Saída: base/composicoes/[projeto].json
       base/composicoes-md/[projeto]-composicoes.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
RAW = BASE / "composicoes-raw"
OUT_JSON = BASE / "composicoes"
OUT_MD = BASE / "composicoes-md"
OUT_JSON.mkdir(parents=True, exist_ok=True)
OUT_MD.mkdir(parents=True, exist_ok=True)
QUEUE = BASE / "phase4-queue.json"
LOG = BASE / "phase4-pipeline.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma4:e4b"
NUM_CTX = 16384
TIMEOUT_S = 600

PROMPT = """Analise a tabela de composições/insumos abaixo (extraída de um orçamento de obra) e retorne APENAS um JSON válido (sem markdown, sem texto antes/depois) no formato exato:

{
  "distribuicao": {
    "material_pct": 0,
    "mao_obra_pct": 0,
    "equipamento_pct": 0,
    "outros_pct": 0
  },
  "insumos_criticos": [
    {"insumo": "string", "categoria": "material|mao_obra|equipamento", "motivo": "string"}
  ],
  "padroes_observados": ["string"],
  "macrogrupos_destaque": ["string"]
}

REGRAS:
- Use APENAS textos que aparecem literalmente na tabela. Não invente.
- distribuicao: estime os percentuais baseado nos itens listados (somar 100)
- insumos_criticos: top 5 itens cuja variação de preço afetaria mais o total
- padroes_observados: até 5 padrões repetidos (ex: "Concreto FCK 30 MPa aparece em vários itens")
- macrogrupos_destaque: até 3 macrogrupos onde a composição é mais relevante
- O JSON deve ser sintaticamente válido"""


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def log_event(e):
    e.setdefault("ts", now_iso())
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue():
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    items = [{"projeto": p.stem, "status": "pending", "attempts": 0}
             for p in sorted(RAW.glob("*.json"))]
    QUEUE.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    return items


def save_queue(q):
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def call_ollama(prompt, model=DEFAULT_MODEL):
    payload = {
        "model": model, "prompt": prompt, "stream": False,
        "options": {"num_ctx": NUM_CTX, "temperature": 0.3, "repeat_penalty": 1.2},
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
    r.raise_for_status()
    return r.json().get("response", ""), time.time() - t0


JSON_RE = re.compile(r"\{[\s\S]*\}")


def _fix_bad_escapes(s):
    return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', s)


def _balance_braces(s):
    o, c = s.count("{"), s.count("}")
    if c > o:
        for _ in range(c - o):
            i = s.rfind("}")
            if i < 0:
                break
            s = s[:i] + s[i + 1:]
    elif o > c:
        s = s + "}" * (o - c)
    return s


def extract_json(raw):
    s = raw.strip()
    s = re.sub(r"^```(?:json)?", "", s).strip()
    s = re.sub(r"```$", "", s).strip()
    m = JSON_RE.search(s)
    if not m:
        return None
    cand = m.group(0)
    for c in [cand, _fix_bad_escapes(cand), _balance_braces(_fix_bad_escapes(cand))]:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def compact_composicoes(raw_data):
    """Monta compact view (~3-4k chars) das top composições por valor."""
    lines = [f"# Composições/Insumos — {raw_data['projeto']}", ""]
    for aba in raw_data.get("abas", []):
        nome = aba.get("nome", "?")
        cats = aba.get("cat_counts", {})
        items = aba.get("items", [])
        lines.append(f"## {nome}  (n={len(items)} | mat={cats.get('material',0)} mo={cats.get('mao_obra',0)} eq={cats.get('equipamento',0)})")

        items_with_val = [it for it in items if it.get("total") and it["total"] > 0]
        items_with_val.sort(key=lambda x: -(x.get("total") or 0))
        items_use = items_with_val[:30] if items_with_val else items[:30]

        for it in items_use[:25]:
            desc = (it.get("descricao") or "")[:70]
            un = it.get("unidade") or ""
            cons = it.get("consumo") or ""
            pu = it.get("pu") or 0
            tot = it.get("total") or 0
            cat = it.get("categoria", "?")[:3]
            lines.append(f"- [{cat}] {desc} | {un} | cons={cons} | PU={pu} | T={tot:.0f}" if tot else f"- [{cat}] {desc} | {un} | cons={cons} | PU={pu}")
        lines.append("")

    text = "\n".join(lines)
    if len(text) > 4500:
        text = text[:4500] + "\n…[trunc]"
    return text


def render_md(slug, parsed, model, dur):
    lines = [f"# {slug} — composições (Gemma)", ""]
    lines.append(f"_Gerado em {now_iso()} por {model} ({dur:.1f}s)_")
    lines.append("")

    dist = parsed.get("distribuicao") or {}
    if dist:
        lines.append("## Distribuição estimada")
        lines.append(f"- Material: **{dist.get('material_pct', 0)}%**")
        lines.append(f"- Mão-de-obra: **{dist.get('mao_obra_pct', 0)}%**")
        lines.append(f"- Equipamento: **{dist.get('equipamento_pct', 0)}%**")
        lines.append(f"- Outros: **{dist.get('outros_pct', 0)}%**")
        lines.append("")

    crit = parsed.get("insumos_criticos") or []
    if crit:
        lines.append("## Insumos críticos")
        for c in crit:
            lines.append(f"- _{c.get('categoria', '?')}_ **{c.get('insumo', '?')}** — {c.get('motivo', '')}")
        lines.append("")

    pad = parsed.get("padroes_observados") or []
    if pad:
        lines.append("## Padrões observados")
        for p in pad:
            lines.append(f"- {p}")
        lines.append("")

    mg = parsed.get("macrogrupos_destaque") or []
    if mg:
        lines.append("## Macrogrupos em destaque")
        for m in mg:
            lines.append(f"- {m}")
    return "\n".join(lines)


def process_project(slug, model=DEFAULT_MODEL):
    started = time.time()
    summary = {"projeto": slug, "model": model, "status": "pending"}

    raw_path = RAW / f"{slug}.json"
    if not raw_path.exists():
        summary["status"] = "no_raw"
        summary["duration_s"] = round(time.time() - started, 2)
        log_event(summary)
        return summary

    try:
        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        compact = compact_composicoes(raw)
        summary["compact_chars"] = len(compact)

        full_prompt = PROMPT + "\n\n---\n\n" + compact
        gemma_raw, dur = call_ollama(full_prompt, model)
        summary["llm_duration_s"] = round(dur, 1)
        summary["raw_chars"] = len(gemma_raw)

        parsed = extract_json(gemma_raw)
        if not parsed:
            summary["status"] = "parse_failed"
            summary["raw_sample"] = gemma_raw[:300]
        else:
            summary["status"] = "done"
            (OUT_JSON / f"{slug}.json").write_text(
                json.dumps({"projeto": slug, "model": model, "ts": now_iso(),
                            "duration_s": round(dur, 1), "raw": gemma_raw, "parsed": parsed},
                           indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            (OUT_MD / f"{slug}-composicoes.md").write_text(
                render_md(slug, parsed, model, dur), encoding="utf-8"
            )
            summary["dist"] = parsed.get("distribuicao", {})
            summary["n_criticos"] = len(parsed.get("insumos_criticos") or [])
    except requests.exceptions.Timeout:
        summary["status"] = "timeout"
    except Exception as e:
        summary["status"] = "failed"
        summary["error"] = f"{type(e).__name__}: {e}"

    summary["duration_s"] = round(time.time() - started, 2)
    log_event(summary)
    return summary


def main():
    queue = init_queue()
    targets = [p for p in queue if p.get("status") == "pending"]
    print(f"processing {len(targets)} projects with {DEFAULT_MODEL}", flush=True)

    counts = {}
    t0 = time.time()
    for i, p in enumerate(targets, 1):
        s = process_project(p["projeto"])
        counts[s["status"]] = counts.get(s["status"], 0) + 1
        p["status"] = s["status"]
        p["attempts"] = p.get("attempts", 0) + 1
        p["last_summary"] = s
        save_queue(queue)
        elapsed = time.time() - t0
        eta = int((elapsed / i) * (len(targets) - i)) if i else 0
        d = s.get("dist") or {}
        line = (
            f"[{i}/{len(targets)}] {p['projeto']:<42} {s['status']:<13} "
            f"mat={d.get('material_pct', '?')} mo={d.get('mao_obra_pct', '?')} "
            f"crit={s.get('n_criticos', 0)}  {s.get('llm_duration_s', 0):.1f}s ETA={eta}s"
        )
        print(line, flush=True)

    print()
    print(f"summary: {counts}")
    print(f"total: {int(time.time() - t0)}s")


if __name__ == "__main__":
    main()
