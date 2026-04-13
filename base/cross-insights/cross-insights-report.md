# Cross-Project Insights — Phase 5
_Gerado em 2026-04-13T19:59:01_

Análise de **126 projetos** da base Cartesian via Gemma local.
5 perguntas independentes, ~568s total.

## Famílias de projetos por similaridade

### 1.
- **nome_familia:** Loteamentos e Master Plan (Infraestrutura Pesada)
- **criterios:** Projetos de escala massiva (AC > 10.000m²) focados em infraestrutura básica, pavimentação, drenagem e serviços de loteamento, com custo unitário baixo.
- **projetos_exemplares:** estilo-condominios-estilo-condominios
- **ac_range:** 20000-25000 m²
- **n_estimado_total:** 1

### 2.
- **nome_familia:** Grandes Condomínios Residenciais (Escala Média-Alta)
- **criterios:** Projetos de grande porte (AC > 7000m²) com foco em estrutura residencial, áreas comuns complexas (lazer, academia) e custos unitários moderados, indicando desenvolvimento habitacional consolidado.
- **projetos_exemplares:** fonseca-empreendimentos-estoril, cln-porto-ruby, pass-e-connect, chiquetti-e-dalvesco-cielo
- **ac_range:** 7000-14500 m²
- **n_estimado_total:** 4

### 3.
- **nome_familia:** Alto Padrão e Luxo (Detalhe e Acabamento Premium)
- **criterios:** Projetos de pequeno a médio porte, caracterizados por altíssimo custo por metro quadrado (R$/m² > 60.000) e foco em acabamentos de luxo, superestrutura detalhada e sistemas especializados.
- **projetos_exemplares:** as-ramos-paessaggio, amalfi-maiori, thozen-mirador-de-alicante
- **ac_range:** 260-500 m²
- **n_estimado_total:** 3

### 4.
- **nome_familia:** Desenvolvimento Urbano e Mixed-Use (Equilíbrio Estrutural)
- **criterios:** Projetos de porte médio, com foco em estruturas verticais e sistemas MEP, representando um equilíbrio entre a complexidade estrutural e o custo unitário moderado.
- **projetos_exemplares:** etr-zion-meridian-tower, cn-brava-ocean
- **ac_range:** 450-5500 m²
- **n_estimado_total:** 2

### 5.
- **nome_familia:** Reserva e Ambientação (Baixa Densidade)
- **criterios:** Projetos com foco em áreas de lazer, ambientação e serviços complementares, característicos de reservas ou empreendimentos de baixa densidade construtiva.
- **projetos_exemplares:** rosner-reserva-sao-vicente
- **ac_range:** 5000-7500 m²
- **n_estimado_total:** 1

## Outliers estruturais

### 1.
- **slug:** adore-cacupe
- **campo:** concreto_m3_m2
- **valor:** 0.8657
- **tipo:** muito_alto
- **causa_provavel:** Possível erro de medição ou projeto de estrutura de grande volume não típico.

### 2.
- **slug:** fg-blue-coast
- **campo:** aço_kg_m3
- **valor:** 147.59
- **tipo:** muito_alto
- **causa_provavel:** Alto índice de aço, sugerindo reforço estrutural excessivo ou tipo de elemento não padrão.

### 3.
- **slug:** nova-empreendimentos-domus
- **campo:** forma_m2_m2
- **valor:** 6.1865
- **tipo:** muito_alto
- **causa_provavel:** Forma excessiva, indicando elementos estruturais muito grandes ou complexidade não usual.

### 4.
- **slug:** gdi-playa-negra
- **campo:** forma_m2_m2
- **valor:** 4.0826
- **tipo:** muito_alto
- **causa_provavel:** Forma excessiva, sugerindo elementos de grande porte ou geometria complexa.

### 5.
- **slug:** all-acacias-jk
- **campo:** concreto_m3_m2
- **valor:** 0.5107
- **tipo:** muito_alto
- **causa_provavel:** Volume de concreto muito alto, fora da faixa residencial típica.

### 6.
- **slug:** grupo-duo-colin
- **campo:** forma_m2_m2
- **valor:** 4.886
- **tipo:** muito_alto
- **causa_provavel:** Forma excessiva, indicando um sistema estrutural muito robusto ou não residencial.

### 7.
- **slug:** cota-365
- **campo:** aço_kg_m3
- **valor:** 17.21
- **tipo:** muito_baixo
- **causa_provavel:** Baixo índice de aço, sugerindo subdimensionamento ou uso de materiais não metálicos.

### 8.
- **slug:** hacasa-brisa-da-armacao
- **campo:** concreto_m3_m2
- **valor:** 0.0169
- **tipo:** muito_baixo
- **causa_provavel:** Volume de concreto extremamente baixo, indicando estrutura mínima ou erro de medição.

