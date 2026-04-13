# Camada Qualitativa Gemma — Enriquecimento dos Orçamentos Executivos

_Criado em 2026-04-13 após pipeline multi-fase rodado sobre os 126 orçamentos executivos entregues._

Esta é a **fonte canônica** da camada qualitativa adicionada à base paramétrica V2. É complementar aos índices numéricos que já existiam (`calibration-indices.json`, `base-pus-cartesian.json`, `indices-executivo/*.json`) — não os substitui.

## Por que existe

A base numérica V2 captura muito bem **quanto custa** cada macrogrupo (18 MGs, PUs medianos, índices estruturais, splits MO/material). Mas ela **não** captura:

- Sub-disciplinas granulares dentro de cada macrogrupo (ex: dentro de "Estrutura" → Concreto, Armadura, Forma, Escoramento)
- Observações do orçamentista explicando decisões (revisões, premissas, estimativas)
- Premissas técnicas dos memoriais/apresentações (tipo de fundação considerado, perdas, prazo, BDI)
- Padrões cross-aba identificáveis só por quem lê o orçamento inteiro
- Itens fora-da-curva justificados

A Camada Gemma extrai tudo isso via LLM local (gemma4:e4b) rodando sobre os xlsx/pdf entregues, sem custo de tokens API.

## O que contém

### Arquivos por projeto (em `~/orcamentos-openclaw/base/`)

| Arquivo | Origem | Conteúdo |
|---|---|---|
| `itens-detalhados/[projeto].json` | Python openpyxl | **Todas as linhas** de todos os xlsx do projeto — código, descrição, unidade, qtd, PU, total, aba, seção, observações textuais |
| `sub-disciplinas/[projeto].json` | Gemma sobre `itens-detalhados` | Sub-disciplinas, observações categorizadas, padrões, fora-da-curva |
| `sub-disciplinas-md/[projeto]-qualitativo.md` | Gemma | Relatório legível da análise qualitativa |
| `premissas/[projeto].json` | Gemma sobre PDFs | Metadata do pdf, premissas técnicas, BDI/encargos, decisões consolidadas, observações chave |
| `premissas-md/[projeto]-premissas.md` | Gemma | Relatório legível das premissas do pdf |
| `indices-executivo/[projeto].json` | Merge | **Original + chave `qualitative`** agregando tudo acima |

### Compact views intermediárias

| Arquivo | Função |
|---|---|
| `compact-views/[projeto].md` | Markdown compacto (~3-4k chars) usado como input do Gemma Fase 2 |
| `pdfs-text/[projeto].txt` | Texto extraído dos PDFs (até 30k chars/pdf) usado na Fase 3 |

### Logs e filas

| Arquivo | Função |
|---|---|
| `phase1-extract.log.jsonl` | Log append-only da Fase 1 |
| `phase2-queue.json` + `phase2-pipeline.log.jsonl` | Estado da Fase 2 (retomável) |
| `phase3-queue.json` + `phase3-pipeline.log.jsonl` | Estado da Fase 3 (retomável) |
| `relatorio-consolidado-YYYY-MM-DD.md` | Relatório agregado gerado por `final_report.py` |

## Schema da chave `qualitative` em `indices-executivo/[projeto].json`

Após `merge_qualitative.py`, cada JSON da base passa a ter esse bloco adicional:

```json
{
  "projeto": "amalfi-tramonti",
  "ac": 15602.85,
  "ur": 90,
  "macrogrupos": { ... },
  "disciplinas": { ... },
  "qualitative": {
    "updated_at": "2026-04-13T00:12:34",

    "phase1_extraction": {
      "n_abas": 27,
      "total_itens": 11359,
      "total_observacoes": 385,
      "fonte": "scripts/extract_itens_detalhados.py",
      "json_path": "...itens-detalhados/amalfi-tramonti.json"
    },

    "sub_disciplinas": [
      {
        "macrogrupo": "Estrutura",
        "sub_disciplina": "Concreto",
        "itens_exemplo": ["Concreto Usinado FCK = 35MPa Bombeavel", "..."]
      }
    ],

    "observacoes_orcamentista": [
      {
        "contexto": "Projeto de elétrica",
        "observacao": "REVISÃO do valor... recebido em 14/05/25",
        "categoria": "revisao"
      }
    ],

    "padroes_identificados": [
      "Valores de Gerenciamento Técnico se repetem em diferentes blocos"
    ],

    "fora_da_curva": [
      { "item": "SUPOSIÇÃO", "motivo": "Sem imagem comercial" }
    ],

    "phase2_meta": {
      "model": "gemma4:e4b",
      "ts": "2026-04-12T20:20:05",
      "duration_s": 96.9,
      "compact_chars": 3225
    },

    "pdf_metadata": {
      "ac_m2": "15602.85", "ur": 90,
      "tipologia": "Edificação residencial...",
      "data_base": "mai/2025",
      "cub_referencia": null
    },

    "premissas_tecnicas": [
      { "area": "Fundação", "premissa": "Considerado blocos, vigas e cisterna" },
      { "area": "Perdas", "premissa": "Considerado 13% de perda, h=5cm" }
    ],

    "bdi_encargos": [
      { "componente": "BDI", "valor_pct": "25%", "nota": "..." }
    ],

    "decisoes_consolidadas": [
      { "contexto": "Prazo", "decisao": "Tempo de permanência para 24 meses" }
    ],

    "observacoes_chave_pdf": ["..."],

    "phase3_meta": {
      "model": "gemma4:e4b",
      "ts": "2026-04-12T22:14:17",
      "duration_s": 107.2,
      "excerpt_chars": 4287
    }
  }
}
```

**Campos opcionais:** `phase3_*` aparecem apenas para os **58 projetos** que tinham pdf/docx. Os outros 68 só têm `phase1_*` e `phase2_*`.

## Como consultar

### Por código Python

```python
import json
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"

def load_project(slug: str) -> dict:
    return json.loads((BASE / "indices-executivo" / f"{slug}.json").read_text(encoding="utf-8"))

# Exemplo: listar sub-disciplinas de um projeto
p = load_project("amalfi-tramonti")
for sd in p.get("qualitative", {}).get("sub_disciplinas", []):
    print(f"{sd['macrogrupo']}: {sd['sub_disciplina']}")

# Exemplo: puxar premissas técnicas de um projeto
for pr in p.get("qualitative", {}).get("premissas_tecnicas", []):
    print(f"{pr['area']}: {pr['premissa']}")
```

### Agregação cross-projeto (futuro — ver FASES-FUTURAS.md)

Phase 5 do roadmap vai rodar Gemma sobre os agregados pra descobrir padrões entre projetos (famílias, outliers, sub-disciplinas comuns).

## Pacote Paramétrico → Executivo (Fluxo 0, v0.2)

Pra usar a camada qualitativa de forma **integrada** ao gerar orçamentos novos, existe um pipeline orquestrado em 2 etapas:

```bash
# Etapa 1 — gera gate de validação
python scripts/gerar_pacote.py --slug NOVO --ac 15000 --ur 90 --padrao alto

# (humano valida o gate.xlsx, salva como -validado.xlsx)

# Etapa 2 — gera paramétrico + executivo + validação
python scripts/gerar_pacote.py --slug NOVO --continue
```

Saída em `~/orcamentos-openclaw/base/pacotes/NOVO/`:
- `gate-NOVO.xlsx` — decisões pra validar
- `parametrico-NOVO.xlsx` — pelo V2 calibrado
- `executivo-NOVO.xlsx` — 18 abas, sub-disciplinas reais, confidence tags
- `validacao-NOVO.md` — relatório de coerência
- `state.json` — estado retomável

**Fonte dos totais (cascata):**
1. **Primário:** `calibration-indices.json → por_macrogrupo` (18 macrogrupos com R$/m² mediano calibrado de 58-131 projetos cada, ajustado por padrão)
2. **Fallback:** mediana dos 5 similares
3. **Granularização:** itens detalhados dos similares (referência, não soma)

