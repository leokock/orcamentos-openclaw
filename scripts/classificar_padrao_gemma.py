#!/usr/bin/env python3
"""Phase 18 — Classificacao de padrao via Gemma local.

Para cada um dos 126 projetos da base, coleta sinais (itens de Pisos,
Esquadrias, Loucas, Fachada + metricas numericas + flags de assinatura)
e pergunta pro Gemma classificar em {economico, medio, medio-alto, alto, luxo}
com justificativa rastreavel.

Pipeline retomavel:
- Fila em base/phase18-queue.json (status por projeto)
- Log append em base/phase18-classificacao.log.jsonl
- Output por projeto em base/padroes-classificados/{slug}.json
- Consolidado final em base/padroes-classificados-consolidado.json

Uso:
    python scripts/classificar_padrao_gemma.py            # roda fila toda
    python scripts/classificar_padrao_gemma.py --slug X   # um so
    python scripts/classificar_padrao_gemma.py --test     # smoke 3 projetos
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
DET_DIR = BASE / "itens-detalhados"
IDX_DIR = BASE / "indices-executivo"
OUT_DIR = BASE / "padroes-classificados"
OUT_DIR.mkdir(parents=True, exist_ok=True)

QUEUE = BASE / "phase18-queue.json"
LOG = BASE / "phase18-classificacao.log.jsonl"
CONSOLIDADO = BASE / "padroes-classificados-consolidado.json"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"
TIMEOUT = 600  # 10 min por chamada

TARGET_ABAS_KEYWORDS = {
    "pisos": ["piso", "rodape", "rodapé"],
    "esquadrias": ["esquadria", "porta", "janela", "vidro", "aluminio"],
    "loucas": ["louca", "louça", "metais", "metal"],
    "fachada": ["fachada", "revestimento extern"],
    "sistemas_especiais": ["especiais", "lazer", "piscina"],
}

# Fallback: per-item description keywords (when aba name doesn't match)
ITEM_DESC_PATTERNS = {
    "pisos": re.compile(
        r"\b(porcelanato|ceramic[ao]|m[aá]rmore|granito|laminado|vin[ií]lico|rodap[eé]|"
        r"contra ?piso|regulariza[cç][aã]o de piso|piso elevado|piso vin[ií]lico|"
        r"carpete|taco|madeira|deck)\b", re.IGNORECASE),
    "esquadrias": re.compile(
        r"\b(porta|janela|vidro|esquadria|alum[ií]nio|brise|guarda[-\s]?corpo|gradil|"
        r"batente|ferragem|fechadura|corrim[aã]o|serralheria|vitro|caixilho|"
        r"temperado|laminado[-\s]*seguran[cç]a|pivot|basculant)\b", re.IGNORECASE),
    "loucas": re.compile(
        r"\b(torneira|vaso|cuba|pia|chuveiro|registr[oa]|v[aá]lvula|sif[aã]o|"
        r"tanque|bid[eê]|bacia|louç|deca|docol|roca|blukit|franke|lavat[oó]rio|"
        r"mictori[oa]|acess[oó]rio de banh)\b", re.IGNORECASE),
    "fachada": re.compile(
        r"\b(fachada|revestimento extern|acm|pastilha|textura|grafiato|"
        r"pele de vidro|curtain[-\s]?wall|cortina de vidro|reboco extern)\b", re.IGNORECASE),
    "sistemas_especiais": re.compile(
        r"\b(piscina|sauna|spa|ofur[oô]|jacuzzi|gerador|automa[cç][aã]o|"
        r"elevador|heliponto|fitness|gourmet|brinquedoteca|sal[aã]o|coworking|pet)\b",
        re.IGNORECASE),
}

SIGNATURE_PATTERNS = {
    "piscina_aquecida": r"\b(piscina[^.]{0,40}aquec|aquec[^.]{0,40}piscina)\b",
    "gerador": r"\bgerador\b|\bgmg\b",
    "automacao": r"\bautoma[cç][aã]o\b|\bdom[oó]tica\b|\bcabeamento estruturado\b",
    "spa_sauna": r"\bspa\b|\bsauna\b|\bofur[oô]\b|\bjacuzzi\b",
    "elevador_panoramico": r"\belevador[^.]{0,20}panor[aâ]mico\b|\bpanor[aâ]mico[^.]{0,20}elevador\b",
    "marmore": r"\bm[aá]rmore\b",
    "granito": r"\bgranito\b",
    "acm": r"\bacm\b|\baluminum composite\b",
    "porcelanato_grande": r"\b(120\s?[x×]\s?120|100\s?[x×]\s?100|90\s?[x×]\s?90|80\s?[x×]\s?80)\b",
    "porcelanato_pequeno": r"\b(45\s?[x×]\s?45|60\s?[x×]\s?60)\b",
    "laminado": r"\blaminado\b",
    "vinilico": r"\bvin[ií]lico\b",
    "docol_deca": r"\b(docol|deca|roca|franke|blukit)\b",
    "fitness_academia": r"\b(academia|fitness)\b",
    "gourmet": r"\b(gourmet)\b",
    "heliponto": r"\bheliponto\b",
    "home_theater": r"\bhome\s?theater\b",
    "adega": r"\badega\b",
}


def _load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _normalize(s: str) -> str:
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s


def _extract_item_fields(it: dict) -> dict:
    desc = str(it.get("descricao", "")).strip()
    pu = it.get("pu") if isinstance(it.get("pu"), (int, float)) else None
    qtd = it.get("qtd") if isinstance(it.get("qtd"), (int, float)) else None
    total = it.get("total") if isinstance(it.get("total"), (int, float)) else None
    un = it.get("unidade") or ""
    return {
        "desc": desc[:150],
        "un": str(un)[:12],
        "qtd": qtd,
        "pu": pu,
        "total": total,
    }


def _coletar_itens_relevantes(slug: str) -> dict:
    """Coleta itens de Pisos/Esquadrias/Louças/Fachada/SE com 2 estratégias.

    1. **Aba-name matching**: se a aba tem nome tipo "PISOS", "ESQUADRIAS" etc,
       todos os itens dela entram na categoria.
    2. **Item-desc matching (fallback)**: se a estratégia 1 deu <5 itens pra
       alguma categoria, varre TODAS as abas e classifica cada item pela
       descrição via regex. Funciona pra xlsx em formato Sienge/EAP/Relatório
       genérico sem aba por macrogrupo.
    """
    det = _load_json(DET_DIR / f"{slug}.json")
    out = {k: [] for k in TARGET_ABAS_KEYWORDS}

    # Strategy 1: aba-name matching
    for aba in det.get("abas", []) or []:
        nome = _normalize(aba.get("nome", ""))
        target = None
        for key, kws in TARGET_ABAS_KEYWORDS.items():
            if any(kw in nome for kw in kws):
                target = key
                break
        if not target:
            continue
        for it in aba.get("itens", []) or []:
            desc = str(it.get("descricao", "")).strip()
            if not desc or len(desc) < 3:
                continue
            out[target].append(_extract_item_fields(it))

    # Strategy 2: per-item desc matching for categories that came up short
    # Priority order: mais específicas primeiro, pisos por último (regex mais
    # genérico que pega "madeira", "laminado" que aparecem em esquadrias)
    PRIORITY_ORDER = ["esquadrias", "loucas", "fachada", "sistemas_especiais", "pisos"]
    underfilled = [k for k in PRIORITY_ORDER if len(out[k]) < 5]
    if underfilled:
        already_seen = set()
        for cat in out:
            for it in out[cat]:
                already_seen.add(it["desc"][:80])
        for aba in det.get("abas", []) or []:
            for it in aba.get("itens", []) or []:
                desc = str(it.get("descricao", "")).strip()
                if not desc or len(desc) < 3:
                    continue
                key = desc[:80]
                if key in already_seen:
                    continue
                for cat in underfilled:
                    pat = ITEM_DESC_PATTERNS.get(cat)
                    if pat and pat.search(desc):
                        out[cat].append(_extract_item_fields(it))
                        already_seen.add(key)
                        break

    return out


def _detectar_flags(itens_relevantes: dict) -> dict:
    all_desc = []
    for key in itens_relevantes:
        for it in itens_relevantes[key]:
            all_desc.append(_normalize(it["desc"]))
    text = " | ".join(all_desc)
    flags = {}
    for name, pat in SIGNATURE_PATTERNS.items():
        flags[name] = bool(re.search(pat, text, re.IGNORECASE))
    return flags


def _top_itens_por_total(itens: list, n: int = 15) -> list:
    def key(it):
        t = it.get("total") or 0
        if not t and it.get("pu") and it.get("qtd"):
            t = it["pu"] * it["qtd"]
        return -(t or 0)
    return sorted(itens, key=key)[:n]


def coletar_sinais(slug: str) -> dict:
    det = _load_json(DET_DIR / f"{slug}.json")
    idx = _load_json(IDX_DIR / f"{slug}.json")

    ac = idx.get("ac") or 0
    ur = idx.get("ur") or 0
    total = idx.get("total") or 0
    rsm2 = (total / ac) if ac else 0
    m2_por_ur = (ac / ur) if ur else 0
    rs_por_ur = (total / ur) if ur else 0

    itens_rel = _coletar_itens_relevantes(slug)
    flags = _detectar_flags(itens_rel)

    # Top itens por macrogrupo
    top = {k: _top_itens_por_total(itens_rel[k], 15) for k in itens_rel}

    # Disciplinas R$/m² do indices-executivo
    disciplinas = {}
    for k, v in (idx.get("disciplinas") or {}).items():
        if isinstance(v, dict) and v.get("rsm2"):
            disciplinas[k] = round(v["rsm2"], 2)

    return {
        "slug": slug,
        "projeto_meta": {
            "ac": ac,
            "ur": ur,
            "total": total,
            "rsm2": round(rsm2, 2),
            "m2_por_ur": round(m2_por_ur, 2),
            "rs_por_ur": round(rs_por_ur, 2),
        },
        "disciplinas_rsm2": disciplinas,
        "flags_assinatura": flags,
        "top_itens_finish": top,
        "n_itens_total": det.get("total_itens", 0),
        "qualitative_tipologia": ((idx.get("qualitative") or {}).get("pdf_metadata") or {}).get("tipologia"),
    }


def build_prompt(sinais: dict) -> str:
    pm = sinais["projeto_meta"]
    flags_on = [k for k, v in sinais["flags_assinatura"].items() if v]
    flags_off = [k for k, v in sinais["flags_assinatura"].items() if not v]

    # Serializar top itens legível
    top_blocks = []
    for mg_key, itens in sinais["top_itens_finish"].items():
        if not itens:
            continue
        lines = []
        for it in itens[:12]:
            pu = f"R$ {it['pu']:,.2f}" if it.get("pu") else "-"
            qtd = f"{it['qtd']:,.2f}" if it.get("qtd") else "-"
            total = f"R$ {it['total']:,.0f}" if it.get("total") else "-"
            lines.append(f"  - {it['desc'][:100]} [{it['un']}, qtd={qtd}, pu={pu}, total={total}]")
        top_blocks.append(f"### {mg_key.upper()}\n" + "\n".join(lines))
    itens_txt = "\n\n".join(top_blocks) if top_blocks else "(sem itens relevantes capturados)"

    disc_txt = "\n".join(f"  - {k}: R$ {v:,.2f}/m²" for k, v in sorted(sinais["disciplinas_rsm2"].items())) or "(sem dados)"

    tipologia = sinais.get("qualitative_tipologia") or "(não informada)"

    return f"""Você é um especialista em orçamentos de construção civil. Classifique o padrão de acabamento do projeto abaixo em uma das 5 classes: **economico, medio, medio-alto, alto, luxo**.

