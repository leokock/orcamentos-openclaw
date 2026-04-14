#!/usr/bin/env python3
"""Phase 16a v2 — Extração de quantitativos via geometria (ifcopenshell.geom).

Em vez de tentar ler QTOs (que estão vazios nos IFCs desses projetos), usa
`ifcopenshell.geom.create_shape` + bounding box pra calcular:
- Wall: área = max(dx,dy) × dz  (length × altura)
- Slab: área = dx × dy           (área em planta)
- Beam: comprimento = max(dx,dy,dz); volume = dx×dy×dz
- Column: altura = dz; volume = dx×dy×dz
- Railing: comprimento = max(dx,dy)
- CurtainWall: área = perímetro × altura

Saída: base/quantitativos-bim/[projeto].json (sobrescreve v1)
"""
from __future__ import annotations

import json
import re
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

import ifcopenshell
import ifcopenshell.geom

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = BASE / "quantitativos-bim"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = BASE / "phase16a-v2-extract.log.jsonl"


SETTINGS = ifcopenshell.geom.settings()
try:
    SETTINGS.set("disable-opening-subtractions", True)
except Exception:
    pass


def find_ifcs(slug: str) -> list[str]:
    base = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA") / slug
    if not base.exists():
        return []
    ifcs = []
    for p in base.rglob("*.ifc"):
        sp = str(p).lower()
        if "obsoleto" in sp or "antigo" in sp or "backup" in sp:
            continue
        size = p.stat().st_size
        if size < 1024 * 100:
            continue
        ifcs.append((size, str(p)))
    ifcs.sort(reverse=True)
    return [p for _, p in ifcs[:8]]


def bbox(shape_verts):
    if not shape_verts:
        return None
    xs = shape_verts[0::3]
    ys = shape_verts[1::3]
    zs = shape_verts[2::3]
    if not xs:
        return None
    return (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs))


def geom_of(elem):
    try:
        shape = ifcopenshell.geom.create_shape(SETTINGS, elem)
        return shape.geometry.verts
    except Exception:
        return None


def get_type_name(element) -> str:
    try:
        name = element.Name or ""
        obj_type = element.ObjectType or ""
        try:
            import ifcopenshell.util.element as u
            type_obj = u.get_type(element)
            type_name = (type_obj.Name if type_obj else "") or ""
        except Exception:
            type_name = ""
        for txt in [obj_type, type_name, name]:
            if txt:
                return str(txt)[:120]
    except Exception:
        pass
    return ""


def parse_wall_type(name: str) -> dict:
    m = re.search(r"(\d+(?:[,\.]\d+)?)\s*(?:cm)?", name)
    thickness = None
    if m:
        try:
            thickness = float(m.group(1).replace(",", "."))
        except Exception:
            pass
    material = "outros"
    n = name.lower()
    if "bloco cer" in n or "ceramico" in n or "cerâmico" in n:
        material = "bloco_ceramico"
    elif "concret" in n and "bloco" in n:
        material = "bloco_concreto"
    elif "drywall" in n or "gesso" in n or "placa gesso" in n:
        material = "drywall"
    elif "corta fog" in n or " cf " in n:
        material = "corta_fogo"
    elif "vidro" in n:
        material = "vidro"
    elif "alv" in n:
        material = "alvenaria_generica"
    return {"thickness_cm": thickness, "material": material}


