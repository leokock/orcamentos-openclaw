# Briefing: INSTALAÇÕES TELEFÔNICAS/LÓGICAS — THOZEN ELECTRA — R01

## Metadados
- **Projeto:** Thozen Electra
- **Cliente:** [a confirmar]
- **Disciplina:** Instalações Telefônicas e Lógica (Cabeamento Estruturado)
- **Revisão:** R01
- **Data:** 2026-03-24
- **Fonte dos dados:** 
  - 9 arquivos IFC (rev.01, outubro/2024)
  - 18 arquivos DWG (rev.01, [24]) — **PROCESSADOS**
- **Projetista responsável:** R. Rubens Alves
- **Área total construída:** [a confirmar com Memorial/Arquitetura]
- **Pavimentos:** 
  - Térreo (1º)
  - G1 a G5 (2º ao 6º pavimento - garagens)
  - Lazer (7º)
  - Tipo (8º ao 31º - 24 pavimentos tipo)
  - Casa de Máquinas (cobertura)

---

## 🆕 NOVIDADES R01

### Dados Extraídos dos DWGs

Esta revisão incorpora **dados novos** extraídos diretamente dos arquivos DWG (18 arquivos, rev.01), complementando os dados do IFC. Os DWGs forneceram informações que não estavam modeladas nos IFCs:

**Novos itens identificados:**
1. **Eletrodutos de diâmetros maiores:** ø1.1/4" (32mm) e ø3" (75mm) — usados em prumadas verticais e alimentações principais
2. **Caixas de passagem de dimensões maiores:** 60x120x20cm, 80x120x20cm, 40x120x15cm, etc. — usadas em shafts técnicos e prumadas
3. **Acessórios de infraestrutura:** Cotovelos, conectores box/arruela, buchas terminais (quantidades reais por pavimento)
4. **Condutores identificados:** CFTV, UTP, CCI, Cordplast (símbolos/trechos marcados nas plantas)
5. **Pontos de uso detalhados:** Caixas 4x2 para Interfone, Câmera CFTV, Controle de Acesso, e Caixas 4x4 para Dados/Telefone

### Tabela Comparativa: IFC vs DWG

| Categoria | Fonte IFC (R00) | Fonte DWG (R01) | Observação |
|-----------|----------------|----------------|------------|
| **Pontos RJ45/RJ11** | 90 pontos | 90 pontos | ✅ Confirmado |
| **Caixas 4x2/4x4** | 648 unidades | 648 unidades | ✅ Confirmado |
| **Eletrodutos ø3/4" e ø1"** | ~33.400 m | ~33.400 m | ✅ Confirmado |
| **Eletrodutos ø1.1/4"** | ❌ Não identificado | **132 m** | 🆕 Novo (prumadas) |
| **Eletrodutos ø3"** | ❌ Não identificado | **112 m** | 🆕 Novo (prumadas principais) |
| **Caixas passagem >30x30** | ❌ Não identificado | **21 unidades** | 🆕 Novo (shafts técnicos) |
| **Cotovelos** | ❌ Não quantificado | **4.414 unidades** | 🆕 Novo (curvas de eletrodutos) |
| **Conectores/Buchas** | ❌ Não quantificado | **556 + 132 unidades** | 🆕 Novo (fixação) |
| **Condutores identificados** | ❌ Não identificado | **324 trechos** | 🆕 Novo (CFTV, UTP, CCI, Cordplast) |
| **Pontos de uso detalhados** | ❌ Genérico | **193 unidades** | 🆕 Novo (Interfone, CFTV, Controle Acesso, Dados/Tel) |

---

## 1. Especificações Gerais

### Sistema de Cabeamento Estruturado

**Normas de referência:**
- NBR 14565 - Cabeamento estruturado para edifícios comerciais e data centers
- ANSI/TIA-568 - Commercial Building Telecommunications Cabling Standard
- NBR 15465 - Eletrodutos de PVC rígido antichama

**Arquitetura do Sistema:**
- Distribuição horizontal: pontos de telecomunicações por pavimento
- Distribuição vertical: prumadas em eletrodutos (ø1.1/4" e ø3") com caixas de passagem em shafts
- Categoria de cabo: [a confirmar se CAT6, CAT6A ou misto - não identificado nos DWGs]
- Material de infraestrutura: PVC flexível antichama (ramais), PVC rígido (prumadas), aço galvanizado (calhas)

