# Briefing: INSTALAÇÕES TELEFÔNICAS/LÓGICAS — THOZEN ELECTRA — R00

## Metadados
- **Projeto:** Thozen Electra
- **Cliente:** [a confirmar]
- **Disciplina:** Instalações Telefônicas e Lógica (Cabeamento Estruturado)
- **Revisão:** R00
- **Data:** 2026-03-20
- **Fonte dos dados:** 
  - 9 arquivos IFC (rev.01, outubro/2024)
  - 18 arquivos DWG (rev.01, [24])
- **Projetista responsável:** R. Rubens Alves
- **Área total construída:** [a confirmar com Memorial/Arquitetura]
- **Pavimentos:** 
  - Térreo (1º)
  - G1 a G5 (2º ao 6º pavimento - garagens)
  - Lazer (7º)
  - Tipo (8º ao 31º - 24 pavimentos tipo)
  - Casa de Máquinas (cobertura)

---

## 1. Especificações Gerais

### Sistema de Cabeamento Estruturado

**Normas de referência:**
- NBR 14565 - Cabeamento estruturado para edifícios comerciais e data centers
- ANSI/TIA-568 - Commercial Building Telecommunications Cabling Standard
- [a confirmar normas específicas adotadas no projeto]

**Arquitetura do Sistema:**
- Distribuição horizontal: pontos de telecomunicações por pavimento
- Distribuição vertical: prumadas em eletrodutos e calhas
- Categoria de cabo: [a confirmar se CAT6, CAT6A ou misto - não identificado nos IFCs]
- Material de infraestrutura: PVC (eletrodutos), aço galvanizado (calhas)

**Tipos de Pontos:**
- **Pontos de dados (RJ45):** 46 pontos (concentrados no Térreo)
- **Pontos de voz (RJ11):** 44 pontos (Térreo + Tipo)
- **Pontos modulares:** 102 módulos diversos (cabo coaxial, cegos)

**Observações importantes:**
- A maioria dos pontos lógicos está concentrada no **Térreo** (áreas comuns, portaria, administração)
- **Pavimentos Tipo (8º~31º)** têm apenas 8 pontos de voz (provavelmente interfones internos)
- **Garagens (G1~G5)** NÃO possuem pontos de dados/voz mapeados nos IFCs (apenas infraestrutura passiva)
- **Lazer (7º)** possui infraestrutura mas não tem pontos de telecomunicações identificados
- Há presença significativa de módulos para cabo coaxial (51 un) — possível infraestrutura para CFTV

---

## 2. Quantitativos Extraídos

### 2.1 Pontos de Telecomunicações

| # | Item | Especificação | UN | QTD | Pavimentos | Observação |
|---|------|--------------|-----|-----|-----------|------------|
| 1 | Ponto de dados | Módulo RJ45 PVC | ponto | 38 | Térreo | Áreas técnicas/administrativas |
| 2 | Ponto de dados | Módulo RJ45 Inox | ponto | 8 | Térreo | Áreas molhadas/externas |
| 3 | Ponto de voz | Módulo RJ11 PVC | ponto | 36 | Térreo | Portaria/Administração |
| 4 | Ponto de voz | Módulo RJ11 PVC | ponto | 8 | Tipo (24x) | Interfones internos |
| 5 | Módulo cabo coaxial | PVC | módulo | 51 | Térreo + Lazer + Tipo | Infraestrutura CFTV/TV |
| 6 | Módulo cego | PVC | módulo | 51 | Térreo + Lazer + Tipo | Reserva técnica |

**Subtotal de pontos ativos:** 90 pontos (46 dados + 44 voz)  
**Subtotal de infraestrutura:** 102 módulos

**⚠️ IMPORTANTE:** Os IFCs modelam apenas as famílias de tomadas/conectores. **Não foi possível extrair** quantitativos de:
- Cabos UTP (metragem por categoria)
- Patch panels
- Racks de telecomunicações
- DG (Distribuidor Geral)
- Switches/ativos de rede

Esses elementos devem estar em:
- Memoriais descritivos em PDF
- Plantas de cabeamento (DWGs) - não processados nesta extração
- Quantitativos do próprio projetista

---

### 2.2 Infraestrutura Passiva — Caixas e Acessórios

