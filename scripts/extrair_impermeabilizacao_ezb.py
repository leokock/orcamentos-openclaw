import openpyxl
from collections import defaultdict

wb = openpyxl.load_workbook(
    'planejamento/OBRA - Elizabeth/06. Dimensionamento de recursos/CTN-GSL_EZB - Orçamento Executivo_R03.xlsx',
    read_only=True, data_only=True
)
ws = wb['IMPERMEABILIZAÇÃO']

data = []
for row in ws.iter_rows(values_only=True):
    if row[3] != 'SERVIÇO':
        continue
    
    multiplicador = row[0]
    pavimento = row[2]
    descricao = str(row[5]) if row[5] else ''
    unid = row[6]
    qtd = row[7] if row[7] else 0
    sistema = row[8]
    ambiente = row[9]
    tipo_surface = str(row[10]) if row[10] else ''
    
    tipo = 'OUTRO'
    if tipo_surface.strip().startswith('PISO'):
        tipo = 'PISO'
    elif tipo_surface.strip().startswith('PAREDE'):
        tipo = 'PAREDE'
    elif tipo_surface.strip().startswith('TETO'):
        tipo = 'TETO'
    elif descricao.startswith('PISO:'):
        tipo = 'PISO'
    elif descricao.startswith('PAREDE:'):
        tipo = 'PAREDE'
    elif descricao.startswith('TETO:'):
        tipo = 'TETO'
    
    mult = 1
    if multiplicador == 'Tipo x8':
        mult = 8
    elif multiplicador == 'Penthouse x22':
        mult = 22
    
    data.append({
        'pavimento': pavimento,
        'multiplicador': multiplicador,
        'mult': mult,
        'descricao': descricao,
        'tipo': tipo,
        'qtd': qtd,
        'unid': unid,
        'sistema': sistema,
        'ambiente': ambiente,
        'qtd_total': qtd * mult
    })

# Totais gerais
total_piso = sum(d['qtd_total'] for d in data if d['tipo'] == 'PISO')
total_parede = sum(d['qtd_total'] for d in data if d['tipo'] == 'PAREDE')
total_teto = sum(d['qtd_total'] for d in data if d['tipo'] == 'TETO')

print("=== IMPERMEABILIZACAO E TRATAMENTOS - EZB ===")
print(f"TOTAL PISO:   {total_piso:.2f} m2")
print(f"TOTAL PAREDE: {total_parede:.2f} m2")
print(f"TOTAL TETO:   {total_teto:.2f} m2")
print(f"TOTAL GERAL:  {total_piso+total_parede+total_teto:.2f} m2")
print()

# Por pavimento
pav_groups = defaultdict(lambda: {'PISO': 0.0, 'PAREDE': 0.0, 'TETO': 0.0})
for d in data:
    if d['tipo'] in ['PISO', 'PAREDE', 'TETO']:
        pav_groups[d['pavimento']][d['tipo']] += d['qtd_total']

print("POR PAVIMENTO:")
for pav in sorted(pav_groups.keys(), key=lambda x: str(x)):
    g = pav_groups[pav]
    print(f"  {pav}: PISO={g['PISO']:.2f} | PAREDE={g['PAREDE']:.2f} | TETO={g['TETO']:.2f}")

print()

# Por sistema (IMPER)
sis_groups = defaultdict(lambda: {'PISO': 0.0, 'PAREDE': 0.0, 'TETO': 0.0})
for d in data:
    if d['tipo'] in ['PISO', 'PAREDE', 'TETO']:
        sys_key = str(d['sistema']) if d['sistema'] else 'N/A'
        sis_groups[sys_key][d['tipo']] += d['qtd_total']

print("POR SISTEMA:")
for sis in sorted(sis_groups.keys()):
    g = sis_groups[sis]
    total_s = g['PISO'] + g['PAREDE'] + g['TETO']
    print(f"  Sist. {sis}: PISO={g['PISO']:.2f} | PAREDE={g['PAREDE']:.2f} | TETO={g['TETO']:.2f} | TOTAL={total_s:.2f}")
