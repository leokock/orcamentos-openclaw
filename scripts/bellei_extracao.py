"""
Extração de Quantidades por Pavimento — OBRA BELLEI (BSR)
Baseado na Documentação do Sistema de Extração v3.0

Estrutura da EAP:
- SUPRAESTRUTURA: pavimento na ETAPA ("SUPRAESTRUTURA - {PAV} - PILARES...")
- Demais CCs: pavimento na SUBETAPA ("Prefix - {PAV}")
  com expansão de Tipo A (x5), Tipo B (x5), Tipo C (x4), Tipo D (x4)

Output: uma aba por Célula Construtiva, com formato NOV-DOM adaptado.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import re
from collections import OrderedDict

INPUT_FILE  = r'C:\Users\leona\orcamentos\planejamento\OBRA - BELLEI\CTN-BSR_ATY - Orçamento Executivo_R01 -.xlsx'
OUTPUT_FILE = r'C:\Users\leona\orcamentos\planejamento\OBRA - BELLEI\BSR_Extracao_Quantidades.xlsx'

# ─── Expansão de tipos ────────────────────────────────────────────────────────
# Ordem dos andares intercalada conforme SUPRAESTRUTURA
TIPO_A_FLOORS = ['6° ANDAR', '8° ANDAR', '10° ANDAR', '12° ANDAR', '14° ANDAR']
TIPO_B_FLOORS = ['7° ANDAR', '9° ANDAR', '11° ANDAR', '13° ANDAR', '15° ANDAR']
TIPO_C_FLOORS = ['17° ANDAR', '19° ANDAR', '21° ANDAR', '23° ANDAR']
TIPO_D_FLOORS = ['18° ANDAR', '20° ANDAR', '22° ANDAR', '24° ANDAR']

TIPO_EXPAND = {
    'Tipo A (x5)': (TIPO_A_FLOORS, 5),
    'Tipo B (x5)': (TIPO_B_FLOORS, 5),
    'Tipo C (x4)': (TIPO_C_FLOORS, 4),
    'Tipo D (x4)': (TIPO_D_FLOORS, 4),
}

# Ordem canônica dos pavimentos (base → topo) — para SUBETAPA-based CCs
PAV_ORDER_SUB = [
    'Subsolo', 'Térreo', 'G1', 'G2', 'G3', 'G4', 'Lazer',
    '6° ANDAR', '7° ANDAR', '8° ANDAR', '9° ANDAR', '10° ANDAR',
    '11° ANDAR', '12° ANDAR', '13° ANDAR', '14° ANDAR', '15° ANDAR',
    'Garden',
    '17° ANDAR', '18° ANDAR', '19° ANDAR', '20° ANDAR',
    '21° ANDAR', '22° ANDAR', '23° ANDAR', '24° ANDAR',
    'Cobertura', 'Barrilete', 'Reservatório',
]

# Ordem para SUPRAESTRUTURA — via etapas diretas
PAV_ORDER_SUPRA = [
    'SUBSOLO', 'TÉRREO',
    '1° ANDAR', '2° ANDAR', '3° ANDAR', '4° ANDAR', '5° ANDAR',
    'POLIMENTO DOS PISOS',
    '6° ANDAR', '7° ANDAR', '8° ANDAR', '9° ANDAR', '10° ANDAR',
    '11° ANDAR', '12° ANDAR', '13° ANDAR', '14° ANDAR', '15° ANDAR',
    '16° ANDAR',
    '17° ANDAR', '18° ANDAR', '19° ANDAR', '20° ANDAR',
    '21° ANDAR', '22° ANDAR', '23° ANDAR', '24° ANDAR',
    '25° ANDAR', '26° ANDAR', '27° ANDAR',
]

# CCs sem breakdown por pavimento
CC_SEM_PAV = {
    'MOVIMENTAÇÃO DE TERRA', 'INFRAESTRUTURA', 'CONTENÇÃO',
    'COBERTURA / TELHADO', 'ESQUADRIAS', 'FACHADA', 'PISCINAS',
    'CONDOMÍNIO / ÁREAS COMUNS', 'LIMPEZA FINAL', 'IMPREVISTOS E CONTINGÊNCIAS'
}

# ─── Cores (NOV-DOM / GRL style) ────────────────────────────────────────────
CLR = {
    'cc_bg':    'FF2F5496',  # azul escuro — linha 1 (CC)
    'etapa_bg': 'FF4472C4',  # azul médio — linha 2 (etapa)
    'sub_bg':   'FF8FAADC',  # azul claro — linha 3 (serviço desc)
    'un_bg':    'FFC6EFCE',  # verde — linha 4 (unidade)
    'pav_bg':   'FFD6DCE4',  # cinza claro — coluna A
    'tot_bg':   'FFFFFF00',  # amarelo — TOTAL
    'white':    'FFFFFFFF',
    'gray':     'FFF2F2F2',
    'title':    'FFFFFFFF',  # fonte branca
}

def fill(hex_color):
    return PatternFill('solid', fgColor=hex_color)

def font_bold(color='FF000000', size=9):
    return Font(bold=True, color=color, size=size)

def font_normal(size=9):
    return Font(size=9)

def center_align():
    return Alignment(horizontal='center', vertical='center', wrap_text=True)

def left_align():
    return Alignment(horizontal='left', vertical='center', wrap_text=True)

thin = Side(style='thin', color='FFC0C0C0')
thin_border = Border(left=thin, right=thin, top=thin, bottom=thin)


# ─── Leitura da EAP ──────────────────────────────────────────────────────────
print("Lendo Ger_Executivo...")
wb_in = openpyxl.load_workbook(INPUT_FILE, data_only=True)
ws_in = wb_in['Ger_Executivo']

records = []  # lista de dicts com cc, etapa, subetapa, desc, un, qtd
cc = etapa = subetapa = ''

for row in ws_in.iter_rows(min_row=8, max_row=ws_in.max_row):
    h = row[7].value   # col H: NIVEL
    j = row[9].value   # col J: Descrição
    k = row[10].value  # col K: Unidade
    l = row[11].value  # col L: Quantidade

    if h == 'CÉLULA CONSTRUTIVA':
        cc = (j or '').strip()
    elif h == 'ETAPA':
        etapa = (j or '').strip()
    elif h == 'SUBETAPA':
        subetapa = (j or '').strip()
    elif h == 'SERVIÇO' and j:
        try:
            qtd = float(l) if l is not None else 0.0
        except (TypeError, ValueError):
            qtd = 0.0
        records.append({
            'cc': cc, 'etapa': etapa, 'subetapa': subetapa,
            'desc': str(j).strip(), 'un': str(k or '').strip(), 'qtd': qtd
        })

print(f"  {len(records)} serviços lidos.")

# ─── Helpers ──────────────────────────────────────────────────────────────────

def extract_pav_from_supra(etapa_name):
    """Extrai pavimento de etapa SUPRAESTRUTURA: 'SUPRAESTRUTURA - SUBSOLO - ...' → 'SUBSOLO'"""
    parts = etapa_name.split(' - ')
    if len(parts) >= 2:
        return parts[1].strip().upper()
    return etapa_name.upper()

def extract_pav_from_sub(subetapa_name):
    """Extrai pavimento de subetapa: 'Prefix - {PAV}' → '{PAV}'"""
    if ' - ' in subetapa_name:
        return subetapa_name.rsplit(' - ', 1)[1].strip()
    return subetapa_name.strip()

def extract_prefix_from_sub(subetapa_name):
    """Extrai prefixo de subetapa: 'Prefix - {PAV}' → 'Prefix'"""
    if ' - ' in subetapa_name:
        return subetapa_name.rsplit(' - ', 1)[0].strip()
    return subetapa_name.strip()

def sort_key_pav(pav, order):
    try:
        return order.index(pav)
    except ValueError:
        return 9999

def safe_sheet_name(name):
    """Sanitiza nome de aba para Excel (max 31 chars, sem chars especiais)"""
    name = re.sub(r'[\\\/\*\?\[\]:]', '', name)
    return name[:31]


# ─── Construção de dados por CC ───────────────────────────────────────────────

def build_cc_data_sem_pav(cc_records):
    """
    Para CCs sem breakdown por pavimento.
    Retorna: { (etapa, subetapa, desc, un): qtd }
    """
    data = OrderedDict()
    for r in cc_records:
        key = (r['etapa'], r['subetapa'], r['desc'], r['un'])
        data[key] = r['qtd']
    return data

def build_cc_data_supra(cc_records):
    """
    Para SUPRAESTRUTURA: pavimento na etapa.
    Retorna:
      - col_keys: lista de (etapa_base, subetapa, desc, un) — colunas únicas
      - pav_order: lista de pavimentos na ordem correta
      - matrix: { pav: { col_key: qtd } }
    """
    # Coletar colunas e dados
    col_keys = []
    col_set = set()
    matrix = OrderedDict()
    pavs_found = []

    for r in cc_records:
        pav = extract_pav_from_supra(r['etapa'])
        col = (r['subetapa'], r['desc'], r['un'])

        if pav not in matrix:
            matrix[pav] = {}
            pavs_found.append(pav)
        if col not in col_set:
            col_set.add(col)
            col_keys.append(col)

        matrix[pav][col] = r['qtd']

    # Ordenar pavimentos
    pavs_sorted = sorted(pavs_found, key=lambda p: sort_key_pav(p, PAV_ORDER_SUPRA))

    return col_keys, pavs_sorted, matrix

def build_cc_data_sub(cc_records):
    """
    Para CCs com pavimento na SUBETAPA, com expansão de Tipo A/B/C/D.
    Retorna:
      - col_keys: lista de (prefix, desc, un)
      - pav_order: lista de pavimentos expandidos, na ordem
      - matrix: { pav: { col_key: qtd } }
    """
    col_keys = []
    col_set = set()
    matrix = OrderedDict()
    pavs_found = []

    for r in cc_records:
        pav_raw = extract_pav_from_sub(r['subetapa'])
        prefix = extract_prefix_from_sub(r['subetapa'])
        col = (prefix, r['desc'], r['un'])
        qtd = r['qtd']

        if col not in col_set:
            col_set.add(col)
            col_keys.append(col)

        # Verificar se é tipo expansível
        if pav_raw in TIPO_EXPAND:
            floors, n = TIPO_EXPAND[pav_raw]
            qtd_per_floor = (qtd / n) if n > 0 else 0
            for fl in floors:
                if fl not in matrix:
                    matrix[fl] = {}
                    pavs_found.append(fl)
                matrix[fl][col] = qtd_per_floor
        else:
            if pav_raw not in matrix:
                matrix[pav_raw] = {}
                pavs_found.append(pav_raw)
            matrix[pav_raw][col] = qtd

    # Ordenar pavimentos
    pavs_sorted = sorted(set(pavs_found), key=lambda p: sort_key_pav(p, PAV_ORDER_SUB))

    return col_keys, pavs_sorted, matrix


# ─── Escrita do Excel ─────────────────────────────────────────────────────────

def write_sheet_sem_pav(ws, cc_name, data):
    """Aba simples para CCs sem pavimento: etapa/subetapa/serviço em lista."""
    # Cabeçalho
    ws.row_dimensions[1].height = 20
    ws['A1'] = cc_name
    ws['A1'].fill = fill(CLR['cc_bg'])
    ws['A1'].font = font_bold(CLR['title'], 10)
    ws['A1'].alignment = left_align()
    ws.merge_cells('A1:F1')

    ws['A2'] = 'Etapa'
    ws['B2'] = 'Subetapa'
    ws['C2'] = 'Serviço'
    ws['D2'] = 'UN'
    ws['E2'] = 'Quantidade'
    for col in ['A', 'B', 'C', 'D', 'E']:
        ws[f'{col}2'].fill = fill(CLR['etapa_bg'])
        ws[f'{col}2'].font = font_bold(CLR['title'])
        ws[f'{col}2'].alignment = center_align()
        ws.column_dimensions[col].width = 25

    row_idx = 3
    for (etapa, subetapa, desc, un), qtd in data.items():
        bg = CLR['white'] if (row_idx % 2 == 1) else CLR['gray']
        for col, val in zip(['A', 'B', 'C', 'D', 'E'],
                             [etapa, subetapa, desc, un, qtd]):
            cell = ws[f'{col}{row_idx}']
            cell.value = val
            cell.fill = fill(bg)
            cell.font = font_normal()
            cell.border = thin_border
            if col == 'E':
                cell.number_format = '#,##0.00'
                cell.alignment = center_align()
            else:
                cell.alignment = left_align()
        row_idx += 1

    ws.column_dimensions['C'].width = 50
    ws.freeze_panes = 'A3'


def write_sheet_pivot(ws, cc_name, col_keys, pavs, matrix, is_supra=False):
    """
    Aba pivô: rows=pavimentos, cols=serviços.
    Header de 4 linhas (CC / etapa-prefix / desc / un).
    """
    HEADER_ROWS = 4
    DATA_COL_START = 2  # col B em diante

    # ── Dimensões ──
    ws.row_dimensions[1].height = 22
    ws.row_dimensions[2].height = 18
    ws.row_dimensions[3].height = 40
    ws.row_dimensions[4].height = 14

    # Col A: pavimentos
    ws.column_dimensions['A'].width = 22

    # ── Col A cabeçalho ──
    ws.cell(1, 1, 'Pavimento')
    ws.cell(1, 1).fill = fill(CLR['cc_bg'])
    ws.cell(1, 1).font = font_bold(CLR['title'], 10)
    ws.cell(1, 1).alignment = center_align()
    ws.merge_cells(start_row=1, start_column=1, end_row=4, end_column=1)

    # ── CC name no topo como título ──
    # Escrever CC name na linha 1, mergeando todas as colunas
    last_col = DATA_COL_START + len(col_keys) - 1
    if last_col >= DATA_COL_START:
        ws.cell(1, 2, cc_name)
        ws.cell(1, 2).fill = fill(CLR['cc_bg'])
        ws.cell(1, 2).font = font_bold(CLR['title'], 11)
        ws.cell(1, 2).alignment = center_align()
        if last_col > 2:
            ws.merge_cells(start_row=1, start_column=2, end_row=1, end_column=last_col)

    # ── Colunas de dados: header linhas 2-4 ──
    prev_prefix = None
    prefix_start_col = None

    for i, col_key in enumerate(col_keys):
        excel_col = DATA_COL_START + i

        if is_supra:
            prefix, desc, un = col_key   # (subetapa, desc, un)
        else:
            prefix, desc, un = col_key   # (subetapa_prefix, desc, un)

        # Linha 2: prefix (etapa/subetapa agrupador) — merge células com mesmo prefix
        cell2 = ws.cell(2, excel_col, prefix)
        cell2.fill = fill(CLR['etapa_bg'])
        cell2.font = font_bold(CLR['title'], 9)
        cell2.alignment = center_align()
        ws.column_dimensions[get_column_letter(excel_col)].width = 14

        # Linha 3: descrição do serviço
        cell3 = ws.cell(3, excel_col, desc)
        cell3.fill = fill(CLR['sub_bg'])
        cell3.font = font_normal()
        cell3.alignment = center_align()

        # Linha 4: unidade
        cell4 = ws.cell(4, excel_col, f'({un})')
        cell4.fill = fill(CLR['un_bg'])
        cell4.font = font_normal()
        cell4.alignment = center_align()

    # Merge células de prefix consecutivos na linha 2
    # (fazer após escrever tudo)
    if col_keys:
        run_prefix = col_keys[0][0]
        run_start = DATA_COL_START
        for i, col_key in enumerate(col_keys[1:], start=1):
            pfx = col_key[0]
            if pfx != run_prefix:
                # Fechar merge anterior
                end_col = DATA_COL_START + i - 1
                if end_col > run_start:
                    ws.merge_cells(start_row=2, start_column=run_start,
                                   end_row=2, end_column=end_col)
                run_prefix = pfx
                run_start = DATA_COL_START + i
        # último grupo
        end_col = DATA_COL_START + len(col_keys) - 1
        if end_col > run_start:
            ws.merge_cells(start_row=2, start_column=run_start,
                           end_row=2, end_column=end_col)

    # ── Dados por pavimento ──
    for pav_idx, pav in enumerate(pavs):
        excel_row = HEADER_ROWS + 1 + pav_idx
        bg = CLR['white'] if (pav_idx % 2 == 0) else CLR['gray']

        # Coluna A: pavimento
        cell_a = ws.cell(excel_row, 1, pav)
        cell_a.fill = fill(CLR['pav_bg'])
        cell_a.font = font_bold()
        cell_a.alignment = left_align()
        cell_a.border = thin_border

        # Dados
        pav_data = matrix.get(pav, {})
        for i, col_key in enumerate(col_keys):
            excel_col = DATA_COL_START + i
            qtd = pav_data.get(col_key, None)
            cell = ws.cell(excel_row, excel_col)
            if qtd is not None and qtd != 0:
                cell.value = round(qtd, 2)
                cell.number_format = '#,##0.00'
            else:
                cell.value = None
            cell.fill = fill(bg)
            cell.font = font_normal()
            cell.alignment = center_align()
            cell.border = thin_border

    # ── Linha de TOTAL ──
    if pavs:
        tot_row = HEADER_ROWS + 1 + len(pavs)
        cell_tot_a = ws.cell(tot_row, 1, 'TOTAL')
        cell_tot_a.fill = fill(CLR['tot_bg'])
        cell_tot_a.font = font_bold()
        cell_tot_a.alignment = center_align()
        cell_tot_a.border = thin_border

        for i in range(len(col_keys)):
            excel_col = DATA_COL_START + i
            data_start = HEADER_ROWS + 1
            data_end = HEADER_ROWS + len(pavs)
            col_letter = get_column_letter(excel_col)
            cell = ws.cell(tot_row, excel_col)
            cell.value = f'=SUM({col_letter}{data_start}:{col_letter}{data_end})'
            cell.number_format = '#,##0.00'
            cell.fill = fill(CLR['tot_bg'])
            cell.font = font_bold()
            cell.alignment = center_align()
            cell.border = thin_border

    # Congelar painéis em B5 (cabeçalho + col pavimento)
    ws.freeze_panes = 'B5'


# ─── MAIN ─────────────────────────────────────────────────────────────────────

print("Construindo workbook de saída...")
wb_out = openpyxl.Workbook()
wb_out.remove(wb_out.active)  # remove aba default

# Agrupar records por CC
from collections import defaultdict
by_cc = defaultdict(list)
for r in records:
    by_cc[r['cc']].append(r)

# Ordem das abas: manter ordem original das CCs
cc_order = list(dict.fromkeys(r['cc'] for r in records))

for cc_name in cc_order:
    cc_records = by_cc[cc_name]
    sheet_name = safe_sheet_name(cc_name)
    ws = wb_out.create_sheet(sheet_name)

    if cc_name in CC_SEM_PAV:
        # Lista simples sem pivot por pavimento
        data = build_cc_data_sem_pav(cc_records)
        write_sheet_sem_pav(ws, cc_name, data)
        print(f"  [{cc_name}] → aba simples ({len(data)} itens)")

    elif cc_name == 'SUPRAESTRUTURA':
        col_keys, pavs, matrix = build_cc_data_supra(cc_records)
        write_sheet_pivot(ws, cc_name, col_keys, pavs, matrix, is_supra=True)
        print(f"  [{cc_name}] → pivot {len(pavs)} pavs × {len(col_keys)} cols")

    else:
        col_keys, pavs, matrix = build_cc_data_sub(cc_records)
        write_sheet_pivot(ws, cc_name, col_keys, pavs, matrix, is_supra=False)
        print(f"  [{cc_name}] → pivot {len(pavs)} pavs × {len(col_keys)} cols")

print(f"\nSalvando em {OUTPUT_FILE}...")
wb_out.save(OUTPUT_FILE)
print("✓ Extração concluída!")
