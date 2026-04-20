---
projeto: Arthen Arboris
inspiracao: CTN-ALF-SFL — Orçamento Paramétrico (Amalfi San Felice)
data_analise: 2026-04-20
proposito: Mapear a estrutura da apresentação San Felice pra replicar pro Arboris
---

# Estrutura da Apresentação — Arboris (baseada em CTN-ALF-SFL)

## Visão geral

Apresentação **20 slides**, formato institucional Cartesian (azul Cartesian + cinza claro + laranja acento). Fluxo: capa → dados → totais → composição → especificações → benchmarks → tipologia/área priv. → planejamento → curvas → entregáveis.

---

## Slide 1 — Capa Cartesian
- Fundo claro com linhas gráficas Cartesian
- Logo Cartesian centralizado
- **Template reutilizável — mesma capa**

## Slide 2 — Capa do projeto
- **Esquerda:** título "Orçamento Paramétrico" + nome do empreendimento grande (SAN FELICE) + cliente (AMALFI EMPREENDIMENTOS) + metadados (cidade, data-base, CUB)
- **Direita:** render 3D do edifício
- **Adaptar:** "ARBORIS" + "ARTHEN EMPREENDIMENTOS" + "Itajaí/SC | Data-base: Março/2026 | CUB/SC: R$ 3.028,45/m²"

## Slide 3 — Jornada da Reunião (índice)
Lista numerada 01–06 dos blocos temáticos:
1. Dados e Premissas do Projeto
2. Visão Geral do Orçamento
3. Composição por Macrogrupo
4. Especificações
5. Obras de Referência
6. Análise de Custo por Área Privativa

## Slide 4 — Características do Empreendimento
Tabela azul escuro com linhas alternadas + render 3D à direita

**Campos (adaptados para Arboris):**
| Campo | San Felice | **Arboris** |
|---|---|---|
| Área Construída | 7.648,96 m² | **12.472,98 m²** |
| Unid. Residenciais/Comerciais | 54 un. | **98 un.** |
| Pavimentos (tipo) | 13 (8 tipo) | **24 (19 tipo)** |
| Elevadores | 2 | **2** |
| Área Privativa | 4.100,48 m² | **— obter** |
| Área Terreno | 968,52 m² | **— obter** |
| Prazo | 38 meses | **30 meses** |
| Ambientes Lazer | 7 | **— obter** |

## Slide 5 — Visão Geral do Orçamento
4 cards 2×2 com ícones + valores grandes em laranja:

| Card | San Felice | **Arboris (v3)** |
|---|---|---|
| Custo Total | R$ 26,6 Mi | **R$ 45,5 Mi** |
| Custo por m² | R$ 3.485/m² | **R$ 3.645/m²** |
| Custo por Unidade | R$ 494 mil | **R$ 494 mil** (coincidência!) |
| Fator CUB/SC | 1,15 CUB | **1,20 CUB** |

## Slide 6 — Detalhamento do Custo (tabela completa)
Tabela com 4 colunas: Etapa | Valor Orçado | % | Valor/m²

Todas as etapas do orçamento (15-17 linhas) + linha TOTAL destacada em azul.

**Para Arboris:** reaproveitar tabela CUSTOS_MACROGRUPO do v3 com as 18 linhas + TOTAL.

## Slide 7 — Composição do Orçamento (barras + TOP 3)
- **Esquerda:** gráfico de barras horizontais dos 10 maiores macrogrupos (valores em %)
- **Direita:** 3 cards verticais com TOP 3 macrogrupos, cada um com %, valor em Mi e 1-linha de justificativa

**Para Arboris — TOP 3 provável (após ajustes):**
1. **Supraestrutura 21,6%** — R$ 9,8 Mi — *Laje convencional em torre de 24 pavimentos*
2. **Instalações 10,8%** — R$ 4,9 Mi — *Elétrica, hidro, PPCI, gás, telecom — 3-4 dorm. c/ 2 BWCs*
3. **Gerenciamento 10,2%** — R$ 4,6 Mi — *30 meses de obra*
(ou, após ajustar elevadores, **Sist. Especiais** sobe)

## Slides 8-11 — Especificações (4 slides agrupados)

Cada slide com ~3-4 macrogrupos, padrão:
- **Título "ESPECIFICAÇÕES"**
- Bloco por macrogrupo: nome + % + valor total + valor/m², seguido de 2-3 bullets com especificações técnicas

**Ordem de apresentação San Felice (por ordem de grandeza):**
- Slide 8: Supraestrutura, Gerenciamento, Instalações, Esquadrias
- Slide 9: Alvenaria, Complementares, Infraestrutura, Rev. Parede
- Slide 10: Pisos, Fachada, Sistemas Especiais
- Slide 11: Pintura, Rev. Teto, Impermeab., Mov. Terra

