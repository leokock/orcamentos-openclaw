# Parkside Rio Branco | Índices de Orçamento Executivo

> **Projeto:** Parkside Rio Branco | **Cliente:** Parkside  
> **Localização:** Av. Rio Branco, Centro, Florianópolis/SC  
> **Data-base:** Set/2025 | **CUB/SC:** R$ 2.978,02 (ago/2025)  
> **Extração:** 06/03/2026 (projeto base paramétrica)

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Parkside Rio Branco | — |
| Código CTN | — | PKS-RBR | — |
| Revisão | — | Executivo | — |
| Localização | — | Av. Rio Branco, Centro, Florianópolis/SC | — |
| Incorporador/Cliente | — | Parkside | — |
| Área do Terreno | AT | 884,99 | m² |
| Área Construída | AC | 8.660,10 | m² |
| Área Privativa | AP | 5.303,81 | m² |
| Unid. Habitacionais | UR_H | 160 | un |
| Unid. Comerciais | UR_C | 3 | un |
| Total Unidades | UR | 163 | un |
| Nº Total Pavimentos | NP | 22 | un |
| Nº Pavimentos Tipo | NPT | 15 | un |
| Nº Pav. Garagem | NPG | 2 | un |
| Prazo de Obra | — | 33 | meses |
| Data-base | — | Set/2025 | — |
| **CUB na Data-base** | — | **R$ 2.978,02** | **R$** |
| **CUB normalizado (dez/2023)** | — | **R$ 2.752,67** | **R$** |
| R$/m² Total (com ger., COM enxoval) | — | 4.753,80 | R$/m² |
| R$/m² Total (sem ger., sem imprev., COM enxoval) | — | 4.402,82 | R$/m² |
| **R$/m² Total (sem ger., sem imprev., SEM enxoval)** | **—** | **3.559,33** | **R$/m²** |
| **R$/m² norm. (sem ger., SEM enxoval)** | — | **3.290,27** | **R$/m²** |
| **R$/m² norm. (com ger., SEM enxoval)** | — | **3.544,10** | **R$/m²** |
| CUB ratio (com ger., COM enxoval) | — | 1,60 | CUB |
| **CUB ratio (sem ger., SEM enxoval)** | **—** | **1,20** | **CUB** |
| Tipo de Laje | — | Concreto armado | — |
| Tipo de Fundação | — | Sapatas + Cortina de contenção | — |
| Padrão Acabamento | — | Studios mobiliados (médio/alto) | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | Gerenciamento Técnico e ADM (R$ 2.197.602,25) |
| **Tem MOE (Mão de Obra) separado?** | **Sim** | **Empreitada Global R$ 10.831.779 (26,3% do total)** |
| **Tem ENXOVAL separado?** | **Sim** | **R$ 10.344.375 (25,1% do total) — EXCLUIR** |
| **Custos diretos de obra (sem ger., sem imprev., SEM enxoval)** | R$ 30.824.031 | Base para índices |
| **Custos diretos de obra (sem ger., sem imprev., COM enxoval)** | R$ 41.168.406 | Valor bruto executivo |
| **Custos totais (com ger., SEM enxoval)** | R$ 30.698.649 | Sem imprevistos |

> **⚠️ NOTA CRÍTICA — ENXOVAL MOBILIADO:**  
> Este é um prédio de **studios MOBILIADOS**. O orçamento inclui **R$ 10.344.374,88 de ENXOVAL** (25,1% do total) — mobiliário, decoração, equipamentos dos apartamentos.  
> **Para calibração paramétrica, o enxoval foi EXCLUÍDO** do total.  
>   
> - **Total COM Enxoval:** R$ 41.168.405,73 → R$ 4.753,80/m² → **CUB ratio 1,60**  
> - **Total SEM Enxoval:** R$ 30.824.030,85 → R$ 3.559,33/m² → **CUB ratio 1,20**  
>   
> O CUB ratio de **1,20 (sem enxoval)** é **ALTO** para padrão médio, mas justificável por:  
> - Studios compactos (54 m²/un) — maior custo por m² devido à escala reduzida por unidade  
> - Centro de Florianópolis — terreno caro, fundação em terreno urbano  
> - 2 subsolos com contenção (cortina de concreto armado)  
> - 22 pavimentos — estrutura verticalizada  
> - Climatização, exaustão e pressurização separados (SPDA completo)  
> - Equipamentos especiais (elevadores, plataforma, interfonia, CFTV)

> **⚠️ NOTA CRÍTICA — EMPREITADA GLOBAL:**  
> Diferente da maioria dos projetos, o Parkside tem **Empreitada Global de R$ 10.831.779 (26,3% do total)** com **breakdown detalhado por disciplina** (civil 60%, pintura 10%, cerâmicos 10%, hidro 6%, elétrica 6%, portas 3%, contenção 2%, limpeza 2%, louças 1%).  
>   
> **Para calibração, a empreitada foi DISTRIBUÍDA** nos macrogrupos correspondentes:  
> - Civil (R$ 6.499.068) → Supraestrutura  
> - Pintura (R$ 1.083.178) → Pintura  
> - Cerâmicos (R$ 1.083.178) → Rev. Internos + Acabamentos  
> - Hidro (R$ 649.907) → Instalações  
> - Elétricas (R$ 649.907) → Instalações  
> - Portas/Rodapés (R$ 324.953) → Esquadrias  
> - Contenção (R$ 216.636) → Infraestrutura/Contenção  
> - Limpeza (R$ 216.636) → Gerenciamento  
> - Louças (R$ 108.318) → Louças e Metais

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| Gerenciamento Técnico e ADM + Limpeza (empr.) | 1-Gerenciamento | R$ 2.197.602 + R$ 216.636 = R$ 2.414.238 |
| Movimentação de Terra | 2-Mov.Terra | R$ 378.280 |
| Infraestrutura + Contenção (empr.) | 3-Infraestrutura | R$ 909.261 + R$ 278.469 + R$ 216.636 = R$ 1.404.366 |
| Supraestrutura + Civil (empr.) | 4-Supraestrutura | R$ 3.324.999 + R$ 6.499.068 = R$ 9.824.067 |
| Alvenaria | 5-Alvenaria | R$ 743.691 |
| Impermeabilização | 6-Impermeabilização | R$ 411.651 |
| Instalações (Elétr, Hidro, GLP, Prev) + Hidro/Elétr (empr.) | 7-Instalações | R$ 2.728.300 + R$ 649.907 + R$ 649.907 = R$ 4.028.114 |
| Equipamentos e Sist. Especiais | 8-Sist.Especiais | R$ 903.000 |
| Climatização, Exaustão, Pressurização | 9-Climatização | R$ 476.100 |
| Rev. Internos Piso + Parede + Cerâmicos (empr. 50%) | 10-Rev.Int.Parede | R$ 617.053 + R$ 148.023 + R$ 541.589 = R$ 1.306.665 |
| Acabamentos Internos Teto | 11-Teto | R$ 1.074.213 |
| Acabamentos Internos Piso + Cerâmicos (empr. 50%) | 12-Pisos | R$ 1.467.904 + R$ 541.589 = R$ 2.009.493 |
| Pintura Interna + Pintura (empr.) | 13-Pintura | R$ 114.896 + R$ 1.083.178 = R$ 1.198.074 |
| Esquadrias + Portas/Rodapés (empr.) | 14-Esquadrias | R$ 2.816.850 + R$ 324.953 = R$ 3.141.803 |
| Louças e Metais + Louças (empr.) | 15-Louças | R$ 553.893 + R$ 108.318 = R$ 662.211 |
| Rev. Argamassados Fachada + Pintura Fachada | 16-Fachada | R$ 109.937 + R$ 49.085 = R$ 159.022 |
| Cobertura + Serviços Complementares | 17-Complementares | R$ 31.661 + R$ 365.403 = R$ 397.064 |
| Imprevistos e Contingências | 18-Imprevistos | R$ 291.980 |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Ref. Urban Life | Ref. Barbados |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 9,78 | N/D | N/D |
| Área por Unidade | AC / UR | 53,13 | 146,7 | 192,0 |
| Unidades por Terreno | UR / AT | 184,2 un/1000m² | N/D | N/D |
| Área Privativa / AC | AP / AC | 61,2% | N/D | N/D |

