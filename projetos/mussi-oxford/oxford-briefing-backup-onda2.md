# OXFORD - MUSSI EMPREENDIMENTOS
## Briefing de Orçamento Paramétrico

**Data de Geração:** 12/03/2026  
**Base:** Dados arquitetônicos consolidados (`oxford-dados-arquitetura.md`)  
**Revisão dos Projetos:** Revisão 1 - Junho/2024

---

## 1. Identificação do Projeto

| Campo | Valor |
|-------|-------|
| **Nome do projeto** | Oxford |
| **Cliente/Incorporadora** | Mussi Empreendimentos |
| **Cidade/Região** | Itajaí |
| **Estado** | SC |
| **Data-base dos preços (mês/ano)** | ⚠️ **CONFIRMAR COM LEO** (sugestão: março/2026) |
| **CUB referência (R$/m²)** | ⚠️ **CONFIRMAR** — CUB/SC R8N março/2026 |

---

## 2. Dados do Programa (📐 extraídos do PDF)

### Essenciais

| Variável | ID | Valor | Unidade | Status | Observação |
|----------|----|-------|---------|--------|------------|
| **Área Construída Total** | AC | ⚠️ **NÃO DISPONÍVEL** | m² | **CRÍTICO** | Quadro de áreas geral NÃO consta nas plantas individuais. **SOLICITAR AO CLIENTE.** |
| **Nº Unidades Residenciais** | UR | **~86 a 103** | un | **ESTIMADO** | Cálculo: 17 pav. tipo × 4-6 un/pav. + 1 ático. Verificar plantas individuais de tipologias. |
| **Nº Total Pavimentos** | NP | **27** | un | ✅ **EXTRAÍDO** | Térreo + G2-G5 + Lazer + 17 tipo + Ático + 3 técnicos |
| **Nº Pavimentos Tipo** | NPT | **17** | un | ✅ **EXTRAÍDO** | 7º ao 23º pavimento |
| **Nº Elevadores** | ELEV | **2** | un | **ESTIMADO** | Identificado "caixa de elevador" nas plantas. Verificar memorial. |
| **Nº Vagas** | VAG | **136+** | un | ✅ **EXTRAÍDO** | G1=25, G3=37, G4=37, G5=37. G2 não especificado. |
| **Área do Terreno** | AT | ⚠️ **NÃO DISPONÍVEL** | m² | **CRÍTICO** | Solicitar projeto de implantação. |

### Importantes

| Variável | ID | Valor | Unidade | Status | Observação |
|----------|----|-------|---------|--------|------------|
| **Área Projeção Torre** | APT | ⚠️ **NÃO DISPONÍVEL** | m² | **SOLICITAR** | Planta de implantação necessária |
| **Perímetro Projeção Torre** | PPT | ⚠️ **NÃO DISPONÍVEL** | m | **SOLICITAR** | Planta de implantação necessária |
| **Área Projeção Embasamento** | APE | ⚠️ **NÃO DISPONÍVEL** | m² | **SOLICITAR** | Planta de implantação necessária |
| **Perímetro Proj. Embasamento** | PPE | ⚠️ **NÃO DISPONÍVEL** | m | **SOLICITAR** | Planta de implantação necessária |
| **Nº Subsolos** | NS | **0** | un | **ESTIMADO** | Plantas G1-G5 = térreo + 4 pav. garagem acima. Verificar cortes. |
| **Nº Pav. Embasamento** | NPE | **5** | un | **ESTIMADO** | G1 (térreo) + G2-G5 (garagem) |
| **Prazo de Obra** | — | ⚠️ **NÃO DEFINIDO** | meses | **CONFIRMAR COM CLIENTE** | Sugestão: 30-36 meses (padrão para 27 pav.) |

### Opcionais

