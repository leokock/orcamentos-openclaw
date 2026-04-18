#!/usr/bin/env python3
"""Fase 1 do PLANO-ANALISE-PRODUTO — Extração de metadados estruturados.

Usa Gemma local (via Ollama) pra ler memoriais/PDFs/docs de projetos e
extrair JSON estruturado com tipologia, localização, sistema estrutural,
n_pavimentos, n_elevadores, etc.

Fontes processadas (em ordem de prioridade):
  1. PROJETO.md / briefing / memorial.md (mais direto)
  2. *.docx (memoriais justificativos)
  3. PDFs de memorial descritivo / estudos preliminares
  4. qualitative.observacoes_orcamentista (dos 126 executivos)
  5. IFC (se disponível) — via ifcopenshell

Output: base/metadados-projeto/{slug}.json

Pipeline retomável via base/metadados-queue.json.

Uso:
    python scripts/extrair_metadados_projeto.py                 # fila toda
    python scripts/extrair_metadados_projeto.py --slug arthen-arboris
    python scripts/extrair_metadados_projeto.py --source drive  # só _Projetos_IA
    python scripts/extrair_metadados_projeto.py --source exec   # só executivos
    python scripts/extrair_metadados_projeto.py --test          # 3 projetos smoke
"""
from __future__ import annotations

import argparse
import json
import re
import time
import unicodedata
from datetime import datetime
from pathlib import Path

import requests

BASE = Path.home() / "orcamentos-openclaw" / "base"
METADADOS_DIR = BASE / "metadados-projeto"
METADADOS_DIR.mkdir(parents=True, exist_ok=True)
IDX_DIR = BASE / "indices-executivo"
PROJETOS_DIR = Path.home() / "orcamentos" / "projetos"

QUEUE = BASE / "metadados-queue.json"
LOG = BASE / "metadados-extracao.log.jsonl"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"

MAX_TEXT_CHARS = 12000  # caber no num_ctx 16k com folga
TIMEOUT = 180


PROMPT_TEMPLATE = """Leia o texto abaixo (memorial descritivo ou briefing de construção civil brasileira) e extraia metadados estruturados em JSON.

RETORNE APENAS O JSON, sem texto adicional. Use null quando informação não estiver disponível.

Schema esperado:
{{
  "cidade": "string|null",
  "uf": "SC|RS|PR|SP|RJ|MG|BA|GO|ES|DF|CE|PE|outros|null",
  "tipologia": "residencial_multifamiliar|residencial_misto|comercial|lajes_corporativas|casa_condominio|industrial|null",
  "padrao_declarado": "economico|medio|medio_alto|alto|luxo|null",
  "n_torres": "int|null",
  "n_pavimentos_total": "int|null",
  "n_pavimentos_garagem": "int|null",
  "n_pavimentos_tipo": "int|null",
  "n_pavimentos_lazer": "int|null",
  "n_tipologias_apto": "int|null",
  "n_elevadores": "int|null",
  "n_unidades_residenciais": "int|null",
  "n_unidades_comerciais": "int|null",
  "n_vagas_garagem": "int|null",
  "area_construida_m2": "float|null",
  "area_terreno_m2": "float|null",
  "area_lazer_m2": "float|null",
  "area_privativa_tipo_m2": "float|null",
  "sistema_estrutural": "alvenaria_estrutural|concreto_armado|concreto_protendido|pre_moldado|misto|null",
  "fck_predominante_mpa": "int|null",
  "altura_pe_direito_m": "float|null",
  "tem_subsolo": "bool|null",
  "tem_pele_de_vidro": "bool|null",
  "tem_churrasqueira_apto": "bool|null",
  "tem_gerador": "bool|null",
  "tem_piscina": "bool|null",
  "tem_spda": "bool|null",
  "tem_climatizacao_central": "bool|null",
  "tipo_cobertura": "telha_ceramica|telha_metalica|laje_impermeabilizada|concreto_aparente|null",
  "cub_referencia": "string|null",
  "data_memorial_iso": "YYYY-MM-DD|null",
  "observacoes_relevantes": "string|null"
}}

TEXTO:
{texto}"""


