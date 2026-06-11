# Análise detalhada - Brickell vs empreendimentos semelhantes v00

## Objetivo

Comparar o orçamento paramétrico v00 do Brickell Modern Home com cinco empreendimentos internos da base Cartesian/Drive, usando R$/m² e custo normalizado na mesma área construída do Brickell.

## Fontes e critérios

- Fonte dos comparáveis: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Parametrico_IA\REVISAO-OBRAS-131.xlsx`.
- Fonte Brickell: `C:\Users\leona\orcamentos-openclaw\base\pacotes\brickell-nowa\brickell-nowa-parametrico-v00-final.xlsx`.
- Critérios de seleção: residencial vertical em SC/litoral; padrão médio-alto ou alto; porte próximo de 10.840 m²; custo e R$/m² válidos no consolidado; inclusão de um limite superior premium.
- Correção temporal aplicada por CUB: R$/m² valor presente = (R$/m² original / CUB origem) x CUB atual. CUB atual adotado: R$ 3.850,00 (2026-05), fonte: CUB atual adotado no pacote Brickell v00 / Supabase Ampli SC.

## Conclusão executiva

- Brickell está em **4.018 R$/m²**, totalizando **R$ 43.556.004,95**.
- A média dos 5 comparáveis é **3.832 R$/m²**; Brickell está **4,8%** acima.
- A mediana dos 5 comparáveis é **3.629 R$/m²**; Brickell está **10,7%** acima.
- Sem o limite superior `neuhaus-origem`, a média direta cai para **3.630 R$/m²**; Brickell fica **10,7%** acima.
- Em posição relativa, Brickell fica acima de **3** comparáveis e abaixo de **2** comparáveis.
- Faixa da amostra: **terrassa-amaro** em 3.100 R$/m² até **neuhaus-origem** em 4.642 R$/m².

## Conclusão em valor presente por CUB

- Brickell está em **1,04 CUB** e permanece em **4.018 R$/m²** porque já está na base atual adotada.
- A média dos 5 comparáveis corrigidos é **5.160 R$/m² VP**; Brickell fica **-22,1%** contra essa média.
- A mediana corrigida é **4.798 R$/m² VP**; Brickell fica **-16,3%** contra a mediana.
- Sem Neuhaus Origem, a média direta corrigida é **4.918 R$/m² VP**; Brickell fica **-18,3%** contra os comparáveis diretos corrigidos.
- Em valor presente, Brickell fica acima de **0** comparáveis e abaixo de **5** comparáveis.
- Faixa corrigida da amostra: **terrassa-amaro** em 4.328 R$/m² VP até **neuhaus-origem** em 6.129 R$/m² VP.
- Total médio corrigido aplicado à AC do Brickell: **R$ 55.940.809,68**; Brickell fica **R$ -12.384.804,73** contra essa referência.

Leitura: nominalmente o Brickell parecia acima da média direta. Após trazer os comparáveis para valor presente por CUB, ele fica abaixo da média corrigida e abaixo da mediana corrigida. A principal leitura muda: o Brickell não está inflado contra a base histórica; ele está competitivo quando os custos antigos são atualizados.

## Leitura por empreendimento

### adore-level-up

- Local/padrão: Balneário Camboriú/SC, medio-alto, residencial_vertical_alto.
- Porte: AC 11.102,72 m²; UR n/d; total original R$ 40.287.855,69.
- Custo: 3.629 R$/m², abaixo do Brickell. Brickell está 10,7% acima desse comparável.
- CUB/data: 2.911,91 em 2025-08; CUB ratio 1,25; R$/m² em valor presente 4.798, acima do Brickell em valor presente. Em valor presente, esse comparável está 19,4% acima do Brickell.
- Total normalizado na AC do Brickell: R$ 39.335.662,34.
- Total em valor presente normalizado na AC do Brickell: R$ 52.007.891,73.
- Por que entra: Balneário Camboriú, SC, área praticamente igual ao Brickell e tipologia vertical alto/médio-alto. Bom comparável de porte e mercado litorâneo.
- Fonte CUB: `C:\Users\leona\orcamentos-openclaw\archive\v1-pre-fase19\indices\adore-level-up-indices.md`.
- Pasta Drive: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Adore Incorporações\Level Up`.

### terrassa-amaro

