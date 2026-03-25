# ANÁLISE HIDROSSANITÁRIA - GRAN ROYAL RESIDENCE
**Grandezza Construtora | Balneário Piçarras/SC**

Data: 15/03/2026  
Fonte: Projetos Hidrosanitários rev00 (Hidráulico e Sanitário Executivo/Aprovativo)

---

## 1. SISTEMA HIDRÁULICO

### 1.1 RESERVATÓRIOS E ARMAZENAMENTO

**Reservatório Inferior (3° Pavimento):**
- **Capacidade total:** 30 m³
- **Composição:** 2 células em concreto armado impermeabilizado
  - Célula 01: 16,95 m² × h lâmina 1,10m = 12,71 m³ útil (altura livre 0,35m)
  - Célula 02: 19,80 m² × h lâmina 1,10m = 14,85 m³ útil (altura livre 0,35m)
- **Fonte:** HID 01_GRR_SUBSOLO, corte esquemático; HID 03_GRR_2° E 3° PVTO

**Reservatório de Reúso (Subsolo):**
- **Capacidade:** 5 m³
- **Tipo:** Tanque Fortlev 5000L
- **Dimensões:** Ø 2,25m × h 1,51m
- **Sistema:** Aproveitamento de água da chuva + realimentador automático
- **Bombeamento:** Pressurizador dedicado + bomba de recalque
- **Fonte:** HID 01_GRR_SUBSOLO

**Reservatório Superior (Cobertura):**
- **Capacidade total:** 30 m³ (confirmado)
- **Composição:** 2 reservatórios Fortlev 15.000L cada
  - Reservatório 01: V=15m³, Ø 3,20m, h=2,20m
  - Reservatório 02: V=15m³, Ø 3,20m, h=2,20m
- **Distribuição funcional:**
  - Volume consumo: 15.000L
  - Volume RTI (Reserva Técnica de Incêndio): 15.000L
- **Alimentação:** Recalque do reservatório inferior (3° pavimento)
- **Fonte:** HID 07_GRR_CORTE ESQUEMÁTICO, HID 08_GRR_COBERTURA E RESERVATÓRIO

---

### 1.2 BOMBEAMENTO E PRESSURIZAÇÃO

**Bomba de Recalque (Subsolo → Reservatório Superior):**
- **Altura geométrica:** 71,09 m
- **Perda de carga:** 2,68 m
- **Altura manométrica:** 73,83 m
- **Vazão de trabalho:** 7,9 m³/h
- **Sistema:** Duas motobombas (ativa + reserva) com relé biestável
- **Tubulação:** PPR PN 12 (sucção e recalque)
- **Alimentação reservatório superior:** Dimensionada para abastecer consumo diário em até 6h
- **Fonte:** HID 01_GRR_SUBSOLO, detalhe 3D bomba de recalque

**Sistema de Pressurização (Barrilete - 3° Pavimento):**
- **Função:** Atender pavimentos 5° ao 19° (zona pressurizada)
- **Pressão de regulagem:** 25 m.c.a (sistema com inversor de frequência)
- **Equipamentos:** 2 pressurizadores (código 05 e 06 na lista)
  - Vazão: 2,41 m³/h cada
  - Pressão: 20 m.c.a cada
- **Tubulação de distribuição:**
  - AF-03: Ø32mm (alimenta 5° ao 9°)
  - AF-04: Ø32mm (alimenta 10° ao 14°)
  - AF-05, AF-06, AF-07, AF-08: Ø32mm cada (alimentam 15° ao 19°)
- **Bypass:** Sistema com válvula N.F. (normalmente fechada) para consumo em caso de falta de energia ou manutenção
- **Fonte:** HID 07_GRR_CORTE ESQUEMÁTICO; HID 08_GRR_COBERTURA E RESERVATÓRIO, detalhe 3D pressurizador

**Bomba de Recalque - Água de Reúso (Subsolo):**
- **Função:** Recalcar água da cisterna pluvial para pontos de consumo
- **Tipo:** Pressurizador dedicado
- **Tubulação:** AR-01 Ø32mm (distribuição em todos os pavimentos)
- **Pontos de uso:** TJ 3/4" com cadeado e placa "ÁGUA NÃO POTÁVEL"
- **Fonte:** HID 01_GRR_SUBSOLO, HID 02_GRR_TÉRREO

---

### 1.3 ZONAS DE PRESSÃO

**Zona Pressurizada (Pavimentos 5° ao 19°):**
- **Pressão:** 25 m.c.a (sistema inversor de frequência)
- **Altura pressurizada:** ~60m (da cota barrilete 6279 até 19°pvto 5724)
- **Colunas de alimentação:**
  - AF-01: Ø60mm (consumo gravitacional - backup)
  - AF-03, AF-04, AF-05, AF-06, AF-07, AF-08: Ø32mm (pressurizadas)
