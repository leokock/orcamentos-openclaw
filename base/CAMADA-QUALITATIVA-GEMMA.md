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

### Cross-project insights (Fase 5)

| Análise | Saída |
|---|---|
| Famílias de projetos por similaridade | `cross-insights/familias.json` |
| Outliers estruturais | `cross-insights/outliers.json` |
| Padrões de observações repetidas | `cross-insights/padroes_comuns.json` |
| Novos índices derivados sugeridos | `cross-insights/indices_sugeridos.json` |
| Lacunas de cobertura na base | `cross-insights/lacunas.json` |
| **Relatório consolidado** | `cross-insights/cross-insights-report.md` |

### Retry Fase 2 (Fase 6)

| Projeto | Sub-disc antes | Sub-disc depois |
|---|---|---|
| xpcon-porto-cerro | 3 | **14** |
| paludo-urban-life | 4 | **14** |
| neuhaus-botanico | 4 | **13** |
| f-nogueira-soberano | 3 | **10** |
| viva4-barra4 | 4 | **10** |
| ... (14 outros projetos melhorados) | | |

Total: 19/21 projetos com sub-disciplinas enriquecidas.

### Mineração profunda (Fases 8-15, desde 13/04 madrugada)

| Fase | Método | Saída |
|---|---|---|
| **8** — Comentários + texto livre | Python openpyxl (cell.comment) | `comentarios-completos/*.json` (126) |
| **9** — Fórmulas Excel | Python openpyxl (data_only=False) | `formulas/*.json` (126) |
| **10** — Normalização + PUs cross-projeto | Python hash-based (O(n)) | `itens-pus-agregados.json` (4.210 clusters) |
| **11** — Curvas ABC | Python | `curvas-abc/*.json` + `curva-abc-master.json` |
| **13** — Índices derivados | Python agregador | `indices-derivados-v2.json` (29 índices) |
| **14** — Observações completas via Gemma | Gemma e4b | `observacoes-insights/*.json` (126 em andamento) |
| **15** — Base master consolidada | Python | `base-indices-master-YYYY-MM-DD.json` (322 KB) |

### Novos 29 índices derivados (Fase 13)

**PUs medianos cross-projeto:**
- Concreto usinado: R$ 517,65/m³ (n=54)
- Aço CA-50: R$ 6,80/kg (n=48)
- Forma de madeira: R$ 16,49/m² (n=64)
- Impermeabilização: R$ 39,81/m² (n=105)
- Porcelanato: R$ 72,04/m² (n=60)
- Pintura acrílica: R$ 43,27/m² (n=110)
- Bloco cerâmico: R$ 1,40/un (n=19)

**Custos totais por m² AC:**
- Concreto: R$ 228,90/m² AC (n=64)
- Aço: R$ 231,82/m² AC (n=65)
- Forma: R$ 164,98/m² AC (n=69)
- Escoramento: R$ 47,67/m² AC (n=57)
- Impermeabilização: R$ 264,88/m² AC (n=95)
- Elevador: R$ 213,33/m² AC (n=70)
- Piscina: R$ 19,63/m² AC (n=65)
- Pintura: R$ 594,46/m² AC (n=96)
- Esquadrias: R$ 1.154,33/m² AC (n=96)
- Louças: R$ 109,76/m² AC (n=76)

**Cross-projeto:**
- CI total R$/m² AC: R$ 305,56 (n=55)
- Curva ABC %A: 12,2% (n=125)
- Material %: 35% (n=21), Mão-obra %: 20% (n=20), Equipamento %: 8% (n=12)

**Modelo Gemma usado:** `gemma4:e4b` (9.6 GB VRAM) via Ollama local. **Custo total:** R$ 0.

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

---

## Fase 14 — Gemma sobre observações completas (concluída 2026-04-14)

Rodada final de Gemma sobre `comentarios-completos/[projeto].json` (capturado na Fase 8 via openpyxl `cell.comment`). Diferente das fases 2/3 que olharam compact views ou PDFs, esta processou o **texto livre real do orçamentista** dentro das células do xlsx.

**Output:** `~/orcamentos-openclaw/base/observacoes-insights/[projeto].json` (126 arquivos)

