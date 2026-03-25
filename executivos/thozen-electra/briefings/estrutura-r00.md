# Briefing de Estrutura - Thozen Electra (R00)

**Projeto:** Edifício Residencial Thozen Electra  
**Endereço:** Rua Rubens Alves  
**Data de Extração:** 20/03/2026  
**Revisão:** R00  
**Responsável:** Cartesiano (IA)

---

## 1. Resumo do Projeto

### 1.1 Caracterização Geral
- **Tipologia:** Edifício residencial vertical
- **Número de pavimentos:** 35 pavimentos totais
  - Fundação
  - Térreo (L1)
  - 5 pavimentos de garagem (L2 a L6: G1 a G5)
  - 1 pavimento de lazer (L7)
  - 24 pavimentos tipo (L8 a L31: Tipo 01 a Tipo 24)
  - Telhado (L32)
  - Casa de máquinas (L33)
  - Reservatório (L34)
  - Tampa (L35)

### 1.2 Elementos Estruturais Identificados
- **Infraestrutura:** 70 elementos (blocos + vigas baldrame)
- **Pilares:** 1.531 elementos
- **Vigas:** 3.531 elementos
- **Lajes:** 1.527 elementos

---

## 2. Premissas de Extração

### 2.1 Fonte de Dados
- **Arquivo IFC:** `1203 - THOZEN - RUBENS ALVES - BLOCOS+RAMPAS DE ACESSO - R26.ifc`
- **Localização:** `projetos/thozen-electra/projetos/01 ESTRUTURA/IFC/`
- **Tamanho:** 53 MB
- **Revisão do projeto:** R26

### 2.2 Metodologia
- Extração de quantitativos via análise de modelo IFC usando `ifcopenshell`
- Volumes estimados a partir de dimensões nominais extraídas dos nomes dos elementos
- **LIMITAÇÃO IMPORTANTE:** O IFC não contém quantidades (IfcElementQuantity) explícitas
- Volumes calculados com base em:
  - **Pilares:** seção nominal × altura estimada (2,8m por pavimento)
  - **Vigas:** seção nominal × comprimento estimado (5,0m médio)
  - **Lajes:** espessura nominal × área estimada (20 m² por pano)
  - **Baldrame:** seção nominal × comprimento estimado (3,0m médio)

### 2.3 Classes FCK Identificadas
⚠️ **PENDENTE:** O IFC não especifica classe de concreto (fck) nos elementos.  
**Ação necessária:** Consultar memorial descritivo ou prancha de especificações estruturais.

**Premissas adotadas (padrão de mercado):**
- Infraestrutura (blocos/baldrame): fck 25 MPa (C25)
- Pilares: fck 30-40 MPa (a definir por trecho)
- Vigas e lajes: fck 30 MPa (C30)

---

## 3. Quantitativos Extraídos

### 3.1 INFRAESTRUTURA

#### 3.1.1 Fundações - Blocos e Vigas Baldrame

**Resumo:**
- **Quantidade total:** 70 elementos
- **Volume estimado de concreto:** 54,58 m³

**Detalhamento por tipo:**

| Elemento | Seção (cm) | QTD | Volume Est. (m³) | Observação |
|----------|-----------|-----|------------------|------------|
| **Vigas Baldrame 20×250** | | | | |
| Viga 1 a 16 (20×250) | 20×250 | 16 | 24,00 | Vigas de perímetro |
| **Vigas Baldrame 14×184** | | | | |
| Viga 1 a 6 (14×184) | 14×184 | 6 | 4,62 | Vigas internas |
| **Vigas Baldrame 14×164** | | | | |
| Vigas diversas (14×164) | 14×164 | 23 | 15,87 | Vigas internas |
| **Vigas Baldrame 14×124** | | | | |
| Vigas diversas (14×124) | 14×124 | 21 | 10,92 | Vigas menores |
| **Blocos/Pranchas** | | | | |
| Pra4 (70×70×30) | 70×70×30 | 3 | - | Blocos de apoio |
| Pra2 (70×70×30) | 70×70×30 | 1 | - | Bloco de apoio |

