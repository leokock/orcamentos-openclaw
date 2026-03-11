# Índices Expandidos — Amalfi Maiori (CTN-ALF-MRI)

> Extraído em: 05/03/2026
> Fonte: Orçamento Comentado R05 (XLSX 47 sheets) + Apresentação R02 (XLSX 6 sheets) + PDF Análise
> Método: openpyxl data_only=True (coluna 6 = Cartesian como referência principal)

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Amalfi Maiori | — |
| Código CTN | — | CTN-ALF-MRI | — |
| Revisão | — | R05 (Orçamento) / R02 (Apresentação) | — |
| Localização | — | Itajaí/SC | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Construtora Amalfi | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | 8.366,50 (Apres.) / 8.369,50 (Orç.) | m² |
| Unid. Habitacionais | UR_H | 60 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 60 | un |
| Nº Total Pavimentos | NP | 18 | un |
| Nº Pavimentos Tipo | NPT | 11 (+1 diferenciado) | un |
| Nº Pav. Garagem | NPG | 3 | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 38 | meses |
| Data-base | — | Jul/2023 | — |
| CUB Referência | — | R$ 2.747,90 | R$ |
| R$/m² Total | — | 3.010,31 | R$/m² |
| CUB ratio | — | 1,10 | CUB |
| Tipo de Laje | — | N/D (fck 40 MPa) | — |
| Tipo de Fundação | — | Blocos + Baldrames (fundação profunda presumida) | — |
| Padrão Acabamento | — | Alto | — |

> **Nota:** AC usada nos cálculos = 8.366,50 m² (valor da Apresentação R02). O Orçamento R05 usa 8.369,50 m².

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | N/D (AT não informado) | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 139,4 m²/un | 243,7 | 78,7 |
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
| Residencial | 60 | 100% | 82,8 (área privativa) |

> Área privativa total: 4.969,86 m² → 82,8 m²/un (área privativa média)

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Descrição | Observação |
|---|---|---|
| Térreo | 1 pav | Sala comercial + acesso |
| Garagem G1, G2, G3 | 3 pav | 3 subsolos |
| Tipo Diferenciado | 1 pav | 1º andar tipo |
| Tipo (×11) | 11 pav | Pavimentos tipo repetitivos |
| Lazer/Rooftop | 1 pav | Área de lazer no topo |
| Reservatório + Barrilete + Casa Máquinas | Técnicos | — |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 419.762 |
| R$ / m² AP | Total / AP | R$ 5.067,69 |
| CUB / UR | (R$/UR) / CUB | 152,8 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 3.318.914 | 396,69 | 13,18% | — |
| 2 | Movimentação de Terra | 61.667 | 7,37 | 0,24% | 10-20 |
| 3 | Infraestrutura | 1.477.672 | 176,62 | 5,87% | 170-210 |
| 4 | Supraestrutura | 4.952.967 | 592,00 | 19,67% | 660-790 |
| 5 | Paredes e Painéis | 957.804 | 114,48 | 3,80% | 100-150 |
| 6 | Impermeabilização | 539.873 | 64,53 | 2,14% | 40-90 |
| 7 | Instalações (Elét+Hidro+GLP+Prev) | 2.471.960 | 295,46 | 9,81% | 280-340 |
| 8 | Equipamentos e Sist. Especiais | 1.127.280 | 134,74 | 4,48% | 130-240 |
| 9 | Climatização | — | — | — | (dentro de Sist. Especiais) |
| 10 | Rev. Internos Parede | 1.640.085 | 196,03 | 6,51% | 150-190 |
| 11 | Teto | 482.761 | 57,70 | 1,92% | 50-80 |
| 12 | Pisos | 1.116.640 | 133,47 | 4,43% | 170-200 |
| 13 | Pintura Interna | 1.143.520 | 136,68 | 4,54% | 90-140 |
| 14 | Esquadrias | 2.795.226 | 334,10 | 11,10% | 240-330 |
| 15 | Louças e Metais | 205.366 | 24,55 | 0,82% | — |
| 16 | Cobertura | 123.462 | 14,76 | 0,49% | 5-15 |
| 17 | Fachada | 1.248.714 | 149,25 | 4,96% | 100-170 |
| 18 | Complementares | 1.521.822 | 181,89 | 6,04% | 120-210 |
| — | **TOTAL** | **25.185.733** | **3.010,31** | **100%** | **2.315-3.175** |

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | 594,37 | 28,7% | 40 MPa | N/D |
| Vigas | 339,41 | 16,4% | 40 MPa | N/D |
| Lajes | 1.134,35 | 54,8% | 40 MPa | N/D |
| **TOTAL** | **2.068,13** | **100%** | **40 MPa** | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto / AC | 0,247 | m³/m² | 0,242 | 0,189 |

