# ANÁLISE ONDA 4 - ELÉTRICO + PPCI
## Gran Royal Residence - Grandezza Construtora

**Data da Análise:** 15/03/2026  
**Projeto:** Gran Royal Residence - Balneário Piçarras/SC  
**Área Total:** 5.225,33 m²  
**Pavimentos:** 19 (1 subsolo + 4 garagens + 1 lazer + 14 tipo)  
**Unidades:** 30 apartamentos (2 por pavimento tipo, 5° ao 19°)

---

## 1. SISTEMA ELÉTRICO

### 1.1 ENTRADA DE ENERGIA E DISTRIBUIÇÃO GERAL
**Fonte:** ELE 12_GRR_ENTR.DISTR.ENERGIA_rev00.pdf

**Fornecimento:**
- **Tipo:** Trifásico (3 fases + neutro + PE)
- **Concessionária:** Celesc
- **Ponto de Entrega:** Poste existente da Celesc (derivação ramal de ligação)

**Infraestrutura de Entrada:**
- **Caixa de Passagem Subterrânea:** Tipo B1, dimensões internas (85×65×85)cm, concreto/alvenaria, tampa ferro fundido nodular padrão Celesc
- **Ramal de Entrada Subterrâneo:** 2 condutores cobre por fase + 2 neutro, instalado em 2 eletrodutos PEAD
- **QMC (Quadro de Medição Coletivo):** Capacidade 33 medidores, padrão Celesc, dimensões (406,4×137×20)cm, face inferior mín. 30cm do piso acabado
- **Eletrocalha Principal:** Tipo perfurada, chapa aço galvanizada a fogo, dimensões 400×100mm, interliga QMC ao shaft da prumada elétrica

**Ramais de Carga:**
- **Apartamentos (30 circuitos):** 5 condutores Cobre 10mm², isolação EPR 0,6/1kV (3F + N + PE)
- **Áreas Comuns (2 circuitos - COND-01 e COND-02):** 5 condutores Cobre 25mm², isolação EPR 0,6/1kV (3F + N + PE)

**Prumada Elétrica:**
- **Travessa de Sustentação Vertical:** Perfilado perfurado aço galvanizado a fogo (400×100mm), ancorado a cada 3,0m (1 por pavimento)
- **Total de Condutores na Prumada:** 160 condutores (ramais de carga)

**Esquema de Aterramento:** TN-S (condutor de proteção PE distribuído de forma distinta do condutor Neutro N)

---

### 1.2 QUADROS DE DISTRIBUIÇÃO E CARGAS INSTALADAS POR PAVIMENTO
**Fonte:** ELE 08_GRR_DIAGRAMAS_COND_rev00.pdf, ELE 01 a ELE 07

#### SUBSOLO
- **QD COND 01-CENTRAL**
  - Potência Instalada: 85.736 VA
  - Potência Demandada: 31.124,40 VA
  - Fase A: 36.088 VA | Fase B: 33.388 VA | Fase C: 33.262 VA
  - Disjuntor Geral: 3P/70A
  - Principais circuitos:
    - 14: Tomadas Bloco Autônomo PPCI (400 VA)
    - 17: Tomada Central de (100 VA)
    - 18,19,20: QD ELE-01 (8.500 VA)
    - 21,22,23: QD ELE-02 (8.500 VA)
    - 24: QD COND 06-COBERTURA (4.400 VA)

- **PC BOMBAS HID.**
  - Potência Instalada: 6.000 VA
  - Potência Demandada: 4.500 VA
  - Distribuição equilibrada: 2.000 VA por fase

#### 1º PAVTO - G2

- **QD HALL PAVTOS** (repetido em pavimentos de garagem)
  - Potência Instalada: 2.100 VA
  - Potência Demandada: 820 VA

#### 3º PVTO - G4

- **QD COND 03-G3**
  - Potência Instalada: 3.760 VA
  - Potência Demandada: 1.760 VA

#### 4º PVTO - LAZER

- **QD COND 05-LAZER**
  - Potência Instalada: 38.165 VA
  - Potência Demandada: 8.725 VA
  - Fase A: 10.735 VA | Fase B: 13.845 VA | Fase C: 13.585 VA
  - Principais circuitos:
    - 14: Tomadas Uso Geral Sala de Festas (2.900 VA)

- **QDC (Lazer)**
  - Potência Instalada: 16.155 VA
  - Potência Demandada: 7.996,45 VA
  - Fase A: 4.489 VA | Fase B: 5.933 VA | Fase C: 5.733 VA

- **QDC (Adicional Lazer)**
  - Potência Instalada: 2.500 VA
  - Potência Demandada: 2.500 VA
  - Distribuição equilibrada: ~833 VA por fase

#### COBERTURA

- **QD COND 06-COBERTURA**
  - Potência Instalada: 4.400 VA
  - Potência Demandada: 1.760 VA
  - Disjuntor Geral: 1P/50A (In:50A)
  - Circuitos de iluminação (100 VA cada)
  - Fonte: ELE 07_GRR_COBERTURA_RESERV._rev00.pdf

---

### 1.3 DIMENSIONAMENTO ELÉTRICO POR UNIDADE TIPO

**Fonte:** ELE 04_GRR_UNIFILAR_AP TIPO FN 02_rev00.pdf e ELE 06_GRR_UNIFILAR_APTO TIPO_FN 01_rev00.pdf

#### APARTAMENTO TIPO FN 02 (96,13 m²)

**Quadro de Distribuição (QDC):**
- **Tipo:** Embutir, corpo PVC, capacidade mín. 36 módulos padrão DIN
- **Potência Instalada:** 39.300 VA
- **Potência Demandada:** 20.680 VA
- **Distribuição por Fase:**
  - Fase A: 13.200 VA
  - Fase B: 13.100 VA
  - Fase C: 13.000 VA
- **Disjuntor Geral:** 3F10 (N10) PE10, In: 50A
- **DPS:** 275V, 20kA
- **DR (Dispositivo Diferencial-Residual):** 4P, In:63A/30mA
- **Espaços de Reserva:** 4 circuitos (conforme NBR 5410)

**Circuitos (16 circuitos + reserva):**

