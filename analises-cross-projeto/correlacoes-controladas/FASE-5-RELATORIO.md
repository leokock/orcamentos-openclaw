# Fase 5 — Correlações Controladas + PCA + Clustering

**Gerado:** 2026-04-18
**Base:** 131 projetos enriquecidos, 102 variáveis analisadas
**Scripts:** `scripts/correlacoes_controladas.py` + `scripts/gerar_planilha_correlacoes.py`

---

## O que mudou das análises anteriores

Fase 5 é **matemática** — aplica estatística formal ao que até agora era descrição. O ponto central: **correlações parciais controlando por confundidores**. Sem esse controle, muitas "descobertas" são artefato.

### Mudança de conclusão: 3 achados anteriores foram RELATIVIZADOS

| Achado anterior | Evidência original | Achado após controle |
|---|---|---|
| "Gerenciamento alto → projeto caro" | r(ger%, rsm2) ~ moderada | **r_parcial(ger% \| regiao) = -0.095 (NULA)** — o que parecia causal era regional |
| "Projetos com mais supra são caros" | correlação aparente | **r_parcial(supra% \| regiao) = -0.039** — mesma coisa: confundidor regional |
| "Taxa aço alta sinaliza R$/m² alto" | fraca | **r_parcial(taxa_aco \| regiao) = -0.12** — sem efeito direto |

### Achados que SOBREVIVERAM o controle

| Correlação | Simples | Parcial | Conclusão |
|---|---:|---:|---|
| AC vs R$/m² \| cub_regiao | -0.27 | **-0.317** | Economia de escala real (leve) — mesmo dentro da mesma região |
| AC vs Total \| cub_regiao | +0.56 | **+0.529** | Total escala com área (óbvio e confirmado) |
| Gerenciamento% vs Hidro% | -0.685 | — | Padrão EPCM: quando ger domina, outros caem |
| Concreto vs Forma (m²/m²) | +0.788 | — | Trivial (mais concreto = mais forma) |

---

## Correlações stratificadas — heterogeneidade revelada

**`r(AC, R$/m²)` dentro de cada região:**

| Região | n | r | Leitura |
|---|---:|---:|---|
| SC-Floripa | 33 | -0.098 | **NULA** — não há economia de escala |
| SC-Vale-Itajaí | 24 | -0.151 | Quase nula |
| SC-BC | 18 | -0.347 | Leve |
| SC-Litoral-Norte | 12 | **-0.516** | **Moderada** — efeito real aqui |

**Insight:** a economia de escala **só aparece em regiões periféricas** (Litoral-Norte: Bombinhas, Itapema, Porto Belo). Em capital/centros urbanos (Floripa, Vale Itajaí) o mercado é consolidado e escala não dá desconto.

**Implicação comercial:** vender "economia de escala" funciona em Litoral-Norte. Em Floripa/Vale Itajaí, argumentar "qualidade por preço fixo" em vez.

---

## PCA — 5 componentes explicam 67% da variação

| Componente | Var explicada | Interpretação |
|---|---:|---|
| **PC1 — "Densidade de acabamento"** | 28.1% | Taxa aço + cobertura + porcelanato. Projetos com mais acabamento fino |
| **PC2 — "Obra acabada"** | 16.8% | Pintura externa + contrapiso + manta asfáltica |
| **PC3 — "Drywall/imperm"** | 9.7% | Drywall divisória + imperm + sist especiais |
| **PC4 — "Infraestrutura"** | 7.1% | Estacas + hidro + rev parede |
| **PC5 — "Terra/forro"** | 5.5% | Mov terra + forro gesso + guarda-corpo |

**Implicação:** os 49 indicadores físicos podem ser reduzidos a **~5 dimensões**. Pra visualização + classificação, usar PC1 × PC2 como scatter plot já captura 45% da variação.

**Se fôssemos criar um "score de produto"**: PC1 (densidade acabamento) sozinho explica 28% — projetos com PC1 alto são "mais bem acabados".

---

## Clustering Ward hierárquico (alternativa ao K-means)

Sobre 67 projetos com dados MG completos, **Ward produziu 4 clusters estáveis:**

| Cluster | N | Exemplos (top 3) | Hipótese de perfil |
|---|---:|---|---|
| 1 | 27 | adore-level-up, amalfi-maiori, amalfi-marine | **Médio-alto padrão standard** |
| 2 | 31 | caledonia-mowe, chiquetti-atlantis, colline-france | **Alto padrão convencional** |
| 3 | 8 | all-lago-di-garda, mendes-empreendimentos, nova-domus | **"EPCM expandido"** (Nova, ALL — alta ger) |
| 4 | 1 | lotisa-serenity | **Outlier** (R$/m² eficiente) |

**Cluster 3 confirma análise anterior** — os 8 projetos são os que já identificamos como "EPCM com escopo expandido" (Nova Empreendimentos + ALL + Mendes).

---

## Como esses resultados mudam o plano

### Fase 6 — Regressão R$/m² (próxima)
Agora temos evidência de que:
- Cub-região é variável dominante — usar como feature principal
- Supraestrutura%, Gerenciamento% **NÃO devem entrar** como features (são artefato regional)
- AC (log) entra como feature — tem efeito real mesmo controlando

**Modelo proposto:**
```
log(rsm2) ~ padrao + cub_regiao + tipologia_canonica + log(AC) + ε
```

Esperado R² ≥ 0.5 (vs -0.17 antes de controlar).

### Fase 10 — Simulador
Com insights causais, o simulador pode dar **melhor diagnóstico de "por quê"** um projeto novo está caro ou barato:
- "Seu projeto está 15% acima da mediana porque está em Floripa (região mais cara), não por escopo inflado"
- "Economia de escala disponível: em Litoral-Norte, aumentar AC em 20% reduz R$/m² em ~5%. Em Floripa, efeito nulo."

---

## Limitações e próximos passos

1. **Amostras pequenas por região** — Litoral-Norte tem só n=12. Correlação r=-0.52 tem IC amplo.
2. **Projetos com "insuficiente" ou econômico/médio com n<5** — não entram bem em regressão.
3. **Cluster 4 (n=1)** — Ward produziu cluster isolado com 1 projeto (lotisa-serenity) — outlier real ou limitação do método.
4. **Correlações parciais binárias** — controlamos por UMA variável de cada vez. Multi-controle seria regressão multivariada (Fase 6).

**Próxima:** Fase 6 — regressão multivariada (agora com guidance claro de quais features incluir).

---

## Arquivos

- **Dados:** `base/correlacoes-controladas.json` (9KB)
- **Excel:** `analises-cross-projeto/correlacoes-controladas/correlacoes-controladas.xlsx` (6 abas)
- **Scripts:** `scripts/correlacoes_controladas.py` + `scripts/gerar_planilha_correlacoes.py`