- **Válvulas de retenção:** Instaladas em AF-01 Ø60mm (dois pontos)
- **Fonte:** HID 07_GRR_CORTE ESQUEMÁTICO

**Zona Gravitacional (Pavimentos 10° ao 14° - parcial):**
- **Pressão estática:** 12,60 a 35,66 m.c.a
- **Coluna:** AF-01 Ø60mm (gravidade pura do reservatório superior)
- **Válvula de retenção:** Soldável 60mm TIGRE (dois pontos)
- **Fonte:** HID 07_GRR_CORTE ESQUEMÁTICO

**Zona de ERP - Estação Redutora de Pressão (9° Pavimento):**
- **Pressão montante (Pm):** 35,66 m.c.a
- **Pressão jusante (Pju):** 20,37 m.c.a
- **Altura ERP:** 245m, 260m (referências de cota)
- **Justificativa:** NBR 5626 - pressão estática nos pontos de utilização não pode superar 400 kPa (40 m.c.a)
- **Fonte:** HID 07_GRR_CORTE ESQUEMÁTICO

---

### 1.4 DISTRIBUIÇÃO POR PAVIMENTO

#### SUBSOLO
**Água Fria:**
- Bomba de recalque + tubulações de sucção/recalque para reservatório superior
- Sistema de cisterna pluvial (5m³) com bomba de recalque para reúso

**Água de Reúso:**
- Pressurizador + coluna AR-01 Ø32mm iniciando distribuição vertical

**Fonte:** HID 01_GRR_SUBSOLO

---

#### TÉRREO
**Água Fria:**
- Hidrômetro predial: DN 1 1/2" (Qmax 20m³/h, Qn 10m³/h) - padrão CASAN
- Alimentador predial: Ø50mm (entrada da concessionária)
- Coluna AL-01 Ø63mm (alimentação reservatório inferior)
- TJ 3/4" para lixeira (torneira de jardim h=60cm)

**Água de Reúso:**
- Coluna AR-01 Ø32mm com TJ 3/4" + cadeado + placa "ÁGUA NÃO POTÁVEL"
- Registro de gaveta 3/4" h=180cm

**Fonte:** HID 02_GRR_TÉRREO

---

#### 2° e 3° PAVIMENTOS (Garagens)
**Água Fria:**
- Coluna AL-01 Ø63mm (alimentação)
- Coluna AF-01 Ø40mm (distribuição)
- TJ 3/4" para lavagem (h=60cm)
- Registro de gaveta 3/4" h=220cm (2°pvto) / h=180cm (3°pvto)

**Água de Reúso:**
- Coluna AR-01 Ø32mm
- TJ 3/4" + RG 3/4" com sinalização "ÁGUA NÃO POTÁVEL"

**Fonte:** HID 03_GRR_2° E 3° PVTO

---

#### 4° PAVIMENTO (LAZER)
**Pontos de Água Fria:**
- 4× Lavatórios (LV) - Ø22mm × 1/2", h=60cm
- 2× Chuveiros (CH) - Ø22mm × 1/2", h=210cm
- 1× Pia cozinha - Ø22mm × 1/2", h=60cm
- 1× Tanque (TQ) - 3/4", h=110cm
- 1× Máquina lavar roupa (MLR) - 3/4", h=80cm
- 1× Torneira jardim (TJ) - 3/4", h=60cm
- **Total pavimento lazer:** ~10 pontos água fria

**Diâmetros de alimentação:**
- Colunas: AF-01 Ø40mm
- Ramais internos: Ø25mm, Ø22mm

**Água de Reúso:**
- Coluna AR-01 Ø32mm
- TJ 3/4" com sinalização

**Fonte:** HID 04_GRR_LAZER (extrapolação baseada em padrão de apartamentos)

---

#### PAVIMENTO TIPO (5° ao 19° - 14 pavimentos × 2 apartamentos = 28 unidades)

**Pontos de Água Fria por apartamento (tipologia padrão):**
- **BWC Suíte:**
  - 1× Lavatório (LV) - Ø22mm × 1/2", h=60cm
  - 1× Vaso sanitário (VS) - 3/4", h=20cm
  - 1× Chuveiro (CH) - Ø22mm × 1/2", h=210cm
- **BWC 02:**
  - 1× Lavatório (LV) - Ø22mm × 1/2", h=60cm
  - 1× Vaso sanitário (VS) - 3/4", h=20cm
  - 1× Chuveiro (CH) - Ø22mm × 1/2", h=210cm
