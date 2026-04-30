# WF Aquarius Residence — Índices de Orçamento Executivo

> Extração de índices a partir de orçamento executivo detalhado (XLSX) com Ger_Executivo e quadro de áreas.
> Projeto: Aquarius Residence — WF Construtora
> Data-base: Jul/2025
> Extraído em: 10/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Aquarius Residence | — |
| Código CTN | — | CTN-WF-AQU | — |
| Revisão | — | R02 | — |
| Localização | — | N/D (provavelmente litoral SC) | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | WF Construtora | — |
| Área do Terreno | AT | 1.080,00 | m² |
| Área Construída | AC | 16.789,05 | m² |
| Área Privativa | — | 7.928,64¹ | m² |
| Unid. Habitacionais | UR_H | 84 | un |
| Unid. Comerciais | UR_C | 6 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 90 | un |
| Nº Total Pavimentos | NP | 30 | un |
| Nº Pavimentos Tipo | NPT | 21 | un |
| Nº Pav. Garagem | NPG | 5 | un |
| Elevadores | ELEV | N/D | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 57 | meses |
| Data-base | — | Jul/2025 | — |
| **CUB na Data-base** | — | **R$ 2.965,54** | **R$** |
| R$/m² Total | — | 3.193,73 | R$/m² |
| CUB ratio | — | 1,08 | CUB |
| Tipo de Laje | — | Nervurada (cubetas) | — |
| Tipo de Fundação | — | Hélice Contínua ø50cm e ø60cm | — |
| Padrão Acabamento | — | Alto | — |

¹ Área privativa extraída da aba "Apresentação" do xlsx.

**Notas:**
- Dados do projeto extraídos da aba "Obra" do orçamento xlsx.
- CUB/SC jul/2025 = R$ 2.965,54 (informado na aba Obra).
- Breakdown por macrogrupo já disponível na aba "Obra" (linhas 31-48).
- 5 tipologias de unidade: Un.01 (106,4m²), Un.02 (75,5m²), Un.03 (104,0m²), Un.04 (78,1m²), Un.05 (76,5m²).
- 3 torres/blocos: Ravello, Marine, Maiori (da aba Apresentação).

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Não verificável | Gerenciamento agrupado |
| **Tem Projetos separado?** | Sim | Incluído no Gerenciamento (aba Ger_Tec e Adm) |
| **Tem MOE (Mão de Obra) separado?** | Sim | MOE aberta por disciplina na Ger_Executivo |
| Metodologia de rateio MOE | — | MOE alocada por etapa dentro de cada célula construtiva |
| Custos Gerenciamento | R$ 6.459.783,51 | 12,05% — inclui projetos, taxas, canteiro, ADM obra, equipe técnica |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo (Aba Obra) | Macrogrupo Padrão | Observação |
|---|---|---|
| Gerenciamento Técnico e Administrativo | 1-Gerenciamento | Projetos + taxas + canteiro + equipe + ADM |
| Movimentação de Terra | 2-Mov. Terra | Escavação + rebaixamento + bota-fora + lastro |
| Infraestrutura | 3-Infraestrutura | HC ø50/60cm + fundação rasa + contenções |
| Supraestrutura | 4-Supraestrutura | Forma + armadura + concreto + escoramento + MO |
| Alvenaria | 5-Alvenaria | Blocos + vedações + MO |
| Impermeabilização e Tratamentos | 6-Impermeabilização | Todos os sistemas |
| Instalações Elétricas, Hidráulicas, GLP e Preventivas | 7-Instalações | Agrupado: elétr + hidro + GLP + preventivo |
| Equipamentos e Sistemas Especiais | 8-Sist. Especiais | Elevadores + piscina + automação + portões |
| Climatização, Exaustão Mecânica e Pressurização | 9-Climatização | Separado do Sist. Especiais |
| Revestimentos Internos de Parede | 10-Rev. Int. Parede | Chapisco + reboco + argamassa interna |
| Revestimentos Internos de Teto | 11-Teto | Forros gesso + acabamentos teto |
| Pisos e Pavimentações | 12-Pisos | Contrapiso + pisos + pavimentações |
| Sistemas de Pintura Interna | 13-Pintura | Pintura interna completa |
| Esquadrias, Vidros e Ferragens | 14-Esquadrias | Alumínio + madeira + vidros + ferragens |
| Louças e Metais | 15-Louças e Metais | Separado (R$ 505.846) |
| Revestimentos e Acabamentos em Fachada | 16-Fachada | Chapisco + reboco + pintura externa |
| Serviços Complementares e Finais | 17-Complementares | Limpeza + infra interna + mob + paisagismo |
| Imprevistos | 18-Imprevistos | 1,30% do total |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % |
|---|---|---|---|---|
| 1 | Gerenciamento | 6.459.783,51 | 384,76 | 12,05% |
| 2 | Mov. Terra | 290.742,39 | 17,32 | 0,54% |
| 3 | Infraestrutura | 3.912.290,74 | 233,03 | 7,30% |
| 4 | Supraestrutura | 9.983.387,47 | 594,64 | 18,62% |
| 5 | Alvenaria | 3.190.022,89 | 190,01 | 5,95% |
| 6 | Impermeabilização | 1.463.560,64 | 87,17 | 2,73% |
| 7 | Instalações | 5.730.937,76 | 341,35 | 10,69% |
| 8 | Sist. Especiais | 1.410.423,59 | 84,01 | 2,63% |
| 9 | Climatização | 1.175.552,17 | 70,02 | 2,19% |
| 10 | Rev. Int. Parede | 2.002.760,72 | 119,29 | 3,74% |
| 11 | Teto | 1.410.266,57 | 84,00 | 2,63% |
| 12 | Pisos | 2.974.617,76 | 177,18 | 5,55% |
| 13 | Pintura | 3.275.186,53 | 195,08 | 6,11% |
| 14 | Esquadrias | 5.304.561,98 | 315,95 | 9,89% |
| 15 | Louças e Metais | 505.846,32 | 30,13 | 0,94% |
| 16 | Fachada | 1.515.128,74 | 90,25 | 2,83% |
| 17 | Complementares | 2.317.724,65 | 138,05 | 4,32% |
| 18 | Imprevistos | 696.945,16 | 41,51 | 1,30% |
| — | **TOTAL** | **53.619.739,59** | **3.193,73** | **100%** |

**DESTAQUES:**
- ✅ **CUB ratio 1,08** — eficiente para alto padrão (mediana ~1,28)
- ⚠️ **Supraestrutura R$ 594,64/m²** — 18,62%, valor absoluto alto (30 pav, HC + contenções)
- ⚠️ **Esquadrias R$ 315,95/m²** — 9,89%, significativo (alto padrão)
- ⚠️ **Instalações R$ 341,35/m²** — 10,69%, acima da média (edifício grande, 30 pav)
- ⚠️ **Pintura R$ 195,08/m²** — 6,11%, ACIMA da faixa típica (~100-130)
- ✅ **Louças e Metais separado** — R$ 505.846 (0,94%)
- ✅ **Climatização separada** — R$ 1.175.552 (2,19%)
- ✅ **Imprevistos 1,30%** — R$ 696.945

### Observações Técnicas

- Orçamento robusto com 1.580 linhas na Ger_Executivo e sheets dedicadas por disciplina
- Fundação: HC ø50cm (825m) e ø60cm (8.500m) + contenções (pranchas provisórias R$ 220.150)
- Prazo de obra longo: 57 meses (quase 5 anos) — reflete porte do empreendimento
- Concreto predominante: 40 MPa bombeável
- MOE por m² de área construída (padrão Cartesian)
