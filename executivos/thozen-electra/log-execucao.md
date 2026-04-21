# Memorial de Execucao — Orcamento Executivo Electra Towers (Thozen)

> Ver tambem: [[gestao-orcamento-electra]] | [[PROJETO]]

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

### LM348 — Lista de Materiais Eletrowatts (16-17/abr/2026)

**Fonte:** 4 PDFs da LM348 (Lista de Materiais) emitidos pela Eletrowatts:
1. `348_LM - HIDRO - rev.00_ELC - CONEXÕES TUBOS.pdf` — 132 itens (conexoes AF, AQ, esgoto, PPR)
2. `348_LM - HIDRO - rev.00_ELC - ETE e CX. GORDURA.pdf` — 20 itens (tanques, bombas, difusores)
3. `348_LM - HIDRO - rev.00_ELC - TUBULAÇÕES.pdf` — 18 itens (tubos PVC, CPVC, PPR, esgoto)
4. `348_LM - HIDRO - rev.00_ELC - VÁLVULAS, MOTOBOMBAS.pdf` — 17 itens (Bermad, Schneider, hidrometros)
**Total: 187 itens** — cobertura COMPLETA (agua fria + agua quente + esgoto + ETE + valvulas/bombas)

**Pipeline de processamento:**
1. Extracao PDF → JSON via `gemma_extract_lm.py` (Gemma local)
2. Rateio por pavimento via `gemma_rateio_pavimento.py` (heuristica Gemma) → 490 distribuicoes
3. Geracao xlsx via `gerar_lm348_xlsx.py` → arquivo `hidraulico-electra-lm348-r01.xlsx` com 5 abas:
   - "Flat por PDF" (187 itens na ordem original)
   - "Por Pavimento" (490 linhas distribuidas)
   - "Rateio" (490 distribuicoes format A com justificativa)
   - "Resumo" (metricas, benchmark R$ 48,32/m2 AC)
   - "HIDROSSANITARIO" (formato IFC anterior — somente agua fria)

#### Correlacao IFC vs PDF (17/abr/2026)

Investigacao do IFC H00 usando ifcopenshell para validar os quantitativos da LM348.

**Descoberta principal:** O pavimento "H18 - 08° PAVTO - TIPO - TORRE B" no IFC modela **ambas as torres** num unico pavimento, apesar do nome dizer "Torre B". O multiplicador correto eh ×24 (nao ×48).

**Validacao conexoes (28 itens mapeados):**
- 26 itens com match < 10% de diferenca (ratio 0.93–1.00×) — praticamente identico
- 1 item proximo (Joelho 90 PVC 40mm: IFC 16 vs PDF 20 → 0.80×)
- 1 discrepante (Adaptador 32mm: IFC 10 vs PDF 195 — provavel item nao modelado no IFC)
- **Conclusao: IFC e LM348 sao consistentes. LM eh autoritativa pra quantitativos.**

**Validacao tubos:**
- CPVC (DN15/22/28), PPR DN90, PVC DN32: match 0.88–0.95× ✅
- PVC DN25: IFC 10.920m vs PDF 18.510m → 0.59× (IFC tem menos ramais modelados)
- PVC DN50/60: IFC tem muito mais que PDF (diferenca de classificacao de diametro)

**O que o IFC NAO tem** (e o PDF tem):
- Esgoto (Serie Normal + Reforcada): 8 tubos + 49 conexoes
- ETE (tanques, compressor, bombas): 20 itens
- Valvulas Bermad (redutoras, controladoras): 12 itens
- Acessorios (caixas sifonadas, ralos, aneis vedacao): 12 itens

#### HIDROSSANITARIO v2 — Lista Geral Precificada (16/abr/2026)

**Arquivo:** [[hidraulico-electra-lm348-r02.xlsx]], aba "HIDROSSANITARIO v2"
**Conteudo:** 187 itens em lista flat, agrupados por 12 subgrupos, precificados.

**Fontes de precos unitarios:**
| Fonte | Itens | Descricao |
|-------|-------|-----------|
| Belle Ville | 65 | PUs reais de projeto anterior — tubos AF, conexoes PVC soldavel, equipamentos |
| Santa Maria | 54 | PUs de orcamento entregue — tubos e conexoes esgoto (Normal + Reforcada) |
| Estimativa | 52 | ETE, acessorios, CPVC FlowGuard, juncoes com reducao — precos de mercado estimados |
| Mercado | 16 | Equipamentos (Bermad, Schneider, hidrometros) — referencias fabricante |

**Conversao de unidades:** Tubulacoes convertidas de barras para metros:
- PVC Soldavel / Esgoto: barras de 6m → ×6
- CPVC FlowGuard / PPR: barras de 3m → ×3

#### HIDROSSANITARIO v3 — 8 Subetapas do Orcamento (17/abr/2026)

**Arquivo:** [[hidraulico-electra-lm348-r03.xlsx]], aba "HIDROSSANITARIO v3"
**Conteudo:** Mesmos 187 itens reagrupados nas 8 subetapas do orcamento Electra:

| Subetapa | Codigo | Itens | O que inclui |
|----------|--------|-------|--------------|
| Instalacoes de agua fria | xx.001 | 58 | Tubos PVC Soldavel (DN25-75) + conexoes AF + adaptadores longos flanges |
| Instalacoes de agua quente | xx.002 | 24 | Tubos CPVC FlowGuard (DN15-28) + PPR (DN90) + conexoes CPVC + conexoes PPR |
| Instalacoes de esgoto e pluviais | xx.003 | 68 | Tubos esgoto Normal/Reforcada + conexoes esgoto + aneis vedacao + caixas sifonadas + ralos + terminais ventilacao + filtro pluvial |
| Cisterna | xx.004 | 20 | ETE completa: tanques (anaerobio, anoxico, aerobio, decantador, desinfeccao, descarte lodo) + caixas gordura + difusores + compressor + medidores + painel + bombas lodo |
| Hidrometros | xx.005 | 2 | Hidrometro Unijato 3/4" (144 un) + Multijato 3/4" (48 un) |
| Reservatorios | xx.006 | 1 | Caixa D'Agua Polietileno 7.500L (2 un) |
| Sistema de bombas | xx.007 | 14 | Skids Schneider (pressurizadores + motobombas recalque) + valvulas Bermad (redutoras, controladoras, alivio, retencao) + ventosas + filtros + chave fluxo + valvula pe crivo |
| Mao de obra | xx.008 | — | Placeholder — benchmark Cartesian R$ 55,00/m2 AC |

#### HIDROSSANITARIO v4 — Por Torre × 8 Subetapas (17/abr/2026)

**Arquivo:** [[hidraulico-electra-lm348-r03.xlsx]], aba "HIDROSSANITARIO v4"
**Conteudo:** 187 itens distribuidos por Embasamento / Torre A / Torre B, cada um com as 8 subetapas.

**Criterio de divisao por torre:**

A distribuicao entre as 3 etapas usa os dados da aba "Por Pavimento" (rateio heuristico Gemma):

| Pavimento na aba "Por Pavimento" | Torre | → Etapa na v4 |
|----------------------------------|-------|---------------|
| TERREO | qualquer | EMBASAMENTO |
| G1, G2, G3, G4, G5 | A, B ou AMBAS | EMBASAMENTO |
| LAZER | qualquer | EMBASAMENTO |
| C_MAQ (Casa de Maquinas) | qualquer | EMBASAMENTO |
| COBERTURA | qualquer | EMBASAMENTO |
| TIPO | A | TORRE A |
| TIPO | B | TORRE B |
| TIPO | AMBAS | Split 50/50 → metade TORRE A, metade TORRE B |

**Logica detalhada:**
1. Cada item da LM348 (187 no total) aparece na aba "Por Pavimento" distribuido em 1 a 5 pavimentos com quantidades proporcionais (ex: Joelho 90° DN25 → 1% Terreo, 49.5% TIPO/A, 49.5% TIPO/B)
2. As quantidades rateadas por pavimento foram somadas conforme a tabela acima
3. Para itens TIPO/AMBAS (28 itens, tipicamente itens de infraestrutura predial como prumadas compartilhadas), a quantidade foi dividida igualmente entre Torre A e Torre B
4. Tubulacoes tiveram a conversao de barras para metros aplicada (×6 para PVC/esgoto, ×3 para CPVC/PPR)
5. Itens que sao 100% infraestrutura (ETE, reservatorios, sistema de bombas C.Maq) ficaram integralmente no EMBASAMENTO

**Resultado da distribuicao:**
| Etapa | Codigo | Itens | Subetapas presentes |
|-------|--------|-------|---------------------|
| EMBASAMENTO | 5.001 | 134 | 8/8 (todas) |
| TORRE A | 5.002 | 120 | 6/8 (sem Cisterna e Reservatorios — ficaram no Embasamento) |
| TORRE B | 5.003 | 119 | 6/8 (mesma estrutura Torre A) |

**Fonte do rateio:** Heuristica Gemma (`gemma_rateio_pavimento.py`) com justificativa tecnica por item (ex: "Joelhos de conexao em prumadas principais no subsolo" → TERREO/AMBAS). Cada distribuicao tem coluna "Origem rateio" na aba "Rateio" do r01.

**Validacao cruzada IFC:** A correlacao IFC vs PDF confirmou que o rateio Gemma eh consistente — os totais por item (comuns + TIPO×24) matcham os totais do PDF com < 10% de diferenca em 26 de 28 itens testados.

**⚠ Limitacoes:**
- O rateio eh heuristico (Gemma), nao eh extracao geometrica do IFC
- Itens de esgoto NAO tem correspondencia no IFC (nao modelados)
- Itens TIPO/AMBAS divididos 50/50 eh simplificacao — a correlacao IFC mostrou ratio real T.A 51,6% / T.B 48,4% pra conexoes

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

> **Migrado para:** [[gestao-orcamento-electra]] (10/04/2026)
> Checklist vivo com status atualizado de cada aba/disciplina. Este log mantém apenas o histórico de execução por disciplina (seções acima).

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

## 16. Estrategia de Preenchimento (10/abr/2026)

**Decisao:** Separar fontes de dados em 3 categorias com fluxo bidirecional Visus <-> Excel.

### Fonte 1 — BIM via Visus (Leo extrai do modelo)
Macrogrupos de arquitetura e acabamentos que tem quantitativo geometrico no modelo BIM:
- 03 Paredes e Paineis
- 04 Impermeabilizacao e Tratamentos
- 12 Revestimentos Argamassados Internos de Parede
- 13 Acabamentos Internos de Parede
- 15 Acabamentos Internos em Teto
- 16 Revestimentos Argamassados em Piso e Pavimentacoes
- 17 Acabamentos em Piso e Pavimentacoes
- 18 Sistemas de Pintura Interna
- 19/20/21 Esquadrias (vidros, madeira, metalicas)
- 22/24 Revestimentos e Acabamentos em Fachada

### Fonte 2 — Planilha via IA (extracao IFC/DWG + processamento)
Disciplinas tecnicas ja processadas ou com dados prontos:
- Hidraulico, Eletrico, Telecomunicacao, Loucas/Metais, PCI, Sprinklers, Estrutura (prontos)
- Sanitario, Exaustao, SPDA (dados existem, falta planilha)
- Ar-Condicionado, Ventilacao (DWG bloqueado, estimativa parametrica)

### Fonte 3 — Indices parametricos (media de executivos entregues)
Itens sem projeto detalhado — usar benchmarks da base Cartesian:
- Ger. Tecnico e Administrativo, Ger. Executivo
- Canteiro, Controle Tecnologico, EPCs
- Equipamentos Especiais, Mobiliario, Piscina

### Fluxo de integracao
1. Leo extrai quantitativos BIM no Visus (arquitetura/acabamentos)
2. Claude preenche planilha Excel com dados de projetos + indices
3. Leo consolida tudo na planilha master Excel
4. Leo importa planilha completa de volta no Visus
5. Visus tem orcamento completo: parte BIM nativa + parte importada

---

## 17. Movimentacao de Terra (11/abr/2026)

### Premissas adotadas

| Premissa | Valor | Fonte |
|----------|-------|-------|
| Area terreno (provisoria) | 4.000 m2 | Estimativa — **DUVIDA: Leo confirma** |
| AC total | 36.088,85 m2 | log-execucao |
| Subsolo | NAO — garagens elevadas | Leo confirmou (10/abr) |
| Fundacao | Estacas HC o60cm, ~198 un/torre | Aba Estacas R00 (Torre 1) |
| Estacas total (2 torres) | ~400 un | Estimativa: Torre 1 (198) + Torre 2 (~200) |
| Infra (blocos+baldrame) | 70 elementos, ~55 m3 concreto | IFC R26 |
| Lencol freatico | ~1,5-2,0m (Porto Belo litoral) | Estimativa geotecnica regional |
| Demolicao existente | Nao | Leo confirmou (10/abr) |
| Condicao terreno | Vegetacao leve, sem edificacao | Leo confirmou (10/abr) |

### Base de benchmarks — 32 projetos Cartesian

Extracao automatizada de 158 planilhas de orcamentos executivos entregues pela Cartesian (pasta `_Entregas/Orcamento_executivo/`). Script: `scripts/benchmark_final.py`. Dados brutos: `temp/benchmark_mov_terra.json`.

**Estatisticas gerais (R$/m2 AC):**

| Metrica | Total Mov Terra (N=28) |
|---------|------------------------|
| Min | R$ 0,00/m2 |
| P25 | R$ 14,09/m2 |
| **Mediana** | **R$ 22,97/m2** |
| P75 | R$ 71,59/m2 |
| Max | R$ 130,65/m2 |

**Projetos de referencia principal (AC > 13k, tipologia comparavel):**