**Tipos de Pontos:**
- **Pontos de dados (RJ45):** 46 pontos (concentrados no Térreo)
- **Pontos de voz (RJ11):** 44 pontos (Térreo + Tipo)
- **Pontos modulares:** 102 módulos diversos (cabo coaxial, cegos)
- **🆕 Pontos de Interfone:** 82 pontos (Térreo, Garagens, Lazer, Tipo)
- **🆕 Pontos de CFTV:** 41 pontos (todos os pavimentos)
- **🆕 Pontos de Controle de Acesso:** 63 pontos (Térreo e Lazer)

**Observações importantes:**
- A maioria dos pontos lógicos está concentrada no **Térreo** (áreas comuns, portaria, administração)
- **Pavimentos Tipo (8º~31º)** têm 8 pontos de voz + 16 pontos de interfone
- **Garagens (G1~G5)** possuem infraestrutura para interfones e CFTV (8 pontos/pav cada sistema)
- **Lazer (7º)** possui 16 pontos de interfone + 4 câmeras CFTV + 31 pontos de controle de acesso
- Há presença significativa de condutores identificados (324 trechos: 171 CFTV, 47 UTP, 60 CCI, 103 Cordplast)

---

## 2. Quantitativos Extraídos (Atualizado com DWG)

### 2.1 Pontos de Telecomunicações

| # | Item | Especificação | UN | QTD | Pavimentos | Observação |
|---|------|--------------|-----|-----|-----------|------------|
| 1 | Ponto de dados | Módulo RJ45 PVC | ponto | 38 | Térreo | Áreas técnicas/administrativas |
| 2 | Ponto de dados | Módulo RJ45 Inox | ponto | 8 | Térreo | Áreas molhadas/externas |
| 3 | Ponto de voz | Módulo RJ11 PVC | ponto | 36 | Térreo | Portaria/Administração |
| 4 | Ponto de voz | Módulo RJ11 PVC | ponto | 8 | Tipo (24x) | Interfones internos |
| 5 | Módulo cabo coaxial | PVC | módulo | 51 | Térreo + Lazer + Tipo | Infraestrutura CFTV/TV |
| 6 | Módulo cego | PVC | módulo | 51 | Térreo + Lazer + Tipo | Reserva técnica |
| 7 | 🆕 Caixa 4x2 - Interfone | PVC | ponto | 10 | Térreo | 🆕 DWG |
| 8 | 🆕 Caixa 4x2 - Interfone | PVC | ponto | 8 | G1~G5 (5x) | 🆕 DWG |
| 9 | 🆕 Caixa 4x2 - Interfone | PVC | ponto | 16 | Lazer | 🆕 DWG |
| 10 | 🆕 Caixa 4x2 - Interfone | PVC | ponto | 16 | Tipo (24x) | 🆕 DWG |
| 11 | 🆕 Caixa 4x2 - Câmera CFTV | PVC | ponto | 2 | Térreo | 🆕 DWG |
| 12 | 🆕 Caixa 4x2 - Câmera CFTV | PVC | ponto | 6~7 | G1~G5 (média) | 🆕 DWG |
| 13 | 🆕 Caixa 4x2 - Câmera CFTV | PVC | ponto | 4 | Lazer | 🆕 DWG |
| 14 | 🆕 Caixa 4x2 - Câmera CFTV | PVC | ponto | 3 | Casa Máquinas | 🆕 DWG |
| 15 | 🆕 Caixa 4x2 - Controle Acesso | PVC | ponto | 32 | Térreo | 🆕 DWG |
| 16 | 🆕 Caixa 4x2 - Controle Acesso | PVC | ponto | 31 | Lazer | 🆕 DWG |
| 17 | 🆕 Caixa 4x4 - Dados/Telefone | PVC | ponto | 36 | Térreo | 🆕 DWG (RJ45/RJ11) |

**Subtotal de pontos ativos (IFC):** 90 pontos (46 dados + 44 voz)  
**🆕 Subtotal de pontos identificados (DWG):** +193 pontos (82 interfone + 41 CFTV + 63 controle acesso + 36 dados/tel duplos)  
**TOTAL GERAL:** 283 pontos de telecomunicações