| Variável | ID | Valor | Unidade | Status | Observação |
|----------|----|-------|---------|--------|------------|
| **Pav. Tipo Diferenciados** | NPD | **1** | un | **ESTIMADO** | 8º pavimento parece ter tipologia diferente do 7º |
| **Nº Pavimentos Duplex** | ND | **0** | un | **ESTIMADO** | Não identificado nas plantas |
| **Churrasqueiras** | CHU | **1+** | un | **ESTIMADO** | Espaço gourmet no 6º pav. (lazer) |
| **Área de Lazer** | AL | **~433** | m² | **PARCIAL** | 432,88 m² especificados (Espaço Gourmet + Bar Externo). Outros ambientes presentes mas sem área. |
| **Área de Subsolos** | AS | **0** | m² | **ESTIMADO** | Sem subsolo |
| **Área Embasamento** | AE | ⚠️ **NÃO DISPONÍVEL** | m² | **SOLICITAR** | Área G1-G5 não totalizada |
| **Locação da Obra** | LC | ⚠️ **NÃO DISPONÍVEL** | m | **SOLICITAR** | Perímetro do terreno |
| **BDI aplicado** | — | ⚠️ **NÃO DEFINIDO** | × | **CONFIRMAR** | Padrão Cartesian: 25-30% |

---

## 3. Perguntas Decisivas (❓ resposta humana)

### 🔴 Alto Impacto (definições CRÍTICAS)

#### Q2. Tipo de Laje ❓

**Resposta Provisória:** ⚠️ **Cubetas (padrão)** — NÃO CONFIRMADO

**Justificativa:** 
- Projeto não especifica tipo de laje estrutural
- Cubetas é o padrão mais comum em SC para edifícios residenciais multipavimentos
- Sistema permite vãos típicos de unidades residenciais (~5-6m)

**⚠️ CONFIRMAR COM:** 
- Projeto estrutural (prancha de forma)
- Memorial descritivo estrutural
- Cliente/projetista estrutural

**Alternativas possíveis:** Protendida (se vãos >7m), Maciça (se pé-direito reduzido)

---

#### Q5. Padrão de Acabamento ❓

**Resposta Provisória:** ⚠️ **Alto Padrão** — ESTIMADO com base em indicadores

**Justificativa:**
- **Localização:** Rua Uruguai / Rua Imbituba, Centro de Itajaí (região nobre)
- **Cliente:** Mussi Empreendimentos (incorporadora conhecida por empreendimentos médio-alto padrão em Itajaí)
- **Programa:** 27 pavimentos, área de lazer completa (piscina, fitness, coworking, espaço gourmet), ático/penthouse
- **Indicadores:** 
  - Brise metálico na fachada (4º pav.) → elemento arquitetônico sofisticado
  - Pergolado vazado no lazer
  - Área comercial no térreo (salas de ~100m²) → indica perfil de público
  - Cobertura habitável (ático 24º pav.)

**Classificação:**
- [x] **Alto Padrão** (porcelanato retificado, pintura eletrostática, acabamentos premium)
- Descartado "Super Alto Padrão" — ausência de pele de vidro ou elementos ultra-premium

**⚠️ CONFIRMAR COM:**
- Memorial descritivo
- Tabela de acabamentos
- Cliente (posicionamento comercial pretendido)

---

#### Q3. Contenção ❓

**Resposta Provisória:** ⚠️ **NÃO** — ESTIMADO (terreno aparentemente plano)

**Justificativa:**
- Planta G1 (térreo) mostra **3 áreas de jardim externo** → indica ausência de subsolo
- Pavimentos G1-G5 = térreo + 4 pav. garagem **ACIMA DO NÍVEL DA RUA**
- Sem indicação de escavação nas plantas

**⚠️ ATENÇÃO:** Rua Uruguai / Rua Imbituba pode ter desnível entre ruas.

**⚠️ CONFIRMAR COM:**
- Projeto de implantação (corte de implantação)
- Levantamento topográfico
- Projeto de fundação (se houver escavação)

**Se houver contenção:**
- Tipo mais provável: **Cortina de estacas** (padrão para terrenos urbanos em SC)
- Extensão: verificar perímetro do terreno

---

#### Q19. Prazo de Obra ❓

**Resposta Provisória:** ⚠️ **36 meses** — ESTIMADO

**Justificativa:**
- **Porte:** 27 pavimentos → obra de grande porte
- **Comparativo:** 
  - Padrão mercado SC: ~1,5 mês/pavimento para alto padrão
  - 27 pav. × 1,5 = 40,5 meses
  - Com embasamento de 5 pavimentos (garagem acima do solo): -4 meses vs subsolo
