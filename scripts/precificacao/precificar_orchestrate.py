"""Orquestrador CLI da precificação 3 fontes.

Encadeia as fases determinísticas (pool → candidates → resolver_cartesian → montar)
e marca quando o subagent codex (Aquos/Internet) precisa entrar.

USO TÍPICO (do bot Cartesiano):

  # 1. Descobrir candidatos a projeto-ref
  python scripts/precificacao/precificar_descoberta.py --client <cliente> --pretty
  # → bot pergunta no Slack, recebe escolha

  # 2. Coletar dumps MongoDB via MCP cartesian-mongodb (ver precificar_dump_mongo.py --protocol)
  # → bot escreve cartesian-raw/{buildings,purchase_orders_items_full,resources_batch*}.json

  # 3. Rodar orquestrador (fases determinísticas)
  python scripts/precificacao/precificar_orchestrate.py \\
    --slug alfa-colinas \\
    --proj-ref-xlsx "<path planilha PCI>" \\
    --proj-ref-xlsx "<path planilha sanit>" \\
    --proj-ref-xlsx "<path planilha tel>" \\
    --proj-ref-label Aquos \\
    --phases auto

  # 4. Bot orquestra subagent codex pra Aquos+Internet (fase 5)
  #    via tool sessions_spawn — ver precificar_resolver_subagent.py --print-prompt
  #    e salva match-aquos-resolved-{disc}.json / internet-{disc}.json em _tmp/

  # 5. Re-rodar orquestrador pra montar com Aquos+Internet preenchidos
  python scripts/precificacao/precificar_orchestrate.py \\
    --slug alfa-colinas --proj-ref-label Aquos --phases montar

Fases (--phases):
  pool         — só pools (Cartesian + Aquos)
  candidates   — só fuzzy candidates
  resolver     — só heurística Cartesian
  montar       — só montagem xlsx
  auto         — tudo até onde der (até montagem mesmo sem Aquos+Internet, gera xlsx só Cartesian)

Por padrão, escreve TUDO em `executivos/[slug]/_tmp/precificacao/` e
saída final em `executivos/[slug]/XX-precificacao-banco-de-dados/`.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from precificar_common import (
    discover_disciplinas, executivo_dir, tmp_dir,
)

SCRIPT_DIR = Path(__file__).resolve().parent


def run_step(label: str, cmd: list[str], dry_run: bool = False) -> int:
    """Executa step com prefix label. Retorna exit code."""
    print(f"\n>>> {label}")
    print(f"    $ {' '.join(cmd)}")
    if dry_run:
        print("    (dry-run)")
        return 0
    proc = subprocess.run(cmd, cwd=Path(__file__).resolve().parents[2])
    print(f"<<< exit={proc.returncode}")
    return proc.returncode


def _disc_from_xlsx_path(xlsx_path: Path) -> str | None:
    """Tenta inferir disc slug do nome do arquivo (PCI/Sanit/Telef/Elet/Hidro/Estrut)."""
    name = xlsx_path.stem.lower()
    if "pci" in name or "incendio" in name:
        return "pci"
    if "sanit" in name or "hidro" in name or "esgoto" in name or "agua" in name:
        return "sanitario"
    if "telef" in name or "telec" in name or "telecom" in name or "cabeam" in name:
        return "telecom"
    if "elet" in name or "elétri" in name:
        return "eletrico"
    if "estrut" in name:
        return "estrutura"
    return None


def phase_pool(slug: str, proj_ref_xlsx: list[str], dump_dir: str | None, dry_run: bool):
    """Pool Cartesian + Pool Aquos (1 por disciplina)."""
    # Pool Cartesian
    cmd = [sys.executable, str(SCRIPT_DIR / "precificar_pool_cartesian.py"), "--slug", slug]
    if dump_dir:
        cmd.extend(["--dump-dir", dump_dir])
    rc = run_step("Pool Cartesian", cmd, dry_run)
    if rc != 0:
        print(f"!! pool cartesian falhou ({rc}) — continuando assim mesmo")

    # Pool Aquos (1 por arquivo)
    for xlsx in proj_ref_xlsx or []:
        disc = _disc_from_xlsx_path(Path(xlsx))
        if not disc:
            print(f"!! não consegui inferir disciplina de {xlsx} — pulando")
            continue
        rc = run_step(
            f"Pool Aquos ({disc})",
            [sys.executable, str(SCRIPT_DIR / "precificar_pool_aquos.py"),
             "--slug", slug, "--xlsx", xlsx, "--disc", disc],
            dry_run,
        )


def phase_candidates(slug: str, dry_run: bool):
    return run_step(
        "Candidates fuzzy",
        [sys.executable, str(SCRIPT_DIR / "precificar_candidates.py"),
         "--slug", slug, "--disciplinas", "auto"],
        dry_run,
    )


def phase_resolver_cartesian(slug: str, dry_run: bool):
    return run_step(
        "Resolver Cartesian (heurístico)",
        [sys.executable, str(SCRIPT_DIR / "precificar_resolver_cartesian.py"), "--slug", slug],
        dry_run,
    )


def phase_montar(slug: str, proj_ref_label: str, out_tag: str, dry_run: bool):
    return run_step(
        f"Montar xlsx ({out_tag})",
        [sys.executable, str(SCRIPT_DIR / "precificar_montar.py"),
         "--slug", slug, "--proj-ref-label", proj_ref_label, "--out-tag", out_tag],
        dry_run,
    )


def check_subagent_outputs(slug: str) -> tuple[list[str], list[str]]:
    """Retorna (presentes, ausentes) de arquivos resolved Aquos/Internet."""
    tmp = tmp_dir(slug)
    discs = discover_disciplinas(slug)
    presentes = []
    ausentes = []
    for _, disc in discs:
        for prefix, label in (("match-aquos-resolved", "Aquos"), ("internet", "Internet")):
            p = tmp / f"{prefix}-{disc}.json"
            if p.exists() and p.stat().st_size > 10:
                presentes.append(f"{label}/{disc}")
            else:
                ausentes.append(f"{label}/{disc}")
    return presentes, ausentes


def main():
    ap = argparse.ArgumentParser(description="Orquestrador precificação 3 fontes")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--phases", default="auto",
                    choices=["pool", "candidates", "resolver", "montar", "auto"])
    ap.add_argument("--proj-ref-xlsx", action="append", default=[],
                    help="Path xlsx do projeto-ref (1 por disciplina; pode repetir)")
    ap.add_argument("--proj-ref-label", default="Aquos",
                    help="Label do projeto-ref nos headers do xlsx final")
    ap.add_argument("--out-tag", default="banco-de-dados",
                    help="Sufixo da pasta: XX-precificacao-<TAG>")
    ap.add_argument("--dump-dir", help="Path alternativo pro dump MongoDB (default: tmp/cartesian-raw/)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not executivo_dir(args.slug).exists():
        print(f"❌ executivos/{args.slug}/ não existe. Crie o pacote de quantitativos primeiro (REGRA #3).")
        sys.exit(1)

    print(f"=== Precificação 3 fontes: {args.slug} ===")
    print(f"   Fase: {args.phases}")
    print(f"   Projeto-ref: {args.proj_ref_label}")
    print(f"   Saída: executivos/{args.slug}/<XX>-precificacao-{args.out_tag}/")

    rc_max = 0
    if args.phases in ("pool", "auto"):
        phase_pool(args.slug, args.proj_ref_xlsx, args.dump_dir, args.dry_run)
    if args.phases in ("candidates", "auto"):
        rc = phase_candidates(args.slug, args.dry_run)
        rc_max = max(rc_max, rc)
    if args.phases in ("resolver", "auto"):
        rc = phase_resolver_cartesian(args.slug, args.dry_run)
        rc_max = max(rc_max, rc)

    # Antes de montar, reportar status do subagent (Aquos + Internet)
    if args.phases in ("montar", "auto"):
        presentes, ausentes = check_subagent_outputs(args.slug)
        if ausentes:
            print(f"\n⚠ Subagent ainda não rodou: {len(ausentes)} arquivos resolved ausentes:")
            for a in ausentes[:6]:
                print(f"    - {a}")
            if len(ausentes) > 6:
                print(f"    ... +{len(ausentes) - 6} ausentes")
            print("\n  → Bot deve rodar subagent codex (Aquos+Internet) antes de montar.")
            print(f"  → Ver `python scripts/precificacao/precificar_resolver_subagent.py --slug {args.slug} --disc <DISC> --target aquos --print-prompt`")
            print("\n  Montando com Cartesian APENAS (Aquos+Internet em branco).")
        rc = phase_montar(args.slug, args.proj_ref_label, args.out_tag, args.dry_run)
        rc_max = max(rc_max, rc)

    sys.exit(rc_max)


if __name__ == "__main__":
    main()
