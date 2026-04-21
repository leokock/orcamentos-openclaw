# Observações Técnicas - Extração Estrutura Thozen Electra

**Data:** 20/03/2026  
**Revisão:** R00  
**Responsável:** Cartesiano (IA)

---

## 🔍 Metodologia de Extração

### Processamento do IFC

**Arquivo processado:**  
`1203 - THOZEN - RUBENS ALVES - BLOCOS+RAMPAS DE ACESSO - R26.ifc` (53 MB)

**Biblioteca utilizada:**  
`ifcopenshell` (Python) - parser IFC open-source

**Elementos extraídos:**
- `IfcFooting`: 70 elementos (blocos/baldrame)
- `IfcColumn`: 1.531 elementos (pilares)
- `IfcBeam`: 3.531 elementos (vigas)
- `IfcSlab`: 1.527 elementos (lajes)
- `IfcBuildingStorey`: 80 pavimentos (com duplicações aparentes - 2 torres?)

**Total de produtos IFC:** 6.811 elementos

---

## ⚠️ Limitações Identificadas

### 1. Ausência de QuantitySets
O IFC **NÃO contém** `IfcElementQuantity` explícitos.

**Consequência:**  
Não foi possível extrair volumes reais de concreto diretamente do modelo.

**Solução adotada:**  
Estimativas baseadas em dimensões nominais extraídas dos nomes dos elementos:
- Pilares: seção × altura estimada (2,8m por pavimento)
- Vigas: seção × comprimento estimado (5,0m médio)
- Lajes: espessura × área estimada (20 m² por pano)

**Precisão estimada:** ±30-40%

**Recomendação:**  
Validar volumes com planilha de quantitativos do projetista estrutural.

---

### 2. Estacas Não Modeladas

Não foram identificados elementos do tipo `IfcPile` no IFC.

**Possíveis causas:**
- Fundação não foi modelada (somente blocos/baldrame)
- Estacas estão em arquivo separado
- Fundação é por sapatas (não profunda)

**Recomendação:**  
Solicitar prancha de locação de fundações + memorial descritivo.

---

### 3. Armação Não Representada

Não foram identificados elementos `IfcReinforcingBar` ou `IfcReinforcingMesh`.

**Consequência:**  
Taxa de aço (kg/m³) não pode ser extraída do modelo.

**Recomendação:**  
- Consultar pranchas de detalhamento de armação
- Usar benchmarks de mercado como premissa inicial:
  - Infraestrutura: 100 kg/m³
  - Pilares: 120-150 kg/m³
  - Vigas: 100-120 kg/m³
  - Lajes: 80-100 kg/m³

---

### 4. Classes de Concreto (fck) Não Especificadas

O IFC não contém PropertySets com especificação de resistência característica (fck).

**Premissas adotadas (padrão de mercado):**
- Infraestrutura: fck 25 MPa (C25)
- Pilares: fck 30-40 MPa (variável por trecho)
- Vigas/Lajes: fck 30 MPa (C30)

**Recomendação:**  
Confirmar com memorial descritivo estrutural.

---

### 5. Geometria Simplificada

As dimensões foram extraídas dos **nomes** dos elementos, não da geometria 3D real.

**Exemplos:**
- `IfcColumn - P21 (236x40)` → seção 236×40 cm
- `IfcBeam - Viga 14 (30x55)` → seção 30×55 cm
- `IfcSlab - Pano 28 (28 cm)` → espessura 28 cm

**Limitação:**  
Não captura variações de seção ao longo do elemento (pilares que afunilam, vigas com mísulas, etc.).

**Possível refinamento:**  
Processar geometria 3D real via `ifcopenshell.geom` (mais custoso computacionalmente).

---

## 📐 Observações sobre os Dados Extraídos

### Volumes de Concreto

**Total estimado:** 12.784 m³

**Distribuição:**
- Lajes: 57,6% (7.359 m³)
- Pilares: 23,2% (2.964 m³)
- Vigas: 18,8% (2.406 m³)
- Infraestrutura: 0,4% (55 m³)

**Análise:**
- Proporção lajes/total está alta (esperado 40-50% em edifícios residenciais)
- Pode indicar:
  1. Lajes mais espessas (28 cm é acima do usual)
  2. Áreas de laje superestimadas (estimativa de 20 m² por pano pode estar alta)
  3. Presença de lajes maciças (ao invés de nervuradas)

**Recomendação:**  
Validar espessuras e áreas reais de lajes com projeto.

---

### Distribuição Vertical

**Observação:** O IFC contém 80 `IfcBuildingStorey`, mas muitos duplicados.

**Estrutura identificada:**
- 35 pavimentos únicos nomeados (Fund. → Tampa)
- Possível duplicação devido a:
  - Duas torres no mesmo IFC
  - Rampas modeladas em storeys separados
  - Múltiplos arquivos mesclados

**Recomendação:**  
Confirmar se o projeto possui 1 ou 2 torres.

---

### Seções de Pilares

**Observação:** Grande variedade de seções (126 tipos diferentes).

**Principais:**
- P30 (420×40 cm) - 32 elementos - **Pilares muito grandes** (possivelmente pilares-parede)
- P21, P18, P57, P52 - seções variando de 275×35 a 236×40 cm

