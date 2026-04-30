# Águas de Março — Inbrasul Empreendimentos

> Orçamento executivo extraído e normalizado para base paramétrica.
> Criado: 06/03/2026
> Projeto código: Águas de Março (Inbrasul)

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Águas de Março | — |
| Código CTN | — | CTN-INBR-ADM | — |
| Revisão | — | Executivo | — |
| Localização | — | Navegantes/SC | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Inbrasul Empreendimentos | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | 6.538,41 | m² |
| Unid. Habitacionais | UR_H | 45 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 45 | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 41 | meses |
| Data-base | — | Jan/2023 | — |
| **CUB na Data-base** | — | **R$ 2.651,17** | **R$** |
| R$/m² Total | — | 3.722,92 | R$/m² |
| **R$/m² Calibração** | — | **3.528,02** | **R$/m²** |
| CUB ratio | — | 1,33 | CUB |
| **CUB ratio Calibração** | — | **1,33** | **CUB** |
| Tipo de Laje | — | N/D | — |
| Tipo de Fundação | — | Hélice Contínua | — |
| Padrão Acabamento | — | Médio-Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | Marketing Online + Comissão de Vendas |
| Valor ADM (se separado) | R$ 1.275.000 | 5,24% do total bruto |
| **Tem MOE (Mão de Obra) separado?** | Não | — |
| Valor MOE (se separado) | — | — |
| Metodologia de rateio MOE | — | Incluído nos macrogrupos |
| Custos diretos de obra (sem ADM/MOE) | R$ 16.507.447,73 | 67,86% do total bruto |
| **Total para calibração** | **R$ 23.066.958,32** | **Excluído Marketing/Vendas** |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| Movimentação de Terra | 2-Mov. Terra | — |
| Infraestrutura | 3-Infraestrutura | Fundações HC |
| Supraestrutura | 4-Supraestrutura | Concreto 40 MPa estacas / 35 MPa blocos / 30-35 MPa supra |
| Alvenaria | 5-Alvenaria | — |
| Instalações (elétr+hidro+prev+GLP) | 7-Instalações | Agrupado |
| Sist. Especiais/Equipamentos | 8-Sist. Especiais | — |
| Impermeabilização | 6-Impermeabilização | — |
| Rev. Int. Piso/Parede | 10-Rev.Int.Parede + 12-Pisos | Separado proporcionalmente (46% parede, 54% piso) |
| Rev./Acab. Teto | 11-Teto | — |
| Acabamentos Piso/Parede | 12-Pisos (parte) | Distribuído com Rev. Int. |
| Pintura Interna | 13-Pintura | — |
| Esquadrias | 14-Esquadrias | — |
| Fachada | 16-Fachada | — |
| Cobertura | 17-Complementares | Reclassificado |
| Serv. Complementares | 17-Complementares | — |
| Gerenciamento | 1-Gerenciamento | **Excluído R$ 1.275.000 de Marketing/Vendas** |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | N/D | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 145,3 m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | N/D | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | N/D | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | N/D | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | 45 | 100% | 145,3 |
| Comercial | 0 | 0% | — |
| Estúdio | 0 | 0% | — |

### 2.4 Distribuição de Áreas por Pavimento

N/D — dados não disponíveis no orçamento resumo.

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 512.599 |
| R$ / UR (habitacionais) | Total / UR_H | R$ 512.599 |
| CUB / UR | (R$/UR) / CUB | 193,4 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Os 18 macrogrupos padrão da base paramétrica Cartesian.
> **ATENÇÃO:** O total original (R$ 24.341.958,32) inclui R$ 1.275.000 de Marketing Online + Comissão de Vendas que foram EXCLUÍDOS da calibração.

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 6.559.510,59 | 1.003,34 | 28,44% | 200 - 512 |
| 2 | Movimentação de Terra | 33.815,95 | 5,17 | 0,15% | 6 - 97 |
| 3 | Infraestrutura | 943.165,40 | 144,26 | 4,09% | 115 - 512 |
| 4 | Supraestrutura | 4.008.471,42 | 613,13 | 17,38% | 595 - 979 |
| 5 | Alvenaria | 843.889,59 | 129,08 | 3,66% | 104 - 361 |
| 6 | Impermeabilização | 272.726,87 | 41,71 | 1,18% | 33 - 86 |
| 7 | Instalações (agrupado) | 1.789.257,66 | 273,68 | 7,76% | 234 - 540 |
| 8 | Sistemas Especiais | 862.123,70 | 131,85 | 3,74% | 118 - 425 |
| 9 | Climatização | 0,00 | 0,00 | 0,00% | 22 - 105 |
| 10 | Rev. Internos Parede | 1.085.513,00 | 166,01 | 4,71% | 97 - 254 |
| 11 | Teto | 447.446,78 | 68,44 | 1,94% | 51 - 127 |
| 12 | Pisos | 1.264.081,80 | 193,35 | 5,48% | 118 - 551 |
| 13 | Pintura | 683.055,84 | 104,46 | 2,96% | 84 - 194 |
| 14 | Esquadrias | 1.934.549,11 | 295,91 | 8,39% | 249 - 991 |
| 15 | Louças e Metais | 0,00 | 0,00 | 0,00% | 33 - 33 |
| 16 | Fachada | 879.244,97 | 134,49 | 3,81% | 57 - 279 |
| 17 | Complementares | 1.460.105,64 | 223,33 | 6,33% | 104 - 995 |
| 18 | Imprevistos | 0,00 | 0,00 | 0,00% | 34 - 122 |
| — | **TOTAL** | **23.066.958,32** | **3.528,02** | **100%** | — |

