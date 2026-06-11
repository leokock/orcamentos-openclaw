#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""enumerar_pastas_custo.py — PASSO 1 do lote (SPEC base-custos-historica).

Enumera SO a pasta de custo de TOPO por projeto sob a pasta-mae Cartesian:

    G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento

Bug anterior (corrigido aqui): recursar dentro de "04. Custo" e pegar as
subpastas "03.X Custo - ..." como se fossem pastas de projeto -> centenas de
falsos positivos. AQUI: pegamos o diretorio filho IMEDIATO cujo nome casa o
regex (?i)^0[34][. ]+custo$ (ex.: "04. Custo", "03. Custo") e NAO descemos
dentro dele. Da ~50-53 pastas, nao centenas.

Estrutura real do Drive:
    Projetos em Andamento/
      <Cliente>/
        04. Custo/                 <- pega esta (cliente sem obra)
        <Obra>/
          04. Custo/               <- ou esta (cliente com obras)

Logica:
  - Para cada <Cliente> (1o nivel sob a pasta-mae):
      * se <Cliente> tem filho imediato que casa CUSTO_RE -> emite (cliente,)
      * para cada <Obra> (filho imediato de <Cliente> que NAO e pasta de custo):
          - se <Obra> tem filho imediato que casa CUSTO_RE -> emite (cliente, obra)
  - 1 nivel de obra (nao desce mais fundo procurando custo).
  - Profundidade maxima de busca da pasta de custo: cliente OU cliente/obra.

slug = cliente[-obra] normalizado (NFKD, lower, dashes) — mesma convencao do
run_selftest._slug_from_folder.

Exclui slugs ja carregados (onda 1):
    cincatarina, gdi-santa-monica, tecverde-casa-c4e, sunprime,
    solis-empreendimentos, essege, holze-construtora-e-incorporadora-nouve,
    soles-empreendimentos

Uso:
    py -3.10 scripts/custos_historica/enumerar_pastas_custo.py
    py -3.10 scripts/custos_historica/enumerar_pastas_custo.py --json
    py -3.10 scripts/custos_historica/enumerar_pastas_custo.py --include-excluded
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento")

# Pasta de custo de TOPO: "04. Custo", "03. Custo", "04 Custo", "03  Custo".
# NAO casa subpastas "03.1 Custo - Estrutura" (tem digito depois do 03/04).
CUSTO_RE = re.compile(r"(?i)^0[34][.\s]+custo$")

# Slugs ja carregados (onda 1) — excluir.
JA_CARREGADOS = {
    "cincatarina",
    "gdi-santa-monica",
    "tecverde-casa-c4e",
    "sunprime",
    "solis-empreendimentos",
    "essege",
    "holze-construtora-e-incorporadora-nouve",
    "soles-empreendimentos",
}

# Nomes de 1o-nivel que nao sao cliente (atalhos, planilhas, exports soltos).
SKIP_TOPLEVEL_EXT = {".lnk", ".gsheet", ".gslides", ".gdoc", ".rvt", ".xlsx",
                     ".xls", ".pdf", ".url"}

# Pastas-cliente que NAO sao projeto real (templates, exports administrativos).
SKIP_CLIENTE_KW = ["_template", "template de pastas", "00 - exporta", "exportacao_monday"]

# Extensoes que contam como "tem conteudo de orcamento" no probe rapido.
CONTENT_EXTS = {".xlsx", ".xls", ".xlsb", ".xlsm", ".pdf"}

# Subpastas ignoradas no probe (ruido — desenhos/perspectivas/referencias).
# Espelha discovery_custos.PRUNE_DIR_KW de forma enxuta (probe e' raso).
PROBE_PRUNE_KW = ["referenc", "obsolet", "backup", "projetos", "perspectiva",
                  "render", "3d", "marcenaria", "desenho", "plantas", "imagens",
                  "fotos", "midia", "comunicacao visual", "documentacao tecnica"]


def slugify(parts: list[str]) -> str:
    s = "-".join(p for p in parts if p)
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "projeto"


def _is_custo_topo(child: Path) -> bool:
    try:
        return child.is_dir() and bool(CUSTO_RE.match(child.name))
    except OSError:
        return False


def _custo_child(folder: Path) -> Path | None:
    """Retorna o filho imediato que casa CUSTO_RE, ou None. NAO recursa."""
    try:
        for child in folder.iterdir():
            if _is_custo_topo(child):
                return child
    except (OSError, PermissionError):
        return None
    return None