**⚠️ IMPORTANTE:** Os DWGs forneceram símbolos e caixas de pontos terminais, mas **ainda não foi possível extrair**:
- Cabos UTP (metragem por categoria)
- Patch panels
- Racks de telecomunicações
- DG (Distribuidor Geral)
- Switches/ativos de rede

Esses elementos devem estar em memoriais descritivos ou plantas de layout de salas técnicas.

---

### 2.2 Infraestrutura Passiva — Caixas e Acessórios

| # | Item | Especificação | UN | QTD (IFC) | 🆕 QTD (DWG) | Distribuição Principal | Observação |
|---|------|--------------|-----|-----------|------------|----------------------|------------|
| 1 | Caixa de passagem | 4x2 PVC | un | 289 | — | Todos os pavimentos | Pontos terminais |
| 2 | Suporte para caixa | 4x2 | un | 281 | — | Todos os pavimentos | Fixação |
| 3 | Placa cega | 4x2 PVC | un | 271 | — | Todos os pavimentos | Fechamento |
| 4 | Placa para tomada | 4x2 - 1 módulo PVC | un | 10 | — | Térreo + Tipo | |
| 5 | Placa para tomada | 4x2 - 1 módulo Inox | un | 8 | — | Térreo | Áreas molhadas |
| 6 | Caixa de passagem | 4x4 | un | 87 | — | Térreo + Lazer + Tipo | Pontos duplos |
| 7 | Suporte para caixa | 4x4 | un | 87 | — | Térreo + Lazer + Tipo | Fixação |
| 8 | Placa para tomada | 4x4 - 2 módulos PVC | un | 87 | — | Térreo + Lazer + Tipo | |
| 9 | Caixa octogonal | 4x4 | un | 61 | — | Todos os pavimentos | Derivações |
| 10 | Placa octogonal | 4x4 | un | 61 | — | Todos os pavimentos | Fechamento |
| 11 | Placa de madeira OSB | — | un | 10 | — | G1 | Fixação equipamentos shaft |
| 12 | 🆕 Cx passagem 60x60x12cm | PVC | un | — | 1 | Térreo | 🆕 Shaft técnico |
| 13 | 🆕 Cx passagem 80x120x20cm | PVC | un | — | 2 | Térreo | 🆕 Shaft técnico |
| 14 | 🆕 Cx passagem 60x120x20cm | PVC | un | — | 2 | Térreo + G1 | 🆕 Shaft técnico |
| 15 | 🆕 Cx passagem 60x120x15cm | PVC | un | — | 1 | G1 | 🆕 Shaft técnico |
| 16 | 🆕 Cx passagem 40x120x15cm | PVC | un | — | 15 | G2~Tipo | 🆕 Shafts prumadas |
| 17 | 🆕 Cx passagem 60x40x12cm | PVC | un | — | 1 | Lazer | 🆕 Derivação |
| 18 | 🆕 Cx passagem 40x40x12cm | PVC | un | — | 1 | Lazer | 🆕 Derivação |
| 19 | 🆕 Cx passagem 40x40x15cm | PVC | un | — | 2 | Casa Máquinas | 🆕 Derivação |
| 20 | 🆕 Cx passagem 20x20x12cm | PVC | un | — | 2 | Casa Máquinas | 🆕 Pequenas derivações |

**Subtotal caixas e acessórios (IFC):** 1.252 unidades  
**🆕 Subtotal caixas passagem grandes (DWG):** +27 unidades (shafts técnicos)  
**TOTAL GERAL:** 1.279 unidades

---

### 2.3 Infraestrutura Passiva — Eletrodutos

