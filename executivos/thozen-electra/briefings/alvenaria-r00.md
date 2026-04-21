# Briefing Executivo — Alvenaria
**Projeto:** Thozen Electra  
**Disciplina:** 03 ALVENARIA  
**Revisão:** R00 (base: arquivos R01)  
**Data:** 2026-03-20  
**Responsável:** Cartesiano (extração automatizada)

---

## 1. Resumo Executivo

Projeto de alvenaria para edifício residencial vertical com **32 pavimentos**:
- **Térreo** (01)
- **Garagens** (G1 a G5 — 6 pavimentos, sendo G1=02, G2=03, G3=04, G4=05, G5=06)
- **Lazer** (07)
- **Tipos** (08 a 31 — 24 pavimentos tipo)
- **Casa de Máquinas** (32)

**Total de pranchas disponíveis:** 18 arquivos DWG (R01)
- 9 pranchas de **planta de alvenaria** (numeração sem "B")
- 9 pranchas de **locação** (numeração com "B")

**⚠️ LIMITAÇÃO CRÍTICA:** Os arquivos estão em formato **DWG proprietário**. Não foi possível processar automaticamente os quantitativos sem ferramentas de conversão (ODA File Converter, AutoCAD, etc.). Este briefing documenta a **estrutura esperada** e os **dados a serem extraídos** quando as pranchas forem processadas.

---

## 2. Premissas de Projeto

### 2.1 Estrutura de Pavimentos
| Pavimento | Descrição | Repetições | Arquivo Base | Arquivo Locação |
|-----------|-----------|------------|--------------|-----------------|
| 01 | Térreo | 1x | RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_1B_ TÉRREO LOC PRÉ-EXECUTIVO_R01.dwg |
| 02 | G1 (Garagem 1) | 1x | RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_2B_G1 LOC PRÉ-EXECUTIVO_R01.dwg |
| 03 | G2 (Garagem 2) | 1x | RA_ALV_EXE_03_G2 PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_3B_G2 LOC PRÉ-EXECUTIVO_R01.dwg |
| 04 | G3 (Garagem 3) | 1x | RA_ALV_EXE_04_G3 PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_4B_G3 LOC PRÉ-EXECUTIVO_R01.dwg |
| 05 | G4 (Garagem 4) | 1x | RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_5B_G4 LOC PRÉ-EXECUTIVO_R01.dwg |
| 06 | G5 (Garagem 5) | 1x | RA_ALV_EXE_06_G5 PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_6B_G5 LOC PRÉ-EXECUTIVO_R01.dwg |
| 07 | Lazer | 1x | RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dwg | RA_ALV_EXE_7B_ LAZER LOC PRÉ EXECUTIVO_R01.dwg |
| 08~31 | Tipos | 24x | RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dwg | RA_ALV_EXE_8B_ TIPOS LOC PRÉ-EXECUTIVO_R01.dwg |
| 32 | Casa de Máquinas + Res/Cobertura | 1x | RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dwg | RA_ALV_EXE_9B_ RES E COB LOC PRÉ-EXECUTIVO_R01.dwg |

**Total de pavimentos computados:** 32

### 2.2 Tipos de Alvenaria Esperados
Com base em projetos similares residenciais verticais, espera-se encontrar:

#### a) Alvenaria de Vedação
- Blocos cerâmicos 09×19×19 cm (paredes internas de 9 cm)
- Blocos cerâmicos 14×19×19 cm (paredes internas de 14 cm)
- Blocos de concreto 09×19×39 cm (áreas úmidas, se especificado)
- Blocos de concreto 14×19×39 cm (paredes de divisa entre unidades)

#### b) Divisórias Leves
- Drywall (gesso acartonado) — possível em áreas internas
- Divisórias removíveis (se houver em áreas comuns)

#### c) Elementos Complementares
- **Vergas** — sobre portas e janelas (comprimento típico: vão + 30 cm cada lado)
- **Contravergas** — sob janelas (comprimento típico: vão + 30 cm cada lado)
- **Juntas de dilatação** — em paredes longas (a cada 6-8 m, conforme NBR)
- **Encunhamento** — topo das paredes (alvenaria × laje)

