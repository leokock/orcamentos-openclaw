---
tags: [custos-ia-parametrico, arthen-arboris, decision, analise-alternativa]
projeto: arthen-arboris
data: 2026-04-20
---

# Arthen Arboris — Alternativa: Forro Gesso Mineral vs Acartonado

Análise da versão alternativa do paramétrico do **Arthen Arboris** (Itapema/SC, 12.472,98 m² AC, 98 UR, Padrão Médio-Alto, Entrega Completa) testando a substituição do forro de **gesso acartonado** por **gesso mineral** nas áreas secas.

## Resumo executivo

| Indicador | v00-final (acartonado) | alt-v01 (mineral) | Delta |
|---|---:|---:|---:|
| **Macrogrupo Teto** | R$ 905.729 | R$ 699.534 | **-R$ 206.195** (-22,8%) |
| **Custo Total** | R$ 39.728.474 | R$ 39.522.280 | **-R$ 206.195** (-0,52%) |
| **R$/m² AC** | R$ 3.185,16 | R$ 3.168,63 | -R$ 16,53 |
| **Economia/UR** (98 UR) | — | — | **R$ 2.104/UR** |

**Conclusão:** trocar gesso acartonado por mineral nas áreas secas gera **economia de ~R$ 206k** no macrogrupo Teto. O impacto no custo total do paramétrico é pequeno (-0,52%), mas o macrogrupo Teto fica **23% mais barato**. Ganhos adicionais não monetários em instalação (mais rápida) e acústica.

## Quebra do cálculo

### Premissa comum
- Índice forro: **1,16 m²/m² AC** (INDICES!D16 — entrega Completa = shell×1,00)
- Quantidade total de forro: **14.469 m²** = 1,16 × 12.472,98
- Split assumido no paramétrico original: 70% áreas secas, 15% BWC, 85% estrutura drywall, 100% MO

### v00-final — gesso acartonado (atual)

| Item | Qtd | PU | Total |
|---|---:|---:|---:|
| Forro ST (acartonado áreas secas, 70%) | 10.128 m² | R$ 28 | R$ 283.584 |
| Forro RU (BWC molhadas, 15%) | 2.170 m² | R$ 35 | R$ 75.950 |
| Perfis (estrutura drywall, 85%) | 12.298 m² | R$ 15 | R$ 184.470 |
| MO (empreitada, 100%) | 14.469 m² | R$ 25 | R$ 361.725 |
| **Total Teto** | | | **R$ 905.729** |

**Composição unitária efetiva acartonado áreas secas:** R$ 28 (material) + R$ 15 (perfil) + R$ 25 (MO) = **R$ 68/m² completo**.

### alt-v01 — gesso mineral (proposta)

| Item | Qtd | PU | Total |
|---|---:|---:|---:|
| Forro Mineral (áreas secas, 70%) | 10.128 m² | **R$ 53** | R$ 536.784 |
| Forro RU (BWC, acartonado mantido, 15%) | 2.170 m² | R$ 35 | R$ 75.950 |
| Perfis (só BWC, 15%) | 2.170 m² | R$ 15 | R$ 32.550 |
| MO (só BWC, 15%) | 2.170 m² | R$ 25 | R$ 54.250 |
| **Total Teto** | | | **R$ 699.534** |

**Composição unitária efetiva mineral áreas secas:** R$ 53 (material + instalação inclusa) = **R$ 53/m² completo**.

**Delta por m² de forro em áreas secas: -R$ 15/m² (-22% vs acartonado)**.

## Fontes dos índices (Supabase `indices-cartesian`)

Consulta SQL na tabela `pus_cross_v2`:

| Cluster | Descrição | n_proj | n_obs | mediana | cv |
|---:|---|---:|---:|---:|---:|
| 3781 | **Forro de gesso mineral — material e instalação** | 2 | 16 | **R$ 53,00** | 0,049 |
| 826 | Forro gesso acartonado áreas secas — mat+MO | 15 | 61 | R$ 96,60 | 0,534 |
| 1396 | Forro gesso acartonado áreas molhadas — mat+MO | 13 | 30 | R$ 103,55 | 0,077 |
| 2674 | Forro gesso liso áreas secas — mat+MO | 3 | 23 | R$ 36,00 | 0,181 |

