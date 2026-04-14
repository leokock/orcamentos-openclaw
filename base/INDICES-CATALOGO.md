# Catálogo de Índices Cartesian — Guia de Leitura

_Gerado em 2026-04-14T13:18:36 via `scripts/gerar_catalogo_indices.py`_

**Planilha:** [INDICES-CATALOGO.xlsx](INDICES-CATALOGO.xlsx) — 677 KB, 10 abas, ~6.500 linhas de dados

---

## Bem-vindo

Se você é engenheiro civil e está abrindo essa planilha pela primeira vez, este documento é seu mapa. Ele explica **o que é cada coisa, como ler os números, e como usar o catálogo no dia-a-dia** de um orçamentista. Leia do começo ao fim da primeira vez — leva 10 minutos e te economiza horas depois.

A planilha é longa (quase 6.500 linhas de dados), mas é **toda filtável e ordenável**. Você não precisa "ler" ela linha por linha. Você **pergunta** (ex: "quanto custa o PU médio de porcelanato?") e **filtra** até achar a resposta.

---

## Por que esse catálogo existe

A Cartesian já fez mais de **126 orçamentos executivos** ao longo dos últimos anos. Cada um deles tem centenas de itens com quantidades, unidades, preços unitários, memoriais, premissas. Isso é um tesouro de informação, mas até agora estava **espalhado** em arquivos separados: cada projeto um .xlsx, cada calibração um .json, cada análise qualitativa um .md. Impossível de consultar rápido.

Nos últimos meses consolidamos tudo isso numa **base paramétrica V2** com vários tipos de índice derivados dos 126 projetos reais. Este catálogo é o **mapa único** dessa base — tudo o que a gente sabe sobre custo de construção consolidado num xlsx filtrável.

**Pra que serve na prática:**
- Estimar custo de um projeto novo sem precisar fazer orçamento detalhado
- Validar um orçamento contra o histórico (é razoável? tá fora da curva?)
- Justificar decisões técnicas pro cliente com dados ("nossa base de 23 projetos similares mostra que...")
- Identificar qual insumo tá caro/barato na sua proposta
- Comparar padrões (médio vs alto vs luxo) por macrogrupo
- Entender qual obra da base mais se parece com a que você está orçando

---

## Os 3 tipos de índice que você vai encontrar

Antes de entrar nas abas, saiba que temos **3 famílias diferentes** de índice, e elas respondem perguntas diferentes:

### 1. Índices de preço unitário (R$/unidade)

**"Quanto custa 1 m³ de concreto? 1 kg de aço? 1 m² de porcelanato?"**

Esses são os PUs (preços unitários) tradicionais. Em moeda por unidade física. Eles estão nas abas **PUS_CROSS_V1** (1.740 clusters com lista de obras-fonte) e **PUS_CROSS_V2** (4.210 clusters, mais cobertura mas sem lista). São bons pra compor um orçamento bottom-up — multiplicar quantidade × PU.

Exemplo: "Concreto usinado FCK 30 MPa bombeável, base da Cartesian mostra mediana de R$ 590/m³ (n=25 projetos)."

### 2. Índices de custo por área (R$/m² AC)

**"Quanto um m² de alvenaria custa no orçamento total? E um m² de pintura? E esquadrias?"**

Esses são os índices por **macrogrupo** expressos em R$/m² de AC (área construída). Úteis pra top-down — você multiplica R$/m² × AC do projeto e tem o custo do macrogrupo direto, sem precisar compor item a item. Estão nas abas **CALIBRACAO_GLOBAL** (média dos 126 sem distinção de padrão) e **CALIBRACAO_CONDICIONAL** (segregada por padrão Gemma: econômico, médio, médio-alto, alto, luxo).

Exemplo: "Esquadrias padrão alto, mediana R$ 395/m² AC (n=23 projetos classificados como 'alto')."

### 3. Índices de consumo físico (quantidade/m² AC)

**"Quantos m³ de concreto por m² de AC? Quantos kg de aço por m³ de concreto?"**

