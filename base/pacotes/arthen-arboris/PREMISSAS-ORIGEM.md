---
projeto: Arthen Arboris
cliente: Arthen Empreendimentos
local: **Itapema/SC** (Morretes — Ruas 418 e 420)
data_base: Março/2026
versao: v00 (primeira entrega ao cliente)
data_analise: 2026-04-20
fonte_primaria: MORRETES - RUA 418 - MEMORIAL DESCRITIVO.pdf (07/08/2024)
---

# Origem das Premissas — Arthen Arboris

> Este documento rastreia **item a item** de onde vieram as premissas do paramétrico. Duas classificações possíveis:
>
> - 📋 **[MEMORIAL]** — especificação explícita no memorial descritivo do cliente
> - 📊 **[CARTESIAN]** — estimativa com base na média de mercado e base histórica Cartesian (126 obras)
> - 🏗️ **[PROJETO]** — obtido dos projetos DWG/PDF no Drive (planta, corte, arquitetura)

---

## Dados físicos e briefing

| Campo | Valor | Fonte |
|---|---|---|
| Endereço | Ruas 418 e 420, Morretes — Itapema/SC | 📋 Memorial |
| Área do terreno | 1.008,00 m² | 📋 Memorial |
| Área construída total | 12.472,98 m² | 📋 Memorial |
| Unidades residenciais | 90 | 📋 Memorial |
| Unidades comerciais | 8 | 📋 Memorial |
| Total de unidades | 98 | 📋 Memorial |
| Vagas de estacionamento | 99 | 📋 Memorial |
| Pavimentos | 24 (Térreo + G1 + G2 + G3 + Diferenciado + 14 Tipo + Rooftop + Cobertura) | 📋 Memorial + 🏗️ Projetos |
| Apartamentos/andar tipo | 6 (2 suítes + lavabo + sala com cozinha + sacada c/ churrasq.) | 📋 Memorial |
| Elevadores | 2 (1 social + 1 emergência), marca Atlas/Thyssen/Otis ou equivalente | 📋 Memorial |
| Padrão declarado | **MÉDIO** (interesse social) | 📋 Memorial |
| Padrão técnico (acabamentos) | Médio-Alto (Portobello, Deca, Incepa) | 📊 Cartesian inferido dos materiais |
| Subsolos | **ZERO** (tudo acima do nível do solo) | 📋 Memorial |
| Sistema estrutural | Concreto armado, estacas hélice contínua | 📋 Memorial |
| fck mínimo concreto | 20 MPa (memorial) → 30 MPa (prática Cartesian) | 📋 + 📊 |
| Aço | CA-50 e CA-60 | 📋 Memorial |
| Prazo de execução | 36 meses | 📊 Cartesian (memorial não declara) |
| CUB referência | R$ 3.028,45 (Mar/26) | 📊 Sinduscon-SC |

---

## Macrogrupo 1 — Gerenciamento Técnico e Administrativo

| Item | Premissa adotada | Fonte |
|---|---|---|
| Prazo 36 meses | Cartesian (memorial não declara; 36m é mediana pra torres 24 pav.) | 📊 |
| Engenheiro PJ | R$ 8.000/mês | 📊 Cartesian — padrão médio (v00) |
| Mestre de obras | R$ 7.000/mês | 📊 Cartesian — padrão médio (v00) |
| Encarregado | R$ 4.000/mês | 📊 Cartesian — padrão médio (v00) |
| ~~Estagiário~~ | **NÃO INCLUSO** | Decisão projeto (v00) |
| ~~Técnico de segurança~~ | **NÃO INCLUSO** | Decisão projeto (v00) |
| Almoxarife | R$ 3.377/mês | 📊 Mediana Cartesian (n=4) |
| Vigilância | R$ 5.000/mês (verba) | 📊 Cartesian — verba reduzida (v00) |
| Limpeza obra (2) | R$ 2.500/mês cada | 📊 Cartesian |
| EPI | R$ 908/mês | 📊 Mediana Cartesian (n=8) |
| Placas de obra | 📋 Memorial declara | 📋 |
| Canteiro + containers + instalações provisórias | Cartesian (memorial não dimensiona) | 📊 |
| Cremalheira + minigrua | Cartesian (memorial não declara) | 📊 |
| Projetos + consultorias (ATP, compat., BIM) | Cartesian | 📊 |
| Taxas + seguros + ensaios + meio ambiente | Cartesian | 📊 |