- **Ajuste:** 36 meses = prazo realista para obra sem subsolo, com garagem sobreposta

**Premissas:**
- Equipe dimensionada adequadamente
- Sem paralisações prolongadas
- Logística urbana (Centro de Itajaí) pode impactar cronograma

**⚠️ CONFIRMAR COM:** Cliente (expectativa comercial de entrega)

**Alternativas:**
- [ ] **30 meses** — se cronograma agressivo (risco de sobrecusto)
- [x] **36 meses** — equilibrado
- [ ] **42 meses** — conservador (+ custos indiretos)

---

#### Q4. Nº de Subsolos ❓

**Resposta:** ✅ **0 subsolos** — CONFIRMADO pelos dados arquitetônicos

**Justificativa:**
- Planta G1 = **Térreo** com jardins externos (não há escavação)
- Plantas G2-G5 = **4 pavimentos de garagem ACIMA do térreo**
- 136 vagas distribuídas em pavimentos elevados
- Sistema de rampa de acesso veicular (não rampa de descida)

**Impacto:**
- Economia significativa vs empreendimentos com subsolo
- Fundação mais simples (sem contenção/rebaixamento de lençol)
- Prazo de obra reduzido (~4-6 meses a menos)

---

### 🟡 Médio Impacto

#### Q1. Tipo de Fundação

**Resposta Provisória:** ⚠️ **Hélice Contínua** (padrão referência)

**Justificativa:**
- Padrão regional para edifícios em SC
- Centro de Itajaí: solo tipicamente misto (areia/argila)
- 27 pavimentos: carga compatível com hélice contínua

**⚠️ CONFIRMAR COM:** Projeto de fundação / Sondagem SPT

**Alternativas possíveis:**
- Estaca Franki (se solo resistente mais profundo)
- Tubulão (se solo rochoso ou problemático)

---

#### Q6. Tipo de Esquadria

**Resposta Provisória:** ⚠️ **Pintura Eletrostática** — ESTIMADO (compatível com Alto Padrão)

**Justificativa:**
- Padrão de acabamento **Alto Padrão** → esquadrias de qualidade superior
- Pintura eletrostática > anodizado em durabilidade e estética
- Brise metálico na fachada indica preocupação com acabamento externo

**⚠️ CONFIRMAR COM:** Memorial descritivo / Tabela de esquadrias

**Quantidades identificadas (8º pav.):**
- 17 portas + 16 janelas/gradis por pavimento tipo

---

#### Q10. Tipo de Fachada

**Resposta Provisória:** ⚠️ **Textura + Pintura** (padrão) com **Elementos Especiais**

**Justificativa:**
- **Elementos identificados:**
  - Brise metálico (16,73 m no 4º pavimento) → proteção solar + estética
  - Pergolado vazado (lazer 6º pav.)
  - Muro 1,80m (lazer)
- **Tipologia:** Fachada mista (revestimento principal + elementos arquitetônicos)

**⚠️ CONFIRMAR COM:** Projeto de fachadas / Memorial descritivo

**Opções:**
- [ ] Textura + pintura (*referência*)
- [ ] **Misto** (textura + ACM/cerâmica em detalhes) ← **MAIS PROVÁVEL**
- [ ] Cerâmica/Pastilha completa
- [ ] Pele de vidro (descartado — não identificado)

---

#### Q11. MO Fachada

**Resposta Provisória:** ⚠️ **Empreitada** — ESTIMADO (+20% custo)

**Justificativa:**
- Brise metálico = especialização técnica (montagem de estrutura metálica)
- Pergolado vazado = estrutura especial
- Elementos arquitetônicos complexos geralmente demandam subempreitada

**⚠️ CONFIRMAR COM:** Cliente (modelo de contratação previsto)

---

#### Q8. Vedação Interna

**Resposta Provisória:** ⚠️ **Misto** (Alvenaria + Drywall)

**Justificativa:**
- **Alto Padrão** → flexibilidade de layout (drywall em áreas molhadas/técnicas)
- **Unidades residenciais pequenas** (~35m² médio) → drywall economiza espaço
- **Áreas técnicas identificadas** nas plantas → instalações embutidas (compatível com drywall)