Esses são os índices **estruturais** que traduzem geometria em material. Ajudam a dimensionar rapidamente o **quantitativo** antes de ter projeto executivo. Estão na aba **INDICES_ESTRUTURAIS**.

Exemplo: "Concreto mediano 0,34 m³ por m² de AC (n=52 projetos). Se seu AC é 13.000 m², espere ~4.400 m³ de concreto estrutural."

**Regra prática:** num paramétrico novo você usa **consumo físico × AC × PU** pra bottom-up, ou **R$/m² × AC** pra top-down. As duas abordagens devem chegar em números próximos — se divergirem muito, é sinal de que algum índice tá fora da curva e vale investigar.

---

## Entendendo as colunas estatísticas (pense como quem lê um curva de distribuição)

Quase toda aba tem essas colunas:

| Coluna | O que significa | Como interpretar |
|---|---|---|
| **`n`** | Quantos projetos contribuíram pro índice | `n ≥ 10` é robusto, `n=5-9` razoável, `n<5` frágil (use com cuidado) |
| **`min` / `max`** | O menor e o maior valor observado | Dão a ideia do extremo — mas podem ser outliers. Não use pra calibração direta. |
| **`p10` / `p90`** | Valores de corte: 10% dos projetos ficam abaixo do p10 e 10% acima do p90 | A **faixa P10-P90 contém 80% dos projetos** — é o intervalo "normal" |
| **`p25` / `p75`** | Idem, mas 50% dos projetos ficam entre eles (faixa inter-quartil) | Intervalo **mais estreito, mais típico** — 50% dos projetos se encaixam aqui |
| **`mediana` (`p50`)** | O valor do meio — 50% dos projetos abaixo, 50% acima | **É o valor que a calibração V2 usa como "típico".** Mais robusto que a média |
| **`media`** | Média aritmética (soma / n) | Pode ser puxada por outliers (1 projeto com PU absurdo distorce). **Prefira mediana.** |
| **`cv`** | Coeficiente de variação = desvio-padrão / média | Grau de dispersão: `cv<0.3` = **confiável** (projetos parecidos). `0.3-0.5` = **variável** (depende do padrão/cidade). `>0.5` = **volátil** (investigar por quê) |
| **`projetos_fonte`** | _(só em PUS_CROSS_V1)_ | Lista de slugs das obras que contribuíram — permite rastrear "quem bancou esse número" |

### Leitura prática de uma linha

Exemplo real: **concreto usinado FCK 30**, na aba INDICES_DERIVADOS_V2:

```
n=25  min=420  p10=490  p25=560  mediana=590  media=605  p75=650  p90=710  max=820  cv=0.14
```

Como ler isso?
- **25 projetos** bancam esse índice — dados robustos ✅
- A **mediana é R$ 590/m³** — é o valor típico, use esse como default
- **80% dos projetos** ficam entre **R$ 490 e R$ 710/m³** (p10-p90) — essa é sua faixa razoável
- **50% dos projetos** ficam entre **R$ 560 e R$ 650** (p25-p75) — faixa mais apertada, sem extremos
- **CV = 0,14** → baixíssima dispersão, todos os projetos têm preço parecido → **confiança alta** nesse índice
- Se seu orçamento tem concreto a R$ 900, você está acima do max (**R$ 820**) — investiga. Pode ser erro, localização remota, fornecedor único.
- Se seu orçamento tem concreto a R$ 400, abaixo do min (**R$ 420**) — também investiga.

### Regra rápida de "confio ou não?"

| n | cv | Confiança |
|---|---|---|
| ≥ 10 | < 0.3 | 🟢 **Alta** — use direto |
| 5-9 | < 0.4 | 🟡 **Média** — use mas valide contra o contexto |
| < 5 | qualquer | 🔴 **Baixa** — use só como ponto de partida, não pra calibração final |
| qualquer | > 0.5 | 🔴 **Baixa** — a dispersão indica que o "típico" não se aplica. Precisa investigar o por quê (padrão? cidade? método construtivo?) |

