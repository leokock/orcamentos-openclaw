# Auditoria de Documentação — Orçamento Paramétrico

> Data: 07/03/2026
> Autor: Jarvis (sub-agente)
> Escopo: Todos os arquivos de documentação do sistema de orçamento paramétrico
> Status: **Diagnóstico completo — correções aplicadas em 11/mar/2026**

---

## Atualização 11/mar/2026

### Números atualizados
- **calibration-data.json**: 75 projetos (era 58 na auditoria)
- **calibration-stats.json**: 75 projetos, 22 categorias, 74 com AC — regenerado com bug `pct.mean` corrigido
- **indices-subdisciplina.json**: 205 projetos extraídos, 435 índices únicos, 114 com AC válido
- **Formatos de extração**: 5 (resumo: 99, detalhado: 72, gerenciamento: 52, sienge: 22, analítico: 15)
- **Script de extração**: `scripts/extract_indices.py`

### Itens resolvidos (da auditoria original)
- ✅ **2.1** "18 projetos" → corrigido em todos os docs (75 calibrados, 205 extraídos)
- ✅ **2.3** Bug `pct.mean` com valores absurdos → calibration-stats.json regenerado corretamente
- ✅ **2.6** Regra de recalibração contraditória → BRIEFING atualizado para "após cada novo executivo"
- ✅ **2.8** Inconsistência calibration-data vs calibration-stats → ambos com 75 projetos
- ✅ Contagens sincronizadas em: AGENTS.md, ORCAMENTO-PARAMETRICO-WORKFLOW.md, CLAUDE.md, README.md, BRIEFING, FRAMEWORK, ESTRATEGIA-DOIS-TIERS

### Itens ainda pendentes
- 🟡 **2.2** Medianas do script vs calibration-stats — verificar se `gerar_template_dinamico.py` foi atualizado
- 🟡 **2.4** TEMPLATE-INDICES-EXPANDIDO.md referenciado em caminho antigo (movido para `archive/`)
- 🟡 **2.5** Script referenciado em caminhos inconsistentes (alguns docs apontam raiz, real está em `scripts/`)
- 🟡 **2.7** Índices soltos na raiz (7 arquivos `*-indices.md` fora de `indices/`)
- 🟡 **3.1-3.8** Duplicidades de conteúdo entre docs — consolidação pendente
- 🟡 **3.8** pacote-drive/ desatualizado vs raiz

---

## 1. Arquivos Mapeados

### 1.1 Documentação Principal (6 arquivos)

| Arquivo | Tipo | Tamanho |
|---------|------|---------|
| `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` | Workflow completo (3 fluxos) | ~390 linhas |
| `orcamento-parametrico/docs/README.md` | README do diretório | ~245 linhas |
| `orcamento-parametrico/BASE-CONHECIMENTO-PARAMETRICO.md` | Base textual de projetos | ~3.386 linhas |
| `orcamento-parametrico/BRIEFING-PARAMETRICO.md` | Checklist de briefing (25 perguntas) | ~175 linhas |
| `orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` | Framework de extração de índices | ~160 linhas |
| `orcamento-parametrico/docs/ESTRATEGIA-DOIS-TIERS.md` | Dois tiers de produto | ~100 linhas |

### 1.2 Documentação Secundária (3 arquivos)

| Arquivo | Tipo |
|---------|------|
| `orcamento-parametrico/docs/MAPA-COBERTURA.md` | Mapa de cobertura por cidade |
| `orcamento-parametrico/REORGANIZACAO-LOG.md` | Log da reorganização de 06/mar |
| `orcamento-parametrico/indices/FALTAM-CALIBRAR.md` | Lista de índices não calibrados |

### 1.3 Pacote Drive (cópia autocontida) — 10 arquivos

