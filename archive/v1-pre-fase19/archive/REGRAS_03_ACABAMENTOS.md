# REGRAS DE NEGÓCIO — Grupo 03: Acabamentos, Revestimentos, Esquadrias e Complementares

> Documento gerado a partir da análise das abas: Rev. Internos Piso e Parede, TETO, Acabamentos de Piso e Parede, PINTURA INTERNA, ESQUADRIAS, COBERTURA, Rev. Fachada, COMPLEMENTARES.

---

## Glossário de Variáveis de Entrada (DADOS_INICIAIS)

| Identificador | Descrição | Unidade |
|---|---|---|
| AC (E9) | Área Total Construída | m² |
| UR (E10) | Unidades Residenciais | un |
| NP (E15) | Número Total de Pavimentos | un |
| AL (E21) | Área de Lazer | m² |
| APT (E19) | Área de Projeção da Torre | m² |
| PPT (E20) | Perímetro de Projeção da Torre | m |

---

## 1. REVESTIMENTOS INTERNOS DE PISO E PAREDE

### 1.1 Variáveis de Entrada
- **AC** — Área Total Construída (base para índices paramétricos)
- **Área de alvenaria interna** — importada da aba ALVENARIA (área total de paredes internas)
- **Área de chapisco de fachada** — importada da aba Rev. Fachada (para desconto)
- **Áreas específicas por pavimento** — calculadas individualmente (com deduções de áreas molhadas e técnicas)

### 1.2 Índices Paramétricos
| Serviço | Unidade do Índice | Lógica |
|---|---|---|
| Contrapiso | m² / AC | Índice calculado = área de contrapiso ÷ AC |
| Manta acústica | m² / AC | Índice calculado = área de manta ÷ AC |
| Chapisco interno | m² / AC | Índice calculado = área de chapisco ÷ AC |
| Reboco interno | m² / AC | Índice calculado = área de reboco ÷ AC |
| Polimento de concreto | m² (absoluto) | Quantidade direta por pavimento, com deduções |
| Piso alisado | m² (absoluto) | Quantidade direta (ex: áreas técnicas × nº pavimentos) |

### 1.3 Regras de Cálculo

1. **Contrapiso:**
   - Quantidade = somatório das áreas de piso por pavimento, com deduções de áreas molhadas/técnicas (banheiros, sacadas, halls)
   - O índice paramétrico é derivado: `índice = quantidade_contrapiso ÷ AC`
   - Existe referência a um fator ~0.62 × AC (desabilitado com `*0`), sugerindo que o índice típico gira em torno de **0.60 a 0.65 m²/AC**

2. **Manta acústica:**
   - `Área de manta = Área de contrapiso × 0.80`
   - Regra: manta acústica cobre 80% da área de contrapiso (exclui áreas molhadas, halls, etc.)

3. **Chapisco interno:**
   - `Área de chapisco = (Área total de alvenaria × 2) − Área de chapisco de fachada`
   - Lógica: área de alvenaria conta os dois lados da parede (×2), depois desconta a fachada (que tem chapisco próprio)

4. **Reboco interno:**
   - `Área de reboco = Área de chapisco interno` (mesma quantidade, 1:1)

5. **Polimento de concreto:**
   - Quantidade calculada por pavimento com deduções individuais (áreas molhadas, circulações técnicas)
   - Preço unitário fixo (R$/m²)

6. **Piso alisado:**
   - Quantidade = área unitária × número de pavimentos (tipicamente áreas técnicas como halls de escada)

### 1.4 Fatores de Custo
- **BDI = 1.1** (10%) — aplicado a TODOS os itens: `Valor = Quantidade × Preço Unitário × 1.1`
- Preços unitários fixos por tipo de serviço (R$/m²)
- Referência de preço: "Média" (cotação de mercado)

### 1.5 Indicador de Totalização
- `Custo por m² de AC = Total da aba ÷ AC`
- `Custo por m² de AC sem BDI = (Total ÷ AC) ÷ 1.1`

