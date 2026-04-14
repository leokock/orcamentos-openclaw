# Sessão 2026-04-14 — Revisão dos 3 pacotes + Fases 14, 16, 17, 18, 18b

_Sessão longa cobrindo: Gemma sobre observações completas, quantitativos físicos BIM/DXF/PDF, memoriais de extração, revisão profunda dos 3 pacotes reais (arthen, placon, thozen), fix arquitetural do calibrado vs itens, e classificação semântica de padrão de 126 projetos via Gemma._

## Contexto inicial

Base V2 já tinha 126 projetos entregues com índices numéricos (R$/m² por macrogrupo, 4.210 PUs cross-projeto, 29 índices derivados), mas os 3 pacotes reais (arthen-arboris, placon-arminio-tavares, thozen-electra) precisavam de revisão profunda antes de virarem entregáveis finais. Objetivo da sessão: achar todas as incoerências, corrigir, e entregar versão final rastreável.

## Fase 14 — Gemma sobre observações completas (conclusão)

Rodada final de Gemma sobre `comentarios-completos/[projeto].json` (texto livre dentro das células do xlsx, capturado na Fase 8 via `openpyxl.cell.comment`).

**Output:** `base/observacoes-insights/{slug}.json` — 126 arquivos, 824 KB total.

| Métrica | Total | Média/projeto |
|---|---|---|
| Temas extraídos | 883 | 7,0 |
| Justificativas técnicas | 646 | 5,1 |
| Flags de risco | 179 | 1,4 |

**Duração:** 170 min (10.206 s) com `gemma4:e4b` local.

Esta camada explica **por que** itens fugiram da mediana — é a fonte primária pra revisão de novos orçamentos contra a base.

## Fase 16 — Quantitativos físicos (BIM + DXF + PDF)

Pipeline novo que extrai quantitativos físicos diretamente do projeto, independente do orçamento. Permite cross-validar o memorial executivo.

### 16a — BIM v2 via geometric bounding box

**Problema descoberto:** IFCs dos 3 projetos vinham com `Pset_QuantityTakeOff` vazio (ninguém populou QTOs na modelagem). Primeira extração retornou 0 m², 0 m³.

**Solução:** trocar pra `ifcopenshell.geom.create_shape` com `disable-opening-subtractions`. Calcula bounding box 3D de cada elemento IFC — **~3ms por elemento**, independente de QTOs existirem.

**Script:** [scripts/extract_quantitativos_bim_v2.py](scripts/extract_quantitativos_bim_v2.py)

Captura: IfcWall, IfcSlab, IfcBeam, IfcColumn, IfcDoor, IfcWindow, IfcSpace, IfcCurtainWall, IfcRailing, IfcRoof, IfcCovering.

### 16b — DXF via ezdxf

**Script:** [scripts/extract_quantitativos_dxf.py](scripts/extract_quantitativos_dxf.py)

Extrai TEXT/MTEXT, layers, entity counts, flags de lazer (piscina, sauna, gourmet, fitness, etc). Thozen: **21 DXFs processados em 1.147 s**.

### 16c — PDF via pypdf

**Script:** [scripts/extract_quantitativos_pdf.py](scripts/extract_quantitativos_pdf.py)

Lê memoriais, quadros NBR 12.721, especificações. Extrai áreas, unidades, m³, kg, pavimentos. Placon: **14 PDFs relevantes lidos**.

### 16d — Consolidação

**Script:** [scripts/consolidar_quantitativos.py](scripts/consolidar_quantitativos.py)

Merge BIM + DXF + PDF + `state.json` do pacote → `base/quantitativos-consolidados/{slug}.json`.

## Fase 17 — Memoriais de extração

**Script:** [scripts/gerar_memorial_extracao.py](scripts/gerar_memorial_extracao.py)

Consolida tudo (BIM + DXF + PDF) num memorial rastreável por projeto, cross-referenciando cada quantitativo contra os 4.210 PUs cross-projeto + 29 índices derivados.

