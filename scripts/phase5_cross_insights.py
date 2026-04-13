#!/usr/bin/env python3
"""Phase 5 — Cross-project benchmarking e inteligência de base.

Roda Gemma sobre AGREGADOS dos 126 projetos da base (não 1 chamada por
projeto), pra descobrir padrões, outliers, famílias, novos índices, lacunas.

5 perguntas, cada uma é uma chamada Gemma separada com input ~6-8k chars:
1. Famílias de projetos por similaridade
2. Outliers estruturais (quantitativos anômalos)
3. Padrões de observações repetidas (premissas comuns)
4. Novos índices derivados sugeridos
5. Lacunas de cobertura na base

Saída: base/cross-insights/{familias,outliers,padroes_comuns,indices_sugeridos,lacunas}.json
       base/cross-insights/cross-insights-report.md (consolidado)
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
INDICES = BASE / "indices-executivo"
ITENS = BASE / "itens-detalhados"
SUB = BASE / "sub-disciplinas"
PREMISSAS = BASE / "premissas"
CROSS_DIR = BASE / "cross-insights"
CROSS_DIR.mkdir(parents=True, exist_ok=True)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"
NUM_CTX = 16384
TIMEOUT_S = 600


def call_ollama(prompt: str) -> tuple[str, float]:
    payload = {
        "model": MODEL, "prompt": prompt, "stream": False,
        "options": {"num_ctx": NUM_CTX, "temperature": 0.3, "repeat_penalty": 1.2},
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
    r.raise_for_status()
    return r.json().get("response", ""), time.time() - t0


JSON_RE = re.compile(r"\{[\s\S]*\}|\[[\s\S]*\]")


def _fix_bad_escapes(s: str) -> str:
    return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', s)


def _balance_braces(s: str) -> str:
    o, c = s.count("{"), s.count("}")
    if c > o:
        for _ in range(c - o):
            i = s.rfind("}")
            if i < 0:
                break
            s = s[:i] + s[i + 1:]
    elif o > c:
        s = s + "}" * (o - c)
    return s


def extract_json(raw: str):
    s = raw.strip()
    s = re.sub(r"^```(?:json)?", "", s).strip()
    s = re.sub(r"```$", "", s).strip()
    m = JSON_RE.search(s)
    if not m:
        return None
    cand = m.group(0)
    for c in [cand, _fix_bad_escapes(cand), _balance_braces(_fix_bad_escapes(cand))]:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def load_all() -> list[dict]:
    out = []
    for jp in sorted(INDICES.glob("*.json")):
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
            d["_slug"] = jp.stem
            out.append(d)
        except Exception:
            continue
    return out


def montar_dossie_compacto(projetos: list[dict], top_n: int = 30) -> str:
    """Monta um dossiê compacto agregado dos top_n projetos mais ricos."""
    enriched = []
    for p in projetos:
        qual = p.get("qualitative") or {}
        n_sub = len(qual.get("sub_disciplinas") or [])
        n_obs = len(qual.get("observacoes_orcamentista") or [])
        n_prem = len(qual.get("premissas_tecnicas") or [])
        ac = p.get("ac") or 0
        if ac < 1:
            continue
        enriched.append({
            "slug": p["_slug"],
            "ac": ac,
            "ur": p.get("ur"),
            "rsm2": p.get("rsm2"),
            "total": p.get("total"),
            "n_sub": n_sub,
            "n_obs": n_obs,
            "n_prem": n_prem,
            "qual": qual,
            "richness": n_sub * 2 + n_obs + n_prem * 2,
        })

    enriched.sort(key=lambda x: -x["richness"])
    top = enriched[:top_n]

    lines = [f"# Base Cartesian — Top {len(top)} projetos por riqueza qualitativa", ""]
    lines.append("Cada projeto: AC, UR, R$/m², top sub-disciplinas, top observações.")
    lines.append("")

    for p in top:
        lines.append(f"## {p['slug']}")
        lines.append(f"AC={p['ac']:.0f}m² UR={p['ur'] or '?'} R$/m²={p['rsm2'] or '?'}")
        subs = p["qual"].get("sub_disciplinas") or []
        if subs:
            sample_subs = []
            for sd in subs[:8]:
                mg = sd.get("macrogrupo", "")
                sub = sd.get("sub_disciplina", "")
                if mg and sub:
                    sample_subs.append(f"{mg}>{sub}")
            if sample_subs:
                lines.append(f"sub: {' | '.join(sample_subs)}")

        obs = p["qual"].get("observacoes_orcamentista") or []
        if obs:
            sample_obs = [f"[{o.get('categoria', '?')}]{str(o.get('observacao', ''))[:50]}"
                          for o in obs[:4]]
            lines.append(f"obs: {' | '.join(sample_obs)}")

        prem = p["qual"].get("premissas_tecnicas") or []
        if prem:
            sample_prem = [f"[{pr.get('area', '?')}]{str(pr.get('premissa', ''))[:50]}"
                           for pr in prem[:3]]
            lines.append(f"prem: {' | '.join(sample_prem)}")
        lines.append("")

    text = "\n".join(lines)
    if len(text) > 8000:
        text = text[:8000] + "\n…[trunc]"
    return text


def calcular_estatisticas_estruturais(projetos: list[dict]) -> str:
    """Estatísticas estruturais e indices_consumo, pra outliers."""
    import statistics
    rows = []
    for p in projetos:
        ac = p.get("ac") or 0
        ie = p.get("indices_estruturais") or {}
        if not ac or not ie:
            continue
        rows.append({
            "slug": p["_slug"],
            "ac": ac,
            "concreto_m3_m2": ie.get("concreto_m3_por_m2_ac"),
            "aco_kg_m3": ie.get("aco_kg_por_m3_concreto"),
            "forma_m2_m2": ie.get("forma_m2_por_m2_ac"),
        })
    if not rows:
        return ""

    lines = ["# Indices estruturais (todos com dados)", ""]
    lines.append("slug | ac | concreto_m3/m2 | aco_kg/m3 | forma_m2/m2")
    for r in rows[:60]:
        c = r['concreto_m3_m2']
        a = r['aco_kg_m3']
        f = r['forma_m2_m2']
        lines.append(f"{r['slug']} | {r['ac']:.0f} | {c if c else '-'} | {a if a else '-'} | {f if f else '-'}")
    return "\n".join(lines)[:6000]


def pergunta(name: str, prompt_specific: str, dossie: str) -> dict:
    print(f"\n=== Pergunta {name} ===")
    full = prompt_specific + "\n\n---\n\n" + dossie
    print(f"  prompt chars: {len(full)}")
    raw, dur = call_ollama(full)
    print(f"  raw chars: {len(raw)}  duration: {dur:.1f}s")
    parsed = extract_json(raw)
    if not parsed:
        print(f"  parse failed; raw sample: {raw[:200]}")
        return {"name": name, "status": "parse_failed", "raw": raw, "duration": dur}
    return {"name": name, "status": "done", "parsed": parsed, "raw": raw, "duration": dur}


def main():
    print("Loading base...")
    projetos = load_all()
    print(f"  loaded {len(projetos)} projetos")

    dossie = montar_dossie_compacto(projetos, top_n=25)
    print(f"  dossie: {len(dossie)} chars")

    estruturais = calcular_estatisticas_estruturais(projetos)
    print(f"  estruturais: {len(estruturais)} chars")

    results = {}

    P1 = ("""Analise o dossiê de projetos da Cartesian abaixo. Agrupe os projetos em FAMÍLIAS por similaridade (AC, UR, padrão, perfil de sub-disciplinas).

