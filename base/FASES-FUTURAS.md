# Fases Futuras — Roadmap Retomável

_Criado em 2026-04-13 após conclusão das Fases 1-3 + Pacote v0.2._
_Atualizado em 2026-04-14 madrugada após conclusão de TODAS as 15 fases._

## ✅ Estado atual — TODAS as fases concluídas

| Fase | Descrição | Status |
|---|---|---|
| **1** | 333.751 itens extraídos de 126 projetos | ✅ |
| **2** | 126 projetos com sub-disciplinas/observações/padrões Gemma | ✅ |
| **3** | 58 projetos com premissas/BDI/decisões de PDFs | ✅ |
| **4** | 22 projetos com composições extraídas + análise Gemma | ✅ |
| **5** | Cross-project benchmarking (5 análises Gemma) — rodada 2x | ✅ |
| **6** | Retry Fase 2 com compact view rica: 19/21 projetos melhorados | ✅ |
| **7 / 7.1-7.6** | Pacote v0.3 + 6 melhorias do pipeline | ✅ |
| **8** | Comentários + texto livre dos xlsx (Python openpyxl) | ✅ |
| **9** | Fórmulas Excel (data_only=False) — rastreabilidade | ✅ |
| **10 v2** | Normalização hash-based + 4.210 PUs cross-projeto | ✅ |
| **11** | Curvas ABC individuais (126) + master | ✅ |
| **12** | Embutida na 10 v2 (PUs cross-projeto já agregados) | ✅ |
| **13** | 29 novos índices derivados cross-projeto | ✅ |
| **14** | Gemma sobre observações completas (em andamento, 20/126 em bg) | ⏳ |
| **15** | base-indices-master.json consolidado (322 KB) | ✅ |

## 🎁 Resultados tangíveis

- **3 pacotes reais entregues** (arthen, placon, thozen) — R$ 186M total, com audit v2 contra PUs cross-projeto
- **16+ scripts novos** em `~/orcamentos-openclaw/scripts/`
- **Base master** única consolidando todos os índices (322 KB, base-indices-master-2026-04-13.json)
- **~40 commits** no GitHub
- **Doc atualizada**: SKILL.md v0.4, CAMADA-QUALITATIVA-GEMMA.md, esta FASES-FUTURAS

## 🔜 Pendências e oportunidades futuras

- **Fase 14** ainda rodando em background (Gemma sobre observações completas — ~3h total)
- **Revisão Arthen**: comparar v2 antigo (R$ 42,6M) vs v2.1 novo (R$ 36,5M) — decisão pendente
- **Cópia pra Drive**: pacotes aprovados via `copiar_pacotes_drive.py --confirm`
- **Fase 16 sugerida**: cronograma + curva S a partir das fórmulas Excel capturadas na Fase 9
- **Fase 17 sugerida**: dashboard interativo dos índices derivados (HTML ou Streamlit)
- **Upgrade Gemma**: se GPU mudar, rodar Fase 2/3/4/14 com gemma4:26b pra melhor precisão

Todos os scripts estão em `~/orcamentos-openclaw/scripts/`.

## Fase 7.x — Melhorias do Pacote Paramétrico→Executivo (alta prioridade)

Refinos diretos no pacote v0.2 que valem ser feitos antes de partir pra Fase 4. Cada item abaixo é independente e implementável em 30-90 min.

### 7.1 — Multiplicador por padrão mais sofisticado (~30 min)

Hoje `valores_macrogrupos_calibrados()` aplica multiplicador heurístico simples (Médio 1.0 / Médio-Alto 1.05 / Alto 1.10 / Luxo 1.25) sobre todos os macrogrupos uniformemente.

**Melhoria:** aplicar multiplicador **diferencial por macrogrupo** baseado em projetos calibrados:
- Acabamentos (Pisos, Esquadrias, Louças, Pintura, Rev. Int., Fachada) → multiplicador maior em padrões altos (1.20-1.50)
- Estrutura (Supra, Infra, Mov. Terra) → multiplicador neutro (1.00)
- Sistemas Especiais → ajuste por presença de itens (gerador, automação, piscina aquecida)

**Implementação:** estender `valores_macrogrupos_calibrados()` recebendo `padrao` + `gate_decisoes` (do gate validado) e aplicando ajustes contextualizados. Tabela de multiplicadores por macrogrupo × padrão derivada de regressão sobre os 126 projetos.

