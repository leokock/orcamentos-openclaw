# Aposentadoria orcamentos-openclaw - Fase 0

Data: 2026-06-11

## Estado inicial verificado

- Branch local: `main`.
- Divergencia inicial: `ahead 1 / behind 1` em relacao a `origin/main`.
- Commit local nao publicado: `3c11cad Add quantitativos extraction Bela Vida (Chiquetti) - Fase 1+2`.
- Commit remoto pendente: `ca4da35 chore: remover symlinks orfaos BASE-CONHECIMENTO e BRIEFING-PARAMETRICO`.
- Status inicial: 667 entradas no `git status --porcelain`.
- Distribuicao inicial: 573 delecoes, 73 arquivos novos e 21 modificacoes.

## Decisao de seguranca

O diretorio `executivos` agora e um symlink para o Drive:

`G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA`

Por isso, as delecoes vistas em `executivos/**` sao tratadas como limpeza do indice Git do repo legado, nao como delecao fisica. A Fase 0 deve parar de rastrear conteudo que vive no Drive e manter esse historico apenas nos commits antigos.

## Grupos de triagem

- Mounts e saidas locais ignoradas: `executivos`, `parametricos`, `planejamento`, `projetos`, `output`, `temp`, `_tmp`, `archive`, `executivos_PRE-SYMLINK-bak`.
- Conteudo real a preservar no snapshot: `base/`, `docs/`, `scripts/`, `skills/` e arquivos raiz modificados.
- Commit remoto pendente deve ser integrado por rebase depois que a arvore local estiver commitada, porque `git pull --rebase --autostash` falha quando ha tracked files sob symlink.

## Validacao esperada

- `git status --short --branch` limpo.
- `ahead 0 / behind 0`.
- Tag `snapshot-aposentadoria-2026-06` criada e publicada.