---

## Visão guiada aba por aba

### 📋 Aba 1 — **LEIA_ME** (dentro do xlsx)

Versão resumida deste guia dentro da própria planilha. Serve pra você se orientar sem precisar sair do Excel. Contém o mapa das 10 abas, schema das colunas, exemplos de filtros, gaps conhecidos.

### 🏗 Aba 2 — **PROJETOS** (126 linhas)

**É o seu ponto de partida.** Lista completa dos 126 projetos executivos da base, com metadados principais.

Colunas: `slug | padrao_gemma | confianca | ac_m2 | ur | total_rs | rsm2 | m2_por_ur | rs_por_ur | cidade | fonte`

**Quando usar:**
- **"Quais obras são similares à minha?"** → filtre por `padrao_gemma` igual ao seu, `ac_m2` dentro de ±25%, `ur` próximo. Os que sobrarem são sua referência.
- **"Qual o R$/m² típico de alto padrão?"** → filtre `padrao_gemma = alto` → ordene `rsm2` → olhe a faixa.
- **"Meu projeto tem custo/UR razoável?"** → compare o valor do seu projeto com a coluna `rs_por_ur` dos similares.
- **Cross-reference:** quando uma outra aba citar um slug (ex: `adore-cacupe`), volte aqui pra ver quem é esse projeto, onde fica, qual o porte.

**Importante:** a coluna `padrao_gemma` não é um rótulo dado pelo orçamentista original — é uma **classificação feita automaticamente pelo Gemma (LLM)** analisando os itens de acabamento (porcelanato, mármore, ACM, elevador panorâmico, etc.) de cada projeto. 94% dos projetos têm confiança alta/média.

### 🧱 Aba 3 — **CALIBRACAO_GLOBAL** (18 linhas)

**Os 18 macrogrupos da Cartesian em R$/m² AC, agregados de todos os 126 projetos sem distinção de padrão.**

Colunas: `macrogrupo | n | min | p10 | p25 | mediana | media | p75 | p90 | max | unidade | fonte`

**Quando usar:**
- **Primeiro rascunho de um paramétrico:** pegue a mediana de cada macrogrupo × seu AC e some — você tem uma estimativa grosseira do custo total em 2 minutos.
- **Sanity check:** abriu um orçamento executivo novo e quer ver se o R$/m² de Esquadrias (por exemplo) está dentro do esperado? Essa aba te dá a faixa p10-p90 onde 80% dos projetos caem.

**Cuidado:** essa aba mistura projetos de padrão econômico com padrão alto. A dispersão é grande (cv geralmente 0.5+). **Use a aba CALIBRACAO_CONDICIONAL quando souber o padrão do seu projeto** — é mais preciso.

### 🎯 Aba 4 — **CALIBRACAO_CONDICIONAL** (64 linhas)

**A estrela da base V2.** Mesmos 18 macrogrupos, mas agora **segregados por padrão Gemma** (econômico / médio / médio-alto / alto / luxo). É a fonte primária da calibração que a Cartesian usa pós-fase 18b.

Colunas: `padrao | macrogrupo | n | min | p10 | p25 | mediana | media | p75 | p90 | max | unidade | fonte`

**Por que é melhor que a global:** um projeto alto padrão tem Esquadrias muito mais caro que um econômico. Se você usa a mediana "global", subestima alto e superestima econômico. Aqui a mediana é **específica do padrão**, então é sempre mais aderente.

**Quando usar:**
- **Paramétrico de projeto novo:** você sabe o padrão pretendido → pega a mediana do seu padrão em cada MG × AC → soma.
- **Comparar padrões:** quanto Esquadrias custa a mais em "alto" vs "médio"? Filtre `macrogrupo=Esquadrias` → ordene por `padrao` → calcule a diferença. Isso te dá dados pra negociar com cliente.
- **Entender o "salto de padrão":** de econômico pra médio as diferenças estão em Pisos, Rev.Parede, Louças. De alto pra luxo estão em Fachada, Sistemas Especiais, Complementares. Os dados estão aí, filtre e veja.

