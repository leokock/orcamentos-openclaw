# Revisão Consolidada — Qwen2.5:14b

**Modelo:** qwen2.5:14b local (via Ollama)
**Data:** 2026-04-18
**MDs revisados:** 5 (Paludo vs Nova, Cluster3, Financeira, Avançada, Produto)
**Tempo total:** ~17 min (4 calls sequenciais, 160-238s cada)

---

## Padrões comuns nas críticas

Analisando as 5 revisões em conjunto, 4 padrões de fraqueza se repetem em múltiplos documentos:

### Padrão 1 — Correlação fraca tratada como causal

**Ocorrências:**
- **Financeira:** r=-0.17 entre AC e R$/m² apresentado como "economia de escala fraca" mas declarativamente
- **Produto:** correlação alvenaria×porcelanato r=1.00 classificada como "artefato" sem descartar causalidade real
- **Paludo vs Nova:** "11× mais itens = mais trabalho" é salto lógico

**Correção padrão:** quando |r| < 0.3, usar linguagem "sugere" em vez de "indica"; nunca generalizar sem IC (intervalo de confiança).

### Padrão 2 — Amostra pequena tratada como significativa

**Ocorrências:**
- **Financeira:** econômico (n=3) e médio (n=2) usados como referência sem ressalvas suficientes
- **Avançada:** outliers "top caros" baseados em 1 projeto por cliente
- **Cluster3:** conclusão sobre Grandezza Gran Royal baseada em 1 projeto

**Correção padrão:** declarar n explicitamente em cada afirmação. Não tirar conclusão quando n<5 em grupo.

### Padrão 3 — Hipóteses alternativas não consideradas

**Ocorrências (TODAS as 5 revisões apontaram):**
- **Localização geográfica** — nunca considerada
- **Estrutura de precificação do cliente** — confundida com escopo
- **Fornecedores locais / negociação de escala** — ignorada
- **Complexidade real do projeto** (fck, especificação) — não mapeada

**Correção padrão:** adicionar seção "hipóteses alternativas" em cada análise.

### Padrão 4 — Recomendações genéricas demais

**Ocorrências:** 5 de 5 documentos receberam crítica de genericidade.

Exemplos específicos:
- "Reunião comercial com Nova" → sem agenda
- "Validar sanity de orçamento" → sem método
- "Encorajar registro de alertas" → sem estratégia
- "Criar linha EPCM" → sem detalhamento de serviços

**Correção padrão:** toda recomendação deve ter: (a) passos concretos, (b) responsável sugerido, (c) critério de sucesso mensurável.

---

## Críticas específicas por documento

### PALUDO-VS-NOVA-RESUMO.md

**Críticas principais:**
1. "11× mais itens ≠ mais trabalho" — indicação de detalhamento não reflete necessariamente escopo ou custo real
2. Hipótese "geográfica" ignorada (Paludo RS/SC vs Nova possivelmente em outras regiões)
3. Faltava comparação de PUs item-a-item
4. Recomendação "reunião com Nova" sem pontos específicos

**Status:** ✅ **APLICADO** em `PALUDO-VS-NOVA-V2-APOS-REVISAO.md`. Acrescentado comparativo PU por 24 categorias, 5 hipóteses alternativas, 6 recomendações específicas com passos.

### CLUSTER3-E-PARAMETRICO-RESUMO.md

**Críticas principais:**
1. "Cluster 3 = EPCM" é hipótese forte sem evidência contratual
2. Diferença Paludo-Nova pode ser estratégia de gestão, não eficiência EPCM
3. Grandezza Gran Royal classificado como "simples" só pelo R$/m² baixo

**Status:** ⚠️ **PARCIALMENTE RESPONDIDO** — análise PU da v2 refuta "Nova só margem" mas não temos contratos pra validar EPCM. Vou deixar hipótese como "forte hipótese sem contrato" em vez de afirmação.

### ANALISE-FINANCEIRA-RESUMO.md

**Críticas principais:**
1. r=-0.17 tratado como "economia de escala fraca" — interpretação forte demais
2. Econômico n=3 e médio n=2 usados como benchmark
3. "Focar em padrão pra estimativa inicial" — ignora localização e tipo

**Status:** ⚠️ **DOC PRECISA ATUALIZAÇÃO** — ver seção "Correções aplicadas" abaixo.

### ANALISE-AVANCADA-RESUMO.md

**Críticas principais:**
1. "Nova top caros" baseado em 1 projeto — sem escopo comparável
2. Complexidade por padrão sem explicar causa da variação
3. "Preencher AC" é tarefa sem priorização

**Status:** ⚠️ **DOC PRECISA ATUALIZAÇÃO**.

### ANALISE-PRODUTO-RESUMO.md