> **Observação:** Coeficiente de aproveitamento **9,78** é **MUITO ALTO**, indicando verticalização intensa (22 pavimentos em terreno de 885 m²). Área por unidade (53,13 m²/un) é **muito compacta** (studios), significativamente menor que Urban Life (146,7 m²) e Barbados (192 m²). Isso explica o CUB ratio elevado — unidades menores têm maior custo relativo por m².

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Ref. Barbados |
|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | N/D |
| UR por Elevador | UR / ELEV | N/D (estim. 3-4 elev.) | N/D |

> **Observação:** Para 22 pavimentos e 163 unidades, estimativa de 3-4 elevadores (R$ 903k em Equipamentos Especiais inclui elevadores + plataforma).

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial (studios) | 160 | 98,2% | 53,13 |
| Comercial | 3 | 1,8% | N/D |

> **Observação:** Pavimentos incluem Sub2 (700,82 m²) + Sub1 (613,50 m²) + Térreo (560,05 m²) + Pav2 (403,28 m²) + Garden (488,63 m²) + 15 Tipos (5.481,15 m²) + Cobertura (322,67 m²) + Barrilete (45 m²) + Reservatório (45 m²) = 8.660,10 m² total.

### 2.4 Custo por Unidade

| Índice | Fórmula | Valor | Valor Normalizado |
|---|---|---|---|
| R$ / UR (sem ger., sem imprev., SEM enxoval) | Total / UR | R$ 189.074 | R$ 174.778 |
| R$ / UR (com ger., SEM enxoval) | Total / UR | R$ 203.872 | R$ 188.448 |
| CUB / UR (sem ger., SEM enxoval) | (R$/UR) / CUB | 63,5 CUB | 63,5 CUB |
| R$ / UR (COM enxoval) | Total / UR | R$ 252.515 | R$ 233.399 |

> **Observação:** Custo por unidade (R$ 189k sem ger./enxoval, R$ 253k com enxoval) é **significativamente menor** que Urban Life (R$ 337k) e Barbados (R$ 491k), refletindo unidades **muito compactas** (53 m² vs 147-192 m²). O CUB/UR de **63,5** é baixo em valor absoluto, mas o **CUB ratio de 1,20/m²** é alto — característica de studios onde o custo fixo (banheiro, cozinha, porta) se dilui em área menor.

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

### 3.1 Breakdown Original (Set/2025, CUB ago/2025 R$ 2.978,02, SEM Enxoval)

| # | Macrogrupo | Valor (R$) | R$/m² | % s/ ger. | Observação |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 2.414.238 | 278,78 | — | Inclui Limpeza (empr.) |
| 2 | Movimentação de Terra | 378.280 | 43,68 | 1,23% | — |
| 3 | **Infraestrutura + Contenção** | **1.404.366** | **162,17** | **4,56%** | **Inclui contenção cortina (empr.)** |
| 4 | **Supraestrutura (mat + MO)** | **9.824.067** | **1.134,41** | **31,87%** | **Inclui Civil (empr. R$ 6,5M)** |
| 5 | Alvenaria | 743.691 | 85,88 | 2,41% | — |
| 6 | Impermeabilização | 411.651 | 47,53 | 1,34% | — |
| 7 | **Instalações (agrupado)** | **4.028.114** | **465,13** | **13,07%** | **Inclui Hidro+Elétr (empr.)** |
| 8 | Sistemas Especiais | 903.000 | 104,27 | 2,93% | Elevadores, plataforma |
| 9 | **Climatização** | **476.100** | **54,98** | **1,54%** | **Separado** (raro) |
| 10 | **Rev. Internos Parede** | **1.306.665** | **150,88** | **4,24%** | **Inclui 50% Cerâmicos (empr.)** |
| 11 | Teto | 1.074.213 | 124,04 | 3,49% | — |
| 12 | **Pisos** | **2.009.493** | **232,02** | **6,52%** | **Inclui 50% Cerâmicos (empr.)** |
| 13 | **Pintura** | **1.198.074** | **138,33** | **3,89%** | **Inclui Pintura (empr.)** |
| 14 | **Esquadrias** | **3.141.803** | **362,80** | **10,20%** | **Inclui Portas/Rodapés (empr.)** |
| 15 | **Louças e Metais** | **662.211** | **76,47** | **2,15%** | **Inclui Louças (empr.)** — **Separado** (raro) |
| 16 | Fachada | 159.022 | 18,36 | 0,52% | Rev. Argamassa + Pintura |
| 17 | Complementares | 397.064 | 45,85 | 1,29% | Cobertura + Serv.Compl. |
| 18 | Imprevistos | 291.980 | 33,72 | — | Separado |
| — | **TOTAL (sem ger., sem imprev., SEM enxoval)** | **30.824.031** | **3.559,33** | **100%** | — |
| — | **TOTAL (com ger., sem imprev., SEM enxoval)** | **30.698.649** | **3.544,10** | — | — |
| — | **TOTAL (com ger., com imprev., SEM enxoval)** | **30.990.629** | **3.577,82** | — | — |

### 3.2 Valores Normalizados (Base CUB Dez/2023 = R$ 2.752,67)

> **Fator de normalização:** 2.752,67 / 2.978,02 = **0,9244**

| # | Macrogrupo | Valor Norm. (R$) | R$/m² Norm. | % s/ ger. | Faixa Obras Similares | Status |
|---|---|---|---|---|---|---|
| 1 | Gerenciamento | 2.231.715 | 257,71 | — | 260-550 | ⚠️ Abaixo (borda) |
| 2 | Movimentação de Terra | 349.672 | 40,38 | 1,23% | 7-85 | ✅ Dentro |
| 3 | **Infraestrutura + Contenção** | **1.298.236** | **149,91** | **4,56%** | 115-344 | ✅ Dentro |
| 4 | **Supraestrutura (mat + MO)** | **9.081.394** | **1.048,66** | **31,87%** | 485-1.236 | ✅ Dentro (médio-alto) |
| 5 | Alvenaria | 687.470 | 79,40 | 2,41% | 123-324 | ⚠️ Abaixo |
| 6 | Impermeabilização | 380.526 | 43,94 | 1,34% | 43-94 | ✅ Dentro |
| 7 | **Instalações** | **3.723.598** | **429,99** | **13,07%** | 240-623 | ✅ Dentro |
| 8 | Sistemas Especiais | 834.833 | 96,42 | 2,93% | 89-748 | ✅ Dentro |
| 9 | **Climatização** | **440.105** | **50,82** | **1,54%** | 26-210 | ✅ Dentro |
| 10 | **Rev. Internos Parede** | **1.208.042** | **139,49** | **4,24%** | 107-425 | ✅ Dentro |
| 11 | Teto | 993.067 | 114,67 | 3,49% | 27-151 | ✅ Dentro |
| 12 | **Pisos** | **1.857.579** | **214,48** | **6,52%** | 59-534 | ✅ Dentro |
| 13 | **Pintura** | **1.107.469** | **127,88** | **3,89%** | 84-194 | ✅ Dentro |
| 14 | **Esquadrias** | **2.904.651** | **335,38** | **10,20%** | 244-950 | ✅ Dentro |
| 15 | **Louças e Metais** | **612.181** | **70,69** | **2,15%** | 23-51 | **⚠️ ACIMA** |
| 16 | Fachada | 146.998 | 16,98 | 0,52% | 57-546 | ⚠️ Abaixo |
| 17 | Complementares | 367.029 | 42,38 | 1,29% | 49-995 | ✅ Dentro |
| 18 | Imprevistos | 269.938 | 31,17 | — | 48-174 | ⚠️ Abaixo |
| — | **TOTAL Norm. (sem ger., sem imprev., SEM enxoval)** | **28.493.585** | **3.290,27** | **100%** | — | — |
| — | **TOTAL Norm. (com ger., SEM enxoval)** | **30.725.300** | **3.548,98** | — | — | — |