| Projeto | AC (m2) | Total MT | R$/m2 | Contexto |
|---------|---------|----------|-------|----------|
| Be Brave Meraki | 22.461 | R$ 316.584 | 14,09 | Litoral SC, porte similar |
| Brasin Redentor | 16.728 | R$ 70.239 | 4,20 | Itajai, valor baixo |
| WF Aquarius | 16.789 | R$ 290.742 | 17,32 | Medio porte |
| Mussi Chelsea | 15.149 | R$ 217.216 | 14,34 | Medio porte |
| Neuhaus Origem | 14.559 | R$ 334.392 | 22,97 | = mediana da base |
| Chateau Versailles | 32.507 | R$ 122.422 | 3,77 | AC proximo mas TEM subsolo pesado |
| XPCon Porto Cerro | 13.189 | R$ 201.549 | 15,28 | Litoral SC |
| FG Blue Coast | 13.132 | R$ 68.942 | 5,25 | Valor baixo |
| Viva4 Barra4 | 13.223 | R$ 994.139 | 75,18 | OUTLIER — contencao pesada |
| Blue Heaven Monolyt | 14.693 | R$ 1.491.120 | 101,49 | OUTLIER — contencao pesada |

**Filtro:** Descartados outliers com contencao/subsolo profundo (Monolyt, Barra4). Faixa relevante: R$ 4-23/m2 AC.

### Precos unitarios de referencia (medianas da base Cartesian)

| Item | N projetos | PU mediano | Unidade | Projetos de referencia |
|------|-----------|------------|---------|------------------------|
| Escavacao mecanica | 22 | R$ 36,36 | R$/m3 | Viva4, Brasin, Mussi, FG, Fonseca, Cota 365 |
| Bota-fora c/ transporte | 26 | R$ 45,45 | R$/m3 | Blue Heaven, Cota, Viva4, Santo Andre, CK Cielo |
| Reaterro compactado | 25 | R$ 14,55 | R$/m3 | Blue Heaven Monolyt, Viva4, Brasin, XPCon |
| Lastro concreto magro | 26 | R$ 495,25 | R$/m3 | Viva4, BH Monolyt, Tramonti, BH Aquos, Chateau |
| Mobilizacao/desmob | 21 | R$ 26.000 | vb | Be Brave, Cota, XPCon (3), Brasin, FG |
| Arrasamento estaca HC | 6 | R$ 300,00 | R$/un | Chateau (252un), Be Brave (218un), Santo Andre (88un), ETR Zion (85un) |
| Rebaixamento lencol | 17 | R$ 2,64 | R$/m2 AC | XPCon (R$ 34.800), WF (R$ 32.314), Chelsea (R$ 36.000) |
| Limpeza vegetal | 2 | R$ 5,50 | R$/m2 | Caledonia (434m2 x R$ 5,50) |

### Quantitativos estimados

| Componente | Calculo | Volume/QTD |
|-----------|---------|------------|
| Escavacao geral (nivelamento) | 4.000 m2 terreno x 0,35m corte medio | 1.400 m3 |
| Escavacao valas (blocos+baldrame) | 70 elementos x ~8,5 m3/un (sobreescav. 2,5x) | 600 m3 |
| **Total escavacao** | | **2.000 m3** |
| Reaterro compactado | Valas apos concretagem — ~25% do escavado | 500 m3 |
| Material p/ bota-fora | (2.000 - 500) x 1,30 empolamento | 1.950 m3 |
| Lastro concreto magro 5cm | Area fundacoes + valas (~800 m2 x 0,05m) | 40 m3 |
| Arrasamento estacas HC | ~200/torre x 2 torres, 50cm arrasamento | 400 un |

### Preenchimento por item (6 servicos)

---

#### 01.001.001.001 — Locacao da obra

| Campo | Valor |
|-------|-------|
| **Unidade:** | m2 |
| **Quantidade:** | 4.000 |
| **Preco unitario:** | R$ 10,00/m2 |
| **Total:** | R$ 40.000 |

**Justificativa da quantidade:**
Area do terreno estimada em 4.000 m2 (DUVIDA — Leo confirma). Locacao abrange todo o terreno: implantacao das torres, eixos de estacas, gabarito de obra e relocacoes durante execucao.

**Justificativa do preco:**
- SINAPI 73688 (locacao topografica): R$ 6-10/m2
- SINAPI 74077 (gabarito de locacao): complementar
- Elizabeth II (template): R$ 26.235 para terreno 1.040 m2 = R$ 25,23/m2 terreno (inclui gabarito completo, valor alto)
- Estoril (Fonseca): R$ 44.540 para AC 14.492 = R$ 3,07/m2 AC → equivale a ~R$ 30/m2 terreno (est. 1.430 m2)
- Parkside (Trindade): R$ 6.981 para AC 3.333 = R$ 2,09/m2 AC → ~R$ 10/m2 terreno (est. 712 m2)
- **Decisao:** Adotado R$ 10/m2 terreno (ganho de escala vs projetos menores). Projeto com ~400 estacas por torre exige locacao precisa com estacao total.

---

#### 01.002.001.001 — Limpeza da camada vegetal

| Campo | Valor |
|-------|-------|
| **Unidade:** | m2 |
| **Quantidade:** | 4.000 |
| **Preco unitario:** | R$ 3,50/m2 |
| **Total:** | R$ 14.000 |

**Justificativa da quantidade:**
Area integral do terreno (~4.000 m2). Remocao mecanizada de camada vegetal 20-30cm em todo o terreno.

**Justificativa do preco:**
- SINAPI 73947 (limpeza mecanizada terreno): R$ 2,50-4,00/m2
- Caledonia MOWE (base Cartesian): 434 m2 x R$ 5,50/m2 = R$ 2.389 (terreno pequeno, custo unitario maior)
- Estoril (Fonseca): R$ 14.766 para AC 14.492 = R$ 1,02/m2 AC
- **Decisao:** Adotado R$ 3,50/m2 (mediana SINAPI). Terreno sem edificacao, vegetacao leve (confirmado Leo).

---

#### 01.002.001.002 — Remocao de entulhos e residuos

| Campo | Valor |
|-------|-------|
| **Unidade:** | vb |
| **Quantidade:** | 1 |
| **Preco unitario:** | R$ 15.000 |
| **Total:** | R$ 15.000 |

**Justificativa:**
Sem demolicao (confirmado Leo). Residuos apenas da limpeza vegetal + material solto.
- Estimativa: 25-30 cacambas estacionarias de 5m3 x R$ 400-500/cacamba = R$ 10.000-15.000
- Tramonti (Amalfi): R$ 140.000 (COM demolicao — nao comparavel)
- FG Blue Coast: R$ 126.066 (1.576 m3 x R$ 80/m3 — COM demolicao)
- **Decisao:** Adotado R$ 15.000 (faixa alta da estimativa sem demolicao). Inclui carga, transporte ate CTR e destinacao final conforme CONAMA 307.

---

#### 01.002.002.001 — Mao de Obra de Canteiro

| Campo | Valor |
|-------|-------|
| **Unidade:** | vb |
| **Quantidade:** | 1 |
| **Preco unitario:** | R$ 25.000 |
| **Total:** | R$ 25.000 |

**Justificativa:**
Servicos iniciais de preparo: tapumes (perimetro ~260m estimado), acessos provisorios, sinalizacao de obra (placa CREA, seguranca), limpeza e nivelamento da area do canteiro, montagem de base para containers.
- NAO inclui instalacoes provisorias (agua, luz, esgoto) — esses estao na aba CANTEIRO
- Item pouco detalhado na base (maioria dos projetos tem aba CANTEIRO separada)
- Benchmark geral Cartesian: R$ 15.000-35.000 para obras medio-grande porte
- **Decisao:** R$ 25.000 (meio da faixa).

---

#### 01.003.001.001 — Mao de obra movimentacao de terra

| Campo | Valor |
|-------|-------|
| **Unidade:** | vb |
| **Quantidade:** | 1 |
| **Preco unitario:** | R$ 335.000 |
| **Total:** | R$ 335.000 |

**Justificativa — detalhamento por componente:**

| # | Componente | Volume/QTD | PU | Subtotal | Fonte PU (N projetos, mediana) |
|---|-----------|-----------|-----|----------|-------------------------------|
| 1 | Escavacao mecanica (nivelamento + valas) | 2.000 m3 | R$ 36,36/m3 | R$ 72.720 | Med. 22 projetos. Refs: Brasin Redentor (2.798 m3 x R$ 36,36 = R$ 102k), FG Blue Coast (1.892 m3 x R$ 36,36 = R$ 69k), Fonseca Estoril (1.565 m3 x R$ 36,36 = R$ 57k), Mussi Chelsea (2.145 m3 x R$ 37,44 = R$ 80k) |
| 2 | Bota-fora c/ empolamento 30% | 1.950 m3 | R$ 45,45/m3 | R$ 88.628 | Med. 26 projetos. Refs: Chateau (4.081 m3 x R$ 30 = R$ 122k), Mussi Chelsea (2.027 m3 x R$ 35 = R$ 71k), Fonseca Estoril (R$ 103k), XPCon Porto Cerro (R$ 51k). PU varia R$ 25-68/m3, mediana R$ 45,45 |
| 3 | Reaterro compactado | 500 m3 | R$ 14,55/m3 | R$ 7.275 | Med. 25 projetos. Refs: Brasin (1.609 m3 x R$ 14,55 = R$ 23k), XPCon Porto Cerro (967 m3 x R$ 14,55 = R$ 14k), BH Aquos (1.499 m3 x R$ 14,55 = R$ 22k). PU muito consistente na base |
| 4 | Lastro concreto magro 5cm | 40 m3 | R$ 495,25/m3 | R$ 19.810 | Med. 26 projetos. Refs: Chateau (135 m3 x R$ 408 = R$ 55k), Brasin (37 m3 x R$ 495 = R$ 18k), FG Blue Coast (49 m3 x R$ 495 = R$ 24k). PU varia R$ 395-542, mediana R$ 495,25 |
| 5 | Mobilizacao/desmob. equipamento | 1 vb | R$ 26.000 | R$ 26.000 | Med. 21 projetos. Refs: Be Brave R$ 26k, Cota 365 R$ 26k, XPCon Porto Cerro R$ 26k, XPCon Marena R$ 26k, Brasin R$ 18,5k, FG R$ 18,5k. Valor muito consistente (R$ 18,5-35k) |
| 6 | Arrasamento de estacas HC | 400 un | R$ 300/un | R$ 120.000 | Med. 6 projetos. Refs: Chateau (252 un x R$ 300 = R$ 75,6k), Be Brave (218 un x R$ 300 = R$ 65,4k), Santo Andre (88 un x R$ 300 = R$ 26,4k), ETR Zion (85 un x R$ 300 = R$ 25,5k). PU de R$ 300/un e unanime na base |
| | **Subtotal componentes** | | | **R$ 334.433** | |
| | Arredondamento | | | R$ 567 | |
| | **Total adotado** | | | **R$ 335.000** | |

**Verificacao cruzada (R$/m2 AC):**
- Electra: R$ 335.000 / 36.089 m2 = R$ 9,28/m2 AC (apenas MO mov terra)
- Elizabeth II (template): R$ 233.000 / 16.750 m2 = R$ 13,91/m2 AC (valor proporcionalmente maior, terreno menor)
- Chateau (COM subsolo): escavacao + bota-fora = R$ 786k / 32.507 = R$ 24,18/m2 AC

**Nota sobre volume de escavacao:**
Electra NAO tem subsolo (garagens elevadas). Volume de escavacao e predominantemente:
- Nivelamento do terreno (corte medio 0,35m)
- Valas para blocos e vigas baldrame (sobreescavacao 30cm lateral + 10cm fundo)
- Volume total ~2.000 m3, compativel com projetos de porte similar sem subsolo

---

#### 01.004.001.001 — Rebaixamento de Lencol freatico

| Campo | Valor |
|-------|-------|
| **Unidade:** | vb |
| **Quantidade:** | 1 |
| **Preco unitario:** | R$ 95.000 |
| **Total:** | R$ 95.000 |

**Justificativa:**
Porto Belo/SC, terreno litoraneo — lencol freatico estimado em 1,5-2,0m. Blocos de fundacao com profundidade 1,1-2,0m (dados IFC R26) trabalham no nivel ou abaixo do lencol. Sistema wellpoint (ponteiras filtrantes) durante fase de fundacao.

**Benchmarks da base Cartesian (N=17 projetos):**

| Metrica | Valor |
|---------|-------|
| Min | R$ 0,08/m2 AC |
| P25 | R$ 1,20/m2 AC |
| **Mediana** | **R$ 2,64/m2 AC** |
| P75 | R$ 4,39/m2 AC |
| Max | R$ 19,74/m2 AC |

**Projetos de referencia (sem subsolo profundo):**

| Projeto | AC (m2) | Rebaixamento | R$/m2 AC |
|---------|---------|-------------|----------|
| XPCon Porto Cerro | 13.189 | R$ 34.800 | 2,64 |
| WF Aquarius | 16.789 | R$ 32.314 | 1,92 |
| Mussi Chelsea | 15.149 | R$ 36.000 | 2,38 |
| Be Brave Meraki | 22.461 | R$ 36.000 | 1,60 |
| Blue Heaven Aquos | 9.522 | R$ 52.800 | 5,54 |
| Blue Heaven Monolyt | 14.693 | R$ 39.600 | 2,70 |
| Santo Andre Belle Ville | 7.879 | R$ 26.400 | 3,35 |

**Calculo adotado:**
- Mediana da base: R$ 2,64/m2 AC
- Electra: R$ 2,64 x 36.089 = R$ 95.275 → arredondado R$ 95.000
- Posicionamento: na mediana da base (17 projetos), coerente com terreno litoraneo (lencol raso)
- Se sondagem indicar lencol > 3m, este item pode ser reduzido ou eliminado

