# Brava Mundo — Índices de Orçamento Executivo

> Extração de índices a partir de orçamento executivo detalhado.
> Projeto: Mendes Empreendimentos
> Data-base: Abr/2022 (orçamento R03, revisado em 19/05/2022)
> Extraído em: 06/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Brava Mundo | — |
| Código CTN | — | N/A | — |
| Revisão | — | R03 | — |
| Localização | — | Brava, Itajaí/SC | — |
| Endereço | — | Região costeira (Praia Brava) | — |
| Incorporador/Cliente | — | Mendes Empreendimentos | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | 4.811,54 | m² |
| Área Privativa | — | N/D | m² |
| Unid. Habitacionais | UR_H | 55 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 55 | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | N/D | meses |
| Data-base | — | Abr/2022 | — |
| **CUB na Data-base** | — | **R$ 2.461,35** | **R$** |
| R$/m² Total | — | 3.930,84 | R$/m² |
| CUB ratio | — | 1,60 | CUB |
| Tipo de Laje | — | N/D | — |
| Tipo de Fundação | — | Estacas (projeto alterado na R03) | — |
| Padrão Acabamento | — | Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | N/D | — |
| Valor ADM (se separado) | N/A | — |
| **Tem MOE (Mão de Obra) separado?** | N/D | — |
| Valor MOE (se separado) | N/A | — |
| Metodologia de rateio MOE | — | N/D |
| Custos diretos de obra (sem ADM/MOE) | R$ 15.800.104,95 | 83,54% (excluindo Gerenciamento) |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| 1. Gerenciamento Técnico e Administrativo | 1-Gerenciamento | R$ 3.113.588,95 |
| 2. Movimentação de Terra | 2-Mov. Terra | R$ 449.100,00 |
| 3. Contenções e Arrimos | 3-Contenção | R$ 640.926,46 — separado de Infraestrutura |
| 4. Infraestrutura | 4-Infraestrutura | R$ 880.098,86 — estacas (projeto alterado) |
| 5. Supraestrutura | 5-Supraestrutura | R$ 3.604.138,11 |
| 6. Alvenaria | 6-Alvenaria | R$ 729.403,27 |
| 7-11. Instalações (Elétr+Hidro+Prev+Clim+Telecom) | 7-Instalações | R$ 2.471.816,73 (soma 5 disciplinas) |
| 12. Impermeabilização | 8-Impermeabilização | R$ 298.123,80 |
| 13. Rev. Internos Piso e Parede | 10-Rev. Int. Parede | R$ 456.914,41 |
| 14. Rev. e Acabamentos Internos Teto | 11-Teto | R$ 284.405,57 |
| 15. Acabamentos em Piso e Parede | 12-Pisos | R$ 1.068.096,65 |
| 16. Pintura Interna | 13-Pintura | R$ 427.743,05 |
| 17. Esquadrias, Vidros e Ferragens | 14-Esquadrias | R$ 2.682.707,91 |
| 18. Rev. e Acabamentos de Fachada | 16-Fachada | R$ 747.408,06 |
| 19. Equip. e Sistemas Especiais | 8-Sist. Especiais | R$ 664.000,00 |
| 20. Serviços Complementares e Finais | 17-Complementares | R$ 395.222,07 |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor |
|---|---|---|
| Área por Unidade | AC / UR | 87,5 m²/UR |
| R$ por Unidade | Total / UR | R$ 343.885,34/UR |

**DESTAQUE:** AC/UR de 87,5 m²/UR indica unidades compactas (estúdios ou 1-2 quartos), típico de empreendimentos na Praia Brava voltados para investimento/temporada.

### 2.2 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 343.885,34 |
| CUB / UR | (R$/UR) / CUB | 139,7 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % |
|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 3.113.588,95 | 647,10 | 16,46% |
| 2 | Movimentação de Terra | 449.100,00 | 93,34 | 2,37% |
| 3 | Contenções e Arrimos | 640.926,46 | 133,20 | 3,39% |
| 4 | Infraestrutura | 880.098,86 | 182,91 | 4,65% |
| 5 | Supraestrutura | 3.604.138,11 | 749,05 | 19,06% |
| 6 | Alvenaria | 729.403,27 | 151,59 | 3,86% |
| 7 | Instalações (agrupado) | 2.471.816,73 | 513,72 | 13,07% |
| 8 | Sistemas Especiais | 664.000,00 | 138,00 | 3,51% |
| 9 | Impermeabilização | 298.123,80 | 61,96 | 1,58% |
| 10 | Rev. Internos Parede | 456.914,41 | 94,96 | 2,42% |
| 11 | Teto | 284.405,57 | 59,11 | 1,50% |
| 12 | Pisos | 1.068.096,65 | 221,98 | 5,65% |
| 13 | Pintura | 427.743,05 | 88,90 | 2,26% |
| 14 | Esquadrias | 2.682.707,91 | 557,55 | 14,18% |
| 15 | Fachada | 747.408,06 | 155,33 | 3,95% |
| 16 | Complementares | 395.222,07 | 82,14 | 2,09% |
| — | **TOTAL** | **18.913.693,90** | **3.930,84** | **100%** |

