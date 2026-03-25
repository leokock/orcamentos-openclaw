# Análise Projeto Parador AG7 — Estrutura, Terraplanagem, Ancoragem e Concreto Aparente

**Data:** 10/03/2026  
**Objetivo:** Identificar documentos úteis para orçamento executivo, levantar quantitativos existentes e apontar riscos de orçamento.

---

## 1. ARQUIVOS-CHAVE ENCONTRADOS

### 📁 18. Estrutura (Pasta ID: `10gOYspbcL0O8Z0_vxcfileOfTswkV6fN`)

| Arquivo | Tipo | Utilidade | Status |
|---------|------|-----------|--------|
| **PAR-EST-EX-GERA-R01 resumo de materiais.pdf** | PDF | ✅ Quantitativos consolidados (aço, concreto, forma) | **CRÍTICO** |
| **PAR-EST-EX-0000-GERA-R00 FundacaoCombinacoes.xlsx** | XLSX | ✅ Esforços nas fundações por combinações | **CRÍTICO** |
| **PAR-EST-EX-0001-GERA-R00 CargasFundacao.xlsx** | XLSX | ✅ Cargas por pilar/fundação | **CRÍTICO** |
| **PAR-EST-EX-0000-PG-SUB1-R00 planta de cargas.pdf** | PDF | Planta de cargas subsolo (gráfico) | Complementar |
| **PAR-EST-EX-0001-PG-SUB1-R00 tabela planta de cargas.pdf** | PDF | Tabela de cargas (gráfico) | Complementar |
| **PAR-EST-EX-0004-PG-SUB1-R00 reacoes contencao.pdf** | PDF | Reações na contenção | Complementar |
| **PAR-EST-EX-2000-PG-GERA-R03.IFC** | IFC | Modelo estrutural Bloco B (40MB) | Prioridade média |
| **PAR-EST-EX-1000-PG-GERA-R02.IFC** | IFC | Modelo estrutural Bloco A (35MB) | Prioridade média |
| **DWG executivos** | DWG | 50+ plantas de forma (subsolo, térreo, tipo, cobertura) | Baixar sob demanda |

### 📁 30. Terraplanagem (Pasta ID: `1moakV-oI2oSYwGeAT4ha-51yNt4m9cmX`)

| Arquivo | Tipo | Utilidade | Status |
|---------|------|-----------|--------|
| **Memorial Terraplenagem Parador-R00.pdf** | PDF | ✅ Escopo, volumes, critérios técnicos | **CRÍTICO** |
| **Parador A1 - terreno primitivo-R02.pdf** | PDF | Planta topográfica (antes) | Complementar |
| **Parador A1 - terreno terraplanado-R02.pdf** | PDF | Planta topográfica (depois) | Complementar |
| **ART 9545133-2-R00.pdf** | PDF | ART do projeto de terraplanagem | Registro |

### 📁 06. Ancoragem (Pasta ID: `1CBVS5YIzFdWNnJ8j2QrU2GWlsgDePuff`)

| Arquivo | Tipo | Utilidade | Status |
|---------|------|-----------|--------|
| **PAR-ANC-EX-0001-PG-COBE-R00.pdf** | PDF | ✅ Ancoragens definitivas Rooftop — 119 pontos | **CRÍTICO** |
| **PAR-ANC-EX-0002-PG-COBE-R00.pdf** | PDF | ✅ Ancoragens definitivas Rooftop — 130 pontos | **CRÍTICO** |
| **PAR-ANC-PE-0001-PG-ROO-R00.pdf** | PDF | Pré-executivo ancoragem (1 prancha) | Complementar |

### 📁 12. Concreto Aparente (Pasta ID: `1zbrisbGZ58Gi7_-6PTWh3ECj4RWrKiH7`)

| Arquivo | Tipo | Utilidade | Status |
|---------|------|-----------|--------|
| **E-mail de AG7 - Especificação do Concreto Pigmentado-R00.pdf** | PDF | ✅ Traço, pigmento, durabilidade, proteção, mockups | **CRÍTICO** |
| **PARADOR-ESTRUTURA PIGMENTADA-R00.ifc** | IFC | Modelo IFC dos elementos em concreto pigmentado | Prioridade média |

