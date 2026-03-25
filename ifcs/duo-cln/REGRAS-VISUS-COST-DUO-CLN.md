# Regras de Extração de Quantitativos — Visus Cost
## Projeto: DUO CLN (IFC Teste)

---

## 1. Resumo do Modelo IFC

- *Pavimento:* 08_1° PAVTO TIPO (nível +2250mm)
- *Formato:* IFC2X3
- *Origem:* Revit (famílias com prefixo CTN_)
- *Total de elementos:* ~2.700

**Contagem por tipo:**
- Paredes (IfcWallStandardCase): 2.067
- Paredes (IfcWall): 174
- Lajes/Pisos (IfcSlab): 174
- Portas (IfcDoor): 49
- Janelas (IfcWindow): 35
- Forros (IfcCovering): 52
- Genéricos/Proxy (IfcBuildingElementProxy): 149

**Quantidades embarcadas no IFC:**
- IfcQuantityLength (Comprimento, Altura, Largura, Profundidade, Perímetro)
- IfcQuantityArea (Área, Área Bruta, Área Lateral Bruta/Líquida, Área do Forro, Área da Projeção)
- IfcQuantityVolume (Volume, Volume Bruto, Volume Líquido)

---

## 2. Mapeamento de Tipos e Famílias

### 2.1 Alvenarias (Paredes Estruturais/Vedação)

| Tipo no IFC | Espessura | Filtro Visus |
|---|---|---|
| 01_ALV 05 cm OSSO | 5 cm | Name contains "ALV 05" |
| 01_ALV 09 cm OSSO | 9 cm | Name contains "ALV 09" |
| 02_ALV 11,5 cm OSSO | 11,5 cm | Name contains "ALV 11,5" |
| 03_ALV 14 cm OSSO | 14 cm | Name contains "ALV 14" |
| 04_ALV 19 cm OSSO | 19 cm | Name contains "ALV 19" |
| 08_ALV CONC 05 cm OSSO | 5 cm (concreto) | Name contains "ALV CONC" |

### 2.2 Divisórias Leves

| Tipo no IFC | Espessura | Filtro Visus |
|---|---|---|
| 17_ACF 12,5 cm | 12,5 cm | Name contains "ACF 12,5" |
| 18_ACF 15 cm | 15 cm | Name contains "ACF 15" |

### 2.3 Outros Tipos de Parede

| Tipo no IFC | Uso | Filtro Visus |
|---|---|---|
| 40_REFRATARIO 1,6 cm | Refratário | Name contains "REFRATARIO" |
| 65_PELE DE VIDRO 7cm | Pele de vidro | Name contains "PELE DE VIDRO" |

### 2.4 Revestimentos de Parede (modelados como IfcWall)

Todos os revestimentos seguem o padrão: `101_REVESTIMENTO PAREDE - [AMBIENTE]` ou `102_REVESTIMENTO ESTRUTURA - [AMBIENTE]`

**Ambientes identificados:**
- LIVING - TIPO
- SUITE
- BWC - TIPO
- BOX BWC - TIPO
- COZINHA - TIPO
- AREA SERVICO - TIPO / TIPO 2
- LAVABO - TIPO
- CIRC. - TIPO
- CIRC E ROUPARIA
- HALL DO PAVIMENTO - TIPO
- ANTECAMARA
- DUTO - DEA / DEF / PRESS
- ELEV.
- ESCADA PRESS.

### 2.5 Revestimentos de Fachada (modelados como IfcWall)

| Tipo no IFC | Filtro Visus |
|---|---|
| REVESTIMENTO FACHADA PAREDE - COR 01 | Name contains "FACHADA PAREDE - COR 01" |
| REVESTIMENTO FACHADA PAREDE - COR 06 | Name contains "FACHADA PAREDE - COR 06" |
| REVESTIMENTO FACHADA PAREDE - COR 13 | Name contains "FACHADA PAREDE - COR 13" |
| REVESTIMENTO FACHADA ESTRUTURA - COR 01 | Name contains "FACHADA ESTRUTURA - COR 01" |
| REVESTIMENTO FACHADA ESTRUTURA - COR 02 | Name contains "FACHADA ESTRUTURA - COR 02" |

### 2.6 Rodapés (modelados como IfcWall)

