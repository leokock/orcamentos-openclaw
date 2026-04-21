# Gestão — Orçamento Executivo Electra Towers

> **Excel padrão** (38 abas, source of truth): `CTN-TZN_ELT - Orçamento Executivo_R00 .xlsx`
> **Excel de trabalho (Leo)**: `CTN-TZN_ELT - Orçamento Executivo_R00_Leo rev01.xlsx`
> **Links**: [[log-execucao]] · [[PROJETO]] · [[README]] · [[COMECE-AQUI]]

> **Nav**: [Estratégia](#estrategia) · [Checklist Master](#checklist) · [Detalhes](#detalhes) · [Dúvidas abertas](#duvidas) · [Próximos passos](#proximos) · [Histórico resolvidas](#historico)

---



# Estratégia de preenchimento

3 fontes de dados. Fluxo: **Visus (BIM) + Planilhas externas (IA) + Índices → Excel padrão → reimporta no Visus**.


| Fonte                 | O que                                                                           | Como                                      |
| --------------------- | ------------------------------------------------------------------------------- | ----------------------------------------- |
| **BIM** `BIM`         | Arquitetura, acabamentos, revestimentos, esquadrias, fachada, impermeabilização | Leo extrai do modelo no Visus             |
| **Planilha IA** `PLN` | Instalações (hidro, elétrico, telecom, PCI, estrutura, HVAC)                    | Quantitativos extraídos de IFC/DWG via IA |
| **Índices** `IDX`     | Ger. Tec/Adm, canteiro, controle tecnológico, EPCs, equipamentos especiais      | Médias de executivos Cartesian            |


---



# Checklist Master — 38 abas do Excel padrão

> Marque `[x]` conforme for preenchendo. Detalhes técnicos (valores, benchmarks, arquivos) na seção [Detalhes](#detalhes).
> Legenda: `BIM` = Visus (Leo) · `PLN` = Planilha IA · `IDX` = Índice paramétrico

## Estrutura da planilha (abas gerais)

- 1. Ger_Executivo_Manual
- 1. Orçamento (consolidação final — depois de tudo)
- 1. Composições
- 1. Insumos (2)
- 1. CAPA
- 1. PROJETOS (24/mar)
- 1. Ger_Executivo_Cartesian
- 1. EAP
- 1. EAP - app
- 1. CPU — vincular N4 com EAP (manual)
- 1. Insumos — validar preços

## Indiretas / Índices — UC1 consolidada `IDX` ([detalhe ↓](#uc1))

- 1. Ger_Tec e Adm
- 1. EPCs
- 1. CANTEIRO
- 1. Cont.Tecnol.
- 1. PISCINA
- 1. Equipamentos Especiais
- 1. MOBILIÁRIO

> **Total UC1: R$ 10.339.456 (R$ 286,50/m² AC)** — 11/abr

## Serviços Civis — BIM (Leo no Visus)

- 1. ESQUADRIAS `BIM`
- 1. IMPERMEABILIZAÇÃO `BIM` ⚠️ pendência Leo

## Infraestrutura / Fundações / Estrutura `PLN` ([detalhe ↓](#estrutura))

- [x] 1. Estacas (20/abr) — r01 pronto: 423 estacas (17×ø500 + 406×ø600 × 25m) R$ 3,07M
  > `disciplinas/estrutura/estacas-electra-r01.xlsx` | LIBERTÉ 1203-2025-R0 ✓ validado vs CONTROLE-REV projetista
- [x] 1. EAP Fundação (20/abr) — 01.002 + 01.003 preparados, R$ 7,67M total (R$ 212/m² AC) ✅ validado benchmark
  > `disciplinas/estrutura/eap-fundacao-r01.xlsx` | Benchmark 45 projetos: Mov+Infra mediana R$ 245/m² AC — Electra R$ 227/m² (ABAIXO mediana)
- [x] 1. Fund. Rasa | Contenção (detalhe via IFC R26, 20/abr) — 70 IfcFooting processadas (66 baldrames + 4 blocos Pra)
  > `disciplinas/estrutura/fund-rasa-electra-r01-detalhado.xlsx` + `cruzamento-ifc-projetista.xlsx`
  > Descoberta: IFC R26 não modela blocos coroamento/laje fund (modelados como IfcColumn/IfcSlab no IFC)
  > Cruzamento total obra: IFC 15.217 m³ ≈ Projetista 15.598 m³ (Δ 2,4% ✅)
- [x] 1. Resumo Estrutura (20/abr parcial) — consolidado projetista 1203 completo
  > `disciplinas/estrutura/projetista-1203-consolidado.xlsx` (5 abas: Resumo + Supra A/B + Aço bitola + Fund. Rasa)
- [ ] 1. Cálculo de apoio
- [ ] 1. Escoramento

### Dúvidas fundação pra validar com Rubens Alves (projetista)
- Sistema de fundação diferente entre torres? (Bloco A = laje maciça/radier; Bloco B = zapatas + blocos coroamento)
- Breakdown "L1 Blocos" CONTROLE-REV = 2.066 m³ inclui baldrame + laje fund? (dif 293 m³ vs QUANT Blocos coroamento isolados)
- Discrepância resumo QUANT-A r245 HÉLICE 2.200 m³ vs real 3.544 m³ (+20%)? (parece desatualização, usar CR detalhado)

### Pendente cotação formal
- LIBERTÉ cotação turnkey vs separada (PUs atuais são estimativa mercado SC R$ 290/m turnkey decomposto proporcional)

## Acabamentos `PLN`

- 1. LOUÇAS E METAIS (24/mar) — IFC Arq R07/R08, T.A + T.B
  > `disciplinas/loucas-metais/loucas-metais-electra-TA-TB-r00.xlsx`

## Hidrossanitário + MO + Bombas + Gás — CON 07 `PLN` ([detalhe ↓](#hidro))

- 1. HIDROSSANITÁRIO — R$ 4,81M / R$ 133,36/m²
- 1. MÃO DE OBRA HIDRO — incluído no CON 07
- 1. Bombeamento - Extra — incluído no CON 07
- 1. GÁS — incluído no CON 07 (ver [dúvida](#duvidas-hidro))

## Elétrico / Telecom `PLN` ([detalhe ↓](#eletrico))

- 1. ELÉTRICO — R03 suplemento (14/abr), R$ 1,33M rastreáveis (pendências R02 abertas)
- 1. MÃO DE OBRA ELETRICA — decidir faixa (base R$ 26/m² vs R02 R$ 170/m²)
- 1. TELECOMUNICAÇÃO (2) — R02 + R03, R$ 463.012 / R$ 12,83/m²
- 1. AUTOMAÇÃO
- 1. ILUMINAÇÃO — decidir se separa do Elétrico

## PCI — CON 08 `PLN` ([detalhe ↓](#pci))

- 1. PPCI — R$ 774.546 / R$ 21,46/m² (SPDA R01 + hidrantes + extintores + alarme + bombas + MO)
- 1. SPRINKLERS — NÃO TEM (Leo confirmou 11/abr, aba zerada)

## Climatização `PLN` ([detalhe ↓](#climatizacao))

- 1. CLIMATIZAÇÃO — R$ 2.772.160 (AC R$ 2,0M + Ventilação R$ 471k + Exaustão R$ 300k)

---



# Detalhes técnicos por disciplina



## Movimentação de Terra `PLN` (11/abr)

> Destino no Excel: **linha na EAP** (não tem aba própria). Serviços preliminares + mov terra.

- Locação da obra — R$ 40.000 (4.000m² × R$ 10/m²)
- Limpeza camada vegetal — R$ 14.000 (4.000m² × R$ 3,50/m²)
- Remoção entulhos — R$ 15.000 vb (sem demolição)
- MO Canteiro — R$ 25.000 vb
- MO movimentação de terra — R$ 335.000 vb (escav + bota-fora + reaterro + lastro + mob + arrasamento)
- Rebaixamento lençol — R$ 95.000 vb (mediana 17 projetos Cartesian)

> **Total: R$ 524.000 (R$ 14,52/m² AC)**. Benchmark: P25 = R$ 14,09, Med = R$ 22,97. Base: 32 projetos.



## Fundações / Estrutura `PLN`

- **Estacas**: R00 tinha dados parciais (Torre 1: ø50cm 17un + ø60cm 406un)
- **Fundação Rasa / Contenção**: pendente
- **Resumo Estrutura**: briefing R00 feito. IFC R26 processado: ~12.784 m³ concreto, 1.531 pilares, 3.531 vigas
- **Escoramento**: pendente



## Hidrossanitário — CON 07 completa (11/abr) `PLN`

> Planilha externa: `disciplinas/hidraulico/hidro-electra-r01.xlsx`
> Sanitário (referência cruzada): `disciplinas/sanitario/sanitario-electra-r01.xlsx`


| Item                   | Valor        | R$/m²    | Fonte                                  |
| ---------------------- | ------------ | -------- | -------------------------------------- |
| Água fria (R01)        | R$ 392.586   | R$ 10,88 | IFC H00 + PUs Belle Ville, item a item |
| Esgoto + pluviais      | R$ 749.565   | R$ 20,77 | Benchmark med. 24 proj                 |
| MO hidro               | R$ 1.984.887 | R$ 55,00 | Benchmark med. 23 proj                 |
| Bombas / pressurização | R$ 541.333   | R$ 15,00 | Abaixo P25, sem subsolo                |
| Gás                    | R$ 449.667   | R$ 12,46 | Benchmark med. 24 proj                 |
| Aquecimento            | R$ 457.968   | R$ 12,69 | Benchmark med. 22 proj                 |
| Reservatórios          | R$ 95.275    | R$ 2,64  | Benchmark med. 19 proj                 |
| Hidrômetros            | R$ 71.456    | R$ 1,98  | Benchmark med. 10 proj                 |
| Drenagem               | R$ 70.012    | R$ 1,94  | Benchmark med. 9 proj                  |


> **Total CON 07: R$ 4.812.748 (R$ 133,36/m² AC)**. Base: 35 projetos. Mediana base: R$ 125,88.
> ⚠️ Gás + aquecimento (R$ 907k) incluídos aqui. Se preencher abas GÁS/CLIMATIZAÇÃO separadas, descontar.
> ⚠️ Sanitário já incluído no esgoto+pluviais (R$ 749.565 = mediana R$ 20,77/m²). Alternativa aba separada: R$ 879.177 (R$ 24,50/m²) — descontar do CON 07.



## Elétrico `PLN`

> R03 suplemento (14/abr): `disciplinas/eletrico/eletrico-electra-r03.xlsx` (5 abas: RESUMO, QUADROS PRINCIPAIS, CAIXAS PASSAGEM, MATERIAL INTERNO CD, DISJUNTORES 18 CDs)
> Relatório: `quantitativos/listas-materiais/COMPARACAO-PDFS-BASE-2026-04-14.md`
> ⚠️ **R03 NÃO SOMA ao R02** — substitui itens "vermelhos" (sem fonte) do R02 pelos itens rastreáveis PDF.

- 5 PDFs Eletrowatts processados, 384 itens rastreáveis: **R$ 1.328.826**
  - 16 quadros principais (QGBT, QM, BEP, banco capacitores): R$ 623.600 (0 fallback)
  - 162 caixas de passagem (exec + prev): R$ 129.045 — 89 fallback amarelo (⚠️ verificar diagrama)
  - 39 itens material interno CD apto tipo (barramentos, cabos, terminais): R$ 79.133 (5 fallback)
  - 167 disjuntores / IDRs / DPS em 18 CDs: R$ 497.048 (9 fallback)

**Pendências R02 NÃO cobertas pelos PDFs** (ver também [dúvidas](#duvidas-eletrico)):

- Definir comprimento médio por trecho de eletroduto — IFC não tem Length. 2m? 3m? 4m? (impacto ±R$ 1M)
- Definir fator cabos vs eletrodutos — 1:1? 1,2x? 1,5x?
- Validar: subestação, gerador e barramento compartilhados entre torres?
- MO elétrica: mediana base R$ 26/m², R02 tinha R$ 170/m² — qual faixa?
- Cabos de força: metragem
- Luminárias: PU
- PU médio dos 89 fallback amarelo em CAIXAS PASSAGEM (ou processar DWGs)



## Telecomunicação `PLN`

- **R02 (30/mar)** — IFC + 18 DWGs, 312 pontos ativos
  > `disciplinas/telefonico/telecomunicacoes-electra-r02.xlsx`
- **R03 suplemento (14/abr)** — 28 caixas de passagem tronco via PDF: +R$ 39.012
  > `disciplinas/telefonico/telecomunicacoes-electra-r03.xlsx`

> **Total consolidado R03: R$ 463.012 (R$ 12,83/m²)**

## PCI / Segurança — CON 08 (11/abr) `PLN`


| Item                     | Valor      | R$/m²   | Fonte                                   |
| ------------------------ | ---------- | ------- | --------------------------------------- |
| Hidrantes                | R$ 130.641 | R$ 3,62 | Med. 11 proj + 67 abrigos IFC           |
| Extintores + sinalização | R$ 68.930  | R$ 1,91 | 145 extintores + 140 placas IFC         |
| **SPDA R01** (14/abr) ★  | R$ 185.092 | R$ 5,13 | Primeiro XLSX formal, 28 itens NBR 5419 |
| Alarme / detecção        | R$ 89.500  | R$ 2,48 | Med. 8 proj                             |
| Bombas PCI               | R$ 119.454 | R$ 3,31 | Med. 12 proj                            |
| MO PPCI                  | R$ 180.444 | R$ 5,00 | Estimativa conservadora                 |
| Sprinklers               | —          | —       | **NÃO TEM** (Leo confirmou 11/abr)      |


> **Total CON 08: R$ 774.546 (R$ 21,46/m² AC)**. Base: 40 projetos.
> Benchmark mediana com sprinklers: R$ 31/m². Sem sprinklers: R$ 21/m² coerente.
> SPDA: `disciplinas/spda/spda-electra-r01.xlsx` (aba única, 28 itens, subtotais por subgrupo NBR 5419). Delta vs benchmark mediana 27 proj (R$ 5,14/m²): -0,23% ✅



## Climatização (11/abr) `PLN`

- **Ar-Condicionado** — R$ 2.000.000 (R$ 55,42/m², benchmark 29 proj)
  > `disciplinas/ar-condicionado/ar-condicionado-electra-r01.xlsx`
  > 520 splits estimados + climatização áreas comuns. DWG bloqueado.
- **Ventilação Mecânica** — R$ 471.600 (R$ 13,07/m², benchmark 4 proj + NBR 14880)
  > `disciplinas/ventilacao/ventilacao-electra-r01.xlsx`
  > Escadas pressurizadas. Premissas não validadas — solicitar DXF Rubens Alves.
- **Exaustão** — R$ 300.560 (R$ 8,33/m², estimativa paramétrica)
  > `disciplinas/exaustao/exaustao-electra-r01.xlsx`
  > 348 banheiros + 48 churrasqueiras + áreas comuns. Benchmark contaminado (keywords).

> **Total Climatização: R$ 2.772.160**



## UC1 Despesas Indiretas — consolidado (11/abr) `IDX`

> `disciplinas/indices/indices-electra-r01.xlsx`
> Benchmark base Cartesian + ajustes conservadores (medianas têm ruído)

Breakdown: Estudos + projetos R$ 1,26M · Taxas R$ 541k · Segurança + EPCs R$ 253k · Gestão + equipe 36m R$ 4,33M · Canteiro operacional R$ 180k · Consumo + manut 36m R$ 650k · Instalações provisórias R$ 433k · Controle tec R$ 433k · Equip. Especiais R$ 902k · Mobiliário R$ 126k · Paisagismo R$ 108k · Piscina R$ 541k · Limpeza final R$ 577k.

> **Total: R$ 10.339.456 (R$ 286,50/m²)**

---



# Dúvidas abertas

> Quando resolver, move pra [Histórico](#historico) com a resposta.

## Movimentação de Terra

- Qual a área do terreno? (11/04) — estimada em 4.000m², afeta locação + limpeza vegetal
- Sondagem confirma profundidade do lençol freático? (11/04) — se > 3m, rebaixamento pode ser reduzido/eliminado
- Quantidade de estacas Torre 2? (11/04) — estimada igual Torre 1 (~200un), afeta custo de arrasamento

## Impermeabilização

- Vai ter tratamento de contrapiso no peitoril ou só impermeabilização? (03/04)

## Pisos / Revestimentos

- Verificar onde vão as soleiras — Pisos ou Revestimentos? (10/04)
- Mão de obra para rodapé (porcelanato + poliestireno)
- Ver sobre rodapé de pintura
- Piso vinílico: composição



## Hidrossanitário

- Gás e aquecimento já incluídos na CON 07 (R$ 907k). Descontar se preencher abas GÁS/CLIMATIZAÇÃO separado (11/04)
- Sanitário: JSON bruto corrompido. Reprocessar IFC sanitário (11/04)
- Verificar se quantidades do IFC hidro estão em mm ou m (assumido mm, convertido na R01) (11/04)



## Elétrico — pendências R02 (ver [detalhe](#eletrico))

- Comprimento médio por trecho de eletroduto (2m? 3m? 4m?) — impacto ±R$ 1M
- Fator cabos vs eletrodutos (1:1? 1,2x? 1,5x?)
- Subestação / gerador / barramento: compartilhados entre torres?
- MO elétrica: mediana base R$ 26/m² vs R02 R$ 170/m² — qual faixa?
- Cabos de força: metragem
- Luminárias: PU
- PU médio dos 89 fallback amarelo (CAIXAS PASSAGEM)

## PCI

- Metragem real tubulação FG hidrantes — IFC deu 67m (subestimado pra 34 pav). Precisa DWG ou memorial (11/04)
- Reservatórios e bombas PCI: especificação (não modelados no IFC) (11/04)

## Esquadrias

- Qual a unidade de contramarco? un ou m²
- verificar a composição do brise (está m2 na composição e linear na extração)

## Pintura

- Adicionar composição massa PVA em teto
- Ajustar posição da fachada porque os itens estão no final no Visus

## Fachada

- Composição de material de reboco externo

## Geral / EAP

- Criar a lógica de exportar composição do Visus e insumos e colocar na planilha Excel

---



# Próximos passos

## Visus (BIM — Leo)

- Impermeabilização — extrair do modelo
- Esquadrias — extrair do modelo
- Paredes e painéis
- Revestimentos argamassados (internos de parede + piso)
- Acabamentos internos (parede, teto, piso)
- Sistemas de pintura interna
- Revestimentos e acabamentos em fachada

## Passar planilhas externas pro Excel padrão

- Hidro R01 → aba HIDROSSANITÁRIO (item a item, PUs Belle Ville)
- Sanitário R01 → já incluído no CON 07 (referência cruzada)
- SPDA R01 → aba PPCI (subseção SPDA, 28 itens NBR 5419)
- Elétrico R03 → aba ELÉTRICO (384 itens rastreáveis dos PDFs Eletrowatts)
- Telecom R03 → aba TELECOMUNICAÇÃO (2) (+28 caixas de passagem tronco)
- Ar-condicionado R01 → aba CLIMATIZAÇÃO (subseção AC)
- Ventilação R01 → aba CLIMATIZAÇÃO (subseção VM)
- Exaustão R01 → aba CLIMATIZAÇÃO (subseção Exaustão)
- Louças e Metais R00 → aba LOUÇAS E METAIS
- Índices UC1 R01 → abas Ger_Tec e Adm, CANTEIRO, EPCs, Cont.Tecnol., Equipamentos Especiais, PISCINA, MOBILIÁRIO
- Movimentação de Terra → linha na EAP (serviços preliminares)

---



# Histórico — Dúvidas resolvidas

- **Sprinklers**: NÃO TEM (11/04) — Leo confirmou, manter aba SPRINKLERS zerada
- **Composição rodapé porcelanato 10cm** (10/04) — criada
- **Verificação da fachada no Visus** — critério criado
- **Fachada esquerda** — feita
- **Fachada frontal** — feita
- **Fachada fundos** — feita



---

*Atualizado: 17/04/2026 (reorganização: Checklist Master source-of-truth + Detalhes + Dúvidas limpas)*