# Índices de Orçamento Executivo — ARV Ingleses Spot

> Projeto: ARV Ingleses Spot (ARV Empreendimentos / ARV Investimentos)
> Revisão: R02
> Criado: 05/03/2026
> Referências: Kirchner (KIR), Adore Level UP (ADR), Amalfi Maiori (AMI), Amalfi Marine (AMN), Be Brave Meraki (BBM)

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Ingleses Spot | — |
| Código CTN | — | N/D | — |
| Revisão | — | R02 | — |
| Localização | — | Florianópolis/SC — Ingleses | — |
| Endereço | — | Rua dos Lordes, 267 — Ingleses — CEP 88058-525 | — |
| Incorporador/Cliente | — | ARV Empreendimentos (ARV Investimentos) | — |
| Área do Terreno | AT | 908,40 | m² |
| Área Construída | AC | 2.618,24 | m² |
| Unid. Habitacionais | UR_H | 49 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | N/D | un |
| Total Unidades | UR | 49 | un |
| Nº Total Pavimentos | NP | 4 (Térreo + 3 Tipo) | un |
| Nº Pavimentos Tipo | NPT | 3 (2º, 3º, 4º) | un |
| Nº Pav. Garagem | NPG | 0 | un |
| Elevadores | ELEV | N/D (provavelmente 1) | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 26 | meses |
| Data-base | — | Jul/2024 (versão 3, Sienge) | — |
| CUB Referência | — | R$ 2.841,51 (Set/2024 SC) | R$ |
| R$/m² Total | — | 5.333,75 | R$/m² |
| CUB ratio | — | 1,88 | CUB |
| Tipo de Laje | — | Protendida (treliçada no térreo, protensão nos demais) | — |
| Tipo de Fundação | — | Hélice Contínua (ø40, ø50, ø60 cm) | — |
| Padrão Acabamento | — | Médio-Alto | — |

**Nota sobre totais:** Planilha (Aba Obra) totaliza R$ 13.965.042,59. O PDF Sienge mostra R$ 13.772.402,04 (UC1 R$ 5.168.002,20 + UC2 R$ 8.604.399,84). Diferença de R$ 192.640,55 (~1,4%). Usamos o total da planilha (R$ 13.965.042,59) como referência principal.

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | **2,88** | 13,94 | 3,48 |
| Área por Unidade | AC / UR | **53,4** m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | **0,054** un/m² | 0,06 | 0,04 |

> **Destaque:** AC/UR = 53,4 m² é o **MENOR** da base — unidades muito compactas (estúdios ou 1-2 dormitórios). Comparar com AMN 98,6 m²/un, ADR 78,7, KIR 243,7.

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | ~49 (se 1 elev.) | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | ~0,25 (se 1 elev.) | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | 49 | 100% | ~53,4 |
| Comercial | 0 | 0% | — |
| Estúdio | N/D | N/D | N/D |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | 684,87 | 26,2% |
| 2º Pvto (Tipo) | 471,39 | 18,0% |
| 3º Pvto (Tipo) | 471,39 | 18,0% |
| 4º Pvto (Tipo) | 471,39 | 18,0% |
| Terraço/Lazer | 471,40 | 18,0% |
| Barrilete/Casa Máquinas | 23,90 | 0,9% |
| Reservatório | 23,90 | 0,9% |

> **Nota:** Térreo responde por 26,2% da AC — área significativa, provavelmente estacionamento + áreas comuns + lojas/serviços.

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | **R$ 285.001** |
| R$ / UR (habitacionais) | Total / UR_H | R$ 285.001 |
| CUB / UR | (R$/UR) / CUB | **100,3 CUB** |

> **Destaque:** R$ 285k/UR é alto em CUB/UR (100,3) — efeito de obra compacta com custos fixos que não escalam linearmente com o número de unidades.

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Mapeamento da planilha (20 macrogrupos) para os 18 macrogrupos padrão da base Cartesian.

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Base (21 proj) |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin¹ | 5.168.001,00 | 1.973,85 | 37,01% | 307 - 1.984 |
| 2 | Movimentação de Terra | 104.321,83 | 39,84 | 0,75% | 7 - 173 |
| 3 | Infraestrutura | 329.268,72 | 125,76 | 2,36% | 115 - 344 |
| 4 | Supraestrutura | 2.263.218,31 | 864,40 | 16,21% | 484 - 1.902 |
| 5 | Alvenaria (Paredes e Painéis) | 467.154,28 | 178,42 | 3,35% | 114 - 324 |
| 6 | Impermeabilização | 163.493,18 | 62,44 | 1,17% | 43 - 94 |
| 7 | Instalações (Elét+Hidro+Prev+Com) | 1.089.602,12 | 416,16 | 7,80% | 281 - 555 |
| 8 | Sistemas Especiais (~60%)² | 197.971,29 | 75,61 | 1,42% | 89 - 748 |
| 9 | Climatização (~40%)² | 131.980,86 | 50,41 | 0,95% | 25 - 210 |
| 10 | Rev. Internos Parede (Rev. Argamassa)³ | 762.054,90 | 291,06 | 5,46% | 107 - 425 |
| 11 | Teto (Forros) | 220.072,85 | 84,05 | 1,58% | 42 - 151 |
| 12 | Pisos (Rev. Cerâmicos) | 393.463,58 | 150,28 | 2,82% | 133 - 534 |
| 13 | Pintura | 451.458,26 | 172,43 | 3,23% | 95 - 187 |
| 14 | Esquadrias | 1.232.074,96 | 470,57 | 8,82% | 237 - 991 |
| 15 | Louças e Metais | 99.969,06 | 38,18 | 0,72% | 23 - 51 |
| 16 | Fachada | N/D⁴ | N/D | N/D | 123 - 546 |
| 17 | Complementares⁵ | 684.557,47 | 261,47 | 4,90% | 49 - 553 |
| 18 | Imprevistos | 206.379,94 | 78,82 | 1,48% | 41 - 174 |
| — | **TOTAL** | **13.965.042,59** | **5.333,75** | **100%** | — |