⚠️ **DADOS FALTANTES:**
- Tipo e quantidade de estacas (não identificadas no IFC)
- Comprimento exato das vigas baldrame (estimado em 3m médio)
- Volumes reais dos blocos Pra2/Pra4 (geometria não processada)
- Taxa de aço por bitola

**Recomendação:** Solicitar prancha de locação de estacas e detalhamento de armação.

---

### 3.2 SUPRAESTRUTURA

#### 3.2.1 Pilares

**Resumo:**
- **Quantidade total:** 1.531 elementos
- **Volume estimado de concreto:** 2.964,25 m³

**Principais tipos (top 15):**

| Tipo | Seção (cm) | QTD | Volume Est. (m³) | % do Total |
|------|-----------|-----|------------------|------------|
| P30 | 420×40 | 32 | 150,53 | 5,1% |
| P21 | 236×40 | 34 | 89,87 | 3,0% |
| P18 | 45×218 | 32 | 87,90 | 3,0% |
| P57 | 275×35 | 32 | 86,24 | 2,9% |
| P52 | 275×35 | 32 | 86,24 | 2,9% |
| P53 | 275×35 | 32 | 86,24 | 2,9% |
| P58 | 275×35 | 32 | 86,24 | 2,9% |
| P49 | 230×40 | 32 | 82,43 | 2,8% |
| P38 | 230×40 | 32 | 82,43 | 2,8% |
| P19 | 250×35 | 32 | 78,40 | 2,6% |
| P20 | 250×35 | 32 | 78,40 | 2,6% |
| P28 | 250×35 | 32 | 78,40 | 2,6% |
| P29 | 250×35 | 32 | 78,40 | 2,6% |
| P66 | 35×250 | 32 | 78,40 | 2,6% |
| P17 | 40×218 | 32 | 78,13 | 2,6% |

**Distribuição por pavimento:**

| Pavimento | Pilares (un) | Observação |
|-----------|--------------|------------|
| Fundação | 69 | Base dos pilares |
| Térreo | 72 | Térreo + rampas |
| G1 a G5 | ~49-51/pav | Garagens (5 pavimentos) |
| Lazer | 46 | Pavimento lazer |
| Tipo 01-24 | ~39-42/pav | Pavimentos tipo (24 pavimentos) |
| Telhado | 25 | Cobertura |
| Casa Máq. | 5 | Barrilete |

⚠️ **DADOS FALTANTES:**
- Taxa de aço por bitola (kg/m³)
- Área de forma (m²)
- Transição de seções ao longo da altura

---

#### 3.2.2 Vigas

**Resumo:**
- **Quantidade total:** 3.531 elementos
- **Volume estimado de concreto:** 2.406,38 m³

**Principais tipos (top 15):**

| Tipo | Seção (cm) | QTD | Volume Est. (m³) | % do Total |
|------|-----------|-----|------------------|------------|
| Viga 14 | 30×55 | 49 | 40,43 | 1,7% |
| Viga 11 | 19×80 | 48 | 36,48 | 1,5% |
| Viga 47 | 14×110 | 45 | 34,65 | 1,4% |
| Viga 66 | 25×110 | 22 | 30,25 | 1,3% |
| Viga 6 | 30×80 | 24 | 28,80 | 1,2% |
| Viga 9 | 30×80 | 24 | 28,80 | 1,2% |
| Viga 60 | 19×55 | 47 | 24,56 | 1,0% |
| Viga 8 | 25×80 | 24 | 24,00 | 1,0% |
| Viga 37 | 22×80 | 24 | 21,12 | 0,9% |
| Viga 38 | 22×80 | 24 | 21,12 | 0,9% |
| Viga 18 | 25×70 | 24 | 21,00 | 0,9% |
| Viga 23 | 25×70 | 24 | 21,00 | 0,9% |
| Viga 31 | 25×70 | 24 | 21,00 | 0,9% |
| Viga 12 | 30×55 | 25 | 20,62 | 0,9% |
| Viga 13 | 30×55 | 25 | 20,62 | 0,9% |

**Distribuição por pavimento:**

