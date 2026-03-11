# Velazquez Residence — Índices de Orçamento Executivo

> Mussi Empreendimentos | Itajaí/SC | Data-base: Jul/2020
> Extraído em: 06/03/2026
> Projeto #45 da base de calibração

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Velazquez Residence | — |
| Código CTN | — | N/D | — |
| Revisão | — | Executivo Final | — |
| Localização | — | Itajaí/SC | — |
| Endereço | — | Rua Laguna, 100 - Fazenda | — |
| Incorporador/Cliente | — | Mussi Empreendimentos | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | ~13.000 (estimado) | m² |
| Unid. Habitacionais | UR_H | ~55 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | ~55 | un |
| Nº Total Pavimentos | NP | ~34 | un |
| Nº Pavimentos Tipo | NPT | 28 | un |
| Nº Pav. Garagem | NPG | 3 (G2, G3, G4) | un |
| Elevadores | ELEV | 3 (2 social + 1 serviço) | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 46 | meses |
| Data-base | — | Jul/2020 | — |
| **CUB na Data-base** | — | **R$ 2.061,00** | **R$** |
| R$/m² Total | — | 2.531,76 | R$/m² |
| CUB ratio | — | 1,23 | CUB |
| Tipo de Laje | — | Nervurada com EPS (cubetas) | — |
| Tipo de Fundação | — | Profunda (blocos + baldrames) | — |
| Padrão Acabamento | — | Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | Embutido em Gerenciamento UC2 |
| Valor ADM (se separado) | R$ 3.797.960 | 11,54% do total |
| **Tem MOE (Mão de Obra) separado?** | Não | Embutido em cada UC |
| Valor MOE (se separado) | N/A | — |
| Metodologia de rateio MOE | — | Embutido nos custos diretos |
| Custos diretos de obra (sem ADM/MOE) | R$ 29.114.910 | 88,46% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| UC2 - Gerenciamento Técnico | 1-Gerenciamento | Projetos, consultorias, ensaios, taxas |
| UC2 - Gerenciamento Administrativo | 1-Gerenciamento | SMS, ADM/Canteiro, Equipamentos (grua + elev) |
| UC3 - Mov. Terra | 2-Mov. Terra | — |
| UC3 - Infraestrutura | 3-Infraestrutura | Fundação blocos + baldrames |
| UC3 - Supraestrutura | 4-Supraestrutura | Concreto fck 40 MPa (toda torre) |
| UC3 - Alvenaria | 5-Alvenaria | Vedação |
| UC3 - Impermeabilização | 6-Impermeabilização | — |
| UC3 - Instalações | 7-Instalações | Elétricas + Hidrossanitárias + Preventivas |
| UC3 - Sistemas Especiais | 8-Sist. Especiais | 3 elevadores + escada pressurizada + piscina |
| UC3 - Climatização | 9-Climatização | — |
| UC3 - Rev. Int. Parede | 10-Rev. Int. Parede | — |
| UC3 - Teto | 11-Teto | — |
| UC3 - Pisos | 12-Pisos | — |
| UC3 - Pintura | 13-Pintura | — |
| UC3 - Esquadrias | 14-Esquadrias | Laqueadas (alto padrão) |
| UC3 - Louças e Metais | 15-Louças e Metais | R$ 0 (embutido em acabamentos) |
| UC3 - Fachada | 16-Fachada | — |
| UC3 - Complementares | 17-Complementares | Cobertura + serv. complementares |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | N/D | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 236,4 m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | N/D | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | 18,3 | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | 0,088 | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | ~55 | 100% | ~236 |
| Comercial | 0 | 0% | — |
| Estúdio | 0 | 0% | — |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | ~300 | ~2,3% |
| G2 (Garagem) | 747 | 5,7% |
| G3 (Garagem) | 935 | 7,2% |
| G4 (Garagem) | 958 | 7,4% |
| Lazer | 992 | 7,6% |
| Tipo (×26) | ~7.800 | ~60% |
| Tipo Diferenciado | 591 | 4,5% |
| Duplex (inferior + superior) | 440 | 3,4% |
| Telhado + Caixa d'Água | ~200 | ~1,5% |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 598.416 |
| R$ / UR (habitacionais) | Total / UR_H | R$ 598.416 |
| CUB / UR | (R$/UR) / CUB | 290,3 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 3.797.959,92 | 292,15 | 11,54% | 200 - 500 |
| 2 | Movimentação de Terra | 46.640,62 | 3,59 | 0,14% | 5 - 100 |
| 3 | Infraestrutura | 1.921.114,38 | 147,78 | 5,84% | 150 - 270 |
| 4 | Supraestrutura | 8.688.169,07 | 668,32 | 26,39% | 550 - 800 |
| 5 | Alvenaria | 1.102.622,10 | 84,82 | 3,35% | 100 - 350 |
| 6 | Impermeabilização | 415.350,45 | 31,95 | 1,26% | 30 - 80 |
| 7 | Instalações (agrupado) | 3.901.033,42 | 300,08 | 11,85% | 240 - 575 |
| 8 | Sistemas Especiais | 1.515.000,00 | 116,54 | 4,60% | 85 - 255 |
| 9 | Climatização | 495.806,00 | 38,14 | 1,51% | 18 - 105 |
| 10 | Rev. Internos Parede | 1.190.618,44 | 91,59 | 3,62% | 90 - 300 |
| 11 | Teto | 493.352,67 | 37,95 | 1,50% | 30 - 130 |
| 12 | Pisos | 2.061.713,72 | 158,59 | 6,26% | 110 - 290 |
| 13 | Pintura | 941.705,75 | 72,44 | 2,86% | 50 - 195 |
| 14 | Esquadrias | 2.766.657,42 | 212,82 | 8,40% | 180 - 625 |
| 15 | Louças e Metais | 0 | 0 | 0% | 0 - 40 |
| 16 | Fachada | 1.452.853,59 | 111,76 | 4,41% | 70 - 280 |
| 17 | Complementares | 2.122.272,79 | 163,25 | 6,45% | 50 - 400 |
| 18 | Imprevistos | 0 | 0 | 0% | 0 - 60 |
| — | **TOTAL** | **32.912.870,34** | **2.531,76** | **100%** | — |

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Dados Gerais Concreto