### 2.3 Premissas de Quantificação
- **Área de alvenaria:** computada em m² de face (desconta vãos > 2 m²)
- **Espessura nominal:** considerar espessura do bloco + revestimento (se aplicável)
- **Repetição de tipos:** pavimentos 08 a 31 são idênticos (24 repetições)
- **Argamassa de assentamento:** considerar 10% da área de alvenaria para estimativa de volume
- **Perdas:** considerar 5-10% de perdas para blocos

---

## 3. Quantitativos (A SEREM EXTRAÍDOS)

### ⚠️ PENDENTE — Processamento de DWG

Os quantitativos abaixo são **estruturas de tabela a serem preenchidas** quando os arquivos DWG forem processados.

### 3.1 Alvenaria por Pavimento

| Pavimento | Tipo de Bloco | Espessura (cm) | Área Total (m²) | Observação |
|-----------|---------------|----------------|-----------------|------------|
| 01 — Térreo | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 02 — G1 | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 03 — G2 | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 04 — G3 | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 05 — G4 | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 06 — G5 | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 07 — Lazer | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 08~31 — Tipo (24x) | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] × 24 | Pavimentos repetidos |
| 32 — Res/Cob | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |

**Subtotal (antes de multiplicar tipos):** [A CALCULAR] m²  
**Total com repetições (tipos × 24):** [A CALCULAR] m²

### 3.2 Blocos Cerâmicos (Estimativa)

| Tipo de Bloco | Dimensões (cm) | Área Unitária (m²/bloco) | Área Total Aplicada (m²) | Quantidade (un) | Observação |
|---------------|----------------|--------------------------|--------------------------|-----------------|------------|
| Cerâmico 09×19×19 | 9 × 19 × 19 | 0,0361 | [A EXTRAIR] | [A CALCULAR] | Vedação interna |
| Cerâmico 14×19×19 | 14 × 19 × 19 | 0,0361 | [A EXTRAIR] | [A CALCULAR] | Vedação divisa |
| Concreto 09×19×39 | 9 × 19 × 39 | 0,0741 | [A EXTRAIR] | [A CALCULAR] | Áreas úmidas |
| Concreto 14×19×39 | 14 × 19 × 39 | 0,0741 | [A EXTRAIR] | [A CALCULAR] | Divisa estrutural |

**Total de blocos:** [A CALCULAR] un

### 3.3 Vergas e Contravergas

| Pavimento | Tipo | Quantidade (un) | Comprimento Unit. (m) | Comprimento Total (m) | Observação |
|-----------|------|-----------------|----------------------|----------------------|------------|
| 01 — Térreo | Verga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 01 — Térreo | Contraverga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 02~06 — Garagens | Verga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 02~06 — Garagens | Contraverga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 07 — Lazer | Verga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 07 — Lazer | Contraverga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 08~31 — Tipo (24x) | Verga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] × 24 | Repetir 24 vezes |
| 08~31 — Tipo (24x) | Contraverga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] × 24 | Repetir 24 vezes |
| 32 — Res/Cob | Verga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 32 — Res/Cob | Contraverga | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |

**Total de vergas:** [A CALCULAR] m  
**Total de contravergas:** [A CALCULAR] m

### 3.4 Juntas de Dilatação

| Pavimento | Quantidade (un) | Comprimento Unit. (m) | Comprimento Total (m) | Observação |
|-----------|-----------------|----------------------|----------------------|------------|
| 01 — Térreo | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 02~06 — Garagens | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 07 — Lazer | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |
| 08~31 — Tipo (24x) | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] × 24 | Repetir 24 vezes |
| 32 — Res/Cob | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |

**Total de juntas:** [A CALCULAR] m

### 3.5 Encunhamento (Topo de Paredes)

| Pavimento | Comprimento de Encunhamento (m) | Observação |
|-----------|--------------------------------|------------|
| 01 — Térreo | [A EXTRAIR] | [A EXTRAIR] |
| 02~06 — Garagens | [A EXTRAIR] | [A EXTRAIR] |
| 07 — Lazer | [A EXTRAIR] | [A EXTRAIR] |
| 08~31 — Tipo (24x) | [A EXTRAIR] × 24 | Repetir 24 vezes |
| 32 — Res/Cob | [A EXTRAIR] | [A EXTRAIR] |

**Total de encunhamento:** [A CALCULAR] m

