# Regras de Negócio — Orçamento Paramétrico
## Bloco 01: Dados Iniciais, Movimentação de Terra, Contenções e Infraestrutura

---

## 1. Aba OBRA — Cadastro do Empreendimento

### Função
Aba de **entrada de dados brutos** do empreendimento. Não faz cálculos paramétricos — serve como fonte primária de onde todas as outras abas puxam informações.

### Dados Cadastrados
- **Projeto**, **Empresa**, **Revisão**, **Endereço/CNPJ**
- **Prazo de Obra** (meses)
- **Área do Terreno** (m²)
- **Nº Elevadores**, **Nº Subsolos**

### Dados Calculados (agregações)
| Variável | Regra de Cálculo |
|----------|-----------------|
| Área Construída | Soma das áreas de todos os pavimentos (coluna D, linhas 21-39) |
| Área Privativa | Soma das áreas privativas de todos os pavimentos (coluna E, linhas 21-38) |
| Área de Lazer | Valor fixo ou calculado manualmente |
| Área Comercial | Soma das áreas privativas das unidades comerciais (linhas 54-59) |
| Nº Pavimentos | Contagem dos pavimentos preenchidos (COUNTA) |
| Nº Unidades Residenciais | Soma da coluna "Nº Unidades" (O21:O39) |
| Total de Dormitórios | Soma da coluna "Quartos" (J20:J39) |
| Nº Banheiros | Soma da coluna "Banheiros" (H20:H39) |
| Nº Churrasqueiras | Soma da coluna "Churrasqueiras" (I20:I39) |
| Nº Vagas | Calculado manualmente |

### Tabela Pavimento-a-Pavimento
Para cada pavimento, registra:
- Torre, Nome do pavimento, Área total, Área privativa, Perímetro, Pé-direito
- Nº de Banheiros, Churrasqueiras, Quartos, Ventokits, Pontos de AR, Equipamentos AR, Ralos, Nº Unidades

**Regra importante:** Pavimentos tipo repetem os mesmos dados por fórmula (ex: banheiros = 3×3+2 = 11 por pavimento tipo).

---

## 2. Aba DADOS_INICIAIS — Dicionário de Variáveis

### Função
Aba de **tradução e consolidação**. Puxa dados da aba Obra e atribui **identificadores curtos** (siglas) usados por todas as abas de cálculo. É o "dicionário de variáveis" do orçamento.

### Variáveis Definidas

| Identificador | Descrição | Unidade | Origem |
|---------------|-----------|---------|--------|
| **AT** | Área do Terreno | m² | Obra!C8 |
| **AC** | Área Total Construída | m² | Obra!C10 (soma áreas pavimentos) |
| **UR** | Unidades Residenciais | un | Obra!F6 |
| **dorm** | Dormitórios | un | Obra!F12 |
| **ban** | Banheiros | un | Obra!C18 |
| **UC** | Unidades Comerciais | un | Obra!F8 |
| **CHU** | Churrasqueiras | un | Obra!F18 |
| **NP** | Nº Total de Pavimentos | un | Obra!F10 |
| **NPT** | Nº Pavimentos Tipo | un | Contagem (COUNTA) dos tipos |
| **NPD** | Nº Pavimentos Tipo Diferenciados | un | Manual |
| **ND** | Nº Pavimentos Duplex | un | Manual |
| **APT** | Área de Projeção da Torre | m² | Obra!D24 (área do 1º tipo) |
| **PPT** | Perímetro de Projeção da Torre | m | Obra!F24 |
| **AL** | Área de Lazer | m² | Obra!C14 |
| **AE** | Área do Embasamento | m² | Obra!D22 (área do pav. garagem) |
| **S** | Área de Subsolos | m² | Obra!D21 (área do térreo/subsolo) |
| **NS** | Nº de Subsolos | un | Manual |
| **APE** | Área de Projeção do Embasamento | m² | = AE (mesma área do embasamento) |
| **PE** | Perímetro de Projeção do Embasamento | m | Obra!F22 |
| **NE** | Nº Pavimentos de Embasamento | un | Manual |

### Regra Geral
> Toda variável de entrada usada em abas de cálculo deve ter seu identificador definido aqui. As abas de serviço referenciam `DADOS_INICIAIS!E<linha>`, nunca a aba Obra diretamente.

### Variáveis-Chave Mais Usadas
As variáveis mais referenciadas pelas abas de cálculo são:
- **APE** (Área de Projeção do Embasamento) — base para fundações, contenções, valas
- **AC** (Área Construída) — base para rateio R$/m² total
- **S** (Área de Subsolos) — base para escavação vertical

