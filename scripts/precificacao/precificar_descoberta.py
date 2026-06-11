"""Descobre candidatos a projeto-referência pra precificação 3-fontes.

Escaneia pastas conhecidas em busca de planilhas xlsx com coluna PREÇO/CUSTO UNITÁRIO
e devolve um JSON pro bot apresentar candidatos ao usuário no Slack.

Locais escaneados:
  1. `projetos/[qualquer]/Arquivos recebidos/.../Quantitativos fornecidos/` — planilhas
     do cliente atual (caso o cliente tenha mandado planilha precificada).
  2. `executivos/entregues/` — orçamentos executivos já entregues (preços validados).
  3. `executivos/*-claude/` — análises Claude com 04-precificacao já feita.

Pra cada xlsx encontrada, retorna:
  - path
  - tamanho
  - aba candidata (PREÇO/Preço/Custo Unitário)
  - count de linhas precificadas
  - heurística de match (slug-projeto extraído do path)
  - data de modificação

Output: JSON em stdout (1 dict com lista candidatos).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import openpyxl

from precificar_common import WORKSPACE_ROOT


SHEET_KEYWORDS = ("preç", "preco", "custo unit", "valor unit", "unit price", "pus")
HEADER_KEYWORDS_DESC = ("descri", "item", "material", "insumo")
HEADER_KEYWORDS_PRICE = ("preç", "preco", "custo unit", "valor unit")

SEARCH_ROOTS = [
    WORKSPACE_ROOT / "executivos" / "entregues",
    WORKSPACE_ROOT / "projetos",
]
# Drive CTN — escaneamento raso de "Arquivos recebidos" por cliente
import os as _os
_CTN_DEFAULT = r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento"
CTN_DRIVE_ROOT = Path(_os.environ.get("CARTESIAN_CTN_ROOT", _CTN_DEFAULT))
# Também procuramos executivos/*-claude/0X-precificacao* (referências validadas)
EXEC_CLAUDE_GLOBS = [
    "executivos/*-claude/0?-precificacao*",
]


def _has_price_sheet(xlsx: Path):
    """Retorna (sheet_name, n_priced_rows) se a planilha tem coluna preço; senão (None, 0)."""
    try:
        wb = openpyxl.load_workbook(xlsx, data_only=True, read_only=True)
    except Exception:
        return None, 0

    best_sheet = None
    best_n = 0
    for sn in wb.sheetnames:
        if not any(k in sn.lower() for k in SHEET_KEYWORDS):
            continue
        try:
            ws = wb[sn]
        except Exception:
            continue
        # search header in first 15 rows
        header_row = None
        price_col = None
        desc_col = None
        for ridx, row in enumerate(ws.iter_rows(min_row=1, max_row=15, values_only=True), start=1):
            row_l = [str(c or "").lower() for c in row]
            for cidx, cell in enumerate(row_l):
                if any(k in cell for k in HEADER_KEYWORDS_PRICE):
                    price_col = cidx
                if any(k in cell for k in HEADER_KEYWORDS_DESC):
                    desc_col = cidx
            if price_col is not None and desc_col is not None:
                header_row = ridx
                break
        if header_row is None or price_col is None:
            continue
        # count priced rows
        n = 0
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            if price_col >= len(row):
                continue
            try:
                v = row[price_col]
                if v is None:
                    continue
                f = float(v)
                if f > 0:
                    n += 1
            except (ValueError, TypeError):
                continue
        if n > best_n:
            best_n = n
            best_sheet = sn
    wb.close()
    return best_sheet, best_n


def _scan_dir(root: Path, max_depth=6, max_results=50):
    out = []
    if not root.exists():
        return out
    for xlsx in root.rglob("*.xlsx"):
        # skip ~$lockfiles e _tmp
        if xlsx.name.startswith("~$") or "_tmp" in xlsx.parts:
            continue
        # depth limit
        try:
            rel_depth = len(xlsx.relative_to(root).parts)
        except ValueError:
            rel_depth = 99
        if rel_depth > max_depth:
            continue
        sheet, n = _has_price_sheet(xlsx)
        if sheet and n >= 10:
            out.append({
                "path": str(xlsx),
                "sheet": sheet,
                "priced_rows": n,
                "size_bytes": xlsx.stat().st_size,
                "mtime": int(xlsx.stat().st_mtime),
                "rel_dir": str(xlsx.parent.relative_to(WORKSPACE_ROOT)) if xlsx.is_relative_to(WORKSPACE_ROOT) else str(xlsx.parent),
            })
        if len(out) >= max_results:
            break
    return out


def _extract_label(path_str: str) -> str:
    """Heurística pra rotular candidato pelo path (Aquos, Malta, etc)."""
    parts = Path(path_str).parts
    # caminhos típicos: .../Cliente/.../arquivo.xlsx ou executivos/<slug>/...
    for p in parts:
        low = p.lower()
        if "aquos" in low or "blue haven" in low or "blh" in low:
            return "Aquos (Blue Haven)"
        if "malta" in low or "mta" in low:
            return "Malta"
        if "atlantia" in low:
            return "Atlantia"
        if "alfa" in low and "colinas" in low:
            return "Alfa Colinas"
    # Fallback: pega o nome do arquivo
    return Path(path_str).stem[:40]


def discover(client_filter: str | None = None, max_results: int = 30,
             scan_drive: bool = True, max_depth_drive: int = 6) -> dict:
    """Retorna dict com `candidates`: lista de candidatos a projeto-referência."""
    all_cands = []
    for root in SEARCH_ROOTS:
        all_cands.extend(_scan_dir(root))
    # também escanear executivos/*-claude/0X-precificacao/
    for glob_pat in EXEC_CLAUDE_GLOBS:
        for d in WORKSPACE_ROOT.glob(glob_pat):
            all_cands.extend(_scan_dir(d))
    # Drive CTN — opt-in, limita depth e filtra por cliente cedo pra não estourar
    if scan_drive and CTN_DRIVE_ROOT.exists():
        if client_filter:
            # tenta achar pasta-mãe do cliente direto: '<Cliente>/Arquivos recebidos/'
            for child in CTN_DRIVE_ROOT.iterdir():
                if child.is_dir() and client_filter.lower() in child.name.lower():
                    recebidos = child / "Arquivos recebidos"
                    if recebidos.exists():
                        all_cands.extend(_scan_dir(recebidos, max_depth=max_depth_drive))
        else:
            # sem filtro: escaneia raso o Drive (lento — só sob demanda)
            all_cands.extend(_scan_dir(CTN_DRIVE_ROOT, max_depth=4, max_results=200))

    # dedupe por path
    seen = set()
    unique = []
    for c in all_cands:
        if c["path"] in seen:
            continue
        seen.add(c["path"])
        c["label"] = _extract_label(c["path"])
        unique.append(c)

    # filtro por cliente (se passado)
    if client_filter:
        cf = client_filter.lower()
        unique = [c for c in unique if cf in c["path"].lower() or cf in c["label"].lower()]

    # ordena: prioriza priced_rows desc, depois mtime desc
    unique.sort(key=lambda c: (-c["priced_rows"], -c["mtime"]))

    return {
        "scanned_at": int(time.time()),
        "n_total": len(unique),
        "candidates": unique[:max_results],
    }


def main():
    ap = argparse.ArgumentParser(description="Descobre candidatos a projeto-referência")
    ap.add_argument("--client", help="Filtra por substring no path/label")
    ap.add_argument("--max", type=int, default=30)
    ap.add_argument("--pretty", action="store_true", help="Imprime pretty-print pro bot")
    args = ap.parse_args()
    res = discover(args.client, args.max)
    if args.pretty:
        print(f"Encontrados {res['n_total']} candidatos:\n")
        for i, c in enumerate(res["candidates"], 1):
            print(f"{i:2d}. {c['label']}")
            print(f"    {c['priced_rows']} itens precificados em '{c['sheet']}'")
            print(f"    {c['rel_dir']}/{Path(c['path']).name}")
            print()
    else:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
