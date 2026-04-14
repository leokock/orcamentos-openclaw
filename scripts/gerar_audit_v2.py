#!/usr/bin/env python3
"""Gera audit-v2-{slug}.md baseado na Fase 10 (PUs cross-projeto)
e na Fase 13 (29 novos índices derivados).

Para cada pacote:
1. Verifica outliers críticos (PU usado >> mediana ou << mediana)
2. Classifica por gravidade: bug (>1000% delta), atenção (>200%), ok
3. Compara totais dos 18 macrogrupos com a nova tabela de índices derivados
4. Sugere ajustes concretos
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw" / "base"
PACOTES = BASE / "pacotes"


def main():
    pus = json.loads((BASE / "itens-pus-agregados.json").read_text(encoding="utf-8"))
    derivados = json.loads((BASE / "indices-derivados-v2.json").read_text(encoding="utf-8"))

    for slug in ("arthen-arboris", "placon-arminio-tavares", "thozen-electra"):
        pasta = PACOTES / slug
        rev_path = pasta / "revisao-pus-cross.md"
        if not rev_path.exists():
            continue

        state = json.loads((pasta / "state.json").read_text(encoding="utf-8"))
        ac = state.get("ac") or 1
        ur = state.get("ur") or 1

        rev_text = rev_path.read_text(encoding="utf-8")

        critical = []
        for m in re.finditer(
            r"\| ([^|]+) \| ([^|]+) \| R\$ ([\d.]+) \| R\$ ([\d.]+) \| \*\*\+?([0-9.\-]+)%\*\* \| (\d+) \|",
            rev_text,
        ):
            mg = m.group(1).strip()
            desc = m.group(2).strip()
            pu_usado = float(m.group(3))
            pu_med = float(m.group(4))
            delta = float(m.group(5))
            n_obs = int(m.group(6))
            gravidade = (
                "bug" if abs(delta) > 1000
                else "critico" if abs(delta) > 500
                else "atencao" if abs(delta) > 100
                else "menor"
            )
            critical.append({
                "mg": mg, "desc": desc, "pu_usado": pu_usado,
                "pu_med": pu_med, "delta": delta, "n_obs": n_obs,
                "gravidade": gravidade,
            })

        bugs = [c for c in critical if c["gravidade"] == "bug"]
        criticos = [c for c in critical if c["gravidade"] == "critico"]
        atencao = [c for c in critical if c["gravidade"] == "atencao"]
        menores = [c for c in critical if c["gravidade"] == "menor"]

        lines = [
            f"# Audit V2 — {slug}",
            "",
            f"_Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} — revisão com base enriquecida (Fases 8-15)_",
            "",
            "## 🎯 Contexto",
            "",
            f"- **AC**: {ac:,.0f} m²".replace(",", "."),
            f"- **UR**: {ur}",
            "- Fontes novas consultadas:",
            "  - `itens-pus-agregados.json` — 4.525 PUs cross-projeto (Fase 10)",
            "  - `indices-derivados-v2.json` — 29 novos índices derivados (Fase 13)",
            "  - `base-indices-master-2026-04-13.json` — base consolidada (Fase 15)",
            "",
            "## 🚨 Gravidade dos outliers",
            "",
            f"| Categoria | Qtd | Ação sugerida |",
            f"|---|---|---|",
            f"| 🔴 **BUG (>1000% delta)** | {len(bugs)} | Investigar origem — provável erro de extração |",
            f"| 🟠 **Crítico (500-1000%)** | {len(criticos)} | Revisar manualmente antes de entregar |",
            f"| 🟡 **Atenção (100-500%)** | {len(atencao)} | Validar se faz sentido pro projeto |",
            f"| 🔵 **Menor (<100%)** | {len(menores)} | Normal, variação de mercado |",
            "",
        ]

        if bugs:
            lines.append("## 🔴 BUGS identificados (delta >1000%)")
            lines.append("")
            lines.append("Provável causa: o `gerar_executivo_auto.py` pode estar usando o TOTAL da linha no lugar do PU em certos casos.")
            lines.append("")
            lines.append("| Macrogrupo | Descrição | PU usado | PU esperado | Delta |")
            lines.append("|---|---|---|---|---|")
            for b in bugs[:10]:
                lines.append(
                    f"| {b['mg']} | {b['desc']} | R$ {b['pu_usado']:,.2f} | "
                    f"R$ {b['pu_med']:,.2f} | **+{b['delta']:,.0f}%** |".replace(",", ".")
                )
            lines.append("")
            lines.append("**AÇÃO**: NÃO ENTREGAR este pacote sem corrigir esses itens. Re-gerar após fix no script.")
            lines.append("")

        if criticos:
            lines.append("## 🟠 Críticos (delta 500-1000%)")
            lines.append("")
            lines.append("| Macrogrupo | Descrição | PU usado | PU esperado | Delta |")
            lines.append("|---|---|---|---|---|")
            for c in criticos[:10]:
                lines.append(
                    f"| {c['mg']} | {c['desc']} | R$ {c['pu_usado']:,.2f} | "
                    f"R$ {c['pu_med']:,.2f} | **+{c['delta']:,.0f}%** |".replace(",", ".")
                )
            lines.append("")

        if atencao:
            lines.append("## 🟡 Atenção (delta 100-500%)")
            lines.append("")
            lines.append("| Macrogrupo | Descrição | PU usado | PU esperado | Delta |")
            lines.append("|---|---|---|---|---|")
            for a in atencao[:15]:
                lines.append(
                    f"| {a['mg']} | {a['desc']} | R$ {a['pu_usado']:,.2f} | "
                    f"R$ {a['pu_med']:,.2f} | **{a['delta']:+.0f}%** |".replace(",", ".")
                )
            lines.append("")

        lines.append("## 📊 Comparação com novos índices derivados (Fase 13)")
        lines.append("")
        lines.append("Faixas P10-P90 da base de 126 projetos:")
        lines.append("")
        lines.append("| Índice derivado | Mediana base | Valor esperado × AC | n projetos |")
        lines.append("|---|---|---|---|")

        relevant_indices = [
            "custo_concreto_rsm2", "custo_aco_rsm2", "custo_forma_rsm2",
            "custo_escoramento_rsm2", "custo_impermeabilizacao_rsm2",
            "custo_elevador_rsm2", "custo_esquadrias_rsm2",
            "custo_pintura_rsm2", "custo_loucas_rsm2",
            "ci_total_rsm2",
        ]
        for ind_name in relevant_indices:
            ind = derivados.get("indices", {}).get(ind_name)
            if not ind:
                continue
            med = ind.get("mediana", 0)
            val_ac = med * ac
            lines.append(
                f"| {ind_name} | R$ {med:.2f}/m² | R$ {val_ac:,.0f} | {ind.get('n', 0)} |".replace(",", ".")
            )
        lines.append("")

        lines.append("## 📋 Recomendações")
        lines.append("")
        if bugs:
            lines.append(f"1. **BLOQUEANTE**: corrigir os {len(bugs)} bugs de PU antes de entregar o pacote ao cliente")
            lines.append(f"2. **Investigar**: rodar script de debug no `gerar_executivo_auto.py` pra ver onde o TOTAL está virando PU")
        if criticos:
            lines.append(f"3. **Revisar manualmente** os {len(criticos)} itens críticos — podem ser variantes legítimas ou erros")
        if atencao:
            lines.append(f"4. **Validar** os {len(atencao)} itens em atenção — podem refletir escolha técnica (ex: acabamento alto-padrão)")
        lines.append(f"5. **Cruzar** os totais por macrogrupo do pacote com a tabela de índices derivados acima")
        lines.append(f"6. **Considerar v2** dos pacotes após fix dos bugs — comparar valores antigos × novos")
        lines.append("")

        lines.append("## 🔗 Arquivos relacionados")
        lines.append("")
        lines.append(f"- `base/pacotes/{slug}/revisao-pus-cross.md` — revisão original de PUs")
        lines.append(f"- `base/pacotes/{slug}/audit-{slug}.md` — audit anterior (v1)")
        lines.append(f"- `base/itens-pus-agregados.json` — base cross-projeto Fase 10")
        lines.append(f"- `base/indices-derivados-v2.json` — 29 novos índices derivados")
        lines.append(f"- `base/base-indices-master-2026-04-13.json` — base master consolidada")
        lines.append("")

        out = pasta / f"audit-v2-{slug}.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"  OK: {out.name}  bugs={len(bugs)} criticos={len(criticos)} atencao={len(atencao)} menores={len(menores)}")


if __name__ == "__main__":
    main()
