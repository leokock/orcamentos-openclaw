"""Helpers pro bot Cartesiano orquestrar subagents (Aquos + Internet).

A chamada do subagent em si é feita pelo bot via tool `sessions_spawn`
do runtime OpenClaw (não dá pra fazer via Python script — o subagent é
processo do gateway). Este script:

  1. Imprime prompts canônicos pros 2 subagents (Aquos + Internet)
  2. Valida JSON resolved devolvido pelo subagent (alfa_id, matched_*, confidence)
  3. Persiste resultado em `match-{aquos,internet}-resolved-{disc}.json`

Fluxo no bot:
  $ python scripts/precificacao/precificar_resolver_subagent.py --slug X --disc pci --target aquos --print-prompt
    → bot pega o prompt impresso
    → bot chama sessions_spawn com esse prompt + items-aquos-pci.json
    → bot aguarda subagent terminar (status=completed)
    → bot pega a saída JSON do subagent
    → bot grava em match-aquos-resolved-pci.json
    → opcional: $ python ... --target aquos --validate match-aquos-resolved-pci.json

Pra Internet, o prompt instrui o subagent a usar WebSearch e devolver
preco_internet/loja/url/observacao por alfa_id.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from precificar_common import tmp_dir


PROMPT_AQUOS = """Você é um auxiliar de precificação. Receberá uma lista de itens (chunks JSON com `alfa_id`, `alfa_desc`, `alfa_unit`, `alfa_qtd` e `candidates` — top-5 candidatos fuzzy pesquisados em uma planilha de preço-referência) e deve escolher o melhor candidato por item.

REGRAS:
1. Escolha 1 candidato dos 5 disponíveis para cada item (ou nenhum).
2. Avalie: similaridade textual, compatibilidade de unidade, mesma bitola/ângulo se aplicável, mesma categoria de peça.
3. Classifique a confiança:
   - alta: match seguro (mesma família, bitola, unidade)
   - média: match parcial (uma divergência menor — bitola ausente, sinônimo)
   - baixa: match incerto (categoria diferente, score baixo, unidade diferente)
   - sem-match: nenhum candidato é razoável

DEVOLVA JSON estrito (array, 1 obj por item):
[
  {"alfa_id": int, "chosen": int (1-5 ou null), "matched_desc": str, "matched_unit": str,
   "matched_price": number, "confidence": "alta"|"média"|"baixa"|"sem-match",
   "reasoning": "explicação curta (1 linha)"},
  ...
]

NÃO inclua comentários, não invente preços, não troque o `alfa_id`. Se sem-match, deixe matched_* como null.
"""

PROMPT_INTERNET = """Você é um auxiliar de precificação. Receberá uma lista de itens de construção civil (formato: `alfa_id`, `alfa_desc`, `alfa_contexto`, `alfa_unit`, `alfa_qtd`) e deve buscar preço de varejo no Brasil para cada um via WebSearch.

REGRAS:
1. Para cada item, use 1-3 buscas web (Mercado Livre, Leroy Merlin, Telhanorte, C&C, lojas especializadas em construção/elétrica/hidráulica).
2. Prefira preço com frete incluso quando visível. Se varia, anote no `observacao`.
3. Use unidade igual à `alfa_unit` quando possível. Se não bater (ex: planilha pede metro, loja vende em rolo de 50m), faça a conversão e marque em `observacao`.
4. Se não achar item exato, escolha o mais próximo e anote em `observacao` que é aproximação.

DEVOLVA JSON estrito (array, 1 obj por item):
[
  {"alfa_id": int, "preco_internet": number|null, "loja": str, "url": str, "observacao": str},
  ...
]

Se realmente não achar nada, preco_internet=null e explique em observacao.
"""


def render_prompt(target: str, slug: str, disc: str, items_file: Path) -> str:
    if target == "aquos":
        prompt = PROMPT_AQUOS
    elif target == "internet":
        prompt = PROMPT_INTERNET
    else:
        raise ValueError(f"target inválido: {target}")
    n = 0
    try:
        n = len(json.loads(items_file.read_text(encoding="utf-8")))
    except Exception:
        pass
    header = f"""[Slug: {slug} | Disciplina: {disc} | Target: {target} | Itens: {n}]
Items input file (lido por você como entrada): {items_file.name}

{prompt}
"""
    return header


def validate_resolved(path: Path, target: str) -> tuple[bool, list[str]]:
    """Valida JSON resolved. Retorna (ok, lista_de_erros)."""
    errs = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return False, [f"JSON inválido: {e}"]
    if not isinstance(data, list):
        return False, ["raiz não é list"]

    if target == "aquos":
        required = {"alfa_id", "confidence"}
        valid_conf = {"alta", "média", "media", "baixa", "sem-match", "sem"}
    elif target == "internet":
        required = {"alfa_id"}
        valid_conf = None
    else:
        return False, [f"target inválido: {target}"]

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            errs.append(f"item[{i}] não é dict")
            continue
        for k in required:
            if k not in item:
                errs.append(f"item[{i}] missing key '{k}'")
        if valid_conf is not None:
            c = item.get("confidence", "")
            if c and c not in valid_conf:
                errs.append(f"item[{i}] confidence inválida: {c!r}")

    return len(errs) == 0, errs


def main():
    ap = argparse.ArgumentParser(description="Helpers pro subagent codex resolver Aquos/Internet")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--disc", required=True, help="pci|sanitario|telecom|...")
    ap.add_argument("--target", required=True, choices=["aquos", "internet"])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--print-prompt", action="store_true", help="Imprime prompt canônico pro subagent")
    g.add_argument("--validate", help="Valida JSON resolved (path)")
    args = ap.parse_args()

    tmp = tmp_dir(args.slug)
    if args.target == "aquos":
        items_file = tmp / f"items-aquos-{args.disc}.json"
    else:
        items_file = tmp / f"items-internet-{args.disc}.json"

    if args.print_prompt:
        if not items_file.exists():
            print(f"❌ {items_file} não existe. Rode precificar_candidates.py primeiro.", file=sys.stderr)
            sys.exit(1)
        print(render_prompt(args.target, args.slug, args.disc, items_file))
        return

    if args.validate:
        ok, errs = validate_resolved(Path(args.validate), args.target)
        if ok:
            print(f"✓ {args.validate} válido")
            sys.exit(0)
        print(f"❌ {args.validate} inválido:")
        for e in errs[:20]:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
