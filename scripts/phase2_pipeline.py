#!/usr/bin/env python3
"""Phase 2 — Gemma qualitative enrichment loop.

For each project in base/itens-detalhados/, generates a mini compact view
(~3-4k chars), sends it to Ollama (gemma4:e4b by default), parses the
JSON response and writes:
  - base/sub-disciplinas/[projeto].json
  - base/sub-disciplinas-md/[projeto]-qualitativo.md

Queue state lives in base/phase2-queue.json (auto-rebuilt if missing).
Resumable: every iteration persists state. Append-only log in
base/phase2-pipeline.log.jsonl.

Usage:
  python phase2_pipeline.py                  # process all pending
  python phase2_pipeline.py <slug>           # process one specific
  python phase2_pipeline.py --reset          # mark everything pending
  python phase2_pipeline.py --status         # print queue status
  python phase2_pipeline.py --limit N        # process first N pending
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

try:
    import requests
except ImportError:
    print("requests not installed. run: pip install requests", file=sys.stderr)
    sys.exit(1)

import compact_view  # type: ignore

BASE = Path.home() / "orcamentos-openclaw" / "base"
DETALHADOS = BASE / "itens-detalhados"
SUB_DIR = BASE / "sub-disciplinas"
MD_DIR = BASE / "sub-disciplinas-md"
QUEUE = BASE / "phase2-queue.json"
LOG = BASE / "phase2-pipeline.log.jsonl"
SUB_DIR.mkdir(parents=True, exist_ok=True)
MD_DIR.mkdir(parents=True, exist_ok=True)

OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/") + "/api/generate"
DEFAULT_MODEL = "gemma4:e4b"
NUM_CTX = 16384
TEMPERATURE = 0.3
REPEAT_PENALTY = 1.2
TIMEOUT_S = 600

PROMPT = """Analise este resumo de orçamento de obra e retorne APENAS um JSON válido (sem markdown, sem texto antes/depois) no formato exato:

{
  "sub_disciplinas": [
    {"macrogrupo": "string", "sub_disciplina": "string", "itens_exemplo": ["string"]}
  ],
  "observacoes_relevantes": [
    {"contexto": "string", "observacao": "string", "categoria": "revisao|premissa|justificativa|alerta|outro"}
  ],
  "padroes_identificados": ["string"],
  "fora_da_curva": [
    {"item": "string", "motivo": "string"}
  ]
}

