# Regras de Extração de Quantitativos — Visus Cost Management
## Projeto: DUO CLN (Modelo Arquitetônico Federado)

**Arquivo:** `DUO_CLN_MOD_ARQ_FED_R01.ifc`
**Tamanho:** ~279 MB
**Software origem:** Revit 2024 → Bonsai 0.8.4 (IfcOpenShell)
**Schema:** IFC2X3
**Data exportação:** 24/02/2026

---

## 1. Estrutura do Modelo

### 1.1 Pavimentos (25 níveis)

| # | Pavimento | Cota (cm) |
|---|-----------|-----------|
| 01 | 3º Subsolo | 84 |
| 02 | 2º Subsolo | 390 |
| 03 | 1º Subsolo | 696 |
| 04 | Térreo | 1002 |
| 05 | 2º Pavto | 1368 |
| 06 | 3º Pavto | 1674 |
| 07 | 4º Pavto | 1980 |
| 08 | 5º Pavto | 2286 |
| 09 | 6º Pavto | 2592 |
| 10 | 7º Pavto | 2898 |
| 11 | 8º Pavto | 3204 |
| 12 | 9º Pavto | 3510 |
| 13 | 10º Pavto | 3816 |
| 14 | 11º Pavto | 4122 |
| 15 | 12º Pavto | 4428 |
| 16 | 13º Pavto | 4734 |
| 17 | 14º Pavto | 5040 |
| 18 | 15º Pavto | 5346 |
| 19 | 16º Pavto | 5652 |
| 20 | 17º Pavto | 5958 |
| 21 | Laje Técnica | 6286 |
| 22 | Cobertura | 6456 |
| 23 | Barrilete | 6786 |
| 24 | Reservatório | 6936 |
| 25 | Tampa do Reservatório | 7250 |

**Pé-direito típico:** ~306 cm (diferença entre pavimentos tipo)

### 1.2 Entidades BIM (elementos construtivos)

| Entidade IFC | Quantidade | O que representa |
|---|---|---|
| IfcWallStandardCase | 17.133 | Paredes padrão (alvenaria, revestimentos, fachada) |
| IfcWall | 1.551 | Paredes não-padrão |
| IfcSlab | 1.383 | Pisos, soleiras, peitoris, rufos |
| IfcBuildingElementProxy | 1.362 | Vergas, contravergas, textos, faixas garagem |
| IfcDoor | 470 | Portas e portões |
| IfcCovering | 448 | Forros |
| IfcWindow | 294 | Janelas |
| IfcRailing | 92 | Guarda-corpos e venezianas |
| IfcStairFlight | 80 | Lances de escada |
| IfcStair | 21 | Escadas (agrupamento) |
| IfcOpeningElement | 15.061 | Aberturas (gerado automaticamente) |

**Total de elementos construtivos quantificáveis: ~22.834**

---

## 2. Property Sets Disponíveis (Metadados)

O modelo é **muito rico em informação**. Além dos Psets padrão IFC, há tabelas customizadas da CTN (Cartesian):

### 2.1 Tabelas CTN (customizadas — principal fonte de dados)

| Property Set | Aplicação | O que contém |
|---|---|---|
| `B02. TABELA DE ALVENARIAS` | Paredes (alvenaria) | Tipo bloco, espessura, acabamento |
| `B04. TABELA REVEST PAREDES` | Paredes (revestimento interno) | Material, espessura, acabamento |
| `B05. TABELA REVEST FACHADAS` | Paredes (fachada) | Material externo, cor, tipo |
| `B06. TABELA REVEST PISO` | Pisos | Material, espessura, acabamento |
| `B09. TABELA DE TETOS` | Forros | Tipo forro, material |
| `B10. TABELA DE PORTAS TOTAL` | Portas | Material, dimensões, tipo abertura |
| `B11. TABELA DE JANELAS TOTAL` | Janelas | Material, dimensões, tipo |
| `B12. TABELA DE BRISES` | Brises | Tipo, material |
| `B13. TABELA DE PELE DE VIDRO` | Pele de vidro | Tipo, material |
| `B15. TABELA DE GUARDA CORPOS` | Guarda-corpos | Material, altura |
| `B16. TABELA DE RODAPES` | Rodapés | Material, altura |
| `B18. TABELA IMPERMEABILIZAÇÃO PAREDE` | Impermeabilização | Tipo, aplicação |
| `P00. TABELA DE PAREDES EXTERNAS` | Paredes externas | Classificação, acabamento |
| `P01. TABELA DE PAREDES INTERNAS` | Paredes internas | Classificação, acabamento |
| `P25. REVESTIMENTOS PISO ESCADA POR PAVIMENTO` | Pisos escada | Material por pavimento |

