# REGRAS DE NEGÓCIO — Grupo 02: Estrutura, Vedação, Instalações, Sistemas Especiais e Impermeabilização

> Documento gerado a partir da análise das abas SUPRAESTRUTURA, ALVENARIA, INSTALAÇÕES, SISTEMAS ESPECIAIS e IMPERMEABILIZAÇÃO do orçamento paramétrico.

---

## Glossário de Variáveis de Entrada (DADOS_INICIAIS)

Todas as abas referenciam variáveis centralizadas na aba DADOS_INICIAIS. Segue o dicionário completo:

| Identificador | Célula | Descrição | Unidade |
|---|---|---|---|
| AT | E8 | Área do Terreno | m² |
| AC | E9 | Área Total Construída | m² |
| UR | E10 | Unidades Residenciais | un |
| dorm | E11 | Dormitórios (total) | un |
| ban | E12 | Banheiros (total) | un |
| UC | E13 | Unidades Comerciais | un |
| CHU | E14 | Churrasqueiras (total) | un |
| NP | E15 | Número Total de Pavimentos | un |
| NPT | E16 | Número de Pavimentos Tipo | un |
| NPD | E17 | Número de Pavimentos Tipo Diferenciados | un |
| ND | E18 | Número de Pavimentos Duplex | un |
| APT | E19 | Área de Projeção da Torre | m² |
| PPT | E20 | Perímetro de Projeção da Torre | m |
| AL | E21 | Área de Lazer | m² |
| AE | E22 | Área do Embasamento | m² |
| S | E23 | Área de Subsolos | m² |
| NS | E24 | Número de Subsolos | un |
| APE | E25 | Área de Projeção do Embasamento (= AE) | m² |
| PE | E26 | Perímetro de Projeção do Embasamento | m |
| NE | E27 | Número de Pavimentos de Embasamento | un |

**Nota:** A maioria das variáveis é puxada automaticamente da aba "Obra", que contém o programa arquitetônico detalhado (áreas por pavimento, quantidades de ambientes, etc.).

---

## 1. SUPRAESTRUTURA

### 1.1 Visão Geral

A aba de Supraestrutura apresenta **5 variantes de sistema estrutural**, cada uma com seus índices paramétricos próprios. A obra utiliza uma combinação (tipicamente Laje Maciça para parte e Cubetas para o restante), mas o modelo permite simular qualquer variante isoladamente.

**Fórmula geral de custo por item:**
```
Valor Total = Preço Unitário × Quantidade × BDI (1.1)
```
Para **concreto**, adiciona-se o fator de perda:
```
Valor Total = Preço Unitário × Quantidade × Perda (1.05) × BDI (1.1)
```

### 1.2 Itens Comuns a Todas as Variantes

Todas as 5 variantes possuem os mesmos 7 itens de custo (com parâmetros diferentes):

| Item | O que é |
|---|---|
| Fabricação de forma | Custo de fabricar os jogos de fôrma (compensado/metálica) |
| Montagem de forma | Custo de montar/desmontar fôrmas no local |
| Escoramento | Aluguel/custo de escoras e torres |
| Concreto | Material (concreto usinado + bomba) |
| Armadura convencional | Aço CA-50/CA-60 para armação |
| Mão de obra estrutural | Serviço completo de execução de concreto armado |
| Perfuração de vigas | Furos para passagens de instalações |

As variantes com **cubetas** adicionam o item "Cubetas" (material dos moldes plásticos).
As variantes com **protensão** adicionam itens de protensão (materiais, cabos e serviços).

### 1.3 Variante 1: LAJE MACIÇA

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Fabricação forma | 1 jogo | jogos | Quantidade de forma de montagem ÷ 1 (reaproveitamento total) × 1 jogo |
| Montagem de forma | 1,2 | m²/AC | Índice × Área construída (referência: aba Obra, área acumulada D36) |
| Escoramento | 4 | un/AE | — (quantidade não tem fórmula visível no MD, provavelmente manual) |
| Concreto | 0,22 | m³/AC | Índice × Área construída |
| Armadura | 78 | kg/m³ | Volume de concreto × índice de armadura |
| Mão de obra | 240 | R$/AC | Valor paramétrico por m² de área construída |
| Perfuração de vigas | 5.300 | R$/NP | Verba por pavimento × Nº total de pavimentos |

