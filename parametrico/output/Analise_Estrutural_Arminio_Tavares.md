# ANÁLISE ESTRUTURAL VIA IFC - ARMINIO TAVARES (PLACON)

**Data:** 09/03/2026 14:21 BRT  
**Arquivo IFC:** PLA_ARM_EST_AP_IFC_REV08.ifc  
**Ferramenta:** ifcopenshell

---

## 📊 RESUMO EXECUTIVO

A análise do IFC estrutural identificou uma **divergência crítica** entre o briefing parametrizado e a estrutura real do projeto:

**Tipo de Laje:**
- **Parametrizado:** Cubetas (laje nervurada)
- **IFC Estrutural:** **Laje Maciça h=20cm (C40)**
- **Impacto no custo:** +R$ 761.607,90 (+2,2%)

---

## 🔍 DADOS EXTRAÍDOS DO IFC

### Elementos Estruturais

| Elemento | Quantidade | Volume (m³) |
|----------|------------|-------------|
| **Pilares** | 193 | 197,07 |
| **Vigas** | 721 | 376,67 |
| **Lajes** | 299 | 1.025,50 |
| **TOTAL CONCRETO** | - | **1.599,24** |

### Tipos de Laje Identificados

| Tipo | Quantidade | % |
|------|------------|---|
| **TQS h=20 - Concreto C40** (Maciça) | 232 | 77,6% |
| TQS - Tubulão | 48 | 16,1% |
| Patamar monolítico (h=15cm) | 15 | 5,0% |
| Outros | 4 | 1,3% |

**Conclusão:** Predominância clara de **laje maciça** (77,6% dos elementos).

### Consumo de Concreto

- **Volume total:** 1.599,24 m³
- **Área construída:** 7.996,45 m²
- **Consumo:** **200 litros/m²** (0,20 m³/m²)

**Benchmark:**
- Residencial econômico: 150-180 L/m²
- Residencial padrão: 180-220 L/m²
- Alto padrão/complexo: 220-280 L/m²

**Status:** ✅ **Consumo alinhado com padrão médio** (200 L/m² está dentro do esperado).

### Pavimentos

- **Total identificado:** 23 pavimentos
- **Distribuição:**
  - 2 subsolos (Provisório + Subsolo)
  - 1 térreo (1º Pavto)
  - 15 pavimentos tipo (2º ao 16º, incluindo 2 transições)
  - 5 pavimentos técnicos (Barrilete, Casa Máquinas, Reservatório, Tampa Res, Duto)

---

## 💰 IMPACTO NO ORÇAMENTO PARAMÉTRICO

### Correção Aplicada

| Item | v2 (Cubetas) | v3 (Maciça IFC) | Diferença |
|------|--------------|-----------------|-----------|
| **Custo/m²** | R$ 4.336,29 | **R$ 4.431,54** | +R$ 95,25 (+2,2%) |
| **Custo Total** | R$ 34.674.954 | **R$ 35.436.562** | +R$ 761.608 |
| **Custo/Unidade** | R$ 770.555 | **R$ 787.479** | +R$ 16.924 |
| **CUB Ratio** | 1,38× | **1,41×** | +0,03 |

### Detalhamento do Ajuste

**Macrogrupo afetado:** Supraestrutura

- Mediana base (CUB dez/23): R$ 693,58/m²
- Mediana atualizada (CUB mar/26): R$ 793,69/m²
- **Fator de ajuste (laje maciça):** 1,12× (+12%)
- **Delta de custo:** +R$ 95,24/m²

**Justificativa:** Laje maciça consome ~12% mais concreto e forma que laje nervurada (cubetas), impactando diretamente o custo de supraestrutura.

---

## ✅ VALIDAÇÃO TÉCNICA

### Consistência dos Dados

1. **Volume de concreto** (1.599 m³) está consistente com:
   - Área construída (7.996 m²)
   - 23 pavimentos
   - Laje maciça h=20cm

2. **Consumo de 200 L/m²** está dentro do esperado para:
   - Edifício residencial de médio/alto padrão
   - Centro urbano (Florianópolis)
   - Sem fundação especial (não foram detectadas estacas/sapatas no IFC)

3. **Tipos de laje** confirmam especificação de projeto:
   - Concreto C40 (resistência adequada para 16 pavimentos)
   - Espessura h=20cm (padrão para lajes maciças em edifícios)

### Observações

⚠️ **Fundação não detectada:** O IFC estrutural não contém elementos de fundação (IfcPile, IfcFooting). Isso pode significar:
- IFC incompleto (apenas superestrutura)
- Fundação em disciplina/arquivo separado
- Fundação não modelada em BIM

**Recomendação:** Confirmar tipo de fundação (Estacas Escavadas foi assumido no briefing, típico para centro de Florianópolis).

---

## 📁 ARQUIVOS GERADOS

1. **Análise estrutural (JSON):**  
   `projetos/arminio-tavares/analise-estrutura.json`

2. **Orçamento atualizado (Excel):**  
   `output/Arminio-Tavares-Parametrico-v3-estrutural-20260309-1421.xlsx`

3. **Briefing atualizado (Markdown):**  
   `output/Briefing_Arminio-Tavares_20260309.md`

4. **Briefing atualizado (Word):**  
   `output/Briefing_Arminio-Tavares_20260309.docx`

5. **Este relatório (Markdown):**  
   `output/Analise_Estrutural_Arminio_Tavares.md`

---

## 🎯 CONCLUSÕES

1. ✅ **IFC estrutural processado com sucesso** — 1.213 elementos analisados (193 pilares + 721 vigas + 299 lajes)

2. ⚠️ **Tipo de laje corrigido** — Cubetas → Laje Maciça h=20cm (impacto +2,2% no custo)

3. ✅ **Consumo de concreto validado** — 200 L/m² está dentro do benchmark para o padrão do projeto

4. ✅ **Orçamento atualizado** — Versão 3 reflete a estrutura real do projeto (R$ 35,4 milhões)

5. ⚠️ **Fundação pendente** — Confirmar tipo de fundação (IFC estrutural não contém elementos de fundação)

---

**Próximos passos sugeridos:**
1. Validar tipo de fundação com equipe estrutural
2. Conferir se há IFC de fundação separado
3. Revisar especificações de concreto (C40 confirmado para lajes)

---

**Gerado por:** Paramétrico (Cartesian Engenharia)  
**Ferramenta:** ifcopenshell + Python 3.11  
**Versão:** 1.0