## Macrogrupo 2 — Movimentação de Terra

| Item | Premissa adotada | Fonte |
|---|---|---|
| Escavação para fundações | 📋 Memorial item 2 | 📋 |
| PU R$ 15/m² AC | Cartesian — **sem subsolo** (memorial) | 📊 |
| ❌ Contenção, escoramento de subsolo, bota-fora profundo | **NÃO APLICÁVEL** — memorial confirma ausência de subsolo | 📋 |

## Macrogrupo 3 — Infraestrutura

| Item | Premissa adotada | Fonte |
|---|---|---|
| Fundação hélice contínua Ø40cm | 📋 Memorial 4.1 | 📋 |
| 190 estacas × 20m médio | 🏗️ Estimado do projeto + norma NBR 6122 | 🏗️ |
| PU R$ 82/m perfuração | 📊 Base Cartesian (n=6) | 📊 |
| PU R$ 632/m³ concreto estaca | 📊 Base Cartesian (n=6) | 📊 |
| Aço fundação R$ 8,77/kg | 📊 Base Cartesian (n=7) | 📊 |
| ❌ Contenção de subsolo | **ZERADO** — memorial: sem subsolo | 📋 |

## Macrogrupo 4 — Supraestrutura

| Item | Premissa adotada | Fonte |
|---|---|---|
| Sistema concreto armado | 📋 Memorial 4.2 | 📋 |
| Laje tipo "mista" (memorial) → premissa **maciça convencional** | 📋 + 📊 |
| fck 30 MPa | 📋 Memorial mínimo 20 + 📊 Cartesian prática moderna | 📋 + 📊 |
| Aço CA-50 | 📋 Memorial 4.2 | 📋 |
| Formas compensado plastif. | 📋 Memorial (pinho/naval 17mm) + 📊 prática atual (plastif. 18mm) | 📋 + 📊 |
| Índice concreto 0,25 m³/m² AC | 📊 Mediana base Cartesian (n=64) | 📊 |
| Índice aço 106 kg/m² AC | 📊 Mediana base Cartesian (n=65) | 📊 |
| Índice forma 7,12 m²/m² AC | 📊 Mediana base Cartesian (n=69) | 📊 |
| PU concreto R$ 590/m³ (fck30) | 📊 Base Cartesian P75 (n=6) | 📊 |
| PU aço R$ 8,67/kg | 📊 Mediana base (n=12) | 📊 |
| PU forma R$ 88/m² | 📊 Entre mediana e P75 base (n=17) | 📊 |
| MO estrutura empreitada R$ 185/m² AC | 📊 Mediana base (n=15) | 📊 |
| Escoramento metálico R$ 20/m² | 📊 Base Cartesian — laje maciça | 📊 |

## Macrogrupo 5 — Alvenaria

| Item | Premissa adotada | Fonte |
|---|---|---|
| **Tijolo furado (bloco cerâmico 14cm)** em TODAS as vedações | 📋 Memorial 4.3 | 📋 |
| Encunhamento c/ argamassa aditivo expansor | 📋 Memorial 4.3 | 📋 |
| Vergas e contravergas em concreto armado | 📋 Memorial 4.3 | 📋 |
| Escada enclausurada em bloco de concreto celular | 📋 Memorial 4.3 | 📋 |
| PU bloco cerâmico R$ 32,95/m² | 📊 Cartesian (bloco + MO separada) | 📊 |
| PU argamassa R$ 3,80/m² | 📊 Cartesian | 📊 |
| PU MO alvenaria R$ 28,50/m² | 📊 Split 35,7% Cartesian | 📊 |
| ❌ Drywall ST/RU | **REMOVIDO** — memorial não especifica drywall | 📋 |