> **Nota:** fck 40 MPa — diferente dos demais projetos da base (fck 30-35 MPa). Pode influenciar PU do concreto para cima.

#### Armadura (Aço)

| Elemento | Peso (kg) | Taxa (kg/m³) |
|---|---|---|
| Pilares | 45.148 | 75,9 |
| Vigas | 63.555 | 187,3 |
| Lajes | 96.447 | 85,0 |
| Escadas | 4.095 | — |
| Rampas | 2.057 | — |
| **TOTAL** | **211.302** | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Taxa de aço global | 102,17 | kg/m³ | 82,32 | 114,88 |
| Aço / AC | 25,25 | kg/m² | 23,86¹ | 21,69 |
| PU aço (corte/dobra obra) | N/D | R$/kg | 6,12-7,98 | — |

¹ KIR: (255.777 kg / 10.722,5 m²)

> **Destaque:** Taxa de aço 102,17 kg/m³ está entre KIR (82,32) e ADR (114,88). Comentário na Apresentação R02: "muito mas muito aço (consumo de 238 kg/m³ de concreto)" — obs referindo ao R$/m² da supra, taxa aço real = 102 kg/m³.

#### Forma

| Elemento | Área (m²) | % |
|---|---|---|
| Pilares | 5.507,11 | 50,8% |
| Vigas | 3.072,07 | 28,4% |
| Lajes | 2.256,46 | 20,8% |
| **TOTAL** | **10.835,64** | **100%** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Forma / AC | 1,30 | m²/m² | 1,25 | 1,36 |

#### Comparativo Estrutural (da aba COMPARAÇÕES)

| Projeto | AC (m²) | Aço (kg) | Concreto (m³) | Forma (m²) | Aço/m³ | Concreto/m² | Forma/m² |
|---|---|---|---|---|---|---|---|
| **Maiori** | **8.367** | **211.302** | **2.068** | **10.836** | **102,2** | **0,247** | **1,30** |
| La Vie MG3 | 10.125 | 180.514 | 2.218 | 14.489 | 81,4 | 0,219 | 1,43 |
| SAK | 1.700 | 54.291 | 577 | 4.702 | 94,0 | 0,340 | 2,77 |
| Paessaggio | 16.348 | 388.922 | 4.491 | 22.817 | 86,6 | 0,275 | 1,40 |

### 4.2 Infraestrutura

#### Fundação — Blocos e Baldrames

| Item | Qtd | Un | Observação |
|---|---|---|---|
| Blocos de fundação | 33 | un | B1 a B22 (diversos tamanhos) |
| Volume blocos | 264,15 | m³ | Concreto C-40 |
| Forma blocos | 310,07 | m² | — |
| Baldrames | 40 | un | V101 a V139 |
| Volume baldrames | 25,66 | m³ | — |
| Forma baldrames | 312,31 | m² | — |
| **Volume concreto total infra** | **331,04** | **m³** | fck 40 (blocos+terreo) |
| **Forma total infra** | **641,51** | **m²** | — |
| Escavação total | 444,06 | m³ | — |
| Volume de bota-fora | 156,04 | m³ | — |

#### Aço Infraestrutura

