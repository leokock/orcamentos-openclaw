#!/usr/bin/env python3.11
"""
Processa extração bruta de ar-condicionado e gera quantitativos organizados
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

def processar_extracao(arquivo_txt):
    """
    Processa arquivo de extração e organiza equipamentos por pavimento
    """
    
    print(f"📋 Processando: {arquivo_txt}\n")
    
    with open(arquivo_txt, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    # Estruturas para armazenar dados
    evaporadoras = defaultdict(list)
    condensadoras = defaultdict(list)
    
    # Padrão para extrair blocos de equipamentos
    # Exemplos:
    # "3x DALLO-  EVAPORADORA SPLIT - 9000 BTU-V184-ARC - LAZER (layer: M-EQPM-____-OTLN)"
    # "2x DALLO-CONDENSADORA SPLIT - 9_000 BTUs-V185-ARC - PAVIMENTOS TIPOS x24 (layer: M-EQPM-____-OTLN)"
    pattern = r'(\d+)x\s+DALLO-\s*-?\s*(EVAPORADORA|CONDENSADORA)\s+SPLIT\s+-\s+(\d+)[_,]?(\d+)?\s*BTU[s]?-[^-]+-ARC\s+-\s+([^(]+)'
    
    for match in re.finditer(pattern, conteudo, re.IGNORECASE):
        qtd = int(match.group(1))
        tipo = match.group(2).strip()
        potencia = match.group(3) + (match.group(4) if match.group(4) else "")
        pavimento = match.group(5).strip()
        
        item = {
            'tipo': tipo,
            'potencia_btu': int(potencia),
            'qtd': qtd,
            'pavimento': pavimento
        }
        
        if tipo.upper() == "EVAPORADORA":
            evaporadoras[pavimento].append(item)
        else:
            condensadoras[pavimento].append(item)
    
    # Imprimir resumo
    print("=" * 80)
    print("📊 QUANTITATIVOS DE AR-CONDICIONADO")
    print("=" * 80)
    
    # Processar evaporadoras
    print("\n### EVAPORADORAS (Unidades Internas)\n")
    
    total_evap = 0
    total_potencia_evap = 0
    
    pavimentos_ordem = ["TÉRREO", "GARAGEM 01", "LAZER", "1º PAVIMENTO TIPO", "PAVIMENTOS TIPOS x24"]
    
    for pav in pavimentos_ordem:
        if pav in evaporadoras:
            print(f"#### {pav}\n")
            print("| Equipamento | Potência (BTU/h) | UN | QTD | Observação |")
            print("|-------------|------------------|-----|-----|------------|")
            
            # Agrupar por potência
            por_potencia = defaultdict(int)
            for item in evaporadoras[pav]:
                por_potencia[item['potencia_btu']] += item['qtd']
            
            for potencia in sorted(por_potencia.keys()):
                qtd = por_potencia[potencia]
                print(f"| Evaporadora Split | {potencia:,} | un | {qtd} | {pav} |")
                total_evap += qtd
                total_potencia_evap += potencia * qtd
            
            print()
    
    print(f"**Total de evaporadoras:** {total_evap} unidades")
    print(f"**Potência total (evaporadoras):** {total_potencia_evap:,} BTU/h (~{total_potencia_evap/12000:.1f} TR)\n")
    
    # Processar condensadoras
    print("\n### CONDENSADORAS (Unidades Externas)\n")
    
    total_cond = 0
    total_potencia_cond = 0
    
    for pav in pavimentos_ordem:
        if pav in condensadoras:
            print(f"#### {pav}\n")
            print("| Equipamento | Potência (BTU/h) | UN | QTD | Observação |")
            print("|-------------|------------------|-----|-----|------------|")
            
            # Agrupar por potência
            por_potencia = defaultdict(int)
            for item in condensadoras[pav]:
                por_potencia[item['potencia_btu']] += item['qtd']
            
            for potencia in sorted(por_potencia.keys()):
                qtd = por_potencia[potencia]
                print(f"| Condensadora Split | {potencia:,} | un | {qtd} | {pav} |")
                total_cond += qtd
                total_potencia_cond += potencia * qtd
            
            print()
    
    print(f"**Total de condensadoras:** {total_cond} unidades")
    print(f"**Potência total (condensadoras):** {total_potencia_cond:,} BTU/h (~{total_potencia_cond/12000:.1f} TR)\n")
    
    # Resumo geral
    print("\n" + "=" * 80)
    print("📈 RESUMO GERAL")
    print("=" * 80)
    print(f"Evaporadoras:   {total_evap:3d} un  |  {total_potencia_evap:,} BTU/h")
    print(f"Condensadoras:  {total_cond:3d} un  |  {total_potencia_cond:,} BTU/h")
    print(f"\nPotência média por evaporadora: {total_potencia_evap/total_evap if total_evap > 0 else 0:,.0f} BTU/h")
    print(f"Potência média por condensadora: {total_potencia_cond/total_cond if total_cond > 0 else 0:,.0f} BTU/h")
    
    # Observações
    print("\n" + "=" * 80)
    print("⚠️  OBSERVAÇÕES")
    print("=" * 80)
    print("- Evaporadoras no pavimento tipo (×24): multiplicar quantidades por 24")
    print("- Tubulações frigoríficas: ainda não extraídas (layers específicos pendentes)")
    print("- Linhas de dreno: ainda não extraídas")
    print("- Instalações elétricas: ainda não extraídas")
    print("- Suportes e acessórios: estimativa baseada em quantidade de equipamentos")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 processar_quantitativo_ac.py <arquivo_extracao.txt>")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    
    if not Path(arquivo).exists():
        print(f"❌ Arquivo não encontrado: {arquivo}")
        sys.exit(1)
    
    processar_extracao(arquivo)
