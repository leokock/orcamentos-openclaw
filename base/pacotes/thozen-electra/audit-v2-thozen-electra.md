# Audit V2 — thozen-electra

_Gerado em 13/04/2026 22:58 — revisão com base enriquecida (Fases 8-15)_

## 🎯 Contexto

- **AC**: 37.894 m²
- **UR**: 348
- Fontes novas consultadas:
  - `itens-pus-agregados.json` — 4.525 PUs cross-projeto (Fase 10)
  - `indices-derivados-v2.json` — 29 novos índices derivados (Fase 13)
  - `base-indices-master-2026-04-13.json` — base consolidada (Fase 15)

## 🚨 Gravidade dos outliers

| Categoria | Qtd | Ação sugerida |
|---|---|---|
| 🔴 **BUG (>1000% delta)** | 0 | Investigar origem — provável erro de extração |
| 🟠 **Crítico (500-1000%)** | 2 | Revisar manualmente antes de entregar |
| 🟡 **Atenção (100-500%)** | 3 | Validar se faz sentido pro projeto |
| 🔵 **Menor (<100%)** | 20 | Normal, variação de mercado |

## 🟠 Críticos (delta 500-1000%)

| Macrogrupo | Descrição | PU usado | PU esperado | Delta |
|---|---|---|---|---|
| Louças_e_Metais | Acabamento de Registro | R$ 493.70 | R$ 50.00 | **+887%** |
| Alvenaria | Encunhamento De Alvenaria De Vedação Com Argamassa Expansiva | R$ 15.04 | R$ 2.37 | **+535%** |

## 🟡 Atenção (delta 100-500%)

| Macrogrupo | Descrição | PU usado | PU esperado | Delta |
|---|---|---|---|---|
| Pintura | Mao De Obra Para Pintura Acrilica Em Paredes. 3 Demaos | R$ 32.00 | R$ 8.43 | **+280%** |
| Esquadrias | Guarda Corpo de Vidro e Aluminio - fornecimento e instalação | R$ 2.150.99 | R$ 768.50 | **+180%** |
| Teto | Forro de madeira - material e mão de obra | R$ 579.00 | R$ 250.00 | **+132%** |

## 📊 Comparação com novos índices derivados (Fase 13)

Faixas P10-P90 da base de 126 projetos:

| Índice derivado | Mediana base | Valor esperado × AC | n projetos |
|---|---|---|---|
| custo_concreto_rsm2 | R$ 228.90/m² | R$ 8.673.783 | 64 |
| custo_aco_rsm2 | R$ 231.82/m² | R$ 8.784.380 | 65 |
| custo_forma_rsm2 | R$ 164.98/m² | R$ 6.251.677 | 69 |
| custo_escoramento_rsm2 | R$ 47.67/m² | R$ 1.806.568 | 57 |
| custo_impermeabilizacao_rsm2 | R$ 264.88/m² | R$ 10.037.201 | 95 |
| custo_elevador_rsm2 | R$ 213.33/m² | R$ 8.083.869 | 70 |
| custo_esquadrias_rsm2 | R$ 1154.33/m² | R$ 43.742.145 | 96 |
| custo_pintura_rsm2 | R$ 594.46/m² | R$ 22.526.337 | 96 |
| custo_loucas_rsm2 | R$ 109.76/m² | R$ 4.159.161 | 76 |
| ci_total_rsm2 | R$ 305.56/m² | R$ 11.579.024 | 55 |

## 📋 Recomendações

3. **Revisar manualmente** os 2 itens críticos — podem ser variantes legítimas ou erros
4. **Validar** os 3 itens em atenção — podem refletir escolha técnica (ex: acabamento alto-padrão)
5. **Cruzar** os totais por macrogrupo do pacote com a tabela de índices derivados acima
6. **Considerar v2** dos pacotes após fix dos bugs — comparar valores antigos × novos

## 🔗 Arquivos relacionados

- `base/pacotes/thozen-electra/revisao-pus-cross.md` — revisão original de PUs
- `base/pacotes/thozen-electra/audit-thozen-electra.md` — audit anterior (v1)
- `base/itens-pus-agregados.json` — base cross-projeto Fase 10
- `base/indices-derivados-v2.json` — 29 novos índices derivados
- `base/base-indices-master-2026-04-13.json` — base master consolidada