**Arquivo a editar:** `consulta_similares.py`

### 7.2 — Memorial Word do executivo (~45 min)

Gerar `Memorial-Executivo-{slug}.docx` consolidando:
- Premissas validadas no gate
- Sub-disciplinas usadas por macrogrupo
- Tabela de macrogrupos com R$/m², total, % e confiança
- Fontes (projetos similares) com rastreabilidade
- BDI/encargos aplicados
- Decisões consolidadas

**Implementação:** criar `gerar_memorial_executivo.py` baseado em template Markdown → pandoc → docx. Pode reutilizar lógica de `gerar_memorial_rastreavel.py` que já existe em `~/orcamentos/scripts/`.

**Trigger:** `gerar_pacote.py --continue` chama no final.

### 7.3 — Aba RESUMO mais expressiva no executivo (~30 min)

Atualizar a aba RESUMO do `executivo-{slug}.xlsx` pra incluir:
- Coluna nova "Fonte" mostrando se o total veio de `calibration-indices` ou `similares` ou está vazio
- Ícones visuais por confiança (🟢/🟡/🔴) baseados em N amostras
- Linha de comparação P10/P25/Mediana/P75/P90 do macrogrupo na base
- Gráfico de pizza (xlsx chart) com distribuição

**Arquivo a editar:** `gerar_executivo_auto.py` → função `aba_resumo`

### 7.4 — Granularização nos 10 macrogrupos hoje sem detalhamento (~1h)

10 macrogrupos do piloto saem com total OK mas sem itens detalhados granulares dos similares (Gerenciamento, Mov. Terra, Supra, Imperm., Rev. Int., Teto, Pisos, Pintura, Fachada, Imprevistos).

**Causa:** `_classify_item()` em `consulta_similares.py` é conservador — só pega itens com keywords de alta confiança. Mas as abas reais dos xlsx (Ger_Executivo, Arquitetura, Obra) misturam tudo e os itens não têm `secao` populada.

**Solução:** ler também as **sub_disciplinas Gemma** (Fase 2) por macrogrupo dos similares e usar ELAS como granularização, em vez de tentar extrair itens dos itens-detalhados brutos. Isso usa dados que JÁ estão classificados e cobre os 18 macrogrupos.

**Implementação:** nova função `granular_via_gemma_subdisciplinas(similares, mg)` que retorna sub-disciplinas + itens_exemplo do qualitative, usado quando `enriquecer_executivo()` retorna vazio.

**Arquivo a editar:** `consulta_similares.py` + `gerar_executivo_auto.py`

### 7.5 — Validação cruzada com base por segmento (~30 min)

A `calibration-indices.json` tem `por_segmento` com R$/m² total mediano por porte (pequeno <8k, médio 8-15k, grande 15-25k, extra >25k). O `validar_pacote.py` deve:
- Identificar o segmento do projeto pelo AC
- Comparar o total executivo com a mediana e P10-P90 do segmento
- Alertar se está fora do P10-P90 (não fora dos 30% absolutos como hoje)

**Arquivo a editar:** `validar_pacote.py`

### 7.6 — Memorial Word do paramétrico junto no pacote (~20 min)

Hoje o pacote roda `gerar_template_dinamico_v2.py` que gera só o xlsx. O `gerar_memorial_rastreavel.py` (que gera o .docx) NÃO é chamado. Adicionar essa chamada no `gerar_pacote.py --continue`.

**Arquivo a editar:** `gerar_pacote.py`

### Ordem sugerida (tudo em uma sessão de ~3h)

1. **7.4** primeiro (1h) — destrava o detalhamento granular dos 10 macrogrupos faltantes — ganho visual imediato
2. **7.6** (20 min) — incluir memorial word do paramétrico
3. **7.2** (45 min) — memorial word do executivo
4. **7.5** (30 min) — validação por segmento
5. **7.3** (30 min) — aba RESUMO mais expressiva
6. **7.1** opcional (30 min) — multiplicador diferencial por macrogrupo

---

## Fase 4 — Composições unitárias (material + MO + equipamento)