---

## 3. Aba MOVIMENTAÇÃO DE TERRA

### Função
Calcula volumes e custos de escavação, rebaixamento de lençol freático, reaterro e regularização do terreno.

### Seção 3.1 — Escavação Vertical de Subsolo

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de subsolo (m²) | DADOS_INICIAIS!E23 → **S** |
| Altura do subsolo (m) | Entrada manual (coluna C) |

#### Regra de Cálculo
```
Volume de escavação = Área de subsolo × Altura do subsolo
```

#### Fator de Custo
```
Valor total = Preço unitário (R$/m³) × Volume × 1.1 (BDI)
```

#### Observações
- Preço unitário zerado no exemplo — indica que pode não se aplicar à obra ou será preenchido depois.

---

### Seção 3.2 — Rebaixamento de Lençol Freático

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Duração (dias) | Calculado: meses × 30 dias |

#### Regra de Cálculo
```
Quantidade = Nº de meses × 30 (dias por mês)
```

#### Fator de Custo
```
Valor total = Quantidade (dias) × Preço unitário (R$/dia) × 1.1 (BDI)
```

#### Observações
- A duração é definida em meses na observação (ex: "4 meses") e convertida em dias na fórmula.

---

### Seção 3.3 — Escavação e Reaterro de Valas

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Volume de infraestrutura (concreto fundação rasa) | INFRAESTRUTURA!D29 |
| Volume de concreto das estacas | INFRAESTRUTURA!D19 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Escavação mecanizada (blocos/baldrames) | 1.3 | m³/Vol infra | Para cada m³ de concreto de fundação rasa, escava-se 1.3 m³ |
| Reaterro (blocos/baldrames) | — | m³/Vol Escavação | Volume reaterrado = Volume escavado − Volume de concreto |
| Bota-fora | 1.3 | — | Fator de empolamento: solo escavado expande 30% |
| Terra das estacas | 1.0 | m³ | Volume = volume de concreto das estacas (1:1) |

#### Regras de Cálculo
```
Escavação mecanizada = 1.3 × Volume de concreto da fundação rasa
Reaterro = Volume escavado − Volume de concreto da fundação rasa
Bota-fora = (Volume escavado − Volume reaterrado) × 1.3 (empolamento)
Terra das estacas = Volume de concreto das estacas (INFRAESTRUTURA!D19)
```

#### Fator de Custo
```
Valor total = Preço unitário (R$/m³) × Volume × 1.1 (BDI)
```

#### Referências Cruzadas
- **INFRAESTRUTURA!D29** → Volume de concreto da fundação rasa (blocos e baldrames)
- **INFRAESTRUTURA!D19** → Volume de concreto das estacas (fundação profunda)

---

### Seção 3.4 — Regularização e Apiloamento de Fundo de Valas

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de Projeção do Embasamento (APE) | DADOS_INICIAIS!E25 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Lastro de concreto magro (e=5cm) | 0.8 | m²/APE | 80% da projeção do embasamento recebe lastro |

#### Regra de Cálculo
```
Área de lastro = 0.8 × Área de Projeção do Embasamento (APE)
```

#### Fator de Custo
```
Preço unitário = 370 × 0.1 = R$ 37,00/m² (custo do concreto magro e=5cm)
Valor total = Preço unitário × Área de lastro × 1.1 (BDI)
```

#### Indicador de Controle
```
Custo por m² de embasamento = Valor total / APE
```

#### Observações
- Nota: "Definição trazida do Celebration da Passe" — indica que o índice 0.8 foi calibrado a partir de obra de referência.

---

### Total Movimentação de Terra
```
Total = Escavação Vertical + Rebaixamento + Escavação/Reaterro de Valas + Regularização
```
**Indicador:** R$/m² de área construída = Total / AC

---

## 4. Aba CONTENÇÕES

### Função
Calcula custos de contenção do terreno: cortina de estacas, parede de concreto e parede diafragma. A aba calcula apenas cortina + parede de concreto no total (parede diafragma referencia dado inexistente — DADOS_INICIAIS!E35 — provavelmente uma alternativa não ativada).

