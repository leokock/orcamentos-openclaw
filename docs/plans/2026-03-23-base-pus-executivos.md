# Plano: Base de Conhecimento Executivo — Processamento de Orçamentos Reais

> **Objetivo:** Processar ~50 planilhas de orçamentos executivos Cartesian e gerar uma base de conhecimento completa: índices paramétricos + PUs detalhados + metadados editáveis
> **Sessão dedicada:** Rodar com o prompt da Seção 7 em nova sessão Claude Code
> **Criado:** 23/mar/2026
> **Atualizado:** 23/mar/2026 (arquitetura incremental + metadados editáveis)

---

## 1. Visão

Cada orçamento executivo processado alimenta **duas camadas**:

```
Executivo Real (.xlsx)
  ├─→ Camada 1: PARAMÉTRICO (macrogrupos, R$/m², CUB ratio)
  │     → calibration-data.json (75+ projetos)
  │     → calibration-stats.json (medianas por macrogrupo)
  │
  └─→ Camada 2: EXECUTIVO DETALHADO (PUs por item, índices de consumo)
        → base-pus-cartesian.json (PU mediano por item)
        → indices-executivo/{projeto}.json (índices detalhados)
        → projetos-metadados.json (cidade, padrão, tipologia — EDITÁVEL)
```

A Camada 1 já existe (sistema paramétrico atual). A Camada 2 é o que este plano cria.

---

## 2. Arquitetura de Dados

### 2.1 Metadados do Projeto (EDITÁVEL)

```json
// ~/orcamentos/base/projetos-metadados.json
{
  "elizabeth": {
    "nome_completo": "Elizabeth II Royal Home",
    "cliente": "Gessele",
    "cidade": "Itapema",        // ← EDITÁVEL (era "Florianópolis", Leo corrigiu)
    "estado": "SC",
    "padrao": "alto",           // baixo, medio, medio-alto, alto, luxo
    "tipologia": "residencial_vertical",
    "ac": 16749.67,
    "ur": 41,
    "pavimentos": 44,
    "subsolos": 0,
    "vagas": 97,
    "cub_base": 3019.26,
    "cub_date": "2026-02-01",
    "data_orcamento": "2026-02-01",
    "revisao": "R01",
    "arquivo_fonte": "CTN-GSL_EZB - Orçamento Executivo_R01 - Entregável.xlsx",
    "processado_em": "2026-03-23",
    "status": "processado"      // pendente, processado, erro
  }
}
```

**Regra:** Quando Leo editar cidade/padrão/tipologia neste JSON, os filtros de projetos similares e as medianas recalculam automaticamente na próxima execução.

### 2.2 Índices Detalhados por Projeto

```json
// ~/orcamentos/base/indices-executivo/elizabeth.json
{
  "projeto": "elizabeth",
  "ac": 16749.67,
  "total": 110631591.67,
  "disciplinas": {
    "ELETRICO": {
      "total": 3569163.72,
      "rsm2": 213.09,
      "itens": [
        {
          "descricao": "Transformador trifásico seco 500kVA",
          "unidade": "pç",
          "quantidade": 1,
          "pu": 79000.00,
          "total": 79000.00,
          "subgrupo": "SUBESTAÇÃO",
          "pavimento": "GERAL",
          "chave_normalizada": "transformador_trifasico_seco_500kva"
        }
      ]
    }
  }
}
```

### 2.3 Base de PUs Consolidada

```json
// ~/orcamentos/base/base-pus-cartesian.json
{
  "transformador_trifasico_seco_500kva": {
    "descricao": "Transformador trifásico seco 500kVA 13.800/380-220V",
    "categoria": "ELETRICO",
    "subgrupo": "SUBESTACAO",
    "unidade": "pç",
    "mediana": 79000.00,
    "p25": 72000.00,
    "p75": 85000.00,
    "min": 65000.00,
    "max": 92000.00,
    "n_projetos": 8,
    "projetos": ["elizabeth", "oxford", "santorini"],
    "cub_base": 3019.26,
    "data_base": "2026-03"
  }
}
```

---

## 3. Pipeline Incremental

### Detecção de novos projetos

