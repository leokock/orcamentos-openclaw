# Scenarium Brava Norte (FG Empreendimentos) — Índices de Orçamento Executivo

> Orçamento executivo completo (XLSX + Apresentação + Análise de Custos)
> **Extraído em:** 05/03/2026
> **Data-base:** Dezembro/2024
> **Revisão:** R00
> **Código CTN:** CTN-FGE-SCN

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Scenarium Brava Norte | — |
| Código CTN | — | CTN-FGE-SCN | — |
| Revisão | — | R00 | — |
| Localização | — | Itajaí/SC | — |
| Endereço | — | Av. Dr. Jose Medeiros Vieira, 240, Brava Norte | — |
| Incorporador/Cliente | — | FG Empreendimentos | — |
| Área do Terreno | AT | 10.168,56 | m² |
| Área Construída | AC | 42.277,77 | m² |
| Unid. Habitacionais | UR_H | 142 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | N/D | un |
| Total Unidades | UR | 142 | un |
| Nº Total Pavimentos | NP | ~12 por torre | un |
| Nº Pavimentos Tipo | NPT | 5 | un |
| Nº Pav. Garagem | NPG | 2 (Sub1 + Sub2 torre D) | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 49 | meses |
| Data-base | — | Dezembro/2024 | — |
| **CUB na Data-base** | — | **R$ 3.190,77** | **R$** |
| CUB médio SC dez/24 | — | R$ 2.868,56 | R$ |
| R$/m² Total | — | 4.888,48 | R$/m² |
| CUB ratio (R16-A) | — | 1,54 | CUB |
| CUB ratio (médio) | — | 1,71 | CUB |
| Tipo de Laje | — | Protendida (tipos) | — |
| Tipo de Fundação | — | Hélice contínua monitorada (Ø40/60cm) + Estaca raiz (Ø40cm) | — |
| Padrão Acabamento | — | Super Alto | — |
| Torres | — | 4 (Sunset, Breeze, Waves, Sunrise) | — |

### Estrutura de Custos do Executivo

> **Essencial para normalização correta** — ADM e MOE podem inflar ou distorcer macrogrupos.

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Parcial | Gerenciamento inclui equipe de obra + projetos + equipamentos (formulário FG) |
| Valor ADM (se separado) | R$ 22.842.123 | 11,05% do total (01 Custos Preliminares + 02 Equipamentos) |
| **Tem MOE (Mão de Obra) separado?** | Não | Embutido nos custos diretos |
| Valor MOE (se separado) | — | — |
| Metodologia de rateio MOE | — | Embutido por etapa |
| Custos diretos de obra (sem ADM/MOE) | R$ 183.831.882 | 88,95% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

> Lista as categorias originais do executivo e como foram mapeadas para os 18 macrogrupos.

| Categoria no Executivo (Sienge) | Macrogrupo Padrão | Observação |
|---|---|---|
| 01. Custos Preliminares, ADM e Operações | 1-Gerenciamento | Inclui equipe técnica + projetos (separação parcial formulário FG) |
| 02. Equipamentos | 1-Gerenciamento | — |
| 03. Infraestrutura | 2-Mov.Terra + 3-Infraestrutura | INCLUI Mov.Terra + Infra + Contenção — aba ANÁLISE separa |
| 04. Supraestrutura | 4-Supraestrutura | — |
| 05. Paredes e Divisórias | 5-Alvenaria | Light Steel Frame + Drywall |
| 06. Sist. Hidrossanitárias e Drenagem | 7-Instalações | Parcial |
| 07. Instalações Elétricas, Lógicas e Telefônicas | 7-Instalações | Parcial |
| 08. Revestimentos Argamassa | 10-Rev. Int. Parede | — |
| 09. Forro | 11-Teto | — |
| 10. Impermeabilização | 6-Impermeabilização | — |
| 11. Sistemas de Pintura | 13-Pintura | Inclui interna + fachada |
| 12. Acabamentos de Piso e Parede | 12-Pisos + 16-Fachada | Grupo agregado (separado na aba ANÁLISE) |
| 13. Esquadrias, Vidros e Ferragens | 14-Esquadrias | — |
| 14. Sist. e Instalações Especiais | 8-Sist.Especiais | — |
| 15. Serviços Complementares e Finais | 17-Complementares | — |
| 16. Decoração e Mobiliário Área Comum | 17-Complementares | — |
| 17. Imprevistos e Contingências | 18-Imprevistos | — |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

