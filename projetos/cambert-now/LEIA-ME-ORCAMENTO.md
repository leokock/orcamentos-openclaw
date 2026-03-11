# Orçamento Executivo - NOW Residence

**Cliente:** Belli Empreendimentos Ltda.  
**Projeto:** NOW Residence  
**Localização:** Rua Luiz Berlim, 123, Centro, Itajaí/SC  
**Data-base:** mar/2026  
**Elaboração:** 11/03/2026

---

## 📊 Resumo Executivo

| Indicador | Valor |
|-----------|-------|
| **Custo Total Estimado** | **R$ 58.359.617,47** |
| **Área Construída Total** | 13.054 m² |
| **Custo por m²** | **R$ 4.470,63/m²** |
| **Custo por Unidade** | R$ 422.895,78/un |
| **CUB-SC (mar/2026)** | R$ 3.150,00/m² |
| **CUB Ratio** | **1,42** |

### Dados do Empreendimento

- **Unidades Residenciais:** 136 apartamentos
- **Unidades Comerciais:** 2 salas (térreo)
- **Pavimentos:** 24 (3 garagens + térreo + lazer + 17 tipos + ático + cobertura)
- **Elevadores:** 3 unidades
- **Vagas de Garagem:** 110
- **Prazo Estimado:** 36 meses

---

## 📁 Estrutura da Planilha

A planilha **`orcamento-executivo-now.xlsx`** contém **5 abas principais**:

### 1. RESUMO EXECUTIVO
- Dados do empreendimento
- Indicadores de custo (R$ total, R$/m², CUB ratio)
- Custo por macrogrupo (18 macrogrupos)
- Gráfico de distribuição (quando visualizado no Excel)

### 2. ORÇAMENTO DETALHADO
- Estrutura hierárquica N1 → N2 → N3 → N4
- 18 macrogrupos completos
- Colunas: Código | Descrição | Un | Qtd | R$ Unit | Total Mat | Total MO | Total | % Total
- Fórmulas ativas do Excel (não valores estáticos)
- Formatação profissional (headers escuros, zebra striping)
- Congelamento de painéis

### 3. CURVA ABC
- Itens ordenados por valor decrescente
- % individual e % acumulado
- Classificação A/B/C (70%-90%-100%)
- Top 20 itens de maior impacto

### 4. CRONOGRAMA FÍSICO-FINANCEIRO
- Meses 1 a 36 (colunas)
- 18 macrogrupos (linhas)
- Estrutura pronta para preenchimento da distribuição mensal
- Totais mensais e % acumulado

### 5. BDI (Bonificações e Despesas Indiretas)
- Composição detalhada do BDI
- 9 componentes (Admin, Lucro, Impostos, etc.)
- BDI composto (fórmula multiplicativa)
- Referência: Acórdão TCU nº 2622/2013

---

## 💰 Distribuição de Custos por Macrogrupo

| # | Macrogrupo | Valor (R$) | % Total | R$/m² |
|---|------------|------------|---------|-------|
| 1 | Supraestrutura | R$ 10.660.385,93 | 18,3% | R$ 816,64 |
| 2 | Gerenciamento | R$ 6.135.118,92 | 10,5% | R$ 469,98 |
| 3 | Infraestrutura | R$ 5.985.244,38 | 10,3% | R$ 458,50 |
| 4 | Instalações | R$ 5.458.587,54 | 9,4% | R$ 418,15 |
| 5 | Complementares | R$ 4.730.035,31 | 8,1% | R$ 362,34 |
| 6 | Esquadrias | R$ 4.537.309,32 | 7,8% | R$ 347,58 |
| 7 | Alvenaria | R$ 2.876.618,60 | 4,9% | R$ 220,36 |
| 8 | Sistemas Especiais | R$ 2.796.003,62 | 4,8% | R$ 214,19 |
| 9 | Pisos | R$ 2.714.448,76 | 4,7% | R$ 207,94 |
| 10 | Fachada | R$ 2.504.292,41 | 4,3% | R$ 191,84 |
| 11 | Rev. Int. Parede | R$ 2.403.763,56 | 4,1% | R$ 184,14 |
| 12 | Pintura | R$ 1.939.824,40 | 3,3% | R$ 148,60 |
| 13 | Impermeabilização | R$ 1.596.047,31 | 2,7% | R$ 122,26 |
| 14 | Movimentação de Terra | R$ 1.200.968,00 | 2,1% | R$ 92,00 |
| 15 | Teto | R$ 916.912,96 | 1,6% | R$ 70,24 |
| 16 | Climatização | R$ 760.917,66 | 1,3% | R$ 58,29 |
| 17 | Imprevistos | R$ 752.693,64 | 1,3% | R$ 57,66 |
| 18 | Louças e Metais | R$ 390.445,14 | 0,7% | R$ 29,91 |