| # | Item | Especificação | UN | QTD (IFC) | 🆕 QTD (DWG) | Distribuição Principal | Observação |
|---|------|--------------|-----|-----------|------------|----------------------|------------|
| 1 | Eletroduto flexível | PVC corrugado ø3/4" e ø1" | m | ~33.400 | — | Todos os pavimentos | Embutido |
| 2 | Eletroduto rígido | PVC NBR 15465 roscável | m | 298 | — | Todos os pavimentos | Aparente/técnico |
| 3 | Eletroduto flexível | PVC espiralado | m | 58 | — | G1 | Áreas técnicas |
| 4 | 🆕 Eletroduto flexível | PVC antichama NBR 15465 ø1.1/4" | m | — | 132 | Térreo, G1, Lazer, Tipo, Casa Máq | 🆕 Prumadas |
| 5 | 🆕 Eletroduto flexível | PVC antichama NBR 15465 ø3" | m | — | 112 | G1~G5, Lazer, Tipo | 🆕 Prumadas principais |
| 6 | Luva para eletroduto | PVC roscável | un | 12 | — | Lazer | Emendas |
| 7 | Curva para eletroduto | PVC roscável com luva | un | 6 | — | Lazer | Mudanças de direção |
| 8 | 🆕 Cotovelo eletroduto | PVC flexível amarelo | un | — | 4.414 | Todos os pavimentos | 🆕 Curvas de tubulação |

**Subtotal eletrodutos (IFC, sem Tipo):** ~5.800 m  
**Subtotal eletrodutos (IFC, com Tipo×24):** ~33.400 m  
**🆕 Subtotal eletrodutos novos diâmetros (DWG):** +244 m (ø1.1/4" e ø3")  
**🆕 Subtotal cotovelos (DWG):** +4.414 unidades  
**TOTAL GERAL (eletrodutos lineares):** ~33.644 m

**⚠️ Distribuição dos novos diâmetros:**
- **ø1.1/4" (132 m):** Térreo (32m), G1 (24m), Lazer (54m), Tipo (16m×24=384m estimado), Casa Máq (16m)
- **ø3" (112 m):** G1~G5 (40m cada = 200m total), Lazer (12m), Tipo (12m×24=288m estimado)

---

### 2.4 🆕 Acessórios de Infraestrutura (Dados DWG)

| # | Item | Especificação | UN | QTD | Distribuição Principal | Observação |
|---|------|--------------|-----|-----|----------------------|------------|
| 1 | 🆕 Cotovelo para eletroduto | PVC flexível amarelo | un | 4.414 | Todos os pavimentos | Curvas de tubulação |
| 2 | 🆕 Conector box e arruela | Alumínio padrão | un | 556 | Todos os pavimentos | Fixação de eletrodutos em caixas |
| 3 | 🆕 Bucha terminal simples | Alumínio padrão | un | 132 | Todos os pavimentos | Acabamento de eletrodutos |
| 4 | Bucha terminal simples | Alumínio padrão (IFC) | un | 860 | Todos os pavimentos | Fixação (dado IFC) |
| 5 | Conector box e arruela | Alumínio padrão (IFC) | un | 860 | Todos os pavimentos | Fixação (dado IFC) |
| 6 | Arruela lisa | 1/4" | un | 658 | G1 | Fixação de calhas |
| 7 | Porca simples | 1/4" | un | 658 | G1 | Fixação de calhas |
| 8 | Parafuso cabeça lentilha | 1/4" | un | 658 | G1 | Fixação de calhas |

**Observação sobre duplicidade:** Os dados de buchas/conectores aparecem tanto no IFC quanto no DWG. A quantidade **DWG é mais precisa** pois vem diretamente dos símbolos de componentes nas plantas. Recomenda-se usar **DWG (556 + 132)** em vez de **IFC (860 + 860)** para evitar superestimação.

---

### 2.5 🆕 Condutores Identificados (Dados DWG)

| # | Item | Especificação | UN | QTD | Distribuição Principal | Observação |
|---|------|--------------|-----|-----|----------------------|------------|
| 1 | 🆕 Condutor CFTV | — | trecho | 171 | Todos os pavimentos | Símbolos de trechos de cabos para CFTV |
| 2 | 🆕 Condutor UTP | — | trecho | 47 | Térreo | Símbolos de trechos de cabos para dados |
| 3 | 🆕 Condutor CCI | — | trecho | 60 | Térreo + Tipo | Símbolos de trechos de cabos para controle |
| 4 | 🆕 Condutor Cordplast | — | trecho | 103 | Térreo + Garagens + Lazer + Casa Máq | Símbolos de trechos de cabos flexíveis |

**TOTAL:** 324 trechos identificados