- **Lavabo:**
  - 1× Lavatório (LV) - Ø22mm × 1/2", h=60cm
  - 1× Vaso sanitário (VS) - 3/4", h=20cm
- **Cozinha:**
  - 1× Pia (PIA) - Ø22mm × 1/2", h=60cm
- **Área de Serviço:**
  - 1× Tanque (TQ) - 3/4", h=110cm
  - 1× Máquina lavar roupa (MLR) - 3/4", h=80cm

**Total por apartamento:** 12 pontos de água fria

**Total pavimento tipo (2 aptos):** 24 pontos de água fria

**Total 14 pavimentos tipo (5° ao 19°):** 336 pontos de água fria (só apartamentos tipo)

**Diâmetros de alimentação:**
- Coluna principal (zona pressurizada): AF-03 a AF-08 Ø32mm
- Coluna backup (gravitacional): AF-01 Ø60mm
- Barrilete apartamento: Ø32mm
- Ramais internos: Ø28mm, Ø25mm, Ø22mm
- Hidrômetro individual: 5m³/h (VN=2,5m³/h) por apartamento
- Válvula de retenção: Soldável 32mm TIGRE (cada apto)

**Fonte:** HID 05_GRR_TIPO; HID 06_GRR_DET TIPO; HID 07_GRR_CORTE ESQUEMÁTICO

---

#### ÁGUA QUENTE - SISTEMA DE AQUECIMENTO

**Tipo de aquecimento:** **Aquecedor de passagem a gás - 25L/min** (individual por apartamento)

**Pontos de água quente por apartamento:**
- 2× Chuveiros (BWC Suíte + BWC 02) - alimentação CPVC (obrigatório, resistência térmica)
- 2× Lavatórios (BWC Suíte + BWC 02) - alimentação CPVC

**Total por apartamento:** 4 pontos de água quente

**Total 14 pavimentos tipo:** 112 pontos de água quente (28 aptos × 4)

**Tubulação:**
- Material: **CPVC obrigatório** no trecho de saída do aquecedor até os pontos (baixa resistência térmica do PVC)
- Diâmetros: Ø25mm, Ø22mm

**Aquecedores:**
- Localização: Área técnica (sacada) de cada apartamento
- Vazão: 25L/min
- Quantidade total: 30 unidades (28 tipo + 2 lazer estimado)

**Registros:**
- Registro de gaveta (RG) 3/4" h=50cm em todos os pontos de água quente

**Fonte:** HID 05_GRR_TIPO; HID 06_GRR_DET TIPO (detalhe isométrico com nota de CPVC obrigatório)

---

### 1.5 QUANTITATIVOS CONSOLIDADOS - ÁGUA

**Pontos de Água Fria:**
- Subsolo: 2 (bomba + TJ estimado)
- Térreo: 1 (TJ lixeira)
- 2° Pavimento: 1 (TJ lavagem)
- 3° Pavimento: 1 (TJ lavagem)
- 4° Lazer: ~10 pontos
- 5° ao 19° (14 tipo): 336 pontos (apartamentos)
- **TOTAL ÁGUA FRIA: ~351 pontos**

**Pontos de Água Quente:**
- 4° Lazer: 2 chuveiros estimado
- 5° ao 19° (14 tipo): 112 pontos (28 aptos × 4)
- **TOTAL ÁGUA QUENTE: ~114 pontos**

**Pontos de Água de Reúso (não potável):**
- Subsolo a 19°: ~19 pontos (TJ por pavimento)
- **TOTAL REÚSO: ~19 pontos**

**Hidrômetros:**
- 1× Predial DN 1 1/2" (20m³/h)
- 30× Individuais 5m³/h (28 tipo + 2 lazer estimado)
- **TOTAL: 31 hidrômetros**

**Aquecedores a gás:**
- **30 unidades** (25L/min cada)

**Metragem Linear Estimada de Tubulações (por tipo/diâmetro):**

*Água Fria (PVC soldável):*
- Ø63mm (alimentação AL-01): ~60m (térreo ao 3°pvto)
- Ø60mm (distribuição gravitacional AF-01): ~180m (barrilete ao 19°)
- Ø50mm (alimentação predial + extravasor): ~30m
- Ø40mm (distribuição): ~40m
- Ø32mm (pressurizadas AF-03 a AF-08 + barriletes aptos): ~600m estimado
- Ø28mm (ramais internos): ~800m estimado
- Ø25mm (ramais): ~1.200m estimado
- Ø22mm (ramais finais): ~1.500m estimado

*Água Quente (CPVC):*
- Ø25mm: ~400m estimado
- Ø22mm: ~600m estimado

*Água de Reúso (PVC):*
- Ø32mm (coluna AR-01): ~60m

**TOTAL ESTIMADO TUBULAÇÕES HIDRÁULICAS: ~5.470m**

