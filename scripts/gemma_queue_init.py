#!/usr/bin/env python3
"""Build gemma-queue.json from _all_projects_mapping.json.

For each project, scan its source folder on Drive and list .xlsx/.pdf/.docx
files (mcp-ollama doesn't support .pptx). The queue feeds the overnight
Gemma loop that enriches base/indices-executivo/[projeto].json with a
qualitative layer.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
MAPPING = BASE / "_all_projects_mapping.json"
INDICES = BASE / "indices-executivo"
QUEUE_OUT = BASE / "gemma-queue.json"

SUPPORTED = {".xlsx", ".pdf", ".docx"}


def normalize_path(win_path: str) -> Path:
    """Return a pathlib.Path that works on the current OS.

    Mapping JSON stores Windows paths ('G:\\Drives compartilhados\\...').
    On Windows we keep them as-is. On POSIX we'd convert to /g/... — not
    implemented here because the loop runs on Windows.
    """
    return Path(win_path)


def scan_project_sources(xlsx_path: Path) -> dict[str, list[str]]:
    folder = xlsx_path.parent
    sources: dict[str, list[str]] = {"xlsx": [], "pdf": [], "docx": []}
    if not folder.exists():
        return sources
    for entry in sorted(folder.iterdir()):
        ext = entry.suffix.lower()
        if ext in SUPPORTED:
            sources[ext.lstrip(".")].append(str(entry))
    return sources


def main() -> None:
    mapping = json.loads(MAPPING.read_text(encoding="utf-8"))
    queue: list[dict] = []
    missing_sources = 0
    missing_json = 0

    for entry in mapping:
        slug = entry["slug"]
        json_path = INDICES / f"{slug}.json"
        xlsx_path = normalize_path(entry["path"])
        sources = scan_project_sources(xlsx_path)

        total_files = sum(len(v) for v in sources.values())
        if total_files == 0:
            missing_sources += 1
        if not json_path.exists():
            missing_json += 1

        queue.append(
            {
                "projeto": slug,
                "status": "pending",
                "sources": sources,
                "json_existente": str(json_path),
                "json_existente_existe": json_path.exists(),
                "folder_drive": str(xlsx_path.parent),
                "ac_existente": None,
            }
        )

        if json_path.exists():
            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
                queue[-1]["ac_existente"] = data.get("ac")
            except Exception:
                pass

    QUEUE_OUT.write_text(
        json.dumps(queue, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"queue size: {len(queue)}")
    print(f"missing source folders: {missing_sources}")
    print(f"missing JSON existente: {missing_json}")
    print(f"written: {QUEUE_OUT}")

    by_count = {}
    for q in queue:
        n = sum(len(v) for v in q["sources"].values())
        by_count[n] = by_count.get(n, 0) + 1
    print("files-per-project distribution:", dict(sorted(by_count.items())))


if __name__ == "__main__":
    main()
