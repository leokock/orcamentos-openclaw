"""Process candidates via Ollama local (qwen2.5:14b) extracting Gerenciamento/Grand Total."""
import csv
import json
import os
import re
import sys
import time
from pathlib import Path

# Import doc_extractor from mcp-ollama
sys.path.insert(0, r'C:\Users\leona\openclaw\mcp-ollama')
from doc_extractor import read_xlsx_filtered

import requests

OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL = 'qwen2.5:14b'
TIMEOUT_S = 180

CANDS_JSON = r'C:\Users\leona\orcamentos-openclaw\base\_candidatos_ollama.json'
OUT_CSV = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-gemma-2026-04-22.csv'
LOG = r'C:\Users\leona\orcamentos-openclaw\base\executivos-gerenciamento-gemma-2026-04-22.log.txt'


def log(msg: str):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def pick_sheet(abas_str: str) -> str | None:
    """Pick the best candidate sheet for Gerenciamento extraction."""
    abas = [a.strip() for a in abas_str.split('|') if a.strip()]
    # Priority order
    priority_patterns = [
        r'^or[çc]amento_executivo$',
        r'^ger_executivo$',
        r'gerenciamento executivo',
        r'executivo$',
    ]
    for pat in priority_patterns:
        for a in abas:
            if re.search(pat, a, re.IGNORECASE):
                return a
    # Fallback: any sheet with keywords
    for a in abas:
        if re.search(r'or[çc]amento|executivo|gerenciamento', a, re.IGNORECASE):
            return a
    return None