Todos seguem o padrão: `RODAPÉ - [AMBIENTE]`

**Ambientes:** LIVING, SUITE, BWC, BOX BWC, COZINHA, AREA SERVICO, LAVABO, CIRC., CIRC E ROUPARIA, ANTECAMARA, SACADA, ESCADA PRESSURIZADA

### 2.7 Pisos/Lajes (IfcSlab)

| Tipo no IFC | Filtro Visus |
|---|---|
| PISO - LIVING - TIPO | Name contains "PISO - LIVING" |
| PISO - SUITE | Name contains "PISO - SUITE" |
| PISO - BWC - TIPO | Name contains "PISO - BWC" |
| PISO - COZINHA - TIPO | Name contains "PISO - COZINHA" |
| PISO - AREA SERVICO - TIPO | Name contains "PISO - AREA SERVICO" |
| PISO - AREA TECNICA TIPO | Name contains "PISO - AREA TECNICA" |
| PISO - LAVABO - TIPO | Name contains "PISO - LAVABO" |
| PISO - CIRC. - TIPO | Name contains "PISO - CIRC." |
| PISO - CIRC. DESCOBERTA - TIPO | Name contains "PISO - CIRC. DESCOBERTA" |
| PISO - CIRC E ROUPARIA | Name contains "PISO - CIRC E ROUP" |
| PISO - HALL DO PAVIMENTO - TIPO | Name contains "PISO - HALL" |
| PISO - ANTECAMARA | Name contains "PISO - ANTECAMARA" |
| PISO - SACADA | Name contains "PISO - SACADA" |
| PISO - PISADA ESCADA - ESCADA PRESSURIZADA | Name contains "PISADA ESCADA" |
| PISO - ESCADA | Name contains "PISO - ESCADA" |
| FORRO - ESCADA - ESCADA PRESSURIZADA | Name contains "FORRO - ESCADA" (Slab) |
| REVESTIMENTO FACHADA PISO SOBRE ALVENARIA - COR 01 | Name contains "FACHADA PISO SOBRE ALV" |
| REVESTIMENTO FACHADA PISO SOBRE ESTRUTURA - COR 01 | Name contains "FACHADA PISO SOBRE ESTRUTURA - COR 01" |
| REVESTIMENTO FACHADA PISO SOBRE ESTRUTURA - COR 13 | Name contains "FACHADA PISO SOBRE ESTRUTURA - COR 13" |
| CTN_Soleira:Soleira | Name contains "Soleira" |
| CTN_Peitoril:Peitoril | Name contains "Peitoril" |
| PEITORIL | Name contains "PEITORIL" |

### 2.8 Portas (IfcDoor)

| Tipo no IFC | Dimensão | Filtro Visus |
|---|---|---|
| P01 - PORTA DE ABRIR, 1 FOLHA, MADEIRA | 60 x 210 cm | Name contains "P01" |
| P02 - PORTA DE ABRIR, 1 FOLHA, MADEIRA | 70 x 210 cm | Name contains "P02" |
| P03 - PORTA DE ABRIR, 1 FOLHA, MADEIRA | 80 x 210 cm | Name contains "P03" |
| P07 - PORTA DE ABRIR, 1 FOLHA, MADEIRA | 90 x 210 cm | Name contains "P07" |
| P0XX - PORTA DE CORRER, 1 FOLHA, A DEFINIR | 70 x 210 cm | Name contains "P0XX" |
| PV05 - PORTA DE CORRER, 3 FOLHAS, ALUMÍNIO E VIDRO | 175 x 230 cm / 300 x 230 cm | Name contains "PV05" |
| PV07 - PORTA DE CORRER, 4 FOLHAS, ALUMÍNIO E VIDRO | 320 x 210 cm | Name contains "PV07" |
| PCF03 - PORTA DE ABRIR, 1 FOLHA, AÇO GALVANIZADO | 100 x 210 cm | Name contains "PCF03" |
| PE - ELEVADOR | — | Name contains "PE - ELEVADOR" |

### 2.9 Janelas (IfcWindow)

