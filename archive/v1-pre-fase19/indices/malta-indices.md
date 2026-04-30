# Malta Residence — Índices de Orçamento Executivo

> Projeto: Nova Empreendimentos | Local: Florianópolis/SC | Data-base: Agosto/2025
> Extraído em: 06/03/2026 | Fonte: XLSX + PDF executivo

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Malta Residence — Nova Empreendimentos | — |
| Código CTN | — | N/D | — |
| Revisão | — | R00 | — |
| Localização | — | Florianópolis/SC | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Nova Empreendimentos | — |
| Área do Terreno | AT | 1.182,72 | m² |
| Área Construída | AC | **7.964,40** | m² |
| Unid. Habitacionais | UR_H | N/D | un |
| Unid. Comerciais | UR_C | N/D | un |
| Estúdios | UR_E | N/D | un |
| Total Unidades | UR | N/D | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | **2** | un (sociais) |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | **~35** | meses |
| Data-base | — | **Agosto/2025** | — |
| **CUB na Data-base** | — | **R$ 2.978,02** | **R$** |
| R$/m² Total | — | **6.091,06** | R$/m² |
| R$/m² Direto (sem ADM) | — | **3.798,44** | R$/m² |
| CUB ratio Total | — | **2,05** | CUB |
| CUB ratio Direto | — | **1,28** | CUB |
| Tipo de Laje | — | **Treliçada TR8/TR16 + Maciça** | — |
| Tipo de Fundação | — | **Hélice contínua + Estaca raiz + Blocos** | — |
| Tipo de Contenção | — | **Estaca raiz 31cm + Cortinas** | — |
| Padrão Acabamento | — | **Médio-alto** | — |

### Estrutura de Custos do Executivo

> **Essencial para normalização correta** — ADM e MOE podem inflar ou distorcer macrogrupos.

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | **Sim** | Terreno + comissões + taxas |
| Valor ADM (se separado) | **R$ 18.259.356,47** | **37,64%** do total |
| **Tem MOE (Mão de Obra) separado?** | **Sim** | Por etapa, aba "3 - MOE" |
| Valor MOE (se separado) | **R$ 9.674.933,29** | **31,98%** dos custos diretos |
| Metodologia de rateio MOE | — | Somado ao MAT por célula construtiva |
| Custos diretos de obra (sem ADM/MOE) | **R$ 30.252.288,33** | **62,36%** do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| CANTEIRO DE OBRAS | 1-Gerenciamento | Custo direto obra (não ADM incorporadora) |
| MOVIMENTAÇÃO DE TERRA | 2-Mov.Terra | — |
| FUNDAÇÕES + INFRAESTRUTURA + CONTENÇÕES | 3-Infraestrutura | Agrupado |
| SUPRAESTRUTURA | 4-Supraestrutura | — |
| ALVENARIAS E VEDAÇÕES | 5-Alvenaria | — |
| IMPERMEABILIZAÇÕES E TRATAMENTOS | 6-Impermeabilização | — |
| INSTALAÇÕES HIDRO + ELÉTR + TELECOM + GÁS | 7-Instalações | Agrupado (4 disciplinas) |
| ELEVADORES E PLATAFORMAS | 8-Sist.Especiais | — |
| INSTALAÇÕES CLIMATIZAÇÃO | 9-Climatização | — |
| REVESTIMENTOS DE ARGAMASSA | 10-Rev.Int.Parede | — |
| FORROS | 11-Teto | — |
| REVESTIMENTOS CERÂMICOS | 12-Pisos | — |
| PINTURAS | 13-Pintura | — |
| ESQUADRIAS | 14-Esquadrias | — |
| LOUÇAS E METAIS | 15-Louças e Metais | — |
| ACABAMENTOS EM FACHADA | 16-Fachada | MOE separado |
| ÁREAS COMUNS + PAISAGISMO + COMPLEMENTARES + LIMPEZA | 17-Complementares | Agrupado (6 células) |
| FUNDO RESERVA | 18-Imprevistos | — |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Os 18 macrogrupos padrão da base paramétrica Cartesian.

