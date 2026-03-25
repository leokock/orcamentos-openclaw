#!/usr/bin/env python3
"""
Calibra índices de consumo para que Bottom-Up (Qtd × PU) bata com medianas dos 75 projetos.
Para cada macrogrupo: Target R$/m² → distribuir em itens com PUs reais → calcular índices.
"""

AC = 13200
CUB_ATUAL = 3028.45
CUB_BASE = 2752.67
FATOR_CUB = CUB_ATUAL / CUB_BASE

# Medianas dos 75 projetos (R$/m², base dez/23) × fator CUB × briefing
# Target = mediana × fator_cub × briefing × AC

def calibrar_macrogrupo(mg_name, target_rsm2, items_with_pus):
    """
    items_with_pus: list of (nome, pu, unidade, peso_pct)
    peso_pct: quanto desse item representa do total (soma = 1.0)
    Retorna items com qtd e total calibrados.
    """
    target_total = target_rsm2 * AC
    result = []
    for nome, pu, unidade, peso in items_with_pus:
        valor = target_total * peso
        qtd = round(valor / pu, 1) if pu > 0 else 0
        indice = round(qtd / AC, 4) if AC > 0 else 0
        result.append({
            'nome': nome,
            'pu': pu,
            'unidade': unidade,
            'qtd': qtd,
            'total': round(valor),
            'indice': indice,
            'indice_desc': f"{indice} {unidade}/m² AC",
        })
    return result

# ============================================================================
# CALIBRAÇÃO POR MACROGRUPO
# ============================================================================

print("CALIBRAÇÃO DE ÍNDICES — NOW RESIDENCE\n")
print(f"AC: {AC} m² | CUB: R$ {CUB_ATUAL}\n")

all_calibrated = {}

# --- GERENCIAMENTO (target ~452 R$/m²) ---
ger_target = 410.70 * FATOR_CUB * 1.00  # briefing 1.0
ger_items = [
    ("Projetos (arq+compl+compat)", 450000/AC, "R$/m²", 0.15),
    ("Consultorias e ATP", 120000/AC, "R$/m²", 0.04),
    ("Ensaios e controle tecnol.", 90000/AC, "R$/m²", 0.03),
    ("Taxas, licenças e seguros", 310000/AC, "R$/m²", 0.10),
    ("Engenheiro residente (PJ)", 14000, "mês", 0.07),
    ("Mestre de obras", 9000, "mês", 0.05),
    ("Encarregado", 5500, "mês", 0.02),
    ("Estagiário", 2000, "mês", 0.01),
    ("Técnico segurança", 6000, "mês", 0.03),
    ("Almoxarife", 3500, "mês", 0.015),
    ("Equipe limpeza", 3000, "mês", 0.01),
    ("EPCs (fixo porte médio)", 300000/AC, "R$/m²", 0.05),
    ("Meio ambiente + licenças amb.", 35000/AC, "R$/m²", 0.01),
    ("Operação inicial / mobilização", 45000/AC, "R$/m²", 0.015),
    ("Inst. provisórias (canteiro)", 120000/AC, "R$/m²", 0.04),
    ("Despesas consumo (água+energia)", 8000, "mês", 0.04),
    ("Equipamentos (grua+elev obra)", 350000/AC, "R$/m²", 0.12),
    ("Despesas diversas", 1, "R$/m²", 0.14),  # residual
]
all_calibrated['Gerenciamento'] = calibrar_macrogrupo("Gerenciamento", ger_target, ger_items)

# --- INFRAESTRUTURA (target ~186 R$/m², sem contenção) ---
infra_target = 198.74 * FATOR_CUB * 0.85  # sem contenção
infra_items = [
    ("Perfuração hélice Ø40cm", 50, "m", 0.20),
    ("Concreto estacas fck30", 632, "m³", 0.18),
    ("Concreto blocos/baldrames fck30", 590, "m³", 0.12),
    ("Aço CA-50 fundação", 8.38, "kg", 0.18),
    ("Forma blocos/baldrames", 45.64, "m²", 0.08),
    ("MO fundação (empreitada)", 1, "R$/m²", 0.15),
    ("Mobilização estaqueiro", 1, "R$/m²", 0.05),
    ("Arrasamento estacas", 1, "R$/m²", 0.04),
]
all_calibrated['Infraestrutura'] = calibrar_macrogrupo("Infraestrutura", infra_target, infra_items)

# --- ALVENARIA (target ~146 R$/m²) ---
alv_target = 147.73 * FATOR_CUB * 0.90
alv_items = [
    ("Bloco cerâmico 14cm (vedação)", 32.95, "m²", 0.22),
    ("Drywall ST (paredes internas)", 156, "m²", 0.18),
    ("Drywall RU (áreas molhadas)", 195, "m²", 0.06),
    ("Argamassa assentamento", 3.80, "m²", 0.04),
    ("Vergas e contravergas", 33.33, "m", 0.06),
    ("Telas ligação alv-estrutura", 3.10, "un", 0.02),
    ("Encunhamento", 2.35, "m", 0.02),
    ("MO alvenaria (empreitada)", 28.50, "m²", 0.28),
    ("MO drywall", 45, "m²", 0.08),
    ("Chapisco rolado", 5.50, "m²", 0.04),
]
all_calibrated['Alvenaria'] = calibrar_macrogrupo("Alvenaria", alv_target, alv_items)