**Scripts envolvidos** (todos em `~/orcamentos-openclaw/scripts/`):
- `gerar_pacote.py` — orquestrador
- `consulta_similares.py` — módulo de consulta + `valores_macrogrupos_calibrados()`
- `gerar_gate_validacao.py` — gera o xlsx do gate
- `gerar_executivo_auto.py` — gera o executivo a partir do gate validado
- `validar_pacote.py` — relatório de coerência

**Pacote piloto rodado (15.000 m² alto-padrão):**
- Total: R$ 48.074.207 / R$ 3.205/m² — coerente com mercado
- 17/18 macrogrupos com confiança 🟢 Alta
- Distribuição realista: Supraestrutura 22.6%, Esquadrias 10.6%, Instalações 9.5%, Gerenciamento 7.7%

Documentação detalhada do fluxo: `~/openclaw/skills/orcamento-parametrico/SKILL.md` → "FLUXO 0".
Roadmap de melhorias (Fase 7.x): `FASES-FUTURAS.md` → "Fase 7.x".

## Quando usar

### Ao gerar um **orçamento paramétrico novo**

Antes de abrir o template V2, verificar se há projetos similares na base com premissas/sub-disciplinas explícitas. Exemplo de consulta:

```python
# Buscar projetos com AC similar ao novo e padrão similar
todos = [load_project(p.stem) for p in (BASE / "indices-executivo").glob("*.json")]
similares = [p for p in todos
             if p.get("ac") and abs(p["ac"] - alvo_ac) < alvo_ac * 0.2
             and p.get("qualitative", {}).get("sub_disciplinas")]

# Inspecionar sub-disciplinas e premissas dos similares
for p in similares[:5]:
    print(p["projeto"], p["ac"])
    for sd in p["qualitative"]["sub_disciplinas"]:
        print(" ", sd)
```

Isso ajuda a:
- **Detalhar mais** a aba de cada macrogrupo (sub-disciplinas reais, não só agregados)
- **Reutilizar premissas técnicas** ("perda 13%", "cisterna 3.5×8m", "prazo 24 meses")
- **Antecipar observações de orçamentista** que costumam aparecer em projetos similares
- **Calibrar BDI/encargos** olhando o que foi usado em projetos entregues

### Ao gerar um **orçamento executivo em modo copiloto**

A cada disciplina trabalhada:
1. **Consultar sub-disciplinas** do mesmo macrogrupo em 3-5 projetos similares da base (query por AC + padrão)
2. **Puxar observações de orçamentista** que apareceram no mesmo macrogrupo — reutilizar como texto-modelo no memorial
3. **Checar padrões_identificados** — se algum projeto similar tinha um padrão relevante (ex: "GTA mantido constante entre blocos"), considerar se aplica
4. **Usar fora_da_curva** como alerta — se um item vai ficar fora-da-curva, usar justificativas existentes como modelo

### Ao analisar um **executivo novo pra alimentar a base**

Depois do fluxo de ingestão tradicional (Fluxo 3 da SKILL), rodar as 3 fases nesse projeto novo:

```bash
# Regenerar queue pra incluir o projeto novo
python scripts/gemma_queue_init.py

# Fase 1 (só o novo)
python scripts/extract_itens_detalhados.py [slug-novo]

# Fase 2 (só o novo)
python scripts/phase2_pipeline.py [slug-novo]

# Fase 3 (só o novo, se tiver pdf)
python scripts/extract_pdf_text.py [slug-novo]
python scripts/phase3_pipeline.py [slug-novo]

# Merge
python scripts/merge_qualitative.py --slug [slug-novo]
```

## Estatísticas da base atual (2026-04-13)

### Camada qualitativa (Fases 1-3)

| Dimensão | Total |
|---|---|
| Projetos com camada qualitativa | **126** |
| Itens detalhados extraídos | **333.751** |
| Observações de orçamentista (raw) | 7.210 |
| Sub-disciplinas identificadas | 761 |
| Observações categorizadas | 553 |
| Padrões cross-aba | 269 |
| Itens fora-da-curva | 22 |
| Projetos com PDF analisado | 58 |
| Premissas técnicas extraídas | 404 |
| BDI/Encargos identificados | 34 |
| Decisões consolidadas | 124 |

