#!/usr/bin/env python3
"""Phase 20 — Extrai indicadores de produto (quantitativos/m²) via Gemma.

Para cada um dos 126 projetos, envia itens de orçamento ao Gemma local
para classificação semântica em ~30 categorias de indicador, extrai
quantidades físicas e normaliza por AC (m²) ou UR.

Pipeline retomável:
- Fila em base/phase20-queue.json (status por projeto)
- Log append em base/phase20-indicadores.log.jsonl
- Output por projeto em base/indicadores-produto/{slug}.json

Uso:
    python scripts/extrair_indicadores_produto.py            # roda fila toda
    python scripts/extrair_indicadores_produto.py --slug X   # um só
    python scripts/extrair_indicadores_produto.py --test     # smoke 3 projetos
    python scripts/extrair_indicadores_produto.py --retry-failed  # reprocessar falhas
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
PAD_FILE = BASE / "padroes-classificados-consolidado.json"
OUT_DIR = BASE / "indicadores-produto"
OUT_DIR.mkdir(parents=True, exist_ok=True)

QUEUE = BASE / "phase20-queue.json"
LOG = BASE / "phase20-indicadores.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"
TIMEOUT = 600

BATCH_SIZE = 150

# Pré-filtro: descartar antes de mandar pro Gemma
SKIP_KEYWORDS = [
    "bdi", "administra", "admin ", "admin.", "encargo",
    "seguro", "taxa", "imposto", "iss ", "inss", "pis ",
    "cofins", "csll", "irrf", "custo indireto", "despesa indireta",
    "ferramenta", "epi ", "equipamento de prote", "placa de obra",
    "canteiro de obra", "barraca", "container",
    "mao de obra", "mao-de-obra", "mão de obra", "mão-de-obra",
    "hora tecnica", "hora técnica", "honorario", "consultoria",
    "projeto executivo", "projeto legal", "as built", "as-built",
    "alvara", "alvará", "licenca", "licença", "cnd ",
    "despesas gerais", "mobiliz", "desmobiliz",
    "topografia", "sondagem", "estudo ", "ensaio",
    "limpeza final", "limpeza de obra", "entrega de chaves",
    "total ", "subtotal", "resumo", "composicao auxiliar",
    "composição auxiliar",
]

# Keywords positivas: se bater, passa direto (pode ser indicador)
KEEP_KEYWORDS = [
    "concreto", "aco ", "aço", "ca-50", "ca-60", "ca50", "ca60",
    "forma", "escoramento",
    "ponto", "tomada", "luminaria", "luminária", "eletroduto", "quadro",
    "agua", "água", "esgoto", "tubul", "registro", "ralo", "sifona",
    "alvenaria", "bloco", "tijolo",
    "chapisco", "reboco", "contrapiso", "porcelanato", "ceramica", "cerâmica",
    "fachada", "revestimento",
    "pintura", "tinta", "massa ",
    "porta", "janela", "vidro", "guarda-corpo", "guarda corpo", "corrimao", "corrimão",
    "manta", "impermeab", "cristaliz",
    "bacia", "sanitari", "sanitári", "lavat", "cuba", "chuveiro", "ducha",
    "forro", "gesso", "drywall",
    "elevador", "hidrante", "sprinkler",
    "cobertura", "telha", "cumeeira",
]

INDICADORES = [
    ("EST_01", "concreto_m3_por_m2_ac", "m³/m² AC", "ac"),
    ("EST_02", "aco_kg_por_m2_ac", "kg/m² AC", "ac"),
    ("EST_03", "forma_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("EST_04", "escoramento_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("ELE_01", "pontos_iluminacao_por_ur", "un/UR", "ur"),
    ("ELE_02", "tomadas_por_ur", "un/UR", "ur"),
    ("ELE_03", "quadros_eletricos_por_pavimento", "un/pav", "pav"),
    ("ELE_04", "luminarias_por_ur", "un/UR", "ur"),
    ("ELE_05", "eletroduto_m_por_m2_ac", "m/m² AC", "ac"),
    ("ELE_06", "pontos_eletricos_total_por_m2_ac", "un/m² AC", "ac"),
    ("HID_01", "pontos_agua_por_ur", "un/UR", "ur"),
    ("HID_02", "pontos_esgoto_por_ur", "un/UR", "ur"),
    ("HID_03", "tubulacao_total_m_por_m2_ac", "m/m² AC", "ac"),
    ("HID_04", "registros_por_ur", "un/UR", "ur"),
    ("HID_05", "ralos_caixas_sifonadas_por_ur", "un/UR", "ur"),
    ("ALV_01", "alvenaria_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("ALV_02", "blocos_un_por_m2_ac", "un/m² AC", "ac"),
    ("REV_01", "chapisco_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("REV_02", "reboco_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("REV_03", "contrapiso_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("REV_04", "porcelanato_ceramica_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("REV_05", "revestimento_fachada_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("PIN_01", "pintura_interna_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("PIN_02", "pintura_externa_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("ESQ_01", "portas_un_por_ur", "un/UR", "ur"),
    ("ESQ_02", "janelas_un_por_ur", "un/UR", "ur"),
    ("ESQ_03", "vidros_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("ESQ_04", "guarda_corpo_m_por_m2_ac", "m/m² AC", "ac"),
    ("IMP_01", "manta_asfaltica_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("IMP_02", "cristalizacao_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("LOU_01", "bacias_sanitarias_por_ur", "un/UR", "ur"),
    ("LOU_02", "lavatorios_por_ur", "un/UR", "ur"),
    ("LOU_03", "cubas_por_ur", "un/UR", "ur"),
    ("LOU_04", "chuveiros_por_ur", "un/UR", "ur"),
    ("DIV_01", "forro_gesso_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("DIV_02", "elevadores_por_torre", "un/torre", "torre"),
    ("DIV_03", "hidrantes_por_pavimento", "un/pav", "pav"),
    ("DIV_04", "sprinklers_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("DIV_05", "cobertura_m2_por_m2_ac", "m²/m² AC", "ac"),
    ("DIV_06", "drywall_divisoria_m2_por_m2_ac", "m²/m² AC", "ac"),
]

# ─── Classificador local (fallback quando Gemma é lento demais) ─────
# Ordem importa: primeiro match vence. Padrões mais específicos primeiro.
# Cada regra: (lista de padrões que DEVEM estar em desc, lista de padrões que NÃO podem estar, categoria)
LOCAL_RULES = [
    # Estrutural
    (["concreto usinado"], [], "CONCRETO"),
    (["concreto estrutural"], [], "CONCRETO"),
    (["concreto magro"], [], "CONCRETO"),
    (["concreto fck"], [], "CONCRETO"),
    (["graute"], [], "CONCRETO"),
    (["aco ca-50"], [], "ACO"),
    (["aco ca-60"], [], "ACO"),
    (["aco ca 50"], [], "ACO"),
    (["aco ca 60"], [], "ACO"),
    (["ca50"], [], "ACO"),
    (["ca60"], [], "ACO"),
    (["armacao"], ["transferencia"], "ACO"),
    (["tela soldada"], [], "ACO"),
    (["forma de madeira"], [], "FORMA"),
    (["forma metalica"], [], "FORMA"),
    (["escoramento"], [], "ESCORAMENTO"),
    (["aco"], ["inoxidavel", "inox", "galvanizado", "tampa"], "ACO"),
    # Elétrica
    (["ponto de iluminacao"], [], "PONTO_ILUMINACAO"),
    (["ponto de luz"], [], "PONTO_ILUMINACAO"),
    (["luminaria"], [], "LUMINARIA"),
    (["tomada"], [], "TOMADA"),
    (["quadro de distribuicao"], ["caixa", "disjuntor"], "QUADRO_ELETRICO"),
    (["quadro eletrico"], ["caixa", "disjuntor"], "QUADRO_ELETRICO"),
    (["qdg"], ["barramento"], "QUADRO_ELETRICO"),
    (["qgbt"], ["barramento"], "QUADRO_ELETRICO"),
    (["eletroduto"], [], "ELETRODUTO"),
    (["ponto eletrico"], [], "PONTO_ELETRICO_GERAL"),
    # Hidro
    (["ponto de agua"], [], "PONTO_AGUA"),
    (["ponto de esgoto"], [], "PONTO_ESGOTO"),
    (["tubo pvc"], [], "TUBULACAO_HIDRO"),
    (["tubo ppr"], [], "TUBULACAO_HIDRO"),
    (["tubo cpvc"], [], "TUBULACAO_HIDRO"),
    (["tubulacao"], [], "TUBULACAO_HIDRO"),
    (["registro"], ["cartorio", "registro de obra"], "REGISTRO"),
    (["ralo"], [], "RALO_CAIXA_SIFONADA"),
    (["caixa sifonada"], [], "RALO_CAIXA_SIFONADA"),
    # Alvenaria
    (["alvenaria"], [], "ALVENARIA"),
    (["bloco ceramico"], [], "BLOCO"),
    (["bloco de concreto"], [], "BLOCO"),
    (["tijolo"], [], "BLOCO"),
    # Revestimentos
    (["chapisco"], [], "CHAPISCO"),
    (["reboco"], [], "REBOCO"),
    (["contrapiso"], [], "CONTRAPISO"),
    (["regularizacao de piso"], [], "CONTRAPISO"),
    (["porcelanato"], [], "PORCELANATO_CERAMICA"),
    (["revestimento ceramico"], [], "PORCELANATO_CERAMICA"),
    (["piso ceramico"], [], "PORCELANATO_CERAMICA"),
    (["ceramica"], ["antichamas", "bloco"], "PORCELANATO_CERAMICA"),
    (["revestimento fachada"], [], "REVESTIMENTO_FACHADA"),
    (["fachada"], ["revestimento"], "REVESTIMENTO_FACHADA"),
    # Pintura
    (["pintura interna"], [], "PINTURA_INTERNA"),
    (["pintura externa"], [], "PINTURA_EXTERNA"),
    (["massa corrida"], [], "PINTURA_INTERNA"),
    (["textura"], ["textura fachada"], "PINTURA_EXTERNA"),
    (["tinta acrilica interna"], [], "PINTURA_INTERNA"),
    (["tinta acrilica externa"], [], "PINTURA_EXTERNA"),
    (["pintura"], [], "PINTURA_INTERNA"),
    # Esquadrias
    (["porta de madeira"], [], "PORTA"),
    (["porta corta-fogo"], [], "PORTA"),
    (["porta corta fogo"], [], "PORTA"),
    (["janela de aluminio"], [], "JANELA"),
    (["janela"], ["contramarco"], "JANELA"),
    (["porta"], ["contramarco", "portao"], "PORTA"),
    (["vidro temperado"], [], "VIDRO"),
    (["vidro laminado"], [], "VIDRO"),
    (["vidro"], [], "VIDRO"),
    (["guarda-corpo"], [], "GUARDA_CORPO"),
    (["guarda corpo"], [], "GUARDA_CORPO"),
    (["corrimao"], [], "GUARDA_CORPO"),
    # Imper
    (["manta asfaltica"], [], "MANTA_ASFALTICA"),
    (["impermeabilizacao"], ["cristaliz"], "MANTA_ASFALTICA"),
    (["cristalizacao"], [], "CRISTALIZACAO"),
    # Louças/metais
    (["bacia sanitaria"], [], "BACIA_SANITARIA"),
    (["vaso sanitario"], [], "BACIA_SANITARIA"),
    (["lavatorio"], [], "LAVATORIO"),
    (["cuba"], [], "CUBA"),
    (["chuveiro"], [], "CHUVEIRO"),
    (["ducha higienica"], [], "CHUVEIRO"),
    # Diversos
    (["forro de gesso"], [], "FORRO"),
    (["forro drywall"], [], "FORRO"),
    (["forro mineral"], [], "FORRO"),
    (["forro"], [], "FORRO"),
    (["elevador"], ["porta de elevador", "vao de elevador", "vaos de elevador", "area das porta", "fechamento", "contramarco", "piso ", "mureta", "instalacao"], "ELEVADOR"),
    (["caixa de hidrante"], [], "HIDRANTE"),
    (["hidrante"], ["mangueira", "registro", "esguicho", "tubul", "barrilete"], "HIDRANTE"),
    (["quadro de distribuicao"], ["caixa"], "QUADRO_ELETRICO"),
    (["sprinkler"], ["tubul", "conexao"], "SPRINKLER"),
    (["chuveiro automatico"], [], "SPRINKLER"),
    (["telha"], [], "COBERTURA"),
    (["cumeeira"], [], "COBERTURA"),
    (["cobertura"], ["pintura", "forro"], "COBERTURA"),
    (["divisoria drywall"], [], "DRYWALL"),
    (["parede drywall"], [], "DRYWALL"),
    (["drywall"], ["forro"], "DRYWALL"),
]


def classify_local(desc: str, unidade: str) -> str:
    """Classifica item via regras locais keyword-based.

    Retorna categoria ou NAO_CLASSIFICAVEL.
    Ordem das regras importa: mais específica primeiro.
    """
    d = _normalize_text(desc)
    for keywords, excludes, cat in LOCAL_RULES:
        if any(ex in d for ex in excludes):
            continue
        if all(kw in d for kw in keywords):
            return cat
    return "NAO_CLASSIFICAVEL"


GEMMA_CATEGORIES = {
    "CONCRETO": "EST_01",
    "ACO": "EST_02",
    "FORMA": "EST_03",
    "ESCORAMENTO": "EST_04",
    "PONTO_ILUMINACAO": "ELE_01",
    "TOMADA": "ELE_02",
    "QUADRO_ELETRICO": "ELE_03",
    "LUMINARIA": "ELE_04",
    "ELETRODUTO": "ELE_05",
    "PONTO_ELETRICO_GERAL": "ELE_06",
    "PONTO_AGUA": "HID_01",
    "PONTO_ESGOTO": "HID_02",
    "TUBULACAO_HIDRO": "HID_03",
    "REGISTRO": "HID_04",
    "RALO_CAIXA_SIFONADA": "HID_05",
    "ALVENARIA": "ALV_01",
    "BLOCO": "ALV_02",
    "CHAPISCO": "REV_01",
    "REBOCO": "REV_02",
    "CONTRAPISO": "REV_03",
    "PORCELANATO_CERAMICA": "REV_04",
    "REVESTIMENTO_FACHADA": "REV_05",
    "PINTURA_INTERNA": "PIN_01",
    "PINTURA_EXTERNA": "PIN_02",
    "PORTA": "ESQ_01",
    "JANELA": "ESQ_02",
    "VIDRO": "ESQ_03",
    "GUARDA_CORPO": "ESQ_04",
    "MANTA_ASFALTICA": "IMP_01",
    "CRISTALIZACAO": "IMP_02",
    "BACIA_SANITARIA": "LOU_01",
    "LAVATORIO": "LOU_02",
    "CUBA": "LOU_03",
    "CHUVEIRO": "LOU_04",
    "FORRO": "DIV_01",
    "ELEVADOR": "DIV_02",
    "HIDRANTE": "DIV_03",
    "SPRINKLER": "DIV_04",
    "COBERTURA": "DIV_05",
    "DRYWALL": "DIV_06",
    "NAO_CLASSIFICAVEL": None,
}

IND_LOOKUP = {ind[0]: (ind[1], ind[2], ind[3]) for ind in INDICADORES}


def _load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _normalize_text(s: str) -> str:
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s


def load_padroes() -> dict:
    data = _load_json(PAD_FILE)
    out = {}
    for p in data.get("projetos", []):
        slug = p.get("projeto")
        if slug:
            out[slug] = p
    return out


SKIP_UNITS = {"vb", "verba", "gl", "global", "un-", "none", ""}


def _should_keep_item(desc: str, unidade: str, qtd) -> bool:
    """Filtra itens antes de mandar pro Gemma.

    Regras:
    - qtd tem que ser numero > 0 (sem isso não dá pra extrair indicador)
    - unidade tem que existir (pular vb, verba, none)
    - keyword positiva libera direto
    - keyword negativa descarta
    """
    if not isinstance(qtd, (int, float)) or qtd <= 0:
        return False
    un = _normalize_text(unidade).strip()
    if un in SKIP_UNITS:
        return False
    d = _normalize_text(desc)
    for kw in KEEP_KEYWORDS:
        if kw in d:
            return True
    for kw in SKIP_KEYWORDS:
        if kw in d:
            return False
    return True


def collect_all_items(slug: str):
    det = _load_json(DET_DIR / f"{slug}.json")
    items = []
    idx = 0
    skipped = 0
    for aba in det.get("abas", []) or []:
        aba_nome = aba.get("nome", "")
        nome_lower = _normalize_text(aba_nome)
        if any(skip in nome_lower for skip in ["dados_iniciais", "opcao", "opção", "planilha1", "resumo", "bdi", "cronograma"]):
            continue
        for it in aba.get("itens", []) or []:
            desc = str(it.get("descricao", "")).strip()
            if not desc or len(desc) < 3:
                continue
            q = it.get("qtd") if isinstance(it.get("qtd"), (int, float)) else None
            u = str(it.get("unidade", ""))
            if not _should_keep_item(desc, u, q):
                skipped += 1
                continue
            items.append({
                "id": idx,
                "descricao": desc[:150],
                "unidade": str(it.get("unidade", ""))[:12],
                "qtd": it.get("qtd") if isinstance(it.get("qtd"), (int, float)) else None,
                "pu": it.get("pu") if isinstance(it.get("pu"), (int, float)) else None,
                "total": it.get("total") if isinstance(it.get("total"), (int, float)) else None,
                "aba": aba_nome,
            })
            idx += 1

    ix = _load_json(IDX_DIR / f"{slug}.json")
    meta = {
        "ac": ix.get("ac") or 0,
        "ur": ix.get("ur") or 0,
        "total": ix.get("total") or 0,
        "n_pavimentos": ix.get("n_pavimentos") or 0,
        "n_torres": ix.get("n_torres") or 0,
    }
    for aba in det.get("abas", []) or []:
        if "dados_iniciais" in _normalize_text(aba.get("nome", "")):
            for it in aba.get("itens", []) or []:
                desc_l = _normalize_text(it.get("descricao", ""))
                qtd = it.get("qtd")
                if not isinstance(qtd, (int, float)):
                    continue
                if "total de pavimento" in desc_l or "numero total de pavimento" in desc_l:
                    meta["n_pavimentos"] = meta["n_pavimentos"] or int(qtd)
                if "numero de torre" in desc_l or "torres" in desc_l:
                    meta["n_torres"] = meta["n_torres"] or int(qtd)
                if "area total construida" in desc_l or "area construida" in desc_l:
                    meta["ac"] = meta["ac"] or qtd
                if "unidades residenciais" in desc_l:
                    meta["ur"] = meta["ur"] or int(qtd)
            break

    return items, meta


def build_gemma_prompt(items_batch):
    items_text = "\n".join(
        f"[{it['id']}] {it['descricao']} | un={it['unidade']} | qtd={it['qtd']}"
        for it in items_batch
    )
    categories_list = "\n".join(f"- {cat}" for cat in GEMMA_CATEGORIES if cat != "NAO_CLASSIFICAVEL")
    return f"""Você é um classificador de itens de orçamento de construção civil.
