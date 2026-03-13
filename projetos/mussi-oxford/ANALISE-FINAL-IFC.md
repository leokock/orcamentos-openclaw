# OXFORD - MUSSI EMPREENDIMENTOS
## Análise Final IFC Estrutural

**Data:** 12/03/2026 22:44 BRT  
**Arquivo:** EST_OXFORD600.12.11.2025.ifc  
**Processamento:** Completo (25.466 produtos)

---

## ⚠️ CONCLUSÕES CRÍTICAS

### 1. Limitações do Arquivo IFC

O arquivo IFC fornecido **não contém quantidades completas** de volume de concreto para todos os elementos:

- ✅ **Lajes:** Quantidades IFC disponíveis (2.390 m³ extraídos)
- ❌ **Vigas:** Quantidades IFC ausentes (volume = 0)
- ❌ **Pilares:** Quantidades IFC ausentes (volume = 0)
- ❌ **Fundação:** Elementos não modelados (0 encontrados)

### 2. Tentativas de Extração

| Método | Resultado | Observação |
|--------|-----------|------------|
| **Propriedades IFC (IfcQuantityVolume)** | 2.390 m³ | Apenas lajes têm quantidades |
| **Cálculo Geométrico (bounding box)** | ~7.183 m³ | Superestimado (inclui vazios) |
| **Recomendado** | Usar PDFs estruturais | Tabelas de quantitativos são fonte confiável |

### 3. Dados Confirmados

**✅ EXTRAÍDOS COM SUCESSO DO IFC:**
- Total de elementos: **3.741** (719 lajes + 2.385 vigas + 637 pilares)
- Estrutura de pavimentos: **33 níveis**
- Padrão de repetição: **TIPO 2-17 idênticos** (16× pavimentos tipo)
- Volume de lajes: **2.390 m³** (confiável)

**❌ NÃO DISPONÍVEIS NO IFC:**
- Volume de vigas e pilares
- Peso de aço (armaduras não modeladas)
- Áreas de forma
- Especificações de materiais (fck, CA-50/60)
- Elementos de fundação

---

## RECOMENDAÇÕES PARA ORÇAMENTO EXECUTIVO

### Fonte de Dados Recomendada

**1ª Opção (PREFERENCIAL):** Tabelas de quantitativos dos PDFs estruturais
- Localização: `/02. PROJETO ESTRUTURAL/EST 260305/`
- Total: 170 pranchas com tabelas de resumo
- Contém: volumes, peso de aço, áreas de forma, especificações

**2ª Opção:** Combinar IFC (lajes) + PDFs (vigas, pilares, fundação)
- Usar IFC para validação e contagem de elementos
- Extrair quantidades precisas dos PDFs

**3ª Opção:** Solicitar arquivo IFC atualizado
- Pedir ao projetista para incluir quantidades de vigas/pilares
- Modelar fundação no IFC

### Estimativas Conservadoras (Baseadas em Índices)

Para orçamento preliminar, usar taxas médias SC:

**Volume de Concreto:**
- Lajes (IFC confirmado): 2.390 m³
- Vigas (estimativa): ~400-500 m³ (taxa 15-20% do total)
- Pilares (estimativa): ~150-200 m³ (taxa 5-8% do total)
- Fundação (estimativa): ~200-300 m³ (sem dados)
- **TOTAL ESTIMADO:** 3.140 - 3.390 m³

**Aço:**
- Taxa para edifícios altos: 80-90 kg/m³
- **TOTAL ESTIMADO:** 250-300 toneladas

**Formas:**
- Taxa média: 12 m²/m³
- **TOTAL ESTIMADO:** 37.000 - 40.000 m²

**Custos Estimados (índices SC fev/2026):**
- Concreto (3.265 m³ × R$ 850/m³): R$ 2.775.250
- Aço (275 ton × R$ 7.500/kg): R$ 2.062.500
- Formas (39.000 m² × R$ 75/m²): R$ 2.925.000
- **TOTAL:** R$ 7.762.750

⚠️ **Margem de segurança: +15%** → R$ 8.927.163

---

## PRÓXIMOS PASSOS

### Ações Imediatas

1. **Solicitar ao cliente Mussi:**
   - Tabelas de quantitativos dos PDFs (se disponíveis separadamente)
   - Memorial descritivo estrutural (especificações de fck, aço)
   - Confirmação se IFC contém fundação modelada

2. **Processar PDFs estruturais:**
   - Extrair tabelas de resumo quantitativo
   - Priorizar: Fundação (PDFs 01-04), Tipo 1 (PDFs 88-103), Vigas/Pilares

3. **Validar com projetista:**
   - Confirmar volume total de concreto
   - Confirmar peso de aço
   - Esclarecer ausência de fundação no IFC

### Arquivos Gerados

Os seguintes arquivos foram criados nesta análise:

- ✅ `oxford-quantitativos-estrutura.md` - Relatório estruturado
- ✅ `oxford-ifc-dados-brutos.json` - Dados completos em JSON
- ✅ `processar_ifc_estrutural.py` - Script de extração
- ✅ `gerar_relatorio_quantitativos.py` - Script de relatório
- ✅ `extrair_volumes_geometria.py` - Script de cálculo geométrico
- ✅ `ANALISE-FINAL-IFC.md` - Este documento

---

## DETALHAMENTO TÉCNICO

### Pavimentos Identificados (33 níveis)

| Categoria | Pavimentos | Volume Lajes (m³) | % do Total |
|-----------|------------|-------------------|------------|
| **Fundação** | Fundação | 0.00 | 0% |
| **Garagens** | G2, G3, G4, G5 + 4 Rampas | 673.00 | 28% |
| **Térreo** | Térreo | 178.65 | 7% |
| **Lazer** | Lazer 1 | 129.65 | 5% |
| **Tipos** | Tipo 1-17 (17 pavimentos) | 1.304.13 | 55% |
| **Especiais** | Ático, Cobertura, Barrilete, Reservatório | 104.66 | 4% |
| **TOTAL** | **33 pavimentos** | **2.390.08 m³** | **100%** |

### Elementos Estruturais

| Tipo | Quantidade | Volume IFC | Observação |
|------|------------|------------|------------|
| **Lajes** | 719 | 2.390 m³ | ✅ Dados confiáveis |
| **Vigas** | 2.385 | 0 m³ | ❌ Quantidades ausentes |
| **Pilares** | 637 | 0 m³ | ❌ Quantidades ausentes |
| **Fundação** | 0 | 0 m³ | ❌ Não modelada |
| **TOTAL** | **3.741** | **2.390 m³** | Apenas lajes |

### Padrão de Repetição Validado

- **TIPO 1:** 76.95 m³ (ligeiramente diferente)
- **TIPO 2-17:** 76.70 m³ cada (variação < 0.1 m³)
- ✅ **Confirmado:** 16 pavimentos tipo idênticos

---

## GLOSSÁRIO TÉCNICO

- **IFC:** Industry Foundation Classes (formato de modelo 3D)
- **ifcopenshell:** Biblioteca Python para leitura de arquivos IFC
- **IfcQuantityVolume:** Propriedade IFC que armazena volumes
- **Bounding box:** Caixa envolvente (superestima volume real)
- **fck:** Resistência característica do concreto à compressão
- **CA-50/CA-60:** Categorias de aço para construção civil

---

**Processamento realizado por:**  
Subagente Jarvis Oxford IFC  
ifcopenshell 0.8.4.post1  
Python 3.14 / macOS
