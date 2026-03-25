# Memorial de Execucao — Orcamento Executivo Electra Towers (Thozen)

**Cliente:** Thozen
**Empreendimento:** Electra Towers
**Localizacao:** Rua Rubens Alves, Balneario Pereque, Porto Belo/SC
**Tipologia:** Residencial vertical (2 torres, 34 pavimentos cada)
**AC:** 36.088,85 m2
**Unidades:** 342 residenciais + 6 comerciais = 348
**Vagas:** 305
**Pavimentos:** 1 Terreo + 5 Garagens + 1 Lazer + 24 Tipo + 3 tecnicos (por torre)
**Prazo de obra:** 36 meses
**Fundacao:** Estacas helice continua (O50cm e O60cm)
**Projetista principal:** R. Rubens Alves (eletrico, telefonico, ventilacao)

---

## Indice de Disciplinas

| # | Disciplina | Status | Revisao | Arquivo-chave |
|---|-----------|--------|---------|---------------|
| 01 | Estrutura | Briefing R00 | R00 | `briefings/estrutura-r00.md` |
| 02 | Arquitetura | Briefing R00 | R00 | `briefings/arquitetura-r00.md` |
| 03 | Alvenaria | Briefing R00-R01, DXF pendente | R01 | `briefings/alvenaria-r01.md` |
| 04 | Esquadria | Briefing R00 | R00 | `briefings/esquadria-r00.md` |
| 05 | Hidraulico | Briefing R00 | R00 | `briefings/hidraulico-r00.md` |
| 06 | Sanitario | Briefing R00 | R00 | `briefings/sanitario-r00.md` |
| 07 | PCI Civil | Briefing R00 | R00 | `briefings/pci-civil-r00.md` |
| 08 | PCI Eletrico | Briefing R00 | R00 | `briefings/pci-eletrico-r00.md` |
| 09 | Eletrico | Discipline pack R01 + Memorial | R01 | `entregas/eletrico-r01-memorial.md` |
| 10 | Telefonico | Briefing R00 + dados IFC | R00 | `briefings/telefonico-r00.md` |
| 11 | SPDA | Briefing R00 | R00 | `briefings/spda-r00.md` |
| 12 | Ventilacao | Briefing R00-R02 (DWG bloqueado) | R02 | `briefings/ventilacao-r02.md` |
| 13 | Exaustao | Briefing R00-R02 (DXF processado) | R02 | `briefings/exaustao-r02.md` |
| 14 | Ar-Condicionado | Briefing R00-R01 (DWG bloqueado) | R01 | `briefings/ar-condicionado-r01.md` |
| -- | Tecnico/Adm | Analise EAP + preenchimento | R00 | `entregas/electra_analise_tecnico_adm.md` |
| -- | EAP | Reestruturada em 4 UCs | v2 | `entregas/EAP-Electra-4UCs-v2.xlsx` |
| -- | Consolidado | R00 -> R01 -> R02 -> R03 | R03 | `entregas/CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx` |

---

## 1. Estrutura (EAP e Organizacao do Orcamento)

### EAP — Estrutura Analitica do Projeto

**Decisao:** Reorganizar de 2 UCs para 4 UCs:
- UC1: **Despesas Indiretas** (ex-Gerenciamento Tecnico e Administrativo)
- UC2: **Embasamento** (infraestrutura + fundacoes + etapas "-EMBASSAMENTO")
- UC3: **Torre A** (etapas "-TORRE A")
- UC4: **Torre B** (etapas "-TORRE B")

**Fonte:** Planilha original `CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx` (684 linhas, 28 colunas)
**Entrega:** `entregas/EAP-Electra-4UCs-v2.xlsx` (com formatacao original preservada — Poppins, bold por nivel, merges, formulas)

