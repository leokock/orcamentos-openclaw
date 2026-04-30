# Residencial Málaga — Índices de Orçamento Executivo

> Extração de índices a partir de orçamento executivo detalhado (XLSX).
> Projeto: Nova Empreendimentos
> Data-base: Abr/2024 (orçamento R02)
> Extraído em: 06/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Residencial Málaga | — |
| Código CTN | — | N/A | — |
| Revisão | — | R02 | — |
| Localização | — | SC (não especificado) | — |
| Incorporador/Cliente | — | Nova Empreendimentos | — |
| Área do Terreno | AT | 2.251,70 | m² |
| Área Construída | AC | 4.430,32 | m² |
| Área Privativa | — | 2.651,04 | m² |
| Unid. Habitacionais | UR_H | 40 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 40 | un |
| Nº Total Pavimentos | NP | 4 | un |
| Nº Pavimentos Tipo | NPT | 1 | un |
| Nº Pav. Garagem | NPG | 1 (subsolo) | un |
| Elevadores | ELEV | 1 | un |
| Vagas Estacionamento | VAG | ~40 | un |
| Prazo de Obra | — | 27 | meses |
| Data-base | — | Abr/2024 | — |
| **CUB na Data-base** | — | **R$ 2.757,56** | **R$** |
| R$/m² Total (obra) | — | 3.492,11 | R$/m² |
| CUB ratio | — | 1,27 | CUB |
| Tipo de Laje | — | Treliçada com cerâmica H12 | — |
| Tipo de Fundação | — | Hélice Contínua ø30/40/50cm + Estaca Escavada ø20cm | — |
| Padrão Acabamento | — | Médio-Alto | — |

### Tipologias de Unidades

| Tipologia | Área (m²) | Qtd |
|---|---|---|
| Tipo A | 83,67 | ~13 |
| Tipo B | 104,22 | ~13 |
| Tipo C | 106,67 | ~14 |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | R$ 6.873.066,80 (terreno, comissões, projetos, admin) |
| Valor ADM (se separado) | R$ 6.873.066,80 | 29,59% do total geral |
| **Tem MOE (Mão de Obra) separado?** | Sim | R$ 5.236.637,86 destacado em seção própria |
| Valor MOE (se separado) | R$ 5.236.637,86 | 22,54% do total geral |
| Metodologia de rateio MOE | — | MO rateada por disciplina no arquivo ANÁLISE_CUSTOS |
| Custos diretos de obra (MAT) | R$ 11.121.086,62 | Material sem MO |
| **Total OBRA (MAT + MO)** | R$ 16.357.724,48 | 70,41% do total geral |
| **Total para calibração (c/ MO rateada)** | R$ 15.471.163,85 | Conforme ANÁLISE_CUSTOS |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Valor c/ MO (R$) |
|---|---|---|
| Canteiro de Obras | 1-Gerenciamento | Excluído¹ |
| Movimentações de Terra | 2-Mov. Terra | 346.870,48 |
| Contenções + Infraestrutura | 3-Infraestrutura | 1.008.205,39 |
| Supraestrutura | 4-Supraestrutura | 3.176.784,19 |
| Alvenaria e Vedações | 5-Alvenaria | 880.759,48 |
| Impermeabilização e Tratamentos | 6-Impermeabilização | 476.297,41 |
| Elétricas + Hidro + Gás + Preventivas | 7-Instalações | 1.852.085,18 |
| Equipamentos + Climatização | 8-Sist. Especiais | 424.312,75 |
| Climatização e Exaustão | 9-Climatização | (incluso em 8) |
| Revestimentos Argamassados | 10-Rev. Int. Parede | 1.176.221,27 |
| Acabamentos em Gesso | 11-Teto | 417.557,42 |
| Revestimentos Cerâmicos + Louças/Metais | 12-Pisos | 1.183.548,46 |
| Pintura Interna | 13-Pintura | 553.705,91 |
| Esquadrias, Vidros e Ferragens | 14-Esquadrias | 1.273.047,98 |
| Acabamentos em Fachada | 16-Fachada | 971.161,27 |
| Cobertura + Limpeza + Serv. Compl. | 17-Complementares | 1.614.533,30 |
| — | 18-Imprevistos | — |

¹ ADM Incorporadora e Canteiro excluídos da calibração paramétrica (estão no total de R$ 6.873.066,80)

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência Base |
|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 1,97 | 3,5 - 14 |
| Área por Unidade | AC / UR | 110,8 | 78 - 310 |
| Unidades por Terreno | UR / AT | 0,018 | 0,03 - 0,06 |
| Eficiência Privativa | APR / AC | 59,8% | 40% - 65% |

