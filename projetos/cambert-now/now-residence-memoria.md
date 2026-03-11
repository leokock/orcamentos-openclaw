# MEMÓRIA DE CÁLCULO — ORÇAMENTO PARAMÉTRICO NOW RESIDENCE

**Projeto:** NOW Residence  
**Cliente:** Belli Empreendimentos Ltda. (CNPJ: 76.323.427/0001-92)  
**Localização:** Rua Luiz Berlim, 123, Centro, Itajaí/SC  
**Arquiteto:** Simon Martignone (CAU-SC: A 165367-9)  
**Data da Análise:** 11/03/2026  
**Responsável Técnico:** Cartesian Engenharia  
**Método:** Orçamento Paramétrico Calibrado (Base: 75 projetos reais)  

---

## 1. DADOS GERAIS DO PROJETO

| Parâmetro | Valor | Observação |
|-----------|-------|-----------|
| **Área Construída (AC)** | 13.054 m² | Incluindo shafts e áreas comuns |
| **Área Computável** | 8.244 m² | ~63% da AC total |
| **Unidades Residenciais (UR)** | 136 apartamentos | 8/andar × 17 pavimentos tipo + ático |
| **Unidades Comerciais** | 2 salas | Térreo (60,15 m² + 62,49 m²) |
| **Total de Pavimentos (NP)** | 24 | 3 garagens + térreo + lazer + 17 tipos + ático + cobertura |
| **Pavimentos Tipo (NPT)** | 17 | 6º ao 20º pavimento |
| **Elevadores** | 3 | 2 sociais + 1 emergência |
| **Vagas de Garagem** | 110 | 3 subsolos (G1, G2, G3) |
| **Área do Terreno** | ~1.500 m² | Estimativa (centro Itajaí) |
| **Pé-direito Tipo** | 3,06 m | Entre lajes |
| **Altura Total** | ~78,72 m | Da fundação ao topo |

---

## 2. TIPOLOGIAS DOS APARTAMENTOS

| Tipologia | Qtd | Área Privativa | Distribuição |
|-----------|-----|---------------|--------------|
| Studios (~32 m²) | 34 | 31,83-31,84 m² | 2 un/pav × 17 pav |
| 1 dorm (~39-40 m²) | 51 | 39,46-39,91 m² | 3 un/pav × 17 pav |
| 2 dorms (~45 m²) | 17 | 45,14 m² | 1 un/pav × 17 pav |
| 2 dorms (~71-73 m²) | 34 | 71,42-72,96 m² | 2 un/pav × 17 pav |
| **TOTAL** | **136** | — | 8 un/pav × 17 pav |

**Índice AC/UR:** 95,98 m²/unidade  
**Índice Vagas/UR:** 0,81 vagas/unidade  

---

## 3. ESPECIFICAÇÕES TÉCNICAS PRINCIPAIS

### 3.1 Estrutura
- **Sistema:** Concreto armado + protendido (misto)
- **Fundação:** Estaca hélice contínua (provável, 3 subsolos)
- **Contenção:** Cortina de estacas (3 subsolos, centro Itajaí)
- **Lajes:** Mista (armado + protendido, conforme memorial)
- **Subsolos:** 3 pavimentos de garagem

### 3.2 Vedações e Revestimentos
- **Paredes externas:** Alvenaria blocos cerâmicos
- **Paredes internas:** Drywall ou alvenaria (misto)
- **Fachada:** Mista (tijolinho + ripado + reboco/textura)
  - Tijolinho: 890 m²
  - Ripado: 475 m²
  - Peitoril: 800 ml (880 m²)
- **Piso interno:** Laminado (áreas privativas), porcelanato (áreas comuns)
- **Revestimento interno:** Reboco + pintura, cerâmica em BWCs

### 3.3 Esquadrias e Fechamentos
- **Esquadrias:** Alumínio anodizado com vidro
- **Portas:** Internas (madeira), entrada (blindada)
- **Guarda-corpo:** Vidro temperado + corrimão metálico (varandas)

### 3.4 Instalações
- **Aquecimento:** Gás individual
- **Elétricas:** Padrão residencial (quadros, circuitos, iluminação)
- **Hidrossanitárias:** Água fria, esgoto, águas pluviais, gás GLP
- **Pressurização:** Sim (3 elevadores + 24 pavimentos)
- **Preventivas:** SPDA, hidrantes, extintores, sinalização

### 3.5 Sistemas Especiais
- **Gerador:** Provável (padrão alto + 3 elevadores)
- **Automação:** Básico (CFTV + interfone)
- **Fotovoltaicas:** Não mencionado no projeto
- **Ponto carro elétrico:** Não mencionado no projeto