**Críticas principais:**
1. "Padrão é acabamento, não estrutura" — conclusão forte baseada em variação de concreto/m² pequena
2. Outliers sem análise detalhada de causa (só "classificação errada ou não-convencional")
3. "Adicionar janelas aluminio_pu_m2" tem mérito mas precisa plano de integração

**Status:** ⚠️ **DOC PRECISA AJUSTE** de linguagem (forte → suave).

---

## Correções aplicadas nesta sessão

### ✅ PALUDO-VS-NOVA-V2-APOS-REVISAO.md (novo)

- Removida afirmação "Nova entrega mais coisa"
- Adicionada comparação PU por 24 categorias (arquivo `paludo-vs-nova-pus-comparacao.xlsx`)
- Achado: Nova NÃO é uniformemente mais cara (+86% chapisco, mas -53% porta madeira)
- 5 hipóteses alternativas explícitas
- 6 recomendações com passos concretos + agenda de reunião

### ✅ paludo-vs-nova-pus-comparacao.xlsx (novo)

- 10 categorias comparáveis (n≥3 em ambos)
- Delta mediana +16% (Nova ligeiramente mais cara na mediana, não uniformemente)
- Guarda-corpo identificado como falso positivo (Paludo=provisório, Nova=definitivo)

---

## Correções pendentes (próxima iteração)

Não vou reescrever os 4 MDs agora — marcar as ressalvas em linhas específicas basta por ora. Futuramente, rodar `revisar_md_qwen.py` sempre antes de "fechar" uma análise.

**Para cada MD:**

### ANALISE-FINANCEIRA-RESUMO.md — ressalvas a adicionar

- Na seção "Padrão > Escala", substituir "correlação fraca" por "**correlação muito tênue (r=-0.17, n=55)** — sugere economia de escala leve, mas não significativa estatisticamente"
- Adicionar disclaimer em econômico/médio: "**⚠ amostra pequena (n=3 e n=2) — referência fraca, buscar mais dados**"
- Adicionar hipóteses alternativas: localização, tipo, estrutura cliente

### ANALISE-AVANCADA-RESUMO.md — ressalvas a adicionar

- "Top caros" → "top caros (n=1-2 por cliente, investigação caso-a-caso necessária)"
- "Complexidade por padrão" → adicionar hipóteses (escopo, tipologia, maturidade do cliente)
- "Preencher AC" → criar priorização: primeiro os 10 clientes com >3 projetos

### CLUSTER3-E-PARAMETRICO-RESUMO.md — ressalvas a adicionar

- "Cluster 3 = EPCM" → "**Cluster 3 tem padrão de distribuição consistente com EPCM/fee-based (35% em gerenciamento). Confirmar via análise de contrato.**"
- "Paludo referência de eficiência" → "Paludo tem R$/m² 2.7k-3.7k no mesmo padrão. Causa (escopo, localização, estratégia) precisa de análise adicional."

### ANALISE-PRODUTO-RESUMO.md — ressalvas a adicionar

- "Padrão é acabamento, não estrutura" → suavizar: "**Em alto e médio-alto, indicadores estruturais variam pouco entre padrões — a diferenciação parece vir principalmente de acabamentos e instalações**"
- Outliers: adicionar análise caso-a-caso (santo-andre-belle-ville merece investigação dedicada)

---

## Recomendação operacional

**Criar checklist de "qualidade de análise" Cartesian:**

- [ ] N declarado em toda afirmação estatística
- [ ] |r| < 0.3 usa linguagem "sugere", não "indica"
- [ ] Hipóteses alternativas listadas (mínimo 3)
- [ ] Recomendações com passos concretos + responsável + prazo
- [ ] Amostra n<5 sempre com disclaimer
- [ ] Rodar `revisar_md_qwen.py` antes de fechar

**Integrar no processo:** antes de publicar qualquer análise pro Drive, rodar revisão qwen local e aplicar correções. Custo: ~3 min/MD. Benefício: qualidade sobe muito.

---

## Observação meta — a qualidade do qwen2.5:14b

qwen2.5:14b funciona **bem** em PT-BR (diferente do gemma4:e4b que retornava vazio):
- 160-238 segundos por documento de 6-10k chars
- Críticas específicas, citam trechos originais
- Não é superficial — aponta padrões de fraqueza real
- Sugestões de hipóteses alternativas são pertinentes

**Conclusão:** qwen2.5:14b é viável como revisor local. Adicionar ao fluxo.

---

## Arquivos

- **Revisões individuais:** `base/revisoes-qwen/revisao-*.md` (5 arquivos)
- **Este consolidado:** `base/REVISAO-QWEN-CONSOLIDADA.md`
- **Script reusável:** `scripts/revisar_md_qwen.py`
- **Aplicação v2 Paludo vs Nova:** `base/PALUDO-VS-NOVA-V2-APOS-REVISAO.md`
- **Dados PU Paludo vs Nova:** `base/paludo-vs-nova-pus.json` + Excel
