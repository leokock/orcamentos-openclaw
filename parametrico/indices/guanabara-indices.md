# Residencial Guanabara — André Muller (Sinop/MT)

> Análise completa do orçamento executivo — 43º projeto da base paramétrica Cartesian
> Criado: 06/03/2026 | Data-base: Fev/2023
> **DESTAQUE:** Primeiro projeto com ALVENARIA ESTRUTURAL, primeiro fora de SC, maior nº de UR da base (64)

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Residencial Guanabara | — |
| Incorporador/Cliente | — | André Muller | — |
| Localização | — | Sinop/MT | — |
| Endereço | — | Rua Guanabara, 1280 - Residencial Ipanema | — |
| Área do Terreno | AT | 3.002,77 | m² |
| Área Construída | AC | 4.440,50 | m² |
| Total Unidades | UR | 64 | un |
| Área por apt | — | 57,65 | m² |
| AC/UR | — | 69,4 | m²/un |
| Nº Total Pavimentos | NP | ~9 | un |
| Nº Pavimentos Tipo | NPT | 6 | un |
| Nº Pav. Garagem | NPG | 0 | un |
| Elevadores | ELEV | 2 | un |
| Torres | — | 2 (idênticas) | un |
| Prazo de Obra | — | 18 | meses |
| Data-base | — | Fev/2023 | — |
| **CUB na Data-base** | — | **R$ 2.591,01** | **R$** |
| Valor Total | — | R$ 14.337.198,41 | R$ |
| R$/m² Total | — | 3.228,74 | R$/m² |
| CUB ratio | — | 1,2461 | CUB |
| Tipo de Laje | — | Convencional | — |
| Tipo de Fundação | — | Sapatas + blocos/baldrames (embasamento) + Estaca hélice (torres) | — |
| Padrão Acabamento | — | Médio | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | Incluído no Gerenciamento Técnico |
| Valor ADM (se separado) | R$ 480.558 | 3,35% do total |
| **Tem MOE (Mão de Obra) separado?** | Sim | MO terceirizada agrupada na UC2 (embasamento) |
| Valor MOE (se separado) | R$ 3.819.542 | 26,64% do total (todas etapas) |
| Metodologia de rateio MOE | — | Global consolidado no embasamento |
| Custos diretos de obra (sem ADM/MOE) | R$ 10.517.640 | 73,36% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| UC5 Gerenciamento Técnico | 1-Gerenciamento | Projetos R$ 138k, incorporação R$ 120k, taxas R$ 292k |
| UC5 Gerenciamento Administrativo | 1-Gerenciamento | SMS R$ 37k, canteiro R$ 767k, equip R$ 71k |
| UC2 MO Própria | 1-Gerenciamento | 4 serventes + 2 pedreiros |
| UC2 Mov. Terra | 2-Mov. Terra | — |
| UC2 Fundação (sapatas/baldrames) | 3-Infraestrutura | Fundação rasa no embasamento |
| Torres Fundação (estaca hélice) | 3-Infraestrutura | R$ 325k/torre |
| UC2 Estrutura + Torres Estrutura | 4-Supraestrutura | Lajes + vigas (sem pilares de CA nos apts) |
| UC2 Alvenaria + Torres Alvenaria | 5-Alvenaria | ESTRUTURAL fgk 15-20 MPa + vedação + drywall |
| UC2 Impermeabilização | 6-Impermeabilização | — |
| UC2 Instalações + Torres Instalações | 7-Instalações | Inclui ETE própria R$ 224k/torre |
| UC2 Sistemas Especiais + Torres | 8-Sist. Especiais | Elevadores R$ 218k/torre |
| UC2 Climatização | 9-Climatização | — |
| UC2 Revestimentos Internos | 10-Rev. Int. Parede | — |
| UC2 Teto | 11-Teto | — |
| UC2 Pisos | 12-Pisos | — |
| UC2 Pintura | 13-Pintura | — |
| UC2 Esquadrias | 14-Esquadrias | — |
| UC2 Louças e Metais | 15-Louças e Metais | — |
| UC2 Fachada | 16-Fachada | Textura acrílica (sem ACM/pastilha) |
| UC2 Complementares | 17-Complementares | — |
| UC2 Imprevistos | 18-Imprevistos | 1,52% do total |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Observação |
|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 1,48 | 5 lotes, 600m² cada |
| Área por Unidade | AC / UR | 69,4 m²/un | **MENOR DA BASE** (4× menor que Adda/Serenity) |
| Unidades por Terreno | UR / AT | 0,021 un/m² | 64 UR (maior da base) |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Observação |
|---|---|---|---|
| UR por Elevador | UR / ELEV | 32 | 1 elevador/torre |
| Elevadores por Pavimento | ELEV / NP | 0,22 | 2 torres com 9 pavimentos cada |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | 64 | 100% | 57,65 |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Observação |
|---|---|
| Embasamento | Térreo + áreas comuns |
| Torres (2×) | Térreo + 6 tipos + PCD + cobertura/barrilete |
| Total | 9 pavimentos por torre |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 224.018 |
| CUB / UR | (R$/UR) / CUB | 86,5 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | Comparativo Base |
|---|---|---|---|---|---|
| 1 | Gerenciamento | 1.720.320,91 | 387,42 | 12,00 | ⚠️ ACIMA — Inclui MO própria |
| 2 | Mov. Terra | 19.982,12 | 4,50 | 0,14 | ✅ Dentro |
| 3 | Infraestrutura | 1.068.053,13 | 240,53 | 7,45 | ✅ Dentro |
| 4 | Supraestrutura | 1.410.081,29 | 317,55 | 9,83 | 🔽 **BAIXO** (alvenaria estrutural) |
| 5 | Alvenaria | 1.423.157,27 | 320,49 | 9,92 | 🔴 **ALTO** (estrutural) |
| 6 | Impermeabilização | 322.448,32 | 72,62 | 2,25 | ✅ Dentro |
| 7 | Instalações | 1.826.248,50 | 411,27 | 12,74 | 🔴 **ALTO** (inclui ETE própria) |
| 8 | Sist. Especiais | 1.003.933,91 | 226,14 | 7,00 | ✅ Dentro |
| 9 | Climatização | 74.208,84 | 16,71 | 0,52 | ✅ Dentro |
| 10 | Rev. Int. Parede | 1.247.304,65 | 280,89 | 8,70 | ⚠️ ACIMA |
| 11 | Teto | 456.659,62 | 102,84 | 3,18 | 🔴 **ALTO** |
| 12 | Pisos | 1.194.226,70 | 268,94 | 8,33 | ✅ Dentro |
| 13 | Pintura | 460.055,52 | 103,60 | 3,21 | ✅ Dentro |
| 14 | Esquadrias | 1.041.740,04 | 234,60 | 7,27 | ✅ Dentro |
| 15 | Louças e Metais | 106.062,57 | 23,89 | 0,74 | ✅ Dentro |
| 16 | Fachada | 534.054,65 | 120,27 | 3,72 | ✅ Dentro (textura acrílica) |
| 17 | Complementares | 210.941,50 | 47,50 | 1,47 | ✅ Dentro |
| 18 | Imprevistos | 217.718,87 | 49,03 | 1,52 | ✅ Dentro (1,5% padrão) |
| — | **TOTAL** | **14.337.198,41** | **3.228,74** | **100%** | — |

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

