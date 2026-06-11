from __future__ import annotations

import shutil
from bisect import bisect_left
from pathlib import Path
from statistics import mean, median

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


PKG = Path(r"C:\Users\leona\orcamentos-openclaw\base\pacotes\flow-da-lagoa")
FINAL_DIR = Path(r"C:\Users\leona\orcamentos\parametricos\flow-da-lagoa")
INPUT = FINAL_DIR / "comparativo-flow-vs-similares-v03-analise-detalhada.xlsx"
OUTPUT = PKG / "comparativo-flow-vs-similares-v04-cub-presente.xlsx"
OUTPUT_MD = PKG / "ANALISE-CUB-PRESENTE-COMPARATIVO-FLOW-v04.md"

FLOW_AC = 15000.62
CURRENT_CUB_DATE = "2026-05"
CURRENT_CUB = 3096.25

# CUB-SC residencial multifamiliar/médio usado como indexador linear.
# Fontes: base local atualizacao-cub-dez23-fev26.xlsx, JSONs de índices e tabela histórica pública SENGE-SC.
CUB_SERIES = {
    "2022-11": 2633.22,
    "2023-02": 2662.47,
    "2023-03": 2671.65,
    "2023-08": 2718.92,
    "2024-01": 2752.67,
    "2024-04": 2757.56,
    "2024-11": 2863.73,
    "2025-03": 2916.12,
    "2025-04": 2923.52,
    "2025-05": 2934.53,
    "2025-06": 2965.54,
    "2025-07": 2978.02,
    "2025-08": 2993.04,
    "2025-09": 2999.38,
    "2025-10": 3003.02,
    "2025-11": 3008.84,
    "2025-12": 3012.64,
    "2026-01": 3019.26,
    "2026-02": 3028.45,
    "2026-03": 3037.72,
    "2026-04": 3064.10,
    "2026-05": CURRENT_CUB,
    "2026-06": CURRENT_CUB,
}

REF_OVERRIDES = {
    "Flow da Lagoa": ("2026-06", CURRENT_CUB, "CUB presente do próprio Flow"),
    "lumis-live": ("2023-02", 2662.47, "CUB explícito no JSON: cub_data_base 2023-02"),
    "mussi-empreendimentos-chelsea": ("2022-11", 2633.22, "Data inferida da pasta Chelsea Residence 11.2022"),
    "fonseca-empreendimentos-estoril": ("2026-01", 3019.26, "Data de entrega 2026-01-15; CUB da série"),
    "pavcor": ("2026-04", 3064.10, "Data inferida do entregável executivo R02 de 15/04/2026"),
    "neuhaus-origem": ("2023-08", 2718.92, "Data inferida da pasta 2023.08 - Origem 3300"),
    "pass-e-connect": ("2025-03", 2907.85, "CUB explícito no metadata: CUB/SC 2.907,85"),
    "nobria": ("2024-01", 2752.67, "CUB explícito no metadata: 2.752,67"),
    "mabrem-gran-torino": ("2024-04", 2757.56, "CUB explícito no JSON: cub_data_base 2024-04"),
    "cota-365": ("2025-07", 2965.54, "CUB explícito no JSON: cub_ref 2.965,54"),
    "hacasa-brisa-da-armacao": ("2024-11", 2863.73, "CUB explícito no JSON: cub_ref 2.863,73"),
}