**Estatísticas agregadas (126/126 projetos, 170 min total):**

| Dimensão | Total | Média/projeto |
|---|---|---|
| Temas extraídos | 883 | 7.0 |
| Flags de risco | 179 | 1.4 |
| Justificativas técnicas | 646 | 5.1 |

**Schema do JSON:**
```json
{
  "projeto": "...",
  "temas": ["..."],
  "justificativas": [{"item": "...", "razao": "...", "fonte_celula": "..."}],
  "flags_risco": [{"tipo": "...", "descricao": "...", "severidade": "alta|media|baixa"}],
  "padroes": ["..."],
  "decisoes": ["..."]
}
```

Esta camada é a fonte primária quando se quer entender **por que** um item teve PU acima/abaixo da mediana, ou **qual** decisão técnica explica um desvio. É o que mais agrega valor pra revisão de novos orçamentos contra a base.

## Fases 16 + 17 — Quantitativos físicos + Memorial de extração (concluída 2026-04-14)

Pipeline complementar que extrai quantitativos físicos diretamente do **projeto** (BIM, DXF, PDF) — não do orçamento. Permite cross-validar o memorial executivo ("o BIM tem X m² de alvenaria, o orçamento previu Y") e gerar memorial de extração rastreável.

**Scripts:**
- `extract_quantitativos_bim_v2.py` — ifcopenshell.geom (geometric bbox) ~3ms/elemento. Extrai: walls, slabs, beams, columns, doors, windows, spaces, curtain walls, railings, roofs, coverings.
- `extract_quantitativos_dxf.py` — ezdxf (TEXT/MTEXT/layers/lazer keywords).
- `extract_quantitativos_pdf.py` — pypdf (áreas, unidades, m³, kg, pavimentos).
- `consolidar_quantitativos.py` — merge BIM+DXF+PDF + ac do `state.json` → `quantitativos-consolidados/[projeto].json`.
- `gerar_memorial_extracao.py` — `memorial-extracao-{slug}.md` com cross-ref a 4.210 PUs cross-projeto + 29 índices derivados.

**Validado em 3 projetos reais** (arthen-arboris, placon-arminio-tavares, thozen-electra). Output: 27-30 KB/memorial.

**Como usar:** quando um novo executivo precisar de cross-validação física, rodar a sequência 16a→16b→16c→16d→17 sobre o slug do projeto. Os JSONs ficam em `quantitativos-{bim,dxf,pdf,consolidados}/` e o memorial em `pacotes/{slug}/memorial-extracao-{slug}.md`.

---

## Fase 18 — Classificação semântica de padrão via Gemma (concluída 2026-04-14)

Classificador rodando Gemma `gemma4:e4b` sobre os 126 projetos da base pra atribuir um label de padrão real (economico/medio/medio-alto/alto/luxo) a partir dos **materiais, marcas e dimensões dos itens de acabamento**. Substitui a estratificação anterior por bucket rsm2 (proxy circular).

### Por que existe

A calibração condicional original usava quartis de R$/m² total pra estratificar padrão — era circular (calibrava R$/m² a partir de buckets de R$/m²) e viesada por extrações incompletas. O Gemma lê os itens reais (porcelanato 120×120 vs cerâmico 45×45, mármore vs pintura texturizada, Docol/Deca vs Tigre/Astra) e classifica semanticamente.

### Pipeline

**Script:** `scripts/classificar_padrao_gemma.py`

Por projeto:
1. Coleta itens de Pisos/Esquadrias/Louças/Fachada/Sistemas Especiais via 2 estratégias:
   - **Aba-name matching:** nome da aba contém keyword (PISOS, ESQUADRIAS, LOUCAS...)
   - **Fallback por descrição:** regex por categoria aplicado a TODOS os itens de TODAS as abas (pra xlsx em formato Sienge/EAP/Relatório único). Prioridade: esquadrias > louças > fachada > SE > pisos.