| # | Macrogrupo | Valor (R$) | R$/m² | R$/m² norm | % | Faixa Obras Similares |
|---|---|---|---|---|---|---|
| 1 | Gerenciamento | 1,011,755.34 | 127.03 | 117.42 | 3.34% | 348 - 522 |
| 2 | Mov. Terra | 548,050.79 | 68.81 | 63.61 | 1.81% | 10 - 15 |
| 3 | Infraestrutura | 2,580,123.39 | 323.96 | 299.44 | 8.53% | 158 - 237 |
| 4 | Supraestrutura | 6,806,829.78 | 854.66 | 789.98 | 22.50% | 568 - 852 |
| 5 | Alvenaria | 1,774,388.96 | 222.79 | 205.93 | 5.87% | 115 - 173 |
| 6 | Impermeabilização | 1,002,774.02 | 125.91 | 116.38 | 3.31% | 52 - 78 |
| 7 | Instalações | 3,184,557.79 | 399.85 | 369.59 | 10.53% | 285 - 428 |
| 8 | Sist. Especiais | 586,983.60 | 73.70 | 68.12 | 1.94% | 127 - 190 |
| 9 | Climatização | 648,665.24 | 81.45 | 75.28 | 2.14% | 33 - 50 |
| 10 | Rev. Int. Parede | 3,300,702.10 | 414.43 | 383.07 | 10.91% | 110 - 164 |
| 11 | Teto | 603,138.70 | 75.73 | 70.00 | 1.99% | 54 - 81 |
| 12 | Pisos | 1,626,850.38 | 204.27 | 188.81 | 5.38% | 158 - 236 |
| 13 | Pintura | 994,560.42 | 124.88 | 115.43 | 3.29% | 94 - 141 |
| 14 | Esquadrias | 3,292,806.36 | 413.44 | 382.16 | 10.88% | 226 - 338 |
| 15 | Louças e Metais | 228,396.87 | 28.68 | 26.51 | 0.75% | N/D |
| 16 | Fachada | 204,769.74 | 25.71 | 23.77 | 0.68% | 111 - 166 |
| 17 | Complementares | 1,576,421.94 | 197.93 | 182.96 | 5.21% | 142 - 213 |
| 18 | Imprevistos | 280,512.91 | 35.22 | 32.56 | 0.93% | N/D |
| — | **TOTAL DIRETO** | **30,252,288.33** | **3798.44** | **—** | **100%** | — |

> **Nota ADM:** O total acima NÃO inclui ADM da incorporadora (R$ 18.259.356,47 = terreno + comissões + taxas). Para CUB ratio total (2,05), somar o ADM. Para calibração paramétrica, usar apenas os custos diretos (CUB ratio 1,28).

> **Nota MOE:** Mão de obra separada na aba "3 - MOE" foi somada ao material (aba "2 - MAT") em cada célula construtiva. Total MOE = R$ 9.674.933,29 (31,98% dos custos diretos).

> **Nota Fachada:** Valor muito baixo (R$ 204.769,74) porque a maior parte do revestimento de fachada está em "REVESTIMENTOS DE ARGAMASSA" (R$ 3.300.702,10). Possível subdivisão diferente no executivo — chapisco + reboco externo classificado como revestimento interno.

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

> **Dados não disponíveis** — o executivo não fornece breakdown detalhado de volumes de concreto, aço, forma por elemento. Apenas totais por célula construtiva.

### 4.1 Supraestrutura

| Item | Valor |
|---|---|
| Total Supraestrutura | R$ 6.806.829,78 |
| MAT | R$ 4.291.347,13 |
| MOE | R$ 2.515.482,66 |
| R$/m² AC | R$ 854,66 |
| R$/m² norm (dez/23) | R$ 789,98 |

