# Cross-Project Insights — Phase 5
_Gerado em 2026-04-13T18:39:25_

Análise de **126 projetos** da base Cartesian via Gemma local.
5 perguntas independentes, ~576s total.

## Famílias de projetos por similaridade

### 1.
- **nome_familia:** Mega Loteamentos e Infraestrutura de Grande Escala
- **criterios:** Projetos com a maior área construída (AC > 13000m²) e foco primário em Infraestrutura Básica, Terraplenagem, Pavimentação e serviços de loteamento.
- **projetos_exemplares:** estilo-condominios-estilo-condominios, wf-aquarius, pass-e-connect
- **ac_range:** 13000-24000 m²
- **n_estimado_total:** 3

### 2.
- **nome_familia:** Complexos Residenciais de Alto Padrão (Grandes Lotes)
- **criterios:** Projetos de grande porte (AC > 7000m²) com foco em Estrutura, Acabamentos de alto nível, Lazer e Equipamentos, característicos de condomínios fechados de luxo.
- **projetos_exemplares:** fonseca-empreendimentos-estoril, cln-porto-ruby, chiquetti-e-dalvesco-cielo
- **ac_range:** 7000-15000 m²
- **n_estimado_total:** 3

### 3.
- **nome_familia:** Projetos de Uso Misto e Ambientação (Resorts/Reserva)
- **criterios:** Projetos de médio a grande porte (AC 500-7500m²) onde o foco principal é a Ambientação, Mobiliário e Áreas de Lazer, com menor ênfase em infraestrutura bruta.
- **projetos_exemplares:** rosner-reserva-sao-vicente, cn-brava-ocean
- **ac_range:** 500-7500 m²
- **n_estimado_total:** 2

### 4.
- **nome_familia:** Edificações de Médio Porte e Detalhamento de Sistemas
- **criterios:** Projetos de médio porte (AC 350-5000m²) com alta complexidade em Instalações (Elétrica/Hidráulica) e Acabamentos internos, típicos de torres ou edifícios de uso misto.
- **projetos_exemplares:** etr-zion-meridian-tower, amalfi-maiori
- **ac_range:** 350-5000 m²
- **n_estimado_total:** 2

### 5.
- **nome_familia:** Projetos de Nicho e Execução Detalhada (Foco em Orçamento)
- **criterios:** Projetos de pequeno porte (AC < 600m²) com foco extremamente detalhado em Orçamento Executivo, Superestrutura e sistemas específicos, sugerindo um escopo altamente especializado.
- **projetos_exemplares:** thozen-mirador-de-alicante
- **ac_range:** 300-600 m²
- **n_estimado_total:** 1

## Outliers estruturais

### 1.
- **slug:** adore-cacupe
- **campo:** concreto_m3_m2
- **valor:** 0.8657
- **tipo:** muito_alto
- **causa_provavel:** Possível erro de medição ou projeto com excesso de concreto em relação à área construída.

### 2.
- **slug:** adore-cacupe
- **campo:** forma_m2_m2
- **valor:** 6.9527
- **tipo:** muito_alto
- **causa_provavel:** Indica um alto consumo de formas, sugerindo um projeto complexo ou excessivo de elementos verticais.

### 3.
- **slug:** fg-blue-coast
- **campo:** concreto_m3_m2
- **valor:** 0.6247
- **tipo:** muito_alto
- **causa_provavel:** Alto volume de concreto, indicando uma estrutura muito massiva ou um erro de cálculo.

### 4.
- **slug:** fg-blue-coast
- **campo:** aco_kg_m3
- **valor:** 147.59
- **tipo:** muito_alto
- **causa_provavel:** Excesso de aço, podendo indicar superdimensionamento estrutural ou erro de cálculo.

### 5.
- **slug:** nova-empreendimentos-domus
- **campo:** concreto_m3_m2
- **valor:** 0.6829
- **tipo:** muito_alto
- **causa_provavel:** Volume de concreto significativamente acima da média, sugerindo alta densidade estrutural.

### 6.
- **slug:** nova-empreendimentos-domus
- **campo:** forma_m2_m2
- **valor:** 6.1865
- **tipo:** muito_alto
- **causa_provavel:** Consumo de formas extremamente alto, indicando um projeto com muitas superfícies verticais ou complexidade elevada.

### 7.
- **slug:** gdi-playa-negra
- **campo:** concreto_m3_m2
- **valor:** 0.6212
- **tipo:** muito_alto
- **causa_provavel:** Alto volume de concreto, sugerindo estrutura robusta ou erro de medição.