- Local/padrão: Itajaí/SC, alto, residencial_vertical_alto.
- Porte: AC 10.479,34 m²; UR n/d; total original R$ 32.487.650,19.
- Custo: 3.100 R$/m², abaixo do Brickell. Brickell está 29,6% acima desse comparável.
- CUB/data: 2.757,56 em 2024-04; CUB ratio 1,12; R$/m² em valor presente 4.328, acima do Brickell em valor presente. Em valor presente, esse comparável está 7,7% acima do Brickell.
- Total normalizado na AC do Brickell: R$ 33.606.715,62.
- Total em valor presente normalizado na AC do Brickell: R$ 46.920.413,39.
- Por que entra: Itajaí, SC, área muito próxima e padrão alto. Entra como referência local direta, mesmo com data-base não informada no consolidado.
- Fonte CUB: `C:\Users\leona\orcamentos-openclaw\archive\v1-pre-fase19\indices\terrassa-amaro-indices.md`.
- Pasta Drive: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Terrassa\Amaro`.

### mussi-empreendimentos-chelsea

- Local/padrão: Itajaí/SC, medio-alto, residencial_vertical_alto.
- Porte: AC 15.149,39 m²; UR 41; total original R$ 52.163.485,94.
- Custo: 3.443 R$/m², abaixo do Brickell. Brickell está 16,7% acima desse comparável.
- CUB/data: 2.846,12 em 2024-11; CUB ratio 1,21; R$/m² em valor presente 4.658, acima do Brickell em valor presente. Em valor presente, esse comparável está 15,9% acima do Brickell.
- Total normalizado na AC do Brickell: R$ 37.326.114,21.
- Total em valor presente normalizado na AC do Brickell: R$ 50.491.736,02.
- Por que entra: Itajaí, SC, 41 UR contra 38 UR do Brickell. Área maior, mas produto e escala de unidades são muito próximos.
- Fonte CUB: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo\Mussi Empreendimentos\Chelsea\CTN_MSS_CLS - Orçamento R02.xlsx`.
- Pasta Drive: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Mussi Empreendimentos\Chelsea Residence 11.2022`.

### gdi-playa-negra

- Local/padrão: Florianópolis/SC, medio-alto, residencial_vertical_alto.
- Porte: AC 8.518,60 m²; UR n/d; total original R$ 37.027.025,39.
- Custo: 4.347 R$/m², acima do Brickell. Esse comparável está 8,2% acima do Brickell.
- CUB/data: 2.841,51 em 2024-08; CUB ratio 1,53; R$/m² em valor presente 5.889, acima do Brickell em valor presente. Em valor presente, esse comparável está 46,6% acima do Brickell.
- Total normalizado na AC do Brickell: R$ 47.118.599,85.
- Total em valor presente normalizado na AC do Brickell: R$ 63.841.622,74.
- Por que entra: Florianópolis, SC, residencial vertical alto/médio-alto, R$/m² próximo ao Brickell. Funciona como comparável de patamar superior operacional.
- Fonte CUB: `C:\Users\leona\orcamentos-openclaw\archive\v1-pre-fase19\indices\gdi-playanegra-indices.md`.
- Pasta Drive: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\GDI Empreendimentos\Playa Negra`.

### neuhaus-origem

- Local/padrão: Florianópolis/SC, alto, residencial_vertical_alto.
- Porte: AC 14.559,12 m²; UR n/d; total original R$ 67.590.131,02.
- Custo: 4.642 R$/m², acima do Brickell. Esse comparável está 15,5% acima do Brickell.
- CUB/data: 2.916,12 em 2025-03; CUB ratio 1,59; R$/m² em valor presente 6.129, acima do Brickell em valor presente. Em valor presente, esse comparável está 52,5% acima do Brickell.
- Total normalizado na AC do Brickell: R$ 50.325.705,56.
- Total em valor presente normalizado na AC do Brickell: R$ 66.442.384,54.
- Por que entra: Florianópolis, SC, padrão alto e área maior. Usei como limite superior para entender se Brickell está perto do teto premium.
- Fonte CUB: `C:\Users\leona\orcamentos-openclaw\archive\v1-pre-fase19\indices\origem-indices.md`.
- Pasta Drive: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Neuhaus\2023.08 - Origem 3300`.

## Por que o Brickell aparece acima da média direta

- O Brickell foi modelado como padrão alto, não médio-alto puro.
- A torre tem 29 níveis no IFC, altura descendente PPCI de 67,32 m e 4 níveis de garagem, o que pressiona estrutura, sistemas, elevadores e gerenciamento.
- O projeto tem climatização com pacote CLI real, gerador, pressurização/controle de fumaça, piscina e lazer de cobertura.
- O custo de complementares e louças foi corrigido no v00 porque o default V2 ficava baixo para o padrão do produto.
- Na leitura nominal, comparáveis com data-base antiga puxavam a média para baixo. Na leitura por CUB, esse efeito é removido e o Brickell passa a ficar competitivo contra a média corrigida.

## Riscos da comparação

- `terrassa-amaro` e `mussi-empreendimentos-chelsea` tinham data-base ausente no consolidado, mas a data/CUB foi recuperada dos arquivos de índices ou do executivo entregue.
- `neuhaus-origem` é limite superior, não comparável médio direto.
- A comparação usa consolidado de R$/m², não abertura item a item de todos os empreendimentos.
- O CUB atual adotado foi o mesmo do pacote Brickell v00 (R$ 3.850,00). Se Leo optar por trocar para outro índice oficial/Sinduscon, os R$/m² em valor presente mudam proporcionalmente, mas os CUB ratios de origem permanecem rastreáveis.
- A v00 do Brickell ainda depende de validação de fachada, vagas, fundação/SPT, esquadrias e memorial de acabamentos.

## Recomendação

- Para validação interna, tratar o Brickell como orçamento dentro da faixa e competitivo em valor presente por CUB.
- Na leitura de apresentação, mostrar duas faixas: comparáveis diretos corrigidos e limite superior premium.
- Se fachada, esquadrias ou acabamentos vierem mais premium que a premissa atual, o Brickell tende a se aproximar mais de `gdi-playa-negra` e `neuhaus-origem`.
- Em total nominal normalizado, a média dos 5 comparáveis na AC do Brickell é **R$ 41.542.559,52**; Brickell está **R$ 2.013.445,44** acima. Sem o limite superior, a média direta nominal normalizada é **R$ 39.346.773,00**.
- Em total corrigido por CUB, a média dos 5 comparáveis na AC do Brickell é **R$ 55.940.809,68**; Brickell está **R$ -12.384.804,73** contra essa referência.
