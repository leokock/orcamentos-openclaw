#!/usr/bin/env python3
r"""discovery_custos.py — Fase 1 (SPEC base-custos-historica).

Dado um caminho de pasta de CUSTO (ex.: ".../<Cliente>/[<Obra>/]04. Custo"),
varre recursivamente e classifica os arquivos relevantes pra extração:

  - workbook_orcamento : xlsx/xls/xlsb que parece ser o orçamento principal
                         (Ger_Executivo / Orçamento / planilha-mãe de itens)
  - composicao         : xlsx/pdf de composições/CPU/insumos
  - relatorio_pdf      : PDFs de relatório (Orçamento.pdf, ABC, Composições) — Tipo C
  - eap                : xlsx de EAP do orçamento
  - cotacao            : xlsx/pdf de cotações de fornecedor
  - outros             : demais arquivos (ignorados por padrão pelo parser)

Para cada arquivo: sha1, tamanho, mtime ISO (BRT, GMT-3), papel, score.
NÃO abre o conteúdo dos arquivos — só metadados de FS + heurística de nome.
O parse pesado fica no parse_custos.py.

Uso CLI:
    python discovery_custos.py "<pasta de custo>"
    python discovery_custos.py "<pasta>" --json    # só o JSON cru

Reúso: pick do maior xlsx inspirado em extract_composicoes.pick_xlsx;
seleção de arquivo-capa inspirada em extrair_dados_entregas.encontrar_arquivo_capa.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path

BRT = timezone(timedelta(hours=-3))

# Extensões que sabemos abrir (xlsb precisa pyxlsb/Excel COM; marcamos mas não abrimos aqui)
WB_EXTS = {".xlsx", ".xls", ".xlsb", ".xlsm"}
PDF_EXTS = {".pdf"}

# Ruído típico de pasta de custo Cartesian/AltoQi — nunca é o orçamento principal
SKIP_NAME_PATTERNS = [
    r"~\$",            # lock file do Office
    r"\.tmp$",
    r"backup",
    r"c[oó]pia de",
    r"copy of",
]

# Subpastas a PODAR (não descer) — descoberta real: "04. Custo" tem ~1467 PDFs de
# projeto/desenho/marcenaria (centenas de MB cada) que NÃO são o orçamento. Descer
# nelas = varrer 17 GB. Cap por nome de diretório (substring, sem acento, lower).
PRUNE_DIR_KW = [
    "projetos",            # 3.6 .../Projetos/R0X/... = perspectivas 3D, plantas
    "perspectiva", "render", "3d",
    "documentacao tecnica", "documentação técnica",
    "marcenaria", "comunicacao visual", "comunicação visual",
    "desenho", "plantas", "imagens", "fotos", "midia", "mídia",
    "antigas", "lixeira", "_old", "obsoleto",
    # Pastas de REFERÊNCIA / OBSOLETO / BACKUP — podem conter o orçamento de OUTRO
    # projeto usado como base (caso Be Brave que pegou CTN-KIR de Kirchner numa
    # subpasta de referência). NUNCA é o orçamento-mãe da pasta corrente.
    "referenc", "referência", "referencia",
    "obsolet", "obsoleto", "obsoletos",
    "backup", "back-up", "back up",
]

# PDF acima disso não é relatório de orçamento (é desenho/perspectiva). O relatório
# AltoQi de TecVerde tem ~poucos MB; os desenhos têm 60-455 MB.
PDF_MAX_MB = 25
# Limite pra sha1 automático no walk: arquivos maiores só recebem sha1 sob demanda
# (picks). Evita hashear 17 GB. O parser/loader rehash os picks selecionados.
SHA1_AUTO_MAX_MB = 30

# Sinais de que o workbook é o orçamento-MÃE (mais alto = mais provável)
ORCAMENTO_NAME_KW = [
    ("orçamento executivo", 60), ("orcamento executivo", 60),
    ("orçamento_executivo", 60), ("orcamento_executivo", 60),
    ("orçamento", 40), ("orcamento", 40),
    ("executivo", 30),
    ("gerencial", 20), ("ger_exec", 25), ("ger executivo", 25),
    ("fechamento", 25),
    ("entregável", 15), ("entregavel", 15),
    ("completo", 10),
]

COMPOSICAO_NAME_KW = ["composi", "cpu", "insumo", "analítico", "analitico"]
EAP_NAME_KW = ["eap"]
COTACAO_NAME_KW = ["cotaç", "cotac", "cotação", "cotacao", "fornecedor", "proposta"]
RELATORIO_NAME_KW = ["relatório", "relatorio", "abc serviços", "abc servicos",
                     "abc insumos", "curva abc"]
# "Apresentação" / "paramétrico" / "emissão" são RESUMOS/slides, não a planilha-mãe
# de itens — penaliza o score pra não vencer o orçamento itemizado (espelha
# processar_executivo.is_executivo, que exclui slides).
APRESENTACAO_PENALTY_KW = ["apresenta", "parametrico", "paramétrico", "emissao",
                           "emissão", "slide", "resumo"]

# Revisão (R00/R01/...) extraída do nome — pra priorizar a última revisão
REV_RE = re.compile(r"\bR(\d{2})\b", re.IGNORECASE)


def _norm(s: str) -> str:
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def sha1_of(path: Path, chunk: int = 1 << 20) -> str:
    """sha1 hex do conteúdo do arquivo (streaming, seguro p/ arquivos grandes)."""
    h = hashlib.sha1()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _mtime_iso(path: Path) -> str:
    try:
        ts = path.stat().st_mtime
        return datetime.fromtimestamp(ts, BRT).isoformat(timespec="seconds")
    except OSError:
        return ""


def _should_skip(name: str) -> bool:
    low = name.lower()
    return any(re.search(p, low) for p in SKIP_NAME_PATTERNS)


def _should_prune_dir(dirname: str) -> bool:
    """True se NÃO devemos descer nesta subpasta (desenhos/perspectivas/cotações antigas)."""
    n = _norm(dirname)
    return any(kw in n for kw in (_norm(x) for x in PRUNE_DIR_KW))


# Keywords de exclusão por CAMINHO (qualquer componente). Diferente do prune por
# nome de dir: aqui defendemos contra pegar orçamento de OUTRO projeto que vive numa
# pasta de Referência/Obsoleto/Backup (caso Be Brave → CTN-KIR de Kirchner). Vale
# mesmo com --no-prune (rglob), onde os dirs não são podados durante a descida.
EXCLUDE_PATH_KW = ["referenc", "obsolet", "backup", "back-up", "back up"]


def _path_excluida(rel_path: str) -> str | None:
    """Se algum componente do caminho relativo bate keyword de exclusão, devolve o
    componente ofensor (motivo); senão None. Não confia em acento (NFKD)."""
    for comp in Path(rel_path).parts:
        n = _norm(comp)
        for kw in EXCLUDE_PATH_KW:
            if _norm(kw) in n:
                return comp
    return None


def _walk_pruned(root: Path):
    """os.walk-like que poda diretórios irrelevantes (evita varrer 17 GB de desenhos)."""
    import os
    for dirpath, dirnames, filenames in os.walk(root):
        # poda in-place (os.walk respeita a edição de dirnames)
        dirnames[:] = [d for d in dirnames if not _should_prune_dir(d)]
        for fn in filenames:
            yield Path(dirpath) / fn


def _revisao(name: str):
    m = REV_RE.search(name)
    return f"R{m.group(1)}" if m else None


def classify_file(path: Path, size_mb: float | None = None) -> dict:
    """Classifica papel + score de um arquivo pelo nome/extensão (sem abrir).

    size_mb: se informado, PDFs grandes (> PDF_MAX_MB) caem pra papel 'outros'
    (são desenhos/perspectivas, não relatório de orçamento)."""
    name = path.name
    low = _norm(name)
    ext = path.suffix.lower()
    rev = _revisao(name)

    # Default
    papel = "outros"
    score = 0

    if ext in WB_EXTS:
        # workbook: pontua por keyword de orçamento, composição, eap, cotação
        orc_score = 0
        for kw, w in ORCAMENTO_NAME_KW:
            if _norm(kw) in low:
                orc_score = max(orc_score, w)
        comp_hit = any(k in low for k in (_norm(x) for x in COMPOSICAO_NAME_KW))
        eap_hit = any(k in low for k in EAP_NAME_KW)
        cot_hit = any(k in low for k in (_norm(x) for x in COTACAO_NAME_KW))

        # Composição/EAP/cotação têm precedência de PAPEL mesmo se contiverem "orçamento"
        if eap_hit and "orcamento" in low:
            papel, score = "eap", 30 + (int(rev[1:]) if rev else 0)
        elif comp_hit and orc_score == 0:
            papel, score = "composicao", 25
        elif cot_hit and orc_score == 0:
            papel, score = "cotacao", 15
        elif orc_score > 0:
            papel = "workbook_orcamento"
            score = orc_score + (int(rev[1:]) if rev else 0)
            # demote apresentação/paramétrico/emissão (são resumos, não a itemizada)
            if any(k in low for k in (_norm(x) for x in APRESENTACAO_PENALTY_KW)):
                score -= 35
        else:
            # workbook sem keyword forte — candidato fraco a orçamento
            papel, score = "workbook_orcamento", 5

    elif ext in PDF_EXTS:
        # PDF grande = desenho/perspectiva, não relatório de orçamento
        if size_mb is not None and size_mb > PDF_MAX_MB:
            return {"papel": "outros", "score": 0, "revisao": rev, "ext": ext,
                    "openable_here": True, "motivo_outros": f"pdf grande {size_mb:.0f}MB"}
        if any(k in low for k in (_norm(x) for x in RELATORIO_NAME_KW)):
            papel, score = "relatorio_pdf", 30
        elif any(k in low for k in (_norm(x) for x in COMPOSICAO_NAME_KW)):
            papel, score = "composicao", 25  # Composições.pdf
        elif "orcamento" in low or "orçamento" in name.lower():
            papel, score = "workbook_orcamento", 35  # Orçamento.pdf (Tipo C)
            score += (int(rev[1:]) if rev else 0)
            # demote paramétrico/emissão/apresentação PDFs (não são o itemizado)
            if any(k in low for k in (_norm(x) for x in APRESENTACAO_PENALTY_KW)):
                score -= 35
        else:
            papel, score = "relatorio_pdf", 10

    return {
        "papel": papel,
        "score": score,
        "revisao": rev,
        "ext": ext,
        "openable_here": ext in {".xlsx", ".xlsm", ".pdf"},  # xls/xlsb precisam engine externo
    }


def discover(folder: str | Path, compute_sha1: bool = True,
             prune: bool = True) -> dict:
    """Varre a pasta de custo e devolve manifesto estruturado.

    prune=True (default): poda subpastas de desenho/perspectiva/cotação-antiga
    (descoberta real: "04. Custo" tem ~1467 PDFs / 17 GB de desenhos não-orçamento).
    compute_sha1=True: sha1 dos arquivos relevantes ATÉ SHA1_AUTO_MAX_MB no walk; os
    picks selecionados sempre recebem sha1 (mesmo grandes) no fim, sob demanda.
    """
    folder = Path(folder)
    out = {
        "folder": str(folder),
        "exists": folder.exists(),
        "scanned_at": datetime.now(BRT).isoformat(timespec="seconds"),
        "pruned": prune,
        "files": [],
        "errors": [],
        "n_skipped_big_pdf": 0,
        "n_excluded_path": 0,
        "excluded_path": [],
    }
    if not folder.exists():
        out["errors"].append("folder not found")
        return out

    walker = _walk_pruned(folder) if prune else (p for p in folder.rglob("*") if p.is_file())
    candidates = []
    try:
        for p in walker:
            if not p.is_file():
                continue
            if _should_skip(p.name):
                continue
            ext = p.suffix.lower()
            if ext not in WB_EXTS and ext not in PDF_EXTS:
                continue
            # excluir arquivos em subpastas de Referência/Obsoleto/Backup — podem ser
            # o orçamento de OUTRO projeto (caso Be Brave → CTN-KIR de Kirchner).
            try:
                rel = str(p.relative_to(folder))
            except ValueError:
                rel = p.name
            ofensor = _path_excluida(rel)
            if ofensor:
                out["n_excluded_path"] += 1
                if len(out["excluded_path"]) < 50:
                    out["excluded_path"].append({"rel": rel, "motivo": ofensor})
                continue
            candidates.append(p)
    except (OSError, PermissionError) as e:
        out["errors"].append(f"walk: {e}")

    for p in candidates:
        try:
            stat = p.stat()
            size_mb = round(stat.st_size / (1 << 20), 2)
            meta = classify_file(p, size_mb=size_mb)
            if meta.get("motivo_outros", "").startswith("pdf grande"):
                out["n_skipped_big_pdf"] += 1
                # mantém no inventário como 'outros' mas sem sha1
            rec = {
                "path": str(p),
                "name": p.name,
                "rel": str(p.relative_to(folder)),
                "size": stat.st_size,
                "size_mb": size_mb,
                "mtime": _mtime_iso(p),
                **meta,
                "sha1": None,
            }
            # sha1 só pra papel relevante e tamanho razoável (evita hashear 17 GB)
            if (compute_sha1 and meta["papel"] != "outros"
                    and size_mb <= SHA1_AUTO_MAX_MB):
                try:
                    rec["sha1"] = sha1_of(p)
                except (OSError, PermissionError) as e:
                    out["errors"].append(f"sha1 {p.name}: {e}")
            out["files"].append(rec)
        except (OSError, PermissionError) as e:
            out["errors"].append(f"stat {p}: {e}")

    # Ordenar por papel-prioridade e score desc
    out["files"].sort(key=lambda r: (-r["score"], -r["size"]))

    # Picks de conveniência pro parser
    out["picks"] = _build_picks(out["files"])
    out["counts"] = _counts(out["files"])

    # Garantir sha1 dos PICKS (mesmo se grandes — só são poucos arquivos)
    if compute_sha1:
        pick_paths = {v for k, v in out["picks"].items()
                      if isinstance(v, str) and v}
        by_path = {f["path"]: f for f in out["files"]}
        for pp in pick_paths:
            f = by_path.get(pp)
            if f and not f["sha1"]:
                try:
                    f["sha1"] = sha1_of(Path(pp))
                except (OSError, PermissionError) as e:
                    out["errors"].append(f"sha1-pick {Path(pp).name}: {e}")

    return out


def _build_picks(files: list[dict]) -> dict:
    """Escolhe os arquivos-alvo principais por papel.

    workbook_orcamento: PARSEÁVEL primeiro (openable_here), depois score, depois size.
    Motivo: um .xlsb/.xls de score maior não serve (sem engine aqui) — pra Tipo C o
    Orçamento.pdf itemizado (openable) deve vencer o Orçamento_R02.xlsb.
    """
    def best(role, openable_first=False):
        cands = [f for f in files if f["papel"] == role]
        if not cands:
            return None
        if openable_first:
            cands.sort(key=lambda f: (0 if f["openable_here"] else 1, -f["score"], -f["size"]))
        else:
            cands.sort(key=lambda f: (-f["score"], 0 if f["openable_here"] else 1, -f["size"]))
        return cands[0]["path"]

    # Guardar também o melhor por score sem o filtro de openable (rastreio/auditoria:
    # ex. o .xlsb é a fonte editável real, registrado mesmo sem parser aqui).
    def best_any(role):
        cands = [f for f in files if f["papel"] == role]
        if not cands:
            return None
        cands.sort(key=lambda f: (-f["score"], -f["size"]))
        return cands[0]["path"]

    picks = {
        "workbook_orcamento": best("workbook_orcamento", openable_first=True),
        "workbook_orcamento_top_score": best_any("workbook_orcamento"),
        "composicao": best("composicao", openable_first=True),
        "eap": best("eap", openable_first=True),
        "relatorio_pdf": best("relatorio_pdf"),
        "cotacao": best("cotacao", openable_first=True),
    }
    # Lista completa de composições (pode haver várias)
    picks["composicao_all"] = [f["path"] for f in files if f["papel"] == "composicao"]
    picks["relatorio_pdf_all"] = [f["path"] for f in files if f["papel"] == "relatorio_pdf"]
    return picks


def _counts(files: list[dict]) -> dict:
    c = {}
    for f in files:
        c[f["papel"]] = c.get(f["papel"], 0) + 1
    return c


def main():
    ap = argparse.ArgumentParser(description="Discovery de arquivos de custo (Fase 1)")
    ap.add_argument("folder", help="caminho da pasta de custo")
    ap.add_argument("--no-sha1", action="store_true", help="pular cálculo de sha1")
    ap.add_argument("--no-prune", action="store_true",
                    help="NÃO podar subpastas de desenho (varre tudo; lento em 04. Custo)")
    ap.add_argument("--json", action="store_true", help="imprimir só o JSON")
    args = ap.parse_args()

    result = discover(args.folder, compute_sha1=not args.no_sha1, prune=not args.no_prune)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Pasta: {result['folder']}")
    print(f"Existe: {result['exists']}  | arquivos relevantes: {len(result['files'])}"
          f"  | PDFs grandes pulados: {result.get('n_skipped_big_pdf', 0)}  | pruned: {result.get('pruned')}")
    print(f"Contagem por papel: {result['counts']}")
    if result["errors"]:
        print(f"Erros: {result['errors']}")
    print("\nPicks:")
    for k, v in result["picks"].items():
        if k.endswith("_all"):
            continue
        print(f"  {k:<20} {Path(v).name if v else '—'}")
    print("\nArquivos (ordenados por score):")
    for f in result["files"][:30]:
        print(f"  [{f['papel']:<18} s={f['score']:>3}] {f['name']}  "
              f"({f['size_mb']}MB, {f['mtime']}, sha1={str(f['sha1'])[:10]})")


if __name__ == "__main__":
    main()
