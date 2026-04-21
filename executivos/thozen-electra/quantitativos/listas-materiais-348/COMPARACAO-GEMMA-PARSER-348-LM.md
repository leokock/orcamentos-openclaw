# Comparativo - Extracao Gemma vs Parser Deterministico (lote 348_LM)

**Data:** 2026-04-15 00:05
**Fonte:** `quantitativos/listas-materiais-348/`
**Threshold needs_review:** divergencia > 10.0%

**PDFs analisados:** 21/21
**PDFs com divergencia > 10.0%:** 8

## Resumo por PDF

| Disciplina | PDF | Fmt | Parser | Gemma | Delta | Delta % | Review? |
|---|---|---|---:|---:|---:|---:|:---:|
| eletrico | `ele-acabamentos` | B | 100 | 100 | 0 | +0.0% | ok |
| eletrico | `ele-cabos-alim` | B | 15 | 15 | 0 | +0.0% | ok |
| eletrico | `ele-eletrocalhas` | B | 100 | 100 | 0 | +0.0% | ok |
| eletrico | `ele-enfiacoes` | B | 183 | 183 | 0 | +0.0% | ok |
| eletrico | `ele-iluminacoes` | B | 38 | 38 | 0 | +0.0% | ok |
| eletrico | `ele-tubulacoes` | B | 84 | 84 | 0 | +0.0% | ok |
| hidraulico | `hidro-conexoes` | A | 0 | 132 | 132 | +100.0% | FLAG |
| hidraulico | `hidro-ete` | A | 0 | 20 | 20 | +100.0% | FLAG |
| hidraulico | `hidro-tubulacoes` | A | 0 | 18 | 18 | +100.0% | FLAG |
| hidraulico | `hidro-valvulas` | A | 0 | 17 | 17 | +100.0% | FLAG |
| ppci-civil | `ppci-gerais` | A | 1 | 13 | 12 | +1200.0% | FLAG |
| ppci-civil | `ppci-igc` | A | 7 | 93 | 86 | +1228.6% | FLAG |
| ppci-civil | `ppci-mecanico` | A | 0 | 21 | 21 | +100.0% | FLAG |
| ppci-civil | `ppci-shp` | A | 1 | 30 | 29 | +2900.0% | FLAG |
| ppci-eletrico | `ppcie-acabamentos` | B | 131 | 131 | 0 | +0.0% | ok |
| ppci-eletrico | `ppcie-enfiacoes` | B | 52 | 52 | 0 | +0.0% | ok |
| ppci-eletrico | `ppcie-tubulacoes` | B | 81 | 81 | 0 | +0.0% | ok |
| spda | `spda-completo` | A | 61 | 59 | -2 | -3.3% | ok |
| telefonico | `tel-acabamentos` | B | 69 | 69 | 0 | +0.0% | ok |
| telefonico | `tel-eletrocalhas` | B | 18 | 18 | 0 | +0.0% | ok |
| telefonico | `tel-tubulacoes` | B | 69 | 69 | 0 | +0.0% | ok |

## PDFs flagged para revisao

Divergencia > 10% entre Gemma e parser pode indicar:
- Parser bug: format A com colunas nao previstas (ex: COD. extra)
- Gemma alucinacao / dedup incorreto
- PDF OCR ruim / encoding quebrado

Acao recomendada: reprocessar com `--model 26b` e reinspecionar manualmente o PDF.

### `hidro-conexoes` (hidraulico)
- Formato: A
- Parser: 0 itens
- Gemma:  132 itens
- Delta:  132 (+100.0%)
- Documentos: gemma=1 parser=1

### `hidro-ete` (hidraulico)
- Formato: A
- Parser: 0 itens
- Gemma:  20 itens
- Delta:  20 (+100.0%)
- Documentos: gemma=1 parser=1

### `hidro-tubulacoes` (hidraulico)
- Formato: A
- Parser: 0 itens
- Gemma:  18 itens
- Delta:  18 (+100.0%)
- Documentos: gemma=1 parser=1

### `hidro-valvulas` (hidraulico)
- Formato: A
- Parser: 0 itens
- Gemma:  17 itens
- Delta:  17 (+100.0%)
- Documentos: gemma=1 parser=1

### `ppci-gerais` (ppci-civil)
- Formato: A
- Parser: 1 itens
- Gemma:  13 itens
- Delta:  12 (+1200.0%)
- Documentos: gemma=1 parser=1

### `ppci-igc` (ppci-civil)
- Formato: A
- Parser: 7 itens
- Gemma:  93 itens
- Delta:  86 (+1228.6%)
- Documentos: gemma=1 parser=1

### `ppci-mecanico` (ppci-civil)
- Formato: A
- Parser: 0 itens
- Gemma:  21 itens
- Delta:  21 (+100.0%)
- Documentos: gemma=1 parser=1

### `ppci-shp` (ppci-civil)
- Formato: A
- Parser: 1 itens
- Gemma:  30 itens
- Delta:  29 (+2900.0%)
- Documentos: gemma=1 parser=1

## Agregado por disciplina

| Disciplina | PDFs | Total parser | Total gemma | Delta total |
|---|---:|---:|---:|---:|
| eletrico | 6 | 520 | 520 | +0 |
| hidraulico | 4 | 0 | 187 | +187 |
| ppci-civil | 4 | 9 | 157 | +148 |
| ppci-eletrico | 3 | 264 | 264 | +0 |
| spda | 1 | 61 | 59 | -2 |
| telefonico | 3 | 156 | 156 | +0 |
