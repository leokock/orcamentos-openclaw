"""Filter candidates from first-pass CSV for second-pass Ollama extraction."""
import csv
import re
import json
import os

SRC = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-varredura-2026-04-22.csv'
OUT_CANDS = r'C:\Users\leona\orcamentos-openclaw\base\_candidatos_ollama.json'

patterns = re.compile(
    r'or[cç]amento_executivo|ger_executivo|gerenciamento|geren|canteiro|admin|indiretos',
    re.IGNORECASE,
)

cands = []
with open(SRC, encoding='utf-8') as f:
    rd = csv.DictReader(f)
    for row in rd:
        if row.get('grand_total') and row['grand_total'].strip():
            continue
        abas = row.get('abas_encontradas', '')
        if patterns.search(abas):
            # Keep only if file exists
            p = row.get('path', '')
            if p and os.path.isfile(p):
                cands.append({
                    'path': p,
                    'cliente': row.get('cliente', ''),
                    'projeto': row.get('projeto', ''),
                    'xlsx_name': row.get('xlsx_name', ''),
                    'abas_encontradas': abas,
                })

# Diversify — pick up to 30, max 2 per (cliente, projeto)
seen = {}
diversified = []
for c in cands:
    key = (c['cliente'], c['projeto'])
    if seen.get(key, 0) >= 1:
        continue
    seen[key] = seen.get(key, 0) + 1
    diversified.append(c)
    if len(diversified) >= 30:
        break

with open(OUT_CANDS, 'w', encoding='utf-8') as f:
    json.dump(diversified, f, ensure_ascii=False, indent=2)

print(f'Total candidatos pós-filtro: {len(cands)}')
print(f'Diversificados (1 por projeto): {len(diversified)}')
print(f'Salvos em: {OUT_CANDS}')
for i, c in enumerate(diversified):
    print(f'  {i+1:2d}. {c["cliente"][:18]:18s} | {c["projeto"][:30]:30s} | {c["xlsx_name"][:50]}')