| Tipo no IFC | Dimensão | Filtro Visus |
|---|---|---|
| J01 - JANELA MAXIM-AR, 1 FOLHA, ALUMÍNIO E VIDRO | 55 x 75 cm | Name contains "J01" |
| J02 - JANELA CORRER, 1+1 FOLHAS, ALUMÍNIO E VIDRO | 70 x 124 cm | Name contains "J02" |
| J06 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 115 x 110 cm | Name contains "J06" |
| J07 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 115 x 120 cm | Name contains "J07" |
| J08 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 115 x 209 cm | Name contains "J08" |
| J09 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 125 x 209 cm | Name contains "J09" |
| J11 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 135 x 209 cm | Name contains "J11" |
| J14 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 165 x 110 cm | Name contains "J14" |
| J18 - JANELA CORRER, 2 FOLHAS, ALUMÍNIO E VIDRO | 85 x 110 cm | Name contains "J18" |
| GR01 - JANELA FIXA, 1 FOLHA, TELA AÇO GALVANIZADO | 46 x 43 cm | Name contains "GR01" |
| GR02 - JANELA FIXA, 1 FOLHA, TELA AÇO GALVANIZADO | 162 x 200 cm | Name contains "GR02" |
| GR04 - JANELA FIXA, 1 FOLHA, TELA AÇO GALVANIZADO | 110 x 76 cm | Name contains "GR04" |

### 2.10 Forros (IfcCovering)

| Tipo no IFC | Filtro Visus |
|---|---|
| FORRO - LIVING - TIPO | Name contains "FORRO - LIVING" |
| FORRO - SUITE | Name contains "FORRO - SUITE" |
| FORRO - BWC - TIPO | Name contains "FORRO - BWC" |
| FORRO - COZINHA - TIPO | Name contains "FORRO - COZINHA" |
| FORRO - AREA SERVICO - TIPO | Name contains "FORRO - AREA SERVICO" |
| FORRO - LAVABO - TIPO | Name contains "FORRO - LAVABO" |
| FORRO - CIRC. - TIPO | Name contains "FORRO - CIRC." |
| FORRO - CIRC E ROUPARIA | Name contains "FORRO - CIRC E ROUP" |
| FORRO - HALL DO PAVIMENTO - TIPO | Name contains "FORRO - HALL" |
| FORRO - ANTECAMARA | Name contains "FORRO - ANTECAMARA" |
| FORRO - SACADA | Name contains "FORRO - SACADA" |
| FORRO - ESCADA | Name contains "FORRO - ESCADA" |

### 2.11 Elementos Genéricos (IfcBuildingElementProxy)

| Tipo no IFC | Uso | Filtro Visus |
|---|---|---|
| CTN_Verga Portas:Padrão | Verga de porta | Name contains "Verga Portas" |
| CTN_Verga Janelas:Padrão | Verga de janela | Name contains "Verga Janelas" |
| CTN_Contraverga Janelas:Padrão | Contraverga de janela | Name contains "Contraverga" |
| CTN_Texto_Modelo | Anotação (ignorar) | Name contains "Texto_Modelo" |

---

## 3. Regras de Extração por Serviço (Visus Cost)

### REGRA 01 — Alvenaria de Vedação

**Objetivo:** Quantificar m² de alvenaria por espessura

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "ALV" AND NOT contains "REVESTIMENTO" AND NOT contains "RODAPÉ" AND NOT contains "FACHADA" AND NOT contains "REFRATARIO" AND NOT contains "PELE" AND NOT contains "ACF" |
| Agrupamento | Por TypeName (cada espessura vira uma linha) |
| Quantidade | NetSideArea (m²) |
| Alternativa | Length × Height (IfcQuantityLength) |

**Sub-regras por espessura:**
- `ALV 05` → Alvenaria 5 cm
- `ALV 09` → Alvenaria 9 cm
- `ALV 11,5` → Alvenaria 11,5 cm
- `ALV 14` → Alvenaria 14 cm
- `ALV 19` → Alvenaria 19 cm
- `ALV CONC 05` → Alvenaria de concreto 5 cm

---

### REGRA 02 — Divisórias em Aço/Drywall (ACF)

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "ACF" |
| Agrupamento | Por TypeName |
| Quantidade | NetSideArea (m²) |

---

### REGRA 03 — Revestimento Interno de Parede

**Objetivo:** m² de revestimento por ambiente

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "101_REVESTIMENTO PAREDE" |
| Agrupamento | Por ambiente (extrair texto após "PAREDE - ") |
| Quantidade | NetSideArea (m²) |

