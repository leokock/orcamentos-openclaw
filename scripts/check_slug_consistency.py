#!/usr/bin/env python3
"""Phase 20n — Verifica consistencia de slugs entre parametrico e executivo.

Como referenciado no protocolo CLUSTER3-E-PARAMETRICO-RESUMO.md.

Uso:
    python scripts/check_slug_consistency.py            # relatorio geral
    python scripts/check_slug_consistency.py --pairs    # lista pares existentes
    python scripts/check_slug_consistency.py --orphan   # so listados sem par

Objetivo:
    1. Identificar paramétricos sem executivo correspondente (pacotes em andamento)
    2. Identificar executivos sem paramétrico (projetos legados)
    3. Identificar PARES potenciais (slugs similares) que precisam ser cross-referenced
    4. Gerar tabela de cross-reference sugerida
"""
from __future__ import annotations

import argparse
import json
import unicodedata
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
PAR_DIR = BASE / "pacotes"
IDX_DIR = BASE / "indices-executivo"
OUT_JSON = BASE / "slug-consistency-report.json"
OUT_MD = BASE / "SLUG-CONSISTENCY-REPORT.md"

SIMILARITY_THRESHOLD = 0.7  # slugs com similaridade >= 0.7 sao candidatos a match


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def similarity(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def listar_parametricos():
    if not PAR_DIR.exists():
        return []
    slugs = []
    for d in sorted(PAR_DIR.iterdir()):
        if not d.is_dir():
            continue
        state = d / "state.json"
        info = {"slug": d.name, "state_exists": state.exists()}
        if state.exists():
            try:
                s = json.loads(state.read_text(encoding="utf-8"))
                info.update({
                    "ac": s.get("ac"),
                    "padrao": s.get("padrao"),
                    "etapa": s.get("etapa"),
                    "gate_validado": bool(s.get("gate_validado_xlsx")),
                    "parametrico_ok": bool(s.get("parametrico_xlsx")),
                })
            except Exception:
                pass
        slugs.append(info)
    return slugs


def listar_executivos():
    slugs = []
    for f in sorted(IDX_DIR.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        slugs.append({
            "slug": d.get("projeto") or f.stem,
            "ac": d.get("ac"),
            "total": d.get("total"),
            "padrao_registrado": d.get("padrao"),
        })
    return slugs


def encontrar_matches(pars, execs):
    """Identifica pares: exact match, partial match, unmatched."""
    exact_matches = []
    partial_matches = []
    par_unmatched = []

    exec_slug_set = {e["slug"] for e in execs}

    for par in pars:
        pslug = par["slug"]
        if pslug in exec_slug_set:
            exact_matches.append({"par": par, "exec_slug": pslug, "similarity": 1.0})
            continue

        # Busca partial
        best = None
        best_sim = 0
        for ex in execs:
            s = similarity(pslug, ex["slug"])
            if s >= SIMILARITY_THRESHOLD and s > best_sim:
                best = ex
                best_sim = s

        if best:
            partial_matches.append({"par": par, "exec_slug": best["slug"],
                                    "exec_info": best, "similarity": round(best_sim, 3)})
        else:
            par_unmatched.append(par)

    # Executivos sem paramétrico
    par_slug_set = {p["slug"] for p in pars}
    exec_unmatched_orphans = [e for e in execs if e["slug"] not in par_slug_set]
    # Se tem partial_match, também é "orphan" em exato
    partial_exec_slugs = {pm["exec_slug"] for pm in partial_matches}
    exec_no_pair = [e for e in exec_unmatched_orphans if e["slug"] not in partial_exec_slugs]

    return {
        "exact_matches": exact_matches,
        "partial_matches": partial_matches,
        "parametricos_sem_exec": par_unmatched,
        "executivos_sem_par": exec_no_pair,
    }


def gerar_md(pars, execs, matches, out_path):
    lines = [
        "# Relatorio de Consistencia de Slug — Paramétrico ↔ Executivo",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Paramétricos na base:** {len(pars)} (`base/pacotes/`)",
        f"**Executivos na base:** {len(execs)} (`base/indices-executivo/`)",
        "",
        "---",
        "",
        "## Status atual",
        "",
        f"- ✓ Pares **exact match** (mesmo slug em ambos): **{len(matches['exact_matches'])}**",
        f"- ⚠ Pares **partial match** (slugs similares, possivelmente mesmo projeto): **{len(matches['partial_matches'])}**",
        f"- ✗ Paramétricos **sem executivo** (projetos em andamento): **{len(matches['parametricos_sem_exec'])}**",
        f"- ✗ Executivos **sem paramétrico** (projetos legados): **{len(matches['executivos_sem_par'])}**",
        "",
    ]

    if matches["exact_matches"]:
        lines += ["## ✓ Exact matches (pares válidos pra comparação)", "",
                  "| Slug | AC paramétrico | Padrão | Status |", "|---|---:|---|---|"]
        for m in matches["exact_matches"]:
            p = m["par"]
            lines.append(f"| `{p['slug']}` | {p.get('ac', 'N/D')} | {p.get('padrao', 'N/D')} | Pode rodar `comparar_param_exec.py --slug {p['slug']}` |")
        lines.append("")

    if matches["partial_matches"]:
        lines += ["## ⚠ Partial matches — REVISAR MANUALMENTE", "",
                  "Slugs similares em paramétrico e executivo. Podem ser:",
                  "- Mesmo projeto com slug divergente (renomear 1 dos 2 para casar)",
                  "- Projetos diferentes do mesmo cliente (não casar, deixar como estão)",
                  "",
                  "| Paramétrico | Executivo | Similaridade | Ação sugerida |",
                  "|---|---|---:|---|"]
        for m in matches["partial_matches"]:
            p = m["par"]
            lines.append(f"| `{p['slug']}` | `{m['exec_slug']}` | {m['similarity']:.2f} | Verificar se é o mesmo projeto |")
        lines.append("")

    if matches["parametricos_sem_exec"]:
        lines += ["## Paramétricos sem executivo (projetos em andamento)", "",
                  "| Slug | AC | Padrão | Etapa | Gate OK |",
                  "|---|---:|---|---|---|"]
        for p in matches["parametricos_sem_exec"]:
            lines.append(f"| `{p['slug']}` | {p.get('ac', 'N/D')} | {p.get('padrao', 'N/D')} | {p.get('etapa', 'N/D')} | {'✓' if p.get('gate_validado') else '—'} |")
        lines.append("")
        lines.append("**Ação:** quando executivo for fechado, **manter o MESMO slug** em `indices-executivo/{slug}.json` pra criar par rastreável.")
        lines.append("")

    if matches["executivos_sem_par"]:
        lines += ["## Executivos sem paramétrico — legado", "",
                  f"Total: {len(matches['executivos_sem_par'])} projetos. Não é problema — só não será possível medir erro paramétrico retroativo.",
                  ""]

    lines += ["---", "", "## Protocolo pra manter consistência",
              "",
              "Ao fechar um paramétrico:",
              "1. Registrar `slug` canônico no `state.json`",
              "2. **Reusar o mesmo slug** ao iniciar o executivo",
              "3. Rodar `python scripts/check_slug_consistency.py` periodicamente",
              "4. Quando houver par: rodar `python scripts/comparar_param_exec.py --slug X`",
              "",
              "Métrica de sucesso (de CLUSTER3-E-PARAMETRICO-RESUMO.md):",
              "- 1 par rastreável até 30/jun/2026",
              "- 5 pares até 31/dez/2026",
              "- 20 pares = modelo preditivo de erro viável",
              ""]

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", action="store_true", help="mostrar só pares existentes")
    ap.add_argument("--orphan", action="store_true", help="mostrar só orfaos")
    args = ap.parse_args()

    pars = listar_parametricos()
    execs = listar_executivos()
    matches = encontrar_matches(pars, execs)

    print(f"Paramétricos: {len(pars)}")
    print(f"Executivos: {len(execs)}")
    print(f"Exact matches: {len(matches['exact_matches'])}")
    print(f"Partial matches: {len(matches['partial_matches'])}")
    print(f"Parametricos sem exec: {len(matches['parametricos_sem_exec'])}")
    print(f"Executivos sem par: {len(matches['executivos_sem_par'])}")

    if args.pairs:
        print("\n=== EXACT MATCHES ===")
        for m in matches["exact_matches"]:
            print(f"  {m['par']['slug']}")
        print("\n=== PARTIAL MATCHES ===")
        for m in matches["partial_matches"]:
            print(f"  par={m['par']['slug']:<30}  exec={m['exec_slug']:<30}  sim={m['similarity']:.2f}")
        return

    if args.orphan:
        print("\n=== PARAMETRICOS SEM EXEC ===")
        for p in matches["parametricos_sem_exec"]:
            print(f"  {p['slug']}  (etapa={p.get('etapa', 'N/D')})")
        return

    # Relatorio completo
    OUT_JSON.write_text(json.dumps({
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_parametricos": len(pars), "n_executivos": len(execs),
        "exact_matches": matches["exact_matches"],
        "partial_matches": matches["partial_matches"],
        "parametricos_sem_exec": matches["parametricos_sem_exec"],
        "executivos_sem_par_count": len(matches["executivos_sem_par"]),
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    gerar_md(pars, execs, matches, OUT_MD)
    print(f"\nSalvo:")
    print(f"  {OUT_JSON}")
    print(f"  {OUT_MD}")


if __name__ == "__main__":
    main()
