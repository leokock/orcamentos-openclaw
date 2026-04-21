# SPDA - Sistema de Proteção contra Descargas Atmosféricas
**Projeto:** Thozen Electra  
**Disciplina:** 11 SPDA  
**Revisão:** R00  
**Responsável Técnico:** R. Rubens Alves  
**Data da Análise:** 2026-03-20  
**Mapeamento Memorial:** N1 07 Instalações Elétricas → N2 07.02 SPDA

---

## 1. RESUMO EXECUTIVO

Sistema de proteção contra descargas atmosféricas para edifício residencial vertical com 32 níveis (~87m de altura), conforme NBR 5419. O projeto contempla:

- **4 descidas principais** com cabo de cobre nu 50mm²
- **Sistema de captação** na cobertura (Casa de Máquinas)
- **5 anéis equipotenciais** distribuídos ao longo da altura
- **Sistema de aterramento** com hastes cobreadas e malha horizontal
- **Conexões e acessórios** para interligação de todos os elementos

### Características do Edifício
- **Altura total:** ~87m (estimado)
- **Pavimentos:** 32 (Térreo + 5 garagens + Lazer + 24 tipos + Casa de Máquinas)
- **Tipo:** Residencial vertical
- **Nível de proteção (estimado):** III ou IV (conforme NBR 5419-2)

---

## 2. PREMISSAS TÉCNICAS

### 2.1. Normas Aplicáveis
- NBR 5419:2015 — Proteção contra descargas atmosféricas (partes 1 a 4)
- NBR 5410:2004 — Instalações elétricas de baixa tensão

### 2.2. Estrutura Vertical
| Nível | Descrição | Observação |
|-------|-----------|------------|
| Casa de Máquinas | Cobertura | Sistema de captação principal |
| 9º~31º Pavto | Tipo (23x) | Pavimentos repetidos |
| 8º Pavto | Tipo | Primeiro pavimento tipo |
| 7º Pavto | Lazer | Andar de lazer |
| 6º Pavto | G5 | Garagem |
| 5º Pavto | G4 | Garagem |
| 4º Pavto | G3 | Garagem |
| 3º Pavto | G2 | Garagem |
| 2º Pavto | G1 | Garagem |
| 1º Pavto | Térreo | Pavimento térreo |

### 2.3. Premissas de Cálculo
- **Altura do edifício:** ~87m (Térreo 3m + Garagens 5×2.7m + Lazer 3m + Tipos 24×2.5m + Casa Máq. 4m)
- **Número de descidas:** 4 (conforme NBR 5419 — mínimo 2, recomendado 1 a cada 20m de perímetro)
- **Espaçamento entre descidas:** ~30m (perímetro estimado ~120m)
- **Anéis equipotenciais:** 5 (a cada ~17m de altura, conforme NBR 5419 — máximo 20m)
- **Bitola dos condutores:** 50mm² descidas, 35mm² anéis (conforme NBR 5419 Tab. 6)
- **Sistema de aterramento:** Misto (hastes verticais + malha horizontal)

### 2.4. Limitações da Análise
⚠️ **IMPORTANTE:** Os quantitativos apresentados são **ESTIMATIVAS TÉCNICAS** baseadas em:
- Análise da estrutura de pavimentos (10 arquivos DWG)
- Premissas típicas de projetos de SPDA conforme NBR 5419
- Dimensões estimadas a partir de edifícios similares

**Não foi possível extrair quantitativos precisos dos arquivos DWG** (formato proprietário AutoCAD). Para levantamento detalhado, é necessário:
1. Conversão dos DWGs para DXF ou PDF com cotas
2. Acesso aos arquivos no AutoCAD/software compatível
3. Confirmação das dimensões reais (perímetro, distâncias, alturas)

---

## 3. QUANTITATIVOS ESTIMADOS