**DESTAQUE:** CA de 1,97 indica aproveitamento moderado do terreno. Eficiência privativa de 59,8% é boa para projeto com garagem em subsolo.

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência |
|---|---|---|---|
| Vagas por Unidade | VAG / UR | 1,0 | 1,0 - 2,5 |
| UR por Elevador | UR / ELEV | 40,0 | 7 - 47 |
| Elevadores por Pavimento | ELEV / NP | 0,25 | 0,09 - 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial (2-3 dorm) | 40 | 100% | 66,3 (priv) |
| Comercial | 0 | 0% | — |

### 2.4 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total Obra / UR | R$ 386.779,10 |
| R$ / UR (habitacionais) | Total Obra / UR_H | R$ 386.779,10 |
| CUB / UR | (R$/UR) / CUB | 140,3 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Referência |
|---|---|---|---|---|---|
| 1 | Gerenciamento | —¹ | — | — | 300 - 500 |
| 2 | Movimentação de Terra | 346.870,48 | 78,29 | 2,24% | 15 - 80 |
| 3 | Infraestrutura | 1.008.205,39 | 227,57 | 6,52% | 170 - 300 |
| 4 | Supraestrutura | 3.176.784,19 | 717,06 | 20,53% | 690 - 790 |
| 5 | Alvenaria | 880.759,48 | 198,80 | 5,69% | 120 - 200 |
| 6 | Impermeabilização | 476.297,41 | 107,51 | 3,08% | 30 - 130 |
| 7 | Instalações (agrupado) | 1.852.085,18 | 418,05 | 11,97% | 220 - 420 |
| 8 | Sistemas Especiais | 316.852,20 | 71,52 | 2,05% | 70 - 260 |
| 9 | Climatização | 107.460,55 | 24,26 | 0,69% | 20 - 80 |
| 10 | Rev. Internos Parede | 1.176.221,27 | 265,49 | 7,60% | 115 - 270 |
| 11 | Teto | 417.557,42 | 94,25 | 2,70% | 35 - 95 |
| 12 | Pisos | 1.183.548,46 | 267,15 | 7,65% | 145 - 270 |
| 13 | Pintura | 553.705,91 | 124,98 | 3,58% | 50 - 130 |
| 14 | Esquadrias | 1.273.047,98 | 287,35 | 8,23% | 250 - 350 |
| 15 | Louças e Metais | 116.007,77² | 26,19 | 0,75% | 20 - 40 |
| 16 | Fachada | 971.161,27 | 219,21 | 6,28% | 130 - 300 |
| 17 | Complementares | 1.614.533,30 | 364,43 | 10,44% | 110 - 370 |
| 18 | Imprevistos | — | — | — | — |
| — | **TOTAL** | **15.471.163,85³** | **3.492,11** | **100%** | — |

¹ Gerenciamento/ADM Incorporadora separado (R$ 6.873.066,80) — não incluído na calibração
² Louças e Metais: R$ 84.587,94 (MAT) + R$ 31.419,83 (MO) = R$ 116.007,77
³ Total conforme ANÁLISE_CUSTOS com MO rateada

**DESTAQUES:**
- ✅ **Supraestrutura R$ 717,06/m²** — dentro da faixa (690-790)
- ✅ **Instalações R$ 418,05/m²** — no limite superior da faixa (220-420)
- ✅ **Esquadrias R$ 287,35/m²** — dentro da faixa (250-350)
- ⚠️ **Mov. Terra R$ 78,29/m²** — próximo ao limite superior (15-80)
- ⚠️ **Teto R$ 94,25/m²** — próximo ao limite superior (35-95)
- ✅ **CUB ratio 1,27** — alinhado com mediana de obras similares

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento / Pavimento | Volume (m³) | fck | PU Concreto (R$/m³) |
|---|---|---|---|
| Subsolo (escada + laje) | 132,86 | 35 | 495,34 |
| Térreo | 402,80 | 35 | 495,34 |
| Tipo | 132,95 | 35 | 495,34 |
| Mezanino | 153,39 | 35 | 495,34 |
| Ático | 307,55 | 35 | 495,34 |
| Casa de Máquinas | 64,03 | 35 | 495,34 |
| Reservatório | 34,79 | 35 | 603,75 |
| **TOTAL** | **1.228,37** | — | — |

| Índice | Valor | Un | Referência |
|---|---|---|---|
| Consumo concreto supra / AC | 0,277 | m³/m² | 0,19 - 0,28 |

