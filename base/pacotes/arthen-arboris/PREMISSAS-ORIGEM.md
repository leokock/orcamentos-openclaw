---
projeto: Arthen Arboris
cliente: Arthen Empreendimentos
local: Itapema/SC (Morretes — Ruas 418 e 420)
data_base: Março/2026
versao: v00 (primeira entrega ao cliente)
data_analise: Abril/2026
fonte_primaria: MORRETES - RUA 418 - MEMORIAL DESCRITIVO.pdf (07/08/2024)
---

# Origem das Premissas — Arthen Arboris

Este documento apresenta, item a item, de onde vieram as premissas adotadas no paramétrico:

- **[MEMORIAL]** — especificação declarada explicitamente no memorial descritivo do cliente
- **[CARTESIAN]** — estimativa Cartesian com base em média de mercado e em 126 obras comparáveis já orçadas
- **[PROJETO]** — dado obtido dos projetos arquitetônicos (DWG/PDF) do Drive

---

## Dados físicos e premissas gerais

| Campo | Valor | Fonte |
|---|---|---|
| Endereço | Ruas 418 e 420, Morretes — Itapema/SC | Memorial |
| Área do terreno | 1.008,00 m² | Memorial |
| Área construída total | 12.472,98 m² | Memorial |
| Unidades residenciais | 90 | Memorial |
| Unidades comerciais | 8 | Memorial |
| Total de unidades | 98 | Memorial |
| Vagas de estacionamento | 99 | Memorial |
| Pavimentos | 24 (Térreo + G1 + G2 + G3 + Diferenciado + 14 Tipo + Rooftop + Cobertura) | Memorial + Projetos |
| Apartamentos por andar tipo | 6 (2 suítes + lavabo + living com cozinha + sacada com churrasqueira) | Memorial |
| Elevadores | 2 (1 social + 1 de emergência) | Memorial |
| Padrão declarado | Médio (Interesse Social) | Memorial |
| Subsolos | Não há — tudo acima do nível do solo | Memorial |
| Sistema estrutural | Concreto armado com estacas hélice contínua | Memorial |
| Aço | CA-50 e CA-60 | Memorial |
| Prazo de execução | 36 meses | Cartesian — prática usual para torres de 24 pavimentos |
| CUB referência | R$ 3.028,45 (Março/2026) | Sinduscon-SC |

---

## Macrogrupo 1 — Gerenciamento Técnico e Administrativo

| Item | Premissa adotada | Fonte |
|---|---|---|
| Prazo de 36 meses | Prática usual Cartesian para torres de 24 pavimentos | Cartesian |
| Engenheiro residente PJ | R$ 8.000/mês | Cartesian — padrão médio |
| Mestre de obras | R$ 7.000/mês | Cartesian — padrão médio |
| Encarregado | R$ 4.000/mês | Cartesian — padrão médio |
| Almoxarife | R$ 3.377/mês | Cartesian — valor de mercado |
| Vigilância (verba mensal) | R$ 5.000/mês | Cartesian — verba enxuta |
| Limpeza de obra (2 auxiliares) | R$ 2.500/mês cada | Cartesian |
| EPI coletivo | R$ 908/mês | Cartesian |
| Placas de identificação da obra | Conforme normas | Memorial item 1 |
| Canteiro + containers + instalações provisórias | Dimensionamento Cartesian | Cartesian |
| Cremalheira e minigrua em regime de locação | Necessário para torre de 24 pav. | Cartesian |
| Projetos e consultorias (arquitetura + ATP + compatibilização BIM) | Escopo padrão | Cartesian |
| Taxas, seguros, ensaios tecnológicos e meio ambiente | Exigências legais | Cartesian |

## Macrogrupo 2 — Movimentação de Terra

| Item | Premissa adotada | Fonte |
|---|---|---|
| Escavação para fundações | Memorial item 2 | Memorial |
| R$ 15/m² AC | Valor de mercado para obra sem subsolo em solo típico do litoral norte SC | Cartesian + Memorial |

## Macrogrupo 3 — Infraestrutura