def log_event(e):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def extract_ifc(ifc_path: str) -> dict:
    print(f"  opening {Path(ifc_path).name} ({Path(ifc_path).stat().st_size // 1024 // 1024} MB)...", flush=True)
    t0 = time.time()
    try:
        f = ifcopenshell.open(ifc_path)
    except Exception as e:
        return {"error": f"open: {type(e).__name__}: {e}"}

    result = {
        "file": Path(ifc_path).name,
        "schema": f.schema,
        "walls": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0, "total_length_m": 0},
        "slabs": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0, "total_volume_m3": 0},
        "beams": {"n": 0, "n_geom_ok": 0, "total_volume_m3": 0, "total_length_m": 0},
        "columns": {"n": 0, "n_geom_ok": 0, "total_volume_m3": 0, "total_height_m": 0},
        "doors": {"n": 0, "by_type": {}},
        "windows": {"n": 0, "by_type": {}},
        "stairs": {"n": 0},
        "railings": {"n": 0, "n_geom_ok": 0, "total_length_m": 0},
        "curtain_walls": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0},
        "spaces": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0, "total_volume_m3": 0},
        "roofs": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0},
        "coverings": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0},
    }

    walls = f.by_type("IfcWall") + f.by_type("IfcWallStandardCase")
    print(f"    walls: {len(walls)}", flush=True)
    for w in walls:
        result["walls"]["n"] += 1
        name = get_type_name(w)
        parsed = parse_wall_type(name)
        mat = parsed["material"]
        thick = parsed["thickness_cm"]
        key = f"{mat}_{int(thick) if thick else '?'}cm"
        if key not in result["walls"]["by_type"]:
            result["walls"]["by_type"][key] = {"n": 0, "area_m2": 0, "length_m": 0, "example_names": []}
        bt = result["walls"]["by_type"][key]
        bt["n"] += 1
        if len(bt["example_names"]) < 3 and name:
            bt["example_names"].append(name[:80])

        verts = geom_of(w)
        bb = bbox(verts)
        if bb:
            dx, dy, dz = bb
            length = max(dx, dy)
            area = length * dz
            bt["area_m2"] += area
            bt["length_m"] += length
            result["walls"]["total_area_m2"] += area
            result["walls"]["total_length_m"] += length
            result["walls"]["n_geom_ok"] += 1

    slabs = f.by_type("IfcSlab")
    print(f"    slabs: {len(slabs)}", flush=True)
    for s in slabs:
        result["slabs"]["n"] += 1
        verts = geom_of(s)
        bb = bbox(verts)
        if bb:
            dx, dy, dz = bb
            area = dx * dy
            vol = area * dz
            result["slabs"]["total_area_m2"] += area
            result["slabs"]["total_volume_m3"] += vol
            result["slabs"]["n_geom_ok"] += 1

    beams = f.by_type("IfcBeam")
    print(f"    beams: {len(beams)}", flush=True)
    for b in beams:
        result["beams"]["n"] += 1
        verts = geom_of(b)
        bb = bbox(verts)
        if bb:
            dx, dy, dz = bb
            length = max(dx, dy, dz)
            vol = dx * dy * dz
            result["beams"]["total_length_m"] += length
            result["beams"]["total_volume_m3"] += vol
            result["beams"]["n_geom_ok"] += 1

    cols = f.by_type("IfcColumn")
    print(f"    columns: {len(cols)}", flush=True)
    for c in cols:
        result["columns"]["n"] += 1
        verts = geom_of(c)
        bb = bbox(verts)
        if bb:
            dx, dy, dz = bb
            vol = dx * dy * dz
            result["columns"]["total_height_m"] += dz
            result["columns"]["total_volume_m3"] += vol
            result["columns"]["n_geom_ok"] += 1

    doors = f.by_type("IfcDoor")
    print(f"    doors: {len(doors)}", flush=True)
    for d in doors:
        result["doors"]["n"] += 1
        t = get_type_name(d)[:60] or "sem_tipo"
        result["doors"]["by_type"][t] = result["doors"]["by_type"].get(t, 0) + 1

    wins = f.by_type("IfcWindow")
    print(f"    windows: {len(wins)}", flush=True)
    for w in wins:
        result["windows"]["n"] += 1
        t = get_type_name(w)[:60] or "sem_tipo"
        result["windows"]["by_type"][t] = result["windows"]["by_type"].get(t, 0) + 1

    result["stairs"]["n"] = len(f.by_type("IfcStair"))

    for r in f.by_type("IfcRailing"):
        result["railings"]["n"] += 1
        verts = geom_of(r)
        bb = bbox(verts)
        if bb:
            length = max(bb[0], bb[1])
            result["railings"]["total_length_m"] += length
            result["railings"]["n_geom_ok"] += 1

    for cw in f.by_type("IfcCurtainWall"):
        result["curtain_walls"]["n"] += 1
        verts = geom_of(cw)
        bb = bbox(verts)
        if bb:
            area = max(bb[0], bb[1]) * bb[2]
            result["curtain_walls"]["total_area_m2"] += area
            result["curtain_walls"]["n_geom_ok"] += 1

    spaces = f.by_type("IfcSpace")
    print(f"    spaces: {len(spaces)}", flush=True)
    for s in spaces:
        result["spaces"]["n"] += 1
        long_name = (s.LongName or s.Name or "")[:50] or "sem_nome"
        if long_name not in result["spaces"]["by_type"]:
            result["spaces"]["by_type"][long_name] = {"n": 0, "area_m2": 0}
        bt = result["spaces"]["by_type"][long_name]
        bt["n"] += 1

        verts = geom_of(s)
        bb = bbox(verts)
        if bb:
            dx, dy, dz = bb
            area = dx * dy
            vol = area * dz
            bt["area_m2"] += area
            result["spaces"]["total_area_m2"] += area
            result["spaces"]["total_volume_m3"] += vol
            result["spaces"]["n_geom_ok"] += 1

    for r in f.by_type("IfcRoof"):
        result["roofs"]["n"] += 1
        verts = geom_of(r)
        bb = bbox(verts)
        if bb:
            area = bb[0] * bb[1]
            result["roofs"]["total_area_m2"] += area
            result["roofs"]["n_geom_ok"] += 1

    for c in f.by_type("IfcCovering"):
        result["coverings"]["n"] += 1
        t = get_type_name(c)[:50] or "sem_tipo"
        if t not in result["coverings"]["by_type"]:
            result["coverings"]["by_type"][t] = {"n": 0, "area_m2": 0}
        bt = result["coverings"]["by_type"][t]
        bt["n"] += 1
        verts = geom_of(c)
        bb = bbox(verts)
        if bb:
            area = bb[0] * bb[1]
            bt["area_m2"] += area
            result["coverings"]["total_area_m2"] += area
            result["coverings"]["n_geom_ok"] += 1

    try:
        del f
    except Exception:
        pass

    result["duration_s"] = round(time.time() - t0, 1)
    print(f"    OK in {result['duration_s']}s  walls_geom={result['walls']['n_geom_ok']}/{result['walls']['n']}  slabs={result['slabs']['n_geom_ok']}/{result['slabs']['n']}")
    return result