### 2.2 Property Sets de parâmetros importantes

| Property Set | Aplicação |
|---|---|
| `VEDAÇÃO - PARÂMETROS IMPORTANTES` | Dados-chave das paredes |
| `VEDAÇÃO - VERIFICAÇÃO DE MODELO` | Flags de controle de qualidade |
| `PISO - PARÂMETROS IMPORTANTES` | Dados-chave dos pisos |
| `FORRO - PARÂMETROS IMPORTANTES` | Dados-chave dos forros |
| `PORTA - PARÂMETROS IMPORTANTES` | Dados-chave das portas |
| `JANELAS - PARÂMETROS IMPORTANTES` | Dados-chave das janelas |
| `GUARDA-CORPO - PARÂMETROS IMPORTANTES` | Dados-chave dos guarda-corpos |
| `RODAPÉ - PARÂMETROS IMPORTANTES` | Dados-chave dos rodapés |
| `SOLEIRA - PARÂMETROS IMPORTANTES` | Dados-chave das soleiras |
| `PEITORIL - PARÂMETROS IMPORTANTES` | Dados-chave dos peitoris |
| `FACHADA PAREDES - PARÂMETROS IMPORTANTES` | Dados-chave fachada paredes |
| `FACHADA PISO - PARÂMETROS IMPORTANTES` | Dados-chave fachada pisos |
| `FACHADA FORRO - PARÂMETROS IMPORTANTES` | Dados-chave fachada forros |
| `REVESTIMENTO INTERNO - PARÂMETROS IMPORTANTES - OK` | Revestimento interno validado |

### 2.3 Psets padrão IFC

- `Pset_WallCommon`, `Pset_SlabCommon`, `Pset_DoorCommon`, `Pset_WindowCommon`
- `Pset_CoveringCommon`, `Pset_RailingCommon`, `Pset_StairCommon`
- `Pset_QuantityTakeOff` (quantitativos nativos do Revit)
- `Pset_ReinforcementBarPitchOfWall/Slab` (informação de armadura)

---

## 3. Regras de Extração — Passo a Passo

### ETAPA 0: Configuração Inicial

1. **Criar projeto:** Menu → Novo projeto a partir → A partir do IFC
2. **Importar:** `DUO_CLN_MOD_ARQ_FED_R01.ifc`
3. **Configurar EAP (4 níveis):**
   - Nível 1: Disciplina
   - Nível 2: Pavimento
   - Nível 3: Entidade
   - Nível 4: Tipo de componente

---

### ETAPA 1: ALVENARIA (IfcWallStandardCase + IfcWall)

O modelo separa paredes por função no *nome do tipo*. Isso permite criar regras muito específicas.

#### Regra 1.1 — Alvenaria Estrutural/Vedação (osso)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "ALV" E NÃO contém "DESCONSIDERAR" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Alvenaria - " |
| **Categoria EAP** | Alvenaria |
| **Descrição** | Tipo de componente (mostra espessura automaticamente) |

**Tipos que serão capturados:**
- `02_ALV 11,5 cm OSSO`
- `03_ALV 14 cm OSSO`
- `03_ALV 17 cm OSSO`
- `01_ALV 09 cm OSSO`

**Subdividir por:** Tipo de componente → gera uma linha por espessura

#### Regra 1.2 — Paredes a Desconsiderar

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "DESCONSIDERAR" |
| **Contabilizar** | ❌ DESLIGADO (não gerar quantitativo) |

**Tipos:** `00_PAREDE_DESCONSIDERAR_17 cm`, `00_PAREDE_DESCONSIDERAR_22 cm`, `00_PAREDE_DESCONSIDERAR_15 cm`

⚠️ **Importante:** Desligar a contabilização desses elementos logo no início, para não poluir a lista.

#### Regra 1.3 — Pele de Vidro

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "PELE DE VIDRO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Pele de Vidro - " |
| **Categoria EAP** | Esquadrias / Fachada |

**Tipo:** `55_PELE DE VIDRO 5cm`

#### Regra 1.4 — Painel Ventilado

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "PAINEL VENTILADO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Painel Ventilado - " |
| **Categoria EAP** | Fachada |

