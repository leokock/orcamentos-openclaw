"""Consolida 6 mds em 00-projeto/ → projeto.json (machine-readable, fonte única).

Cada md em 00-projeto/ tem frontmatter YAML + corpo markdown. Esse script:
1. Lê os 6 mds (projeto, areas, pavimentos, apartamentos, lazer, vagas)
2. Funde todos os frontmatters num único dict
3. Valida contra projeto-schema.json
4. Salva projeto.json no mesmo diretório

Uso:
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/consolidar_projeto.py
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/consolidar_projeto.py --projeto-dir "G:/.../00-projeto"
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/consolidar_projeto.py --validate-only
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
DEFAULT_PROJETO_DIR = Path(
    r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\orcamento\00-projeto"
)
SCHEMA_PATH = SCRIPT_DIR.parent / "base" / "pacotes" / "_schema" / "projeto-schema.json"

EXPECTED_MDS = ["projeto.md", "areas.md", "pavimentos.md", "apartamentos.md", "lazer.md", "vagas.md"]


def parse_frontmatter(md_text: str) -> dict:
    """Extrai bloco YAML entre `---` no topo do arquivo."""
    lines = md_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}
    yaml_text = "\n".join(lines[1:end])
    try:
        return yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as e:
        raise RuntimeError(f"YAML inválido no frontmatter: {e}")


def consolidar(projeto_dir: Path) -> dict:
    """Consolida todos os mds num único dict."""
    if not projeto_dir.is_dir():
        raise FileNotFoundError(f"projeto_dir não existe: {projeto_dir}")

    consolidated: dict = {}
    fontes_unique: set[str] = set()

    for md_name in EXPECTED_MDS:
        md_path = projeto_dir / md_name
        if not md_path.exists():
            print(f"  [warn] arquivo ausente: {md_name}", flush=True)
            continue
        text = md_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            print(f"  [warn] sem frontmatter YAML: {md_name}", flush=True)
            continue

        # acumular fontes
        if "fontes" in fm:
            for f in fm.pop("fontes"):
                fontes_unique.add(f)

        # mesclar (chaves de nível 1 não devem colidir entre mds)
        for k, v in fm.items():
            if k in consolidated:
                if isinstance(consolidated[k], dict) and isinstance(v, dict):
                    consolidated[k] = {**consolidated[k], **v}
                else:
                    print(f"  [warn] chave {k!r} duplicada em {md_name}; sobrescreve", flush=True)
                    consolidated[k] = v
            else:
                consolidated[k] = v
        print(f"  [ok] {md_name} ({len(fm)} chaves)", flush=True)

    if fontes_unique:
        consolidated["fontes"] = sorted(fontes_unique)

    return consolidated


def validar(data: dict, schema_path: Path) -> list[str]:
    """Valida data contra schema. Retorna lista de erros (vazia = OK)."""
    try:
        import jsonschema
    except ImportError:
        print("  [skip] jsonschema não instalado — instalar com `pip install jsonschema`", flush=True)
        return []
    if not schema_path.exists():
        print(f"  [skip] schema não encontrado: {schema_path}", flush=True)
        return []

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for err in validator.iter_errors(data):
        errors.append(f"  - {' > '.join(str(p) for p in err.absolute_path) or '(root)'}: {err.message}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projeto-dir", type=Path, default=DEFAULT_PROJETO_DIR)
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--out", type=Path, help="Path de saída do projeto.json (default: projeto-dir/projeto.json)")
    args = parser.parse_args(argv)

    print(f"projeto_dir: {args.projeto_dir}", flush=True)
    print(f"schema:      {SCHEMA_PATH}", flush=True)
    print()

    print("Consolidando 6 mds...", flush=True)
    data = consolidar(args.projeto_dir)

    print("\nValidando contra schema...", flush=True)
    errors = validar(data, SCHEMA_PATH)
    if errors:
        print(f"  ❌ {len(errors)} erros de validação:", flush=True)
        for e in errors:
            print(e, flush=True)
        if not args.validate_only:
            print("\n  ⚠ projeto.json NÃO foi escrito (validação falhou)", flush=True)
        return 1
    print("  ✓ schema OK", flush=True)

    if args.validate_only:
        print("\n--validate-only ativo — projeto.json não escrito", flush=True)
        return 0

    out_path = args.out or args.projeto_dir / "projeto.json"
    out_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    size_kb = out_path.stat().st_size / 1024
    print(f"\n✓ projeto.json escrito: {out_path} ({size_kb:.1f} KB)", flush=True)
    print(f"  chaves de nível 1: {sorted(data.keys())}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
