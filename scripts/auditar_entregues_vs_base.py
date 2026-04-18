#!/usr/bin/env python3
"""Fase 1b — Audita pasta _Entregas/Orçamento_executivo/ vs base/indices-executivo/.

Identifica:
- Entregas na pasta Drive que NAO estao na base (faltantes a importar)
- Slugs na base que NAO estao mais nas entregas (orfaos — provavelmente slug errado)
- Pares exatos (match OK)
- Pares por similaridade (possivel match, verificar manualmente)

Saida:
- base/entregues-vs-base.json
- analises-cross-projeto/FASE-1B-COBERTURA-ENTREGUES.md

Uso:
    python scripts/auditar_entregues_vs_base.py
"""
from __future__ import annotations

import json
import unicodedata
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

ENTREGUES_PATH_CANDIDATES = [
    Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo"),
    Path.home() / "orcamentos" / "executivos" / "entregues",
]

BASE = Path.home() / "orcamentos-openclaw" / "base"
IDX_DIR = BASE / "indices-executivo"
OUT_JSON = BASE / "entregues-vs-base.json"
OUT_MD = Path.home() / "orcamentos-openclaw" / "analises-cross-projeto" / "FASE-1B-COBERTURA-ENTREGUES.md"

SIMILARITY_THRESHOLD = 0.6