### 3.1. Sistema de Captação (Cobertura)

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Captor tipo Franklin | Haste aço inox 304, h=0.6m, Ø 1/2" | un | 6 | Distribuídos na cobertura (Casa de Máquinas) |
| Base para captor | Chapa aço galvanizado 200×200×5mm | un | 6 | Fixação na laje de cobertura |
| Chumbador | M10 × 100mm, aço galvanizado | un | 24 | 4 por base de captor |
| Conector captor-descida | Bronze, para cabo 50mm² | un | 6 | Interligação captor com cabo de descida |

**Observação:** Quantidade de captores estimada para cobertura típica de ~400m². Verificar projeto arquitetônico para dimensões reais e posicionamento conforme raio de proteção (método Franklin ou Faraday).

---

### 3.2. Sistema de Descidas

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Cabo de cobre nu | 50mm², têmpera mole, NBR 13248 | m | **354** | 4 descidas × 87m × 1.02 (fator de trajeto) |
| Braçadeira de fixação | Aço galvanizado, p/ cabo 50mm² | un | 176 | 1 a cada 0.5m de descida (4 desc. × 87m / 0.5m) |
| Bucha e parafuso | M8 × 60mm, aço galvanizado | un | 352 | 2 por braçadeira |
| Caixa de inspeção | 300×300×300mm, alvenaria c/ tampa concreto | un | 8 | 2 por descida (topo e base) |
| Conector aparafusado | Bronze, 50mm², parafuso fendido | un | 32 | Conexões nas caixas de inspeção |

**Trajeto das descidas:**
- Casa de Máquinas → Tipos → Lazer → Garagens → Térreo → Aterramento
- Descidas distribuídas nas quinas/faces do edifício
- Trajeto preferencial: prumadas de shafts ou fachadas

---

### 3.3. Anéis Equipotenciais

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Cabo de cobre nu | 35mm², têmpera mole, NBR 13248 | m | **600** | 5 anéis × 120m (perímetro estimado) |
| Conector aparafusado | Bronze, 35mm², parafuso fendido | un | 100 | Conexões entre trechos e com descidas |
| Braçadeira de fixação | Aço galvanizado, p/ cabo 35mm² | un | 300 | 1 a cada 2m de anel |

**Localização dos anéis equipotenciais (estimado):**
- Anel 1: Térreo (~0m)
- Anel 2: 4º Pavto G3 (~17m)
- Anel 3: 7º Pavto Lazer (~34m)
- Anel 4: 15º Pavto Tipo (~51m)
- Anel 5: 23º Pavto Tipo (~68m)

**Função:** Equipotencialização de elementos metálicos (ferragens estruturais, esquadrias, tubulações) e distribuição do potencial elétrico ao longo da altura.

---

### 3.4. Sistema de Aterramento

#### 3.4.1. Hastes de Aterramento

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Haste de aterramento | Cobreada Ø 5/8" × 2.4m, NBR 13571 | un | 8 | 2 hastes por descida |
| Conector haste-cabo | Bronze, tipo soldável ou compressão | un | 8 | 1 por haste |
| Caixa de inspeção aterramento | 400×400×400mm, alvenaria c/ tampa concreto | un | 4 | 1 para cada par de hastes |
| Solda exotérmica | Cartucho p/ cabo 50mm² + haste 5/8" | un | 8 | Conexão haste-cabo |

#### 3.4.2. Malha de Aterramento Horizontal

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Cabo de cobre nu (malha) | 50mm², têmpera mole, NBR 13248 | m | **1000** | Malha enterrada a 0.6-0.8m de profundidade |
| Conector aparafusado (malha) | Bronze, 50mm², parafuso fendido | un | 60 | Interligações da malha |
| Solda exotérmica (malha) | Cartucho p/ cabo 50mm² | un | 40 | Conexões críticas da malha |