| Arquivo | Correspondente |
|---------|---------------|
| `pacote-drive/CLAUDE.md` | Novo — instruções para Claude Code/Cowork |
| `pacote-drive/gerar_template_dinamico.py` | Cópia de `scripts/gerar_template_dinamico.py` |
| `pacote-drive/calibration-data.json` | Cópia de `calibration-data.json` |
| `pacote-drive/calibration-stats.json` | Cópia de `calibration-stats.json` |
| `pacote-drive/BASE-CONHECIMENTO-PARAMETRICO.md` | Cópia de raiz |
| `pacote-drive/BRIEFING-PARAMETRICO.md` | Cópia de raiz |
| `pacote-drive/ESTRATEGIA-DOIS-TIERS.md` | Cópia de `docs/` |
| `pacote-drive/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` | Cópia de `docs/` |
| `pacote-drive/MAPA-COBERTURA.md` | Cópia de `docs/` |
| `pacote-drive/TEMPLATE-INDICES-EXPANDIDO.md` | Cópia de `archive/` |
| + 11 MDs de categorias (ALVENARIA.md, INSTALAÇÕES.md, etc.) | Cópia de `archive/` |

### 1.4 Referências em Arquivos de Sistema

| Arquivo | Seção |
|---------|-------|
| `AGENTS.md` | Seção "Orçamento Paramétrico" (linhas ~295-325) |
| `TOOLS.md` | Não tem referência direta ao paramétrico |
| `CLAUDE.md` | Referência genérica ao workflow |

### 1.5 Dados e Scripts

| Arquivo | Conteúdo |
|---------|----------|
| `calibration-data.json` | **58 projetos** (raiz) |
| `calibration-stats.json` | Estatísticas de **57 projetos** |
| `scripts/gerar_template_dinamico.py` | Script gerador (~2.600 linhas) |
| `indices/` | **59 arquivos** `*-indices.md` |
| Raiz tem **7 arquivos** `*-indices.md` soltos | Não movidos na reorganização |

---

## 2. Incoerências Encontradas

### 🔴 2.1 CRÍTICO — Número de projetos calibrados desatualizado em MÚLTIPLOS arquivos

O `calibration-data.json` tem **75 projetos** (atualizado 11/mar/2026). O `calibration-stats.json` reporta **75 projetos**. Na auditoria original (07/mar), a documentação dizia:

| Arquivo | O que diz | Valor real |
|---------|-----------|------------|
| `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` (3 ocorrências) | "18 projetos reais" | 58 |
| `AGENTS.md` (2 ocorrências) | "18 projetos" | 58 |
| `orcamento-parametrico/docs/README.md` (5 ocorrências) | "18 projetos" | 58 |
| `orcamento-parametrico/BRIEFING-PARAMETRICO.md` (2 ocorrências) | "18 projetos calibrados" | 58 |
| `orcamento-parametrico/BASE-CONHECIMENTO-PARAMETRICO.md` | "53 projetos" (header) | 58 |
| `orcamento-parametrico/pacote-drive/CLAUDE.md` | "54 projetos" calibrados | 58 |
| `orcamento-parametrico/docs/ESTRATEGIA-DOIS-TIERS.md` | "33+ projetos" (Tier 1) | 58 |
| `orcamento-parametrico/docs/ESTRATEGIA-DOIS-TIERS.md` | "50+ projetos" (Tier 2 ressalva) | 58 |
| `orcamento-parametrico/BRIEFING-PARAMETRICO.md` | "40+ projetos" na BASE-CONHECIMENTO | 66 (header da BASE) |

**Resumo:** O número "18" está congelado na data de criação original dos docs (05/mar/2026) e nunca foi atualizado conforme projetos foram adicionados. Cada arquivo mostra um número diferente dependendo de quando foi editado pela última vez.

### 🔴 2.2 CRÍTICO — Medianas do script DESATUALIZADAS vs calibration-stats.json

O dict `MEDIANAS` no `gerar_template_dinamico.py` está significativamente defasado em relação ao `calibration-stats.json`:

| Macrogrupo | Script | Stats.json | Diferença |
|---|---|---|---|
| **Fachada** | 164,53 | 127,83 | **+28,7%** |
| **Imprevistos** | 96,27 | 52,98 | **+81,7%** |
| **Mov. Terra** | 12,40 | 16,16 | **-23,3%** |
| **Sist. Especiais** | 190,04 | 169,40 | **+12,2%** |
| **Teto** | 67,43 | 62,02 | **+8,7%** |
| **Pintura** | 131,49 | 121,48 | **+8,2%** |
| **Esquadrias** | 366,05 | 340,96 | **+7,4%** |
| **Infraestrutura** | 227,95 | 212,47 | **+7,3%** |
| **Climatização** | 0 (hardcoded) | 41,03 | **-100%** |
| **Louças e Metais** | 0 (hardcoded) | 26,35 | **-100%** |

