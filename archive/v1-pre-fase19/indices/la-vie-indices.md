# La Vie — MG3 Construtora (Padrão M3V)

> Orçamento executivo — Balneário Camboriú/SC
> Data-base: Mai/2023 | CUB: R$ 2.688,94 (SC)
> Extraído em: 06/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | La Vie | — |
| Código CTN | — | — | — |
| Revisão | — | 22/05/2023 | — |
| Localização | — | Balneário Camboriú/SC | — |
| Endereço | — | Rua 3150, 390 - Centro | — |
| Incorporador/Cliente | — | MG3 (Padrão M3V) | — |
| Área do Terreno | AT | 945 | m² |
| Área Construída | AC | 10.125,08 | m² |
| Unid. Habitacionais | UR_H | ~30 | un |
| Unid. Comerciais | UR_C | — | un |
| Estúdios | UR_E | — | un |
| Total Unidades | UR | ~30 | un |
| Nº Total Pavimentos | NP | 24 | un |
| Nº Pavimentos Tipo | NPT | 15 | un |
| Nº Pav. Garagem | NPG | 3 | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 36 | meses |
| Data-base | — | Mai/2023 | — |
| **CUB na Data-base** | — | **R$ 2.688,94** | **R$** |
| R$/m² Total (COM trib) | — | 3.115,58 | R$/m² |
| R$/m² Total (SEM trib) | — | 2.803,22 | R$/m² |
| CUB ratio (COM trib) | — | 1,16 | CUB |
| CUB ratio (SEM trib) | — | 1,04 | CUB |
| Tipo de Laje | — | Nervurada (fôrma plástica locada) | — |
| Tipo de Fundação | — | Hélice Contínua + blocos/baldrames | — |
| Padrão Acabamento | — | Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Não | Gerenciamento global (projetos + ADM + equipamentos) |
| Valor ADM (se separado) | — | — |
| **Tem MOE (Mão de Obra) separado?** | Não | Embutida nos custos diretos |
| Valor MOE (se separado) | — | — |
| Metodologia de rateio MOE | — | — |
| Custos diretos de obra (sem ADM/MOE) | R$ 27.850.890,22 | 88,30% do total |
| **DESPESAS TRIBUTÁRIAS** | R$ 3.159.943,06 | 10% do total — EXCLUÍDAS DA CALIBRAÇÃO |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| 01 Serviços Técnicos | 1-Gerenciamento | Projetos R$ 665k, estudos, consultorias, ensaios, licenças |
| 02 Serviços Iniciais | 1-Gerenciamento | Segurança, ADM, canteiro, equipamentos (grua, elevador) |
| 01 Movimentação de Terra | 2-Mov. Terra | — |
| 02 Infraestrutura | 3-Infraestrutura | HC + blocos + baldrames |
| 03 Supraestrutura | 4-Supraestrutura | Concreto 40 MPa, laje nervurada, fôrma locada |
| 04 Paredes e Painéis | 5-Alvenaria | Cerâmico + celular autoclavado + drywall + corta-fogo |
| 05 Impermeabilização e Tratamentos | 6-Impermeabilização | — |
| 06 Sist. Instalações Hidrossanitárias | 7-Instalações | — |
| 07 Sist. Instalações Elétricas | 7-Instalações | — |
| 08 Instalações Preventivas e GLP | 7-Instalações | — |
| 09 Equipamentos e Sistemas Especiais | 8-Sist. Especiais | — |
| 10 Climatização, Exaustão e Pressurização | 9-Climatização | Separado! R$ 899.200 |
| 11 Revestimentos Internos de Parede | 10-Rev. Int. Parede | — |
| 12 Rev. e Acabamentos Internos em Teto | 11-Teto | — |
| 13 Pisos e Pavimentações | 12-Pisos | — |
| 14 Sistemas de Pintura Interna | 13-Pintura | — |
| 15 Esquadrias, Vidros e Ferragens | 14-Esquadrias | — |
| 16 Louças e Metais | 15-Louças e Metais | Separado! R$ 374.574 |
| 17 Rev. e Acabamentos em Fachada | 16-Fachada | Textura projetada (sem ACM/pastilha) |
| 18 Serviços Complementares e Finais | 17-Complementares | — |
| 19 Despesas Tributárias | 18-Imprevistos | EXCLUÍDO DA CALIBRAÇÃO |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 10,71 | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 337,5 m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | 0,03 un/m² | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | N/D | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | N/D | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | ~30 | 100% | ~337 |
| Comercial | 0 | 0% | — |
| Estúdio | 0 | 0% | — |

