# CLAUDE.md — Orcamentos Cartesian

## O que e este workspace

Workspace de orcamentacao (parametrica + executiva) da **Cartesian Engenharia**, acessado por bots no Slack. O bot principal e o **Cartesiano** — assistente tecnico que gera orcamentos, processa IFCs, extrai quantitativos e interage com a equipe via canais Slack.

## Arquitetura

```
Equipe (Slack) → Bot Cartesiano → ~/orcamentos/ (este repo)
                                        ├── Google Drive (symlinks)
                                        └── Supabase (Memorial Cartesiano)
```

- **`~/orcamentos`** (este repo) — workspace do Cartesiano, especializado em orcamentacao
- **`~/clawd`** — workspace do Jarvis (agente geral), configs e skills compartilhadas
- Ambos sincronizam via Obsidian Git plugin (auto-pull 5min)
- Pastas de projetos/entregas sincronizam com Google Drive via symlinks

## Documentacao chave

| Arquivo | O que tem |
|---------|-----------|
| `AGENTS.md` | **Regras completas do bot** — Slack, workflows, dominios (700+ linhas) |
| `TOOLS.md` | Credenciais Supabase, schema de tabelas, RPCs |
| `IDENTITY.md` | Identidade: "Cartesiano", tecnico, preciso, direto |
| `SOUL.md` | Tom, limites, o que faz e nao faz |
| `docs/ORCAMENTO-WORKFLOW.md` | Workflow completo do parametrico (3 fases) |
| `docs/LICOES-APRENDIDAS-OXFORD.md` | Licoes aprendidas do projeto referencia |
| `base/BRIEFING-PARAMETRICO.md` | Template briefing (25 perguntas) |

## Regras criticas (resumo — detalhes em AGENTS.md)

1. **Nunca expor erros no canal** — tratar internamente, responder limpo
2. **Caminhos Drive → local** — converter automaticamente (tabela em AGENTS.md Regra #0)
3. **Baixar arquivos via script** — `python3.11 scripts/slack_file_downloader.py --bot cartesiano --baixar --thread <ts>`
4. **Upload obrigatorio** — todo arquivo gerado deve ir pro Slack com `slack_uploader.py --bot cartesiano --file <f> --thread <ts> --channel <ch>`
5. **Nunca reusar dados de outro projeto** — confirmar fonte antes de gerar

## Scripts principais

| Script | Uso |
|--------|-----|
| `scripts/gerar_template_dinamico_v2.py` | Gerar parametrico (14 abas, bottom-up) |
| `scripts/processar_executivo.py` | Processar orcamento executivo real |
| `scripts/consolidar_base_pus.py` | Recalibrar base de PUs |
| `scripts/gerar_memorial_rastreavel.py` | Memorial Word rastreavel |
| `scripts/slack_file_downloader.py` | Baixar arquivos do Slack |
| `scripts/slack_uploader.py` | Upload de arquivos no Slack |
| `scripts/slack_ifc_processor.py` | Processar IFCs do Slack |
| `scripts/setup-projeto-executivo.sh` | Setup novo projeto executivo (pastas + symlink) |

## Git sync

Dois repos independentes, ambos com auto-pull:

| Local | Remote |
|-------|--------|
| `~/clawd` | `github.com/leokock/openclaw.git` |
| `~/orcamentos` | `github.com/leokock/orcamentos-openclaw.git` |

Ao pedir commit+push, fazer nos dois se houver mudancas em ambos.
