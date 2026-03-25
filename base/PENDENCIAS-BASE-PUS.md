# Pendencias — Base de PUs Executivos Cartesian

**Data:** 23/mar/2026
**Projetos processados:** 75 (57 com itens detalhados, 18 so macrogrupos)
**Itens consolidados:** 1.504 (544 com 3+ projetos, 199 com 5+)
**Pasta dos executivos:** `~/orcamentos/executivos/entregues/` (136 xlsx, 104 pastas, 65 clientes)

---

## 1. Projetos sem AC (13)

Sem area construida, os R$/m2 nao sao calculados. Preencher manualmente em `projetos-metadados.json`.

| Slug | Itens | Fonte |
|------|-------|-------|
| ajr-spot-one | 875 | Spot One (AJR) |
| cambert-engenharia-portal-da-brava | 1.036 | Portal da Brava (Cambert) |
| cgl-arbol-646 | 443 | Arbol 646 (CGL) |
| chiquetti-e-dalvesco-bela-vida | 197 | Bela Vida (Chiquetti/Dalvesco) |
| chiquetti-e-dalvesco-nautilus | 337 | Nautilus (Chiquetti/Dalvesco) |
| chiquetti-e-dalvesco-santorini | 581 | Santorini (Chiquetti/Dalvesco) |
| ck-duo-praia-brava | 1.990 | Duo Praia Brava (CK) |
| ck-rooftop | 1.022 | Rooftop (CK) |
| ck-smart-navegantes | 1.158 | Smart Navegantes (CK) |
| ck-smart-sao-joao | 793 | Smart Sao Joao (CK) |
| ck-unique | 803 | Unique (CK) |
| santa-maria-z | 950 | Z (Santa Maria) |
| terrassa-dom-bosco | 555 | Dom Bosco (Terrassa) |

**Como corrigir:**
```json
// Editar ~/orcamentos/base/projetos-metadados.json
"ck-duo-praia-brava": {
  "ac": 12345.67,   // <-- preencher
  ...
}
```
Depois rodar `python ~/orcamentos/scripts/consolidar_base_pus.py` para recalcular.

---

## 2. Metadados Faltantes (todos os 37 projetos)

Nenhum projeto tem cidade, estado, padrao ou tipologia preenchidos. Esses campos sao editaveis em `projetos-metadados.json` e servem para filtrar projetos similares.

| Campo | Para que serve | Valores possiveis |
|-------|----------------|-------------------|
| `cidade` | Filtro regional | Itajai, Florianopolis, Balneario Camboriu, etc. |
| `estado` | Filtro por estado | SC, PR, RS, etc. |
| `padrao` | Filtro por padrao | baixo, medio, medio-alto, alto, luxo |
| `tipologia` | Tipo de empreendimento | residencial_vertical, residencial_horizontal, comercial, misto |
| `nome_completo` | Nome legivel do projeto | "Santorini Residence" |
| `cliente` | Construtora/incorporadora | "Chiquetti e Dalvesco" |

**Tabela para preenchimento:**