#### Regra 1.5 — ACF (Alvenaria de Concreto/Fechamento)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "ACF" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "ACF - " |
| **Categoria EAP** | Alvenaria |

**Tipo:** `18_ACF 15 cm`

---

### ETAPA 2: REVESTIMENTOS INTERNOS DE PAREDE (IfcWallStandardCase)

O modelo tem revestimentos modelados como paredes separadas, organizados por AMBIENTE. Isso é excelente para quantificação detalhada.

#### Regra 2.1 — Revestimento de Parede (por ambiente)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "101_REVESTIMENTO PAREDE" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Rev. Parede - " |
| **Categoria EAP** | Revestimento Interno Parede |
| **Descrição** | Tipo de componente (traz o ambiente automaticamente) |

**Subdividir por:** Tipo de componente → gera uma linha por ambiente:
- Rev. Parede - SUITE
- Rev. Parede - BANHO (SUITE)
- Rev. Parede - SALA/COZINHA
- Rev. Parede - HALL DO ELEVADOR
- Rev. Parede - CIRCULACAO
- ... (todos os ambientes)

#### Regra 2.2 — Revestimento sobre Estrutura (por ambiente)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "102_REVESTIMENTO ESTRUTURA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Rev. Estrutura - " |
| **Categoria EAP** | Revestimento Interno Parede |

**Nota:** O modelo diferencia revestimento sobre alvenaria (101) e sobre estrutura (102) — composições diferentes (chapisco diferente).

---

### ETAPA 3: RODAPÉS (IfcWallStandardCase)

#### Regra 3.1 — Rodapé (por ambiente)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "RODAPÉ" |
| **Método principal** | Comprimento (QuantityLength) ou Área |
| **Unidade** | m (comprimento) ou m² (área) |
| **Prefixo** | "Rodapé - " |
| **Categoria EAP** | Pisos / Rodapés |

**Ambientes:** Suite, Sala/Cozinha, Hall, Circulação, Copa, Depósito, Escada, Garagem, etc.

---

### ETAPA 4: REVESTIMENTO DE FACHADA (IfcWallStandardCase)

#### Regra 4.1 — Fachada sobre Parede (por cor/acabamento)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA PAREDE" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Parede - " |
| **Categoria EAP** | Fachada |

**Acabamentos de fachada identificados:**
- COR 01 - Revestimento Cerâmico
- COR 02 - Concreto Aparente
- COR 03 - Reboco com Pintura Branca
- COR 04 - Reboco com Pintura Cinza
- COR 05 - Pintura e Textura Branca (Muro de Divisa)
- COR 06 - Reboco Cru

#### Regra 4.2 — Fachada sobre Estrutura (por cor/acabamento)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA ESTRUTURA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Estrutura - " |
| **Categoria EAP** | Fachada |

---

### ETAPA 5: PISOS (IfcSlab)

O modelo tem pisos classificados por AMBIENTE no nome do tipo. Excelente para quantificação.

#### Regra 5.1 — Piso por ambiente

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "PISO" E NÃO contém "FACHADA" E NÃO contém "DEMARCAÇÃO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Piso - " |
| **Categoria EAP** | Pisos |
| **Subdividir** | Tipo de componente |

**Ambientes encontrados:** Suite, Sala/Cozinha, Banho, Hall, Circulação, Garagem, Escada, Sacada, Serviço, Copa, Zeladoria, Fitness, Lavabo, DML, Depósito, Jardim, Passeio, Acesso, Meio-fio, Bordas da Piscina, Grade Metálica, Rampa, Cobertura/Piscina, Reservatório, e outros.

#### Regra 5.2 — Demarcação de Vagas (garagem)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "DEMARCAÇÃO DE VAGAS" |
| **Método principal** | Comprimento (QuantityLength) |
| **Unidade** | m |
| **Prefixo** | "Demarcação Vagas - " |
| **Categoria EAP** | Pintura / Complementares |

#### Regra 5.3 — Soleiras

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab (tipo Soleira) |
| **Filtro** | Tipo contém "Soleira" |
| **Método principal** | Comprimento ou Área |
| **Unidade** | m ou m² |
| **Prefixo** | "Soleira - " |
| **Categoria EAP** | Pisos |

#### Regra 5.4 — Peitoris

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab (tipo Peitoril) |
| **Filtro** | Tipo contém "Peitoril" ou "PEITORIL" |
| **Método principal** | Comprimento ou Área |
| **Unidade** | m ou m² |
| **Prefixo** | "Peitoril - " |
| **Categoria EAP** | Esquadrias / Complementares |

