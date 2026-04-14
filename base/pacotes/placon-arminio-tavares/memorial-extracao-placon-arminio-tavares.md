# Memorial de Extração — placon-arminio-tavares

_Gerado em 13/04/2026 23:27 — Fase 17 (base enriquecida)_

Este documento detalha a **lógica de extração** de cada item do orçamento executivo, rastreando fontes de dados e lógica de precificação.

## 📊 Dados do Projeto

| Campo | Valor |
|---|---|
| **Slug** | `placon-arminio-tavares` |
| **AC (Área Construída)** | 4.077,29 m² |
| **UR (Unidades)** | 55 |
| **Padrão** | medio |

## 🏗 Quantitativos Extraídos do BIM

**Fontes:** 7 IFCs, 0 DXFs, 14 PDFs

### Alvenaria e Paredes (IfcWall)

- **Total de elementos:** 6684 paredes
- **Área total:** 42.741 m²
- **Comprimento total:** 19.007 m

**Por tipo:**

| Tipo (material + espessura) | Qtd | Área m² | Comp m | Exemplos no IFC |
|---|---|---|---|---|
| alvenaria_generica_17cm | 1372 | 15.524 | 5.614 | Basic Wall:SM-EXT-ALV-BE17   22cm-RE6/RI1 / Parede básica:SM-EXT-ALV-BE17   22cm |
| alvenaria_generica_14cm | 1348 | 10.032 | 3.296 | Basic Wall:SM-EXT-ALV-BE14   18cm-RE1/RE1 / Basic Wall:SM-INT-ALV-BE14   18cm-RI |
| alvenaria_generica_11cm | 3174 | 9.448 | 6.965 | Basic Wall:SM-EXT-ALV-BE11.5   15cm-RE1/RE1-RI5 / Basic Wall:SM-INT-ALV-BE11.5   |
| alvenaria_generica_9cm | 524 | 4.358 | 1.621 | Basic Wall:SM-INT-ALV-BE09+BE09  24cm-RI1/RI1 / Basic Wall:SM-INT-ALV-BE09+BE09  |
| outros_?cm | 93 | 1.976 | 655 | Basic Wall:SM-EST-CON-CN0 20cm / Basic Wall:SM-EST-CON-CN0   18cm |
| outros_10cm | 46 | 733 | 173 | Basic Wall:SM-EXT-MET-FACHADA VENTILADA 10CM / Parede básica:SM-EXT-MET-FACHADA  |
| outros_48cm | 86 | 466 | 141 | Basic Wall:SM-INT-DRW-MM48   10cm-RI1/RI1 / Parede básica:SM-INT-DRW-MM48   10cm |
| outros_5cm | 13 | 128 | 23 | Basic Wall:SM-EXT-MET-FACHADA ACM 5CM / Parede básica:SM-EXT-MET-FACHADA ACM 5CM |
| outros_3cm | 12 | 42 | 186 | VISTAS FORROS 3º PAVTO1:VISTAS FORROS 3º PAVTO / VISTAS FORROS 3º PAVTO2:VISTAS  |
| outros_11cm | 12 | 28 | 279 | VISTAS FORRO 11º PAVTO1:VISTAS FORRO 11º PAVTO / VISTAS FORRO 11º PAVTO2:VISTAS  |
| outros_1cm | 2 | 4 | 38 | VISTA DOS FORROS1:VISTA DOS FORROS |
| outros_2cm | 2 | 2 | 17 | VISTAS FORRO 2º PAVTO:VISTAS FORRO 2º PAVTO |

### Estrutura (lajes + vigas + pilares)

| Elemento | Quantidade | Volume m³ | Comprimento/Altura m | Fonte |
|---|---|---|---|---|
| Lajes (IfcSlab) | 917 | 7.673,3 | área 47.245 m² | BIM IfcSlab |
| Vigas (IfcBeam) | 736 | 421,5 | 2.383 | BIM IfcBeam |
| Pilares (IfcColumn) | 193 | 613,6 | 534 | BIM IfcColumn |

- **Concreto total estimado (BIM):** 8.708,3 m³
- **Índice concreto/m² AC:** 2,136 m³/m² (vs mediana base 0,34) 🔴 delta +528%

### Esquadrias e Aberturas

- **Portas (IfcDoor):** 1608 unidades
- **Janelas (IfcWindow):** 889 unidades
- **Pele de vidro (IfcCurtainWall):** 370 elementos, 0 m²
- **Guarda-corpos (IfcRailing):** 340 elementos, 1.321 m

**Top 10 tipos de porta:**

