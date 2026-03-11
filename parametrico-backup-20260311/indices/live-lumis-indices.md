# Índices Expandidos — Live (Lumis)

> Template padrão para extração máxima de índices a partir de orçamentos executivos.
> Criado: 06/03/2026 | Projeto: Live | Cliente: Lumis
> Referências: Kirchner West Village (Dez/23) e Adore Level UP (Ago/25)
> **Arquivo fonte:** Aba "Gerenciamento_Exec" (XLSX) + PDF executivo

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Live | — |
| Código CTN | — | CTN-LUMIS-LIV | — |
| Revisão | — | N/D | — |
| Localização | — | Florianópolis/SC | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Lumis | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | 14.888,46 | m² |
| Unid. Habitacionais | UR_H | N/D | un |
| Unid. Comerciais | UR_C | N/D | un |
| Estúdios | UR_E | N/D | un |
| Total Unidades | UR | N/D | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | N/D | meses |
| Data-base | — | Fev/2023 | — |
| **CUB na Data-base** | — | **R$ 2.662,47** | **R$** |
| R$/m² Total | — | 2.940,01 | R$/m² |
| **R$/m² Normalizado (Dez/23)** | — | **3.039,56** | **R$/m²** |
| CUB ratio | — | 1,104 | CUB |
| Tipo de Laje | — | Protendida | — |
| Tipo de Fundação | — | Sapata | — |
| Padrão Acabamento | — | Alto | — |

### Estrutura de Custos do Executivo

> **Essencial para normalização correta** — ADM e MOE podem inflar ou distorcer macrogrupos.

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Não | Não segregado |
| Valor ADM (se separado) | N/D | — |
| **Tem MOE (Mão de Obra) separado?** | Não | Embutida nos itens |
| Valor MOE (se separado) | N/D | — |
| Metodologia de rateio MOE | — | Embutida por item |
| Custos diretos de obra (sem ADM/MOE) | R$ 43.772.260,74 | 100% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

> Lista as categorias originais do executivo e como foram mapeadas para os 18 macrogrupos.

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| Gerenciamento | 1-Gerenciamento | — |
| Movimentação de Terra | 2-Mov. Terra | Lançado pelo cliente (escavação + desmonte de rocha) |
| Infraestrutura | 3-Infraestrutura | Sapatas |
| Supraestrutura | 4-Supraestrutura | Concreto protendido fck 40 MPa |
| Paredes/Painéis | 5-Alvenaria | — |
| Esquadrias | 14-Esquadrias | Com brises |
| Cobertura | 17-Complementares | Reclassificado |
| Impermeabilização | 6-Impermeabilização | — |
| Rev. Teto | 11-Teto | Forro em banheiro/sacadas |
| Rev. Int. Parede | 10-Rev.Int.Parede | — |
| Rev. Ext. Parede (Fachada) | 16-Fachada | — |
| Rev. Piso | 12-Pisos | — |
| Instalações (elétr+hidro+prev+GLP) | 7-Instalações | — |
| Equip./Sist. Especiais | 8-Sist.Especiais | — |
| Pintura (int + ext) | 13-Pintura | — |
| Serv. Complementares | 17-Complementares | — |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

> Índices que caracterizam o empreendimento como *produto* — úteis para análise de viabilidade, comparação com mercado e entendimento da tipologia.

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | N/D | 13,94 | 3,48 |
| Área por Unidade | AC / UR | N/D | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | N/D | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Vagas por Unidade | VAG / UR | N/D | 2,45¹ | 0,67 |
| UR por Elevador | UR / ELEV | N/D | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | N/D | 0,10 | 0,43 |

¹ Kirchner: 44 UR residenciais (desconsiderando comerciais) — mais vagas/UR por ser alto padrão com vagas duplas/triplas

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | N/D | N/D | N/D |
| Comercial | N/D | N/D | N/D |
| Estúdio | N/D | N/D | N/D |

### 2.4 Distribuição de Áreas por Pavimento

