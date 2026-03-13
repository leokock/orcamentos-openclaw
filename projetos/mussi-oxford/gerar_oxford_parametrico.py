#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico - OXFORD (Mussi Empreendimentos)
Data: 12/03/2026
"""

import sys
import os
from datetime import datetime

# Adiciona o diretório scripts ao path
sys.path.insert(0, '/Users/leokock/orcamentos/scripts')

from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO OXFORD
# ============================================================================

OXFORD_DADOS = {
    "Nome": "Edifício Oxford — Mussi Empreendimentos",
    "Código": "OXFORD-MUSSI",
    "Cidade": "Itajaí/SC",
    "AC": 7500.00,  # ⚠️ ESTIMADO (confirmar com cliente)
    "UR": 95,  # Estimativa média: ~95 unidades (17 tipo × 5-6 un/pav + 1 ático)
    "UC": 2,  # Salas comerciais no térreo
    "NP": 27,  # Térreo + G2-G5 + Lazer + 17 tipo + Ático + 3 técnicos
    "NPT": 17,  # 7º ao 23º pavimento
    "NPG": 5,  # G1 (térreo) + G2-G5
    "ELEV": 2,  # Estimado (caixas identificadas nas plantas)
    "VAG": 136,  # G1=25, G3=37, G4=37, G5=37
    "AT": 1200.00,  # ⚠️ ESTIMADO (confirmar com cliente)
    "NS": 0,  # Sem subsolo (garagem acima do terreno)
    "Prazo": 36,  # Estimado para 27 pavimentos
    "CUB": 3050.00  # CUB/SC R8N março/2026 (⚠️ CONFIRMAR valor exato)
}

# ============================================================================
# BRIEFING OXFORD (25 PERGUNTAS)
# ============================================================================

OXFORD_BRIEFING = {
    "Q1": "Hélice Contínua",  # Fundação (padrão regional)
    "Q2": "Cubetas",  # Laje (padrão, não confirmado)
    "Q3": "Não",  # Contenção (terreno aparentemente plano)
    "Q4": "0",  # Subsolos (confirmado — garagem acima do solo)
    "Q5": "Alto",  # Padrão (localização, programa, indicadores)
    "Q6": "Pintura eletrostática",  # Esquadria (compatível com alto padrão)
    "Q7": "Porcelanato padrão",  # Piso (alto padrão)
    "Q8": "Misto",  # Vedação (alvenaria + drywall)
    "Q9": "Gesso liso",  # Forro (padrão alto)
    "Q10": "Misto",  # Fachada (textura + brise + elementos especiais)
    "Q11": "Empreitada",  # MO Fachada (elementos especiais demandam especialização)
    "Q12": "Completa",  # Cobertura habitável (penthouse 114m²)
    "Q13": "Gás individual",  # Aquecimento (padrão SC)
    "Q14": "Básico",  # Automação (infraestrutura padrão)
    "Q15": "Sem",  # Energia solar (não identificado)
    "Q16": "Completo",  # Lazer (piscina, fitness, coworking, etc — confirmado)
    "Q17": "Básico",  # Paisagismo (jardins térreo + lazer)
    "Q18": "Básico",  # Mobiliário (áreas comuns)
    "Q19": "36",  # Prazo (36 meses — estimado)
    "Q20": "Litoral SC",  # Região (Itajaí/SC)
    "Q21": "Sim",  # Gerador (provável para 27 pavimentos)
    "Q22": "Sim",  # Subestação (carga elevada — estimado)
    "Q23": "Não",  # Fotovoltaicas (não identificado)
    "Q24": "Não",  # Carro elétrico (não especificado)
    "Q25": "Sim"   # Pressurização escada (obrigatória para altura >60m)
}

# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("GERADOR DE ORÇAMENTO PARAMÉTRICO — OXFORD (MUSSI)")
    print("=" * 80)
    print()
    print("Projeto: Edifício Oxford")
    print("Cliente: Mussi Empreendimentos")
    print("Localização: Rua Uruguai / Rua Imbituba, Centro, Itajaí/SC")
    print("Data: 12/03/2026")
    print()
    print("=" * 80)
    print()
    
    # Define caminho de saída
    output_dir = "/Users/leokock/orcamentos/projetos/mussi-oxford"
    os.makedirs(output_dir, exist_ok=True)
    
    # Nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    output_filename = f"OXFORD-Orcamento-Parametrico-{timestamp}.xlsx"
    output_path = os.path.join(output_dir, output_filename)
    
    # Caminho para calibration-stats.json
    calibration_stats_path = "/Users/leokock/orcamentos/parametrico/calibration-stats.json"
    
    print(f"Gerando: {output_filename}")
    print()
    
    # Gera a planilha
    try:
        gerar_planilha(
            output_path=output_path,
            dados_projeto=OXFORD_DADOS,
            briefing_respostas=OXFORD_BRIEFING,
            calibration_stats_path=calibration_stats_path
        )
        
        print()
        print("=" * 80)
        print("✓ ORÇAMENTO PARAMÉTRICO GERADO COM SUCESSO!")
        print("=" * 80)
        print()
        print(f"Arquivo salvo em:")
        print(f"  {output_path}")
        print()
        print("⚠️  OBSERVAÇÕES IMPORTANTES:")
        print()
        print("  1. ÁREA CONSTRUÍDA (7.500 m²) = ESTIMADA")
        print("     → Confirmar com quadro de áreas oficial do projeto")
        print()
        print("  2. ÁREA TERRENO (1.200 m²) = ESTIMADA")
        print("     → Confirmar com projeto de implantação ou escritura")
        print()
        print("  3. CUB MARÇO/2026 (R$ 3.050,00/m²) = VALOR APROXIMADO")
        print("     → Confirmar CUB/SC R8N oficial de março/2026")
        print()
        print("  4. TIPO DE LAJE (Cubetas) = NÃO CONFIRMADO")
        print("     → Validar com projeto estrutural")
        print()
        print("  5. PADRÃO DE ACABAMENTO (Alto) = ESTIMADO")
        print("     → Confirmar com memorial descritivo e tabela de acabamentos")
        print()
        print("=" * 80)
        print()
        print("PRÓXIMOS PASSOS:")
        print()
        print("  1. Validar dados estimados com o cliente Mussi")
        print("  2. Verificar alertas na aba ALERTAS da planilha")
        print("  3. Revisar premissas do briefing conforme memorial descritivo")
        print("  4. Apresentar orçamento ao cliente para aprovação")
        print()
        print("=" * 80)
        
    except Exception as e:
        print()
        print("=" * 80)
        print("✗ ERRO AO GERAR ORÇAMENTO")
        print("=" * 80)
        print()
        print(f"Erro: {str(e)}")
        print()
        import traceback
        traceback.print_exc()
        print()
        print("=" * 80)
        sys.exit(1)