# --- IMPERMEABILIZAÇÃO (target ~57 R$/m²) ---
imp_target = 54.90 * FATOR_CUB * 0.95
imp_items = [
    ("Manta asfáltica 4mm (material)", 82.11, "m²", 0.32),
    ("Argamassa polimérica (bwc)", 8.50, "m²", 0.05),
    ("Regularização superfície", 5.57, "m²", 0.04),
    ("Impermeabilização peitoris", 15.30, "m²", 0.03),
    ("Proteção mecânica", 25, "m²", 0.06),
    ("MO impermeabilização", 68, "m²", 0.35),
    ("MO regularização", 19.50, "m²", 0.10),
    ("Materiais complementares", 1, "R$/m²", 0.05),
]
all_calibrated['Impermeabilização'] = calibrar_macrogrupo("Impermeabilização", imp_target, imp_items)

# --- SIST. ESPECIAIS (target ~161 R$/m²) ---
esp_target = 162.20 * FATOR_CUB * 0.90
esp_items = [
    ("Elevador social (2un)", 192450, "un", 0.24),
    ("Elevador serviço (1un)", 96000, "un", 0.06),
    ("Gerador ~150kVA", 180000, "vb", 0.11),
    ("Automação predial", 80000, "vb", 0.05),
    ("Piscina (estrutura+equip)", 180000, "vb", 0.11),
    ("CFTV / segurança", 80000, "vb", 0.05),
    ("Pressurização escada", 60000, "vb", 0.04),
    ("Para-raios / SPDA", 35000, "vb", 0.02),
    ("Interfonia / controle acesso", 90000, "vb", 0.06),
    ("MO instalação sist. especiais", 1, "R$/m²", 0.26),
]
all_calibrated['Sist. Especiais'] = calibrar_macrogrupo("Sist. Especiais", esp_target, esp_items)

# --- REV. INT. PAREDE (target ~167 R$/m²) ---
rev_target = 159.32 * FATOR_CUB * 0.95
rev_items = [
    ("Reboco interno massa única", 7.00, "m²", 0.08),
    ("Chapisco rolado interno", 5.50, "m²", 0.04),
    ("Cerâmica parede bwc (30×60)", 48, "m²", 0.16),
    ("Cerâmica parede cozinha", 42, "m²", 0.06),
    ("Porcelanato parede áreas comuns", 85, "m²", 0.05),
    ("Argamassa colante AC-II", 12, "m²", 0.04),
    ("Rejunte", 5, "m²", 0.02),
    ("MO reboco (empreitada)", 22.50, "m²", 0.22),
    ("MO assentamento cerâmica", 35, "m²", 0.20),
    ("Materiais complementares", 1, "R$/m²", 0.13),
]
all_calibrated['Rev. Int. Parede'] = calibrar_macrogrupo("Rev. Int. Parede", rev_target, rev_items)

# --- TETO (target ~67 R$/m²) ---
teto_target = 61.11 * FATOR_CUB * 1.00
teto_items = [
    ("Forro gesso acartonado ST", 28, "m²", 0.35),
    ("Forro gesso acartonado RU (bwc)", 35, "m²", 0.08),
    ("Perfis metálicos (estrutura forro)", 15, "m²", 0.15),
    ("MO forro (empreitada)", 25, "m²", 0.30),
    ("Forro mineral (garagem)", 45, "m²", 0.05),
    ("Sanca/tabica gesso", 35, "m", 0.07),
]
all_calibrated['Teto'] = calibrar_macrogrupo("Teto", teto_target, teto_items)

# --- PISOS (target ~189 R$/m²) ---
pisos_target = 181.16 * FATOR_CUB * 0.95
pisos_items = [
    ("Contrapiso autonivelante", 12.10, "m²", 0.06),
    ("Porcelanato 60×60 (comuns)", 81.21, "m²", 0.14),
    ("Laminado/vinílico (aptos)", 65, "m²", 0.14),
    ("Piso cimentado (garagem)", 32, "m²", 0.04),
    ("Piso epóxi (garagem)", 26.17, "m²", 0.04),
    ("Granito/mármore (hall)", 180, "m²", 0.03),
    ("Soleira granito", 120, "m", 0.03),
    ("Rodapé poliestireno", 10.77, "m", 0.04),
    ("Argamassa colante AC-II", 12, "m²", 0.03),
    ("MO contrapiso", 18, "m²", 0.08),
    ("MO assentamento pisos", 32, "m²", 0.18),
    ("MO rodapé", 8.40, "m", 0.04),
    ("Nivelamento laser", 8, "m²", 0.03),
    ("Materiais complementares", 1, "R$/m²", 0.12),
]
all_calibrated['Pisos'] = calibrar_macrogrupo("Pisos", pisos_target, pisos_items)