**Objetivo:** extrair, para os itens de maior custo, a composição unitária (quanto é material, quanto é mão-de-obra, quanto é equipamento). Hoje a base tem PUs totais mas não decompostos — isso impede entender como reajustar preços quando o insumo muda (ex: aço sobe 20%, quanto o PU total é afetado?).

### Duas fontes possíveis

1. **Abas "Composição" / "CPU" / "Insumos"** dentro dos xlsx executivos
2. **Base SINAPI/SICRO** (referência externa que o Cartesian usa)

### Onde estão as composições nos xlsx

Na Fase 1 descobrimos que vários projetos têm abas chamadas:
- `CPU` (custos unitários)
- `Insumos`
- `Composições`
- `Composição de Preço Unitário`

Exemplos de projetos que têm essas abas (ver `itens-detalhados/[projeto].json` → lista de abas):
- `amalfi-tramonti` → abas `Insumos`, `CPU`
- `brasin-redentor` → (checar)
- `pavcor`, `fonseca-empreendimentos-estoril` → provavelmente

### Pipeline proposto

```
Fase 4a (Python)  — extrair abas CPU/Insumos/Composições de cada xlsx
                    → base/composicoes-raw/[projeto].json
                    schema: { aba, item_pai, insumo, unidade, coef, pu, total, categoria (mat/mo/eq) }

Fase 4b (Gemma)   — interpretar cada composição
                    → base/composicoes/[projeto].json
                    schema: { item_pai, material_pct, mo_pct, equip_pct, insumos_principais: [...] }

Fase 4c (merge)   — enriquecer qualitative com composições
                    → merge_qualitative.py estendido
```

### Script a criar

`scripts/extract_composicoes.py`:
1. Abre cada xlsx
2. Filtra abas por nome (regex case-insensitive): `cpu|composi|insumo`
3. Para cada aba:
   - Detecta header com openpyxl (heurística similar a `extract_itens_detalhados.py`, mas procurando por colunas "coef", "consumo", "insumo")
   - Agrupa por item-pai (geralmente primeira coluna com código)
   - Extrai linhas-filha como insumos
4. Classifica cada insumo como material/MO/equipamento via heurística de texto (palavras-chave: "mão de obra", "ferramenta", "aço", "concreto", etc.)
5. Salva `base/composicoes-raw/[projeto].json`

`scripts/phase4_pipeline.py`:
- Loop similar ao phase2/phase3
- Para cada projeto com `composicoes-raw`, gera um compact view por item-pai top-20 e pergunta pro Gemma:
  - Distribuição % entre material/MO/equipamento
  - Se há reajuste-chave (item que seria afetado por variação de aço, concreto, MO)
  - Padrões (ex: "escoramento metálico aparece em todos projetos com laje protendida")

### Tempo estimado

- Fase 4a (Python puro): ~10 min sobre os 126 projetos
- Fase 4b (Gemma): ~2-3h (só roda sobre projetos que tenham composições — provavelmente 30-50% da base)

### Comandos para retomar

```bash
cd ~/orcamentos-openclaw

# 1. Inventariar abas de composição em todos projetos
python -c "
import json
from pathlib import Path
count = 0; hits = []
for jp in Path('base/itens-detalhados').glob('*.json'):
    d = json.loads(jp.read_text(encoding='utf-8'))
    for aba in d.get('abas', []):
        nome = aba.get('nome', '').lower()
        if any(k in nome for k in ['cpu','composi','insumo']):
            hits.append((jp.stem, aba['nome'], aba['n_itens']))
            count += 1
            break
print(f'{len(hits)} projetos com aba de composição')
for h in hits[:20]: print(h)
"

# 2. Se valioso, criar extract_composicoes.py e rodar
# 3. Depois phase4_pipeline.py

# 4. Merge
python scripts/merge_qualitative.py  # adicionar suporte a composicoes
```

## Fase 5 — Cross-project benchmarking e inteligência de base

**Objetivo:** não processar projetos individualmente — rodar Gemma sobre **agregados** da base inteira pra descobrir padrões, outliers, famílias de projetos similares, novos índices derivados. Isso complementa a análise individual feita nas fases 2-3.

### Perguntas que Gemma deve responder