---

### REGRA 04 — Revestimento Interno de Estrutura

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "102_REVESTIMENTO ESTRUTURA" |
| Agrupamento | Por ambiente |
| Quantidade | NetSideArea (m²) |

---

### REGRA 05 — Revestimento de Fachada

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase + IfcWall |
| Filtro | TypeName contains "REVESTIMENTO FACHADA" |
| Agrupamento | Por cor/tipo (COR 01, COR 02, COR 06, COR 13) + substrato (PAREDE vs ESTRUTURA) |
| Quantidade | NetSideArea (m²) |

---

### REGRA 06 — Rodapés

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "RODAPÉ" |
| Agrupamento | Por ambiente |
| Quantidade | Length (ml) — usar IfcQuantityLength "Length" |

---

### REGRA 07 — Pisos por Ambiente

| Campo | Configuração |
|---|---|
| Classe IFC | IfcSlab |
| Filtro | TypeName contains "PISO -" |
| Agrupamento | Por ambiente |
| Quantidade | GrossArea ou NetArea (m²) |

---

### REGRA 08 — Pisos de Fachada (Pingadeiras/Revestimento)

| Campo | Configuração |
|---|---|
| Classe IFC | IfcSlab |
| Filtro | TypeName contains "REVESTIMENTO FACHADA PISO" |
| Agrupamento | Por substrato (ALVENARIA vs ESTRUTURA) e cor |
| Quantidade | GrossArea (m²) |

---

### REGRA 09 — Soleiras e Peitoris

| Campo | Configuração |
|---|---|
| Classe IFC | IfcSlab |
| Filtro | TypeName contains "Soleira" OR "Peitoril" OR "PEITORIL" |
| Agrupamento | Por tipo |
| Quantidade | Soleira → Length (ml) / Peitoril → Length (ml) |

---

### REGRA 10 — Forros

| Campo | Configuração |
|---|---|
| Classe IFC | IfcCovering |
| Filtro | TypeName contains "FORRO" |
| Agrupamento | Por ambiente |
| Quantidade | GrossArea ou GrossCeilingArea (m²) |

---

### REGRA 11 — Portas

| Campo | Configuração |
|---|---|
| Classe IFC | IfcDoor |
| Filtro | TypeName NOT contains "ELEVADOR" |
| Agrupamento | Por código (P01, P02, P03, P07, PV05, PV07, PCF03, P0XX) |
| Quantidade | Count (un) + Width × Height pra conferência |

---

### REGRA 12 — Janelas

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWindow |
| Filtro | TypeName NOT contains "GR" (separar grades) |
| Agrupamento | Por código (J01, J02, J06, J07, J08, J09, J11, J14, J18) |
| Quantidade | Count (un) + Width × Height |

---

### REGRA 13 — Grades/Telas

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWindow |
| Filtro | TypeName contains "GR" |
| Agrupamento | Por código (GR01, GR02, GR04) |
| Quantidade | Count (un) + Width × Height (m²) |

---

### REGRA 14 — Vergas e Contravergas

| Campo | Configuração |
|---|---|
| Classe IFC | IfcBuildingElementProxy |
| Filtro | TypeName contains "Verga" OR "Contraverga" |
| Agrupamento | Verga Portas / Verga Janelas / Contraverga Janelas |
| Quantidade | Count (un) + Length (ml) |

---

### REGRA 15 — Refratário

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "REFRATARIO" |
| Quantidade | NetSideArea (m²) |

---

### REGRA 16 — Pele de Vidro

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "PELE DE VIDRO" |
| Quantidade | NetSideArea (m²) |

---

### REGRA 17 — Espelho de Escada

| Campo | Configuração |
|---|---|
| Classe IFC | IfcWallStandardCase |
| Filtro | TypeName contains "ESPELHO ESCADA" |
| Quantidade | NetSideArea (m²) |

---

## 4. Passo a Passo — Configuração no Visus Cost

### Passo 1: Importar o IFC
1. Abrir o Visus Cost
2. `File > Import > IFC` → selecionar o arquivo `ifc-teste`
3. Aguardar o parsing completo (~373k linhas)
4. Verificar na árvore que o pavimento "08_1° PAVTO TIPO" apareceu

