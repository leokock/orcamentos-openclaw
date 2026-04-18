# Checklist de Qualidade de Análise — Cartesian

**Base:** padrões de crítica detectados em 12 revisões qwen2.5:14b (R1 + R2) sobre 9 MDs de análise
**Uso:** antes de publicar qualquer nova análise, rodar este checklist. Depois, rodar `scripts/revisar_md_qwen.py`.

---

## Parte 1 — Rigor estatístico

### ☐ N explicitado em toda afirmação numérica
Exemplo ruim: "Mediana R$/m² é R$ 3.443"
Exemplo bom: "Mediana R$/m² é R$ 3.443 (n=31, com AC ≥ 1.000m²)"

### ☐ Correlação |r| < 0.3 usa linguagem "sugere", não "indica"
Exemplo ruim: "r=-0.17 → economia de escala fraca"
Exemplo bom: "r=-0.17 (n=55) — correlação muito tênue, *sugere* economia de escala leve, não estatisticamente significativa"

### ☐ Amostras com n<5 NÃO aparecem na tabela principal
Mover para apêndice com aviso "NÃO usar como benchmark".
Exemplo aplicado: análise financeira removeu econômico (n=3) e médio (n=2) da tabela principal.

### ☐ Percentis sempre com n explícito e intervalo
Exemplo bom: "R$/m² alto: p25 R$ 3.217 – p75 R$ 5.200 (n=19)"

### ☐ Outliers automáticos ≠ conclusão definitiva
Projeto fora de p90/p10 é **sinal**, não **veredicto**. Deve sempre vir com "merece investigação dedicada".

---

## Parte 2 — Hipóteses alternativas

### ☐ Seção "Hipóteses alternativas" obrigatória
Mínimo 3 hipóteses além da principal. Qwen R1 e R2 apontaram sistematicamente esse gap.

### ☐ Hipóteses comuns a considerar (check explícito)

- **Localização geográfica** (CUB regional, custo MO local, logística)
- **Tipologia** (residencial, misto, comercial, industrial, retrofit)
- **Fornecedores/escala** (grandes clientes negociam volume)
- **Eficiência operacional interna do cliente** (não subestimar)
- **Especificação técnica** (fck, espessura, acabamento premium)
- **Estrutura de orçamento** (guarda-chuva vs detalhado)
- **Qualidade de dados fornecidos pelo cliente** (dados incompletos geram margem de segurança)
- **Práticas contábeis** (CI classificado diferente entre empresas)

### ☐ Cada hipótese é validável? Com quais dados?
Se hipótese H5 requer "CUB regional por categoria", marcar como **não validável com dados atuais**, não apenas omitir.

---

## Parte 3 — Recomendações operacionais

### ☐ Toda recomendação tem 3 elementos mínimos:
1. **Passos concretos** (o que fazer, em ordem)
2. **Responsável nominal ou por papel** (quem faz)
3. **Critério de sucesso mensurável** (quando saber que deu certo)

### ☐ Exemplos ruins vs bons

**Ruim:** "Preencher AC dos clientes que faltam"
**Bom:** "Preencher AC dos 8 projetos CK até 31/05/2026. Responsável: Patricia (relacionamento CK). Método: extrair do memorial descritivo, não extrapolar. Sucesso: 8/8 com AC válido (≥1.000 m²) registrados em `indices-executivo`."

**Ruim:** "Encorajar registro de alertas"
**Bom:** "Adicionar campo 'riscos/alertas' no briefing (mín 2 itens). Reunião mensal de orçamentistas com leitura dos alertas da base (1h, primeira segunda-feira). Responsável: coordenador de orçamento. Meta 3 meses: 21→40 alertas."

### ☐ Recomendações 100% dependentes de dados externos são marcadas como "bloqueadas"
Exemplo: "Validar hipótese EPCM" → **bloqueada em consulta a 1 contrato**. Responsável comercial, não orçamentista.

---

## Parte 4 — Linguagem e inferência

### ☐ "Sugere" vs "Indica" vs "Confirma"
- **Confirma:** evidência forte, teste estatístico com IC
- **Indica:** correlação moderada, múltiplos indícios
- **Sugere:** correlação fraca ou amostra pequena — não tirar conclusão gerencial