### 3.6 Drywall / Divisórias Leves

| Pavimento | Tipo | Espessura (cm) | Área (m²) | Observação |
|-----------|------|----------------|-----------|------------|
| [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] | [A EXTRAIR] |

**Total de drywall:** [A CALCULAR] m²

---

## 4. Fontes de Dados

### 4.1 Arquivos Processados

**Diretório:** `projetos/thozen-electra/projetos/03 ALVENARIA/`

| Arquivo | Status | Observação |
|---------|--------|------------|
| RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_1B_ TÉRREO LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_2B_G1 LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_03_G2 PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_3B_G2 LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_04_G3 PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_4B_G3 LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_5B_G4 LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_06_G5 PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_6B_G5 LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_7B_ LAZER LOC PRÉ EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |
| RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão (24x) |
| RA_ALV_EXE_8B_ TIPOS LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação (24x) |
| RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Formato DWG — requer conversão |
| RA_ALV_EXE_9B_ RES E COB LOC PRÉ-EXECUTIVO_R01.dwg | ⚠️ NÃO PROCESSADO | Prancha de locação |

**Total:** 18 arquivos DWG (R01)

### 4.2 Documentação de Referência

- `projetos/thozen-electra/PROJETO.md` — Estrutura geral do empreendimento
- `projetos/thozen-electra/projetos/Rubens Alves Lista de arquivos.xlsx` — Índice de arquivos do projeto

---

## 5. Observações e Dados Faltantes

### 5.1 Limitações Técnicas

**⚠️ CRÍTICO — Formato DWG Não Processável:**
- Os arquivos de alvenaria estão em formato **DWG proprietário** (AutoCAD)
- Não há ferramentas de conversão instaladas no ambiente atual:
  - `oda-file-converter` (ODA File Converter) — NÃO disponível
  - `dwg2dxf` — NÃO disponível
  - `teigha` — NÃO disponível
- **Alternativas para processamento:**
  1. **Conversão manual:** Abrir DWG em AutoCAD/BricsCAD e exportar para DXF ou IFC
  2. **Instalação de ODA File Converter:** Ferramenta gratuita da Open Design Alliance
  3. **Upload para processamento online:** Serviços como Autodesk Viewer, A360
  4. **Processamento via API:** Forge API (Autodesk) ou similar

### 5.2 Dados Faltantes Identificados

| Item | Status | Ação Necessária |
|------|--------|----------------|
| **Área de alvenaria por pavimento** | ⚠️ FALTANTE | Processar DWG e extrair polylines/hatch de alvenaria |
| **Tipo de blocos especificados** | ⚠️ FALTANTE | Verificar legendas/texto nas pranchas DWG |
| **Espessura de paredes** | ⚠️ FALTANTE | Verificar cotas e especificações nas pranchas |
| **Quantidade de vergas/contravergas** | ⚠️ FALTANTE | Contar vãos de portas/janelas nas pranchas |
| **Comprimento de vergas/contravergas** | ⚠️ FALTANTE | Medir vãos + acréscimo padrão (30 cm cada lado) |
| **Juntas de dilatação** | ⚠️ FALTANTE | Verificar indicação nas pranchas (símbolo específico) |
| **Encunhamento** | ⚠️ FALTANTE | Calcular perímetro de paredes por pavimento |
| **Drywall/divisórias** | ⚠️ FALTANTE | Verificar se há indicação nas pranchas |
| **Especificações de argamassa** | ⚠️ FALTANTE | Verificar memorial descritivo ou legendas |
| **Altura de pé-direito** | ⚠️ FALTANTE | Cruzar com projeto arquitetônico ou estrutural |

### 5.3 Informações Adicionais Necessárias

#### a) Projeto de Arquitetura
Para complementar a extração de alvenaria, recomenda-se cruzar com:
- **Quadro de áreas** — para validar áreas totais de pavimento
- **Pé-direito** — para calcular área de alvenaria a partir de comprimentos lineares
- **Esquadrias** — para descontar vãos corretamente

Arquivos disponíveis:
- `projetos/thozen-electra/projetos/02 ARQUITETURA/` (DWG + IFC)

#### b) Projeto Estrutural
Para validar interfaces e áreas:
- **Pilares e vigas** — para verificar encontros com alvenaria
- **Lajes** — para validar encunhamento