**Observações:**
- Fôrma: 1 jogo = não há reaproveitamento entre pavimentos (fôrma nova para cada)
- Concreto: preço unitário = R$ 535 (concreto) + R$ 45 (bomba) = R$ 580/m³, com fator de perda 1,05
- Perfuração de vigas: **"Coeficiente originário do Gran Torino (R$ 160,00/un)"** — índice calibrado a partir de obra de referência

### 1.4 Variante 2: LAJE CUBETAS

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Fabricação forma | 3 jogos | jogos | Forma de montagem ÷ Nº pavimentos × 3 jogos (3 reaproveitamentos) |
| Montagem de forma | 1,1 | m²/AC | Índice × Soma de áreas de todos os pavimentos (Obra D21:D35) |
| Escoramento | — | un/APT×NPT | AC − APE (área construída menos área de projeção do embasamento) |
| Cubetas | 25 | R$/AC | AC − APE (apenas pavimentos da torre) |
| Concreto | 0,23 | m³/AC | Complementar à laje maciça (total de 1450m³ − volume da maciça) |
| Armadura | 78 | kg/m³ | Complementar (121.000 kg total − armadura da maciça) |
| Mão de obra | 290 | R$/AC | Valor paramétrico × AC total |
| Perfuração de vigas | 2.300 | R$/NP | Verba por pavimento × Nº total de pavimentos |

**Observações:**
- O **"índice Passione"** é citado: montagem de forma Passione = 0,98 m²/AC (vs. 1,1 usado aqui)
- Concreto Passione: 23 kg/m³; Armadura Passione: 93 kg/m³
- Concreto inclui custo adicional de bombeamento: (535 + 45 + 1,67×0,6) × 1,05
- Quando a obra combina Maciça + Cubetas, as quantidades são calculadas como **complementares** (total − parte maciça)

### 1.5 Variante 3: LAJE CUBETAS PROTENDIDAS

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Fabricação forma | 3 jogos | jogos | Forma de montagem ÷ Nº pavimentos × 3 jogos |
| Montagem de forma | 1,1 | m²/AC | Índice × AC |
| Escoramento | — | un/APT×NPT | AC − APE |
| Cubetas | 25 | R$/AC | AC − APE |
| Protensão materiais | — | — | AC − APE − descontos de áreas específicas (escadas, halls) |
| Protensão serviços | — | — | Mesma área que protensão materiais |
| Concreto | 0,25 | m³/AC | Índice × AC |
| Armadura | 100 | kg/m³ | Volume de concreto × índice |
| Mão de obra | 280 | R$/AC | Valor paramétrico × AC |
| Perfuração de vigas | 2.300 | R$/NP | Verba × NP |

**Observações:**
- Protensão cobre apenas área da torre (descontadas escadas e halls)
- Protensão: materiais R$ 11,50/m² + serviços R$ 11,50/m² = R$ 23,00/m² de área protendida
- Custos identificados como **"Custos Connect Executivo"** (obra de referência)
- Armadura sobe de 78 para 100 kg/m³ (protensão exige mais aço passivo)
- Concreto sobe de 0,23 para 0,25 m³/AC

### 1.6 Variante 4: LAJE TRELIÇADA

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Fabricação forma | 2 jogos | jogos | Forma ÷ NP × 2 jogos |
| Montagem de forma | 2,1 | m²/AC | Índice × AC (referência E38 da aba Obra — área específica) |
| Escoramento Torre | 2 | un/APT×NPT | Índice × APT × NPT |
| Escoramento Embasamento | 2 | un/AE | Índice × AE |
| Cubetas | 25 | R$/AC | Índice × AC |
| Concreto | 0,25 | m³/AC | Índice × AC |
| Armadura | 110 | kg/m³ | Volume × índice |
| Mão de obra | 240 | R$/AC | Valor paramétrico × AC |
| Perfuração de vigas | 5.300 | R$/NP | Verba × NP |

**Observações:**
- Fôrma mais barata (R$ 85/m² vs. R$ 110) por usar menos compensado
- Montagem mais cara (R$ 1,50/m² porém 2,1 m²/AC vs. 1,1-1,2) — compensa na fabricação
- Escoramento separado: torre e embasamento com cálculos independentes
- Armadura mais alta: 110 kg/m³ (treliçada exige mais aço)
- Concreto a R$ 575/m³ (sem parcela de bomba separada)