## Rubric canônica (use como referência)

| Classe | R$/m² | m²/UR | Pisos | Esquadrias | Lazer/Especiais | Fachada |
|---|---|---|---|---|---|---|
| **economico** | < 2.800 | < 50 | cerâmico 45×45, laminado | alumínio simples, MDF | básico ou ausente | textura, pintura |
| **medio** | 2.800–3.400 | 50–70 | porcelanato 60×60 | alumínio linha intermediária | piscina adulto+infantil, salão, playground | pastilha, textura |
| **medio-alto** | 3.400–4.000 | 70–100 | porcelanato 80×80 | esquadria reforçada, acústica | + automação básica, fitness | pastilha + detalhes |
| **alto** | 4.000–5.000 | 100–150 | porcelanato 120×120, granito | alumínio alto-standard, vidro duplo | + spa/sauna, gourmet completo, gerador | ACM, granito |
| **luxo** | > 5.000 | > 150 | mármore, madeira nobre, granito | esquadria com brise automatizado, elevador panorâmico | + piscina aquecida borda infinita, heliponto, adega | mármore, granito, ACM premium |

**Importante:** a rubric é guia, não trava. Dois sinais fortes de classe alta compensam R$/m² baixo. Confie mais em material/marca/dimensão do que em R$/m² isolado — o R$/m² pode estar subestimado por extração parcial.