### 8.
- **slug:** gdi-playa-negra
- **campo:** forma_m2_m2
- **valor:** 4.0826
- **tipo:** muito_alto
- **causa_provavel:** Alto consumo de formas, indicando grande área de superfície a ser moldada.

### 9.
- **slug:** grupo-duo-colin
- **campo:** concreto_m3_m2
- **valor:** 0.6346
- **tipo:** muito_alto
- **causa_provavel:** Volume de concreto elevado, sugerindo estrutura muito pesada ou superdimensionada.

### 10.
- **slug:** grupo-duo-colin
- **campo:** forma_m2_m2
- **valor:** 4.886
- **tipo:** muito_alto
- **causa_provavel:** Consumo de formas muito alto, indicando complexidade ou grande área de superfície.

### 11.
- **slug:** somauma-virginia
- **campo:** concreto_m3_m2
- **valor:** 0.0336
- **tipo:** muito_baixo
- **causa_provavel:** Volume de concreto extremamente baixo, podendo indicar erro de medição ou estrutura muito leve.

### 12.
- **slug:** somauma-virginia
- **campo:** forma_m2_m2
- **valor:** 0.0052
- **tipo:** muito_baixo
- **causa_provavel:** Consumo de formas quase nulo, sugerindo pouca ou nenhuma superfície vertical a ser moldada.

### 13.
- **slug:** homeset-homeset
- **campo:** forma_m2_m2
- **valor:** 0.0896
- **tipo:** muito_baixo
- **causa_provavel:** Consumo de formas muito baixo, indicando pouca área de superfície vertical.

### 14.
- **slug:** hacasa-brisa-da-armacao
- **campo:** aco_kg_m3
- **valor:** 12.5
- **tipo:** muito_baixo
- **causa_provavel:** Baixíssimo teor de aço, podendo indicar subdimensionamento estrutural ou erro de cálculo.

### 15.
- **slug:** cota-365
- **campo:** aco_kg_m3
- **valor:** 17.21
- **tipo:** muito_baixo
- **causa_provavel:** Baixíssimo teor de aço, sugerindo que a estrutura pode estar subdimensionada em relação às cargas esperadas.

## Padrões de observações repetidas

### 1.
- **padrao:** Quantificação seguindo detalhamentos de projeto e
- **exemplos:** Quantificação seguindo detalhamentos de projeto e, Quantificação seguindo detalhamentos de projetos d, Quantificação seguindo detalhamentos de projeto e
- **frequencia_estimada:** alta
- **categoria:** premissa

### 2.
- **padrao:** Levantamento realizado via visus, utilizando arqui
- **exemplos:** Levantamento realizado via visus, utilizando arqui, Levantamento realizado via visus, utilizando arqui, Levantamento realizado via visus, utilizando arqui
- **frequencia_estimada:** media
- **categoria:** premissa

### 3.
- **padrao:** Considerado blocos, vigas de fundação
- **exemplos:** Considerado blocos, vigas de fundação, Considerado blocos, vigas de fundação, Considerado blocos, vigas de fundação
- **frequencia_estimada:** alta
- **categoria:** premissa

### 4.
- **padrao:** Considerado empolamento 30% da escavação
- **exemplos:** Considerado empolamento 30% da escavação, Considerado empolamento 30% da escavação, Considerado empolamento 30% da escavação
- **frequencia_estimada:** alta
- **categoria:** premissa

### 5.
- **padrao:** Armação com consideração de aço cortado e dobra em
- **exemplos:** Armação com consideração de aço cortado e dobra em, Armação com consideração de aço cortado e dobra em
- **frequencia_estimada:** media
- **categoria:** premissa

### 6.
- **padrao:** Considerado sem indicação em projeto
- **exemplos:** Considerado sem indicação em projeto, Considerado sem indicação em projeto, Considerado sem indicação em projeto
- **frequencia_estimada:** media
- **categoria:** premissa

### 7.
- **padrao:** GERENCIAMENTO TÉCNICO E ADMINISTRATIVO
- **exemplos:** GERENCIAMENTO TÉCNICO E ADMINISTRATIVO, GERENCIAMENTO TÉCNICO E ADMINISTRATIVO, GERENCIAMENTO TÉCNICO E ADMINISTRATIVO
- **frequencia_estimada:** alta
- **categoria:** subdisciplina

### 8.
- **padrao:** Justificativa de escavação/fundação
- **exemplos:** [justificativa]Considerado blocos, vigas de fundaç, [justificativa]Considerado 1 bomba para execução d, [justificativa]Considerado blocos, vigas de fundaç
- **frequencia_estimada:** alta
- **categoria:** justificativa