**Nota:** 15 tipos distintos (Tipo 01 a Tipo 15), estimativa ~2 apts por andar = 30 UR.

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | N/D | N/D |
| Mezanino | N/D | N/D |
| Garagem (G01, G02, G03) | N/D | N/D |
| Lazer | N/D | N/D |
| Tipo (×15) | N/D | N/D |
| Dif. Inferior (DINF) | N/D | N/D |
| Dif. Superior (DSUP) | N/D | N/D |
| Cobertura (COB) | N/D | N/D |
| Casa de Máquinas (CMQ) | N/D | N/D |

**Nota:** Dados não disponíveis — XLSX contém quantitativos ARQ (não áreas por pavimento).

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) — SEM trib | Total / UR | R$ 946.093 |
| R$ / UR (habitacionais) — SEM trib | Total / UR_H | R$ 946.093 |
| CUB / UR — SEM trib | (R$/UR) / CUB | 351,9 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Valores SEM Despesas Tributárias (R$ 3.159.943,06 excluídas).

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 3.691.863,57 | 364,62 | 13,01% | 290 - 507 |
| 2 | Movimentação de Terra | 112.462,51 | 11,11 | 0,40% | 9 - 25 |
| 3 | Infraestrutura | 1.587.263,65 | 156,76 | 5,59% | 173 - 244 |
| 4 | Supraestrutura | 6.159.048,54 | 608,30 | 21,70% | 635 - 767 |
| 5 | Alvenaria | 1.583.047,71 | 156,35 | 5,58% | 121 - 162 |
| 6 | Impermeabilização | 575.981,36 | 56,89 | 2,03% | 43 - 65 |
| 7 | Instalações (agrupado) | 2.641.541,44 | 260,90 | 9,31% | 285 - 389 |
| 8 | Sistemas Especiais | 1.134.830,40 | 112,10 | 4,00% | 140 - 214 |
| 9 | Climatização | 899.200,00 | 88,81 | 3,17% | 25 - 105 |
| 10 | Rev. Internos Parede | 924.493,78 | 91,33 | 3,26% | 119 - 198 |
| 11 | Teto | 806.642,07 | 79,67 | 2,84% | 48 - 74 |
| 12 | Pisos | 1.843.361,59 | 182,07 | 6,49% | 150 - 223 |
| 13 | Pintura | 1.199.239,13 | 118,42 | 4,23% | 99 - 163 |
| 14 | Esquadrias | 2.387.171,47 | 235,77 | 8,41% | 295 - 407 |
| 15 | Louças e Metais | 374.574,29 | 37,00 | 1,32% | 33 - 33 |
| 16 | Fachada | 842.952,08 | 83,26 | 2,97% | 109 - 184 |
| 17 | Complementares | 1.619.137,14 | 159,96 | 5,70% | 135 - 235 |
| 18 | Imprevistos | 0,00 | 0,00 | 0,00% | — |
| — | **TOTAL (SEM TRIB)** | **28.382.810,73** | **2.803,22** | **100%** | — |

**Total COM Tributárias:** R$ 31.542.753,79 (R$ 3.115,58/m², CUB ratio 1,16)

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | N/D | N/D | 40 | 630 |
| Vigas | N/D | N/D | 40 | 630 |
| Lajes | N/D | N/D | 40 | 630 |
| Escadas | N/D | N/D | 40 | 630 |
| **TOTAL Supra** | **2.217,51** | **100%** | — | — |
| **Estacas HC** | **879** | — | 40 | 816 |
| **Blocos/Baldrames** | **179,29** | — | 40 | 630 |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto supra / AC | 0,219 | m³/m² | 0,242 | 0,189 |