---

## 2. O QUE DÁ PARA EXTRAIR JÁ

### 🏗️ ESTRUTURA — Quantitativos Consolidados

**Fonte:** `PAR-EST-EX-GERA-R01 resumo de materiais.pdf`

#### Totais Gerais (Bloco A + Bloco B)

| Item | Quantidade | Unidade | Observação |
|------|------------|---------|------------|
| **Aço total** | **802.998 kg** | kg | ~803 t (CA-50 + CA-60) |
| **Concreto C-45** | **7.234,32** | m³ | Todo o concreto é C-45 |
| **Forma total** | **46.679,98** | m² | Área de forma |
| **Taxa média de aço** | **111** | kg/m³ | Taxa aço/concreto |

#### Bloco A

- Aço: 354.154 kg
- Concreto: 3.067 m³
- Forma: 20.024 m²
- Taxa: 115 kg/m³

#### Bloco B

- Aço: 448.843 kg
- Concreto: 4.167 m³
- Forma: 26.655 m²
- Taxa: 108 kg/m³

#### Distribuição de Aço por Bitola (Consolidado)

| Bitola | Tipo | Quantidade (kg) | % do Total |
|--------|------|----------------|------------|
| 5.0 mm | CA-60 | 91.886 | 11,4% |
| 6.3 mm | CA-50 | 28.886 | 3,6% |
| 8.0 mm | CA-50 | 136.645 | 17,0% |
| 10.0 mm | CA-50 | 121.543 | 15,1% |
| **12.5 mm** | **CA-50** | **235.261** | **29,3%** ← Maior consumo |
| 16.0 mm | CA-50 | 92.574 | 11,5% |
| 20.0 mm | CA-50 | 96.200 | 12,0% |

#### Elementos Estruturais Identificados

- Fundações: blocos + arranques
- Subsolo (SS): vigas + lajes + pilares
- Térreo (TER): vigas/paredes + lajes + pilares
- Tipo (TIP): vigas + lajes + pilares (repetição)
- Duplex Superior (DSU): vigas + lajes + pilares
- Cobertura (ROO): vigas + lajes + pilares
- **7 lances de escada por bloco** (14 total)

---

### 🏗️ FUNDAÇÕES — Cargas e Esforços

**Fonte:** `PAR-EST-EX-0001-GERA-R00 CargasFundacao.xlsx` + `FundacaoCombinacoes.xlsx`

#### Pilares de Fundação Identificados

| Pilar | Seção (cm) | Carga PP (tf) | Adicional (tf) | Solo (tf) | Acidental (tf) | Água (tf) | Vento máx (tf) |
|-------|------------|---------------|----------------|-----------|----------------|-----------|----------------|
| PA1 | 24×50 | 42,22 | 12,81 | 13,23 | 10,67 | 5,85 | 1,23 |
| PA2 | 24×50 | 50,74 | 14,48 | 15,39 | 13,05 | 7,29 | 2,50 |
| PA4 | 24×98 | 39,36 | 11,05 | 8,64 | 8,35 | 2,55 | 11,35 |
| PA5 | 24×98 | 23,06 | 6,02 | 4,62 | 4,21 | 1,17 | 5,22 |
| PA6 | 24×50 | 17,90 | 4,36 | 3,91 | 3,28 | 4,06 | 5,46 |
| PA8 | 30×50 | 52,92 | 14,94 | 14,56 | 11,53 | 16,54 | 3,11 |
| PA9 | 24×50 | 42,16 | 13,48 | 13,65 | 10,80 | 15,90 | 0,43 |
| PA11 | 30×50 | 67,82 | 23,35 | 17,90 | 15,28 | 18,79 | 3,88 |
| PA12 | 24×65 | 37,22 | 24,33 | 5,06 | 12,79 | 3,70 | 2,34 |
| PA13 | 20×60 | 25,87 | 18,07 | 2,65 | 8,79 | 0,89 | 7,64 |
| PA14 | 24×50 | 46,65 | 15,28 | 14,91 | 12,15 | 18,11 | 1,40 |
| PA16 | 24×30 | 52,64 | 27,13 | 11,25 | 18,57 | 10,20 | 0,97 |