---

## 2. SISTEMA SANITÁRIO

### 2.1 DISTRIBUIÇÃO POR PAVIMENTO

#### SUBSOLO
**Pontos de Esgoto:**
- Ralos Ø100mm: 3 unidades
- Tubulação de queda AP-1 Ø100mm (águas pluviais)
- Extravasão para rede pública ou ETE

**Caixas:**
- Caixas de passagem pluvial (concreto + tijolos maciços)

**Destino:** ETE (Estação de Tratamento de Esgoto - ver seção 2.4)

**Fonte:** SAN 02_GRR_SUBSOLO

---

#### TÉRREO
**Pontos de Esgoto:**
- Ralos e pontos de coleta de garagens/áreas comuns
- Caixas de inspeção (CI) alvenaria

**Tubulações:**
- TQ (Tubulação de Queda) Ø100mm
- Coleta horizontal Ø100mm, Ø150mm

**Fonte:** SAN 03_GRR_TÉRREO

---

#### 2° e 3° PAVIMENTOS (Garagens)
**Pontos de Esgoto:**
- Ralos de piso Ø100mm
- TQ Ø100mm (descida)
- CI (caixas de inspeção) conforme projeto

**Fonte:** SAN 04_GRR_2° E 3° PVTO

---

#### 4° PAVIMENTO (LAZER)
**Pontos de Esgoto estimados:**
- 4× Lavatórios (DN 40mm)
- 2× Chuveiros (ralos sifonados DN 50mm)
- 2× Vasos sanitários (DN 100mm)
- 1× Pia cozinha (DN 50mm) → Caixa de Gordura
- 1× Tanque (DN 40mm)
- Ralos de piso (DN 40mm, 50mm)
- **Total estimado: ~12 pontos esgoto**

**Tubulações de Queda:**
- TQ-01, TQ-03, TQ-04, TQ-05, TQ-06 Ø75mm ou Ø100mm (conforme projeto)

**Colunas de Ventilação:**
- CV-01, CV-03, CV-04, CV-06 Ø75mm

**Fonte:** SAN 05_GRR_LAZER

---

#### PAVIMENTO TIPO (5° ao 19°)

**Pontos de Esgoto por apartamento:**

**BWC Suíte:**
- 1× Vaso sanitário (VS) - DN 100mm
- 1× Lavatório (LV) - DN 40mm
- 1× Ralo sifonado chuveiro - DN 50mm
- 1× Ralo linear 90cm (grelha inox) - DN 40mm

**BWC 02:**
- 1× Vaso sanitário (VS) - DN 100mm
- 1× Lavatório (LV) - DN 40mm
- 1× Ralo sifonado chuveiro - DN 50mm
- 1× Ralo linear 90cm (grelha inox) - DN 40mm

**Lavabo:**
- 1× Vaso sanitário (VS) - DN 100mm
- 1× Lavatório (LV) - DN 40mm

**Cozinha:**
- 1× Pia - DN 50mm (interligação 15cm acima do transbordamento)
- Caixa sifonada CS 100×150×50mm

**Área de Serviço:**
- 1× Tanque - DN 40mm
- 1× Máquina lavar roupa - DN 40mm
- Caixa sifonada CS 100×150×50mm
- Ralo linear 90cm (grelha inox) - DN 40mm

**Total por apartamento:** 14 pontos de esgoto

**Total pavimento tipo (2 aptos):** 28 pontos de esgoto

**Total 14 pavimentos tipo:** 392 pontos de esgoto

**Tubulações de Queda (TQ) - por pavimento tipo:**
- TQ-01 Ø100mm (esgoto primário - vasos)
- TQ-03 Ø75mm
- TQ-04 Ø75mm
- TQ-05 Ø75mm
- TQ-06 Ø100mm (esgoto primário)
- TG-01 Ø75mm (tubo de gordura - cozinhas)

**Colunas de Ventilação (CV) - por pavimento tipo:**
- CV-01 Ø75mm
- CV-03 Ø75mm
- CV-04 Ø75mm
- CV-06 Ø75mm

**Caixas Sifonadas:**
- CS 100×150×50mm (múltiplas por apartamento)

**Fonte:** SAN 07_GRR_PVTO TIPO (plantas + detalhes isométricos BWC suíte e BWC 02)

---

#### COBERTURA
**Pontos de Esgoto:**
- Extravasão reservatórios
- Terminais de ventilação (TV) das colunas CV
- Ralos de laje

**Fonte:** SAN 08_GRR_COBERTURA

---

### 2.2 TUBULAÇÕES DE QUEDA E VENTILAÇÃO - CONSOLIDADO

