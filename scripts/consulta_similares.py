#!/usr/bin/env python3
"""Módulo de consulta à base qualitativa — puro Python, sem Gemma.

Usado pelos scripts de geração de orçamento (paramétrico e executivo) pra
encontrar projetos similares na base e enriquecer a saída com sub-disciplinas
reais, premissas técnicas e itens detalhados vindos de projetos entregues.

Funções principais:
    projetos_similares(ac, ur, padrao)        → busca base
    enriquecer_parametrico(similares)         → camada leve (sub-disciplinas)
    enriquecer_executivo(similares, mg)       → camada pesada (itens-detalhados)
    premissas_consolidadas(similares)         → premissas técnicas consolidadas
    decisoes_chave(similares)                 → decisões que afetam o executivo
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

BASE = Path.home() / "orcamentos-openclaw" / "base"
INDICES = BASE / "indices-executivo"
ITENS_DETALHADOS = BASE / "itens-detalhados"
PREMISSAS = BASE / "premissas"

_CACHE: dict[str, Any] = {}


def _load_all_projects() -> list[dict]:
    if "all_projects" in _CACHE:
        return _CACHE["all_projects"]
    out = []
    for p in sorted(INDICES.glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            d.setdefault("_slug", p.stem)
            out.append(d)
        except Exception:
            continue
    _CACHE["all_projects"] = out
    return out


def _load_itens_detalhados(slug: str) -> dict | None:
    cache_key = f"det_{slug}"
    if cache_key in _CACHE:
        return _CACHE[cache_key]
    p = ITENS_DETALHADOS / f"{slug}.json"
    if not p.exists():
        _CACHE[cache_key] = None
        return None
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        _CACHE[cache_key] = d
        return d
    except Exception:
        _CACHE[cache_key] = None
        return None


def projetos_similares(ac: float, ur: int | None = None, padrao: str | None = None,
                        n: int = 5, ac_tolerance: float = 0.25) -> list[dict]:
    """Retorna os n projetos mais similares ao alvo.

    Score = (1 - |ac_delta|/ac) * 0.6
          + match_padrao * 0.2
          + match_ur * 0.2

    Filtra projetos sem camada qualitativa (sem sub_disciplinas).
    """
    projetos = _load_all_projects()
    scored = []

    for p in projetos:
        p_ac = p.get("ac")
        if not p_ac or p_ac <= 0:
            continue
        qual = p.get("qualitative") or {}
        if not qual.get("sub_disciplinas"):
            continue

        ac_delta = abs(p_ac - ac) / ac
        if ac_delta > ac_tolerance * 2:
            continue

        score = (1 - ac_delta) * 0.6

        if ur and p.get("ur"):
            ur_delta = abs(p["ur"] - ur) / max(ur, 1)
            score += max(0, 1 - ur_delta) * 0.2

        if padrao:
            pdf_meta = qual.get("pdf_metadata") or {}
            p_padrao = str(pdf_meta.get("tipologia") or "").lower()
            if padrao.lower() in p_padrao:
                score += 0.2

        scored.append((score, p))

    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored[:n]]


def enriquecer_parametrico(similares: list[dict]) -> dict:
    """Extrai a camada leve: sub-disciplinas agregadas por macrogrupo.

    Retorna:
        {
            "sub_disciplinas_por_mg": {
                "Estrutura": [
                    {"sub": "Concreto", "freq": 5, "fontes": [...], "itens_exemplo": [...]},
                    ...
                ],
                ...
            },
            "n_similares": 5,
            "similares": [slug, slug, ...]
        }
    """
    por_mg: dict[str, dict[str, dict]] = defaultdict(dict)

    for p in similares:
        slug = p["_slug"]
        for sd in (p.get("qualitative") or {}).get("sub_disciplinas", []):
            mg_raw = str(sd.get("macrogrupo", "")).strip()
            mg = normalize_macrogrupo(mg_raw)
            sub = str(sd.get("sub_disciplina", "")).strip()
            if not mg or not sub:
                continue
            key = sub.lower()
            if key not in por_mg[mg]:
                por_mg[mg][key] = {
                    "sub": sub,
                    "freq": 0,
                    "fontes": [],
                    "itens_exemplo": [],
                }
            entry = por_mg[mg][key]
            entry["freq"] += 1
            if slug not in entry["fontes"]:
                entry["fontes"].append(slug)
            for it in sd.get("itens_exemplo") or []:
                if it and it not in entry["itens_exemplo"]:
                    entry["itens_exemplo"].append(it)

    result = {}
    for mg, subs in por_mg.items():
        lst = sorted(subs.values(), key=lambda x: -x["freq"])
        result[mg] = lst

    return {
        "sub_disciplinas_por_mg": result,
        "n_similares": len(similares),
        "similares": [p["_slug"] for p in similares],
    }


MG_CANONICO = [
    "Gerenciamento", "Movimentação de Terra", "Infraestrutura", "Supraestrutura",
    "Alvenaria", "Impermeabilização", "Instalações", "Sistemas Especiais",
    "Climatização", "Rev. Interno Parede", "Teto", "Pisos", "Pintura",
    "Esquadrias", "Louças e Metais", "Fachada", "Complementares", "Imprevistos",
]

MG_KEYWORDS = {
    "Gerenciamento": ["gerenciamento", "admin", "administrativo", "ctn", "ger_", "projet", "legal", "taxa", "canteiro", "epc"],
    "Movimentação de Terra": ["mov de terra", "mov. terra", "movimenta", "escava", "aterro", "bota-fora", "terraplen"],
    "Infraestrutura": ["infra", "fundac", "fundaç", "estaca", "conten", "sapata", "bloco de fundac", "hélice"],
    "Supraestrutura": ["supra", "supraestrutura", "concreto", "forma", "escoramento", "armadura", "armação", "aço ca", "laje"],
    "Alvenaria": ["alven", "bloco cer", "drywall", "divisor", "sical", "verga"],
    "Impermeabilização": ["impermea", "manta asfal", "argamassa polim"],
    "Instalações": ["instalac", "instalaç", "elétr", "eletric", "hidro", "hidrául", "ppci", "preven", "glp", "gás", "telecom", "sprink", "sanit"],
    "Sistemas Especiais": ["elevador", "piscina", " ete ", "gerador", "sist especi", "automac", "cftv", "alarme"],
    "Climatização": ["climat", "ar cond", "exaust", "vrf", " ac "],
    "Rev. Interno Parede": ["revest int", "rev int", "reboco int", "cerâmica parede", "chapisco"],
    "Teto": ["forro", "teto", "gesso"],
    "Pisos": ["piso", "contrapiso", "laminado", "porcelanato", "rodapé", "cerâmica piso"],
    "Pintura": ["pintura", "epoxi", "massa corrida", "selador", "látex", "acrílica"],
    "Esquadrias": ["esquadria", "alumínio", "vidro", "pele de vidro", "guarda corpo", "porta ", "janela", "brise"],
    "Louças e Metais": ["louça", "bacia", "cuba", "torneira", "misturador", "granito", "bancada"],
    "Fachada": ["fachada", "pastilha", "textura ext", "rev ext"],
    "Complementares": ["complement", "calçada", "paisag", "mobiliário", "sinaliz", "limpeza final"],
    "Imprevistos": ["imprevist", "conting"],
}

MG_NORMALIZE = {
    "estrutura": "Supraestrutura",
    "estruturas": "Supraestrutura",
    "estrutura e fundações": "Supraestrutura",
    "estrutura e fundação": "Supraestrutura",
    "estrutura/execução": "Supraestrutura",
    "superestrutura": "Supraestrutura",
    "fundações": "Infraestrutura",
    "fundação": "Infraestrutura",
    "acabamentos": "Rev. Interno Parede",
    "acabamentos internos": "Rev. Interno Parede",
    "instalações e equipamentos": "Instalações",
    "instalações elétricas, hidráulicas, glp e preventivas": "Instalações",
    "serviços complementares": "Complementares",
    "serviços gerais e administrativo": "Gerenciamento",
    "serviços técnicos/administrativos": "Gerenciamento",
    "projetos e documentação": "Gerenciamento",
    "mobiliário": "Complementares",
    "acabamentos e mobiliário": "Complementares",
    "fechamento e acabamentos": "Alvenaria",
    "comunicações e segurança": "Sistemas Especiais",
}


def normalize_macrogrupo(mg_raw: str) -> str:
    """Normaliza nome de macrogrupo vindo do Gemma para um dos 18 canônicos."""
    if not mg_raw:
        return ""
    n = mg_raw.strip().lower()
    if n in MG_NORMALIZE:
        return MG_NORMALIZE[n]
    for canon in MG_CANONICO:
        if canon.lower() == n:
            return canon
    for canon in MG_CANONICO:
        canon_low = canon.lower()
        if canon_low in n or any(w in n for w in canon_low.split()):
            return canon
    return mg_raw.strip()


_HIGH_SIGNAL_KW = {
    "Supraestrutura": ["supraestrut", "supra estrut", "concreto usinado", "armadura", "armação", "escoramento", "fck", "ca-50", "ca50"],
    "Infraestrutura": ["fundac", "fundaç", "estaca", "hélice", "tubulão", "sapata", "infraestrut", "bloco de fund", "viga baldrame"],
    "Movimentação de Terra": ["movimentaç", "escavaç", "aterro", "bota-fora", "terraplen"],
    "Alvenaria": ["alvenaria", "bloco cer", "drywall", "divisor", "verga", "encunh"],
    "Impermeabilização": ["impermea"],
    "Instalações": ["hidrául", "hidrossan", "elétrica", "elétric", "telecom", "spda", "gás combust", "preven", "sprink", "incênd", "ppci", "subestaç", "transformador"],
    "Sistemas Especiais": ["elevador", "piscina", "gerador", " ete", "automaç", "cftv", "alarme", "porteiro"],
    "Climatização": ["climatiz", "ar cond", "exausto", " vrf", "split"],
    "Esquadrias": ["esquadria", "alumínio", "porta de ", "porta corta", "janela", "guarda corpo", "pele de vidro", "brise"],
    "Pisos": ["porcelanato", "laminado", "cerâmica piso", "contrapiso", "rodapé", "soleira"],
    "Pintura": ["pintura", "epóxi", "selador", "massa corrida", "látex acríl"],
    "Teto": ["forro", "gesso liso"],
    "Rev. Interno Parede": ["reboco", "chapisco", "cerâmica parede"],
    "Louças e Metais": ["bacia ", "cuba ", "torneira", "misturador", "registro", "bancada granito", "bancada marmore"],
    "Fachada": ["fachada", "pastilha", "textura ext", "rev ext", "argamassa fachada"],
    "Gerenciamento": ["projet arquit", "projet estrut", "projet hidro", "projet elétr", "taxa cartór", "alvará", "habite-se", "epc ", "epi", "almoxar"],
    "Complementares": ["paisag", "calçada", "ligação concession", "limpeza final", "mobiliário"],
    "Imprevistos": ["imprevist", "conting", "reserva técn"],
}


def _match_high_signal(text: str) -> str | None:
    if not text:
        return None
    text = text.lower()
    for mg, kws in _HIGH_SIGNAL_KW.items():
        for kw in kws:
            if kw in text:
                return mg
    return None


def _classify_item(descricao: str, secao: str = "", aba: str = "") -> str | None:
    """Classifica um item nos 18 macrogrupos.

    Prioridade:
        1. Aba (alta confiança) — o nome da aba geralmente identifica disciplina
        2. Seção do item dentro da aba
        3. Descrição com keywords de alta sinal (estritas)
    """
    aba_match = _match_high_signal(aba)
    if aba_match:
        return aba_match

    secao_match = _match_high_signal(secao)
    if secao_match:
        return secao_match

    return _match_high_signal(descricao)


def _classify_aba(nome_aba: str) -> str | None:
    n = nome_aba.lower()
    for mg, kws in MG_KEYWORDS.items():
        for kw in kws:
            if kw in n:
                return mg
    return None


def enriquecer_executivo(similares: list[dict], macrogrupo: str,
                          top_n: int = 30, min_frequency: int = 1) -> dict:
    """Extrai a camada pesada: itens reais dos similares no macrogrupo alvo.

    Para cada projeto similar, carrega itens-detalhados, filtra abas que
    mapeiam para o macrogrupo alvo e coleta os itens. Depois agrega:
        - itens que aparecem em ≥ min_frequency projetos (por descrição normalizada)
        - top N por valor mediano

    Retorna:
        {
            "macrogrupo": "Estrutura",
            "n_projetos_analisados": 5,
            "n_itens_coletados": 420,
            "itens_agregados": [
                {
                    "descricao": "Concreto Usinado FCK = 35MPa Bombeavel",
                    "unidade": "m3",
                    "pu_mediano": 465.0,
                    "pu_min": 380.0,
                    "pu_max": 510.0,
                    "qtd_mediana": 1250.5,
                    "freq_projetos": 4,
                    "fontes": ["amalfi-tramonti", "brasin-redentor", ...]
                },
                ...
            ]
        }
    """
    import statistics

    items_raw: list[dict] = []
    projetos_analisados = 0

    for p in similares:
        slug = p["_slug"]
        det = _load_itens_detalhados(slug)
        if not det:
            continue
        projetos_analisados += 1

        for aba in det.get("abas", []):
            nome_aba = aba.get("nome", "")
            for it in aba.get("itens", []):
                desc = str(it.get("descricao", "")).strip()
                if not desc or len(desc) < 4:
                    continue
                secao = str(it.get("secao", "")).strip()
                mg_classified = _classify_item(desc, secao=secao, aba=nome_aba)
                if mg_classified != macrogrupo:
                    continue
                pu = it.get("pu")
                qtd = it.get("qtd")
                total = it.get("total")
                un_str = str(it.get("unidade") or "").strip().lower()
                pu_ok = isinstance(pu, (int, float)) and pu > 0
                qtd_ok = isinstance(qtd, (int, float)) and qtd > 0
                if not pu_ok or not qtd_ok:
                    continue
                if un_str in ("vb", "vg", "gl", "global", "verba"):
                    continue
                if qtd == 1 and isinstance(pu, (int, float)) and pu > 5000:
                    continue
                items_raw.append({
                    "descricao": desc,
                    "unidade": it.get("unidade") or "",
                    "pu": pu,
                    "qtd": qtd,
                    "total": total,
                    "slug": slug,
                    "aba": nome_aba,
                })

    grouped: dict[str, list[dict]] = defaultdict(list)
    for it in items_raw:
        key = it["descricao"].lower()[:50]
        grouped[key].append(it)

    agg = []
    for key, lst in grouped.items():
        slugs = sorted({it["slug"] for it in lst})
        if len(slugs) < min_frequency:
            continue
        pus = [float(it["pu"]) for it in lst if it.get("pu") and isinstance(it["pu"], (int, float)) and it["pu"] > 0]
        qtds = [float(it["qtd"]) for it in lst if it.get("qtd") and isinstance(it["qtd"], (int, float)) and it["qtd"] > 0]
        totals = [float(it["total"]) for it in lst if it.get("total") and isinstance(it["total"], (int, float)) and it["total"] > 0]
        if not pus and not totals:
            continue

        first = lst[0]
        agg.append({
            "descricao": first["descricao"],
            "unidade": first["unidade"],
            "pu_mediano": statistics.median(pus) if pus else None,
            "pu_min": min(pus) if pus else None,
            "pu_max": max(pus) if pus else None,
            "qtd_mediana": statistics.median(qtds) if qtds else None,
            "total_mediano": statistics.median(totals) if totals else None,
            "freq_projetos": len(slugs),
            "fontes": slugs,
            "n_ocorrencias": len(lst),
        })

    agg.sort(key=lambda x: (-(x.get("total_mediano") or x.get("pu_mediano") or 0), -x["freq_projetos"]))

    return {
        "macrogrupo": macrogrupo,
        "n_projetos_analisados": projetos_analisados,
        "n_itens_coletados": len(items_raw),
        "itens_agregados": agg[:top_n],
    }


def premissas_consolidadas(similares: list[dict], min_freq: int = 1) -> list[dict]:
    """Consolida premissas técnicas dos similares, agrupando as comuns.

    Retorna:
        [
            {
                "area": "Fundação",
                "premissa": "Considerado blocos, vigas e cisterna",
                "freq": 3,
                "fontes": ["amalfi-tramonti", ...]
            }
        ]
    """
    grouped: dict[str, dict] = defaultdict(lambda: {"fontes": [], "raw": []})

    for p in similares:
        slug = p["_slug"]
        for pr in (p.get("qualitative") or {}).get("premissas_tecnicas", []):
            area = str(pr.get("area", "")).strip()
            texto = str(pr.get("premissa", "")).strip()
            if not texto:
                continue
            key = (area.lower(), texto.lower()[:80])
            grouped_key = f"{area}::{texto[:80]}"
            if slug not in grouped[grouped_key]["fontes"]:
                grouped[grouped_key]["fontes"].append(slug)
            grouped[grouped_key]["raw"].append({"area": area, "premissa": texto})

    result = []
    for gk, data in grouped.items():
        if len(data["fontes"]) < min_freq:
            continue
        raw0 = data["raw"][0]
        result.append({
            "area": raw0["area"],
            "premissa": raw0["premissa"],
            "freq": len(data["fontes"]),
            "fontes": data["fontes"],
        })

    result.sort(key=lambda x: -x["freq"])
    return result


def decisoes_chave(similares: list[dict]) -> list[dict]:
    """Decisões do PDF consolidadas para o gate de validação."""
    grouped: dict[str, dict] = defaultdict(lambda: {"fontes": [], "raw": []})

    for p in similares:
        slug = p["_slug"]
        for d in (p.get("qualitative") or {}).get("decisoes_consolidadas", []):
            ctx = str(d.get("contexto", "")).strip()
            dec = str(d.get("decisao", "")).strip()
            if not dec:
                continue
            key = f"{ctx}::{dec[:80]}"
            if slug not in grouped[key]["fontes"]:
                grouped[key]["fontes"].append(slug)
            grouped[key]["raw"].append({"contexto": ctx, "decisao": dec})

    result = []
    for gk, data in grouped.items():
        raw0 = data["raw"][0]
        result.append({
            "contexto": raw0["contexto"],
            "decisao": raw0["decisao"],
            "freq": len(data["fontes"]),
            "fontes": data["fontes"],
        })
    result.sort(key=lambda x: -x["freq"])
    return result


DISCIPLINA_TO_MG = {
    "canteiro": "Gerenciamento",
    "ger_administrativo": "Gerenciamento",
    "ger_executivo": "Gerenciamento",
    "gerenciamento": "Gerenciamento",
    "movimentacao de terra": "Movimentação de Terra",
    "mov de terra": "Movimentação de Terra",
    "fundacoes": "Infraestrutura",
    "fundações": "Infraestrutura",
    "infraestrutura": "Infraestrutura",
    "contencao": "Infraestrutura",
    "contenção": "Infraestrutura",
    "supraestrutura": "Supraestrutura",
    "estrutura": "Supraestrutura",
    "estruturas": "Supraestrutura",
    "alvenaria": "Alvenaria",
    "alvenarias": "Alvenaria",
    "vedacoes": "Alvenaria",
    "impermeabilizacao": "Impermeabilização",
    "impermeabilização": "Impermeabilização",
    "instalacoes eletricas": "Instalações",
    "elétrica": "Instalações",
    "eletrica": "Instalações",
    "instalacoes hidraulicas": "Instalações",
    "hidraulico": "Instalações",
    "hidráulico": "Instalações",
    "hidrossanitario": "Instalações",
    "hidrossanitário": "Instalações",
    "gas": "Instalações",
    "gás": "Instalações",
    "spda": "Instalações",
    "preventivo": "Instalações",
    "pci": "Instalações",
    "telecom": "Instalações",
    "instalacoes": "Instalações",
    "sistemas especiais": "Sistemas Especiais",
    "elevadores": "Sistemas Especiais",
    "climatizacao": "Climatização",
    "climatização": "Climatização",
    "exaustao": "Climatização",
    "revestimento interno": "Rev. Interno Parede",
    "rev. interno": "Rev. Interno Parede",
    "rev int parede": "Rev. Interno Parede",
    "teto": "Teto",
    "forro": "Teto",
    "pisos": "Pisos",
    "piso": "Pisos",
    "pintura": "Pintura",
    "esquadrias": "Esquadrias",
    "loucas e metais": "Louças e Metais",
    "louças e metais": "Louças e Metais",
    "fachada": "Fachada",
    "complementares": "Complementares",
    "servicos complementares": "Complementares",
    "serviços complementares": "Complementares",
    "imprevistos": "Imprevistos",
    "mobiliario": "Complementares",
    "mobiliário": "Complementares",
    "loucas": "Louças e Metais",
}


def _disciplina_to_mg(name: str) -> str | None:
    if not name:
        return None
    n = name.strip().lower()
    if n in DISCIPLINA_TO_MG:
        return DISCIPLINA_TO_MG[n]
    for k, v in DISCIPLINA_TO_MG.items():
        if k in n or n in k:
            return v
    return None


def valores_macrogrupos_v2(similares: list[dict], ac_alvo: float) -> dict:
    """Calcula valores estimados por macrogrupo cross-similares (R$/m² mediano × AC alvo).

    Lê os campos `macrogrupos` e `disciplinas` dos JSONs de similares, mapeia
    pros 18 canônicos, calcula R$/m² mediano por macrogrupo e multiplica pelo
    AC alvo. Retorna dict {macrogrupo: {total_estimado, rsm2_mediano, fontes, n_amostras}}.
    """
    import statistics

    rsm2_amostras: dict[str, list[tuple[float, str]]] = defaultdict(list)

    for p in similares:
        slug = p["_slug"]
        ac_p = p.get("ac")
        if not ac_p or ac_p <= 0:
            continue

        macros = p.get("macrogrupos") or {}
        if isinstance(macros, dict) and macros:
            for mg_raw, val in macros.items():
                mg = normalize_macrogrupo(mg_raw)
                if not mg:
                    continue
                if isinstance(val, dict):
                    total = val.get("total") or val.get("R$") or val.get("valor")
                else:
                    total = val
                if isinstance(total, (int, float)) and total > 0:
                    rsm2_amostras[mg].append((total / ac_p, slug))

        disciplinas = p.get("disciplinas") or {}
        if isinstance(disciplinas, dict):
            for disc_name, disc_data in disciplinas.items():
                mg = _disciplina_to_mg(disc_name)
                if not mg:
                    continue
                if isinstance(disc_data, dict):
                    total = disc_data.get("total")
                    if isinstance(total, (int, float)) and total > 100:
                        rsm2_amostras[mg].append((total / ac_p, slug))

    result = {}
    for mg, amostras in rsm2_amostras.items():
        rsm2_filtered = [r for r, _ in amostras if r >= 1.0]
        if not rsm2_filtered:
            continue
        slugs_used = sorted({s for r, s in amostras if r >= 1.0})
        med = statistics.median(rsm2_filtered)
        mean = statistics.mean(rsm2_filtered)
        rsm2_chosen = max(med, mean)
        result[mg] = {
            "rsm2_mediano": med,
            "rsm2_mean": mean,
            "rsm2_min": min(rsm2_filtered),
            "rsm2_max": max(rsm2_filtered),
            "total_estimado": rsm2_chosen * ac_alvo,
            "n_amostras": len(rsm2_filtered),
            "fontes": slugs_used,
        }

    return result


CALIBRATION_KEY_TO_MG = {
    "Gerenciamento_rsm2": "Gerenciamento",
    "Mov.Terra_rsm2": "Movimentação de Terra",
    "Infraestrutura_rsm2": "Infraestrutura",
    "Supraestrutura_rsm2": "Supraestrutura",
    "Alvenaria_rsm2": "Alvenaria",
    "Impermeabilização_rsm2": "Impermeabilização",
    "Instalações_rsm2": "Instalações",
    "Sist.Especiais_rsm2": "Sistemas Especiais",
    "Climatização_rsm2": "Climatização",
    "Rev.Int.Parede_rsm2": "Rev. Interno Parede",
    "Teto_rsm2": "Teto",
    "Pisos_rsm2": "Pisos",
    "Pintura_rsm2": "Pintura",
    "Esquadrias_rsm2": "Esquadrias",
    "Louças_rsm2": "Louças e Metais",
    "Fachada_rsm2": "Fachada",
    "Complementares_rsm2": "Complementares",
    "Imprevistos_rsm2": "Imprevistos",
}


PADRAO_MULTIPLIERS = {
    "Gerenciamento": {"medio": 1.0, "medio-alto": 1.05, "alto": 1.10, "luxo": 1.20, "economico": 0.90},
    "Movimentação de Terra": {"medio": 1.0, "medio-alto": 1.0, "alto": 1.0, "luxo": 1.0, "economico": 1.0},
    "Infraestrutura": {"medio": 1.0, "medio-alto": 1.0, "alto": 1.05, "luxo": 1.10, "economico": 0.95},
    "Supraestrutura": {"medio": 1.0, "medio-alto": 1.02, "alto": 1.05, "luxo": 1.10, "economico": 0.95},
    "Alvenaria": {"medio": 1.0, "medio-alto": 1.05, "alto": 1.10, "luxo": 1.15, "economico": 0.90},
    "Impermeabilização": {"medio": 1.0, "medio-alto": 1.0, "alto": 1.05, "luxo": 1.10, "economico": 0.95},
    "Instalações": {"medio": 1.0, "medio-alto": 1.10, "alto": 1.20, "luxo": 1.40, "economico": 0.85},
    "Sistemas Especiais": {"medio": 1.0, "medio-alto": 1.15, "alto": 1.30, "luxo": 1.60, "economico": 0.75},
    "Climatização": {"medio": 1.0, "medio-alto": 1.10, "alto": 1.30, "luxo": 1.50, "economico": 0.70},
    "Rev. Interno Parede": {"medio": 1.0, "medio-alto": 1.15, "alto": 1.30, "luxo": 1.55, "economico": 0.85},
    "Teto": {"medio": 1.0, "medio-alto": 1.10, "alto": 1.25, "luxo": 1.50, "economico": 0.85},
    "Pisos": {"medio": 1.0, "medio-alto": 1.20, "alto": 1.40, "luxo": 1.70, "economico": 0.80},
    "Pintura": {"medio": 1.0, "medio-alto": 1.10, "alto": 1.20, "luxo": 1.40, "economico": 0.90},
    "Esquadrias": {"medio": 1.0, "medio-alto": 1.20, "alto": 1.40, "luxo": 1.70, "economico": 0.80},
    "Louças e Metais": {"medio": 1.0, "medio-alto": 1.25, "alto": 1.50, "luxo": 2.00, "economico": 0.80},
    "Fachada": {"medio": 1.0, "medio-alto": 1.15, "alto": 1.35, "luxo": 1.70, "economico": 0.85},
    "Complementares": {"medio": 1.0, "medio-alto": 1.10, "alto": 1.20, "luxo": 1.40, "economico": 0.90},
    "Imprevistos": {"medio": 1.0, "medio-alto": 1.0, "alto": 1.0, "luxo": 1.0, "economico": 1.0},
}


def _padrao_key(padrao: str | None) -> str:
    if not padrao:
        return "medio"
    p = padrao.lower().strip()
    if "luxo" in p:
        return "luxo"
    if "médio-alto" in p or "medio-alto" in p:
        return "medio-alto"
    if "alto" in p:
        return "alto"
    if "econ" in p or "baixo" in p:
        return "economico"
    return "medio"


def valores_macrogrupos_calibrados(ac: float, padrao: str | None = None,
                                     usar_media: bool = False) -> dict:
    """Calcula totais por macrogrupo usando calibration-indices.json (base autoritativa V2).

    Esta é a FONTE PRIMÁRIA dos totais. Lê os 18 macrogrupos calibrados
    com R$/m² mediano de N projetos e multiplica pelo AC alvo.

    Aplica multiplicador diferencial por macrogrupo conforme padrão (ver
    PADRAO_MULTIPLIERS): acabamentos sobem mais em alto/luxo, estrutura
    fica neutra.

    Args:
        ac: Área construída em m²
        padrao: Padrão de acabamento (médio/médio-alto/alto/luxo/econômico)
        usar_media: Se True, usa média ao invés de mediana

    Retorna:
        {macrogrupo: {total_estimado, rsm2, multiplicador_aplicado, ...}}
    """
    cal_path = BASE / "calibration-indices.json"
    if not cal_path.exists():
        return {}

    try:
        cal = json.loads(cal_path.read_text(encoding="utf-8"))
    except Exception:
        return {}

    pm = cal.get("por_macrogrupo", {})
    if not pm:
        return {}

    padrao_key = _padrao_key(padrao)

    result = {}
    for cal_key, mg in CALIBRATION_KEY_TO_MG.items():
        stats = pm.get(cal_key)
        if not isinstance(stats, dict):
            continue
        rsm2 = stats.get("media" if usar_media else "mediana", 0)
        if not rsm2:
            continue

        mults = PADRAO_MULTIPLIERS.get(mg, {})
        multiplier = mults.get(padrao_key, 1.0)
        rsm2_adj = rsm2 * multiplier

        result[mg] = {
            "rsm2_mediano": rsm2,
            "rsm2_ajustado": rsm2_adj,
            "rsm2_min": stats.get("min", 0),
            "rsm2_p10": stats.get("p10", 0),
            "rsm2_p25": stats.get("p25", 0),
            "rsm2_p75": stats.get("p75", 0),
            "rsm2_p90": stats.get("p90", 0),
            "rsm2_max": stats.get("max", 0),
            "total_estimado": rsm2_adj * ac,
            "n_amostras": stats.get("n", 0),
            "source": "calibration-indices.json",
            "padrao_aplicado": padrao_key,
            "multiplicador": multiplier,
        }

    return result


def granular_via_gemma_subdisciplinas(similares: list[dict], macrogrupo: str,
                                        max_subs: int = 8) -> list[dict]:
    """Camada de granularização baseada na Fase 2 Gemma (qualitative.sub_disciplinas).

    Quando enriquecer_executivo() retorna pouco/nada (porque os items detalhados
    brutos não classificaram bem por keyword), esta função volta uma camada acima
    e usa as sub-disciplinas que o Gemma JÁ identificou na Fase 2 — esses dados
    estão classificados por macrogrupo (após normalização) e cada um vem com
    fontes (slugs) e itens_exemplo.

    Retorna lista pronta pra ir na aba do macrogrupo:
        [{descricao, fontes, freq, itens_exemplo}]
    """
    enriq = enriquecer_parametrico(similares)
    sub_por_mg = enriq.get("sub_disciplinas_por_mg", {})

    target_norm = normalize_macrogrupo(macrogrupo).lower()

    items = []
    for mg_key, subs in sub_por_mg.items():
        if mg_key.lower() != target_norm and macrogrupo.lower() not in mg_key.lower():
            continue
        for sd in subs[:max_subs]:
            items.append({
                "descricao": sd["sub"],
                "freq_projetos": sd["freq"],
                "fontes": sd["fontes"],
                "itens_exemplo": sd["itens_exemplo"],
                "source_layer": "gemma_sub_disciplinas",
            })

    return items


def bdi_encargos_observados(similares: list[dict]) -> list[dict]:
    """Retorna BDI/encargos vistos nos similares."""
    out = []
    for p in similares:
        slug = p["_slug"]
        for b in (p.get("qualitative") or {}).get("bdi_encargos", []):
            comp = str(b.get("componente", "")).strip()
            valor = str(b.get("valor_pct") or "").strip()
            if not comp:
                continue
            out.append({
                "componente": comp,
                "valor_pct": valor,
                "nota": str(b.get("nota", "")).strip(),
                "fonte": slug,
            })
    return out


if __name__ == "__main__":
    import sys
    ac = float(sys.argv[1]) if len(sys.argv) > 1 else 15000
    ur = int(sys.argv[2]) if len(sys.argv) > 2 else 90

    sims = projetos_similares(ac=ac, ur=ur, n=5)
    print(f"projetos similares (ac={ac}, ur={ur}): {[p['_slug'] for p in sims]}")
    print()

    enriq = enriquecer_parametrico(sims)
    print(f"sub-disciplinas agregadas por macrogrupo:")
    for mg, subs in enriq["sub_disciplinas_por_mg"].items():
        print(f"  [{mg}]")
        for s in subs[:5]:
            print(f"    - {s['sub']} (freq {s['freq']}/{enriq['n_similares']}, {len(s['itens_exemplo'])} itens exemplo)")
    print()

    prem = premissas_consolidadas(sims)
    print(f"premissas consolidadas ({len(prem)}):")
    for p in prem[:10]:
        print(f"  - [{p['area']}] {p['premissa'][:80]} (freq {p['freq']})")
    print()

    exec_estrut = enriquecer_executivo(sims, "Supraestrutura", top_n=10)
    print(f"top 10 itens de 'Supraestrutura' agregados:")
    for it in exec_estrut["itens_agregados"]:
        pu_m = it.get("pu_mediano") or 0
        print(f"  - {it['descricao'][:50]:50} {it['unidade']:6} PU R$ {pu_m:>10,.2f}  freq {it['freq_projetos']}")
