#!/usr/bin/env python3
"""Phase 3 — Gemma extraction of premissas/BDI/tipologia from PDFs.

Reads base/pdfs-text/[projeto].txt, takes a focused excerpt (~4k chars
mixing first pages with keyword-targeted snippets), sends to Ollama
gemma4:e4b and writes:
  - base/premissas/[projeto].json
  - base/premissas-md/[projeto]-premissas.md

State: base/phase3-queue.json. Log: base/phase3-pipeline.log.jsonl.
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
PDFS_TEXT = BASE / "pdfs-text"
OUT_JSON = BASE / "premissas"
OUT_MD = BASE / "premissas-md"
QUEUE = BASE / "phase3-queue.json"
LOG = BASE / "phase3-pipeline.log.jsonl"
OUT_JSON.mkdir(parents=True, exist_ok=True)
OUT_MD.mkdir(parents=True, exist_ok=True)

OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/") + "/api/generate"
DEFAULT_MODEL = "gemma4:e4b"
NUM_CTX = 16384
TEMPERATURE = 0.3
REPEAT_PENALTY = 1.2
TIMEOUT_S = 600

TARGET_INPUT_CHARS = 4500

KEYWORDS = [
    r"premissa", r"crit[ée]rio", r"\bbdi\b", r"encargo", r"imposto",
    r"tipologia", r"unidade", r"\bur\b", r"\bac\b", r"área constru",
    r"resumo", r"observa", r"considera", r"escopo",
    r"data.base", r"cub", r"\bivp\b", r"reajuste",
]

PROMPT = """Analise este resumo de PDF de orçamento de obra (apresentação ou memorial) e retorne APENAS um JSON válido (sem markdown, sem texto antes/depois) no formato exato:

{
  "metadata": {
    "ac_m2": null,
    "ur": null,
    "tipologia": "string ou null",
    "data_base": "string ou null",
    "cub_referencia": "string ou null"
  },
  "premissas_tecnicas": [
    {"area": "string", "premissa": "string"}
  ],
  "bdi_encargos": [
    {"componente": "string", "valor_pct": "string ou null", "nota": "string"}
  ],
  "decisoes_consolidadas": [
    {"contexto": "string", "decisao": "string"}
  ],
  "observacoes_chave": ["string"]
}

REGRAS ESTRITAS:
- Use APENAS textos e valores que aparecem literalmente no documento. Não invente.
- Premissas: critérios técnicos, considerações construtivas, escopo.
- BDI/Encargos: percentuais ou valores se aparecerem (ex: BDI 25%, INSS 11%).
- Tipologia: descrição do produto imobiliário (n. unidades, área média, mix).
- Decisões: escolhas explicadas no documento (revisão, ajuste, premissa adotada).
- Observações chave: textos relevantes que não se encaixam acima.
- Se um campo não tiver dados, use null para campos simples e [] para listas.
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
             for p in sorted(PDFS_TEXT.glob("*.txt"))]
    QUEUE.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    return items


def save_queue(q: list[dict]) -> None:
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def keyword_excerpt(text: str, target: int = TARGET_INPUT_CHARS) -> str:
    """Build a compact excerpt: first 1.5k chars + keyword snippets."""
    head = text[:1500]
    out = [head]
    used = len(head)

    pat = re.compile("|".join(KEYWORDS), re.IGNORECASE)
    seen_offsets = []
    for m in pat.finditer(text, pos=1500):
        if used >= target:
            break
        center = m.start()
        if any(abs(center - o) < 200 for o in seen_offsets):
            continue
        seen_offsets.append(center)
        snippet = text[max(0, center - 100): center + 250]
        snippet = "\n…" + snippet.strip() + "…\n"
        if used + len(snippet) > target:
            break
        out.append(snippet)
        used += len(snippet)

    return "".join(out)[:target]


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