**Normalizado para CUB base dez/2023 (R$ 2.752,67):**
- Fator de normalização: 2.752,67 / 2.651,17 = **1,0383**
- **R$/m² normalizado: R$ 3.663,14**
- **CUB ratio normalizado: 1,33**

| # | Macrogrupo | R$/m² Normalizado | % |
|---|---|---|---|
| 1 | Gerenciamento | 1.041,77 | 28,44% |
| 2 | Mov. Terra | 5,37 | 0,15% |
| 3 | Infraestrutura | 149,79 | 4,09% |
| 4 | Supraestrutura | 636,62 | 17,38% |
| 5 | Alvenaria | 134,02 | 3,66% |
| 6 | Impermeabilização | 43,31 | 1,18% |
| 7 | Instalações | 284,16 | 7,76% |
| 8 | Sist. Especiais | 136,90 | 3,74% |
| 9 | Climatização | 0,00 | 0,00% |
| 10 | Rev. Int. Parede | 172,37 | 4,71% |
| 11 | Teto | 71,06 | 1,94% |
| 12 | Pisos | 200,76 | 5,48% |
| 13 | Pintura | 108,46 | 2,96% |
| 14 | Esquadrias | 307,25 | 8,39% |
| 15 | Louças | 0,00 | 0,00% |
| 16 | Fachada | 139,64 | 3,81% |
| 17 | Complementares | 231,86 | 6,33% |
| 18 | Imprevistos | 0,00 | 0,00% |
| — | **TOTAL** | **3.663,14** | **100%** |

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

N/D — dados detalhados não disponíveis no orçamento resumo.

#### Armadura (Aço)

N/D — dados detalhados não disponíveis.

**Especificações mencionadas:**
- Concreto 40 MPa (estacas)
- Concreto 35 MPa (blocos)
- Concreto 30-35 MPa (supraestrutura)
- Forma plastificada
- **Corte/dobra EM OBRA** (impacta custo de armadura)

#### Forma

N/D — dados detalhados não disponíveis.

**Especificação mencionada:** Forma plastificada

### 4.2 Infraestrutura

#### Fundação Profunda

**Tipo:** Hélice Contínua (HC)

**Especificação mencionada:**
- HC 40-60cm (diâmetros variados)
- Concreto fck 40 MPa

Dados quantitativos N/D.

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

N/D — levantamento detalhado de áreas não disponível no orçamento resumo.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. |
|---|---|---|---|
| Elétricas | N/D | N/D | N/D |
| Hidrossanitárias | N/D | N/D | N/D |
| Preventivas | N/D | N/D | N/D |
| Gás (GLP) | Incluído | — | — |
| **TOTAL** | **1.789.257,66** | **273,68** | **100%** |

**Nota:** Orçamento resumo apresenta instalações agrupadas (elétr+hidro+prev+GLP). Sem breakdown detalhado.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

N/D — PUs e levantamentos de área não disponíveis no orçamento resumo.

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

N/D — dados detalhados não disponíveis.

**Total:** R$ 1.934.549,11 (R$ 295,91/m²)

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

N/D — dados detalhados não disponíveis.

**Total:** R$ 862.123,70 (R$ 131,85/m²)

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

**Especificidade mencionada:**
- **Consultoria CINDACTA** (durante todo o prazo de 41 meses)
- **Laudo de vizinhança**

Valores detalhados N/D.

### 10.2 Resumo CI

Incluído no macrogrupo **Gerenciamento** (R$ 6.559.510,59 — 28,44% do total).

**ATENÇÃO:** Este valor já exclui os R$ 1.275.000 de Marketing/Vendas do gerenciamento total original.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