2. Detecta **flags de assinatura** via regex: `piscina_aquecida`, `gerador`, `automacao`, `spa_sauna`, `elevador_panoramico`, `marmore`, `granito`, `acm`, `porcelanato_grande`, `porcelanato_pequeno`, `laminado`, `vinilico`, `docol_deca`, `fitness_academia`, `gourmet`, `heliponto`, `home_theater`, `adega`.
3. Métricas: R$/m², m²/UR, R$/UR, disciplinas_rsm2.
4. Monta prompt com rubric canônica de 5 classes + top 15 itens por macrogrupo.
5. Chama Ollama HTTP API com `format: json` (elimina truncamento de resposta).
6. Persiste em `base/padroes-classificados/{slug}.json` + entrada na fila retomável `base/phase18-queue.json`.

### Rubric (resumida)

| Classe | R$/m² | Pisos | Esquadrias | Lazer | Fachada |
|---|---|---|---|---|---|
| economico | <2.800 | cerâmico 45×45 | alumínio simples | básico | textura |
| medio | 2.800-3.400 | porcelanato 60×60 | alumínio intermediário | piscina+salão | pastilha |
| medio-alto | 3.400-4.000 | porcelanato 80×80 | esquadria reforçada | + automação básica | pastilha+detalhes |
| alto | 4.000-5.000 | porcelanato 120×120, granito | vidro duplo | + spa, gerador | ACM, granito |
| luxo | >5.000 | mármore, madeira nobre | brise automatizado | + piscina aquecida, heliponto | mármore premium |

Rubric é guia, não trava. 2 sinais fortes de classe alta compensam R$/m² baixo (o R$/m² pode estar subestimado por extração parcial).

### Output

**Por projeto** (`base/padroes-classificados/{slug}.json`):
```json
{
  "projeto": "slug",
  "classificacao": {
    "padrao": "alto",
    "confianca": "alta",
    "sinais_detectados": ["porcelanato 120x120", "ACM fachada", "gerador", ...],
    "sinais_ausentes_relevantes": ["heliponto", "borda infinita"],
    "justificativa": "...",
    "coerencia_rsm2": "sim|nao|parcial — explicação"
  },
  "sinais_input": {...}
}
```

**Consolidado** em `base/padroes-classificados-consolidado.json`.

### Resultado (126 projetos, ~20 min na 1ª rodada + ~15 min no reprocesso de 84)

| Classe | n | Alta conf | Média | Baixa |
|---|---|---|---|---|
| economico | 4 | 0 | 0 | 4 |
| medio | 4 | 0 | 3 | 1 |
| **medio-alto** | **60** | 27 | 28 | 5 |
| **alto** | **57** | **50** | 7 | 0 |
| luxo | 0 | — | — | — |
| insuficiente | 1 | — | — | — |

**94% classificados com alta/média confiança.**

## Fase 18b — Calibração condicional baseada em labels Gemma

**Script:** `scripts/build_calibration_gemma.py`

Substitui completamente a estratificação rsm2-bucket anterior. Pra cada classe Gemma, agrega medianas por macrogrupo dos projetos classificados naquela classe **E** com `ac+total > 0` em `indices-executivo`.

### Nova `base/calibration-condicional-padrao.json`

| Classe | n projetos | Total R$/m² mediano | MGs cobertos |
|---|---|---|---|
| economico | 3 | 1.767 | 13/18 |
| medio | 2 | 2.467 | 15/18 |
| **medio-alto** | **37** | **3.349** | **18/18** ✅ |
| **alto** | **23** | **4.156** | **18/18** ✅ |
| luxo | 0 | — | — |

`valores_macrogrupos_calibrados()` consulta condicional primeiro (n≥3), fallback pra global × `PADRAO_MULTIPLIERS` quando o bucket tem dados esparsos.

Classes **medio-alto** e **alto** são as mais confiáveis (n≥23, cobertura completa). Classes com n<5 atuam como aproximação + fallback global.

## Fluxo para novos projetos (atualizado fase 18)

```
Novo xlsx executivo → extract_itens_detalhados → itens-detalhados/{slug}.json
                   → classificar_padrao_gemma  → padroes-classificados/{slug}.json
                   → build_calibration_gemma   → calibration-condicional atualizada
                   → processar_executivo (V2)  → indices-executivo/{slug}.json
                   → phase14 (observações Gemma)
                   → merge_qualitative → qualitative key
```
