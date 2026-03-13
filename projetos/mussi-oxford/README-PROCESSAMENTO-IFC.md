# 📊 Processamento IFC Estrutural - Oxford (Mussi)

**Status:** ✅ Concluído  
**Data:** 12/03/2026 22:44 BRT  
**Subagente:** oxford-processar-ifc-estrutural

---

## 🎯 Objetivo Alcançado

Extrair quantitativos estruturais completos do arquivo IFC para orçamento executivo.

**Arquivo Processado:**  
`EST_OXFORD600.12.11.2025.ifc` (21 MB, 25.466 produtos)

---

## 📂 Arquivos Gerados

| Arquivo | Descrição | Tamanho |
|---------|-----------|---------|
| **ANALISE-FINAL-IFC.md** ⭐ | Análise consolidada + conclusões + próximos passos | 5,5 KB |
| **oxford-quantitativos-estrutura.md** | Relatório estruturado completo | 6,1 KB |
| **oxford-ifc-dados-brutos.json** | Dados extraídos em JSON (3.741 elementos) | - |
| **processar_ifc_estrutural.py** | Script de extração de quantidades IFC | 11 KB |
| **gerar_relatorio_quantitativos.py** | Script de geração de relatório | 11,3 KB |
| **extrair_volumes_geometria.py** | Script de cálculo geométrico | 3,6 KB |

**📌 COMECE LENDO:** `ANALISE-FINAL-IFC.md`

---

## ✅ Dados Extraídos com Sucesso

- **3.741 elementos** estruturais processados
  - 719 lajes
  - 2.385 vigas
  - 637 pilares
- **33 pavimentos** mapeados e classificados
- **2.390 m³** de concreto (lajes - dado confiável)
- **Padrão de repetição validado:**
  - TIPO 1: 76,95 m³ (ligeiramente diferente)
  - TIPO 2-17: 76,70 m³ cada (16 pavimentos idênticos, variação < 0,1 m³)

---

## ⚠️ Limitações Identificadas

O arquivo IFC **não contém quantidades completas**:

| Item | Status | Observação |
|------|--------|------------|
| Volume de lajes | ✅ Disponível | 2.390 m³ extraídos |
| Volume de vigas | ❌ Ausente | Propriedades IFC não preenchidas |
| Volume de pilares | ❌ Ausente | Propriedades IFC não preenchidas |
| Fundação | ❌ Não modelada | 0 elementos encontrados |
| Peso de aço | ❌ Ausente | Armaduras não modeladas |
| Área de formas | ❌ Ausente | Propriedades não disponíveis |
| Especificações (fck) | ❌ Ausente | Psets vazios |

---

## 💰 Estimativa Preliminar

**Volume Total Estimado:** 3.140 - 3.390 m³  
(baseado em índices + dados parciais do IFC)

**Custo Estrutura (com margem de segurança 15%):**

### R$ 8.927.163,00

**Detalhamento:**
- Concreto (3.265 m³ × R$ 850/m³): R$ 2.775.250
- Aço (275 ton × R$ 7.500/kg): R$ 2.062.500
- Formas (39.000 m² × R$ 75/m²): R$ 2.925.000

⚠️ **Importante:** Esta é uma estimativa conservadora. Valores precisos dependem do processamento das tabelas de quantitativos dos PDFs estruturais.

---

## 🎯 Próximos Passos

### 1. Processar PDFs Estruturais (PRIORITÁRIO)

**Localização:** `/02. PROJETO ESTRUTURAL/EST 260305/`  
**Total:** 170 pranchas com tabelas de resumo quantitativo

**Dados a extrair:**
- Volumes de vigas e pilares
- Elementos de fundação (blocos, sapatas, estacas)
- Peso de aço (por pavimento)
- Áreas de forma
- Especificações técnicas (fck, CA-50/60)

**Prioridade de processamento:**
1. Fundação (PDFs 01-04)
2. Pavimento TIPO 1 (PDFs 88-103) - referência para multiplicadores
3. Vigas e pilares dos demais pavimentos

### 2. Solicitar ao Cliente Mussi

- Memorial descritivo estrutural (especificações de fck, aço)
- Tabelas de resumo quantitativo (se disponíveis separadamente)
- Confirmação se IFC deveria conter fundação modelada

### 3. Validar com Projetista

- Confirmar volume total de concreto
- Confirmar peso total de aço
- Esclarecer ausência de elementos de fundação no IFC
- Verificar se IFC está desatualizado ou incompleto

---

## 📋 Estrutura de Pavimentos Identificada

| Categoria | Pavimentos | Volume Lajes | % |
|-----------|------------|--------------|---|
| Fundação | Fundação | 0,00 m³ | 0% |
| Garagens | G2, G3, G4, G5 + 4 Rampas | 673,00 m³ | 28% |
| Térreo | Térreo | 178,65 m³ | 7% |
| Lazer | Lazer 1 | 129,65 m³ | 5% |
| **Tipos** | **Tipo 1-17 (17 pav)** | **1.304,13 m³** | **55%** |
| Especiais | Ático, Cobertura, Barrilete, Reservatório | 104,66 m³ | 4% |
| **TOTAL** | **33 pavimentos** | **2.390,08 m³** | **100%** |

---

## 🔧 Ferramentas Utilizadas

- **ifcopenshell 0.8.4** - Leitura e processamento de arquivos IFC
- **Python 3.14** - Scripts de extração e análise
- **Metodologia:** Extração de propriedades IFC + cálculo geométrico (validação)

---

## 📞 Contato

**Processamento realizado por:**  
Subagent Jarvis (OpenClaw)  
Data: 12/03/2026  
Sessão: oxford-processar-ifc-estrutural

Para dúvidas sobre a análise ou próximos passos, consultar `ANALISE-FINAL-IFC.md`.

---

**🎓 Lições Aprendidas:**

1. Arquivos IFC podem estar incompletos - sempre validar disponibilidade de quantidades
2. Lajes geralmente têm propriedades mais completas que vigas/pilares
3. PDFs estruturais ainda são fonte primária confiável para quantitativos executivos
4. Cálculo geométrico (bounding box) superestima volumes - usar apenas para validação
5. Fundação nem sempre é modelada em IFC (comum em projetos brasileiros)