# --- PINTURA (target ~142 R$/m²) ---
pintura_target = 128.87 * FATOR_CUB * 1.00
pintura_items = [
    ("Massa PVA (paredes 2 demãos)", 4.29, "m²", 0.06),
    ("Massa PVA (teto 2 demãos)", 4.29, "m²", 0.03),
    ("Tinta acrílica paredes (3 demãos)", 5.40, "m²", 0.08),
    ("Tinta acrílica teto (2 demãos)", 3.83, "m²", 0.03),
    ("Selador acrílico", 2.50, "m²", 0.03),
    ("Textura rolada (áreas comuns)", 12, "m²", 0.04),
    ("Pintura epóxi piso (garagem)", 26.17, "m²", 0.04),
    ("MO pintura (empreitada)", 15, "m²", 0.40),
    ("MO lixamento/preparação", 8, "m²", 0.15),
    ("Fundo preparador", 3, "m²", 0.02),
    ("Materiais diversos (fitas, lonas)", 1, "R$/m²", 0.12),
]
all_calibrated['Pintura'] = calibrar_macrogrupo("Pintura", pintura_target, pintura_items)

# --- FACHADA (target ~121 R$/m²) ---
fachada_target = 128.96 * FATOR_CUB * 0.85  # textura simples
fachada_items = [
    ("Reboco externo", 15.25, "m²", 0.14),
    ("Textura acrílica fachada", 12, "m²", 0.08),
    ("Pintura acrílica externa (2 demãos)", 8, "m²", 0.06),
    ("Cerâmica fachada (detalhes)", 55, "m²", 0.05),
    ("Selante/junta dilatação", 25, "m", 0.03),
    ("Rufos e pingadeiras", 35, "m", 0.03),
    ("MO reboco externo (empreitada)", 22, "m²", 0.18),
    ("MO pintura fachada", 15, "m²", 0.10),
    ("Balancim/andaime fachadeiro", 18, "m²", 0.15),
    ("Tela fachada (proteção)", 8, "m²", 0.05),
    ("Materiais complementares", 1, "R$/m²", 0.13),
]
all_calibrated['Fachada'] = calibrar_macrogrupo("Fachada", fachada_target, fachada_items)

# --- COMPLEMENTARES (target ~167 R$/m²) ---
comp_target = 168.78 * FATOR_CUB * 0.90
comp_items = [
    ("Paisagismo", 120000, "vb", 0.07),
    ("Mobiliário áreas comuns", 250000, "vb", 0.15),
    ("Decoração halls/lobby", 80000, "vb", 0.05),
    ("Limpeza final pós-obra", 45000, "vb", 0.03),
    ("Ligações definitivas (água+energia)", 60000, "vb", 0.04),
    ("Calçadas e pavimentação externa", 80, "m²", 0.06),
    ("Drenagem/infraestrutura externa", 1, "R$/m²", 0.08),
    ("Cobertura/telhado", 95, "m²", 0.10),
    ("Muro/gradil/portaria", 1, "R$/m²", 0.10),
    ("Diversos (placas, numeração, etc)", 1, "R$/m²", 0.12),
    ("MO serviços complementares", 1, "R$/m²", 0.20),
]
all_calibrated['Complementares'] = calibrar_macrogrupo("Complementares", comp_target, comp_items)

# ============================================================================
# PRINT RESULTADO
# ============================================================================
print("=" * 90)
for mg_name, items in all_calibrated.items():
    total = sum(it['total'] for it in items)
    rsm2 = total / AC
    print(f"\n{'='*80}")
    print(f"{mg_name}: R$ {rsm2:,.0f}/m² | Total: R$ {total:,.0f}")
    print(f"{'='*80}")
    print(f"{'Item':<40} {'Qtd':>8} {'Un':>5} {'PU':>10} {'Total':>12} {'Índice':>12}")
    print("-" * 90)
    for it in items:
        print(f"{it['nome']:<40} {it['qtd']:>8,.0f} {it['unidade']:>5} {it['pu']:>10,.2f} {it['total']:>12,} {it['indice_desc']:>12}")
    print(f"{'TOTAL':<40} {'':>8} {'':>5} {'':>10} {total:>12,}")

# Summary
print(f"\n\n{'='*60}")
print("RESUMO — TODOS OS MACROGRUPOS CALIBRADOS")
print(f"{'='*60}")
grand_total = 0
for mg_name, items in all_calibrated.items():
    total = sum(it['total'] for it in items)
    rsm2 = total / AC
    grand_total += total
    print(f"{mg_name:<25} R$ {rsm2:>6,.0f}/m²  Total: R$ {total:>12,}")
print(f"{'TOTAL CALIBRADO':<25} R$ {grand_total/AC:>6,.0f}/m²  Total: R$ {grand_total:>12,}")
PYEOF