**Observação:** Tabela parcial. Planilha completa contém todas as fundações com combinações de esforços (N, Mx, My, Vx, Vy, Mt).

#### Seções de Fundação Identificadas
- 20×60 cm, 24×30 cm, 24×50 cm, 24×65 cm, 24×98 cm, 30×50 cm

---

### ⛰️ TERRAPLANAGEM — Volumes e Escopo

**Fonte:** `Memorial Terraplenagem Parador-R00.pdf`

#### Quantitativos

| Item | Quantidade | Unidade | Observação |
|------|------------|---------|------------|
| **Área a terraplanar** | **11.723,09** | m² | |
| **Volume de corte** | **20.020** | m³ | Com empolamento 30% |
| **Fator de empolamento** | **30%** | % | |
| **Cota de projeto** | **-0,20 m** | | Abaixo da cota arquitetônica |

#### Serviços Previstos

1. **Preliminares:**
   - Mobilização + preparação
   - Implantação de estruturas de contenção (ver pasta Estrutura)
   - Desmatamento + destocamento + limpeza
   
2. **Escavação/Corte:**
   - Escavação para subsolo
   - Regularização e desempeno de taludes (1:1 = 45°)
   - Verificação com gabarito

3. **Transporte:**
   - **Obrigatório:** caminhões basculantes
   - Gestão de interferência com tráfego urbano
   
4. **Drenagem:**
   - Bombeamento de águas pluviais para nível da rua
   - Tubulação → bocas-de-lobo municipais
   
5. **Complementares:**
   - Acessos provisórios para equipamentos
   - Controle tecnológico/topografia

#### Responsável Técnico
- Ricardo Tiburtius Logullo – Eng. Civil, M.Sc. CREA/SC 072.673-6
- Data: 28/10/2024

---

### 🔗 ANCORAGEM — Dispositivos Definitivos (SPIQ)

**Fonte:** `PAR-ANC-EX-0001-PG-COBE-R00.pdf` + `PAR-ANC-EX-0002-PG-COBE-R00.pdf`

#### Quantitativos

| Prancha | Localização | Quantidade |
|---------|-------------|------------|
| 0001 | Rooftop Cobertura | **119 pontos** |
| 0002 | Rooftop Cobertura | **130 pontos** |
| **TOTAL** | | **249 pontos** |

#### Especificação Técnica

| Item | Especificação |
|------|---------------|
| **Sistema** | Dispositivo de ancoragem definitiva tipo "casa do chumbador" (S-Point ou similar) |
| **Material** | Aço Inox 304L ou 316L |
| **Haste roscada** | Inox ½" (12,7 mm) |
| **Fixação** | Química — resina viniléster ou epóxi (Fischer FIS V) |
| **Furo** | Ø14 mm × 140 mm profundidade |
| **Substrato** | Concreto ou graute ≥ 20 MPa |
| **Carga de ensaio** | **1.500 kgf** (arrancamento estático) |
| **Carga de trabalho** | **600 kgf** (uso) |
| **Fator de segurança** | 2,5 |
| **Ensaio** | **100% dos pontos** |
| **Inspeção periódica** | **12 meses** |

#### Posições

- Verticais: maioria (~170 un)
- Horizontais: ~70 un
- Com vara de manobra 6m: ~10 un (difícil acesso)

#### Espaçamento

- **Padrão:** 2,00 m (máximo)
- **Reduzido:** 0,57 m a 1,85 m (curvas, cantos, zonas críticas)

#### Elementos de Instalação

- **Lajes (LB):** h = 15 cm, 20 cm, 25 cm
- **Vigas de borda (VB):** 200+ vigas (seções variadas: 19×50, 20×20, 30×25, etc.)
- **Pilares de borda (PB):** 200+ pilares (seções variadas: 19×30, 19×60, 20×30, etc.)

