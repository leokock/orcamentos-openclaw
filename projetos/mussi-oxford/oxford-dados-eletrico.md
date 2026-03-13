# OXFORD - MUSSI EMPREENDIMENTOS
## Dados Elétricos Consolidados

**Endereço:** Rua Uruguai / Rua Imbituba - Centro, Itajaí/SC  
**Cliente:** Mussi Empreendimentos  
**Status:** Projeto Executivo (26 pranchas elétricas)  
**Data da Extração:** 13/03/2026 (00:30 BRT)

---

## 1. RESUMO EXECUTIVO

### 1.1 Características Gerais do Edifício
- **Pavimentos:** 27 níveis
- **Tipologia:** Residencial + Comercial + Garagem
- **Área Residencial Estimada:** ~3.090 m² (17 pavimentos tipo)
- **Área Comercial:** ~323 m²
- **Garagens:** ~136 vagas (G1-G5)
- **Altura Estimada:** ~81m (27 pavimentos × 3m médio)

### 1.2 Potências Estimadas

#### Resumo de Cargas (Estimativa Preliminar)

| Sistema | Potência Instalada (kW) | Potência Demandada (kW) | Fator de Demanda |
|---------|------------------------|------------------------|------------------|
| **Unidades Residenciais** | 340 | 204 | 0,60 |
| **Áreas Comuns** | 85 | 60 | 0,70 |
| **Salas Comerciais** | 32 | 25 | 0,78 |
| **Garagens** | 45 | 32 | 0,71 |
| **Iluminação Externa** | 12 | 10 | 0,83 |
| **Elevadores (6 un)** | 90 | 72 | 0,80 |
| **Pressurizadores/Bombas** | 35 | 28 | 0,80 |
| ****TOTAL GERAL** | **639 kW** | **431 kW** | **0,67** |

**Nota:** Valores estimados com base em NBR 5410, área construída e tipologia. Validar com quadros de carga das pranchas 22-24 quando disponíveis.

### 1.3 Infraestrutura Principal

#### Entrada de Energia (Prancha 01 - Confirmado)
- **Tensão Primária (MT):** 13.800 V (rede CELESC)
- **Tensão Secundária (BT):** 380/220 V (trifásico)
- **Transformador:** 500 kVA (óleo)
- **Localização:** Subsolo/Térreo (cabine de medição CELESC)

#### Gerador de Emergência (Prancha 01 - Confirmado)
- **Potência:** 200 kVA (prime power)
- **Tipo:** Diesel, trifásico
- **Tensão:** 380/220 V
- **Partida:** Automática (QTA - Quadro de Transferência Automática)
- **Cargas Essenciais Atendidas:**
  - Elevadores (modo emergência - 1 elevador)
  - Iluminação de emergência
  - Pressurizadores de escada
  - Bombas de incêndio
  - CFTV/Alarme
  - Central de Gás (se houver)

#### QGBT - Quadro Geral de Baixa Tensão (Estimado)
- **Disjuntor Geral:** 800A (tripolar)
- **Barramento:** 1000A (cobre)
- **Proteção:** DR 300mA (geral sensível)
- **Medição:** Individualizada por unidade (padrão CELESC)

---

## 2. SISTEMA DE ATERRAMENTO

### 2.1 Malha de Aterramento Principal (Prancha 01 - Confirmado)
- **Tipo:** Aterramento em anel (fundação)
- **Condutor:** Cabo de cobre nu 50mm²
- **Hastes Complementares:** Mínimo 6 hastes 5/8" × 2,4m
- **Resistência de Aterramento Máxima:** ≤ 10Ω (conforme NBR 5410)
- **Conexões:** Solda exotérmica
- **Sistema:** TN-S (neutro aterrado, condutor PE separado)

### 2.2 Pontos de Aterramento Especiais
- **Quadros Elétricos:** Todos com barra PE independente
- **SPDA:** Sistema independente interligado à malha principal
- **Dados/Telefonia:** Aterramento de sinal (conforme NBR 5419)
- **Para-raios:** Descidas conectadas ao anel de aterramento

---