### 1.6 Observações
- As deduções por pavimento são específicas de cada projeto (áreas molhadas, sacadas, halls variam conforme arquitetura)
- O contrapiso é a "âncora" de vários outros serviços: manta acústica e acabamentos de piso referenciam sua quantidade
- O chapisco interno depende de duas outras abas (ALVENARIA e Rev. Fachada), criando uma **cadeia de dependências**

---

## 2. REVESTIMENTOS E ACABAMENTOS DE TETO

### 2.1 Variáveis de Entrada
- **AC** — Área Total Construída (base do índice)

### 2.2 Índices Paramétricos
| Serviço | Índice | Unidade |
|---|---|---|
| Forro gesso acartonado ST | 0.6 | m² / AC |
| Forro gesso acartonado RU | 0.6 | m² / AC |
| Forro gesso mineral | 0.6 | m² / AC |
| Negativo | 1.2 | m / FORRO |
| Estucamento | 0.2 | m² / AC |

### 2.3 Regras de Cálculo

1. **Índice base de forro = 0.6 m²/AC** — todos os tipos de forro usam o mesmo índice paramétrico

2. **Distribuição por tipo de forro (pesos):**
   - `Forro ST = 0.6 × AC × peso_ST`
   - `Forro RU = 0.6 × AC × peso_RU`
   - `Forro mineral = 0.6 × AC × peso_mineral`
   - Onde os pesos somam 1.0 (ex: 80% ST + 20% RU + 0% mineral)
   - **Regra genérica:** o orçamentista define a proporção entre tipos de forro conforme projeto

3. **Negativo (moldura/sanca):**
   - `Negativo = Área de forro mineral × 1.2 m/m²`
   - Só se aplica ao forro mineral (quando houver). Relação: 1.2 metros lineares por m² de forro

4. **Estucamento (laje aparente):**
   - Quantidade calculada individualmente por pavimento (áreas que ficam com laje aparente sem forro)
   - Índice de referência: ~0.2 m²/AC

### 2.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens
- Fórmula padrão: `Valor = Preço Unitário × Quantidade × 1.1`

### 2.5 Observações
- O índice 0.6 m²/AC para forro é um **padrão paramétrico** que indica que ~60% da AC recebe algum tipo de forro
- A escolha do tipo de forro (ST, RU, mineral) é decisão de projeto — o modelo permite ajustar os pesos
- Estucamento é complementar ao forro: onde não tem forro, tem estucamento (laje aparente tratada)

---

## 3. ACABAMENTOS DE PISO E PAREDE

### 3.1 Variáveis de Entrada
- **AC** — Área Total Construída (para itens com índice R$/AC)
- **Área de contrapiso** — importada da aba Rev. Internos Piso e Parede (define área de porcelanato interno)

### 3.2 Índices Paramétricos
| Serviço | Índice | Unidade | Observação |
|---|---|---|---|
| Rodapés | 30 | R$ / AC | Verba por m² de AC |
| Soleiras e peitoris | 20 | R$ / AC | Verba por m² de AC |
| Revestimentos de parede | 45 | R$ / AC | Verba por m² de AC |

### 3.3 Regras de Cálculo

1. **Porcelanato (piso interno):**
   - `Quantidade = Área de contrapiso` (mesma área da aba de revestimentos internos)
   - Preço unitário composto: material + assentamento + rejunte + argamassa colante
   - Exemplo de composição: `preço = (custo_material × 1.1 de perda) + argamassa_colante + rejunte + mão_de_obra`

2. **Porcelanato de piscina:**
   - Quantidade calculada geometricamente (perímetro × profundidade + fundo)
   - Preço unitário mais alto que porcelanato comum (material especial + impermeabilização)

3. **Itens em verba (rodapés, soleiras, revestimentos de parede):**
   - `Valor = Índice (R$/AC) × AC × 1.1`
   - São verbas globais proporcionais à AC, sem quantificação detalhada
   - **Padrão importante:** quando não se quantifica item a item, usa-se R$/AC como "verba paramétrica"