| # | Item | Especificação | UN | QTD | Distribuição Principal | Observação |
|---|------|--------------|-----|-----|----------------------|------------|
| 1 | Caixa de passagem | 4x2 PVC | un | 289 | Todos os pavimentos | Pontos terminais |
| 2 | Suporte para caixa | 4x2 | un | 281 | Todos os pavimentos | Fixação |
| 3 | Placa cega | 4x2 PVC | un | 271 | Todos os pavimentos | Fechamento |
| 4 | Placa para tomada | 4x2 - 1 módulo PVC | un | 10 | Térreo + Tipo | |
| 5 | Placa para tomada | 4x2 - 1 módulo Inox | un | 8 | Térreo | Áreas molhadas |
| 6 | Caixa de passagem | 4x4 | un | 87 | Térreo + Lazer + Tipo | Pontos duplos |
| 7 | Suporte para caixa | 4x4 | un | 87 | Térreo + Lazer + Tipo | Fixação |
| 8 | Placa para tomada | 4x4 - 2 módulos PVC | un | 87 | Térreo + Lazer + Tipo | |
| 9 | Caixa octogonal | 4x4 | un | 61 | Todos os pavimentos | Derivações |
| 10 | Placa octogonal | 4x4 | un | 61 | Todos os pavimentos | Fechamento |
| 11 | Placa de madeira OSB | -- | un | 10 | G1 | Fixação de equipamentos em shaft |

**Subtotal caixas e acessórios:** 1.252 unidades

**Distribuição por pavimento:**
- **Térreo:** 193 caixas 4x2 + 129 caixas 4x4/octogonais (maior concentração - áreas técnicas)
- **Lazer (7º):** 198 caixas 4x2 + 68 caixas 4x4/octogonais (áreas de convivência)
- **Tipo (8º~31º):** 156 caixas 4x2 + 103 caixas 4x4/octogonais **(multiplicar por 24 pavimentos)**
- **Garagens (G1~G5):** 60~63 caixas 4x2 + 3~5 octogonais por pavimento (circulações)
- **Casa de Máquinas:** 9 caixas 4x2 (mínimo - áreas técnicas)

---

### 2.3 Infraestrutura Passiva — Eletrodutos

| # | Item | Especificação | UN | QTD | Distribuição Principal | Observação |
|---|------|--------------|-----|-----|----------------------|------------|
| 1 | Eletroduto flexível | PVC corrugado | m | 5.456 | Todos os pavimentos | Embutido em paredes/lajes |
| 2 | Eletroduto rígido | PVC NBR 15465 roscável | m | 298 | Todos os pavimentos | Aparente/técnico |
| 3 | Eletroduto flexível | PVC espiralado | m | 58 | G1 | Áreas técnicas |
| 4 | Luva para eletroduto | PVC roscável | un | 12 | Lazer | Emendas |
| 5 | Curva para eletroduto | PVC roscável com luva | un | 6 | Lazer | Mudanças de direção |

**Subtotal eletrodutos:** 5.830 unidades (maioria em metros lineares)

**⚠️ IMPORTANTE:** Os IFCs **NÃO especificam diâmetros** dos eletrodutos. Assumir:
- Eletrodutos para pontos de telecomunicações: 3/4" (20mm) ou 1" (25mm)
- Eletrodutos em prumadas: 1 1/4" (32mm) ou maior
- **Confirmar com memoriais ou plantas detalhadas**

**Distribuição por pavimento:**
- **Térreo:** 1.683 m (maior concentração)
- **Tipo (8º~31º):** 1.201 m **(multiplicar por 24)**
- **Lazer (7º):** 1.407 m (áreas de convivência)
- **G1:** 520 m (incluindo shafts verticais)
- **G2~G6:** 186~242 m por pavimento
- **Casa de Máquinas:** 139 m

**Total aproximado de eletrodutos:** ~5.800 m (sem multiplicar pavimento Tipo)  
**Total real (com Tipo x24):** ~5.800 + (1.201 × 23) = **~33.400 m**

---

### 2.4 Infraestrutura Passiva — Calhas e Acessórios

