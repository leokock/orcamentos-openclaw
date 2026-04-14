# Audit V2 — placon-arminio-tavares

_Gerado em 13/04/2026 22:58 — revisão com base enriquecida (Fases 8-15)_

## 🎯 Contexto

- **AC**: 4.077 m²
- **UR**: 55
- Fontes novas consultadas:
  - `itens-pus-agregados.json` — 4.525 PUs cross-projeto (Fase 10)
  - `indices-derivados-v2.json` — 29 novos índices derivados (Fase 13)
  - `base-indices-master-2026-04-13.json` — base consolidada (Fase 15)

## 🚨 Gravidade dos outliers

| Categoria | Qtd | Ação sugerida |
|---|---|---|
| 🔴 **BUG (>1000% delta)** | 2 | Investigar origem — provável erro de extração |
| 🟠 **Crítico (500-1000%)** | 0 | Revisar manualmente antes de entregar |
| 🟡 **Atenção (100-500%)** | 6 | Validar se faz sentido pro projeto |
| 🔵 **Menor (<100%)** | 14 | Normal, variação de mercado |

## 🔴 BUGS identificados (delta >1000%)

Provável causa: o `gerar_executivo_auto.py` pode estar usando o TOTAL da linha no lugar do PU em certos casos.

| Macrogrupo | Descrição | PU usado | PU esperado | Delta |
|---|---|---|---|---|
| Sistemas_Especiais | Fechamento removível de abertura no piso do elevador em madeira | R$ 3.829.20 | R$ 88.62 | **+4.221%** |
| Rev._Interno_Parede | Chapisco de argamassa preparada em obra de cimento e areia. traço 1:4. | R$ 6.31 | R$ 0.56 | **+1.028%** |

**AÇÃO**: NÃO ENTREGAR este pacote sem corrigir esses itens. Re-gerar após fix no script.

## 🟡 Atenção (delta 100-500%)

| Macrogrupo | Descrição | PU usado | PU esperado | Delta |
|---|---|---|---|---|
| Alvenaria | Chapisco externo de argamassa preparada em obra de cimento e areia. tr | R$ 6.37 | R$ 1.84 | **+246%** |
| Impermeabilização | Impermeabilização com argamassa polimérica impermeabilizante. 3 demãos | R$ 104.00 | R$ 36.26 | **+187%** |
| Impermeabilização | Mão de obra empreitada para execução de Impermeabilização Cisterna com | R$ 45.48 | R$ 16.50 | **+176%** |
| Rev._Interno_Parede | Chapisco interno de argamassa pré-fabricada adesiva de cimento colante | R$ 15.31 | R$ 6.34 | **+141%** |
| Infraestrutura | Escavação mecanizada para blocos de fundação e vigas baldrame. com pre | R$ 78.98 | R$ 34.84 | **+127%** |
| Sistemas_Especiais | Pintura com tinta látex acrílica em fosso do elevador. 1 demão * | R$ 4.80 | R$ 2.25 | **+113%** |

## 📊 Comparação com novos índices derivados (Fase 13)

Faixas P10-P90 da base de 126 projetos:

| Índice derivado | Mediana base | Valor esperado × AC | n projetos |
|---|---|---|---|
| custo_concreto_rsm2 | R$ 228.90/m² | R$ 933.278 | 64 |
| custo_aco_rsm2 | R$ 231.82/m² | R$ 945.178 | 65 |
| custo_forma_rsm2 | R$ 164.98/m² | R$ 672.665 | 69 |
| custo_escoramento_rsm2 | R$ 47.67/m² | R$ 194.382 | 57 |
| custo_impermeabilizacao_rsm2 | R$ 264.88/m² | R$ 1.079.978 | 95 |
| custo_elevador_rsm2 | R$ 213.33/m² | R$ 869.805 | 70 |
| custo_esquadrias_rsm2 | R$ 1154.33/m² | R$ 4.706.548 | 96 |
| custo_pintura_rsm2 | R$ 594.46/m² | R$ 2.423.779 | 96 |
| custo_loucas_rsm2 | R$ 109.76/m² | R$ 447.516 | 76 |
| ci_total_rsm2 | R$ 305.56/m² | R$ 1.245.875 | 55 |

## 📋 Recomendações

1. **BLOQUEANTE**: corrigir os 2 bugs de PU antes de entregar o pacote ao cliente
2. **Investigar**: rodar script de debug no `gerar_executivo_auto.py` pra ver onde o TOTAL está virando PU
4. **Validar** os 6 itens em atenção — podem refletir escolha técnica (ex: acabamento alto-padrão)
5. **Cruzar** os totais por macrogrupo do pacote com a tabela de índices derivados acima
6. **Considerar v2** dos pacotes após fix dos bugs — comparar valores antigos × novos

## 🔗 Arquivos relacionados

- `base/pacotes/placon-arminio-tavares/revisao-pus-cross.md` — revisão original de PUs
- `base/pacotes/placon-arminio-tavares/audit-placon-arminio-tavares.md` — audit anterior (v1)
- `base/itens-pus-agregados.json` — base cross-projeto Fase 10
- `base/indices-derivados-v2.json` — 29 novos índices derivados
- `base/base-indices-master-2026-04-13.json` — base master consolidada
