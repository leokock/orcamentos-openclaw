#!/usr/bin/env python3
"""Merge phase 2 + phase 3 outputs into base/indices-executivo/*.json.

Adds a 'qualitative' key to each existing project JSON without touching
the original numerical structure. Safe to re-run — overwrites only the
qualitative key.

Usage:
  python merge_qualitative.py            # merge all
  python merge_qualitative.py --dry-run  # report only
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
INDICES = BASE / "indices-executivo"
SUB = BASE / "sub-disciplinas"
PREMISSAS = BASE / "premissas"
ITENS = BASE / "itens-detalhados"


def load_json(p: Path) -> dict | None:
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def merge_one(slug: str) -> dict:
    summary = {"projeto": slug, "phase1": False, "phase2": False, "phase3": False}
    base_path = INDICES / f"{slug}.json"
    if not base_path.exists():
        summary["status"] = "no_base"
        return summary

    base = json.loads(base_path.read_text(encoding="utf-8"))

    qualitative = base.get("qualitative", {})
    qualitative["updated_at"] = datetime.now().isoformat(timespec="seconds")

    p1 = load_json(ITENS / f"{slug}.json")
    if p1:
        qualitative["phase1_extraction"] = {
            "n_abas": len(p1.get("abas", [])),
            "total_itens": p1.get("total_itens", 0),
            "total_observacoes": p1.get("total_observacoes", 0),
            "fonte": "scripts/extract_itens_detalhados.py",
            "json_path": str((ITENS / f"{slug}.json").as_posix()),
        }
        summary["phase1"] = True

    p2 = load_json(SUB / f"{slug}.json")
    if p2 and p2.get("parsed"):
        parsed = p2["parsed"]
        qualitative["sub_disciplinas"] = parsed.get("sub_disciplinas") or []
        qualitative["observacoes_orcamentista"] = parsed.get("observacoes_relevantes") or []
        qualitative["padroes_identificados"] = parsed.get("padroes_identificados") or []
        qualitative["fora_da_curva"] = parsed.get("fora_da_curva") or []
        qualitative["phase2_meta"] = {
            "model": p2.get("model"),
            "ts": p2.get("ts"),
            "duration_s": p2.get("duration_s"),
            "compact_chars": p2.get("compact_chars"),
        }
        summary["phase2"] = True

    p3 = load_json(PREMISSAS / f"{slug}.json")
    if p3 and p3.get("parsed"):
        parsed = p3["parsed"]
        qualitative["pdf_metadata"] = parsed.get("metadata") or {}
        qualitative["premissas_tecnicas"] = parsed.get("premissas_tecnicas") or []
        qualitative["bdi_encargos"] = parsed.get("bdi_encargos") or []
        qualitative["decisoes_consolidadas"] = parsed.get("decisoes_consolidadas") or []
        qualitative["observacoes_chave_pdf"] = parsed.get("observacoes_chave") or []
        qualitative["phase3_meta"] = {
            "model": p3.get("model"),
            "ts": p3.get("ts"),
            "duration_s": p3.get("duration_s"),
            "excerpt_chars": p3.get("excerpt_chars"),
        }
        summary["phase3"] = True

    base["qualitative"] = qualitative
    summary["status"] = "merged"
    summary["base_path"] = str(base_path)
    return base, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slug")
    args = ap.parse_args()

    if args.slug:
        slugs = [args.slug]
    else:
        slugs = sorted(p.stem for p in INDICES.glob("*.json"))

    counts = {"merged": 0, "no_base": 0, "phase1": 0, "phase2": 0, "phase3": 0, "skipped": 0}
    for slug in slugs:
        result = merge_one(slug)
        if isinstance(result, tuple):
            base, summary = result
        else:
            summary = result
            counts[summary["status"]] = counts.get(summary["status"], 0) + 1
            continue
        counts["merged"] += 1
        for k in ("phase1", "phase2", "phase3"):
            if summary[k]:
                counts[k] += 1
        if not args.dry_run:
            (INDICES / f"{slug}.json").write_text(
                json.dumps(base, indent=2, ensure_ascii=False), encoding="utf-8"
            )

    print(f"merged: {counts['merged']}")
    print(f"  with phase1: {counts['phase1']}")
    print(f"  with phase2: {counts['phase2']}")
    print(f"  with phase3: {counts['phase3']}")
    if counts["no_base"]:
        print(f"  no base JSON: {counts['no_base']}")
    if args.dry_run:
        print("(dry-run, nothing written)")


if __name__ == "__main__":
    main()
