"""Enriquece JSONs de listas-materiais com campos `pavimento` e `torre`
derivados, aplicando normalizar_pavimento nos textos crus dos itens.

Regras:
- Formato A: primeiro tenta especificacao_local; se pavimento=NA, fallback produto.
- Formato B: usa localizacao+referente (referente tem prioridade pra torre,
  porque o projetista errou a localizacao em pelo menos 1 doc QT-MAT-1950).
- Para Aprovativo (16 quadros gerais): sem pavimento no original. Aplicamos
  fallback TERREO (convencao: quadros principais na subestacao/terreo) e
  extraimos torre do produto.

Saida: sobrescreve os JSONs de entrada adicionando chaves `pavimento` e
`torre` em cada item, + `pavimento_documento`/`torre_documento` em formato B.

Tambem corrige o item NA do Executivo (numero 15, dim ausente).
"""
import json
import sys
from pathlib import Path

BASE = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\quantitativos\listas-materiais")
sys.path.insert(0, str(Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\scripts")))
from normalizar_pavimento import normalizar


def enriquecer_formato_a(data: dict, fallback_pav: str | None = None) -> dict:
    for doc in data["documentos"]:
        for it in doc["itens"]:
            loc = it.get("especificacao_local") or ""
            n = normalizar(loc)
            # Se NA e tem produto, tenta fallback no produto
            if n["pavimento"] == "NA" and it.get("produto"):
                n2 = normalizar(it["produto"])
                if n2["pavimento"] != "NA":
                    n = n2
                elif n2["torre"] != "NA":
                    n["torre"] = n2["torre"]
            # Fallback final por aplicacao (aprovativo: quadros gerais -> TERREO)
            if n["pavimento"] == "NA" and fallback_pav:
                n["pavimento"] = fallback_pav
                n["pavimento_label"] = f"{fallback_pav} (fallback — quadro geral)"
            it["pavimento"] = n["pavimento"]
            it["torre"] = n["torre"]
            it["pavimento_label"] = n["pavimento_label"]
    return data


def enriquecer_formato_b(data: dict) -> dict:
    for doc in data["documentos"]:
        meta = doc["metadata"]
        loc_meta = meta.get("localizacao") or ""
        ref_meta = meta.get("referente") or ""
        # Pavimento: prioridade na localizacao do documento
        n_pav = normalizar(loc_meta)
        # Torre: prioridade no referente (projetista errou localizacao em 1 doc)
        n_torre_ref = normalizar(ref_meta)
        torre = n_torre_ref["torre"] if n_torre_ref["torre"] != "NA" else n_pav["torre"]

        doc["pavimento"] = n_pav["pavimento"]
        doc["torre"] = torre
        doc["pavimento_label"] = n_pav["pavimento_label"]

        for it in doc["itens"]:
            it["pavimento"] = n_pav["pavimento"]
            it["torre"] = torre
            it["pavimento_label"] = n_pav["pavimento_label"]
    return data


def corrigir_executivo_item15(data: dict) -> dict:
    """Item 15 do Executivo tem dim ausente e o parser desalinhou,
    capturando '16' como especificacao_local. A linha real diz:
    '15\\n1\\npç\\n01° PV. TÉRREO - TORRE B' (dim pulada — projetista nao preencheu).
    Corrigir manualmente com pavimento=TERREO torre=B."""
    for doc in data["documentos"]:
        for it in doc["itens"]:
            if it.get("especificacao_local") == "16":
                it["especificacao_local"] = "01° PV. TÉRREO - TORRE B (item 15 dim ausente no PDF)"
                it["pavimento"] = "TERREO"
                it["torre"] = "B"
                it["pavimento_label"] = "01º Térreo"
                it["correcao_manual"] = True
    return data


def main():
    arquivos = [
        ("telecom/telecom.json", "A", None),
        ("spda/spda.json", "A", None),
        ("eletrico/aprovativo.json", "A", "TERREO"),  # quadros gerais -> terreo
        ("eletrico/executivo.json", "A", None),
        ("eletrico/preventivo.json", "A", None),
        ("eletrico/geral.json", "B", None),
        ("eletrico/disjuntores.json", "B", None),
    ]

    for rel, fmt, fallback in arquivos:
        path = BASE / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        if fmt == "A":
            data = enriquecer_formato_a(data, fallback_pav=fallback)
        else:
            data = enriquecer_formato_b(data)
        if "executivo" in rel:
            data = corrigir_executivo_item15(data)

        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        # Estatistica
        itens = []
        for doc in data["documentos"]:
            itens.extend(doc.get("itens", []))
        coberto = sum(1 for it in itens if it.get("pavimento") and it["pavimento"] != "NA")
        print(f"  {rel:30s} fmt={fmt} itens={len(itens):4d} coberto_pav={coberto}/{len(itens)}")


if __name__ == "__main__":
    main()
