# Template Expandido — Índices de Orçamento Executivo

> Template padrão para extração máxima de índices a partir de orçamentos executivos.
> Criado: 05/03/2026 | Atualizado: 05/03/2026
> Referências: Kirchner West Village (Dez/23) e Adore Level UP (Ago/25)

---

## COMO USAR

Ao receber um orçamento executivo (XLSX + PPTX/PDF):
1. Copiar este template para `<nome-projeto>-indices.md`
2. Preencher todas as seções aplicáveis
3. Marcar `N/D` onde não houver dado disponível
4. Registrar resumo na `BASE-CONHECIMENTO-PARAMETRICO.md`

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | _[nome]_ | — |
| Código CTN | — | _[CTN-XXX-YYY]_ | — |
| Revisão | — | _[R00]_ | — |
| Localização | — | _[Cidade/UF]_ | — |
| Endereço | — | _[Rua, nº — Bairro]_ | — |
| Incorporador/Cliente | — | _[nome]_ | — |
| Área do Terreno | AT | _[xxx]_ | m² |
| Área Construída | AC | _[xxx]_ | m² |
| Unid. Habitacionais | UR_H | _[xx]_ | un |
| Unid. Comerciais | UR_C | _[xx]_ | un |
| Estúdios | UR_E | _[xx]_ | un |
| Total Unidades | UR | _[xx]_ | un |
| Nº Total Pavimentos | NP | _[xx]_ | un |
| Nº Pavimentos Tipo | NPT | _[xx]_ | un |
| Nº Pav. Garagem | NPG | _[xx]_ | un |
| Elevadores | ELEV | _[xx]_ | un |
| Vagas Estacionamento | VAG | _[xx]_ | un |
| Prazo de Obra | — | _[xx]_ | meses |
| Data-base | — | _[Mês/Ano]_ | — |
| **CUB na Data-base** | — | **_[R$ x.xxx,xx]_** | **R$** |
| R$/m² Total | — | _[x.xxx,xx]_ | R$/m² |
| CUB ratio | — | _[x,xx]_ | CUB |
| Tipo de Laje | — | _[nervurada/maciça/mista/protendida]_ | — |
| Tipo de Fundação | — | _[hélice contínua/estaca raiz/sapata/etc]_ | — |
| Padrão Acabamento | — | _[alto/médio-alto/médio/econômico]_ | — |

### Estrutura de Custos do Executivo

> **Essencial para normalização correta** — ADM e MOE podem inflar ou distorcer macrogrupos.

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | _[Sim/Não]_ | _[Marketing, vendas, jurídico, comercial]_ |
| Valor ADM (se separado) | _[R$ xxx.xxx]_ | _[xx%]_ do total |
| **Tem MOE (Mão de Obra) separado?** | _[Sim/Não]_ | _[Global ou por etapa]_ |
| Valor MOE (se separado) | _[R$ x.xxx.xxx]_ | _[xx%]_ do total |
| Metodologia de rateio MOE | — | _[Proporcional aos custos diretos / específico por grupo]_ |
| Custos diretos de obra (sem ADM/MOE) | _[R$ xx.xxx.xxx]_ | _[xx%]_ do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

> Lista as categorias originais do executivo e como foram mapeadas para os 18 macrogrupos.

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| _[ex: "Fundações"]_ | _[3-Infraestrutura]_ | — |
| _[ex: "Estrutura de Concreto"]_ | _[4-Supraestrutura]_ | — |
| _[ex: "Vedação"]_ | _[5-Alvenaria]_ | — |
| _[ex: "Revestimento Externo"]_ | _[16-Fachada]_ | _[Inclui chapisco + reboco + pintura]_ |
| _[ex: "Gerenciamento e ADM"]_ | _[1-Gerenciamento]_ | _[Separado ADM incorporadora: R$ xxx.xxx]_ |
| ... | ... | ... |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

> Índices que caracterizam o empreendimento como *produto* — úteis para análise de viabilidade, comparação com mercado e entendimento da tipologia.

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | _[x,xx]_ | 13,94 | 3,48 |
| Área por Unidade | AC / UR | _[xx,x]_ m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | _[x,xx]_ un/m² | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | _[x,xx]_ | 2,45¹ | 0,67 |
| UR por Elevador | UR / ELEV | _[xx]_ | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | _[x,xx]_ | 0,10 | 0,43 |