def _norm(s: str) -> str:
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _probe_conteudo(custo_folder: Path, max_dirs: int = 400) -> tuple[bool, int]:
    """Probe RASO/rapido: a pasta de custo tem algum arquivo de orcamento
    (xlsx/xls/pdf) fora de subpastas-ruido? Retorna (tem_conteudo, n_arquivos).

    NAO e' o discovery completo — so' decide se vale a pena mandar pro driver
    (o driver roda discovery+parse de verdade). Poda subpastas de ruido pra
    nao varrer GB de desenhos. Cap de diretorios visitados pra nao travar.
    """
    n = 0
    dirs_visited = 0
    stack = [custo_folder]
    while stack and dirs_visited < max_dirs:
        d = stack.pop()
        dirs_visited += 1
        try:
            with os.scandir(d) as it:
                for entry in it:
                    try:
                        if entry.is_dir():
                            nm = _norm(entry.name)
                            if any(kw in nm for kw in PROBE_PRUNE_KW):
                                continue
                            stack.append(Path(entry.path))
                        elif entry.is_file():
                            ext = Path(entry.name).suffix.lower()
                            if ext in CONTENT_EXTS and not entry.name.startswith("~$"):
                                n += 1
                                if n >= 1:
                                    # achou pelo menos 1 — basta pra "tem conteudo".
                                    # continua contando barato so' no nivel atual; mas
                                    # pra rapidez, retornamos cedo se ja' temos sinal.
                                    return True, n
                    except OSError:
                        continue
        except (OSError, PermissionError):
            continue
    return (n > 0), n


def _subdirs(folder: Path) -> list[Path]:
    out = []
    try:
        for child in folder.iterdir():
            try:
                if child.is_dir():
                    out.append(child)
            except OSError:
                continue
    except (OSError, PermissionError):
        return []
    return out


def enumerar(root: Path = ROOT) -> dict:
    out = {
        "root": str(root),
        "exists": root.exists(),
        "pastas": [],          # entradas COM conteudo (vao pro driver)
        "vazias": [],          # casaram regex mas sem arquivo de orcamento (skip rapido)
        "excluidas_ja_carregadas": [],
        "erros": [],
    }
    if not root.exists():
        out["erros"].append(f"root nao existe: {root}")
        return out

    for cliente_dir in sorted(_subdirs(root), key=lambda p: p.name.lower()):
        # pular pseudo-clientes (atalhos/arquivos disfarcados de dir nao chegam
        # aqui pois _subdirs ja filtra is_dir; mas .lnk pode ser dir-junction)
        if cliente_dir.suffix.lower() in SKIP_TOPLEVEL_EXT:
            continue

        cliente = cliente_dir.name
        nm_cliente = _norm(cliente)
        if any(kw in nm_cliente for kw in (_norm(x) for x in SKIP_CLIENTE_KW)):
            continue

        # (a) custo direto no cliente (cliente sem obra)
        custo_no_cliente = _custo_child(cliente_dir)
        emitiu_cliente = False
        if custo_no_cliente is not None:
            _emit(out, [cliente], custo_no_cliente)
            emitiu_cliente = True

        # (b) custo dentro de cada obra (1 nivel). Sempre varremos obras mesmo
        #     se o cliente ja teve custo direto (cliente pode ter custo-geral +
        #     obras com custo proprio — emitimos ambos, slugs distintos).
        for obra_dir in sorted(_subdirs(cliente_dir), key=lambda p: p.name.lower()):
            if _is_custo_topo(obra_dir):
                continue  # ja tratado em (a)
            custo_na_obra = _custo_child(obra_dir)
            if custo_na_obra is not None:
                _emit(out, [cliente, obra_dir.name], custo_na_obra)

    out["n_pastas"] = len(out["pastas"])
    out["n_vazias"] = len(out["vazias"])
    out["n_excluidas"] = len(out["excluidas_ja_carregadas"])
    return out


def _emit(out: dict, parts: list[str], custo_folder: Path) -> None:
    slug = slugify(parts)
    rec = {
        "slug": slug,
        "cliente": parts[0],
        "obra": parts[1] if len(parts) > 1 else None,
        "folder": str(custo_folder),
    }
    if slug in JA_CARREGADOS:
        out["excluidas_ja_carregadas"].append(rec)
        return
    tem_conteudo, n_arq = _probe_conteudo(custo_folder)
    rec["n_arquivos_probe"] = n_arq
    if not tem_conteudo:
        out["vazias"].append(rec)
        return
    out["pastas"].append(rec)


def main() -> int:
    ap = argparse.ArgumentParser(description="Enumera pastas de custo de TOPO (PASSO 1).")
    ap.add_argument("--json", action="store_true", help="imprime so o JSON")
    ap.add_argument("--include-excluded", action="store_true",
                    help="inclui no JSON tambem as ja-carregadas")
    ap.add_argument("--root", default=str(ROOT))
    args = ap.parse_args()

    result = enumerar(Path(args.root))

    if args.json:
        if not args.include_excluded:
            result = {k: v for k, v in result.items() if k != "excluidas_ja_carregadas"}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"Root: {result['root']}  (existe={result['exists']})")
    print(f"Pastas de custo COM conteudo (novas, vao pro driver): {result.get('n_pastas', 0)}")
    print(f"Pastas que casaram regex mas VAZIAS (skip):           {result.get('n_vazias', 0)}")
    print(f"Excluidas (ja carregadas onda 1):                     {result.get('n_excluidas', 0)}")
    if result["erros"]:
        print(f"Erros: {result['erros']}")
    print()
    for rec in result["pastas"]:
        obra = f" / {rec['obra']}" if rec["obra"] else ""
        print(f"  [{rec['slug']:<42}] {rec['cliente']}{obra}")
    if result["excluidas_ja_carregadas"]:
        print("\n  --- excluidas (onda 1) ---")
        for rec in result["excluidas_ja_carregadas"]:
            print(f"  [{rec['slug']:<42}] (skip)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
