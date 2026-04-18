#!/usr/bin/env python3
"""Fase 3 — Classifica tipologia canonica de cada projeto via Gemma.

Input:   base/projetos-enriquecidos/{slug}.json (ja tem padrao+cidade+AC+UR)
Output:  base/projetos-enriquecidos/{slug}.json ENRIQUECIDO com tipologia_canonica

Usa contexto rico (padrao, cidade, AC, UR, rsm2, observacoes_gemma) pra Gemma
classificar entre 10 categorias canonicas.

Categorias:
- residencial_vertical_economico  (HIS, MCMV, R$/m² < 2500)
- residencial_vertical_medio
- residencial_vertical_medio_alto
- residencial_vertical_alto
- residencial_vertical_luxo       (R$/m² > 5500 e AC > 5k)
- residencial_misto               (comercio + residencial)
- comercial_vertical              (salas comerciais)
- lajes_corporativas
- casa_condominio                 (casas de luxo)
- industrial                      (galpao, fabrica)

Uso:
    python scripts/classificar_tipologia.py           # fila toda
    python scripts/classificar_tipologia.py --slug X  # 1 projeto
    python scripts/classificar_tipologia.py --test    # 5 projetos smoke
"""
from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
ENR_DIR = BASE / "projetos-enriquecidos"
QUEUE = BASE / "tipologia-queue.json"
LOG = BASE / "tipologia-extracao.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"


PROMPT_TEMPLATE = """Voce e classificador de tipologia de empreendimento imobiliario brasileiro.

Dado contexto abaixo, classifique em UMA categoria canonica:
- residencial_vertical_economico  (padrao economico, HIS, MCMV)
- residencial_vertical_medio
- residencial_vertical_medio_alto
- residencial_vertical_alto
- residencial_vertical_luxo       (alto+ com especificacao premium, vista, localizacao)
- residencial_misto               (comercio/salas no terreo + residencial nos tipos)
- comercial_vertical              (so salas comerciais)
- lajes_corporativas              (edificio corporativo com lajes grandes)
- casa_condominio                 (casas de alto/luxo em condominio fechado)
- industrial                      (galpao, fabrica)
- outros                          (so se realmente nao couber em nenhuma)

CONTEXTO DO PROJETO:
{contexto}

Retorne APENAS JSON:
{{"tipologia_canonica": "residencial_vertical_alto", "confianca": "alta|media|baixa", "motivo": "curta explicacao (1 frase)"}}"""


def _load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_contexto(enr: dict) -> str:
    """Monta string de contexto pra Gemma classificar."""
    partes = []
    partes.append(f"Slug: {enr['slug']}")
    partes.append(f"Cliente inferido: {enr.get('cliente_inferido', '?')}")
    partes.append(f"Padrao construtivo registrado: {enr.get('padrao', '?')}")
    if enr.get("cidade") and enr.get("uf"):
        partes.append(f"Localizacao: {enr['cidade']}/{enr['uf']} (regiao CUB: {enr.get('cub_regiao', '?')})")
    if enr.get("ac_m2"):
        partes.append(f"Area construida: {enr['ac_m2']:,.0f} m²")
    if enr.get("ur"):
        partes.append(f"Unidades residenciais: {enr['ur']}")
    if enr.get("total_rs"):
        partes.append(f"Total orcamento: R$ {enr['total_rs']:,.0f}")
    if enr.get("rsm2"):
        partes.append(f"R$/m²: R$ {enr['rsm2']:,.2f}")
    if enr.get("n_pavimentos_total"):
        partes.append(f"N pavimentos total: {enr['n_pavimentos_total']}")
    if enr.get("n_torres"):
        partes.append(f"N torres: {enr['n_torres']}")
    if enr.get("sistema_estrutural"):
        partes.append(f"Sistema estrutural: {enr['sistema_estrutural']}")
    if enr.get("tipologia_gemma"):
        partes.append(f"Tipologia inferida anteriormente: {enr['tipologia_gemma']}")
    if enr.get("observacoes_gemma"):
        partes.append(f"Observacoes extraidas do memorial: {enr['observacoes_gemma'][:300]}")
    if enr.get("tem_piscina") is True:
        partes.append("Tem piscina: sim")
    if enr.get("tem_pele_vidro") is True:
        partes.append("Tem pele de vidro: sim")
    if enr.get("tem_subsolo") is True:
        partes.append("Tem subsolo: sim")
    return "\n".join(partes)


