#!/usr/bin/env python3
"""Orquestrador do Pacote Paramétrico + Preliminar.

Fluxo completo:
  1. Recebe briefing (slug, AC, UR, padrão, etc.)
  2. Gera GATE de validação (xlsx) com defaults dos similares
  3. Pausa pra Leo validar o gate manualmente
  4. Quando rodado com --continue, lê gate validado e gera:
     - Paramétrico V2 Híbrido (chama gerar_template_dinamico_v2.py)
     - Preliminar (chama gerar_executivo_auto.py) — renomeado de "executivo"
     - Memorial Word (chama gerar_memorial_pacote.py)
     - Relatório de validação (chama validar_pacote.py)
  5. Tudo salvo em uma pasta única: pacotes/[slug]/
  6. OBRIGATÓRIO: após gerar, sincronizar pro Drive compartilhado via
     scripts/sincronizar_parametrico_drive.py --slug {slug} --archive-old

Nomenclatura pós-Fase 19:
  - parametrico-{slug}.{xlsx,docx,pdf} — V2 Híbrido com override manual
  - preliminar-{slug}.{xlsx,docx,pdf} — calibrado com itens de referência
  - (NÃO mais "executivo-*")

Estado persistido em pacotes/[slug]/state.json.

Uso:
  # Etapa 1 — gerar gate
  python gerar_pacote.py --slug projeto-novo --ac 15000 --ur 90 --padrao alto

  # Etapa 2 — depois de validar o gate
  python gerar_pacote.py --slug projeto-novo --continue
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import gerar_gate_validacao  # noqa: E402
import gerar_executivo_auto  # noqa: E402
import gerar_memorial_pacote  # noqa: E402
import validar_pacote  # noqa: E402

BASE = Path.home() / "orcamentos-openclaw" / "base"
PACOTES = BASE / "pacotes"
PACOTES.mkdir(parents=True, exist_ok=True)

V2_SCRIPT = Path.home() / "orcamentos" / "scripts" / "gerar_template_dinamico_v2.py"


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def state_path(slug: str) -> Path:
    return PACOTES / slug / "state.json"


def load_state(slug: str) -> dict:
    p = state_path(slug)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def save_state(slug: str, state: dict) -> None:
    p = state_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def etapa_gate(slug: str, ac: float, ur: int | None, padrao: str | None) -> dict:
    pasta = PACOTES / slug
    pasta.mkdir(parents=True, exist_ok=True)

    gate_xlsx = pasta / f"gate-{slug}.xlsx"
    print(f"[gate] gerando {gate_xlsx}")
    gate_result = gerar_gate_validacao.gerar_gate(slug, ac, ur, padrao, str(gate_xlsx))

    state = {
        "slug": slug,
        "ac": ac,
        "ur": ur,
        "padrao": padrao,
        "etapa": "gate_gerado",
        "gate_xlsx": str(gate_xlsx),
        "gate_validado_xlsx": str(pasta / f"gate-{slug}-validado.xlsx"),
        "gate_result": gate_result,
        "ts_gate": now_iso(),
    }
    save_state(slug, state)

    print()
    print("=" * 70)
    print(f"GATE GERADO em: {gate_xlsx}")
    print("=" * 70)
    print()
    print("PRÓXIMO PASSO (humano):")
    print(f"  1. Abra: {gate_xlsx}")
    print(f"  2. Valide as decisões na aba GATE (ajuste dropdowns)")
    print(f"  3. Marque SIM/NÃO nas premissas e sub-disciplinas")
    print(f"  4. SALVE COMO: {pasta / f'gate-{slug}-validado.xlsx'}")
    print(f"  5. Rode novamente: python scripts/gerar_pacote.py --slug {slug} --continue")
    print()
    return state


def etapa_continue(slug: str) -> dict:
    state = load_state(slug)
    if not state:
        raise RuntimeError(f"Estado do pacote '{slug}' não encontrado. Rode primeiro sem --continue.")

    pasta = PACOTES / slug
    gate_validado = Path(state["gate_validado_xlsx"])
    if not gate_validado.exists():
        raise RuntimeError(
            f"Gate validado não encontrado em {gate_validado}.\n"
            f"Salve o gate como '{gate_validado.name}' antes de continuar."
        )

    ac = state["ac"]
    ur = state.get("ur")
    padrao = state.get("padrao")

    parametrico_xlsx = pasta / f"parametrico-{slug}.xlsx"
    print(f"[parametrico] gerando via V2 em {parametrico_xlsx}")
    if V2_SCRIPT.exists():
        cmd = [
            sys.executable, str(V2_SCRIPT),
            "--ac", str(ac),
            "--ur", str(ur or 0),
            "-o", str(parametrico_xlsx),
        ]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if r.returncode != 0:
                print(f"[parametrico] WARN: V2 retornou {r.returncode}: {r.stderr[:300]}")
                state["parametrico_status"] = "failed"
                state["parametrico_error"] = r.stderr[:500]
            else:
                state["parametrico_status"] = "done"
                state["parametrico_xlsx"] = str(parametrico_xlsx)
        except subprocess.TimeoutExpired:
            state["parametrico_status"] = "timeout"
        except Exception as e:
            state["parametrico_status"] = "exception"
            state["parametrico_error"] = str(e)
    else:
        print(f"[parametrico] WARN: V2 script não encontrado em {V2_SCRIPT}")
        state["parametrico_status"] = "skipped"

    parametrico_docx = pasta / f"parametrico-{slug}.docx"
    print(f"[parametrico-memorial] gerando {parametrico_docx}")
    try:
        mem_result = gerar_memorial_pacote.gerar(slug, "parametrico", parametrico_docx)
        state["parametrico_memorial_status"] = "done"
        state["parametrico_docx"] = str(parametrico_docx)
        state["parametrico_memorial_result"] = mem_result
    except Exception as e:
        print(f"[parametrico-memorial] ERR: {e}")
        state["parametrico_memorial_status"] = "exception"
        state["parametrico_memorial_error"] = str(e)

    preliminar_xlsx = pasta / f"preliminar-{slug}.xlsx"
    print(f"[preliminar] gerando {preliminar_xlsx}")
    try:
        exec_result = gerar_executivo_auto.gerar_executivo(
            slug=slug, ac=ac, ur=ur, padrao=padrao,
            gate_path=gate_validado, output=str(preliminar_xlsx),
        )
        state["preliminar_xlsx"] = str(preliminar_xlsx)
        state["preliminar_result"] = exec_result
        state["preliminar_status"] = "done"
        state["executivo_xlsx"] = str(preliminar_xlsx)
        state["executivo_result"] = exec_result
        state["executivo_status"] = "done"
    except Exception as e:
        print(f"[preliminar] FAIL: {e}")
        state["preliminar_status"] = "failed"
        state["preliminar_error"] = str(e)

    preliminar_docx = pasta / f"preliminar-{slug}.docx"
    if state.get("preliminar_status") == "done":
        print(f"[preliminar-memorial] gerando {preliminar_docx}")
        try:
            mem_result = gerar_memorial_pacote.gerar(slug, "executivo", preliminar_docx)
            state["preliminar_memorial_status"] = "done"
            state["preliminar_docx"] = str(preliminar_docx)
            state["preliminar_memorial_result"] = mem_result
            state["executivo_memorial_status"] = "done"
            state["executivo_docx"] = str(preliminar_docx)
        except Exception as e:
            print(f"[preliminar-memorial] ERR: {e}")
            state["preliminar_memorial_status"] = "exception"
            state["preliminar_memorial_error"] = str(e)

    relatorio_md = pasta / f"validacao-{slug}.md"
    print(f"[validacao] gerando {relatorio_md}")
    try:
        validar_pacote.validar(
            parametrico_path=Path(state.get("parametrico_xlsx", "")) if state.get("parametrico_xlsx") else None,
            executivo_path=preliminar_xlsx,
            ac=ac, ur=ur,
            output=relatorio_md,
        )
        state["relatorio_md"] = str(relatorio_md)
    except Exception as e:
        print(f"[validacao] FAIL: {e}")

    state["etapa"] = "completo"
    state["ts_completo"] = now_iso()
    save_state(slug, state)

    print()
    print("=" * 70)
    print(f"PACOTE COMPLETO — {slug}")
    print("=" * 70)
    print(f"  Pasta: {pasta}")
    print(f"  Paramétrico: {parametrico_xlsx} ({state.get('parametrico_status')})")
    print(f"  Preliminar:  {preliminar_xlsx} ({state.get('preliminar_status')})")
    print(f"  Validação:   {relatorio_md}")
    print(f"  State:       {state_path(slug)}")
    return state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--ac", type=float, default=None)
    ap.add_argument("--ur", type=int, default=None)
    ap.add_argument("--padrao", default=None)
    ap.add_argument("--continue", dest="continuar", action="store_true",
                    help="continuar pacote depois do gate validado")
    args = ap.parse_args()

    if args.continuar:
        etapa_continue(args.slug)
    else:
        if args.ac is None:
            ap.error("--ac obrigatório na primeira execução")
        etapa_gate(args.slug, args.ac, args.ur, args.padrao)


if __name__ == "__main__":
    main()