### 4.2 Infraestrutura

| Item | Valor |
|---|---|
| **Fundações** | R$ 2.182.516,99 |
| - MAT | R$ 2.182.516,99 |
| - MOE | R$ 0,00 (embutido no MAT) |
| **Infraestrutura (MOE)** | R$ 241.873,33 |
| **Contenções** | R$ 155.733,06 |
| - MAT | R$ 58.983,73 |
| - MOE | R$ 96.749,33 |
| **Total Infraestrutura** | **R$ 2.580.123,39** |
| R$/m² AC | R$ 323,96 |
| R$/m² norm (dez/23) | R$ 299,44 |

> **Observação:** Tipo de fundação: Hélice contínua + Estaca raiz + Blocos. Contenção: Estaca raiz 31cm + Cortinas.

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> **Dados não disponíveis** — o executivo fornece valores totais, não quantitativos detalhados por m²/m² AC.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | Origem |
|---|---|---|---|---|
| Hidrossanitárias | 1.552.168,62 | 194,88 | 48,74% | INSTALAÇÕES HIDROSSANITÁRIAS |
| Elétricas + SPDA | 1.343.553,96 | 168,69 | 42,19% | INSTALAÇÕES ELÉTRICAS, TELEFÔNICAS E SPDA |
| Telecom / CFTV | 234.955,20 | 29,50 | 7,38% | INSTALAÇÕES TELECOMUNICAÇÕES / CFTV |
| Gás (GLP) | 53.880,00 | 6,77 | 1,69% | INSTALAÇÕES GÁS |
| **TOTAL** | **3.184.557,79** | **399,85** | **100%** | — |

> **Nota:** Valores acima incluem MAT + MOE somados. MOE das instalações foi distribuído proporcionalmente entre Hidro e Elétrica (R$ 483.746,66 cada) conforme aba "3 - MOE".

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| REVESTIMENTOS DE ARGAMASSA | 3.300.702,10 | 414,43 |
| - MAT | 829.724,14 | 104,18 |
| - MOE | 2.470.977,96 | 310,25 |

> **Observação:** MOE de revestimento é 2,98x o material — indicativo de que o MOE está sendo cotado separadamente (não embutido no PU). Valor muito acima da mediana (R$ 136,95/m²) porque inclui fachada.

### 7.2 Pisos

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| REVESTIMENTOS CERÂMICOS | 1.626.850,38 | 204,27 |
| - MAT | 804.481,05 | 101,03 |
| - MOE | 822.369,33 | 103,24 |

### 7.3 Teto

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| FORROS | 603.138,70 | 75,73 |
| - MAT | 603.138,70 | 75,73 |
| - MOE | 0,00 | 0,00 |

### 7.4 Pintura

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| PINTURAS | 994.560,42 | 124,88 |
| - MAT | 396.310,70 | 49,77 |
| - MOE | 598.249,72 | 75,11 |

### 7.5 Fachada

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| ACABAMENTOS EM FACHADA | 204.769,74 | 25,71 |
| - MAT | 0,00 | 0,00 |
| - MOE | 204.769,74 | 25,71 |

> **Alerta:** Valor de fachada muito abaixo da mediana (R$ 138,51/m²). Possível razão: a maior parte do revestimento externo está classificado em "REVESTIMENTOS DE ARGAMASSA" (R$ 414,43/m² — 3x a mediana de Rev. Int. Parede).

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| ESQUADRIAS | 3.292.806,36 | 413,44 |
| - MAT | 3.196.057,03 | 401,28 |
| - MOE | 96.749,33 | 12,15 |