#### Armadura (Aço) — Por Pavimento

| Pavimento | CA-60 ø5 | CA-50 ø6,3 | CA-50 ø8 | CA-50 ø10 | CA-50 ø12,5 | CA-50 ø16 | CA-50 ø20 | Tela Q-95 (m²) | Total (kg) |
|---|---|---|---|---|---|---|---|---|---|
| Subsolo | 5 | 90 | 6.111 | 903 | 27 | — | — | — | 7.136 |
| Térreo | 1.792 | 2.446 | 4.876 | 3.491 | 2.297 | 3.557 | 13.179 | 1.257 | 33.553 |
| Tipo | 1.074 | 1.711 | 1.673 | 1.341 | 1.641 | 2.144 | 517 | 794 | 11.311 |
| Mezanino | 1.548 | 801 | 947 | 4.719 | 1.897 | 1.575 | 277 | 220 | 12.319 |
| Ático | 1.449 | 1.242 | 1.861 | 2.258 | 1.954 | 1.703 | 1.257 | 956 | 14.192 |
| Casa Máq. | 574 | 238 | 1.009 | 746 | 398 | 245 | 136 | 244 | 3.961 |
| Reservatório | 213 | 442 | 704 | 590 | 165 | — | — | — | 2.114 |
| **TOTAL** | **6.655** | **6.970** | **17.182** | **14.049** | **8.378** | **9.224** | **15.366** | **3.471** | **84.586** |

*Nota: Tela Q-95 = 1,52 kg/m² → 3.471 m² × 1,52 = 5.276 kg adicional*
*Total aço + tela ≈ 84.586 + 5.276 = **89.862 kg***

| Índice | Valor | Un | Referência |
|---|---|---|---|
| Taxa de aço global | 73,2 | kg/m³ | 75 - 115 |
| Aço / AC | 20,28 | kg/m² | 15 - 25 |
| PU aço médio | ~5,80 | R$/kg | 5,50 - 7,00 |

#### Forma

| Pavimento | Pilares (m²) | Vigas (m²) | Lajes (m²) | Escada (m²) | Treliçada (m²) | Total (m²) |
|---|---|---|---|---|---|---|
| Subsolo | — | — | — | 23,03 | — | 23,03 |
| Térreo | 336,01 | 1.165,43 | — | 20,92 | 1.260,93 | 2.783,29 |
| Tipo | 255,27 | 565,54 | 152,67 | 20,92 | 718,78 | 1.713,18 |
| Mezanino | 377,09 | 670,45 | 1.456,59 | 293,61 | 207,86 | 3.005,60 |
| Ático | 370,78 | 797,40 | — | 20,92 | 741,08 | 1.930,18 |
| Casa Máq. | 110,92 | 259,97 | 37,28 | — | 134,38 | 542,55 |
| Reservatório | 60,37 | 205,09 | 25,99 | — | — | 291,45 |
| **TOTAL** | **1.510,44** | **3.663,88** | **1.672,53** | **379,40** | **3.063,03** | **10.289,28** |

| Índice | Valor | Un | Referência |
|---|---|---|---|
| Forma / AC | 2,32 | m²/m² | 1,25 - 1,50 |
| PU forma (média) | ~45,00 | R$/m² | 30 - 70 |

**NOTA:** Índice de forma elevado (2,32 m²/m²) inclui lajes treliçadas contabilizadas como "forma" no orçamento.

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | Total (R$) |
|---|---|---|---|
| Tipo de laje (geral) | Treliçada TR12 com cerâmica H12 | 3.063,03 m² | 264.638,42 |
| PU laje treliçada | — | — | R$ 86,41/m² |
| Escoramento metálico | Para vigas e lajes | 3.181,12 m² | 101.708,92 |
| PU escoramento (simples) | — | — | R$ 25,36/m² |
| PU escoramento (pé direito duplo) | — | 425,87 m² | R$ 50,72/m² |
| Polimento piso garagem | Subsolo + Térreo | 1.046,23 m² | 112.395,55 |

### 4.2 Infraestrutura

#### Fundação Profunda

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Estaca escavada ø20cm | 128 | m | 12,00 | 1.536,00 |
| Estaca HC ø30cm | 694,19 | m | 35,00 | 24.296,65 |
| Estaca HC ø40cm | 1.204 | m | 47,00 | 56.588,00 |
| Estaca HC ø50cm | 480 | m | 60,00 | 28.800,00 |
| **Total ML estacas** | **2.506,19** | **m** | — | **111.220,65** |
| Mobilização equipamentos | 1 | vb | 5.809,00 | 5.809,00 |
| Concreto fck 30 (estacas) | 353,36 | m³ | 481,25 | 170.054,50 |
| Aço CA-50 (estacas) | 10.060,10 | kg | ~6,15 | 61.858,03 |

