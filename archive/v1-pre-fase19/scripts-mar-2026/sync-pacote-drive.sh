#!/bin/bash
# sync-pacote-drive.sh — Sincroniza arquivos do orcamento-parametrico para pacote-drive
# Uso: bash orcamento-parametrico/scripts/sync-pacote-drive.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$(dirname "$SCRIPT_DIR")"
DEST_DIR="$SRC_DIR/pacote-drive"

echo "📦 Sincronizando pacote-drive..."
echo "   Fonte: $SRC_DIR"
echo "   Destino: $DEST_DIR"
echo ""

# Arquivos-chave que devem estar sincronizados
FILES=(
  "calibration-data.json"
  "calibration-stats.json"
  "gerar_template_dinamico.py"
  "BRIEFING-PARAMETRICO.md"
  "BASE-CONHECIMENTO-PARAMETRICO.md"
  "TEMPLATE-INDICES-EXPANDIDO.md"
)

# MDs de categorias (macrogrupos)
CATEGORY_MDS=(
  "ALVENARIA.md"
  "COMPLEMENTARES.md"
  "COBERTURA.md"
  "CONTENÇÕES.md"
  "DADOS_INICIAIS.md"
  "ESQUADRIAS.md"
  "IMPERMEABILIZAÇÃO.md"
  "INFRAESTRUTURA.md"
  "INSTALAÇÕES.md"
)

# Docs
DOC_FILES=(
  "ESTRATEGIA-DOIS-TIERS.md"
  "MAPA-COBERTURA.md"
)

UPDATED=0

sync_file() {
  local src="$1"
  local dest="$2"

  if [ ! -f "$src" ]; then
    echo "   ⚠️  Não encontrado: $(basename "$src")"
    return
  fi

  if [ ! -f "$dest" ] || ! diff -q "$src" "$dest" > /dev/null 2>&1; then
    cp "$src" "$dest"
    echo "   ✅ $(basename "$src")"
    UPDATED=$((UPDATED + 1))
  fi
}

echo "🔄 Arquivos-chave:"
for f in "${FILES[@]}"; do
  sync_file "$SRC_DIR/$f" "$DEST_DIR/$f"
done

echo ""
echo "🔄 MDs de categorias:"
for f in "${CATEGORY_MDS[@]}"; do
  sync_file "$SRC_DIR/$f" "$DEST_DIR/$f"
done

echo ""
echo "🔄 Docs:"
for f in "${DOC_FILES[@]}"; do
  # Docs podem estar em docs/ ou na raiz
  if [ -f "$SRC_DIR/docs/$f" ]; then
    sync_file "$SRC_DIR/docs/$f" "$DEST_DIR/$f"
  elif [ -f "$SRC_DIR/$f" ]; then
    sync_file "$SRC_DIR/$f" "$DEST_DIR/$f"
  fi
done

# Copiar FRAMEWORK se existe em docs/
if [ -f "$SRC_DIR/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md" ]; then
  sync_file "$SRC_DIR/docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md" "$DEST_DIR/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md"
fi

echo ""
if [ "$UPDATED" -eq 0 ]; then
  echo "✨ Tudo já estava atualizado!"
else
  echo "📋 $UPDATED arquivo(s) atualizado(s)."
fi