**NOTA CRÍTICA:** Alvenaria estrutural — pilares de concreto armado apenas em áreas comuns. Paredes carregam a estrutura nas torres.

| Item | Especificação | Observação |
|---|---|---|
| Concreto fck | 25 MPa | **MAIS BAIXO DA BASE** (infra e supra) |
| Tipo estrutural | Alvenaria ESTRUTURAL | Primeiro projeto da base nesse sistema |
| Tipo de laje (tipo) | Convencional | — |

#### MO Supraestrutura

**NOTA:** MO terceirizada da UC2 (R$ 3.819.542) cobre TODAS as etapas num único agrupamento. Impossível separar custo de MO específico de supraestrutura sem quebrar a estrutura do orçamento original.

### 4.2 Infraestrutura

#### Fundação Profunda (Torres)

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | Hélice contínua | — | — | Fundação profunda nas torres |
| Custo/torre | 2 | un | R$ 325.000 | R$ 650k total |

#### Fundação Rasa (Embasamento)

| Item | Especificação |
|---|---|
| Tipo | Sapatas + blocos + baldrames |
| Aplicação | Infraestrutura rasa no embasamento |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

**NOTA:** Levantamento quantitativo não disponível no orçamento fornecido. Impossível calcular índices m²/m² AC sem planilha de quantitativos detalhada.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | Observação |
|---|---|---|---|---|
| **TOTAL** | **1.826.248,50** | **411,27** | **100%** | Inclui ETE própria ~R$ 448k (R$ 224k/torre) |

