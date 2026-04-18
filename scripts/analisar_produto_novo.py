#!/usr/bin/env python3
"""Fase 10 — SIMULADOR de analise de produto novo.

Dado caracteristicas de um projeto, retorna:
1. R$/m² esperado (faixa p25-p75 de combinacao similar)
2. Distribuicao MG esperada
3. Indicadores fisicos esperados
4. Alertas (anti-padroes detectados)
5. Oportunidades de otimizacao
6. 3-5 projetos comparaveis
7. Narrativa Qwen (opcional)

Uso:
    python scripts/analisar_produto_novo.py \\
        --cliente arthen --nome arboris \\
        --cidade Morretes --uf PR \\
        --ac 12500 --ur 48 --padrao medio-alto \\
        --tipologia residencial_vertical_medio_alto \\
        --n-torres 1 --n-pavimentos 15

Saida:
    analises-cross-projeto/simulador/{cliente}-{nome}.md
    analises-cross-projeto/simulador/{cliente}-{nome}.json
"""
from __future__ import annotations

import argparse
import json
import math
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

BASE = Path.home() / "orcamentos-openclaw" / "base"
AGREGADOS = BASE / "analise-enriquecida-agregada.json"
REGR = BASE / "regressao-rsm2.json"
ANTI = BASE / "anti-padroes.json"
ENR = BASE / "projetos-enriquecidos.json"

OUT_DIR = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "simulador"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


