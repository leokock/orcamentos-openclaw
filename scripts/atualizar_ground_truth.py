#!/usr/bin/env python3
"""Fase 12b — Atualiza projetos-enriquecidos com dados REAIS das entregas.

Sobrescreve cidade/UF/data_base/cub_regiao quando entrega tem ground truth.
Mantém inferência quando não tem.

Gera relatório de divergências (inferência vs ground truth).

Output:
- base/projetos-enriquecidos/{slug}.json atualizados
- base/projetos-enriquecidos.json consolidado atualizado
- base/divergencias-ground-truth.json
- analises-cross-projeto/FASE-12-GROUND-TRUTH-RELATORIO.md
"""
from __future__ import annotations

import json
import unicodedata
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
GT_DIR = BASE / "entregas-ground-truth"
ENR_DIR = BASE / "projetos-enriquecidos"
ENR_FILE = BASE / "projetos-enriquecidos.json"
DIV_JSON = BASE / "divergencias-ground-truth.json"
OUT_MD = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "FASE-12-GROUND-TRUTH-RELATORIO.md"


def norm(s):
    s = str(s or "").lower().strip()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


# Mapeamento de cidade normalizada → (nome_canonico, uf, cub_regiao)
CIDADE_CANONICA = {
    "florianopolis": ("Florianópolis", "SC", "SC-Floripa"),
    "floripa": ("Florianópolis", "SC", "SC-Floripa"),
    "balneario camboriu": ("Balneário Camboriú", "SC", "SC-BC"),
    "camboriu": ("Camboriú", "SC", "SC-BC"),
    "balneario picarras": ("Balneário Piçarras", "SC", "SC-Litoral-Norte"),
    "picarras": ("Balneário Piçarras", "SC", "SC-Litoral-Norte"),
    "bombinhas": ("Bombinhas", "SC", "SC-Litoral-Norte"),
    "itajai": ("Itajaí", "SC", "SC-Vale-Itajai"),
    "itapema": ("Itapema", "SC", "SC-Litoral-Norte"),
    "porto belo": ("Porto Belo", "SC", "SC-Litoral-Norte"),
    "penha": ("Penha", "SC", "SC-Litoral-Norte"),
    "chapeco": ("Chapecó", "SC", "SC-Oeste"),
    "blumenau": ("Blumenau", "SC", "SC-Vale-Itajai"),
    "brusque": ("Brusque", "SC", "SC-Vale-Itajai"),
    "joinville": ("Joinville", "SC", "SC-Norte"),
    "navegantes": ("Navegantes", "SC", "SC-Vale-Itajai"),
    "tubarao": ("Tubarão", "SC", "SC-Sul"),
    "criciuma": ("Criciúma", "SC", "SC-Sul"),
    "gramado": ("Gramado", "RS", "RS-Serra"),
    "canela": ("Canela", "RS", "RS-Serra"),
    "caxias do sul": ("Caxias do Sul", "RS", "RS-Serra"),
    "porto alegre": ("Porto Alegre", "RS", "RS-Capital"),
    "morretes": ("Morretes", "PR", "PR-Litoral"),
    "curitiba": ("Curitiba", "PR", "PR-Capital"),
    "sao paulo": ("São Paulo", "SP", "SP-Capital"),
    "santos": ("Santos", "SP", "SP-Litoral"),
    "campinas": ("Campinas", "SP", "SP-Interior"),
    "rio de janeiro": ("Rio de Janeiro", "RJ", "RJ-Capital"),
    "niteroi": ("Niterói", "RJ", "RJ-Capital"),
    "belo horizonte": ("Belo Horizonte", "MG", "MG-Capital"),
    "contagem": ("Contagem", "MG", "MG-Capital"),
    "uberlandia": ("Uberlândia", "MG", "MG-Interior"),
}