| Slug | AC | UR | Cidade | Padrao | Cliente |
|------|----|----|--------|--------|---------|
| adore-cacupe | 6.495 | — | ? | ? | Adore |
| ajr-spot-one | **?** | — | ? | ? | AJR |
| all-acacias-jk | 1.943 | — | ? | ? | ALL |
| all-lago-di-garda | 7.056 | — | ? | ? | ALL |
| amalfi-tramonti | 15.603 | 90 | ? | ? | Amalfi |
| arv-ingleses-spot | 2.618 | 49 | ? | ? | ARV |
| be-brave-meraki | 22.461 | 104 | ? | ? | Be Brave |
| beco-castelo-chateau-de-versailes | 32.507 | 142 | ? | ? | Beco Castelo |
| blue-heaven-aquos | 9.522 | 12 | ? | ? | Blue Heaven |
| blue-heaven-monolyt | 14.693 | 24 | ? | ? | Blue Heaven |
| brasin-redentor | 16.728 | 40 | ? | ? | Brasin |
| by-seasons-by-seasons | 6.349 | 67 | ? | ? | By Seasons |
| caledonia-mowe-caledonia-mowe | 330 | 1 | ? | ? | Caledonia MOWE |
| cambert-engenharia-portal-da-brava | **?** | — | ? | ? | Cambert |
| cgl-arbol-646 | **?** | — | ? | ? | CGL |
| chiquetti-e-dalvesco-bela-vida | **?** | — | ? | ? | Chiquetti/Dalvesco |
| chiquetti-e-dalvesco-cielo | 7.013 | 20 | ? | ? | Chiquetti/Dalvesco |
| chiquetti-e-dalvesco-esmeralda | 5.580 | 37 | ? | ? | Chiquetti/Dalvesco |
| chiquetti-e-dalvesco-nautilus | **?** | — | ? | ? | Chiquetti/Dalvesco |
| chiquetti-e-dalvesco-santorini | **?** | — | ? | ? | Chiquetti/Dalvesco |
| ck-duo-praia-brava | **?** | — | ? | ? | CK |
| ck-rooftop | **?** | — | ? | ? | CK |
| ck-smart-navegantes | **?** | — | ? | ? | CK |
| ck-smart-sao-joao | **?** | — | ? | ? | CK |
| ck-unique | **?** | — | ? | ? | CK |
| cln-porto-ruby | 12.973 | 44 | ? | ? | CLN |
| santa-maria-unimed | 52.516 | — | ? | ? | Santa Maria |
| santa-maria-z | **?** | — | ? | ? | Santa Maria |
| santo-andre-belle-ville | 7.879 | 38 | ? | ? | Santo Andre |
| somauma-virginia | 10.108 | 117 | ? | ? | Somauma |
| terrassa-amaro | 10.479 | — | ? | ? | Terrassa |
| terrassa-dom-bosco | **?** | — | ? | ? | Terrassa |
| viva4-barra4 | 13.223 | 99 | ? | ? | Viva4 |
| viva4-pio4 | 13.541 | 176 | ? | ? | Viva4 |
| wf-aquarius | 16.789 | 84 | ? | ? | WF |
| xpcon-marena | 4.175 | 20 | ? | ? | XPCon |
| xpcon-porto-cerro | 13.189 | 86 | ? | ? | XPCon |

---

## 3. Outliers a Revisar (58 itens com CV > 10)

Itens com coeficiente de variacao > 10 provavelmente tem PU errado (coluna desalinhada na planilha de origem). Os mais criticos:

- **Loucas e Metais:** Vaso sanitario (CV 49.062), cuba cozinha (CV 9.776), bancada granito (CV 7.756) — PUs de R$ 1-9 sao claramente quantidades, nao precos
- **PCI:** Rede hidrantes (CV 4.294) — mesmo problema
- **Gerenciamento:** Levantamento topografico (CV 3.679)

**Recomendacao:** Para consultas confiaveis, filtrar `CV < 2.0`. Dos 1.077 itens:
- CV < 2: **~800 itens confiaveis**
- CV 2-10: ~220 itens (revisar caso a caso)
- CV > 10: 58 itens (provavelmente errados)

---

## 4. Resumo de Cobertura por Disciplina

| Disciplina | Itens | Notas |
|-----------|-------|-------|
| Insumos ABC | 216 | Itens de ABC flat (all-acacias, all-lago-di-garda) |
| Inst. Hidraulicas | 146 | Boa cobertura |
| Inst. Eletricas | 135 | Boa cobertura |
| Gerenciamento | 96 | Boa cobertura |
| Esquadrias | 62 | Boa cobertura |
| Loucas/Metais | 48 | Muitos outliers — revisar |
| Pintura | 47 | OK |
| Serv. Complementares | 44 | OK |
| Revestimentos | 41 | OK |
| Alvenaria | 36 | OK |
| Supraestrutura | 32 | OK |
| Infraestrutura | 27 | OK |
| Impermeabilizacao | 27 | OK |
| Fachada | 21 | OK |
| PCI | 18 | OK |
| Climatizacao | 18 | OK |
| Pisos | 15 | OK |
| Sist. Especiais | 11 | OK |
| Mov. Terra | 8 | Baixo |
| Canteiro | 8 | Itens fixos (cadeira, mesa, etc.) |
| Fundacoes | 6 | Baixo |
| Contencao | 5 | Baixo |
| Forro | 4 | Baixo |
| Gas | 3 | Insuficiente |
| SPDA | 2 | Insuficiente |
| Estacas | 1 | Insuficiente |

