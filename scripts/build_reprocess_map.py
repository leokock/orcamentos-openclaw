#!/usr/bin/env python3
"""Build mapping of new projects to their xlsx paths for reprocessing."""
import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

DRIVE = r'G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo'
BASE = r'C:\Users\leona\orcamentos-openclaw\base'

with open(os.path.join(BASE, 'projetos-metadados.json'), encoding='utf-8') as f:
    meta = json.load(f)

new_slugs = sorted([s for s, m in meta.items() if m.get('processado_em', '') >= '2026-04-09'])

# Build file index from Drive (one pass)
file_index = {}
for client in os.listdir(DRIVE):
    client_path = os.path.join(DRIVE, client)
    if not os.path.isdir(client_path):
        continue
    for item in os.listdir(client_path):
        item_path = os.path.join(client_path, item)
        if os.path.isfile(item_path) and item.lower().endswith(('.xlsx', '.xls', '.xlsb')):
            file_index[item] = item_path
        elif os.path.isdir(item_path):
            for f in os.listdir(item_path):
                if f.lower().endswith(('.xlsx', '.xls', '.xlsb')):
                    file_index[f] = os.path.join(item_path, f)

mapping = []
for slug in new_slugs:
    arquivo = meta[slug].get('arquivo_fonte', '')
    path = file_index.get(arquivo, 'NOT_FOUND')
    m = meta[slug]
    mapping.append({
        'slug': slug,
        'path': path,
        'ac': m.get('ac'),
        'total': m.get('total'),
        'rsm2': m.get('rsm2'),
    })

with open(os.path.join(BASE, '_reprocess_mapping.json'), 'w', encoding='utf-8') as f:
    json.dump(mapping, f, indent=2, ensure_ascii=False)

for m in mapping:
    ac_s = f"{m['ac']:,.0f}" if m['ac'] else '?'
    tot_s = f"R${m['total']:,.0f}" if m['total'] else '?'
    found = 'OK' if m['path'] != 'NOT_FOUND' else 'MISSING'
    print(f"  {m['slug']}: AC={ac_s} Total={tot_s} [{found}]")

found_count = sum(1 for m in mapping if m['path'] != 'NOT_FOUND')
print(f"\nTotal: {len(mapping)} | Found: {found_count}")