**Output:** 3 arquivos `base/pacotes/{slug}/memorial-extracao-{slug}.md` com 375-425 linhas cada.

Exemplo arthen: "6.387 paredes × 36.213 m² alvenaria bloco cerâmico 14cm, 10.746 reboco × 60.096 m²".

## Revisão dos 3 pacotes (via 3 subagents paralelos)

Dispatch de 3 review agents (general-purpose, read-only) em paralelo pra análise profunda. Cada um recebeu state.json, audit-v2, revisao-pus-cross, memorial-extracao, quantitativos-consolidados e a base V2 pra benchmarks.

### Achado crítico comum aos 3 (defeito arquitetural)

**O total apresentado no RESUMO era calibração V2 (R$/m² × AC), NÃO soma dos itens detalhados.** As abas com itens eram amostras cross-projeto — não somavam ao total. Cliente abria o xlsx, somava a coluna, e o número não batia com o RESUMO.

| Projeto | RESUMO total | Soma real itens | Cobertura |
|---|---|---|---|
| arthen-arboris | R$ 36,5M | R$ 10,6M | **29%** |
| placon-arminio-tavares | R$ 12,2M | R$ 7,1M | **58%** |
| thozen-electra | R$ 137,5M | 4-224% variável | **incoerente** |

Causa raiz: `gerar_executivo_auto.py:376` chamava `valores_macrogrupos_calibrados()` pra compor RESUMO, mas só populava abas com `itens_referencia_top10` cross-projeto. Os dois mundos nunca conversavam.

### Outros achados críticos

- **Bugs do audit-v2 não aplicados:** Placon chapisco R$ 6,31 (P50=R$ 0,56), fechamento elevador R$ 3.829, Ar-Cond qty=32.094; Thozen Acabamento de Registro R$ 494 (P50=R$ 50), 6 garbage rows em Sistemas Especiais, encoding broken (Climatiza��o); Arthen Tubo Aço Galv Ø65 R$ 107, Climatização BTU-agnóstica R$ 39,88.
- **BIM cross-check divergente:** Arthen BIM 8.654 m³ concreto vs orçamento 50,86 m³ (-99%); Thozen Torre B perdida no BIM; Placon IfcSlab contaminado com "VISTAS FORRO".
- **Sistemas Especiais = null** em `calibration-indices.json` — caía no fallback `valores_similares` n=1 (Arthen usou 1 projeto único = frágil).
- **Macrogrupos vazios:** Imprevistos nos 3, Climatização thozen 0 itens.

## Decisões arquiteturais (Leo validou)

### Decisão A — Escopo mantido: paramétrico + preliminar calibrado

**Não** transformar o preliminar em executivo verdadeiro (somando itens). Isso exigiria preencher quantitativos do BIM por item — demorado e arriscado. Em vez disso:

- **Paramétrico:** R$/m² × AC por macrogrupo + P10/P50/P90 + fonte/confiança
- **Preliminar:** mesmo paramétrico + lista de itens-referência cross-projeto + cobertura % explícita por MG
- **Disclaimer em todo RESUMO:** "Total = calibração V2. Itens são referência cross-projeto, não somam ao total."

### Decisão B — Revisão de padrões

- **arthen-arboris:** medio → **medio-alto** (BIM mostrou concreto 0,694 m³/m² = +104% sobre mediana)
- **placon-arminio-tavares:** mantém **medio** (74 m²/UR confirma)
- **thozen-electra:** mantém **alto**

### Decisão C — Macrogrupos vazios preenchidos via calibração

Imprevistos nos 3, Climatização thozen completados via valores calibrados V2 (antes ficavam zerados).

### Decisão 4 — Placon AC corrigido

4.077,29 → 4.089,72 m² (valor oficial do Quadro NBR 12.721 do PDF).

### Decisão 5 — Arthen R$ 35,08M vs R$ 36,47M (investigação)

Gap investigado e explicado: **R$ 1.384.514 = Sistemas Especiais** que caía no fallback `valores_similares` n=1 (1 único projeto similar) porque o macrogrupo era null em `calibration-indices.json`. Paramétrico pulava, executivo incluía. Fix: popular Sistemas Especiais na calibration.