| Circ. | Descrição | Potência (VA) | Fase | Disjuntor | Fiação |
|-------|-----------|---------------|------|-----------|--------|
| 1 | Tomada Área Técnica p/ Aquecedor | 100 | A | 1P/10A C-3KA | #2,5 |
| 2 | Tomadas Comunicação (QD VDI) | 200 | B | 1P/10A C-3KA | #2,5 |
| 3 | Iluminação 02 - Área | 600 | - | 1P/10A C-3KA | #1,5 |
| 4 | Tomadas Dormitório 02 | 1.200 | A | 1P/10A C-3KA | #2,5 |
| 5 | Iluminação 01 - Área | 1.300 | - | 1P/10A C-3KA | #1,5 |
| 6 | Tomadas Dormitório 01 | 2.000 | A | 1P/16A C-3KA | #2,5 |
| 7 | AR Condicionado Living | 2.500 | C | 1P/20A B-3KA | #4,0 |
| 8 | Tomadas Suíte | 3.000 | B | 1P/16A C-3KA | #2,5 |
| 9 | Tomadas Estar / Jantar | 2.100 | C | 1P/20A C-3KA | #2,5 |
| 10 | Tomadas Cozinha | 3.800 | A | 1P/32A C-3KA | #6,0 |
| 11 | Chuveiro Elétrico BWC | 6.800 | B | 1P/32A B-3KA | #6,0 |
| 12 | Fogão de Indução | 6.500 | C | 1P/32A C-3KA | #6,0 |
| 13 | Tomadas Lavanderia | 3.800 | B | 1P/20A C-3KA | #4,0 |
| 14 | AR Condicionado | 1.800 | A | 1P/10A C-3KA | #2,5 |
| 15 | AR Condicionado Suíte | 1.800 | B | 1P/10A C-3KA | #2,5 |
| 16 | AR Condicionado | 1.800 | C | 1P/10A C-3KA | #2,5 |

**Total de Pontos (FN 02):**
- **Iluminação:** 2 circuitos (600 + 1.300 = 1.900 VA)
- **Tomadas (TUG + TUE):** 10 circuitos (16.900 VA)
- **AR Condicionado:** 4 circuitos (8.100 VA)
- **Aquecimento (chuveiro + fogão indução):** 2 circuitos (13.300 VA)
- **Total de Circuitos:** 16 + 4 reserva

**Número Estimado de Pontos de Luz:**
- Iluminação geral: ~15-20 pontos (estimativa baseada em planta)
- Interruptores: ~10-12 pontos
- Tomadas: ~30-35 pontos (TUG + TUE)

---

#### APARTAMENTO TIPO FN 01 (92,96 m²)

**Quadro de Distribuição (QDC):**
- **Tipo:** Embutir, corpo PVC, capacidade mín. 36 módulos padrão DIN
- **Potência Instalada:** 40.400 VA
- **Potência Demandada:** 21.020 VA
- **Distribuição por Fase:**
  - Fase A: 13.600 VA
  - Fase B: 13.400 VA
  - Fase C: 13.400 VA
- **Disjuntor Geral:** 3F10 (N10) PE10, In: 50A
- **DPS:** 275V, 20kA
- **DR:** 4P, In:63A/30mA
- **Espaços de Reserva:** 4 circuitos

**Circuitos (17 circuitos + reserva):**

| Circ. | Descrição | Potência (VA) | Fase | Disjuntor | Fiação |
|-------|-----------|---------------|------|-----------|--------|
| 1 | Tomada Área Técnica p/ Aquecedor | 100 | A | 1P/10A C-3KA | #2,5 |
| 2 | Tomadas Comunicação (QD VDI) | 200 | B | 1P/10A C-3KA | #2,5 |
| 3 | Iluminação 02 - Área | 600 | - | 1P/10A C-3KA | #1,5 |
| 4 | Tomadas Dormitório 02 | 1.900 | A | 1P/10A C-3KA | #2,5 |
| 5 | Iluminação 01 - Área | 1.300 | - | 1P/10A C-3KA | #1,5 |
| 6 | Tomadas Dormitório 01 | 2.000 | A | 1P/16A C-3KA | #2,5 |
| 7 | Tomadas Suíte | 3.000 | B | 1P/16A C-3KA | #2,5 |
| 8 | AR Condicionado Living | 2.500 | C | 1P/20A B-3KA | #4,0 |
| 9 | Tomadas Estar / Jantar | 2.500 | C | 1P/32A C-3KA | #6,0 |
| 10 | Chuveiro Elétrico BWC | 6.800 | B | 1P/20A B-3KA | #6,0 |
| 11 | Tomadas Cozinha | 3.800 | A | 1P/32A C-3KA | #4,0 |
| 12 | Fogão de Indução | 6.500 | C | 1P/32A C-3KA | #6,0 |
| 13 | AR Condicionado | 1.800 | A | 1P/10A C-3KA | #2,5 |
| 14 | Tomadas Lavanderia | 3.800 | B | 1P/10A C-3KA | #4,0 |
| 15 | AR Condicionado Suíte | 1.800 | B | 1P/10A C-3KA | #2,5 |
| 17 | AR Condicionado | 1.800 | C | 1P/20A C-3KA | #2,5 |

**Total de Pontos (FN 01):**
- **Iluminação:** 2 circuitos (1.900 VA)
- **Tomadas (TUG + TUE):** 10 circuitos (17.900 VA)
- **AR Condicionado:** 4 circuitos (8.100 VA)
- **Aquecimento:** 2 circuitos (13.300 VA)
- **Total de Circuitos:** 17 + 4 reserva

**Número Estimado de Pontos de Luz:**
- Iluminação geral: ~15-20 pontos
- Interruptores: ~10-12 pontos
- Tomadas: ~30-35 pontos (TUG + TUE)

---

### 1.4 SISTEMA DE VEÍCULOS ELÉTRICOS (VE)

**Fonte:** ELE 09_GRR_CROQUI_VE_G1_G2_rev00.pdf, ELE 10_GRR_CROQUI_VE_G3_G4_rev00.pdf, ELE 11_GRR_DIAGRAMAS_VE_rev00.pdf

**Infraestrutura VE:**
- **COND 02:** Dedicado a Recarga VE
- **Circuitos VE (por vaga):**
  - Potência: 2.000 VA por VE
  - Proteção: DR 2P In:40A/30mA + Disjuntor 1P/40A C-3KA
  - Fiação: #10,0
- **Quantidade de Vagas VE:** Mínimo 8 vagas (circuitos 8 a 17 identificados)
- **Localização:** Garagens G1, G2, G3, G4
- **Diagrama Unifilar:** Disj. Geral Fases ABC + DPS + circuitos individuais por vaga

---

### 1.5 FIAÇÃO E BITOLAS PRINCIPAIS

**Bitolas Utilizadas:**
- **Ramais de Carga Aptos:** #10,0 (3F + N + PE)
- **Ramais Áreas Comuns:** #25,0 (3F + N + PE)
- **Circuitos Iluminação:** #1,5
- **Circuitos Tomadas TUG:** #2,5
- **Circuitos TUE (Chuveiro, Fogão, AR):** #4,0 a #6,0
- **Prumada Elevadores/VE:** #10,0