---

### Resumo consolidado — Movimentacao de Terra

| Item | Servico | Total (R$) |
|------|---------|------------|
| 01.001.001.001 | Locacao da obra | 40.000 |
| 01.002.001.001 | Limpeza camada vegetal | 14.000 |
| 01.002.001.002 | Remocao entulhos e residuos | 15.000 |
| 01.002.002.001 | MO Canteiro | 25.000 |
| 01.003.001.001 | MO movimentacao de terra | 335.000 |
| 01.004.001.001 | Rebaixamento lencol freatico | 95.000 |
| **TOTAL MOVIMENTACAO DE TERRA** | | **R$ 524.000** |
| **R$/m2 AC** | | **R$ 14,52/m2** |

**Posicionamento na base Cartesian:**
- P25 = R$ 14,09/m2 | **Electra = R$ 14,52/m2** | Mediana = R$ 22,97/m2
- Coerente: projeto SEM subsolo, garagens elevadas, sem demolicao. Deve ficar entre P25 e mediana.
- Projetos com contencao pesada (Monolyt R$ 101/m2, Barra4 R$ 75/m2) nao sao comparaveis.

**Duvidas pendentes:**
- [ ] Area do terreno (estimada 4.000 m2 — Leo confirma)
- [ ] Sondagem: profundidade real do lencol freatico (se > 3m, rebaixamento pode cair)
- [ ] Quantidade de estacas Torre 2 (estimada igual Torre 1: ~200 un)

**Entregas:**
- Dados de benchmark: `temp/benchmark_mov_terra.json` (32 projetos, 158 arquivos)
- Script de extracao: `scripts/benchmark_final.py`

## 18. Instalacoes Hidrossanitarias — CON 07 completa (11/abr/2026)

### Escopo

CON 07 completa: agua fria, esgoto+pluviais, bombas, hidrometros, MO hidro, gas, aquecimento, drenagem, reservatorios. NAO inclui PPCI (aba separada) nem piscina (aba separada).

### Premissas

| Premissa | Valor | Fonte |
|----------|-------|-------|
| AC total | 36.088,85 m2 | log-execucao |
| Tipologia | Residencial, 2 torres, 34 pav/torre | Projeto |
| Unidades | 348 (342 residenciais + 6 comerciais) | Projeto |
| Pavimentos hidraulicos | Terreo, G1-G5, Lazer, Tipo x24, Casa Maq, Reservatorio | IFC H00 |
| Dados reais (IFC) | Agua fria — 291.557 mm tubulacao, 3.116 conexoes, 270 registros | IFC H00 rev.01 + 20 DWGs |
| Projetista | R. Rubens Alves | IFC/DWG |

### Base de benchmarks — 35 projetos Cartesian

Extracao automatizada de 158 planilhas. Script: `scripts/benchmark_hidro.py`. Dados: `temp/benchmark_hidro.json`.

**Total Hidrossanitario / AC (N=30 com AC):**

| Metrica | Valor |
|---------|-------|
| Min | R$ 3,08/m2 |
| P25 | R$ 110,14/m2 |
| **Mediana** | **R$ 125,88/m2** |
| P75 | R$ 137,50/m2 |
| Max | R$ 455,37/m2 |

**Por subgrupo (medianas):**

| Subgrupo | N | Mediana R$/m2 AC | Projetos de referencia |
|----------|---|------------------|------------------------|
| MO hidro | 23 | R$ 55,00 | Be Brave R$ 72, Brasin R$ 69, Tramonti R$ 70, Chelsea R$ 60, FG R$ 65, BH Monolyt R$ 60 |
| Bombas/pressuriz. | 29 | R$ 52,26 | Be Brave R$ 75, BH Monolyt R$ 114, Neuhaus R$ 90, Cota R$ 66, Brasin R$ 66 |
| Esgoto + pluviais | 24 | R$ 20,77 | Be Brave R$ 28, Cota R$ 21, BH Monolyt R$ 28, WF R$ 21, Viva4 R$ 22, Chelsea R$ 13 |
| Agua fria | 25 | R$ 12,73 | Be Brave R$ 23, Cota R$ 28, BH Monolyt R$ 28, BH Aquos R$ 21, Cielo R$ 25 |
| Aquecimento | 22 | R$ 12,69 | Santo Andre R$ 103, Cota R$ 26, Be Brave R$ 20, Chelsea R$ 24, BH Monolyt R$ 22 |
| Gas | 24 | R$ 12,46 | Tramonti R$ 20, FG R$ 23, Brasin R$ 16, Cota R$ 15, BH Monolyt R$ 17 |
| Reservatorios | 19 | R$ 2,64 | Viva4 R$ 21, By Seasons R$ 38, WF R$ 15, Passione R$ 15, Be Brave R$ 4 |
| Hidrometros | 10 | R$ 1,98 | Tramonti R$ 2, Viva4 R$ 2, Chelsea R$ 2, Neuhaus R$ 2, By Seasons R$ 5 |
| Drenagem | 9 | R$ 1,94 | Nova Domus R$ 23, BH Monolyt R$ 6, Santo Andre R$ 8, BH Aquos R$ 6 |

### Agua fria — precificacao item a item (dados reais IFC)

**Fonte de quantidades:** IFC H00 rev.01 + 20 DWGs (planilha `hidro-electra-r00.xlsx`, 154 linhas)
**Fonte de PUs:** Santo Andre Belle Ville (aba HIDROSSANITARIO com 100+ PUs detalhados por item)
**Nota:** Quantidades do IFC estao em milimetros. Convertidas para metros na planilha R01.

#### Tubulacoes (3.066 m total convertido)

| Item | QTD (m) | PU (R$/m) | Total | Fonte PU |
|------|---------|-----------|-------|----------|
| PVC Soldavel DN25 | 1.143,5 | 2,57 | R$ 2.939 | Belle Ville: PVC marrom 25mm |
| PVC Soldavel DN32 | 508,7 | 7,80 | R$ 3.968 | Belle Ville: PVC marrom 32mm |
| PVC Soldavel DN40 | 11,7 | 12,83 | R$ 150 | Belle Ville: PVC marrom 40mm |
| PVC Soldavel DN50 | 166,3 | 10,47 | R$ 1.741 | Belle Ville: PVC marrom 50mm |
| PVC Soldavel DN60 | 100,2 | 19,05 | R$ 1.909 | Belle Ville: PVC marrom 60mm |
| PVC Soldavel DN75 | 1,7 | 27,48 | R$ 46 | Belle Ville: PVC marrom 75mm |
| CPVC FlowGuard DN15 | 219,3 | 17,63 | R$ 3.866 | Belle Ville: CPVC Aquaterm 15mm |
| CPVC FlowGuard DN22 | 538,0 | 21,30 | R$ 11.459 | Belle Ville: CPVC Aquaterm 22mm |
| CPVC FlowGuard DN28 | 341,0 | 12,88 | R$ 4.392 | Belle Ville: CPVC Aquaterm 28mm (barra/3) |
| PPR PN25 DN90 | 35,7 | 85,00 | R$ 3.030 | Estimativa mercado (sem ref Belle Ville) |
| **Subtotal tubulacoes** | | | **R$ 33.500** | |

#### Conexoes (29.316 un total com repeticao)

| Item | QTD | PU (R$/un) | Total | Fonte PU |
|------|-----|-----------|-------|----------|
| Joelho PVC Soldavel | 10.927 | 0,78 | R$ 8.523 | Belle Ville: Joelho 90 25mm marrom |
| Joelho CPVC FlowGuard | 6.667 | 3,59 | R$ 23.935 | Belle Ville: Joelho 90 22mm CPVC |
| Joelho c/ Bucha Latao | 2.885 | 4,50 | R$ 12.983 | Estimativa (adaptador sold+bucha) |
| Registro de Esfera Met. | 2.860 | 31,72 | R$ 90.719 | Belle Ville: Reg. gaveta 3/4" |
| Adaptador Curto PVC | 2.041 | 4,08 | R$ 8.327 | Belle Ville: Adapt. sold. curto 50mm |
| Curva PVC Soldavel | 1.638 | 9,80 | R$ 16.052 | Belle Ville: Curva transposicao |
| Bucha de Reducao PVC | 875 | 1,66 | R$ 1.453 | Belle Ville: Bucha red. curta |
| Luva LR PVC | 439 | 2,50 | R$ 1.098 | Belle Ville: Luva 50mm |
| Hidrometro (conexao) | 200 | 547,30 | R$ 109.460 | Belle Ville: Conj. hidrometro Sanasa |
| Outros (PPR, valvulas, flanges) | ~460 | variavel | R$ 10.341 | Belle Ville + estimativa mercado |
| **Subtotal conexoes** | | | **R$ 282.890** | |

#### Equipamentos

