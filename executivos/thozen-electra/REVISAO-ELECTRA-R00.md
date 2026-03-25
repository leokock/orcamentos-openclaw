# Revisão da Planilha Executiva R00 — Electra Towers (Thozen)

> **Tarefa:** Análise da estrutura da planilha executiva R00 do projeto Electra Towers para implementação de workflow incremental por disciplina
> 
> **Data:** 21/03/2026
> **Planilha:** `~/orcamentos/executivo/thozen-electra/CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx`

---

## 1. DADOS DO PROJETO (aba CAPA)

**Identificação:**
- **Projeto:** Electra Towers
- **Cliente:** Thozen
- **Revisão:** R00
- **Localização:** Rua Rubens Alves, Balneário Perequê, Porto Belo/SC

**Configuração:**
- **Área Construída:** 36.088,85 m²
- **Área do Terreno:** 824,72 m²
- **Área de Lazer:** 2.253,40 m²
- **Unidades Residenciais:** 342
- **Unidades Comerciais:** 6
- **Total de Unidades:** 348
- **Nº Pavimentos:** 24 (tipo)
- **Nº Subsolos:** 1
- **Nº Vagas:** 305
- **Prazo de Obra:** 36 meses
- **Tipologia:** 2 torres residenciais verticais + embasamento

**Características Técnicas (de PROJETO.md):**
- **Pavimentos por torre:** 34 (1º Térreo + 5 Garagens + 1 Lazer + 24 Tipo + 3 técnicos)
- **Fundação:** Estacas hélice contínua (Ø50cm e Ø60cm)
- **Status:** Em orçamento executivo (disciplinas sendo desenvolvidas incrementalmente)

---

## 2. ESTRUTURA DA PLANILHA R00

### Abas de Gestão e Configuração

#### CAPA (107 linhas)
- Dados gerais do empreendimento
- Distribuição de áreas por pavimento (Torre 1 e Torre 2)
- Configuração de unidades e dormitórios

#### PROJETOS (72 linhas)
- Gestão dos projetos (disciplinas)
- Controle de revisões e fontes (IFCs, DWGs)

#### BASES (1.031 linhas)
- Estimativas de custos indiretos
- Parâmetros de cálculo (CUB, índices)
- Comparações com outras obras (ex: Porto Ruby)

---

### Abas de Estrutura de Custos

#### EAP (684 linhas)
- **Estrutura Analítica de Projeto** — hierarquia de custos
- Estrutura: Unidade Construtiva → Célula → Etapa → Subetapa → Serviço
- Níveis codificados (ex: 01.001.002 = Unidade 1, Célula 1, Etapa 1, Subetapa 2)

#### EAP Análise (549 linhas)
- **Resumo de custos por macrogrupo**
- Status: **MUITOS VALORES ZERADOS OU #REF!** — confirma que a planilha está em construção
- Etapas identificadas:
  - ✅ Gerenciamento Técnico e Administrativo: R$ 10.320.093,99 (R$ 285,96/m²)
  - ✅ Movimentação de Terra: R$ 1,31
  - ✅ Infraestrutura: R$ 507.169,40 (R$ 14,05/m²)
  - ⏸️ Contenção: R$ 0
  - ✅ Supraestrutura: R$ 152.174,29 (R$ 4,22/m²)
  - ⏸️ Alvenaria: R$ 0
  - ✅ Instalações Elétricas, Hidráulicas, GLP e Preventivas: R$ 9.767.888,03 (R$ 270,66/m²)
  - ⏸️ Louças e Metais: R$ 0
  - ⏸️ Climatização, Exaustão Mecânica e Pressurização: R$ 0
  - ✅ Instalações e Equipamentos e Sistemas Especiais: R$ 3.949.092,02 (R$ 109,43/m²)
  - ⏸️ Revestimentos Argamassados: R$ 0
  - ⏸️ Impermeabilização: #REF!
  - ⏸️ Acabamentos Internos: R$ 0
  - ⏸️ Pisos e Pavimentações: R$ 0
  - ⏸️ Teto: R$ 0
  - ✅ Pintura Interna: R$ 21.474,42 (R$ 0,60/m²)
  - ⏸️ Fachada: R$ 0

#### CPU (4.053 linhas)
- **Composições de Preços Unitários**
- Estrutura: Repetição | Tipo | Descrição | Unidade | Quantidade | Custo Unit. | Custo Total
- Tipos: Etapa, Subetapa, Serviço, Insumo
- Exemplo identificado: Instalações Provisórias (central de aço, central de fôrmas, central de argamassa)