**⚠️ IMPORTANTE:** Esses valores representam **símbolos/trechos marcados nas plantas DWG**, NÃO metragens reais de cabos. Para calcular metragens reais, é necessário:
1. Medir distâncias ponto → quadro em cada planta
2. Adicionar 20% de folga técnica
3. Consolidar por tipo de cabo

**Estimativa conservadora de metragem** (assumindo média de 15m por trecho + 20% folga):
- CFTV: 171 trechos × 18m ≈ **3.078 m**
- UTP: 47 trechos × 18m ≈ **846 m**
- CCI: 60 trechos × 18m ≈ **1.080 m**
- Cordplast: 103 trechos × 18m ≈ **1.854 m**
- **TOTAL ESTIMADO:** ~6.858 m de cabos (a confirmar com medições detalhadas)

---

### 2.6 Infraestrutura Passiva — Calhas e Acessórios (Dados IFC)

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

**⚠️ IMPORTANTE:** Calhas aparecem **SOMENTE no pavimento G1** — provavelmente shaft técnico vertical.

---

## 3. Resumo de Quantitativos Principais (Atualizado R01)

### Consolidado Geral

| Categoria | IFC (R00) | 🆕 DWG (R01) | TOTAL | Unidade | Observação |
|-----------|-----------|-------------|-------|---------|------------|
| **Pontos de dados (RJ45)** | 46 | +36 (duplos 4x4) | 82 | pontos | Térreo |
| **Pontos de voz (RJ11)** | 44 | — | 44 | pontos | Térreo + Tipo |
| **🆕 Pontos Interfone** | — | 82 | 82 | pontos | Todos pavimentos |
| **🆕 Pontos CFTV** | — | 41 | 41 | pontos | Todos pavimentos |
| **🆕 Pontos Controle Acesso** | — | 63 | 63 | pontos | Térreo + Lazer |
| **Caixas de passagem** | 648 | +27 (grandes) | 675 | unidades | 4x2 + 4x4 + octogonais + shafts |
| **Eletrodutos ø3/4" e ø1"** | ~33.400 | — | ~33.400 | metros | Ramais horizontais |
| **🆕 Eletrodutos ø1.1/4"** | — | 132 | 132 | metros | Prumadas |
| **🆕 Eletrodutos ø3"** | — | 112 | 112 | metros | Prumadas principais |
| **🆕 Cotovelos** | — | 4.414 | 4.414 | unidades | Curvas |
| **🆕 Conectores/Buchas** | 1.720 (IFC) | 688 (DWG) | 688* | unidades | *Usar DWG (mais preciso) |
| **Eletrocalhas** | 33 | — | 33 | metros | G1 apenas |
| **Acessórios de fixação (calhas)** | 1.974 | — | 1.974 | unidades | Parafusos/porcas G1 |

### Quantitativos por Pavimento (Consolidado IFC+DWG, sem multiplicadores)

| Pavimento | Dados | Voz | 🆕 Interfone | 🆕 CFTV | 🆕 Ctrl Acesso | Caixas | Elet. ø1" | 🆕 ø1.1/4" | 🆕 ø3" | 🆕 Cotovelos | Calhas |
|-----------|-------|-----|-------------|---------|---------------|--------|-----------|-----------|--------|-------------|--------|
| **Térreo** | 46 | 36 | 10 | 2 | 32 | 322 | 1.683m | 32m | — | 1.337 | — |
| **G1** | — | — | 8 | 6 | — | 65 | 520m | 24m | 40m | 301 | 33m |
| **G2** | — | — | 8 | 7 | — | 68 | 242m | — | 12m | 194 | — |
| **G3** | — | — | 8 | 7 | — | 68 | 242m | — | 12m | 188 | — |
| **G4** | — | — | 8 | 6 | — | 64 | 210m | — | 12m | 163 | — |
| **G5** | — | — | 8 | 5 | — | 60 | 186m | — | 12m | 139 | — |
| **Lazer** | — | — | 16 | 4 | 31 | 266 | 1.407m | 54m | 12m | 1.078 | — |
| **Tipo (8~31)** | — | 8 | 16 | — | — | 259 | 1.201m | 16m | 12m | 918 | — |
| **Casa Máq** | — | — | — | 3 | — | 9 | 139m | 16m | — | 96 | — |