| Item | Peso (kg) | Obs |
|---|---|---|
| Aço fundação (CA50) | 28.935 | Blocos |
| Aço terreo (CA50) | 5.509 | Terreo |
| Aço terreo (CA60) | 444 | — |
| **Total aço infra** | **34.888** | — |
| **Taxa aço infra** | **105,4** | kg/m³ |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Volume concreto infra / AC | 0,040 | m³/m² | — | — |
| Forma infra / AC | 0,077 | m²/m² | — | — |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria total (visus) | #VALUE!¹ | — | 1,37 | 1,56 |
| Chapisco interno (estrutura) | 4.042,83 | 0,48 | — | — |
| Chapisco interno (alvenaria) | 14.098,09 | 1,69 | — | — |
| Chapisco interno total | 18.140,92 | 2,17 | 2,68 | 2,58 |
| Reboco/massa interna | 18.140,92 | 2,17 | 2,68 | 2,58 |
| Estucamento | 599,20 | 0,07 | — | — |
| Forro gesso mineral | 4.749,18 | 0,57 | 0,57 | 0,16 |
| Forro total (gesso+argamassado+estucamento) | 7.139,77 | 0,85 | — | 0,55 |
| Contrapiso | 5.199,16 | 0,62 | 0,66 | 0,76 |
| Piso cerâmico/porcelanato | 4.797,77 | 0,57 | — | — |
| Piso vinílico | 1.201,52 | 0,14 | — | — |
| Pintura parede | 13.581,55 | 1,62 | 2,34 | 1,05 |
| Fachada total (chap+reb) | 6.862,65 | 0,82 | 0,73 | 1,41 |
| Impermeabilização total | 4.088,11 | 0,49 | — | — |

¹ Alvenaria com fórmulas que resultam #VALUE! no data_only. Vergas/contravergas sugerem ~4.224 m² de alvenaria (col. 4 row 38 da aba PAREDE) + 251,59 + 335,28 m² de revestimentos

### 5.2 Comprimentos de Serviço / AC