**DESTAQUES:**
- ⚠️ **Gerenciamento R$ 647,10/m² (16,46%)** — MUITO ALTO, quase o dobro da mediana da base (~408 R$/m²). Possível inclusão ampla de custos de canteiro, equipe e gestão
- ⚠️ **Mov. Terra R$ 93,34/m² (2,37%)** — MUITO ACIMA da mediana (~13 R$/m²), terreno costeiro com instabilidade
- ⚠️ **Contenções R$ 133,20/m² (3,39%)** — Terreno instável em região costeira (Brava) requer contenções significativas
- ⚠️ **Esquadrias R$ 557,55/m² (14,18%)** — MUITO ACIMA da mediana (~310 R$/m²), quase o dobro. Alto padrão
- ⚠️ **Instalações R$ 513,72/m² (13,07%)** — ACIMA da mediana (~368 R$/m²), inclui climatização e automação
- ✅ **Supraestrutura R$ 749,05/m² (19,06%)** — alinhada com mediana (~757 R$/m²)
- 🔽 **Pintura R$ 88,90/m² (2,26%)** — abaixo da mediana (~123 R$/m²)
- 🔽 **Sist. Especiais R$ 138,00/m² (3,51%)** — abaixo da mediana (~212 R$/m²)
- ✅ **CUB ratio 1,60** — ALTO, acima da mediana da base (~1,28). Empreendimento de custo elevado por m²

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

> Dados detalhados de volume de concreto, armadura e forma NÃO disponíveis no executivo.

| Índice | Valor | Un |
|---|---|---|
| Supraestrutura / AC | 749,05 | R$/m² |
| Total Supraestrutura | R$ 3.604.138,11 | R$ |

### 4.2 Infraestrutura

| Item | Valor | Obs |
|---|---|---|
| Infraestrutura / AC | 182,91 R$/m² | Projeto estacas alterado na R03 |
| Contenções / AC | 133,20 R$/m² | Projetos recebidos 20/04, preços atualizados |
| **Total Infra + Contenções** | **316,11 R$/m²** | Soma das duas etapas |

**DESTAQUE:** Infraestrutura + Contenções somam R$ 316,11/m² — solo costeiro com instabilidade requer investimento significativo em fundações e arrimos. Retrabalhos por instabilidade NÃO foram considerados no orçamento.

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> Dados detalhados de áreas de serviço, comprimentos e quantitativos por unidade NÃO disponíveis no executivo.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. |
|---|---|---|---|
| Sist. Inst. Elétricas | 717.507,34 | 149,12 | 29,03% |
| Sist. Inst. Hidrossanitárias e Drenagem | 882.511,64 | 183,41 | 35,70% |
| Instalações Preventivas e GN | 199.906,24 | 41,55 | 8,09% |
| Climatização e Exaustão | 356.207,16 | 74,03 | 14,41% |
| Automação e Sist. Lógicos e Telecom | 315.684,35 | 65,61 | 12,77% |
| **TOTAL** | **2.471.816,73** | **513,72** | **100%** |

**DESTAQUE:** Hidrossanitárias lideram com 35,70% das instalações. A R03 teve redução significativa de -R$ 246,25/m² vs R00 nesta disciplina (revisão de projeto). Climatização e Automação representam 27,18% juntos — alto para empreendimento residencial, indica sistema centralizado ou VRF.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

> Dados detalhados de PUs individualizados NÃO disponíveis no executivo. Valores agregados nos macrogrupos.

### 7.1 Revestimentos de Parede
| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Rev. Internos Piso e Parede | 456.914,41 | 94,96 |

### 7.2 Pisos
| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Acabamentos em Piso e Parede | 1.068.096,65 | 221,98 |

### 7.3 Teto
| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Rev. e Acabamentos Internos Teto | 284.405,57 | 59,11 |

### 7.4 Pintura
| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Pintura Interna | 427.743,05 | 88,90 |

### 7.5 Fachada
| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Rev. e Acabamentos de Fachada | 747.408,06 | 155,33 |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

| Índice | Valor | Un |
|---|---|---|
| Esquadrias / AC | 557,55 | R$/m² |
| Esquadrias / UR | 48.776,51 | R$/UR |
| % do total | 14,18% | — |

**DESTAQUE:** Esquadrias representam 14,18% do total (R$ 557,55/m²), MUITO ACIMA da mediana da base (~310 R$/m²). Empreendimento em região de praia com grandes panos de vidro, esquadrias especificadas para resistência à maresia (anodização/pintura eletrostática).

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Equip. e Sistemas Especiais | 664.000,00 | 138,00 |

| Índice | Valor | Un |
|---|---|---|
| Sist. Especiais / AC | 138,00 | R$/m² |

**NOTA:** Valor abaixo da mediana (~212 R$/m²). Climatização e automação foram alocados em Instalações (etapas 10 e 11), não em Sistemas Especiais.

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

| Item | Valor (R$) | R$/m² AC | % do Total |
|---|---|---|---|
| Gerenciamento Técnico e Administrativo | 3.113.588,95 | 647,10 | 16,46% |