### 3.6 Lazer e Complementares
**Programa de Lazer Completo (12 itens):**
- Academia (73,98 m²)
- Sala de Jogos (49,71 m²)
- 2 Salões de Festas (42,22 + 32,66 m²)
- Piscina (37,80 m²)
- Deck (68,83 m²)
- Espaço Zen (18,96 m²)
- Brinquedoteca (18,52 m²)
- Massagem (12,73 m²)
- Sauna (16,38 m²)
- Pet Place (80,74 m²)
- Crossfit (37,39 m²)
- Playground (76,89 m²)

---

## 4. MÉTODO DE CÁLCULO

### 4.1 Modelo Paramétrico

O orçamento paramétrico utiliza a seguinte fórmula:

```
Valor Final (R$/m²) = Base × Fator CUB × Fator Briefing Composto
```

**Onde:**
- **Base:** Mediana calibrada do macrogrupo (R$/m² base dez/2023)
- **Fator CUB:** Ajuste de inflação (CUB Atual / CUB Base)
- **Fator Briefing Composto:** Produto dos fatores das 25 perguntas de caracterização

### 4.2 Base de Calibração

| Parâmetro | Valor |
|-----------|-------|
| **Projetos na Base** | 75 projetos reais |
| **CUB Base Histórico** | R$ 2.752,67/m² (dez/2023) |
| **CUB Atual Utilizado** | R$ 3.200,00/m² (mar/2026 — estimativa SC) |
| **Fator CUB** | 1,163 (= 3.200 / 2.752,67) |
| **Faixas de Variação** | P10-P90 (10º e 90º percentis da base) |

### 4.3 Briefing de Caracterização (25 Perguntas)

| # | Pergunta | Resposta | Fator Principal | Macrogrupo Afetado |
|---|----------|----------|-----------------|-------------------|
| Q1 | Tipo de Fundação | Estaca hélice contínua | 1,00 | Infraestrutura |
| Q2 | Tipo de Laje | Mista | 1,03 | Supraestrutura |
| Q3 | Contenção | Cortina de estacas | 1,40 | Infraestrutura |
| Q4 | Subsolos | 3+ | 5,00 / 1,60 / 1,90 | Mov. Terra / Infra / Impermeab. |
| Q5 | Padrão | Alto | 1,00-1,45 | Acabamentos (múltiplos) |
| Q6 | Esquadria | Alumínio anodizado | 1,00 | Esquadrias |
| Q7 | Piso | Porcelanato padrão | 1,00 | Pisos |
| Q8 | Vedação | Alvenaria | 1,00 | Alvenaria |
| Q9 | Forro | Gesso liso | 1,00 | Teto |
| Q10 | Fachada | Misto | 1,30 | Fachada |
| Q11 | MO Fachada | Empreitada | 1,20 | Fachada |
| Q12 | Cobertura Habitável | Completa | 1,25 | Complementares |
| Q13 | Aquecimento | Gás individual | 1,00 | Instalações |
| Q14 | Automação | Básico | 1,00 | Sist. Especiais |
| Q15 | Energia | Sem | 1,00 | Sist. Especiais |
| Q16 | Lazer | Completo | 1,00 | Complementares |
| Q17 | Paisagismo | Básico | 1,00 | Complementares |
| Q18 | Mobiliário | Básico | 1,00 | Complementares |
| Q19 | Prazo | 36 meses | 1,00 | Gerenciamento |
| Q20 | Região | Litoral SC | 1,00 | TODOS |
| Q21 | Gerador | Sim | 1,15 | Sist. Especiais |
| Q22 | Subestação | Não | 1,00 | Sist. Especiais |
| Q23 | Fotovoltaicas | Não | 1,00 | Sist. Especiais |
| Q24 | Carro Elétrico | Não | 1,00 | Instalações |
| Q25 | Pressurização | Sim | 1,08 | Instalações |

**Fator Briefing Composto Estimado:** ~1,15 (conservador)  
**Fator Total (CUB × Briefing):** 1,163 × 1,15 = **1,337**

---

## 5. RESULTADOS DO ORÇAMENTO PARAMÉTRICO

### 5.1 Custo Total Estimado

| Indicador | Valor | Observação |
|-----------|-------|-----------|
| **Custo Total** | R$ 57.128.602,80 | Estimativa preliminar |
| **Custo/m²** | R$ 4.376,33 | Base AC = 13.054 m² |
| **Custo/Unidade** | R$ 420.063,26 | 136 apartamentos |
| **CUB Ratio** | 1,37 | Custo/m² ÷ CUB Atual |

