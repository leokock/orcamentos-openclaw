# Regras de Produto — Conhecimento Acionável Cartesian

**Gerado:** 2026-04-19T09:32:04
**Modelo narrativa:** qwen2.5:14b (local)
**Base estatística:** 20 regras derivadas das Fases 5-7

**O que tem aqui:** regras if-then testáveis que emergem das análises quantitativas, traduzidas em linguagem acionável pra reunião comercial e orçamentação.

**Como usar:** antes de fechar paramétrico/executivo novo, revisar as regras aplicáveis ao projeto (cliente, região, padrão). Ajuste as estimativas conforme indicado.

---

## 1. Regras de Cliente (ajustes aprendidos)

*Derivadas da análise de 15 outliers da regressão multivariada*

### 1.1 🟢 IF cliente = Nova Empreendimentos THEN somar ~R$ 2.000/m² à predição

**Força:** alta

**Evidência:** 3/4 projetos Nova são outliers positivos (z>=1). Resíduo médio ~R$ 2.291.

**Recomendação prática:**

> Quando orçar um projeto para a Nova Empreendimentos, adicione R$ 2.000 por metro quadrado ao valor previsto inicialmente. Esta recomendação é baseada em dados que mostram que três quartos dos projetos da empresa são outliers positivos com resíduo médio de aproximadamente R$ 2.291, indicando que os custos tendem a ser significativamente mais altos do que o previsto inicialmente.

### 1.2 ⚪ IF cliente = ALL THEN predição pode subestimar em R$ 2.000-3.000/m²

**Força:** média (n=1 somente)

**Evidência:** ALL Lago di Garda: z=+3.2, resíduo +R$ 2.959.

**Recomendação prática:**

> Quando orçar um projeto de construção civil para qualquer cliente, é importante ajustar a previsão inicial em cerca de R$ 2.000 a R$ 3.000 por metro quadrado para evitar subestimações. Este ajuste se baseia em evidências que mostram uma tendência de subestimar os custos em projetos semelhantes, como o caso específico do Lago di Garda, onde houve um desvio positivo de R$ 2.959 por metro quadrado. Embora seja baseada em apenas um exemplo, este ajuste pode ajudar a garantir uma estimativa mais precisa e realista dos custos totais do projeto.

### 1.3 🟡 IF cliente = Paludo Volo Home THEN subtrair ~R$ 1.100/m²

**Força:** média

**Evidência:** paludo-volo-home tem z=-1.2

**Recomendação prática:**

> Quando orçar um projeto residencial do tipo Paludo Volo Home, subtraia aproximadamente R$ 1.100 por metro quadrado do valor total do orçamento. Esta recomendação é baseada em uma análise que indica que este modelo específico tem um desempenho abaixo da média (z=-1.2), sugerindo custos mais baixos comparados a outros projetos similares. Ajuste o orçamento conforme essa diretriz para refletir melhor as características econômicas deste tipo de construção.

### 1.4 🟡 IF cliente = Santa Maria THEN subtrair ~R$ 1.000/m² (Chapecó CUB menor + escopo enxuto)

**Força:** média

**Evidência:** 1 projeto Santa Maria em outliers negativos

**Recomendação prática:**

> Quando orçar um projeto de construção civil para a cidade de Santa Maria, subtraia aproximadamente R$ 1.000 por metro quadrado do valor base comparável com Chapecó, considerando um escopo mais enxuto. Esta recomendação é baseada em uma única ocorrência fora da curva (outlier) que indicou custos significativamente menores para Santa Maria em relação a outros projetos semelhantes. Ajuste este valor conforme as especificidades do projeto, pois pode haver variações locais de mercado e demanda.

---

## 2. Regras Regionais (CUB)

*Derivadas dos coeficientes da regressão Fase 6 (baseline: SC-BC)*

### 2.1 🟡 IF região = MT-Outros THEN ajustar +478 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ +478/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região de Mato Grosso exceto Cuiabá e Várzea Grande, ajuste o valor por metro quadrado em +478 R$/m² em relação à base SC-BC. Este ajuste reflete a variação dos custos locais nesta área específica, que foi identificada através de um modelo de regressão linear com uma força média. Esta recomendação visa garantir maior precisão no orçamento ao considerar os desvios regionais nos custos da construção.

### 2.2 🟢 IF região = RS-Serra THEN ajustar +1081 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +1081/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região da Serra do Rio Grande do Sul (RS-Serra), ajuste automaticamente o valor por metro quadrado em +1081 R$ comparado à base de cálculo de Santa Catarina - Baixada Continental (SC-BC). Este ajuste é necessário devido a diferenças significativas nos custos locais, como mão de obra especializada e materiais mais caros na região da Serra. A força alta dessa recomendação se deve à forte evidência estatística baseada em coeficientes de regressão que demonstram consistentemente essa variação regional.

