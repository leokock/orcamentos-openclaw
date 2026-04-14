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
| `base/FASES-FUTURAS.md` | Roadmap retomavel — estado de todas as fases (1-19 concluidas) |
| `base/CAMADA-QUALITATIVA-GEMMA.md` | Fonte canonica da camada qualitativa Gemma (sub-disc, premissas, observacoes, classificacao padrao) |
| `base/SESSAO-2026-04-14-REVISAO-3-PACOTES.md` | **Narrativa completa** da sessao de revisao dos 3 pacotes + fases 14/16/17/18/18b/19 |
| `base/PARAMETRICO-V2-HIBRIDO.md` | **Referencia canonica** do fluxo parametrico V2 Hibrido (dropdown + override manual) — fase 19 |
| `base/calibration-condicional-padrao.json` | **Calibracao condicional por padrao Gemma (fonte primaria pos-fase 18b)** |
| `base/padroes-classificados-consolidado.json` | Labels Gemma semanticos dos 125/126 projetos |
| `base/itens-pus-agregados.json` | 4.210 clusters PU cross-projeto (usado no PU sanity filter) |

## Modo autonomo com modelo local (Gemma/Ollama)

Quando o pipeline envolve Gemma/Ollama local, trabalhar **autonomamente**: disparar, monitorar, investigar bugs/gaps, corrigir, reprocessar — sem checkpoint humano. Interacao so em decisoes arquiteturais (escolha entre caminhos grandes), destrutivas (delete/overwrite), ou na entrega final. Pipelines retomaveis (fila + log + resume) sao padrao. Custo zero de token significa que tempo eh o unico custo — investir tempo em iteracao autonoma para chegar no valor final. Ver memorias `feedback_modo_autonomo_gemma_local.md` e `feedback_qualidade_sobre_velocidade.md`.

## Entrega pro Drive compartilhado (OBRIGATORIO para parametricos/preliminares)

Todo parametrico/preliminar gerado em `base/pacotes/{slug}/` deve ser sincronizado pro Google Drive compartilhado como parte da entrega final. **Commitar no git nao eh suficiente** — a equipe Cartesian (orcamentos, comercial, obras) acessa as entregas pelo Drive em `_Parametrico_IA/` ou `_Executivo_IA/`.

**Script autoritativo:** `scripts/sincronizar_parametrico_drive.py`

```bash
# Apos gerar xlsx+docx+pdf do slug
python scripts/sincronizar_parametrico_drive.py --slug {slug} --archive-old

# Ou sync de todos de uma vez
python scripts/sincronizar_parametrico_drive.py --all --archive-old

# Dry-run pra conferir antes de copiar
python scripts/sincronizar_parametrico_drive.py --all --dry-run
```

**Regras:**
- Nomenclatura Drive: `{drive_prefix}-parametrico-v3-hibrido.{xlsx,docx,pdf}` + config.json (padrao Cartesian historico)
- Mapeamento git_slug -> drive_folder/drive_prefix em `scripts/drive-mapping.json` (nem sempre bate — ex: `placon-arminio-tavares` vira `arminio-tavares` no Drive)
- `--archive-old` move versoes antigas `*-parametrico-v*.xlsx` pra subpasta `_antigo/` antes de copiar (preserva historico)
- Drive path (Windows): `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Parametrico_IA\`
- Log append-only em `base/drive-sync.log.jsonl`
- **Confirmar com Leo** antes do primeiro sync de um slug novo (afeta Drive compartilhado)

**Doc canonica:** `base/PARAMETRICO-V2-HIBRIDO.md` secao "Entrega no Drive"

**Memoria correlata:** `~/clawd/memory/project_entrega_parametrico_drive.md`

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
