#!/usr/bin/env python3
"""
Consolidador de PUs Cartesian — agrega pus-raw/*.json em base-pus-cartesian.json.

Passos:
  1. Carrega todos os pus-raw/{slug}-raw.json
  2. Agrupa itens por chave normalizada (dentro da mesma disciplina)
  3. Fuzzy merge de chaves similares (threshold 0.85, mesma disciplina)
  4. Calcula estatísticas: mediana, P25, P75, min, max, n_projetos
  5. Filtra: apenas itens com n_projetos >= 2
  6. Gera base-pus-cartesian.json + resumo.md + qualidade.md

Uso:
  python consolidar_base_pus.py                    # Consolidar tudo
  python consolidar_base_pus.py --no-fuzzy         # Sem fuzzy merge
  python consolidar_base_pus.py --threshold 0.90   # Fuzzy mais restritivo
"""

import os
import sys
import json
import re
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from statistics import median, quantiles

BASE_DIR = os.path.expanduser('~/orcamentos/base')
RAW_DIR = os.path.join(BASE_DIR, 'pus-raw')
METADADOS_PATH = os.path.join(BASE_DIR, 'projetos-metadados.json')
OUTPUT_PATH = os.path.join(BASE_DIR, 'base-pus-cartesian.json')
RESUMO_PATH = os.path.join(BASE_DIR, 'base-pus-cartesian-resumo.md')
QUALIDADE_PATH = os.path.join(BASE_DIR, 'pus-qualidade.md')
MERGE_LOG_PATH = os.path.join(BASE_DIR, 'pus-fuzzy-merges.log')


def load_all_raw():
    """Load all raw JSON files."""
    projetos = {}
    for fname in sorted(os.listdir(RAW_DIR)):
        if not fname.endswith('-raw.json'):
            continue
        slug = fname.replace('-raw.json', '')
        with open(os.path.join(RAW_DIR, fname), 'r', encoding='utf-8') as f:
            projetos[slug] = json.load(f)
    return projetos