---

## 5. Inventario Completo — Todos os Orcamentos Processados (55)

Todos os 55 orcamentos processados, com detalhamento de disciplinas extraidas.

**Legenda:** AC em m2 | UR = unidades residenciais | R$/m2 = custo total / AC | Rev = revisao

### adore-cacupe
- **Arquivo:** CTN-ADR-CCP - Gerenciamento Executivo_R00
- **AC:** 6,495 m2 | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Disciplinas (12):** Movimentacao de Terra(5), Infraestrutura(5), Supraestrutura(13), Sistemas Especiais(14), Servicos Complementares(6), Alvenaria(18), Fachada(2), Impermeabilizacao(8), Forro(4), Pintura(4), Esquadrias(11), Cobertura(2)
- **Total itens:** 92

### adore-level-up
- **Arquivo:** CTN-ADR-LVU- Apresentacao_R00
- **AC:** 11,103 m2 | **UR:** — | **R$/m2:** 3,629 | **Rev:** R00
- **Macrogrupos:** 16 | **Total:** R$ 40,287,856
- **Itens detalhados:** NENHUM (so macrogrupos)

### ajr-spot-one
- **Arquivo:** CTN-AJR-TSO - ORCAMENTO EXECUTIVO
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (14):** Movimentacao de Terra(6), Infraestrutura(20), Supraestrutura(13), Alvenaria(166), Instalacoes Eletricas(50), Instalacoes Hidraulicas(37), PCI(6), Gerenciamento(16), Impermeabilizacao(151), Pintura(228), Esquadrias(161), Cobertura(1), Fachada(15), Servicos Complementares(5)
- **Total itens:** 875

### all-acacias-jk
- **Arquivo:** 01_CTN_ALL_Acacias JK - Planilha_Orcamento_R04
- **AC:** 1,943 m2 | **UR:** — | **R$/m2:** — | **Rev:** R04
- **Disciplinas (1):** Insumos ABC(334)
- **Total itens:** 334

### all-lago-di-garda
- **Arquivo:** 01_CTN_ALL_LDG-Orcamento_R01
- **AC:** 7,056 m2 | **UR:** — | **R$/m2:** 7,160 | **Rev:** R01
- **Disciplinas (1):** Insumos ABC(392)
- **Total itens:** 392

### amalfi-maiori
- **Arquivo:** CTN-ALF-MRI - Apresentacao Orcamento - R02
- **AC:** 397 m2 | **UR:** — | **R$/m2:** 63,490 | **Rev:** R02
- **Macrogrupos:** 17 | **Total:** R$ 25,185,733
- **Itens detalhados:** NENHUM (so macrogrupos)

### amalfi-marine
- **Arquivo:** CTN-ALF-MRN - Apresentacao Orcamento - R01
- **AC:** 522 m2 | **UR:** — | **R$/m2:** 27,041 | **Rev:** R01
- **Macrogrupos:** 17 | **Total:** R$ 14,107,283
- **Itens detalhados:** NENHUM (so macrogrupos)

### amalfi-ravello
- **Arquivo:** CTN-ALF-RVL - Apresentacao Orcamento RVL - R01
- **AC:** 353 m2 | **UR:** — | **R$/m2:** 111,266 | **Rev:** R01
- **Macrogrupos:** 16 | **Total:** R$ 39,313,735
- **Itens detalhados:** NENHUM (so macrogrupos)

### amalfi-tramonti
- **Arquivo:** CTN-ALF-TRM - Orcamento Executivo_R04xlsb
- **AC:** 15,603 m2 | **UR:** 90 | **R$/m2:** — | **Rev:** R04
- **Disciplinas (9):** Canteiro(8), Climatizacao(103), Gas(80), Instalacoes Eletricas(931), Servicos Complementares(60), Loucas e Metais(1), SPDA(108), Fundacoes(5), Contencao(1)
- **Total itens:** 1,297