N/D — não há linha específica no orçamento resumo.

**Total:** R$ 0 (provavelmente incluído em Complementares ou outra categoria)

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 159 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 562,6k/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | N/D | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 1,1 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 86,05 R$/m²/mês | 80,5 | 100,8 |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

N/D — dados detalhados não disponíveis.

**Total:** R$ 272.726,87 (R$ 41,71/m²)

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Serv. Complementares | 1.376.053,18 | 210,49 | — |
| Cobertura | 84.052,46 | 12,86 | — |
| **TOTAL** | **1.460.105,64** | **223,33** | — |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

N/D — não há aba comparativa no orçamento resumo.

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Muito Acima da Média

- **Gerenciamento: R$ 1.003/m² vs mediana R$ 431/m²** (+133%)
  - **MOTIVO IDENTIFICADO:** Gerenciamento total original = R$ 7.834.510 (32% do projeto), incluindo:
    - Marketing Online: R$ 445.000
    - Comissão de Vendas: R$ 830.000
    - **Total Marketing/Vendas: R$ 1.275.000** (excluído da calibração)
  - Mesmo após exclusão, Gerenciamento construtivo = R$ 6.559.510 (28,4%) permanece **MUITO ALTO**
  - Possíveis causas adicionais:
    - Consultoria CINDACTA durante 41 meses
    - Complexidade gestão Navegantes
    - Prazo longo (41 meses) aumenta custo de equipe ADM

### ✅ Dentro da Faixa

- **Infraestrutura:** R$ 144/m² (faixa 115-235, mediana 226) — **ABAIXO da mediana** (possivelmente HC mais simples)
- **Supraestrutura:** R$ 613/m² (faixa 595-979, mediana 710) — **OK**
- **Alvenaria:** R$ 129/m² (faixa 104-361, mediana 146) — **OK**
- **Instalações:** R$ 274/m² (faixa 234-540, mediana 366) — **OK**
- **Rev.Int.Parede:** R$ 166/m² (faixa 97-254, mediana 168) — **OK**
- **Pisos:** R$ 193/m² (faixa 118-551, mediana 196) — **OK**
- **Esquadrias:** R$ 296/m² (faixa 249-991, mediana 356) — **OK**
- **Fachada:** R$ 135/m² (faixa 57-279, mediana 142) — **OK**

### 🔽 Abaixo da Média

- **Mov. Terra:** R$ 5/m² vs mediana R$ 16/m² — Terreno plano ou movimentação mínima
- **Imprevistos:** R$ 0 — **SEM LINHA DE IMPREVISTOS** (risco alto — benchmark 2-5%)

### 📝 Particularidades

- **Corte/dobra EM OBRA** (não em fornecedor externo) — pode aumentar custo de MO e prazo
- **Consultoria CINDACTA 41 meses** — exigência aeronáutica (Navegantes próximo ao aeroporto)
- **Laudo de vizinhança** — área com construções próximas
- **Climatização = R$ 0** — sem sistema centralizado ou embutido em Sist.Especiais
- **Louças = R$ 0** — não separado (incluído em outra categoria)
- **Forma plastificada** — reutilizável, pode reduzir custo

---

## RESUMO DE ÍNDICES GLOBAIS

> Quick reference — os números mais importantes do projeto.

| Indicador | Valor | Un |
|---|---|---|
| **Custo total (calibração)** | R$ 23.066.958 | R$ |
| **Custo total (original c/ marketing)** | R$ 24.341.958 | R$ |
| **R$/m² (calibração)** | 3.528 | R$/m² |
| **R$/m² (normalizado dez/23)** | 3.663 | R$/m² |
| **CUB ratio** | 1,33 | CUB |
| **R$/UR** | R$ 512.599 | R$/UR |
| **AC/UR** | 145,3 | m²/un |
| Gerenciamento / Total | 28,4% | — |
| Ritmo construção | 159 | m²/mês |
| Burn rate | R$ 563k | R$/mês |

---

> **Fonte:** Orçamento Resumo Águas de Março — Inbrasul Empreendimentos
> **Extraído em:** 06/03/2026
> **Notas:**
> - **GERENCIAMENTO ALTO:** Total original R$ 7.834.510 (32%) incluía R$ 1.275.000 de Marketing/Vendas (excluído da calibração)
> - **SEM IMPREVISTOS:** Orçamento não prevê linha de imprevistos (risco)
> - **Consultoria CINDACTA:** Exigência aeronáutica durante todo o prazo (41 meses)
> - **Corte/dobra em obra:** Armadura preparada no canteiro (não terceirizada)
> - Dados estruturais detalhados (volumetria, aço, forma) não disponíveis no resumo fornecido
