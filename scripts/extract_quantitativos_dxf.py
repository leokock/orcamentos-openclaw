#!/usr/bin/env python3
"""Phase 16b — Extração de quantitativos via DXF (ezdxf).

Lê arquivos .dxf dos projetos e extrai:
- Textos TEXT/MTEXT (nomes de ambientes, quantitativos em legendas)
- Entidades por layer (alvenaria, esquadria, etc)
- Linhas com comprimento (guarda-corpos, rodapés)
- Hachuras por área (pisos, alvenaria, revestimento)
- Círculos (pontos elétricos, pontos hidráulicos)

Saída: base/quantitativos-dxf/[projeto].json
"""
from __future__ import annotations

import json
import re
import sys
import time
import traceback
from collections import Counter
from datetime import datetime
from pathlib import Path

import ezdxf

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = BASE / "quantitativos-dxf"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = BASE / "phase16b-extract.log.jsonl"

LAZER_KEYWORDS = {
    "piscina", "pool", "ofurô", "ofuro", "jacuzzi", "spa", "sauna",
    "academia", "fitness", "quadra", "salão", "salao", "gourmet",
    "churrasqueira", "fire place", "playground", "brinquedoteca",
    "kids", "coworking", "pet", "bicicletário",
}


def find_dxfs(slug: str) -> list[Path]:
    base_drive = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA") / slug
    if not base_drive.exists():
        return []
    dxfs = []
    for p in base_drive.rglob("*.dxf"):
        sp = str(p).lower()
        if "obsoleto" in sp or "antigo" in sp or "backup" in sp or "dxf-temp" not in sp.replace("dxf-temp-ref", ""):
            if "dxf-temp" not in sp and "dxf-arcondicionado" not in sp and "dxf-exaustao" not in sp and "dxf-ventilacao" not in sp:
                continue
        dxfs.append(p)
    return sorted(dxfs)


def extract_dxf(dxf_path: Path) -> dict:
    result = {
        "file": dxf_path.name,
        "parent_folder": dxf_path.parent.name,
        "layers": {},
        "texts": [],
        "entities_count": Counter(),
        "circles_count": 0,
        "line_total_length": 0,
        "text_hits": [],
        "errors": [],
    }

    try:
        doc = ezdxf.readfile(str(dxf_path), errors="ignore")
    except Exception as e:
        result["errors"].append(f"open: {type(e).__name__}: {str(e)[:80]}")
        return result

    try:
        msp = doc.modelspace()
    except Exception as e:
        result["errors"].append(f"msp: {e}")
        return result

    texts_set = set()
    count = 0

    for e in msp:
        count += 1
        if count > 100000:
            break

        etype = e.dxftype()
        result["entities_count"][etype] += 1

        layer = e.dxf.get("layer", "?") if hasattr(e.dxf, "get") else "?"
        if layer not in result["layers"]:
            result["layers"][layer] = Counter()
        result["layers"][layer][etype] += 1

        if etype == "TEXT":
            try:
                text = (e.dxf.text or "").strip()
            except Exception:
                text = ""
            if text and text not in texts_set:
                texts_set.add(text)
                if len(result["texts"]) < 500:
                    result["texts"].append({"layer": layer, "text": text[:200]})
                tl = text.lower()
                for kw in LAZER_KEYWORDS:
                    if kw in tl:
                        result["text_hits"].append({"keyword": kw, "text": text[:150], "layer": layer})
                        break

        elif etype == "MTEXT":
            try:
                text = (e.text or "").strip()
            except Exception:
                text = ""
            if text and text not in texts_set:
                texts_set.add(text)
                if len(result["texts"]) < 500:
                    result["texts"].append({"layer": layer, "text": text[:200]})

        elif etype == "CIRCLE":
            result["circles_count"] += 1

        elif etype == "LINE":
            try:
                start = e.dxf.start
                end = e.dxf.end
                dx = end[0] - start[0]
                dy = end[1] - start[1]
                length = (dx * dx + dy * dy) ** 0.5
                result["line_total_length"] += length
            except Exception:
                pass

    result["entities_count"] = dict(result["entities_count"])
    result["layers"] = {k: dict(v) for k, v in result["layers"].items()}
    result["n_texts_unique"] = len(texts_set)

    try:
        del doc
    except Exception:
        pass

    return result


def log_event(e):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def process(slug: str):
    print(f"\n=== {slug} ===")
    t0 = time.time()
    dxfs = find_dxfs(slug)
    print(f"{len(dxfs)} DXFs found (dxf-temp/ + dxf-arcondicionado/ + dxf-exaustao/)")

    if not dxfs:
        print("  nenhum DXF - ok")
        return

    project_result = {
        "projeto": slug,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "n_dxfs": len(dxfs),
        "files": [],
    }

    for dxf_path in dxfs:
        print(f"  {dxf_path.name[:60]}... ", end="", flush=True)
        t = time.time()
        try:
            result = extract_dxf(dxf_path)
        except Exception as e:
            result = {"file": dxf_path.name, "error": str(e)[:200]}
        result["duration_s"] = round(time.time() - t, 1)
        project_result["files"].append(result)
        n_ent = sum(result.get("entities_count", {}).values())
        n_txt = result.get("n_texts_unique", 0)
        hits = len(result.get("text_hits", []))
        err = result.get("errors") or result.get("error", "")
        status = f"{n_ent:>5} ent  {n_txt:>4} txts  {hits:>2} hits  {result['duration_s']}s"
        if err:
            status += f"  ERR: {str(err)[:40]}"
        print(status, flush=True)

    project_result["duration_s"] = round(time.time() - t0, 1)
    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(project_result, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    log_event({"projeto": slug, "n_dxfs": len(dxfs), "duration_s": project_result["duration_s"]})
    print(f"\n  saved: {out}  ({project_result['duration_s']}s)")


def main():
    for slug in ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]:
        process(slug)


if __name__ == "__main__":
    main()