**Pegadinha:** alguns MGs têm `n<3` em certos padrões — nesses casos o sistema de calibração cai num **fallback global** (usa o valor da CALIBRACAO_GLOBAL multiplicado por um fator de padrão). Ou seja, um MG com n=2 é **referência fraca** — o próprio sistema sabe disso e não confia direto.

**Observação importante:** a classe **luxo** tem 0 projetos na base. Isso não é bug — significa que a Cartesian nunca orçou um luxo-luxo (casa Alphaville, cobertura linear Vieira Souto) no histórico. O "alto" da base é o topo real dos empreendimentos multifamiliares residenciais que a Cartesian atende.

### 📊 Aba 5 — **INDICES_DERIVADOS_V2** (29 linhas)

**29 índices calculados combinando os dados brutos.** Inclui PUs consolidados de insumos principais (concreto, aço, porcelanato, pintura), custos de macrogrupo em R$/m², ratios técnicos (aço/concreto, fôrma/concreto) e proporções de curva ABC.

Colunas: `nome | descricao | n | min | p10 | p25 | mediana | media | p75 | p90 | max | cv | unidade | fonte`

**Quando usar:**
- **Composição rápida de custo estrutural:** `pu_concreto_usinado_mediano`, `pu_aco_ca50_mediano`, `pu_forma_madeira_mediano` — mediana dos PUs consolidados de todos os projetos.
- **Ratios pra dimensionar:** `concreto_por_aco_ratio` te dá a razão concreto:aço típica. `forma_por_concreto_ratio` idem pra fôrma.
- **Custos por macrogrupo já computados:** `custo_concreto_rsm2`, `custo_esquadrias_rsm2`, `custo_loucas_rsm2` — R$/m² já pronto pra macrogrupos específicos.
- **Indicadores de curva ABC:** `curva_abc_a_pct` mostra o % de itens que compõem 80% do custo nos projetos da base. Baixo = projeto concentrado em poucos itens; alto = projeto pulverizado.

**Dica:** ordene a aba por `n` desc e ignore tudo com `n<5`. O que sobrar é o que tem base estatística sólida.

### 🔩 Aba 6 — **INDICES_ESTRUTURAIS** (~22 linhas)

**Consumo físico + produto + instalações % + custos indiretos % + segmentos por porte.** É a aba dos engenheiros de verdade — quantidades, não preços.

Seções:
- **Estruturais:** `concreto_m3_por_m2_ac` (0,34 mediano), `aco_kg_por_m3_concreto` (~106), `aco_kg_por_m2_ac`, `forma_m2_por_m2_ac`
- **Produto:** `ac_por_ur` (quantos m² por unidade residencial), `custo_por_ur`, `cub_ratio`, `burn_rate_mensal`, `elevador_pu_un`
- **Instalações %:** hidrossanitárias, elétricas, preventivas, gás, telecom — cada uma como % do custo total do projeto
- **Custos Indiretos %:** projetos/consultorias, taxas/licenças, equipe ADM, EPCs, equipamentos, ensaios, canteiro
- **Segmento por porte:** R$/m² total separado em 4 faixas de AC (pequeno <8k, médio 8-15k, grande 15-25k, extra >25k)

**Quando usar:**
- **Dimensionar quantitativo antes do projeto executivo:** multiplica o consumo mediano × seu AC e você tem uma estimativa de material. `concreto_m3_por_m2_ac × 13.000 m²` = ~4.400 m³ de concreto.
- **Validar % de instalações:** seu projeto tem elétrica representando 10% do total, mas a base mostra mediana 6%? Investigue — pode ter projeto muito complexo (garage full automatizada, automação geral) ou pode ser erro de BDI.
- **Validar % de CI:** se Gerenciamento tá acima da faixa P75, provavelmente tem equipe superdimensionada ou prazo esticado.
- **Segmentação por porte:** escolha o segmento do seu projeto (AC <8k → pequeno, etc) e veja a faixa de R$/m² que projetos daquele porte apresentaram.