#### Normas Aplicáveis
- NR-18.12.12 (Portaria 3.733/2020)
- NR-35 (Trabalho em altura)
- NBR 16325-1 A1 (Proteção contra quedas)
- NBR 16457 (Profundidade de embutimento)

---

### 🎨 CONCRETO APARENTE PIGMENTADO

**Fonte:** `E-mail de AG7 - Especificação do Concreto Pigmentado-R00.pdf`

#### Traço — Composição Base

| Componente | Especificação | % spc | Observação |
|------------|---------------|-------|------------|
| **Pigmento** | **BAYFERROX 601M** (LANXESS) | **0,66% a 1,00%** | Ponto de partida: 0,83% |
| **Cimento base** | 60% CPV + 40% cimento branco | — | Amostra aprovada IW |
| **Alternativa (teste)** | 100% CP + Dióxido de Titânio (TiO₂) | 2% a 4% | Clareamento mais eficiente |

#### Requisitos de Durabilidade — Ambiente Marinho (Classe IV)

| Requisito | Especificação | Justificativa |
|-----------|---------------|---------------|
| **Cobrimento** | ≥ 4,0 cm | Proteção contra cloretos |
| **Relação a/agl** | 0,45 a 0,50 | Reduzir permeabilidade |
| **Sílica ativa** | Sim | Resistência a cloretos |
| **Cristalizante** | Sim | Impermeabilização por cristalização |
| **Tratamento superficial** | Silicato + hidrofugante | Proteção de fachada (sequência obrigatória) |
| **Proteção armaduras** | Opcional: galvanização ou MCI 2005 | Conforme análise de salinidade |

#### Controle de Uniformidade de Cor

⚠️ **RISCO CRÍTICO:** Concreteiras de Balneário Camboriú provavelmente nunca trabalharam com concreto pigmentado.

**Concreteira indicada:** CONCREBRAS (Jair — 48 99166-7191)
- Tem experiência com cimento branco e pigmentos no litoral do PR
- Já forneceu para ÍCARO, AGE360 e PACE da AG7

#### Fornecedores de Pigmento

| Fornecedor | Tipo | Contato |
|------------|------|---------|
| LANXESS | Fabricante | Maria — 11 98444-3304 |
| CLARIQUÍMICA | Distribuidor | Paulo — 11 99600-9438 / 98489-0615 |

#### Testes Propostos (Vértices — Gabriel Regino)

| Teste | Composição | Objetivo |
|-------|-----------|----------|
| 1 | 60% CP + 125 kg/m³ CB (~35%) + 0,83% 601M | Ajuste fino da base aprovada |
| 2 | 100% CP + 2% TiO₂ + 0,83% 601M | Redução custo (menos CB) |
| 3 | 100% CP + 4% TiO₂ + 0,83% 601M | Maior clareamento |
| 4 | 100% CP + 0,83% 601M (sem clareamento) | Comparativo baixo custo |

**Status:** Pendente videochamada AG7 × Vértices + retorno de Lucas Jimeno (IW) sobre tom final desejado.

---

## 3. LACUNAS CRÍTICAS

### 🚨 FUNDAÇÕES + CONTENÇÃO + ESCAVAÇÃO

| Lacuna | Impacto | Prioridade |
|--------|---------|------------|
| **Projeto de contenção/escavação não localizado** | ⚠️ **ALTO** — Impossível orçar sistema de contenção sem projeto | **URGENTE** |
| **Sondagem geotécnica não localizada** | ⚠️ **ALTO** — Tipo de fundação (estaca, tubulão, sapata) indefinido | **URGENTE** |
| **Tipo de fundação não especificado** | ⚠️ **ALTO** — Cargas existem, mas não há definição se é estaca raiz, hélice, tubulão, sapata | **URGENTE** |
| **Comprimentos de estacas/profundidade** | ⚠️ **ALTO** — Sem sondagem, impossível estimar comprimentos | **URGENTE** |
| **Sistema de contenção (cortina, solo grampeado, etc.)** | ⚠️ **ALTO** — Memorial de terraplanagem cita "paredes de contenção" mas não localiza projeto | **URGENTE** |
| **Reações na contenção (PDF existe mas não baixado)** | Médio — Existe arquivo, baixar se necessário | Baixa |