```python
# Verificar o que já foi processado
metadados = load("projetos-metadados.json")
processados = {m["arquivo_fonte"] for m in metadados.values() if m["status"] == "processado"}

# Listar arquivos na pasta
arquivos = listar_executivos(EXEC_DIR)

# Novos = arquivos que não estão nos processados
novos = [a for a in arquivos if a not in processados]
```

### Fluxo de processamento

```
Para cada executivo novo:
  1. Extrair metadados (AC, UR, pavimentos) da aba CAPA
  2. Extrair macrogrupos da aba EAP → alimentar Camada 1 (paramétrico)
  3. Extrair itens detalhados de cada aba de disciplina → alimentar Camada 2 (PUs)
  4. Normalizar nomes de itens
  5. Registrar em projetos-metadados.json (status: "processado")
  6. Salvar indices-executivo/{projeto}.json
  7. Recalcular base-pus-cartesian.json (medianas atualizadas)
```

---

## 3.5 Dados Adicionais a Extrair (além dos PUs)

### 3.5.1 Índices de Consumo

Para cada disciplina, extrair taxas que não dependem de preço (mais estáveis que PUs):

```json
// Exemplo em indices-executivo/{projeto}.json → seção "indices_consumo"
{
  "ESTRUTURA": {
    "aco_kg_por_m3_concreto": 115,
    "forma_m2_por_m3_concreto": 8.2,
    "concreto_m3_por_m2_ac": 0.35
  },
  "ELETRICO": {
    "pontos_eletricos_por_ur": 45,
    "eletroduto_m_por_m2_ac": 2.8,
    "luminarias_por_m2_ac": 0.13
  },
  "HIDRO": {
    "tubulacao_m_por_m2_ac": 1.5,
    "pontos_hidro_por_ur": 22
  }
}
```

Esses índices são calculados automaticamente: `quantidade_total / AC` ou `quantidade_total / UR`.

### 3.5.2 Split MO vs Material

Para cada disciplina, calcular o percentual de mão de obra:

```json
// Em indices-executivo/{projeto}.json → seção "split_mo_material"
{
  "ELETRICO": {"mo_pct": 0.41, "material_pct": 0.59},
  "ESTRUTURA": {"mo_pct": 0.35, "material_pct": 0.65},
  "HIDRO": {"mo_pct": 0.38, "material_pct": 0.62}
}
```

Identificar MO por keywords nas descrições: "mão de obra", "mao de obra", "MOE", "empreiteira", "serviço de", "instalação de" (sem material).

### 3.5.3 Curva ABC por Macrogrupo

Para cada macrogrupo, identificar os top 20 itens de custo e calcular concentração:

```json
// Em indices-executivo/{projeto}.json → seção "curva_abc"
{
  "ELETRICO": {
    "top_20_pct": 0.78,  // top 20 itens = 78% do custo
    "itens": [
      {"desc": "Mão de obra elétrica", "pct": 0.41},
      {"desc": "Subestação", "pct": 0.18},
      {"desc": "Cabeamento geral", "pct": 0.07}
    ]
  }
}
```

Na consolidação: mediana da concentração por macrogrupo. Útil pra saber onde focar revisão no orçamento.

---

## 4. Pasta dos Executivos

```
~/clawd/_local/working-tree-archive/2026-03-18/orcamento-parametrico/executivos/
```

100 arquivos .xlsx. Filtrar:
- INCLUIR: "Orçamento", "Executivo", "Entregável", "Completo"
- EXCLUIR: "Apresentação", "slide", "Gerenciamento" (só gerenciamento)

---

## 5. Normalização de Itens

### Regras

1. Remover acentos, lowercase, snake_case
2. Padronizar medidas: `3/4"` → `3_4_pol`, `ø20mm` → `20mm`, `Ø60cm` → `60cm`
3. Padronizar unidades: `pç` = `un` = `peça`, `m` = `ml`, `m²` = `m2`
4. Agrupar sinônimos:
   - "Eletroduto PVC corrugado 3/4" = "Eletroduto flexível PVC ø20mm" = "Elet. PVC corr. 20mm"
   - Usar fuzzy match (difflib.SequenceMatcher, threshold 0.80)
5. Categorizar pela aba de origem (ELÉTRICO → categoria Elétrica, etc.)

### Categorias padrão

