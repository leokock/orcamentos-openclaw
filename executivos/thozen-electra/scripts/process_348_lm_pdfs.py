"""Orquestrador: processa os 21 PDFs 348_LM Electra via Gemma + parser deterministico.

Para cada PDF da pasta `15. Listas de quantitativos/` com prefixo `348_LM`:
  1. Resolve disciplina a partir do nome do arquivo
  2. Extrai via Gemma (gemma_extract_lm.extract_pdf)
  3. Extrai via parser deterministico (parse_lista_materiais.build_structured)
  4. Salva ambos JSONs em quantitativos/listas-materiais-348/{disciplina}/
  5. Aplica normalizar_pavimento nos itens de formato B
  6. Gera linha no relatorio de comparacao

Suporta --resume (pula PDFs ja processados), --only-pdf, --disciplina, --model.

Uso:
    python scripts/process_348_lm_pdfs.py                         # batch total
    python scripts/process_348_lm_pdfs.py --disciplina hidraulico  # so HIDRO
    python scripts/process_348_lm_pdfs.py --only-pdf "SPDA"        # so SPDA
    python scripts/process_348_lm_pdfs.py --resume                 # skip existentes
    python scripts/process_348_lm_pdfs.py --model 26b              # usa gemma4:26b
    python scripts/process_348_lm_pdfs.py --no-gemma               # so parser det.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

# Paths
PROJETOS_DIR = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Projetos_IA\thozen-electra\projetos\15. Listas de quantitativos")
EXEC_DIR = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra")
OUT_DIR = EXEC_DIR / "quantitativos" / "listas-materiais-348"
SCRIPTS_DIR = EXEC_DIR / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
import gemma_extract_lm as gem
import parse_lista_materiais as parser_det
import normalizar_pavimento as norm


# Mapeamento nome PDF -> (disciplina_dir, slug)
# As 6 disciplinas afetadas pelos 21 PDFs 348_LM.
DISC_MAP: dict[str, tuple[str, str]] = {
    # ELE
    "348_LM - ELE - rev.00 - ACABAMENTOS.pdf":                 ("eletrico", "ele-acabamentos"),
    "348_LM - ELE - rev.00 - CABOS DE ALIMENTAÇÃO_APTO-QM.pdf": ("eletrico", "ele-cabos-alim"),
    "348_LM - ELE - rev.00 - ELETROCALHAS.pdf":                ("eletrico", "ele-eletrocalhas"),
    "348_LM - ELE - rev.00 - ENFIAÇÕES.pdf":                   ("eletrico", "ele-enfiacoes"),
    "348_LM - ELE - rev.00 - ILUMINAÇÕES.pdf":                 ("eletrico", "ele-iluminacoes"),
    "348_LM - ELE - rev.00 - TUBULAÇÕES DE PAREDE_TETO.pdf":   ("eletrico", "ele-tubulacoes"),
    # HIDRO
    "348_LM - HIDRO - rev.00_ELC - CONEXÕES TUBOS.pdf":        ("hidraulico", "hidro-conexoes"),
    "348_LM - HIDRO - rev.00_ELC - ETE e CX. GORDURA.pdf":     ("hidraulico", "hidro-ete"),
    "348_LM - HIDRO - rev.00_ELC - TUBULAÇÕES.pdf":            ("hidraulico", "hidro-tubulacoes"),
    "348_LM - HIDRO - rev.00_ELC - VÁLVULAS, MOTOBOMBAS.pdf":  ("hidraulico", "hidro-valvulas"),
    # PPCI Civil
    "348_LM - PPCI - rev.00_ELC - SISTEMA GERAIS.pdf":         ("ppci-civil", "ppci-gerais"),
    "348_LM - PPCI - rev.00_ELC - SISTEMA IGC.pdf":            ("ppci-civil", "ppci-igc"),
    "348_LM - PPCI - rev.00_ELC - SISTEMA MECÂNICO.pdf":       ("ppci-civil", "ppci-mecanico"),
    "348_LM - PPCI - rev.00_ELC - SISTEMA SHP.pdf":            ("ppci-civil", "ppci-shp"),
    # PPCI Eletrico
    "348_LM - PPCI-ELÉ - rev. 00 - TUBULAÇÕES DE PAREDE_TETO.pdf": ("ppci-eletrico", "ppcie-tubulacoes"),
    "348_LM - PPCI-ELÉ - rev.00 - ACABAMENTOS.pdf":            ("ppci-eletrico", "ppcie-acabamentos"),
    "348_LM - PPCI-ELÉ - rev.00 - ENFIAÇÕES.pdf":              ("ppci-eletrico", "ppcie-enfiacoes"),
    # SPDA
    "348_LM - SPDA - rev.00_ELC - COMPLETO.pdf":               ("spda", "spda-completo"),
    # TEL
    "348_LM - TEL - rev.00 - ACABAMENTOS.pdf":                 ("telefonico", "tel-acabamentos"),
    "348_LM - TEL - rev.00 - ELETROCALHAS.pdf":                ("telefonico", "tel-eletrocalhas"),
    "348_LM - TEL - rev.00 - TUBULAÇÕES DE PAREDE_TETO.pdf":   ("telefonico", "tel-tubulacoes"),
}


def log(msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def normalizar_gemma_output(data: dict) -> dict:
    """Aplica normalizar_pavimento nos itens do output Gemma (formato A ou B).

    Formato B: cada documento ja tem metadata.localizacao -> normaliza.
    Formato A: pode nao ter pavimento (fica NA) -> vai pra Fase 3 de rateio.
    """
    for doc in data.get("documentos", []):
        meta = doc.get("metadata") or {}
        # Source de texto pra normalizacao
        src_text = " ".join([
            str(meta.get("localizacao") or ""),
            str(meta.get("referente") or ""),
            str(meta.get("sistema") or ""),
        ])
        pav_info = norm.normalizar(src_text) if src_text.strip() else {"pavimento": "NA", "torre": "NA", "original": ""}
        meta["pavimento_canonico"] = pav_info["pavimento"]
        meta["torre_canonica"] = pav_info["torre"]
        doc["metadata"] = meta
    return data


def process_one(pdf_name: str, disciplina: str, slug: str, *,
                model: str, resume: bool, no_gemma: bool) -> dict:
    pdf_path = PROJETOS_DIR / pdf_name
    if not pdf_path.exists():
        return {"pdf": pdf_name, "error": f"PDF nao encontrado: {pdf_path}"}

    out_dir = OUT_DIR / disciplina
    out_dir.mkdir(parents=True, exist_ok=True)
    gemma_path = out_dir / f"{slug}.gemma.json"
    parser_path = out_dir / f"{slug}.parser.json"

    result = {"pdf": pdf_name, "disciplina": disciplina, "slug": slug}

    # 1. Parser deterministico (sempre rapido)
    if resume and parser_path.exists():
        log(f"  [parser] skip (cache) {pdf_name}")
    else:
        log(f"  [parser] {pdf_name}")
        t0 = time.time()
        try:
            parser_data = parser_det.build_structured(pdf_path)
            parser_path.write_text(
                json.dumps(parser_data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
            log(f"  [parser] done fmt={parser_data['formato']} n={parser_data['total_itens']} ({time.time()-t0:.0f}s)")
        except Exception as e:
            log(f"  [parser] FAIL: {e}")
            result["parser_error"] = str(e)

    if parser_path.exists():
        try:
            pd = json.loads(parser_path.read_text(encoding="utf-8"))
            result["parser_n_itens"] = pd.get("total_itens", 0)
            result["parser_formato"] = pd.get("formato")
        except Exception:
            pass

    # 2. Gemma
    if no_gemma:
        return result

    if resume and gemma_path.exists():
        log(f"  [gemma]  skip (cache) {pdf_name}")
    else:
        log(f"  [gemma]  {pdf_name} @ {model}")
        t0 = time.time()
        try:
            gemma_data = gem.extract_pdf(pdf_path, model=model)
            gemma_data = normalizar_gemma_output(gemma_data)
            gemma_path.write_text(
                json.dumps(gemma_data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
            log(f"  [gemma]  done fmt={gemma_data['formato']} n={gemma_data['total_itens']} docs={len(gemma_data['documentos'])} ({time.time()-t0:.0f}s)")
        except Exception as e:
            log(f"  [gemma]  FAIL: {e}")
            result["gemma_error"] = str(e)

    if gemma_path.exists():
        try:
            gd = json.loads(gemma_path.read_text(encoding="utf-8"))
            result["gemma_n_itens"] = gd.get("total_itens", 0)
            result["gemma_formato"] = gd.get("formato")
            result["gemma_docs"] = len(gd.get("documentos", []))
        except Exception:
            pass

    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--disciplina", choices=sorted(set(v[0] for v in DISC_MAP.values())),
                    help="Processa so uma disciplina")
    ap.add_argument("--only-pdf", help="Substring para filtrar pdfs (case-sensitive em parte do nome)")
    ap.add_argument("--model", choices=["e4b", "26b"], default="e4b")
    ap.add_argument("--resume", action="store_true", help="Pula PDFs ja processados")
    ap.add_argument("--no-gemma", action="store_true", help="So roda parser deterministico")
    args = ap.parse_args()

    model = gem.MODEL_E4B if args.model == "e4b" else gem.MODEL_26B

    # Filtrar PDFs
    pdfs = list(DISC_MAP.items())
    if args.disciplina:
        pdfs = [(n, v) for n, v in pdfs if v[0] == args.disciplina]
    if args.only_pdf:
        pdfs = [(n, v) for n, v in pdfs if args.only_pdf in n]

    log(f"Processando {len(pdfs)} PDFs (model={model}, resume={args.resume}, no_gemma={args.no_gemma})")
    log(f"Output: {OUT_DIR}")
    log("")

    results = []
    t_start = time.time()
    for i, (pdf_name, (disciplina, slug)) in enumerate(pdfs, 1):
        log(f"[{i}/{len(pdfs)}] {disciplina}/{slug}")
        r = process_one(
            pdf_name, disciplina, slug,
            model=model, resume=args.resume, no_gemma=args.no_gemma,
        )
        results.append(r)
        log("")

    elapsed = time.time() - t_start
    log(f"==== CONCLUIDO em {elapsed/60:.1f} min ====")
    log("")
    log("Sumario:")
    log(f"{'PDF':<60} {'parser':>8} {'gemma':>8} {'delta':>8}")
    for r in results:
        pn = r.get("parser_n_itens", "-")
        gn = r.get("gemma_n_itens", "-")
        if isinstance(pn, int) and isinstance(gn, int) and pn > 0:
            delta = f"{(gn-pn)/pn*100:+.0f}%"
        else:
            delta = "-"
        log(f"{r['pdf'][:58]:<60} {str(pn):>8} {str(gn):>8} {delta:>8}")

    # Salvar sumario JSON
    summary_path = OUT_DIR / "process-summary.json"
    summary_path.write_text(
        json.dumps({"timestamp": datetime.now().isoformat(),
                    "elapsed_s": elapsed,
                    "model": model,
                    "results": results}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    log(f"Sumario salvo: {summary_path}")


if __name__ == "__main__":
    main()