| Item | Premissa adotada | Fonte |
|---|---|---|
| Fundação em estacas hélice contínua Ø40cm | Memorial item 4.1 (NBR 6122) | Memorial |
| 190 estacas × 20m de profundidade média | Estimado a partir do projeto arquitetônico e da sondagem | Projeto |
| PU perfuração R$ 82/m | Valor de mercado para hélice contínua Ø40cm | Cartesian |
| PU concreto de estaca R$ 632/m³ | Valor de mercado (inclui bombeamento em perfuração) | Cartesian |
| PU aço de fundação R$ 8,77/kg | Valor de mercado | Cartesian |
| Blocos, baldrames e formas | Dimensionamento padrão | Cartesian |
| Mão de obra de fundação (empreitada) | Split padrão Cartesian (~35%) | Cartesian |

## Macrogrupo 4 — Supraestrutura

| Item | Premissa adotada | Fonte |
|---|---|---|
| Sistema em concreto armado | Memorial item 4.2 | Memorial |
| Laje maciça convencional | Memorial declara "laje mista conforme projeto estrutural" — premissa conservadora: maciça | Memorial + Cartesian |
| fck 30 MPa | Memorial declara mínimo 20 MPa; Cartesian adota 30 MPa como prática moderna para torres altas | Memorial + Cartesian |
| Aço CA-50 | Memorial item 4.2 | Memorial |
| Formas em compensado plastificado 18mm | Memorial permite compensado naval 17mm; Cartesian usa 18mm plastificado (padrão atual) | Memorial + Cartesian |
| Consumo de concreto 0,25 m³/m² AC | Valor de mercado para torres altas com laje maciça | Cartesian |
| Consumo de aço 106 kg/m² AC | Valor de mercado para pé-direito 3,00m e 19 pav. tipo | Cartesian |
| Consumo de forma 7,12 m²/m² AC | Valor de mercado | Cartesian |
| PU concreto fck30 R$ 590/m³ | Valor de mercado atual — bombeamento e usinagem | Cartesian |
| PU aço CA-50 R$ 8,67/kg | Valor de mercado — corte, dobra e entrega | Cartesian |
| PU forma (fabricação) R$ 88/m² | Valor de mercado — compensado plastificado | Cartesian |
| Mão de obra estrutural empreitada R$ 185/m² AC | Valor de mercado para empreitada de estrutura em concreto armado | Cartesian |
| Escoramento metálico em locação R$ 20/m² de forma | Valor de mercado para laje maciça convencional | Cartesian |

## Macrogrupo 5 — Alvenaria

| Item | Premissa adotada | Fonte |
|---|---|---|
| Alvenaria em bloco cerâmico 14cm (tijolo furado) em todas as vedações | Memorial item 4.3 | Memorial |
| Encunhamento com argamassa + aditivo expansor | Memorial item 4.3 | Memorial |
| Vergas e contravergas em concreto armado | Memorial item 4.3 | Memorial |
| Escada enclausurada em bloco de concreto celular (resistência ao fogo) | Memorial item 4.3 | Memorial |
| PU bloco cerâmico R$ 32,95/m² | Valor de mercado | Cartesian |
| Argamassa de assentamento R$ 3,80/m² | Valor de mercado | Cartesian |
| Mão de obra de alvenaria (empreitada) R$ 28,50/m² | Valor de mercado | Cartesian |

## Macrogrupo 6 — Impermeabilização

| Item | Premissa adotada | Fonte |
|---|---|---|
| Manta asfáltica 4mm em áreas externas, terraços, sacadas, caixa d'água, lajes, piscinas e forro de casa de máquinas | Memorial item 4.5 | Memorial |
| Argamassa polimérica em BWCs, lavabos e áreas técnicas | Memorial item 4.5 | Memorial |
| Vigas de fundação | Memorial item 4.5 | Memorial |
| Índice de 0,30 m²/m² AC | Valor de mercado para obra sem subsolo, com piscina e áreas molhadas completas | Cartesian |
| PU manta R$ 82,11/m² + MO R$ 68/m² + regularização R$ 19,50/m² | Valor de mercado | Cartesian |

## Macrogrupo 7 — Instalações

