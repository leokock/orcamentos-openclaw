#!/usr/bin/env python3
"""Bloco 0 — Análise arquitetônica multi-camada de um projeto.

Para cada projeto, varre a pasta no Drive procurando indícios de espaços de
lazer e equipamentos especiais (piscina, academia, salão, gourmet, etc.).

Estratégia em 4 camadas (todas rodam em sequência, agregam resultados):

1. **IFC via ifcopenshell** (camada principal)
   - IfcSpace.LongName/Name → keywords lazer
   - Fallback: IfcBuildingStorey.Name pra detectar "LAZER" pavimento

2. **DXF via ezdxf** (complemento)
   - Entidades TEXT/MTEXT → keywords lazer

3. **PDF via pypdf** (fallback rico)
   - Memoriais, apresentações, quadros NBR

4. **Nomes de arquivo** (último recurso)
   - Regex em nomes de DWG/IFC/PDF

Saída: `base/pacotes/{slug}/analise-arquitetura.json`

Uso:
    python analise_arquitetura.py --slug thozen-electra \\
        --pasta "G:\\...\\thozen-electra"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import traceback
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    import ifcopenshell
    HAVE_IFC = True
except ImportError:
    HAVE_IFC = False

try:
    import ezdxf
    HAVE_DXF = True
except ImportError:
    HAVE_DXF = False

try:
    from pypdf import PdfReader
    HAVE_PDF = True
except ImportError:
    HAVE_PDF = False


BASE = Path.home() / "orcamentos-openclaw" / "base"
PACOTES = BASE / "pacotes"


# ---------------------------------------------------------------- KEYWORDS ---

LAZER_CATEGORIES = {
    "piscina": ["piscina", "swimming pool", "pool club", "kids pool"],
    "piscina_aquecida": ["piscina aquecida", "piscina climatizada", "heated pool"],
    "ofuro_spa": ["ofurô", "ofuro", "jacuzzi", " spa", "spa interno", "beauty spa"],
    "sauna": ["sauna", "vapor", "steam"],
    "academia": ["academia", "fitness", "musculação", "musculacao", "gym"],
    "quadra": ["quadra esportiva", "mini quadra", "quadra de tênis", "quadra poliesportiva", "squash"],
    "salao_festas": ["salão de festas", "salao de festas", "salão festas", "salão social"],
    "salao_gourmet": ["salão gourmet", "salao gourmet", "gourmet room", "gourmet club", "espaço gourmet", "área gourmet", "gourmet"],
    "churrasqueira": ["churrasqueira", "churrasco", "bbq", "fire place", "fire pit", "espaço grill"],
    "playground": ["playground", "parquinho"],
    "brinquedoteca": ["brinquedoteca", "kids room", "kids place"],
    "kids": ["kids ", "fraldário", "fraldario"],
    "coworking": ["coworking", "co-working", "home office", "sala de reunião", "sala de reuniao"],
    "lavanderia": ["lavanderia coletiva", "laundromat"],
    "pet": ["pet place", "pet care", "petcare", "pet shop", "praça pet", "praca pet"],
    "bicicletario": ["bicicletário", "bicicletario", "bike room"],
    "lounge_pub": ["lounge", " pub ", "wine bar", "lobby bar"],
    "gerador": ["gerador", "grupo gerador", "gmg"],
    "elevador": ["elevador social", "elevador de serviço", "elevador de servico"],
    "lazer_generico": ["área de lazer", "area de lazer", "espaço lazer", "rooftop lazer", "terraço lazer"],
}

# Build flat list for fast scanning
ALL_KEYWORDS: dict[str, str] = {}  # keyword -> category
for cat, kws in LAZER_CATEGORIES.items():
    for kw in kws:
        ALL_KEYWORDS[kw.lower()] = cat


def _scan_text(text: str) -> list[tuple[str, str, str]]:
    """Returns list of (category, keyword, snippet) hits in text."""
    if not text:
        return []
    hits = []
    text_lower = text.lower()
    for kw, cat in ALL_KEYWORDS.items():
        idx = 0
        while True:
            pos = text_lower.find(kw, idx)
            if pos < 0:
                break
            start = max(0, pos - 30)
            end = min(len(text), pos + len(kw) + 30)
            snippet = text[start:end].replace("\n", " ").strip()
            hits.append((cat, kw, snippet))
            idx = pos + len(kw)
    return hits


# ------------------------------------------------------------------ LAYERS ---

def layer_ifc(folder: Path, log: list) -> dict:
    """Camada 1 — IFC via ifcopenshell."""
    out: dict = {"layer": "ifc", "files_read": [], "hits": [], "storeys": [], "errors": []}
    if not HAVE_IFC:
        out["errors"].append("ifcopenshell não disponível")
        return out

    ifc_files = []
    for f in folder.rglob("*.ifc"):
        sf = str(f).lower()
        if "obsoleto" in sf or "antigo" in sf or "backup" in sf:
            continue
        ifc_files.append(f)

    log.append(f"  [ifc] {len(ifc_files)} arquivos IFC válidos (sem OBSOLETOS)")

    for ifc_path in ifc_files[:6]:
        try:
            t0 = time.time()
            f = ifcopenshell.open(str(ifc_path))
            out["files_read"].append({
                "file": ifc_path.name,
                "schema": f.schema,
                "duration": round(time.time() - t0, 1),
            })

            spaces = f.by_type("IfcSpace")
            for s in spaces:
                name = ((s.Name or "") + " " + (s.LongName or "")).strip()
                if not name:
                    continue
                hits = _scan_text(name)
                for cat, kw, _snip in hits:
                    out["hits"].append({
                        "category": cat,
                        "keyword": kw,
                        "source": f"IFC IfcSpace: {ifc_path.name}",
                        "name": name[:120],
                    })

            stories = f.by_type("IfcBuildingStorey")
            for st in stories:
                sname = (st.Name or "").strip()
                if not sname:
                    continue
                if sname not in out["storeys"]:
                    out["storeys"].append(sname)
                hits = _scan_text(sname)
                for cat, kw, _snip in hits:
                    out["hits"].append({
                        "category": cat,
                        "keyword": kw,
                        "source": f"IFC IfcBuildingStorey: {ifc_path.name}",
                        "name": sname[:80],
                    })
            log.append(f"    OK {ifc_path.name} ({len(spaces)} spaces, {len(stories)} storeys)")
        except Exception as e:
            log.append(f"    ERR {ifc_path.name}: {type(e).__name__}: {str(e)[:80]}")
            out["errors"].append(f"{ifc_path.name}: {type(e).__name__}: {e}")

    return out


def layer_dxf(folder: Path, log: list) -> dict:
    """Camada 2 — DXF via ezdxf."""
    out: dict = {"layer": "dxf", "files_read": [], "hits": [], "errors": []}
    if not HAVE_DXF:
        out["errors"].append("ezdxf não disponível")
        return out

    dxf_files = []
    for f in folder.rglob("*.dxf"):
        sf = str(f).lower()
        if "obsoleto" in sf or "antigo" in sf or "backup" in sf:
            continue
        dxf_files.append(f)

    log.append(f"  [dxf] {len(dxf_files)} arquivos DXF")

    for dxf_path in dxf_files[:30]:
        try:
            t0 = time.time()
            doc = ezdxf.readfile(str(dxf_path))
            msp = doc.modelspace()
            file_hits = 0
            for e in msp:
                etype = e.dxftype()
                if etype == "TEXT":
                    text = e.dxf.get("text", "")
                elif etype == "MTEXT":
                    text = getattr(e, "text", "") or ""
                else:
                    continue
                text = str(text).strip()
                if not text:
                    continue
                hits = _scan_text(text)
                for cat, kw, _snip in hits:
                    out["hits"].append({
                        "category": cat,
                        "keyword": kw,
                        "source": f"DXF: {dxf_path.name}",
                        "name": text[:120],
                    })
                    file_hits += 1
            out["files_read"].append({"file": dxf_path.name, "duration": round(time.time() - t0, 1), "hits": file_hits})
            log.append(f"    OK {dxf_path.name} ({file_hits} hits)")
        except Exception as e:
            log.append(f"    ERR {dxf_path.name}: {type(e).__name__}: {str(e)[:80]}")
            out["errors"].append(f"{dxf_path.name}: {type(e).__name__}: {e}")

    return out


def layer_pdf(folder: Path, log: list) -> dict:
    """Camada 3 — PDF via pypdf (memoriais, apresentações, quadros NBR)."""
    out: dict = {"layer": "pdf", "files_read": [], "hits": [], "errors": []}
    if not HAVE_PDF:
        out["errors"].append("pypdf não disponível")
        return out

    pdf_files = []
    relevant_keywords = ["memorial", "apresenta", "lazer", "implanta", "compatibili"]
    nbr_blacklist = ["quadro i_", "quadro ii_", "quadro iii_", "quadro iv", "quadro v_",
                     "quadro va_", "quadro vi_", "quadro vii_", "quadro viii_",
                     "informações preliminares", "informacoes preliminares"]
    for f in folder.rglob("*.pdf"):
        sf = str(f).lower()
        if "obsoleto" in sf or "antigo" in sf or "backup" in sf:
            continue
        if any(b in sf for b in nbr_blacklist):
            continue
        if not any(k in sf for k in relevant_keywords):
            continue
        pdf_files.append(f)

    log.append(f"  [pdf] {len(pdf_files)} PDFs relevantes")

    for pdf_path in pdf_files[:25]:
        try:
            t0 = time.time()
            r = PdfReader(str(pdf_path))
            file_hits = 0
            for pg_idx, pg in enumerate(r.pages[:20]):
                t = pg.extract_text() or ""
                if not t.strip():
                    continue
                hits = _scan_text(t)
                for cat, kw, snip in hits:
                    out["hits"].append({
                        "category": cat,
                        "keyword": kw,
                        "source": f"PDF: {pdf_path.name} p{pg_idx + 1}",
                        "name": snip[:120],
                    })
                    file_hits += 1
            out["files_read"].append({"file": pdf_path.name, "duration": round(time.time() - t0, 1), "hits": file_hits})
            log.append(f"    OK {pdf_path.name} ({file_hits} hits)")
        except Exception as e:
            log.append(f"    ERR {pdf_path.name}: {type(e).__name__}: {str(e)[:60]}")
            out["errors"].append(f"{pdf_path.name}: {type(e).__name__}: {e}")

    return out


def layer_filenames(folder: Path, log: list) -> dict:
    """Camada 4 — Nomes de arquivo (DWG/IFC/PDF)."""
    out: dict = {"layer": "filename", "hits": []}
    extensions = {".dwg", ".ifc", ".pdf", ".dxf", ".rvt"}

    for f in folder.rglob("*"):
        if f.suffix.lower() not in extensions:
            continue
        sf = str(f).lower()
        if "obsoleto" in sf or "antigo" in sf or "backup" in sf:
            continue
        name = f.name
        hits = _scan_text(name)
        for cat, kw, _snip in hits:
            out["hits"].append({
                "category": cat,
                "keyword": kw,
                "source": f"filename: {f.parent.name}/{name}",
                "name": name,
            })

    log.append(f"  [filename] {len(out['hits'])} hits em nomes de arquivo")
    return out


# ----------------------------------------------------------------- ANALYSIS ---

def consolidate(layers: list[dict]) -> dict:
    """Consolida hits de todas as camadas por categoria."""
    by_cat: dict[str, dict] = defaultdict(lambda: {
        "category": "",
        "count": 0,
        "sources": [],
        "samples": [],
    })

    for layer in layers:
        for hit in layer.get("hits", []):
            cat = hit["category"]
            entry = by_cat[cat]
            entry["category"] = cat
            entry["count"] += 1
            src = hit.get("source", "")
            if src not in entry["sources"]:
                entry["sources"].append(src)
            sample = f"[{hit.get('keyword')}] {hit.get('name', '')[:80]}"
            if sample not in entry["samples"]:
                entry["samples"].append(sample)

    return {cat: dict(info) for cat, info in by_cat.items()}


def gerar_decisoes(consolidado: dict) -> dict:
    """Mapeia categorias detectadas em decisões binárias do gate."""
    return {
        "tem_piscina": "piscina" in consolidado or "piscina_aquecida" in consolidado,
        "piscina_aquecida": "piscina_aquecida" in consolidado,
        "tem_ofuro_spa": "ofuro_spa" in consolidado,
        "tem_sauna": "sauna" in consolidado,
        "tem_academia": "academia" in consolidado,
        "tem_quadra": "quadra" in consolidado,
        "tem_salao_festas": "salao_festas" in consolidado,
        "tem_gourmet": "salao_gourmet" in consolidado,
        "tem_churrasqueira": "churrasqueira" in consolidado,
        "tem_playground": "playground" in consolidado or "brinquedoteca" in consolidado or "kids" in consolidado,
        "tem_coworking": "coworking" in consolidado,
        "tem_pet": "pet" in consolidado,
        "tem_bicicletario": "bicicletario" in consolidado,
        "tem_gerador_dedicado": "gerador" in consolidado,
        "lazer_generico_mencionado": "lazer_generico" in consolidado,
    }


def analisar(slug: str, pasta: Path) -> dict:
    inicio = time.time()
    log: list[str] = [f"\n=== Análise arquitetônica: {slug} ==="]
    log.append(f"  pasta: {pasta}")
    log.append(f"  pasta existe: {pasta.exists()}")

    if not pasta.exists():
        return {
            "projeto": slug,
            "pasta": str(pasta),
            "ts": datetime.now().isoformat(timespec="seconds"),
            "erro": "pasta não encontrada",
            "log": log,
        }

    layers = []
    layers.append(layer_ifc(pasta, log))
    layers.append(layer_dxf(pasta, log))
    layers.append(layer_pdf(pasta, log))
    layers.append(layer_filenames(pasta, log))

    consolidado = consolidate(layers)
    decisoes = gerar_decisoes(consolidado)

    duracao = round(time.time() - inicio, 1)
    log.append(f"\n  → {len(consolidado)} categorias detectadas em {duracao}s")

    return {
        "projeto": slug,
        "pasta": str(pasta),
        "ts": datetime.now().isoformat(timespec="seconds"),
        "duracao_s": duracao,
        "categorias_detectadas": consolidado,
        "decisoes_inferidas": decisoes,
        "layers": [{"layer": L["layer"],
                    "files_read": len(L.get("files_read", [])),
                    "hits": len(L.get("hits", [])),
                    "errors": len(L.get("errors", []))}
                   for L in layers],
        "log": log,
        "_layers_full": layers,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--pasta", required=True)
    ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()

    pasta = Path(args.pasta)
    result = analisar(args.slug, pasta)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = PACOTES / args.slug / "analise-arquitetura.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n".join(result["log"]))
    print(f"\nDecisões inferidas:")
    for k, v in result["decisoes_inferidas"].items():
        marker = "✓" if v else "—"
        print(f"  {marker} {k}: {v}")
    print(f"\nSaída: {out_path}")


if __name__ == "__main__":
    main()
