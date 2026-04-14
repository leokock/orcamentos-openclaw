#!/usr/bin/env python3
"""Phase 13 — Gera novos índices derivados a partir das Fases 1-12.

Calcula 30+ novos índices cross-projeto baseando-se em:
- itens-detalhados (Fase 1)
- sub-disciplinas Gemma (Fase 2)
- composições (Fase 4)
- curvas ABC (Fase 11)
- pus-agregados (Fase 10 — se disponível)

Saída: base/indices-derivados-v2.json
"""
from __future__ import annotations

import json
import re
import statistics
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
INDICES = BASE / "indices-executivo"
ITENS = BASE / "itens-detalhados"
COMP = BASE / "composicoes"
CURVA_DIR = BASE / "curvas-abc"
OUT = BASE / "indices-derivados-v2.json"


def load_all_indices() -> list[dict]:
    out = []
    for jp in sorted(INDICES.glob("*.json")):
        try:
            d = json.loads(jp.read_text(encoding="utf-8"))
            d["_slug"] = jp.stem
            out.append(d)
        except Exception:
            pass
    return out


def load_all_detalhados() -> dict[str, dict]:
    out = {}
    for jp in sorted(ITENS.glob("*.json")):
        try:
            out[jp.stem] = json.loads(jp.read_text(encoding="utf-8"))
        except Exception:
            pass
    return out


def stats(values: list[float]) -> dict:
    vs = [v for v in values if isinstance(v, (int, float)) and v > 0]
    if not vs:
        return None
    vs.sort()
    return {
        "n": len(vs),
        "min": round(vs[0], 4),
        "p10": round(vs[int(len(vs) * 0.1)], 4) if len(vs) > 10 else round(vs[0], 4),
        "p25": round(vs[int(len(vs) * 0.25)], 4) if len(vs) > 4 else round(vs[0], 4),
        "mediana": round(statistics.median(vs), 4),
        "media": round(statistics.mean(vs), 4),
        "p75": round(vs[int(len(vs) * 0.75)], 4) if len(vs) > 4 else round(vs[-1], 4),
        "p90": round(vs[int(len(vs) * 0.9)], 4) if len(vs) > 10 else round(vs[-1], 4),
        "max": round(vs[-1], 4),
        "cv": round(statistics.stdev(vs) / statistics.mean(vs), 3) if len(vs) > 1 and statistics.mean(vs) > 0 else 0,
    }


def find_item_contains(items: list[dict], keywords: list[str]) -> list[dict]:
    out = []
    for it in items:
        desc = (it.get("descricao") or "").lower()
        if any(kw in desc for kw in keywords):
            out.append(it)
    return out