| Índice | Valor | Un | Referência |
|---|---|---|---|
| ML estaca / AC | 0,566 | m/m² | 0,19 - 0,55 |
| ML estaca / UR | 62,65 | m/UR | 15 - 130 |
| Nº estacas equiv. / UR | ~2,0 | un/UR | 1,3 - 4,3 |
| Taxa aço estacas | 28,5 | kg/m³ | 25 - 35 |

**DESTAQUE:** ML estaca/AC de 0,566 m/m² acima da faixa típica, indicando solo com baixa capacidade de carga.

#### Fundação Rasa (Blocos + Sapatas + Vigas Baldrame)

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Forma blocos | 213,47 | m² | 77,58 | 16.560,66 |
| Forma sapatas | 24,40 | m² | 77,58 | 1.892,91 |
| Forma vigas baldrame | 811,72 | m² | 72,58 | 58.913,18 |
| Forma cisterna | 243,84 | m² | 77,58 | 18.916,72 |
| Forma pilares arranque | 140,53 | m² | 104,24 | 14.648,24 |
| **Total forma** | **1.433,96** | **m²** | — | **110.931,71** |
| Concreto fck 30 | 160,94 | m³ | 458,50 | 73.790,99 |
| Concreto fck 35 (ETE) | 30,97 | m³ | 488,50 | 15.128,85 |
| **Total concreto fund. rasa** | **191,91** | **m³** | — | **88.919,84** |
| Aço fundação rasa | 14.825,90 | kg | ~6,62 | 98.063,90 |

| Índice | Valor | Un |
|---|---|---|
| Taxa aço fund. rasa | 77,25 | kg/m³ |
| Forma fund. rasa / AC | 0,324 | m²/m² |

#### Contenções

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Concreto contenções | 95,72 | m³ | — | — |
| Forma contenções | 787,33 | m² | — | — |
| Aço contenções | ~5.448 | kg | — | — |
| **Total Contenções** | — | — | — | **125.699,04** |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

### 5.1 Movimentação de Terra

| Serviço | Volume (m³) | Índice (m³/m² AC) |
|---|---|---|
| Escavação total | 1.563,72 | 0,353 |
| Reaterro | 1.036,40 | 0,234 |
| Bota-fora | 667,18 | 0,151 |
| Apiloamento | 1.511,65 m² | 0,341 m²/m² |
| Lastro | 207,61 | 0,047 |

### 5.2 Terraplanagem

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Terraplanagem | 148.167,83 | 33,44 |
| Demolições e limpeza | 30.235,99 | 6,83 |
| Drenagem | 26.677,35 | 6,02 |
| Escavações, reaterro, lastro | 115.606,11 | 26,09 |
| **Total Mov. Terra** | **320.687,29** | **72,38** |

### 5.3 Quantitativos Estruturais Consolidados

| Índice | Valor | Un | Observação |
|---|---|---|---|
| Concreto total (supra + infra) | 1.773,64 | m³ | Estacas + fund. rasa + supra |
| Concreto supra / AC | 0,277 | m³/m² | — |
| Concreto infra / AC | 0,123 | m³/m² | Fund. profunda + rasa |
| Aço total | ~109.372 | kg | Supra + infra |
| Aço / AC | 24,69 | kg/m² | — |
| Forma total | ~11.723 | m² | Supra + infra |
| Forma / AC | 2,65 | m²/m² | — |

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor MAT (R$) | R$/m² AC | % Instal. | MO (R$) |
|---|---|---|---|---|
| Elétricas e Telefônicas | 635.544,44 | 143,45 | 52,4% | 261.831,91 |
| Hidrossanitárias | 503.956,91 | 113,75 | 41,5% | 261.831,91 |
| Gás | 12.647,00 | 2,85 | 1,0% | — |
| Preventivas (incêndio + SPDA) | 60.265,24 | 13,60 | 5,0% | — |
| **TOTAL** | **1.212.413,59** | **273,66** | **100%** | **523.663,82** |

| Índice | Valor | Un |
|---|---|---|
| MAT instalações / AC | 273,66 | R$/m² |
| MO instalações / AC | 118,20 | R$/m² |
| Total instalações / AC | 391,86 | R$/m² |
| Razão MO/Material | 0,43 | — |

### Detalhamento Elétricas por Pavimento

