# Botânico — Neuhaus (Jul/2022)

> Análise completa de orçamento executivo.
> Criado: 06/03/2026
> Status: Calibrado

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Botânico | — |
| Código CTN | — | N/D | — |
| Revisão | — | N/D | — |
| Localização | — | SC (provável Bal. Piçarras/Penha) | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Neuhaus | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | **3.123,40** | m² |
| Unid. Habitacionais | UR_H | 20 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | **20** | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | **1** | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | **29** | meses |
| Data-base | — | **Jul/2022** | — |
| **CUB na Data-base** | — | **R$ 2.572,55** | **R$** |
| R$/m² Total | — | **3.622,71** | R$/m² |
| CUB ratio | — | **1,408** | CUB |
| Tipo de Laje | — | Não especificado (convencional provável) | — |
| Tipo de Fundação | — | Hélice contínua + blocos/baldrames | — |
| Padrão Acabamento | — | Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Não | Incluído em Gerenciamento |
| Valor ADM (se separado) | N/A | — |
| **Tem MOE (Mão de Obra) separado?** | Não | Embutida nos itens |
| Valor MOE (se separado) | N/A | — |
| Metodologia de rateio MOE | — | Embutida em cada macrogrupo |
| Custos diretos de obra (sem ADM/MOE) | R$ 9.226.097 | 81,5% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| Gerenciamento | 1-Gerenciamento | R$ 2.089.078,17 (18,46%) |
| Movimentação de Terra | 2-Mov. Terra | R$ 60.092,60 |
| Infraestrutura | 3-Infraestrutura | Fundações + infra |
| Supraestrutura | 4-Supraestrutura | Concreto fck 35 MPa, compensado plastificado |
| Alvenaria | 5-Alvenaria | Vedação (quant. BIM MDPLAN) |
| Impermeabilização | 6-Impermeabilização | Argamassa + manta asfáltica |
| Instalações | 7-Instalações | Hidro + elétrica + preventiva agregadas |
| Sistemas Especiais | 8-Sist. Especiais | Inclui climatização |
| Climatização | 9-Climatização | R$ 0 (embutido em Sist. Especiais) |
| Rev. Int. Parede | 10-Rev. Int. Parede | Chapisco + reboco + massa |
| Teto | 11-Teto | Gesso modulado |
| Pisos/Acabamentos | 12-Pisos | Porcelanato + cerâmico + vinílico |
| Pintura | 13-Pintura | Sistema completo |
| Esquadrias | 14-Esquadrias | Alumínio + guarda-corpo + portas |
| Louças e Metais | 15-Louças e Metais | R$ 0 (embutido em acabamentos) |
| Fachada | 16-Fachada | ACM perfurado + pastilhas cerâmicas |
| Complementares | 17-Complementares | Cobertura + serv. complementares |
| Imprevistos | 18-Imprevistos | R$ 0 (embutido em Complementares) |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Observação |
|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | N/D | Terreno não informado |
| Área por Unidade | AC / UR | **156,2** m²/un | Unidades médias |
| Unidades por Terreno | UR / AT | N/D | — |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Observação |
|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | — |
| UR por Elevador | UR / ELEV | **20** | Único projeto da base com 1 elevador |
| Elevadores por Pavimento | ELEV / NP | N/D | — |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | 20 | 100% | 156,2 |
| Comercial | 0 | 0% | — |
| Estúdio | 0 | 0% | — |

### 2.4 Distribuição de Áreas por Pavimento

Não disponível.

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | **R$ 565.758,76** |
| R$ / UR (habitacionais) | Total / UR_H | **R$ 565.758,76** |
| CUB / UR | (R$/UR) / CUB | **219,9 CUB** |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % |
|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 2.089.078,17 | **668,85** | **18,46%** |
| 2 | Movimentação de Terra | 60.092,60 | 19,24 | 0,53% |
| 3 | Infraestrutura | 920.136,14 | **294,59** | 8,13% |
| 4 | Supraestrutura | 2.567.394,33 | **821,99** | **22,69%** |
| 5 | Alvenaria | 307.538,54 | 98,46 | 2,72% |
| 6 | Impermeabilização | 256.448,09 | 82,11 | 2,27% |
| 7 | Instalações (agrupado) | 1.120.560,70 | 358,76 | 9,90% |
| 8 | Sistemas Especiais | 487.000,00 | 155,92 | 4,30% |
| 9 | Climatização | 0 | 0 | 0% |
| 10 | Rev. Internos Parede | 632.400,78 | 202,47 | 5,59% |
| 11 | Teto | 147.356,11 | 47,18 | 1,30% |
| 12 | Pisos | 454.436,44 | 145,49 | 4,02% |
| 13 | Pintura | 251.314,00 | 80,46 | 2,22% |
| 14 | Esquadrias | 1.222.124,41 | **391,28** | 10,80% |
| 15 | Louças e Metais | 0 | 0 | 0% |
| 16 | Fachada | 236.645,69 | 75,77 | 2,09% |
| 17 | Complementares | 562.649,21 | 180,14 | 4,97% |
| 18 | Imprevistos | 0 | 0 | 0% |
| — | **TOTAL** | **11.315.175,21** | **3.622,71** | **100%** |

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