**Impacto:** Paramétricos gerados pelo script usam medianas antigas (de quando havia ~18 projetos), não as medianas atuais com 57 projetos. A diferença é comercialmente significativa em macrogrupos como Fachada (+28,7%) e Imprevistos (+81,7%).

**Nota:** Climatização e Louças e Metais estão zerados no script — provavelmente porque na calibração original (18 projetos) não havia dados suficientes. Agora há 14 projetos com Climatização e 6 com Louças e Metais.

### 🔴 2.3 CRÍTICO — calibration-stats.json com valores absurdos em `pct.mean`

Os campos `pct.mean` de 16 dos 21 macrogrupos contêm valores na casa de milhões em vez de percentuais (<100):

- Alvenaria: `pct.mean = 5.143.444,15` (deveria ser ~4-5%)
- Supraestrutura: `pct.mean = 23.741.227,45` (deveria ser ~20%)
- Todos os 16 macrogrupos afetados

**Causa provável:** Bug no script de recalibração — provavelmente está somando os valores absolutos (R$) no campo `pct` em vez dos percentuais, ou há projetos no `calibration-data.json` com o campo `pct` contendo valores absolutos (R$) em vez de percentuais.

**Impacto:** A mediana do `pct` ainda parece correta (é robusta a outliers), mas o `mean` e os `min`/`max` estão completamente errados. Qualquer lógica que use esses campos (ex: alertas, benchmark) produzirá resultados absurdos.

### 🟡 2.4 TEMPLATE-INDICES-EXPANDIDO.md referenciado em caminho que não existe

Múltiplos documentos referenciam `orcamento-parametrico/TEMPLATE-INDICES-EXPANDIDO.md` na raiz:

- `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` linha 25: `orcamento-parametrico/TEMPLATE-INDICES-EXPANDIDO.md`
- `orcamento-parametrico/docs/README.md` linha 25 e 107
- `orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` linha 5

**Mas o arquivo está em:**
- `orcamento-parametrico/archive/TEMPLATE-INDICES-EXPANDIDO.md` (movido na reorganização)
- `orcamento-parametrico/pacote-drive/TEMPLATE-INDICES-EXPANDIDO.md` (cópia)

**Não existe em:** `orcamento-parametrico/TEMPLATE-INDICES-EXPANDIDO.md` (caminho referenciado)

### 🟡 2.5 Script referenciado em caminhos inconsistentes

O script `gerar_template_dinamico.py` tem 3 cópias em caminhos diferentes:

| Caminho | Status |
|---------|--------|
| `orcamento-parametrico/gerar_template_dinamico.py` | **Não existe** (referenciado em WORKFLOW, README, AGENTS.md) |
| `orcamento-parametrico/scripts/gerar_template_dinamico.py` | **Ativo** (94KB, última edição 06/mar) |
| `orcamento-parametrico/pacote-drive/gerar_template_dinamico.py` | Cópia desatualizada (output_dir diferente) |

Documentos que referenciam o caminho errado:
- `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`: `orcamento-parametrico/gerar_template_dinamico.py`
- `AGENTS.md`: `orcamento-parametrico/gerar_template_dinamico.py`
- `orcamento-parametrico/docs/README.md`: `gerar_template_dinamico.py` (raiz do dir)

### 🟡 2.6 Regra de recalibração contraditória

| Arquivo | O que diz |
|---------|-----------|
| `BRIEFING-PARAMETRICO.md` (linha 161) | "Se ≥3 novos projetos desde última calibração: recalibrar template" |
| `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` (linha 281-283) | "SEMPRE após cada novo executivo processado — não esperar acumular" |
| `AGENTS.md` (linha 318) | "recalibrar medianas imediatamente (regra Leo 05/mar/2026)" |

**O BRIEFING ainda tem a regra antiga (≥3 projetos).** O WORKFLOW e AGENTS.md foram atualizados para recalibração contínua. A regra correta é a do WORKFLOW/AGENTS (decisão do Leo de 05/mar).

### 🟡 2.7 Índices soltos na raiz (não movidos para `indices/`)

7 arquivos `*-indices.md` ficaram na raiz do `orcamento-parametrico/` fora da pasta `indices/`:

- `belissimo-indices.md`
- `one-palace-indices.md`
- `paludo-barbados-indices.md`
- `paludo-urbanlife-indices.md` (duplicado — também existe em `indices/`)
- `parkside-riobranco-indices.md`
- `passione-indices.md`
- `vancouver-indices.md`

O `paludo-urbanlife-indices.md` existe em ambos os locais com conteúdo diferente (versões diferentes).

### 🟡 2.8 calibration-data.json vs calibration-stats.json inconsistência de contagem

- `calibration-data.json`: **58 projetos**
- `calibration-stats.json`: `total_projects: 57`, `global.cub_ratio.n: 56`

Provavelmente o último projeto adicionado (belissimo?) não está refletido nas stats, ou há um projeto sendo excluído das estatísticas.

---

## 3. Duplicidades Encontradas

### 🔴 3.1 Modelo de cálculo explicado em 6+ lugares

A fórmula `Valor Final = Base R$/m² × Fator CUB × Fator Briefing` aparece em:

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — seção "Modelo de Cálculo (3 camadas)" (~30 linhas detalhadas)
2. **`AGENTS.md`** — seção "Orçamento Paramétrico" (~5 linhas resumidas)
3. **`orcamento-parametrico/docs/README.md`** — seção "Modelo de Cálculo" (~20 linhas com exemplo)
4. **`orcamento-parametrico/pacote-drive/CLAUDE.md`** — seção "Modelo de Cálculo" (~8 linhas)
5. **`orcamento-parametrico/BRIEFING-PARAMETRICO.md`** — seção "Workflow do Jarvis" item 5 (1 linha)
6. **`orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md`** — referência indireta

**Risco:** Quando o modelo muda, precisa atualizar em 6 lugares. Já há inconsistência no CUB Base (2.752,67 em todos, mas a referência varia: alguns dizem "18 projetos", outros "54", outros "58").

### 🔴 3.2 Estrutura das 14 abas descrita em 4 lugares

A tabela com as 14 abas do template Excel aparece em:

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — tabela completa com 14 linhas + colunas Função e Preenchida
2. **`orcamento-parametrico/docs/README.md`** — tabela completa com 14 linhas + colunas Tipo e Função
3. **`orcamento-parametrico/pacote-drive/CLAUDE.md`** — referência "14 abas" sem tabela detalhada
4. **`AGENTS.md`** — "14 abas" mencionado sem detalhe

### 🟡 3.3 Lista de briefing (25 perguntas) em 3 lugares

1. **`orcamento-parametrico/BRIEFING-PARAMETRICO.md`** — lista completa com opções e impacto (~125 linhas)
2. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — lista resumida das 25 perguntas (com prioridade 🔴🟡🟢)
3. **`orcamento-parametrico/docs/README.md`** — lista das "9 perguntas críticas" (sub-set)

### 🟡 3.4 Mapeamento dos 18 macrogrupos em 3 lugares

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — tabela com nomes comuns
2. **`orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md`** — tabela com itens típicos detalhados
3. **`orcamento-parametrico/pacote-drive/CLAUDE.md`** — lista numerada

### 🟡 3.5 Regra de compatibilidade Excel (IFS proibido) em 4 lugares

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — seção "Regras Técnicas"
2. **`orcamento-parametrico/docs/README.md`** — seção "Regras Técnicas"
3. **`orcamento-parametrico/pacote-drive/CLAUDE.md`** — seção "Regras Críticas"
4. **`AGENTS.md`** — "Nenhuma fórmula IFS()"

### 🟡 3.6 Regra DATA-BASE (CUB) em 4 lugares

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — parágrafo com ⚠️
2. **`AGENTS.md`** — parágrafo com ⚠️
3. **`orcamento-parametrico/docs/README.md`** — seção "Data-base"
4. **`orcamento-parametrico/pacote-drive/CLAUDE.md`** — seção "Regras Críticas"

### 🟡 3.7 Fluxo de processamento de executivo em 4 lugares

O workflow de "receber executivo → extrair → indices.md → calibrar" aparece em:

1. **`docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** — Fluxo 2 (~80 linhas, mais completo)
2. **`orcamento-parametrico/docs/README.md`** — seção "Como Adicionar Novo Executivo" (~50 linhas)
3. **`orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md`** — workflow detalhado (~160 linhas, mais técnico)
4. **`orcamento-parametrico/BRIEFING-PARAMETRICO.md`** — seção "Ao receber orçamento executivo real" (~10 linhas)

### 🟡 3.8 pacote-drive/ inteiro é duplicata

A pasta `pacote-drive/` contém cópias de:
- `calibration-data.json` — **desatualizada** (33 projetos vs 58 na raiz)
- `calibration-stats.json` — **desatualizada**
- `BASE-CONHECIMENTO-PARAMETRICO.md` — **desatualizada** (51 projetos vs 66)
- `BRIEFING-PARAMETRICO.md` — **desatualizada**
- `gerar_template_dinamico.py` — **desatualizada** (output_dir diferente)
- `ESTRATEGIA-DOIS-TIERS.md` — idêntico
- `MAPA-COBERTURA.md` — idêntico
- `FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` — idêntico

**Risco:** Quem abrir o pacote-drive no Claude Code/Cowork vai trabalhar com dados desatualizados (33 projetos em vez de 58). Não há mecanismo de sincronização automática.

---

## 4. Informação Obsoleta Identificada

### 🔴 4.1 "18 projetos" em todos os documentos-base

O número "18" é de ~05/mar/2026 (validação Domus). Desde então, foram adicionados ~40 projetos. Todos os documentos abaixo estão obsoletos neste aspecto:

- `docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` — "base calibrada com 18 projetos reais" (cabeçalho e 3 ocorrências)
- `AGENTS.md` — "Base calibrada com 18 projetos reais" e "calibration-data.json (18 projetos)"
- `orcamento-parametrico/docs/README.md` — "18 projetos" em 5 ocorrências
- `orcamento-parametrico/BRIEFING-PARAMETRICO.md` — "18 projetos calibrados" em 2 ocorrências

### 🔴 4.2 Medianas no script congeladas na calibração de ~18 projetos

O dict `MEDIANAS` no `gerar_template_dinamico.py` não foi atualizado após a adição em massa de projetos. As medianas atuais (com 57 projetos) são significativamente diferentes em vários macrogrupos (Fachada: +28,7%, Imprevistos: +81,7%).

### 🟡 4.3 "40+ projetos" na BASE-CONHECIMENTO

O header da BASE-CONHECIMENTO diz "66 projetos" e "53 projetos calibrados", mas o arquivo só tem 5 seções `## PROJETO` (49, 50, 51, 52, 53). Os projetos 1-48 parecem ter sido removidos ou nunca foram adicionados como seções completas. A referência a "PUs detalhados dos projetos 12-25: `orcamento-parametrico/PUs-NOVOS-PROJETOS.md`" aponta para um arquivo que está em `archive/` agora.

### 🟡 4.4 Referência a "TEMPLATE-INDICES-EXPANDIDO.md" na raiz

O arquivo foi movido para `archive/` na reorganização de 06/mar, mas as referências não foram atualizadas. Quem seguir o WORKFLOW vai procurar o arquivo no lugar errado.

### 🟡 4.5 BRIEFING tem regra de recalibração antiga

Linha 161: "Se ≥3 novos projetos desde última calibração: recalibrar template" — superada pela regra de recalibração contínua decidida pelo Leo em 05/mar.

---

## 5. Proposta de Consolidação

### 5.1 Single Source of Truth — Hierarquia proposta

```
AGENTS.md
  └── Resumo executivo (5-8 linhas, aponta para WORKFLOW)

docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md  ← FONTE ÚNICA do workflow
  └── 3 fluxos, modelo de cálculo, regras técnicas, lições aprendidas

orcamento-parametrico/docs/README.md  ← FONTE ÚNICA de "como usar" o diretório
  └── Estrutura de arquivos, comandos, checklist rápido

orcamento-parametrico/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md  ← FONTE ÚNICA da extração
  └── Mapeamento de categorias, workflow de extração detalhado

orcamento-parametrico/BRIEFING-PARAMETRICO.md  ← FONTE ÚNICA das perguntas
  └── 25 perguntas com opções e impacto

orcamento-parametrico/docs/ESTRATEGIA-DOIS-TIERS.md  ← FONTE ÚNICA dos tiers
orcamento-parametrico/docs/MAPA-COBERTURA.md  ← FONTE ÚNICA da cobertura
```

### 5.2 Ações Concretas (por prioridade)

#### 🔴 P1 — Crítico (impacta entregas comerciais)