### 1.7 Variante 5: LAJE PROTENDIDA (sem cubetas)

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Fabricação forma | 3 jogos | jogos | Forma ÷ NP × 3 |
| Montagem de forma | 2,1 | m²/AC | Índice × AC |
| Escoramento | 3 | un/AE | ROUNDUP(Índice × APE × 3 jogos) |
| Protensão materiais | 12,3 | R$/m² | Área = (NPT + NPD) × APT + AE |
| Protensão cabos | 2,83 | kg/m² | Índice × área de protensão |
| Protensão serviços | 9.000 | R$/pav | Verba por pavimento × NP |
| Concreto | 0,25 | m³/AC | Índice × AC |
| Armadura | 90 | kg/m³ | Volume × índice |
| Mão de obra | 240 | R$/AC | Valor paramétrico × AC |
| Perfuração de vigas | 5.300 | R$/NP | Verba × NP |

**Observações:**
- Protensão cobre torre + embasamento: (NPT + NPD) × APT + AE
- Cabos de protensão: 2,83 kg/m² × R$ 12,30/kg
- Armadura convencional reduz para 90 kg/m³ (protensão substitui parte do aço)
- Concreto R$ 580/m³ (535 + 45) com fator de perda 1,05

### 1.8 Quadro Comparativo das Variantes

| Parâmetro | Maciça | Cubetas | Cub. Protendida | Treliçada | Protendida |
|---|---|---|---|---|---|
| Jogos de fôrma | 1 | 3 | 3 | 2 | 3 |
| Montagem (m²/AC) | 1,2 | 1,1 | 1,1 | 2,1 | 2,1 |
| Preço fôrma (R$/m²) | 110 | 110 | 110 | 85 | 110 |
| Concreto (m³/AC) | 0,22 | 0,23 | 0,25 | 0,25 | 0,25 |
| Armadura (kg/m³) | 78 | 78 | 100 | 110 | 90 |
| MO (R$/AC) | 240 | 290 | 280 | 240 | 240 |
| Perfuração (R$/NP) | 5.300 | 2.300 | 2.300 | 5.300 | 5.300 |
| Tem cubetas? | Não | Sim | Sim | Sim | Não |
| Tem protensão? | Não | Não | Sim | Não | Sim |

### 1.9 Regras de Composição do Total

- O **TOTAL SUPRAESTRUTURA** na planilha soma **duas variantes** (ex: Laje Maciça + Cubetas): `G77 = G30 + G17`
- A escolha de quais variantes combinar depende do projeto estrutural
- O indicador R$/m² é calculado como: Total ÷ AC, e também sem BDI: (Total ÷ 1,1) ÷ AC

---

## 2. ALVENARIA (PAREDES E PAINÉIS)

### 2.1 Visão Geral

A aba apresenta **2 variantes** de vedação:
- **Alvenaria convencional** (blocos cerâmicos/concreto)
- **Alvenaria + Drywall** (sistema misto)

### 2.2 Variante 1: ALVENARIA CONVENCIONAL

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Alvenaria externa | 0,6 | m²/AE | Índice × AC (nota: fórmula usa E9 = AC, não AE) |
| Alvenaria interna | 0,8 | m²/AL | Índice × AC (nota: fórmula usa E9 = AC, não AL) |
| Alvenaria escadas | 0,18 | m²/AC | Índice × AC |
| Alvenaria refratária | 1,75 | m²×CHU | Índice × Nº de churrasqueiras |
| Serviços complementares | 12,5 | R$/m² | Soma das alvenarias (externa + interna + escadas) |
| Mão de obra | — | R$/m² | Soma das alvenarias (externa + interna + escadas) |

**Fatores de custo:**
- Alvenaria externa e interna: R$ 45/m² × BDI 1,1
- Alvenaria escadas: R$ 75/m² × **Perda 1,05** × BDI 1,1 (único item com fator de perda)
- Alvenaria refratária: R$ 310/m² × BDI 1,1 (custo mais alto — material especial)
- Serviços complementares: R$ 6,50/m² (preço unitário difere do parâmetro de R$ 12,50)
- Mão de obra: R$ 48/m²

**Observações:**
- As unidades da coluna C (AE, AL) parecem **indicativas da origem conceitual** do índice, mas a fórmula real usa AC (E9) para externos e internos
- A alvenaria refratária é proporcional ao número de churrasqueiras, não à área

