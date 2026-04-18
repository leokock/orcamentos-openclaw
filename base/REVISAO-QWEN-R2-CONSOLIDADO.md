# Revisão Qwen — Round 2 Consolidado

**Gerado:** 2026-04-18
**Round 1:** `REVISAO-QWEN-CONSOLIDADA.md` (5 MDs iniciais)
**Round 2:** este documento — valida MDs corrigidos + revisa documentos novos

**Objetivo:** medir se as correções aplicadas após Round 1 foram eficazes, e capturar críticas novas.

---

## Resumo executivo

| MD | R1 críticas | R2 críticas | Mudança |
|---|---:|---:|---|
| PALUDO-VS-NOVA-V2-APOS-REVISAO | (novo doc) | 3 saltos lógicos + 2 hipóteses + 3 dados faltantes | — |
| ANALISE-FINANCEIRA-RESUMO | 3 saltos | 3 saltos + 3 hipóteses + 4 dados + genéricas | **similar (não piorou, não resolveu)** |
| CLUSTER3-E-PARAMETRICO-RESUMO | 3 saltos | 2 saltos + 2 hipóteses novas | **menos grave** |
| SESSAO-18ABR-RESUMO | (não revisado R1) | 2 saltos + 2 hipóteses + 3 dados faltantes | — |

**Padrão do Round 2:**
- Críticas mais **cirúrgicas** e profundas, menos "salto genérico"
- Aponta **hipóteses alternativas novas** não cobertas na v1 (ex: eficiência operacional interna)
- Pede **dados externos específicos** (contratos, especificações, CUB regional)
- Pede **cronograma + responsável nominal** nas ações

---

## PALUDO-VS-NOVA-V2-APOS-REVISAO — Round 2

**Críticas novas (que não estavam no R1):**

### 1. H4 "especificação premium" baseada só em porta de madeira
> "Paludo especifica acabamento premium (H4) é suposição sem evidências além de porta de madeira. Não há dados comparativos diretos sobre qualidade dos produtos."

**Status:** ⚠️ **crítica VÁLIDA** — a v2 inferiu "premium" de 1 item só. **Correção possível:** adicionar ressalva que "H4 precisa ser validada com especificação técnica dos produtos (tipo de porta, espessura vidro, gramatura de tinta)".

### 2. Localização precisa CUB regional específico
> "H5 sobre localização/custo regional poderia ser mais explorada com dados específicos de custos regionais (CUB) para cada categoria universal, não apenas uma observação genérica."

**Status:** ⚠️ **VÁLIDA mas NÃO corrigível aqui** — precisa dos dados de localização (temos em apenas 5 dos 126 projetos).

### 3. "Análise projetos-pares" pressupõe semelhança além do tamanho
> "Sugere-se analisar o projeto-pares (Paludo Volo Home vs Nova Malaga) como comparação quase direta, mas isso pressupõe semelhanças significativas além do tamanho."

**Status:** ⚠️ **VÁLIDA**. **Correção:** qualificar "comparação quase direta" → "comparação de projetos similares em escala (AC 3.9k vs 4.4k) — outras variáveis (tipologia, localização, especificação) ainda precisam ser controladas."

### 4. Reunião comercial sem estratégia baseada em respostas
> "As perguntas-chave são boas, mas seria útil ter um esboço da estratégia de negociação baseada nas respostas."

**Status:** ⚠️ **VÁLIDA mas escopo amplia análise** — demanda estratégia comercial completa, que é outra análise.

---

## CLUSTER3-E-PARAMETRICO-RESUMO — Round 2

**Críticas persistentes (do R1, não totalmente resolvidas):**

### 1. Hipótese EPCM ainda sem evidência contratual
Mesmo com ressalva adicionada em R1, qwen volta a apontar:
> "A hipótese é baseada apenas no padrão observado na distribuição percentual do gerenciamento, sem evidências contratuais."

**Status:** 🔵 **Corretamente persistente** — só resolve com dados externos (ler contratos). Aceitar como limitação conhecida.

### 2. Diferença Paludo vs Nova pode ser eficiência operacional (NOVA HIPÓTESE)
> "A conclusão que a diferença é apenas contexto comercial e escopo não considera eficiência operacional interna ou práticas contábeis diferentes entre os clientes."

**Status:** ⚠️ **Hipótese NOVA importante** — R1 não tinha essa. **Correção possível:** adicionar H6 à análise Paludo vs Nova: "eficiência operacional interna do cliente (métricas de produtividade, uso de recursos, práticas contábeis)".

### 3. Ação "manter slug" ainda genérica
> "Esta recomendação é muito genérica e não especifica como garantir que os slugs sejam mantidos consistentes. É necessário um protocolo operacional detalhado, incluindo responsabilidades específicas de equipes e ferramentas para monitorar."