| Item | Premissa adotada | Fonte |
|---|---|---|
| Água, esgoto e pluvial em PVC rígido Tigre/Amanco | Memorial item 8.4 | Memorial |
| Captação de água da chuva + cisterna | Memorial item 8.4 | Memorial |
| Medidor individual de água por apartamento | Memorial item 8.4 | Memorial |
| 12 pontos de água fria e quente por apartamento | Memorial item 8.4.1 | Memorial |
| Gás GLP com central no térreo (comodato) e medidor por andar | Memorial itens 8.1 e 8.2 | Memorial |
| Sistema de preventivos: extintores + hidrantes + alarme + iluminação de emergência + sinalização | Memorial item 8.5 | Memorial |
| Para-raios (SPDA) | Memorial itens 8.5 | Memorial |
| Elétrica com condutores Pirelli/Conduspar + interruptores Tramontina/Pial | Memorial item 8.6 | Memorial |
| Pontos de espera para ar-condicionado split (dreno + eletroduto) em suítes e sala | Memorial item 8.3 | Memorial |
| Sensores de presença em áreas comuns | Memorial item 8.7 | Memorial |
| Dimensionamento de pontos elétricos e hidráulicos | Valor de mercado para tipologia 2 suítes + lavabo | Cartesian |
| PUs materiais (elétrica, hidro, preventivas, gás e telecom) | Valor de mercado | Cartesian |

## Macrogrupo 8 — Sistemas Especiais

| Item | Premissa adotada | Fonte |
|---|---|---|
| 2 elevadores (1 social + 1 de serviço/emergência) para 8 pessoas | Memorial item 8.8 | Memorial |
| Marca Atlas / Thyssen Krupp / Otis / Boxtop / Lgtech ou equivalente | Memorial item 8.8 | Memorial |
| PU elevador social R$ 260.000 | Valor de mercado para torre de 19 pavimentos tipo | Cartesian |
| PU elevador de serviço R$ 250.000 | Valor de mercado para torre de 19 pavimentos tipo | Cartesian |
| Gerador dedicado R$ 180.000 | Valor de mercado (memorial não detalha o equipamento) | Cartesian |
| Piscina adulto + piscina infantil + ofurô no Rooftop | Memorial (18º Pavto Rooftop) | Memorial |
| Equipamentos de piscina R$ 220.000 | Valor de mercado | Cartesian |
| SPDA (para-raios) | Memorial item 8.5 | Memorial |
| CFTV + interfonia + automação + bombas + quadros de comando | Dimensionamento Cartesian (memorial não detalha) | Cartesian |

## Macrogrupo 9 — Climatização

| Item | Premissa adotada | Fonte |
|---|---|---|
| Infraestrutura de ar-condicionado (dreno + eletroduto + recuo drywall) em suítes e sala | Memorial item 8.3 — somente infraestrutura | Memorial |
| Exaustão mecânica de BWCs enclausurados | Projeto arquitetônico | Cartesian + Projeto |
| Exaustão de churrasqueiras (sacadas dos apartamentos) | Memorial (sacada com churrasqueira) | Memorial |
| Infraestrutura geral de ar-condicionado R$ 10/m² AC | Valor de mercado | Cartesian |

## Macrogrupo 10 — Revestimentos Internos de Parede

| Item | Premissa adotada | Fonte |
|---|---|---|
| Reboco em massa única + chapisco em todas as paredes internas (alvenaria 100% em bloco cerâmico) | Memorial item 4.3 (alvenaria convencional) | Memorial |
| Azulejo 30×45 em banheiros | Memorial itens 5.3 e 6.3.2 | Memorial |
| Azulejo 30×45 na parede molhada da cozinha (não em toda a parede) | Memorial item 6.4.2 | Memorial |
| Azulejo 30×45 na parede molhada da área de serviço | Memorial item 6.5.2 | Memorial |
| Paredes de sala, suítes, circulação e lavabos: pintura (sem azulejo) | Memorial itens 6.1.2, 6.2.2, 6.6.2 | Memorial |
| Porcelanato nas paredes dos halls principais do edifício | Memorial item 7.1.1 | Memorial |
| Marcas de acabamento: Eliane, Cecrisa, Itagres, Portobello, Pettra ou equivalente | Memorial item 5.3 | Memorial |
| PU azulejo 30×45 R$ 38/m² | Valor de mercado para o formato especificado | Cartesian |
| PU porcelanato de parede R$ 85/m² | Valor de mercado | Cartesian |
| Argamassa colante + rejunte flexível | Prática usual | Cartesian |
| Mão de obra de reboco R$ 22,50/m² + MO cerâmica R$ 35/m² | Valor de mercado (empreitada) | Cartesian |

