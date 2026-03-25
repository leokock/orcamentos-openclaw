# Open Cloud Import Scoping

Guia curto para imports diretos no Supabase via Open Cloud, scripts externos ou agentes.

## Objetivo

Evitar que `insumos` e `composicoes` caiam no catálogo global por engano quando o
destino real é um cliente ou um projeto.

## Regra de Escopo

Os registros de `insumos` e `composicoes` só podem existir em um destes 3 estados:

| Escopo | source | client_id | project_id |
|-------|--------|-----------|------------|
| Catálogo global | `catalog` | `null` | `null` |
| Catálogo do cliente | `catalog` | preenchido | `null` |
| Específico do projeto | `project` | preenchido | preenchido |

Estados inválidos:

- `source = 'catalog'` com `project_id` preenchido
- `source = 'project'` com `client_id` nulo
- `source = 'project'` com `project_id` nulo

Essa regra é imposta pela constraint `insumos_client_project_consistency`.

## Regra de negócio prática

- Se o item deve aparecer em qualquer projeto do cliente: grave no catálogo do cliente.
- Se o item deve aparecer só em um projeto: grave como específico do projeto.
- Use catálogo global apenas quando o item for realmente compartilhado entre todos os clientes.

Para o caso atual:

- Cliente `Thozen`: `2297582c-660c-45c8-9c3a-84aea1b5ac01`
- Projeto `Electra Towers`: `cdff0592-fb3c-4c13-9516-efde6b56b336`

Se a intenção for "aparecer dentro do Electra e também servir como catálogo do cliente",
o escopo correto é o catálogo do cliente:

- `source = 'catalog'`
- `client_id = '2297582c-660c-45c8-9c3a-84aea1b5ac01'`
- `project_id = null`

## Exemplos de payload

### 1. Catálogo global

```json
{
  "code": "INS_01000",
  "description": "Item global",
  "type": "material",
  "unit": "UN",
  "price_cents": 1500,
  "origin_system": "import",
  "source": "catalog",
  "client_id": null,
  "project_id": null
}
```

### 2. Catálogo do cliente Thozen

```json
{
  "code": "INS_01001",
  "description": "Item do catálogo Thozen",
  "type": "material",
  "unit": "UN",
  "price_cents": 1500,
  "origin_system": "import",
  "source": "catalog",
  "client_id": "2297582c-660c-45c8-9c3a-84aea1b5ac01",
  "project_id": null
}
```

### 3. Item específico do projeto Electra Towers

```json
{
  "code": "INS_01002",
  "description": "Item exclusivo do Electra Towers",
  "type": "material",
  "unit": "UN",
  "price_cents": 1500,
  "origin_system": "import",
  "source": "project",
  "client_id": "2297582c-660c-45c8-9c3a-84aea1b5ac01",
  "project_id": "cdff0592-fb3c-4c13-9516-efde6b56b336"
}
```

## Upsert correto

A unicidade atual não é por `code` sozinho. O upsert deve respeitar:

```text
(code, client_id, project_id)
```

Em Supabase JS:

```ts
await supabase
  .from("insumos")
  .upsert(rows, {
    onConflict: "code,client_id,project_id",
    ignoreDuplicates: false
  });
```

Não usar:

```ts
onConflict: "code"
```

porque isso mistura escopos diferentes.

## SQL de referência

### Inserir em catálogo do cliente

```sql
insert into public.insumos (
  code,
  description,
  type,
  unit,
  price_cents,
  origin_system,
  source,
  client_id,
  project_id
) values (
  'INS_01001',
  'Item do catálogo Thozen',
  'material',
  'UN',
  1500,
  'import',
  'catalog',
  '2297582c-660c-45c8-9c3a-84aea1b5ac01',
  null
);
```

### Inserir como item do projeto

```sql
insert into public.insumos (
  code,
  description,
  type,
  unit,
  price_cents,
  origin_system,
  source,
  client_id,
  project_id
) values (
  'INS_01002',
  'Item exclusivo do Electra Towers',
  'material',
  'UN',
  1500,
  'import',
  'project',
  '2297582c-660c-45c8-9c3a-84aea1b5ac01',
  'cdff0592-fb3c-4c13-9516-efde6b56b336'
);
```

## Conversão de imports gravados errado como globais

Se o lote foi gravado como global e o destino correto era o catálogo do cliente:

```sql
update public.insumos
set client_id = '2297582c-660c-45c8-9c3a-84aea1b5ac01',
    source = 'catalog',
    project_id = null,
    updated_at = now()
where origin_system = 'import'
  and source = 'catalog'
  and client_id is null
  and project_id is null
  and created_at >= '2026-03-20 17:55:08.35276+00'
  and created_at <= '2026-03-20 17:56:01.9208+00';
```

Observação:

- antes do `update`, verificar códigos duplicados dentro do lote
- se houver duplicidade, renomear uma das cópias antes de mover para o catálogo do cliente

## Queries de verificação

### Quantos itens existem no catálogo do cliente

```sql
select count(*) as qty
from public.insumos
where client_id = '2297582c-660c-45c8-9c3a-84aea1b5ac01'
  and project_id is null;
```

### Quantos itens são específicos do projeto

```sql
select count(*) as qty
from public.insumos
where project_id = 'cdff0592-fb3c-4c13-9516-efde6b56b336';
```

### Escopo visível no contexto do projeto

```sql
select count(*) as qty
from public.insumos
where
  (client_id is null and project_id is null)
  or (client_id = '2297582c-660c-45c8-9c3a-84aea1b5ac01' and project_id is null)
  or (project_id = 'cdff0592-fb3c-4c13-9516-efde6b56b336');
```

## Resumo operacional para agentes externos

Antes de importar, decidir explicitamente o destino:

1. Global para todos os clientes
2. Catálogo do cliente
3. Projeto específico

Se o usuário disser "quero que apareça dentro do projeto X e esse catálogo é do cliente Y",
o padrão correto costuma ser:

- catálogo do cliente se o item deve valer para outros projetos do mesmo cliente
- projeto específico se o item deve existir só naquele projeto