¹ Kirchner: 44 UR residenciais (desconsiderando comerciais) — mais vagas/UR por ser alto padrão com vagas duplas/triplas

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | _[xx]_ | _[xx%]_ | _[xxx]_ |
| Comercial | _[xx]_ | _[xx%]_ | _[xxx]_ |
| Estúdio | _[xx]_ | _[xx%]_ | _[xxx]_ |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | _[x.xxx]_ | _[xx%]_ |
| _[Sobreloja / Mezanino]_ | _[x.xxx]_ | _[xx%]_ |
| _[Garden / Garagem]_ | _[x.xxx]_ | _[xx%]_ |
| Tipo (×N) | _[x.xxx]_ | _[xx%]_ |
| Cobertura | _[x.xxx]_ | _[xx%]_ |
| Barrilete/Reservatório | _[xxx]_ | _[x%]_ |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | _[R$ xxx.xxx]_ |
| R$ / UR (habitacionais) | Total / UR_H | _[R$ xxx.xxx]_ |
| CUB / UR | (R$/UR) / CUB | _[xx,x CUB]_ |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Os 18 macrogrupos padrão da base paramétrica Cartesian.

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | _[x.xxx.xxx]_ | _[xxx]_ | _[xx%]_ | _[xxx - xxx]_ |
| 2 | Movimentação de Terra | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | _[xx - xx]_ |
| 3 | Infraestrutura | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 4 | Supraestrutura | _[x.xxx.xxx]_ | _[xxx]_ | _[xx%]_ | _[xxx - xxx]_ |
| 5 | Alvenaria | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 6 | Impermeabilização | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | _[xx - xxx]_ |
| 7 | Instalações (agrupado) | _[x.xxx.xxx]_ | _[xxx]_ | _[xx%]_ | _[xxx - xxx]_ |
| 8 | Sistemas Especiais | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 9 | Climatização | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | _[xx - xxx]_ |
| 10 | Rev. Internos Parede | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 11 | Teto | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | _[xx - xx]_ |
| 12 | Pisos | _[x.xxx.xxx]_ | _[xxx]_ | _[xx%]_ | _[xxx - xxx]_ |
| 13 | Pintura | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xx - xxx]_ |
| 14 | Esquadrias | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 15 | Louças e Metais | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | _[xx - xx]_ |
| 16 | Fachada | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xx - xxx]_ |
| 17 | Complementares | _[x.xxx.xxx]_ | _[xxx]_ | _[x%]_ | _[xxx - xxx]_ |
| 18 | Imprevistos | _[xxx.xxx]_ | _[xx]_ | _[x%]_ | — |
| — | **TOTAL** | **_[xx.xxx.xxx]_** | **_[x.xxx]_** | **100%** | — |

> **Nota:** Quando o executivo traz Climatização dentro de Sistemas Especiais, separar. Quando traz Cobertura como grupo próprio, reclassificar dentro de Complementares ou Supraestrutura conforme natureza.

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | _[xxx]_ | _[xx%]_ | _[xx]_ | _[xxx]_ |
| Vigas | _[xxx]_ | _[xx%]_ | _[xx]_ | _[xxx]_ |
| Lajes | _[x.xxx]_ | _[xx%]_ | _[xx]_ | _[xxx]_ |
| Escadas | _[xx]_ | _[x%]_ | _[xx]_ | _[xxx]_ |
| **TOTAL** | **_[x.xxx]_** | **100%** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto / AC | _[x,xxx]_ | m³/m² | 0,242 | 0,189 |

#### Armadura (Aço)

| Elemento | Peso (kg) | Taxa (kg/m³) |
|---|---|---|
| Pilares | _[xx.xxx]_ | _[xxx]_ |
| Vigas | _[xx.xxx]_ | _[xxx]_ |
| Lajes | _[xx.xxx]_ | _[xx]_ |
| Escadas | _[x.xxx]_ | _[xx]_ |
| **TOTAL** | **_[xxx.xxx]_** | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Taxa de aço global | _[xx,xx]_ | kg/m³ | 82,32 | 114,88 |
| PU aço (corte/dobra obra) | _[x,xx]_ | R$/kg | 6,12-7,98 | _[—]_ |

#### Forma