### 9.
- **slug:** somauma-virginia
- **campo:** concreto_m3_m2
- **valor:** 0.0336
- **tipo:** muito_baixo
- **causa_provavel:** Volume de concreto muito baixo, sugerindo estrutura de fachada ou não estrutural.

### 10.
- **slug:** somauma-virginia
- **campo:** forma_m2_m2
- **valor:** 0.0052
- **tipo:** muito_baixo
- **causa_provavel:** Forma extremamente baixa, indicando ausência de elementos estruturais de concreto.

### 11.
- **slug:** chiquetti-e-dalvesco-cielo
- **campo:** concreto_m3_m2
- **valor:** 0.1197
- **tipo:** muito_baixo
- **causa_provavel:** Volume de concreto abaixo do esperado, podendo indicar estrutura de baixo porte ou erro de medição.

### 12.
- **slug:** blue-heaven-aquos
- **campo:** forma_m2_m2
- **valor:** 0.4878
- **tipo:** muito_baixo
- **causa_provavel:** Forma muito baixa, sugerindo elementos estruturais muito pequenos ou não típicos.

### 13.
- **slug:** blue-heaven-monolyt
- **campo:** aço_kg_m3
- **valor:** 48.21
- **tipo:** muito_baixo
- **causa_provavel:** Baixo índice de aço, sugerindo subdimensionamento ou uso de reforço mínimo.

### 14.
- **slug:** homeset-homeset
- **campo:** forma_m2_m2
- **valor:** 0.0896
- **tipo:** muito_baixo
- **causa_provavel:** Forma extremamente baixa, indicando ausência de elementos estruturais de concreto.

### 15.
- **slug:** chiquetti-e-dalvesco-cielo
- **campo:** aço_kg_m3
- **valor:** 46.33
- **tipo:** muito_baixo
- **causa_provavel:** Baixo índice de aço, sugerindo subdimensionamento ou uso de reforço mínimo.

## Padrões de observações repetidas

### 1.
- **padrao:** Quantificação seguindo detalhamentos de projeto e
- **exemplos:** Quantificação seguindo detalhamentos de projeto e, Quantificação seguindo detalhamentos de projeto e
- **frequencia_estimada:** alta
- **categoria:** premissa

### 2.
- **padrao:** Levantamento realizado via visus, utilizando arqui
- **exemplos:** Levantamento realizado via visus, utilizando arqui, Levantamento realizado via visus, utilizando arqui
- **frequencia_estimada:** alta
- **categoria:** premissa

### 3.
- **padrao:** Considerado blocos, vigas de fundação
- **exemplos:** Considerado blocos, vigas de fundação, Considerado blocos, vigas de fundação
- **frequencia_estimada:** alta
- **categoria:** premissa

### 4.
- **padrao:** Considerado empolamento 30% da escavação
- **exemplos:** Considerado empolamento 30% da escavação, Considerado empolamento 30% da escavação
- **frequencia_estimada:** alta
- **categoria:** premissa

### 5.
- **padrao:** GERENCIAMENTO TÉCNICO E ADMINISTRATIVO
- **exemplos:** GERENCIAMENTO TÉCNICO E ADMINISTRATIVO, GERENCIAMENTO TÉCNICO E ADMINISTRATIVO
- **frequencia_estimada:** alta
- **categoria:** premissa

### 6.
- **padrao:** Considerado sem indicação em projeto
- **exemplos:** Considerado sem indicação em projeto, Considerado sem indicação em projeto
- **frequencia_estimada:** media
- **categoria:** premissa

### 7.
- **padrao:** Justificativa de serviços/elementos
- **exemplos:** Quantidade de aba, advindo do projeto com retirada, Justificativa de serviços/elementos
- **frequencia_estimada:** media
- **categoria:** justificativa

### 8.
- **padrao:** Custo baseado em índices
- **exemplos:** Custo baseado em índices Alameda Jardins, Custo baseado em índices / Solicitado pelo cliente
- **frequencia_estimada:** media
- **categoria:** premissa

### 9.
- **padrao:** Movimentação de terra para bota fora
- **exemplos:** Movimentação de bota-fora para escavação do terren, Movimentação de terra para bota fora, com 30% de f
- **frequencia_estimada:** media
- **categoria:** premissa

### 10.
- **padrao:** Alerta de divergência de custo
- **exemplos:** Custo no Sienge e apropriado divergem muito, Valor do Sienge 126 mil/ apropriado 586 mil
- **frequencia_estimada:** baixa
- **categoria:** alerta

### 11.
- **padrao:** Estrutura de concreto com alvenaria de vedação.
- **exemplos:** Estrutura de concreto com alvenaria de vedação.
- **frequencia_estimada:** baixa
- **categoria:** premissa