def norm(s):
    s = str(s or "").lower().replace(" ", "-").replace("_", "-")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def similarity(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def encontrar_entregues_path():
    for p in ENTREGUES_PATH_CANDIDATES:
        try:
            # Valida que tem conteúdo (pasta existir mas vazia não serve)
            if p.exists() and p.is_dir():
                has_subdir = any(c.is_dir() for c in p.iterdir())
                if has_subdir:
                    return p
        except (OSError, PermissionError):
            continue
    return None


def listar_entregues():
    """Lista todos os {cliente}/{obra}/ na pasta entregues."""
    path = encontrar_entregues_path()
    if not path:
        return [], None
    entregues = []
    try:
        for cli_dir in sorted(path.iterdir()):
            if not cli_dir.is_dir():
                continue
            cli = cli_dir.name
            try:
                for obra_dir in sorted(cli_dir.iterdir()):
                    if obra_dir.is_dir():
                        slug_candidato = f"{norm(cli)}-{norm(obra_dir.name)}"
                        # Lista arquivos xlsx/pdf pra referência
                        arquivos = []
                        try:
                            for f in obra_dir.iterdir():
                                if f.is_file() and f.suffix.lower() in (".xlsx", ".pdf", ".docx"):
                                    arquivos.append(f.name)
                        except (OSError, PermissionError):
                            pass
                        entregues.append({
                            "cliente": cli,
                            "obra": obra_dir.name,
                            "slug_canonico": slug_candidato,
                            "path": str(obra_dir.relative_to(path)),
                            "n_arquivos": len(arquivos),
                            "arquivos_amostra": arquivos[:5],
                        })
            except (OSError, PermissionError):
                continue
    except (OSError, PermissionError):
        return [], path
    return entregues, path


def listar_base():
    """Lista slugs na base + metadados básicos."""
    slugs = []
    for f in sorted(IDX_DIR.glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            slugs.append({
                "slug": d.get("projeto") or f.stem,
                "ac": d.get("ac"),
                "total": d.get("total"),
            })
        except Exception:
            slugs.append({"slug": f.stem})
    return slugs


def encontrar_matches(entregues, base):
    """Match entre entregues e base por similaridade."""
    base_slugs = {b["slug"]: b for b in base}
    base_keys_norm = {norm(s): s for s in base_slugs}

    exatos = []
    parciais = []
    entregues_faltantes = []

    for ent in entregues:
        slug = ent["slug_canonico"]

        # Match exato
        if slug in base_slugs:
            exatos.append({"entrega": ent, "slug_base": slug})
            continue

        # Match normalizado
        if slug in base_keys_norm:
            orig = base_keys_norm[slug]
            exatos.append({"entrega": ent, "slug_base": orig})
            continue

        # Match parcial
        best = None
        best_sim = 0
        for bs in base_slugs:
            s = similarity(slug, bs)
            if s >= SIMILARITY_THRESHOLD and s > best_sim:
                best = bs
                best_sim = s

        if best:
            parciais.append({
                "entrega": ent,
                "slug_base_similar": best,
                "similaridade": round(best_sim, 3),
            })
        else:
            entregues_faltantes.append(ent)

    # Órfãos: slugs na base sem entrega
    entregues_slugs_norm = {norm(e["slug_canonico"]) for e in entregues}
    parciais_slugs = {norm(p["slug_base_similar"]) for p in parciais}
    exatos_slugs = {norm(e["slug_base"]) for e in exatos}
    orfaos = []
    for b in base:
        bs = b["slug"]
        bsn = norm(bs)
        if bsn not in entregues_slugs_norm and bsn not in parciais_slugs and bsn not in exatos_slugs:
            orfaos.append(b)

    return {
        "exatos": exatos,
        "parciais": parciais,
        "entregues_faltantes": entregues_faltantes,
        "orfaos_na_base": orfaos,
    }


def gerar_md(entregues, base, matches, path_entregues, out: Path):
    lines = [
        "# Fase 1b — Cobertura de Entregues vs Base",
        "",
        f"**Gerado:** {datetime.now().isoformat(timespec='seconds')}",
        f"**Path entregues:** `{path_entregues}`",
        f"**Total entregas no Drive:** {len(entregues)} (obra por cliente)",
        f"**Total slugs na base:** {len(base)}",
        "",
        "## Resumo",
        "",
        f"- ✓ Pares exatos: **{len(matches['exatos'])}**",
        f"- ⚠ Pares parciais (revisar): **{len(matches['parciais'])}**",
        f"- ✗ Entregas faltantes (importar): **{len(matches['entregues_faltantes'])}**",
        f"- 🔍 Órfãos na base (slug nao tem entrega): **{len(matches['orfaos_na_base'])}**",
        "",
        "---",
        "",
    ]

    if matches["entregues_faltantes"]:
        lines += [
            "## Entregas faltantes (a importar)",
            "",
            "| Cliente | Obra | Slug sugerido | Arquivos |",
            "|---|---|---|---:|",
        ]
        for e in matches["entregues_faltantes"]:
            lines.append(f"| {e['cliente']} | {e['obra']} | `{e['slug_canonico']}` | {e['n_arquivos']} |")
        lines.append("")

    if matches["parciais"]:
        lines += [
            "## Pares parciais (REVISAR MANUALMENTE)",
            "",
            "Entregas com slug similar a um slug existente — podem ser o mesmo projeto com grafia diferente, ou projetos diferentes. Verificar antes de agir.",
            "",
            "| Entrega (Cliente/Obra) | Slug canônico | Slug base similar | Sim |",
            "|---|---|---|---:|",
        ]
        for p in matches["parciais"]:
            e = p["entrega"]
            lines.append(f"| {e['cliente']}/{e['obra']} | `{e['slug_canonico']}` | `{p['slug_base_similar']}` | {p['similaridade']:.2f} |")
        lines.append("")

    if matches["orfaos_na_base"]:
        lines += [
            "## Órfãos na base (slug não tem entrega correspondente)",
            "",
            "Esses projetos foram processados mas a pasta Entregas não os contém — possível slug errado na base ou entrega movida.",
            "",
            "| Slug base | AC (m²) | Total (R$) |",
            "|---|---:|---:|",
        ]
        for o in matches["orfaos_na_base"]:
            ac = f"{o['ac']:,.0f}" if o.get("ac") else "—"
            tot = f"R$ {o['total']:,.0f}" if o.get("total") else "—"
            lines.append(f"| `{o['slug']}` | {ac} | {tot} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Próximos passos",
        "",
        "1. **Revisar pares parciais:** decidir quais são o mesmo projeto (renomear slug na base pra casar)",
        "2. **Importar faltantes:** rodar `scripts/importar_entregues_faltantes.py` ou processar manualmente",
        "3. **Investigar órfãos:** decidir se mantém na base ou remove (pode ser projeto nao-entregue, orcamento de teste, etc)",
        "4. **Re-rodar Fase 1 + Fase 3** nos novos slugs após importação",
        "5. **Validar cobertura final:** rodar esse auditor de novo pra garantir cobertura 100%",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")


def main():
    print("Listando entregues...", flush=True)
    entregues, path = listar_entregues()
    if not entregues:
        print(f"ERRO: nao encontrou pasta entregues. Candidatos:", flush=True)
        for p in ENTREGUES_PATH_CANDIDATES:
            print(f"  {p}: {'exists' if p.exists() else 'NAO EXISTE'}", flush=True)
        return
    print(f"  {len(entregues)} entregas em {path}", flush=True)

    print("Listando base...", flush=True)
    base = listar_base()
    print(f"  {len(base)} slugs na base", flush=True)

    print("Comparando...", flush=True)
    matches = encontrar_matches(entregues, base)

    print(f"\n=== RESULTADO ===", flush=True)
    print(f"Exatos: {len(matches['exatos'])}", flush=True)
    print(f"Parciais: {len(matches['parciais'])}", flush=True)
    print(f"Faltantes: {len(matches['entregues_faltantes'])}", flush=True)
    print(f"Orfaos: {len(matches['orfaos_na_base'])}", flush=True)

    # Print amostras
    if matches["entregues_faltantes"]:
        print("\n=== FALTANTES (a importar) ===", flush=True)
        for e in matches["entregues_faltantes"][:10]:
            print(f"  {e['cliente']}/{e['obra']} -> {e['slug_canonico']}", flush=True)

    # Salva
    resultado = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "path_entregues": str(path),
        "n_entregues": len(entregues),
        "n_base": len(base),
        "matches": matches,
    }
    OUT_JSON.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    gerar_md(entregues, base, matches, path, OUT_MD)
    print(f"\nSalvo: {OUT_JSON}", flush=True)
    print(f"Salvo: {OUT_MD}", flush=True)


if __name__ == "__main__":
    main()