| # | Item | Especificação | UN | QTD | Pavimentos | Observação |
|---|------|--------------|-----|-----|-----------|------------|
| 1 | Eletrocalha perfurada | Pré-zincada [dimensões a confirmar] | m | 33 | G1 | Bandeja de cabos |
| 2 | Emenda interna | Para eletrocalha pré-zincada | un | 50 | G1 | Conexões lineares |
| 3 | Curva horizontal | Para eletrocalha perfurada pré-zincada | un | 10 | G1 | Mudanças de direção |
| 4 | Curva vertical externa | Para eletrocalha perfurada pré-zincada | un | 4 | G1 | Subidas/descidas |
| 5 | Curva vertical interna | Para eletrocalha perfurada pré-zincada | un | 4 | G1 | Subidas/descidas |
| 6 | Tê horizontal | Para eletrocalha perfurada pré-zincada | un | 4 | G1 | Derivações |
| 7 | Redução | Para eletrocalha perfurada pré-zincada | un | 1 | G1 | Mudança de seção |

**Subtotal calhas:** 106 unidades (33 m lineares + 73 acessórios)

**⚠️ IMPORTANTE:** 
- Calhas aparecem **SOMENTE no pavimento G1** — provavelmente shaft técnico vertical
- **Dimensões das calhas NÃO especificadas** nos IFCs — confirmar em plantas (provável 100x50mm ou 150x50mm)
- A baixa quantidade sugere uso apenas em prumadas principais, não em distribuição horizontal

---

### 2.5 Acessórios de Fixação e Acabamento

| # | Item | Especificação | UN | QTD | Observação |
|---|------|--------------|-----|-----|------------|
| 1 | Bucha terminal simples | Alumínio padrão | un | 860 | Fixação de eletrodutos |
| 2 | Conector box e arruela | Alumínio padrão | un | 860 | Fixação de eletrodutos |
| 3 | Arruela lisa | 1/4" | un | 658 | Fixação de calhas (G1) |
| 4 | Porca simples | 1/4" | un | 658 | Fixação de calhas (G1) |
| 5 | Parafuso cabeça lentilha | 1/4" | un | 658 | Fixação de calhas (G1) |

**Subtotal acessórios:** 3.694 unidades

**Observação:** 
- Os 1.974 itens de parafusos/porcas/arruelas estão todos no **G1** — fixação das calhas no shaft
- Buchas e conectores distribuídos conforme densidade de eletrodutos

---

## 3. Resumo de Quantitativos Principais

### Consolidado Geral

| Categoria | Total | Unidade | Observação |
|-----------|-------|---------|------------|
| **Pontos de dados (RJ45)** | 46 | pontos | Térreo |
| **Pontos de voz (RJ11)** | 44 | pontos | Térreo + Tipo |
| **Caixas de passagem** | 648 | unidades | 4x2 + 4x4 + octogonais |
| **Eletrodutos** | ~33.400 | metros | Inclui Tipo x24 |
| **Eletrocalhas** | 33 | metros | G1 apenas |
| **Acessórios de fixação** | 3.694 | unidades | Buchas, conectores, parafusos |

### Quantitativos por Pavimento (sem multiplicadores)

| Pavimento | Pontos Dados | Pontos Voz | Caixas Total | Eletrodutos (m) | Calhas (m) |
|-----------|--------------|------------|--------------|-----------------|------------|
| Térreo | 46 | 36 | 322 | 1.683 | — |
| G1 (2º) | — | — | 65 | 520 | 33 |
| G2 (3º) | — | — | 68 | 242 | — |
| G3 (4º) | — | — | 68 | 242 | — |
| G4 (5º) | — | — | 64 | 210 | — |
| G5 (6º) | — | — | 60 | 186 | — |
| Lazer (7º) | — | — | 266 | 1.407 | — |
| Tipo (8º~31º) | — | 8 | 259 | 1.201 | — |
| Casa Máquinas | — | — | 9 | 139 | — |

**⚠️ Multiplicadores:**
- **Tipo (8º~31º):** 24 pavimentos → multiplicar quantidades acima por 24
- **Exemplo:** Pontos de voz no Tipo = 8 × 24 = **192 pontos**

---

## 4. Premissas Adotadas

