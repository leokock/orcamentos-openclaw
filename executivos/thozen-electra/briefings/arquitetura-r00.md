# Briefing de Arquitetura - Thozen Electra
**Revisão:** R00  
**Data:** 2026-03-20  
**Projeto:** Thozen Electra  
**Disciplina:** Arquitetura (02 ARQUITETURA)

---

## 1. Resumo Executivo

Edifício residencial de **26 pavimentos acima do térreo** (24 pavimentos tipo + cobertura + casa de máquinas + reservatórios), **5 pavimentos de garagem** subsolo, **1 pavimento de lazer** e **térreo comercial/acesso**.

**Estrutura vertical:**
- **Calçada** (cota -77.48m)
- **01-Térreo** (cota 0.52m): Acesso, áreas comerciais, lobby
- **02-Garagem 01** a **06-Garagem 05** (cotas 350.52m a 1540.52m): 5 níveis de estacionamento
- **07-Lazer** (cota 1890.52m): Área de lazer completa
- **1º ao 24º Pavimento Tipo** (cotas 2250.52m a 9702.52m): Apartamentos residenciais
- **09-Cobertura** (cota 10026.52m)
- **10-Casa de Máquinas** (cota 10226.02m)
- **11-Reservatórios** (cota 10456.00m)
- **12-Cobertura Reservatórios** (cota 10656.00m)

**Total de pavimentos modelados:** 36  
**Total de espaços (ambientes):** 838 espaços identificados nos IFCs  
**Esquadrias:** 480 (embasamento) + 4008 (torre tipo) = **4488 unidades** (portas + janelas)

---

## 2. Premissas

### 2.1. Fontes de Dados
- **IFC 1:** `RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc` (34 MB)
  - Pavimentos: Calçada, Térreo, Garagens (5 níveis), Lazer, Cobertura, Casa Máquinas, Reservatórios
  - Espaços: 730 ambientes
  - Esquadrias: 373 portas + 107 janelas
  - Lajes/Pisos: 229 instâncias

- **IFC 2:** `RA_ARQ_EXE_MODELAGEM TIPO_R07.ifc` (76 MB)
  - Pavimentos: 1º ao 24º Pavimento Tipo (repetição)
  - Espaços: 108 ambientes (pavimento tipo)
  - Esquadrias: 2376 portas + 1632 janelas
  - Lajes/Pisos: 2381 instâncias

- **DWGs:** 11 arquivos CAD disponíveis (não processados nesta extração)
  - Térreo, Garagens (G1-G5), Lazer, Tipos, Cortes, Cobertura

### 2.2. Limitações Identificadas
- **⚠️ Áreas dos espaços não exportadas:** Os IFCs não contêm valores de área (IfcSpace.Area = 0.00 m²) — será necessário extrair dos DWGs ou pranchas PDF.
- **⚠️ Quantidades de revestimentos incompletas:** Apenas 17 revestimentos identificados (tipo CEILING), sem áreas calculadas.
- **⚠️ Dimensões de esquadrias não exportadas:** Portas e janelas sem largura/altura no IFC.

### 2.3. Dados Pendentes
1. **Quadro de áreas por pavimento** (AC, UR, NP)
2. **Áreas de revestimentos** por ambiente (pisos, paredes, tetos)
3. **Dimensionamento de esquadrias** (largura x altura)
4. **Especificações de acabamentos** detalhadas por ambiente
5. **Comprimentos de rodapés, soleiras, forros**

---

## 3. Quantitativos Extraídos

### 3.1. Estrutura Vertical - Pavimentos

