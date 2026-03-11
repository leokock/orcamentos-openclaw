# Orçamento Executivo — Workspace

Área de trabalho para criação e manutenção de orçamentos executivos.

## Documentação
- **Workflow completo:** `docs/ORCAMENTO-EXECUTIVO-WORKFLOW.md`
- **Sistema Memorial:** `docs/MEMORIAL-CARTESIANO-SISTEMA.md`

## Estrutura

```
orcamento-executivo/
├── README.md              # Este arquivo
├── templates/
│   ├── briefing-template.md   # Template de briefing por disciplina
│   └── diff-template.md      # Template de relatório de mudanças
└── projetos/
    └── [nome-projeto]/        # Um diretório por projeto
        ├── PROJETO.md         # Dados do projeto
        ├── briefings/         # Briefings por disciplina e revisão
        ├── planilhas/         # Planilhas Excel geradas
        ├── diffs/             # Relatórios de mudanças entre revisões
        └── fontes/            # PDFs/IFCs originais recebidos
```

## Como Usar

1. Leo envia PDFs/IFCs de uma disciplina
2. Jarvis processa → gera briefing + planilha
3. Leo valida → upload no Memorial Cartesiano
4. Na atualização: Jarvis compara → relatório de mudanças → Leo aprova → nova versão

## Disciplinas Suportadas

- Estrutura (fundação + supraestrutura)
- Instalações Hidrossanitárias
- Instalações Elétricas
- Instalações Especiais (PCI, climatização, elevadores, etc.)
- Esquadrias

---

*Criado: 10/mar/2026*