### Seção 4.1 — Cortina de Estacas

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de Projeção do Embasamento (APE) | DADOS_INICIAIS!E25 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Nº total de estacas | 0.15 | un/APE | Para cada m² de projeção, 0.15 estacas |
| Estaca Ø40 | 0.1 | proporção | 10% das estacas são diâmetro 40 |
| Estaca Ø50 | 0.5 | proporção | 50% das estacas são diâmetro 50 |
| Estaca Ø60 | 0.4 | proporção | 40% das estacas são diâmetro 60 |
| Profundidade (todas) | 20 | m/un | Cada estaca tem 20m de profundidade |
| Armação 6,3mm | 1.66 | kg/m³ | Taxa de aço fino por m³ de concreto |
| Armação 16mm | 10.18 | kg/m³ | Taxa de aço grosso por m³ de concreto |

#### Regras de Cálculo
```
Nº total de estacas = 0.15 × APE
Estacas Ø40 = 10% × Nº total
Estacas Ø50 = 50% × Nº total
Estacas Ø60 = 40% × Nº total

Metragem linear (cada diâmetro) = Nº estacas do diâmetro × 20m

Volume de concreto = Σ (π × D²/4 × Metragem linear) para cada diâmetro
  → Soma das seções circulares × comprimento de cada grupo

Armação 6,3mm = 1.66 kg/m³ × Volume concreto
Armação 16mm = 10.18 kg/m³ × Volume concreto
```

#### Fator de Custo
```
Valor total (por item) = Preço unitário × Quantidade
```
**Nota:** Nesta aba NÃO aparece o fator ×1.1 (BDI) nas fórmulas de valor — diferente das demais abas. Pode indicar que os preços já incluem BDI, ou que a aba está incompleta.

#### Observações
- Mobilização é verba fixa (1 vb).
- A distribuição percentual dos diâmetros (10/50/40) é o parâmetro-chave — define a cortina.

---

### Seção 4.2 — Parede de Concreto (Muro de Arrimo / Contenção)

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de Projeção do Embasamento (APE) | DADOS_INICIAIS!E25 |
| Custo de mão de obra (referência) | SUPRAESTRUTURA!B15 × 1.5 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Forma (resinado) | 2.1 | m²/APE | 2.1 m² de forma para cada m² de projeção |
| Concreto | 0.65 | m³/APE | 0.65 m³ de concreto para cada m² de projeção |
| Armação | 110 | kg/m³ | 110 kg de aço para cada m³ de concreto |
| Mão de obra | — | R$/APE | Custo da supraestrutura × 1.5 (fator de dificuldade contenção) |

#### Regras de Cálculo
```
Forma = 2.1 × APE
Concreto = 0.65 × APE
Armação = 110 kg/m³ × Volume de concreto
Mão de obra = Custo unitário supraestrutura × 1.5 × APE
```

#### Fator de Custo
```
Valor total = Preço unitário × Quantidade
```
**Nota sobre mão de obra:** O preço unitário da mão de obra é puxado da aba SUPRAESTRUTURA (custo de mão de obra da estrutura) multiplicado por 1.5. Isso reflete que a execução de contenção é ~50% mais cara que a estrutura convencional.

---

### Seção 4.3 — Parede Diafragma (Alternativa)

#### Estrutura
Mesmos índices da Parede de Concreto (forma 2.1, concreto 0.65, armação 110 kg/m³), mas referencia **DADOS_INICIAIS!E35** que não existe na aba de dados — provavelmente uma variável para obra com parede diafragma que não foi ativada neste caso.

#### Mão de Obra
Referencia `SUPRAESTRUTURA!B84 × 1.5` (posição diferente na supraestrutura).

---

### Total Contenções
```
Total = Cortina de Estacas + Parede de Concreto
```
**Indicador:** R$/m² de área construída = Total / AC

**Nota:** A Parede Diafragma (seção 4.3) NÃO é somada no total — é alternativa à Cortina de Estacas.

---

## 5. Aba INFRAESTRUTURA

### Função
Calcula custos de fundação profunda (estacas) e fundação rasa (blocos, baldrames e piso).

### Seção 5.1 — Fundação Profunda (Estacas)

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de Projeção do Embasamento (APE) | DADOS_INICIAIS!E25 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Nº total de estacas | 0.14 | un/APE | Para cada m² de projeção, 0.14 estacas |
| Estaca Ø40 | 0 | proporção | 0% (não utilizado nesta obra) |
| Estaca Ø50 | 0.6 | proporção | 60% das estacas são diâmetro 50 |
| Estaca Ø60 | 0.4 | proporção | 40% das estacas são diâmetro 60 |
| Estaca Ø80 | 0 | proporção | 0% (não utilizado nesta obra) |
| Profundidade (todas) | 28 | m/un | Cada estaca tem 28m de profundidade |
| Fator de perda (concreto) | 1.3 | perda | 30% de perda no concreto das estacas |
| Armação | 12 | kg/m³ | 12 kg de aço por m³ de concreto |