### arv-ingleses-spot
- **Arquivo:** CTN_ARV-SPT - Orcamento_R04
- **AC:** 2,618 m2 | **UR:** 49 | **R$/m2:** — | **Rev:** R04
- **Disciplinas (9):** Canteiro(9), Estacas(1), Gas(3), Fundacoes(1), Supraestrutura(17), Esquadrias(24), Instalacoes Eletricas(5), Climatizacao(2), Loucas e Metais(31)
- **Total itens:** 93

### as-ramos-paessaggio
- **Arquivo:** CTN-ASR-PAE - Apresentacao Orcamento - R04
- **AC:** 264 m2 | **UR:** — | **R$/m2:** 129,838 | **Rev:** R04
- **Macrogrupos:** 17 | **Total:** R$ 34,284,020
- **Itens detalhados:** NENHUM (so macrogrupos)

### be-brave-meraki
- **Arquivo:** CTN_BBV_MKR - Orcamento Executivo -R00
- **AC:** 22,461 m2 | **UR:** 104 | **R$/m2:** — | **Rev:** R00
- **Disciplinas (4):** Canteiro(8), Infraestrutura(3), Supraestrutura(42), Loucas e Metais(157)
- **Total itens:** 210

### beco-castelo-chateau-de-versailes
- **Arquivo:** CTN_BCT-CTM - Orcamento_R01
- **AC:** 32,507 m2 | **UR:** 142 | **R$/m2:** — | **Rev:** R01
- **Disciplinas (7):** Estacas(1), Gas(59), Fundacoes(3), Telecom(54), Instalacoes Eletricas(377), Loucas e Metais(22), Esquadrias(109)
- **Total itens:** 625

### blue-heaven-aquos
- **Arquivo:** CTN_BHE-AQO - Orcamento-R03
- **AC:** 9,522 m2 | **UR:** 12 | **R$/m2:** — | **Rev:** R03
- **Disciplinas (2):** Canteiro(8), Gerenciamento(107)
- **Total itens:** 115

### blue-heaven-monolyt
- **Arquivo:** CTN_BHE-MON - Orcamento
- **AC:** 14,693 m2 | **UR:** 24 | **R$/m2:** — | **Rev:** —
- **Disciplinas (1):** Canteiro(8)
- **Total itens:** 8

### brasin-mario-lago
- **Arquivo:** CTN-BRS-RML-Apresentacao Orcamento - R01
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R01
- **Macrogrupos:** 17 | **Total:** R$ 23,491,182
- **Itens detalhados:** NENHUM (so macrogrupos)

### brasin-redentor
- **Arquivo:** CTN_BRS_RDT - Orcamento Executivo R01 - Entregavel.xlsb
- **AC:** 16,728 m2 | **UR:** 40 | **R$/m2:** — | **Rev:** R01
- **Disciplinas (7):** Loucas e Metais(15), Instalacoes Eletricas(110), Instalacoes Hidraulicas(200), Infraestrutura(8), Fundacoes(3), Supraestrutura(51), Escoramento(43)
- **Total itens:** 430

### brava-construtora-mar-a-vista
- **Arquivo:** CTN-BRV-MAV- Apresentacao Orcamento - R01
- **AC:** 563 m2 | **UR:** — | **R$/m2:** 18,550 | **Rev:** R01
- **Macrogrupos:** 16 | **Total:** R$ 10,446,495
- **Itens detalhados:** NENHUM (so macrogrupos)

### by-seasons-by-seasons
- **Arquivo:** CTN-BSN-FSN - Orcamento_R00
- **AC:** 6,349 m2 | **UR:** 67 | **R$/m2:** — | **Rev:** R00
- **Disciplinas (5):** Canteiro(9), Gas(49), Fundacoes(4), Infraestrutura(11), Loucas e Metais(96)
- **Total itens:** 169

