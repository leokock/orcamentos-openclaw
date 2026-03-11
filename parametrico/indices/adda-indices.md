# Residencial Adda — Índices de Orçamento Executivo

> Extração de índices a partir de orçamento executivo detalhado (XLSX) e apresentação oficial (PPTX).
> Projeto: Macom Construtora e Incorporadora LTDA
> Data-base: Jun/2023 (orçamento), Set/2023 (revisão R02)
> Extraído em: 06/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Residencial Adda | — |
| Código CTN | — | N/A | — |
| Revisão | — | R02 | — |
| Localização | — | Itapema/SC | — |
| Endereço | — | Rua 299, nº 142 - Meia Praia | — |
| Incorporador/Cliente | — | Macom Construtora e Incorporadora LTDA | — |
| Área do Terreno | AT | 463,30 | m² |
| Área Construída | AC | 4.358,27 | m² |
| Área Privativa | — | 1.800,12 | m² |
| Unid. Habitacionais | UR_H | 14 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 14 | un |
| Nº Total Pavimentos | NP | 22 | un |
| Nº Pavimentos Tipo | NPT | 14 | un |
| Nº Pav. Garagem | NPG | 0 | un |
| Elevadores | ELEV | 2 | un |
| Vagas Estacionamento | VAG | ~28¹ | un |
| Prazo de Obra | — | 36 | meses |
| Data-base | — | Jun/2023 | — |
| **CUB na Data-base** | — | **R$ 2.725,79** | **R$** |
| R$/m² Total | — | 3.082,60 | R$/m² |
| CUB ratio | — | 1,13 | CUB |
| Tipo de Laje | — | Nervurada (cubetas) / Maciça embasamento | — |
| Tipo de Fundação | — | Hélice Contínua ø60cm | — |
| Padrão Acabamento | — | Alto | — |

¹ Estimado a partir de layout de embasamento (não especificado no orçamento)

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Não | Custos de ADM incorporadora não incluídos no executivo |
| Valor ADM (se separado) | N/A | — |
| **Tem MOE (Mão de Obra) separado?** | Não | MO incluída nos preços unitários por disciplina |
| Valor MOE (se separado) | N/A | — |
| Metodologia de rateio MOE | — | Incluída nos PUs de cada serviço |
| Custos diretos de obra (sem ADM/MOE) | R$ 11.987.774,87 | 89,23% (excluindo Gerenciamento + Imprevistos) |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| Gerenciamento Técnico e Administrativo | 1-Gerenciamento | Serviços técnicos + equipe + canteiro + equipamentos |
| Movimentação de Terra | 2-Mov. Terra | Rebaixamento lençol + mov. terra + lastro |
| Infraestrutura | 3-Infraestrutura | Fundação profunda (HC ø60cm) + fundação rasa |
| Supraestrutura | 4-Supraestrutura | Concreto + armadura + forma + cubetas + escoramento |
| Alvenaria, Vedações e Divisórias | 5-Alvenaria | Paredes e painéis |
| Impermeabilização e Tratamentos | 6-Impermeabilização | Sistemas impermeabilização |
| Instalações Elétr, Hidro, GLP, Prev | 7-Instalações | Hidro + Elétr + Preventivas + Gás + Telecom (apresentação) |
| Equipamentos e Sistemas Especiais | 8-Sist. Especiais | Elevadores + piscina + automação + climatização (agrupado) |
| Revestimentos Internos Piso e Parede | 10-Rev. Int. Parede | Chapisco + reboco + cerâmicos |
| Revestimentos e Acabamentos Teto | 11-Teto | Forro gesso + reboco teto |
| Acabamentos de Piso e Parede | 12-Pisos | Contrapiso + pisos + rodapés + louças/metais |
| Pintura Interna | 13-Pintura | Sistema pintura completo |
| Esquadrias, Vidros e Ferragens | 14-Esquadrias | Alumínio + madeira + guarda-corpos + vidros |
| Cobertura | 17-Complementares | Cobertura + Serviços Complementares |
| Revestimentos e Acabamentos de Fachada | 16-Fachada | Chapisco + reboco + pintura externa |
| Serviços Complementares | 17-Complementares | Agregado com Cobertura |
| Imprevistos e Contingências | 18-Imprevistos | 1,48% do total |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 9,41 | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 311,3 | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | 0,030 | 0,06 | 0,04 |