### 2.3 Variante 2: ALVENARIA + DRYWALL

**Índices paramétricos:**

| Item | Índice | Unidade | Regra de cálculo da quantidade |
|---|---|---|---|
| Alvenaria embasamento | 1,0 | m²/AE | Índice × AE (Área do Embasamento) |
| Alvenaria lazer | 0,4 | m²/AL | Índice × AL (Área de Lazer) |
| Alvenaria tipo | 1,65 | m²/APT×(NPT+2ND) | Índice × APT × (NPT + NPD) × **0,4** |
| Drywall tipo | 1,65 | m²/APT×(NPT+2ND) | Índice × APT × (NPT + NPD) × **0,6** |
| Alvenaria escadas | 0,2 | m²/AC | Índice × AC |
| Alv. cobertura/reservatório | 0,8 | m²/APT | Índice × APT |
| Alvenaria refratária | 1,75 | m²×CHU | Referência cruzada: **SISTEMAS ESPECIAIS!B10** (nº churrasqueiras) |
| Serviços complementares | 12,5 | R$/m² | Soma de todas alvenarias (exceto drywall e refratária) |
| Mão de obra | 35 | R$/m² | Mesma base dos serviços complementares |

**Regras especiais:**
- **Proporção alvenaria/drywall nos tipos:** 40% alvenaria + 60% drywall (fixo no modelo)
- A planilha calcula automaticamente a proporção: `J24 = Drywall ÷ (Alvenaria+Drywall)`
- **Drywall é significativamente mais caro:** R$ 220/m² vs. R$ 45/m² da alvenaria
- Mão de obra mais barata: R$ 35/m² (vs. R$ 48 na convencional) — drywall inclui MO no preço
- Alvenaria refratária usa **referência cruzada** com aba SISTEMAS ESPECIAIS (nº de churrasqueiras)

**Fatores de custo:**
- Alvenaria convencional: R$ 45/m² × BDI 1,1
- Drywall: R$ 220/m² × BDI 1,1
- Alvenaria escadas: R$ 70/m² × BDI 1,1 (sem fator de perda nesta variante)
- Alvenaria refratária: R$ 210/m² (preço diferente da variante 1, pois unidade é por unidade de churrasqueira)

### 2.4 Indicador R$/m²

- Total Alvenaria ÷ AC = R$/m² (com BDI)
- Total ÷ 1,1 ÷ AC = R$/m² (sem BDI)
- Na planilha-base, o **TOTAL ALVENARIA usa a variante convencional** (`G33 = G16`)

---

## 3. INSTALAÇÕES

### 3.1 Visão Geral

A aba de Instalações é a mais simples: **todos os itens são 100% paramétricos sobre a Área Construída (AC)**, sem variantes. A fórmula é sempre:
```
Valor Total = Índice (R$/AC) × AC × BDI (1.1)
```

Não há fator de perda (1,05) em nenhum item — perdas já estão embutidas nos índices.

### 3.2 Instalações Elétricas

| Item | Índice (R$/m² AC) |
|---|---|
| Entrada de Energia | 5,50 |
| Eletrodutos e Eletrocalhas | 10,00 |
| Cabos e Fiações | 30,00 |
| Quadros e Disjuntores | 18,00 |
| Acabamentos Elétricos | 15,00 |
| Equipamentos e Iluminação | 15,00 |
| Mão de Obra Elétrica | 60,00 |
| **Subtotal Elétrica** | **153,50** |

### 3.3 Instalações Hidrossanitárias

| Item | Índice (R$/m² AC) |
|---|---|
| Água Fria | 25,00 |
| Água Quente | 20,00 |
| Águas Pluviais | 10,00 |
| Instalações Sanitárias | 15,00 |
| Louças e Metais | 20,00 |
| Mão de Obra Hidráulica | 55,00 |
| **Subtotal Hidro** | **145,00** |

### 3.4 Instalações Preventivas e GLP

| Item | Índice (R$/m² AC) |
|---|---|
| Instalações Preventivas (PPCI) | 20,00 |
| Instalações de GLP | 13,00 |
| SPDA (Proteção e Aterramento) | 8,00 |
| **Subtotal Preventivas** | **41,00** |

### 3.5 Totais e Indicador

- **Índice total de Instalações = 339,50 R$/m² AC** (sem BDI)
- Com BDI: **373,45 R$/m² AC**
- Distribuição: Elétrica 45%, Hidro 43%, Preventivas 12%