4. **Itens com área direta (paver, grama sintética, vinílico):**
   - Quantidade medida diretamente do projeto
   - `Valor = Quantidade × Preço Unitário × 1.1`

### 3.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens
- Composição de preço para porcelanato inclui perda embutida no custo unitário (~10% no material)

### 3.5 Observações
- **Cadeia de dependência:** porcelanato interno = mesma área do contrapiso (aba anterior)
- Itens de áreas externas (paver, piscina, grama) são quantificados diretamente do projeto
- O padrão de "verba por R$/AC" aparece em 3 itens — é um mecanismo para simplificar itens de difícil quantificação paramétrica

---

## 4. PINTURA INTERNA

### 4.1 Variáveis de Entrada
- **AC** — Área Total Construída (para itens com índice R$/AC)
- **Área de polimento de concreto** — importada de Rev. Internos (define área de pintura epóxi)
- **Área de piso alisado** — importada de Rev. Internos (define área de pintura antiderrapante)

### 4.2 Índices Paramétricos
| Serviço | Índice | Unidade | Observação |
|---|---|---|---|
| Textura escadas | 25 | R$ / AC | Verba proporcional à AC |
| Pintura interna geral | 75 | R$ / AC | Verba proporcional à AC |

### 4.3 Regras de Cálculo

1. **Pintura epóxi (piso):**
   - `Quantidade = Área de polimento de concreto` (da aba Rev. Internos)
   - `Valor = Quantidade × Preço R$/m² × 1.1`

2. **Pintura antiderrapante (piso):**
   - `Quantidade = Área de piso alisado` (da aba Rev. Internos)
   - `Valor = Quantidade × Preço R$/m² × 1.1`

3. **Textura de escadas:**
   - `Valor = (Índice R$/AC × AC) × 1 × 1.1`
   - Verba paramétrica: o preço unitário intermediário é calculado como `índice × AC`

4. **Pintura interna geral (paredes e teto):**
   - `Valor = (75 R$/AC × AC) × 1 × 1.1`
   - Verba paramétrica que engloba toda a pintura interna de paredes e tetos

### 4.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens

### 4.5 Observações
- A pintura interna geral é o item de maior peso (75 R$/AC), e é uma **verba única** — não detalha tipos de tinta
- Pintura de pisos (epóxi e antiderrapante) é dimensionada pelas áreas da aba de revestimentos — outra cadeia de dependência
- O nome do total ("TOTAL IMPERMEABILIZAÇÃO") na planilha parece ser um erro de label — trata-se de pintura interna
- **Padrão:** itens de pintura que dependem de área usam quantidades de outras abas; itens genéricos usam R$/AC

---

## 5. ESQUADRIAS

### 5.1 Variáveis de Entrada
- **AC** — Área Total Construída (para esquadrias de alumínio e serralheria)
- **NP** — Número Total de Pavimentos (para PCF e corrimão)
- **UR** — Unidades Residenciais (para esquadrias de madeira e fechaduras)
- **Levantamento por pavimento** — áreas de guarda-corpo e pele de vidro medidas por pavimento

### 5.2 Índices Paramétricos
| Serviço | Índice | Unidade |
|---|---|---|
| Esquadrias de alumínio | 0.15 | m² / AC |
| Serralherias | 5 | R$ / AC |

### 5.3 Regras de Cálculo

1. **Esquadrias de alumínio:**
   - `Quantidade (m²) = 0.15 × AC`
   - Índice paramétrico: 15% da AC corresponde à área de esquadrias de alumínio
   - `Valor = Quantidade × Preço R$/m² × 1.1`

2. **Pele de vidro:**
   - Quantidade = somatório de áreas de pele de vidro por pavimento (levantamento direto)
   - Tipicamente em embasamento/térreo (fachada comercial)

3. **Guarda-corpo de vidro:**
   - Quantidade (m linear) = somatório de comprimentos por pavimento (levantamento direto)
   - Preço unitário já inclui margem: `preço = valor_base × 1.1` (perda/negociação embutida)