1. **Famílias de projetos:** dado os 126 projetos, agrupar em famílias por similaridade (AC + UR + padrão + sub-disciplinas). Retornar 5-10 clusters com exemplares representativos.
2. **Outliers estruturais:** projetos com kg aço/m³ ou m³ concreto/m² AC >3σ da mediana — listar e sugerir causa provável (carga alta, balanços grandes, subsolos, etc.)
3. **Padrões de observações:** textos que se repetem em >10 projetos (ex: "perda 13%") — consolidar como "premissa padrão Cartesian"
4. **Novos índices derivados:** olhando sub-disciplinas cruzadas com valor, sugerir novos índices ainda não calculados (ex: "custo de escoramento por m² de laje")
5. **Lacunas de cobertura:** dimensões/campos vazios em vários projetos que deveriam ter dados (oportunidade de melhorar ingestão)

### Pipeline proposto

**Input agregado:** em vez de 1 projeto = 1 chamada, montar um "dossiê" consolidado:
- Top 30 projetos mais ricos da base (com mais sub-disciplinas + premissas)
- Tabela resumida: slug | AC | UR | total | R$/m² | top 5 macrogrupos por % | top 3 sub-disciplinas
- Cabe em ~8-10k chars — borderline pro Gemma e4b, mas viável se enxuto

**Loop diferente:** cada pergunta é uma chamada Gemma separada (5 chamadas totais, não 126). Tempo: ~10-15 min total.

### Script a criar

`scripts/phase5_cross_insights.py`:
1. Carrega `indices-executivo/*.json` (todos 126)
2. Monta dossiê agregado em markdown (~8k chars)
3. Pergunta 1: "Agrupe os projetos em famílias" → salva `base/cross-insights/familias.json`
4. Pergunta 2: "Liste outliers estruturais" → `base/cross-insights/outliers.json`
5. Pergunta 3: "Padrões de observações repetidas" → `base/cross-insights/padroes-comuns.json`
6. Pergunta 4: "Novos índices sugeridos" → `base/cross-insights/indices-sugeridos.json`
7. Pergunta 5: "Lacunas de cobertura" → `base/cross-insights/lacunas.json`
8. Gera `cross-insights-report.md` consolidando tudo

### Tempo estimado

Total: ~15-20 min. É o item mais barato do roadmap em tempo.

### Comandos para retomar

```bash
cd ~/orcamentos-openclaw
# Criar phase5_cross_insights.py (ver sketch acima)
python scripts/phase5_cross_insights.py
cat base/cross-insights-report.md
```

## Fase 6 — Iteração e melhoria contínua

**Objetivo:** melhorar a qualidade das fases anteriores reprocessando projetos problemáticos com prompts mais ricos ou modelos maiores (se gemma4:26b ficar viável no futuro).

### Alvos

1. **Re-rodar Fase 2 com prompt enriquecido** para projetos que vieram com <5 sub-disciplinas (provavelmente porque o compact view não foi suficiente). Estender o compact view pra 5-6k chars pra esses casos.

2. **Projetos com template macro** (25 projetos com ≤50 itens) — tentar pegar o xlsx alternativo se existir, ou extrair da apresentação pdf linhas que virem itens

3. **Retry de parse failures** automático: pipeline2/3 já tem `--retry-failed`. Rodar periodicamente se Gemma atualizar.

4. **Upgrade pra gemma4:26b** se Leo trocar de GPU (precisa ≥16GB VRAM). O 26b é mais preciso e mais honesto (não alucina na mesma medida), mas inviável em RTX 3050 8GB.

### Comandos para retomar

```bash
cd ~/orcamentos-openclaw

# Retry parse failures acumulados
python scripts/phase2_pipeline.py --retry-failed
python scripts/phase3_pipeline.py --retry-failed

# Re-rodar Fase 2 com compact view maior (precisa flag --big no compact_view.py ou alterar MINI_*)
# Alvo: projetos com <5 sub_disciplinas
python -c "
import json
from pathlib import Path
few = []
for p in Path('base/sub-disciplinas').glob('*.json'):
    d = json.loads(p.read_text(encoding='utf-8'))
    n = len((d.get('parsed') or {}).get('sub_disciplinas') or [])
    if n < 5: few.append((p.stem, n))
print(f'{len(few)} projetos com <5 sub_disciplinas')
for f in few: print(' ', f)
"
```

## Fase 7 — Integração com pipeline de geração de orçamentos