def load_metadados():
    if os.path.exists(METADADOS_PATH):
        with open(METADADOS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def agrupar_por_chave(projetos):
    """Group items by (discipline, normalized_key).
    Returns dict: (discipline, key) -> list of {slug, pu, qty, unit, total, desc}
    """
    agrupado = defaultdict(list)

    for slug, data in projetos.items():
        ac = data.get('ac')
        for disc_label, disc_data in data.get('disciplinas', {}).items():
            for item in disc_data.get('itens', []):
                chave = item.get('chave_normalizada', '')
                if not chave or len(chave) < 3:
                    continue
                pu = item.get('pu')
                if not pu or pu <= 0:
                    continue

                agrupado[(disc_label, chave)].append({
                    'slug': slug,
                    'pu': pu,
                    'quantidade': item.get('quantidade'),
                    'unidade': item.get('unidade', ''),
                    'total': item.get('total', 0),
                    'descricao': item.get('descricao', ''),
                    'ac': ac,
                })

    return agrupado


def fuzzy_merge(agrupado, threshold=0.85):
    """Merge similar keys within the same discipline.
    Returns merged dict + log of merges.
    """
    merges = []

    # Group keys by discipline
    by_disc = defaultdict(list)
    for (disc, key) in agrupado:
        by_disc[disc].append(key)

    merged = dict(agrupado)  # copy

    for disc, keys in by_disc.items():
        keys_sorted = sorted(keys)
        merged_into = {}  # key -> canonical key

        for i, key_a in enumerate(keys_sorted):
            if key_a in merged_into:
                continue
            for j in range(i + 1, len(keys_sorted)):
                key_b = keys_sorted[j]
                if key_b in merged_into:
                    continue

                # Only compare keys of similar length (avoid merging "concreto" with "concreto_fck_35_mpa_bombeado")
                if abs(len(key_a) - len(key_b)) > max(len(key_a), len(key_b)) * 0.4:
                    continue

                ratio = SequenceMatcher(None, key_a, key_b).ratio()
                if ratio >= threshold:
                    # Merge key_b into key_a (keep the one with more entries)
                    entries_a = len(merged.get((disc, key_a), []))
                    entries_b = len(merged.get((disc, key_b), []))

                    if entries_b > entries_a:
                        canonical, absorbed = key_b, key_a
                    else:
                        canonical, absorbed = key_a, key_b

                    # Check unit compatibility
                    units_a = set(e['unidade'] for e in merged.get((disc, canonical), []) if e.get('unidade'))
                    units_b = set(e['unidade'] for e in merged.get((disc, absorbed), []) if e.get('unidade'))
                    if units_a and units_b and not units_a.intersection(units_b):
                        continue  # Different units, don't merge

                    merged[(disc, canonical)].extend(merged.pop((disc, absorbed), []))
                    merged_into[absorbed] = canonical
                    merges.append({
                        'disc': disc,
                        'canonical': canonical,
                        'absorbed': absorbed,
                        'ratio': round(ratio, 3),
                    })

    return merged, merges


def calcular_estatisticas(agrupado, min_projetos=2):
    """Calculate statistics per item. Returns dict of consolidated items."""
    base = {}

    for (disc, chave), entries in agrupado.items():
        # Unique projects
        projetos = list(set(e['slug'] for e in entries))
        if len(projetos) < min_projetos:
            continue

        pus = [e['pu'] for e in entries if e['pu'] and e['pu'] > 0]
        if not pus:
            continue

        pus_sorted = sorted(pus)
        n = len(pus_sorted)

        # Descriptions (pick most common)
        descs = [e['descricao'] for e in entries if e.get('descricao')]
        desc_counts = defaultdict(int)
        for d in descs:
            desc_counts[d] += 1
        best_desc = max(desc_counts, key=desc_counts.get) if desc_counts else chave

        # Unit (most common)
        units = [e['unidade'] for e in entries if e.get('unidade')]
        unit_counts = defaultdict(int)
        for u in units:
            unit_counts[u] += 1
        best_unit = max(unit_counts, key=unit_counts.get) if unit_counts else ''

        # CUB base (most recent)
        cub_bases = [e.get('ac') for e in entries if e.get('ac')]

        med = median(pus_sorted)
        if n >= 4:
            q = quantiles(pus_sorted, n=4)
            p25, p75 = q[0], q[2]
        else:
            p25, p75 = pus_sorted[0], pus_sorted[-1]

        base[f"{disc}::{chave}"] = {
            'descricao': best_desc,
            'categoria': disc,
            'chave': chave,
            'unidade': best_unit,
            'mediana': round(med, 2),
            'p25': round(p25, 2),
            'p75': round(p75, 2),
            'min': round(min(pus), 2),
            'max': round(max(pus), 2),
            'n_projetos': len(projetos),
            'n_observacoes': n,
            'projetos': projetos,
            'cv': round((max(pus) - min(pus)) / med, 2) if med > 0 else None,
            'data_base': datetime.now().strftime('%Y-%m'),
        }

    return base


def gerar_resumo(base):
    """Generate human-readable summary (top 200 items by frequency)."""
    items = sorted(base.values(), key=lambda x: (-x['n_projetos'], -x['mediana']))[:200]

    lines = [
        "# Base de PUs Cartesian — Resumo\n",
        f"**Data:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Total itens:** {len(base)}",
        f"**Itens com 3+ projetos:** {sum(1 for v in base.values() if v['n_projetos'] >= 3)}\n",
        "---\n",
    ]

    current_cat = None
    for item in items:
        cat = item['categoria']
        if cat != current_cat:
            lines.append(f"\n## {cat}\n")
            lines.append("| Item | Un | Mediana | P25-P75 | N |")
            lines.append("|------|-----|---------|---------|---|")
            current_cat = cat

        desc = item['descricao'][:50]
        lines.append(
            f"| {desc} | {item['unidade']} | "
            f"R$ {item['mediana']:,.2f} | "
            f"R$ {item['p25']:,.2f} — {item['p75']:,.2f} | "
            f"{item['n_projetos']} |"
        )

    with open(RESUMO_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Resumo salvo: {RESUMO_PATH}")


def gerar_qualidade(base, projetos, merges):
    """Generate quality report with outliers and issues."""
    lines = [
        "# Relatório de Qualidade — Base PUs Cartesian\n",
        f"**Data:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Projetos processados:** {len(projetos)}",
        f"**Itens únicos (n>=2):** {len(base)}",
        f"**Itens com 3+ projetos:** {sum(1 for v in base.values() if v['n_projetos'] >= 3)}",
        f"**Fuzzy merges realizados:** {len(merges)}\n",
        "---\n",
    ]

    # Outliers: items with CV > 1.0
    lines.append("\n## Itens com Alta Variabilidade (CV > 1.0)\n")
    lines.append("| Item | Categoria | Mediana | Min-Max | CV | N |")
    lines.append("|------|-----------|---------|---------|----|----|")
    outliers = sorted(
        [v for v in base.values() if v.get('cv') and v['cv'] > 1.0],
        key=lambda x: -x['cv']
    )
    for item in outliers[:30]:
        lines.append(
            f"| {item['descricao'][:40]} | {item['categoria']} | "
            f"R$ {item['mediana']:,.2f} | "
            f"R$ {item['min']:,.2f} — {item['max']:,.2f} | "
            f"{item['cv']:.1f} | {item['n_projetos']} |"
        )

    # Disciplines with few items
    lines.append("\n\n## Disciplinas com Poucos Itens Consolidados\n")
    disc_counts = defaultdict(int)
    for v in base.values():
        disc_counts[v['categoria']] += 1
    for disc, n in sorted(disc_counts.items(), key=lambda x: x[1]):
        flag = " **⚠ INSUFICIENTE**" if n < 5 else ""
        lines.append(f"- {disc}: {n} itens{flag}")

    # Projects with no AC
    metadados = load_metadados()
    no_ac = [slug for slug, m in metadados.items() if not m.get('ac')]
    if no_ac:
        lines.append(f"\n\n## Projetos sem AC ({len(no_ac)})\n")
        for slug in sorted(no_ac):
            lines.append(f"- {slug}")

    # Fuzzy merge summary
    if merges:
        lines.append(f"\n\n## Fuzzy Merges ({len(merges)})\n")
        lines.append("| Disciplina | Canonical | Absorbed | Ratio |")
        lines.append("|-----------|-----------|----------|-------|")
        for m in merges[:30]:
            lines.append(f"| {m['disc']} | {m['canonical'][:30]} | {m['absorbed'][:30]} | {m['ratio']} |")
        if len(merges) > 30:
            lines.append(f"\n*... e mais {len(merges) - 30} merges (ver pus-fuzzy-merges.log)*")

    with open(QUALIDADE_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Qualidade salvo: {QUALIDADE_PATH}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Consolidar base de PUs')
    parser.add_argument('--no-fuzzy', action='store_true', help='Pular fuzzy merge')
    parser.add_argument('--threshold', type=float, default=0.85, help='Threshold fuzzy match')
    parser.add_argument('--min-projetos', type=int, default=2, help='Min projetos por item')
    args = parser.parse_args()

    print("Carregando raw files...")
    projetos = load_all_raw()
    print(f"  {len(projetos)} projetos")

    print("Agrupando por chave normalizada...")
    agrupado = agrupar_por_chave(projetos)
    print(f"  {len(agrupado)} chaves únicas (disciplina + item)")

    merges = []
    if not args.no_fuzzy:
        print(f"Fuzzy merge (threshold={args.threshold})...")
        agrupado, merges = fuzzy_merge(agrupado, threshold=args.threshold)
        print(f"  {len(merges)} merges realizados")
        print(f"  {len(agrupado)} chaves após merge")

        # Save merge log
        with open(MERGE_LOG_PATH, 'w', encoding='utf-8') as f:
            json.dump(merges, f, ensure_ascii=False, indent=2)

    print("Calculando estatísticas...")
    base = calcular_estatisticas(agrupado, min_projetos=args.min_projetos)
    print(f"  {len(base)} itens com >= {args.min_projetos} projetos")

    # Save consolidated base
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(base, f, ensure_ascii=False, indent=2)
    print(f"Base salva: {OUTPUT_PATH}")

    # Generate reports
    gerar_resumo(base)
    gerar_qualidade(base, projetos, merges)

    # Summary stats
    print("\n" + "=" * 60)
    print("CONSOLIDAÇÃO COMPLETA")
    print("=" * 60)
    print(f"Projetos: {len(projetos)}")
    print(f"Itens consolidados (n>=2): {len(base)}")
    print(f"Itens com 3+ projetos: {sum(1 for v in base.values() if v['n_projetos'] >= 3)}")
    print(f"Itens com 5+ projetos: {sum(1 for v in base.values() if v['n_projetos'] >= 5)}")
    print(f"Fuzzy merges: {len(merges)}")

    disc_counts = defaultdict(int)
    for v in base.values():
        disc_counts[v['categoria']] += 1
    print("\nPor disciplina:")
    for disc, n in sorted(disc_counts.items(), key=lambda x: -x[1]):
        print(f"  {disc}: {n} itens")


if __name__ == '__main__':
    main()