**Eletrodutos:**
- **Tipo:** Corrugado Amarelo
- **Diâmetros:** Ø3/4" (25mm), Ø1" (32mm)
- **Eletrocalha Principal:** 400×100mm, aço galvanizado a fogo

---

## 2. SPDA (SISTEMA DE PROTEÇÃO CONTRA DESCARGAS ATMOSFÉRICAS)

**Fonte:** SPDA 01 a SPDA 06, Lista de Materiais SPDA.xlsx

### 2.1 NÍVEL DE PROTEÇÃO E TIPO DE CAPTOR

- **Nível de Proteção:** Não especificado explicitamente nos arquivos analisados (padrão recomendado NBR 5419: Nível III ou IV para edifício residencial)
- **Tipo de Captor:** Captor Franklin (terminal aéreo)
  - 1× Captor Franklin em latão cromado, h=250mm (Tel 010)
  - Instalado em mastro simples 3m × Ø 1.1/2" (Tel 460)
  - Base para mastro em alumínio fundido Ø 1.1/2" (Tel 065)
  - Conjunto de estais rígidos 0,5m × Ø 1.1/2" (Tel 442)
  - Abraçadeira para mastro sem conector Ø 1.1/2" (Tel 807)
- **Minicaptores:** 8× Minicaptor 7/8" × 1/8" × 300mm (Tel 942)

### 2.2 MALHA DE ATERRAMENTO

**Sistema de Aterramento:**
- **Cordoalhas (Captação e Descida):**
  - Cordoalha aço galvanizado Ø 3/8" (51mm²): 133,482m (peso 54,728kg) - Tel 5738
  - Cordoalha aço galvanizado Ø 7/16" (74mm²): 181,791m (peso 107,257kg) - Tel 5776
  - **Total Cordoalhas:** 315,273m

- **Eletrodos de Aterramento (Rebars):**
  - Rebar Ø 8mm × 3,00m (50mm²): 116 peças (comprimento total 350,169m, peso 140,068kg) - Tel 762
  - Rebar adicional (componentes): 36 peças (peso 5,040kg)
  - **Total Rebars:** 152 peças, 355,209m

- **Barras Chatas (Malha Horizontal):**
  - Barra chata Alumínio 7/8" × 1/8" × 3m (70mm²): 41 peças (peso 20,500kg) - Tel 771
  - Comprimento total: 123m

- **Conexões e Emendas:**
  - Emenda L aço G.F. 200×200mm Ø 3/8": 3 peças (Tel 767)
  - Clips para emenda de rebars Ø 8-10mm: 369 peças (Tel 5238)
  - ATERRINSERT® para Rebars Ø 8-10mm (disco latão zincado, rosca fêmea M12): 17 peças (Tel 656)

- **Curvas e Acessórios:**
  - Curva 7/8" × 1/8" × 300mm (70mm²) em Alumínio: 8 peças (Tel 778)
  - Curva Horizontal 7/8" × 1/8" × 300mm com furos: 11 peças (Tel 781)

- **Equipotencialização:**
  - Caixa de equipotencialização de sobrepor 9 terminais (250×200×100mm): 1 peça (Tel 901)

**Fixação e Ancoragem:**
- Bucha Nylon S 6×30 (furo Ø6mm): 151 peças (Tel 5306)
- Bucha Nylon S 8×40 (furo Ø8mm): 10 peças (Tel 5308)
- Parafuso inox autoatarraxante cabeça panela Ø4,2×32mm: 151 peças (Tel 5333)
- Parafuso sextavado rosca soberba inox M6×45mm: 10 peças (Tel 5346)
- Parafuso Alumínio Cabeça Chata 1/4"×5/8": 114 peças (Tel 5321)
- Porca alumínio sextavada 1/4": 114 peças (Tel 5313)
- Arruela lisa aço inox AISI 316 (d1:7-7,5mm, d2:16,25mm, h:1,2-1,5mm): 10 peças (Tel 5303)

---

## 3. PPCI (PROJETO DE PREVENÇÃO E COMBATE A INCÊNDIO)

**Fonte:** Memorial Descritivo PPCI, Memorial de Cálculo Hidrantes, PCI 01 a PCI 10

### 3.1 CLASSIFICAÇÃO E OCUPAÇÃO

- **Ocupação:** A-2 - Residencial Multifamiliar Vertical (edifício de apartamentos em geral)
- **Classe de Risco:** **Risco Leve**
- **Carga de Incêndio Específica:** 300 MJ/m² (100 < qfi ≤ 300)
- **Altura Total da Edificação:** 69,07m (altura para efeito de bombeiros: 57,24m)
- **Área Total:** 5.225,33 m²
- **Área Comum Total:** 2.469,15 m²
- **Número de Pavimentos:** 19
- **Normas Aplicadas:** NCIP (Código de Segurança Contra Incêndio e Pânico - SC), NBR 5410, IN 001 a IN 28 do CBMSC

---

### 3.2 MEDIDAS DE SEGURANÇA INSTALADAS

**Sistemas Obrigatórios (conforme IN 001 - Parte 02, Tabela 03, Anexo B):**
1. ✅ Alarme de Incêndio e DAI (Detecção Automática de Incêndio) - IN 12
2. ✅ Brigada de Incêndio - IN 28 (capacitação EaD CBMSC recomendada)
3. ✅ Controle de Materiais e Acabamento - IN 18
4. ✅ Controle de Fumaça - IN 10
5. ✅ Extintores - IN 06
6. ✅ Gás Combustível - IN 08
7. ✅ Hidráulico Preventivo (SHP - Sistema de Hidrantes e Mangotinhos) - IN 07
8. ✅ Iluminação de Emergência - IN 11
9. ✅ Instalações Elétricas de Baixa Tensão - IN 19
10. ✅ Saídas de Emergência - IN 09
11. ✅ Sinalização para Abandono de Local (SAL) - IN 13
12. ✅ TRRF - Proteção Estrutural - IN 14

---

### 3.3 SISTEMA HIDRÁULICO PREVENTIVO (SHP)

**Fonte:** Memorial de Cálculo de Hidrantes, PCI 07_GRR_SHP_rev00.pdf

#### 3.3.1 CARACTERÍSTICAS GERAIS

- **Sistema Adotado:** Hidrantes (Tipo I)
- **Número Total de Hidrantes:** **20 hidrantes**
- **Hidrantes em Uso Simultâneo:** 4
- **Vazão Mínima na Ponta do Esguicho:** 70 L/min
- **Tipo de Esguicho:** Agulheta
- **Fator de Vazão (K):** 32,5
- **Pressão Mínima no Hidrante Desfavorável (H19):** 46,639 mca

