# Mussi vs Pass-e — Análise Interpretada

**Data:** 2026-04-18
**Dados brutos:** `base/comparacoes-clientes/mussi-vs-pass-e.md` (gerado por `scripts/comparar_clientes.py`)
**Este MD:** aplica crítica qwen R2 — documento automático era dump de dados, faltava interpretação

---

## Contexto

Mussi (4 projetos, R$/m² 2.949) e Pass-e (6 projetos, R$/m² 3.429) são **ambos médio-alto**, com AC total similar em magnitude. A diferença de R$/m² é +16.3% — aparentemente Pass-e mais caro. Mas os dados do comparador sugerem **outra história**.

---

## Achado central

### Indicadores estruturais são praticamente idênticos

| Indicador | Mussi | Pass-e | Delta |
|---|---:|---:|---:|
| concreto_m3_por_m2_ac | 0.4112 | 0.4149 | +0.9% |
| taxa_aco_kg_por_m3 | 71.57 | 73.06 | +2.1% |
| aco_kg_por_m2_ac | 31.16 | 28.00 | -10% |
| forma_m2_por_m2_ac | 2.44 | 1.41 | -42% |

Concreto e taxa de aço praticamente **iguais** (diferença <3%). Aço por m² AC tem variação moderada. Forma tem variação grande, provavelmente porque Pass-e usa forma metálica reutilizável (menos m² extraído por m² AC).

**Implicação:** a estrutura das obras é muito parecida. A diferença de R$/m² não vem de materiais estruturais caros.

### O que diferencia é estrutura de ORÇAMENTO, não de OBRA

| MG | Mussi % | Pass-e % | Diff pp | Leitura |
|---|---:|---:|---:|---|
| Instalações Gerais | 10.2% | 0.0% | -10.2pp | **Mussi mantém guarda-chuva "Instalações"; Pass-e detalha por disciplina** |
| Rev Parede | 5.4% | 0.0% | -5.4pp | **Mussi usa guarda-chuva; Pass-e desdobra** |
| Pintura Geral | 3.8% | 0.0% | -3.8pp | Mesma coisa |
| Pisos | 6.8% | 9.6% | +2.8pp | Pass-e detalha mais |
| Hidrossanitária | 12.9% | 10.1% | -2.8pp | Mussi tem Hidro no top 1; Pass-e divide |
| Gerenciamento | 9.8% | 12.0% | +2.2pp | Similar |
| Supraestrutura | 23.7% | 21.8% | -1.9pp | Similar (commodity) |
| Esquadrias | 9.4% | 7.6% | -1.8pp | Similar |

**Padrão inequívoco:** Mussi concentra ~19pp do orçamento em 3 categorias guarda-chuva ("Instalações Gerais", "Rev Parede", "Pintura Geral"). Pass-e tem **0% nessas 3** — desmembra tudo nas categorias específicas.

### Implicação para a diferença de R$/m²

A diferença **+16% da Pass-e** pode ser parcialmente explicada por:

1. **Mais detalhamento = mais margem de segurança** — quando orçamentista detalha, tende a ser mais cauteloso em cada item
2. **Volume de itens** — Mussi tem 1.765 itens/projeto (med), Pass-e 1.090 itens/projeto — contraintuitivo (Mussi tem mais itens mas orçamento mais enxuto? Ou é efeito de amostra)
3. **Maturidade do orçamentista** — equipe Cartesian evoluiu a canonização ao longo do tempo; projetos mais recentes podem ser mais detalhados

**Não podemos concluir** que Pass-e "paga mais caro real". Podemos dizer que **o orçamento Pass-e é mais detalhado e acaba agregando mais margem por item**.

---

## PUs — variação grande mas amostra pequena