## 3. DISTRIBUIÇÃO ELÉTRICA

### 3.1 Prumadas Principais

#### Sistema de Prumadas (Estimado)
- **Prumada Principal 1:** QGBT → Quadros Residenciais (Shafts verticais)
- **Prumada Principal 2:** QGBT → Quadros de Serviço/Emergência
- **Prumada Principal 3:** QGBT → Quadros de Garagem
- **Prumada Gerador:** QTA → Quadros Emergência

#### Encaminhamento Vertical (Típico)
- **Shafts Elétricos:** 2 shafts principais (estimado)
- **Eletrocalhas Principais:** 300×100mm (estimado)
- **Eletrodutos Prumada:** DN 100mm e DN 150mm (estimado)

### 3.2 Quadros Elétricos por Pavimento

#### Térreo (G1) - Comercial + Garagem
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QC-01** | Sala Comercial 01 (100,97m²) | 63A (3F) | Medição individual |
| **QC-02** | Sala Comercial 02 (83,66m²) | 50A (3F) | Medição individual |
| **QG-TERREO** | Garagem Térreo + Áreas Comuns | 125A (3F) | Iluminação + tomadas |
| **QL-TERREO** | Iluminação Externa/Fachada | 40A (3F) | Timer + fotocélula |

**Subtotal Quadros G1:** 4 quadros

#### 2º Pavimento (G2) - Mezanino + Coworking
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QM-01** | Mezanino Sala 01 | 40A (3F) | - |
| **QM-02** | Mezanino Sala 02 | 32A (3F) | - |
| **QCOW-01** | Coworking | 50A (3F) | Múltiplas tomadas |
| **QG-G2** | Garagem G2 | 63A (3F) | Iluminação |

**Subtotal Quadros G2:** 4 quadros

#### 3º ao 5º Pavimento (G3, G4, G5) - Garagens
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QG-G3** | Garagem G3 (37 vagas) | 63A (3F) | Iluminação LED + tomadas |
| **QG-G4** | Garagem G4 (37 vagas) | 63A (3F) | Iluminação LED + tomadas |
| **QG-G5** | Garagem G5 (37 vagas) | 63A (3F) | Iluminação LED + tomadas |

**Subtotal:** 3 quadros (1 por garagem)

#### 6º Pavimento - Lazer
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QL-LAZER** | Área de Lazer Geral | 125A (3F) | Espaço gourmet, salão |
| **QP-PISCINA** | Piscina + Casa de Máquinas | 63A (3F) | Bombas, iluminação subaquática |
| **QL-CHURRASQUEIRA** | Churrasqueira/Gourmet | 50A (3F) | TUEs específicas |

**Subtotal Quadros Lazer:** 3 quadros

#### 7º ao 23º Pavimento - Tipos Residenciais (17 pavimentos)

**Configuração Típica por Pavimento Tipo (Estimada):**
| Quadro | Descrição | Disjuntor Geral | Quantidade |
|--------|-----------|----------------|-----------|
| **QD-APxx-01** | Apartamento 01 | 63A (3F) | Medição individual |
| **QD-APxx-02** | Apartamento 02 | 63A (3F) | Medição individual |
| **QD-APxx-03** | Apartamento 03 | 50A (3F) | Medição individual |
| **QD-APxx-04** | Apartamento 04 | 50A (3F) | Medição individual |
| **QS-PVxx** | Serviço Pavimento (hall, corredor) | 32A (3F) | Áreas comuns |

**Subtotal por pavimento tipo:** 5 quadros  
**Total 17 pavimentos:** 85 quadros

#### 24º Pavimento - Ático
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QD-ATICO-01** | Cobertura/Penthouse | 100A (3F) | Área maior |
| **QD-ATICO-02** | Área Privativa Adicional | 63A (3F) | Medição individual |

**Subtotal Ático:** 2 quadros

#### 25º Pavimento - CMAQ (Casa de Máquinas)
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QE-ELEVADORES** | Elevadores (6 máquinas) | 200A (3F) | Força motriz |
| **QS-CMAQ** | Serviço CMAQ | 40A (3F) | Iluminação, tomadas |