Gerenciamento, Mov.Terra, Infraestrutura, Supraestrutura, Alvenaria, Impermeabilização, Instalações Elétricas, Instalações Hidráulicas, PCI, Gás, Climatização, Sistemas Especiais, Revestimentos, Acabamentos, Pintura, Esquadrias, Fachada, Louças/Metais, Cobertura, Complementares

---

## 6. Estrutura de Saída

```
~/orcamentos/base/
├── projetos-metadados.json           # Metadados editáveis (cidade, padrão, etc.)
├── base-pus-cartesian.json           # PUs consolidados com estatísticas
├── base-pus-cartesian-resumo.md      # Tabela legível (top 200 itens)
├── pus-qualidade.md                  # Relatório de validação e outliers
├── indices-executivo/                # Um JSON por projeto processado
│   ├── elizabeth.json
│   ├── oxford.json
│   ├── santorini.json
│   └── ...
├── pus-raw/                          # Dados brutos extraídos (backup)
│   ├── elizabeth-raw.json
│   └── ...
├── calibration-data.json             # Camada 1 (já existe, atualizar)
└── calibration-stats.json            # Camada 1 (já existe, atualizar)
```

---

## 7. Prompt para Sessão Dedicada

Copiar e colar ao iniciar nova sessão do Claude Code em `~/clawd`:

```
Preciso processar os orçamentos executivos da Cartesian para construir uma base de conhecimento completa (índices paramétricos + PUs detalhados).

**Plano completo:** ~/orcamentos/docs/plans/2026-03-23-base-pus-executivos.md
Leia o plano inteiro antes de começar.

**Pasta dos executivos:** ~/clawd/_local/working-tree-archive/2026-03-18/orcamento-parametrico/executivos/

**O que fazer (resumo — detalhes no plano):**

1. INVENTARIAR: Listar todos os .xlsx, filtrar executivos (excluir "Apresentação", "slide"). Registrar inventário

2. PROCESSAR CADA PLANILHA (uma por vez, read_only):
   a) Aba CAPA → extrair AC, UR, pavimentos → metadados
   b) Aba EAP → extrair macrogrupos → Camada 1 (paramétrico)
   c) Abas de disciplina → extrair itens com PU → Camada 2 (executivo)
   d) Salvar em ~/orcamentos/base/indices-executivo/{nome}.json e pus-raw/{nome}-raw.json

3. NORMALIZAR: Agrupar itens similares, criar chaves normalizadas

4. CONSOLIDAR: Calcular mediana/P25/P75 por item → base-pus-cartesian.json

5. EXTRAIR ÍNDICES ADICIONAIS (por projeto):
   a) Índices de consumo (kg aço/m3, m eletroduto/m2 AC, pontos/UR)
   b) Split MO vs Material (% por disciplina)
   c) Curva ABC (top 20 itens por macrogrupo, concentração %)
   Ver seção 3.5 do plano para detalhes

6. VALIDAR: Flaggar outliers, gerar relatório de qualidade

7. ATUALIZAR DOCUMENTAÇÃO:
   a) ~/orcamentos/AGENTS.md — adicionar seção base de PUs
   b) ~/clawd/CLAUDE.md — atualizar referência à base de PUs

**Regras:**
- Processar 1 arquivo por vez (planilhas grandes)
- Se der erro em uma planilha, registrar e seguir para a próxima
- Salvar progresso a cada 5 planilhas
- Criar ~/orcamentos/base/projetos-metadados.json com dados editáveis (cidade, padrão)
- Pipeline incremental: verificar o que já foi processado antes de reprocessar
- Me atualizar no Telegram (chat_id: 104742984) a cada 10 planilhas processadas

**Output:** Ver seção 6 do plano para estrutura completa de saída

6. ATUALIZAR DOCUMENTAÇÃO: Após processar, atualizar:
   a) ~/orcamentos/AGENTS.md (Cartesiano/OpenClaw) — adicionar seção sobre base de PUs executivos, como consultar, como usar no orçamento executivo
   b) ~/clawd/CLAUDE.md (Claude Code) — atualizar seção de Orçamento Paramétrico com referência à base de PUs executivos
   Ambos precisam saber: onde estão os dados, como consultar, como usar no fluxo de orçamento
```

---

## 8. Atualização da Documentação (AGENTS.md + CLAUDE.md)

### Por que é importante

