# Plano Completo — Análise de Produto Imobiliário Cartesian

**Objetivo:** estabelecer base de conhecimento sobre **padrões de produto imobiliário** (correlações, anti-padrões, benchmarks) pra que, na análise de um próximo projeto, o sistema Cartesian consiga **sugerir como o produto pode ser melhorado** antes da obra ter custo realizado.

**Método:** processamento local com Gemma (extração rápida) + Qwen2.5:14b (interpretação qualitativa), rodando em loops overnight sobre toda a base disponível (executivos entregues + paramétricos ativos + projetos brutos).

**Escopo temporal:** ~2 semanas de execução (noites + fins de semana), com checkpoints diários de revisão.

---

## 1. Diagnóstico do estado atual

### Dados estruturados já coletados
- **126 projetos** com `indices-executivo/*.json` (macrogrupos, estruturais, esquadrias, PUs)
- **49 indicadores físicos** extraídos cross-projeto (`indicadores-produto-agregados.json`)
- **Clusters + distribuição MG + quartis + correlações** (3 análises cross já feitas)
- **8 fichas de cliente** consolidadas (Nova, Paludo, Mussi, etc)
- **Checklist de qualidade** institucional aplicado

### Gaps identificados (pela revisão qwen R1+R2)
- **Localização** — só 5/126 projetos têm cidade/UF estruturada
- **Tipologia** — não há campo (residencial/misto/comercial/misto-comercial)
- **Data_base** — só 14/126 projetos
- **Especificação técnica** — não temos fck, classe de tinta, espessura de vidro por item
- **Contratos** — hipótese EPCM não validada
- **Programa arquitetônico** — número de tipologias, metragem de cada, área de lazer, vagas

### Dados brutos ainda não processados (ouro não extraído)
Em `~/orcamentos/projetos/` (Drive `_Projetos_IA/`) temos:
- **Memoriais descritivos** (PDF + DOCX) — 8-10 projetos têm
- **IFCs** (BIM) — fg-senna tem 13 IFCs por bloco, placon tem, san-fellice tem
- **DWGs + PDFs** de plantas — todos têm
- **Estudos preliminares** (lazer, tipologia, diferenciados)
- **RTs + ARTs** (responsabilidade técnica, quem projetou)
- **Estudos de tráfego de elevador** (san-fellice)
- **Relatórios de compatibilização** (arthen-arboris)

---

## 2. Arquitetura do conhecimento

### Hierarquia de abstração

```
┌─────────────────────────────────────────────────┐
│ CAMADA 5 — TEORIA DE PRODUTO                    │
│  "Dado X, espere Y. Evite Z."                   │
│  Regras if-then testáveis                        │
└─────────────────────────────────────────────────┘
                      ↑ deriva de
┌─────────────────────────────────────────────────┐
│ CAMADA 4 — PADRÕES NARRATIVOS                   │
│  "Clientes eficientes têm essa característica"  │
│  Qwen escreve (PT-BR)                            │
└─────────────────────────────────────────────────┘
                      ↑ agrega
┌─────────────────────────────────────────────────┐
│ CAMADA 3 — CORRELAÇÕES CONTROLADAS              │
│  r[mg_gerenciamento, rsm2] controlando padrão   │
│  Python + scipy, n>=30 em cada subgrupo          │
└─────────────────────────────────────────────────┘
                      ↑ mede
┌─────────────────────────────────────────────────┐
│ CAMADA 2 — METADADOS ENRIQUECIDOS               │
│  tipologia, localização, fck, n_tipologias, ... │
│  Gemma extrai de PDFs/memoriais                  │
└─────────────────────────────────────────────────┘
                      ↑ adiciona a
┌─────────────────────────────────────────────────┐
│ CAMADA 1 — DADOS BRUTOS ESTRUTURADOS (feito)    │
│  49 indicadores físicos + financeiros por proj  │
└─────────────────────────────────────────────────┘
```

### Por que Gemma + Qwen?

| Modelo | Use case | Força | Fraqueza |
|---|---|---|---|
| **Gemma4:e4b** (9.6GB) | **Extração estruturada em volume** | Rápido (~1s/item), bom com JSON | PT-BR ruim pra geração longa |
| **Qwen2.5:14b** (9GB) | **Interpretação, crítica, narrativa** | PT-BR excelente, raciocínio | Lento (~4min/doc grande) |

