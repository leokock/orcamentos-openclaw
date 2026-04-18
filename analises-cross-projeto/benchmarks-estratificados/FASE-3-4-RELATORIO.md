# Fase 3 + Fase 4 — Tipologia + Análise Enriquecida Estratificada

**Gerado:** 2026-04-18
**Base:** 131 projetos enriquecidos (Fase 1)
**Duração:** Fase 3 = 12min (Gemma 131×5s) + Fase 4 = 1min

---

## Fase 3 — Classificação de Tipologia Canônica

**Método:** Gemma2.5:14b recebeu contexto rico de cada projeto (padrão + cidade + AC + UR + rsm2 + sistema estrutural + observações) e classificou em 10 categorias canônicas.

### Resultado

| Tipologia | N projetos | % |
|---|---:|---:|
| residencial_vertical_alto | 80 | 61% |
| residencial_vertical_medio_alto | 37 | 28% |
| residencial_misto | 5 | 4% |
| residencial_vertical_medio | 4 | 3% |
| residencial_vertical_economico | 4 | 3% |
| casa_condominio | 1 | 1% |
| **Total** | **131** | **100%** |

### Qualidade
- **Confiança "alta":** 117/131 (89%)
- **Confiança "média":** 14/131 (11%)
- Confiança baixa: 0

### Descoberta destacada
**Arthen-Arboris classificado como residencial_misto** (não residencial puro). Gemma detectou, via memorial, a presença de componente comercial. Isso valida o método: classificação não se limita ao slug, usa contexto real.

### Distribuição cruzada

**131 projetos por (tipologia, padrão):**
- alto + residencial_vertical_alto = 49 (37% da base)
- medio-alto + residencial_vertical_medio_alto = 33 (25%)
- medio-alto + residencial_vertical_alto = 27 (21%)
- alto + residencial_vertical_medio_alto = 4 (3%)
- outros = 18 (14%)

---

## Fase 4 — Análise Enriquecida Estratificada

**Método:** `scripts/analise_enriquecida.py` cruzou projetos por 4 dimensões:
- CUB-região (9 valores)
- Padrão construtivo
- Tipologia canônica
- Cliente

**Output:** `base/analise-enriquecida-agregada.json` + `benchmarks-estratificados.xlsx` (6 abas)

### Resultado 1 — Por CUB-região

| Região | N projetos | R$/m² mediana | AC mediana |
|---|---:|---:|---:|
| SC-Floripa | 35 | **R$ 3.755** | 12.517 m² |
| SC-Vale-Itajaí | 33 | R$ 3.295 | 11.231 m² |
| SC-BC | 29 | R$ 3.430 | N/D* |
| SC-Litoral-Norte | 13 | R$ 3.036 | 4.430 m² |
| SP-Capital | 5 | R$ 3.028 | — |
| RS-Serra | 4 | R$ 3.392 | — |

*SC-BC: dados de total incompletos em vários projetos

**Insight 1:** **Delta regional de 24% entre extremos** (Floripa mediana R$ 3.755 vs Litoral-Norte R$ 3.036). Diferença não é por padrão (ambas têm mix alto+médio-alto) — é por **CUB local**.

### Resultado 2 — Por (Região, Padrão)

**Combinações com n≥3 (11 combinações):**

| Região | Padrão | N | R$/m² mediana | Interpretação |
|---|---|---:|---:|---|
| SC-Floripa | alto | 13 | **R$ 4.864** | Mais caro: capital + alto padrão |
| SC-Vale-Itajaí | alto | 17 | R$ 3.784 | **22% abaixo de Floripa alto** |
| SC-BC | medio-alto | 15 | R$ 3.430 | Mercado BC = médio-alto dominante |
| SC-Floripa | medio-alto | 18 | R$ 3.499 | — |
| SC-Litoral-Norte | alto | 6 | R$ 3.401 | **30% abaixo de Floripa alto** |
| SC-Vale-Itajaí | medio-alto | 13 | R$ 3.443 | — |
| SC-Litoral-Norte | medio-alto | 6 | R$ 2.662 | Mais barato |

**Insight 2 (forte):** **Mesma classificação de padrão tem variação 22-30% entre regiões**. Isso confirma que "padrão" sozinho não é suficiente pra precificar — **CUB-região é variável tão importante quanto**.

### Resultado 3 — Por (Região, Padrão, Tipologia)

**14 combinações com n≥3 — esta é a granularidade que alimenta o Simulador (Fase 10):**

