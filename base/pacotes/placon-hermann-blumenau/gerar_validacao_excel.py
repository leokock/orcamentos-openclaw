# -*- coding: utf-8 -*-
"""
Gera o workbook de Validação BIM × Paramétrico (ARQUITETURA) — Placon Hermann Blumenau.
Lê as quantidades reais do classificador (validar_bim_arquitetura) e monta:
  - PLACAR    : aderência por macrogrupo (qtd BIM × paramétrico, Δ%, confiança)
  - REPRICE   : reprice por macrogrupo (total atual × fator × total repreçado, Δ R$)
  - BIM_DETALHE: classificação completa do takeoff
  - PREMISSAS : decisões e premissas do Leo nesta validação
Paleta Cartesian V2. Escopo: só arquitetura (estrutura fica p/ revisão futura).
"""
import os, sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validar_bim_arquitetura as V

AC = V.AC
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "validacao-bim-arquitetura-hermann-v09.xlsx")

# Parede diafragma (substitui a contenção genérica de R$147k na Infraestrutura).
# Estimativa paramétrica — AJUSTAR com o quantitativo do projeto estrutural/orçamento de fundação.
PD_PERIM = 100.0   # m — perímetro contido (subsolo ~21x30 m)
PD_ALTURA = 8.0    # m — altura do painel (subsolo ~4 m + ficha)
PD_PU = 800.0      # R$/m² — parede diafragma (concreto + escavação + lama bentonítica, ~40 cm)
PAREDE_DIAFRAGMA = PD_PERIM * PD_ALTURA * PD_PU   # = 640.000
CONTENCAO_ATUAL = 147000.0
INFRA_TOTAL_ATUAL = 1228123.72

# ---- paleta Cartesian V2 ----
AZUL = "245AE4"; LARANJA = "FD3400"; PRETO = "111111"
CINZA_CLARO = "F4F4F4"; CINZA_MED = "E7E7E9"; BRANCO = "FFFFFF"
FONT = "Poppins"

thin = Side(style="thin", color=CINZA_MED)
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def hdr(cell, text, bg=AZUL, fg=BRANCO, size=10, align="center"):
    cell.value = text
    cell.font = Font(name=FONT, bold=True, color=fg, size=size)
    cell.fill = PatternFill("solid", fgColor=bg)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)
    cell.border = BORDER


def cel(cell, text, bold=False, fg=PRETO, bg=None, size=10, align="left", numfmt=None):
    cell.value = text
    cell.font = Font(name=FONT, bold=bold, color=fg, size=size)
    if bg:
        cell.fill = PatternFill("solid", fgColor=bg)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=False)
    cell.border = BORDER
    if numfmt:
        cell.number_format = numfmt


def titulo(ws, row, text, span):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1)
    c.value = text
    c.font = Font(name=FONT, bold=True, color=BRANCO, size=13)
    c.fill = PatternFill("solid", fgColor=PRETO)
    c.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[row].height = 24


# ============ 1. quantidades BIM (do classificador) ============
rows = V.load_solibri()
grp = defaultdict(lambda: defaultdict(float))
for r in rows:
    mg, sub, metric = V.classify(r)
    if mg is None:
        continue
    grp[mg][sub] += r["area"] if metric == "area" else (r["count"] if metric == "count" else 0)

# paredes de bloco revestidas (face logic) p/ revestimento
ext_face = int_part = 0.0
for r in rows:
    if r["bet"] == "External Walls" and r["type"].startswith("VED BCE") and "reboco" in r["mat"]:
        if "EXT" in r["type"] or "(EXT)" in r["mat"]:
            ext_face += r["area"]
        else:
            int_part += r["area"]
reb_int = int_part * 2 + ext_face            # revestimento interno (2x part + face int fachada)

# EA split
ea_lav = sum(r["area"] for r in rows if r["bet"] == "External Walls"
             and r["type"].startswith("EA ") and "LAVANDERIA" in r["type"])
ea_total = grp["ELEM_ARQ"]["elemento arq (EA)"]
ea_fach = ea_total - ea_lav