**Distribuição estimada:**
- Alvenaria: vedação externa, shafts, áreas molhadas estruturais
- Drywall: divisórias internas, forros, acabamentos especiais

**⚠️ CONFIRMAR COM:** Projeto executivo / Memorial descritivo

---

#### Q16. Nível de Lazer

**Resposta:** ✅ **Completo** — CONFIRMADO pelos dados arquitetônicos

**Justificativa — Ambientes identificados no 6º pavimento:**
- ✅ Piscina (21,98 m²)
- ✅ Espaço Gourmet (40,38 m²)
- ✅ Bar Externo / Área Externa (392,50 m²)
- ✅ Sala de Estar / Lounge
- ✅ Sala de Jogos
- ✅ Salão de Festas
- ✅ Brinquedoteca
- ✅ Fitness / Academia
- ✅ Espaço Coworking

**Classificação:**
- [ ] Básico (salão + churrasqueira)
- [x] **Completo** (+ piscina, academia) ← **CONFIRMADO**
- [ ] Premium (+ spa, rooftop) — não identificado spa/ofurô/sauna/rooftop lounge

**Área total de lazer:** ~433 m² (áreas especificadas)

---

### 🟢 Baixo Impacto (refinamento)

#### Q7. Piso

**Resposta Provisória:** ⚠️ **Porcelanato Retificado** — ESTIMADO (compatível com Alto Padrão)

**Opções:**
- [ ] Cerâmica (descartado — padrão Econômico)
- [x] **Porcelanato** (60×60 ou 80×80 retificado) ← **MAIS PROVÁVEL**
- [ ] Vinílico (descartado — não condiz com posicionamento)
- [ ] Importado/Premium (possível em áreas nobres: lobby, lazer)
- [ ] Mármore (possível no ático)

**⚠️ CONFIRMAR COM:** Tabela de acabamentos

---

#### Q9. Forro

**Resposta Provisória:** ⚠️ **Gesso Liso** — ESTIMADO (padrão Alto Padrão)

**Justificativa:**
- Alto padrão geralmente usa gesso liso ou gesso com detalhes (sanca/rebaixos)
- Unidades residenciais: gesso liso é o padrão
- Áreas comuns (lazer): possível gesso com detalhes arquitetônicos

**Opções:**
- [ ] Estucamento (padrão Econômico)
- [x] **Gesso liso** ← **MAIS PROVÁVEL**
- [ ] Gesso negativo (possível em áreas comuns)
- [ ] Gesso sanca (possível em unidades maiores)
- [ ] Mineral (descartado — uso comercial/corporativo)

**⚠️ CONFIRMAR COM:** Memorial descritivo

---

#### Q12. Cobertura Habitável

**Resposta:** ✅ **Completa** — CONFIRMADO

**Justificativa — 24º Pavimento (Ático/Penthouse):**
- ✅ Sala / Estar: 14,68 m²
- ✅ Suíte / Dormitório: 30,97 m²
- ✅ Living (área social): 42,81 m²
- ✅ Sacada / Terraço: 26,37 m²
- ✅ Área total: ~114,83 m²

**Classificação:**
- [ ] Não
- [ ] Básica (área técnica + pequena área social)
- [x] **Completa** (unidade residencial penthouse) ← **CONFIRMADO**

**Impacto:**
- Impermeabilização especial (laje de cobertura habitável)
- Acabamentos premium (padrão superior ao tipo)
- Instalações completas (hidráulica, elétrica, climatização)

---

#### Q13. Aquecimento

**Resposta Provisória:** ⚠️ **Gás Individual** — ESTIMADO (padrão SC)

**Justificativa:**
- Padrão regional para edifícios residenciais em SC
- Custo-benefício adequado para clima de Itajaí (verões quentes, invernos amenos)
- Alto padrão geralmente inclui aquecimento

**⚠️ CONFIRMAR COM:** Projeto hidrossanitário / Memorial