### caledonia-mowe-caledonia-mowe
- **Arquivo:** CTN_MFZ_MOWE - Orcamento_R00
- **AC:** 330 m2 | **UR:** 1 | **R$/m2:** 4,865 | **Rev:** R00
- **Disciplinas (4):** Fundacoes(15), Infraestrutura(3), Supraestrutura(9), Loucas e Metais(48)
- **Total itens:** 75

### cambert-engenharia-portal-da-brava
- **Arquivo:** MTH - CAM_PBR - Orcamento_Executivo_R01
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R01
- **Disciplinas (14):** Movimentacao de Terra(4), Infraestrutura(20), Supraestrutura(173), Alvenaria(121), Instalacoes Eletricas(21), Instalacoes Hidraulicas(50), PCI(6), Gerenciamento(28), Impermeabilizacao(75), Pintura(248), Esquadrias(118), Fachada(157), Cobertura(8), Servicos Complementares(7)
- **Total itens:** 1,036

### carraro-vertice
- **Arquivo:** CTN-CRR-VRT - Apresentacao Orcamento - R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Disciplinas (1):** Gerenciamento(1)
- **Total itens:** 1

### cgl-arbol-646
- **Arquivo:** CTN_CGL-ARB - Orcamento_Executivo - R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Disciplinas (15):** Movimentacao de Terra(16), Infraestrutura(60), Supraestrutura(64), Alvenaria(20), Instalacoes Eletricas(28), Instalacoes Hidraulicas(20), PCI(8), Climatizacao(8), Impermeabilizacao(40), Pintura(60), Esquadrias(36), Cobertura(20), Fachada(48), Gerenciamento(8), Servicos Complementares(7)
- **Total itens:** 443

### chiquetti-e-dalvesco-bela-vida
- **Arquivo:** Orcamento Bela Vida - Cartesian - R02
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R02
- **Disciplinas (18):** Gerenciamento(1), Movimentacao de Terra(7), Infraestrutura(34), Supraestrutura(12), Alvenaria(10), Impermeabilizacao(9), Instalacoes Hidraulicas(5), Instalacoes Eletricas(8), PCI(1), Gas(1), Sistemas Especiais(5), Climatizacao(4), Revestimentos(52), Pintura(5), Esquadrias(14), Loucas e Metais(21), Cobertura(2), Servicos Complementares(6)
- **Total itens:** 197

### chiquetti-e-dalvesco-cielo
- **Arquivo:** CTN_CDV-CST - Orcamento - Entregavel
- **AC:** 7,013 m2 | **UR:** 20 | **R$/m2:** — | **Rev:** —
- **Disciplinas (8):** Canteiro(8), Fundacoes(4), Infraestrutura(4), Supraestrutura(24), Instalacoes Hidraulicas(180), Instalacoes Eletricas(213), Servicos Complementares(248), Loucas e Metais(1)
- **Total itens:** 682

### chiquetti-e-dalvesco-esmeralda
- **Arquivo:** CTN-CDV-ESM - Orcamento -R00
- **AC:** 5,580 m2 | **UR:** 37 | **R$/m2:** — | **Rev:** R00
- **Disciplinas (8):** Supraestrutura(25), Canteiro(8), Loucas e Metais(25), Impermeabilizacao(4), Infraestrutura(9), Instalacoes Hidraulicas(155), Exaustao(107), Instalacoes Eletricas(406)
- **Total itens:** 739

### chiquetti-e-dalvesco-nautilus
- **Arquivo:** MTH_CHI-NAU - Orcamento Executivo_R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Disciplinas (15):** Movimentacao de Terra(4), Contencao(2), Infraestrutura(17), Supraestrutura(22), Alvenaria(46), Instalacoes Eletricas(9), Instalacoes Hidraulicas(5), PCI(3), Gerenciamento(19), Impermeabilizacao(50), Loucas e Metais(8), Pintura(64), Esquadrias(79), Fachada(7), Servicos Complementares(2)
- **Total itens:** 337

### chiquetti-e-dalvesco-santorini
- **Arquivo:** CTN-CHI-SAN - Orcamento_Executivo_R02
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R02
- **Disciplinas (16):** Gerenciamento(79), Movimentacao de Terra(5), Contencao(22), Infraestrutura(14), Supraestrutura(22), Alvenaria(47), Instalacoes Eletricas(6), Instalacoes Hidraulicas(4), PCI(3), Sistemas Especiais(21), Impermeabilizacao(37), Revestimentos(156), Loucas e Metais(8), Pintura(58), Esquadrias(97), Servicos Complementares(2)
- **Total itens:** 581