## Macrogrupo 11 — Revestimentos e Acabamentos em Teto

| Item | Premissa adotada | Fonte |
|---|---|---|
| Forro de gesso acartonado liso (sem moldura, com negativo no perímetro) em todas as áreas privativas | Memorial itens 6.1.3 a 6.6.3 | Memorial |
| Forro resistente à umidade em BWCs e áreas molhadas | Prática de execução | Cartesian |
| Teto de estacionamento e áreas comuns: reboco com pintura acrílica | Memorial itens 7.1.3 e 7.3.4 | Memorial |
| PU forro ST R$ 28/m² + RU R$ 35/m² | Valor de mercado | Cartesian |

## Macrogrupo 12 — Pisos e Pavimentações

| Item | Premissa adotada | Fonte |
|---|---|---|
| Sala e circulação: porcelanato 60×60 Portobello/Eliane | Memorial itens 6.1.1 | Memorial |
| Suítes: piso laminado Eucafloor/Durafloor/Duratex | Memorial itens 5.1.3 e 6.2.1 | Memorial |
| Banheiros, cozinha, área de serviço e lavabos: porcelanato 60×60 | Memorial itens 6.3.1 a 6.6.1 | Memorial |
| Estacionamento: cimento alisado | Memorial item 7.3.1 | Memorial |
| Halls comuns do edifício: granito polido (Andorinha / Ubatuba / Samoa) | Memorial item 5.1.1 | Memorial |
| Contrapiso autonivelante | Prática de execução | Cartesian |
| Rodapé em poliestireno, madeira ou cerâmica | Memorial itens 6.1.4 e seguintes | Memorial |
| PU porcelanato R$ 81/m² | Valor de mercado | Cartesian |
| PU laminado R$ 65/m² | Valor de mercado | Cartesian |

## Macrogrupo 13 — Pintura Interna

| Item | Premissa adotada | Fonte |
|---|---|---|
| Paredes privativas: tinta PVA aplicada sobre massa acrílica (sistema único: emassamento como base + acabamento em PVA) | Memorial itens 5.4 e 6.1.2 | Memorial |
| Marcas de tinta: Suvinil ou Coral | Memorial item 5.4 | Memorial |
| Tetos: tinta acrílica em 2 demãos | Memorial item 7.1.3 | Memorial |
| Estacionamento, escadaria e áreas técnicas: pintura látex ou textura | Memorial itens 7.3 e 7.6.3 | Memorial |
| Demarcação de vagas em cores amarelo e preto conforme norma | Memorial item 7.3.5 | Memorial |
| PU massa acrílica R$ 6/m² | Valor de mercado | Cartesian |
| PU tinta PVA R$ 3/m² (2 demãos) | Valor de mercado | Cartesian |
| PU acrílica teto R$ 3,83/m² + selador R$ 2,50/m² | Valor de mercado | Cartesian |
| Mão de obra de pintura R$ 15/m² + lixamento R$ 8/m² (empreitada) | Valor de mercado | Cartesian |

## Macrogrupo 14 — Esquadrias, Vidros e Ferragens

| Item | Premissa adotada | Fonte |
|---|---|---|
| Janelas de alumínio com pintura eletrostática preta | Memorial item 5.7 | Memorial |
| Soleiras em granito nas janelas | Memorial item 5.7 | Memorial |
| Guarda-corpo de sacadas em alvenaria + esquadria de alumínio envidraçada | Memorial item 5.7.1 | Memorial |
| Portas dos apartamentos: folhas laminadas semi-ocas brancas + caixilhos em madeira de reflorestamento | Memorial item 5.6 | Memorial |
| Ferragens em zamac com acabamento acetinado ou cromado — Papaiz, Arouca, Pado ou equivalente | Memorial item 5.9 | Memorial |
| Serralheria interna: corrimãos, guarda-corpos, portões de garagem e grades técnicas | Escopo usual para o padrão | Cartesian |
| PUs esquadria alumínio + serralheria | Valor de mercado | Cartesian |

