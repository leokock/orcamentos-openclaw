"""Merge first-pass + Gemma results, compute new percentiles, update analysis docx."""
import csv
import statistics
from pathlib import Path

PASS1_CSV = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-varredura-2026-04-22.csv'
PASS2_CSV = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-gemma-2026-04-22.csv'


def f(v):
    if v is None or v == '':
        return None
    try:
        return float(v)
    except Exception:
        return None


def percentiles(values, pcts=(25, 50, 75, 85, 90)):
    if not values:
        return {p: None for p in pcts}
    sv = sorted(values)
    out = {}
    for p in pcts:
        if len(sv) == 1:
            out[p] = sv[0]
        else:
            k = (len(sv) - 1) * p / 100
            lo, hi = int(k), min(int(k) + 1, len(sv) - 1)
            out[p] = sv[lo] + (sv[hi] - sv[lo]) * (k - lo)
    return out


def main():
    combined = []  # list of dicts with ger, gt, ac, pct, rsm2, cliente, projeto, source

    # Pass 1: heuristic (has grand_total)
    with open(PASS1_CSV, encoding='utf-8') as fp:
        for row in csv.DictReader(fp):
            gt = f(row.get('grand_total'))
            ger = f(row.get('total_gerenciamento'))
            ac = f(row.get('ac_m2'))
            if gt and gt > 100_000 and ger and ger > 0:
                pct = ger / gt * 100
                rsm2 = (ger / ac) if (ac and ac > 0) else None
                combined.append({
                    'source': 'heuristica',
                    'cliente': row.get('cliente', ''),
                    'projeto': row.get('projeto', ''),
                    'ger': ger, 'gt': gt, 'ac': ac,
                    'pct': pct, 'rsm2': rsm2,
                })

    pass1_count = len(combined)

    # Pass 2: Ollama extractions (skip if also in pass1 or suspeito or invalid)
    pass1_keys = {(r['cliente'], r['projeto']) for r in combined}
    pass2_added = 0
    pass2_rejected = 0
    pass2_total = 0
    if Path(PASS2_CSV).is_file():
        with open(PASS2_CSV, encoding='utf-8') as fp:
            for row in csv.DictReader(fp):
                pass2_total += 1
                if row.get('status') != 'ok':
                    continue
                if row.get('suspeito'):
                    pass2_rejected += 1
                    continue
                gt = f(row.get('grand_total_brl'))
                ger = f(row.get('total_gerenciamento_brl'))
                ac = f(row.get('ac_m2'))
                if not (gt and gt > 500_000 and ger and ger > 0):
                    pass2_rejected += 1
                    continue
                pct = ger / gt * 100
                if pct < 2 or pct > 40:
                    pass2_rejected += 1
                    continue
                if ger > gt:
                    pass2_rejected += 1
                    continue
                key = (row.get('cliente', ''), row.get('projeto', ''))
                if key in pass1_keys:
                    continue
                rsm2 = (ger / ac) if (ac and 100 < ac < 200_000) else None
                combined.append({
                    'source': 'ollama',
                    'cliente': row.get('cliente', ''),
                    'projeto': row.get('projeto', ''),
                    'ger': ger, 'gt': gt, 'ac': ac,
                    'pct': pct, 'rsm2': rsm2,
                })
                pass2_added += 1

    # Stats
    print(f'\n=== BASE COMBINADA ===')
    print(f'Pass 1 (heurística): {pass1_count} projetos')
    print(f'Pass 2 (Ollama): {pass2_total} candidatos processados, {pass2_added} adicionados, {pass2_rejected} rejeitados')
    print(f'TOTAL COMBINADO: {len(combined)} projetos\n')

    pcts = [r['pct'] for r in combined]
    rsm2s = [r['rsm2'] for r in combined if r['rsm2']]

    print(f'=== GERENCIAMENTO — % do total ===')
    p_pct = percentiles(pcts)
    for k, v in p_pct.items():
        print(f'  P{k}: {v:.2f}%' if v else f'  P{k}: —')

    print(f'\n=== GERENCIAMENTO — R$/m² ===')
    p_rs = percentiles(rsm2s)
    for k, v in p_rs.items():
        print(f'  P{k}: R$ {v:,.2f}/m²' if v else f'  P{k}: —')

    # Subset: AC 3k-6k m² (similar ao Placon)
    sub = [r for r in combined if r['ac'] and 3000 <= r['ac'] <= 6000]
    print(f'\n=== SUBSET AC 3k-6k m² (similar Placon, n={len(sub)}) ===')
    if sub:
        p_pct_sub = percentiles([r['pct'] for r in sub])
        p_rs_sub = percentiles([r['rsm2'] for r in sub if r['rsm2']])
        for k, v in p_pct_sub.items():
            print(f'  P{k} %: {v:.2f}%' if v else f'  P{k} %: —')
        for k, v in p_rs_sub.items():
            print(f'  P{k} R$/m²: R$ {v:,.2f}' if v else f'  P{k} R$/m²: —')

    # Placon ref
    PLACON_AC = 4_340  # placeholder — ver parametrico
    PLACON_GER = None
    PLACON_GT = None

    # Print all
    print(f'\n=== TOP 10 POR % GERENCIAMENTO ===')
    for r in sorted(combined, key=lambda x: -x['pct'])[:10]:
        print(f'  {r["pct"]:5.2f}% | R${r["rsm2"] or 0:7.0f}/m² | AC {r["ac"] or 0:>6.0f} | {r["cliente"][:15]:15s}/{r["projeto"][:25]:25s} [{r["source"][:4]}]')

    # Save merged CSV
    OUT_MERGED = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-merged-2026-04-22.csv'
    with open(OUT_MERGED, 'w', encoding='utf-8', newline='') as fp:
        w = csv.DictWriter(fp, fieldnames=['source', 'cliente', 'projeto', 'ger', 'gt', 'ac', 'pct', 'rsm2'])
        w.writeheader()
        for r in combined:
            w.writerow(r)
    print(f'\nMerged CSV: {OUT_MERGED}')

    return {
        'pass1_count': pass1_count,
        'pass2_added': pass2_added,
        'pass2_rejected': pass2_rejected,
        'pass2_total': pass2_total,
        'total': len(combined),
        'percentiles_pct': p_pct,
        'percentiles_rsm2': p_rs,
        'combined': combined,
    }


if __name__ == '__main__':
    main()