**Tubulações de Queda (TQ) principais:**
- TQ Ø150mm: 1 coluna (esgoto geral - estimado)
- TQ Ø100mm: 6 colunas × 19 pavimentos = ~114m lineares
- TQ Ø75mm: 4 colunas × 19 pavimentos = ~76m lineares
- TG (Tubo Gordura) Ø75mm: 1 coluna × 19 pavimentos = ~19m

**Colunas de Ventilação (CV):**
- CV Ø75mm: 4 colunas × 19 pavimentos = ~76m lineares

**Ramais horizontais (estimativa por diâmetro):**
- DN 40mm: ~2.500m
- DN 50mm: ~1.200m
- DN 75mm: ~400m
- DN 100mm: ~800m
- DN 150mm: ~150m

**TOTAL ESTIMADO TUBULAÇÕES SANITÁRIAS: ~5.335m**

**Fonte:** SAN 01_GRR_LISTAS E DETALHES (lista de materiais consolidada)

---

### 2.3 CAIXAS E ELEMENTOS DE INSPEÇÃO

**Caixa de Gordura Especial (CGE):**
- **Tipo:** Alvenaria (tijolos maciços + concreto + impermeabilização)
- **Dimensionamento:** População 204 indivíduos por caixa
- **Função:** Coleta de mais de 12 cozinhas (30 apartamentos)
- **Volume útil calculado:** 2N + 20 = 2×204 + 20 = 428 litros
- **Dimensões adotadas úteis:** 60 × 113 × 80 cm
- **Volume adotado:** 441 litros
- **Quantidade:** 1 unidade (centralizada - atende todo edifício)
- **Manutenção:** Limpeza a cada 3 meses
- **Destino efluente:** ETE

**Caixas de Inspeção (CI) Alvenaria:**
- Material: Tijolos maciços + tampa concreto + impermeabilização
- Dimensões mínimas: Profundidade ≥60cm, Largura ≥60cm
- Brita nº2 no fundo
- Quantidade: Conforme projeto (múltiplas unidades)

**Caixas de Passagem Pluvial:**
- Material: Concreto + tijolos maciços
- Tampa de concreto
- Localização: Subsolo e térreo

**Caixas Sifonadas (CS):**
- Tipo padrão: 100×150×50mm (PVC)
- Quantidade estimada: ~60 unidades (2 por apartamento × 30 aptos)

**Fonte:** SAN 01_GRR_LISTAS E DETALHES (detalhes construtivos + memorial de cálculo CGE)

---

### 2.4 DESTINO FINAL - ETE (ESTAÇÃO DE TRATAMENTO DE ESGOTO)

**Sistema:** ETE Predial Compacta - Lodos Ativados (Aeróbio)

**Fornecedor:** TW Saneamento (Pinhais/PR)

**Projeto:** Consultoria Ambiental Brazil - Eng. Maria Rosí Melo Rodrigues (CREA/SC 7561/D)

**Vazão dimensionada:** 28,80 m³/dia

**Processo de Tratamento:**

1. **Pré-tratamento (TSS):**
   - Gradeamento (remoção de sólidos grosseiros e materiais flutuantes)
   - Câmara de sedimentação (remoção de areia e sólidos pesados)

2. **Reator Aeróbio - Tanque de Aeração:**
   - Processo: Lodos ativados com aeração convencional
   - Formação de flocos biológicos sedimentáveis

3. **Decantador Secundário:**
   - Separação biomassa (lodo ativado) do efluente tratado
   - Efluente clarificado

4. **Desinfecção - Polimento Final:**
   - Cloração com pastilhas de hipoclorito de cálcio
   - Garantia de qualidade microbiológica conforme padrões legais

**Fluxograma:**
```
Entrada Esgoto → Caixa Gordura (edifício) → Gradeamento/Desarenador → 
Reator Aeróbio → Decantador Secundário → Polimento → Descarte
```

**Manutenção prevista:**
- **Semanal:** Retirar resíduos da grade e caixa de areia, limpar superfície dos tanques
- **Mensal:** Verificar sopradores, válvulas, difusores, sistema de retorno de lodo
- **Trimestral:** Análises laboratoriais, inspeção estrutural e vedação

**Valor:** R$ 178.630,00 (projeto + fornecimento - CIF)

**Prazo de entrega:** 75 dias calendário após sinal

**Observações importantes:**
- NÃO contempla: instalação, interligações hidráulicas, escavação, bases de concreto, descarregamento
- Dimensionamentos: Consultoria Ambiental Brazil

**Fonte:** ORÇAMENTO - TW SANEAMENTO (ORÇ-013/2025, 02/jul/2025)

---

### 2.5 QUANTITATIVOS CONSOLIDADOS - ESGOTO