## Correções aplicadas aos scripts

### 1. Sistemas Especiais populado em calibration-indices.json

Agregado de 59 projetos filtrados (filtro 30-800 R$/m²): **mediana R$ 163/m²**, n=59.

### 2. `aba_resumo` + `aba_macrogrupo` — disclaimer + cobertura %

Nova coluna **Σ itens** + **Cobertura %** por macrogrupo. Disclaimer no A3 em vermelho. Row de totais mostra soma real dos itens e cobertura global.

### 3. `enriquecer_executivo` — filtros de saneamento

- Descrição puramente numérica (garbage rows thozen)
- Quantidade absurda (>10.000 pra un não-m²/kg) — pega o bug "Ar Condicionado qty=32.094"
- Unidade de descrição isolada com dígitos

### 4. PU sanity filter via cross-check 4.210 clusters

Nova função `_sanity_filter_pus()` em `consulta_similares.py`. Cross-check contra `base/itens-pus-agregados.json`:
- Tokenize descrição, match contra cluster keys (overlap ≥2 tokens)
- Se `pu_ratio > 3x` ou `< 0.33x` e `freq_projetos < 3` → substitui pela mediana do cluster
- Flag `_pu_substituido: true` pra transparência

Resolve os bugs PU do audit-v2 sem hardcode.

### 5. Encoding dos nomes de aba

`titulo = mg.replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("õ", "o")[:25]` em `gerar_executivo_auto.py:236`. Elimina Climatiza��o, Lou�as, Movimenta��o broken.

### 6. Renomeação executivo → preliminar

`executivo-{slug}.{xlsx,docx,pdf}` → `preliminar-{slug}.*` em `gerar_pacote.py`. Arquivos antigos movidos para `base/pacotes/{slug}/_antigo-executivo/`.

## Fase 18 — Classificação semântica de padrão via Gemma

### Problema do proxy anterior

Primeira versão da calibração-condicional usou **bucket rsm2 total** (quartis de R$/m²) como proxy de padrão. Circular: estávamos calibrando R$/m² a partir de buckets de R$/m².

### Sinais disponíveis (análise)

Identificamos 12 sinais possíveis: itens de acabamento fino (porcelanato 120×120, mármore, ACM), R$/m² por disciplina, m²/UR, R$/UR, flags de assinatura (piscina aquecida, gerador, spa, etc), tipologia Gemma PDF, observações fase 14.

Tipologia Gemma era texto livre inútil ("15 pavimentos, 2 subsolos, studios com ofurô") — 47/126 projetos e zero valor classificatório.

### Estratégia escolhida

**Classificador Gemma full para todos os 126** (Leo preferiu qualidade sobre velocidade com modelo local). Rubric canônica de 5 classes (economico/medio/medio-alto/alto/luxo) com critérios explícitos. Input por projeto: top 30 itens de Pisos/Esquadrias/Louças/Fachada/SE + flags de assinatura + métricas numéricas.

### Script

[scripts/classificar_padrao_gemma.py](scripts/classificar_padrao_gemma.py):
- `coletar_sinais()`: 2 estratégias de extração (aba-name + fallback por descrição regex)
- `build_prompt()`: rubric + sinais estruturados
- `call_gemma()`: Ollama HTTP API com `format: json` (garante output estruturado, elimina truncamento)
- Fila retomável `base/phase18-queue.json`
- Output por projeto em `base/padroes-classificados/{slug}.json`

### Iteração (exemplo de modo autônomo)

**Rodada 1** — 126/126 em ~20 min. Distribuição suspeita: 32 "economico baixa confiança" (zero alta/média). Investigação: **TODOS com n_top=0**, ou seja, extração vazia.

**Raiz:** 84 projetos estavam em formato diferente de xlsx (Sienge EAP, ABC_INSUMOS, ABC_SERVIÇOS, "Relatório" único) — nomes de aba não matchavam meu regex de keywords.

