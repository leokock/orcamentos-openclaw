# Workflow: Geração de Orçamento Executivo a partir de Projetos

> Processo faseado para gerar orçamento executivo do zero, a partir de PDFs de projeto (arquitetônico, estrutural, instalações).
> Criado: 10/03/2026 | Autor: Jarvis + Leo
> Testado em: Residencial Estoril (Fonseca Neto) — comparativo com executivo real R$ 44,4M

---

## VISÃO GERAL

**Input:** PDFs de projeto (Drive ou Slack) + EAP-BASE
**Output:** Planilha de orçamento executivo + memorial de briefing com rastreabilidade completa

**Princípio:** Cada disciplina é processada em sub-agente isolado para evitar overflow de contexto. Resultados intermediários ficam em arquivos markdown. A consolidação final trabalha com dados estruturados, não PDFs brutos.

---

## PRÉ-REQUISITOS

- [ ] Acesso aos PDFs de projeto (Drive API ou upload direto)
- [ ] EAP-BASE.md validada (estrutura de referência dos macrogrupos)
- [ ] Memorial de briefing do projeto criado (TEMPLATE-MEMORIA-PROJETO.md)
- [ ] Pasta do projeto criada: `orcamento-parametrico/projetos/<nome-projeto>/`

---

## ESTRUTURA DE PASTAS

```
orcamento-parametrico/projetos/<nome-projeto>/
├── briefing.md                    # Memorial completo (rastreabilidade, versões, decisões)
├── pdfs/                          # PDFs baixados do Drive (organizados por disciplina)
│   ├── arquitetonico/
│   ├── estrutural/
│   ├── hidro/
│   ├── sanitario/
│   ├── eletrico/
│   ├── ppci/
│   └── especificos/
├── extracoes/                     # Output de cada fase (markdown estruturado)
│   ├── 01-arquitetonico.md
│   ├── 02-estrutural.md
│   ├── 03-instalacoes.md
│   ├── 04-especificos.md
│   └── 05-consolidado.md
├── planilha/                      # Planilha(s) gerada(s)
│   └── <nome>-executivo-v1.xlsx
└── comparativo/                   # Comparativo com executivo real (quando disponível)
    └── analise-comparativa.md
```

---

## FASES

### Fase 0 — Setup e Inventário
**Executor:** Sessão principal
**Tempo estimado:** 5 min

1. Criar pasta do projeto (`projetos/<nome>/`)
2. Acessar Drive via API e listar todos os arquivos disponíveis
3. Criar `briefing.md` a partir do `TEMPLATE-MEMORIA-PROJETO.md`
4. Registrar inventário de documentos recebidos no briefing
5. Validar EAP contra EAP-BASE.md

**Output:** briefing.md com seção 2 (Documentos Recebidos) preenchida

---

### Fase 1 — Extração Arquitetônica
**Executor:** Sub-agente isolado
**Input:** PDFs arquitetônicos (plantas, cortes, fachadas)
**Timeout:** 600s (10 min)

**O que extrair:**
- Quadro de áreas (AC, AT, área por pavimento)
- Nº de unidades, tipologias, mix de apartamentos
- Nº de pavimentos (total, tipo, garagem, subsolo)
- Nº de vagas
- Nº de elevadores
- Especificações visíveis (tipo de esquadria, acabamentos indicados)
- Dimensões de fachada (para estimar revestimento)
- Áreas de lazer e áreas comuns
- Pé-direito por pavimento (quando indicado nos cortes)

**Output:** `extracoes/01-arquitetonico.md` — dados estruturados com fonte (nome do PDF + prancha)

**Atualizar:** briefing.md seções 2 e 3

---

### Fase 2 — Extração Estrutural
**Executor:** Sub-agente isolado
**Input:** PDFs estruturais (fundação, embasamento, formas, armação)
**Timeout:** 600s

