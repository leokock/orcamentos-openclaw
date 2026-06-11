# docs/ — legado de documentação do Cartesiano

> **Nota 2026-06-10:** a documentação canônica do bot `@Cartesiano` e do time foi movida para `~/cartesian/docs/`. Este diretório fica como legado histórico/ponte; não adicionar workflow novo aqui.

Os docs originais foram arquivados em `../archive/2026-05-cleanup/docs-pre-fusao/`. Ponteiros antigos para `~/openclaw/docs/orcamento/` existem apenas por histórico.

---

## Onde encontrar o conhecimento canônico

### Orçamento (5 docs canônicos)

| Doc | Cobre |
|---|---|
| `~/cartesian/docs/orcamento/README.md` | Índice + árvore de decisão |
| `~/cartesian/docs/orcamento/PARAMETRICO.md` | Workflow V2 Híbrido completo |
| `~/cartesian/docs/orcamento/EXECUTIVO.md` | Copiloto incremental, 7 etapas por disciplina, lições |
| `~/cartesian/docs/orcamento/QUANTITATIVOS-E-PRECIFICACAO.md` | REGRA #3 (pacote por disciplina) + REGRA #4 (3 fontes) + framework executivo→paramétrico |
| `~/cartesian/docs/orcamento/MEMORIAL.md` | Memorial descritivo Word + Memorial Cartesiano (Supabase) |
| `~/cartesian/docs/orcamento/OPERACAO.md` | Fluxos A/B, handoff, Drive paths, kickoff, integração equipe |

### Modelagem BIM (4 docs canônicos)

| Doc | Cobre |
|---|---|
| `~/openclaw/docs/modelagem/README.md` | Índice + árvore de decisão |
| `~/openclaw/docs/modelagem/PROCESSO-REVIT.md` | Manual completo Cartesian (14 etapas, parâmetros CTN_*, templates) |
| `~/openclaw/docs/modelagem/VISUS-INTEGRACAO.md` | EAP → AltoQi + cadastro insumos/composições |
| `~/openclaw/docs/modelagem/BIM-COORDENACAO.md` | Construflow (bot @Bim) + atas Cartesian (R00/R01/R02) |
| `~/openclaw/docs/modelagem/REVIT-MCP-AUTOMACAO.md` | Automação via mcp__revit__* e mcp__acad__* + plugin CTNext |

---

## Como o bot Cartesiano acessa esses docs

Quando precisar formar uma resposta longa (workflow detalhado, conceito explicado), bot pode:

1. **Ler de path absoluto** — `~/cartesian/docs/orcamento/X.md`
2. **Nao criar symlink reverso** para docs canonicos aqui; isso reintroduz duplicacao.

---

## O que continua aqui em `docs/`

- **Stubs-redirect** (curtos, apontando pros canônicos):
  - `ORCAMENTO-WORKFLOW.md` → PARAMETRICO/EXECUTIVO
  - `ESTRATEGIA-DOIS-TIERS.md` → PARAMETRICO (seção Tiers)
  - `LICOES-APRENDIDAS-OXFORD.md` → EXECUTIVO (seção Lições)
  - `AGENTS-PARAMETRICO-DETAIL.md` → PARAMETRICO
  - `AGENTS-EXECUTIVO-DETAIL.md` → EXECUTIVO
  - `QUANTITATIVOS-EXECUTIVOS-PADRAO.md` → QUANTITATIVOS-E-PRECIFICACAO
  - `PRECIFICACAO-3-FONTES.md` → QUANTITATIVOS-E-PRECIFICACAO
  - `FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` → QUANTITATIVOS-E-PRECIFICACAO
  - `WORKFLOW-EXECUTIVO-INCREMENTAL.md` → EXECUTIVO
  - `MAPA-COBERTURA.md` → OPERACAO
  - `COMO-FALAR-COM-CARTESIANO.md` → OPERACAO

- **Plans históricos** em `docs/plans/` (preservados como histórico, não absorvidos)
- **`COMO-FALAR-COM-CARTESIANO.docx`** (versão Word pra equipe Cartesian — não tocada)
- **`_build_como_falar.js`** (script auxiliar — não tocado)

---

## Onde mexer pra mudar comportamento do bot Cartesiano

| Quero mudar... | Editar... |
|---|---|
| Regras de comportamento Slack (postagem, upload, erros) | `~/cartesian/AGENTS.md` |
| Identidade/tom do bot | `~/cartesian/IDENTITY.md` / `SOUL.md` |
| Workflow didático (paramétrico, executivo, etc.) | `~/cartesian/docs/orcamento/{X}.md` (canônico) |
| Base de dados (calibrações, índices) | `~/orcamentos-openclaw/base/` (= `~/openclaw/data/base/` via junction) |
| Scripts | `~/orcamentos-openclaw/scripts/` (= `~/openclaw/data/scripts-orcamento/` via junction) |

---

## Plano completo da reorganização

`C:\Users\leona\.claude\plans\eu-tenho-aqui-a-gentle-lark.md`