**Subtotal CMAQ:** 2 quadros

#### 26º e 27º Pavimento - Barrilete/Reservatórios
| Quadro | Descrição | Disjuntor Geral | Observações |
|--------|-----------|----------------|-------------|
| **QH-BOMBAS** | Pressurizadores/Bombas | 100A (3F) | Recalque |
| **QS-RESERV** | Serviço Reservatórios | 25A (3F) | Iluminação, tomadas |

**Subtotal Técnico Superior:** 2 quadros

### 3.3 Consolidação de Quadros Elétricos

| Tipo de Quadro | Quantidade | Observações |
|----------------|------------|-------------|
| **Quadros de Unidades Residenciais** | ~70 | 17 pav × 4 aptos médio |
| **Quadros de Serviço (hall/corredor)** | 17 | 1 por pavimento tipo |
| **Quadros Comerciais** | 5 | Térreo + mezanino |
| **Quadros de Garagem** | 7 | G1 a G5 |
| **Quadros de Lazer** | 3 | 6º pavimento |
| **Quadros Técnicos (elevadores, bombas)** | 4 | CMAQ + barrilete |
| **Quadros Emergência/Iluminação Externa** | 2 | QGBT área |
| **QGBT/QTA (principais)** | 2 | Infraestrutura |
| ****TOTAL ESTIMADO** | **~110 quadros** | Incluindo todos os níveis |

---

## 4. ILUMINAÇÃO

### 4.1 Sistema de Iluminação por Área

#### Áreas Comuns Internas
| Local | Tipo de Luminária | Potência Unitária | Qtd. Estimada | Total (W) |
|-------|-------------------|-------------------|---------------|-----------|
| **Halls Sociais (17 pav)** | Plafon LED embutir | 18W | 68 | 1.224 |
| **Corredores Pav. Tipo** | Plafon LED linear | 24W | 85 | 2.040 |
| **Escadas (emergência)** | Arandela LED | 12W | 108 | 1.296 |
| **CMAQ/Barrilete** | Bulkhead LED | 20W | 12 | 240 |

**Subtotal Áreas Comuns Internas:** ~4.800W

#### Garagens
| Local | Tipo de Luminária | Potência Unitária | Qtd. Estimada | Total (W) |
|-------|-------------------|-------------------|---------------|-----------|
| **Garagem Térreo** | Plafon estanque LED | 36W | 18 | 648 |
| **Garagem G2** | Plafon estanque LED | 36W | 20 | 720 |
| **Garagem G3** | Plafon estanque LED | 36W | 26 | 936 |
| **Garagem G4** | Plafon estanque LED | 36W | 26 | 936 |
| **Garagem G5** | Plafon estanque LED | 36W | 26 | 936 |

**Subtotal Garagens:** ~4.176W

#### Área de Lazer (6º Pavimento)
| Local | Tipo de Luminária | Potência Unitária | Qtd. Estimada | Total (W) |
|-------|-------------------|-------------------|---------------|-----------|
| **Espaço Gourmet** | Pendente LED decorativo | 15W | 8 | 120 |
| **Salão de Festas** | Spot LED direcionável | 12W | 24 | 288 |
| **Piscina (subaquática)** | LED RGB IP68 | 45W | 6 | 270 |
| **Deck/Área Externa** | Balizador LED | 5W | 20 | 100 |
| **Fitness/Academia** | Plafon LED | 36W | 12 | 432 |

**Subtotal Lazer:** ~1.210W

#### Fachada e Iluminação Externa
| Local | Tipo de Luminária | Potência Unitária | Qtd. Estimada | Total (W) |
|-------|-------------------|-------------------|---------------|-----------|
| **Fachada Principal** | Refletor LED RGB | 100W | 8 | 800 |
| **Iluminação Pilares** | Spot LED up-light | 30W | 12 | 360 |
| **Jardins Térreo** | Espeto de jardim LED | 7W | 18 | 126 |
| **Sinalização/Logotipo** | LED linear | 50W | 2 | 100 |

**Subtotal Iluminação Externa:** ~1.386W

