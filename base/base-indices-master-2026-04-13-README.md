# Base de Índices Master — 2026-04-13

Consolidação de TODOS os índices do sistema Cartesian em um único arquivo JSON.

## Conteúdo

| Seção | Origem | Qtd |
|---|---|---|
| `indices_v2_original` | calibration-indices.json | V2 completo |
| `indices_derivados_v2` | Fase 13 (gerar_novos_indices.py) | 29 novos índices |
| `pus_agregados_top_500` | Fase 10 (normalize_descriptions.py) | Top 500 de 4.525 PUs |
| `curva_abc_master` | Fase 11 (extract_curvas_abc.py) | 125 projetos |
| `cross_insights` | Fase 5 (phase5_cross_insights.py) | 5 análises Gemma |

## Tamanho total
322 KB

## Como consultar

```python
import json
master = json.load(open("base-indices-master-2026-04-13.json"))

# Índices derivados novos (Fase 13)
for nome, stats in master["indices_derivados_v2"].items():
    print(nome, stats["mediana"])

# PUs agregados cross-projeto (Fase 10)
for p in master["pus_agregados_top_500"][:10]:
    print(p["desc"], p["pu_mediana"], p["n_observacoes"])

# Consultar outliers estruturais identificados por Gemma (Fase 5)
outliers = master["cross_insights"]["outliers"]
```

Gerado por `scripts/gerar_base_indices_master.py`.