| Serviço | Comprimento (m) | Índice (m/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Verga + contraverga | 2.178,10 | 0,26 | 0,33 | 0,13 |
| Rodapé | 4.175,50 | 0,50 | 0,84 | — |
| Contramarco | 1.644,37 | 0,20 | 0,27 | — |
| Peitoril | 352,14 | 0,04 | — | — |
| Faixa garagem | 205,60 + 193,70 | 0,05 | — | — |
| Negativo fachada | 61,00 | 0,01 | — | — |

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Bacias sanitárias | 167 | 2,78 | — | 0,4 |
| Registros gaveta c/ canopla 3/4" | 236 | 3,93 | — | — |
| Registros gaveta c/ canopla 1" | 60 | 1,00 | — | — |
| Pontos de luz (privativa) | 134 | 2,23 | — | — |
| Pontos de luz (total) | ~1.406 | 23,4 | — | — |

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor Material (R$) | Obs |
|---|---|---|
| Hidráulicas (Alimentação+AF) | 202.536 | Alimentação 134.582 + AF 67.955 |
| Sanitário (Esgoto) | 105.589 | — |
| Elétricas | ~550.000² | Quadros 192.697 + luminárias 74.339 + fiação etc. |
| Preventivas | ~120.000² | Hidrantes 48.803 + bombas etc. |
| Gás (GLP) | 76.325 | — |
| Lógica/Telecom | 206.026 | — |
| Interfonia | 11.280 | — |
| CFTV | 3.035 | — |
| **TOTAL instalações** | **~2.471.960** | **R$ 295,46/m²** |

² Valores estimados dos subtotais visíveis. O total final R$ 2.471.960 vem da aba ORÇAMENTO_EXECUTIVO (inclui MO).

> **Nota:** O orçamento não separa MO por disciplina de instalação. Total do macrogrupo = R$ 295,46/m² (dentro da faixa 280-340).

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | Descrição |
|---|---|---|---|
| Chapisco estrutura | 4.042,83 | m² | Chapisco interno |
| Chapisco alvenaria | 14.098,09 | m² | Chapisco interno |
| Massa única | 18.140,92 | m² | Reboco interno |
| Estucamento | 599,20 | m² | Acabamento fino |
| Cerâmico parede banheiro | 2.090,64 | m² | Placa 32×60cm |
| Cerâmico parede cozinha | 672,01 | m² | Placa 32×60cm |
| Cerâmico parede A. privativa | 742,47 | m² | Placa 32×60cm |
| Porcelanato parede A. comum | 55,74 | m² | Barcelona cristal 90×90 |
| Peitoril/pingadeira | 352,14 | m | Material a confirmar |

### 7.2 Pisos

| Item | Qtd | Un | Descrição |
|---|---|---|---|
| Contrapiso 4cm | 373,87 | m² | Argamassa estabilizada |
| Contrapiso 5cm | 3.392,96 | m² | Argamassa estabilizada |
| Contrapiso 6cm | 1.220,09 | m² | Argamassa estabilizada |
| Contrapiso escada | 212,24 | m² | 4cm |
| **Total contrapiso** | **5.199,16** | **m²** | — |
| Porcelanato Barc. Cristal 90×90 NAT | 2.544,51 | m² | Privativa + áreas comuns |
| Porcelanato Barc. Cristal 90×90 EXT | 517,02 | m² | Áreas externas |
| Piso vinílico 20×120cm | 1.201,52 | m² | A. privativa |
| Piso polido garagem | 1.729,84 | m² | Polimento + pintura |
| Piso cimentado | 330,20 | m² | Calçada |
| Piso cimentado ranhurado | 236,90 | m² | — |
| Pastilha piscina | 28,00 | m² | Placa 5×5cm |
| Rodapé poliestireno 12cm | ✓ | m | — |
| Rodapé poliestireno 7cm | ✓ | m | Majoritário |
| **Total rodapé** | **4.175,50** | **m** | — |
| Soleira granito | 422,86 | m | Branco Siena e=2cm |
| Soleira porcelanato | 105,02 | m | 90×90 |

### 7.3 Teto

| Item | Qtd | Un | Descrição |
|---|---|---|---|
| Estucamento teto (concreto) | 146,99 | m² | Estrutura aparente |
| Estucamento teto c/ pintura | 135,37 | m² | — |
| Forro gesso mineral | 4.749,18 | m² | Placa mineral + textura |
| Forro gesso corrido | 4,34 | m² | + selador |
| Forro A. técnica | 14,62 | m² | — |
| Marquise | 10,87 | m² | — |
| Reboco teto c/ pintura | 270,76 | m² | Massa única 20mm |
| Reboco teto c/ textura | 1.818,51 | m² | Massa única 20mm |
| **Total teto** | **7.139,77** | **m²** | — |
| Perímetro negativo | 7.022,55 | m | — |

### 7.4 Pintura

| Item | Qtd | Un | Descrição |
|---|---|---|---|
| Massa corrida | 46,31 | m² | Mochetas |
| Pintura parede A. privativa | 6.087,81 | m² | Alvenaria |
| Pintura parede estrutura A. priv. | 1.472,92 | m² | — |
| Pintura parede A. comum | 348,15 | m² | — |
| Pintura parede Hall | 640,28 + 211,28 | m² | Alv + estr |
| Textura antecâmara/escada | 935,67 + 741,43 | m² | Alv + estr |
| Textura garagem | 1.157,02 + 491,60 | m² | Alv + estr |
| Pintura sala comercial | 678,06 + 250,88 | m² | — |
| **Total pintura parede** | **13.581,55** | **m²** | — |
| **Decomposição:** | | | |
| Selador | 13.581,55 | m² | — |
| Massa | 10.115,33 | m² | — |
| Pintura acrílica | 9.819,66 | m² | — |
| Pintura PVA | 443,06 | m² | — |
| Textura | 3.466,22 | m² | — |
| Faixas garagem | 193,70 | m | — |

### 7.5 Fachada

| Item | Qtd | Un | Descrição |
|---|---|---|---|
| Chapisco estrutura (externo) | 2.179,00 | m² | — |
| Chapisco alvenaria (externo) | 4.683,65 | m² | — |
| Massa única (externo) | 6.862,65 | m² | — |
| Pintura fachada — Nanquim | 231,37 | m² | Alv 185,63 + Estr 45,74 |
| Pintura fachada — Ouro Branco | 1.534,97 | m² | Alv 927,08 + Estr 607,89 |
| Pintura fachada — Cimento Queimado | 1.289,65 | m² | Alv 779,94 + Estr 509,71 |
| Pintura fachada — Patativa | 2.280,75 | m² | Alv 1.844,50 + Estr 436,25 |
| Pintura fachada — Madagascar | 674,35 | m² | Alv 340,37 + Estr 333,98 |
| Pintura fachada divisa — Cim Queim | 828,47 | m² | Alv 585,01 + Estr 243,46 |
| Pintura fachada — Ouro Branco (muro) | 16,97 | m² | — |
| Pintura fachada — Verde Arbusto | 6,12 | m² | — |
| **Total fachada (alvenaria)** | **4.683,65** | **m²** | — |
| **Total fachada (estrutura)** | **2.179,00** | **m²** | — |
| Negativo fachada (Nanquim) | 41,45 | m | — |
| Negativo fachada (Madagascar) | 19,55 | m | — |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

| Tipo | Qtd/Área | Un | Obs |
|---|---|---|---|
| Brise alumínio (chumbo) | 428,46 | m² | — |
| Contramarco | 1.644,37 | m | — |
| Pele de vidro | 139,13 | m² | 16 esquadrias fixas (VF1-VF16) |
| Guarda-corpo vidro temp. lam. | 597,80 | m | h=120cm, sem corrimão |
| Guarda-corpo alumínio (sacada) | 270,00 | m | Corrimão madeira |
| Gradil alumínio (A. técnica) | 14,41 | m | — |
| Gradil alumínio (sacada metálico) | 34,96 | m | — |
| Esquadrias alumínio | #VALUE! | m² | Fórmulas não resolvidas |
| Portas madeira | #VALUE! | un | Fórmulas não resolvidas |
| PCF | #VALUE! | un | Fórmulas não resolvidas |

### 8.2 Índices

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Contramarco / AC | 0,20 | m/m² | 0,27 | — |
| Pele de vidro | 139,13 | m² total | — | — |
| Brise | 428,46 | m² total | — | — |
| GC vidro | 597,80 | m total | — | — |
| Esquadrias R$/m² AC | 334,10 | R$/m² | — | — |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Sistemas Especiais (total) | — | — | 1.127.280 |
| Interfonia | — | — | 11.280 |
| CFTV | — | — | 3.035 |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Sistemas Especiais / AC | 134,74 | R$/m² | 96,44 | 179,87 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor Cartesian (R$) | Valor Amalfi (R$) |
|---|---|---|
| Arquitetônico | 74.000 | 74.000 |
| Interiores | 65.550 | N/R |
| Estrutural | 41.100 | 41.100 |
| Fachada técnico | 2.884 | N/R |
| Fundação | 7.635 | N/R |
| Hidrossanitário | 10.000 | 10.000 |
| Elétrico | 6.000 | 6.000 |
| Preventivo | 15.000 | 15.000 |
| Ar Condicionado | 1.000 | 1.000 |
| Telecom | 2.000 | 2.000 |
| Luminotécnico | 1.000 | 1.000 |
| Telefonia | 1.000 | 1.000 |
| Segurança | 850 | 850 |
| Terraplanagem | 1.500 | 1.500 |
| Impermeabilização | 37.800 | 0 (não realizado) |
| Esquadrias | 26.550 | 0 (não realizado) |
| Isolamento acústico | 59.120 | 0 (não realizado) |
| Sonorização | 5.000 | 0 (não realizado) |
| Piscinas | 4.370 | 0 (não realizado) |
| Comunicação Visual | 8.500 | 0 (não realizado) |
| Paisagismo | 13.800 | 0 (não realizado) |
| Legalização/incorporação | 15.310 | 15.310 |
| **Total Projetos** | **399.969** | **244.829** |

> **Nota:** Cartesian orça projetos que a Amalfi não contratou (impermeabilização, esquadrias, acústico, etc.)

### Consultorias

| Item | Valor Cartesian (R$) |
|---|---|
| Consultoria esquadrias | 5.000 |
| Compatibilização BIM | 10.975 |
| Controle qualidade | 49.260 |
| Modelagem BIM arq. | 41.832 |
| Modelagem BIM complementar | 20.000 |
| Consultoria legalização | 8.500 |
| Orçamento e Planejamento | 50.891 |
| **Total Consultorias** | **186.458** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) |
|---|---|
| Aprovação prefeitura | 20.905 |
| Bombeiros | 6.863 |
| Licença ambiental | 5.000 |
| Alvará construção | 8.456 |
| Aprovação água/esgoto | 2.513 |
| Habite-se prefeitura | 10.886 |
| Habite-se bombeiros | 5.775 |
| Seguro obra | 17.334 |
| IPTU | 43.343 |
| ARTs | 1.811 |
| Cartório | 10.000 |
| INSS | 9.090 |
| Incorporação | 19.500 |
| **Total Taxas** | **161.475** |

