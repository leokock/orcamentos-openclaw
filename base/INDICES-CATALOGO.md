# Catálogo de Índices Cartesian

_Gerado em 2026-04-14T13:03:07 via `scripts/gerar_catalogo_indices.py`_

## O que é

Catálogo navegável de **todos os índices** da base Cartesian V2 (pós-fase 19). Consolida em um único arquivo Excel o que estava espalhado em 5+ JSONs. Permite filtrar, ordenar e cross-referenciar índices por categoria, robustez estatística (n_projetos, cv) e faixa de valores.

**Planilha:** [INDICES-CATALOGO.xlsx](INDICES-CATALOGO.xlsx) — 677 KB, 10 abas

## Mapa das 10 abas

| # | Aba | N linhas | Fonte primária | Descrição |
|---|---|---|---|---|
| 1 | LEIA_ME | 1 | — | Este mapa + schema + exemplos de filtros |
| 2 | PROJETOS | 126 | padroes-classificados + indices-executivo | 126 projetos com padrão Gemma, AC, UR, R$/m² |
| 3 | CALIBRACAO_GLOBAL | 18 | calibration-indices.json | 18 macrogrupos global (sem segmentação de padrão) |
| 4 | CALIBRACAO_CONDICIONAL | 64 | calibration-condicional-padrao.json | 18 MGs × 5 padrões Gemma (economico→luxo) — fonte primária fase 18b |
| 5 | INDICES_DERIVADOS_V2 | 29 | base-indices-master.json:indices_derivados_v2 | 29 derivados: PU insumos, custo por MG, splits MO/Material |
| 6 | INDICES_ESTRUTURAIS | ~35 | calibration-indices.json | Consumos físicos (concreto, aço, fôrma), produto, instalações %, CI %, segmentos por porte |
| 7 | **PUS_CROSS_V1** | **1740** | base-pus-cartesian.json | **1.740 clusters COM lista de obras fonte** |
| 8 | PUS_CROSS_V2 | 4210 | itens-pus-agregados.json | **4.210 clusters** (mais cobertura) — SEM lista de obras |
| 9 | CURVA_ABC_MASTER | 126 | base-indices-master.json:curva_abc_master | Curva ABC por projeto (n itens, n curva A, valor total) |
| 10 | CROSS_INSIGHTS_GEMMA | varia | base-indices-master.json:cross_insights | Análises Gemma: famílias, lacunas, outliers, padrões, índices sugeridos |

## Schema das colunas numéricas

Convenção usada em todas as abas estatísticas:

- **`n`** — número de projetos ou observações que contribuíram
- **`min` / `max`** — extremos observados
- **`p10` / `p25` / `p75` / `p90`** — percentis
- **`mediana` (p50)** — valor típico (é o que a calibração V2 usa)
- **`media`** — aritmética (pode ser puxada por outliers)
- **`cv`** — coeficiente de variação (`<0.3` confiável, `>0.5` volátil)
- **`projetos_fonte`** — _só em PUS_CROSS_V1_ — lista de slugs separados por `;`

## Exemplos de filtros úteis

### 1. PUs robustos de concreto
Aba **PUS_CROSS_V2** → filtrar `key` contém "concreto" + `n_projetos ≥ 10` + `cv < 0.3`

### 2. Esquadrias: alto vs luxo
Aba **CALIBRACAO_CONDICIONAL** → filtrar `padrao ∈ {alto, luxo}` + `macrogrupo = Esquadrias`

### 3. Quais obras bancam o PU mediano de porcelanato?
Aba **PUS_CROSS_V1** → filtrar `descricao` contém "porcelanato" → coluna `projetos_fonte`

### 4. Projetos alto padrão
Aba **PROJETOS** → filtrar `padrao_gemma = alto` → ordenar por `rsm2` desc

### 5. Índices derivados mais confiáveis
Aba **INDICES_DERIVADOS_V2** → ordenar `n` desc → ignorar `n<5`

### 6. MGs com maior dispersão por padrão
Aba **CALIBRACAO_CONDICIONAL** → calcular `p90-p10` → ordenar desc

## Gaps conhecidos

- **PUS_CROSS_V2 (4.210 clusters) NÃO tem lista de projetos** — usa hash-based clustering (fase 10 v2) que não preservou fontes. Quando precisar rastrear obras, use **PUS_CROSS_V1 (1.740)** que tem a lista completa.
- Alguns MGs em **CALIBRACAO_CONDICIONAL** têm `n<3` pro bucket — script paramétrico cai no fallback global × PADRAO_MULTIPLIERS nesses casos
- **`custo_por_ur`** nos derivados tem apenas `n=2` — baixa confiança estatística
- Classe **`luxo`** em CALIBRACAO_CONDICIONAL tem 0 projetos (Gemma não encontrou luxo real na base Cartesian — ver fase 18)
- Campos `disciplinas` / `indices_consumo` / `split_mo_material` dentro de cada `indices-executivo/{slug}.json` estão majoritariamente vazios — os dados agregados estão nos arquivos `calibration-*`

## Como regenerar

```bash
cd ~/orcamentos-openclaw
python scripts/gerar_catalogo_indices.py
```

Sem argumentos — lê dinamicamente todos os JSONs da base e regenera `INDICES-CATALOGO.xlsx` + este MD. Deve rodar depois de qualquer update na base (nova calibração, novo projeto processado, nova fase Gemma).

## JSONs fonte

- `base/calibration-indices.json` — 18 MGs global + produto + estruturais + instalações + ci + segmentos
- `base/calibration-condicional-padrao.json` — 18 MGs × 5 padrões (fase 18b, fonte primária)
- `base/base-indices-master-2026-04-13.json` — consolidado 322 KB (derivados + curva ABC + cross insights)
- `base/itens-pus-agregados.json` — 4.210 clusters V2 (fase 10 v2)
- `base/base-pus-cartesian.json` — 1.740 clusters V1 com lista de projetos
- `base/padroes-classificados-consolidado.json` — labels Gemma fase 18 (125/126 projetos)
- `base/indices-executivo/*.json` — 126 arquivos por projeto