def call_ollama(prompt: str) -> str:
    payload = {
        'model': MODEL,
        'prompt': prompt,
        'stream': False,
        'options': {'temperature': 0.0, 'num_ctx': 16384},
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
    r.raise_for_status()
    return r.json().get('response', '')


def parse_json(txt: str) -> dict | None:
    # Strip code fences
    txt = re.sub(r'^```(?:json)?\s*', '', txt.strip())
    txt = re.sub(r'\s*```$', '', txt.strip())
    # Find first { ... }
    m = re.search(r'\{[\s\S]*\}', txt)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def process(cand: dict, idx: int, total: int) -> dict:
    path = cand['path']
    abas = cand['abas_encontradas']
    sheet = pick_sheet(abas)

    result = {
        'idx': idx,
        'cliente': cand['cliente'],
        'projeto': cand['projeto'],
        'xlsx_name': cand['xlsx_name'],
        'path': path,
        'aba_usada': sheet or '',
        'total_gerenciamento_brl': '',
        'grand_total_brl': '',
        'ac_m2': '',
        'prazo_meses': '',
        'unidades_ur': '',
        'observacoes': '',
        'pct_gerenciamento': '',
        'rsm2_gerenciamento': '',
        'status': '',
        'tempo_s': '',
        'suspeito': '',
    }

    if not sheet:
        result['status'] = 'sem_aba'
        log(f'{idx}/{total}: {cand["cliente"]}/{cand["projeto"]} — SKIP (sem aba)')
        return result

    log(f'{idx}/{total}: {cand["cliente"]}/{cand["projeto"]} — aba={sheet} — lendo xlsx...')
    t0 = time.time()
    try:
        content = read_xlsx_filtered(path, [sheet])
    except Exception as e:
        result['status'] = f'erro_leitura: {type(e).__name__}'
        log(f'  ERRO leitura: {e}')
        return result

    if content.startswith('[ERRO]'):
        result['status'] = 'erro_leitura'
        result['observacoes'] = content[:200]
        log(f'  {content[:200]}')
        return result

    # Truncate if too big (already 300k cap in read_xlsx_filtered)
    n_chars = len(content)
    log(f'  Lido: {n_chars:,} chars — chamando {MODEL}...')

    prompt = f"""Abaixo está uma aba de planilha de orçamento executivo de obra (construção civil brasileira).

Extraia os seguintes valores monetários em reais (BRL):

1. total_gerenciamento_brl — VALOR TOTAL do macrogrupo GERENCIAMENTO (também chamado de "Canteiro e Indiretos", "Gerenciamento Técnico e Administrativo", "CI", "Administração da Obra", "Ger_Executivo"). Procure linhas como "TOTAL GERENCIAMENTO", "SUBTOTAL INDIRETOS", "Canteiro e Indiretos - Total", etc.

2. grand_total_brl — VALOR GRAND TOTAL / TOTAL GERAL DA OBRA (soma de TODOS os macrogrupos). Procure "TOTAL GERAL", "CUSTO TOTAL", "Total da Obra", última linha de totalização.

3. ac_m2 — Área Construída em m² (procure "Área Construída", "AC", "Área Total", só o número).

4. prazo_meses — prazo de execução em meses (procure "Prazo", "Duração"). null se não encontrar.

5. unidades_ur — número de unidades residenciais (UR, apartamentos). null se não encontrar.

IMPORTANTE:
- Valores em BRL como números decimais, sem "R$" nem separadores de milhar. Ex: 5062193.47
- Se não encontrar um valor com certeza, use null.
- Responda APENAS em JSON válido, sem explicação nem markdown.

Schema exato:
{{"total_gerenciamento_brl": 0.0, "grand_total_brl": 0.0, "ac_m2": 0.0, "prazo_meses": null, "unidades_ur": null, "observacoes": "breve nota"}}

Dados da planilha:
{content}
"""

    try:
        resp = call_ollama(prompt)
    except Exception as e:
        result['status'] = f'erro_ollama: {type(e).__name__}'
        result['tempo_s'] = f'{time.time()-t0:.1f}'
        log(f'  ERRO ollama: {e}')
        return result

    elapsed = time.time() - t0
    result['tempo_s'] = f'{elapsed:.1f}'

    data = parse_json(resp)
    if not data:
        result['status'] = 'parse_falhou'
        result['observacoes'] = resp[:200]
        log(f'  PARSE FALHOU ({elapsed:.0f}s): {resp[:200]}')
        return result

    tot_ger = data.get('total_gerenciamento_brl')
    gt = data.get('grand_total_brl')
    ac = data.get('ac_m2')

    result['total_gerenciamento_brl'] = tot_ger if tot_ger is not None else ''
    result['grand_total_brl'] = gt if gt is not None else ''
    result['ac_m2'] = ac if ac is not None else ''
    result['prazo_meses'] = data.get('prazo_meses') if data.get('prazo_meses') is not None else ''
    result['unidades_ur'] = data.get('unidades_ur') if data.get('unidades_ur') is not None else ''
    result['observacoes'] = (data.get('observacoes') or '')[:300]
    result['status'] = 'ok'

    # Validate: values realistic?
    suspeito = []
    if isinstance(gt, (int, float)):
        if gt > 500_000_000 or gt < 100_000:
            suspeito.append(f'grand_total_fora_range={gt}')
    if isinstance(tot_ger, (int, float)) and isinstance(gt, (int, float)) and gt > 0:
        pct = tot_ger / gt * 100
        result['pct_gerenciamento'] = f'{pct:.2f}'
        if pct < 2 or pct > 40:
            suspeito.append(f'pct_fora_range={pct:.1f}')
        if isinstance(ac, (int, float)) and ac > 0:
            result['rsm2_gerenciamento'] = f'{tot_ger/ac:.2f}'
    if isinstance(ac, (int, float)) and (ac < 100 or ac > 200_000):
        suspeito.append(f'ac_fora_range={ac}')
    if tot_ger is not None and gt is not None and isinstance(tot_ger, (int, float)) and isinstance(gt, (int, float)):
        if tot_ger > gt:
            suspeito.append('ger>total')

    result['suspeito'] = '; '.join(suspeito)
    marker = ' [SUSPEITO]' if suspeito else ''
    log(f'  OK ({elapsed:.0f}s): ger={tot_ger}, gt={gt}, ac={ac}{marker}')
    return result


def main():
    with open(CANDS_JSON, encoding='utf-8') as f:
        cands = json.load(f)

    log(f'Iniciando processamento de {len(cands)} candidatos (model={MODEL})')
    log(f'Saida CSV: {OUT_CSV}')

    # Open CSV for incremental writing
    fields = [
        'idx', 'cliente', 'projeto', 'xlsx_name', 'path', 'aba_usada',
        'total_gerenciamento_brl', 'grand_total_brl', 'ac_m2', 'prazo_meses',
        'unidades_ur', 'pct_gerenciamento', 'rsm2_gerenciamento', 'observacoes',
        'status', 'tempo_s', 'suspeito',
    ]
    t_start = time.time()
    ok_count = 0
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, c in enumerate(cands, 1):
            # Global timeout: 40 min
            if time.time() - t_start > 40 * 60:
                log(f'TIMEOUT 40min atingido — interrompendo em {i-1}/{len(cands)}')
                break
            try:
                row = process(c, i, len(cands))
            except Exception as e:
                log(f'  EXCEPTION: {type(e).__name__}: {e}')
                row = {k: '' for k in fields}
                row.update({
                    'idx': i, 'cliente': c['cliente'], 'projeto': c['projeto'],
                    'xlsx_name': c['xlsx_name'], 'path': c['path'],
                    'status': f'exception_{type(e).__name__}',
                })
            w.writerow({k: row.get(k, '') for k in fields})
            f.flush()
            if row.get('status') == 'ok':
                ok_count += 1

    log(f'DONE — {ok_count} válidos de {len(cands)} candidatos — tempo total {(time.time()-t_start)/60:.1f}min')


if __name__ == '__main__':
    main()