## Macrogrupo 6 — Impermeabilização

| Item | Premissa adotada | Fonte |
|---|---|---|
| Manta asfáltica 4mm + argamassa polimérica | 📋 Memorial 4.5 (normas vigentes + cada ambiente) | 📋 |
| BWCs, terraços, sacadas, caixa d'água, lajes, piscinas, forro casa de máquinas | 📋 Memorial 4.5 | 📋 |
| **Vigas de fundação** (memorial explicitamente) | 📋 Memorial 4.5 | 📋 |
| Índice impermeab. 0,30 m²/m² AC | 📊 Base Cartesian **sem subsolo** (reduzido de 0,45) | 📊 + 📋 |
| PU manta R$ 82,11/m² | 📊 Mediana Cartesian | 📊 |
| PU MO imperm. R$ 68/m² + regulariz. R$ 19,50/m² | 📊 Split 56,5% Cartesian | 📊 |
| ❌ Impermeab. de piso enterrado de subsolo | **REMOVIDO** — memorial: sem subsolo | 📋 |

## Macrogrupo 7 — Instalações

| Item | Premissa adotada | Fonte |
|---|---|---|
| Água fria, quente, esgoto, pluvial em PVC Tigre/Amanco | 📋 Memorial 8.4 | 📋 |
| Captação água da chuva + cisterna | 📋 Memorial 8.4 | 📋 |
| Medidor individual de água por apto | 📋 Memorial 8.4 | 📋 |
| 12 pontos água fria/quente (cozinha + BWCs + A.S.) | 📋 Memorial 8.4.1 | 📋 |
| Gás GLP com central no térreo | 📋 Memorial 8.1 + 8.2 | 📋 |
| Sistema preventivo (extintores + hidrantes + alarme + iluminação) | 📋 Memorial 8.5 | 📋 |
| Elétrica com condutores Pirelli/Conduspar + Tramontina/Pial | 📋 Memorial 8.6 | 📋 |
| Pontos ar-condicionado split (dreno+eletro) em suítes+sala | 📋 Memorial 8.3 | 📋 |
| Sensor de presença em áreas comuns | 📋 Memorial 8.7 | 📋 |
| Índice elétrica 1,77 m/m² × fator tipologia 1,15 | 📊 Mediana Cartesian | 📊 |
| Índice hidro 1,08 m/m² × fator BWC 1,15 | 📊 Mediana Cartesian | 📊 |
| PUs elétrica/hidro/PPCI/gás/telecom | 📊 Cartesian | 📊 |

## Macrogrupo 8 — Sistemas Especiais

| Item | Premissa adotada | Fonte |
|---|---|---|
| 2 elevadores (1 social + 1 serviço/emergência) p/ 8 pessoas | 📋 Memorial 8.8 | 📋 |
| Marca Atlas/Thyssen/Otis/Boxtop/Lgtech ou equivalente | 📋 Memorial 8.8 | 📋 |
| PU elevador social R$ 260.000 | 📊 Entre P25 e mediana Cartesian (n=7) | 📊 |
| PU elevador serviço R$ 250.000 | 📊 Entre P25 e mediana Cartesian (n=4) | 📊 |
| Gerador dedicado R$ 180.000 | 📊 Cartesian (memorial não declara) | 📊 |
| **Piscina adulto + piscina infantil + ofurô** no Rooftop | 📋 Memorial (18º Pavto Rooftop) | 📋 |
| PU piscinas R$ 220.000 | 📊 Cartesian — memorial confirma | 📊 |
| SPDA (para-raios) | 📋 Memorial 8.5 | 📋 |
| CFTV + interfonia + automação + bombas + quadros | 📊 Cartesian (memorial não detalha) | 📊 |