> **⚠️ OBSERVAÇÕES CRÍTICAS:**
> 
> 1. **Supraestrutura R$ 1.049/m²** (31,87%) — **MUITO ALTA**, refletindo:
>    - MO Civil (empreitada) integrada (R$ 6.499.068, 60% da empreitada global)
>    - 22 pavimentos verticalizados (estrutura robusta)
>    - Concreto de qualidade (fck N/D, mas padrão alto pelo custo)
>    - Comparativo: Urban Life R$ 655/m² (MO embutida), Barbados R$ 1.118/m² (mat + empr. separada)
>    - **Parkside R$ 1.049/m² está entre os dois, mas mais próximo do Barbados em complexidade**
> 
> 2. **Instalações R$ 430/m²** (13,07%) — **ALTA**, refletindo:
>    - MO Hidro + Elétr (empreitada) integradas (R$ 649.907 + R$ 649.907 = R$ 1.299.814)
>    - Material R$ 2.728.300 + MO R$ 1.299.814 = R$ 4.028.114 total
>    - Comparativo: Urban Life R$ 324/m² (dentro faixa), Barbados R$ 159/m² (subdimensionado)
>    - **Parkside tem instalações robustas, acima da faixa similar mas justificável por 163 UR + 22 pav.**
> 
> 3. **Louças e Metais R$ 70,69/m²** (2,15%) — **ACIMA da faixa** (23-51):
>    - Material R$ 553.893 + MO (empreitada) R$ 108.318 = R$ 662.211 total
>    - R$ 662.211 / 163 UR = **R$ 4.063/UR** — razoável para studios mobiliados
>    - **Justificável:** 163 unidades = 163 kits completos (cuba, vaso, torneiras, registros, etc.)
>    - Comparativo: Urban Life não tem separado (incluído em Instal./Compl.)
> 
> 4. **Fachada R$ 16,98/m²** (0,52%) — **MUITO ABAIXO** da faixa (57-546):
>    - Rev. Argamassa R$ 109.937 + Pintura R$ 49.085 = R$ 159.022 total
>    - **Possível causa:** Executivo pode ter detalhamento incompleto de fachada (ACM, revestimento cerâmico, vidros podem estar em Esquadrias ou Acabamentos)
>    - **Ação:** Verificar se revestimento de fachada (além de argamassa/pintura) está em outro macrogrupo

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura (Mat + MO integrados — Breakdown por Pavimento)

| Pavimento | Área (m²) | Valor Estimado (R$) | % Supra | Observação |
|---|---|---|---|---|
| Sub2 | 700,82 | 794.829 | 8,1% | Garagem |
| Sub1 | 613,50 | 695.826 | 7,1% | Garagem |
| Térreo | 560,05 | 635.273 | 6,5% | Comercial |
| Pav2 | 403,28 | 457.405 | 4,7% | — |
| Garden | 488,63 | 554.286 | 5,6% | — |
| 15 Tipos | 5.481,15 | 6.216.791 | 63,3% | ~R$ 414.453/pav |
| Cobertura | 322,67 | 366.049 | 3,7% | — |
| Barrilete | 45,00 | 51.042 | 0,5% | — |
| Reservatório | 45,00 | 51.042 | 0,5% | — |
| **TOTAL** | **8.660,10** | **9.824.067** | **100%** | **Mat + MO (Civil empr.)** |

> **Nota:** Valores estimados proporcionalmente à área (R$ 1.134,41/m² médio). O executivo original não detalha supraestrutura por pavimento, apenas o total de materiais (R$ 3.324.999) + empreitada civil (R$ 6.499.068).

### 4.2 Componentes da Supraestrutura (baseado no total)

| Item | Valor (R$) | Valor Norm. (R$) | % Supra | Observação |
|---|---|---|---|---|
| Materiais (concreto, armadura, forma) | 3.324.999 | 3.074.201 | 33,8% | Do executivo original |
| MO Civil (empreitada) | 6.499.068 | 6.007.193 | 66,2% | Empreitada global (60%) |
| **TOTAL** | **9.824.067** | **9.081.394** | **100%** | — |

> **Observação:** MO representa **66,2% do custo de supraestrutura** — proporção muito alta, indicando:
> - Complexidade construtiva (22 pavimentos, verticalização intensa)
> - Mão de obra cara em Florianópolis
> - Estrutura robusta com alto consumo de horas/m²
> 
> Comparativo: Tipicamente MO estrutura é 40-50% do total. Parkside está significativamente acima, possivelmente por contenção complexa + altura da edificação.

### 4.3 Infraestrutura

| Item | Valor | Valor Norm. | Observação |
|---|---|---|---|
| Movimentação de Terra | 378.280 | 349.672 | Terraplanagem, escavação, bota-fora |
| Serviços Preliminares (demolição) | 37.755 | 34.900 | — |
| Fundações Sapatas (mat) | 885.092 | 818.189 | Forma, armadura, concreto 30MPa |
| Contenção Cortina (mat) | 278.469 | 257.430 | Forma, armadura, concreto |
| Contenção MO (empreitada) | 216.636 | 200.255 | Empreitada global (2%) |
| Drenagem | 24.169 | 22.342 | — |
| **TOTAL Infraestrutura** | **1.404.366** | **1.298.236** | — |
| R$/m² Infraestrutura | 162,17 | 149,91 | ✅ Dentro faixa (115-344) |
| % do Total | 4,56% | 4,56% | ✅ Típico (4-7%) |

> **Comparativo:** Urban Life R$ 61,21/m² | Barbados R$ 103,67/m².  
> Parkside R$ 149,91/m² é **significativamente mais caro**, refletindo:
> - 2 subsolos escavados em terreno urbano
> - Contenção em cortina de concreto armado (R$ 278.469 mat + R$ 216.636 MO = R$ 495.105 total)
> - Fundações rasas/sapatas robustas (R$ 885.092)
> 
> **Breakdown Fundações Sapatas:**
> - Forma: R$ 56.189
> - Armadura: R$ 342.382 (maior componente)
> - Piso concreto armado: R$ 132.455
> - Concreto 30MPa: R$ 354.065
> 
> **Breakdown Contenção:**
> - Forma cortina: R$ 60.509
> - Armadura: R$ 80.068
> - Concreto: R$ 137.893
> - MO empreitada: R$ 216.636
> - **Total Contenção:** R$ 495.105 (R$ 57,17/m² AC)

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> **Dados de levantamento detalhado não disponíveis no executivo resumido.**

### 5.1 Estimativas Baseadas em Valores Globais

| Item | Estimativa | Observação |
|---|---|---|
| Alvenaria / AC | ~0,80-1,00 m²/m² | Baseado em R$ 85,88/m² AC (abaixo faixa típica — studios compactos) |
| Pintura / AC | ~2,50-3,00 m²/m² | Baseado em R$ 138,33/m² AC (alta — inclui empreitada) |
| Impermeabilização | ~550-650 m² | Áreas molhadas, lajes garagem, reservatórios |
| Esquadrias / AC | ~0,12-0,15 m²/m² | Baseado em R$ 362,80/m² AC |
| Climatização | N/D | Sistema separado (exaustão, pressurização, SPDA) |

> **Observação Alvenaria:** R$ 85,88/m² está **abaixo** da faixa típica (100-120 R$/m²), possivelmente porque studios têm menos divisórias internas (ambientes integrados). A relação alvenaria/AC deve ser menor (~0,8-1,0 vs 1,2-1,5 típico).

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

> **Executivo agrupa todas as disciplinas + empreitada.** Total disponível com distribuição estimada:

| Disciplina | Valor Estimado (R$) | Valor Norm. (R$) | R$/m² | R$/m² Norm. | % Instal. | Obs |
|---|---|---|---|---|---|---|
| Hidrossanitárias (mat + MO) | 1.611.246 | 1.489.582 | 186,08 | 172,02 | 40% | Estimativa (material + empr. hidro) |
| Elétricas (mat + MO) | 1.611.246 | 1.489.582 | 186,08 | 172,02 | 40% | Estimativa (material + empr. elétrica) |
| Preventivas (incêndio, SPDA) | 403.811 | 373.396 | 46,62 | 43,13 | 10% | Estimativa |
| Gás (GLP) | 201.906 | 186.698 | 23,31 | 21,56 | 5% | Estimativa |
| Outras (lógica, telefonia, etc.) | 201.906 | 186.698 | 23,31 | 21,56 | 5% | Estimativa |
| **TOTAL** | **4.028.114** | **3.723.598** | **465,13** | **429,99** | **100%** | — |

| Item | Valor | Observação |
|---|---|---|
| Instalações / AC | 465,13 R$/m² | **⚠️ ACIMA** da faixa similar (250-300), dentro faixa geral (240-623) |
| Instalações Norm. / AC | 429,99 R$/m² | Dentro da faixa geral (240-623) |
| % do Total (s/ ger.) | 13,07% | **ACIMA** do típico (8-11%) |

