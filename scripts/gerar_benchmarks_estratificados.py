#!/usr/bin/env python3
"""Fase 8 — Benchmarks estratificados.

Gera 1 MD por combinação (CUB-região × padrão × tipologia) com benchmarks
detalhados. Útil pra consulta rápida quando começa projeto novo.

Output:
    analises-cross-projeto/benchmarks-estratificados/{regiao}/{padrao}/{tipologia}.md
    analises-cross-projeto/benchmarks-estratificados/INDEX.md
"""
from __future__ import annotations

import json
import unicodedata
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
AGG = BASE / "analise-enriquecida-agregada.json"
ENR = BASE / "projetos-enriquecidos.json"
IND_DIR = BASE / "projetos-enriquecidos"
OUT_ROOT = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "benchmarks-estratificados"


def slug_safe(s):
    """Converte string em path seguro."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower().replace(" ", "-").replace("/", "-")
    return s


def carregar_projetos():
    """Carrega projetos enriquecidos + tipologia dos arquivos individuais."""
    enr = json.loads(ENR.read_text(encoding="utf-8"))
    projs = enr["projetos"]
    for p in projs:
        indiv = IND_DIR / f"{p['slug']}.json"
        if indiv.exists():
            try:
                d = json.loads(indiv.read_text(encoding="utf-8"))
                for k in ("tipologia_canonica", "tipologia_confianca", "tipologia_motivo"):
                    if d.get(k):
                        p[k] = d[k]
            except Exception:
                pass
    return {p["slug"]: p for p in projs}


def gerar_md_combinacao(key, info, projs_dict, out_path):
    """Gera MD detalhado pra uma combinação."""
    partes = key.split("::")
    nome_combo = info["nome"]

    # Parsear tipo de combinação
    if key.startswith("reg_pad_tip::"):
        regiao, padrao, tipologia = partes[1], partes[2], partes[3]
        tipo = "Região × Padrão × Tipologia"
    elif key.startswith("regiao_padrao::"):
        regiao, padrao, tipologia = partes[1], partes[2], "_misto_"
        tipo = "Região × Padrão"
    elif key.startswith("regiao::"):
        regiao, padrao, tipologia = partes[1], "_misto_", "_misto_"
        tipo = "Região"
    else:
        return None

    lines = [
        f"# Benchmark — {nome_combo}",
        "",
        f"**Tipo de combinação:** {tipo}",
        f"**N projetos:** {info['n_projetos']}",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        "",
        "---",
        "",
        "## Perfil financeiro",
        "",
    ]

    rs = info.get("rsm2_stats") or {}
    ac = info.get("ac_stats") or {}
    tot = info.get("total_stats") or {}
    ur = info.get("ur_stats") or {}

    if rs:
        lines.append("### R$/m² (projetos válidos, AC ≥ 1.000 m², R$/m² ∈ [500, 10k])")
        lines.append("")
        lines.append("| Percentil | R$/m² |")
        lines.append("|---|---:|")
        for k, label in [("min", "mín"), ("p25", "p25"), ("mediana", "**mediana**"),
                         ("p75", "p75"), ("max", "máx")]:
            v = rs.get(k)
            if v:
                lines.append(f"| {label} | R$ {v:,.0f} |")
        if rs.get("cv") is not None:
            lines.append(f"| CV (coef. variação) | {rs['cv']:.2f} |")
        lines.append(f"| N | {rs.get('n', 'N/D')} |")
        lines.append("")

    if ac:
        lines.extend([
            "### Área construída",
            "",
            "| Percentil | AC (m²) |",
            "|---|---:|",
            f"| mín | {ac.get('min'):,.0f} |" if ac.get('min') else "",
            f"| mediana | {ac.get('mediana'):,.0f} |" if ac.get('mediana') else "",
            f"| máx | {ac.get('max'):,.0f} |" if ac.get('max') else "",
            "",
        ])

    if tot and tot.get("mediana"):
        lines.extend([
            "### Total orçamento",
            "",
            f"- **Mediana total:** R$ {tot['mediana']:,.0f}",
            f"- Faixa: R$ {tot.get('min', 0):,.0f} — R$ {tot.get('max', 0):,.0f}",
            "",
        ])

    if ur and ur.get("mediana"):
        lines.append(f"**UR mediana:** {ur['mediana']:.0f}")
        lines.append("")

    # Estrutural
    conc = info.get("concreto_stats") or {}
    taxa = info.get("taxa_aco_stats") or {}
    forma = info.get("forma_stats") or {}
    if conc or taxa or forma:
        lines.extend([
            "## Perfil estrutural",
            "",
            "| Indicador | Mediana | n |",
            "|---|---:|---:|",
        ])
        if conc.get("mediana"):
            lines.append(f"| Concreto (m³/m² AC) | {conc['mediana']:.3f} | {conc.get('n', 'N/D')} |")
        if taxa.get("mediana"):
            lines.append(f"| Taxa aço (kg/m³ concreto) | {taxa['mediana']:.1f} | {taxa.get('n', 'N/D')} |")
        if forma.get("mediana"):
            lines.append(f"| Forma (m²/m² AC) | {forma['mediana']:.3f} | {forma.get('n', 'N/D')} |")
        lines.append("")

    # Distribuição MG
    mg = info.get("mg_pct_med") or {}
    if mg:
        lines.extend([
            "## Distribuição % Macrogrupo (mediana)",
            "",
            "| Macrogrupo | % do total |",
            "|---|---:|",
        ])
        for m, pct in sorted(mg.items(), key=lambda x: -x[1])[:20]:
            lines.append(f"| {m} | {pct:.1f}% |")
        lines.append("")

    # Top clientes
    top_cli = info.get("top_clientes") or {}
    if top_cli:
        lines.extend(["## Top clientes nesta combinação", ""])
        for c, n in list(top_cli.items())[:10]:
            lines.append(f"- **{c}**: {n} projeto(s)")
        lines.append("")

    # Lista de projetos
    slugs = info.get("slugs") or []
    if slugs:
        lines.extend([
            f"## Projetos ({len(slugs)})",
            "",
            "| Projeto | AC (m²) | R$/m² | Tipologia | Cidade |",
            "|---|---:|---:|---|---|",
        ])
        for slug in slugs[:30]:
            p = projs_dict.get(slug, {})
            ac_v = f"{p.get('ac_m2'):,.0f}" if p.get('ac_m2') else "N/D"
            rsm_v = f"R$ {p.get('rsm2'):,.0f}" if p.get('rsm2') else "N/D"
            tip = p.get('tipologia_canonica', 'N/D').replace('residencial_vertical_', 'rv_')
            cid = p.get('cidade', 'N/D')
            lines.append(f"| `{slug}` | {ac_v} | {rsm_v} | {tip} | {cid} |")
        lines.append("")

    # Interpretação automática
    lines.extend(["## Interpretação automática", ""])
    if rs.get("mediana"):
        lines.append(f"- Em `{regiao}`, empreendimentos {padrao}{' ' + tipologia if tipologia != '_misto_' else ''} custam tipicamente **R$ {rs['mediana']:,.0f}/m²** (faixa p25-p75: R$ {rs.get('p25', 0):,.0f}–R$ {rs.get('p75', 0):,.0f}).")
    if rs and rs.get("cv") is not None:
        if rs["cv"] < 0.15:
            lines.append(f"- CV {rs['cv']:.2f} — variação **baixa**. Benchmark confiável.")
        elif rs["cv"] < 0.30:
            lines.append(f"- CV {rs['cv']:.2f} — variação **moderada**. Bom benchmark mas considerar escopo.")
        else:
            lines.append(f"- CV {rs['cv']:.2f} — variação **alta**. Projetos nesta combinação são heterogêneos; usar com cuidado.")
    if info['n_projetos'] < 5:
        lines.append(f"- ⚠️ Amostra pequena (n={info['n_projetos']}) — tratar como referência, não conclusão.")
    elif info['n_projetos'] >= 10:
        lines.append(f"- ✓ Amostra razoável (n={info['n_projetos']}) — benchmark estatisticamente útil.")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    print("Carregando dados...", flush=True)
    agg = json.loads(AGG.read_text(encoding="utf-8"))
    projs_dict = carregar_projetos()
    combinacoes = agg["combinacoes"]

    gerados = []
    for key, info in combinacoes.items():
        if info.get("n_projetos", 0) < 3:
            continue

        # Categoriza path
        partes = key.split("::")
        if partes[0] == "reg_pad_tip":
            regiao, padrao, tipologia = partes[1], partes[2], partes[3]
            subdir = OUT_ROOT / slug_safe(regiao) / slug_safe(padrao)
            subdir.mkdir(parents=True, exist_ok=True)
            out_path = subdir / f"{slug_safe(tipologia)}.md"
        elif partes[0] == "regiao_padrao":
            regiao, padrao = partes[1], partes[2]
            subdir = OUT_ROOT / slug_safe(regiao)
            subdir.mkdir(parents=True, exist_ok=True)
            out_path = subdir / f"{slug_safe(padrao)}.md"
        elif partes[0] == "regiao":
            regiao = partes[1]
            subdir = OUT_ROOT
            subdir.mkdir(parents=True, exist_ok=True)
            out_path = subdir / f"regiao-{slug_safe(regiao)}.md"
        elif partes[0] == "cliente":
            # Pula — fichas de cliente ja existem em outra pasta
            continue
        else:
            continue

        gerar_md_combinacao(key, info, projs_dict, out_path)
        gerados.append({
            "key": key,
            "path": str(out_path.relative_to(OUT_ROOT.parent.parent)),
            "n": info["n_projetos"],
            "rsm2_mediana": (info.get("rsm2_stats") or {}).get("mediana"),
        })
        print(f"  {info['nome']:<60} n={info['n_projetos']:>3}", flush=True)

    # INDEX.md
    index_path = OUT_ROOT / "INDEX.md"
    lines = [
        "# Índice — Benchmarks Estratificados",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Total de benchmarks:** {len(gerados)}",
        "",
        "Benchmarks organizados por granularidade:",
        "- `regiao-{X}.md` — só região",
        "- `{regiao}/{padrao}.md` — região × padrão",
        "- `{regiao}/{padrao}/{tipologia}.md` — granularidade máxima",
        "",
        "---",
        "",
    ]

    # Agrupa por região
    from collections import defaultdict
    por_regiao = defaultdict(list)
    for g in gerados:
        k = g["key"]
        partes = k.split("::")
        regiao = partes[1] if len(partes) > 1 else "outro"
        por_regiao[regiao].append(g)

    for regiao, grupos in sorted(por_regiao.items()):
        lines.append(f"## {regiao} ({len(grupos)} benchmarks)")
        lines.append("")
        lines.append("| Tipo | Combinação | N | R$/m² mediana | Arquivo |")
        lines.append("|---|---|---:|---:|---|")
        for g in sorted(grupos, key=lambda x: -x["n"]):
            key = g["key"]
            partes = key.split("::")
            tipo = {"reg_pad_tip": "Rg × Pd × Tp", "regiao_padrao": "Rg × Pd", "regiao": "Região"}.get(partes[0], "?")
            nome = " | ".join(partes[1:])
            rsm2 = f"R$ {g['rsm2_mediana']:,.0f}" if g.get("rsm2_mediana") else "N/D"
            caminho = g["path"].replace("analises-cross-projeto/benchmarks-estratificados/", "")
            lines.append(f"| {tipo} | {nome} | {g['n']} | {rsm2} | [{caminho}]({caminho}) |")
        lines.append("")

    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nSalvo: {index_path}", flush=True)
    print(f"Total benchmarks gerados: {len(gerados)}", flush=True)


if __name__ == "__main__":
    main()