### 10.3 Equipe Administrativa (resumo do R05)

| Item | Valor (R$) | Obs |
|---|---|---|
| Serviços Técnicos | 798.492 | Projetos + Consultorias + Ensaios |
| Consumos/Taxas/Documentos | 173.695 | Licenças + Docs |
| Serviços Iniciais | 2.496.092 | Segurança, EPCs, equipamentos, canteiro, equipe |
| **Total CI** | **3.693.203** | — |

### 10.4 Proteção Coletiva (EPCs)

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bandeja primária (fixa) | 206,80 | m | 483,68 | 100.024 |
| Bandeja secundária (móvel) | 94,28 | m | 169,32 | 15.963 |
| GC vãos (forma madeira) | 289,09 | m | 18,67 | 5.398 |
| GC pós-desforma (escora metálica) | 282,84 | m | 18,67 | 5.281 |
| Fechamento removível vãos | 184,68 | m² | 58,18 | 10.745 |
| Proteção linha de vida | 282,84 | m | 87,17 | 24.655 |
| Tela SLQA | 865,49 | m² | — | — |
| Sinalização placas | 13,80 | m² | — | — |
| Tapume | 73,86 | m | — | — |
| EPIs | — | vb | — | 18.355 |

### 10.5 Ensaios Tecnológicos