> **⚠️ CONTRASTE COM BARBADOS E URBAN LIFE:**  
> Instalações representam **13,07% do total** e **R$ 465/m²**, **acima da faixa benchmark similar** (250-300 R$/m²) mas **dentro da faixa geral** (240-623 R$/m²).  
> 
> **Comparativo:**
> - **Parkside:** 13,07%, R$ 465/m² — **ACIMA**
> - **Urban Life:** 12,49%, R$ 287/m² — dentro faixa
> - **Barbados:** 5,73%, R$ 159/m² — subdimensionado
> 
> **Justificativas para Parkside estar acima:**
> 1. **163 unidades** — cada uma precisa de pontos elétricos, hidráulicos, gás
> 2. **22 pavimentos** — prumadas longas, maior consumo de tubulação/fiação
> 3. **Studios mobiliados** — podem ter mais pontos elétricos para eletrodomésticos integrados
> 4. **Climatização separada** (R$ 476.100) — não está incluída em Instalações, senão seria ainda maior
> 5. **MO empreitada** — R$ 649.907 (hidro) + R$ 649.907 (elétrica) = R$ 1.299.814 (32% das instalações)
> 
> **Conclusão:** Instalações do Parkside estão **adequadamente orçadas** para a complexidade do projeto. O alto valor é justificável e **não é subdimensionamento** como o Barbados.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

> **Dados detalhados não disponíveis no executivo resumido.** Índices globais:

### 7.1 Revestimentos de Parede

| Item | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|
| Rev. Internos Parede (+ cerâm. empr. 50%) | 150,88 | 139,49 | Dentro faixa (107-425), dentro similar (140-190) |
| Rev. Argam. Parede (base) | 17,09 | 15,80 | Material base argamassa |
| Fachada (argam. + pint.) | 18,36 | 16,98 | **⚠️ MUITO ABAIXO** faixa (57-546) |

> **Observação Fachada:** R$ 18,36/m² é **extremamente baixo**. Comparativo: Urban Life R$ 120/m², Barbados R$ 108/m². Possível que revestimentos de fachada (ACM, cerâmica, pastilha) estejam classificados em Esquadrias ou Acabamentos. **Requer verificação do executivo original.**

### 7.2 Pisos

| Item | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|
| Pisos (acab. + cerâm. empr. 50%) | 232,02 | 214,48 | **ACIMA** faixa similar (160-180), dentro faixa geral (59-534) |
| Rev. Argam. Piso (base) | 71,25 | 65,86 | Material base argamassa |

> **Observação Pisos:** R$ 232/m² está **acima da faixa similar** (160-180) mas dentro da faixa geral ampla. Justificável por:
> - Studios mobiliados — piso de qualidade (porcelanato, laminado)
> - MO cerâmicos (empreitada) integrada — 50% de R$ 1.083.178 = R$ 541.589 (R$ 62,54/m²)
> - Comparativo: Urban Life R$ 188/m², Barbados R$ 115/m²

### 7.3 Teto

| Item | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|
| Teto (forros) | 124,04 | 114,67 | **ACIMA** faixa similar (65-75), dentro faixa geral (27-151) |

> **Observação Teto:** R$ 124/m² está **significativamente acima da faixa similar** (65-75). Comparativo: Urban Life R$ 81/m², Barbados R$ 47/m². Possível causa:
> - Forros especiais (gesso rebaixado, sancas, iluminação embutida)
> - Studios mobiliados podem ter forro mais elaborado
> - **Aba "Obra" mostra Forros: R$ 1.074.213** — confirma valor alto

### 7.4 Pintura

| Item | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|
| Pintura (interna + fachada + empr.) | 138,33 | 127,88 | **ACIMA** faixa similar (100-120), dentro faixa geral (84-194) |
| Pintura Interna (material) | 13,27 | 12,27 | Material base |
| Pintura Fachada (material) | 5,67 | 5,24 | Material base |
| MO Pintura (empreitada) | 125,12 | 115,67 | Empreitada global (10%) |

> **Observação Pintura:** R$ 138/m² está **acima da faixa similar**, mas quase todo o custo vem da **empreitada** (R$ 125/m²). Material é apenas R$ 19/m² (13,27 + 5,67). Isso indica que a **MO de pintura é cara** em Florianópolis ou o projeto tem área de pintura significativa (mais que 3× a AC).

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

> **Dados detalhados não disponíveis no executivo resumido.** Índices globais:

| Item | Valor | Valor Norm. | Observação |
|---|---|---|---|
| Esquadrias, Vidros, Ferragens (material) | 2.816.850 | 2.603.824 | Do executivo |
| MO Instalação Portas/Rodapés (empr.) | 324.953 | 300.327 | Empreitada global (3%) |
| **Total Esquadrias** | **3.141.803** | **2.904.651** | — |
| R$/m² Esquadrias | 362,80 | 335,38 | ✅ Dentro faixa geral (244-950), similar (280-330) no topo |
| % do Total (s/ ger.) | 10,20% | 10,20% | Dentro do típico (7-11%) |
| R$/UR | R$ 19.278 | R$ 17.817 | Alto para studios |

> **Observação:** R$ 362,80/m² está no **topo da faixa similar** (280-330), mas dentro da faixa geral ampla. Comparativo:
> - **Parkside:** R$ 363/m² (10,20%)
> - **Urban Life:** R$ 389/m² (15,02%) — **ACIMA** da faixa
> - **Barbados:** R$ 257/m² (9,24%)
> 
> Parkside está **mais controlado que Urban Life**, apesar de alto em valor absoluto. Possível causa:
> - Studios compactos — menos esquadrias por m² de AC
> - Janelas de qualidade (alumínio, vidro temperado) para padrão médio/alto
> - Portas de entrada + internas + guarda-corpos (163 unidades)
> 
> **Aba "Obra" mostra Serralheria: R$ 817.722** — pode incluir parte das esquadrias metálicas, guarda-corpos, portões.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

> **Dados parcialmente disponíveis no executivo.**

| Item | Valor | Valor Norm. | Observação |
|---|---|---|---|
| Equipamentos e Sist. Especiais | 903.000 | 834.833 | Do executivo |
| Elevador + Plataforma (aba Obra) | 903.000 | 834.833 | Mesma rubrica |
| R$/m² Sistemas Especiais | 104,27 | 96,42 | — |
| % do Total (s/ ger.) | 2,93% | 2,93% | — |

> **⚠️ ALERTA — SISTEMAS ESPECIAIS ABAIXO DA FAIXA:**  
> R$ 104,27/m² está **significativamente abaixo da faixa similar** (200-250 R$/m²), embora dentro da faixa geral ampla (89-748).  
> 
> **Comparativo:**
> - **Parkside:** R$ 104/m² (2,93%)
> - **Urban Life:** R$ 160/m² (6,22%) — dentro faixa geral, abaixo similar
> - **Barbados:** R$ 156/m² (5,60%)
> 
> **Para 163 UR em 22 pavimentos**, esperaríamos:
> - **3-4 elevadores** — R$ 250k-350k/un = R$ 750k-1.400k
> - **Plataforma PNE** — R$ 80k-120k
> - **Interfonia/CFTV** — R$ 100k-150k
> - **Portaria eletrônica** — R$ 50k-80k
> - **Automação predial** — R$ 100k-200k
> - **Total estimado:** R$ 1.130k-1.950k (R$ 130-225/m²)
> 
> O valor de **R$ 903k** está no **limite inferior** do esperado. Possíveis causas:
> 1. Elevadores econômicos (não premium)
> 2. Automação/interfonia em escopo básico
> 3. CFTV pode estar em outra rubrica (Instalações ou Complementares)
> 4. Possível complementação futura ou contratação separada
> 
> **Ação:** Verificar se interfonia, CFTV, automação estão classificados em Instalações ou Complementares.

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Gerenciamento Técnico e ADM

| Item | Valor (R$) | Valor Norm. (R$) | R$/m² | R$/m² Norm. |
|---|---|---|---|---|
| Gerenciamento Técnico/Admin (exec.) | 2.197.602 | 2.031.380 | 253,76 | 234,54 |
| MO Limpeza (empreitada) | 216.636 | 200.255 | 25,02 | 23,12 |
| **TOTAL Gerenciamento** | **2.414.238** | **2.231.715** | **278,78** | **257,71** |
| **% do Total** | **7,83%** | **7,83%** | — | — |

> **Observação:** Gerenciamento representa **7,83% do total** (sem enxoval), dentro da faixa típica (7-12%), mas **abaixo** do Urban Life (11,03%) e Barbados (8,16%). Justificável pelo prazo menor (33 vs 44 meses) e equipe otimizada.

### 10.2 Composição do Gerenciamento (estimativa)

