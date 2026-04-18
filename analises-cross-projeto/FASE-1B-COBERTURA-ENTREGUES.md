# Fase 1b — Cobertura de Entregues vs Base

**Gerado:** 2026-04-18T13:29:39
**Path entregues:** `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo`
**Total entregas no Drive:** 130 (obra por cliente)
**Total slugs na base:** 126

## Resumo

- ✓ Pares exatos: **121**
- ⚠ Pares parciais (revisar): **4**
- ✗ Entregas faltantes (importar): **5**
- 🔍 Órfãos na base (slug nao tem entrega): **5**

---

## Entregas faltantes (a importar)

| Cliente | Obra | Slug sugerido | Arquivos |
|---|---|---|---:|
| Essege | Dom | `essege-dom` | 2 |
| EZE | Canto Grande | `eze-canto-grande` | 2 |
| Pavitec | Siena | `pavitec-siena` | 5 |
| Rosner | Alameda Jardins | `rosner-alameda-jardins` | 5 |
| Serati | Manhatan | `serati-manhatan` | 0 |

## Pares parciais (REVISAR MANUALMENTE)

Entregas com slug similar a um slug existente — podem ser o mesmo projeto com grafia diferente, ou projetos diferentes. Verificar antes de agir.

| Entrega (Cliente/Obra) | Slug canônico | Slug base similar | Sim |
|---|---|---|---:|
| Holze/Nouve | `holze-nouve` | `holze-sense-106` | 0.61 |
| Inbrasul/Amber | `inbrasul-amber` | `inbrasul-opus` | 0.67 |
| Mabrem/Liberato | `mabrem-liberato` | `mabrem-gran-torino` | 0.67 |
| Santa Maria/We | `santa-maria-we` | `santa-maria-z` | 0.89 |

## Órfãos na base (slug não tem entrega correspondente)

Esses projetos foram processados mas a pasta Entregas não os contém — possível slug errado na base ou entrega movida.

| Slug base | AC (m²) | Total (R$) |
|---|---:|---:|
| `cambert-portal-da-brava` | — | — |
| `nm-empreendimentos` | 1,541 | R$ 4,958,344 |
| `nobria` | 12,880 | R$ 42,384,127 |
| `pavcor` | 14,283 | R$ 49,360,279 |
| `sak-engenharia` | 1,701 | R$ 6,535,457 |

---

## Próximos passos

1. **Revisar pares parciais:** decidir quais são o mesmo projeto (renomear slug na base pra casar)
2. **Importar faltantes:** rodar `scripts/importar_entregues_faltantes.py` ou processar manualmente
3. **Investigar órfãos:** decidir se mantém na base ou remove (pode ser projeto nao-entregue, orcamento de teste, etc)
4. **Re-rodar Fase 1 + Fase 3** nos novos slugs após importação
5. **Validar cobertura final:** rodar esse auditor de novo pra garantir cobertura 100%