**Pontos de Esgoto:**
- Subsolo: 3 (ralos)
- Térreo: ~5 estimado
- 2° Pavimento: ~3 estimado
- 3° Pavimento: ~3 estimado
- 4° Lazer: ~12 estimado
- 5° ao 19° (14 tipo): 392 pontos (28 aptos × 14)
- Cobertura: ~3 estimado
- **TOTAL ESGOTO: ~421 pontos**

**Tubulações de Queda (TQ):**
- TQ Ø150mm: 1 coluna
- TQ Ø100mm: 6 colunas
- TQ Ø75mm: 4 colunas
- TG Ø75mm: 1 coluna (gordura)

**Colunas de Ventilação (CV):**
- CV Ø75mm: 4 colunas principais

**Caixas:**
- Caixa de Gordura Especial: 1 unidade (441L)
- Caixas Sifonadas CS 100×150×50mm: ~60 unidades
- Caixas de Inspeção alvenaria: múltiplas conforme projeto

---

## 3. LISTA DE MATERIAIS CONSOLIDADA

### 3.1 CONEXÕES - ESGOTO (Sistema completo)

**Fonte:** SAN 01_GRR_LISTAS E DETALHES

| Descrição | Quantidade |
|-----------|-----------|
| Anel de vedação Série N, 50mm | 1.942 |
| Anel de vedação Série N, 75mm | 539 |
| Anel de vedação Série N, 100mm | 335 |
| Anel de vedação Série N, 150mm | 19 |
| Anel de vedação Vaso Sanitário | 11 |
| Curva 90° Curta 50mm | 22 |
| Curva 90° Curta 75mm | 24 |
| Curva 90° Curta 100mm | 214 |
| Joelho 45° 40mm | 541 |
| Joelho 45° 50mm | 45 |
| Joelho 45° 75mm | 76 |
| Joelho 45° 100mm | 1 |
| Joelho 45° 150mm | 279 |
| Joelho 90° 40mm | 151 |
| Joelho 90° 50mm | 14 |
| Joelho 90° 75mm | 114 |
| Joelho 90° 100mm | 2 |
| Junção Simples 50×50mm | 99 |
| Junção Simples 75×50mm | 95 |
| Junção Simples 100×50mm | 12 |
| Junção Simples 100×75mm | 14 |
| Junção Simples 100×100mm | 783 |
| Luva Simples 50mm | 277 |
| Luva Simples 75mm | 436 |
| Luva Simples 100mm | 1 |
| Luva Simples 150mm | 37 |
| Tê 40×40mm | 1 |
| Tê 50×50mm | 84 |
| Tê 75×50mm | 70 |
| Tê 100×100mm | 86 |

**Marca especificada:** TIGRE (Série Normal)

---

### 3.2 CONEXÕES - ÁGUAS PLUVIAIS

**Fonte:** SAN 01_GRR_LISTAS E DETALHES

| Descrição | Quantidade |
|-----------|-----------|
| Anel de vedação Série N, 75mm | 30 |
| Anel de vedação Série N, 100mm | 335 |
| Anel de vedação Série N, 150mm | 19 |
| Joelho 45° 75mm | 5 |
| Joelho 45° 100mm | 54 |
| Joelho 45° 150mm | 4 |
| Joelho 90° 75mm | 5 |
| Joelho 90° 100mm | 54 |
| Joelho 90° 150mm | 3 |
| Junção Simples 75×75mm | 3 |
| Junção Simples 100×100mm | 37 |
| Junção Simples 150×100mm | 3 |
| Luva Simples 75mm | 13 |
| Luva Simples 100mm | 147 |
| Luva Simples 150mm | 9 |
| Tê 100×75mm | 1 |
| Tê 100×100mm | 1 |

**Marca especificada:** TIGRE (Série Normal)

---

### 3.3 TUBULAÇÕES - TOTAIS ESTIMADOS

**Esgoto Sanitário (PVC Série Normal):**
- Ø40mm: ~2.500m
- Ø50mm: ~1.200m
- Ø75mm: ~400m
- Ø100mm: ~800m
- Ø150mm: ~150m

**Águas Pluviais (PVC Série Normal):**
- Ø75mm: ~50m
- Ø100mm: ~200m
- Ø150mm: ~100m

**Água Fria (PVC Soldável Rígido):**
- Ø22mm: ~1.500m
- Ø25mm: ~1.200m
- Ø28mm: ~800m
- Ø32mm: ~600m
- Ø40mm: ~40m
- Ø50mm: ~30m
- Ø60mm: ~180m
- Ø63mm: ~60m

**Água Quente (CPVC - obrigatório):**
- Ø22mm: ~600m
- Ø25mm: ~400m

