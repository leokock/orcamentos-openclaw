#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
"""
Gerador de Orçamento Paramétrico — PARADOR AG7
Usando script base da Cartesian + dados extraídos do projeto
"""

import sys
import os

# Adicionar path do script base
sys.path.insert(0, '/Users/leokock/clawd/orcamento-parametrico/scripts')

# Importar módulo base
from gerar_template_dinamico import gerar_planilha

# ============================================================================
# DADOS DO PROJETO PARADOR AG7
# ============================================================================

ROZZO_DADOS = {
    "nome_projeto": "PARADOR - AG7",
    "cliente": "AG7 Empreendimentos",
    "data_base": "mar/2026",
    "localizacao": "Balneário Camboriú - SC (Estaleirinho)",
    
    # Dados essenciais
    "AC": 21240,  # m² — ESTIMADA (18.000 privativa + 3.240 áreas comuns)
    "UR": 36,     # unidades
    "NP": 4,      # pavimentos (SS, TER, N01, Duplex/Rooftop)
    "NPT": 1,     # pavimento tipo
    "ELEV": 7,    # elevadores
    "VAG": 173,   # vagas — ESTIMADA
    "AT": 10933.48,  # m² terreno
    
    # Dados importantes
    "NS": 1,      # subsolos
    "PRAZO": 24,  # meses
    "N_BLOCOS": 7,  # blocos A-G
    
    # CUB
    "CUB_BASE": 2752.67,  # dez/23 (base calibração)
    "CUB": 3100.00,  # mar/26 — ESTIMADO (atualização ~12,6% aa) — campo usado pelo script
    "CUB_ATUAL": 3100.00,  # mar/26 — ESTIMADO (atualização ~12,6% aa)
}

ROZZO_BRIEFING = {
    # Alto Impacto
    "Q1_fundacao": "Hélice Contínua",  # Blocos (estacas + blocos) → aproximado como hélice
    "Q2_laje": "Convencional",  # 20 cm com vigas
    "Q3_contencao": "Cortina",  # 1 subsolo, terreno declive
    "Q4_subsolos": 1,
    "Q5_padrao": "Super Alto",  # Certificações triplas + automação premium
    
    # Médio Impacto
    "Q6_esquadria": "Alto Desempenho",  # Tratamento acústico completo
    "Q7_piso": "Porcelanato Premium",  # Pedra 3 cm
    "Q8_vedacao": "Misto",  # Alvenaria + paredes duplas acústicas
    "Q9_forro": "Gesso Negativo",  # Gesso + GLASROC
    "Q10_fachada": "Misto",  # Textura + concreto aparente pigmentado
    "Q11_mo_fachada": "Empreitada",  # Padrão alto
    "Q12_cobertura": "Completa",  # Rooftop com lazer
    "Q13_aquecimento": "Bomba Calor",  # Múltiplo (gás + bomba + piso)
    "Q14_automacao": "Premium",  # Bowers & Wilkins + completo
    "Q15_energia": "Sem",  # Não mencionado solar
    "Q16_lazer": "Premium",  # Piscinas + spa + academia completa
    "Q17_paisagismo": "Premium",  # GBC Biodiversidade
    "Q18_mobiliario": "Completo",  # Salões decorados
    "Q19_prazo": 24,  # meses
    "Q20_regiao": "Litoral SC",
    
    # Infraestrutura Técnica
    "Q21_gerador": "Sim",  # Dimensionado conforto
    "Q22_subestacao": "Sim",  # Carregadores 7,4 kW/apto
    "Q23_solar": "Não",
    "Q24_carro_eletrico": "Sim",  # 1 carregador 7,4 kW por apto
    "Q25_pressurizacao": "Sim",  # GBC + Fitwell + NBR 15575
}

# ============================================================================
# GERAÇÃO
# ============================================================================

if __name__ == "__main__":
    output_path = "/Users/leokock/clawd/tmp/parador-ag7/PARADOR-AG7-parametrico-v1.xlsx"
    
    print("🏗️  Gerando orçamento paramétrico — PARADOR AG7")
    print(f"   AC: {ROZZO_DADOS['AC']:,.0f} m² (ESTIMADA)")
    print(f"   Padrão: {ROZZO_BRIEFING['Q5_padrao']}")
    print(f"   CUB Base: R$ {ROZZO_DADOS['CUB_BASE']:.2f}/m² (dez/23)")
    print(f"   CUB Atual: R$ {ROZZO_DADOS['CUB_ATUAL']:.2f}/m² (mar/26)")
    print()
    
    # Gerar planilha
    try:
        gerar_planilha(
            output_path=output_path,
            dados_projeto=ROZZO_DADOS,
            briefing_respostas=ROZZO_BRIEFING
        )
        
        print(f"✅ Planilha gerada: {output_path}")
        print()
        print("📋 Próximos passos:")
        print("   1. Validar AC confirmada (atualmente ESTIMADA em 21.240 m²)")
        print("   2. Validar vagas confirmadas (atualmente ESTIMADA em 173)")
        print("   3. Atualizar CUB mar/2026 (atualmente ESTIMADO)")
        print("   4. Revisar briefing se necessário")
        
    except Exception as e:
        print(f"❌ Erro ao gerar planilha: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