## Dados do projeto: {sinais['slug']}

**Métricas numéricas:**
- AC: {pm['ac']:,.0f} m²
- UR (unidades): {pm['ur']}
- Total: R$ {pm['total']:,.0f}
- R$/m²: R$ {pm['rsm2']:,.2f}
- m²/UR: {pm['m2_por_ur']:,.1f}
- R$/UR: R$ {pm['rs_por_ur']:,.0f}
- Tipologia declarada: {tipologia}

**R$/m² por disciplina:**
{disc_txt}

**Flags de assinatura detectados automaticamente:**
- PRESENTES: {', '.join(flags_on) if flags_on else '(nenhum)'}
- AUSENTES: {', '.join(flags_off[:8])}

**Top itens de acabamento (Pisos, Esquadrias, Louças, Fachada, Sistemas Especiais):**

{itens_txt}

## Sua tarefa

Analise os itens acima com atenção a:
1. **Material e marca** (porcelanato vs cerâmico, mármore/granito vs pintura, Docol/Deca/Roca vs Tigre/Astra)
2. **Dimensão** (120×120 >> 60×60 >> 45×45)
3. **Especificidade** (brise automatizado, vidro duplo, acústico, ACM, automação)
4. **Lazer** (piscina aquecida, spa, sauna, ofurô, gourmet, fitness, adega, heliponto)
5. **Coerência numérica** (se R$/m² bate com a classe que os materiais sugerem)

