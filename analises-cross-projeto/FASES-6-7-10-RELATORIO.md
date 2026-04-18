# Fases 6+7+10 — Regressão + Anti-Padrões + SIMULADOR

**Gerado:** 2026-04-18
**Scripts:** `scripts/regressao_rsm2.py`, `scripts/anti_padroes.py`, `scripts/analisar_produto_novo.py`

---

## Fase 6 — Regressão Multivariada

**Modelo:** `R$/m² ~ log(AC) + cub_regiao + padrao + tipologia_canonica`

**Método:** OLS com dummies pra categoricas + bootstrap 300x pra IC 95%.

**Resultados:**
- n = 55 projetos (filtro AC ≥ 1000 m², R$/m² ∈ [500, 10.000])
- **R² = 0.389**
- RMSE = R$ 935/m²
- **MAE = R$ 658/m² (~17% da mediana)**
- std resíduo = R$ 935/m²

### Coeficientes (efeito isolado controlando outros)

**Efeitos fortes (|coef| > R$ 400):**

| Feature | Coef (R$/m²) | IC 95% |
|---|---:|---|
| intercept (baseline: BC + alto + residencial_vertical_alto) | +6.857 | [+1.499, +13.685] |
| padrao_medio | **-2.430** | [-3.299, +0] |
| padrao_economico | -1.068 | [-2.019, +58] |
| tipologia_canonica_residencial_vertical_economico | -1.068 | [-2.019, +58] |
| cub_regiao_SC-Litoral-Norte | -944 | [-2.730, +570] |
| cub_regiao_SC-Oeste | -939 | [-3.003, +1.946] |
| cub_regiao_SP-Capital | -613 | [-2.100, +826] |
| cub_regiao_SC-Floripa | +559 | [-1.219, +2.451] |
| padrao_medio-alto | -457 | [-1.277, +660] |
| log_ac | -264 | [-977, +184] |

### Leitura

- **Padrão é a variável mais forte**: mudar alto → médio reduz ~R$ 2.430/m²
- **Floripa encarece ~R$ 560/m² vs BC** (baseline)
- **Litoral-Norte barateia ~R$ 940/m²** mais que BC
- **log_ac tem coef -264** mas IC inclui 0 — economia de escala leve, não estatisticamente significativa

R² 0.389 é moderado. Não é um modelo perfeito, mas **explica 39% da variação** — muito melhor que a tentativa inicial (r=-0.17 com só AC).

---

## Fase 7 — Anti-Padrões

**Método:** usa resíduos da Fase 6. Outliers com |z| ≥ 1.0 são analisados pra encontrar features que concentram outliers (cliente, região, tipologia).

**5 regras detectadas (ordenadas por força):**

### Regras ACIMA do modelo (aumentar predição)

| Regra | Ajuste | Força | Evidência |
|---|---:|---|---|
| **IF cliente = Nova Empreendimentos** | **+R$ 2.000/m²** | alta | 3/4 projetos Nova são outliers positivos, resíduo médio +R$ 2.291 |
| IF cliente = ALL | +R$ 2.500/m² | média | n=1 (Lago di Garda, z=+3.2, resíduo +R$ 2.959) |

### Regras ABAIXO do modelo (reduzir predição)

| Regra | Ajuste | Força | Evidência |
|---|---:|---|---|
| **IF cliente = F Nogueira** | **-R$ 1.200/m²** | alta | 2/2 projetos F Nogueira outliers negativos (z=-1.3 cada) |
| IF cliente = Paludo Volo Home | -R$ 1.100/m² | média | z=-1.2 em 1 projeto |
| IF cliente = Santa Maria | -R$ 1.000/m² | média | Chapecó CUB menor + escopo enxuto |

### Top 3 outliers positivos (MAIS CAROS que esperado)

1. **nova-empreendimentos-domus:** real R$ 7.668, prev R$ 4.206 → **+45% (z=+3.7)**
2. **all-lago-di-garda:** real R$ 7.160, prev R$ 4.201 → **+41% (z=+3.2)**
3. **nova-empreendimentos-malta:** real R$ 6.091, prev R$ 4.626 → +24% (z=+1.6)

### Top 3 outliers negativos (MAIS BARATOS que esperado)

1. **nm-empreendimentos:** real R$ 3.218, prev R$ 5.060 → **-57% (z=-2.0)**
2. **f-nogueira-wpr:** real R$ 2.549, prev R$ 3.759 → -48% (z=-1.3)
3. **mussi-empreendimentos-soho:** real R$ 2.456, prev R$ 3.648 → -49% (z=-1.3)

---

## Fase 10 — SIMULADOR DE PRODUTO NOVO

**Deliverable final.** Script: `scripts/analisar_produto_novo.py`

### Uso

```bash
python scripts/analisar_produto_novo.py \
    --cliente arthen --nome arboris \
    --cidade Morretes --uf PR \
    --ac 12500 --ur 48 \
    --padrao medio-alto \
    --tipologia residencial_vertical_medio_alto \
    --n-torres 1 --n-pavimentos 15
```

### O que o simulador faz

1. **Regressão (Fase 6)** calcula R$/m² base dada as features
2. **Busca combinação empírica** (Fase 4) — tenta match exato por `(regiao, padrao, tipologia)`; se não tiver amostra, relaxa pra `(regiao, padrao)` ou só `(regiao)`
3. **Aplica regras de cliente** (Fase 7) — Nova +2k, F Nogueira -1.2k, etc
4. **Calcula faixa** ±0.67σ em torno da predição (aproxima p25-p75)
5. **Lista 5 projetos comparáveis** por (região, padrão) + proximidade de log(AC)
6. **Gera alertas** (combinação fraca, desvio grande, anti-padrão detectado)
7. **Identifica oportunidades** (economia escala em litoral-norte, etc)
8. **Estima distribuição % MG** esperada (mediana da combinação)

