# Regras de Extração de Quantitativos — Visus Cost Management
## Projeto: THZ ELE — Torre A (Modelo Arquitetônico — 1º Pavto Tipo)

**Arquivo:** `ifc-teste` (original: `THZ_ELE_MOD_ARQ_TORRE_A_R03.ifc`)
**Tamanho:** ~30 MB
**Software origem:** Revit 2024 (PTB) — exportação nativa IFC
**Schema:** IFC2X3
**Data exportação:** 16/01/2026
**Escopo:** 1 pavimento tipo (08_1º PAVTO TIPO) — cota 2250 cm

---

## 1. Estrutura do Modelo

### 1.1 Pavimentos

| # | Pavimento | Cota (cm) |
|---|-----------|-----------|
| 08 | 1º Pavto Tipo | 2250 |

⚠️ Modelo contém apenas 1 pavimento — ideal para aula/teste. Multiplicar quantitativos pelo nº de pavimentos tipo para estimativa total.

### 1.2 Entidades BIM (elementos construtivos)

| Entidade IFC | Quantidade | O que representa |
|---|---|---|
| IfcWallStandardCase | 2.067 | Paredes padrão (alvenaria, revestimentos, fachada, rodapés) |
| IfcWall | 174 | Paredes não-padrão |
| IfcSlab | 174 | Pisos, soleiras, peitoris |
| IfcBuildingElementProxy | 149 | Vergas, contravergas, molduras, textos |
| IfcCovering | 52 | Forros |
| IfcDoor | 49 | Portas |
| IfcWindow | 35 | Janelas |
| IfcRailing | 18 | Guarda-corpos e corrimãos |

**Total de elementos construtivos quantificáveis: ~2.718**

---

## 2. Property Sets Disponíveis (Metadados)

### 2.1 Tabelas CTN (customizadas — prefixo T)

| Property Set | Aplicação | O que contém |
|---|---|---|
| `T02. TABELA DE ALVENARIAS` | Paredes (alvenaria geral) | Tipo bloco, espessura |
| `T03. TABELA REVEST PAREDES` | Revestimento interno parede | Material, acabamento |
| `T04. TABELA REVEST FACHADAS - PAREDES` | Fachada sobre paredes | Cor, material externo |
| `T05. TABELA REVEST FACHADAS - PISOS` | Fachada sobre pisos | Cor, material |
| `T07. TABELA REVEST PISO` | Pisos | Material, acabamento |
| `T08. TABELA CONTRAPISOS` | Contrapisos | Espessura, tipo |
| `T12. TABELA DE TETOS` | Forros | Tipo, material |
| `T13. TABELA DE PORTAS TOTAL` | Portas | Material, dimensões, tipo |
| `T14. TABELA DE JANELAS TOTAL` | Janelas | Material, dimensões, tipo |
| `T18. TABELA DE GUARDA CORPOS` | Guarda-corpos | Material, altura |
| `T19. TABELA DE RODAPES` | Rodapés | Material, altura |
| `T20. TABELA PINGADEIRAS/PEITORIL` | Peitoris e pingadeiras | Material |
| `T24. TABELA DE ALVENARIAS EXTERNAS` | Paredes externas | Classificação |
| `T25. TABELA DE ALVENARIAS INTERNAS` | Paredes internas | Classificação |
| `T26. TABELA REBOCO INTERNO POR TIPO` | Reboco interno detalhado | Por tipo de parede |
| `T27. SOLEIRAS POR PAVIMENTO` | Soleiras | Por pavimento |

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
| `FACHADA PISO - PARÂMETROS IMPORTANTES` | Dados-chave fachada pisos |
| `MOLDURAS - PARÂMETROS IMPORTANTES` | Dados-chave das molduras |
| `MULTICATEGORIA - REVESTS POR AMBIENTE` | Resumo revestimentos por ambiente |

### 2.3 Diferenças em relação ao DUO CLN

| Item | DUO CLN | THZ Torre A |
|---|---|---|
| Prefixo tabelas | B (B02, B04...) | T (T02, T03...) |
| Tabela contrapisos | Não tem | T08 ✅ |
| Tabela reboco por tipo | Não tem | T26 ✅ |
| Tabela alv. interna/externa | Não tem separado | T24 + T25 ✅ |
| Tabela pingadeiras | Não tem | T20 ✅ |
| Tabela soleiras por pvto | Não tem | T27 ✅ |
| Molduras fachada | Não tem | Tem (IfcBuildingElementProxy) ✅ |