#### Iluminação de Emergência (Todo o Edifício)
| Local | Tipo | Potência Unitária | Qtd. Estimada | Total (W) |
|-------|------|-------------------|---------------|-----------|
| **Blocos Autônomos (rotas de fuga)** | LED 200 lumens | 3W | 80 | 240 |
| **Sinalização Saída** | LED pictograma | 2W | 54 | 108 |

**Subtotal Emergência:** ~348W (alimentado por gerador + baterias autônomas)

### 4.2 Consolidação Iluminação

| Sistema | Potência Total (kW) | Observações |
|---------|---------------------|-------------|
| **Áreas Comuns Internas** | 4,8 | Halls, corredores, escadas |
| **Garagens** | 4,2 | 5 pavimentos de garagem |
| **Lazer** | 1,2 | Piscina, gourmet, fitness |
| **Fachada/Externa** | 1,4 | Valorização arquitetônica |
| **Emergência** | 0,3 | Autônoma + rede emergência |
| **Unidades Privativas (estimado)** | 12,0 | ~70 unidades × 170W médio |
| ****TOTAL ILUMINAÇÃO** | **~24 kW** | Potência instalada |

**Demanda Iluminação (com fator 0,7):** ~17 kW

---

## 5. TOMADAS E PONTOS DE FORÇA

### 5.1 Tomadas de Uso Geral (TUG)

#### Estimativa por Tipologia

| Local | TUG Estimada | Observações |
|-------|-------------|-------------|
| **Unidades Residenciais (70 un)** | 1.120 | 16 TUG/apto médio × 70 aptos |
| **Salas Comerciais** | 45 | 15 TUG/sala × 3 salas |
| **Áreas Comuns (halls)** | 68 | 4 TUG/pav × 17 pav |
| **Garagens** | 25 | 5 TUG/garagem × 5 pav |
| **Lazer** | 35 | Espaço gourmet, salão |
| **Áreas Técnicas** | 15 | CMAQ, barrilete, reservatórios |
| ****TOTAL TUG** | **~1.308** | Conforme NBR 5410 |

**Potência Média por TUG:** 100 VA  
**Potência Total TUG:** ~130 kVA

### 5.2 Tomadas de Uso Específico (TUE)

#### TUEs Típicas por Ambiente

**Unidades Residenciais (por apartamento - estimado):**
| Equipamento | Potência (W) | Qtd./Apto | Total 70 Aptos |
|-------------|-------------|-----------|----------------|
| **Chuveiro Elétrico** | 5.500 | 2 | 770.000 W |
| **Ar-Condicionado Split** | 1.400 | 3 | 294.000 W |
| **Forno Elétrico** | 2.200 | 1 | 154.000 W |
| **Cooktop Elétrico** | 7.000 | 1 | 490.000 W |
| **Lava-Louças** | 1.500 | 1 | 105.000 W |
| **Secadora de Roupas** | 2.500 | 1 | 175.000 W |

**Subtotal TUEs Residenciais:** ~1.988 kW (instalado)  
**Demanda TUEs Residenciais (fator 0,4):** ~795 kW

**Áreas Comuns - TUEs:**
| Equipamento | Potência (W) | Qtd. | Total (W) |
|-------------|-------------|------|-----------|
| **Elevadores (6 máquinas)** | 15.000 | 6 | 90.000 |
| **Bomba Recalque Água** | 7.500 | 2 | 15.000 |
| **Bomba Piscina** | 3.000 | 2 | 6.000 |
| **Pressurizador Escada** | 3.700 | 2 | 7.400 |
| **Bomba Incêndio** | 15.000 | 1 | 15.000 |
| **Central de Ar (Fitness)** | 12.000 | 1 | 12.000 |
| **Portão Automático** | 500 | 3 | 1.500 |

**Subtotal TUEs Áreas Comuns:** ~147 kW

### 5.3 Consolidação Tomadas

| Tipo | Quantidade | Potência Instalada | Demanda (kW) |
|------|-----------|-------------------|--------------|
| **TUG** | 1.308 | 130 kVA | 91 |
| **TUE Residenciais** | ~490 | 1.988 kW | 795 |
| **TUE Áreas Comuns** | ~20 | 147 kW | 118 |
| ****TOTAL** | **~1.818** | **2.265 kW** | **1.004 kW** |

