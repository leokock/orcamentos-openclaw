#!/usr/bin/env python3
"""Fase 13 — Revisa pendências via Qwen2.5:14b.

Pendências (após Fase 12 ground truth):
A) 49 projetos sem data_base → tenta extrair de indices-executivo (18 direto)
   + Qwen pra inferir nos 31 restantes a partir de observações/cliente/etc.
B) 7 projetos com tipologia_confianca="media" → re-classifica com contexto rico
C) 6 projetos com padrão problemático (desconhecido/null/insuficiente/medio_alto)
   → Qwen determina padrão canônico a partir de cliente/tipologia/indicadores

Output:
- Atualiza base/projetos-enriquecidos/{slug}.json
- Atualiza base/projetos-enriquecidos.json
- Gera base/pendencias-qwen-relatorio.json
- Log em base/pendencias-qwen.log.jsonl
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
ENR_FILE = BASE / "projetos-enriquecidos.json"
IND_DIR = BASE / "indices-executivo"
GT_DIR = BASE / "entregas-ground-truth"
LOG = BASE / "pendencias-qwen.log.jsonl"
REL = BASE / "pendencias-qwen-relatorio.json"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:14b"

MESES_PT = {
    "jan": 1, "janeiro": 1, "fev": 2, "fevereiro": 2, "mar": 3, "marco": 3, "março": 3,
    "abr": 4, "abril": 4, "mai": 5, "maio": 5, "jun": 6, "junho": 6,
    "jul": 7, "julho": 7, "ago": 8, "agosto": 8, "set": 9, "setembro": 9,
    "out": 10, "outubro": 10, "nov": 11, "novembro": 11, "dez": 12, "dezembro": 12,
}

PADROES_CANON = ["economico", "medio", "medio-alto", "alto", "luxo"]


# ============================================================
# Normalização de data_base
# ============================================================

def normalizar_data_base(s: str) -> str | None:
    """Converte string de data em ISO YYYY-MM. Aceita:
    - '2022-01', '2022-01-15'
    - '15.10.2021', '08/07/2024', '22/05/2023'
    - 'jul/2025', 'AGOSTO/2022', 'ABRIL/23'
    - 'mai/2022', 'nov/2024'
    Retorna None se não conseguir parsear.
    """
    if not s or not isinstance(s, str):
        return None
    s = s.strip().lower()

    # YYYY-MM ou YYYY-MM-DD
    m = re.match(r"^(\d{4})-(\d{1,2})", s)
    if m:
        ano, mes = int(m.group(1)), int(m.group(2))
        if 2015 <= ano <= 2030 and 1 <= mes <= 12:
            return f"{ano:04d}-{mes:02d}"

    # DD.MM.YYYY ou DD/MM/YYYY
    m = re.match(r"^(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})", s)
    if m:
        dia, mes, ano = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if ano < 100:
            ano += 2000
        if 2015 <= ano <= 2030 and 1 <= mes <= 12:
            return f"{ano:04d}-{mes:02d}"

    # Mês/ano texto: jul/2025, JUNHO/2022, ABRIL/23
    m = re.match(r"^([a-zç]+)\s*[./-]\s*(\d{2,4})", s)
    if m:
        mes_txt = m.group(1)[:5]
        ano = int(m.group(2))
        if ano < 100:
            ano += 2000
        for k, v in MESES_PT.items():
            if mes_txt.startswith(k[:5]):
                if 2015 <= ano <= 2030:
                    return f"{ano:04d}-{v:02d}"
                break

    return None


# ============================================================
# Qwen wrapper
# ============================================================

def call_qwen(prompt: str, timeout: int = 300, json_format: bool = True) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": 600,
            "num_ctx": 4096,
        },
    }
    if json_format:
        payload["format"] = "json"
    r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
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


def log(e: dict):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


# ============================================================
# Contexto rico pra Qwen
# ============================================================

def build_contexto_full(enr: dict, ind: dict | None, gt: dict | None, include_dates: bool = True) -> str:
    """Monta contexto completo pra Qwen analisar.

    include_dates=False remove datas de extração/processamento (usado para inferência de data_base).
    """
    p = []
    p.append(f"Slug: {enr['slug']}")
    p.append(f"Cliente inferido: {enr.get('cliente_inferido', '?')}")
    if enr.get("cidade"):
        p.append(f"Localização: {enr.get('cidade')}/{enr.get('uf', '?')} (CUB: {enr.get('cub_regiao', '?')})")
    if enr.get("padrao") and enr.get("padrao") not in ("null", "desconhecido", "insuficiente"):
        p.append(f"Padrão registrado: {enr.get('padrao')}")
    if enr.get("tipologia_canonica"):
        p.append(f"Tipologia: {enr.get('tipologia_canonica')} (confiança: {enr.get('tipologia_confianca', '?')})")
    if enr.get("ac_m2"):
        p.append(f"AC: {enr['ac_m2']:,.0f} m²")
    if enr.get("ur"):
        p.append(f"UR: {enr['ur']}")
    if enr.get("rsm2"):
        p.append(f"R$/m²: R$ {enr['rsm2']:,.2f}")
    if enr.get("total_rs"):
        p.append(f"Total: R$ {enr['total_rs']:,.0f}")
    if enr.get("n_pavimentos_total"):
        p.append(f"Pavimentos total: {enr['n_pavimentos_total']}")
    if enr.get("n_torres"):
        p.append(f"Torres: {enr['n_torres']}")
    if enr.get("sistema_estrutural"):
        p.append(f"Sistema estrutural: {enr['sistema_estrutural']}")
    if enr.get("concreto_m3_m2_ac"):
        p.append(f"Concreto: {enr['concreto_m3_m2_ac']:.3f} m³/m²")
    if enr.get("observacoes_gemma"):
        p.append(f"Observações memorial: {str(enr['observacoes_gemma'])[:400]}")

    # indices-executivo: observações do orçamentista
    if ind:
        qual = ind.get("qualitative") or {}
        obs = qual.get("observacoes_orcamentista") or []
        if obs and isinstance(obs, list):
            textos = []
            for o in obs[:10]:
                if isinstance(o, dict):
                    textos.append(o.get("observacao", ""))
            textos = [t for t in textos if t]
            if textos:
                p.append(f"Observações orçamentista: {' | '.join(textos)[:500]}")
        padroes = qual.get("padroes_identificados") or []
        if padroes:
            p.append(f"Padrões identificados no orçamento: {str(padroes)[:300]}")

    # ground truth
    if gt and "dados" in gt:
        dd = gt["dados"]
        if dd.get("empreendimento"):
            p.append(f"Empreendimento (capa entrega): {dd['empreendimento']}")
        if dd.get("cliente"):
            p.append(f"Cliente (capa entrega): {dd['cliente']}")
        if gt.get("extracao_em") and include_dates:
            p.append(f"Entrega processada em: {gt['extracao_em']}")

    return "\n".join(p)


# ============================================================
# (A) data_base
# ============================================================

def extrair_data_base_indices(slug: str) -> tuple[str | None, str | None]:
    """Tenta extrair data_base de indices-executivo. Retorna (iso, raw)."""
    f = IND_DIR / f"{slug}.json"
    if not f.exists():
        return None, None
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None, None
    raw = (d.get("data_base") or d.get("cub_data_base") or
           (d.get("qualitative") or {}).get("pdf_metadata", {}).get("data_base"))
    if not raw:
        return None, None
    iso = normalizar_data_base(str(raw))
    return iso, str(raw)


PROMPT_DATA_BASE = """Você analisa projetos de construção civil brasileiros para determinar a data-base do CUB do orçamento.