---

## 3. Regras de Extração — Passo a Passo

### ETAPA 0: Configuração Inicial

1. **Criar projeto:** Menu → Novo projeto a partir → A partir do IFC
2. **Importar:** `ifc-teste` (THZ_ELE_MOD_ARQ_TORRE_A_R03.ifc)
3. **Configurar EAP (3 níveis):** — modelo tem 1 pavimento
   - Nível 1: Disciplina
   - Nível 2: Entidade
   - Nível 3: Tipo de componente

---

### ETAPA 1: ALVENARIA (IfcWallStandardCase + IfcWall)

#### Regra 1.1 — Alvenaria de Vedação (osso)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "ALV" E NÃO contém "CONC" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Alvenaria - " |
| **Categoria EAP** | Alvenaria |
| **Subdividir** | Tipo de componente |

**Tipos capturados:**
- `01_ALV 05 cm OSSO`
- `01_ALV 09 cm OSSO`
- `02_ALV 11,5 cm OSSO`
- `03_ALV 14 cm OSSO`
- `04_ALV 19 cm OSSO`

#### Regra 1.2 — Alvenaria de Concreto

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "ALV CONC" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Alv. Concreto - " |
| **Categoria EAP** | Alvenaria |

**Tipo:** `08_ALV CONC 05 cm OSSO`

#### Regra 1.3 — ACF (Alvenaria de Concreto/Fechamento)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "ACF" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "ACF - " |
| **Categoria EAP** | Alvenaria |

**Tipos:** `17_ACF 12,5 cm`, `18_ACF 15 cm`

#### Regra 1.4 — Refratário

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "REFRATARIO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Refratário - " |
| **Categoria EAP** | Alvenaria / Complementares |

**Tipo:** `40_REFRATARIO 1,6 cm`

#### Regra 1.5 — Pele de Vidro

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "PELE DE VIDRO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Pele de Vidro - " |
| **Categoria EAP** | Esquadrias / Fachada |

**Tipo:** `65_PELE DE VIDRO 7cm`

---

### ETAPA 2: REVESTIMENTOS INTERNOS DE PAREDE (IfcWallStandardCase)

#### Regra 2.1 — Revestimento sobre Parede/Alvenaria (101)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "101_REVESTIMENTO PAREDE" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Rev. Parede - " |
| **Categoria EAP** | Revestimento Interno Parede |
| **Subdividir** | Tipo de componente |

**Ambientes:**
- Living, Suite, BWC, Box BWC, Cozinha, Lavabo
- Área Serviço (Tipo + Tipo 2), Circ., Circ e Rouparia
- Hall do Pavimento, Antecâmara, Escada Press., Elevador
- Duto DEA, Duto DEF, Duto Press.

#### Regra 2.2 — Revestimento sobre Estrutura (102)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "102_REVESTIMENTO ESTRUTURA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Rev. Estrutura - " |
| **Categoria EAP** | Revestimento Interno Parede |
| **Subdividir** | Tipo de componente |

**Mesmos ambientes da regra 2.1** — separação permite composição diferente (chapisco sobre concreto vs chapisco sobre alvenaria).

#### Regra 2.3 — Revestimento Espelho de Escada (104)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "104_REVESTIMENTO ESPELHO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Rev. Espelho Escada - " |
| **Categoria EAP** | Revestimento Interno Parede |

**Tipo:** `104_REVESTIMENTO ESPELHO ESCADA - ESCADA PRESSURIZADA`

---

### ETAPA 3: RODAPÉS (IfcWallStandardCase)

#### Regra 3.1 — Rodapé por ambiente

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "RODAPÉ" |
| **Método principal** | Comprimento (QuantityLength) ou Área |
| **Unidade** | m ou m² |
| **Prefixo** | "Rodapé - " |
| **Categoria EAP** | Pisos / Rodapés |
| **Subdividir** | Tipo de componente |

**Ambientes:** Suite, Living, Cozinha, BWC, Box BWC, Lavabo, Área Serviço, Circ., Circ e Rouparia, Antecâmara, Escada, Sacada

---

### ETAPA 4: REVESTIMENTO DE FACHADA (IfcWallStandardCase)

