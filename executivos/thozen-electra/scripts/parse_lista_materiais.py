"""Parser para listas de materiais Eletrowatts (PDFs Thozen Electra).

Suporta 2 formatos detectados automaticamente:

FORMATO A (template manual — Aprovativo, Executivo, Preventivo, SPDA, Telecom):
- Cabecalho: ITEM | QUANT. | UNID. | DIMENSOES | ESPECIFICACAO
- Descricoes de PRODUTO em bloco separado "DADOS DOS PRODUTOS"
- Pareamento posicional (N-esimo item <-> N-esima descricao)

FORMATO B (sistema QT-MAT — Geral, Disjuntores):
- "QUANTITATIVO DE MATERIAIS" + "CODIGO: QT-MAT-NNNN"
- Cabecalho: # | CODIGO | QTD | UN | DESCRICAO (inline, 5 colunas)
- Multi-pagina: cada pagina e um "documento" independente com metadata propria
  (REFERENTE, LOCALIZACAO, DISCIPLINA)

Output JSON:
{
  "pdf_origem": "...",
  "formato": "A" | "B",
  "documentos": [ { "metadata": {...}, "itens": [...] } ],
  "total_itens": N,
  "pareamento_consistente": bool (so formato A)
}

Uso:
    python parse_lista_materiais.py <pdf_path> <output_json>
"""
import json
import re
import sys
from pathlib import Path

import fitz

UNITS = {"pc", "pç", "pca", "peca", "peça", "un", "uni", "m", "m2", "m3", "kg", "cj"}
STOPWORDS_HEADER = {
    "RELACIONADO POR:", "SOLICITADO POR:", "DATA:", "ITEM", "QUANT. UNID.",
    "DIMENSÕES", "ESPECIFICAÇÃO", "REFERENTE:", "CLIENTE:", "OBRA:",
    "OBSERVAÇÕES:", "DADOS DOS PRODUTOS", "PRODUTO", "LISTA DE MATERIAS",
    "QUANTITATIVO DE MATERIAIS", "LISTA DE MATERIAIS", "PROJETO:",
    "LOCALIZAÇÃO:", "SOLICITAÇÃO:", "DISCIPLINA:", "#", "CÓDIGO", "QTD",
    "UN", "DESCRIÇÃO", "OBSERVAÇÃO:",
}
ROD_RE = re.compile(
    r"eletrowatts|3368\.3312|Morretes|Trabalhando para iluminar|"
    r"DIMENSÕES:\s*LARGURA|Gerado em:|rel:|VD-\d|^\d+\s+de\s+\d+$",
    re.IGNORECASE | re.MULTILINE,
)


def extract_pdf_pages(pdf_path: Path) -> list[str]:
    doc = fitz.open(pdf_path)
    pages = [pg.get_text() for pg in doc]
    doc.close()
    return pages


def detect_format(full_text: str) -> str:
    if "QUANTITATIVO DE MATERIAIS" in full_text and "QT-MAT" in full_text:
        return "B"
    return "A"


# -------------------- Formato A --------------------

def _is_unit_a(token: str) -> bool:
    return token.strip().lower().replace(".", "") in UNITS


PLACEHOLDER_PATTERNS = (
    "VERIFICAR DIAGRAMA", "VERIFICAR IMAGEM", "VERIFICAR PLANTA",
    "VERIFICAR PROJETO", "VER DIAGRAMA", "VER PROJETO",
)


def _is_structured_line_a(s: str) -> bool:
    if not s:
        return True
    if s in STOPWORDS_HEADER:
        return True
    if s.startswith(("RELACIONADO POR", "SOLICITADO POR", "DATA:", "REFERENTE:",
                     "CLIENTE:", "OBRA:", "OBSERVAÇÕES:", "DADOS DOS PRODUTOS",
                     "LISTA DE MATERIAS", "PRODUTO")):
        return True
    if ROD_RE.search(s):
        return True
    if re.fullmatch(r"\d+", s):
        return True
    if re.fullmatch(r"\d+([.,]\d+)?", s):
        return True
    if _is_unit_a(s):
        return True
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", s):
        return True
    # Placeholder tipo "VERIFICAR DIAGRAMA" (aparece nas colunas DIM/ESPEC quando
    # o projetista remete ao desenho principal)
    upper = s.upper()
    if any(p in upper for p in PLACEHOLDER_PATTERNS) and len(s) < 40:
        return True
    return False


def _looks_like_dimension(s: str) -> bool:
    return bool(re.search(r"\d+\s*[xX]\s*\d+", s))