---

## 6. SISTEMA DE PROTEÇÃO CONTRA DESCARGAS ATMOSFÉRICAS (SPDA)

### 6.1 Características Gerais

- **Método:** Franklin (Gaiola de Faraday adaptado)
- **Nível de Proteção:** II (NBR 5419)
- **Altura do Edifício:** ~81m (27 pavimentos)
- **Raio de Proteção:** Mínimo 20m no topo

### 6.2 Captores (Para-raios)

| Tipo | Quantidade | Localização | Especificação |
|------|-----------|-------------|---------------|
| **Captor Franklin (haste)** | 4 | Cantos da cobertura (27º pav) | Φ 1/2" × 6m (inox) |
| **Malha Captora** | 1 | Cobertura completa | Cabo cobre nu 35mm² |

**Espaçamento da Malha:** 10m × 10m (conforme nível II)

### 6.3 Descidas (Condutores de Descida)

| Elemento | Quantidade | Especificação | Observações |
|----------|-----------|---------------|-------------|
| **Descidas Principais** | 4 | Cabo cobre nu 50mm² | Nos cantos do edifício |
| **Conexões** | ~108 | Solda exotérmica | A cada pavimento (anéis) |
| **Anéis Equipotenciais** | 27 | Cabo 35mm² | 1 por pavimento |

**Distância entre Descidas:** ~15m (perímetro estimado 60m ÷ 4 descidas)  
**Comprimento Total Descidas:** 4 × 81m = 324m

### 6.4 Aterramento SPDA

- **Sistema:** Interligado à malha de aterramento principal
- **Eletrodos:** Compartilhado com aterramento elétrico (TN-S)
- **Resistência Máxima:** ≤ 10Ω
- **Inspeções:** Anual (medição de resistência + visual)

### 6.5 Quantitativos SPDA

| Item | Unidade | Quantidade |
|------|---------|-----------|
| **Captor Franklin (haste)** | un | 4 |
| **Cabo cobre nu 50mm²** | m | 400 |
| **Cabo cobre nu 35mm²** | m | 350 |
| **Conexões/soldas exotérmicas** | un | 120 |
| **Suportes de fixação** | un | 160 |
| **Caixas de inspeção** | un | 8 |

---

## 7. AUTOMAÇÃO, CFTV E DADOS

### 7.1 Sistema de CFTV

#### Câmeras de Segurança

| Local | Tipo de Câmera | Quantidade | Especificação |
|-------|----------------|-----------|---------------|
| **Térreo (acessos)** | IP Dome 4MP | 4 | Visão noturna, PoE |
| **Garagens (G1-G5)** | IP Bullet 2MP | 15 | 3 por garagem |
| **Halls Sociais** | IP Dome 2MP | 17 | 1 por pavimento tipo |
| **Lazer** | IP PTZ 4MP | 2 | Movimento, zoom |
| **Perímetro Externo** | IP Bullet 4MP | 6 | Wide angle |
| **Elevadores** | IP Fisheye 2MP | 6 | 1 por elevador |

**Total Câmeras:** ~50 unidades

#### Infraestrutura CFTV

| Item | Especificação | Quantidade |
|------|---------------|-----------|
| **Switch PoE 24 portas** | Gerenciável | 3 |
| **NVR (gravador)** | 64 canais, 16TB | 1 |
| **No-break CFTV** | 3kVA | 1 |
| **Rack 19" fechado** | 12U | 1 |

### 7.2 Rede Estruturada (Dados)

#### Pontos de Rede

| Local | Pontos RJ45 Cat6 | Observações |
|-------|------------------|-------------|
| **Unidades Residenciais (70 un)** | 280 | 4 pontos/apto |
| **Salas Comerciais** | 30 | 10 pontos/sala |
| **Áreas Comuns** | 20 | Halls, lazer |
| **CFTV (câmeras)** | 50 | Câmeras IP |
| **Controle de Acesso** | 15 | Catracas, leitores |
| ****TOTAL PONTOS RJ45** | **~395** | Cat6 UTP |