### 🚨 ESTRUTURA

| Lacuna | Impacto | Prioridade |
|--------|---------|------------|
| **Quantitativo de blocos/sapatas de fundação** | Alto — Só temos cargas, não geometria/volume | Alta |
| **Volume de concreto por pavimento detalhado** | Médio — Temos total, mas não break por pavimento | Média |
| **Memorial de cálculo estrutural** | Médio — Critérios, fck, sobrecargas, ações | Média |
| **Detalhamento de escadas** | Baixo — Sabemos que são 7 por bloco, falta geometria | Baixa |

### 🚨 CONCRETO APARENTE

| Lacuna | Impacto | Prioridade |
|--------|---------|------------|
| **Tom final não definido** | ⚠️ **ALTO** — Lucas Jimeno (IW) ainda não confirmou tom exato | **URGENTE** |
| **Mockups não executados** | ⚠️ **ALTO** — 4 testes propostos pendentes de execução | **URGENTE** |
| **Quantitativo de superfície aparente** | ⚠️ **ALTO** — Não sabemos m² de fachada em concreto pigmentado | **URGENTE** |
| **Modelo IFC de concreto pigmentado não analisado** | Médio — Arquivo existe (1,1 MB), pode ter m² de faces | Alta |
| **Controle de qualidade na concreteira não detalhado** | Alto — Videochamada AG7 × Vértices pendente | Alta |

### 🚨 TERRAPLANAGEM

| Lacuna | Impacto | Prioridade |
|--------|---------|------------|
| **Projeto de contenção (citado no memorial)** | ⚠️ **ALTO** — Memorial cita, mas não localizado | **URGENTE** |
| **Destino final do material escavado** | Médio — 20.000 m³ precisam de destino | Média |
| **Restrições municipais de tráfego** | Médio — BC tem trânsito pesado | Média |

### 🚨 ANCORAGEM

| Lacuna | Impacto | Prioridade |
|--------|---------|------------|
| **Legenda completa dos códigos VA/PA/LA** | Médio — Dificulta quantificação exata por tipo | Média |
| **Localização em planta de cada ponto** | Baixo — Tempos de deslocamento/logística | Baixa |
| **Consumo de resina por furo** | Médio — Impacta custo de insumo | Média |

---

## 4. IMPLICAÇÕES PARA ORÇAMENTO EXECUTIVO

### ⚠️ RISCOS CRÍTICOS DE ORÇAMENTO

#### 1. **FUNDAÇÕES — RISCO MÁXIMO (Bloqueador)**

**Problema:**  
Não foi localizado:
- Projeto de fundação (tipo: estaca, tubulão, sapata)
- Sondagem geotécnica
- Projeto de contenção/escavação

**Impacto:**  
❌ **IMPOSSÍVEL ORÇAR fundações e contenção sem esses projetos.**

**Itens bloqueados:**
- Sistema de contenção (cortina atirantada, solo grampeado, parede diafragma, etc.)
- Tipo de fundação (estaca raiz, hélice contínua, pré-moldada, tubulão, sapata)
- Comprimento de estacas (depende de sondagem)
- Volume de concreto de blocos/sapatas/tubulões
- Armação de blocos
- Sistema de escavação + escoramento

**Custo estimado dos itens bloqueados:**  
**30% a 40% do custo total da estrutura** (fundação + contenção costumam representar essa faixa em obras com subsolo em terreno íngreme/marinho)

**Ação imediata:**  
1. Solicitar à AG7: sondagem geotécnica
2. Solicitar ao calculista estrutural: projeto executivo de fundação (memorial + pranchas)
3. Solicitar ao geotécnico: projeto executivo de contenção

---

#### 2. **CONCRETO APARENTE — RISCO ALTO (Custo + Prazo)**

**Problema:**  
- Tom final não definido (pendente retorno Lucas Jimeno/IW)
- Mockups não executados (4 testes propostos)
- Quantitativo de superfície aparente não levantado
- Concreteiras locais sem experiência com pigmentação

