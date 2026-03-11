# Orçamento Paramétrico — 2cinco4 Edition

> Projeto: Edif. Comercial/Residencial Multifamiliar
> Local: Ruas 254 e 254A, Meia Praia, Itapema/SC
> Proprietário: Família H Empreendimentos
> Data da estimativa: 04/03/2026
> Base de regras: CTN-IVC-LRJ Gerenciamento Executivo R00

---

## 1. DADOS DE ENTRADA (extraídos dos PDFs)

### 1.1 Dados do Terreno
| Item | Valor |
|------|-------|
| Localização | Ruas 254 e 254A, Meia Praia, Itapema/SC |
| Lotes | 25, 27, 28 e 29 |
| Área do Terreno (AT) | ~900 m² (estimado das dimensões) |
| Zoneamento | Não especificado nos PDFs |

### 1.2 Programa do Edifício

| Pavimento | Nível (m) | Pé-direito | Área Estimada (m²) |
|-----------|-----------|------------|-------------------|
| Nível da Rua | -0,13 | — | — |
| 1° Pavto Térreo (comercial) | 0,32 | 3,60 | 863 |
| 2° Pavto Garagem 01 + Lazer 01 | 3,92 | 3,06 | 869 |
| 3° Pavto Garagem 02 + Lazer 02 | 6,98 | 3,24 | 882 |
| Mezanino 3° Pavto | 10,22 | 3,78 | 678 |
| 4° Pavto Tipo 01 | 14,00 | 3,24 | 403 |
| 5° ao 25° Pavto Tipo 02 (×21) | 17,24 a 82,04 | 3,24 | 302 × 21 = 6.342 |
| 26° Pavto Rooftop | 85,28 | 3,24 | 271 |
| Cobertura | 88,52 | 2,20 | 26 |
| Casa de Máquinas | 90,72 | 2,20 | 8 |
| Cx d'Água | 92,92 | 2,00 | 34 |
| Tampa Cx d'Água | 94,92 | — | — |
| **TOTAL** | | | **~10.503** |

### 1.3 Variáveis Paramétricas (DADOS_INICIAIS)

| Sigla | Descrição | Valor | Fonte |
|-------|-----------|-------|-------|
| **AC** | Área Total Construída | **10.503 m²** | Soma dos pavimentos |
| **APE** | Área Projeção Embasamento | **870 m²** | Footprint base (térreo) |
| **APT** | Área Projeção Torre | **350 m²** | Footprint torre (tipo 02 ≈ 302 m² + paredes) |
| **NP** | Nº Total de Pavimentos | **30** | Térreo a Tampa Cx |
| **NPT** | Nº Pavimentos Tipo | **22** | 1 tipo 01 + 21 tipo 02 |
| **UR** | Unidades Residenciais | **44** | 2 (tipo 01) + 42 (tipo 02) |
| **UC** | Unidades Comerciais | **9** | Térreo |
| **NE** | Nº Elevadores | **2** | 3,51 + 3,80 m² |
| **NS** | Nº Subsolos | **0** | Garagens acima do nível |
| **CHU** | Churrasqueiras | **45** | 44 sacadas gourmet + 1 lazer (estimado) |
| **AL** | Área de Lazer | **700 m²** | Base (489) + Rooftop (211) |
| **PPT** | Perímetro Projeção Torre | **~76 m** | 2×(23,26+14,70) estimado |
| **NQ** | Nº Quartos/Dormitórios | **132** | 3 suítes × 44 aptos |
| **NB** | Nº Banheiros | **176** | 4 BWC × 44 aptos (3BWC + 1 lavabo) |
| **HE** | Altura do Edifício | **95 m** | -0,13 a 94,92 |
| **NVAGAS** | Nº Vagas | **55** | Distribuídas em 3 pavimentos |

---

## 2. QUANTITATIVOS PARAMÉTRICOS