| Pavimento | Área (m²) | % da AC |
|---|---|---|
| Térreo | N/D | N/D |
| Garagem | N/D | N/D |
| Tipo (×N) | N/D | N/D |
| Cobertura | N/D | N/D |

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | N/D |
| R$ / UR (habitacionais) | Total / UR_H | N/D |
| CUB / UR | (R$/UR) / CUB | N/D |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

> Os 18 macrogrupos padrão da base paramétrica Cartesian.

| # | Macrogrupo | Valor (R$) | R$/m² | R$/m² Norm. | % | Faixa Obras Similares |
|---|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 2.866.588 | 192,54 | 199,07 | 6,55% | 260 - 1.071 |
| 2 | Movimentação de Terra | 1.955.644 | 131,35 | 135,80 | 4,47% | 10 - 97 |
| 3 | Infraestrutura | 1.478.807 | 99,33 | 102,69 | 3,38% | 100 - 512 |
| 4 | Supraestrutura | 9.987.703 | 670,84 | 693,58 | 22,82% | 548 - 979 |
| 5 | Alvenaria | 2.253.920 | 151,39 | 156,53 | 5,15% | 91 - 361 |
| 6 | Impermeabilização | 911.050 | 61,19 | 63,26 | 2,08% | 41 - 94 |
| 7 | Instalações (agrupado) | 4.491.140 | 301,65 | 311,88 | 10,26% | 218 - 623 |
| 8 | Sistemas Especiais | 1.810.856 | 121,63 | 125,75 | 4,14% | 96 - 425 |
| 9 | Climatização | 0 | 0,00 | 0,00 | 0,00% | 22 - 105 |
| 10 | Rev. Internos Parede | 2.858.450 | 191,99 | 198,50 | 6,53% | 77 - 254 |
| 11 | Teto | 567.859 | 38,14 | 39,43 | 1,30% | 33 - 127 |
| 12 | Pisos | 3.025.992 | 203,24 | 210,13 | 6,91% | 56 - 551 |
| 13 | Pintura | 1.321.970 | 88,79 | 91,80 | 3,02% | 88 - 210 |
| 14 | Esquadrias | 5.862.062 | 393,73 | 407,07 | 13,39% | 229 - 991 |
| 15 | Louças e Metais | 0 | 0,00 | 0,00 | 0,00% | 23 - 33 |
| 16 | Fachada | 1.840.742 | 123,64 | 127,83 | 4,21% | 92 - 279 |
| 17 | Complementares | 2.539.478 | 170,57 | 176,35 | 5,80% | 63 - 995 |
| 18 | Imprevistos | 0 | 0,00 | 0,00 | 0,00% | 44 - 122 |
| — | **TOTAL** | **43.772.261** | **2.940,01** | **3.039,56** | **100%** | — |

> **Nota:** Climatização e Louças zerados (embutidos em outros grupos). Imprevistos = 0 (SEM MARGEM). Cobertura reclassificada em Complementares (R$ 268.844).

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

#### Volume de Concreto

| Elemento | Volume (m³) | % | fck | PU Concreto (R$/m³) |
|---|---|---|---|---|
| Pilares | N/D | N/D | 40 | N/D |
| Vigas | N/D | N/D | 40 | N/D |
| Lajes | N/D | N/D | 40 | N/D |
| Escadas | N/D | N/D | 40 | N/D |
| **TOTAL** | **N/D** | **100%** | — | — |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Consumo concreto / AC | N/D | m³/m² | 0,242 | 0,189 |

> **Nota:** Projeto usa **concreto protendido fck 40 MPa** — especificação acima do padrão (fck 30-35).

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
| PU aço (corte/dobra obra) | N/D | R$/kg | 6,12-7,98 | N/D |

> **Nota:** Aço com **corte/dobra em obra** (conforme especificação fornecida).

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
| Tipo de laje (tipo) | **Protendida** | — | — |
| Tipo de laje (embasamento) | **Protendida** | — | — |
| Cubetas/EPS (se aplicável) | N/D | N/D | N/D |
| Escoramento | N/D | N/D | N/D |

