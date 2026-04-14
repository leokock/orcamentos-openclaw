# Audit V2 — arthen-arboris

_Gerado em 13/04/2026 22:58 — revisão com base enriquecida (Fases 8-15)_

## 🎯 Contexto

- **AC**: 12.473 m²
- **UR**: 98
- Fontes novas consultadas:
  - `itens-pus-agregados.json` — 4.525 PUs cross-projeto (Fase 10)
  - `indices-derivados-v2.json` — 29 novos índices derivados (Fase 13)
  - `base-indices-master-2026-04-13.json` — base consolidada (Fase 15)

## 🚨 Gravidade dos outliers

| Categoria | Qtd | Ação sugerida |
|---|---|---|
| 🔴 **BUG (>1000% delta)** | 0 | Investigar origem — provável erro de extração |
| 🟠 **Crítico (500-1000%)** | 0 | Revisar manualmente antes de entregar |
| 🟡 **Atenção (100-500%)** | 2 | Validar se faz sentido pro projeto |
| 🔵 **Menor (<100%)** | 19 | Normal, variação de mercado |

## 🟡 Atenção (delta 100-500%)

| Macrogrupo | Descrição | PU usado | PU esperado | Delta |
|---|---|---|---|---|
| Instalações | Tubo de Aço Galvanizado - Ø65 | R$ 107.30 | R$ 35.28 | **+204%** |
| Pisos | Rodapé em madeira | R$ 59.81 | R$ 22.69 | **+164%** |

## 📊 Comparação com novos índices derivados (Fase 13)

Faixas P10-P90 da base de 126 projetos:

| Índice derivado | Mediana base | Valor esperado × AC | n projetos |
|---|---|---|---|
| custo_concreto_rsm2 | R$ 228.90/m² | R$ 2.855.023 | 64 |
| custo_aco_rsm2 | R$ 231.82/m² | R$ 2.891.426 | 65 |
| custo_forma_rsm2 | R$ 164.98/m² | R$ 2.057.774 | 69 |
| custo_escoramento_rsm2 | R$ 47.67/m² | R$ 594.642 | 57 |
| custo_impermeabilizacao_rsm2 | R$ 264.88/m² | R$ 3.303.799 | 95 |
| custo_elevador_rsm2 | R$ 213.33/m² | R$ 2.660.850 | 70 |
| custo_esquadrias_rsm2 | R$ 1154.33/m² | R$ 14.397.965 | 96 |
| custo_pintura_rsm2 | R$ 594.46/m² | R$ 7.414.666 | 96 |
| custo_loucas_rsm2 | R$ 109.76/m² | R$ 1.369.011 | 76 |
| ci_total_rsm2 | R$ 305.56/m² | R$ 3.811.299 | 55 |

## 📋 Recomendações

4. **Validar** os 2 itens em atenção — podem refletir escolha técnica (ex: acabamento alto-padrão)
5. **Cruzar** os totais por macrogrupo do pacote com a tabela de índices derivados acima
6. **Considerar v2** dos pacotes após fix dos bugs — comparar valores antigos × novos

## 🔗 Arquivos relacionados

- `base/pacotes/arthen-arboris/revisao-pus-cross.md` — revisão original de PUs
- `base/pacotes/arthen-arboris/audit-arthen-arboris.md` — audit anterior (v1)
- `base/itens-pus-agregados.json` — base cross-projeto Fase 10
- `base/indices-derivados-v2.json` — 29 novos índices derivados
- `base/base-indices-master-2026-04-13.json` — base master consolidada