## Macrogrupo 9 — Climatização

| Item | Premissa adotada | Fonte |
|---|---|---|
| Só infraestrutura (dreno + eletroduto + recuo drywall) | 📋 Memorial 8.3 — entrega só infra | 📋 |
| ❌ Aparelhos splits dentro dos aptos | **REMOVIDO** — memorial 12: "Aparelhos de ar condicionados" não fornecidos | 📋 |
| Exaustão mecânica BWCs enclausurados | 📊 Cartesian (memorial implícito no projeto) | 📊 |
| Exaustão churrasqueiras sacadas | 📋 Memorial (sacada com churrasq.) + 📊 Cartesian |
| Infra AR geral R$ 10/m² AC | 📊 Cartesian | 📊 |

## Macrogrupo 10 — Revestimentos Internos de Parede

| Item | Premissa adotada | Fonte |
|---|---|---|
| Reboco massa única R$ 7/m² + chapisco R$ 5,50 | 📊 Cartesian | 📊 |
| **Azulejo 30×45 em BWCs** (não 30×60) | 📋 Memorial 5.3 + 6.3.2 | 📋 |
| PU azulejo R$ 38/m² | 📊 Cartesian (30×45 é mais barato que 30×60) | 📊 |
| Azulejo cozinha **só parede molhada** (não toda) | 📋 Memorial 6.4.2 | 📋 |
| Azulejo área de serviço só parede molhada | 📋 Memorial 6.5.2 | 📋 |
| Sala/suítes/circulação: **pintura PVA sobre acrílica** (sem cerâmica) | 📋 Memorial 6.1.2 + 6.2.2 | 📋 |
| Porcelanato áreas comuns (halls edifício) R$ 85/m² | 📊 Cartesian (memorial 7.1.1) | 📊 |
| ❌ **Granito em bancadas** | **REMOVIDO** — memorial 12: "Bancadas de granito" não fornecidas pelo cliente | 📋 |

## Macrogrupo 11 — Revestimentos e Acabamentos em Teto

| Item | Premissa adotada | Fonte |
|---|---|---|
| Forro gesso acartonado liso (sem moldura, negativo no perímetro) | 📋 Memorial 6.1.3 a 6.6.3 (todas áreas privativas) | 📋 |
| Forro RU em BWCs e áreas molhadas | 📊 Cartesian (memorial não especifica RU, mas é prática) | 📊 |
| Teto estacionamento/comuns: reboco + pintura acrílica (sem forro) | 📋 Memorial 7.1.3 + 7.3.4 | 📋 |
| PU forro ST R$ 28/m² + RU R$ 35/m² | 📊 Mediana Cartesian | 📊 |

## Macrogrupo 12 — Pisos e Pavimentações

| Item | Premissa adotada | Fonte |
|---|---|---|
| **Sala/circulação: porcelanato 60×60 Portobello/Eliane** | 📋 Memorial 6.1.1 | 📋 |
| **Suítes: piso LAMINADO** Eucafloor/Durafloor/Duratex | 📋 Memorial 5.1.3 + 6.2.1 | 📋 |
| **BWCs/Cozinha/A.S./Lavabos: porcelanato 60×60** | 📋 Memorial 6.3.1 a 6.6.1 | 📋 |
| PU porcelanato R$ 81/m² | 📊 Mediana Cartesian (n=60) | 📊 |
| PU laminado R$ 65/m² | 📊 Mediana Cartesian | 📊 |
| PU médio ponderado R$ 73/m² (mix de suítes+demais) | 📊 Calculado com base no memorial | 📊 |
| **Estacionamento: cimento alisado** | 📋 Memorial 7.3.1 | 📋 |
| Halls comuns: granito polido/flameado (Andorinha/Ubatuba/Samoa) | 📋 Memorial 5.1.1 | 📋 |
| Contrapiso autonivelante | 📊 Cartesian (memorial não detalha) | 📊 |
| Rodapé poliestireno/madeira/cerâmica | 📋 Memorial 6.1.4, 6.2.4 etc | 📋 |

