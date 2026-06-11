"""Resolver Cartesian via heurística determinística (sem LLM).

Portado quase 1:1 de ~/openclaw/scripts/alfa_precificar_step6b_auto_resolve.py.
Mudanças:
  - parametrizado por --slug (lê items-cartesian-{disc}.json em tmp do slug)
  - lista de disciplinas vem da estrutura executivos/[slug]/

Heurística (cada candidate top-5 é avaliado, fica com o melhor):
  alta:   score >= ~70 + unidade compat + bitola igual + categoria igual + head_noun ok
  média:  score >= 60 + unidade compat + sem conflitos graves
  baixa:  score >= 50, ou alguma penalidade (bitola/categoria/head)
  sem:    score < 50 ou nenhum candidato aceitável

Output: tmp/match-cartesian-resolved-{disc}.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from precificar_common import (
    norm_unit, units_compatible, tmp_dir, discover_disciplinas,
)


# === Heurística (mesma lógica do step6b) ===

STOPWORDS = {
    "de", "do", "da", "dos", "das", "e", "ou", "para", "em", "com", "sem",
    "o", "a", "os", "as", "no", "na", "nos", "nas", "que", "se", "ao",
    "um", "uma", "uns", "umas",
}

CATEGORIAS = {
    # PCI
    "acionador", "central", "detector", "sirene", "extintor", "hidrante", "mangueira",
    "esguicho", "tampao", "registro", "valvula", "bomba", "painel", "placa", "luminaria",
    "sinalizacao", "sprinkler", "chuveiro",
    # Sanitário
    "tubo", "luva", "joelho", "te", "junta", "juncao", "anel", "reducao", "redutor",
    "bucha", "cap", "curva", "tampa", "sifao", "ralo", "caixa", "torneira",
    "vaso", "lavatorio", "cuba", "tanque", "filtro", "hidrometro",
    "bacia", "assento", "ducha", "misturador",
    # Telecom / elétrica
    "cabo", "fio", "eletroduto", "conduite", "tomada", "interruptor", "disjuntor",
    "quadro", "fita", "conector", "distribuidor", "ponto",
}

CATEGORY_SYNONYMS = {
    "tubulacao": "tubo", "tubos": "tubo",
    "valvulas": "valvula",
    "luvas": "luva", "joelhos": "joelho",
    "registros": "registro",
    "aneis": "anel",
    "tes": "te",
    "juncoes": "juncao", "junta": "juncao",
    "reducoes": "reducao",
}


def _norm_basic(s):
    """Normalização mais simples só pra heurística (mantém pontuação relevante)."""
    if not s:
        return ""
    import unicodedata as ud
    s = str(s).lower()
    s = ud.normalize("NFKD", s)
    s = "".join(c for c in s if not ud.combining(c))
    return re.sub(r"\s+", " ", s).strip()


def extract_bitola(s: str):
    s = _norm_basic(s)
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*mm\b", s)
    if m:
        return m.group(1).replace(",", ".") + "mm"
    m = re.search(r"(\d+\s*\.?\s*\d*/\d+)\s*[\"\']", s)
    if m:
        return m.group(1).replace(" ", "")
    m = re.search(r"\b(\d+/\d+)\b", s)
    if m:
        return m.group(1)
    m = re.search(r"\bdn\s*(\d+)", s)
    if m:
        return "dn" + m.group(1)
    return None


def extract_angulo(s: str):
    s = _norm_basic(s)
    m = re.search(r"\b(45|90|135|180|22[\s.]*5|30|60)\s*(?:o|°|graus|gr)?\b", s)
    if m:
        return m.group(1).replace(" ", "").replace(".", "")
    return None


def significant_tokens(s: str):
    return [t for t in re.findall(r"[a-z0-9]+", _norm_basic(s))
            if t not in STOPWORDS and len(t) >= 2 and not t.isdigit()]


def category_tokens(s: str):
    toks = significant_tokens(s)
    out = []
    for t in toks:
        n = CATEGORY_SYNONYMS.get(t, t)
        if n in CATEGORIAS or t in CATEGORIAS:
            out.append(n)
    return out


def specificity(s: str) -> int:
    return len(significant_tokens(s))


def head_noun(s: str):
    toks = significant_tokens(s)
    if not toks:
        return None
    return toks[0]


def category_match(alfa_desc, cand_desc):
    alfa_cats = category_tokens(alfa_desc)
    cand_cats = set(category_tokens(cand_desc))
    if not alfa_cats:
        return True, [], list(cand_cats)
    ok = any(c in cand_cats for c in alfa_cats)
    return ok, alfa_cats, list(cand_cats)


def head_noun_in_cand(alfa_desc, cand_desc):
    alfa_toks = significant_tokens(alfa_desc)
    cand_toks = set(significant_tokens(cand_desc))
    if not alfa_toks or not cand_toks:
        return False
    return alfa_toks[0] in cand_toks


def assess(alfa_desc: str, alfa_unit: str, cand: dict):
    """Retorna (confidence, reasoning_str)."""
    score = cand.get("score", 0) or 0
    cand_desc = cand.get("desc", "")
    cand_unit = cand.get("unit", "")
    if not cand_desc or score < 35:
        return "sem-match", "sem candidato adequado"

    unit_ok = units_compatible(alfa_unit, cand_unit)
    bit_alfa = extract_bitola(alfa_desc)
    bit_cand = extract_bitola(cand_desc)
    bitola_match = (bit_alfa is None and bit_cand is None) or (bit_alfa and bit_cand and bit_alfa == bit_cand)
    bitola_alfa_missing = bit_alfa is not None and bit_cand is None
    bitola_conflict = bit_alfa and bit_cand and bit_alfa != bit_cand
    ang_alfa = extract_angulo(alfa_desc)
    ang_cand = extract_angulo(cand_desc)
    ang_conflict = ang_alfa and ang_cand and ang_alfa != ang_cand
    spec_alfa = specificity(alfa_desc)
    spec_cand = specificity(cand_desc)
    cand_is_generic = spec_cand <= 2 and spec_alfa >= 3
    head_ok = head_noun_in_cand(alfa_desc, cand_desc)
    cat_ok, alfa_cats, cand_cats = category_match(alfa_desc, cand_desc)

    reasons = [f"score {score}"]
    base = "alta"
    if not unit_ok:
        base = "baixa"
        reasons.append(f"unidade diverge ({alfa_unit} vs {cand_unit})")
    if bitola_conflict:
        reasons.append(f"bitola diverge ({bit_alfa} vs {bit_cand})")
        base = "baixa"
    if ang_conflict:
        reasons.append(f"ângulo diverge ({ang_alfa}° vs {ang_cand}°)")
        base = "baixa"
    if not cat_ok:
        reasons.append(f"categoria diverge (Alfa: {alfa_cats} | cand: {cand_cats})")
        base = "baixa"
    elif not head_ok:
        h_alfa = head_noun(alfa_desc)
        reasons.append(f"substantivo principal ausente ({h_alfa!r} não está no candidato)")
        if base in ("alta", "média"):
            base = "baixa"
    if bitola_alfa_missing:
        reasons.append(f"cand não especifica bitola (Alfa: {bit_alfa})")
        if base == "alta":
            base = "média"
    if cand_is_generic:
        reasons.append(f"cand muito genérico ({spec_cand} tok vs Alfa {spec_alfa})")
        if base in ("alta", "média"):
            base = "baixa"

    if score < 50:
        return "sem-match", " | ".join(reasons + ["score baixo"])
    if score < 70 and base == "alta":
        base = "média"
    if score < 60 and base in ("alta", "média"):
        base = "baixa"
    if base == "alta" and not (unit_ok and bitola_match and not bitola_conflict and not cand_is_generic):
        base = "média"

    return base, " | ".join(reasons)


def resolve_items(items: list[dict]) -> list[dict]:
    """Para cada item, escolhe o melhor candidato dos top-5."""
    rank = {"alta": 4, "média": 3, "baixa": 2, "sem-match": 1}
    out = []
    for it in items:
        cands = it.get("candidates", [])
        alfa_desc = it["alfa_desc"]
        alfa_unit = it["alfa_unit"]
        best = None
        best_conf = "sem-match"
        best_reason = "nenhum candidato avaliado"
        best_idx = None
        for i, c in enumerate(cands, 1):
            conf, reason = assess(alfa_desc, alfa_unit, c)
            if rank[conf] > rank[best_conf] or (rank[conf] == rank[best_conf] and best is None):
                best = c
                best_conf = conf
                best_reason = reason
                best_idx = i
        if best and best_conf != "sem-match":
            out.append({
                "alfa_id": it["alfa_id"],
                "chosen": best_idx,
                "matched_desc": best["desc"],
                "matched_unit": best["unit"],
                "matched_price": best["price"],
                "obra_id": best.get("obra_id", ""),
                "obra_nome": best.get("obra_nome", ""),
                "source": best.get("source", ""),
                "date": best.get("date", ""),
                "confidence": best_conf,
                "reasoning": best_reason,
            })
        else:
            out.append({
                "alfa_id": it["alfa_id"],
                "chosen": None,
                "matched_desc": None,
                "matched_unit": None,
                "matched_price": None,
                "obra_id": None,
                "obra_nome": None,
                "source": None,
                "date": None,
                "confidence": "sem-match",
                "reasoning": best_reason,
            })
    return out


def main():
    ap = argparse.ArgumentParser(description="Resolve Cartesian determinístico")
    ap.add_argument("--slug", required=True)
    args = ap.parse_args()

    tmp = tmp_dir(args.slug)
    discs = discover_disciplinas(args.slug)
    grand = {}
    for _, disc in discs:
        items_path = tmp / f"items-cartesian-{disc}.json"
        if not items_path.exists():
            print(f"  {disc}: items-cartesian-{disc}.json não existe, pulando")
            continue
        items = json.loads(items_path.read_text(encoding="utf-8"))
        resolved = resolve_items(items)
        out = tmp / f"match-cartesian-resolved-{disc}.json"
        out.write_text(json.dumps(resolved, ensure_ascii=False, indent=2), encoding="utf-8")
        stats = {"alta": 0, "média": 0, "baixa": 0, "sem-match": 0}
        for r in resolved:
            stats[r["confidence"]] += 1
        grand[disc] = (len(resolved), stats)
        print(f"{disc.upper()}: total={len(resolved)}, alta={stats['alta']}, média={stats['média']}, baixa={stats['baixa']}, sem={stats['sem-match']}")
        print(f"  -> {out.name}")

    print("\nGrand total:")
    total = sum(t for t, _ in grand.values())
    a = sum(s["alta"] for _, s in grand.values())
    m = sum(s["média"] for _, s in grand.values())
    b = sum(s["baixa"] for _, s in grand.values())
    sem = sum(s["sem-match"] for _, s in grand.values())
    cov = 100 * (a + m + b) / max(1, total)
    print(f"  {total} itens | alta={a} média={m} baixa={b} sem={sem} | cobertura {cov:.1f}%")


if __name__ == "__main__":
    main()