def norm(s):
    s = str(s or "").lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _read_md(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def _read_pdf(path: Path, max_pages: int = 10) -> str:
    try:
        import pdfplumber
        texto = []
        with pdfplumber.open(str(path)) as pdf:
            for i, page in enumerate(pdf.pages[:max_pages]):
                t = page.extract_text()
                if t:
                    texto.append(t)
        return "\n\n".join(texto)
    except Exception as e:
        return f"[erro lendo PDF: {e}]"


def _read_docx(path: Path) -> str:
    try:
        import docx
        doc = docx.Document(str(path))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception as e:
        return f"[erro lendo DOCX: {e}]"


def _read_ifc_meta(path: Path) -> str:
    """Lê metadados básicos do IFC (n pavimentos, áreas de laje)."""
    try:
        import ifcopenshell
        f = ifcopenshell.open(str(path))
        info = []
        projeto = f.by_type("IfcProject")
        if projeto:
            info.append(f"Projeto IFC: {projeto[0].Name}")
        andares = f.by_type("IfcBuildingStorey")
        info.append(f"Num pavimentos (IfcBuildingStorey): {len(andares)}")
        if andares:
            nomes = [a.Name for a in andares if a.Name][:20]
            info.append(f"Pavimentos: {', '.join(nomes)}")
        # Área aproximada
        lajes = f.by_type("IfcSlab")
        info.append(f"Num lajes: {len(lajes)}")
        return "\n".join(info)
    except Exception as e:
        return f"[erro lendo IFC: {e}]"


def coletar_fontes_drive(slug: str) -> tuple[str, list]:
    """Coleta texto de todas as fontes do projeto em _Projetos_IA/{slug}/."""
    proj_dir = PROJETOS_DIR / slug
    if not proj_dir.exists():
        return "", []

    textos = []
    fontes = []

    # MDs na raiz do projeto e subpastas top
    for md in proj_dir.rglob("*.md"):
        if md.stat().st_size > 200:  # skip muito pequenos
            t = _read_md(md)
            if t:
                textos.append(f"## FONTE: {md.name}\n{t[:5000]}")
                fontes.append(str(md.relative_to(proj_dir)))

    # DOCX
    for dx in proj_dir.rglob("*.docx"):
        if "memorial" in norm(dx.name) or "justif" in norm(dx.name) or "brief" in norm(dx.name):
            t = _read_docx(dx)
            if t and not t.startswith("[erro"):
                textos.append(f"## FONTE: {dx.name}\n{t[:5000]}")
                fontes.append(str(dx.relative_to(proj_dir)))

    # PDFs memorial/briefing
    for pdf in proj_dir.rglob("*.pdf"):
        if "memorial" in norm(pdf.name) or "briefing" in norm(pdf.name) or "rt" in norm(pdf.name)[:5]:
            t = _read_pdf(pdf, max_pages=8)
            if t and not t.startswith("[erro"):
                textos.append(f"## FONTE: {pdf.name}\n{t[:4000]}")
                fontes.append(str(pdf.relative_to(proj_dir)))
                if len(textos) >= 5:  # limite pra não inflar
                    break

    # 1 IFC como exemplo
    ifcs = list(proj_dir.rglob("*.ifc"))
    if ifcs:
        ifc_info = _read_ifc_meta(ifcs[0])
        textos.append(f"## FONTE: {ifcs[0].name}\n{ifc_info[:1500]}")
        fontes.append(str(ifcs[0].relative_to(proj_dir)))

    texto_combinado = "\n\n".join(textos)[:MAX_TEXT_CHARS]
    return texto_combinado, fontes


def coletar_fonte_exec(slug: str) -> tuple[str, list]:
    """Coleta texto de qualitative.observacoes_orcamentista do executivo."""
    f = IDX_DIR / f"{slug}.json"
    if not f.exists():
        return "", []
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return "", []

    q = d.get("qualitative") or {}
    textos = []

    # Observações orçamentista
    obs_list = q.get("observacoes_orcamentista") or []
    if obs_list:
        obs_txt = []
        for obs in obs_list:
            if isinstance(obs, dict):
                ctx = obs.get("contexto", "")
                msg = obs.get("observacao", "")
                cat = obs.get("categoria", "")
                obs_txt.append(f"[{cat}] {ctx}: {msg}")
        textos.append("## OBSERVACOES_ORCAMENTISTA:\n" + "\n".join(obs_txt))

    # Notas no topo do JSON
    if d.get("notas"):
        textos.append(f"## NOTAS: {d['notas']}")
    if d.get("data_base"):
        textos.append(f"## DATA_BASE: {d['data_base']}")

    # Dados estruturais tb viram contexto
    est = d.get("indices_estruturais") or {}
    if est:
        textos.append("## INDICES_ESTRUTURAIS:")
        for k, v in est.items():
            textos.append(f"  {k}: {v}")

    # Dados gerais
    textos.append(f"## PROJETO: {slug}")
    if d.get("ac"):
        textos.append(f"AC: {d['ac']} m²")
    if d.get("ur"):
        textos.append(f"UR: {d['ur']}")
    if d.get("total"):
        textos.append(f"Total: R$ {d['total']:,.0f}")

    return "\n".join(textos)[:MAX_TEXT_CHARS], ["qualitative"]


def call_gemma(prompt: str) -> str:
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "top_p": 0.9,
            "num_predict": 2000,
            "num_ctx": 16384,
        },
    }, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response", "").strip()