> **Observação:** Valor acima da mediana (R$ 282,08/m²) em 46,5%. Possível indicativo de padrão de esquadrias mais alto (alumínio + vidro temperado) ou área envidraçada maior.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| ELEVADORES E PLATAFORMAS | 586.983,60 | 73,70 |
| - MAT | 586.983,60 | 73,70 |
| - MOE | 0,00 | 0,00 |
| **PU por elevador** | **R$ 293.491,80** | **(2 elevadores sociais)** |

> **Observação:** Valor abaixo da mediana de Sist. Especiais (R$ 158,64/m²) porque não inclui outros sistemas (gerador, pressurização, automação, CFTV além do básico).

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Gerenciamento (Custo Direto de Obra)

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| CANTEIRO DE OBRAS | 1.011.755,34 | 127,03 |
| - MAT | 915.006,01 | 114,88 |
| - MOE | 96.749,33 | 12,15 |

> **Observação:** Valor abaixo da mediana de Gerenciamento (R$ 435,10/m²) porque NÃO inclui:
> - Projetos (incluídos na aba "1 - ADM")
> - Taxas e licenças (incluídos na aba "1 - ADM")
> - Equipe ADM (incluída na aba "1 - ADM")
> 
> O valor de R$ 127,03/m² refere-se apenas ao canteiro físico (equipamentos, consumíveis, segurança).

### 10.2 ADM Incorporadora (NÃO entra nos custos diretos)

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| AQUISIÇÃO DO TERRENO | 7.736.011,06 | 971,29 |
| ETAPAS INICIAIS [ADM INDIRETAS] | 10.523.345,41 | 1.321,29 |
| - Comissão venda | 2.253.378,22 | 282,99 |
| - Despesas administrativas | 398.131,91 | 50,00 |
| - Laudos e vistorias | 85.500,00 | 10,74 |
| - (restante não detalhado) | 7.786.335,28 | 977,56 |
| **TOTAL ADM INCORPORADORA** | **18.259.356,47** | **2.292,58** |

> **Nota:** Esses valores NÃO entram na calibração paramétrica. São custos da incorporadora (terreno, marketing, vendas, jurídico, financeiro). Para orçamento de obra pura, considerar apenas os R$ 30.252.288,33 de custos diretos.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| LOUÇAS E METAIS | 228.396,87 | 28,68 |
| - MAT | 146.159,94 | 18,35 |
| - MOE | 82.236,93 | 10,33 |

> **Observação:** Dados de quantitativo por UR não disponíveis (UR não informada no executivo).

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor |
|---|---|---|
| Ritmo de construção | AC / Prazo | **227 m²/mês** |
| Burn rate mensal (direto) | Total direto / Prazo | **R$ 864.351/mês** |
| Burn rate mensal (total) | Total com ADM / Prazo | **R$ 1.386.047/mês** |
| Custo / mês / m² (direto) | (Total direto/Prazo) / AC | **108,53 R$/m²/mês** |

> **Nota:** Prazo estimado em ~35 meses (não confirmado no executivo — assumido).

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Item | Valor Total (R$) | R$/m² AC |
|---|---|---|
| IMPERMEABILIZAÇÕES E TRATAMENTOS | 1.002.774,02 | 125,91 |
| - MAT | 809.275,36 | 101,62 |
| - MOE | 193.498,67 | 24,30 |

> **Observação:** Valor acima da mediana (R$ 65,31/m²) em 92,8%. Possível indicativo de:
> - Áreas molhadas extensas (banheiros, cozinhas, sacadas, piscina)
> - Impermeabilização de laje de cobertura + subsolo
> - Tratamento de juntas de dilatação em fachada

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| ÁREAS COMUNS E PAISAGISMO | 780.978,78 | 98,07 |
| REVESTIMENTOS COMPLEMENTARES | 502.949,85 | 63,15 |
| COBERTURAS | 67.657,45 | 8,50 |
| LIMPEZA FINAL DE OBRA | 117.444,09 | 14,75 |
| SERVIÇOS COMPLEMENTARES | 68.692,03 | 8,63 |
| LIMPEZA DE OBRA | 38.699,73 | 4,86 |
| **TOTAL COMPLEMENTARES** | **1.576.421,94** | **197,93** |