4. **PCF (Porta Corta-Fogo):**
   - `Quantidade = 2 × NP` (2 portas por pavimento — escadaria)

5. **Corrimão de madeira:**
   - `Quantidade = 11 × NP` (11 metros lineares por pavimento — lances de escada)

6. **Fechadura biométrica:**
   - `Quantidade = UR × fator` (pode ser 0 quando não se aplica)

7. **Esquadrias de madeira (portas internas):**
   - Quantidade = contagem direta de portas por pavimento tipo × número de repetições + portas únicas
   - Fórmula genérica: `(portas_por_apto × aptos_por_andar + portas_comuns) × nº_pavimentos_tipo + portas_únicas`

8. **Serralherias (verba):**
   - `Valor = 5 R$/AC × AC × 1.1`
   - Verba paramétrica para serviços diversos de serralheria

### 5.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens
- Guarda-corpo tem dupla aplicação de 1.1 (no preço base E no valor total) — verificar se intencional

### 5.5 Observações
- **Mistura de métodos:** índice paramétrico (alumínio, serralheria) + levantamento direto (pele de vidro, guarda-corpo) + fórmula funcional (PCF, corrimão, portas)
- A aba contém **levantamento auxiliar** (linhas 27-46) com quantidades de guarda-corpo e pele de vidro por pavimento
- Esquadrias de alumínio: o índice 0.15 m²/AC é referência de mercado (média de projetos similares)
- A área de esquadrias de alumínio também é usada na aba de **Fachada** como dedução de vãos

---

## 6. COBERTURA

### 6.1 Variáveis de Entrada
- **AC** — Área Total Construída (para totalização)
- **Área de cobertura** — definida diretamente (pode ser 0 em edifícios com laje impermeabilizada)

### 6.2 Índices Paramétricos
- Nesta aba não há índices paramétricos (m²/AC). As quantidades são diretas.

### 6.3 Regras de Cálculo

1. **Estrutura e telhamento:**
   - Quantidade em m² (área de cobertura) — definida diretamente
   - Pode ser 0 quando o edifício não tem telhado convencional

2. **Serviços complementares:**
   - `Quantidade = mesma área de estrutura e telhamento`
   - Cobre rufos, calhas, cumeeiras, etc.

3. **Pergolados e passarelas:**
   - Quantidades diretas quando aplicável

### 6.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens
- Fórmula: `Valor = Preço Unitário × Quantidade × 1.1`

### 6.5 Observações
- Aba simples e direta — sem fórmulas paramétrica complexas
- Em edifícios altos com laje impermeabilizada, a cobertura pode ser zerada (estrutura = 0 m²)
- Serviços complementares sempre acompanham a mesma área da estrutura (relação 1:1)
- Totalização segue o padrão: `Custo/m² de AC = Total ÷ AC`

---

## 7. REVESTIMENTO DE FACHADA

### 7.1 Variáveis de Entrada
- **AC** — Área Total Construída (para totalização R$/AC)
- **Perímetro por pavimento** — perímetro da projeção de cada pavimento
- **Pé-direito por pavimento** — altura livre de cada pavimento
- **Área de vãos (esquadrias)** — importada da aba ESQUADRIAS (dedução)
- **Área de brise** — somatório por pavimento (acabamento especial)
- **Área de porcelanato de fachada** — somatório por pavimento

### 7.2 Índices Paramétricos
- Os índices são **calculados** a partir do levantamento, não definidos a priori.
- A aba usa levantamento detalhado por pavimento para calcular a área total de fachada.

### 7.3 Regras de Cálculo

#### 7.3.1 Área total de fachada (revestimento argamassado)
```
Área de fachada = Σ (perímetro_pavimento × pé_direito_pavimento) − Área de esquadrias de alumínio
```
- **SUMPRODUCT** do perímetro × pé-direito de cada pavimento
- Deduz a área de esquadrias (vãos) importada da aba ESQUADRIAS
- Resultado = área líquida para chapisco e reboco