def merge_consolidado(cons: dict, result: dict):
    for k in ["walls", "slabs", "beams", "columns", "doors", "windows",
               "stairs", "railings", "curtain_walls", "spaces", "roofs", "coverings"]:
        src = result.get(k, {})
        dst = cons[k]
        if "n" in src:
            dst["n"] += src.get("n", 0)
        if "n_geom_ok" in src:
            dst["n_geom_ok"] = dst.get("n_geom_ok", 0) + src.get("n_geom_ok", 0)
        for field in ["total_area_m2", "total_volume_m3", "total_length_m", "total_height_m"]:
            if field in src:
                dst[field] = dst.get(field, 0) + src.get(field, 0)
        if "by_type" in src:
            for tk, tv in src["by_type"].items():
                if tk not in dst["by_type"]:
                    dst["by_type"][tk] = {"n": 0, "area_m2": 0, "length_m": 0, "example_names": []} if isinstance(tv, dict) else 0
                if isinstance(tv, dict):
                    d = dst["by_type"][tk]
                    d["n"] = d.get("n", 0) + tv.get("n", 0)
                    d["area_m2"] = d.get("area_m2", 0) + tv.get("area_m2", 0)
                    d["length_m"] = d.get("length_m", 0) + tv.get("length_m", 0)
                    if "example_names" in tv:
                        for name in tv["example_names"]:
                            if name not in d.get("example_names", []):
                                d.setdefault("example_names", []).append(name)
                                if len(d["example_names"]) >= 5:
                                    break
                else:
                    dst["by_type"][tk] += tv


