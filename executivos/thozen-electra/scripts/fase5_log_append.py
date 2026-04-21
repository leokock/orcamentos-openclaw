"""Fase 5: gera o texto de append para log-execucao.md e (opcionalmente) aplica.

Le os dados agregados do pipeline 348_LM:
  - quantitativos/listas-materiais-348/process-summary.json
  - quantitativos/listas-materiais-348/COMPARACAO-GEMMA-PARSER-348-LM.md (para copiar tabela)
  - disciplinas/{eletrico,hidraulico,...}/*.lm348-r01.xlsx (lista dos xlsx gerados)

Gera a secao 28 do log-execucao.md no padrao das sessoes anteriores.

Uso:
    python scripts/fase5_log_append.py            # print na tela (dry-run)
    python scripts/fase5_log_append.py --apply    # da append no log-execucao.md
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

EXEC_DIR = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra")
JSON_DIR = EXEC_DIR / "quantitativos" / "listas-materiais-348"
DISC_DIR = EXEC_DIR / "disciplinas"
LOG_PATH = EXEC_DIR / "log-execucao.md"

DISC_OUT = {
    "eletrico":       ("eletrico",       "eletrico-electra-lm348-r01.xlsx"),
    "hidraulico":     ("hidraulico",     "hidraulico-electra-lm348-r01.xlsx"),
    "telefonico":     ("telefonico",     "telecomunicacoes-electra-lm348-r01.xlsx"),
    "ppci-civil":     ("pci-civil",      "ppci-civil-electra-lm348-r01.xlsx"),
    "ppci-eletrico":  ("pci-eletrico",   "ppci-eletrico-electra-lm348-r01.xlsx"),
    "spda":           ("spda",           "spda-electra-lm348-r01.xlsx"),
}


def gerar_secao() -> str:
    lines = []
    today = datetime.now().strftime("%d/%b/%Y").lower()
    lines.append(f"## 28. Processamento PDFs 348_LM via Gemma local ({today})")
    lines.append("")
    lines.append("**Contexto.** A equipe Eletrowatts entregou 21 PDFs novos de listas de")
    lines.append("materiais (`348_LM - ... - rev.00`) em `_Projetos_IA/thozen-electra/projetos/")
    lines.append("15. Listas de quantitativos/`. Complementam os 7 PDFs de `LM - Caixas e")
    lines.append("Quadros` processados na Secao 27 (mesmo dia). Cobertura: 6 disciplinas")
    lines.append("(Eletrico, Hidraulico, Telefonico, PPCI Civil, PPCI Eletrico, SPDA).")
    lines.append("")
    lines.append("**Objetivo.** Extrair cada PDF via Gemma local, organizar por pavimento")
    lines.append("canonico (TERREO->G1->...->COBERTURA) e gerar xlsx de incremento")
    lines.append("`{disciplina}-electra-lm348-r01.xlsx` pra cada disciplina afetada.")
    lines.append("")
    lines.append("### Pipeline")
    lines.append("")
    lines.append("1. **Fase 1 (Extracao Gemma).** Cada PDF foi lido e passado ao modelo")
    lines.append("   `gemma4:e4b` local via `scripts/gemma_extract_lm.py`. Dois formatos")
    lines.append("   detectados automaticamente:")
    lines.append("   - **Formato B (QT-MAT):** 12 PDFs. Cada pagina do PDF = 1 documento")
    lines.append("     Eletrowatts com LOCALIZACAO explicita (ex: `A) 01o PAVTO - TERREO`).")
    lines.append("     Enviado pagina-a-pagina pro Gemma; pavimento extraido do header.")
    lines.append("   - **Formato A (Eletrowatts manual):** 9 PDFs. Lista totalizada sem")
    lines.append("     pavimento. Processado em 1 chamada unica; pavimento resolvido depois.")
    lines.append("     Layouts diferentes detectados pelo prompt (A1-A5: com/sem COD.,")
    lines.append("     com/sem DIM., com/sem MARCA/REFERENCIA).")
    lines.append("")
    lines.append("2. **Fase 2 (Cross-check).** `scripts/comparacao_gemma_parser_348.py`")
    lines.append("   rodou o parser deterministico `parse_lista_materiais.py` nos mesmos")
    lines.append("   21 PDFs em paralelo e comparou totais de itens por PDF. Divergencia")
    lines.append("   > 10% dispara flag `needs_review` no relatorio.")
    lines.append("   Relatorio: `quantitativos/listas-materiais-348/COMPARACAO-GEMMA-PARSER-348-LM.md`")
    lines.append("")
    lines.append("3. **Fase 3 (Rateio por pavimento).** Pros 9 PDFs formato A sem pavimento")
    lines.append("   explicito, segundo pass Gemma (`scripts/gemma_rateio_pavimento.py`)")
    lines.append("   aplica heuristica tecnica por sistema (SPDA cobertura+descidas,")
    lines.append("   HIDRO-TUBOS prumada 70% TIPO, PPCI-SHP proporcional 32 pav, etc.)")
    lines.append("   distribuindo item-a-item entre (pavimento, torre). Resultado salvo em")
    lines.append("   `{slug}.rateio.json` com justificativa por linha.")
    lines.append("")
    lines.append("4. **Fase 4 (Geracao xlsx).** `scripts/gerar_lm348_xlsx.py` consome")
    lines.append("   `.gemma.json` + `.rateio.json` por disciplina e produz xlsx com 4 abas:")
    lines.append("   - **Por Pavimento** — itens ordenados canonico com subtotais por grupo")
    lines.append("   - **Flat por PDF** — itens na ordem original do PDF com rastreabilidade")
    lines.append("   - **Rateio** — justificativas das distribuicoes (so format A)")
    lines.append("   - **Resumo** — totais, contagens por pavimento, benchmark mediana")
    lines.append("")
    lines.append("### Sumario da extracao")
    lines.append("")

    # Carregar summary
    summary_path = JSON_DIR / "process-summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        elapsed_min = summary.get("elapsed_s", 0) / 60
        lines.append(f"- Modelo Gemma: `{summary.get('model', '?')}`")
        lines.append(f"- Tempo total batch: {elapsed_min:.0f} min")
        lines.append(f"- PDFs processados: {len(summary.get('results', []))}")
        lines.append("")
        lines.append("| PDF | Disc | Parser | Gemma | Delta |")
        lines.append("|---|---|---:|---:|---:|")
        for r in summary.get("results", []):
            pdf = r.get("pdf", "")[:50]
            pn = r.get("parser_n_itens", "-")
            gn = r.get("gemma_n_itens", "-")
            if isinstance(pn, int) and isinstance(gn, int) and pn > 0:
                delta = f"{(gn-pn)/pn*100:+.0f}%"
            else:
                delta = "-"
            lines.append(f"| `{pdf}` | {r.get('disciplina', '-')} | {pn} | {gn} | {delta} |")
        lines.append("")
    else:
        lines.append("_process-summary.json nao encontrado (batch ainda nao completou)_")
        lines.append("")

    # Lista de xlsx gerados
    lines.append("### Entregaveis (disciplinas/*/lm348-r01.xlsx)")
    lines.append("")
    for disc, (disc_dir, fname) in DISC_OUT.items():
        p = DISC_DIR / disc_dir / fname
        exists = "OK" if p.exists() else "PENDENTE"
        lines.append(f"- [{exists}] `disciplinas/{disc_dir}/{fname}`")
    lines.append("")

    # Comparacao com secao 27
    lines.append("### Escopo total (Secao 27 + Secao 28)")
    lines.append("")
    lines.append("- Secao 27: 7 PDFs (LM Caixas e Quadros) = 413 itens, disciplinas ELE/SPDA/TEL")
    lines.append("- Secao 28: 21 PDFs (348_LM) = ver tabela acima, 6 disciplinas cobertas")
    lines.append(f"- **Total Electra 14/abr:** 28 PDFs extraidos e catalogados por pavimento")
    lines.append("")
    lines.append("### Revisao Leo (next actions)")
    lines.append("")
    lines.append("- [ ] Abrir cada xlsx `lm348-r01` e conferir aba **Por Pavimento**")
    lines.append("- [ ] Conferir que subtotais por pavimento batem com o total de cada PDF")
    lines.append("- [ ] Validar as distribuicoes da aba **Rateio** nos 9 PDFs format A")
    lines.append("- [ ] Comparar R$/m2 AC do **Resumo** vs mediana da disciplina")
    lines.append("- [ ] Mesclar com as revisoes anteriores (r03, r01, etc) quando quiser")
    lines.append("  consolidar — lm348-r01 e um incremento autocontido")
    lines.append("- [ ] Reprocessar PDFs flagged `needs_review` (ver secao Cross-check do relatorio)")
    lines.append("")
    lines.append("### Scripts criados (versionados no openclaw)")
    lines.append("")
    lines.append("- `scripts/gemma_extract_lm.py` — wrapper Gemma com prompt A/B dinamico")
    lines.append("- `scripts/process_348_lm_pdfs.py` — orquestrador CLI com --resume")
    lines.append("- `scripts/gemma_rateio_pavimento.py` — rateio heuristico por sistema")
    lines.append("- `scripts/gerar_lm348_xlsx.py` — gerador xlsx comum 4 abas")
    lines.append("- `scripts/comparacao_gemma_parser_348.py` — cross-check report")
    lines.append("- `scripts/fase5_log_append.py` — este script")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Append direto no log-execucao.md")
    args = ap.parse_args()

    secao = gerar_secao()
    if args.apply:
        # Regra CLAUDE.md: append only, nunca edit
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write("\n")
            f.write(secao)
        print(f"[ok] appended na {LOG_PATH}")
    else:
        print(secao)


if __name__ == "__main__":
    main()
