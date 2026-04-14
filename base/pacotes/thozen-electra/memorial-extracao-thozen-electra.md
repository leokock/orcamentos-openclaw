# Memorial de Extração — thozen-electra

_Gerado em 13/04/2026 23:27 — Fase 17 (base enriquecida)_

Este documento detalha a **lógica de extração** de cada item do orçamento executivo, rastreando fontes de dados e lógica de precificação.

## 📊 Dados do Projeto

| Campo | Valor |
|---|---|
| **Slug** | `thozen-electra` |
| **AC (Área Construída)** | 37.893,89 m² |
| **UR (Unidades)** | 348 |
| **Padrão** | alto |

## 🏗 Quantitativos Extraídos do BIM

**Fontes:** 8 IFCs, 21 DXFs, 0 PDFs

### Alvenaria e Paredes (IfcWall)

- **Total de elementos:** 28014 paredes
- **Área total:** 127.902 m²
- **Comprimento total:** 46.944 m

**Por tipo:**

| Tipo (material + espessura) | Qtd | Área m² | Comp m | Exemplos no IFC |
|---|---|---|---|---|
| alvenaria_generica_11cm | 7872 | 42.159 | 15.487 | Parede básica:ALV 11,5  R2/R2 |
| alvenaria_generica_14cm | 3981 | 29.301 | 11.227 | Parede básica:ALV 14  R2/R2 |
| outros_2cm | 6417 | 20.106 | 6.862 | Parede básica:REV. REBOCO INTERNO 2cm |
| alvenaria_generica_9cm | 5064 | 12.874 | 4.421 | Parede básica:ALV 9  R0/R2 / Parede básica:ALV 9  R2/R2 |
| alvenaria_generica_19cm | 1342 | 9.350 | 3.561 | Parede básica:ALV 19  R2/R2 |
| alvenaria_generica_15cm | 912 | 5.774 | 2.169 | Parede básica:ALV SIP 15  R2/R2 |
| alvenaria_generica_5cm | 1056 | 4.582 | 1.572 | Parede básica:ALV 5 R2/R0 |
| outros_3cm | 648 | 1.865 | 779 | Parede básica:REV. REBOCO EXTERNO 3cm |
| alvenaria_generica_12cm | 288 | 1.083 | 381 | Parede básica:ALV SIP 12,5  R2/R2 |
| outros_20cm | 338 | 678 | 240 | Parede básica:Genérico - 20 mm |
| outros_5cm | 48 | 99 | 109 | Parede básica:REV. REBOCO INTERNO 5cm |
| bloco_concreto_6cm | 48 | 32 | 135 | Parede básica:ALV BLOCO DE CONCRETO 6cm |

### Estrutura (lajes + vigas + pilares)

| Elemento | Quantidade | Volume m³ | Comprimento/Altura m | Fonte |
|---|---|---|---|---|
| Lajes (IfcSlab) | 3914 | 14.423,6 | área 72.697 m² | BIM IfcSlab |
| Vigas (IfcBeam) | 3531 | 4.305,7 | 18.870 | BIM IfcBeam |
| Pilares (IfcColumn) | 1531 | 4.551,1 | 4.904 | BIM IfcColumn |

- **Concreto total estimado (BIM):** 23.280,4 m³
- **Índice concreto/m² AC:** 0,614 m³/m² (vs mediana base 0,34) 🔴 delta +81%

### Esquadrias e Aberturas

- **Portas (IfcDoor):** 2376 unidades
- **Janelas (IfcWindow):** 1632 unidades
- **Pele de vidro (IfcCurtainWall):** 24 elementos, 0 m²
- **Guarda-corpos (IfcRailing):** 531 elementos, 1.382 m

**Top 10 tipos de porta:**

- **DALLO-PORTA INTERNA:PM 80X210**: 912 un
- **DALLO-PORTA INTERNA:PM 70X210**: 552 un
- **DALLO-PORTA INTERNA:PM 90X210**: 192 un
- **DALLO-PORTA INTERNA:PM 60X210**: 144 un
- **DALLO-PORTA DO ELEVADOR:PE 80X210**: 144 un
- **DALLO-PORTA DE CORRER DE MADEIRA:PMC 70X210**: 72 un
- **PORTA CORRER - 4 FOLHAS EMBUTIDAS:PORTA CORRER - 4 FOLHAS EM**: 49 un
- **DALLO-PORTA DE CORRER DE MADEIRA:PMC 90X210**: 48 un
- **DALLO-PORTA CORTA-FOGO:PM 80X210**: 48 un
- **DALLO-PORTA CORTA-FOGO:PM 100X210**: 48 un

**Top 10 tipos de janela:**

- **DALLO-JAN. BASC. 1F  S. PERS. ALUM. BRANCO:JA 60X75**: 552 un
- **DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO:JA 170X110**: 192 un
- **DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO:JA 140X214**: 144 un
- **VENEZIANA:425x425**: 96 un
- **DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. BRANCO:JA 120x**: 73 un
- **DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO:JA 120X214**: 72 un
- **DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO:JA 120X120**: 72 un
- **DALLO-JAN. CORRER 2F S. PERS. COM PEIT. DE VIDRO ALUM. BRANC**: 48 un
- **DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO:JA 130X214**: 48 un
- **DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. BRANCO:JA 100x**: 47 un