### ☐ Inferências baseadas em 1 único item são sinal de atenção
Exemplo: concluir "Paludo usa acabamento premium" baseado só em porta de madeira 2× o preço de Nova.
**Ação:** declarar "hipótese baseada em 1 item, validar com outros acabamentos".

### ☐ "Refinamento" vs "Mudança" vs "Discrepância"
- **Refinamento:** grupo original ainda visível, só melhor separado
- **Mudança:** grupo original se dissolveu, novos clusters emergiram
- **Discrepância:** resultado inesperado, requer investigação

Nunca usar "refinamento" sem explicar **por que** é refinamento.

---

## Parte 5 — Processo de publicação

### ☐ Antes de salvar `.md` como versão final:

1. ☐ Rodar checklist acima manualmente (5 min)
2. ☐ Rodar `scripts/revisar_md_qwen.py --file seu_md.md` (~4 min)
3. ☐ Ler revisão qwen. Aplicar críticas válidas
4. ☐ Rodar `scripts/revisar_md_qwen.py --file seu_md.md --suffix="-r2"` (~4 min) **apenas se MD foi significativamente reescrito**
5. ☐ Commit no git `orcamentos-openclaw`
6. ☐ Sincronizar pro Drive em `~/orcamentos/parametricos/`

### ☐ Quando parar de refinar:
- Após R2, se MDs têm mesma quantidade de críticas que R1 sem pioorar, **parar**. Críticas remanescentes são limitações de dados, não de análise.
- **R3 é raro** — só em MD crítico que passou por reescrita maior.

---

## Parte 6 — Limitações conhecidas da base Cartesian

(Declarar em qualquer análise nova como ressalvas transversais)

- **Localização:** só 5/126 projetos têm cidade/UF explícita em qualitative
- **Tipologia:** não há campo estruturado (residencial/comercial/misto) em indices-executivo
- **Data_base:** só 14/126 projetos têm — impossível análise temporal/inflação
- **Contratos:** não temos acesso aos contratos assinados → hipóteses EPCM/fee-based são **sinais estatísticos**, não confirmações
- **Especificação técnica por item:** não temos especificação detalhada (fck, gramatura, classe de tinta) — comparação de PU sem essa info tem limite
- **PU por item:** 335-826 descrições únicas por cliente, canonização matching tem erro
- **Paramétrico ↔ Executivo:** 0 pares rastreáveis hoje (4 paramétricos ativos, 126 executivos legados). Ver `scripts/check_slug_consistency.py`

---

## Uso prático

Colar esta ordem de seções em todo MD novo de análise:

```markdown
# [Título]

**Gerado em:** [data]
**Base:** [n projetos, filtros aplicados]
**N mínimo aplicado:** [ex: AC ≥ 1.000 m², R$/m² ∈ [500, 10.000]]

## Limitações desta versão
[lista de limitações transversais + específicas da análise]

## Hipóteses principais
[1-3 conclusões, cada uma com grau: sugere/indica/confirma + evidência]

## Hipóteses alternativas
[mínimo 3, com info de quais dados externos validariam]

## Recomendações operacionais
[cada uma: passos concretos + responsável + critério de sucesso]

## Apêndice (opcional)
[amostras pequenas, dados brutos, detalhes técnicos]
```

---

## Histórico de aplicação

| MD | R1 | R2 | Status |
|---|---|---|---|
| PALUDO-VS-NOVA-RESUMO | ✓ | — | Substituído por V2 |
| PALUDO-VS-NOVA-V2-APOS-REVISAO | ✓ | ✓ | 6 hipóteses (H1-H6), correções aplicadas |
| CLUSTER3-E-PARAMETRICO-RESUMO | ✓ | ✓ | Protocolo slug com responsável + métrica |
| ANALISE-FINANCEIRA-RESUMO | ✓ | ✓ | Amostras pequenas movidas pro apêndice |
| ANALISE-AVANCADA-RESUMO | ✓ | (em R2b) | Ressalvas R1 aplicadas |
| ANALISE-PRODUTO-RESUMO | ✓ | (em R2b) | Ressalvas R1 aplicadas |
| SESSAO-18ABR-RESUMO | — | ✓ | Explicação redistribuição clusters |
| mussi-vs-pass-e | — | (em R2b) | — |

**Próximas análises:** todas devem passar por este checklist + revisão qwen antes da publicação.
