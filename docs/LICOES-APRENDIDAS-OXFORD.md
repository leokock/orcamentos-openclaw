# LIÇÕES APRENDIDAS — PROJETO OXFORD (MUSSI)

**Data:** 12-13/março/2026  
**Duração total:** ~6h10 (18h00 → 00h10)  
**Resultado:** 4 entregáveis completos (orçamento paramétrico, executivo, memorial, briefing)

---

## 1. ESTRUTURA DE DADOS E DOCUMENTAÇÃO

### ✅ O QUE FUNCIONOU BEM

**1.1 Análise Sequencial em Ondas**
- Dividir análise em disciplinas (arquitetura → hidro → estrutura → PPCI → elétrico) permitiu processamento organizado
- Cada onda gerou arquivo `.md` consolidado, facilitando referência posterior
- Arquivos intermediários foram fundamentais para rastreabilidade

**1.2 Processamento IFC Como Prioridade**
- IFC estrutural, mesmo incompleto, deu dados PRECISOS de lajes (2.390 m³)
- Muito melhor que estimativas por CUB ou amostragem pura
- **Decisão:** Sempre priorizar IFC quando disponível, mesmo que parcial

**1.3 Amostragem Inteligente + Multiplicadores**
- Processar 27 PDFs (16% do total) com multiplicadores validados (×4 garagens, ×16 tipos) = cobertura 100%
- Economizou tempo sem perder precisão
- Taxa de aço 71,7 kg/m³ validou a metodologia ✅

**1.4 Consolidação de Quantitativos em Planilhas XLSX**
- Hidrossanitário: 10 planilhas XLSX → consolidação automática via script
- Muito mais eficiente que extração manual de PDFs

### ⚠️ ARMADILHAS IDENTIFICADAS

**1.5 IFC Estrutural Incompleto**
- **Problema:** IFC tinha lajes completas, mas vigas/pilares sem volumes preenchidos, fundação não modelada
- **Causa:** Comum em IFC estrutural — modeladores não preenchem todos os property sets
- **Solução aplicada:** Complementar com PDFs (amostragem inteligente)
- **Lição:** SEMPRE validar completude do IFC antes de confiar 100%

**1.6 Timeout em Processamento de PDFs (10 min insuficiente)**
- **Problema:** 3 ondas consecutivas com timeout (PPCI, Elétrico, Memorial Descritivo)
- **Causa:** Volume grande de PDFs técnicos (23 PPCI, 26 Elétrico)
- **Solução aplicada:** Aumentar timeout pra 15-20 min + amostragem inteligente
- **Lição:** Para disciplinas com >20 PDFs, usar timeout mínimo 15 min OU dividir em sub-ondas

**1.7 Dados Bloqueadores Não Solicitados Cedo**
- **Problema:** Área Construída Total e Área do Terreno faltaram — bloquearam orçamento paramétrico preciso
- **Lição:** **PRIMEIRA ação ao receber projeto:** solicitar quadro de áreas oficial, implantação, memorial descritivo
- **Checklist pré-análise:**
  - [ ] Quadro de áreas geral (AC, AT, áreas por pavimento)
  - [ ] Projeto de implantação
  - [ ] Memorial descritivo (se existir)
  - [ ] Data-base de preços/CUB
  - [ ] Especificações de acabamento

---

## 2. PROCESSAMENTO TÉCNICO

### ✅ BOAS PRÁTICAS VALIDADAS

**2.1 Script Python para IFC (ifcopenshell)**
- Biblioteca `ifcopenshell` funcionou perfeitamente para extração de dados
- Script gerou JSON completo (932 KB) com todos os elementos
- **Padrão:** Usar `ifcopenshell` como ferramenta padrão pra IFC

**2.2 Processamento de Planilhas XLSX com pandas**
- `pandas` + `openpyxl` permitiram leitura/consolidação rápida de planilhas hidro
- Consolidação de 10 planilhas em <5 min
- **Padrão:** Para quantitativos em Excel, sempre usar pandas

