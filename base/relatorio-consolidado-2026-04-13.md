# Expansão de Índices Paramétricos — Relatório Consolidado
_Gerado em 2026-04-13_

Pipeline multi-fase que enriqueceu a base de 126 orçamentos executivos com camada qualitativa via Gemma local (gemma4:e4b), sem custo de tokens API.

## Fase 1 — Extração detalhada (Python)

- Projetos processados: **126**
- Itens totais extraídos: **333.751**
- Observações de orçamentista: **7.210**
- Abas processadas: **987**

**Distribuição por tamanho:**
- 5k+ itens: 27
- 1k-5k itens: 41
- 100-1k itens: 25
- 1-100 itens: 32
- 0 itens: 1

**Top 10 projetos por contagem de itens:**
- fonseca-empreendimentos-estoril: 15.953 itens. 32 abas
- pass-e-connect: 15.172 itens. 38 abas
- fg-blue-coast: 14.433 itens. 20 abas
- cn-brava-ocean: 11.798 itens. 3 abas
- nova-empreendimentos-domus: 11.521 itens. 21 abas
- amalfi-tramonti: 11.359 itens. 27 abas
- neuhaus-origem: 10.680 itens. 12 abas
- xpcon-porto-cerro: 9.744 itens. 28 abas
- xpcon-marena: 8.745 itens. 19 abas
- pavcor: 8.616 itens. 16 abas

## Fase 2 — Análise qualitativa via Gemma (e4b)

- Projetos na fila: **126**
- Status: done=126
- Sub-disciplinas extraídas: **761**
- Observações de orçamentista: **553**
- Padrões identificados: **269**
- Itens fora-da-curva: **22**
- Tempo médio Gemma: **87.9s/projeto**
- Tempo total processado: 184.6 min

**3 projetos com mais sub-disciplinas:**
- cn-brava-ocean: 14 sub-disciplinas
- santa-maria-unimed: 13 sub-disciplinas
- muller-empreendimentos-elleva: 10 sub-disciplinas

## Fase 3 — Premissas / BDI / Tipologia de PDFs (Gemma e4b)

- PDFs processados: **58**
- Status: done=58
- Premissas técnicas extraídas: **404**
- BDI/Encargos identificados: **34**
- Decisões consolidadas: **124**

## Arquivos gerados

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