| Pavimento | Valor (R$) |
|---|---|
| Subsolo | 54.806,67 |
| Térreo | 403.225,60 |
| Tipo | 75.421,80 |
| Mezanino | 38.118,30 |
| Ático | 15.910,76 |
| Casa de Máquinas | 6.095,46 |
| Comunicações | 41.965,85 |
| **Total** | **635.544,44** |

### Detalhamento Hidrossanitárias por Pavimento

| Pavimento | Valor (R$) |
|---|---|
| Subsolo | 205.355,42 |
| Térreo | 105.266,47 |
| Tipo | 82.442,33 |
| Mezanino | 39.778,21 |
| Ático | 16.799,11 |
| Casa de Máquinas | 16.316,76 |
| Barrilete | 36.648,26 |
| Reservatório | 1.350,36 |
| **Total** | **503.956,91** |

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos Argamassados

| Pavimento | Valor MAT (R$) | Valor MO (R$) | Total (R$) |
|---|---|---|---|
| Subsolo | 56.550,56 | 130.585,89 | 187.136,45 |
| Térreo | 130.162,40 | 321.327,15 | 451.489,55 |
| Tipo | 99.099,14 | 174.180,32 | 273.279,46 |
| Mezanino | 72.076,82 | 165.399,60 | 237.476,42 |
| Ático | 30.696,36 | 78.585,21 | 109.281,57 |
| Casa de Máquinas | 9.309,79 | 20.150,33 | 29.460,12 |
| Fachadas (N/S/L/O) | 184.186,64 | 497.480,63¹ | 681.667,27 |
| **Total** | **582.081,72** | **1.387.709,13** | **1.969.790,85** |

¹ MO fachada concentrada em "Fachada Norte" no orçamento

| Índice | Valor | Un |
|---|---|---|
| Rev. argamassados MAT / AC | 131,39 | R$/m² |
| Rev. argamassados MO / AC | 313,23 | R$/m² |
| Rev. argamassados Total / AC | 444,62 | R$/m² |

### 7.2 Revestimentos Cerâmicos

| Pavimento | Valor MAT (R$) | Valor MO (R$) | Total (R$) |
|---|---|---|---|
| Subsolo | 3.800,25 | 3.419,03 | 7.219,28 |
| Térreo | 243.719,91 | 233.556,72 | 477.276,63 |
| Tipo | 62.841,39 | 94.562,13 | 157.403,52 |
| Mezanino | 41.446,54 | 81.087,99 | 122.534,53 |
| Ático | 1.247,35 | 32.485,08 | 33.732,43 |
| **Total** | **353.055,43** | **445.114,25** | **798.169,68** |

| Índice | Valor | Un |
|---|---|---|
| Rev. cerâmicos / AC | 180,15 | R$/m² |

### 7.3 Pintura Interna

| Pavimento | Valor MAT (R$) | Valor MO (R$) | Total (R$) |
|---|---|---|---|
| Subsolo | 46.682,51 | 68.184,81 | 114.867,32 |
| Térreo | 52.330,81 | 86.996,62 | 139.327,43 |
| Tipo | 46.509,07 | 64.739,83 | 111.248,90 |
| Mezanino | 50.204,41 | 83.175,84 | 133.380,25 |
| Ático | 14.274,99 | 29.978,83 | 44.253,82 |
| Casa de Máquinas | 3.322,61 | 7.305,55 | 10.628,16 |
| **Total** | **213.324,42** | **340.381,49** | **553.705,91** |

| Índice | Valor | Un |
|---|---|---|
| Pintura interna / AC | 124,98 | R$/m² |

### 7.4 Acabamentos em Gesso

| Pavimento | Valor (R$) |
|---|---|
| Subsolo | 444,44 |
| Térreo | 63.434,00 |
| Tipo | 25.157,75 |
| Mezanino | 64.966,27 |
| Ático | 12.672,66 |
| **Total** | **166.675,12** |

| Índice | Valor | Un |
|---|---|---|
| Gesso / AC | 37,62 | R$/m² |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo e Pavimento