def process(slug: str):
    print(f"\n=== {slug} ===")
    t0 = time.time()
    ifcs = find_ifcs(slug)
    print(f"{len(ifcs)} IFCs")

    if not ifcs:
        return

    cons = {
        "walls": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0, "total_length_m": 0},
        "slabs": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0, "total_volume_m3": 0},
        "beams": {"n": 0, "n_geom_ok": 0, "total_volume_m3": 0, "total_length_m": 0},
        "columns": {"n": 0, "n_geom_ok": 0, "total_volume_m3": 0, "total_height_m": 0},
        "doors": {"n": 0, "by_type": {}},
        "windows": {"n": 0, "by_type": {}},
        "stairs": {"n": 0},
        "railings": {"n": 0, "n_geom_ok": 0, "total_length_m": 0},
        "curtain_walls": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0},
        "spaces": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0, "total_volume_m3": 0},
        "roofs": {"n": 0, "n_geom_ok": 0, "total_area_m2": 0},
        "coverings": {"n": 0, "n_geom_ok": 0, "by_type": {}, "total_area_m2": 0},
    }

    project_result = {
        "projeto": slug,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "n_ifcs": len(ifcs),
        "method": "geometric_bbox",
        "files": [],
        "consolidado": cons,
    }

    for ifc_path in ifcs:
        try:
            result = extract_ifc(ifc_path)
        except Exception as e:
            result = {"file": Path(ifc_path).name, "error": str(e), "traceback": traceback.format_exc()[-300:]}
            print(f"    ERR: {e}")
        project_result["files"].append(result)
        if "error" not in result:
            merge_consolidado(cons, result)

    project_result["duration_s"] = round(time.time() - t0, 1)

    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(project_result, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    print(f"\n  TOTAIS CONSOLIDADOS (v2 geom):")
    print(f"    Walls:   {cons['walls']['n']:>5}  {cons['walls']['total_area_m2']:>10,.0f} m² ({cons['walls']['n_geom_ok']} geom ok)".replace(",", "."))
    print(f"    Slabs:   {cons['slabs']['n']:>5}  {cons['slabs']['total_area_m2']:>10,.0f} m²  {cons['slabs']['total_volume_m3']:>6,.0f} m³".replace(",", "."))
    print(f"    Beams:   {cons['beams']['n']:>5}  {cons['beams']['total_volume_m3']:>10,.0f} m³".replace(",", "."))
    print(f"    Columns: {cons['columns']['n']:>5}  {cons['columns']['total_volume_m3']:>10,.0f} m³".replace(",", "."))
    print(f"    Doors:   {cons['doors']['n']:>5}")
    print(f"    Windows: {cons['windows']['n']:>5}")
    print(f"    Spaces:  {cons['spaces']['n']:>5}  {cons['spaces']['total_area_m2']:>10,.0f} m²".replace(",", "."))
    print(f"    Curtain: {cons['curtain_walls']['n']:>5}  {cons['curtain_walls']['total_area_m2']:>10,.0f} m²".replace(",", "."))
    print(f"\n  total duration: {project_result['duration_s']}s")

    log_event({"projeto": slug, "duration_s": project_result["duration_s"],
                "walls": cons["walls"], "slabs": cons["slabs"],
                "beams": cons["beams"], "columns": cons["columns"]})


def main():
    for slug in ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]:
        process(slug)


if __name__ == "__main__":
    main()