| Item | Especificação |
|---|---|
| **fck supraestrutura** | **40 MPa (TODA a torre — pilares, vigas, lajes)** |
| **fck infraestrutura** | Blocos: 30 MPa / Baldrames: 40 MPa |
| Tipo de laje | Nervurada com EPS (cubetas) |
| Fundação | Profunda — blocos + baldrames |

**Nota:** Uso de concreto fck 40 MPa em toda a supraestrutura é decisão estrutural significativa — torre alta (34 pavimentos) justifica concreto de maior resistência para reduzir seções de pilares e aumentar área útil.

#### Índices Estimados

> ⚠️ **Dados quantitativos detalhados não disponíveis no executivo analisado.** Índices estruturais (m³ concreto/AC, kg aço/m³, m² forma/AC) não puderam ser extraídos.

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> ⚠️ **Levantamento quantitativo detalhado não disponível.** Não foi possível extrair índices m²/m² AC ou m/m² AC para alvenaria, revestimentos, pisos, etc.

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Elétricas | 1.615.635,52 | 124,28 | 41,4% | N/D |
| Hidrossanitárias | 1.855.978,90 | 142,77 | 47,6% | N/D |
| Preventivas + GLP | 429.419,00 | 33,03 | 11,0% | N/D |
| **TOTAL** | **3.901.033,42** | **300,08** | **100%** | **N/D** |

**Nota:** MO não separada por disciplina no executivo.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

> ⚠️ **PUs detalhados e MO por serviço não disponíveis.** Executivo traz valores globais por macrogrupo sem discriminação item a item.

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