def _looks_like_local(s: str) -> bool:
    return bool(re.search(
        r"\b(BLOCO|T[EÉ]RREO|TIPO|LAZER|PAVIMENTO|PAV\.?|G\d|C\.\s*P\.|C\.\s*M[AÁ]Q)\b",
        s.upper(),
    ))


def parse_formato_a(full_text: str, pdf_name: str) -> dict:
    lines = [l.rstrip() for l in full_text.splitlines()]

    # Metadata global
    meta = {"data": None, "referente": None, "cliente": None, "obra": None}
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("DATA:"):
            rest = s.replace("DATA:", "").strip()
            if rest:
                meta["data"] = rest
            elif i + 1 < len(lines):
                nxt = lines[i + 1].strip()
                if re.match(r"\d{2}/\d{2}/\d{4}", nxt):
                    meta["data"] = nxt
        elif s.startswith("REFERENTE:"):
            meta["referente"] = s.replace("REFERENTE:", "").strip() or None
        elif s.startswith("CLIENTE:"):
            meta["cliente"] = s.replace("CLIENTE:", "").strip() or None
        elif s.startswith("OBRA:"):
            meta["obra"] = s.replace("OBRA:", "").strip() or None

    # Parse itens
    items: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if re.fullmatch(r"\d+", line):
            num = int(line)
            if i + 4 < len(lines):
                qtd_line = lines[i + 1].strip()
                unid_line = lines[i + 2].strip()
                dim_line = lines[i + 3].strip()
                espec_line = lines[i + 4].strip()
                if (
                    re.fullmatch(r"\d+([.,]\d+)?", qtd_line)
                    and _is_unit_a(unid_line)
                    and dim_line
                    and espec_line
                ):
                    items.append({
                        "numero": num,
                        "qtd": float(qtd_line.replace(",", ".")),
                        "unidade": unid_line.replace(".", "").lower(),
                        "dimensoes": dim_line,
                        "especificacao_local": espec_line,
                    })
                    i += 5
                    continue
            i += 1
            continue
        i += 1

    # Coletar descricoes PRODUTO = linhas nao-estruturadas. Em vez de usar heuristicas
    # fragias (look_like_local/dimension), subtrair exatamente os valores que ja foram
    # consumidos como dimensoes/especificacao_local dos itens.
    consumidos = set()
    for it in items:
        consumidos.add(it["dimensoes"])
        consumidos.add(it["especificacao_local"])
    produtos_raw: list[str] = []
    consumo_count: dict[str, int] = {}
    for l in lines:
        s = l.strip()
        if _is_structured_line_a(s):
            continue
        if s in consumidos:
            # Subtrai UMA ocorrencia por item que a consumiu. Como consumidos pode ter
            # o mesmo valor repetido (ex: todos itens com dim=VERIFICAR DIAGRAMA),
            # rastreamos quantas vezes ja descontamos.
            n = sum(1 for it in items if it["dimensoes"] == s or it["especificacao_local"] == s)
            consumo_count.setdefault(s, 0)
            if consumo_count[s] < n:
                consumo_count[s] += 1
                continue
        produtos_raw.append(s)

    # Merge heuristico (quebras de linha)
    produtos: list[str] = []
    buffer = ""
    for s in produtos_raw:
        end = buffer.rstrip()
        should_merge = bool(buffer) and (
            end.endswith(("+", "/", ","))
            or (end.endswith("-") and not end.endswith(" -"))
            or (s and s[0].islower())
        )
        if should_merge:
            buffer = end + " " + s
        else:
            if buffer:
                produtos.append(buffer.strip())
            buffer = s
    if buffer:
        produtos.append(buffer.strip())

    # Dedup produtos: se aparecem mais vezes que itens (ruido por multi-pagina),
    # truncar/dedup. Estrategia: se len(produtos) > 2 * len(items), pegar unicos na
    # ordem de primeira aparicao.
    if len(produtos) > len(items) * 2 and items:
        seen = {}
        for p in produtos:
            seen.setdefault(p, 0)
            seen[p] += 1
        # Filtrar: manter os produtos com mais ocorrencias = provaveis PRODUTOs reais
        produtos = [p for p, _ in sorted(seen.items(), key=lambda x: -x[1])]

    # Pareamento posicional
    itens_com_produto = []
    for idx, it in enumerate(items):
        prod = produtos[idx] if idx < len(produtos) else None
        itens_com_produto.append({**it, "produto": prod})

    return {
        "pdf_origem": pdf_name,
        "formato": "A",
        "documentos": [
            {
                "metadata": meta,
                "total_itens": len(items),
                "total_descricoes_produto": len(produtos),
                "pareamento_consistente": len(items) == len(produtos),
                "itens": itens_com_produto,
                "produtos_nao_pareados": produtos[len(items):] if len(produtos) > len(items) else [],
            }
        ],
        "total_itens": len(items),
        "pareamento_consistente": len(items) == len(produtos),
    }