### Validação com arthen-arboris (Fase 11)

**Input:** arthen/arboris em Morretes/PR, AC 12.500 m², 48 UR, médio-alto, residencial_vertical_medio_alto, 1 torre, 15 pavimentos.

**Output do simulador:**
- R$/m² regressão: R$ 3.405
- Faixa: R$ 2.779 – R$ 4.032
- Total estimado: **R$ 42.568.000**

**Paramétrico V3 manual da Cartesian** (gerado antes do simulador):
- R$/m²: R$ 3.349
- Total: R$ 41.768.000

**Diferença:** +1.7% em R$/m², +1.9% em total.

**✅ Simulador consistente com o trabalho manual da equipe.** Num projeto completamente novo (Morretes/PR não tem base histórica), o simulador chegou em ±2% do paramétrico detalhado.

---

## Arquitetura do Simulador (modelo mental)

```
Input (cliente, cidade, padrão, tipologia, AC, UR)
        ↓
    [1] Regressão OLS → R$/m² base (R² 0.39)
        ↓
    [2] Busca combinação (região, padrão, tipologia) na base
        ↓ se n≥3
        Mediana + p25-p75 empíricos
        ↓
    [3] Média(regressão, mediana combo) = base
        ↓
    [4] Anti-padrão: +2k (Nova/ALL) | -1.2k (F.Nogueira) | ...
        ↓
    [5] Predição final + faixa ±0.67σ
        ↓
    [6] Projetos similares + alertas + oportunidades
```

### Confiança da predição

| N combinação | Confiança |
|---:|---|
| n ≥ 10 | alta |
| n ≥ 3 | média |
| n < 3 | baixa — usar só regressão |

### Limitações conhecidas

- **R² = 0.389** significa que 61% da variância permanece não-explicada. Modelo é indicativo, não determinístico.
- **MAE R$ 658/m²** = erro médio da predição (~17% da mediana alto padrão).
- **Tipologias raras** (luxo, casa-condomínio, industrial) têm amostra muito pequena → predição dessas tipologias usa regressão pura.
- **Cidades fora da base** (ex: interior SP/MG/GO) usam CUB "{UF}-Outros" genérico.
- **Regras de cliente** só funcionam pros clientes mapeados (7 top). Clientes novos não têm ajuste.

---

## Impacto operacional esperado

### Uso 1 — Briefing comercial rápido
Orçamentista novo recebe solicitação. Em 1 minuto tem predição + faixa + projetos comparáveis. Não precisa esperar análise de 2 dias.

### Uso 2 — Sanity check de paramétrico manual
Equipe gera paramétrico, compara com simulador. Se diferença > 20%, revisa.

### Uso 3 — Negociação comercial
Cliente pede desconto. Mostra mediana regional + projetos similares. Justifica preço.

### Uso 4 — Entrada pra análise estratégica
"Cliente X está sempre 30% acima da mediana — vale a pena atender?"

---

## Evolução futura

### Short-term (fácil)
- Adicionar mais clientes nas regras de anti-padrão (ex: Paludo tem múltiplos projetos = poderia ter regra específica por projeto/sub-tipo)
- Exposição web (Streamlit ou similar) pra facilitar uso
- Integração com base LINDO (dados atuais vêm de JSONs)

### Mid-term (com dados novos)
- Adicionar tipologia mais fina (pele de vidro, vagas, área/unidade)
- Modelo Random Forest / Gradient Boosting (R² provavelmente > 0.5)
- Predição de distribuição % MG mais fina (atualmente só mediana da combo)

### Long-term (qualidade de dados)
- Importar 9 PDFs faltantes (Fase 1c) pra aumentar base
- Consolidar dados de pós-obra pra validar paramétrico → executivo
- Adicionar dimensão temporal (CUB histórico) pra ajustar inflação

---

## Arquivos gerados nesta sessão

- `base/regressao-rsm2.json` (coeficientes + IC95)
- `base/residuos-por-projeto.json` (resíduos dos 55 projetos)
- `base/anti-padroes.json` (regras detectadas)
- `analises-cross-projeto/simulador/arthen-arboris.{json,md}` (validação)
- `scripts/regressao_rsm2.py`
- `scripts/anti_padroes.py`
- `scripts/analisar_produto_novo.py`

---

## Plano — status atualizado

| Fase | Status | Output |
|---|---|---|
| 1 | ✅ | 131 projetos com metadados |
| 1b | ✅ | Auditoria entregues vs base |
| 1c | ⚪ baixa prioridade | Import 9 PDFs |
| 2 | ✅ (na Fase 1) | Cidade 100% |
| 3 | ✅ | Tipologia 131/131 |
| 4 | ✅ | 14 combinações (região × padrão × tipologia) |
| 5 | ✅ | Correlações controladas + PCA + Ward |
| **6** | **✅** | **Regressão R²=0.39** |
| **7** | **✅** | **5 regras anti-padrão** |
| 8 | ⚪ (pode rodar) | Benchmarks estratificados |
| 9 | ⚪ (pode rodar) | Regras textuais (Qwen) |
| **10** | **✅** | **SIMULADOR MVP funcionando** |
| 11 | ✅ | Validação arthen-arboris OK (±2%) |
| 12 | ⚪ | Manutenção mensal |

**Objetivo principal do plano alcançado:** simulador de produto funcional e validado.