> ⚠️ **Detalhamento não disponível.** Total Esquadrias: R$ 2.766.657,42 (R$ 212,82/m²). Padrão alto — acabamento laqueado mencionado no briefing.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevadores (social + serviço) | 3 | ~505.000 | 1.515.000,00 (categoria completa) |
| Escada pressurizada | incluído | — | (embutido em Sist. Especiais) |
| Equipamentos piscina aquecida | incluído | — | (embutido em Sist. Especiais) |

**Nota:** Categoria Sistemas Especiais R$ 1.515.000 inclui 2 elevadores sociais + 1 elevador de serviço + escada pressurizada + equipamentos piscina aquecida.

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Item | Valor (R$) |
|---|---|
| Projetos | 182.000 |
| Estudos | 46.000 |
| Consultorias | 177.000 |
| Ensaios | 30.000 |
| **TOTAL PROJETOS + CONSULTORIAS** | **435.000** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) |
|---|---|
| Taxas (alvará, licenças, etc.) | 131.000 |

### 10.3 Equipe Administrativa

> ⚠️ **Detalhamento de cargos e salários não disponível.** Total UC2 Ger. Administrativo: R$ 3.230.610.

**Estimativas baseadas em prazo 46 meses:**
- Engenheiro Civil: ~R$ 8.000/mês
- Mestre de obras: ~R$ 9.350/mês

### 10.4 Proteção Coletiva (EPCs)

| Item | Valor (R$) |
|---|---|
| SMS (Segurança Medicina do Trabalho) | 223.000 |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Período | Total (R$) |
|---|---|---|---|
| **Grua** | **AQUISIÇÃO** | **46 meses** | **410.000 (compra) + 26.000 (manutenção)** |
| Elevador cremalheira | Locação + manutenção | 46 meses | 121.000 |
| Plataforma | Locação | 46 meses | 87.000 |

**DESTAQUE:** Aquisição de grua (R$ 410k) — decisão atípica. Maioria dos projetos loca. Indica expectativa de uso intenso + possível reuso em obras futuras.

### 10.6 Ensaios Tecnológicos

| Item | Valor (R$) |
|---|---|
| Ensaios | 30.000 |

### 10.7 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Ger. Técnico (projetos, estudos, consultorias, ensaios, taxas) | 567.350 | 43,64 | 14,9% | 1,72% |
| Ger. Administrativo (SMS, ADM/Canteiro, Equipamentos) | 3.230.610 | 248,51 | 85,1% | 9,81% |
| **TOTAL CI (UC2)** | **3.797.960** | **292,15** | **100%** | **11,54%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

> ⚠️ **Não separado — R$ 0 no macrogrupo.** Louças e metais embutidos em Acabamentos ou Complementares.

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 283 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 715.497/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 1,35 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 1,20 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 55,04 R$/m²/mês | 80,5 | 100,8 |

**Nota:** Prazo de 46 meses é o **mais longo da base de calibração** — reflexo da complexidade (34 pavimentos, torre alta).

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

> ⚠️ **Detalhamento não disponível.** Total: R$ 415.350,45 (R$ 31,95/m²).

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² |
|---|---|---|
| Cobertura | 167.055,60 | 12,85 |
| Serviços Complementares (ambientação, comunicação visual, paisagismo, limpeza final, etc.) | 1.955.217,19 | 150,40 |
| **TOTAL COMPLEMENTARES** | **2.122.272,79** | **163,25** |

---

## SEÇÃO 15 — DESTAQUES E ALERTAS

### 🔵 TORRE ALTA — 34 PAVIMENTOS (RECORDE DA BASE)

- **Mais alto em número de pavimentos** de todos os projetos calibrados
- 3 subsolos + 28 andares residenciais + lazer + telhado
- Prazo 46 meses (mais longo da base)
- Concreto fck 40 MPa em **TODA** a supraestrutura (decisão estrutural para torre alta)
- Escada pressurizada (exigência normativa edifício alto)

### 🔴 ALERTAS — CUSTOS ALTOS

