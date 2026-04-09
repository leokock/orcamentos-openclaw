#!/usr/bin/env python3
"""
Batch processor for new executivo projects on Google Drive.
Finds xlsx files in each project folder, picks the best one, and processes it.
"""

import sys
import os
import re
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['PYTHONIOENCODING'] = 'utf-8'

import processar_executivo as pe

# Override paths for Windows + Google Drive
DRIVE_ROOT = r'G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo'
pe.EXEC_DIR = DRIVE_ROOT


def normalize(s):
    """Normalize string for slug comparison."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower().replace(' ', '-')


def make_slug(client, project):
    """Create slug from client/project names."""
    return f"{normalize(client)}-{normalize(project)}"


def score_file(filename):
    """Score xlsx file to pick best candidate (higher = better)."""
    u = filename.upper()
    s = 0
    if 'EXECUTIVO' in u or 'COMPLETO' in u or 'ENTREGAVEL' in u or 'ENTREGÁVEL' in u:
        s += 20
    if 'ORÇAMENTO' in u or 'ORCAMENTO' in u:
        s += 10
    if 'APRESENTA' in u:
        s -= 5  # Prefer executivo over apresentação
    if 'GERENCIAMENTO' in u:
        s -= 3  # Gerenciamento is partial
    if 'EAP' in u:
        s -= 10  # EAP comentada is not a budget
    # Higher revision = better
    rev = re.search(r'R(\d+)', filename)
    if rev:
        s += int(rev.group(1))
    # Larger files tend to be more complete
    return s


def find_xlsx(folder):
    """Find xlsx/xls/xlsb files in a folder (non-recursive)."""
    files = []
    try:
        for f in os.listdir(folder):
            if f.lower().endswith(('.xlsx', '.xls', '.xlsb')):
                files.append(os.path.join(folder, f))
    except Exception:
        pass
    return files


def get_already_processed():
    """Get set of processed slugs from metadados."""
    meta = pe.load_metadados()
    return {slug for slug, m in meta.items() if m.get('status') == 'processado'}


def find_missing_projects():
    """Find all projects in Drive that haven't been processed."""
    processed = get_already_processed()
    missing = []

    for client_name in sorted(os.listdir(DRIVE_ROOT)):
        client_path = os.path.join(DRIVE_ROOT, client_name)
        if not os.path.isdir(client_path):
            continue

        # Check if files are at root level (no subfolders)
        subfolders = [d for d in os.listdir(client_path)
                      if os.path.isdir(os.path.join(client_path, d))]

        if not subfolders:
            # Files at root level - treat client as project too
            xlsx_files = find_xlsx(client_path)
            if xlsx_files:
                slug = normalize(client_name)
                if slug not in processed:
                    best = max(xlsx_files, key=lambda f: score_file(os.path.basename(f)))
                    missing.append({
                        'client': client_name,
                        'project': client_name,
                        'slug': slug,
                        'xlsx': best,
                        'all_xlsx': len(xlsx_files),
                    })
        else:
            for project_name in sorted(subfolders):
                project_path = os.path.join(client_path, project_name)
                xlsx_files = find_xlsx(project_path)
                if not xlsx_files:
                    continue

                slug = make_slug(client_name, project_name)
                if slug not in processed:
                    best = max(xlsx_files, key=lambda f: score_file(os.path.basename(f)))
                    missing.append({
                        'client': client_name,
                        'project': project_name,
                        'slug': slug,
                        'xlsx': best,
                        'all_xlsx': len(xlsx_files),
                    })

    return missing


def main():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 70)
    print("BATCH PROCESSAMENTO - NOVOS EXECUTIVOS")
    print("=" * 70)

    missing = find_missing_projects()
    print(f"\nProjetos faltantes com planilha: {len(missing)}")
    print()

    if '--dry-run' in sys.argv:
        for i, p in enumerate(missing, 1):
            print(f"  {i:2d}. [{p['slug']}] {p['client']}/{p['project']}")
            print(f"      Arquivo: {os.path.basename(p['xlsx'])}")
        print(f"\nTotal: {len(missing)} (dry run, nenhum processado)")
        return

    success = 0
    errors = 0
    results = []

    for i, p in enumerate(missing, 1):
        print(f"\n[{i}/{len(missing)}] {p['client']}/{p['project']}")
        print(f"  Arquivo: {os.path.basename(p['xlsx'])}")
        print(f"  Slug: {p['slug']}")

        try:
            meta, indices_data, raw_data = pe.processar_executivo(p['xlsx'], p['slug'])
            pe.salvar_outputs(p['slug'], meta, indices_data, raw_data)

            ac = meta.get('ac')
            total = meta.get('total')
            rsm2 = meta.get('rsm2')
            n_macros = len(indices_data.get('macrogrupos', {}))
            n_items = sum(
                len(items) for items in indices_data.get('disciplinas', {}).values()
            ) if indices_data.get('disciplinas') else 0

            results.append({
                'slug': p['slug'],
                'ac': ac,
                'total': total,
                'rsm2': rsm2,
                'macros': n_macros,
                'items': n_items,
                'status': 'ok',
            })
            success += 1
            print(f"  OK: AC={ac}, Total={total}, {n_macros} macrogrupos, {n_items} itens")

        except Exception as e:
            results.append({
                'slug': p['slug'],
                'status': 'erro',
                'erro': str(e),
            })
            errors += 1
            print(f"  ERRO: {e}")

        if i % 10 == 0:
            print(f"\n  >>> Progresso: {success} ok, {errors} erros, {len(missing) - i} restantes\n")

    # Summary
    print()
    print("=" * 70)
    print(f"BATCH COMPLETO: {success} ok, {errors} erros")
    print("=" * 70)

    print("\n--- RESULTADOS ---")
    for r in results:
        if r['status'] == 'ok':
            ac_str = f"AC={r['ac']:,.0f}" if r['ac'] else "AC=?"
            total_str = f"R${r['total']:,.0f}" if r['total'] else "Total=?"
            print(f"  OK  {r['slug']}: {ac_str}, {total_str}, {r['macros']}MG, {r['items']}itens")
        else:
            print(f"  ERR {r['slug']}: {r['erro'][:60]}")

    return success, errors


if __name__ == '__main__':
    main()