| Pavimento | Cota (m) | Espaços | Observação |
|-----------|----------|---------|------------|
| Calçada | -77.48 | 0 | Nível externo |
| 01-TÉRREO | 0.52 | 55 | Acesso, comercial, lobby |
| 02-GARAGEM 01 | 350.52 | 123 | Estacionamento subsolo |
| 03-GARAGEM 02 | 647.52 | 122 | Estacionamento subsolo |
| 04-GARAGEM 03 | 945.52 | 123 | Estacionamento subsolo |
| 05-GARAGEM 04 | 1242.52 | 100 | Estacionamento subsolo |
| 06-GARAGEM 05 | 1540.52 | 96 | Estacionamento subsolo |
| 07-LAZER | 1890.52 | 76 | Área de lazer completa |
| 1º PAV TIPO | 2250.52 | 106 | Apartamentos |
| 08-PAVIMENTOS TIPOS (x24) | 2574.52 | 0 | Representação coletiva |
| 3º a 24º PAV TIPO | 2898.52 - 9702.52 | ~106 cada | 22 andares repetidos |
| 09-COBERTURA | 10026.52 | 26 | Cobertura habitável |
| 10-CASA DE MÁQUINAS | 10226.02 | 0 | Equipamentos |
| 11-RESERVATÓRIOS | 10456.00 | 9 | Reserva d'água |
| 12-COB. RESERVATÓRIOS | 10656.00 | 0 | Proteção |

**Total de pavimentos:** 36  
**Altura total estimada:** ~107 metros (da cota -77.48m à cota 10656m)

### 3.2. Espaços por Zona

#### Térreo (55 espaços)
Ambientes identificados (IFC exportou apenas códigos numéricos 757-1353, sem nomes):
- Espaços comerciais
- Lobby de acesso
- Circulações
- Áreas técnicas
- **⚠️ Necessário cruzar com DWG para nomenclatura e áreas**

#### Garagens (564 espaços no total)
- G1: 123 espaços (vagas + circulação + apoio)
- G2: 122 espaços
- G3: 123 espaços
- G4: 100 espaços
- G5: 96 espaços
- **⚠️ Necessário DWG para confirmar número real de vagas**

#### Lazer (76 espaços)
Identificados tipos de piso característicos:
- Piso 10 90x90 Área de lazer (áreas secas)
- Piso 10 Vinílico (áreas de atividades)
- Piso 10 Cimentício (áreas molhadas)
- Piso 10 Pastilha piscina (piscinas)
- Piso 10 Porc. Amadeirado (decks)
- Piso 10 Pedra natural (áreas externas)
- Grama / Grama sintética (áreas verdes)
- Soleira de granito (muretas)
- **⚠️ Necessário DWG para áreas e especificações completas**

#### Pavimento Tipo (106 espaços)
Ambientes identificados (códigos numéricos 1317-1430):
- Apartamentos (estimado: 4 a 6 unidades por andar, dependendo da tipologia)
- Halls de elevadores (2 identificados: Hall dos Aptos)
- Circulações (escadas, corredores)
- Shafts técnicos
- **⚠️ Necessário DWG para planta baixa tipo com áreas e tipologias**

#### Cobertura (26 espaços)
Áreas técnicas, terraços, reservatórios

### 3.3. Revestimentos

#### 3.3.1. Pisos - Tipologias Identificadas

| Código | Tipologia | Aplicação | Observação |
|--------|-----------|-----------|------------|
| Piso 8 | Cimento Pintado | Garagens, áreas técnicas | Pavimento industrial |
| Piso 10 | 60x60 Porcelanato | Áreas comuns garagens | Piso técnico |
| Piso 10 | 90x90 Porcelanato | Salas comerciais, halls, lazer | Piso nobre acabamento |
| Piso 10 | 90x90 Apartamentos | Interiores dos apartamentos | Especificação residencial |
| Piso 10 | 90x90 BWC | Banheiros dos apartamentos | Revestimento cerâmico |
| Piso 10 | Vinílico | Dormitórios dos apartamentos | Piso vinílico |
| Piso 10 | Cimentício | Áreas molhadas lazer | Cimentício impermeável |
| Piso 10 | Pastilha piscina | Piscinas | Pastilha cerâmica |
| Piso 10 | Porc. Amadeirado | Decks lazer | Porcelanato imitação madeira |
| Piso 10 | Pedra natural | Áreas externas lazer | Pedra natural |
| Piso 20 | Cimentício | Sacadas/varandas | Cimentício externo |
| Piso | Grama | Áreas verdes | Grama natural |
| Piso | Grama sintética | Áreas verdes cobertas | Grama sintética |
| Piso | Calçada - Placa cimentícia | Calçadas externas | Concreto aparente |
| Piso | Rampa Garagens | Rampas de acesso garagens | Piso antiderrapante |
| Piso | Rampa/Patamar/Escada Térreo 90x90 | Escadas térreo | Porcelanato 90x90 |
| Piso | Soleira de granito - muretas | Soleiras e muretas | Granito |
| Laje | 10cm | Lajes estruturais | Concreto armado |

