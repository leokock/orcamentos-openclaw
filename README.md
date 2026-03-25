# Orcamentos Cartesian Engenharia

Workspace centralizado de orcamentacao parametrica e executiva.

---

## Estrutura

```
~/orcamentos/
├── base/                  # Conhecimento para gerar orcamentos
│   ├── indices/           # 78 indices extraidos de executivos reais
│   ├── calibration-*.json # Dados calibrados (medianas, P10, P90)
│   ├── templates/         # Templates parametrico + executivo
│   └── *.md               # Base conhecimento, briefing, subdisciplinas
│
├── parametricos/          # Parametricos entregues (planilhas + apresentacoes)
│
├── executivos/            # Executivos entregues (por projeto)
│   ├── templates/         # Templates de EAP, briefing, diff
│   └── thozen-electra/    # Projeto executivo completo (referencia)
│
├── projetos/              # Projetos — inputs para parametrico E/OU executivo
│   ├── mussi-oxford/      # Referencia completa (param + exec + memorial)
│   ├── parador-ag7/
│   ├── thozen-electra/    # Fontes DXF/DWG
│   └── ...
│
├── scripts/               # Scripts reutilizaveis (extracoes, IFC, DWG, Slack)
├── docs/                  # Workflows e processos genericos
├── memory/                # Memoria do Cartesiano
└── skills/                # Skills do Cartesiano (apresentacoes)
```

---

## Fluxo de Trabalho

```
Cliente envia projeto → projetos/<nome>/
                              ↓
                    base/ (indices + calibracao + templates)
                              ↓
              ┌───────────────┴───────────────┐
              │                               │
        parametricos/                   executivos/
        (planilha 14 abas)              (planilha + memorial)
              │                               │
              └───────────┬───────────────────┘
                          ↓
              Executivo processado → base/indices/<nome>-indices.md
                                  → recalibra calibration-data.json
```

---

## Inicio Rapido

### Novo Parametrico
1. Receber dados do projeto → `projetos/<nome>/`
2. Ler `docs/ORCAMENTO-WORKFLOW.md` (Fase 1-3)
3. Responder briefing: `base/BRIEFING-PARAMETRICO.md` (25 perguntas)
4. Gerar com `scripts/gerar_template_dinamico.py`
5. Entrega vai em `parametricos/`

### Novo Executivo
1. Receber projetos completos → `projetos/<nome>/`
2. Ler `docs/LICOES-APRENDIDAS-OXFORD.md`
3. Usar templates de `executivos/templates/`
4. Entrega vai em `executivos/<nome>/`

### Alimentar Base (pos-executivo)
1. Processar executivo real entregue
2. Extrair indices → `base/indices/<nome>-indices.md`
3. Atualizar `base/calibration-data.json`
4. Recalibrar medianas automaticamente

---

## Documentacao

| Doc | Quando ler |
|-----|------------|
| `docs/ORCAMENTO-WORKFLOW.md` | Antes de qualquer orcamento |
| `docs/LICOES-APRENDIDAS-OXFORD.md` | Antes de executivo |
| `docs/ESTRATEGIA-DOIS-TIERS.md` | Entender param vs exec |
| `docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` | Converter exec → param |
| `base/BRIEFING-PARAMETRICO.md` | Perguntas do briefing |
| `base/BASE-CONHECIMENTO.md` | Base textual 40+ projetos |

---

## Projeto de Referencia — Oxford 600 Residence

**Localizacao:** `projetos/mussi-oxford/`

Entregaveis: Parametrico (14 abas) + Executivo (8 abas) + Memorial (21 tabelas) + Briefing

---

## Links

- **Base parametrica:** `base/` (indices, calibracao, templates)
- **Fonte dos dados:** `~/clawd/orcamento-parametrico/` (git tracked)
- **Workspace Jarvis:** `~/clawd/`

---

**Ultima atualizacao:** 23/marco/2026
