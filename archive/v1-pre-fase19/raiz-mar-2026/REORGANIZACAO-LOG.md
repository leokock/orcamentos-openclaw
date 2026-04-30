# Log de Reorganização — orcamento-parametrico/

> Data: 06/03/2026
> Executado por: Jarvis (subagent)

## Resumo

A pasta foi reorganizada de ~270 arquivos flat para uma estrutura organizada em subpastas.

### Arquivos movidos por pasta

| Pasta | Qtd | Conteúdo |
|-------|-----|----------|
| `indices/` | 58 | 57 arquivos *-indices.md + FALTAM-CALIBRAR.md |
| `executivos/` | 96 | xlsx/pdf de orçamentos originais recebidos (analíticos, custos indiretos, gerenciamento, prazo, levantamentos) |
| `parametricos/` | 50 | xlsx/pdf/pptx gerados (paramétricos, apresentações, templates, painel HTML) |
| `docs/` | 10 | documentação, workflow, estratégia, referências, estudo Monolyt, atualização CUB |
| `scripts/` | 2 | gerar_template_dinamico.py, exportar-pacote-drive.sh |
| `archive/` | 48 | templates v1-v3, rozzo v1-v3, MaisonBeach v3-v4, scripts obsoletos, lock files, MDs de categorias, MDs obsoletos, __pycache__, duplicatas de indices |

### Mantidos na raiz
- `calibration-data.json` (54 projetos, após remoção da duplicata "adda")
- `calibration-stats.json`
- `BASE-CONHECIMENTO-PARAMETRICO.md`
- `BRIEFING-PARAMETRICO.md`
- `pacote-drive/` (mantido no lugar)

## Duplicatas de Índices Resolvidas

Todos os pares tinham conteúdo diferente (versões diferentes do template). Mantido o mais completo/atualizado:

| Mantido (em indices/) | Arquivado (em archive/) | Critério |
|---|---|---|
| `arv-ingleses-spot-indices.md` (809 linhas) | `arv-inglesesspot-indices.md` (595 linhas) | Mais completo |
| `brasin-mariolago-indices.md` (782 linhas) | `brasin-mario-lago-indices.md` (746 linhas) | Mais completo |
| `brava-sixteen-indices.md` (484 linhas) | `mendes-bravasixteen-indices.md` (377 linhas) | Mais completo, nome padronizado |
| `etr-mediterraneo-indices.md` (792 linhas) | `etr-zion-mediterraneo-indices.md` (697 linhas) | Mais completo |
| `soho-538-indices.md` (746 linhas) | `soho-indices.md` (258 linhas) | Muito mais completo |

## Duplicata "adda" no calibration-data.json

- Removida entrada index 39 (sem `normalized` nem `meta`)
- Mantida entrada index 40 (com `normalized` e `meta` completos)
- Total projetos: 54 (antes: 55 com duplicata)

## Script gerar_template_dinamico.py — Path Atualizado

- `output_dir` alterado de `~/clawd/orcamento-parametrico` para `~/clawd/orcamento-parametrico/parametricos`
- Único arquivo com conteúdo alterado (1 linha)

## Índices Faltando Calibrar

- 26 indices não estão no calibration-data.json
- Lista completa em `indices/FALTAM-CALIBRAR.md`
- Alguns podem ser aliases de projetos já calibrados (ex: eze-eilat ↔ eilat)

## Scripts Arquivados

- `gerar_template.py` → versão antiga, substituída por `gerar_template_dinamico.py`
- `gerar-rozzo.py` → obsoleto
- `merge_cowork.py` → obsoleto
- `criar_apresentacao_rozzo.py` → obsoleto

## MDs de Categorias Arquivados

ALVENARIA, SUPRAESTRUTURA, TETO, COBERTURA, COMPLEMENTARES, CONTENÇÕES, ESQUADRIAS, IMPERMEABILIZAÇÃO, INFRAESTRUTURA, INSTALAÇÕES, MOVIMENTAÇÃO_DE_TERRA, PINTURA_INTERNA, SISTEMAS_ESPECIAIS, Acabamentos_de_Piso_e_Parede, Rev._Fachada, Rev._Internos_Piso_e_Parede, Auxiliar, Obra, DADOS_INICIAIS, REGRAS_01-03, REGRAS_CONSOLIDADO, TEMPLATE-INDICES-EXPANDIDO, PUs-NOVOS-PROJETOS
