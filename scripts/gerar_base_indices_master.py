#!/usr/bin/env python3
"""Phase 15 — Consolida TODOS os índices e dados em base-indices-master.json.

Lê:
- calibration-indices.json (V2 original)
- indices-derivados-v2.json (Fase 13)
- base-pus-cartesian.json (V2 original)
- itens-pus-agregados.json (Fase 10 v2)
- curva-abc-master.json (Fase 11)
- por_segmento do calibration
- por_macrogrupo do calibration
- cross-insights (Fase 5)

Gera um JSON unificado com TODOS os índices do sistema, versionado.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT = BASE / f"base-indices-master-{datetime.now().strftime('%Y-%m-%d')}.json"


def load(path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"_error": str(e)}


def main():
    print("loading all data sources...")

    cal = load(BASE / "calibration-indices.json") or {}
    derivados = load(BASE / "indices-derivados-v2.json") or {}
    pus_base = load(BASE / "base-pus-cartesian.json") or {}
    pus_novos = load(BASE / "itens-pus-agregados.json") or {}
    curva_master = load(BASE / "curva-abc-master.json") or {}

    cross_dir = BASE / "cross-insights"
    cross = {}
    if cross_dir.exists():
        for fp in cross_dir.glob("*.json"):
            try:
                cross[fp.stem] = load(fp)
            except Exception:
                pass

    print(f"  calibration keys: {list(cal.keys())[:6]}")
    print(f"  derivados indices: {len(derivados.get('indices', {}))}")
    print(f"  pus base entries: {len(pus_base) if isinstance(pus_base, dict) else 0}")
    print(f"  pus novos clusters: {len(pus_novos.get('pus_agregados', [])) if isinstance(pus_novos, dict) else 0}")
    print(f"  cross insights: {list(cross.keys())}")

    master = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "version": "v3",
        "description": (
            "Base consolidada de índices da Cartesian — inclui todos os índices "
            "originais V2 + novos derivados v2 (Fase 13) + PUs cross-projeto agregados "
            "(Fase 10) + curvas ABC (Fase 11) + cross-insights (Fase 5). "
            "Fonte autoritativa para geração de orçamentos."
        ),
        "counts": {
            "indices_v2_produto": len((cal.get("produto") or {})),
            "indices_v2_estruturais": len((cal.get("estruturais") or {})),
            "indices_v2_instalacoes": len((cal.get("instalacoes") or {})),
            "indices_v2_ci": len((cal.get("ci") or {})),
            "indices_v2_macrogrupo": len((cal.get("por_macrogrupo") or {})),
            "indices_v2_segmento": len((cal.get("por_segmento") or {})),
            "indices_derivados_v2": len(derivados.get("indices", {})),
            "pus_agregados": len(pus_novos.get("pus_agregados", []) if isinstance(pus_novos, dict) else []),
            "curvas_abc_projetos": curva_master.get("n_projetos", 0),
            "cross_insights_sections": len(cross),
        },
        "indices_v2_original": cal,
        "indices_derivados_v2": derivados.get("indices", {}),
        "pus_agregados_top_500": sorted(
            pus_novos.get("pus_agregados", []) if isinstance(pus_novos, dict) else [],
            key=lambda x: -x.get("n_observacoes", 0),
        )[:500],
        "curva_abc_master": curva_master,
        "cross_insights": cross,
    }

    OUT.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")
    size_kb = OUT.stat().st_size // 1024
    print(f"\nsaved: {OUT} ({size_kb} KB)")

    readme = BASE / f"base-indices-master-{datetime.now().strftime('%Y-%m-%d')}-README.md"
    readme.write_text(f"""# Base de Índices Master — {datetime.now().strftime('%Y-%m-%d')}

Consolidação de TODOS os índices do sistema Cartesian em um único arquivo JSON.

## Conteúdo

| Seção | Origem | Qtd |
|---|---|---|
| `indices_v2_original` | calibration-indices.json | V2 completo |
| `indices_derivados_v2` | Fase 13 (gerar_novos_indices.py) | {len(derivados.get('indices', {}))} novos índices |
| `pus_agregados_top_500` | Fase 10 (normalize_descriptions.py) | Top 500 de 4.525 PUs |
| `curva_abc_master` | Fase 11 (extract_curvas_abc.py) | {curva_master.get('n_projetos', 0)} projetos |
| `cross_insights` | Fase 5 (phase5_cross_insights.py) | {len(cross)} análises Gemma |

## Tamanho total
{size_kb} KB

## Como consultar

```python
import json
master = json.load(open("{OUT.name}"))

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
""", encoding="utf-8")
    print(f"readme: {readme}")


if __name__ == "__main__":
    main()
