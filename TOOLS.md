# TOOLS.md - Cartesiano Local Notes

## Memorial Cartesiano — Supabase (App de Orçamento)

### Credenciais
- Arquivo: `.env.sensitive` (gitignored)
- Variáveis: `MEMORIAL_SUPABASE_URL`, `MEMORIAL_SUPABASE_ANON`, `MEMORIAL_EMAIL`, `MEMORIAL_PASSWORD`

### Autenticação
O Supabase do Memorial usa RLS. Precisa autenticar com email/senha pra obter JWT:

```bash
source .env.sensitive

# 1. Obter token JWT
TOKEN=$(curl -s "${MEMORIAL_SUPABASE_URL}/auth/v1/token?grant_type=password" \
  -H "apikey: ${MEMORIAL_SUPABASE_ANON}" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"${MEMORIAL_EMAIL}\",\"password\":\"${MEMORIAL_PASSWORD}\"}" | python3 -c "import json,sys; print(json.load(sys.stdin)['access_token'])")

# 2. Usar token nas requests
curl -s "${MEMORIAL_SUPABASE_URL}/rest/v1/TABELA?select=*&limit=10" \
  -H "apikey: ${MEMORIAL_SUPABASE_ANON}" \
  -H "Authorization: Bearer ${TOKEN}"
```

### Tabelas Principais (Orçamento)
- `budgets` — orçamentos
- `budget_items` — itens do orçamento (EAP/WBS)
- `budget_versions` — versões do orçamento
- `budget_support_spreadsheets` — planilhas de apoio
- `composicoes` — composições de preço unitário (CPUs)
- `composicoes_items` — itens das composições
- `insumos` — insumos com preços
- `insumo_price_history` — histórico de preços

### Tabelas Projeto
- `projects` — projetos
- `clients` — clientes
- `project_floors` — pavimentos
- `project_towers` — torres
- `project_building_data` — dados da edificação
- `project_indices` — índices do projeto
- `project_premises` — premissas

### Tabelas Quantitativo
- `quantitativo_items` — itens quantitativos
- `quantitativo_versions` — versões quantitativo
- `quantitativo_allocations` — alocações

### Tabelas Questionário/Briefing
- `questionnaires` — questionários
- `questionnaire_sections` — seções
- `questionnaire_questions` — perguntas
- `question_answers` — respostas

### RPCs Úteis
- `rpc/batch_insert_quantitativo_items` — inserir itens em lote
- `rpc/get_quantitativo_hierarchy` — hierarquia completa
- `rpc/get_total_budget_value` — valor total do orçamento
- `rpc/recalculate_all_budget_totals` — recalcular totais

### User ID do Leo
- `ffb7fc3d-032b-413f-bfa9-456f307c4350`

### Exemplo: Listar projetos
```bash
curl -s "${MEMORIAL_SUPABASE_URL}/rest/v1/projects?select=id,name,client_id&limit=10" \
  -H "apikey: ${MEMORIAL_SUPABASE_ANON}" \
  -H "Authorization: Bearer ${TOKEN}"
```

### Exemplo: Inserir item no orçamento
```bash
curl -s "${MEMORIAL_SUPABASE_URL}/rest/v1/budget_items" \
  -H "apikey: ${MEMORIAL_SUPABASE_ANON}" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{"budget_id":"...","description":"...","unit":"m2","quantity":100,"unit_price":50.00}'
```

---

## Why Separate?

Skills are shared. Your setup is yours.