**O que extrair:**
- Tipo de fundação (estacas, sapatas, radier)
- Metragem/profundidade de estacas
- Volume de concreto por elemento (blocos, pilares, vigas, lajes)
- Tipo de laje (maciça, protendida, cubetas, alveolar)
- fck indicado
- Áreas de forma por pavimento
- Contenções (cortina, tirante, etc.)
- Especificações de aço (CA-50, CA-60, telas)

**Output:** `extracoes/02-estrutural.md`

**Atualizar:** briefing.md seção 4 (premissas de laje, fundação, contenção)

---

### Fase 3 — Extração de Instalações
**Executor:** Sub-agente isolado
**Input:** PDFs de Hidro, Sanitário, Elétrico, PPCI, Gás
**Timeout:** 600s

**O que extrair por disciplina:**
- **Hidráulica:** pontos de água fria/quente, diâmetros, tipo de aquecimento, reservatórios
- **Sanitário:** pontos de esgoto, caixas de inspeção, diâmetros
- **Elétrico:** quadros, circuitos, pontos de luz/tomada, alimentadores, gerador
- **PPCI:** sprinklers (qtd), hidrantes, detecção, alarme, tipo de sistema
- **Gás (se disponível):** pontos, tipo de gás, central

**Output:** `extracoes/03-instalacoes.md`

---

### Fase 4 — Extração de Específicos
**Executor:** Sub-agente isolado
**Input:** PDFs de Climatização, SPDA, Automação, Comunicação, Drenagem, etc.
**Timeout:** 600s

**O que extrair:**
- **Climatização:** nº de pontos de AC, tipo (split, VRF), infra prevista
- **SPDA:** tipo de sistema, captores
- **Automação:** escopo (portões, iluminação, CFTV)
- **Comunicação/Telecom:** tipo de cabeamento, CFTV, interfonia
- **Drenagem:** extensão, caixas
- **Interiores:** especificações de acabamento detalhadas

**Output:** `extracoes/04-especificos.md`

---

### Fase 5 — Consolidação e Geração da Planilha
**Executor:** Sub-agente isolado (contexto limpo)
**Input:** Os 4 arquivos de extração + EAP-BASE.md + briefing.md + base paramétrica
**Timeout:** 900s (15 min)

**Processo:**
1. Ler os 4 arquivos de extração (dados já estruturados — leve)
2. Cruzar com EAP-BASE.md (estrutura dos macrogrupos)
3. Para cada item da EAP:
   - Usar quantitativo extraído dos projetos (quando disponível)
   - Aplicar preço unitário da base de referência (SINAPI/TCPO/base CTN)
   - Quando quantitativo não disponível, estimar via índice paramétrico (R$/m² AC)
4. Gerar planilha executiva (.xlsx) com:
   - Aba resumo (18 macrogrupos)
   - Abas por disciplina (itens detalhados)
   - Indicadores (R$/m², CUB ratio, % por macrogrupo)
5. Registrar premissas e fontes no briefing.md

**Output:**
- `planilha/<nome>-executivo-v1.xlsx`
- `extracoes/05-consolidado.md` (resumo numérico)
- briefing.md atualizado (seções 5, 6, 8)

---

### Fase 6 — Comparativo (quando há executivo real)
**Executor:** Sessão principal ou sub-agente
**Input:** Planilha gerada + executivo real

**Processo:**
1. Comparar macrogrupo a macrogrupo (R$ e %)
2. Identificar desvios > 10%
3. Analisar causas dos desvios
4. Documentar aprendizados para calibrar o processo

**Output:** `comparativo/analise-comparativa.md`

---

## TEMPLATE DA PLANILHA

**Template base:** `orcamento-parametrico/TEMPLATE-Orcamento-Executivo.xlsx` (12 abas)
**Localização:** raiz do `orcamento-parametrico/` (genérico, sem dados de projeto específico na CAPA)

### Abas do Template

