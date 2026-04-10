#!/usr/bin/env python3
"""Map all 126 projects to their xlsx paths on Google Drive."""
import json, os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

DRIVE = r'G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo'
BASE = r'C:\Users\leona\orcamentos-openclaw\base'

with open(os.path.join(BASE, 'projetos-metadados.json'), encoding='utf-8') as f:
    meta = json.load(f)

# Build complete file index from Drive (all xlsx/xls/xlsb)
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

def find_file(arquivo_fonte):
    """Try multiple strategies to find the xlsx."""
    if not arquivo_fonte:
        return None

    # Direct match
    if arquivo_fonte in file_index:
        return file_index[arquivo_fonte]

    # Strip "entrega-Client-Project--" prefix
    if arquivo_fonte.startswith('entrega-'):
        parts = arquivo_fonte.split('--', 1)
        if len(parts) == 2:
            real_name = parts[1]
            if real_name in file_index:
                return file_index[real_name]
            # Try with spaces around dashes
            for fname, fpath in file_index.items():
                if real_name.replace(' ', '') in fname.replace(' ', ''):
                    return fpath

    # Fuzzy: match by CTN code (e.g., CTN-ADR-CCP)
    ctn_match = re.search(r'(CTN[_-]\w+[_-]\w+)', arquivo_fonte)
    if ctn_match:
        code = ctn_match.group(1).replace('_', '-').upper()
        for fname, fpath in file_index.items():
            fname_code = re.search(r'(CTN[_-]\w+[_-]\w+)', fname)
            if fname_code:
                fc = fname_code.group(1).replace('_', '-').upper()
                if code[:10] == fc[:10]:
                    # Prefer .xlsx over .xls/.xlsb
                    if fpath.endswith('.xlsx'):
                        return fpath
        # Second pass: accept any format
        for fname, fpath in file_index.items():
            fname_code = re.search(r'(CTN[_-]\w+[_-]\w+)', fname)
            if fname_code:
                fc = fname_code.group(1).replace('_', '-').upper()
                if code[:10] == fc[:10]:
                    return fpath

    # MTH code match
    mth_match = re.search(r'(MTH[_-]\w+[_-]\w+)', arquivo_fonte)
    if mth_match:
        code = mth_match.group(1).replace('_', '-').upper()
        for fname, fpath in file_index.items():
            fname_code = re.search(r'(MTH[_-]\w+[_-]\w+)', fname)
            if fname_code:
                fc = fname_code.group(1).replace('_', '-').upper()
                if code[:10] == fc[:10]:
                    if fpath.endswith('.xlsx'):
                        return fpath
        for fname, fpath in file_index.items():
            fname_code = re.search(r'(MTH[_-]\w+[_-]\w+)', fname)
            if fname_code:
                fc = fname_code.group(1).replace('_', '-').upper()
                if code[:10] == fc[:10]:
                    return fpath

    return None

mapping = []
for slug in sorted(meta.keys()):
    arquivo = meta[slug].get('arquivo_fonte', '')
    path = find_file(arquivo)
    mapping.append({
        'slug': slug,
        'path': path or 'NOT_FOUND',
        'arquivo_fonte': arquivo,
    })

found = sum(1 for m in mapping if m['path'] != 'NOT_FOUND')
not_found = [m for m in mapping if m['path'] == 'NOT_FOUND']

with open(os.path.join(BASE, '_all_projects_mapping.json'), 'w', encoding='utf-8') as f:
    json.dump(mapping, f, indent=2, ensure_ascii=False)

print(f'Total: {len(mapping)} | Found: {found} | Missing: {len(not_found)}')
if not_found:
    print(f'\nNot found:')
    for m in not_found:
        print(f'  {m["slug"]}: {m["arquivo_fonte"][:60]}')