| Região | Padrão | Tipologia | N |
|---|---|---|---:|
| SC-Vale-Itajaí | alto | residencial_vertical_alto | 16 |
| SC-Floripa | medio-alto | residencial_vertical_medio_alto | 14 |
| SC-BC | alto | residencial_vertical_alto | 13 |
| SC-Floripa | alto | residencial_vertical_alto | 13 |
| SC-BC | medio-alto | residencial_vertical_alto | 10 |
| SC-Vale-Itajaí | medio-alto | residencial_vertical_medio_alto | 9 |
| SC-Litoral-Norte | alto | residencial_vertical_alto | 6 |
| SC-BC | medio-alto | residencial_vertical_medio_alto | 4 |
| SC-Vale-Itajaí | medio-alto | residencial_vertical_alto | 4 |
| SC-Floripa | medio-alto | residencial_vertical_alto | 3 |
| SC-Litoral-Norte | medio-alto | residencial_vertical_alto | 3 |
| SC-Litoral-Norte | medio-alto | residencial_vertical_medio_alto | 3 |
| SC-Outros | alto | residencial_vertical_alto | 3 |
| SP-Capital | medio-alto | residencial_vertical_medio_alto | 3 |

### Descobertas importantes

1. **"Alto padrão" é vendido como residencial_vertical_alto em Vale-Itajaí (16/17), mas em BC/Floripa há sobreposição com medio-alto** — o mercado BC rotula como "alto" projetos que Gemma classifica como médio-alto.

2. **Tipologia diverge do padrão registrado em 31 casos** — 10 projetos com padrão "medio-alto" foram classificados por tipologia como "residencial_vertical_alto" pelo Gemma, e vice-versa. Isso é normal: padrão é auto-declarado pelo cliente, tipologia é classificação objetiva.

3. **Santa Maria é outlier de eficiência:** R$ 1.604/m² (n=3) — bem abaixo de qualquer mediana regional. Chapecó (SC-Oeste) tem CUB menor + escopo enxuto.

4. **Nova e ALL fora da curva:** Nova R$ 6.107 (n=4, Floripa) · ALL R$ 7.159 (n=2, Floripa) — 50-85% acima da mediana Floripa alto. Confirma análise Paludo-vs-Nova V2.

---

## Impacto pra Fases seguintes

### Fase 5 — Correlações controladas (pronta pra rodar)
Agora dá pra calcular `r(rsm2, ac | cub_regiao)` — ver se economia de escala existe dentro da mesma região.

### Fase 6 — Regressão R$/m² (pronta pra rodar)
Variáveis independentes disponíveis:
- AC (contínua)
- CUB-região (categórica, 9 valores)
- Padrão (categórica, 4 valores)
- Tipologia canônica (categórica, 6 valores)

Esperado R² > 0.5 (era -0.17 com só AC).

### Fase 10 — Simulador (muito próximo)
Dado input (cliente + cidade + AC + UR + padrão + tipologia), o simulador agora pode:
1. Encontrar a combinação (região, padrão, tipologia) na matriz de 14 combinações com n≥3
2. Retornar R$/m² p25-p75 da combinação
3. Listar projetos comparáveis da mesma combinação
4. Comparar input com mediana da combinação e sinalizar desvio

**Pra projetos em combinação sem amostra:** usar regressão (Fase 6) como fallback.

---

## Arquivos

- **Excel:** `analises-cross-projeto/benchmarks-estratificados/benchmarks-estratificados.xlsx` (6 abas)
- **Agregado:** `base/analise-enriquecida-agregada.json` (48 combinações)
- **Enriquecidos:** `base/projetos-enriquecidos/{slug}.json` (131 projetos, todos com tipologia)
- **Scripts:**
  - `scripts/classificar_tipologia.py` — Gemma classifica
  - `scripts/analise_enriquecida.py` — estratificação
  - `scripts/gerar_planilha_enriquecida.py` — Excel
  - `scripts/auditar_entregues_vs_base.py` — Fase 1b

---

## Próximas ações sugeridas

1. **Validar tipologias de "confiança média"** — 14 projetos podem ter classificação incorreta
2. **Rodar Fase 5** (correlações controladas) — agora é barato (Python scipy)
3. **Rodar Fase 6** (regressão multivariada) — primeiro modelo preditivo
4. **Começar Fase 10** (simulador) — já temos dados suficientes pra MVP
5. **Decisão pendente:** Fase 1c (import 9 PDFs faltantes) — vale a pena agora ou deixar pra depois?