Retorne APENAS um JSON válido (sem markdown) no formato:
{
  "familias": [
    {
      "nome_familia": "string",
      "criterios": "string descrevendo o que define a família",
      "projetos_exemplares": ["slug1", "slug2", "slug3"],
      "ac_range": "min-max m²",
      "n_estimado_total": 10
    }
  ]
}

REGRAS:
- Entre 5 e 10 famílias
- Use apenas slugs que aparecem no dossiê
- Critérios devem ser claros e quantificáveis""")

    P2 = ("""Analise os índices estruturais abaixo (concreto m³/m² AC, aço kg/m³ concreto, forma m²/m² AC).

Identifique OUTLIERS — projetos com valores muito acima ou muito abaixo da mediana esperada (concreto típico 0.18-0.30 m³/m², aço típico 60-130 kg/m³, forma típica 1.4-2.0 m²/m²).

Retorne APENAS JSON válido:
{
  "outliers": [
    {
      "slug": "string",
      "campo": "concreto_m3_m2|aco_kg_m3|forma_m2_m2",
      "valor": 0.0,
      "tipo": "muito_alto|muito_baixo",
      "causa_provavel": "string"
    }
  ]
}

Use só slugs que aparecem nos dados. Limite a 15 outliers mais relevantes.""")

    P3 = ("""Analise as observações de orçamentista no dossiê. Identifique TEXTOS QUE SE REPETEM em vários projetos (premissas/observações comuns que apareceriam como padrão Cartesian).