**Importacao no Memorial Cartesiano:**
- 108 itens importados (N1-N3): 2 UCs, 27 Celulas, 79 Etapas
- CPUs (N4): vinculacao manual (match automatico falhou — nomenclaturas divergentes entre EAP e base de CPUs)
- Project ID Memorial: `cdff0592-fb3c-4c13-9516-efde6b56b336`

### Gestao de Projetos (aba PROJETOS)

**Decisao:** Preencher com todos os IFC/DWG recebidos, por disciplina
**Entrega:** `entregas/Projetos-Electra-Preenchido.xlsx`

### Planilha R00 — Analise do que ja existia

**Achados na planilha original:**
- 835 insumos + 926 CPUs ja na base
- Estacas preenchidas (Torre 1: O50cm 17un + O60cm 406un)
- Gerenciamento consolidado: R$ 10,3M (R$ 286/m2)
- Instalacoes consolidado: R$ 9,8M (R$ 271/m2)
- Sist. Especiais consolidado: R$ 3,9M (R$ 109/m2)
- Supraestrutura muito baixo: R$ 152k (R$ 4/m2 — incompleto, benchmark ~R$ 500/m2)
- Infraestrutura muito baixo: R$ 507k (R$ 14/m2 — incompleto, benchmark ~R$ 137/m2)
- #REF! em Impermeabilizacao
- Disciplinas zeradas: Alvenaria, Loucas, Esquadrias, Climatizacao, Revestimentos, Fachada, Teto

**Benchmark utilizado:** SOHO 538 (R$ 2.161/m2), For Seasons (R$ 3.520/m2), Eliat (R$ 3.642/m2)

---

## 2. Gerenciamento Tecnico e Administrativo

**Fonte:** EAP original + base de 926 CPUs do Electra
**Analise:** 117 servicos na EAP, 43 com preco definido, 74 sem preco
**Match automatico com base de CPUs:** 0 itens (nomenclaturas completamente diferentes)

**Decisao:** Itens de gerenciamento sao servicos intelectuais, consultorias e custos operacionais — NAO constam em bancos tradicionais (SINAPI, PINI). Fontes recomendadas: historico Cartesian, cotacoes, tabelas de honorarios (CAU, CREA, AsBEA).

**Entregas:**
- `entregas/electra_analise_tecnico_adm.md` — analise detalhada dos 117 servicos
- `entregas/Tec_Adm_Electra_Preenchido.xlsx` — planilha com recomendacoes por item
- `entregas/Justificativas_Tec_Adm_Electra_Base_Cartesian.docx` — justificativas

**Pendente:** Cotacoes reais para os 74 itens sem preco (laboratorios, empreiteiras, consultorias)

---

## 3. Estrutura (Infraestrutura + Supraestrutura)

**Fonte:** IFC `1203 - THOZEN - RUBENS ALVES - BLOCOS+RAMPAS DE ACESSO - R26.ifc`
**Dados extraidos do IFC:**
- Volume estimado de concreto: ~12.784 m3
- Elementos contados: 1.531 pilares, 3.531 vigas, 1.527 lajes, 70 infra
- Distribuicao por pavimento mapeada

**Dados faltantes (criticos):**
- Estacas: tipo, diametro, comprimento, quantidade (parcialmente na aba Estacas da R00)
- Classes de concreto (fck por elemento)
- Armacao (taxa de aco, bitolas)
- Areas de forma (m2)
- Tipo de laje (macica ou nervurada — espessura 28cm sugere macica, mas pode ser nervurada + capa)

**Decisao:** Aguardar memorial descritivo estrutural e prancha de fundacoes para complementar.

**Entrega:** `briefings/estrutura-r00.md` + `briefings/estrutura-r00.json`

---

## 4. Alvenaria

**Fonte:** 18 DWGs R01 (pre-executivo)
**Bloqueador:** DWG em formato binario (AutoCAD 2018/2019/2020) — nao processavel sem ODA File Converter
**Dados parciais na R00:** Terreo + 1o Subsolo preenchidos (Bloco 9cm, 14cm, 19cm)

