#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""processar_lote.py — PASSO 2 do lote (SPEC base-custos-historica).

DRIVER deterministico (Claude=0). Para cada pasta de custo enumerada por
enumerar_pastas_custo.py:

  1. roda o pipeline existente em SUBPROCESSO isolado, com timeout por pasta:
       run_selftest.run_one() = discovery_custos (pick endurecido, ja' exclui
       Referencias/Obsoletos/Backup) -> parse_custos (fix coluna total)
       -> resolve_data_preco -> grava staging em
       _local/base-custos-historica/staging/<slug>/
  2. le o manifest do staging e aplica o GATE por pasta:
       - status == 'pendente-ocr' (PDF sem tabela)        -> status=pendente-ocr (NAO carrega)
       - reconcile pu*qtd vs total  >= 95%                 -> OK
       - reconcile < 95% E nao-excecao                     -> status=descartado (NAO carrega)
       - excecao 'orcamento so-folha' (sem triple pu/qtd/total
         em massa, mas tem itens com total)               -> carrega, documentado
  3. dedup vs os ja-carregados (126 base + onda1): SequenceMatcher>=0.7 OU
     mesmo cliente outra obra -> registra em dedup-review.json, NAO mergeia.
     Por padrao tambem NAO carrega forte-match (e' 'restante' so' o que e' novo);
     --carregar-dups forca a carga mesmo assim.
  4. se passou no gate e nao e' forte-dup -> carrega com carregar_fato_supabase.py
     (fonte_leva=drive-53-pastas-2026-06, vintage derivado do data_base).

Cada pasta em try/except + timeout (subprocess) — se falhar/estourar:
  status=erro, motivo registrado, e CONTINUA pra proxima.

Saidas:
  _local/base-custos-historica/onda2-resultado.json  (1 entrada por pasta)
  _local/base-custos-historica/dedup-review.json      (overlaps vs 126+onda1)

Abre UMA linha em ingest_runs (running -> done) com as contagens agregadas.

ZERO escrita nas tabelas antigas. PYTHONIOENCODING=utf-8.

Uso:
    set PYTHONIOENCODING=utf-8
    py -3.10 scripts/custos_historica/processar_lote.py
    py -3.10 scripts/custos_historica/processar_lote.py --limit 5         # so' 5 (smoke)
    py -3.10 scripts/custos_historica/processar_lote.py --only-slug xpcon-aurun
    py -3.10 scripts/custos_historica/processar_lote.py --incluir-dups    # processa forte-match tb
    py -3.10 scripts/custos_historica/processar_lote.py --carregar-dups   # carrega forte-match tb
    py -3.10 scripts/custos_historica/processar_lote.py --dry-run         # nao escreve no Supabase
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import enumerar_pastas_custo as enum
from dotenv import dotenv_values
from supabase import create_client

BRT = timezone(timedelta(hours=-3))

REPO_ROOT = _HERE.parent.parent                      # .../orcamentos-openclaw
ENV_FILE = REPO_ROOT / ".env.indices-cartesian"

BASE_LOCAL = Path(r"C:\Users\leona\openclaw\_local\base-custos-historica")
STAGING = BASE_LOCAL / "staging"
RESULT_JSON = BASE_LOCAL / "onda2-resultado.json"
DEDUP_JSON = BASE_LOCAL / "dedup-review.json"

FONTE_LEVA = "drive-53-pastas-2026-06"
SCRIPT_VERSION = "processar_lote.py@v1"

TIMEOUT_POR_PASTA = 240          # s — selftest (discovery+parse+data) por pasta
TIMEOUT_LOAD = 180               # s — carregar_fato_supabase por slug
# Gate de reconciliacao pu*qtd vs total: deve fechar PERTO de 100%. Banda
# [95%, 105%]: abaixo = itens faltando/PU errado; MUITO acima (ex 2755%, 9e11%)
# = coluna misparseada (qtd lida como total, casas decimais, etc.) — extracao
# quebrada, NAO carregar.
RECONCILE_MIN = 95.0             # %
RECONCILE_MAX = 105.0            # %

PY = sys.executable              # py -3.10 atual

# Ja' carregados (126 base + onda1). Onda1 vem do enumerador; os 126 sao injetados
# em runtime (lidos do Supabase). Aqui so' a semente onda1 caso o DB esteja off.
ONDA1 = sorted(enum.JA_CARREGADOS)


# ---------------------------------------------------------------------------
# Supabase helpers
# ---------------------------------------------------------------------------

def conectar():
    if not ENV_FILE.exists():
        raise FileNotFoundError(f".env nao encontrado: {ENV_FILE}")
    env = dotenv_values(ENV_FILE)
    url = env.get("SUPABASE_URL")
    key = env.get("SUPABASE_SECRET_KEY")
    if not url or not key or str(key).startswith("COLE_AQUI"):
        raise RuntimeError("SUPABASE_URL/SUPABASE_SECRET_KEY ausentes no .env")
    return create_client(url, key)


def slugs_ja_carregados(client) -> list[str]:
    """SO os slugs ja carregados NESTA leva (fonte_leva drive) — idempotencia de re-run.
    Overlap com a base-2026-04 NAO conta: e' ENRICH (carrega a versao datada do Drive,
    coexiste via UNIQUE (slug, fonte_leva))."""
    refs = set(ONDA1)
    try:
        resp = (client.table("fato_projetos").select("slug")
                .eq("fonte_leva", FONTE_LEVA).execute())
        for r in (resp.data or []):
            if r.get("slug"):
                refs.add(r["slug"])
    except Exception as e:
        print(f"  ! aviso: nao consegui ler fato_projetos ({e}); uso so' onda1")
    return sorted(refs)


def abrir_run(client, params: dict) -> int:
    resp = client.table("ingest_runs").insert({
        "fonte_leva": FONTE_LEVA,
        "status": "running",
        "script_version": SCRIPT_VERSION,
        "params": params,
        "tabelas_afetadas": ["fato_projetos", "fato_itens", "fato_composicao_insumos"],
    }).execute()
    rid = resp.data[0]["id"]
    print(f"> ingest_runs aberto: run_id={rid} (running)")
    return rid


def fechar_run(client, run_id: int, n_proj: int, n_itens: int, n_insumos: int,
               status: str = "done"):
    client.table("ingest_runs").update({
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "n_projetos": n_proj,
        "n_itens": n_itens,
        "n_insumos": n_insumos,
    }).eq("id", run_id).execute()
    print(f"> ingest_runs fechado: run_id={run_id} status={status} "
          f"(proj={n_proj} itens={n_itens} insumos={n_insumos})")


def contar_leva(client) -> dict:
    """Contagens da leva drive (fonte_leva) nas tabelas novas."""
    out = {}
    for t in ("fato_projetos", "fato_itens", "fato_composicao_insumos"):
        try:
            resp = (client.table(t).select("id", count="exact")
                    .eq("fonte_leva", FONTE_LEVA).limit(1).execute())
            out[t] = resp.count if resp.count is not None else "?"
        except Exception as e:
            out[t] = f"erro:{e}"
    return out


# ---------------------------------------------------------------------------
# Dedup vs ja-carregados
# ---------------------------------------------------------------------------

def _cliente_token(slug: str) -> str:
    return slug.split("-")[0] if slug else ""


def classificar_dedup(slug: str, refs: list[str]) -> dict:
    """Compara slug novo vs refs (126+onda1). Retorna:
        {exato, forte, melhor_ref, ratio, candidatos[], mesmo_cliente[]}.
    Forte = exato OU SequenceMatcher>=0.7. NAO mergeia — so' classifica."""
    if slug in refs:
        return {"exato": True, "forte": True, "melhor_ref": slug, "ratio": 1.0,
                "candidatos": [{"ref_slug": slug, "tipo": "exato", "ratio": 1.0}],
                "mesmo_cliente": []}
    cli = _cliente_token(slug)
    cands = []
    melhor_ref, melhor = None, 0.0
    mesmo_cliente = []
    for r in refs:
        ratio = SequenceMatcher(None, slug, r).ratio()
        if ratio > melhor:
            melhor, melhor_ref = ratio, r
        if ratio >= 0.7:
            cands.append({"ref_slug": r, "tipo": "sequence", "ratio": round(ratio, 3)})
        if _cliente_token(r) == cli and cli:
            mesmo_cliente.append(r)
    cands.sort(key=lambda c: -c["ratio"])
    forte = bool(cands)
    return {"exato": False, "forte": forte, "melhor_ref": melhor_ref,
            "ratio": round(melhor, 3), "candidatos": cands[:5],
            "mesmo_cliente": sorted(set(mesmo_cliente))[:8]}


# ---------------------------------------------------------------------------
# Pipeline por pasta (subprocesso isolado + timeout)
# ---------------------------------------------------------------------------

def rodar_selftest(folder: str, slug: str) -> tuple[str, str]:
    """Roda run_selftest.py em subprocesso (timeout). Retorna (resultado, detalhe).
    resultado in {ok, timeout, erro}. Em 'ok' o staging/<slug>/manifest.json existe."""
    cmd = [PY, str(_HERE / "run_selftest.py"), folder, "--slug", slug]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=TIMEOUT_POR_PASTA, env=env,
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"timeout >{TIMEOUT_POR_PASTA}s"
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "")[-600:]
        return "erro", f"rc={proc.returncode}: {tail}"
    return "ok", ""