Classifique CADA item abaixo em UMA das categorias. Extraia a QUANTIDADE FÍSICA do item.

## CATEGORIAS (use exatamente estes nomes):
{categories_list}
- NAO_CLASSIFICAVEL (não se encaixa em nenhuma)

## REGRAS:
1. Use a DESCRIÇÃO e UNIDADE pra decidir a categoria
2. Se qtd=None ou qtd=0, retorne qtd: null
3. Foque em QUANTIDADE FÍSICA (m², m³, kg, un, m), NÃO em custo
4. Cada item recebe EXATAMENTE 1 categoria
5. Itens genéricos como "MÃO DE OBRA", "BDI", "ADMINISTRAÇÃO" -> NAO_CLASSIFICAVEL
6. "Ponto de luz", "ponto elétrico", "ponto de iluminação" -> PONTO_ILUMINACAO
7. "Alvenaria de bloco" -> ALVENARIA (m²). "Bloco cerâmico", "bloco de concreto" -> BLOCO (un)
8. "Impermeabilização" genérica -> MANTA_ASFALTICA. "Cristalização" -> CRISTALIZACAO
9. "Forro de gesso", "forro drywall", "forro mineral" -> FORRO
10. "Divisória drywall", "parede drywall" -> DRYWALL (m²)

## ITENS:
{items_text}

