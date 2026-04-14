# Memorial de Extração — arthen-arboris

_Gerado em 13/04/2026 23:27 — Fase 17 (base enriquecida)_

Este documento detalha a **lógica de extração** de cada item do orçamento executivo, rastreando fontes de dados e lógica de precificação.

## 📊 Dados do Projeto

| Campo | Valor |
|---|---|
| **Slug** | `arthen-arboris` |
| **AC (Área Construída)** | 12.472,98 m² |
| **UR (Unidades)** | 98 |
| **Padrão** | medio |

## 🏗 Quantitativos Extraídos do BIM

**Fontes:** 1 IFCs, 0 DXFs, 0 PDFs

### Alvenaria e Paredes (IfcWall)

- **Total de elementos:** 19525 paredes
- **Área total:** 122.155 m²
- **Comprimento total:** 40.931 m

**Por tipo:**

| Tipo (material + espessura) | Qtd | Área m² | Comp m | Exemplos no IFC |
|---|---|---|---|---|
| outros_2cm | 10746 | 60.096 | 19.490 | LED 02:LED 02 / Parede básica:REV_2,5_REBOCO INTERNO |
| bloco_ceramico_14cm | 6387 | 36.213 | 13.516 | Parede básica:ALV_14_BLOCO CERAMICO |
| outros_3cm | 1436 | 14.928 | 5.223 | Parede básica:REV_3,5_REBOCO EXTERNO |
| bloco_ceramico_19cm | 810 | 7.061 | 2.219 | Parede básica:ALV_19_BLOCO CERAMICO |
| outros_?cm | 36 | 2.424 | 318 | Parede básica:REV MAD / Parede básica:ESCURO |
| outros_1cm | 10 | 1.096 | 32 | LED1:LED / Detalhe Fachada1:Detalhe Fachada |
| drywall_11cm | 36 | 153 | 53 | Parede básica:ALV_11,5_DRYWALL |
| bloco_ceramico_9cm | 30 | 76 | 24 | Parede básica:ALV_9_BLOCO CERAMICO |
| bloco_ceramico_5cm | 30 | 76 | 24 | Parede básica:ALV_5_BLOCO CERAMICO |
| outros_20cm | 4 | 33 | 32 | Parede básica:20_EXTERIOR BRA |

### Estrutura (lajes + vigas + pilares)

| Elemento | Quantidade | Volume m³ | Comprimento/Altura m | Fonte |
|---|---|---|---|---|
| Lajes (IfcSlab) | 1068 | 7.506,3 | área 58.843 m² | BIM IfcSlab |
| Vigas (IfcBeam) | 1279 | 250,6 | 2.633 | BIM IfcBeam |
| Pilares (IfcColumn) | 461 | 896,9 | 1.460 | BIM IfcColumn |

- **Concreto total estimado (BIM):** 8.653,8 m³
- **Índice concreto/m² AC:** 0,694 m³/m² (vs mediana base 0,34) 🔴 delta +104%

### Esquadrias e Aberturas

- **Portas (IfcDoor):** 735 unidades
- **Janelas (IfcWindow):** 400 unidades
- **Pele de vidro (IfcCurtainWall):** 495 elementos, 0 m²
- **Guarda-corpos (IfcRailing):** 60 elementos, 187 m

**Top 10 tipos de porta:**

- **PORTA SIMPLES:80 x 210 cm**: 210 un
- **PORTA SIMPLES:70 x 210 cm**: 197 un
- **PORTA SIMPLES:90 x 210 cm**: 75 un
- **PORTA VENEZIANA  COM BANDEIRA - METÁLICA:80 x 210**: 60 un
- **PORTA SIMPLES:CORRER -  70 x 210 cm**: 45 un
- **PORTA DO ELEVADOR:PE**: 40 un
- **PORTA DE CORRER - DUPLA:260x210**: 30 un
- **PORTA DE CORRER - DUPLA:250**: 30 un
- **PORTA SIMPLES:PCF 90 x 210 cm**: 12 un
- **PORTA DE GIRO - CORTINA:PORTA DE GIRO - CORTINA PV02**: 9 un

**Top 10 tipos de janela:**

- **JANELA PADRÃO:150x120_2 FOLHAS**: 120 un
- **JANELA FIXA - 1 FOLHA:60x80**: 120 un
- **JANELA PADRÃO:120x120_2 FOLHAS**: 60 un
- **JANELA FIXA - 1 FOLHA:80 x 80**: 40 un
- **JANELA FIXA - 1 FOLHA:50x80**: 30 un
- **JANELA BASCULANTE HORIZONTAL - 3 FOLHAS:60x80**: 30 un

### Ambientes (IfcSpace)

- **Total:** 1238 ambientes
- **Área total:** 43.305 m²
- **Volume total:** 157.928 m³

**Top 15 tipos de ambiente por área:**