**⚠️ DESTAQUE:** Concreto estacas R$ 816/m³ — MUITO acima do usual (R$ 500-630). Premium BC pricing.

#### Armadura (Aço)

| Elemento | Peso (kg) | Taxa (kg/m³) |
|---|---|---|
| N/D | N/D | N/D |

#### Forma

| Tipo | Área (m²) | Reutilizações | PU (R$/m²) |
|---|---|---|---|
| Fôrma plástica (laje nervurada) | LOCADA | — | R$ 316.800 (locação global) |
| Escoramento metálico | LOCADO | — | Incluído no total |

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | PU (R$) |
|---|---|---|---|
| Tipo de laje (tipo) | Nervurada (fôrma plástica locada) | — | — |
| Tipo de laje (embasamento) | Idem | — | — |
| Cubetas/EPS (se aplicável) | Fôrma plástica reutilizável | — | — |
| Escoramento | Metálico locado | — | — |

#### Equipamentos Grandes (Carga Vertical)

| Equipamento | Tipo | Custo Total (R$) |
|---|---|---|
| Grua | AQUISIÇÃO | 216.000 |
| Grua — Montagem/Desmontagem | — | 55.000 |
| Grua — Mobilização | — | 24.000 |
| Grua — Manutenção | — | 18.000 |
| Grua — Ascensão | — | 45.000 |
| **TOTAL GRUA** | — | **358.000** |
| Elevador Cremalheira | OBRA | Incluído em equipamentos |

**⚠️ DESTAQUE:** Grua COMPRADA (não locada) — decisão estratégica MG3.

### 4.2 Infraestrutura

#### Fundação Profunda

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | HC | — | — | Perfuração realizada |
| Perfuração HC | 879 | m³ concreto | 816 | fck 40, slump 24±2 |
| **Total estacas** | **879** | **m³** | **816** | **R$ 221.400 realizado** |
| Concreto fck 40 (estacas) | 879 | m³ | 816 | ALTO (usual R$ 500-630) |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| m³ estaca / AC | 0,087 | m³/m² | 0,39 (ML) | 0,19 (ML) |

**Nota:** Dados em volume concreto (não ML perfuração) — diâmetros não especificados.

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|
| Forma (blocos+baldrames) | N/D | m² | N/D |
| Concreto fck 40 | 179,29 | m³ | 630 |
| Aço | N/D | kg | N/D |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> Dados do XLSX BIM (quantitativos arquitetônicos). Não é planilha de custo.

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria cerâmica 11,5cm | 2.829 | 0,28 | — | — |
| Alvenaria cerâmica 14cm | 2.725 | 0,27 | — | — |
| Drywall 7cm (lã de rocha) | 4.285 | 0,42 | — | — |
| Drywall 9cm (lã de rocha) | 315 | 0,03 | — | — |
| Alv. corta-fogo 12,5cm | 1.708 | 0,17 | — | — |
| **Alvenaria total estimada** | **~11.862** | **1,17** | 1,37 | 1,56 |
| Fachada (estrutura + alv.) | 5.876 | 0,58 | 0,73 | 1,41 |

**⚠️ NOTA:** Índice alvenaria 1,17 m²/m² — na faixa esperada, mas abaixo da mediana (1,37-1,56). Drywall extensivo (4.600 m²) reduz alv. convencional.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | 1.085.307,58 | 107,18 | 41,08% | N/D |
| Elétricas | 1.155.192,41 | 114,08 | 43,73% | N/D |
| Preventivas + GLP | 401.041,45 | 39,61 | 15,18% | N/D |
| **TOTAL** | **2.641.541,44** | **260,90** | **100%** | **N/D** |

**⚠️ NOTA:** Instalações R$ 260,90/m² — ABAIXO da mediana (~352/m²). Eficiente.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| N/D | N/D | N/D | N/D | N/D |