def main():
    print("loading...")
    projetos = load_all_indices()
    detalhados = load_all_detalhados()
    print(f"  {len(projetos)} indices loaded, {len(detalhados)} detalhados loaded")

    derivados: dict = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_projetos": len(projetos),
        "indices": {},
    }

    print("\ncomputing derivados...")

    def add_index(name: str, desc: str, values_func):
        vals = []
        for p in projetos:
            try:
                v = values_func(p)
                if v is not None:
                    vals.append(v)
            except Exception:
                pass
        s = stats(vals)
        if s:
            s["nome"] = name
            s["descricao"] = desc
            derivados["indices"][name] = s
            print(f"  {name:<35} n={s['n']:>3} mediana={s['mediana']}")
            return s
        return None

    add_index("ac_por_ur", "Área Construída por Unidade Residencial",
              lambda p: (p.get("ac") / p.get("ur")) if p.get("ac") and p.get("ur") else None)

    add_index("custo_por_ur", "Custo total por unidade residencial",
              lambda p: (p.get("total") / p.get("ur")) if p.get("total") and p.get("ur") else None)

    add_index("rsm2_total", "R$/m² total do projeto",
              lambda p: p.get("rsm2"))

    def get_inst_breakdown(p, key):
        inst = p.get("instalacoes_breakdown") or {}
        ac = p.get("ac")
        if not ac:
            return None
        v = inst.get(key)
        if isinstance(v, (int, float)) and v > 0:
            return v / ac
        return None

    add_index("eletrica_rsm2", "Elétrica R$/m² AC",
              lambda p: get_inst_breakdown(p, "eletrica"))
    add_index("hidro_rsm2", "Hidrossanitário R$/m² AC",
              lambda p: get_inst_breakdown(p, "hidro") or get_inst_breakdown(p, "hidrossanitaria"))
    add_index("preventiva_rsm2", "PPCI R$/m² AC",
              lambda p: get_inst_breakdown(p, "preventiva") or get_inst_breakdown(p, "pci"))
    add_index("gas_rsm2", "GLP R$/m² AC",
              lambda p: get_inst_breakdown(p, "gas"))
    add_index("telecom_rsm2", "Telecom R$/m² AC",
              lambda p: get_inst_breakdown(p, "telecom"))

    def ratio_estrutural(p, key, other):
        ie = p.get("indices_estruturais") or {}
        a = ie.get(key)
        b = ie.get(other)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b > 0:
            return a / b
        return None

    add_index("concreto_por_aco_ratio", "Relação concreto (m³) / aço (kg)",
              lambda p: ratio_estrutural(p, "concreto_total_m3", "aco_total_kg"))

    add_index("forma_por_concreto_ratio", "Relação forma (m²) / concreto (m³)",
              lambda p: ratio_estrutural(p, "forma_total_m2", "concreto_total_m3"))

    def compute_item_stat(p, keywords, metric="pu"):
        """Encontra itens por keywords e retorna estatística."""
        slug = p["_slug"]
        det = detalhados.get(slug)
        if not det:
            return None
        vals = []
        for aba in det.get("abas", []):
            matched = find_item_contains(aba.get("itens", []), keywords)
            for it in matched:
                v = it.get(metric)
                if isinstance(v, (int, float)) and v > 0:
                    vals.append(v)
        if not vals:
            return None
        return statistics.median(vals)

    add_index("pu_concreto_usinado_mediano", "PU mediano Concreto Usinado (R$/m³)",
              lambda p: compute_item_stat(p, ["concreto usinado", "concreto fck"]))
    add_index("pu_aco_ca50_mediano", "PU mediano Aço CA-50 (R$/kg)",
              lambda p: compute_item_stat(p, ["aço ca-50", "aco ca-50", "aço ca50"]))
    add_index("pu_forma_madeira_mediano", "PU mediano Forma de madeira (R$/m²)",
              lambda p: compute_item_stat(p, ["forma", "fôrma"]))
    add_index("pu_bloco_ceramico_mediano", "PU mediano Bloco cerâmico",
              lambda p: compute_item_stat(p, ["bloco cer", "bloco ceramico"]))
    add_index("pu_impermeabilizacao_mediano", "PU mediano Impermeabilização",
              lambda p: compute_item_stat(p, ["impermea", "manta asfal"]))
    add_index("pu_porcelanato_mediano", "PU mediano Porcelanato",
              lambda p: compute_item_stat(p, ["porcelanato"]))
    add_index("pu_pintura_acrilica_mediano", "PU mediano Pintura acrílica",
              lambda p: compute_item_stat(p, ["pintura", "tinta acril"]))

    def compute_sum_by_keyword(p, keywords):
        slug = p["_slug"]
        det = detalhados.get(slug)
        ac = p.get("ac")
        if not det or not ac:
            return None
        total = 0
        for aba in det.get("abas", []):
            for it in find_item_contains(aba.get("itens", []), keywords):
                t = it.get("total")
                if isinstance(t, (int, float)) and t > 0:
                    total += t
        return total / ac if total > 0 else None

    add_index("custo_concreto_rsm2", "Custo total Concreto R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["concreto usinado", "concreto fck", "concreto bomb"]))
    add_index("custo_aco_rsm2", "Custo total Aço R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["aço ca", "aco ca", "armação"]))
    add_index("custo_forma_rsm2", "Custo total Forma R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["forma", "fôrma", "forma madeira"]))
    add_index("custo_escoramento_rsm2", "Custo total Escoramento R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["escoramento"]))
    add_index("custo_impermeabilizacao_rsm2", "Custo total Impermeabilização R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["impermea"]))
    add_index("custo_elevador_rsm2", "Custo total Elevadores R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["elevador"]))
    add_index("custo_piscina_rsm2", "Custo total Piscina R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["piscina"]))
    add_index("custo_pintura_rsm2", "Custo total Pintura R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["pintura", "tinta"]))
    add_index("custo_esquadrias_rsm2", "Custo total Esquadrias R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["esquadri", "porta de", "janela"]))
    add_index("custo_loucas_rsm2", "Custo total Louças e Metais R$/m² AC",
              lambda p: compute_sum_by_keyword(p, ["louça", "torneira", "bacia", "cuba"]))

    def sum_ci(p):
        ci = p.get("ci_detalhado") or {}
        ac = p.get("ac")
        if not ac:
            return None
        total = sum(v for v in ci.values() if isinstance(v, (int, float)))
        return total / ac if total > 0 else None

    add_index("ci_total_rsm2", "Custos Indiretos total R$/m² AC",
              sum_ci)

    def distribuicao_composicao(p, key):
        slug = p["_slug"]
        comp_path = COMP / f"{slug}.json"
        if not comp_path.exists():
            return None
        try:
            d = json.loads(comp_path.read_text(encoding="utf-8"))
            v = (d.get("parsed") or {}).get("distribuicao", {}).get(key)
            if isinstance(v, (int, float)) and v > 0:
                return v
        except Exception:
            pass
        return None

    add_index("material_pct_composicao", "% Material da composição unitária",
              lambda p: distribuicao_composicao(p, "material_pct"))
    add_index("mao_obra_pct_composicao", "% Mão-de-obra da composição unitária",
              lambda p: distribuicao_composicao(p, "mao_obra_pct"))
    add_index("equipamento_pct_composicao", "% Equipamento da composição unitária",
              lambda p: distribuicao_composicao(p, "equipamento_pct"))

    def curva_abc_ratio(p):
        slug = p["_slug"]
        cp = CURVA_DIR / f"{slug}.json"
        if not cp.exists():
            return None
        try:
            d = json.loads(cp.read_text(encoding="utf-8"))
            n = d.get("n_itens") or 0
            na = d.get("n_a") or 0
            return (na / n * 100) if n > 0 else None
        except Exception:
            pass
        return None

    add_index("curva_abc_a_pct", "% de itens na classe A da curva ABC",
              curva_abc_ratio)

    print(f"\n{len(derivados['indices'])} indices derivados calculados")

    OUT.write_text(json.dumps(derivados, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"saved: {OUT}")


if __name__ == "__main__":
    main()