| Ambiente | Qtd | Área m² |
|---|---|---|
| ÁREA DE CIRCULAÇÃO E MANOBRA | 6 | 5.625 |
| LIVING | 90 | 3.728 |
| TIPO 05 | 34 | 2.918 |
| TIPO 06 | 34 | 2.918 |
| TIPO 04 | 34 | 2.726 |
| TIPO 01 | 34 | 2.726 |
| ÁREA TÉCNICA | 69 | 2.614 |
| TIPO 03 | 34 | 2.476 |
| TIPO 02 | 34 | 2.476 |
| SUÍTE | 150 | 1.909 |
| CIRCULAÇÃO | 36 | 1.782 |
| ÁREA | 24 | 1.460 |
| CIRC. VERTICAL | 35 | 1.304 |
| Laje técnica | 30 | 1.164 |
| DORMITÓRIO | 60 | 702 |

## 💰 Orçamento Executivo — Lógica de Extração por Item

Cada item abaixo mostra: descrição, PU usado, PU base cross-projeto (se disponível), faixa P10-P90 e fonte.

### Gerenciamento

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Almoxarife | mes | 20,00 | R$ 4.750 | R$ 4.000,00 | R$ 2000 - 5127 | 23 | 🟢 Alta |
| Equipamentos de proteção Individual (EPI) | mes | 20,00 | R$ 3.000 | R$ 1.530,30 | R$ 250 - 12176 | 7 | 🟡 Média |

### Movimentação_de_Terra

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Escavação mecanizada para Instalação de Reservatórios e Caixas | m3 | 629,33 | R$ 60 | — | — | — | 🔴 Sem ref |
| Escavação mecanizada para blocos e baldrames, com previsao de forma | m3 | 284,82 | R$ 60 | R$ 58,58 | R$ 36 - 92 | 6 | 🟡 Média |
| Reaterro mecanizado para blocos e baldrames | m3 | 221,55 | R$ 12 | — | — | — | 🔴 Sem ref |
| Movimentação de terra para bota-fora de escavação | m3 | 63,27 | R$ 35 | — | — | — | 🔴 Sem ref |

### Infraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mão de obra para execução de concreto armado em infraestrutura | m3 | 40,43 | R$ 1.173 | — | — | — | 🔴 Sem ref |
| Lastro de concreto magro, aplicado em elementos de fundação, espessura | m2 | 120,06 | R$ 23 | — | — | — | 🔴 Sem ref |

### Supraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mão de obra para execução de concreto armado em supraestrutura | m3 | 50,86 | R$ 782 | R$ 290,00 | R$ 240 - 782 | 21 | 🟢 Alta |
| Concreto usinado bombeável, para piso, Fck 30MPa, abatimento 7 à 11cm, | m3 | 65,78 | R$ 490 | — | — | — | 🔴 Sem ref |
| Concreto usinado bombeável, para supraestrutura, Fck 30MPa, com Brita  | m3 | 50,86 | R$ 613 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 12,5 mm para alvenaria estrutural, cort | kg | 4.172,50 | R$ 7 | R$ 6,57 | R$ 7 - 7 | 4 | 🟡 Média |
| Concreto usinado bombeável, para infraestrutura, Fck 30MPa, incluindo  | m3 | 40,43 | R$ 575 | — | — | — | 🔴 Sem ref |
| Armação aço CA-60, tela soldada nervurada Q92 para supraestrutura, cor | m2 | 1.522,03 | R$ 14 | — | — | — | 🔴 Sem ref |
| Armação aço CA-60, tela soldada nervurada Q138 para supraestrutura, co | m2 | 657,83 | R$ 30 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 12,5 mm para radier, corte e dobra em i | kg | 1.698,00 | R$ 7 | — | — | — | 🔴 Sem ref |
| Concreto usinado bombeável, para enchimento, Fck 30MPa, com Brita 1, S | m3 | 15,14 | R$ 613 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 10,0 mm para supraestrutura, corte e do | kg | 1.223,00 | R$ 7 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 10,0 mm para alvenaria estrutural, cort | kg | 1.200,50 | R$ 7 | R$ 6,57 | R$ 7 - 7 | 4 | 🟡 Média |
| Armação aço CA-50, diâmetro de 10,0 mm para radier, corte e dobra em i | kg | 897,00 | R$ 7 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 6,3 mm para supraestrutura, corte e dob | kg | 558,00 | R$ 8 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 16,0 mm para supraestrutura, corte e do | kg | 433,50 | R$ 7 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 20,0 mm para supraestrutura, corte e do | kg | 306,00 | R$ 7 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 25,0 mm para supraestrutura, corte e do | kg | 283,50 | R$ 7 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 8,0 mm para supraestrutura, corte e dob | kg | 171,00 | R$ 8 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 12,5 mm para supraestrutura, corte e do | kg | 49,00 | R$ 7 | R$ 8,74 | R$ 8 - 10 | 375 | 🟢 Alta |