def _balance_braces(s: str) -> str:
    opens = s.count("{")
    closes = s.count("}")
    if closes > opens:
        extra = closes - opens
        for _ in range(extra):
            idx = s.rfind("}")
            if idx < 0:
                break
            s = s[:idx] + s[idx + 1:]
    elif opens > closes:
        s = s + "}" * (opens - closes)
    return s


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
    attempts.append(_balance_braces(_fix_bad_escapes(re.sub(r",(\s*[}\]])", r"\1", candidate))))
    for c in attempts:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def render_md(slug: str, parsed: dict, model: str, duration: float) -> str:
    lines = [f"# {slug} — premissas (Gemma)", ""]
    lines.append(f"_Gerado em {now_iso()} por {model} ({duration:.1f}s)_")
    lines.append("")

    meta = parsed.get("metadata") or {}
    if meta:
        lines.append("## Metadata extraída do PDF")
        for k, v in meta.items():
            if v not in (None, ""):
                lines.append(f"- **{k}:** {v}")
        lines.append("")

    prem = parsed.get("premissas_tecnicas") or []
    if prem:
        lines.append("## Premissas técnicas")
        for p in prem:
            lines.append(f"- _{p.get('area','?')}_ — {p.get('premissa','')}")
        lines.append("")

    bdi = parsed.get("bdi_encargos") or []
    if bdi:
        lines.append("## BDI / Encargos")
        for b in bdi:
            v = b.get("valor_pct") or "—"
            lines.append(f"- **{b.get('componente','?')}** ({v}) — {b.get('nota','')}")
        lines.append("")

    dec = parsed.get("decisoes_consolidadas") or []
    if dec:
        lines.append("## Decisões consolidadas")
        for d in dec:
            lines.append(f"- _{d.get('contexto','?')}_ — {d.get('decisao','')}")
        lines.append("")

    obs = parsed.get("observacoes_chave") or []
    if obs:
        lines.append("## Observações chave")
        for o in obs:
            lines.append(f"- {o}")

    return "\n".join(lines)


def process_project(slug: str, model: str) -> dict:
    started = time.time()
    summary = {"projeto": slug, "model": model, "status": "pending"}

    txt_path = PDFS_TEXT / f"{slug}.txt"
    if not txt_path.exists():
        summary["status"] = "no_pdf_text"
        summary["duration_s"] = round(time.time() - started, 2)
        log_event(summary)
        return summary

    try:
        text = txt_path.read_text(encoding="utf-8")
        excerpt = keyword_excerpt(text)
        summary["pdf_chars"] = len(text)
        summary["excerpt_chars"] = len(excerpt)

        prompt_full = PROMPT + "\n\n---\n\n" + excerpt
        raw, duration = call_ollama(prompt_full, model)
        summary["llm_duration_s"] = round(duration, 1)
        summary["raw_chars"] = len(raw)

        parsed = extract_json(raw)
        if not parsed:
            summary["status"] = "parse_failed"
            summary["raw_sample"] = raw[:300]
        else:
            summary["status"] = "done"
            summary["premissas_n"] = len(parsed.get("premissas_tecnicas") or [])
            summary["bdi_n"] = len(parsed.get("bdi_encargos") or [])
            summary["decisoes_n"] = len(parsed.get("decisoes_consolidadas") or [])

            (OUT_JSON / f"{slug}.json").write_text(
                json.dumps({"projeto": slug, "model": model, "ts": now_iso(),
                            "excerpt_chars": len(excerpt), "duration_s": round(duration, 1),
                            "raw_response": raw, "parsed": parsed},
                           indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            (OUT_MD / f"{slug}-premissas.md").write_text(
                render_md(slug, parsed, model, duration), encoding="utf-8"
            )
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
                p["last_summary"] = {k: v for k, v in s.items() if k != "traceback"}
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
        p["last_summary"] = {k: v for k, v in s.items() if k != "traceback"}
        save_queue(queue)

        elapsed = time.time() - t0
        avg = elapsed / i if i else 0
        eta = int(avg * (len(targets) - i))
        line = (
            f"[{i}/{len(targets)}] {slug:<42} {s['status']:<13} "
            f"{s.get('excerpt_chars',0):>5}c {s.get('llm_duration_s',0):>5.1f}s "
            f"prem={s.get('premissas_n',0):>2} bdi={s.get('bdi_n',0):>2} "
            f"dec={s.get('decisoes_n',0):>2} ETA={eta}s"
        )
        print(line, flush=True)

    print()
    print(f"summary: {counts}")
    print(f"total elapsed: {int(time.time()-t0)}s")


if __name__ == "__main__":
    main()
