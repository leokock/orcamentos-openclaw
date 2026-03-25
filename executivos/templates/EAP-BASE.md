# EAP Base — Orçamento Executivo Cartesian

*Base: Estoril (Fonseca Neto) | 21 macrogrupos | R$ 44,4M | 14.492 m²*
*A ser refinada projeto a projeto*

---

## Macrogrupos (N1) — com fonte de dados

| # | MACROGRUPO | R$/m² | % | FONTE |
|---|-----------|-------|---|-------|
| 01 | Gerenciamento Técnico e Administrativo | 531,92 | 17,4% | 💰 VERBA |
| 02 | Movimentação de Terra | 16,07 | 0,5% | 💰 VERBA |
| 03 | Infraestrutura (Fundação) | 160,26 | 5,2% | 📋 PLANILHA |
| 04 | Contenção | 10,95 | 0,4% | 📋 PLANILHA |
| 05 | Supraestrutura | 709,97 | 23,2% | 📋 PLANILHA |
| 06 | Alvenaria | 167,52 | 5,5% | 🧊 BIM |
| 07 | Inst. Elétricas, Hidráulicas, GLP e Preventivas | 422,60 | 13,8% | 📋 PLANILHA |
| 08 | Climatização, Exaustão e Pressurização | 42,29 | 1,4% | 📋 PLANILHA |
| 09 | Equipamentos e Sistemas Especiais | 111,00 | 3,6% | 📋 PLANILHA |
| 10 | Instalações Especiais | — | — | 📋 PLANILHA |
| 11 | Rev. Argamassados Piso | — | — | 🧊 BIM |
| 12 | Rev. Argamassados Parede | — | — | 🧊 BIM |
| 13 | Rev. Argamassados Teto | — | — | 🧊 BIM |
| 14 | Impermeabilização | 70,77 | 2,3% | 🧊 BIM |
| 15 | Acabamentos Internos Parede | — | — | 🧊 BIM |
| 16 | Acabamentos Pisos e Pavimentações | — | — | 🧊 BIM |
| 17 | Acabamentos Internos Teto | — | — | 🧊 BIM |
| 18 | Pintura Interna | 139,13 | 4,5% | 🧊 BIM |
| 19 | Pintura de Fachada | — | — | 🧊 BIM / 📐 ARQ |
| 20 | Rev. Argamassados de Fachada | — | — | 🧊 BIM / 📐 ARQ |
| 21 | Acabamentos de Fachada | 181,17 | 5,9% | 🧊 BIM / 📐 ARQ |
| 22 | Esquadrias, Vidros e Ferragens | 312,41 | 10,2% | 📋 PLANILHA |
| 23 | Louças e Metais | — | — | 📋 PLANILHA |
| 24 | Cobertura | 17,97 | 0,6% | 📐 ARQ / 💰 VERBA |
| 25 | Serviços Complementares | 126,73 | 4,1% | 💰 VERBA |
| 26 | Imprevistos | 44,53 | 1,5% | 💰 VERBA (% sobre total) |

**TOTAL: R$ 3.065,28/m²** (1,02 CUB/SC dez/2025)

---

## Legenda de Fontes

- 🧊 *BIM* — Quantidade extraída do modelo 3D (Blender/IFC). Entra direto no sistema, sem aba na planilha
- 📋 *PLANILHA* — Quantidade extraída de PDF/IFC de projeto. Jarvis/Cartesiano processa e gera planilha
- 📐 *ARQ* — Quantidade extraída do projeto arquitetônico (análise de pranchas/modelo). Pode ser BIM ou planilha dependendo do nível de modelagem
- 💰 *VERBA* — Estimativa por base histórica (58 projetos calibrados + executivos reais)

---

## Abas da Planilha por Macrogrupo (correspondência Estoril)

| Macrogrupo | Abas do Estoril | Fonte |
|-----------|----------------|-------|
| 01 Gerenciamento | Ger_Tec e Adm, EPCs, CANTEIRO, Controle Tecnologico, Ensaios | 💰 VERBA |
| 02 Movimentação | (sem aba — VB) | 💰 VERBA |
| 03 Infraestrutura | Estacas, Aço_Estacas, Fundação Rasa, Visus-Infraestrutura, Aço_Infraestrutura | 📋 PLANILHA |
| 04 Contenção | (dentro de Infraestrutura) | 📋 PLANILHA |
| 05 Supraestrutura | Supraestrutura | 📋 PLANILHA |
| 06 Alvenaria | Visus-Alvenaria | 🧊 BIM |
| 07 Instalações E/H/GLP/PCI | INSTALAÇÕES, HIDROSSANITÁRIO, ELÉTRICO, TELEFONE, PCI, SPDA | 📋 PLANILHA |
| 08 Climatização | CLIMATIZAÇÃO | 📋 PLANILHA |
| 09 Equipamentos Especiais | (dentro de Instalações) | 📋 PLANILHA |
| 11-13 Revestimentos | Visus-Rev.Acab.Parede, Visus-Piso, Visus-Teto | 🧊 BIM |
| 14 Impermeabilização | Visus-Impermeabilização | 🧊 BIM |
| 15-17 Acabamentos | Visus-Rev.Acab.Parede, Visus-Piso, Visus-Soleiras | 🧊 BIM |
| 18 Pintura Interna | Rufos,Pintura,garagem,pergol | 🧊 BIM |
| 19-21 Fachada | (combinação BIM + análise ARQ) | 🧊 BIM / 📐 ARQ |
| 22 Esquadrias | ESQUADRIAS | 📋 PLANILHA |
| 23 Louças e Metais | LOUÇAS E METAIS | 📋 PLANILHA |
| 24 Cobertura | Visus-Telhado, Visus-Calha | 📐 ARQ |
| 25 Serv. Complementares | CHURRASQUEIRAS E SHAFTS, Piscinas, MOBILIÁRIO | 💰 VERBA |
| 26 Imprevistos | (% sobre total) | 💰 VERBA |

---

## Estrutura Ger_Executivo (EAP Completa)

A planilha Ger_Executivo organiza os itens em 5 níveis:
- *Nível 1:* Unidade Construtiva (ex: Torre, Embasamento)
- *Nível 2:* Célula Construtiva (ex: Subsolo 1, Tipo 1...14, Cobertura)
- *Nível 3:* Etapa (corresponde ao N1 da EAP)
- *Nível 4:* Subetapa (corresponde ao N2/N3)
- *Nível 5:* Serviço (item folha)

Exemplo de endereçamento: 3.5.4.3 = Unid.3 → Célula 5 → Etapa 4 → Subetapa 3

A distribuição por pavimento (Célula Construtiva) permite:
- Cronograma físico-financeiro por pavimento
- Curva de desembolso realista
- Controle de execução por frente de serviço

---

*Documento vivo — será atualizado conforme a EAP for refinada*
