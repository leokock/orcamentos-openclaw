#!/usr/bin/env python3.11
"""
Debug - Verifica se a fórmula de Prazo (Q19) está afetando Gerenciamento
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gerar_template_dinamico import BRIEFING, gerar_formula_ifs

# Encontrar Q19 (Prazo)
q19_idx = None
for idx, q in enumerate(BRIEFING):
    if q["num"] == "Q19":
        q19_idx = idx
        print(f"Q19 encontrada no índice {idx}")
        print(f"Pergunta: {q['pergunta']}")
        print(f"Opções: {q['opcoes']}")
        print(f"Afeta: {q['afeta']}")
        print(f"Fatores Gerenciamento: {q['fatores'].get('Gerenciamento', {})}")
        break

if q19_idx is None:
    print("ERRO: Q19 não encontrada!")
    sys.exit(1)

print("\n" + "="*70)
print("FÓRMULA GERADA PARA GERENCIAMENTO × Q19:")
print("="*70)

formula = gerar_formula_ifs("Gerenciamento", q19_idx)
print(formula)

print("\n" + "="*70)
print("INTERPRETAÇÃO:")
print("="*70)
print("Esta fórmula deveria retornar:")
print("  • 0.60 se BRIEFING!C21 = '18'")
print("  • 0.75 se BRIEFING!C21 = '24'")
print("  • 0.88 se BRIEFING!C21 = '30'")
print("  • 1.00 se BRIEFING!C21 = '36'")
print("  • 1.15 se BRIEFING!C21 = '42'  ← MUDANÇA ESPERADA")
print("  • 1.30 se BRIEFING!C21 = '48'")
print("\nSe ao mudar Q19 de '30' para '42' o fator NÃO mudou de 0.88 para 1.15,")
print("então há um problema na planilha Excel gerada (não no script Python).")
print("\n" + "="*70)
print("SOLUÇÃO:")
print("="*70)
print("1. Abra a planilha no Excel/LibreOffice")
print("2. Vá para a aba FATORES")
print("3. Localize a linha 'Gerenciamento' (linha 3)")
print("4. Localize a coluna Q19 (coluna T - 20ª coluna)")
print("5. Verifique se a célula T3 contém a fórmula acima")
print("6. Se SIM → o problema está na propagação do cálculo")
print("7. Se NÃO → regere a planilha com o script atualizado")
print("\n8. Para forçar recálculo: CTRL+ALT+F9 (Excel) ou CTRL+SHIFT+F9 (LibreOffice)")