**DESTAQUE:** AC/UR de 311,3 m²/UR é o 2º maior da base Cartesian (ao lado do Serenity com 309 m²/UR). Empreendimento de alto padrão com unidades de 4 suítes (1 apt/andar).

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | 2,0 | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | 7,0 | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | 0,091 | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial (4 suítes) | 14 | 100% | 311,3 |
| Comercial | 0 | 0% | — |
| Estúdio | 0 | 0% | — |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | 329.000² / AC | 7,5% |
| Mezanino 1 | 270.000 / AC | 6,2% |
| 2º Pavimento | 211.000 / AC | 4,8% |
| Mezanino 2 | 213.000 / AC | 4,9% |
| Lazer | 295.000 / AC | 6,8% |
| Tipo (×14) | 1.475.000 / AC | 33,8% |
| Barrilete | 123.000 / AC | 2,8% |

² Valores em R$ do orçamento (áreas não detalhadas por pavimento)

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 959.629,44 |
| R$ / UR (habitacionais) | Total / UR_H | R$ 959.629,44 |
| CUB / UR | (R$/UR) / CUB | 352,1 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 1.447.037,29 | 332,02 | 10,77% | 300 - 400 |
| 2 | Movimentação de Terra | 72.727,08 | 16,69 | 0,54% | 7 - 13 |
| 3 | Infraestrutura | 854.810,65 | 196,14 | 6,36% | 170 - 240 |
| 4 | Supraestrutura | 3.018.599,12 | 692,61 | 22,47% | 720 - 770 |
| 5 | Alvenaria | 551.049,47 | 126,44 | 4,10% | 120 - 160 |
| 6 | Impermeabilização | 174.785,54 | 40,10 | 1,30% | 30 - 60 |
| 7 | Instalações (agrupado) | 1.240.277,70 | 284,58 | 9,23% | 220 - 320 |
| 8 | Sistemas Especiais | 761.934,02 | 174,82 | 5,67% | 210 - 260 |
| 9 | Climatização | 0³ | 0 | 0% | — |
| 10 | Rev. Internos Parede | 499.530,63 | 114,62 | 3,72% | 120 - 200 |
| 11 | Teto | 146.805,21 | 33,68 | 1,09% | 50 - 70 |
| 12 | Pisos | 634.372,38 | 145,56 | 4,72% | 170 - 200 |
| 13 | Pintura | 561.657,70 | 128,87 | 4,18% | 95 - 125 |
| 14 | Esquadrias | 1.474.476,64 | 338,32 | 10,98% | 250 - 290 |
| 15 | Louças e Metais | 0³ | 0 | 0% | — |
| 16 | Fachada | 972.820,16 | 223,21 | 7,24% | 170 - 300 |
| 17 | Complementares | 824.720,72 | 189,24 | 6,14% | 110 - 200 |
| 18 | Imprevistos | 199.207,85 | 45,71 | 1,48% | — |
| — | **TOTAL** | **13.434.812,16** | **3.082,60** | **100%** | — |

³ Climatização e Louças/Metais incluídos em Sist. Especiais e Pisos, respectivamente (sem separação possível no executivo).

**DESTAQUES:**
- ⚠️ **Mov. Terra R$ 16,69/m²** — ACIMA da faixa (7-13) devido a rebaixamento de lençol freático (R$ 12.641,62)
- 🔽 **Supraestrutura R$ 692,61/m²** — abaixo da faixa (720-770), possível eficiência construtiva
- ⚠️ **Esquadrias R$ 338,32/m²** — MUITO ACIMA da faixa (250-290), 10,98% do total
- 🔽 **Teto R$ 33,68/m²** — ABAIXO da faixa (50-70), mínimo da base
- ⚠️ **Pintura R$ 128,87/m²** — ACIMA da faixa (95-125)
- 🔽 **Sist. Especiais R$ 174,82/m²** — abaixo da faixa (210-260)
- ✅ **CUB ratio 1,13** — abaixo da mediana Cartesian (~1,28), eficiente para alto padrão

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | N/D | — | 40 | 630 |
| Vigas | N/D | — | 40 | 630 |
| Lajes | N/D | — | 40→35→30⁴ | 630 |
| Escadas | N/D | — | 40 | 630 |
| **TOTAL estimado** | **1.050⁵** | **100%** | — | — |

