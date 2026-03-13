# 🏗️ RESUMO EXECUTIVO - ESTRUTURA OXFORD

**Cliente:** Mussi Empreendimentos  
**Projeto:** Edifício Oxford  
**Data:** 12/03/2026 23:50 BRT

---

## 📊 QUANTITATIVOS TOTAIS

### Concreto
- **Fundação:** 455 m³ (blocos sobre estacas tipo 60)
- **Lajes:** 2.390 m³ (dado IFC completo)
- **Vigas + Pilares:** ~500 m³ (estimado)*
- **TOTAL:** ~3.345 m³

### Aço (CA-50/CA-60)
- **Fundação:** 54,8 ton
- **Vigas:** 30,2 ton
- **Lajes:** 108,3 ton
- **Pilares:** ~47 ton (parcial medido + estimado)*
- **TOTAL:** ~240 ton
- **Taxa:** 71,7 kg/m³ ✅ (dentro da faixa 70-90 kg/m³ para edifícios altos)

### Formas
- **TOTAL:** ~40.000 m² (estimado)*

---

## 💰 CUSTO ESTIMADO (Índices SC Mar/2026)

| Item | Quantidade | R$/un | Subtotal |
|------|-----------|-------|----------|
| Concreto | 3.345 m³ | R$ 850 | R$ 2,84 mi |
| Aço | 240 ton | R$ 7.500/ton | R$ 1,80 mi |
| Formas | 40.000 m² | R$ 75 | R$ 3,00 mi |
| **TOTAL** | - | - | **R$ 7,64 mi** |

**Custo/m² área:** R$ 1.770/m² ✅ (compatível com edifícios altos SC)

---

## 🔍 METODOLOGIA

**Fontes de Dados:**
1. **IFC (EST_OXFORD600.12.11.2025.ifc):**
   - Volume lajes: 2.390 m³ (100% preciso)
   - 25.466 produtos processados
   - 3.741 elementos estruturais

2. **PDFs (EST 260305 - 27 de 170 pranchas):**
   - Fundação: 100% processado
   - Pavimentos: Amostragem inteligente com multiplicadores
   - Garagem 2 representa G2-G5 (×4)
   - Tipos 2-17 idênticos confirmados (×16)

**Confiabilidade:**
- ✅ **Alta:** Lajes (IFC), Fundação (PDFs), Aço lajes/vigas (amostra)
- ⚠️ **Média:** Vigas/pilares volume (estimado), Formas (estimado)

---

## 🏢 ESTRUTURA DO EDIFÍCIO

- **Fundação:** Blocos sobre estacas tipo 60, fck 50 MPa
- **Garagens:** 5 níveis (G1 a G5)
- **Térreo + Lazer:** 2 níveis
- **Pavimentos Tipo:** 17 unidades (TIPO 1 + TIPOS 2-17 idênticos)
- **Ático + Cobertura:** 2 níveis
- **TOTAL:** 26 pavimentos

---

## ⚠️ OBSERVAÇÕES

**Valores Estimados (*) - Validar com Calculista:**
1. Volume de vigas e pilares (~500 m³)
2. Aço de pilares pavimentos tipo (~45 ton)
3. Área de formas (~40.000 m²)

**Próximos Passos:**
1. Validar volumes de vigas/pilares com projetista estrutural
2. Obter área de formas precisa (calculista ou cálculo por geometria IFC)
3. Confirmar especificações de concreto (fck por elemento)

---

**Documento Completo:** `oxford-quantitativos-estrutura.md`  
**Dados Brutos:** `temp-oxford-pdfs/quantitativos_*.json`
