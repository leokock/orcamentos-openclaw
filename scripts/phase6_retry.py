#!/usr/bin/env python3
"""Phase 6 — Retry da Fase 2 com prompt enriquecido (compact view rica).

Identifica projetos com <5 sub_disciplinas (sinal de que o compact view
mini de 3-4k chars não foi suficiente) e re-roda Gemma com a versão RICH
do compact view (~7-8k chars com mais itens, mais abas, mais observações).

Sobrescreve apenas se a nova versão tiver MAIS sub-disciplinas que a antiga.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
import compact_view  # noqa: E402
import phase2_pipeline  # noqa: E402

BASE = Path.home() / "orcamentos-openclaw" / "base"
SUB = BASE / "sub-disciplinas"
SUB_MD = BASE / "sub-disciplinas-md"
LOG = BASE / "phase6-retry.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma4:e4b"
NUM_CTX = 16384
TIMEOUT_S = 600


def call_ollama(prompt, model=DEFAULT_MODEL):
    payload = {
        "model": model, "prompt": prompt, "stream": False,
        "options": {"num_ctx": NUM_CTX, "temperature": 0.3, "repeat_penalty": 1.2},
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
    r.raise_for_status()
    return r.json().get("response", ""), time.time() - t0


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def log_event(e):
    e.setdefault("ts", now_iso())
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def identify_low_coverage(min_subs=5):
    out = []
    for p in sorted(SUB.glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            n = len((d.get("parsed") or {}).get("sub_disciplinas") or [])
            if n < min_subs:
                out.append((p.stem, n))
        except Exception:
            pass
    return out


def process_one(slug, model=DEFAULT_MODEL):
    started = time.time()
    summary = {"projeto": slug, "model": model, "status": "pending"}

    detalhe_path = BASE / "itens-detalhados" / f"{slug}.json"
    if not detalhe_path.exists():
        summary["status"] = "no_detalhe"
        log_event(summary)
        return summary

    sub_path = SUB / f"{slug}.json"
    old_n_subs = 0
    if sub_path.exists():
        try:
            old = json.loads(sub_path.read_text(encoding="utf-8"))
            old_n_subs = len((old.get("parsed") or {}).get("sub_disciplinas") or [])
        except Exception:
            pass

    try:
        compact = compact_view.render_project_rich(slug)
        summary["compact_chars"] = len(compact)
        summary["old_n_subs"] = old_n_subs

        prompt = phase2_pipeline.PROMPT + "\n\n---\n\n" + compact
        raw, dur = call_ollama(prompt, model)
        summary["llm_duration_s"] = round(dur, 1)

        parsed = phase2_pipeline.extract_json(raw)
        if not parsed:
            summary["status"] = "parse_failed"
            summary["raw_sample"] = raw[:300]
            log_event(summary)
            return summary

        new_n_subs = len(parsed.get("sub_disciplinas") or [])
        summary["new_n_subs"] = new_n_subs
        summary["delta"] = new_n_subs - old_n_subs

        if new_n_subs > old_n_subs:
            out_json = {
                "projeto": slug,
                "model": model,
                "ts": now_iso(),
                "compact_chars": len(compact),
                "duration_s": round(dur, 1),
                "raw_response": raw,
                "parsed": parsed,
                "phase6_retry": True,
                "previous_n_subs": old_n_subs,
            }
            sub_path.write_text(json.dumps(out_json, indent=2, ensure_ascii=False), encoding="utf-8")
            md = phase2_pipeline.render_md(slug, parsed, raw, model, dur)
            (SUB_MD / f"{slug}-qualitativo.md").write_text(md, encoding="utf-8")
            summary["status"] = "improved"
        else:
            summary["status"] = "no_improvement"
    except requests.exceptions.Timeout:
        summary["status"] = "timeout"
    except Exception as e:
        summary["status"] = "failed"
        summary["error"] = f"{type(e).__name__}: {e}"

    summary["duration_s"] = round(time.time() - started, 2)
    log_event(summary)
    return summary


def main():
    targets = identify_low_coverage(min_subs=5)
    print(f"\n{len(targets)} projetos com <5 sub_disciplinas — retry com compact view RICA")
    print()

    counts = {}
    t0 = time.time()
    for i, (slug, old_n) in enumerate(targets, 1):
        s = process_one(slug)
        counts[s["status"]] = counts.get(s["status"], 0) + 1
        elapsed = time.time() - t0
        eta = int((elapsed / i) * (len(targets) - i)) if i else 0
        line = (
            f"[{i}/{len(targets)}] {slug:<42} {s['status']:<15} "
            f"{old_n} -> {s.get('new_n_subs', '?')}  "
            f"{s.get('llm_duration_s', 0):.1f}s ETA={eta}s"
        )
        print(line, flush=True)

    print()
    print(f"summary: {counts}")
    print(f"total: {int(time.time() - t0)}s")


if __name__ == "__main__":
    main()
