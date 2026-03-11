# Base de Conhecimento Paramétrica — Cartesian Engenharia

> Objetivo: Acumular índices, preços unitários e regras de negócio de múltiplos orçamentos paramétricos para gerar estimativas no nível da equipe.
> Última atualização: 07/03/2026 (5 projetos com seções detalhadas neste arquivo — projetos 49-53)
> Calibração completa: ver `calibration-data.json` (58 projetos) e `indices/*.md` (65 projetos indexados)
> PUs detalhados dos projetos 12-25: `archive/PUs-NOVOS-PROJETOS.md`
> **Último projeto adicionado:** **Malta Residence** (Nova Empreendimentos) — **7.964 m²** (AC), **CUB 1,28** (direto), Florianópolis/SC, **35 meses**, **2 elevadores sociais**. **DESTAQUES:** **Estrutura de custos separada** — ADM incorporadora R$ 18,26M (terreno + comissões) não entra na calibração. **Rev. Int. Parede R$ 414/m² (10,91%) = 180% acima mediana** — inclui fachada. **Fachada R$ 26/m² (0,68%) = 83% abaixo mediana** — subdivisão diferente do executivo. **Gerenciamento R$ 127/m² (3,34%) = 73% abaixo mediana** — só canteiro físico (projetos/equipe na ADM). **Impermeabilização R$ 126/m² (3,31%) = 78% acima mediana**. **MOE separado** R$ 9,67M (31,98% dos custos diretos). Laje treliçada TR8/TR16 + maciça. Fundação: HC + estaca raiz + blocos. Contenção: estaca raiz 31cm + cortinas. Data-base ago/2025. Índices completos: `orcamento-parametrico/malta-indices.md`.

> **Projeto anterior:** **Suíça Home** (NM Empreendimentos) — **1.541 m²** (AC EXPLÍCITO), **CUB 1,21**, Navegantes/SC, **~8-10 UR**, **~7-8 pavimentos**, **18 meses** (prazo mais curto da base). **🔴 MENOR PROJETO DA BASE** — substitui Botânico (3.123 m²) como menor AC por >50%. **DESTAQUES:** **Impermeabilização R$ 128/m² (3,98%) = 2× benchmark** (R$ 40-60). **Gerenciamento R$ 508/m² (15,78%)** = alto por efeito escala. **Fachada R$ 188/m² (5,83%)** = acima benchmark (R$ 90-140). **Fundação SAPATAS** = único ou raríssimo na base (maioria usa hélice/estacas). **ETE própria** (fossa séptica + filtro anaeróbio). **Laje treliçada com EPS**, concreto fck 30 MPa. Esquadrias alumínio Suprema + **PVC preto** (diferenciador). Data-base jan/2023. Sem Climatização/Louças/Imprevistos separados. **Ritmo construção: 86 m²/mês** (AC pequeno + prazo curto). Índices completos: `orcamento-parametrico/suica-home-indices.md`.


---



---

## PROJETO 53: Malta Residence (Nova Empreendimentos)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Incorporador | — | Nova Empreendimentos | — |
| Localização | — | Florianópolis/SC | — |
| Área Construída | AC | **7.964,40** | m² |
| Área do Terreno | AT | **1.182,72** | m² |
| Unidades Habitacionais | UR | N/D | un |
| Prazo | — | **~35** | meses |
| Elevadores | ELEV | **2** | un (sociais) |
| Data-base | — | **Agosto/2025** | — |
| CUB na data-base | — | R$ 2.978,02 | R$ |
| **Total Direto (MAT+MOE)** | — | **R$ 30.252.288,33** | R$ |
| **Total com ADM** | — | **R$ 48.511.644,80** | R$ |
| R$/m² Direto | — | **R$ 3.798,44** | R$/m² |
| R$/m² Total | — | **R$ 6.091,06** | R$/m² |
| **CUB ratio Direto** | — | **1,28** | CUB |
| **CUB ratio Total** | — | **2,05** | CUB |

### Custos por Macrogrupo — Malta (R$ — Ago/2025, custos diretos apenas)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| **🔴 Supraestrutura** | **6.806.830** | **854,66** | **22,50%** |
| **🔴 Rev. Int. Parede** | **3.300.702** | **414,43** | **10,91%** |
| **🔴 Esquadrias** | **3.292.806** | **413,44** | **10,88%** |
| Instalações | 3.184.558 | 399,85 | 10,53% |
| Infraestrutura | 2.580.123 | 323,96 | 8,53% |
| Alvenaria | 1.774.389 | 222,79 | 5,87% |
| Pisos | 1.626.850 | 204,27 | 5,38% |
| Complementares | 1.576.422 | 197,93 | 5,21% |
| Gerenciamento | 1.011.755 | 127,03 | 3,34% |
| **🔴 Impermeabilização** | **1.002.774** | **125,91** | **3,31%** |
| Pintura | 994.560 | 124,88 | 3,29% |
| Climatização | 648.665 | 81,45 | 2,14% |
| Teto | 603.139 | 75,73 | 1,99% |
| Sist. Especiais | 586.984 | 73,70 | 1,94% |
| Mov. Terra | 548.051 | 68,81 | 1,81% |
| Imprevistos | 280.513 | 35,22 | 0,93% |
| Louças e Metais | 228.397 | 28,68 | 0,75% |
| **🔴 Fachada** | **204.770** | **25,71** | **0,68%** |

**Validação:** Soma dos 18 macrogrupos = R$ 30.252.288 ✓

**⚠️ ADM Incorporadora (NÃO entra na calibração):** R$ 18.259.356,47
- Aquisição do Terreno: R$ 7.736.011
- Comissões + Taxas + Laudos: R$ 10.523.345

### Normalização CUB Base (dez/2023)

| Métrica | Original (ago/25) | Normalizado (dez/23) |
|---|---|---|
| CUB de referência | R$ 2.978,02 | R$ 2.752,67 |
| Fator de atualização | — | **0,9243** |
| R$/m² Direto | R$ 3.798,44 | **R$ 3.510,82** |

**Macrogrupos normalizados (destaque anomalias):**
- **Supraestrutura:** R$ 854,66 × 0,9243 = **R$ 789,98/m²** — 11% acima mediana (R$ 709,64) ✅
- **Rev. Int. Parede:** R$ 414,43 × 0,9243 = **R$ 383,07/m²** — **180% acima mediana** (R$ 136,95) 🔴
- **Esquadrias:** R$ 413,44 × 0,9243 = **R$ 382,16/m²** — 36% acima mediana (R$ 282,08) ⚠️
- **Impermeabilização:** R$ 125,91 × 0,9243 = **R$ 116,38/m²** — 78% acima mediana (R$ 65,31) 🔴
- **Gerenciamento:** R$ 127,03 × 0,9243 = **R$ 117,42/m²** — **73% abaixo mediana** (R$ 435,10) 🔴
- **Fachada:** R$ 25,71 × 0,9243 = **R$ 23,77/m²** — **83% abaixo mediana** (R$ 138,51) 🔴

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| R$/UR | N/D | R$/UR |
| AC/UR | N/D | m²/un |
| Ritmo construção | **~227** | m²/mês |
| Burn rate (direto) | **R$ 864k** | R$/mês |
| Burn rate (total) | **R$ 1,39M** | R$/mês |
| Custo/mês/m² (direto) | **~109** | R$/m²/mês |

### Destaques Técnicos

**🔴 ESTRUTURA DE CUSTOS SEPARADA:**
- **ADM Incorporadora:** R$ 18,26M (37,64% do total) — terreno + comissões + taxas
- **Custos Diretos:** R$ 30,25M (62,36%) — obra pura
- **MOE Separado:** R$ 9,67M (31,98% dos custos diretos) — aba "3 - MOE"
- **Metodologia:** MAT + MOE somados por célula construtiva

**🔴 REV. INT. PAREDE R$ 414/m² (10,91%) — 180% ACIMA MEDIANA:**
- **Possível causa:** Revestimento de fachada classificado em "Revestimentos de Argamassa"
- MOE = 2,98× MAT (R$ 2.471k vs R$ 830k) — MOE separado inflou o valor
- Valor normalizado: R$ 383/m² = **2,8× mediana** (R$ 136,95)

**🔴 FACHADA R$ 26/m² (0,68%) — 83% ABAIXO MEDIANA:**
- **Explicação:** Subdivisão diferente do executivo
- Chapisco + reboco externo → "Revestimentos de Argamassa" (R$ 414/m²)
- "Acabamentos em Fachada" → só MOE de pintura/acabamento final (R$ 205k)
- **Regra:** Ao usar Malta como referência, somar Rev. Int. Parede + Fachada = R$ 440/m² (total real de revestimento)

**🔴 GERENCIAMENTO R$ 127/m² (3,34%) — 73% ABAIXO MEDIANA:**
- **Não comparável:** Executivo separa ADM incorporadora (R$ 18,26M) do canteiro de obra (R$ 1,01M)
- Mediana (R$ 435/m²) inclui projetos + equipe + taxas
- Malta R$ 127/m² = apenas canteiro físico (equipamentos, consumíveis, segurança)
- **Regra:** Não usar Malta como referência para Gerenciamento — estrutura de custos diferente

**🔴 IMPERMEABILIZAÇÃO R$ 126/m² (3,31%) — 78% ACIMA MEDIANA:**
- Valor normalizado: R$ 116/m² vs mediana R$ 65/m²
- Possível causa: áreas molhadas extensas + tratamento laje cobertura/subsolo
- Valor absoluto alto: R$ 1.002.774

**⚠️ ESQUADRIAS R$ 413/m² (10,88%) — 36% ACIMA MEDIANA:**
- Valor normalizado: R$ 382/m² vs mediana R$ 282/m²
- Possível causa: padrão de esquadrias alto ou grande área envidraçada
- Valor absoluto: R$ 3.292.806 (10,88% dos custos diretos)

**🟢 INFRAESTRUTURA R$ 324/m² (8,53%):**
- Fundação: Hélice contínua + Estaca raiz + Blocos
- Contenção: Estaca raiz 31cm + Cortinas
- Valor normalizado: R$ 299/m² vs mediana R$ 197/m² (+52%)

**🟢 LAJE MISTA:**
- Treliçada TR8/TR16 + Maciça
- Não há breakdown de volumes (executivo não detalha m³/elemento)

**🟢 INSTALAÇÕES R$ 400/m² (10,53%):**
- Agrupado: Hidro + Elétr + Telecom + Gás
- Hidro = 48,74% | Elétr = 42,19% | Telecom = 7,38% | Gás = 1,69%
- Valor normalizado: R$ 370/m² vs mediana R$ 356/m² (+4%)

### Lições para Calibração

1. **Revestimento de parede + Fachada:** Somar os dois ao usar Malta como referência (R$ 440/m² total)
2. **Gerenciamento:** Não usar Malta — estrutura de custos diferente (canteiro isolado)
3. **MOE separado:** Verificar se outros executivos também separam MOE — pode inflar Rev. Int. Parede
4. **ADM Incorporadora:** SEMPRE separar do custo direto de obra (não entra na calibração)
5. **Impermeabilização alta:** Justificada se áreas molhadas extensas ou tratamento especial

### Arquivos Relacionados

- **Índices completos:** `orcamento-parametrico/malta-indices.md`
- **XLSX:** `~/.openclaw/media/inbound/43278b5e-388b-4458-8769-3182ed21cc8f.xlsx`
- **PDF:** `~/.openclaw/media/inbound/c8708bf8-e8f4-4e71-836d-77f68e01866a.pdf`


## PROJETO 52: Suíça Home (NM Empreendimentos)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Incorporador | — | NM Empreendimentos | — |
| Localização | — | Navegantes/SC | — |
| Área Construída | AC | **1.540,93** | m² |
| Unidades Habitacionais | UR_H | ~8-10 | un |
| Total Unidades | UR | ~8-10 | un |
| AC/UR | — | **~150-190** | m²/un |
| Prazo | — | **18** | meses |
| Nº Pavimentos | NP | **~7-8** | pav |
| Elevadores | ELEV | **1** | un |
| Torres | — | **1** | — |
| Data-base | — | **Jan/2023** | — |
| CUB na data-base | — | R$ 2.651,17 | R$ |
| Total | — | **R$ 4.958.343,62** | R$ |
| R$/m² | — | **R$ 3.217,76** | R$/m² |
| **CUB ratio** | — | **1,214** | CUB |

### Custos por Macrogrupo — Suíça Home (R$ — Jan/2023)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| **🔴 Gerenciamento** | **782.447** | **507,78** | **15,78%** |
| **🔴 Supraestrutura** | **927.189** | **601,71** | **18,70%** |
| Instalações | 495.318 | 321,44 | 10,00% |
| Esquadrias | 415.399 | 269,58 | 8,38% |
| Rev. Int. Parede | 296.666 | 192,52 | 5,98% |
| Fachada | 289.013 | **187,56** | 5,83% |
| Pisos | 288.829 | 187,44 | 5,83% |
| Pintura | 208.758 | 135,48 | 4,21% |
| Alvenaria | 198.208 | 128,63 | 4,00% |
| **🔴 Impermeabilização** | **197.304** | **128,04** | **3,98%** |
| Sist. Especiais | 272.857 | 177,07 | 5,50% |
| Complementares | 170.557 | 110,69 | 3,41% |
| Teto | 101.919 | 66,14 | 2,06% |
| Mov. Terra | 42.400 | 27,52 | 0,86% |
| Climatização | 0 | 0 | 0% |
| Louças e Metais | 0 | 0 | 0% |
| Imprevistos | 0 | 0 | 0% |
| Infraestrutura | 271.480 | 176,18 | 5,48% |

**Validação:** Soma dos 18 macrogrupos = R$ 4.958.344 ✓

### Normalização CUB Base (dez/2023)

| Métrica | Original (jan/23) | Normalizado (dez/23) |
|---|---|---|
| CUB de referência | R$ 2.651,17 | R$ 2.752,67 |
| Fator de atualização | — | **1,0383** |
| R$/m² | R$ 3.217,76 | **R$ 3.340,95** |

**Macrogrupos normalizados:**
- **Gerenciamento:** R$ 507,78 × 1,0383 = **R$ 527,12/m²** — 21% acima mediana (R$ 435,10)
- **Impermeabilização:** R$ 128,04 × 1,0383 = **R$ 132,93/m²** — **104% acima mediana** (R$ 65,31) 🔴
- **Fachada:** R$ 187,56 × 1,0383 = **R$ 194,74/m²** — 50% acima mediana (R$ 129,47)
- **Supraestrutura:** R$ 601,71 × 1,0383 = **R$ 624,61/m²** — 12% abaixo mediana (R$ 709,64)

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| R$/UR | **R$ 495-620k** | R$/UR (estimado) |
| AC/UR | **~150-190** | m²/un |
| Ritmo construção | **~86** | m²/mês |
| Burn rate | **R$ 275k** | R$/mês |
| Custo/mês/m² | **~179** | R$/m²/mês |
| Meses por pavimento | **~2,3-2,6** | meses/pav |
| UR por mês | **~0,4-0,6** | un/mês |

### Destaques Técnicos

**🔴 MENOR PROJETO DA BASE:**
- AC 1.541 m² — 50% menor que Botânico (3.123 m²)
- Total R$ 5M — menor valor absoluto da base
- 18 meses — **prazo mais curto da base**

**🔴 IMPERMEABILIZAÇÃO R$ 128/m² (3,98%):**
- **2× acima do benchmark** do próprio executivo (R$ 40-60)
- Normalizado: R$ 133/m² = **104% acima mediana**
- Manta asfáltica generalizada
- Segundo mais alto da base em %

**🔴 FACHADA R$ 188/m² (5,83%):**
- Acima benchmark (R$ 90-140)
- **Cerâmica 7×26 + granito preto São Gabriel** = custo alto pra escala pequena
- Normalizado: R$ 195/m² = **50% acima mediana**

**🟡 EFEITO ESCALA (similar ao Botânico):**
- **Gerenciamento 15,8% (R$ 508/m²)** — alto por escala
- Normalizado: R$ 527/m² = 21% acima mediana
- Benchmark interno: R$ 350-420 → Suíça Home 20-45% acima

**✅ DIFERENCIADORES TÉCNICOS:**
- **Fundação SAPATAS** (fck 30 MPa) — único ou raríssimo na base (maioria usa hélice contínua/estacas)
- **ETE própria:** fossa séptica + filtro anaeróbio + caixa desinfecção (sem rede coletora)
- **Esquadrias:** Alumínio Suprema + **PVC preto** + portas madeira (PVC preto = diferenciador)
- **Laje treliçada com EPS** (compensado plastificado 17mm, 2 jogos de forma)
- **Concreto fck 30 MPa** em toda estrutura (infra + supra)
- **Andaime fachadeiro locação** (não aquisição)

**📝 AUSÊNCIAS:**
- Climatização: R$ 0 (não há sistema separado)
- Louças e Metais: R$ 0 (embutido em acabamentos ou fornecimento incorporadora)
- Imprevistos: R$ 0 (não previsto separadamente)

### Benchmark Interno (do próprio executivo)

| Macrogrupo | Suíça Home R$/m² | Benchmark R$/m² | Desvio |
|---|---|---|---|
| **Gerenciamento** | **508** | **350-420** | **+20-45%** ⚠️ |
| **Impermeabilização** | **128** | **40-60** | **+113-220%** 🔴 |
| **Fachada** | **188** | **90-140** | **+34-109%** ⚠️ |
| **Esquadrias** | **270** | **300-670** | **-10 a -60%** ✅ |

**Nota:** Benchmark são projetos Canto Grande, Opus Home e GMF (citados no executivo).

### Insights e Conclusões

**1. Efeito Escala Dominante**
- AC 1.541 m² cria **efeito escala** fortíssimo
- Gerenciamento R$ 508/m² vs benchmark R$ 350-420
- Custos indiretos diluídos em área pequena

**2. Impermeabilização Superdimensionada**
- R$ 128/m² = **2× o benchmark**
- Manta asfáltica generalizada
- Região litorânea (Navegantes) exige proteção
- Área pequena = dificuldade de otimizar fornecimento

**3. Fachada Elaborada**
- R$ 188/m² para projeto pequeno
- Cerâmica + granito = custo material alto
- Padrão médio-alto bem acabado
- Fachada não foi simplificada apesar da escala

**4. Fundação Rasa — Diferenciador**
- **Sapatas** (sem estacas) é raríssimo na base
- Solo competente em Navegantes
- Redução significativa de custo de infra
- Fundação R$ 176/m² = moderado (sem custo de perfuração)

**5. ETE Própria**
- Sistema completo de tratamento (fossa + filtro + desinfecção)
- Sem rede coletora municipal
- Custo embutido em Sist. Especiais

**6. CUB Ratio 1,21 — Moderado**
- Apesar do pequeno porte, CUB 1,21 não é extremo
- Base tem projetos 1,4-1,79
- Eficiência construtiva razoável
- Laje treliçada + sapatas ajudam

---

## PROJETO 51: Origem 3300 (Neuhaus Incorporadora)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Incorporador | — | Neuhaus Incorporadora | — |
| Localização | — | Balneário Camboriú/SC | — |
| Endereço | — | Rua 3300, Centro | — |
| Área Construída | AC | **14.559,12** | m² |
| Unidades Habitacionais | UR_H | **43** | un |
| Unidades Comerciais | UR_C | **6** | un |
| Total Unidades | UR | **49** | un |
| AC/UR | — | **297,1** | m²/un |
| Prazo | — | **48** | meses |
| Data-base | — | **Mar/2025** | — |
| CUB na data-base | — | R$ 2.916,12 | R$ |
| Total | — | **R$ 67.590.131,00** | R$ |
| R$/m² | — | **R$ 4.642,46** | R$/m² |
| **CUB ratio** | — | **1,60** | CUB |

### Custos por Macrogrupo — Origem 3300 (R$ — Mar/2025)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| **🔴 Gerenciamento** | **13.723.637** | **942,61** | **20,30%** |
| **🔴 Supraestrutura** | **14.465.388** | **993,56** | **21,40%** |
| **🔴 Esquadrias** | **6.022.410** | **413,65** | **8,91%** |
| Instalações | 4.737.605 | 325,40 | 7,01% |
| Complementares | 3.815.404 | 262,06 | 5,64% |
| Alvenaria | 3.199.967 | 219,79 | 4,73% |
| Infraestrutura | 3.183.719 | 218,68 | 4,71% |
| Sist. Especiais | 3.072.221 | 211,02 | 4,55% |
| Fachada | 2.858.852 | 196,36 | 4,23% |
| Pisos | 2.732.206 | 187,70 | 4,04% |
| **🔴 Pintura** | **2.611.040** | **179,34** | **3,86%** |
| Rev. Int. Parede | 1.868.736 | 128,36 | 2,76% |
| Impermeabilização | 1.381.564 | 94,89 | 2,04% |
| Teto | 1.178.521 | 80,95 | 1,74% |
| Imprevistos | 1.056.205 | 72,55 | 1,56% |
| Louças e Metais | 708.836 | 48,69 | 1,05% |
| Climatização | 639.419 | 43,92 | 0,95% |
| Mov. Terra | 334.392 | 22,97 | 0,49% |

**Validação:** Soma dos 18 macrogrupos = R$ 67.590.131 ✓

### Normalização CUB Base (dez/2023)

| Métrica | Original (mar/25) | Normalizado (dez/23) |
|---|---|---|
| CUB de referência | R$ 2.916,12 | R$ 2.752,67 |
| Fator de atualização | — | **0,9440** |
| R$/m² | R$ 4.642,46 | **R$ 4.382,48** |

**Macrogrupos normalizados:**
- **Gerenciamento:** R$ 942,61 × 0,944 = **R$ 889,83/m²** — 🔴 **RECORDE NORMALIZADO DA BASE**
- **Supraestrutura:** R$ 993,56 × 0,944 = **R$ 937,92/m²** — 🔴 **RECORDE NORMALIZADO DA BASE**
- **Esquadrias:** R$ 413,65 × 0,944 = **R$ 390,48/m²** — 🔴 **RECORDE NORMALIZADO DA BASE**

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| R$/UR (todas) | **R$ 1.379.390** | R$/UR |
| R$/UR (habitacionais) | **R$ 1.571.631** | R$/UR |
| AC/UR | **297,1** | m²/un |
| AC/UR (habitacionais) | **338,6** | m²/un |
| Ritmo construção | **303** | m²/mês |
| Burn rate | **R$ 1,41 M** | R$/mês |
| Custo/mês/m² | **96,7** | R$/m²/mês |
| Meses por pavimento | **1,4** | meses/pav |
| UR por mês | **1,0** | un/mês |

### Estrutura do Empreendimento

**Layout detalhado (áreas por pavimento):**
- Térreo: 994,58 m² (salas comerciais)
- Mezanino: 276,65 m²
- G1-G4: 980,62 m² cada (4 subsolos) = **RECORDE** (empatado)
- Lazer 1: 979,79 m²
- Lazer 2: 320,72 m²
- Tipo Garden: 394,74 m² (1 pav)
- Tipo 18x: 5.797,11 m² (18 pav → 322,06 m²/pav)
- Duplex Inferior 2x: 645,71 m² (2 pav)
- Duplex Superior 2x: 538,06 m² (2 pav)
- Penthouse Inferior: 320,90 m²
- Penthouse Superior: 283,92 m²
- Cobertura: 36,85 m²
- Barrilete/Casa Máquinas: 47,61 m²
- **Total: 14.559,12 m²** ✓

**NPT:** 18 tipos + 1 garden + 2 duplex + 1 penthouse = **22 residenciais**  
**NPG:** 4 (G1 a G4)  
**Subsolos:** 4 (RECORDE — empatado com outros)

### Destaques

1. 🔴 **MÚLTIPLOS RECORDES ABSOLUTOS DA BASE:**
   - **MAIOR valor total:** R$ 67,6M (+2× o segundo maior)
   - **Gerenciamento R$ 943/m²** (20,3%) → Normalizado R$ 890/m² → **142% acima da mediana (R$ 411/m²)**
   - **Supraestrutura R$ 994/m²** (21,4%) → Normalizado R$ 938/m² → **34% acima da mediana (R$ 699/m²)**
   - **Esquadrias R$ 414/m²** (8,9%) → Normalizado R$ 390/m² → **40% acima da mediana (R$ 280/m²)**
   - **Pintura R$ 179/m²** (3,9%) → Normalizado R$ 169/m² → **58% acima da mediana (R$ 113/m²)**
   - **Alvenaria R$ 220/m²** (4,7%) → Normalizado R$ 207/m² → **42% acima da mediana (R$ 155/m²)**

2. 🔵 **CUB RATIO 1,60** — 2º mais alto da base (após Brava Sixteen 1,73). **Justificado:** Balneário Camboriú super luxo, CUB 1,6 é padrão de mercado BC.

3. 🔵 **BALNEÁRIO CAMBORIÚ** — Epicentro super luxo SC. Segundo Neuhaus na base (Botânico: CUB 1,41, R$ 3.622/m²). Primeiro projeto na base com endereço "Rua 3300, Centro" (branding forte).

4. ✅ **POSITIVOS:**
   - AC e UR explícitos (14.559,12 m², 49 UR)
   - **Louças separadas** R$ 49/m² (raro na base — maioria embute)
   - Imprevistos incluídos (1,56%)
   - Climatização separada (R$ 44/m²)
   - EAP granular (18 macrogrupos)
   - Data-base mar/2025 = **projeto mais recente da base**

5. ⚠️ **OUTLIER POR PADRÃO:**
   - Super luxo BC → **não usar como benchmark para obras "normais"**
   - Gerenciamento 20,3% distorce medianas → **considerar excluir de benchmarks de gerenciamento para obras médio/alto padrão**
   - Infra pesada (R$ 3,2M) sem fundação especificada → provável fundação profunda complexa
   - 35 pavimentos (torre alta) + 4 subsolos → complexidade estrutural elevada

6. 📝 **48 MESES** — 2º maior prazo da base (empatado com outros). Ritmo R$ 303 m²/mês alinhado com mediana.

7. 📝 **TIPOLOGIAS MISTAS:** 18 tipos + garden + 2 duplex + penthouse = 22 residenciais + 6 salas comerciais térreo.

8. ⚠️ **SEM DETALHAMENTO QUANTITATIVO:** Orçamento não traz volumes de concreto, áreas de serviço, comprimentos. Apenas valores agregados (R$ e R$/m²).

**Documentação completa:** `orcamento-parametrico/origem-indices.md`




---

## PROJETO 49: Central Park (MZ Empreendimentos)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Incorporador | — | MZ Empreendimentos | — |
| Elaboração | — | **Methodo Engenharia** (predecessor Cartesian) | — |
| Localização | — | Itajaí/SC (provável) | — |
| Área Construída | AC | **8.744,16** | m² |
| Unidades | UR | **34** | un |
| AC/UR | — | **257,2** | m²/un |
| Prazo | — | ~33 | meses |
| Data-base | — | **Ago/2021** | — |
| CUB na data-base | — | R$ 2.307,92 | R$ |
| Total | — | R$ 20.373.276,93 | R$ |
| R$/m² | — | R$ 2.329,93 | R$/m² |
| **CUB ratio** | — | **1,0095** | CUB |