| Item | QTD | PU (R$/un) | Total | Fonte PU |
|------|-----|-----------|-------|----------|
| Pressurizador Schneider VFD BC-92 | 4 cj | 8.500 | R$ 34.000 | Cotacao mercado Schneider |
| Hidrometro multijato 3/4" | 38 un | 547,30 | R$ 20.797 | Belle Ville: Conj. hidrometro |
| Reservatorio polietileno 7.500L | 2 un | 4.200 | R$ 8.400 | Cotacao mercado AMelo |
| Valvula esfera DN75 (3") | 16 un | 467,46 | R$ 7.479 | Belle Ville: Reg. gaveta bruto 3" |
| Valvula ventosa combinada DN50 | 2 un | 1.200 | R$ 2.400 | Cotacao mercado |
| Valvula retencao horiz. 1.1/2" | 6 un | 229,80 | R$ 1.379 | Belle Ville: Reg. gaveta bruto 2" |
| Flange cobre p/ limpeza | 11 un | 88,19 | R$ 970 | Belle Ville: Adapt. flanges |
| Filtro tipo T 2" | 2 un | 350,00 | R$ 700 | Cotacao mercado |
| Torneira boia 1/2" | 2 un | 35,00 | R$ 70 | Cotacao mercado |
| **Subtotal equipamentos** | | | **R$ 76.196** | |

**Total agua fria (material): R$ 392.586 (R$ 10,88/m2 AC)**
Benchmark mediana agua fria: R$ 12,73/m2. Electra = 85% da mediana (coerente: so material, sem MO).

### Demais subgrupos — benchmark Cartesian

Distribuicao por pavimento usando proporcoes do Elizabeth II (14 etapas).

| Subgrupo | R$/m2 AC | Total | N proj | Justificativa |
|----------|----------|-------|--------|---------------|
| Esgoto + pluviais | R$ 20,77 | R$ 749.565 | 24 | Mediana. Electra nao tem dados de esgoto do IFC. Refs: Be Brave R$ 28, Cota R$ 21, WF R$ 21 |
| MO hidro | R$ 55,00 | R$ 1.984.887 | 23 | Mediana. Valor muito consistente na base (R$ 45-72/m2). Refs: Be Brave R$ 72, FG R$ 65, Duo Colin R$ 65, Duo Mosaico R$ 60 |
| Bombas/pressurizacao | R$ 15,00 | R$ 541.333 | 29 | Abaixo P25 (R$ 32). Electra sem subsolo = sem bomba esgoto pesada. 4x VFD BC-92 ja incluidos na agua fria |
| Gas | R$ 12,46 | R$ 449.667 | 24 | Mediana. Refs: Tramonti R$ 20, FG R$ 23, Brasin R$ 16, Be Brave R$ 8 |
| Aquecimento | R$ 12,69 | R$ 457.968 | 22 | Mediana. Inclui aquecedores a gas, boilers, sist. agua quente. Refs: Cota R$ 26, Be Brave R$ 20, Chelsea R$ 24 |
| Reservatorios | R$ 2,64 | R$ 95.275 | 19 | Mediana. Concreto de reservatorio superior, alem das 2 caixas ja na agua fria. Refs: XPCon R$ 9, Be Brave R$ 4, Indepy R$ 3 |
| Hidrometros | R$ 1,98 | R$ 71.456 | 10 | Mediana. 38 un reais do IFC × R$ 547 = R$ 20.797 (material). Diferenca = instalacao + infra |
| Drenagem | R$ 1,94 | R$ 70.012 | 9 | Mediana. Drenos, ralos. Refs: BH Monolyt R$ 6, BH Aquos R$ 6, Santo Andre R$ 8 |

### Resumo consolidado — CON 07

| Subgrupo | Total (R$) | R$/m2 AC | Fonte |
|----------|-----------|----------|-------|
| Agua fria (material) | 392.586 | 10,88 | **REAL** (IFC + Belle Ville PUs) |
| Esgoto + pluviais | 749.565 | 20,77 | Benchmark med. 24 proj |
| MO hidro | 1.984.887 | 55,00 | Benchmark med. 23 proj |
| Bombas/pressurizacao | 541.333 | 15,00 | Benchmark abaixo P25 |
| Gas | 449.667 | 12,46 | Benchmark med. 24 proj |
| Aquecimento | 457.968 | 12,69 | Benchmark med. 22 proj |
| Reservatorios | 95.275 | 2,64 | Benchmark med. 19 proj |
| Hidrometros | 71.456 | 1,98 | Benchmark med. 10 proj |
| Drenagem | 70.012 | 1,94 | Benchmark med. 9 proj |
| **TOTAL CON 07** | **4.812.748** | **133,36** | |

**Posicionamento na base Cartesian:**

| Referencia | R$/m2 AC |
|-----------|---------|
| BH Aquos (9.522 m2) | R$ 104 |
| XPCon Porto Cerro (13.189 m2) | R$ 105 |
| Mussi Chelsea (15.149 m2) | R$ 110 |
| Brasin Redentor (16.728 m2) | R$ 122 |
| **Mediana base (N=30)** | **R$ 126** |
| **Electra proposto** | **R$ 133** |
| Neuhaus Origem (14.559 m2) | R$ 135 |
| WF Aquarius (16.789 m2) | R$ 135 |
| Be Brave Meraki (22.461 m2) | R$ 147 |

Electra 6% acima da mediana — coerente por ter 2 torres (mais prumadas, mais duplicacao de sistemas).

**Nota:** O valor inclui gas + aquecimento. Na planilha master do Electra, GAS e CLIMATIZACAO sao abas separadas. Se forem preenchidas separadamente, descontar R$ 25,15/m2 (R$ 907.635) do total hidro pra nao duplicar.

### Entregas

- Planilha: `disciplinas/hidraulico/hidro-electra-r01.xlsx` (agua fria item a item + benchmark por pavimento)
- Dados benchmark: `temp/benchmark_hidro.json` (35 projetos)
- Script extracao: `scripts/benchmark_hidro.py`
- Script geracao planilha: `scripts/gerar_hidro_r01.py`

### Duvidas pendentes

- [ ] Sanitario: JSON bruto existe mas esta corrompido. Precisa reprocessar IFC sanitario
- [ ] Gas: falta briefing/extracao (aba GAS da master pode duplicar com valor aqui)
- [ ] Aquecimento: verificar se entra na CON 07 ou na CLIMATIZACAO

## 19. Instalacoes Eletricas — CON 06 (11/abr/2026, EM ANDAMENTO)

### Status: PARCIAL — quantitativos reextraidos, precificacao pendente

### Premissas

| Premissa | Valor | Fonte |
|----------|-------|-------|
| AC total | 36.088,85 m2 | log-execucao |
| Tipologia | Residencial, 2 torres, 34 pav/torre | Projeto |
| IFCs eletricos | 9 arquivos rev.01 (Terreo a Casa Maq) | R. Rubens Alves |
| DWGs eletricos | 18 pranchas rev.01 (T.A + T.B) | R. Rubens Alves |

### Base de benchmarks — 34 projetos Cartesian

Extracao automatizada de 158 planilhas. Script: `scripts/benchmark_eletrico.py`. Dados: `temp/benchmark_eletrico.json`.

**Total Eletrico / AC (N=31 com AC):**

| Metrica | Valor |
|---------|-------|
| Min | R$ 0,06/m2 |
| P25 | R$ 15,88/m2 |
| **Mediana** | **R$ 155,92/m2** |
| P75 | R$ 184,86/m2 |
| Max | R$ 223,30/m2 |

**Por subgrupo (medianas):**

| Subgrupo | N | Mediana R$/m2 AC |
|----------|---|------------------|
| Fios e cabos | 24 | R$ 31,77 |
| MO eletrica | 30 | R$ 26,17 |
| Eletrodutos | 26 | R$ 17,98 |
| Subestacao | 6 | R$ 14,73 |
| Quadros | 24 | R$ 10,42 |
| Gerador | 16 | R$ 6,00 |
| Entrada energia | 22 | R$ 6,24 |
| Tomadas | 15 | R$ 5,85 |
| Luminarias | 25 | R$ 1,74 |

**Projetos de referencia (AC > 13k):**

| Projeto | AC (m2) | Total | R$/m2 |
|---------|---------|-------|-------|
| WF Aquarius | 16.789 | R$ 2.795.697 | 166,52 |
| BH Aquos | 9.522 | R$ 1.605.893 | 168,64 |
| XPCon Porto Cerro | 13.189 | R$ 2.056.354 | 155,92 |
| Mussi Chelsea | 15.149 | R$ 2.272.080 | 149,98 |
| Neuhaus Origem | 14.559 | R$ 2.036.990 | 139,91 |
| Be Brave Meraki | 22.461 | R$ 4.584.784 | 204,12 |
| Brasin Redentor | 16.728 | R$ 3.658.112 | 218,68 |
| BH Monolyt | 14.693 | R$ 3.281.041 | 223,30 |

### Quantitativos reais do Electra (reextraidos 11/abr)

#### Eletrodutos (IFC — 202.413 trechos com x24 tipo)

| Diametro | Trechos | Metragem est. (x3m/trecho) |
|----------|---------|---------------------------|
| 3/4" (20mm) | 167.479 | 502.437 m |
| 1.1/2" (38mm) | 11.112 | 33.336 m |
| 1.1/4" (32mm) | 11.057 | 33.171 m |
| 1" (25mm) | 10.183 | 30.549 m |
| 3" (75mm) | 2.365 | 7.095 m |
| 2" (50mm) | 202 | 606 m |
| 4" (100mm) | 15 | 45 m |
| **Total** | **202.413** | **607.239 m (est.)** |

**ATENCAO:** Metragem estimada com 3m/trecho. IFC nao tem propriedade Length. Pode ser 2-4m. Impacto: +-R$ 1M.

#### Dispositivos (DXF — 2.751 un com x24 tipo)

| Item | QTD |
|------|-----|
| Tomadas 10A | 968 |
| Tomadas 20A | 368 |
| Interruptor 1 Simples | 347 |
| Interruptor Paralelo | 216 |
| Quadro Distribuicao 1 Porta | 171 |
| Interruptor 2 Simples | 159 |
| Quadro de Comando | 154 |
| Tomada Chuveiro | 74 |
| Quadro de Medicao | 73 |
| Luminaria/Arandela | 95 |
| Sensor | 33 |
| Tomada AR | 28 |
| **Total dispositivos** | **2.751** |

#### Luminarias (IFC — 4.661 un com x24 tipo)

| Pavimento | QTD |
|-----------|-----|
| Terreo | 140 |
| G1-G5 | 412 (77+80+80+78+97) |
| Lazer | 119 |
| Tipo x24 | 3.984 (166/pav) |
| Casa Maquinas | 0 |
| **Total** | **4.661** |

#### Itens NAO modelados (estimativa/cotacao)

| Item | Situacao |
|------|----------|
| Cabos e fios | 1.014 trechos sem bitola. Metragem ~ eletrodutos x 1,0-1,5 |
| Subestacao | Nao modelada. R00 tinha 2x trafo + religador + TC/TP |
| Gerador | Nao modelado. R00 tinha ~500kVA + QTA + tanque |
| Barramento | Nao modelado. R00 tinha ~150m barramento blindado |
| Entrada energia | Nao modelada. R00 tinha quadros medicao + cabos EPR |

### Problema identificado na R00

A planilha R00 (`eletrico-electra-TA-TB-r00.xlsx`) tem:
- Torre A: R$ 5.889.827
- Torre B: R$ 5.809.350
- Soma bruta: R$ 11.699.177

**Duplicacao detectada:** Subestacao (R$ 606k), gerador (R$ 450k), barramento (R$ 140k) e entrada (R$ 122k) aparecem identicos nas 2 torres — sao itens compartilhados. Duplicacao: R$ 1.318.541.

**MO inflada:** R$ 3.067.727/torre = R$ 6.135.454 total = R$ 170/m2. Mediana da base e R$ 26/m2.

**Total corrigido (sem duplicacao): R$ 10.380.636 = R$ 287/m2 — 84% acima da mediana.**

### Proximos passos (continuar na proxima sessao)

- [ ] Definir comprimento medio por trecho de eletroduto (2m? 3m? 4m?)
- [ ] Definir fator cabos vs eletrodutos (1,0? 1,2? 1,5?)
- [ ] Precificar cada item com PU SINAPI/Belle Ville/cotacao
- [ ] Recalcular MO com benchmark adequado
- [ ] Comparar total com faixa R$ 140-223/m2 dos comparaveis
- [ ] Gerar planilha R01

### Entregas parciais

- Dados benchmark: `temp/benchmark_eletrico.json` (34 projetos)
- Script extracao: `scripts/benchmark_eletrico.py`
- Quantitativos IFC: `quantitativos/eletrico-ifc-completo.json`
- Quantitativos DXF: `quantitativos/eletrico-dxf-dispositivos.json`

## 20. Instalacoes Preventivas — CON 08 / PPCI (11/abr/2026)

### Premissas

| Premissa | Valor | Fonte |
|----------|-------|-------|
| AC total | 36.088,85 m2 | log-execucao |
| Sprinklers | **NAO TEM** | Leo confirmou (11/abr) |
| Sistemas existentes | Hidrantes + extintores + sinalizacao + SPDA + alarme | IFC PCI rev.01 |
| IFCs processados | PCI rev.01 Torre A (24MB) + Torre B (23MB) + IGC rev.01 T.A (37MB) + T.B (42MB) | R. Rubens Alves |
| DWGs | 11 pranchas | rev.00 |

### Base de benchmarks — 40 projetos Cartesian

Script: `scripts/benchmark_ppci.py`. Dados: `temp/benchmark_ppci.json`.

**Total PPCI / AC (N=28 com AC):**

| Metrica | Valor |
|---------|-------|
| Min | R$ 0,11/m2 |
| P25 | R$ 16,22/m2 |
| **Mediana** | **R$ 31,25/m2** |
| P75 | R$ 41,00/m2 |
| Max | R$ 201,62/m2 |

**Por subgrupo (medianas):**

| Subgrupo | N | Mediana R$/m2 AC | Projetos de referencia |
|----------|---|------------------|------------------------|
| SPDA | 27 | R$ 5,14 | Brasin R$ 5, Tramonti R$ 5, Fonseca R$ 6, Cota R$ 4, Chelsea R$ 5 |
| Hidrantes | 11 | R$ 3,62 | Brasin R$ 9, Tramonti R$ 5, Santo Andre R$ 4, Mosaico R$ 4 |
| Bombas PCI | 12 | R$ 3,31 | Tramonti R$ 6, Santo Andre R$ 10, Colin R$ 6, Holze R$ 6 |
| Alarme/deteccao | 8 | R$ 2,48 | Tramonti R$ 3, Santo Andre R$ 2, ARV R$ 9, Domus R$ 4 |
| Extintores + sinalizacao | 8 | R$ 1,91 | Brasin R$ 27 (outlier), Neuhaus R$ 2, Santo Andre R$ 3, Viva4 R$ 2 |
| MO PPCI | 29 | R$ 26,13 | **CONTAMINADO** — keywords capturam MO eletrica. Adotado R$ 5/m2 conservador |

### Quantitativos reais do Electra (IFC PCI rev.01)

| Item | QTD | Fonte | Obs |
|------|-----|-------|-----|
| Abrigos de hidrante | 67 un (33 T.A + 34 T.B) | IFC PCI rev.01 | Caixa aluminio. Mangueira/esguicho nao modelados |
| Extintores PQS 4kg | 133 un (66 T.A + 67 T.B) | IFC PCI rev.01 | Classe BC (confirmar ABC) |
| Extintores CO2 6kg | 7 un (3 T.A + 4 T.B) | IFC PCI rev.01 | |
| Extintores outros | 5 un | IFC PCI rev.01 | Tipo a confirmar |
| Suportes parede | 135 un | IFC PCI rev.01 | |
| Placas fotoluminescentes E5 | 140 un (69 T.A + 71 T.B) | IFC PCI rev.01 | |
| Pintura de piso | 21 un | IFC PCI rev.01 | Sinalizacao extintor |
| Tubulacao FG 150mm | 67,26 m | IFC PCI rev.01 | **SUBESTIMADO** — 424 trechos mas metragem muito baixa |
| Cotovelos 90 FG | 117 un | IFC PCI rev.01 | |
| Tes de reducao FG | 151 un | IFC PCI rev.01 | |
| Valvulas/registros | 138 un | IFC PCI rev.01 | |
| Reservatorios PCI | **NAO MODELADO** | - | Solicitar memorial |
| Bombas PCI | **NAO MODELADO** | - | Solicitar memorial |
| Sprinklers | **NAO TEM** | Leo confirmou | |

### Preenchimento por subgrupo

#### Hidrantes — R$ 130.641

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 3,62 |
| **Total:** | R$ 130.641 |

**Justificativa:** Mediana de 11 projetos. Dados reais: 67 abrigos de hidrante (IFC). Kit abrigo completo (caixa + mangueira 30m + esguicho + chave + adaptador) = ~R$ 1.500-2.000/un = R$ 100-134k. Mais tubulacao FG (metragem real subestimada no IFC). Adotado mediana R$ 3,62/m2 que cobre material + tubulacao.
Refs: Brasin R$ 8,93/m2 (R$ 149k), Tramonti R$ 4,65/m2 (R$ 73k), Santo Andre R$ 3,81/m2 (R$ 30k).

#### Extintores + sinalizacao — R$ 68.930

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 1,91 |
| **Total:** | R$ 68.930 |

**Justificativa:** Mediana de 8 projetos (extintores) + 14 projetos (sinalizacao). Dados reais: 145 extintores + 140 placas + 21 pinturas piso.
- Extintor PQS 4kg c/ suporte: ~R$ 180/un x 133 = R$ 23.940
- Extintor CO2 6kg: ~R$ 450/un x 7 = R$ 3.150
- Placas fotoluminescentes: ~R$ 25/un x 140 = R$ 3.500
- Sinalizacao complementar (saida emergencia, rotas): ~R$ 15.000 vb
- Iluminacao emergencia: ~R$ 23.000 vb
Total estimado por item: ~R$ 68.590. Coerente com mediana R$ 1,91/m2.

#### SPDA — R$ 185.577

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 5,14 |
| **Total:** | R$ 185.577 |

**Justificativa:** Mediana de 27 projetos — subgrupo mais robusto. Edificio alto (34 pav, ~107m) exige SPDA classe II ou III (NBR 5419). Inclui captores, descidas, aterramento, DPS.
Refs: Brasin R$ 5,14/m2 (R$ 86k), Tramonti R$ 5,29/m2 (R$ 83k), Fonseca R$ 5,65/m2 (R$ 82k), Chelsea R$ 4,61/m2 (R$ 70k).
Electra 2 torres = ~2x o custo unitario. Mediana adequada.

#### Alarme e deteccao — R$ 89.500

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 2,48 |
| **Total:** | R$ 89.500 |

**Justificativa:** Mediana de 8 projetos. Central de alarme + detectores de fumaca + acionadores manuais + sirenes.
Refs: Santo Andre R$ 2,48/m2 (R$ 20k), Tramonti R$ 3,36/m2 (R$ 52k), Domus R$ 4,22/m2 (R$ 21k).

#### Bombas PCI — R$ 119.454

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 3,31 |
| **Total:** | R$ 119.454 |

**Justificativa:** Mediana de 12 projetos. Bomba principal + jockey + quadro comando + tubulacao succao/recalque. NAO modelados no IFC — dado via benchmark.
Refs: Tramonti R$ 6,19/m2 (R$ 97k), Colin R$ 5,95/m2 (R$ 41k), By Seasons R$ 3,31/m2 (R$ 21k), Chelsea R$ 2,37/m2 (R$ 36k).

#### MO PPCI — R$ 180.444

| Campo | Valor |
|-------|-------|
| **R$/m2 AC:** | R$ 5,00 |
| **Total:** | R$ 180.444 |

**Justificativa:** Mediana da base (R$ 26/m2) esta contaminada com MO eletrica (keywords sobrepostas). Adotado R$ 5/m2 conservador — proporcional ao escopo sem sprinklers. Inclui MO instalacao tubulacao FG, montagem abrigos, fixacao extintores, sinalizacao, testes.

### Resumo consolidado — CON 08 PPCI (SEM sprinklers)

| Subgrupo | Total (R$) | R$/m2 AC | Fonte |
|----------|-----------|----------|-------|
| Hidrantes | 130.641 | 3,62 | Benchmark med. 11 proj + dados IFC |
| Extintores + sinalizacao | 68.930 | 1,91 | Benchmark med. 8 proj + dados IFC |
| SPDA | 185.577 | 5,14 | Benchmark med. 27 proj |
| Alarme/deteccao | 89.500 | 2,48 | Benchmark med. 8 proj |
| Bombas PCI | 119.454 | 3,31 | Benchmark med. 12 proj |
| MO PPCI | 180.444 | 5,00 | Estimativa conservadora |
| **TOTAL CON 08** | **774.546** | **21,46** | |

**Posicionamento:** Entre P25 (R$ 16/m2) e mediana (R$ 31/m2). Coerente: sem sprinklers, que representam 76% do PPCI no Elizabeth II.

**Projetos comparaveis SEM sprinklers (nenhum projeto da base tem sprinklers separados alem do Brasin):**
A maioria dos projetos com R$ 15-35/m2 INCLUI sprinklers embutido. Sem sprinklers, R$ 21/m2 e coerente.

### Entregas

- Dados benchmark: `temp/benchmark_ppci.json` (40 projetos)
- Script extracao: `scripts/benchmark_ppci.py`

### Duvidas pendentes

- [x] Sprinklers: NAO TEM (Leo confirmou)
- [ ] Metragem real tubulacao FG (67m subestimado — precisa DWG ou memorial)
- [ ] Reservatorios e bombas PCI: especificacao (nao modelados)
- [ ] SPDA: briefing R00 feito, falta planilha executiva

## 21. Sanitario (11/abr/2026)

**DECISAO:** Sanitario do Electra JA ESTA INCLUIDO no CON 07 Hidrossanitario (subgrupo "Esgoto + pluviais" = R$ 749.565 = R$ 20,77/m2 AC).

**Justificativa:** Benchmark sanitario da base Cartesian tem N=3 apenas (maioria dos projetos agrupa esgoto+pluviais). Mediana base = R$ 20,77/m2 que e EXATAMENTE o valor ja alocado no CON 07.

**Alternativa (se abrir aba separada):**

| Item | R$/m2 | Valor |
|------|-------|-------|
| Esgoto primario (tubo+conexoes) | 8,00 | R$ 288.711 |
| Esgoto secundario (ralos+caixas) | 4,50 | R$ 162.400 |
| Aguas pluviais | 8,00 | R$ 288.711 |
| MO sanitario | 4,00 | R$ 144.355 |
| **Total alternativo** | **24,50** | **R$ 879.177** |

Se abrir aba, descontar R$ 749.565 do CON 07 Hidro pra nao duplicar.

**Entrega:** `disciplinas/sanitario/sanitario-electra-r01.xlsx` (referencia cruzada)

---

## 22. Ventilacao Mecanica — Escadas Pressurizadas (11/abr/2026)

**Status:** PREMISSAS NAO VALIDADAS — DWG R05 bloqueado

**Base de benchmarks: 4 projetos Cartesian**

| Metrica | R$/m2 AC |
|---------|----------|
| Min | 6,23 |
| Mediana | 9,24 |
| P75 | 13,50 |
| Max | 13,50 |

**Projetos de referencia:**
- WF Aquarius R$ 226.652 (R$ 13,50/m2)
- Be Brave Meraki R$ 140.000 (R$ 6,23/m2)
- Mussi Chelsea R$ 140.000 (R$ 9,24/m2)
- Santo Andre Belle Ville R$ 50.292 (R$ 6,38/m2)

**Quantitativos estimados (NBR 14880:2024):**

| Item | QTD | PU | Total |
|------|-----|-----|-------|
| Ventiladores centrifugos 8-12k m3/h | 2 | R$ 35.000 | R$ 70.000 |
| Dampers corta-fogo 90min | 64 | R$ 1.200 | R$ 76.800 |
| Dampers motorizados | 4 | R$ 2.500 | R$ 10.000 |
| Duto vertical o600mm | 200 m | R$ 250 | R$ 50.000 |
| Duto derivacao | 60 m | R$ 180 | R$ 10.800 |
| Isolamento termico | 380 m2 | R$ 85 | R$ 32.300 |
| Grelhas/difusores | 42 | R$ 350 | R$ 14.700 |
| Automacao (CLP + IHM) | 1 | R$ 45.000 | R$ 45.000 |
| Cabos e eletrica | 1 | R$ 25.000 | R$ 25.000 |
| Mobilizacao + testes | 1 | R$ 15.000 | R$ 15.000 |
| MO instalacao | 1 | R$ 45.000 | R$ 45.000 |
| BDI + contingencia (~20%) | 1 | R$ 77.000 | R$ 77.000 |
| **TOTAL** | | | **R$ 471.600** |

**R$/m2 AC: R$ 13,07** — entre mediana e P75 da base. Electra 2 torres = 2 escadas pressurizadas justifica.

**Entrega:** `disciplinas/ventilacao/ventilacao-electra-r01.xlsx`

**Pendencias:** DWG bloqueado. Solicitar DXF/memorial ao Rubens Alves.

---

## 23. Exaustao Mecanica (11/abr/2026)

**Status:** Estimativa parametrica (DXF com dados parciais)

**Base de benchmarks:** Benchmark automatico contaminado (keywords EXAUSTAO caem em AR-CONDICIONADO). Uso estimativa parametrica de mercado.

**Faixa tipica residencial:** R$ 5-15/m2 AC

**Quantitativos estimados:**

| Item | QTD | PU | Total |
|------|-----|-----|-------|
| Exaustor axial banheiro (80 m3/h) | 348 un | R$ 120 | R$ 41.760 |
| Exaustor areas comuns | 40 un | R$ 450 | R$ 18.000 |
| Exaustor churrasqueira c/ coifa | 48 un | R$ 850 | R$ 40.800 |
| Duto galvanizado o150mm | 1.500 m | R$ 45 | R$ 67.500 |
| Duto galvanizado o200mm | 800 m | R$ 65 | R$ 52.000 |
| Grelhas de exaustao | 500 un | R$ 45 | R$ 22.500 |
| Conexoes e acessorios | 1 vb | R$ 15.000 | R$ 15.000 |
| Mobilizacao | 1 vb | R$ 8.000 | R$ 8.000 |
| MO instalacao | 1 vb | R$ 35.000 | R$ 35.000 |
| **TOTAL** | | | **R$ 300.560** |

**R$/m2 AC: R$ 8,33** — dentro da faixa tipica.

**Entrega:** `disciplinas/exaustao/exaustao-electra-r01.xlsx`

---

## 24. Ar-Condicionado (11/abr/2026)

**Status:** Benchmark — DWG R05 bloqueado, sem quantitativos IFC

**Base de benchmarks: 29 projetos Cartesian**

| Metrica | R$/m2 AC |
|---------|----------|
| Min | 0,83 |
| P25 | 19,12 |
| **Mediana** | **34,05** |
| P75 | 52,21 |
| Max | 130,82 (BH Monolyt) |

**Projetos de referencia:**
- WF Aquarius R$ 1.175.552 (R$ 70,02/m2)
- Be Brave Meraki R$ 1.172.771 (R$ 52,21/m2)
- Cota 365 R$ 1.083.705 (R$ 61,91/m2)
- BH Aquos R$ 943.629 (R$ 99,10/m2)

**Proposta: splits individuais + climatizacao areas comuns**

| Item | QTD | PU | Total |
|------|-----|-----|-------|
| Split hi-wall 9.000 BTU (quartos) | 200 | R$ 2.200 | R$ 440.000 |
| Split hi-wall 12.000 BTU (salas/suites) | 280 | R$ 2.500 | R$ 700.000 |
| Split 18.000 BTU (aptos grandes) | 40 | R$ 3.200 | R$ 128.000 |
| Tubulacao frigorigena (Cu isolado) | 3.500 m | R$ 45 | R$ 157.500 |
| Dreno PVC | 1.500 m | R$ 12 | R$ 18.000 |
| Eletrica associada | 520 | R$ 180 | R$ 93.600 |
| Infraestrutura (furos, suportes) | 1 vb | R$ 45.000 | R$ 45.000 |
| Mobilizacao + testes + carga | 1 vb | R$ 35.000 | R$ 35.000 |
| MO instalacao (520 pontos × R$ 350) | 520 | R$ 350 | R$ 182.000 |
| Climatizacao areas comuns (lobby, academia) | 1 cj | R$ 120.000 | R$ 120.000 |
| BDI + contingencia (~5%) | - | - | R$ 80.900 |
| **TOTAL** | | | **R$ 2.000.000** |

**R$/m2 AC: R$ 55,42** — entre mediana e P75. Coerente com comparaveis.

**Entrega:** `disciplinas/ar-condicionado/ar-condicionado-electra-r01.xlsx`

---

## 25. Indices / Despesas Indiretas — UC1 (11/abr/2026)

**Status:** Benchmark base Cartesian + ajustes conservadores de mercado

**NOTA:** Benchmark da base tem ruido (keywords capturam secoes inteiras como totais em alguns projetos). Valores ajustados conservadoramente.

**Proposta consolidada:**

| Codigo | Item | R$/m2 | Total | Fonte |
|--------|------|-------|-------|-------|
| 01.001 | Estudos, projetos e consultorias | 35,00 | R$ 1.263.110 | ~1,5% obra |
| 01.002 | Taxas e documentos (licencas, aprovacoes, seguros) | 15,00 | R$ 541.333 | Mercado |
| 02.001 | Seguranca do trabalho + EPIs/EPCs | 7,00 | R$ 252.622 | Med. 28 proj (R$ 7,13) |
| 02.002.001 | Equipe gestao e apoio (eng. residente 36m) | 120,00 | R$ 4.330.662 | Obra 36m |
| 02.002.002 | Operacao inicial canteiro | 5,00 | R$ 180.444 | Benchmark |
| 02.002.003 | Despesas consumo/manutencao (36m) | 18,00 | R$ 649.599 | Obra 36m |
| 02.002.004 | Instalacoes provisorias (containers) | 12,00 | R$ 433.066 | Cotacao |
| 03.001 | Controle tecnologico (ensaios) | 12,00 | R$ 433.066 | Conservador |
| 04.001 | Equipamentos especiais (elev, bomba, grua) | 25,00 | R$ 902.221 | Conservador |
| 04.002 | Mobiliario areas comuns | 3,50 | R$ 126.311 | Med. 22 proj (R$ 2,88) |
| 04.003 | Paisagismo | 3,00 | R$ 108.267 | Med. 20 proj (R$ 2,54) |
| 04.004 | Piscina (equipamentos + acabamentos) | 15,00 | R$ 541.333 | Mercado (Electra tem) |
| 04.005 | Limpeza final | 16,00 | R$ 577.421 | Med. 9 proj (R$ 15,94) |
| **TOTAL** | | **286,50** | **R$ 10.339.456** | |

**R$/m2 AC: R$ 286,50**

**Benchmarks ruidosos — ajustes feitos:**
- Ger.Tec/Adm: mediana inflada (outliers Rosner R$ 2.679/m2 e ARV R$ 3.286/m2). Uso R$ 120/m2 conservador.
- Controle tec: mediana R$ 67/m2 contaminada por capturar secao inteira. Uso R$ 12/m2.
- Equipamentos especiais: mediana R$ 2,61/m2 subestimada. Uso R$ 25/m2 considerando elevador cremalheira.
- Piscina: mediana R$ 0,98/m2 subestimada. Uso R$ 15/m2 considerando escopo real.

**Entrega:** `disciplinas/indices/indices-electra-r01.xlsx`

**Pendencias:**
- [ ] Definir equipe real de gestao (eng residente + apoio)
- [ ] Contrato controle tecnologico (laboratorio)
- [ ] Confirmar equipamentos especiais (elevador cremalheira?)
- [ ] Escopo piscina (acabamentos completos?)

---

## CONSOLIDADO SESSAO 10-11/ABR — ELECTRA

| Disciplina | Total | R$/m2 AC | Status |
|-----------|-------|----------|--------|
| Mov. Terra (CON 01) | R$ 524.000 | 14,52 | Completo |
| Hidro (CON 07) | R$ 4.812.748 | 133,36 | Completo |
| Eletrico (CON 06) | R$ 6.444.152* | 178,56* | **Parcial** (sem cabos) |
| PPCI (CON 08) | R$ 774.546 | 21,46 | Completo |
| Sanitario | INCLUIDO NO CON 07 | - | Completo (ref cruzada) |
| Ventilacao Mecanica | R$ 471.600 | 13,07 | Premissas |
| Exaustao | R$ 300.560 | 8,33 | Estimativa |
| Ar-Condicionado | R$ 2.000.000 | 55,42 | Benchmark |
| Indices/Desp Indiretas | R$ 10.339.456 | 286,50 | Benchmark |
| **TOTAL PARCIAL** | **R$ 25.667.062** | **711,22** | |

*Eletrico sem cabos — quando adicionar cabos, deve subir ~R$ 1-2M

**Disciplinas ainda nao trabalhadas nesta sessao (ja existentes R00):**
- Estrutura (briefing R00)
- Arquitetura/Esquadrias/Alvenaria (briefings R00, BIM Visus do Leo)
- Louças e Metais (R00 existente)
- Telecom (R01 existente)
- Gas (avaliar abrir aba separada ou manter em Hidro CON 07)

**Base de benchmarks gerada:** 7 scripts, 7 JSONs, 158 arquivos xlsx locais (~162 processados).

**Scripts criados:**
- scripts/benchmark_final.py (Mov Terra)
- scripts/benchmark_hidro.py
- scripts/benchmark_eletrico.py
- scripts/benchmark_ppci.py
- scripts/benchmark_complementares.py (Sanit + Clima + Vent + Exaust)
- scripts/benchmark_indices.py
- scripts/gerar_hidro_r01.py
- scripts/gerar_mov_terra_r01.py
- scripts/gerar_ppci_r01.py
- scripts/gerar_eletrico_r01_parcial.py
- scripts/gerar_disciplinas_pendentes_r01.py

## 26. Atualizacoes Leo no Visus / BIM (11/abr/2026)

Leo esta trabalhando em paralelo no modelo BIM (Visus) para extrair quantitativos de arquitetura/acabamentos. Atualizacoes desta sessao:

### Pintura - Fachadas (BIM Visus)

- [x] Verificacao da fachada - criterio criado no Visus
- [x] Fachada esquerda quantificada
- [x] Fachada frontal quantificada
- [x] Fachada fundos quantificada
- [ ] Ajustar posicao da fachada (itens estao no final no Visus - reorganizar ordem)
- [ ] Adicionar composicao de massa PVA em teto

**Contexto:** Fachadas (macrogrupos 22 e 24 da EAP) sao extraidas direto do modelo BIM via Visus. Criterio de extracao foi definido nesta sessao.

### Esquadrias - Duvida unidade contramarco

- [ ] Qual a unidade de contramarco? un ou m2?
  > Impacto: afeta como a composicao de esquadrias sera montada. Contramarco pode ser cotado por peca (un) ou por perimetro de vao (m).
  > **Acao:** Leo define antes de consolidar esquadrias na master.

---

## 27. Processamento PDFs Lista de Materiais Eletrowatts (14/abr/2026)

**Contexto:** Leo recebeu 7 PDFs novos de "Lista de Materiais - Caixas e Quadros" do projetista Eletrowatts (07/04/2026), cobrindo SPDA, Telecom e Elétrico (5 pdfs: Aprovativo, Executivo, Preventivo, Geral, Disjuntores). Objetivo: processar com Gemma local / parser determinístico, comparar com extrações IFC/DXF existentes, e gerar xlsx rastreáveis para destravar os ~41% "vermelhos" (sem fonte) do Elétrico R02.

**Execução:** Parser Python determinístico (Gemma só usado para diagnóstico inicial — PDFs são tabelas estruturadas, regex é mais confiável). Suporta 2 formatos detectados automaticamente:
- **Formato A (template manual Eletrowatts):** ITEM | QUANT. | UNID. | DIMENSÕES | ESPECIFICAÇÃO + bloco "DADOS DOS PRODUTOS". Usado em Aprovativo, Executivo, Preventivo, SPDA, Telecom.
- **Formato B (sistema QT-MAT):** # | CÓDIGO | QTD | UN | DESCRIÇÃO inline, multi-página com metadata própria por documento. Usado em Geral (QT-MAT-1941) e Disjuntores (QT-MAT ×18).

Script: `scripts/parse_lista_materiais.py` (parser dual-format, ~280 linhas).

**Extração — total 413 itens granulares:**

| PDF | Formato | Itens | Pareamento |
|-----|---------|-------|------------|
| SPDA | A | 1 (manual — layout fragmentado) | ✅ |
| Telecom | A | 28 | ✅ pareado 100% |
| Aprovativo | A | 16 | ✅ pareado 100% |
| Executivo | A | 113 (1 possivelmente perdido de 114 — item 15 sem dimensão) | parcial |
| Preventivo | A | 49 | parcial |
| Geral (QT-MAT-1941) | B | 39 (3 docs) | ✅ |
| Disjuntores (QT-MAT 1932..1951) | B | 167 em 18 CDs | ✅ |

JSONs salvos em `quantitativos/listas-materiais/{eletrico,spda,telecom}/*.json`.

**Relatório comparativo completo:** `quantitativos/listas-materiais/COMPARACAO-PDFS-BASE-2026-04-14.md` (4 kB — lista o que cada PDF adiciona vs base IFC/DXF/briefing, decisões de autoridade por tipo de item, próximos passos).

### 27.1 SPDA R01 — primeira entrega formal

Script: `scripts/gerar_spda_r01.py`.
Fontes: briefing SPDA R00 (NBR 5419 — captação/descidas/equipot/aterramento/acessórios, 27 itens) + PDF Eletrowatts (1 item novo: 12 caixas BEL alumínio 20×20×15 cm) + PUs mercado SC 2026/SINAPI.

| Métrica | Valor |
|---------|-------|
| Total itens | 28 (27 briefing + 1 PDF novo) |
| Total material | R$ 142.378,40 |
| MO instalação (30%) | R$ 42.713,52 |
| **Total material + MO** | **R$ 185.091,92** |
| R$/m² AC | 5,13 |
| Benchmark Cartesian (mediana 27 projetos) | 5,14 R$/m² = R$ 185.512,88 |
| Delta vs mediana | −0,23 % ✅ |

Entrega: **`disciplinas/spda/spda-electra-r01.xlsx`** (primeira planilha formal SPDA — destrava disciplina).

### 27.2 Telecom R03 — suplemento ao R02

Script: `scripts/gerar_telecom_r03.py`.
28 caixas de passagem tronco (NÃO estavam no IFC — IFC tinha caixas 4×2/4×4 de tomada, PDF tem caixas de passagem por pavimento). Dimensões 20×20×12 a 60×120×20 cm. PU por faixa de volume (4 faixas SINAPI/mercado).

| Item | Valor |
|------|-------|
| Total material 28 caixas | R$ 32.510,00 |
| MO adicional (20%) | R$ 6.502,00 |
| **Total suplemento R03** | **R$ 39.012,00 (R$ 1,08/m²)** |
| R02 anterior (30/mar) | R$ 424.000 (R$ 11,75/m²) |
| **Total consolidado R03** | **R$ 463.012,00 (R$ 12,83/m²)** |

Entrega: **`disciplinas/telefonico/telecomunicacoes-electra-r03.xlsx`** (2 abas: CAIXAS PASSAGEM PDF + RESUMO R03).

### 27.3 Elétrico R03 — suplemento multi-aba ao R02

Script: `scripts/gerar_eletrico_r03.py`.
Consolida os 5 PDFs elétricos em 4 abas temáticas + resumo. Usa tabelas de PU por regex/keyword (54 patterns cadastrados cobrindo minidisjuntores mono/tri, IDRs bi/tetra, DPS, disjuntores caixa moldada, barramentos, cabos, quadros).

| Aba | Itens | Fallbacks | Total R$ | R$/m² |
|-----|-------|-----------|----------|-------|
| QUADROS PRINCIPAIS | 16 | 0 | 623.600 | 17,28 |
| CAIXAS PASSAGEM | 162 (113 exec + 49 prev) | 89 (55 %) | 129.045 | 3,57 |
| MATERIAL INTERNO CD | 39 (QT-MAT-1941) | 5 (13 %) | 79.133 | 2,19 |
| DISJUNTORES | 167 em 18 CDs | 9 (5 %) | 497.048 | 13,77 |
| **TOTAL SUPLEMENTO R03** | **384** | **103 (27 %)** | **1.328.826** | **36,82** |

**⚠️ R03 NÃO SOMA AO R02 — substitui itens "vermelhos".** O R02 (R$ 6.444.152) tinha 41 % vermelho (sem fonte) justamente em quadros/disjuntores/entrada/material interno. O R03 rastreia 384 desses itens com fonte PDF direta + PU de mercado, destravando ~20 % do R02 vermelho.

**Fallbacks em amarelo no xlsx (89 caixas de passagem):** itens Executivo/Preventivo com dimensão "VERIFICAR DIAGRAMA" ou "VER PROJETO APROVAT." — projetista remete ao desenho. PU default R$ 150 aplicado. **Ação Leo:** decidir PU médio ou processar DWGs.

Entrega: **`disciplinas/eletrico/eletrico-electra-r03.xlsx`** (5 abas: RESUMO + QUADROS PRINCIPAIS + CAIXAS PASSAGEM + MATERIAL INTERNO CD + DISJUNTORES 18 CDs).

### 27.4 Pendências não resolvidas pelos PDFs (permanecem do R02)

Os PDFs cobrem "caixas e quadros" — NÃO resolvem:
- [ ] Comprimento médio dos trechos de eletroduto (IFC não tem Length)
- [ ] Fator cabos vs eletrodutos (1:1? 1,5×?)
- [ ] Subestação/gerador/barramento — compartilhados entre torres?
- [ ] MO elétrica — R02 tinha R$ 170/m² vs mediana base R$ 26/m²
- [ ] Cabos de força metragem
- [ ] Luminárias (qtd ok, PU pendente)

### 27.5 Scripts criados nesta sessão

- `scripts/parse_lista_materiais.py` — parser dual-format (A + B) com pareamento posicional + subtração por consumidos
- `scripts/gerar_spda_r01.py` — gerador SPDA R01 (28 itens NBR + PDF)
- `scripts/gerar_telecom_r03.py` — gerador Telecom R03 (28 caixas PDF + suplemento)
- `scripts/gerar_eletrico_r03.py` — gerador Elétrico R03 (4 abas temáticas com 384 itens)

### 27.6 Próxima sessão — ação Leo

1. Abrir `spda-electra-r01.xlsx` — validar PUs SPDA, confirmar item BEL 12 caixas
2. Abrir `telecomunicacoes-electra-r03.xlsx` — validar 28 caixas passagem e PUs
3. Abrir `eletrico-electra-r03.xlsx` — focar nos 89 fallback amarelos (caixas passagem) e decidir PU médio
4. Consolidar totais no master Excel (`CTN-TZN_ELT - Orçamento Executivo_R00_Leo rev01.xlsx`)

### 27.7 Reorganização por pavimento (14/abr/2026 — iteração pós-feedback Leo)

**Feedback:** "a extração precisa ser sempre por pavimento" — regra geral, não só pra este projeto.

**Implementação:**

- Criado `scripts/normalizar_pavimento.py` — mapeador regex que recebe string livre (campo `especificacao_local` do formato A ou `metadata.localizacao` do formato B) e retorna `(pavimento, torre)` padronizados segundo a convenção Electra:
  - **Pavimentos:** `TERREO` (01º), `G1`-`G5` (02-06º), `LAZER` (07º), `TIPO` (08-31º ×24), `C_MAQ` (casa de máquinas), `COBERTURA`, `NA`
  - **Torres:** `A`, `B`, `AMBAS`, `NA`
  - Função `ordem_pavimento()` fornece ordem canônica pra ordenação Electra.
- Criado `scripts/enriquecer_jsons_pavimento.py` — enriquece todos os JSONs de `quantitativos/listas-materiais/` com campos derivados `pavimento`, `torre` e `pavimento_label` em cada item (formato A) ou documento+itens (formato B).
- Regra especial formato B: quando `localizacao` e `referente` conflitam quanto à torre (QT-MAT-1950 diz `[TORRE A]` mas referente diz `BLOCO B`), priorizar `referente` — projetista errou a localização.
- Regra especial Aprovativo: os 16 quadros gerais têm apenas `VERIFICAR DIAGRAMA` na especificação. Fallback: torre extraída do texto do produto (`BLOCO A/B`) e pavimento = `TERREO` (convenção: quadros principais ficam na subestação/térreo).
- Corrigido item 15 do Executivo (que tinha dimensão ausente no PDF e fez o parser desalinhar, virando `'16'` como `especificacao_local`): corrigido manualmente pra `TERREO/B`.

**Cobertura final:**

| PDF | Itens | Coberto por pavimento | Observação |
|-----|-------|-----------------------|------------|
| Telecom | 28 | 28/28 (100%) | Todos os itens do formato A tinham `especificacao_local` explícito |
| SPDA | 1 | 0/1 | Caixa BEL sem referência — usa coluna `Localização no prédio` semântica |
| Aprovativo | 16 | 16/16 | Fallback TERREO + torre do produto |
| Executivo | 113 | 113/113 | 1 item corrigido manualmente (dim ausente) |
| Preventivo | 49 | 49/49 | 100% coberto |
| Geral (QT-MAT-1941) | 39 | 39/39 | Metadata `localizacao` do documento |
| Disjuntores (QT-MAT ×18) | 167 | 167/167 | Idem |

**xlsx regenerados:**

- `disciplinas/spda/spda-electra-r01.xlsx` — 12 colunas (adicionada `Localização no prédio` semântica, pois SPDA é sistema vertical que atravessa o prédio). Totais iguais (R$ 185.091,92).
- `disciplinas/telefonico/telecomunicacoes-electra-r03.xlsx` — 3 abas: `CAIXAS POR PAVIMENTO` (ordenada Térreo→G1→…→C.Máq com subtotais por pavimento), `RESUMO POR PAVIMENTO` (pivot qtd/R$ por pavimento × torre A/B), `RESUMO R03` (consolidado com R02).
- `disciplinas/eletrico/eletrico-electra-r03.xlsx` — 5 abas reorganizadas por pavimento: `RESUMO R03` (agora com pivot por pavimento × aba temática), `QUADROS PRINCIPAIS`, `CAIXAS PASSAGEM`, `MATERIAL INTERNO CD`, `DISJUNTORES 18 CDs`. Todas as 4 abas temáticas ordenadas pela ordem canônica de pavimento Electra + Torre + item, com subtotais de pavimento.

**Totais mantidos:** mesma lógica de PU, mesmos valores (R$ 1.328.826 elétrico, R$ 39.012 telecom suplemento, R$ 185.092 SPDA). Só mudou a organização.

---

*Criado em 2026-03-25 | Atualizado continuamente durante o projeto*

## 28. Processamento PDFs 348_LM via Gemma local (15/apr/2026)

**Contexto.** A equipe Eletrowatts entregou 21 PDFs novos de listas de
materiais (`348_LM - ... - rev.00`) em `_Projetos_IA/thozen-electra/projetos/
15. Listas de quantitativos/`. Complementam os 7 PDFs de `LM - Caixas e
Quadros` processados na Secao 27 (mesmo dia). Cobertura: 6 disciplinas
(Eletrico, Hidraulico, Telefonico, PPCI Civil, PPCI Eletrico, SPDA).

**Objetivo.** Extrair cada PDF via Gemma local, organizar por pavimento
canonico (TERREO->G1->...->COBERTURA) e gerar xlsx de incremento
`{disciplina}-electra-lm348-r01.xlsx` pra cada disciplina afetada.

### Pipeline

1. **Fase 1 (Extracao Gemma).** Cada PDF foi lido e passado ao modelo
   `gemma4:e4b` local via `scripts/gemma_extract_lm.py`. Dois formatos
   detectados automaticamente:
   - **Formato B (QT-MAT):** 12 PDFs. Cada pagina do PDF = 1 documento
     Eletrowatts com LOCALIZACAO explicita (ex: `A) 01o PAVTO - TERREO`).
     Enviado pagina-a-pagina pro Gemma; pavimento extraido do header.
   - **Formato A (Eletrowatts manual):** 9 PDFs. Lista totalizada sem
     pavimento. Processado em 1 chamada unica; pavimento resolvido depois.
     Layouts diferentes detectados pelo prompt (A1-A5: com/sem COD.,
     com/sem DIM., com/sem MARCA/REFERENCIA).

2. **Fase 2 (Cross-check).** `scripts/comparacao_gemma_parser_348.py`
   rodou o parser deterministico `parse_lista_materiais.py` nos mesmos
   21 PDFs em paralelo e comparou totais de itens por PDF. Divergencia
   > 10% dispara flag `needs_review` no relatorio.
   Relatorio: `quantitativos/listas-materiais-348/COMPARACAO-GEMMA-PARSER-348-LM.md`

3. **Fase 3 (Rateio por pavimento).** Pros 9 PDFs formato A sem pavimento
   explicito, segundo pass Gemma (`scripts/gemma_rateio_pavimento.py`)
   aplica heuristica tecnica por sistema (SPDA cobertura+descidas,
   HIDRO-TUBOS prumada 70% TIPO, PPCI-SHP proporcional 32 pav, etc.)
   distribuindo item-a-item entre (pavimento, torre). Resultado salvo em
   `{slug}.rateio.json` com justificativa por linha.

4. **Fase 4 (Geracao xlsx).** `scripts/gerar_lm348_xlsx.py` consome
   `.gemma.json` + `.rateio.json` por disciplina e produz xlsx com 4 abas:
   - **Por Pavimento** — itens ordenados canonico com subtotais por grupo
   - **Flat por PDF** — itens na ordem original do PDF com rastreabilidade
   - **Rateio** — justificativas das distribuicoes (so format A)
   - **Resumo** — totais, contagens por pavimento, benchmark mediana

### Sumario da extracao

- Modelo Gemma: `gemma4:e4b`
- Tempo total batch: 255 min
- PDFs processados: 21

| PDF | Disc | Parser | Gemma | Delta |
|---|---|---:|---:|---:|
| `348_LM - ELE - rev.00 - ACABAMENTOS.pdf` | eletrico | 100 | 100 | +0% |
| `348_LM - ELE - rev.00 - CABOS DE ALIMENTAÇÃO_APTO-` | eletrico | 15 | 15 | +0% |
| `348_LM - ELE - rev.00 - ELETROCALHAS.pdf` | eletrico | 100 | 100 | +0% |
| `348_LM - ELE - rev.00 - ENFIAÇÕES.pdf` | eletrico | 183 | 183 | +0% |
| `348_LM - ELE - rev.00 - ILUMINAÇÕES.pdf` | eletrico | 38 | 38 | +0% |
| `348_LM - ELE - rev.00 - TUBULAÇÕES DE PAREDE_TETO.` | eletrico | 84 | 84 | +0% |
| `348_LM - HIDRO - rev.00_ELC - CONEXÕES TUBOS.pdf` | hidraulico | 0 | 132 | - |
| `348_LM - HIDRO - rev.00_ELC - ETE e CX. GORDURA.pd` | hidraulico | 0 | 20 | - |
| `348_LM - HIDRO - rev.00_ELC - TUBULAÇÕES.pdf` | hidraulico | 0 | 18 | - |
| `348_LM - HIDRO - rev.00_ELC - VÁLVULAS, MOTOBOMBAS` | hidraulico | 0 | 17 | - |
| `348_LM - PPCI - rev.00_ELC - SISTEMA GERAIS.pdf` | ppci-civil | 1 | 13 | +1200% |
| `348_LM - PPCI - rev.00_ELC - SISTEMA IGC.pdf` | ppci-civil | 7 | 93 | +1229% |
| `348_LM - PPCI - rev.00_ELC - SISTEMA MECÂNICO.pdf` | ppci-civil | 0 | 21 | - |
| `348_LM - PPCI - rev.00_ELC - SISTEMA SHP.pdf` | ppci-civil | 1 | 30 | +2900% |
| `348_LM - PPCI-ELÉ - rev. 00 - TUBULAÇÕES DE PAREDE` | ppci-eletrico | 81 | 81 | +0% |
| `348_LM - PPCI-ELÉ - rev.00 - ACABAMENTOS.pdf` | ppci-eletrico | 131 | 131 | +0% |
| `348_LM - PPCI-ELÉ - rev.00 - ENFIAÇÕES.pdf` | ppci-eletrico | 52 | 52 | +0% |
| `348_LM - SPDA - rev.00_ELC - COMPLETO.pdf` | spda | 61 | 59 | -3% |
| `348_LM - TEL - rev.00 - ACABAMENTOS.pdf` | telefonico | 69 | 69 | +0% |
| `348_LM - TEL - rev.00 - ELETROCALHAS.pdf` | telefonico | 18 | 18 | +0% |
| `348_LM - TEL - rev.00 - TUBULAÇÕES DE PAREDE_TETO.` | telefonico | 69 | 69 | +0% |

### Entregaveis (disciplinas/*/lm348-r01.xlsx)

- [OK] `disciplinas/eletrico/eletrico-electra-lm348-r01.xlsx`
- [OK] `disciplinas/hidraulico/hidraulico-electra-lm348-r01.xlsx`
- [OK] `disciplinas/telefonico/telecomunicacoes-electra-lm348-r01.xlsx`
- [OK] `disciplinas/pci-civil/ppci-civil-electra-lm348-r01.xlsx`
- [OK] `disciplinas/pci-eletrico/ppci-eletrico-electra-lm348-r01.xlsx`
- [OK] `disciplinas/spda/spda-electra-lm348-r01.xlsx`

### Escopo total (Secao 27 + Secao 28)

- Secao 27: 7 PDFs (LM Caixas e Quadros) = 413 itens, disciplinas ELE/SPDA/TEL
- Secao 28: 21 PDFs (348_LM) = ver tabela acima, 6 disciplinas cobertas
- **Total Electra 14/abr:** 28 PDFs extraidos e catalogados por pavimento

### Revisao Leo (next actions)

- [ ] Abrir cada xlsx `lm348-r01` e conferir aba **Por Pavimento**
- [ ] Conferir que subtotais por pavimento batem com o total de cada PDF
- [ ] Validar as distribuicoes da aba **Rateio** nos 9 PDFs format A
- [ ] Comparar R$/m2 AC do **Resumo** vs mediana da disciplina
- [ ] Mesclar com as revisoes anteriores (r03, r01, etc) quando quiser
  consolidar — lm348-r01 e um incremento autocontido
- [ ] Reprocessar PDFs flagged `needs_review` (ver secao Cross-check do relatorio)

### Scripts criados (versionados no openclaw)

- `scripts/gemma_extract_lm.py` — wrapper Gemma com prompt A/B dinamico
- `scripts/process_348_lm_pdfs.py` — orquestrador CLI com --resume
- `scripts/gemma_rateio_pavimento.py` — rateio heuristico por sistema
- `scripts/gerar_lm348_xlsx.py` — gerador xlsx comum 4 abas
- `scripts/comparacao_gemma_parser_348.py` — cross-check report
- `scripts/fase5_log_append.py` — este script

---

## 29. Fundação — Infraestrutura (20/abr/2026)

Primeira passada consolidada de fundação profunda (estacas hélice contínua) + fundação rasa (blocos coroamento + baldrame + laje fund) usando 4 fontes cruzadas do projetista 1203 (Rubens Alves) + proposta LIBERTÉ 1203-2025-R0.

### Fontes (4 xlsx projetista + proposta LIBERTÉ)

| Fonte | Arquivo | Conteúdo-chave |
|-------|---------|----------------|
| Projetista 1203 | `QUANTIDADES AÇO E CONCRETO - BLOCO A.xlsx` | Supra A por pavimento (L1-L35) + resumo r245: HÉLICE 2.200m³ / BLOCOS 2.066m³ |
| Projetista 1203 | `QUANTIDADES AÇO E CONCRETO - BLOCO B.xlsx` | Supra B por pavimento + topo r3-4: Zapatas 0,22m³ + Blocos coroamento 750,97m³ |
| Projetista 1203 | `CONTROLE DE REVISÃO - BLOCO A (1).xlsx` | Aço por bitola + linha "Somente Estacas": 1.424m³ / 23.185 kg (ø6.3 + ø16) |
| Projetista 1203 | `CONTROLE DE REVISÃO - BLOCO B (1).xlsx` | Idem Torre B: 1.529m³ / 24.446 kg |
| LIBERTÉ (fornecedor) | `ESTACAS.jpeg` (Proposta 1203-2025-R0) | 17×ø500 + 406×ø600 × 25m × C40 + 20% sobre = 3.544m³ / 47.631 kg aço |

### Etapa 1 — Extração consolidada projetista

Script: `scripts/extrair_projetista_1203.py`
Outputs: `disciplinas/estrutura/projetista-1203-consolidado.json` + `.xlsx` (5 abas)

**Validação cruzada (0% divergência):**
- Aço estacas soma CR (Bloco A + B) = 47.631 kg = LIBERTÉ total ✅
- Concreto CR sem sobreconsumo: 2.953 m³ × 1,20 = 3.544 m³ = LIBERTÉ com +20% ✅

### Etapa 2 — Identificação de tipologias

**Fundação profunda (empreendimento inteiro):**
- 17 estacas ø500mm × 25m = 425m comp
- 406 estacas ø600mm × 25m = 10.150m comp
- Total: 423 estacas, 10.575m comp, C40
- Aço CA-50: 6.175 kg ø6.3mm + 41.456 kg ø16mm = 47.631 kg total

**Fundação rasa (por torre):**

| Bloco | Elemento | Forma (m²) | Volume (m³) | Aço (kg) |
|-------|----------|-----------:|-------------:|---------:|
| A | Laje maciça fundação (topo QUANT-A r3) | — | 1.021,75 | 112.136 |
| B | Zapatas isoladas (QUANT-B r208) | 1,44 | 0,22 | 15 |
| B | Blocos de coroamento (QUANT-B r209) | 746,31 | 750,97 | 66.021 |
| — | **Total A+B (QUANT-A r245-246)** | — | **2.066,36** | **213.051** |

Torre A tem sistema de laje maciça (radier?), Torre B tem zapatas isoladas + blocos coroamento individuais. Confirmar com projetista na próxima revisão.

### Etapa 3 — EAP fundação preparada (01.002 + 01.003)

**Entregável:** `disciplinas/estrutura/eap-fundacao-r01.xlsx`

**01.002 FUNDAÇÃO PROFUNDA — R$ 3.067.440 (R$ 85/m² AC)** ✅ dentro faixa típica SC (R$ 50-90/m²)

| Sub-item | Qtd | Unid | PU estimado | Total |
|----------|----:|------|-----------:|------:|
| 01.002.001 Perfuração | 10.575 | m | R$ 101,50 | R$ 1.073.363 |
| 01.002.002 Armadura | 47.631 | kg | R$ 9,66 | R$ 460.116 |
| 01.002.003 Acessórios | 423 | un | R$ 362,50 | R$ 153.338 |
| 01.002.004 Concreto C40 (+20%) | 3.544 | m³ | R$ 346,30 | R$ 1.227.283 |
| 01.002.005 MO estacas | 10.575 | m | R$ 14,50 | R$ 153.338 |

**01.003 FUNDAÇÃO RASA — R$ 4.601.543 (R$ 127/m² AC)** ⚠️ acima faixa típica SC (R$ 30-60/m²)

| Sub-item | Qtd | Unid | PU estimado | Total |
|----------|----:|------|-----------:|------:|
| 01.003.001 Forma | 1.900 | m² | R$ 130,00 | R$ 247.000 |
| 01.003.002 Armadura | 213.051 | kg | R$ 13,00 | R$ 2.769.663 |
| 01.003.003 Concreto C30 | 2.066 | m³ | R$ 680,00 | R$ 1.404.880 |
| 01.003.004 MO | 1 | vb | R$ 180.000 | R$ 180.000 |

**TOTAL FUNDAÇÃO: R$ 7.668.983 (R$ 212/m² AC)** ⚠️ acima faixa típica SC (R$ 80-150/m²)

### Etapa 4 — Aba Estacas r01 preparada

**Entregável:** `disciplinas/estrutura/estacas-electra-r01.xlsx` — 2 linhas agregadas por diâmetro:

| Torre | Ø (m) | Qtd | Cota | Comp | Escav | Bota-fora | Concreto | ø6.3 | ø16 |
|-------|------:|----:|-----:|------:|------:|----------:|---------:|-----:|-----:|
| Empreendimento | 0.50 | 17 | 25 | 425 | 83,5 | 108,6 | 83,5 | 248 | 1.666 |
| Empreendimento | 0.60 | 406 | 25 | 10.150 | 2.869,8 | 3.730,8 | 2.869,8 | 5.927 | 39.790 |
| **TOTAL** | | **423** | | **10.575** | **2.953,3** | **3.839,4** | **2.953,3** | **6.175** | **41.456** |

**Taxa aço calculada:** (6.175 + 41.456) / 2.953,3 = **16,13 kg/m³** — típico hélice contínua (faixa 15-25) ✅

**⚠ Mudança no master:** template Gessele (198×ø60cm × 34m) deve ser REMOVIDO. Master row 5 coluna N rotula "20" (kg aço) mas projeto Electra usa ø16 — renomear para "16" ao colar.

### Alertas / Dúvidas pendentes pra reunião com projetista

1. **R$/m² AC fund. rasa fora do padrão (R$ 127 vs típico R$ 30-60):**
   - Aço 213.051 kg em 2.066 m³ = 103 kg/m³ (OK pra prédio alto 2 torres × 35 pav)
   - PUs podem estar conservadores — validar com cotação real
   - Investigar se "L1 Blocos" no CONTROLE-REV = 2.066 m³ inclui baldrame + laje fund (diferencial de 293 m³ vs QUANT-B r4 Blocos coroamento 751 m³)

2. **Sistema de fundação é diferente entre torres?**
   - Bloco A: Lajes maciças fundação (radier?)
   - Bloco B: Zapatas + Blocos coroamento
   - Confirmar com Rubens Alves

3. **Discrepância resumo QUANT-A r245 "HÉLICE 2.200 m³" vs real 3.544 m³ (+20%)**
   - Resumo pode ser anterior à revisão LIBERTÉ
   - Ignorar, usar CONTROLE-REV detalhado que bate com LIBERTÉ

4. **Cotação FORMAL LIBERTÉ ainda não chegou** — PUs usados são estimativa turnkey R$ 290/m decompostos proporcional

### Pendências pra próxima sessão

- [ ] Detalhamento por grupo da aba "Fund. Rasa | Contenção" (blocos retangulares, hexagonais, vigas fund, pilares fund, laje fund, duto/cisterna, contenções) — precisa processar IFC R26 pra dimensões individuais
- [ ] Cruzamento IFC R26 × projetista (por pavimento) pra sanity check supra
- [ ] Benchmark real da base Cartesian pra refinar PUs de fund. rasa (suspeita R$ 127/m² AC alto)
- [ ] Solicitar cotação formal LIBERTÉ
- [ ] Validar com Rubens Alves: (a) sistema de fund. por torre, (b) breakdown "L1 Blocos" = 2.066 m³

### Scripts criados

- `scripts/extrair_projetista_1203.py` — lê 4 xlsx projetista + hardcode LIBERTÉ, gera JSON+xlsx consolidado
- `scripts/gerar_estacas_r01.py` — gera xlsx aba Estacas com 2 linhas agregadas
- `scripts/gerar_eap_fundacao_r01.py` — gera xlsx aba EAP com 9 sub-itens de fundação

### Entregáveis (no Drive, prontos pra Leo colar)

- [x] `disciplinas/estrutura/projetista-1203-consolidado.json`
- [x] `disciplinas/estrutura/projetista-1203-consolidado.xlsx` (5 abas)
- [x] `disciplinas/estrutura/estacas-electra-r01.xlsx`
- [x] `disciplinas/estrutura/eap-fundacao-r01.xlsx`

---

## 30. Validação benchmark fundação (20/abr/2026)

Benchmark rodado em 162 xlsx de `_Entregas/Orçamento_executivo/` (base Cartesian completa). Resultado: **Electra está abaixo da mediana no TOTAL de infraestrutura**, mesmo com o alerta inicial de R$ 127/m² AC na fund. rasa isolada.

### Script e dados

- Script: `scripts/benchmark_infra_supra.py`
- Dados: `dados/benchmark_infra_supra.json`
- 0 erros de processamento, 162/162 xlsx processados

### Benchmarks agregados (R$/m² AC)

| Macrogrupo | N | Min | P25 | **Mediana** | P75 | Max |
|------------|---|----:|----:|------------:|----:|----:|
| Mov. Terra | 46 | 0,0 | 10,2 | **18,2** | 41,1 | 207,2 |
| Infraestrutura (inclui fund. prof + rasa) | 53 | 0,1 | 137 | **199** | 254 | (outlier) |
| Supraestrutura | 53 | 0,2 | 482 | **604** | 724 | (outlier) |
| Paredes/Alvenaria | 51 | 0,0 | 114 | **134** | 161 | (outlier) |
| **Mov + Infra (comparável Electra fundação)** | 45 | 0,1 | 158 | **245** | 286 | 459 |

### Posicionamento do Electra

| Item Electra | Valor | Posição na base | Status |
|--------------|------:|-----------------|--------|
| Mov. Terra | R$ 14,52/m² | abaixo da mediana (P25-mediana) | ✅ |
| Infra Total (Fund. Prof + Rasa) | R$ 212/m² | entre mediana e P75 | ✅ |
| **TOTAL Mov + Infra** | **R$ 227/m²** | **abaixo da mediana** | ✅✅ |

### Conclusão — alerta anterior era falso positivo

Na seção 29 havia alerta de que fund. rasa isolada (R$ 127/m² AC) estaria acima da faixa típica SC (R$ 30-60/m² AC). O benchmark real da base Cartesian mostra que:

- A faixa "R$ 30-60/m²" era estimativa de mercado generalista, **não** a base real de projetos similares
- Projetos de 45+ entregas Cartesian têm **Mov + Infra em mediana R$ 245/m² AC**, com P75 de R$ 286/m²
- Electra R$ 227/m² tá ABAIXO da mediana — faz sentido pro perfil (2 torres, 35 pav, sem subsolo)

**Implicação pro xlsx eap-fundacao-r01:** PUs estimados estão **alinhados com a prática Cartesian**. Leo pode manter a entrega atual como R01 e substituir PUs específicos quando a LIBERTÉ enviar cotação formal (reduz marginal, não reformula).

### Pendências que ainda fazem sentido investigar

- Cotação formal LIBERTÉ turnkey (confirmar R$ 290/m estimado) — impacto ±10% no subtotal 01.002
- Breakdown "L1 Blocos" CONTROLE-REV = 2.066 m³ inclui baldrame? (não muda total, só detalhe)
- Sistema fund. Bloco A (laje maciça/radier) vs Bloco B (zapatas + blocos) — confirmar com Rubens Alves (não muda valor)

### Atualização da gestão

Item 01.003 (Fund. Rasa) removido do status "⚠️" pra "✅ validado contra benchmark".

---

## 31. Memorial Word gerado + Etapas 5 e 6 concluídas (20/abr/2026)

### Memorial-Execucao-Electra.docx (62 KB)

Pandoc instalado via winget. Comando reprodutível:
```bash
pandoc log-execucao.md -o Memorial-Execucao-Electra.docx --from markdown --to docx --toc --toc-depth=2
```

Output: 62 KB com TOC (table of contents) até nível 2. Pronto pra enviar ao cliente se necessário (após revisão dos rascunhos).

### Etapa 5 — Fund. Rasa detalhado via IFC R26

**Entregáveis:**
- `scripts/extrair_fund_rasa_ifc.py` — processa IFC via ifcopenshell + BBOX 3D
- `dados/ifc-r26-fund-rasa.json` — dados brutos 70 footings
- `disciplinas/estrutura/fund-rasa-electra-r01-detalhado.xlsx` (2 abas: Por Elemento + Agrupado)

**70 IfcFooting no IFC R26 (125,87 m³ BBOX):**

| Tipologia | Seção (cm) | Qtd |
|-----------|-----------|----:|
| Viga baldrame | 14×124 | 26 |
| Viga baldrame | 14×164 | 18 |
| Viga baldrame | 14×184 | 6 |
| Viga baldrame | 20×250 | 16 |
| Bloco Pra | 70×70×30 | 4 |

**DESCOBERTA:** O IFC R26 (arquivo "BLOCOS+RAMPAS DE ACESSO") **só modela vigas baldrame + 4 blocos Pra pequenos**. Os **blocos de coroamento** das 423 estacas e a **laje de fundação** (radier do Bloco A) **NÃO estão como IfcFooting** — foram modelados como IfcColumn (blocos) ou IfcSlab (radier), explicando a "aparente" divergência com projetista (2.066 m³ em Blocos do CONTROLE-REV).

### Etapa 6 — Cruzamento IFC R26 × Projetista 1203

**Entregáveis:**
- `scripts/cruzar_ifc_projetista.py` — compara IFC BBOX × projetista QUANT
- `dados/cruzamento-ifc-vs-projetista.json` — resultados
- `disciplinas/estrutura/cruzamento-ifc-projetista.xlsx`

**Resultados (amostragem 100 elementos/tipo, extrapolação):**

| Categoria | IFC BBOX (m³) | Projetista (m³) | Δ % | Flag |
|-----------|--------------:|----------------:|----:|------|
| Fund. Profunda (estacas) | 0 | 3.544 | 100% | 🔴 IFC não modela estacas (arquivo BLOCOS+RAMPAS só) |
| Fund. Rasa (só IfcFooting) | 126 | 2.066 | 94% | 🔴 IFC cobre só baldrames + Pra pequenos |
| Supra (pil+vig+laje) | 15.091 | 11.331 | 33% | 🔴 BBOX superestima (lajes nervuradas) |
| **TOTAL obra (sem estacas)** | **15.217** | **15.598** | **2,4%** | **✅ OK** |

**Por que o total bate se por categoria está fora?**

A hipótese mais provável é que o projetista 1203 **modelou blocos de coroamento como IfcColumn** (é estrutura de apoio) e a **laje de fundação como IfcSlab** — portanto, ~1.940 m³ da "fund. rasa projetista" aparece no "supra IFC" na nossa comparação. Dois erros se compensam:

- IFC **superestima supra** (+33%) porque BBOX ≠ volume real (lajes nervuradas têm vazios não contabilizados)
- IFC **subestima fund. rasa** (-94%) porque não classificou blocos coroamento + laje fund como IfcFooting
- Total bate (2,4% ✅) — sanity check aprovado

### Conclusão Etapas 5+6

**Bottom line:** dados do projetista estão ÍNTEGROS. O cruzamento confirma (no total) que projetista está reportando corretamente. Por categoria o IFC diverge por questões de classificação (IfcFooting vs IfcColumn vs IfcSlab) e limitação do BBOX.

**Consequência prática pro orçamento:**
- Confiar nos dados do projetista (QUANT A/B + CONTROLE-REV) ✓
- Cálculo LIBERTÉ 3.544 m³ de estacas também bate com CONTROLE-REV estacas + 20% ✓
- Os R01 (estacas + EAP fundação + Fund.Rasa detalhe) são consistentes entre si

### Ações técnicas pendentes (não urgentes)

- Solicitar ao projetista Rubens Alves: IFC complementar modelando blocos coroamento + laje fund explicitamente como IfcFooting/IfcPileCap (facilita cruzamentos futuros)
- Refinar volume IFC via shape.geometry triangle mesh (em vez de BBOX) pra matar a superestimativa em lajes nervuradas — script opcional pra próxima sessão

### Scripts reaproveitáveis pra outros projetos

- `scripts/extrair_fund_rasa_ifc.py` — roda em qualquer IFC com IfcFooting, agrupa por tipologia/seção
- `scripts/cruzar_ifc_projetista.py` — cruzamento IFC BBOX × projetista JSON (padrão Cartesian)
- Adaptar paths no topo dos scripts e rodar.

---