**Impacto em custo:**

| Item | Custo Base | Custo Pigmentado | Δ (%) | Observação |
|------|------------|------------------|-------|------------|
| Concreto C-45 padrão | R$ 650/m³ | R$ 850-1.050/m³ | **+30% a +60%** | Pigmento + CB + controle qualidade |
| Sílica ativa + cristalizante | — | R$ 80-120/m³ | — | Ambiente marinho (obrigatório) |
| Tratamento superficial | — | R$ 45-70/m² | — | Silicato + hidrofugante |
| Galvanização armaduras | — | R$ 5-8/kg | **+700%** | Opcional (se optar) |
| MCI 2005 (nano inibidor) | — | R$ 25-40/m³ | — | Opcional (se optar) |

**Risco de retrabalho:**  
Se o tom não for aprovado após concretagem, **custo de demolição + refazer = R$ 1.200-1.500/m³** (concreto + mão de obra + forma + descarte).

**Risco de manchamento:**  
Variação de cor entre betonadas gera **perda estética irreversível** → necessita controle rigoroso na concreteira (custo de acompanhamento técnico full-time).

**Ação imediata:**  
1. Executar os 4 mockups propostos por Gabriel Regino (Vértices)
2. Confirmar tom com Lucas Jimeno (IW)
3. Quantificar m² de fachada em concreto aparente (analisar IFC)
4. Videochamada AG7 × Vértices × CONCREBRAS (Jair) para alinhar controle de qualidade

**Prazo de impacto:**  
Mockups + aprovação podem adicionar **4 a 8 semanas** ao cronograma antes de liberar concretagem de fachada.

---

#### 3. **TERRAPLANAGEM + CONTENÇÃO — RISCO ALTO (Bloqueador)**

**Problema:**  
Memorial cita "estruturas de contenção" mas projeto não foi localizado.

**Impacto:**  
Volume de corte (20.000 m³) requer contenção prévia. Sem projeto de contenção:
- Impossível orçar sistema (cortina, grampeamento, parede diafragma, etc.)
- Impossível definir cronograma (escavação depende de instalação da contenção)
- Risco de instabilidade se escavar sem contenção adequada

**Custo estimado da contenção:**  
R$ 150-400/m² de face (depende do tipo: solo grampeado ~R$ 200/m², cortina atirantada ~R$ 350/m²)

**Ação imediata:**  
Solicitar à AG7 o projeto de contenção citado no memorial de terraplanagem.

---

#### 4. **ANCORAGEM — RISCO MÉDIO (Custo Controlável)**

**Quantitativo definido:** 249 pontos  
**Custo unitário estimado:** R$ 800-1.200/ponto (material + instalação + ensaio)  
**Custo total estimado:** R$ 200.000 a R$ 300.000

**Riscos:**
- Acesso difícil (vara de manobra 6m) aumenta tempo de instalação
- Geometria curva da cobertura dificulta locação precisa
- 100% de ensaios obrigatórios (custo de instrumentação + mão de obra)

**Ação:**  
- Confirmar legenda VA/PA/LA com projetista (Tresso Engenharia — Alexandre)
- Solicitar planta com mark-up de localização exata dos pontos

---

### 📊 RESUMO DE IMPACTO NO ORÇAMENTO

| Disciplina | Status Docs | Quantitativos | Risco Orçamento | Bloqueador? |
|------------|-------------|---------------|-----------------|-------------|
| **Estrutura (superestrutura)** | ✅ Completo | ✅ Disponível | 🟢 Baixo | ❌ Não |
| **Fundações** | ❌ Ausente | ⚠️ Só cargas | 🔴 Máximo | ✅ **SIM** |
| **Contenção/Escavação** | ❌ Ausente | ⚠️ Só memorial | 🔴 Máximo | ✅ **SIM** |
| **Terraplanagem** | ✅ Completo | ✅ Disponível | 🟢 Baixo | ❌ Não |
| **Ancoragem** | ✅ Completo | ✅ Disponível | 🟡 Médio | ❌ Não |
| **Concreto Aparente** | ⚠️ Parcial | ❌ Ausente | 🔴 Alto | ⚠️ Risco retrabalho |

