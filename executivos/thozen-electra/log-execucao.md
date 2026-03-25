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

| #   | Disciplina      | Status                            | Revisao | Arquivo-chave                                         |
| --- | --------------- | --------------------------------- | ------- | ----------------------------------------------------- |
| 01  | Estrutura       | Briefing R00                      | R00     | [[estrutura-r00]]                                     |
| 02  | Arquitetura     | Briefing R00                      | R00     | [[arquitetura-r00]]                                   |
| 03  | Alvenaria       | Briefing R00-R01, DXF pendente    | R01     | [[alvenaria-r01]]                                     |
| 04  | Esquadria       | Briefing R00                      | R00     | [[esquadria-r00]]                                     |
| 05  | Hidraulico      | Planilha R00 (IFC+DWG, T.A/T.B)  | R00     | [[hidro-electra-r00.xlsx]]                            |
| 06  | Sanitario       | Briefing R00                      | R00     | [[sanitario-r00]]                                     |
| 07  | PCI Civil       | Briefing R00                      | R00     | [[pci-civil-r00]]                                     |
| 08  | PCI Eletrico    | Briefing R00                      | R00     | [[pci-eletrico-r00]]                                  |
| 09  | Eletrico        | Planilha R00 (IFC+DXF, T.A/T.B)  | R01     | [[eletrico-electra-r00.xlsx]]                         |
| 10  | Telefonico      | R01 — IFC + 18 DWGs processados   | R01     | [[telecomunicacoes-electra-r01.xlsx]]                  |
| 11  | SPDA            | Briefing R00                      | R00     | [[spda-r00]]                                          |
| 12  | Ventilacao      | Briefing R00-R02 (DWG bloqueado)  | R02     | [[ventilacao-r02]]                                    |
| 13  | Exaustao        | Briefing R00-R02 (DXF processado) | R02     | [[exaustao-r02]]                                      |
| 14  | Ar-Condicionado | Briefing R00-R01 (DWG bloqueado)  | R01     | [[ar-condicionado-r01]]                               |
| --  | Tecnico/Adm     | Analise EAP + preenchimento       | R00     | [[electra_analise_tecnico_adm]]                       |
| --  | EAP             | 4 UCs × pavimentos (v3 definitiva)| v3      | [[EAP_Electra_Pavimentos.xlsx]]                       |
| --  | Consolidado     | R00 -> R01 -> R02 -> R03          | R03     | [[CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx]] |

---

## 1. Estrutura (EAP e Organizacao do Orcamento)

### EAP — Estrutura Analitica do Projeto

**Decisao:** Reorganizar de 2 UCs para 4 UCs:
- UC1: **Despesas Indiretas** (ex-Gerenciamento Tecnico e Administrativo)
- UC2: **Embasamento** (infraestrutura + fundacoes + etapas "-EMBASSAMENTO")
- UC3: **Torre A** (etapas "-TORRE A")
- UC4: **Torre B** (etapas "-TORRE B")

**Fonte:** Planilha original [[CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx]] (684 linhas, 28 colunas)

**Evolucao:**
- v1: [[EAP-Electra-4UCs.xlsx]] — separacao em 4 abas simples
- v2: [[EAP-Electra-4UCs-v2.xlsx]] — formatacao preservada, codigos renumerados
- v3 (DEFINITIVA): [[EAP_Electra_Pavimentos.xlsx]] — cada CC aberta por pavimento (24/mar/2026)

**EAP v3 — Estrutura por pavimento:**
- *Despesas Indiretas:* 3 CCs, 29 itens (sem quebra por pavimento)
- *Embasamento:* 24 CCs, cada uma aberta por 8 pavimentos (Terreo, Terreo 02, G1-G5, 7° Lazer). Infraestrutura mantida sem quebra (obra geral)
- *Torre A:* 19 CCs × 4 pavimentos (Tipo x24, Telhado, Casa de Maquinas, Reservatorio)
- *Torre B:* 19 CCs × 4 pavimentos (mesma estrutura Torre A)
- Garagens: cada uma separada (G1, G2, G3, G4, G5)

**Importacao no Memorial Cartesiano:**
- 108 itens importados (N1-N3): 2 UCs, 27 Celulas, 79 Etapas
- CPUs (N4): vinculacao manual (match automatico falhou — nomenclaturas divergentes entre EAP e base de CPUs)
- Project ID Memorial: `cdff0592-fb3c-4c13-9516-efde6b56b336`

### Gestao de Projetos (aba PROJETOS)