### Camada de composições (Fase 4 — desde 13/04 noite)

| Dimensão | Total |
|---|---|
| Projetos com abas CPU/Insumos/Composições | **22** |
| Insumos extraídos (raw) | **35.147** |
| Insumos classificados como Material | ~17.000 |
| Insumos classificados como Mão de Obra | ~5.000 |
| Insumos classificados como Equipamento | ~750 |
| Análise Gemma sobre composições | em `composicoes/*.json` |
| Memoriais .md de composições | em `composicoes-md/*.md` |

### Cross-project insights (Fase 5 — desde 13/04 noite)

| Análise | Saída |
|---|---|
| Famílias de projetos por similaridade | `cross-insights/familias.json` |
| Outliers estruturais | `cross-insights/outliers.json` |
| Padrões de observações repetidas | `cross-insights/padroes_comuns.json` |
| Novos índices derivados sugeridos | `cross-insights/indices_sugeridos.json` |
| Lacunas de cobertura na base | `cross-insights/lacunas.json` |
| **Relatório consolidado** | `cross-insights/cross-insights-report.md` |

**Modelo usado:** `gemma4:e4b` (9.6 GB VRAM) via Ollama local. **Custo:** R$ 0.

## Limitações conhecidas

1. **Qualidade depende do input.** Projetos com planilhas-resumo (template ETAPA/VALOR ORÇADO) têm sub-disciplinas genéricas porque o source não tem granularidade — Gemma reflete fielmente o que encontra.
2. **Gemma 26b é inviável** em 8GB VRAM. O e4b é o único modelo que roda em tempo razoável (~90s/chamada) e não alucina em inputs ≤5k chars.
3. **Inputs devem ser pré-processados.** Xlsx grandes (>300k chars) são filtrados para compact views (~3-4k chars) antes de ir ao Gemma. Nunca passar xlsx bruto.
4. **Não-determinismo do Gemma.** Chamadas repetidas podem variar. A Fase 2 teve 3 falhas de parse em 126 rodadas iniciais (resolvidas no retry).
5. **Pptx não é suportado** pelo mcp-ollama, então projetos só com pptx de apresentação ficam sem Fase 3.

## Scripts relacionados

Todos em `~/orcamentos-openclaw/scripts/`:

| Script | Fase | Função |
|---|---|---|
| `gemma_queue_init.py` | setup | Cria fila com 126 projetos a partir de `_all_projects_mapping.json` |
| `extract_itens_detalhados.py` | 1 | Heurística openpyxl → itens brutos |
| `phase1_summary.py` | 1 | Relatório de estatísticas da Fase 1 |
| `compact_view.py` | 2 input | Itens → markdown compacto (~3-4k chars) |
| `phase2_pipeline.py` | 2 | Loop Gemma sobre compact views |
| `extract_pdf_text.py` | 3 input | PDFs → texto concatenado |
| `phase3_pipeline.py` | 3 | Loop Gemma sobre texto dos pdfs |
| `merge_qualitative.py` | merge | Consolida Fases 1-3 em `indices-executivo/[projeto].json` |
| `final_report.py` | report | Gera relatório agregado diário |

## Relacionamento com a base V2

A **base V2 paramétrica** (`calibration-indices.json`, `base-pus-cartesian.json`, etc.) continua sendo a fonte de verdade para:
- Índices quantitativos calibrados
- PUs medianos por item
- Split MO/Material
- Segmentação por porte

A **Camada Qualitativa Gemma** adiciona uma dimensão textual/semântica que complementa os números. Nenhuma das duas substitui a outra.

**Fluxo de alimentação da base ao processar um novo executivo:**

```
Novo xlsx  →  processar_executivo.py (V2)  →  calibration-* atualizados
          ↘
            extract_itens_detalhados.py + phase2/3 (camada Gemma)  →  qualitative key
```

Ambos fluxos rodam em paralelo. O V2 continua autoritativo para números; a camada Gemma serve como referência textual/semântica.