| Tipo | Área (m²) | Reutilizações | PU (R$/m²) |
|---|---|---|---|
| Madeira serrada (vigas/pilares) | _[x.xxx]_ | _[x]_ | _[xx]_ |
| Madeirite/compensado (lajes) | _[x.xxx]_ | _[x]_ | _[xx]_ |
| **TOTAL** | **_[xx.xxx]_** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Forma / AC | _[x,xx]_ | m²/m² | 1,25 | 1,36 |

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | PU (R$) |
|---|---|---|---|
| Tipo de laje (tipo) | _[cubeta/nervurada/maciça/protendida]_ | — | — |
| Tipo de laje (embasamento) | _[idem]_ | — | — |
| Cubetas/EPS (se aplicável) | _[dimensão]_ | _[xxx/pav]_ | _[xxx]_ |
| Escoramento | _[tipo]_ | _[xxx]_ | _[xxx]_ |

#### MO Supraestrutura

| Item | Área (m²) | PU MO (R$/m²) | Obs |
|---|---|---|---|
| MO tipo | _[x.xxx]_ | _[xxx]_ | _[contrato/estimativa]_ |
| MO embasamento | _[x.xxx]_ | _[xxx]_ | _[fator ×1,3 do tipo]_ |

### 4.2 Infraestrutura

#### Fundação Profunda

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | _[HC/raiz/franki]_ | — | — | — |
| Estaca ø_[xx]_cm | _[x.xxx]_ | m | _[xxx]_ | _[xx un × xx m]_ |
| Estaca ø_[xx]_cm | _[x.xxx]_ | m | _[xxx]_ | _[xx un × xx m]_ |
| **Total estacas** | **_[x.xxx]_** | **m** | — | **_[xxx un]_** |
| Concreto fck _[xx]_ | _[x.xxx]_ | m³ | _[xxx]_ | — |
| Aço fundação profunda | _[xx.xxx]_ | kg | _[x,xx]_ | — |
| Taxa aço fundação | _[xx]_ | kg/m³ | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| ML estaca / AC | _[x,xx]_ | m/m² | 0,39 | 0,19 |
| ML estaca / UR | _[xx,x]_ | m/UR | 95,6 | 15,1 |
| Nº estacas / UR | _[x,x]_ | un/UR | 3,3 | 1,3 |

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|---|
| Forma (blocos+baldrames) | _[x.xxx]_ | m² | _[xx]_ |
| Concreto fck _[xx]_ | _[xxx]_ | m³ | _[xxx]_ |
| Aço | _[xx.xxx]_ | kg | _[x,xx]_ |
| Taxa aço fund. rasa | _[xx]_ | kg/m³ | — |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> Relações m²/m² AC e m/m² AC que permitem comparar a "intensidade" de serviços entre projetos independente do custo.

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria total | _[xx.xxx]_ | _[x,xx]_ | 1,37 | 1,56 |
| Chapisco interno | _[xx.xxx]_ | _[x,xx]_ | 2,68² | 2,58 |
| Reboco/massa interna | _[xx.xxx]_ | _[x,xx]_ | 2,68 | 2,58 |
| Forro gesso | _[x.xxx]_ | _[x,xx]_ | 0,57 | 0,16³ |
| Forro total (gesso+argamassado) | _[x.xxx]_ | _[x,xx]_ | — | 0,55 |
| Contrapiso | _[x.xxx]_ | _[x,xx]_ | 0,66⁴ | 0,76 |
| Piso cerâmico | _[x.xxx]_ | _[x,xx]_ | — | — |
| Piso laminado | _[x.xxx]_ | _[x,xx]_ | — | — |
| Pintura parede | _[xx.xxx]_ | _[x,xx]_ | 2,34 | 1,05 |
| Pintura teto | _[x.xxx]_ | _[x,xx]_ | 0,87 | 0,55 |
| Fachada total (chap+reb+pint) | _[x.xxx]_ | _[x,xx]_ | 0,73 | 1,41 |
| Cobertura (telhamento) | _[xxx]_ | _[x,xx]_ | N/A⁵ | 0,07 |

² KIR: chapisco + massa única = mesma área (28.702 m²)
³ ADR: forro gesso acartonado = 1.729 m² (0,16), mas total com argamassado = 6.145 m² (0,55)
⁴ KIR: contrapiso comum 2.612 + acústico 4.464 = 7.076 m² → 0,66 m²/m²
⁵ KIR: laje técnica no topo, sem telhamento convencional

### 5.2 Comprimentos de Serviço / AC