def brl(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(value: float) -> str:
    return f"{value * 100:.1f}%".replace(".", ",")


def month_to_num(month: str) -> int:
    y, m = month.split("-")
    return int(y) * 12 + int(m)


def cub_for_month(month: str) -> tuple[float, str]:
    if month in CUB_SERIES:
        return CUB_SERIES[month], "direto"
    keys = sorted(CUB_SERIES, key=month_to_num)
    nums = [month_to_num(k) for k in keys]
    target = month_to_num(month)
    idx = bisect_left(nums, target)
    if idx == 0:
        return CUB_SERIES[keys[0]], f"extrapolado de {keys[0]}"
    if idx >= len(keys):
        return CUB_SERIES[keys[-1]], f"extrapolado de {keys[-1]}"
    k0, k1 = keys[idx - 1], keys[idx]
    n0, n1 = nums[idx - 1], nums[idx]
    v0, v1 = CUB_SERIES[k0], CUB_SERIES[k1]
    value = v0 + (v1 - v0) * ((target - n0) / (n1 - n0))
    return value, f"interpolado entre {k0} e {k1}"


def load_records():
    wb = load_workbook(INPUT, data_only=True)
    ws = wb["COMPARATIVO"]
    headers = [c.value for c in ws[1]]
    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        rec = dict(zip(headers, row))
        if rec.get("Empreendimento"):
            records.append(rec)
    return wb, records


def add_cub_sheet(wb, records):
    if "CUB_PRESENTE" in wb.sheetnames:
        del wb["CUB_PRESENTE"]
    ws = wb.create_sheet("CUB_PRESENTE", 1)

    blue = PatternFill("solid", fgColor="245AE4")
    orange = PatternFill("solid", fgColor="FD3400")
    gray = PatternFill("solid", fgColor="F4F4F4")
    white = Font(color="FFFFFF", bold=True)
    bold = Font(bold=True)
    thin = Side(style="thin", color="E7E7E9")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws["A1"] = "CORREÇÃO TEMPORAL POR CUB - VALOR PRESENTE"
    ws["A1"].font = Font(bold=True, size=14, color="111111")
    ws.merge_cells("A1:M1")
    ws["A2"] = f"CUB presente usado: {CURRENT_CUB_DATE} = {brl(CURRENT_CUB)}/m². Fórmula: valor presente = valor nominal × CUB presente / CUB referência."
    ws.merge_cells("A2:M2")

    headers = [
        "Empreendimento",
        "Data ref.",
        "CUB ref.",
        "Fonte CUB/data",
        "R$/m² nominal",
        "CUB equivalente nominal",
        "R$/m² presente",
        "Total presente na AC Flow",
        "Dif. R$/m² presente vs Flow",
        "Dif. % presente vs Flow",
        "Classificação",
        "Leitura",
        "Observação",
    ]
    ws.append(headers)

    corrected = []
    flow_present = None
    for rec in records:
        name = rec["Empreendimento"]
        ref_month, cub_ref, source = REF_OVERRIDES.get(name, (rec.get("Data base") or "", None, "Sem data suficiente"))
        if cub_ref is None and ref_month:
            cub_ref, method = cub_for_month(str(ref_month))
            source = f"{source}; CUB {method}"
        rsm2 = float(rec["R$/m²"])
        cub_equiv = rsm2 / cub_ref
        rsm2_present = cub_equiv * CURRENT_CUB
        total_present = rsm2_present * FLOW_AC
        if name == "Flow da Lagoa":
            flow_present = rsm2_present
        corrected.append((rec, ref_month, cub_ref, source, cub_equiv, rsm2_present, total_present))

    assert flow_present is not None

    for rec, ref_month, cub_ref, source, cub_equiv, rsm2_present, total_present in corrected:
        name = rec["Empreendimento"]
        diff = rsm2_present - flow_present
        diff_pct = (rsm2_present / flow_present) - 1
        if name == "Flow da Lagoa":
            klass = "Base"
            reading = "Valor presente base."
        elif rsm2_present < flow_present * 0.93:
            klass = "Abaixo do Flow corrigido"
            reading = "Serve como piso/pressão de baixa; validar escopo antes de reduzir Flow."
        elif rsm2_present > flow_present * 1.08:
            klass = "Acima do Flow corrigido"
            reading = "Serve como teto/pressão de alta; checar padrão e escopo."
        else:
            klass = "Faixa aderente"
            reading = "Bom comparável corrigido temporalmente."
        obs = ""
        if "inferida" in source.lower():
            obs = "Data inferida; revisar se houver data-base oficial."
        ws.append([
            name,
            ref_month,
            cub_ref,
            source,
            rec["R$/m²"],
            cub_equiv,
            rsm2_present,
            total_present,
            diff,
            diff_pct,
            klass,
            reading,
            obs,
        ])

    start = ws.max_row + 3
    direct_rows = [
        r for r in range(4, ws.max_row + 1)
        if ws.cell(r, 1).value != "Flow da Lagoa"
        and ws.cell(r, 11).value != "Acima do Flow corrigido"
    ]
    all_rows = [r for r in range(4, ws.max_row + 1) if ws.cell(r, 1).value != "Flow da Lagoa"]
    present_values_all = [ws.cell(r, 7).value for r in all_rows]
    present_values_direct = [ws.cell(r, 7).value for r in direct_rows]
    ws.cell(start, 1, "Indicador")
    ws.cell(start, 2, "Valor")
    ws.cell(start, 3, "Leitura")
    summary = [
        ("Flow presente", flow_present, "Base corrigida."),
        ("Média 10 comparáveis corrigidos", mean(present_values_all), "Inclui alto e misto."),
        ("Mediana 10 comparáveis corrigidos", median(present_values_all), "Centro da amostra corrigida."),
        ("Média sem limites acima do Flow", mean(present_values_direct), "Exclui os acima do Flow corrigido."),
        ("Mediana sem limites acima do Flow", median(present_values_direct), "Centro dos aderentes/pisos."),
    ]
    for item in summary:
        ws.append(item)

    for row in ws.iter_rows():
        for cell in row:
            cell.border = border
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    for row in (3, start):
        for cell in ws[row]:
            cell.fill = blue
            cell.font = white
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws["A2"].fill = orange
    ws["A2"].font = white
    for row in range(4, start - 2):
        if row % 2 == 0:
            for cell in ws[row]:
                cell.fill = gray
        for col in (3, 5, 7, 8, 9):
            ws.cell(row, col).number_format = 'R$ #,##0.00'
        ws.cell(row, 6).number_format = '0.000'
        ws.cell(row, 10).number_format = '0.0%'
    for row in range(start + 1, ws.max_row + 1):
        ws.cell(row, 2).number_format = 'R$ #,##0.00'
    for col in range(1, ws.max_column + 1):
        letter = get_column_letter(col)
        width = max(len(str(ws.cell(row, col).value or "")) for row in range(1, ws.max_row + 1))
        ws.column_dimensions[letter].width = min(max(width + 2, 12), 62)

    return {
        "flow_present": flow_present,
        "all_present": present_values_all,
        "direct_present": present_values_direct,
        "corrected": corrected,
    }


def write_md(stats):
    flow = stats["flow_present"]
    all_avg = mean(stats["all_present"])
    all_med = median(stats["all_present"])
    direct_avg = mean(stats["direct_present"])
    direct_med = median(stats["direct_present"])
    lines = [
        "# Análise temporal por CUB - Flow da Lagoa v04",
        "",
        f"CUB presente usado: {CURRENT_CUB_DATE} = {brl(CURRENT_CUB)}/m².",
        "",
        "## Conclusão executiva",
        "",
        f"- Flow permanece em {brl(flow)}/m² no valor presente, pois já foi gerado com CUB atual.",
        f"- Média dos 10 comparáveis corrigidos: {brl(all_avg)}/m².",
        f"- Mediana dos 10 comparáveis corrigidos: {brl(all_med)}/m².",
        f"- Média sem os comparáveis acima do Flow corrigido: {brl(direct_avg)}/m².",
        f"- Mediana sem os comparáveis acima do Flow corrigido: {brl(direct_med)}/m².",
        f"- Flow fica {pct(flow / all_med - 1)} acima da mediana geral corrigida.",
        "",
        "## Leitura",
        "",
        "- A correção por CUB reduz a distância de obras antigas que pareciam baratas nominalmente.",
        "- Pass-e Connect continua muito aderente ao Flow depois da correção.",
        "- Neuhaus Origem permanece acima do Flow e funciona como teto de padrão alto.",
        "- Pavcor fica muito próximo depois da correção, mas sua data foi inferida pelo entregável executivo.",
        "- Mussi Chelsea e Neuhaus têm data inferida por pasta; revisar se houver data-base oficial.",
        "",
        "## Critério",
        "",
        "- Fórmula: R$/m² presente = R$/m² nominal × CUB presente / CUB referência.",
        "- Quando havia CUB explícito no JSON, usei o CUB explícito.",
        "- Quando só havia data de entrega/data-base, usei a série CUB-SC.",
        "- Quando não havia data no consolidado, usei uma inferência documentada por pasta/entregável.",
    ]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    wb, records = load_records()
    stats = add_cub_sheet(wb, records)
    wb.save(OUTPUT)
    write_md(stats)
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUTPUT, FINAL_DIR / OUTPUT.name)
    shutil.copy2(OUTPUT_MD, FINAL_DIR / OUTPUT_MD.name)
    print(OUTPUT)
    print(FINAL_DIR / OUTPUT.name)


if __name__ == "__main__":
    main()