| Item | Mussi PU | Pass-e PU | Delta | Possível causa |
|---|---:|---:|---:|---|
| chapisco | R$ 28.34 | R$ 6.69 | -76% | Mussi talvez inclua MO + material; Pass-e só material |
| pintura | R$ 2.70 | R$ 41.53 | +1438% | Exatamente o oposto — classificação diferente |
| contrapiso | R$ 29.20 | R$ 65.11 | +123% | Pass-e inclui nivelamento + MO; Mussi só material |
| forro_gesso | R$ 25.81 | R$ 109.52 | +324% | Idem |
| porcelanato | R$ 106.69 | R$ 108.39 | +2% | Iguais — provavelmente mesmo escopo |
| rodape | R$ 21.05 | R$ 36.19 | +72% | Possível especificação diferente |
| reboco | R$ 28.34 | R$ 28.00 | 0% | Iguais |

**⚠ Amostras n=2-3 em cada — não tirar conclusões estatísticas.**

**Hipótese mais plausível:** os dois orçamentos usam **metodologias de composição diferentes**:
- Um inclui tudo no PU ("cheio" — material + MO + encargos)
- Outro separa PU de material do PU de mão-de-obra em linhas diferentes

Só inspeção manual dos orçamentos confirma. **Não comparar PUs entre clientes sem verificar método de composição**.

---

## Qualitativa

| Cliente | Observações | Alertas | Revisões | Fora-da-curva |
|---|---:|---:|---:|---:|
| Mussi | 22 | 0 | 1 | 0 |
| Pass-e | 14 | 0 | 0 | 0 |

**Mussi teve 1 revisão** — "Revisão dos quantitativos de supraestrutura - 26.02.2021" — sem mais detalhes no registro. Pass-e com 0 revisões. Ambos com 0 alertas e 0 fora-da-curva.

Ambos têm **qualidade de dados consistente** — diferente do contraste Paludo (0) vs Nova (4 fora-da-curva).

---

## Conclusões

1. **Mussi e Pass-e são mais similares do que os números agregados sugerem** — mesma estrutura construtiva (concreto/m², taxa aço idênticos), mesma qualidade de dados (poucos alertas em ambos).

2. **A diferença +16% de R$/m² da Pass-e é majoritariamente método de orçamento** — Pass-e desmembra categorias, Mussi mantém guarda-chuvas. Quando desmembra, tende a acumular margem específica por linha.

3. **Mussi é candidato natural a template "orçamento enxuto"** — mantém macro-categorias ("Instalações", "Rev Parede", "Pintura") ao invés de desdobrar. Pode reduzir tempo de orçamento sem perder qualidade.

4. **Pass-e é candidato a template "orçamento detalhado"** — útil pra licitação onde detalhamento exigido é alto.

5. **Não concluir que Pass-e "cobra mais"** — é diferença de método, e método afeta margem por linha, mas não necessariamente custo real da obra.

---

## Recomendações operacionais

### Imediatas

1. **Pedir a 1 orçamento Mussi e 1 Pass-e**: inspeção manual do método de composição de PU (material+MO vs desmembrado). Responsável: coordenador de orçamento. Prazo: 2 semanas. Output: nota na base de conhecimento comparando métodos.

2. **Classificar projetos novos por método**: adicionar campo `metodo_composicao_pu` em `indices-executivo` (valores: "cheio" | "desmembrado" | "misto"). Permite análise mais limpa de PU cross-cliente no futuro.

### Estratégicas

3. **Padronizar detalhamento**: definir política Cartesian — detalhar sempre ou nunca? Hoje varia por orçamentista. Uniformizar reduz variância e permite comparação confiável.

4. **Educar orçamentistas sobre impacto do método**: mostrar que detalhamento adiciona margem por linha. Se cliente quer preço competitivo, usar método "cheio". Se quer comparar propostas, "detalhado".

---

## Limitações desta análise

- AC total de Pass-e inclui projetos com AC pequeno (mediana 7.319 m² vs Mussi 13.000 m²) — pode enviesar R$/m² mediana
- PUs com n=2-3 insuficientes pra análise estatística real
- Apenas 4+6 = 10 projetos totais — amostra baixa pra conclusão definitiva
- Não sabemos se clientes são da mesma região (CUB diferente afeta tudo)
- Qwen R2 notou corretamente que o relatório automático era dump de dados — esta análise interpretada foi feita manualmente em cima do dump