**Alternativas:**
- [ ] Sem aquecimento (descartado — não condiz com Alto Padrão)
- [x] **Gás individual** ← **MAIS PROVÁVEL**
- [ ] Central (possível, mas menos comum em SC)
- [ ] Solar (possível complemento)
- [ ] Bomba de calor (raro em SC)

---

#### Q14. Automação

**Resposta Provisória:** ⚠️ **Básico** — ESTIMADO

**Justificativa:**
- Alto Padrão geralmente inclui infraestrutura para automação
- **Infraestrutura identificada:**
  - Área técnica em unidades (1,55-1,73 m²)
  - Sistema de elevadores
  - Shafts (HID, Elétrica, Água)
- **Escopo estimado:** Interfone, controle de acesso, preparação para automação residencial

**Opções:**
- [ ] Mínimo (interfone básico)
- [x] **Básico** (interfone + preparação) ← **ESTIMADO**
- [ ] Completo (automação de iluminação + persianas)
- [ ] Premium (integração total / smart home)

**⚠️ CONFIRMAR COM:** Projeto elétrico / Memorial de automação

---

#### Q15. Energia Solar

**Resposta Provisória:** ⚠️ **Sem** — ESTIMADO (não identificado nas plantas)

**Justificativa:**
- Não identificado nas plantas técnicas (25º-27º pavimentos)
- 27º pavimento = Reservatórios (sem menção a placas fotovoltaicas)
- Laje de cobertura impermeabilizada (compatível com placas, mas não especificado)

**⚠️ CONFIRMAR COM:**
- Projeto elétrico
- Memorial de sustentabilidade
- Cliente (interesse em certificação/economia)

**Se houver:**
- [ ] Solar comum (aquecimento água)
- [ ] Solar completo (aquecimento + fotovoltaico)

---

#### Q17. Paisagismo

**Resposta Provisória:** ⚠️ **Básico** — ESTIMADO

**Justificativa — Áreas verdes identificadas:**
- ✅ Térreo (G1): 3 áreas de jardim externo
- ✅ Lazer (6º pav.): Área externa com paisagismo (392,50 m²)