**Configuração estimada da malha:**
- Área: ~200m² (ao redor do perímetro do edifício)
- Espaçamento: reticulado ~5m × 5m
- Profundidade: 0.6m mínimo
- Conexão com hastes verticais e eletrodo estrutural (caso existente)

---

### 3.5. Conexões e Acessórios Gerais

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Conector paralelo | Bronze, 50mm², derivação | un | 20 | Derivações ao longo das descidas |
| Conector cruzado | Bronze, 35-50mm², interseção | un | 20 | Conexões anéis × descidas |
| Arruela de pressão | Bronze, M10 | un | 200 | Complemento de conectores aparafusados |
| Fita de advertência | "SPDA - Não Remover", PVC | m | 100 | Sinalização ao longo das descidas |
| Caixa de inspeção subsolo | 400×400×400mm, c/ tampa articulada | un | 4 | Acesso ao sistema de aterramento |

---

### 3.6. Equipotencialização de Sistemas

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Barra equipotencial | Cobre eletrolítico 20×3mm, 300mm | un | 8 | Quadros elétricos (QGF, QGB) |
| Conector barra-cabo | Bronze, p/ barra 20mm + cabo 35mm² | un | 16 | Interligação barras com anéis |
| Cabo de cobre flexível | 25mm², isolado 750V verde | m | 80 | Equipotencialização de quadros e prumadas metálicas |

**Elementos a equipotencializar (conforme NBR 5419-3):**
- Ferragens estruturais (pilares, vigas)
- Esquadrias metálicas (janelas, portas)
- Tubulações metálicas (hidráulica, gás, esgoto)
- Quadros elétricos (QGF, QGB, QD apartamentos)
- Prumadas de elevadores e escadas metálicas
- Tanques, reservatórios e estruturas metálicas

---

## 4. RESUMO DE QUANTITATIVOS (TOTALIZADORES)

### 4.1. Condutores

| Item | Bitola | Quantidade (m) |
|------|--------|----------------|
| Cabo de cobre nu (descidas) | 50mm² | 354 |
| Cabo de cobre nu (anéis equipotenciais) | 35mm² | 600 |
| Cabo de cobre nu (malha aterramento) | 50mm² | 1000 |
| Cabo de cobre flexível (equipotencialização) | 25mm² | 80 |
| **TOTAL CONDUTORES** | — | **2034** |

### 4.2. Elementos Principais

| Categoria | Quantidade |
|-----------|------------|
| Captores tipo Franklin | 6 un |
| Descidas (trajetos) | 4 un |
| Hastes de aterramento 5/8" × 2.4m | 8 un |
| Anéis equipotenciais | 5 un |
| Caixas de inspeção (total) | 16 un |

### 4.3. Conexões e Fixações

| Categoria | Quantidade |
|-----------|------------|
| Conectores aparafusados bronze | 212 un |
| Braçadeiras de fixação | 476 un |
| Soldas exotérmicas | 48 un |
| Chumbadores e parafusos | 400+ un |

---

## 5. MEMORIAL DE CÁLCULO (VALIDAÇÃO)

### 5.1. Verificação do Número de Descidas (NBR 5419-3, item 5.3.4)

**Critério:** Distância entre descidas ≤ 20m (nível de proteção III) ou ≤ 25m (nível IV)

Premissas:
- Perímetro estimado: 120m
- 4 descidas → espaçamento médio: 120m / 4 = **30m**

⚠️ **Não conformidade parcial:** Espaçamento de 30m excede o recomendado. Sugestão:
- **Nível de proteção IV:** 30m > 25m → considerar 5 ou 6 descidas
- **Nível de proteção III:** 30m > 20m → considerar 6 descidas

**Ação recomendada:** Verificar no projeto DWG o perímetro real e o nível de proteção especificado. Ajustar número de descidas conforme necessário.

---

### 5.2. Verificação dos Anéis Equipotenciais (NBR 5419-3, item 5.4.2.2)

