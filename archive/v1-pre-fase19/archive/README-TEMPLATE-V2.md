# Template de Orçamento Paramétrico v2 - Briefing Dinâmico

## 📋 Visão Geral

Sistema de orçamento paramétrico com briefing interativo que atualiza automaticamente os custos através de dropdowns selecionáveis.

**Arquivos gerados:**
- `rozzo-vd-parametrico-v2.xlsx` — Versão pré-preenchida com dados do Edifício Rozzo
- `template-orcamento-parametrico-v2.xlsx` — Template limpo para novos projetos
- `gerar_template_dinamico.py` — Script Python para gerar novas versões

## 🎯 Modelo de Cálculo

```
Valor Final (R$/m²) = Base × Fator CUB × Fator Briefing Composto
```

**Onde:**
- **Base** = Mediana calibrada do macrogrupo (dez/2023)
- **Fator CUB** = CUB Atual / CUB Base (ajuste de inflação)
- **Fator Briefing Composto** = Produto de todos os 25 fatores do briefing

## 📊 Estrutura da Planilha

### 1. DADOS_PROJETO
- Inputs do projeto (AC, UR, UC, NP, etc.)
- CUB Atual e CUB Base
- Layout 2 colunas
- Células em azul claro = inputs editáveis

### 2. BRIEFING (⚠️ Aba destacada em laranja)
- 25 perguntas com dropdowns (Data Validation)
- Coluna C = resposta selecionável
- Coluna D = macrogrupos afetados
- Respostas ficam em C2:C26 (Q1=C2, Q25=C26)

### 3. FATORES
- Matriz 18 linhas (macrogrupos) × 25 colunas (perguntas)
- Cada célula = fórmula IFS que lê o dropdown do BRIEFING
- Última coluna (AA) = `=PRODUCT(B:Z)` = Fator Briefing Composto
- Cores: azul (<1), laranja (>1), cinza (=1)

### 4. CUSTOS_MACROGRUPO
- Cálculo final por macrogrupo
- Todas as colunas usam fórmulas (não valores estáticos)
- Colunas: #, Macrogrupo, Base R$/m², Fator CUB, Fator Briefing, R$/m² Ajustado, Valor Total, %, Faixa Min, Faixa Max, Status

### 5. PAINEL
- Dashboard com KPIs calculados por fórmula
- Custo Total, Custo/m², Custo/Unidade
- Top 3 Macrogrupos (por % do custo total)

### 6. ALERTAS
- Semáforo automático por macrogrupo
- ✓ = dentro da faixa P10-P90
- ⚠ = fora da faixa, mas dentro de ±20%
- ✗ = >20% fora da faixa (revisar premissas)

### 7. NOTAS
- Premissas, limitações e instruções de uso

## 🔧 Como Usar

1. **Preencher DADOS_PROJETO** com informações do empreendimento
2. **Responder BRIEFING** (usar os dropdowns em cada pergunta)
3. **Verificar CUSTOS_MACROGRUPO** (atualiza automaticamente)
4. **Analisar ALERTAS** para validar se os valores estão coerentes
5. **Consultar PAINEL** para visualização rápida dos KPIs

## 📐 Briefing - 25 Perguntas

### Fundação e Estrutura
- Q1: Tipo de Fundação (5 opções) → afeta Infraestrutura
- Q2: Tipo de Laje (5 opções) → afeta Supraestrutura
- Q3: Contenção (5 opções) → afeta Infraestrutura
- Q4: Subsolos (4 opções) → afeta Mov.Terra, Infraestrutura, Impermeabilização

### Acabamentos
- Q5: Padrão (5 níveis) → afeta 7 macrogrupos (Rev.Int., Teto, Pisos, Pintura, Esquadrias, Fachada, Complementares)
- Q6: Esquadria (4 opções) → afeta Esquadrias
- Q7: Piso (5 opções) → afeta Pisos
- Q8: Vedação (3 opções) → afeta Alvenaria
- Q9: Forro (5 opções) → afeta Teto
- Q10: Fachada (5 opções) → afeta Fachada
- Q11: MO Fachada (2 opções) → afeta Fachada

### Instalações e Sistemas
- Q12: Cobertura Habitável (3 opções) → afeta Complementares
- Q13: Aquecimento (5 opções) → afeta Instalações
- Q14: Automação (4 opções) → afeta Sist. Especiais
- Q15: Energia (3 opções) → afeta Sist. Especiais
- Q21: Gerador (Sim/Não) → afeta Sist. Especiais
- Q22: Subestação (Sim/Não) → afeta Sist. Especiais
- Q23: Fotovoltaicas (Sim/Não) → afeta Sist. Especiais
- Q24: Carro Elétrico (Sim/Não) → afeta Instalações
- Q25: Pressurização (Sim/Não) → afeta Instalações

### Áreas Comuns
- Q16: Lazer (3 opções) → afeta Complementares
- Q17: Paisagismo (4 opções) → afeta Complementares
- Q18: Mobiliário (4 opções) → afeta Complementares

### Contexto
- Q19: Prazo (6 opções: 18 a 48 meses) → afeta Gerenciamento
- Q20: Região (5 opções) → afeta TODOS os macrogrupos

## 📈 Base de Calibração

- **18 projetos reais** executados entre 2022-2024
- **CUB base:** R$ 2.752,67 (dez/2023)
- **Medianas calibradas** (R$/m²):
  - Gerenciamento: 407,07
  - Supraestrutura: 722,66
  - Instalações: 366,96
  - Esquadrias: 367,23
  - (...)

## 🔬 Fórmulas IFS

Cada célula da matriz FATORES usa fórmulas IFS do Excel:

```excel
=IFS(
  BRIEFING!$C$2="Hélice Contínua", 1.0,
  BRIEFING!$C$2="Estaca Franki", 0.9,
  BRIEFING!$C$2="Tubulão", 1.15,
  BRIEFING!$C$2="Sapata/Radier", 0.75,
  BRIEFING!$C$2="Estaca raiz", 1.10,
  TRUE, 1
)
```

**Características:**
- Referenciam sempre as células absolutas ($C$2 a $C$26)
- Cobrem TODAS as opções do dropdown
- Fallback `TRUE, 1` no final
- Retornam `=1` para perguntas que não afetam o macrogrupo

## 🛠️ Manutenção

Para regerar ou modificar as planilhas:

```bash
cd ~/clawd/orcamento-parametrico
python3.11 gerar_template_dinamico.py
```

O script gera automaticamente:
1. Versão pré-preenchida com dados do Rozzo
2. Versão template limpa

## ⚠️ Limitações

- Estimativa preliminar (não substitui orçamento executivo)
- Não inclui: terreno, projetos, aprovações, marketing, impostos
- Climatização e Louças/Metais são placeholders (valor 0)
- Faixas podem variar conforme região e características específicas

## 📞 Contato

**Cartesian Engenharia**  
leonardo@cartesianengenharia.com  
www.cartesianengenharia.com

---

_Gerado em: 05/mar/2026_  
_Versão: 2.0_