#### Regra 5.5 — Rufo Metálico

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "RUFO" |
| **Método principal** | Comprimento (QuantityLength) |
| **Unidade** | m |
| **Prefixo** | "Rufo - " |
| **Categoria EAP** | Impermeabilização / Complementares |

#### Regra 5.6 — Revestimento Fachada (piso sobre estrutura)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA PISO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Piso - " |
| **Categoria EAP** | Fachada |

#### Regra 5.7 — Forro da Rampa

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "FORRO - RAMPA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Categoria EAP** | Tetos |

#### Regra 5.8 — Patamar Escada

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab (tipo Patamar monolítico) |
| **Filtro** | Tipo contém "Patamar" |
| **Método principal** | Área ou Volume |
| **Categoria EAP** | Supraestrutura / Escadas |

---

### ETAPA 6: PORTAS (IfcDoor)

#### Regra 6.1 — Portas (todas, subdivididas por tipo)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcDoor |
| **Filtro** | NÃO contém "ELEVADOR" E NÃO contém "ALCAPAO" |
| **Método principal** | Quantidade (un) — usar propriedade fixa = 1 |
| **Unidade** | un |
| **Categoria EAP** | Esquadrias |
| **Subdividir** | Tipo (DoorStyle) |

**Tipos identificados (únicos):**
- P1 - Porta de Abrir, 2 Folhas, Alumínio Veneziana (120x210, 100x210)
- P2 - Porta de Correr, 2 Folhas, Alumínio Veneziana (200x210, 165x210, 200x190)
- P3 - Porta de Abrir, 1 Folha, Alumínio Veneziana (90x180)
- P4 - Porta de Abrir, 1 Folha, Alumínio e Vidro (80x240)
- P5 - Porta de Abrir, 1 Folha, Alumínio Veneziana (90x180)
- P6 - Porta de Abrir, 1 Folha, Corta Fogo (80x210)
- P7 - Porta de Abrir, 1 Folha, Alumínio Veneziana (82x210) / Madeira (90x210)
- P8 - Porta de Abrir, 1 Folha, Madeira (80x210)
- P9 - Porta de Abrir, 1 Folha, Madeira (70x210)
- P10 - Porta de Abrir, 1 Folha, Madeira (80x210)
- P11 - Porta de Correr, 2 Folhas, Alumínio e Vidro (260x240)
- P12 - Porta de Correr, 2 Folhas, Alumínio e Vidro (260x240) / Corta Fogo (82x210)
- P13 - Porta de Abrir, 1 Folha, Alumínio e Vidro (100x240)
- P14 - Porta de Abrir, 1 Folha, Madeira (60x210)
- P15 - Porta de Abrir, 1 Folha, Corta Fogo (60x210)
- P17 - Porta de Abrir, 1 Folha, Alumínio e Vidro (150x240)
- P19 - Porta de Correr, 4 Folhas, Alumínio e Vidro (460x240)
- P20 - Porta de Correr, 4 Folhas, Alumínio e Vidro (600x240)
- P21 - Porta de Abrir, 1 Folha, Alumínio Veneziana (80x200)
- P22 - Porta de Abrir, 1 Folha, Alumínio e Vidro (170x240)
- PT1 - Portão Basculante, Aço Galvanizado e Vidro (300x250)
- PT2 - Portão de Correr, Alumínio/Aço/Vidro (215x250)
- PT4 - Portão Basculante, Aço Galvanizado (375x310)
- E1 - Porta de Correr, 2 Folhas, Alumínio e Vidro (299x302)
- E3 - Porta Fixa, 1 Folha, Alumínio e Vidro (188x302)

#### Regra 6.2 — Aberturas de Elevador

| Campo | Configuração |
|---|---|
| **Entidade** | IfcDoor |
| **Filtro** | Tipo contém "ELEVADOR" |
| **Método principal** | Quantidade (un) |
| **Prefixo** | "Abertura Elevador - " |
| **Categoria EAP** | Sistemas Especiais |

#### Regra 6.3 — Alçapão

| Campo | Configuração |
|---|---|
| **Entidade** | IfcDoor |
| **Filtro** | Tipo contém "ALCAPAO" |
| **Método principal** | Quantidade (un) |
| **Prefixo** | "Alçapão - " |
| **Categoria EAP** | Complementares |