#### Regras de Cálculo
```
Nº total de estacas = ROUNDUP(0.14 × APE)  ← arredonda pra cima (estacas inteiras)
Estacas por diâmetro = ROUNDUP(proporção × Nº total)

Metragem linear = Nº estacas × Profundidade (28m)

Volume de concreto = Σ (π × D²/4 × Metragem linear) para cada diâmetro
  → Volume teórico das seções circulares

Preço unitário concreto = (Custo concreto + Bomba + Aditivo) × 1.3 (perda)
  → Composição: (535 + 45 + 1.67×0.6) × 1.3

Armação = 12 kg/m³ × Volume de concreto
```

#### Fator de Custo
```
Valor total = Preço unitário × Quantidade × 1.1 (BDI)
```

**Exceção:** Apoio e arrasamento de estacas usa fator ×1.0 (sem BDI) — serviço de canteiro incluído no preço.

#### Observações
- Nota "Índice Passione" — indica que o parâmetro 0.14 un/APE foi calibrado a partir da obra Passione (obra de referência).
- A profundidade de 28m é padrão para todas as estacas (mesmo campo B14 replicado para Ø60 e Ø80).
- O ROUNDUP garante que o nº de estacas é sempre inteiro (arredondamento para cima).
- Diâmetros Ø40 e Ø80 existem na estrutura mas estão zerados — a planilha suporta 4 diâmetros, ativa-se conforme a obra.

---

### Seção 5.2 — Fundação Rasa (Blocos, Baldrames e Piso)

#### Variáveis de Entrada
| Variável | Origem |
|----------|--------|
| Área de Projeção do Embasamento (APE) | DADOS_INICIAIS!E25 |
| Custo de mão de obra (referência) | SUPRAESTRUTURA!B43 × 1.5 |

#### Índices Paramétricos

| Serviço | Parâmetro | Unidade | Significado |
|---------|-----------|---------|-------------|
| Forma (resinado) | 1.1 | m²/APE | 1.1 m² de forma para cada m² de projeção |
| Concreto (40 MPa) | 0.6 | m³/APE | 0.6 m³ de concreto para cada m² de projeção |
| Armação | 70 | kg/m³ | 70 kg de aço para cada m³ de concreto |
| Piso de concreto armado | 1.0 | m²/APE | 100% da área de projeção recebe piso |
| Mão de obra | — | R$/APE | Custo supraestrutura × 1.5 |

#### Regras de Cálculo
```
Forma = 1.1 × APE
Concreto = 0.6 × APE
Armação = 70 kg/m³ × Volume de concreto
Piso = 1.0 × APE (área total de projeção)
Mão de obra = Custo unitário supraestrutura × 1.5 × APE
```

#### Composição do Preço do Concreto
```
Preço unitário = (535 + 45 + 1.67 × 0.6) × 1.05
                  ↑concreto ↑bomba ↑aditivo      ↑5% perda
```
**Nota:** Na fundação rasa, a perda do concreto é 5% (×1.05), menor que nas estacas (30% / ×1.3).

#### Composição do Preço do Piso
O preço unitário do piso é calculado como composição interna:
```
Custo piso/m² = (Concreto × 0.12) + (Armação × índice_armação) + (Forma × índice_forma)
```
Onde os índices 0.12 m³/m² de concreto, 110×0.12 kg de armação e 1×0.12 m² de forma representam o consumo por m² de piso.

#### Fator de Custo
```
Valor total = Preço unitário × Quantidade × 1.1 (BDI)
```

#### Observações
- Nota "Indice do Passione" no concreto — mesma obra de referência da fundação profunda.
- Mão de obra puxa da SUPRAESTRUTURA (B43) com fator ×1.5, igual à contenção.

---

### Total Infraestrutura
```
Total = Fundação Profunda + Fundação Rasa
```

**Indicadores:**
- R$/m² de área construída (com BDI) = Total / AC
- R$/m² de área construída (sem BDI) = (Total / AC) / 1.1

---

## 6. Padrões e Regras Transversais

### 6.1 — Padrão de Cálculo Paramétrico
Todas as abas seguem o mesmo modelo:
```
Quantidade = Índice Paramétrico × Variável de Entrada (da aba DADOS_INICIAIS)
Valor Total = Quantidade × Preço Unitário × BDI (1.1)
```

