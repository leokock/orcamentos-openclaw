"""Protocolo de coleta do MongoDB Cartesian via MCP `cartesian-mongodb`.

Este script DOCUMENTA e VALIDA o pacote de dumps que o bot Cartesiano deve gerar
ANTES de rodar `precificar_pool_cartesian.py`.

NOTA: a coleta em si é feita pelo bot via tools MCP `mcp__c62301cb-…__*`
(prefixo varia por instância). Este script só:
  1. lista o que deve existir no dump dir
  2. valida que cada arquivo é JSON parseável
  3. checa se há volume mínimo (warning se PO < 5000 ou resources < 30000)

Estrutura esperada em `executivos/[slug]/_tmp/precificacao/cartesian-raw/`:

  buildings.json
      Saída de: mcp__cartesian-mongodb__listar_obras (ou collection 'buildings')
      Shape: [{"id": str, "name": str, "company": str, ...}, ...]

  purchase_orders_items_full.json
      Saída de: consultar_collection('purchase_orders_items') com projeção
      {resource_description, unit_of_measure, unit_price, building_id, date}
      Cobertura: ~6.500 itens em ~3 obras com BI denso

  resources_batch1.json ... resources_batch4.json
      Saída de: consultar_collection('resources') paginado, ~15k por batch
      Projeção: {description, unit_of_measure, unit_price, building_id, measurement_date}
      Cobertura: ~60k itens em ~50 obras

Wrapper MCP nos formatos:
  - mcp_returns: {"result": "JSON_string"}  (parse 2x — load_mcp_result no pool)
  - direct: [..., ...]  (parse 1x)

Ambos suportados pelo `precificar_pool_cartesian.load_mcp_result`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from precificar_common import tmp_dir

REQUIRED_FILES = [
    "buildings.json",
    "purchase_orders_items_full.json",
]
RESOURCES_GLOB = "resources_batch*.json"

MIN_PO_ITEMS = 5000
MIN_RESOURCES_TOTAL = 30000


def _peek_count(path: Path) -> int:
    """Conta items num dump (suporta wrapper {result: JSON_string})."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return -1
    if isinstance(data, dict) and "result" in data:
        try:
            data = json.loads(data["result"])
        except Exception:
            return -1
    if isinstance(data, list):
        return len(data)
    return -1


def validate(slug: str) -> bool:
    raw_dir = tmp_dir(slug) / "cartesian-raw"
    if not raw_dir.exists():
        print(f"❌ Pasta {raw_dir} não existe.")
        print("   Bot Cartesiano deve coletar dumps via MCP cartesian-mongodb antes.")
        return False

    ok = True
    print(f"Validando {raw_dir}/")
    for fname in REQUIRED_FILES:
        p = raw_dir / fname
        if not p.exists():
            print(f"  ❌ {fname} ausente")
            ok = False
            continue
        n = _peek_count(p)
        print(f"  ✓  {fname}: {n} itens")
        if fname == "purchase_orders_items_full.json" and 0 <= n < MIN_PO_ITEMS:
            print(f"     ⚠ esperado ≥ {MIN_PO_ITEMS}, encontrado {n}")

    batches = sorted(raw_dir.glob(RESOURCES_GLOB))
    if not batches:
        print(f"  ❌ Nenhum resources_batch*.json encontrado")
        ok = False
    else:
        total = 0
        for b in batches:
            n = _peek_count(b)
            print(f"  ✓  {b.name}: {n} itens")
            if n > 0:
                total += n
        if total < MIN_RESOURCES_TOTAL:
            print(f"     ⚠ resources total {total} < esperado {MIN_RESOURCES_TOTAL}")

    if ok:
        print(f"\n✓ Dump pronto. Próximo passo: python scripts/precificacao/precificar_pool_cartesian.py --slug {slug}")
    return ok


def print_collection_protocol():
    """Imprime instruções pro bot coletar via MCP."""
    print("""
=== PROTOCOLO DE COLETA (executado pelo bot Cartesiano via MCP) ===

1. Listar obras (uma vez, dump completo):
   tool: mcp__cartesian-mongodb__listar_obras
   args: {}
   write: cartesian-raw/buildings.json

2. Purchase orders items (preço PAGO real — fonte primária):
   tool: mcp__cartesian-mongodb__consultar_collection
   args: {
     "collection": "purchase_orders_items",
     "projection": {"resource_description":1, "unit_of_measure":1, "unit_price":1, "building_id":1, "date":1},
     "limit": 50000
   }
   write: cartesian-raw/purchase_orders_items_full.json

3. Resources (orçamento estimado — fonte secundária, paginar em batches):
   loop batch_idx in 1..N (até esgotar):
     tool: mcp__cartesian-mongodb__consultar_collection
     args: {
       "collection": "resources",
       "projection": {"description":1, "unit_of_measure":1, "unit_price":1, "building_id":1, "measurement_date":1},
       "skip": (batch_idx-1)*15000,
       "limit": 15000
     }
     write: cartesian-raw/resources_batch<batch_idx>.json
     se len < 15000: parar (fim dos dados)

4. Validar: python scripts/precificacao/precificar_dump_mongo.py --slug <SLUG> --validate

Cache TTL recomendado: 24h. Reusar dump existente se mtime < 24h.
""".strip())


def main():
    ap = argparse.ArgumentParser(description="Protocolo de dump MongoDB Cartesian")
    ap.add_argument("--slug", help="Validar dump existente")
    ap.add_argument("--validate", action="store_true", help="Modo validação")
    ap.add_argument("--protocol", action="store_true", help="Imprimir protocolo MCP")
    args = ap.parse_args()

    if args.protocol or not (args.slug or args.validate):
        print_collection_protocol()
        return

    if args.slug:
        ok = validate(args.slug)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