### 💰 Aba 7 — **PUS_CROSS_V1** (1740 linhas) ⭐ TESOURO DA BASE

**A aba mais preciosa pra quem quer rastrear "quem bancou esse número".** 1.740 clusters de PU cross-projeto, **com lista de obras-fonte em cada linha**.

Colunas: `categoria | chave | descricao | unidade | n_proj | n_obs | min | p25 | mediana | p75 | max | cv | projetos_fonte`

**O que é um "cluster":** itens semanticamente iguais de projetos diferentes agrupados. Ex: "Concreto usinado FCK 30 bombeado" pode aparecer em 30 projetos com pequenas variações de descrição — um cluster consolida todos esses num único registro com mediana robusta.

**Quando usar:**
- **"Quais obras sustentam esse PU mediano?"** → filtre a descrição, olhe a coluna `projetos_fonte`. Se são 3 obras só da mesma construtora, pode ser viés. Se são 15 obras de 5 construtoras diferentes, é uma mediana forte.
- **Auditar um PU específico do seu orçamento:** seu concreto tá a R$ 750. Nessa aba, concreto FCK 30 tem mediana R$ 590, p90 R$ 710. Você está acima do p90 — justifique (obra remota? usina única?).
- **Validar insumos caros:** ordene por `mediana` desc, veja os clusters mais caros da base. Se seu projeto tem um desses, precisa ter atenção especial pra não estourar.

**Dicas de filtro:**
- `n_proj ≥ 5` + `cv < 0.3` = PUs robustos
- Busca por palavra-chave na `chave` ou `descricao` (ex: "porcelanato", "bloco", "vidro")
- Ordene por `categoria` pra navegar macrogrupo por macrogrupo

### 📚 Aba 8 — **PUS_CROSS_V2** (4210 linhas) — mais cobertura, sem fontes

Versão nova (fase 10 v2) do cluster de PUs, com **2.4x mais clusters** (4.210 vs 1.740). A diferença: usa **hash-based clustering semântico** que consegue agrupar itens com descrições mais diversas.

Colunas: `cluster_id | key (tokens) | descricao | unidades | n_proj | n_obs | pu_min | pu_p10 | pu_p25 | pu_mediana | pu_p75 | pu_p90 | pu_max | pu_media | cv`

**Limitação:** o algoritmo V2 não preservou a **lista de projetos** fonte em cada cluster. Então você tem a quantidade (n_proj) mas não sabe **quais** obras bancam o número.

**Quando usar:**
- **Cobertura ampla:** quando a V1 não tem o item que você procura, provavelmente a V2 tem (quase 3x mais itens).
- **Comparação rápida de PUs:** ordene por `n_proj` desc pra ver os itens mais presentes na base.
- **`key`** mostra os tokens semânticos usados pro clustering (ex: `porcelanato|60x60|retificado`) — útil pra filtrar por palavra-chave.

**Regra prática:** use V1 quando precisar justificar/rastrear, V2 quando só quer um número de referência.

### 🅰 Aba 9 — **CURVA_ABC_MASTER** (126 linhas)

**1 linha por projeto da base.** Mostra quantos itens tem, quantos desses itens compõem a curva A (80% do custo), e o valor total.

Colunas: `slug | status | n_itens | n_a | pct_a | valor_total_rs`

**Pra que serve:**
- **Identificar projetos "concentrados" vs "pulverizados":** ordene por `pct_a` asc. Projetos com pct_a ≈ 5% são altamente concentrados (poucos itens dominam); pct_a ≈ 25% são pulverizados (muitos itens pequenos).
- **Achar projetos de referência por porte total:** filtre `valor_total_rs` próximo ao do seu projeto novo.
- **Validar sanidade do seu orçamento:** se seu projeto tem 2.000 itens e a curva A pega 400 (20%), compare com a base — projetos Cartesian costumam ter curva A na faixa 5-15% do total.