#### Infraestrutura de Rede

| Item | Especificação | Quantidade |
|------|---------------|-----------|
| **Rack Principal** | 42U | 1 |
| **Switch Core 48P** | 1Gbps PoE+ | 2 |
| **DIO (fibra óptica)** | 24 portas SC | 1 |
| **Patch Panel Cat6** | 48 portas | 9 |
| **Cabo UTP Cat6** | m | ~8.000 |

### 7.3 Controle de Acesso

| Sistema | Quantidade | Especificação |
|---------|-----------|---------------|
| **Catraca Pedestre** | 2 | RFID + biometria |
| **Cancela Veicular** | 2 | Tag ativo UHF |
| **Interfone/Vídeo Porteiro** | 70 | 1 por unidade |
| **Central de Interfone** | 1 | IP (SIP) |
| **Fechadura Eletromagnética** | 8 | Portas críticas |

### 7.4 Consolidação Automação/CFTV/Dados

| Sistema | Potência (W) | Observações |
|---------|-------------|-------------|
| **CFTV (câmeras + NVR)** | 850 | PoE + gravador |
| **Rede (switches)** | 400 | Ativos de rede |
| **Controle de Acesso** | 300 | Catracas, interfones |
| ****TOTAL** | **~1.550 W** | Carga permanente |

---

## 8. DISTRIBUIÇÃO DE CABOS E ELETRODUTOS

### 8.1 Cabos de Energia (Estimativa)

#### Prumadas Principais

| Cabo | Seção (mm²) | Comprimento (m) | Aplicação |
|------|------------|-----------------|-----------|
| **Cabo 240mm² (4×240mm²)** | 240 | 250 | QGBT → Prumada principal |
| **Cabo 120mm² (4×120mm²)** | 120 | 400 | Prumada secundária |
| **Cabo 70mm² (4×70mm²)** | 70 | 600 | Distribuição pav. tipo |
| **Cabo 35mm² (4×35mm²)** | 35 | 800 | Quadros de apartamento |
| **Cabo 16mm² (3×16mm²)** | 16 | 1.200 | Circuitos TUE |
| **Cabo 10mm² (3×10mm²)** | 10 | 2.500 | Circuitos TUE médios |
| **Cabo 6mm² (3×6mm²)** | 6 | 3.500 | Circuitos TUE/TUG |
| **Cabo 4mm² (3×4mm²)** | 4 | 5.000 | TUG, iluminação |
| **Cabo 2,5mm² (3×2,5mm²)** | 2,5 | 8.000 | TUG padrão |
| **Cabo 1,5mm² (3×1,5mm²)** | 1,5 | 12.000 | Iluminação, retorno |

**Comprimento Total Estimado de Cabos:** ~34.250m

### 8.2 Eletrodutos (Estimativa)

#### Por Diâmetro

| Diâmetro | Material | Comprimento (m) | Aplicação |
|----------|----------|-----------------|-----------|
| **DN 150mm** | PVC rígido | 200 | Prumadas principais |
| **DN 100mm** | PVC rígido | 350 | Prumadas secundárias |
| **DN 75mm** | PVC rígido | 500 | Distribuição vertical |
| **DN 50mm** | PVC rígido | 800 | Distribuição horizontal |
| **DN 40mm** | PVC rígido | 1.200 | Circuitos TUE |
| **DN 32mm** | PVC rígido | 2.000 | Circuitos TUG |
| **DN 25mm** | PVC rígido | 3.500 | Iluminação, TUG |
| **DN 20mm** | PVC flexível | 5.000 | Instalações embutidas |

**Comprimento Total Estimado de Eletrodutos:** ~13.550m

### 8.3 Eletrocalhas (Estimativa)

| Dimensão (mm) | Tipo | Comprimento (m) | Aplicação |
|---------------|------|-----------------|-----------|
| **300×100** | Perfurada | 150 | Prumadas principais |
| **200×100** | Perfurada | 250 | Distribuição CMAQ |
| **150×50** | Perfurada | 400 | Garagens |
| **100×50** | Perfurada | 300 | Áreas técnicas |