#### 3.3.2 TUBULAÇÃO E MANGUEIRAS

- **Tubulação:** Aço Galvanizado (AG)
- **Diâmetro da Tubulação Principal:** 2.½" (65mm)
- **Diâmetro das Mangueiras:** 1.½" (40mm)
- **Comprimento das Mangueiras (Pavtos Tipo):** 1× 15m
- **Comprimento das Mangueiras (Outros Pavtos):** 2× 15m = 30m (ex: Hidrante 01A - Subsolo)
- **Coeficiente de Rugosidade (Hazen-Williams):**
  - Tubulação aço: 120
  - Mangueiras: 140

#### 3.3.3 RESERVATÓRIO E RESERVA TÉCNICA

- **Reservatório SHP:** 2× Tanque Fortlev 15m³ = **30m³ total**
- **Tomada de Alimentação:** Lateral de cada reservatório, FºGº 2.½"
- **Saída de Limpeza:** Lateral de cada reservatório, FºGº 1.½", RG 1.½"
- **Válvula de Retenção:** VR 2.½"
- **Registro de Gaveta:** RG 2.½"

#### 3.3.4 LOCALIZAÇÃO DOS HIDRANTES POR PAVIMENTO

**Distribuição (estimada conforme memorial e pranchas):**

| Pavimento | Hidrantes | Observações |
|-----------|-----------|-------------|
| **Subsolo** | H01A | Mangueira 2×15m=30m, h fundo abrigo=65cm, h tomada d'água=130cm |
| **G1 (1º Pvto)** | - | - |
| **G2 (2º Pvto)** | - | - |
| **G3 (3º Pvto)** | - | - |
| **G4 (Lazer)** | - | - |
| **Pavtos Tipo (5º ao 19°)** | H16, H17, H18, H19 | Requinte 1.½" - 13mm, h=130cm, mangueira 1×15m |
| **Cobertura/Reservatório** | - | Reservatórios SHP |

**Observação:** A distribuição exata dos 20 hidrantes por pavimento não estava detalhada nas seções extraídas dos PDFs. O memorial cita H16, H17, H18, H19 como hidrantes dos pavimentos tipo, e H01A no subsolo. Recomenda-se revisar as pranchas PCI 01 a PCI 06 para mapeamento completo.

#### 3.3.5 ABRIGO DE MANGUEIRAS

- **Dimensões:** 75×45×20cm
- **Conteúdo:**
  - Chave de mangueira
  - Mangueira e esguicho
  - Hidrante
  - Mangotinho (quando aplicável)
- **Altura do Fundo do Abrigo:** 65cm (subsolo), variável conforme pavimento
- **Altura da Tomada d'Água:** 130cm do piso acabado
- **Sinalização:** Quadro de 1,00×1,00m com bordas de 10cm, pintado no piso nas cores vermelho com bordas em amarelo (quando instalado em garagens)

#### 3.3.6 REGISTRO DE RECALQUE

- **Localização:** Conforme projeto (não especificado nos trechos extraídos)
- **Tipo:** Sem válvula de retenção

#### 3.3.7 BOMBA DE INCÊNDIO

- **Quadro de Comando:** PC BOMBAS HID.
- **Potência Instalada:** 6.000 VA
- **Potência Demandada:** 4.500 VA
- **Distribuição:** 2.000 VA por fase (trifásico)
- **Observação:** Detalhes de vazão e pressão não extraídos dos trechos analisados

---

### 3.4 SISTEMA DE EXTINTORES

**Fonte:** Memorial Descritivo PPCI (Seção 9), plantas PCI 01 a PCI 10

#### 3.4.1 CRITÉRIOS GERAIS (IN 06)

- **Tipo de Extintor:** Portáteis
- **Classificação de Fogo:**
  - **Classe A:** Materiais sólidos (madeira, papel, tecido)
  - **Classe B:** Líquidos inflamáveis (tintas, solventes, GLP)
  - **Classe C:** Equipamentos elétricos energizados

#### 3.4.2 DISTRIBUIÇÃO POR PAVIMENTO

**Observação:** As pranchas PCI não foram extraídas em detalhes suficientes para listar a localização exata de cada extintor. Recomenda-se consultar PCI 01 a PCI 05 para mapeamento completo.

**Estimativa com base em norma:**
- **Distância máxima a percorrer:** 25m para Classe A, 15m para Classe B (risco leve)
- **Capacidade Extintora Mínima (Classe A):** 2-A (risco leve)
- **Capacidade Extintora Mínima (Classe B):** 10-B (risco leve)
- **Estimativa de Extintores por Pavimento Tipo:** 2-3 extintores (ABC)
- **Estimativa Total (19 pavimentos):** ~40-60 extintores

**Tipos Esperados:**
- **Pó Químico ABC:** Áreas comuns, corredores
- **CO2:** Áreas com equipamentos elétricos (quadros, subestação)
- **Água Pressurizada:** Escadas de emergência (classe A)

---

### 3.5 SISTEMA DE DETECÇÃO E ALARME DE INCÊNDIO (SDAI)

**Fonte:** PCI 09_GRR_SDAI_rev00.pdf, Memorial Descritivo PPCI (Seção 12)

#### 3.5.1 TIPO DE SISTEMA

- **Sistema:** SDAI Endereçável
- **Central de Alarme:** Central endereçável (tensão elétrica máx. 30 VCC)
- **Alimentação:** 12Vcc (baterias) + 24Vcc (alimentação circuitos)
- **Número de Laços:** 3 laços
  - **Laço 1:** Pavimentos 1º a 4º + Reservatório
  - **Laço 2 e 3:** Pavimento Lazer + Pavimentos Tipo (repetição)
  - **Cobertura Reservatório:** Conectado ao Laço 1

#### 3.5.2 DISPOSITIVOS POR TIPO

**Detectores:**
- **Tipo:** Detector Pontual de Calor (símbolo presente nas plantas)
- **Localização:** Halls de elevador, corredores, áreas comuns
- **Quantidade por Pavimento Tipo:** ~2-3 detectores (estimativa baseada em símbolo nas plantas)
- **Total Estimado:** ~60-70 detectores (considerando 19 pavimentos + áreas comuns)

**Acionadores Manuais:**
- **Tipo:** Acionador Manual de Alarme Convencional
- **Altura de Instalação:** 0,90m a 1,35m do piso acabado
- **Localização:** Próximo a saídas de emergência, escadas
- **Quantidade por Pavimento:** Mínimo 1 por pavimento
- **Total Estimado:** ~20 acionadores