Retorne APENAS JSON válido:
{
  "padroes_comuns": [
    {
      "padrao": "string descrevendo o padrão",
      "exemplos": ["frase1", "frase2"],
      "frequencia_estimada": "alta|media|baixa",
      "categoria": "premissa|justificativa|revisao|alerta"
    }
  ]
}

Liste 10-15 padrões. Use textos que aparecem literalmente no dossiê.""")

    P4 = ("""Olhando o dossiê dos projetos da Cartesian (sub-disciplinas + valores), sugira NOVOS ÍNDICES DERIVADOS que poderiam ser calculados a partir dos dados existentes — índices que agregariam valor mas que ainda não estão calculados (ex: "custo de escoramento por m² de laje protendida").

Retorne APENAS JSON válido:
{
  "indices_sugeridos": [
    {
      "nome_indice": "string",
      "formula": "string descrevendo cálculo",
      "macrogrupo_relacionado": "string",
      "valor_potencial": "string explicando por que valeria a pena calcular",
      "n_projetos_disponiveis": 10
    }
  ]
}

Sugira 8-12 índices novos.""")

    P5 = ("""Olhando o dossiê, identifique LACUNAS DE COBERTURA — dimensões/campos que faltam em vários projetos (ex: "premissas técnicas faltando em 30% dos projetos") ou áreas pouco representadas (ex: "poucos projetos com piscina aquecida").

Retorne APENAS JSON válido:
{
  "lacunas": [
    {
      "lacuna": "string",
      "impacto": "alto|medio|baixo",
      "n_projetos_afetados": 10,
      "como_resolver": "string"
    }
  ]
}

Liste 8-12 lacunas com prioridade por impacto.""")

    perguntas = [
        ("familias", P1, dossie),
        ("outliers", P2, estruturais),
        ("padroes_comuns", P3, dossie),
        ("indices_sugeridos", P4, dossie),
        ("lacunas", P5, dossie),
    ]

    log = []
    for name, prompt, ctx in perguntas:
        try:
            r = pergunta(name, prompt, ctx)
        except Exception as e:
            r = {"name": name, "status": "error", "error": f"{type(e).__name__}: {e}"}
        results[name] = r

        out_path = CROSS_DIR / f"{name}.json"
        out_path.write_text(json.dumps(r, indent=2, ensure_ascii=False), encoding="utf-8")
        log.append({"name": name, "status": r.get("status", "?"), "duration": r.get("duration", 0)})

    print("\n=== Summary ===")
    for l in log:
        print(f"  {l['name']:<22} {l['status']:<14} {l.get('duration', 0):>6.1f}s")

    relatorio = []
    relatorio.append(f"# Cross-Project Insights — Phase 5")
    relatorio.append(f"_Gerado em {datetime.now().isoformat(timespec='seconds')}_")
    relatorio.append(f"")
    relatorio.append(f"Análise de **{len(projetos)} projetos** da base Cartesian via Gemma local.")
    relatorio.append(f"5 perguntas independentes, ~{sum(l.get('duration', 0) for l in log):.0f}s total.")
    relatorio.append(f"")

    for name, label in [
        ("familias", "Famílias de projetos por similaridade"),
        ("outliers", "Outliers estruturais"),
        ("padroes_comuns", "Padrões de observações repetidas"),
        ("indices_sugeridos", "Novos índices derivados sugeridos"),
        ("lacunas", "Lacunas de cobertura na base"),
    ]:
        relatorio.append(f"## {label}")
        relatorio.append(f"")
        r = results.get(name) or {}
        if r.get("status") != "done":
            relatorio.append(f"_(falhou: {r.get('status', '?')})_")
            relatorio.append("")
            continue
        parsed = r.get("parsed") or {}
        rows = []
        for k, v in parsed.items():
            if isinstance(v, list):
                rows = v
                break
        if not rows:
            relatorio.append("_(sem dados)_")
            relatorio.append("")
            continue
        for i, item in enumerate(rows[:15], 1):
            relatorio.append(f"### {i}.")
            for k, v in item.items():
                if isinstance(v, list):
                    v_str = ", ".join(str(x)[:50] for x in v[:5])
                else:
                    v_str = str(v)[:200]
                relatorio.append(f"- **{k}:** {v_str}")
            relatorio.append("")

    out_md = CROSS_DIR / "cross-insights-report.md"
    out_md.write_text("\n".join(relatorio), encoding="utf-8")
    print(f"\nrelatorio: {out_md}")


if __name__ == "__main__":
    main()