---

## 5. PRÓXIMOS PASSOS RECOMENDADOS

### 🚨 URGENTE (Bloqueadores)

1. **Solicitar à AG7:**
   - [ ] Sondagem geotécnica (SPT ou similar)
   - [ ] Projeto executivo de fundação
   - [ ] Projeto executivo de contenção/escavação

2. **Concreto Aparente:**
   - [ ] Confirmar tom com Lucas Jimeno (IW Arquitetura)
   - [ ] Executar 4 mockups propostos (Vértices)
   - [ ] Quantificar m² de fachada aparente (analisar IFC `PARADOR-ESTRUTURA PIGMENTADA-R00.ifc`)
   - [ ] Agendar videochamada AG7 × Vértices × CONCREBRAS

### 🔶 ALTA PRIORIDADE

3. **Ancoragem:**
   - [ ] Solicitar legenda completa VA/PA/LA ao projetista (Tresso Eng.)
   - [ ] Solicitar planta com mark-up de localização

4. **Estrutura:**
   - [ ] Solicitar memorial de cálculo estrutural (critérios, fck, sobrecargas)
   - [ ] Solicitar quantitativo de blocos/sapatas

### 🔷 MÉDIA PRIORIDADE

5. **Terraplanagem:**
   - [ ] Confirmar destino final dos 20.000 m³ escavados
   - [ ] Verificar restrições municipais de tráfego/horário em BC

6. **Geral:**
   - [ ] Baixar modelos IFC estruturais (se precisar de geometrias específicas)
   - [ ] Baixar DWG executivos (sob demanda conforme avanço do orçamento)

---

## 6. DOCUMENTOS PRIORITÁRIOS PARA DOWNLOAD (Próxima Rodada)

Caso necessite avançar em alguma frente específica:

| Arquivo Google Drive | ID | Tamanho | Prioridade |
|----------------------|----|---------|------------|
| PARADOR-ESTRUTURA PIGMENTADA-R00.ifc | 1WB5DWoPvPp0lyphFWdNciZc9FBvdWZo6 | 1,1 MB | Alta (quantificar m²) |
| PAR-EST-EX-2000-PG-GERA-R03.IFC (Bloco B) | 1tdqu0-WnhJKnM-lqeQvkzWS0-Bi3qlwe | 40 MB | Média (geometrias detalhadas) |
| PAR-EST-EX-1000-PG-GERA-R02.IFC (Bloco A) | 1Dl2GWlUXI-QLmXcn6EMuOHT9lA7HxVzT | 35 MB | Média (geometrias detalhadas) |
| PAR-ANC-PE-0001-PG-ROO-R00.pdf (Pré-exec anc.) | 1kWKGZXe1JyehIBMIKdhtg1kgqybPBTI3 | 1 MB | Baixa (apenas pré-executivo) |

---

## 7. CONCLUSÃO

### ✅ O que já está pronto para orçar:

- Superestrutura (aço, concreto, forma)
- Terraplanagem (volumes, serviços)
- Ancoragens (quantitativo, especificação)

### ❌ O que está bloqueado:

- **Fundações** (tipo, comprimento, volume)
- **Contenção** (sistema, área, tipo)
- **Concreto aparente** (m² de superfície, tom final, mockups)

### 💰 Estimativa de Impacto:

Itens bloqueados representam aproximadamente **35% a 50% do custo total da estrutura**.

**Recomendação:**  
Orçar separadamente:
1. **Orçamento Fase 1 (liberado):** Superestrutura + Terraplanagem + Ancoragem
2. **Orçamento Fase 2 (pendente):** Fundações + Contenção + Concreto Aparente (após receber projetos faltantes)

---

**Relatório gerado por:** Jarvis (sub-agente)  
**Pasta Google Drive analisada:** `1In7TnY1TkQSA6UOlXYbyiw_z9kJ0OWV0`  
**Total de arquivos mapeados:** 200+ (escaneados 4 pastas principais)  
**Arquivos baixados e analisados:** 10 (8 PDFs + 2 XLSX)