### Custos por Macrogrupo — Central Park (R$ — Ago/2021)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| **🔴 Gerenciamento** | **3.361.698,64** | **384,45** | **16,50%** |
| Supraestrutura | 4.556.478,72 | 521,09 | 22,36% |
| Instalações | 1.943.301,73 | 222,24 | 9,54% |
| Esquadrias | 1.609.984,44 | 184,12 | 7,90% |
| Pisos | 1.460.124,69 | 166,98 | 7,17% |
| Rev. Int. Parede | 1.179.716,88 | 134,91 | 5,79% |
| Sist. Especiais | 1.031.174,54 | 117,93 | 5,06% |
| Pintura | 954.010,89 | 109,10 | 4,68% |
| Complementares | 932.967,37 | 106,70 | 4,58% |
| Alvenaria | 897.319,42 | 102,62 | 4,40% |
| Infraestrutura | 752.144,92 | 86,02 | 3,69% |
| Fachada | 714.232,08 | 81,68 | 3,51% |
| Teto | 588.987,05 | 67,36 | 2,89% |
| Impermeabilização | 295.931,89 | 33,84 | 1,45% |
| Mov. Terra | 95.203,64 | 10,89 | 0,47% |
| Climatização | 0 | 0 | 0% |
| Louças e Metais | 0 | 0 | 0% |
| Imprevistos | 0 | 0 | 0% |

**Validação:** Ger.Técnico (R$ 482k) + Ger.Admin (R$ 2.880k) + Executivo (R$ 17.012k) = R$ 20.373k ✓

### Normalização CUB Base (dez/2023)

| Métrica | Original (ago/21) | Normalizado (dez/23) |
|---|---|---|
| CUB de referência | R$ 2.307,92 | R$ 2.752,67 |
| Fator de atualização | — | **1,1928** |
| R$/m² | R$ 2.329,93 | **R$ 2.779,27** |

**Gerenciamento normalizado:** R$ 384,45 × 1,1928 = **R$ 458,63/m²** — 🔴 **MAIS ALTO DA BASE**

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| R$/UR | R$ 599.214 | R$/UR |
| AC/UR | **257,2** | m²/un |
| Ritmo construção | 265 | m²/mês |
| Burn rate | R$ 617k | R$/mês |
| Custo/mês/m² | 70,6 | R$/m²/mês |

### Destaques

1. 🔴 **GERENCIAMENTO R$ 384/m² (16,5%) — RECORDE DA BASE** — Benchmark interno do próprio executivo indica R$ 300-320/m² para obras similares. **20% acima da faixa superior**. Normalizado para dez/2023: **R$ 459/m²** (mais alto da base calibrada)
2. 🔵 **PROJETO METHODO** — Elaborado quando a empresa ainda se chamava Methodo Engenharia (predecessor da Cartesian, antes do rebranding 2021). BIM arquitetônico feito pela Methodo, quantitativos infra/supra/instalações fornecidos pelo cliente
3. ✅ **CUB RATIO 1,01** — Eficiente, similar ao Brooklyn (1,02) e West Coast (1,02). Projeto bem calibrado
4. ✅ **SUPRAESTRUTURA R$ 521/m²** — Faixa baixa vs projetos similares (Mussi Soho/Velazquez R$ 568-668/m²)
5. ✅ **INFRAESTRUTURA R$ 86/m²** — LOW, mesmo incluindo contenção
6. ⚠️ **APARTAMENTOS GRANDES** — 34 UR com 257 m²/UR. Segundo maior da base (atrás apenas do Serenity com 309 m²/UR). Alto padrão com unidades espaçosas
7. ⚠️ **PINTURA R$ 109/m²** — Acima da mediana (~R$ 95/m²)
8. ⚠️ **CLIMATIZAÇÃO/LOUÇAS/IMPREVISTOS R$ 0** — Não separados (embutidos em outras categorias)
9. 📝 **AC e UR EXPLÍCITOS** — Alta confiabilidade dos dados
10. 📝 **PRAZO 33 MESES** — Razoável para o porte (8.744 m²)

**Documentação completa:** `orcamento-parametrico/central-park-indices.md`