### 7.2 Pisos

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Porcelanato 80×160 | N/D | m² | N/D | N/D |
| Vinílico | N/D | m² | N/D | N/D |
| Pedras (áreas comuns) | N/D | m² | N/D | N/D |

**⚠️ DESTAQUE:** Pisos R$ 182/m² — ALTO, condizente com acabamentos premium.

### 7.3 Teto

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Drywall extensivo | N/D | m² | N/D | N/D |

**⚠️ DESTAQUE:** Teto R$ 79,67/m² — na faixa ALTA (mediana 61,70). Drywall extensivo.

### 7.5 Fachada

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Textura projetada (cinza claro/médio/escuro/branca) | N/D | m² | N/D | N/D |
| STO 3mm | N/D | m² | N/D | N/D |

**⚠️ DESTAQUE:** Fachada R$ 83,26/m² — BAIXO para BC! Textura projetada (sem ACM/pastilha/pedra).

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

| Tipo | Qtd/Área | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| N/D | N/D | N/D | N/D | 2.387.171,47 |

**⚠️ DESTAQUE:** Esquadrias R$ 235,77/m² — dentro da faixa (295-407), mas com vidros de fachada significativos.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| N/D | N/D | N/D | 1.134.830,40 |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|
| Sistemas Especiais / AC | 112,10 | R$/m² | 96,44 | 179,87 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Projetos diversos | 665.000 | 65,68 |
| Estudos | 45.000 | 4,44 |
| Consultorias | 30.000 | 2,96 |
| **TOTAL PROJETOS** | **740.000** | **73,08** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Licenças/Taxas | 97.701 | 9,65 |
| **TOTAL TAXAS** | **97.701** | **9,65** |

### 10.3 Ensaios Tecnológicos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Ensaios diversos | 45.000 | 4,44 |
| **TOTAL ENSAIOS** | **45.000** | **4,44** |

### 10.4 Segurança e SMS

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Segurança/SMS | 514.000 | 50,76 |
| **TOTAL SEGURANÇA** | **514.000** | **50,76** |

### 10.5 Administração e Canteiro

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Administração + Canteiro | 1.559.000 | 153,96 |
| **TOTAL ADM** | **1.559.000** | **153,96** |

### 10.6 Demolições e Limpeza

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Demolições/Limpeza terreno | 126.000 | 12,44 |
| **TOTAL DEMOLIÇÕES** | **126.000** | **12,44** |

### 10.7 Equipamentos (Grua + Elevador)

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Grua (aquisição + montagem + etc) | 358.000 | 35,36 |
| Elevador cremalheira | incluído | — |
| Outros equipamentos | 250.000 | 24,69 |
| **TOTAL EQUIPAMENTOS** | **608.000** | **60,05** |

### 10.8 Resumo CI (Gerenciamento)

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 740.000 | 73,08 | 20,05% | 2,61% |
| Taxas e Licenças | 97.701 | 9,65 | 2,65% | 0,34% |
| Ensaios | 45.000 | 4,44 | 1,22% | 0,16% |
| Segurança/SMS | 514.000 | 50,76 | 13,92% | 1,81% |
| Administração + Canteiro | 1.559.000 | 153,96 | 42,23% | 5,49% |
| Demolições/Limpeza | 126.000 | 12,44 | 3,41% | 0,44% |
| Equipamentos | 608.000 | 60,05 | 16,47% | 2,14% |
| **TOTAL CI** | **3.691.863,57** | **364,62** | **100%** | **13,01%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| N/D | N/D | N/D | N/D | 374.574,29 |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | R$ 12.486 | R$/UR |
| Louças+Metais / AC | 37,00 | R$/m² |

**✨ DESTAQUE:** Louças e Metais SEPARADOS no orçamento — R$ 37/m². Um dos poucos projetos da base com louças destacadas.

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 281 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 788k/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 1,5 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 0,8 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 77,9 R$/m²/mês | 80,5 | 100,8 |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Sistema | Área (m²) | PU Material (R$) | PU MO (R$) | Aplicação |
|---|---|---|---|---|
| N/D | N/D | N/D | N/D | N/D |

