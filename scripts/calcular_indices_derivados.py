#!/usr/bin/env python3
"""Calculate derived parametric indices from existing extracted data."""
import json, os, sys, statistics

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\leona\orcamentos-openclaw\base'
INDICES_DIR = os.path.join(BASE, 'indices-executivo')
META_PATH = os.path.join(BASE, 'projetos-metadados.json')
CAL_PATH = os.path.join(BASE, 'calibration-indices.json')

with open(META_PATH, encoding='utf-8') as f:
    meta = json.load(f)

# Load all project data
projects = {}
for fname in os.listdir(INDICES_DIR):
    if not fname.endswith('.json'):
        continue
    slug = fname.replace('.json', '')
    with open(os.path.join(INDICES_DIR, fname), encoding='utf-8') as f:
        data = json.load(f)
    m = meta.get(slug, {})
    # Merge metadados into project data
    data['_meta'] = m
    data['_ac'] = m.get('ac') or data.get('ac')
    data['_total'] = m.get('total') or data.get('total')
    data['_rsm2'] = m.get('rsm2') or data.get('rsm2')
    data['_ur'] = m.get('ur')
    data['_cub'] = m.get('cub_valor')
    data['_prazo'] = m.get('prazo_meses')
    projects[slug] = data


def safe_div(a, b):
    if a and b and b > 0:
        return round(a / b, 4)
    return None


def calc_stats(values):
    if len(values) < 2:
        return None
    values = sorted(values)
    n = len(values)
    return {
        'n': n,
        'min': round(values[0], 4),
        'p10': round(values[max(0, int(n * 0.1))], 4),
        'p25': round(values[int(n * 0.25)], 4),
        'mediana': round(statistics.median(values), 4),
        'p75': round(values[int(n * 0.75)], 4),
        'p90': round(values[min(n - 1, int(n * 0.9))], 4),
        'max': round(values[-1], 4),
        'media': round(statistics.mean(values), 4),
    }


# === CALCULATE DERIVED INDICES ===

indices = {
    'produto': {},
    'estruturais': {},
    'instalacoes': {},
    'ci': {},
    'por_macrogrupo': {},
    'por_segmento': {},
}

# 1. Produto (AC/UR, Custo/UR, CUB Ratio)
ac_ur_vals = []
custo_ur_vals = []
cub_ratio_vals = []
burn_rate_vals = []

for slug, p in projects.items():
    ac = p['_ac']
    total = p['_total']
    ur = p['_ur']
    cub = p['_cub']
    prazo = p['_prazo']

    if ac and ur and isinstance(ur, (int, float)) and ur > 0 and 20 < ac / ur < 300:
        ac_ur_vals.append(ac / ur)
    if total and ur and isinstance(ur, (int, float)) and ur > 0:
        custo_ur = total / ur
        if 50000 < custo_ur < 2000000:
            custo_ur_vals.append(custo_ur)
    if ac and total and cub and isinstance(cub, (int, float)) and cub > 0:
        rsm2 = total / ac
        ratio = rsm2 / cub
        if 0.5 < ratio < 3.0:
            cub_ratio_vals.append(ratio)
    if total and prazo and isinstance(prazo, (int, float)) and prazo > 0:
        burn = total / prazo
        if burn > 100000:
            burn_rate_vals.append(burn)

indices['produto']['ac_por_ur'] = calc_stats(ac_ur_vals)
indices['produto']['custo_por_ur'] = calc_stats(custo_ur_vals)
indices['produto']['cub_ratio'] = calc_stats(cub_ratio_vals)
indices['produto']['burn_rate_mensal'] = calc_stats(burn_rate_vals)

print(f"=== ÍNDICES DE PRODUTO ===")
print(f"  AC/UR:       {indices['produto']['ac_por_ur']}")
print(f"  Custo/UR:    {indices['produto']['custo_por_ur']}")
print(f"  CUB Ratio:   {indices['produto']['cub_ratio']}")
print(f"  Burn Rate:   {indices['produto']['burn_rate_mensal']}")

# 2. Estruturais (consolidar de indices_estruturais)
concreto_m3_m2 = []
aco_kg_m3 = []
aco_kg_m2 = []
forma_m2_m2 = []

