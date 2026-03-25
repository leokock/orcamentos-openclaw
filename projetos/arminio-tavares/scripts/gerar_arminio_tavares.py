#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - Armínio Tavares
Usa os dados do briefing atualizado (incluindo hidrossanitário) para gerar planilha
"""

import sys
import os
from pathlib import Path

# Importar o gerador principal
sys.path.insert(0, str(Path(__file__).parent))
from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO ARMÍNIO TAVARES
# ============================================================================

ARMINIO_DADOS = {
    "Nome": "Edifício Armínio Tavares — PLACON",
    "Código": "ARQ 24.027",
    "Cidade": "Florianópolis/SC",
    "AC": 7996.45,      # Área Construída Total (IFC)
    "UR": 45,           # Unidades Residenciais
    "UC": 0,            # Unidades Comerciais
    "NP": 16,           # Número de Pavimentos (2º ao 16º + térreo)
    "NPT": 15,          # Pavimentos Tipo (excluindo subsolo, térreo, técnicos)
    "NPG": 2,           # Níveis de Garagem (2 subsolos)
    "ELEV": 2,          # Elevadores (estimado)
    "VAG": 50,          # Vagas de garagem (estimado)
    "AT": 486.40,       # Área do Terreno
    "NS": 2,            # Número de Subsolos
    "Prazo": 30,        # Prazo estimado (meses)
    "CUB": 3050.00      # CUB SC (atualizado)
}

ARMINIO_BRIEFING = {
    "Q1": "Hélice Contínua",         # Fundação (padrão Floripa centro)
    "Q2": "Cortina concreto",        # Contenção
    "Q3": "Sim",                     # Subsolo (2 níveis)
    "Q4": "2",                       # Número de subsolos
    "Q5": "Standard",                # Estrutura
    "Q6": "Alumínio anodizado",      # Esquadrias
    "Q7": "Porcelanato padrão",      # Piso
    "Q8": "Alvenaria",               # Vedação
    "Q9": "Gesso liso",              # Forro
    "Q10": "Textura + pintura",      # Fachada
    "Q11": "Empreitada",             # Gestão
    "Q12": "Sim",                    # Barramento blindado (elétrico)
    "Q13": "Gás individual",         # Gás
    "Q14": "Básico",                 # Automação
    "Q15": "Sem",                    # Climatização
    "Q16": "Completo",               # Instalações hidrossanitárias (DADOS IFC)
    "Q17": "Médio",                  # Acabamento (padrão PLACON)
    "Q18": "Básico",                 # Paisagismo
    "Q19": "30",                     # Prazo (meses)
    "Q20": "Centro Fpolis",          # Localização
    "Q21": "Sim",                    # SPDA/Para-raios
    "Q22": "Não",                    # Fachada especial
    "Q23": "Não",                    # Piscina (a confirmar)
    "Q24": "Sim",                    # Salão de festas (térreo amplo)
    "Q25": "Não"                     # Heliponto
}

# ============================================================================
# GERAÇÃO
# ============================================================================

if __name__ == '__main__':
    output_dir = Path(__file__).parent.parent / "projetos" / "arminio-tavares"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "orcamento-parametrico-arminio-tavares-v2.xlsx"
    calibration_stats_path = Path(__file__).parent.parent / "calibration-stats.json"
    
    print("="*70)
    print("GERADOR DE ORÇAMENTO PARAMÉTRICO - ARMÍNIO TAVARES")
    print("="*70)
    print(f"\nProjeto: {ARMINIO_DADOS['Nome']}")
    print(f"Código: {ARMINIO_DADOS['Código']}")
    print(f"Área Construída: {ARMINIO_DADOS['AC']:,.2f} m²")
    print(f"Unidades: {ARMINIO_DADOS['UR']}")
    print(f"Pavimentos: {ARMINIO_DADOS['NP']}")
    print(f"Subsolos: {ARMINIO_DADOS['NS']}")
    print(f"\nIncluindo dados hidrossanitários extraídos do IFC:")
    print(f"  • 425 pontos hidráulicos (9,4 pts/un)")
    print(f"  • 2.400 m de tubulação (0,30 ml/m²)")
    print(f"  • 430 conexões")
    print(f"  • 304 equipamentos sanitários")
    print(f"  • 200 registros/válvulas")
    print(f"  • 4 reservatórios")
    print(f"\nGerando planilha...")
    
    try:
        gerar_planilha(
            output_path=str(output_path),
            dados_projeto=ARMINIO_DADOS,
            briefing_respostas=ARMINIO_BRIEFING,
            calibration_stats_path=str(calibration_stats_path) if calibration_stats_path.exists() else None
        )
        
        print(f"✓ Planilha gerada com sucesso!")
        print(f"\nArquivo: {output_path}")
        print(f"Tamanho: {output_path.stat().st_size / 1024:.1f} KB")
        print("\n" + "="*70)
        print("PRÓXIMOS PASSOS:")
        print("  1. Abrir planilha no Excel/LibreOffice")
        print("  2. Revisar valores calculados")
        print("  3. Ajustar briefing se necessário")
        print("  4. Comparar com projetos similares (Catena, Connect)")
        print("="*70)
        
    except Exception as e:
        print(f"✗ ERRO ao gerar planilha: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