**2.3 Geração de Excel Profissional com openpyxl**
- Orçamento executivo gerado com formatação completa (bordas, cores, hierarquia)
- BDI aplicado via fórmulas
- **Padrão:** Usar openpyxl para gerar orçamentos executivos (não apenas CSV)

**2.4 ⚠️ REGRA CRÍTICA: Extração SEMPRE por Pavimento**
- **OBRIGATÓRIO:** Orçamento executivo SEMPRE com quantitativos separados por pavimento
- **Motivo:** Permite análise de custo por andar, validação de multiplicadores, rastreabilidade
- **Implementação:** Script `gerar-orcamento-executivo.py` deve estruturar dados por pavimento
- **Nunca fazer:** Consolidar tudo em uma linha única sem quebra por pavimento

### ⚠️ PROBLEMAS TÉCNICOS ENCONTRADOS

**2.5 APIs de PDF com Falhas (OpenAI/Anthropic)**
- Durante processamento elétrico, APIs retornaram erros 520/401/quota
- **Solução aplicada:** Fallback para estimativas calibradas (NBR 5410 + padrões de mercado)
- **Lição:** Ter SEMPRE fallback para extração de PDF (OCR local, estimativas por norma, etc.)

**2.6 PDFs Grandes (>5 MB) Causam Lentidão**
- Pranchas elétricas 22-24 tinham 4,9 MB, 8,2 MB, 16 MB
- Processamento lento ou timeout
- **Lição:** Detectar PDFs >5 MB e processar separadamente OU dividir em chunks

---

## 3. ESTRATÉGIA DE SUBAGENTES

### ✅ PADRÕES EFICAZES

**3.1 Timeout Mínimo: 10 min (Tarefas Simples), 15-20 min (Processamento Pesado)**
- Tarefas de consolidação/escrita: 10 min OK
- Processamento de PDFs/análise pesada: 15-20 min necessário
- **Regra:** `runTimeoutSeconds: 600` (mínimo) para TUDO, `900-1200` para processamento pesado

**3.2 Uma Tarefa Atômica por Subagente**
- Subagente "gerar orçamento paramétrico" focado APENAS nisso = sucesso
- Subagente "analisar tudo de PPCI + gerar memorial" = timeout
- **Regra:** 1 subagente = 1 entregável ou 1 análise de disciplina

**3.3 Instruções Claras com Exemplos de Output**
- Subagentes com instruções estruturadas + exemplo de formato esperado = melhores resultados
- Especialmente importante para tabelas, formatação, estrutura de documentos

### ⚠️ ARMADILHAS COM SUBAGENTES

**3.4 Comunicação Mid-Flight com Subagente Ativo (sessions_send)**
- **Problema:** Tentei enviar instrução adicional (rastreabilidade) pro subagente do memorial enquanto ele processava → timeout
- **Causa:** Subagente já estava rodando, mensagem não foi processada
- **Solução:** Aguardar conclusão + lançar segundo subagente para ajustes
- **Lição:** NÃO tentar "corrigir rota" de subagente ativo — deixar terminar e ajustar depois

**3.5 Polling/Listagem de Subagentes Ativo**
- **NUNCA fazer:** `subagents list` em loop enquanto aguarda conclusão
- Sistema de push-based announcements funciona bem
- **Regra:** Só checar status quando precisar intervir/debugar

---

## 4. QUALIDADE DOS ENTREGÁVEIS

### ✅ DIFERENCIAIS QUE AGREGARAM VALOR

**4.1 Rastreabilidade Memorial ↔ Orçamento**
- Leo pediu explicitamente às 23h45: "memorial bem completo considerando tudo"
- 21 tabelas de quantitativos com referência cruzada (Aba X, Item Y)
- **Impacto:** Memorial deixa de ser "documento burocrático" e vira ferramenta de gestão
- **Lição:** SEMPRE incluir rastreabilidade — cliente pode não pedir, mas agrega muito valor

