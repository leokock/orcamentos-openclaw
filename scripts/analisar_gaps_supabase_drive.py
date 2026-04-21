#!/usr/bin/env python
"""
Cruza Drive `_Entregas/Orçamento_executivo/{cliente}/{projeto}/` vs tabela
`projetos` no Supabase indices-cartesian pra identificar gaps (executivos
entregues que ainda não foram mapeados como índices).
"""
from __future__ import annotations

import io
import os
import re
import sys
import unicodedata
from pathlib import Path

from dotenv import dotenv_values
from supabase import create_client

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Entregas\Orçamento_executivo")
ENV = Path(r"C:\Users\leona\orcamentos-openclaw\.env.indices-cartesian")


def slugify(text: str) -> str:
    """cliente/projeto → cliente-projeto slug (lowercase, sem acento)."""
    t = unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("ascii")
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t


def listar_drive() -> list[tuple[str, str, str]]:
    """Retorna [(cliente, projeto, slug_esperado), ...]"""
    rows = []
    for cliente in sorted(os.listdir(ROOT)):
        path_c = ROOT / cliente
        if not path_c.is_dir():
            continue
        subs = sorted(s for s in os.listdir(path_c) if (path_c / s).is_dir())
        if subs:
            for sub in subs:
                slug = f"{slugify(cliente)}-{slugify(sub)}"
                rows.append((cliente, sub, slug))
        else:
            # Pasta de cliente sem subpasta → slug só com cliente
            slug = slugify(cliente)
            rows.append((cliente, "(direto)", slug))
    return rows


def fuzzy_match(slug_drive: str, slugs_supabase: set[str]) -> str | None:
    """
    Tenta casar slug do Drive com slugs do Supabase.
    1. match exato
    2. slug_drive contém slug_supabase (ou vice-versa)
    3. cliente+projeto colapsado (ex: 'amalfi-amalfi' ≈ 'amalfi-...')
    """
    # 1. exato
    if slug_drive in slugs_supabase:
        return slug_drive

    # 2. contém/contido
    # ex: drive 'ck-smart-sao-joao' vs supabase 'ck-smart-sao-joao' (OK)
    # ex: drive 'estilo-condominios-estilo-condominios' colapsado
    # reduz repetição tipo 'x-x'
    parts = slug_drive.split("-")
    # tenta colapsar repetições
    if len(parts) > 1 and parts[0] == parts[1]:
        tentativa = "-".join(parts[1:])
        if tentativa in slugs_supabase:
            return tentativa
    # busca inversa
    for s in slugs_supabase:
        if s.startswith(slug_drive) or slug_drive.startswith(s):
            return s
        # drive 'all-acacias-jk' vs supabase 'all-acacias-jk'
        if s == slug_drive:
            return s
        # drive 'f-nogueira-wpr' vs supabase 'f-nogueira-wpr'

    return None


def main():
    env = dotenv_values(ENV)
    client = create_client(env["SUPABASE_URL"], env["SUPABASE_SECRET_KEY"])

    # Pega todos os slugs do Supabase
    resp = client.table("projetos").select("slug, padrao_gemma, ac_m2, rsm2").execute()
    supabase_rows = {r["slug"]: r for r in resp.data}
    supabase_slugs = set(supabase_rows.keys())

    drive_entries = listar_drive()
    print(f"Drive tem {len(drive_entries)} pastas (cliente/projeto)")
    print(f"Supabase tem {len(supabase_slugs)} projetos")
    print()

    matched = []
    missing = []
    for cliente, proj, slug_esperado in drive_entries:
        m = fuzzy_match(slug_esperado, supabase_slugs)
        if m is None:
            missing.append((cliente, proj, slug_esperado))
        else:
            matched.append((cliente, proj, slug_esperado, m))

    # Também identifica slugs do Supabase que NÃO estão no Drive (entregas sumidas?)
    slugs_do_drive_casadas = {m[3] for m in matched}
    supabase_sem_pasta = supabase_slugs - slugs_do_drive_casadas

    print("=" * 80)
    print(f"[1] JÁ MAPEADOS no Supabase: {len(matched)}/{len(drive_entries)}")
    print("=" * 80)

    print()
    print("=" * 80)
    print(f"[2] FALTAM MAPEAR (Drive tem, Supabase não) — {len(missing)} projetos")
    print("=" * 80)
    for cliente, proj, slug in sorted(missing):
        print(f"  - {cliente} / {proj:30s}  (slug esperado: {slug})")

    print()
    print("=" * 80)
    print(f"[3] NO SUPABASE MAS SEM PASTA NO DRIVE — {len(supabase_sem_pasta)} slugs")
    print("=" * 80)
    for slug in sorted(supabase_sem_pasta):
        r = supabase_rows[slug]
        print(f"  - {slug:50s} padrao={r['padrao_gemma']} ac={r['ac_m2']}")

    # Salva report em .md
    report = Path(r"C:\Users\leona\orcamentos-openclaw\base\GAPS-INDICES-DRIVE-SUPABASE.md")
    with report.open("w", encoding="utf-8") as f:
        f.write(f"""---
tags: [custos-ia-parametrico, analise, supabase, gap-analysis]
data: 2026-04-20
---

# Gaps: Drive Entregas/Orçamento_executivo ↔ Supabase `indices-cartesian`

Análise cruzada entre as pastas do Drive compartilhado e a tabela `projetos`
no Supabase, pra identificar projetos executivos entregues que ainda não
foram calibrados/ingeridos na base de índices.

- **Drive:** `_Entregas/Orçamento_executivo/{{cliente}}/{{projeto}}/` — {len(drive_entries)} pastas
- **Supabase:** tabela `projetos` — {len(supabase_slugs)} linhas
- **Casados:** {len(matched)}
- **⚠ Gaps (faltam mapear):** {len(missing)}
- **Fantasmas (Supabase sem pasta no Drive):** {len(supabase_sem_pasta)}

## [1] Projetos FALTAM MAPEAR no Supabase

Executivos entregues que ainda não viraram índice. Priorizar esses pra calibração.

| Cliente | Projeto | Slug esperado |
|---|---|---|
""")
        for cliente, proj, slug in sorted(missing):
            f.write(f"| {cliente} | {proj} | `{slug}` |\n")

        f.write(f"""

## [2] Projetos do Supabase SEM pasta no Drive

Provavelmente slugs antigos que foram renomeados ou pastas que existem mas
não foram casadas pelo fuzzy match. Revisar manualmente.

| Slug | Padrão | AC (m²) |
|---|---|---:|
""")
        for slug in sorted(supabase_sem_pasta):
            r = supabase_rows[slug]
            f.write(f"| `{slug}` | {r['padrao_gemma']} | {r['ac_m2']} |\n")

        f.write(f"""

## [3] Projetos JÁ mapeados (OK)

{len(matched)} projetos casados. Ver tabela `projetos` no Supabase pra detalhes.

## Próximos passos

1. Pros {len(missing)} **gaps**: decidir prioridade — entregues recentes (2026) primeiro
2. Pros executivos priorizados: rodar pipeline de extração (scripts de calibração do paramétrico V2) e ingerir no Supabase via `INSERT INTO projetos`
3. Revisar os {len(supabase_sem_pasta)} "fantasmas" — alguns podem ser só questão de nome de pasta (renomear) ou slug antigo (dedup no Supabase)
""")
    print()
    print(f"> Report salvo em {report}")


if __name__ == "__main__":
    main()