1. **Atualizar medianas no script** — Sincronizar dict `MEDIANAS` em `gerar_template_dinamico.py` com as medianas atuais do `calibration-stats.json`. Incluir Climatização e Louças e Metais (hoje zerados).

2. **Corrigir bug em calibration-stats.json** — Os campos `pct.mean` contêm valores absolutos (R$) em vez de percentuais. Investigar causa no script de recalibração e regenerar stats.

3. **Sincronizar contagens** — Atualizar todos os "18 projetos" para o número real. Sugestão: usar variável simbólica tipo "N projetos" nos docs que apontam para `calibration-data.json` como fonte, ou manter o número atualizado mas usar linguagem que envelhece melhor (ex: "50+ projetos" em vez de "58").

4. **Reconciliar calibration-data vs calibration-stats** — O data.json tem 58 projetos, o stats.json reporta 57. Regenerar stats a partir dos dados.

#### 🟡 P2 — Importante (impacta produtividade)

5. **Corrigir caminhos de referência:**
   - `TEMPLATE-INDICES-EXPANDIDO.md` → mover de `archive/` para `docs/` (é referência ativa, não obsoleto) ou atualizar todas as referências
   - `gerar_template_dinamico.py` → atualizar referências para `scripts/gerar_template_dinamico.py`

6. **Mover índices soltos para `indices/`** — Os 7 arquivos `*-indices.md` na raiz devem ir para `indices/`. Resolver duplicata do `paludo-urbanlife-indices.md`.

7. **Eliminar duplicidades na explicação do modelo:**
   - `AGENTS.md` → manter apenas resumo de 3-5 linhas + pointer para WORKFLOW
   - `orcamento-parametrico/docs/README.md` → manter seção "Modelo de Cálculo" mas mais curta, apontando para WORKFLOW para detalhes
   - `BRIEFING-PARAMETRICO.md` → remover seção "Base Atual" e "Workflow do Jarvis" (pertencem ao WORKFLOW, não ao briefing)
   - O WORKFLOW permanece como fonte única e completa

8. **Atualizar regra de recalibração no BRIEFING** — Mudar de "≥3 novos projetos" para "após cada novo executivo" (alinhado com WORKFLOW e AGENTS).

#### 🟢 P3 — Manutenção (organização e higiene)

9. **Definir estratégia para pacote-drive/:**
   - Opção A: Transformar `exportar-pacote-drive.sh` em script que copia automaticamente os arquivos atualizados
   - Opção B: Eliminar cópias estáticas e manter apenas o `CLAUDE.md` com instruções de onde achar os arquivos
   - Enquanto existir, deve ter warning claro de "pode estar desatualizado"

10. **Limpar BASE-CONHECIMENTO-PARAMETRICO.md:**
    - Atualizar header (números de projetos)
    - Verificar se os projetos 1-48 existem no arquivo ou só na memória (apenas 5 seções `## PROJETO` existem)
    - Corrigir referência a `PUs-NOVOS-PROJETOS.md` (está em archive/)

11. **Consolidar listas de macrogrupos:**
    - FRAMEWORK deve ser a fonte única da tabela detalhada de mapeamento
    - WORKFLOW pode manter tabela resumida mas referenciar FRAMEWORK para detalhes

12. **Remover seções duplicadas do README.md:**
    - O README repete quase integralmente o WORKFLOW. Manter apenas: estrutura de arquivos, como rodar o script, e pointers para docs detalhados

---

## 6. Resumo Executivo

| Categoria | Qtd |
|-----------|-----|
| Arquivos de documentação mapeados | 10+ |
| Cópias no pacote-drive | 10+ |
| Incoerências encontradas | **8** (3 críticas, 5 importantes) |
| Duplicidades encontradas | **8** (2 críticas, 6 importantes) |
| Info obsoleta | **5** itens |
| Ações propostas | **12** (4 P1, 4 P2, 4 P3) |

**As 3 questões mais urgentes:**
1. 🔴 Medianas do script defasadas (impacta valores dos paramétricos gerados)
2. 🔴 Bug nos `pct.mean` do calibration-stats.json (valores absurdos)
3. 🔴 Todos os docs dizem "18 projetos" quando na verdade são 58

---

*Auditoria concluída em 07/03/2026. Nenhuma alteração executada — apenas diagnóstico e propostas.*