> Índices que caracterizam o empreendimento como *produto* — úteis para análise de viabilidade, comparação com mercado e entendimento da tipologia.

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 4,16 | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 297,7 m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | 0,014 un/m² | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45 | 0,67 |
| UR por Elevador | UR / ELEV | N/D | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | N/D | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Tipo 01 | N/D | N/D | 72,29 |
| Tipo 02 | N/D | N/D | 87,86 |
| Tipo 03 | N/D | N/D | 96,26 |
| Tipo 04 | N/D | N/D | 113,26 |
| Estúdio | N/D | N/D | 46,51 |
| Garden | N/D | N/D | 239,51 |
| Penthouse 2001 | 1 | — | 280,90 |
| Penthouse 2002 | 1 | — | 275,05 |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Sub2 (só torre D) | N/D | — |
| Sub1 | N/D | — |
| Lazer1/Térreo | N/D | — |
| Lazer2/Mezanino | N/D | — |
| Tipos (5 pavimentos) | N/D | — |
| Duplex inferior | N/D | — |
| Duplex superior | N/D | — |
| Terraço (só torre A) | N/D | — |
| Técnico | N/D | — |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 1.455.592 |
| R$ / UR (habitacionais) | Total / UR_H | R$ 1.455.592 |
| CUB / UR | (R$/UR) / CUB | 456,3 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Os 18 macrogrupos padrão da base paramétrica Cartesian.

| # | Macrogrupo | Valor (R$) | R$/m² | % | Faixa Obras Similares |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 22.842.123 | 540,29 | 11,05% | 307-702 |
| 2 | Movimentação de Terra | 3.078.669 | 72,82 | 1,49% | 9-97 |
| 3 | Infraestrutura | 13.428.436 | 317,62 | 6,50% | 118-418 |
| 4 | Supraestrutura | 30.247.018 | 715,44 | 14,64% | 485-1.902 |
| 5 | Alvenaria | 13.469.645 | 318,60 | 6,52% | 104-361 |
| 6 | Impermeabilização | 2.429.083 | 57,46 | 1,18% | 38-94 |
| 7 | Instalações (agrupado) | 14.736.927 | 348,58 | 7,13% | 234-555 |
| 8 | Sistemas Especiais | 9.188.311 | 217,33 | 4,45% | 89-748 |
| 9 | Climatização | N/D | N/D | N/D | — |
| 10 | Rev. Internos Parede | 4.258.015 | 100,72 | 2,06% | 97-289 |
| 11 | Teto | 2.631.205 | 62,24 | 1,27% | 27-151 |
| 12 | Pisos | 26.983.602 | 638,25 | 13,05% | 59-638 |
| 13 | Pintura | 5.514.484 | 130,43 | 2,67% | 84-194 |
| 14 | Esquadrias | 24.623.391 | 582,42 | 11,91% | 244-991 |
| 15 | Louças e Metais | N/D | N/D | N/D | 22-51 |
| 16 | Fachada | 13.641.661 | 322,67 | 6,60% | 57-546 |
| 17 | Complementares | 19.413.937 | 459,29 | 9,39% | 49-995 |
| 18 | Imprevistos | 3.051.397 | 72,18 | 1,48% | 52-175 |
| — | **TOTAL** | **206.674.005** | **4.888,48** | **100%** | — |

> **Nota:** Climatização (grupo 9) não aparece separado neste executivo — embutido em Instalações ou Sistemas Especiais. Louças e Metais (grupo 15) embutido nos Acabamentos. Complementares inclui Serviços Complementares (R$ 8,34M) + Decoração (R$ 9,82M) + Cobertura (R$ 1,25M da aba ANÁLISE).

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | N/D | — | 35 | N/D |
| Vigas | N/D | — | 35 | N/D |
| Lajes | N/D | — | 35 | N/D |
| Escadas | N/D | — | 35 | N/D |
| **TOTAL** | **N/D** | **100%** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto / AC | N/D | m³/m² | 0,242 | 0,189 |

#### Armadura (Aço)

| Elemento | Peso (kg) | Taxa (kg/m³) |
|---|---|---|
| Pilares | N/D | N/D |
| Vigas | N/D | N/D |
| Lajes | N/D | N/D |
| Escadas | N/D | N/D |
| **TOTAL** | **N/D** | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Taxa de aço global | N/D | kg/m³ | 82,32 | 114,88 |
| PU aço (corte/dobra obra) | N/D | R$/kg | 6,12-7,98 | — |