**Para Arboris — exemplo do bullet de SUPRAESTRUTURA:**
> **SUPRAESTRUTURA** — 21,6% — R$ 9,8 Mi | R$ 786/m²
> - Laje convencional maciça na torre (fck30)
> - Aço CA-50 em 106 kg/m² (consumo típico pé-direito 3,0m)
> - Inclui: concreto, formas, armação, escoramento e MO empreitada

## Slide 12 — Análise com Obras de Referência
Tabela 5 colunas: Etapa | Arboris R$/m² | Faixa Referência | Média Ref. | Variação

**Fonte de dados:** `calibration-condicional-padrao.json` Médio-Alto (n=37) — pegar P25–P75 como "faixa" e mediana como "média ref". Adicionar variação % à direita, com cores (verde se dentro, amarelo se atenção, vermelho se fora).

**Linha TOTAL (s/ ger.):** Arboris R$ 3.273 vs Faixa R$ 2.700–3.600 → **-3%** dentro.

## Slide 13 — Comparativo com Versão Anterior
Tabela 7 colunas × 16 linhas: Etapa | (Paramétrico novo: Valor | R$/m²) | (Preliminar anterior: Valor | Valor indexado | R$/m²) | (Diferença: Valor | R$/m²)

**Para Arboris:** comparar v3 (2026-04) vs v2 (2026-04-14 inicial, se houver diferença significativa) OU comparar com o **preliminar 2025** do Arboris (se o cliente teve uma versão anterior). Caso não exista versão anterior, **pular slide** ou reusar pra comparar **"paramétrico 2026 vs executivo DWG-PRÉ-EXECUTIVO 2025"** que já está na pasta do cliente.

> ⚠️ Verificar se há um `ARBORIS-PDF-PRÉ EXECUTIVO` no Drive — se sim, usar como versão anterior.

## Slide 14 — Comparação com Obras da Construtora
Tabela 4 colunas: Etapa | Obra A (destaque azul) | Obra B | Obra C

**Para Arboris** — obras Arthen com as quais comparar:
- O cliente Arthen não aparece com outros projetos no workspace atual. Duas opções:
  - **Opção A (análogos de mercado):** usar 2-3 projetos **Médio-Alto** da base Cartesian com AC e UR parecidos (ex: Tramonti, Ravello, NF Itajaí)
  - **Opção B (pedir dados ao cliente):** se Arthen tiver outros empreendimentos entregues, solicitar R$/m² indexado pra comparação

Sugestão imediata: **usar os 3 benchmarks Amalfi (SFL, Maiori, Marine)** que estão no PDF SFL — as três são obras de alto nível em cidade próxima (Navegantes vs Itajaí), mesmo CUB, padrão comparável. Mudar cabeçalho para "Comparação com obras de referência do litoral norte SC".

## Slide 15 — Análise de Custo por Área Privativa
- Tabela superior: Empreendimento | Área Privativa | R$/m² Priv.
- Gráfico de barras abaixo comparando os valores

**Exige dado:** área privativa do Arboris. Calcular a partir do IFC ou pedir ao cliente.

## Slide 16 — Custo por Tipologia de Unidade + Quadro de Áreas
Duas áreas no slide:
- **Superior:** tabela de tipologias com área privativa + custo estimado por unidade
- **Inferior:** quadro comparativo entre versões (ÁREA CONSTRUÍDA, PAVIMENTOS, UNIDADES, ÁREA PRIVATIVA, AP/AC, CUSTO/AP)

**Requer dados:** número de tipologias distintas do Arboris + área privativa de cada tipologia.

## Slide 17 — Planejamento Macro (cronograma visual)
Tabela tipo Gantt com linhas de macrogrupos × colunas de meses (M1 a M30 pro Arboris, vs M1–M38 do SFL).

**Células pintadas de azul** indicam o mês em que a etapa está ativa. Adicionar eventualmente um número dentro (ordem de entrada).

**Para Arboris:** 30 meses. Etapas a mapear:
- Mov. Terra (M1–M3)
- Infraestrutura (M2–M6)
- Supraestrutura (M5–M17 ≈ 13 meses: 19 pav tipo + ático + torre)
- Alvenaria (M8–M22)
- Instalações (M9–M24)
- Sist. Especiais + Elev. (M14–M25)
- Impermeab. (M12–M25)
- Rev. Piso+Parede (M14–M28)
- Rev. Teto (M15–M26)
- Pintura (M16–M30)
- Esquadrias (M18–M28)
- Fachada (M14–M27)
- Complementares (M26–M30)

Base pra curva: extrair do `curva-fisico-financeira.json` se o script gerar. Se não, distribuir manualmente conforme lógica acima.

## Slides 18–19 — Curva de Distribuição de Custos (duas variações)

**Slide 18:**
- **Superior:** gráfico de barras mês a mês com % do custo total em cada mês (ex: M16 = 4,66%)
- **Inferior:** gráfico de barras com valor absoluto em R$ por mês