- **SM-SOL:Soleira**: 303 un
- **SM-POR-MAD-1 Folha Abrir:090x210cm**: 228 un
- **SM-POR-MAD-1 Folha Abrir:070x210cm**: 220 un
- **SM-POR-ALU-2 Folhas Abrir-Veneziana:100x080cm**: 156 un
- **SM-POR-ELV-2 Folhas Correr:080x210cm**: 96 un
- **SM-PJA-ALU-X Folhas Correr-1 Direção:2 Folhas-240x220cm-Vidr**: 84 un
- **SM-POR-ALU-1 Folha Abrir-Veneziana:050x150cm   C/ Estrutura **: 83 un
- **SM-PJA-ALU-X Folhas Correr-1 Direção:2 Folhas-180x220cm-Vidr**: 80 un
- **SM-POR-PCI-1 Folha Abrir:090x210cm**: 60 un
- **SM-POR-PCI-1 Folha Abrir:080x210cm**: 60 un

**Top 10 tipos de janela:**

- **SM-JAN-Pingadeira:Pingadeira**: 335 un
- **SM-JAN-ALU-X Folhas Correr-1 Direção- X Folhas Fixas Inf:3 F**: 184 un
- **SM-JAN-ALU-X Folhas Maximar:1 Folha-060x060cm-Vidro 8mm**: 160 un
- **SM-JAN-VEN-ALU-1 Folha Fixa-Tela Aramada:92,5x100cm**: 112 un
- **SM-JAN-ALU-X Folhas Fixas:3 Folhas-240x200cm-Vidro 8mm**: 48 un
- **SM-JAN-ALU-X Folhas Maximar - X Folhas Fixas Inf:2 Folhas(1-**: 24 un
- **SM-JAN-ALU-X Folhas Fixas:3 Folhas-300x210cm-Vidro 8mm**: 8 un
- **SM-JAN-ALU-X Folhas Fixas:3 Folhas-240x210cm-Vidro 8mm**: 4 un
- **SM-JAN-VID-Porta padrão dimas:50x100**: 4 un
- **SM-JAN-VEN-ALU-1 Folha Fixa-Tela Aramada1:125x075cm**: 4 un

### Ambientes (IfcSpace)

- **Total:** 4 ambientes
- **Área total:** 413 m²
- **Volume total:** 1.653 m³

**Top 15 tipos de ambiente por área:**

| Ambiente | Qtd | Área m² |
|---|---|---|
| Ambiente | 4 | 413 |

## 💰 Orçamento Executivo — Lógica de Extração por Item

Cada item abaixo mostra: descrição, PU usado, PU base cross-projeto (se disponível), faixa P10-P90 e fonte.

### Gerenciamento

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Alvarás, Licenças e Taxas de Aprovação * | m2 | 3.972,30 | R$ 3 | — | — | — | 🔴 Sem ref |

### Movimentação_de_Terra

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Aterro com material externo * | m3 | 1.296,71 | R$ 9 | — | — | — | 🔴 Sem ref |
| Reaterro mecanizado de valas, com retroescavadeira * | m3 | 175,62 | R$ 22 | — | — | — | 🔴 Sem ref |

### Infraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Movimentação de terra para bota-fora - sapatas e vigas* | m3 | 5.520,25 | R$ 15 | — | — | — | 🔴 Sem ref |
| Fabricação, montagem e desmontagem de fôrma para viga baldrame, em cha | m2 | 591,31 | R$ 57 | — | — | — | 🔴 Sem ref |
| Escavação mecanizada para blocos de fundação e vigas baldrame, com pre | m3 | 411,00 | R$ 79 | R$ 34,84 | R$ 13 - 39 | 12 | 🟢 Alta |
| Fabricação, montagem e desmontagem de fôrma para sapata, em chapa de m | m2 | 456,32 | R$ 54 | R$ 60,63 | R$ 53 - 195 | 4 | 🟡 Média |

### Supraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Concreto usinado bombeável, para supraestrutura, fck 30MPa, slump = 16 | m3 | 1.177,33 | R$ 688 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 6,3mm para supraestrutura, corte e dobr | kg | 13.244,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 12,5mm para supraestrutura, corte e dob | kg | 13.517,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Concreto usinado bombeável, para blocos, sapatas e baldrames, fck 30 M | m3 | 146,31 | R$ 680 | — | — | — | 🔴 Sem ref |
| Armação aço CA-50, diâmetro de 10,0mm para supraestrutura, corte e dob | kg | 12.605,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 8,0mm para supraestrutura, corte e dobr | kg | 11.840,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-60, diâmetro de 5,0mm para supraestrutura, corte e dobr | kg | 10.793,00 | R$ 9 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 16,0mm para supraestrutura, corte e dob | kg | 11.859,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 25,0mm para supraestrutura, corte e dob | kg | 6.827,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 20,0mm para supraestrutura, corte e dob | kg | 6.176,00 | R$ 8 | R$ 8,96 | R$ 7 - 11 | 630 | 🟢 Alta |
| Escoramento com pontalete de madeira de eucalipto * | m2 | 5.004,20 | R$ 5 | R$ 20,75 | R$ 13 - 42 | 20 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 12,5mm para blocos, sapatas e baldrames | kg | 2.824,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 16,0mm para blocos, sapatas e baldrames | kg | 2.281,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 20,0mm para blocos, sapatas e baldrames | kg | 2.042,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 25,0mm para blocos, sapatas e baldrames | kg | 1.262,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 10,0mm para blocos, sapatas e baldrames | kg | 1.189,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-60, diâmetro de 5,0mm para blocos, sapatas e baldrames, | kg | 647,00 | R$ 9 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 6,3mm para blocos, sapatas e baldrames, | kg | 219,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |
| Armação aço CA-50, diâmetro de 8,0mm para blocos, sapatas e baldrames, | kg | 150,00 | R$ 8 | R$ 7,60 | R$ 7 - 8 | 29 | 🟢 Alta |

### Alvenaria

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Alvenaria de vedação de tijolos 9 furos (baiano) 11,5x19x19, com argam | m2 | 1.474,20 | R$ 42 | R$ 27,38 | R$ 27 - 36 | 5 | 🟡 Média |
| Verga/contraverga de concreto, moldada in loco* | m | 858,53 | R$ 42 | R$ 33,33 | R$ 29 - 57 | 154 | 🟢 Alta |
| Alvenaria de vedação de tijolos 6 furos (baiano) 09x14x19cm (espessura | m2 | 741,48 | R$ 31 | R$ 25,45 | R$ 25 - 31 | 5 | 🟡 Média |
| Chapisco interno argamassa cimento e areia (1:3), aplicado em alvenari | m2 | 6.650,63 | R$ 2 | R$ 1,64 | R$ 1 - 2 | 65 | 🟢 Alta |
| Tela soldada para ligação alvenaria/estrutura em chapisco externo 7,5x | m2 | 1.285,56 | R$ 12 | R$ 25,07 | R$ 2 - 26 | 56 | 🟢 Alta |
| Tela soldada para ligação alvenaria/estrutura em reboco e emboço inter | m2 | 1.169,00 | R$ 12 | — | — | — | 🔴 Sem ref |
| Chapisco externo de argamassa preparada em obra de cimento e areia, tr | m2 | 1.897,42 | R$ 6 | R$ 1,84 | R$ 2 - 5 | 42 | 🟢 Alta |
| Tela soldada para ligacao alvenaria/estrutura - para blocos de 9 a 14  | un | 2.348,00 | R$ 4 | R$ 3,10 | R$ 1 - 10 | 349 | 🟢 Alta |
| Encunhamento de alvenaria de vedação com argamassa expansiva * | m | 2.054,10 | R$ 1 | R$ 2,37 | R$ 2 - 8 | 221 | 🟢 Alta |

### Impermeabilização

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Impermeabilização com argamassa polimérica impermeabilizante, 3 demãos | m2 | 927,91 | R$ 104 | R$ 36,26 | R$ 8 - 36 | 12 | 🟢 Alta |
| Mão de obra para impermeabilização com argamassa polimérica * | m2 | 846,68 | R$ 45 | R$ 26,57 | R$ 16 - 30 | 72 | 🟢 Alta |
| Impermeabilização de Baldrames (Hidroasfalto) * | m2 | 591,31 | R$ 52 | — | — | — | 🔴 Sem ref |
| Impermeabilização Reservatório com Argamassa Polimérica | m2 | 137,64 | R$ 130 | — | — | — | 🔴 Sem ref |
| Mão de obra para impermeabilização de vigas baldrame * | m2 | 591,31 | R$ 21 | — | — | — | 🔴 Sem ref |
| Regularização de superfície para impermeabilização * | m2 | 1.265,72 | R$ 8 | R$ 5,57 | R$ 3 - 8 | 176 | 🟢 Alta |
| Mão de obra para impermeabilização de manta asfáltica * | m2 | 182,16 | R$ 49 | R$ 70,00 | R$ 48 - 88 | 48 | 🟢 Alta |
| Mão de obra empreitada para execução de proteção mecânica em superfíci | m2 | 182,16 | R$ 38 | R$ 31,75 | R$ 32 - 32 | 22 | 🟢 Alta |
| Impermeabilização com manta asfáltica espessura 4mm, uma camada, aplic | m2 | 100,94 | R$ 60 | R$ 93,41 | R$ 50 - 180 | 30 | 🟢 Alta |
| Selador impermeabilizante, aplicação em paredes externas, 1 demão * | m2 | 1.958,59 | R$ 2 | R$ 1,17 | R$ 1 - 2 | 5 | 🟡 Média |
| Impermeabilização Cisterna com Argamassa Polimérica | m2 | 90,88 | R$ 32 | — | — | — | 🔴 Sem ref |
| Impermeabilização com manta líquida * | m2 | 50,66 | R$ 51 | — | — | — | 🔴 Sem ref |
| Mão de obra empreitada para execução de Impermeabilização Cisterna com | m2 | 49,61 | R$ 45 | R$ 16,50 | R$ 16 - 16 | 15 | 🟢 Alta |
| Mão de obra para impermeabilização de peitoris com manta líquida * | m2 | 50,66 | R$ 36 | R$ 25,00 | R$ 12 - 32 | 135 | 🟢 Alta |
| Impermeabilização de Poço de Elevador * | m2 | 8,35 | R$ 33 | R$ 18,70 | R$ 19 - 33 | 4 | 🟡 Média |

### Instalações

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| AUTOMAÇÃO - Persiana Motorizada | pç | 4,00 | R$ 3.022 | R$ 3.021,80 | R$ 3022 - 3022 | 5 | 🟡 Média |
| Válvula redutora de pressão: 42LP 1.1/4" - BERMAD - ø32xø32 | pç | 2,00 | R$ 4.738 | — | — | — | 🔴 Sem ref |
| PEAD - Polietileno de Alta Densidade - 1.1/2" | m | 261,31 | R$ 29 | R$ 11,38 | R$ 3 - 44 | 9 | 🟡 Média |
| Filtro T compact 2" - BERMAD - ø50xø50 | pç | 1,50 | R$ 4.779 | — | — | — | 🔴 Sem ref |
| Caixa Sifonada com Grelha e Porta Grelha Redondos com 3 Entradas - DN  | pç | 70,00 | R$ 100 | — | — | — | 🔴 Sem ref |
| PEAD - Polietileno de Alta Densidade - 2" | m | 89,30 | R$ 44 | R$ 11,38 | R$ 3 - 44 | 9 | 🟡 Média |
| CAIXA DE PASSAGEM - PISO - Tampa 90x70 - B125 - Padrão CELESC | pç | 2,50 | R$ 1.640 | — | — | — | 🔴 Sem ref |
| Conforme apresentado no Esquema Vertical - ESQUEMA VERTICAL ( AQUA-UP- | pç | 2,00 | R$ 1.500 | — | — | — | 🔴 Sem ref |
| TOMADAS DE TELEFONE, TV E DADOS - Dock de Som | pç | 2,00 | R$ 1.500 | — | — | — | 🔴 Sem ref |
| Registro de gaveta Industrial 2 1/2" - DocolBásicos - ø75xø75 | pç | 9,00 | R$ 293 | — | — | — | 🔴 Sem ref |
| XLPE - 1kV (Prysmian) - 120 mm² - Azul claro | m | 78,40 | R$ 25 | — | — | — | 🔴 Sem ref |
| XLPE - 1kV (Prysmian) - 120 mm² - Branco | m | 78,40 | R$ 25 | — | — | — | 🔴 Sem ref |
| XLPE - 1kV (Prysmian) - 120 mm² - Preto | m | 78,40 | R$ 25 | — | — | — | 🔴 Sem ref |
| XLPE - 1kV (Prysmian) - 120 mm² - Vermelho | m | 78,40 | R$ 25 | — | — | — | 🔴 Sem ref |
| QUADRO DE DISTRIBUIÇÃO CARREGADOR VEICULAR - 1800X800X250 até 30 | pç | 1,00 | R$ 2.500 | — | — | — | 🔴 Sem ref |
| CAIXA DE PASSAGEM - PISO - Tampa 65x45 - R1 | pç | 4,00 | R$ 560 | — | — | — | 🔴 Sem ref |
| Válvula redutora de pressão 42LP - 3/4" - ø20xø20 | pç | 1,00 | R$ 1.985 | — | — | — | 🔴 Sem ref |
| Filtro de água pluvial: ACQUASAVE VF1 - ø150xø100xø150xø100 | pç | 1,00 | R$ 1.980 | — | — | — | 🔴 Sem ref |
| PVC - 750V (Prysmian) - 2.5 mm² - Azul claro | m | 418,94 | R$ 3 | R$ 6,22 | R$ 3 - 8 | 52 | 🟢 Alta |
| PEAD - Polietileno de Alta Densidade - Fita Sinalizadora de Conduto de | m | 63,40 | R$ 23 | — | — | — | 🔴 Sem ref |

### Sistemas_Especiais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Fechamento removível de abertura no piso do elevador em madeira | m2 | 16,93 | R$ 3.829 | R$ 88,62 | R$ 57 - 3829 | 7 | 🟡 Média |
| Acabamento em granito em piso de elevador * | m2 | 21,44 | R$ 455 | — | — | — | 🔴 Sem ref |
| Mão de obra empreitada para regularização e pintura do fosso do elevad | m2 | 101,28 | R$ 20 | R$ 15,50 | R$ 16 - 16 | 25 | 🟢 Alta |
| Fechamento removível de vãos de porta de elevador em madeira * | m2 | 12,18 | R$ 61 | R$ 45,45 | R$ 26 - 90 | 20 | 🟢 Alta |
| Pintura com tinta látex acrílica em fosso do elevador, 1 demão * | m2 | 101,28 | R$ 5 | R$ 2,25 | R$ 2 - 2 | 52 | 🟢 Alta |

### Climatização

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Instalação de Exaustor tipo Vento Kit * | un | 55,00 | R$ 222 | — | — | — | 🔴 Sem ref |
| Ar condicionado Split 18.000 BTU/H - 18.000 BTU/h | pç | 1,00 | R$ 4.299 | — | — | — | 🔴 Sem ref |
| Ar condicionado Split 12.000 BTU/H - 12.000 BTU/h | pç | 1,00 | R$ 3.139 | — | — | — | 🔴 Sem ref |
| Terminal de ventilação ciruclar plastico 100mm - 100 | pç | 2,00 | R$ 995 | R$ 995,00 | R$ 995 - 995 | 5 | 🟡 Média |
| Renovador de ar 100mm - 100mm | pç | 2,00 | R$ 405 | R$ 404,99 | R$ 405 - 405 | 5 | 🟡 Média |
| Tubo de Cobre Flexível para Ar Condicionado (L) - 1/4" | m | 48,49 | R$ 14 | R$ 17,85 | R$ 14 - 28 | 20 | 🟢 Alta |
| Tubo de Cobre Flexível para Ar Condicionado (S) - 1/2" | m | 29,94 | R$ 25 | R$ 17,85 | R$ 14 - 28 | 20 | 🟢 Alta |
| Eletroduto Flexível Tipo Leve - 3/4" | m | 68,83 | R$ 3 | R$ 2,72 | R$ 1 - 4 | 157 | 🟢 Alta |
| Tubo - PVC Esgoto - Série Normal - 100 | m | 13,27 | R$ 13 | R$ 19,77 | R$ 13 - 45 | 64 | 🟢 Alta |
| Ar Condicionado | Ar Condicionado | 32.094,94 | R$ 105 | — | — | — | 🔴 Sem ref |
| Isolamento Térmico (S) - 12 mm | m | 48,54 | R$ 2 | R$ 1,68 | R$ 1 - 2 | 22 | 🟢 Alta |
| Isolamento Térmico (L) - 6 mm | m | 48,54 | R$ 1 | R$ 1,68 | R$ 1 - 2 | 22 | 🟢 Alta |
| Isolamento Térmico (S) - 18 mm | m | 27,09 | R$ 2 | R$ 1,68 | R$ 1 - 2 | 22 | 🟢 Alta |
| Joelho 90º - ø100xø100 | pç | 3,00 | R$ 8 | R$ 14,13 | R$ 8 - 14 | 22 | 🟢 Alta |
| Isolamento Térmico (L) - 10 mm | m | 27,09 | R$ 2 | R$ 1,68 | R$ 1 - 2 | 22 | 🟢 Alta |
| Caixa de passagem: 24.000 BTU/H - 24.000 BTU/h | pç | 2,00 | R$ 19 | R$ 15,73 | R$ 8 - 19 | 12 | 🟢 Alta |
| Caixa de passagem: 12.000 BTU/H - 12.000 BTU/h | pç | 4,00 | R$ 8 | R$ 15,73 | R$ 8 - 19 | 12 | 🟢 Alta |
| Luva Simples 100mm, Esgoto Série Normal - TIGRE - ø100xø100 | pç | 3,00 | R$ 5 | R$ 5,04 | R$ 5 - 5 | 15 | 🟢 Alta |
| Luva Soldável com Rosca 25 x 1/2'' - ø25xø20 | pç | 7,00 | R$ 4 | R$ 2,57 | R$ 1 - 4 | 10 | 🟢 Alta |
| Caixa de passagem: 30.000 BTU/H - 30.000 BTU/h | pç | 1,00 | R$ 23 | R$ 15,73 | R$ 8 - 19 | 12 | 🟢 Alta |

### Rev._Interno_Parede

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Chapisco interno de argamassa pré-fabricada adesiva de cimento colante | m2 | 1.662,66 | R$ 15 | R$ 6,34 | R$ 6 - 6 | 11 | 🟢 Alta |
| Chapisco externo de argamassa preparada em obra de cimento e areia, tr | m2 | 474,35 | R$ 6 | R$ 4,27 | R$ 4 - 6 | 5 | 🟡 Média |
| Chapisco de argamassa preparada em obra de cimento e areia, traço 1:4, | m2 | 195,83 | R$ 6 | R$ 0,56 | R$ 0 - 4 | 26 | 🟢 Alta |

### Teto

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Forro de gesso liso, aplicação em áreas secas e molhadas - material e  | m2 | 2.355,51 | R$ 55 | R$ 38,39 | R$ 36 - 54 | 22 | 🟢 Alta |

### Pisos

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Revestimento interno de piso porcelanato, placa 90x90cm | m2 | 1.921,94 | R$ 72 | — | — | — | 🔴 Sem ref |
| Rodapé em poliestireno, altura 7 cm* | m | 2.635,76 | R$ 21 | R$ 38,56 | R$ 39 - 39 | 17 | 🟢 Alta |
| Piso Laminado de Madeira * | m2 | 676,44 | R$ 72 | R$ 67,15 | R$ 67 - 72 | 4 | 🟡 Média |
| Contrapiso comum em argamassa estabilizada, aderida, espessura 4cm * | m2 | 1.301,77 | R$ 36 | R$ 21,45 | R$ 15 - 59 | 88 | 🟢 Alta |
| Revestimento em porcelanato amadeirado em parede externa, incluindo re | m2 | 116,56 | R$ 133 | R$ 138,83 | R$ 124 - 145 | 4 | 🟡 Média |
| Soleira em granito polido, largura 20cm, aplicação em áreas privativas | m2 | 21,59 | R$ 473 | R$ 477,06 | R$ 473 - 477 | 4 | 🟡 Média |
| Rodapé cerâmico, altura 7 cm, com placa 90x90, aplicação em sacadas e  | m | 90,13 | R$ 14 | R$ 6,46 | R$ 6 - 14 | 5 | 🟡 Média |

### Pintura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Pintura com tinta látex acrílica em paredes internas, acabamento fosco | m2 | 6.856,52 | R$ 8 | R$ 4,99 | R$ 3 - 7 | 130 | 🟢 Alta |
| Mão de obra empreitada para pintura com tinta látex acrílica em demarc | m2 | 2.816,90 | R$ 14 | — | — | — | 🔴 Sem ref |
| Pintura epóxi em piso, aplicação manual, 2 demãos * | m2 | 1.119,00 | R$ 42 | R$ 25,36 | R$ 3 - 88 | 43 | 🟢 Alta |
| Pintura com tinta látex acrílica em teto, acabamento fosco, 2 demãos * | m2 | 3.675,21 | R$ 9 | R$ 5,64 | R$ 4 - 9 | 84 | 🟢 Alta |
| Selador acrílico em paredes, 1 demão * | m2 | 7.320,48 | R$ 4 | R$ 4,26 | R$ 4 - 4 | 7 | 🟡 Média |
| Pintura com tinta látex acrílica em paredes externas, 2 demãos, cor ci | m2 | 1.958,59 | R$ 12 | R$ 41,84 | R$ 6 - 45 | 17 | 🟢 Alta |
| Mão de obra empreitada para aplicação de pintura epóxi em piso, 2 demã | m2 | 1.119,00 | R$ 20 | R$ 12,80 | R$ 13 - 13 | 11 | 🟢 Alta |
| Mão de obra empreitada para aplicação de fundo selador em paredes inte | m2 | 3.675,21 | R$ 5 | R$ 2,35 | R$ 2 - 5 | 7 | 🟡 Média |
| Selador acrílico em teto, 1 demão * | m2 | 3.675,21 | R$ 4 | R$ 4,62 | R$ 4 - 5 | 7 | 🟡 Média |
| Pintura tinta látex acrílica em parede de demarcação de vagas, aplicaç | m2 | 362,68 | R$ 8 | — | — | — | 🔴 Sem ref |
| Pintura epóxi em piso para demarcação de faixa de garagem, aplicação m | m | 43,26 | R$ 20 | R$ 39,46 | R$ 13 - 60 | 16 | 🟢 Alta |
| Mão de obra empreitada para pintura de faixas de demarcação de garagem | m | 43,26 | R$ 15 | R$ 14,00 | R$ 2 - 19 | 26 | 🟢 Alta |

### Esquadrias

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Kit porta de abrir de madeira, folha leve/média, 70x210cm, fixação com | un | 77,00 | R$ 729 | R$ 1.517,47 | R$ 729 - 1517 | 4 | 🟡 Média |
| Kit porta de abrir de madeira, folha leve/média, 80x210cm, fixação com | un | 55,00 | R$ 729 | R$ 1.517,47 | R$ 729 - 1517 | 4 | 🟡 Média |
| Kit porta de abrir de madeira, folha leve/média, 90x210cm, fixação com | un | 30,00 | R$ 803 | R$ 1.517,47 | R$ 803 - 1517 | 5 | 🟡 Média |
| Contramarco de alumínio, fixação com argamassa, incluso mão de obra | m | 995,28 | R$ 15 | R$ 19,01 | R$ 17 - 91 | 110 | 🟢 Alta |
| Porta Corta Fogo 0.90x2.10m Completa | un | 7,00 | R$ 1.250 | — | — | — | 🔴 Sem ref |

### Louças_e_Metais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Bacia com caixa acoplada / Detalhe: Linha Izy, Bacia: P.111.17, caixa: | un | 27,00 | R$ 1.090 | R$ 1.090,00 | R$ 750 - 1090 | 4 | 🟡 Média |
| Bacia Sanitaria para PNE - com caixa acoplada | un | 2,50 | R$ 1.279 | R$ 808,21 | R$ 808 - 1148 | 63 | 🟢 Alta |
| Bacia Sanitária com caixa acoplada | un | 1,00 | R$ 1.148 | R$ 808,21 | R$ 808 - 1148 | 63 | 🟢 Alta |
| Bacia Sanitária p/ PNE com Caixa Montana | un | 1,00 | R$ 1.337 | R$ 1.337,11 | R$ 808 - 1337 | 13 | 🟢 Alta |
| Registro de gaveta Industrial 2 1/2" - DocolBásicos - ø65xø65 | pç | 2,00 | R$ 297 | — | — | — | 🔴 Sem ref |
| Torneira De Mesa Cozinha Bica Móvel Gali 00801306 Docol | un | 3,00 | R$ 196 | R$ 196,00 | R$ 196 - 196 | 5 | 🟡 Média |
| Torneira Bica Alta 1/4 de volta | un | 1,00 | R$ 196 | R$ 196,00 | R$ 196 - 196 | 39 | 🟢 Alta |
| Acabamento de Registro | un | 3,00 | R$ 50 | R$ 50,00 | R$ 50 - 50 | 90 | 🟢 Alta |
| Acabamento de Registro / Detalhe: Linha: C71 - Ref: C71 - ORION | un | 2,50 | R$ 60 | R$ 60,00 | R$ 60 - 60 | 5 | 🟡 Média |
| Tampo de Granito com cuba -120 x50cm | un | 1,00 | R$ 567 | R$ 495,41 | R$ 360 - 495 | 36 | 🟢 Alta |
| Torneira para lavatório | un | 1,00 | R$ 50 | R$ 50,00 | R$ 50 - 50 | 50 | 🟢 Alta |
| Acabamento de Registro  PNE | un | 1,00 | R$ 60 | R$ 60,00 | R$ 60 - 60 | 16 | 🟢 Alta |

### Fachada

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Revestimento de Fachada com Pedra * | m2 | 210,89 | R$ 216 | — | — | — | 🔴 Sem ref |

### Complementares

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Calçada em basalto | m2 | 325,77 | R$ 169 | — | — | — | 🔴 Sem ref |
| Espreguiçadeira Brisa Estofado Navy Base Alumínio Taupe - 75469 - Sun  | — | 4,00 | R$ 5.205 | — | — | — | 🔴 Sem ref |
| Cortina | — | 5,00 | R$ 2.900 | R$ 2.900,00 | R$ 2000 - 2900 | 21 | 🟢 Alta |
| Acabamentos Especiais | — | 38,03 | R$ 450 | R$ 450,00 | R$ 225 - 450 | 75 | 🟢 Alta |
| ESTANTE PARA DUMBELL 10 PARES (TAC 043) - TITANIUM ESSENTIAL | — | 2,00 | R$ 5.100 | — | — | — | 🔴 Sem ref |
| Poltrona Externa Lunna - Wood | — | 2,00 | R$ 4.774 | — | — | — | 🔴 Sem ref |
| Cadeira Leme com Detalhe em Recouro e Braços, em Madeira Maciça | — | 8,00 | R$ 1.158 | — | — | — | 🔴 Sem ref |
| Conjunto com Mesa Ripada + 4 Cadeiras de Jardim e Piscina + Ombrelone  | — | 2,00 | R$ 4.598 | — | — | — | 🔴 Sem ref |
| Cadeira Área Externa de Alumínio Carmy com Corda Naútica Grafite/Amênd | — | 10,00 | R$ 891 | — | — | — | 🔴 Sem ref |
| Mesa Dobravel Quadrada Primavera Stain Castanho 90cm - 34793 Sun House | — | 5,00 | R$ 1.485 | — | — | — | 🔴 Sem ref |
| Calçada em paver | m2 | 89,85 | R$ 82 | — | — | — | 🔴 Sem ref |
| Cadeira de Aço Carbono Estofada Moderna Logos Bouclê Off White / Cinza | — | 6,00 | R$ 1.115 | — | — | — | 🔴 Sem ref |
| Kit 10 pares de halteres emb. De 1 a 10 KG (Kit H 10) - FIT4 | — | 2,00 | R$ 3.265 | R$ 3.938,32 | R$ 2612 - 4612 | 4 | 🟡 Média |
| Poltronas Decorativas Para Sala De Estar Base Fixa Londres L02 Bouclê  | — | 8,00 | R$ 745 | — | — | — | 🔴 Sem ref |
| Poltrona Delgada - Lider Interiores | — | 2,00 | R$ 2.890 | — | — | — | 🔴 Sem ref |
| Piso de borracha para playground | — | 17,06 | R$ 300 | — | — | — | 🔴 Sem ref |
| Mesa Bouman Solo Concreto & Granilite | uso área externo | — | 1,00 | R$ 5.000 | — | — | — | 🔴 Sem ref |
| Forno Elétrico de Embutir Brastemp 67L Inox com Função Ar Forçado e Pa | — | 1,00 | R$ 4.892 | — | — | — | 🔴 Sem ref |
| Banqueta Alta de Madeira Palla Estofada com Braços - (IMC) Branco | — | 3,00 | R$ 1.627 | — | — | — | 🔴 Sem ref |
| Mesa de Jantar Orgânica Cloe de Madeira com Tampo de Vidro | — | 1,00 | R$ 4.738 | — | — | — | 🔴 Sem ref |

## 📈 Comparação com Índices Derivados (Fase 13)

Totais esperados por macrogrupo baseados em 29 índices derivados de 126 projetos:

| Índice | Mediana | × AC = Esperado | Status |
|---|---|---|---|
| Concreto | R$ 229/m² | R$ 933.278 | n=64 |
| Aço | R$ 232/m² | R$ 945.178 | n=65 |
| Forma | R$ 165/m² | R$ 672.665 | n=69 |
| Escoramento | R$ 48/m² | R$ 194.382 | n=57 |
| Impermeabilização | R$ 265/m² | R$ 1.079.978 | n=95 |
| Elevadores | R$ 213/m² | R$ 869.805 | n=70 |
| Pintura | R$ 594/m² | R$ 2.423.779 | n=96 |
| Esquadrias | R$ 1154/m² | R$ 4.706.548 | n=96 |
| Louças | R$ 110/m² | R$ 447.516 | n=76 |

## 📋 Resumo de Rastreabilidade

- **Itens do executivo analisados:** 156
- **Com match na base de 4.210 PUs cross-projeto:** 99 (63% se total > 0)
- **Sem referência direta:** 57

## 🔗 Fontes e Arquivos

- **Quantitativos BIM consolidados:** `base/quantitativos-consolidados/placon-arminio-tavares.json`
- **BIM raw:** `base/quantitativos-bim/placon-arminio-tavares.json`
- **DXF raw:** `base/quantitativos-dxf/placon-arminio-tavares.json`
- **PDF raw:** `base/quantitativos-pdf/placon-arminio-tavares.json`
- **Executivo:** `base/pacotes/placon-arminio-tavares/executivo-placon-arminio-tavares.xlsx`
- **PUs cross-projeto:** `base/itens-pus-agregados.json` (4.210 clusters)
- **Índices derivados:** `base/indices-derivados-v2.json` (29 índices)
- **Base master:** `base/base-indices-master-2026-04-13.json`