A data-base é o MÊS/ANO DO CUB DE REFERÊNCIA usado no orçamento. Não é a data de hoje nem a data de extração/processamento do projeto pela IA.

REGRAS ESTRITAS:
1. SÓ retorne uma data se houver EVIDÊNCIA TEXTUAL no memorial ou observações (ex: "CUB jan/2024", "referência SINDUSCON fev/2023", "data base: 03/2022").
2. NÃO infira a partir da data em que o documento foi processado pela IA.
3. NÃO assuma que "data-base = data atual".
4. NÃO chute com base no nome do projeto, no cliente ou na região.
5. Se não houver CITAÇÃO EXPLÍCITA de mês/ano no contexto, retorne null.

CONTEXTO:
{contexto}

Responda APENAS JSON:
{{"data_base_iso": "YYYY-MM ou null", "confianca": "alta|media|baixa", "motivo": "cite a passagem textual que justifica (ou explique por que não há evidência)"}}

Se NÃO houver pistas textuais explícitas, responda:
{{"data_base_iso": null, "confianca": "baixa", "motivo": "sem citação explícita de mês/ano de CUB no contexto"}}"""


def inferir_data_base_qwen(enr: dict, ind: dict | None, gt: dict | None) -> dict:
    contexto = build_contexto_full(enr, ind, gt, include_dates=False)
    prompt = PROMPT_DATA_BASE.format(contexto=contexto)
    t0 = time.time()
    try:
        raw = call_qwen(prompt)
        resp = parse_json(raw)
    except Exception as e:
        return {"erro": str(e)[:200], "duration_s": round(time.time() - t0, 1)}
    resp["duration_s"] = round(time.time() - t0, 1)
    # Valida formato data
    d = resp.get("data_base_iso")
    if d:
        d_norm = normalizar_data_base(d)
        resp["data_base_iso"] = d_norm
    return resp


# ============================================================
# (B) tipologia
# ============================================================

TIPOLOGIAS = [
    "residencial_vertical_economico",
    "residencial_vertical_medio",
    "residencial_vertical_medio_alto",
    "residencial_vertical_alto",
    "residencial_vertical_luxo",
    "residencial_misto",
    "comercial_vertical",
    "lajes_corporativas",
    "casa_condominio",
    "industrial",
    "outros",
]

PROMPT_TIPOLOGIA = """Você é especialista em classificação de empreendimentos imobiliários brasileiros.

