#!/usr/bin/env python3
"""Extract text from PDFs (presentations, memorials) for Gemma analysis.

Reads source PDFs from base/gemma-queue.json, extracts text via pypdf
and writes one .txt per project to base/pdfs-text/[projeto].txt with
all PDFs concatenated. Used as input for phase3_pipeline.py.
"""
from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("pypdf not installed: pip install pypdf", file=sys.stderr)
    sys.exit(1)

BASE = Path.home() / "orcamentos-openclaw" / "base"
QUEUE = BASE / "gemma-queue.json"
OUT_DIR = BASE / "pdfs-text"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = BASE / "phase3-pdf-extract.log.jsonl"

MAX_PAGES = 50
MAX_CHARS_PER_PDF = 30000


def extract_pdf(path: Path) -> tuple[str, dict]:
    info = {"file": path.name, "size_kb": path.stat().st_size // 1024,
            "pages_total": 0, "pages_read": 0, "chars": 0, "errors": []}
    try:
        reader = PdfReader(str(path))
        info["pages_total"] = len(reader.pages)
        chunks = []
        for i, page in enumerate(reader.pages):
            if i >= MAX_PAGES:
                break
            try:
                t = page.extract_text() or ""
                chunks.append(t)
                info["pages_read"] += 1
            except Exception as e:
                info["errors"].append(f"page{i}: {type(e).__name__}")
        text = "\n\n".join(chunks)
        if len(text) > MAX_CHARS_PER_PDF:
            text = text[:MAX_CHARS_PER_PDF] + "\n…[trunc]"
        info["chars"] = len(text)
        return text, info
    except Exception as e:
        info["errors"].append(f"open: {type(e).__name__}: {e}")
        return "", info


def process_project(project: dict) -> dict:
    slug = project["projeto"]
    pdfs = project["sources"].get("pdf", [])
    docxs = project["sources"].get("docx", [])
    summary = {"projeto": slug, "n_pdf": len(pdfs), "n_docx": len(docxs),
               "files": [], "total_chars": 0, "status": "pending"}

    if not pdfs and not docxs:
        summary["status"] = "no_pdf"
        return summary

    out_path = OUT_DIR / f"{slug}.txt"
    parts = [f"# {slug}\n"]

    for p in pdfs:
        text, info = extract_pdf(Path(p))
        summary["files"].append(info)
        if text:
            parts.append(f"\n## PDF: {info['file']}  ({info['pages_read']}/{info['pages_total']} págs)\n")
            parts.append(text)

    for d in docxs:
        try:
            try:
                from docx import Document
            except ImportError:
                summary["files"].append({"file": Path(d).name, "errors": ["python-docx not installed"]})
                continue
            doc = Document(d)
            text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
            if len(text) > MAX_CHARS_PER_PDF:
                text = text[:MAX_CHARS_PER_PDF] + "\n…[trunc]"
            parts.append(f"\n## DOCX: {Path(d).name}\n")
            parts.append(text)
            summary["files"].append({"file": Path(d).name, "chars": len(text), "errors": []})
        except Exception as e:
            summary["files"].append({"file": Path(d).name, "errors": [f"{type(e).__name__}: {e}"]})

    full = "\n".join(parts)
    out_path.write_text(full, encoding="utf-8")
    summary["total_chars"] = len(full)
    summary["status"] = "done" if summary["total_chars"] > 100 else "empty"
    return summary


def main():
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    targets = [p for p in queue if p["sources"].get("pdf") or p["sources"].get("docx")]
    if len(sys.argv) > 1:
        only = sys.argv[1]
        targets = [p for p in targets if p["projeto"] == only]

    print(f"processing {len(targets)} projects with PDFs", flush=True)
    counts = {}
    for i, p in enumerate(targets, 1):
        try:
            s = process_project(p)
        except Exception as e:
            s = {"projeto": p["projeto"], "status": "failed",
                 "error": f"{type(e).__name__}: {e}",
                 "tb": traceback.format_exc()[-300:]}
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
        counts[s["status"]] = counts.get(s["status"], 0) + 1
        n_files = len(s.get("files", []))
        print(f"[{i}/{len(targets)}] {p['projeto']:<40} {s['status']:<8} files={n_files} chars={s.get('total_chars',0)}", flush=True)
    print(f"\nsummary: {counts}")


if __name__ == "__main__":
    main()