**Pavimentos mapeados:** 01 Terreo, 02-06 G1-G5, 07 Lazer, 08-31 Tipo (x24), 32 Res/Cob

**Decisao:** Solicitar DXF ao projetista ou instalar ODA File Converter para conversao automatica.

**Scripts criados:** `scripts/extrair_alvenaria_dxf.py`, `scripts/processar_todos_alvenaria.sh`
**Entrega:** `briefings/alvenaria-r00.md`, `briefings/alvenaria-r01.md`

**Pendente:** Conversao DWG -> DXF e extracao automatizada

---

## 5. Esquadrias

**Fonte:** DWGs de arquitetura
**Dados extraidos:** Mapa preliminar de tipologias (portas madeira P1/P2/P3, aluminio, vidros temperados)
**Entrega:** `briefings/esquadria-r00.md` + `briefings/esquadria-r00.json`

**Pendente:** Quantitativos detalhados por pavimento, caderno de especificacoes

---

## 6. Instalacoes Hidrossanitarias

**Fonte:** IFCs + DWGs rev.01
**Entregas:** `briefings/hidraulico-r00.md`, `briefings/sanitario-r00.md`

**Pendente:** Extracao detalhada de tubulacoes por diametro e metragem

---

## 7. Instalacoes Eletricas

**Fonte primaria:** 9 IFCs rev.01 (1 por pavimento) — Projetista R. Rubens Alves
**Referencia de precos:** Elizabeth II Royal Home (Gessele, Itapema) — R$ 213/m2

**Quantitativos extraidos dos IFCs:**
- Luminarias: 4.655 un (837 por pavimento unico, tipo x24 = 3.984)
- Eletrodutos: ~213.000 trechos (7 faixas de diametro: 3/4" a 4")
- Distribuicao completa por pavimento

**Decisao:** R$/m2 adotado R$ 190/m2 (ajuste de -10.8% vs Elizabeth II por ser medio-alto padrao, nao alto puro)
**Distribuicao por 13 subgrupos:** Subestacao 18%, MO 41%, Barramento 6.8%, Gerador 7%, Entrada 12.4%, etc.

**Total:** R$ 6.856.881,50 (R$ 190/m2)

**Relatorio de confianca:**
- Verde (3%): luminarias + eletrodutos (rastreaveis ao IFC)
- Amarelo (56%): subgrupos referenciados no Elizabeth II
- Vermelho (41%): MO, gerador, quadros, tomadas, cabos (sem fonte direta)

**Entregas:**
- `entregas/eletrico-r01-discipline-pack.xlsx`
- `entregas/eletrico-r01-memorial.md` / `.docx`
- `entregas/eletrico-r01-confianca.md`
- `entregas/eletrico-r01-por-pavimento.xlsx`

**Pendente:** Processar 18 DWGs para especificacoes tecnicas, cotacoes de subestacao e gerador, detalhamento de quadros e tomadas

---

## 8. Telecomunicacoes (Cabeamento Estruturado)

**Fonte:** 9 IFCs rev.01 + 18 DWGs rev.01 — Projetista R. Rubens Alves

**Quantitativos extraidos dos IFCs:**
- 46 pontos de dados (RJ45) — concentrados no Terreo
- 44 pontos de voz (RJ11) — Terreo + Tipo
- ~648 caixas de passagem (4x2, 4x4, octogonais)
- ~33.400 m de eletrodutos (incluindo Tipo x24)
- 33 m de eletrocalhas (G1 apenas — shaft vertical)
- 3.694 acessorios de fixacao

**Dados NAO modelados nos IFCs (pendentes):**
- Metragens de cabos UTP (CAT6/CAT6A)
- Racks de telecomunicacoes (quantidade, localizacao)
- Patch panels (tipo, portas)
- DG (Distribuidor Geral)
- Diametros de eletrodutos (buscar em DWGs)
- Pontos logicos nas garagens