def call_gemma(prompt: str, timeout: int = 120) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "top_p": 0.9,
            "num_predict": 400,  # resposta curta
            "num_ctx": 2048,
        },
    }, timeout=timeout)
    r.raise_for_status()
    return r.json().get("response", "").strip()


def parse_json(raw: str) -> dict:
    raw = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
    raw = re.sub(r"\s*```\s*$", "", raw, flags=re.MULTILINE)
    s, e = raw.find("{"), raw.rfind("}")
    if s < 0 or e <= s:
        raise ValueError(f"JSON nao encontrado: {raw[:200]}")
    j = raw[s:e + 1]
    try:
        return json.loads(j)
    except json.JSONDecodeError:
        j = re.sub(r",\s*}", "}", j)
        return json.loads(j)


def processar(slug: str) -> dict:
    t0 = time.time()
    enr_path = ENR_DIR / f"{slug}.json"
    if not enr_path.exists():
        return {"slug": slug, "erro": "enriquecido nao encontrado"}
    enr = _load(enr_path)

    contexto = build_contexto(enr)
    prompt = PROMPT_TEMPLATE.format(contexto=contexto)

    try:
        raw = call_gemma(prompt)
        resp = parse_json(raw)
    except Exception as e:
        return {"slug": slug, "erro": f"gemma: {str(e)[:150]}"}

    enr["tipologia_canonica"] = resp.get("tipologia_canonica")
    enr["tipologia_confianca"] = resp.get("confianca")
    enr["tipologia_motivo"] = resp.get("motivo")
    enr["tipologia_em"] = datetime.now().isoformat(timespec="seconds")

    enr_path.write_text(json.dumps(enr, indent=2, ensure_ascii=False), encoding="utf-8")
    return {
        "slug": slug,
        "tipologia": resp.get("tipologia_canonica"),
        "confianca": resp.get("confianca"),
        "duration_s": round(time.time() - t0, 1),
    }


def log(e: dict):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue() -> dict:
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    slugs = sorted(f.stem for f in ENR_DIR.glob("*.json"))
    q = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "fase": "3-tipologia",
        "items": {s: {"status": "pending"} for s in slugs},
    }
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    return q


def save_queue(q: dict):
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default=None)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    if args.slug:
        r = processar(args.slug)
        print(f"{args.slug}: {json.dumps(r, ensure_ascii=False)}")
        return

    if args.test:
        for s in ["thozen-electra", "amalfi-maiori", "paludo-volo-home",
                  "nova-empreendimentos-evora", "santa-maria-unimed"]:
            r = processar(s)
            print(f"{s}: {json.dumps(r, ensure_ascii=False)}")
        return

    q = init_queue()
    pending = [s for s, v in q["items"].items()
               if v["status"] == "pending" or (args.retry_failed and v["status"] == "failed")]
    print(f"Pendentes: {len(pending)}/{len(q['items'])}", flush=True)
    t_start = time.time()

    for i, slug in enumerate(pending, start=1):
        elapsed = time.time() - t_start
        eta = (elapsed / i) * (len(pending) - i) if i > 0 else 0
        print(f"[{i}/{len(pending)}] {slug} (elapsed {elapsed/60:.1f}min eta {eta/60:.1f}min)", flush=True)
        q["items"][slug] = {"status": "in_progress"}
        save_queue(q)
        try:
            r = processar(slug)
            if "erro" in r:
                q["items"][slug] = {"status": "failed", "error": r["erro"]}
                log({"slug": slug, "status": "failed", "erro": r["erro"]})
                print(f"  FAIL: {r['erro']}", flush=True)
            else:
                q["items"][slug] = {
                    "status": "done",
                    "tipologia": r["tipologia"],
                    "confianca": r["confianca"],
                    "duration_s": r["duration_s"],
                }
                log({"slug": slug, "status": "done", **r})
                print(f"  -> {r['tipologia']} ({r['confianca']}) {r['duration_s']}s", flush=True)
        except Exception as e:
            err = str(e)[:200]
            q["items"][slug] = {"status": "failed", "error": err}
            log({"slug": slug, "status": "failed", "erro": err})
            print(f"  CRASH: {err}", flush=True)
        save_queue(q)

    done = sum(1 for v in q["items"].values() if v["status"] == "done")
    failed = sum(1 for v in q["items"].values() if v["status"] == "failed")
    print(f"\nDone: {done}/{len(q['items'])} | Failed: {failed}", flush=True)


if __name__ == "__main__":
    main()