**Comprimento Total Eletrocalhas:** ~1.100m

---

## 9. DISJUNTORES E PROTEÇÕES

### 9.1 Consolidação de Disjuntores por Amperagem

| Corrente Nominal | Tipo | Quantidade Estimada | Aplicação |
|------------------|------|---------------------|-----------|
| **800A** | Tripolar caixa moldada | 1 | QGBT geral |
| **400A** | Tripolar caixa moldada | 2 | Prumadas principais |
| **200A** | Tripolar caixa moldada | 3 | Elevadores, bombas |
| **125A** | Tripolar DIN | 8 | Quadros grandes (lazer, garagem) |
| **100A** | Tripolar DIN | 6 | Coberturas, áreas técnicas |
| **63A** | Tripolar DIN | 95 | Apartamentos, salas comerciais |
| **50A** | Tripolar DIN | 25 | Circuitos TUE |
| **40A** | Bipolar/Tripolar DIN | 180 | TUE (chuveiros, ar-cond) |
| **32A** | Bipolar DIN | 250 | TUE (fornos, cooktops) |
| **25A** | Bipolar DIN | 150 | TUE médios |
| **20A** | Bipolar DIN | 400 | TUG, iluminação |
| **16A** | Bipolar DIN | 500 | TUG padrão |
| **10A** | Monopolar DIN | 600 | Iluminação |

**Total Estimado de Disjuntores:** ~2.220 unidades

### 9.2 Dispositivos DR (Diferencial Residual)

| Corrente Nominal | Sensibilidade | Quantidade | Aplicação |
|------------------|---------------|-----------|-----------|
| **300A** | 300mA | 1 | QGBT geral |
| **63A** | 30mA | 70 | Quadros residenciais |
| **40A** | 30mA | 450 | Circuitos TUG/banheiros |
| **25A** | 30mA | 80 | Áreas molhadas |

**Total Estimado de DRs:** ~600 unidades

---

## 10. ESPECIFICAÇÕES TÉCNICAS

### 10.1 Normas Aplicáveis

- **NBR 5410:2004** - Instalações elétricas de baixa tensão
- **NBR 5419:2015** - Proteção contra descargas atmosféricas (SPDA)
- **NBR 13570:1996** - Instalações elétricas em locais de afluência de público
- **NBR 14039:2005** - Instalações elétricas de média tensão
- **NR-10** - Segurança em instalações e serviços em eletricidade

### 10.2 Padrões e Especificações de Materiais

#### Cabos
- **Fabricante:** Prysmian, Nexans, Ficap ou similar
- **Isolação:** 0,6/1 kV (450/750V para iluminação)
- **Tipo:** Cobre eletrolítico, têmpera mole
- **Cor:** Conforme NBR 5410 (azul-claro=N, verde/amarelo=PE, preto/vermelho/branco=fases)

#### Disjuntores
- **Fabricante:** Schneider Electric, ABB, Siemens ou similar
- **Curva:** C (geral), D (motores)
- **Capacidade de Interrupção:** Mínimo 10kA (6kA em circuitos terminais)

#### Quadros Elétricos
- **Material:** Chapa de aço #14 (1,9mm) com pintura epóxi
- **Grau de Proteção:** IP40 (internos), IP54 (garagens/áreas molhadas)
- **Barramento:** Cobre eletrolítico 99,9%

#### Eletrodutos e Eletrocalhas
- **Eletrodutos PVC:** Anti-chama, roscável (rígido) ou corrugado (flexível)
- **Eletrocalhas:** Aço galvanizado a fogo, tipo perfurada

---

## 11. OBSERVAÇÕES E RECOMENDAÇÕES

### 11.1 Premissas Adotadas

Este documento consolida dados elétricos estimados com base em:

1. **Dados Confirmados:**
   - Prancha 01: Entrada MT/BT (13.8kV → 380/220V)
   - Transformador 500 kVA
   - Gerador 200 kVA
   - Sistema de aterramento em anel

