#!/usr/bin/env python3
"""Generates the final consolidated report after phases 1-3.

Reads:
  - base/itens-detalhados/*.json   (phase 1)
  - base/sub-disciplinas/*.json    (phase 2)
  - base/premissas/*.json          (phase 3)
  - base/phase{1,2,3}*.log.jsonl

Writes:
  - base/relatorio-consolidado-YYYY-MM-DD.md
"""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
ITENS = BASE / "itens-detalhados"
SUB = BASE / "sub-disciplinas"
PREMISSAS = BASE / "premissas"
INDICES = BASE / "indices-executivo"


def load_log(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except Exception:
                pass
    return out


def load_jsons(d: Path) -> list[dict]:
    if not d.exists():
        return []
    out = []
    for p in sorted(d.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            data["_slug"] = p.stem
            out.append(data)
        except Exception:
            pass
    return out


def section_phase1() -> str:
    items = load_jsons(ITENS)
    if not items:
        return "## Fase 1 — sem dados\n"
    total_itens = sum(d.get("total_itens", 0) for d in items)
    total_obs = sum(d.get("total_observacoes", 0) for d in items)
    total_abas = sum(len(d.get("abas", [])) for d in items)
    by_size = Counter()
    for d in items:
        n = d.get("total_itens", 0)
        if n >= 5000:
            by_size["5k+"] += 1
        elif n >= 1000:
            by_size["1k-5k"] += 1
        elif n >= 100:
            by_size["100-1k"] += 1
        elif n > 0:
            by_size["1-100"] += 1
        else:
            by_size["0"] += 1

    lines = [
        "## Fase 1 — Extração detalhada (Python)",
        "",
        f"- Projetos processados: **{len(items)}**",
        f"- Itens totais extraídos: **{total_itens:,}**".replace(",", "."),
        f"- Observações de orçamentista: **{total_obs:,}**".replace(",", "."),
        f"- Abas processadas: **{total_abas}**",
        "",
        "**Distribuição por tamanho:**",
    ]
    for k in ("5k+", "1k-5k", "100-1k", "1-100", "0"):
        lines.append(f"- {k} itens: {by_size.get(k, 0)}")

    top10 = sorted(items, key=lambda d: d.get("total_itens", 0), reverse=True)[:10]
    lines.append("")
    lines.append("**Top 10 projetos por contagem de itens:**")
    for d in top10:
        lines.append(f"- {d['_slug']}: {d.get('total_itens', 0):,} itens, {len(d.get('abas', []))} abas".replace(",", "."))

    lines.append("")
    return "\n".join(lines)


def section_phase2() -> str:
    items = load_jsons(SUB)
    log = load_log(BASE / "phase2-pipeline.log.jsonl")
    queue = []
    qp = BASE / "phase2-queue.json"
    if qp.exists():
        queue = json.loads(qp.read_text(encoding="utf-8"))

    if not items and not queue:
        return "## Fase 2 — não iniciada\n"

    by_status = Counter(p.get("status", "?") for p in queue)
    n_done = by_status.get("done", 0)

    total_sub = total_obs = total_pad = total_fora = 0
    durations = []
    for d in items:
        parsed = d.get("parsed", {})
        total_sub += len(parsed.get("sub_disciplinas") or [])
        total_obs += len(parsed.get("observacoes_relevantes") or [])
        total_pad += len(parsed.get("padroes_identificados") or [])
        total_fora += len(parsed.get("fora_da_curva") or [])
        if d.get("duration_s"):
            durations.append(d["duration_s"])

    lines = [
        "## Fase 2 — Análise qualitativa via Gemma (e4b)",
        "",
        f"- Projetos na fila: **{len(queue)}**",
        f"- Status: " + ", ".join(f"{k}={v}" for k, v in sorted(by_status.items(), key=lambda x: -x[1])),
        f"- Sub-disciplinas extraídas: **{total_sub}**",
        f"- Observações de orçamentista: **{total_obs}**",
        f"- Padrões identificados: **{total_pad}**",
        f"- Itens fora-da-curva: **{total_fora}**",
    ]
    if durations:
        avg = sum(durations) / len(durations)
        lines.append(f"- Tempo médio Gemma: **{avg:.1f}s/projeto**")
        lines.append(f"- Tempo total processado: {sum(durations)/60:.1f} min")
    lines.append("")

    failed = [p for p in queue if p.get("status") in ("failed", "parse_failed", "timeout")]
    if failed:
        lines.append(f"**Projetos com falha ({len(failed)}):**")
        for f in failed[:20]:
            err = (f.get("last_summary") or {}).get("error", "")
            lines.append(f"- {f['projeto']}: {f['status']} {err[:60]}")
        lines.append("")

    examples = sorted(items, key=lambda d: len(d.get("parsed", {}).get("sub_disciplinas") or []), reverse=True)[:3]
    if examples:
        lines.append("**3 projetos com mais sub-disciplinas:**")
        for d in examples:
            n = len(d.get("parsed", {}).get("sub_disciplinas") or [])
            lines.append(f"- {d['_slug']}: {n} sub-disciplinas")
        lines.append("")

    return "\n".join(lines)


def section_phase3() -> str:
    items = load_jsons(PREMISSAS)
    log = load_log(BASE / "phase3-pipeline.log.jsonl")
    queue = []
    qp = BASE / "phase3-queue.json"
    if qp.exists():
        queue = json.loads(qp.read_text(encoding="utf-8"))

    if not items and not queue:
        return "## Fase 3 — não iniciada\n"

    by_status = Counter(p.get("status", "?") for p in queue)
    total_prem = total_bdi = total_dec = 0
    for d in items:
        parsed = d.get("parsed", {})
        total_prem += len(parsed.get("premissas_tecnicas") or [])
        total_bdi += len(parsed.get("bdi_encargos") or [])
        total_dec += len(parsed.get("decisoes_consolidadas") or [])

    lines = [
        "## Fase 3 — Premissas / BDI / Tipologia de PDFs (Gemma e4b)",
        "",
        f"- PDFs processados: **{len(items)}**",
        f"- Status: " + ", ".join(f"{k}={v}" for k, v in sorted(by_status.items(), key=lambda x: -x[1])),
        f"- Premissas técnicas extraídas: **{total_prem}**",
        f"- BDI/Encargos identificados: **{total_bdi}**",
        f"- Decisões consolidadas: **{total_dec}**",
        "",
    ]
    return "\n".join(lines)


def section_artifacts() -> str:
    return """## Arquivos gerados

### Por projeto (em `~/orcamentos-openclaw/base/`)
- `itens-detalhados/[projeto].json` — Fase 1: extração completa de todas as linhas dos xlsx
- `sub-disciplinas/[projeto].json` — Fase 2: JSON da análise Gemma + raw response
- `sub-disciplinas-md/[projeto]-qualitativo.md` — Fase 2: relatório legível
- `premissas/[projeto].json` — Fase 3: JSON da análise de PDFs
- `premissas-md/[projeto]-premissas.md` — Fase 3: relatório legível
- `indices-executivo/[projeto].json` — original + chave `qualitative` mesclada

### Logs e estado
- `phase1-extract.log.jsonl`
- `phase2-pipeline.log.jsonl` + `phase2-queue.json`
- `phase3-pdf-extract.log.jsonl` + `phase3-pipeline.log.jsonl` + `phase3-queue.json`
- `compact-views/*.md` — entradas compactas para Gemma
- `pdfs-text/*.txt` — texto extraído dos PDFs

### Scripts (em `~/orcamentos-openclaw/scripts/`)
- `gemma_queue_init.py`
- `extract_itens_detalhados.py`
- `phase1_summary.py`
- `compact_view.py`
- `phase2_pipeline.py`
- `extract_pdf_text.py`
- `phase3_pipeline.py`
- `merge_qualitative.py`
- `final_report.py`
"""


def main():
    today = date.today().isoformat()
    out = [
        f"# Expansão de Índices Paramétricos — Relatório Consolidado",
        f"_Gerado em {today}_",
        "",
        "Pipeline multi-fase que enriqueceu a base de 126 orçamentos executivos com camada qualitativa via Gemma local (gemma4:e4b), sem custo de tokens API.",
        "",
        section_phase1(),
        section_phase2(),
        section_phase3(),
        section_artifacts(),
    ]
    out_path = BASE / f"relatorio-consolidado-{today}.md"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