## RESPONDA com JSON array (sem texto adicional):
[{{"id": 0, "cat": "CONCRETO", "qtd": 150.0}}, ...]

Se o item não tem quantidade extraível, retorne qtd: null.
Retorne APENAS o JSON array."""


def call_gemma(prompt: str) -> dict:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.9,
            "num_predict": 6000,
            "num_ctx": 12288,
        },
    }, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def parse_gemma_response(raw: str):
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```\s*$", "", raw, flags=re.MULTILINE)
    start = raw.find("[")
    end = raw.rfind("]")
    if start < 0 or end < 0 or end <= start:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            j = raw[start:end + 1]
            obj = json.loads(j)
            if isinstance(obj, dict):
                for key in ("items", "results", "data", "classificacao"):
                    if key in obj and isinstance(obj[key], list):
                        return obj[key]
                return [obj]
        raise ValueError(f"No JSON found in response: {raw[:300]}")
    j = raw[start:end + 1]
    try:
        return json.loads(j)
    except json.JSONDecodeError:
        j2 = re.sub(r",\s*]", "]", j)
        j2 = re.sub(r",\s*}", "}", j2)
        return json.loads(j2)


def process_project(slug: str, padroes: dict, retry: int = 1, use_gemma: bool = False) -> dict:
    t0 = time.time()
    items, meta = collect_all_items(slug)

    pad_info = padroes.get(slug, {})
    padrao = pad_info.get("padrao", "desconhecido")
    if pad_info.get("ac") and not meta["ac"]:
        meta["ac"] = pad_info["ac"]
    if pad_info.get("ur") and not meta["ur"]:
        meta["ur"] = pad_info["ur"]

    all_classified = []
    if use_gemma:
        n_batches = (len(items) + BATCH_SIZE - 1) // BATCH_SIZE
        for batch_idx in range(n_batches):
            batch = items[batch_idx * BATCH_SIZE:(batch_idx + 1) * BATCH_SIZE]
            prompt = build_gemma_prompt(batch)
            last_err = None
            success = False
            for attempt in range(retry + 1):
                try:
                    r = call_gemma(prompt)
                    raw = r.get("response", "")
                    classified = parse_gemma_response(raw)
                    all_classified.extend(classified)
                    success = True
                    break
                except Exception as e:
                    last_err = e
                    time.sleep(2)
            if not success:
                print(f"  [warn] batch {batch_idx+1}/{n_batches} failed: {last_err}", flush=True)
    else:
        # Local keyword-based classification (fast)
        for it in items:
            cat = classify_local(it["descricao"], it.get("unidade", ""))
            all_classified.append({
                "id": it["id"],
                "cat": cat,
                "qtd": it.get("qtd"),
            })

    item_by_id = {it["id"]: it for it in items}

    indicadores = {}
    nao_classificados = []
    for cl in all_classified:
        if not isinstance(cl, dict):
            continue
        item_id = cl.get("id")
        cat = cl.get("cat") or cl.get("categoria") or "NAO_CLASSIFICAVEL"
        qtd = cl.get("qtd") if cl.get("qtd") is not None else cl.get("quantidade")

        if cat == "NAO_CLASSIFICAVEL" or cat not in GEMMA_CATEGORIES:
            orig = item_by_id.get(item_id, {})
            nao_classificados.append(orig.get("descricao", f"id={item_id}"))
            continue

        ind_id = GEMMA_CATEGORIES[cat]
        if ind_id is None:
            continue

        if qtd is None or qtd == 0:
            orig = item_by_id.get(item_id, {})
            qtd = orig.get("qtd")
        if qtd is None or not isinstance(qtd, (int, float)) or qtd <= 0:
            continue

        if ind_id not in indicadores:
            indicadores[ind_id] = {"soma_qtd": 0, "n_itens": 0, "itens_fonte": []}
        indicadores[ind_id]["soma_qtd"] += qtd
        indicadores[ind_id]["n_itens"] += 1
        orig = item_by_id.get(item_id, {})
        if orig.get("descricao"):
            indicadores[ind_id]["itens_fonte"].append(orig["descricao"][:80])

    result_indicadores = {}
    for ind_id, agg in indicadores.items():
        name, unit, norm_by = IND_LOOKUP[ind_id]
        divisor = 1
        if norm_by == "ac":
            divisor = meta["ac"] or 1
        elif norm_by == "ur":
            divisor = meta["ur"] or 1
        elif norm_by == "pav":
            divisor = meta["n_pavimentos"] or 1
        elif norm_by == "torre":
            divisor = meta["n_torres"] or 1

        valor = round(agg["soma_qtd"] / divisor, 4) if divisor > 0 else None
        if valor is not None and valor > 0:
            result_indicadores[name] = {
                "id": ind_id,
                "valor": valor,
                "unidade": unit,
                "soma_bruta": round(agg["soma_qtd"], 2),
                "n_itens": agg["n_itens"],
                "itens_fonte": agg["itens_fonte"][:10],
            }

    conc = indicadores.get("EST_01")
    aco = indicadores.get("EST_02")
    if conc and aco and conc["soma_qtd"] > 0:
        taxa = round(aco["soma_qtd"] / conc["soma_qtd"], 2)
        result_indicadores["taxa_aco_kg_por_m3"] = {
            "id": "EST_03b",
            "valor": taxa,
            "unidade": "kg/m³",
            "soma_bruta": aco["soma_qtd"],
            "n_itens": aco["n_itens"],
            "itens_fonte": ["(calculado: aço total / concreto total)"],
        }

    duration = round(time.time() - t0, 1)
    result = {
        "slug": slug,
        "padrao": padrao,
        "ac_m2": meta["ac"],
        "ur": meta["ur"],
        "n_pavimentos": meta["n_pavimentos"],
        "n_torres": meta["n_torres"],
        "total_r$": meta["total"],
        "data_extracao": datetime.now().isoformat(timespec="seconds"),
        "duration_s": duration,
        "n_itens_processados": len(items),
        "n_itens_classificados": len(all_classified),
        "n_indicadores_extraidos": len(result_indicadores),
        "indicadores": result_indicadores,
        "nao_classificados_sample": nao_classificados[:20],
    }

    out_path = OUT_DIR / f"{slug}.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


def log_event(e: dict) -> None:
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue() -> dict:
    if QUEUE.exists():
        return json.loads(QUEUE.read_text(encoding="utf-8"))
    slugs = sorted(p.stem for p in DET_DIR.glob("*.json"))
    q = {"created": datetime.now().isoformat(timespec="seconds"),
         "phase": "phase20-indicadores-produto",
         "items": {s: {"status": "pending"} for s in slugs}}
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    return q


def save_queue(q: dict) -> None:
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Phase 20: Extract product indicators via Gemma")
    ap.add_argument("--slug", default=None, help="process only this project")
    ap.add_argument("--test", action="store_true", help="smoke test on 3 projects")
    ap.add_argument("--retry-failed", action="store_true", help="reprocess failed only")
    ap.add_argument("--use-gemma", action="store_true", help="use Gemma (slow); default is local keyword rules")
    args = ap.parse_args()

    padroes = load_padroes()
    print(f"Loaded {len(padroes)} project classifications", flush=True)

    if args.slug:
        print(f"=== {args.slug} ===", flush=True)
        r = process_project(args.slug, padroes, use_gemma=args.use_gemma)
        print(f"  indicadores: {r['n_indicadores_extraidos']}, items: {r['n_itens_classificados']}/{r['n_itens_processados']}, {r['duration_s']}s", flush=True)
        for name, ind in sorted(r["indicadores"].items()):
            print(f"    {name:<45} {ind['valor']:>10.4f} {ind['unidade']}", flush=True)
        return

    slugs_test = ["amalfi-maiori", "thozen-mirador-de-alicante", "brasin-redentor"]
    if args.test:
        for s in slugs_test:
            if not (DET_DIR / f"{s}.json").exists():
                print(f"  [skip] {s} not found", flush=True)
                continue
            print(f"\n=== {s} ===", flush=True)
            try:
                r = process_project(s, padroes, use_gemma=args.use_gemma)
                print(f"  indicadores: {r['n_indicadores_extraidos']}, {r['duration_s']}s", flush=True)
                for name, ind in sorted(r["indicadores"].items())[:10]:
                    print(f"    {name:<45} {ind['valor']:>10.4f} {ind['unidade']}", flush=True)
            except Exception as e:
                print(f"  FAIL: {e}", flush=True)
        return

    q = init_queue()
    pending = [s for s, v in q["items"].items()
               if v["status"] == "pending" or (args.retry_failed and v["status"] == "failed")]
    print(f"Pendentes: {len(pending)}/{len(q['items'])}", flush=True)
    t_start = time.time()

    for i, slug in enumerate(pending, start=1):
        elapsed = time.time() - t_start
        eta = (elapsed / i) * (len(pending) - i) if i > 0 else 0
        print(f"\n[{i}/{len(pending)}] {slug} (elapsed {elapsed/60:.1f}min, eta {eta/60:.1f}min)", flush=True)
        q["items"][slug] = {"status": "in_progress"}
        save_queue(q)
        try:
            r = process_project(slug, padroes, use_gemma=args.use_gemma)
            q["items"][slug] = {
                "status": "done",
                "n_indicadores": r["n_indicadores_extraidos"],
                "duration_s": r["duration_s"],
            }
            log_event({"projeto": slug, "status": "done",
                        "n_indicadores": r["n_indicadores_extraidos"],
                        "duration_s": r["duration_s"]})
            print(f"  -> {r['n_indicadores_extraidos']} indicadores em {r['duration_s']}s", flush=True)
        except Exception as e:
            err = str(e)[:200]
            q["items"][slug] = {"status": "failed", "error": err}
            log_event({"projeto": slug, "status": "failed", "error": err})
            print(f"  FAIL: {err}", flush=True)
        save_queue(q)

    done = {s: v for s, v in q["items"].items() if v["status"] == "done"}
    failed = {s: v for s, v in q["items"].items() if v["status"] == "failed"}
    print(f"\n{'='*60}", flush=True)
    print(f"Total done:   {len(done)}/{len(q['items'])}", flush=True)
    print(f"Total failed: {len(failed)}", flush=True)
    if done:
        avg_ind = sum(v.get("n_indicadores", 0) for v in done.values()) / len(done)
        print(f"Avg indicadores/projeto: {avg_ind:.1f}", flush=True)


if __name__ == "__main__":
    main()