### 🧠 Aba 10 — **CROSS_INSIGHTS_GEMMA** (varia)

**Análises qualitativas cross-projeto feitas pelo Gemma (LLM local).** Leu todos os 126 projetos e destilou observações gerais da base.

Colunas: `secao | tipo | campo | conteudo`

Seções:
- **`familias`** — agrupamento de projetos por tipologia/característica
- **`indices_sugeridos`** — índices que o Gemma sugeriu criar a partir dos padrões que identificou
- **`lacunas`** — coisas que faltam na base (tipologias não cobertas, regiões, padrões)
- **`outliers`** — projetos que destoam do resto (pra cima ou pra baixo)
- **`padroes_comuns`** — padrões recorrentes que o Gemma identificou

**Quando usar:** menos pra cálculo, mais pra **entender a base qualitativamente**. Útil antes de tomar uma decisão estratégica ("tem projeto similar na base ou estamos no escuro?").

---

## Cenários reais de uso no dia-a-dia

### Cenário 1: "Preciso estimar um novo projeto de 13.000 m² alto padrão"

1. Abrir **PROJETOS** → filtrar `padrao_gemma = alto` + `ac_m2 entre 10.000 e 16.000` → anotar os ~5 slugs mais próximos
2. Abrir **CALIBRACAO_CONDICIONAL** → filtrar `padrao = alto` → pegar mediana de cada MG → multiplicar por 13.000 → somar → tem o **custo top-down**
3. Abrir **INDICES_ESTRUTURAIS** → seção "Segmento por porte" → linha `medio_8k_15k_rsm2` → ver se sua soma tá dentro da faixa p25-p75 daquele porte
4. Se tudo bate, seu paramétrico está em linha com a base. Se não bate, descobrir por qual MG especificamente divergiu.

### Cenário 2: "O orçamentista me mandou um PU de concreto R$ 780. Isso tá ok?"

1. Abrir **PUS_CROSS_V2** → filtrar `key` contém "concreto" + "usinado" → ver faixa `pu_p10` a `pu_p90`
2. Se o concreto mediano da base é R$ 590 e p90 é R$ 710, seu orçamentista está **acima do p90** → tem que justificar (localização remota? concreto especial? preço hoje diferente da data-base da média?)
3. Volte pra **PUS_CROSS_V1** → procure o mesmo cluster → coluna `projetos_fonte` → olhe quais obras bancam essa mediana → avalie se são obras em contexto similar ao seu

### Cenário 3: "Quanto vou cobrar a mais pra passar de médio-alto pra alto no mesmo projeto?"

1. Abrir **CALIBRACAO_CONDICIONAL** → filtrar `macrogrupo in (Pisos, Rev. Interno Parede, Esquadrias, Louças e Metais, Fachada)` (os 5 mais sensíveis ao padrão) → colunas `mediana`
2. Para cada MG: subtrair `mediana medio-alto` de `mediana alto`
3. Somar as diferenças × AC do projeto → tem a **ordem de grandeza do "salto de padrão"**
4. Use pra negociar com o cliente: "esse upgrade custa +R$ X/m², distribuído nesses 5 macrogrupos"

### Cenário 4: "Meu projeto tem Sistemas Especiais puxando o custo. Isso é comum?"

1. Abrir **CALIBRACAO_CONDICIONAL** → filtrar `padrao = alto` + `macrogrupo = Sistemas Especiais` → olhar mediana e p90
2. Abrir **PROJETOS** → identificar 2-3 projetos da base que são de alto padrão próximo ao seu
3. Abrir **CROSS_INSIGHTS_GEMMA** → procurar na seção `padroes_comuns` se tem observação sobre Sistemas Especiais em projetos alto padrão (ex: "piscina aquecida é comum em 60% dos alto padrão")
4. Cross-checar: se seu projeto tem piscina aquecida + sauna + spa + gerador dedicado, está dentro do padrão alto. Se tem automação total + heliponto + elevador panorâmico, está extrapolando pra luxo.

