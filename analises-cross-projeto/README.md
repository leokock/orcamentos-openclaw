# Análises Cross-Projeto — Base de Conhecimento Cartesian

**Propósito:** consolidar análises que atravessam múltiplos projetos pra identificar padrões de produto imobiliário, correlações e benchmarks acionáveis.

**Análises específicas de UM projeto** ficam em `~/orcamentos/parametricos/{slug}/` (Drive). Aqui é **o que aprendemos olhando TODOS juntos**.

---

## Plano geral

**→ Ver [PLANO-ANALISE-PRODUTO.md](./PLANO-ANALISE-PRODUTO.md) — cronograma de 12 fases pra extrair conhecimento acionável**

---

## Estrutura

### Fase 1-3 — Feito (análises base)

| Pasta | O que tem | Pergunta respondida |
|---|---|---|
| [`produto/`](./produto/) | 18 abas, 49 indicadores físicos | "O projeto tem X pontos de iluminação por UR — é muito ou pouco pro padrão?" |
| [`financeira/`](./financeira/) | 12 abas, R$ e % MG | "Onde está a grana? Qual a distribuição por macrogrupo?" |
| [`avancada/`](./avancada/) | 8 abas, clusters + qualitativa | "Quem são os clientes? Que tipologias emergem? O que os orçamentistas anotaram?" |
| [`clusters/`](./clusters/) | 5 abas, deep-dive Cluster 1 | "O que caracteriza o segmento EPCM/alto-gerenciamento?" |
| [`fichas-cliente/`](./fichas-cliente/) | 14 fichas comerciais | "Qual o perfil da Nova? Paludo? Mussi?" (uso em reunião comercial) |
| [`comparacoes/`](./comparacoes/) | Paludo vs Nova, Mussi vs Pass-e | "Dois clientes similares — o que difere?" |
| [`qualidade/`](./qualidade/) | Checklist + revisões qwen | "Como garantir que nossa análise não tem salto lógico?" |
| [`sessoes/`](./sessoes/) | Resumos de sessão | "O que fizemos em cada dia de trabalho" |

### Fase 4-10 — A fazer (enriquecimento)

| Pasta (a criar) | Fase | Pergunta |
|---|---|---|
| `correlacoes-controladas/` | 5 | "Quais correlações são reais, quais são artefato?" |
| `anti-padroes/` | 7 | "Quais combinações geram custo excessivo?" |
| `benchmarks-estratificados/` | 8 | "Pra tipologia+padrão+região X, qual a faixa esperada?" |
| `regras-produto/` | 9 | "Se projeto tem X, devemos esperar Y. Se tem Z, evitar W." |
| `simulador/` | 10 | **Deliverable final: dado projeto novo, qual a análise preditiva?** |

---

## Como navegar

**Quero benchmark rápido pra um projeto novo:**
→ `produto/analise-produto-cartesian.xlsx` (aba BENCHMARKS)

**Quero entender R$/m² de um padrão:**
→ `financeira/analise-financeira-cartesian.xlsx` (aba RESUMO)

**Quero saber o perfil de um cliente específico:**
→ `fichas-cliente/fichas-cliente-cartesian.xlsx` (1 aba por cliente)

**Quero ver projetos similares ao meu:**
→ `avancada/analise-avancada-cartesian.xlsx` (aba CLUSTERS)

**Quero investigar um outlier:**
→ `produto/analise-produto-cartesian.xlsx` (aba OUTLIERS)

**Quero entender por que 2 clientes têm R$/m² tão diferente:**
→ `comparacoes/PALUDO-VS-NOVA-V2-APOS-REVISAO.md`

**Quero publicar uma análise nova sem erros:**
→ `qualidade/CHECKLIST-QUALIDADE-ANALISE.md`

---

## Scripts associados (em `~/orcamentos-openclaw/scripts/`)

| Script | Gera | Pasta destino |
|---|---|---|
| `extrair_indicadores_produto.py` | `base/indicadores-produto/*.json` | — |
| `agregar_indicadores_produto.py` | `base/indicadores-produto-agregados.json` | — |
| `gerar_planilha_analise_produto.py` | Excel 18 abas | `produto/` |
| `analise_financeira_executivos.py` | `base/analise-financeira-agregada.json` | — |
| `gerar_planilha_financeira.py` | Excel 12 abas | `financeira/` |
| `analise_avancada.py` | `base/analise-avancada-agregada.json` | — |
| `gerar_planilha_avancada.py` | Excel 8 abas | `avancada/` |
| `gerar_planilha_cluster3_parametrico.py` | Excel 5 abas | `clusters/` |
| `gerar_fichas_cliente.py` | Excel 14 fichas | `fichas-cliente/` |
| `comparar_clientes.py` | MD + JSON por par | `comparacoes/` |
| `comparar_param_exec.py` | MD + JSON por par | (aguardando primeiro par) |
| `revisar_md_qwen.py` | Revisões | `qualidade/revisoes-qwen/` |
| `check_slug_consistency.py` | Relatório pares | `qualidade/` |

---

## Dados brutos (fonte)

- `base/indices-executivo/*.json` — 126 projetos entregues
- `base/itens-detalhados/*.json` — 306k+ itens
- `base/indicadores-produto/*.json` — 126 extrações físicas
- `base/metadados-projeto/*.json` — **Fase 1 (a criar)**
- `base/localizacao-projetos.json` — **Fase 2 (a criar)**

---

## Ciclo de qualidade

Toda análise nova publicada aqui passa por:

1. Escrever MD
2. Rodar `scripts/revisar_md_qwen.py --file {caminho}` (R1)
3. Aplicar críticas
4. Se reescreveu muito: rodar R2 (`--suffix="-r2"`)
5. Commit
6. Atualizar `README.md` da pasta correspondente

**→ Ver [qualidade/CHECKLIST-QUALIDADE-ANALISE.md](./qualidade/CHECKLIST-QUALIDADE-ANALISE.md) pra rigor estatístico obrigatório.**