### 9.
- **padrao:** Movimentação de terra para bota fora
- **exemplos:** [Movimentação de Terra]0,24%, [MOVIMENTAÇÃO DE TERRA]Movimentação de terra para 
- **frequencia_estimada:** media
- **categoria:** premissa

### 10.
- **padrao:** Alerta de divergência de custo
- **exemplos:** [alerta]Custo no Sienge e apropriado divergem muit, [alerta]Valor do Sienge 126 mil/ apropriado 586 mi
- **frequencia_estimada:** baixa
- **categoria:** alerta

### 11.
- **padrao:** Estrutura de concreto com alvenaria de vedação.
- **exemplos:** [Geral]Estrutura de concreto com alvenaria de veda
- **frequencia_estimada:** baixa
- **categoria:** premissa

### 12.
- **padrao:** Serviços de Lazer (Piscina, Academia)
- **exemplos:** [Geral]Área de Lazer: Piscina, Salão de Festas, Ac, [Lazer]Duas áreas de lazer, com piscina, academia,
- **frequencia_estimada:** media
- **categoria:** premissa

## Novos índices derivados sugeridos

### 1.
- **nome_indice:** Índice de Intensidade Estrutural (IE)
- **formula:** (Custo de Estrutura + Custo de Fundações) / AC
- **macrogrupo_relacionado:** Estrutura e Fundações
- **valor_potencial:** Permite comparar a complexidade estrutural (e, portanto, o risco e o custo de engenharia) de diferentes projetos, independentemente do tamanho total. É crucial para identificar se o custo está na fund
- **n_projetos_disponiveis:** 10