### Cenário 5: "Tô orçando e preciso validar o consumo físico de concreto"

1. Abrir **INDICES_ESTRUTURAIS** → seção "Estruturais" → linha `concreto_m3_por_m2_ac`
2. Mediana 0,34 m³/m² → multiplicar por seu AC → quantitativo esperado
3. Se seu projeto tem laje protendida, o número deve ser **menor** que a mediana (protendida usa ~0,22 m³/m²)
4. Se tem laje convencional pesada com pé-direito alto, **maior** (até 0,45)
5. Se seu quantitativo está fora da faixa p10-p90 (0,21-0,57), revisar modelagem estrutural

### Cenário 6: "Preciso saber se BDI da minha proposta tá agressivo ou não"

1. Abrir **INDICES_ESTRUTURAIS** → seção "Custos Indiretos %" → linhas `projetos_consultorias_pct_total`, `taxas_licencas_pct_total`, `equipe_adm_pct_total`, `canteiro_pct_total`
2. Somar as medianas → tem o **CI típico como % do total** nos projetos da base
3. Comparar com o CI da sua proposta → se estiver 20% abaixo da mediana, você está **agressivo** (pode dar prejuízo); 20% acima, **folgado** (pode perder o contrato)

---

## Gaps e pegadinhas

### 1. PUS_CROSS_V2 não tem lista de projetos

A versão 2 do clustering (4.210 clusters) ganhou cobertura mas perdeu rastreabilidade. Quando você quiser **auditar** um PU específico ou citar "fontes" pro cliente, use **PUS_CROSS_V1** (1.740 clusters com lista completa de obras). Quando quiser **cobertura ampla** (procurar um item raro), use V2.

### 2. Classe "luxo" tem 0 projetos

A base Cartesian não tem casos de luxo-luxo (cobertura linear, casa Alphaville premium). O "alto" é o topo real. Se você está orçando um projeto que claramente é luxo absoluto, use o "alto" como referência inferior e aplique um multiplicador — não confie no "luxo" da aba CALIBRACAO_CONDICIONAL porque ela tá vazia.

### 3. `custo_por_ur` tem n=2

Esse índice específico (R$ por unidade residencial) só tem 2 projetos com dado válido — confiança estatística **péssima**. Se precisar do custo/UR, melhor calcular direto da aba PROJETOS filtrando por similares e tirando a média dos 5 mais próximos.

### 4. Alguns MGs em CALIBRACAO_CONDICIONAL têm n baixo

Classes econômico e luxo têm poucos projetos — alguns macrogrupos específicos dentro delas podem ter `n<3`. Nesses casos o sistema de calibração cai num **fallback global × multiplicador de padrão**. Na prática: se você está orçando econômico e viu uma mediana estranha, confira a coluna `n` — se for baixo, desconfie.

### 5. CV alto num índice = não confiável

`cv > 0.5` significa que a dispersão é tão grande que o "valor típico" não tem muito significado. Isso acontece em macrogrupos muito dependentes do padrão (Louças, Fachada, Sistemas Especiais). A solução é usar a **CALIBRACAO_CONDICIONAL** em vez da global — ao segregar por padrão, o CV dentro de cada bucket cai drasticamente.

### 6. Os 126 projetos da base são TODOS da Cartesian

Essa base representa o universo de projetos que a Cartesian já orçou. Ela é **fortemente viesada para multifamiliar residencial alto-padrão em SC** (Itajaí, Balneário Camboriú, Florianópolis, Navegantes). Se você estiver orçando um galpão industrial, um hospital, ou um residencial em Pernambuco, os índices aqui são **ponto de partida**, não verdade absoluta.

---

## Glossário rápido