#### Insumos (1.225 linhas)
- **Catálogo de insumos** com preços unitários
- Grupos: Aço, Concreto, Blocos, Argamassa, etc.
- Exemplos:
  - Arame Galvanizado: R$ 13,69/kg
  - Aço CA50 10mm: R$ 5,76/kg
  - Aço CA50 20mm: R$ 5,59/kg
  - Monocordoalha engraxada CP-190: R$ 15,50/kg
- Status: **Aparentemente populado**

---

### Abas por Disciplina (Templates Estruturados)

#### Estacas (86 linhas)
- **Status:** ✅ PREENCHIDO
- **Torre 1:**
  - Ø50cm: 17 un × 25m = 425m total
  - Ø60cm: 406 un × 25m = 10.150m total

#### Fund. Rasa | Contenção (256 linhas)
- **Status:** ⏸️ ESTRUTURA VAZIA
- Template pronto para:
  - Blocos quadrados/retangulares (Torre 1, Torre 2)
  - Blocos triangulares
  - Vigas baldrames
  - Contenções (parede diafragma, mureta guia, viga coroamento)

#### Resumo Estrutura (84 linhas)
- **Status:** ⏸️ ESTRUTURA VAZIA
- Template com níveis:
  - Contenções
  - Fundação (blocos, pilares, vigas, contrapiso, cisternas, dutos)
  - Embasamento (térreo, garagens)
  - Torre (pavimentos tipo, cobertura, barrilete)
- Elementos por nível: pilares, vigas, lajes, escadas, reservatórios

#### Escoramento (1.000 linhas)
- Template estruturado (não analisado em detalhe)

#### ARQUITETURA (97 linhas)
- **Status:** ✅ PARCIALMENTE PREENCHIDO
- **Alvenaria de vedação com blocos de concreto:**
  - 1º Subsolo 1: Bloco 14cm (130,61 m²), Bloco 19cm (143,39 m²)
  - Térreo: Bloco 9cm (1,71 m²), Bloco 14cm (197,94 m²), Bloco 19cm (323,75 m²)
  - 1º Pavto (Torre): estrutura pronta, valores a preencher

#### LOUÇAS E METAIS (995 linhas)
- **Status:** ⏸️ ESTRUTURA VAZIA
- Template com aplicações:
  - Louças: bacia sanitária, cuba, lavatório, cuba cozinha, tanque
  - Metais: torneiras, registros, válvulas
  - Chuveiros e acessórios
- Colunas: Aplicação | Descrição | Un. | Total | Qtde por Pavimento (Térreo, Tipo, etc)

#### ESQUADRIAS (1.082 linhas)
- **Status:** ⏸️ ESTRUTURA VAZIA
- Template com tipos:
  - Portas madeira (P1, P2, P3 - abrir/correr)
  - Corrimão madeira
  - Esquadrias alumínio
  - Vidros temperados
- Colunas: Aplicação | Descrição | Largura | Altura | Total m²/m | Total un | Qtde por Pavimento

#### Exaustão e Climatização (969 linhas)
- Template estruturado (não analisado em detalhe)

#### MOBILIÁRIO (400 linhas)
- Template estruturado (não analisado em detalhe)

---

### Abas de Instalações Especiais (Templates)

#### EPCs (1.004 linhas)
- Template para equipamentos especiais (elevadores, escadas rolantes, etc.)

#### CANTEIRO (976 linhas)
- Template para instalações de canteiro de obras

#### Cont.Tecnol. (1.082 linhas)
- Template para contingências tecnológicas

#### Equipamentos Especiais (980 linhas)
- Template geral de equipamentos

---

## 3. DISCIPLINAS EM DESENVOLVIMENTO (de PROJETO.md)

### ✅ Instalações Especiais — Prevenção e Combate a Incêndio (PCI)
- **Revisão:** R00 (2026-03-20)
- **Status:** ⚠️ Preliminar
- **Fontes:** IFC rev.01 (Torre A e B), DWGs 11 pranchas
- **Briefings:** `briefings/pci-civil-r00.md` + resumo + anexo pavimentos
- **Pendências:**
  - Reservatórios e bombas de incêndio (não encontrados no IFC)
  - Metragem real de tubulação (valor extraído subestimado)
  - Sistema de sprinklers (não identificado)
  - Memorial descritivo do sistema