def parse_json(raw: str) -> dict:
    raw = raw.strip()
    # Remove markdown fence se existir
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```\s*$", "", raw, flags=re.MULTILINE)
    # Busca primeiro {
    s = raw.find("{")
    e = raw.rfind("}")
    if s < 0 or e <= s:
        raise ValueError(f"JSON nao encontrado: {raw[:300]}")
    j = raw[s:e + 1]
    try:
        return json.loads(j)
    except json.JSONDecodeError:
        # Tenta limpar vírgulas perdidas
        j2 = re.sub(r",\s*}", "}", j)
        j2 = re.sub(r",\s*]", "]", j2)
        return json.loads(j2)


def processar_projeto(slug: str, source: str = "auto") -> dict:
    t0 = time.time()
    if source == "drive":
        texto, fontes = coletar_fontes_drive(slug)
    elif source == "exec":
        texto, fontes = coletar_fonte_exec(slug)
    else:  # auto — tenta drive, se vazio cai pra exec
        texto, fontes = coletar_fontes_drive(slug)
        if len(texto) < 200:
            texto, fontes = coletar_fonte_exec(slug)

    if len(texto) < 100:
        return {"slug": slug, "erro": "fontes vazias", "duration_s": round(time.time() - t0, 1)}

    prompt = PROMPT_TEMPLATE.format(texto=texto)
    try:
        raw = call_gemma(prompt)
        meta = parse_json(raw)
    except Exception as e:
        return {"slug": slug, "erro": f"gemma falhou: {str(e)[:200]}",
                "duration_s": round(time.time() - t0, 1)}

    result = {
        "slug": slug,
        "fontes": fontes,
        "fonte_tipo": source,
        "n_chars_texto": len(texto),
        "gemma_model": MODEL,
        "extracao_em": datetime.now().isoformat(timespec="seconds"),
        "duration_s": round(time.time() - t0, 1),
        "metadados": meta,
    }

    out = METADADOS_DIR / f"{slug}.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result


def log(e: dict):
    e.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def init_queue(source: str) -> dict:
    if QUEUE.exists():
        q = json.loads(QUEUE.read_text(encoding="utf-8"))
        # Adiciona novos projetos que não estavam na fila
        return q

    projetos = set()
    # Drive
    if PROJETOS_DIR.exists():
        for d in PROJETOS_DIR.iterdir():
            if d.is_dir() and not d.name.startswith("."):
                projetos.add(d.name)
    # Exec
    for f in IDX_DIR.glob("*.json"):
        projetos.add(f.stem)

    q = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "fase": "1-metadados",
        "items": {s: {"status": "pending"} for s in sorted(projetos)},
    }
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")
    return q


def save_queue(q: dict):
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default=None, help="1 projeto específico")
    ap.add_argument("--source", default="auto", choices=["auto", "drive", "exec"])
    ap.add_argument("--test", action="store_true", help="smoke 3 projetos")
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    if args.slug:
        r = processar_projeto(args.slug, args.source)
        print(f"=== {args.slug} ===")
        if "erro" in r:
            print(f"  ERRO: {r['erro']}")
        else:
            print(f"  OK ({r['duration_s']}s, {r['n_chars_texto']} chars, {len(r['fontes'])} fontes)")
            meta = r.get("metadados", {})
            for k in ["cidade", "uf", "tipologia", "padrao_declarado", "n_torres",
                      "n_pavimentos_total", "sistema_estrutural", "area_construida_m2"]:
                v = meta.get(k)
                if v is not None:
                    print(f"    {k}: {v}")
        return

    test_slugs = ["arthen-arboris", "thozen-electra", "alto-ribeirao"]
    if args.test:
        for s in test_slugs:
            r = processar_projeto(s, args.source)
            print(f"\n=== {s} ===")
            if "erro" in r:
                print(f"  ERRO: {r['erro']}")
            else:
                print(f"  OK ({r['duration_s']}s)")
                meta = r.get("metadados", {})
                print(f"    {json.dumps({k: v for k, v in meta.items() if v is not None}, ensure_ascii=False)[:500]}")
        return

    q = init_queue(args.source)
    pending = [s for s, v in q["items"].items()
               if v["status"] == "pending" or (args.retry_failed and v["status"] == "failed")]
    print(f"Pendentes: {len(pending)}/{len(q['items'])}", flush=True)
    t_start = time.time()

    for i, slug in enumerate(pending, start=1):
        elapsed = time.time() - t_start
        eta = (elapsed / i) * (len(pending) - i) if i > 0 else 0
        print(f"\n[{i}/{len(pending)}] {slug} (elapsed {elapsed/60:.1f}min, eta {eta/60:.1f}min)", flush=True)
        q["items"][slug] = {"status": "in_progress"}
        save_queue(q)
        try:
            r = processar_projeto(slug, args.source)
            if "erro" in r:
                q["items"][slug] = {"status": "failed", "error": r["erro"], "duration_s": r.get("duration_s")}
                log({"projeto": slug, "status": "failed", "error": r["erro"]})
                print(f"  FAIL: {r['erro']}", flush=True)
            else:
                q["items"][slug] = {"status": "done", "duration_s": r["duration_s"],
                                    "n_chars": r["n_chars_texto"], "n_fontes": len(r["fontes"])}
                log({"projeto": slug, "status": "done", "duration_s": r["duration_s"]})
                meta = r.get("metadados", {})
                resumo = {k: meta.get(k) for k in ["cidade", "uf", "tipologia", "n_pavimentos_total"]
                          if meta.get(k)}
                print(f"  OK {r['duration_s']}s | {resumo}", flush=True)
        except Exception as e:
            err = str(e)[:200]
            q["items"][slug] = {"status": "failed", "error": err}
            log({"projeto": slug, "status": "failed", "error": err})
            print(f"  CRASH: {err}", flush=True)
        save_queue(q)

    done = sum(1 for v in q["items"].values() if v["status"] == "done")
    failed = sum(1 for v in q["items"].values() if v["status"] == "failed")
    print(f"\n{'='*60}", flush=True)
    print(f"Done: {done}/{len(q['items'])} | Failed: {failed}", flush=True)


if __name__ == "__main__":
    main()
