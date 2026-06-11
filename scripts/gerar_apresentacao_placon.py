"""
Gera apresentacao .pptx do Placon Arminio Tavares parametrico V2 Hibrido.
Adaptado do script Arboris (v00) para o caso Placon (uso misto residencial + comercial,
Centro Historico de Floripa, 4.077 m2 AC, 55 UR, 18 pav, 24 meses).

Dados lidos via 'formulas' lib direto do xlsx parametrico.
Saida: base/pacotes/placon-arminio-tavares/apresentacao-placon-arminio-tavares.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import math
import os
import json
import formulas

# ============ PADRAO VISUAL CARTESIAN ============
AZUL_PRIM = RGBColor(0x1E, 0x52, 0xF5)   # Cartesian blue
AZUL_NAVY = RGBColor(0x0F, 0x1C, 0x4A)
LARANJA = RGBColor(0xFF, 0x57, 0x22)
CINZA_FUNDO = RGBColor(0xF4, 0xF6, 0xF8)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
CINZA_LINHA = RGBColor(0xE8, 0xEE, 0xF4)
CINZA_TXT = RGBColor(0x45, 0x4E, 0x5E)
PRETO = RGBColor(0x1A, 0x1A, 0x1A)
VERDE = RGBColor(0x2E, 0x8B, 0x57)

W = Inches(13.33)
H = Inches(7.5)

SLUG = "placon-arminio-tavares"
BASE = os.path.join(os.path.dirname(__file__), "..", "base", "pacotes", SLUG)
BASE = os.path.abspath(BASE)
XLSX_PATH = os.path.join(BASE, f"parametrico-{SLUG}.xlsx")
CONFIG_PATH = os.path.join(BASE, "parametrico-v2-config.json")
OUT_PATH = os.path.join(BASE, f"apresentacao-{SLUG}.pptx")

# ============ LOAD DADOS ============
with open(CONFIG_PATH, encoding='utf-8') as f:
    cfg = json.load(f)

AC = cfg['ac']                            # 4077.29
AP = cfg['area_privativa']                # 2083.94
AREA_COMUM = cfg['area_comum']            # 1993.35
UR = cfg['ur']                            # 55
AP_MEDIA = cfg['area_privativa_media_por_ur']  # 37.89
NP = cfg['np']                            # 18
NPT = cfg['npt']                          # 15
ALTURA = cfg['altura_rota_fuga']          # 40.68
ELEV = cfg['elev']                        # 2
VAG = cfg['vag']                          # 59
VAG_PRIV = cfg['vag_privativas']          # 55
VAG_PCD = cfg['vag_pcd_visitante']        # 4
PRAZO = cfg['prazo']                      # 24
CUB = cfg['cub']                          # 3028.45
TERRENO = cfg['area_terreno']             # 900
TERRENO_REM = cfg['area_terreno_remanescente']  # 873.27
PE_DIREITO = cfg['pe_direito_m_real']     # 2.88
BRIEFING = cfg['briefing']

print("Calculando formulas via formulas lib...")
xl = formulas.ExcelModel().loads(str(XLSX_PATH)).finish()
sol = xl.calculate()

def _val(cell):
    return sol[f"'[parametrico-{SLUG}.xlsx]CUSTOS_MACROGRUPO'!{cell}"].value[0][0]

# Macrogrupos — lendo direto (ordem fixa na aba CUSTOS_MACROGRUPO, rows 4..21)
MACROGRUPOS_ORDEM = [
    ('Gerenciamento', 4),
    ('Mov. Terra', 5),
    ('Infraestrutura', 6),
    ('Supraestrutura', 7),
    ('Alvenaria', 8),
    ('Impermeabilização', 9),
    ('Instalações', 10),
    ('Sist. Especiais', 11),
    ('Climatização', 12),
    ('Rev. Int. Parede', 13),
    ('Teto', 14),
    ('Pisos', 15),
    ('Pintura', 16),
    ('Esquadrias', 17),
    ('Louças e Metais', 18),
    ('Fachada', 19),
    ('Complementares', 20),
    ('Imprevistos', 21),
]

MACROS = []
for name, row in MACROGRUPOS_ORDEM:
    rsm2 = _val(f'B{row}')
    pct = _val(f'C{row}') * 100
    total = _val(f'D{row}')
    MACROS.append((name, float(total), float(pct), float(rsm2)))

GRAND_TOTAL = float(_val('D22'))
RSM2_TOTAL = float(_val('B22'))
CUSTO_UR = GRAND_TOTAL / UR

print(f"  Grand Total: R$ {GRAND_TOTAL:,.2f}")
print(f"  RS/m2: R$ {RSM2_TOTAL:,.2f}")
print(f"  Custo/UR: R$ {CUSTO_UR:,.2f}")

# ============ HELPERS ============
prs = Presentation()
prs.slide_width = W
prs.slide_height = H


def add_blank_slide():
    return prs.slides.add_slide(prs.slide_layouts[6])

def add_rect(slide, x, y, w, h, fill_color, line=False, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = fill_color
    if not line:
        s.line.fill.background()
    else:
        s.line.color.rgb = fill_color
    s.shadow.inherit = False
    return s

def add_text(slide, x, y, w, h, text, size=14, bold=False, color=PRETO,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, font='Calibri'):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = anchor
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    return tb

def add_footer(slide, n=None):
    txt = 'Cartesian' if n is None else f'Cartesian  |  {n}'
    add_text(slide, Inches(11.5), Inches(7.15), Inches(1.7), Inches(0.3),
             txt, size=10, bold=True, color=AZUL_PRIM, align=PP_ALIGN.RIGHT)


def fmt_brl(v):
    return f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def fmt_brl_int(v):
    return f'R$ {v:,.0f}'.replace(',', '.')

def fmt_mi(v):
    return f'R$ {v/1e6:.2f} Mi'.replace('.', ',')


# ============================================================
# SLIDE 1 — Capa Cartesian (brand)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0), Inches(2.8), W, Inches(1.8),
         'Cartesian', size=96, bold=True, color=AZUL_PRIM, align=PP_ALIGN.CENTER)
add_text(s, Inches(0), Inches(4.5), W, Inches(0.5),
         'Coordenação Técnica e Orçamentária', size=20, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_text(s, Inches(0), Inches(5.2), W, Inches(0.4),
         'Orçamento Paramétrico V2 Híbrido', size=16, color=AZUL_NAVY, align=PP_ALIGN.CENTER)


# ============================================================
# SLIDE 2 — Sumario Executivo
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.8),
         'SUMÁRIO EXECUTIVO', size=32, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.2), Inches(12), Inches(0.4),
         'Residencial Armínio Tavares  |  Placon Empreendimentos  |  Florianópolis/SC  |  Abr/2026',
         size=13, color=CINZA_TXT)

cards = [
    (fmt_mi(GRAND_TOTAL), 'CUSTO TOTAL', f'Paramétrico V2 — {len(MACROS)} macrogrupos'),
    (f'R$ {RSM2_TOTAL:,.0f}/m²'.replace(',', '.'), 'CUSTO POR M² AC', f'AC total: {AC:,.2f} m²'.replace(',', '.')),
    (fmt_mi(CUSTO_UR * 1), 'CUSTO POR UR', f'{UR} unidades residenciais'),
    (f'{PRAZO} meses', 'PRAZO DE OBRA', 'Inicio previsto conforme cronograma'),
]
xs = [Inches(0.8), Inches(7.0)]
ys = [Inches(2.0), Inches(4.6)]
for i, (big, label, desc) in enumerate(cards):
    x = xs[i % 2]
    y = ys[i // 2]
    add_rect(s, x, y, Inches(5.5), Inches(2.4), AZUL_NAVY)
    add_text(s, x, y+Inches(0.2), Inches(5.5), Inches(0.8),
             big, size=32, bold=True, color=LARANJA, align=PP_ALIGN.CENTER)
    add_text(s, x, y+Inches(1.15), Inches(5.5), Inches(0.4),
             label, size=14, bold=True, color=BRANCO, align=PP_ALIGN.CENTER)
    add_text(s, x, y+Inches(1.65), Inches(5.5), Inches(0.5),
             desc, size=12, color=CINZA_LINHA, align=PP_ALIGN.CENTER)
add_footer(s, '02')


# ============================================================
# SLIDE 3 — Identificação do Empreendimento
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'IDENTIFICAÇÃO DO EMPREENDIMENTO', size=28, bold=True, color=AZUL_PRIM)

info = [
    ('Empreendimento', 'Residencial Armínio Tavares'),
    ('Cliente', 'Placon Empreendimentos Imobiliários Ltda.'),
    ('CNPJ', '10.226.625/0001-20'),
    ('Endereço', 'Rua Dr. Armínio Tavares, Centro, Florianópolis/SC'),
    ('Região', 'Centro Histórico — área consolidada'),
    ('Data-base', 'Março/2026'),
    ('CUB/SC Mar-26', fmt_brl(CUB) + '/m²'),
    ('Origem dos dados', 'PL_R05 arquitetônico + PCI 26/02/26 aprovado'),
    ('Versão paramétrico', 'V2 Híbrido (Fase 19 — calibração 126 projetos)'),
    ('Margem de precisão', '±10% (paramétrico + preliminar)'),
]
y = Inches(1.4)
for k, v in info:
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.5), AZUL_NAVY)
    add_text(s, Inches(1.0), y, Inches(4.0), Inches(0.5),
             k, size=12, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.2), y, Inches(7.1), Inches(0.5),
             v, size=12, bold=True, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.54)
add_footer(s, '03')


# ============================================================
# SLIDE 4 — Parametros Urbanisticos
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'PARÂMETROS URBANÍSTICOS', size=28, bold=True, color=AZUL_PRIM)

urb = [
    ('Zoneamento', 'ARM-4.5 / ARP-2.4'),
    ('Uso declarado', 'Misto — residencial + comercial (térreo)'),
    ('Área do terreno', f'{TERRENO:,.2f} m²'.replace(',', '.')),
    ('Área remanescente (doação)', f'{TERRENO_REM:,.2f} m²'.replace(',', '.')),
    ('Número de pavimentos', f'{NP} (16 numerados + barrilete + reservatório)'),
    ('Pavimentos tipo', f'{NPT}'),
    ('Altura rota de fuga', f'{ALTURA} m'),
    ('Uso do térreo', 'Comercial — mín. 577 m² exigidos pelo zoneamento'),
    ('Incentivos urbanísticos', 'Uso misto + área remanescente (doação)'),
]
y = Inches(1.4)
for k, v in urb:
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.5), BRANCO)
    add_rect(s, Inches(0.8), y, Inches(0.12), Inches(0.5), AZUL_PRIM)
    add_text(s, Inches(1.0), y, Inches(4.0), Inches(0.5),
             k, size=12, color=CINZA_TXT, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.2), y, Inches(7.1), Inches(0.5),
             v, size=12, bold=True, color=AZUL_NAVY, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.55)
add_footer(s, '04')


# ============================================================
# SLIDE 5 — Configuração do Produto
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'CONFIGURAÇÃO DO PRODUTO', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Produto orientado a perfil urbano compacto — studios e 1-2 dorm com vocação de locação',
         size=12, color=CINZA_TXT)

# Mini-cards
produto = [
    (f'{UR}', 'UNIDADES', 'Residenciais'),
    (f'{AP_MEDIA:.1f} m²', 'AP MÉDIA', 'Área privativa/UR'),
    (f'{NP}', 'PAVIMENTOS', f'{NPT} pavs tipo'),
    (f'{VAG}', 'VAGAS', f'{VAG_PRIV} priv + {VAG_PCD} PCD/visit.'),
    (f'{ELEV}', 'ELEVADORES', 'Social + emergência'),
    (f'{PE_DIREITO} m', 'PÉ-DIREITO', 'Tipo compacto'),
]
xs = [Inches(0.8 + 4.15*i) for i in range(3)]
ys = [Inches(1.8), Inches(4.4)]
for i, (big, label, desc) in enumerate(produto):
    x = xs[i % 3]
    y = ys[i // 3]
    add_rect(s, x, y, Inches(3.9), Inches(2.3), BRANCO)
    add_rect(s, x, y, Inches(0.12), Inches(2.3), LARANJA)
    add_text(s, x, y+Inches(0.25), Inches(3.9), Inches(0.9),
             big, size=40, bold=True, color=AZUL_PRIM, align=PP_ALIGN.CENTER)
    add_text(s, x, y+Inches(1.2), Inches(3.9), Inches(0.4),
             label, size=13, bold=True, color=AZUL_NAVY, align=PP_ALIGN.CENTER)
    add_text(s, x, y+Inches(1.65), Inches(3.9), Inches(0.4),
             desc, size=11, color=CINZA_TXT, align=PP_ALIGN.CENTER)

add_text(s, Inches(0.8), Inches(7.0), Inches(12), Inches(0.3),
         'Uso misto com comercial no térreo (mín. 577 m²) atende à exigência do zoneamento ARM-4.5/ARP-2.4',
         size=10, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '05')


# ============================================================
# SLIDE 6 — Quadro de Áreas
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'QUADRO DE ÁREAS', size=28, bold=True, color=AZUL_PRIM)

# Tabela de áreas
areas = [
    ('Área do terreno', f'{TERRENO:,.2f} m²'.replace(',', '.'), '—'),
    ('Área remanescente (doação)', f'{TERRENO_REM:,.2f} m²'.replace(',', '.'), '—'),
    ('Área Construída Total (AC)', f'{AC:,.2f} m²'.replace(',', '.'), '100,00%'),
    ('Área privativa', f'{AP:,.2f} m²'.replace(',', '.'), f'{AP/AC*100:.2f}%'),
    ('Área comum', f'{AREA_COMUM:,.2f} m²'.replace(',', '.'), f'{AREA_COMUM/AC*100:.2f}%'),
    ('AP média por UR', f'{AP_MEDIA:.2f} m²', '—'),
    ('AC PCI (aprovado)', f'{cfg["ac_pci"]:,.2f} m²'.replace(',', '.'), '—'),
]
hdr_y = Inches(1.4)
add_rect(s, Inches(1.0), hdr_y, Inches(11.3), Inches(0.5), AZUL_PRIM)
add_text(s, Inches(1.2), hdr_y, Inches(5.5), Inches(0.5), 'ITEM',
         size=13, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(6.5), hdr_y, Inches(3.0), Inches(0.5), 'VALOR',
         size=13, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(9.5), hdr_y, Inches(2.8), Inches(0.5), '% AC',
         size=13, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

y = hdr_y + Inches(0.55)
for i, (k, v, pct) in enumerate(areas):
    bg = BRANCO if i % 2 == 0 else CINZA_LINHA
    add_rect(s, Inches(1.0), y, Inches(11.3), Inches(0.5), bg)
    add_text(s, Inches(1.2), y, Inches(5.5), Inches(0.5),
             k, size=12, color=PRETO, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(6.5), y, Inches(3.0), Inches(0.5),
             v, size=12, bold=True, color=AZUL_NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(9.5), y, Inches(2.8), Inches(0.5),
             pct, size=12, color=CINZA_TXT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.55)

add_text(s, Inches(0.8), Inches(6.9), Inches(12), Inches(0.3),
         'Fonte: projeto legal PL_R05 arquitetônico + PCI 26/02/26 carimbado aprovado',
         size=10, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '06')


# ============================================================
# SLIDE 7 — Briefing V2 (14 decisões)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'BRIEFING V2 — 14 DECISÕES', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Parâmetros de calibração do paramétrico V2 Híbrido (dropdowns da aba BRIEFING)',
         size=12, color=CINZA_TXT)

briefing_labels = [
    ('Laje', BRIEFING.get('laje', '—')),
    ('Subsolos', BRIEFING.get('subsolos', '—')),
    ('Fundação', BRIEFING.get('fundacao', '—')),
    ('Padrão acabamento', BRIEFING.get('padrao_acabamento', '—')),
    ('Fachada', BRIEFING.get('fachada', '—')),
    ('Pressurização', BRIEFING.get('pressurizacao', '—')),
    ('N. torres', BRIEFING.get('n_torres', '—')),
    ('Gerador', BRIEFING.get('gerador', '—')),
    ('Entrega', BRIEFING.get('entrega', '—')),
    ('Tipologia', BRIEFING.get('tipologia', '—')),
    ('Pé-direito (briefing)', BRIEFING.get('pe_direito', '—')),
    ('N. banheiros', BRIEFING.get('n_banheiros', '—')),
    ('Tipo de piso', BRIEFING.get('tipo_piso', '—')),
    ('Piscina', BRIEFING.get('piscina', '—')),
]

# 2 colunas de 7
col_x = [Inches(0.8), Inches(6.9)]
row_h = Inches(0.55)
start_y = Inches(1.7)
for idx, (k, v) in enumerate(briefing_labels):
    col = idx // 7
    row = idx % 7
    x = col_x[col]
    y = start_y + row_h * row
    add_rect(s, x, y, Inches(6.0), Inches(0.5), BRANCO)
    add_rect(s, x, y, Inches(0.1), Inches(0.5), AZUL_PRIM)
    add_text(s, x+Inches(0.2), y, Inches(3.0), Inches(0.5),
             k, size=11, color=CINZA_TXT, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, x+Inches(3.2), y, Inches(2.7), Inches(0.5),
             v, size=11, bold=True, color=AZUL_NAVY, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_footer(s, '07')


# ============================================================
# SLIDE 8 — Metodologia V2 Híbrido
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'METODOLOGIA — V2 HÍBRIDO', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Paramétrico calibrado bottom-up com base em 126 projetos da Cartesian',
         size=13, color=CINZA_TXT)

blocks = [
    ('📊 O QUE É',
     ['Estimativa de custos bottom-up em 18 macrogrupos',
      'Calibrado por briefing de 14 decisões (laje, fachada, tipologia…)',
      'Valores unitários vêm de base histórica (4.210 PUs cross-projeto)',
      '29 índices físicos derivados (m²/m², kg/m², consumos)']),
    ('🎯 POR QUE USAR',
     ['Decisão de viabilidade antes de projeto executivo',
      'Benchmark cross-projeto (P25-P50-P75 da base Cartesian)',
      'Overrides manuais durante reunião (aba INDICES)',
      'Transição suave do paramétrico para o orçamento preliminar']),
    ('⚖️ PRECISÃO',
     ['Margem ±10% — compatível com paramétrico calibrado',
      'NÃO é BoQ executivo rastreável item a item',
      'Itens de referência cross-projeto (não levantamento do CAD)',
      'Re-calibrado condicionalmente via labels Gemma semânticos']),
]
y = Inches(1.7)
for title, bullets in blocks:
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(1.6), BRANCO)
    add_rect(s, Inches(0.8), y, Inches(0.12), Inches(1.6), LARANJA)
    add_text(s, Inches(1.05), y+Inches(0.1), Inches(11), Inches(0.4),
             title, size=14, bold=True, color=AZUL_PRIM)
    by = y + Inches(0.55)
    for b in bullets:
        add_text(s, Inches(1.15), by, Inches(11.2), Inches(0.28),
                 '• ' + b, size=10, color=PRETO)
        by += Inches(0.26)
    y += Inches(1.7)
add_footer(s, '08')


# ============================================================
# SLIDE 9 — Macrogrupos (visão geral) — tabela completa
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.5), Inches(0.4), Inches(12), Inches(0.7),
         'COMPOSIÇÃO POR MACROGRUPO', size=28, bold=True, color=AZUL_PRIM)

hdr_y = Inches(1.15)
add_rect(s, Inches(0.5), hdr_y, Inches(12.3), Inches(0.4), AZUL_PRIM)
add_text(s, Inches(0.6), hdr_y, Inches(4.5), Inches(0.4), 'MACROGRUPO',
         size=11, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(5.2), hdr_y, Inches(2.6), Inches(0.4), 'CUSTO TOTAL',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(8.0), hdr_y, Inches(1.2), Inches(0.4), '%',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(9.3), hdr_y, Inches(1.8), Inches(0.4), 'R$/m²',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(11.2), hdr_y, Inches(1.5), Inches(0.4), 'BARRA',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

max_pct = max(m[2] for m in MACROS)
y = Inches(1.55)
for i, (name, val, pct, rsm2) in enumerate(MACROS):
    bg = BRANCO if i % 2 == 0 else CINZA_LINHA
    add_rect(s, Inches(0.5), y, Inches(12.3), Inches(0.28), bg)
    add_text(s, Inches(0.6), y, Inches(4.5), Inches(0.28),
             name, size=9, color=PRETO, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.2), y, Inches(2.6), Inches(0.28),
             fmt_brl(val), size=9, color=PRETO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(8.0), y, Inches(1.2), Inches(0.28),
             f'{pct:.1f}%', size=9, color=PRETO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(9.3), y, Inches(1.8), Inches(0.28),
             f'R$ {rsm2:,.0f}'.replace(',', '.'), size=9, color=PRETO,
             align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    bw = Inches(1.4 * pct / max_pct)
    add_rect(s, Inches(11.25), y+Inches(0.06), bw, Inches(0.16), AZUL_PRIM)
    y += Inches(0.28)

# Total
add_rect(s, Inches(0.5), y, Inches(12.3), Inches(0.35), AZUL_PRIM)
add_text(s, Inches(0.6), y, Inches(4.5), Inches(0.35), 'GRAND TOTAL',
         size=11, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(5.2), y, Inches(2.6), Inches(0.35),
         fmt_brl(GRAND_TOTAL), size=11, bold=True, color=BRANCO,
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(8.0), y, Inches(1.2), Inches(0.35), '100%',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(9.3), y, Inches(1.8), Inches(0.35),
         f'R$ {RSM2_TOTAL:,.0f}'.replace(',', '.'), size=11, bold=True, color=BRANCO,
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
add_footer(s, '09')


# ============================================================
# SLIDE 10 — Top 5 macrogrupos (barras horizontais)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'TOP 5 MACROGRUPOS POR CUSTO', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Concentram tipicamente 65-75% do custo total de uma obra residencial compacta',
         size=12, color=CINZA_TXT)

top5 = sorted(MACROS, key=lambda x: -x[1])[:5]
maxv = top5[0][1]
chart_x = Inches(0.8)
chart_y = Inches(1.8)
chart_w = Inches(11.7)
row_h = Inches(1.0)
for i, (name, val, pct, rsm2) in enumerate(top5):
    y = chart_y + row_h * i
    # label + %
    add_text(s, chart_x, y, Inches(3.0), row_h,
             f'{i+1}. {name}', size=14, bold=True, color=AZUL_NAVY, anchor=MSO_ANCHOR.MIDDLE)
    # barra
    bar_w = Inches(6.5 * val / maxv)
    add_rect(s, chart_x + Inches(3.1), y + Inches(0.2), bar_w, Inches(0.55), AZUL_PRIM)
    # valor
    add_text(s, chart_x + Inches(3.1) + bar_w + Inches(0.1), y, Inches(2.0), row_h,
             fmt_mi(val), size=13, bold=True, color=LARANJA, anchor=MSO_ANCHOR.MIDDLE)
    # sub-label
    add_text(s, chart_x + Inches(3.1), y + Inches(0.78), Inches(6.5), Inches(0.25),
             f'{pct:.1f}% do total  |  R$ {rsm2:,.0f}/m²'.replace(',', '.'),
             size=10, color=CINZA_TXT)

add_text(s, Inches(0.8), Inches(7.0), Inches(12), Inches(0.3),
         f'Soma dos Top 5: {sum(m[2] for m in top5):.1f}% do Grand Total',
         size=11, bold=True, color=AZUL_PRIM, align=PP_ALIGN.CENTER)
add_footer(s, '10')


# ============================================================
# SLIDES 11-13 — Detalhes técnicos (Supraestrutura, Fachada, Esquadrias)
# ============================================================
def slide_detalhe(title, mg_name, descritivo, bullets, n):
    s = add_blank_slide()
    add_rect(s, 0, 0, W, H, CINZA_FUNDO)
    add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
             title, size=28, bold=True, color=AZUL_PRIM)
    # Busca o macrogrupo
    mg = next((m for m in MACROS if m[0] == mg_name), None)
    if mg:
        _, val, pct, rsm2 = mg
        add_rect(s, Inches(0.8), Inches(1.3), Inches(11.7), Inches(1.0), AZUL_NAVY)
        add_text(s, Inches(1.0), Inches(1.3), Inches(4.0), Inches(1.0),
                 fmt_mi(val), size=28, bold=True, color=LARANJA, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, Inches(5.2), Inches(1.3), Inches(3.5), Inches(1.0),
                 f'{pct:.1f}% do total', size=18, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, Inches(8.8), Inches(1.3), Inches(3.5), Inches(1.0),
                 f'R$ {rsm2:,.0f}/m²'.replace(',', '.'),
                 size=18, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    # Descritivo
    add_text(s, Inches(0.8), Inches(2.5), Inches(11.7), Inches(0.5),
             descritivo, size=14, bold=True, color=AZUL_PRIM)
    y = Inches(3.1)
    for b in bullets:
        add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.6), BRANCO)
        add_rect(s, Inches(0.8), y, Inches(0.1), Inches(0.6), LARANJA)
        add_text(s, Inches(1.0), y, Inches(11.5), Inches(0.6),
                 '• ' + b, size=12, color=PRETO, anchor=MSO_ANCHOR.MIDDLE)
        y += Inches(0.65)
    add_footer(s, n)

slide_detalhe(
    'SUPRAESTRUTURA — LAJE PROTENDIDA',
    'Supraestrutura',
    'Briefing: laje Protendida — ganho de pé-direito e vãos livres em tipologia compacta',
    [
        f'Torre de {NP} pavimentos com {NPT} pavimentos tipo repetitivos',
        'Laje protendida permite maior vão livre e pé-direito liquido útil',
        'Pé-direito de projeto: 2,88 m (compacto — ideal para studios/1-2 dorm)',
        f'Altura rota de fuga: {ALTURA} m — exige instalações preventivas completas',
        'Fundação em estacas hélice (briefing) — compatível com solo de Centro Floripa',
    ],
    '11',
)

slide_detalhe(
    'FACHADA — TEXTURA',
    'Fachada',
    'Briefing: fachada em Textura — acabamento de custo intermediário, durabilidade adequada',
    [
        'Tinta premium acrílica com textura (2-4 cores) — sem revestimento cerâmico externo',
        f'Torre vertical de {NP} pavimentos — PU contempla balancim fachadeiro',
        'Área de fachada estimada: ~1,4 a 1,6 m²/m² AC (típico para torre compacta)',
        'Opção cerâmica elevaria este macrogrupo em ~40% — descartada no briefing',
        'Muros periféricos: tinta acrílica lisa ou textura complementar',
    ],
    '12',
)

slide_detalhe(
    'ESQUADRIAS — PADRÃO MÉDIO-ALTO',
    'Esquadrias',
    'Briefing: padrão Médio-Alto — alumínio eletrostático + vidros temperados',
    [
        'Janelas de alumínio com pintura eletrostática (padrão superior ao anodizado)',
        f'{UR} unidades com configuração studios / 1-2 dorm — esquadrias compactas',
        'Vidros temperados em todas as aberturas (segurança NBR)',
        'Soleiras em granito nas esquadrias (padrão M-A)',
        'Ferragens Papaiz/Arouca/Pado (padrão Cartesian)',
    ],
    '13',
)


# ============================================================
# SLIDE 14 — Gerenciamento com overrides
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'GERENCIAMENTO — OVERRIDES APLICADOS', size=26, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Ajustes manuais do Leo durante revisão do briefing V2 (22/abr)',
         size=12, color=CINZA_TXT)

ger = next((m for m in MACROS if m[0] == 'Gerenciamento'), None)
if ger:
    _, val, pct, rsm2 = ger
    add_rect(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.0), AZUL_NAVY)
    add_text(s, Inches(1.0), Inches(1.7), Inches(4.0), Inches(1.0),
             fmt_mi(val), size=28, bold=True, color=LARANJA, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.2), Inches(1.7), Inches(3.5), Inches(1.0),
             f'{pct:.1f}% do total', size=18, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(8.8), Inches(1.7), Inches(3.5), Inches(1.0),
             f'R$ {rsm2:,.0f}/m²'.replace(',', '.'),
             size=18, color=BRANCO, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

add_text(s, Inches(0.8), Inches(2.9), Inches(11.7), Inches(0.4),
         'PREMISSAS APLICADAS NO GERENCIAMENTO',
         size=14, bold=True, color=AZUL_PRIM)

ger_notes = [
    f'Prazo de obra: {PRAZO} meses (compatível com torre {NP} pavimentos / {NPT} tipo)',
    'Equipe técnica enxuta — engenheiro residente + mestre + encarregados',
    'Canteiro de obras em terreno urbano com logística de Centro Histórico',
    'Overrides aplicados pelo Leo refletem equipe real da Cartesian para obra Placon',
    'Inclui: projetos complementares, consultorias, taxas, ensaios, EPI, vigilância',
    'Valor ajustado para perfil Placon (uso misto, obra urbana compacta)',
]
y = Inches(3.5)
for note in ger_notes:
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.45), BRANCO)
    add_rect(s, Inches(0.8), y, Inches(0.1), Inches(0.45), LARANJA)
    add_text(s, Inches(1.0), y, Inches(11.5), Inches(0.45),
             '• ' + note, size=11, color=PRETO, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.5)
add_footer(s, '14')


# ============================================================
# SLIDE 15 — Comparativo vs outros projetos
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'COMPARATIVO — OBRAS SIMILARES DA BASE CARTESIAN', size=26, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Perfis anonimizados — AC 3.300-4.800 m² — residencial vertical',
         size=12, color=CINZA_TXT)

# Perfis reais da base Cartesian (Supabase indices-cartesian, tabela projetos)
# AC 3.3-4.8k m², padrão M-A/Alto. Anonimizado por perfil.
projetos = [
    ('PLACON (este)',           'Médio-Alto', 4077, RSM2_TOTAL, True,  AZUL_PRIM),
    ('Obra compacta mid-rise',  'Alto',       4430, 5247, False, CINZA_TXT),
    ('Obra padrão alto',        'Alto',       4617, 4197, False, CINZA_TXT),
    ('Obra padrão alto',        'Alto',       4812, 4188, False, CINZA_TXT),
    ('Obra compacta M-A',       'Médio-Alto', 4410, 3799, False, CINZA_TXT),
    ('Obra boutique',           'Alto',       3972, 3134, False, CINZA_TXT),
    ('Obra padrão M-A',         'Médio-Alto', 4440, 3229, False, CINZA_TXT),
]

hdr_y = Inches(1.7)
add_rect(s, Inches(0.8), hdr_y, Inches(11.7), Inches(0.4), AZUL_PRIM)
cols = [('PERFIL',      1.0, 4.2, PP_ALIGN.LEFT),
        ('PADRÃO',      5.3, 2.2, PP_ALIGN.CENTER),
        ('AC (m²)',     7.6, 1.6, PP_ALIGN.CENTER),
        ('R$/m² AC',    9.3, 2.1, PP_ALIGN.CENTER),
        ('STATUS',     11.5, 1.0, PP_ALIGN.CENTER)]
for txt, x, w, al in cols:
    add_text(s, Inches(x), hdr_y, Inches(w), Inches(0.4),
             txt, size=11, bold=True, color=BRANCO, align=al, anchor=MSO_ANCHOR.MIDDLE)

y = hdr_y + Inches(0.45)
for name, padrao, ac, rsm2, highlight, cor in projetos:
    bg = CINZA_LINHA if highlight else BRANCO
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.5), bg)
    add_rect(s, Inches(0.8), y, Inches(0.12), Inches(0.5), cor)
    add_text(s, Inches(1.0), y, Inches(4.2), Inches(0.5),
             name, size=12, bold=highlight, color=AZUL_PRIM if highlight else PRETO,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.3), y, Inches(2.2), Inches(0.5),
             padrao, size=11, color=PRETO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(7.6), y, Inches(1.6), Inches(0.5),
             f'{ac:,.0f}'.replace(',', '.'), size=11, color=PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(9.3), y, Inches(2.1), Inches(0.5),
             f'R$ {rsm2:,.0f}'.replace(',', '.'),
             size=12, bold=highlight, color=LARANJA if highlight else PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    status = 'ATUAL' if highlight else 'base'
    add_text(s, Inches(11.5), y, Inches(1.0), Inches(0.5),
             status, size=10, color=CINZA_TXT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.55)

add_text(s, Inches(0.8), Inches(5.9), Inches(12), Inches(0.5),
         'Placon em R$ 4.255/m² — acima da mediana M-A (~R$ 3.500) e próximo da faixa Alto',
         size=12, bold=True, color=AZUL_NAVY, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
         'Reflete laje protendida, fachada elaborada e canteiro centro histórico (terreno 900 m²)',
         size=10, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '15')


# ============================================================
# SLIDE 16 — Benchmark base Cartesian (faixas P25-P75)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'BENCHMARK — BASE CARTESIAN (126 PROJETOS)', size=24, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Faixas de custo por m² — base real de 126 obras residenciais verticais já entregues pela Cartesian',
         size=12, color=CINZA_TXT)

# VALORES REAIS da tabela calibracao_global (Supabase indices-cartesian)
# Consultado em 23/04/2026. n = nº de projetos com valor observado por macrogrupo.
benchmarks = [
    # (macrogrupo, p25, p50, p75, n)
    ('Supraestrutura',     532, 657,  718, 56),
    ('Gerenciamento',      126, 224,  507, 131),
    ('Esquadrias',         261, 308,  413, 56),
    ('Instalações',        146, 275,  367, 80),
    ('Pisos',              160, 201,  251, 42),
    ('Infraestrutura',     139, 195,  240, 63),
    ('Complementares',     109, 174,  247, 57),
    ('Sist. Especiais',    117, 163,  211, 59),
    ('Alvenaria',          118, 152,  203, 130),
    ('Fachada',             84, 134,  196, 33),
    ('Pintura',            102, 124,  151, 61),
    ('Rev. Int. Parede',    56,  93,  149, 61),
]

# Constrói mapa do Placon
placon_rsm2 = {m[0]: m[3] for m in MACROS}

hdr_y = Inches(1.7)
add_rect(s, Inches(0.8), hdr_y, Inches(11.7), Inches(0.4), AZUL_PRIM)
add_text(s, Inches(1.0), hdr_y, Inches(2.7), Inches(0.4), 'MACROGRUPO',
         size=11, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(3.8), hdr_y, Inches(1.4), Inches(0.4), 'PLACON',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(5.3), hdr_y, Inches(1.3), Inches(0.4), 'ECONÔMICO',
         size=10, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(6.7), hdr_y, Inches(1.3), Inches(0.4), 'MERCADO',
         size=10, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(8.1), hdr_y, Inches(1.3), Inches(0.4), 'PREMIUM',
         size=10, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(9.5), hdr_y, Inches(0.8), Inches(0.4), 'n',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(10.4), hdr_y, Inches(2.0), Inches(0.4), 'POSIÇÃO',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

y = hdr_y + Inches(0.45)
for idx_row, (mg, p25, p50, p75, n) in enumerate(benchmarks):
    placon = placon_rsm2.get(mg, 0)
    bg = BRANCO if idx_row % 2 == 0 else CINZA_LINHA
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(0.32), bg)
    add_text(s, Inches(1.0), y, Inches(2.7), Inches(0.32),
             mg, size=10, color=PRETO, anchor=MSO_ANCHOR.MIDDLE)
    # Posição didática
    if placon < p25:
        status = 'ABAIXO DO MERCADO'
        cor = VERDE
    elif placon <= p50:
        status = 'COMPETITIVO'
        cor = AZUL_PRIM
    elif placon <= p75:
        status = 'MERCADO'
        cor = CINZA_TXT
    else:
        status = 'ACIMA DO MERCADO'
        cor = LARANJA
    add_text(s, Inches(3.8), y, Inches(1.4), Inches(0.32),
             f'R$ {placon:,.0f}'.replace(',', '.'), size=10, bold=True, color=AZUL_PRIM,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.3), y, Inches(1.3), Inches(0.32),
             f'R$ {p25:,.0f}'.replace(',', '.'), size=10, color=PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(6.7), y, Inches(1.3), Inches(0.32),
             f'R$ {p50:,.0f}'.replace(',', '.'), size=10, color=PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(8.1), y, Inches(1.3), Inches(0.32),
             f'R$ {p75:,.0f}'.replace(',', '.'), size=10, color=PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(9.5), y, Inches(0.8), Inches(0.32),
             str(n), size=9, color=CINZA_TXT,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(10.4), y, Inches(2.0), Inches(0.32),
             status, size=10, bold=True, color=cor, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.32)

# Legenda didática das faixas
legenda_y = Inches(6.5)
add_rect(s, Inches(0.8), legenda_y, Inches(11.7), Inches(0.9), BRANCO)
add_text(s, Inches(1.0), legenda_y + Inches(0.05), Inches(11.3), Inches(0.3),
         'Como ler:', size=10, bold=True, color=AZUL_PRIM)
add_text(s, Inches(1.0), legenda_y + Inches(0.3), Inches(11.3), Inches(0.3),
         '• ECONÔMICO = obras que ficaram entre as 25% mais baratas  |  • MERCADO = custo típico (metade das obras custa mais, metade menos)',
         size=9, color=PRETO)
add_text(s, Inches(1.0), legenda_y + Inches(0.55), Inches(11.3), Inches(0.3),
         '• PREMIUM = obras que ficaram entre as 25% mais caras  |  "ACIMA DO MERCADO" significa que o item está mais caro que 3 em cada 4 obras comparáveis',
         size=9, color=PRETO)

add_text(s, Inches(0.8), Inches(7.45), Inches(12), Inches(0.25),
         'Fonte: base Cartesian — 126 obras residenciais verticais, Grande Florianópolis e Litoral Norte/SC',
         size=8, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '16')


# ============================================================
# SLIDE 17 — Justificativas (itens acima do mercado)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'JUSTIFICATIVAS — ITENS ACIMA DO MERCADO', size=26, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Por que alguns macrogrupos estão acima da média da base Cartesian',
         size=12, color=CINZA_TXT)

# (macrogrupo, placon_rsm2, mediana_mercado, motivos_texto)
justif = [
    ('Supraestrutura', 801, 657,
     'Laje PROTENDIDA (+15–25% vs convencional) • 18 pavimentos / 40m de altura • '
     'volume e taxa de aço maiores para vãos livres'),
    ('Gerenciamento', 729, 224,
     'Obra compacta (4.077 m²) com prazo longo (24 meses) dilui custos fixos • '
     'Centro histórico Floripa: canteiro restrito (900 m²), taxas/incorporação mais altas • '
     'Base inclui obras menores sem estrutura técnica formal'),
    ('Complementares', 330, 174,
     'Padrão Médio-Alto com entrega completa: salão, hall premium, academia, churrasqueira • '
     'Áreas comuns robustas (48,9% da AC) com acabamento diferenciado'),
    ('Fachada', 237, 134,
     'Altura de 40m exige plataformas motorizadas e logística vertical • '
     'Padrão M-A em centro histórico pede acabamento mais elaborado • '
     'Mais superfícies expostas (fachadas ativas leste/oeste)'),
    ('Climatização', 118, 39,
     'Pré-instalação de split completo em 55 unidades (dutos, tubulação, pontos) • '
     'Climatização de áreas comuns (salão, academia, hall) • '
     'Base histórica tem obras sem pré-instalação'),
]

# Header
hdr_y = Inches(1.7)
add_rect(s, Inches(0.4), hdr_y, Inches(12.5), Inches(0.4), AZUL_PRIM)
add_text(s, Inches(0.55), hdr_y, Inches(2.0), Inches(0.4), 'MACROGRUPO',
         size=11, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(2.55), hdr_y, Inches(1.1), Inches(0.4), 'PLACON',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(3.65), hdr_y, Inches(1.1), Inches(0.4), 'MERCADO',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(4.75), hdr_y, Inches(0.9), Inches(0.4), 'Δ',
         size=11, bold=True, color=BRANCO, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(s, Inches(5.75), hdr_y, Inches(7.1), Inches(0.4), 'MOTIVO TÉCNICO',
         size=11, bold=True, color=BRANCO, anchor=MSO_ANCHOR.MIDDLE)

y = hdr_y + Inches(0.45)
row_h = Inches(0.88)
for idx, (mg, placon, mediana, motivo) in enumerate(justif):
    bg = BRANCO if idx % 2 == 0 else CINZA_LINHA
    add_rect(s, Inches(0.4), y, Inches(12.5), row_h, bg)
    add_rect(s, Inches(0.4), y, Inches(0.12), row_h, LARANJA)
    delta_pct = (placon - mediana) / mediana * 100
    add_text(s, Inches(0.55), y, Inches(2.0), row_h,
             mg, size=11, bold=True, color=AZUL_PRIM, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(2.55), y, Inches(1.1), row_h,
             f'R$ {placon}', size=11, bold=True, color=LARANJA,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(3.65), y, Inches(1.1), row_h,
             f'R$ {mediana}', size=11, color=PRETO,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(4.75), y, Inches(0.9), row_h,
             f'+{delta_pct:.0f}%', size=11, bold=True, color=LARANJA,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.85), y + Inches(0.05), Inches(7.0), row_h - Inches(0.1),
             motivo, size=9, color=PRETO)
    y += row_h

# Nota final
add_text(s, Inches(0.8), Inches(6.75), Inches(12), Inches(0.3),
         'Sist. Especiais (R$ 213 vs R$ 163 / +31%) e Pintura (R$ 154 vs R$ 124 / +24%) também aparecem no limite superior —',
         size=9, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.8), Inches(7.0), Inches(12), Inches(0.3),
         'refletem automação/segurança padrão M-A e altura da torre (logística de pintura)',
         size=9, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.8), Inches(7.4), Inches(12), Inches(0.3),
         'Macrogrupos não listados estão dentro da faixa de mercado ou mais econômicos que a mediana.',
         size=9, color=AZUL_PRIM, bold=True, align=PP_ALIGN.CENTER)
add_footer(s, '17')


# ============================================================
# SLIDE 18 — Curva Física Mensal (barras)
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'CURVA FÍSICA MENSAL — 24 MESES', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         'Distribuição mensal de desembolso físico-financeiro (curva S típica)',
         size=12, color=CINZA_TXT)

N_MONTHS = PRAZO
# Curva S com pico no meio
pesos = []
for m in range(1, N_MONTHS+1):
    p = math.exp(-((m - N_MONTHS/2)**2) / (2 * (N_MONTHS/5)**2))
    pesos.append(p)
soma = sum(pesos)
pct_dist = [p / soma * 100 for p in pesos]
valores = [p / 100 * GRAND_TOTAL for p in pct_dist]

chart_x = Inches(0.8)
chart_y = Inches(1.8)
chart_w = Inches(11.7)
bar_w = Emu(int(int(chart_w - Inches(0.4)) / N_MONTHS))
maxp = max(pct_dist)

for m in range(N_MONTHS):
    v = pct_dist[m]
    bh = Inches(3.8 * v / maxp)
    x = chart_x + Inches(0.2) + bar_w * m
    add_rect(s, x, chart_y + Inches(4.0) - bh, bar_w - Emu(80000), bh, AZUL_PRIM)
    add_text(s, x - Emu(40000), chart_y + Inches(4.0) - bh - Inches(0.25),
             bar_w + Emu(160000), Inches(0.2),
             f'{v:.1f}%', size=7, color=AZUL_NAVY, align=PP_ALIGN.CENTER)
    add_text(s, x, chart_y + Inches(4.05), bar_w, Inches(0.2),
             f'M{m+1}', size=8, color=CINZA_TXT, align=PP_ALIGN.CENTER)

# Resumo abaixo
add_text(s, Inches(0.8), Inches(6.2), Inches(12), Inches(0.3),
         f'Pico mensal: mês {pct_dist.index(max(pct_dist))+1} ({max(pct_dist):.1f}% — R$ {max(valores)/1e6:.2f} Mi)',
         size=12, bold=True, color=AZUL_PRIM, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.8), Inches(6.6), Inches(12), Inches(0.3),
         f'Valor médio mensal: R$ {GRAND_TOTAL/N_MONTHS/1e6:.2f} Mi',
         size=11, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '18')


# ============================================================
# SLIDE 19 — Curva Acumulada
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'CURVA FÍSICA ACUMULADA (S-CURVE)', size=28, bold=True, color=AZUL_PRIM)
add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(0.4),
         f'Avanço acumulado 0% → 100% ao longo dos {N_MONTHS} meses de obra',
         size=12, color=CINZA_TXT)

pct_acum = []
tot = 0
for p in pct_dist:
    tot += p
    pct_acum.append(tot)

chart_y = Inches(1.8)
chart_x = Inches(0.8)
chart_w = Inches(11.7)
bar_w = Emu(int(int(chart_w - Inches(0.4)) / N_MONTHS))

for m in range(N_MONTHS):
    v = pct_acum[m]
    bh = Inches(3.8 * v / 100)
    x = chart_x + Inches(0.2) + bar_w * m
    add_rect(s, x, chart_y + Inches(4.0) - bh, bar_w - Emu(60000), bh, LARANJA)
    if m % 3 == 0 or m == N_MONTHS - 1:
        add_text(s, x - Emu(40000), chart_y + Inches(4.0) - bh - Inches(0.25),
                 bar_w + Emu(160000), Inches(0.2),
                 f'{v:.0f}%', size=8, bold=True, color=AZUL_NAVY, align=PP_ALIGN.CENTER)
    add_text(s, x, chart_y + Inches(4.05), bar_w, Inches(0.2),
             f'M{m+1}', size=8, color=CINZA_TXT, align=PP_ALIGN.CENTER)

# Marcadores
m50 = next((i for i, p in enumerate(pct_acum) if p >= 50), N_MONTHS-1) + 1
add_text(s, Inches(0.8), Inches(6.2), Inches(12), Inches(0.3),
         f'50% de avanço atingido no mês {m50}',
         size=12, bold=True, color=AZUL_PRIM, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.8), Inches(6.6), Inches(12), Inches(0.3),
         f'Entrega final (100%): mês {N_MONTHS}',
         size=11, color=CINZA_TXT, align=PP_ALIGN.CENTER)
add_footer(s, '19')


# ============================================================
# SLIDE 20 — Ressalvas e próximos passos
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, CINZA_FUNDO)
add_text(s, Inches(0.8), Inches(0.5), Inches(12), Inches(0.7),
         'RESSALVAS E PRÓXIMOS PASSOS', size=28, bold=True, color=AZUL_PRIM)

secoes = [
    ('⚠️ RESSALVAS',
     [
         'Produto de USO MISTO — valores não contemplam separação fina de custos comercial/residencial',
         'Gerenciamento já foi ajustado com overrides do Leo (22/abr) para refletir equipe real',
         'PU de fachada em torre de Centro Histórico pode sofrer ajuste por logística urbana',
         'Paramétrico V2 tem margem ±10% — não é substituto do orçamento executivo rastreável',
         'Itens de referência cross-projeto — não representam levantamento específico do CAD',
     ]),
    ('🎯 PRÓXIMOS PASSOS',
     [
         'Overrides de índices na aba INDICES durante a reunião (valor efetivo vs calculado)',
         'Alinhamento de pacote de acabamentos do cliente (contrato de entrega Completa)',
         'Definição de método construtivo de fachada (balancim x andaime tubular)',
         'Cronograma físico-financeiro detalhado após amarração de datas com cliente',
         'Preliminar rastreável com Visus/BIM se cliente aprovar passar ao executivo',
     ]),
]
y = Inches(1.4)
for title, bullets in secoes:
    add_rect(s, Inches(0.8), y, Inches(11.7), Inches(2.7), BRANCO)
    add_rect(s, Inches(0.8), y, Inches(0.15), Inches(2.7), AZUL_PRIM)
    add_text(s, Inches(1.05), y+Inches(0.1), Inches(11), Inches(0.4),
             title, size=15, bold=True, color=AZUL_PRIM)
    by = y + Inches(0.55)
    for b in bullets:
        add_text(s, Inches(1.15), by, Inches(11.2), Inches(0.38),
                 '• ' + b, size=11, color=PRETO)
        by += Inches(0.4)
    y += Inches(2.85)
add_footer(s, '20')


# ============================================================
# SLIDE 21 — Contato
# ============================================================
s = add_blank_slide()
add_rect(s, 0, 0, W, H, AZUL_NAVY)
add_text(s, Inches(0), Inches(1.5), W, Inches(1.5),
         'Cartesian', size=96, bold=True, color=BRANCO, align=PP_ALIGN.CENTER)
add_text(s, Inches(0), Inches(3.3), W, Inches(0.5),
         'Coordenação Técnica e Orçamentária', size=20, color=CINZA_LINHA, align=PP_ALIGN.CENTER)
add_rect(s, Inches(5.3), Inches(4.1), Inches(2.7), Inches(0.04), LARANJA)
add_text(s, Inches(0), Inches(4.3), W, Inches(0.5),
         'Leonardo Kock Adriano', size=20, bold=True, color=BRANCO, align=PP_ALIGN.CENTER)
add_text(s, Inches(0), Inches(4.9), W, Inches(0.4),
         'leonardo@cartesianengenharia.com', size=14, color=CINZA_LINHA, align=PP_ALIGN.CENTER)
add_text(s, Inches(0), Inches(5.35), W, Inches(0.4),
         'Itajaí/SC  |  Abril/2026', size=13, color=CINZA_LINHA, align=PP_ALIGN.CENTER)

add_rect(s, 0, Inches(6.5), W, Inches(1.0), AZUL_PRIM)
add_text(s, Inches(0.5), Inches(6.55), W - Inches(1.0), Inches(0.45),
         'RESIDENCIAL ARMÍNIO TAVARES — ORÇAMENTO PARAMÉTRICO V2 HÍBRIDO',
         size=16, bold=True, color=BRANCO, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.5), Inches(7.0), W - Inches(1.0), Inches(0.35),
         'Placon Empreendimentos  |  Florianópolis/SC',
         size=12, color=BRANCO, align=PP_ALIGN.CENTER)


# ============ SALVAR ============
prs.save(OUT_PATH)
print(f"\n✅ Apresentacao salva: {OUT_PATH}")
print(f"   Slides: {len(prs.slides)}")
print(f"   Tamanho: {os.path.getsize(OUT_PATH) / 1024:.0f} KB")
