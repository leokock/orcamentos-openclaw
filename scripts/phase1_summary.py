#!/usr/bin/env python3
"""Phase 1 — summary report.

Reads base/phase1-extract.log.jsonl and base/itens-detalhados/*.json,
prints aggregated stats and a list of projects that failed or extracted
suspiciously little (zero items, etc.) for re-run targeting.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
LOG = BASE / "phase1-extract.log.jsonl"
OUT_DIR = BASE / "itens-detalhados"


def read_log() -> list[dict]:
    if not LOG.exists():
        return []
    out = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def main() -> None:
    log = read_log()
    if not log:
        print("no log found")
        return

    by_status = Counter(e.get("status", "?") for e in log)
    print("=== status counts ===")
    for k, v in sorted(by_status.items(), key=lambda x: -x[1]):
        print(f"  {k:<10} {v}")

    done = [e for e in log if e.get("status") == "done"]
    print(f"\n=== done={len(done)} ===")
    if done:
        n_itens = [e.get("total_itens", 0) for e in done]
        n_obs = [e.get("total_observacoes", 0) for e in done]
        n_abas = [e.get("abas", 0) for e in done]
        print(f"  itens     total={sum(n_itens):>9}  avg={sum(n_itens)//len(done):>5}  min={min(n_itens):>5}  max={max(n_itens):>5}")
        print(f"  obs       total={sum(n_obs):>9}  avg={sum(n_obs)//len(done):>5}  min={min(n_obs):>5}  max={max(n_obs):>5}")
        print(f"  abas      total={sum(n_abas):>9}  avg={sum(n_abas)//len(done):>5}  min={min(n_abas):>5}  max={max(n_abas):>5}")

        durations = [e.get("duration_s", 0) for e in done]
        print(f"  duration  total={sum(durations):>9.1f}s  avg={sum(durations)/len(done):>5.1f}s  max={max(durations):>5.1f}s")

    suspicious = [e for e in done if e.get("total_itens", 0) < 50]
    if suspicious:
        print(f"\n=== suspicious (<50 items) — {len(suspicious)} ===")
        for s in suspicious:
            print(f"  {s['projeto']:<45} itens={s.get('total_itens',0):<5} abas={s.get('abas',0)}")

    failed = [e for e in log if e.get("status") in ("failed", "no_xlsx")]
    if failed:
        print(f"\n=== failed/no_xlsx — {len(failed)} ===")
        for f in failed:
            print(f"  {f['projeto']:<45} {f['status']:<10} {f.get('error','')[:80]}")

    if done:
        top10 = sorted(done, key=lambda e: e.get("total_itens", 0), reverse=True)[:10]
        print("\n=== top 10 by item count ===")
        for t in top10:
            print(f"  {t['projeto']:<45} itens={t.get('total_itens',0):<6} abas={t.get('abas',0)}")


if __name__ == "__main__":
    main()