**Notas de mapeamento:**

¹ **Gerenciamento inclui:** Terreno (R$ 1.806.000), Desp. Administrativas (R$ 2.098.044), Custos Indiretos (R$ 1.031.001), Instalações Provisórias (R$ 177.917), Equipamentos (R$ 55.040). Corresponde à UC1 do PDF Sienge (R$ 5.168.002,20). O valor é inflacionado pelo custo de terreno — sem terreno, gerenciamento seria R$ 3.362.001 = R$ 1.284/m² (22,4%), mais alinhado com a base.

² **Climatização, Equip e Sist Especiais** (R$ 329.952,15) — separado em estimativa 40/60 por falta de breakdown detalhado na planilha.

³ **Revestimentos de Argamassa** inclui tanto revest. internos quanto fachada — sem dado separado disponível na planilha.

⁴ **Fachada:** Não segregada como macrogrupo na planilha — está dentro de "Revestimentos de Argamassa".

⁵ **Complementares** agrupa: Rev. Complementares (R$ 243.250,90) + Mobiliário/Paisagismo/Decoração (R$ 220.000,00) + Limpeza (R$ 86.974,94) + Ligações Definitivas (R$ 65.000,00) + Cobertura (R$ 69.331,63).

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto (por pavimento)

| Pavimento | Volume (m³) | fck | Tipo Laje |
|---|---|---|---|
| Térreo | 9,36 | N/D | Treliçada (153 m²) |
| 2º Pvto | 118,67 | 35 MPa | Protendida |
| 3º Pvto | 106,76 | 35 MPa | Protendida |
| 4º Pvto | 106,68 | 35 MPa | Protendida |
| Terraço | 151,33 | 35 MPa | Protendida |
| **TOTAL** | **492,80** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR | Ref. AMN |
|---|---|---|---|---|---|
| Consumo concreto / AC | **0,188** | m³/m² | 0,242 | 0,189 | 0,253 |

> **Nota:** Concreto/AC = 0,188 — alinhado com ADR (0,189) e abaixo de KIR (0,242) e AMN (0,253). Coerente com protensão + obra de 4 pavimentos.

#### Armadura — Protensão

| Pavimento | Protensão (kg) |
|---|---|
| 2º Pvto | 1.369,46 |
| 3º Pvto | 1.453,46 |
| 4º Pvto | 1.453,46 |
| Terraço | 1.382,17 |
| **TOTAL** | **5.658,55** |

| Índice | Valor | Un |
|---|---|---|
| Protensão total | 5.658,55 | kg |
| Protensão / m³ concreto (excl. Térreo) | 11,70 | kg/m³ |
| Protensão / m² AC | 2,16 | kg/m² |

> Aço convencional (CA-50/CA-60) da supraestrutura não foi quantificado globalmente na planilha — dados parciais do 2º Pvto mostram CA-50 em metragens lineares, não peso total.

#### Forma (dados do Ger_Executivo)

| Pavimento | Forma (m²) | Laje Treliçada (m²) |
|---|---|---|
| Térreo | 450,24 | 153,00 |
| 2º Pvto | 692,68 | — |
| 3º Pvto | 658,34 | — |
| 4º Pvto | 657,62 | — |
| Terraço+Lazer | 1.300,99 | — |
| Barrilete | 730,48 | — |
| Fundo Reserv. | 91,06 | — |
| Teto Reserv. | 201,53 | 72,16 |
| **TOTAL** | **4.782,94** | **225,16** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR | Ref. AMI |
|---|---|---|---|---|---|
| Forma / AC | **1,83** | m²/m² | 1,25 | 1,36 | 1,30 |

> **Destaque:** Forma/AC = 1,83 é **ALTO** — 33% acima de ADR (1,36) e 47% acima de KIR (1,25). Explicado pela escala pequena da obra (2.618 m²) com barrilete e reservatório que somam áreas de forma desproporcionais.

**Preços unitários forma:**
- Material forma: R$ 42,80/m²
- MO montagem/desmontagem: R$ 4,86/m²
- Escoramento: R$ 99,26/m²
- Laje treliçada: R$ 124,67/m²