Não disponível no nível de detalhamento do executivo.

**Concreto especificado:**
- **fck 35 MPa** (infraestrutura + supraestrutura)
- Compensado plastificado + escoramento metálico

#### Armadura (Aço)

Não disponível.

#### Forma

Não disponível.

**Sistema especificado:**
- Compensado plastificado (premium)
- Escoramento metálico

#### Tipo de Laje e Complementos

| Item | Especificação |
|---|---|
| Tipo de laje (tipo) | Não especificado (convencional provável) |
| Tipo de laje (embasamento) | Não especificado |
| Sistema de forma | Compensado plastificado + escoramento metálico |

#### MO Supraestrutura

Não disponível separadamente.

### 4.2 Infraestrutura

#### Fundação

| Item | Especificação |
|---|---|
| Tipo de fundação | Hélice contínua + blocos/baldrames |
| Concreto | fck 35 MPa |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

Dados quantitativos detalhados não disponíveis. Orçamento apresentado em macrogrupos.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. |
|---|---|---|---|
| **TOTAL AGRUPADO** | **1.120.560,70** | **358,76** | **100%** |

> Instalações apresentadas de forma agrupada no executivo (hidro + elétrica + preventiva).

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

**Sistema especificado:**
- Chapisco + reboco
- Rev. Int. Parede: R$ 202,47/m²

### 7.2 Pisos

**Sistema especificado:**
- Porcelanato (áreas comuns + banheiros)
- Cerâmico (áreas técnicas)
- Vinílico (áreas íntimas)
- Drenante + podotátil (térreo)

**Índice:** R$ 145,49/m²

### 7.3 Teto

**Sistema especificado:**
- Gesso modulado standard (áreas secas)
- Gesso modulado resistente à umidade (áreas molhadas)
- Garagens: laje aparente + estucamento

**Índice:** R$ 47,18/m²

### 7.4 Pintura

**Sistema especificado:**
- Sistema completo parede

**Índice:** R$ 80,46/m²

### 7.5 Fachada

**Sistema especificado:**
- Chapisco + reboco + textura acrílica + pintura acrílica
- **ACM perfurado** (elemento de destaque)
- **Pastilhas cerâmicas**
- Alto padrão

**Índice:** R$ 75,77/m²

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

**Sistema especificado:**
- Alumínio (portas + janelas)
- Guarda-corpo alumínio/vidro temperado
- Portas madeira

**Índice total:** R$ 391,28/m² (Top 3 da base)

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Valor (R$) | R$/m² |
|---|---|---|
| **Sist. Especiais (com climatização)** | **487.000,00** | **155,92** |

> Climatização embutida em Sistemas Especiais (sistema de climatização listado).

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

Gerenciamento apresentado como categoria única:

| Item | Valor (R$) | R$/m² | % |
|---|---|---|---|
| **Gerenciamento** | **2.089.078,17** | **668,85** | **18,46%** |

**RECORDE ABSOLUTO DA BASE** — Custos fixos não diluem em projeto pequeno.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

**Sistema especificado:**
- Bacias sanitárias + acabamentos de registro (apartamentos)
- Conjunto completo (áreas comuns)

**Valor:** R$ 0 (não separado no breakdown)

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor |
|---|---|---|
| Ritmo de construção | AC / Prazo | **107,7** m²/mês |
| Burn rate mensal | Total / Prazo | **R$ 390,2k**/mês |
| UR por mês | UR / Prazo | **0,69** un/mês |
| Custo / mês / m² | (Total/Prazo) / AC | **124,9** R$/m²/mês |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

**Sistema especificado:**
- Argamassa polimérica (BWC, cozinha, sacada, peitoris, lajes)
- Manta asfáltica (áreas externas)

**Índice:** R$ 82,11/m²

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² |
|---|---|---|
| Cobertura | 3.516,57 | 1,13 |
| Serv. Complementares | 559.132,64 | 179,02 |
| **TOTAL** | **562.649,21** | **180,14** |

