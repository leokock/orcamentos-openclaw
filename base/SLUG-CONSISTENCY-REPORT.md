# Relatorio de Consistencia de Slug — Paramétrico ↔ Executivo

**Gerado:** 2026-04-18T10:25:09
**Paramétricos na base:** 4 (`base/pacotes/`)
**Executivos na base:** 126 (`base/indices-executivo/`)

---

## Status atual

- ✓ Pares **exact match** (mesmo slug em ambos): **0**
- ⚠ Pares **partial match** (slugs similares, possivelmente mesmo projeto): **0**
- ✗ Paramétricos **sem executivo** (projetos em andamento): **4**
- ✗ Executivos **sem paramétrico** (projetos legados): **126**

## Paramétricos sem executivo (projetos em andamento)

| Slug | AC | Padrão | Etapa | Gate OK |
|---|---:|---|---|---|
| `arthen-arboris` | 12472.98 | medio-alto | completo | ✓ |
| `pacote-piloto` | 15000.0 | alto | completo | ✓ |
| `placon-arminio-tavares` | 4089.72 | medio | completo | ✓ |
| `thozen-electra` | 37893.89 | alto | completo | ✓ |

**Ação:** quando executivo for fechado, **manter o MESMO slug** em `indices-executivo/{slug}.json` pra criar par rastreável.

## Executivos sem paramétrico — legado

Total: 126 projetos. Não é problema — só não será possível medir erro paramétrico retroativo.

---

## Protocolo pra manter consistência

Ao fechar um paramétrico:
1. Registrar `slug` canônico no `state.json`
2. **Reusar o mesmo slug** ao iniciar o executivo
3. Rodar `python scripts/check_slug_consistency.py` periodicamente
4. Quando houver par: rodar `python scripts/comparar_param_exec.py --slug X`

Métrica de sucesso (de CLUSTER3-E-PARAMETRICO-RESUMO.md):
- 1 par rastreável até 30/jun/2026
- 5 pares até 31/dez/2026
- 20 pares = modelo preditivo de erro viável