**Escoramento total:** ~2.008 m² (471,39 × 3 tipo + 471,40 terraço + 23,90 × 3 barrilete/reserv.)

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | PU (R$) |
|---|---|---|---|
| Tipo de laje (tipo) | Protendida | 3 pavimentos | — |
| Tipo de laje (embasamento) | Treliçada | 153 m² (térreo) | 124,67/m² |
| Escoramento | Convencional | ~2.008 m² | 99,26/m² |
| Forma (material) | — | 4.783 m² | 42,80/m² |
| Forma (MO montagem) | — | 4.783 m² | 4,86/m² |

#### MO Supraestrutura

| Item | Área (m²) | PU MO (R$/m²) | Obs |
|---|---|---|---|
| MO tipo | N/D | N/D | Dados não disponíveis como PU único |
| MO embasamento | N/D | N/D | — |

### 4.2 Infraestrutura

#### Fundação Profunda (Hélice Contínua)

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | HC | — | — | Hélice Contínua |
| Estaca ø40cm | 126 | m | N/D | 7 un × 18 m |
| Estaca ø50cm | 504 | m | N/D | 28 un × 18 m |
| Estaca ø60cm | 90 | m | N/D | 5 un × 18 m |
| **Total estacas** | **720** | **m** | — | **40 un** |
| Concreto fck 30 | 140,24 | m³ | N/D | Inclui 30% perda |
| Aço fundação profunda | 2.756 | kg | N/D | CA-50 |
| Taxa aço fundação prof. | 19,65 | kg/m³ | — | — |
| Escavação estacas | 140,24 | m³ | — | — |
| Bota-fora estacas | 182,31 | m³ | — | — |

**Detalhamento aço fund. profunda (CA-50):**
- ø6,3 = 452 kg
- ø10 = 23 kg
- ø12,5 = 284 kg
- ø16 = 1.997 kg

**MO fundação profunda:** R$ 90.316,66
- Apoio: R$ 19.215
- HC ø40: R$ 8.618
- HC ø50: R$ 51.710
- HC ø60: R$ 10.773

| Índice | Valor | Un | Ref. KIR | Ref. ADR | Ref. AMN |
|---|---|---|---|---|---|
| ML estaca / AC | **0,275** | m/m² | 0,39 | 0,19 | 0,28 |
| ML estaca / UR | **14,7** | m/UR | 95,6 | 15,1 | 46,7 |
| Nº estacas / UR | **0,82** | un/UR | 3,3 | 1,3 | 2,3 |

> **Nota:** ML estaca/AC = 0,275 — muito próximo do AMN (0,28). Nº estacas/UR muito baixo (0,82) reflete a alta densidade de unidades por estaca.

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|---|
| Forma (blocos+baldrames) | 683,65 | m² | 18,29/m² |
| Concreto fck 35 | 80,14 | m³ | 175,28/m³ |
| Aço | 6.516 | kg | N/D |
| Taxa aço fund. rasa | 81,31 | kg/m³ | — |
| MO fund. rasa | — | vb | R$ 25.660,26 |

**Detalhamento aço fund. rasa:**
- CA-60: ø5 = 195,6 kg
- CA-50: ø6,3 = 220,7 kg, ø8 = 2.686 kg, ø10 = 654 kg, ø12,5 = 643,8 kg, ø16 = 342,8 kg, ø20 = 1.773,1 kg

> **Taxa aço fund. rasa = 81,31 kg/m³** — alinhada com KIR (81,96 kg/m³) e ADR (81,00 kg/m³). Consistente com a base.

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR | Ref. AMN |
|---|---|---|---|---|---|
| Alvenaria total | 3.882,70 | **1,48** | 1,37 | 1,56 | 1,33 |
| Chapisco interno | N/D | N/D | 2,68 | 2,58 | N/D |
| Reboco/massa interna | N/D | N/D | 2,68 | 2,58 | N/D |
| Forro gesso | N/D | N/D | 0,57 | 0,16 | 0,59 |
| Contrapiso | N/D | N/D | 0,66 | 0,76 | 0,71 |
| Piso cerâmico | N/D | N/D | — | — | N/D |
| Pintura parede | N/D | N/D | 2,34 | 1,05 | 1,31 |
| Pintura teto | N/D | N/D | 0,87 | 0,55 | N/D |
| Fachada total | N/D | N/D | 0,73 | 1,41 | 0,86 |
| Cobertura (telhamento) | N/D | N/D | N/A | 0,07 | N/D |

> **Alvenaria/AC = 1,48** — dentro da faixa (KIR 1,37 a ADR 1,56), mais próximo do AMI/AMN.

### 5.2 Detalhamento Alvenaria por Pavimento

| Pavimento | Cerâmico (m²) | Concreto/Celular (m²) | Total (m²) |
|---|---|---|---|
| Térreo | 412,35 | 73,60 | 485,95 |
| 2º Pvto | 935,35 | 82,52 | 1.017,87 |
| 3º Pvto | 935,35 | 82,52 | 1.017,87 |
| 4º Pvto | 896,93 | 82,35 | 979,28 |
| Terraço | 84,26 | 194,42 | 278,68 |
| Cobertura | 78,36 | — | 78,36 |
| Reservatório | 24,69 | — | 24,69 |
| **TOTAL** | **3.367,29** | **515,41** | **3.882,70** |

**Proporção:** 86,7% cerâmico, 13,3% concreto/celular.