#### Forma

| Tipo | Área (m²) | Reutilizações | PU (R$/m²) |
|---|---|---|---|
| Madeira serrada (vigas/pilares) | N/D | N/D | N/D |
| Madeirite/compensado (lajes) | N/D | N/D | N/D |
| **TOTAL** | **N/D** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Forma / AC | N/D | m²/m² | 1,25 | 1,36 |

#### Tipo de Laje e Complementos

| Item | Especificação | Qtd | PU (R$) |
|---|---|---|---|
| Tipo de laje (tipo) | Protendida | — | — |
| Tipo de laje (embasamento) | N/D | — | — |
| Cubetas/EPS (se aplicável) | N/A (protendida) | — | — |
| Escoramento | Escoramento metálico | N/D | N/D |
| **Protensão** | **2,83 kg/m²** | — | **Serviços R$ 9.000/pav** |

#### Especificações Estruturais

| Item | Especificação |
|---|---|
| Forma | Compensada plastificada 20mm, 4 usos |
| Corte e dobra aço | Indústria |
| Concreto tipos | fck 35 MPa |
| Protensão | 2,83 kg/m² + serviços R$ 9.000/pav |

#### MO Supraestrutura

| Item | Área (m²) | PU MO (R$/m²) | Obs |
|---|---|---|---|
| MO tipo | N/D | N/D | — |
| MO embasamento | N/D | N/D | — |

### 4.2 Infraestrutura

#### Fundação Profunda

| Item | Qtd | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Tipo de estaca | HC monitorada + Estaca raiz | — | — | — |
| Estaca HC Ø40cm | N/D | m | N/D | — |
| Estaca HC Ø60cm | N/D | m | N/D | — |
| Estaca raiz Ø40cm | N/D | m | N/D | — |
| **Total estacas** | **N/D** | **m** | — | **N/D un** |
| Concreto fck 40 (HC) | N/D | m³ | N/D | 20% perda |
| Concreto fck 30 (raiz) | N/D | m³ | N/D | 30% perda, argamassa |
| Aço fundação profunda | N/D | kg | N/D | — |
| Taxa aço fundação | N/D | kg/m³ | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| ML estaca / AC | N/D | m/m² | 0,39 | 0,19 |
| ML estaca / UR | N/D | m/UR | 95,6 | 15,1 |
| Nº estacas / UR | N/D | un/UR | 3,3 | 1,3 |

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|---|
| Forma (blocos+baldrames) | N/D | m² | N/D |
| Concreto fck N/D | N/D | m³ | N/D |
| Aço | N/D | kg | N/D |
| Taxa aço fund. rasa | N/D | kg/m³ | — |

#### Contenção

| Sistema | Especificação | Obs |
|---|---|---|
| Grampeamento | Grampeamento | — |
| Parede diafragma | Com atirantamento | — |
| Muro de flexão | — | — |
| Concreto contenção | fck 30-35 MPa com impermeabilizante | — |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> Relações m²/m² AC e m/m² AC que permitem comparar a "intensidade" de serviços entre projetos independente do custo.

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria total | N/D | N/D | 1,37 | 1,56 |
| Chapisco interno | N/D | N/D | 2,68 | 2,58 |
| Reboco/massa interna | N/D | N/D | 2,68 | 2,58 |
| Forro gesso | N/D | N/D | 0,57 | 0,16 |
| Forro total (gesso+argamassado) | N/D | N/D | — | 0,55 |
| Contrapiso | N/D | N/D | 0,66 | 0,76 |
| Piso cerâmico | N/D | N/D | — | — |
| Piso laminado | N/D | N/D | — | — |
| Pintura parede | N/D | N/D | 2,34 | 1,05 |
| Pintura teto | N/D | N/D | 0,87 | 0,55 |
| Fachada total (chap+reb+pint) | N/D | N/D | 0,73 | 1,41 |
| Cobertura (telhamento) | N/D | N/D | N/A | 0,07 |

### 5.2 Comprimentos de Serviço / AC