| Termo | O que é |
|---|---|
| **AC** | Área Construída (m²) — denominador padrão de todos os índices R$/m² |
| **UR** | Unidades Residenciais — apartamentos/casas no empreendimento |
| **Macrogrupo (MG)** | Uma das 18 categorias canônicas Cartesian (Gerenciamento, Mov.Terra, Infra, Supra, Alvenaria, etc) |
| **R$/m² AC** | Custo em reais dividido pela área construída total do projeto |
| **Paramétrico** | Orçamento rápido baseado em índices (top-down), sem BoQ detalhado |
| **Preliminar** | Versão mais detalhada do paramétrico, com itens de referência (pós-fase 18b da Cartesian) |
| **Executivo** | Orçamento completo item a item com quantitativos do projeto executivo — **NÃO é o que a base aqui tem** |
| **PU** | Preço Unitário (R$ por unidade física: m², m³, kg, un) |
| **CUB** | Custo Unitário Básico — índice mensal do Sinduscon usado pra normalizar data-base |
| **CUB Ratio** | Relação entre o R$/m² do projeto e o CUB da data-base (>1 = projeto mais caro que CUB) |
| **Bottom-up** | Compor custo item a item (Qtd × PU = Total) — o que a aba de detalhe do paramétrico faz |
| **Top-down** | Estimar custo agregado a partir de índices R$/m² × AC — o que CALIBRACAO_CONDICIONAL permite |
| **Mediana (p50)** | Valor central — 50% dos projetos abaixo, 50% acima. Mais robusta que média contra outliers |
| **Percentis p10/p25/p75/p90** | Cortes da distribuição. P10-P90 contém 80% dos projetos; P25-P75 contém 50% |
| **CV** | Coeficiente de Variação = desvio-padrão / média. Mede dispersão normalizada |
| **Curva ABC** | Ordenação de itens pelo valor acumulado. Itens "A" somam 80% do custo total |
| **Padrão Gemma** | Classificação (econômico/médio/médio-alto/alto/luxo) feita automaticamente pelo LLM Gemma analisando itens de acabamento |
| **Fase XX** | Marcos do desenvolvimento da base V2 (ver `base/FASES-FUTURAS.md` pra timeline completa) |

---

## Como regenerar este catálogo

Quando você atualizar a base (novo projeto processado, nova calibração, novos dados Gemma), rode:

```bash
cd ~/orcamentos-openclaw
python scripts/gerar_catalogo_indices.py
```

O script lê dinamicamente todos os JSONs da base e regenera **o xlsx + este md**. Rode sem argumentos.

## JSONs fonte (pra quem quer abrir o dado bruto)

- `base/calibration-indices.json` — 18 MGs global + estruturais + instalações + CI + produto + segmentos
- `base/calibration-condicional-padrao.json` — 18 MGs × 5 padrões Gemma (fase 18b, **fonte primária da calibração atual**)
- `base/base-indices-master-2026-04-13.json` — consolidado 322 KB (29 derivados + curva ABC + cross insights)
- `base/itens-pus-agregados.json` — 4.210 clusters PU V2 (fase 10 v2)
- `base/base-pus-cartesian.json` — 1.740 clusters PU V1 **com lista de projetos**
- `base/padroes-classificados-consolidado.json` — labels Gemma fase 18 (125/126 projetos classificados)
- `base/indices-executivo/*.json` — 126 arquivos individuais por projeto

## Onde encontrar mais contexto

- **[FASES-FUTURAS.md](FASES-FUTURAS.md)** — linha do tempo completa das fases de desenvolvimento da base V2 (1-19)
- **[SESSAO-2026-04-14-REVISAO-3-PACOTES.md](SESSAO-2026-04-14-REVISAO-3-PACOTES.md)** — narrativa da sessão que fechou o modelo V2 + 18b + 19
- **[PARAMETRICO-V2-HIBRIDO.md](PARAMETRICO-V2-HIBRIDO.md)** — como o gerador paramétrico usa esses índices na prática
- **[CAMADA-QUALITATIVA-GEMMA.md](CAMADA-QUALITATIVA-GEMMA.md)** — detalhes de como a camada qualitativa Gemma foi construída