**Fix autônomo:** adicionei `ITEM_DESC_PATTERNS` — regex por descrição de item (porcelanato, esquadria, torneira, ACM, piscina etc) como fallback. Prioridade: esquadrias > louças > fachada > SE > pisos (pisos matcharia "madeira" antes de esquadrias).

**Rodada 2** — reprocessei os 84 projetos com o fallback. Recuperou 52-75 itens por projeto.

### Distribuição final

| Classe | n | Conf alta | Conf média | Conf baixa |
|---|---|---|---|---|
| economico | 4 | 0 | 0 | 4 (dados genuinamente pobres) |
| medio | 4 | 0 | 3 | 1 |
| **medio-alto** | **60** | 27 | 28 | 5 |
| **alto** | **57** | **50** | 7 | 0 |
| luxo | **0** | — | — | — |
| insuficiente | 1 | — | — | — |

**125/126 via Gemma semântico, 94% alta/média confiança.**

### Sanity R$/m² por classe (monotônico ✓)

- economico median R$ 1.983 | medio 2.534 | medio-alto 3.482 | alto 4.345 | luxo —

### Comparação Gemma vs rsm2_bucket anterior

- Concordam: 20 | **Gemma > bucket: 29** (extração rsm2 subestimava) | Gemma < bucket: 16 | Sem rsm2: 60

Os 60 sem rsm2 pra comparar confirmam o valor da Fase 18: projetos que não tinham R$/m² extraído foram classificados pelo Gemma via materiais.

### Zero luxo

Decisão B de Leo: aceitar. Cartesian não tem luxo-luxo na base (casa Alphaville). O que chama "alto" na base é o topo real dos empreendimentos residenciais.

## Fase 18b — Calibração condicional baseada em labels Gemma

### Script

[scripts/build_calibration_gemma.py](scripts/build_calibration_gemma.py) — agrega medianas por-macrogrupo de cada classe usando os labels Gemma reais cruzados com `indices-executivo` com `ac+total > 0`.

### Nova calibration-condicional-padrao.json

| Classe | n | Total R$/m² | MGs cobertos |
|---|---|---|---|
| economico | 3 | 1.767 | 13/18 (dados esparsos → fallback global) |
| medio | 2 | 2.467 | 15/18 (dados esparsos → fallback global) |
| **medio-alto** | **37** | **3.349** | **18/18 ✅** |
| **alto** | **23** | **4.156** | **18/18 ✅** |
| luxo | 0 | — | — |

`valores_macrogrupos_calibrados()` em `consulta_similares.py` consulta condicional primeiro, fallback pra global × `PADRAO_MULTIPLIERS` quando n<3 no bucket.

## Totais finais dos 3 pacotes

| Projeto | AC | UR | Padrão | Total | R$/m² | Δ vs início sessão |
|---|---|---|---|---|---|---|
| **arthen-arboris** | 12.473 | 98 | medio-alto | **R$ 41,77M** | 3.349 | +14,5% (partida 36,47M) |
| **placon-arminio-tavares** | 4.090 | 55 | medio | **R$ 12,17M** | 2.976 | +0% (ajuste AC) |
| **thozen-electra** | 37.894 | 348 | alto | **R$ 157,48M** | 4.156 | +14,5% (partida 137,52M) |

Total conjunto: **R$ 211,42M** (vs R$ 186,17M no início).

## Entregas por projeto

Em `base/pacotes/{slug}/`:
- `parametrico-{slug}.{xlsx,docx,pdf}` — R$/m² por macrogrupo com P10/P50/P90
- `preliminar-{slug}.{xlsx,docx,pdf}` — idem + 30 itens-referência por MG + cobertura %
- `memorial-extracao-{slug}.md` — quantitativos BIM/DXF/PDF cross-ref a 4.210 PUs
- `_antigo-executivo/` — versão anterior arquivada (audit + executivo antigo)

## Scripts novos criados nessa sessão

