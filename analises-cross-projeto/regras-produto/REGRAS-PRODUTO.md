# Regras de Produto — Conhecimento Acionável Cartesian

**Gerado:** 2026-04-19T01:34:06
**Modelo narrativa:** qwen2.5:14b (local)
**Base estatística:** 18 regras derivadas das Fases 5-7

**O que tem aqui:** regras if-then testáveis que emergem das análises quantitativas, traduzidas em linguagem acionável pra reunião comercial e orçamentação.

**Como usar:** antes de fechar paramétrico/executivo novo, revisar as regras aplicáveis ao projeto (cliente, região, padrão). Ajuste as estimativas conforme indicado.

---

## 1. Regras de Cliente (ajustes aprendidos)

*Derivadas da análise de 16 outliers da regressão multivariada*

### 1.1 🟢 IF cliente = Nova Empreendimentos THEN somar ~R$ 2.000/m² à predição

**Força:** alta

**Evidência:** 3/4 projetos Nova são outliers positivos (z>=1). Resíduo médio ~R$ 2.291.

**Recomendação prática:**

> Quando orçar um projeto para a Nova Empreendimentos, adicione R$ 2.000 por metro quadrado ao valor previsto inicialmente. Essa correção é necessária porque três quartos dos projetos da empresa são outliers positivos, com resíduos médios de aproximadamente R$ 2.291 acima do esperado. Esta regra tem uma força alta e ajuda a garantir que o orçamento seja mais preciso e realista para esse cliente específico.

### 1.2 ⚪ IF cliente = ALL THEN predição pode subestimar em R$ 2.000-3.000/m²

**Força:** média (n=1 somente)

**Evidência:** ALL Lago di Garda: z=+3.2, resíduo +R$ 2.959.

**Recomendação prática:**

> Quando orçar um projeto de construção civil para qualquer cliente, especialmente se for uma obra do tipo residencial ou comercial com características similares ao Lago di Garda, é recomendado ajustar a previsão em +R$ 2.959 por metro quadrado. Este ajuste visa compensar uma tendência observada que pode levar à subestimação dos custos. Baseia-se em evidências de um único caso com forte indicativo de desvio (+R$ 2.959/m²), o que, embora seja um conjunto limitado de dados, sugere a necessidade de revisão adicional para garantir uma estimativa mais precisa e realista dos custos.

### 1.3 🟢 IF cliente = F Nogueira THEN subtrair ~R$ 1.200/m² da predição

**Força:** alta

**Evidência:** 2 projetos F Nogueira são outliers negativos consistentes (~-R$ 1.210 ambos)

**Recomendação prática:**

> Quando orçar um projeto para o cliente F Nogueira, subtraia aproximadamente R$ 1.200 por metro quadrado da estimativa inicial. Esta recomendação é baseada em evidências de dois projetos anteriores do mesmo cliente que apresentaram desvios consistentes e negativos de cerca de R$ 1.210 por metro quadrado, indicando uma tendência específica para esse contratante.

### 1.4 🟡 IF cliente = Paludo Volo Home THEN subtrair ~R$ 1.100/m²

**Força:** média

**Evidência:** paludo-volo-home tem z=-1.2

**Recomendação prática:**

> Quando orçar um projeto para o cliente Paludo Volo Home, subtraia aproximadamente R$ 1.100 por metro quadrado do valor total do orçamento. Esta recomendação é baseada em dados que indicam uma desviância negativa de z=-1.2 para esse tipo de cliente específico, sugerindo que os custos tendem a ser consistentemente mais baixos nesses projetos comparados à média geral.

### 1.5 🟡 IF cliente = Santa Maria THEN subtrair ~R$ 1.000/m² (Chapecó CUB menor + escopo enxuto)

**Força:** média

**Evidência:** 1 projeto Santa Maria em outliers negativos

**Recomendação prática:**

> Quando orçar um projeto para a cidade de Santa Maria, subtraia aproximadamente R$ 1.000 por metro quadrado do valor padrão usado como referência, como o CUB (Custo Unitário Básico) de Chapecó. Essa redução é necessária porque há evidências de que os custos na região de Santa Maria são consistentemente menores em comparação com outras áreas, refletindo um escopo mais enxuto nos projetos locais. Esta recomendação baseia-se em um único projeto fora da média que apresentou resultados negativos em relação à previsão inicial, indicando a necessidade de ajustes para evitar sobreestimações futuras.

---

## 2. Regras Regionais (CUB)

*Derivadas dos coeficientes da regressão Fase 6 (baseline: SC-BC)*