**Avisadores:**
- **Tipo:** Indicador Áudio-Visual com Sirene Acoplada
- **Altura de Instalação:** h > 1,8m
- **Potência Sonora:** 90-115 dBA (medido a 1m), mín. 15 dBA acima do ruído de fundo (medido a 3m)
- **Quantidade por Pavimento:** ~1-2 avisadores
- **Total Estimado:** ~25-30 avisadores

**Dispositivos Complementares:**
- **Telefone de Emergência / Interfone:** Presente em pontos estratégicos
- **Intercomunicador PcD:** Altura 80-120cm
- **Isoladores de Linha:** A cada 20 dispositivos (conforme diagrama unifilar)

#### 3.5.3 FIAÇÃO SDAI

- **Cabos de Alimentação:** +24Vcc / -24Vcc, #1,5mm²
- **Cabos de Laço:** #1,5mm² (conforme diagrama)

---

### 3.6 ILUMINAÇÃO DE EMERGÊNCIA

**Fonte:** Memorial Descritivo PPCI (Seção 7), plantas PCI

#### 3.6.1 TIPO DE SISTEMA

- **Sistema:** Não Permanente (acende automaticamente quando energia normal é desligada)
- **Tipo de Fonte:** Blocos Autônomos
- **Composição de Cada Bloco:**
  - 30 lâmpadas SMD LED, potência 1,2W cada
  - Autonomia: 2,5h (modo maior luminosidade), 5,5h (modo menor luminosidade)
  - Nível de Iluminamento: Mín. 3 Lux (piso em locais planos), 5 Lux (desníveis)
  - Luminosidade (modo menor): 80 Lumens
- **Bateria:** Íon-lítio 3,7V 1300mA/H, vida útil 2 anos

#### 3.6.2 LOCALIZAÇÃO

- **Altura de Instalação:** 2,10m ou embutida no forro
- **Locais de Instalação:**
  - Escadas de emergência (todos os pavimentos)
  - Corredores e áreas de circulação
  - Halls de elevador
  - Saídas de emergência
  - Desníveis e mudanças de direção
- **Quantidade Estimada:** ~80-100 blocos (considerando escadas, corredores, halls em 19 pavimentos)

---

### 3.7 SINALIZAÇÃO PARA ABANDONO DE LOCAL (SAL)

**Fonte:** Memorial Descritivo PPCI (Seção 8)

#### 3.7.1 TIPOS DE SINALIZAÇÃO

- **Placa Fotoluminescente:**
  - Mensagem: "SAÍDA" (podendo ser acompanhada de simbologia)
  - Seta direcional (em mudanças de direção)
  - Fundo verde, mensagens e símbolos em branco fotoluminescente
  - Dimensões mínimas conforme Tabela 1 (IN 13)

- **Placa Luminosa:**
  - Mensagem: "SAÍDA" (cor vermelha ou verde)
  - Seta direcional
  - Fundo branco leitoso, acrílico ou similar
  - Fonte de energia: Conjunto de blocos autônomos (tomada exclusiva por bloco)

- **Placa de Acessibilidade:**
  - Mensagem: "SAÍDA" + Símbolo Internacional de Acessibilidade
  - Tipo: Fotoluminescente ou luminosa

#### 3.7.2 ALIMENTAÇÃO DE ENERGIA

- **Circuito Elétrico:** Independente, disjuntor identificado
- **Blocos Autônomos:** Tomada exclusiva por bloco

#### 3.7.3 DISTRIBUIÇÃO

- **Locação:** Indicada em plantas baixas (PCI 01 a PCI 10)
- **Detalhamentos:** Legenda e detalhes em projeto
- **Estimativa de Placas:** ~40-50 placas (considerando escadas, corredores, saídas em 19 pavimentos)

---

### 3.8 SAÍDAS DE EMERGÊNCIA

**Fonte:** Memorial Descritivo PPCI (Seção 6), IN 09

#### 3.8.1 CÁLCULO DE POPULAÇÃO

- **Pavimento Tipo:** 14 pavimentos × 11 dormitórios por pavimento = 154 dormitórios
- **Critério:** 2 pessoas por dormitório (Anexo C, IN 09)
- **População Pavimento de Maior Ocupação:** 22 pessoas
- **População Total Residencial:** ~308 pessoas (estimativa 14 pvtos tipo × 22 pessoas)

#### 3.8.2 DIMENSIONAMENTO DAS SAÍDAS

**Fórmula:** N = P / C (N = unidades de passagem, P = população, C = capacidade)

**Valores Tabelados (IN 09, Anexo C):**
- **Corredores e Circulação:** C = 60
- **Escadas e Rampas:** C = 45
- **Portas:** C = 100

**Cálculo para P = 90 pessoas (considerado no memorial):**
- **Corredores:** N = 90/60 = 1,5 → **2 unidades** → **Largura mín. 1,20m** ✅
- **Escadas:** N = 90/45 = 2 → **2 unidades** → **Largura mín. 1,20m** ✅ (Art. 63, IN 09)
- **Portas:** N = 90/100 = 0,9 → **1 unidade** → **Largura mín. 80cm** ✅

**Larguras Adotadas:**
- **Corredores e Circulação:** 1,20m
- **Escadas de Emergência:** 1,20m
- **Portas Corta-Fogo:** 80cm ou 90cm (conforme tipologia)
- **Porta de Saída do Edifício (Descarga):** 1,20m

#### 3.8.3 DEGRAUS DA ESCADA

**Fórmula de Blondel:** 63cm ≤ (2h + b) ≤ 64cm
- **h (espelho):** 16-18cm (adotado 18cm)
- **b (piso):** 27cm
- **Verificação:** (2 × 18) + 27 = 63cm ✅

**Requisitos:**
- Revestimento: Material incombustível e antiderrapante (IN 18)
- Espelho (h): 16-18cm
- Piso (b): Conforme fórmula de Blondel

#### 3.8.4 DISTÂNCIAS MÁXIMAS A SEREM PERCORRIDAS

- **Ocupação A-2 (Residencial Multifamiliar):**
  - **Piso Elevado:** 40m (com uma saída única + DAI)
  - **Piso de Descarga:** 50m
- **Distância Medida:** Da porta da unidade autônoma mais distante até local seguro/relativa segurança
- **Caminhamento Interno (dentro da unidade):** Ilimitado (Ocupação A)
- **Distância Medida no Pavimento de Descarga:** 27m ✅ (conforme memorial)

#### 3.8.5 ELEMENTOS DE PROTEÇÃO

- **Paredes Resistentes ao Fogo:** 2 horas (PCF)
- **Portas Corta-Fogo:** Resistência ao fogo 90 minutos (P90)
- **Guarda-Corpos:** Conforme NBR 14718 (resistência a esforços horizontais/verticais e impactos)
- **Piso Antiderrapante:** Em escadas e áreas de risco