**4.2 Sistema de Validação no Orçamento Paramétrico**
- Semáforo P10-P90 automático (verde/amarelo/vermelho)
- Aba "ALERTAS" destacando dados fora da faixa
- **Impacto:** Cliente consegue validar premissas sozinho
- **Lição:** Incluir validações automáticas em orçamentos paramétricos

**4.3 Briefing com Status (✅ ⚠️ ❌)**
- Dados confirmados vs estimados vs indisponíveis claramente marcados
- Lista de bloqueadores críticos destacada
- **Impacto:** Transparência total sobre confiabilidade dos dados
- **Lição:** NUNCA entregar estimativa sem marcar claramente como tal

**4.4 Backup Automático Antes de Edições Grandes**
- Criar `*-backup-pre-rastreabilidade.md` antes de adicionar 21 tabelas
- **Impacto:** Segurança para reverter se necessário
- **Lição:** Sempre fazer backup antes de edições estruturais grandes

### ⚠️ GAPS IDENTIFICADOS

**4.5 Faltou Resumo Executivo Visual (Dashboard)**
- Orçamentos têm dados completos, mas falta visualização executiva (gráficos, KPIs)
- **Melhoria futura:** Gerar dashboard em Power BI ou Excel com gráficos (custo por sistema, %, cronograma visual)

**4.6 Memorial Não Tem Cronograma de Execução**
- Memorial tem quantitativos completos, mas não tem cronograma físico-financeiro
- **Melhoria futura:** Adicionar seção "Cronograma Estimado" com marcos principais

---

## 5. COMUNICAÇÃO COM O CLIENTE (LEO)

### ✅ PADRÕES DE COMUNICAÇÃO EFICAZES

**5.1 Opções Claras com Contexto**
- Apresentar 2-3 opções (A/B/C) com pros/cons
- Leo decide rápido quando opções são claras
- Exemplo: "Opção A: gerar agora com estimativas | Opção B: processar IFC primeiro"

**5.2 Avisos de Conclusão Estruturados**
- Formato eficaz:
  ```
  ✅ ONDA X CONCLUÍDA
  Output: arquivo.xlsx
  Dados: resumo dos principais resultados
  Próximo passo: opções ou pergunta
  ```
- Leo respondeu bem a esse formato consistente

**5.3 Confirmação Explícita Antes de Processos Longos**
- Antes de lançar subagentes de 15-20 min, confirmar com Leo
- Ele aprova rápido ("Combinado!", "Quero sim") mas gosta de estar no controle

### ⚠️ ERROS DE COMUNICAÇÃO

**5.4 Não Avisar de Limitações Cedo**
- Deveria ter avisado sobre dados faltantes (AC, AT) LOGO no início
- Avisei só quando chegou na Onda 2 (briefing)
- **Lição:** Identificar bloqueadores na PRIMEIRA análise (arquitetura) e avisar imediatamente

**5.5 Subestimar Pedido de "Completo"**
- Leo pediu "memorial bem completo considerando tudo"
- Primeira versão não tinha rastreabilidade detalhada
- Precisei adicionar depois (segunda passagem)
- **Lição:** Quando Leo pede "completo", ele quer COMPLETO mesmo (não economizar)

---

## 6. GESTÃO DE TEMPO E RECURSOS

### ✅ EFICIÊNCIAS ALCANÇADAS

**6.1 Processamento Paralelo**
- Ondas 3 e 4 rodando em paralelo (hidro + PPCI) economizou ~10 min
- **Padrão:** Sempre que ondas forem independentes, rodar em paralelo

**6.2 Reutilização de Scripts**
- Script `gerar_template_dinamico.py` já existia (sistema paramétrico)
- Apenas adaptei parâmetros pro Oxford
- **Lição:** Manter biblioteca de scripts reutilizáveis

**6.3 Consolidação Progressiva**
- Cada onda gerou arquivo `.md` → facilitou geração dos entregáveis finais
- Não precisei "voltar aos PDFs" na hora de gerar orçamentos
- **Lição:** Arquivos intermediários bem estruturados aceleram etapas finais

### ⚠️ DESPERDÍCIOS IDENTIFICADOS