- **Supraestrutura R$ 668/m² e 26,4%** → ALTO (torre alta = muito concreto por m²)
  - Normalizado: R$ 893/m² → **RECORDE da base de calibração**
  - Torres altas têm consumo estrutural por m² maior (pilares reforçados, lajes nervuradas pesadas)
  
- **Esquadrias R$ 213/m²** — acabamento laqueado, padrão alto
  
- **Instalações R$ 300/m²** — instalações pesadas (torre alta = prumadas longas, pressurização, automação)
  
- **Gerenciamento R$ 292/m² (11,54%)** — equipe gestão 46 meses (engenheiro ~R$ 8k/mês, mestre ~R$ 9,35k/mês)
  - Normalizado: R$ 390/m²
  
- **Grua AQUISIÇÃO R$ 410k + manutenção R$ 26k** — decisão atípica (maioria loca)

### ✅ DENTRO DA FAIXA / BAIXO

- **Alvenaria R$ 85/m²** — LOW (vedação simples, não estrutural)
  
- **Climatização R$ 38/m²** — moderado
  
- **Impermeabilização R$ 32/m²** — LOW
  
- **Louças e Metais: R$ 0** (não separado — embutido em acabamentos/complementares)
  
- **Imprevistos: R$ 0** (não incluído)

### ⚠️ DATA BASE JUL/2020 — PROJETO MAIS ANTIGO DA BASE

- CUB/SC Jul/2020 ≈ **R$ 2.061** (estimado por interpolação entre Dez/19 R$ 1.969 e Dez/20 R$ 2.127)
- **Fator de normalização 1,336** (o maior da base — diferença temporal significativa)
- **Custos nominais não comparáveis diretamente com projetos 2023-2024** — sempre usar valores normalizados

### 📝 PARTICULARIDADES

- **AC ESTIMADO ~13.000 m²** (não há AC explícito no executivo)
  - Metodologia: soma de lajes por pavimento → ~12.960 m² → arredondado 13.000 m²
  - Validação cruzada: ~211 m²/andar acabado + ~90 m² circulação = ~300 m²/andar ✓
  - Validação R$/m²: ~R$ 2.532 → CUB ratio 1,23 → compatível com padrão alto Itajaí ✓

- **Layout complexo:**
  - 26 pavimentos tipo (~300 m²/andar)
  - 1 tipo diferenciado (laje 591 m²)
  - 1 duplex (inferior 250 m² + superior 189 m² = 440 m²)

- **3 elevadores** (2 social + 1 serviço) — adequado para torre alta

- **Piscina aquecida** — custo embutido em Sistemas Especiais

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 32.912.870 | R$ |
| **R$/m²** | 2.532 | R$/m² |
| **CUB ratio** | 1,23 | CUB |
| **R$/UR** | R$ 598.416 | R$/UR |
| **AC/UR** | 236,4 | m²/un |
| Concreto supra / AC | N/D | m³/m² |
| Taxa aço supra | N/D | kg/m³ |
| Forma / AC | N/D | m²/m² |
| Alvenaria / AC | N/D | m²/m² |
| Forro / AC | N/D | m²/m² |
| Pintura parede / AC | N/D | m²/m² |
| Fachada / AC | N/D | m²/m² |
| Portas / UR | N/D | un/UR |
| Estacas / AC | N/D | m/m² |
| MO instalações / AC | N/D | R$/m² |
| Elevador | ~R$ 505.000 | R$/un |
| Ritmo construção | 283 | m²/mês |
| Burn rate | R$ 715.497 | R$/mês |

---

> **Fonte:** Mussi Empreendimentos - Velazquez Residence (Executivo Final)
> **Extraído em:** 06/03/2026
> **Notas:** AC estimado por soma de lajes (~13.000 m²). Levantamento quantitativo detalhado não disponível. Louças não separadas (embutido em acabamentos). Data-base jul/2020 (CUB estimado R$ 2.061). Projeto mais antigo e torre mais alta da base de calibração.