alv_bim = grp["ALVENARIA"]["alvenaria bloco (face externa)"] + grp["ALVENARIA"]["alvenaria bloco (interna)"] + ea_lav
forro_gesso = grp["TETO/FORRO"]["forro gesso"]
ripado = grp["TETO/FORRO"]["forro ripado madeira"]
piso_base = grp["PISOS"]["area-base laje elevada"] + grp["PISOS"]["area-base piso sobre solo (magro)"]
fach_bim = grp["FACHADA"]["parede concreto+revest externo"] + ext_face + grp["FACHADA"]["brise ripado madeira"] + ea_fach
pint_par = reb_int + ext_face + grp["FACHADA"]["parede concreto+revest externo"]  # ~ interno + face externa pintada

# ============ 2. dados paramétrico (lidos das abas) ============
PARAM_QTD = {
    "Alvenaria": 9654, "Rev. Int. Parede": 11367, "Teto/Forro": 5796,
    "Pisos (contrapiso)": 9993, "Fachada": 9111, "Pintura (paredes)": 18266,
    "Pintura (teto)": 6642, "Impermeabilização": 2645,
}
PARAM_TOTAL = {
    "Alvenaria": 1067218.50, "Rev. Int. Parede": 746551.70, "Teto/Forro": 426839.00,
    "Pisos": 1121985.15, "Esquadrias": 1910337.00, "Fachada": 1393983.00,
    "Pintura": 908984.40, "Impermeabilização": 470100.10,
}
RIPADO_PU = 180.0  # R$/m² estimado p/ forro ripado de madeira (premissa a confirmar)

# ============ 3. placar (qtd BIM × paramétrico) ============
# (macrogrupo, qtd_bim, un, qtd_param, confiança, status)
placar = [
    ("Alvenaria", alv_bim, "m²", PARAM_QTD["Alvenaria"], "Forte", "Qtd OK ±3% · 100% BLOCO confirmado (sem drywall em modelo/transcrições/Drive)"),
    ("Rev. Int. Parede", reb_int, "m²", PARAM_QTD["Rev. Int. Parede"], "Forte", "Validado (~1,5%) · split reboco×cerâmica é premissa"),
    ("Teto/Forro (gesso)", forro_gesso, "m²", PARAM_QTD["Teto/Forro"], "Forte", "Param ~9% alto"),
    ("Teto/Forro (ripado madeira)", ripado, "m²", 0, "Forte", "ITEM NOVO — paramétrico não previu (premium)"),
    ("Pisos (área-base)", piso_base, "m²", PARAM_QTD["Pisos (contrapiso)"], "Forte", "Real ~7% maior · acabamento de apto não modelado"),
    ("Esquadrias", 0, "—", 0, "Fraca", "Contagem BIM suja de componentes · precisa quadro de esquadrias"),
    ("Fachada", fach_bim, "m²", PARAM_QTD["Fachada"], "Média", "Param ~12% alto (c/ muretas EA) · confiar no BIM (decisão Leo)"),
    ("Pintura (paredes)", pint_par, "m²", PARAM_QTD["Pintura (paredes)"], "Forte", "Validado (~1%)"),
    ("Pintura (teto)", forro_gesso, "m²", PARAM_QTD["Pintura (teto)"], "Média", "Param ~25% alto"),
    ("Impermeabilização", 0, "—", PARAM_QTD["Impermeabilização"], "Nula", "Não modelado — manter paramétrico"),
]

# ============ 4. reprice por macrogrupo ============
def f(real, param):
    return real / param if param else 1.0

reprice = []  # (macro, total_atual, fator/driver, total_novo, nota)
# Alvenaria — 100% bloco cerâmico (confirmado: sem drywall). Reboco vai em Rev.parede.
ALV_PU_BLOCO = 32.95 + 3.80 + 28.50  # bloco + argamassa + MO assentamento = 65,25 R$/m²
ta = PARAM_TOTAL["Alvenaria"]; alv_novo = alv_bim * ALV_PU_BLOCO
reprice.append(("Alvenaria", ta, alv_novo/ta, alv_novo,
                f"100% bloco {alv_bim:.0f}m²×R${ALV_PU_BLOCO:.2f} (sem drywall — confirmado); reboco já em Rev.parede"))