**Espessuras predominantes (cerâmico):**
- 9 cm: ~1.564 m² (46,4%)
- 11,5 cm: ~1.415 m² (42,0%)
- 14 cm: ~318 m² (9,5%)
- 19 cm: ~70 m² (2,1%)

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Bacias sanitárias | 61 | **1,24** | — | 0,4 |
| Registros (acabamentos) | 60 | 1,22 | — | 0,6 |
| Portas (madeira+PCF) | N/D | N/D | 10,7 | 3,2 |

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

> A planilha agrupa todas as instalações em um único macrogrupo ("Instalações Elét, Hidro, Prev, Comunicação"). Breakdown por disciplina **não disponível**.

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | N/D | N/D | N/D | N/D |
| Elétricas | N/D | N/D | N/D | N/D |
| Preventivas | N/D | N/D | N/D | N/D |
| Gás (GLP) | N/D | N/D | N/D | N/D |
| Comunicações/Telecom | N/D | N/D | N/D | N/D |
| **TOTAL** | **1.089.602,12** | **416,16** | **100%** | **N/D** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| MO total instalações / AC | N/D | R$/m² | 69,20 | 122,38 |
| Mat. total instalações / AC | N/D | R$/m² | 171,69 | 265,99 |
| Razão MO/Material | N/D | — | 0,40 | 0,46 |

> **⚠️ Instalações = R$ 416/m²** — **ACIMA** da média da base (R$ 365) e acima do topo da faixa estável (R$ 380 default alto SC). Mais alto que KIR (241), ADR (388/432 c/ clim.), Redentor (367). Pode indicar especificação premium ou efeito de escala pequena na diluição de itens fixos (SPDA, entrada energia, quadros, bombas).

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

> Dados detalhados de PUs por item de acabamento **não disponíveis** na planilha fonte. Apenas totais por macrogrupo.

### 7.1 Revestimentos de Parede (Rev. Argamassa)

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Total Rev. Argamassa | — | — | — | — |
| **Total do macrogrupo** | — | — | — | R$ 762.054,90 (291,06 R$/m²) |

> Inclui interno + fachada (não segregados na planilha).

### 7.2 Pisos (Rev. Cerâmicos)

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Total Rev. Cerâmicos | — | — | — | — |
| **Total do macrogrupo** | — | — | — | R$ 393.463,58 (150,28 R$/m²) |

### 7.3 Teto (Forros)

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Total Forros | — | — | — | — |
| **Total do macrogrupo** | — | — | — | R$ 220.072,85 (84,05 R$/m²) |

### 7.4 Pintura

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Total Pinturas | — | — | — | — |
| **Total do macrogrupo** | — | — | — | R$ 451.458,26 (172,43 R$/m²) |

### 7.5 Fachada

> **Não segregada** como macrogrupo na planilha. Está incluída em "Revestimentos de Argamassa".

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

> Breakdown detalhado por tipo de esquadria **não disponível** na planilha fonte.

| Item | Total (R$) |
|---|---|
| **Total Esquadrias, Vidros e Ferragens** | **R$ 1.232.074,96** |

### 8.2 Índices

| Índice | Valor | Un | Ref. KIR | Ref. ADR | Ref. AMI |
|---|---|---|---|---|---|
| Esquadrias / AC | **470,57** | R$/m² | 211,11 | 344,23 | 334,10 |
| Esquadrias / UR | **25.144** | R$/UR | 51.445 | 27.106 | 46.587 |

> **⚠️ Esquadrias = R$ 470,57/m²** — **ACIMA** da maioria dos projetos da base. Acima de KIR (211), ADR (344), AMI (334), AMN (237). Comparável ao Redentor (518). Pode indicar esquadrias de padrão elevado ou guarda-corpo/brise em proporção alta.

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

> Macrogrupo "Climatização, Equip e Sist Especiais" = R$ 329.952,15. Estimativa de split 40/60 por ausência de breakdown.

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Climatização (~40%) | — | — | ~131.981 |
| Sistemas Especiais (~60%) | — | — | ~197.971 |
| Elevadores | N/D (provav. 1) | N/D | N/D |
| Demais sistemas | — | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR | Ref. AMN |
|---|---|---|---|---|---|
| Sist. Especiais / AC | **75,61** | R$/m² | 96,44 | 179,87 | 171,78 |
| Climatização / AC | **50,41** | R$/m² | 25,16 | 71,61 | N/D |

> Sistemas Especiais R$ 76/m² está **ABAIXO** da base (89-748). Pode indicar escopo reduzido (poucos equipamentos de lazer, sem piscina aquecida, sem solar).

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

> Dados extraídos da UC1 do PDF Sienge (R$ 5.168.002,20).

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Arquitetônico executivo | 149.980 | 57,28 |
| Estrutural | 20.335 | 7,77 |
| Elétrico | 30.969 | 11,83 |
| Hidrossanitário | 26.930 | 10,29 |
| Preventivo | 18.434 | 7,04 |
| Climatização | 10.877 | 4,16 |
| Interiores/ambientação | 36.920 | 14,10 |
| Fundação | 9.645 | 3,68 |
| EIV | 11.500 | 4,39 |
| As Built | 12.000 | 4,58 |
| Piscina | 9.900 | 3,78 |
| **TOTAL PROJETOS** | **337.490** | **128,90** |

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Orçamento e Planejamento | 17.450 | 6,67 |
| Eng/Financeiro/Suprimentos | 158.503 | 60,54 |
| Contabilidade | 48.400 | 18,49 |
| Advocatícios | 100.000 | 38,20 |
| Ambiental | 3.800 | 1,45 |
| Segurança Trabalho | 12.740 | 4,87 |
| **TOTAL CONSULTORIAS** | **340.893** | **130,20** |