| Categoria | Valor (R$) | % |
|---|---|---|
| **Esquadrias de Alumínio** | **992.009,17** | **81,3%** |
| - Subsolo | 8.012,48 | 0,7% |
| - Térreo | 309.169,28 | 25,3% |
| - Tipo/Mezanino | 507.141,65 | 41,5% |
| - Ático | 158.072,10 | 12,9% |
| - Casa de Máquinas | 9.603,65 | 0,8% |
| **Esquadrias de Madeira** | **210.216,27** | **17,2%** |
| - Subsolo | 2.787,12 | 0,2% |
| - Térreo | 78.847,68 | 6,5% |
| - Tipo/Mezanino | 113.039,65 | 9,3% |
| - Ático | 14.323,91 | 1,2% |
| - Casa de Máquinas | 1.217,91 | 0,1% |
| **Esquadrias Metálicas** | **18.466,16** | **1,5%** |
| - Térreo | 7.963,76 | 0,7% |
| - Ático | 1.902,40 | 0,2% |
| - Casa de Máquinas | 8.600,00 | 0,7% |
| **TOTAL** | **1.220.681,60** | **100%** |

| Índice | Valor | Un |
|---|---|---|
| Esquadrias MAT / AC | 275,53 | R$/m² |
| Esquadrias Total / AC | 287,35 | R$/m² |
| Esquadrias / UR | 30.517,04 | R$/UR |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevador social | 1 | 161.210,66 | 161.210,66 |
| Equipamentos piscina | 1 vb | 53.245,00 | 53.245,00 |
| Aquecimento central | 1 vb | 84.506,54 | 84.506,54 |
| Geração água quente | 1 vb | 17.890,00 | 17.890,00 |
| **Total Equipamentos** | — | — | **316.852,20** |
| Climatização e Exaustão | — | — | 107.460,55 |
| **TOTAL SIST. ESPECIAIS + CLIM.** | — | — | **424.312,75** |

| Índice | Valor | Un | Referência |
|---|---|---|---|
| Elevador (R$/un) | 161.210,66 | R$ | 160k - 320k |
| Sistemas Especiais / AC | 71,52 | R$/m² | 70 - 260 |
| Climatização / AC | 24,26 | R$/m² | 20 - 80 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI) — ADM INCORPORADORA

> **NOTA:** Este projeto tem ADM Incorporadora separado (R$ 6.873.066,80). Abaixo o detalhamento:

### 10.1 Aquisição do Terreno

| Item | Valor (R$) |
|---|---|
| Valor compra do terreno | 2.055.914,26 |
| ITBI / FRJ | 360.000,00 |
| Taxas tabelionato / Registro | 2.997,60 |
| **Total Terreno** | **2.418.911,86** |

### 10.2 Comissões e Despesas Administrativas

| Item | Valor (R$) |
|---|---|
| Comissão venda unidades | 762.506,84 |
| Outorga onerosa e taxas terreno | 134.152,59 |
| Laudos e vistorias | 24.990,00 |
| **Total Comissões/Desp.** | **921.649,43** |

### 10.3 Serviços Técnicos e Projetos

| Disciplina | Valor (R$) |
|---|---|
| Assessoria Ambiental (27 meses) | 26.460,00 |
| Relatório Final Ambiental | 8.000,00 |
| Corte de Árvores | 10.000,00 |
| Compensação Ambiental | 100.000,00 |
| Levantamento Planialtimétrico | 10.500,00 |
| Sondagem de Percussão | 10.513,00 |
| **Total Estudos** | **165.473,00** |

| Projeto | Valor (R$) |
|---|---|
| Arquitetônico | 115.930,30 |
| Estrutural | 30.000,00 |
| Fundações e Contenções | 23.000,00 |
| Elétrico e Telecom | 13.000,00 |
| Hidrossanitário, Preventivo e SPDA | 21.000,00 |
| Piscina | 5.000,00 |
| Climatização | 10.000,00 |
| Interiores | 102.770,90 |
| Impermeabilização | 17.800,00 |
| Segurança do Trabalho | 3.800,00 |
| Fachada | 26.116,20 |
| ETE | 3.500,00 |
| Terraplanagem | 5.600,00 |
| Canteiro | 3.000,00 |
| Compatibilização BIM | 29.000,00 |
| As-built | 15.000,00 |
| **Total Projetos** | **424.517,40** |

### 10.4 Consultorias

| Item | Valor (R$) |
|---|---|
| Levantamento Ambiental | 16.800,00 |
| Advocacia | 177.028,20 |
| Orçamento e Planejamento | 25.917,00 |
| Contabilidade | 98.912,64 |
| Fiscalização (27 meses) | 226.800,00 |
| ART | 1.405,30 |
| Assessoria SST (27 meses) | 31.050,00 |
| PGR | 4.600,00 |
| Regularização matrículas | 5.300,00 |
| **Total Consultorias** | **587.813,14** |

### 10.5 Administração da Obra

