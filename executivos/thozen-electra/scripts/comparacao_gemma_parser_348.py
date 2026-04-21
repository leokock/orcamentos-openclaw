"""Fase 2 do pipeline 348_LM: gera COMPARACAO-GEMMA-PARSER-348-LM.md.

Varre todos os {slug}.gemma.json e {slug}.parser.json em
`quantitativos/listas-materiais-348/` e compara:
- total de itens
- divergencia em %
- por documento (para formato B, onde cada doc = 1 pavimento)

PDFs com divergencia >10% sao marcados como needs_review. O relatorio serve
pra:
  1. Auditar qualidade Gemma vs parser deterministico
  2. Identificar PDFs que precisam reprocessar com gemma4:26b
  3. Documentar a extracao pro log-execucao.md

Uso: python scripts/comparacao_gemma_parser_348.py
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

JSON_DIR = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\quantitativos\listas-materiais-348")
OUT_MD = JSON_DIR / "COMPARACAO-GEMMA-PARSER-348-LM.md"

THRESH_REVIEW_PCT = 10.0  # divergencia > X% => needs_review


def carregar_pares() -> list[dict]:
    """Encontra todos os slug.gemma.json / slug.parser.json disponiveis."""
    pares = []
    for disc_dir in sorted(JSON_DIR.iterdir()):
        if not disc_dir.is_dir():
            continue
        for gemma_file in sorted(disc_dir.glob("*.gemma.json")):
            slug = gemma_file.stem.replace(".gemma", "")
            parser_file = gemma_file.parent / f"{slug}.parser.json"
            pares.append({
                "disciplina": disc_dir.name,
                "slug": slug,
                "gemma_path": gemma_file,
                "parser_path": parser_file if parser_file.exists() else None,
            })
    return pares


def comparar(par: dict) -> dict:
    try:
        g = json.loads(par["gemma_path"].read_text(encoding="utf-8"))
    except Exception as e:
        return {**par, "erro": f"leitura gemma falhou: {e}"}

    if not par["parser_path"]:
        return {
            **par,
            "gemma_n": g.get("total_itens", 0),
            "parser_n": None,
            "delta_pct": None,
            "needs_review": False,
            "nota": "parser nao processado",
        }

    try:
        p = json.loads(par["parser_path"].read_text(encoding="utf-8"))
    except Exception as e:
        return {**par, "erro": f"leitura parser falhou: {e}"}

    gn = g.get("total_itens", 0)
    pn = p.get("total_itens", 0)
    delta = gn - pn
    if pn > 0:
        delta_pct = (delta / pn) * 100.0
    else:
        delta_pct = None if gn == 0 else 100.0
    needs_review = delta_pct is not None and abs(delta_pct) > THRESH_REVIEW_PCT

    return {
        **par,
        "formato": g.get("formato"),
        "gemma_n": gn,
        "parser_n": pn,
        "delta": delta,
        "delta_pct": delta_pct,
        "needs_review": needs_review,
        "n_docs_gemma": len(g.get("documentos", [])),
        "n_docs_parser": len(p.get("documentos", [])),
    }


def escrever_md(resultados: list[dict]) -> None:
    lines = []
    lines.append("# Comparativo - Extracao Gemma vs Parser Deterministico (lote 348_LM)")
    lines.append("")
    lines.append(f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Fonte:** `quantitativos/listas-materiais-348/`")
    lines.append(f"**Threshold needs_review:** divergencia > {THRESH_REVIEW_PCT}%")
    lines.append("")

    # Agregados
    total_pdfs = len(resultados)
    processados = [r for r in resultados if "erro" not in r and r.get("gemma_n") is not None]
    needs_rev = [r for r in processados if r.get("needs_review")]
    lines.append(f"**PDFs analisados:** {len(processados)}/{total_pdfs}")
    lines.append(f"**PDFs com divergencia > {THRESH_REVIEW_PCT}%:** {len(needs_rev)}")
    lines.append("")
    lines.append("## Resumo por PDF")
    lines.append("")
    lines.append("| Disciplina | PDF | Fmt | Parser | Gemma | Delta | Delta % | Review? |")
    lines.append("|---|---|---|---:|---:|---:|---:|:---:|")
    for r in sorted(resultados, key=lambda x: (x.get("disciplina", ""), x.get("slug", ""))):
        if "erro" in r:
            lines.append(f"| {r['disciplina']} | {r['slug']} | - | - | - | - | - | ERRO: {r['erro']} |")
            continue
        gn = r.get("gemma_n")
        pn = r.get("parser_n")
        delta = r.get("delta")
        delta_pct = r.get("delta_pct")
        pct_str = f"{delta_pct:+.1f}%" if delta_pct is not None else "-"
        rev = "FLAG" if r.get("needs_review") else "ok"
        if r.get("nota"):
            rev = r["nota"]
        lines.append(f"| {r['disciplina']} | `{r['slug']}` | {r.get('formato','-')} | {pn if pn is not None else '-'} | {gn if gn is not None else '-'} | {delta if delta is not None else '-'} | {pct_str} | {rev} |")
    lines.append("")

    # Detalhe dos PDFs flagged
    if needs_rev:
        lines.append("## PDFs flagged para revisao")
        lines.append("")
        lines.append("Divergencia > 10% entre Gemma e parser pode indicar:")
        lines.append("- Parser bug: format A com colunas nao previstas (ex: COD. extra)")
        lines.append("- Gemma alucinacao / dedup incorreto")
        lines.append("- PDF OCR ruim / encoding quebrado")
        lines.append("")
        lines.append("Acao recomendada: reprocessar com `--model 26b` e reinspecionar manualmente o PDF.")
        lines.append("")
        for r in needs_rev:
            lines.append(f"### `{r['slug']}` ({r['disciplina']})")
            lines.append(f"- Formato: {r.get('formato')}")
            lines.append(f"- Parser: {r.get('parser_n')} itens")
            lines.append(f"- Gemma:  {r.get('gemma_n')} itens")
            lines.append(f"- Delta:  {r.get('delta')} ({r.get('delta_pct'):+.1f}%)")
            lines.append(f"- Documentos: gemma={r.get('n_docs_gemma')} parser={r.get('n_docs_parser')}")
            lines.append("")

    # Estatisticas agregadas por disciplina
    lines.append("## Agregado por disciplina")
    lines.append("")
    lines.append("| Disciplina | PDFs | Total parser | Total gemma | Delta total |")
    lines.append("|---|---:|---:|---:|---:|")
    por_disc: dict[str, dict] = {}
    for r in processados:
        d = r.get("disciplina", "?")
        por_disc.setdefault(d, {"pdfs": 0, "parser": 0, "gemma": 0})
        por_disc[d]["pdfs"] += 1
        por_disc[d]["parser"] += r.get("parser_n") or 0
        por_disc[d]["gemma"] += r.get("gemma_n") or 0
    for d in sorted(por_disc):
        agg = por_disc[d]
        delta = agg["gemma"] - agg["parser"]
        lines.append(f"| {d} | {agg['pdfs']} | {agg['parser']} | {agg['gemma']} | {delta:+d} |")
    lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"relatorio gravado: {OUT_MD}")


def main():
    pares = carregar_pares()
    resultados = [comparar(p) for p in pares]
    escrever_md(resultados)
    # Resumo stdout
    proc = [r for r in resultados if "erro" not in r]
    rev = [r for r in proc if r.get("needs_review")]
    print(f"{len(proc)} PDFs analisados, {len(rev)} flagged")


if __name__ == "__main__":
    main()
