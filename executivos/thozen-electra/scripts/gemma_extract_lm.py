"""Wrapper Gemma para extracao de listas de materiais 348_LM Electra.

Chama a API do Ollama local (http://localhost:11434/api/generate) com prompts
estruturados pra dois formatos: A (Eletrowatts totalizado) e B (QT-MAT por
pavimento). Retorna JSON no MESMO schema do parse_lista_materiais.py
(compativel com normalizar_pavimento e geradores de xlsx).

Uso como modulo:
    from gemma_extract_lm import extract_pdf
    data = extract_pdf(Path("348_LM - SPDA ... .pdf"), model="gemma4:e4b")

Uso CLI (para smoke-test):
    python gemma_extract_lm.py <pdf_path> <out_json> [--model e4b|26b]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import fitz
import httpx

OLLAMA_HOST = "http://localhost:11434"
OLLAMA_TIMEOUT = 1200.0

MODEL_E4B = "gemma4:e4b"
MODEL_26B = "gemma4:26b"

# num_ctx por modelo (gemma4:26b estoura VRAM acima de 16k no RTX 3050)
NUM_CTX_BY_MODEL = {
    MODEL_E4B: 32768,
    MODEL_26B: 16384,
}


def call_gemma(prompt: str, model: str = MODEL_E4B, num_ctx: int | None = None,
               temperature: float = 0.0) -> str:
    """Chama /api/generate do Ollama. Retorna texto puro (sem [ERRO] handling)."""
    if num_ctx is None:
        num_ctx = NUM_CTX_BY_MODEL.get(model, 16384)
    body = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": num_ctx,
            "temperature": temperature,
            "top_p": 0.9,
            "repeat_penalty": 1.15,
        },
    }
    with httpx.Client(timeout=OLLAMA_TIMEOUT) as client:
        r = client.post(f"{OLLAMA_HOST}/api/generate", json=body)
    r.raise_for_status()
    return r.json().get("response", "").strip()


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(.+?)\s*```", re.DOTALL)


def extract_json(text: str) -> dict:
    """Extrai JSON de uma resposta Gemma. Lida com fences ``` e texto ao redor."""
    if not text:
        raise ValueError("resposta vazia")
    # Tenta fence primeiro
    m = _JSON_FENCE_RE.search(text)
    candidate = m.group(1) if m else text
    # Tenta parse direto
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    # Encontrar primeira { e ultimo } balanceado
    start = candidate.find("{")
    if start < 0:
        raise ValueError(f"sem JSON detectado: {text[:200]}")
    depth = 0
    end = -1
    in_str = False
    esc = False
    for i in range(start, len(candidate)):
        ch = candidate[i]
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end < 0:
        raise ValueError(f"JSON incompleto: {text[:200]}")
    return json.loads(candidate[start:end])


def call_gemma_json(prompt: str, model: str, max_retries: int = 3) -> dict:
    """Chama Gemma e extrai JSON com retry."""
    last_err = None
    for attempt in range(max_retries):
        text = call_gemma(prompt, model=model, temperature=0.0)
        try:
            return extract_json(text)
        except (ValueError, json.JSONDecodeError) as e:
            last_err = e
            # Reforca instrucao de JSON puro no retry
            prompt = (
                prompt
                + "\n\nATENCAO: sua resposta anterior nao foi JSON valido. "
                + "Responda APENAS com JSON valido entre ```json ... ```, "
                + "sem nenhum texto explicativo antes ou depois."
            )
    raise ValueError(f"Gemma falhou em retornar JSON valido apos {max_retries} tentativas: {last_err}")


# -------------------- Prompts --------------------

PROMPT_FORMAT_B = """Voce e um extrator de listas de materiais. Abaixo esta o texto de UMA pagina
de um PDF "QUANTITATIVO DE MATERIAIS" (sistema QT-MAT, Eletrowatts). Cada
pagina representa UM documento independente referente a um pavimento especifico
da obra Residencial Electra Towers.

Extraia TODOS os itens da tabela na ordem em que aparecem. A tabela tem 5
colunas: # | CODIGO | QTD | UN | DESCRICAO. Ignore rodapes ("Gerado em", "rel:",
"VD-X", "X de Y").

Retorne JSON valido no formato EXATO:
```json
{{
  "metadata": {{
    "codigo": "QT-MAT-XXXX",
    "referente": "<texto apos REFERENTE:>",
    "cliente": "<texto apos CLIENTE:>",
    "projeto": "<texto apos PROJETO:>",
    "localizacao": "<texto apos LOCALIZACAO:>",
    "solicitacao": "<data apos SOLICITACAO:>",
    "disciplina": "<texto apos DISCIPLINA:>"
  }},
  "itens": [
    {{"numero": 1, "codigo": "2020 00 000", "qtd": 61, "unidade": "un",
      "descricao": "..."}}
  ],
  "total_itens": <int>
}}
```

REGRAS:
- Preserve codigos EXATAMENTE como aparecem (espacos inclusos).
- qtd SEMPRE numero (int ou float, sem aspas); vira ponto decimal.
- unidade em minuscula (un, m, m2, m3, kg, cj, pc).
- descricao: texto completo do item sem quebras; se o PDF quebra em linhas,
  concatene com espaco.
- NUNCA invente itens. Se nao conseguir ler, deixe a lista vazia.
- metadata.codigo deve ser exatamente "QT-MAT-XXXX" (remover prefixos).
- Responda SOMENTE com o JSON em bloco ```json ... ```.

TEXTO DA PAGINA:
<<<
{page_text}
>>>"""


PROMPT_FORMAT_A = """Voce e um extrator de listas de materiais. Abaixo esta o texto completo de um
PDF "LISTA DE MATERIAS" template manual Eletrowatts. Diferentes PDFs usam
LAYOUTS DIFERENTES de tabela. Antes de extrair, IDENTIFIQUE as colunas do
header. Possibilidades ja observadas:

  Layout A1 (simples): ITEM | QUANT. | UNID. | DIMENSOES | ESPECIFICACAO
  Layout A2 (com cod): ITEM | COD. | QUANT. | UNID. | PRODUTO | MARCA/REFERENCIA
  Layout A3 (hidro):   ITEM | QUANT. | PRODUTO | DIAM. | MARCA/REFERENCIA
  Layout A4 (curto):   ITEM | QUANT. | UNID. | PRODUTO | MARCA/REFERENCIA
  Layout A5 (minimo):  ITEM | QUANT. | PRODUTO

Encontre a linha do header (tem palavras-chave ITEM, QUANT, PRODUTO etc) e
descubra QUAIS colunas existem e em QUE ORDEM. Cada item comeca com um
numero inteiro na primeira coluna (ITEM) e ocupa linhas consecutivas na
ordem das colunas do header.

ATENCAO - ERROS COMUNS:
- CODIGO (ex: "8502") NAO e quantidade. So vai no campo "codigo" se existir.
- QUANT e a coluna que tem numeros tipo "30", "180", "2,5" (pequenos).
- Numeros de 4 digitos consecutivos (8502, 5107) geralmente sao codigos.
- O numero do ITEM pode pular (4, 5, 7, 11, ...) porque e uma lista agrupada.
  Preserve os numeros literais do PDF, NAO renumere.

Retorne JSON valido no formato EXATO:
```json
{{
  "metadata": {{
    "sistema": "<ex: SPDA COMPLETO, HIDRO-CONEXOES, PPCI-SHP>",
    "data": "<DD/MM/AAAA ou null>",
    "relacionado_por": "<nome ou null>",
    "solicitado_por": "<nome ou null>",
    "projeto": "<num ou texto>",
    "layout_detectado": "<A1|A2|A3|A4|A5>",
    "colunas_header": ["ITEM","COD.","QUANT.","UNID.","PRODUTO","MARCA"]
  }},
  "itens": [
    {{"numero": 4, "codigo": "8502", "qtd": 30, "unidade": "pc",
      "dimensoes": null, "produto": "RE-BARS - BARRAS REDONDAS ...",
      "marca": "TEL-768", "especificacao_local": null}}
  ],
  "total_itens": <int>
}}
```

REGRAS:
- qtd SEMPRE numero (int/float, sem aspas); virgula vira ponto.
- numero SEMPRE o numero literal do ITEM no PDF (inteiro).
- Se uma coluna nao existe no layout, use null (nao omita o campo).
- unidade em minuscula (pc, un, m, m2, m3, kg, cj).
- codigo: string EXATA (sem espacos extras), ou null.
- produto: descricao completa SEM quebras de linha.
- marca: texto apos o produto na coluna MARCA/REFERENCIA, ou null.
- NUNCA invente itens. NUNCA renumere. Se um item tem qtd ilegivel, use null.
- NAO duplique itens com mesmo numero.
- Responda SOMENTE com o JSON em bloco ```json ... ```.

TEXTO DO PDF:
<<<
{pdf_text}
>>>"""


# -------------------- Extracao por formato --------------------

def _pdf_pages(pdf_path: Path) -> list[str]:
    doc = fitz.open(pdf_path)
    pages = [pg.get_text() for pg in doc]
    doc.close()
    return pages


def _detect_format(full_text: str) -> str:
    if "QUANTITATIVO DE MATERIAIS" in full_text and "QT-MAT" in full_text:
        return "B"
    return "A"


def extract_format_b(pdf_path: Path, model: str) -> dict:
    """Extrai PDF formato B (QT-MAT) pagina-a-pagina via Gemma.

    Multi-pagina: detecta "X de Y" no header. Se Y > 1, concatena paginas do
    mesmo documento antes de mandar. Paginas sem "QUANTITATIVO DE MATERIAIS"
    sao ignoradas (rodapes, capas).
    """
    pages = _pdf_pages(pdf_path)
    documentos = []
    i = 0
    while i < len(pages):
        page_text = pages[i]
        if "QUANTITATIVO DE MATERIAIS" not in page_text:
            i += 1
            continue
        # Detecta "X de Y" no header
        m = re.search(r"(\d+)\s+de\s+(\d+)", page_text[:500])
        total_partes = int(m.group(2)) if m else 1
        # Coleta todas as partes
        bloco = page_text
        partes_consumidas = 1
        j = i + 1
        while partes_consumidas < total_partes and j < len(pages):
            bloco += "\n" + pages[j]
            partes_consumidas += 1
            j += 1
        # Chama Gemma
        prompt = PROMPT_FORMAT_B.format(page_text=bloco[:80000])  # cap 80k chars
        start = time.time()
        try:
            doc = call_gemma_json(prompt, model=model, max_retries=3)
            doc["_gemma_elapsed_s"] = round(time.time() - start, 1)
            doc["_page_range"] = f"{i+1}-{j if total_partes > 1 else i+1}"
            documentos.append(doc)
        except Exception as e:
            documentos.append({
                "_error": str(e),
                "_page_range": f"{i+1}-{j if total_partes > 1 else i+1}",
                "metadata": {},
                "itens": [],
                "total_itens": 0,
            })
        i = j if total_partes > 1 else i + 1

    total = sum(d.get("total_itens", 0) for d in documentos)
    return {
        "pdf_origem": pdf_path.name,
        "formato": "B",
        "extractor": "gemma",
        "model": model,
        "documentos": documentos,
        "total_itens": total,
        "total_documentos": len(documentos),
    }


def extract_format_a(pdf_path: Path, model: str) -> dict:
    """Extrai PDF formato A (Eletrowatts manual) em uma unica chamada Gemma."""
    pages = _pdf_pages(pdf_path)
    full_text = "\n".join(pages)
    # Truncate pra caber em num_ctx
    # gemma4:e4b @32k ~ 120k chars; gemma4:26b @16k ~ 60k chars
    max_chars = 100000 if model == MODEL_E4B else 55000
    text = full_text[:max_chars]
    prompt = PROMPT_FORMAT_A.format(pdf_text=text)
    start = time.time()
    try:
        doc = call_gemma_json(prompt, model=model, max_retries=3)
        doc["_gemma_elapsed_s"] = round(time.time() - start, 1)
    except Exception as e:
        doc = {
            "_error": str(e),
            "metadata": {},
            "itens": [],
            "total_itens": 0,
            "pareamento_consistente": False,
        }
    return {
        "pdf_origem": pdf_path.name,
        "formato": "A",
        "extractor": "gemma",
        "model": model,
        "documentos": [doc],
        "total_itens": doc.get("total_itens", 0),
        "pareamento_consistente": doc.get("pareamento_consistente", False),
    }


def extract_pdf(pdf_path: Path, model: str = MODEL_E4B) -> dict:
    pages = _pdf_pages(pdf_path)
    full_text = "\n".join(pages)
    fmt = _detect_format(full_text)
    if fmt == "B":
        return extract_format_b(pdf_path, model)
    return extract_format_a(pdf_path, model)


# -------------------- CLI (smoke-test) --------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("out_json", type=Path)
    ap.add_argument("--model", choices=["e4b", "26b"], default="e4b")
    args = ap.parse_args()

    model = MODEL_E4B if args.model == "e4b" else MODEL_26B
    print(f"[extract] {args.pdf.name} via {model}")
    start = time.time()
    data = extract_pdf(args.pdf, model=model)
    elapsed = time.time() - start

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    fmt = data["formato"]
    total = data["total_itens"]
    n_docs = len(data["documentos"])
    print(f"[done] formato={fmt} docs={n_docs} total_itens={total} "
          f"elapsed={elapsed:.1f}s -> {args.out_json}")


if __name__ == "__main__":
    main()