### ck-artefacto
- **Arquivo:** CTN-CK _ART- Orcamento apresentacao - R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Macrogrupos:** 15 | **Total:** R$ 81,985,617
- **Itens detalhados:** NENHUM (so macrogrupos)

### ck-duo-praia-brava
- **Arquivo:** MTH_CK-DUO_Orcamento completo 21.05.2021
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (17):** Gerenciamento(87), Infraestrutura(24), Supraestrutura(204), Alvenaria(286), Instalacoes Eletricas(134), Instalacoes Hidraulicas(128), PCI(13), Climatizacao(11), Sistemas Especiais(3), Impermeabilizacao(114), Revestimentos(281), Pisos(122), Forro(26), Pintura(344), Esquadrias(116), Fachada(89), Servicos Complementares(8)
- **Total itens:** 1,990

### ck-habitah
- **Arquivo:** CTN-CK _HBT- Orcamento apresentacao - R01
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R01
- **Disciplinas (1):** Gerenciamento(14)
- **Total itens:** 14

### ck-rooftop
- **Arquivo:** MTH_CK-RFT_Orcamento Completo 01.04.2021
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (13):** Gerenciamento(73), Infraestrutura(2), Alvenaria(183), Instalacoes Eletricas(109), Instalacoes Hidraulicas(61), PCI(54), Climatizacao(30), Impermeabilizacao(35), Revestimentos(93), Pintura(164), Esquadrias(162), Fachada(52), Servicos Complementares(4)
- **Total itens:** 1,022

### ck-smart-navegantes
- **Arquivo:** MTH_CK-NVT_Orcamento Completo 01.04.2021
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (13):** Infraestrutura(4), Alvenaria(146), Instalacoes Eletricas(83), Instalacoes Hidraulicas(48), PCI(64), Climatizacao(16), Impermeabilizacao(47), Revestimentos(139), Pintura(197), Esquadrias(195), Fachada(138), Gerenciamento(75), Servicos Complementares(6)
- **Total itens:** 1,158

### ck-smart-sao-joao
- **Arquivo:** MTH_CK-SJ_Orcamento Completo 01.04.2021
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (14):** Gerenciamento(80), Infraestrutura(9), Alvenaria(118), Instalacoes Eletricas(61), Instalacoes Hidraulicas(29), PCI(35), Climatizacao(10), Impermeabilizacao(35), Revestimentos(82), Pintura(172), Esquadrias(97), Cobertura(2), Fachada(53), Servicos Complementares(10)
- **Total itens:** 793

### ck-unique
- **Arquivo:** MTH_CK-UNI_Orcamento completo 01.04.2021
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** —
- **Disciplinas (17):** Gerenciamento(77), Infraestrutura(22), Supraestrutura(73), Alvenaria(120), Instalacoes Eletricas(8), Instalacoes Hidraulicas(6), PCI(4), Climatizacao(1), Sistemas Especiais(1), Impermeabilizacao(38), Revestimentos(111), Pisos(49), Forro(12), Pintura(138), Esquadrias(95), Fachada(40), Servicos Complementares(8)
- **Total itens:** 803

### ck-urbe
- **Arquivo:** CTN-CK-URB- Apresentacao Orcamento - R02
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R02
- **Disciplinas (1):** Gerenciamento(1)
- **Total itens:** 1

### cln-porto-ruby
- **Arquivo:** CTN_CLN_PBY - Orcamento - R01
- **AC:** 12,973 m2 | **UR:** 44 | **R$/m2:** — | **Rev:** R01
- **Disciplinas (5):** Canteiro(8), Fundacoes(4), Infraestrutura(2), Supraestrutura(64), Loucas e Metais(18)
- **Total itens:** 96