# Rev parede
fr = f(reb_int, PARAM_QTD["Rev. Int. Parede"]); tr = PARAM_TOTAL["Rev. Int. Parede"]
reprice.append(("Rev. Int. Parede", tr, fr, tr*fr, "fator área revestida"))
# Teto: forro gesso scale + ripado add
ft = f(forro_gesso, PARAM_QTD["Teto/Forro"]); tt = PARAM_TOTAL["Teto/Forro"]
teto_novo = tt*ft + ripado*RIPADO_PU
reprice.append(("Teto/Forro", tt, ft, teto_novo, f"forro gesso ×{ft:.3f} + ripado {ripado:.0f}m²×R${RIPADO_PU:.0f} (PU estimado)"))
# Pisos: scale só contrapiso+MO contrapiso
contrapiso_lines = 120915.30 + 179874.00
fp = f(piso_base, PARAM_QTD["Pisos (contrapiso)"])
pisos_novo = (PARAM_TOTAL["Pisos"] - contrapiso_lines) + contrapiso_lines*fp
reprice.append(("Pisos", PARAM_TOTAL["Pisos"], fp, pisos_novo, f"só contrapiso+MO ×{fp:.3f}; acabamento apto mantido"))
# Esquadrias: keep
reprice.append(("Esquadrias", PARAM_TOTAL["Esquadrias"], 1.0, PARAM_TOTAL["Esquadrias"], "mantido — BIM não confiável p/ esquadria"))
# Fachada
ffa = f(fach_bim, PARAM_QTD["Fachada"]); tfa = PARAM_TOTAL["Fachada"]
reprice.append(("Fachada", tfa, ffa, tfa*ffa, "fator envelope BIM (decisão: confiar no BIM)"))
# Pintura: wall lines ×fator paredes; teto line ×fator teto
fpw = f(pint_par, PARAM_QTD["Pintura (paredes)"]); fpt = f(forro_gesso, PARAM_QTD["Pintura (teto)"])
teto_line = 25438.86
pint_novo = (PARAM_TOTAL["Pintura"] - teto_line)*fpw + teto_line*fpt
reprice.append(("Pintura", PARAM_TOTAL["Pintura"], fpw, pint_novo, f"paredes ×{fpw:.3f}; pintura teto ×{fpt:.3f}"))
# Imperm keep
reprice.append(("Impermeabilização", PARAM_TOTAL["Impermeabilização"], 1.0, PARAM_TOTAL["Impermeabilização"], "mantido — não modelado"))
# Infraestrutura — contenção genérica -> parede diafragma (confirmado proj. estrutural Lunardeli)
infra_novo = INFRA_TOTAL_ATUAL - CONTENCAO_ATUAL + PAREDE_DIAFRAGMA
reprice.append(("Infraestrutura (contenção)", INFRA_TOTAL_ATUAL, infra_novo/INFRA_TOTAL_ATUAL, infra_novo,
                f"contenção R${CONTENCAO_ATUAL:,.0f} -> PAREDE DIAFRAGMA R${PAREDE_DIAFRAGMA:,.0f} (estimativa {PD_PERIM:.0f}m x {PD_ALTURA:.0f}m x R${PD_PU:.0f}/m² — ajustar c/ proj. estrutural)"))
# Gerenciamento — projetos e equipamentos a preço de mercado (refino)
GER_ATUAL = 3634040.00; ger_novo = GER_ATUAL - 120000 - 80000  # projetos 500->380; grua 480->400
reprice.append(("Gerenciamento", GER_ATUAL, ger_novo/GER_ATUAL, ger_novo,
                "projetos R$500k->380k (mercado ~R$65/m²) + grua+cremalheira R$480k->400k (grua curta) = -R$200k; equipe mantida enxuta"))
