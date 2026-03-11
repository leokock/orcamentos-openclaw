# Sense 106 — Índices de Orçamento Executivo

> Projeto: Sense 106 | Cliente: Holze Empreendimentos
> Criado: 06/03/2026 | Fonte: Orçamento Executivo (XLSX) + Apresentação (PDF)
> Extração: Sub-agente de calibração

---

## SEÇÃO 1 — DADOS DO PROJETO

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Nome do Projeto | — | Sense 106 | — |
| Código CTN | — | CTN-HLZ-S106 | — |
| Revisão | — | R00 | — |
| Localização | — | Porto Belo/SC | — |
| Incorporador/Cliente | — | Holze Empreendimentos | — |
| Área do Terreno | AT | 720,16 | m² |
| Área Construída | AC | 8.700,00 | m² |
| Unidades Habitacionais | UR | 60 | un |
| Total Unidades | UR | 60 | un |
| Nº Total Pavimentos | NP | 27 | un |
| Elevadores | ELEV | 2 | un |
| Prazo de Obra | — | 48 | meses |
| Data-base | — | Set/2024 | — |
| **CUB na Data-base** | — | **R$ 2.844,00** | **R$** |
| R$/m² Total | — | 3.515,51 | R$/m² |
| R$/m² (sem terreno) | — | 3.463,79 | R$/m² |
| CUB ratio | — | 1,24 | CUB |
| CUB ratio (sem terreno) | — | 1,22 | CUB |
| Tipo de Laje | — | N/D | — |
| Tipo de Fundação | — | N/D | — |
| Padrão Acabamento | — | Médio-Alto | — |

### Estrutura de Custos do Executivo

| Aspecto | Valor | Observação |
|---|---|---|
| **Tem ADM Incorporadora separado?** | N/D | — |
| **Tem MOE (Mão de Obra) separado?** | Não | MO incluída nos itens |
| Metodologia de rateio MOE | — | — |
| Custos diretos de obra (sem ADM/MOE) | R$ 25.275.750,91 | 82,6% do total |
| Custos indiretos (sem terreno) | R$ 4.859.213,98 | 15,9% do total |
| Terreno | R$ 450.000,00 | 1,5% do total |

### Mapeamento de Etapas do Executivo → Macrogrupos Padrão

| Categoria no Executivo | Macrogrupo Padrão | Observação |
|---|---|---|
| 01. Movimentação de Terra | 2-Mov.Terra | — |
| 02. Infraestrutura | 3-Infraestrutura | — |
| 03. Supraestrutura | 4-Supraestrutura | — |
| 04. Alvenaria | 5-Alvenaria | — |
| 05-08. Instalações (Elét+Com+Hidro+Prev/Gás) | 7-Instalações | Agrupadas |
| 09. Climatização/Exaustão | 9-Climatização | — |
| 10. Impermeabilização | 6-Impermeabilização | — |
| 11. Rev. Int. Piso/Parede | 10-Rev.Int.Parede + 12-Pisos | Separados 55/45% |
| 12. Rev./Acab. Teto | 11-Teto | — |
| 13. Acabamentos Piso/Parede | 10-Rev.Int.Parede + 12-Pisos | Separados 40/60% |
| 14. Pintura Interna | 13-Pintura | — |
| 15. Esquadrias/Vidros/Ferragens | 14-Esquadrias | — |
| 16. Cobertura | 17-Complementares | Reclassificada |
| 17. Fachada | 16-Fachada | — |
| 18. Equip./Sist. Especiais | 8-Sist.Especiais | — |
| 19. Louças e Metais | 15-Louças | — |
| 20. Serv. Complementares | 17-Complementares | — |
| 21. Imprevistos | 18-Imprevistos | — |
| Custos Indiretos (CI) | 1-Gerenciamento | Sem terreno |

---

## SEÇÃO 2 — PRODUTO IMOBILIÁRIO

### 2.1 Eficiência do Terreno

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| Coeficiente de Aproveitamento (CA) | AC / AT | 12,08 | 13,94 | 3,48 |
| Área por Unidade | AC / UR | 145,0 m²/un | 243,7 | 78,7 |
| Unidades por Terreno | UR / AT | 0,083 un/m² | 0,06 | 0,04 |

### 2.2 Infraestrutura de Apoio

| Índice | Fórmula | Valor | Referência KIR | Referência ADR |
|---|---|---|---|---|
| UR por Elevador | UR / ELEV | 30 | 22 | 47 |
| Elevadores por Pavimento | ELEV / NP | 0,074 | 0,10 | 0,43 |

### 2.3 Mix de Tipologias

| Tipologia | Qtd | % do Total | Área Média (m²/un) |
|---|---|---|---|
| Residencial | 60 | 100% | 145,0 |

### 2.4 Distribuição de Áreas por Pavimento