| Script | Fase | Propósito |
|---|---|---|
| `extract_quantitativos_bim_v2.py` | 16a | BIM via geometric bbox |
| `extract_quantitativos_dxf.py` | 16b | DXF via ezdxf |
| `extract_quantitativos_pdf.py` | 16c | PDF via pypdf |
| `consolidar_quantitativos.py` | 16d | Merge BIM+DXF+PDF |
| `gerar_memorial_extracao.py` | 17 | Memorial cross-ref |
| `classificar_padrao_gemma.py` | 18 | Classificação semântica |
| `build_calibration_gemma.py` | 18b | Calibração condicional |

## Scripts modificados

- `consulta_similares.py` — PU sanity filter + calibração condicional + garbage filter
- `gerar_executivo_auto.py` — aba_resumo com disclaimer/cobertura, aba_macrogrupo com soma itens, encoding fix
- `gerar_pacote.py` — rename executivo → preliminar

## Arquivos de base novos

- `base/observacoes-insights/*.json` — 126 (Fase 14)
- `base/quantitativos-bim/*.json` — 3 (Fase 16a)
- `base/quantitativos-dxf/*.json` — 1 (thozen)
- `base/quantitativos-pdf/*.json` — 1 (placon)
- `base/quantitativos-consolidados/*.json` — 3
- `base/padroes-classificados/*.json` — 126 (Fase 18)
- `base/padroes-classificados-consolidado.json` (Fase 18)
- `base/calibration-condicional-padrao.json` (Fase 18b)
- `base/itens-pus-agregados.json` — 4.210 clusters (usado pelo PU sanity filter)
- Updated: `base/calibration-indices.json` — populado Sist.Especiais (antes null)

## Processo de trabalho (modo autônomo)

Esta sessão estabeleceu o padrão de modo autônomo com modelo local:

- **Pipeline longo overnight** disparado e iterado sem pausa a cada passo
- **Bugs descobertos e corrigidos** sem checkpoint humano (encoding, garbage rows, PU anômalos, Sistemas Especiais null)
- **Re-processamento** quando descoberto insight (84 projetos com n_top=0 → fallback regex → rodada 2) sem pedir permissão
- **Checkpoints humanos apenas em decisões arquiteturais grandes**: Decisão A (escopo), Decisão B (rubric luxo), Decisão C (opção Gemma full vs híbrido)

Leo validou essa abordagem como padrão pra todo trabalho futuro com Gemma local. Ver memória `feedback_modo_autonomo_gemma_local.md`.

## Commits da sessão

1. `598b6b6` — Fase 14 (observações Gemma 126), Fase 16 (quantitativos), Fase 17 (memoriais)
2. `4905311` — Revisão 3 pacotes: calibração condicional rsm2-bucket + preliminar
3. `70a9f4b` — Fase 18: classificação Gemma de 126 projetos
4. `105a277` — Fase 18b: calibração Gemma labels + regerar 3 pacotes
5. `37ac040` / `1fefe3f` — Documentação das fases 14/16/17/18/18b (orcamentos + openclaw)
6. `756e050` — Fase 19: Paramétrico V2 Híbrido (override manual) + 3 pacotes regerados

## Fase 19 — Paramétrico V2 Híbrido (dropdown + override manual)

Após validar os 3 paramétricos gerados pelo `gerar_template_dinamico_v2.py`, Leo pediu uma evolução: permitir que o orçamentista sobrescreva **diretamente** qualquer índice da aba `INDICES` durante reunião com cliente, sem precisar mexer em fórmulas. O modelo anterior só permitia ajuste indireto via 14 dropdowns do BRIEFING.

### Arquitetura híbrida

Nova aba `INDICES` com 6 colunas:

| Col | Campo | Editável |
|---|---|---|
| A | Nome do índice | não |
| **B** | Valor calculado (fórmula IF do BRIEFING) | não (mantém lógica reativa) |
| **C** | **Override manual** | **sim** (vazio por default, input laranja) |
| **D** | Valor efetivo `=IF(C="",B,C)` | não (calculado — consumido pelas abas) |
| E | Unidade | não |
| F | Fonte + nota | não |

