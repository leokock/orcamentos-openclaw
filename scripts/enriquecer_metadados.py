#!/usr/bin/env python3
"""Fase 1b — Enriquece metadados da Fase 1 com dados de outras fontes.

Consolida:
- base/metadados-projeto/*.json (Fase 1 via Gemma)
- base/indices-executivo/*.json (AC, UR, total, macrogrupos, estruturais)
- base/padroes-classificados-consolidado.json (padrão canônico 126/126)
- base/indicadores-produto/*.json (indicadores físicos)
- inferência de cidade/UF via slug + mapa manual

Saída: base/projetos-enriquecidos.json (1 arquivo consolidado)
       base/projetos-enriquecidos/{slug}.json (1 por projeto)
"""
from __future__ import annotations

import json
import unicodedata
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
METADADOS_DIR = BASE / "metadados-projeto"
IDX_DIR = BASE / "indices-executivo"
PROD_DIR = BASE / "indicadores-produto"
PAD_FILE = BASE / "padroes-classificados-consolidado.json"
OUT_JSON = BASE / "projetos-enriquecidos.json"
OUT_DIR = BASE / "projetos-enriquecidos"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def norm(s):
    s = str(s or "").lower().replace("_", "-")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


# ─── Mapa manual: slug → (cidade, uf) ─────────────────────────────
# Baseado em clientes conhecidos da Cartesian (SC+RS+PR+SP+RJ+MG+GO)
MAPA_CIDADES = {
    # Clientes com múltiplos projetos — consolidado do conhecimento Cartesian
    "nova-empreendimentos-": ("Florianópolis", "SC"),  # Nova tem base em Floripa
    "amalfi-": ("Bombinhas", "SC"),  # Amalfi é de Bombinhas
    "paludo-volo-": ("Gramado", "RS"),  # Paludo Volo
    "paludo-barbados": ("Bombinhas", "SC"),
    "paludo-nassau": ("Bombinhas", "SC"),
    "paludo-urban-life": ("Gramado", "RS"),
    "brava-construtora-": ("Balneário Camboriú", "SC"),
    "cn-brava-": ("Balneário Camboriú", "SC"),
    "arthen-arboris": ("Morretes", "PR"),
    "santa-maria-": ("Chapecó", "SC"),
    "pass-e-": ("Itajaí", "SC"),  # Pass-e é de Itajaí
    "thozen-electra": ("Balneário Camboriú", "SC"),
    "thozen-mirador-": ("Itapema", "SC"),
    "mussi-empreendimentos-": ("Itajaí", "SC"),
    "chiquetti-e-dalvesco-": ("Itajaí", "SC"),
    "ck-": ("Balneário Camboriú", "SC"),
    "f-nogueira-": ("Florianópolis", "SC"),
    "grandezza-gran-": ("Balneário Piçarras", "SC"),
    "grupo-duo-": ("Itajaí", "SC"),
    "mendes-empreendimentos-": ("Itapema", "SC"),
    "mtf-m-": ("Itajaí", "SC"),
    "muller-empreendimentos-": ("Balneário Camboriú", "SC"),
    "neuhaus-": ("Florianópolis", "SC"),
    "viva4-": ("Itajaí", "SC"),
    "blue-heaven-": ("Florianópolis", "SC"),
    "brasin-": ("Itajaí", "SC"),
    "adore-": ("Balneário Camboriú", "SC"),
    "fonseca-empreendimentos-": ("Florianópolis", "SC"),
    "fg-": ("Florianópolis", "SC"),
    "homeset-": ("Florianópolis", "SC"),
    "all-": ("Florianópolis", "SC"),
    "terrassa-": ("Itajaí", "SC"),
    "etr-zion-": ("Porto Belo", "SC"),
    "gdi-": ("Itajaí", "SC"),
    "bellei-salvador-": ("Florianópolis", "SC"),  # Bellei tem projetos SC
    "hacasa-": ("Florianópolis", "SC"),
    "colline-de-france-": ("Gramado", "RS"),
    "inbrasul-": ("Florianópolis", "SC"),
    "xpcon-": ("Balneário Camboriú", "SC"),
    "pavcor": ("Chapecó", "SC"),
    "santo-andre-": ("Camboriú", "SC"),
    "estilo-condominios-": ("Balneário Camboriú", "SC"),
    "lotisa-": ("Itajaí", "SC"),
    "libra-concept-": ("Florianópolis", "SC"),
    "h-empreendimentos-": ("Balneário Camboriú", "SC"),
    "as-ramos-": ("Balneário Camboriú", "SC"),
    "be-brave-": ("Florianópolis", "SC"),
    "nova-empreendimentos-domus": ("Florianópolis", "SC"),
    "pavcor": ("Chapecó", "SC"),
    # Outros clientes menos frequentes
    "ajr-spot-one": ("São Paulo", "SP"),
    "santa-maria-feat": ("Chapecó", "SC"),
    "santa-maria-unimed": ("Chapecó", "SC"),
    "santa-maria-z": ("Chapecó", "SC"),
    "by-seasons-": ("Florianópolis", "SC"),
    "beco-castelo-": ("Balneário Camboriú", "SC"),
    "mabrem-": ("Itajaí", "SC"),
    "caledonia-": ("Florianópolis", "SC"),
    "colline-de-france-colline-de-france": ("Gramado", "RS"),
    "all-acacias-": ("Florianópolis", "SC"),
    "all-lago-di-garda": ("Florianópolis", "SC"),
    "arv-ingleses-": ("Florianópolis", "SC"),
    "fg-blue-coast": ("Florianópolis", "SC"),
    "fg-scenarium": ("Florianópolis", "SC"),
    "placon-arminio-tavares": ("Florianópolis", "SC"),
    "san-fellice": ("Bombinhas", "SC"),
    "arminio-tavares": ("Florianópolis", "SC"),
    "cambert-now": ("Itajaí", "SC"),
    "bci-alipio": ("Florianópolis", "SC"),
    "nf-itajai": ("Itajaí", "SC"),
    "ctn-alf-sfl": ("Bombinhas", "SC"),
    "tak": ("Florianópolis", "SC"),
    "alto-ribeirao": ("Florianópolis", "SC"),
    "gessele-elisabeth": ("Florianópolis", "SC"),
    "fg-senna": ("Florianópolis", "SC"),
    "senna-tower": ("Florianópolis", "SC"),
    # Adicionados após identificação de faltantes
    "cambert-": ("Balneário Camboriú", "SC"),
    "dimas-": ("Florianópolis", "SC"),
    "eze-": ("Balneário Camboriú", "SC"),
    "holze-": ("Florianópolis", "SC"),
    "indepy-": ("São Paulo", "SP"),
    "kirchner-": ("Florianópolis", "SC"),
    "lumis-": ("Florianópolis", "SC"),
    "macom-": ("São Paulo", "SP"),
    "mz-": ("Florianópolis", "SC"),
    "nm-empreendimentos": ("Florianópolis", "SC"),
    "parkside-": ("Florianópolis", "SC"),
    "rosner-": ("Balneário Camboriú", "SC"),
    "sak-": ("Florianópolis", "SC"),
    "somauma-": ("Florianópolis", "SC"),
    "wf-": ("Balneário Camboriú", "SC"),
    "carraro-": ("Florianópolis", "SC"),
    "cln-": ("Balneário Camboriú", "SC"),
    "cota-365": ("Florianópolis", "SC"),
}


