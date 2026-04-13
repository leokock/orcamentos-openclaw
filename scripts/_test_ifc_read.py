#!/usr/bin/env python3
"""Smoke test — ifcopenshell + ezdxf, IFC reading with lazer keywords."""
import sys
import time
from pathlib import Path

try:
    import ifcopenshell
    print(f"ifcopenshell OK: {ifcopenshell.version}")
except ImportError as e:
    print(f"ifcopenshell FAIL: {e}")
    sys.exit(1)

try:
    import ezdxf
    print(f"ezdxf OK: {ezdxf.__version__}")
except ImportError as e:
    print(f"ezdxf FAIL: {e}")

LAZER_KEYWORDS = [
    "piscina", "pool", "ofurô", "ofuro", "jacuzzi", "spa", "sauna",
    "academia", "fitness", "musculaç", "quadra", "squash",
    "salão", "salao", "festa", "gourmet", "churrasqu", "fire place", "pub",
    "lounge", "game", "bar",
    "playground", "brinquedoteca", "kids", "fraldário",
    "coworking", "office", "reuni",
    "pet", "bicicletário", "bike",
    "lazer", "recrea", "convivência",
]


def test_ifc(ifc_path: str) -> dict:
    t0 = time.time()
    print(f"\n=== testing {Path(ifc_path).name} ===")
    try:
        f = ifcopenshell.open(ifc_path)
        print(f"  opened in {time.time()-t0:.1f}s")
        print(f"  schema: {f.schema}")

        spaces = f.by_type("IfcSpace")
        print(f"  IfcSpace count: {len(spaces)}")

        hits = []
        all_names = set()
        for s in spaces:
            name = (s.Name or "") + " " + (s.LongName or "")
            name_lower = name.lower()
            if name.strip():
                all_names.add(name.strip()[:80])
            for kw in LAZER_KEYWORDS:
                if kw in name_lower:
                    hits.append({"kw": kw, "name": name.strip()})
                    break

        print(f"  unique space names: {len(all_names)}")
        print(f"  lazer hits: {len(hits)}")
        for h in hits[:12]:
            print(f"    - [{h['kw']}] {h['name'][:70]}")

        if len(all_names) < 30:
            print(f"  all names (sample):")
            for n in sorted(all_names)[:20]:
                print(f"    · {n}")

        return {"ifc": Path(ifc_path).name, "schema": f.schema,
                "n_spaces": len(spaces), "n_hits": len(hits), "duration": round(time.time()-t0, 1)}
    except Exception as e:
        print(f"  ERR: {type(e).__name__}: {e}")
        return {"ifc": Path(ifc_path).name, "error": str(e)}


if __name__ == "__main__":
    base = r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA"
    ifcs = [
        base + r"\thozen-electra\projetos\02 ARQUITETURA\IFC\RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc",
        base + r"\arthen-arboris\IFC-ARBORIS 16.03.26\IFC\CORTAFF_ARB_PEX_ARQ_MODELO FEDERADO_R02_16-03-26.ifc",
        base + r"\placon-arminio-tavares\Arquitetonico\PE01\03_IFC\PLA_ARM_ARQ_EX_IFC_R01.ifc",
    ]
    results = []
    for p in ifcs:
        r = test_ifc(p)
        results.append(r)
    print("\n=== summary ===")
    for r in results:
        print(f"  {r}")