| Item | Valor (R$) | Obs |
|---|---|---|
| Controle tecnológico concreto | 17.370 | 1.200 CP × R$ 12,10 + ensaios |

### 10.6 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 624.797 | 74,68 | 16,9% | 2,5% |
| Consultorias | 186.458 | 22,29 | 5,0% | 0,7% |
| Ensaios | 17.370 | 2,08 | 0,5% | 0,1% |
| Taxas e Licenças | 161.475 | 19,30 | 4,4% | 0,6% |
| Documentos | 12.220 | 1,46 | 0,3% | 0,0% |
| Serviços Iniciais (ADM+EPCs+Equip) | 2.496.092 | 298,35 | 67,6% | 9,9% |
| **TOTAL CI** | **3.693.203** | **441,38** | **100%** | **14,67%** |

> **Destaque:** CI em 14,67% do total (R$ 441/m²) — considerando o total Cartesian R$ 25.185.733 com CI de R$ 3.693.203. O macrogrupo "Gerenciamento Téc/Admin" do PDF = R$ 3.318.914 (13,18%) — a diferença reflete reclassificação de itens entre CI e complementares.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bacia sanitária com caixa acoplada | 161 | 2,68 | 769 | 123.809 |
| Bacia Vogue Plus Conforto | 2 | — | 1.532 | 3.064 |
| Bacia Carrara Ébano | 1 | — | 3.370 | 3.370 |
| Bacia Carrara | 3 | — | 2.808 | 8.424 |
| Acabamento registro 3/4" | 169 | 2,82 | 24 | 4.053 |
| Acabamento registro Argon | 2 | — | 938 | 1.876 |
| Torneira cozinha Monocomando | 1 | — | 2.380 | 2.380 |
| Torneira lavatório standard | — | — | 145 | 145 |
| Lavatório embutido | 2 | — | 109 | 218 |
| Pia inox | 2 | — | 170 | 340 |
| Ralo | 50 | 0,83 | 18 | 900 |
| Barra apoio | 10 | 0,17 | 300 | 2.998 |
| **LOUÇAS subtotal** | — | — | — | **162.333** |
| **MARMOARIA** | — | — | — | **27.982** |
| **ACESSÓRIOS** | — | — | — | **4.353** |
| **MO louças e metais** | 8.366,5 m² | — | 7,00/m² | **58.566** |
| **TOTAL** | — | — | — | **~205.366** |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | R$ 3.423 | R$/UR |
| Louças+Metais / AC | 24,55 | R$/m² |
| MO L&M / AC | 7,00 | R$/m² |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 220 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 663k/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 2,1 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 1,6 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 79,2 R$/m²/mês | 80,5 | 100,8 |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Sistema | Área (m²) | Aplicação |
|---|---|---|
| Argamassa polimérica | 217,62 | Área de serviço |
| Argamassa polimérica | 1.191,01 | Banheiro |
| Argamassa polimérica | 772,87 | Box banheiro |
| Argamassa polimérica | 457,64 | Cozinha |
| Argamassa polimérica | 157,40 | Reservatórios |
| Argamassa polimérica | 436,30 | Sacada |
| **Subtotal arg. polimérica** | **3.232,84** | — |
| Manta asfáltica 4mm | 121,43 | Áreas externas |
| Manta asfáltica 4mm | 311,98 | Terraços |
| Manta asfáltica | 35,36 | Floreiras |
| Manta asfáltica 4mm | 66,21 | Piscina |
| **Subtotal manta** | **534,98** | — |
| Manta líquida peitoris | 320,29 | Peitoris |
| **TOTAL** | **4.088,11** | — |

