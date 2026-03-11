# BRIEFING PARAMÉTRICO - ARMINIO TAVARES (PLACON)

**Data:** 09/03/2026  
**Cliente:** Placon  
**Projeto:** Arminio Tavares  
**Fonte:** IFC fornecido

---

## DADOS EXTRAÍDOS DO IFC

### Arquitetura (IFC_ARQ_R06)
- **Área Construída Total (AC):** 7.996,45 m²
- **Área do Terreno (AT):** 486,40 m²
- **Unidades Residenciais (UR):** 45 apartamentos
- **Número de Pavimentos Totais:** 22 (2 subsolos + 16 pav + 4 técnicos)
- **Número de Pavimentos Tipo (NP):** 15
- **Número de Subsolos (NS):** 2 (1.314,20 m²)
- **Número de Elevadores (NE):** 2
- **Vagas de Garagem:** ~50
- **Área Térreo (grande):** 1.513,57 m² (áreas comuns significativas)

### Estrutura (IFC_EST_REV08) - Análise Quantitativa
- **Volume Total de Concreto:** 1.599,24 m³
  - Pilares: 197,07 m³ (193 pilares)
  - Vigas: 376,67 m³ (721 vigas)
  - Lajes: 1.025,50 m³ (299 lajes)
- **Consumo de Concreto:** 200 litros/m² (0,20 m³/m²)
- **Tipo de Laje Predominante:** Maciça h=20cm (C40) - 77% das lajes
- **Pavimentos Estruturais:** 23 (incluindo provisório, subsolos, técnicos)

---

## 25 VARIÁVEIS DO BRIEFING PARAMÉTRICO

### 1. ALTO IMPACTO (Multiplicadores)

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| **Tipo de Laje** | Maciça h=20cm (C40) | Confirmado via IFC estrutural (232 lajes) |
| **Padrão de Acabamento** | Médio/Alto Padrão | Confirmado (padrão PLACON) |
| **Sistema de Contenção** | Cortina de concreto | Terreno urbano central (2 subsolos) |
| **Prazo de Obra** | 30 meses | Prazo típico para edifício deste porte |

### 2. ESPECIFICAÇÕES TÉCNICAS

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| **Tipo de Fundação** | Estacas Escavadas | Terreno centro Florianópolis |
| **Tipo de Estrutura** | Concreto Armado | Padrão mercado |
| **Tipo de Vedação** | Alvenaria Convencional | Padrão |
| **Tipo de Cobertura** | Laje Impermeabilizada | Padrão |
| **Tipo de Esquadrias** | Alumínio Anodizado | Alto padrão |
| **Tipo de Fachada** | Textura + Pintura | Padrão mercado |
| **Tipo de Piso Garagem** | Concreto Polido | Padrão |
| **Sistema Elétrico** | Barramento Blindado | +5% em instalações elétricas |

### 3. EQUIPAMENTOS E SISTEMAS

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| **Elevadores** | 2 | Extraído do IFC |
| **Gerador** | Sim | Padrão para alto padrão |
| **Sistema de Ar Condicionado Central** | Não | Padrão mercado |
| **Sistema de Automação Predial** | Básica | Confirmado no briefing detalhado |
| **Infraestrutura Carro Elétrico** | Sim | Tendência atual |
| **Sistema de Captação de Água da Chuva** | Não | Não especificado |
| **Aquecimento Solar** | Não | Não especificado |
| **Sistema de Pressurização de Escada** | Sim | Exigência NBR para 15 pavimentos |

### 4. ÁREAS DE LAZER

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| **Área de Lazer** | Completo (Piscina + Academia) | Padrão alto padrão |
| **Salão de Festas** | Sim | Padrão |
| **Playground** | Sim | Padrão |

### 5. COMPLEXIDADE

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| **Topografia do Terreno** | Plano | Assumido (não especificado no IFC) |
| **Dificuldade de Acesso** | Normal | Terreno urbano central |

---

## CÁLCULO BASE

- **CUB SC mar/2026:** R$ 3.150,00/m²
- **Base de calibração:** 58 projetos Cartesian
- **Metodologia:** Medianas por macrogrupo × fator CUB × fatores de briefing

---

## RESULTADO ✅

### Versão 3 - Ajustado com IFC Estrutural

- **Custo Total:** R$ 35.436.562,23
- **Custo/m²:** R$ 4.431,54
- **Custo/Unidade (45 un):** R$ 787.479,16
- **CUB Ratio:** 1,41×

**Ajuste realizado:**
- Tipo de laje corrigido: Cubetas → **Laje Maciça h=20cm** (confirmado via IFC estrutural)
- Impacto: +R$ 761.607,90 (+2,2%) em relação à versão anterior
- Fator de ajuste supraestrutura: 1,12× (laje maciça +12% vs cubetas)

**Base de Cálculo:**
- CUB mar/2026: R$ 3.150,00/m²
- Base calibração: 58 projetos (dez/2023)
- Fator atualização CUB: 1,1443×
- Área Construída: 7.996,45 m²
- Volume Concreto (IFC): 1.599,24 m³ (200 L/m²)

---

## OBSERVAÇÕES

1. ⚠️ **BRIEFING ATUALIZADO (09/03/2026 13:10)** — Correção de dados críticos após revisão
2. Dados extraídos do IFC detalhado em `projetos/arminio-tavares/briefing-arminio-tavares.md`
3. **Erro corrigido:** Área construída atualizada de 2.772 m² → 7.996,45 m² (+188%)
4. Variáveis de impacto em custo ajustadas:
   - Sistema elétrico: Barramento blindado (+5%)
   - Automação: Básica (não "Não")
   - Contenção: Cortina de concreto
   - Fundação: Estacas escavadas (não hélice contínua)
5. **Orçamento precisa ser regenerado** com área correta

---

**Gerado por:** Paramétrico (Cartesian Engenharia)  
**Versão:** 1.1 (atualizado após revisão)  
**Atualização:** 09/03/2026 13:10 BRT