---

### ETAPA 7: JANELAS (IfcWindow)

#### Regra 7.1 — Janelas (todas, subdivididas por tipo)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWindow |
| **Método principal** | Quantidade (un) |
| **Unidade** | un |
| **Categoria EAP** | Esquadrias |
| **Subdividir** | Tipo (WindowStyle) |

**Tipos identificados:**
- J1 - Janela Maxim-ar, 1+1 Folhas, Alumínio e Vidro (80x220)
- J2 - Janela Fixa, 1 Folha, Alumínio Veneziana (180x172)
- J3 - Janela Correr, 2+1 Folhas, Alumínio e Vidro (140x170)
- J4 - Janela Maxim-ar, 6+1 Folhas, Alumínio e Vidro (500x70)
- J5 - Janela Fixa, 1 Folha, Tela Aço Galvanizado (105x80)
- J6 - Janela Fixa, 1 Folha, Tela Aço Galvanizado (105x80)
- J7 - Janela Maxim-ar, 1+1 Folhas, Alumínio e Vidro (50x70)
- J9 - Janela Correr, 2+1 Folhas, Alumínio e Vidro (180x170)
- J10 - Janela Correr, 2 Folhas, Alumínio com Veneziana (180x70)
- J11 - Janela Correr, 2 Folhas, Alumínio com Veneziana (150x70)
- J12 - Janela Maxim-ar, 1+1 Folhas, Alumínio e Vidro (80x220)
- J13 - Janela Fixa, 1 Folha, Tela Aço Galvanizado (180x50)
- E2 - Janela Correr, 5 Folhas, Alumínio e Vidro (194.8x302)
- E4 - Janela Correr, 1+1 Folhas, Alumínio e Vidro (81x242)
- E5 - Janela Correr, 5+1 Folhas, Alumínio e Vidro (760x220)

---

### ETAPA 8: FORROS / TETOS (IfcCovering)

#### Regra 8.1 — Forro (por ambiente)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcCovering |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Forro - " |
| **Categoria EAP** | Tetos |
| **Subdividir** | Tipo de componente |

**Ambientes:** Suite, Sala/Cozinha, Banho, Hall, Circulação, Escada, Elevador, Lavabo, Sacada, DML, Copa, Zeladoria, Fitness, Garagem, Grill Rooftop, e outros.

⚠️ **Atenção:** Existem também tipos de forro para projeção de pavimento superior e projeção de cobertura — avaliar se devem ser quantificados ou desligados.

---

### ETAPA 9: GUARDA-CORPOS E VENEZIANAS (IfcRailing)

#### Regra 9.1 — Guarda-corpo (por tipo)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcRailing |
| **Método principal** | Comprimento (QuantityLength) |
| **Unidade** | m |
| **Categoria EAP** | Esquadrias / Guarda-corpos |
| **Subdividir** | Tipo |

**Tipos:**
- Guarda-corpo Alumínio e Vidro, H=110 cm
- Guarda-corpo Alumínio e Vidro, H=160 cm
- Guarda-corpo Metálico, H=120 cm
- Veneziana Ar-condicionado, H=110 cm
- Veneziana Chaminé, H=40 cm
- Corrimão Escada Parede - Madeira

---

### ETAPA 10: ESCADAS (IfcStair + IfcStairFlight)

#### Regra 10.1 — Lances de Escada

| Campo | Configuração |
|---|---|
| **Entidade** | IfcStairFlight |
| **Método principal** | Volume ou Área |
| **Categoria EAP** | Supraestrutura / Escadas |

---

### ETAPA 11: VERGAS E CONTRAVERGAS (IfcBuildingElementProxy)

#### Regra 11.1 — Verga de Portas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Verga Portas" |
| **Método principal** | Volume (QuantityVolume) ou Comprimento |
| **Unidade** | m³ ou m |
| **Prefixo** | "Verga Porta - " |
| **Categoria EAP** | Alvenaria / Complementares |

#### Regra 11.2 — Verga de Janelas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Verga Janelas" |
| **Método principal** | Volume ou Comprimento |
| **Prefixo** | "Verga Janela - " |
| **Categoria EAP** | Alvenaria / Complementares |

#### Regra 11.3 — Contraverga de Janelas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Contraverga Janelas" |
| **Método principal** | Volume ou Comprimento |
| **Prefixo** | "Contraverga - " |
| **Categoria EAP** | Alvenaria / Complementares |