**Total de tipologias:** 18  
**⚠️ Áreas não quantificadas no IFC — necessário levantamento em DWG**

#### 3.3.2. Paredes
**⚠️ Revestimentos de parede não exportados no IFC**  
Necessário extrair dos DWGs:
- Azulejos banheiros (altura, área)
- Revestimentos cozinhas
- Pinturas internas
- Texturas externas

#### 3.3.3. Forros
Identificados apenas revestimentos tipo CEILING sem quantificação.  
**⚠️ Necessário DWG para:**
- Forros de gesso
- Forros de PVC
- Lajes aparentes
- Áreas por ambiente

### 3.4. Esquadrias

#### 3.4.1. Resumo por Tipo

| Tipo | IFC Embasamento | IFC Tipo | Total Estimado | Observação |
|------|-----------------|----------|----------------|------------|
| Portas | 373 | 2376 | ~2749 | Inclui portas de madeira, alumínio, elevadores |
| Janelas | 107 | 1632 | ~1739 | Inclui janelas, vidros fixos, basculantes |
| **TOTAL** | **480** | **4008** | **~4488** | 24 pavimentos tipo |

#### 3.4.2. Portas - Tipologias Identificadas

**Embasamento:**
- DALLO-PORTA DE ALUMÍNIO VENEZIANA SEM PEITORIL: PAV 60x210, PAV 80x210
- DALLO-PORTA INTERNA: PM 60x210, PM 80x210, PM 90x210
- DALLO-PORTA DE CORRER DE MADEIRA: PMC 90x210
- DALLO-PORTA DO ELEVADOR: PE 80x210

**Pavimento Tipo:**
- DALLO-PORTA INTERNA: PM 60x210, PM 80x210, PM 90x210
- DALLO-PORTA DE CORRER DE MADEIRA: PMC 90x210
- DALLO-PORTA DE ALUMÍNIO VENEZIANA SEM PEITORIL: PAV 60x210, PAV 80x210

**⚠️ Dimensões não exportadas no IFC — necessário mapa de esquadrias em DWG**

#### 3.4.3. Janelas - Tipologias Identificadas

**Embasamento:**
- VIDRO FIXO: VF 1,20x2,40 / VF 1,30x2,40 / VF 1,70x2,40 / VF 2,00x2,40 / VF 2,35x2,40 / VF 3,00x1,80 / VF 3,00x1,90 / VF 3,00x2,40 / VF 8,55x1,90

**Pavimento Tipo:**
- DALLO-JAN. BASC. 1F S. PERS. ALUM. BRANCO: JA 60x75
- DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO: JA 150x209, JA 170x110

**⚠️ Dimensões não exportadas no IFC — necessário mapa de esquadrias em DWG**

### 3.5. Lajes/Pisos Estruturais

**Total de instâncias de lajes:** 2610 (229 embasamento + 2381 tipo)

Tipologias por pavimento (exemplo):
- **Laje 10cm:** Lajes estruturais de concreto armado
- **Escada moldada no local:** Escadas estruturais

**⚠️ Áreas não quantificadas no IFC**

### 3.6. Rodapés, Soleiras, Pingadeiras
**⚠️ Não identificados no IFC**  
Necessário levantamento em DWG:
- Rodapés por ambiente (material, altura, comprimento)
- Soleiras de portas (material, dimensões)
- Pingadeiras esquadrias (comprimento)

---

## 4. Fontes de Dados

### 4.1. Arquivos Processados
1. `RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc` — Processado via ifcopenshell
2. `RA_ARQ_EXE_MODELAGEM TIPO_R07.ifc` — Processado via ifcopenshell