Responda **APENAS** com JSON válido nesse schema (sem comentários, sem markdown, sem texto antes/depois):

```json
{{
  "padrao": "economico|medio|medio-alto|alto|luxo",
  "confianca": "alta|media|baixa",
  "sinais_detectados": ["sinal 1 textual", "sinal 2 textual", "..."],
  "sinais_ausentes_relevantes": ["spa", "gerador", "..."],
  "justificativa": "2-3 frases explicando a escolha citando itens específicos",
  "coerencia_rsm2": "sim|nao|parcial — explicação curta se não for sim"
}}
```"""


def call_gemma(prompt: str) -> dict:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": 2000,
            "num_ctx": 8192,
        },
    }, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def parse_response(raw: str) -> dict:
    # Extract JSON between curly braces, tolerant to code fences
    raw = raw.strip()
    # Strip ```json ... ``` fences
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```\s*$", "", raw, flags=re.MULTILINE)
    # Find first { and matching last }
    start = raw.find("{")
    end = raw.rfind("}")
    if start < 0 or end < 0 or end <= start:
        raise ValueError(f"No JSON object found in response: {raw[:200]}")
    j = raw[start:end + 1]
    # Try plain parse, then cleanup common issues
    try:
        return json.loads(j)
    except json.JSONDecodeError:
        j2 = re.sub(r",\s*}", "}", j)
        j2 = re.sub(r",\s*]", "]", j2)
        return json.loads(j2)


def log_event(e: dict) -> None:
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue() -> dict:
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    slugs = sorted(p.stem for p in IDX_DIR.glob("*.json"))
    q = {"created": datetime.now().isoformat(timespec="seconds"),
         "items": {s: {"status": "pending"} for s in slugs}}
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    return q


def save_queue(q: dict) -> None:
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def processar_projeto(slug: str, retry: int = 1) -> dict:
    t0 = time.time()
    sinais = coletar_sinais(slug)
    prompt = build_prompt(sinais)

    last_err = None
    for attempt in range(retry + 1):
        try:
            r = call_gemma(prompt)
            raw = r.get("response", "")
            parsed = parse_response(raw)
            result = {
                "projeto": slug,
                "ts": datetime.now().isoformat(timespec="seconds"),
                "duration_s": round(time.time() - t0, 1),
                "model": MODEL,
                "attempt": attempt + 1,
                "classificacao": parsed,
                "sinais_input": {
                    "projeto_meta": sinais["projeto_meta"],
                    "flags_assinatura": sinais["flags_assinatura"],
                    "disciplinas_rsm2": sinais["disciplinas_rsm2"],
                    "n_itens_top": sum(len(v) for v in sinais["top_itens_finish"].values()),
                },
                "raw_response_preview": raw[:500],
            }
            out = OUT_DIR / f"{slug}.json"
            out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
            return result
        except Exception as e:
            last_err = e
            time.sleep(2)
    raise RuntimeError(f"{slug}: classificacao falhou apos {retry+1} tentativas: {last_err}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default=None, help="processar apenas este projeto")
    ap.add_argument("--test", action="store_true", help="smoke test em 3 projetos")
    ap.add_argument("--retry-failed", action="store_true", help="reprocessar apenas os failed")
    args = ap.parse_args()

    if args.slug:
        print(f"=== {args.slug} ===")
        r = processar_projeto(args.slug)
        c = r["classificacao"]
        print(f"  padrao: {c.get('padrao')} (conf={c.get('confianca')})  {r['duration_s']}s")
        print(f"  just: {c.get('justificativa','')[:150]}")
        return

    slugs_test = ["arthen-arboris", "placon-arminio-tavares", "thozen-electra"]
    if args.test:
        q = init_queue()
        for s in slugs_test:
            print(f"\n=== {s} ===")
            try:
                r = processar_projeto(s)
                c = r["classificacao"]
                print(f"  padrao: {c.get('padrao')} (conf={c.get('confianca')})  {r['duration_s']}s")
                print(f"  sinais: {c.get('sinais_detectados', [])[:5]}")
                print(f"  just: {c.get('justificativa','')[:200]}")
                q["items"][s] = {"status": "done", "padrao": c.get("padrao"),
                                 "duration_s": r["duration_s"]}
                log_event({"projeto": s, "status": "done", "padrao": c.get("padrao"),
                           "duration_s": r["duration_s"]})
            except Exception as e:
                print(f"  FAIL: {e}")
                q["items"][s] = {"status": "failed", "error": str(e)[:200]}
                log_event({"projeto": s, "status": "failed", "error": str(e)[:200]})
            save_queue(q)
        return

    q = init_queue()
    pending = [s for s, v in q["items"].items()
               if v["status"] == "pending" or (args.retry_failed and v["status"] == "failed")]
    print(f"Pendentes: {len(pending)}/{len(q['items'])}")
    t_start = time.time()
    for i, slug in enumerate(pending, start=1):
        elapsed = time.time() - t_start
        eta = (elapsed / i) * (len(pending) - i) if i > 0 else 0
        print(f"\n[{i}/{len(pending)}] {slug} (elapsed {elapsed/60:.1f}min, eta {eta/60:.1f}min)")
        q["items"][slug] = {"status": "in_progress"}
        save_queue(q)
        try:
            r = processar_projeto(slug)
            c = r["classificacao"]
            q["items"][slug] = {"status": "done", "padrao": c.get("padrao"),
                                "confianca": c.get("confianca"),
                                "duration_s": r["duration_s"]}
            log_event({"projeto": slug, "status": "done", "padrao": c.get("padrao"),
                       "confianca": c.get("confianca"), "duration_s": r["duration_s"]})
            print(f"  -> {c.get('padrao')} ({c.get('confianca')}) em {r['duration_s']}s")
        except Exception as e:
            err = str(e)[:200]
            q["items"][slug] = {"status": "failed", "error": err}
            log_event({"projeto": slug, "status": "failed", "error": err})
            print(f"  FAIL: {err}")
        save_queue(q)

    # Consolidar
    done = {s: v for s, v in q["items"].items() if v["status"] == "done"}
    failed = {s: v for s, v in q["items"].items() if v["status"] == "failed"}
    print(f"\n{'='*60}")
    print(f"Total done:   {len(done)}/{len(q['items'])}")
    print(f"Total failed: {len(failed)}")
    if done:
        from collections import Counter
        dist = Counter(v.get("padrao") for v in done.values())
        print(f"\nDistribuicao:")
        for k, v in dist.most_common():
            print(f"  {k:<12} {v}")


if __name__ == "__main__":
    main()