| Serviço | Comprimento (m) | Índice (m/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Encunhamento | N/D | N/D | 0,62 | 0,47 |
| Verga + contraverga | N/D | N/D | 0,33 | 0,13 |
| Rodapé | N/D | N/D | 0,84 | — |
| Contramarco | N/D | N/D | 0,27 | — |
| Negativo gesso (se aplicável) | N/D | N/D | 0,79 | — |

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas (madeira+PCF) | N/D | N/D | 10,7 | 3,2 |
| Bacias sanitárias | N/D | N/D | — | 0,4 |
| Registros | N/D | N/D | — | 0,6 |
| Pontos elétricos | N/D | N/D | — | — |

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | 7.709.706 | 182,36 | 52,3% | N/D |
| Elétricas | 7.027.221 | 166,22 | 47,7% | N/D |
| Preventivas | N/D (embutido) | N/D | — | N/D |
| Gás (GLP) | N/D (embutido) | N/D | — | N/D |
| Comunicações/Telecom | N/D (embutido) | N/D | — | N/D |
| **TOTAL** | **14.736.927** | **348,58** | **100%** | **N/D** |

> **Nota:** Executivo usa categoria ampla "Sist. Hidrossanitárias e Drenagem" + "Instalações Elétricas, Lógicas e Telefônicas". Preventivas, GLP e comunicações possivelmente embutidos ou em Sistemas Especiais.

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| MO total instalações / AC | N/D | R$/m² | 69,20 | 122,38 |
| Mat. total instalações / AC | N/D | R$/m² | 171,69 | 265,99 |
| Razão MO/Material | N/D | — | 0,40 | 0,46 |

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco rolado | N/D | m² | N/D | N/D |
| Massa única / reboco 2,5cm | N/D | m² | N/D | N/D |
| Estucamento | N/D | m² | N/D | N/D |
| Cerâmico parede (porcelanato) | N/D | m² | N/D | N/D |
| Travertino bruto (hall, lazer) | N/D | m² | N/D | N/D |
| Porcelanato 90×90 (BWCs) | N/D | m² | N/D | N/D |

### 7.2 Pisos

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Contrapiso comum | N/D | m² | N/D | N/D |
| Porcelanato 120×120 polido (privativo) | N/D | m² | N/D | N/D |
| Porcelanato 90×90 acetinado (BWCs) | N/D | m² | N/D | N/D |
| Vinílico (áreas privativas) | N/D | m² | N/D | N/D |
| Travertino (lazer) | N/D | m² | N/D | N/D |
| Pisos elevados com travertino (lazer) | N/D | m² | N/D | N/D |
| Polido argamassa 1:3 (garagem) | N/D | m² | N/D | N/D |

### 7.3 Teto

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Forro gesso acartonado standard | N/D | m² | N/D | N/D |
| Forro gesso RU (áreas úmidas) | N/D | m² | N/D | N/D |
| Forro madeira/ACM/travertino (lazer) | N/D | m² | N/D | N/D |
| Negativo gesso | N/D | m | N/D | N/D |

### 7.4 Pintura

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema pintura parede (selador+massa+tinta) | N/D | m² | N/D | N/D |
| Textura acrílica (escadas/garagem) | N/D | m² | N/D | N/D |
| Pintura teto (forro gesso) | N/D | m² | N/D | N/D |

### 7.5 Fachada

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco externo | N/D | m² | N/D | N/D |
| Reboco externo / massa única | N/D | m² | N/D | N/D |
| Textura / pintura fachada | N/D | m² | N/D | N/D |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

| Tipo | Qtd/Área | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Alumínio (portas+janelas) | N/D | m² | N/D | N/D |
| Alumínio Gold 32mm | N/D | m² | N/D | N/D |
| Guarda-corpo autoportante alum/vidro | N/D | m² | N/D | N/D |
| Portas madeira | N/D | un | N/D | N/D |
| Porta corta-fogo | N/D | un | N/D | N/D |
| Fechadura eletrônica | N/D | un | N/D | N/D |

### 8.2 Índices

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas / UR | N/D | un/UR | 10,7 | 3,2 |
| PU alumínio médio | N/D | R$/m² | — | 1.350 |
| PU guarda-corpo | N/D | R$/m² | 1.277 | — |
| PU pele de vidro | N/D | R$/m² | 2.021 | — |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevadores | N/D | N/D | N/D (embutido em Sist.Especiais) |
| Equipamentos piscina | N/D | N/D | N/D |
| Aspiração central | N/D | N/D | N/D |
| CFTV + interfonia | — | — | N/D |
| Automação | — | — | N/D |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Elevador (R$/un) | N/D | R$ | 317.500 | 187.800 |
| Sistemas Especiais / AC | 217,33 | R$/m² | 96,44 | 179,87 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Arquitetônico legal | 103.046 | 2,44 |
| Arquitetônico executivo | 507.333 | 12,00 |
| Arquitetura Interiores | 352.597 | 8,34 |
| Arquitetura Fachada | 61.810 | 1,46 |
| Terraplenagem | 9.386 | 0,22 |
| Fundação | 146.573 | 3,47 |
| Estrutural CA | 193.726 | 4,58 |
| Estrutura Metálica | 18.796 | 0,44 |
| Elétrico/Comunicação/Telefonia/Luminotécnico | 299.128 | 7,08 |
| Automação | 13.565 | 0,32 |
| Hidrossanitário/Drenagem/Pluvial | 122.903 | 2,91 |
| Irrigação | 23.250 | 0,55 |
| Preventivo e Gás | 58.265 | 1,38 |
| Climatização/Exaustão | 52.673 | 1,25 |
| Impermeabilização | 20.609 | 0,49 |
| Esquadrias | 24.731 | 0,59 |
| Forro | 19.025 | 0,45 |
| Sonorização | 10.305 | 0,24 |
| Piscina | 58.125 | 1,38 |
| Comunicação Visual | 5.073 | 0,12 |
| Paisagismo | 28.539 | 0,68 |
| As Built | 46.649 | 1,10 |
| **TOTAL PROJETOS** | **2.176.104** | **51,48** |

### 10.2 Serviços Técnicos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Topografia | 24.541 | 0,58 |
| Ensaios e Laudos | 506.428 | 11,98 |
| Estudos | 161.622 | 3,82 |
| Consultorias | 186.121 | 4,40 |
| **TOTAL SERV. TÉCNICOS** | **878.712** | **20,79** |

### 10.3 Serviços Preliminares e Canteiro

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Serviços Preliminares | 358.144 | 8,47 |
| Construção Canteiro | 410.688 | 9,72 |
| Ligações Provisórias | 2.830.044 | 66,95 |
| **TOTAL PRELIM+CANTEIRO** | **3.598.877** | **85,13** |

### 10.4 Equipamentos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Equipamentos (cat 02 Sienge) | 3.213.346 | 76,01 |

> **Nota:** Equipamentos são categoria própria no orçamento Sienge (cat 02). Incluem grua, cremalheira, balancim, etc.

### 10.5 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 2.176.104 | 51,48 | 9,5% | 1,1% |
| Serviços Técnicos | 878.712 | 20,79 | 3,8% | 0,4% |
| Serv. Preliminares e Canteiro | 3.598.877 | 85,13 | 15,8% | 1,7% |
| Equipamentos | 3.213.346 | 76,01 | 14,1% | 1,6% |
| **Subtotal identificado** | **9.867.039** | **233,40** | **43,2%** | **4,8%** |
| **Gerenciamento total** | **22.842.123** | **540,29** | **100%** | **11,1%** |

> **Nota:** Diferença de R$ 12,98M entre subtotal identificado e total (56,8% do GE) pode incluir equipe de obra, custos administrativos da incorporadora não detalhados na aba "Relatório" do XLSX.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

> **Nota:** Louças e Metais não aparecem como categoria separada neste executivo — embutidos nos Acabamentos.

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bacia sanitária | N/D | N/D | N/D | N/D (embutido) |
| Cuba banheiro | N/D | N/D | N/D | N/D (embutido) |
| Cuba cozinha (inox) | N/D | N/D | N/D | N/D (embutido) |
| Torneira lavatório | N/D | N/D | N/D | N/D (embutido) |
| Torneira cozinha | N/D | N/D | N/D | N/D (embutido) |
| Registro comum | N/D | N/D | N/D | N/D (embutido) |
| Registro pressão | N/D | N/D | N/D | N/D (embutido) |
| Chuveiro | N/D | N/D | N/D | N/D (embutido) |
| Acessórios banheiro | — | — | N/D | N/D (embutido) |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | N/D | R$/UR |
| Louças+Metais / AC | N/D | R$/m² |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 863 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 4,22 M/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 4,08 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 2,9 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 99,8 R$/m²/mês | 80,5 | 100,8 |

> **Destaque:** Ritmo 863 m²/mês — **181% acima KIR e 180% acima ADR**. Burn rate R$ 4,22M/mês — **389% acima KIR, 277% acima ADR**. Escala do empreendimento (42k m², 4 torres) permite paralelização e diluição de custos indiretos.

### Cronograma de Fases (quando disponível na apresentação)

| Fase | Duração (meses) | % do Prazo |
|---|---|---|
| Infraestrutura | N/D | N/D |
| Supraestrutura | N/D | N/D |
| Fachada | N/D | N/D |
| Acabamentos | N/D | N/D |

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

| Sistema | Área (m²) | PU Material (R$) | PU MO (R$) | Aplicação |
|---|---|---|---|---|
| Argamassa polimérica | N/D | N/D | N/D | Banheiros, cozinhas |
| Manta asfáltica 4mm | N/D | N/D | N/D | Terraços, piscinas |
| Manta líquida (peitoris) | N/D | N/D | — | Esquadrias |
| Tinta asfáltica | N/D | N/D | — | Baldrames, poço elev. |
| Regularização | N/D | N/D | — | Preparo superfície |
| Proteção mecânica | N/D | N/D | — | Sobre manta |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Serv. Complementares (cat 15) | 8.339.298 | 197,25 | Sienge |
| Decoração e Mobiliário (cat 16) | 9.820.861 | 232,29 | Sienge |
| Cobertura (aba ANÁLISE) | 1.253.778 | 29,66 | Aba ANÁLISE_CUSTOS |
| **Complementares total** | **19.413.937** | **459,29** | — |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

> Quando a planilha contém aba comparativa com outros projetos.

### Projetos de Referência (da aba CÁLCULO_MÉDIAS)

| Projeto | AC (m²) | Data-base | R$/m² | CUB | Obs |
|---|---|---|---|---|---|
| Liberato | 10.520 | Mai/2023 | N/D | N/D | — |
| Gran Torino | 12.519 | Abr/2024 | N/D | N/D | — |
| Ravello | 13.434 | Fev/2024 | N/D | N/D | — |
| Brava Ocean | 61.764 | Nov/2023 | N/D | N/D | — |
| Brava Valley | 6.003 | Mai/2022 | N/D | N/D | — |
| Paessaggio | N/D | Mai/2023 | N/D | N/D | — |
| Brasin | N/D | Mar/2023 | N/D | N/D | — |
| Lumis | N/D | Fev/2023 | N/D | N/D | — |
| Adda | N/D | Jun/2023 | N/D | N/D | — |
| Dom Bosco | N/D | Nov/2022 | N/D | N/D | — |
| San Marino | N/D | Mar/2021 | N/D | N/D | — |
| Dom | N/D | Fev/2023 | N/D | N/D | — |
| Thozen | N/D | Dez/2023 | N/D | N/D | — |
| Habitah | N/D | Ago/2022 | N/D | N/D | — |

> **Nota:** Aba CÁLCULO_MÉDIAS lista projetos de referência da FG, mas valores comparativos não fornecidos. Permite contexto de portfólio da incorporadora.

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

> Pontos que merecem atenção do Leo na revisão.

### ⚠️ Acima da Média
- **Alvenaria R$ 318,60/m² vs média base 146-361** — explica: Light Steel Frame como vedação externa (bem mais caro que alvenaria convencional, R$ 115-150 benchmark). Dentro da faixa máxima mas puxando pro topo.
- **Pisos R$ 638,25/m² vs média base 59-638** — **EXATAMENTE NO TOPO DA FAIXA**. Padrão super alto (travertino lazer, pisos elevados, porcelanato 120×120 polido, vinílico) explica. Agregação Piso+Parede+Fachada dificulta separação (aba ANÁLISE separa: Acabamentos R$ 638/m² + Fachada R$ 323/m² = R$ 961/m² total acabamentos).
- **Fachada R$ 322,67/m² vs média base 57-546** — dentro da faixa mas acima da mediana (146). Possivelmente pela separação da aba ANÁLISE (R$ 13,64M).
- **Complementares R$ 459,29/m² vs média base 49-995** — dentro da faixa, abaixo da média geral (240) mas incluindo Cobertura (R$ 29,66/m²) + Decoração (R$ 232/m²).

### ✅ Dentro da Faixa
- **Gerenciamento R$ 540,29/m² (faixa 307-702)** — médio-alto, apropriado pra projeto de 49 meses.
- **Mov.Terra R$ 72,82/m² (faixa 9-97)** — dentro.
- **Infraestrutura R$ 317,62/m² (faixa 118-418)** — dentro, próximo do topo (contenção + fundações profundas).
- **Supraestrutura R$ 715,44/m² (faixa 485-1.902)** — dentro, próximo da mediana protendida (636-980 para NPT≥10).
- **Instalações R$ 348,58/m² (faixa 234-555)** — dentro da faixa estável (310-431 sem outliers).
- **Sistemas Especiais R$ 217,33/m² (faixa 89-748)** — dentro, próximo da mediana (201).
- **Impermeabilização R$ 57,46/m² (faixa 38-94)** — dentro.
- **Rev.Int.Parede R$ 100,72/m² (faixa 97-289)** — abaixo da mediana (171) — pode indicar menos reboco (mais drywall?).
- **Teto R$ 62,24/m² (faixa 27-151)** — dentro.
- **Pintura R$ 130,43/m² (faixa 84-194)** — dentro.
- **Esquadrias R$ 582,42/m² (faixa 244-991)** — acima da mediana (356) mas dentro da faixa alto padrão. Alumínio Gold explica.
- **Imprevistos R$ 72,18/m² (1,48%)** — dentro da faixa 52-175, consistente com ~1,5-3% padrão.

### 🔽 Abaixo da Média
— Nenhum macrogrupo significativamente abaixo da faixa esperada.

### 📝 Particularidades
1. **Laje PROTENDIDA** — diferente da maioria dos projetos da base que usa cubetas. R$/m² supraestrutura (715) dentro da faixa protendida com NPT≥10 (636-980).
2. **Light Steel Frame vedação** — explica Alvenaria alta (318 vs 115-150 benchmark alvenaria convencional). Primeira referência de Steel Frame na base.
3. **4 torres** — segundo maior número de torres da base (depois Sisa Wave com 42 pav total). Complexidade logística e paralelização.
4. **Agregação Acabamentos** — categoria Sienge "Acabamentos de Piso e Parede" (R$ 39M) agrega piso + parede + fachada. Aba ANÁLISE separa: Acabamentos Piso/Parede internos R$ 26,98M + Fachada R$ 13,64M.
5. **Super alto padrão** — travertino, alumínio gold, aspiração central, piscinas aquecidas. CUB ratio 1,54 (R16-A) / 1,71 (médio) confirma padrão.
6. **Prazo 49 meses** — o mais longo da base após Catena (54m). Escala (42k m²) e 4 torres justificam.
7. **Ritmo 863 m²/mês** — **181% acima KIR/ADR**. Paralelização de 4 torres permite ritmo muito superior aos projetos mono-torre.
8. **Incorporadora FG** — primeiro projeto FG Empreendimentos na base. Portfolio de 14 projetos de referência (benchmark aba CÁLCULO_MÉDIAS).

---

## RESUMO DE ÍNDICES GLOBAIS

> Quick reference — os números mais importantes do projeto.

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 206.674.005 | R$ |
| **R$/m²** | 4.888,48 | R$/m² |
| **CUB ratio (R16-A)** | 1,54 | CUB |
| **CUB ratio (médio)** | 1,71 | CUB |
| **R$/UR** | R$ 1.455.592 | R$/UR |
| **AC/UR** | 297,7 | m²/un |
| Concreto supra / AC | N/D | m³/m² |
| Taxa aço supra | N/D | kg/m³ |
| Forma / AC | N/D | m²/m² |
| Alvenaria / AC | N/D | m²/m² |
| Forro / AC | N/D | m²/m² |
| Pintura parede / AC | N/D | m²/m² |
| Fachada / AC | N/D | m²/m² |
| Portas / UR | N/D | un/UR |
| Estacas / AC | N/D | m/m² |
| MO instalações / AC | N/D | R$/m² |
| Elevador | N/D (embutido) | R$/un |
| Ritmo construção | 863 | m²/mês |
| Burn rate | R$ 4,22 M | R$/mês |
| Torres | 4 | un |
| NPT | 5 | pav |
| Prazo | 49 | meses |

---

> **Fonte:** CTN-FGE-SCN, R00
> **Extraído em:** 05/03/2026
> **Notas:** Primeiro projeto FG Empreendimentos na base. Laje protendida, Light Steel Frame vedação, 4 torres, super alto padrão (travertino, alumínio gold). Dados quantitativos estruturais (m³ concreto, kg aço, m² forma) não disponíveis no XLSX fornecido — apenas totais por macrogrupo. Aba ANÁLISE_CUSTOS fornece breakdown alternativo mais granular que o Sienge padrão.