def canonizar_cidade(cidade_raw, uf_raw):
    """Normaliza cidade/UF do ground truth pra forma canônica."""
    if not cidade_raw:
        return None, uf_raw, None
    n = norm(cidade_raw)
    if n in CIDADE_CANONICA:
        nome, uf, cub = CIDADE_CANONICA[n]
        return nome, uf, cub
    # Tenta match parcial
    for k, (nome, uf, cub) in CIDADE_CANONICA.items():
        if k in n or n in k:
            return nome, uf, cub
    # Fallback: mantém como veio + CUB genérico
    return cidade_raw.title(), uf_raw, f"{uf_raw}-Outros" if uf_raw else None


def main():
    print("Carregando ground truth...", flush=True)
    gt_data = {}
    for f in GT_DIR.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        if "dados" in d and not d.get("erro"):
            gt_data[d["slug"]] = d["dados"]
    print(f"  {len(gt_data)} projetos com ground truth", flush=True)

    print("Carregando enriquecidos...", flush=True)
    enr_data = json.loads(ENR_FILE.read_text(encoding="utf-8"))
    enr_map = {p["slug"]: p for p in enr_data["projetos"]}

    # Compara e atualiza
    divergencias = []
    atualizados_count = 0
    for slug, gt in gt_data.items():
        # Slug mapping — gt tem slugs de entregas; enriquecidos tem slugs de indices-executivo
        # Tentar match exato primeiro
        matches = [slug]
        # Alguns slugs das entregas podem ter sufixo diferente
        # Ex: "ck-mission" pode estar como "ck-mission-r03" no indices-executivo

        matched_slug = None
        for candidate in matches:
            if candidate in enr_map:
                matched_slug = candidate
                break

        # Se não match direto, tenta fuzzy
        if not matched_slug:
            # Busca slug em enr_map que comece com mesmo cliente e tenha obra similar
            partes_gt = slug.split("-", 1)
            if len(partes_gt) == 2:
                cli_gt, obra_gt = partes_gt
                for enr_slug in enr_map:
                    if enr_slug.startswith(cli_gt) and obra_gt[:5] in enr_slug:
                        matched_slug = enr_slug
                        break

        if not matched_slug:
            divergencias.append({
                "tipo": "slug_sem_match",
                "slug_gt": slug,
                "gt": gt,
            })
            continue

        # Compara
        enr = enr_map[matched_slug]
        cidade_gt, uf_gt, cub_gt = canonizar_cidade(gt.get("cidade"), gt.get("uf"))

        div = {
            "slug_gt": slug,
            "slug_enr": matched_slug,
            "antes": {
                "cidade": enr.get("cidade"),
                "uf": enr.get("uf"),
                "cub_regiao": enr.get("cub_regiao"),
                "data_base": enr.get("data_memorial"),
            },
            "ground_truth": {
                "cidade_raw": gt.get("cidade"),
                "cidade_canonica": cidade_gt,
                "uf": uf_gt,
                "cub_regiao": cub_gt,
                "data_base_iso": gt.get("data_base_iso"),
                "data_entrega_iso": gt.get("data_entrega_iso"),
                "cub_valor": gt.get("cub_valor"),
                "total_rs": gt.get("total_rs"),
                "rsm2": gt.get("rsm2"),
            },
        }

        alterou = []
        if cidade_gt and cidade_gt != enr.get("cidade"):
            alterou.append(f"cidade: {enr.get('cidade')} -> {cidade_gt}")
            enr["cidade"] = cidade_gt
            enr["cidade_fonte"] = "ground_truth_entrega"
        if uf_gt and uf_gt != enr.get("uf"):
            alterou.append(f"uf: {enr.get('uf')} -> {uf_gt}")
            enr["uf"] = uf_gt
        if cub_gt and cub_gt != enr.get("cub_regiao"):
            alterou.append(f"cub_regiao: {enr.get('cub_regiao')} -> {cub_gt}")
            enr["cub_regiao"] = cub_gt
        if gt.get("data_base_iso"):
            enr["data_base"] = gt["data_base_iso"]
            enr["data_base_fonte"] = "ground_truth_entrega"
            alterou.append(f"data_base: {gt['data_base_iso']}")
        if gt.get("data_entrega_iso"):
            enr["data_entrega"] = gt["data_entrega_iso"]
        if gt.get("cub_valor"):
            enr["cub_valor_entrega"] = gt["cub_valor"]

        div["alteracoes"] = alterou
        if alterou:
            atualizados_count += 1
            divergencias.append(div)

            # Salva arquivo individual
            ind_path = ENR_DIR / f"{matched_slug}.json"
            ind_path.write_text(json.dumps(enr, indent=2, ensure_ascii=False), encoding="utf-8")

    # Atualiza consolidado
    enr_data["projetos"] = list(enr_map.values())
    enr_data["ground_truth_aplicado_em"] = datetime.now().isoformat(timespec="seconds")
    ENR_FILE.write_text(json.dumps(enr_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Salva divergências
    DIV_JSON.write_text(json.dumps({
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "n_ground_truth": len(gt_data),
        "n_matches": sum(1 for d in divergencias if d.get("alteracoes")),
        "n_sem_match": sum(1 for d in divergencias if d.get("tipo") == "slug_sem_match"),
        "atualizacoes": atualizados_count,
        "divergencias": divergencias,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    # Gera MD
    from collections import Counter
    cidades_alteradas = Counter()
    datas_adicionadas = 0
    for d in divergencias:
        for a in d.get("alteracoes", []):
            if a.startswith("cidade:"):
                cidades_alteradas[a] += 1
            if a.startswith("data_base:"):
                datas_adicionadas += 1

    lines = [
        "# Fase 12 — Ground Truth de Cidade + Data Base + Tipologia",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Resumo",
        "",
        f"- Entregas com ground truth extraído: **{len(gt_data)}**",
        f"- Projetos atualizados: **{atualizados_count}**",
        f"- Data base populada (antes era null): **{datas_adicionadas}**",
        f"- Divergências cidade encontradas: **{sum(1 for d in divergencias if any('cidade' in a for a in d.get('alteracoes', [])))}**",
        "",
        "---",
        "",
        "## Impacto",
        "",
        "Antes da Fase 12: cidade via **mapa manual** (inferência de cliente, não dado real).",
        "",
        "Depois da Fase 12: cidade via **leitura da capa do PDF/XLSX da entrega** (ground truth).",
        "",
        "Vantagens:",
        "- Cidade correta mesmo quando cliente tem obra em lugar inesperado",
        "- Data base = mês de referência do CUB → permite normalização temporal",
        "- Total e R$/m² diretos da entrega (mais confiáveis que indices-executivo)",
        "",
    ]

    # Top cidades mudadas
    if cidades_alteradas:
        lines.append("## Top 20 alterações de cidade")
        lines.append("")
        lines.append("| De → Para | N |")
        lines.append("|---|---:|")
        for mud, n in cidades_alteradas.most_common(20):
            lines.append(f"| {mud} | {n} |")
        lines.append("")

    # Sem match
    sem_match = [d for d in divergencias if d.get("tipo") == "slug_sem_match"]
    if sem_match:
        lines.append(f"## Slugs de entrega sem match na base enriquecida ({len(sem_match)})")
        lines.append("")
        lines.append("Esses projetos estão no Drive mas não em `indices-executivo/`. Possíveis entregas não-importadas.")
        lines.append("")
        for s in sem_match[:20]:
            lines.append(f"- `{s['slug_gt']}`")
        if len(sem_match) > 20:
            lines.append(f"- ...+ {len(sem_match)-20}")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nGround truth aplicado em {atualizados_count} projetos", flush=True)
    print(f"Data base populada: {datas_adicionadas}", flush=True)
    print(f"Salvo: {DIV_JSON}", flush=True)
    print(f"Salvo: {OUT_MD}", flush=True)


if __name__ == "__main__":
    main()
