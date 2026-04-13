#!/usr/bin/env python3
"""Test other Placon IFCs + DXF reading via ezdxf."""
import ifcopenshell
import ezdxf

BASE = r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA"

LAZER_KEYWORDS = [
    "piscina", "pool", "ofurô", "ofuro", "jacuzzi", "spa", "sauna",
    "academia", "fitness", "quadra", "salão", "salao", "festa",
    "gourmet", "churrasqu", "fire place", "pub", "lounge", "game",
    "playground", "brinquedoteca", "kids", "coworking", "pet",
    "lazer", "recrea",
]


def test_ifc(label, path):
    print(f"\n=== {label} ===")
    print(f"  path: {path}")
    try:
        f = ifcopenshell.open(path)
        print(f"  schema: {f.schema}")
        spaces = f.by_type("IfcSpace")
        print(f"  IfcSpace count: {len(spaces)}")
        hits = 0
        for s in spaces:
            name = ((s.Name or "") + " " + (s.LongName or "")).lower()
            if any(kw in name for kw in LAZER_KEYWORDS):
                hits += 1
        print(f"  lazer hits: {hits}")
        if spaces and hits == 0:
            print("  sample space names:")
            for s in spaces[:10]:
                n = (s.Name or "") + " | " + (s.LongName or "")
                print(f"    - {n[:80]}")
        # Also try IfcBuildingStorey (pavimentos)
        stories = f.by_type("IfcBuildingStorey")
        print(f"  IfcBuildingStorey count: {len(stories)}")
        for st in stories[:8]:
            print(f"    - {st.Name}")
        # Also IfcZone or IfcGroup
        zones = f.by_type("IfcZone")
        print(f"  IfcZone count: {len(zones)}")
    except Exception as e:
        print(f"  ERR: {type(e).__name__}: {e}")


def test_dxf(label, path):
    print(f"\n=== DXF {label} ===")
    print(f"  path: {path}")
    try:
        doc = ezdxf.readfile(path)
        msp = doc.modelspace()
        n_ents = len(list(msp))
        print(f"  version: {doc.dxfversion}")
        print(f"  modelspace entities: {n_ents}")
        # Extract all text
        texts = []
        for e in msp:
            if e.dxftype() in ("TEXT", "MTEXT"):
                t = e.dxf.get("text", "") if e.dxftype() == "TEXT" else e.text
                if t:
                    texts.append(str(t).strip())
        print(f"  text entities: {len(texts)}")
        # Check for lazer keywords
        hits = []
        for t in texts:
            tl = t.lower()
            for kw in LAZER_KEYWORDS:
                if kw in tl:
                    hits.append((kw, t[:80]))
                    break
        print(f"  lazer hits in text: {len(hits)}")
        for kw, t in hits[:15]:
            print(f"    [{kw}] {t}")
    except Exception as e:
        print(f"  ERR: {type(e).__name__}: {e}")


placon_ifcs = [
    ("Placon PE02", BASE + r"\placon-arminio-tavares\Arquitetonico\PE02\IFC\PLA_ARM_ARQ_EX_IFC_PE02.ifc"),
    ("Placon AP-INÍCIO", BASE + r"\placon-arminio-tavares\Arquitetonico\AP - INÍCIO DE OBRA\03_IFC\PLA_ARM_ARQ_EP_R06.ifc"),
    ("Placon PE01-PRÉVIO", BASE + r"\placon-arminio-tavares\Arquitetonico\PE01 - PRÉVIO (SUB e 1º PAV)\03_IFC\SAO_PLACON ARMÍNIO_AP_R01.ifc"),
]
for label, p in placon_ifcs:
    test_ifc(label, p)

thozen_dxfs = [
    ("Thozen LAZER", BASE + r"\thozen-electra\dxf-temp\RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dxf"),
    ("Thozen TÉRREO", BASE + r"\thozen-electra\dxf-temp\RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dxf"),
]
for label, p in thozen_dxfs:
    test_dxf(label, p)