### 2.1 Movimentação de Terra
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Escavação valas | 1,3 × Vol.infra (est.) | ~780 | m³ |
| Lastro concreto magro | 0,8 × APE | 696 | m² |
| Aterro compactado | ~0,5 × APE | 435 | m³ |
| Bota-fora (c/ empolamento 1,30) | Vol.escav × 1,3 | ~1.014 | m³ |

### 2.2 Contenções
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Forma parede contenção | 2,1 × APE | 1.827 | m² |
| Concreto parede contenção | 0,65 × APE × 1,05 | 594 | m³ |
| Armação contenção | 70 kg/m³ × Vol. | 41.580 | kg |

### 2.3 Infraestrutura (Fundações)
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Nº estacas (fundação) | 0,14 × APE | 122 | un |
| Nº estacas (cortina) | 0,15 × APE | 131 | un |
| Forma blocos/baldrames | 1,1 × APE | 957 | m² |
| Concreto blocos/baldrames | 0,6 × APE × 1,05 | 548 | m³ |
| Armação blocos/baldrames | 70 kg/m³ × Vol. | 38.360 | kg |

### 2.4 Supraestrutura (considerando Laje Cubetas — variante mais comum)
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Montagem forma (3 jogos) | 1,1 × AC | 11.624 | m² |
| Concreto estrutural | 0,23 × AC × 1,05 | 2.552 | m³ |
| Armadura | 78 kg/m³ × Vol. | 199.056 | kg (~199 ton) |
| MO estrutura | 290 R$/m² × AC | R$ 3.064.430 | |

### 2.5 Alvenaria (Convencional)
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Alvenaria externa | 0,6 × AC | 6.340 | m² |
| Alvenaria interna | 0,8 × AC | 8.454 | m² |
| **Total alvenaria** | | **14.794** | **m²** |
| Alvenaria escadas (c/ perda 1,05) | ~NPT × perímetro escada | ~400 | m² |

### 2.6 Revestimentos Internos
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Contrapiso | 0,62 × AC | 6.552 | m² |
| Manta acústica | 80% do contrapiso | 5.241 | m² |
| Chapisco | (alv.ext + alv.int) × 2 - fachada | ~23.000 | m² |

### 2.7 Teto/Forro
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Forro total | 0,6 × AC | 6.340 | m² |
| Estucamento | 0,2 × AC | 2.113 | m² |

### 2.8 Esquadrias
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Esquadrias alumínio | 0,15 × AC | 1.585 | m² |
| PCF (portas corta-fogo) | 2 × NP | 60 | un |
| Corrimão | 11 × NP | 330 | m |

### 2.9 Fachada
| Serviço | Fórmula | Quantidade | Unidade |
|---------|---------|-----------|---------|
| Perímetro fachada total | PPT × NPT × pé-direito | 76 × 22 × 3,24 = 5.417 | m² |
| *Deduzir esquadrias* | ~30% (estimado) | -1.625 | m² |
| **Fachada líquida** | | **~3.792** | **m²** |

---

## 3. CUSTOS PARAMÉTRICOS (R$/m² AC)

### 3.1 Verbas Diretas (índice R$/m² × AC)
| Serviço | Índice R$/m² | AC (m²) | Custo (R$) |
|---------|-------------|---------|-----------|
| Instalações Elétricas | 153,50 | 10.567 | 1.622.035 |
| Instalações Hidrossanitárias | 145,00 | 10.567 | 1.532.215 |
| Instalações Preventivas + GLP | 41,00 | 10.567 | 433.247 |
| **Subtotal Instalações** | **339,50** | | **3.587.497** |
| Pintura interna geral | 75,00 | 10.567 | 792.525 |
| Rev. parede (acabamento) | 45,00 | 10.567 | 475.515 |
| Rodapés | 30,00 | 10.567 | 317.010 |
| Textura escadas | 25,00 | 10.567 | 264.175 |
| Soleiras e peitoris | 20,00 | 10.567 | 211.340 |
| Limpeza | 15,00 | 10.567 | 158.505 |
| Paisagismo | 11,00 | 10.567 | 116.237 |
| Comunicação visual | 10,00 | 10.567 | 105.670 |
| Serralheria | 5,00 | 10.567 | 52.835 |
| Desmobilização | 5,00 | 10.567 | 52.835 |
| Ligações definitivas | 4,00 | 10.567 | 42.268 |
| **Subtotal Verbas R$/AC** | **584,50** | | **6.176.412** |