**Entregas:**
- `briefings/telefonico-r00.md`
- `entregas/relatorio-extracao-telefonico-thozen.md`
- `entregas/thozen-electra-telefonico-consolidado.json`

**Pendente:** Preenchimento da aba de Telecomunicacao na planilha R00 (proxima acao)

---

## 9. SPDA (Para-raios)

**Fonte:** DWGs (sem IFC)
**Entrega:** `briefings/spda-r00.md` + `briefings/spda-r00.json`

**Pendente:** Extracao detalhada — depende de conversao DWG -> DXF

---

## 10. PCI (Prevencao e Combate a Incendio)

### PCI Civil
**Fonte:** IFC rev.01 (Torre A e B) + 11 pranchas DWG
**Quantitativos extraidos:** 78 abrigos, 73 extintores, 67m tubulacao (SUBESTIMADO)
**Entrega:** `briefings/pci-civil-r00.md` + resumo + anexo pavimentos

**Pendentes criticos:**
- Reservatorios e bombas de incendio (nao encontrados no IFC)
- Metragem real de tubulacao (espera-se >> 67m)
- Sistema de sprinklers (nao identificado)
- Memorial descritivo

### PCI Eletrico
**Fonte:** IFC + DWGs
**Entrega:** `briefings/pci-eletrico-r00.md`

---

## 11. Ventilacao Mecanica (Escadas Pressurizadas)

**Fonte:** DWG R05 (RA_EVM_LEGAL_PROJETO_R05.dwg, 5.39 MB) — Projetista Rubens Alves
**Bloqueador:** DWG binario nao processavel. Extracao via strings: 0 palavras-chave em 72.678 strings.

**Premissas adotadas (baseadas em NBR 14880:2024 — NAO VALIDADAS):**
- 2 ventiladores centrifugos (8.000-12.000 m3/h, 5-7.5 CV)
- 64 dampers corta-fogo 90min
- 200 m de duto vertical O600mm
- 42 grelhas/difusores
- Custo estimado: R$ 342k - R$ 545k (com BDI + contingencia)

**Decisao:** Todos os 46 itens marcados como NAO VALIDADO. Incerteza mantida em +/- 30-50%.

**Entregas:** `briefings/ventilacao-r00.md` ate `briefings/ventilacao-r02.md` + checklists
**Pendente:** Solicitar DXF + memorial descritivo ao projetista Rubens Alves

---

## 12. Exaustao

**Fonte:** DXF processado com sucesso
**Entregas:** `briefings/exaustao-r00.md` ate `briefings/exaustao-r02.md`
**Dados:** Processamento DXF com dados reais extraidos

---

## 13. Ar-Condicionado e Climatizacao

**Fonte:** DWG R05 (RA_ARC_EXE_00_TODAS CAD_R05.dwg, 5.0 MB)
**Bloqueador:** DWG binario nao processavel (mesmo problema da Ventilacao)
**Estimativa parametrica:** R$ 80-150/m2 AC -> R$ 1,6M - 4,5M (+/- 30-40%)

**Entregas:** `briefings/ar-condicionado-r00.md`, `briefings/ar-condicionado-r01.md`
**Pendente:** Conversao DWG -> DXF ou dados do projetista

---

## 14. Consolidacao Geral (R01 -> R02 -> R03)

**R01:** Primeira versao consolidada com todas as disciplinas disponiveis
**R02:** Formato Elizabeth II + memorial rastreavel + doc Word
**R03 (atual):** Ajustado (Mov.Terra, Loucas, Complementares)

| Item | Valor |
|------|-------|
| **Total** | **R$ 161,3M** |
| **R$/m2** | **R$ 4.469** |
| **CUB Ratio** | **1.48** |

**Entregas:**
- `entregas/CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx`
- `entregas/CTN-TZN_ELT-Orcamento-Executivo-R03-MEMORIAL.docx`

