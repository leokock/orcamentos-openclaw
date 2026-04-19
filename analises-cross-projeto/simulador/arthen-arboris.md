# Simulador de Produto — arthen / arboris

**Gerado:** 2026-04-19T09:15:53
**Cliente:** arthen
**Empreendimento:** arboris
**Localização:** Morretes/PR (região CUB: `PR-Litoral`)
**Padrão:** medio-alto
**Tipologia:** `residencial_vertical_medio_alto`
**AC:** 12,500.0 m²
**UR:** 48
**N pavimentos:** 15
**N torres:** 1

---

## 🎯 Predição de R$/m² e Total

| Fonte | R$/m² |
|---|---:|
| Regressão multivariada (Fase 6) | R$ 2,609 |
| Base médio (regr + combo)/2 | R$ 2,609 |
| **Predição final R$/m²** | **R$ 2,609** |
| Faixa provável (±0.67σ) | R$ 1,945 — R$ 3,273 |
| **Total estimado** | **R$ 32,607,004** |

---

## 📊 Base estatística

- Combinação consultada: `nenhuma` (sem combinacao)
- N de projetos similares na base: 0

## ⚠️ Alertas

- Predição usa combinação sem combinacao. N de projetos similares é pequeno; usar predição com cautela.

---

## 🔬 Método

O R$/m² final combina:
1. **Regressão multivariada** (Fase 6, R²=0.39): `log(AC) + cub_regiao + padrao + tipologia`
2. **Mediana empírica** da combinação (Fase 4): projetos semelhantes na base
3. **Ajuste por cliente** (Fase 7, quando aplicável): regras if-then detectadas

**Confiança da predição:** baixa

⚠️ **Use como ESTIMATIVA INICIAL**, não como orçamento definitivo. MAE da regressão é ~R$ 660/m² (~17% da mediana).