### cn-brava-garden
- **Arquivo:** CTN-CN-BGR- Apresentacao_Orcamento - R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Macrogrupos:** 14 | **Total:** R$ 45,491,117
- **Itens detalhados:** NENHUM (so macrogrupos)

### cn-brava-ocean
- **Arquivo:** CTN-CN-BVO- Apresentacao_Orcamento - R00A
- **AC:** 505 m2 | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Dados:** nenhum item ou macrogrupo extraido

### cn-brava-valley
- **Arquivo:** CTN-CN-BBV- Apresentacao_Orcamento - R00
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Macrogrupos:** 14 | **Total:** R$ 57,502,889
- **Itens detalhados:** NENHUM (so macrogrupos)

### h-empreendimentos-atlantia
- **Arquivo:** CTN-H-ATL - Apresentacao Orcamento - R02
- **AC:** 289 m2 | **UR:** — | **R$/m2:** 139,959 | **Rev:** R02
- **Macrogrupos:** 17 | **Total:** R$ 40,420,185
- **Itens detalhados:** NENHUM (so macrogrupos)

### santa-maria-feat
- **Arquivo:** CTN-STM-FET - Apresentacao Orcamento_R00
- **AC:** 398 m2 | **UR:** — | **R$/m2:** 141,082 | **Rev:** R00
- **Macrogrupos:** 17 | **Total:** R$ 56,098,317
- **Itens detalhados:** NENHUM (so macrogrupos)

### santa-maria-unimed
- **Arquivo:** CTN-STM-UNI - Gerenciamento_executivo_R01
- **AC:** 52,516 m2 | **UR:** — | **R$/m2:** 1,604 | **Rev:** R01
- **Disciplinas (12):** Movimentacao de Terra(6), Infraestrutura(19), Supraestrutura(7), Alvenaria(6), Sistemas Especiais(13), Impermeabilizacao(8), Forro(3), Pintura(3), Esquadrias(8), Cobertura(2), Fachada(8), Servicos Complementares(6)
- **Total itens:** 89

### santa-maria-z
- **Arquivo:** CTN-STM-RSZ - Orcamento_Executivo_R07
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R07
- **Disciplinas (15):** Gerenciamento(21), Movimentacao de Terra(1), Infraestrutura(1), Supraestrutura(266), Alvenaria(145), Pintura(175), Esquadrias(99), Cobertura(9), Impermeabilizacao(42), Fachada(41), Instalacoes Eletricas(75), Instalacoes Hidraulicas(24), PCI(38), Loucas e Metais(12), Servicos Complementares(1)
- **Total itens:** 950

### santo-andre-belle-ville
- **Arquivo:** CTN-STA-BVL - Orcamento_R01 - Entregavel
- **AC:** 7,879 m2 | **UR:** 38 | **R$/m2:** — | **Rev:** R01
- **Disciplinas (11):** Canteiro(8), Fundacoes(4), Contencao(17), Supraestrutura(37), Instalacoes Hidraulicas(540), Instalacoes Eletricas(423), Gas(49), Climatizacao(26), Servicos Complementares(48), Esquadrias(84), Loucas e Metais(3)
- **Total itens:** 1,239

### santo-andre-lausanne
- **Arquivo:** CTN_STA_LAU - Apresentacao Orcamento - R00
- **AC:** 354 m2 | **UR:** — | **R$/m2:** — | **Rev:** R00
- **Dados:** nenhum item ou macrogrupo extraido

### somauma-virginia
- **Arquivo:** CTN-SMU-VGN -Orcamento comentado-R00
- **AC:** 10,108 m2 | **UR:** 117 | **R$/m2:** — | **Rev:** R00
- **Disciplinas (2):** Canteiro(8), Escoramento(14)
- **Total itens:** 22

### terrassa-amaro
- **Arquivo:** CTN-TRS-AMR -Orcamento-R01
- **AC:** 10,479 m2 | **UR:** — | **R$/m2:** 3,100 | **Rev:** R01
- **Disciplinas (14):** Contencao(27), Supraestrutura(142), Alvenaria(135), Instalacoes Eletricas(11), Instalacoes Hidraulicas(89), PCI(17), Climatizacao(11), Revestimentos(296), Forro(18), Pintura(150), Esquadrias(74), Servicos Complementares(3), Loucas e Metais(63), Infraestrutura(4)
- **Total itens:** 1,040