O processo de orçamento executivo roda em DUAS plataformas:
- **Claude Code** (~/clawd) → sessões interativas, processamento pesado
- **OpenClaw/Cartesiano** (~/orcamentos) → atende equipe no Slack, gera orçamentos

Ambos precisam entender a base de PUs e o fluxo de executivo. O Cartesiano lê `~/orcamentos/AGENTS.md`, o Claude Code lê `~/clawd/CLAUDE.md`.

### O que adicionar ao AGENTS.md do Cartesiano

```markdown
## Base de Preços Unitários (PUs Executivos)

Sistema de PUs extraídos de ~50 orçamentos executivos reais da Cartesian.

### Arquivos
- `~/orcamentos/base/base-pus-cartesian.json` — PUs consolidados (mediana, P25, P75 por item)
- `~/orcamentos/base/projetos-metadados.json` — metadados dos projetos (cidade, padrão, editável)
- `~/orcamentos/base/indices-executivo/{projeto}.json` — índices detalhados por projeto

### Como usar
1. **Ao orçar um item:** consultar base-pus-cartesian.json para o PU mediano
2. **Ao filtrar projetos similares:** usar projetos-metadados.json (cidade, padrão, AC)
3. **Ao comparar:** cruzar PU do item com mediana da base
4. **Ao gerar discipline pack:** preencher PUs automaticamente da base

### Fluxo de Orçamento Executivo
Ver ~/orcamentos/docs/plans/2026-03-23-orcamento-executivo-design.md
```

### O que adicionar ao CLAUDE.md

Referência na seção de Orçamento Paramétrico apontando para a base de PUs executivos e o design doc do processo de executivo.

---

## 9. Manutenção Futura

### Adicionar novos executivos

1. Leo coloca nova planilha na pasta de executivos
2. Roda sessão dedicada com o mesmo prompt
3. Pipeline detecta automaticamente os novos (não reprocessa os já feitos)
4. Medianas recalculam com o novo projeto incluído

### Corrigir metadados

1. Leo edita `projetos-metadados.json` (ex: mudar cidade de "Florianópolis" para "Itapema")
2. Na próxima execução, filtros de projetos similares usam os dados corrigidos
3. Não precisa reprocessar — só recalcular medianas

### Recalibrar paramétrico

Quando novos executivos forem processados, a Camada 1 (calibration-data.json) também é atualizada automaticamente — regra de recalibração contínua (Leo, 05/mar/2026).

---

*Plano criado em 23/mar/2026. Revisado com arquitetura incremental, metadados editáveis, e atualização de AGENTS.md + CLAUDE.md.*

---

## 10. Resultado da Execução (23/mar/2026)

### Números finais

| Métrica | Valor |
|---------|-------|
| Projetos processados | 75 |
| Com itens detalhados | 57 |
| Só macrogrupos | 18 |
| Itens brutos extraídos | 22.000+ |
| Itens consolidados (n>=2) | 1.504 |
| Itens com 3+ projetos | 544 |
| Itens com 5+ projetos | 199 |
| Disciplinas cobertas | 26 |

### Pasta definitiva

`~/orcamentos/executivos/entregues/` — organizada por `Cliente/Projeto/*.xlsx` (136 arquivos, 104 pastas, 65 clientes).

### Formatos suportados

O `processar_executivo.py` detecta automaticamente 4 formatos:
1. **Multi-abas** — abas individuais por disciplina (ELÉTRICO, HIDROSSANITÁRIO, etc.)
2. **Sienge** — aba única "Relatório" ou "EAP" com códigos XX.XXX.XXX.XXX
3. **Analítico** — códigos hierárquicos X.X.X em aba "Orçamento Executivo"
4. **ABC Insumos** — lista flat ordenada por custo

### Scripts

| Script | Uso |
|--------|-----|
| `~/orcamentos/scripts/processar_executivo.py --inventory` | Ver o que tem e o que falta |
| `~/orcamentos/scripts/processar_executivo.py --batch` | Processar todos os pendentes |
| `~/orcamentos/scripts/processar_executivo.py --process <path>` | Processar 1 arquivo |
| `~/orcamentos/scripts/consolidar_base_pus.py` | Recalcular medianas |

### Pendências

Ver `~/orcamentos/base/PENDENCIAS-BASE-PUS.md` para inventário completo e lista de pendências (AC faltando, metadados, outliers).