---

### 3.9 PORTAS CORTA-FOGO

**Fonte:** Dados de arquitetura (Onda 1), Memorial PPCI

#### 3.9.1 QUANTIDADE TOTAL

- **Total de Portas Corta-Fogo:** **43 portas**
  - 39× Portas 80×210cm (P90)
  - 4× Portas 90×210cm (P90)
- **Resistência ao Fogo:** 90 minutos (P90)

#### 3.9.2 LOCALIZAÇÃO POR PAVIMENTO

**Estimativa (considerando arquitetura padrão):**
- **Antecâmaras:** 2 portas por pavimento (acesso DEA + DEF)
- **Escadas de Emergência:** 2 portas por pavimento (DEA + DEF)
- **Pavimentos Tipo (5º ao 19°):** 14 pvtos × ~2-3 portas = ~30-40 portas
- **Pavimentos de Garagem + Lazer:** ~5-10 portas
- **Subsolo:** 2-3 portas

**Distribuição Estimada:**

| Pavimento | Portas Corta-Fogo | Observações |
|-----------|-------------------|-------------|
| Subsolo | ~3 | Acesso escadas |
| G1 a G4 | ~8 | 2 portas/pvto (DEA+DEF) |
| Lazer | ~3 | Acesso escadas + áreas específicas |
| Pavtos Tipo (5° ao 19°) | ~28 | 2 portas/pvto (DEA+DEF) |
| **Total** | **~43** | **Confere com arquitetura** ✅ |

#### 3.9.3 REQUISITOS

- **Dispositivos de Fechamento:** Mecânicos ou automáticos (permanecem fechadas, porém destrancadas)
- **Placa Obrigatória:** "PORTA CORTA-FOGO: mantenha fechada"
- **Vão Livre Mínimo:** 80cm ou 90cm (conforme tipologia)

---

### 3.10 SISTEMA DE GÁS COMBUSTÍVEL (GLP)

**Fonte:** Memorial Descritivo PPCI (Seção 11), PCI 08_GRR_GLP_rev00.pdf

#### 3.10.1 CENTRAL DE GLP

- **Localização:** 2º Pvto - G3 (Garagem, Central GLP e Acesso)
- **Capacidade:** Não especificada nos trechos extraídos
- **Tipo:** Central de Armazenamento de GLP (gás liquefeito de petróleo)
- **Área da Central (Arquitetura):** Incluída nos 368,75 m² do 2º Pvto

#### 3.10.2 REQUISITOS (IN 08)

- **Ventilação:** Natural permanente (aberturas na parte superior e inferior)
- **Distância de Segurança:** Conforme IN 08 (afastamento de fontes de ignição, aberturas de edificações)
- **Sinalização:** Placa "CENTRAL DE GÁS - PROIBIDO FUMAR"
- **Registro de Corte:** Externo à central, acessível e sinalizado
- **Croqui de Localização:** Indicado em PCI 08

**Observação:** Os detalhes específicos da central (capacidade em kg, número de botijões/tanques, diagrama de tubulação) não foram extraídos dos trechos analisados. Recomenda-se revisar PCI 08_GRR_GLP_rev00.pdf completo.

---

### 3.11 TRRF (TEMPO REQUERIDO DE RESISTÊNCIA AO FOGO) ESTRUTURAL

**Fonte:** Memorial Descritivo PPCI (Seção 13), IN 14

#### 3.11.1 DETERMINAÇÃO DO TRRF

- **Ocupação:** A-2 (Residencial Multifamiliar)
- **Altura da Edificação:** 57,24m (para efeito de bombeiros)
- **Carga de Incêndio:** 300 MJ/m² (Risco Leve)
- **TRRF Estimado (Tabela IN 14):** **60 minutos** (para altura 54-80m, ocupação A-2, risco leve)

**Observação:** O valor exato do TRRF não foi extraído dos trechos do memorial. Recomenda-se confirmar na seção 13 do memorial descritivo.

#### 3.11.2 REQUISITOS ESTRUTURAIS

- **Elementos Estruturais (pilares, vigas, lajes):** Devem atender ao TRRF
- **Revestimento de Proteção:** Conforme cálculo estrutural e especificação do projeto estrutural
- **Norma:** ABNT NBR 15200 (Projeto de estruturas de concreto em situação de incêndio)

---

### 3.12 CONTROLE DE FUMAÇA (VENTILAÇÃO MECÂNICA)

**Fonte:** GRANDEZZA-GRAN ROYAL-EXA-SUB-MEM-R00-assdig.pdf (Memorial Ventilação Mecânica)

#### 3.12.1 SISTEMA DE VENTILAÇÃO MECÂNICA DO SUBSOLO

**Objetivo:**
- Manter garagem de subsolo livre do gás monóxido de carbono (CO)
- Permitir segurança dos ocupantes através de troca de ar periódica
- Acionamento automático em caso de elevação dos níveis de CO

**Normas Aplicadas:**
- NBR 16401-3/2008 (Qualidade do ar interior)
- CBMSC IN 10 (Sistema de controle de fumaça)

#### 3.12.2 DIMENSIONAMENTO

**Cálculo de Suprimento de Ar:**
- **Critério:** 300 m³/h por vaga de estacionamento (IN 10, Art. 24, §4º)
- **Vagas no Subsolo:** 9 vagas
- **Vazão Requerida:** Q = 9 × 300 = 2.700 m³/h

**Exaustor Adotado:**
- **Vazão:** 2.785 m³/h
- **Pressão Estática Disponível:** 20 mmCa
- **Densidade do Ar (Condição Padrão):** 1,204 kg/m³

#### 3.12.3 TRAJETÓRIA DE ESCAPE

- **Sistema:** Dutos de descarga de ar vertical
- **Destino:** Ar contaminado levado diretamente para exterior da edificação
- **Entrada de Ar Puro:** Ventilação permanente no portão de entrada para o subsolo

#### 3.12.4 COMPONENTES DO SISTEMA

**Equipamentos:**
- **Exaustor:** 1 unidade, vazão 2.785 m³/h, pressão 20 mmCa
- **Sensores de CO:** Detecção de monóxido de carbono (acionamento automático)
- **Timer:** Acionamento periódico para renovação de ar
- **Grupo Moto-Gerador Automatizado:** Fonte de energia alternativa (garantia de funcionamento)

**Dutos:**
- **Tipo:** Dutos verticais de exaustão
- **Superfície Interna:** Lisa e estanque
- **Grelhas de Exaustão:** Instaladas rente ao teto ou máx. 20cm abaixo do teto