### 12.
- **padrao:** Serviços complementares de infraestrutura
- **exemplos:** ORÇAMENTO_EXECUTIVO>INFRAESTRUTURA, Serviços Gerais>INFRAESTRUTURA
- **frequencia_estimada:** media
- **categoria:** sub_disciplina

### 13.
- **padrao:** Revisão de prazo/custo em questionário
- **exemplos:** Custo respondido no questionário dia 18/04/2024, Custo e prazo respondido no questionário dia 18/04
- **frequencia_estimada:** baixa
- **categoria:** revisao

## Novos índices derivados sugeridos

### 1.
- **nome_indice:** Índice de Densidade de Sistemas MEP (Mecânica, Elétrica e Hidráulica)
- **formula:** (Custo de Elétrica + Custo de Hidráulica + Custo de Climatização) / AC (m²)
- **macrogrupo_relacionado:** Instalações e Sistemas
- **valor_potencial:** Permite identificar projetos com alta complexidade de infraestrutura por área construída. É crucial para orçamentos de serviços de engenharia e detecção de subdimensionamento de redes.
- **n_projetos_disponiveis:** 25

### 2.
- **nome_indice:** Índice de Custo de Acabamento por Área de Fachada
- **formula:** Custo de Fachada (Esquadrias + Revestimentos de Fachada) / Área de Fachada (m²)
- **macrogrupo_relacionado:** Acabamentos e Envelopamento
- **valor_potencial:** Mede a sofisticação e o custo do envelope do edifício. É um indicador chave para o mercado de alto padrão e ajuda a diferenciar o valor do acabamento externo do valor interno.
- **n_projetos_disponiveis:** 25

### 3.
- **nome_indice:** Índice de Dependência de Serviços Complementares
- **formula:** Custo de Serviços Complementares / (Custo Total - Custo de Serviços Complementares)
- **macrogrupo_relacionado:** Gestão e Serviços Adicionais
- **valor_potencial:** Quantifica a proporção de custos que não são diretamente estruturais ou de acabamento (ex: mobiliário, paisagismo, gerenciamento). Alto índice sugere complexidade de execução ou alto foco em áreas com
- **n_projetos_disponiveis:** 25

### 4.
- **nome_indice:** Índice de Risco de Escavação e Movimentação de Terra
- **formula:** Custo de Movimentação de Terra + Custo de Fundações / AC (m²)
- **macrogrupo_relacionado:** Infraestrutura e Fundações
- **valor_potencial:** Mede o impacto do terreno e da fundação no custo final. É um indicador de risco geotécnico e de viabilidade, especialmente em terrenos complexos ou com grande volume de terra a ser removida.
- **n_projetos_disponiveis:** 25

### 5.
- **nome_indice:** Índice de Complexidade de Disciplinas (Diversidade)
- **formula:** Número de sub-disciplinas únicas listadas / AC (m²)
- **macrogrupo_relacionado:** Escopo e Detalhamento
- **valor_potencial:** Mede a complexidade do escopo do projeto. Um número alto de sub-disciplinas para uma área dada sugere um projeto multifuncional ou de altíssima customização, aumentando o risco e o tempo de execução.
- **n_projetos_disponiveis:** 25

### 6.
- **nome_indice:** Índice de Custo de Sustentabilidade/Ambientação
- **formula:** Custo de AMBIENTAÇÃO / Custo Total
- **macrogrupo_relacionado:** Sustentabilidade e Impacto Ambiental
- **valor_potencial:** Permite comparar o investimento em mitigação de impacto ambiental em diferentes projetos. É um indicador crescente de valor e conformidade regulatória.
- **n_projetos_disponiveis:** 25

### 7.
- **nome_indice:** Índice de Overhead de Gestão (Gestão Técnica)
- **formula:** Custo de Serviços Gerais/Administrativo / Custo Total
- **macrogrupo_relacionado:** Gerenciamento e Controle
- **valor_potencial:** Mede a porcentagem de custo dedicada à gestão e administração do projeto. Ajuda a identificar se o custo está sendo absorvido por serviços de coordenação ou por execução física.
- **n_projetos_disponiveis:** 25

### 8.
- **nome_indice:** Índice de Densidade de Equipamentos Especiais
- **formula:** Custo de Equipamentos e Sistemas Especiais / AC (m²)
- **macrogrupo_relacionado:** Tecnologia e Equipamentos
- **valor_potencial:** Mede a concentração de tecnologia e equipamentos de alto valor (ex: elevadores, sistemas de segurança complexos, equipamentos médicos). É um indicador de uso de tecnologia e funcionalidade especializa
- **n_projetos_disponiveis:** 25