N/D — Levantamento não disponível no executivo

### 2.5 Custo por Unidade

| Índice | Fórmula | Valor |
|---|---|---|
| R$ / UR (todas) | Total / UR | R$ 509.749 |
| R$ / UR (sem terreno) | Total s/ terreno / UR | R$ 502.250 |
| CUB / UR | (R$/UR) / CUB | 179,3 CUB |

---

## SEÇÃO 3 — CUSTOS POR MACROGRUPO PARAMÉTRICO

| # | Macrogrupo | Valor (R$) | R$/m² | % | R$/m² Norm. Dez/23 |
|---|---|---|---|---|---|
| 1 | Gerenciamento Técnico/Admin | 4.859.214 | 558,53 | 16,1% | 540,62 |
| 2 | Movimentação de Terra | 149.821 | 17,22 | 0,5% | 16,67 |
| 3 | Infraestrutura | 2.033.142 | 233,70 | 6,7% | 226,21 |
| 4 | Supraestrutura | 7.512.492 | 863,51 | 24,9% | 835,74 |
| 5 | Alvenaria | 1.061.157 | 121,99 | 3,5% | 118,08 |
| 6 | Impermeabilização | 434.083 | 49,89 | 1,4% | 48,29 |
| 7 | Instalações (agrupado) | 2.805.796 | 322,50 | 9,3% | 312,13 |
| 8 | Sistemas Especiais | 1.064.716 | 122,38 | 3,5% | 118,46 |
| 9 | Climatização | 198.050 | 22,76 | 0,7% | 22,03 |
| 10 | Rev. Internos Parede | 1.382.930 | 158,96 | 4,6% | 153,87 |
| 11 | Teto | 557.344 | 64,06 | 1,9% | 62,02 |
| 12 | Pisos | 1.561.361 | 179,47 | 5,2% | 173,70 |
| 13 | Pintura | 1.225.835 | 140,90 | 4,1% | 136,40 |
| 14 | Esquadrias | 2.055.709 | 236,29 | 6,8% | 228,72 |
| 15 | Louças e Metais | 300.014 | 34,48 | 1,0% | 33,38 |
| 16 | Fachada | 825.485 | 94,88 | 2,7% | 91,83 |
| 17 | Complementares | 1.655.822 | 190,33 | 5,5% | 184,22 |
| 18 | Imprevistos | 451.995 | 51,95 | 1,5% | 50,28 |
| — | **TOTAL** | **30.134.965** | **3.463,79** | **100%** | **3.352,66** |

> **Nota:** Fator de normalização para CUB dez/2023 = 0.9679 (2752.67 / 2844.00)
> **Separação Piso/Parede:** Rev. Int. (55/45%) + Acabamentos (40/60%) conforme padrão base

---

## SEÇÃO 4 — ÍNDICES ESTRUTURAIS DETALHADOS

### 4.1 Supraestrutura

**⚠️ DADOS LIMITADOS** — Orçamento executivo não traz decomposição de concreto, aço, forma por elemento.

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| R$/m² supraestrutura | 863,51 | R$/m² | 548,40 | 595,82 |
| Posição vs benchmark | +57% | — | — | — |

> **Observação:** R$/m² supra acima do topo da faixa (560-630 base anterior, até 755 Catena). Compatível com Kirchner (R$ 548) se considerar data-base diferente ou laje mais complexa.

### 4.2 Infraestrutura

**⚠️ DADOS LIMITADOS** — Não há decomposição de fundação profunda vs rasa, tipo de estaca, quantidades.

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| R$/m² infraestrutura | 233,70 | R$/m² | 221,12 | 174,86 |
| Posição vs benchmark | ✅ Dentro (topo) | — | — | — |

---

## SEÇÃO 5 — ÍNDICES DE CONSUMO (Eficiência Construtiva)

**⚠️ DADOS NÃO DISPONÍVEIS** — Orçamento executivo não traz levantamento de áreas de serviço (alvenaria m², chapisco m², contrapiso m², etc.)

---

## SEÇÃO 6 — INSTALAÇÕES (Breakdown por Disciplina)

| Disciplina | Valor (R$) | R$/m² AC | % Instal. |
|---|---|---|---|
| Hidrossanitárias | 1.139.543 | 130,98 | 40,6% |
| Elétricas | 1.198.159 | 137,72 | 42,7% |
| Preventivas/Gás | 361.841 | 41,59 | 12,9% |
| Comunicações | 106.252 | 12,21 | 3,8% |
| **TOTAL** | **2.805.796** | **322,50** | **100%** |

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Total instalações / AC | 322,50 | R$/m² | 240,89 | 388,37 |
| Posição vs benchmark | ✅ Dentro (faixa 280-400) | — | — | — |