### Passo 2: Verificar as Propriedades Disponíveis
1. Selecionar qualquer parede na árvore
2. Ir em `Properties` → verificar que existem:
   - *TypeName* (nome do tipo — é o campo principal de filtro)
   - *BaseQuantities* (Length, Height, Width, Area, Volume)
   - *Pset_WallCommon*, *Pset_DoorCommon*, etc.
3. Se `TypeName` não aparecer, usar `Name` (contém a mesma info neste IFC)

### Passo 3: Criar os Grupos de Custo (Cost Groups)
1. Criar estrutura hierárquica:
   - *01 - ALVENARIA*
     - 01.01 - ALV 05 cm
     - 01.02 - ALV 09 cm
     - 01.03 - ALV 11,5 cm
     - 01.04 - ALV 14 cm
     - 01.05 - ALV 19 cm
     - 01.06 - ALV CONC 05 cm
   - *02 - DIVISÓRIAS (ACF)*
     - 02.01 - ACF 12,5 cm
     - 02.02 - ACF 15 cm
   - *03 - REVESTIMENTO INTERNO PAREDE*
     - (um item por ambiente)
   - *04 - REVESTIMENTO INTERNO ESTRUTURA*
   - *05 - REVESTIMENTO FACHADA*
   - *06 - RODAPÉS*
   - *07 - PISOS*
   - *08 - PISOS FACHADA*
   - *09 - SOLEIRAS E PEITORIS*
   - *10 - FORROS*
   - *11 - PORTAS*
   - *12 - JANELAS*
   - *13 - GRADES/TELAS*
   - *14 - VERGAS E CONTRAVERGAS*
   - *15 - ELEMENTOS ESPECIAIS*

### Passo 4: Criar as Regras de Associação
Para cada grupo de custo:

1. Clicar com botão direito no grupo → `Add Rule` (ou `Assign Elements`)
2. Configurar o filtro:
   - *Property:* TypeName (ou Name)
   - *Condition:* Contains
   - *Value:* conforme a coluna "Filtro Visus" das tabelas acima
3. Definir a quantidade:
   - Selecionar a BaseQuantity adequada (ex: NetSideArea para paredes)
4. Testar: verificar que os elementos corretos foram capturados

### Passo 5: Validação Cruzada
1. Para cada regra, verificar:
   - Quantidade de elementos capturados ≈ esperado
   - Nenhum elemento ficou "órfão" (sem regra)
   - Nenhum elemento foi capturado por 2 regras
2. Usar o filtro "Unassigned Elements" pra identificar o que sobrou
3. Elementos `CTN_Texto_Modelo` (anotação) podem ser ignorados

### Passo 6: Excluir Elementos que Não São Quantificáveis
- *CTN_Texto_Modelo* → anotação de projeto, não é elemento construtivo
- *PE - ELEVADOR* → abertura do elevador, não é porta propriamente

### Passo 7: Exportar/Revisar
1. Revisar os quantitativos gerados
2. Exportar para Excel se necessário
3. Comparar com memorial descritivo/quantitativo de referência

---

## 5. Dicas e Observações

- *Atenção:* Os revestimentos (101_ e 102_) estão modelados como `IfcWallStandardCase`, não como `IfcCovering`. Os filtros por TypeName são essenciais
- *Rodapés* também são `IfcWallStandardCase` — a quantidade principal é comprimento (ml), não área
- *Caracteres especiais:* No IFC, caracteres acentuados aparecem codificados (ex: `\X2\00E1\X0\` = á, `\X2\00C9\X0\` = É). O Visus Cost normalmente decodifica automaticamente
- *Fachada:* Os nomes genéricos "COR 01 - NOME DA COR" indicam que a especificação da cor real ainda precisa ser definida pelo projeto
- *Pisos sobre Slab vs IfcCovering:* Neste modelo os pisos são `IfcSlab` (não Covering). Já os forros são `IfcCovering`
- *1 pavimento tipo:* Este IFC contém apenas 1 pavimento tipo. Para o edifício completo, multiplicar pela quantidade de pavimentos tipo

---

*Documento gerado a partir da análise do arquivo `orcamentos/ifcs/duo-cln/ifc-teste`*
*Data: 23/03/2026*