**Objetivo:** usar a camada qualitativa durante a **geração** de orçamentos novos (paramétricos e executivos), não só como consulta manual.

### Mudanças no `gerar_template_dinamico_v2.py`

Adicionar passo antes de preencher as abas:
1. Dado o briefing do projeto novo (AC, UR, padrão, segmento), buscar na base os 5 projetos mais similares (por AC + UR + padrão)
2. Agregar sub-disciplinas comuns desses 5 projetos por macrogrupo
3. Ao preencher a aba de um macrogrupo, **pre-popular as sub-disciplinas** com base nos projetos similares
4. Marcar na planilha quais sub-disciplinas vieram da base qualitativa (fonte rastreável)

### Mudanças no fluxo de executivo (copiloto)

A cada disciplina que Leo pede:
1. Buscar projetos similares na base
2. Listar no log-execucao.md as premissas/observações usadas como referência
3. Ao gerar o memorial, citar projetos similares como rastreabilidade

### Proposta de implementação

Criar `scripts/consulta_similares.py`:
```python
def projetos_similares(ac, ur, padrao, n=5):
    """Retorna os n projetos mais similares da base, incluindo qualitative."""
    ...

def premissas_modelo(slug_alvo, macrogrupo=None):
    """Consolida premissas técnicas de projetos similares para um macrogrupo."""
    ...
```

Essa função seria chamada pelos scripts de geração existentes (`gerar_template_dinamico_v2.py`, pipeline de executivo) e também manualmente durante conversas com Leo.

### Tempo estimado

- Escrever `consulta_similares.py`: ~30 min
- Integrar no `gerar_template_dinamico_v2.py`: ~30 min
- Validar com 1 projeto piloto: ~1h

## Ordem sugerida de retomada

Se tiver 1-2h disponíveis hoje à noite, sugiro:

1. **Fase 5** primeiro (15-20 min) — dá insights imediatos sobre a base que valem para tudo depois
2. **Fase 7.1** (`consulta_similares.py` + integração) — bloqueia menos trabalho futuro porque destrava uso prático da camada qualitativa
3. **Fase 4** se sobrar tempo — mais exploratória, resultado incerto

Se tiver 4h+:
1. Fase 5
2. Fase 7.1 + 7.2 (integração completa)
3. Fase 4 (inventário + extract_composicoes.py + primeira rodada)
4. Fase 6 iterações específicas

## Comandos úteis (cheat sheet)

```bash
cd ~/orcamentos-openclaw

# Ver estado das filas
python scripts/phase2_pipeline.py --status
python scripts/phase3_pipeline.py --status

# Re-rodar um projeto específico em qualquer fase
python scripts/extract_itens_detalhados.py <slug>
python scripts/phase2_pipeline.py <slug>
python scripts/phase3_pipeline.py <slug>
python scripts/merge_qualitative.py --slug <slug>

# Regenerar relatório consolidado
python scripts/final_report.py

# Ver JSON qualitativo de um projeto
python -c "
import json
d = json.load(open('base/indices-executivo/amalfi-tramonti.json', encoding='utf-8'))
print(json.dumps(d.get('qualitative', {}), indent=2, ensure_ascii=False)[:3000])
"

# Listar todos os .md qualitativos gerados
ls base/sub-disciplinas-md/
ls base/premissas-md/

# Começar do zero (cuidado — apaga filas, não apaga os JSONs de resultado)
rm base/phase2-queue.json base/phase3-queue.json
python scripts/gemma_queue_init.py
```

## Pré-requisitos pra rodar tudo de novo

1. Ollama rodando (`ollama serve`) com `gemma4:e4b` pulled
2. Python 3.14+ com `openpyxl`, `pypdf`, `requests`
3. Drive `G:` montado com pasta `_Entregas/Orçamento_executivo`
4. `~/orcamentos-openclaw/base/_all_projects_mapping.json` atualizado

## Referências

- Documentação canônica da camada: `CAMADA-QUALITATIVA-GEMMA.md` (neste diretório)
- Relatório consolidado: `relatorio-consolidado-YYYY-MM-DD.md` (gerado por `final_report.py`)
- Base paramétrica V2: `~/openclaw/skills/orcamento-parametrico/SKILL.md`
- Workflow canônico de orçamentos: `~/orcamentos/docs/ORCAMENTO-WORKFLOW.md`