| Tipo | Valor Estimado (R$) | Valor Norm. (R$) | % do CI | Observação |
|---|---|---|---|---|
| Gerenciamento Técnico | 482.848 | 446.343 | 20% | Estudos + Projetos + Consultorias + Ensaios |
| Consumos/Taxas/Docs | 241.424 | 223.172 | 10% | Licenciamentos + Documentos |
| Gerenciamento ADM | 1.689.966 | 1.562.200 | 70% | Segurança + ADM/Canteiro + Equipamentos |
| **TOTAL CI** | **2.414.238** | **2.231.715** | **100%** | — |

> **Observação:** Proporções estimadas baseadas em benchmarks (Urban Life: técnico 18%, consumos 6%, ADM 76%). Parkside provavelmente tem proporção maior de técnico (20%) e consumos (10%) devido à complexidade (22 pavimentos, contenção, centro urbano).

### 10.3 Equipe de Gestão (estimativa)

| Cargo | Prazo | Custo Mensal Estimado | Total (R$) | Total Norm. (R$) |
|---|---|---|---|---|
| Mestre de Obra | 33 meses | R$ 15.000 | 495.000 | 457.572 |
| Encarregado | 33 meses | R$ 8.000 | 264.000 | 244.038 |
| Guincheiro | 30 meses | R$ 6.000 | 180.000 | 166.392 |
| **TOTAL Equipe (estim.)** | — | — | **939.000** | **868.002** |

> **Observação:** Equipe estimada (R$ 939k) representa ~39% do CI total, semelhante ao Urban Life (43%). O prazo de 33 meses para 8.660 m² é razoável (ritmo de 262 m²/mês).

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

> **Dados separados no executivo — RARO!**

| Item | Valor | Valor Norm. | R$/UR | Obs |
|---|---|---|---|---|
| Louças e Metais (material) | 553.893 | 512.078 | R$ 3.398 | Do executivo |
| MO Instalação Louças/Metais (empr.) | 108.318 | 100.142 | R$ 665 | Empreitada global (1%) |
| **TOTAL** | **662.211** | **612.181** | **R$ 4.063** | — |
| R$/m² | 76,47 | 70,69 | — | **⚠️ ACIMA faixa (23-51)** |

> **⚠️ OBSERVAÇÃO CRÍTICA — LOUÇAS E METAIS ACIMA DA FAIXA:**  
> R$ 76,47/m² (normalizado R$ 70,69/m²) está **significativamente acima** da faixa benchmark (23-51 R$/m²).  
> 
> **Justificativas:**
> 1. **163 unidades** — cada uma precisa de kit completo:
>    - Cuba pia (cozinha): ~R$ 300-500
>    - Vaso sanitário: ~R$ 400-700
>    - Torneira pia: ~R$ 200-400
>    - Torneira chuveiro: ~R$ 300-600
>    - Registros (2-3 un): ~R$ 200-400
>    - Metais diversos (sifão, válvulas, flexíveis): ~R$ 300-500
>    - **Total/UR:** R$ 1.700-3.100 (médio R$ 2.400)
> 
> 2. **R$ 4.063/UR** está **acima** do estimado (R$ 2.400-3.000 típico), mas justificável por:
>    - Studios mobiliados — podem ter metais de qualidade superior
>    - Louças de marca (Deca, Docol, Tramontina)
>    - Complementos (papeleira, saboneteira, cabides) incluídos
> 
> 3. **Comparativo:** Maioria dos projetos **NÃO separa** louças/metais (incluem em Instalações ou Complementares). Parkside ter separado é **positivo para calibração**.
> 
> 4. **Análise R$/m²:** Para benchmarks, a faixa 23-51 pode estar **subdimensionada** ou incluir apenas **material** (sem MO). Parkside tem material + MO separados:
>    - Material: R$ 63,96/m² (normalizado R$ 59,14/m²) — **ainda acima** da faixa
>    - MO: R$ 12,51/m² (normalizado R$ 11,56/m²)
> 
> **Conclusão:** Louças e Metais do Parkside estão **adequadamente orçadas** para 163 unidades com padrão médio/alto. O alto R$/m² reflete a **densidade de unidades** (163 UR em 8.660 m² = 1 UR cada 53 m²), não superfaturamento. **Para calibração, usar com ressalva** — ajustar por densidade de unidades.

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

> **Prazo disponível:** 33 meses (abr/2026 → dez/2028).

| Índice | Valor | Referência |
|---|---|---|
| Prazo | 33 meses | Do executivo |
| Ritmo de construção | 262,4 m²/mês | 8.660 ÷ 33 |
| Burn rate (sem ger., sem enxoval) | R$ 933.758/mês | R$ 30,82M ÷ 33 |
| Burn rate (com ger., sem enxoval) | R$ 938.918/mês | R$ 30,98M ÷ 33 |
| R$/m²/mês | 108,42 R$/m²/mês | R$ 3.577,82 ÷ 33 |
| UR/mês | 4,9 UR/mês | 163 ÷ 33 |

> **Comparativo:**
> - **Parkside:** 262 m²/mês, R$ 934k/mês, 4,9 UR/mês
> - **Urban Life:** 160 m²/mês, R$ 420k/mês (44 meses, 48 UR)
> - **Barbados:** ~86-108 m²/mês (estimado 16-20 meses, 9 UR)
> 
> **Observações:**
> 1. **Ritmo 1,6× maior** que Urban Life (262 vs 160 m²/mês) — eficiência de verticalização (22 pav.)
> 2. **Burn rate 2,2× maior** (R$ 934k vs R$ 420k/mês) — obra mais cara total, mas prazo menor
> 3. **R$/m²/mês** (108,42) é **1,8× maior** que Urban Life (59,66) — velocidade de queima mais intensa
> 4. **UR/mês** (4,9) é semelhante ao Urban Life (~1,1 UR/mês × 44 meses = 48 UR) considerando prazo
> 
> **Conclusão:** Parkside tem **ritmo acelerado** de construção, compatível com empreiteira experiente e cronograma apertado (33 meses para 22 pavimentos). Burn rate alto reflete custo absoluto elevado, mas prazo otimizado.

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

> **Dados detalhados não disponíveis no executivo resumido.** Índices globais:

| Item | Valor | Valor Norm. | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|---|---|
| Impermeabilização | R$ 411.651 | R$ 380.526 | 47,53 | 43,94 | ✅ Dentro faixa (43-94), dentro similar (55-65) na borda inf. |
| % do Total | 1,34% | 1,34% | — | — | ⚠️ Abaixo típico (2-3%) |
| Área estimada | ~570-690 m² | — | — | — | Baseado em R$ 600-720/m² típico |

> **Observação:** R$ 47,53/m² está **na borda inferior** da faixa similar (55-65). Comparativo:
> - **Parkside:** R$ 47,53/m² (1,34%)
> - **Urban Life:** R$ 62,28/m² (2,40%)
> - **Barbados:** R$ 64,42/m² (2,58%)
> 
> Parkside está **abaixo** dos benchmarks. Possíveis causas:
> 1. Área de impermeabilização menor (22 pavimentos, menos área de laje exposta vs Barbados 3 pav.)
> 2. Método mais econômico (manta asfáltica vs cristalização + manta)
> 3. **Studios compactos** — menos área de banheiros/áreas molhadas por m² de AC
> 
> **Estimativa de área:**
> - 163 unidades × 1 banheiro = ~163 banheiros × 3 m²/banheiro = ~490 m² (banheiros)
> - Garagem Sub2 + Sub1 = ~1.314 m² (lajes)
> - Reservatório = ~45 m² (fundo + paredes)
> - Jardineiras/floreiras = ~50 m² (estimado)
> - **Total estimado:** ~600-700 m² (vs 570-690 pela conta inversa)
> 
> **Conclusão:** Impermeabilização está **no limite inferior da faixa**, mas não é alarmante. Pode refletir método econômico ou área realmente menor devido à verticalização (menos lajes expostas).

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

> **Cobertura e Serviços Complementares separados no executivo.** Breakdown:

| Item | Valor (R$) | Valor Norm. (R$) | R$/m² | R$/m² Norm. | Obs |
|---|---|---|---|---|---|
| Cobertura | 31.661 | 29.266 | 3,66 | 3,38 | **⚠️ MUITO ABAIXO** faixa (10-30) |
| Serviços Complementares | 365.403 | 337.763 | 42,19 | 39,00 | Dentro faixa (49-995) na borda inf. |
| Paisagismo (aba Obra) | 129.902 | 120.079 | 15,00 | 13,87 | Incluído em Serv.Compl. |
| Imprevistos | 291.980 | 269.938 | 33,72 | 31,17 | **⚠️ ABAIXO** faixa (48-174) |
| **Total Complementares (s/ imprev.)** | **397.064** | **367.029** | **45,85** | **42,38** | — |
| **% do Total (s/ ger.)** | **1,29%** | **1,29%** | — | — | ⚠️ Abaixo típico (3-5%) |

