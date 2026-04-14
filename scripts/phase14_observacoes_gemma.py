#!/usr/bin/env python3
"""Phase 14 — Gemma loop sobre observações e comentários completos.

Para cada projeto com comentários/textos extraídos na Fase 8, monta compact
view de observações (~4k chars) e pede pro Gemma identificar:
- Temas recorrentes
- Justificativas técnicas
- Flags de risco ou decisões críticas
- Padrões cross-comentário

Saída: base/observacoes-insights/[projeto].json
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
COM_DIR = BASE / "comentarios-completos"
OUT_JSON = BASE / "observacoes-insights"
OUT_MD = BASE / "observacoes-insights-md"
OUT_JSON.mkdir(parents=True, exist_ok=True)
OUT_MD.mkdir(parents=True, exist_ok=True)
QUEUE = BASE / "phase14-queue.json"
LOG = BASE / "phase14-pipeline.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma4:e4b"
NUM_CTX = 16384
TIMEOUT_S = 600


PROMPT = """Analise os comentários e observações abaixo (extraídos de planilhas de orçamento) e retorne APENAS um JSON válido (sem markdown, sem texto extra) no formato exato:

{
  "temas_recorrentes": ["string"],
  "justificativas_tecnicas": [
    {"tema": "string", "texto": "string"}
  ],
  "flags_risco": [
    {"tipo": "string", "descricao": "string"}
  ],
  "padroes_orcamentista": ["string"],
  "decisoes_criticas": [
    {"contexto": "string", "decisao": "string"}
  ]
}

REGRAS:
- Use APENAS textos que aparecem literalmente nos comentários. NÃO INVENTE.
- temas_recorrentes: até 8 temas que aparecem em múltiplos comentários
- justificativas_tecnicas: até 10 explicações técnicas (por que algo foi feito assim)
- flags_risco: alertas (valores estimados, projeto faltando, medição incerta, etc.)
- padroes_orcamentista: expressões típicas do orçamentista (ex: "Estimado com base no projeto")
- decisoes_criticas: decisões que afetam o orçamento
- Se não houver dados suficientes para uma lista, retorne []"""


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


def compact_com(slug: str) -> str | None:
    p = COM_DIR / f"{slug}.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text(encoding="utf-8"))
    total_com = d.get("total_comentarios", 0)
    total_txt = d.get("total_textos_livres", 0)
    if total_com == 0 and total_txt < 5:
        return None

    lines = [f"# {slug} — observações e comentários"]
    lines.append(f"comentarios={total_com} | textos_livres={total_txt}")
    lines.append("")

    char_limit = 4000
    used = 0

    for aba in d.get("abas", []):
        nome = aba.get("nome", "?")
        coms = aba.get("comentarios", [])
        txts = aba.get("textos_livres", [])
        if not coms and not txts:
            continue

        head = f"\n## {nome}\n"
        if used + len(head) > char_limit:
            break
        lines.append(head.strip())
        used += len(head)

        for com in coms[:15]:
            t = com.get("text", "").strip()[:200]
            line = f"- [com@{com.get('cell', '?')}] {t}"
            if used + len(line) > char_limit:
                break
            lines.append(line)
            used += len(line)

        for txt in txts[:20]:
            t = txt.get("text", "").strip()[:200]
            line = f"- [txt@{txt.get('cell', '?')}] {t}"
            if used + len(line) > char_limit:
                break
            lines.append(line)
            used += len(line)

        if used > char_limit:
            break

    return "\n".join(lines)[:4500]


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def log_event(e):
    e.setdefault("ts", now_iso())
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue():
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    slugs = [p.stem for p in sorted(COM_DIR.glob("*.json"))]
    items = [{"projeto": s, "status": "pending", "attempts": 0} for s in slugs]
    QUEUE.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    return items


def save_queue(q):
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def process(slug, model=DEFAULT_MODEL):
    started = time.time()
    summary = {"projeto": slug, "model": model, "status": "pending"}

    compact = compact_com(slug)
    if not compact:
        summary["status"] = "no_data"
        summary["duration_s"] = round(time.time() - started, 2)
        log_event(summary)
        return summary

    summary["compact_chars"] = len(compact)

    try:
        prompt = PROMPT + "\n\n---\n\n" + compact
        raw, dur = call_ollama(prompt, model)
        summary["llm_duration_s"] = round(dur, 1)
        summary["raw_chars"] = len(raw)

        parsed = extract_json(raw)
        if not parsed:
            summary["status"] = "parse_failed"
            summary["raw_sample"] = raw[:300]
        else:
            summary["status"] = "done"
            out = {
                "projeto": slug,
                "model": model,
                "ts": now_iso(),
                "duration_s": round(dur, 1),
                "compact_chars": len(compact),
                "raw": raw,
                "parsed": parsed,
            }
            (OUT_JSON / f"{slug}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

            summary["temas_n"] = len(parsed.get("temas_recorrentes") or [])
            summary["just_n"] = len(parsed.get("justificativas_tecnicas") or [])
            summary["risk_n"] = len(parsed.get("flags_risco") or [])
            summary["pad_n"] = len(parsed.get("padroes_orcamentista") or [])
    except requests.exceptions.Timeout:
        summary["status"] = "timeout"
    except Exception as e:
        summary["status"] = "failed"
        summary["error"] = f"{type(e).__name__}: {str(e)[:200]}"

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
        s = process(p["projeto"])
        counts[s["status"]] = counts.get(s["status"], 0) + 1
        p["status"] = s["status"]
        p["last_summary"] = {k: v for k, v in s.items() if k != "error"}
        save_queue(queue)
        elapsed = time.time() - t0
        eta = int((elapsed / i) * (len(targets) - i)) if i else 0
        line = (
            f"[{i}/{len(targets)}] {p['projeto']:<42} {s['status']:<12} "
            f"temas={s.get('temas_n', 0):>2} risk={s.get('risk_n', 0):>2} "
            f"{s.get('llm_duration_s', 0):>5.1f}s ETA={eta}s"
        )
        print(line, flush=True)

    print()
    print(f"summary: {counts}")
    print(f"total: {int(time.time() - t0)}s")


if __name__ == "__main__":
    main()
