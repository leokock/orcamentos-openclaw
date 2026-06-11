#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MIGRAÇÃO LOAD-ONLY — JSON antigos da base anterior -> tabelas novas.

Dois modos:

1) PROJETOS (default) — indices-executivo/*.json -> fato_projetos.
   Lê os ~126 JSON crus e carrega em fato_projetos com fonte_leva="base-2026-04".
   PRESERVA os campos crus (macrogrupos, disciplinas jsonb) + ac/total/padrao/cidade/rsm2/ur/fonte.
   UPSERT idempotente: ON CONFLICT (slug, fonte_leva).

2) ITENS (--itens) — itens-detalhados/*.json -> fato_itens.
   Lê os ~126 JSON de itens detalhados (cada arquivo tem `abas` -> `itens`) e carrega
   centenas de milhares de linhas em fato_itens com fonte_leva="base-2026-04".
   Campos por item: slug, codigo, descricao, unidade, qtd, pu, total, aba (=nome da aba),
   macrogrupo (=secao quando houver). data_base/vintage ficam NULL (base antiga não tem data).
   Chave natural sintética pra idempotência (a base antiga não tem source_sha1/row reais):
       source_sha1   = sha1(bytes do arquivo) — estável entre runs, único por projeto
       source_sheet  = nome da aba
       source_row    = índice global do item dentro do arquivo (0..N)
   UPSERT idempotente: ON CONFLICT (source_sha1, source_sheet, source_row).
   BATCHES de 2000 linhas/insert via service_role (mesmo padrão de carregar_fato_supabase.py).

Em ambos os modos: abre 1 linha em ingest_runs (status running -> done/error).
Não usa Claude. Sem extração extra. PYTHONIOENCODING=utf-8. NÃO toca nas tabelas antigas.

Diretórios de origem (auto-detectados, primeiro que existir):
    projetos: C:\\Users\\leona\\openclaw\\data\\base\\indices-executivo
              C:\\Users\\leona\\orcamentos-openclaw\\base\\indices-executivo
    itens:    C:\\Users\\leona\\openclaw\\data\\base\\itens-detalhados
              C:\\Users\\leona\\orcamentos-openclaw\\base\\itens-detalhados

Uso:
    set PYTHONIOENCODING=utf-8
    py -3.10 scripts/custos_historica/migrar_raw_antigo.py                 # projetos
    py -3.10 scripts/custos_historica/migrar_raw_antigo.py --dry-run
    py -3.10 scripts/custos_historica/migrar_raw_antigo.py --itens         # itens
    py -3.10 scripts/custos_historica/migrar_raw_antigo.py --itens --dry-run
    py -3.10 scripts/custos_historica/migrar_raw_antigo.py --itens --dir <caminho>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from dotenv import dotenv_values
from supabase import create_client, Client

REPO_ROOT = Path(__file__).resolve().parent.parent.parent  # .../orcamentos-openclaw
ENV_FILE = REPO_ROOT / ".env.indices-cartesian"

CANDIDATE_DIRS = [
    Path(r"C:\Users\leona\openclaw\data\base\indices-executivo"),
    REPO_ROOT / "base" / "indices-executivo",
]

CANDIDATE_DIRS_ITENS = [
    Path(r"C:\Users\leona\openclaw\data\base\itens-detalhados"),
    REPO_ROOT / "base" / "itens-detalhados",
]

FONTE_LEVA = "base-2026-04"
SCRIPT_VERSION = "migrar_raw_antigo.py@v1"
BATCH_SIZE = 100
BATCH_SIZE_ITENS = 2000

EMPTY_SENTINELS = {"", None, "—", "-", "null", "None"}


def to_numeric(value: Any) -> float | None:
    if value in EMPTY_SENTINELS:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip().replace(",", ".")
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def to_int_numeric(value: Any) -> float | None:
    # ur é numeric no schema novo; mantém float pra ser tolerante.
    return to_numeric(value)


def to_text(value: Any) -> str | None:
    if value is None:
        return None
    s = str(value).strip()
    if s in EMPTY_SENTINELS:
        return None
    return s


def chunked(iterable: Iterable, size: int):
    buf = []
    for item in iterable:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def descobrir_dir(override: str | None, candidates: list[Path] | None = None, rotulo: str = "indices-executivo") -> Path:
    if override:
        p = Path(override)
        if not p.exists():
            raise FileNotFoundError(f"--dir não existe: {p}")
        return p
    for cand in (candidates or CANDIDATE_DIRS):
        if cand.exists():
            return cand
    raise FileNotFoundError(
        f"Não achei o diretório {rotulo}. Tentei:\n  "
        + "\n  ".join(str(c) for c in (candidates or CANDIDATE_DIRS))
    )


def build_row(d: dict, run_id: int | None) -> dict:
    # slug pode vir como 'projeto' (maioria) ou 'slug' (alguns arquivos).
    slug = to_text(d.get("slug")) or to_text(d.get("projeto"))
    return {
        "slug": slug,
        "cidade": to_text(d.get("cidade")),
        "fonte": to_text(d.get("fonte")),
        "ac_m2": to_numeric(d.get("ac")),
        "ur": to_int_numeric(d.get("ur")),
        "total_rs": to_numeric(d.get("total")),
        "rsm2": to_numeric(d.get("rsm2")),
        "padrao": to_text(d.get("padrao")),
        "padrao_confianca": to_numeric(d.get("padrao_confianca")),
        # CRÍTICO: preservar crus pro gate de continuidade.
        "macrogrupos": d.get("macrogrupos") if d.get("macrogrupos") is not None else {},
        "disciplinas": d.get("disciplinas") if d.get("disciplinas") is not None else {},
        "data_base": None,   # base antiga não tem data_base confiável
        "vintage": None,
        "fonte_leva": FONTE_LEVA,
        "run_id": run_id,
    }


def abrir_run(client: Client, n_arquivos: int, origem: str) -> int:
    resp = (
        client.table("ingest_runs")
        .insert(
            {
                "fonte_leva": FONTE_LEVA,
                "status": "running",
                "script_version": SCRIPT_VERSION,
                "params": {"origem": origem, "n_arquivos": n_arquivos},
                "tabelas_afetadas": ["fato_projetos"],
            }
        )
        .execute()
    )
    run_id = resp.data[0]["id"]
    print(f"> ingest_runs aberto: run_id={run_id} (status=running)")
    return run_id


def fechar_run(client: Client, run_id: int, n_projetos: int, status: str = "done") -> None:
    client.table("ingest_runs").update(
        {
            "finished_at": datetime.utcnow().isoformat(),
            "status": status,
            "n_projetos": n_projetos,
        }
    ).eq("id", run_id).execute()
    print(f"> ingest_runs fechado: run_id={run_id} status={status} n_projetos={n_projetos}")


# ----------------------------------------------------------------------------
# MODO ITENS — itens-detalhados/*.json -> fato_itens
# ----------------------------------------------------------------------------

def file_sha1(fp: Path) -> str:
    """sha1 dos bytes do arquivo — estável entre runs, único por projeto/arquivo."""
    h = hashlib.sha1()
    with fp.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def build_item_rows(fp: Path, run_id: int | None) -> list[dict]:
    """
    Lê 1 arquivo itens-detalhados e devolve as linhas pra fato_itens.

    Cada arquivo tem `abas` (lista) -> cada aba tem `nome` + `itens` (lista).
    Chave natural sintética:
        source_sha1  = sha1 do arquivo (igual pra todos os itens do projeto)
        source_sheet = nome da aba
        source_row   = índice global do item dentro do arquivo (0..N), garante unicidade
    """
    with fp.open("r", encoding="utf-8") as f:
        d = json.load(f)

    slug = to_text(d.get("projeto")) or to_text(d.get("slug")) or fp.stem
    sha = file_sha1(fp)

    rows: list[dict] = []
    row_idx = 0  # índice GLOBAL no arquivo -> unicidade com source_sha1 fixo
    for aba in (d.get("abas") or []):
        aba_nome = to_text(aba.get("nome")) or ""
        for it in (aba.get("itens") or []):
            descricao = to_text(it.get("descricao")) or ""
            # fato_itens.descricao é NOT NULL; pula linhas totalmente vazias (sem desc/codigo).
            codigo = to_text(it.get("codigo"))
            if not descricao and not codigo:
                row_idx += 1
                continue
            rows.append({
                "slug": slug,
                "source_sha1": sha,
                "source_sheet": aba_nome,
                "source_row": row_idx,
                "codigo": codigo,
                "descricao": descricao or (codigo or ""),
                "unidade": to_text(it.get("unidade")),
                "qtd": to_numeric(it.get("qtd")),
                "pu": to_numeric(it.get("pu")),
                "total": to_numeric(it.get("total")),
                "aba": aba_nome or None,
                "macrogrupo": to_text(it.get("secao")),
                "data_base": None,   # base antiga não tem data
                "vintage": None,
                "fonte_leva": FONTE_LEVA,
                "run_id": run_id,
            })
            row_idx += 1
    return rows


def abrir_run_itens(client: Client, n_arquivos: int, origem: str) -> int:
    resp = (
        client.table("ingest_runs")
        .insert(
            {
                "fonte_leva": FONTE_LEVA,
                "status": "running",
                "script_version": SCRIPT_VERSION,
                "params": {"origem": origem, "n_arquivos": n_arquivos, "modo": "itens"},
                "tabelas_afetadas": ["fato_itens"],
            }
        )
        .execute()
    )
    run_id = resp.data[0]["id"]
    print(f"> ingest_runs aberto: run_id={run_id} (status=running, modo=itens)")
    return run_id


def fechar_run_itens(client: Client, run_id: int, n_itens: int, status: str = "done") -> None:
    client.table("ingest_runs").update(
        {
            "finished_at": datetime.utcnow().isoformat(),
            "status": status,
            "n_itens": n_itens,
        }
    ).eq("id", run_id).execute()
    print(f"> ingest_runs fechado: run_id={run_id} status={status} n_itens={n_itens}")


def main_itens(args) -> int:
    src_dir = descobrir_dir(args.dir, CANDIDATE_DIRS_ITENS, "itens-detalhados")
    arquivos = sorted(src_dir.glob("*.json"))
    print(f"> [ITENS] Origem: {src_dir}")
    print(f"> [ITENS] Arquivos .json: {len(arquivos)}")
    print(f"> [ITENS] fonte_leva = {FONTE_LEVA}")

    if not arquivos:
        print(f"ERRO: nenhum .json encontrado em {src_dir}", file=sys.stderr)
        return 1

    if not ENV_FILE.exists():
        print(f"ERRO: .env não encontrado em {ENV_FILE}", file=sys.stderr)
        return 1
    env = dotenv_values(ENV_FILE)
    url = env.get("SUPABASE_URL")
    key = env.get("SUPABASE_SECRET_KEY")
    if not url or not key or str(key).startswith("COLE_AQUI"):
        print("ERRO: SUPABASE_URL/SUPABASE_SECRET_KEY não preenchidos no .env", file=sys.stderr)
        return 1

    # Monta todas as linhas (sem run_id ainda).
    rows: list[dict] = []
    n_skip_vazio = 0
    slugs_set = set()
    for fp in arquivos:
        before = len(rows)
        file_rows = build_item_rows(fp, None)
        rows.extend(file_rows)
        if file_rows:
            slugs_set.add(file_rows[0]["slug"])
        # (n_skip não é exato por arquivo, mas reportamos o total no fim)

    print(f"> [ITENS] Linhas montadas: {len(rows)} | slugs distintos: {len(slugs_set)}")

    if args.dry_run:
        amostra = rows[0] if rows else {}
        print("  [dry-run] amostra[0]:")
        print("   ", json.dumps(
            {k: amostra.get(k) for k in
             ("slug", "source_sha1", "source_sheet", "source_row",
              "codigo", "descricao", "unidade", "qtd", "pu", "total", "aba", "macrogrupo")},
            ensure_ascii=False,
        ))
        # checagem de unicidade da chave natural (sanity, não escreve)
        chaves = {(r["source_sha1"], r["source_sheet"], r["source_row"]) for r in rows}
        print(f"  [dry-run] chaves naturais únicas: {len(chaves)} / {len(rows)} linhas")
        return 0

    print(f"> [ITENS] Conectando no Supabase: {url}")
    client = create_client(url, key)

    run_id = abrir_run_itens(client, len(arquivos), str(src_dir))
    for r in rows:
        r["run_id"] = run_id

    status_final = "done"
    enviados = 0
    try:
        for batch in chunked(rows, BATCH_SIZE_ITENS):
            client.table("fato_itens").upsert(
                batch, on_conflict="source_sha1,source_sheet,source_row"
            ).execute()
            enviados += len(batch)
            print(f"    upserted {enviados}/{len(rows)}")
    except Exception as e:
        status_final = "error"
        print(f"\nERRO durante upsert de itens: {e}", file=sys.stderr)
        fechar_run_itens(client, run_id, enviados, status="error")
        raise

    fechar_run_itens(client, run_id, enviados, status=status_final)
    print(f"\n=== RESUMO ITENS === fato_itens upserted ({FONTE_LEVA}): {enviados} | slugs: {len(slugs_set)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Só lê/imprime, não escreve.")
    parser.add_argument("--dir", type=str, help="Override do diretório de origem.")
    parser.add_argument(
        "--itens", action="store_true",
        help="Modo ITENS: carrega itens-detalhados/*.json em fato_itens.",
    )
    args = parser.parse_args()

    if args.itens:
        return main_itens(args)

    src_dir = descobrir_dir(args.dir)
    arquivos = sorted(src_dir.glob("*.json"))
    print(f"> Origem: {src_dir}")
    print(f"> Arquivos .json: {len(arquivos)}")
    print(f"> fonte_leva = {FONTE_LEVA}")

    if not ENV_FILE.exists():
        print(f"ERRO: .env não encontrado em {ENV_FILE}", file=sys.stderr)
        return 1
    env = dotenv_values(ENV_FILE)
    url = env.get("SUPABASE_URL")
    key = env.get("SUPABASE_SECRET_KEY")
    if not url or not key or str(key).startswith("COLE_AQUI"):
        print("ERRO: SUPABASE_URL/SUPABASE_SECRET_KEY não preenchidos no .env", file=sys.stderr)
        return 1

    rows = []
    sem_slug = []
    sem_macro = 0
    sem_disc = 0
    for fp in arquivos:
        with fp.open("r", encoding="utf-8") as f:
            d = json.load(f)
        row = build_row(d, None)
        if not row["slug"]:
            sem_slug.append(fp.name)
            continue
        if not row["macrogrupos"]:
            sem_macro += 1
        if not row["disciplinas"]:
            sem_disc += 1
        rows.append(row)

    print(f"> Linhas válidas (com slug): {len(rows)}")
    if sem_slug:
        print(f"  [aviso] {len(sem_slug)} arquivos sem slug/projeto: {sem_slug}")
    print(f"  macrogrupos vazios: {sem_macro} | disciplinas vazias: {sem_disc}")

    if args.dry_run:
        amostra = rows[0] if rows else {}
        print("  [dry-run] amostra[0]:")
        print("   ", json.dumps(
            {k: amostra.get(k) for k in ("slug", "ac_m2", "total_rs", "rsm2", "padrao", "cidade")},
            ensure_ascii=False,
        ))
        print(f"    macrogrupos keys: {list((amostra.get('macrogrupos') or {}).keys())[:5]}")
        print(f"    disciplinas keys: {list((amostra.get('disciplinas') or {}).keys())[:5]}")
        return 0

    print(f"> Conectando no Supabase: {url}")
    client = create_client(url, key)

    run_id = abrir_run(client, len(arquivos), str(src_dir))
    for r in rows:
        r["run_id"] = run_id

    status_final = "done"
    enviados = 0
    try:
        for batch in chunked(rows, BATCH_SIZE):
            client.table("fato_projetos").upsert(batch, on_conflict="slug,fonte_leva").execute()
            enviados += len(batch)
            print(f"    upserted {enviados}/{len(rows)}")
    except Exception as e:
        status_final = "error"
        print(f"\nERRO durante upsert: {e}", file=sys.stderr)
        fechar_run(client, run_id, enviados, status="error")
        raise

    fechar_run(client, run_id, enviados, status=status_final)
    print(f"\n=== RESUMO === fato_projetos upserted ({FONTE_LEVA}): {enviados}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
