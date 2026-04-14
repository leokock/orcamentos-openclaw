#!/usr/bin/env python3
"""Sincroniza os arquivos do paramétrico V2 Híbrido de um pacote git
para o Google Drive compartilhado (_Parametrico_IA).

Mapeia: base/pacotes/{slug}/parametrico-{slug}.{xlsx,docx,pdf}
     -> _Parametrico_IA/{drive_folder}/{drive_prefix}-parametrico-v3-hibrido.{ext}

Também copia o parametrico-v2-config.json pra rastreabilidade e opcionalmente
arquiva versões antigas do paramétrico no subfolder _antigo/.

Mapeamento git_slug -> drive_folder é customizável no arquivo
`scripts/drive-mapping.json` (cria com default se não existir).

Uso:
    python scripts/sincronizar_parametrico_drive.py --slug arthen-arboris
    python scripts/sincronizar_parametrico_drive.py --slug arthen-arboris --archive-old
    python scripts/sincronizar_parametrico_drive.py --slug arthen-arboris --dry-run
    python scripts/sincronizar_parametrico_drive.py --all --archive-old

Windows path do Drive é auto-detectado (G:\\Drives compartilhados\\...).
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

BASE = Path.home() / "orcamentos-openclaw"
PACOTES = BASE / "base" / "pacotes"
MAPPING_FILE = BASE / "scripts" / "drive-mapping.json"
LOG_FILE = BASE / "base" / "drive-sync.log.jsonl"

# Windows: G:\Drives compartilhados\...
# Mac: ~/Library/CloudStorage/GoogleDrive-...
POSSIBLE_DRIVE_ROOTS = [
    Path("G:/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/_Parametrico_IA"),
    Path.home() / "Library/CloudStorage/GoogleDrive-leonardo@cartesianengenharia.com/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/_Parametrico_IA",
]

# Default mapping: git_slug -> (drive_folder, drive_prefix)
# drive_folder = nome da pasta dentro de _Parametrico_IA/
# drive_prefix = prefixo dos arquivos (pode diferir do slug — ex: placon-arminio-tavares -> arminio-tavares)
DEFAULT_MAPPING = {
    "arthen-arboris": {
        "drive_folder": "arthen-arboris",
        "drive_prefix": "arthen-arboris",
    },
    "placon-arminio-tavares": {
        "drive_folder": "arminio-tavares",
        "drive_prefix": "arminio-tavares",
    },
    "thozen-electra": {
        "drive_folder": "thozen-electra",
        "drive_prefix": "thozen-electra",
    },
}


def find_drive_root() -> Path | None:
    for p in POSSIBLE_DRIVE_ROOTS:
        if p.exists():
            return p
    return None


def load_mapping() -> dict:
    if not MAPPING_FILE.exists():
        MAPPING_FILE.parent.mkdir(parents=True, exist_ok=True)
        MAPPING_FILE.write_text(json.dumps(DEFAULT_MAPPING, indent=2, ensure_ascii=False),
                                 encoding="utf-8")
        print(f"  [info] criado {MAPPING_FILE} com mapeamento default")
    return json.loads(MAPPING_FILE.read_text(encoding="utf-8"))


def log_event(event: dict) -> None:
    event.setdefault("ts", datetime.now().isoformat(timespec="seconds"))
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def sync_slug(slug: str, drive_root: Path, mapping: dict,
              archive_old: bool = False, dry_run: bool = False) -> dict:
    """Sincroniza um slug: copia xlsx/docx/pdf/config pro Drive."""
    if slug not in mapping:
        raise ValueError(f"slug '{slug}' não está em drive-mapping.json — adicione manualmente")

    m = mapping[slug]
    drive_folder = m["drive_folder"]
    drive_prefix = m["drive_prefix"]

    src_dir = PACOTES / slug
    dst_dir = drive_root / drive_folder

    if not src_dir.exists():
        raise FileNotFoundError(f"Pacote git não existe: {src_dir}")

    result = {
        "slug": slug,
        "drive_folder": drive_folder,
        "drive_prefix": drive_prefix,
        "dst_dir": str(dst_dir),
        "copied": [],
        "archived": [],
        "skipped": [],
        "errors": [],
    }

    if not dry_run:
        dst_dir.mkdir(parents=True, exist_ok=True)

    # Arquivar versões antigas (se solicitado)
    if archive_old and dst_dir.exists():
        antigo_dir = dst_dir / "_antigo"
        for old_file in list(dst_dir.iterdir()):
            if not old_file.is_file():
                continue
            name = old_file.name
            # Matches: {prefix}-parametrico-v{N}*.xlsx, {prefix}-analise-v{N}*.xlsx
            is_old_param = (
                name.startswith(f"{drive_prefix}-parametrico-")
                and not name.startswith(f"{drive_prefix}-parametrico-v3-hibrido")
                and not name.startswith(f"{drive_prefix}-parametrico-v3-config")
            )
            is_old_analise = name.startswith(f"{drive_prefix}-analise-")
            if is_old_param or is_old_analise:
                dst_archive = antigo_dir / name
                if dry_run:
                    result["archived"].append(f"[DRY] {name} -> _antigo/")
                    continue
                antigo_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(old_file), str(dst_archive))
                result["archived"].append(name)

    # Copiar xlsx/docx/pdf do pacote
    for ext in ("xlsx", "docx", "pdf"):
        src = src_dir / f"parametrico-{slug}.{ext}"
        dst_name = f"{drive_prefix}-parametrico-v3-hibrido.{ext}"
        dst = dst_dir / dst_name
        if not src.exists():
            result["skipped"].append(f"{src.name} (não existe no pacote)")
            continue
        if dry_run:
            result["copied"].append(f"[DRY] {src.name} -> {dst_name}")
            continue
        try:
            shutil.copy2(str(src), str(dst))
            result["copied"].append(dst_name)
        except Exception as e:
            result["errors"].append(f"{ext}: {e}")

    # Copiar config JSON pra rastreabilidade
    src_cfg = src_dir / "parametrico-v2-config.json"
    if src_cfg.exists():
        dst_cfg_name = f"{drive_prefix}-parametrico-v3-config.json"
        dst_cfg = dst_dir / dst_cfg_name
        if dry_run:
            result["copied"].append(f"[DRY] {src_cfg.name} -> {dst_cfg_name}")
        else:
            try:
                shutil.copy2(str(src_cfg), str(dst_cfg))
                result["copied"].append(dst_cfg_name)
            except Exception as e:
                result["errors"].append(f"config: {e}")

    return result


def main():
    ap = argparse.ArgumentParser(description="Sincroniza parametrico V2 Híbrido pro Drive")
    ap.add_argument("--slug", help="Slug do pacote (ex: arthen-arboris)")
    ap.add_argument("--all", action="store_true", help="Sincronizar todos os slugs do mapping")
    ap.add_argument("--archive-old", action="store_true",
                    help="Mover versões antigas (parametrico-v1/v2/etc) pra _antigo/")
    ap.add_argument("--dry-run", action="store_true",
                    help="Simular operações sem copiar de verdade")
    args = ap.parse_args()

    if not args.slug and not args.all:
        ap.error("Use --slug X ou --all")

    drive_root = find_drive_root()
    if not drive_root:
        print("ERRO: Google Drive não encontrado nos paths esperados:")
        for p in POSSIBLE_DRIVE_ROOTS:
            print(f"  - {p}")
        sys.exit(1)

    print(f"Drive root: {drive_root}")
    mapping = load_mapping()

    slugs = [args.slug] if args.slug else sorted(mapping.keys())
    all_results = []

    for slug in slugs:
        print(f"\n=== {slug} ===")
        try:
            r = sync_slug(slug, drive_root, mapping,
                          archive_old=args.archive_old, dry_run=args.dry_run)
        except Exception as e:
            print(f"  FAIL: {e}")
            all_results.append({"slug": slug, "error": str(e)})
            continue

        print(f"  -> {r['dst_dir']}")
        for item in r["archived"]:
            print(f"  archived: {item}")
        for item in r["copied"]:
            print(f"  copied:   {item}")
        for item in r["skipped"]:
            print(f"  skipped:  {item}")
        for item in r["errors"]:
            print(f"  ERR:      {item}")

        if not args.dry_run:
            log_event({
                "action": "sync_parametrico",
                "slug": slug,
                "n_copied": len(r["copied"]),
                "n_archived": len(r["archived"]),
                "n_errors": len(r["errors"]),
            })

        all_results.append(r)

    print(f"\n{'='*60}")
    n_ok = sum(1 for r in all_results if isinstance(r, dict) and not r.get("error") and not r.get("errors"))
    n_fail = len(all_results) - n_ok
    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"{mode} — {n_ok}/{len(all_results)} sync OK, {n_fail} falhas")


if __name__ == "__main__":
    main()