*Costão: R$/m² = R$ 162,9M / 38.429 m² ≈ 4.239 (sem CI segregado)
*Fasolo VDF: R$/m² = R$ 58,4M / 20.550 m² ≈ 2.843 (data-base 2021, valores desatualizados)
*Fasolo ELS e EIS: totais com fórmulas quebradas (#REF!) na planilha

---

## PROJETO 50: Botânico (Neuhaus)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Incorporador | — | Neuhaus | — |
| Localização | — | SC (provável Bal. Piçarras/Penha) | — |
| Área Construída | AC | **3.123,40** | m² |
| Unidades | UR | **20** | un |
| AC/UR | — | **156,2** | m²/un |
| Elevadores | ELEV | **1** | un |
| Torres | — | 1 | — |
| Prazo | — | **29** | meses |
| Data-base | — | **Jul/2022** | — |
| CUB na data-base | — | R$ 2.572,55 | R$ |
| Total | — | R$ 11.315.175,21 | R$ |
| R$/m² | — | R$ 3.622,71 | R$/m² |
| **CUB ratio** | — | **1,408** | CUB |

### Custos por Macrogrupo — Botânico (R$ — Jul/2022)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| **🔴 Supraestrutura** | **2.567.394,33** | **821,99** | **22,69%** |
| **🔴 Gerenciamento** | **2.089.078,17** | **668,85** | **18,46%** |
| Esquadrias | 1.222.124,41 | 391,28 | 10,80% |
| Instalações | 1.120.560,70 | 358,76 | 9,90% |
| **🔴 Infraestrutura** | **920.136,14** | **294,59** | **8,13%** |
| Rev. Int. Parede | 632.400,78 | 202,47 | 5,59% |
| Complementares | 562.649,21 | 180,14 | 4,97% |
| Sist. Especiais | 487.000,00 | 155,92 | 4,30% |
| Pisos | 454.436,44 | 145,49 | 4,02% |
| Alvenaria | 307.538,54 | 98,46 | 2,72% |
| Impermeabilização | 256.448,09 | 82,11 | 2,27% |
| Pintura | 251.314,00 | 80,46 | 2,22% |
| Fachada | 236.645,69 | 75,77 | 2,09% |
| Teto | 147.356,11 | 47,18 | 1,30% |
| Mov. Terra | 60.092,60 | 19,24 | 0,53% |
| Climatização | 0 | 0 | 0% |
| Louças e Metais | 0 | 0 | 0% |
| Imprevistos | 0 | 0 | 0% |

**Validação:** Total = R$ 11.315.175,21 ✓

### Normalização CUB Base (dez/2023)

| Métrica | Original (jul/22) | Normalizado (dez/23) |
|---|---|---|
| CUB de referência | R$ 2.572,55 | R$ 2.752,67 |
| Fator de atualização | — | **1,0700** |
| R$/m² | R$ 3.622,71 | **R$ 3.876,30** |

**Destaques normalização:**
- **Gerenciamento normalizado:** R$ 668,85 × 1,07 = **R$ 715,67/m²** — 🔴 **RECORDE ABSOLUTO DA BASE**
- **Supraestrutura normalizada:** R$ 821,99 × 1,07 = **R$ 879,53/m²** — 🔴 **RECORDE ABSOLUTO DA BASE**
- **Infraestrutura normalizada:** R$ 294,59 × 1,07 = **R$ 315,21/m²** — 🔴 **RECORDE ABSOLUTO DA BASE**
- **Esquadrias normalizadas:** R$ 391,28 × 1,07 = **R$ 418,67/m²** — Top 3 da base

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| **R$/UR** | **R$ 565.758,76** | R$/UR |
| **AC/UR** | **156,2** | m²/un |
| **UR por elevador** | **20** | UR/elev |
| Ritmo construção | 107,7 | m²/mês |
| Burn rate | R$ 390k | R$/mês |
| Custo/mês/m² | 124,9 | R$/m²/mês |

### Destaques

1. 🔴 **MENOR AC DA BASE: 3.123 m²** — Menos da metade do 2º menor projeto. **Efeito escala crítico:** custos fixos não diluem
2. 🔴 **GERENCIAMENTO R$ 669/m² (18,5%) — RECORDE ABSOLUTO** — Benchmark base: R$ 300-450/m² (9-15%). **50% acima do limite superior**. Normalizado: **R$ 716/m²** (mais alto de todos os 50 projetos)
3. 🔴 **SUPRAESTRUTURA R$ 822/m² (22,7%) — RECORDE EM R$/m²** — Compensado plastificado = sistema premium. fck 35 MPa = especificação alta. Normalizado: **R$ 880/m²** (mais alto da base)
4. 🔴 **INFRAESTRUTURA R$ 295/m² (8,1%) — RECORDE** — Hélice contínua em escala pequena = custo unitário alto. Normalizado: **R$ 315/m²** (mais alto da base)
5. 🔴 **ESQUADRIAS R$ 391/m² (10,8%) — TOP 3 DA BASE** — Alumínio + guarda-corpo alumínio/vidro temperado. Normalizado: **R$ 419/m²**
6. 🔴 **CUB RATIO 1,41 — 2º MAIS ALTO DA BASE** — Atrás apenas do Brava Sixteen (1,73). Indica custo elevado vs CUB de referência
7. 🔴 **R$/m² NORMALIZADO R$ 3.876 — 2º MAIS CARO DA BASE** — Atrás apenas do Elleva (R$ 4.540). Reflexo dos múltiplos recordes
8. 🔵 **PROJETO BOUTIQUE** — 20 UR (menor quantidade da base). **1 elevador** (único projeto com apenas 1 elevador). **29 meses** (prazo curto). **Fachada premium:** ACM perfurado + pastilhas cerâmicas = alto padrão
9. ⚠️ **OUTLIER POR ESCALA** — Os R$/m² altos são resultado de **ineficiência de escala**, não de padrão excepcional. **USAR COM CAUTELA como referência:** ✅ Tecnologias e sistemas (forma compensado, fck 35, etc), ✅ Percentuais relativos entre macrogrupos, ⚠️ Valores absolutos R$/m² (distorcidos pela escala)
10. ✅ **CLIMATIZAÇÃO EMBUTIDA** em Sist. Especiais (não separada)
11. ✅ **IMPREVISTOS EMBUTIDOS** em Complementares
12. 📝 **QUANTIFICAÇÃO BIM MDPLAN** (não Cartesian)
13. 📝 **BENCHMARK INCLUI BRAVA GARDEN** como referência de obra similar
14. 📝 **fck 35 MPa** (infraestrutura + supraestrutura) — especificação alta
15. 📝 **FUNDAÇÃO:** Hélice contínua + blocos/baldrames

**Documentação completa:** `orcamento-parametrico/botanico-indices.md`

**Impacto na calibração:**
- **Medianas afetadas:** Gerenciamento (↑2,6%), Supraestrutura (↑1,5%), Infraestrutura (↑0,2%)
- **Benchmark recomendado:** Para projetos >8.000m², usar medianas da base. Para projetos 3.000-5.000m², Botânico é referência válida. Para projetos <3.000m², Botânico pode até subestimar custos (escala ainda menor)

*Exito Oiti: CUB 0,94 artificialmente baixo (infraestrutura e contenções = R$ 0). CUB real estimado: 1,10-1,20 após incluir fundação (R$ 150-300/m²)

### 🔵 TRIO MUSSI COMPLETO (Itajaí/SC) — Análise Comparativa

Com a adição de **Brooklyn**, a base agora contém os **3 projetos Mussi Empreendimentos** em Itajaí/SC — torres altas, laje cubetas EPS, fundação HC, 3 elevadores:

| Projeto | AC (m²) | UR | NP | Prazo | CUB data-base | CUB ratio | R$/m² data-base | R$/m² norm (dez/23) | Diferencial |
|---------|---------|----|----|-------|---------------|-----------|-----------------|---------------------|-------------|
| **Brooklyn** | **13.060** | **85** | **~33** | **46** | **2.470,83 (mai/22)** | **1,009** | **2.493** | **2.778** | **Mais eficiente** |
| Velazquez | ~13.000 | 55 | 34 | 46 | 2.061 (jul/20) | 1,228 | 2.532 | 3.381 | Torre mais alta |
| Soho | ~12.000 | 47 | 31 | 40 | 2.150 (fev/21) | 1,142 | 2.456 | 3.144 | Primeiro do trio |

**Insight chave:** Brooklyn tem **85 UR (vs 55 e 47)** = **economia de escala** → custos fixos (gerenciamento, elevadores, sistemas especiais, complementares) diluídos em mais apartamentos. **CUB 1,01 = MAIS BAIXO DOS 3** — não é suborçamento, é eficiência real.

**Validação cruzada interna:** A própria apresentação do Brooklyn CITA Soho e Velazquez como "obras similares" de referência → Mussi usa trio como benchmark interno.

---

## DADOS DE ENTRADA — PROJETO 3: Amalfi San Felice (CTN-ALF-SFL)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 953,88 | m² |
| Área Construída | AC | 7.456,95 | m² |
| Unidades Habitacionais | UR | 45 | un |
| Churrasqueiras | CHU | 47 | un |
| Nº Total Pavimentos | NP | 13 | un |
| Nº Pavimentos Tipo | NPT | 9 | un |
| Nº Pav. Tipo Diferenciados | NPD | 0 | un |
| Área de Lazer | AL | 308,79 | m² |
| Área Projeção Torre | APT | 545,25 | m² |
| Perímetro Projeção Torre | PPT | 109,27 | m |
| Área Embasamento | AE | 2.339,49 | m² |
| Área Projeção Embasamento | APE | 761,33 | m² |
| Perímetro Projeção Embasamento | PPE | 121,18 | m |
| Nº Pav. Embasamento | NPE | 3 | un |
| Nº Subsolos | NS | 0 | un |
| Meses de Obra | — | 38 | meses |
| Elevadores | — | 2 | un |

### Custos Diretos + Indiretos — Amalfi San Felice (R$ — Mar/2024)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Gerenciamento Técnico e Admin. | 3.151.072 | 422,57 | 12,8% |
| Supraestrutura (Cubetas) | 4.465.115 | 598,79 | 18,2% |
| Instalações (Elét+Hidro+Prev) | 2.405.326 | 322,56 | 9,8% |
| Esquadrias | 1.821.771 | 244,31 | 7,4% |
| Complementares | 1.744.926 | 234,00 | 7,1% |
| Alvenaria | 1.550.152 | 207,88 | 6,3% |
| Acabamentos Piso/Parede | 1.436.759 | 192,67 | 5,9% |
| Infraestrutura | 1.366.208 | 183,21 | 5,6% |
| Fachada | 1.294.276 | 173,57 | 5,3% |
| Sistemas Especiais | 1.132.452 | 151,87 | 4,6% |
| Pintura | 1.046.623 | 140,36 | 4,3% |
| Rev. Internos Piso/Parede | 1.044.320 | 140,05 | 4,3% |
| Teto | 747.783 | 100,28 | 3,0% |
| Imprevistos (3%) | 623.122 | 83,55 | 2,5% |
| Impermeabilização | 549.022 | 73,63 | 2,2% |
| Movimentação de Terra | 165.987 | 22,26 | 0,7% |
| **TOTAL** | **24.544.913** | **3.292** | **100%** |

### Índices-chave — Amalfi San Felice

#### Supraestrutura (Cubetas, opção escolhida)

| Item | Índice | Un | PU (R$) | Obs |
|------|--------|----|---------|-----|
| Fabricação forma | 8 reutilizações | m² | 85,00 | |
| Montagem forma | 2,0 | m²/AC | 1,50 | |
| Escoramento torre | — | m² | 45 R$/m² | |
| Escoramento embasamento | — | m² | 45 R$/m² | |
| Cubetas | — | m² | 24 R$/m² | |
| Concreto | 0,23 | m³/AC | 603 R$/m³ | 535+40+bomb, 5% perda |
| Armadura | 110 | kg/m³ | 7,25 R$/kg | 10% perda |
| MO estrutura | 200 | R$/AC | — | |

#### Instalações (R$/AC)

| Subgrupo | Índice (R$/AC) |
|----------|---------------|
| Elétricas | 127,00 |
| Hidrossanitárias | 150,56 |
| Preventivas + GLP | 45,00 |
| **Total** | **322,56** |

#### Esquadrias

| Item | Qtd | PU (R$) |
|------|-----|---------|
| Alumínio | 1.342 m² | 741,33 R$/m² |
| Guarda-corpo vidro | 391 m² | 727,37 R$/m² |
| Gradil | 229 m | 671,38 R$/m |
| PCF | 24 un | 1.150 R$/un |
| Esquadrias madeira | 288 un | 900 R$/un |
| Corrimão madeira | 237 m | 181,50 R$/m |
| Portão alumínio | 2 un | 18.000 R$/un |

#### Alvenaria (com Drywall)

| Item | Qtd | PU (R$) | Obs |
|------|-----|---------|-----|
| Alv. embasamento | 0,8 m²/AE | 30 R$/m² | |
| Alv. tipo | 1,5 m²/APT×NPT | 30 R$/m² | |
| Drywall tipo | 1,5 m²/APT×NPT | 220 R$/m² | Alto padrão |
| Alv. escadas | 0,17 m²/AC | 60 R$/m² | |
| MO | — | 65 R$/m² | |

#### Custos Indiretos (R$ 3.764.677 — via planilha CI)

| Grupo | Valor (R$) | R$/m² |
|-------|-----------|-------|
| Gerenciamento Técnico | 501.500 | 67,25 |
| Segurança/MA/Saúde | 500.605 | 67,13 |
| Administração/canteiro | 2.507.256 | 336,22 |
| Equipamentos | 255.315 | 34,23 |
| **Total Indiretos** | **3.764.677** | **504,83** |

#### Equipe de Gestão (38 meses)

| Cargo | Custo/mês |
|-------|-----------|
| Engenheiro Civil | 7.200 |
| Mestre Geral | 5.000 |
| Almoxarife | 2.500 |
| Auxiliar Engenharia | 9.000 |
| Estagiário | 1.300 |
| Operador Guincho | 4.500 |
| Servente | 4.200 |
| Setor Projetos | 3.000 |
| Vigilância | 12.212 |
| **Total/mês** | **~48.912** |

---

## DADOS DE ENTRADA — PROJETO 26: Kirchner West Village (CTN-KIR-WST)

| Variável | ID | Valor | Unidade |
|---|---|---|---|
| Localização | — | Itapema/SC | — |
| Área do Terreno | AT | 769,20 | m² |
| Área Construída | AC | 10.722,50 | m² |
| Unidades Habitacionais | UR | 44 | un |
| Nº Total Pavimentos | NP | 21 | un |
| Nº Pavimentos Tipo | NPT | 15 | un |
| Nº Pav. Garagem | NPG | 3 | un |
| Elevadores | — | 2 | un |
| Prazo de Obra | — | 35 | meses |
| Data-base | — | Dez/2023 | — |
| CUB ref. | — | 2.752,67 | R$ |

### Custos por Macrogrupo — Kirchner West Village (R$ — Dez/2023)

| Grupo | Valor (R$) | R$/m² | % |
|---|---|---|---|
| Gerenciamento Técnico e Admin. | 2.786.052 | 259,83 | 9,2% |
| Movimentação de Terra | 110.350 | 10,29 | 0,4% |
| Infraestrutura | 2.370.949 | 221,12 | 7,9% |
| Supraestrutura (Cubetas) | 5.880.204 | 548,40 | 19,5% |
| Alvenaria | 1.669.970 | 155,74 | 5,5% |
| Impermeabilização | 717.784 | 66,94 | 2,4% |
| Instalações (Hidro+Elét+Prev+Gás+Telecom) | 2.583.002 | 240,89 | 8,6% |
| Sistemas Especiais | 1.034.052 | 96,44 | 3,4% |
| Climatização | 269.763 | 25,16 | 0,9% |
| Rev. Internos Parede | 2.179.759 | 203,29 | 7,2% |
| Teto | 568.584 | 53,03 | 1,9% |
| Pisos e Pavimentações | 2.316.032 | 216,00 | 7,7% |
| Pintura | 2.128.847 | 198,54 | 7,1% |
| Esquadrias | 2.263.600 | 211,11 | 7,5% |
| Louças e Metais | 351.078 | 32,74 | 1,2% |
| Fachada | 1.201.334 | 112,04 | 4,0% |
| Complementares | 1.316.232 | 122,75 | 4,4% |
| Imprevistos (1,5%) | 446.214 | 41,61 | 1,5% |
| **TOTAL** | **30.193.806** | **2.815,93** | **100%** |

> **Origem:** Orçamento executivo R03 (não paramétrico). Índices detalhados em `orcamento-parametrico/kirchner-west-village-indices.md`

### Índices-chave — Kirchner West Village

#### Supraestrutura (Cubetas)

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Concreto total | 2.595 m³ | 0,242 m³/AC | 567 R$/m³ | fck 35, bombeável |
| Taxa de aço | 213.596 kg | 82,32 kg/m³ | 6,17-7,98 | Corte e dobra obra |
| Forma montagem | 13.377 m² | 1,25 m²/AC | 2,81-6,59 | |
| Cubetas/pav (54×54) | ~779 | un/pav | 116,72 (compra) | |
| MO estrutura tipo | — | R$/m² | 188 | Preço Kirchner |
| MO G1+Lazer | — | R$/m² | 244 | 1,3× tipo |

#### Infraestrutura

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Estacas HC | 4.205 m (145 un) | 0,39 m/AC | 100-120 | ø50+ø60 |
| Concreto fck 40 | 1.237 m³ | — | 590 | Estacas |
| Concreto fck 35 | 562 m³ | — | 567 | Blocos+baldrames |
| Aço fundação rasa | 46.040 kg | 81,96 kg/m³ | 6,12-6,60 | |
| MO infra | — | R$/m² laje | 250 | |

#### Instalações (R$/m² AC)

| Subgrupo | Índice (R$/m² AC) |
|---|---|
| Hidrossanitárias | 87,03 |
| Elétricas | 101,90 |
| Preventivas | 23,87 |
| Gás | 13,98 |
| Comunicações | 14,11 |
| **Total** | **240,89** |

#### MO Instalações (contratos R$/m² AC)

| Disciplina | R$/m² AC |
|---|---|
| Hidrossanitária | 30,15 |
| Elétrica | 24,40 |
| Telecom | 10,45 |
| Preventiva | 4,20 |
| **Total MO** | **69,20** |

#### Alvenaria

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Alvenaria total | 14.682 m² | 1,37 m²/AC | — | |
| Bloco cerâmico 9cm | — | m² | 31,77 | Material |
| Bloco cerâmico 14cm | — | m² | 47,21 | Material |
| MO bloco cerâmico | — | m² | 36,00 | |

#### Esquadrias

| Item | Qtd | PU (R$) | Obs |
|---|---|---|---|
| Guarda-corpo alum/vidro | 205 m² | 1.276,85 | |
| Pele de vidro | 204 m² | 2.020,79 | |
| Porta madeira 80×210 | 185 un | 1.465,65 | |
| PCF 90×210 | 42 un | 1.060 | |
| Brise | 176 m² | 1.303,63 | |
| Portas/UR | 10,73 | — | |

---

## DADOS DE ENTRADA — PROJETO 27: Adore Level UP (CTN-ADR-LVU)

| Variável | Valor |
|---|---|
| Localização | Florianópolis/SC (Cachoeira do Bom Jesus) |
| Empresa | Adore Incorporações |
| Área Construída (AC) | 11.102,72 m² |
| Área do Terreno | 3.193 m² |
| Unidades | 141 (88 resid + 33 estúdios + 20 comerciais) |
| Pavimentos | 7 (Térreo, Sobreloja, Garden, 2 Tipo, Cobertura, Barrilete/Reserv.) |
| Elevadores | 3 |
| Vagas | 95 |
| Prazo | 36 meses |
| Data-base | Agosto/2025 |
| CUB | R$ 2.911,91 |
| R$/m² | R$ 3.628,65 |
| CUB ratio | 1,25 |
| Tipo Laje | Nervurada (embasamento) + Maciça (tipo) |
| Fundação | Hélice contínua ø40/ø50/ø60 — 12m |
| Revisão | R00 (Michelle/Edileni) |

### Custos por Macrogrupo — Adore Level UP (R$ — Ago/2025)

| Grupo | Valor (R$) | R$/m² | % |
|---|---|---|---|
| Gerenciamento Técnico e Admin. | 4.073.248 | 366,87 | 10,1% |
| Movimentação de Terra | 198.729 | 17,90 | 0,5% |
| Infraestrutura | 1.941.462 | 174,86 | 4,8% |
| Supraestrutura | 6.615.187 | 595,82 | 16,4% |
| Alvenaria | 1.669.934 | 150,41 | 4,2% |
| Instalações (Elét+Hidro+GLP+Prev) | 4.311.922 | 388,37 | 10,7% |
| Equipamentos e Sistemas Especiais | 1.997.062 | 179,87 | 5,0% |
| Impermeabilização | 948.729 | 85,45 | 2,4% |
| Rev. Internos Parede | 3.214.009 | 289,48 | 8,0% |
| Teto | 753.156 | 67,84 | 1,9% |
| Pisos | 4.313.008 | 388,46 | 10,7% |
| Pintura Interna | 1.273.616 | 114,71 | 3,2% |
| Esquadrias | 3.821.897 | 344,23 | 9,5% |
| Cobertura | 375.409 | 33,81 | 0,9% |
| Fachada | 1.517.056 | 136,64 | 3,8% |
| Complementares | 3.263.432 | 293,93 | 8,1% |
| **TOTAL** | **40.287.856** | **3.628,65** | **100%** |

### Índices-chave — Adore Level UP

#### Supraestrutura (Nervurada embasamento + Maciça tipo)

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Concreto total | 2.100 m³ | 0,189 m³/AC | 578 R$/m³ | fck 30, bombeável |
| Taxa de aço | 241.241 kg | 114,88 kg/m³ | 6,50-7,00 | Corte e dobra obra |
| Forma total | 15.055 m² | 1,36 m²/AC | — | |
| Cubetas (nervurada) | 3.659 un | — | 75/un (locação) | Embasamento |
| MO supraestrutura | — | R$/m² AC | 243,91 | Contrato empreiteira |

#### Infraestrutura

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Estacas HC | 2.124 m (177 un) | 0,19 m/AC | 96 | ø40+ø50+ø60, 12m |
| Concreto fck 40 | 524 m³ | — | 716 | Estacas |
| Concreto fck 30 | 300 m³ | — | 578 | Blocos+baldrames |
| Aço infraestrutura | 24.338 kg | 81,00 kg/m³ | 6,12-7,00 | |
| MO infra | — | vb | 758.777 | Contrato |

#### Instalações (R$/m² AC)

| Subgrupo | Índice (R$/m² AC) |
|---|---|
| Hidrossanitárias | 136,17 |
| Elétricas | 172,02 |
| Preventivas | 21,15 |
| Gás | 14,30 |
| Comunicações | 17,03 |
| Climatização+Exaustão | 71,61 |
| **Total** | **432,28** |

#### MO Instalações (contratos R$/m² AC)

| Disciplina | R$/m² AC |
|---|---|
| Hidrossanitária | 61,86 |
| Elétrica | 47,72 |
| Preventiva | 6,93 |
| Gás | 5,72 |
| **Total MO** | **122,23** |

#### Alvenaria

| Item | Índice | Un | PU (R$) | Obs |
|---|---|---|---|---|
| Alvenaria total | 17.358 m² | 1,56 m²/AC | — | |
| Bloco cerâmico 11,5cm | — | m² | 37,57 | Material |
| Bloco cerâmico 14cm | — | m² | 59,61 | Material |
| MO alvenaria | — | m² | 46,73 | Contrato |

#### Esquadrias

| Item | Qtd | PU (R$) | Obs |
|---|---|---|---|
| Esquadrias alumínio | 1.030 m² | 1.350,00 | Fornec+inst |
| Vitrine de vidro | 483 m² | 1.534,00 | |
| Guarda-corpo vidro+alum | 226 m² | 935,99 | |
| Porta madeira 80×210 | 280 un | 1.355,00 | Kit c/ espuma |
| Fechadura eletrônica | 88 un | 1.386,60 | |
| Portas/UR | 3,05 | — | 141 unidades |

> 📁 Índices detalhados: `orcamento-parametrico/adore-level-up-indices.md`

---

## DADOS DE ENTRADA — PROJETO 28: Amalfi Maiori (CTN-ALF-MRI)

| Variável | Valor |
|---|---|
| Localização | Itajaí/SC |
| Empresa | Construtora Amalfi |
| Área Construída (AC) | 8.366,50 m² (Apres.) / 8.369,50 m² (Orç.) |
| Área Privativa | 4.969,86 m² |
| Unidades | 60 (residenciais) |
| Pavimentos | 18 (Térreo, 3 Garagens, 1 Tipo Dif., 11 Tipo, Rooftop, Reserv/Barl/CMax) |
| Elevadores | N/D |
| Vagas | N/D |
| Prazo | 38 meses |
| Data-base | Julho/2023 |
| CUB | R$ 2.747,90 |
| R$/m² | R$ 3.010,31 |
| CUB ratio | 1,10 |
| Tipo Laje | N/D (concreto fck 40 MPa) |
| Fundação | Blocos + Baldrames (33 blocos, 40 baldrames) |
| Revisão | R05 (Orçamento) / R02 (Apresentação) |

### Custos por Macrogrupo — Amalfi Maiori (R$ — Jul/2023)

| Grupo | Valor (R$) | R$/m² | % |
|---|---|---|---|
| Gerenciamento Técnico e Admin. | 3.318.914 | 396,69 | 13,18% |
| Movimentação de Terra | 61.667 | 7,37 | 0,24% |
| Infraestrutura | 1.477.672 | 176,62 | 5,87% |
| Supraestrutura | 4.952.967 | 592,00 | 19,67% |
| Paredes e Painéis | 957.804 | 114,48 | 3,80% |
| Instalações (Elét+Hidro+GLP+Prev) | 2.471.960 | 295,46 | 9,81% |
| Equipamentos e Sistemas Especiais | 1.127.280 | 134,74 | 4,48% |
| Impermeabilização | 539.873 | 64,53 | 2,14% |
| Rev. Internos Parede | 1.640.085 | 196,03 | 6,51% |
| Teto | 482.761 | 57,70 | 1,92% |
| Pisos | 1.116.640 | 133,47 | 4,43% |
| Pintura Interna | 1.143.520 | 136,68 | 4,54% |
| Esquadrias | 2.795.226 | 334,10 | 11,10% |
| Louças e Metais | 205.366 | 24,55 | 0,82% |
| Cobertura | 123.462 | 14,76 | 0,49% |
| Fachada | 1.248.714 | 149,25 | 4,96% |
| Complementares | 1.521.822 | 181,89 | 6,04% |
| **TOTAL** | **25.185.733** | **3.010,31** | **100%** |

### Índices-chave — Amalfi Maiori

#### Supraestrutura (fck 40 MPa)

| Item | Índice | Un | Obs |
|---|---|---|---|
| Concreto total | 2.068 m³ | 0,247 m³/AC | fck 40 (acima da média) |
| Pilares | 594,37 m³ | 28,7% | — |
| Vigas | 339,41 m³ | 16,4% | — |
| Lajes | 1.134,35 m³ | 54,8% | — |
| Taxa de aço | 211.302 kg | 102,17 kg/m³ | Entre KIR (82) e ADR (115) |
| Forma total | 10.836 m² | 1,30 m²/AC | — |
| **R$/m² supraestrutura** | **592,00** | **R$/m²** | **Abaixo faixa 660-790** |

#### Infraestrutura (Blocos + Baldrames)

| Item | Índice | Un | Obs |
|---|---|---|---|
| Blocos fundação | 33 un | 264,15 m³ | Concreto C-40 |
| Baldrames | 40 un | 25,66 m³ | — |
| Forma infra | 641,51 m² | 0,077 m²/AC | — |
| Aço infra | 34.888 kg | 105,4 kg/m³ | — |

#### Acabamentos e Instalações

| Item | Índice | Un |
|---|---|---|
| Chapisco interno | 18.141 m² | 2,17 m²/AC |
| Forro total | 7.140 m² | 0,85 m²/AC |
| Contrapiso | 5.199 m² | 0,62 m²/AC |
| Pintura parede | 13.582 m² | 1,62 m²/AC |
| Fachada (massa) | 6.863 m² | 0,82 m²/AC |
| Impermeabilização | 4.088 m² | 0,49 m²/AC |
| Rodapé | 4.176 m | 0,50 m/AC |
| Contramarco | 1.644 m | 0,20 m/AC |
| Instalações | R$ 295/m² | Dentro 280-340 |
| Esquadrias | R$ 334/m² | Acima 240-330 |
| Louças e Metais / UR | R$ 3.423 | R$/UR |

#### Destaques

- ⚠️ **Supraestrutura abaixo** da faixa: R$ 592/m² vs 660-790 (-10%)
- ⚠️ **Esquadrias acima**: R$ 334/m² vs 240-330 (brise 428 m² + pele vidro 139 m²)
- ⚠️ **CI alto**: 13,18% (formulário CI preenchido pelo engenheiro Vinícius)
- ✅ Instalações, fachada, impermeabilização, alvenaria dentro das faixas
- 📝 **fck 40 MPa** em toda supra (diferente dos demais projetos fck 30-35)
- 📝 **Duas colunas de preço**: Cartesian vs Amalfi (diferenças em projetos/consultorias)

> 📁 Índices detalhados: `orcamento-parametrico/amalfi-maiori-indices.md`

---

## COMPARATIVO ENTRE PROJETOS (R$/m²)

| Grupo | 2cinco4 (R$/m²) | San Felice (R$/m²) | Δ |
|-------|----------------|-------------------|---|
| Gerenciamento | 307 | 423 | +37% |
| Supraestrutura | 661 | 599 | -9% |
| Instalações | 327 | 323 | -1% ✅ |
| Esquadrias | 417 | 244 | -41% |
| Alvenaria | 154 | 208 | +35% |
| Sistemas Especiais | 215 | 152 | -29% |
| Impermeabilização | 73 | 74 | +1% ✅ |
| Rev. Internos | 201 | 140 | -30% |
| Teto | 74 | 100 | +36% |
| Acabamentos | 200 | 193 | -4% ✅ |
| Pintura | 171 | 140 | -18% |
| Fachada | 154 | 174 | +13% |
| Complementares | 184 | 234 | +27% |
| Imprevistos | 92 | 84 | -9% |
| **TOTAL** | **3.457** | **3.292** | **-5%** |

### Observações do Comparativo:
1. **Instalações e Impermeabilização** praticamente idênticas → índices R$/AC estáveis
2. **Esquadrias muito diferentes** — 2cinco4 tem pele de vidro e brises caros; San Felice mais simples
3. **Gerenciamento maior no SF** proporcionalmente — prédio menor dilui menos os custos fixos (vigilância, equipe)
4. **Alvenaria maior no SF** — alto uso de drywall (R$ 220/m²) puxa o índice pra cima
5. **Supraestrutura 2cinco4 mais cara** — prédio mais alto (27 vs 13 pav)

---

## DADOS DE ENTRADA — PROJETO 4: BD Jardim Campeche

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 866,65 | m² |
| Área Construída | AC | 3.632,78 | m² |
| Unidades Residenciais | UR | 20 | un |
| Unidades Comerciais | UC | 2 | un |
| Churrasqueiras | CHU | 21 | un |
| Nº Total Pavimentos | NP | 7 | un |
| Nº Pavimentos Tipo | NPT | 4 | un |
| Nº Pav. Tipo Diferenciados | NPD | 1 | un |
| Área de Lazer | AL | 473,79 | m² |
| Área Projeção Torre | APT | 634,94 | m² |
| Perímetro Projeção Torre | PPT | 120,70 | m |
| Área Subsolos | AS | 655,95 | m² |
| Nº Subsolos | NS | 1 | un |
| Área Embasamento | AE | 674,15 | m² |
| Área Projeção Embasamento | APE | 674,15 | m² |
| Perímetro Projeção Embasamento | PPE | 123,46 | m |
| Nº Pav. Embasamento | NPE | 1 | un |
| Meses de Obra | — | 36 | meses |
| Elevadores | — | 1 | un |
| Vagas | — | 22 | un |
| Dormitórios | — | 42 | un |
| Banheiros | — | 51 | un |
| Área Privativa | — | 2.064,55 | m² |

### Custos — BD Jardim Campeche (R$ — Jan/2026)

> **NOTA:** Este projeto tem "Mobiliário Privativo" (R$ 4,43M = 1.950 R$/m² de área privativa) como item separado. O R$/m² abaixo EXCLUI mob. privativo pra comparação justa.

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura (Cubetas) | 2.901.220 | 798,62 | 17,8% |
| Gerenciamento Técn. e Admin. | 2.551.044 | 702,02 | 15,6% |
| Esquadrias | 1.379.827 | 379,83 | 8,5% |
| Instalações (Elét+Hidro+Prev) | 1.372.646 | 377,85 | 8,4% |
| Infraestrutura | 978.971 | 269,48 | 6,0% |
| Complementares | 965.572 | 265,79 | 5,9% |
| Acabamentos Piso/Parede | 918.707 | 252,89 | 5,6% |
| Rev. Internos Piso/Parede | 808.213 | 222,48 | 5,0% |
| Sistemas Especiais | 697.858 | 192,10 | 4,3% |
| Contenção (Parede Diafragma) | 692.137 | 190,53 | 4,2% |
| Pintura | 678.658 | 186,81 | 4,2% |
| Fachada | 667.707 | 183,80 | 4,1% |
| Movimentação de Terra | 309.992 | 85,33 | 1,9% |
| Teto | 299.766 | 82,52 | 1,8% |
| Impermeabilização | 292.180 | 80,43 | 1,8% |
| Imprevistos (3%) | 270.405 | 74,44 | 1,7% |
| Cobertura | 159.581 | 43,93 | 1,0% |
| **Subtotal (s/ mob. privativo)** | **16.314.492** | **4.491** | **100%** |
| Mobiliário Privativo | 4.428.460 | 1.219,16 | — |
| **TOTAL GERAL** | **20.742.952** | **5.710** | — |

### Custos Indiretos — BD Jardim Campeche (R$ 2.581.278 = 711 R$/m²)

| Grupo | Valor (R$) | R$/m² |
|-------|-----------|-------|
| Gerenciamento Técnico | 408.540 | 112,45 |
| Segurança/MA/Saúde | 337.319 | 92,85 |
| Administração/canteiro | 1.502.849 | 413,72 |
| Equipamentos | 332.570 | 91,55 |
| **Total Indiretos** | **2.581.278** | **710,55** |

#### Equipe de Gestão (36 meses)

| Cargo | Custo/mês |
|-------|-----------|
| Engenheiro Civil | 6.600 |
| Mestre Geral | 7.500 |
| Auxiliar Engenharia | 5.500 |
| Operador Guincho | 3.500 (13 meses) |
| Equipe apoio (2 pess.) | 4.777 |
| Vigilância noturna | 5.087 |
| **Total/mês** | **~30.700** |

### Particularidades — BD Jardim Campeche

1. **Subsolo:** 1 subsolo (655 m²) — gera escavação vertical (R$ 223k) + rebaixamento de lençol (R$ 33k)
2. **Contenção:** Parede diafragma (não cortina de estacas) — R$ 692k (190 R$/m²)
3. **Mobiliário privativo separado:** R$ 4,43M = 1.950 R$/m² de área privativa (marcenaria completa?)
4. **Pele de vidro nas lojas:** 376 m² a R$ 980/m² = R$ 369k
5. **Fachada com pastilha + porcelanato amadeirado:** R$ 269k em acabamentos especiais
6. **Alvenaria predominante (pouco drywall):** Apenas 46 m² de drywall tipo ST
7. **Piso cerâmico (sem porcelanato nem vinílico):** Mais econômico que projetos anteriores
8. **Fechadura biométrica:** R$ 1.500/un × 20 unidades
9. **Esquadria madeira mais cara:** R$ 2.100/un (vs R$ 900 no San Felice)
10. **BDI = 1.10** aplicado em todos os preços unitários do analítico

---

## DADOS DE ENTRADA — PROJETO 5: Monolyt (Blue Heaven)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 7.541,68 | m² |
| Área Construída | AC | 14.693,42 | m² |
| Unidades Residenciais | UR | 24 | un |
| Nº Total Pavimentos | NP | 4 + 4 (2 torres) | un |
| Nº Pavimentos Tipo | NPT | 3 + 3 | un |
| Nº Pav. Diferenciados | NPD | 1 (Torre B) | un |
| Nº Pav. Duplex | ND | 1 + 1 | un |
| Área Projeção Torre A | APT-A | 1.375,85 | m² |
| Área Projeção Torre B | APT-B | 1.294,19 | m² |
| Perímetro Torre A | PPT-A | 239,41 | m |
| Perímetro Torre B | PPT-B | 209,46 | m |
| Área Lazer Interna | ALI | 343,39 | m² |
| Área Lazer Externa | ALE | 2.661,29 | m² |
| Área Subsolos | AS | 3.904,14 (2×TA + 1×TB) | m² |
| Nº Subsolos | NS | 2 (TA) + 1 (TB) | un |
| Área Embasamento | APE | 3.904,14 | m² |
| Perímetro Embasamento | PPE | 176,28 + 215,72 | m |
| Meses de Obra | — | 36 | meses |
| Elevadores | — | 6 + 1 (1 parada) = 7 | un |
| Churrasqueiras | CHU | 24 | un |
| CUB/SC data-base | — | 2.758,46 (Mai/2024) | R$ |
| Laje | — | Protendida | — |
| Torres | — | 2 (A e B) | un |

### Custos — Monolyt (R$ — Mai/2024)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura (Protendida) | 16.955.390 | 1.153,94 | 19,3% |
| Gerenciamento Técn. e Admin. | 14.538.860 | 989,48 | 16,5% |
| Esquadrias | 9.402.166 | 639,89 | 10,7% |
| Sistemas Especiais | 7.227.829 | 491,91 | 8,2% |
| Instalações (Elét+Hidro+Prev) | 6.206.501 | 422,40 | 7,1% |
| Infraestrutura | 5.742.340 | 390,81 | 6,5% |
| Acabamentos Piso/Parede | 4.311.126 | 293,41 | 4,9% |
| Complementares | 3.531.038 | 240,31 | 4,0% |
| Alvenaria | 3.148.673 | 214,29 | 3,6% |
| Fachada | 3.087.626 | 210,14 | 3,5% |
| Mov. Terra | 2.545.063 | 173,21 | 2,9% |
| Imprevistos | 2.562.538 | 174,40 | 2,9% |
| Pintura | 2.297.073 | 156,33 | 2,6% |
| Teto | 1.764.974 | 120,12 | 2,0% |
| Rev. Internos Piso/Parede | 1.754.485 | 119,41 | 2,0% |
| Contenção | 1.644.605 | 111,93 | 1,9% |
| Impermeabilização | 1.260.169 | 85,76 | 1,4% |
| **TOTAL** | **87.980.454** | **5.987,75** | **100%** |

*2,17 CUB/SC*

### Custos Indiretos — Monolyt (R$ ~13,5M = 919 R$/m²)

| Grupo | Valor (R$) | R$/m² |
|-------|-----------|-------|
| Gerenciamento Técnico | 1.959.447 | 133,36 |
| Segurança/MA/Saúde | 878.433 | 59,78 |
| Administração/canteiro | 9.608.771 | 653,81 |
| Equipamentos | 1.064.057 | 72,42 |
| **Total Indiretos** | **~13.510.709** | **~919** |

#### Equipe de Gestão (36 meses) — ~R$ 225k/mês total

| Cargo | Custo/mês | Obs |
|-------|-----------|-----|
| Engenheiro Civil | 0 | (custo não alocado na obra) |
| 2× Mestre Geral | 25.760 | |
| 2× Contra Mestre | 10.000 | (18 meses finais) |
| 2× Almoxarife | 8.509 | |
| 4× Estagiário | 7.840 | |
| 2× Operador Grua | 31.200 | (27 meses) |
| 2× Operador Bobcat | 11.600 | |
| 2× Operador Cremalheira | 14.800 | (27 meses) |
| Equipe apoio (16 pess.) | 76.912 | (36 meses) |
| Equipe apoio extra (8 pess.) | 38.456 | (18 meses finais) |
| 3× Vigilância | 15.261 | |

### Particularidades — Monolyt

1. **Super alto padrão Bal. Camboriú** — R$ 5.988/m² (2,17 CUB)
2. **2 torres** — primeiro projeto multi-torre na base
3. **Laje PROTENDIDA** — diferente dos outros que usam cubetas. MO R$ 280/m² + protensão R$ 35/kg
4. **Piscinas privativas aquecidas** — equipamento de piscina R$ 1,34M (33 unidades)
5. **Placas fotovoltaicas:** R$ 1,37M como sistema especial
6. **Concreto aparente na fachada:** 10.610 m² a R$ 117,70/m² (resina, não textura)
7. **Piso madeira engenheirada:** 2.123 m² a R$ 437,80/m² (altíssimo padrão)
8. **Vidro piscina estrutural:** 516 m² a R$ 2.300/m² = R$ 1,31M
9. **Guarda-corpo vidro:** 557 m² a R$ 2.100/m² = R$ 1,29M
10. **Esquadria alumínio premium:** R$ 1.650/m² (vs R$ 1.290 no Campeche)
11. **2 gruas** — montagem + desmontagem R$ 220k
12. **Drywall predominante:** 7.929 m² drywall vs 4.993 m² alvenaria (60/40)
13. **Paisagismo externo alto valor:** R$ 440,67/m² × 2.661 m² = R$ 1,29M
14. **Infra + equipamento carro elétrico:** 24 unidades = R$ 285k
15. **Lago:** R$ 85,8k
16. **Fechadura eletrônica:** R$ 2.500/un (vs R$ 1.500 Campeche)
17. **Esquadria madeira:** R$ 1.535/un (vs R$ 2.100 Campeche, R$ 900 SF)
18. **Imprevistos:** ~3% consistente

---

## DADOS DE ENTRADA — PROJETO 6: Aquos Oasis Home (Blue Heaven)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 4.960,00 | m² |
| Área Construída | AC | 7.191,64 | m² |
| Unidades Residenciais | UR | 12 | un |
| Nº Total Pavimentos | NP | 4 + 4 + 4 (3 torres) | un |
| Nº Pavimentos Tipo | NPT | 3 + 3 + 3 | un |
| Nº Pav. Duplex | ND | 1 + 1 + 1 | un |
| Área Projeção Torres | APT | 904,39 (B/C) + 747,75 (A) | m² |
| Perímetro Torres | PPT | 233,45 + 239,41 | m |
| Área Lazer Interna | ALI | 53,04 | m² |
| Área Lazer Externa | ALE | 3.278,00 | m² |
| Área Subsolos | AS | 1.114,05 (B/C) + 967,51 (A) = 2.081,56 | m² |
| Nº Subsolos | NS | 1 + 1 + 1 | un |
| Área Embasamento | APE | 2.081,56 | m² |
| Meses de Obra | — | 36 | meses |
| Elevadores | — | ~6 | un |
| Torres | — | 3 (A, B, C) | un |
| CUB/SC data-base | — | 2.811,86 (Ago/2024) | R$ |
| Laje | — | Protendida | — |

### Custos — Aquos (R$ — Ago/2024)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Gerenciamento | 14.269.425 | 1.983,77 | 20,8% |
| Supraestrutura (Protendida) | 13.677.682 | 1.901,89 | 19,9% |
| Esquadrias | 5.968.291 | 829,89 | 8,7% |
| Sistemas Especiais | 5.378.764 | 747,92 | 7,8% |
| Complementares | 3.979.048 | 553,29 | 5,8% |
| Fachada | 3.928.649 | 546,28 | 5,7% |
| Infraestrutura | 3.113.525 | 432,94 | 4,5% |
| Instalações (Elét+Hidro+Prev) | 3.037.749 | 422,40 | 4,4% |
| Acabamentos Piso/Parede | 2.874.782 | 399,74 | 4,2% |
| Alvenaria | 2.332.924 | 324,39 | 3,4% |
| Contenção | 2.144.585 | 298,21 | 3,1% |
| Imprevistos | 1.996.980 | 277,68 | 2,9% |
| Mov. Terra | 1.578.343 | 219,47 | 2,3% |
| Pintura | 1.310.025 | 182,16 | 1,9% |
| Rev. Internos Piso/Parede | 1.214.241 | 168,84 | 1,8% |
| Teto | 1.084.571 | 150,81 | 1,6% |
| Impermeabilização | 673.401 | 93,64 | 1,0% |
| **TOTAL** | **68.562.985** | **9.534** | **100%** |

*3,39 CUB/SC*

### Custos Indiretos — Aquos (~R$ 9,2M base CI = 1.279 R$/m²)

| Grupo | Valor (R$) | R$/m² |
|-------|-----------|-------|
| Gerenciamento Técnico | 1.555.180 | 216,26 |
| Segurança/MA/Saúde | 785.506 | 109,22 |
| Administração/canteiro | 5.847.343 | 812,96 |
| Equipamentos | 1.012.604 | 140,80 |
| **Total CI (tab)** | **~9.200.633** | **~1.279** |

*Nota: o GE do analítico mostra R$ 14,27M (1.984 R$/m²) — diferença pode incluir itens adicionais não detalhados na aba CI*

### Particularidades — Aquos

1. **3 torres** — projeto mais fragmentado da base (12 UR em 3 torres = 4 aptos/torre)
2. **Laje protendida** — mesma tipologia do Monolyt (Blue Heaven)
3. **Supraestrutura R$ 1.902/m²** — ainda mais cara que Monolyt (1.154) por efeito de escala (7,2k vs 14,7k m²)
4. **Fachada R$ 546/m²** — a mais cara da base: pedra natural (1.457 m² a ~R$ 1.294/m²) + concreto aparente (7.862 m²) + piscinas pedra (558 m²)
5. **Complementares R$ 553/m²** — fechamento condomínio madeira R$ 1,06M + paisagismo privativo R$ 516k + paisagismo comum R$ 1,07M
6. **Contenção R$ 298/m²** — parede concreto 60cm (mais espessa que Campeche 20cm)
7. **Piscinas privativas aquecidas** + infra carro elétrico (como Monolyt)
8. **Equipe/mês menor que Monolyt** — ~R$ 140k/mês (vs 225k) — 1 mestre (vs 2), sem engenheiro alocado
9. **CUB ratio mais alto da base:** 3,39 CUB — efeito de escala extremo (3 torres × 4 aptos)

---

## DADOS DE ENTRADA — PROJETO 7: Redentor (Brasin)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 774,60 | m² |
| Área Construída | AC | 16.727,83 | m² |
| Unidades Residenciais | UR | 40 | un |
| Nº Total Pavimentos | NP | 43 | un |
| Nº Pavimentos Tipo | NPT | 32 | un |
| Nº Pav. Diferenciados | NPD | 1 | un |
| Nº Pav. Duplex | ND | 1 | un |
| Área Projeção Torre | APT | 383,13 | m² |
| Perímetro Torre | PPT | 88,89 | m |
| Área Lazer | AL | 1.156,76 | m² |
| Área Embasamento | AE | 5.653,56 | m² |
| Área Subsolos | AS | 0 | m² |
| Nº Subsolos | NS | 0 | un |
| Nº Pav. Embasamento | NPE | 6 | un |
| Meses de Obra | — | 50 | meses |
| CUB/SC data-base | — | 2.752,32 (Set/2023) | R$ |
| Laje | — | Protendida | — |
| Fundação | — | Estaca raíz (ø40-50, 30m prof.) | — |

### Custos — Redentor (R$ — Set/2023)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura (Protendida) | 13.295.076 | 794,79 | 19,7% |
| Esquadrias (linha Gold) | 8.661.677 | 517,80 | 12,8% |
| Gerenciamento | 6.211.221 | 371,31 | 9,2% |
| Instalações | 6.137.704 | 366,92 | 9,1% |
| Fachada | 4.606.194 | 275,36 | 6,8% |
| Infraestrutura (estaca raíz) | 4.159.370 | 248,65 | 6,2% |
| Sist. Especiais | 3.963.127 | 236,92 | 5,9% |
| Complementares | 3.584.586 | 214,29 | 5,3% |
| Acabamentos Piso/Parede | 3.343.149 | 199,86 | 4,9% |
| Alvenaria | 2.931.761 | 175,26 | 4,3% |
| Rev. Internos | 2.943.259 | 175,95 | 4,4% |
| Imprevistos | 1.969.674 | 117,75 | 2,9% |
| Pintura | 1.830.434 | 109,42 | 2,7% |
| Teto (forro mineral + acartonado) | 1.733.743 | 103,64 | 2,6% |
| Impermeabilização | 1.438.507 | 85,99 | 2,1% |
| Mov. Terra | 816.007 | 48,78 | 1,2% |
| **TOTAL** | **67.625.490** | **4.043** | **100%** |

*1,47 CUB/SC*

### Particularidades — Redentor

1. **Prédio mais alto da base:** 43 pavimentos (32 tipo) — escala vertical enorme
2. **Laje protendida** — supraestrutura a 795 R$/m² (abaixo do Monolyt 1.154, diluição por mais pavimentos tipo)
3. **Esquadrias linha Gold:** R$ 518/m² — alto padrão mas menor que BC
4. **Estaca raíz:** fundação profunda (30m) com estacas de 40-50cm + hélice contínua 50-70cm
5. **Fachada R$ 275/m²:** pintura + revestimentos especiais (R$ 709k) — mais caro que standard
6. **Sem subsolo** — terreno pequeno (775 m²) com 6 pav embasamento
7. **Forro mineral + acartonado:** R$ 104/m² (opção mais cara que gesso liso)
8. **50 meses de obra** — o mais longo da base
9. **Instalações acima da média:** R$ 367/m² (edifício alto = mais pressurização, hidrantes, etc)
10. **Imprevistos:** 2,9% consistente com os outros projetos
11. **Data-base antiga (Set/2023)** — valores precisam correção CUB pra comparar com projetos 2024-2026

---

## DADOS DE ENTRADA — PROJETO 8: Catena (CKock)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 720,08 | m² |
| Área Construída | AC | 9.242,43 | m² |
| Unidades Residenciais | UR | 48 | un |
| Nº Total Pavimentos | NP | 30 | un |
| Meses de Obra | — | 54 | meses |
| CUB/SC data-base | — | 3.008,84 (Nov/2025) | R$ |

### Custos — Catena (R$ — Nov/2025)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura | 6.996.295 | 757,00 | 22,4% |
| Gerenciamento | 3.622.621 | 392,00 | 11,6% |
| Instalações | 3.400.752 | 368,00 | 10,9% |
| Esquadrias | 2.865.710 | 310,00 | 9,2% |
| Infraestrutura | 2.198.063 | 238,00 | 7,0% |
| Sist. Especiais | 1.959.248 | 212,00 | 6,3% |
| Complementares | 1.589.535 | 172,00 | 5,1% |
| Acabamentos | 1.564.511 | 169,00 | 5,0% |
| Rev. Internos | 1.531.100 | 166,00 | 4,9% |
| Alvenaria | 1.496.546 | 162,00 | 4,8% |
| Fachada | 1.279.395 | 138,00 | 4,1% |
| Pintura | 1.138.119 | 123,00 | 3,6% |
| Imprevistos | 540.783 | 59,00 | 1,7% |
| Teto | 448.073 | 48,00 | 1,4% |
| Impermeabilização | 416.618 | 45,00 | 1,3% |
| Mov. Terra | 155.173 | 17,00 | 0,5% |
| **TOTAL** | **31.202.541** | **3.376** | **100%** |

*1,12 CUB/SC*

### Particularidades — Catena

1. **Primeiro projeto "médio-alto" padrão** na base — CUB ratio 1,12 (vs 1,18-3,39 nos outros)
2. **Impermeabilização apenas R$ 45/m²** — a mais baixa da base (menos itens impermeabilizados?)
3. **Teto R$ 48/m²** — o mais baixo, sugere forro simples (gesso liso, sem negativo nem sanca)
4. **Fachada R$ 138/m²** — a mais barata, revestimento mais simples
5. **48 UR em 30 pavimentos** — alta densidade
6. **54 meses** — prazo longo (segundo maior), pode indicar equipe mais enxuta

---

## DADOS DE ENTRADA — PROJETO 9: Zapata (CKock)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 622,90 | m² |
| Área Construída | AC | 7.532,89 | m² |
| Unidades Residenciais | UR | 36 + 2 UC | un |
| Nº Total Pavimentos | NP | 24 | un |
| Nº Pavimentos Tipo | NPT | 18 | un |
| Churrasqueiras | CHU | 37 | un |
| Nº Subsolos | NS | 0 | un |
| Área Projeção Torre | APT | 233,81 | m² |
| Perímetro Torre | PPT | 58,74 | m |
| Área Lazer | AL | 504,89 | m² |
| Área Embasamento | AE | 3.252,31 | m² |
| Nº Pav. Embasamento | NPE | 6 | un |
| Meses de Obra | — | 48 | meses |
| CUB/SC data-base | — | 2.993,04 (Set/2025) | R$ |

### Custos — Zapata (R$ — Set/2025)

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura | 5.507.455 | 731,00 | 22,9% |
| Instalações | 2.744.524 | 364,00 | 11,4% |
| Gerenciamento | 2.428.979 | 322,00 | 10,1% |
| Esquadrias | 2.263.298 | 300,00 | 9,4% |
| Infraestrutura | 1.520.390 | 202,00 | 6,3% |
| Sist. Especiais | 1.517.065 | 201,00 | 6,3% |
| Complementares | 1.346.812 | 179,00 | 5,6% |
| Fachada | 1.319.586 | 175,00 | 5,5% |
| Alvenaria | 1.217.983 | 162,00 | 5,1% |
| Acabamentos | 1.018.034 | 135,00 | 4,2% |
| Pintura | 939.809 | 125,00 | 3,9% |
| Rev. Internos | 808.994 | 107,00 | 3,4% |
| Imprevistos | 629.726 | 84,00 | 2,6% |
| Teto | 365.195 | 48,00 | 1,5% |
| Impermeabilização | 351.740 | 47,00 | 1,5% |
| Mov. Terra | 70.000 | 9,00 | 0,3% |
| **TOTAL** | **24.049.588** | **3.193** | **100%** |

*1,07 CUB/SC*

### Particularidades — Zapata

1. **Projeto mais "econômico" da base** — 1,07 CUB, padrão médio
2. **Porto Belo/SC** — mercado diferente de BC e Itapema
3. **2 salas comerciais** no térreo (UC)
4. **Terreno mínimo:** 623 m² → alta verticalização (24 pav em terreno pequeno)
5. **Sem subsolo** — estacionamento no embasamento (6 pavimentos)
6. **Impermeabilização R$ 47/m²** — consistente com o Catena (mesma construtora)
7. **Teto R$ 48/m²** — mesmo padrão que Catena (forro simples)
8. **Rev. Internos apenas R$ 107/m²** — o mais baixo, menos reboco/chapisco
9. **Tinha R00 e R01** — R01 reduziu R$ 3M (-12%), otimizou esquadrias (-35%) e revestimentos
10. **Mesma construtora que Catena** — CKock Empreendimentos, padrões de custo similares

---

## DADOS DE ENTRADA — PROJETO 29: Amalfi Marine (CTN-ALF-MRN)

> **Fonte:** Orçamento Comentado R01 + Apresentação R01 (Jul/2023)
> **Índices expandidos:** `orcamento-parametrico/amalfi-marine-indices.md` (16 seções completas)
> **Mesma construtora:** Amalfi (mesmo do Maiori #28)

### Dados Gerais
- **AC:** 4.498,66 m² | **AP:** 2.651,04 m² | **UR:** 27 un (3 tipologias: 83,67 / 104,22 / 106,67 m²)
- **Pavimentos:** 14 (Térreo, G1, Lazer, 9 Tipos, Cobertura, Casa Máq., Reservatório) | NPT=9, NPG=1
- **Vagas:** 29 | **Elevadores:** 1 | **Prazo:** 30 meses
- **CUB Ago/23:** R$ 2.750,52 | **R$/m²:** 3.135,89 (1,14 CUB) | **Total:** R$ 14.107.283
- **Laje:** Nervurada (cubeta 66×66×21cm) | **Fundação:** Hélice contínua | **Concreto:** fck 30 MPa

### Macrogrupos (R$/m²)

| Macrogrupo | R$/m² | % | Status vs Faixa |
|---|---|---|---|
| Gerenciamento Téc/Admin | 521,71 | 16,64% | ✅ |
| Movimentação de Terra | 16,84 | 0,54% | ✅ |
| Infraestrutura | 343,98 | 10,97% | ⚠️ MUITO ACIMA (faixa 115-190) |
| Supraestrutura | 484,53 | 15,45% | 🔽 Abaixo (faixa 560-630) |
| Paredes e Painéis | 117,11 | 3,73% | ✅ |
| Instalações | 281,28 | 8,97% | 🔽 Abaixo (faixa 330-400) |
| Equip. e Sist. Especiais | 171,78 | 5,48% | ✅ |
| Impermeabilização | 66,94 | 2,13% | 🔽 Marginal |
| Rev. Internos Parede | 163,27 | 5,21% | ✅ |
| Teto | 42,00 | 1,34% | ✅ |
| Pisos | 142,75 | 4,55% | 🔽 Abaixo (faixa 180-210) |
| Pintura Interna | 142,72 | 4,55% | ✅ |
| Esquadrias | 237,47 | 7,57% | 🔽 Marginal |
| Louças e Metais | 23,79 | 0,76% | ✅ |
| Cobertura | 15,04 | 0,48% | ✅ |
| Fachada | 123,43 | 3,94% | ✅ |
| Complementares | 241,25 | 7,69% | ✅ (topo) |

### Índices Estruturais

| Índice | Valor |
|---|---|
| Concreto supra / AC | 0,253 m³/m² |
| Concreto total / AC | 0,319 m³/m² |
| Taxa aço supra (c/ tela) | 80,2 kg/m³ |
| Aço supra / AC | 20,3 kg/m² |
| Forma montagem / AC | 2,09 m²/m² |
| ML estaca / AC | 0,28 m/m² |
| Estacas / UR | 2,3 un/UR |
| Alvenaria / AC | 1,33 m²/m² |
| Forro gesso / AC | 0,59 m²/m² |
| Contrapiso / AC | 0,71 m²/m² |
| Pintura parede / AC | 1,31 m²/m² |
| Fachada / AC | 0,86 m²/m² |
| Portas / UR | 8,8 un/UR |

### Destaques

1. **Projeto MENOR** que os demais da base (4.499 m² vs 8.367-11.103 dos anteriores) — dado valioso para calibração de escala
2. **Infraestrutura R$ 344/m²** — 81% acima do topo da faixa. Solo de Navegantes (lençol freático alto) + contrato VB Geotesc
3. **Supraestrutura R$ 485/m²** — 18% abaixo do Maiori (R$ 582). Laje cubeta mais econômica em prédio menor, fck 30 vs 40
4. **CI = 16,64%** — o mais alto da base. Escala menor dilui menos (8 pessoas × 30 meses para 4.499 m²)
5. **Elevador Otis R$ 479.500** — 1 elevador para 27 UR (ratio alto)
6. **Mobiliário R$ 194/m²** — programa completo de áreas comuns puxando complementares para cima
7. **Forma/AC = 9,20** — o mais alto entre projetos comparados (vs 5-7 típico)
8. **Concreto/AC = 0,227** na comparação interna — o mais BAIXO entre projetos comparados
9. **Comparações protendido vs alv. estrutural** previstas mas dados perdidos (#REF!)
10. **Mesma construtora do Maiori** — permite comparação direta de escalas (4.499 vs 8.367 m²)

---

## COMPARATIVO CONSOLIDADO — 21 PROJETOS (R$/m²)

> Excluídos: CTN-IVC-LRJ (só regras), Fasolo VDF (data 2021 defasada), Fasolo ELS (fórmulas quebradas), Sisa Wave (misto mall+resid, distorce médias)

| Grupo | Range | Média | CV% | Status | Drivers |
|-------|-------|-------|-----|--------|---------|
| Instalações | 310-555 | 365 | 15% | ✅ Estável | EIS outlier (sprinklers 130 R$/AC) |
| Pintura | 95-187 | 125 | 18% | ✅ Estável | Padrão de textura vs acrílica |
| Impermeabilização | 43-94 | 65 | 22% | ⚠️ Moderado | CKock/Fasolo muito baixo |
| Rev. Internos | 107-222 | 145 | 22% | ⚠️ Moderado | Drywall vs reboco |
| Alvenaria | 146-324 | 200 | 23% | ⚠️ Moderado | % drywall + escala |
| Acabamentos | 135-400 | 215 | 25% | ⚠️ Moderado | Pedra, vinílico, madeira engenheirada |
| Teto | 48-151 | 85 | 32% | ❌ Variável | Forro simples vs sanca/negativo elaborado |
| Complementares | 49-995 | 240 | 80%* | ❌ Variável | Costão resort outlier; sem ele: 133-312, CV 28% |
| Esquadrias | 244-830 | 400 | 35% | ❌ Variável | PVC vs alumínio, brise, pele de vidro |
| Supraestrutura | 599-1.902 | 750 | 35% | ❌ Variável | Laje (cubetas/protendida/maciça) + NPT |
| Fachada | 138-546 | 210 | 40% | ❌ Variável | Pedra natural, concreto aparente |
| Sist. Especiais | 89-748 | 230 | 55% | ❌ Variável | Sprinklers, VRF, piscinas, solar |
| Gerenciamento | 307-1.984 | 550 | 60% | ❌ Variável | Padrão + escala + meses + equipe |

*Costão Complementares = R$ 995/m² (resort com R$ 38M em infraestrutura). Excluindo: média 225, CV 28%.

### Faixas de CUB ratio (21 projetos)

| Faixa | CUB ratio | Projetos | Padrão |
|-------|-----------|----------|--------|
| Econômico | 1,07-1,18 | Zapata, Catena, 2cinco4, Cota365 | Médio a Alto, >10k m² |
| Padrão SC | 1,28-1,39 | D'Lohn, MP298, Eternity, Lorenzo, Connect, Passione, Passione, Viva | Alto, 5-13k m² |
| Premium SC | 1,47-1,67 | Redentor, Campeche, Neuhaus, Sisa Wave | Alto grande porte ou diferenciado |
| Super Alto BC | 2,17-3,39 | Monolyt, Aquos | Bal. Camboriú, acabamento topo |
| Hotel/Resort | 2,99-4,24* | Colline Hotel, Costão* | Sistemas complexos (VRF, etc.) |

### Insights consolidados (25 projetos):

1. **Instalações continuam o MAIS estável** — range 310-555 R$/AC (expandido pelo EIS com sprinklers). Sem EIS: 310-431 com CV ~10%. Default seguro para qualquer paramétrico.

2. **Supraestrutura: protensão dilui com NPT:**
   - Cubetas (8+ projetos): 599-821 R$/m² — faixa estreita, previsível
   - Protendida: 636-979 R$/m² para NPT≥10 (boa diluição), até 1.902 para NPT=3 (Aquos)
   - Maciça (Colline): 704-768 R$/m² — competitiva com cubetas
   - **Regra de ouro:** Cubetas é o default mais seguro. Protendida só compensa com NPT≥10.

3. **DNA por construtora confirmado com mais dados:**
   - **CKock:** impermeab ~46, teto ~48, fachada ~138 (os mais baixos)
   - **Meia Praia (3 projetos):** supraestrutura 607-765, instalações 349-354, fachada 193-236 — DNA Itapema consistente
   - **Blue Heaven:** 2-3x mais caro que padrão SC em tudo (acabamento extremo)
   - **Pass-e:** Connect ~3.584, Passione ~3.778 — faixa 1,29-1,36 CUB

4. **Floripa tem contenção cara:**
   - Cota 365: 182 R$/m², D'Lohn: 91, Campeche: 190, EIS: 207
   - vs Itapema/Porto Belo: 0-72 R$/m²
   - **Regra:** Projeto em Floripa → somar 100-200 R$/m² de contenção

5. **Escala importa exponencialmente para gerenciamento:**
   - <5k m²: 544-702 R$/m² (Passione, Campeche, Viva, EIS)
   - 5-15k m²: 322-496 R$/m² (maioria)
   - >15k m²: 307-371 R$/m² (2cinco4, Redentor, Sisa)
   - Aquos outlier: 1.984 R$/m² (escala pequena + super alto + equipe premium)

6. **PVC esquadrias aparece em 2 projetos:**
   - Viva Perequê: 0,14 m²/AC (PVC + pele de vidro)
   - Colline: 1.626 R$/m² (standard), 3.253 R$/m² (arredondada)
   - Tendência? Monitorar se mais projetos adotam PVC.

7. **Sprinklers (EIS):** 130 R$/AC é custo significativo — eleva instalações de ~350 para ~555. Briefing deve perguntar se o projeto exige sprinkler (normalmente >30m ou >750m²/pav).

8. **Elevadores: preço por parada vs unitário:**
   - Formato novo: 244k-486k por unidade (escala de preço por NP)
   - Formato antigo: 13,5k-20k por NP (parada)
   - EIS e Connect: elevadores mais caros (486k Connect — 20 pav)

9. **Complementares têm padrão previsível se excluir outliers:**
   - Mobiliário lazer: 1.500-2.500 R$/AL (média 1.850)
   - Paisagismo: 5-65 R$/AC (média 18 excluindo Neuhaus=65 e Costão resort)
   - Limpeza: 6,5-20 R$/AC (média 15)
   - Comunicação visual: 7-25 R$/AC (média 10)

10. **Costão do Santinho é caso à parte** — resort com infraestrutura própria (R$ 38M complementares). Não usar como referência para residencial padrão.

---

## COMPARATIVO HISTÓRICO — 4 PROJETOS INICIAIS (R$/m²)

> **Nota:** Tabela mantida para referência histórica. Ver "COMPARATIVO CONSOLIDADO — 21 PROJETOS" acima para dados atualizados.

| Grupo | 2cinco4 (11k m²) | San Felice (7,5k m²) | Campeche* (3,6k m²) | Monolyt (14,7k m²) | Média | CV% | Obs |
|-------|---------|-----------|----------|---------|-------|-----|-----|
| Gerenciamento | 307 | 423 | 702 | 989 | 605 | 48% | Escala + padrão (Monolyt super alto) |
| Supraestrutura | 661 | 599 | 799 | 1.154 | 803 | 30% | Protendida (Monolyt) >> Cubetas |
| Instalações | 327 | 323 | 378 | 422 | 363 | 13% | *Relativamente estável* ✅ |
| Esquadrias | 417 | 244 | 380 | 640 | 420 | 38% | Padrão das esquadrias varia muito |
| Alvenaria | 154 | 208 | 146 | 214 | 181 | 20% | Drywall puxa pra cima |
| Sist. Especiais | 215 | 152 | 192 | 492 | 263 | 58% | Piscinas+solar Monolyt é outlier |
| Impermeabilização | 73 | 74 | 80 | 86 | 78 | 7% | *Muito estável* ✅ |
| Rev. Internos | 201 | 140 | 222 | 119 | 171 | 27% | Monolyt: mais drywall = menos reboco |
| Teto | 74 | 100 | 83 | 120 | 94 | 21% | *Relativamente estável* ✅ |
| Acabamentos | 200 | 193 | 253 | 293 | 235 | 19% | Madeira engenheirada puxa pra cima |
| Pintura | 171 | 140 | 187 | 156 | 164 | 12% | *Estável* ✅ |
| Fachada | 154 | 174 | 184 | 210 | 181 | 13% | *Estável* ✅ |
| Complementares | 184 | 234 | 266 | 240 | 231 | 14% | *Estável* ✅ |
| Imprevistos | 92 | 84 | 74 | 174 | 106 | 45% | ~3% do total |
| Mov. Terra | 22 | 22 | 85 | 173 | 76 | 96% | Depende de subsolo e terreno |
| Contenção | — | — | 191 | 112 | 151 | — | Depende do tipo |
| **TOTAL** | **3.457** | **3.292** | **4.491** | **5.988** | **4.307** | — | — |

*Campeche: sem mob. privativo

### Insights com 4 projetos:

1. **Índices estáveis (CV < 15% — usar como default):**
   - Impermeabilização: 73-86 R$/m² (média 78, CV 7%) ✅
   - Pintura: 140-187 R$/m² (média 164, CV 12%) ✅
   - Instalações: 323-422 R$/m² (média 363, CV 13%) ✅
   - Fachada: 154-210 R$/m² (média 181, CV 13%) ✅
   - Complementares: 184-266 R$/m² (média 231, CV 14%) ✅

2. **Índices moderadamente variáveis (CV 15-25% — ajustar com briefing):**
   - Acabamentos: 193-293 R$/m² (média 235, CV 19%) — depende do tipo de piso
   - Alvenaria: 146-214 R$/m² (média 181, CV 20%) — drywall vs alvenaria
   - Teto: 74-120 R$/m² (média 94, CV 21%) — negativo e sancas puxam

3. **Índices muito variáveis (CV > 25% — obrigatório perguntar):**
   - Supraestrutura: 599-1.154 R$/m² — tipo de laje muda tudo
   - Esquadrias: 244-640 R$/m² — padrão e pele de vidro
   - Gerenciamento: 307-989 R$/m² — escala + padrão + equipe
   - Sist. Especiais: 152-492 R$/m² — piscinas, solar, elevadores
   - Mov. Terra: 22-173 R$/m² — subsolo e terreno

4. **Laje protendida vs cubetas:**
   - Cubetas: 599-799 R$/m² (média ~687)
   - Protendida: 1.154 R$/m² (1 ponto, mas ~68% mais caro)
   - Diferença se explica: protensão (R$ 35/kg × 62t = R$ 2,37M extra)

5. **Super alto padrão BC (Monolyt) vs Alto padrão SC:**
   - Total: 5.988 vs 3.300-4.500 R$/m²
   - Drivers: esquadrias (+R$ 260/m²), sist. especiais (+R$ 300/m²), supraestrutura (+R$ 350/m²), gerenciamento (+R$ 300/m²)

---

## COMPARATIVO ENTRE OS 3 PROJETOS (R$/m² — sem mob. privativo)

| Grupo | 2cinco4 | San Felice | Campeche | Média | Obs |
|-------|---------|-----------|----------|-------|-----|
| Gerenciamento | 307 | 423 | 702 | 477 | Escala: quanto menor o prédio, maior |
| Supraestrutura | 661 | 599 | 799 | 686 | Cubetas nos 3; Campeche menor = menos diluição |
| Instalações | 327 | 323 | 378 | 343 | *Relativamente estável* ✅ |
| Esquadrias | 417 | 244 | 380 | 347 | Depende de pele de vidro e padrão |
| Alvenaria | 154 | 208 | 146 | 169 | SF tem mais drywall |
| Sistemas Especiais | 215 | 152 | 192 | 186 | Escala dos equipamentos |
| Impermeabilização | 73 | 74 | 80 | 76 | *Muito estável* ✅ |
| Rev. Internos | 201 | 140 | 222 | 188 | Campeche: mais reboco |
| Teto | 74 | 100 | 83 | 86 | *Estável* ✅ |
| Acabamentos | 200 | 193 | 253 | 215 | Varia com tipo de piso |
| Pintura | 171 | 140 | 187 | 166 | Campeche: epóxi garagem |
| Fachada | 154 | 174 | 184 | 171 | *Relativamente estável* ✅ |
| Complementares | 184 | 234 | 266 | 228 | Lazer relativo à AC |
| Imprevistos | 92 | 84 | 74 | 83 | ~3% consistente |
| Mov. Terra | 22 | 22 | 85 | 43 | Subsolo puxa pra cima |
| Cobertura | 72 | — | 44 | 58 | Muito variável |
| **TOTAL** | **3.457** | **3.292** | **4.491** | **3.747** | — |

### Insights do Comparativo com 3 projetos:

1. **Índices estáveis (confiáveis pra qualquer projeto):**
   - Impermeabilização: 73-80 R$/m² (média 76)
   - Teto: 74-100 R$/m² (média 86)
   - Instalações: 323-378 R$/m² (média 343)
   - Fachada: 154-184 R$/m² (média 171) — sem acabamentos especiais

2. **Efeito de escala comprovado:**
   - Gerenciamento: 307 (11k m²) → 423 (7,5k m²) → 702 (3,6k m²) — relação inversa clara
   - Supraestrutura: mesma tendência
   - Regra: custos fixos (equipe, equipamentos) diluem mais em obras maiores

3. **Subsolo impacta muito a movimentação de terra:**
   - Sem subsolo: ~22 R$/m²
   - Com 1 subsolo: 85 R$/m² (4x mais)

4. **Contenção varia por tipo:**
   - 2cinco4: cortina de estacas
   - Campeche: parede diafragma (190 R$/m²)
   - San Felice: não aparece como grupo separado

---

## PUs DEFAULT PARA NOVOS PARAMÉTRICOS (base 25 projetos, data-base ~2024-2025)

> **Instrução:** Usar estes valores como ponto de partida. Ajustar pelos drivers indicados e pelo briefing do projeto.
> **Referência de arquivo detalhado:** `archive/PUs-NOVOS-PROJETOS.md`

### Supraestrutura — Default por tipo de laje

| Parâmetro | Cubetas | Protendida (NPT≥10) | Protendida (NPT<10) | Maciça |
|-----------|---------|---------------------|---------------------|--------|
| Concreto (m³/AC) | 0,25 | 0,25 | 0,25 | 0,20 |
| Armadura (kg/m³) | 100-110 | 90-110 | 90-110 | 90-100 |
| MO Estrutura (R$/AC) | 240 | 240 | 240 | 210 |
| Cubetas/Protensão | 25 R$/AC | 12,30 R$/m² mat + 2,83 kg/m² cabos + 9.000/pav serv | idem | — |
| Forma (jogos) | 2-3 | 2-3 | 2-3 | 2-4 |
| R$/m² esperado | 600-820 | 636-980 | 1.000-1.900 | 700-770 |

### Instalações — Default R$/AC (padrão alto SC)

| Subitem | Default | Range (21 proj) | Obs |
|---------|---------|-----------------|-----|
| Entrada Energia | 5,5 | 2,65-30 | Connect outlier (30) |
| Eletrodutos | 10-12 | 8-17 | |
| Cabos/Fiações | 30 | 25-40 | |
| Quadros/Disjuntores | 15-18 | 6-22 | |
| Acabamentos Elétricos | 12-15 | 10-20 | |
| Equipamentos/Iluminação | 15 | 2-21 | |
| MO Elétrica | 60 | 45-70 | |
| Água Fria | 22-25 | 15-32 | |
| Água Quente | 20 | 7,5-32 | |
| Pluviais | 10 | 4-12 | |
| Sanitárias | 15 | 8-16 | |
| Louças/Metais | 35 | 5-50 | D'Lohn/Neuhaus premium |
| MO Hidráulica | 55 | 40-55 | |
| Preventivas | 20 | 9,5-25 | +130 se sprinkler! |
| GLP | 15 | 5-22 | |
| SPDA | 8 | 4-10 | |
| **Total Instalações** | **350-380** | **310-555** | |

### Esquadrias — Default

| Item | Default | Range | Obs |
|------|---------|-------|-----|
| Alumínio (m²/AC) | 0,15 | 0,11-0,20 | Motorizado=0,11, EIS=0,20 |
| PVC (m²/AC) | 0,14 | — | Só Viva e Colline |
| Serralheria (R$/AC) | 10 | 2-10 | Ou VB (80-350k) nos antigos |
| GC Alumínio/Vidro (R$/m²) | 950-2.100 | 600-2.100 | |
| Brise (R$/m²) | 1.000-1.600 | 750-2.000 | |
| Porta Madeira (R$/un) | 900-3.000 | 80 R$/AC-3.000/un | |

### Sistemas Especiais — Default

| Item | Default | Range | Obs |
|------|---------|-------|-----|
| Infra AC (R$/ponto) | 1.200-1.500 | 1.200-1.500 | Antigos: 25-40 R$/AC |
| AC instalado (R$/un) | 5.000 | 5.000-6.000 | |
| Churrasqueira (R$/un) | 2.600 | 280-4.000 | D'Lohn=280 (só ponto gás) |
| Ventokit (R$/un) | 900 | 900-1.200 | |
| Elevador (R$/un) | 365.000 | 244k-486k | Escala com NP |
| CFTV (R$/AC) | 2 | 1,5-5 | |
| Interfone (R$/AC) | 5 | 2-9 | |
| TV/Internet (R$/AC) | 3-6 | 3-12 | |
| Automação/Segurança (R$/AC) | 5 | 5-8 | |
| Infra carro elétrico (R$/vaga) | 560 | 547-800 | |
| Gerador (R$/un) | 42.000-120.000 | 20k-209k | Escala com porte |
| Piscina (R$/un) | 25.000 | 25k-270k | Aquecida=muito mais |
| Sauna (R$/un) | 8.000 | 7.980-75k | |

### Impermeabilização — Default

| Item | Default | Range | Obs |
|------|---------|-------|-----|
| Regularização (R$/m²) | 25 | 6-25 | |
| Poço elevador (R$/m²) | 45 | 30-45 | |
| Baldrames (R$/m²) | 30 | 30-40 | |
| Ralos (R$/AC) | 1 | 0,25-2,8 | |
| Cimentícias (m²/AC) | 0,25-0,30 | 0,15-0,30 | |
| Manta asfáltica (m²/AC) | 0,10-0,16 | 0,05-2,97 | |
| Peitoril (R$/AC) | 0,6-1,2 | 0,6-1,3 | |
| Proteção mecânica (R$/m²) | 28 | 12-80 | |

### Complementares — Default

| Item | Default | Range | Obs |
|------|---------|-------|-----|
| Mobiliário/Decoração | 1.750 R$/AL | 50 R$/AC - 2.500 R$/AL | Costão=2.500 |
| Comunicação Visual (R$/AC) | 10 | 7-25 | |
| Paisagismo (R$/AC) | 15 | 5-65 | Neuhaus=65 outlier |
| Ligações definitivas (R$/AC) | 4 | 4-15 | |
| Limpeza (R$/AC) | 15 | 6,5-20 | |
| Desmobilização (R$/AC) | 5 | 2-5 | |

### Gerenciamento — Modelo por AC

| Faixa AC (m²) | R$/m² esperado | Obs |
|---------------|----------------|-----|
| < 5.000 | 544-702 | Escala pequena, custos fixos pesam |
| 5.000 - 10.000 | 400-550 | Faixa padrão |
| 10.000 - 20.000 | 307-496 | Boa diluição |
| > 20.000 | 307-371 | Excelente diluição |
| Super alto padrão | +50-100% sobre a faixa | Equipe premium, mais equipamentos |

---

## DADOS DE ENTRADA — PROJETO 2: 2cinco4 Edition

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Área do Terreno | AT | 1.127,10 | m² |
| Área Construída | AC | 11.218,19 | m² |
| Unidades Residenciais | UR | 44 | un |
| Unidades Comerciais | UC | 9 | un |
| Churrasqueiras | CHU | 46 | un |
| Nº Total Pavimentos | NP | 27 | un |
| Nº Pavimentos Tipo | NPT | 21 | un |
| Nº Pav. Tipo Diferenciados | NPD | 1 | un |
| Área Projeção Torre | APT | 309,43 | m² |
| Perímetro Projeção Torre | PPT | 76,88 | m |
| Área de Lazer | AL | 730,76 | m² |
| Área Embasamento | AE | 3.907,21 | m² |
| Área Projeção Embasamento | APE | 981,89 | m² |
| Perímetro Projeção Embasamento | PE | 161,88 | m |
| Nº Pav. Embasamento | NE | 4 | un |
| Meses de Obra | — | 52 | meses |
| CUB/SC referência | — | 2.934,53 | R$/m² |

---

## CUSTOS DIRETOS — 2cinco4 Edition (R$ — Jun/2024)

### Resumo por Grupo

| Grupo | Valor (R$) | R$/m² | % |
|-------|-----------|-------|---|
| Supraestrutura (Cubetas) | 7.413.979 | 660,89 | 19,1% |
| Esquadrias, Vidros, Ferragens | 4.674.216 | 416,66 | 12,1% |
| Instalações (Elét+Hidro+Prev) | 3.668.348 | 327,00 | 9,5% |
| Gerenciamento Técnico e Admin. | 3.445.019 | 307,09 | 8,9% |
| Sistemas Especiais | 2.414.995 | 215,27 | 6,2% |
| Rev. Argamassados Piso/Parede | 2.253.069 | 200,84 | 5,8% |
| Acabamentos Piso/Parede | 2.239.443 | 199,63 | 5,8% |
| Infraestrutura | 2.050.376 | 182,77 | 5,3% |
| Complementares | 2.061.540 | 183,77 | 5,3% |
| Pintura Interna | 1.922.072 | 171,34 | 5,0% |
| Alvenaria | 1.725.490 | 153,81 | 4,4% |
| Fachada | 1.723.630 | 153,65 | 4,4% |
| Imprevistos (3%) | 1.029.289 | 91,75 | 2,7% |
| Teto | 826.118 | 73,64 | 2,1% |
| Impermeabilização | 823.318 | 73,39 | 2,1% |
| Cobertura | 278.818 | 24,85 | 0,7% |
| Movimentação de Terra | 234.239 | 20,88 | 0,6% |
| **TOTAL** | **38.783.958** | **3.457,24** | **100%** |
| **TOTAL (s/ Gerenciamento)** | **35.338.939** | **3.150,15** | — |
| **Razão CUB** | — | **1,18 CUB** | — |

---

## DADOS DE ENTRADA — PROJETO 10/11: Colline de France (CTN-COLLINE)

> **Tipo:** Hotel + Residencial (empreendimento misto — PRIMEIRO HOTEL na base)
> **Localização:** Miguel Pereira/RJ (PRIMEIRO PROJETO NO RIO DE JANEIRO)
> **Data-base:** Mar/2025 | **CUB/RJ:** R$ 2.303,36
> **Meses de obra:** 36 (hotel 24, residencial 36)

### Dados Gerais

| Variável | Hotel | Residencial | Total |
|----------|-------|-------------|-------|
| AC (m²) | 6.049 | 21.510 | 27.559 |
| UR/Quartos | 36 quartos | 60 unid | 96 |
| NP (pavimentos) | 5 | 23 | 28 |
| NPT (tipo) | 0 | 13 | 13 |
| NPD (diferenciados) | 3 | 1 | 4 |
| ND (duplex) | 0 | 1 | 1 |
| AT (m²) | — | — | 6.049 |
| APT (m²) | 1.022 | 739 | 1.761 |
| PPT (m) | 151 | 203 | 354 |
| AL (lazer) (m²) | 0 | 2.513 | 2.513 |
| AE (embasamento) (m²) | 1.676 | 7.367 | 9.042 |
| APE (proj. embas.) (m²) | 2.087 | 2.366 | 4.453 |
| NS (subsolos) | 1 | 0 | 1 |
| CHU (churrasqueiras) | 0 | 60 | 60 |
| Elevadores | 3 (4 paradas) | 6 (25 paradas) | 9 |
| Meses | 24 | 36 | — |
| Tipo laje | Maciça | Maciça | — |

### Custos por Grupo (R$ — Mar/2025)

| Grupo | Hotel (R$) | R$/m² Hotel | Resid (R$) | R$/m² Resid | Total (R$) | R$/m² Total |
|-------|-----------|-------------|------------|-------------|-----------|-------------|
| Gerenciamento | — | — | — | — | 13.604.538 | 494 |
| Mov. Terra | 137.246 | 23 | 150.402 | 7 | 287.648 | 10 |
| Infraestrutura | 2.200.958 | 364 | 4.184.720 | 195 | 6.385.677 | 232 |
| Supraestrutura | 4.644.537 | 768 | 15.149.858 | 704 | 19.794.394 | 718 |
| Paredes/Painéis | 2.968.838 | 491 | 6.993.313 | 325 | 9.962.150 | 361 |
| Instalações | 3.789.528 | 626 | 9.279.750 | 431 | 13.069.278 | 474 |
| Sist. Especiais | 6.534.262 | 1.080 | 5.166.429 | 240 | 11.700.691 | 425 |
| Impermeabilização | 493.452 | 82 | 1.276.413 | 59 | 1.769.866 | 64 |
| Rev. Internos | 2.569.648 | 425 | 2.958.540 | 138 | 5.528.188 | 201 |
| Teto | 831.200 | 137 | 2.442.172 | 114 | 3.273.372 | 119 |
| Pisos/Pavimentações | 3.231.122 | 534 | 7.331.642 | 341 | 10.562.764 | 383 |
| Pintura | 890.238 | 147 | 3.699.800 | 172 | 4.590.037 | 167 |
| Esquadrias | 10.170.063 | 1.681 | 17.129.486 | 796 | 27.299.549 | 991 |
| Cobertura | 1.393.694 | 230 | 1.138.286 | 53 | 2.531.981 | 92 |
| Fachada | 1.254.678 | 207 | 3.653.145 | 170 | 4.907.823 | 178 |
| Complementares | 564.004 | 93 | 6.972.618 | 324 | 7.536.622 | 273 |
| **TOTAL** | **41.673.467** | **6.889** | **87.526.573** | **4.069** | **142.804.578** | **5.182** |
| **CUB ratio** | — | **2,99** | — | **1,77** | — | **2,25** |

### Custos Indiretos — Colline (R$ 13,6M = 494 R$/m²)

| Subgrupo | Valor (R$) | Obs |
|----------|-----------|-----|
| Ger. Técnico (estudos, projetos, taxas) | 4.293.333 | Inclui R$ 2,5M em licenciamentos/taxas/impostos + outorga |
| Seg. Trabalho + EPCs | 1.572.839 | 2 técnicos seg. R$7k/mês, EPCs hotel + resid separados |
| Equipe Hotel (24 meses) | 1.185.234 | Eng R$12k, almox R$4,2k, mestre R$8,4k, 2 estag R$3k, vigil. R$15,3k, grua oper. R$15,6k |
| Equipe Resid (36 meses) | 2.264.911 | Eng Sr R$18k, aux eng R$5k, almox R$4,2k, 2 mestres R$16,7k, vigil. R$15,3k, grua oper. R$15,6k |
| Canteiro + Instalações | 591.609 | Galpão R$276k, banheiros R$171k |
| Consumo e Manutenção | 619.198 | |
| Equipamentos | 2.995.861 | 1 grua resid R$501k loc + R$81k ascensão, 2 cremalheiras resid R$1M, 1 crem hotel R$200k, balancim R$148k, andaime R$415k |

### Particularidades do Colline (insights únicos)

1. **Empreendimento misto Hotel + Residencial** — custos muito diferentes por m²:
   - Hotel: R$ 6.889/m² (2,99 CUB) — padrão super alto, complexidade de sistemas
   - Residencial: R$ 4.069/m² (1,77 CUB) — alto padrão
2. **Localização: Rio de Janeiro** — CUB/RJ R$ 2.303 (vs CUB/SC ~R$ 2.900-3.000)
3. **Laje MACIÇA** — primeiro projeto com laje maciça na base (todos anteriores eram cubetas ou protendida)
   - Resid: concreto 0,20 m³/AC, armadura 100 kg/m³, forma 4 jogos, MO 210 R$/AC
   - Hotel: concreto 0,20 m³/AC, armadura 90 kg/m³, forma 2 jogos, MO 210 R$/AC
4. **Esquadrias PVC** (não alumínio!) — R$ 1.626/m² (standard) e R$ 3.253/m² (arredondadas)
   - Gradil elaborado: R$ 2.443/m (externo), R$ 3.053/m (sacada), R$ 7.641/m (interno)
   - Esquadrias madeira isolantes hotel: R$ 9.662/un (isolamento acústico/térmico)
5. **Hotel — climatização VRF:** R$ 210/AC (infra) + condensadoras R$ 132.780/un × 16 = R$ 2,3M
   - Exaustão cozinha hotel: R$ 603.450 (industrial)
   - Aspiração central hotel: 21,5 R$/AC
   - Banheiras de imersão hotel: R$ 9.320/un × 27
6. **Chafariz** R$ 110k, espelho d'água R$ 25k
7. **Cobertura:** Telhamento Shingle R$ 198/m² + estrutura metálica R$ 131/m² + MO R$ 644/m² (inclinação ~56° = ×3,35 sobre telhado convencional)
8. **Paredes:** Drywall dominante (0,90 m²/AC a R$ 191/m²) + alvenaria só para externo, escadas e refratárias
9. **Fachada elaborada:** Molduras (pilares/paredes) com chapisco+reboco R$ 34/m² + MO R$ 130/m², pintura molduras R$ 12/m² + MO R$ 200/m², beiral 2.589 m × R$ 38/m
10. **Custos indiretos proporcionalmente altíssimos:** R$ 494/m² (vs média base SC ~350-500 R$/m²), puxado por licenciamentos/taxas/outorga RJ
11. **Elevadores:** Hotel 3 × R$ 151.569 (4 paradas) vs Residencial 6 × R$ 370k média (25 paradas!)

### PUs Detalhados — RESID

#### Supraestrutura (Laje Maciça)
| Item | Parâmetro | PU | Total (R$) |
|------|-----------|-----|-----------|
| Fabricação forma | 4 jogos | 110 R$/m² | 891.369 |
| Montagem forma | 2,5 m²/AC | 2,50 R$/m² | 116.486 |
| Escoramento | 4 un/AE | 17 R$/un | 752.301 |
| Concreto | 0,20 m³/AC | 558 R$/m³ | 3.643.837 |
| Armadura conv. | 100 kg/m³ | 7,62 R$/kg | 4.739.040 |
| MO estrutura | 210 R$/AC | — | 4.968.875 |
| **Total** | | | **15.149.858 (704 R$/AC)** |

#### Instalações RESID
| Subgrupo | R$/AC | Total (R$) |
|----------|-------|-----------|
| Entrada energia | 5,5 | 130.137 |
| Eletrodutos | 18 | 425.904 |
| Cabos/fiações | 30 | 709.839 |
| Quadros/disjuntores | 15 | 354.920 |
| Acabam. elétricos | 12 | 283.936 |
| Equip/iluminação | 5 | 118.307 |
| Gerador | vb | 185.000 |
| Subestação | vb | 310.000 |
| Infra carro elétrico | 60 × 547 | 36.102 |
| MO elétrica | 65 | 1.537.985 |
| **Subtotal Elétrica** | **~190** | **4.092.129** |
| Água fria | 22 | 520.549 |
| Água quente | 20 | 473.226 |
| Águas pluviais | 10 | 236.613 |
| Sanitárias | 17 | 402.242 |
| Hidrômetro | 1 | 23.661 |
| Bombas pressurização | 4 × 22.500 | 99.000 |
| Bombas recalque | 2 × 6.800 | 14.960 |
| Est. redutora pressão | 4 × 5.240 | 23.056 |
| MO hidráulica | 55 | 1.301.372 |
| **Subtotal Hidro** | **~144** | **3.094.680** |
| Louças | 20 R$/AC + 214 bacias × R$ 1.683 | — | 400.063 + 360.186 |
| Metais | 16 | 378.581 |
| Bancadas/pias | 22 × 3.500 | — | 77.000 |
| MO louças | 10 | 236.613 |
| **Subtotal Louças/Metais** | **~51** | **1.092.257** |
| Prev. hidrantes | 5 | 118.307 |
| Bombas prev. | 2 × 22.500 | — | 49.500 |
| Sinalização | 4,5 | 106.476 |
| Alarme | 2,5 | 59.153 |
| SPDA | 10 | 236.613 |
| MO preventivo | 8 | 189.290 |
| GLP | 7,2 | 170.361 |
| MO GLP | 3 | 70.984 |
| **Subtotal Prev+GLP** | **~47** | **1.000.685** |
| **TOTAL INSTALAÇÕES** | **431** | **9.279.750** |

#### Esquadrias RESID
| Item | Qtd | PU | Total (R$) |
|------|-----|-----|-----------|
| Contramarco | 7.097 m | 44 R$/m | 343.642 |
| MO contramarco | 7.097 m | 22 R$/m | 171.743 |
| PVC standard | 5.391 m² | 1.626 R$/m² | 9.644.217 |
| PVC arredondada | 411 m² | 3.253 R$/m² | 1.470.053 |
| Pele de vidro | 113 m² | 1.100 R$/m² | 136.294 |
| Portão alumínio | 1 un | 18.000 R$/un | 19.800 |
| Guarda-corpo vidro | 223 m | 1.045 R$/m | 256.833 |
| Gradil | 905 m | 2.443 R$/m | 2.430.654 |
| Corrimão inox | 104 m | 150 R$/m | 17.130 |
| Corrimão escada | 729 m | 120 R$/m | 96.162 |
| Serralheria | 5 R$/AC | — | 118.307 |
| PCF | 92 un | 1.850 R$/un | 187.220 |
| Fechadura biométrica | 60 un | 1.445 R$/un | 95.381 |
| Portas alumínio | 72 un | 850 R$/un | 67.320 |
| Esquadrias madeira | 773 un | 2.300 R$/un | 1.955.690 |
| MO portas | 773 un | 140 R$/un | 119.042 |
| **TOTAL** | | | **17.129.486 (796 R$/AC)** |

#### Esquadrias HOTEL
| Item | Qtd | PU | Total (R$) |
|------|-----|-----|-----------|
| Alumínio fachada | 2.143 m² | 3.253 R$/m² | 6.971.175 |
| Alumínio internas | 429 m² | 1.462 R$/m² | 626.675 |
| Gradil externo | 161 m | 2.062 R$/m | 331.250 |
| Gradil sacada | 73 m | 3.053 R$/m | 244.847 |
| Gradil interno | 43 m | 7.641 R$/m | 331.250 |
| Guarda-corpo balustre | 133 m | 1.310 R$/m | 173.688 |
| Madeira isolante | 38 un | 9.662 R$/un | 403.876 |
| Madeira standard | 73 un | 6.725 R$/un | 540.038 |
| Madeira correr | 4 un | 11.863 R$/un | 52.197 |
| Fechadura biométrica | 36 un | 1.445 R$/un | 52.026 |
| PCF | 10 un | 1.850 R$/un | 20.350 |
| **TOTAL** | | | **10.170.063 (1.681 R$/AC hotel)** |

#### Sistemas Especiais HOTEL (R$ 6,7M = 1.113 R$/AC)
| Item | Qtd | PU | Total (R$) |
|------|-----|-----|-----------|
| Infra AC VRF | 6.049 AC | 210 R$/AC | 1.397.358 |
| Evaporadoras | 85 un | 2.582 R$/un | 241.417 |
| Condensadoras VRF | 16 un | 132.780 R$/un | 2.336.928 |
| UTA | 4 un | 32.915 R$/un | 144.826 |
| Exaustão cozinha | 1 vb | 603.450 | 663.795 |
| Exaustão banheiros | 38 un | 1.100 R$/un | 45.980 |
| Hydrokit | 5 un | 38.500 R$/un | 192.500 |
| Elevadores 4 par. | 3 un | 151.569 R$/un | 500.179 |
| Banheira imersão | 27 un | 9.320 R$/un | 276.804 |
| Aspiração central | 6.049 AC | 21,5 R$/AC | 143.063 |
| Aquecimento piso | 188 m² | 280 R$/m² | 57.924 |
| Chafariz | 1 un | 110.000 | 110.000 |
| Piscina | 2+2 priv | 38.181+25.300 | 139.659 |
| Outros | 30 R$/AC | — | 199.623 |

#### Sistemas Especiais RESID (R$ 5,2M = 240 R$/AC)
| Item | Qtd | PU | Total (R$) |
|------|-----|-----|-----------|
| Infra AC | 455 un | 1.500 R$/un | 750.750 |
| AC split | 4 un | 3.000 R$/un | 13.200 |
| AC cassete | 16 un | 14.400 R$/un | 253.440 |
| VAE | 44 un | 2.500 R$/un | 121.000 |
| Exaustão garagem | 45 un | 2.300 R$/un | 113.850 |
| Coifa | 60 un | 950 R$/un | 62.700 |
| Churrasqueiras | 62 un | 4.200 R$/un | 286.440 |
| Elevadores 25 par. | 4 soc × 392k + 2 × 327k | — | 2.444.333 |
| Aquecimento piso | 650 m² | 280 R$/m² | 200.079 |
| Piscina lazer | 5 un | 36.831 R$/un | 202.572 |
| Piscina privativa | 4 un | 25.300 R$/un | 111.320 |
| Sauna | 2 un | 8.500 R$/un | 18.700 |
| Hidromassagem | 2 un | 24.980 R$/un | 54.956 |

#### Impermeabilização RESID (R$ 1,28M = 59 R$/AC)
| Item | Parâmetro | PU | Total (R$) |
|------|-----------|-----|-----------|
| Regularização | 25 R$/m² | 22 R$/m² | 240.843 |
| Poço elevador | 45 R$/m² | 41 R$/m² | 5.163 |
| Baldrames | 30 R$/m² | 35 R$/m² | 80.488 |
| Ralos | 0,4 R$/AC | — | 9.465 |
| Cimentícia | 0,35 m²/AC | 60 R$/m² | 451.716 |
| Manta asfáltica | 0,10 m²/AC | 150 R$/m² | 399.895 |
| Peitoril | 0,6 R$/AC | — | 14.197 |
| Proteção mecânica | — | 28 R$/m² | 74.647 |

#### Fachada RESID (R$ 3,65M = 170 R$/AC)
| Item | Qtd (m²) | PU | Total (R$) |
|------|----------|-----|-----------|
| Chapisco | 13.476 | 7,50 R$/m² | 111.180 |
| Reboco | 13.476 | 17 R$/m² | 252.007 |
| MO reboco | 13.476 | 65 R$/m² | 963.557 |
| Molduras chapisco+reboco | 1.847 | 34,30 R$/m² | 69.691 |
| MO molduras | 1.847 | 130 R$/m² | 264.136 |
| Textura | 13.476 | 25 R$/m² | 370.599 |
| MO textura | 13.476 | 52 R$/m² | 770.846 |
| Pintura molduras | 2.014 | 12 R$/m² | 26.585 |
| MO pintura molduras | 2.014 | 200 R$/m² | 443.079 |
| Beiral | 2.589 m | 38 R$/m | 108.214 |
| Acabamentos especiais | — | — | 176.654 |

#### Complementares RESID (R$ 6,97M = 324 R$/AC)
| Item | Parâmetro | PU | Total (R$) |
|------|-----------|-----|-----------|
| Calçadas/passeios | 301 m² | 180 R$/m² | 59.530 |
| Móveis/decoração | 2.513 AL | 1.800 R$/AL | 4.976.532 |
| Comunicação visual | 10 R$/AC | — | 236.613 |
| Paisagismo | 12 R$/AC | — | 283.936 |
| Irrigação/ilum/mob ext. | 15 R$/AC | — | 354.920 |
| Playground | 311 m² | 930 R$/m² | 318.041 |
| Pet place | 80 m² | 744 R$/m² | 65.063 |
| Quadra poliesportiva | 45 m² | 550 R$/m² | 27.298 |
| Ligações definitivas | 4 R$/AC | — | 94.645 |
| Desmobilização | 3,5 R$/AC | — | 82.815 |
| Limpeza | 20 R$/AC | — | 473.226 |

---

## ÍNDICES DETALHADOS — 2cinco4 (CUBETAS)

### Supraestrutura — Laje Cubetas (escolhida)

| Item | Índice | Un | PU (R$) | Obs |
|------|--------|----|---------|-----|
| Fabricação forma | 3 jogos | m² | 110,00 | |
| Montagem forma | 2,1 | m²/AC | 2,50 | Índice Atlantia |
| Escoramento | 0,28 | un/m² | 11,51 | |
| Cubetas (locação) | 10 meses | mês | 12.541,50 | 929 un |
| Concreto | 0,28 | m³/AC | 610,05 | Índice Atlantia |
| Armadura | 75 | kg/m³ | 5,95 | Índice Atlantia |
| MO estrutura | 240 | R$/AC | empreitada | MO empreitada Atlantia |
| Perfuração vigas | 4.240 | R$/NP | — | Orig. Gran Torino |

### Supraestrutura — Comparativo de Variantes (2cinco4)

| Item | Maciça | Cubetas | Treliçada | Protendida |
|------|--------|---------|-----------|------------|
| Concreto (m³/AC) | 0,22 | 0,28 | 0,25 | 0,25 |
| Armadura (kg/m³) | 110 | 75 | 110 | 90 |
| MO (R$/AC) | 240 | 240 | 240 | 240 |
| Forma montagem (m²/AC) | 2,5 | 2,1 | 2,1 | 2,1 |
| PU Concreto | 610,05 | 610,05 | 575 | 580 |
| PU Armadura | 7,62 | 5,95 | 7,25 | 7,62 |
| **Total** | **7.808.061** | **7.413.979** | **1.244.909** | **8.482.789** |

> Nota: Treliçada tem valor muito baixo pois parece cobrir apenas itens parciais (embasamento/mezanino?)

### Infraestrutura + Contenções

| Item | Índice | Un | PU (R$) | Obs |
|------|--------|----|---------|-----|
| **Infra + Contenção total** | — | — | — | R$ 2.050.376 (182,77 R$/m²) |
| Ref. Atlantia | — | — | — | Índice custos Atlantia |

> Nota: Nesta planilha, Mov. Terra e Infra usam índices do projeto Atlantia como referência (R$/APE)

### Instalações (R$/AC direto)

| Subgrupo | Índice (R$/AC) | Total (R$) |
|----------|---------------|-----------|
| Elétricas | ~153,5 | — |
| Hidrossanitárias | ~145 | — |
| Preventivas + GLP | ~41 | — |
| **Total Instalações** | **327,00** | **3.668.348** |

### Esquadrias — Detalhamento

| Item | Qtd | Un | PU (R$) | Total (R$) |
|------|-----|----|---------|-----------|
| Alumínio (0,16 m²/AC) | 1.795 | m² | 1.100 | 2.171.842 |
| Pele de vidro (0,08 m²/AC) | 897 | m² | 950 | 937.841 |
| Brise fachada | 373 | m² | 1.350 | 553.846 |
| Guarda-corpo vidro | 382 | m² | 773 | 324.763 |
| Esquadrias madeira | 409 | un | 970 | 436.403 |
| PCF | 62 | un | 1.200 | 81.840 |
| Corrimão madeira | 381 | m | 85 | 35.607 |
| Fechadura biométrica | 44 | un | 1.250 | 60.500 |
| Portão alumínio | 1 | un | 18.000 | 19.800 |
| Gradil área técnica | 33 | m² | 736 | 27.095 |
| Serralheria | 2 R$/AC | vb | — | 24.680 |
| **Total** | | | | **4.674.216** |

### Impermeabilização

| Item | Índice | Un | PU (R$) | Total (R$) |
|------|--------|----|---------|-----------|
| Regularização | — | m² | 7,00 | 37.441 |
| Proteção mecânica | — | m² | 50,00 | 82.336 |
| MO reg+prot | — | vb | — | 186.172 |
| Poço elevador | — | m² | 66,00 | 3.593 |
| Baldrames | — | m² | 64,00 | 52.535 |
| Ralos | 2 R$/AC | vb | — | 24.680 |
| Cimentícia (0,3 m²/AC) | 0,30 | m²/AC | 70,00 | 259.140 |
| Manta asfáltica (0,08 m²/AC) | 0,08 | m²/AC | 98,00 | 100.913 |
| Manta asfáltica floreiras (0,05 m²/AC) | 0,05 | m²/AC | 98,00 | 60.466 |
| Peitoril | 1,3 R$/AC | vb | — | 16.042 |
| **Total** | | | | **823.318** |

### Pintura Interna

| Item | Qtd | Un | PU (R$) | Total (R$) |
|------|-----|----|---------|-----------|
| Piso epóxi | 192 | m² | 110,00 | 23.189 |
| Piso resina | 3.156 | m² | 30,00 | 104.148 |
| Textura escadas | 5.048 | m² | 34,00 | 188.802 |
| Textura teto | 3.253 | m² | 34,00 | 121.668 |
| Pintura tetos | 8.163 | m² | 49,00 | 439.961 |
| Pintura massa acrílica (banheiros) | 1.262 | m² | 51,00 | 70.801 |
| Pintura interna | 18.061 | m² | 49,00 | 973.503 |
| **Total** | | | | **1.922.072** |

### Fachada

| Item | Qtd | Un | PU (R$) | Total (R$) |
|------|-----|----|---------|-----------|
| Chapisco e reboco | 8.209 | m² | 36,00 | 325.067 |
| MO fachada | 8.209 | m² | empreitada | 698.144 |
| Tratamento friso | 2.416 | m | 2,50 | 6.643 |
| Textura | 8.209 | m² | 28,00 | 252.830 |
| MO textura | 8.209 | m² | 42,00 | 379.245 |
| Acabamentos especiais | 1 | vb | 5 R$/m² | 61.700 |
| **Total** | | | | **1.723.630** |

### Cobertura

| Item | Qtd | Un | PU (R$) | Total (R$) |
|------|-----|----|---------|-----------|
| Estrutura e telhamento | 801 | m² | 160,00 | 141.023 |
| MO cobertura | 1 | vb | — | 83.777 |
| Serviços complementares | 801 | m² | 30,00 | 26.442 |
| Pergolados | 56 | m² | 450,00 | 27.575 |
| **Total** | | | | **278.818** |

### Complementares

| Item | Índice | Total (R$) | Obs |
|------|--------|-----------|-----|
| Móveis/decoração | 1.500 R$/AL | 1.205.762 | AL = 730,76 m² |
| Comunicação visual | 10 R$/AC | 123.400 | |
| Paisagismo | 20 R$/AC | 246.800 | |
| Ligações definitivas | 4 R$/AC | 49.360 | |
| Desmobilização | — | 74.469 | |
| Custos compl. entrega | — | 139.629 | |
| Limpeza | 18 R$/AC | 222.120 | |
| **Total** | | **2.061.540** | |

---

## CUSTOS INDIRETOS — 2cinco4 Edition

### Resumo Custos Indiretos: R$ 3.445.019 (307,09 R$/m²)

| Grupo | Valor (R$) | % CI |
|-------|-----------|------|
| **01. Gerenciamento Técnico** | **854.648** | **24,8%** |
| Estudos, Projetos, Consultorias | 520.678 | |
| Taxas e Documentos | 333.971 | |
| **02. Gerenciamento Administrativo** | **2.590.371** | **75,2%** |
| Segurança, MA e Saúde | 548.940 | |
| Administração e Canteiro | 1.354.704 | |
| Equipamentos | 686.726 | |

### Detalhamento Equipe de Gestão (52 meses)

| Cargo | Custo/mês | Total |
|-------|-----------|-------|
| Engenheiro Civil | 5.000 | 260.000 |
| Mestre Geral | 4.000 | 208.000 |
| Almoxarife | 2.400 | 124.800 |
| Auxiliar Engenharia | 3.500 | 182.000 |
| **Subtotal** | **14.900** | **774.800** |

### Detalhamento Equipamentos Principais

| Item | Custo |
|------|-------|
| Cremalheira (locação 24 meses) | 216.000 + 12.600 (mont/desmob) |
| Mini-grua (locação 25 meses) | 212.500 + 7.000 (mont/desmob) |
| Balancim (locação + mont) | 179.736 |
| Veículo apoio (52 meses) | 13.000 |

### Detalhamento Proteção Coletiva (EPCs)

| Item | Qtd | PU | Total |
|------|-----|----|-------|
| Bandeja primária | 239 m | 403,30 | 96.292 |
| Bandeja secundária | 77 m | 365,00 | 28.061 |
| Tela fachadeira com impressão | 6.805 m² | 11,50 | 78.262 |
| Varal de segurança | 308 m | 105,00 | 32.290 |
| Guarda-corpo laje pós-desforma | 308 m | 16,50 | 5.074 |
| Guarda-corpo vãos com régua | 760 m | 16,00 | 12.157 |
| EPI | vb | — | 32.000 |
| Sinalização | vb | — | 2.804 |

### Índices R$/m² dos Custos Indiretos

| Item | R$/m² |
|------|-------|
| Projetos e consultorias | 46,41 |
| Taxas e documentos | 29,77 |
| Segurança/MA/Saúde | 48,93 |
| Administração/canteiro | 120,76 |
| Equipamentos | 61,22 |
| **Total Indiretos** | **307,09** |

---

## CUSTOS DE SERVIÇO (EMPREITADA) — 2cinco4

### MO por Grupo (via aba "Custos Serviços")

| Serviço | Área (m²) | Custo MO (R$) | R$/m² |
|---------|-----------|-------------|-------|
| Fundações | — | 511.972 | 363,02 R$/APE |
| Supraestrutura | 11.218 | 3.071.833 | 236,77 R$/AC |
| Alvenaria | — | 837.773 | 62,77 (empreitada) |
| **Total MO** | | **~9.300.000** (estimado) | |

> Ref. empreiteiro: Custos MO incluem balancim, ferramentas, instalações canteiro

---

## COMPARATIVO — Minha Estimativa vs Real

| Grupo | Meu Paramétrico (R$) | Real (R$) | Diferença |
|-------|---------------------|-----------|-----------|
| Supraestrutura | 7.280.860 | 7.413.979 | -1,8% ✅ |
| Instalações | 3.922.946 | 3.668.348 | +6,9% |
| Esquadrias | 2.987.947 | 4.674.216 | -36,1% ❌ |
| Sistemas Especiais | 2.319.469 | 2.414.995 | -4,0% ✅ |
| Rev. Internos | 2.055.476 | 2.253.069 | -8,8% |
| Acabamentos | 2.072.544 | 2.239.443 | -7,5% |
| Alvenaria | 1.914.086 | 1.725.490 | +10,9% |
| Infraestrutura | 1.882.723 | 2.050.376 | -8,2% |
| Complementares | 1.674.899 | 2.061.540 | -18,8% |
| Pintura | 1.424.732 | 1.922.072 | -25,9% ❌ |
| Fachada | 1.176.046 | 1.723.630 | -31,8% ❌ |
| Teto | 811.205 | 826.118 | -1,8% ✅ |
| Impermeabilização | 484.472 | 823.318 | -41,2% ❌ |
| Cobertura | 33.000 | 278.818 | -88,1% ❌ |
| Mov. Terra | 93.884 | 234.239 | -59,9% ❌ |
| Gerenciamento | NÃO INCLUÍDO | 3.445.019 | — |
| Imprevistos (3%) | NÃO INCLUÍDO | 1.029.289 | — |
| **TOTAL** | **31.777.991** | **38.783.958** | **-18,1%** |
| **TOTAL (mesmo escopo)** | **31.777.991** | **34.309.650** | **-7,4%** |

### Lições Aprendidas

1. **AC subestimado:** Eu estimei 10.503 m², real é 11.218 m² (+6,8%) — preciso do quadro de áreas oficial
2. **Esquadrias muito subestimadas:** Faltou considerar pele de vidro (R$ 950/m²), brises (R$ 1.350/m²), guarda-corpo (R$ 773/m²), fechaduras biométricas. Esquadrias = 12% do total, segundo maior grupo
3. **Fachada subestimada:** MO de fachada é empreitada separada (R$ 698k) — não estava no modelo original
4. **Impermeabilização mais complexa:** Floreiras, peitoris, MO separada — mais itens que o modelo básico
5. **Cobertura muito maior:** 801 m² (vs 300 estimado) + pergolados + MO separada
6. **Pintura mais detalhada:** Resina de piso (garagens), textura de teto, massa acrílica banheiros — mais tipos
7. **Complementares:** Paisagismo 20 R$/AC (vs 11) + custos de entrega + desmobilização maior
8. **Os índices de estrutura (cubetas) bateram muito bem** (-1,8%)! A estrutura é paramétrica mesmo
9. **Itens de acabamento/fachada precisam de levantamento mais detalhado** — são específicos de cada projeto

---

## REGRAS PARA PRÓXIMOS PROJETOS

### Ajustes nos Índices (baseado no 2cinco4):

| Item | Índice Antigo | Índice Calibrado | Fonte |
|------|--------------|-----------------|-------|
| Esquadrias alumínio | 0,15 m²/AC | 0,16 m²/AC | 2cinco4 |
| PU Alumínio | 1.250 R$/m² | 1.100 R$/m² | 2cinco4 |
| Pele de vidro | não incluía | 0,08 m²/AC, 950 R$/m² | 2cinco4 |
| Brise fachada | não incluía | levantamento específico | 2cinco4 |
| Guarda-corpo | não incluía | levantamento específico | 2cinco4 |
| Esquadrias madeira | 2.100/un | 970/un | 2cinco4 |
| PCF | 1.750/un | 1.200/un | 2cinco4 |
| Paisagismo | 11 R$/AC | 20 R$/AC | 2cinco4 |
| Limpeza | 15 R$/AC | 18 R$/AC | 2cinco4 |
| Cobertura | 55 R$/m² | 160 R$/m² est. + 30 compl. | 2cinco4 |
| Armadura (cubetas) | 78 kg/m³ | 75 kg/m³ | 2cinco4 Atlantia |
| PU Armadura | 7,62 R$/kg | 5,95 R$/kg | 2cinco4 Atlantia |
| Impermeab. cimentícia | 0,25 m²/AC | 0,30 m²/AC | 2cinco4 |
| Custos indiretos | NÃO INCLUÍA | 307 R$/m² | 2cinco4 |
| Imprevistos | NÃO INCLUÍA | 3% do direto | 2cinco4 |

### Checklist de Itens Frequentemente Esquecidos
- [ ] Pele de vidro (embasamento/comercial)
- [ ] Brise de fachada (quantificar da fachada)
- [ ] Guarda-corpo vidro (sacadas, terraços)
- [ ] Fechadura biométrica
- [ ] MO fachada (empreitada separada)
- [ ] MO cobertura (empreitada separada)
- [ ] MO impermeabilização (separada de material)
- [ ] Pergolados/passarelas
- [ ] Pintura resina de piso (garagens)
- [ ] Textura de teto (área comum)
- [ ] Custos indiretos (gerenciamento + canteiro + EPCs + equipamentos)
- [ ] Imprevistos/contingência (3%)
- [ ] Custos de entrega de obra

---

## ÍNDICES DETALHADOS — COMPARATIVO MULTI-PROJETO

### Supraestrutura — Parâmetros por Projeto

| Parâmetro | 2cinco4 | San Felice | Monolyt | Aquos | Redentor | Colline Resid | Colline Hotel | Unidade |
|-----------|---------|------------|---------|-------|----------|---------------|---------------|---------|
| Tipo laje | Cubetas | Cubetas | Protendida | Protendida | Protendida | **Maciça** | **Maciça** | — |
| Concreto | 0,28 | ~0,25 | 0,25 | 0,25 | 0,25 | 0,20 | 0,20 | m³/AC |
| PU Concreto | 610 | 575 | 730 | 730 | 656* | 558 | 558 | R$/m³ |
| Armadura conv. | 75 | 110 | 112 | 112 | 85 | 100 | 90 | kg/m³ |
| PU Armadura | 5,95 | 7,25 | 8,00 | 8,00 | 8,00* | 7,62 | 7,62 | R$/kg |
| Protensão | — | — | 16,78 | 16,78 | 16,78 | — | — | kg/m³ |
| PU Protensão | — | — | 35,00 | 35,00 | 23,35* | — | — | R$/kg |
| Forma fabricação | 3 jogos | — | 4 jogos | 4 jogos | 30%** | 4 jogos | 2 jogos | reutilizações |
| PU Forma | 110 | — | 115 | 115 | ~95* | 110 | 110 | R$/m² |
| Montagem forma | 2,1 | — | 2,1 | 2,1 | 2,5 | 2,5 | 2,5 | m²/AC |
| PU Montagem | 2,50 | — | 4,75 | 4,75 | 4,50* | 2,50 | 2,50 | R$/m² |
| MO estrutura | 240 | — | 280 | 500 | 190 | 210 | 210 | R$/AC |
| Escoramento | 11,51/un | — | 19,00/un | 19,00/un | 57,00/m² | 17/un | 17/un | R$ |
| Piso armado | — | — | 228/APE | 228/APE | — | — | — | R$/m² |
| **R$/AC total** | **661** | **599** | **1.154** | **1.902** | **795** | **704** | **768** | R$/m² |

*Redentor usa formato de planilha diferente (Mar/2023) — PUs calculados a partir dos totais
**Redentor: fabricação = 30% do custo, não número de jogos

> **Insight — Laje Maciça (Colline):** Concreto mais baixo (0,20 m³/AC vs 0,25-0,28), forma mais barata, sem protensão. Resultado: 704-768 R$/AC, comparável à cubetas (599-661) e bem abaixo de protendida (795-1.902). Primeira referência de maciça na base.

### Instalações — Parâmetros R$/AC por Subgrupo

| Subgrupo | 2cinco4 | Monolyt | Aquos | Redentor | CKock* | Unidade |
|----------|---------|---------|-------|----------|--------|---------|
| Entrada energia | — | 5 | 5 | 5,5 | — | R$/AC |
| Eletrodutos | — | 23 | 23 | 10 | — | R$/AC |
| Cabos e fiações | — | 40 | 40 | 30 | — | R$/AC |
| Quadros/disjuntores | — | 25 | 25 | 15 | — | R$/AC |
| Acabamentos elétricos | — | 30 | 30 | 15 | — | R$/AC |
| Equipamentos/iluminação | — | 20 | 20 | 15 | — | R$/AC |
| MO elétrica | — | 60 | 60 | 45 | — | R$/AC |
| **Subtotal Elétrica** | **~154** | **203** | **203** | **150,5** | — | R$/AC |
| Água fria | — | 25 | 25 | 28 | — | R$/AC |
| Água quente | — | 20 | 20 | 28 | — | R$/AC |
| Águas pluviais | — | 10 | 10 | 10 | — | R$/AC |
| Sanitárias | — | 15 | 15 | 16 | — | R$/AC |
| Louças e metais | — | 15 | 15 | 30 | — | R$/AC |
| MO hidráulica | — | 55 | 55 | 45 | — | R$/AC |
| **Subtotal Hidro** | **~145** | **140** | **140** | **157** | — | R$/AC |
| Preventivas | — | 18 | 18 | — | — | R$/AC |
| GLP | — | 15 | 15 | — | — | R$/AC |
| SPDA | — | 8 | 8 | — | — | R$/AC |
| **Subtotal Prev+GLP** | **~41** | **41** | **41** | — | — | R$/AC |
| **TOTAL INSTAL.** | **327** | **422** | **422** | **367** | **~366** | R$/AC |

*CKock (Catena/Zapata): sem decomposição por subgrupo nas planilhas

### Esquadrias — PUs por Tipo (Multi-Projeto)

| Item | 2cinco4 | San Felice | Campeche | Monolyt | Aquos | Redentor | Colline R | Colline H | Un |
|------|---------|------------|----------|---------|-------|----------|-----------|-----------|-----|
| Alumínio standard | 1.100 | 840 | — | 1.650 | 1.650 | 1.200 | — | 1.462 int | R$/m² |
| PVC standard | — | — | — | — | — | — | 1.626 | — | R$/m² |
| PVC arredondada | — | — | — | — | — | — | 3.253 | 3.253 | R$/m² |
| Pele de vidro | 950 | — | 980 | — | — | 1.000 | 1.100 | — | R$/m² |
| PCF | 1.200 | — | — | 1.750 | 1.750 | 1.750 | 1.850 | 1.850 | R$/un |
| Guarda-corpo vidro | 773 | — | — | 2.100 | 2.100 | 1.000 | 1.045/m | — | R$/m² |
| Gradil elaborado | — | — | — | — | — | — | 2.443/m | 7.641/m | R$/m |
| Brise | 1.350 | — | — | — | — | 2.000 | — | — | R$/m² |
| Esquadria madeira | 970 | 900 | 2.100 | 1.535 | 2.500 | 2.200 | 2.300 | 6.725 | R$/un |
| Madeira isolante | — | — | — | — | — | — | — | 9.662 | R$/un |
| Fechadura eletrônica | 1.250 | — | 1.500 | 2.500 | 2.750 | 1.300 | 1.445 | 1.445 | R$/un |
| Portão alumínio | 18.000 | — | — | 20.000 | 22.000 | 16.000 | 18.000 | 18.000 | R$/un |
| Serralheria | 2 R$/AC | — | — | 10 R$/AC | 10 R$/AC | 400k vb | 5 R$/AC | 5 R$/AC | R$/AC |

> **Insight — PVC como material (Colline):** Primeira vez na base usando esquadrias PVC em vez de alumínio. R$ 1.626/m² standard, R$ 3.253/m² arredondada. Esquadrias madeira hotel com isolamento acústico/térmico a R$ 9.662/un — 3-4x o preço de madeira standard.

### Sistemas Especiais — PUs Unitários

| Item | Monolyt | Aquos | Redentor | Un | Obs |
|------|---------|-------|----------|-----|-----|
| Infra AC cassete | 100 | 100 | — | R$/AC | Blue Heaven padrão |
| Infra AC (por un) | — | — | 1.500 | R$/un | Redentor |
| AC instalado | 8.000 | 8.000 | 5.000 | R$/un | |
| Ventokit | 900 | 900 | 900 | R$/un | Estável! |
| Churrasqueira | 2.600 | 2.600 | 2.000 | R$/un | BC > Itapema |
| Elevador | 210.000 | 210.000 | *16.000/NP | R$/un | *Redentor usa R$/pav |
| Elevador 1 parada | 52.500 | 52.500 | — | R$/un | Atlas ABC |
| Gerador | 80.000 | 80.000 | 109.200 | R$/un | |
| Carro elétrico infra | 800 | 800 | — | R$/un | BC feature |
| Carro elétrico instal. | 10.000 | 10.000 | — | R$/un | BC feature |
| Placas fotovoltaicas | 1.244.902 | 1.244.902 | — | R$/vb | Blue Heaven |
| Equipamento piscina | 36.831 | 36.831 | — | R$/un | Piscina aquecida |
| Sauna | 3.900 | 3.900 | — | R$/m² | |
| CFTV | 2 | 2 | 1,5 | R$/AC | |
| Interfone | 4 | 4 | 7 | R$/AC | |
| Controle acesso | 2 | 2 | — | R$/AC | |
| TV/internet | 3 | 4 | 5 | R$/AC | |
| Automação/segurança | 8 | 8 | — | R$/AC | BC complexidade |
| Outros sistemas | 30 | 30 | 20 | R$/AC | |

### Complementares — Parâmetros

| Item | 2cinco4 | Monolyt | Aquos | Redentor | Un |
|------|---------|---------|-------|----------|-----|
| Móveis/decoração | 1.500 | 3.100 | 3.100 | 2.400 | R$/ALI |
| Mob. jardim/gardens | — | 150 | 150 | — | R$/ALI |
| Comunicação visual | 10 | 12 | 12 | 10 | R$/AC |
| Paisagismo externo | 20 | 441 R$/ALE | 441 R$/ALE | 17 | R$/AC ou R$/ALE |
| Lago | — | 1.500 R$/m² | — | — | R$/m² |
| Fechamento madeira | — | — | 45 R$/m³ | — | Aquos feature |
| Ligações definitivas | 4 | 5 | 5 | — | R$/AC |
| Desmobilização | ~6 | 10 | 10 | — | R$/AC |
| Limpeza | 18 | 20 | 20 | 15 | R$/AC |

### Impermeabilização — Parâmetros

| Item | 2cinco4 | Monolyt | Un | Obs |
|------|---------|---------|-----|-----|
| Regularização + proteção | 57 R$/m² | 25 R$/m² | R$/m² | Blue Heaven simplificado |
| Cimentícia | 0,30 m²/AC | — | m²/AC | |
| Manta asfáltica | 0,08 m²/AC | 0,40 R$/AC* | m²/AC | *Monolyt usa R$/AC |
| Floreiras/peitoril | 0,05 m²/AC | — | m²/AC | |
| Paisagismo impermeab. | — | 28 R$/m² | R$/m² ALE | |
| Ralos | 2 R$/AC | — | R$/AC | |
| **Total** | **73 R$/AC** | **86 R$/AC** | — | |

### Fachada — Parâmetros

| Item | 2cinco4 | Monolyt | Aquos | Redentor | Un |
|------|---------|---------|-------|----------|-----|
| Chapisco e reboco | 36 R$/m² | — | 113 R$/m² | — | R$/m² fachada |
| Concreto aparente (resina) | — | 117,70 | 129,48 | — | R$/m² |
| MO fachada empreitada | ~85 R$/m² | — | — | — | R$/m² fachada |
| Textura | 28 R$/m² | — | — | — | R$/m² |
| MO textura | 42 R$/m² | — | — | — | R$/m² |
| Pedra natural fachada | — | — | 1.294 R$/m² | — | R$/m² |
| Pedra piscina fachada | — | — | 1.294 R$/m² | — | R$/m² |
| Pintura | — | 250 R$/m² | — | — | R$/m² |
| Caixilharia/serviços | — | 350 R$/m² | — | — | R$/m² |
| **R$/AC total** | **154** | **210** | **546** | **275** | R$/AC |

---

## WORKFLOW PADRÃO — INGESTÃO DE NOVO PROJETO

### Ao receber planilhas de um novo projeto, SEMPRE extrair:

1. **Dados gerais:** AC, AT, UR, NP, NPT, NS, APT, PPT, AL, AE, APE, CHU, elevadores, meses, data-base, CUB
2. **R$/m² por grupo de custo** (da aba consolidada/apresentação)
3. **Índices detalhados (PUs item a item):**
   - Supraestrutura: concreto m³/AC, PU concreto, armadura kg/m³, PU armadura, protensão kg/m³, MO R$/AC, forma jogos/reutilizações, PU forma
   - Instalações: R$/AC por subgrupo (elétrica, hidro, preventiva + GLP)
   - Esquadrias: PU alumínio R$/m², PU madeira R$/un, PU pele vidro, PU guarda-corpo, PU brise, PU fechadura
   - Sistemas Especiais: PU elevador, PU churrasqueira, PU ventokit, PU AC, PU piscina, PU gerador
   - Impermeabilização: índices m²/AC por tipo (cimentícia, manta), PU por tipo
   - Fachada: PU reboco, PU textura, MO empreitada, PU revestimento especial
   - Complementares: móveis R$/ALI, comunicação visual R$/AC, paisagismo R$/AC ou R$/ALE, limpeza R$/AC
4. **Custos indiretos:** Ger. Técnico, Seg/MA/Saúde, Admin/canteiro (equipe/mês + composição), Equipamentos
5. **Particularidades** que diferem dos demais projetos (itens novos, outliers)
6. **Atualizar tabelas comparativas** de índices multi-projeto
7. **Recalcular CV%** dos grupos para verificar estabilidade

> Este workflow garante que cada projeto alimenta a base com dados granulares, não só totais por grupo.

---

## COMO USAR ESTA BASE

### Para gerar um novo paramétrico:
1. Receber PDFs ou quadro de áreas → extrair variáveis (AC, UR, NP, NPT, etc.)
2. **Identificar data-base e região** → buscar CUB vigente daquela data/estado
3. Consultar índices desta base → aplicar os calibrados pelo projeto mais similar (padrão, região, porte)
4. **Se data-base dos índices ≠ data do novo orçamento:** corrigir pelo INCC antes de aplicar
5. Para itens paramétricos (R$/AC): multiplicar direto (com PU corrigido)
6. Para itens de levantamento: estimar quantidades pelos PDFs + aplicar PU
7. Somar custos indiretos (~307 R$/m² para alto padrão SC — corrigir por data e região)
8. Aplicar imprevistos (3%)
9. Comparar R$/m² total com CUB vigente do estado (range: 1,0-1,3 CUB para alto padrão)

### Para cada novo projeto que entrar:
1. Extrair dados e fazer o paramétrico
2. Quando receber o GE real, comparar com o paramétrico
3. Registrar diferenças e calibrar índices
4. Adicionar à tabela de projetos registrados

> A base melhora com cada projeto. Quanto mais projetos, mais precisa fica.

---

## DADOS DE ENTRADA — PROJETO 36: ETR Mediterrâneo Tower (CTN-ETR-MDT)

> **Fonte:** Orçamento Executivo R01 (XLSX + PDF) — Nov/2024
> **Índices expandidos:** `orcamento-parametrico/etr-zion-mediterraneo-indices.md` (16 seções completas)

### Dados Gerais
- **AC:** 4.617,34 m² | **AT:** 508,20 m² | **AP:** 2.378,15 m² (XLSX) / 1.821,09 m² (PDF)
- **UR:** 20 un (residenciais) | 3 tipologias: Diferenciado 151,89 m², Tipo 01 86,46 m², Tipo 02 89,40 m²
- **Pavimentos:** 13 (Térreo, Mezanino, G1, G2, Lazer, Tipo Dif., 9× Tipo, Casa Máq., Reservatório) | NPT=10, NPG=2
- **Elevadores:** 2 | **Prazo:** 42 meses
- **CUB/SC Nov/24:** R$ 2.863,73 | **R$/m²:** 4.196,73 (1,47 CUB) | **Total:** R$ 19.377.746,95
- **Laje:** Nervurada (cubetas ATEX 60×60) | **Fundação:** Hélice contínua Ø50, 35m prof. | **Padrão:** Alto (Portobello, pedra natural, marcenaria)
- **Incorporador:** ETR (ETR Zion / ETR Empreendimentos) | **Local:** Itapema/SC (Meia Praia)

### Macrogrupos (R$/m²)

| Macrogrupo | R$/m² | % | Obs |
|---|---|---|---|
| Gerenciamento Téc/Admin | 599,14 | 14,28% | CI completo |
| Movimentação de Terra | 12,62 | 0,30% | |
| Infraestrutura | 223,82 | 5,33% | HC Ø50 + fund. rasa |
| Supraestrutura | 755,97 | 18,01% | Maior macrogrupo |
| Paredes e Painéis | 237,63 | 5,66% | |
| Impermeabilização | 56,79 | 1,35% | |
| Inst. Elétr/Hidráulicas/GLP/Prev | 361,98 | 8,63% | |
| Sistemas e Inst. Elétricas | 216,73 | 5,16% | |
| Rev. Internos Parede | 248,10 | 5,91% | |
| Rev/Acab. Teto | 85,03 | 2,03% | |
| Pisos e Pavimentações | 365,22 | 8,70% | |
| Pintura Interna | 151,77 | 3,62% | |
| Esquadrias, Vidros, Ferragens | 369,37 | 8,80% | Alto padrão |
| Louças e Metais | 22,45 | 0,53% | |
| Cobertura | 15,11 | 0,36% | |
| Fachada | 222,43 | 5,30% | |
| Serviços Complementares | 190,56 | 4,54% | |
| Imprevistos | 62,02 | 1,48% | |
| **TOTAL** | **4.196,73** | **100%** | |

> Instalações agrupadas (itens 7+8): R$ 578,71/m² (13,79%). PDF menciona Equipamentos Especiais R$ 740k (elevadores+piscina) e Climatização R$ 252k dentro desses grupos.

### Índices Estruturais

| Índice | Valor | Obs |
|---|---|---|
| Concreto supra / AC | 0,247 m³/m² | fck 35 MPa, R$ 606/m³ |
| Taxa aço supra | 86,1 kg/m³ | 98.275 kg total |
| Aço supra / AC | 21,28 kg/m² | |
| Concreto fund. prof. | 350,83 m³ fck 40 | c/ 30% perda, R$ 826/m³ |
| ML estaca / AC | 0,644 m/m² | ⚠️ 65% acima KIR (0,39) |
| ML estaca / UR | 148,75 m/UR | 85 un HC Ø50 × 35m |
| Nº estacas / UR | 4,25 un/UR | |
| Taxa aço fund. rasa | 91,4 kg/m³ | 18.570 kg / 203,29 m³ |
| Alvenaria / AC | 0,993 m²/m² | Cerâmica + concreto celular |
| Chapisco-reboco / AC | 1,42 m²/m² | |
| Forro total / AC | 0,889 m²/m² | Gesso + estucamento + madeira |
| Contrapiso / AC | 0,998 m²/m² | Comum + acústico |
| Negativo gesso / AC | 0,833 m/m² | |
| Encunhamento / AC | 0,481 m/m² | |
| Ritmo construção | 109,9 m²/mês | ⚠️ Muito baixo (KIR 306, ADR 308) |

### Custos Indiretos (R$ 2.766.421,59 = 599,14 R$/m² = 14,28%)

| Subgrupo | Valor (R$) | R$/m² |
|---|---|---|
| Projetos e Consultorias | 481.949,75 | 104,38 |
| Taxas e Licenças | 104.796,82 | 22,70 |
| Equipe ADM (6 pessoas, 42m) | 1.165.552,61 | 252,44 |
| EPCs/Segurança | 348.844,74 | 75,56 |
| Canteiro + Despesas Consumo | 358.919,27 | 77,73 |

#### Equipe (42 meses): Engenheiro R$ 7.390/m, Mestre R$ 5.132/m, Almoxarife R$ 2.566/m, Assistente ADM R$ 2.500/m, Guincheiro R$ 4.619/m (36m), Limpeza R$ 6.205/m

### Destaques

1. ⚠️ **Fundação pesada** — ML estaca/AC 0,644 (65% acima KIR). Solo fraco Meia Praia, 85 estacas a 35m
2. ⚠️ **Ritmo muito baixo** — 110 m²/mês (vs 306 KIR, 308 ADR). Terreno 508 m² limita logística
3. ⚠️ **CI alto** — 14,28% (R$ 599/m²). Prazo 42 meses amplifica custos fixos
4. ⚠️ **Esquadrias R$ 369/m²** — alto padrão (Portobello, vidros, marcenaria)
5. ✅ Taxa aço 86,1 kg/m³ — entre KIR (82) e ADR (115)
6. ✅ Concreto/AC 0,247 — alinhado com KIR (0,242)
7. ✅ CUB ratio 1,47 — igual ao Redentor (Itapema, alto padrão)
8. 📝 Alvenaria/AC 0,993 — abaixo da média (menos compartimentação?)
9. 📝 Cubetas ATEX 60×60: 3.492 un × R$ 103 = R$ 359k
10. 📝 Área privativa diverge 30% entre XLSX (2.378 m²) e PDF (1.821 m²)

---

## DADOS DE ENTRADA — PROJETO 37: FG Blue Coast (CTN-FGE-BCO)

> **Fonte:** Orçamento Executivo R01 Auditoria (XLSX + PDF) — Out/2025
> **Índices expandidos:** `orcamento-parametrico/fge-bluecoast-indices.md` (16 seções completas)

### Dados Gerais
- **AC:** 13.131,85 m² | **AT:** 1.047,03 m² | **AP:** 7.900,36 m²
- **UR:** 36 un (35 residenciais + 1 comercial) | Tipologias: Tipo 196,01 m² (30 pvtos), Diferenciado 01 307,43 m², Diferenciado 02 244,51 m², Duplex 392,50 m²
- **Pavimentos:** 50 (Térreo ×2, G1-G4, Lazer ×3, Tipo Dif. ×2, Tipo ×30, Duplex ×6, Lazer 3, Casa Máq., Barrilete, Reservatórios) | NPT=32, NPG=4
- **Elevadores:** 3 (2 sociais + 1 emergência) | **Prazo:** 40 meses
- **CUB/SC Out/25:** R$ 2.999,38 | **R$/m²:** 6.081,49 (2,03 CUB) | **Total:** R$ 79.861.234,36
- **Laje:** N/D | **Fundação:** Hélice contínua ø60cm, 186 estacas × 15m, fck 40 MPa | **Padrão:** Super Alto
- **Incorporador:** FG Empreendimentos | **Local:** Balneário Camboriú/SC (Pioneiros)

### Macrogrupos (R$/m² — estrutura GE 16 etapas)

| Etapa GE | R$/m² | % | Obs |
|---|---|---|---|
| 01 Custos Preliminares, ADM e Operações | 667,13 | 10,97% | Serv. Técnicos + Canteiro + Operação |
| 02 Equipamentos de Grande Porte | 108,78 | 1,79% | Cremalheira + grua (4× benchmark) |
| 03 Infraestrutura | 349,19 | 5,74% | HC ø60 + blocos/vigas |
| 04 Supraestrutura | 1.236,28 | 20,33% | ❌ 53% acima benchmark. Taxa aço 139 kg/m³ |
| 05 Alvenarias e Vedações | 283,07 | 4,65% | ❌ 66% acima benchmark |
| 06 Inst. Hidrossanitárias | 171,69 | 2,82% | Custo apropriado R$ 3.082k (R$ 235/m²) |
| 07 Inst. Elétricas | 331,09 | 5,44% | Custo apropriado R$ 4.099k (R$ 312/m²) |
| 08 Revestimentos Argamassa | 164,38 | 2,70% | Emb 60 + Torre 100 R$/m² |
| 09 Forro | 64,00 | 1,05% | Muito abaixo benchmark |
| 10 Impermeabilização | 92,25 | 1,52% | Lev. acima (benchmark 55-90) |
| 11 Pintura | 194,47 | 3,20% | ✅ Dentro |
| 12 Acabamentos Piso/Parede | 580,82 | 9,55% | ❌ 3,8× acima — super alto padrão |
| 13 Esquadrias, Vidros e Ferragens | 950,31 | 15,63% | Fachada imponente, muita esquadria |
| 14 Equipamentos e Sistemas Especiais | 594,87 | 9,78% | Fachada ventilada (atípica) |
| 15 Serviços Complementares e Finais | 154,57 | 2,54% | ✅ Dentro |
| 16 Decoração e Mobiliário | 138,60 | 2,28% | R$ 2.067/m² sobre área lazer |
| **TOTAL** | **6.081,49** | **100%** | **2,03 CUB** |

### Índices-Chave

| Índice | Valor | Un |
|---|---|---|
| CUB ratio | 2,03 | CUB |
| R$/UR | R$ 2.218.368 | R$/UR |
| AC/UR | 364,77 | m²/un |
| AP/UR | 219,45 | m²/un |
| Taxa aço supra | ~139 | kg/m³ |
| ML estaca/AC | 0,21 | m/m² |
| Estacas/UR | 5,17 | un/UR |
| Elevador R$/un | R$ 792.018 | R$/un |
| Ritmo construção | 328 | m²/mês |
| Burn rate | R$ 2,00M | R$/mês |
| Pm (produtividade) | 47 | h/m² |
| CI / AC | 775,91 | R$/m² (12,76%) |
| Louças+Metais / UR | R$ 12.593 | R$/UR |
| PCI / AC | 260,06 | R$/m² |

### Destaques

1. ❌ **Supraestrutura crítica** — R$ 1.236/m² (benchmark 730-810, +53%). Taxa de aço 139 kg/m³ vs 55 kg/m³ (2,5×). 32% do custo é aço
2. ❌ **Acabamentos 3,8×** — R$ 581/m² (benchmark 100-150). Altíssimo padrão com nuances de cores/texturas
3. ❌ **Equipamentos/Sistemas 2,9×** — R$ 595/m² (benchmark 170-200). Fachada ventilada atípica (nenhuma obra similar usa)
4. ❌ **Alvenaria +66%** — R$ 283/m² (benchmark 100-170). 30 tipos + embasamento extenso
5. ⚠️ **Equip. Grande Porte 4×** — R$ 109/m² (benchmark 16-27). Justificado: cremalheira + grua para 50 pvtos
6. ⚠️ **Esquadrias +36%** — R$ 950/m² (benchmark 630-700). Fachada imponente
7. ❓ **Hidro/Elétrica — custo apropriado ≠ orçado** — Hidro: R$ 2.254k orçado vs R$ 3.082k apropriado. Elétrica: R$ 4.348k vs R$ 4.099k
8. ❓ **Forro muito abaixo** — R$ 64/m² (benchmark 160-210). "Quase não tem argamassados de parede"
9. 📝 **CUB 2,03** — alto vs benchmark 1,10-1,50. Justificado: 50 pvtos + super alto padrão + BC
10. 📝 **Fachada ventilada** — custo embutido em Equipamentos/Sistemas, sem comparável no portfólio CTN
11. 📝 **Decoração/Mobiliário** — R$ 1.820k (R$ 2.067/m² sobre 880 m² de lazer)
12. 📝 **Cobertura mínima** — R$ 2.970 (R$ 0,23/m²), prédio sem cobertura convencional
13. 📝 **Canteiro** — 234 pessoas (226 + 8 ADM), produtividade 328 m²/mês
14. 📝 **7 obras referência CTN:** DOM, M Village, LUMIS, NAUTILUS, SANTORINI, Redentor, Mario Lago

---

## DADOS DE ENTRADA — PROJETO 42: Fonseca Neto Estoril (CTN-FSN-EST)

> **Fonte:** Orçamento Executivo R00 - Letícia (15/01/2025) — Data-base Dez/2025
> **Índices expandidos:** `orcamento-parametrico/fonseca-estoril-indices.md` (16 seções completas)
> **⚠️ ALVENARIA ESTRUTURAL** — 1º projeto da base com este sistema construtivo

### Dados Gerais
- **AC:** 14.491,98 m² | **AT:** 1.430,00 m² | **AP:** 7.757,61 m²
- **UR:** 112 un (110 residenciais + 2 comerciais) | Tipologias: ~70 m² privativos médios
- **Pavimentos:** 20 (Subsolo + Térreo + G3-G5 + Lazer + Tipo Dif. + Tipo ×10 + Cobertura + CMaq/Barrilete) | NPT=12×2 torres, NPG=5
- **Elevadores:** 2 (Torres A + B) | **Prazo:** 48 meses
- **CUB/SC Dez/25:** R$ 3.008,84 | **R$/m²:** 3.545,06 (1,18 CUB) | **Total:** R$ 51.374.961,20
- **Laje:** Mista (protendida G3 + convencional tipo) | **Fundação:** HC ø60/70/80cm (137 estacas, 2.825m) | **Padrão:** Médio-Alto
- **Incorporador:** Fonseca Neto | **Local:** Rua Licurana, 721 - Tabuleiro, Camboriú/SC
- **TIPO ESTRUTURAL:** **ALVENARIA ESTRUTURAL** (blocos concreto 3-6 MPa, 14×19 cm)

### Macrogrupos (R$/m² — estrutura GTA + GE 20 etapas)

| Etapa | R$/m² | % | Obs |
|---|---|---|---|
| GTA (Gerenciamento) | 531,92 | 15,0% | Projetos R$670k + Licenças R$620k + Restante R$6.2M |
| 01 Serviços Preliminares | 16,07 | 0,5% | Prep. terreno + terraplanagem + locação |
| 02 Fundações e Contenções | 171,21 | 4,8% | HC ø60/70/80 + contenção cortina + fund. rasa |
| 03 Supraestrutura | 709,97 | 20,0% | ⚠️ ALVENARIA ESTRUTURAL (não comparável c/ CA) |
| 04 Alvenaria e Vedações | 167,52 | 4,7% | Estrutural (blocos concreto) + vedação (cerâmico) |
| 05 Inst. Hidrossanitárias | 169,76 | 4,8% | Inclui louças R$216k + metais R$133k + ETE R$175k |
| 06 Inst. Elétricas | 199,47 | 5,6% | Disjuntores R$482k (17%), eletrodutos telecom R$174k |
| 07 Inst. Preventivas e GLP | 47,71 | 1,4% | PCI + GLP |
| 08 Climatização e Exaustão | 42,29 | 1,2% | Equip. + redes frigorígenas |
| 09 SPDA | 5,65 | 0,2% | Material + MO |
| 10 Impermeabilização | 70,77 | 2,0% | Visus BIM detalhado |
| 11 Revestimentos Argamassados | 182,35 | 5,1% | Chapisco + reboco + estucamento |
| 12 Acabamentos de Teto | 62,93 | 1,8% | Gesso mineral + RU + reboco+textura |
| 13 Acabamentos Piso/Parede | 234,50 | 6,6% | Porcelanato + cerâmico + concreto garagem |
| 14 Pintura Interna | 139,13 | 3,9% | ✅ Dentro |
| 15 Esquadrias | 312,41 | 8,8% | Alumínio + madeira (418+ portas) + PCF + corrimão |
| 16 Cobertura | 17,97 | 0,5% | Fibrocimento 273,61 m² |
| 17 Equip. e Sistemas Especiais | 111,00 | 3,1% | Elevadores + piscinas + fachada ventilada |
| 18 Revestimentos Fachada | 181,17 | 5,1% | **FACHADA VENTILADA** R$ 702,08/un (2º da base) |
| 19 Serviços Complementares | 126,73 | 3,6% | — |
| 20 Imprevistos | 44,53 | 1,3% | ⚠️ Muito baixo (benchmark 2-5%) |

### Índices Globais

| Índice | Valor | Un |
|---|---|---|
| R$/UR | R$ 458.705 | R$/UR |
| AC/UR | 129,39 | m²/un |
| AP/UR | 69,26 | m²/un |
| Concreto total / AC | 0,412 | m³/m² |
| ML estaca / AC | 0,195 | m/m² |
| Estacas / UR | 1,22 | un/UR |
| Instalações / AC | 464,90 | R$/m² |
| Ritmo construção | 301,9 | m²/mês |
| Burn rate | R$ 1,07M | R$/mês |
| Pm (produtividade) | 41 | h/m² |
| CI / AC | 531,92 | R$/m² (15,0%) |

### Destaques

1. ⚠️ **ALVENARIA ESTRUTURAL** — 1º projeto da base com este sistema. Supra+Alvenaria = R$ 877/m² (24,7%) — métrica comparável. Benchmarks de supra/alvenaria de concreto armado NÃO se aplicam
2. ⚠️ **FACHADA VENTILADA** — R$ 702,08/un (insumo). 2º projeto CTN com este sistema (após Blue Coast FG)
3. ⚠️ **Instalações 15% acima** — R$ 623/m² (faixa 240-540). MO elétrica = MO hidro = R$ 988.601 (possível template)
4. ⚠️ **Imprevistos 1,26%** — muito abaixo do benchmark (2-5%)
5. 📝 **2 torres (A + B)** — duplica instalações, esquadrias, elevadores
6. 📝 **Protensão G3** — laje garagem com monocordoalha engraxada
7. 📝 **41 abas Visus BIM** — detalhamento excepcional
8. 📝 **CUB 1,18** — excelente para Camboriú, padrão médio-alto
9. 📝 **ETE inclusa** — R$ 175.134 (dentro de Hidro)
10. 📝 **Mobiliário** — R$ 1.322k (R$ 1.158/m² sobre 1.142 m² lazer)

---

## DADOS DE ENTRADA — PROJETO 43: Residencial Urban Life (Paludo, Joaçaba/SC)

> **Fonte:** Orçamento Executivo Fev/2021 (Versão 04/02/2021)
> **Índices expandidos:** `orcamento-parametrico/indices/paludo-urbanlife-indices.md` (16 seções completas)
> **⚠️ PRIMEIRO PROJETO JOAÇABA/SC** — Cidade nova na base paramétrica

### Dados Gerais
- **AC:** 7.040,19 m² | **AT:** N/D | **AP:** N/D
- **UR:** 48 un | Tipologias: ~146,7 m²/un médios
- **Pavimentos:** N/D | **Prazo:** ~44 meses (inferido — mestre 42m, guincheiro/cremalheira 36m)
- **CUB/SC Fev/21:** R$ 2.201,37 (estimado) | **R$/m²:** 2.624,80 (1,19 CUB) | **Total:** R$ 18.479.084,15
- **R$/m² Normalizado (dez/23):** 3.282,58 | **Total Normalizado:** R$ 23.109.241,45
- **Laje:** Concreto armado moldado in loco | **Fundação:** Rasa (sapatas + baldrame fck 35 MPa) | **Padrão:** Médio
- **Incorporador:** Paludo | **Local:** Rua Felipe Schmidt, 576 - Centro, Joaçaba/SC

### Macrogrupos (R$/m² — estrutura 18 macrogrupos padrão)

| Macrogrupo | R$/m² | % | R$/m² Norm. | Obs |
|---|---|---|---|---|
| 1-Gerenciamento | 289,47 | 11,03% | 362,01 | Técnico R$375k + ADM R$1.663k (44m prazo) |
| 2-Mov. Terra | 18,61 | 0,71% | 23,27 | Terreno plano ou pouco desnível |
| 3-Infraestrutura | 54,22 | 2,07% | 67,81 | ✅ Fundação rasa apenas (solo bom) |
| 4-Supraestrutura | 580,52 | 22,12% | 726,03 | ⚠️ 22% do total — ALTO |
| 5-Alvenaria | 100,53 | 3,83% | 125,72 | Vedação + estrutural |
| 6-Impermeabilização | 55,17 | 2,10% | 68,99 | ✅ Dentro da faixa |
| 7-Instalações | 286,69 | 10,92% | 358,53 | Elétr. + Hidro + GLP + Preventivas |
| 8-Sist. Especiais | 142,59 | 5,43% | 178,32 | Elevadores, portão, interfone, CFTV |
| 9-Climatização | 0,00 | 0,00% | 0,00 | ⚠️ Sem destaque (provável A/C comprador) |
| 10-Rev. Int. Parede | 168,80 | 6,43% | 211,09 | Reboco + azulejo + gesso |
| 11-Teto | 71,72 | 2,73% | 89,68 | Forro gesso + pintura teto |
| 12-Pisos | 166,88 | 6,36% | 208,69 | Contrapiso + porcelanato + cerâmica |
| 13-Pintura | 101,80 | 3,88% | 127,28 | ✅ Dentro |
| 14-Esquadrias | 344,53 | 13,13% | 430,79 | ⚠️ 13% do total — ALTO (alumínio linha superior) |
| 15-Louças e Metais | 0,00 | 0,00% | 0,00 | ⚠️ Embutido em Instalações/Complementares |
| 16-Fachada | 106,53 | 4,06% | 133,20 | ✅ Dentro |
| 17-Complementares | 95,94 | 3,66% | 119,98 | Cobertura R$69k + complementares R$606k |
| 18-Imprevistos | 40,95 | 1,56% | 51,21 | ⚠️ Baixo (benchmark 2-5%) |

### Gerenciamento Detalhado (UC1)

**Técnico (R$ 375.100 = R$ 53/m²):**
- Estudos: R$ 57.350 (sondagem R$ 24,7k + geológico R$ 17,6k + topografia/outros)
- Projetos: R$ 103.000 (arquitetônico R$ 30k, hidro R$ 12,5k, elétrico R$ 11,5k, etc)
- Consultorias: R$ 58.000 (orçamento/plan R$ 23k, auditoria R$ 15k, etc)
- Ensaios/Laudos: R$ 30.000 (NBR 15575, controle tecnológico)
- Taxas/Docs: R$ 126.750 (Alvará, ARTs, licenças)

**ADM/Canteiro (R$ 1.662.593,95 = R$ 236/m²):**
- EPCs (SMS): R$ 162.978 (EPIs, tela fachadeira, bandeja, guarda-corpo)
- Equipe Obra: R$ 883.200 (Mestre 42m × R$ 12,8k + Guincheiro 36m × R$ 4,8k + Op. Cremalheira 36m × R$ 4,8k)
- Instalações Provisórias: R$ 244.839 (escritório, alojamento, banheiros, etc)
- Consumos/Manutenção: R$ 187.608 (energia, água, limpeza, manutenção)
- Equipamentos: R$ 167.200 (grua, cremalheira, manutenções)
- Outros ADM: ~R$ 16.769

### Índices Globais

| Índice | Valor Original | Valor Norm. (dez/23) | Un |
|---|---|---|---|
| R$/UR (com ger.) | R$ 385.000 | R$ 481.442 | R$/UR |
| R$/UR (diretos) | R$ 336.523 | R$ 420.765 | R$/UR |
| AC/UR | 146,7 | 146,7 | m²/un |
| MO supra / AC | 205 | 256,33 | R$/m² |
| MO infra / AC | 205 | 256,33 | R$/m² |
| Ritmo construção | 160,0 | 160,0 | m²/mês |
| Burn rate | R$ 420,0k | R$ 525,2k | R$/mês |
| CI / AC | 289,47 | 362,01 | R$/m² (11,03%) |

### Destaques

1. 🆕 **PRIMEIRO PROJETO JOAÇABA/SC** — Cidade nova na base (sem referências locais prévias)
2. ⚠️ **Supraestrutura 22% do total** — R$ 581/m² (726 normalizado). Possível: muitos pavimentos, estrutura robusta, ou laje maciça
3. ⚠️ **Esquadrias 13% do total** — R$ 345/m² (431 normalizado). Possível: alumínio linha superior ou muito vidro na fachada
4. ⚠️ **Prazo 44 meses** — mais longo que média (30-36m), elevando custos de equipe obra
5. ✅ **Fundação rasa apenas** — R$ 54/m² (67 normalizado). Solo de boa capacidade de suporte (típico de Joaçaba)
6. ⚠️ **MO estrutura embutida** — R$ 205/m² por pavimento (diferente de Barbados que tinha empreitada global separada)
7. ⚠️ **Sem Louças e Metais destacadas** — provável embutido em Instalações ou Complementares
8. ⚠️ **Sem climatização destacada** — provável que A/C seja responsabilidade do comprador
9. ⚠️ **Imprevistos 1,56%** — abaixo do benchmark (2-5%)
10. 📝 **Data-base Fev/2021** — início da pandemia COVID-19, possível pressão em preços de insumos
11. 📝 **CUB 1,19** — dentro da faixa (médio padrão 1,10-1,30)
12. 📝 **Ritmo 160 m²/mês** — lento vs obras similares (KIR 306, ADR 308). Burn rate R$ 420k/mês moderado
13. 📝 **Comparativo com Barbados e Nassau** — apresentação menciona que Urban Life tem valores mais altos em quase todas as etapas
14. 📝 **Aba "Auxiliar" na apresentação** — contém outro breakdown (Total: R$ 11.417.532,53, AC: 4.338,77 m², 46 UR). Pode ser versão sem comercial ou outra torre

---

## DADOS DE ENTRADA — PROJETO 44: Residencial Barbados (PAL-BAR)

> **Fonte:** Orçamento Executivo Paludo — Data-base Out/2021
> **Índices expandidos:** `orcamento-parametrico/paludo-barbados-indices.md` (16 seções completas)
> **⚠️ EMPREITADA GLOBAL MO ESTRUTURA** — R$ 1.232.827 (25,65%) separada, somar à Supraestrutura para calibração

### Dados Gerais
- **AC:** 1.728,35 m² | **AT:** N/D | **AP:** N/D
- **UR:** 9 un (100% residenciais) | Tipologias: ~192 m² médios
- **Pavimentos:** 6 (Térreo + Garagem + 2 Tipos + Duplex Inf/Sup/Terraço + Cobertura) | NPT=2, NPG=1
- **Elevadores:** N/D | **Prazo:** N/D
- **CUB/SC Out/21:** R$ 2.381,05 | **CUB Norm. (Dez/23):** R$ 2.752,67 | **Fator:** 1,15614
- **R$/m² (sem ger.):** 2.554,28 (1,073 CUB) | **R$/m² Norm.:** 2.952,89 | **Total (sem ger.):** R$ 4.414.695,11
- **R$/m² (com ger.):** 2.781,34 | **R$/m² Norm.:** 3.215,39 | **Total (com ger.):** R$ 4.807.136,02
- **Laje:** N/D | **Fundação:** N/D | **Padrão:** Médio
- **Incorporador:** Paludo | **Local:** Rua Tucano, 236 - Bombinhas/SC

### Macrogrupos (R$/m² normalizado — CUB Dez/23)

| Etapa | R$/m² | R$/m² Norm. | % | Obs |
|---|---|---|---|---|
| Gerenciamento Técnico/ADM | 227,06 | 262,47 | 8,16% | Separado |
| Mov. Terra | 17,84 | 20,62 | 0,64% | ✅ Dentro |
| Infraestrutura | 103,67 | 119,85 | 3,73% | ✅ Dentro |
| **Supraestrutura (materiais)** | 404,78 | 467,97 | 14,55% | **Sem empreitada** |
| **Empreitada Global (MO estrut.)** | 713,30 | 824,71 | 25,65% | **Somar na calibração** |
| **SUPRA AJUSTADA (Mat+MO)** | **1.118,08** | **1.292,68** | **40,20%** | **Total completo** |
| Alvenaria | 57,21 | 66,14 | 2,06% | ⚠️ Abaixo (faixa 123-324) |
| Impermeabilização | 64,42 | 74,49 | 2,32% | ✅ Dentro |
| Instalações (todas) | 159,26 | 184,13 | 5,73% | ⚠️ Abaixo (faixa 240-432, 8-11%) |
| Sistemas Especiais | 156,10 | 180,48 | 5,61% | ✅ Dentro |
| Rev. Internos Parede | 114,58 | 132,49 | 4,12% | ✅ Dentro |
| Teto | 46,59 | 53,87 | 1,68% | ✅ Dentro |
| Pisos | 114,60 | 132,52 | 4,12% | ✅ Dentro |
| Pintura Interna | 128,02 | 148,03 | 4,60% | ✅ Dentro |
| Esquadrias | 256,91 | 297,05 | 9,24% | ✅ Dentro (tendendo alto) |
| Cobertura | 17,83 | 20,61 | 0,64% | — |
| Fachada | 87,63 | 101,32 | 3,15% | ✅ Dentro |
| Serv. Complementares | 111,54 | 128,98 | 4,01% | ✅ Dentro |

### Composição por Tipo de Custo (valores originais)

| Tipo | Valor (R$) | % | R$/m² | R$/m² Norm. |
|---|---|---|---|---|
| Empreitada Global (MO estrut.) | 1.232.827 | 25,65% | 713,30 | 824,71 |
| Materiais | 2.205.536 | 45,88% | 1.276,11 | 1.475,38 |
| Mão de Obra (outros) | 254.605 | 5,30% | 147,32 | 170,31 |
| Serviço (MO+Mat) | 592.784 | 12,33% | 343,03 | 396,71 |
| Equipamentos | 70.142 | 1,46% | 40,59 | 46,93 |
| Despesas Indiretas | 381.941 | 7,95% | 221,00 | 255,56 |
| Imprevistos | 69.302 | 1,44% | 40,10 | 46,36 |

> **Nota:** Empreitada 25,65% + Materiais 45,88% = 71,5% do custo total

### Breakdown Supraestrutura (materiais apenas, R$ 699.593)

| Item | Valor (R$) | % Supra | R$/m² | R$/m² Norm. |
|---|---|---|---|---|
| Armadura | 344.700 | 49,3% | 199,46 | 230,58 |
| Concreto | 211.570 | 30,2% | 122,42 | 141,53 |
| Complementares | 77.490 | 11,1% | 44,83 | 51,83 |
| Forma | 65.830 | 9,4% | 38,09 | 44,03 |
| **Total Materiais** | **699.590** | **100%** | **404,78** | **467,97** |
| **+ Empreitada Global (MO)** | **1.232.827** | — | **713,30** | **824,71** |
| **= Supraestrutura TOTAL** | **1.932.417** | — | **1.118,08** | **1.292,68** |

### Índices Globais

| Índice | Valor | Valor Norm. | Un |
|---|---|---|---|
| R$/UR (sem ger.) | R$ 490.522 | R$ 567.143 | R$/UR |
| R$/UR (com ger.) | R$ 534.126 | R$ 617.547 | R$/UR |
| AC/UR | 192,0 | 192,0 | m²/un |
| CUB/UR (sem ger.) | 206,0 | 206,0 | CUB/un |
| Concreto total / AC | ~0,20-0,23 | — | m³/m² (estimado) |
| Aço total / AC | ~26-29 | — | kg/m² (estimado) |
| Taxa aço supra | ~130-140 | — | kg/m³ (estimado) |
| Instalações / AC | 159,26 | 184,13 | R$/m² |
| CI / AC | 227,06 | 262,47 | R$/m² (8,16%) |

> **Nota:** Consumos estruturais são estimativas (executivo fornece custos, não quantitativos)

### Benchmark Nassau (Paludo, Bombinhas/SC, Out/2021)

| Projeto | AC (m²) | R$/m² (sem ger.) | CUB ratio | Diferença |
|---|---|---|---|---|
| **Barbados** | 1.728 | 2.554,28 | 1,073 | Referência |
| **Nassau** | N/D | 2.433,32 | ~1,022 | **-5%** (mais barato) |

> **Nota:** Ambos mesma data-base (out/2021), mesmo incorporador, mesma região. Nassau 5% mais econômico.

### Destaques

1. ⚠️ **Empreitada Global 25,65%** — MO estrutura separada (R$ 1.232.827). Para calibração: **somar à Supraestrutura** → R$ 1.932.420 (40,2% / R$ 1.118/m²)
2. ⚠️ **Instalações muito abaixo** — R$ 159/m² (normalizado R$ 184/m²) vs faixa 240-432. Apenas 5,73% vs típico 8-11%. Possível simplificação ou subcontratação não detalhada
3. ⚠️ **Alvenaria baixa** — R$ 57/m² (normalizado R$ 66/m²) vs faixa 123-324. Possível vedação leve ou alvenaria em outro grupo
4. ✅ **Breakdown Supraestrutura detalhado** — Armadura 49,3%, Concreto 30,2%, Forma 9,4%, Complementares 11,1%
5. 📝 **Pequeno porte (9 unidades)** — Custos fixos diluídos em menos unidades → R$/m² e R$/UR mais altos que projetos maiores
6. 📝 **Unidades amplas (192 m²/un)** — Consistente com padrão médio Bombinhas
7. 📝 **CUB ratio 1,073** — Conservador para Bombinhas (mercado turístico de alto padrão, projetos chegam a 1,3-1,5)
8. 📝 **Comparativo direto Nassau** — Mesmo incorporador/região, 5% mais barato. Benchmark confiável
9. 📝 **Gerenciamento 8,16%** — Razoável para pequeno porte
10. 📝 **Composição:** 71,5% é empreitada+materiais (25,65% + 45,88%)

### Adequação para Calibração

**✅ Macrogrupos confiáveis:** Gerenciamento, Mov.Terra, Infraestrutura, Impermeabilização, Rev.Internos Parede, Teto, Pisos, Pintura, Esquadrias, Fachada, Complementares

**⚠️ Com ressalva:** Supraestrutura (somar empreitada ou usar só materiais), Alvenaria (baixa), Instalações (muito baixa)

**🎯 Destaque:** Breakdown Supraestrutura (armadura/concreto/forma/compl.) excelente para calibração de proporções internas do macrogrupo

**📊 Índice global R$/m²:** Confiável (R$ 2.952,89 normalizado sem ger.) com ressalva de escala pequena (9 unidades)

**🔍 Dados insuficientes:** Prazo, detalhamento de instalações, levantamento de áreas, PUs de acabamentos, tipo de laje/fundação

---

## DADOS DE ENTRADA — PROJETO 45: Residencial Volo Home (PAL-VLH)

> **Fonte:** Orçamento Executivo + Apresentação Oficial (PPTX) — Data-base Nov/2023 (estimado)
> **Índices expandidos:** `orcamento-parametrico/indices/paludo-volohome-indices.md` (16 seções completas)
> **⚠️ CUB/RS USADO (NÃO CUB/SC)** — CUB/RS out/2023 = R$ 2.418,97. Projeto possivelmente no Rio Grande do Sul
> **⚠️ EMPREITADA GLOBAL MO** — R$ 3.670.000 (29,40%) não distribuída, impacta todos os macrogrupos

### Dados Gerais
- **AC:** 3.972,30 m² | **AT:** N/D | **AP:** N/D
- **UR:** ~29 un (estimado a partir de 29 churrasqueiras) | Tipologias: ~137 m²/un médios
- **Pavimentos:** N/D | **Prazo:** N/D
- **CUB/RS Out/23:** R$ 2.418,97 | **CUB Base (SC Dez/23):** R$ 2.752,67 | **Fator Normalização:** 1,1380
- **R$/m² (original):** 3.142,15 (1,299 CUB) | **R$/m² Norm.:** 3.575,55 | **Total (original):** R$ 12.481.581,97
- **Total Normalizado:** R$ 14.204.719,20
- **Laje:** N/D | **Fundação:** N/D | **Padrão:** Alto/Médio-Alto
- **Incorporador:** Paludo | **Local:** A confirmar (possivelmente RS)
- **Indicadores produto:** 93 infraestruturas ar-condicionado, 162 portas (77×70cm + 55×80cm + 30×90cm), 29 churrasqueiras

### Macrogrupos (R$/m² normalizado — CUB base Dez/23)

| Etapa | R$/m² Original | R$/m² Norm. | % | Obs |
|---|---|---|---|---|
| Gerenciamento Técnico/ADM | 250,39 | 284,89 | 7,97% | 🔽 -5% a -29% vs benchmark |
| **Empreitada Global (MO)** | **923,90** | **1.051,39** | **29,40%** | **⚠️ Não distribuída — verba única** |
| Mov. Terra | 32,87 | 37,40 | 1,05% | ⚠️ +56% a +212% (benchmark 18-24) |
| Infraestrutura | 60,53 | 68,89 | 1,93% | 🔽 **-59% a -71%** (CRÍTICO) |
| Supraestrutura (materiais) | 479,55 | 545,71 | 15,26% | 🔽 -24% a -29% (MO na empreitada) |
| Alvenaria | 70,80 | 80,57 | 2,25% | 🔽 -33% a -50% |
| Instalações | 168,30 | 191,50 | 5,36% | 🔽 -13% a -40% |
| Sist. Especiais | 98,76 | 112,38 | 3,14% | 🔽 -35% a -45% |
| Impermeabilização | 70,98 | 80,77 | 2,26% | ⚠️ +35% a +169% |
| Rev. Internos Piso/Parede | 126,75 | 144,24 | 4,03% | ✅ Dentro (-28% a +20%) |
| Teto | 54,13 | 61,60 | 1,72% | ✅ Dentro (-12% a +23%) |
| Pisos (Acabamentos) | 92,92 | 105,77 | 2,96% | 🔽 -38% a -47% |
| Pintura Interna | 165,47 | 188,28 | 5,27% | ⚠️ **+51% a +98%** (3,5× Volo Ocean) |
| Esquadrias | 328,25 | 373,57 | 10,45% | ⚠️ +29% a +49% |
| Cobertura + Complementares | 72,30 | 82,27 | 2,30% | 🔽 -25% a -59% |
| Imprevistos | 46,75 | 53,20 | 1,49% | ⚠️ Baixo (benchmark 2-5%) |

### Curva ABC — Top 5 Insumos (valores originais)

| Item | Valor (R$) | % Curva | R$/m² | R$/m² Norm. |
|---|---|---|---|---|
| 1. Empreitada MO Parte Civil | 3.670.000 | 32,7% | 923,90 | 1.051,39 |
| 2. Esquadrias Alumínio | 982.360 | 8,8% | 247,29 | 281,33 |
| 3. Armadura total | 931.537 | 8,3% | 234,50 | 266,86 |
| 4. MO terceiros (pintura + impermeab + bomb.) | 919.559 | 8,2% | 231,48 | 263,42 |
| 5. Concreto fck 30 bombeado | 756.973 | 6,7% | 190,56 | 216,86 |

> **Nota:** Curva ABC totaliza R$ 11.220.576 (89,9% do total)

### Breakdown Estrutura (estimativas — dados completos indisponíveis)

| Item | Estimativa | Índice | Ref. KIR | Ref. ADR |
|---|---|---|---|---|
| Concreto total | ~757 m³ | 0,191 m³/m² | 0,242 | 0,189 |
| Armadura total | 931.537 kg | 234,5 kg/m² | — | — |
| Taxa aço supra | — | 123 kg/m³ | 82,32 | 114,88 |
| PU concreto | ~R$ 1.000/m³ | — | — | — |
| PU aço | R$ 6,50-7,50/kg | — | 6,12-7,98 | — |

> **DESTAQUE:** Taxa aço 123 kg/m³ é ALTA (vs ref 82-115), indicando estrutura robusta ou maior densidade de armadura

### Índices Globais

| Índice | Valor Original | Valor Norm. | Un |
|---|---|---|---|
| R$/UR (29 UR est.) | R$ 430.399 | R$ 489.834 | R$/UR |
| AC/UR | 137,0 | 137,0 | m²/un |
| CUB/UR | 177,9 | 177,9 | CUB/un |
| Concreto / AC | 0,191 | — | m³/m² |
| Taxa aço supra | 123 | — | kg/m³ |
| Aço / AC | 234,5 | — | kg/m² |
| Portas / UR | 5,6 | — | un/UR |
| Churrasqueiras / UR | 1,0 | — | un/UR |
| Ar-condicionado / UR | 3,2 | — | un/UR |
| CI / AC | 284,89 | — | R$/m² (7,97%) |

### Comparativo Volo Home vs Volo Ocean (valores normalizados)

> **Volo Ocean:** CUB R$ 2.643,16 (dez/2022), R$ 3.438/m² → Normalizado R$ 3.583/m² (fator 1,042)

| Macrogrupo | Volo Home (R$/m²) | Volo Ocean (R$/m²) | Δ | Obs |
|---|---|---|---|---|
| Empreitada | 1.051,39 | 1.030,84 | +2,0% | Alinhado |
| Supraestrutura (mat.) | 545,71 | 421,07 | +29,6% | Home MAIOR |
| Instalações | 191,50 | 181,31 | +5,6% | — |
| Esquadrias | 373,57 | 327,19 | +14,2% | — |
| Fachada | 113,23 | 145,88 | -22,4% | Home MENOR |
| **Pintura** | **188,28** | **56,27** | **+234,6%** | **⚠️ Home 3,3× MAIOR** |

### Comparativo Portfólio Paludo (valores normalizados dez/2023)

| Projeto | Data-base | CUB | R$/m² Original | R$/m² Norm. | CUB Ratio |
|---|---|---|---|---|---|
| Barbados | Out/2021 | 2.381,34 | 2.554 | 2.953 | 1,07 |
| Nassau | Ago/2021 | 2.329,85 | 2.433 | 2.875 | 1,04 |
| Urban Life | Fev/2021 | 2.201,37 | 2.625 | 3.283 | 1,19 |
| Volo Ocean | Dez/2022 | 2.643,16 | 3.438 | 3.583 | 1,30 |
| **Volo Home** | **Nov/2023** | **2.418,97 (RS)** | **3.142** | **3.576** | **1,30** |

> **DESTAQUE:** Volo Home R$/m² normalizado (3.576) ALINHADO com Volo Ocean (3.583) e CUB ratio idêntico (1,30), demonstrando consistência Paludo apesar da estrutura atípica

### Destaques

1. ⚠️ **CUB/RS usado (não CUB/SC)** — CUB/RS out/2023 = R$ 2.418,97 é 12,1% MENOR que CUB/SC dez/2023 (R$ 2.752,67). Projeto possivelmente no RS (indicadores: churrasqueiras 1/UR típico gaúcho)
2. ⚠️ **Empreitada Global 29,40% não distribuída** — R$ 3.670.000 como verba única de MO. Impossível calibrar macrogrupos corretamente (MO ausente). Supraestrutura, Alvenaria, Rev. Internos, Fachada aparecem artificialmente baixos (só materiais)
3. ⚠️ **Infraestrutura 59-71% ABAIXO** — R$ 68,89/m² vs 170-240. CRÍTICO. Possível: fundação rasa/simples OU erro de classificação OU parte na empreitada
4. ⚠️ **Pintura 3,3× Volo Ocean** — R$ 188,28/m² vs R$ 54/m². Desvio +234%. Curva ABC: MO terceiros (pintura + impermeab + bombeamento) = R$ 919.559 (8,2%). Possível: alto padrão com múltiplas demãos/texturas OU erro de classificação
5. ⚠️ **Mov. Terra +56% a +212%** — R$ 37,40/m² vs 18-24. Possível rebaixamento/contenção
6. ⚠️ **Impermeabilização +35% a +169%** — R$ 80,77/m² vs 30-60. Sistemas de alto desempenho ou MO terceiros elevada
7. ⚠️ **Esquadrias +29% a +49%** — R$ 373,57/m² (10,45% do total). Alto padrão, grandes vãos
8. ⚠️ **Sist. Especiais -35% a -45%** — R$ 112,38/m² vs 173-206. Apesar de 93 infraestruturas A/C. Possível: climatização na empreitada
9. ⚠️ **Imprevistos 1,49%** — abaixo do benchmark (2-5%)
10. 📝 **Taxa aço 123 kg/m³** — ALTA vs benchmarks (82-115). Estrutura robusta
11. 📝 **Concreto 0,191 m³/m²** — eficiente vs KIR 0,242, alinhado com ADR 0,189
12. 📝 **R$/m² norm. 3.576 alinhado com portfólio Paludo** — Barbados/Nassau/Urban Life/Volo Ocean convergem para R$ 2.900-3.600/m² norm. e CUB ratio 1,07-1,30
13. 📝 **CUB ratio 1,30** — consistente com Volo Ocean (mesmo padrão)
14. 📝 **Churrasqueiras 1/UR** — típico gaúcho, reforça localização RS
15. 📝 **Gerenciamento 7,97%** — ABAIXO típico (10-12%), possível prazo curto ou equipe enxuta

### Adequação para Calibração

**⚠️ NÃO RECOMENDADO para calibração direta** — Estrutura de custos atípica com empreitada global não distribuída invalida os macrogrupos individuais

**✅ Uso alternativo:**
1. **R$/m² global normalizado (3.576)** — confiável como benchmark de custo total para projetos Paludo alto padrão
2. **CUB ratio (1,30)** — confiável como referência de padrão Paludo
3. **Curva ABC** — proporções de insumos (empreitada 32,7%, esquadrias 8,8%, armadura 8,3%, MO terceiros 8,2%, concreto 6,7%) úteis para validação
4. **Comparativo Volo Home vs Volo Ocean** — delta entre macrogrupos (pintura +234%, supra +30%, fachada -22%) indica variações de especificação

**🎯 Ação requerida antes da calibração:**
1. **Distribuir empreitada global** proporcionalmente aos macrogrupos com MO alta (Supra, Alvenaria, Rev. Internos, Pintura, Fachada) OU
2. **Documentar como "MO Global" separada** e calibrar apenas materiais OU
3. **Aguardar projeto Paludo com estrutura convencional** para calibração confiável

**🔍 Dados insuficientes:** Prazo, nº pavimentos, tipo laje/fundação, detalhamento instalações, áreas de serviço, PUs acabamentos, UR exato (estimado 29)

---

## DADOS DE ENTRADA — PROJETO 43: Parkside Rio Branco (Parkside, Florianópolis/SC)

> **Fonte:** Orçamento Executivo — Data-base Set/2025
> **Índices expandidos:** `orcamento-parametrico/parkside-riobranco-indices.md` (16 seções completas)
> **⚠️ STUDIOS MOBILIADOS** — Enxoval R$ 10,3M (25,1%) EXCLUÍDO da calibração
> **⚠️ EMPREITADA GLOBAL DISTRIBUÍDA** — R$ 10,8M (26,3%) com breakdown por disciplina (RARO)

### Dados Gerais
- **AC:** 8.660,10 m² | **AT:** 884,99 m² | **AP:** 5.303,81 m²
- **UR:** 163 un (160 residenciais + 3 comerciais) | Tipologias: Studios ~54 m²/un (compactos)
- **Pavimentos:** 22 (Sub2 700m² + Sub1 613m² + Térreo 560m² + Pav2 403m² + Garden 489m² + 15 Tipos 5.481m² + Cobertura 323m² + Barrilete 45m² + Reservatório 45m²)
- **Elevadores:** N/D (estim. 3-4) | **Prazo:** 33 meses (abr/2026 → dez/2028)
- **CUB/SC Ago/25:** R$ 2.978,02 | **R$/m²:** 3.559,33 (SEM enxoval, 1,20 CUB) / 4.753,80 (COM enxoval, 1,60 CUB) | **Total:** R$ 30.824.031 (SEM enxoval) / R$ 41.168.406 (COM enxoval)
- **Laje:** Concreto armado | **Fundação:** Sapatas + Cortina contenção | **Padrão:** Médio/Alto (studios mobiliados)
- **Incorporador:** Parkside | **Local:** Av. Rio Branco, Centro, Florianópolis/SC
- **TIPO ESTRUTURAL:** Concreto Armado + 2 subsolos escavados com contenção

### Macrogrupos (R$/m² SEM Enxoval — após distribuição empreitada)

| Etapa | R$/m² | R$/m² Norm. | % | Obs |
|---|---|---|---|---|
| Gerenciamento (+ Limpeza empr.) | 278,78 | 257,71 | 7,83% | ⚠️ Borda inferior (260-550) |
| Movimentação de Terra | 43,68 | 40,38 | 1,23% | ⚠️ Acima (10-20) — 2 subsolos |
| **Infraestrutura (+ Contenção empr.)** | **162,17** | **149,91** | **4,56%** | ✅ Dentro (115-344) |
| **Supraestrutura (mat + Civil empr.)** | **1.134,41** | **1.048,66** | **31,87%** | ⚠️ MUITO ALTA — MO 66% do total |
| Alvenaria | 85,88 | 79,40 | 2,41% | ⚠️ Abaixo (123-324) — studios |
| Impermeabilização | 47,53 | 43,94 | 1,34% | ✅ Borda inf. (43-94) |
| **Instalações (+ Hidro/Elétr empr.)** | **465,13** | **429,99** | **13,07%** | ⚠️ ACIMA similar (250-300) |
| Sistemas Especiais | 104,27 | 96,42 | 2,93% | ✅ Dentro (89-748) |
| **Climatização** | **54,98** | **50,82** | **1,54%** | ✅ Dentro (26-210) — **SEPARADO** |
| **Rev. Internos Parede (+ 50% Cerâm. empr.)** | **150,88** | **139,49** | **4,24%** | ✅ Dentro (107-425) |
| Teto | 124,04 | 114,67 | 3,49% | ⚠️ Acima similar (65-75) |
| **Pisos (+ 50% Cerâm. empr.)** | **232,02** | **214,48** | **6,52%** | ⚠️ Acima similar (160-180) |
| **Pintura (+ Pintura empr.)** | **138,33** | **127,88** | **3,89%** | ⚠️ Acima similar (100-120) |
| **Esquadrias (+ Portas/Rodapés empr.)** | **362,80** | **335,38** | **10,20%** | ✅ Topo similar (280-330) |
| **Louças e Metais (+ Louças empr.)** | **76,47** | **70,69** | **2,15%** | **⚠️ ACIMA (23-51)** — **SEPARADO** |
| **Fachada** | **18,36** | **16,98** | **0,52%** | **⚠️ MUITO ABAIXO (57-546)** — **RED FLAG** |
| Complementares | 45,85 | 42,38 | 1,29% | ✅ Borda inf. (49-995) |
| Imprevistos | 33,72 | 31,17 | 0,95% | ⚠️ Abaixo (48-174) — risco |

### Empreitada Global — Breakdown por Disciplina (RARO e VALIOSO)

| Disciplina | Valor (R$) | % Empreitada | Macrogrupo Destino |
|---|---|---|---|
| MO Civil (estrutura) | 6.499.068 | 60% | Supraestrutura |
| MO Pintura | 1.083.178 | 10% | Pintura |
| MO Revestimento Cerâmicos | 1.083.178 | 10% | Rev. Internos (50%) + Pisos (50%) |
| MO Instalações Hidrossanitárias | 649.907 | 6% | Instalações |
| MO Instalações Elétricas | 649.907 | 6% | Instalações |
| MO Instalação Portas/Rodapés | 324.953 | 3% | Esquadrias |
| MO Contenção | 216.636 | 2% | Infraestrutura |
| MO Limpeza e Ajudantes | 216.636 | 2% | Gerenciamento |
| MO Instalação Louças/Metais | 108.318 | 1% | Louças e Metais |
| **TOTAL Empreitada** | **10.831.779** | **100%** | — |

### Índices Globais (SEM Enxoval)

| Índice | Valor | Valor Norm. | Un |
|---|---|---|---|
| R$/UR | R$ 189.074 | R$ 174.778 | R$/UR |
| AC/UR | 53,13 | 53,13 | m²/un |
| AP/UR | 32,54 | 32,54 | m²/un |
| AP/AC | 61,2% | 61,2% | % |
| Coef. Aproveitamento (CA) | 9,78 | 9,78 | — |
| Ritmo construção | 262,4 | 262,4 | m²/mês |
| Burn rate (sem ger.) | R$ 934k | R$ 864k | R$/mês |
| R$/m²/mês | 108,42 | 100,22 | R$/m²/mês |
| UR/mês | 4,9 | 4,9 | UR/mês |
| CI / AC | 278,78 | 257,71 | R$/m² (7,83%) |

### Infraestrutura Detalhada

| Item | Valor (R$) | Valor Norm. (R$) | Observação |
|---|---|---|---|
| Serviços Preliminares (demolição) | 37.755 | 34.900 | — |
| Movimentação de Terra | 378.280 | 349.672 | Terraplanagem + escavação + bota-fora |
| Fundações Sapatas (material) | 885.092 | 818.189 | Forma + armadura + piso concreto + concreto 30MPa |
| Contenção Cortina (material) | 278.469 | 257.430 | Forma + armadura + concreto |
| Contenção MO (empreitada) | 216.636 | 200.255 | Empreitada global (2%) |
| Drenagem | 24.169 | 22.342 | — |
| **TOTAL Infraestrutura** | **1.404.366** | **1.298.236** | — |

### Destaques

1. **⚠️ ENXOVAL MOBILIADO R$ 10,3M (25,1%)** — Studios MOBILIADOS. Enxoval EXCLUÍDO da calibração. COM enxoval: R$ 4.754/m², CUB 1,60 (MUITO ALTO). SEM enxoval: R$ 3.559/m², CUB 1,20 (ALTO, mas justificável)
2. **✅ EMPREITADA GLOBAL DISTRIBUÍDA** — R$ 10,8M (26,3%) com breakdown detalhado por disciplina (civil 60%, pintura 10%, cerâmicos 10%, hidro 6%, elétr 6%, portas 3%, contenção 2%, limpeza 2%, louças 1%). RARO e VALIOSO — permite separar Mat vs MO nos macrogrupos
3. **✅ CLIMATIZAÇÃO SEPARADA** — R$ 476k (R$ 55/m², 1,54%) — exaustão, pressurização, SPDA. RARO ter separado de Instalações
4. **✅ LOUÇAS E METAIS SEPARADOS** — R$ 662k (R$ 76/m², 2,15%) — material + MO empreitada. RARO ter separado. R$ 4.063/UR — alto, mas justificável por 163 kits completos
5. **⚠️ FACHADA SUBDIMENSIONADA** — R$ 18,36/m² é 9× MENOR que faixa mínima (57-546). Rev. Argamassa + Pintura = R$ 159k total. POSSÍVEL: revestimento fachada (ACM, cerâmica, pastilha) classificado em Esquadrias ou Acabamentos. **RED FLAG — VERIFICAR EXECUTIVO ORIGINAL antes de calibrar**
6. **⚠️ SUPRAESTRUTURA R$ 1.049/m² (31,87%)** — MUITO ALTA. Material R$ 3,3M + MO Civil (empr.) R$ 6,5M = R$ 9,8M total. **MO representa 66,2% do total de supra** — proporção muito alta, indicando: (1) 22 pavimentos verticalizados, (2) MO cara em Florianópolis, (3) contenção complexa + altura. Comparativo: Urban Life R$ 655/m² (12 pav., MO embutida) | Barbados R$ 1.118/m² (3 pav., mat + empr. separada)
7. **⚠️ INSTALAÇÕES R$ 465/m² (13,07%)** — ACIMA faixa similar (250-300), dentro geral (240-623). Material R$ 2.728k + MO Hidro+Elétr (empr.) R$ 1.300k = R$ 4.028k total. **Justificável:** 163 unidades + 22 pavimentos → prumadas longas, maior consumo. Comparativo: Urban Life R$ 324/m² (dentro), Barbados R$ 159/m² (subdimensionado). **Parkside tem instalações adequadamente orçadas**
8. **⚠️ IMPREVISTOS 0,95%** — R$ 292k (R$ 33,72/m²) é muito abaixo benchmark (2-5%). Margem baixa para contingências — projeto vulnerável a variações
9. **⚠️ LOUÇAS/METAIS ACIMA FAIXA** — R$ 76/m² vs 23-51. **Causa:** densidade de unidades alta (163 UR em 8.660 m² = 0,0188 UR/m²). R$ 4.063/UR é razoável para studios mobiliados padrão médio/alto. **Para calibração:** ajustar por densidade — `Louças/m² = R$ 4.000/UR × (UR/AC)`
10. 📝 **CUB ratio 1,20 (SEM enxoval)** — ALTO para padrão médio, mas justificável por: (1) studios compactos (54 m²/un) — maior custo fixo por m², (2) centro Florianópolis — terreno caro, fundação urbana, (3) 2 subsolos com contenção cortina, (4) 22 pavimentos — estrutura verticalizada, (5) 163 unidades — alta densidade de instalações/louças/esquadrias
11. 📝 **Verticalização intensa** — CA 9,78, 22 pavimentos em 885 m² terreno. Ritmo 262 m²/mês (1,6× Urban Life)
12. 📝 **Contenção Total R$ 495k** — Material R$ 278k + MO (empr.) R$ 217k = R$ 495k (R$ 57,17/m² AC)
13. 📝 **Densidade de unidades** — 1 UR cada 53 m² (vs Urban Life 1 UR cada 147 m²). Explica alto custo de Louças/Metais, Instalações, Esquadrias por m²
14. 📝 **MO Supraestrutura 66,2%** — Material R$ 3,3M (33,8%) + MO R$ 6,5M (66,2%) = R$ 9,8M supra. Proporção muito acima típico (40-50% MO)

### Adequação para Calibração

**✅ EXCELENTE para calibração** — com ressalvas documentadas

**🎯 Macrogrupos confiáveis:**
- Infraestrutura + Contenção (R$ 149,91/m² norm.) — com 2 subsolos
- Supraestrutura Mat+MO (R$ 1.048,66/m² norm.) — verticalização intensa
- Instalações Mat+MO (R$ 429,99/m² norm.) — alta densidade UR
- Climatização separada (R$ 50,82/m² norm.) — RARO
- Impermeabilização (R$ 43,94/m² norm.)
- Rev. Internos, Teto, Pisos, Pintura, Esquadrias
- Complementares

**⚠️ Macrogrupos com ressalva:**
- **Louças e Metais** (R$ 70,69/m² norm.) — ACIMA faixa, mas justificável por densidade. **Calibrar ajustado por UR/AC**
- **Fachada** (R$ 16,98/m² norm.) — MUITO ABAIXO. **VERIFICAR antes de calibrar** — possível subdimensionamento ou classificação em outro macrogrupo
- Alvenaria (R$ 79,40/m² norm.) — abaixo faixa, mas justificável por studios compactos
- Gerenciamento (R$ 257,71/m² norm.) — borda inferior faixa
- Imprevistos (R$ 31,17/m² norm.) — abaixo faixa, risco

**🎯 Valor EXCEPCIONAL:**
1. **Empreitada distribuída** — permite separar Mat vs MO em 9 macrogrupos (RARO)
2. **Enxoval separado** — permite calibração com/sem mobiliário
3. **Climatização separada** — RARO
4. **Louças/Metais separados** — RARO
5. **Verticalização intensa (22 pav.)** — referência para obras altas com contenção
6. **Alta densidade UR** — referência para studios/compactos

**🔍 Dados insuficientes:**
- Detalhamento instalações por disciplina (hidro/elétrica/preventiva não separados no executivo)
- Breakdown supraestrutura por pavimento (apenas total disponível)
- PUs de acabamentos detalhados
- Levantamento de áreas (alvenaria/AC, forro/AC, pintura/AC)
- **Fachada detalhada** — CRÍTICO para calibração

**📊 Complementaridade com outros projetos:**
- **Urban Life:** escala média (48 UR, 12 pav., terreno plano) — complementa Parkside (163 UR, 22 pav., contenção)
- **Barbados:** escala pequena (9 UR, 3 pav., litoral) — complementa espectro de complexidade
- **Parkside cobre:** obras verticalizadas (>15 pav.) com contenção + alta densidade UR + studios compactos