### Ambientes (IfcSpace)

- **Total:** 108 ambientes
- **Área total:** 2.635 m²
- **Volume total:** 6.713 m³

**Top 15 tipos de ambiente por área:**

| Ambiente | Qtd | Área m² |
|---|---|---|
| Garagem 01 | 1 | 1.442 |
| Suíte 1 | 9 | 233 |
| Living | 8 | 229 |
| Circulação | 7 | 169 |
| Suíte 2 | 8 | 120 |
| Suíte 3 | 6 | 89 |
| Cozinha | 8 | 65 |
| Abas G01 | 1 | 45 |
| Escada | 2 | 33 |
| A. Serviço | 7 | 24 |
| BWC suíte 1 | 6 | 23 |
| Suíte3 | 1 | 20 |
| Antecamara | 2 | 18 |
| Elevador | 4 | 17 |
| BWC suíte 2 | 5 | 17 |

## 💰 Orçamento Executivo — Lógica de Extração por Item

Cada item abaixo mostra: descrição, PU usado, PU base cross-projeto (se disponível), faixa P10-P90 e fonte.

### Gerenciamento

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Equipe Indireta - Almoxarife | mes | 49,00 | R$ 7.285 | — | — | — | 🔴 Sem ref |
| Equipe Indireta - Auxiliar de Almoxarife | mes | 41,00 | R$ 4.513 | — | — | — | 🔴 Sem ref |

### Movimentação_de_Terra

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Serviço de Bota-fora - Escavação Vertical | m3 | 49.803,29 | R$ 45 | — | — | — | 🔴 Sem ref |
| Escavação mecanizada para blocos de coroamento e baldrames, com previs | m3 | 6.867,96 | R$ 36 | — | — | — | 🔴 Sem ref |
| Serviço de Terraplenagem / Escavação e Carga Mecanizada em Corte - Des | m3 | 20.260,56 | R$ 4 | — | — | — | 🔴 Sem ref |
| Reaterro mecanizado para blocos de coroamento e baldrames, com miniesc | m3 | 3.939,07 | R$ 15 | — | — | — | 🔴 Sem ref |
| Serviço de Terraplenagem / Espalhamento / Umedecimento / Compactação e | m3 | 0,06 | R$ 9 | — | — | — | 🔴 Sem ref |

### Infraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mao de obra para execução de infraestrutura de concreto armado | m3 | 1.201,59 | R$ 1.986 | — | — | — | 🔴 Sem ref |
| Execucao Estaca Raiz 400Mm | m | 2.928,00 | R$ 356 | — | — | — | 🔴 Sem ref |
| Execucao Estaca Helice Continua 060Cm | m | 3.996,00 | R$ 113 | R$ 105,00 | R$ 48 - 160 | 103 | 🟢 Alta |
| Execucao Estaca Helice Continua 040Cm | m | 1.808,00 | R$ 101 | R$ 105,00 | R$ 48 - 160 | 103 | 🟢 Alta |
| Serviço de Bota-fora - Valas de Infraestrutura | m2 | 3.807,55 | R$ 45 | — | — | — | 🔴 Sem ref |
| Serviço de Arrasamento Mecanizado de Estacas | un | 518,00 | R$ 300 | — | — | — | 🔴 Sem ref |
| Serviço de Bota-fora - Estaca | m3 | 2.242,48 | R$ 68 | — | — | — | 🔴 Sem ref |
| Fabricação e montagem de forma para bloco de fundação - em madeira Com | m2 | 2.074,98 | R$ 68 | — | — | — | 🔴 Sem ref |
| Infraestrutura para carregamento de carro elétrico | pto | 104,00 | R$ 550 | — | — | — | 🔴 Sem ref |
| Apiloamento de solo para elementos de infraestrutura | m2 | 1.467,69 | R$ 7 | — | — | — | 🔴 Sem ref |