| Item | Valor (R$) |
|---|---|
| Taxa de Negócio (parcela inicial) | 150.000,00 |
| Taxa de Negócio (12 parcelas) | 221.944,08 |
| Taxa Administração (31 meses) | 1.611.757,89 |
| **Total Taxa Admin** | **1.983.701,97** |

| Item | Valor (R$) |
|---|---|
| Taxas e Alvarás | 50.000,00 |
| Seguro obra | 35.500,00 |
| Impostos e taxas | 15.000,00 |
| IPTU | 50.000,00 |
| Certidão INSS | 5.000,00 |
| Assembleias | 1.500,00 |
| Aprovação projetos | 25.000,00 |
| **Total Taxas/Licenças** | **182.000,00** |

| Item | Valor (R$) |
|---|---|
| Habite-se | 6.000,00 |
| Renovação documentos | 5.000,00 |
| Despesas cartorárias | 167.000,00 |
| Taxas SPE | 5.000,00 |
| Manual Proprietário/Síndico | 6.000,00 |
| **Total Documentações** | **189.000,00** |

### 10.6 Resumo CI (ADM Incorporadora)

| Subgrupo | Valor (R$) | R$/m² | % do ADM | % do Total |
|---|---|---|---|---|
| Terreno | 2.418.911,86 | 546,00 | 35,2% | 10,4% |
| Comissões/Despesas | 921.649,43 | 208,04 | 13,4% | 4,0% |
| Serviços Técnicos | 1.177.803,54 | 265,85 | 17,1% | 5,1% |
| Administração Obra | 2.354.701,97 | 531,52 | 34,3% | 10,1% |
| **TOTAL ADM** | **6.873.066,80** | **1.551,37** | **100%** | **29,6%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS

| Pavimento | Valor MAT (R$) | Valor MO (R$) | Total (R$) |
|---|---|---|---|
| Subsolo | — | 8.034,92 | 8.034,92 |
| Térreo | — | 8.411,63 | 8.411,63 |
| Tipo | — | 5.404,93 | 5.404,93 |
| Mezanino | — | 1.717,97 | 1.717,97 |
| Ático | — | 7.850,38 | 7.850,38 |
| **Total MO** | — | **31.419,83** | **31.419,83** |
| **Material** | **84.587,94** | — | **84.587,94** |
| **TOTAL** | — | — | **116.007,77** |

| Índice | Valor | Un |
|---|---|---|
| Louças e Metais / AC | 26,19 | R$/m² |
| Louças e Metais / UR | 2.900,19 | R$/UR |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Referência |
|---|---|---|---|
| Ritmo de construção | AC / Prazo | 164,1 m²/mês | 120 - 310 |
| Burn rate mensal (obra) | Total / Prazo | R$ 573,0k/mês | — |
| Meses por pavimento | Prazo / NP | 6,75 | 1,6 - 5,1 |
| UR por mês | UR / Prazo | 1,48 un/mês | 0,4 - 4,0 |
| Custo / mês / m² | (Total/Prazo) / AC | 129,3 R$/m²/mês | 80 - 100 |

**NOTA:** Ritmo de 164,1 m²/mês é razoável para projeto de 4 pavimentos com subsolo.

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Aplicação | Valor (R$) | % |
|---|---|---|
| Fundação e Contenção | 191.831,03 | 51,6% |
| Cisternas | 6.001,49 | 1,6% |
| Poço Elevador | 1.179,81 | 0,3% |
| ETE | 19.335,09 | 5,2% |
| Térreo | 70.600,79 | 19,0% |
| Tipo | 28.784,11 | 7,7% |
| Mezanino | 10.984,77 | 3,0% |
| Ático | 28.622,86 | 7,7% |
| Casa de Máquinas | 7.908,69 | 2,1% |
| Reservatório | 6.316,02 | 1,7% |
| **Total MAT** | **371.564,65** | **100%** |
| **MO** | **104.732,76** | — |
| **TOTAL** | **476.297,41** | — |

| Índice | Valor | Un |
|---|---|---|
| Impermeabilização MAT / AC | 83,87 | R$/m² |
| Impermeabilização Total / AC | 107,51 | R$/m² |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² |
|---|---|---|
| Cobertura | 100.363,46 | 22,65 |
| Limpeza de Obra | 105.988,75 | 23,92 |
| Área Comum e Mobiliário | 1.487.598,00 | 335,78 |
| Fundo de Reserva | 171.159,30 | 38,63 |
| **Total MAT** | **1.865.109,51** | **420,99** |
| **MO (Cobertura + Limpeza)** | **36.656,46** | **8,27** |
| **TOTAL** | **1.901.765,97** | **429,26** |