**Divisão de trabalho:**
- Gemma: "leia este memorial de 20 páginas e extraia {tipologia, n_pavimentos, ...} em JSON"
- Qwen: "dado esses 126 projetos agrupados por padrão, escreva 500 palavras sobre o que diferencia produtos eficientes"

---

## 3. Pipeline de análises (12 fases)

### Fase 1 — Enriquecimento de metadados (Gemma) 🔵 NÃO INICIADA

**Input:** PDFs/DOCX de memoriais + plantas em `~/orcamentos/projetos/`

**Processamento:**
- Usar `gemma` para extrair, de cada projeto, um JSON estruturado:
  ```json
  {
    "slug": "arthen-arboris",
    "cidade": "Morretes",
    "uf": "PR",
    "tipologia": "residencial multifamiliar",
    "n_torres": 1,
    "n_pavimentos_total": 15,
    "n_tipologias_apto": 3,
    "tipologias_apto": [
      {"nome": "Tipo 1", "area_m2": 85, "n_dormitorios": 2, "n_suites": 1, "n_vagas": 1},
      ...
    ],
    "area_lazer_m2": 420,
    "n_elevadores": 2,
    "sistema_estrutural": "alvenaria estrutural|concreto armado|misto",
    "fck_predominante_projeto": 30,
    "altura_pe_direito": 2.8,
    "data_memorial": "2026-03-16",
    "tem_pele_de_vidro": false,
    "tem_churrasqueira_apto": true,
    "tipo_cobertura": "telha cerâmica|laje impermeabilizada|metálica",
    ...
  }
  ```

**Saída:** `base/metadados-projeto/{slug}.json`

**Estimativa:** 20 projetos do `_Projetos_IA/` + extração dos 126 executivos via qualitative → **~2 noites**

**Script a criar:** `scripts/extrair_metadados_projeto.py`

---

### Fase 1c — Import de entregas em PDF (OCR + extração) ⚪ NOVO

**Contexto:** auditor Fase 1b identificou **9 entregas no Drive sem par na base**, todas entregues apenas em PDF (não xlsx):
- Essege/Dom, EZE/Canto Grande, Pavitec/Siena, Rosner/Alameda Jardins, Serati/Manhatan
- Holze/Nouve, Inbrasul/Amber, Mabrem/Liberato, Santa Maria/We

Também há **5 órfãos na base** (slug existe mas não aparece na pasta Drive): cambert-portal-da-brava, nm-empreendimentos, nobria, pavcor, sak-engenharia. Possíveis causas: projeto cancelado, pasta movida, slug errado.

**Atividades Fase 1c:**

1. **Import minimal (rápido):** criar `indices-executivo/{slug}.json` com metadados básicos extraídos dos nomes de pasta + Gemma lendo o PDF capa/apresentação:
   ```json
   {"projeto": "eze-canto-grande", "fonte": "pdf_entrega", "cidade": "...", "ur": "...", "ac": "..."}
   ```
2. **OCR de tabelas (custoso, opcional):** usar `pdfplumber.extract_tables()` pra tentar pegar planilha ABC/serviços do PDF. Sucesso variável.
3. **Rodar Fase 1 + Fase 3** nos 9 slugs novos
4. **Fase 1b re-auditar** pra garantir cobertura
5. **Investigar órfãos:** verificar se cada um está em `/Serviços Concluídos/`, renomeado, ou deve ser removido da base

**Prioridade:** baixa — esses 9 projetos são <7% da base e não têm dados estruturais. Deixar como "expand quando a base for re-processada com OCR robusto".

**Script a criar:** `scripts/importar_pdf_entregas.py`

---

### Fase 1b — Expansão de cobertura: TODOS os entregues 🔵 NOVO

**Contexto:** Leo pediu que a reclassificação (tipologia + cidade) se aplique a **todos os projetos em `_Entregas/Orçamento_executivo/`** (path local via symlink `~/orcamentos/executivos/entregues/`).

**Estado atual:** base tem 126 projetos em `indices-executivo/`. Pasta entregues tem **130 obras em 73 clientes** (subpastas `cliente/obra/`). Diferença: ~4-6 entregas recentes ainda não importadas.

**Atividades:**

1. **Criar symlink** (se não existir): `~/orcamentos/executivos/entregues/ → _Entregas/Orçamento_executivo/` (conforme CLAUDE.md já define)