**Total Projetos + Consultorias: R$ 678.383 (259,10 R$/m²)**

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Outorga onerosa | 60.960 | 23,28 |
| Licenciamento/taxas | 42.452 | 16,21 |
| ARTs e laudos | 13.385 | 5,11 |
| Habite-se | 9.190 | 3,51 |
| **TOTAL TAXAS** | **125.987** | **48,12** |

### 10.3 Equipe Administrativa

> Dados detalhados de equipe mensal não disponíveis de forma unitária. O total de "Administração de obra" = R$ 880.306.

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Administração obra | 880.306 | 336,23 |

| Índice | Valor | Un |
|---|---|---|
| Administração obra / AC | 336,23 | R$/m² |
| Administração obra / mês | 33.858 | R$/mês (÷26 meses) |

### 10.4 Proteção Coletiva (EPCs)

| Item | Valor (R$) |
|---|---|
| Guarda-corpo forma | 1.997 |
| Guarda-corpo laje | 13.577 |
| Rede SLQA | 22.692 |
| Sinalização | 5.000 |
| Linha de vida | 16.463 |
| EPI | 3.500 |
| **TOTAL EPCs** | **63.230** |

| Índice | Valor | Un |
|---|---|---|
| EPCs / AC | **24,15** | R$/m² |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Período | Custo/mês (R$) | Total (R$) |
|---|---|---|---|---|
| Mini-grua | Locação | 14 meses | 2.260 | 31.640 |
| Andaime | Locação | 4 meses | 1.500 | 6.000 |
| Balancim | Locação | 4 meses | 2.600 | 10.400 |
| Montagem balancim | — | 14 un | 500/un | 7.000 |
| **TOTAL** | — | — | — | **55.040** |

| Índice | Valor | Un |
|---|---|---|
| Equipamentos / AC | **21,02** | R$/m² |

### 10.6 Ensaios Tecnológicos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Ensaios tecnológicos | 25.960 | 9,92 |

### 10.7 Outros CI

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Softwares | 106.480 | 40,67 |
| Impressões | 6.179 | 2,36 |
| Seguro obra | 9.255 | 3,54 |
| Consumos mensais | 37.431 | 14,30 |
| Equipamentos canteiro | 15.140 | 5,78 |
| Topografia | 21.260 | 8,12 |
| Sondagens | 4.926 | 1,88 |

**Consumos mensais (26 meses):**
- Energia: R$ 14.296 (R$ 550/mês)
- Água: R$ 14.296 (R$ 550/mês)
- Internet: R$ 3.640 (R$ 140/mês)
- Limpeza: R$ 5.200 (R$ 200/mês)

**Softwares (26 meses):**
- Prevision: R$ 24.400 (R$ 938/mês)
- Conaz: R$ 4.800 (R$ 185/mês)
- Sienge: R$ 49.560 (R$ 1.906/mês)
- DocuSign: R$ 4.420 (R$ 170/mês)
- ConstruCode: R$ 14.300 (R$ 550/mês)
- ConstruFlow: R$ 9.000 (R$ 346/mês)

### 10.8 Despesas Administrativas (não são CI de obra)

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Taxa estruturação | 569.067 | 217,35 |
| Comissões vendas | 640.354 | 244,58 |
| Despesas cartorárias | 3.833 | 1,46 |
| Despesas bancárias | 3.465 | 1,32 |
| Marketing | 780 | 0,30 |
| Outros encargos | 240 | 0,09 |
| **TOTAL DESP. ADM** | **1.217.739** | **465,10** |

### 10.9 Terreno

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Aquisição terreno | 1.750.000 | 668,37 |
| Taxas terreno | 56.000 | 21,39 |
| **TOTAL TERRENO** | **1.806.000** | **689,76** |

### 10.10 Instalações Provisórias (Canteiro + Segurança)

| Item | Valor (R$) |
|---|---|
| Canteiro | 39.920 |
| Ligações provisórias | 4.220 |
| PCMAT | 3.150 |
| Limpeza vegetal | 4.996 |
| Entulhos | 62.400 |
| **TOTAL** | **177.917** |

### 10.11 Resumo CI (UC1 completa)

| Subgrupo | Valor (R$) | R$/m² | % da UC1 |
|---|---|---|---|
| Terreno | 1.806.000 | 689,76 | 34,95% |
| Despesas Administrativas | 2.098.044 | 801,32 | 40,60% |
| Custos Indiretos (obra) | 1.031.001 | 393,78 | 19,95% |
| Instalações Provisórias | 177.917 | 67,95 | 3,44% |
| Equipamentos | 55.040 | 21,02 | 1,06% |
| **TOTAL UC1** | **5.168.002** | **1.973,85** | **100%** |