### Supraestrutura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mao de obra para execucacao de supraestrutura de concreto armado | m2 | 14.634,80 | R$ 280 | — | — | — | 🔴 Sem ref |
| Locação de escoramento metálico pe direito simples | m2 | 14.634,80 | R$ 87 | R$ 87,33 | R$ 87 - 87 | 3 | 🟡 Média |
| Concreto de Estaca Fck = 40 Mpa / Bombeável | m3 | 1.357,50 | R$ 736 | — | — | — | 🔴 Sem ref |
| Concreto da Fundação Rasa Fck = 35 Mpa / Bombeável (com Impermeabiliza | m3 | 1.201,59 | R$ 660 | — | — | — | 🔴 Sem ref |
| Concreto da Estrutura Fck = 35 Mpa / Bombeável (com aditivo impermeabi | m3 | 1.122,00 | R$ 660 | — | — | — | 🔴 Sem ref |
| Concreto da Estrutura Fck = 35 Mpa / Bombeável | m3 | 981,51 | R$ 600 | — | — | — | 🔴 Sem ref |
| Armacao Estaca Aco Ca-50 Ø 25.0mm Corte E Dobra Em Indústria | kg | 71.751,00 | R$ 8 | R$ 8,29 | R$ 8 - 10 | 7 | 🟡 Média |
| Concreto de Contenção Fck = 30 Mpa / Bombeável (com Impermeabilizante) | m3 | 734,45 | R$ 649 | — | — | — | 🔴 Sem ref |
| Argamassa de Estaca Fck=30MPa / Bombeável | m3 | 323,08 | R$ 1.041 | — | — | — | 🔴 Sem ref |
| Armacao Fundação Aco Ca-50 Ø 25.0Mm Corte E Dobra Em Indústria | kg | 47.928,90 | R$ 7 | R$ 6,97 | R$ 7 - 7 | 13 | 🟢 Alta |
| Armacao Estrutura Aco Ca-50 Ø 12.5Mm Corte E Dobra Em Indústria | kg | 47.524,05 | R$ 7 | R$ 7,07 | R$ 7 - 8 | 20 | 🟢 Alta |
| Armacao Estrutura Aco Ca-50 Ø 16.0Mm Corte E Dobra Em Indústria | kg | 37.339,97 | R$ 7 | R$ 7,07 | R$ 7 - 8 | 20 | 🟢 Alta |
| Armacao Estrutura Aco Ca-50 Ø 8.0Mm Corte E Dobra Em Indústria | kg | 29.648,26 | R$ 7 | R$ 7,07 | R$ 7 - 8 | 20 | 🟢 Alta |
| Armacao Estrutura Aco Ca-50 Ø 25.0Mm Corte E Dobra Em Indústria | kg | 30.307,28 | R$ 7 | R$ 7,07 | R$ 7 - 8 | 20 | 🟢 Alta |
| Armacao Estaca Aco Ca-50 Ø 16.0mm Corte E Dobra Em Indústria | kg | 19.430,00 | R$ 8 | R$ 8,29 | R$ 8 - 10 | 7 | 🟡 Média |
| Armacao Fundação Aco Ca-50 Ø 12.5Mm Corte E Dobra Em Indústria | kg | 19.330,28 | R$ 7 | R$ 6,97 | R$ 7 - 7 | 13 | 🟢 Alta |
| Concreto de Contenção Fck = 35 Mpa / Bombeável (com Impermeabilizante) | m3 | 168,70 | R$ 660 | — | — | — | 🔴 Sem ref |
| Armacao Fundação Aco Ca-50 Ø 20.0Mm Corte E Dobra Em Indústria | kg | 16.043,08 | R$ 7 | R$ 6,97 | R$ 7 - 7 | 13 | 🟢 Alta |
| Armacao Fundação Aco Ca-50 Ø 16.0Mm Corte E Dobra Em Indústria | kg | 15.353,92 | R$ 7 | R$ 6,97 | R$ 7 - 7 | 13 | 🟢 Alta |
| Armacao Estrutura Aco Ca-50 Ø 10.0Mm Corte E Dobra Em Indústria | kg | 13.123,83 | R$ 7 | R$ 7,07 | R$ 7 - 8 | 20 | 🟢 Alta |

### Alvenaria

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Alvenaria Com Blocos De Concreto Celular Auto Clavado - 12,5X30X60Cm | m2 | 697,42 | R$ 102 | R$ 101,84 | R$ 102 - 102 | 4 | 🟡 Média |
| Mao de Obra Empreitada - Instalação de Parede de Drywall | m2 | 1.675,52 | R$ 40 | R$ 40,00 | R$ 40 - 40 | 4 | 🟡 Média |
| Parede Com Sistema Em Chapas De Gesso Para Drywall, Uso Interno, Monta | m2 | 209,59 | R$ 191 | — | — | — | 🔴 Sem ref |
| Mao de Obra para Execução de Alvenaria de Vedação - internas e externa | m2 | 773,81 | R$ 35 | R$ 35,00 | R$ 35 - 35 | 4 | 🟡 Média |
| Tratamento De Alinhamento do Drywall com Martique e Tarucel | m | 798,81 | R$ 29 | R$ 29,42 | R$ 29 - 29 | 4 | 🟡 Média |
| Alvenaria de vedação de blocos cerâmicos furados na horizontal de 19,0 | m2 | 152,77 | R$ 53 | R$ 34,05 | R$ 28 - 45 | 83 | 🟢 Alta |
| Encunhamento De Alvenaria De Vedação Com Argamassa Expansiva | m | 419,12 | R$ 15 | R$ 2,37 | R$ 2 - 8 | 221 | 🟢 Alta |
| Chapisco aplicado em alvenarias externas, com colher de pedreiro, de a | m2 | 1.788,62 | R$ 3 | R$ 2,54 | R$ 3 - 3 | 4 | 🟡 Média |
| Tela soldada para Amarração Alvenaria | un | 614,00 | R$ 4 | R$ 3,60 | R$ 4 - 4 | 4 | 🟡 Média |
| Chapisco aplicado em alvenarias internas, com colher de pedreiro, de a | m2 | 107,05 | R$ 3 | R$ 2,54 | R$ 3 - 3 | 4 | 🟡 Média |

### Impermeabilização

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Impermeabilização De Superfície Com Aspersão de CWS e CWS100 - Process | m2 | 3.093,87 | R$ 65 | — | — | — | 🔴 Sem ref |
| Mão de obra impermeabilização de aspersão de CWS | m2 | 3.093,87 | R$ 27 | R$ 27,40 | R$ 27 - 27 | 3 | 🟡 Média |
| Impermeabilização com resina acrílica e perfil extrudado neoprene (jee | m | 95,28 | R$ 225 | — | — | — | 🔴 Sem ref |
| Regularizacao de superficie para impermeabilizacao | m2 | 2.044,88 | R$ 6 | R$ 5,57 | R$ 3 - 8 | 176 | 🟢 Alta |
| Impermeabilização De Superfície Com Argamassa Polimérica, 3 Demãos | m2 | 123,69 | R$ 39 | R$ 68,00 | R$ 39 - 75 | 7 | 🟡 Média |
| Mão de obra impermeabilização de argamassa polimérica | m2 | 123,69 | R$ 25 | R$ 26,57 | R$ 16 - 30 | 72 | 🟢 Alta |

### Instalações

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mão de obra para execução de instalações hidráulicas e drenagem | m2 | 42.277,77 | R$ 40 | — | — | — | 🔴 Sem ref |
| Quadro de distribuição para telecomunicações (10U/10") , dimensões con | un | 142,00 | R$ 2.500 | — | — | — | 🔴 Sem ref |
| Mão de obra instalações preventivas | m2 | 42.277,77 | R$ 8 | R$ 6,20 | R$ 3 - 8 | 8 | 🟡 Média |
| ELETRODUTO DE PVC RÍGIDO, TIPO ROSCA, Ø ¾” | m | 37.500,00 | R$ 8 | R$ 12,95 | R$ 8 - 25 | 8 | 🟡 Média |
| Arame guia galvanizado, seção 14 AWG, para ser passado em todas as tub | m | 48.000,00 | R$ 4 | — | — | — | 🔴 Sem ref |
| QUADRO GERAL E OU DE DISTRIBUIÇÃO METÁLICO PARA SUPERVISÃO E AUTOMAÇÃO | un | 84,00 | R$ 2.000 | — | — | — | 🔴 Sem ref |
| Cabo de logica UTP-4P tipo par trançado - categoria 6 gigalan AZ Cat.6 | m | 43.615,00 | R$ 4 | — | — | — | 🔴 Sem ref |
| Cabo interno òptico - Cabo Fiber-Lan 50/125x2 Fibras Furukawa | m | 43.615,00 | R$ 4 | — | — | — | 🔴 Sem ref |
| Manutenção Elétrica Provisória | mes | 49,00 | R$ 3.052 | R$ 200,00 | R$ 176 - 3052 | 5 | 🟡 Média |
| 01 leitor Biometria | un | 284,00 | R$ 484 | — | — | — | 🔴 Sem ref |
| Manutenção Hidrossanitário Provisória | mes | 49,00 | R$ 2.671 | — | — | — | 🔴 Sem ref |
| ELETRODUTO DE PVC RÍGIDO, TIPO ROSCA, Ø 1” | m | 10.800,00 | R$ 9 | R$ 12,95 | R$ 8 - 25 | 8 | 🟡 Média |
| 01 interrupor de comando da persiana | un | 553,00 | R$ 109 | — | — | — | 🔴 Sem ref |
| Arandela blindada em alumínio pintado, modelo a ser definido, com  uma | un | 142,00 | R$ 383 | — | — | — | 🔴 Sem ref |
| Placa com 2 tomadas para conector RJ-45 | un | 1.222,00 | R$ 33 | — | — | — | 🔴 Sem ref |
| CABOS  DO TIPO EPROTENAX  1000 V (90o) 185mm² | m | 230,00 | R$ 169 | — | — | — | 🔴 Sem ref |
| 01 pulsador ou teclado de comando da iluminação | un | 2.516,00 | R$ 14 | — | — | — | 🔴 Sem ref |
| ELETRODUTO DE PVC RÍGIDO, TIPO ROSCA, Ø 1 ¼” | m | 2.034,00 | R$ 17 | R$ 12,95 | R$ 8 - 25 | 8 | 🟡 Média |
| CABOS DO TIPO ANTI-CHAMA, ISOLAMENTO PARA 750 V (70o) 2,5mm² | m | 3.200,00 | R$ 6 | — | — | — | 🔴 Sem ref |
| 20 x 20 x 10 cm (de embutir) - Caixa de passagem | un | 90,00 | R$ 333 | — | — | — | 🔴 Sem ref |

### Sistemas_Especiais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Locação Elevador Cremalheira | mes | 28,00 | R$ 19.200 | R$ 9.000,00 | R$ 5500 - 22000 | 21 | 🟢 Alta |
| 28.04 | 35.05 | 1,25 | R$ 35.050 | — | — | — | 🔴 Sem ref |
| Montagem E Desmontagem Elevador Cremalheira | un | 2,00 | R$ 16.300 | R$ 9.500,00 | R$ 9500 - 16300 | 4 | 🟡 Média |
| 24.21 | 31.473000000000003 | 1,30 | R$ 31.473 | — | — | — | 🔴 Sem ref |
| 19.82 | 25.766000000000002 | 1,30 | R$ 25.766 | — | — | — | 🔴 Sem ref |
| 10.8 | 5.4 | 0,50 | R$ 5.400 | — | — | — | 🔴 Sem ref |
| Mao De Obra Para Pintura de Poço do Elevador, 2 Demaos | m2 | 294,94 | R$ 16 | R$ 16,00 | R$ 16 - 16 | 4 | 🟡 Média |
| GERADOR DE COLORO BZ -30 | un | 1,00 | R$ 3.657 | R$ 3.296,12 | R$ 3296 - 3657 | 7 | 🟡 Média |
| 11.16 | 3.3479999999999683 | 0,30 | R$ 3.348 | — | — | — | 🔴 Sem ref |
| GERADOR DE COLORO BZ -20 | un | 1,00 | R$ 3.296 | R$ 3.296,12 | R$ 3296 - 3657 | 7 | 🟡 Média |
| TAMPA ARTICULADA GDA 110X110cm CÓDIGO 3140 | un | 1,00 | R$ 3.200 | — | — | — | 🔴 Sem ref |
| Mobilização E Desmobilização Elevador Cremalheira | un | 2,00 | R$ 1.328 | — | — | — | 🔴 Sem ref |
| 13.28 | 2.6559999999999993 | 0,20 | R$ 2.656 | — | — | — | 🔴 Sem ref |
| TAMPA GDA REBAIXADA C/ GRELHA 80X80cm CÓDIGO 3078 | un | 1,00 | R$ 1.850 | R$ 1.850,00 | R$ 1850 - 1850 | 6 | 🟡 Média |
| Bomba BM-33 1/3 cv p/ piscinas de até 40 mil litros
SODAMAR | un | 1,00 | R$ 1.416 | — | — | — | 🔴 Sem ref |
| Bomba 1/4cv BM-25 p/ piscinas de até 28 mil litro
SODAMAR | un | 1,00 | R$ 1.317 | — | — | — | 🔴 Sem ref |
| Bomba 1/4 cv BM-25 p/ piscinas de até 28 mil litros
SODAMAR | un | 1,00 | R$ 1.055 | — | — | — | 🔴 Sem ref |
| Filtro para piscina FM-36 p/ até 40 mil litros
SODAMAR | un | 1,00 | R$ 978 | R$ 807,00 | R$ 714 - 978 | 10 | 🟢 Alta |
| Filtro para piscina FM-30 p/ até 28 mil litros
SODAMAR | un | 1,00 | R$ 900 | R$ 807,00 | R$ 714 - 978 | 10 | 🟢 Alta |
| Tela  Elevador em Aço Galvanizado | m2 | 55,14 | R$ 16 | — | — | — | 🔴 Sem ref |

### Rev._Interno_Parede

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Mao de obra para reboco externo, inclui chapisco | m2 | 1.796,66 | R$ 55 | R$ 58,00 | R$ 55 - 80 | 26 | 🟢 Alta |
| Reboco externo em argamassa industrializada, espessura de 25mm | m2 | 1.788,62 | R$ 29 | R$ 28,92 | R$ 29 - 29 | 4 | 🟡 Média |
| Mao de obra para reboco interno, incluindo chapisco | m2 | 227,07 | R$ 34 | — | — | — | 🔴 Sem ref |
| Reboco interno em argamassa industrializada, espessura de 20mm, com ex | m2 | 227,07 | R$ 27 | R$ 27,13 | R$ 27 - 27 | 4 | 🟡 Média |
| Chapisco aplicado em estruturas de concreto, com desempenadeira dentad | m2 | 85,16 | R$ 7 | R$ 5,38 | R$ 2 - 7 | 78 | 🟢 Alta |

### Teto

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Forro de Gesso Acartonada para Áreas Molhadas - material e mão de obra | m2 | 2.772,10 | R$ 116 | — | — | — | 🔴 Sem ref |
| Revestimento em Forro com Mármore Travertino Bruto, rejunte cimentício | m2 | 72,09 | R$ 1.944 | R$ 1.856,24 | R$ 356 - 1944 | 6 | 🟡 Média |
| Forro de Gesso Acartonada para Áreas Secas - material e mão de obra | m2 | 1.102,21 | R$ 101 | R$ 100,88 | R$ 101 - 101 | 4 | 🟡 Média |
| Forro de ACM- material e mão de obra | m2 | 143,43 | R$ 508 | — | — | — | 🔴 Sem ref |
| Forro de madeira - material e mão de obra | m2 | 4,41 | R$ 579 | R$ 250,00 | R$ 210 - 390 | 11 | 🟢 Alta |

### Pisos

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Revestimento em Porcelanato Alto Padrão Polido, rejunte acrílico - 120 | m2 | 9.709,27 | R$ 165 | — | — | — | 🔴 Sem ref |
| Revestimento em Porcelanato Parede interno Alto Padrão Acetinado, reju | m2 | 9.962,61 | R$ 126 | R$ 145,91 | R$ 126 - 158 | 4 | 🟡 Média |
| Contrapiso Acustico de Regularização de Base para Revestimento de Piso | m2 | 8.610,19 | R$ 105 | R$ 44,63 | R$ 18 - 112 | 12 | 🟢 Alta |
| Revestimento em Porcelanato Alto Padrão Acetinado, rejunte acrílico -  | m2 | 2.074,13 | R$ 134 | R$ 145,91 | R$ 126 - 158 | 4 | 🟡 Média |
| Revestimento Rodapé com mármore travertino bruto, com rejunte cimentíc | m | 145,34 | R$ 884 | R$ 1.856,24 | R$ 356 - 1944 | 6 | 🟡 Média |
| Revestimento Rodapé Madeira - altura 20cm | m | 729,30 | R$ 116 | — | — | — | 🔴 Sem ref |
| Revestimento em Porcelanato Alto Padrão Resistente a Escorregamento, r | m2 | 654,90 | R$ 124 | — | — | — | 🔴 Sem ref |
| Revestimento em Porcelanato Parede externo, rejunte acrílico - 280x280 | m2 | 158,00 | R$ 411 | — | — | — | 🔴 Sem ref |
| Mao de obra para execucao de contrapiso comum e acústico | m2 | 1.444,04 | R$ 35 | R$ 37,00 | R$ 28 - 40 | 21 | 🟢 Alta |
| Revestimento em Porcelanato Piso Médio Padrão Natural, rejunte acrílic | m2 | 333,52 | R$ 76 | — | — | — | 🔴 Sem ref |
| Mao de obra para execucao de contrapiso estruturado | m2 | 608,81 | R$ 38 | — | — | — | 🔴 Sem ref |
| Revestimento em Porcelanato Piso, rejunte acrílico - 100x100cm | m2 | 120,97 | R$ 142 | R$ 81,15 | R$ 20 - 142 | 6 | 🟡 Média |
| Mao de obra Rodapé Madeira | m | 729,30 | R$ 22 | R$ 24,50 | R$ 22 - 24 | 3 | 🟡 Média |
| Revestimento em Soleira com Mármore Travertino, com rejunte cimentício | m2 | 5,68 | R$ 2.354 | — | — | — | 🔴 Sem ref |
| Revestimento em Porcelanato Parede interno Médio Padrão Acetinado, rej | m2 | 84,65 | R$ 158 | R$ 145,91 | R$ 126 - 158 | 4 | 🟡 Média |
| Contrapiso Estruturado de Base para Revestimento de Piso, com argamass | m2 | 518,64 | R$ 20 | — | — | — | 🔴 Sem ref |
| Contrapiso de Regularização de Base para Revestimento de Piso, com arg | m2 | 149,49 | R$ 39 | R$ 44,63 | R$ 18 - 112 | 12 | 🟢 Alta |
| Mao de obra Rodapé PVC / Aluminio | m | 392,97 | R$ 22 | R$ 22,00 | R$ 22 - 22 | 3 | 🟡 Média |
| Mao de obra para colocacao e rejuntamento de revestimento cerâmico/por | m2 | 164,06 | R$ 45 | R$ 45,00 | R$ 42 - 52 | 9 | 🟡 Média |
| Mao de obra para aplicacao de pedra natural em Soleiras e Pingadeiras | m2 | 162,57 | R$ 38 | — | — | — | 🔴 Sem ref |

### Pintura

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Pintura Epoxi Em Piso 2 Demaos - Aplicacao Em Garagens - Incluindo Fai | m2 | 5.732,20 | R$ 40 | — | — | — | 🔴 Sem ref |
| Mao De Obra Para Pintura Acrílica Em Teto 3 Demaos | m2 | 1.134,13 | R$ 32 | R$ 32,00 | R$ 13 - 32 | 23 | 🟢 Alta |
| Mao De Obra Para Pintura Acrilica Em Paredes, 3 Demaos | m2 | 920,70 | R$ 32 | R$ 8,43 | R$ 2 - 15 | 181 | 🟢 Alta |
| Mao De Obra Para Pintura Epoxi Em Paredes, 2 Demaos | m2 | 373,26 | R$ 47 | — | — | — | 🔴 Sem ref |
| Pintura Epoxi a Base de Água em Parede - Demarcação de Faixa de Garage | m2 | 263,98 | R$ 40 | — | — | — | 🔴 Sem ref |
| Pintura Epoxi a Base de Água em Parede, 2 Demaos | m2 | 241,27 | R$ 40 | — | — | — | 🔴 Sem ref |
| Mao De Obra Para Pintura Epoxi Em Piso, 2 demãos (Incluindo Faixas De  | m2 | 173,81 | R$ 47 | — | — | — | 🔴 Sem ref |
| Pintura Com Tinta Latex Acrilica, Acabamento Fosco Em Paredes Internas | m2 | 639,89 | R$ 7 | R$ 4,99 | R$ 3 - 7 | 130 | 🟢 Alta |
| Pintura Epoxi Em Piso, 2 Demaos, Aplicacao Em Garagens, Àreas Técnicas | m2 | 88,86 | R$ 40 | — | — | — | 🔴 Sem ref |
| Mao De Obra Para Pintura Epoxi Em Rodape, 2 Demaos | m | 362,89 | R$ 9 | R$ 6,71 | R$ 4 - 9 | 8 | 🟡 Média |
| Mao de obra para Pintura Acrilica em Paredes Externas, 2 demaos | m2 | 27,80 | R$ 45 | R$ 41,84 | R$ 6 - 45 | 17 | 🟢 Alta |
| Mão De Obra Para Pintura Com Tinta Esmalte Sintético, Em Madeira/Corri | m | 73,78 | R$ 11 | R$ 7,06 | R$ 1 - 11 | 8 | 🟡 Média |
| Pintura Com Tinta Latex Acrilica, Acabamento Acetinado Em Teto, 3 Dema | m2 | 68,23 | R$ 8 | — | — | — | 🔴 Sem ref |
| Pintura Com Tinta Esmalte Sintético, Em Madeira/Corrimão, 3 Demaos | m | 73,78 | R$ 1 | R$ 7,06 | R$ 1 - 11 | 8 | 🟡 Média |

### Esquadrias

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Esquadrias de alumínio - fornecimento e instalação | m2 | 7.549,72 | R$ 1.218 | R$ 1.088,02 | R$ 844 - 1350 | 29 | 🟢 Alta |
| Guarda Corpo vidro, com suporte de fixação em piso -  fornecimento e i | m2 | 2.152,64 | R$ 2.366 | — | — | — | 🔴 Sem ref |
| Guarda Corpo de Vidro Estrutural - fornecimento e instalação | m2 | 808,92 | R$ 2.366 | — | — | — | 🔴 Sem ref |
| Brise Filetado Arkwood - material e mão de obra | m2 | 1.596,55 | R$ 995 | — | — | — | 🔴 Sem ref |
| Guarda Corpo de Vidro Autoportante - fornecimento e instalação | m2 | 467,16 | R$ 2.320 | — | — | — | 🔴 Sem ref |
| Porta de madeira- correr - folha leve/média - 70x210cm (kit completo)  | un | 264,00 | R$ 2.421 | R$ 1.711,00 | R$ 960 - 2576 | 8 | 🟡 Média |
| Guarda Corpo de Vidro e Aluminio - fornecimento e instalação | m2 | 289,04 | R$ 2.151 | R$ 768,50 | R$ 600 - 936 | 26 | 🟢 Alta |
| Esquadrias de Alumínio Unitizadas - fornecimento e instalação | m2 | 550,10 | R$ 671 | — | — | — | 🔴 Sem ref |
| Porta de madeira- correr (trilho lateral) - folha leve/média - 70x210c | un | 46,00 | R$ 2.576 | R$ 1.711,00 | R$ 960 - 2576 | 8 | 🟡 Média |
| Porta de madeira- correr - folha leve/média - 80x210cm (kit completo)  | un | 16,00 | R$ 2.421 | R$ 1.711,00 | R$ 960 - 2421 | 7 | 🟡 Média |
| Esquadrias Metálicas - Porta Corta Fogo P90 90x210 - fornecimento e in | un | 19,50 | R$ 1.433 | R$ 1.433,00 | R$ 973 - 1433 | 5 | 🟡 Média |
| Rodapé em alumínio, altura 3cm | m | 392,97 | R$ 66 | — | — | — | 🔴 Sem ref |
| Porta de madeira- abrir - folha leve/média - 80x210cm (kit completo) - | un | 14,00 | R$ 1.711 | R$ 1.711,00 | R$ 960 - 2421 | 7 | 🟡 Média |
| Porta de madeira- abrir - folha leve/média - 60x210cm (kit completo) - | un | 7,00 | R$ 1.711 | R$ 1.405,06 | R$ 960 - 1711 | 4 | 🟡 Média |
| Porta de madeira- abrir - folha leve/média - 90x210cm (kit completo) - | un | 5,00 | R$ 1.811 | R$ 1.528,80 | R$ 960 - 1811 | 6 | 🟡 Média |
| Porta de madeira- abrir - folha leve/média - 70x210cm (kit completo) - | un | 5,00 | R$ 1.711 | R$ 1.711,00 | R$ 960 - 2576 | 8 | 🟡 Média |
| Esquadrias Metálicas - Alçapão 80x80 - fornecimento e instalacao | un | 8,00 | R$ 973 | R$ 1.433,00 | R$ 973 - 1433 | 5 | 🟡 Média |
| Porta de madeira- pivotante - folha leve/média - 153x210cm (kit comple | un | 1,00 | R$ 2.267 | — | — | — | 🔴 Sem ref |
| Moldura em alumínio para churrasqueiras - fornecimento e instalação | m | 17,20 | R$ 86 | R$ 530,00 | R$ 530 - 530 | 13 | 🟢 Alta |

### Louças_e_Metais

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Banheiro - Bacia Sanitária / Caixa Acoplada | un | 510,00 | R$ 1.625 | R$ 1.049,00 | R$ 708 - 1683 | 5 | 🟡 Média |
| Acabamento de Registro | un | 927,00 | R$ 494 | R$ 50,00 | R$ 50 - 50 | 90 | 🟢 Alta |
| Torneira Lavatório mesa | un | 17,00 | R$ 1.055 | R$ 350,00 | R$ 90 - 1055 | 5 | 🟡 Média |
| Cozinha - Cuba / Inox | un | 5,00 | R$ 2.750 | R$ 432,69 | R$ 250 - 2750 | 5 | 🟡 Média |
| Parafuso niquelado para fixação de bacia sanitária - tamanho S-10 | un | 2.064,00 | R$ 6 | R$ 5,95 | R$ 1 - 25 | 3 | 🟡 Média |
| Banheiro - Bacia Sanitária PNE | un | 6,00 | R$ 1.625 | R$ 978,28 | R$ 708 - 1625 | 4 | 🟡 Média |
| Torneira misturador pia cozinha | un | 5,00 | R$ 1.055 | R$ 250,00 | R$ 180 - 1055 | 5 | 🟡 Média |
| Banheiro - Cuba de Sobrepor - PNE | un | 2,00 | R$ 1.813 | R$ 492,89 | R$ 350 - 1813 | 3 | 🟡 Média |
| Anel de vedação, 100 mm, para saíde de bacia sanitária | un | 516,00 | R$ 5 | R$ 5,00 | R$ 5 - 13 | 3 | 🟡 Média |
| Torneira de Jardins | un | 27,00 | R$ 25 | R$ 50,20 | R$ 25 - 75 | 6 | 🟡 Média |
| Torneira tanque | un | 1,00 | R$ 125 | R$ 89,90 | R$ 39 - 271 | 7 | 🟡 Média |

### Fachada

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Entelamento Da Fachada | m2 | 11.510,52 | R$ 11 | — | — | — | 🔴 Sem ref |

### Complementares

| Descrição | Un | Qtd | PU usado | PU base mediano | Faixa P10-P90 | n obs | Conf |
|---|---|---|---|---|---|---|---|
| Esteira profissional touch Adidas | — | 3,00 | R$ 20.000 | — | — | — | 🔴 Sem ref |
| Área: | — | 16,77 | R$ 2.218 | R$ 1.462,17 | R$ 118 - 3457 | 93 | 🟢 Alta |
| Mesa de jantar Hiller | — | 2,00 | R$ 15.531 | — | — | — | 🔴 Sem ref |
| Espreguiçadeira Duma - Brisa Casa | — | 6,00 | R$ 4.180 | — | — | — | 🔴 Sem ref |
| Cadeira Évora com braço | — | 6,00 | R$ 4.000 | — | — | — | 🔴 Sem ref |
| Cadeira Rio sem braço - Studio Ambientes | — | 24,00 | R$ 900 | — | — | — | 🔴 Sem ref |
| Mesa Poker Arizona redondo | — | 2,00 | R$ 10.000 | — | — | — | 🔴 Sem ref |
| Banco Scala - De Lazzari | — | 4,00 | R$ 4.500 | — | — | — | 🔴 Sem ref |
| Mesa com tampo quadrado - Studio Ambientes | — | 6,00 | R$ 2.500 | — | — | — | 🔴 Sem ref |
| Vaso caixa alta M | — | 25,00 | R$ 500 | — | — | — | 🔴 Sem ref |
| Manutenção Tapume e Calçada | mes | 49,00 | R$ 250 | — | — | — | 🔴 Sem ref |
| Poltrona Yan | — | 2,00 | R$ 5.896 | — | — | — | 🔴 Sem ref |
| Espreguiçadeira Santorini | — | 8,00 | R$ 1.200 | — | — | — | 🔴 Sem ref |
| Sofá linha Austin Up | — | 2,00 | R$ 4.500 | — | — | — | 🔴 Sem ref |
| Kit toalhas | — | 15,00 | R$ 500 | R$ 500,00 | R$ 200 - 500 | 9 | 🟡 Média |
| Calçada/passeio em piso intertravado, com bloco retangular cor natural | m2 | 76,45 | R$ 95 | — | — | — | 🔴 Sem ref |
| Poltrona Blad | — | 4,00 | R$ 1.800 | — | — | — | 🔴 Sem ref |
| Cadeira bloo | — | 8,00 | R$ 850 | — | — | — | 🔴 Sem ref |
| Calçada provisória, execuão de piso intertravado | m2 | 65,97 | R$ 103 | — | — | — | 🔴 Sem ref |
| Jogo Jantar Chá Bar Hotel 30 Peças Porcelana Germer 6 Pessoas | — | 21,00 | R$ 320 | R$ 320,00 | R$ 320 - 320 | 4 | 🟡 Média |

## 📈 Comparação com Índices Derivados (Fase 13)

Totais esperados por macrogrupo baseados em 29 índices derivados de 126 projetos:

| Índice | Mediana | × AC = Esperado | Status |
|---|---|---|---|
| Concreto | R$ 229/m² | R$ 8.673.783 | n=64 |
| Aço | R$ 232/m² | R$ 8.784.380 | n=65 |
| Forma | R$ 165/m² | R$ 6.251.677 | n=69 |
| Escoramento | R$ 48/m² | R$ 1.806.568 | n=57 |
| Impermeabilização | R$ 265/m² | R$ 10.037.201 | n=95 |
| Elevadores | R$ 213/m² | R$ 8.083.869 | n=70 |
| Pintura | R$ 594/m² | R$ 22.526.337 | n=96 |
| Esquadrias | R$ 1154/m² | R$ 43.742.145 | n=96 |
| Louças | R$ 110/m² | R$ 4.159.161 | n=76 |

## 📋 Resumo de Rastreabilidade

- **Itens do executivo analisados:** 188
- **Com match na base de 4.210 PUs cross-projeto:** 91 (48% se total > 0)
- **Sem referência direta:** 97

## 🔗 Fontes e Arquivos

- **Quantitativos BIM consolidados:** `base/quantitativos-consolidados/thozen-electra.json`
- **BIM raw:** `base/quantitativos-bim/thozen-electra.json`
- **DXF raw:** `base/quantitativos-dxf/thozen-electra.json`
- **PDF raw:** `base/quantitativos-pdf/thozen-electra.json`
- **Executivo:** `base/pacotes/thozen-electra/executivo-thozen-electra.xlsx`
- **PUs cross-projeto:** `base/itens-pus-agregados.json` (4.210 clusters)
- **Índices derivados:** `base/indices-derivados-v2.json` (29 índices)
- **Base master:** `base/base-indices-master-2026-04-13.json`