**Água de Reúso (PVC):**
- Ø32mm: ~60m

**Sucção/Recalque (PPR PN 12):**
- Ø63mm: ~30m
- Ø50mm: ~20m
- Ø40mm: ~10m

---

### 3.4 REGISTROS E VÁLVULAS

**Registros de Gaveta (RG):**
- RG 3/4": ~350 unidades (distribuídos em todos os pontos AF/AQ/Reúso)
- RG 1": ~30 unidades (tanques)
- RG 1 1/4": 2 unidades (pressurizadores)

**Válvulas de Retenção (VE/VR):**
- VE 1": ~30 unidades (apartamentos)
- VE 1 1/2": 2 unidades (alimentação)
- VE 2": 4 unidades (bombeamento)
- VR Soldável 32mm TIGRE: 30 unidades (apartamentos)
- VR Soldável 60mm TIGRE: 2 unidades (colunas principais)

**Válvulas de Escoamento (VS):**
- VS 3/4": ~90 unidades (vasos sanitários + pontos)

---

### 3.5 EQUIPAMENTOS PRINCIPAIS

**Bombeamento e Pressurização:**
- 2× Motobombas de recalque (7,9 m³/h, 73,83 mca) - ativa + reserva
- 2× Pressurizadores (2,41 m³/h, 20 mca cada)
- 1× Pressurizador sistema pluvial
- Quadros elétricos com relé biestável

**Aquecimento:**
- 30× Aquecedores de passagem a gás 25L/min

**Medição:**
- 1× Hidrômetro predial DN 1 1/2" (Qmax 20m³/h)
- 30× Hidrômetros individuais 5m³/h (VN 2,5m³/h)

**Tratamento:**
- 1× ETE Compacta 28,80 m³/dia (TW Saneamento)
- 1× Filtro VF1 Ecco AcquaSave (sistema pluvial)
- 1× Realimentador automático reservatório

**Reservatórios:**
- 2× Fortlev 15.000L (cobertura)
- 1× Fortlev 5.000L (subsolo - pluvial)
- 2× Células concreto armado impermeabilizado (3° pvto)

---

## 4. ESPECIFICAÇÕES TÉCNICAS E NORMAS

### 4.1 Normas de Referência
- **NBR 5626** - Sistemas prediais de água fria
- **NBR 8160** - Sistemas prediais de esgoto sanitário
- **NBR 10844** - Instalações prediais de águas pluviais
- **NBR 15575** - Edificações habitacionais - Desempenho
- **NBR 6493** - Identificação de tubulações (cores)

### 4.2 Inclinações de Projeto
**Água Potável (no sentido da seta):** 0,5%

**Esgoto e Águas Pluviais (no sentido da seta):**
- PVC Ø250mm e Ø200mm: 0,5%
- PVC Ø150mm, Ø100mm: 1,0%
- PVC Ø75mm, Ø50mm, Ø40mm, Ø20mm: 2,0%

### 4.3 Espaçamento Entre Suportes - Tubulação Sanitária Horizontal
- Ø40mm: Suportes a cada 40cm
- Ø50mm: Suportes a cada 50cm
- Ø100mm: Suportes a cada 100cm
- Ø150mm: Suportes a cada 150cm

**Tubulação Vertical:** Suporte (braçadeira) a cada 2 metros

### 4.4 Pressões de Projeto
- **Pressão máxima estática nos pontos:** ≤ 400 kPa (40 mca) - NBR 5626
- **Pressão zona pressurizada:** 25 mca (inversor de frequência)
- **Pressão zona gravitacional:** 12,60 a 35,66 mca
- **Pressão jusante ERP (9° pvto):** 20,37 mca
- **Velocidade máxima flúido:** ≤ 10 m/s - NBR 5626

### 4.5 Materiais Obrigatórios
- **Água quente (saída aquecedor):** CPVC (resistência térmica)
- **Sucção/recalque bombas:** PPR PN 12
- **Esgoto e pluvial:** PVC Série Normal TIGRE
- **Água fria:** PVC Soldável Rígido

### 4.6 Vida Útil de Projeto
**20 anos** (conforme NBR 15575), considerando:
- Periodicidade correta de manutenção
- Execução adequada dos processos

---

## 5. OBSERVAÇÕES IMPORTANTES DE PROJETO

### 5.1 Sistema Hidráulico
1. Alimentação reservatório inferior dimensionada para abastecimento em até 6h (consumo diário)
2. Alimentação reservatório superior dimensionada para abastecimento em até 6h + atenuação golpe de aríete
3. Filtro de linha previsto nas redes de consumo (proteção equipamentos pós-reservatório)
4. Barrilete com registros para individualizar células dos reservatórios
5. Simultaneidade água quente conforme briefing técnico com proprietário
6. Projeto dimensionado para chuva 5 min / período retorno 25 anos (NBR 10844)