REGRAS ESTRITAS:
- Use APENAS textos e valores que aparecem literalmente no documento. Não invente.
- Sub-disciplinas: agrupe os itens reais por temas mais granulares dentro de cada macrogrupo (ex: "Concreto", "Armadura", "Forma" dentro de "Estrutura"). Cite no máximo 3 itens por sub-disciplina.
- Observações: pegue as observações textuais que explicam decisões e categorize.
- Padrões: o que se repete entre abas (ex: "valores idênticos em 3 blocos diferentes").
- Fora-da-curva: itens marcados com alerta ou desproporcionais.
- Se um campo não tiver dados suficientes, retorne lista vazia [].
- O JSON deve ser sintaticamente válido."""


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def log_event(event: dict) -> None:
    event.setdefault("ts", now_iso())
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def init_queue() -> list[dict]:
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    items = [{"projeto": p.stem, "status": "pending", "attempts": 0}
             for p in sorted(DETALHADOS.glob("*.json"))]
    QUEUE.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    return items


def save_queue(q: list[dict]) -> None:
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def call_ollama(prompt_full: str, model: str) -> tuple[str, float]:
    payload = {
        "model": model,
        "prompt": prompt_full,
        "stream": False,
        "options": {
            "num_ctx": NUM_CTX,
            "temperature": TEMPERATURE,
            "repeat_penalty": REPEAT_PENALTY,
        },
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
    r.raise_for_status()
    data = r.json()
    return data.get("response", ""), time.time() - t0


JSON_RE = re.compile(r"\{[\s\S]*\}")


def _fix_bad_escapes(s: str) -> str:
    return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', s)


def extract_json(raw: str) -> dict | None:
    s = raw.strip()
    s = re.sub(r"^```(?:json)?", "", s).strip()
    s = re.sub(r"```$", "", s).strip()
    m = JSON_RE.search(s)
    if not m:
        return None
    candidate = m.group(0)
    attempts = [candidate]
    attempts.append(re.sub(r",(\s*[}\]])", r"\1", candidate))
    attempts.append(_fix_bad_escapes(candidate))
    attempts.append(_fix_bad_escapes(re.sub(r",(\s*[}\]])", r"\1", candidate)))
    for c in attempts:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def render_md(slug: str, parsed: dict, raw: str, model: str, duration: float) -> str:
    lines = [f"# {slug} — análise qualitativa Gemma", ""]
    lines.append(f"_Gerado em {now_iso()} por {model} ({duration:.1f}s)_")
    lines.append("")

    sub = parsed.get("sub_disciplinas") or []
    if sub:
        lines.append("## Sub-disciplinas identificadas")
        by_macro: dict[str, list] = {}
        for s in sub:
            by_macro.setdefault(s.get("macrogrupo", "?"), []).append(s)
        for macro, lst in by_macro.items():
            lines.append(f"### {macro}")
            for s in lst:
                lines.append(f"- **{s.get('sub_disciplina','?')}**")
                for it in s.get("itens_exemplo") or []:
                    lines.append(f"  - {it}")
            lines.append("")

    obs = parsed.get("observacoes_relevantes") or []
    if obs:
        lines.append("## Observações de orçamentista")
        for o in obs:
            cat = o.get("categoria", "outro")
            ctx = o.get("contexto", "")
            txt = o.get("observacao", "")
            lines.append(f"- _{cat}_ **{ctx}** — {txt}")
        lines.append("")

    pad = parsed.get("padroes_identificados") or []
    if pad:
        lines.append("## Padrões identificados")
        for p in pad:
            lines.append(f"- {p}")
        lines.append("")

    fora = parsed.get("fora_da_curva") or []
    if fora:
        lines.append("## Itens fora-da-curva")
        for f in fora:
            lines.append(f"- **{f.get('item','?')}** — {f.get('motivo','')}")
        lines.append("")

    return "\n".join(lines)


def process_project(slug: str, model: str) -> dict:
    started = time.time()
    summary = {"projeto": slug, "model": model, "status": "pending"}

    detalhe_path = DETALHADOS / f"{slug}.json"
    if not detalhe_path.exists():
        summary["status"] = "no_detalhe"
        summary["duration_s"] = round(time.time() - started, 2)
        log_event(summary)
        return summary

    try:
        compact = compact_view.render_project_mini(slug)
        summary["compact_chars"] = len(compact)

        prompt_full = PROMPT + "\n\n---\n\n" + compact
        raw, duration = call_ollama(prompt_full, model)
        summary["llm_duration_s"] = round(duration, 1)
        summary["raw_chars"] = len(raw)

        parsed = extract_json(raw)
        if not parsed:
            summary["status"] = "parse_failed"
            summary["raw_sample"] = raw[:300]
        else:
            summary["status"] = "done"
            summary["sub_disciplinas_n"] = len(parsed.get("sub_disciplinas") or [])
            summary["observacoes_n"] = len(parsed.get("observacoes_relevantes") or [])
            summary["padroes_n"] = len(parsed.get("padroes_identificados") or [])
            summary["fora_curva_n"] = len(parsed.get("fora_da_curva") or [])

            out_json = {
                "projeto": slug,
                "model": model,
                "ts": now_iso(),
                "compact_chars": len(compact),
                "duration_s": round(duration, 1),
                "raw_response": raw,
                "parsed": parsed,
            }
            (SUB_DIR / f"{slug}.json").write_text(
                json.dumps(out_json, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            md = render_md(slug, parsed, raw, model, duration)
            (MD_DIR / f"{slug}-qualitativo.md").write_text(md, encoding="utf-8")
    except requests.exceptions.Timeout:
        summary["status"] = "timeout"
    except Exception as e:
        summary["status"] = "failed"
        summary["error"] = f"{type(e).__name__}: {e}"
        summary["traceback"] = traceback.format_exc()[-400:]

    summary["duration_s"] = round(time.time() - started, 2)
    log_event(summary)
    return summary


def cmd_status() -> None:
    if not QUEUE.exists():
        print("queue not initialized")
        return
    q = json.loads(QUEUE.read_text(encoding="utf-8"))
    by = {}
    for p in q:
        by[p.get("status", "?")] = by.get(p.get("status", "?"), 0) + 1
    print(f"total: {len(q)}")
    for k, v in sorted(by.items(), key=lambda x: -x[1]):
        print(f"  {k:<15} {v}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    if args.status:
        cmd_status()
        return

    if args.reset:
        if QUEUE.exists():
            QUEUE.unlink()
        init_queue()
        print("queue reset")
        return

    queue = init_queue()

    if args.slug:
        slug = args.slug
        s = process_project(slug, args.model)
        for p in queue:
            if p["projeto"] == slug:
                p["status"] = s["status"]
                p["attempts"] = p.get("attempts", 0) + 1
                p["last_run"] = now_iso()
                p["last_summary"] = {k: v for k, v in s.items() if k not in ("traceback",)}
        save_queue(queue)
        print(json.dumps(s, indent=2, ensure_ascii=False))
        return

    targets = []
    for p in queue:
        st = p.get("status", "pending")
        if st == "pending":
            targets.append(p)
        elif args.retry_failed and st in ("failed", "parse_failed", "timeout"):
            targets.append(p)
    if args.limit:
        targets = targets[: args.limit]

    print(f"processing {len(targets)} projects with {args.model}", flush=True)
    counts: dict[str, int] = {}
    t0 = time.time()
    for i, p in enumerate(targets, 1):
        slug = p["projeto"]
        s = process_project(slug, args.model)
        counts[s["status"]] = counts.get(s["status"], 0) + 1
        p["status"] = s["status"]
        p["attempts"] = p.get("attempts", 0) + 1
        p["last_run"] = now_iso()
        p["last_summary"] = {k: v for k, v in s.items() if k not in ("traceback",)}
        save_queue(queue)

        elapsed = time.time() - t0
        avg = elapsed / i if i else 0
        eta = int(avg * (len(targets) - i))
        line = (
            f"[{i}/{len(targets)}] {slug:<42} {s['status']:<13} "
            f"{s.get('compact_chars',0):>5}c {s.get('llm_duration_s',0):>5.1f}s "
            f"sub={s.get('sub_disciplinas_n',0):>2} obs={s.get('observacoes_n',0):>2} "
            f"pad={s.get('padroes_n',0):>2} ETA={eta}s"
        )
        print(line, flush=True)

    print()
    print(f"summary: {counts}")
    print(f"total elapsed: {int(time.time()-t0)}s")


if __name__ == "__main__":
    main()