#### 7.3.2 Chapisco e reboco de fachada
- `Quantidade = Área de fachada líquida (calculada acima)`
- Preço composto: chapisco + reboco (somados no preço unitário)
- `Valor = Área × (preço_chapisco + preço_reboco) × 1.1`

#### 7.3.3 Tratamento de friso
- `Quantidade = Σ perímetros de todos os pavimentos` (metros lineares)
- Cada pavimento gera um friso no encontro de laje
- `Valor = Comprimento × Preço R$/m × 1.1`

#### 7.3.4 Pintura de fachada — Textura
- `Área de textura = Área total de fachada − (Área porcelanato + Área ACM + Área brise)`
- É o "restante" da fachada que recebe textura
- Preço composto: selador + textura
- `Valor = Área × (preço_selador + preço_textura) × 1.1`

#### 7.3.5 Porcelanato de fachada
- Quantidade = somatório das áreas de porcelanato por pavimento
- Preço composto: material + assentamento + rejunte + argamassa
- `Valor = Área × preço_composto × 1.1`

#### 7.3.6 Acabamentos especiais
- **ACM (Alumínio Composto):** quantidade direta, preço alto (~850 R$/m²)
- **Led vertical:** comprimento direto em metros lineares
- **Brise amadeirado:** quantidade = somatório de áreas de brise por pavimento
  - Preço elevado (~1800 R$/m²)

### 7.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens

### 7.5 Observações
- **Aba mais complexa** do grupo — combina levantamento geométrico por pavimento com cálculo paramétrico
- Contém **tabela auxiliar** (colunas J-P) com dados por pavimento: área, perímetro, pé-direito, vãos, brise, porcelanato
- A dedução de vãos (esquadrias) cria **dependência cruzada** com a aba ESQUADRIAS
- A distribuição textura/porcelanato/ACM/brise determina o nível de acabamento da fachada (e o custo)
- Casa de máquinas e reservatório: área estimada como `área_último_pav ÷ 4`, perímetro simplificado
- **Padrão:** `Custo/m² de AC = Total ÷ AC` e `Custo/m² de AC sem BDI = (Total ÷ AC) ÷ 1.1`

---

## 8. COMPLEMENTARES

### 8.1 Variáveis de Entrada
- **AC** — Área Total Construída (para todos os itens com R$/AC)
- **AL** — Área de Lazer (para móveis e decoração)

### 8.2 Índices Paramétricos
| Serviço | Índice | Unidade |
|---|---|---|
| Móveis e decoração | 1500 | R$ / AL |
| Comunicação visual | 10 | R$ / AC |
| Paisagismo | 11 | R$ / AC |
| Ligações definitivas | 4 | R$ / AC |
| Desmobilização | 5 | R$ / AC |
| Limpeza | 15 | R$ / AC |

### 8.3 Regras de Cálculo

1. **Móveis e decoração:**
   - `Quantidade = Área de Lazer (AL)`
   - `Valor = AL × 1500 R$/m² × 1.1`
   - Único item que usa AL em vez de AC

2. **Demais itens (comunicação visual, paisagismo, ligações, desmobilização, limpeza):**
   - `Quantidade = Índice R$/AC × AC`
   - `Valor = Quantidade × 1.1`
   - São **verbas paramétricas** proporcionais à AC

### 8.4 Fatores de Custo
- **BDI = 1.1** (10%) em todos os itens

### 8.5 Observações
- Todos os itens são verbas — sem quantificação detalhada
- A base AL para móveis é lógica: o mobiliário se concentra na área de lazer, não na AC total
- Os índices R$/AC representam custos de finalização da obra
- Limpeza (15 R$/AC) é o item mais caro, seguido de paisagismo (11 R$/AC)

---

## PADRÕES COMUNS IDENTIFICADOS

### P1. Fator BDI Universal = 1.1
**Todos** os itens de **todas** as abas aplicam o fator 1.1 (10% de BDI). É a regra mais consistente do modelo:
```
Valor Total = Quantidade × Preço Unitário × 1.1
```