for slug, p in projects.items():
    ie = p.get('indices_estruturais', {})
    if not ie:
        continue
    ac = p['_ac']

    v = ie.get('concreto_m3_por_m2_ac')
    if v and 0.05 < v < 0.8:
        concreto_m3_m2.append(v)

    v = ie.get('aco_kg_por_m3_concreto')
    if v and 30 < v < 200:
        aco_kg_m3.append(v)

    aco = ie.get('aco_total_kg')
    if aco and ac and ac > 0:
        ratio = aco / ac
        if 5 < ratio < 100:
            aco_kg_m2.append(ratio)

    v = ie.get('forma_m2_por_m2_ac')
    if v and 0.3 < v < 3.0:
        forma_m2_m2.append(v)

indices['estruturais']['concreto_m3_por_m2_ac'] = calc_stats(concreto_m3_m2)
indices['estruturais']['aco_kg_por_m3_concreto'] = calc_stats(aco_kg_m3)
indices['estruturais']['aco_kg_por_m2_ac'] = calc_stats(aco_kg_m2)
indices['estruturais']['forma_m2_por_m2_ac'] = calc_stats(forma_m2_m2)

print(f"\n=== ÍNDICES ESTRUTURAIS ===")
for k, v in indices['estruturais'].items():
    if v:
        print(f"  {k}: n={v['n']} med={v['mediana']} avg={v['media']}")

# 3. Instalações % por subdisciplina
inst_pcts = {'hidrossanitarias': [], 'eletricas': [], 'preventivas': [], 'gas': [], 'telecom': []}

for slug, p in projects.items():
    total = p['_total']
    if not total or total <= 0:
        continue
    ib = p.get('instalacoes_breakdown', {})
    for disc in inst_pcts:
        val = ib.get(disc)
        if isinstance(val, dict):
            val = val.get('valor')
        if val and isinstance(val, (int, float)) and val > 0:
            pct = val / total
            if 0.001 < pct < 0.15:
                inst_pcts[disc].append(pct)

for disc, vals in inst_pcts.items():
    indices['instalacoes'][f'{disc}_pct_total'] = calc_stats(vals)

print(f"\n=== INSTALAÇÕES % DO TOTAL ===")
for k, v in indices['instalacoes'].items():
    if v:
        print(f"  {k}: n={v['n']} med={v['mediana']:.1%} avg={v['media']:.1%}")

# 4. CI subcategorias % do total
ci_pcts = {'projetos_consultorias': [], 'taxas_licencas': [], 'equipe_adm': [],
           'epcs': [], 'equipamentos_carga': [], 'ensaios': [], 'canteiro': []}

for slug, p in projects.items():
    total = p['_total']
    if not total or total <= 0:
        continue
    ci = p.get('ci_detalhado', {})
    for cat in ci_pcts:
        entry = ci.get(cat)
        val = None
        if isinstance(entry, dict):
            val = entry.get('valor')
        elif isinstance(entry, (int, float)):
            val = entry
        if val and val > 0:
            pct = val / total
            if 0.0001 < pct < 0.20:
                ci_pcts[cat].append(pct)

for cat, vals in ci_pcts.items():
    indices['ci'][f'{cat}_pct_total'] = calc_stats(vals)

print(f"\n=== CI % DO TOTAL ===")
for k, v in indices['ci'].items():
    if v:
        print(f"  {k}: n={v['n']} med={v['mediana']:.2%} avg={v['media']:.2%}")

# 5. R$/m² por macrogrupo
mg_names_std = [
    'Gerenciamento', 'Mov.Terra', 'Infraestrutura', 'Supraestrutura',
    'Alvenaria', 'Impermeabilização', 'Instalações', 'Sist.Especiais',
    'Climatização', 'Rev.Int.Parede', 'Teto', 'Pisos', 'Pintura',
    'Esquadrias', 'Louças', 'Fachada', 'Complementares', 'Imprevistos'
]