> **Observação Cobertura:** R$ 3,66/m² é **extremamente baixo** (similar R$ 10-30). Comparativo:
> - **Parkside:** R$ 3,66/m² (0,10%)
> - **Urban Life:** R$ 11,06/m² (0,37%)
> - **Barbados:** R$ 17,83/m² (0,70%)
> 
> Justificável por prédio alto (22 pav.) onde cobertura é fração mínima da AC:
> - Cobertura: 322,67 m² (3,7% da AC total)
> - R$ 31.661 / 322,67 m² = **R$ 98,11/m² de cobertura** — razoável para telhado/laje impermeabilizada
> - Mas R$ 31.661 / 8.660 m² AC = R$ 3,66/m² AC — muito baixo por diluição em AC grande
> 
> **Observação Imprevistos:** R$ 33,72/m² está **abaixo** da faixa (48-174). Pode indicar:
> 1. Orçamento apertado com pouca margem para contingências
> 2. Executivo muito detalhado (menor risco/imprevistos)
> 3. **Risco:** Projeto pode estourar o orçamento se houver imprevistos reais

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

### 15.1 Comparação com Urban Life e Barbados

> **Fonte:** Executivo Parkside + Executivos Urban Life e Barbados

| Etapa | Parkside R$/m² | Urban Life R$/m² | Barbados R$/m² | Faixa Similar | Status PKS |
|---|---|---|---|---|---|
| Mov. Terra | 43,68 | 21,01 | 17,84 | 10-20 | **⚠️ ACIMA** |
| Infraestrutura | 162,17 | 61,21 | 103,67 | 115-344 | ✅ Dentro |
| Supraestrutura | 1.134,41 | 655,33 | 404,78¹ | 485-1.236 | ✅ Dentro (alto) |
| Alvenaria | 85,88 | 113,48 | 57,21 | 123-324 | ⚠️ Abaixo |
| Instalações | 465,13 | 323,61 | 159,26 | 240-623 | ✅ Dentro (alto) |
| Sist. Especiais | 104,27 | 160,97 | 156,10 | 89-748 | ✅ Dentro |
| Climatização | 54,98 | — | — | 26-210 | ✅ Dentro |
| Impermeabilização | 47,53 | 62,28 | 64,42 | 43-94 | ✅ Dentro (borda inf.) |
| Rev. Int. Parede | 150,88 | 190,56 | 114,58 | 107-425 | ✅ Dentro |
| Teto | 124,04 | 80,96 | 46,59 | 27-151 | ✅ Dentro |
| Pisos | 232,02 | 188,39 | 114,60 | 59-534 | ✅ Dentro |
| Pintura | 138,33 | 114,90 | 128,02 | 84-194 | ✅ Dentro |
| Esquadrias | 362,80 | 388,93 | 256,91 | 244-950 | ✅ Dentro |
| Louças e Metais | 76,47 | — | — | 23-51 | **⚠️ ACIMA** |
| Cobertura | 3,66 | 11,06 | 17,83 | 10-30 | ⚠️ Abaixo |
| Fachada | 18,36 | 120,25 | 87,63 | 57-546 | **⚠️ MUITO ABAIXO** |
| Complementares | 45,85 | 108,16 | 111,54 | 49-995 | ✅ Borda inf. |
| **TOTAL (sem ger.)** | **3.559,33** | **2.590,15** | **2.554,28** | **2.010-2.500** | **⚠️ ACIMA** |

> ¹ Barbados R$ 404,78/m² é **SÓ MATERIAIS** de supraestrutura. Somando empreitada global → R$ 1.118/m².  
> Parkside R$ 1.134/m² **JÁ INCLUI MO**, portanto é comparação mais justa (similar ao Barbados total).

### 15.2 Comparação de Índices Globais

| Projeto | Local | AC (m²) | UR | R$/m² (s/ ger., s/ enxoval) | CUB ratio | Data-base |
|---|---|---|---|---|---|---|
| **Parkside** | **Florianópolis** | **8.660** | **163** | **3.559** | **1,20** | **Set/2025** |
| Urban Life | Joaçaba | 7.040 | 48 | 2.590 (norm.) | 0,94 | Fev/2021 |
| Barbados | Bombinhas | 1.728 | 9 | 2.554 | 1,07 | Out/2021 |

> **Observações:**
> - Parkside é **37% mais caro** que Urban Life (R$ 3.559 vs R$ 2.590/m² normalizado)
> - Parkside é **39% mais caro** que Barbados (R$ 3.559 vs R$ 2.554/m²)
> - **CUB ratio 1,20** é **ALTO** (sem enxoval), mas justificável por:
>   - Studios compactos (53 m²/un) — maior custo por m²
>   - Centro de Florianópolis — terreno caro, fundação urbana
>   - 2 subsolos com contenção
>   - 22 pavimentos — estrutura verticalizada complexa
>   - Climatização separada (exaustão, pressurização)
>   - Louças e Metais separados (163 kits completos)
> 
> **Principais diferenças vs Urban Life:**
> - **Supraestrutura:** R$ 1.134 vs R$ 655/m² (+73%) — 22 vs 12 pavimentos, maior complexidade
> - **Infraestrutura:** R$ 162 vs R$ 61/m² (+165%) — contenção + 2 subsolos vs terreno plano
> - **Instalações:** R$ 465 vs R$ 324/m² (+44%) — 163 vs 48 unidades, maior densidade
> - **Louças e Metais:** R$ 76 vs não separado — Parkside tem separado, Urban Life incluído em outras
> - **Fachada:** R$ 18 vs R$ 120/m² (-85%) — **possível subdimensionamento Parkside**

### 15.3 Análise de Escala

| Indicador | Parkside | Urban Life | Barbados |
|---|---|---|---|
| AC / UR | 53,13 | 146,7 | 192,0 |
| CUB ratio (s/ ger.) | 1,20 | 0,94 | 1,07 |
| R$/UR (s/ ger.) | R$ 189.074 | R$ 379.942 | R$ 491.467 |
| Pavimentos | 22 | 12 | 3 |
| Verticalização | Alta | Média | Baixa |

> **Paradoxo da Escala:**
> - **R$/m² CRESCE** com verticalização: Parkside (R$ 3.559, 22 pav.) > Barbados (R$ 2.554, 3 pav.)
> - **R$/UR DIMINUI** com compactação: Parkside (R$ 189k, 53 m²/un) < Barbados (R$ 491k, 192 m²/un)
> - **CUB ratio reflete complexidade construtiva**, não escala absoluta:
>   - Parkside 1,20 — alta complexidade (22 pav., contenção, centro urbano)
>   - Barbados 1,07 — média complexidade (3 pav., litoral, terreno irregular)
>   - Urban Life 0,94 — baixa complexidade relativa (12 pav., terreno plano, escala média)

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ✅ Dentro da Faixa (Valores Normalizados, comparado com faixa similar)

- **Movimentação de Terra 1,23%** (R$ 40,38/m² norm.) — na borda superior da faixa (10-20), possivelmente devido a 2 subsolos escavados
- **Infraestrutura 4,56%** (R$ 149,91/m² norm.) — ✅ dentro faixa (115-344), acima da média devido à contenção
- **Impermeabilização 1,34%** (R$ 43,94/m² norm.) — dentro faixa (43-94), borda inferior
- **Sistemas Especiais 2,93%** (R$ 96,42/m² norm.) — dentro faixa geral (89-748)
- **Climatização 1,54%** (R$ 50,82/m² norm.) — dentro faixa (26-210), **separado** (raro)
- **Rev. Internos Parede 4,24%** (R$ 139,49/m² norm.) — dentro faixa (107-425)
- **Teto 3,49%** (R$ 114,67/m² norm.) — dentro faixa geral (27-151), acima similar (65-75)
- **Pisos 6,52%** (R$ 214,48/m² norm.) — dentro faixa geral (59-534), acima similar (160-180)
- **Pintura 3,89%** (R$ 127,88/m² norm.) — dentro faixa geral (84-194), acima similar (100-120)
- **Esquadrias 10,20%** (R$ 335,38/m² norm.) — dentro faixa geral (244-950), topo similar (280-330)
- **Complementares 1,29%** (R$ 42,38/m² norm.) — dentro faixa (49-995), borda inferior