**Status:** ⚠️ **VÁLIDA**. **Correção:** especificar responsável (orçamentista que fecha paramétrico) + ferramenta (script `check_slug_consistency.py` a criar).

---

## ANALISE-FINANCEIRA-RESUMO — Round 2

**Críticas R2 (qwen foi persistente mesmo com correções R1):**

### 1. Amostras pequenas ainda apresentadas (R1 marcou, R2 pede remoção)
> "A análise afirma que as amostras econômico e médio são insuficientes para conclusões estatísticas (n=3 e n=2), mas ainda assim apresenta valores medianos e deltas. Esses dados não devem ser usados como referência fraca."

**Status:** ⚠️ **VÁLIDA** — disclaimer do R1 não foi suficiente. **Correção aplicada:** medianas de econômico/médio movidas para **Apêndice** com aviso "NÃO usar como benchmark", tabela principal agora tem apenas alto (n=19) e médio-alto (n=31).

### 2. Correlação r=-0.17 ainda sugere economia de escala
**Status:** ⚠️ Persistente — mesmo com ressalva "tênue", qwen considera que dizer "sugere economia de escala leve" ainda é forte. Aceitar como limitação de escolha de linguagem.

### 3. Recomendações sem considerar localização/tipologia
**Status:** ⚠️ **VÁLIDA**. **Correção aplicada:** recomendações "Empreitada direta" e "Negociação com fornecedores" ganharam ressalvas sobre condições locais + diretrizes concretas (consolidar volume, comparar com PU de referência, 3 cotações acima de R$ 50k).

---

## SESSAO-18ABR-RESUMO — Round 2 (primeira revisão deste MD)

### 1. Redistribuição de clusters — mudança ≠ refinamento
> "A afirmação 'Cluster 3 virou Cluster 1 + parte do Cluster 3 — refinamento, não discrepância' é vaga e carece de evidências. Não está claro como a redistribuição foi feita e por que constitui refinamento."

**Status:** ⚠️ **VÁLIDA**. **Correção possível:** adicionar seção "Impacto da canonização nos clusters" com tabela antes/depois detalhada.

### 2. Fichas Amalfi/Chiquetti N/D sem cronograma
**Status:** ⚠️ Já endereçado parcialmente no ANALISE-AVANCADA-RESUMO.md corrigido (priorização CK primeiro), mas SESSAO ainda não refletia.

### 3. Falta plano de integração qualitativa → fichas
> "Observações qualitativas serão integradas com as fichas comerciais. Seria necessário um plano mais detalhado sobre a metodologia."

**Status:** ✅ **JÁ IMPLEMENTADO** no commit posterior (seção "PONTOS DE ATENÇÃO" nas fichas com alertas/revisões/fora-curva destacados). SESSAO precisa atualização.

---

## Correções aplicáveis agora (sem dados externos novos)

### Ações diretas:

1. **PALUDO-VS-NOVA-V2:** adicionar **H6 — Eficiência operacional interna** (nova hipótese do R2 CLUSTER3)
2. **PALUDO-VS-NOVA-V2:** ressalva H4 "premium baseado em 1 item" + qualificar "projeto-pares"
3. **CLUSTER3:** ressalva "H6 eficiência operacional" como hipótese alternativa
4. **SESSAO-18ABR:** atualizar seção "qualitativa nas fichas" (já implementado, só documentar)

### Aceitar como limitações (não corrigíveis sem dados novos):

- Localização com CUB regional por projeto
- Contratos pra validar EPCM
- Especificações técnicas para validar "premium"
- Métricas de produtividade interna dos clientes

---

## Padrão geral observado: retornos decrescentes mas não nulos

O R2 mostra:
- **Correções do R1 funcionaram** — críticas R2 não repetem R1 principais
- **Críticas R2 são mais profundas** — pedem dados externos ou sinalizam hipóteses novas
- **Algumas correções criam novas perguntas** — ciclo infinito se não parar

**Recomendação operacional:** rodar qwen **uma vez** por MD, aplicar correções, **parar**. Rodar múltiplas vezes no mesmo MD tem retorno decrescente (e custo crescente — 10 min por doc grande).

Exceção: rodar 2ª vez em MDs **significantemente reescritos** (como PALUDO-VS-NOVA-V2 foi) pra validar.

---

## Arquivos

- Revisões R1: `base/revisoes-qwen/revisao-*.md` (sem sufixo)
- Revisões R2: `base/revisoes-qwen/revisao-*-r2.md`
- R1 consolidado: `base/REVISAO-QWEN-CONSOLIDADA.md`
- **Este R2 consolidado:** `base/REVISAO-QWEN-R2-CONSOLIDADO.md`