**Decisao:** Preencher com todos os IFC/DWG recebidos, por disciplina
**Entrega:** [[Projetos-Electra-Preenchido.xlsx]]

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
- [[electra_analise_tecnico_adm]] — analise detalhada dos 117 servicos
- [[Tec_Adm_Electra_Preenchido.xlsx]] — planilha com recomendacoes por item
- [[Justificativas_Tec_Adm_Electra_Base_Cartesian.docx]] — justificativas

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

**Entrega:** [[estrutura-r00]] + [[estrutura-r00.json]]

---

## 4. Alvenaria

**Fonte:** 18 DWGs R01 (pre-executivo)
**Bloqueador:** DWG em formato binario (AutoCAD 2018/2019/2020) — nao processavel sem ODA File Converter
**Dados parciais na R00:** Terreo + 1o Subsolo preenchidos (Bloco 9cm, 14cm, 19cm)

**Pavimentos mapeados:** 01 Terreo, 02-06 G1-G5, 07 Lazer, 08-31 Tipo (x24), 32 Res/Cob

**Decisao:** Solicitar DXF ao projetista ou instalar ODA File Converter para conversao automatica.

**Scripts criados:** [[extrair_alvenaria_dxf.py]], [[processar_todos_alvenaria.sh]]
**Entrega:** [[alvenaria-r00]], [[alvenaria-r01]]

**Pendente:** Conversao DWG -> DXF e extracao automatizada

---

## 5. Esquadrias

**Fonte:** DWGs de arquitetura
**Dados extraidos:** Mapa preliminar de tipologias (portas madeira P1/P2/P3, aluminio, vidros temperados)
**Entrega:** [[esquadria-r00]] + [[esquadria-r00.json]]

**Pendente:** Quantitativos detalhados por pavimento, caderno de especificacoes

---

## 6. Instalacoes Hidrossanitarias

**Fonte:** IFC H00 completo rev.01 + 20 DWGs rev.01 (H01-H20) — Projetista R. Rubens Alves
**Entregas iniciais:** [[hidraulico-r00]], [[sanitario-r00]]

### IFC H00 — Quantitativos Gerais
- **Arquivo:** `348 - H00 [00] rev.01 - EL_R.Rubens Alves - COMPLETO.ifc`
- **Elementos totais:** 5.841 (2.715 tubulacoes + 3.116 conexoes + 10 terminais)
- **100% dos elementos com coordenada X** — permite split por torre
- **12 pavimentos modelados:** Terreo, G1-G5, Lazer, Tipo (x24), Casa de Maquinas, Reservatorio

**Tubulacoes totais (IFC):**
- PVC Soldavel: 193.367 m (66,3%) — DN63, DN81, DN101, DN127, DN152, DN190
- CPVC FlowGuard: 62.520 m (21,4%) — DN55, DN71, DN38 (agua quente)
- PPR PN25: 35.669 m (12,2%) — DN228 (recalque e pressurizacao)
- **Total:** 291.557 m (sem multiplicacao do tipo)

**Estimativa com tipo x24:** 3.066.013 m tubulacoes, 36.926 conexoes, 2.708 registros

**Equipamentos identificados:**
- 2 reservatorios polietileno 7.500L A'Melo (06° Pavto G5)
- 4 pressurizadores Schneider VFD BC-92 (2CV) — Casa de Maquinas
- Hidrometros multijato 3/4" (30 un Terreo + 8 un G4)

### DWG H01-H20 — Extracao de Conexoes por Torre (25/mar/2026)
- **20 DWGs** convertidos para DXF via ODA File Converter (batch)
- DWGs ja vinham separados por torre no filename: `[T.A]` / `[T.B]`
- **Componentes extraidos (blocos INSERT):** joelhos PVC/CPVC, adaptadores, luvas, registros de esfera, curvas, bucha reducao, uniao, valvulas, hidrometros, flanges

**Componentes DXF — Pavimento Tipo (por torre, por pavimento):**
- T.A: 578 componentes (197 joelhos PVC, 140 joelhos CPVC, 61 c/ bucha latao, 57 registros, 39 adaptadores, 36 curvas, 19 bucha red., 13 luva LR, 7 joelho 45° CPVC, 4 uniao, 4 hidrometro)
- T.B: 593 componentes (237 joelhos PVC, 133 joelhos CPVC, 57 registros, 56 c/ bucha latao, 41 adaptadores, 31 curvas, 16 bucha red., 5 luva LR, 5 joelho 90° CPVC, 4 joelho 45° CPVC, 4 uniao, 4 hidrometro)