# Instalações — indexada ao CUB; CUB real mai/26 (R$3.064,10 vs placeholder R$3.100)
INST_ATUAL = 2255138.13; inst_novo = 2229040.00
reprice.append(("Instalações", INST_ATUAL, inst_novo/INST_ATUAL, inst_novo,
                "indexada ao CUB; CUB-SC real mai/26 R$3.064,10 (era R$3.100 placeholder) = -R$26k"))

GRAND_ATUAL = 23278659.95

# ============ 5. montar workbook ============
wb = openpyxl.Workbook()

# ---- PLACAR ----
ws = wb.active; ws.title = "PLACAR"
ws.sheet_view.showGridLines = False
titulo(ws, 1, "VALIDAÇÃO BIM × PARAMÉTRICO — ARQUITETURA · Placon Hermann Blumenau", 8)
cel(ws.cell(2,1), f"Modelo arquitetônico OSPA (Solibri) × Paramétrico V2 · AC {AC:,.2f} m² · escopo: só arquitetura (estrutura em revisão à parte)", fg=AZUL, size=9)
ws.merge_cells("A2:H2")
heads = ["Macrogrupo", "Qtd BIM", "Un", "Índice real\n(m²/m² AC)", "Qtd paramétrico", "Índice param", "Δ%", "Confiança / observação"]
for j,h in enumerate(heads,1): hdr(ws.cell(4,j), h)
rr = 5
for macro, qb, un, qp, conf, obs in placar:
    cel(ws.cell(rr,1), macro, bold=True)
    cel(ws.cell(rr,2), round(qb,1) if qb else "—", align="right", numfmt="#,##0")
    cel(ws.cell(rr,3), un, align="center")
    cel(ws.cell(rr,4), round(qb/AC,3) if qb else "—", align="right", numfmt="0.000")
    cel(ws.cell(rr,5), qp if qp else "—", align="right", numfmt="#,##0")
    cel(ws.cell(rr,6), round(qp/AC,3) if qp else "—", align="right", numfmt="0.000")
    delta = (qb-qp)/qp if (qb and qp) else None
    dtxt = f"{delta*100:+.0f}%" if delta is not None else "—"
    dfg = LARANJA if (delta is not None and abs(delta)>0.10) else PRETO
    cel(ws.cell(rr,7), dtxt, align="center", fg=dfg, bold=(dfg==LARANJA))
    cel(ws.cell(rr,8), f"[{conf}] {obs}", size=9)
    rr += 1
widths=[26,11,5,12,14,12,8,52]
for j,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(j)].width = w

# ---- REPRICE ----
ws2 = wb.create_sheet("REPRICE")
ws2.sheet_view.showGridLines = False
titulo(ws2, 1, "REPRICE ARQUITETURA — quantidade real × PU paramétrico", 5)
for j,h in enumerate(["Macrogrupo","Total atual (R$)","Fator","Total repreçado (R$)","Δ (R$) / nota"],1):
    hdr(ws2.cell(3,j), h)
rr=4; soma_at=soma_nv=0.0
for macro, tat, fat, tnv, nota in reprice:
    cel(ws2.cell(rr,1), macro, bold=True)
    cel(ws2.cell(rr,2), round(tat,2), align="right", numfmt='#,##0')
    cel(ws2.cell(rr,3), round(fat,3), align="center", numfmt='0.000')
    cel(ws2.cell(rr,4), round(tnv,2), align="right", numfmt='#,##0')
    d=tnv-tat
    cel(ws2.cell(rr,5), f"{d:+,.0f} — {nota}", size=9, fg=(LARANJA if abs(d)>50000 else PRETO))
    soma_at+=tat; soma_nv+=tnv; rr+=1