Com base no contexto abaixo, classifique a TIPOLOGIA canônica do projeto com alta confiança e justificativa detalhada.

Categorias (escolha UMA):
- residencial_vertical_economico  (HIS, MCMV, R$/m² < 2500, padrão econômico)
- residencial_vertical_medio      (R$/m² 2500-3500, padrão médio)
- residencial_vertical_medio_alto (R$/m² 3500-4500, padrão médio-alto)
- residencial_vertical_alto       (R$/m² 4500-5500, padrão alto)
- residencial_vertical_luxo       (R$/m² > 5500 + especificação premium + localização nobre)
- residencial_misto               (comércio/salas no térreo + residencial nos tipos)
- comercial_vertical              (só salas comerciais)
- lajes_corporativas              (edifício corporativo com lajes grandes)
- casa_condominio                 (casas de alto/luxo em condomínio fechado)
- industrial                      (galpão, fábrica)

CONTEXTO:
{contexto}

Análise crítica: considere AC, UR, R$/m², cidade, padrão construtivo, observações.
A classificação anterior teve confiança MÉDIA — você precisa melhorar.

Responda APENAS JSON:
{{"tipologia_canonica": "residencial_vertical_alto", "confianca": "alta|media|baixa", "motivo": "justificativa com 2-3 evidências"}}"""


def classificar_tipologia_qwen(enr: dict, ind: dict | None, gt: dict | None) -> dict:
    contexto = build_contexto_full(enr, ind, gt)
    prompt = PROMPT_TIPOLOGIA.format(contexto=contexto)
    t0 = time.time()
    try:
        raw = call_qwen(prompt)
        resp = parse_json(raw)
    except Exception as e:
        return {"erro": str(e)[:200], "duration_s": round(time.time() - t0, 1)}
    resp["duration_s"] = round(time.time() - t0, 1)
    tip = resp.get("tipologia_canonica", "")
    # Normaliza typo comum: "residential_*" -> "residencial_*"
    if tip.startswith("residential_"):
        tip = tip.replace("residential_", "residencial_", 1)
        resp["tipologia_canonica"] = tip
    if tip not in TIPOLOGIAS:
        resp["erro"] = f"tipologia invalida: {tip}"
    return resp


# ============================================================
# (C) padrão
# ============================================================

PROMPT_PADRAO = """Você é especialista em padrão construtivo de empreendimentos imobiliários brasileiros.