### 2.
- **nome_indice:** Índice de Complexidade de Instalações (ICI)
- **formula:** (Custo de Elétrica + Custo de Hidráulica + Custo de Gás) / AC
- **macrogrupo_relacionado:** Instalações e Sistemas
- **valor_potencial:** Mede a densidade de serviços técnicos. Um ICI alto pode indicar um projeto de alto padrão ou alta complexidade operacional (ex: laboratórios, data centers), ajudando a prever custos de MEP (Mechanical
- **n_projetos_disponiveis:** 12

### 3.
- **nome_indice:** Custo de Acabamento por Área Útil (CAAU)
- **formula:** (Custo de Acabamentos + Custo de Mobiliário) / AC
- **macrogrupo_relacionado:** Acabamentos e Mobiliário
- **valor_potencial:** É um indicador de luxo e padrão de mercado. Permite segmentar projetos em categorias (econômico, médio, alto luxo) de forma quantitativa, sendo mais robusto que apenas olhar o R$/m² total.
- **n_projetos_disponiveis:** 10

### 4.
- **nome_indice:** Índice de Impacto de Terraplenagem (IET)
- **formula:** Custo de Movimentação de Terra / AC
- **macrogrupo_relacionado:** Infraestrutura Básica e Movimentação de Terra
- **valor_potencial:** Quantifica o impacto do terreno no custo final. Um IET alto pode sinalizar necessidade de contenção, tratamento de solo ou grandes variações topográficas, sendo um indicador de risco geotécnico.
- **n_projetos_disponiveis:** 8

### 5.
- **nome_indice:** Overhead de Gestão e Administração (OGA)
- **formula:** Custo de Gerenciamento Técnico e Administrativo / (Custo Total - Custo de Serviços Básicos)
- **macrogrupo_relacionado:** Serviços Gerais e Administrativo
- **valor_potencial:** Mede a proporção de custo dedicada à gestão e coordenação em relação ao custo físico de construção. Ajuda a identificar projetos que exigem alto nível de supervisão ou que possuem escopo de serviços c
- **n_projetos_disponiveis:** 12

### 6.
- **nome_indice:** Complexidade de Fachada (ICF)
- **formula:** Custo de Esquadrias e Fachada / AC
- **macrogrupo_relacionado:** Fechamento e Acabamentos
- **valor_potencial:** Indica a sofisticação e o custo do envelope do edifício. É um indicador chave para o marketing imobiliário e para a previsão de custos em projetos de alto impacto visual.
- **n_projetos_disponiveis:** 10

### 7.
- **nome_indice:** Índice de Serviços Complementares (ISC)
- **formula:** Custo de Serviços Complementares / AC
- **macrogrupo_relacionado:** Serviços Complementares
- **valor_potencial:** Captura custos 'fora da caixa' (ex: paisagismo, áreas de lazer, equipamentos específicos). É vital para avaliar o custo de qualidade de vida e o valor agregado ao empreendimento.
- **n_projetos_disponiveis:** 12

### 8.
- **nome_indice:** Risco de Premissas (RP)
- **formula:** Contagem de [premissa] ou [justificativa] nas observações / Total de Sub-disciplinas
- **macrogrupo_relacionado:** Análise de Dados Qualitativos
- **valor_potencial:** Mede a dependência do custo final em suposições ou ajustes manuais. Quanto maior o RP, maior o risco de desvio orçamentário, pois o custo não está totalmente ancorado em detalhes de projeto.
- **n_projetos_disponiveis:** 25

### 9.
- **nome_indice:** Densidade de Sub-disciplinas (DSD)
- **formula:** Contagem total de sub-disciplinas únicas / AC
- **macrogrupo_relacionado:** Estrutura de Dados
- **valor_potencial:** Mede a diversidade e a abrangência do escopo do projeto. Um DSD alto sugere um projeto multidisciplinar e complexo, exigindo mais coordenação e maior risco de conflitos de escopo.
- **n_projetos_disponiveis:** 25

### 10.
- **nome_indice:** Custo de Equipamentos Especiais (CEE)
- **formula:** Custo de Elevadores + Custo de Geradores / AC
- **macrogrupo_relacionado:** Equipamentos e Sistemas Especiais
- **valor_potencial:** Isola o custo de equipamentos de alto valor agregado e impacto operacional (elevadores, bombas, geradores). É um indicador direto da funcionalidade e do nível de serviço do edifício.
- **n_projetos_disponiveis:** 10

## Lacunas de cobertura na base

### 1.
- **lacuna:** Área Útil (UR) e Unidades Residenciais Definidas
- **impacto:** alto
- **n_projetos_afetados:** 7
- **como_resolver:** Padronizar a coleta de dados exigindo o número total de unidades (apartamentos/salas) e a área útil média por unidade, em vez de apenas a Área Construída (AC) total.

### 2.
- **lacuna:** Custo por Metro Quadrado (R$/m²) Consistente
- **impacto:** alto
- **n_projetos_afetados:** 3
- **como_resolver:** Exigir o preenchimento obrigatório do R$/m² em todas as submissões, e detalhar se o custo inclui ou exclui impostos, taxas e serviços de gestão.

### 3.
- **lacuna:** Detalhamento de Sustentabilidade e Certificações (ESG)
- **impacto:** alto
- **n_projetos_afetados:** 9
- **como_resolver:** Criar um checklist obrigatório de requisitos ESG, cobrindo eficiência energética (certificações), gestão de resíduos e uso de materiais de baixo impacto ambiental.

### 4.
- **lacuna:** Custos Operacionais e de Manutenção (OPEX)
- **impacto:** alto
- **n_projetos_afetados:** 9
- **como_resolver:** Incluir uma seção de análise de ciclo de vida (LCA) ou custos operacionais projetados (OPEX) para os primeiros 5 anos de uso, detalhando manutenção de equipamentos críticos (elevadores, bombas, sistem

### 5.
- **lacuna:** Especificação de Equipamentos e Sistemas Críticos (Backup/Energia)
- **impacto:** medio
- **n_projetos_afetados:** 7
- **como_resolver:** Padronizar a exigência de detalhes sobre subestações elétricas, capacidade de geradores de backup (Nº de geradores, potência em kVA) e sistemas de automação predial (BMS).

### 6.
- **lacuna:** Materiais de Acabamento e Fornecedores Premium
- **impacto:** medio
- **n_projetos_afetados:** 9
- **como_resolver:** Exigir o cadastro de materiais de alto custo (pisos, esquadrias, louças) com marca, modelo e fornecedor específico, em vez de apenas categorias genéricas (ex: 'porcelanato').

### 7.
- **lacuna:** Detalhes de Infraestrutura de Lazer e Áreas Comuns
- **impacto:** medio
- **n_projetos_afetados:** 6
- **como_resolver:** Criar um escopo detalhado para áreas de lazer, incluindo dimensionamento de equipamentos (academia, piscinas aquecidas, etc.), e a previsão de serviços complementares (paisagismo, iluminação cênica).

### 8.
- **lacuna:** Gestão de Riscos e Contingência (Reserva Técnica)
- **impacto:** medio
- **n_projetos_afetados:** 9
- **como_resolver:** Exigir a inclusão de uma reserva técnica percentual (ex: 5-10% do custo total) e a justificativa de sua aplicação, cobrindo variações de escopo ou custos não previstos.