# subtotal arquitetura
cel(ws2.cell(rr,1), "SUBTOTAL MACROGRUPOS AJUSTADOS", bold=True, bg=CINZA_CLARO)
cel(ws2.cell(rr,2), round(soma_at,2), bold=True, align="right", numfmt='#,##0', bg=CINZA_CLARO)
cel(ws2.cell(rr,3), "", bg=CINZA_CLARO)
cel(ws2.cell(rr,4), round(soma_nv,2), bold=True, align="right", numfmt='#,##0', bg=CINZA_CLARO)
cel(ws2.cell(rr,5), f"{soma_nv-soma_at:+,.0f}", bold=True, bg=CINZA_CLARO, fg=LARANJA); rr+=2
delta_total = soma_nv - soma_at
cel(ws2.cell(rr,1), "GRAND TOTAL paramétrico atual", bold=True)
cel(ws2.cell(rr,2), round(GRAND_ATUAL,2), bold=True, align="right", numfmt='#,##0'); rr+=1
cel(ws2.cell(rr,1), "GRAND TOTAL c/ ajustes (arquitetura + parede diafragma)", bold=True, fg=BRANCO, bg=AZUL)
cel(ws2.cell(rr,2), round(GRAND_ATUAL+delta_total,2), bold=True, align="right", numfmt='#,##0', fg=BRANCO, bg=AZUL); rr+=1
cel(ws2.cell(rr,1), f"R$/m² → {(GRAND_ATUAL+delta_total)/AC:,.2f}  (era {GRAND_ATUAL/AC:,.2f})", fg=AZUL, size=9); rr+=1
UR = 35
cel(ws2.cell(rr,1), f"Custo/UR ({UR} UR) → R$ {(GRAND_ATUAL+delta_total)/UR:,.0f}  (era R$ {GRAND_ATUAL/UR:,.0f})", fg=AZUL, size=9); rr+=2
cel(ws2.cell(rr,1), "Base confirmada no projeto legal R05 (prancha 02): AC = 5.877,96 m² · 35 aptos + 1 loja. "
                    "Logo a recalibração de AC/UR não altera a base — o que recalcula o custo é a validação de arquitetura acima.", size=9, fg=PRETO); rr+=1
ws2.merge_cells(start_row=rr-1, start_column=1, end_row=rr-1, end_column=5)
for j,w in enumerate([34,18,9,20,60],1): ws2.column_dimensions[get_column_letter(j)].width=w

# ---- BIM_DETALHE ----
ws3 = wb.create_sheet("BIM_DETALHE")
ws3.sheet_view.showGridLines = False
titulo(ws3,1,"CLASSIFICAÇÃO DO TAKEOFF BIM (por tag de material)",4)
for j,h in enumerate(["Macrogrupo","Subitem","Área (m²)","m²/m² AC"],1): hdr(ws3.cell(3,j),h)
rr=4
for mg in sorted(grp):
    for sub,val in sorted(grp[mg].items(), key=lambda x:-x[1]):
        cel(ws3.cell(rr,1), mg, bold=True)
        cel(ws3.cell(rr,2), sub)
        cel(ws3.cell(rr,3), round(val,1), align="right", numfmt='#,##0.0')
        cel(ws3.cell(rr,4), round(val/AC,3), align="right", numfmt='0.000')
        rr+=1
for j,w in enumerate([20,40,12,10],1): ws3.column_dimensions[get_column_letter(j)].width=w

