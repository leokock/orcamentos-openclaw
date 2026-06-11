import openpyxl

wb = openpyxl.load_workbook(
    'planejamento/OBRA - Elizabeth/06. Dimensionamento de recursos/CTN-GSL_EZB - Orçamento Executivo_R03.xlsx',
    read_only=True, data_only=True
)
ws = wb['IMPERMEABILIZAÇÃO']

print("=== ESTRUTURA: linhas com SERVIÇO (todas as colunas A-L) ===")
print(f"{'ROW':<5} {'ColA(EAP)':<12} {'ColB(Medicao)':<30} {'ColC(Pav)':<36} {'ColD(Apoio)':<10} {'ColH(Qtd)':<10} {'ColI(IMPER)':<12} {'ColK(Total)'}")

count = 0
pav_counts = {}
for i, row in enumerate(ws.iter_rows(values_only=True), 1):
    if row[3] == 'SERVIÇO':
        pav = str(row[2])
        pav_counts[pav] = pav_counts.get(pav, 0) + 1
        if count < 5 or pav.startswith('10') or pav.startswith('17') or pav.startswith('18') or pav.startswith('39'):
            print(f"L{i:<4} colA={repr(row[0]):<12} colB={str(row[1])[:28]:<30} colC={pav[:34]:<36} colD={str(row[3]):<10} colH={str(row[7]):<10} colI={str(row[8]):<12} colK={row[10]}")
        count += 1

print(f"\nTotal linhas SERVIÇO: {count}")
print("\nItens por pavimento:")
for pav, cnt in pav_counts.items():
    print(f"  {pav}: {cnt} itens")

# Verificar total na linha subtotal 1.1.
print("\n=== LINHA SUBTOTAL 1.1. ===")
for i, row in enumerate(ws.iter_rows(values_only=True), 1):
    if row[4] == '1.1.':
        print(f"L{i}: colH={row[7]}, colI={row[8]}, colK={row[10]}, colQ(idx16)={row[16] if len(row)>16 else 'N/A'}")

# Verificar o total nos pavimento subtotals (linhas sem SERVIÇO nem None no apoio)
print("\n=== SUBTOTAIS POR PAVIMENTO (sem SERVIÇO) ===")
for i, row in enumerate(ws.iter_rows(values_only=True), 1):
    if row[2] and row[3] is None and row[4] and str(row[4]).startswith('1.1.') and len(str(row[4])) > 4:
        print(f"L{i}: item={row[4]}, pav={row[2]}, colH={row[7]}, colI={row[8]}")
