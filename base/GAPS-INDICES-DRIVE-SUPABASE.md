---
tags: [custos-ia-parametrico, analise, supabase, gap-analysis]
data: 2026-04-20
---

# Gaps: Drive Entregas/Orçamento_executivo ↔ Supabase `indices-cartesian`

Análise cruzada entre as pastas do Drive compartilhado e a tabela `projetos`
no Supabase, pra identificar projetos executivos entregues que ainda não
foram calibrados/ingeridos na base de índices.

- **Drive:** `_Entregas/Orçamento_executivo/{cliente}/{projeto}/` — 134 pastas
- **Supabase:** tabela `projetos` — 126 linhas
- **Casados:** 125
- **⚠ Gaps (faltam mapear):** 9
- **Fantasmas (Supabase sem pasta no Drive):** 1

## [1] Projetos FALTAM MAPEAR no Supabase

Executivos entregues que ainda não viraram índice. **Priorização por data de modificação no Drive** (mais recente = provavelmente mais atual).

| # | Prioridade | Cliente / Projeto | Slug esperado | Modificado | Arquivos | Formato |
|---:|---|---|---|---|---:|---|
| 1 | 🔥 **alta** | Pavitec / Siena | `pavitec-siena` | 2026-04-09 | 5 | PDF |
| 2 | 🔥 **alta** | Rosner / Alameda Jardins | `rosner-alameda-jardins` | 2026-04-09 | 5 | PDF |
| 3 | 🟡 média | EZE / Canto Grande | `eze-canto-grande` | 2026-03-11 | 4 | PDF + PPTX |
| 4 | 🟡 média | Mabrem / Liberato | `mabrem-liberato` | 2026-03-11 | 2 | PDF + PPTX |
| 5 | 🟡 média | Essege / Dom | `essege-dom` | 2026-03-11 | 2 | PDF |
| 6 | 🟡 média | Holze / Nouve | `holze-nouve` | 2026-03-11 | 2 | PDF |
| 7 | 🟡 média | Inbrasul / Amber | `inbrasul-amber` | 2026-03-11 | 1 | PDF |
| 8 | 🟡 média | Santa Maria / We | `santa-maria-we` | 2026-03-10 | 1 | PDF |
| 9 | ⚪ verificar | Serati / Manhatan | `serati-manhatan` | 2026-03-10 | **0** | pasta vazia |

**Recomendação:** começar pelos 2 de abril (Pavitec/Siena e Rosner/Alameda Jardins — têm 5 PDFs cada, entregas mais recentes) e descer pela lista. O **Serati/Manhatan está vazio** no Drive — verificar se a entrega foi cancelada antes de ingerir.


## [2] Projetos do Supabase SEM pasta no Drive

Provavelmente slugs antigos que foram renomeados ou pastas que existem mas
não foram casadas pelo fuzzy match. Revisar manualmente.

| Slug | Padrão | AC (m²) |
|---|---|---:|
| `cambert-portal-da-brava` | alto | 0.0 |


## [3] Projetos JÁ mapeados (OK)

125 projetos casados. Ver tabela `projetos` no Supabase pra detalhes.

## Próximos passos

1. Pros 9 **gaps**: decidir prioridade — entregues recentes (2026) primeiro
2. Pros executivos priorizados: rodar pipeline de extração (scripts de calibração do paramétrico V2) e ingerir no Supabase via `INSERT INTO projetos`
3. Revisar os 1 "fantasmas" — alguns podem ser só questão de nome de pasta (renomear) ou slug antigo (dedup no Supabase)