### 3.2 Verbas por Área de Lazer
| Serviço | Índice | Base | Custo (R$) |
|---------|--------|------|-----------|
| Móveis/decoração lazer | 1.500 R$/m² | 700 m² (AL) | 1.050.000 |

### 3.3 MO Estrutura
| Serviço | Índice | Base | Custo (R$) |
|---------|--------|------|-----------|
| MO supraestrutura (cubetas) | 290 R$/m² | 10.567 m² | 3.064.430 |
| MO contenção (×1,5) | 435 R$/m² | ~870 m² (APE) | 378.450 |
| MO infra (×1,5) | 435 R$/m² | ~870 m² (APE) | 378.450 |

### 3.4 Fator BDI
Todos os valores acima devem ser multiplicados por **1,10 (BDI 10%)**.

---

## 4. RESUMO PARCIAL DE CUSTOS

*⚠️ PARCIAL — inclui apenas itens com índice R$/m² direto. Falta: materiais estruturais, esquadrias, fachada, impermeabilização, cobertura, elevadores, revestimentos de piso, e outros itens que dependem de preços unitários.*

| Grupo | Custo s/ BDI (R$) | Com BDI (×1,10) |
|-------|--------------------|-----------------|
| Instalações (elétrica + hidro + preventivas) | 3.587.497 | 3.946.247 |
| MO Supraestrutura | 3.064.430 | 3.370.873 |
| Pintura | 1.056.700 | 1.162.370 |
| Acabamentos (rev. parede + rodapés + soleiras) | 1.003.865 | 1.104.252 |
| Móveis/decoração lazer | 1.050.000 | 1.155.000 |
| MO Contenção + Infra | 756.900 | 832.590 |
| Complementares (limpeza + paisagismo + com.visual + desm. + ligações) | 475.515 | 523.067 |
| Serralheria | 52.835 | 58.119 |
| **SUBTOTAL PARCIAL** | **11.047.742** | **~12.152.517** |

### Custo/m² parcial: ~R$ 1.052/m² (sem BDI) | ~R$ 1.157/m² (com BDI)

*Para referência: custo total típico de construção residencial multifamiliar alto padrão em SC (2024-2025): R$ 3.500 - 5.500/m². O subtotal parcial acima (~R$ 1.117/m²) cobre aproximadamente 25-30% do custo total, o que é coerente pois faltam os itens de material mais pesados (concreto, aço, esquadrias de alumínio, elevadores, fachada).*

---

## 5. QUANTIDADES-CHAVE PARA COTAÇÃO

*Itens que dependem de preços unitários (Sienge/TCPO/cotação) para completar o orçamento:*

| Item | Quantidade | Unidade | Observação |
|------|-----------|---------|------------|
| Estacas (fundação) | 122 | un | Tipo e profundidade: a definir (sondagem) |
| Estacas (cortina) | 131 | un | Idem |
| Concreto blocos/baldrames | 548 | m³ | Com perda 5% |
| Concreto contenção | 594 | m³ | Com perda 5% |
| Concreto supraestrutura | 2.552 | m³ | Cubetas, com perda 5% |
| Armadura total | ~280 | ton | Fundação + contenção + supra |
| Forma (3 jogos) | 11.624 | m² | Cubetas |
| Alvenaria total | 14.794 | m² | Ext 6.340 + Int 8.454 |
| Contrapiso | 6.552 | m² | |
| Manta acústica | 5.241 | m² | |
| Forro | 6.340 | m² | |
| Esquadrias alumínio | 1.585 | m² | |
| PCF | 60 | un | |
| Corrimão | 330 | m | |
| Fachada (líquida) | ~3.792 | m² | Revestimento/pintura |
| Elevadores | 2 | un | ~27 paradas |
| Porcelanato (≈ contrapiso) | ~6.552 | m² | |

