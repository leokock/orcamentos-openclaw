#!/bin/bash
# Script para processar todos os DXFs de alvenaria do Thozen Electra
# Autor: Cartesiano (Cartesian Engenharia)
# Data: 2026-03-20

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Diretórios
DXF_DIR="projetos/thozen-electra/projetos/03 ALVENARIA/dxf"
OUTPUT_DIR="executivo/thozen-electra/quantitativos/alvenaria"

# Criar diretório de saída
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  PROCESSAMENTO EM LOTE — Alvenaria Thozen Electra                 ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Verificar se o diretório de DXF existe
if [ ! -d "$DXF_DIR" ]; then
    echo -e "${RED}❌ ERRO: Diretório de DXF não encontrado: $DXF_DIR${NC}"
    echo -e "${YELLOW}⚠️  Execute primeiro a conversão DWG → DXF com ODA File Converter${NC}"
    echo ""
    echo "Exemplo:"
    echo "  oda-file-converter \\"
    echo "    --input 'projetos/thozen-electra/projetos/03 ALVENARIA/' \\"
    echo "    --output 'projetos/thozen-electra/projetos/03 ALVENARIA/dxf/' \\"
    echo "    --format DXF \\"
    echo "    --version R2018"
    exit 1
fi

# Verificar se há DXFs
DXF_COUNT=$(find "$DXF_DIR" -type f -iname "*.dxf" | wc -l | tr -d ' ')
if [ "$DXF_COUNT" -eq 0 ]; then
    echo -e "${RED}❌ ERRO: Nenhum arquivo DXF encontrado em: $DXF_DIR${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Encontrados $DXF_COUNT arquivos DXF${NC}"
echo ""

# Mapeamento de arquivos para pavimentos
declare -A MAPA_PAVIMENTOS
MAPA_PAVIMENTOS["RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dxf"]="01-Terreo"
MAPA_PAVIMENTOS["RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dxf"]="02-G1"
MAPA_PAVIMENTOS["RA_ALV_EXE_03_G2 PRÉ-EXECUTIVO_R01.dxf"]="03-G2"
MAPA_PAVIMENTOS["RA_ALV_EXE_04_G3 PRÉ-EXECUTIVO_R01.dxf"]="04-G3"
MAPA_PAVIMENTOS["RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dxf"]="05-G4"
MAPA_PAVIMENTOS["RA_ALV_EXE_06_G5 PRÉ-EXECUTIVO_R01.dxf"]="06-G5"
MAPA_PAVIMENTOS["RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dxf"]="07-Lazer"
MAPA_PAVIMENTOS["RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dxf"]="08-Tipo"
MAPA_PAVIMENTOS["RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dxf"]="09-ResCob"

# Processar cada DXF
PROCESSADOS=0
ERROS=0

for DXF_FILE in "$DXF_DIR"/*.dxf; do
    FILENAME=$(basename "$DXF_FILE")
    
    # Ignorar arquivos de locação (terminados em "B")
    if [[ "$FILENAME" =~ .*B_.* ]]; then
        echo -e "${YELLOW}⏭️  Ignorando prancha de locação: $FILENAME${NC}"
        continue
    fi
    
    # Buscar nome do pavimento
    PAVIMENTO=${MAPA_PAVIMENTOS[$FILENAME]}
    if [ -z "$PAVIMENTO" ]; then
        echo -e "${YELLOW}⚠️  Pavimento não mapeado para: $FILENAME (processando como 'Desconhecido')${NC}"
        PAVIMENTO="Desconhecido"
    fi
    
    # Nome do arquivo de saída
    OUTPUT_FILE="$OUTPUT_DIR/${PAVIMENTO}.json"
    
    # Processar
    echo -e "${BLUE}🔄 Processando: $FILENAME → $PAVIMENTO${NC}"
    
    if python3.11 scripts/extrair_alvenaria_dxf.py "$DXF_FILE" --pavimento "$PAVIMENTO" --output "$OUTPUT_FILE" --quiet; then
        echo -e "${GREEN}✅ Concluído: $OUTPUT_FILE${NC}"
        PROCESSADOS=$((PROCESSADOS + 1))
    else
        echo -e "${RED}❌ ERRO ao processar: $FILENAME${NC}"
        ERROS=$((ERROS + 1))
    fi
    
    echo ""
done

# Resumo final
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  RESUMO DO PROCESSAMENTO                                          ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo -e "${GREEN}✅ Processados com sucesso: $PROCESSADOS${NC}"
if [ "$ERROS" -gt 0 ]; then
    echo -e "${RED}❌ Erros: $ERROS${NC}"
fi
echo ""
echo -e "${BLUE}📁 Arquivos JSON salvos em: $OUTPUT_DIR${NC}"
echo ""

# Gerar relatório consolidado
echo -e "${BLUE}📊 Gerando relatório consolidado...${NC}"
RELATORIO_FILE="$OUTPUT_DIR/relatorio-consolidado.md"

cat > "$RELATORIO_FILE" << 'EOF'
# Relatório Consolidado — Alvenaria Thozen Electra

**Gerado em:** $(date '+%Y-%m-%d %H:%M:%S')  
**Fonte:** DXFs processados via `extrair_alvenaria_dxf.py`

---

## Quantitativos por Pavimento

| Pavimento | Área Total (m²) | Comprimento Total (m) | Arquivo JSON |
|-----------|-----------------|----------------------|--------------|
EOF

# Adicionar dados ao relatório (usando jq se disponível)
if command -v jq &> /dev/null; then
    for JSON_FILE in "$OUTPUT_DIR"/*.json; do
        if [ -f "$JSON_FILE" ]; then
            PAVIMENTO=$(jq -r '.pavimento' "$JSON_FILE")
            AREA=$(jq -r '.area_total' "$JSON_FILE")
            COMPRIMENTO=$(jq -r '.comprimento_total' "$JSON_FILE")
            FILENAME=$(basename "$JSON_FILE")
            
            printf "| %s | %.2f | %.2f | %s |\n" "$PAVIMENTO" "$AREA" "$COMPRIMENTO" "$FILENAME" >> "$RELATORIO_FILE"
        fi
    done
else
    echo "| (Instale 'jq' para gerar tabela consolidada) | - | - | - |" >> "$RELATORIO_FILE"
fi

cat >> "$RELATORIO_FILE" << 'EOF'

---

## Próximos Passos

1. **Validar dados:** Verificar coerência entre pavimentos similares (G1~G5, Tipos)
2. **Calcular totais:** Multiplicar pavimento Tipo (08) por 24 repetições
3. **Preencher briefing:** Atualizar `executivo/thozen-electra/briefings/alvenaria-r00.md`
4. **Gerar planilha:** Executar `scripts/gerar_planilha_alvenaria.py`

---

**Gerado por:** `scripts/processar_todos_alvenaria.sh`
EOF

echo -e "${GREEN}✅ Relatório consolidado salvo em: $RELATORIO_FILE${NC}"
echo ""

# Exibir próximos passos
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  PRÓXIMOS PASSOS                                                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}1.${NC} Revisar os JSONs em: ${BLUE}$OUTPUT_DIR${NC}"
echo -e "${YELLOW}2.${NC} Validar quantitativos (comparar pavimentos similares)"
echo -e "${YELLOW}3.${NC} Atualizar briefing: ${BLUE}executivo/thozen-electra/briefings/alvenaria-r00.md${NC}"
echo -e "${YELLOW}4.${NC} Gerar planilha Excel: ${BLUE}scripts/gerar_planilha_alvenaria.py${NC}"
echo ""

exit 0