## Macrogrupo 13 — Pintura Interna

| Item | Premissa adotada | Fonte |
|---|---|---|
| Paredes privativas: **pintura PVA sobre acrílica** (Suvinil/Coral) | 📋 Memorial 5.4 + 6.x | 📋 |
| Tetos: acrílica | 📋 Memorial 7.1.3 | 📋 |
| Estacionamento/escadaria: textura ou pintura látex | 📋 Memorial 7.3 + 7.6.3 | 📋 |
| PU acrílica R$ 5,40/m² + PVA R$ 4,29/m² + selador R$ 2,50 | 📊 Cartesian | 📊 |
| MO pintura R$ 15/m² + lixamento R$ 8/m² | 📊 Cartesian split 66,2% | 📊 |

## Macrogrupo 14 — Esquadrias, Vidros e Ferragens

| Item | Premissa adotada | Fonte |
|---|---|---|
| **Janelas alumínio com pintura eletrostática preta** | 📋 Memorial 5.7 | 📋 |
| **Soleiras em granito** | 📋 Memorial 5.7 | 📋 |
| **Guarda-corpo sacadas: alvenaria + esquadria alumínio envidraçada** | 📋 Memorial 5.7.1 | 📋 |
| **Portas apartamentos: folhas laminadas semi-ocas brancas** | 📋 Memorial 5.6 | 📋 |
| **Ferragens zamac Papaiz/Arouca/Pado** | 📋 Memorial 5.9 | 📋 |
| PU esquadrias R$ 280/m² AC × padrão × entrega | 📊 Cartesian | 📊 |
| PU serralheria R$ 45/m² AC × fator padrão | 📊 Cartesian (corrimãos + portões + grades técnicas) | 📊 |

## Macrogrupo 15 — Louças e Metais

**⚠️ ESCOPO MUITO REDUZIDO por determinação do memorial** (item 12):

| Item | Incluso? | Fonte |
|---|:---:|---|
| **Bacias sanitárias com caixa acoplada** Deca/Incepa/Celite | ✅ SIM | 📋 Memorial 5.5 + 6.3.4 |
| Lavatórios (cubas e pias) | ❌ NÃO | 📋 Memorial 12 |
| **Bancadas de granito** | ❌ NÃO | 📋 Memorial 12 |
| Torneiras | ❌ NÃO | 📋 Memorial 12 |
| Chuveiros (duchas e elétricos) | ❌ NÃO | 📋 Memorial 12 |
| Acabamentos hidráulicos (metais sanitários) | ❌ NÃO | 📋 Memorial 12 |
| Assentos sanitários | ❌ NÃO | 📋 Memorial 12 |
| Box dos banheiros | ❌ NÃO | 📋 Memorial 12 |
| Luminárias | ❌ NÃO | 📋 Memorial 12 |
| Tanques de roupa | ❌ NÃO | 📋 Memorial 12 |
| Aparelhos de ar condicionados | ❌ NÃO | 📋 Memorial 12 |
| Olho mágico / mobílias | ❌ NÃO | 📋 Memorial 12 |

**Escopo Louças e Metais v00:** **só bacias sanitárias**.
- 3 bacias/apto × 98 aptos = **294 bacias**
- PU R$ 650 (bacia Deca/Incepa com caixa acoplada + MO de instalação)
- Total: **R$ 191.100 (R$ 15/m² AC)**

## Macrogrupo 16 — Fachada

| Item | Premissa adotada | Fonte |
|---|---|---|
| **Tinta premium acrílica com 2 a 4 cores + texturas** | 📋 Memorial 9.1 | 📋 |
| **Muros: tinta premium acrílica lisa ou textura** | 📋 Memorial 9.2 | 📋 |
| PU material textura R$ 50/m² | 📊 Cartesian (textura projetada acrílica premium) | 📊 |
| PU MO textura R$ 30/m² | 📊 Cartesian | 📊 |
| PU balancim R$ 18/m² | 📊 Cartesian | 📊 |
| Índice fachada/AC 1,55 m²/m² | 📊 Cartesian (torre vertical de 24 pav.) | 📊 |
| ❌ Cerâmica de fachada | **REMOVIDO** — memorial especifica textura premium | 📋 |