**Critério:** Anéis a cada 20m de altura (nível III) ou a cada espaçamento equivalente ao nível de proteção

Premissas:
- Altura do edifício: 87m
- 5 anéis → espaçamento médio: 87m / 5 = **17.4m** ✅

**Status:** Conforme NBR 5419 para nível de proteção III.

---

### 5.3. Verificação das Bitolas (NBR 5419-3, Tabela 6)

| Elemento | Bitola Especificada | Bitola Mínima NBR | Status |
|----------|---------------------|-------------------|--------|
| Descidas (cobre) | 50mm² | 35mm² (Nível III-IV) | ✅ Conforme |
| Anéis (cobre) | 35mm² | 35mm² (Nível III-IV) | ✅ Conforme |
| Malha aterramento | 50mm² | 50mm² (enterrado) | ✅ Conforme |

**Status:** Bitolas adequadas conforme NBR 5419.

---

### 5.4. Verificação do Sistema de Aterramento (NBR 5419-3, item 5.5)

**Critério:** Resistência de aterramento ≤ 10Ω (recomendado)

Premissas:
- 8 hastes cobreadas 5/8" × 2.4m
- Malha horizontal ~1000m de cabo 50mm²
- Solo típico (resistividade 100-500 Ω·m)

**Estimativa conservadora:**
- Resistência de 1 haste isolada: ~25-50Ω
- Resistência de 8 hastes em paralelo (fator de redução 0.6): ~10-20Ω
- Resistência da malha horizontal: ~5-15Ω
- **Resistência total (hastes + malha):** ~3-10Ω ✅

**Status:** Sistema de aterramento adequado para maioria dos solos. Recomenda-se medição de resistividade do solo e ajuste se necessário.

---

## 6. FONTES DE DADOS

### 6.1. Arquivos DWG Analisados

| Arquivo | Descrição | Observação |
|---------|-----------|------------|
| 348_02_SPDA_rev.00_EL_Rubens Alves - 01º PAVTO. TÉRREO.dwg | Térreo | 3.0 MB |
| 348_03_SPDA_rev.00_EL_Rubens Alves - 02º PAVTO. G1.dwg | Garagem 1 | 3.3 MB |
| 348_04_SPDA_rev.00_EL_Rubens Alves - 03º PAVTO. G2.dwg | Garagem 2 | 4.2 MB |
| 348_05_SPDA_rev.00_EL_Rubens Alves - 04º PAVTO. G3.dwg | Garagem 3 | 4.2 MB |
| 348_06_SPDA_rev.00_EL_Rubens Alves - 05º PAVTO. G4.dwg | Garagem 4 | 4.4 MB |
| 348_07_SPDA_rev.00_EL_Rubens Alves - 06º PAVTO. G5.dwg | Garagem 5 | 4.4 MB |
| 348_08_SPDA_rev.00_EL_Rubens Alves - 07º PAVTO. LAZER.dwg | Lazer | 2.2 MB |
| 348_09_SPDA_rev.00_EL_Rubens Alves - 08º PAVTO. TIPO.dwg | Tipo (1º) | 2.5 MB |
| 348_10_SPDA_rev.00_EL_Rubens Alves - 09º~31º PAVTO. TIPO (23x).dwg | Tipos (23×) | 1.9 MB |
| 348_11_SPDA_rev.00_EL_Rubens Alves - CASA DE MÁQUINAS.dwg | Casa Máquinas | 1.9 MB |

**Total de arquivos:** 10 DWGs  
**Responsável Técnico:** R. Rubens Alves  
**Revisão:** R00  

### 6.2. Documentação de Referência

- `PROJETO.md` — Informações gerais do empreendimento Thozen Electra
- NBR 5419:2015 — Proteção contra descargas atmosféricas (norma de referência)
- NBR 5410:2004 — Instalações elétricas de baixa tensão

---

## 7. OBSERVAÇÕES E DADOS FALTANTES