#### MO Supraestrutura

| Item | Área (m²) | PU MO (R$/m²) | Obs |
|---|---|---|---|
| MO tipo | N/D | N/D | Embutida |
| MO embasamento | N/D | N/D | Embutida |

### 4.2 Infraestrutura

#### Fundação Rasa

| Item | Qtd | Un | PU (R$) |
|---|---|---|---|
| Forma (blocos+baldrames) | N/D | m² | N/D |
| Concreto fck _[xx]_ | N/D | m³ | N/D |
| Aço | N/D | kg | N/D |
| Taxa aço fund. rasa | N/D | kg/m³ | — |

> **Nota:** Projeto usa **sapata** como tipo de fundação (especificação fornecida).

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

> Relações m²/m² AC e m/m² AC que permitem comparar a "intensidade" de serviços entre projetos independente do custo.

### 5.1 Áreas de Serviço / AC

| Serviço | Área (m²) | Índice (m²/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Alvenaria total | N/D | N/D | 1,37 | 1,56 |
| Chapisco interno | N/D | N/D | 2,68² | 2,58 |
| Reboco/massa interna | N/D | N/D | 2,68 | 2,58 |
| Forro gesso | N/D | N/D | 0,57 | 0,16³ |
| Forro total (gesso+argamassado) | N/D | N/D | — | 0,55 |
| Contrapiso | N/D | N/D | 0,66⁴ | 0,76 |
| Piso cerâmico | N/D | N/D | — | — |
| Piso laminado | N/D | N/D | — | — |
| Pintura parede | N/D | N/D | 2,34 | 1,05 |
| Pintura teto | N/D | N/D | 0,87 | 0,55 |
| Fachada total (chap+reb+pint) | N/D | N/D | 0,73 | 1,41 |
| Cobertura (telhamento) | N/D | N/D | N/A⁵ | 0,07 |

² KIR: chapisco + massa única = mesma área (28.702 m²)
³ ADR: forro gesso acartonado = 1.729 m² (0,16), mas total com argamassado = 6.145 m² (0,55)
⁴ KIR: contrapiso comum 2.612 + acústico 4.464 = 7.076 m² → 0,66 m²/m²
⁵ KIR: laje técnica no topo, sem telhamento convencional

> **Nota:** Teto R$ 38,14/m² — **muito baixo** (benchmark 53-127 R$/m²). Indica que o projeto tem **forro somente em banheiros e sacadas** (conforme observação fornecida).

### 5.2 Comprimentos de Serviço / AC

| Serviço | Comprimento (m) | Índice (m/m² AC) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Encunhamento | N/D | N/D | 0,62 | 0,47 |
| Verga + contraverga | N/D | N/D | 0,33 | 0,13 |
| Rodapé | N/D | N/D | 0,84⁶ | — |
| Contramarco | N/D | N/D | 0,27 | — |
| Negativo gesso (se aplicável) | N/D | N/D | 0,79 | — |

⁶ KIR: 9.058 m rodapé / 10.722,50 m² AC

### 5.3 Quantitativos por Unidade (/UR)

| Item | Qtd Total | Índice (/UR) | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas (madeira+PCF) | N/D | N/D | 10,7 | 3,2 |
| Bacias sanitárias | N/D | N/D | — | 0,4⁷ |
| Registros | N/D | N/D | — | 0,6 |
| Pontos elétricos | N/D | N/D | — | — |

⁷ ADR: bacias/metais entregues só em áreas comuns + bacias privativas (56 un / 141 UR)

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. | MO (R$/m² AC) |
|---|---|---|---|---|
| Hidrossanitárias | N/D | N/D | N/D | N/D |
| Elétricas | N/D | N/D | N/D | N/D |
| Preventivas | N/D | N/D | N/D | N/D |
| Gás (GLP) | N/D | N/D | N/D | N/D |
| Comunicações/Telecom | N/D | N/D | N/D | N/D |
| **TOTAL** | **4.491.140** | **301,65** | **100%** | **N/D** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| MO total instalações / AC | N/D | R$/m² | 69,20 | 122,38 |
| Mat. total instalações / AC | N/D | R$/m² | 171,69 | 265,99 |
| Razão MO/Material | N/D | — | 0,40 | 0,46 |

> **Nota:** Instalações **R$ 301,65/m²** — dentro da faixa estável (240-400 R$/m²), mas no limite inferior. Boa eficiência.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

### 7.1 Revestimentos de Parede

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco rolado | N/D | m² | N/D | N/D |
| Massa única / reboco 2,5cm | N/D | m² | N/D | N/D |
| Estucamento | N/D | m² | N/D | N/D |
| Cerâmico parede (porcelanato) | N/D | m² | N/D | N/D |
| Peitoril granito | N/D | m² | N/D | N/D |
| Moldura elevador | N/D | m | N/D | N/D |

### 7.2 Pisos

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Contrapiso comum | N/D | m² | N/D | N/D |
| Contrapiso acústico | N/D | m² | N/D | N/D |
| Porcelanato 90×90 | N/D | m² | N/D | N/D |
| Piso laminado | N/D | m² | N/D | N/D |
| Rodapé poliestireno | N/D | m | N/D | N/D |
| Soleira granito | N/D | m² | N/D | N/D |
| Piso polido garagem | N/D | m² | N/D | N/D |

### 7.3 Teto

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Forro gesso acartonado standard | N/D | m² | N/D | N/D |
| Forro gesso RU (áreas úmidas) | N/D | m² | N/D | N/D |
| Forro madeira (sacadas) | N/D | m² | N/D | N/D |
| Negativo gesso | N/D | m | N/D | N/D |
| Reboco teto | N/D | m² | N/D | N/D |
| Estucamento teto (garagem) | N/D | m² | N/D | N/D |

### 7.4 Pintura

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Sistema pintura parede (selador+massa+tinta) | N/D | m² | N/D | N/D |
| Textura acrílica (escadas/garagem) | N/D | m² | N/D | N/D |
| Pintura teto (forro gesso) | N/D | m² | N/D | N/D |
| Epóxi/resina acrílica piso garagem | N/D | m² | N/D | N/D |
| Cimento queimado | N/D | m² | N/D | N/D |

### 7.5 Fachada

| Item | Qtd | Un | PU Material (R$) | PU MO (R$) |
|---|---|---|---|---|
| Chapisco externo | N/D | m² | N/D | N/D |
| Reboco externo / massa única | N/D | m² | N/D | N/D |
| Estucamento pilares aparentes | N/D | m² | N/D | N/D |
| Textura / pintura fachada | N/D | m² | N/D | N/D |
| Pastilha / porcelanato fachada | N/D | m² | N/D | N/D |
| Juntas dilatação fachada | N/D | m | N/D | N/D |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

### 8.1 Por Tipo

| Tipo | Qtd/Área | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Alumínio (portas+janelas) | N/D | m² | N/D | N/D |
| Contramarco | N/D | m | N/D | N/D |
| Guarda-corpo alumínio/vidro | N/D | m² | N/D | N/D |
| Pele de vidro | N/D | m² | N/D | N/D |
| Gradil alumínio | N/D | m² | N/D | N/D |
| Portas madeira (72-82cm) | N/D | un | N/D | N/D |
| Portas madeira (90cm+) | N/D | un | N/D | N/D |
| Porta corta-fogo | N/D | un | N/D | N/D |
| Fechadura eletrônica | N/D | un | N/D | N/D |
| Brise/venezianas | N/D | m² | N/D | N/D |
| Portão alumínio (garagem) | N/D | un | N/D | N/D |

### 8.2 Índices

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Portas / UR | N/D | un/UR | 10,7 | 3,2 |
| PU alumínio médio | N/D | R$/m² | — | 1.350 |
| PU guarda-corpo | N/D | R$/m² | 1.277 | — |
| PU pele de vidro | N/D | R$/m² | 2.021 | — |

> **Nota:** Esquadrias **R$ 393,73/m²** — alto padrão, **com brises** (conforme especificação fornecida). Benchmark: 244-640 R$/m².

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

| Item | Qtd | PU (R$) | Total (R$) |
|---|---|---|---|
| Elevadores | N/D | N/D | N/D |
| Equipamentos piscina | N/D | N/D | N/D |
| ETE / tratamento esgoto | N/D | N/D | N/D |
| Gerador | N/D | N/D | N/D |
| Sistema aproveitamento pluvial | N/D | N/D | N/D |
| Infra carro elétrico | N/D | N/D | N/D |
| CFTV + interfonia | — | — | N/D |
| Automação | — | — | N/D |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Elevador (R$/un) | N/D | R$ | 317.500 | 187.800 |
| Sistemas Especiais / AC | 121,63 | R$/m² | 96,44 | 179,87 |

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Arquitetônico executivo | N/D | N/D |
| Estrutural | N/D | N/D |
| Elétrico | N/D | N/D |
| Hidrossanitário | N/D | N/D |
| Preventivo | N/D | N/D |
| Climatização | N/D | N/D |
| Paisagismo | N/D | N/D |
| Interiores/ambientação | N/D | N/D |
| Fachada técnico | N/D | N/D |
| Orçamento e planejamento | N/D | N/D |
| **TOTAL PROJETOS** | **N/D** | **N/D** |

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Alvará construção | N/D | N/D |
| Licenças ambientais | N/D | N/D |
| ARTs | N/D | N/D |
| Bombeiros | N/D | N/D |
| Habite-se | N/D | N/D |
| INSS obra | N/D | N/D |
| IPTU obra | N/D | N/D |
| Incorporação | N/D | N/D |
| **TOTAL TAXAS** | **N/D** | **N/D** |

### 10.3 Equipe Administrativa

| Cargo | Qtd | Custo/mês (R$) | Meses | Total (R$) |
|---|---|---|---|---|
| Engenheiro Civil | N/D | N/D | N/D | N/D |
| Mestre de obras | N/D | N/D | N/D | N/D |
| Almoxarife | N/D | N/D | N/D | N/D |
| Estagiário engenharia | N/D | N/D | N/D | N/D |
| Operador grua | N/D | N/D | N/D | N/D |
| Vigilância noturna | N/D | N/D | N/D | N/D |
| **TOTAL EQUIPE** | — | **N/D**/mês | — | **N/D** |

| Índice | Valor | Un |
|---|---|---|
| Equipe ADM / AC | N/D | R$/m² |
| Equipe ADM / mês | N/D | R$/mês |

### 10.4 Proteção Coletiva (EPCs)

| Item | Qtd | Un | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bandeja primária | N/D | m | N/D | N/D |
| Bandeja secundária | N/D | m | N/D | N/D |
| Guarda-corpo laje | N/D | m | N/D | N/D |
| Tela fachadeira | N/D | m² | N/D | N/D |
| Varal de segurança | N/D | m | N/D | N/D |
| EPIs (estimativa) | — | vb | — | N/D |

### 10.5 Equipamentos de Carga/Obra

| Equipamento | Tipo | Período | Custo/mês (R$) | Total (R$) |
|---|---|---|---|---|
| Elevador cremalheira | N/D | N/D | N/D | N/D |
| Grua | N/D | N/D | N/D | N/D |
| Balancins | N/D | N/D | N/D | N/D |
| Andaime | N/D | N/D | N/D | N/D |
| Ferramentas gerais | — | — | — | N/D |

### 10.6 Ensaios Tecnológicos

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Controle tecnológico concreto | N/D | N/D |
| Ensaio guarda-corpo | N/D | — |
| Ensaio arrancamento reboco | N/D | — |
| **TOTAL ENSAIOS** | **N/D** | **N/D** |

### 10.7 Resumo CI

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | N/D | N/D | N/D | N/D |
| Taxas e Licenças | N/D | N/D | N/D | N/D |
| Equipe ADM | N/D | N/D | N/D | N/D |
| EPCs | N/D | N/D | N/D | N/D |
| Equipamentos | N/D | N/D | N/D | N/D |
| Ensaios | N/D | N/D | N/D | N/D |
| Seguro de obra | N/D | N/D | N/D | N/D |
| Canteiro | N/D | N/D | N/D | N/D |
| **TOTAL CI** | **2.866.588** | **192,54** | **100%** | **6,55%** |

> **Nota:** CI R$ 192,54/m² — **MUITO ABAIXO** do benchmark (260-1.071 R$/m²). **Gerenciamento 6,55%** é o **mais baixo da base** (benchmark 9-20%). Indica eficiência ou possível subestimativa.

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

| Item | Qtd Total | /UR | PU (R$) | Total (R$) |
|---|---|---|---|---|
| Bacia sanitária | N/D | N/D | N/D | N/D |
| Cuba banheiro | N/D | N/D | N/D | N/D |
| Cuba cozinha (inox) | N/D | N/D | N/D | N/D |
| Torneira lavatório | N/D | N/D | N/D | N/D |
| Torneira cozinha | N/D | N/D | N/D | N/D |
| Registro comum | N/D | N/D | N/D | N/D |
| Registro pressão | N/D | N/D | N/D | N/D |
| Chuveiro | N/D | N/D | N/D | N/D |
| Acessórios banheiro | — | — | N/D | N/D |

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | N/D | R$/UR |
| Louças+Metais / AC | 0,00 | R$/m² |

> **Nota:** Louças e Metais **R$ 0** — **embutidos em outros grupos** (Instalações ou Complementares). Benchmark: 23-33 R$/m².

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | N/D | 306 | 308 |
| Burn rate mensal | Total / Prazo | N/D | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | N/D | 1,7 | 5,1 |
| UR por mês | UR / Prazo | N/D | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | N/D | 80,5 | 100,8 |

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

> **Nota:** Impermeabilização R$ 61,19/m² — dentro da faixa (41-94 R$/m²), próximo à mediana (52 R$/m²).

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

| Item | Valor (R$) | R$/m² | Obs |
|---|---|---|---|
| Ambientação/mobiliário | N/D | N/D | N/D |
| Paisagismo | N/D | N/D | — |
| Comunicação visual | N/D | N/D | — |
| Calçadas e passeios | N/D | N/D | — |
| Limpeza final | N/D | N/D | — |
| Desmobilização | N/D | N/D | — |
| Ligações definitivas | N/D | N/D | — |
| Caução empreiteiro | N/D | N/D | N/D |

> **Nota:** Complementares R$ 170,57/m² — dentro da faixa (63-995 R$/m²), próximo da mediana (184 R$/m²). Cobertura R$ 268.844 foi reclassificada aqui.

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

> Quando a planilha contém aba comparativa com outros projetos.

### Projetos de Referência

| Projeto | Cidade | AC (m²) | Pavimentos | Prazo | CUB | R$/m² |
|---|---|---|---|---|---|---|
| N/D | — | — | — | — | — | — |

### Comparativo R$/m² AC por Macrogrupo (indexado ao CUB de referência)

| Macrogrupo | Este projeto | Média referências | Desvio |
|---|---|---|---|
| Gerenciamento | 192,54 | N/D | N/D |
| Supraestrutura | 670,84 | N/D | N/D |
| Instalações | 301,65 | N/D | N/D |
| ... | ... | ... | ... |

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

> Pontos que merecem atenção do Leo na revisão.

### ⚠️ Abaixo da Média / Alertas Críticos

- **Gerenciamento 6,55% (R$ 192,54/m²)** — **MAIS BAIXO DA BASE** (benchmark 9-20%, R$ 260-1.071/m²). Eficiência excepcional ou possível subestimativa. Verificar se custos indiretos estão completos.
- **Mov. Terra R$ 131,35/m²** — **2º MAIS ALTO DA BASE** (benchmark R$ 10-97/m²). Solo complexo com **desmonte de rocha** (conforme especificação). Custo lançado pelo cliente.
- **Teto R$ 38,14/m²** — **MUITO ABAIXO** (benchmark R$ 53-127/m²). Indica forro **somente em banheiros e sacadas** (conforme observação fornecida). Resto do projeto sem forro.
- **Imprevistos R$ 0** — **SEM MARGEM DE CONTINGÊNCIA** (benchmark 2-5%). Risco alto se surgirem problemas. Recomendar adicionar 2-3%.
- **Climatização R$ 0** — Embutida em outros grupos. Verificar se está em Sistemas Especiais.
- **Louças R$ 0** — Embutidas em Instalações ou Complementares. Benchmark: R$ 23-33/m².

### ✅ Dentro da Faixa

- **Instalações R$ 301,65/m²** — ✅ Dentro (240-400 R$/m²), no limite inferior. Boa eficiência.
- **Impermeabilização R$ 61,19/m²** — ✅ Dentro (41-94 R$/m²), próximo à mediana (52 R$/m²).
- **Pintura R$ 88,79/m²** — ✅ Dentro (88-210 R$/m²), no limite inferior.
- **Fachada R$ 123,64/m²** — ✅ Dentro (92-279 R$/m²), próximo à mediana (138 R$/m²).
- **Complementares R$ 170,57/m²** — ✅ Dentro (63-995 R$/m²), próximo da mediana (184 R$/m²).

### 🔽 Ligeiramente Abaixo

- **Infraestrutura R$ 99,33/m²** — Abaixo do esperado (benchmark 100-512 R$/m²). Fundação em **sapata** (mais econômica que estacas).
- **Alvenaria R$ 151,39/m²** — Dentro da faixa (91-361 R$/m²), próximo à mediana (146 R$/m²).

### 🔼 Acima da Média

- **Supraestrutura R$ 670,84/m²** — Dentro da faixa (548-979 R$/m²), mas acima da mediana (700 R$/m²). **Concreto protendido fck 40 MPa** justifica o custo elevado.
- **Esquadrias R$ 393,73/m²** — Alto padrão (benchmark 229-991 R$/m²). **Com brises**, justifica o custo.

### 📝 Particularidades

- **Concreto protendido fck 40 MPa** — Especificação acima do padrão (fck 30-35). Justifica supraestrutura elevada.
- **Sapata** — Fundação rasa mais econômica que estacas. Explica infraestrutura baixa.
- **Desmonte de rocha** — Movimentação de terra R$ 131/m² muito acima da média (R$ 10-97/m²). Solo difícil.
- **Corte/dobra em obra** — Aço processado in-loco (sem pré-fabricação).
- **Florianópolis/SC** — Mercado diferente de Itapema/BC. CUB SC Fev/23 = R$ 2.662,47.
- **Sem imprevistos** — R$ 0 (0%). Recomendar adicionar margem de 2-5%.
- **Forro mínimo** — Teto R$ 38/m² indica cobertura apenas em banheiros/sacadas.

---

## RESUMO DE ÍNDICES GLOBAIS

> Quick reference — os números mais importantes do projeto.

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | R$ 43.772.261 | R$ |
| **R$/m²** | 2.940,01 | R$/m² |
| **R$/m² Normalizado (Dez/23)** | 3.039,56 | R$/m² |
| **CUB ratio** | 1,104 | CUB |
| **R$/UR** | N/D | R$/UR |
| **AC/UR** | N/D | m²/un |
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
| Elevador | N/D | R$/un |
| Ritmo construção | N/D | m²/mês |
| Burn rate | N/D | R$/mês |

---

> **Fonte:** Aba "Gerenciamento_Exec" (XLSX) + PDF executivo
> **Extraído em:** 06/03/2026
> **Notas:** **SEM IMPREVISTOS** (R$ 0). **Gerenciamento 6,55%** — mais baixo da base. **Mov. Terra R$ 131/m²** — desmonte de rocha. **Concreto protendido fck 40 MPa**. **Sapata**. **Corte/dobra em obra**. **Florianópolis/SC**. **Teto mínimo** (R$ 38/m² — só banheiros/sacadas). **Esquadrias com brises** (R$ 394/m²).