**Total Impermeabilização:** R$ 575.981,36 (R$ 56,89/m²) — na mediana (50-65).

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| N/D | 1.619.137,14 | 159,96 | — |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

### Projetos de Referência (Balneário Camboriú)

| Projeto | Cidade | AC (m²) | Pavimentos | Prazo | CUB | R$/m² |
|---|---|---|---|---|---|---|
| Brisa Armação | Penha/SC | 6.907 | 22 | N/D | 2.752,67 | 3.890,51 |
| BD Campeche | Floripa/SC | 3.633 | N/D | N/D | 3.012,64 | 5.709,79 |

**Nota:** La Vie R$ 2.803/m² (sem trib) — ABAIXO de referências similares BC/Penha. Eficiente para o padrão.

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média

- **Alvenaria R$ 156,35/m²** — ALTO! Mas inclui drywall extensivo (4.285 m² DW 7cm + 315 m² DW 9cm + 1.708 m² corta-fogo 12,5cm). Mediana esperada ~146.
- **Concreto Estacas R$ 816/m³** — MUITO acima do usual (R$ 500-630). Premium BC pricing + fck 40.

### ✅ Dentro da Faixa

- **Climatização R$ 88,81/m²** — Separada! Valor alto, condizente com BC (faixa 25-105).
- **Louças e Metais R$ 37/m²** — Um dos poucos projetos com louças separadas na base.
- **Pisos R$ 182/m²** — Alto, condizente com acabamentos premium (porcelanato 80×160, vinílico, pedras).
- **Esquadrias R$ 235,77/m²** — Dentro da faixa (295-407), mas com vidros de fachada significativos.
- **Teto R$ 79,67/m²** — Na faixa alta (48-74), drywall extensivo.

### 🔽 Abaixo da Média

- **Supraestrutura R$ 608/m²** — ABAIXO da mediana (~700). Eficiente para o porte (laje nervurada locada).
- **Fachada R$ 83,26/m²** — BAIXO para BC! Textura projetada (sem ACM/pastilha/pedra). Mediana esperada ~140.
- **Instalações R$ 260,90/m²** — ABAIXO da mediana (~352). Eficiente.

### 📝 Particularidades

- **Despesas Tributárias R$ 3,16M (10%)** — EXCLUÍDAS da calibração. Maioria dos projetos não inclui tributos no executivo.
- **Grua COMPRADA** — R$ 358k total (aquisição + montagem + manutenção + ascensão). Decisão estratégica MG3.
- **Laje Nervurada Locada** — Fôrma plástica reutilizável (R$ 316.800 locação). Reduz custo vs aquisição.
- **3 Subsolos (G01, G02, G03)** — 24 pavimentos totais. Terreno 945 m², CA 10,71 — aproveitamento intenso.
- **15 Tipos Distintos (Tipo 01-15)** — Alta variação tipológica (+ DINF, DSUP, COB).

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total (SEM trib)** | R$ 28.382.810,73 | R$ |
| **Custo total (COM trib)** | R$ 31.542.753,79 | R$ |
| **R$/m² (SEM trib)** | 2.803,22 | R$/m² |
| **R$/m² (COM trib)** | 3.115,58 | R$/m² |
| **CUB ratio (SEM trib)** | 1,04 | CUB |
| **CUB ratio (COM trib)** | 1,16 | CUB |
| **R$/UR (SEM trib)** | R$ 946.093 | R$/UR |
| **AC/UR** | 337,5 | m²/un |
| Concreto supra / AC | 0,219 | m³/m² |
| Alvenaria / AC | ~1,17 | m²/m² |
| Ritmo construção | 281 | m²/mês |
| Burn rate | R$ 788k | R$/mês |

---

> **Fonte:** Orçamento executivo MG3, versão 22/05/2023
> **Extraído em:** 06/03/2026
> **Notas:** Total original R$ 31.542.753,79 inclui Despesas Tributárias R$ 3.159.943,06 (excluídas para calibração). AC estimado via área de supraestrutura MO (10.125,08 m²). UR estimado via 15 tipos × 2 apt/andar = ~30 UR.