### ✅ Instalações Telefônicas e Lógica (Cabeamento Estruturado)
- **Revisão:** R00 (2026-03-20)
- **Status:** ⚠️ PARCIAL — Infraestrutura passiva extraída
- **Fontes:** 9 IFCs rev.01 + 18 DWGs rev.01
- **Projetista:** R. Rubens Alves
- **Briefings:** `briefings/telefonico-r00.md` + resumo
- **Quantitativos extraídos:**
  - 46 pontos de dados (RJ45)
  - 44 pontos de voz (RJ11)
  - ~648 caixas de passagem
  - ~33.400 m de eletrodutos (incluindo Tipo x24)
  - 33 m de eletrocalhas
  - 3.694 acessórios de fixação
- **Pendências:**
  - Metragens de cabos UTP (CAT6/CAT6A) — não modelados
  - Racks de telecomunicações (quantidade, localização)
  - Patch panels (tipo, portas)
  - DG (Distribuidor Geral) — especificação e localização

### ⏸️ Instalações Especiais — Ventilação Mecânica (Escadas Pressurizadas)
- **Revisão:** R05 (projeto legal)
- **Status:** ⚠️ PREMISSAS NÃO VALIDADAS — DWG não pôde ser processado
- **Fontes:** RA_EVM_LEGAL_PROJETO_R05.dwg (AutoCAD 2018/2019/2020)
- **Briefings:** `briefings/ventilacao-r00.md` + resumo + log extração
- **Quantitativos:** Estimativas baseadas em NBR 14880:2024
- **Custo estimado:** R$ 328k - 554k
- **Pendências:**
  - Extração automática do DWG falhou
  - Todos os quantitativos são estimativas
  - Memorial descritivo obrigatório
  - Prancha de detalhes
  - Confirmação de número de escadas pressurizadas

### 🚧 Instalações Especiais — Ar-Condicionado e Climatização
- **Revisão:** R05
- **Status:** 🚧 EXTRAÇÃO PENDENTE — DWG não pôde ser processado
- **Fontes:** RA_ARC_EXE_00_TODAS CAD_R05.dwg (5.0 MB, AutoCAD nativo)
- **Briefings:** `briefings/ar-condicionado-r00.md` (estrutura pronta)
- **Estimativa paramétrica:** R$ 80-150/m² AC → R$ 1,6M - 4,5M (±30-40% precisão)
- **Pendências:**
  - Conversão DWG → DXF necessária
  - Equipamentos (condensadoras, evaporadoras, VRF)
  - Tubulações frigoríficas
  - Linhas de dreno
  - Memorial descritivo

---

## 4. ANÁLISE — O QUE JÁ ESTÁ PREENCHIDO vs O QUE FALTA

### ✅ Preenchido ou Parcialmente Preenchido

| Disciplina | Status | Completude |
|------------|--------|------------|
| Gerenciamento Técnico/Administrativo | ✅ | Valores consolidados (R$ 10,3M) |
| Infraestrutura (Estacas) | ✅ | Quantitativos completos (Torre 1) |
| Supraestrutura | ✅ | Valor consolidado (R$ 152k) |
| Instalações (Elétrica/Hidro/GLP/Preventivas) | ✅ | Valor consolidado (R$ 9,7M) |
| Equipamentos e Sistemas Especiais | ✅ | Valor consolidado (R$ 3,9M) |
| Pintura Interna | ✅ | Valor consolidado (R$ 21,4k) |
| Arquitetura (Alvenaria) | 🟡 | Térreo + 1º Subsolo preenchidos |

### ⏸️ Estrutura Pronta, Aguardando Dados

| Disciplina | Template | Pendências |
|------------|----------|------------|
| Fundação Rasa | ✅ | Blocos, vigas baldrames, contenção |
| Resumo Estrutura | ✅ | Pilares, vigas, lajes, escadas (por pavimento) |
| Louças e Metais | ✅ | Quantidades por tipologia e pavimento |
| Esquadrias | ✅ | Portas, janelas, vidros (por tipologia) |
| Climatização | ✅ | Equipamentos, tubulações, acessórios |
| Exaustão | ✅ | Dutos, dampers, grelhas |
| Mobiliário | ✅ | Armários, bancadas, equipamentos fixos |
| Canteiro | ✅ | Instalações provisórias, equipamentos |

### ❌ Disciplinas com Valor Zero ou #REF!