#### Regra 4.1 — Fachada sobre Parede

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA PAREDE" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Parede - " |
| **Categoria EAP** | Fachada |
| **Subdividir** | Tipo de componente |

**Cores/acabamentos:**
- COR 01 - NOME DA COR (a definir)
- COR 06 - NOME DA COR (a definir)
- COR 13 - NOME DA COR (a definir)

⚠️ *Nomes genéricos ("NOME DA COR")* — modelo ainda em desenvolvimento. Os nomes reais serão definidos pelo projetista.

#### Regra 4.2 — Fachada sobre Estrutura

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWallStandardCase |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA ESTRUTURA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Estrutura - " |
| **Categoria EAP** | Fachada |

**Cores:** COR 01, COR 02

---

### ETAPA 5: PISOS (IfcSlab)

#### Regra 5.1 — Piso por ambiente

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "PISO" E NÃO contém "FACHADA" E NÃO contém "PISADA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Piso - " |
| **Categoria EAP** | Pisos |
| **Subdividir** | Tipo de componente |

**Ambientes:** Suite, Living, Cozinha, BWC, Lavabo, Área Serviço, Circ., Circ e Rouparia, Circ. Descoberta, Hall do Pavimento, Antecâmara, Escada, Sacada, Área Técnica

#### Regra 5.2 — Pisada de Escada

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "PISADA ESCADA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Pisada Escada - " |
| **Categoria EAP** | Escadas |

#### Regra 5.3 — Soleiras

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab (tipo CTN_Soleira) |
| **Filtro** | Tipo contém "Soleira" |
| **Método principal** | Comprimento ou Área |
| **Unidade** | m ou m² |
| **Prefixo** | "Soleira - " |
| **Categoria EAP** | Pisos |

#### Regra 5.4 — Peitoris

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab (tipo CTN_Peitoril ou PEITORIL) |
| **Filtro** | Tipo contém "Peitoril" ou "PEITORIL" |
| **Método principal** | Comprimento ou Área |
| **Unidade** | m ou m² |
| **Prefixo** | "Peitoril - " |
| **Categoria EAP** | Esquadrias / Complementares |

#### Regra 5.5 — Revestimento Fachada (piso sobre estrutura/alvenaria)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "REVESTIMENTO FACHADA PISO" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Fachada Piso - " |
| **Categoria EAP** | Fachada |
| **Subdividir** | Tipo de componente |

**Tipos:** Sobre Estrutura COR 01, Sobre Estrutura COR 13, Sobre Alvenaria COR 01

#### Regra 5.6 — Forro da Escada (modelado como Slab)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcSlab |
| **Filtro** | Tipo contém "FORRO - ESCADA" |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Categoria EAP** | Tetos |

---

### ETAPA 6: PORTAS (IfcDoor)

#### Regra 6.1 — Portas (subdivididas por tipo)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcDoor |
| **Filtro** | NÃO contém "ELEVADOR" |
| **Método principal** | Quantidade (un) |
| **Unidade** | un |
| **Categoria EAP** | Esquadrias |
| **Subdividir** | Tipo (DoorStyle) |

**Tipos identificados:**
- P01 - Porta de Abrir, 1 Folha, Madeira (60x210)
- P02 - Porta de Abrir, 1 Folha, Madeira (70x210)
- P03 - Porta de Abrir, 1 Folha, Madeira (80x210)
- P07 - Porta de Abrir, 1 Folha, Madeira (90x210)
- P0XX - Porta de Correr, 1 Folha, A Definir (70x210) ⚠️
- PCF03 - Porta de Abrir, 1 Folha, Aço Galvanizado (100x210) — Corta-fogo
- PV05 - Porta de Correr, 3 Folhas, Alumínio e Vidro (175x230 e 300x230)
- PV07 - Porta de Correr, 4 Folhas, Alumínio e Vidro (320x210)

⚠️ `P0XX` = porta a definir — modelo em fase de desenvolvimento

#### Regra 6.2 — Abertura de Elevador

| Campo | Configuração |
|---|---|
| **Entidade** | IfcDoor |
| **Filtro** | Tipo contém "ELEVADOR" |
| **Contabilizar** | Separar ou desligar (não é porta real) |
| **Prefixo** | "Abertura Elevador" |
| **Categoria EAP** | Sistemas Especiais |

---

### ETAPA 7: JANELAS (IfcWindow)