### 6.2 — BDI (Benefícios e Despesas Indiretas)
- **Fator padrão: 1.1 (10%)** — aplicado multiplicando o valor (Preço × Quantidade) por 1.1
- Presente em quase todas as fórmulas de valor total
- **Exceção:** Apoio e arrasamento de estacas (INFRAESTRUTURA linha 22) usa fator 1.0
- **Exceção:** Aba CONTENÇÕES não aplica BDI explícito (pode estar embutido nos preços)

### 6.3 — Fatores de Perda
- **Concreto estacas (fundação profunda):** 1.3 (30% de perda) — aplicado no preço unitário
- **Concreto blocos/baldrames (fundação rasa):** 1.05 (5% de perda) — aplicado no preço unitário
- **Empolamento de terra (bota-fora):** 1.3 (30% de expansão) — aplicado no volume

### 6.4 — Fator de Dificuldade de Mão de Obra
- **Contenção e Infraestrutura:** Custo de mão de obra = Custo da supraestrutura × **1.5**
- Reflete maior complexidade/dificuldade de execução em fundações e contenções vs. estrutura convencional

### 6.5 — Variável Dominante: APE
A **Área de Projeção do Embasamento (APE)** é a variável mais influente nestas abas:
- Nº de estacas (fundação e contenção) = f(APE)
- Volumes de concreto de fundação rasa = f(APE)
- Áreas de forma = f(APE)
- Área de lastro = f(APE)
- Volumes de escavação de valas = f(Volume concreto) = f(APE)

### 6.6 — Referências Cruzadas Entre Abas

```
OBRA → DADOS_INICIAIS → INFRAESTRUTURA → MOVIMENTAÇÃO DE TERRA
                      → CONTENÇÕES
                      → (SUPRAESTRUTURA — referenciada mas não analisada)
```

| De | Para | Dado |
|----|------|------|
| Obra | DADOS_INICIAIS | Todas as variáveis de entrada |
| DADOS_INICIAIS | INFRAESTRUTURA | APE (E25), AC (E9) |
| DADOS_INICIAIS | CONTENÇÕES | APE (E25), AC (E9) |
| DADOS_INICIAIS | MOVIMENTAÇÃO DE TERRA | S (E23), APE (E25), AC (E9) |
| INFRAESTRUTURA | MOVIMENTAÇÃO DE TERRA | Volume concreto estacas (D19), Volume concreto fund. rasa (D29) |
| SUPRAESTRUTURA | INFRAESTRUTURA | Custo mão de obra (B43) |
| SUPRAESTRUTURA | CONTENÇÕES | Custo mão de obra (B15, B84) |

### 6.7 — Indicador de Controle (R$/m²)
Todas as abas calculam um indicador final:
```
Custo por m² = Total da aba / Área Construída (AC)
```
Isso permite comparar o custo paramétrico com benchmarks de mercado e obras anteriores.

### 6.8 — Calibração por Obras de Referência
Os índices paramétricos são calibrados a partir de obras reais:
- **"Índice Passione"** — obra Passione (estacas, concreto fundação)
- **"Definição do Celebration da Passe"** — obra Celebration (lastro)
- Esses nomes nas observações documentam a origem dos parâmetros para rastreabilidade.

---

## 7. Resumo dos Índices Paramétricos Principais

| Aba | Serviço | Índice | Unidade | Base |
|-----|---------|--------|---------|------|
| INFRA | Nº estacas (fundação) | 0.14 | un/m² | APE |
| INFRA | Forma blocos/baldrames | 1.1 | m²/m² | APE |
| INFRA | Concreto blocos/baldrames | 0.6 | m³/m² | APE |
| INFRA | Armação blocos/baldrames | 70 | kg/m³ | Vol. concreto |
| INFRA | Armação estacas | 12 | kg/m³ | Vol. concreto |
| INFRA | Piso concreto armado | 1.0 | m²/m² | APE |
| CONTENÇÃO | Nº estacas (cortina) | 0.15 | un/m² | APE |
| CONTENÇÃO | Forma parede | 2.1 | m²/m² | APE |
| CONTENÇÃO | Concreto parede | 0.65 | m³/m² | APE |
| CONTENÇÃO | Armação parede | 110 | kg/m³ | Vol. concreto |
| MOV. TERRA | Escavação valas | 1.3 | m³/m³ | Vol. infra |
| MOV. TERRA | Empolamento bota-fora | 1.3 | fator | Vol. líquido |
| MOV. TERRA | Lastro concreto magro | 0.8 | m²/m² | APE |

---

*Documento gerado em 04/03/2026 — Análise das abas Obra, DADOS_INICIAIS, MOVIMENTAÇÃO DE TERRA, CONTENÇÕES e INFRAESTRUTURA.*