**⚠️ IMPORTANTE:** Estes são valores **estimados** via cálculo manual das fórmulas. A planilha Excel contém os valores exatos calculados automaticamente.

### 5.2 Top 5 Macrogrupos por Valor

| # | Macrogrupo | Valor (R$) | % | R$/m² |
|---|------------|------------|---|-------|
| 1 | Supraestrutura | 11.861.035,30 | 20,8% | 908,61 |
| 2 | Gerenciamento | 7.167.405,57 | 12,5% | 549,06 |
| 3 | Instalações | 5.904.601,90 | 10,3% | 452,32 |
| 4 | Esquadrias | 5.300.773,73 | 9,3% | 406,07 |
| 5 | Infraestrutura | 3.468.347,17 | 6,1% | 265,69 |

### 5.3 Distribuição Completa por Macrogrupo

**Abrir a planilha gerada para visualizar:**
- Custos detalhados dos 18 macrogrupos
- Percentuais finais calculados
- Semáforos de alerta (verde/amarelo/vermelho)
- Faixas de variação (P10-P90)

---

## 6. FATORES QUE IMPACTAM O CUSTO

### 6.1 Fatores de Elevação de Custo

| Característica | Impacto | Macrogrupo Afetado |
|----------------|---------|-------------------|
| 3 subsolos (garagens) | +60% | Infraestrutura + Mov. Terra |
| Contenção cortina de estacas | +40% | Infraestrutura |
| Laje mista (protendido + armado) | +3% | Supraestrutura |
| Padrão Alto | +20-45% | Acabamentos (múltiplos) |
| Fachada mista (tijolinho + ripado) | +30% | Fachada |
| Lazer completo (12 itens) | +40% | Complementares |
| Centro Itajaí (mobilização, logística) | +5-10% | Gerenciamento/Indiretos |
| Pressurização (24 pavimentos) | +8% | Instalações |
| Gerador (3 elevadores) | +15% | Sist. Especiais |

### 6.2 Fatores de Redução de Custo

| Característica | Impacto | Observação |
|----------------|---------|------------|
| Repetição de pavimentos (17 tipos) | -5-10% | Produtividade estrutura/forma |
| Laminado em vez de porcelanato | -15% | Piso áreas privativas |
| Automação básica (sem full home) | -30% | Sist. Especiais |
| Sem fotovoltaicas | -10% | Sist. Especiais |
| Sem ponto carro elétrico | -5% | Instalações |

---

## 7. ANÁLISE DE PRODUTO

### 7.1 Indicadores de Produto

| Indicador | Este Projeto | Faixa Típica | Status |
|-----------|--------------|--------------|--------|
| **AC/UR** | 95,98 m²/UR | 90-160 m²/UR | ✓ OK |
| **Vagas/UR** | 0,81 vagas/UR | 1,0-2,0 vagas/UR | ⚠ Baixo |
| **% Tipo (NPT/NP)** | 70,8% (17/24) | 60-80% | ✓ OK |
| **Elevador/UR** | 0,022 elev/UR | 0,015-0,030 | ✓ OK |
| **CUB Ratio** | 1,37 | 1,00-1,50 | ✓ OK |

### 7.2 Observações Técnicas

**Pontos Fortes:**
- Proporção AC/UR adequada (95,98 m²/un)
- Boa repetição de pavimentos tipo (70,8%)
- Lazer completo e bem dimensionado
- Padrão alto bem caracterizado (tijolinho, ripado, vidros)
- Localização privilegiada (centro Itajaí)

**Pontos de Atenção:**
- Índice vagas/UR abaixo da faixa típica (0,81 vs 1,0-2,0)
  - **Justificativa:** Localização centro + perfil studios/1 dorm (59% das unidades)
- Custo elevado de infraestrutura (3 subsolos + contenção)
- Custo elevado de fachada (tijolinho + ripado)
- Logística complexa (centro urbano, restrições de horário)

---

## 8. PREMISSAS E LIMITAÇÕES

### 8.1 Premissas Adotadas

1. **CUB:** R$ 3.200,00/m² (mar/2026 — estimativa SC, sem confirmação oficial)
2. **Data-base:** mar/2026
3. **Prazo:** 36 meses (estimativa padrão)
4. **Condições normais de obra:**
   - Sem atrasos de fornecimento
   - Equipe experiente
   - Condições climáticas favoráveis
   - Projetos executivos completos e compatibilizados

### 8.2 Não Inclui