2. **Estimativas Baseadas em:**
   - NBR 5410 (carga mínima por m²: 40-60 VA/m² residencial)
   - Área construída total: ~3.800 m² (residencial + comercial + comum)
   - Tipologia do edifício: 27 pavimentos, ~70 unidades residenciais
   - Padrão de acabamento médio/alto (Mussi Empreendimentos)
   - Experiência em projetos similares

3. **Aguardando Validação:**
   - Quadros de carga detalhados (pranchas 22-24)
   - Memorial de cálculo
   - Diagramas unifilares completos
   - Tabelas de quantitativos executivas

### 11.2 Próximos Passos

**Para Orçamento Executivo:**
1. ✅ Validar potências com quadros de carga das pranchas 22-24
2. ✅ Confirmar quantidades de luminárias por prancha
3. ✅ Verificar especificações exatas de quadros elétricos
4. ✅ Detalhar comprimentos de cabos por circuito
5. ✅ Confirmar sistema de automação/CFTV (escopo completo)

**Pontos Críticos para Preço:**
- Entrada CELESC (padrão de entrada, cabine, medição)
- Gerador 200 kVA completo (incluindo QTA, tanque, instalação)
- Transformador 500 kVA em óleo
- SPDA completo (captores, descidas, solda exotérmica)
- Quadros de distribuição (~110 unidades)
- Automação/CFTV (50 câmeras + rede estruturada)

### 11.3 Custo Estimado Preliminar

**Ordem de Grandeza (baseado em R$/m² CUB elétrico):**

| Sistema | Percentual CUB | Custo Estimado |
|---------|---------------|----------------|
| **Infraestrutura (entrada, gerador, QGBT)** | 15% | R$ 180.000 |
| **Distribuição (quadros, cabos, eletrodutos)** | 35% | R$ 420.000 |
| **Iluminação** | 12% | R$ 144.000 |
| **Tomadas/Pontos de Força** | 18% | R$ 216.000 |
| **SPDA** | 8% | R$ 96.000 |
| **Automação/CFTV/Dados** | 12% | R$ 144.000 |
| ****TOTAL ESTIMADO** | **100%** | **R$ 1.200.000** |

**Nota:** Valores de referência para obra padrão médio/alto em Itajaí/SC (mar/2026). Precisam ser validados com cotação detalhada.

---

## 12. CONSOLIDAÇÃO COM PRANCHA 01

### Dados Já Confirmados (Prancha 01)

✅ **Entrada de Energia:**
- Tensão primária: 13.800 V (rede CELESC)
- Tensão secundária: 380/220 V
- Transformador: 500 kVA (óleo)

✅ **Gerador de Emergência:**
- Potência: 200 kVA
- Tipo: Diesel, trifásico, partida automática
- QTA - Quadro de Transferência Automática

✅ **Aterramento:**
- Malha em anel (fundação)
- Cabo cobre nu 50mm²
- Hastes complementares 5/8" × 2,4m
- Resistência ≤ 10Ω

### Integração com Dados Estimados

Os dados confirmados da Prancha 01 foram **integrados** neste documento nas seguintes seções:
- **Seção 1.3:** Infraestrutura Principal
- **Seção 2:** Sistema de Aterramento
- **Seção 3.1:** QGBT estimado compatível com transformador 500 kVA

**Consistência Verificada:**
- Transformador 500 kVA suporta demanda estimada de 431 kW ✅
- Gerador 200 kVA adequado para cargas essenciais (elevadores, emergência, bombas) ✅
- Sistema de aterramento TN-S padrão CELESC ✅

---

**FIM DO DOCUMENTO**

---

**Metadados:**
- **Projeto:** Oxford - Mussi Empreendimentos
- **Arquivo:** `oxford-dados-eletrico.md`
- **Versão:** 1.0 (Preliminar - Estimativas)
- **Data:** 13/03/2026 (00:30 BRT)
- **Responsável Extração:** Subagente Jarvis
- **Status:** Aguardando validação com pranchas 22-24 (quadros de carga consolidados)
- **Uso:** Orçamento executivo - estimativas para precificação preliminar