## Macrogrupo 17 — Serviços Complementares

| Item | Premissa adotada | Fonte |
|---|---|---|
| **Central de lixo** (piso cerâmico, paredes azulejadas até o teto, portas venezianas alumínio) | 📋 Memorial 7.4 | 📋 |
| **Central de gás** (piso cerâmico antiderrapante, portas venezianas alumínio) | 📋 Memorial 7.5 | 📋 |
| **Caixas d'água fibra de vidro** Fortlev/Bakof | 📋 Memorial 7.6 | 📋 |
| **Cobertura: laje impermeabilizada OU telha fibrocimento 6mm** (madeira de lei ou metálica) | 📋 Memorial 4.6 + 7.7 | 📋 |
| **Rooftop 18º Pavto** (sala jogos + coworking + kids + 2 gourmets + ofurô + 2 piscinas + academia + 2 lavabos) | 📋 Memorial (18º Pavto) | 📋 |
| Paisagismo | 📊 Cartesian (memorial não detalha) | 📊 |
| Mobiliário áreas comuns | 📊 Cartesian | 📊 |
| Comunicação visual + limpeza final + ligações definitivas | 📊 Cartesian | 📊 |
| **Pintura de muros premium acrílica** | 📋 Memorial 9.2 | 📋 |
| Pavimentação externa + desmobilização | 📊 Cartesian | 📊 |

## Macrogrupo 18 — Imprevistos e Contingências

| Item | Premissa adotada | Fonte |
|---|---|---|
| Percentual 1,5% sobre subtotal | 📊 Cartesian — padrão para paramétrico | 📊 |

---

## Resumo da origem das premissas

| Classificação | Quantidade de itens | Observação |
|---|:---:|---|
| 📋 **[MEMORIAL]** — declarado pelo cliente | ~55 itens | Define acabamentos, sistemas, marcas |
| 📊 **[CARTESIAN]** — estimativa Cartesian | ~45 itens | PUs, mão-de-obra, índices físicos, gerenciamento |
| 🏗️ **[PROJETO]** — projetos DWG/PDF | ~5 itens | Dimensões estruturais confirmadas |
| 📋 + 📊 — híbrido | ~10 itens | Memorial declara tipo, Cartesian estima PU |

**Áreas onde o memorial é omisso e dependemos 100% de média de mercado Cartesian:**
- Prazo de execução (36 meses — padrão Cartesian pra torre 24 pav.)
- Gerenciamento: todos os PUs de equipe técnica, vigilância, EPI, consumos
- Sistemas Especiais: CFTV, interfonia, automação, bombas, quadros de comando
- PUs materiais de concreto, aço, forma (memorial dá fck mínimo e material mas não PU)
- Índices físicos (m²/m² AC, kg/m² AC, m³/m² AC) — base 126 obras Cartesian
- Percentual de imprevistos (1,5% padrão Cartesian)

**Áreas onde o memorial é CLARO e foi seguido rigorosamente:**
- Alvenaria em bloco cerâmico (sem drywall)
- Fachada em textura premium acrílica (sem cerâmica)
- Pisos: porcelanato 60×60 + laminado em suítes
- Paredes: pintura PVA+acrílica nas áreas secas, azulejo 30×45 só em molhadas
- Sem subsolo (mov. terra, contenção, impermeab. piso enterrado zerados)
- Louças: SÓ bacias sanitárias (sem cubas, bancadas, metais, box, luminárias, ar)
- Elevadores: 2 unidades, marcas específicas

**Este documento acompanha o paramétrico v00 como transparência ao cliente.**
