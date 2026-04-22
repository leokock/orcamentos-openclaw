# Estrutura do Orçamento — Thozen Electra

> Painel mestre de progresso do orçamento executivo.
> Última atualização: **2026-04-21 23:46 BRT**
>
> Atualizar via: `python -X utf8 orcamento-parametrico/scripts/atualizar_painel.py`

## Resumo geral

- **Disciplinas totais:** 22
- **Processadas (quantitativos prontos):** 1/22 (4.5%)
- **Memorial preenchido:** 2/22 (9.1%)
- **Custo acumulado (só processadas):** **R$ 591.298,60**
- **Pendências totais:** 🔴 2 Alta · 🟡 4 Média · ⚪ 3 Baixa

## Legenda de status

| Ícone | Status | Significado |
|:---:|---|---|
| ⬜ | Template | Só `extracao.xlsx` gerada a partir do template — memorial ainda é stub |
| 📝 | Memorial | Memorial preenchido (análise das fórmulas feita) — falta gerar quantitativos.xlsx |
| ⏸️ | Aguarda outras | Memorial pronto MAS depende de varredura cross-disciplinas (processar por último) |
| ✅ | Processada | `quantitativos.xlsx` pronto com valores Electra + pendências sinalizadas |

## Status por disciplina

| # | Disciplina | Status | Memorial | Extração | Quantitativos | Total R$ | Pendências |
|---:|---|:---:|:---:|:---:|:---:|---:|:---:|
| 1 | [EPCs](04-disciplinas/EPCs/) | 📝 Memorial | ✅ (13.4 KB) | ✅ | ⬜ | — | — |
| 2 | [Canteiro](04-disciplinas/Canteiro/) | ✅ Processada | ✅ (12.6 KB) | ✅ | ✅ | R$ 591.298,60 | 🔴 2 · 🟡 4 · ⚪ 3 |
| 3 | [Controle tecnológico](04-disciplinas/Controle tecnológico/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 4 | [Esquadrias](04-disciplinas/Esquadrias/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 5 | [Estacas](04-disciplinas/Estacas/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 6 | [Fund. Rasa e Contenção](04-disciplinas/Fund. Rasa e Contenção/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 7 | [Estrutura e Escoramento](04-disciplinas/Estrutura e Escoramento/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 8 | [Impermeabilização](04-disciplinas/Impermeabilização/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 9 | [Louças e metais](04-disciplinas/Louças e metais/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 10 | [Piscina](04-disciplinas/Piscina/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 11 | [Equipamentos especiais](04-disciplinas/Equipamentos especiais/) | ⏸️ Aguarda outras | ✅ (25.0 KB) | ✅ | ⬜ | — | — |
| 12 | [Elétrico](04-disciplinas/Elétrico/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 13 | [Hidrossanitário](04-disciplinas/Hidrossanitário/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 14 | [PPCI](04-disciplinas/PPCI/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 15 | [Sprinklers](04-disciplinas/Sprinklers/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 16 | [Telecomunicação](04-disciplinas/Telecomunicação/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 17 | [Gás](04-disciplinas/Gás/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 18 | [Automação](04-disciplinas/Automação/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 19 | [Climatização](04-disciplinas/Climatização/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 20 | [Iluminação](04-disciplinas/Iluminação/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 21 | [Mobiliário](04-disciplinas/Mobiliário/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |
| 22 | [Bombeamento](04-disciplinas/Bombeamento/) | ⬜ Template | ⬜ stub | ✅ | ⬜ | — | — |

## Próximas ações sugeridas

**Prontas pra gerar quantitativos (memorial já pronto):**
- EPCs

**Aguardando análise das fórmulas (memorial stub):**
- Controle tecnológico
- Esquadrias
- Estacas
- Fund. Rasa e Contenção
- Estrutura e Escoramento
- Impermeabilização
- Louças e metais
- Piscina
- Elétrico
- Hidrossanitário
- ... (+9)

**⏸️ Aguardando outras disciplinas (processar por último):**
- Equipamentos especiais — depende de varredura cross-disciplinas (ver memorial)

## Workflow por disciplina

Para cada disciplina, seguir 3 passos em ordem:

1. **Analisar fórmulas** do `extracao.xlsx` → escrever `memorial.md` detalhado
   (regras de extração, fontes, dependências, pendências)
2. **Escrever script gerador** `gerar_quantitativos_{disciplina}.py` que lê `projeto.json`
   e produz `quantitativos.xlsx` com valores Electra fechados + pendências sinalizadas
3. **Rodar** e atualizar este painel via `atualizar_painel.py`

## Referências

- **Dados-fonte do projeto:** [00-projeto/](00-projeto/) (6 mds + projeto.json)
- **EAP:** [01-eap/](01-eap/)
- **Composições e insumos:** [02-composicoes-insumos/](02-composicoes-insumos/)
- **Orçamento resumo:** [03-orcamento-resumo/](03-orcamento-resumo/)
- **README geral:** [README.md](README.md)