Arquivos disponíveis:
- `projetos/thozen-electra/projetos/01 ESTRUTURA/` (DWG + IFC)

#### c) Memorial Descritivo
Se disponível, pode conter:
- Especificações de blocos (tipo, resistência, dimensões)
- Especificações de argamassa (traço, resistência)
- Detalhes de execução (vergas, juntas, encunhamento)

**Status:** Não localizado no workspace atual.

### 5.4 Próximos Passos Recomendados

1. **Converter DWG para formato processável:**
   - Opção 1: Instalar ODA File Converter e converter DWG → DXF
   - Opção 2: Solicitar ao time arquivos em DXF ou IFC
   - Opção 3: Processar manualmente em AutoCAD e extrair quantitativos

2. **Extrair dados das pranchas:**
   - Legendas e especificações de blocos
   - Áreas de alvenaria por hatch/polyline
   - Vãos de portas/janelas para vergas/contravergas
   - Juntas de dilatação (se indicadas)

3. **Cruzar com outros projetos:**
   - Arquitetura (pé-direito, esquadrias)
   - Estrutura (pilares, vigas para encunhamento)

4. **Validar quantitativos:**
   - Comparar área total de alvenaria com benchmark (m²/m² de AC)
   - Verificar coerência entre pavimentos similares (tipos)

5. **Gerar planilha executiva:**
   - Estrutura compatível com Memorial Cartesiano
   - N1 09 Alvenaria
   - Subdivisões por tipo de bloco e pavimento

---

## 6. Estrutura do Memorial Cartesiano (Referência)

Este briefing servirá para gerar planilha compatível com:

**N1 09 — ALVENARIA**
- **N2 09.01** — Alvenaria de Vedação
  - **N3 09.01.01** — Blocos Cerâmicos
  - **N3 09.01.02** — Blocos de Concreto
  - **N3 09.01.03** — Blocos de Gesso
- **N2 09.02** — Divisórias
  - **N3 09.02.01** — Drywall
  - **N3 09.02.02** — Divisórias Removíveis
- **N2 09.03** — Elementos Complementares
  - **N3 09.03.01** — Vergas
  - **N3 09.03.02** — Contravergas
  - **N3 09.03.03** — Juntas de Dilatação
  - **N3 09.03.04** — Encunhamento

---

## 7. Changelog

| Data | Revisão | Alteração | Responsável |
|------|---------|-----------|-------------|
| 2026-03-20 | R00 | Briefing inicial — estrutura e dados faltantes identificados | Cartesiano (extração automatizada) |

---

## 8. Anexos

### A. Nomenclatura de Arquivos

**Padrão:** `RA_ALV_EXE_XX_DESCRIÇÃO_R01.dwg`
- `RA` = Rubens Alves (responsável técnico)
- `ALV` = Alvenaria
- `EXE` = Executivo
- `XX` = Número do pavimento (01, 02, ..., 09)
- `XXB` = Prancha de locação (1B, 2B, ..., 9B)
- `R01` = Revisão 01

### B. Mapeamento Pavimento × Arquivo

| Código | Pavimento | Descrição Completa |
|--------|-----------|-------------------|
| 01 | Térreo | 01° Pavimento Térreo |
| 02 | G1 | 02° Pavimento — Garagem 1 |
| 03 | G2 | 03° Pavimento — Garagem 2 |
| 04 | G3 | 04° Pavimento — Garagem 3 |
| 05 | G4 | 05° Pavimento — Garagem 4 |
| 06 | G5 | 06° Pavimento — Garagem 5 |
| 07 | Lazer | 07° Pavimento — Lazer |
| 08 | Tipo | 08° a 31° Pavimentos — Tipo (24 repetições) |
| 09 | Res/Cob | 32° Pavimento — Reservatório e Cobertura |

---

**FIM DO BRIEFING**

---

## Metadados

- **Arquivo:** `executivo/thozen-electra/briefings/alvenaria-r00.md`
- **Formato:** Markdown (compatível com GitHub, VS Code, Obsidian)
- **Encoding:** UTF-8
- **Gerado por:** Cartesiano v1.0 (subagent `extração-alvenaria-electra`)
- **Data de geração:** 2026-03-20 10:33 BRT