Com base no contexto abaixo, determine o PADRÃO CONSTRUTIVO canônico.

Categorias válidas:
- economico   (HIS, MCMV, R$/m² < 2500)
- medio       (R$/m² 2500-3500)
- medio-alto  (R$/m² 3500-4500)
- alto        (R$/m² 4500-5500, spec superior)
- luxo        (R$/m² > 5500, premium/vista/localização nobre)

O padrão anterior estava registrado como "{padrao_atual}" — problemático ou ausente.
Você deve determinar o padrão correto usando TODAS as evidências disponíveis:
- R$/m² (se existe)
- Cliente habitual (alguns clientes têm padrão recorrente)
- Localização (região valoriza acima/abaixo)
- AC, UR, sistemas especiais (pele de vidro, piscina, climatização central)
- Tipologia (luxo costuma vir com AC menor e R$/m² maior)
- Observações

CONTEXTO:
{contexto}

Responda APENAS JSON:
{{"padrao_canonico": "alto", "confianca": "alta|media|baixa", "motivo": "justificativa com 2-3 evidências"}}"""


def determinar_padrao_qwen(enr: dict, ind: dict | None, gt: dict | None) -> dict:
    contexto = build_contexto_full(enr, ind, gt)
    prompt = PROMPT_PADRAO.format(contexto=contexto, padrao_atual=enr.get("padrao", "?"))
    t0 = time.time()
    try:
        raw = call_qwen(prompt)
        resp = parse_json(raw)
    except Exception as e:
        return {"erro": str(e)[:200], "duration_s": round(time.time() - t0, 1)}
    resp["duration_s"] = round(time.time() - t0, 1)
    pad = resp.get("padrao_canonico", "")
    # normaliza medio_alto -> medio-alto
    if pad == "medio_alto":
        pad = "medio-alto"
        resp["padrao_canonico"] = pad
    if pad not in PADROES_CANON:
        resp["erro"] = f"padrao invalido: {pad}"
    return resp


# ============================================================
# Orquestração
# ============================================================

def carregar_enr(slug: str) -> dict | None:
    f = ENR_DIR / f"{slug}.json"
    if not f.exists():
        return None
    return json.loads(f.read_text(encoding="utf-8"))


def carregar_ind(slug: str) -> dict | None:
    f = IND_DIR / f"{slug}.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None


def carregar_gt(slug: str) -> dict | None:
    f = GT_DIR / f"{slug}.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None


def salvar_enr(slug: str, enr: dict):
    f = ENR_DIR / f"{slug}.json"
    f.write_text(json.dumps(enr, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-data-base", action="store_true", help="Pula passo A")
    ap.add_argument("--skip-tipologia", action="store_true", help="Pula passo B")
    ap.add_argument("--skip-padrao", action="store_true", help="Pula passo C")
    ap.add_argument("--only", default=None, help="Só processa 1 slug")
    args = ap.parse_args()

    enr_cons = json.loads(ENR_FILE.read_text(encoding="utf-8"))
    enr_map = {p["slug"]: p for p in enr_cons["projetos"]}

    relatorio = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "modelo": MODEL,
        "data_base_aplicado_indices": [],
        "data_base_aplicado_qwen": [],
        "data_base_sem_resposta": [],
        "tipologia_reclassificada": [],
        "padrao_determinado": [],
    }

    # ===== PASSO A: data_base =====
    if not args.skip_data_base:
        sem_db = [p for p in enr_cons["projetos"] if not p.get("data_base")]
        if args.only:
            sem_db = [p for p in sem_db if p["slug"] == args.only]
        print(f"\n=== PASSO A: {len(sem_db)} projetos sem data_base ===", flush=True)

        # A.1: extração direta de indices-executivo
        aplicados_ind = 0
        para_qwen = []
        for p in sem_db:
            slug = p["slug"]
            iso, raw = extrair_data_base_indices(slug)
            if iso:
                enr = carregar_enr(slug) or {}
                enr["data_base"] = iso
                enr["data_base_fonte"] = "indices_executivo_pdf_metadata"
                enr["data_base_raw"] = raw
                salvar_enr(slug, enr)
                p["data_base"] = iso
                p["data_base_fonte"] = "indices_executivo_pdf_metadata"
                aplicados_ind += 1
                relatorio["data_base_aplicado_indices"].append({
                    "slug": slug, "data_base": iso, "raw": raw,
                })
                print(f"  [IND] {slug:<45} {raw!r:<20} → {iso}", flush=True)
            else:
                para_qwen.append(p)

        print(f"  {aplicados_ind} aplicados direto dos indices-executivo", flush=True)

        # A.2: Qwen pra restantes
        print(f"\n  {len(para_qwen)} restantes → Qwen ({len(para_qwen)*30}s estimados)", flush=True)
        for i, p in enumerate(para_qwen, 1):
            slug = p["slug"]
            enr = carregar_enr(slug)
            if not enr:
                continue
            ind = carregar_ind(slug)
            gt = carregar_gt(slug)
            resp = inferir_data_base_qwen(enr, ind, gt)
            log({"slug": slug, "tipo": "data_base", **resp})
            iso = resp.get("data_base_iso")
            if iso:
                enr["data_base"] = iso
                enr["data_base_fonte"] = "qwen_inferencia"
                enr["data_base_confianca"] = resp.get("confianca")
                enr["data_base_motivo"] = resp.get("motivo")
                salvar_enr(slug, enr)
                p["data_base"] = iso
                p["data_base_fonte"] = "qwen_inferencia"
                relatorio["data_base_aplicado_qwen"].append({
                    "slug": slug, "data_base": iso,
                    "confianca": resp.get("confianca"),
                    "motivo": resp.get("motivo"),
                })
                print(f"  [QWEN {i}/{len(para_qwen)}] {slug:<45} → {iso} ({resp.get('confianca')}) {resp.get('duration_s')}s", flush=True)
            else:
                relatorio["data_base_sem_resposta"].append({
                    "slug": slug,
                    "motivo": resp.get("motivo") or resp.get("erro"),
                })
                print(f"  [QWEN {i}/{len(para_qwen)}] {slug:<45} → SEM RESPOSTA ({resp.get('motivo','')[:80]})", flush=True)

    # ===== PASSO B: tipologia =====
    if not args.skip_tipologia:
        medias = [p for p in enr_cons["projetos"] if p.get("tipologia_confianca") == "media"]
        if args.only:
            medias = [p for p in medias if p["slug"] == args.only]
        print(f"\n=== PASSO B: {len(medias)} projetos com tipologia confiança=média ===", flush=True)
        for i, p in enumerate(medias, 1):
            slug = p["slug"]
            enr = carregar_enr(slug)
            if not enr:
                continue
            ind = carregar_ind(slug)
            gt = carregar_gt(slug)
            resp = classificar_tipologia_qwen(enr, ind, gt)
            log({"slug": slug, "tipo": "tipologia", **resp})
            nova = resp.get("tipologia_canonica")
            conf = resp.get("confianca")
            if nova and resp.get("erro") is None and conf in ("alta", "media"):
                enr["tipologia_canonica"] = nova
                enr["tipologia_confianca"] = conf
                enr["tipologia_motivo"] = resp.get("motivo")
                enr["tipologia_fonte"] = "qwen_revisao"
                salvar_enr(slug, enr)
                relatorio["tipologia_reclassificada"].append({
                    "slug": slug,
                    "antes": p.get("tipologia_canonica"),
                    "depois": nova,
                    "confianca": conf,
                    "motivo": resp.get("motivo"),
                })
                print(f"  [{i}/{len(medias)}] {slug:<45} {p.get('tipologia_canonica', '?'):<35} → {nova:<35} ({conf}) {resp.get('duration_s')}s", flush=True)
            else:
                print(f"  [{i}/{len(medias)}] {slug:<45} → SEM MUDANÇA ({resp.get('erro') or conf})", flush=True)

    # ===== PASSO C: padrão =====
    if not args.skip_padrao:
        problematicos = []
        for p in enr_cons["projetos"]:
            pad = (p.get("padrao") or "").lower()
            if pad in ("", "null", "desconhecido", "insuficiente", "medio_alto"):
                problematicos.append(p)
        if args.only:
            problematicos = [p for p in problematicos if p["slug"] == args.only]
        print(f"\n=== PASSO C: {len(problematicos)} projetos com padrão problemático ===", flush=True)
        for i, p in enumerate(problematicos, 1):
            slug = p["slug"]
            enr = carregar_enr(slug)
            if not enr:
                continue
            ind = carregar_ind(slug)
            gt = carregar_gt(slug)
            resp = determinar_padrao_qwen(enr, ind, gt)
            log({"slug": slug, "tipo": "padrao", **resp})
            novo = resp.get("padrao_canonico")
            conf = resp.get("confianca")
            if novo and resp.get("erro") is None and conf in ("alta", "media"):
                # Preserva padrao_anterior original (não sobrescreve em re-runs)
                if "padrao_anterior" not in enr:
                    enr["padrao_anterior"] = enr.get("padrao")
                enr["padrao_canonico"] = novo
                enr["padrao_confianca"] = conf
                enr["padrao_motivo"] = resp.get("motivo")
                enr["padrao_fonte"] = "qwen_revisao"
                enr["padrao"] = novo
                salvar_enr(slug, enr)
                p["padrao"] = novo
                p["padrao_canonico"] = novo
                p["padrao_fonte"] = "qwen_revisao"
                relatorio["padrao_determinado"].append({
                    "slug": slug,
                    "antes": enr.get("padrao_anterior"),
                    "depois": novo,
                    "confianca": conf,
                    "motivo": resp.get("motivo"),
                })
                print(f"  [{i}/{len(problematicos)}] {slug:<45} {enr.get('padrao_anterior', '?'):<15} → {novo:<12} ({conf}) {resp.get('duration_s')}s", flush=True)
            else:
                print(f"  [{i}/{len(problematicos)}] {slug:<45} → SEM MUDANÇA ({resp.get('erro') or conf})", flush=True)

    # Salva consolidado
    enr_cons["projetos"] = list(enr_map.values())
    enr_cons["pendencias_qwen_aplicado_em"] = datetime.now().isoformat(timespec="seconds")
    ENR_FILE.write_text(json.dumps(enr_cons, indent=2, ensure_ascii=False), encoding="utf-8")

    # Relatório
    REL.write_text(json.dumps(relatorio, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n✅ Concluído", flush=True)
    print(f"   data_base aplicado (indices): {len(relatorio['data_base_aplicado_indices'])}", flush=True)
    print(f"   data_base aplicado (qwen):    {len(relatorio['data_base_aplicado_qwen'])}", flush=True)
    print(f"   data_base sem resposta:        {len(relatorio['data_base_sem_resposta'])}", flush=True)
    print(f"   tipologia reclassificada:      {len(relatorio['tipologia_reclassificada'])}", flush=True)
    print(f"   padrão determinado:            {len(relatorio['padrao_determinado'])}", flush=True)
    print(f"   Relatório: {REL}", flush=True)


if __name__ == "__main__":
    main()