> **Nota:** Sem decomposição MO vs Material no executivo. Faixa esperada: MO 30-40%, Mat 60-70%.

---

## SEÇÃO 7 — ACABAMENTOS (PUs e MO)

**⚠️ DADOS NÃO DISPONÍVEIS** — Orçamento executivo traz valores totais por grupo, sem decomposição de PUs item a item.

### 7.1 Revestimentos de Parede

| Item | Estimativa |
|---|---|
| Rev. Int. Parede | R$ 158,96/m² (macrogrupo total) |

### 7.2 Pisos

| Item | Estimativa |
|---|---|
| Pisos | R$ 179,47/m² (macrogrupo total) |

### 7.3 Teto

| Item | Estimativa |
|---|---|
| Teto | R$ 64,06/m² (macrogrupo total) |

### 7.4 Pintura

| Item | Estimativa |
|---|---|
| Pintura | R$ 140,90/m² (macrogrupo total) |

### 7.5 Fachada

| Item | Estimativa |
|---|---|
| Fachada | R$ 94,88/m² (macrogrupo total) |

---

## SEÇÃO 8 — ESQUADRIAS (Detalhamento)

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz decomposição por tipo (alumínio, madeira, guarda-corpo, etc.)

| Item | Estimativa |
|---|---|
| Esquadrias total | R$ 236,29/m² AC |
| Posição vs benchmark | ✅ Dentro (240-330) |

---

## SEÇÃO 9 — SISTEMAS ESPECIAIS E EQUIPAMENTOS

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz decomposição por tipo de sistema.

| Item | Estimativa |
|---|---|
| Sist. Especiais total | R$ 122,38/m² AC |
| Climatização | R$ 22,76/m² AC |
| **Total Sist.Esp + Clim** | **R$ 145,14/m²** |
| Posição vs benchmark | 🔽 Abaixo (faixa 170-240) |

> **Especificidades mencionadas:** Infra climatização + Painéis solares + Infra carros elétricos

---

## SEÇÃO 10 — CUSTOS INDIRETOS DETALHADOS (CI)

### 10.1 Projetos e Consultorias

| Disciplina | Valor (R$) | R$/m² AC |
|---|---|---|
| Projetos/Consultorias | 598.398 | 68,78 |

> Inclui: Ampli R$ 33.900, Prevision R$ 71.800

### 10.2 Taxas e Licenças

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Taxas/Documentos | 1.106.677 | 127,20 |

### 10.3 Equipe Administrativa

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz composição detalhada da equipe.

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Administração/Canteiro | 2.174.995 | 249,94 |

### 10.4 Proteção Coletiva (EPCs)

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Segurança/Meio Ambiente | 479.062 | 55,06 |

### 10.5 Equipamentos de Carga/Obra

| Item | Valor (R$) | R$/m² AC |
|---|---|---|
| Equipamentos | 500.082 | 57,48 |

### 10.6 Ensaios Tecnológicos

N/D — Não segregado no executivo

### 10.7 Resumo CI (sem terreno)

| Subgrupo | Valor (R$) | R$/m² | % do CI | % do Total |
|---|---|---|---|---|
| Projetos e Consultorias | 598.398 | 68,78 | 12,3% | 2,0% |
| Taxas e Licenças | 1.106.677 | 127,20 | 22,8% | 3,7% |
| Administração/Canteiro | 2.174.995 | 249,94 | 44,7% | 7,2% |
| Segurança/Meio Ambiente | 479.062 | 55,06 | 9,9% | 1,6% |
| Equipamentos | 500.082 | 57,48 | 10,3% | 1,7% |
| **TOTAL CI (sem terreno)** | **4.859.214** | **558,53** | **100%** | **16,1%** |

---

## SEÇÃO 11 — LOUÇAS E METAIS (Por Unidade)

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz decomposição por item.

| Índice | Valor | Un |
|---|---|---|
| Louças+Metais / UR | R$ 5.000 | R$/UR |
| Louças+Metais / AC | 34,48 | R$/m² |

---

## SEÇÃO 12 — PRODUTIVIDADE E PRAZO

| Índice | Fórmula | Valor | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Ritmo de construção | AC / Prazo | 181 m²/mês | 306 | 308 |
| Burn rate mensal | Total / Prazo | R$ 0,64 M/mês | R$ 863k | R$ 1,12M |
| Meses por pavimento | Prazo / NP | 1,8 | 1,7 | 5,1 |
| UR por mês | UR / Prazo | 1,3 un/mês | 1,3 | 3,9 |
| Custo / mês / m² | (Total/Prazo) / AC | 73 R$/m²/mês | 80,5 | 100,8 |

> **Observação:** Ritmo de 181 m²/mês está 41% abaixo das referências (~300 m²/mês). Prazo de 48 meses é longo para 8.700 m².