| # | Premissa | Justificativa |
|---|---------|---------------|
| 1 | Diâmetros de eletrodutos não especificados | IFCs contêm apenas geometria, sem atributos de diâmetro. Adotar 3/4" para ramais terminais e 1" ou maior para prumadas (confirmar em plantas). |
| 2 | Dimensões de calhas não especificadas | IFCs não contêm dimensões. Provavelmente 100x50mm ou 150x50mm para prumadas (confirmar memorial). |
| 3 | Categoria de cabos UTP não identificada | IFCs modelam apenas conectores. Assumir **CAT6** ou **CAT6A** conforme memorial do projetista. |
| 4 | Metragens de cabos não extraídas | Cabos não estão modelados nos IFCs. Calcular com base em: (distância ponto → quadro) + 20% de folga. |
| 5 | Racks e patch panels não quantificados | Elementos não modelados nos IFCs. Buscar em memoriais descritivos ou plantas de layout de salas técnicas. |
| 6 | DG (Distribuidor Geral) não identificado | Não há referência explícita nos IFCs. Confirmar localização (provável: subsolo ou térreo, próximo a entrada de concessionária). |
| 7 | Pavimentos Garagem (G1~G5) sem pontos ativos | IFCs mostram apenas infraestrutura passiva (caixas, eletrodutos). Pontos de interfone/CFTV devem estar em outro projeto (segurança/automação). |
| 8 | Multiplicador de pavimento Tipo | Projeto indica "08°~31° PAVTO. TIPO (24x)" — **24 pavimentos tipo repetidos**. |

---

## 5. Precificação

| # | Tipo de Insumo/Serviço | Fonte do Preço | Data-base | Observação |
|---|----------------------|---------------|-----------|------------|
| 1 | Módulo conector RJ45 CAT6 | SINAPI | mar/2026 | Verificar se projeto usa CAT6 ou CAT6A |
| 2 | Módulo conector RJ11 | SINAPI | mar/2026 | Pontos de voz |
| 3 | Caixa de passagem 4x2 e 4x4 | SINAPI | mar/2026 | PVC e Inox |
| 4 | Eletroduto flexível PVC corrugado | SINAPI | mar/2026 | Diversos diâmetros (confirmar) |
| 5 | Eletroduto rígido PVC roscável | SINAPI | mar/2026 | Diversos diâmetros (confirmar) |
| 6 | Eletrocalha perfurada galvanizada | SINAPI | mar/2026 | Confirmar dimensões |
| 7 | Cabo UTP CAT6/CAT6A | Cotação | mar/2026 | Metragem a calcular |
| 8 | Patch panel 24/48 portas | Cotação | mar/2026 | Quantidade a definir |
| 9 | Rack 19" (altura a definir) | Cotação | mar/2026 | Quantidade a definir |
| 10 | Mão de obra — lançamento e certificação | Base interna Cartesian | mar/2026 | Incluir teste e certificação |

---

## 6. Pendências / Dúvidas

### Dados Faltantes (CRÍTICO)

- [ ] **Cabeamento:** Categoria (CAT6 / CAT6A), metragem total, cores
- [ ] **Racks:** Quantidade, localização, altura (RUs)
- [ ] **Patch Panels:** Quantidade, tipo (24p / 48p), categoria
- [ ] **DG (Distribuidor Geral):** Localização, especificação
- [ ] **Quadros de telecomunicações:** Quantidade por pavimento, especificação
- [ ] **Switches/Ativos de rede:** Fora de escopo de instalações? Confirmar responsável
- [ ] **Diâmetros de eletrodutos:** Confirmar com plantas detalhadas ou memorial
- [ ] **Dimensões de calhas:** Confirmar 100x50mm ou 150x50mm
- [ ] **Topologia de rede:** Estrela? Anel? Cascateamento?

### Esclarecimentos com Projetista

- [ ] **Pontos lógicos nas garagens (G1~G5):** Há pontos de interfone? CFTV? Controle de acesso? Ou está em projeto separado?
- [ ] **Lazer (7º pavimento):** 266 caixas mas 0 pontos de telecomunicações identificados — há pontos de dados/voz previstos?
- [ ] **Casa de Máquinas:** Há sala técnica/rack neste pavimento?
- [ ] **Placa de madeira OSB no G1:** Para que finalidade? Fixação de equipamentos em shaft?
- [ ] **Prumadas verticais:** Qual a rota? Shafts dedicados ou compartilhados com elétrica?

### Integração com Outros Projetos

- [ ] **CFTV:** Há projeto separado? Os 51 módulos de cabo coaxial são para CFTV ou TV a cabo?
- [ ] **Automação:** Há projeto de automação predial? Rede separada?
- [ ] **Interfonia:** Sistema digital? Analógico? Integrado com controle de acesso?

---

## 7. Mapeamento para Memorial Cartesiano