# ---- PREMISSAS ----
ws4 = wb.create_sheet("PREMISSAS")
ws4.sheet_view.showGridLines = False
titulo(ws4,1,"PREMISSAS E DECISÕES — validação arquitetura",1)
notas = [
 "Escopo: SÓ arquitetura. Estrutura (concreto/aço/fôrma/Supraestrutura) será revisada em sessão separada.",
 "Fonte BIM: modelo arquitetônico OSPA, takeoff Solibri (aba Building Element Quantities).",
 "Cuidado de leitura: o Solibri soma todas as camadas de material por elemento IFC — classificamos por TAG de material, não pela classe bruta.",
 "Net Area de parede = UMA face. Revestimento interno = 2× partições + 1× face interna da fachada (validado pelo casamento com o paramétrico).",
 "DECISÃO Leo: muretas 'EA' distribuídas — LAVANDERIA → alvenaria; demais (sacada/peitoril) → fachada.",
 "DECISÃO Leo: fachada — confiar no BIM e reduzir (envelope real ~6.845 m² + muretas externas).",
 "MATERIALIDADE ALVENARIA = 100% BLOCO CERÂMICO (confirmado). Busca cruzada não achou NENHUM drywall no Hermann: modelo BIM (todas paredes .VED bloco cerâmico), transcrições (reuniões Premissas Première + cronograma falam só alvenaria/bloco), WhatsApp do grupo, e Drive (sem memorial especificando drywall; o 'drywall' só aparece como rótulo de dropdown genérico do próprio paramétrico V2). Alvenaria repreçada a R$ 65,25/m² (bloco+argamassa+MO); reboco das paredes já está orçado em Rev. Parede (que casou com o BIM), então não há dupla contagem.",
 f"PREMISSA: forro ripado de madeira repreçado a R$ {RIPADO_PU:.0f}/m² (estimado) — item novo que o paramétrico não previu.",
 "Esquadrias: contagem BIM contaminada por componentes (folha/contramarco/puxador). Não repreçado — recomenda-se quadro de esquadrias.",
 "Impermeabilização: praticamente não modelada — mantida pelo índice do paramétrico.",
]
for i,n in enumerate(notas, start=3):
    c=ws4.cell(i,1); c.value=("• "+n); c.font=Font(name=FONT,size=10); c.alignment=Alignment(wrap_text=True,vertical="top")
ws4.column_dimensions["A"].width=130
for i in range(3,3+len(notas)): ws4.row_dimensions[i].height=30

# ---- PREMISSAS_DRIVE (varredura 2026-06-01) ----
ws5 = wb.create_sheet("PREMISSAS_DRIVE")
ws5.sheet_view.showGridLines = False
titulo(ws5,1,"PREMISSAS — VARREDURA DRIVE (Hermann Blumenau) · 01/06/2026",5)
cel(ws5.cell(2,1), "Extraído dos docs do projeto no Drive: ARQ GER_PROJ R05, PCI EP R00 (Première), ELE/HID/EST EP, COO análise de instalações, ata Premissas Première (05/11/2025).", fg=AZUL, size=9)
ws5.merge_cells("A2:E2")
for j,h in enumerate(["Categoria","Premissa","Valor confirmado (Drive)","Fonte","Status vs paramétrico"],1):
    hdr(ws5.cell(4,j), h)