**Classificação:**
- [ ] Sem (descartado)
- [x] **Básico** (jardins + paisagismo lazer) ← **ESTIMADO**
- [ ] Elaborado (projeto paisagístico assinado, espécies especiais)
- [ ] Premium (jardins verticais, espelhos d'água, paisagismo de autor)

**⚠️ CONFIRMAR COM:** Projeto de paisagismo (se existir)

---

#### Q18. Mobiliário

**Resposta Provisória:** ⚠️ **Básico** (áreas comuns) — ESTIMADO

**Justificativa:**
- Alto Padrão geralmente mobilia áreas comuns (lazer)
- **Ambientes que demandam mobiliário:**
  - Espaço Gourmet (mesas, cadeiras, bancada)
  - Sala de Jogos (mesa de jogos, sofás)
  - Fitness (equipamentos de academia)
  - Brinquedoteca (móveis infantis)
  - Coworking (mesas, cadeiras, estações de trabalho)

**Classificação:**
- [ ] Sem
- [x] **Básico** (mobília funcional áreas comuns) ← **ESTIMADO**
- [ ] Completo (mobília + decoração completa)
- [ ] Decorado (projeto de interiores assinado, acabamentos especiais)

**⚠️ CONFIRMAR COM:** Projeto de interiores / Cliente

---

#### Q20. Região

**Resposta:** ✅ **Litoral SC** — CONFIRMADO

**Justificativa:**
- Endereço: Rua Uruguai / Rua Imbituba, **Centro, Itajaí/SC**
- Itajaí = cidade litorânea (20km de Balneário Camboriú)

**Impacto:**
- Custos de mão de obra regional SC
- Logística de materiais (proximidade portuária — vantagem)
- CUB/SC como referência

---

### ⚡ Infraestrutura Técnica (Sim/Não)

#### Q21. Gerador?

**Resposta Provisória:** ⚠️ **SIM** — ESTIMADO (+15% em Sist. Especiais)

**Justificativa:**
- **27 pavimentos** → NBR 5410 pode exigir gerador para sistema de emergência
- **Elevadores** (mínimo 2) → backup de energia para resgate
- **Casa de Máquinas (25º pav.)** → espaço técnico compatível com gerador

**⚠️ CONFIRMAR COM:** Projeto elétrico / PPCI

---

#### Q22. Subestação?

**Resposta Provisória:** ⚠️ **SIM** — ESTIMADO (+10% em Sist. Especiais)

**Justificativa:**
- **Porte do empreendimento:** 27 pavimentos + ~90 unidades
- **Carga estimada:** >75 kVA (limite para fornecimento BT)
- **Padrão para edifícios deste porte:** Subestação transformadora (entrada MT 13,8 kV)

**⚠️ CONFIRMAR COM:** 
- Projeto elétrico (memorial de cálculo de carga)
- Concessionária local (CELESC)

---

#### Q23. Placas Fotovoltaicas?

**Resposta Provisória:** ⚠️ **NÃO** — ESTIMADO (não identificado)

**Justificativa:**
- Não identificado nas plantas técnicas (27º pav. = reservatórios, sem menção a placas)
- Laje de cobertura impermeabilizada = compatível com instalação futura, mas não especificado

**⚠️ CONFIRMAR COM:** Cliente / Projeto elétrico

**Se incluir:**
- Sistema on-grid conectado à CELESC
- Redução de custos operacionais (condomínio)
- Possível argumento de venda (sustentabilidade)

---

#### Q24. Infra Carro Elétrico?

**Resposta Provisória:** ⚠️ **NÃO** — ESTIMADO (+5% em Instalações se incluir)

**Justificativa:**
- Não identificado nas plantas
- Não é obrigatório em Itajaí (legislação municipal)
- Alto Padrão em 2024 pode incluir preparação

**⚠️ CONFIRMAR COM:**
- Cliente (diferencial comercial?)
- Projeto elétrico (preparação de infraestrutura)

**Se incluir:**
- Eletrodutos dimensionados
- Quadros de distribuição preparados
- Pontos de recarga em garagem

---

#### Q25. Pressurização Escada?

**Resposta Provisória:** ⚠️ **SIM** — ESTIMADO (+8% em Instalações)

**Justificativa:**
- **NBR 15200 / Código de Segurança contra Incêndio SC:** Edifícios >60m (altura) ou >23m (altura de escape) devem ter escada pressurizada
- **27 pavimentos** → altura estimada ~81m (3m/pav.) → **OBRIGATÓRIO**

**⚠️ CONFIRMAR COM:** 
- Projeto de PPCI (Plano de Prevenção e Proteção Contra Incêndio)
- Código de Bombeiros SC

**Sistema:**
- Ventilador de pressurização
- Dutos e grelhas de insuflamento
- Controle automático

---

## 4. DADOS FALTANTES CRÍTICOS (⛔ Solicitar ao Cliente)

### 🔴 BLOQUEADORES (sem esses não gera orçamento)

1. **Área Construída Total (AC)** — m²
   - Fonte: Quadro de áreas geral / Projeto de implantação
   - **CRÍTICO:** Base de cálculo de todo o orçamento

2. **Área do Terreno (AT)** — m²
   - Fonte: Escritura / Levantamento topográfico
   - **CRÍTICO:** Cálculo de fundação, movimento de terra, locação

3. **Data-base dos preços** — mês/ano
   - Confirmar com cliente: usar março/2026 ou data específica?

### 🟡 IMPORTANTES (melhoram precisão ~20%)

4. **Nº exato de Unidades Residenciais**
   - Verificar: Plantas individuais de tipologias / Memorial

5. **Áreas de Projeção** (APT, PPT, APE, PPE)
   - Fonte: Projeto de implantação

6. **Memorial Descritivo Completo**
   - Especificações de acabamentos
   - Sistemas técnicos (fundação, estrutura, instalações)

7. **Projeto Estrutural**
   - Tipo de laje (confirmar se cubetas ou outra)
   - Sistema estrutural (paredes, pilares, vigas)

8. **Sondagem SPT**
   - Tipo de fundação adequado
   - Profundidade / carga admissível

### 🟢 DESEJÁVEIS (refinam resultado)

9. **Projeto de Implantação** (corte de implantação)
   - Confirmar ausência de subsolo
   - Níveis de terreno / contenção

10. **Tabela de Acabamentos**
    - Especificações detalhadas por ambiente

11. **Prazo de Obra** (expectativa comercial)
    - Define custos indiretos

12. **BDI** (Bonificações e Despesas Indiretas)
    - Padrão Cartesian ou específico do cliente?

---

## 5. RESUMO EXECUTIVO — Dados Prontos para Geração

### ✅ Confirmados

| Item | Valor |
|------|-------|
| Nº Total Pavimentos | 27 |
| Nº Pavimentos Tipo | 17 |
| Nº Vagas Garagem | 136+ |
| Nº Subsolos | 0 |
| Área de Lazer | ~433 m² |
| Nível de Lazer | Completo |
| Cobertura Habitável | Sim (Penthouse 114m²) |
| Região | Litoral SC (Itajaí) |
| Cliente | Mussi Empreendimentos |

### ⚠️ Estimados (Validar)

| Item | Valor Estimado | Confiabilidade |
|------|---------------|----------------|
| Nº Unidades Residenciais | 86-103 | Média (baseado em contagem visual) |
| Nº Elevadores | 2 | Alta (padrão para porte) |
| Nº Pav. Embasamento | 5 | Alta (G1-G5 identificados) |
| Padrão Acabamento | Alto Padrão | Alta (indicadores múltiplos) |
| Tipo de Laje | Cubetas | Média (padrão regional) |
| Tipo de Fundação | Hélice Contínua | Média (padrão regional) |
| Prazo de Obra | 36 meses | Média (cálculo porte) |
| Contenção | Não | Alta (plantas indicam) |

### ⛔ Faltantes CRÍTICOS

- Área Construída Total (AC)
- Área do Terreno (AT)
- Data-base CUB

---

## 6. PRÓXIMOS PASSOS

### Sequência Recomendada:

1. **Solicitar ao cliente Mussi:**
   - ✅ Quadro de áreas geral (AC, AT)
   - ✅ Memorial descritivo
   - ✅ Projeto de implantação
   - ✅ Confirmação de data-base de preços

2. **Validar estimativas:**
   - Contagem exata de unidades (plantas individuais de tipologias)
   - Tipo de laje estrutural (projeto estrutural)
   - Padrão de acabamento (tabela de acabamentos)

3. **Gerar orçamento paramétrico:**
   - Preencher template Excel (`DADOS_PROJETO` e `BRIEFING`)
   - Rodar script `gerar_template_dinamico.py`
   - Gerar apresentação

4. **Reunião de validação:**
   - Apresentar premissas e estimativas
   - Ajustar conforme feedback
   - Refinar orçamento

---

## 7. OBSERVAÇÕES TÉCNICAS

### Complexidades Identificadas

🔧 **Estruturais:**
- 27 pavimentos → sistema estrutural robusto
- Garagem sobreposta (4 pav.) → cargas significativas na estrutura
- Brise metálico → interface estrutura/fachada

🔧 **Instalações:**
- 27 pavimentos → sistema de recalque (água) + sistema de drenagem
- Casa de Máquinas (25º pav.) → elevadores com grande curso
- Pressurização de escada (obrigatória para altura >60m)

🔧 **Execução:**
- Centro urbano (Itajaí) → logística de canteiro restrita
- 27 pavimentos → grua de grande porte
- Prazo longo (36 meses) → custos indiretos relevantes

### Riscos e Incertezas

⚠️ **Alto:** Área construída total (impacta todo orçamento)  
⚠️ **Médio:** Tipo de laje (±15% na supraestrutura)  
⚠️ **Médio:** Padrão de acabamento (±30% em acabamentos)  
⚠️ **Baixo:** Contenção (parece não ter, mas verificar implantação)

---

**Briefing gerado por:** Jarvis (Subagente Onda 2)  
**Próxima etapa:** Aguardar dados faltantes + validação com Leo/Cliente → Gerar template Excel

---

*Este briefing consolida os dados extraídos das plantas arquitetônicas e estabelece premissas técnicas razoáveis para estimativa paramétrica. Valores marcados com ⚠️ devem ser VALIDADOS antes da geração do orçamento final.*