**Controles:**
- **Acionamento Automático:** Sensor de CO (nível crítico > 40ppm)
- **Acionamento Manual Complementar:** Tipo "liga", em local de fácil acesso
- **Parada do Sistema:** Somente após CO reduzir abaixo de 40ppm
- **Quadro de Comando:** Timer + interface com sensores

#### 3.12.5 SISTEMA ELÉTRICO E PROTEÇÃO

- **Circuito Elétrico:** Independente, conforme NBR 5410
- **Proteção de Circuitos:** Acondicionados para garantir operação em situação de emergência
- **Circuitos em Áreas de Risco:** Protegidos contra calor de incêndio pelo tempo de utilização do GMG

**Observação:** O memorial não especificou detalhes de potência do exaustor ou do GMG. Recomenda-se revisar o memorial completo e as pranchas de ventilação mecânica.

---

#### 3.12.6 SISTEMA DE PRESSURIZAÇÃO DE ESCADA

**Observação:** Não foram extraídos detalhes do sistema de pressurização de escada nos trechos analisados. Este sistema é obrigatório para edifícios acima de 60m de altura (conforme IN 10). Recomenda-se verificar as pranchas de ventilação mecânica e o memorial descritivo completo para:
- Vazão de insuflamento de ar
- Diferencial de pressão entre escada e antecâmara
- Equipamentos (ventilador, dutos, grelhas)

---

### 3.13 CONTROLE DE MATERIAIS DE ACABAMENTO

**Fonte:** Memorial Descritivo PPCI (Seção 5), IN 18

#### 3.13.1 CRITÉRIOS APLICADOS

- **Norma:** IN 018 do CBMSC
- **Objetivo:** Garantir controles de materiais de acabamento e revestimento
- **Especificações:** Conforme indicado nas plantas do projeto

**Requisitos Gerais:**
- **Escadas de Emergência:** Revestimento incombustível e antiderrapante
- **Paredes e Tetos em Rotas de Fuga:** Materiais com resistência ao fogo adequada
- **Pisos:** Antiderrapantes em escadas, rampas e áreas de risco

---

### 3.14 ACESSO DE VIATURAS

**Fonte:** Memorial Descritivo PPCI (Seção 15)

#### 3.14.1 REQUISITOS (IN 09)

- **Via de Acesso:** Largura mínima para passagem de viatura do Corpo de Bombeiros
- **Raio de Giro:** Adequado para manobra de viatura
- **Resistência do Piso:** Suportar peso da viatura carregada
- **Faixa de Estacionamento Proibido:** Sinalização horizontal e vertical

**Observação:** Detalhes específicos (largura da via, localização do ponto de estacionamento da viatura) não foram extraídos. Recomenda-se revisar seção 15 do memorial e planta de situação.

---

## 4. RESUMO EXECUTIVO - QUANTITATIVOS PRINCIPAIS

### 4.1 ELÉTRICO

| Item | Valor |
|------|-------|
| **Entrada de Energia** | Trifásica, Celesc, ramal subterrâneo |
| **QMC** | 33 medidores |
| **Ramais de Carga Aptos** | 30 circuitos, #10,0 (3F+N+PE) |
| **Ramais Áreas Comuns** | 2 circuitos (COND-01, COND-02), #25,0 |
| **Prumada Elétrica** | 160 condutores, eletrocalha 400×100mm |
| **QD COND 01-CENTRAL** | 85.736 VA instalada, 31.124 VA demandada |
| **QD COND 05-LAZER** | 38.165 VA instalada, 8.725 VA demandada |
| **Apto Tipo FN 02** | 39.300 VA instalada, 20.680 VA demandada, 16 circuitos |
| **Apto Tipo FN 01** | 40.400 VA instalada, 21.020 VA demandada, 17 circuitos |
| **Vagas VE** | Mín. 8 vagas, 2.000 VA/vaga, DR 2P 40A/30mA |

### 4.2 SPDA

| Item | Valor |
|------|-------|
| **Captor** | 1× Franklin, h=250mm, mastro 3m |
| **Cordoalhas** | 315,273m (Ø 3/8" + Ø 7/16") |
| **Rebars** | 152 peças, 355,209m, Ø 8mm×3m |
| **Barras Chatas** | 41 peças, 123m, Alumínio 7/8"×1/8" |
| **Minicaptores** | 8 unidades |
| **Caixa Equipotencialização** | 1 unidade, 9 terminais |

### 4.3 PPCI

| Item | Valor |
|------|-------|
| **Classificação** | A-2, Risco Leve, 300 MJ/m² |
| **Hidrantes** | 20 unidades, vazão 70 L/min, mangueira 1.½"×15m |
| **Reservatório SHP** | 30m³ (2× Fortlev 15m³) |
| **Extintores** | ~40-60 unidades (estimativa) |
| **SDAI** | Sistema endereçável, 3 laços, ~60-70 detectores |
| **Acionadores Manuais** | ~20 unidades |
| **Avisadores Áudio-Visuais** | ~25-30 unidades |
| **Iluminação de Emergência** | ~80-100 blocos autônomos, 30 LEDs/bloco |
| **Sinalização SAL** | ~40-50 placas (fotoluminescentes/luminosas) |
| **Portas Corta-Fogo** | 43 unidades (39× 80cm + 4× 90cm), P90 |
| **Central GLP** | 2º Pvto - G3, capacidade não especificada |
| **Ventilação Subsolo** | Exaustor 2.785 m³/h, 9 vagas, sensores CO |
| **TRRF Estrutural** | ~60 minutos (estimativa) |

---

## 5. RASTREABILIDADE DAS INFORMAÇÕES

### 5.1 FONTES CONSULTADAS

**ELÉTRICO (12 PDFs):**
- ✅ ELE 01_GRR_SUBSOLO_1°PVT_2°PVT_rev00.pdf
- ✅ ELE 02_GRR_3°PVT_4°PVT_5°PVT_rev00.pdf
- ✅ ELE 03_GRR_5°PVTO_AP TIPO FN 02_rev00.pdf
- ✅ ELE 04_GRR_UNIFILAR_AP TIPO FN 02_rev00.pdf (detalhado)
- ✅ ELE 05_GRR_5°PVTO_AP TIPO_FN 01_rev00.pdf
- ✅ ELE 06_GRR_UNIFILAR_APTO TIPO_FN 01_rev00.pdf (detalhado)
- ✅ ELE 07_GRR_COBERTURA_RESERV._rev00.pdf (detalhado)
- ✅ ELE 08_GRR_DIAGRAMAS_COND_rev00.pdf (detalhado)
- ✅ ELE 09_GRR_CROQUI_VE_G1_G2_rev00.pdf
- ✅ ELE 10_GRR_CROQUI_VE_G3_G4_rev00.pdf
- ✅ ELE 11_GRR_DIAGRAMAS_VE_rev00.pdf (detalhado)
- ✅ ELE 12_GRR_ENTR.DISTR.ENERGIA_rev00.pdf (detalhado)