### 7.1. Limitações da Análise Atual

⚠️ **Os arquivos DWG não puderam ser processados automaticamente.** Os quantitativos apresentados são **ESTIMATIVAS** baseadas em:

1. **Premissas geométricas:**
   - Perímetro do edifício: estimado em 120m (típico para edifícios residenciais verticais)
   - Altura por pavimento: 2.5m (tipos), 2.7m (garagens), 3-4m (térreo e casa máquinas)
   - Área de cobertura: ~400m² (típico para edifícios de ~32 pavimentos)

2. **Premissas normativas:**
   - Nível de proteção: III ou IV (mais comum para edifícios residenciais)
   - Número de descidas: 4 (premissa conservadora)
   - Bitolas conforme NBR 5419 Tabela 6

3. **Premissas de projeto:**
   - Sistema misto de aterramento (hastes + malha)
   - Anéis equipotenciais a cada ~17m
   - Trajeto de descidas retilíneo (fator de correção 1.02)

### 7.2. Dados que Precisam ser Confirmados

Para orçamentação EXECUTIVA precisa, é necessário extrair dos DWGs:

#### 7.2.1. Geometria do Edifício
- [ ] Perímetro real de cada pavimento (principalmente cobertura)
- [ ] Distâncias entre descidas (conforme posicionamento no projeto)
- [ ] Alturas reais por pavimento (verificar cotas estruturais)
- [ ] Área da cobertura (Casa de Máquinas)

#### 7.2.2. Sistema de Captação
- [ ] Tipo de sistema: Franklin (hastes) ou Faraday (malha + hastes)
- [ ] Quantidade exata de captores
- [ ] Posicionamento dos captores (cotas XY)
- [ ] Altura dos captores (h = 0.3m, 0.6m, 1.0m?)

#### 7.2.3. Descidas
- [ ] Número real de descidas (4, 5, 6?)
- [ ] Trajeto exato de cada descida (prumadas, shafts, fachadas)
- [ ] Comprimento real por descida (considerar desvios)
- [ ] Pontos de fixação e passagem por lajes

#### 7.2.4. Anéis Equipotenciais
- [ ] Número de anéis (5 ou mais?)
- [ ] Localização exata (pavimentos)
- [ ] Perímetro real de cada anel
- [ ] Conexões com elementos estruturais

#### 7.2.5. Aterramento
- [ ] Configuração da malha (reticulado, radial, misto)
- [ ] Dimensões da malha (área, espaçamento entre condutores)
- [ ] Número de hastes por descida
- [ ] Profundidade de enterramento
- [ ] Integração com eletrodo de fundação (se existente)

#### 7.2.6. Equipotencialização
- [ ] Lista de elementos metálicos a equipotencializar
- [ ] Quadros elétricos (localização e quantidade)
- [ ] Prumadas metálicas (localização)
- [ ] Esquadrias metálicas (perímetro total)

#### 7.2.7. Especificações Técnicas
- [ ] Nível de proteção especificado (I, II, III ou IV)
- [ ] Especificações de materiais (fabricantes, modelos)
- [ ] Detalhes de conexões (soldadas, aparafusadas, soldas exotérmicas)
- [ ] Memorial descritivo do projetista

### 7.3. Ações Recomendadas

Para avançar com o orçamento executivo:

1. **Opção A — Processar DWGs no AutoCAD:**
   - Abrir cada arquivo DWG no AutoCAD ou software compatível
   - Exportar para PDF com cotas visíveis
   - Medir manualmente os elementos principais
   - Extrair legendas, notas e especificações técnicas

2. **Opção B — Converter para DXF:**
   - Solicitar arquivos em formato DXF (open format)
   - Processar via ezdxf (Python) para extração automatizada
   - Extrair: linhas, textos, blocos, comprimentos