### Alvenaria

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Alvenaria estrutural de blocos de concreto (espessura 19cm) - 8MPa - E | m2 | 843,91 | R$ 70 | — | — | — | 🔴 Sem ref |
| Mão de obra para execução de alvenaria estrutural | m2 | 843,91 | R$ 47 | — | — | — | 🔴 Sem ref |
| Mão de obra para instalação de paredes com placa drywall | m2 | 516,95 | R$ 40 | — | — | — | 🔴 Sem ref |
| Graute para alvenaria estrutural - fgk 20MPa | m3 | 24,84 | R$ 504 | — | — | — | 🔴 Sem ref |
| Parede com sistema de chapas de Drywall duplo 70mm, placa standart e r | m2 | 32,05 | R$ 175 | — | — | — | 🔴 Sem ref |
| Verga/Contraverga de Concreto moldada in loco | m | 108,98 | R$ 59 | R$ 33,33 | R$ 29 - 57 | 154 | 🟢 Alta |
| Parede com sistema de chapas de Drywall 48mm, com Isolamento Acústico, | m2 | 30,18 | R$ 189 | — | — | — | 🔴 Sem ref |
| Parede com sistema de chapas de Drywall 70mm, placa standart (70/S) | m2 | 51,69 | R$ 90 | — | — | — | 🔴 Sem ref |
| Alvenaria de vedação de blocos cerâmicos furados na horizontal de 11,5 | m2 | 40,96 | R$ 49 | R$ 33,13 | R$ 29 - 69 | 18 | 🟢 Alta |
| Encunhamento com Expansor | m | 84,91 | R$ 16 | — | — | — | 🔴 Sem ref |
| Tela soldada para ligacao alvenaria/estrutura - para blocos de 9 a 14c | un | 105,00 | R$ 3 | R$ 3,10 | R$ 1 - 10 | 349 | 🟢 Alta |
| Parede com sistema de chapas de Drywall 48mm, placa standart (48/S) | m2 | 1,10 | R$ 73 | — | — | — | 🔴 Sem ref |

