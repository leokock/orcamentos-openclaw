# Insumos — Catálogo de itens

## O que é

**Insumo** = item individual com preço unitário (ex.: "saco de cimento CP-II 50kg",
"hora de pedreiro", "m² de bloco cerâmico"). É a granularidade mínima do custo.

## Estrutura da aba `insumos.xlsx`

| Coluna | Conteúdo |
|---|---|
| Código | ID único do insumo |
| Descrição | Nome do insumo |
| Unidade | un, m², m³, kg, h, vb, etc. |
| Preço unitário | R$ |
| Fonte preço | Sinapi, mercado, cotação direta |
| Última atualização | Data |

## Como composições consomem insumos

Cada composição tem uma lista de "insumo + coeficiente":
- Ex.: composição "1 m² de alvenaria" pode consumir:
  - 12,5 blocos cerâmicos (insumo BLO-001 × coef 12,5)
  - 0,025 m³ de argamassa (insumo ARG-002 × coef 0,025)
  - 0,5 h de pedreiro (insumo MO-005 × coef 0,5)
  - 0,3 h de servente (insumo MO-006 × coef 0,3)

Custo unitário da composição = soma de (insumo.preço × coef).

## Hierarquia preço

1. **Insumo** (preço unitário)
2. **Composição** (custo por unidade do serviço, calculado dos insumos)
3. **CPU** (Custo Por Unidade pré-calculado, vem de Composição × quantidade ou similar)
4. **Serviço da EAP** = composição × quantidade extraída do projeto

## Workflow de revisão

- Atualizar **insumos.xlsx** quando preços de mercado mudarem (CUB/SC ou cotação direta)
- Composições recalculam automaticamente (planilha tem fórmulas)
- Validar com `cpu.xlsx` se valores agregados batem
