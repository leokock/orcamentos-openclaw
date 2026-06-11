#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LOADER de produção — staging JSONL (custos historica) -> Supabase indices-cartesian.

Lê o staging de UM ou MAIS slugs em:
    _local/base-custos-historica/staging/<slug>/projeto.json
    _local/base-custos-historica/staging/<slug>/itens.jsonl
    _local/base-custos-historica/staging/<slug>/insumos.jsonl

E faz UPSERT idempotente nas TABELAS NOVAS (jamais nas antigas):
    - fato_projetos              ON CONFLICT (slug, fonte_leva)
    - fato_itens                 ON CONFLICT (source_sha1, source_sheet, source_row)
    - fato_composicao_insumos    só pros itens recém-inseridos neste run (evita duplicar em re-run)
    - ingest_runs                1 linha de controle (status running -> done)

Regras:
    - fonte_leva = "drive-53-pastas-2026-06"
    - vintage calculado em Python a partir de data_base (YYYY + 'Q' + trimestre, ex 2026Q2).
    - Reusa a credencial service_role do .env.indices-cartesian (mesmo padrão do
      scripts/ingestar_indices_supabase.py).
    - LOAD-ONLY (sem Claude). PYTHONIOENCODING=utf-8.

Uso:
    set PYTHONIOENCODING=utf-8
    py -3.10 scripts/custos_historica/carregar_fato_supabase.py cincatarina gdi-santa-monica tecverde-casa-c4e
    py -3.10 scripts/custos_historica/carregar_fato_supabase.py --all        # todos os slugs em staging
    py -3.10 scripts/custos_historica/carregar_fato_supabase.py --dry-run <slug>
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Iterator

# Garante UTF-8 no stdout mesmo se PYTHONIOENCODING não foi setado.
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from dotenv import dotenv_values
from supabase import create_client, Client

# ----------------------------------------------------------------------------
# Constantes
# ----------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent  # .../orcamentos-openclaw
ENV_FILE = REPO_ROOT / ".env.indices-cartesian"

# Staging vive no openclaw (sibling do orcamentos-openclaw).
STAGING_ROOT = Path(
    r"C:\Users\leona\openclaw\_local\base-custos-historica\staging"
)

FONTE_LEVA = "drive-53-pastas-2026-06"
SCRIPT_VERSION = "carregar_fato_supabase.py@v1"

BATCH_SIZE = 500

EMPTY_SENTINELS = {"", None, "—", "-", "null", "None"}


# ----------------------------------------------------------------------------
# Coerções
# ----------------------------------------------------------------------------

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


def to_int(value: Any) -> int | None:
    if value in EMPTY_SENTINELS:
        return None
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def to_text(value: Any) -> str | None:
    if value is None:
        return None
    s = str(value).strip()
    if s in EMPTY_SENTINELS:
        return None
    return s


def to_date(value: Any) -> str | None:
    """Retorna ISO date 'YYYY-MM-DD' ou None. Aceita date/datetime/str."""
    if value in EMPTY_SENTINELS:
        return None
    if isinstance(value, (date, datetime)):
        return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()
    s = str(value).strip()
    # Já vem como '2026-05-01' no staging
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date().isoformat()
    except (TypeError, ValueError):
        return None