#### Regra 11.4 — Faixas de Garagem

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "FAIXAS DE GARAGEM" |
| **Método principal** | Comprimento ou Área |
| **Prefixo** | "Faixas Garagem - " |
| **Categoria EAP** | Pintura / Complementares |

#### Regra 11.5 — Escada Marinheiro

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Escada Marinheiro" |
| **Método principal** | Quantidade (un) |
| **Categoria EAP** | Complementares |

#### Regra 11.6 — Elementos de Texto/Desconsiderar

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Texto do modelo" |
| **Contabilizar** | ❌ DESLIGADO |

---

## 4. Sugestão de EAP Final (Estrutura Analítica)

```
1. ALVENARIA
   1.1 Alvenaria 9 cm
   1.2 Alvenaria 11,5 cm
   1.3 Alvenaria 14 cm
   1.4 Alvenaria 17 cm
   1.5 ACF 15 cm
   1.6 Vergas (portas + janelas)
   1.7 Contravergas

2. REVESTIMENTO INTERNO PAREDE
   2.1 Revestimento sobre Alvenaria (por ambiente)
   2.2 Revestimento sobre Estrutura (por ambiente)

3. PISOS
   3.1 Piso por ambiente
   3.2 Soleiras
   3.3 Rodapés (por ambiente)
   3.4 Demarcação de vagas

4. TETOS / FORROS
   4.1 Forro por ambiente

5. FACHADA
   5.1 Revestimento Cerâmico (COR 01)
   5.2 Concreto Aparente (COR 02)
   5.3 Reboco + Pintura Branca (COR 03)
   5.4 Reboco + Pintura Cinza (COR 04)
   5.5 Textura Branca - Muro (COR 05)
   5.6 Reboco Cru (COR 06)
   5.7 Pele de Vidro
   5.8 Painel Ventilado

6. ESQUADRIAS
   6.1 Portas (por tipo P1-P22)
   6.2 Portões (PT1, PT2, PT4)
   6.3 Janelas (por tipo J1-J13, E2-E5)
   6.4 Guarda-corpos
   6.5 Venezianas AC
   6.6 Peitoris

7. IMPERMEABILIZAÇÃO
   7.1 Impermeabilização Parede (dados da B18)
   7.2 Rufos

8. ESCADAS
   8.1 Lances
   8.2 Patamares
   8.3 Corrimãos

9. COMPLEMENTARES
   9.1 Faixas garagem
   9.2 Escada marinheiro
   9.3 Alçapão
```

---

## 5. Dicas Importantes para este Modelo

### ✅ Pontos fortes
- **Modelo extremamente rico** em metadados — tabelas CTN com informações detalhadas por ambiente
- **Nomenclatura padronizada** — fácil de criar filtros (códigos 01_, 02_, 101_, 102_, P1-P22, J1-J13)
- **Separação revestimento alvenaria vs estrutura** (101 vs 102) — permite composições diferentes
- **Fachada com cores/acabamentos** — quantificação precisa por tipo de acabamento
- **Vergas e contravergas modeladas** — raro e muito valioso
- **Pset_QuantityTakeOff** presente — quantitativos nativos do Revit disponíveis

### ⚠️ Atenção
- **Paredes "DESCONSIDERAR"** — desligar ANTES de gerar lista (senão inflam a área de alvenaria)
- **Textos modelados** (IfcBuildingElementProxy "Texto do modelo") — desligar
- **Aberturas de elevador** (IfcDoor tipo ELEVADOR) — não são portas reais, separar
- **Pisos de fachada** (IfcSlab com "REVESTIMENTO FACHADA") — classificar como fachada, não piso
- **Forro de projeção** — avaliar se é forro real ou só referência de projeto

### 🔢 Ordem recomendada de configuração
1. Desligar elementos a desconsiderar (Paredes, Textos)
2. Configurar EAP (4 níveis)
3. Regras de Alvenaria (por espessura)
4. Regras de Revestimento (separar 101 vs 102)
5. Regras de Pisos (por ambiente)
6. Regras de Fachada (por cor)
7. Regras de Esquadrias (por tipo)
8. Regras de Forros
9. Elementos complementares (vergas, rodapés, etc.)
10. Verificação final + Atualizar lista

---

*Documento gerado em 23/03/2026 a partir da análise do IFC `DUO_CLN_MOD_ARQ_FED_R01.ifc`*
*Cartesian Engenharia — Jarvis 🦞*