> **Se excluir terreno:** CI efetivo = R$ 3.362.002 = R$ 1.284/m² (24,1% do total).
> **Se excluir terreno + desp. admin:** CI de obra puro = R$ 1.263.958 = R$ 483/m² (9,1% do total) — dentro da faixa base (350-700 R$/m²).

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bacia PNE com caixa | 6 | 0,12 | 1.337,11 | 8.022,66 |
| Bacia com caixa acoplada | 55 | 1,12 | 1.148,21 | 63.151,61 |
| Lavatório suspenso PNE | 2 | 0,04 | 878,49 | 1.756,98 |
| **Subtotal Louças** | — | — | — | **72.931,25** |
| Torneira lavatório | 3 | 0,06 | 50,00 | 150,00 |
| Torneira bica alta | 4 | 0,08 | 196,00 | 784,00 |
| Acabamento registro | 60 | 1,22 | 50,00 | 3.000,00 |
| Acabamento registro PNE | 6 | 0,12 | 60,00 | 360,00 |
| Barra apoio deficiente | 7 | 0,14 | 35,00 | 245,00 |
| Banqueta articulável | 1 | 0,02 | 709,69 | 709,69 |
| Chuveiro elétrico | 1 | 0,02 | 60,00 | 60,00 |
| **Subtotal Metais** | — | — | — | **5.308,69** |
| Granito 138×55 | 3 | 0,06 | 975,50 | 2.926,50 |
| Granito 275×55 | 1 | 0,02 | 2.809,20 | 2.809,20 |
| Tampo com cuba (apto) | 55 | 1,12 | 567,43 | 15.425,91 |
| **Subtotal Bancadas** | — | — | — | **21.729,04** |
| **TOTAL** | — | — | — | **99.968,98** |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | **R$ 2.040** | R$/UR |
| Louças+Metais / AC | **38,18** | R$/m² |

> **Louças+Metais/UR = R$ 2.040** — baixo comparado com AMI (R$ 3.423/UR) e base geral. Reflete padrão médio-alto (não alto).
>
> **Nota:** Torneiras e metais com PUs muito baixos (R$ 50/un para torneira lavatório, R$ 50/un para registro). Indica entrega "básica" — sem metais premium. Apenas 3 torneiras lavatório + 4 torneiras bica alta para 49 unidades sugere que metais privativos ficam por conta do comprador.

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR | Ref. AMN |
|---|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | **100,7** m²/mês | 306 | 308 | 150 |
| Burn rate mensal | Total / Prazo | **R$ 0,54M**/mês | R$ 0,86M | R$ 1,12M | R$ 0,47M |
| Meses por pavimento | Prazo / NP | **6,5** | 1,7 | 5,1 | 2,1 |
| UR por mês | UR / Prazo | **1,88** un/mês | 1,3 | 3,9 | 0,9 |
| Custo / mês / m² | (Total/Prazo) / AC | **205,14** R$/m²/mês | 80,5 | 100,8 | 104,5 |

> **Destaques produtividade:**
> - Ritmo = 101 m²/mês — **o MAIS BAIXO** da base (KIR 306, ADR 308, AMN 150). Obra muito pequena.
> - Custo/mês/m² = R$ 205 — **o MAIS ALTO** da base. Custos fixos mensais (equipe, equipamentos) divididos por pouca área = ineficiência de escala.
> - Burn rate R$ 537k/mês é moderado em absoluto, mas altíssimo por m².

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Índice | Valor | Un | Ref. base |
|---|---|---|---|
| Impermeabilização / AC | **62,44** | R$/m² | Média 65, range 43-94 |

> **Impermeabilização R$ 62/m²** — dentro da faixa, levemente abaixo da média. Alinhado com AMI (64,53) e AMN (66,94). Dados de breakdown por sistema não disponíveis na planilha.

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Revestimentos Complementares | 243.250,90 | 92,91 | — |
| Mobiliário, Paisagismo e Decoração | 220.000,00 | 84,03 | Estimativa/verba |
| Limpeza final | 86.974,94 | 33,22 | — |
| Ligações definitivas | 65.000,00 | 24,83 | — |
| Cobertura | 69.331,63 | 26,48 | — |
| **TOTAL COMPLEMENTARES** | **684.557,47** | **261,47** | — |

> **Complementares R$ 261/m²** — dentro da faixa (49-553), acima da média sem outliers (~225). Puxado por Rev. Complementares R$ 93/m².
>
> **Mobiliário R$ 220k (R$ 84/m²):** Valor relativamente alto por m² — se tiver terraço/lazer de 471 m², dá R$ 467/m² de área de lazer, dentro da faixa (R$ 1.500-2.500/AL da base) se considerar que inclui paisagismo.

---

## SEÇÃO 15 — BENCHMARK

### Projetos de Referência (Obras Menores + Protendida na Base)

