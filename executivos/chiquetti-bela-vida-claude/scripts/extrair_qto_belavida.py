"""
Extrai quantitativos dos 5 arquivos da pasta `Lista de Quantidades` do projeto
Bela Vida (Chiquetti) para 5 arquivos extracao_{disc}.xlsx com formatacao
padronizada (cor por disciplina, aba EXTRACAO + RESUMO).

Saida em: ~/orcamentos/executivos/chiquetti-bela-vida-claude/extracao/

Uso:
    python scripts/extrair_qto_belavida.py
    python scripts/extrair_qto_belavida.py --check  (re-extrai e diffa contagens)
"""
import os, sys, math, argparse
from collections import defaultdict
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

BASE_DRIVE = r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Chiquetti e Dal Vesco\2024 - Bela Vida\04. Custo\Lista de Quantidades"
OUT_DIR = os.path.expanduser(r"~\orcamentos\executivos\chiquetti-bela-vida-claude\extracao")

# Cores por disciplina (hex sem #)
COLORS = {
    "CLI": "FFE0B2",  # laranja claro
    "ELE": "FFF59D",  # amarelo claro
    "HID": "BBDEFB",  # azul claro
    "SAN": "C8E6C9",  # verde claro
    "TEL": "D1C4E9",  # roxo claro
}

MACROGRUPO = {
    "CLI": "08 Climatizacao, Exaustao e Pressurizacao",
    "ELE": "07 Inst. Eletricas, Hidraulicas, GLP e Preventivas",
    "HID": "07 Inst. Eletricas, Hidraulicas, GLP e Preventivas",
    "SAN": "07 Inst. Eletricas, Hidraulicas, GLP e Preventivas",
    "TEL": "07 Inst. Eletricas, Hidraulicas, GLP e Preventivas",
}

DISCIPLINA = {
    "CLI": "Climatizacao",
    "ELE": "Eletrico",
    "HID": "Hidraulico",
    "SAN": "Sanitario",
    "TEL": "Telecom",
}

FILES = {
    "CLI": ("CDV_BLV_CLI_EX_000_GER_QTV_R02.xlsx", "EX R02"),
    "ELE": ("CDV_BLV_ELE_EP_000_GER_QNT_R00.xlsx", "EP R00"),
    "HID": ("CDV_BLV_HID_EX_000_DOC_QUANTITATIVO_R00.xlsx", "EX R00"),
    "SAN": ("CDV_BLV_SAN_EX_000_DOC_QUANTITATIVO_R00.xlsx", "EX R00"),
    "TEL": ("CDV_BLV_TEL_EP_000_GER_QNT_R00.xls", "EP R00"),
}

CLI_HEADER_IGNORE = {"TOTAL", "CLIMATIZACAO", "CLIMATIZAÇÃO"}

COLUMNS = [
    "Macrogrupo", "Disciplina", "Categoria fonte", "Subcategoria",
    "Codigo fonte", "Descricao", "Unidade", "Quantidade",
    "Pavimento", "Sheet origem", "Arquivo fonte", "Revisao fonte",
    "Observacao",
]


# ============================================================
# Helpers
# ============================================================

def to_num(v):
    if v is None: return None
    if isinstance(v, (int, float)):
        if isinstance(v, float) and math.isnan(v): return None
        return float(v)
    s = str(v).strip()
    if not s or s.lower() == "nan": return None
    try:
        return float(s)
    except Exception:
        try:
            return float(s.replace(",", "."))
        except Exception:
            return None

def clean(s):
    if s is None: return ""
    if isinstance(s, float) and math.isnan(s): return ""
    s = str(s).strip()
    if s.lower() == "nan": return ""
    return s.replace("\n", " ")

def norm_descr(s):
    """Remove prefixos comuns de export Revit."""
    if not s: return s
    for prefix in ["Tipos de tubos:", "Familia e tipo:", "Família e tipo:"]:
        if s.startswith(prefix):
            s = s[len(prefix):].strip()
    return s


# ============================================================
# Extractors por disciplina
# ============================================================