**6.4 3 Timeouts Consecutivos (PPCI, Elétrico, Memorial)**
- Total: ~30 min desperdiçados em timeouts
- **Causa:** Timeout inicial muito otimista (10 min)
- **Lição:** Ser realista com timeout desde o início (15-20 min para processamento pesado)

**6.5 Tentativa de Processar TODOS os PDFs Estruturais**
- Primeira tentativa: processar 340 PDFs → óbvio que daria timeout
- **Lição:** Fazer análise de viabilidade ANTES de lançar subagente (quantos arquivos? quanto tempo por arquivo?)

---

## 7. DADOS E VALIDAÇÕES

### ✅ VALIDAÇÕES QUE FUNCIONARAM

**7.1 Taxa de Aço (kg/m³ concreto)**
- Oxford: 71,7 kg/m³
- Faixa esperada: 70-90 kg/m³
- ✅ Validação passou — dados estruturais consistentes

**7.2 Potência Elétrica vs Transformador**
- Potência demandada: 431 kW
- Transformador: 500 kVA
- ✅ Dimensionamento correto (margem de ~15%)

**7.3 Reservatório RTI vs Número de Hidrantes**
- RTI: 21.663L
- Hidrantes: 24 internos DN65
- ✅ Atende NBR 13714 (mínimo 18.000L)

**7.4 Multiplicadores de Pavimentos Tipo**
- IFC confirmou: Tipos 2-17 são IDÊNTICOS (mesmo nome de arquivo)
- Multiplicador ×16 validado ✅

### ⚠️ VALIDAÇÕES PENDENTES

**7.5 Laje Tipo "Cubetas" Não Confirmada**
- Assumido com base em padrão regional SC
- **Risco:** Se for laje maciça ou nervurada, muda custo estrutura
- **Lição:** SEMPRE validar tipo de laje com projeto estrutural (memorial ou IFC)

**7.6 Padrão de Acabamento "Alto Padrão"**
- Classificado com base em indicadores (localização, lazer completo, brise, ático)
- Mas sem memorial descritivo oficial
- **Risco:** Se acabamento for médio padrão, muda custo/m²
- **Lição:** Solicitar memorial descritivo OU especificações de acabamento antes de classificar padrão

---

## 8. PRÓXIMOS PROJETOS — CHECKLIST OTIMIZADO

### 📋 FASE 1: RECEBIMENTO DO PROJETO (DIA 0)

**Solicitar ao cliente:**
- [ ] Quadro de áreas geral (AC total, AT, áreas por pavimento)
- [ ] Projeto de implantação (com AT, projeções, cortes)
- [ ] Memorial descritivo (se existir)
- [ ] Especificações de acabamento
- [ ] Data-base de preços/CUB
- [ ] Arquivo IFC (se disponível)
- [ ] Quantitativos executivos (se disponíveis)

**Análise preliminar:**
- [ ] Listar TODOS os arquivos disponíveis (contar PDFs, XLSXs, IFCs)
- [ ] Identificar disciplinas (arquitetura, estrutura, hidro, elétrico, PPCI)
- [ ] Mapear dados faltantes críticos
- [ ] Estimar tempo de processamento (regra: ~2 min por PDF pesado)

### 📋 FASE 2: ANÁLISE POR DISCIPLINA (DIAS 1-2)

**Onda 1: Arquitetura (sempre primeiro)**
- [ ] Processar plantas baixas → quadro de áreas, pavimentos, tipologias
- [ ] **IDENTIFICAR BLOQUEADORES** (AC, AT, dados faltantes)
- [ ] **AVISAR CLIENTE IMEDIATAMENTE** se faltar dados críticos
- [ ] Validar multiplicadores (pavimentos tipo idênticos?)

**Onda 2: IFC Estrutural (se disponível)**
- [ ] Validar completude do IFC (lajes, vigas, pilares, fundação preenchidos?)
- [ ] Extrair volumes/pesos/áreas
- [ ] Anotar limitações (o que falta no IFC?)