CUB_REGIAO_MAP = {
    ("SC", "Florianópolis"): "SC-Floripa",
    ("SC", "Balneário Camboriú"): "SC-BC",
    ("SC", "Balneário Piçarras"): "SC-Litoral-Norte",
    ("SC", "Bombinhas"): "SC-Litoral-Norte",
    ("SC", "Itajaí"): "SC-Vale-Itajai",
    ("SC", "Itapema"): "SC-Litoral-Norte",
    ("SC", "Porto Belo"): "SC-Litoral-Norte",
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
    return CUB_REGIAO_MAP.get((uf, cidade), f"{uf}-Outros" if uf else "desconhecido")


def inferir_ajuste_cliente(cliente_slug: str, anti_padroes: dict) -> tuple[float, str]:
    """Retorna ajuste em R$/m² a somar, baseado nas regras Fase 7."""
    cs = norm(cliente_slug)
    for regra in anti_padroes.get("regras_detectadas", []):
        r_txt = regra["regra"].lower()
        if "nova empreendimentos" in r_txt and "nova" in cs:
            return 2000, "Nova Empreendimentos tem padrão consistente de +R$ 2.000/m² vs predição (3/4 projetos outliers positivos)"
        if "cliente = all" in r_txt and cs.startswith("all"):
            return 2500, "ALL tem projetos +R$ 2.000-3.000/m² (n=1, média confiança)"
        if "f nogueira" in r_txt and cs.startswith("f-nogueira"):
            return -1200, "F Nogueira tem projetos -R$ 1.200/m² consistente (2 projetos, z=-1.3 cada)"
        if "paludo volo home" in r_txt and cs.startswith("paludo"):
            return -1100, "Paludo Volo Home tipicamente -R$ 1.100/m²"
        if "santa maria" in r_txt and cs.startswith("santa"):
            return -1000, "Santa Maria (Chapecó) -R$ 1.000/m² por CUB menor + escopo enxuto"
    return 0, None


def aplicar_regressao(log_ac, cub_reg, padrao, tipologia, regressao):
    """Calcula R$/m² previsto pela regressao."""
    coefs = {c["feature"]: c["coef"] for c in regressao["coeficientes"]}
    r = coefs.get("intercept", 0)
    r += coefs.get("log_ac", 0) * log_ac
    r += coefs.get(f"cub_regiao_{cub_reg}", 0)
    r += coefs.get(f"padrao_{padrao}", 0)
    r += coefs.get(f"tipologia_canonica_{tipologia}", 0)
    return r


def buscar_combinacao(cub_reg, padrao, tipologia, agregados):
    """Busca combinacao especifica. Se nao tiver, relaxa ate achar."""
    key_completa = f"reg_pad_tip::{cub_reg}::{padrao}::{tipologia}"
    if key_completa in agregados["combinacoes"]:
        return agregados["combinacoes"][key_completa], "exata (regiao+padrao+tipologia)"

    key_rp = f"regiao_padrao::{cub_reg}::{padrao}"
    if key_rp in agregados["combinacoes"]:
        return agregados["combinacoes"][key_rp], "parcial (regiao+padrao, ignora tipologia)"

    key_r = f"regiao::{cub_reg}"
    if key_r in agregados["combinacoes"]:
        return agregados["combinacoes"][key_r], "minima (só regiao)"

    return None, "sem combinacao"


def projetos_comparaveis(slug_base, cub_reg, padrao, tipologia, ac, enr, k=5):
    """Retorna k projetos mais similares por combinacao + proximidade de AC."""
    candidatos = []
    for p in enr["projetos"]:
        if p.get("cub_regiao") != cub_reg:
            continue
        if p.get("padrao") != padrao:
            continue
        if p.get("ac_m2") and ac:
            dist_ac = abs(math.log(p["ac_m2"]) - math.log(ac))
            candidatos.append((dist_ac, p))

    candidatos.sort(key=lambda x: x[0])
    return [
        {"slug": p["slug"], "ac": p.get("ac_m2"), "rsm2": p.get("rsm2"),
         "distancia_ac_log": round(d, 3), "tipologia": p.get("tipologia_canonica")}
        for d, p in candidatos[:k]
    ]


def simular(args):
    # Carrega bases
    agregados = json.loads(AGREGADOS.read_text(encoding="utf-8"))
    regressao = json.loads(REGR.read_text(encoding="utf-8"))
    anti_padroes = json.loads(ANTI.read_text(encoding="utf-8"))
    enr = json.loads(ENR.read_text(encoding="utf-8"))

    cub_reg = args.cub_regiao or cub_regiao(args.cidade, args.uf)
    log_ac = math.log(args.ac)
    slug_base = f"{norm(args.cliente)}-{norm(args.nome)}"

    # 1. Regressao — predicao "base" sem ajustes
    rsm2_regr = aplicar_regressao(log_ac, cub_reg, args.padrao, args.tipologia, regressao)

    # 2. Busca combinacao empirica
    combo, combo_tipo = buscar_combinacao(cub_reg, args.padrao, args.tipologia, agregados)
    rsm2_combo_med = None
    rsm2_combo_p25 = None
    rsm2_combo_p75 = None
    if combo:
        rs = combo.get("rsm2_stats") or {}
        rsm2_combo_med = rs.get("mediana")
        rsm2_combo_p25 = rs.get("p25")
        rsm2_combo_p75 = rs.get("p75")

    # 3. Ajuste por cliente (anti-padrao)
    ajuste_cliente, ajuste_motivo = inferir_ajuste_cliente(slug_base, anti_padroes)

    # 4. Predicao final (combinar regressao + combo empirica)
    if rsm2_combo_med:
        rsm2_base = (rsm2_regr + rsm2_combo_med) / 2  # media
    else:
        rsm2_base = rsm2_regr
    rsm2_final = rsm2_base + ajuste_cliente

    # 5. Faixa (usando std residuo da regressao)
    std = regressao.get("std_residuo", 700)
    faixa_low = rsm2_final - 0.67 * std   # ~p25 (0.67 sigma ~ 25th percentile for normal)
    faixa_high = rsm2_final + 0.67 * std

    # 6. Total estimado
    total_estimado = rsm2_final * args.ac

    # 7. Projetos comparaveis
    comps = projetos_comparaveis(slug_base, cub_reg, args.padrao, args.tipologia, args.ac, enr)

    # 8. Alertas
    alertas = []
    if rsm2_combo_med and abs(rsm2_final - rsm2_combo_med) / rsm2_combo_med > 0.15:
        alertas.append(f"Predição final ({rsm2_final:.0f}) difere em {(rsm2_final/rsm2_combo_med - 1)*100:+.0f}% da mediana da combinação ({rsm2_combo_med:.0f}) — verificar se escopo atípico.")
    if ajuste_motivo:
        alertas.append(f"Cliente {args.cliente} tem desvio histórico: {ajuste_motivo}")
    if combo_tipo != "exata (regiao+padrao+tipologia)":
        alertas.append(f"Predição usa combinação {combo_tipo}. N de projetos similares é pequeno; usar predição com cautela.")

    # 9. Oportunidades de otimizacao
    oportunidades = []
    if cub_reg == "SC-Litoral-Norte" and args.ac < 15000:
        oportunidades.append("Litoral-Norte tem economia de escala moderada (r=-0.52). Se viável, ampliar AC reduz R$/m² ~5-10%.")
    if args.padrao == "alto" and cub_reg == "SC-Floripa":
        oportunidades.append("Floripa alto é mais cara (+R$ 559/m² vs BC). Considerar BC se localização permitir.")
    if cub_reg == "SC-Floripa" and ajuste_cliente == 0:
        oportunidades.append("Cliente não é Nova/ALL (sem ajuste positivo), tampouco F Nogueira/Paludo/Santa Maria (sem negativo). Predição segue padrão regional típico.")

    # MG esperados (da combinacao)
    mg_esperado = combo.get("mg_pct_med") if combo else {}

    return {
        "input": vars(args),
        "slug": slug_base,
        "cub_regiao": cub_reg,
        "predicao": {
            "rsm2_regressao": round(rsm2_regr, 2),
            "rsm2_combinacao_mediana": rsm2_combo_med,
            "rsm2_combinacao_p25": rsm2_combo_p25,
            "rsm2_combinacao_p75": rsm2_combo_p75,
            "rsm2_base_medio": round(rsm2_base, 2),
            "ajuste_cliente": ajuste_cliente,
            "ajuste_motivo": ajuste_motivo,
            "rsm2_final": round(rsm2_final, 2),
            "faixa_rsm2": [round(faixa_low, 2), round(faixa_high, 2)],
            "total_estimado": round(total_estimado, 0),
        },
        "combinacao_usada": {
            "chave": combo["nome"] if combo else "nenhuma",
            "tipo": combo_tipo,
            "n_projetos": combo["n_projetos"] if combo else 0,
            "top_clientes": combo.get("top_clientes") if combo else None,
        },
        "mg_esperado": mg_esperado,
        "projetos_comparaveis": comps,
        "alertas": alertas,
        "oportunidades": oportunidades,
    }


def gerar_md(resultado: dict, out_md: Path):
    r = resultado
    inp = r["input"]
    p = r["predicao"]

    lines = [
        f"# Simulador de Produto — {inp['cliente']} / {inp['nome']}",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Cliente:** {inp['cliente']}",
        f"**Empreendimento:** {inp['nome']}",
        f"**Localização:** {inp['cidade']}/{inp['uf']} (região CUB: `{r['cub_regiao']}`)",
        f"**Padrão:** {inp['padrao']}",
        f"**Tipologia:** `{inp['tipologia']}`",
        f"**AC:** {inp['ac']:,} m²",
        f"**UR:** {inp.get('ur') or 'N/D'}",
        f"**N pavimentos:** {inp.get('n_pavimentos') or 'N/D'}",
        f"**N torres:** {inp.get('n_torres') or 'N/D'}",
        "",
        "---",
        "",
        "## 🎯 Predição de R$/m² e Total",
        "",
        "| Fonte | R$/m² |",
        "|---|---:|",
        f"| Regressão multivariada (Fase 6) | R$ {p['rsm2_regressao']:,.0f} |",
    ]

    if p["rsm2_combinacao_mediana"]:
        lines.append(f"| Mediana da combinação (Fase 4) | R$ {p['rsm2_combinacao_mediana']:,.0f} |")
        lines.append(f"| p25 / p75 da combinação | R$ {p['rsm2_combinacao_p25']:,.0f} / R$ {p['rsm2_combinacao_p75']:,.0f} |")

    lines.append(f"| Base médio (regr + combo)/2 | R$ {p['rsm2_base_medio']:,.0f} |")

    if p["ajuste_cliente"]:
        sinal = "+" if p["ajuste_cliente"] > 0 else ""
        lines.append(f"| Ajuste cliente (anti-padrão) | {sinal}R$ {p['ajuste_cliente']:,.0f} |")

    lines.extend([
        f"| **Predição final R$/m²** | **R$ {p['rsm2_final']:,.0f}** |",
        f"| Faixa provável (±0.67σ) | R$ {p['faixa_rsm2'][0]:,.0f} — R$ {p['faixa_rsm2'][1]:,.0f} |",
        f"| **Total estimado** | **R$ {p['total_estimado']:,.0f}** |",
        "",
        "---",
        "",
    ])

    # Combinacao usada
    combo = r["combinacao_usada"]
    lines.extend([
        "## 📊 Base estatística",
        "",
        f"- Combinação consultada: `{combo['chave']}` ({combo['tipo']})",
        f"- N de projetos similares na base: {combo['n_projetos']}",
    ])
    if combo.get("top_clientes"):
        top = ", ".join(f"{c}({n})" for c, n in list(combo["top_clientes"].items())[:3])
        lines.append(f"- Top clientes na combinação: {top}")
    lines.append("")

    # Alertas
    if r["alertas"]:
        lines.extend(["## ⚠️ Alertas", ""])
        for a in r["alertas"]:
            lines.append(f"- {a}")
        lines.append("")

    # Oportunidades
    if r["oportunidades"]:
        lines.extend(["## 💡 Oportunidades de otimização", ""])
        for o in r["oportunidades"]:
            lines.append(f"- {o}")
        lines.append("")

    # Distribuição MG esperada
    if r["mg_esperado"]:
        lines.extend(["## 🏗️ Distribuição % por Macrogrupo esperada (mediana da combinação)", ""])
        lines.append("| Macrogrupo | % esperado |")
        lines.append("|---|---:|")
        mg_sorted = sorted(r["mg_esperado"].items(), key=lambda x: -x[1])
        for mg, pct in mg_sorted[:15]:
            lines.append(f"| {mg} | {pct:.1f}% |")
        lines.append("")

    # Projetos comparáveis
    if r["projetos_comparaveis"]:
        lines.extend([
            "## 🔗 Projetos comparáveis",
            "",
            "| Projeto | AC (m²) | R$/m² | Tipologia |",
            "|---|---:|---:|---|",
        ])
        for p in r["projetos_comparaveis"]:
            rsm2 = f"R$ {p['rsm2']:,.0f}" if p.get('rsm2') else "N/D"
            ac = f"{p['ac']:,.0f}" if p.get('ac') else "N/D"
            lines.append(f"| `{p['slug']}` | {ac} | {rsm2} | {p.get('tipologia') or 'N/D'} |")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🔬 Método",
        "",
        "O R$/m² final combina:",
        "1. **Regressão multivariada** (Fase 6, R²=0.39): `log(AC) + cub_regiao + padrao + tipologia`",
        "2. **Mediana empírica** da combinação (Fase 4): projetos semelhantes na base",
        "3. **Ajuste por cliente** (Fase 7, quando aplicável): regras if-then detectadas",
        "",
        f"**Confiança da predição:** {'alta' if combo['n_projetos'] >= 10 else 'média' if combo['n_projetos'] >= 3 else 'baixa'}",
        "",
        "⚠️ **Use como ESTIMATIVA INICIAL**, não como orçamento definitivo. MAE da regressão é ~R$ 660/m² (~17% da mediana).",
    ])

    out_md.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--nome", required=True)
    ap.add_argument("--cidade", required=True)
    ap.add_argument("--uf", required=True)
    ap.add_argument("--ac", type=float, required=True)
    ap.add_argument("--ur", type=int, default=None)
    ap.add_argument("--padrao", required=True, choices=["economico", "medio", "medio-alto", "alto"])
    ap.add_argument("--tipologia", default="residencial_vertical_alto",
                    choices=["residencial_vertical_economico", "residencial_vertical_medio",
                             "residencial_vertical_medio_alto", "residencial_vertical_alto",
                             "residencial_vertical_luxo", "residencial_misto",
                             "comercial_vertical", "lajes_corporativas", "casa_condominio"])
    ap.add_argument("--cub-regiao", default=None, help="override regiao CUB")
    ap.add_argument("--n-torres", type=int, default=None)
    ap.add_argument("--n-pavimentos", type=int, default=None)
    args = ap.parse_args()

    resultado = simular(args)

    slug = resultado["slug"]
    out_json = OUT_DIR / f"{slug}.json"
    out_md = OUT_DIR / f"{slug}.md"
    out_json.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    gerar_md(resultado, out_md)

    print(f"\nSalvo: {out_json}")
    print(f"Salvo: {out_md}")

    # Resumo console
    p = resultado["predicao"]
    print(f"\n=== RESUMO {slug} ===")
    print(f"  R$/m² regressão:      R$ {p['rsm2_regressao']:,.0f}")
    if p["rsm2_combinacao_mediana"]:
        print(f"  R$/m² combinação:     R$ {p['rsm2_combinacao_mediana']:,.0f} (mediana)")
    if p["ajuste_cliente"]:
        print(f"  Ajuste cliente:       {'+' if p['ajuste_cliente']>0 else ''}R$ {p['ajuste_cliente']:,.0f}")
    print(f"  R$/m² FINAL:          R$ {p['rsm2_final']:,.0f}  (faixa {p['faixa_rsm2'][0]:,.0f}–{p['faixa_rsm2'][1]:,.0f})")
    print(f"  Total estimado:       R$ {p['total_estimado']:,.0f}")
    print(f"  Alertas: {len(resultado['alertas'])} | Oportunidades: {len(resultado['oportunidades'])}")


if __name__ == "__main__":
    main()