| Pavimento | Vigas (un) | Observação |
|-----------|------------|------------|
| Térreo | ~170 | Térreo + rampas |
| G1-G5 | ~60-110/pav | Garagens |
| Lazer | ~190 | Pavimento lazer (estrutura complexa) |
| Tipo 01-24 | ~100-110/pav | Pavimentos tipo |
| Telhado | ~105 | Cobertura |
| Casa Máq. | ~13 | Barrilete |
| Reservatório | ~29 | Reservatórios |

⚠️ **DADOS FALTANTES:**
- Comprimento real de cada viga (estimado em 5m médio)
- Taxa de aço por bitola (kg/m³)
- Área de forma (m²)

---

#### 3.2.3 Lajes

**Resumo:**
- **Quantidade total:** 1.527 elementos (panos de laje)
- **Volume estimado de concreto:** 7.358,80 m³
- **Espessura predominante:** 28 cm

**Principais tipos (top 15):**

| Tipo | Espessura (cm) | QTD | Volume Est. (m³) | % do Total |
|------|---------------|-----|------------------|------------|
| Pano 28 | 28 | 55 | 308,00 | 4,2% |
| Pano 31 | 28 | 55 | 308,00 | 4,2% |
| Pano 35 | 28 | 50 | 280,00 | 3,8% |
| Pano 5 | 28 | 49 | 274,40 | 3,7% |
| Pano 34 | 28 | 48 | 268,80 | 3,7% |
| Pano 36 | 28 | 47 | 263,20 | 3,6% |
| Pano 29 | 28 | 44 | 246,40 | 3,3% |
| Pano 23 | 28 | 38 | 212,80 | 2,9% |
| Pano 17 | 28 | 34 | 190,40 | 2,6% |
| Pano 22 | 28 | 32 | 179,20 | 2,4% |
| Pano 24 | 28 | 32 | 179,20 | 2,4% |
| Pano 16 | 28 | 31 | 173,60 | 2,4% |
| Pano 18 | 28 | 31 | 173,60 | 2,4% |
| Pano 19 | 28 | 31 | 173,60 | 2,4% |
| Pano 25 | 28 | 30 | 168,00 | 2,3% |

**Espessuras identificadas:**
- **28 cm:** Espessura predominante (maioria dos panos)
- **15 cm:** Pano 1 (34 elementos) - provavelmente laje de cobertura ou áreas técnicas

**Distribuição por pavimento:**

| Pavimento | Lajes (panos) | Observação |
|-----------|--------------|------------|
| Fundação | ~67 | Lajes sobre terreno/baldrame |
| Térreo | ~65 | Térreo + rampas |
| G1-G5 | ~20-35/pav | Garagens |
| Lazer | ~90 | Pavimento lazer |
| Tipo 01-24 | ~43-48/pav | Pavimentos tipo |
| Telhado | ~46 | Cobertura |
| Casa Máq. | ~6 | Barrilete |
| Reservatório | ~10 | Reservatórios |
| Tampa | 4 | Fechamento superior |

⚠️ **DADOS FALTANTES:**
- Área real de cada pano de laje (estimado em 20 m² por pano)
- Taxa de aço por bitola (kg/m²)
- Área de forma (m² - considerando que lajes treliçadas podem não necessitar forma inferior)

---

## 4. Resumo Geral de Quantitativos

### 4.1 Volume Total de Concreto (Estimado)

| Disciplina | Item | Volume (m³) | % do Total |
|-----------|------|-------------|------------|
| **INFRAESTRUTURA** | Blocos/Baldrame | 54,58 | 0,4% |
| **SUPRAESTRUTURA** | Pilares | 2.964,25 | 23,2% |
| | Vigas | 2.406,38 | 18,8% |
| | Lajes | 7.358,80 | 57,6% |
| **TOTAL GERAL** | | **12.784,01** | **100%** |

### 4.2 Dados Complementares Necessários

#### Aço
⚠️ **NÃO IDENTIFICADO NO IFC**

Necessário para orçamento:
- [ ] Taxa de aço por elemento (kg/m³)
- [ ] Distribuição por bitola (CA-50, CA-60)
- [ ] Consumo total estimado (ton)

**Sugestão de premissa (benchmarks de mercado):**
- Infraestrutura: ~100 kg/m³
- Pilares: ~120-150 kg/m³
- Vigas: ~100-120 kg/m³
- Lajes: ~80-100 kg/m³