---

## 6. PREMISSAS E LIMITAÇÕES

### PDFs analisados (14 de ~15):
✅ 01 - Implantação e Situação
✅ 02 - 1° Pavto Térreo
✅ 03 - 2° Pavto Garagem 01 e Lazer 01
✅ 04 - 3° Pavto Garagem 02 e Lazer 02
✅ 05 - Mezanino 3° Pavto
✅ 06 - 4° Pavto Tipo 01
✅ 07 - Pavto Tipo 02 (×21)
✅ 07A - Variações Aptos Tipo
✅ 10 - Corte AA'
✅ 11 - Corte BB'
✅ 12 - Fachada Rua 254
✅ 13 - Fachada Rua 254 A
✅ 14 - Fachada Lateral Esquerda
✅ 15 - Fachada Lateral Direita
✅ 08 - 26° Pavto Rooftop
✅ 09 - Cobertura e Cx d'Água

### Premissas assumidas:
1. **AC estimado por soma de áreas dos planos** — um quadro de áreas oficial daria valor preciso
2. **APE estimado pelo footprint do térreo** (~870 m²) — pode variar
3. **Churrasqueiras = 45** (1 por apto + 1 lazer) — confirmar se sacada gourmet inclui churrasqueira de alvenaria
4. **Tipo de fundação: estacas** — depende de sondagem
5. **Supraestrutura: Cubetas** — variante mais comum, mas precisa confirmação do projetista
6. **Preços unitários não incluídos** — regras documentadas são de outra obra (CTN-IVC-LRJ), servem como referência paramétrica mas devem ser atualizados
7. **Área do terreno estimada** — sem matrícula ou levantamento planialtimétrico

### Rooftop (26° Pavto — extraído do PDF 08):
- Área Descanso: 12,84 m²
- Estar: 20,22 m² + 56,16 m² = 76,38 m²
- Massagem: 9,19 m²
- Ducha/Cromoterapia: 8,61 m²
- Sauna: 7,87 m²
- Academia: 69,47 m²
- Espaço Yoga: 27,10 m²
- Hall: 13,32 m²
- BWC PCD: 4,25 m² + Lavabo: 3,67 m² + Lavabo PCD: 3,69 m²
- Área espera escada: 10,93 m²
- Antecâmara + Elevadores + Escadaria: ~28,48 m²
- **Total Rooftop: ~271 m²** (lazer útil: ~211 m²)
- Laje Split: Academia + Massagem/Estar
- Jardins externos (não computados na área)

### Cobertura (PDF 09):
- Circulação: 8,06 + 3,86 = 11,92 m²
- Mangotinho: 6,27 m²
- Casa de Máquinas: 3,80 + 4,02 = 7,82 m²
- Telhado: Fibrocimento i=10%, Calha Metálica i=2%
- Cx d'Água: Célula 01 (14,78 m²) + Célula 02 (19,22 m²) = 34,00 m² — paredes em concreto
- Tampa Cx d'Água: laje impermeabilizada nível 94,92

### Para completar o orçamento, faltam:
- [ ] Quadro de áreas oficial (AC preciso)
- [ ] Sondagem (tipo e profundidade de fundação)
- [ ] Definição do sistema estrutural (supraestrutura)
- [ ] Preços unitários atualizados (Sienge/TCPO/cotação)
- [ ] Projeto de fachada (tipo de revestimento, pele de vidro, etc.)
- [ ] Nº exato de churrasqueiras