2. **Script `scripts/auditar_entregues_vs_base.py`:**
   - Lista todos os `cliente/obra/` em `entregues/`
   - Mapeia pra slug canônico (ex: `Amalfi/Maiori` → `amalfi-maiori`)
   - Compara com `base/indices-executivo/*.json`
   - Gera: (a) lista de "faltantes" (entregues sem slug na base), (b) lista de "órfãos" (slugs na base sem entrega correspondente)

3. **Script `scripts/importar_entregues_faltantes.py`** (se faltantes > 0):
   - Pra cada entrega faltante, buscar orçamento executivo xlsx/pdf na pasta
   - Extrair dados estruturados via pipeline existente (gerar_novos_indices ou manual)
   - Criar `base/indices-executivo/{slug}.json` correspondente
   - Disparar Fase 1 + Fase 3 pros novos slugs

4. **Re-aplicar cidade + tipologia em TODOS:**
   - Re-rodar `enriquecer_metadados.py` (Fase 1) — garantir cidade em 100%
   - Re-rodar `classificar_tipologia.py` (Fase 3) nos novos slugs
   - Validar que `projetos-enriquecidos/*.json` cobre 130/130 entregues

5. **Relatório:** `FASE-1B-COBERTURA-ENTREGUES.md` com:
   - Total entregues analisados
   - Slugs novos importados
   - Slugs sem match (órfãos antigos que não estão mais nas entregas)
   - Cobertura final de cidade + tipologia

**Prazo:** 1 dia (após Fase 3 terminar). Script de auditoria é rápido, importação depende do volume (máximo ~10 projetos novos).

**Output:** base expande de 126 pra 130+ projetos com cidade + tipologia em 100%.

---

### Fase 2 — Normalização de localização (manual + Gemma) 🔵

**Objetivo:** todos os 126 projetos têm cidade/UF.

**Estratégia:**
1. Gemma extrai de qualitative.observacoes onde houver
2. Para projetos sem: buscar no nome do cliente + slug pistas ("cn-brava" = Brava/SC)
3. Manter lista `base/localizacao-projetos.json` com: {slug, cidade, uf, cub_regiao}

**Regiões CUB Sinduscon:** SC, RS, PR, SP, RJ, MG, BA (e subdivisões onde aplicável).

**Saída:** adicionar campo `cidade/uf/cub_regiao` em `indices-executivo/*.json`

**Script a criar:** `scripts/normalizar_localizacao.py`

---

### Fase 3 — Classificação de tipologia (Gemma) 🔵

**Objetivo:** campo categórico por projeto.

**Categorias alvo:**
- `residencial_vertical_economico` (HIS, MCMV)
- `residencial_vertical_medio` (empreendimento popular classe C)
- `residencial_vertical_medio_alto` (classe B)
- `residencial_vertical_alto` (classe A)
- `residencial_vertical_luxo` (classe AA)
- `residencial_misto` (comercial + residencial)
- `comercial_vertical`
- `lajes_corporativas`
- `casa_condominio`
- `industrial`

**Método:** Gemma lê memorial + valor/m² + padrão registrado + número unidades + área + localização → retorna tipologia canônica.

**Saída:** `indices-executivo/*.json` ganha campo `tipologia_canonica`.

**Script:** `scripts/classificar_tipologia.py`

---

### Fase 4 — Re-rodar análises com metadados enriquecidos ⚪

Após Fases 1-3:
- Re-rodar `agregar_indicadores_produto.py` com estratificação por tipologia+localização
- Re-rodar `analise_financeira_executivos.py` com filtro CUB regional
- Re-rodar `analise_avancada.py` com vetor de assinatura incluindo tipologia

**Saída:** versões v2 das análises principais.

---

### Fase 5 — Correlações controladas (Python + scipy) ⚪

**Objetivo:** eliminar falsas correlações (ex: alvenaria~porcelanato r=1.00 era artefato).

**Análises:**

1. **Correlações parciais** — r(X, Y | Z) onde Z é fator confundidor
   - Exemplo: r(pontos_iluminacao, rsm2 | tipologia)
   - Se cai pra 0, a correlação original vinha de tipologia, não de causalidade direta

2. **Regressão multivariada** — R$/m² = β0 + β1·AC + β2·tipologia + β3·cub_regiao + β4·padrão + ε
   - Identificar coeficientes estatisticamente significativos (p<0.05)

