# Análise Hidrossanitária - Armínio Tavares

**Data:** 09/03/2026
**Fonte:** IFC Hidrossanitário (Ihs_EX_Placon_Armínio Tavares_R00.ifc)

---

## 1. DADOS EXTRAÍDOS DO IFC

### 1.1 Tubulações
- **Total de segmentos:** 803
- **Comprimento total:** 1.763,71 m (corrigido de cm)
- **Sistemas identificados:** Não especificado no IFC (provavelmente AF, AQ, ES, AP)

### 1.2 Conexões
- **Total:** 428 unidades
- **Tipos principais:**
  - Conexões genéricas: 224
  - TPL (Águas Pluviais): 75 unidades
  - TQS (Esgoto Sanitário): 26 unidades
  - TGD (Gás): 25 unidades
  - TAS (Água Fria/Quente): 30 unidades
  - TVT (Ventilação): 24 unidades

### 1.3 Terminais e Equipamentos
- **Pontos hidráulicos (terminais):** 47
- **Equipamentos sanitários:** Não modelados no IFC
- **Válvulas/Registros:** Não modelados
- **Bombas:** Não modeladas
- **Reservatórios:** Não modelados

### 1.4 Distribuição por Pavimentos
- **17 níveis:** 1º Pavimento ao 16º + Barrilete
- **Elevação total:** 0m (1º Pav) a 43,56m (Barrilete)

---

## 2. ESTIMATIVAS COMPLEMENTARES

Baseado nos dados do IFC + briefing existente (45 unidades, 7.996 m²):

### 2.1 Pontos Hidráulicos Totais
- **Pontos identificados no IFC:** 47
- **Estimativa por unidade:** 8-10 pontos/un (cozinha, banheiros, área de serviço)
- **Total estimado:** 45 un × 9 pontos/un = **405 pontos hidráulicos**
- **Pontos áreas comuns:** ~20 pontos (térreo, subsolos)
- **TOTAL ESTIMADO:** **425 pontos hidráulicos**

### 2.2 Tubulações por Sistema
Baseado no comprimento total extraído (1.764m) e ratios típicos:

| Sistema | % Estimado | Comprimento (m) | ml/m² AC |
|---------|------------|-----------------|----------|
| Água Fria | 35% | 617 | 0,077 |
| Água Quente | 15% | 265 | 0,033 |
| Esgoto Sanitário | 25% | 441 | 0,055 |
| Águas Pluviais | 20% | 353 | 0,044 |
| Gás/Outros | 5% | 88 | 0,011 |
| **TOTAL** | **100%** | **1.764** | **0,221** |

**Observação:** O ratio de 0,221 ml/m² está abaixo da média (0,25-0,35 ml/m² para edifícios residenciais). Possível que algumas tubulações não estejam modeladas no IFC.

### 2.3 Estimativa Ajustada (Ratio de Mercado)
Para edifícios residenciais similares, adotando 0,30 ml/m²:
- **Tubulação total estimada:** 7.996 m² × 0,30 ml/m² = **2.399 m**

| Sistema | ml/m² | Comprimento (m) |
|---------|-------|-----------------|
| Água Fria | 0,105 | 840 |
| Água Quente | 0,045 | 360 |
| Esgoto Sanitário | 0,075 | 600 |
| Águas Pluviais | 0,060 | 480 |
| Gás/Outros | 0,015 | 119 |
| **TOTAL** | **0,300** | **2.399** |

### 2.4 Equipamentos Sanitários
Baseado em 45 unidades residenciais:

| Item | Qtd/Un | Total |
|------|--------|-------|
| Bacias sanitárias | 1,5 | 68 |
| Lavatórios | 1,5 | 68 |
| Chuveiros/Duchas | 1,5 | 68 |
| Tanques | 1,0 | 45 |
| Pias de cozinha | 1,0 | 45 |
| **Subtotal Unidades** | | **294** |
| Áreas Comuns | | 10 |
| **TOTAL** | | **304 equipamentos** |

### 2.5 Registros e Válvulas
- **Registros de gaveta (AF):** 1 por unidade + prumadas = ~60
- **Registros de pressão:** 45 (1 por unidade)
- **Registros de esfera:** ~80
- **Válvulas de retenção:** ~15
- **TOTAL ESTIMADO:** ~200 registros/válvulas

### 2.6 Reservatórios
Baseado em consumo típico (200L/dia por pessoa, 2,5 pessoas/un):
- **Consumo diário:** 45 un × 2,5 pessoas × 200L = 22.500 L/dia
- **Reservatório superior:** 1/3 do diário = 7.500 L (arredondado: **2 × 4.000L**)
- **Reservatório inferior:** 2/3 do diário = 15.000 L (arredondado: **2 × 8.000L**)
- **Reserva de incêndio:** Conforme AVCB

---

## 3. RECOMENDAÇÕES PARA O ORÇAMENTO PARAMÉTRICO

### 3.1 Valores a Incluir no Briefing
- ✅ **Pontos hidráulicos:** 425 pontos
- ✅ **Tubulação total:** 2.399 m (ou 2.400 m arredondado)
- ✅ **Conexões:** 430 unidades (arredondado do IFC)
- ✅ **Equipamentos sanitários:** 304 peças
- ✅ **Registros/Válvulas:** 200 unidades
- ✅ **Reservatórios:** 4 unidades (2×4m³ + 2×8m³)

### 3.2 Ratios de Verificação
- **ml/m² tubulação:** 0,30 (adequado para residencial)
- **pontos/unidade:** 9,4 (adequado)
- **equipamentos/unidade:** 6,5 (adequado)

### 3.3 Próximos Passos
1. ✅ Atualizar briefing-arminio-tavares.md com dados hidrossanitários
2. ⏳ Regerar orçamento paramétrico com valores atualizados
3. ⏳ Comparar com projetos similares da base (Catena, Connect)
4. ⏳ Validar custos de instalações hidrossanitárias

---

**Gerado por:** Cartesiano (OpenClaw)
**Base:** IFC Hidrossanitário + Estimativas de Mercado