**Ratios Torre (IFC):**
- Pavimento Tipo: T.A 51,6% / T.B 48,4%
- Terreo: 66% / 34%
- Lazer: 57% / 43%
- Casa de Maquinas: 50% / 50%

### Planilha R00 executiva — separada Emb / T.A / T.B (25/mar/2026)
- **Arquivo:** [[hidro-electra-r00.xlsx]]
- **Fonte dados:** IFC H00 (tubulacoes) + DWG H01-H20 (conexoes por torre) + briefing R00 (equipamentos) — SOMENTE Electra
- **Formato:** aba unica sequencial — Embasamento → Torre A → Torre B
- **Embasamento:** 96 itens (Terreo, G01-G05, Lazer, Casa Maquinas, Reservatorio) — quantidades cheias
- **Torre A:** 19 itens — Pav Tipo x24 (tubulacoes por ratio IFC 51,6% + conexoes DXF direto)
- **Torre B:** 19 itens — Pav Tipo x24 (tubulacoes por ratio IFC 48,4% + conexoes DXF direto)
- **Coluna K (custo unitario):** em branco — Leo precisa preencher/validar PUs

**Pendente:**
- Preencher custos unitarios da planilha hidro
- Sanitario (disciplina separada — pasta `06 SANITARIO`)
- Aguas pluviais (disciplina separada)
- Gas (disciplina separada)

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
- [[eletrico-r01-discipline-pack.xlsx]]
- [[eletrico-r01-memorial]] / `.docx`
- [[eletrico-r01-confianca]]
- [[eletrico-r01-por-pavimento.xlsx]]

**Planilha R00 executiva — separada T.A / T.B (25/mar/2026):**
- Arquivo: [[eletrico-electra-r00.xlsx]]
- Fonte dados: IFC rev.01 (9 arquivos) + DXF (dispositivos) — SOMENTE dados do Electra
- Separacao por torre: coordenada X do IFC (midpoint X=366.0)
- Formato: aba unica sequencial — Embasamento (compartilhado) → Torre A → Torre B
- Embasamento: 120 itens (Geral, Terreo, G01-G05, Lazer, Casa Maquinas) — quantidades cheias
- Torre A: 23 itens — Pav Tipo x24 (~52% pelo ratio IFC)
- Torre B: 23 itens — Pav Tipo x24 (~48% pelo ratio IFC)
- 12 subgrupos EAP: Barramento, Dispositivos, Eletrodutos, Entrada de Energia, Gerador, Interruptores, Luminarias, Mao de Obra, Quadros, Sensores, Subestacao, Tomadas
- Template visual: Elizabeth II (somente estilos, nenhum dado)

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
- [[telefonico-r00]]
- [[relatorio-extracao-telefonico-thozen]]
- [[thozen-electra-telefonico-consolidado.json]]

**Planilha R00 (24/mar/2026):**
- Arquivo: `telecomunicacoes-electra-r00.xlsx`
- Base: template Elizabeth II (Gessele) adaptado pro Electra
- Pavimentos: Terreo, G1-G5, Lazer, Tipo (x24), Casa de Maquinas
- Total estimado: R$ 424.322 (R$ 11,76/m²)
- Fonte quantitativos: IFC rev.01 | Fonte precos: Elizabeth II (Gessele)

**Processamento DWG (24/mar/2026 — noite):**
- 18 DWGs convertidos para DXF via ODA File Converter (CLI batch)
- Script: `quantitativos/telefonico/extrair_telefonico.py`
- Dados brutos: `quantitativos/telefonico/dados_brutos_telefonico.json` (142 KB)
- 18 extrações individuais: `quantitativos/telefonico/extracao_t02.md` a `extracao_t19.md`
- Consolidado: `quantitativos/telefonico/consolidado_telefonico.md`

**Planilha R01 (25/mar/2026):**
- Arquivo: `telecomunicacoes-electra-r01.xlsx`
- Revisao: `R01 - Jarvis/IFC+DWG 24/03/2026`
- 96 novos itens adicionados (distribuidos em 9 pavimentos)
- Formatacao e formulas preservadas da R00

**Dados NOVOS do DWG (nao existiam no IFC):**
- Eletrodutos ø1.1/4" e ø3" (IFC so tinha ø1" e ø3/4")
- 9 novas dimensoes de caixas de passagem (40x120, 80x120, 60x120, etc)
- 4.414 cotovelos de eletroduto
- 415 conectores box + 132 buchas terminal
- 324 trechos de condutores classificados (CFTV, UTP, CCI, Cordplast)
- 222 pontos de uso novos (interfones, cameras, controle de acesso, dados/telefone)