3. **Clustering hierárquico** — refinar os 4 clusters atuais com dendrograma (não só K-means)

4. **PCA** (análise de componentes principais) — reduzir 49 indicadores em 3-5 componentes interpretáveis

**Saída:** `analises-cross-projeto/correlacoes-controladas/`
- `RESUMO-CORRELACOES.md` — quais correlações sobrevivem ao controle
- `regressao-rsm2.xlsx` — coeficientes + IC + significância
- `pca-componentes.xlsx` — componentes principais

**Script:** `scripts/correlacoes_controladas.py` (usar scipy.stats, sklearn)

---

### Fase 6 — Análise de decomposição R$/m² (Python) ⚪

**Objetivo:** decompor R$/m² de cada projeto em fatores explicativos.

**Fórmula:**
```
R$/m² = base_tipologia
      + ajuste_padrão
      + ajuste_localização (CUB regional)
      + ajuste_escala (log(AC))
      + ajuste_modelo_contratação (EPCM vs não)
      + ajuste_especificação (premium/normal)
      + residual (variação não explicada)
```

**Método:** regressão linear multinível com cada fator como variável.

**Saída:** pra cada projeto, tabela de decomposição — "seu R$/m² é R$ 4.200, composto por R$ 2.800 base tipológica + R$ 400 padrão + R$ 300 localização + R$ 700 escala + ε".

**Utilidade direta:** ao orçar projeto novo, apresentar decomposição esperada antes de ir a detalhe.

---

### Fase 7 — Detecção de anti-padrões (Gemma + Qwen) ⚪

**Objetivo:** identificar **combinações ruins** — projetos que gastaram mais que o esperado por motivo identificável.

**Processamento:**
1. Pra cada projeto, calcular **resíduo** da regressão (Fase 6)
2. Projetos com resíduo positivo > 2σ = "gastou acima do esperado"
3. Qwen lê o memorial + qualitative do projeto e escreve "provavelmente por X"
4. Classificar em padrões recorrentes: "especificação premium em escopo econômico", "gerenciamento excessivo pra escala", "fachada envidraçada com AC baixo", etc

**Saída:** `analises-cross-projeto/anti-padroes/ANTI-PADROES.md`

---

### Fase 8 — Benchmarks estratificados (Python) ⚪

**Objetivo:** pra cada combinação `(tipologia, padrão, faixa_AC, cub_regiao)`, publicar benchmarks.

**Exemplo de saída:**
```
Residencial vertical médio-alto, AC 5-15k m², Região SC-Litoral:
  R$/m² total:     p25 R$ 3.100  |  med R$ 3.450  |  p75 R$ 3.800  (n=12)
  Supraestrutura:  19-22% do total (med 20.5%)
  Gerenciamento:   12-16% do total
  Esquadrias:      8-11% do total
  ...
  Taxa aço:        65-75 kg/m³ concreto
  Concreto:        0.32-0.40 m³/m² AC
  Pintura interna: 4.5-6.5 m²/m² AC
```

**Saída:** `analises-cross-projeto/benchmarks-estratificados/` com 1 MD por combinação (uns 40-60 arquivos — granularidade adequada ao volume da base).

---

### Fase 9 — Regras de produto testáveis (Qwen) ⚪

**Objetivo:** dos padrões descobertos nas Fases 5-8, extrair **regras acionáveis** via Qwen.

**Exemplo de regra:**
```
IF tipologia = residencial_vertical_alto
AND pele_de_vidro = true
AND AC < 8000 m²
THEN esperar fachada_rsm2 > R$ 250
AND avaliar se tamanho compensa o custo (economia de escala ruim)
```

**Formato:** cada regra tem:
- Condição (IF)
- Predição (THEN espere)
- Força (baseado em n, p-value, consistência)
- Referência (quais projetos suportam)

**Saída:** `analises-cross-projeto/regras-produto/REGRAS.yaml` (formato estruturado) + MD explicativo

---

### Fase 10 — Simulador de análise de produto novo (Python + Qwen) ⚪

**Objetivo:** input = características do projeto novo, output = análise preditiva + recomendações.