| Índice | Valor | Un |
|---|---|---|
| Impermeabilização / AC | 0,49 | m²/m² |
| Arg. polimérica / total | 79,1% | — |
| Manta asfáltica / total | 13,1% | — |
| Manta líquida / total | 7,8% | — |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Mobiliário áreas comuns | 479.361 | 57,29 | 13 ambientes lazer (Cartesian) |
| Mobiliário (Amalfi) | 719.041 | 85,93 | +50% taxa para itens não previstos |
| **Total complementares** | **1.521.822** | **181,89** | — |

### Detalhamento Mobiliário (por ambiente)

| Ambiente | Valor (R$) |
|---|---|
| Academia | 27.490 |
| Coworking | 32.440 |
| Games | 31.700 |
| Hall entrada | 12.400 |
| Lavanderia | 29.300 |
| Oficina | 13.400 |
| Gourmet | 51.593 |
| Kids | 16.600 |
| Playground | 35.600 |
| Salão de Festas | 86.502 |
| Pub Jogos | 64.503 |
| Estar Piscina | 19.800 |
| Verbas Interiores | 71.433 |
| **Total geral** | **479.361** |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

### Projetos de Referência (aba CÁLCULO_MÉDIAS)

| Projeto | Data Base | CUB | AC (m²) | R$/m² (original) | R$/m² (indexado) |
|---|---|---|---|---|---|
| DOM | Fev/2023 | 2.662,47 | 6.003 | 3.271,12 | 3.376,08 |
| Liberato | Mai/2023 | 2.688,94 | 10.520 | 2.764,29 | 2.824,90 |
| Paessaggio | Abr/2023 | 2.680,84 | 16.348 | 3.302,64 | 3.385,26 |
| M Village | Dez/2022 | 2.643,16 | N/D | 3.635,17 | 3.779,22 |
| La Vie MG3 | Abr/2023 | 2.680,84 | 10.125 | 2.574,69 | 2.639,09 |

### Comparativo R$/m² por Macrogrupo (MAIORI vs Médias indexadas)

| Macrogrupo | Maiori | DOM | Liberato | Paessaggio | La Vie |
|---|---|---|---|---|---|
| Gerenciamento | 397 | 440 | 290 | 327 | 360 |
| Supraestrutura | 592 | 754 | 663 | 796 | 627 |
| Instalações | 295 | 321 | 279 | 259 | 312 |
| Esquadrias | 334 | 334 | 249 | 266 | 281 |
| Fachada | 149 | 171 | 105 | 221 | 85 |
| **TOTAL** | **3.010** | **3.376** | **2.825** | **3.385** | **2.639** |

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Faixa
- **Esquadrias: R$ 334/m² vs faixa 240-330** — brise alumínio R$ 428 m² (componente significativo), pele de vidro 139 m², guarda-corpo vidro 598 m. Alto padrão de acabamento
- **Revestimentos Parede: R$ 196/m² vs faixa 150-190** — ligeiramente acima, grande volume de cerâmica (3.505 m² total parede)
- **Cobertura: R$ 14,76/m² vs faixa 5-15** — no limite superior
- **CI alto: 13,18% do total** — 14,67% se considerado o total Cartesian (R$ 3.693.203). Projetos não contratados pela Amalfi inflam o orçamento Cartesian