- **Terreno:** Custo de aquisição do terreno
- **Projetos:** Custos de projetos complementares (arquitetura, estrutura, instalações)
- **Aprovações:** Taxas de aprovação, alvarás, registros
- **Marketing e Vendas:** Publicidade, estande de vendas, corretagem
- **Impostos:** ISS, PIS, COFINS, IR
- **Financeiro:** Juros, financiamento, garantias
- **Paisagismo Externo:** Calçadas, muros, portaria externa
- **Decoração Interna:** Ambientes decorados além do básico

### 8.3 Limitações do Método

1. **Estimativa Preliminar:** Não substitui orçamento executivo detalhado
2. **Variação Possível:** ±15-20% conforme fornecedores, época do ano, condições de mercado
3. **Faixas P10-P90:** Baseadas em 75 projetos da base Cartesian (2022-2024)
4. **Quantitativos Estruturais:** IFC sem dados quantitativos extraíveis (volume concreto, aço, forma)
5. **Quantitativos Fachada:** Dados parciais (tijolinho, ripado, peitoril confirmados; restante estimado)
6. **Quantitativos Instalações:** Parte extraída do IFC Elétrico, parte estimada via índices paramétricos

---

## 9. RECOMENDAÇÕES

### 9.1 Antes de Aprovar o Orçamento

1. **Abrir a planilha Excel gerada** para visualizar:
   - Valores calculados automaticamente (PAINEL)
   - Semáforos de alerta (ALERTAS)
   - Distribuição completa dos 18 macrogrupos (CUSTOS_MACROGRUPO)

2. **Validar o CUB:** Confirmar CUB SC mar/2026 oficial (estimado R$ 3.200/m²)

3. **Revisar briefing:** Ajustar respostas das 25 perguntas se necessário

4. **Solicitar quantitativos detalhados:**
   - Relatório TQS (concreto, forma, aço)
   - Elevações de fachada legíveis
   - Plantas hidrossanitárias completas (água fria, água quente, gás)

### 9.2 Para Orçamento Executivo

1. **Levantamento completo de quantitativos:**
   - Estrutura: volume concreto, área de forma, peso de aço (por TQS ou similar)
   - Fachada: medição direta nas elevações, quadro de esquadrias completo
   - Instalações: plantas completas de todas as disciplinas

2. **Composições de custo:**
   - Cotar fornecedores locais (Itajaí/região)
   - Aplicar produtividades reais da construtora
   - Incluir BDI específico do projeto

3. **Planejamento executivo:**
   - Cronograma físico-financeiro detalhado
   - Curva ABC de insumos
   - Plano de mobilização e logística (centro urbano)

---

## 10. ARQUIVOS GERADOS

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| **Planilha Excel** | `~/orcamentos/projetos/cambert-now/NOW-Residence-Orcamento-Parametrico.xlsx` | 14 abas com cálculos completos |
| **Memória de Cálculo** | `~/orcamentos/projetos/cambert-now/now-residence-memoria.md` | Este documento |
| **Script Gerador** | `~/orcamentos/projetos/cambert-now/gerar_now_residence.py` | Script Python para regenerar planilha |
| **Quantitativos Estruturais** | `~/orcamentos/projetos/cambert-now/quantitativos-estrutural.md` | Análise do IFC estrutural |
| **Quantitativos Fachada** | `~/orcamentos/projetos/cambert-now/quantitativos-fachada.md` | Extração de revestimentos e esquadrias |
| **Quantitativos Instalações** | `~/orcamentos/projetos/cambert-now/quantitativos-instalacoes.md` | Análise do IFC elétrico + índices paramétricos |
| **Dados Gerais** | `~/orcamentos/projetos/cambert-now/NOW-RESIDENCE-DADOS.md` | Resumo do projeto |

---

## 11. CONTATO

**Responsável Técnico:**  
Cartesian Engenharia  
Leonardo Kock Adriano — Engenheiro Civil  
leonardo@cartesianengenharia.com  
www.cartesianengenharia.com  

**Data da Emissão:** 11/03/2026  
**Revisão:** R00  

---

**⚠️ AVISO LEGAL:**

Este orçamento paramétrico é uma **estimativa preliminar** baseada em dados históricos de 75 projetos reais da base Cartesian Engenharia. Os valores apresentados possuem margem de variação de ±15-20% e **não substituem um orçamento executivo detalhado**.

Os custos finais da obra podem variar significativamente em função de:
- Condições de mercado (fornecedores, sazonalidade)
- Especificações técnicas detalhadas
- Condições do terreno (sondagem, nível d'água)
- Logística de obra (acessos, restrições de horário)
- Produtividade da equipe contratada
- Eventos imprevistos (chuvas, greves, falta de insumos)

**Recomenda-se a elaboração de orçamento executivo completo antes de qualquer decisão de investimento.**