### terrassa-dom-bosco
- **Arquivo:** CTN-TRS-DBS - EAP_Comentada_R02
- **AC:** **FALTANDO** | **UR:** — | **R$/m2:** — | **Rev:** R02
- **Disciplinas (14):** Contencao(6), Supraestrutura(55), Alvenaria(80), Instalacoes Eletricas(44), Instalacoes Hidraulicas(43), PCI(41), Climatizacao(7), Revestimentos(147), Forro(13), Pintura(52), Esquadrias(34), Servicos Complementares(1), Loucas e Metais(11), Infraestrutura(21)
- **Total itens:** 555

### thozen-mirador-de-alicante
- **Arquivo:** CTN-THO-MAT - Apresentacao Orcamento - R03
- **AC:** 475 m2 | **UR:** — | **R$/m2:** 73,778 | **Rev:** R03
- **Macrogrupos:** 17 | **Total:** R$ 35,031,765
- **Itens detalhados:** NENHUM (so macrogrupos)

### viva4-barra4
- **Arquivo:** CTN_VV4-BR4 - Orcamento Final_R02.xls
- **AC:** 13,223 m2 | **UR:** 99 | **R$/m2:** — | **Rev:** R04
- **Disciplinas (5):** Canteiro(8), Loucas e Metais(255), Fundacoes(171), Infraestrutura(18), Instalacoes Eletricas(166)
- **Total itens:** 618

### viva4-pio4
- **Arquivo:** CTN_VV4-PIO4 - Orcamento_R00.xls - Entregavel
- **AC:** 13,541 m2 | **UR:** 176 | **R$/m2:** — | **Rev:** R00
- **Disciplinas (7):** Canteiro(8), Instalacoes Eletricas(187), Escoramento(49), Contencao(10), SPDA(36), Climatizacao(98), Loucas e Metais(1)
- **Total itens:** 389

### wf-aquarius
- **Arquivo:** CTN_WF_AQUARIUS - Orcamento-R02
- **AC:** 16,789 m2 | **UR:** 84 | **R$/m2:** — | **Rev:** R02
- **Disciplinas (3):** Canteiro(8), Infraestrutura(25), Supraestrutura(88)
- **Total itens:** 121

### xpcon-marena
- **Arquivo:** CTN_XPC_MRN - Orcamento Executivo_R02
- **AC:** 4,175 m2 | **UR:** 20 | **R$/m2:** — | **Rev:** R02
- **Disciplinas (8):** Canteiro(8), Fundacoes(51), Infraestrutura(4), Supraestrutura(31), Instalacoes Hidraulicas(825), SPDA(1), Climatizacao(94), Loucas e Metais(2)
- **Total itens:** 1,016

### xpcon-porto-cerro
- **Arquivo:** CTN_XPC_Porto Cerro - Orcamento_R01-ENTREGA
- **AC:** 13,189 m2 | **UR:** 86 | **R$/m2:** — | **Rev:** R01
- **Disciplinas (14):** Canteiro(8), Fundacoes(7), Infraestrutura(8), Supraestrutura(24), Alvenaria(10), Servicos Complementares(19), Esquadrias(49), Loucas e Metais(103), Gas(81), PCI(56), SPDA(11), Climatizacao(77), Instalacoes Hidraulicas(753), Instalacoes Eletricas(169)
- **Total itens:** 1,375

---

## 6. Proximos Passos

1. **Preencher metadados** — Leo edita `projetos-metadados.json` com cidade, padrao, AC dos 13 faltantes
2. **Reconsolidar** — `python ~/orcamentos/scripts/consolidar_base_pus.py`
3. **Processar novos executivos** — colocar xlsx em `~/orcamentos/executivos/entregues/` e rodar:
   ```bash
   python ~/orcamentos/scripts/processar_executivo.py --batch
   python ~/orcamentos/scripts/consolidar_base_pus.py
   ```
4. **Melhorar detector de colunas** — para reduzir outliers em Loucas/Metais (columns desalinhadas)