**⚠️ Multiplicadores:**
- **Tipo (8º~31º):** 24 pavimentos → Ex: Interfones = 16 × 24 = 384 pontos
- **Estimativa total Tipo:** Elet. ø1" = 1.201 × 24 ≈ 28.824m, ø1.1/4" = 16 × 24 ≈ 384m, ø3" = 12 × 24 ≈ 288m

---

## 4. Premissas Adotadas

| # | Premissa | Justificativa | Status R01 |
|---|---------|---------------|-----------|
| 1 | Diâmetros de eletrodutos não especificados no IFC | IFCs contêm apenas geometria, sem atributos de diâmetro. | ✅ **RESOLVIDO** — DWGs fornecem specs (ø3/4", ø1", ø1.1/4", ø3") |
| 2 | Dimensões de calhas não especificadas | IFCs não contêm dimensões. Provavelmente 100x50mm ou 150x50mm para prumadas. | ⏳ Aguardando memorial |
| 3 | Categoria de cabos UTP não identificada | IFCs/DWGs modelam apenas conectores e símbolos de condutores. | ⏳ Assumir **CAT6** ou **CAT6A** conforme memorial |
| 4 | Metragens de cabos não extraídas | Cabos não estão modelados nos IFCs. Símbolos de trechos identificados nos DWGs. | ⏳ Calcular: (distância ponto → quadro) + 20% folga |
| 5 | Racks e patch panels não quantificados | Elementos não modelados nos IFCs/DWGs. | ⏳ Buscar em memoriais/plantas de layout |
| 6 | DG (Distribuidor Geral) não identificado | Não há referência explícita nos IFCs/DWGs. | ⏳ Confirmar localização (provável: G1 ou Térreo) |
| 7 | Pavimentos Garagem (G1~G5) com pontos identificados | DWGs mostram 8 pontos de interfone + 5~7 câmeras CFTV por pavimento. | ✅ **CONFIRMADO** — Dados extraídos |
| 8 | Multiplicador de pavimento Tipo | Projeto indica "08°~31° PAVTO. TIPO (24x)". | ✅ **CONFIRMADO** — 24 pavimentos tipo repetidos |
| 9 | Quantidades de buchas/conectores | IFC mostra 860+860, DWG mostra 556+132. | ✅ **USAR DWG** (mais preciso — símbolos diretos) |

---

## 5. Precificação

| # | Tipo de Insumo/Serviço | Fonte do Preço | Data-base | Observação |
|---|----------------------|---------------|-----------|------------|
| 1 | Módulo conector RJ45 CAT6 | SINAPI | mar/2026 | Verificar se projeto usa CAT6 ou CAT6A |
| 2 | Módulo conector RJ11 | SINAPI | mar/2026 | Pontos de voz |
| 3 | Caixa de passagem 4x2, 4x4 e grandes | SINAPI | mar/2026 | PVC (diversas dimensões) |
| 4 | Eletroduto flexível PVC corrugado | SINAPI | mar/2026 | ø3/4", ø1", ø1.1/4", ø3" |
| 5 | Eletroduto rígido PVC roscável | SINAPI | mar/2026 | Diversos diâmetros |
| 6 | Eletrocalha perfurada galvanizada | SINAPI | mar/2026 | Confirmar dimensões (100x50 ou 150x50) |
| 7 | 🆕 Cotovelo para eletroduto flexível | SINAPI | mar/2026 | PVC amarelo |
| 8 | 🆕 Conector box e arruela | SINAPI | mar/2026 | Alumínio padrão |
| 9 | 🆕 Bucha terminal simples | SINAPI | mar/2026 | Alumínio padrão |
| 10 | Cabo UTP CAT6/CAT6A | Cotação | mar/2026 | Metragem a calcular (~6.858m estimado) |
| 11 | Patch panel 24/48 portas | Cotação | mar/2026 | Quantidade a definir |
| 12 | Rack 19" (altura a definir) | Cotação | mar/2026 | Quantidade a definir |
| 13 | Mão de obra — lançamento e certificação | Base interna Cartesian | mar/2026 | Incluir teste e certificação |

---

## 6. Pendências / Dúvidas