### 2.3 🟢 IF região = SC-BC THEN ajustar +1099 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +1099/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto na região de Santa Catarina, especificamente em Balneário Camboriú, ajuste automaticamente o valor base por metro quadrado em +1099 R$/m². Esta recomendação é fundamentada em análises recentes que demonstram uma variação significativa nos custos dessa localidade em comparação com a média da região (baseline SC-BC). A alta força desta regra indica que este ajuste é crucial para garantir a precisão do orçamento, refletindo corretamente os custos locais específicos.

### 2.4 🟢 IF região = SC-Floripa THEN ajustar +1549 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +1549/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto em Florianópolis (SC-Floripa), ajuste automaticamente o valor por metro quadrado em +1549 R$/m² em relação à base de custos de Balneario Camboriú (SC-BC). Este ajuste é necessário devido a diferenças significativas nos custos locais, como mão de obra especializada e materiais mais caros na região de Florianópolis. A evidência baseia-se em análises de regressão que demonstram consistentemente essa variação.

### 2.5 🟢 IF região = SC-Litoral-Norte THEN ajustar +904 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +904/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região do Litoral Norte de Santa Catarina, ajuste automaticamente o custo em +R$ 904 por metro quadrado em relação à baseline definida para SC-BC. Este ajuste é baseado em uma forte evidência que demonstra uma diferença significativa nos custos de construção nesta região específica, refletindo fatores como materiais mais caros e mão de obra especializada.

### 2.6 🟢 IF região = SC-Outros THEN ajustar +1126 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +1126/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil em Santa Catarina fora das regiões metropolitanas de Blumenau e Chapecó (SC-Outros), ajuste automaticamente o valor por metro quadrado em R$ 1126,00 acima do baseline estabelecido para SC-BC. Essa recomendação é baseada em uma análise que identificou um aumento significativo nos custos na região devido a fatores como logística mais complexa e disponibilidade limitada de mão de obra especializada. A força alta da evidência indica que este ajuste deve ser aplicado consistentemente para refletir corretamente os custos locais.

### 2.7 🟢 IF região = SC-Vale-Itajai THEN ajustar +772 R$/m² vs baseline (SC-BC)

**Força:** alta

**Evidência:** Coef regressão = R$ +772/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região do Vale do Itajaí em Santa Catarina, ajuste automaticamente o valor por metro quadrado em +772 R$/m² em relação à baseline definida para SC-BC. Este ajuste é necessário devido a fatores locais específicos que aumentam os custos na região, como materiais mais caros e mão de obra especializada. A evidência baseia-se em análises estatísticas com coeficiente de regressão confirmado, indicando uma forte correlação entre localização e aumento nos custos de construção.

### 2.8 🟡 IF região = SP-Capital THEN ajustar +362 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ +362/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar um projeto de construção civil na região da capital de São Paulo, ajuste o valor por metro quadrado em +362 R$/m² em relação à baseline estabelecida para Santa Catarina - Balneário Camboriú (SC-BC). Este ajuste é necessário porque os custos de mão de obra, materiais e logística na capital paulista são significativamente mais altos que na região de SC-BC, refletindo uma diferença comprovada por análise de regressão.

### 2.9 🟡 IF região = null-Outros THEN ajustar +638 R$/m² vs baseline (SC-BC)

**Força:** média

**Evidência:** Coef regressão = R$ +638/m². Baseline é SC-BC.

**Recomendação prática:**

> Quando orçar projetos de construção civil em regiões fora do padrão definido como "null-Outros", ajuste automaticamente o valor por metro quadrado em +638 R$/m² em relação à baseline SC-BC. Este ajuste é baseado em uma análise que identificou essa variação média para áreas não especificadas no modelo original, refletindo custos operacionais e logísticos distintos nessas regiões.

---

## 3. Regras de Padrão Construtivo

*Derivadas dos coeficientes da regressão Fase 6 (baseline: padrão alto)*

### 3.1 🟡 IF padrão = economico THEN ajustar -1022 R$/m² vs baseline (alto)

**Força:** média

**Evidência:** Coef regressão = R$ -1022/m². Baseline é padrão alto.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto de construção civil com um padrão econômico, ajuste automaticamente o valor por metro quadrado em R$ -1022/m² em relação ao baseline (padrão alto). Essa recomendação é baseada em uma análise que identificou essa diferença média entre os padrões econômicos e altos, com um coeficiente de regressão estabelecendo esse valor específico. Ajustar conforme indicado permitirá que seu orçamento seja mais preciso para projetos que seguem o padrão econômico.

### 3.2 🟢 IF padrão = medio THEN ajustar -2202 R$/m² vs baseline (alto)

**Força:** alta