#### Regra 7.1 — Janelas (subdivididas por tipo)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcWindow |
| **Método principal** | Quantidade (un) |
| **Unidade** | un |
| **Categoria EAP** | Esquadrias |
| **Subdividir** | Tipo (WindowStyle) |

**Tipos identificados:**
- J01 - Maxim-ar, 1 Folha, Alumínio e Vidro (55x75)
- J02 - Correr, 1+1 Folhas, Alumínio e Vidro (70x124)
- J06 - Correr, 2 Folhas, Alumínio e Vidro (115x110)
- J07 - Correr, 2 Folhas, Alumínio e Vidro (115x120)
- J08 - Correr, 2 Folhas, Alumínio e Vidro (115x209)
- J09 - Correr, 2 Folhas, Alumínio e Vidro (125x209)
- J11 - Correr, 2 Folhas, Alumínio e Vidro (135x209)
- J14 - Correr, 2 Folhas, Alumínio e Vidro (165x110)
- J18 - Correr, 2 Folhas, Alumínio e Vidro (85x110)
- GR01 - Fixa, Tela Aço Galvanizado (46x43) — grelha
- GR02 - Fixa, Tela Aço Galvanizado (162x200) — grelha
- GR04 - Fixa, Tela Aço Galvanizado (110x76) — grelha

**Dica:** Separar janelas reais (J) de grelhas (GR) com filtro no tipo.

---

### ETAPA 8: FORROS / TETOS (IfcCovering)

#### Regra 8.1 — Forro por ambiente

| Campo | Configuração |
|---|---|
| **Entidade** | IfcCovering |
| **Método principal** | Área (QuantityArea) |
| **Unidade** | m² |
| **Prefixo** | "Forro - " |
| **Categoria EAP** | Tetos |
| **Subdividir** | Tipo de componente |

**Ambientes:** Suite, Living, Cozinha, BWC, Lavabo, Área Serviço, Circ., Circ e Rouparia, Hall do Pavimento, Antecâmara, Escada, Sacada

---

### ETAPA 9: GUARDA-CORPOS (IfcRailing)

#### Regra 9.1 — Guarda-corpo por tipo

| Campo | Configuração |
|---|---|
| **Entidade** | IfcRailing |
| **Método principal** | Comprimento (QuantityLength) |
| **Unidade** | m |
| **Categoria EAP** | Esquadrias / Guarda-corpos |
| **Subdividir** | Tipo |

**Tipos:**
- GP01, GP02, GP03, GP04 - Guarda-corpo Alumínio e Vidro, 80 cm
- GP10, GP11, GP14 - Guarda-corpo Metálico, 90 cm
- Corrimão Escada Parede - Madeira

---

### ETAPA 10: VERGAS, CONTRAVERGAS E MOLDURAS (IfcBuildingElementProxy)

#### Regra 10.1 — Verga de Portas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Verga Portas" |
| **Método principal** | Volume ou Comprimento |
| **Prefixo** | "Verga Porta - " |
| **Categoria EAP** | Alvenaria |

#### Regra 10.2 — Verga de Janelas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Verga Janelas" |
| **Método principal** | Volume ou Comprimento |
| **Prefixo** | "Verga Janela - " |
| **Categoria EAP** | Alvenaria |

#### Regra 10.3 — Contraverga de Janelas

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Contraverga" |
| **Método principal** | Volume ou Comprimento |
| **Prefixo** | "Contraverga - " |
| **Categoria EAP** | Alvenaria |

#### Regra 10.4 — Molduras de Fachada

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Molduras_Fachada" |
| **Método principal** | Comprimento ou Área |
| **Prefixo** | "Moldura Fachada - " |
| **Categoria EAP** | Fachada |

#### Regra 10.5 — Textos (desconsiderar)

| Campo | Configuração |
|---|---|
| **Entidade** | IfcBuildingElementProxy |
| **Filtro** | Tipo contém "Texto_Modelo" |
| **Contabilizar** | ❌ DESLIGADO |

---

## 4. Sugestão de EAP Final

