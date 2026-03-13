# Orçamentos Cartesian Engenharia

Workspace de orçamentação paramétrica e executiva da Cartesian Engenharia.

---

## 📚 Documentação Principal

**Leia antes de iniciar qualquer projeto:**

1. **[ORCAMENTO-WORKFLOW.md](docs/ORCAMENTO-WORKFLOW.md)** — Processo completo de orçamentação (4 fases)
2. **[LICOES-APRENDIDAS-OXFORD.md](docs/LICOES-APRENDIDAS-OXFORD.md)** — Lições do projeto Oxford (12 seções, armadilhas + boas práticas)

---

## 🗂️ Estrutura

```
~/orcamentos/
├── docs/                    # Documentação de processos
│   ├── ORCAMENTO-WORKFLOW.md         # Workflow completo ⭐
│   └── LICOES-APRENDIDAS-OXFORD.md   # Lições aprendidas ⭐
├── projetos/                # Projetos de orçamentação
│   ├── mussi-oxford/        # Oxford 600 Residence (referência completa)
│   └── ...
├── scripts/                 # Scripts Python auxiliares
├── parametrico/            # Symlink → ~/clawd/orcamento-parametrico
└── executivo/              # Templates de orçamento executivo
```

---

## 🚀 Início Rápido

### Novo Projeto de Orçamentação

1. **Ler documentação obrigatória:**
   - [ORCAMENTO-WORKFLOW.md](docs/ORCAMENTO-WORKFLOW.md) (workflow completo)
   - [LICOES-APRENDIDAS-OXFORD.md](docs/LICOES-APRENDIDAS-OXFORD.md) (armadilhas + boas práticas)

2. **Criar estrutura do projeto:**
   ```bash
   cd ~/orcamentos/projetos
   mkdir <nome-projeto>
   cd <nome-projeto>
   
   # Criar pastas por disciplina
   mkdir "01. PROJETO ARQUITETONICO"
   mkdir "02. PROJETO ESTRUTURAL"
   mkdir "03. PROJETO HIDROSSANITARIO"
   mkdir "04. PROJETO ELETRICO"
   mkdir "05. PROJETO PPCI"
   ```

3. **Seguir Fase 1 do workflow:**
   - Solicitar dados críticos ao cliente (Dia 0)
   - Fazer análise preliminar (inventário de arquivos)

4. **Consultar projeto de referência:**
   - `projetos/mussi-oxford/` — exemplo completo com 4 entregáveis

---

## 📖 Workflow Resumido

### Fase 1: Recebimento (Dia 0)
✅ Solicitar quadro de áreas, memorial, especificações, IFC  
✅ Inventário de arquivos por disciplina  
✅ Identificar bloqueadores

### Fase 2: Análise (Dias 1-2)
✅ Arquitetura → Hidro → Estrutura (IFC + PDFs) → PPCI → Elétrico  
✅ Amostragem inteligente + multiplicadores  
✅ Validar taxa de aço, dimensionamentos

### Fase 3: Entregáveis (Dia 3)
✅ Briefing → Paramétrico → Executivo → Memorial (com rastreabilidade)

### Fase 4: Validação (Dia 4)
✅ Validações técnicas (taxa aço, potência vs trafo, custo/m² vs CUB)  
✅ Backup e entrega

---

## 🎯 Entregáveis Padrão

1. **Orçamento Paramétrico** — Excel 14 abas
   - Briefing dinâmico (25 dropdowns)
   - 18 macrogrupos orçamentários
   - Sistema de validação (semáforo P10-P90)
   - Base calibrada com 75 projetos reais

2. **Orçamento Executivo** — Excel 8 abas
   - Estrutura, hidro, elétrico, PPCI, vedações, acabamentos, lazer
   - BDI 25% aplicado
   - Formatação profissional
   - Custos unitários SINAPI

3. **Memorial Descritivo** — Markdown (→ DOCX)
   - 14 seções estruturadas
   - 20-25 tabelas de rastreabilidade (memorial ↔ orçamento)
   - Normas técnicas completas

4. **Briefing Final** — Markdown
   - Dados confirmados ✅ vs estimados ⚠️ vs indisponíveis ❌
   - Lista de bloqueadores críticos
   - Próximos passos

---

## ⚙️ Stack Técnico

**Python:**
- `ifcopenshell` → IFC estrutural
- `pandas` + `openpyxl` → Excel (leitura/escrita)
- `pdfplumber` → Extração de PDFs

**Scripts principais:**
- `~/clawd/orcamento-parametrico/scripts/gerar_template_dinamico.py` — Gerador de orçamento paramétrico

---

## 📊 Projeto de Referência — Oxford 600 Residence

**Localização:** `projetos/mussi-oxford/`

**Entregáveis gerados:**
- ✅ Orçamento Paramétrico (14 abas, 33 KB)
- ✅ Orçamento Executivo (8 abas, 24 KB)
- ✅ Memorial Descritivo (77 KB, 21 tabelas rastreáveis)
- ✅ Briefing Final (dados consolidados)

**Métricas:**
- 779 arquivos processados
- 1 IFC estrutural (21 MB)
- ~6h30 de trabalho total
- 4 entregáveis completos

**Lições aprendidas:** [docs/LICOES-APRENDIDAS-OXFORD.md](docs/LICOES-APRENDIDAS-OXFORD.md)

---

## ⚠️ Checklist Obrigatório

### ✅ SEMPRE FAZER
- Solicitar dados críticos no Dia 0
- Validar completude do IFC antes de confiar
- Usar timeout realista (15-20 min para processamento pesado)
- Incluir rastreabilidade memorial ↔ orçamento
- Marcar estimativas claramente (✅ ⚠️ ❌)
- Fazer backup antes de enviar

### ⛔ NUNCA FAZER
- Confiar 100% em IFC sem validar completude
- Usar timeout otimista (<15 min) para >20 PDFs
- Entregar estimativas sem marcar claramente
- Pular validações cruzadas (taxa aço, potência vs trafo)

---

## 🔗 Links Úteis

- **Sistema Paramétrico:** `~/clawd/orcamento-parametrico/`
- **Workspace Jarvis:** `~/clawd/`
- **Documentação OpenClaw:** `~/clawd/docs/`

---

**Última atualização:** 13/março/2026  
**Baseado em:** Projeto Oxford 600 Residence (Mussi Empreendimentos)
