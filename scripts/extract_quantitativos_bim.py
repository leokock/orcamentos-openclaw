#!/usr/bin/env python3
"""Phase 16a — Extração exaustiva de quantitativos BIM (IFC) por projeto.

Para cada projeto, abre todos os IFCs disponíveis e extrai quantitativos
dos elementos construtivos:

- IfcWall / IfcWallStandardCase → área por tipo
- IfcSlab → área + volume (lajes)
- IfcBeam → volume + comprimento (vigas)
- IfcColumn → volume + altura (pilares)
- IfcDoor → quantidade por tipo (portas)
- IfcWindow → quantidade por tipo (janelas)
- IfcStair → quantidade (escadas)
- IfcRailing → comprimento (guarda-corpos)
- IfcCurtainWall → área (pele de vidro)
- IfcSpace → área + volume + contagem por tipo (ambientes)
- IfcRoof → área
- IfcCovering → área por tipo (pisos, forros, revestimentos)

Saída: base/quantitativos-bim/[projeto].json
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
import ifcopenshell.util.element as ifcutil

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = BASE / "quantitativos-bim"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = BASE / "phase16a-extract.log.jsonl"

PROJETOS = {
    "arthen-arboris": [
        r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA\arthen-arboris\IFC-ARBORIS 16.03.26\IFC\CORTAFF_ARB_PEX_ARQ_MODELO FEDERADO_R02_16-03-26.ifc",
    ],
    "thozen-electra": [],
    "placon-arminio-tavares": [],
}


def find_ifcs(slug: str) -> list[str]:
    base_drive = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA") / slug
    if not base_drive.exists():
        return []
    ifcs = []
    for p in base_drive.rglob("*.ifc"):
        sp = str(p).lower()
        if "obsoleto" in sp or "antigo" in sp or "backup" in sp:
            continue
        size = p.stat().st_size
        if size < 1024:
            continue
        ifcs.append((size, str(p)))
    ifcs.sort(reverse=True)
    return [p for _, p in ifcs[:8]]


def get_qto_value(element, prop_names: list[str]) -> float | None:
    """Extract numeric quantity from element via ifcopenshell.util.element."""
    try:
        psets = ifcutil.get_psets(element, qtos_only=True)
        for pset_name, pset_data in psets.items():
            for key, val in pset_data.items():
                if any(pn.lower() in key.lower() for pn in prop_names):
                    if isinstance(val, (int, float)) and val > 0:
                        return float(val)
    except Exception:
        pass
    return None


def get_type_name(element) -> str:
    """Get material/type from element name or type."""
    try:
        name = element.Name or ""
        obj_type = element.ObjectType or ""

        type_obj = ifcutil.get_type(element)
        type_name = (type_obj.Name if type_obj else "") or ""

        for txt in [obj_type, type_name, name]:
            if txt:
                return str(txt)[:120]
    except Exception:
        pass
    return ""


def parse_wall_type(name: str) -> dict:
    """Extract wall thickness + material from name (ex: ALV_14_BLOCO CERAMICO)."""
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
    elif "corta fog" in n or "cf " in n.lower():
        material = "corta_fogo"
    elif "vidro" in n:
        material = "vidro"
    return {"thickness_cm": thickness, "material": material}


def extract_ifc(ifc_path: str) -> dict:
    print(f"  opening {Path(ifc_path).name} ({Path(ifc_path).stat().st_size // 1024 // 1024} MB)...", flush=True)
    t0 = time.time()
    try:
        f = ifcopenshell.open(ifc_path)
    except Exception as e:
        return {"error": f"open: {type(e).__name__}: {e}"}

    print(f"    loaded in {time.time()-t0:.1f}s, schema={f.schema}")

    result = {
        "file": Path(ifc_path).name,
        "schema": f.schema,
        "walls": {"n": 0, "by_type": {}, "total_area_m2": 0, "total_length_m": 0},
        "slabs": {"n": 0, "total_area_m2": 0, "total_volume_m3": 0},
        "beams": {"n": 0, "total_volume_m3": 0, "total_length_m": 0},
        "columns": {"n": 0, "total_volume_m3": 0, "total_height_m": 0},
        "doors": {"n": 0, "by_type": {}},
        "windows": {"n": 0, "by_type": {}},
        "stairs": {"n": 0},
        "railings": {"n": 0, "total_length_m": 0},
        "curtain_walls": {"n": 0, "total_area_m2": 0},
        "spaces": {"n": 0, "by_type": {}, "total_area_m2": 0, "total_volume_m3": 0},
        "roofs": {"n": 0, "total_area_m2": 0},
        "coverings": {"n": 0, "by_type": {}, "total_area_m2": 0},
    }

    t = time.time()
    wall_types = f.by_type("IfcWall") + f.by_type("IfcWallStandardCase")
    print(f"    processing {len(wall_types)} walls...", flush=True)
    for w in wall_types:
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

        area = get_qto_value(w, ["GrossSideArea", "NetSideArea", "GrossArea", "NetArea"])
        length = get_qto_value(w, ["Length"])
        if area:
            bt["area_m2"] += area
            result["walls"]["total_area_m2"] += area
        if length:
            bt["length_m"] += length
            result["walls"]["total_length_m"] += length
        result["walls"]["n"] += 1

    slabs = f.by_type("IfcSlab")
    print(f"    processing {len(slabs)} slabs...", flush=True)
    for s in slabs:
        result["slabs"]["n"] += 1
        area = get_qto_value(s, ["GrossArea", "NetArea"])
        vol = get_qto_value(s, ["GrossVolume", "NetVolume"])
        if area:
            result["slabs"]["total_area_m2"] += area
        if vol:
            result["slabs"]["total_volume_m3"] += vol

    beams = f.by_type("IfcBeam")
    print(f"    processing {len(beams)} beams...", flush=True)
    for b in beams:
        result["beams"]["n"] += 1
        vol = get_qto_value(b, ["GrossVolume", "NetVolume"])
        length = get_qto_value(b, ["Length"])
        if vol:
            result["beams"]["total_volume_m3"] += vol
        if length:
            result["beams"]["total_length_m"] += length

    cols = f.by_type("IfcColumn")
    print(f"    processing {len(cols)} columns...", flush=True)
    for c in cols:
        result["columns"]["n"] += 1
        vol = get_qto_value(c, ["GrossVolume", "NetVolume"])
        h = get_qto_value(c, ["Height", "Length"])
        if vol:
            result["columns"]["total_volume_m3"] += vol
        if h:
            result["columns"]["total_height_m"] += h

    doors = f.by_type("IfcDoor")
    print(f"    processing {len(doors)} doors...", flush=True)
    for d in doors:
        result["doors"]["n"] += 1
        t_name = get_type_name(d)
        key = t_name[:60] or "sem_tipo"
        if key not in result["doors"]["by_type"]:
            result["doors"]["by_type"][key] = 0
        result["doors"]["by_type"][key] += 1

    wins = f.by_type("IfcWindow")
    print(f"    processing {len(wins)} windows...", flush=True)
    for w in wins:
        result["windows"]["n"] += 1
        t_name = get_type_name(w)
        key = t_name[:60] or "sem_tipo"
        if key not in result["windows"]["by_type"]:
            result["windows"]["by_type"][key] = 0
        result["windows"]["by_type"][key] += 1

    result["stairs"]["n"] = len(f.by_type("IfcStair"))

    railings = f.by_type("IfcRailing")
    for r in railings:
        result["railings"]["n"] += 1
        length = get_qto_value(r, ["Length"])
        if length:
            result["railings"]["total_length_m"] += length

    cws = f.by_type("IfcCurtainWall")
    for cw in cws:
        result["curtain_walls"]["n"] += 1
        area = get_qto_value(cw, ["GrossArea", "NetArea", "GrossSideArea"])
        if area:
            result["curtain_walls"]["total_area_m2"] += area

    spaces = f.by_type("IfcSpace")
    print(f"    processing {len(spaces)} spaces...", flush=True)
    for s in spaces:
        result["spaces"]["n"] += 1
        long_name = s.LongName or s.Name or ""
        key = (long_name[:50] or "sem_nome")
        if key not in result["spaces"]["by_type"]:
            result["spaces"]["by_type"][key] = {"n": 0, "area_m2": 0}
        bt = result["spaces"]["by_type"][key]
        bt["n"] += 1
        area = get_qto_value(s, ["GrossFloorArea", "NetFloorArea", "GrossArea", "NetArea"])
        vol = get_qto_value(s, ["GrossVolume", "NetVolume"])
        if area:
            bt["area_m2"] += area
            result["spaces"]["total_area_m2"] += area
        if vol:
            result["spaces"]["total_volume_m3"] += vol

    for r in f.by_type("IfcRoof"):
        result["roofs"]["n"] += 1
        area = get_qto_value(r, ["GrossArea", "NetArea"])
        if area:
            result["roofs"]["total_area_m2"] += area

    covers = f.by_type("IfcCovering")
    for c in covers:
        result["coverings"]["n"] += 1
        t_name = get_type_name(c)
        key = t_name[:50] or "sem_tipo"
        if key not in result["coverings"]["by_type"]:
            result["coverings"]["by_type"][key] = {"n": 0, "area_m2": 0}
        bt = result["coverings"]["by_type"][key]
        bt["n"] += 1
        area = get_qto_value(c, ["GrossArea", "NetArea"])
        if area:
            bt["area_m2"] += area
            result["coverings"]["total_area_m2"] += area

    try:
        del f
    except Exception:
        pass

    result["duration_s"] = round(time.time() - t0, 1)
    print(f"    OK in {result['duration_s']}s")
    return result


def log_event(e):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def process(slug: str):
    print(f"\n=== {slug} ===")
    t0 = time.time()
    ifcs = find_ifcs(slug)
    print(f"{len(ifcs)} IFCs found:")
    for p in ifcs:
        print(f"  {p}")

    if not ifcs:
        return

    project_result = {
        "projeto": slug,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "n_ifcs": len(ifcs),
        "files": [],
        "consolidado": {
            "walls": {"n": 0, "by_type": {}, "total_area_m2": 0, "total_length_m": 0},
            "slabs": {"n": 0, "total_area_m2": 0, "total_volume_m3": 0},
            "beams": {"n": 0, "total_volume_m3": 0, "total_length_m": 0},
            "columns": {"n": 0, "total_volume_m3": 0, "total_height_m": 0},
            "doors": {"n": 0, "by_type": {}},
            "windows": {"n": 0, "by_type": {}},
            "stairs": {"n": 0},
            "railings": {"n": 0, "total_length_m": 0},
            "curtain_walls": {"n": 0, "total_area_m2": 0},
            "spaces": {"n": 0, "by_type": {}, "total_area_m2": 0, "total_volume_m3": 0},
            "roofs": {"n": 0, "total_area_m2": 0},
            "coverings": {"n": 0, "by_type": {}, "total_area_m2": 0},
        },
    }

    for ifc_path in ifcs:
        try:
            result = extract_ifc(ifc_path)
        except Exception as e:
            result = {"file": Path(ifc_path).name, "error": str(e), "traceback": traceback.format_exc()[-300:]}
            print(f"    ERR: {e}")
        project_result["files"].append(result)

        if "error" not in result:
            cons = project_result["consolidado"]
            for k in ["walls", "slabs", "beams", "columns", "doors", "windows",
                       "stairs", "railings", "curtain_walls", "spaces", "roofs", "coverings"]:
                src = result.get(k, {})
                dst = cons[k]
                if "n" in src:
                    dst["n"] += src.get("n", 0)
                for field in ["total_area_m2", "total_volume_m3", "total_length_m", "total_height_m"]:
                    if field in src:
                        dst[field] = dst.get(field, 0) + src.get(field, 0)
                if "by_type" in src:
                    for tk, tv in src["by_type"].items():
                        if tk not in dst["by_type"]:
                            dst["by_type"][tk] = {"n": 0, "area_m2": 0} if isinstance(tv, dict) else 0
                        if isinstance(tv, dict):
                            for f in ["n", "area_m2", "length_m"]:
                                if f in tv:
                                    dst["by_type"][tk][f] = dst["by_type"][tk].get(f, 0) + tv[f]
                        else:
                            dst["by_type"][tk] += tv

    project_result["duration_s"] = round(time.time() - t0, 1)

    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(project_result, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    print(f"\n  TOTAIS CONSOLIDADOS:")
    cons = project_result["consolidado"]
    print(f"    Walls:    {cons['walls']['n']:>5}  {cons['walls']['total_area_m2']:,.0f} m²")
    print(f"    Slabs:    {cons['slabs']['n']:>5}  {cons['slabs']['total_area_m2']:,.0f} m²  {cons['slabs']['total_volume_m3']:,.0f} m³")
    print(f"    Beams:    {cons['beams']['n']:>5}  {cons['beams']['total_volume_m3']:,.0f} m³")
    print(f"    Columns:  {cons['columns']['n']:>5}  {cons['columns']['total_volume_m3']:,.0f} m³")
    print(f"    Doors:    {cons['doors']['n']:>5}")
    print(f"    Windows:  {cons['windows']['n']:>5}")
    print(f"    Spaces:   {cons['spaces']['n']:>5}  {cons['spaces']['total_area_m2']:,.0f} m²")
    print(f"    Curtain:  {cons['curtain_walls']['n']:>5}  {cons['curtain_walls']['total_area_m2']:,.0f} m²")
    print(f"\n  {out}")
    log_event({"projeto": slug, "n_ifcs": len(ifcs), "duration_s": project_result["duration_s"], "consolidado_totals": {
        k: {"n": v.get("n", 0), "area": v.get("total_area_m2", 0), "vol": v.get("total_volume_m3", 0)}
        for k, v in cons.items() if isinstance(v, dict)
    }})


def main():
    for slug in ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]:
        process(slug)


if __name__ == "__main__":
    main()
