# Fase 12 — Ground Truth de Cidade + Data Base + Tipologia

**Gerado:** 2026-04-19T09:14:02

## Resumo

- Entregas com ground truth extraído: **129**
- Projetos atualizados: **83**
- Data base populada (antes era null): **83**
- Divergências cidade encontradas: **0**

---

## Impacto

Antes da Fase 12: cidade via **mapa manual** (inferência de cliente, não dado real).

Depois da Fase 12: cidade via **leitura da capa do PDF/XLSX da entrega** (ground truth).

Vantagens:
- Cidade correta mesmo quando cliente tem obra em lugar inesperado
- Data base = mês de referência do CUB → permite normalização temporal
- Total e R$/m² diretos da entrega (mais confiáveis que indices-executivo)

## Slugs de entrega sem match na base enriquecida (7)

Esses projetos estão no Drive mas não em `indices-executivo/`. Possíveis entregas não-importadas.

- `essege-dom`
- `eze-canto-grande`
- `holze-nouve`
- `inbrasul-amber`
- `mabrem-liberato`
- `pavitec-siena`
- `rosner-alameda-jardins`