**DESTAQUE:** Área Comum e Mobiliário representa 80% dos complementares (R$ 335,78/m²), indicando especificação de lazer completo.

---

## SEÇÃO 15 — FACHADA (Detalhamento)

### 15.1 Acabamentos em Fachada

| Orientação | Valor MAT (R$) |
|---|---|
| Norte | 63.689,02 |
| Sul | 59.555,20 |
| Leste | 25.891,18 |
| Oeste | 46.099,10 |
| **Total MAT** | **195.234,50** |
| **MO** | **94.259,49** |
| **Total Acabamentos Fachada** | **289.493,99** |

### 15.2 Revestimentos Argamassados em Fachada

| Orientação | Valor MAT (R$) |
|---|---|
| Norte | 60.068,93 |
| Sul | 56.814,65 |
| Leste | 23.974,18 |
| Oeste | 43.328,88 |
| **Total Argamassados** | **184.186,64** |
| **MO (inclusa em Rev. Arg.)** | **497.480,63** |

| Índice | Valor | Un |
|---|---|---|
| Fachada total / AC | 219,21 | R$/m² |

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média
- **Movimentação de Terra:** R$ 78,29/m² — próximo ao limite superior (15-80)
- **Teto (Gesso):** R$ 94,25/m² — próximo ao limite superior (35-95)
- **Instalações:** R$ 418,05/m² — no limite superior (220-420), indicando complexidade de sistemas

### ✅ Dentro da Faixa
- **Supraestrutura:** R$ 717,06/m² — bem alinhado (690-790)
- **Alvenaria:** R$ 198,80/m² — dentro da faixa (120-200)
- **Esquadrias:** R$ 287,35/m² — dentro da faixa (250-350)
- **Impermeabilização:** R$ 107,51/m² — dentro da faixa (30-130)
- **Pintura:** R$ 124,98/m² — dentro da faixa (50-130)
- **Fachada:** R$ 219,21/m² — dentro da faixa (130-300)
- **CUB ratio 1,27** — alinhado com mediana de obras similares

### 🔽 Abaixo da Média
- **Sistemas Especiais:** R$ 71,52/m² — próximo ao limite inferior (70-260)
- **Climatização:** R$ 24,26/m² — dentro da faixa mas conservador (20-80)

### 📝 Particularidades
- **Empreendimento compacto:** 4 pavimentos, 40 unidades (10 apts/andar)
- **Fundação mista:** HC ø30/40/50cm + estaca escavada ø20cm — solo desafiador (ML/AC = 0,566)
- **Laje treliçada TR12** — eficiência construtiva
- **Subsolo de garagem:** Garagem em subsolo (971,88 m² polidos)
- **Padrão médio-alto:** Eficiência privativa 59,8%, mobiliário/lazer completo (R$ 335,78/m²)
- **ADM Incorporadora separado:** 29,6% do total (R$ 6.873.066,80) — acima do típico
- **Taxa de aço:** 73,2 kg/m³ — dentro da faixa (75-115)

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total OBRA (c/ MO)** | R$ 15.471.163,85 | R$ |
| **Custo total GERAL** | R$ 23.230.791,28 | R$ |
| **R$/m² (obra)** | 3.492,11 | R$/m² |
| **R$/m² (geral)** | 5.243,59 | R$/m² |
| **CUB ratio (obra)** | 1,27 | CUB |
| **CUB ratio (geral)** | 1,90 | CUB |
| **R$/UR (obra)** | 386.779,10 | R$/UR |
| **R$/UR (geral)** | 580.769,78 | R$/UR |
| **AC/UR** | 110,8 | m²/un |
| Concreto supra / AC | 0,277 | m³/m² |
| Taxa aço supra | 73,2 | kg/m³ |
| Forma / AC | 2,32 | m²/m² |
| Estacas / AC | 0,566 | m/m² |
| Estacas / UR | 62,65 | m/UR |
| Elevador / UR | 40,0 | UR/elev |
| Ritmo construção | 164,1 | m²/mês |
| Burn rate | R$ 573,0k | R$/mês |
| Meses por pavimento | 6,75 | meses/pav |

---

> **Fonte:** Orçamento Executivo R02 (Abr/2024) + Análise de Custos
> **Extraído em:** 06/03/2026
> **Notas:** Executivo com alto nível de detalhamento. ADM Incorporadora separado (29,6%). MO rateada por disciplina na aba ANÁLISE_CUSTOS. Valores de calibração usando total de R$ 15.471.163,85 (sem ADM incorporadora).