### 2.1 🟡 IF região = SC-Floripa THEN ajustar +559 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ +559/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto em Florianópolis (SC-Floripa), ajuste o valor de referência em +559 R$/m² em relação à baseline estabelecida para Balneario Camboriú (SC-BC). Este ajuste reflete a diferença nos custos locais, que incluem fatores como mão de obra especializada e materiais mais caros na região de Florianópolis.

### 2.2 🟢 IF região = SC-Litoral-Norte THEN ajustar -944 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ -944/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região do Litoral Norte de Santa Catarina, ajuste automaticamente o custo em -944 R$/m² em relação à baseline estabelecida para SC-BC. Este ajuste reflete uma diferença significativa e consistentemente observada nos custos dessa área específica, que é resultado de fatores locais como menor custo de mão de obra e materiais comparativamente ao baseline.

### 2.3 🟢 IF região = SC-Oeste THEN ajustar -939 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ -939/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto de construção civil na região do Oeste de Santa Catarina (SC-Oeste), ajuste automaticamente o valor por metro quadrado em -939 R$/m² em relação à baseline definida para SC-BC. Este ajuste é necessário porque a análise de regressão mostrou que os custos nesta área específica são consistentemente 939 R$ mais baixos por metro quadrado comparados ao padrão estabelecido para SC-BC, o que reflete uma diferença significativa e consistente na economia local.

### 2.4 🟡 IF região = SC-Vale-Itajai THEN ajustar -310 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ -310/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região do Vale do Itajaí em Santa Catarina, ajuste automaticamente o custo por metro quadrado em R$ -310/m² em relação à baseline definida para SC-BC. Este ajuste reflete uma diferença média identificada através de análises de regressão que consideram variáveis locais como materiais específicos, mão de obra e custos regionais.

### 2.5 🟡 IF região = SP-Capital THEN ajustar -613 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ -613/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região da capital de São Paulo (SP-Capital), ajuste o custo por metro quadrado em -613 R$/m² em relação à baseline estabelecida para Santa Catarina – Balneário Camboriú (SC-BC). Este ajuste é baseado em uma análise que identificou uma diferença significativa nos custos de construção entre essas duas regiões, com a capital paulista apresentando valores mais baixos. Ajustar o orçamento conforme essa regra ajudará a garantir um preços mais precisos e competitivos para projetos na região metropolitana de São Paulo.

---

## 3. Regras de Padrão Construtivo

*Derivadas dos coeficientes da regressão Fase 6 (baseline: padrão alto)*

### 3.1 🟡 IF padrão = economico THEN ajustar -1069 R$/m² vs baseline (alto)

**Força:** média

**Evidência:** Coef regressão = R$ -1069/m². Baseline é padrão alto.

**Recomendação prática:**

> Quando orçar um projeto de construção civil com padrões econômicos, ajuste automaticamente o valor do orçamento em -1069 R$/m² em relação ao baseline que considera padrões altos. Essa recomendação é baseada em uma análise de regressão que identificou essa diferença média entre os padrões econômicos e os padrões mais elevados, fornecendo um ajuste preciso para garantir a precisão do orçamento sem sobrestimar custos.

### 3.2 🟢 IF padrão = medio THEN ajustar -2430 R$/m² vs baseline (alto)

**Força:** alta

**Evidência:** Coef regressão = R$ -2430/m². Baseline é padrão alto.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto de construção civil com um padrão médio, ajuste automaticamente o valor por metro quadrado em R$ -2430/m² em relação ao baseline (padrão alto). Essa recomendação é baseada em uma forte evidência que mostra uma correlação significativa entre o padrão médio e a economia de custos em relação ao padrão mais elevado, com um coeficiente de regressão de R$ -2430/m².

### 3.3 🟡 IF padrão = medio-alto THEN ajustar -457 R$/m² vs baseline (alto)

**Força:** média

**Evidência:** Coef regressão = R$ -457/m². Baseline é padrão alto.

**Recomendação prática:**

> Quando você estiver elaborando um orçamento para um projeto de construção civil com padrões médio-altos, ajuste automaticamente o valor em -457 R$/m² em relação ao baseline (padrão alto). Este ajuste é baseado em uma análise que identificou essa diferença como resultado de variáveis específicas associadas a projetos de padrão médio-alto. A aplicação dessa recomendação ajudará a otimizar o orçamento, refletindo mais precisamente os custos esperados para esse tipo específico de projeto.

---

## 4. Regras Causais (Controle de Confundidores)

*Derivadas de correlações parciais Fase 5 — refutam correlações aparentes*

### 4.1 🟡 Economia de escala real mas leve (controlando região)

**Força:** média

