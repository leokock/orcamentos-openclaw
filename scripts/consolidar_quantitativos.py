#!/usr/bin/env python3
"""Phase 16d — Consolida quantitativos BIM + DXF + PDF por projeto.

Lê as 3 fontes (Fase 16a, 16b, 16c) e gera um JSON unificado por projeto
com todos os quantitativos encontrados, prontos para usar como base no
memorial de extração (Fase 17).

Estrutura de saída:
{
    "projeto": "slug",
    "ac_m2": 12472,
    "ur": 98,
    "quantitativos": {
        "alvenaria": {...},
        "estrutura": {...},
        "esquadrias": {...},
        "ambientes": {...},
        "especiais": {...}
    },
    "fontes": [...]
}
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
BIM_DIR = BASE / "quantitativos-bim"
DXF_DIR = BASE / "quantitativos-dxf"
PDF_DIR = BASE / "quantitativos-pdf"
OUT_DIR = BASE / "quantitativos-consolidados"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def consolidar(slug: str) -> dict:
    bim = load_json(BIM_DIR / f"{slug}.json")
    dxf = load_json(DXF_DIR / f"{slug}.json")
    pdf = load_json(PDF_DIR / f"{slug}.json")
    indices = load_json(BASE / "indices-executivo" / f"{slug}.json")
    state = load_json(BASE / "pacotes" / slug / "state.json")

    ac = state.get("ac") or indices.get("ac") or 0
    ur = state.get("ur") or indices.get("ur") or 0

    cons = {
        "projeto": slug,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "ac_referencia_m2": ac,
        "ur_referencia": ur,
        "fontes": {
            "bim": bim.get("n_ifcs", 0),
            "dxf": dxf.get("n_dxfs", 0),
            "pdf": pdf.get("n_pdfs", 0),
        },
        "quantitativos": {},
    }

    bim_cons = bim.get("consolidado", {})

    walls = bim_cons.get("walls", {})
    alv = {
        "n_unidades": walls.get("n", 0),
        "area_total_m2": round(walls.get("total_area_m2", 0), 2),
        "comprimento_total_m": round(walls.get("total_length_m", 0), 2),
        "por_tipo": {},
        "fonte": "BIM IfcWall + IfcWallStandardCase",
    }
    for key, data in walls.get("by_type", {}).items():
        alv["por_tipo"][key] = {
            "qtd": data.get("n", 0),
            "area_m2": round(data.get("area_m2", 0), 2),
            "comprimento_m": round(data.get("length_m", 0), 2),
            "exemplos": data.get("example_names", []),
        }
    cons["quantitativos"]["alvenaria_e_paredes"] = alv

    slabs = bim_cons.get("slabs", {})
    beams = bim_cons.get("beams", {})
    cols = bim_cons.get("columns", {})
    estr = {
        "lajes": {
            "n": slabs.get("n", 0),
            "area_m2": round(slabs.get("total_area_m2", 0), 2),
            "volume_m3": round(slabs.get("total_volume_m3", 0), 2),
            "fonte": "BIM IfcSlab",
        },
        "vigas": {
            "n": beams.get("n", 0),
            "volume_m3": round(beams.get("total_volume_m3", 0), 2),
            "comprimento_m": round(beams.get("total_length_m", 0), 2),
            "fonte": "BIM IfcBeam",
        },
        "pilares": {
            "n": cols.get("n", 0),
            "volume_m3": round(cols.get("total_volume_m3", 0), 2),
            "altura_total_m": round(cols.get("total_height_m", 0), 2),
            "fonte": "BIM IfcColumn",
        },
    }

    concreto_total = (slabs.get("total_volume_m3", 0) + beams.get("total_volume_m3", 0) + cols.get("total_volume_m3", 0))
    if concreto_total > 0:
        estr["concreto_total_m3_estimado"] = round(concreto_total, 2)
        if ac > 0:
            estr["concreto_por_m2_ac_estimado"] = round(concreto_total / ac, 4)

    cons["quantitativos"]["estrutura"] = estr

    doors = bim_cons.get("doors", {})
    wins = bim_cons.get("windows", {})
    cws = bim_cons.get("curtain_walls", {})
    rails = bim_cons.get("railings", {})
    esq = {
        "portas": {
            "n": doors.get("n", 0),
            "fonte": "BIM IfcDoor",
            "top_tipos": dict(sorted(doors.get("by_type", {}).items(), key=lambda x: -x[1])[:15]),
        },
        "janelas": {
            "n": wins.get("n", 0),
            "fonte": "BIM IfcWindow",
            "top_tipos": dict(sorted(wins.get("by_type", {}).items(), key=lambda x: -x[1])[:15]),
        },
        "pele_de_vidro": {
            "n": cws.get("n", 0),
            "area_m2": round(cws.get("total_area_m2", 0), 2),
            "fonte": "BIM IfcCurtainWall",
        },
        "guarda_corpos": {
            "n": rails.get("n", 0),
            "comprimento_m": round(rails.get("total_length_m", 0), 2),
            "fonte": "BIM IfcRailing",
        },
    }
    cons["quantitativos"]["esquadrias_e_aberturas"] = esq

    spaces = bim_cons.get("spaces", {})
    amb = {
        "n": spaces.get("n", 0),
        "area_total_m2": round(spaces.get("total_area_m2", 0), 2),
        "volume_total_m3": round(spaces.get("total_volume_m3", 0), 2),
        "fonte": "BIM IfcSpace",
        "top_tipos": {},
    }
    for key, data in list(sorted(spaces.get("by_type", {}).items(),
                                  key=lambda x: -(x[1].get("area_m2", 0) if isinstance(x[1], dict) else 0)))[:30]:
        if isinstance(data, dict):
            amb["top_tipos"][key] = {
                "n": data.get("n", 0),
                "area_m2": round(data.get("area_m2", 0), 2),
            }
    cons["quantitativos"]["ambientes"] = amb

    covs = bim_cons.get("coverings", {})
    roofs = bim_cons.get("roofs", {})
    acab = {
        "coverings": {
            "n": covs.get("n", 0),
            "area_total_m2": round(covs.get("total_area_m2", 0), 2),
            "por_tipo": covs.get("by_type", {}),
            "fonte": "BIM IfcCovering",
        },
        "cobertura": {
            "n": roofs.get("n", 0),
            "area_m2": round(roofs.get("total_area_m2", 0), 2),
            "fonte": "BIM IfcRoof",
        },
        "escadas_n": bim_cons.get("stairs", {}).get("n", 0),
    }
    cons["quantitativos"]["acabamentos"] = acab

    dxf_totals = {
        "n_dxfs_lidos": dxf.get("n_dxfs", 0),
        "arquivos_com_hit_lazer": sum(1 for f in dxf.get("files", []) if f.get("text_hits")),
        "total_hits_lazer": sum(len(f.get("text_hits", [])) for f in dxf.get("files", [])),
        "fonte": "DXF ezdxf",
    }
    cons["quantitativos"]["dxf_quantitativos"] = dxf_totals

    if pdf.get("files"):
        pdf_areas = []
        for f in pdf["files"]:
            for a in f.get("areas_encontradas", [])[:20]:
                pdf_areas.append(a)
        cons["quantitativos"]["pdf_areas_encontradas"] = {
            "total": len(pdf_areas),
            "amostra": pdf_areas[:30],
            "fonte": "PDF memoriais",
        }

    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps(cons, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return cons


def main():
    for slug in ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]:
        print(f"\n=== {slug} ===")
        bim_path = BIM_DIR / f"{slug}.json"
        if not bim_path.exists():
            print("  BIM ainda nao disponivel, skip")
            continue

        cons = consolidar(slug)
        q = cons["quantitativos"]
        print(f"  AC ref: {cons['ac_referencia_m2']:,.0f} m²")
        print(f"  Alvenaria: {q['alvenaria_e_paredes']['n_unidades']} unidades, {q['alvenaria_e_paredes']['area_total_m2']:,.0f} m²")
        print(f"  Lajes: {q['estrutura']['lajes']['n']}, {q['estrutura']['lajes']['area_m2']:,.0f} m², {q['estrutura']['lajes']['volume_m3']:,.1f} m³")
        print(f"  Vigas: {q['estrutura']['vigas']['n']}, {q['estrutura']['vigas']['volume_m3']:,.1f} m³")
        print(f"  Pilares: {q['estrutura']['pilares']['n']}, {q['estrutura']['pilares']['volume_m3']:,.1f} m³")
        print(f"  Portas: {q['esquadrias_e_aberturas']['portas']['n']}")
        print(f"  Janelas: {q['esquadrias_e_aberturas']['janelas']['n']}")
        print(f"  Ambientes (IfcSpace): {q['ambientes']['n']}, {q['ambientes']['area_total_m2']:,.0f} m²")
        print(f"  saved: {OUT_DIR / f'{slug}.json'}")


if __name__ == "__main__":
    main()