**Análise:**
- Seções grandes indicam:
  - Edifício alto (32 pavimentos → cargas significativas)
  - Possível concreto de alta resistência (fck 40-50 MPa)
  - Projeto estrutural otimizado (redução de seções nos pavimentos superiores)

**Recomendação:**  
Confirmar transição de seções ao longo da altura (pilares podem ter seções variáveis por trecho).

---

### Espessura de Lajes

**Espessura predominante:** 28 cm

**Análise:**
- 28 cm é espesso para lajes de edifício residencial (usual: 12-20 cm)
- Pode indicar:
  1. Lajes maciças (não nervuradas/treliçadas)
  2. Sobrecarga alta (garagens, lazer com piscina)
  3. Vãos grandes (redução de vigas)

**Recomendação:**  
Confirmar se lajes são maciças ou mistas (nervurada com capa).  
Se nervuradas, revisar volume de concreto (redução significativa).

---

## 🛠️ Melhorias Possíveis (Próximas Revisões)

### Curto prazo (R01)
1. **Validação de volumes** com planilha do calculista
2. **Inclusão de dados de fundações** (estacas/sapatas)
3. **Especificação de fck** por elemento
4. **Taxa de aço** (estimativa inicial via benchmarks)

### Médio prazo (R02)
1. **Processamento de geometria 3D real** via `ifcopenshell.geom`
2. **Cálculo de áreas de forma** por contato entre elementos
3. **Extração de comprimentos reais** de vigas
4. **Áreas reais** de panos de laje

### Longo prazo (R03+)
1. **Detalhamento de armação** (se disponível em IFC ou pranchas)
2. **Integração com orçamento executivo** (planilha Excel)
3. **Comparação com benchmarks** da base de calibração Cartesian
4. **Análise de custo R$/m³** por elemento

---

## 📊 Benchmarks de Referência

Para validação dos volumes extraídos, comparar com benchmarks de mercado:

### Volume de concreto por pavimento tipo
**Extraído:** ~12.784 m³ / 35 pav ≈ **365 m³/pav**

**Benchmark:** Edifício residencial padrão alto → 200-300 m³/pav

**Análise:**  
Volume está ligeiramente acima do esperado. Possíveis causas:
- Presença de garagens (lajes mais espessas)
- Pavimento lazer (piscina, estrutura especial)
- Duas torres no mesmo modelo

---

### Taxa de concreto por m² de área construída
**Não calculado** - área construída não disponível no IFC.

**Recomendação:**  
Extrair área construída do projeto arquitetônico para calcular:
- **m³ de concreto / m² de área construída** (benchmark: 0,15-0,25 m³/m²)

---

## 🎯 Checklist de Validação

Antes de prosseguir para orçamento executivo, validar:

- [ ] Volume total de concreto (~12.784 m³) com planilha do calculista
- [ ] Espessura de lajes (28 cm é maciça ou total nervurada?)
- [ ] Tipo de fundação (estacas, sapatas, tubulões?)
- [ ] Classes de concreto (fck) por trecho
- [ ] Seções de pilares ao longo da altura (há transição?)
- [ ] Número de torres (1 ou 2?)
- [ ] Área construída total (para cálculo de m³/m²)
- [ ] Sistema de lajes (maciça, nervurada, treliçada?)

---

## 📁 Arquivos Complementares Disponíveis

### DWG Preformas
`projetos/thozen-electra/projetos/01 ESTRUTURA/DWG/1203 - PREFORMAS - R20.DWG`

**Observação:** Revisão R20 (anterior ao IFC R26).

**Possível uso:**
- Detalhamento de armação (se prancha de preforma contiver)
- Validação de seções e dimensões
- Identificação de elementos não modelados no IFC

**Limitação:**  
Requer software CAD (AutoCAD, DraftSight) para processamento.

---

## 🚨 Alertas para o Time

### 1. Volumes são ESTIMATIVAS
Os volumes apresentados foram calculados com premissas conservadoras mas ainda são estimativas.  
**NÃO usar para orçamento final sem validação do projetista estrutural.**

### 2. Dados de armação FALTANTES
Aço representa ~40-50% do custo de estrutura. Sem dados de armação, orçamento fica incompleto.  
**Priorizar obtenção de pranchas de detalhamento ou planilha com taxas de aço.**

### 3. Fundações AUSENTES
Fundações podem representar 15-30% do custo de estrutura.  
**Solicitar urgentemente prancha de locação + especificações de estacas/sapatas.**

### 4. Espessuras de lajes a CONFIRMAR
Se lajes forem nervuradas (não maciças), volume de concreto pode cair 30-50%.  
**Impacto direto no orçamento - confirmar ASAP.**

---

## 💡 Dicas para Próximas Extrações

1. **Sempre verificar** se IFC contém QuantitySets antes de assumir geometria nominal
2. **Documentar premissas** claramente (comprimentos médios, áreas estimadas, etc.)
3. **Cruzar dados** com múltiplas fontes (IFC + DWG + planilha do calculista)
4. **Manter histórico** de revisões para rastreabilidade
5. **Comunicar incertezas** ao time (± % de precisão)

---

**Documento gerado automaticamente via análise técnica de IFC.**  
**Para dúvidas, contatar: @Cartesiano (Slack)**