### 5.2 Sistema Sanitário
7. Sistema projetado para não permitir autossifonagem ou quebra de fecho hídrico
8. Caixa de Gordura Especial: limpeza a cada 3 meses (apartamentos)
9. ETE e caixas do sistema: limpeza a cada 1 ano
10. Terminais de ventilação: tê ou dispositivo anti-pluvial obrigatório
11. Passagens em lajes/paredes com fita intumescente (tubos Ø40 a Ø150mm) + argamassa corta-fogo
12. Envelopamento de tubos em contato com elementos construtivos (redução ruídos/vibrações)

### 5.3 Execução
13. Execução sob supervisão de profissional habilitado (obrigatório)
14. Ensaios de estanqueidade: água (15 min, 60 kPa) ou ar (15 min, 35 kPa)
15. Ensaio final com fumaça (após colocação aparelhos) - 15 min, 0,25 kPa
16. As Built obrigatório ao término da execução
17. Qualquer alteração no projeto: consultar projetista previamente

---

## 6. RASTREABILIDADE DAS INFORMAÇÕES

### Pranchas Hidráulicas
- **HID 01** - Subsolo (bombeamento, cisterna)
- **HID 02** - Térreo (hidrômetro predial, alimentação)
- **HID 03** - 2° e 3° Pavimentos (garagens)
- **HID 04** - Lazer (pontos comuns)
- **HID 05** - Tipo (planta, pontos AF/AQ)
- **HID 06** - Detalhes Tipo (isométricos, aquecedor)
- **HID 07** - Corte Esquemático (zonas de pressão, bombeamento vertical)
- **HID 08** - Cobertura e Reservatório (pressurizadores, bypass)

### Pranchas Sanitárias - Executivo
- **SAN 01** - Listas e Detalhes (quantitativos, especificações, memorial)
- **SAN 02** - Subsolo (ralos, AP)
- **SAN 03** - Térreo (caixas inspeção)
- **SAN 04** - 2° e 3° Pavimentos (esgoto garagens)
- **SAN 05** - Lazer (esgoto áreas comuns)
- **SAN 06** - 5° Pavimento (primeiro tipo)
- **SAN 07** - Pavimento Tipo (detalhes BWC, isométricos)
- **SAN 08** - Cobertura (terminais ventilação)

### Pranchas Sanitárias - Aprovativo
- **Pranchas 01 a 04** - Aprovação concessionária/prefeitura

### Orçamento ETE
- **ORÇAMENTO TW SANEAMENTO** - ORÇ-013/2025 (02/jul/2025)

---

## 7. RESUMO EXECUTIVO

### Características Principais

**Água Fria:**
- Sistema misto: gravitacional (10° a 14°) + pressurizado (5° a 19°)
- Reservação total: 65 m³ (30m³ superior + 30m³ inferior + 5m³ pluvial)
- Bombeamento: 7,9 m³/h, 73,83 mca
- Pressurização: 2× 2,41 m³/h, 25 mca
- ~351 pontos

**Água Quente:**
- Aquecedores individuais a gás (30× 25L/min)
- Tubulação CPVC obrigatória
- ~114 pontos

**Água de Reúso:**
- Cisterna 5m³ + realimentador automático
- Distribuição vertical pressurizada
- ~19 pontos (uso não potável - sinalizado)

**Esgoto Sanitário:**
- Sistema separador absoluto
- Caixa Gordura Especial centralizada (441L)
- ETE Compacta 28,80 m³/dia (lodos ativados)
- 6 TQ principais (Ø75 a Ø150mm)
- 4 CV (Ø75mm)
- ~421 pontos

**Totais Consolidados:**
- **Pontos:** 905 (351 AF + 114 AQ + 19 reúso + 421 esgoto)
- **Tubulações:** ~10.805m lineares (5.470m hidráulico + 5.335m sanitário)
- **Aquecedores:** 30 unidades (25L/min)
- **Hidrômetros:** 31 (1 predial + 30 individuais)
- **ETE:** 1 unidade (28,80 m³/dia)

---

**Análise elaborada em:** 15 de março de 2026  
**Responsável técnico projeto:** Eng. Gabriel Gustavo Fabro Haas (CREA SC 126.031-9)  
**Projetista sanitário:** Giovana P. (CREA SC 126.031-9)  
**Projetista hidráulico:** Fabiane D.  
**Projeto ETE:** Eng. Maria Rosí Melo Rodrigues (CREA/SC 7561/D) - Consultoria Ambiental Brazil

---

**FIM DA ANÁLISE ONDA 3 - HIDROSSANITÁRIO**