mg_rsm2 = {mg: [] for mg in mg_names_std}
mg_keywords = {
    'Gerenciamento': ['gerenciamento', 'gerenc', 'ci', 'admin', 'custos indiretos'],
    'Mov.Terra': ['moviment', 'terra', 'escav', 'terraplenagem'],
    'Infraestrutura': ['infraestr', 'fundaç', 'fundac', 'contenç', 'contenc', 'estaca'],
    'Supraestrutura': ['supraest', 'estrutura', 'concreto armado'],
    'Alvenaria': ['alvenar', 'vedaç', 'vedac', 'blocos', 'parede'],
    'Impermeabilização': ['impermeab'],
    'Instalações': ['instalaç', 'instalac', 'elétri', 'eletri', 'hidro', 'prevent'],
    'Sist.Especiais': ['especiai', 'elevador', 'equipamento'],
    'Climatização': ['climatiz', 'hvac', 'ar condicion', 'exaust'],
    'Rev.Int.Parede': ['revestimento', 'reboco', 'chapisco'],
    'Teto': ['teto', 'forro', 'gesso'],
    'Pisos': ['piso', 'paviment', 'contrapiso'],
    'Pintura': ['pintura', 'epóxi', 'epoxi', 'textura'],
    'Esquadrias': ['esquadr', 'vidro', 'alumín', 'alumin', 'guarda'],
    'Louças': ['louça', 'louca', 'metais', 'bancada'],
    'Fachada': ['fachad'],
    'Complementares': ['complement', 'paisag', 'limpeza', 'calçad'],
    'Imprevistos': ['imprevisto', 'contingên', 'contingen'],
}

for slug, p in projects.items():
    ac = p['_ac']
    if not ac or ac <= 0:
        continue
    mgs = p.get('macrogrupos', {})
    for mg_name, mg_data in mgs.items():
        val = mg_data.get('valor', 0) if isinstance(mg_data, dict) else 0
        if not val or val <= 0:
            continue
        rsm2 = val / ac
        # Match to standard name
        mg_lower = mg_name.lower()
        matched = False
        for std_name, keywords in mg_keywords.items():
            if any(kw in mg_lower for kw in keywords):
                if 1 < rsm2 < 3000:
                    mg_rsm2[std_name].append(rsm2)
                matched = True
                break

for mg, vals in mg_rsm2.items():
    indices['por_macrogrupo'][f'{mg}_rsm2'] = calc_stats(vals)

print(f"\n=== R$/m² POR MACROGRUPO ===")
for k, v in indices['por_macrogrupo'].items():
    if v and v['n'] >= 3:
        print(f"  {k}: n={v['n']} med=R${v['mediana']:,.0f} avg=R${v['media']:,.0f}")

# 6. Segmentar por porte
segments = {
    'pequeno_lt8k': (0, 8000),
    'medio_8k_15k': (8000, 15000),
    'grande_15k_25k': (15000, 25000),
    'extra_gt25k': (25000, 999999),
}

for seg_name, (ac_min, ac_max) in segments.items():
    seg_rsm2 = []
    for slug, p in projects.items():
        ac = p['_ac']
        rsm2 = p['_rsm2']
        if not ac or not rsm2:
            continue
        if ac_min <= ac < ac_max and 500 < rsm2 < 10000:
            seg_rsm2.append(rsm2)
    indices['por_segmento'][f'{seg_name}_rsm2'] = calc_stats(seg_rsm2)

print(f"\n=== R$/m² POR SEGMENTO ===")
for k, v in indices['por_segmento'].items():
    if v:
        print(f"  {k}: n={v['n']} med=R${v['mediana']:,.0f} avg=R${v['media']:,.0f}")

# 7. Elevador R$/un
elev_pu = []
for slug, p in projects.items():
    se = p.get('sistemas_especiais_detail', {})
    elev = se.get('elevadores', {})
    if isinstance(elev, dict) and elev.get('pu_un'):
        pu = elev['pu_un']
        if 50000 < pu < 1000000:
            elev_pu.append(pu)
    elif isinstance(elev, dict) and elev.get('valor') and elev.get('qtd'):
        qtd = elev['qtd']
        val = elev['valor']
        if qtd > 0:
            pu = val / qtd
            if 50000 < pu < 1000000:
                elev_pu.append(pu)

indices['produto']['elevador_pu_un'] = calc_stats(elev_pu)
print(f"\n=== ELEVADOR R$/UN ===")
if indices['produto']['elevador_pu_un']:
    v = indices['produto']['elevador_pu_un']
    print(f"  n={v['n']} med=R${v['mediana']:,.0f} avg=R${v['media']:,.0f}")

# Save
with open(CAL_PATH, 'w', encoding='utf-8') as f:
    json.dump(indices, f, indent=2, ensure_ascii=False)

print(f"\n✓ Salvo em {CAL_PATH}")
print(f"\nTotal de índices calculados: {sum(1 for cat in indices.values() for k, v in cat.items() if v and isinstance(v, dict) and v.get('n', 0) >= 2)}")