## Macrogrupo 15 — Louças e Metais

O memorial define um escopo reduzido para este macrogrupo. **Serão fornecidas pela construtora apenas:**

| Item | Premissa adotada | Fonte |
|---|---|---|
| Bacias sanitárias com caixas de descarga acopladas | Memorial itens 5.5 e 6.3.4 | Memorial |
| Marca Deca, Incepa, Celite ou equivalente | Memorial item 5.5 | Memorial |
| Quantidade: 3 bacias por apartamento (2 suítes + 1 lavabo) × 98 unidades = 294 bacias | Projeto arquitetônico | Memorial + Projeto |
| PU unitário R$ 650 (bacia + caixa acoplada + MO de instalação) | Valor de mercado | Cartesian |

**Itens que ficarão por conta do comprador ou de terceiros, conforme memorial item 12:** cubas e pias, bancadas de granito, torneiras, chuveiros (duchas e elétricos), acabamentos hidráulicos (metais sanitários), assentos sanitários, box dos banheiros, luminárias, tanques de roupa, aparelhos de ar condicionado, olho mágico e mobílias.

## Macrogrupo 16 — Fachada

| Item | Premissa adotada | Fonte |
|---|---|---|
| Tinta premium acrílica em 2 a 4 cores, aplicada com textura | Memorial item 9.1 | Memorial |
| Muros: tinta premium acrílica lisa ou com textura | Memorial item 9.2 | Memorial |
| PU material (textura premium) R$ 50/m² | Valor de mercado | Cartesian |
| PU mão de obra de aplicação R$ 30/m² | Valor de mercado | Cartesian |
| PU balancim fachadeiro R$ 18/m² | Necessário para torre de 24 pavimentos | Cartesian |
| Índice fachada/AC de 1,55 m²/m² | Valor usual para torre vertical de 24 andares | Cartesian |

## Macrogrupo 17 — Serviços Complementares

| Item | Premissa adotada | Fonte |
|---|---|---|
| Central de lixo (piso cerâmico, paredes azulejadas, portas de alumínio) | Memorial item 7.4 | Memorial |
| Central de gás (piso antiderrapante, portas de alumínio) | Memorial item 7.5 | Memorial |
| Caixas d'água em fibra de vidro Fortlev / Bakof Tec | Memorial item 7.6 | Memorial |
| Cobertura: laje impermeabilizada ou telha fibrocimento 6mm com estrutura em madeira de lei ou metálica | Memorial itens 4.6 e 7.7 | Memorial |
| Rooftop (18º Pavto): sala de jogos + coworking + espaço kids + 2 áreas gourmet + ofurô + 2 piscinas + academia + 2 lavabos | Memorial (descrição do 18º Pavto) | Memorial |
| Pintura dos muros: tinta premium acrílica | Memorial item 9.2 | Memorial |
| Paisagismo, mobiliário de áreas comuns e comunicação visual | Escopo usual para o padrão | Cartesian |
| Limpeza final, ligações definitivas e desmobilização | Prática de entrega | Cartesian |

## Macrogrupo 18 — Imprevistos e Contingências

| Item | Premissa adotada | Fonte |
|---|---|---|
| 1,5% sobre o subtotal do orçamento | Padrão Cartesian para orçamentos paramétricos | Cartesian |

---

## Resumo

O paramétrico do Arboris foi construído com **forte aderência ao memorial descritivo do cliente**. Todas as especificações de acabamento (pisos, paredes, tetos, pintura, louças, esquadrias, fachada) seguem literalmente o que foi declarado no memorial de agosto/2024. Os valores de mercado Cartesian (PUs e mão de obra) foram aplicados em itens onde o memorial não traz detalhe quantitativo — principalmente em gerenciamento, dimensionamentos físicos (m³ de concreto, kg de aço, m² de forma), mão de obra especializada e imprevistos.