### ⚠️ Fora da Faixa / Particularidades

- **Supraestrutura 31,87%** (R$ 1.048,66/m² norm.) — **MUITO ALTA**, refletindo:
  - **MO Civil (empreitada) R$ 6.499.068** (66,2% do total de supra) — empreitada global distribuída
  - **22 pavimentos verticalizados** — estrutura robusta, maior consumo de horas/m²
  - **Contenção complexa** (cortina de concreto armado)
  - **Comparativo:** Urban Life R$ 655/m² (MO embutida, 12 pav.) | Barbados R$ 1.118/m² (mat + empr., 3 pav.)
  - **Análise:** Parkside R$ 1.049/m² está **no médio-alto da faixa** (485-1.236), justificável pela verticalização intensa
  - **Ação:** Valor está **dentro da faixa geral**, mas é o **maior componente** do orçamento (31,87%)

- **Instalações 13,07%** (R$ 429,99/m² norm.) — **ACIMA da faixa similar** (250-300), dentro geral (240-623):
  - Material R$ 2.728.300 + MO (empr. hidro + elétrica) R$ 1.299.814 = R$ 4.028.114 total
  - **Justificável:** 163 unidades + 22 pavimentos → prumadas longas, maior consumo de tubulação/fiação
  - **Comparativo:** Urban Life R$ 324/m² (dentro faixa) | Barbados R$ 159/m² (subdimensionado)
  - **Análise:** Parkside tem instalações **adequadamente orçadas** para a complexidade
  - **Ação:** Usar como referência de instalações robustas para calibração

- **Louças e Metais 2,15%** (R$ 70,69/m² norm.) — **ACIMA da faixa** (23-51):
  - Material R$ 553.893 + MO (empr.) R$ 108.318 = R$ 662.211 total
  - **R$ 4.063/UR** — alto para padrão médio, mas justificável para studios mobiliados
  - **Análise:** O alto R$/m² reflete a **densidade de unidades** (163 UR em 8.660 m² = 1 UR cada 53 m²)
  - **Ação:** **Usar com ressalva na calibração** — ajustar por densidade de unidades (UR/AC). Para projetos com UR/AC similar (~0,02 UR/m²), usar R$ 70/m². Para UR/AC menor (~0,01 UR/m²), usar R$ 35-40/m²

- **Alvenaria 2,41%** (R$ 79,40/m² norm.) — **ABAIXO da faixa** (123-324):
  - **Possível causa:** Studios compactos com menos divisórias internas (ambientes integrados)
  - **Comparativo:** Urban Life R$ 113/m² | Barbados R$ 57/m²
  - **Análise:** Parkside está entre os dois, mas mais próximo do Barbados (obras menores têm menos alvenaria/m²)
  - **Ação:** Verificar se há alvenaria de vedação externa (pode estar em Fachada)

- **Fachada 0,52%** (R$ 16,98/m² norm.) — **MUITO ABAIXO da faixa** (57-546):
  - Rev. Argamassa R$ 109.937 + Pintura R$ 49.085 = R$ 159.022 total
  - **Comparativo:** Urban Life R$ 120/m² | Barbados R$ 108/m²
  - **⚠️ ALERTA CRÍTICO:** R$ 16,98/m² é **9× menor** que a faixa mínima esperada
  - **Possíveis causas:**
    1. Revestimento de fachada (ACM, cerâmica, pastilha) classificado em **Esquadrias** (vidros/painéis)
    2. Revestimento de fachada classificado em **Acabamentos** (pisos/paredes)
    3. **Executivo incompleto** — fachada pode ter complementação futura
    4. Serralheria (R$ 817.722 na aba Obra) pode incluir painéis/revestimentos metálicos
  - **Ação:** **VERIFICAR EXECUTIVO ORIGINAL** — fachada subdimensionada é red flag para calibração

- **Gerenciamento 7,83%** (R$ 257,71/m² norm.) — **NA BORDA INFERIOR** da faixa (260-550):
  - Executivo R$ 2.197.602 + Limpeza (empr.) R$ 216.636 = R$ 2.414.238 total
  - **Comparativo:** Urban Life R$ 327/m² (11,03%) | Barbados R$ 289/m² (8,16%)
  - **Análise:** Parkside está **levemente abaixo** do esperado para 33 meses e 163 unidades
  - **Possível causa:** Equipe otimizada ou gerenciamento enxuto
  - **Ação:** Está dentro da faixa, mas no limite inferior — pode indicar equipe pequena ou terceirização de gestão

- **Imprevistos 0,95%** (R$ 31,17/m² norm.) — **ABAIXO da faixa** (48-174):
  - **R$ 291.980** representa apenas **0,95% do total** (sem ger., sem enxoval)
  - **Comparativo:** Tipicamente 2-5% do total
  - **⚠️ RISCO:** Orçamento pode estourar se houver imprevistos reais (alterações de projeto, condições de terreno, inflação)
  - **Ação:** Alertar que a margem de contingência é **baixa** — projeto vulnerável a variações

### 📊 Dados Disponíveis vs Insuficientes

**✅ Disponível (detalhado ou calculável):**
- Breakdown completo por macrogrupo (18 categorias + imprevistos)
- **Empreitada global com distribuição por disciplina** (civil, pintura, cerâmicos, hidro, elétrica, portas, contenção, limpeza, louças) — **RARO e VALIOSO**
- **Enxoval separado** (R$ 10.344.375) — permite calibração com/sem enxoval
- **Climatização separada** (R$ 476.100) — **RARO**
- **Louças e Metais separados** (R$ 662.211) — **RARO**
- Infraestrutura detalhada (sapatas, contenção, drenagem)
- Dados do produto (163 UR, 22 pav., 2 subsolos, 8.660 m²)
- Prazo (33 meses)

**⚠️ Insuficiente (estimativa ou ausente):**
- Detalhamento de instalações por disciplina (hidro/elétrica/preventiva/gás não separados no executivo)
- Breakdown de supraestrutura por pavimento (apenas total disponível)
- PUs de acabamentos (pisos, revestimentos, pintura por m²)
- Levantamento de áreas (alvenaria/AC, forro/AC, pintura/AC, esquadrias/AC)
- Detalhamento de esquadrias por tipo (janelas, portas, guarda-corpos)
- Composição do gerenciamento (estudos, projetos, equipe não detalhados)
- **Fachada detalhada** (revestimentos, painéis, ACM — **CRÍTICO**)

### 🔍 Insights para Calibração

1. **Empreitada Global Distribuída (26,3% do total):** Este projeto é **EXCEPCIONAL** para calibração porque tem breakdown detalhado da empreitada:
   - Civil 60% → Supraestrutura (R$ 6,5M)
   - Pintura 10% → Pintura (R$ 1,1M)
   - Cerâmicos 10% → Rev. Internos + Pisos (R$ 1,1M)
   - Hidro 6% + Elétr 6% → Instalações (R$ 1,3M)
   - Portas 3% → Esquadrias (R$ 325k)
   - Contenção 2% → Infraestrutura (R$ 217k)
   - Limpeza 2% → Gerenciamento (R$ 217k)
   - Louças 1% → Louças e Metais (R$ 108k)
   
   **Valor para calibração:** Permite separar **material vs MO** em cada macrogrupo, raro em executivos.

2. **Enxoval Separado (R$ 10,3M, 25,1% do total):** Permite comparação limpa com/sem enxoval:
   - **COM enxoval:** R$ 4.754/m² → CUB ratio 1,60 (MUITO ALTO)
   - **SEM enxoval:** R$ 3.559/m² → CUB ratio 1,20 (ALTO, mas justificável)
   
   **Valor para calibração:** Demonstra o impacto de **mobiliário** em studios — calibrar SEM enxoval.

3. **Climatização Separada (R$ 476k, 1,54%):** Raro ter exaustão, pressurização e SPDA separados de Instalações.
   
   **Valor para calibração:** Permite calibrar **Climatização** como macrogrupo independente.

4. **Louças e Metais Separados (R$ 662k, 2,15%):** Maioria dos projetos inclui em Instalações ou Complementares.
   
   **Valor para calibração:** Permite calibrar **Louças/Metais** como macrogrupo independente, ajustado por **densidade de unidades** (UR/AC).

5. **Verticalização Intensa (22 pavimentos):** CUB ratio 1,20 é alto, mas justificável por:
   - Estrutura verticalizada complexa
   - Contenção + 2 subsolos
   - Instalações longas (22 prumadas)
   - Studios compactos (maior custo fixo por m²)
   
   **Valor para calibração:** Referência para **obras verticalizadas** (>15 pavimentos) com contenção.