---

## 4. SISTEMAS ESPECIAIS

### 4.1 Visão Geral

Aba com **4 subgrupos** e lógica de cálculo heterogênea — mistura itens paramétricos (R$/AC) com itens de quantidade fixa (equipamentos específicos).

### 4.2 Climatização, Exaustão Mecânica e Pressurização

| Item | Regra de quantidade | Preço unitário |
|---|---|---|
| Infraestrutura AR | Soma de pontos de AR por pavimento (Obra!L21:L39) | R$ 1.200/ponto |
| Instalação AR | Soma de aparelhos AR (Obra!M21:M39) | R$ 9.000/aparelho |
| Ventokit | Soma de ventokits (Obra!K21:K39) | R$ 900/un |
| Churrasqueiras | Soma de churrasqueiras (Obra!I21:I39) | R$ 2.600/un |

**Regra:** Quantidades vêm diretamente do **programa arquitetônico** (aba Obra), não de índices paramétricos. Cada pavimento tem suas quantidades de pontos de AR, aparelhos, ventokits e churrasqueiras.

**Referência cruzada:** O item Churrasqueiras (B10) desta aba é referenciado pela aba ALVENARIA (variante Drywall, item refratária).

### 4.3 Comunicação

| Item | Índice (R$/m² AC) | Regra especial |
|---|---|---|
| CFTV | 1,50 | Padrão: Índice × AC × BDI |
| Interfone | 1,50 | **(Índice × AC + UR × R$ 800) × BDI** — acrescenta R$ 800 por unidade residencial (porteiro com vídeo) |
| TV e Internet | 4,00 | Padrão |
| Automação e Segurança | 5,00 | Padrão |

**Observação importante:** O item Interfone tem lógica diferente dos demais — soma uma parcela fixa por unidade residencial (R$ 800/UR) ao cálculo paramétrico. Anotação: *"considerando porteiro com vídeo"*.

### 4.4 Equipamentos

| Item | Regra de quantidade | Regra de preço |
|---|---|---|
| Elevadores | Quantidade fixa (ex: 2) | Preço ajustado por fórmula de proporcionalidade entre obras |
| Grupo gerador | Quantidade fixa | R$ 42.000/un |
| Pressurização escada | Quantidade fixa | R$ 26,40 × AC (preço escala com área) |
| Bombas | Quantidade fixa | R$ 10.000/un |
| Infra carro elétrico | Quantidade fixa | R$ 560/un |
| Equip. carro elétrico 23kV | Quantidade fixa | R$ 9.500/un |
| Piscina aquecida | Quantidade fixa | R$ 121.000/un |
| Sauna | Quantidade fixa | R$ 8.500/un |
| Spa | Quantidade fixa | R$ 15.000/un |
| Hidromassagem | Quantidade fixa | R$ 25.000/un |
| Sistema aquecimento | Quantidade (0 = não se aplica) | R$ 55 × AC |

**Observações:**
- Elevadores: preço calculado por **proporcionalidade** entre obras de referência — ajusta valor de contrato de obra anterior pelo número de pavimentos e índice de correção
- Pressurização e aquecimento: **preço unitário escala com AC** (não é valor fixo)
- Itens de lazer (piscina, sauna, spa, hidromassagem) são **inclusão opcional** — zerar quantidade se não houver
- Todos com BDI 1,1, exceto sistema de aquecimento (quando qty=0, usa multiplicação direta sem BDI)

### 4.5 Outros Sistemas Especiais

| Item | Índice (R$/m² AC) |
|---|---|
| Outros sistemas | 20,00 |

Verba genérica para sistemas não listados.

---

## 5. IMPERMEABILIZAÇÃO

### 5.1 Visão Geral

Itens mistos: alguns paramétricos sobre AC, outros com quantidades específicas. Todos com BDI 1,1, sem fator de perda.

### 5.2 Índices Paramétricos

| Item | Índice | Unidade | Regra de cálculo da quantidade | Preço (R$/m²) |
|---|---|---|---|---|
| Impermeabilização cimentícia | 0,25 | m²/AC | Índice × AC | 60 |
| Impermeabilização manta asfáltica | 0,11 | m²/AC | Índice × AC | 110 |
| Impermeabilização de peitoril | 0,6 | R$/AC | Quantidade = 1 (verba); Preço = Índice × AC | — |
| Regularização de superfície | 25 | R$/m² | Soma: imp. cimentícia + imp. manta asfáltica | 22 |
| Proteção mecânica | 28 | R$/m² | = Área de manta asfáltica | 28 |