| Serviço | Comprimento (m) | Índice (m/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Encunhamento | _[x.xxx]_ | _[x,xx]_ | 0,62 | 0,47 |
| Verga + contraverga | _[x.xxx]_ | _[x,xx]_ | 0,33 | 0,13 |
| Rodapé | _[x.xxx]_ | _[x,xx]_ | 0,84⁶ | — |
| Contramarco | _[x.xxx]_ | _[x,xx]_ | 0,27 | — |
| Negativo gesso (se aplicável) | _[x.xxx]_ | _[x,xx]_ | 0,79 | — |

⁶ KIR: 9.058 m rodapé / 10.722,50 m² AC

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas (madeira+PCF) | _[xxx]_ | _[x,x]_ | 10,7 | 3,2 |
| Bacias sanitárias | _[xx]_ | _[x,x]_ | — | 0,4⁷ |
| Registros | _[xx]_ | _[x,x]_ | — | 0,6 |
| Pontos elétricos | _[xxx]_ | _[xx]_ | — | — |

⁷ ADR: bacias/metais entregues só em áreas comuns + bacias privativas (56 un / 141 UR)

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[xx]_ |
| Elétricas | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[xx]_ |
| Preventivas | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[xx]_ |
| Gás (GLP) | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[xx]_ |
| Comunicações/Telecom | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[xx]_ |
| **TOTAL** | **_[x.xxx.xxx]_** | **_[xxx]_** | **100%** | **_[xx]_** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| MO total instalações / AC | _[xx]_ | R$/m² | 69,20 | 122,38 |
| Mat. total instalações / AC | _[xxx]_ | R$/m² | 171,69 | 265,99 |
| Razão MO/Material | _[x,xx]_ | — | 0,40 | 0,46 |

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco rolado | _[xx.xxx]_ | m² | _[x,xx]_ | _[—]_ |
| Massa única / reboco 2,5cm | _[xx.xxx]_ | m² | _[xx,xx]_ | _[xx]_ |
| Estucamento | _[x.xxx]_ | m² | _[xx,xx]_ | _[xx]_ |
| Cerâmico parede (porcelanato) | _[x.xxx]_ | m² | _[xx,xx]_ | _[xx]_ |
| Peitoril granito | _[xxx]_ | m² | _[xxx]_ | _[xx]_ |
| Moldura elevador | _[xxx]_ | m | _[xxx]_ | _[xx]_ |

### 7.2 Pisos

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Contrapiso comum | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Contrapiso acústico | _[x.xxx]_ | m² | _[xx]_ | — |
| Porcelanato 90×90 | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Piso laminado | _[x.xxx]_ | m² | _[xxx]_ | _[xx]_ |
| Rodapé poliestireno | _[x.xxx]_ | m | _[xx]_ | _[xx]_ |
| Soleira granito | _[xxx]_ | m² | _[xxx]_ | _[xx]_ |
| Piso polido garagem | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |

### 7.3 Teto

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Forro gesso acartonado standard | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Forro gesso RU (áreas úmidas) | _[xxx]_ | m² | _[xx]_ | _[xx]_ |
| Forro madeira (sacadas) | _[xxx]_ | m² | _[xxx]_ | _[xx]_ |
| Negativo gesso | _[x.xxx]_ | m | _[xx]_ | — |
| Reboco teto | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Estucamento teto (garagem) | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |

### 7.4 Pintura

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema pintura parede (selador+massa+tinta) | _[xx.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Textura acrílica (escadas/garagem) | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Pintura teto (forro gesso) | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Epóxi/resina acrílica piso garagem | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Cimento queimado | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |

### 7.5 Fachada

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco externo | _[x.xxx]_ | m² | _[x,xx]_ | — |
| Reboco externo / massa única | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Estucamento pilares aparentes | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Textura / pintura fachada | _[x.xxx]_ | m² | _[xx]_ | _[xx]_ |
| Pastilha / porcelanato fachada | _[xxx]_ | m² | _[xxx]_ | _[xx]_ |
| Juntas dilatação fachada | _[x.xxx]_ | m | _[xx]_ | — |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

| Tipo | Qtd/Área | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Alumínio (portas+janelas) | _[xxx]_ | m² | _[x.xxx]_ | _[xxx.xxx]_ |
| Contramarco | _[x.xxx]_ | m | _[xx]_ | _[xx.xxx]_ |
| Guarda-corpo alumínio/vidro | _[xxx]_ | m² | _[x.xxx]_ | _[xxx.xxx]_ |
| Pele de vidro | _[xxx]_ | m² | _[x.xxx]_ | _[xxx.xxx]_ |
| Gradil alumínio | _[xxx]_ | m² | _[xxx]_ | _[xx.xxx]_ |
| Portas madeira (72-82cm) | _[xxx]_ | un | _[x.xxx]_ | _[xxx.xxx]_ |
| Portas madeira (90cm+) | _[xxx]_ | un | _[x.xxx]_ | _[xxx.xxx]_ |
| Porta corta-fogo | _[xx]_ | un | _[x.xxx]_ | _[xx.xxx]_ |
| Fechadura eletrônica | _[xx]_ | un | _[x.xxx]_ | _[xx.xxx]_ |
| Brise/venezianas | _[xxx]_ | m² | _[x.xxx]_ | _[xxx.xxx]_ |
| Portão alumínio (garagem) | _[x]_ | un | _[xx.xxx]_ | _[xx.xxx]_ |

### 8.2 Índices

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas / UR | _[x,x]_ | un/UR | 10,7 | 3,2 |
| PU alumínio médio | _[x.xxx]_ | R$/m² | — | 1.350 |
| PU guarda-corpo | _[x.xxx]_ | R$/m² | 1.277 | — |
| PU pele de vidro | _[x.xxx]_ | R$/m² | 2.021 | — |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevadores | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| Equipamentos piscina | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| ETE / tratamento esgoto | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| Gerador | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| Sistema aproveitamento pluvial | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| Infra carro elétrico | _[x]_ | _[xxx.xxx]_ | _[xxx.xxx]_ |
| CFTV + interfonia | — | — | _[xxx.xxx]_ |
| Automação | — | — | _[xxx.xxx]_ |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Elevador (R$/un) | _[xxx.xxx]_ | R$ | 317.500 | 187.800 |
| Sistemas Especiais / AC | _[xxx]_ | R$/m² | 96,44 | 179,87 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Arquitetônico executivo | _[xxx.xxx]_ | _[xx]_ |
| Estrutural | _[xxx.xxx]_ | _[xx]_ |
| Elétrico | _[xx.xxx]_ | _[x]_ |
| Hidrossanitário | _[xx.xxx]_ | _[x]_ |
| Preventivo | _[xx.xxx]_ | _[x]_ |
| Climatização | _[xx.xxx]_ | _[x]_ |
| Paisagismo | _[xx.xxx]_ | _[x]_ |
| Interiores/ambientação | _[xx.xxx]_ | _[x]_ |
| Fachada técnico | _[xx.xxx]_ | _[x]_ |
| Orçamento e planejamento | _[xx.xxx]_ | _[x]_ |
| **TOTAL PROJETOS** | **_[xxx.xxx]_** | **_[xx]_** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Alvará construção | _[xx.xxx]_ | _[x]_ |
| Licenças ambientais | _[xx.xxx]_ | _[x]_ |
| ARTs | _[xx.xxx]_ | _[x]_ |
| Bombeiros | _[xx.xxx]_ | _[x]_ |
| Habite-se | _[xx.xxx]_ | _[x]_ |
| INSS obra | _[xx.xxx]_ | _[x]_ |
| IPTU obra | _[xx.xxx]_ | _[x]_ |
| Incorporação | _[xx.xxx]_ | _[x]_ |
| **TOTAL TAXAS** | **_[xxx.xxx]_** | **_[xx]_** |

### 10.3 Equipe Administrativa

| Cargo | Qtd | Custo/mês (R$) | Meses | Total (R$) |
|---|---|---|---|---|
| Engenheiro Civil | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| Mestre de obras | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| Almoxarife | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| Estagiário engenharia | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| Operador grua | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| Vigilância noturna | _[x]_ | _[x.xxx]_ | _[xx]_ | _[xxx.xxx]_ |
| **TOTAL EQUIPE** | — | **_[xx.xxx]_/mês** | — | **_[x.xxx.xxx]_** |

| Índice | Valor | Un |
|---|---|---|
| Equipe ADM / AC | _[xxx]_ | R$/m² |
| Equipe ADM / mês | _[xx.xxx]_ | R$/mês |

### 10.4 Proteção Coletiva (EPCs)

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bandeja primária | _[xxx]_ | m | _[xxx]_ | _[xx.xxx]_ |
| Bandeja secundária | _[xxx]_ | m | _[xxx]_ | _[xx.xxx]_ |
| Guarda-corpo laje | _[xxx]_ | m | _[xxx]_ | _[xx.xxx]_ |
| Tela fachadeira | _[x.xxx]_ | m² | _[xx]_ | _[xx.xxx]_ |
| Varal de segurança | _[xxx]_ | m | _[xx]_ | _[xx.xxx]_ |
| EPIs (estimativa) | — | vb | — | _[xx.xxx]_ |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Período | Custo/mês (R$) | Total (R$) |
|---|---|---|---|---|
| Elevador cremalheira | _[compra/locação]_ | _[xx meses]_ | _[x.xxx]_ | _[xxx.xxx]_ |
| Grua | _[compra/locação]_ | _[xx meses]_ | _[x.xxx]_ | _[xxx.xxx]_ |
| Balancins | _[compra/locação]_ | _[xx meses]_ | _[x.xxx]_ | _[xx.xxx]_ |
| Andaime | _[locação]_ | _[xx meses]_ | _[x.xxx]_ | _[xx.xxx]_ |
| Ferramentas gerais | — | — | — | _[xx.xxx]_ |

### 10.6 Ensaios Tecnológicos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Controle tecnológico concreto | _[xx.xxx]_ | _[x]_ |
| Ensaio guarda-corpo | _[x.xxx]_ | — |
| Ensaio arrancamento reboco | _[x.xxx]_ | — |
| **TOTAL ENSAIOS** | **_[xx.xxx]_** | **_[x]_** |

### 10.7 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[x%]_ |
| Taxas e Licenças | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[x%]_ |
| Equipe ADM | _[x.xxx.xxx]_ | _[xxx]_ | _[xx%]_ | _[x%]_ |
| EPCs | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[x%]_ |
| Equipamentos | _[xxx.xxx]_ | _[xx]_ | _[xx%]_ | _[x%]_ |
| Ensaios | _[xx.xxx]_ | _[x]_ | _[x%]_ | _[x%]_ |
| Seguro de obra | _[xx.xxx]_ | _[x]_ | _[x%]_ | _[x%]_ |
| Canteiro | _[xx.xxx]_ | _[x]_ | _[x%]_ | _[x%]_ |
| **TOTAL CI** | **_[x.xxx.xxx]_** | **_[xxx]_** | **100%** | **_[xx%]_** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bacia sanitária | _[xx]_ | _[x,x]_ | _[x.xxx]_ | _[xxx.xxx]_ |
| Cuba banheiro | _[xx]_ | _[x,x]_ | _[x.xxx]_ | _[xx.xxx]_ |
| Cuba cozinha (inox) | _[xx]_ | _[x,x]_ | _[xxx]_ | _[xx.xxx]_ |
| Torneira lavatório | _[xx]_ | _[x,x]_ | _[x.xxx]_ | _[xx.xxx]_ |
| Torneira cozinha | _[xx]_ | _[x,x]_ | _[xxx]_ | _[xx.xxx]_ |
| Registro comum | _[xx]_ | _[x,x]_ | _[xxx]_ | _[xx.xxx]_ |
| Registro pressão | _[xx]_ | _[x,x]_ | _[xxx]_ | _[x.xxx]_ |
| Chuveiro | _[xx]_ | _[x,x]_ | _[xxx]_ | _[x.xxx]_ |
| Acessórios banheiro | — | — | _[xxx]_ | _[xx.xxx]_ |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | _[R$ x.xxx]_ | R$/UR |
| Louças+Metais / AC | _[xx]_ | R$/m² |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | _[xxx]_ m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | _[R$ x,xx M]_/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | _[x,x]_ | 1,7 | 5,1 |
| UR por mês | UR / Prazo | _[x,x]_ un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | _[xxx]_ R$/m²/mês | 80,5 | 100,8 |

### Cronograma de Fases (quando disponível na apresentação)

| Fase | Duração (meses) | % do Prazo |
|---|---|---|
| Infraestrutura | _[x]_ | _[xx%]_ |
| Supraestrutura | _[xx]_ | _[xx%]_ |
| Fachada | _[x]_ | _[xx%]_ |
| Acabamentos | _[xx]_ | _[xx%]_ |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Sistema | Área (m²) | PU Material (R$) | PU MO (R$) | Aplicação |
|---|---|---|---|---|
| Argamassa polimérica | _[x.xxx]_ | _[xx]_ | _[xx]_ | Banheiros, cozinhas |
| Manta asfáltica 4mm | _[x.xxx]_ | _[xxx]_ | _[xx]_ | Terraços, piscinas |
| Manta líquida (peitoris) | _[xxx]_ | _[xx]_ | — | Esquadrias |
| Tinta asfáltica | _[xxx]_ | _[xx]_ | — | Baldrames, poço elev. |
| Regularização | _[x.xxx]_ | _[xx]_ | — | Preparo superfície |
| Proteção mecânica | _[x.xxx]_ | _[xx]_ | — | Sobre manta |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Ambientação/mobiliário | _[xxx.xxx]_ | _[xx]_ | _[estimativa/projeto]_ |
| Paisagismo | _[xx.xxx]_ | _[x]_ | — |
| Comunicação visual | _[xx.xxx]_ | _[x]_ | — |
| Calçadas e passeios | _[xx.xxx]_ | _[x]_ | — |
| Limpeza final | _[xx.xxx]_ | _[x]_ | — |
| Desmobilização | _[xx.xxx]_ | _[x]_ | — |
| Ligações definitivas | _[xx.xxx]_ | _[x]_ | — |
| Caução empreiteiro | _[xxx.xxx]_ | _[xx]_ | _[% do global]_ |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

> Quando a planilha contém aba comparativa com outros projetos.

### Projetos de Referência

| Projeto | Cidade | AC (m²) | Pavimentos | Prazo | CUB | R$/m² |
|---|---|---|---|---|---|---|
| _[nome 1]_ | _[cidade]_ | _[x.xxx]_ | _[xx]_ | _[xx]_ | _[x.xxx]_ | _[x.xxx]_ |
| _[nome 2]_ | _[cidade]_ | _[x.xxx]_ | _[xx]_ | _[xx]_ | _[x.xxx]_ | _[x.xxx]_ |
| ... | ... | ... | ... | ... | ... | ... |

### Comparativo R$/m² AC por Macrogrupo (indexado ao CUB de referência)

| Macrogrupo | Este projeto | Média referências | Desvio |
|---|---|---|---|
| Gerenciamento | _[xxx]_ | _[xxx]_ | _[±xx]_ |
| Supraestrutura | _[xxx]_ | _[xxx]_ | _[±xx]_ |
| Instalações | _[xxx]_ | _[xxx]_ | _[±xx]_ |
| ... | ... | ... | ... |

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

> Pontos que merecem atenção do Leo na revisão.

### ⚠️ Acima da Média
- _[macrogrupo X: R$ xxx/m² vs média R$ xxx — motivo provável]_

### ✅ Dentro da Faixa
- _[macrogrupo Y: R$ xxx/m² — alinhado]_

### 🔽 Abaixo da Média
- _[macrogrupo Z: R$ xxx/m² vs média R$ xxx — possível motivo]_

### 📝 Particularidades
- _[tipo de laje diferente, fundação especial, exigência do cliente, etc.]_

---

## RESUMO DE ÍNDICES GLOBAIS

> Quick reference — os números mais importantes do projeto.

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | _[R$ xx.xxx.xxx]_ | R$ |
| **R$/m²** | _[x.xxx]_ | R$/m² |
| **CUB ratio** | _[x,xx]_ | CUB |
| **R$/UR** | _[R$ xxx.xxx]_ | R$/UR |
| **AC/UR** | _[xx,x]_ | m²/un |
| Concreto supra / AC | _[x,xxx]_ | m³/m² |
| Taxa aço supra | _[xx,x]_ | kg/m³ |
| Forma / AC | _[x,xx]_ | m²/m² |
| Alvenaria / AC | _[x,xx]_ | m²/m² |
| Forro / AC | _[x,xx]_ | m²/m² |
| Pintura parede / AC | _[x,xx]_ | m²/m² |
| Fachada / AC | _[x,xx]_ | m²/m² |
| Portas / UR | _[x,x]_ | un/UR |
| Estacas / AC | _[x,xx]_ | m/m² |
| MO instalações / AC | _[xx]_ | R$/m² |
| Elevador | _[xxx.xxx]_ | R$/un |
| Ritmo construção | _[xxx]_ | m²/mês |
| Burn rate | _[R$ x,xx M]_ | R$/mês |

---

> **Fonte:** _[código projeto, revisão]_
> **Extraído em:** _[DD/MM/AAAA]_
> **Notas:** _[particularidades, itens retirados a pedido do cliente, etc.]_