def inferir_cidade(slug: str) -> tuple[str | None, str | None]:
    """Infere (cidade, uf) de um slug via mapa manual (longest-prefix match)."""
    s = norm(slug)
    # Longest prefix match
    matches = sorted((k for k in MAPA_CIDADES if s.startswith(norm(k))),
                     key=len, reverse=True)
    if matches:
        cidade, uf = MAPA_CIDADES[matches[0]]
        return cidade, uf
    return None, None


# ─── CUB regional (aproximação) ───────────────────────────────────
CUB_REGIAO = {
    ("SC", "Florianópolis"): "SC-Floripa",
    ("SC", "Balneário Camboriú"): "SC-BC",
    ("SC", "Balneário Piçarras"): "SC-Litoral-Norte",
    ("SC", "Bombinhas"): "SC-Litoral-Norte",
    ("SC", "Itajaí"): "SC-Vale-Itajai",
    ("SC", "Itapema"): "SC-Litoral-Norte",
    ("SC", "Porto Belo"): "SC-Litoral-Norte",
    ("SC", "Penha"): "SC-Litoral-Norte",
    ("SC", "Camboriú"): "SC-BC",
    ("SC", "Chapecó"): "SC-Oeste",
    ("SC", "Blumenau"): "SC-Vale-Itajai",
    ("RS", "Gramado"): "RS-Serra",
    ("RS", "Caxias do Sul"): "RS-Serra",
    ("RS", "Porto Alegre"): "RS-Capital",
    ("PR", "Morretes"): "PR-Litoral",
    ("PR", "Curitiba"): "PR-Capital",
    ("SP", "São Paulo"): "SP-Capital",
    ("RJ", "Rio de Janeiro"): "RJ-Capital",
}


