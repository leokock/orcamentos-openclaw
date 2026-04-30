# Terrassa Dom Bosco — Índices de Orçamento Executivo

> Extração de índices a partir de orçamento executivo detalhado (EAP XLSX) e apresentação oficial (PDF).
> Projeto: Terrassa / Dom Bosco
> Data-base: Nov/2022
> Extraído em: 10/03/2026

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Terrassa Dom Bosco | — |
| Código CTN | — | CTN-TRS-DBS | — |
| Revisão | — | R02 | — |
| Localização | — | Dom Bosco, Itajaí/SC | — |
| Endereço | — | N/D | — |
| Incorporador/Cliente | — | Terrassa | — |
| Área do Terreno | AT | N/D | m² |
| Área Construída | AC | 9.764,67 | m² |
| Área Privativa | — | N/D | m² |
| Unid. Habitacionais | UR_H | 112 | un |
| Unid. Comerciais | UR_C | 0 | un |
| Estúdios | UR_E | 0 | un |
| Total Unidades | UR | 112 | un |
| Nº Total Pavimentos | NP | N/D | un |
| Nº Pavimentos Tipo | NPT | N/D | un |
| Nº Pav. Garagem | NPG | N/D | un |
| Elevadores | ELEV | 2¹ | un |
| Vagas Estacionamento | VAG | N/D | un |
| Prazo de Obra | — | 36 | meses |
| Data-base | — | Nov/2022 | — |
| **CUB na Data-base** | — | **R$ 2.633,22** | **R$** |
| R$/m² Total | — | 2.289,53 | R$/m² |
| CUB ratio | — | 0,87 | CUB |
| Tipo de Laje | — | N/D (cubetas mencionadas no EAP) | — |
| Tipo de Fundação | — | Hélice Contínua (estimativa) + Blocos Coroamento | — |
| Padrão Acabamento | — | Médio-Alto | — |

¹ Estimado a partir do EAP (2 elevadores orçados a R$ 261.192,12 cada).