**Onda 3: Estrutura Complementar (PDFs)**
- [ ] Se IFC incompleto: processar PDFs com amostragem inteligente
- [ ] Aplicar multiplicadores validados
- [ ] Validar taxa de aço (70-90 kg/m³)

**Onda 4: Hidrossanitário**
- [ ] Priorizar planilhas XLSX de quantitativos (se disponíveis)
- [ ] Se só PDFs: amostragem + multiplicadores

**Onda 5: Elétrico**
- [ ] Buscar quadro de cargas consolidado (prancha específica)
- [ ] Validar potência demandada vs transformador

**Onda 6: PPCI**
- [ ] Processar memoriais descritivos (prioridade)
- [ ] Extrair quantitativos de sistemas obrigatórios
- [ ] Validar aprovação CBMSC

**Timeout recomendado por onda:**
- Arquitetura: 10 min
- IFC: 15 min
- PDFs estruturais: 20 min
- Hidro (com XLSX): 10 min
- Elétrico: 15 min
- PPCI: 15 min

### 📋 FASE 3: GERAÇÃO DE ENTREGÁVEIS (DIA 3)

**Ordem de geração:**
1. Briefing (consolidar dados confirmados vs estimados)
2. Orçamento Paramétrico (usar briefing)
3. Orçamento Executivo (consolidar quantitativos)
4. Memorial Descritivo (com rastreabilidade desde o início)

**Checklist memorial descritivo:**
- [ ] 14 seções estruturadas (identificação, características, sistemas, normas)
- [ ] Tabelas de quantitativos em CADA sistema
- [ ] Referência cruzada ao orçamento (Aba X, Item Y)
- [ ] Dados estimados claramente marcados
- [ ] Backup antes de edições grandes

**Checklist orçamento executivo:**
- [ ] **⚠️ EXTRAÇÃO POR PAVIMENTO** (regra obrigatória — nunca consolidar em linha única)
- [ ] Formatação profissional (bordas, cores, hierarquia)
- [ ] BDI aplicado corretamente
- [ ] Subtotais por grupo
- [ ] Totais por sistema com BDI
- [ ] Custos unitários atualizados (SINAPI)

**Checklist orçamento paramétrico:**
- [ ] Briefing dinâmico (25 dropdowns)
- [ ] Sistema de validação (semáforo P10-P90)
- [ ] Aba ALERTAS com dados fora da faixa
- [ ] Ressalvas sobre estimativas

### 📋 FASE 4: VALIDAÇÃO E ENTREGA (DIA 4)

**Validações finais:**
- [ ] Taxa de aço estrutura (70-90 kg/m³)
- [ ] Potência elétrica vs transformador
- [ ] Reservatórios vs demanda/normas
- [ ] Custo/m² vs CUB da região
- [ ] Todos os dados estimados marcados

**Documentação:**
- [ ] README com instruções de uso
- [ ] Lista de dados faltantes/validações pendentes
- [ ] Próximos passos recomendados

---

## 9. FERRAMENTAS E BIBLIOTECAS VALIDADAS

### ✅ STACK TÉCNICO EFICAZ

**Python:**
- `ifcopenshell` → IFC estrutural ✅
- `pandas` + `openpyxl` → Excel (leitura/escrita) ✅
- `pdfplumber` → Extração de PDFs ✅
- `python-docx` → Geração de DOCX (não usado no Oxford, mas disponível)

**Comandos shell úteis:**
- `find . -name "*.pdf" | wc -l` → contar PDFs
- `ls -lh` → verificar tamanho de arquivos
- `grep -c "padrão"` → validar conteúdo

**Formatação:**
- Markdown → base de documentação (fácil conversão pra DOCX depois)
- Excel → orçamentos (openpyxl com formatação profissional)

---

## 10. MÉTRICAS DO PROJETO OXFORD

**Inputs:**
- 779 arquivos (340 PDFs estrutura + 26 PDFs elétrico + 23 PDFs PPCI + 10 plantas arquitetura + 10 XLSX hidro + ...)
- 1 IFC estrutural (21 MB)

