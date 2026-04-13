#!/usr/bin/env python3
"""Copia pacotes finalizados para as pastas de entrega no Google Drive.

NÃO RODA AUTOMATICAMENTE — Leo precisa aprovar cada projeto.

Para cada slug aprovado, copia:
- parametrico-{slug}.xlsx → ~/orcamentos/parametricos/{slug}/{slug}-parametrico.xlsx
- parametrico-{slug}.docx → ~/orcamentos/parametricos/{slug}/{slug}-Memorial-Parametrico.docx
- parametrico-{slug}.pdf  → ~/orcamentos/parametricos/{slug}/{slug}-Memorial-Parametrico.pdf
- executivo-{slug}.xlsx   → ~/orcamentos/executivos/{slug}/{slug}-executivo.xlsx
- executivo-{slug}.docx   → ~/orcamentos/executivos/{slug}/{slug}-Memorial-Executivo.docx
- executivo-{slug}.pdf    → ~/orcamentos/executivos/{slug}/{slug}-Memorial-Executivo.pdf
- audit-{slug}.md          → ~/orcamentos/parametricos/{slug}/audit.md
- validacao-{slug}.md      → ~/orcamentos/parametricos/{slug}/validacao.md

Uso:
    python copiar_pacotes_drive.py --slug projeto-aprovado --dry-run
    python copiar_pacotes_drive.py --slug projeto-aprovado --confirm
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

PACOTES = Path.home() / "orcamentos-openclaw" / "base" / "pacotes"
DRIVE_PARAM = Path.home() / "orcamentos" / "parametricos"
DRIVE_EXEC = Path.home() / "orcamentos" / "executivos"


def plan_copies(slug: str) -> list[tuple[Path, Path, str]]:
    src_pasta = PACOTES / slug
    dst_param = DRIVE_PARAM / slug
    dst_exec = DRIVE_EXEC / slug

    copies = [
        (src_pasta / f"parametrico-{slug}.xlsx", dst_param / f"{slug}-parametrico.xlsx", "param xlsx"),
        (src_pasta / f"parametrico-{slug}.docx", dst_param / f"{slug}-Memorial-Parametrico.docx", "param docx"),
        (src_pasta / f"parametrico-{slug}.pdf", dst_param / f"{slug}-Memorial-Parametrico.pdf", "param pdf"),
        (src_pasta / f"executivo-{slug}.xlsx", dst_exec / f"{slug}-executivo.xlsx", "exec xlsx"),
        (src_pasta / f"executivo-{slug}.docx", dst_exec / f"{slug}-Memorial-Executivo.docx", "exec docx"),
        (src_pasta / f"executivo-{slug}.pdf", dst_exec / f"{slug}-Memorial-Executivo.pdf", "exec pdf"),
        (src_pasta / f"audit-{slug}.md", dst_param / "audit.md", "audit md"),
        (src_pasta / f"validacao-{slug}.md", dst_param / "validacao.md", "validacao md"),
        (src_pasta / "analise-arquitetura.json", dst_param / "analise-arquitetura.json", "arq json"),
    ]
    return copies


def execute(slug: str, dry_run: bool = True) -> dict:
    copies = plan_copies(slug)
    summary = {
        "slug": slug,
        "dry_run": dry_run,
        "operations": [],
        "errors": [],
    }

    for src, dst, label in copies:
        op = {"label": label, "src": str(src), "dst": str(dst)}
        if not src.exists():
            op["status"] = "src_missing"
            summary["operations"].append(op)
            continue
        if dry_run:
            op["status"] = "would_copy"
            op["src_size"] = src.stat().st_size
        else:
            try:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                op["status"] = "copied"
                op["bytes"] = dst.stat().st_size if dst.exists() else 0
            except Exception as e:
                op["status"] = "error"
                op["error"] = f"{type(e).__name__}: {e}"
                summary["errors"].append(op["error"])
        summary["operations"].append(op)

    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--dry-run", action="store_true", help="show what would be copied (default)")
    ap.add_argument("--confirm", action="store_true", help="actually copy")
    args = ap.parse_args()

    if not args.confirm and not args.dry_run:
        args.dry_run = True

    summary = execute(args.slug, dry_run=not args.confirm)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