def extract_cli():
    fn, rev = FILES["CLI"]
    wb = openpyxl.load_workbook(os.path.join(BASE_DRIVE, fn), data_only=True)
    rows = []

    # Sheet principal
    ws = wb["Lista de Materiais"]
    current_cat = None
    seq = 0
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c, d = (row + (None,)*4)[:4]
        code_s = clean(a); descr_s = clean(b); un_s = clean(c)
        qtd = to_num(d)
        # Pular cabecalho do arquivo + linha de header de colunas (row 9: Item/Especificacao/Unid)
        if r_idx <= 9: continue
        if code_s and not descr_s and not un_s and qtd is None:
            if code_s.upper() in CLI_HEADER_IGNORE: continue
            current_cat = code_s
            continue
        if code_s and (qtd is not None or (un_s and descr_s)):
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["CLI"],
                "Disciplina": DISCIPLINA["CLI"],
                "Categoria fonte": current_cat or "?",
                "Subcategoria": "",
                "Codigo fonte": code_s,
                "Descricao": norm_descr(descr_s),
                "Unidade": un_s,
                "Quantidade": qtd,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Lista de Materiais",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })

    # Sheet auxiliar "Sheet1" - Dutos churrasqueira
    ws = wb["Sheet1"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        if r_idx <= 7: continue
        sys = row[3] if len(row) > 3 else None
        comm = row[4] if len(row) > 4 else None
        qtd = to_num(row[5]) if len(row) > 5 else None
        if comm and qtd is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["CLI"],
                "Disciplina": DISCIPLINA["CLI"],
                "Categoria fonte": "Dutos churrasqueira (Sheet1)",
                "Subcategoria": clean(sys),
                "Codigo fonte": f"SH1-{seq:03d}",
                "Descricao": clean(comm),
                "Unidade": "un",
                "Quantidade": qtd,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Sheet1",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "Dutos para churrasqueira",
            })

    return rows


def extract_ele():
    fn, rev = FILES["ELE"]
    wb = openpyxl.load_workbook(os.path.join(BASE_DRIVE, fn), data_only=True)
    ws = wb["ELETRICO"]
    raw = []  # (cat, descr, un, qtd, row)
    current_cat = None
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c = (row + (None,)*3)[:3]
        descr = clean(a); un = clean(b); qtd = to_num(c)
        if r_idx == 1: continue
        if descr and not un and qtd is None:
            current_cat = descr; continue
        if descr and qtd is not None:
            raw.append((current_cat or "?", descr, un, qtd, r_idx))

    # Dedupe: somar (cat, descr, un) iguais; marcar Observacao
    bucket = defaultdict(lambda: {"qtd": 0.0, "rows": [], "count": 0})
    for cat, descr, un, qtd, r_idx in raw:
        key = (cat, descr, un)
        bucket[key]["qtd"] += qtd
        bucket[key]["rows"].append(r_idx)
        bucket[key]["count"] += 1

    rows = []
    seq = 0
    for (cat, descr, un), info in bucket.items():
        seq += 1
        obs = f"merged: {info['count']} ocorrencias (rows {','.join(map(str, info['rows']))})" if info["count"] > 1 else ""
        rows.append({
            "Macrogrupo": MACROGRUPO["ELE"],
            "Disciplina": DISCIPLINA["ELE"],
            "Categoria fonte": cat,
            "Subcategoria": "",
            "Codigo fonte": f"ELE-{seq:03d}",
            "Descricao": descr,
            "Unidade": un,
            "Quantidade": info["qtd"],
            "Pavimento": "Nao Identificado",
            "Sheet origem": "ELETRICO",
            "Arquivo fonte": fn,
            "Revisao fonte": rev,
            "Observacao": obs,
        })
    return rows