**Comparativo R00 vs R01:**
- Pontos ativos: 90 → 312 (+246%)
- Diametros de eletroduto: 2 → 4
- Tipos de caixa de passagem: 1 → 10
- Acessorios quantificados: 0 → 5.102 un
- Condutores identificados: 0 → 324 trechos

**Pendencias restantes (nem IFC nem DWG):**
- Metragens de cabos UTP/CFTV (estimativa ~6.858m)
- Especificacao de racks e patch panels
- DG (Distribuidor Geral)
- Dimensoes de calhas (100x50 ou 150x50mm)
- Categoria dos cabos (CAT6 vs CAT6A)
- Esses dados devem estar em memorial descritivo do projetista

---

## 9. SPDA (Para-raios)

**Fonte:** DWGs (sem IFC)
**Entrega:** [[spda-r00]] + [[spda-r00.json]]

**Pendente:** Extracao detalhada — depende de conversao DWG -> DXF

---

## 10. PCI (Prevencao e Combate a Incendio)

### PCI Civil
**Fonte:** IFC rev.01 (Torre A e B) + 11 pranchas DWG
**Quantitativos extraidos:** 78 abrigos, 73 extintores, 67m tubulacao (SUBESTIMADO)
**Entrega:** [[pci-civil-r00]] + resumo + anexo pavimentos

**Pendentes criticos:**
- Reservatorios e bombas de incendio (nao encontrados no IFC)
- Metragem real de tubulacao (espera-se >> 67m)
- Sistema de sprinklers (nao identificado)
- Memorial descritivo

### PCI Eletrico
**Fonte:** IFC + DWGs
**Entrega:** [[pci-eletrico-r00]]

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

**Entregas:** [[ventilacao-r00]] ate [[ventilacao-r02]] + checklists
**Pendente:** Solicitar DXF + memorial descritivo ao projetista Rubens Alves

---

## 12. Exaustao

**Fonte:** DXF processado com sucesso
**Entregas:** [[exaustao-r00]] ate [[exaustao-r02]]
**Dados:** Processamento DXF com dados reais extraidos

---

## 13. Ar-Condicionado e Climatizacao

**Fonte:** DWG R05 (RA_ARC_EXE_00_TODAS CAD_R05.dwg, 5.0 MB)
**Bloqueador:** DWG binario nao processavel (mesmo problema da Ventilacao)
**Estimativa parametrica:** R$ 80-150/m2 AC -> R$ 1,6M - 4,5M (+/- 30-40%)

**Entregas:** [[ar-condicionado-r00]], [[ar-condicionado-r01]]
**Pendente:** Conversao DWG -> DXF ou dados do projetista

---

## 14. Loucas e Metais

**Fonte:** IFC Arquitetura R07 (TIPO) + R08 (EMBASAMENTO + COBERTURA) — Escritorio Dallo
**Metodo de separacao T.A / T.B:** Coordenada X dos elementos no IFC (midpoint entre torres)

**Quantitativos extraidos por torre (por pavimento tipo):**

| Item | Torre A | Torre B | Total/pav |
|------|---------|---------|-----------|
| Bacia Sanitaria c/ Caixa Acoplada | 16 | 16 | 32 |
| Cuba Sobrepor Quadrada (Banheiro) | 11 | 2 | 13 |
| Cuba Semi-Encaixe (BWC) | 0 | 6 | 6 |
| Cuba Inox Cozinha (Apto) | 4 | 8 | 12 |
| Cuba Inox Cozinha (Lazer/Comum) | 4 | 3 | 7 |
| Tanque Simples | 4 | 4 | 8 |
| Chuveiro Quadrado | 12 | 12 | 24 |
| Aquecedor a Gas | 4 | 3 | 7 |
| Churrasqueira (Espeto) | 4 | 4 | 8 |
| Condensadora Split | 19 | 20 | 39 |

**Embasamento (Terreo + Lazer):**
- T.A: 12 bacias, 7 cubas sobrepor, 5 cubas PNE, 2 bacias PNE, 10 barras apoio PNE, 6 chuv
- T.B: 11 bacias, 6 cubas sobrepor, 4 cubas PNE, 1 bacia PNE, 8 barras apoio PNE, 3 chuv

**Observacao sobre IFC:** Louças NAO estavam modeladas nos IFCs de Sanitario (apenas ETE/lodo ativado). Foram encontradas no IFC de Arquitetura como familias Dallo e Deca. "Familia2" = Bacia Sanitaria c/ Caixa Acoplada.