### P2. Totalização por R$/AC
Todas as abas calculam o **custo por m² de área construída** como indicador final:
```
R$/AC = Total da aba ÷ AC
R$/AC sem BDI = (Total ÷ AC) ÷ 1.1
```
Isso permite comparação entre obras e benchmarking de mercado.

### P3. Três Métodos de Quantificação

| Método | Descrição | Exemplos |
|---|---|---|
| **Índice paramétrico (m²/AC)** | Quantidade proporcional à AC | Forro (0.6), esquadrias alumínio (0.15), contrapiso (~0.62) |
| **Verba paramétrica (R$/AC)** | Custo global proporcional à AC | Pintura interna (75), limpeza (15), rodapés (30), serralheria (5) |
| **Levantamento direto** | Quantidade medida do projeto | Piscina, paver, guarda-corpo, pele de vidro, porcelanato fachada |

### P4. Cadeia de Dependências entre Abas
```
ALVENARIA ──→ Rev. Internos (chapisco = alvenaria×2 − fachada)
Rev. Internos ──→ Acabamentos Piso (porcelanato = contrapiso)
Rev. Internos ──→ Pintura Interna (epóxi = polimento; antiderrapante = piso alisado)
Rev. Internos ──→ Rev. Fachada (desconto do chapisco interno)
ESQUADRIAS ──→ Rev. Fachada (dedução de vãos da área de fachada)
DADOS_INICIAIS ──→ TODAS as abas (AC, UR, NP, AL, etc.)
```

### P5. Padrão de "Verba por R$/AC"
Quando um item é difícil de quantificar parametricamente (rodapés, soleiras, serralheria, pintura geral, limpeza, etc.), o modelo usa **verba proporcional à AC**. Isso simplifica sem perder a proporcionalidade ao porte da obra.

### P6. Composição de Preço Unitário
Para itens como porcelanato, o preço unitário é **composto**: material (com perda) + argamassa + rejunte + mão de obra. Mas aparece como valor único na planilha, com a composição feita em fórmula.

### P7. Distribuição por Pesos
Quando um mesmo índice serve vários tipos (ex: forro = 0.6 m²/AC), a distribuição entre tipos é feita por **pesos que somam 1.0** (ex: 80% ST, 20% RU, 0% mineral). Isso permite ajustar o mix sem mudar o índice total.

### P8. Fachada = Levantamento Geométrico
A fachada é a exceção ao padrão paramétrico puro: usa **levantamento por pavimento** (perímetro × pé-direito) com deduções. É a aba mais complexa e a que mais depende de dados geométricos do projeto.

---

## RESUMO DOS ÍNDICES PARAMÉTRICOS TÍPICOS

| Serviço | Índice | Unidade | Aba |
|---|---|---|---|
| Contrapiso | ~0.62 | m² / AC | Rev. Internos |
| Manta acústica | ~0.50 | m² / AC | Rev. Internos (80% do contrapiso) |
| Forro (total) | 0.60 | m² / AC | TETO |
| Estucamento | 0.20 | m² / AC | TETO |
| Esquadrias alumínio | 0.15 | m² / AC | ESQUADRIAS |
| Pintura interna geral | 75 | R$ / AC | Pintura Interna |
| Textura escadas | 25 | R$ / AC | Pintura Interna |
| Rodapés | 30 | R$ / AC | Acabamentos |
| Soleiras e peitoris | 20 | R$ / AC | Acabamentos |
| Rev. parede (acabamento) | 45 | R$ / AC | Acabamentos |
| Serralheria | 5 | R$ / AC | Esquadrias |
| Comunicação visual | 10 | R$ / AC | Complementares |
| Paisagismo | 11 | R$ / AC | Complementares |
| Ligações definitivas | 4 | R$ / AC | Complementares |
| Desmobilização | 5 | R$ / AC | Complementares |
| Limpeza | 15 | R$ / AC | Complementares |
| Móveis/decoração | 1500 | R$ / AL | Complementares |
| PCF | 2 | un / NP | Esquadrias |
| Corrimão | 11 | m / NP | Esquadrias |