### 5.3 Itens com Quantidade Específica

| Item | Regra de quantidade | Preço (R$/m²) |
|---|---|---|
| Poço do elevador | Cálculo geométrico: (base + perímetro × altura) × nº poços | 41 |
| Baldrames | **Referência cruzada: INFRAESTRUTURA!D28** (área de baldrames) | 35 |
| Ralos | Soma de ralos por pavimento (Obra!N21:N39) | 56/un |

### 5.4 Regras de Cálculo

- **Regularização:** Aplica-se apenas nas áreas que receberão impermeabilização (cimentícia + manta)
- **Proteção mecânica:** Aplica-se apenas sobre a manta asfáltica (não sobre cimentícia)
- **Peitoril:** Tratado como verba global (quantidade = 1), preço = 0,6 × AC
- **Ralos:** Quantidade vem do programa arquitetônico, não de índice paramétrico

### 5.5 Indicador R$/m²

- Total ÷ AC = R$/m² (com BDI)
- Total ÷ 1,1 ÷ AC = R$/m² (sem BDI)

---

## 6. REFERÊNCIAS CRUZADAS ENTRE ABAS

| De (aba) | Para (aba) | O que referencia |
|---|---|---|
| ALVENARIA (Drywall) | SISTEMAS ESPECIAIS | Nº de churrasqueiras (B10) para alvenaria refratária |
| IMPERMEABILIZAÇÃO | INFRAESTRUTURA | Área de baldrames (D28) |
| IMPERMEABILIZAÇÃO | Obra | Quantidade de ralos por pavimento (N21:N39) |
| SISTEMAS ESPECIAIS | Obra | Pontos AR, aparelhos, ventokits, churrasqueiras (I,K,L,M 21:39) |
| SUPRAESTRUTURA (Maciça) | Obra | Área acumulada (D36) |
| SUPRAESTRUTURA (Cubetas) | Obra | Áreas por pavimento (D21:D35) |
| TODAS | DADOS_INICIAIS | Variáveis de entrada (AC, APT, NP, etc.) |

---

## 7. FATORES DE CUSTO — RESUMO

| Fator | Valor | Aplicação |
|---|---|---|
| BDI | 1,10 (10%) | **Todos os itens** — Bonificação e Despesas Indiretas |
| Perda de material | 1,05 (5%) | Apenas **concreto** (todas variantes) e **alvenaria de escadas** (variante convencional) |

**Regra geral:** O BDI de 1,1 é aplicado universalmente. O fator de perda de 1,05 é aplicado seletivamente apenas em materiais com desperdício significativo previsto (concreto bombeado, alvenaria em condições especiais como escadas).

---

## 8. OBSERVAÇÕES E OBRAS DE REFERÊNCIA

O modelo paramétrico foi calibrado com base em obras reais:

- **"Passione"** — Referência para índices de cubetas (montagem forma 0,98 m²/AC, concreto 23, armadura 93 kg/m³)
- **"Gran Torino"** — Referência para perfuração de vigas (R$ 160/un por furo, convertido em verba por pavimento)
- **"Connect Executivo"** — Referência para custos de protensão e cubetas protendidas
- **"Nova"** — Referência alternativa para perfuração de vigas (verba de R$ 1.500/pavimento)

Esses nomes aparecem como **observações na planilha** e servem para rastrear a origem dos índices quando for necessário recalibrar.

---

## 9. REGRAS GENÉRICAS DO MODELO

1. **Tudo escala com AC** — A Área Total Construída é o driver principal de custo em todas as abas
2. **Variáveis secundárias** — APT, NP, NPT, AE, CHU complementam para itens específicos
3. **Fórmula padrão:** `Quantidade = Índice × Variável de Entrada` → `Custo = Quantidade × Preço Unitário × BDI`
4. **Equipamentos são exceção** — Têm quantidade e preço fixos (não paramétricos)
5. **O modelo permite simulação** — Trocar variante de laje, proporção alvenaria/drywall, incluir/excluir equipamentos de lazer
6. **Indicador de controle:** Cada aba calcula R$/m² de AC para comparação entre obras