**TOTAL:** R$ 58.359.617,47 | 100,0%

---

## ⚠️ Observações Importantes

### Premissas de Preços Unitários

1. **Base:** SINAPI SC (mar/2026) — valores estimados
2. **Para itens sem referência:** preços de mercado Itajaí/SC padrão alto
3. **Cross-check:** Orçamento paramétrico (~R$ 58,4 M)

### Status dos Quantitativos

✅ **Disponíveis:**
- Fachada (quantitativos extraídos do projeto)
- Instalações (estimativa baseada em PDFs de projeto)
- Memorial descritivo (especificações completas)

⚠️ **Estimativas paramétricas:**
- Estruturais (IFC sem quantidades — 2.350 m³ concreto, 15.650 m² formas, 200 ton aço)
- Usar relatórios nativos do TQS quando disponíveis

### Valores Críticos (Acima da Faixa Esperada)

Os seguintes macrogrupos estão **acima da faixa P90 do benchmark** devido às características do projeto:

1. **Infraestrutura (R$ 458,50/m²)** — 3 subsolos + cortina de estacas
2. **Movimentação de Terra (R$ 92,00/m²)** — 3 subsolos em centro urbano
3. **Impermeabilização (R$ 122,26/m²)** — 3 níveis de subsolo

Esses valores são coerentes com a complexidade do empreendimento.

---

## 📋 Próximos Passos Recomendados

### 1. Validação de Quantitativos

- [ ] Solicitar relatório de quantitativos do TQS (concreto, formas, aço)
- [ ] Validar quantitativos de fachada com elevações
- [ ] Conferir quantitativos de instalações com projetos executivos completos

### 2. Cronograma Físico-Financeiro

- [ ] Preencher distribuição mensal dos macrogrupos (aba CRONOGRAMA)
- [ ] Definir marcos principais (fundação, estrutura, vedação, acabamento)
- [ ] Ajustar curva S de desembolso

### 3. Detalhamento de Itens

- [ ] Completar aba ORÇAMENTO DETALHADO com todos os itens de cada macrogrupo
- [ ] Adicionar composições de custos detalhadas
- [ ] Incluir códigos SINAPI/ORSE

### 4. Curva ABC

- [ ] Atualizar aba CURVA ABC com todos os itens do orçamento detalhado
- [ ] Identificar itens classe A para negociação prioritária
- [ ] Estratégia de compras para itens de alto impacto

### 5. Revisão Final

- [ ] Revisão por engenheiro de custos sênior
- [ ] Validação com orçamentista externo (se aplicável)
- [ ] Aprovação do cliente

---

## 🔧 Metodologia Utilizada

### Base de Cálculo

- **Orçamento paramétrico:** Base calibrada com 75 projetos reais (Cartesian)
- **Fator CUB:** CUB Atual / CUB Base = 3.150 / 3.150 = 1,00
- **Fator Briefing:** Aplicado conforme características do projeto (fundação, padrão, lazer, etc.)

### Rateio Material x Mão de Obra

- **Material:** 40% do custo total do item
- **Mão de Obra:** 60% do custo total do item

Essa proporção é típica para obras de incorporação residencial vertical de médio/alto padrão.

### BDI Aplicável

| Item | % |
|------|---|
| Administração Central | 8,50% |
| Garantias e Seguros | 1,20% |
| Riscos e Imprevistos | 1,50% |
| Lucro | 10,00% |
| Despesas Financeiras | 1,80% |
| ISS (5%) | 5,00% |
| COFINS (3%) | 3,00% |
| PIS (0,65%) | 0,65% |
| CPRB (4,5%) | 4,50% |
| **BDI Composto** | **~41,5%** |

**Importante:** BDI calculado pelo método composto (multiplicativo), conforme recomendação do TCU.

---

## 📞 Contato

**Cartesian Engenharia**  
Leonardo Kock Adriano  
Engenheiro Civil  
leonardo@cartesianengenharia.com  
www.cartesianengenharia.com

---

*Documento gerado automaticamente em: 11/03/2026*  
*Revisão: R00*
