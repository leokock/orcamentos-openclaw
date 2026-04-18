#!/usr/bin/env python3
"""Phase 20l — Revisao critica de MDs de analise via qwen2.5:14b local.

Para cada MD de analise, pede ao qwen:
- Identificar saltos logicos sem base nos dados
- Questionar hipoteses
- Sugerir analises/dados complementares
- Apontar ambiguidades ou trechos fracos

Saida: base/revisoes-qwen/{nome-md}.md

Uso:
    python scripts/revisar_md_qwen.py                 # revisa todos os principais
    python scripts/revisar_md_qwen.py --file X.md     # revisa arquivo especifico
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
OUT_DIR = BASE / "revisoes-qwen"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:14b"

# MDs principais pra revisar (caminhos relativos a BASE)
MDS_PRIORITARIOS = [
    "PALUDO-VS-NOVA-RESUMO.md",
    "CLUSTER3-E-PARAMETRICO-RESUMO.md",
    "ANALISE-FINANCEIRA-RESUMO.md",
    "ANALISE-AVANCADA-RESUMO.md",
    "ANALISE-PRODUTO-RESUMO.md",
]

# Round 2: MDs corrigidos + MDs novos
MDS_ROUND2 = [
    "PALUDO-VS-NOVA-V2-APOS-REVISAO.md",  # novo doc, aplica criticas
    "ANALISE-FINANCEIRA-RESUMO.md",  # corrigido
    "CLUSTER3-E-PARAMETRICO-RESUMO.md",  # corrigido
    "SESSAO-18ABR-RESUMO.md",  # nunca revisado
]

# Round 2b: MDs que ficaram sem revisao R2 no primeiro disparo
MDS_ROUND2B = [
    "ANALISE-AVANCADA-RESUMO.md",
    "ANALISE-PRODUTO-RESUMO.md",
    "comparacoes-clientes/mussi-vs-pass-e.md",
]


PROMPT_REVISAO = """Voce e um engenheiro senior de orcamento de obras civil atuando como revisor critico de uma analise quantitativa feita por um agente de IA.

Abaixo esta o documento a revisar. Seu papel nao e elogiar, e CRITICAR CONSTRUTIVAMENTE. Em portugues brasileiro direto, sem rodeios.

Estrutura sua resposta em 4 secoes curtas:

## 1. Saltos logicos ou conclusoes fracas
Aponte afirmacoes que nao se sustentam totalmente nos dados apresentados. Ex: correlacao tratada como causalidade, amostra pequena tirando conclusao generica, etc.

## 2. Hipoteses alternativas
Existem explicacoes alternativas para os achados principais que a analise nao considerou?

## 3. Dados/analises complementares que faltam
O que voce, como orcamentista senior, gostaria de ver pra validar as conclusoes?

## 4. Acoes praticas: sao mesmo acionaveis?
As recomendacoes operacionais no documento sao realistas? Ou sao genericas demais?

Seja especifico. Quando apontar fraqueza, cite o trecho ou numero do documento. Maximo 500 palavras.

---

DOCUMENTO PARA REVISAR:

{conteudo}
"""


def call_qwen(prompt: str, timeout: int = 1200) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.4,
            "top_p": 0.9,
            "num_predict": 1500,
            "num_ctx": 16384,  # docs grandes
        },
    }, timeout=timeout)
    r.raise_for_status()
    return r.json().get("response", "").strip()


def revisar_arquivo(md_path: Path) -> dict:
    if not md_path.exists():
        return {"erro": f"nao encontrado: {md_path}"}
    conteudo = md_path.read_text(encoding="utf-8")
    # Trunca se muito grande (qwen context 16k, ~10k chars)
    if len(conteudo) > 12000:
        conteudo = conteudo[:12000] + "\n\n[...documento truncado...]"
    prompt = PROMPT_REVISAO.format(conteudo=conteudo)
    t0 = time.time()
    try:
        resp = call_qwen(prompt)
        el = time.time() - t0
        return {"ok": True, "revisao": resp, "duration_s": round(el, 1),
                "tamanho_doc": len(conteudo)}
    except Exception as e:
        return {"erro": str(e)[:300], "duration_s": round(time.time() - t0, 1)}


def salvar_revisao(md_name: str, r: dict, suffix: str = "") -> Path:
    # Usar apenas basename (md_name pode ter "/" em path relativo)
    from pathlib import PurePath
    base_name = PurePath(md_name).name
    if base_name.endswith(".md") and suffix:
        base_name = base_name[:-3] + suffix + ".md"
    out = OUT_DIR / f"revisao-{base_name}"
    lines = [
        f"# Revisao critica: {md_name}",
        "",
        f"**Modelo:** qwen2.5:14b (local)",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Tempo:** {r.get('duration_s', 0)}s",
        "",
        "---",
        "",
        r.get("revisao", r.get("erro", "SEM CONTEUDO")),
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None)
    ap.add_argument("--round", default="1", choices=["1", "2", "2b"], help="1=MDs prioritarios, 2=corrigidos, 2b=restantes")
    ap.add_argument("--suffix", default="", help="sufixo pra arquivo de saida (ex: -r2)")
    args = ap.parse_args()

    if args.file:
        arquivos = [args.file]
    elif args.round == "2":
        arquivos = MDS_ROUND2
    elif args.round == "2b":
        arquivos = MDS_ROUND2B
    else:
        arquivos = MDS_PRIORITARIOS

    resumos = []
    for fn in arquivos:
        md_path = BASE / fn
        if not md_path.exists():
            # Tenta path absoluto
            md_path = Path(fn) if Path(fn).is_absolute() else md_path
        print(f"\n=== Revisando {fn} ===", flush=True)
        r = revisar_arquivo(md_path)
        if r.get("erro"):
            print(f"  ERRO: {r['erro']}", flush=True)
            resumos.append({"arquivo": fn, "status": "erro", "erro": r["erro"]})
            continue
        out = salvar_revisao(fn, r, args.suffix)
        print(f"  OK ({r['duration_s']}s, {r['tamanho_doc']} chars) → {out.name}", flush=True)
        # Print preview da revisao
        preview = r["revisao"][:600].replace("\n", " ").strip()
        print(f"  Preview: {preview[:400]}...", flush=True)
        resumos.append({"arquivo": fn, "status": "ok", "duration_s": r["duration_s"], "out": str(out)})

    # Resumo consolidado
    consolidado = OUT_DIR / "RESUMO-REVISOES.md"
    lines = [
        "# Revisoes Qwen2.5:14b — Indice",
        "",
        f"Gerado em {datetime.now().isoformat(timespec='seconds')}",
        "",
        "| Arquivo | Status | Tempo | Revisao |",
        "|---|---|---:|---|",
    ]
    for r in resumos:
        if r["status"] == "ok":
            link = Path(r["out"]).name
            lines.append(f"| {r['arquivo']} | ✓ | {r['duration_s']}s | [{link}]({link}) |")
        else:
            lines.append(f"| {r['arquivo']} | ✗ | — | {r.get('erro', '')[:80]} |")
    consolidado.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n\nIndice consolidado: {consolidado}", flush=True)


if __name__ == "__main__":
    main()
