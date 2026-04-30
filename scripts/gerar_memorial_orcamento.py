"""Gera o `memorial-orcamento.md` agregado da Electra + `.docx` via pandoc.

Consolida:
- Identidade da obra (00-projeto/projeto.json)
- Decisões oficiais do cliente (00-projeto/decisoes-estudo-projeto.json)
- EAP (01-eap/eap.md)
- Composições e insumos (02-composicoes-insumos/)
- Memoriais de cada disciplina (04-disciplinas/*/memorial.md + 05-extras/*/memorial.md)
- Consolidado de custo + pendências
- Pendências globais (00-projeto/REVISAO-POS-ESTUDO.md)

Uso:
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_memorial_orcamento.py
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_memorial_orcamento.py --no-docx
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

from atualizar_painel import (
    DISCIPLINAS_DIR,
    EXTRAS_DIR,
    ORCAMENTO_DIR,
    discovery,
    fmt_brl,
    ordem_planejada,
    status_icon,
    status_label,
)

PROJETO_DIR = ORCAMENTO_DIR / "00-projeto"
EAP_DIR = ORCAMENTO_DIR / "01-eap"
COMP_DIR = ORCAMENTO_DIR / "02-composicoes-insumos"
MEMORIAL_MD = ORCAMENTO_DIR / "memorial-orcamento.md"
MEMORIAL_DOCX = ORCAMENTO_DIR / "memorial-orcamento.docx"


def brt_now() -> str:
    return datetime.now(timezone(timedelta(hours=-3))).strftime("%Y-%m-%d %H:%M BRT")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def secao_identidade(proj: dict) -> list[str]:
    p = proj["projeto"]
    a = proj["areas"]
    r = proj["resumo"]
    apts = proj["apartamentos"]
    vagas = proj["vagas"]
    infra = proj["infraestrutura_comum"]

    end = p["endereco"]
    endereco = f"{end['rua']}, {end['numero']} — {end['bairro']}, {end['cidade']}/{end['uf']} (mun. legal {end['municipio_legal']})"

    lines = [
        "## 1. Identidade da obra",
        "",
        "| Item | Valor |",
        "|---|---|",
        f"| **Cliente** | {p['cliente']} |",
        f"| **Proprietário** | {p['proprietario']} ({p['cnpj_proprietario']}) |",
        f"| **Empreendimento** | {p['nome']} ({p['codigo']}) |",
        f"| **Tipologia** | {p['tipo']} |",
        f"| **Endereço** | {endereco} |",
        f"| **Torres** | {p['numero_torres']} |",
        f"| **Pavimentos distintos** | {r['total_pavtos_distintos']} tipos ({r['total_pavtos_fisicos']} físicos) |",
        f"| **Área construída total** | {a['construida_total_m2']:,.2f} m² |".replace(",", "X").replace(".", ",").replace("X", "."),
        f"| **Área privativa total** | {a['privativa_total_m2']:,.2f} m² |".replace(",", "X").replace(".", ",").replace("X", "."),
        f"| **Unidades residenciais** | {apts['total_unidades']} |",
        f"| **Salas comerciais** | {proj.get('salas_comerciais', {}).get('total', '—')} |",
        f"| **Vagas totais** | {vagas['total_geral']} |",
        f"| **Elevadores** | {infra['elevadores']['total']} ({infra['elevadores']['sociais']} sociais + {infra['elevadores']['emergencia']} emergência) |",
        f"| **Prazo de obra** | {p['prazo_obra_meses']} meses ({p['prazo_obra_inicio']} → {p['prazo_obra_termino']}) |",
        f"| **Revisão do memorial** | {proj['revisao']} (atualizado em {proj['data_atualizacao']}) |",
        "",
    ]
    return lines


def secao_decisoes(decisoes: dict) -> list[str]:
    lines = ["## 2. Decisões oficiais do cliente", ""]
    lines.append(f"> Extrato do Estudo de Projeto / Ata de Reunião oficial Cartesian.")
    lines.append(f"> Fonte de verdade — prevalece sobre IFC/DWG quando houver conflito.")
    lines.append(f"> Última extração: {decisoes.get('_meta', {}).get('data_extracao', '—')}")
    lines.append("")

    cron = decisoes.get("cronograma_oficial", {})
    if cron:
        lines.append("### Cronograma")
        lines.append(f"- **Início:** {cron.get('inicio_obra')} · **Término:** {cron.get('termino_obra')} · **Duração:** {cron.get('duracao_meses')} meses")
        if cron.get("estrategia"):
            lines.append(f"- **Estratégia:** {cron['estrategia']}")
        if cron.get("estrutura_duracao_anos"):
            lines.append(f"- **Estrutura completa:** {cron['estrutura_duracao_anos']} anos")
        lines.append("")

    contato = decisoes.get("contato_cliente", {}).get("principal", {})
    if contato:
        lines.append("### Contato principal")
        lines.append(f"- **{contato.get('nome')}** — {contato.get('cargo')} ({contato.get('email')})")
        lines.append("")

    bench = decisoes.get("contato_cliente", {}).get("projeto_benchmark")
    if bench:
        lines.append(f"**Projeto benchmark:** {bench} — Nicholas aponta onde Electra difere.")
        lines.append("")

    return lines


def secao_eap() -> list[str]:
    lines = ["## 3. EAP adotada", ""]
    eap_md = read_text(EAP_DIR / "eap.md")
    eap_json_path = EAP_DIR / "eap.json"

    if eap_json_path.exists():
        try:
            eap_json = read_json(eap_json_path)
            resumo = eap_json.get("_resumo") if isinstance(eap_json, dict) else None
            if resumo:
                lines.append(f"- **Estrutura:** {resumo.get('unidades','—')} unidades · {resumo.get('celulas','—')} células · {resumo.get('etapas','—')} etapas · **{resumo.get('subetapas','—')} subetapas**")
        except Exception:
            pass

    lines.append(f"- **EAP doc:** [[eap]] · planilha `01-eap/eap.xlsx` (importado no AltoQi Visus via `EAP-Visus.xlsx`)")
    lines.append("")

    if eap_md:
        lines.append("### Critério de estruturação")
        lines.append("")
        # extrai só primeiros N parágrafos
        trecho = "\n".join(eap_md.splitlines()[:40])
        lines.append(trecho)
        lines.append("")

    return lines


def secao_composicoes() -> list[str]:
    lines = ["## 4. Composições e insumos — base de custo", ""]
    insumos_path = COMP_DIR / "insumos-precos.json"
    if insumos_path.exists():
        try:
            insumos = read_json(insumos_path)
            n = insumos.get("total_insumos") if isinstance(insumos, dict) else len(insumos)
            fonte = insumos.get("fonte", "—") if isinstance(insumos, dict) else "—"
            lines.append(f"- **Catálogo de insumos:** {n} itens (fonte: {fonte})")
        except Exception:
            pass
    lines.append(f"- **Docs:** [[composicoes]] · [[insumos]]")
    lines.append(f"- **Planilhas de referência:** `02-composicoes-insumos/composicoes.xlsx`, `insumos.xlsx`, `cpu.xlsx`")
    lines.append(f"- **Fonte dos PUs:** AltoQi Visus + cotações Cartesian (histórico de projetos executivos)")
    lines.append("")
    return lines


def secao_disciplinas(itens: list[dict]) -> list[str]:
    lines = ["## 5. Orçamento por disciplina", ""]
    lines.append("Cada disciplina abaixo tem seu memorial inline. Fonte: `04-disciplinas/<nome>/memorial.md` ou `05-extras/<nome>/memorial.md` — acessível também pelos wikilinks na lista abaixo.")
    lines.append("")

    for item in itens:
        num = item.get("order", "—")
        folder = item["folder"]
        icon = status_icon(item["status"])
        label = status_label(item["status"])
        root = EXTRAS_DIR if item["kind"] == "extra" else DISCIPLINAS_DIR
        rel_base = "05-extras" if item["kind"] == "extra" else "04-disciplinas"

        lines.append(f"### {num}. {folder} — {icon} {label}")
        lines.append("")
        lines.append(f"**Fonte:** [[{rel_base}/{folder}/memorial|{folder}/memorial.md]]")
        lines.append("")

        meta = []
        if item["total_rs"] is not None:
            meta.append(f"**Total:** {fmt_brl(item['total_rs'])}")
        pend = item.get("pendencias") or {}
        pend_total = sum(pend.values()) if pend else 0
        if pend_total:
            meta.append(f"**Pendências:** 🔴 {pend.get('Alta',0)} · 🟡 {pend.get('Média',0)} · ⚪ {pend.get('Baixa',0)}")
        if meta:
            lines.append(" · ".join(meta))
            lines.append("")

        memorial_path = root / folder / "memorial.md"
        if item["memorial_filled"] and memorial_path.exists():
            content = memorial_path.read_text(encoding="utf-8")
            # shift heading levels: # → ####, ## → #####, etc (pra caber em H3)
            shifted = re.sub(r"(?m)^(#{1,6}) ", lambda m: "#" * (len(m.group(1)) + 3) + " ", content)
            lines.append(shifted.rstrip())
            lines.append("")
        else:
            lines.append(f"_Memorial ainda é stub._")
            lines.append("")

        lines.append("---")
        lines.append("")

    return lines


def secao_consolidado(itens: list[dict], proj: dict) -> list[str]:
    ac = proj["areas"]["construida_total_m2"]

    lines = ["## 6. Consolidado", ""]
    lines.append(f"Área construída total: **{ac:,.2f} m²**".replace(",", "X").replace(".", ",").replace("X", "."))
    lines.append("")
    lines.append("| # | Disciplina | Status | Total R$ | R$/m² AC |")
    lines.append("|---:|---|:---:|---:|---:|")

    total_geral = 0.0
    processadas = 0
    for item in itens:
        num = item.get("order", "—")
        folder = item["folder"]
        icon = status_icon(item["status"])
        total = item["total_rs"]
        if total is not None:
            total_geral += total
            processadas += 1
            rs_m2 = f"R$ {total/ac:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if ac else "—"
            lines.append(f"| {num} | {folder} | {icon} | {fmt_brl(total)} | {rs_m2} |")
        else:
            lines.append(f"| {num} | {folder} | {icon} | — | — |")

    lines.append(f"| — | **TOTAL (processadas: {processadas}/{len(itens)})** | — | **{fmt_brl(total_geral)}** | **R$ {total_geral/ac:,.2f}** |".replace(",", "X").replace(".", ",").replace("X", "."))
    lines.append("")
    lines.append(f"⚠ Total só agrega as **{processadas} disciplinas com `quantitativos.xlsx` fechado**. Disciplinas em status ⬜/📝/⏸️ ainda não somam.")
    lines.append("")
    return lines


def secao_metodologia() -> list[str]:
    return [
        "## 7. Metodologia",
        "",
        "### 3 fontes de dados",
        "",
        "| Fonte | Escopo | Quem extrai |",
        "|---|---|---|",
        "| **BIM (Visus)** | Arquitetura, revestimentos, acabamentos, esquadrias, fachada, impermeabilização | Leo (extração direta do modelo) |",
        "| **Planilha (IA)** | Instalações (hidro, elétrico, telecom, PCI, estrutura, HVAC), louças, metais | Claude + Leo (IFC/DWG processados) |",
        "| **Índices paramétricos** | Ger. Téc/Adm, canteiro, controle tecnológico, EPCs, mobiliário | Claude (médias de executivos Cartesian) |",
        "",
        "### Fluxo",
        "",
        "BIM (Visus) + Planilha (IA/índices) → Excel consolidado → reimporta no Visus.",
        "",
        "### Workflow por disciplina (3 passos)",
        "",
        "1. **Analisar fórmulas** do `extracao.xlsx` → escrever `memorial.md` detalhado",
        "2. **Script gerador** `gerar_quantitativos_<disciplina>.py` → `quantitativos.xlsx` com valores Electra fechados",
        "3. **Atualizar painel** via `atualizar_painel.py` e regenerar este memorial via `gerar_memorial_orcamento.py`",
        "",
    ]


def secao_pendencias_globais() -> list[str]:
    revisao = read_text(PROJETO_DIR / "REVISAO-POS-ESTUDO.md")
    lines = ["## 8. Pendências globais", ""]
    lines.append("Extraído de [[REVISAO-POS-ESTUDO]] — checklist de revisão contra o Estudo de Projeto/Ata.")
    lines.append("")

    # extrair seções "Pendências que travam fechamento" até o fim
    match = re.search(r"## 🚨 Pendências.*?(?=\n## (?!🚨)|\Z)", revisao, re.DOTALL)
    if match:
        # shift headings
        trecho = match.group(0)
        trecho = re.sub(r"(?m)^(#{1,6}) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", trecho)
        lines.append(trecho.rstrip())
        lines.append("")
    else:
        lines.append("_Seção de pendências não encontrada em REVISAO-POS-ESTUDO.md._")
        lines.append("")

    return lines


def gerar_md() -> str:
    proj = read_json(PROJETO_DIR / "projeto.json")
    try:
        decisoes = read_json(PROJETO_DIR / "decisoes-estudo-projeto.json")
    except FileNotFoundError:
        decisoes = {}

    ordem = ordem_planejada()
    itens = []
    for order, folder, kind in ordem:
        root = EXTRAS_DIR if kind == "extra" else DISCIPLINAS_DIR
        pasta = root / folder
        if not pasta.exists():
            continue
        info = discovery(pasta, kind)
        info["order"] = order
        info["kind"] = kind
        itens.append(info)
    itens.sort(key=lambda x: x.get("order", 999))

    lines = []
    lines.append("---")
    lines.append("tags: [electra, memorial, orcamento-executivo]")
    lines.append(f"gerado: \"{brt_now()}\"")
    lines.append("---")
    lines.append("")
    lines.append("# Memorial — Orçamento Executivo Thozen Electra")
    lines.append("")
    lines.append(f"> **Auto-gerado.** Última geração: **{brt_now()}**")
    lines.append(">")
    lines.append("> Regenerar: `py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_memorial_orcamento.py`")
    lines.append(">")
    lines.append("> Este documento agrega os memoriais por disciplina + dados oficiais do empreendimento + decisões do cliente + pendências globais. Serve como entregável final do orçamento executivo.")
    lines.append(">")
    lines.append("> **Fontes:** [[projeto]] (dados oficiais) · [[estudo-de-projeto-ata]] (decisões) · [[Estrutura do orçamento]] (painel) · `04-disciplinas/*/memorial.md`")
    lines.append("")

    lines.extend(secao_identidade(proj))
    if decisoes:
        lines.extend(secao_decisoes(decisoes))
    lines.extend(secao_eap())
    lines.extend(secao_composicoes())
    lines.extend(secao_disciplinas(itens))
    lines.extend(secao_consolidado(itens, proj))
    lines.extend(secao_metodologia())
    lines.extend(secao_pendencias_globais())

    return "\n".join(lines) + "\n"


def gerar_docx(md_path: Path, docx_path: Path) -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("⚠ pandoc não encontrado no PATH — pulando geração do docx")
        return False
    try:
        subprocess.run(
            [pandoc, str(md_path), "-o", str(docx_path), "--from", "markdown", "--to", "docx"],
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠ pandoc falhou: {e}")
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-docx", action="store_true", help="Não gerar o .docx (só o .md)")
    args = ap.parse_args()

    md = gerar_md()
    MEMORIAL_MD.write_text(md, encoding="utf-8")
    n_lines = md.count("\n")
    print(f"✓ Memorial md gerado: {MEMORIAL_MD} ({n_lines:,} linhas, {len(md):,} bytes)")

    if not args.no_docx:
        ok = gerar_docx(MEMORIAL_MD, MEMORIAL_DOCX)
        if ok:
            size_kb = MEMORIAL_DOCX.stat().st_size / 1024
            print(f"✓ Memorial docx gerado: {MEMORIAL_DOCX} ({size_kb:.1f} KB)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