**DESTAQUE:** R$ 411/m² é ALTO para a base, mas contexto justifica — sistema próprio de tratamento de esgoto (fossa séptica + filtro anaeróbico + sumidouros).

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

**NOTA:** Detalhamento de PUs e quantitativos não disponível no orçamento consolidado fornecido. Valores agregados por macrogrupo apenas.

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

| Categoria | Valor (R$) | R$/m² AC | Observação |
|---|---|---|
| **TOTAL** | **1.041.740,04** | **234,60** | Dentro da faixa esperada |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) | Observação |
|---|---|---|---|---|
| Elevadores | 2 | ~R$ 218.000 | ~R$ 436.000 | 1 por torre |
| ETE | 2 | ~R$ 224.000 | ~R$ 448.000 | Sistema próprio/torre |
| Outros | — | — | ~R$ 120.000 | CFTV, automação, etc |
| **TOTAL** | — | — | **1.003.933,91** | R$ 226/m² |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| **TOTAL PROJETOS** | **R$ 138.000** | **31,08** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Incorporação + taxas gerais | R$ 120.000 | 27,02 |
| Outras taxas | R$ 292.000 | 65,77 |
| **TOTAL TAXAS** | **R$ 412.000** | **92,79** |

### 10.3 Equipe Administrativa

**NOTA:** Incluído no Gerenciamento Administrativo (R$ 876.301).

| Item | Valor (R$) | Observação |
|---|---|---|
| SMS | R$ 37.000 | Segurança |
| Canteiro | R$ 767.000 | Infraestrutura |
| Equipamentos | R$ 71.000 | Manutenção (equipamentos próprios) |

### 10.4 MO Própria (Apoio)

| Cargo | Observação |
|---|---|
| Serventes | 4 (apoio civil + canteiro) |
| Pedreiros | 2 |
| **Custo total** | **R$ 363.462** |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Observação |
|---|---|---|
| Manipulador telescópico | Próprio | Manutenção apenas |
| Condutor entulho | Próprio | Manutenção apenas |
| Carro | Próprio | Manutenção apenas |
| Mini grua | Próprio | Manutenção apenas |
| Andaime fachadeiro | Próprio | Manutenção apenas |

**DESTAQUE:** Equipamentos próprios (não locados) — custo de manutenção R$ 71k dentro do Gerenciamento.