| # | Aba | Tipo | Descrição |
|---|-----|------|-----------|
| 1 | Reuniões | Dinâmica | Especificações, prazos, status extraídos de reuniões (MongoDB) |
| 2 | CAPA | Obrigatória | Dados do projeto, incorporador, responsáveis |
| 3 | Quadro de Áreas | Obrigatória | AC, áreas por pavimento, vagas |
| 4 | Mapa de Projetos | Obrigatória | Disciplinas recebidas, revisões, responsáveis |
| 6 | Fundações | Condicional | Estacas, blocos, aço — quando há dados estruturais |
| 7 | Climatização | Condicional | Splits, tubulação, caixas polares — quando há projeto AVAC |
| 8 | PPCI | Condicional | Hidrantes, alarme, PCF, bombas |
| 9 | SPDA | Condicional | Captação, descidas, equalização |
| 10 | ECTAS | Condicional | Estação de tratamento — quando aplicável |
| 11 | Drenagem | Condicional | Geodrenos, tubulação |
| 12 | Gás GLP | Condicional | Medidores, tubulação, churrasqueiras |
| 13 | Instalações (Resumo) | Obrigatória | Consolidado de todas as instalações |

### Regra de Flexibilidade

**A planilha NÃO é fixa.** O template define a estrutura *mínima*, mas:

1. **Adicionar abas:** Se a análise dos projetos revelar dados não previstos no template (ex: quantitativo BIM detalhado de alvenaria, esquadrias com especificação completa, paisagismo, piscinas), criar novas abas com os dados disponíveis
2. **Expandir abas existentes:** Se uma disciplina tiver mais detalhes do que o template prevê, adicionar seções dentro da aba existente
3. **Remover abas condicionais:** Se o projeto não tem determinada disciplina (ex: sem ECTAS, sem SPDA), não incluir a aba vazia
4. **Sempre documentar:** Cada aba nova ou seção expandida deve ter rastreabilidade (fonte, confiança, data)

**Princípio:** A planilha se adapta ao projeto, não o contrário. Mais dados = planilha mais rica.

---

## REGRAS IMPORTANTES

### Context Hygiene
- *Uma disciplina por sub-agente* — nunca misturar arquitetônico com estrutural no mesmo contexto
- *PDF → Markdown → Planilha* — o PDF nunca vai direto pra consolidação
- *Timeout mínimo 600s* para fases de extração (PDFs pesados)
- Se uma fase falhar, recomeçar só ela (outputs anteriores estão em arquivo)

### Rastreabilidade
- *Toda decisão vai pro briefing.md* (seção 6 — Decisões e Ajustes)
- *Toda premissa tem fonte* (qual PDF, qual prancha, qual página)
- *Toda versão é registrada* (seção 5 — Histórico de Versões)
- Quando não há dado do projeto, registrar "estimado via índice paramétrico" + qual índice

### Qualidade
- Antes de gerar planilha, validar totais (R$/m² total deve estar na faixa esperada para o padrão)
- CUB ratio como sanity check (tipicamente 1.0–1.5 para residencial vertical)
- Comparar distribuição % dos macrogrupos com base histórica (alertar desvios > 5pp)

---

## CHECKLIST RÁPIDO

- [ ] Fase 0: Pasta criada, briefing.md iniciado, inventário de documentos
- [ ] Fase 1: Extração arquitetônica concluída
- [ ] Fase 2: Extração estrutural concluída
- [ ] Fase 3: Extração instalações concluída
- [ ] Fase 4: Extração específicos concluída
- [ ] Fase 5: Consolidação e planilha gerada
- [ ] Fase 6: Comparativo (se aplicável)
- [ ] briefing.md completo e atualizado
- [ ] Planilha revisada pelo Leo

---

*Workflow v1.0 — 10/03/2026*
*Referências: FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md, TEMPLATE-MEMORIA-PROJETO.md, EAP-BASE.md*