### ✅ Dentro da Faixa
- **Infraestrutura: R$ 177/m²** — dentro de 170-210
- **Instalações: R$ 295/m²** — dentro de 280-340
- **Sist. Especiais: R$ 135/m²** — dentro de 130-240
- **Impermeabilização: R$ 65/m²** — dentro de 40-90
- **Teto: R$ 58/m²** — dentro de 50-80
- **Pintura: R$ 137/m²** — dentro de 90-140
- **Fachada: R$ 149/m²** — dentro de 100-170
- **Complementares: R$ 182/m²** — dentro de 120-210
- **Alvenaria: R$ 114/m²** — dentro de 100-150

### 🔽 Abaixo da Faixa
- **Supraestrutura: R$ 592/m² vs faixa 660-790** — **significativamente abaixo** (-10% do mínimo). Possíveis fatores: eficiência estrutural, preços de MO/material competitivos na região. Taxa de aço (102 kg/m³) é média e forma/AC (1,30) é normal
- **Pisos: R$ 133/m² vs faixa 170-200** — abaixo. Porcelanato Barcelona Cristal predomina (relativamente econômico), grande área de vinílico (1.202 m²)
- **Movimentação Terra: R$ 7/m² vs faixa 10-20** — abaixo, terreno relativamente plano ou já preparado

### 📝 Particularidades
- **fck 40 MPa** em toda supraestrutura — diferente da maioria dos projetos (fck 30-35). Custo do concreto proporcionalmente mais caro, mas volume total é eficiente
- **Duas colunas de preço:** Cartesian (referência orçamentária) e Amalfi (realidade do cliente). Diferenças relevantes em projetos/consultorias (Amalfi não contratou vários projetos orçados pela Cartesian)
- **Área AC diverge entre documentos:** 8.366,50 m² (Apresentação) vs 8.369,50 m² (Orçamento R05)
- **Alvenaria com fórmulas #VALUE!** — células dependem de referências externas não resolvidas em data_only. Total estimável por vergas/contravergas (~4.500 m²)
- **Mobiliário premium:** 13 ambientes de lazer + verbas interiores = R$ 479k (Cartesian), R$ 719k com taxa Amalfi (+50%)
- **Supraestrutura Cartesian vs Amalfi:** Cartesian orçou R$ 4.953k, mas planilha Amalfi teve R$ 8.010k (R$ 957/m²!) — diferença gigante reflete preços de concreto/aço/forma diferentes

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 25.185.733 | R$ |
| **R$/m²** | 3.010,31 | R$/m² |
| **CUB ratio** | 1,10 | CUB |
| **R$/UR** | R$ 419.762 | R$/UR |
| **R$/m² AP** | 5.067,69 | R$/m² AP |
| **AC/UR** | 139,4 | m²/un |
| **AP/UR** | 82,8 | m²/un |
| Concreto supra / AC | 0,247 | m³/m² |
| Concreto infra / AC | 0,040 | m³/m² |
| Taxa aço supra | 102,17 | kg/m³ |
| Taxa aço infra | 105,4 | kg/m³ |
| Forma supra / AC | 1,30 | m²/m² |
| Chapisco interno / AC | 2,17 | m²/m² |
| Forro total / AC | 0,85 | m²/m² |
| Contrapiso / AC | 0,62 | m²/m² |
| Pintura parede / AC | 1,62 | m²/m² |
| Fachada (massa) / AC | 0,82 | m²/m² |
| Rodapé / AC | 0,50 | m/m² |
| Contramarco / AC | 0,20 | m/m² |
| Impermeabilização / AC | 0,49 | m²/m² |
| Louças+Metais / UR | R$ 3.423 | R$/UR |
| Louças+Metais / AC | 24,55 | R$/m² |
| Instalações / AC | 295,46 | R$/m² |
| Sist. Especiais / AC | 134,74 | R$/m² |
| Ritmo construção | 220 | m²/mês |
| Burn rate | R$ 663k | R$/mês |

---

> **Fonte:** CTN-ALF-MRI, R05 (Orçamento) / R02 (Apresentação)
> **Extraído em:** 05/03/2026
> **Notas:** Coluna Cartesian como referência. fck 40 MPa em toda supra. Alvenaria com #VALUE! (fórmulas externas). Supraestrutura abaixo da faixa (R$ 592 vs 660-790). Esquadrias acima da faixa (R$ 334 vs 240-330). CI 13,18%.