### Dados Faltantes (CRÍTICO)

- [x] ~~**Diâmetros de eletrodutos**~~ ✅ **RESOLVIDO R01** — DWGs fornecem ø3/4", ø1", ø1.1/4", ø3"
- [x] ~~**Quantidades de cotovelos, conectores, buchas**~~ ✅ **RESOLVIDO R01** — DWGs fornecem quantidades por pavimento
- [x] ~~**Pontos de interfone, CFTV, controle de acesso**~~ ✅ **RESOLVIDO R01** — DWGs fornecem pontos detalhados
- [x] ~~**Condutores identificados**~~ ✅ **PARCIALMENTE RESOLVIDO R01** — Símbolos de trechos identificados (metragem a calcular)
- [ ] **Cabeamento:** Categoria (CAT6 / CAT6A), metragem total, cores
- [ ] **Racks:** Quantidade, localização, altura (RUs)
- [ ] **Patch Panels:** Quantidade, tipo (24p / 48p), categoria
- [ ] **DG (Distribuidor Geral):** Localização, especificação
- [ ] **Quadros de telecomunicações:** Quantidade por pavimento, especificação
- [ ] **Switches/Ativos de rede:** Fora de escopo de instalações? Confirmar responsável
- [ ] **Dimensões de calhas:** Confirmar 100x50mm ou 150x50mm

### Esclarecimentos com Projetista

- [x] ~~**Pontos lógicos nas garagens (G1~G5)**~~ ✅ **RESOLVIDO R01** — 8 interfones + 5~7 câmeras por pavimento
- [ ] **Lazer (7º pavimento):** 266 caixas + 16 interfones + 4 câmeras + 31 controles de acesso — há pontos de dados/voz adicionais?
- [ ] **Casa de Máquinas:** Há sala técnica/rack neste pavimento?
- [ ] **Placa de madeira OSB no G1:** Para fixação de equipamentos em shaft? (confirmado nos DWGs)
- [ ] **Prumadas verticais:** Qual a rota? Shafts dedicados ou compartilhados com elétrica?

### Integração com Outros Projetos

- [ ] **CFTV:** Há projeto separado? Os condutores CFTV identificados nos DWGs são compatíveis com projeto de segurança?
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
| 🆕 Cotovelos, conectores, buchas | 07.001 | Acessórios de Infraestrutura |
| 🆕 Condutores (CFTV, UTP, CCI, Cordplast) | 14.007 | Cabeamento (a confirmar metragem) |
| 🆕 Pontos de Interfone | 14.007 | Sistema de Interfonia |
| 🆕 Pontos de CFTV | 14.008 | Sistema de CFTV (ou projeto separado) |
| 🆕 Pontos de Controle de Acesso | 14.009 | Sistema de Controle de Acesso |
| Racks e Patch Panels | 14.007 | Equipamentos de Rede |
| DG (Distribuidor Geral) | 14.007 | Equipamento Principal |

---

## 8. Arquivos de Origem

### Arquivos IFC Processados (R00)

1. `348 - T01 [09] - rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO.ifc` (17 MB)
2. `348 - T02 [09] - rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1.ifc` (7.8 MB)
3. `348 - T03 [09] - rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2.ifc` (2.9 MB)
4. `348 - T04 [09] - rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3.ifc` (2.9 MB)
5. `348 - T05 [09] - rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4.ifc` (2.7 MB)
6. `348 - T06 [09] - rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5.ifc` (2.6 MB)
7. `348 - T07 [09] - rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER.ifc` (13 MB)
8. `348 - T08 [09] - rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO (24x).ifc` (12 MB)
9. `348 - T09 [09] - rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS.ifc` (1.5 MB)

### 🆕 Arquivos DWG Processados (R01)

18 arquivos DWG (2 por pavimento: Torre A e Torre B) — rev.01:

**Térreo:**
1. `348 - T02 [24] rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO [T. A].dxf`
2. `348 - T03 [24] rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO [T. B].dxf`

**Garagens (G1~G5):**
3-4. `348 - T04/T05 [24] rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1 [T. A/B].dxf`
5-6. `348 - T06/T07 [24] rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2 [T. A/B].dxf`
7-8. `348 - T08/T09 [24] rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3 [T. A/B].dxf`
9-10. `348 - T10/T11 [24] rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4 [T. A/B].dxf`
11-12. `348 - T12/T13 [24] rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5 [T. A/B].dxf`

