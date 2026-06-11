#!/usr/bin/env python3
r"""resolve_data_preco.py — Fase 1 (SPEC base-custos-historica §5 hierarquia da data do preço).

Resolve a DATA-BASE do preço de um workbook/PDF, com origem e confiança.

Hierarquia (maior confiança primeiro), grava a origem:
  (1) célula "data base" no xlsx/PDF            [alta]
  (2) mês CUB (data do CUB de referência)        [alta]
  (3) data no nome da pasta "06.2022" via regex  [média]
  (4) revisão R00/R01 ordena safras              [média/baixa] -> só informativa, NÃO data sozinha
  (5) mtime do arquivo                           [baixa]

Regras: dia=01; rejeita datas no futuro e anteriores a 2015.

Este módulo é determinístico (Python). A desambiguação Claude (quando a hierarquia
empata de verdade) acontece na fase real — aqui devolvemos os candidatos coletados
em `candidatos[]` + a escolha + a flag `ambiguo` pra Claude resolver depois.

API principal:
    resolve_data_preco(texto_capa=None, folder_path=None, file_name=None,
                       file_mtime_iso=None, celula_data_base=None, cub_mes=None,
                       cub_valor=None) -> dict

Retorno:
    {
      "data_base": "YYYY-MM-DD" | None,
      "origem": "celula_data_base|cub_mes|nome_pasta|revisao|mtime|None",
      "confianca": "alta|media|baixa|nenhuma",
      "ambiguo": bool,
      "candidatos": [ {origem, data, confianca, raw} ... ],
      "vintage": "YYYYQn" | None,
      "cub_valor": float|None, "cub_mes": str|None
    }
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime

MIN_YEAR = 2015
MAX_DATE = date.today()

MESES = {
    "jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
    "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12,
    "janeiro": 1, "fevereiro": 2, "marco": 3, "março": 3, "abril": 4,
    "maio": 5, "junho": 6, "julho": 7, "agosto": 8, "setembro": 9,
    "outubro": 10, "novembro": 11, "dezembro": 12,
}

# "data base ... 24/05/2026" ou "data base: maio/2026" ou "data-base 05/2026"
# (rótulo ANTES da data — formato Cartesian/openpyxl)
DATA_BASE_RE = re.compile(
    r"data[\s_\-]*base\s*[:\|]?[\s\|]{0,8}("
    r"(?:19|20)\d{2}[-/][01]?\d[-/][0-3]?\d|"      # ISO 2026-05-24 (openpyxl datetime)
    r"[0-3]?\d[/.\-][01]?\d[/.\-]\d{4}|"            # 24/05/2026
    r"[01]?\d[/.\-]\d{4}|"                          # 05/2026
    r"[a-zç]+[/.\-]\s?\d{2,4})",                    # maio/2026
    re.IGNORECASE,
)
# Formato AltoQi/SIENGE: a DATA vem ANTES do rótulo "Data base":
#   "Versão do orçamento 1 - 20/11/2024 - 18:31:39 Data base"
# Cap de 30 chars entre a data e o rótulo evita casar uma data distante por acaso.
DATA_BASE_ANTES_RE = re.compile(
    r"("
    r"[0-3]?\d[/.\-][01]?\d[/.\-]\d{4}|"            # 20/11/2024
    r"(?:19|20)\d{2}[-/][01]?\d[-/][0-3]?\d|"       # ISO
    r"[a-zç]{3,9}[/.\-]\s?\d{2,4}"                  # nov/2024
    r")[^\n\r]{0,30}?data[\s_\-]*base",
    re.IGNORECASE,
)
# CUB de referência: "CUB 05/2026", "CUB maio/2026", "ref. CUB jul/23", "CUB ... 2026-05-01"
CUB_MES_RE = re.compile(
    r"cub[^\n\r]{0,40}?("
    r"(?:19|20)\d{2}[-/][01]?\d[-/][0-3]?\d|"       # ISO 2026-05-01
    r"[01]?\d[/.\-]\d{4}|"
    r"[a-zç]{3,9}[/.\-]\s?\d{2,4})",
    re.IGNORECASE,
)
# data na pasta: "06.2022", "2022-06", "06_2022"
PASTA_MM_YYYY = re.compile(r"\b([01]?\d)[._\-/]((?:19|20)\d{2})\b")
PASTA_YYYY_MM = re.compile(r"\b((?:19|20)\d{2})[._\-/]([01]?\d)\b")
REV_RE = re.compile(r"\bR(\d{2})\b", re.IGNORECASE)


def _valid(d: date | None) -> bool:
    return bool(d) and d.year >= MIN_YEAR and d <= MAX_DATE


def _mk(y: int, m: int) -> date | None:
    if not (1 <= m <= 12):
        return None
    try:
        d = date(y, m, 1)
    except ValueError:
        return None
    return d if _valid(d) else None


def _parse_mes_token(tok) -> date | None:
    """Parseia um token de data tolerante: ISO YYYY-MM-DD (+ hora), dd/mm/yyyy,
    mm/yyyy, mes/aa, mes/yyyy. Aceita também datetime/date direto (openpyxl)."""
    if tok is None:
        return None
    # openpyxl devolve datetime/date — usar direto
    if isinstance(tok, datetime):
        return _mk(tok.year, tok.month)
    if isinstance(tok, date):
        return _mk(tok.year, tok.month)

    t = str(tok).strip().lower()
    # cortar hora de um ISO "2026-05-24 00:00:00"
    t = re.sub(r"\s+\d{1,2}:\d{2}(:\d{2})?$", "", t)
    t = t.replace(" ", "")

    # ISO YYYY-MM-DD ou YYYY/MM/DD
    m = re.match(r"^((?:19|20)\d{2})[-/]([01]?\d)[-/]([0-3]?\d)$", t)
    if m:
        return _mk(int(m.group(1)), int(m.group(2)))

    # dd/mm/yyyy ou dd-mm-yyyy ou dd.mm.yyyy
    m = re.match(r"^([0-3]?\d)[/.\-]([01]?\d)[/.\-](\d{4})$", t)
    if m:
        return _mk(int(m.group(3)), int(m.group(2)))

    # mm/yyyy
    m = re.match(r"^([01]?\d)[/.\-](\d{4})$", t)
    if m:
        return _mk(int(m.group(2)), int(m.group(1)))

    # mes-textual/yy ou /yyyy (jul/23, maio/2026)
    m = re.match(r"^([a-zç]{3,9})[/.\-](\d{2,4})$", t)
    if m:
        mes = MESES.get(m.group(1))
        if mes:
            yy = m.group(2)
            year = int(yy) if len(yy) == 4 else 2000 + int(yy)
            return _mk(year, mes)

    return None


def _vintage(d: date | None) -> str | None:
    if not d:
        return None
    q = (d.month - 1) // 3 + 1
    return f"{d.year}Q{q}"


def from_texto(texto: str) -> list[dict]:
    """Coleta candidatos (1) célula data base e (2) CUB de um blob de texto (capa/PDF)."""
    cands = []
    if not texto:
        return cands

    for m in DATA_BASE_RE.finditer(texto):
        d = _parse_mes_token(m.group(1))
        if d:
            cands.append({"origem": "celula_data_base", "data": d.isoformat(),
                          "confianca": "alta", "raw": m.group(0)[:80]})

    # data ANTES do rótulo (AltoQi/SIENGE: "... 20/11/2024 - 18:31:39 Data base")
    for m in DATA_BASE_ANTES_RE.finditer(texto):
        d = _parse_mes_token(m.group(1))
        if d:
            cands.append({"origem": "celula_data_base", "data": d.isoformat(),
                          "confianca": "alta", "raw": m.group(0)[:80]})

    for m in CUB_MES_RE.finditer(texto):
        d = _parse_mes_token(m.group(1))
        if d:
            cands.append({"origem": "cub_mes", "data": d.isoformat(),
                          "confianca": "alta", "raw": m.group(0)[:80]})

    return cands


def from_nome_pasta(path_or_name: str) -> list[dict]:
    """Coleta candidato (3): data no nome do caminho/pasta."""
    cands = []
    if not path_or_name:
        return cands
    s = str(path_or_name)

    for m in PASTA_MM_YYYY.finditer(s):
        d = _mk(int(m.group(2)), int(m.group(1)))
        if d:
            cands.append({"origem": "nome_pasta", "data": d.isoformat(),
                          "confianca": "media", "raw": m.group(0)})
    for m in PASTA_YYYY_MM.finditer(s):
        d = _mk(int(m.group(1)), int(m.group(2)))
        if d:
            cands.append({"origem": "nome_pasta", "data": d.isoformat(),
                          "confianca": "media", "raw": m.group(0)})
    return cands


def from_mtime(mtime_iso: str | None) -> list[dict]:
    """Coleta candidato (5): mtime do arquivo, dia forçado a 01."""
    if not mtime_iso:
        return []
    try:
        dt = datetime.fromisoformat(mtime_iso)
    except ValueError:
        return []
    d = _mk(dt.year, dt.month)
    if not d:
        return []
    return [{"origem": "mtime", "data": d.isoformat(), "confianca": "baixa",
             "raw": mtime_iso}]


def revisao_de(name: str):
    if not name:
        return None
    m = REV_RE.search(name)
    return f"R{m.group(1)}" if m else None


# Prioridade de origem (maior = vence)
ORIGEM_PRIORIDADE = {
    "celula_data_base": 100,
    "cub_mes": 90,
    "nome_pasta": 60,
    "revisao": 40,
    "mtime": 10,
}
CONFIANCA_DE_ORIGEM = {
    "celula_data_base": "alta",
    "cub_mes": "alta",
    "nome_pasta": "media",
    "revisao": "media",
    "mtime": "baixa",
}


def resolve_data_preco(texto_capa: str | None = None,
                       folder_path: str | None = None,
                       file_name: str | None = None,
                       file_mtime_iso: str | None = None,
                       celula_data_base: str | None = None,
                       cub_mes: str | None = None,
                       cub_valor=None) -> dict:
    """Resolve data-base aplicando a hierarquia. Tudo opcional; usa o que vier.

    `celula_data_base` e `cub_mes`: tokens já extraídos diretamente de células
    conhecidas (ex.: CAPA!C7, BASES!B11) — entram como candidatos de alta confiança
    sem depender do regex sobre o blob de texto.
    """
    candidatos: list[dict] = []

    # Candidatos explícitos (célula conhecida) — máxima confiança
    if celula_data_base:
        d = _parse_mes_token(celula_data_base)
        if d:
            candidatos.append({"origem": "celula_data_base", "data": d.isoformat(),
                               "confianca": "alta", "raw": str(celula_data_base)})
    if cub_mes:
        d = _parse_mes_token(cub_mes)
        if d:
            candidatos.append({"origem": "cub_mes", "data": d.isoformat(),
                               "confianca": "alta", "raw": str(cub_mes)})

    # Candidatos extraídos de texto / nome / mtime
    candidatos += from_texto(texto_capa or "")
    candidatos += from_nome_pasta(folder_path or "")
    candidatos += from_nome_pasta(file_name or "")
    candidatos += from_mtime(file_mtime_iso)

    rev = revisao_de(file_name or "") or revisao_de(folder_path or "")

    # Dedupe por (origem, data)
    seen = set()
    deduped = []
    for c in candidatos:
        k = (c["origem"], c["data"])
        if k in seen:
            continue
        seen.add(k)
        deduped.append(c)
    candidatos = deduped

    # Escolha: maior prioridade de origem; em empate de origem, data mais recente.
    escolha = None
    if candidatos:
        escolha = max(
            candidatos,
            key=lambda c: (ORIGEM_PRIORIDADE.get(c["origem"], 0), c["data"]),
        )

    # Ambiguidade: duas origens de mesma prioridade-máxima discordam de data,
    # OU a melhor é baixa confiança e há candidato de média/alta com data diferente.
    ambiguo = False
    if escolha:
        top_pri = ORIGEM_PRIORIDADE.get(escolha["origem"], 0)
        same_pri_datas = {c["data"] for c in candidatos
                          if ORIGEM_PRIORIDADE.get(c["origem"], 0) == top_pri}
        if len(same_pri_datas) > 1:
            ambiguo = True

    if escolha:
        return {
            "data_base": escolha["data"],
            "origem": escolha["origem"],
            "confianca": escolha["confianca"],
            "ambiguo": ambiguo,
            "revisao": rev,
            "candidatos": candidatos,
            "vintage": _vintage(date.fromisoformat(escolha["data"])),
            "cub_valor": cub_valor,
            "cub_mes": cub_mes,
        }

    # Nada resolvido — devolve revisão como sinal de ordenação, mas sem data
    return {
        "data_base": None,
        "origem": None,
        "confianca": "nenhuma",
        "ambiguo": False,
        "revisao": rev,
        "candidatos": [],
        "vintage": None,
        "cub_valor": cub_valor,
        "cub_mes": cub_mes,
    }


def main():
    ap = argparse.ArgumentParser(description="Resolver data-base do preço (Fase 1)")
    ap.add_argument("--texto", default=None, help="blob de texto da capa/PDF")
    ap.add_argument("--folder", default=None)
    ap.add_argument("--file", default=None)
    ap.add_argument("--mtime", default=None, help="mtime ISO do arquivo")
    ap.add_argument("--celula", default=None, help="token da célula data base")
    ap.add_argument("--cub-mes", default=None)
    ap.add_argument("--cub-valor", default=None, type=float)
    args = ap.parse_args()

    r = resolve_data_preco(
        texto_capa=args.texto, folder_path=args.folder, file_name=args.file,
        file_mtime_iso=args.mtime, celula_data_base=args.celula,
        cub_mes=args.cub_mes, cub_valor=args.cub_valor,
    )
    print(json.dumps(r, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