### 10.6 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 138.000 | 31,08 | 8,02% | 0,96% |
| Taxas e Licenças | 412.000 | 92,79 | 23,95% | 2,87% |
| Gerenciamento Administrativo | 876.301 | 197,35 | 50,94% | 6,11% |
| MO Própria | 363.462 | 81,86 | 21,13% | 2,54% |
| **TOTAL CI (sem MO terceirizada)** | **1.720.321** | **387,42** | **100%** | **12,00%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Valor Total (R$) | /UR | R$/m² AC |
|---|---|---|---|
| **TOTAL** | **106.062,57** | **R$ 1.657/UR** | **23,89** |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Observação |
|---|---|---|---|
| Ritmo de construção | AC / Prazo | 247 m²/mês | 2 torres paralelas |
| Burn rate mensal | Total / Prazo | R$ 796.511/mês | — |
| Meses por pavimento | Prazo / NP | 2,0 | ~9 pavimentos/torre |
| UR por mês | UR / Prazo | 3,6 un/mês | 64 UR em 18 meses |
| Custo / mês / m² | (Total/Prazo) / AC | 179 R$/m²/mês | — |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Categoria | Valor (R$) | R$/m² AC | Observação |
|---|---|---|
| **TOTAL** | **322.448,32** | **72,62** | Dentro da faixa esperada |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Observação |
|---|---|---|
| **TOTAL** | **210.941,50** | **47,50** | Dentro da faixa |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

### Projetos de Referência (da própria planilha)

| Projeto | Cidade | Data | CUB | R$/m² | Observação |
|---|---|---|---|---|---|
| Belissimo | — | Out/22 | 2.632 | ~1.693 | **Sem gerenciamento** |
| Homeset | — | Dez/22 | 2.643 | ~2.312 | **Sem gerenciamento** |
| Carraro | — | Set/22 | 1.907 | ~4.303 | Outlier alto |

**Faixa referência Muller:** R$ 2.100-3.100/m² para obras similares  
**Guanabara:** R$ 3.228/m² — dentro do topo da faixa (contexto MT + alvenaria estrutural)

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### 🔵 TIPOLOGIA NOVA NA BASE

- ✅ **Primeiro projeto com ALVENARIA ESTRUTURAL**
- ✅ **Primeiro projeto fora de SC** (Sinop/MT — interior do Mato Grosso)
- ✅ **64 UR** — MAIS unidades da base
- ✅ **AC/UR = 69,4 m²** — MENOR da base (4× menor que Adda/Serenity)
- ✅ **2 torres idênticas + embasamento** — não torre única

### 🔴 ALERTAS — Acima da Média

- **Alvenaria R$ 320/m²** — MAIS ALTO da base, mas é ESTRUTURAL (substitui parte da supraestrutura)
  - **Contexto:** Blocos estruturais fgk 15-20 MPa + graute + armadura
  - **Redistribuição estrutural:** Supra + Alvenaria = R$ 638/m² é ABAIXO da maioria dos projetos em concreto armado
- **Teto R$ 103/m²** — ALTO (benchmark 50-80)
- **Rev. Int. Parede R$ 281/m²** — acima do esperado (150-220)
- **Instalações R$ 411/m²** — alto, mas justificado (inclui ETE própria R$ 224k/torre)
- **Gerenciamento R$ 387/m²** — acima (inclui MO própria R$ 363k)

### ✅ DENTRO DA FAIXA

- **Fachada R$ 120/m²** — textura acrílica (sem ACM/pastilha)
- **Esquadrias R$ 234/m²** — dentro da faixa
- **Imprevistos 1,52%** — padrão
- **CUB ratio 1,25** — próximo da mediana da base
- **Sist. Especiais R$ 226/m²** — inclui elevadores R$ 218k/torre
- **Mov. Terra R$ 4,50/m²** — muito baixo (terreno plano)

### 🔽 ABAIXO DA MÉDIA

- **Supraestrutura R$ 317/m²** — LOW porque não tem pilares de concreto armado nas torres (exceto áreas comuns)
  - **Contexto:** Em alvenaria estrutural, paredes carregam a estrutura — custo migra para Alvenaria
- **Concreto fck 25 MPa** — MAIS BAIXO DA BASE (benchmark 30-40 MPa)

### ⚠️ CONTEXTUALIZAÇÃO ESTRUTURAL — ALVENARIA ESTRUTURAL