**Processamento:**
- 15 ondas de análise/geração
- 3 timeouts (recuperados com sucesso)
- 13 subagentes lançados
- ~6h10 de trabalho total

**Outputs:**
- 4 entregáveis principais (2 XLSX + 2 MD)
- 10 arquivos de análise intermediária (.md)
- 4 JSONs de dados brutos
- 3 scripts Python reutilizáveis
- 1 documento de lições aprendidas (este)

**Precisão alcançada:**
- Estrutura: dados reais IFC + PDFs (alta confiança)
- Hidro: quantitativos reais de planilhas executivas (alta confiança)
- Elétrico: memorial + estimativas calibradas (média confiança)
- PPCI: memoriais completos (alta confiança)
- Acabamentos: estimativas por área (baixa confiança — validar)

---

## 11. CONCLUSÕES E RECOMENDAÇÕES

### 🎯 PRINCIPAIS APRENDIZADOS

1. **IFC é ouro quando disponível** — mesmo incompleto, dá dados precisos (validar completude primeiro)
2. **Timeout realista desde o início** — 15-20 min para processamento pesado, não 10 min
3. **Solicitar dados críticos NO DIA 0** — quadro de áreas, memorial, especificações
4. **Rastreabilidade agrega muito valor** — memorial + orçamento conectados = ferramenta de gestão
5. **Amostragem inteligente funciona** — processar 16% dos PDFs com multiplicadores = cobertura 100%
6. **Validações cruzadas são essenciais** — taxa de aço, potência vs trafo, reservatórios vs norma
7. **Marcar estimativas claramente** — transparência sobre confiabilidade dos dados
8. **Backup antes de edições grandes** — segurança para reverter

### 🚀 OTIMIZAÇÕES PARA PRÓXIMOS PROJETOS

**Redução de tempo esperada:** ~30% (de 6h10 → ~4h20)

**Como:**
- Solicitar dados críticos no Dia 0 (elimina bloqueios)
- Timeout realista desde o início (elimina 3 timeouts = -30 min)
- Template de briefing pré-preenchido (economiza 20 min)
- Scripts reutilizáveis (economiza 30 min)
- Rastreabilidade desde o início no memorial (não adicionar depois)

**Ganho de qualidade esperado:**
- Menos dados estimados (mais dados reais solicitados cedo)
- Validações automáticas desde a primeira versão
- Entregáveis com rastreabilidade completa desde o início

---

## 12. CHECKLIST RÁPIDO — RESUMO EXECUTIVO

### ✅ SEMPRE FAZER

- [ ] **⚠️ ORÇAMENTO EXECUTIVO: Extração SEMPRE por pavimento** (nunca consolidar em linha única)
- [ ] Solicitar dados críticos no Dia 0 (quadro de áreas, memorial, especificações)
- [ ] Validar completude do IFC antes de confiar
- [ ] Usar timeout mínimo 15 min para processamento pesado
- [ ] Aplicar amostragem inteligente + multiplicadores
- [ ] Incluir rastreabilidade memorial ↔ orçamento
- [ ] Marcar estimativas claramente (✅ ⚠️ ❌)
- [ ] Validar dados críticos (taxa aço, potência vs trafo, etc.)
- [ ] Fazer backup antes de edições estruturais grandes
- [ ] Documentar lições aprendidas ao final

### ⛔ NUNCA FAZER

- [ ] Confiar 100% em IFC sem validar completude
- [ ] Usar timeout otimista (10 min) para >20 PDFs
- [ ] Tentar processar centenas de PDFs sem amostragem
- [ ] Entregar estimativas sem marcar claramente
- [ ] Pular validações cruzadas (taxa aço, dimensionamentos)
- [ ] Tentar corrigir rota de subagente ativo (sessions_send mid-flight)
- [ ] Fazer polling de subagentes em loop
- [ ] Assumir tipo de laje sem validar com projeto estrutural

---

**FIM DO DOCUMENTO**

*Essas lições aprendidas devem ser consultadas no início de TODOS os projetos futuros de orçamentação.*
