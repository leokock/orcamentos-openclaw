#!/usr/bin/env python3.11
"""Gerar Armínio Tavares com prazo de 42 meses para teste"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from gerar_arminio_tavares import ARMINIO_DADOS, ARMINIO_BRIEFING
from gerar_template_dinamico import gerar_planilha

# Alterar prazo para 42 meses
ARMINIO_BRIEFING["Q19"] = "42"
ARMINIO_DADOS["Prazo"] = 42

output_dir = Path(__file__).parent.parent / "projetos" / "arminio-tavares"
output_path = output_dir / "orcamento-parametrico-arminio-42meses-TESTE.xlsx"
calibration_stats_path = Path(__file__).parent.parent / "calibration-stats.json"

print("Gerando versão TESTE com prazo de 42 meses...")
gerar_planilha(
    output_path=str(output_path),
    dados_projeto=ARMINIO_DADOS,
    briefing_respostas=ARMINIO_BRIEFING,
    calibration_stats_path=str(calibration_stats_path) if calibration_stats_path.exists() else None
)
print(f"✓ Gerado: {output_path}")
print(f"\nNesta versão Q19 já está em '42' meses.")
print(f"Compare o custo de Gerenciamento com a versão de 30 meses.")
print(f"ESPERADO: ~31% maior (fator 1.15 vs 0.88)")
