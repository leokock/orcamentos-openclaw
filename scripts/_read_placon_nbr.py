#!/usr/bin/env python3
"""Temp script — read Placon NBR quadros."""
from pathlib import Path
from pypdf import PdfReader

base = Path.home() / "orcamentos-openclaw" / "temp" / "placon-nbr"
print(f"base exists: {base.exists()}, items: {len(list(base.iterdir())) if base.exists() else 0}")

for f in sorted(base.glob("0*.pdf")):
    print(f"\n=== {f.name} ({f.stat().st_size // 1024} KB) ===")
    try:
        r = PdfReader(str(f))
        for i, pg in enumerate(r.pages):
            t = pg.extract_text() or ""
            t = t.replace("\n\n", "\n").strip()
            print(f"  [p{i+1}]")
            print(t)
    except Exception as e:
        print(f"  err: {e}")