**Modelo de rastreabilidade per-item:**
- Verde: Proj. [Projetista] [IFC/DXF] [rev]
- Amarelo: Param. base Cartesian
- Vermelho: Estimado

---

## Checklist de Preenchimento — Planilha R00

### Abas Gerais
- [ ] **CAPA** — Falta preencher
- [x] **PROJETOS** — Preenchido (24/mar)
- [x] **EAP** — Reestruturada em 4 UCs (24/mar)
- [ ] **EAP Analise** — Falta preencher
- [ ] **CPU** — Falta vincular com EAP
- [ ] **Insumos** — Falta validar precos
- [ ] **BASES** — Falta preencher

### Abas por Disciplina
- [ ] Ger_Tec e Adm
- [ ] Ger_Executivo
- [ ] Estacas
- [ ] Fund. Rasa / Contencao
- [ ] Resumo Estrutura
- [ ] Escoramento
- [ ] ARQUITETURA
- [ ] LOUCAS E METAIS
- [ ] ESQUADRIAS
- [ ] Exaustao e Climatizacao
- [ ] MOBILIARIO
- [ ] Equipamentos Especiais
- [ ] EPCs
- [ ] CANTEIRO
- [ ] Cont.Tecnol.

### Disciplinas tecnicas
- [ ] Estacas
- [ ] Fundacao Rasa / Contencao
- [ ] Resumo Estrutura
- [ ] Escoramento
- [ ] Impermeabilizacao
- [ ] Loucas e Metais
- [ ] Equipamentos Especiais
- [ ] Piscina
- [ ] Eletrico
- [ ] Hidrossanitario
- [ ] PPCI
- [ ] Sprinkler
- [ ] Telecomunicacao (proxima)
- [ ] Gas
- [ ] Automacao
- [ ] Climatizacao
- [ ] Iluminacao
- [ ] Mobiliario

---

## Bloqueadores Tecnicos

1. **DWG binario** — Ventilacao, Ar-Condicionado, Alvenaria precisam de conversao DWG -> DXF (ODA File Converter ou solicitar DXF ao projetista Rubens Alves)
2. **Memorial descritivo** — necessario para validar premissas de Ventilacao, PCI, Climatizacao
3. **CPUs no Memorial** — Leo precisa vincular N4 manualmente (match automatico falhou)

---

## Projetistas Identificados

| Disciplina | Projetista | Fonte |
|-----------|-----------|-------|
| Eletrico, Telefonico, Ventilacao | R. Rubens Alves | IFC/DWG rev.01 |
| Estrutura | (a confirmar) | IFC rev.26 |
| Arquitetura | (a confirmar) | — |

---

## Arquivos-chave

| Arquivo | Descricao |
|---------|-----------|
| `CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx` | Planilha original do cliente |
| `CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx` | Ultima versao consolidada (IA) |
| `CTN-TZN_ELT-Orcamento-Executivo-R03-MEMORIAL.docx` | Memorial rastreavel R03 |
| `REVISAO-ELECTRA-R00.md` | Analise detalhada da planilha R00 |
| `briefings/*.md` | 14 briefings por disciplina |
| `scripts/*.py` | Scripts de extracao e processamento |
| **Este arquivo** | `log-execucao.md` — memorial de execucao |

---

## Convencoes deste Memorial

Este documento e organizado **por disciplina**, nao por dia. Cada secao registra:
1. **Fontes** — de onde veio cada informacao (IFC, DWG, briefing, base PU)
2. **Decisoes** — escolhas feitas e justificativas
3. **Quantitativos** — dados extraidos e premissas
4. **Entregas** — arquivos gerados
5. **Pendentes** — dados faltantes, validacoes necessarias

**Regra de edicao:** Claude so adiciona no final de cada secao. Leo pode editar qualquer parte. Este MD sera a base do memorial Word final do projeto.

---

*Criado em 2026-03-25 | Atualizado continuamente durante o projeto*