| Projeto | Cidade | AC (m²) | Pavimentos | Prazo | CUB ratio | R$/m² |
|---|---|---|---|---|---|---|
| **Ingleses Spot** | **Floripa/SC** | **2.618** | **4** | **26** | **1,88** | **5.334** |
| Amalfi Marine (AMN) | Navegantes/SC | 4.499 | 14 | 30 | 1,14 | 3.136 |
| BD Campeche | Floripa/SC | 3.633 | 7 | 36 | 1,54* | 4.491 |
| Viva Perequê | Porto Belo/SC | 5.576 | 15 | 36 | 1,39 | 4.129 |
| EIS Jurerê | Floripa/SC | 5.348 | 14 | N/D | N/D | N/D |
| Redentor (protendida) | Itapema/SC | 16.728 | 43 | 50 | 1,47 | 4.043 |
| Monolyt (protendida) | Bal. Camboriú/SC | 14.693 | 8 (2 torres) | 36 | 2,17 | 5.988 |

*Campeche sem mob. privativo

### Comparativo R$/m² AC por Macrogrupo (vs projetos menores da base)

| Macrogrupo | Ingleses Spot | Campeche | AMN | Média Ref. | Posição |
|---|---|---|---|---|---|
| Gerenciamento | 1.974¹ | 702 | 522 | 612 | ⚠️ MUITO acima (inclui terreno) |
| Supraestrutura | 864 | 799 | 485 | 642 | ⚠️ Acima (+35%) |
| Instalações | 416 | 378 | 281 | 330 | ⚠️ Acima (+26%) |
| Esquadrias | 471 | 380 | 237 | 309 | ⚠️ Acima (+52%) |
| Alvenaria | 178 | 146² | 117 | 132 | ⚠️ Acima (+35%) |
| Impermeabilização | 62 | 80 | 67 | 74 | ✅ Abaixo (-16%) |
| Rev. Internos + Fachada | 291 | 222+184 | 163+123 | N/A | N/A (agrupado) |
| Teto | 84 | 83 | 42 | 62 | ⚠️ Acima (+35%) |
| Pisos | 150 | 253³ | 143 | 198 | ✅ Abaixo (-24%) |
| Pintura | 172 | 187 | 143 | 165 | ✅ Dentro (+4%) |
| Louças/Metais | 38 | N/D | 24 | 31 | ✅ Dentro |
| Complementares | 261 | 266 | 241 | 254 | ✅ Dentro (+3%) |
| Imprevistos | 79 | 74 | N/D | 77 | ✅ Dentro |

¹ Inclui terreno R$ 1.806k → sem terreno = R$ 1.284/m²
² Campeche pouco drywall
³ Campeche: acabamento mais elaborado

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média

- **Gerenciamento R$ 1.974/m² (37%):** MUITO ALTO — mas inclui terreno (R$ 1,8M = R$ 690/m²), comissões de venda (R$ 640k), taxa de estruturação (R$ 569k). Sem terreno: R$ 1.284/m² (24,1%). Sem terreno + sem desp. administrativas: R$ 483/m² (9,1%). O "Gerenciamento" neste projeto é na verdade o custo da UC1 (incorporação), não apenas gestão de obra.

- **Supraestrutura R$ 864/m²:** Acima da faixa cubetas (600-820) mas explicável por laje **protendida** em obra de **4 pavimentos** — pouca diluição de custos fixos (grua, escoramento, mobilização). Comparar com Redentor (R$ 795/m² protendida, 32 pav tipo) e Monolyt (R$ 1.154, 3+3 pav tipo). Ingleses com NPT=3 está na faixa "protendida NPT<10" da base (R$ 1.000-1.900), embora abaixo por ser obra mais simples.

- **Esquadrias R$ 471/m²:** **ELEVADO** — acima de 85% dos projetos da base. Precisa entender se inclui guarda-corpo premium, brise, pele de vidro ou se é apenas alumínio de padrão alto. Para 49 unidades compactas, dá ~R$ 25.144/UR em esquadrias, o que parece desproporcional.

- **Instalações R$ 416/m²:** Acima do default alto SC (350-380). Pode ser efeito de escala — itens fixos (SPDA, entrada energia, quadros, bombas) divididos por 2.618 m² pesam mais. Ou especificação mais completa (sprinklers? VRF?).

- **R$/m² total = R$ 5.334 (1,88 CUB):** Alto, mas coerente com o porte (2.618 m²). Obras menores da base: Campeche R$ 4.491 (3.633 m²), AMN R$ 3.136 (4.499 m²). A escala pequena dilui mal os custos fixos.

### ✅ Dentro da Faixa

- **Impermeabilização R$ 62/m²:** Alinhada com a média (65 R$/m²), consistente com AMI (65) e AMN (67).

- **Pintura R$ 172/m²:** Dentro da faixa estável (95-187), próxima do topo — coerente com padrão médio-alto.

- **Louças e Metais R$ 38/m²:** Dentro da faixa (23-51). PU baixo dos metais (R$ 50/torneira) indica entrega básica.

- **Complementares R$ 261/m²:** Dentro da faixa ajustada (133-312 sem outliers). Mobiliário R$ 220k é verba estimada.

- **Imprevistos R$ 79/m² (1,48%):** Conservador — abaixo dos 3% típicos. Para uma obra de R$ 14M, imprevistos de R$ 206k parece baixo.

### 🔽 Abaixo da Média