### 4.2. Arquivos Disponíveis (Não Processados)
Arquivos DWG em `projetos/thozen-electra/projetos/02 ARQUITETURA/DWG/`:
1. `RA_ARQ_EXE_01_TÉRREO_R02.dwg` (4.8 MB)
2. `RA_ARQ_EXE_02_G1_R02.dwg` (4.9 MB)
3. `RA_ARQ_EXE_03_G2_R02.dwg` (4.7 MB)
4. `RA_ARQ_EXE_04_G3_R02.dwg` (4.6 MB)
5. `RA_ARQ_EXE_05_G4_R02.dwg` (5.4 MB)
6. `RA_ARQ_EXE_06_G5_R02.dwg` (4.4 MB)
7. `RA_ARQ_EXE_07_LAZER_R02.dwg` (11 MB)
8. `RA_ARQ_EXE_08_TIPOS_R02.dwg` (5.3 MB)
9. `RA_ARQ_EXE_09_RES E COB_R02.dwg` (695 KB)
10. `RA_ARQ_EXE_10_CORTE1_R02.dwg` (2.3 MB)
11. `RA_ARQ_EXE_11_CORTE2_R02.dwg` (1.3 MB)

**Próxima etapa:** Processar DWGs para extrair quadros de áreas e mapas de esquadrias.

---

## 5. Observações e Recomendações

### 5.1. Dados Faltantes (Críticos)
1. **Quadro de áreas por pavimento**
   - AC (Área Construída)
   - UR (Área Útil Real)
   - NP (Não Pavimentado)
   - Fonte: Extrair de prancha PDF "Quadro de Áreas" ou DWG

2. **Áreas de revestimentos por ambiente**
   - Pisos: m² por tipologia e ambiente
   - Paredes: m² por altura e tipo de revestimento
   - Forros: m² por tipologia
   - Fonte: DWGs de arquitetura executiva

3. **Mapa de esquadrias completo**
   - Código, Dimensões (LxH), Material, Tipo de abertura, Vidro
   - Quantidade por pavimento
   - Fonte: DWG `RA_ARQ_EXE_08_TIPOS_R02.dwg` ou prancha de esquadrias

4. **Especificações de acabamentos**
   - Memória descritiva de acabamentos por ambiente
   - Marcas/modelos de referência
   - Fonte: Memorial descritivo ou caderno de especificações

### 5.2. Inconsistências Identificadas
- **Cotas muito altas:** As cotas dos pavimentos estão em centímetros (ex: cota 350.52m para Garagem 01 deveria ser 3.51m). Verificar se é erro de exportação ou de unidade do IFC.

### 5.3. Próximos Passos
1. **Processar DWGs** com script de extração de textos/blocos para:
   - Quadro de áreas
   - Mapa de esquadrias
   - Tabelas de revestimentos
   
2. **Cruzar dados IFC + DWG** para validar quantidades de ambientes e esquadrias

3. **Gerar planilha executiva** com colunas:
   - Código Memorial | Descrição | UN | QTD | Preço Unit. | Total | Observação
   - Subdividir por N2/N3 do Memorial Cartesiano:
     - **N1 05 Vedações e Esquadrias** (portas, janelas, vidros)
     - **N1 11 Revestimentos** (pisos, paredes, tetos)
     - **N1 12 Pinturas** (paredes internas/externas)

4. **Solicitar informações adicionais** ao time:
   - Prancha com quadro de áreas oficial
   - Memorial descritivo de acabamentos
   - Especificações técnicas de esquadrias

---

## 6. Sumário de Quantitativos

| Item | Quantidade | Unidade | Observação |
|------|------------|---------|------------|
| Pavimentos totais | 36 | un | Incluindo subsolos, tipo, cobertura |
| Pavimentos tipo | 24 | un | 1º ao 24º andar |
| Espaços/Ambientes | 838 | un | Total identificado nos IFCs |
| Portas | ~2749 | un | Estimado (373 emb + 2376 tipo) |
| Janelas | ~1739 | un | Estimado (107 emb + 1632 tipo) |
| Lajes/Pisos | 2610 | un | Instâncias de piso estrutural |
| Tipologias de piso | 18 | un | Acabamentos diferentes |
| Área total construída | **⚠️ PENDENTE** | m² | Necessário quadro de áreas |
| Área de revestimentos | **⚠️ PENDENTE** | m² | Necessário DWG |
| Comprimento rodapés | **⚠️ PENDENTE** | m | Necessário DWG |
| Comprimento soleiras | **⚠️ PENDENTE** | m | Necessário DWG |

---

**Gerado por:** Cartesiano (Subagente: extração-arquitetura-electra)  
**Método:** Processamento de IFC via ifcopenshell  
**Status:** Parcial — Aguardando processamento de DWGs para complementar dados