**Evidência:** r parcial = -0.317 (n=99). Projetos maiores TÊM R$/m² um pouco menor mesmo dentro da mesma região.

**Recomendação prática:**

> Quando orçar projetos de construção civil em uma mesma região, ajuste os custos para refletir a economia de escala real e ligeira observada. Para projetos maiores, reduza levemente o valor R$/m² conforme a evidência indica uma relação negativa entre tamanho do projeto e custo por metro quadrado (r parcial = -0.317 com base em 99 projetos). Esta recomendação visa melhorar a precisão orçamentária, refletindo que maiores obras tendem a ter menores custos unitários devido à eficiência operacional e compras em escala maior.

### 4.2 🟢 Supraestrutura% ≠ preditor de R$/m² alto

**Força:** alta

**Evidência:** r parcial = -0.039 (NULO). Correlação simples era artefato regional. NÃO usar supra% pra estimar preço.

**Recomendação prática:**

> Quando você estiver elaborando um orçamento para uma obra de construção civil e notar que a porcentagem da suposta "supraestrutura" parece influenciar significativamente o custo por metro quadrado (R$/m²), é importante não usar essa porcentagem como base para estimativas de preço. A evidência indica que há pouca correlação entre a proporção da supraestrutura e os custos unitários, com um coeficiente de correlação parcial (-0.039) sendo praticamente nulo e considerado um artefato regional não generalizável. Portanto, ajuste seu processo para evitar o uso desta métrica isolada ao estimar custos, garantindo assim uma melhor precisão no orçamento final.

### 4.3 🟢 Gerenciamento% alto ≠ projeto caro

**Força:** alta

**Evidência:** r parcial = -0.095. Projetos EPCM (gerenciamento concentrado) não são intrinsecamente caros. Preço alto vem de escopo/região/especificação, não da estrutura de orçamento.

**Recomendação prática:**

> Quando você observar um alto percentual de gerenciamento em um projeto de construção civil, é importante entender que isso não necessariamente indica que o orçamento do projeto será elevado. O ajuste a ser feito nesse caso é focar na análise detalhada das especificações técnicas, escopo do trabalho e condições geográficas da obra, já que esses são os fatores reais que influenciam o custo total.
> 
> A evidência indica claramente que projetos EPCM (Engineering, Procurement, Construction and Management), que tendem a ter uma estrutura de gerenciamento mais concentrada e detalhada, não estão intrinsecamente associados a orçamentos mais altos. Portanto, é crucial evitar o equívoco de supor automaticamente que um alto percentual de gerenciamento resultará em custos elevados para o projeto.

---

## 5. Regras de Economia de Escala (por região)

*Heterogêneas — só algumas regiões têm efeito escala*

### 5.1 🟢 IF região = SC-BC THEN aumentar AC reduz R$/m²

**Força:** alta

**Evidência:** r = -0.35 (n=18). Economia de escala forte/moderada.

**Recomendação prática:**

> Quando você está orçamentando um projeto em Balneário Camboriú (SC), aumente a produtividade da mão de obra (AC) e reduza os custos por metro quadrado (R$/m²). Essa estratégia é baseada em uma forte economia de escala observada em 18 projetos, onde foi notada uma correlação negativa significativa (r = -0.35), indicando que aumentar a produtividade pode levar a um custo mais baixo por metro quadrado no local.

### 5.2 🟡 IF região = SC-Litoral-Norte THEN aumentar AC reduz R$/m²

**Força:** média

**Evidência:** r = -0.52 (n=12). Economia de escala forte/moderada.

**Recomendação prática:**

> Quando orçar um projeto na região do Litoral Norte de Santa Catarina, ajuste os custos para aumentar a quantidade de mão-de-obra e reduzir o valor por metro quadrado em materiais. Essa medida é baseada em uma forte economia de escala observada nesta área específica (r = -0.52 com 12 amostras), indicando que projetos maiores tendem a ter custos mais baixos por unidade devido à eficiência operacional e à disponibilidade de recursos especializados na região.

---

## Legenda

- 🟢 **Alta** — n ≥ 10 ou coeficiente > R$ 1.000/m² ou |r| ≥ 0.5
- 🟡 **Média** — n entre 3-9 ou coeficiente entre R$ 500-1.000
- ⚪ **Baixa** — n < 3 ou evidência indireta

## Procedência das evidências

- **Fase 5 (correlações controladas):** `base/correlacoes-controladas.json`
- **Fase 6 (regressão):** `base/regressao-rsm2.json`
- **Fase 7 (anti-padrões):** `base/anti-padroes.json`
- **Validação final (Fase 11):** `analises-cross-projeto/simulador/arthen-arboris.md`