- Contenção
- Alvenaria (consolidado)
- Louças e Metais (consolidado)
- Climatização (consolidado)
- Revestimentos Argamassados (piso/parede/teto)
- Impermeabilização (#REF! — erro de fórmula)
- Acabamentos Internos (parede, piso, teto)
- Fachada

---

## 5. OBSERVAÇÕES TÉCNICAS

### Estrutura da Planilha
- **Hierarquia clara:** EAP → CPU → Insumos (rastreabilidade completa)
- **Templates bem estruturados:** Cada disciplina tem formato padronizado
- **Rastreabilidade:** Cada serviço aponta para composições (CPU) que apontam para insumos
- **Repetição de pavimentos:** Estrutura suporta replicação (Tipo x24)

### Erros Identificados
- **#REF!** na coluna de percentual (EAP Análise) — fórmula quebrada ou referência inválida
- **Valores zerados** em disciplinas não iniciadas (esperado para R00)

### Áreas de Atenção
- **Infraestrutura:** Valor muito baixo (R$ 507k para 36k m²) — pode estar incompleto
- **Supraestrutura:** Valor extremamente baixo (R$ 152k) — provável erro ou falta de dados
- **Instalações:** Valor alto (R$ 9,7M) — pode incluir equipamentos que deveriam estar separados

---

## 6. ACHADOS SOBRE ÍNDICES PARAMÉTRICOS

### Base Disponível
- **Total de obras:** 66 arquivos de índices em `~/orcamentos/parametrico-backup-20260311/indices/`
- **Cobertura:** Residencial vertical alto padrão (SC e litoral)
- **Granularidade:** Índices por disciplina (18 macrogrupos padrão)

### Obras Mais Similares ao Electra Towers

#### Características do Electra (para comparação):
- **Área Construída:** 36.088,85 m²
- **Tipologia:** Residencial multifamiliar alto padrão
- **Configuração:** 2 torres, 24 pavimentos tipo, embasamento com garagens
- **Unidades:** 342 residenciais + 6 comerciais
- **Fundação:** Estacas hélice contínua (Ø50, Ø60)
- **Padrão:** Alto (inferido de equipamentos especiais, instalações)

#### Obras Comparáveis (por similaridade de porte/padrão):

**1. SOHO 538 Art Residences** (`soho-538-indices.md`)
- **AC:** 13.632,23 m² (38% do Electra)
- **Tipologia:** Residencial multifamiliar alto padrão
- **Configuração:** 30 pavimentos, 22 tipo, 3 garagens
- **Unidades:** 48 un (46 apts + 2 coberturas)
- **Fundação:** Profunda (estacas) + Rasa
- **Laje:** Nervurada/cubeta (torre) + Maciça (embasamento)
- **Padrão:** Alto
- **Data-base:** Fev/2021 (CUB R$ 2.112,90)
- **R$/m² Total:** R$ 2.161,28 (1,023 CUB)
- **✅ Referência ideal:** Estrutura similar, padrão alto, configuração vertical

**2. By Seasons - For Seasons Apartments** (`byseasons-forseasons-indices.md`)
- **AC:** 6.348,51 m² (18% do Electra)
- **Tipologia:** Residencial multifamiliar alto padrão
- **Configuração:** ~18 pavimentos, 14 tipo, 2 garagens
- **Unidades:** 54 un
- **Fundação:** Hélice Contínua Ø50 e Ø60 (IGUAL ao Electra!)
- **Laje:** Cubetas ATEX 60×60
- **Padrão:** Alto (heliponto, piscina, garden&spa, coworking)
- **Data-base:** Set/2024 (CUB R$ 2.841,51)
- **R$/m² Total:** R$ 3.520,25 (1,24 CUB)
- **✅ Referência excelente:** Fundação idêntica, padrão alto, 2024

**3. Edifício Eliat (EZE Eilat)** (`eze-eilat-indices.md`)
- **AC:** 1.767,30 m² (5% do Electra)
- **Tipologia:** Residencial alto padrão
- **Configuração:** ~7 pavimentos, 4 tipo, 1 garagem
- **Fundação:** Hélice Contínua
- **Padrão:** Alto (porcelanato 90×90/120×120, alumínio Suprema, aspiração central)
- **Data-base:** Nov/2023 (CUB R$ 2.754,98)
- **R$/m² Total:** R$ 3.641,80 (1,32 CUB)
- **✅ Referência útil:** Padrão alto, índices por disciplina detalhados

**4. Amalfi Marine/Maiori** (`amalfi-marine-indices.md`, `amalfi-maiori-indices.md`)
- **AC:** ~6-8k m² cada
- **Tipologia:** Residencial vertical alto padrão (litoral SC)
- **Padrão:** Alto
- **✅ Referência regional:** Obras similares em SC litoral

**5. ARV Ingleses Spot** (`arv-ingleses-spot-indices.md`)
- **AC:** Grande porte
- **Tipologia:** Residencial vertical
- **✅ Referência útil:** Porte maior, índices completos

**6. Asramos Paessaggio** (`asramos-paessaggio-indices.md`)
- **AC:** Grande porte
- **Tipologia:** Residencial vertical
- **✅ Referência útil:** Porte maior, índices completos

### Índices-Chave para Benchmark

| Macrogrupo | SOHO 538 (R$/m²) | For Seasons (R$/m²) | Eliat (R$/m²) | Electra R00 (R$/m²) |
|------------|------------------|---------------------|---------------|---------------------|
| 1-Gerenciamento | 211,36 | N/D | N/D | 285,96 ✅ |
| 2-Mov. Terra | 3,32 | N/D | N/D | 0,00 ⚠️ |
| 3-Infraestrutura | 136,66 | N/D | N/D | 14,05 ⚠️ |
| 4-Supraestrutura | 499,91 | N/D | N/D | 4,22 ⚠️ |
| 5-Alvenaria | 82,28 | N/D | N/D | 0,00 ⏸️ |
| 7-Instalações | ~250 (agregado) | N/D | N/D | 270,66 ✅ |
| 9-Climatização | 31,87 | N/D | N/D | 0,00 ⏸️ |
| 8-Sist. Especiais | 111,15 | N/D | N/D | 109,43 ✅ |
| 15-Louças e Metais | 29,46 | N/D | N/D | 0,00 ⏸️ |
| 14-Esquadrias | 212,88 | N/D | N/D | 0,00 ⏸️ |

**⚠️ ALERTAS:**
- **Infraestrutura:** R$ 14,05/m² vs R$ 136,66/m² (SOHO) → Provavelmente incompleto
- **Supraestrutura:** R$ 4,22/m² vs R$ 499,91/m² (SOHO) → Definitivamente incompleto
- **Mov. Terra:** Praticamente zero → Falta preencher

---

## 7. CONCLUSÕES

### Situação Atual da Planilha R00
1. **Estrutura sólida:** Templates bem desenhados, hierarquia clara, rastreabilidade completa
2. **Preenchimento parcial:** ~30% das disciplinas com valores consolidados
3. **Disciplinas críticas faltantes:** Estrutura (supra completa), Alvenaria, Revestimentos, Esquadrias, Louças, Climatização
4. **Erros de fórmula:** #REF! em Impermeabilização (EAP Análise)
5. **Valores suspeitos:** Infraestrutura e Supraestrutura muito baixos (provável falta de dados)

### Prioridades de Preenchimento (ordem sugerida)
1. **Estrutura (Supraestrutura completa)** — impacto alto (R$ 500/m² típico)
2. **Alvenaria** — estrutura já iniciada (Térreo + Subsolo)
3. **Esquadrias** — padrão alto, impacto significativo (R$ 200/m² típico)
4. **Louças e Metais** — 348 unidades, quantidades multiplicam rápido
5. **Revestimentos (piso/parede/teto)** — área grande (36k m²)
6. **Climatização** — padrão alto exige sistema completo
7. **Impermeabilização** — corrigir #REF! e preencher

### Base Paramétrica — Qualidade
- **✅ Excelente:** 66 obras indexadas, cobertura de SC litoral
- **✅ Similaridade alta:** SOHO 538, For Seasons, Eliat são ótimas referências
- **✅ Granularidade:** Índices por disciplina (18 macrogrupos)
- **✅ Atualidade:** For Seasons (set/2024) é recente

---

## 8. PRÓXIMOS PASSOS

1. **Criar workflow incremental** (WORKFLOW-EXECUTIVO-INCREMENTAL.md)
2. **Definir checklist por disciplina** (o que precisa, como validar)
3. **Mapear índices de referência** para cada disciplina
4. **Fluxo de interação:** Leo → Jarvis/Cartesiano → Planilha → Validação
5. **Documentar processo** para o time da Cartesian replicar via Slack

---

*Última atualização: 2026-03-21*