**Slide 19:**
- **Superior:** gráfico linear da **curva acumulada em %** (S-curve)
- **Inferior:** gráfico linear da **curva acumulada em R$**

**Para Arboris:** exportar do script de curva física-financeira ou gerar no openpyxl a partir do planejamento macro.

## Slide 20 — Entregáveis (encerramento)
Lista numerada 01–03 + render 3D à direita:
01. Apresentação
02. Orçamento Analítico
03. Planejamento Macro e Distribuição Físico-Financeira

Footer azul com nome do projeto + construtora + local + mês.

**Para Arboris:** "ARBORIS — ORÇAMENTO PARAMÉTRICO | Arthen Empreendimentos | Itajaí/SC | Abril 2026"

---

## Template técnico da apresentação

### Paleta de cores (extraídas do PDF)
- **Azul Cartesian primário:** #1E52F5 (barras, títulos destacados)
- **Azul escuro navy:** #0F1C4A (tabelas, cabeçalhos)
- **Laranja acento:** #FF5722 (números grandes, destaques "R$ 26,6 Mi")
- **Cinza claro fundo:** #F4F6F8
- **Branco linhas alternadas:** #FFFFFF / #E8EEF4

### Tipografia
- Família sans-serif (provavelmente Poppins ou Inter)
- Títulos em **bold** e CAIXA ALTA
- Valores em bold
- Disclaimers em itálico cinza

### Componentes visuais recorrentes
- Barras laterais coloridas (azul/vermelho) antes de cada bloco
- Tabelas com cabeçalho azul + linhas alternadas cinza/branco
- Cards 2×2 com ícones (dinheiro, régua, casa, pizza) em branco sobre fundo azul
- Render 3D sempre à direita em slides de capa/tipologia/entregáveis
- Rodapé discreto com logo "Cartesian" no canto inferior direito

---

## Plano de execução sugerido

### Fase 1 — Coleta de dados faltantes (antes de gerar a apresentação)
1. **Área privativa total do Arboris** — extrair do IFC ou pedir pra Arthen
2. **Número de tipologias** e área privativa de cada — extrair do IFC
3. **Área terreno + ambientes de lazer** — checar projeto arquitetônico
4. **Definir se comparará com obras Arthen** ou com base Cartesian/Amalfi

### Fase 2 — Aplicar os ajustes de ANALISE-ERROS-v3.md ao paramétrico
Antes de gerar a apresentação, **rodar os ajustes pendentes** (elevadores, louças, imprevistos, climatização, complementares) pro paramétrico refletir os números que vão pro cliente.

### Fase 3 — Gerar a apresentação
Opções técnicas:
- **python-pptx** (skill `cartesian-presentation`) — padrão Cartesian já implementado
- **Gamma** — se quiser gerar com AI (menos controle, mais rápido)
- **Manual no Figma/PowerPoint** — máximo controle visual

Recomendação: **python-pptx via skill cartesian-presentation**, puxando os dados direto do xlsx paramétrico v3 (ou v4 após ajustes) — garante reprodutibilidade e consistência visual com o template Cartesian.

### Fase 4 — Entrega
Pasta final no Drive:
```
_Parametrico_IA/arthen-arboris/
  arthen-arboris-apresentacao-v1.pdf
  arthen-arboris-apresentacao-v1.pptx
  arthen-arboris-parametrico-v3-hibrido.xlsx (já existe)
  arthen-arboris-planejamento-macro.xlsx (gerar)
  arthen-arboris-curva-fisico-financeira.xlsx (gerar)
```

Após aprovação interna (Patricia / Leo), enviar no Drive compartilhado com Arthen.

---

## Anexo — Seções do PDF San Felice mapeadas por página

| Pág | Conteúdo | Reuso | Adaptação |
|---:|---|---|---|
| 1 | Capa Cartesian | 100% | — |
| 2 | Capa projeto + render + metadados | 100% | substituir texto + imagem |
| 3 | Jornada da reunião | 100% | texto igual |
| 4 | Características empreendimento | 90% | só números |
| 5 | Visão geral (4 cards) | 100% | números |
| 6 | Detalhamento do custo (tabela) | 100% | substituir tabela |
| 7 | Composição (barras + TOP 3) | 100% | números + justificativas |
| 8-11 | Especificações agrupadas | 100% | substituir bullets técnicos |
| 12 | Comparação obras de referência | 100% | usar base Cartesian Médio-Alto |
| 13 | Comparativo versão anterior | condicional | só se houver versão anterior |
| 14 | Comparação obras da construtora | condicional | usar Amalfi ou pedir Arthen |
| 15 | Custo por área privativa | 100% | requer AP |
| 16 | Tipologias + quadro áreas | 100% | requer tipologias |
| 17 | Planejamento macro | 100% | gerar novo cronograma |
| 18-19 | Curva distribuição custos | 100% | gerar novos gráficos |
| 20 | Entregáveis | 100% | só substituir footer |