#### Formas
⚠️ **NÃO IDENTIFICADO NO IFC**

Necessário para orçamento:
- [ ] Área de forma de pilares (m²)
- [ ] Área de forma de vigas (m²)
- [ ] Área de forma de lajes (m² - se laje maciça ou mista)
- [ ] Sistema de forma (compensado, metálica, etc.)

#### Estacas
⚠️ **NÃO IDENTIFICADO NO IFC**

Necessário para orçamento:
- [ ] Tipo de fundação (estaca hélice, raiz, tubulão, sapata)
- [ ] Diâmetro das estacas
- [ ] Comprimento médio e total
- [ ] Quantidade
- [ ] fck do concreto de estaca

---

## 5. Fontes de Dados

### 5.1 Arquivos Processados
1. **IFC Principal:**  
   `projetos/thozen-electra/projetos/01 ESTRUTURA/IFC/1203 - THOZEN - RUBENS ALVES - BLOCOS+RAMPAS DE ACESSO - R26.ifc`  
   - Revisão: R26
   - Data de modificação: 07/10 (ano a confirmar)
   - Tamanho: 53 MB

2. **DWG Disponível (não processado):**  
   `projetos/thozen-electra/projetos/01 ESTRUTURA/DWG/1203 - PREFORMAS - R20.DWG`  
   - Revisão: R20 (anterior ao IFC R26)
   - Contém pranchas de preforma (pode ter detalhamento de armação)

### 5.2 Arquivos Complementares Necessários
- [ ] Memorial descritivo estrutural
- [ ] Prancha de locação de estacas
- [ ] Pranchas de detalhamento de armação
- [ ] Planilha de quantitativos do projetista estrutural (se disponível)

---

## 6. Observações e Validações Necessárias

### 6.1 Limitações da Extração
1. **Volumes estimados:** Baseados em dimensões nominais e comprimentos médios, não em geometria real 3D.
2. **Sem quantidades IFC:** O arquivo não contém IfcElementQuantity, impedindo extração precisa de volumes.
3. **Estacas ausentes:** Sistema de fundação profunda não está modelado no IFC.
4. **Armação não modelada:** Aço não está representado no modelo.

### 6.2 Próximos Passos Recomendados
1. **Validação de volumes:**  
   - Solicitar planilha de quantitativos do projetista estrutural  
   - Comparar com volumes extraídos do IFC  
   - Ajustar estimativas conforme necessário

2. **Complementação de dados:**  
   - Obter memorial descritivo para especificações de materiais (fck, aço)  
   - Solicitar prancha de fundações (estacas)  
   - Consultar detalhamento de armação (taxa de aço)

3. **Refinamento de quantitativos:**  
   - Processar geometria 3D real (se possível via ifcopenshell.geom)  
   - Extrair áreas de forma por contato entre elementos  
   - Calcular comprimentos reais de vigas via modelo

4. **Geração de planilha executiva:**  
   - Aguardar validação de dados faltantes  
   - Mapear itens para Memorial Cartesiano (N1 03 Infraestrutura, N1 04 Supraestrutura)  
   - Gerar planilha Excel com composições

### 6.3 Dados que Precisam Validação Urgente
- [ ] **Volume de concreto:** Confirmar se ~12.784 m³ está na ordem de grandeza esperada para o projeto
- [ ] **Espessura de lajes:** Confirmar se 28cm é espessura maciça ou altura total (laje + enchimento)
- [ ] **Sistema estrutural:** Confirmar se é concreto armado convencional ou misto (protendido, pré-moldado)
- [ ] **Classe de concreto:** Definir fck por trecho de estrutura

---

## 7. Metadados do Briefing

- **Versão:** R00 (primeira extração)
- **Data:** 20/03/2026
- **Responsável:** Cartesiano (Assistente IA - Cartesian Engenharia)
- **Fonte:** Modelo IFC R26
- **Status:** ⚠️ DADOS INCOMPLETOS - Aguardando complementação
- **Próxima revisão:** R01 (após recebimento de memorial descritivo + prancha de fundações)

---

**Arquivo gerado automaticamente via análise de modelo IFC.**  
**Para dúvidas ou ajustes, contatar o time de orçamentos da Cartesian Engenharia.**