3. **Opção C — Solicitar Planilha do Projetista:**
   - Verificar se R. Rubens Alves possui planilha de quantitativos
   - Solicitar memorial de cálculo do SPDA
   - Usar como referência para validação

4. **Opção D — Levantamento Manual:**
   - Imprimir DWGs em PDF (via AutoCAD)
   - Realizar levantamento manual com régua/escala
   - Conferir com projetista elétrico

### 7.4. Validações Pendentes

Após obter os dados reais dos DWGs:

- [ ] Verificar conformidade com NBR 5419 (nível de proteção, espaçamentos, bitolas)
- [ ] Conferir compatibilidade com projeto estrutural (pontos de fixação)
- [ ] Validar integração com projeto elétrico (equipotencialização de quadros)
- [ ] Verificar detalhes de aterramento (resistividade do solo, integração com fundações)
- [ ] Confirmar especificações de materiais e fornecedores disponíveis

---

## 8. PRÓXIMOS PASSOS

### 8.1. Imediatos (Orçamento Paramétrico)
Para orçamento preliminar/paramétrico, os quantitativos estimados **podem ser utilizados** com as seguintes ressalvas:

- ✅ Usar para estimativa de custo total do SPDA (ordem de grandeza)
- ✅ Comparar com benchmarks de projetos similares
- ⚠️ Aplicar margem de segurança de **±20-30%**
- ⚠️ Identificar no orçamento como "Quantitativos Estimados — Sujeito a Revisão"

### 8.2. Para Orçamento Executivo Definitivo
Antes de fechar o orçamento executivo final:

1. **Processar arquivos DWG** (via AutoCAD, DXF ou PDF)
2. **Extrair quantitativos reais** de cada elemento
3. **Validar com memorial descritivo** do projetista
4. **Ajustar quantidades** conforme levantamento real
5. **Gerar revisão R01** deste briefing com dados confirmados

### 8.3. Integração com Memorial Cartesiano
Este briefing alimentará a **Planilha de Apoio N1 07.02 SPDA** no Memorial Cartesiano:

- **Fonte de quantidade:** `Planilha` (este briefing)
- **Estrutura:** Decomposição por subsistemas (captação, descidas, anéis, aterramento)
- **Formato:** Excel com abas por subsistema
- **Compatibilização:** Integrar com N1 07.01 Instalações Elétricas (quadros, equipotencialização)

---

## 9. CONTATOS E RESPONSÁVEIS

- **Projetista SPDA:** R. Rubens Alves
- **Cliente:** Thozen
- **Empreendimento:** Electra
- **Análise técnica:** Cartesiano (Cartesian Engenharia)
- **Data:** 2026-03-20

---

## 10. ANEXOS

### 10.1. Checklist de Validação

Ao processar os DWGs, verificar:

- [ ] Plantas de todos os pavimentos (10 arquivos)
- [ ] Detalhes de conexões (cortes, isométricos)
- [ ] Especificações técnicas (legendas, notas)
- [ ] Memorial descritivo do projetista
- [ ] Detalhes de aterramento (planta de situação)
- [ ] Integração com outros projetos (estrutural, elétrico)
- [ ] Normas e níveis de proteção especificados
- [ ] ART/RRT do responsável técnico

### 10.2. Referências Normativas Complementares

- NBR 5419-1:2015 — Princípios gerais
- NBR 5419-2:2015 — Gerenciamento de risco
- NBR 5419-3:2015 — Danos físicos a estruturas e perigos à vida
- NBR 5419-4:2015 — Sistemas elétricos e eletrônicos internos na estrutura
- NBR 13571:1996 — Hastes de aterramento aço-cobreadas
- NBR 13248:2000 — Cabos de cobre nus para fins elétricos

---

**Fim do Briefing SPDA R00 — Thozen Electra**

---

*Este documento foi gerado a partir de análise automatizada da estrutura de arquivos do projeto. Para levantamento definitivo, é necessário processamento dos arquivos DWG originais.*