⁴ fck reduz conforme altura (embasamento 40, tipo 35→30)
⁵ Estimado a partir de AC e índice típico 0,24 m³/m²

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto / AC | 0,241⁵ | m³/m² | 0,242 | 0,189 |

#### Armadura (Aço)

| Elemento | Peso (kg) | Taxa (kg/m³) |
|---|---|---|
| Pilares | N/D | — |
| Vigas | N/D | — |
| Lajes | N/D | — |
| Escadas | N/D | — |
| **TOTAL estimado** | **~80.000⁶** | — |

⁶ Estimado a partir de volume concreto × taxa típica 75-80 kg/m³

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Taxa de aço global | 76⁶ | kg/m³ | 82,32 | 114,88 |
| PU aço (corte/dobra obra) | N/D | R$/kg | 6,12-7,98 | — |

#### Forma

| Tipo | Área (m²) | Reutilizações | PU (R$/m²) |
|---|---|---|---|
| Compensado plastificado 17mm | N/D | 2 | N/D |
| **TOTAL estimado** | **~5.450⁷** | — | — |

⁷ Estimado a partir de AC × índice típico 1,25 m²/m²

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Forma / AC | 1,25⁷ | m²/m² | 1,25 | 1,36 |

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | PU (R$) |
|---|---|---|---|
| Tipo de laje (tipo) | Nervurada com cubetas | — | — |
| Tipo de laje (embasamento) | Maciça | — | — |
| Cubetas/EPS | Diversos | ~60-80/pav | 30.505,18 (total) |
| Escoramento | Madeira | — | 71.802,44 (total) |

#### MO Supraestrutura

| Item | Área (m²) | PU MO (R$/m²) | Obs |
|---|---|---|---|
| MO tipo + embasamento | 4.358,27 | 200 | Empreitada global |

### 4.2 Infraestrutura

#### Fundação Profunda

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | HC | — | — | Hélice Contínua |
| Estaca ø60cm | 1.810 | m | 103,09 | Perfuração (prof. média 30m) |
| **Total estacas** | **1.810** | **m** | — | **~60 un × 30m** |
| Concreto fck 30 | 512 | m³ | 654 | — |
| Aço fundação profunda CA-50 ø16mm | 2.681,6 | kg | N/D | — |
| Taxa aço fundação | 5,2 | kg/m³ | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| ML estaca / AC | 0,415 | m/m² | 0,39 | 0,19 |
| ML estaca / UR | 129,3 | m/UR | 95,6 | 15,1 |
| Nº estacas / UR | 4,3 | un/UR | 3,3 | 1,3 |

**DESTAQUE:** ML estaca/UR de 129,3 m/UR é alto, refletindo solo com baixa capacidade de carga e necessidade de estacas profundas (~30m).

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|---|
| Forma (blocos+baldrames) | 365,94 | m² | 200 (MO) |
| Concreto fck 40 | 138,51 | m³ | 630 |
| Aço (diversos diâmetros) | ~19.836 | kg | N/D |
| Taxa aço fund. rasa | 143 | kg/m³ | — |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

### 5.1 Áreas de Serviço / AC

> Dados não detalhados no executivo — estimativas não disponíveis com confiança.

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria total | N/D | N/D | 1,37 | 1,56 |
| Chapisco interno | N/D | N/D | 2,68 | 2,58 |
| Reboco/massa interna | N/D | N/D | 2,68 | 2,58 |
| Forro gesso | N/D | N/D | 0,57 | 0,16 |
| Contrapiso | N/D | N/D | 0,66 | 0,76 |
| Pintura parede | N/D | N/D | 2,34 | 1,05 |
| Fachada total | N/D | N/D | 0,73 | 1,41 |