def ler_manifest(slug: str) -> dict | None:
    p = STAGING / slug / "manifest.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def avaliar_gate(manifest: dict) -> tuple[str, str, dict]:
    """Aplica o GATE. Retorna (decisao, motivo, metrics).
    decisao in {carregar, descartado, pendente-ocr}."""
    counts = manifest.get("counts", {})
    n_itens = counts.get("itens", 0)
    n_insumos = counts.get("insumos", 0)
    reconcile = manifest.get("reconcile") or {}
    pct = reconcile.get("pct")
    n_rec = reconcile.get("n", 0)
    status = manifest.get("status")
    metrics = {"n_itens": n_itens, "n_insumos": n_insumos,
               "reconcile_pct": pct, "reconcile_n": n_rec}

    # PDF sem tabela extraivel
    if status == "pendente-ocr":
        return "pendente-ocr", manifest.get("status_motivo") or "PDF sem tabela", metrics

    # Tipo B (fallback) cuja coluna total nao reconciliou no reparo: o parser ja
    # marcou pendente-revisao (nenhuma aba do workbook fechou pu*qtd~=total). NAO
    # carrega lixo nem chuta — fila de revisao manual de coluna.
    if status == "pendente-revisao":
        return "pendente-revisao", (manifest.get("status_motivo")
                                    or "coluna total nao reconciliou — revisar mapeamento"), metrics

    if n_itens == 0:
        return "descartado", "sem itens extraidos", metrics

    # Reconcile dentro da banda [95%, 105%] -> extracao saudavel, carrega
    if pct is not None and RECONCILE_MIN <= pct <= RECONCILE_MAX:
        return "carregar", f"reconcile {pct}% em [{RECONCILE_MIN},{RECONCILE_MAX}]%", metrics

    # Excecao 'orcamento so-folha': itens existem com total, mas o triple
    # pu/qtd/total quase nao aparece (n_rec ~0) — folha de servicos sem
    # composicao itemizada. Carrega documentado (a base ganha o total/grupo).
    # So' vale quando o reconcile NAO foi calculado em massa (n_rec baixo); se
    # n_rec e' alto e o pct estourou, e' misparse, nao folha.
    if n_rec == 0 and n_itens > 0:
        return "carregar", ("excecao orcamento-so-folha: itens com total mas sem "
                            "triple pu*qtd (n_reconcile=0) — carrega documentado"), metrics
    if 0 < n_rec < max(3, 0.10 * n_itens) and (pct is None or pct <= RECONCILE_MAX):
        return "carregar", (f"excecao orcamento-so-folha parcial: so' {n_rec}/{n_itens} "
                            f"itens tem triple pu*qtd — carrega documentado"), metrics

    # fora da banda (abaixo de 95% ou MUITO acima de 105%) e nao-excecao -> descarta
    if pct is not None and pct > RECONCILE_MAX:
        return "descartado", (f"reconcile {pct}% > {RECONCILE_MAX}% "
                              f"(n_reconcile={n_rec}/{n_itens}) — coluna misparseada, extracao quebrada"), metrics
    return "descartado", (f"reconcile {pct}% < {RECONCILE_MIN}% "
                          f"(n_reconcile={n_rec}/{n_itens}) — extracao suspeita"), metrics