# (cat, premissa, valor, fonte, status, flag)  flag: 'ok'|'novo'|'disc'
PD = [
 ("Vedação","Parede / divisória","Alvenaria de bloco cerâmico ~15 cm (8 furos/concreto/siporex). SEM drywall.","PCI §3.13 + modelo BIM","CONFIRMA 100% bloco — sem drywall","ok"),
 ("Estrutura","Laje","Maciça h=20–25 cm, não protendida; fck mín. 40 MPa; agressividade III","EST FORMA Lunardeli R01","fck 40 vs config 30 — tratar na revisão estrutural","disc"),
 ("Estrutura","Fundação","Estacas + blocos; contenção do subsolo por PAREDE DIAFRAGMA","EST FORMA + ata Première","INCORPORADO: contenção R$147k -> parede diafragma ~R$640k (+R$493k, estimativa)","novo"),
 ("Sist. Especiais","Pressurização escada","NÃO. Escada enclausurada ventilada (EEV) natural por dutos","PCI §3.13.2.3","CONFIRMA 'Não' (pressurização mecânica)","ok"),
 ("Sist. Especiais","Gás","Gás Natural (SCGás) + ERPM; aquecedor passagem + fogão por apto. LOJA SEM GÁS","PCI §3.9 + COO","novo detalhe (GN, não GLP)","novo"),
 ("Sist. Especiais","Gerador","Não dedicado (Placon). Première recomenda ~12 kVA só p/ bomba pluvial","ELE §3.5 + COO","CONFIRMA allowance 12 kVA","ok"),
 ("Climatização","Sistema","Split individual (evaporadora s/ portas; condensadora em área técnica de fachada)","COO + ata Première","novo detalhe","novo"),
 ("Elétrica","Fornecimento","Baixa tensão; proteção 400 A; DP 245,69 kVA; medição centralizada; sem subestação","ELE EP R00","novo detalhe","novo"),
 ("Elétrica","Veículos elétricos","36–37 vagas c/ infra de carregador (3,6 kW, carga lenta)","ELE + ata Première","novo detalhe","novo"),
 ("Elevadores","Quantidade","2 elevadores (caixa de corrida mín. 1,80 m, negociada c/ TKE)","GER_PROJ R05 + ata","CONFIRMA 2 elevadores","ok"),
 ("Hidráulica","Reservatórios","Inferior 20.000 L + Superior 30.000 L (inclui RTI 15.000 L)","HID EP R00 + PCI","novo detalhe","novo"),
 ("Geometria","Unidades (UR)","35 apartamentos + 1 loja (quadro UNIDADES do projeto legal R05)","ARQ legal R05 prancha 02","CONFIRMA 35 UR (HID dizia 36 — superado)","ok"),
 ("Geometria","Área construída (AC)","5.877,96 m² (Total) · CA 4.074,04 · Privativa 3.564,73","ARQ legal R05 quadro de áreas (prancha 02)","CONFIRMA AC 5.877,96 (PCI 5.966 era versão antiga)","ok"),
 ("Geometria","Pavimentos","18 (enquadramento PCI) / ~20–22 níveis estruturais","PCI vs config","definições diferentes — ok","ok"),
 ("Geometria","Alturas (Corte AA)","Fachada 69,96 m · topo extração fumaça 83,98 m · TOTAL empreendimento 86,98 m (regulatória zoneamento/PCI ~51,76 m)","ARQ legal R05 Corte AA","ESCLARECIDO: 2 alturas + total; config antigo 46 m era limite de zoneamento","ok"),
 ("Fachada","Característica","Floreiras de concreto em todos os pavimentos + guarda-corpo H=1,30 m","GER_PROJ R05 + PCI","atenção: custo fachada + compartimentação PCI","novo"),
 ("PCI","Compartimentação","Vertical e horizontal NÃO exigidas (<60 m / <75 m)","PCI §3.5/§3.6","-","ok"),
 ("PCI","CMAR (IN18)","Controle de materiais de acabamento exigido em áreas comuns + loja","PCI §3.7","impacta especificação de acabamento","novo"),
 ("Prazo","Obra","Não encontrado nos docs (config usa 30 meses, estimativa Cartesian)","—","mantido","ok"),
]
rr=5
for cat,prem,val,fonte,status,flag in PD:
    fg = LARANJA if flag=="disc" else (AZUL if flag=="novo" else PRETO)
    cel(ws5.cell(rr,1), cat, bold=True)
    cel(ws5.cell(rr,2), prem)
    cel(ws5.cell(rr,3), val, size=9)
    cel(ws5.cell(rr,4), fonte, size=9)
    cel(ws5.cell(rr,5), status, size=9, fg=fg, bold=(flag=="disc"))
    rr+=1
for j,w in enumerate([16,22,46,26,40],1): ws5.column_dimensions[get_column_letter(j)].width=w
ws5.cell(rr+1,1).value="Legenda: laranja = divergência a resolver · azul = premissa nova (não estava no paramétrico) · preto = confirma o paramétrico"
ws5.cell(rr+1,1).font=Font(name=FONT,size=9,italic=True,color=AZUL)

wb.save(OUT)
print("OK ->", OUT)
print(f"Subtotal arquitetura: atual {soma_at:,.0f} -> repreçado {soma_nv:,.0f}  (Δ {soma_nv-soma_at:+,.0f})")
print(f"Grand total: {GRAND_ATUAL:,.0f} -> {GRAND_ATUAL+delta_total:,.0f}  ({(GRAND_ATUAL+delta_total)/AC:,.2f}/m²)")