| Subsistema do Briefing | Código Memorial (N2/N3) | Observação |
|----------------------|------------------------|------------|
| Pontos de Telecomunicações | 07.005 | Instalações Telefônicas |
| Cabeamento Estruturado | 14.007 | Instalações Especiais - Cabeamento Estruturado |
| Eletrodutos (infraestrutura) | 07.001 | Infraestrutura de Eletrodutos |
| Calhas (infraestrutura) | 07.001 | Infraestrutura de Eletrodutos e Calhas |
| Caixas e acessórios | 07.001 | Infraestrutura Elétrica/Telefônica |
| Racks e Patch Panels | 14.007 | Equipamentos de Rede |
| DG (Distribuidor Geral) | 14.007 | Equipamento Principal |

**Observação:** Instalações telefônicas podem ser alocadas em **N1 07 (Instalações Elétricas)** ou **N1 14 (Instalações Especiais)** conforme critério da Cartesian. Cabeamento estruturado moderno geralmente vai em **14 - Instalações Especiais**.

---

## 8. Arquivos de Origem

### Arquivos IFC Processados

1. `348 - T01 [09] - rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO.ifc` (17 MB)
2. `348 - T02 [09] - rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1.ifc` (7.8 MB)
3. `348 - T03 [09] - rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2.ifc` (2.9 MB)
4. `348 - T04 [09] - rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3.ifc` (2.9 MB)
5. `348 - T05 [09] - rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4.ifc` (2.7 MB)
6. `348 - T06 [09] - rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5.ifc` (2.6 MB)
7. `348 - T07 [09] - rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER.ifc` (13 MB)
8. `348 - T08 [09] - rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO (24x).ifc` (12 MB)
9. `348 - T09 [09] - rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS.ifc` (1.5 MB)

### Arquivos DWG Disponíveis (Não Processados)

18 arquivos DWG (2 por pavimento: Torre A e Torre B) — rev.01 — disponíveis em:  
`projetos/thozen-electra/projetos/10 TELEFONICO/DWG/`

**Sugestão:** Processar DWGs para complementar dados faltantes (diâmetros, metragens de cabos, layouts de racks).

---

## 9. Histórico de Revisões

| Revisão | Data | Arquivos Recebidos | Mudanças |
|---------|------|--------------------|----------|
| R00 | 2026-03-20 | 9 IFCs + 18 DWGs (rev.01) | **Versão inicial** — Extração automática via IFC. Dados incompletos: faltam cabos, racks, patch panels, DG. Necessário complementar com memoriais e plantas detalhadas. |

---

## 10. Observações Finais

### Limitações da Extração IFC

Esta extração foi realizada com base nos **modelos IFC fornecidos**, que contêm principalmente:
- Geometria de famílias do Revit (caixas, eletrodutos, calhas, conectores)
- Quantidades de elementos modelados

**NÃO foram extraídos** (porque não estão modelados nos IFCs ou não têm atributos suficientes):
- Metragens de cabos UTP
- Especificações técnicas de racks, patch panels, DG
- Diâmetros precisos de eletrodutos
- Dimensões de calhas
- Topologia de rede
- Endereçamento lógico

### Próximos Passos

1. ✅ **Extração IFC concluída** — quantitativos de infraestrutura passiva (caixas, eletrodutos, calhas, conectores)
2. ⏳ **Processar DWGs** — obter plantas com cotas, diâmetros, metragens de cabos
3. ⏳ **Analisar memoriais descritivos** — especificações técnicas, topologia de rede, equipamentos
4. ⏳ **Calcular metragens de cabos** — com base em distâncias ponto-quadro + folgas
5. ⏳ **Consolidar em planilha executiva** — compatível com Memorial Cartesiano (N1 07 ou N1 14)

### Recomendações

- **Validar multiplicador de pavimento Tipo:** Confirmar se são realmente 24 pavimentos idênticos ou se há variações
- **Confirmar integração com CFTV:** Os módulos de cabo coaxial sugerem infraestrutura para CFTV — verificar se há projeto separado
- **Revisar pontos em garagens:** É incomum garagens não terem pontos de interfone/controle de acesso — verificar se está em projeto de automação
- **Certificação de rede:** Incluir no orçamento os custos de teste e certificação de cabos (Fluke, etc.)

---

*Briefing gerado por Cartesiano | Data: 2026-03-20 | Fonte: IFCs rev.01 (out/2024)*

**Status:** ⚠️ PARCIAL — Necessário complementar com dados de cabeamento, racks e ativos de rede