6. **Fachada Subdimensionada (R$ 16,98/m²):** **RED FLAG** para calibração.
   
   **Ação:** Verificar executivo original antes de usar na calibração. Se confirmado subdimensionamento, **EXCLUIR macrogrupo Fachada** da calibração ou ajustar manualmente.

7. **Comparativo com Urban Life e Barbados:**
   - **Parkside:** Alta complexidade, alta verticalização, alta densidade de UR
   - **Urban Life:** Média complexidade, média verticalização, média densidade de UR
   - **Barbados:** Baixa complexidade (3 pav.), baixa verticalização, baixa densidade de UR
   
   **Valor para calibração:** Os três projetos **se complementam** para cobrir espectro de complexidade:
   - Usar **Parkside** para obras verticalizadas (>15 pav.) com contenção
   - Usar **Urban Life** para obras médias (8-15 pav.) terreno plano
   - Usar **Barbados** para obras baixas (≤5 pav.) terreno irregular

8. **Supraestrutura Mat+MO Separados:** Materiais R$ 3,3M + MO R$ 6,5M = R$ 9,8M total
   
   **Valor para calibração:** Permite calibrar **MO de estrutura** separadamente (66,2% do total de supra).

### 🎯 Recomendações para Uso na Calibração

- **Macrogrupos confiáveis:** Mov.Terra, Infraestrutura, Supraestrutura, Impermeabilização, Instalações, Climatização, Rev.Internos, Teto, Pisos, Pintura, Esquadrias, Louças/Metais, Complementares
- **Macrogrupos com ressalva:** Alvenaria (abaixo faixa — verificar), Fachada (MUITO abaixo — **EXCLUIR** ou verificar), Gerenciamento (borda inferior), Imprevistos (abaixo — **risco**)
- **Índice global R$/m² (SEM enxoval):** Confiável (R$ 3.559,33 original, R$ 3.290,27 normalizado) — boa referência para **obras verticalizadas com contenção** em **Florianópolis**
- **CUB ratio (SEM enxoval):** Confiável (1,20) — padrão **ALTO** para studios verticalizados
- **Instalações:** **Excelente referência** (R$ 465/m², acima faixa similar mas justificável) — usar para obras com **alta densidade de unidades** (>0,015 UR/m²)
- **Louças e Metais:** **Excelente referência** (R$ 76/m², separado) — usar ajustado por **densidade de unidades**
- **Climatização:** **Excelente referência** (R$ 55/m², separado) — usar para obras com exaustão/pressurização/SPDA
- **Empreitada Global:** **EXCEPCIONAL para calibração** — permite separar Mat vs MO em múltiplos macrogrupos

### ⚠️ ALERTAS CRÍTICOS PARA CALIBRAÇÃO

1. **FACHADA SUBDIMENSIONADA:** R$ 16,98/m² é 9× menor que faixa mínima esperada (57-546).
   - **AÇÃO:** **VERIFICAR EXECUTIVO ORIGINAL** antes de usar Fachada na calibração.
   - **Se confirmado:** **EXCLUIR Fachada** ou ajustar manualmente baseado em benchmarks (usar R$ 100-120/m² similar).

2. **ENXOVAL EXCLUIR:** Sempre calibrar **SEM enxoval** (R$ 10,3M).
   - **AÇÃO:** Usar **R$ 3.559/m²** (sem enxoval), **NÃO** R$ 4.754/m² (com enxoval).

3. **DENSIDADE DE UNIDADES:** Louças/Metais (R$ 76/m²) reflete densidade alta (0,0188 UR/m²).
   - **AÇÃO:** Ajustar por densidade na calibração. Fórmula: `Louças/m² = R$ 4.000/UR × (UR/AC)`.

4. **IMPREVISTOS BAIXOS:** Apenas 0,95% do total (R$ 31/m²).
   - **AÇÃO:** Alertar que projeto tem **margem baixa** para contingências.

---

## RESUMO DE ÍNDICES GLOBAIS

### Valores Originais (Set/2025, CUB ago/2025 R$ 2.978,02, SEM Enxoval)

| Indicador | Valor | Un |
|---|---|---|
| **Custo total (sem ger., sem imprev., SEM enxoval)** | R$ 30.824.031 | R$ |
| **Custo total (com ger., SEM enxoval)** | R$ 30.698.649 | R$ |
| **Custo total (COM enxoval)** | R$ 41.168.406 | R$ |
| **R$/m² (sem ger., sem imprev., SEM enxoval)** | 3.559,33 | R$/m² |
| **R$/m² (com ger., SEM enxoval)** | 3.544,10 | R$/m² |
| **R$/m² (COM enxoval)** | 4.753,80 | R$/m² |
| **CUB ratio (com ger., SEM enxoval)** | 1,20 | CUB |
| **CUB ratio (COM enxoval)** | 1,60 | CUB |
| **R$/UR (sem ger., SEM enxoval)** | R$ 189.074 | R$/UR |
| **R$/UR (COM enxoval)** | R$ 252.515 | R$/UR |
| AC/UR | 53,13 | m²/un |
| Supraestrutura / AC (mat + MO) | 1.134,41 | R$/m² |
| Instalações / AC (mat + MO) | 465,13 | R$/m² |
| Esquadrias / AC (mat + MO) | 362,80 | R$/m² |
| Gerenciamento / AC | 278,78 | R$/m² |
| Louças e Metais / AC (mat + MO) | 76,47 | R$/m² |
| Climatização / AC | 54,98 | R$/m² |

### Valores Normalizados (Base Dez/2023, CUB R$ 2.752,67, Fator 0,9244)

| Indicador | Valor | Un |
|---|---|---|
| **Custo total (sem ger., sem imprev., SEM enxoval)** | R$ 28.493.585 | R$ |
| **Custo total (com ger., SEM enxoval)** | R$ 30.725.300 | R$ |
| **R$/m² (sem ger., sem imprev., SEM enxoval)** | 3.290,27 | R$/m² |
| **R$/m² (com ger., SEM enxoval)** | 3.548,98 | R$/m² |
| **CUB ratio (com ger., SEM enxoval)** | 1,29 | CUB |
| **CUB ratio (sem ger., sem imprev., SEM enxoval)** | 1,20 | CUB |
| **R$/UR (sem ger., SEM enxoval)** | R$ 174.778 | R$/UR |
| Supraestrutura / AC (mat + MO) | 1.048,66 | R$/m² |
| Instalações / AC (mat + MO) | 429,99 | R$/m² |
| Esquadrias / AC (mat + MO) | 335,38 | R$/m² |
| Gerenciamento / AC | 257,71 | R$/m² |
| Louças e Metais / AC (mat + MO) | 70,69 | R$/m² |
| Climatização / AC | 50,82 | R$/m² |

---

> **Fonte:** Executivo Parkside — Parkside Rio Branco (Av. Rio Branco, Centro, Florianópolis/SC)  
> **Extraído em:** 06/03/2026  
> **Notas CRÍTICAS:**  
> - **ENXOVAL EXCLUÍDO** (R$ 10.344.375, 25,1% do total) — calibração usa valores **SEM enxoval**  
> - **Empreitada Global DISTRIBUÍDA** (R$ 10.831.779, 26,3% do total) nos macrogrupos correspondentes — **RARO e VALIOSO**  
> - **Fachada SUBDIMENSIONADA** (R$ 16,98/m² vs 57-546 esperado) — **VERIFICAR antes de calibrar**  
> - **Louças/Metais SEPARADOS** (R$ 76/m²) — calibrar ajustado por densidade de unidades (UR/AC)  
> - **Climatização SEPARADA** (R$ 55/m²) — exaustão, pressurização, SPDA  
> - **Imprevistos BAIXOS** (0,95%, R$ 31/m²) — risco de estouro de orçamento  
> - **CUB ratio 1,20** (sem enxoval) é **ALTO**, mas justificável por verticalização intensa (22 pav.) + contenção + studios compactos  
> - **Supraestrutura R$ 1.049/m²** (31,87%) inclui MO Civil (empreitada R$ 6,5M, 66% do total supra)  
> - **Instalações R$ 465/m²** (13,07%) inclui MO Hidro+Elétr (empreitada R$ 1,3M, 32% do total instal.)  
> - Projeto **VALIOSO para calibração** de obras verticalizadas com contenção  
> - Adequado para calibração com ressalvas documentadas (Fachada, Louças ajustado por UR/AC)