### 9.
- **nome_indice:** Índice de Proporção de Acabamento vs. Estrutura
- **formula:** Custo de Acabamentos / Custo de Estrutura e Fundações
- **macrogrupo_relacionado:** Valor Agregado e Acabamento
- **valor_potencial:** É um indicador de luxo e qualidade percebida. Um índice alto sugere que o valor do projeto está mais na estética e conforto do que na mera função estrutural.
- **n_projetos_disponiveis:** 25

### 10.
- **nome_indice:** Índice de Custo de Infraestrutura de Loteamento
- **formula:** Custo de Infraestrutura Básica / AC (m²)
- **macrogrupo_relacionado:** Desenvolvimento Urbano e Loteamento
- **valor_potencial:** Fundamental para projetos de grande escala ou loteamentos. Indica o custo por metro quadrado para levar serviços básicos (pavimentação, drenagem, redes) até a área construída.
- **n_projetos_disponiveis:** 25

## Lacunas de cobertura na base

### 1.
- **lacuna:** Definição e Quantificação da Área Não Coberta (UR)
- **impacto:** alto
- **n_projetos_afetados:** 8
- **como_resolver:** Exigir a quantificação detalhada da Área Não Coberta (UR) em todos os projetos, seja por levantamento topográfico ou por premissa de cálculo, para evitar subestimação de custos de infraestrutura e pai

### 2.
- **lacuna:** Custos de Operação e Manutenção (O&M)
- **impacto:** alto
- **n_projetos_afetados:** 10
- **como_resolver:** Incorporar uma fase de análise de ciclo de vida (LCC) nos dossiês, detalhando custos anuais de manutenção, consumo de energia, água e pessoal para os primeiros 5 anos de operação.

### 3.
- **lacuna:** Detalhamento de Sistemas de Sustentabilidade e Certificações
- **impacto:** alto
- **n_projetos_afetados:** 10
- **como_resolver:** Tornar obrigatória a inclusão de premissas de certificações (LEED, AQUA, etc.), detalhando o uso de materiais de baixo carbono, sistemas de captação de água pluvial e eficiência energética.

### 4.
- **lacuna:** Integração e Detalhamento de Redes de Serviços Urbanos (Saneamento)
- **impacto:** alto
- **n_projetos_afetados:** 9
- **como_resolver:** Exigir o detalhamento específico das conexões e dimensionamentos de redes de água potável, esgoto e drenagem pluvial, incluindo a previsão de taxa de ocupação e capacidade de vazão em pontos de conexã

### 5.
- **lacuna:** Gestão de Riscos e Contingências Estruturadas
- **impacto:** medio
- **n_projetos_afetados:** 10
- **como_resolver:** Implementar um registro formal de riscos (Risk Register) que contemple riscos não técnicos (ex: mudanças regulatórias, atrasos de licenciamento, flutuação cambial) e seus respectivos planos de mitigaç

### 6.
- **lacuna:** Especificação de Materiais e Acabamentos de Áreas Comuns
- **impacto:** medio
- **n_projetos_afetados:** 8
- **como_resolver:** Padronizar a especificação de acabamentos em áreas comuns, exigindo marcas, modelos e fornecedores específicos para pisos, louças e metais, em vez de apenas categorias genéricas.

### 7.
- **lacuna:** Detalhamento de Sistemas de Energia Renovável
- **impacto:** medio
- **n_projetos_afetados:** 7
- **como_resolver:** Incluir a análise de viabilidade técnica e econômica para a integração de fontes de energia renovável (ex: painéis solares fotovoltaicos, sistemas de aquecimento solar) e o dimensionamento de subestaç

### 8.
- **lacuna:** Planejamento de Desmobilização e Resíduos de Construção
- **impacto:** medio
- **n_projetos_afetados:** 8
- **como_resolver:** Exigir um plano detalhado de gestão de resíduos (PGRCC), incluindo custos de descarte, logística reversa e a previsão de desmobilização de estruturas temporárias ao final da obra.

### 9.
- **lacuna:** Detalhamento de Sistemas de Segurança e Controle de Acesso
- **impacto:** medio
- **n_projetos_afetados:** 7
- **como_resolver:** Aprofundar o escopo de segurança, detalhando sistemas de CFTV por zonas, controle biométrico de acesso, e planos de resposta a emergências (brigadas, rotas de fuga, etc.).

### 10.
- **lacuna:** Coordenação e Detalhamento BIM (Building Information Modeling)
- **impacto:** medio
- **n_projetos_afetados:** 6
- **como_resolver:** Tornar obrigatória a entrega de modelos BIM coordenados, com foco em detecção de interferências (clash detection) entre disciplinas (elétrica, hidráulica, estrutura) e a quantificação automatizada de 