**⚠ Nota sobre confiança do PU mineral:** Supabase tem só `n_proj=2` e `n_obs=16` pro cluster 3781, mas o `cv=0,049` (baixíssima variação) indica consistência nos poucos pontos existentes. Validar com fornecedor local (Itapema/SC) antes de fechar.

**⚠ Benchmark acartonado — o paramétrico v00 usa PU R$ 68 (desagregado) mas o mercado (Supabase mediana) está em R$ 96,60/m² completo.** A versão alt-mineral a R$ 53 é ainda mais competitiva se calibrada contra o mercado real.

## Vantagens do gesso mineral

1. **Custo**: ~22% mais barato que acartonado (na composição completa)
2. **Velocidade de instalação**: aplicação direta na laje, sem estrutura metálica
3. **Acústica**: melhor absorção sonora que gesso ST
4. **Monolítico**: sem juntas aparentes
5. **Resistência ao fogo**: mineral (carbonato/sílica) tem maior resistência térmica

## Limitações que precisam ser verificadas

1. **Áreas molhadas**: **não aplicável em BWC** — o paramétrico alt mantém acartonado RU nas 15% de área molhada
2. **Instalações embutidas**: gesso mineral é aplicado como massa contínua → **impossível passar eletrodutos, sprinklers, iluminação embutida** após instalação. Isso precisa ser resolvido no projeto hidrossanitário/elétrico antes da execução
3. **Acesso de manutenção**: qualquer reparo em tubulação obriga quebrar o forro mineral (diferente do drywall modular)
4. **Qualidade da base**: mineral aplicado direto na laje exige **laje bem executada** (sem desníveis > 5mm/m); se a estrutura tiver muita variação, o consumo de material aumenta
5. **Disponibilidade em SC/Itapema**: fornecedor local precisa ser cotado (Supabase tem só 2 projetos — validar)

## Recomendações

1. **Usar alt-v01 como referência de negociação** com a obra/cliente — pode abrir desconto de até R$ 200k se mantido padrão Médio-Alto
2. **Validar com projeto de instalações** antes de decidir — se tem iluminação sancada/cortineiro, fita LED ou sprinklers no forro, o mineral pode não ser viável (ou exigir composição mista)
3. **Cotar com 2-3 fornecedores locais** (Itapema/Balneário Camboriú/Itajaí) pra validar o PU R$ 53 do Supabase
4. **Considerar composição híbrida**: mineral nos quartos/sala (áreas "limpas") + acartonado nas áreas de circulação/hall (onde passa mais instalação)

## Arquivos gerados

- **xlsx alternativo:** [`arthen-arboris-parametrico-alt-gesso-mineral-v01.xlsx`](../../../../orcamentos/parametricos/arthen-arboris/arthen-arboris-parametrico-alt-gesso-mineral-v01.xlsx) — cópia do v00-final com aba Teto modificada + nota na aba PREMISSAS
- **script gerador:** [`gerar_parametrico_alt_gesso_mineral.py`](./gerar_parametrico_alt_gesso_mineral.py) — idempotente, re-executa qualquer hora

## Para regenerar com outros PUs

Editar as constantes no topo do script:
```python
PU_GESSO_MINERAL = 53  # cluster 3781 Supabase
PU_GESSO_RU = 35
PU_PERFIL = 15
PU_MO = 25
```
E rodar: `PYTHONIOENCODING=utf-8 py -3.10 gerar_parametrico_alt_gesso_mineral.py`

## Quando abrir no Excel

Os totais do PAINEL e da aba CUSTOS_MACROGRUPO **vão recalcular automaticamente** ao abrir o xlsx no Excel (as fórmulas seguem `=SUM(F4:F7)` e afins). Se Leo salvar de novo no Excel, os valores ficam persistidos pro próximo consumer.

## Log de consulta Supabase (esta análise)

```sql
SELECT cluster_id, descricao, n_proj, n_obs,
       pu_min, pu_p25, pu_mediana, pu_p75, pu_max, cv
FROM pus_cross_v2
WHERE descricao ILIKE '%gesso mineral%'
   OR descricao ILIKE '%gesso acartonado%';
```

Rodado em 2026-04-20 via MCP `mcp__claude_ai_Supabase__execute_sql` com `project_id=nzyyptcfiqalhpybklfd`.