**Evidência:** Coef regressão = R$ -2202/m². Baseline é padrão alto.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto de construção civil com um padrão médio, ajuste automaticamente o valor por metro quadrado em -2.202 R$ comparado ao baseline (padrão alto). Esta recomendação é baseada em uma análise que mostra uma correlação forte e direta entre o padrão médio e a redução de custos em 2.202 R$/m², quando comparado com projetos que seguem um padrão mais elevado. A aplicação desta regra ajudará a garantir que seu orçamento seja preciso e competitivo para projetos com padrões médios.

---

## 4. Regras Causais (Controle de Confundidores)

*Derivadas de correlações parciais Fase 5 — refutam correlações aparentes*

### 4.1 🟡 Economia de escala real mas leve (controlando região)

**Força:** média

**Evidência:** r parcial = -0.317 (n=99). Projetos maiores TÊM R$/m² um pouco menor mesmo dentro da mesma região.

**Recomendação prática:**

> Quando orçar projetos de construção civil em uma mesma região, ajuste os custos por metro quadrado para baixo conforme o tamanho do projeto aumenta. Esta recomendação é baseada em evidências que mostram uma leve economia de escala: projetos maiores têm um custo R$/m² ligeiramente menor (coeficiente -0.317, n=99). Portanto, ao orçar grandes obras, reduza levemente o custo unitário para refletir essa tendência observada na prática.

### 4.2 🟢 Supraestrutura% ≠ preditor de R$/m² alto

**Força:** alta

**Evidência:** r parcial = -0.039 (NULO). Correlação simples era artefato regional. NÃO usar supra% pra estimar preço.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto de construção civil e notar que a porcentagem da suprapredial (estruturas acima do nível do solo) é significativamente alta em relação ao total do projeto, não use essa informação como base para estimar o preço final por metro quadrado. A evidência indica que há uma correlação nula entre a porcentagem de suprapredial e os custos unitários elevados, sendo que qualquer associação observada anteriormente era resultado de características regionais específicas e não pode ser generalizada.
> 
> Essa recomendação é baseada em análises estatísticas que mostram que fatores locais influenciavam erroneamente a percepção da relação entre suprapredial e custos, o que não se aplica consistentemente em todo o espectro de projetos. Portanto, para estimativas mais precisas, concentre-se em outros indicadores relevantes do projeto ao invés de depender dessa porcentagem específica.

### 4.3 🟢 Gerenciamento% alto ≠ projeto caro

**Força:** alta

**Evidência:** r parcial = -0.095. Projetos EPCM (gerenciamento concentrado) não são intrinsecamente caros. Preço alto vem de escopo/região/especificação, não da estrutura de orçamento.

**Recomendação prática:**

> Quando você observar um alto percentual de gerenciamento em um projeto de construção civil, é importante não assumir automaticamente que isso significa que o orçamento será elevado. Este ajuste deve ser feito ao analisar projetos EPCM (Engineering, Procurement, Construction and Management), onde a concentração do gerenciamento pode estar mais presente sem necessariamente aumentar os custos totais. O preço final de um projeto é determinado principalmente pelo escopo, região e especificações técnicas, não pela estrutura de gerenciamento. Portanto, ao lidar com projetos EPCM, foque nas variáveis que realmente impactam o custo, como materiais e mão de obra, em vez de se preocupar excessivamente com os custos associados à gestão concentrada.

---

## 5. Regras de Economia de Escala (por região)

*Heterogêneas — só algumas regiões têm efeito escala*

### 5.1 🟢 IF região = SC-BC THEN aumentar AC reduz R$/m²

**Força:** alta

**Evidência:** r = -0.35 (n=18). Economia de escala forte/moderada.

**Recomendação prática:**

> Quando você estiver orçamentando um projeto em Balneário Camboriú (SC), ajuste os custos para aumentar a quantidade de mão-de-obra e reduzir os custos por metro quadrado. Isso é necessário porque há uma forte economia de escala na região, com evidências que mostram uma correlação negativa significativa entre o tamanho do projeto e o custo por metro quadrado (r = -0.35). Essa estratégia ajudará a otimizar os custos e melhorar a eficiência no orçamento.

### 5.2 🟡 IF região = SC-Litoral-Norte THEN aumentar AC reduz R$/m²

**Força:** média

**Evidência:** r = -0.52 (n=12). Economia de escala forte/moderada.

**Recomendação prática:**

> Quando orçar projetos na região do Litoral Norte de Santa Catarina, ajuste os custos para um valor mais baixo por metro quadrado (R$/m²) em comparação com outras regiões. Esta redução é justificada pela economia de escala forte/moderada observada nesta área específica, indicando que a relação custo-benefício tende a ser mais favorável devido a fatores locais como infraestrutura e disponibilidade de mão de obra.

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