**77 referências** `INDICES!B{n}` nas abas de detalhe substituídas por `INDICES!D{n}` via replace mecânico (protegendo a aba INDICES própria, que mantém self-references em B).

### 3 novos índices overridable (antes embutidos em fórmulas)

- **Row 33:** Fator viga protendida (0.08 vs 0.30)
- **Row 34:** Fator laje protendida (0.60 vs 0.35)
- **Row 35:** Fator hidro BWC (1.15 vs 1.0)

Antes eram hardcoded em `IF(BRIEFING!B4="Protendida",...)` dentro das abas de macrogrupo — ninguém conseguia alterar. Agora moram na INDICES e aceitam override.

### Pré-preenchimento do BRIEFING via config JSON

Novo campo `"briefing": {...}` no schema do config. 14 chaves mapeadas 1:1 com os dropdowns. Valores inválidos geram warning e caem no default.

**Fix de encoding:** `open(config)` do Windows usava `cp1252` por default e corrompia acentos do JSON. Corrigido pra `encoding='utf-8'` explícito.

### Fix self-reference dentro da aba INDICES

A linha 29 (PU piso predominante) usava `INDICES!B20` (fator padrão calculado), ignorando override. Alterado pra `INDICES!D20` — agora respeita override do fator padrão.

### Configs por projeto

Criados 3 arquivos em `base/pacotes/{slug}/parametrico-v2-config.json` com dados reais extraídos de:
- `state.json` (AC, UR, padrão Gemma)
- `analise-arquitetura.json` (lazer detectado → piscina/gerador/sauna/spa)
- `memorial-extracao-{slug}.md` (BIM volumes)

| Projeto | Laje | Padrão | Fachada | Piscina | Gerador |
|---|---|---|---|---|---|
| arthen-arboris | Convencional | Médio-Alto | Cerâmica | Sim | Sim |
| placon-arminio-tavares | Convencional | Médio | Cerâmica | Não | Não |
| thozen-electra | **Protendida** | **Alto** | **ACM** | **Aquecida** | Sim |

### Regeração

Parametricos atuais arquivados em `_antigo-parametrico/` dentro de cada pacote. Novos gerados com:
```bash
python scripts/gerar_template_dinamico_v2.py \
  --config base/pacotes/{slug}/parametrico-v2-config.json \
  -o base/pacotes/{slug}/parametrico-{slug}.xlsx
```

Depois `gerar_memorial_pacote.py --tipo parametrico` pra docx, `docx2pdf` pra pdf.

### Documentação formalizada

- **[base/PARAMETRICO-V2-HIBRIDO.md](PARAMETRICO-V2-HIBRIDO.md)** — referência canônica standalone do fluxo
- Atualizado: `base/FASES-FUTURAS.md`, `base/CAMADA-QUALITATIVA-GEMMA.md`, `openclaw/CLAUDE.md`, `openclaw/AGENTS.md`, `openclaw/docs/ORCAMENTO-PARAMETRICO-REFERENCE.md`, `openclaw/orcamento-parametrico/BASE-CONHECIMENTO-PARAMETRICO.md`

### Commits

- `8d704a5` (rebased → `756e050`) — Script + configs + 3 pacotes regerados

## Próximos passos sugeridos

- **Rodar Fase 16 nos outros 123 projetos** da base (overnight ~5h)
- **Validar memoriais** lendo arthen/placon/thozen e marcando itens duvidosos
- **Revisar zero luxo** com rubric mais relaxada se aparecer caso real
- **Dashboard interativo** dos índices derivados (HTML ou Streamlit)
- **Cronograma + curva S** a partir de fórmulas Excel capturadas na Fase 9
- **Migrar mais índices embutidos pra INDICES overridable** — auditar fatores hardcoded que sobraram dentro de fórmulas de macrogrupo (ex: 0.40 bloco cerâmico em alvenaria row 587, 0.25/0.08 drywall, splits MO fixos)