```
1. ALVENARIA
   1.1 Alvenaria 05 cm
   1.2 Alvenaria 09 cm
   1.3 Alvenaria 11,5 cm
   1.4 Alvenaria 14 cm
   1.5 Alvenaria 19 cm
   1.6 Alvenaria Concreto 05 cm
   1.7 ACF 12,5 cm
   1.8 ACF 15 cm
   1.9 Refratário
   1.10 Vergas (portas + janelas)
   1.11 Contravergas

2. REVESTIMENTO INTERNO PAREDE
   2.1 Revestimento sobre Alvenaria - 101 (por ambiente)
   2.2 Revestimento sobre Estrutura - 102 (por ambiente)
   2.3 Revestimento Espelho Escada - 104

3. PISOS
   3.1 Piso por ambiente
   3.2 Pisada escada
   3.3 Soleiras
   3.4 Rodapés (por ambiente)

4. TETOS / FORROS
   4.1 Forro por ambiente

5. FACHADA
   5.1 Fachada Parede (COR 01, 06, 13)
   5.2 Fachada Estrutura (COR 01, 02)
   5.3 Fachada Piso (COR 01, 13)
   5.4 Pele de Vidro
   5.5 Molduras

6. ESQUADRIAS
   6.1 Portas madeira (P01-P07)
   6.2 Portas alumínio/vidro (PV05, PV07)
   6.3 Porta corta-fogo (PCF03)
   6.4 Janelas alumínio/vidro (J01-J18)
   6.5 Grelhas (GR01-GR04)
   6.6 Guarda-corpos alumínio/vidro (GP01-04)
   6.7 Guarda-corpos metálicos (GP10-14)
   6.8 Peitoris

7. ESCADAS
   7.1 Pisadas
   7.2 Corrimão madeira

8. COMPLEMENTARES
   8.1 Refratário (churrasqueira)
```

---

## 5. Dicas Importantes para este Modelo

### ✅ Pontos fortes
- **Modelo leve** (~30 MB) — ideal para treino/aula
- **Nomenclatura padronizada CTN** — mesma lógica do DUO CLN
- **Tabelas extras** que o DUO CLN não tem: T08 (contrapisos), T26 (reboco por tipo), T24/T25 (alv. ext/int separadas), T27 (soleiras por pvto)
- **Pset_QuantityTakeOff** presente
- **Revestimento espelho escada (104)** — nível de detalhe raro
- **Molduras de fachada modeladas** como proxy

### ⚠️ Atenção
- **1 pavimento apenas** — multiplicar quantitativos para total do edifício
- **Cores de fachada genéricas** ("NOME DA COR") — projeto em fase inicial
- **Porta P0XX** ("A DEFINIR") — item pendente de especificação
- **Textos modelados** (CTN_Texto_Modelo) — desligar antes de gerar lista
- **Grelhas (GR)** modeladas como janelas — separar na classificação

### 🔢 Ordem recomendada de configuração
1. Desligar Textos (IfcBuildingElementProxy → CTN_Texto_Modelo)
2. Configurar EAP (3 níveis)
3. Regras de Alvenaria (5 espessuras + ACF + concreto + refratário)
4. Regras de Revestimento (101, 102, 104)
5. Regras de Pisos (por ambiente + pisada escada)
6. Regras de Fachada (por cor — parede, estrutura, piso)
7. Regras de Esquadrias (portas por tipo + janelas + grelhas separadas)
8. Regras de Forros
9. Guarda-corpos e corrimãos
10. Vergas, contravergas e molduras
11. Rodapés e soleiras
12. Verificação final + Atualizar lista

---

## 6. Comparativo THZ vs DUO CLN (para aula)

| Aspecto | THZ Torre A | DUO CLN |
|---|---|---|
| Pavimentos | 1 (tipo) | 25 (completo) |
| Tamanho | 30 MB | 279 MB |
| Paredes | 2.241 | 18.684 |
| Portas | 49 (10 tipos) | 470 (25 tipos) |
| Janelas | 35 (12 tipos) | 294 (15 tipos) |
| Tabelas CTN | T (mais completas) | B (padrão) |
| Fachada | 5 cores (genéricas) | 6 cores (definidas) |
| Molduras | ✅ Modeladas | ❌ Não tem |
| Contrapisos | ✅ T08 | ❌ Não tem |

**Recomendação para aula:** Usar o THZ (leve, 1 pvto, rápido de carregar) para demonstrar o fluxo, depois mostrar o DUO CLN como exemplo de modelo completo.

---

*Documento gerado em 23/03/2026 a partir da análise do IFC `THZ_ELE_MOD_ARQ_TORRE_A_R03.ifc`*
*Cartesian Engenharia — Jarvis 🦞*