# -------------------- Formato B --------------------

def parse_formato_b_page(page_text: str) -> dict:
    """Parse uma pagina do formato QT-MAT."""
    lines = [l.rstrip() for l in page_text.splitlines()]
    meta = {
        "codigo": None, "referente": None, "cliente": None,
        "projeto": None, "localizacao": None, "solicitacao": None, "disciplina": None,
    }

    def _next_value(idx: int) -> str | None:
        for j in range(idx + 1, min(idx + 4, len(lines))):
            nxt = lines[j].strip()
            if nxt:
                return nxt
        return None

    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("CÓDIGO:") and "QT-MAT" in s:
            meta["codigo"] = s.replace("CÓDIGO:", "").strip()
        elif s == "REFERENTE:":
            meta["referente"] = _next_value(i)
        elif s == "CLIENTE:":
            meta["cliente"] = _next_value(i)
        elif s == "PROJETO:":
            meta["projeto"] = _next_value(i)
        elif s == "LOCALIZAÇÃO:":
            meta["localizacao"] = _next_value(i)
        elif s == "SOLICITAÇÃO:":
            meta["solicitacao"] = _next_value(i)
        elif s == "DISCIPLINA:":
            meta["disciplina"] = _next_value(i)

    # Encontrar inicio da tabela (depois de "DESCRIÇÃO")
    start = None
    for i, l in enumerate(lines):
        if l.strip() == "DESCRIÇÃO":
            start = i + 1
            break
    if start is None:
        return {"metadata": meta, "itens": [], "total_itens": 0}

    body = lines[start:]
    items: list[dict] = []
    i = 0
    while i < len(body):
        line = body[i].strip()
        # Parar em rotulos de fim
        if line.startswith(("OBSERVAÇÃO:", "REFERENTE:")) or ROD_RE.search(line):
            break
        # Formato linha: num / codigo / qtd / un / descricao (5 linhas consecutivas)
        if re.fullmatch(r"\d+", line):
            num = int(line)
            if i + 4 < len(body):
                cod = body[i + 1].strip()
                qtd = body[i + 2].strip()
                un = body[i + 3].strip()
                desc = body[i + 4].strip()
                if (
                    re.fullmatch(r"[\d\s]+", cod)  # codigo eh so numeros e espacos
                    and re.fullmatch(r"\d+([.,]\d+)?", qtd)
                    and un and len(un) <= 4
                    and desc and len(desc) >= 5
                ):
                    items.append({
                        "numero": num,
                        "codigo": cod,
                        "qtd": float(qtd.replace(",", ".")),
                        "unidade": un.lower(),
                        "descricao": desc,
                    })
                    i += 5
                    continue
        i += 1

    return {"metadata": meta, "itens": items, "total_itens": len(items)}


def parse_formato_b(pages: list[str], pdf_name: str) -> dict:
    documentos = []
    total = 0
    for page_text in pages:
        if "QUANTITATIVO DE MATERIAIS" not in page_text:
            continue
        doc = parse_formato_b_page(page_text)
        documentos.append(doc)
        total += doc["total_itens"]
    return {
        "pdf_origem": pdf_name,
        "formato": "B",
        "documentos": documentos,
        "total_itens": total,
        "total_documentos": len(documentos),
    }


# -------------------- Main --------------------

def build_structured(pdf_path: Path) -> dict:
    pages = extract_pdf_pages(pdf_path)
    full_text = "\n".join(pages)
    fmt = detect_format(full_text)
    if fmt == "B":
        return parse_formato_b(pages, pdf_path.name)
    return parse_formato_a(full_text, pdf_path.name)


def main():
    if len(sys.argv) < 3:
        print("uso: parse_lista_materiais.py <pdf> <out_json>")
        sys.exit(1)
    pdf = Path(sys.argv[1])
    out = Path(sys.argv[2])
    data = build_structured(pdf)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    fmt = data["formato"]
    total = data["total_itens"]
    if fmt == "A":
        pareado = data["pareamento_consistente"]
        print(f"formato=A total_itens={total} pareado={pareado} -> {out}")
    else:
        ndocs = data["total_documentos"]
        print(f"formato=B docs={ndocs} total_itens={total} -> {out}")


if __name__ == "__main__":
    main()
