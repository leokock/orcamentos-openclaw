#!/usr/bin/env python3
"""Phase 16c — Extração de quantitativos de PDFs.

Lê memoriais descritivos e quadros NBR 12.721 dos 3 projetos e extrai:
- Quadro de áreas (por pavimento)
- Quadro de unidades autônomas (tipo, quantidade, área)
- Especificações técnicas (acabamentos por ambiente)
- Tabelas de esquadrias (tipo, dimensões, quantidade)

Saída: base/quantitativos-pdf/[projeto].json
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = BASE / "quantitativos-pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)
TEMP = Path.home() / "orcamentos-openclaw" / "temp"
TEMP.mkdir(parents=True, exist_ok=True)


PROJETOS_BASE = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA")


def find_relevant_pdfs(slug: str) -> list[Path]:
    base = PROJETOS_BASE / slug
    if not base.exists():
        return []
    pdfs = []
    keywords = ["memorial", "quadro", "nbr", "especific", "tabela", "legenda", "area", "apresenta"]
    for p in base.rglob("*.pdf"):
        sp = str(p).lower()
        if "obsoleto" in sp or "antigo" in sp or "backup" in sp:
            continue
        if any(k in sp for k in keywords):
            size = p.stat().st_size
            pdfs.append((size, p))
    pdfs.sort(key=lambda x: -x[0])
    return [p for _, p in pdfs[:25]]


NUM_RE = re.compile(r"[\d]{1,4}[,\.][\d]{2,4}|\b\d{1,6}\b")
AREA_RE = re.compile(r"([\d.,]+)\s*m[²2]", re.IGNORECASE)


def extract_pdf(pdf_path: Path, dest_ascii: Path) -> dict:
    result = {
        "file": pdf_path.name,
        "pages": 0,
        "total_chars": 0,
        "areas_encontradas": [],
        "numeros_chave": [],
        "sections": {},
        "errors": [],
    }

    try:
        if any(ord(c) > 127 for c in pdf_path.name):
            import shutil
            shutil.copy2(pdf_path, dest_ascii)
            path_to_use = dest_ascii
        else:
            path_to_use = pdf_path

        r = PdfReader(str(path_to_use))
    except Exception as e:
        result["errors"].append(f"open: {type(e).__name__}")
        return result

    result["pages"] = len(r.pages)
    all_text = []
    for i, pg in enumerate(r.pages[:30]):
        try:
            t = pg.extract_text() or ""
        except Exception:
            t = ""
        all_text.append(t)

    full_text = "\n".join(all_text)
    result["total_chars"] = len(full_text)

    for m in AREA_RE.finditer(full_text):
        val_str = m.group(1).replace(".", "").replace(",", ".")
        try:
            v = float(val_str)
            if 5 <= v <= 100000:
                result["areas_encontradas"].append({"valor_m2": v, "context": full_text[max(0, m.start()-40): m.end()+10]})
        except Exception:
            pass

    if len(result["areas_encontradas"]) > 100:
        result["areas_encontradas"] = result["areas_encontradas"][:100]

    for pattern, key in [
        (r"([\d.]+)\s*[Uu]nidades?", "unidades"),
        (r"([\d.,]+)\s*[Mm]³|([\d.,]+)\s*[Mm]3", "m3"),
        (r"([\d.,]+)\s*kg", "kg"),
        (r"([\d.,]+)\s*[Pp]avimentos?", "pavimentos"),
    ]:
        matches = re.findall(pattern, full_text)
        if matches:
            result["sections"][key] = [str(m)[:20] for m in matches[:30]]

    return result


def process(slug: str):
    print(f"\n=== {slug} ===")
    t0 = time.time()
    pdfs = find_relevant_pdfs(slug)
    print(f"{len(pdfs)} relevant PDFs")

    if not pdfs:
        return

    project_result = {
        "projeto": slug,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "n_pdfs": len(pdfs),
        "files": [],
    }

    temp_slug = TEMP / slug
    temp_slug.mkdir(exist_ok=True)

    for i, p in enumerate(pdfs):
        print(f"  [{i+1}] {p.name[:70]}... ", end="", flush=True)
        t = time.time()
        dest = temp_slug / f"file_{i:03d}.pdf"
        try:
            r = extract_pdf(p, dest)
            r["duration_s"] = round(time.time() - t, 1)
        except Exception as e:
            r = {"file": p.name, "error": str(e)[:100]}
        project_result["files"].append(r)
        n_areas = len(r.get("areas_encontradas", []))
        chars = r.get("total_chars", 0)
        print(f"pg={r.get('pages', 0):>3} chars={chars:>5} areas={n_areas:>3}")

    project_result["duration_s"] = round(time.time() - t0, 1)
    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(project_result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  saved: {out}")


def main():
    for slug in ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]:
        process(slug)


if __name__ == "__main__":
    main()