### 5.2 Comprimentos de Serviço / AC

| Serviço | Comprimento (m) | Índice (m/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Encunhamento | N/D | N/D | 0,62 | 0,47 |
| Verga + contraverga | N/D | N/D | 0,33 | 0,13 |
| Rodapé | N/D | N/D | 0,84 | — |

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas (madeira+PCF) | N/D | N/D | 10,7 | 3,2 |
| Bacias sanitárias | ~60⁸ | ~4,3 | — | 0,4 |
| Registros | N/D | N/D | — | 0,6 |

⁸ Estimado: 4 suítes/UR × 14 UR + áreas comuns

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | 424.208,15 | 97,35 | 34,2% | N/D |
| Elétricas | 481.199,94 | 110,43 | 38,8% | N/D |
| Preventivas | 130.157,98 | 29,87 | 10,5% | N/D |
| Gás (GLP) | 42.400,00 | 9,73 | 3,4% | N/D |
| Comunicações/Telecom | 28.301,41 | 6,49 | 2,3% | N/D |
| Automações | 34.866,16 | 8,00 | 2,8% | N/D |
| Equipamentos⁹ | 99.144,06 | 22,75 | 8,0% | N/D |
| **TOTAL** | **1.240.277,70** | **284,58** | **100%** | **N/D** |

⁹ Equipamentos = parte do grupo "Equipamentos e Sistemas Especiais" que se relaciona a instalações (ex: pressurizadores, bombas)

**NOTA:** Apresentação oficial agrupa Instalações = R$ 1.240.277,70 (incluindo Telecom + Automações que no detalhado aparecem separados). Mantido conforme apresentação para consistência com benchmark.

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| MO total instalações / AC | N/D | R$/m² | 69,20 | 122,38 |
| Mat. total instalações / AC | N/D | R$/m² | 171,69 | 265,99 |
| Razão MO/Material | N/D | — | 0,40 | 0,46 |

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

> Dados não disponíveis no executivo com nível de detalhamento suficiente para extração de PUs individualizados. Valores agregados em macrogrupos.

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema completo (chapisco+reboco) | N/D | m² | N/D | N/D |
| Cerâmico parede (porcelanato) | N/D | m² | N/D | N/D |

### 7.2 Pisos

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Contrapiso | N/D | m² | N/D | N/D |
| Porcelanato | N/D | m² | N/D | N/D |
| Piso laminado | N/D | m² | N/D | N/D |

### 7.3 Teto

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Forro gesso acartonado | N/D | m² | N/D | N/D |
| Reboco teto | N/D | m² | N/D | N/D |

### 7.4 Pintura

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema completo (selador+massa+tinta) | N/D | m² | N/D | N/D |

### 7.5 Fachada

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema completo fachada | N/D | m² | N/D | N/D |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

> Dados agregados no executivo — sem detalhamento por tipo.

| Tipo | Qtd/Área | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Esquadrias (global) | N/D | — | — | 1.474.476,64 |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Esquadrias / AC | 338,32 | R$/m² | — | — |
| Esquadrias / UR | 105.319,76 | R$/UR | — | — |

**DESTAQUE:** Esquadrias representam 10,98% do total (R$ 338,32/m²), MUITO ACIMA da faixa típica de obras similares (250-290 R$/m²). Possíveis causas: alto padrão, grandes vãos de vidro, guarda-corpos especiais.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevadores Smart | 2 | N/D | N/D¹⁰ |
| Equipamentos piscina | — | — | N/D |
| Automação | — | — | 34.866,16 |
| Climatização | — | — | N/D¹¹ |
| **TOTAL (agrupado)** | — | — | **761.934,02** |

¹⁰ Elevadores incluídos no total de Sistemas Especiais (sem separação)
¹¹ Climatização incluída em Sistemas Especiais (sem separação)

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Elevador (R$/un) | N/D | R$ | 317.500 | 187.800 |
| Sistemas Especiais / AC | 174,82 | R$/m² | 96,44 | 179,87 |

**DESTAQUE:** Sistemas Especiais R$ 174,82/m² está ABAIXO da faixa típica (210-260), apesar do empreendimento ter lazer completo (piscina, academia, playground, sala de jogos, salão de festas, espaço zen). Possível eficiência na aquisição de equipamentos.

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Estudos | 19.579,00 | 4,49 |
| Projetos (diversos) | 121.509,04 | 27,88 |
| Ensaios | 21.861,00 | 5,02 |
| **TOTAL PROJETOS** | **162.949,04** | **37,39** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Consumos/Taxas/Documentos | 124.436,42 | 28,55 |

### 10.3 Equipe Administrativa

| Cargo | Qtd | Custo/mês (R$) | Meses | Total (R$) |
|---|---|---|---|---|
| Equipe ADM (global) | — | 10.888,67 | 36 | 391.992,24 |

| Índice | Valor | Un |
|---|---|---|
| Equipe ADM / AC | 89,95 | R$/m² |
| Equipe ADM / mês | 10.888,67 | R$/mês |

### 10.4 Proteção Coletiva (EPCs)

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Segurança/Meio Ambiente/Saúde | — | — | — | 237.153,92 |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Período | Custo/mês (R$) | Total (R$) |
|---|---|---|---|---|
| Equipamentos obra (global) | — | 36 | 5.323,48 | 191.645,13 |
| Carga e transporte | — | — | — | 120.000,00 |
| **TOTAL EQUIPAMENTOS** | — | — | — | **311.645,13** |

### 10.6 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 162.949,04 | 37,39 | 11,3% | 1,2% |
| Taxas e Licenças | 124.436,42 | 28,55 | 8,6% | 0,9% |
| Equipe ADM | 391.992,24 | 89,95 | 27,1% | 2,9% |
| EPCs | 237.153,92 | 54,42 | 16,4% | 1,8% |
| Equipamentos | 311.645,13 | 71,51 | 21,5% | 2,3% |
| Canteiro | 101.198,83 | 23,22 | 7,0% | 0,8% |
| Despesas ADM | 104.642,76 | 24,01 | 7,2% | 0,8% |
| Serviços Preliminares | 13.018,95 | 2,99 | 0,9% | 0,1% |
| **TOTAL CI** | **1.447.037,29** | **332,02** | **100%** | **10,77%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

> Dados incluídos no macrogrupo "Pisos" (Acabamentos) — sem separação possível.

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Louças + Metais (estimado) | — | — | — | Incluído em Pisos |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 121 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 373,2k/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 1,64 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 0,39 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 85,6 R$/m²/mês | 80,5 | 100,8 |

**NOTA:** Ritmo de 121 m²/mês é baixo comparado a referências (306-308), refletindo empreendimento verticalizado (22 pavimentos) com áreas pequenas por pavimento e ciclo longo (36 meses).

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Sistema | Área (m²) | PU Material (R$) | PU MO (R$) | Aplicação |
|---|---|---|---|---|
| Impermeabilização (global) | N/D | N/D | N/D | N/D |
| **TOTAL** | — | — | — | **174.785,54** |

| Índice | Valor | Un |
|---|---|---|
| Impermeabilização / AC | 40,10 | R$/m² |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Cobertura | 29.957,71 | 6,87 | — |
| Serviços Complementares | 794.763,01 | 182,36 | — |
| **TOTAL COMPLEMENTARES** | **824.720,72** | **189,24** | — |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

### Comparativo R$/m² AC por Macrogrupo (da apresentação oficial)

| Macrogrupo | ADDA (R$/m²) | Similares (R$/m²) | Desvio |
|---|---|---|---|
| Gerenciamento | 332,02 | 300-400 | ✅ Dentro |
| Mov. Terra | 16,69 | 7-13 | ⚠️ +28% a +139% |
| Infraestrutura | 196,14 | 170-240 | ✅ Dentro |
| Supraestrutura | 692,61 | 720-770 | 🔽 -4% a -10% |
| Alvenaria | 126,44 | 120-160 | ✅ Dentro |
| Instalações | 284,58 | 220-320 | ✅ Dentro |
| Equip/Sist Especiais | 174,82 | 210-260 | 🔽 -17% a -33% |
| Impermeabilização | 40,10 | 30-60 | ✅ Dentro |
| Rev. Int Piso/Parede | 114,62 | 120-200 | 🔽 -4% a -43% |
| Teto | 33,68 | 50-70 | 🔽 -33% a -52% |
| Acabamentos | 145,56 | 170-200 | 🔽 -14% a -27% |
| Pintura | 128,87 | 95-125 | ⚠️ +3% a +36% |
| Esquadrias | 338,32 | 250-290 | ⚠️ +17% a +35% |
| Cobertura | 6,87 | 4-10 | ✅ Dentro |
| Fachada | 223,21 | 170-300 | ✅ Dentro |
| Complementares | 182,36 | 110-200 | ✅ Dentro |

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média
- **Movimentação de Terra:** R$ 16,69/m² vs 7-13 — rebaixamento de lençol freático (R$ 12.641,62 = 74% do grupo) eleva custo
- **Pintura:** R$ 128,87/m² vs 95-125 — 3% a 36% acima da faixa, possível especificação de alto padrão
- **Esquadrias:** R$ 338,32/m² vs 250-290 — 17% a 35% acima, representando 10,98% do total. Maior destaque do projeto

### ✅ Dentro da Faixa
- **Gerenciamento:** R$ 332,02/m² — bem calibrado para empreendimento de 36 meses
- **Infraestrutura:** R$ 196,14/m² — dentro da faixa (170-240)
- **Alvenaria:** R$ 126,44/m² — alinhado (120-160)
- **Instalações:** R$ 284,58/m² — dentro da faixa (220-320)
- **Fachada:** R$ 223,21/m² — alinhado (170-300)

### 🔽 Abaixo da Média
- **Supraestrutura:** R$ 692,61/m² vs 720-770 — 4% a 10% abaixo, possível eficiência construtiva (laje nervurada + PU concreto R$ 630/m³)
- **Sistemas Especiais:** R$ 174,82/m² vs 210-260 — 17% a 33% abaixo, apesar do lazer completo
- **Teto:** R$ 33,68/m² vs 50-70 — 33% a 52% abaixo, **mínimo da base Cartesian**
- **Rev. Int. Piso/Parede:** R$ 114,62/m² vs 120-200 — 4% a 43% abaixo
- **Pisos (Acabamentos):** R$ 145,56/m² vs 170-200 — 14% a 27% abaixo

### 📝 Particularidades
- **Empreendimento verticalizado:** 22 pavimentos, 14 unidades (1 apt/andar) — ciclo longo, áreas pequenas/pav
- **Fundação desafiadora:** HC ø60cm com 30m de profundidade média — solo de baixa capacidade
- **Laje nervurada com cubetas** — eficiência estrutural
- **Sem subsolo de garagem** — embasamento acima do térreo
- **Alto padrão:** 311,3 m²/UR (2º maior da base), 4 suítes/apto, lazer completo
- **CUB ratio 1,13** — abaixo da mediana da base (~1,28), eficiente para o padrão

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 13.434.812,16 | R$ |
| **R$/m²** | 3.082,60 | R$/m² |
| **CUB ratio** | 1,13 | CUB |
| **R$/UR** | 959.629,44 | R$/UR |
| **AC/UR** | 311,3 | m²/un |
| Concreto supra / AC | 0,241 | m³/m² |
| Taxa aço supra | 76 | kg/m³ |
| Forma / AC | 1,25 | m²/m² |
| Estacas / AC | 0,415 | m/m² |
| Estacas / UR | 129,3 | m/UR |
| Elevador / UR | 7,0 | UR/elev |
| Ritmo construção | 121 | m²/mês |
| Burn rate | R$ 373,2k | R$/mês |
| Meses por pavimento | 1,64 | meses/pav |

---

> **Fonte:** Orçamento Executivo R02 (Set/2023) + Apresentação Oficial
> **Extraído em:** 06/03/2026
> **Notas:** Executivo com nível de agregação médio. Alguns índices de consumo (áreas de serviço, quantitativos detalhados) não disponíveis. Dados de equipamentos/sistemas especiais agrupados sem separação por item. Louças/metais incluídos em Acabamentos. Climatização incluída em Sistemas Especiais.