---

## SEÇÃO 15 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média

- **Rev. Int. Parede:** R$ 414,43/m² vs mediana R$ 136,95 (+203%) — Possível razão: inclui revestimento de fachada (chapisco + reboco externo)
- **Esquadrias:** R$ 413,44/m² vs mediana R$ 282,08 (+46,5%) — Padrão de esquadrias alto ou grande área envidraçada
- **Impermeabilização:** R$ 125,91/m² vs mediana R$ 65,31 (+92,8%) — Áreas molhadas extensas ou tratamento de laje cobertura/subsolo

### ✅ Dentro da Faixa

- **Supraestrutura:** R$ 854,66/m² vs mediana R$ 709,64 — Alinhado (+20,4%)
- **Instalações:** R$ 399,85/m² vs mediana R$ 356,48 — Alinhado (+12,2%)
- **Infraestrutura:** R$ 323,96/m² vs mediana R$ 197,73 — Acima mas justificado (fundação profunda + contenção)

### 🔽 Abaixo da Média

- **Gerenciamento:** R$ 127,03/m² vs mediana R$ 435,10 (-70,8%) — **Não comparável:** o executivo separa ADM incorporadora (R$ 18,26M) do canteiro de obra (R$ 1,01M). Mediana inclui projetos + equipe + taxas
- **Fachada:** R$ 25,71/m² vs mediana R$ 138,51 (-81,4%) — **Reclassificação:** maior parte da fachada está em "Revestimentos de Argamassa"
- **Louças e Metais:** R$ 28,68/m² vs mediana R$ 0,00 — Muitos projetos não detalham louças separadamente

### 📝 Particularidades

- **Laje:** Treliçada TR8/TR16 + Maciça (tipo misto)
- **Fundação:** Hélice contínua + Estaca raiz + Blocos (múltiplos tipos)
- **Contenção:** Estaca raiz 31cm + Cortinas
- **MOE separado:** R$ 9,67M (31,98% dos custos diretos) — somado ao MAT por célula
- **ADM incorporadora:** R$ 18,26M (37,64% do total) — **NÃO entra na calibração paramétrica**

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total (com ADM)** | **R$ 48.511.644,80** | R$ |
| **Custo direto (sem ADM)** | **R$ 30.252.288,33** | R$ |
| **R$/m² Total** | **6.091,06** | R$/m² |
| **R$/m² Direto** | **3.798,44** | R$/m² |
| **CUB ratio Total** | **2,05** | CUB |
| **CUB ratio Direto** | **1,28** | CUB |
| ADM Incorporadora / Total | 37,64% | % |
| MOE / Custos diretos | 31,98% | % |
| MAT / Custos diretos | 68,02% | % |

---

> **Fonte:** XLSX (43278b5e-388b-4458-8769-3182ed21cc8f.xlsx) + PDF executivo
> **Extraído em:** 06/03/2026
> **Notas:**
> - **Estrutura de custos:** ADM incorporadora separada (R$ 18,26M = terreno + comissões). Para calibração paramétrica, usar apenas custos diretos (R$ 30,25M).
> - **MOE separado:** Aba "3 - MOE" soma R$ 9,67M (31,98% dos custos diretos). Já somado ao MAT por célula construtiva.
> - **Fachada subdividida:** Maior parte do revestimento externo está em "REVESTIMENTOS DE ARGAMASSA" (R$ 414,43/m²). "ACABAMENTOS EM FACHADA" tem apenas R$ 25,71/m² (só MOE de pintura/acabamento final).
> - **Gerenciamento reduzido:** R$ 127,03/m² refere-se apenas ao canteiro físico. Projetos, taxas, equipe ADM estão na aba "1 - ADM" (R$ 18,26M incorporadora).