def extract_hid():
    fn, rev = FILES["HID"]
    wb = openpyxl.load_workbook(os.path.join(BASE_DRIVE, fn), data_only=True)
    rows = []
    seq = 0

    # Tigre - Conexoes: col A=Sistema, B=Familia, C=Contador, D=Descricao
    ws = wb["Tigre - Conexões"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c, d = (row + (None,)*4)[:4]
        if r_idx <= 3: continue
        sys = clean(a); fam = clean(b); cnt = to_num(c); descr = clean(d) or fam
        if sys and cnt is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["HID"],
                "Disciplina": DISCIPLINA["HID"],
                "Categoria fonte": "Conexoes Tigre",
                "Subcategoria": sys,
                "Codigo fonte": f"HID-{seq:03d}",
                "Descricao": descr,
                "Unidade": "un",
                "Quantidade": cnt,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Tigre - Conexoes",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "Sistema Revit vazio na fonte" if sys == "Nao definido" or sys == "Não definido" else "",
            })

    # Tabela de acessorio: A=Sistema, B=Familia, C=Contador
    ws = wb["Tabela de acessório de tubo"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c = (row + (None,)*3)[:3]
        if r_idx <= 3: continue
        sys = clean(a); fam = clean(b); cnt = to_num(c)
        if sys and cnt is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["HID"],
                "Disciplina": DISCIPLINA["HID"],
                "Categoria fonte": "Acessorios de tubo",
                "Subcategoria": sys,
                "Codigo fonte": f"HID-{seq:03d}",
                "Descricao": fam,
                "Unidade": "un",
                "Quantidade": cnt,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Tabela de acessorio de tubo",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })

    # Quant de tubos: A=Sistema, B=Familia, C=Diam, D=Comp(m)
    ws = wb["Quant de tubos"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c, d = (row + (None,)*4)[:4]
        if r_idx <= 3: continue
        sys = clean(a); fam = norm_descr(clean(b)); diam = clean(c); comp = to_num(d)
        if sys and comp is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["HID"],
                "Disciplina": DISCIPLINA["HID"],
                "Categoria fonte": "Tubos",
                "Subcategoria": sys,
                "Codigo fonte": f"HID-{seq:03d}",
                "Descricao": f"{fam} - DN {diam}",
                "Unidade": "m",
                "Quantidade": comp,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Quant de tubos",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })

    # Quant de material hidraulico: A=Fabricante, B=Familia, C=Contador
    ws = wb["Quant de material hidráulico"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c = (row + (None,)*3)[:3]
        if r_idx <= 3: continue
        fab = clean(a); fam = clean(b); cnt = to_num(c)
        if fam and cnt is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["HID"],
                "Disciplina": DISCIPLINA["HID"],
                "Categoria fonte": "Material hidraulico",
                "Subcategoria": fab or "Sem fabricante",
                "Codigo fonte": f"HID-{seq:03d}",
                "Descricao": fam,
                "Unidade": "un",
                "Quantidade": cnt,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Quant de material hidraulico",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })
    return rows


def extract_san():
    fn, rev = FILES["SAN"]
    wb = openpyxl.load_workbook(os.path.join(BASE_DRIVE, fn), data_only=True)
    rows = []
    seq = 0

    def infer_sub(text):
        t = text.lower() if text else ""
        if "esgoto" in t: return "Esgoto"
        if "marrom" in t or "agua fria" in t or "água fria" in t: return "Agua Fria"
        return "Outros"

    # Quant de tubos: A=Familia, B=Diam, C=Comp
    ws = wb["Quant de tubos"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c = (row + (None,)*3)[:3]
        if r_idx <= 3: continue
        fam = norm_descr(clean(a)); diam = clean(b); comp = to_num(c)
        if fam and comp is not None:
            seq += 1
            sub = infer_sub(fam)
            rows.append({
                "Macrogrupo": MACROGRUPO["SAN"],
                "Disciplina": DISCIPLINA["SAN"],
                "Categoria fonte": "Tubos",
                "Subcategoria": sub,
                "Codigo fonte": f"SAN-{seq:03d}",
                "Descricao": f"{fam} - DN {diam}",
                "Unidade": "m",
                "Quantidade": comp,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Quant de tubos",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "Subcategoria inferida do nome da familia",
            })

    # Quant de material hidraulico: A=Familia, B=Contador
    ws = wb["Quant de material hidráulico"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b = (row + (None,)*2)[:2]
        if r_idx <= 3: continue
        fam = clean(a); cnt = to_num(b)
        if fam and cnt is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["SAN"],
                "Disciplina": DISCIPLINA["SAN"],
                "Categoria fonte": "Material hidraulico",
                "Subcategoria": "Materiais/Equipamentos",
                "Codigo fonte": f"SAN-{seq:03d}",
                "Descricao": fam,
                "Unidade": "un",
                "Quantidade": cnt,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Quant de material hidraulico",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })

    # Quant de conexao de tubo: A=Familia, B=Descricao, C=Contador
    ws = wb["Quant de conexão de tubo"]
    for r_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        a, b, c = (row + (None,)*3)[:3]
        if r_idx <= 3: continue
        fam = clean(a); descr = clean(b); cnt = to_num(c)
        if fam and cnt is not None:
            seq += 1
            text_for_sub = (descr or fam)
            sub = infer_sub(text_for_sub) if "Esgoto" in fam or "Esgoto" in descr or "Marrom" in fam or "Marrom" in descr else "Conexoes"
            rows.append({
                "Macrogrupo": MACROGRUPO["SAN"],
                "Disciplina": DISCIPLINA["SAN"],
                "Categoria fonte": "Conexoes de tubo",
                "Subcategoria": sub,
                "Codigo fonte": f"SAN-{seq:03d}",
                "Descricao": descr or fam,
                "Unidade": "un",
                "Quantidade": cnt,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "Quant de conexao de tubo",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })
    return rows


def extract_tel():
    fn, rev = FILES["TEL"]
    df = pd.read_excel(os.path.join(BASE_DRIVE, fn), sheet_name="CABEAMENTO", header=None)
    rows = []
    current_cat = None
    seq = 0
    for r_idx in range(len(df)):
        row = df.iloc[r_idx].tolist()
        a = row[0] if len(row) > 0 else None
        b = row[1] if len(row) > 1 else None
        c = row[2] if len(row) > 2 else None
        descr = clean(a); un = clean(b); qtd = to_num(c)
        if r_idx <= 1: continue
        if descr and not un and qtd is None:
            current_cat = descr; continue
        if descr and qtd is not None:
            seq += 1
            rows.append({
                "Macrogrupo": MACROGRUPO["TEL"],
                "Disciplina": DISCIPLINA["TEL"],
                "Categoria fonte": current_cat or "?",
                "Subcategoria": "",
                "Codigo fonte": f"TEL-{seq:03d}",
                "Descricao": descr,
                "Unidade": un,
                "Quantidade": qtd,
                "Pavimento": "Nao Identificado",
                "Sheet origem": "CABEAMENTO",
                "Arquivo fonte": fn,
                "Revisao fonte": rev,
                "Observacao": "",
            })
    return rows


# ============================================================
# Writer
# ============================================================

def write_xlsx(disc, rows, out_path):
    wb = openpyxl.Workbook()

    # ----- Aba EXTRACAO -----
    ws = wb.active
    ws.title = "EXTRACAO"

    color = COLORS[disc]
    header_fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    header_font = Font(bold=True, size=11)
    thin = Side(border_style="thin", color="999999")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header
    for col_idx, col_name in enumerate(COLUMNS, start=1):
        c = ws.cell(row=1, column=col_idx, value=col_name)
        c.fill = header_fill
        c.font = header_font
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border

    # Data
    for r_idx, item in enumerate(rows, start=2):
        for col_idx, col_name in enumerate(COLUMNS, start=1):
            v = item.get(col_name, "")
            c = ws.cell(row=r_idx, column=col_idx, value=v)
            c.border = border
            if col_name == "Quantidade" and isinstance(v, (int, float)):
                c.number_format = "#,##0.00"
                c.alignment = Alignment(horizontal="right")
            elif col_name == "Descricao":
                c.alignment = Alignment(wrap_text=True, vertical="top")

    # Column widths
    widths = {"Macrogrupo": 35, "Disciplina": 15, "Categoria fonte": 30, "Subcategoria": 22,
              "Codigo fonte": 12, "Descricao": 55, "Unidade": 8, "Quantidade": 12,
              "Pavimento": 18, "Sheet origem": 25, "Arquivo fonte": 38, "Revisao fonte": 12,
              "Observacao": 40}
    for col_idx, col_name in enumerate(COLUMNS, start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = widths.get(col_name, 15)
    ws.freeze_panes = "A2"
    ws.row_dimensions[1].height = 32

    # ----- Aba RESUMO -----
    ws2 = wb.create_sheet("RESUMO")
    ws2.cell(row=1, column=1, value=f"RESUMO - {disc} {DISCIPLINA[disc]}").font = Font(bold=True, size=14)
    ws2.cell(row=2, column=1, value=f"Arquivo fonte: {FILES[disc][0]}")
    ws2.cell(row=3, column=1, value=f"Revisao fonte: {FILES[disc][1]}")
    ws2.cell(row=4, column=1, value=f"Macrogrupo: {MACROGRUPO[disc]}")
    ws2.cell(row=5, column=1, value=f"Total de itens extraidos: {len(rows)}")
    ws2.cell(row=5, column=1).font = Font(bold=True)

    # Subtotal por Categoria fonte
    cats = defaultdict(int)
    subs = defaultdict(int)
    for it in rows:
        cats[it["Categoria fonte"]] += 1
        if it["Subcategoria"]:
            subs[it["Subcategoria"]] += 1

    r = 7
    ws2.cell(row=r, column=1, value="Itens por Categoria fonte").font = Font(bold=True)
    ws2.cell(row=r, column=1).fill = header_fill
    ws2.cell(row=r, column=2, value="Qtd itens").font = Font(bold=True)
    ws2.cell(row=r, column=2).fill = header_fill
    r += 1
    for cat, n in sorted(cats.items(), key=lambda kv: -kv[1]):
        ws2.cell(row=r, column=1, value=cat)
        ws2.cell(row=r, column=2, value=n)
        r += 1

    if subs:
        r += 1
        ws2.cell(row=r, column=1, value="Itens por Subcategoria").font = Font(bold=True)
        ws2.cell(row=r, column=1).fill = header_fill
        ws2.cell(row=r, column=2, value="Qtd itens").font = Font(bold=True)
        ws2.cell(row=r, column=2).fill = header_fill
        r += 1
        for sub, n in sorted(subs.items(), key=lambda kv: -kv[1]):
            ws2.cell(row=r, column=1, value=sub)
            ws2.cell(row=r, column=2, value=n)
            r += 1

    # Alertas
    r += 2
    ws2.cell(row=r, column=1, value="Alertas").font = Font(bold=True)
    ws2.cell(row=r, column=1).fill = header_fill
    r += 1
    has_obs = [it for it in rows if it["Observacao"]]
    obs_counts = defaultdict(int)
    for it in has_obs:
        obs_counts[it["Observacao"]] += 1
    for obs, n in sorted(obs_counts.items(), key=lambda kv: -kv[1]):
        ws2.cell(row=r, column=1, value=obs)
        ws2.cell(row=r, column=2, value=n)
        r += 1
    if not has_obs:
        ws2.cell(row=r, column=1, value="Nenhum alerta")
        r += 1

    ws2.column_dimensions["A"].width = 60
    ws2.column_dimensions["B"].width = 14

    wb.save(out_path)


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Apenas re-extrai e mostra contagens (sem regravar arquivos)")
    args = parser.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)

    extractors = {
        "CLI": extract_cli,
        "ELE": extract_ele,
        "HID": extract_hid,
        "SAN": extract_san,
        "TEL": extract_tel,
    }
    file_slugs = {
        "CLI": "extracao_cli_climatizacao.xlsx",
        "ELE": "extracao_ele_eletrica.xlsx",
        "HID": "extracao_hid_hidraulica.xlsx",
        "SAN": "extracao_san_sanitaria.xlsx",
        "TEL": "extracao_tel_telecom.xlsx",
    }

    print("=" * 70)
    print("Extracao de quantitativos - Bela Vida")
    print("=" * 70)
    summary = {}
    for disc, extractor in extractors.items():
        rows = extractor()
        n = len(rows)
        out = os.path.join(OUT_DIR, file_slugs[disc])
        summary[disc] = {"n": n, "file": out}
        if args.check:
            print(f"  [{disc}] {n} itens (dry-run)")
        else:
            write_xlsx(disc, rows, out)
            print(f"  [{disc}] {n} itens -> {os.path.basename(out)}")

    total = sum(s["n"] for s in summary.values())
    print(f"\nTotal: {total} itens em {len(summary)} arquivos")
    if not args.check:
        print(f"Saida: {OUT_DIR}")


if __name__ == "__main__":
    main()