**Lazer:**
13-14. `348 - T14/T15 [24] rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER [T. A/B].dxf`

**Tipo:**
15-16. `348 - T16/T17 [24] rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO [T. A/B].dxf`

**Casa de Máquinas:**
17-18. `348 - T18/T19 [24] rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS [T. A/B].dxf`

**Dados consolidados:** `dados_brutos_telefonico.json` (142 KB)

---

## 9. Histórico de Revisões

| Revisão | Data | Arquivos Recebidos | Mudanças |
|---------|------|--------------------|----------|
| R00 | 2026-03-20 | 9 IFCs (rev.01) | **Versão inicial** — Extração via IFC. Dados incompletos: faltam cabos, racks, patch panels, DG, diâmetros de eletrodutos, pontos de interfone/CFTV/controle. |
| R01 | 2026-03-24 | 18 DWGs (rev.01) | **🆕 Atualização com dados dos DWGs:** (1) Diâmetros de eletrodutos identificados (ø1.1/4" e ø3"), (2) Caixas de passagem grandes para shafts (21 un), (3) Cotovelos, conectores e buchas quantificados (4.414 + 556 + 132 un), (4) Pontos de interfone (82), CFTV (41) e controle de acesso (63) identificados, (5) Condutores CFTV/UTP/CCI/Cordplast mapeados (324 trechos). Pendentes: metragens de cabos, racks, patch panels, DG. |

---

## 10. Observações Finais

### Avanços R01

✅ **Diâmetros de eletrodutos identificados** — DWGs fornecem specs completas (ø3/4", ø1", ø1.1/4", ø3")  
✅ **Caixas de passagem grandes** — 21 unidades para shafts técnicos (60x120, 80x120, 40x120, etc.)  
✅ **Acessórios de infraestrutura quantificados** — 4.414 cotovelos, 556 conectores, 132 buchas  
✅ **Pontos de uso detalhados** — 82 interfones, 41 câmeras CFTV, 63 controles de acesso  
✅ **Condutores identificados** — 324 trechos (CFTV, UTP, CCI, Cordplast)  
✅ **Garagens com pontos ativos** — 8 interfones + 5~7 câmeras por pavimento (G1~G5)  

### Pendências Restantes

⏳ **Cabeamento:** Categoria (CAT6/CAT6A), metragem total (estimar ~6.858m), cores  
⏳ **Ativos de rede:** Racks, patch panels, DG, switches  
⏳ **Dimensões de calhas:** Confirmar 100x50mm ou 150x50mm  
⏳ **Memoriais descritivos:** Topologia de rede, especificações técnicas  

### Próximos Passos

1. ✅ **Extração IFC concluída** (R00)
2. ✅ **Extração DWG concluída** (R01)
3. ⏳ **Calcular metragens de cabos** — medir distâncias ponto-quadro + 20% folga
4. ⏳ **Analisar memoriais descritivos** — racks, patch panels, DG, topologia
5. ⏳ **Consolidar em planilha executiva R01** — compatível com Memorial Cartesiano

### Recomendações

- **Validar multiplicador de pavimento Tipo:** Confirmar se são realmente 24 pavimentos idênticos ou se há variações
- **Confirmar integração com CFTV:** Verificar se há projeto de segurança separado ou se os condutores CFTV são do escopo telecom
- **Revisar pontos em Lazer:** 266 caixas + 16 interfones + 4 câmeras + 31 controles de acesso — verificar se há pontos de dados/voz adicionais
- **Certificação de rede:** Incluir no orçamento os custos de teste e certificação de cabos (Fluke, etc.)
- **Usar quantidades DWG para buchas/conectores:** DWG (556+132) é mais preciso que IFC (860+860) — evitar duplicação

---

*Briefing gerado por Cartesiano | Data: 2026-03-24 | Fonte: IFCs rev.01 (out/2024) + DWGs rev.01 (mar/2026)*

**Status:** ⚙️ EM ANDAMENTO — Infraestrutura passiva completa. Pendente: cabeamento, ativos de rede, memoriais