---

## SEÇÃO 13 — IMPERMEABILIZAÇÃO (Detalhamento)

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz decomposição por sistema.

| Índice | Valor | Un | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Impermeabilização / AC | 49,89 | R$/m² | 66,94 | 85,45 |
| Posição vs benchmark | 🔽 Abaixo (faixa 55-90) | — | — | — |

---

## SEÇÃO 14 — COMPLEMENTARES E FINAIS

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz decomposição detalhada.

| Item | Valor (R$) | R$/m² |
|---|---|---|
| Serv. Complementares | 1.625.997 | 186,96 |
| Cobertura (reclassificada) | 29.825 | 3,43 |
| **Total Complementares** | **1.655.822** | **190,33** |

---

## SEÇÃO 15 — BENCHMARK (ADM PRELIMINAR)

**⚠️ DADOS NÃO DISPONÍVEIS** — Executivo não traz aba comparativa com outros projetos.

---

## SEÇÃO 16 — DESTAQUES E ALERTAS

### ⚠️ Acima da Média
- **Supraestrutura: R$ 863/m²** — 57% acima KIR (R$ 548), 45% acima ADR (R$ 596). Possível laje mais complexa ou data-base de PUs diferente.
- **Gerenciamento: R$ 559/m² (16,1%)** — no topo da faixa. Pode refletir prazo longo (48 meses) diluindo menos custos fixos.

### ✅ Dentro da Faixa
- **Instalações: R$ 323/m²** — dentro da faixa mais estável da base (280-400).
- **Infraestrutura: R$ 234/m²** — no topo da faixa (115-235), consistente com Porto Belo.
- **Alvenaria: R$ 122/m²** — dentro (100-170).
- **Esquadrias: R$ 236/m²** — dentro (240-330).
- **Pintura: R$ 141/m²** — dentro (95-187).
- **Fachada: R$ 95/m²** — dentro (100-180).

### 🔽 Abaixo da Média
- **Teto: R$ 64/m²** — abaixo do esperado (80-120). Possível forro mais simples.
- **Impermeabilização: R$ 50/m²** — abaixo (55-90). Menos áreas impermeabilizadas ou sistema mais econômico.
- **Sistemas Especiais: R$ 122/m²** — abaixo (170-240). Apesar de mencionar climatização + solar + carro elétrico, o valor é conservador.

### 📝 Particularidades
- **Piso vinílico nos aptos** (mencionado na apresentação) — sistema mais econômico que porcelanato.
- **Infra climatização + painéis solares + carros elétricos** — features listadas, mas custo total de Sist.Especiais + Climatização = R$ 145/m² está abaixo da faixa de projetos com esses sistemas (>200 R$/m²). Possível que seja infra apenas, sem equipamentos.
- **Prazo de 48 meses** — um dos mais longos da base (só Catena 54m e Atlantia 65m). Ritmo lento (181 m²/mês).
- **Porto Belo/SC** — mesmo mercado que Zapata (CUB 1,07), Viva Perequê (1,39). CUB 1,22 está intermediário.
- **27 pavimentos** — prédio alto, mas terreno pequeno (720 m²). Verticalização intensa.

---

## RESUMO DE ÍNDICES GLOBAIS

| Indicador | Valor | Un |
|---|---|---|
| **Custo total** | **R$ 30.584.965** | R$ |
| **Custo total (sem terreno)** | **R$ 30.134.965** | R$ |
| **R$/m²** | **3.515,51** | R$/m² |
| **R$/m² (sem terreno)** | **3.463,79** | R$/m² |
| **R$/m² normalizado (dez/23)** | **3.352,66** | R$/m² |
| **CUB ratio** | **1,24** | CUB |
| **CUB ratio (sem terreno)** | **1,22** | CUB |
| **R$/UR** | **R$ 509.749** | R$/UR |
| **AC/UR** | **145,0** | m²/un |
| Concreto supra / AC | N/D | m³/m² |
| Taxa aço supra | N/D | kg/m³ |
| Forma / AC | N/D | m²/m² |
| Alvenaria / AC | N/D | m²/m² |
| Forro / AC | N/D | m²/m² |
| Pintura parede / AC | N/D | m²/m² |
| Fachada / AC | N/D | m²/m² |
| Estacas / AC | N/D | m/m² |
| MO instalações / AC | N/D | R$/m² |
| Ritmo construção | 181 | m²/mês |
| Burn rate | R$ 0,64 M | R$/mês |

---

> **Fonte:** Orçamento Executivo Sense 106 (Set/2024)
> **Extraído em:** 06/03/2026
> **Notas:** Dados de levantamento (quantidades, PUs item a item) não disponíveis no executivo. Análise baseada em totais por macrogrupo. Normalização para CUB dez/2023 aplicada para calibração.