**Interface proposta:**
```bash
python scripts/analisar_produto_novo.py \
  --cliente arthen \
  --nome arboris \
  --tipologia residencial_vertical_medio_alto \
  --cidade Morretes --uf PR \
  --ac 12500 \
  --ur 48 \
  --padrao medio-alto \
  --n_torres 1 \
  --n_pavimentos 15
```

**Output automatizado:**
1. R$/m² esperado (faixa p25-p75 da combinação)
2. Distribuição MG esperada
3. Indicadores físicos esperados
4. **Alertas**: se algum parâmetro gera anti-padrão conhecido
5. **Oportunidades de otimização**: baseadas em regras Fase 9
6. **Projetos comparáveis**: 3-5 da base mais similares
7. **Narrativa**: Qwen escreve 300 palavras interpretando o perfil

**Saída:** `analises-cross-projeto/simulador/{cliente}-{projeto}.md`

**Utilidade:** **este é o deliverable final que justifica tudo** — é o que entrega valor na análise de próximo projeto.

---

### Fase 11 — Validação com arthen-arboris (piloto) ⚪

**Método:**
1. Rodar o simulador (Fase 10) com inputs do arthen-arboris
2. Comparar predição com o paramétrico V3 já gerado
3. Medir desvio
4. Ajustar modelos conforme necessário
5. Quando arthen virar executivo, rodar `comparar_param_exec.py` e medir erro real

---

### Fase 12 — Manutenção contínua ⚪

**Frequência mensal:**
- Rodar `extrair_metadados_projeto.py` pros projetos novos
- Re-agregar
- Re-treinar regressão/clustering

**Frequência por projeto novo:**
- Sempre rodar Fase 10 (simulador) no início
- Sempre usar `CHECKLIST-QUALIDADE-ANALISE.md` antes de publicar

---

## 4. Cronograma sugerido (loops overnight)

| Noite | Fase | Atividade | Tempo estimado |
|---|---|---|---|
| **N1** | 1 | Gemma extrai metadados de ~20 projetos do `_Projetos_IA/` | 3-5h |
| **N2** | 1 (cont) | Gemma extrai de `_Executivo_IA/` + `_Entregas/` | 4-6h |
| **N2.5** | 1b | Auditar entregues vs base + importar faltantes + re-classificar | 4-8h |
| **N3** | 2-3 | Normalização localização + classificação tipologia | 3-4h |
| **N4** | 4 | Re-rodar 3 análises principais com metadados | 30min (CPU) |
| **N5** | 5 | Correlações controladas + regressão + PCA | 1-2h |
| **N6** | 6 | Decomposição R$/m² + ajuste de modelo | 2h |
| **N7** | 7 | Detecção anti-padrões (Qwen escreve por projeto outlier) | 6-8h Qwen |
| **N8** | 8 | Benchmarks estratificados | 1h |
| **N9** | 9 | Qwen extrai regras (com múltiplas passadas) | 4-6h |
| **N10** | 10 | Implementar simulador | 1 dia (pessoa) |
| **N11** | 11 | Validação com arthen-arboris | 2h |
| **N12+** | 12 | Manutenção | contínuo |

**Total:** ~12 noites de processamento + ~2 dias de trabalho humano.

---

## 5. Métricas de sucesso

| Métrica | Objetivo | Como medir |
|---|---|---|
| Cobertura de metadados | 90%+ dos projetos com tipologia, localização | contar projetos com campos preenchidos |
| Poder explicativo da regressão | R² ≥ 0.6 | output da regressão na Fase 5 |
| Regras de produto acionáveis | ≥ 20 regras com força ≥ média | contar em REGRAS.yaml |
| Validação do simulador | desvio médio < 10% no paramétrico arthen | comparar com V3 existente |
| Melhoria em próximo paramétrico | redução de retrabalho em 30% | medir tempo de orçamento antes/depois |

---

## 6. Estrutura de arquivos proposta

### Drive `~/orcamentos/parametricos/` (`_Parametrico_IA/`)
**Apenas pastas de projeto** — nenhum arquivo solto:
```
parametricos/
├── TAK/
├── arminio-tavares/
├── arthen-arboris/
├── bci-alipio/
├── cambert-now/
├── ctn-alf-sfl/
├── nf-itajai/
└── thozen-electra/
```