### Impermeabilização

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Impermeabilização em banheiro, áreas técnicas, cozinhas, terraços (Loc | m2 | 4.152,92 | R$ 48 | — | — | — | 🔴 Sem ref |
| Impermeabilização com manta asfáltica em arquibancadas, áreas comercia | m2 | 1.070,59 | R$ 178 | — | — | — | 🔴 Sem ref |
| Mão de obra impermeabilização com argamassa polimérica | m2 | 4.152,92 | R$ 30 | R$ 26,57 | R$ 16 - 30 | 72 | 🟢 Alta |
| Mão de obra impermeabilização com manta asfáltica | m2 | 1.194,45 | R$ 48 | R$ 70,00 | R$ 48 - 88 | 48 | 🟢 Alta |
| Impermeabilização com manta asfáltica em cozinhas (Local V) | m2 | 123,86 | R$ 94 | — | — | — | 🔴 Sem ref |
| Impermeabilização de piso e paredes com cimento polimérico e resina ac | m2 | 51,24 | R$ 106 | — | — | — | 🔴 Sem ref |
| Mão de obra impermeabilização de reservatório | m2 | 82,87 | R$ 36 | — | — | — | 🔴 Sem ref |
| Mão de obra para impermeabilização de peitoris | m2 | 43,88 | R$ 32 | R$ 32,00 | R$ 22 - 32 | 15 | 🟢 Alta |
| Impermeabilização de peitoris | m2 | 43,88 | R$ 26 | — | — | — | 🔴 Sem ref |
| Mão de obra para impermeabilização de poço de elevador com cristalizan | m2 | 51,40 | R$ 15 | — | — | — | 🔴 Sem ref |
| Impermeabilização em poço de elevador (Local II) | m2 | 51,40 | R$ 11 | — | — | — | 🔴 Sem ref |

### Instalações

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Quadro distrib. chapa pintada - embutir | pç | 112,00 | R$ 2.210 | — | — | — | 🔴 Sem ref |
| Interruptor DR 25A, 30mA, Tipo AC, bipolar | un | 14,00 | R$ 88 | — | — | — | 🔴 Sem ref |
| Eletroduto PVC flexível - Eletroduto leve - 3/4" | m | 23.784,70 | R$ 3 | — | — | — | 🔴 Sem ref |
| HIDRÔMETROS MULTIJATO CLASSE B DN25 (1") QN: 2,50 M³/H | un | 113,00 | R$ 863 | — | — | — | 🔴 Sem ref |
| Eletroduto PVC flexível - Eletroduto pesado - 1.1/4" | m | 8.052,00 | R$ 9 | — | — | — | 🔴 Sem ref |
| DPS Classe 2 275V/20kA Tripolar | un | 1,00 | R$ 401 | — | — | — | 🔴 Sem ref |
| Quadro de distribuição, 500x1000x120mm | un | 109,00 | R$ 730 | — | — | — | 🔴 Sem ref |
| TUBO PVC ESG SN DN100 | m | 4.289,45 | R$ 14 | — | — | — | 🔴 Sem ref |
| TUBO CPVC DN28 | m | 1.396,10 | R$ 41 | — | — | — | 🔴 Sem ref |
| Caixa de Luz 4''x4'', de embutir, em PVC para eletroduto corrugado | un | 46,00 | R$ 1.419 | R$ 1,72 | R$ 2 - 1419 | 4 | 🟡 Média |
| TUBO PVC SOLD DN 25 | m | 20.157,90 | R$ 3 | — | — | — | 🔴 Sem ref |
| Disjuntor Caixa Moldada Tripolar 90A, Curva C, 250/440V 6kA | un | 1,00 | R$ 307 | R$ 405,40 | R$ 173 - 534 | 14 | 🟢 Alta |
| TUBO CPVC DN22 | m | 2.111,30 | R$ 24 | — | — | — | 🔴 Sem ref |
| Mão de obra instalações SPDA | Unid. | 14.491,98 | R$ 4 | R$ 3,00 | R$ 3 - 4 | 10 | 🟢 Alta |
| Caixa de Passagem de sobrepor, 500x500x400mm, fabricado em PVC anticha | un | 57,00 | R$ 922 | — | — | — | 🔴 Sem ref |
| MISTURADOR MONOCOMANDO Ø3/4" | un | 206,00 | R$ 240 | — | — | — | 🔴 Sem ref |
| Disjuntor Tripolar Termomagnético -
norma DIN (Curva C) - 125 A - 10 k | pç | 27,00 | R$ 1.534 | R$ 213,58 | R$ 55 - 1629 | 24 | 🟢 Alta |
| Barramento Blindado BWW01-MA250J-54 | m | 142,00 | R$ 320 | — | — | — | 🔴 Sem ref |
| Quadro de destribuição varíavel | un | 76,00 | R$ 487 | — | — | — | 🔴 Sem ref |
| TUBO PVC ESG SR DN100 | m | 1.083,88 | R$ 28 | — | — | — | 🔴 Sem ref |

### Sistemas_Especiais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| PISCINA ADULTA 1 | 1.1999999999999993 | 61,92 | R$ 74 | — | — | — | 🔴 Sem ref |
| SDAI - Acionador manual + avisador audio visual de alarme | un | 37,00 | R$ 202 | — | — | — | 🔴 Sem ref |
| Pintura com tinta látex PVA em poços dos elevadores, 2 demãos | m2 | 1.594,49 | R$ 5 | — | — | — | 🔴 Sem ref |
| Revestimento de granito em piso do elevador | m2 | 12,35 | R$ 557 | — | — | — | 🔴 Sem ref |
| Gerador de Cloro à base sal com capacidade de gerar 20g de cloro puro  | un | 1,50 | R$ 4.170 | — | — | — | 🔴 Sem ref |
| PISCINA INFANTIL | 0.6500000000000004 | 7,62 | R$ 5 | — | — | — | 🔴 Sem ref |
| GERADOR DE COLORO BZ -20 | un | 1,50 | R$ 3.296 | R$ 3.296,12 | R$ 3296 - 3657 | 7 | 🟡 Média |
| MOTOBOMBA SYLLENT AUTO ESCORVANTE 1/3CV Mono | un | 4,00 | R$ 1.166 | R$ 1.499,00 | R$ 1166 - 1699 | 14 | 🟢 Alta |
| GERADOR DE COLORO BZ -30 | un | 1,00 | R$ 3.657 | R$ 3.296,12 | R$ 3296 - 3657 | 7 | 🟡 Média |
| MOTOBOMBA SYLLENT AUTO ESCORVANTE 3/4CV Mono | un | 2,00 | R$ 1.699 | R$ 1.499,00 | R$ 1166 - 1699 | 14 | 🟢 Alta |
| TAMPA ARTICULADA GDA 110X110cm CÓDIGO 3140 | un | 1,00 | R$ 3.200 | — | — | — | 🔴 Sem ref |
| Refletor em LED 20W RGB c/ ângulo 150º, encaixe em tubo de 25mm com ve | un | 7,00 | R$ 426 | — | — | — | 🔴 Sem ref |
| TAMPA GDA REBAIXADA C/ GRELHA 80X80cm CÓDIGO 3078 | un | 1,50 | R$ 1.850 | R$ 1.850,00 | R$ 1850 - 1850 | 6 | 🟡 Média |
| SDAI - Repetidora de central de alarme endereçavel | un | 2,00 | R$ 1.049 | — | — | — | 🔴 Sem ref |
| SDAI - Central de alarme endereçavel | un | 1,00 | R$ 2.069 | — | — | — | 🔴 Sem ref |
| Bomba 3/4 cv BM-75 p/ piscinas de até 78 mil litros
SODAMAR | un | 1,00 | R$ 1.603 | — | — | — | 🔴 Sem ref |
| Filtro para piscina FM-50 p/ até 78 mil litros
SODAMAR | un | 1,00 | R$ 1.443 | R$ 807,00 | R$ 714 - 978 | 10 | 🟢 Alta |
| MOTOBOMBA SODRAMAR BMP-25 | un | 2,00 | R$ 716 | — | — | — | 🔴 Sem ref |
| FILTRO SODRAMAR FM-36 – COM 40kg areia | un | 2,00 | R$ 714 | R$ 714,00 | R$ 714 - 714 | 6 | 🟡 Média |
| Coadeira modelo Padrão – Sodramar | un | 1,50 | R$ 785 | — | — | — | 🔴 Sem ref |

### Climatização

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Unidade Condensadora 36.000 BTU/h, LG ou similar | Unid. | 3,50 | R$ 4.500 | R$ 3.901,59 | R$ 1492 - 4500 | 7 | 🟡 Média |
| Unidade Evaporadora Hi wall, 36000 BTU/h, LG ou similar | Unid. | 3,50 | R$ 4.253 | R$ 3.311,42 | R$ 1625 - 4253 | 7 | 🟡 Média |
| Unidade Condensadora 24.000 BTU/h, LG ou similar | Unid. | 2,00 | R$ 3.902 | R$ 3.901,59 | R$ 1492 - 4500 | 7 | 🟡 Média |
| Unidade Evaporadora Hi wall, 24000 BTU/h, LG ou similar | Unid. | 2,00 | R$ 3.311 | R$ 3.311,42 | R$ 1625 - 4253 | 7 | 🟡 Média |
| Unidade Condensadora 12.000 BTU/h, LG ou similar | Unid. | 2,50 | R$ 1.918 | R$ 3.901,59 | R$ 1492 - 4500 | 7 | 🟡 Média |
| Unidade Evaporadora Hi wall, 12000 BTU/h, LG ou similar | Unid. | 2,50 | R$ 1.792 | R$ 3.311,42 | R$ 1625 - 4253 | 7 | 🟡 Média |
| Unidade Evaporadora Hi wall, 9000 BTU/h, LG ou similar | Unid. | 2,00 | R$ 1.625 | R$ 3.311,42 | R$ 1625 - 4253 | 7 | 🟡 Média |
| Rede frigorígena para Split de 9000Btu/h contendo: Linha de Líquido: T | m | 78,46 | R$ 40 | R$ 39,88 | R$ 40 - 40 | 19 | 🟢 Alta |
| Unidade Condensadora 9.000 BTU/h, LG ou similar | Unid. | 2,00 | R$ 1.492 | R$ 3.901,59 | R$ 1492 - 4500 | 7 | 🟡 Média |
| Unidade Condensadora 18.000 BTU/h, LG ou similar | Unid. | 1,00 | R$ 2.770 | R$ 3.901,59 | R$ 1492 - 4500 | 7 | 🟡 Média |
| Unidade Evaporadora Hi wall, 18000 BTU/h, LG ou similar | Unid. | 1,00 | R$ 2.357 | R$ 3.311,42 | R$ 1625 - 4253 | 7 | 🟡 Média |
| Rede frigorígena para Split de 18000Btu/h contendo: Linha de Líquido:  | m | 52,34 | R$ 40 | R$ 39,88 | R$ 40 - 40 | 19 | 🟢 Alta |
| Rede frigorígena para Split de 24000Btu/h contendo: Linha de Líquido:  | m | 42,23 | R$ 40 | R$ 39,88 | R$ 40 - 40 | 19 | 🟢 Alta |
| Rede frigorígena para Split de 36000Btu/h contendo: Linha de Líquido:  | m | 43,24 | R$ 40 | R$ 39,88 | R$ 40 - 40 | 19 | 🟢 Alta |
| Rede frigorígena para Split de 12000Btu/h contendo: Linha de Líquido:  | m | 28,75 | R$ 40 | R$ 39,88 | R$ 40 - 40 | 19 | 🟢 Alta |
| Caixa Polar | Unid. | 10,00 | R$ 23 | — | — | — | 🔴 Sem ref |

### Rev._Interno_Parede

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mão de obra para reboco interno, incluindo chapisco | m2 | 3.816,42 | R$ 69 | — | — | — | 🔴 Sem ref |
| Massa unica para reboco de teto em argamassa estabilizada - espessura  | m2 | 3.816,42 | R$ 16 | R$ 18,05 | R$ 16 - 18 | 13 | 🟢 Alta |
| Chapisco rolado aplicado em teto | m2 | 3.816,42 | R$ 6 | — | — | — | 🔴 Sem ref |
| Massa unica para reboco em argamassa estabilizada - espessura de 20mm | m2 | 783,97 | R$ 15 | — | — | — | 🔴 Sem ref |
| Chapisco de argamassa preparada em obra de cimento e areia traço 1:4 - | m2 | 783,97 | R$ 3 | R$ 2,84 | R$ 3 - 13 | 6 | 🟡 Média |

### Teto

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Forro de gesso acartonado em cozinhas | m2 | 1.044,71 | R$ 87 | — | — | — | 🔴 Sem ref |
| Forro de gesso acartonado em banheiros | m2 | 763,44 | R$ 97 | — | — | — | 🔴 Sem ref |
| Forro de gesso acartonado em áreas internas | m2 | 200,91 | R$ 87 | — | — | — | 🔴 Sem ref |

### Pisos

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Rodapé em madeira | m2 | 2.378,33 | R$ 60 | R$ 22,69 | R$ 11 - 60 | 8 | 🟡 Média |
| Mão de obra para colocação de rodapé em madeira | m | 2.378,33 | R$ 13 | — | — | — | 🔴 Sem ref |
| Mão de obra para execução de contrapiso e regularização | m2 | 1.054,16 | R$ 24 | — | — | — | 🔴 Sem ref |
| Rodapé em cerâmica Gail | m2 | 925,87 | R$ 21 | — | — | — | 🔴 Sem ref |
| Soleira em granito, acabamento polido, largura 35cm | m | 149,20 | R$ 102 | — | — | — | 🔴 Sem ref |
| Mão de obra para colocação de rodapé em porcelanato | m | 625,87 | R$ 22 | R$ 8,40 | R$ 8 - 22 | 16 | 🟢 Alta |
| Contrapiso comum em argamassa autonivelante, espessura 3cm | m2 | 146,91 | R$ 24 | — | — | — | 🔴 Sem ref |
| Mão de Obra colocalção de soleira de Granito | m | 14,92 | R$ 12 | — | — | — | 🔴 Sem ref |

### Pintura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mão de obra para pintura com tinta acrílica sobre argamassa | m2 | 23.331,36 | R$ 34 | — | — | — | 🔴 Sem ref |
| Pintura com tinta látex PVA em paredes internas, aplicação manual 2 de | m2 | 32.323,32 | R$ 6 | — | — | — | 🔴 Sem ref |
| Pintura com tinta látex acrílica em paredes externas, aplicação manual | m2 | 5.191,20 | R$ 6 | R$ 11,50 | R$ 6 - 20 | 8 | 🟡 Média |
| Pintura com tinta látex em teto, acabamento fosco, aplicação manual, 3 | m2 | 5.544,65 | R$ 5 | — | — | — | 🔴 Sem ref |
| Mão de obra para pintura com tinta hidrofugante | m2 | 846,15 | R$ 28 | — | — | — | 🔴 Sem ref |
| Pintura com tinta látex em gesso, acabamento fosco, aplicação manual,  | m2 | 2.009,06 | R$ 6 | — | — | — | 🔴 Sem ref |
| Pintura com tinta hidrofugante, aplicação manual, 2 demãos, em concret | m2 | 423,07 | R$ 19 | — | — | — | 🔴 Sem ref |
| Pintura Portas de Madeira da Entrada | un | 134,00 | R$ 23 | — | — | — | 🔴 Sem ref |

### Esquadrias

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Esquadria Fixa com Bandeira superior | m2 | 550,13 | R$ 2.281 | — | — | — | 🔴 Sem ref |
| Guarda-corpo em alumínio e vidro h=50cm | m2 | 336,43 | R$ 1.901 | R$ 990,00 | R$ 655 - 44550 | 42 | 🟢 Alta |
| Esquadria de alumínio Restaurante | m2 | 156,31 | R$ 3.041 | — | — | — | 🔴 Sem ref |
| Janela com caixilho translúcido 3 folhas, de correr em vidro transpare | un | 27,00 | R$ 9.305 | — | — | — | 🔴 Sem ref |
| Porta de madeira de abrir 82x210cm, fixação com espuma expansiva | un | 187,00 | R$ 1.007 | — | — | — | 🔴 Sem ref |
| Porta de madeira de abrir 72x210cm, fixação com espuma expansiva | un | 181,00 | R$ 1.006 | — | — | — | 🔴 Sem ref |
| Execução de contramarco de esquadrias de alumínio | m | 4.438,64 | R$ 33 | — | — | — | 🔴 Sem ref |
| Corrimão em alumínio | m | 379,07 | R$ 380 | — | — | — | 🔴 Sem ref |
| Janela com caixilho translúcido 2 folhas, de correr em vidro transpare | un | 13,50 | R$ 11.025 | — | — | — | 🔴 Sem ref |
| Guarda-corpo em alumínio e vidro h=60cm | m2 | 42,99 | R$ 1.901 | R$ 990,00 | R$ 655 - 44550 | 42 | 🟢 Alta |
| Porta corta-fogo em aço galvanizado P90 90x210cm | un | 33,00 | R$ 2.072 | — | — | — | 🔴 Sem ref |
| Janela com caixilho 7 folhas. 5 inferiores fixas e 2 superiores pivota | un | 27,00 | R$ 2.374 | — | — | — | 🔴 Sem ref |
| Janela com caixilho 4 folhas, 3 inferiores fixas e superior pivotante  | un | 36,00 | R$ 1.200 | — | — | — | 🔴 Sem ref |
| Janela com caixilho 6 folhas. 2 inferiores fixas e 4 superiores pivota | un | 20,00 | R$ 1.996 | — | — | — | 🔴 Sem ref |
| Mão de obra para instalação de corrimão de alumínio | m | 379,07 | R$ 67 | — | — | — | 🔴 Sem ref |
| Porta de madeira de abrir 62x210cm, fixação com espuma expansiva | un | 25,00 | R$ 1.006 | — | — | — | 🔴 Sem ref |
| Janela com caixilho 2 folhas de correr em vidro transparente e bandeir | un | 9,00 | R$ 3.570 | — | — | — | 🔴 Sem ref |
| Porta corta-fogo em aço galvanizado P90 100x210cm | un | 10,00 | R$ 2.183 | — | — | — | 🔴 Sem ref |
| Guarda-corpo em alumínio e vidro h=110cm | m2 | 6,97 | R$ 1.901 | R$ 990,00 | R$ 655 - 44550 | 42 | 🟢 Alta |
| Janela com caixilho folha superior maximar e bandeira inferior fixa em | un | 9,00 | R$ 1.409 | — | — | — | 🔴 Sem ref |

### Louças_e_Metais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Banheiro - Bacia Sanitária / Caixa Acoplada | un | 208,00 | R$ 830 | R$ 1.049,00 | R$ 708 - 1683 | 5 | 🟡 Média |
| Acabamento de Registro Comum | un | 585,00 | R$ 176 | — | — | — | 🔴 Sem ref |
| Kit bacia sanitaria | un | 210,00 | R$ 345 | — | — | — | 🔴 Sem ref |
| Bacia com caixa acoplada / Detalhe: Linha Living, branco, saída lado d | un | 105,00 | R$ 650 | R$ 1.624,90 | R$ 523 - 1625 | 15 | 🟢 Alta |
| Acabamento de Registro | un | 400,00 | R$ 90 | R$ 50,00 | R$ 50 - 50 | 90 | 🟢 Alta |
| Regulador De Pressão 2º Estágio Com Registro De Fecho Rápido | un | 115,00 | R$ 272 | — | — | — | 🔴 Sem ref |
| Misturador monocomando | un | 146,00 | R$ 170 | — | — | — | 🔴 Sem ref |
| Válvula reta com registro de Fecho Rápido 1/2'' BSP | un | 226,00 | R$ 28 | — | — | — | 🔴 Sem ref |
| Cuba Pia Cozinha - Lazer | un | 3,00 | R$ 1.981 | — | — | — | 🔴 Sem ref |
| Registro Globo Angular 2.1/2" | un | 35,00 | R$ 150 | R$ 96,00 | R$ 87 - 150 | 8 | 🟡 Média |
| Registro de Gaveta Industrial, Bronze - 2.1/2" | un | 12,00 | R$ 433 | — | — | — | 🔴 Sem ref |
| Lavatório suspenso \ Detalhe: Cuba viggo 54cm branca | un | 9,00 | R$ 450 | R$ 1.574,10 | R$ 450 - 1574 | 15 | 🟢 Alta |
| Banheiro - Bacia Sanitária PNE | un | 4,50 | R$ 937 | R$ 978,28 | R$ 708 - 1625 | 4 | 🟡 Média |
| Torneira Lavatório mesa | un | 13,50 | R$ 235 | R$ 350,00 | R$ 90 - 1055 | 5 | 🟡 Média |
| SHP - Bacia de contenção - 375 Litros - Abaixo do Tanque | un | 2,00 | R$ 1.259 | — | — | — | 🔴 Sem ref |
| GÁS - Registro de fecho rápido com caixa | un | 2,00 | R$ 1.099 | — | — | — | 🔴 Sem ref |
| Torneira para Lavatório\ Detalhe: Cromado Vercci | un | 18,00 | R$ 120 | R$ 1.054,93 | R$ 1055 - 1055 | 14 | 🟢 Alta |
| Banheiro - Cuba de Sobrepor - PNE | un | 2,00 | R$ 493 | R$ 492,89 | R$ 350 - 1813 | 3 | 🟡 Média |
| Cozinha - Cuba / Inox | un | 2,00 | R$ 433 | R$ 432,69 | R$ 250 - 2750 | 5 | 🟡 Média |
| Cozinha - Cuba Dupla / Inox | un | 1,00 | R$ 783 | — | — | — | 🔴 Sem ref |

### Fachada

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Revestimento interno de piso em pastilha porcelana | m2 | 559,81 | R$ 436 | — | — | — | 🔴 Sem ref |
| Revestimento interno de parede em pastilha Jatobá coleção natural 2,5x | m2 | 357,06 | R$ 443 | — | — | — | 🔴 Sem ref |
| Restauração de revestimento interno/externo de parede em pastilha porc | m2 | 2.438,66 | R$ 62 | — | — | — | 🔴 Sem ref |
| Mão de obra para colocação e rejuntamento de pastilha em parede | m2 | 1.790,51 | R$ 48 | — | — | — | 🔴 Sem ref |
| Tela de Proteção de Fachada | m2 | 5.026,27 | R$ 12 | — | — | — | 🔴 Sem ref |
| Revestimento interno/externo de parede em pastilha porcelana | m2 | 24,17 | R$ 436 | — | — | — | 🔴 Sem ref |

### Complementares

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Quadra Poliesportiva | — | 205,99 | R$ 1.168 | R$ 1.168,35 | R$ 1168 - 7848 | 3 | 🟡 Média |
| Espreguiçadeira Calhetas em Corda Pet Cinza | — | 8,00 | R$ 6.620 | — | — | — | 🔴 Sem ref |
| Esteira Profissional Adidas T-23 (T-23) - Adidas | — | 2,00 | R$ 25.172 | R$ 20.137,60 | R$ 20138 - 25172 | 10 | 🟢 Alta |
| Esteira Profissional Adidas T-23  (T-23) - Adidas | — | 2,00 | R$ 20.138 | R$ 20.137,60 | R$ 20138 - 25172 | 10 | 🟢 Alta |
| Cadeira Arco Encosto Estofado | — | 16,50 | R$ 1.939 | — | — | — | 🔴 Sem ref |
| Elíptico Adidas X-21 | — | 2,00 | R$ 14.490 | — | — | — | 🔴 Sem ref |
| Cadeira Paloma sem braçoNomade Home | — | 20,00 | R$ 1.390 | — | — | — | 🔴 Sem ref |
| Refrigerador Expositor Venax EXPVBL 330 Preto Fosco | — | 4,00 | R$ 6.890 | — | — | — | 🔴 Sem ref |
| Cadeira Com Almofada Em Corda Náutica Área Externa | — | 24,00 | R$ 811 | — | — | — | 🔴 Sem ref |
| Cadeira Palermo Scaburi | — | 7,50 | R$ 2.530 | — | — | — | 🔴 Sem ref |
| Mesa Lateral Deck Externa 50cm x 39cm | — | 7,00 | R$ 2.579 | — | — | — | 🔴 Sem ref |
| Espreguiçadeira de Madeira Tramontina em Jatobá Eco Blindage e Encosto | — | 8,00 | R$ 2.161 | — | — | — | 🔴 Sem ref |
| Banqueta com Braço Isis Estofada Encosto Detalhe em Madeira Estrutura  | — | 6,50 | R$ 2.178 | — | — | — | 🔴 Sem ref |
| Poltrona Nature | Área Externa | — | 2,00 | R$ 5.999 | — | — | — | 🔴 Sem ref |
| Painel Marcenaria | — | 13,92 | R$ 850 | — | — | — | 🔴 Sem ref |
| Cortina | — | 4,00 | R$ 2.900 | R$ 2.900,00 | R$ 2000 - 2900 | 21 | 🟢 Alta |
| Quadro Decorativo Abstrato Mar, Moldura Preta | — | 2,00 | R$ 5.589 | — | — | — | 🔴 Sem ref |
| Cadeira Soer Fixa 4 Pés Alta Azul | — | 8,00 | R$ 1.346 | — | — | — | 🔴 Sem ref |
| Futon Sofá Cama Casal Oriental Acquablock Branco Off | — | 6,00 | R$ 1.790 | — | — | — | 🔴 Sem ref |
| Lava e Seca Samsung WD11M com Digital Inverter WD11M4473PW Branca 11/7 | — | 3,00 | R$ 3.519 | — | — | — | 🔴 Sem ref |

## 📈 Comparação com Índices Derivados (Fase 13)

Totais esperados por macrogrupo baseados em 29 índices derivados de 126 projetos:

| Índice | Mediana | × AC = Esperado | Status |
|---|---|---|---|
| Concreto | R$ 229/m² | R$ 2.855.023 | n=64 |
| Aço | R$ 232/m² | R$ 2.891.426 | n=65 |
| Forma | R$ 165/m² | R$ 2.057.774 | n=69 |
| Escoramento | R$ 48/m² | R$ 594.642 | n=57 |
| Impermeabilização | R$ 265/m² | R$ 3.303.799 | n=95 |
| Elevadores | R$ 213/m² | R$ 2.660.850 | n=70 |
| Pintura | R$ 594/m² | R$ 7.414.666 | n=96 |
| Esquadrias | R$ 1154/m² | R$ 14.397.965 | n=96 |
| Louças | R$ 110/m² | R$ 1.369.011 | n=76 |

## 📋 Resumo de Rastreabilidade

- **Itens do executivo analisados:** 195
- **Com match na base de 4.210 PUs cross-projeto:** 67 (34% se total > 0)
- **Sem referência direta:** 128

## 🔗 Fontes e Arquivos

- **Quantitativos BIM consolidados:** `base/quantitativos-consolidados/arthen-arboris.json`
- **BIM raw:** `base/quantitativos-bim/arthen-arboris.json`
- **DXF raw:** `base/quantitativos-dxf/arthen-arboris.json`
- **PDF raw:** `base/quantitativos-pdf/arthen-arboris.json`
- **Executivo:** `base/pacotes/arthen-arboris/executivo-arthen-arboris.xlsx`
- **PUs cross-projeto:** `base/itens-pus-agregados.json` (4.210 clusters)
- **Índices derivados:** `base/indices-derivados-v2.json` (29 índices)
- **Base master:** `base/base-indices-master-2026-04-13.json`
