#!/bin/bash
# Exporta pacote autocontido para o Drive (Pathy usar no Claude Code/Cowork)
# Uso: bash exportar-pacote-drive.sh [destino]

DEST="${1:-$(dirname $0)/pacote-drive}"
SRC="$(dirname $0)"

echo "📦 Exportando pacote paramétrico para: $DEST"

mkdir -p "$DEST"
mkdir -p "$DEST/atualizacoes"

# Arquivos essenciais
cp "$SRC/gerar_template_dinamico.py" "$DEST/"
cp "$SRC/calibration-data.json" "$DEST/"
cp "$SRC/calibration-stats.json" "$DEST/"
cp "$SRC/BRIEFING-PARAMETRICO.md" "$DEST/"
cp "$SRC/BASE-CONHECIMENTO-PARAMETRICO.md" "$DEST/"
cp "$SRC/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md" "$DEST/"
cp "$SRC/TEMPLATE-INDICES-EXPANDIDO.md" "$DEST/"

# Arquivos de detalhe por macrogrupo (auxiliares)
for f in ALVENARIA.md COBERTURA.md COMPLEMENTARES.md CONTENÇÕES.md DADOS_INICIAIS.md \
         ESQUADRIAS.md IMPERMEABILIZAÇÃO.md INFRAESTRUTURA.md INSTALAÇÕES.md; do
    [ -f "$SRC/$f" ] && cp "$SRC/$f" "$DEST/"
done

# Documentação dos dois tiers (já na pasta)
# CLAUDE.md, MAPA-COBERTURA.md, ESTRATEGIA-DOIS-TIERS.md — já existem

echo "✅ Pacote exportado com sucesso!"
echo ""
echo "Arquivos:"
ls -1 "$DEST/" | while read f; do
    size=$(du -sh "$DEST/$f" 2>/dev/null | cut -f1)
    echo "  $f ($size)"
done
echo ""
echo "📝 Próximo passo: copiar pasta '$DEST' pro Google Drive"
