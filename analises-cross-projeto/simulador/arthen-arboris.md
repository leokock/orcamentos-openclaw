# Simulador de Produto — arthen / arboris

**Gerado:** 2026-04-19T14:35:35
**Cliente:** arthen
**Empreendimento:** arboris
**Localização:** Porto Belo/SC (região CUB: `SC-Litoral-Norte`)
**Padrão:** medio-alto
**Tipologia:** `residencial_misto`
**AC:** 12,000.0 m²
**UR:** 180
**N pavimentos:** 20
**N torres:** 1

---

## 🎯 Predição de R$/m² e Total

| Fonte | R$/m² |
|---|---:|
| Regressão multivariada (Fase 6) | R$ 3,717 |
| Mediana da combinação (Fase 4) | R$ 2,878 |
| p25 / p75 da combinação | R$ 2,663 / R$ 3,516 |
| Base médio (regr + combo)/2 | R$ 3,297 |
| **Predição final R$/m²** | **R$ 3,297** |
| Faixa provável (±0.67σ) | R$ 2,637 — R$ 3,958 |
| **Total estimado** | **R$ 39,568,014** |

---

## 📊 Base estatística

- Combinação consultada: `SC-Litoral-Norte | medio-alto` (parcial (regiao+padrao, ignora tipologia))
- N de projetos similares na base: 9
- Top clientes na combinação: paludo(2), all(1), amalfi(1)

## ⚠️ Alertas

- Predição usa combinação parcial (regiao+padrao, ignora tipologia). N de projetos similares é pequeno; usar predição com cautela.

## 💡 Oportunidades de otimização

- Litoral-Norte tem economia de escala moderada (r=-0.52). Se viável, ampliar AC reduz R$/m² ~5-10%.

## 🏗️ Distribuição % por Macrogrupo esperada (mediana da combinação)

| Macrogrupo | % esperado |
|---|---:|
| Gerenciamento | 33.8% |
| Supraestrutura | 22.0% |
| Outros | 10.3% |
| Instal Geral | 9.2% |
| Esquadrias | 7.8% |
| Hidrossanitaria | 5.7% |
| Infraestrutura | 5.5% |
| Sist Especiais | 5.2% |
| Complementares | 4.8% |
| Pisos | 4.7% |
| Pint Interna | 4.6% |
| Pintura Geral | 4.4% |
| Rev Parede | 3.5% |
| Fachada | 3.2% |
| Eletrica | 2.3% |

## 🔗 Projetos comparáveis

| Projeto | AC (m²) | R$/m² | Tipologia |
|---|---:|---:|---|
| `mabrem-gran-torino` | 12,519 | R$ 2,974 | residencial_vertical_alto |
| `amalfi-tramonti` | 15,603 | N/D | residencial_vertical_medio_alto |
| `holze-sense-106` | 8,700 | R$ 3,516 | residencial_vertical_medio_alto |
| `all-lago-di-garda` | 7,056 | R$ 7,160 | residencial_vertical_alto |
| `by-seasons-by-seasons` | 6,349 | N/D | residencial_vertical_medio_alto |

---

## 🔬 Método

O R$/m² final combina:
1. **Regressão multivariada** (Fase 6, R²=0.39): `log(AC) + cub_regiao + padrao + tipologia`
2. **Mediana empírica** da combinação (Fase 4): projetos semelhantes na base
3. **Ajuste por cliente** (Fase 7, quando aplicável): regras if-then detectadas

**Confiança da predição:** média

⚠️ **Use como ESTIMATIVA INICIAL**, não como orçamento definitivo. MAE da regressão é ~R$ 660/m² (~17% da mediana).