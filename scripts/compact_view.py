#!/usr/bin/env python3
"""Phase 2 helper — compact markdown view of a project's itens-detalhados.

Reads base/itens-detalhados/[projeto].json (which can be huge — 15k+ items)
and emits a structured ~10k-char markdown that Gemma can read reliably:
- project metadata (slug, AC, totals from existing JSON)
- per sheet: name, n_itens, total R$, top items table, observations
- pre-flagged outliers (PU > 3x median of same sheet)

Usage: python compact_view.py <slug>            # prints to stdout
       python compact_view.py <slug> -o <path>  # writes to file
       python compact_view.py --all-to <dir>    # writes all 126
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
DETALHADOS = BASE / "itens-detalhados"
INDICES = BASE / "indices-executivo"

TARGET_CHARS = 10000
TOP_ITEMS_PER_SHEET = 25
MAX_OBS_PER_SHEET = 12
MAX_SHEETS_FULL_DETAIL = 12
MAX_DESC_CHARS = 70

MINI_TOP_ITEMS_PER_SHEET = 8
MINI_MAX_SHEETS = 5
MINI_MAX_OBS_TOTAL = 15
MINI_DESC_CHARS = 55

RICH_TOP_ITEMS_PER_SHEET = 15
RICH_MAX_SHEETS = 8
RICH_MAX_OBS_TOTAL = 30
RICH_DESC_CHARS = 75
RICH_MAX_CHARS = 7500


def fmt_money(v) -> str:
    if v is None:
        return ""
    try:
        return f"{float(v):,.0f}".replace(",", ".")
    except Exception:
        return str(v)


def fmt_num(v) -> str:
    if v is None:
        return ""
    try:
        f = float(v)
        if f == int(f):
            return f"{int(f)}"
        return f"{f:.2f}"
    except Exception:
        return str(v)


def trunc(s, n=MAX_DESC_CHARS) -> str:
    if s is None:
        return ""
    s = str(s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def sheet_total(itens: list[dict]) -> float:
    s = 0.0
    for it in itens:
        v = it.get("total")
        if v is None:
            continue
        try:
            s += float(v)
        except Exception:
            pass
    return s


def detect_outliers(itens: list[dict]) -> set[int]:
    """Mark item indices whose PU is > 3x median of same sheet (above 100 R$)."""
    pus = []
    for it in itens:
        pu = it.get("pu")
        if pu is None:
            continue
        try:
            f = float(pu)
            if f > 0:
                pus.append(f)
        except Exception:
            pass
    if len(pus) < 5:
        return set()
    med = statistics.median(pus)
    threshold = med * 3
    out = set()
    for i, it in enumerate(itens):
        pu = it.get("pu")
        if pu is None:
            continue
        try:
            f = float(pu)
            if f > threshold and f > 100:
                out.add(i)
        except Exception:
            pass
    return out


def render_sheet(aba: dict, full_detail: bool) -> str:
    lines = []
    nome = aba.get("nome", "?")
    fonte = aba.get("fonte", "")
    n_itens = aba.get("n_itens", 0)
    itens = aba.get("itens", [])
    obs = aba.get("observacoes", [])
    total = sheet_total(itens)

    head = f"### {nome}"
    if fonte:
        head += f"  _(fonte: {fonte})_"
    lines.append(head)
    lines.append(f"itens={n_itens} | total=R$ {fmt_money(total)}")

    if not itens:
        if obs:
            lines.append("")
            lines.append("**observações:**")
            for o in obs[:MAX_OBS_PER_SHEET]:
                lines.append(f"- {trunc(o, 90)}")
        return "\n".join(lines)

    if not full_detail:
        return "\n".join(lines)

    sorted_itens = sorted(
        itens,
        key=lambda it: (float(it["total"]) if it.get("total") not in (None, "") else -1),
        reverse=True,
    )
    outliers = detect_outliers(itens)
    outlier_descs = {id(itens[i]): True for i in outliers}

    lines.append("")
    lines.append("**top itens (por total):**")
    lines.append("| desc | un | qtd | pu | total | seção |")
    lines.append("|---|---|---|---|---|---|")
    shown = 0
    for it in sorted_itens:
        if shown >= TOP_ITEMS_PER_SHEET:
            break
        desc = trunc(it.get("descricao"))
        if not desc:
            continue
        flag = " ⚠" if outlier_descs.get(id(it)) else ""
        lines.append(
            f"| {desc}{flag} | {trunc(it.get('unidade'), 8)} | {fmt_num(it.get('qtd'))} "
            f"| {fmt_num(it.get('pu'))} | {fmt_money(it.get('total'))} | {trunc(it.get('secao',''), 30)} |"
        )
        shown += 1

    secoes = []
    seen_sec = set()
    for it in itens:
        s = it.get("secao")
        if s and s not in seen_sec:
            seen_sec.add(s)
            secoes.append(s)
            if len(secoes) >= 20:
                break
    if secoes:
        lines.append("")
        lines.append(f"**seções identificadas ({len(seen_sec)} total):** " + " · ".join(trunc(s, 35) for s in secoes[:20]))

    if obs:
        lines.append("")
        lines.append("**observações:**")
        for o in obs[:MAX_OBS_PER_SHEET]:
            lines.append(f"- {trunc(o, 90)}")

    if outliers:
        lines.append("")
        lines.append(f"**{len(outliers)} itens com PU > 3x mediana sinalizados (⚠)**")

    return "\n".join(lines)


def is_aggregate_row(it: dict) -> bool:
    """Rows with only total filled (no qty AND no PU) are usually section sums."""
    has_qty = it.get("qtd") not in (None, "", 0)
    has_pu = it.get("pu") not in (None, "", 0)
    has_total = it.get("total") not in (None, "", 0)
    return has_total and not has_qty and not has_pu


def render_project_rich(slug: str) -> str:
    """Compact view RICA (~6-8k chars) — pra Fase 6 retry de projetos com <5 sub-disciplinas.

    Mais top-itens (15 vs 8), mais abas (8 vs 5), mais observações (30 vs 15),
    descrições mais longas (75 vs 55), aceita até 7500 chars (vs 4500).
    """
    detalhe_path = DETALHADOS / f"{slug}.json"
    if not detalhe_path.exists():
        return f"# {slug}\n\nERRO: itens-detalhados não encontrado."

    detalhe = json.loads(detalhe_path.read_text(encoding="utf-8"))
    abas = detalhe.get("abas", [])

    indices_path = INDICES / f"{slug}.json"
    indices_meta = {}
    if indices_path.exists():
        try:
            d = json.loads(indices_path.read_text(encoding="utf-8"))
            indices_meta = {"ac": d.get("ac"), "ur": d.get("ur"),
                            "total": d.get("total"), "rsm2": d.get("rsm2"),
                            "n_disciplinas": len(d.get("disciplinas", {}))}
        except Exception:
            pass

    out = [f"# {slug}"]
    if indices_meta.get("ac"):
        out.append(f"AC={fmt_num(indices_meta['ac'])}m² UR={indices_meta.get('ur') or '?'}")
        if indices_meta.get("rsm2"):
            out.append(f"R$/m² (existing): {fmt_num(indices_meta['rsm2'])}")
    out.append("")
    out.append(f"Abas total no xlsx: {len(abas)}")
    out.append("")

    abas_validas = []
    for aba in abas:
        itens = [it for it in aba.get("itens", []) if not is_aggregate_row(it)]
        if not itens:
            continue
        abas_validas.append((sheet_total(itens), aba, itens))
    abas_validas.sort(key=lambda x: x[0], reverse=True)

    seen_obs = set()
    obs_global: list[str] = []

    for idx, (tot, aba, itens) in enumerate(abas_validas[:RICH_MAX_SHEETS]):
        out.append(f"## {aba.get('nome','?')}  (R$ {fmt_money(tot)}, {len(itens)} itens)")
        sorted_itens = sorted(
            itens,
            key=lambda it: (float(it["total"]) if it.get("total") not in (None, "", 0) else -1),
            reverse=True,
        )
        for it in sorted_itens[:RICH_TOP_ITEMS_PER_SHEET]:
            desc = trunc(it.get("descricao"), RICH_DESC_CHARS)
            if not desc:
                continue
            parts = [desc]
            if it.get("unidade"):
                parts.append(str(it["unidade"]))
            if it.get("qtd"):
                parts.append(f"qtd={fmt_num(it['qtd'])}")
            if it.get("pu"):
                parts.append(f"pu={fmt_num(it['pu'])}")
            if it.get("total"):
                parts.append(f"R${fmt_money(it['total'])}")
            out.append("- " + " | ".join(parts))

        for o in aba.get("observacoes", [])[:8]:
            o = o.strip()
            key = o[:60].lower()
            if key not in seen_obs:
                seen_obs.add(key)
                obs_global.append(o)
        out.append("")

    if obs_global:
        out.append("## observações de orçamentista")
        for o in obs_global[:RICH_MAX_OBS_TOTAL]:
            out.append(f"- {trunc(o, 130)}")

    text = "\n".join(out)
    if len(text) > RICH_MAX_CHARS:
        text = text[:RICH_MAX_CHARS] + "\n…[trunc]"
    return text


def render_project_mini(slug: str) -> str:
    """3-4k char compact view targeting safe Gemma input size."""
    detalhe_path = DETALHADOS / f"{slug}.json"
    if not detalhe_path.exists():
        return f"# {slug}\n\nERRO: itens-detalhados não encontrado."

    detalhe = json.loads(detalhe_path.read_text(encoding="utf-8"))
    abas = detalhe.get("abas", [])

    indices_path = INDICES / f"{slug}.json"
    indices_meta = {}
    if indices_path.exists():
        try:
            d = json.loads(indices_path.read_text(encoding="utf-8"))
            indices_meta = {"ac": d.get("ac"), "ur": d.get("ur"), "total": d.get("total")}
        except Exception:
            pass

    out = [f"# {slug}"]
    if indices_meta.get("ac"):
        out.append(f"AC={fmt_num(indices_meta['ac'])}m² UR={indices_meta.get('ur') or '?'}")
    out.append("")

    abas_validas = []
    for aba in abas:
        itens = [it for it in aba.get("itens", []) if not is_aggregate_row(it)]
        if not itens:
            continue
        abas_validas.append((sheet_total(itens), aba, itens))
    abas_validas.sort(key=lambda x: x[0], reverse=True)

    seen_obs = set()
    obs_global: list[str] = []

    for idx, (tot, aba, itens) in enumerate(abas_validas[:MINI_MAX_SHEETS]):
        out.append(f"## {aba.get('nome','?')}  (R$ {fmt_money(tot)}, {len(itens)} itens)")
        sorted_itens = sorted(
            itens,
            key=lambda it: (float(it["total"]) if it.get("total") not in (None, "", 0) else -1),
            reverse=True,
        )
        for it in sorted_itens[:MINI_TOP_ITEMS_PER_SHEET]:
            desc = trunc(it.get("descricao"), MINI_DESC_CHARS)
            if not desc:
                continue
            parts = [desc]
            if it.get("unidade"):
                parts.append(str(it["unidade"]))
            if it.get("qtd"):
                parts.append(f"qtd={fmt_num(it['qtd'])}")
            if it.get("pu"):
                parts.append(f"pu={fmt_num(it['pu'])}")
            if it.get("total"):
                parts.append(f"R${fmt_money(it['total'])}")
            out.append("- " + " | ".join(parts))

        for o in aba.get("observacoes", [])[:5]:
            o = o.strip()
            key = o[:60].lower()
            if key not in seen_obs:
                seen_obs.add(key)
                obs_global.append(o)
        out.append("")

    if obs_global:
        out.append("## observações de orçamentista")
        for o in obs_global[:MINI_MAX_OBS_TOTAL]:
            out.append(f"- {trunc(o, 110)}")

    text = "\n".join(out)
    if len(text) > 4500:
        text = text[:4500] + "\n…[trunc]"
    return text


def render_project(slug: str) -> str:
    detalhe_path = DETALHADOS / f"{slug}.json"
    if not detalhe_path.exists():
        return f"# {slug}\n\nERRO: itens-detalhados não encontrado."

    detalhe = json.loads(detalhe_path.read_text(encoding="utf-8"))
    abas = detalhe.get("abas", [])
    total_itens = detalhe.get("total_itens", 0)

    indices_path = INDICES / f"{slug}.json"
    indices_meta = {}
    if indices_path.exists():
        try:
            d = json.loads(indices_path.read_text(encoding="utf-8"))
            indices_meta = {
                "ac": d.get("ac"),
                "ur": d.get("ur"),
                "total": d.get("total"),
                "rsm2": d.get("rsm2"),
                "n_disciplinas": len(d.get("disciplinas", {})),
            }
        except Exception:
            pass

    out = []
    out.append(f"# {slug}")
    out.append("")
    if indices_meta:
        out.append("## metadata")
        if indices_meta.get("ac"):
            out.append(f"- AC: {fmt_num(indices_meta['ac'])} m²")
        if indices_meta.get("ur"):
            out.append(f"- UR: {indices_meta['ur']} unidades")
        if indices_meta.get("total"):
            out.append(f"- total índices existentes: R$ {fmt_money(indices_meta['total'])}")
        if indices_meta.get("rsm2"):
            out.append(f"- R$/m² (índices): {fmt_num(indices_meta['rsm2'])}")
        if indices_meta.get("n_disciplinas"):
            out.append(f"- disciplinas pré-extraídas: {indices_meta['n_disciplinas']}")
        out.append("")
    out.append(f"## extração detalhada (Fase 1)")
    out.append(f"- abas: {len(abas)} | itens totais: {total_itens}")
    out.append("")

    abas_ordenadas = sorted(
        abas,
        key=lambda a: sheet_total(a.get("itens", [])),
        reverse=True,
    )

    out.append("## abas ordenadas por valor")
    for i, aba in enumerate(abas_ordenadas):
        full = i < MAX_SHEETS_FULL_DETAIL
        out.append("")
        out.append(render_sheet(aba, full_detail=full))

    text = "\n".join(out)
    if len(text) > TARGET_CHARS * 1.6:
        text = text[: int(TARGET_CHARS * 1.6)] + "\n\n…[truncado]"
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("-o", "--out", help="output file path")
    ap.add_argument("--all-to", help="render every project to this directory")
    ap.add_argument("--stats", action="store_true", help="just print size stats")
    ap.add_argument("--mini", action="store_true", help="use mini compact view (~3-4k chars)")
    args = ap.parse_args()

    render = render_project_mini if args.mini else render_project

    if args.all_to:
        out_dir = Path(args.all_to)
        out_dir.mkdir(parents=True, exist_ok=True)
        sizes = []
        for jp in sorted(DETALHADOS.glob("*.json")):
            slug = jp.stem
            txt = render(slug)
            (out_dir / f"{slug}.md").write_text(txt, encoding="utf-8")
            sizes.append((len(txt), slug))
        sizes.sort()
        print(f"wrote {len(sizes)} compact views to {out_dir}")
        if sizes:
            print(f"size: min={sizes[0][0]}  median={sizes[len(sizes)//2][0]}  max={sizes[-1][0]} ({sizes[-1][1]})")
        return

    if not args.slug:
        ap.error("slug required (or use --all-to)")

    txt = render(args.slug)
    if args.out:
        Path(args.out).write_text(txt, encoding="utf-8")
        print(f"wrote {len(txt)} chars -> {args.out}")
    elif args.stats:
        print(f"slug={args.slug}  chars={len(txt)}  lines={txt.count(chr(10))+1}")
    else:
        sys.stdout.write(txt)


if __name__ == "__main__":
    main()