**Regra de interpretação:**  
Em projetos com alvenaria estrutural, o custo se redistribui:
- **MENOS na Supraestrutura** (apenas lajes + vigas, sem pilares de CA)
- **MAIS na Alvenaria** (paredes carregam a estrutura: blocos estruturais, graute, armadura)

**Comparação correta com concreto armado:**  
Somar Supra + Alvenaria = R$ 638/m² — ABAIXO da maioria dos projetos em concreto armado (que têm Supra R$ 600-800/m² + Alvenaria R$ 100-200/m²).

### 📝 Particularidades

- **Localização:** Interior do Mato Grosso (primeiro projeto fora de SC)
- **ETE própria:** Sistema completo (fossa séptica + filtro anaeróbico + sumidouros) — R$ 448k total
- **Equipamentos:** Próprios (manipulador telescópico, mini grua, andaime fachadeiro, etc) — apenas manutenção
- **MO terceirizada:** Agrupada em conta única (R$ 3,8M) cobrindo TODAS as etapas
- **Padrão:** Médio (apts compactos 57m², interior MT)
- **Torres:** 2 idênticas (não torre única como maioria da base)

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 14.337.198,41 | R$ |
| **R$/m²** | 3.228,74 | R$/m² |
| **CUB ratio** | 1,25 | CUB |
| **R$/UR** | R$ 224.018 | R$/UR |
| **AC/UR** | 69,4 | m²/un |
| **UR total** | 64 | un |
| **Torres** | 2 | un |
| **Elevadores** | 2 | un |
| **Prazo** | 18 | meses |
| **Ritmo** | 247 | m²/mês |
| **Burn rate** | R$ 796.511 | R$/mês |
| Concreto fck | 25 | MPa |
| Alvenaria tipo | Estrutural (fgk 15-20) | — |
| Fundação embasamento | Sapatas + blocos/baldrames | — |
| Fundação torres | Estaca hélice | — |
| ETE | Própria (2 sistemas) | — |

---

## NORMALIZAÇÃO CUB BASE (dez/2023)

| Item | Valor |
|---|---|
| CUB base Cartesian | R$ 2.752,67 |
| CUB MT mar/23 (projeto) | R$ 2.591,01 |
| Fator de atualização | 1,06240 |
| **R$/m² normalizado** | **R$ 3.430,26** |

### Categorias Normalizadas (R$/m² dez/2023)

| Macrogrupo | Original (fev/23) | Normalizado (dez/23) |
|---|---|---|
| Gerenciamento | 387,42 | 411,56 |
| Mov. Terra | 4,50 | 4,78 |
| Infraestrutura | 240,53 | 255,55 |
| Supraestrutura | 317,55 | 337,31 |
| Alvenaria | 320,49 | 340,44 |
| Impermeabilização | 72,62 | 77,13 |
| Instalações | 411,27 | 436,83 |
| Sist. Especiais | 226,14 | 240,18 |
| Climatização | 16,71 | 17,75 |
| Rev. Int. Parede | 280,89 | 298,36 |
| Teto | 102,84 | 109,25 |
| Pisos | 268,94 | 285,69 |
| Pintura | 103,60 | 110,07 |
| Esquadrias | 234,60 | 249,18 |
| Louças e Metais | 23,89 | 25,37 |
| Fachada | 120,27 | 127,75 |
| Complementares | 47,50 | 50,46 |
| Imprevistos | 49,03 | 52,09 |

---

> **Fonte:** Orçamento Executivo Residencial Guanabara  
> **Incorporador:** André Muller  
> **Extraído em:** 06/03/2026  
> **Notas:** Primeiro projeto da base com alvenaria estrutural. MO terceirizada agrupada em conta única na UC2 (embasamento). Concreto fck 25 MPa (mais baixo da base). ETE própria. Equipamentos próprios (manutenção). Interior MT — primeiro projeto fora de SC.
