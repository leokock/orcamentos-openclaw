---
tags: [anchor, custos-ia-parametrico, indice]
---

# Premissas narrativas dos índices

Pasta com `.md` narrativos que explicam **origem, premissa, metodologia e limites** de cada índice do catálogo `indices-cartesian` (Supabase).

Os dados estruturados (stats, n, mediana, p25, p75) vivem no Supabase. Esses `.md` aqui são a **camada narrativa (query D)** — abertos via `Read` depois que a query SQL retorna o `premissa_md_path`.

## Estrutura

```
indices-premissas/
├── residencial_vertical/       ← tipos de obra atuais (só este hoje)
│   ├── indices_derivados/      ← stubs pros 29 índices derivados V2
│   ├── indices_estruturais/    ← stubs pros 23 índices estruturais
│   └── pus_cross/              ← premissas específicas pra PUs críticos (opcional)
├── residencial_horizontal/     ← (futuro)
├── industrial/                 ← (futuro)
└── ...
```

## Template pro stub

Cada `.md` de premissa segue esse formato:

```markdown
---
tags: [custos-ia-parametrico, indice, residencial-vertical]
indice: nome_do_indice
unidade: R$/m²
fonte_xlsx: calibration-indices.json (ou outra)
n: 52
---

# {nome_do_indice}

## O que é

Descrição curta (1-2 linhas).

## Como foi calculado

Metodologia: qual fórmula, quais projetos entraram, filtros aplicados.

## Premissas

O que foi assumido (ex: incluiu loteamentos? excluiu reformas? agregou ou não obras infra-heavy?).

## Quando usar / quando NÃO usar

Limites do índice. Ex: "só aplicar em residencial alto padrão — cv alto indica dispersão entre padrões".

## Links

- [[rsm2_total]] — índice relacionado
- Query SQL canônica pra puxar atualização: `SELECT * FROM indices_derivados_v2 WHERE nome = '{nome}'`
```

## Como Claude usa (query D)

1. SQL: `SELECT nome, premissa_md_path FROM indices_derivados_v2 WHERE nome = 'X'`
2. Se `premissa_md_path` não-null, `Read` o arquivo
3. Se null, responde com os stats do Supabase + aviso "premissa narrativa ainda não documentada"

## Atualização

Preencher conforme cada índice for usado em orçamento novo e Leo precisar justificar pro cliente. Não precisa preencher todos de uma vez — cobertura orgânica via uso real.