**DESTAQUE:** Gerenciamento representa 16,46% do total — muito alto vs mediana da base (~11%). Possível inclusão abrangente de custos de canteiro, equipe técnica, equipamentos e despesas administrativas.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

> Dados não disponíveis separadamente — incluídos em Pisos/Acabamentos.

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

> Dados de prazo NÃO disponíveis no executivo.

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Item | Total (R$) | R$/m² AC |
|---|---|---|
| Impermeabilização | 298.123,80 | 61,96 |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² AC | % do Total |
|---|---|---|---|
| Serviços Complementares e Finais | 395.222,07 | 82,14 | 2,09% |

---

## SEÇÃO 15 — BENCHMARK / COMPARATIVO DE REVISÕES

### Comparativo R03 vs R00 (R$/m²)

| Macrogrupo | R03 (R$/m²) | R00 (R$/m²) | Δ (R$/m²) | Obs |
|---|---|---|---|---|
| **TOTAL** | **3.930,84** | **3.859,95** | **+70,89 (+1,84%)** | — |
| Gerenciamento | 647,10 | 457,75 | +189,35 | Maior aumento |
| Supraestrutura | 749,05 | 568,86 | +180,19 | 2º maior aumento |
| Mov. Terra | 93,34 | 19,55 | +73,79 | 3º maior aumento |
| Hidrossanitárias | — | — | -246,25 | Maior redução (revisão projeto) |
| Elétricas | — | — | -153,54 | 2ª maior redução |
| Climatização | — | — | -51,34 | 3ª maior redução |

**NOTA:** Variação total de apenas +1,84% entre R00 e R03, mas com grandes compensações internas: aumentos em Gerenciamento/Supraestrutura/Mov. Terra compensados por reduções em Hidrossanitárias/Elétricas/Climatização.

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média
- **Gerenciamento:** R$ 647,10/m² — 58% acima da mediana (~408). Representa 16,46% do total
- **Mov. Terra:** R$ 93,34/m² — ~7x a mediana (~13). Terreno costeiro com instabilidade, necessidade de preparação extensiva
- **Contenções:** R$ 133,20/m² — região de Brava requer arrimos significativos
- **Esquadrias:** R$ 557,55/m² — 80% acima da mediana (~310). Região costeira com exigência de esquadrias de alta performance
- **Instalações:** R$ 513,72/m² — 40% acima da mediana (~368). Inclui climatização centralizada + automação

### ✅ Dentro da Faixa
- **Supraestrutura:** R$ 749,05/m² — alinhada com mediana (~757)
- **Alvenaria:** R$ 151,59/m² — alinhada com mediana (~162)
- **Infraestrutura:** R$ 182,91/m² — dentro da faixa
- **Pisos:** R$ 221,98/m² — acima da mediana (~169), padrão alto
- **Fachada:** R$ 155,33/m² — alinhada com mediana (~138-155)

### 🔽 Abaixo da Média
- **Pintura:** R$ 88,90/m² — 28% abaixo da mediana (~123)
- **Sist. Especiais:** R$ 138,00/m² — 35% abaixo da mediana (~212). Climatização alocada em Instalações
- **Teto:** R$ 59,11/m² — abaixo da mediana (~48-59), mas alinhado
- **Complementares:** R$ 82,14/m² — abaixo da mediana (~172)

### 📝 Particularidades
- **Região costeira (Praia Brava, Itajaí/SC)** — terreno com instabilidade, contenções e movimentação de terra elevados
- **55 unidades com AC/UR de 87,5 m²** — unidades compactas, possivelmente voltadas para investimento/temporada
- **CUB ratio 1,60** — alto, reflete custo elevado por m² para a data-base
- **Retrabalhos por instabilidade do terreno NÃO considerados** — risco de custos adicionais em contenções e infraestrutura
- **Projeto de estacas alterado na R03** — novos quantitativos de blocos
- **Grandes variações entre R00 e R03** — compensações internas significativas (Gerenciamento/Supraestrutura subiram, Instalações desceram)
- **Climatização + Automação em Instalações** — diferente de outros projetos que alocam em Sist. Especiais

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 18.913.693,90 | R$ |
| **R$/m²** | 3.930,84 | R$/m² |
| **CUB ratio** | 1,60 | CUB |
| **R$/UR** | 343.885,34 | R$/UR |
| **AC/UR** | 87,5 | m²/un |
| **UH** | 55 | un |
| **AC** | 4.811,54 | m² |
| CUB data-base | R$ 2.461,35 | R$ (abr/22) |

---

> **Fonte:** Orçamento Executivo R03 (19/05/2022) — Mendes Empreendimentos
> **Extraído em:** 06/03/2026
> **Notas:** Executivo com nível de agregação por etapa (20 etapas). Dados detalhados de quantitativos (concreto, aço, forma, áreas de serviço) não disponíveis. Contenções separadas de Infraestrutura. Climatização e Automação incluídos em Instalações. Retrabalhos por instabilidade do terreno NÃO considerados no orçamento.