def cub_regiao(cidade, uf):
    return CUB_REGIAO.get((uf, cidade), f"{uf}-Outros" if uf else None)


def _load(p: Path):
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    print("Carregando fontes...", flush=True)
    # Padroes
    pad_data = _load(PAD_FILE)
    pad_map = {p["projeto"]: p for p in pad_data.get("projetos", [])}

    # Metadados Gemma
    meta_gemma = {}
    for f in METADADOS_DIR.glob("*.json"):
        d = _load(f)
        if d.get("slug"):
            meta_gemma[d["slug"]] = d.get("metadados", {})

    # Indices executivo
    ix_data = {}
    for f in IDX_DIR.glob("*.json"):
        d = _load(f)
        slug = d.get("projeto") or f.stem
        ix_data[slug] = d

    # Indicadores produto
    prod_data = {}
    for f in PROD_DIR.glob("*.json"):
        d = _load(f)
        slug = d.get("slug") or f.stem
        prod_data[slug] = d

    # Consolida
    all_slugs = sorted(set(list(ix_data.keys()) + list(meta_gemma.keys())))
    print(f"Slugs únicos: {len(all_slugs)}", flush=True)

    enriquecidos = []
    for slug in all_slugs:
        pi = pad_map.get(slug, {})
        meta = meta_gemma.get(slug, {}) or {}
        ix = ix_data.get(slug, {}) or {}
        prod = prod_data.get(slug, {}) or {}
        est = ix.get("indices_estruturais") or {}

        # Localização: prioriza Gemma, fallback mapa manual
        cidade = meta.get("cidade") or None
        uf = meta.get("uf") or None
        if not cidade or not uf:
            c2, u2 = inferir_cidade(slug)
            cidade = cidade or c2
            uf = uf or u2

        # Padrão (100% coberto)
        padrao = pi.get("padrao") or meta.get("padrao_declarado") or "desconhecido"

        # Escala
        ac = ix.get("ac") or prod.get("ac_m2") or meta.get("area_construida_m2")
        ur = ix.get("ur") or prod.get("ur") or meta.get("n_unidades_residenciais")
        total = ix.get("total") or 0
        rsm2 = ix.get("rsm2") or 0

        # Estrutural (prefere indices-executivo)
        concreto_m3_m2 = est.get("concreto_m3_por_m2_ac") or meta.get("concreto_m3_por_m2_ac")
        taxa_aco = est.get("aco_kg_por_m3_concreto") or meta.get("taxa_aco")
        forma_m2_m2 = est.get("forma_m2_por_m2_ac")
        fck = est.get("fck_predominante") or meta.get("fck_predominante_mpa")
        sist_est = meta.get("sistema_estrutural")
        if est.get("tipo_estaca"):
            meta["tipo_estaca"] = est.get("tipo_estaca")

        # ⚠ IMPORTANTE: Gemma tende a marcar False por omissão (não-menção != ausência).
        # Pra evitar viés, usamos None quando extração foi parcial (poucas fontes).
        # Booleans só são confiáveis se True (aí foi menção explícita).
        n_fontes_meta = len(meta_gemma.get(slug, {})) if slug in meta_gemma else 0

        def bool_conservador(campo):
            """Retorna True se Gemma disse True, None caso contrário (não confio em False)."""
            v = meta.get(campo)
            return v if v is True else None

        # Escopo/diferenciais
        record = {
            "slug": slug,
            "cliente_inferido": slug.split("-")[0],
            # Classificação
            "padrao": padrao,
            "tipologia_gemma": meta.get("tipologia"),
            # Localização
            "cidade": cidade,
            "uf": uf,
            "cub_regiao": cub_regiao(cidade, uf),
            # Escala
            "ac_m2": ac,
            "ur": ur,
            "total_rs": total,
            "rsm2": rsm2,
            # Estrutural
            "concreto_m3_m2_ac": concreto_m3_m2,
            "taxa_aco_kg_m3": taxa_aco,
            "forma_m2_m2_ac": forma_m2_m2,
            "fck_predominante": fck,
            "sistema_estrutural": sist_est,
            "n_pavimentos_total": meta.get("n_pavimentos_total"),
            "n_pavimentos_garagem": meta.get("n_pavimentos_garagem"),
            "n_pavimentos_tipo": meta.get("n_pavimentos_tipo"),
            "n_torres": meta.get("n_torres"),
            "n_elevadores": meta.get("n_elevadores"),
            "n_tipologias_apto": meta.get("n_tipologias_apto"),
            "area_privativa_tipo_m2": meta.get("area_privativa_tipo_m2"),
            # Diferenciais (conservador: só True declarado vale; False tratado como None)
            "tem_pele_vidro": bool_conservador("tem_pele_de_vidro"),
            "tem_piscina": bool_conservador("tem_piscina"),
            "tem_gerador": bool_conservador("tem_gerador"),
            "tem_spda": bool_conservador("tem_spda"),
            "tem_climatizacao_central": bool_conservador("tem_climatizacao_central"),
            "tem_churrasqueira_apto": bool_conservador("tem_churrasqueira_apto"),
            "tem_subsolo": bool_conservador("tem_subsolo"),
            # Meta
            "tem_metadados_gemma": slug in meta_gemma,
            "observacoes_gemma": meta.get("observacoes_relevantes"),
            "cub_referencia_memorial": meta.get("cub_referencia"),
            "data_memorial": meta.get("data_memorial_iso"),
        }
        enriquecidos.append(record)

        # Salva individual
        (OUT_DIR / f"{slug}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")

    # Stats
    from collections import Counter
    stats = {
        "n_projetos": len(enriquecidos),
        "cobertura": {},
    }
    campos = ["padrao", "cidade", "uf", "cub_regiao", "ac_m2", "ur", "total_rs",
              "concreto_m3_m2_ac", "taxa_aco_kg_m3", "sistema_estrutural",
              "n_pavimentos_total", "tem_metadados_gemma", "tipologia_gemma",
              "tem_pele_vidro", "tem_gerador", "tem_piscina"]
    for c in campos:
        n = sum(1 for r in enriquecidos if r.get(c) not in (None, "", 0, "desconhecido"))
        stats["cobertura"][c] = f"{n}/{len(enriquecidos)} ({n/len(enriquecidos)*100:.0f}%)"

    # Distribuição de UF
    ufs = Counter(r["uf"] for r in enriquecidos if r.get("uf"))
    stats["por_uf"] = dict(ufs.most_common())

    # Distribuição por cub_regiao
    cubs = Counter(r["cub_regiao"] for r in enriquecidos if r.get("cub_regiao"))
    stats["por_cub_regiao"] = dict(cubs.most_common())

    # Distribuição padrão
    stats["por_padrao"] = dict(Counter(r["padrao"] for r in enriquecidos))

    # Grava consolidado
    out = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "stats": stats,
        "projetos": enriquecidos,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nSalvo: {OUT_JSON}", flush=True)
    print(f"\n=== COBERTURA ===", flush=True)
    for c, v in stats["cobertura"].items():
        print(f"  {c:<30} {v}", flush=True)
    print(f"\n=== POR UF ===", flush=True)
    for uf, n in stats["por_uf"].items():
        print(f"  {uf}: {n}", flush=True)
    print(f"\n=== POR CUB REGIAO ===", flush=True)
    for cub, n in stats["por_cub_regiao"].items():
        print(f"  {cub}: {n}", flush=True)
    print(f"\n=== POR PADRAO ===", flush=True)
    for pad, n in stats["por_padrao"].items():
        print(f"  {pad}: {n}", flush=True)


if __name__ == "__main__":
    main()