def vintage_from_data_base(data_base_iso: str | None) -> str | None:
    """
    Calcula vintage em Python a partir da data_base.
    Formato: YYYY + 'Q' + trimestre (1..4). Ex: 2026-05-01 -> '2026Q2'.
    """
    iso = to_date(data_base_iso)
    if iso is None:
        return None
    try:
        d = datetime.strptime(iso, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None
    trimestre = (d.month - 1) // 3 + 1
    return f"{d.year}Q{trimestre}"


# ----------------------------------------------------------------------------
# Leitura do staging
# ----------------------------------------------------------------------------

def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_jsonl(path: Path) -> Iterator[dict]:
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def chunked(iterable: Iterable, size: int):
    buf = []
    for item in iterable:
        buf.append(item)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


# ----------------------------------------------------------------------------
# Transformadores staging -> linha das tabelas novas
# ----------------------------------------------------------------------------

def build_fato_projeto(projeto: dict, run_id: int | None) -> dict:
    data_base = to_date(projeto.get("data_base"))
    vintage = vintage_from_data_base(projeto.get("data_base")) or to_text(projeto.get("vintage"))
    return {
        "slug": to_text(projeto.get("slug")),
        "cidade": to_text(projeto.get("cidade")),
        "fonte": to_text(projeto.get("fonte")) or to_text(projeto.get("folder")),
        "ac_m2": to_numeric(projeto.get("ac")),
        "ur": to_numeric(projeto.get("ur")),
        "total_rs": to_numeric(projeto.get("total")),
        "rsm2": to_numeric(projeto.get("rsm2")),
        "padrao": to_text(projeto.get("padrao")),
        "padrao_confianca": to_numeric(projeto.get("padrao_confianca")),
        "macrogrupos": projeto.get("macrogrupos") or {},
        "disciplinas": projeto.get("disciplinas") or {},
        "data_base": data_base,
        "vintage": vintage,
        "fonte_leva": FONTE_LEVA,
        "run_id": run_id,
    }


def build_fato_item(item: dict, projeto: dict, run_id: int | None) -> dict:
    data_base = to_date(item.get("data_base") or projeto.get("data_base"))
    vintage = (
        vintage_from_data_base(item.get("data_base") or projeto.get("data_base"))
        or to_text(item.get("vintage"))
    )
    completude = projeto.get("completude") or {}
    return {
        "slug": to_text(item.get("slug")),
        "source_sha1": to_text(item.get("source_sha1")) or "",
        "source_sheet": to_text(item.get("source_sheet")) or "",
        "source_row": to_int(item.get("source_row")) if item.get("source_row") is not None else 0,
        "codigo": to_text(item.get("codigo")),
        "descricao": to_text(item.get("descricao")) or "",
        "descricao_norm": to_text(item.get("descricao_norm")),
        "unidade": to_text(item.get("unidade")),
        "qtd": to_numeric(item.get("qtd")),
        "pu": to_numeric(item.get("pu")),
        "pu_sem_bdi": to_numeric(item.get("pu_sem_bdi")),
        "total": to_numeric(item.get("total")),
        "aba": to_text(item.get("aba")),
        "macrogrupo": to_text(item.get("macrogrupo")) or to_text(item.get("macrogrupo_cru")),
        "cluster_key": to_text(item.get("cluster_key")),
        "data_base": data_base,
        "vintage": vintage,
        "data_base_origem": to_text(item.get("data_base_origem")),
        "data_base_confianca": to_text(item.get("data_base_confianca")),
        "cub_mes": to_text(item.get("cub_mes")),
        "folder_tipo": (to_text(item.get("folder_tipo")) or "")[:1] or None,
        "revisao": to_text(item.get("revisao")),
        "completeness_tier": to_text(completude.get("tier")),
        "completeness_score": to_numeric(completude.get("score")),
        "fonte_leva": FONTE_LEVA,
        "run_id": run_id,
    }


def build_fato_insumo(insumo: dict, item_id: int, projeto: dict, run_id: int | None) -> dict:
    data_base = to_date(insumo.get("data_base") or projeto.get("data_base"))
    vintage = (
        vintage_from_data_base(insumo.get("data_base") or projeto.get("data_base"))
        or to_text(insumo.get("vintage"))
    )
    return {
        "item_id": item_id,
        "slug": to_text(insumo.get("slug")) or to_text(projeto.get("slug")),
        "descricao": to_text(insumo.get("descricao")) or "",
        "descricao_norm": to_text(insumo.get("descricao_norm")),
        "insumo_key": to_text(insumo.get("insumo_key")),
        "categoria": to_text(insumo.get("categoria")),
        "fornecedor": to_text(insumo.get("fornecedor")),
        "unidade": to_text(insumo.get("unidade")),
        "consumo": to_numeric(insumo.get("consumo")),
        "pu": to_numeric(insumo.get("pu")),
        "total": to_numeric(insumo.get("total")),
        "data_base": data_base,
        "vintage": vintage,
        "fonte_leva": FONTE_LEVA,
        "run_id": run_id,
    }


# ----------------------------------------------------------------------------
# Carregamento por slug
# ----------------------------------------------------------------------------

def carregar_slug(
    client: Client,
    slug: str,
    run_id: int | None,
    dry_run: bool,
) -> dict:
    base = STAGING_ROOT / slug
    projeto_path = base / "projeto.json"
    itens_path = base / "itens.jsonl"
    insumos_path = base / "insumos.jsonl"

    if not projeto_path.exists():
        raise FileNotFoundError(f"projeto.json não encontrado para slug={slug} em {projeto_path}")

    projeto = read_json(projeto_path)
    print(f"\n=== {slug} ===")
    print(f"  data_base={projeto.get('data_base')} vintage(calc)={vintage_from_data_base(projeto.get('data_base'))}")

    stats = {
        "slug": slug,
        "projeto_upserted": 0,
        "itens_lidos": 0,
        "itens_upserted": 0,
        "itens_inseridos_novos": 0,
        "insumos_lidos": 0,
        "insumos_inseridos": 0,
    }

    # --- 1) fato_projetos (upsert por slug,fonte_leva) ---
    proj_row = build_fato_projeto(projeto, run_id)
    if dry_run:
        print(f"  [dry-run] fato_projetos upsert: {json.dumps({k: proj_row[k] for k in ('slug','ac_m2','total_rs','data_base','vintage','fonte_leva')}, ensure_ascii=False)}")
    else:
        client.table("fato_projetos").upsert(proj_row, on_conflict="slug,fonte_leva").execute()
        stats["projeto_upserted"] = 1

    # --- 2) fato_itens (upsert por source_sha1,source_sheet,source_row) ---
    itens_raw = list(read_jsonl(itens_path))
    stats["itens_lidos"] = len(itens_raw)
    item_rows = [build_fato_item(it, projeto, run_id) for it in itens_raw]

    # Conjunto de chaves naturais existentes ANTES do upsert (pra saber quais são novos).
    chaves = [(r["source_sha1"], r["source_sheet"], r["source_row"]) for r in item_rows]
    existentes_antes: set[tuple] = set()
    if not dry_run and chaves:
        # Busca por source_sha1 deste slug (todos os itens compartilham o mesmo sha1 do workbook).
        shas = sorted({r["source_sha1"] for r in item_rows if r["source_sha1"]})
        for sha in shas:
            resp = (
                client.table("fato_itens")
                .select("source_sha1,source_sheet,source_row")
                .eq("source_sha1", sha)
                .eq("fonte_leva", FONTE_LEVA)
                .execute()
            )
            for row in (resp.data or []):
                existentes_antes.add((row["source_sha1"], row["source_sheet"], row["source_row"]))

    novos = [
        r for r in item_rows
        if (r["source_sha1"], r["source_sheet"], r["source_row"]) not in existentes_antes
    ]
    stats["itens_inseridos_novos"] = len(novos)

    if dry_run:
        print(f"  [dry-run] fato_itens: {len(item_rows)} linhas (novas estimadas={len(item_rows)})")
    else:
        enviados = 0
        for batch in chunked(item_rows, BATCH_SIZE):
            client.table("fato_itens").upsert(
                batch, on_conflict="source_sha1,source_sheet,source_row"
            ).execute()
            enviados += len(batch)
        stats["itens_upserted"] = enviados
        print(f"  fato_itens upserted: {enviados} (novos neste run: {len(novos)})")

    # --- 3) fato_composicao_insumos (só pros itens recém-inseridos) ---
    insumos_raw = list(read_jsonl(insumos_path))
    stats["insumos_lidos"] = len(insumos_raw)

    if not insumos_raw:
        print("  (sem insumos)")
    elif dry_run:
        print(f"  [dry-run] fato_composicao_insumos: {len(insumos_raw)} insumos (inseriria só se houvesse item novo)")
    elif not novos:
        # Re-run: nenhum item novo -> não duplica insumos.
        print(f"  fato_composicao_insumos: 0 inseridos (nenhum item novo neste run -> evita duplicar)")
    else:
        # item_id é NOT NULL e os insumos do staging são composição a nível de projeto
        # (sem ponteiro de linha). Ancora todos no PRIMEIRO item recém-inserido do slug.
        sha_anchor = novos[0]["source_sha1"]
        sheet_anchor = novos[0]["source_sheet"]
        row_anchor = novos[0]["source_row"]
        resp = (
            client.table("fato_itens")
            .select("id")
            .eq("source_sha1", sha_anchor)
            .eq("source_sheet", sheet_anchor)
            .eq("source_row", row_anchor)
            .eq("fonte_leva", FONTE_LEVA)
            .limit(1)
            .execute()
        )
        if not resp.data:
            raise RuntimeError(f"Não achei item âncora pra insumos do slug={slug}")
        anchor_item_id = resp.data[0]["id"]

        insumo_rows = [build_fato_insumo(ins, anchor_item_id, projeto, run_id) for ins in insumos_raw]
        enviados = 0
        for batch in chunked(insumo_rows, BATCH_SIZE):
            client.table("fato_composicao_insumos").insert(batch).execute()
            enviados += len(batch)
        stats["insumos_inseridos"] = enviados
        print(f"  fato_composicao_insumos inseridos: {enviados} (âncora item_id={anchor_item_id})")

    return stats


# ----------------------------------------------------------------------------
# ingest_runs
# ----------------------------------------------------------------------------

def abrir_run(client: Client, slugs: list[str]) -> int:
    resp = (
        client.table("ingest_runs")
        .insert(
            {
                "fonte_leva": FONTE_LEVA,
                "status": "running",
                "script_version": SCRIPT_VERSION,
                "params": {"slugs": slugs, "staging_root": str(STAGING_ROOT)},
                "tabelas_afetadas": [
                    "fato_projetos",
                    "fato_itens",
                    "fato_composicao_insumos",
                ],
            }
        )
        .execute()
    )
    run_id = resp.data[0]["id"]
    print(f"> ingest_runs aberto: run_id={run_id} (status=running)")
    return run_id


def fechar_run(client: Client, run_id: int, totais: dict, status: str = "done") -> None:
    client.table("ingest_runs").update(
        {
            "finished_at": datetime.utcnow().isoformat(),
            "status": status,
            "n_projetos": totais.get("n_projetos", 0),
            "n_itens": totais.get("n_itens", 0),
            "n_insumos": totais.get("n_insumos", 0),
        }
    ).eq("id", run_id).execute()
    print(f"> ingest_runs fechado: run_id={run_id} status={status}")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def descobrir_slugs() -> list[str]:
    if not STAGING_ROOT.exists():
        return []
    return sorted(
        p.name for p in STAGING_ROOT.iterdir()
        if p.is_dir() and (p / "projeto.json").exists()
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="Slugs a carregar (subpastas de staging).")
    parser.add_argument("--all", action="store_true", help="Carrega todos os slugs em staging.")
    parser.add_argument("--dry-run", action="store_true", help="Só lê e imprime; não escreve no Supabase.")
    args = parser.parse_args()

    if args.all:
        slugs = descobrir_slugs()
    else:
        slugs = args.slugs
    if not slugs:
        print("ERRO: informe slugs ou use --all.", file=sys.stderr)
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

    print(f"> Conectando no Supabase: {url}")
    print(f"> fonte_leva = {FONTE_LEVA}")
    print(f"> slugs = {slugs}")
    client = create_client(url, key)

    run_id = None
    if not args.dry_run:
        run_id = abrir_run(client, slugs)

    all_stats = []
    status_final = "done"
    try:
        for slug in slugs:
            st = carregar_slug(client, slug, run_id, args.dry_run)
            all_stats.append(st)
    except Exception as e:
        status_final = "error"
        print(f"\nERRO durante carga: {e}", file=sys.stderr)
        if run_id is not None:
            try:
                fechar_run(client, run_id, _totais(all_stats), status="error")
            except Exception:
                pass
        raise

    # Resumo
    print("\n=== RESUMO ===")
    for st in all_stats:
        print(
            f"  {st['slug']}: projeto={st['projeto_upserted']} "
            f"itens_lidos={st['itens_lidos']} itens_upserted={st['itens_upserted']} "
            f"itens_novos={st['itens_inseridos_novos']} "
            f"insumos_lidos={st['insumos_lidos']} insumos_inseridos={st['insumos_inseridos']}"
        )

    if run_id is not None:
        fechar_run(client, run_id, _totais(all_stats), status=status_final)

    return 0


def _totais(all_stats: list[dict]) -> dict:
    return {
        "n_projetos": sum(s.get("projeto_upserted", 0) for s in all_stats),
        "n_itens": sum(s.get("itens_upserted", 0) for s in all_stats),
        "n_insumos": sum(s.get("insumos_inseridos", 0) for s in all_stats),
    }


if __name__ == "__main__":
    sys.exit(main())