**Notas:**
- AC e número de unidades back-calculados a partir do total (R$ 22.356.494,19), R$/m² (R$ 2.289,53) e R$/unidade (R$ 199.611,56) da apresentação.
- Área do terreno, nº de pavimentos, vagas e área privativa NÃO constam nos documentos disponíveis.
- CUB/SC nov/2022 = R$ 2.633,22 (conforme apresentação oficial).

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | Sim | EAP item 01 "INCORPORAÇÃO" = R$ 232.500 (incluído no Gerenciamento) |
| **Tem Projetos separado?** | Sim | EAP item 02 "PROJETOS" = R$ 441.211,99 (incluído no Gerenciamento) |
| **Tem MOE (Mão de Obra) separado?** | Sim | MOE aberta por disciplina dentro de cada etapa da EAP |
| Metodologia de rateio MOE | — | MOE alocada por etapa (supraestrutura, alvenaria, revestimentos, etc.) |
| Custos Indiretos (Gerenciamento) | R$ 3.224.160,12 | 14,42% — inclui incorporação, projetos, taxas, canteiro, ADM obra |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo (EAP) | Macrogrupo Padrão | Observação |
|---|---|---|
| CI 01-Incorporação + 02-Projetos + 03-Taxas + 04-Canteiro/ADM | 1-Gerenciamento | Total custos indiretos |
| CD 20.002-Mov. Terra | 2-Mov. Terra | Terraplanagem e bota-fora |
| CD 01-Contenções e Fundações | 3-Infraestrutura | HC estimada + blocos + vigas baldrame |
| CD 02-Supraestrutura | 4-Supraestrutura | Formas, armação, concreto, escoramento, MO |
| CD 03-Alvenaria e Vedações | 5-Alvenaria | Blocos cerâmicos + concreto celular + MO |
| CD 10-Impermeabilizações | 6-Impermeabilização | Todos os sistemas |
| CD 04+05+06+07-Instalações | 7-Instalações | Elétricas + Hidro + Preventivo + GLP |
| CD 13-Elevadores + 17-Inst.Complementares | 8-Sist. Especiais | Elevadores + interfonia/CFTV/automação |
| CD 08-Climatização e Exaustão | 9-Climatização | Separado (infra clim + exaustão + instalação AC) |
| CD 09.001+09.004-Rev. Argamassa Internos | 10-Rev. Int. Parede | Chapisco + reboco int + MO interna |
| CD 12-Forros | 11-Teto | Gesso mineral + negativos + sancas |
| CD 09.002+11-Contrapiso + Rev. Cerâmicos | 12-Pisos | Contrapiso + pisos + azulejos + rodapés + MO |
| CD 14-Pinturas | 13-Pintura | Internas + externas (materiais + MO) |
| CD 15-Esquadrias | 14-Esquadrias | Alumínio + madeira + PCF + ferragens + vidros |
| CD 18-Louças e Metais | 15-Louças e Metais | Louças + metais (valor baixo, só áreas comuns) |
| CD 09.003+09.005-Rev. Argamassa Externos | 16-Fachada | Chapisco + reboco ext + MO externa |
| CD 16+19+20(excl 20.002)-Complementares | 17-Complementares | Rev. complementares + limpeza + infra interna + mob + paisagismo |
| (não contemplado) | 18-Imprevistos | Não há verba de imprevistos na EAP |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % |
|---|---|---|---|---|
| 1 | Gerenciamento | 3.224.160,12 | 330,19 | 14,42% |
| 2 | Mov. Terra | 175.800,00 | 18,00 | 0,79% |
| 3 | Infraestrutura | 1.355.082,02 | 138,77 | 6,06% |
| 4 | Supraestrutura | 4.298.496,86 | 440,21 | 19,23% |
| 5 | Alvenaria | 1.168.205,51 | 119,64 | 5,23% |
| 6 | Impermeabilização | 282.800,18 | 28,96 | 1,26% |
| 7 | Instalações | 2.323.537,12 | 237,95 | 10,39% |
| 8 | Sist. Especiais | 668.853,99 | 68,50 | 2,99% |
| 9 | Climatização | 557.429,00 | 57,09 | 2,49% |
| 10 | Rev. Int. Parede | 1.401.601,35 | 143,54 | 6,27% |
| 11 | Teto | 537.433,44 | 55,04 | 2,40% |
| 12 | Pisos | 1.970.722,03 | 201,82 | 8,81% |
| 13 | Pintura | 1.078.015,30 | 110,40 | 4,82% |
| 14 | Esquadrias | 1.438.209,23 | 147,29 | 6,43% |
| 15 | Louças e Metais | 35.001,30 | 3,58 | 0,16% |
| 16 | Fachada | 532.690,60 | 54,55 | 2,38% |
| 17 | Complementares | 1.308.456,14 | 134,00 | 5,85% |
| 18 | Imprevistos | 0,00 | 0,00 | 0,00% |
| — | **TOTAL** | **22.356.494,19** | **2.289,53** | **100%** |

**DESTAQUES:**
- ⚠️ **CUB ratio 0,87** — MUITO ABAIXO da mediana (~1,28). Possíveis causas: data-base nov/2022 com custos pré-inflação, padrão médio-alto (não alto), sem imprevistos
- ⚠️ **Imprevistos 0%** — orçamento sem verba de contingência
- 🔽 **Louças e Metais R$ 3,58/m²** — apenas louças de áreas comuns (aptos sem louças/metais)
- ⚠️ **Gerenciamento 14,42%** — inclui incorporação (R$ 232.500) e projetos (R$ 441.212)
- ✅ **Climatização separada** — R$ 557.429 (2,49%) — infra + exaustão + instalação AC
- 🔽 **Fachada R$ 54,55/m²** — baixo, apenas reboco + chapisco externo (sem ACM/pele de vidro)

### Limitações da Extração

- Dados extraídos da EAP Comentada (xlsx) que é o orçamento executivo completo com ~1.194 linhas de serviço
- PDFs de apresentação e executivo usados para validar AC, CUB, totais e data-base
- Área construída e unidades foram back-calculados (não informados diretamente)
- Sem informação de nº de pavimentos, vagas, área terreno nos documentos disponíveis