### Repo `~/orcamentos-openclaw/analises-cross-projeto/` (FEITO)
```
analises-cross-projeto/
├── produto/              # análise de indicadores físicos (v1)
├── financeira/           # análise $, % MG (v1)
├── avancada/             # cluster + qualitativa (v1)
├── clusters/             # deep-dive Cluster 1 EPCM (v1)
├── fichas-cliente/       # perfis comerciais (v1)
├── comparacoes/          # Paludo vs Nova, Mussi vs Pass-e
├── qualidade/            # checklist + revisões qwen
├── sessoes/              # resumos de sessão
│
├── correlacoes-controladas/  # FASE 5 (a criar)
├── anti-padroes/             # FASE 7 (a criar)
├── benchmarks-estratificados/ # FASE 8 (a criar)
├── regras-produto/           # FASE 9 (a criar)
├── simulador/                # FASE 10+11 (a criar)
└── PLANO-ANALISE-PRODUTO.md  # este arquivo
```

### Repo `~/orcamentos-openclaw/base/` — dados brutos agregados
```
base/
├── indices-executivo/*.json     # 126 projetos (já existe)
├── indicadores-produto/*.json   # 126 projetos (já existe)
├── metadados-projeto/*.json     # Fase 1 (a criar)
├── localizacao-projetos.json    # Fase 2 (a criar)
├── indicadores-*-agregados.json # re-gerar na Fase 4
└── ...
```

### Repo `~/orcamentos-openclaw/scripts/` — scripts reusáveis
```
scripts/
├── (scripts existentes — 13 arquivos)
├── extrair_metadados_projeto.py  # Fase 1
├── normalizar_localizacao.py     # Fase 2
├── classificar_tipologia.py      # Fase 3
├── correlacoes_controladas.py    # Fase 5
├── decomposicao_rsm2.py          # Fase 6
├── detectar_anti_padroes.py      # Fase 7
├── gerar_benchmarks.py           # Fase 8
├── extrair_regras_qwen.py        # Fase 9
└── analisar_produto_novo.py      # Fase 10 (SIMULADOR)
```

---

## 7. Riscos e mitigações

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Gemma falha em extrair metadados bem (PDFs escaneados) | Média | OCR prévio + retry com prompt refinado; fallback manual nos top 10 clientes |
| Qwen gera regras triviais ou erradas | Média | Validação humana obrigatória em regras antes de aplicar no simulador |
| R² da regressão fica baixo (< 0.4) | Alta (base pequena) | Aceitar e usar faixa em vez de ponto; mais dados ao longo do tempo melhoram |
| Tipologia difícil de canonizar | Média | Usar padrão já registrado + localizar de outra forma em casos ambíguos |
| Projetos brutos incompletos | Alta | Priorizar análise nos projetos com dado completo; deixar outros na fila |

---

## 8. Primeira entrega (próxima sessão)

**Minha sugestão de priorização:**

1. **Reorganização de arquivos** ✅ **FEITO** nesta sessão
2. **Gerar índice do `analises-cross-projeto/`** — README.md navegável em cada subdir
3. **Script `extrair_metadados_projeto.py`** — Fase 1, rodando Gemma nos PDFs/memoriais
4. **Disparar Fase 1 overnight**
5. **Na manhã seguinte**: Fase 2 (localização) + Fase 3 (tipologia)

Se tudo der certo até N3, nos dias seguintes atacamos Fase 4-6 (análises matemáticas) que são rápidas.

---

## 9. Observações meta

- **Este plano nasce do ciclo qwen R1+R2** — as limitações que qwen apontou (localização, tipologia, contratos) se tornaram Fases 1-3 do plano
- **Não duplicar trabalho já feito** — os indicadores físicos, clusters, fichas já estão feitos; o plano só **enriquece** a base pra fazer novas camadas
- **Qwen continua como revisor** — todo MD novo gerado nas Fases 5-9 passa por `revisar_md_qwen.py` antes de publicar
- **Simulador (Fase 10) é o entregável-chave** — se tudo mais falhar mas o simulador funcionar, a Cartesian ganha ferramenta que nenhum concorrente tem
- **Base continua crescendo** — próximos projetos alimentam a regressão e tornam regras mais fortes

---

## Próxima ação imediata

Criar `scripts/extrair_metadados_projeto.py` e disparar na próxima noite sobre os 7 projetos do `_Projetos_IA/`. Isso começa a Fase 1.

**Pergunta pro Leo:** aprovar plano antes de executar Fase 1, ou seguir direto pro script?