> Imprevistos embutidos nos Serv. Complementares (mencionado na PPTX slide 11).

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

**Projeto de referência citado:**
- **Brava Garden** (incluído na coluna de benchmark do executivo)

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### 🔴 RECORDES MÚLTIPLOS — Efeito Escala Projeto Pequeno

#### **MENOR AC da base: 3.123 m²**
- Menos da metade do 2º menor projeto
- Efeito escala: custos fixos não diluem

#### **Gerenciamento R$ 669/m² (18,5%): RECORDE ABSOLUTO**
- Benchmark base: R$ 300-450/m² (9-15%)
- Projeto pequeno = custos fixos pesam mais

#### **Supra R$ 822/m² (22,7%): RECORDE em R$/m²**
- Compensado plastificado = sistema premium
- fck 35 MPa = especificação alta
- Benchmark base: R$ 600-750/m²

#### **Infra R$ 295/m² (8,1%): RECORDE**
- Hélice contínua em escala pequena = custo unitário alto
- Benchmark base: R$ 150-250/m²

#### **Esquadrias R$ 391/m² (10,8%): Top 3 da base**
- Alumínio + guarda-corpo alumínio/vidro temperado
- Benchmark base: R$ 250-350/m²

#### **CUB ratio 1,41: 2º mais alto da base**
- Atrás apenas do Brava Sixteen (1,73)
- Indica custo elevado vs CUB de referência

#### **R$/m² norm R$ 3.876: 2º mais caro da base**
- Normalizado para dez/2023
- Reflexo dos múltiplos recordes

### 🔵 CONTEXTO — Projeto Boutique

- **20 UR:** menor quantidade da base
- **1 elevador:** único projeto da base com apenas 1 elevador
- **29 meses:** prazo curto para o tamanho
- **Fachada premium:** ACM perfurado + pastilhas cerâmicas = alto padrão
- **Localização:** SC (provável Balneário Piçarras/Penha)
- **Incorporador:** Neuhaus (atuação regional)

### ⚠️ IMPACTO NA CALIBRAÇÃO

**ESTE PROJETO É OUTLIER POR ESCALA**
- Os R$/m² altos são resultado de **ineficiência de escala**, não de padrão excepcional
- Usar com cautela como referência:
  - ✅ Tecnologias e sistemas (forma compensado, fck 35, etc)
  - ✅ Percentuais relativos entre macrogrupos
  - ⚠️ Valores absolutos R$/m² (distorcidos pela escala)

**Benchmark recomendado:**
- Para projetos >8.000m²: usar medianas da base
- Para projetos 3.000-5.000m²: Botânico é referência válida
- Para projetos <3.000m²: Botânico pode até subestimar custos (escala ainda menor)

### ✅ DENTRO DA FAIXA (ajustado pela escala)

- **Alvenaria:** R$ 98/m² — esperado para projeto BIM (quantificação precisa)
- **Pintura:** R$ 80/m² — alinhado
- **Fachada:** R$ 76/m² — razoável mesmo com ACM (área de fachada menor em projeto pequeno)

### 📝 PARTICULARIDADES

- **Quantificação:** BIM MDPLAN (não Cartesian)
- **Climatização:** embutida em Sist. Especiais (não separada)
- **Imprevistos:** embutidos em Complementares
- **Louças:** bacias + acabamentos registro (não separadas no breakdown)
- **Data-base:** Jul/2022 (CUB SC R$ 2.572,55)

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 11.315.175,21 | R$ |
| **R$/m²** | 3.622,71 | R$/m² |
| **R$/m² normalizado (dez/23)** | 3.876,30 | R$/m² |
| **CUB ratio** | **1,408** | CUB |
| **R$/UR** | R$ 565.758,76 | R$/UR |
| **AC/UR** | 156,2 | m²/un |
| Gerenciamento / AC | **669** | R$/m² |
| Infra / AC | **295** | R$/m² |
| Supra / AC | **822** | R$/m² |
| Instalações / AC | 359 | R$/m² |
| Esquadrias / AC | **391** | R$/m² |
| Fachada / AC | 76 | R$/m² |
| Ritmo construção | 108 | m²/mês |
| Burn rate | R$ 390k | R$/mês |
| **Elevadores** | **1** | un |
| **UR por elevador** | **20** | UR/elev |

---

> **Fonte:** Orçamento Executivo Botânico — Neuhaus
> **Extraído em:** 06/03/2026
> **Notas:** AC EXPLÍCITO 3.123m². MENOR projeto da base. Múltiplos recordes por efeito escala. Benchmark inclui Brava Garden. Quant. MDPLAN. Climatização + Imprevistos embutidos.