def carregar_slug_subprocess(slug: str) -> tuple[bool, str, dict]:
    """Chama carregar_fato_supabase.py pro slug (timeout). Retorna (ok, detalhe, stats)."""
    cmd = [PY, str(_HERE / "carregar_fato_supabase.py"), slug]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=TIMEOUT_LOAD, env=env,
        )
    except subprocess.TimeoutExpired:
        return False, f"load timeout >{TIMEOUT_LOAD}s", {}
    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode != 0:
        return False, f"load rc={proc.returncode}: {out[-600:]}", {}
    # parse das contagens da linha de RESUMO do loader
    stats = _parse_loader_stats(out, slug)
    return True, "carregado", stats


def _parse_loader_stats(out: str, slug: str) -> dict:
    """Extrai itens_upserted/itens_novos/insumos_inseridos do stdout do loader."""
    import re
    stats = {"itens_upserted": 0, "itens_novos": 0, "insumos_inseridos": 0}
    m = re.search(r"itens_upserted=(\d+).*?itens_novos=(\d+).*?insumos_inseridos=(\d+)",
                  out, re.DOTALL)
    if m:
        stats["itens_upserted"] = int(m.group(1))
        stats["itens_novos"] = int(m.group(2))
        stats["insumos_inseridos"] = int(m.group(3))
    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Driver de lote (PASSO 2).")
    ap.add_argument("--limit", type=int, default=None, help="processa so' as N primeiras (smoke).")
    ap.add_argument("--only-slug", action="append", default=None, help="processa so' este(s) slug(s).")
    ap.add_argument("--pular-fuzzy", action="store_true",
                    help="NAO processa pastas com fuzzy-match (>=0.7) vs ja-carregados "
                         "(default: processa e carrega — slug novo = linhas novas, sem merge; "
                         "fuzzy so' vira flag em dedup-review). Match EXATO sempre e' pulado.")
    ap.add_argument("--dry-run", action="store_true", help="nao escreve no Supabase (so' staging+gate).")
    ap.add_argument("--root", default=str(enum.ROOT))
    args = ap.parse_args()

    BASE_LOCAL.mkdir(parents=True, exist_ok=True)
    STAGING.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    print(f"=== processar_lote — {datetime.now(BRT).isoformat(timespec='seconds')} ===")
    print(f"  staging: {STAGING}")
    print(f"  fonte_leva: {FONTE_LEVA}  | dry_run={args.dry_run}")

    # 1. enumerar
    print("\n[1/4] Enumerando pastas de custo de TOPO...")
    enr = enum.enumerar(Path(args.root))
    pastas = enr.get("pastas", [])
    print(f"  com conteudo: {len(pastas)}  | vazias: {enr.get('n_vazias')}  | "
          f"excluidas onda1: {enr.get('n_excluidas')}")

    if args.only_slug:
        sel = set(args.only_slug)
        pastas = [p for p in pastas if p["slug"] in sel]
        print(f"  filtro --only-slug -> {len(pastas)} pastas")
    if args.limit:
        pastas = pastas[: args.limit]
        print(f"  filtro --limit -> {len(pastas)} pastas")

    # 2. conectar + refs pra dedup
    client = None
    refs = list(ONDA1)
    run_id = None
    if not args.dry_run:
        print("\n[2/4] Conectando no Supabase...")
        client = conectar()
        refs = slugs_ja_carregados(client)
        print(f"  refs ja-carregados NESTA leva drive (idempotencia; base=ENRICH, NAO conta): {len(refs)}")
        import os as _os
        _skipf = r"C:\Users\leona\openclaw\_local\base-custos-historica\attempted-slugs.txt"
        if _os.path.exists(_skipf):
            with open(_skipf, encoding="utf-8") as _fh:
                _att = {l.strip() for l in _fh if l.strip()}
            refs = sorted(set(refs) | _att)
            print(f"  + skip-list de TENTADOS antes: {len(_att)} -> refs {len(refs)} (processa so o nao-tentado)")
        run_id = abrir_run(client, {
            "root": args.root, "n_enumeradas": len(pastas),
            "pular_fuzzy": args.pular_fuzzy,
            "staging_root": str(STAGING),
        })

    # 3. processar pasta a pasta
    print(f"\n[3/4] Processando {len(pastas)} pastas (timeout {TIMEOUT_POR_PASTA}s/pasta)...")
    resultados = []
    dedup_reviews = []
    agg = {"carregado": 0, "descartado": 0, "pendente-ocr": 0, "pendente-revisao": 0,
           "erro": 0, "dup-skip": 0, "timeout": 0}
    tot_itens = tot_insumos = tot_proj = 0

    for i, p in enumerate(pastas, 1):
        slug = p["slug"]
        folder = p["folder"]
        rec = {"slug": slug, "folder": folder, "cliente": p.get("cliente"),
               "obra": p.get("obra"), "status": None, "motivo": None,
               "n_itens": None, "n_insumos": None, "reconcile_pct": None,
               "data_base": None, "folder_tipo": None, "dedup": None}
        print(f"\n  [{i}/{len(pastas)}] {slug}")

        # dedup — classifica (NAO mergeia). Match EXATO de slug = ja-carregado de
        # verdade -> pular. Fuzzy (>=0.7) / mesmo-cliente = obra/safra distinta:
        # slug novo, gera LINHAS NOVAS (UNIQUE e' (slug,fonte_leva)), zero risco de
        # merge -> processa+carrega por padrao; so' vira flag de revisao humana.
        dd = classificar_dedup(slug, refs)
        rec["dedup"] = {"exato": dd["exato"], "fuzzy": dd["forte"] and not dd["exato"],
                        "melhor_ref": dd["melhor_ref"], "ratio": dd["ratio"]}
        if (dd["forte"] and not dd["exato"]) or dd["mesmo_cliente"]:
            dedup_reviews.append({
                "new_slug": slug, "folder": folder,
                "ratio": dd["ratio"],
                "candidatos": dd["candidatos"], "mesmo_cliente": dd["mesmo_cliente"],
                "acao": "REVISAR — nao forcar merge; obra/safra distinta provavel (processado normalmente)",
            })

        # match EXATO -> ja-carregado de verdade, pula
        if dd["exato"]:
            rec["status"] = "dup-skip"
            rec["motivo"] = f"slug EXATO ja-carregado ('{slug}') -> pulado"
            agg["dup-skip"] += 1
            print(f"      dup-skip (slug exato ja-carregado)")
            resultados.append(rec)
            continue

        # fuzzy + --pular-fuzzy -> pula extracao (opt-in)
        if dd["forte"] and args.pular_fuzzy:
            rec["status"] = "dup-skip"
            rec["motivo"] = (f"fuzzy-match vs '{dd['melhor_ref']}' (ratio={dd['ratio']}) "
                             f"-> --pular-fuzzy ativo, NAO processado")
            agg["dup-skip"] += 1
            print(f"      dup-skip fuzzy (match '{dd['melhor_ref']}' ratio={dd['ratio']}, --pular-fuzzy)")
            resultados.append(rec)
            continue

        # rodar pipeline (subprocesso + timeout)
        res, det = rodar_selftest(folder, slug)
        if res == "timeout":
            rec["status"] = "erro"; rec["motivo"] = det
            agg["erro"] += 1; agg["timeout"] += 1
            print(f"      ERRO timeout"); resultados.append(rec); continue
        if res == "erro":
            rec["status"] = "erro"; rec["motivo"] = det
            agg["erro"] += 1
            print(f"      ERRO {det[:120]}"); resultados.append(rec); continue

        manifest = ler_manifest(slug)
        if manifest is None:
            rec["status"] = "erro"; rec["motivo"] = "manifest ausente apos selftest"
            agg["erro"] += 1
            print("      ERRO manifest ausente"); resultados.append(rec); continue

        rec["folder_tipo"] = manifest.get("folder_tipo")
        rec["data_base"] = (manifest.get("data_base") or {}).get("data_base")

        decisao, motivo, metrics = avaliar_gate(manifest)
        rec["n_itens"] = metrics["n_itens"]
        rec["n_insumos"] = metrics["n_insumos"]
        rec["reconcile_pct"] = metrics["reconcile_pct"]
        rec["motivo"] = motivo

        if decisao == "pendente-ocr":
            rec["status"] = "pendente-ocr"; agg["pendente-ocr"] += 1
            print(f"      pendente-ocr — {motivo[:100]}")
            resultados.append(rec); continue
        if decisao == "pendente-revisao":
            rec["status"] = "pendente-revisao"
            agg["pendente-revisao"] = agg.get("pendente-revisao", 0) + 1
            print(f"      pendente-revisao — {motivo[:100]}")
            resultados.append(rec); continue
        if decisao == "descartado":
            rec["status"] = "descartado"; agg["descartado"] += 1
            print(f"      descartado — {motivo[:100]}")
            resultados.append(rec); continue

        # decisao == carregar
        if args.dry_run:
            rec["status"] = "ok-staging"
            print(f"      gate OK ({motivo[:70]}) [dry-run: nao carrega]")
            resultados.append(rec); continue

        ok, det_load, lstats = carregar_slug_subprocess(slug)
        if not ok:
            rec["status"] = "erro"; rec["motivo"] = f"gate OK mas load falhou: {det_load}"
            agg["erro"] += 1
            print(f"      ERRO load: {det_load[:120]}")
            resultados.append(rec); continue

        rec["status"] = "carregado"
        rec["load_stats"] = lstats
        agg["carregado"] += 1
        tot_proj += 1
        tot_itens += lstats.get("itens_novos", 0)
        tot_insumos += lstats.get("insumos_inseridos", 0)
        # adiciona o slug carregado aos refs (evita re-dup dentro da mesma leva)
        if slug not in refs:
            refs.append(slug)
        print(f"      CARREGADO itens_novos={lstats.get('itens_novos')} "
              f"insumos={lstats.get('insumos_inseridos')} (reconcile={rec['reconcile_pct']}%)")
        resultados.append(rec)

    # 4. gravar logs + fechar run
    print("\n[4/4] Gravando logs...")
    RESULT_JSON.write_text(json.dumps({
        "gerado_em": datetime.now(BRT).isoformat(timespec="seconds"),
        "fonte_leva": FONTE_LEVA,
        "run_id": run_id,
        "agg": agg,
        "totais_carregados": {"projetos": tot_proj, "itens_novos": tot_itens,
                              "insumos": tot_insumos},
        "pastas": resultados,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    DEDUP_JSON.write_text(json.dumps({
        "gerado_em": datetime.now(BRT).isoformat(timespec="seconds"),
        "fonte_leva": FONTE_LEVA,
        "criterio": ("match parcial de slug (SequenceMatcher>=0.7) OU mesmo cliente "
                     "(1o token) vs 126 base + onda1; NAO forcar merge."),
        "n_reviews": len(dedup_reviews),
        "reviews": dedup_reviews,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  -> {RESULT_JSON}")
    print(f"  -> {DEDUP_JSON}")

    if client is not None and run_id is not None:
        fechar_run(client, run_id, tot_proj, tot_itens, tot_insumos, status="done")

    leva = contar_leva(client) if client is not None else {}
    dt = time.time() - t0
    print("\n=== RESUMO ===")
    print(f"  agg: {agg}")
    print(f"  carregados nesta run: proj={tot_proj} itens_novos={tot_itens} insumos={tot_insumos}")
    if leva:
        print(f"  contagens leva drive no Supabase: {leva}")
    print(f"  tempo total: {dt/60:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())
