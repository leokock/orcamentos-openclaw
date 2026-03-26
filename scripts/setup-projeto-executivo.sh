#!/bin/bash
# Setup de novo projeto executivo — cria pastas + symlink pro Drive
# Uso: ./scripts/setup-projeto-executivo.sh [slug-do-projeto]
# Exemplo: ./scripts/setup-projeto-executivo.sh senna-tower

set -e

SLUG="$1"
if [ -z "$SLUG" ]; then
  echo "Uso: $0 [slug-do-projeto]"
  echo "Exemplo: $0 senna-tower"
  exit 1
fi

BASE="$HOME/orcamentos"
DRIVE_EXEC="$HOME/Library/CloudStorage/GoogleDrive-leonardo@cartesianengenharia.com/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/_Executivo_IA"

echo "Criando projeto executivo: $SLUG"

# 1. Criar pasta do projeto no git
mkdir -p "$BASE/executivos/$SLUG/briefings"
mkdir -p "$BASE/executivos/$SLUG/fontes"
mkdir -p "$BASE/executivos/$SLUG/diffs"
mkdir -p "$BASE/executivos/$SLUG/planilhas"
echo "  Pastas criadas em executivos/$SLUG/"

# 2. Criar pasta no Drive
mkdir -p "$DRIVE_EXEC/$SLUG"
echo "  Pasta criada no Drive: _Executivo_IA/$SLUG/"

# 3. Symlink entregas/ → Drive
if [ -L "$BASE/executivos/$SLUG/entregas" ]; then
  echo "  Symlink entregas/ ja existe"
elif [ -d "$BASE/executivos/$SLUG/entregas" ]; then
  echo "  AVISO: entregas/ e uma pasta real (nao symlink). Mova os arquivos pro Drive e troque pelo symlink."
else
  ln -s "$DRIVE_EXEC/$SLUG" "$BASE/executivos/$SLUG/entregas"
  echo "  Symlink criado: entregas/ → Drive/_Executivo_IA/$SLUG/"
fi

# 4. Criar PROJETO.md se nao existir
if [ ! -f "$BASE/executivos/$SLUG/PROJETO.md" ]; then
  cat > "$BASE/executivos/$SLUG/PROJETO.md" << EOF
# Projeto: $SLUG

## Informacoes Gerais
- **Nome:** [a preencher]
- **Cliente:** [a preencher]
- **Tipologia:** [a preencher]
- **Status:** Em orcamento executivo

## Localizacao dos Arquivos Fonte
- Projetos: \`projetos/$SLUG/\` (Google Drive)
- Entregas: \`executivos/$SLUG/entregas/\` (Google Drive via symlink)
- Briefings: \`executivos/$SLUG/briefings/\` (git)

---
*Criado em $(date +%Y-%m-%d)*
EOF
  echo "  PROJETO.md criado"
fi

echo ""
echo "Setup completo! Estrutura:"
echo "  executivos/$SLUG/"
echo "    briefings/    (git — trabalho tecnico)"
echo "    entregas/     (Drive — xlsx, docx pro cliente)"
echo "    fontes/       (git — fontes locais)"
echo "    PROJETO.md    (git — dados do projeto)"