**Metais derivados:** Fórmulas automaticas na planilha (torneiras, sifoes, valvulas, aneis de vedacao) — calculam a partir das quantidades de louças.

**Entregas:**
- v1: [[loucas-metais-electra-r00.xlsx]] — versao unificada (torres juntas x24)
- v2 (ATUAL): [[loucas-metais-electra-TA-TB-r00.xlsx]] — separada Torre A + Torre B, 3 pavimentos cada (Terreo x1, Lazer x1, Tipo x24)
- 28 itens em 4 secoes: Louças (12), Metais (13), Pontos Especiais (2), Ar-Condicionado (1)

**Pendente:** Validar com DWG/memorial descritivo. Separacao por coordenada pode ter margem de erro em itens de area comum.

---

## 15. Consolidacao Geral (R01 -> R02 -> R03)

**R01:** Primeira versao consolidada com todas as disciplinas disponiveis
**R02:** Formato Elizabeth II + memorial rastreavel + doc Word
**R03 (atual):** Ajustado (Mov.Terra, Loucas, Complementares)

| Item | Valor |
|------|-------|
| **Total** | **R$ 161,3M** |
| **R$/m2** | **R$ 4.469** |
| **CUB Ratio** | **1.48** |

**Entregas:**
- [[CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx]]
- [[CTN-TZN_ELT-Orcamento-Executivo-R03-MEMORIAL.docx]]

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
- [x] LOUCAS E METAIS ✅ (preenchido 24/mar — T.A + T.B separadas)
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
- [x] Loucas e Metais ✅ (preenchido 24/mar — separado T.A + T.B, fonte IFC Arq R07/R08)
- [ ] Equipamentos Especiais
- [ ] Piscina
- [x] Eletrico ✅ (R00 25/mar — IFC+DXF, separado Emb/T.A/T.B, aba unica)
- [x] Hidrossanitario ✅ (R00 25/mar — IFC H00 + 20 DWGs, separado Emb/T.A/T.B, conexoes DXF por torre)
- [ ] PPCI
- [ ] Sprinkler
- [x] Telecomunicacao ✅ (R01 25/mar — IFC + 18 DWGs processados, 96 itens novos)
- [ ] Gas
- [ ] Automacao
- [ ] Climatizacao
- [ ] Iluminacao
- [ ] Mobiliario

---

## Bloqueadores Tecnicos

1. **DWG binario** — Ventilacao, Ar-Condicionado, Alvenaria precisam de conversao DWG -> DXF (ODA File Converter instalado e funcional — usado com sucesso no Telefonico 24/mar e Hidraulico 25/mar)
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
| [[CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx]] | Planilha original do cliente |
| [[CTN-TZN_ELT-Orcamento-Executivo-R03-AJUSTADO.xlsx]] | Ultima versao consolidada (IA) |
| [[CTN-TZN_ELT-Orcamento-Executivo-R03-MEMORIAL.docx]] | Memorial rastreavel R03 |
| [[REVISAO-ELECTRA-R00]] | Analise detalhada da planilha R00 |
| `briefings/*.md` | 14 briefings por disciplina |
| `scripts/*.py` | Scripts de extracao e processamento |
| [[telecomunicacoes-electra-r01.xlsx]] | Planilha telecom R01 (IFC + DWG) |
| **Este arquivo** | [[log-execucao]] — memorial de execucao |

---

## Convencoes deste Memorial

Este documento e organizado **por disciplina**, nao por dia. Cada secao registra:
1. **Fontes** — de onde veio cada informacao (IFC, DWG, briefing, base PU)
2. **Decisoes** — escolhas feitas e justificativas
3. **Quantitativos** — dados extraidos e premissas
4. **Entregas** — arquivos gerados
5. **Pendentes** — dados faltantes, validacoes necessarias

**Regra de edicao:** Claude so adiciona no final de cada secao. Leo pode editar qualquer parte. Este MD sera a base do memorial Word final do projeto.

**Regra de entrega (25/mar/2026):** Toda atualizacao de planilha gera 3 entregas obrigatorias:
1. Planilha atualizada (.xlsx)
2. Este log atualizado (log-execucao.md)
3. **Documento Word (.docx) com o log de execucao convertido** — para a equipe acessar sem depender de Markdown

**Envio:** Sempre que gerar atualizacao, enviar os 2 arquivos (planilha + Word do log) no Slack para a equipe acompanhar.

---

*Criado em 2026-03-25 | Atualizado continuamente durante o projeto*