- **Infraestrutura R$ 126/m²:** Significativamente abaixo da faixa (115-344, média ~200). Com 40 estacas HC de 18m = 720 m lineares, e fundação rasa de 80 m³ concreto, o custo parece baixo. Pode indicar terreno com boa capacidade de suporte em Ingleses.

- **Movimentação de Terra R$ 40/m²:** Dentro da faixa (7-173), razoável para terreno sem subsolo e sem contenção.

- **Sistemas Especiais R$ 76/m²:** ABAIXO da base (89-748). Escopo reduzido — sem piscina aquecida, sem solar, poucos sistemas. Para obra de 49 unidades compactas, parece coerente.

### 📝 Particularidades

1. **Obra MUITO PEQUENA (2.618 m²):** A menor da base por larga margem (próxima é AMN com 4.499 m²). Todos os custos fixos (equipe, equipamentos, licenças, softwares) são diluídos em pouca área, inflacionando o R$/m². O custo total (R$ 14M) é relativamente baixo — o R$/m² alto é efeito matemático da área.

2. **Laje protendida em 4 pavimentos:** Escolha técnica interessante. Protensão normalmente é usada em vãos maiores ou edifícios mais altos. Para 3 pavimentos tipo + terraço, o custo da protensão (5.659 kg × ~R$ 35/kg ≈ R$ 198k) pode não ter se pago versus treliçada em todos os andares.

3. **49 unidades em 2.618 m² = 53,4 m²/UR:** As unidades mais compactas da base. Provável mix de estúdios e 1-quarto. Alta densidade significa muitas instalações (pontos hidráulicos, elétricos, medidores) por m² de área construída — explica em parte as instalações acima da média.

4. **Terreno dentro do "Gerenciamento":** A planilha coloca terreno (R$ 1,8M), comissões (R$ 640k), taxa de estruturação (R$ 569k) e demais despesas administrativas junto com CI de obra. Para análise paramétrica pura, seria necessário separar: obra propriamente dita ≈ R$ 8.797.041,59 (UC2 R$ 8.604.399,84 + parte da UC1).

5. **Concreto/AC = 0,188 m³/m²:** Alinhado com protendida — protensão reduz seção de concreto. Similar ao ADR (0,189).

6. **Alvenaria/AC = 1,48:** Dentro da faixa, predominantemente cerâmica (87%). Uso de bloco celular (13%) sugere divisórias internas leves.

7. **Forma/AC = 1,83:** O mais alto entre os projetos comparados, refletindo a desproporção de áreas auxiliares (barrilete 730 m², reservatório) versus AC reduzida.

8. **Imprevistos a apenas 1,48%:** Abaixo do padrão da base (3%). Para uma obra de R$ 14M, R$ 206k de contingência é apertado. Risco de estouro orçamentário.

9. **Software R$ 106k (R$ 41/m²):** Custo alto por m² — mesma licença de Sienge, Prevision, ConstruCode que uma obra de 20.000 m² pagaria, mas dividida por 2.618 m². Efeito de escala claro.

10. **Diferença Planilha vs PDF:** R$ 192.640 (1,4%) de diferença entre total da planilha (R$ 13.965.042) e PDF Sienge (R$ 13.772.402). Verificar se é ajuste de revisão.

---

## RESUMO DE ÍNDICES GLOBAIS

> Quick reference — os números mais importantes do projeto.

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 13.965.043 | R$ |
| **R$/m²** | 5.333,75 | R$/m² |
| **CUB ratio** | 1,88 | CUB |
| **R$/UR** | R$ 285.001 | R$/UR |
| **AC/UR** | 53,4 | m²/un |
| Concreto supra / AC | 0,188 | m³/m² |
| Protensão total | 5.659 | kg |
| Protensão / m³ concreto | 11,70 | kg/m³ |
| Forma / AC | 1,83 | m²/m² |
| Alvenaria / AC | 1,48 | m²/m² |
| Forro / AC | N/D (R$ 84/m²) | m²/m² |
| Pintura parede / AC | N/D (R$ 172/m²) | m²/m² |
| Fachada / AC | N/D (incluída em Rev. Argamassa) | m²/m² |
| Portas / UR | N/D | un/UR |
| Estacas / AC | 0,275 | m/m² |
| MO instalações / AC | N/D | R$/m² |
| Elevador | N/D | R$/un |
| Ritmo construção | 100,7 | m²/mês |
| Burn rate | R$ 0,54M | R$/mês |
| Taxa aço fund. profunda | 19,65 | kg/m³ |
| Taxa aço fund. rasa | 81,31 | kg/m³ |
| Escoramento total | ~2.008 | m² |
| Louças+Metais / UR | R$ 2.040 | R$/UR |

---

> **Fonte:** ARV Ingleses Spot, Revisão R02 — Planilha orçamento Sienge v3 + PDF UC1/UC2
> **Extraído em:** 05/03/2026
> **Notas:**
> - UC1 (Gerenciamento) inclui terreno + despesas administrativas + CI de obra — inflaciona fortemente o R$/m²
> - Obra de 2.618 m² é a menor da base — efeito de escala em praticamente todos os índices
> - Dados de breakdown detalhado (PUs, áreas por serviço) limitados — planilha em formato macro
> - Imprevistos a 1,48% é conservador vs padrão 3% da base