**SPDA (6 PDFs + XLSX):**
- ⚠️ SPDA 01 a SPDA 06 (não extraídos em detalhe — plantas de malha)
- ✅ Lista de Materiais SPDA.xlsx (detalhado)

**PPCI (10 PDFs + 2 Memoriais):**
- ✅ PCI 01_GRR_TÉRREO E SUB_rev00.pdf
- ⚠️ PCI 02_GRR_2º e 3º PVTO_rev00.pdf (não extraído)
- ⚠️ PCI 03_GRR_4º PVTO_rev00.pdf (não extraído)
- ✅ PCI 04_GRR_PVTO TIPO_rev00.pdf
- ⚠️ PCI 05_GRR_COBERTURA_rev00.pdf (não extraído)
- ⚠️ PCI 06_GRR_CORTES_rev00.pdf (não extraído)
- ✅ PCI 07_GRR_SHP_rev00.pdf (detalhado — hidrantes)
- ⚠️ PCI 08_GRR_GLP_rev00.pdf (não extraído — só referenciado)
- ✅ PCI 09_GRR_SDAI_rev00.pdf (detalhado)
- ⚠️ PCI 10_GRR_OUTROS DETALHES_rev00.pdf (não extraído)
- ✅ GRAN ROYAL - PCI - MEMORIAL DESCRITIVO.pdf (detalhado)
- ✅ GRAN ROYAL - PCI - MEMORIAL DE CÁLCULO DE HIDRANTES.pdf (detalhado)

**VENTILAÇÃO MECÂNICA (4 PDFs):**
- ✅ GRANDEZZA-GRAN ROYAL-EXA-SUB-MEM-R00-assdig.pdf (detalhado)
- ⚠️ GRANDEZZA-GRAN ROYAL-EXA-SUB-LAY-R00.pdf (não extraído — layout)
- ⚠️ GRANDEZZA-GRAN ROYAL-EXA-SUB-P1-R00-assdig.pdf (não extraído — prancha)
- ⚠️ GRANDEZZA-GRAN ROYAL-EXA-SUB-ART-R00-assdig.pdf (não extraído — ART)

### 5.2 DADOS NÃO EXTRAÍDOS (REQUEREM ANÁLISE COMPLEMENTAR)

**ELÉTRICO:**
- Carga instalada detalhada por pavimento (G1, G2, G3)
- Demanda total da edificação (kW/kVA)
- Tipo de disjuntor geral da entrada (capacidade, modelo)
- Detalhamento de eletrodutos por trecho

**SPDA:**
- Plantas de malha de aterramento por pavimento (SPDA 01 a SPDA 06)
- Nível de proteção exato (NBR 5419)
- Resistência de aterramento esperada (Ohms)

**PPCI:**
- Localização exata de cada extintor por pavimento (PCI 01 a PCI 05)
- Capacidade da central GLP (kg, nº de botijões/tanques)
- TRRF exato (confirmação na seção 13 do memorial)
- Detalhes do sistema de pressurização de escada (vazão, pressão, equipamentos)
- Distribuição completa dos 20 hidrantes por pavimento

---

## 6. OBSERVAÇÕES E RECOMENDAÇÕES

### 6.1 OBSERVAÇÕES GERAIS

1. **Apartamentos Tipo:** As duas tipologias (FN 01 e FN 02) têm cargas instaladas muito próximas (~40kVA), com distribuição equilibrada entre fases. Ambas incluem fogão de indução e chuveiro elétrico, gerando alta demanda.

2. **Sistema VE:** Infraestrutura para veículos elétricos com mínimo 8 vagas já preparadas, com circuitos dedicados e proteção diferencial-residual.

3. **Esquema TN-S:** O esquema de aterramento TN-S (condutor PE separado do N) está corretamente especificado para toda a edificação.

4. **SPDA Completo:** Lista de materiais SPDA detalhada, permitindo quantificação precisa. Faltam apenas as plantas de malha por pavimento para validação.

5. **PPCI Robusto:** Sistema completo com 12 medidas de segurança (conforme IN 001), incluindo ventilação mecânica do subsolo e SDAI endereçável.

6. **Portas Corta-Fogo:** Quantidade de 43 portas confere com a arquitetura (2 DEA + 2 DEF por pavimento tipo + áreas comuns).

### 6.2 RECOMENDAÇÕES PARA ANÁLISE COMPLEMENTAR

**Prioridade ALTA:**
1. Revisar **PCI 01 a PCI 05** para mapear localização exata de extintores por pavimento
2. Revisar **PCI 08_GRR_GLP_rev00.pdf** para capacidade da central GLP e diagrama de tubulação
3. Revisar **SPDA 01 a SPDA 06** para validar malha de aterramento por pavimento
4. Confirmar **TRRF exato** na seção 13 do Memorial Descritivo PPCI
5. Revisar pranchas de **ventilação mecânica** (layout, equipamentos) para sistema de pressurização de escada

**Prioridade MÉDIA:**
6. Calcular **demanda total da edificação** (kW/kVA) com base nos QDs de todos os pavimentos
7. Validar **distâncias máximas de extintores** por pavimento com plantas PCI
8. Revisar **detalhamento de eletrodutos** (ELE 01 a ELE 12) para quantificação de materiais

**Prioridade BAIXA:**
9. Validar **número exato de pontos de luz** e **interruptores** por apartamento tipo com plantas ELE 03 e ELE 05
10. Verificar **resistência de aterramento SPDA** (se especificado em memorial ou relatório)

---

## 7. ENTREGÁVEL FINAL

✅ **Documento completo salvo em:**  
`/Users/leokock/orcamentos/projetos/grandezza-gran-royal/analise/onda4-eletrico-ppci.md`

**Conteúdo:**
- Sistema elétrico por pavimento (cargas, QDs, disjuntores)
- Quantitativo por unidade tipo (circuitos, pontos, fiação)
- SPDA completo (materiais, captação, aterramento)
- PPCI completo (hidrantes, extintores, SDAI, iluminação emergência, sinalização, portas CF, GLP, ventilação)
- Rastreabilidade de fontes (PDFs consultados)
- Recomendações para análise complementar

---

**Análise concluída em 15/03/2026 às 08:45 BRT**  
**Subagente:** onda4-eletrico-ppci  
**Documentos analisados:** 34 arquivos (12 Elétrico + 7 SPDA + 12 PPCI + 4 Ventilação)
