"""Extrai abas individuais do template (CTN-TZN_ELT - Orçamento Executivo_R00 - Copia.xlsx)
pra arquivos xlsx separados em 01-eap/, 02-composicoes-insumos/, 03-orcamento-resumo/.

Usa o mesmo zipfile-based approach do gerar_pastas_executivo_electra.py:
- Mantém só a aba alvo + CAPA + EAP (pra resolução de fórmulas) + infra mínima
- Crop rows vazias
- Strip drawings de hidden tabs
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

# reusa funções do gerador principal
sys.path.insert(0, str(Path(__file__).parent))
from gerar_pastas_executivo_electra import (  # noqa: E402
    modify_workbook_xml,
    modify_workbook_rels,
    modify_content_types,
    crop_empty_rows,
    strip_drawings_from_sheet,
    strip_drawings_from_sheet_rels,
    parse_sheet_attrs,
    sheet_entries_from_wb,
    LOCAL_STAGING,
)

DEFAULT_TEMPLATE = Path(
    r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\orcamento\CTN-TZN_ELT - Orçamento Executivo_R00  - Copia.xlsx"
)
DEFAULT_DEST_ROOT = Path(
    r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\orcamento"
)

# extrações: {pasta: {output_filename: [abas_a_manter_visiveis]}}
EXTRACTIONS = {
    "01-eap": {
        "eap.xlsx": ["EAP"],
    },
    "02-composicoes-insumos": {
        "composicoes.xlsx": ["Composições"],
        "insumos.xlsx": ["Insumos"],
        "cpu.xlsx": ["CPU"],
    },
    "03-orcamento-resumo": {
        "orcamento.xlsx": ["Orçamento"],
    },
}

# infra hidden em todas as extrações (pra fórmulas resolverem)
HIDDEN_INFRA = ["CAPA", "PROJETOS", "Ger_Tec e Adm", "Ger_Executivo_Cartesian"]


def extract_xlsx(template: Path, dest: Path, visible_tabs: list[str]) -> Path:
    """Replica gerar_pastas_executivo_electra.build_discipline_xlsx mas pras abas auxiliares."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    LOCAL_STAGING.mkdir(parents=True, exist_ok=True)
    staging = LOCAL_STAGING / dest.name
    if staging.exists():
        staging.unlink()

    with zipfile.ZipFile(template, "r") as zin:
        wb_xml = zin.read("xl/workbook.xml").decode("utf-8")
        rels_xml = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        ct_xml = zin.read("[Content_Types].xml").decode("utf-8")

    # construir disc-like dict
    disc = {"source_tabs": visible_tabs, "slug": dest.stem, "folder": dest.parent.name}
    new_wb, deleted_names, deleted_rids = modify_workbook_xml(
        wb_xml,
        target_disc_tabs=visible_tabs,
        keep_visible=[],  # tudo passa via target_disc_tabs
        hidden_sheets=HIDDEN_INFRA,
    )
    new_rels, deleted_targets = modify_workbook_rels(rels_xml, deleted_rids)

    # reachability walk pra drawings/media (copia exata do gerador principal)
    paths_to_delete = set()
    deleted_part_paths = set()
    deleted_sheet_paths = set()
    for target in deleted_targets:
        norm = target.lstrip("/")
        full = "xl/" + norm if not norm.startswith("xl/") else norm
        paths_to_delete.add(full)
        deleted_part_paths.add(full)
        deleted_sheet_paths.add(full)
        sheet_rels = full.replace("worksheets/", "worksheets/_rels/") + ".rels"
        paths_to_delete.add(sheet_rels)
        deleted_part_paths.add(sheet_rels)

    def _collect_rels_targets(zin, rels_path, base_prefix):
        try:
            content = zin.read(rels_path).decode("utf-8")
        except KeyError:
            return set()
        out = set()
        for m in re.finditer(r'<Relationship\s+([^>]*?)/>', content, re.DOTALL):
            attrs = parse_sheet_attrs(m.group(1))
            t = attrs.get("Target", "")
            if not t or t.startswith("http"):
                continue
            if t.startswith("/"):
                resolved = t.lstrip("/")
            else:
                parts = (base_prefix + "/" + t).split("/")
                stack = []
                for p in parts:
                    if p == ".." and stack:
                        stack.pop()
                    elif p and p != ".":
                        stack.append(p)
                resolved = "/".join(stack)
            out.add(resolved)
        return out

    with zipfile.ZipFile(template, "r") as zin:
        rels_str = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid_to_sheet_path: dict = {}
        for m in re.finditer(r'<Relationship\s+([^>]*?)/>', rels_str, re.DOTALL):
            a = parse_sheet_attrs(m.group(1))
            if a.get("Type", "").endswith("/worksheet"):
                rid_to_sheet_path[a["Id"]] = "xl/" + a["Target"].lstrip("/")

        hidden_sheet_paths: set = set()
        for p_entry in sheet_entries_from_wb(wb_xml):
            nm = p_entry["name"]
            if nm in deleted_names:
                continue
            if nm in HIDDEN_INFRA and nm not in visible_tabs:
                sp = rid_to_sheet_path.get(p_entry.get("r:id"))
                if sp:
                    hidden_sheet_paths.add(sp)

        all_sheet_rels = [n for n in zin.namelist() if n.startswith("xl/worksheets/_rels/")]
        kept_sheet_rels = [r for r in all_sheet_rels if r not in paths_to_delete]
        deleted_sheet_rels = [r for r in all_sheet_rels if r in paths_to_delete]

        kept_targets: set = set()
        hidden_sheet_drawing_targets: set = set()
        for rels_path in kept_sheet_rels:
            base = rels_path.rsplit("/_rels/", 1)[0]
            sheet_xml_path = rels_path.replace("/_rels/", "/").removesuffix(".rels")
            targets = _collect_rels_targets(zin, rels_path, base)
            if sheet_xml_path in hidden_sheet_paths:
                hidden_sheet_drawing_targets |= targets
            else:
                kept_targets |= targets

        deleted_targets_from_sheets: set = set()
        for rels_path in deleted_sheet_rels:
            base = rels_path.rsplit("/_rels/", 1)[0]
            deleted_targets_from_sheets |= _collect_rels_targets(zin, rels_path, base)

        first_degree_orphans = (deleted_targets_from_sheets | hidden_sheet_drawing_targets) - kept_targets
        paths_to_delete |= first_degree_orphans
        deleted_part_paths |= first_degree_orphans

        # 2º grau: media via drawings rels
        drawing_rels_paths = [
            p for p in zin.namelist()
            if p.startswith("xl/drawings/_rels/") and p.endswith(".rels")
        ]
        kept_media: set = set()
        for drp in drawing_rels_paths:
            drawing_file = drp.replace("/_rels/", "/").removesuffix(".rels")
            if drawing_file in first_degree_orphans:
                paths_to_delete.add(drp)
                deleted_part_paths.add(drp)
                continue
            if drawing_file not in kept_targets:
                continue
            base = drp.rsplit("/_rels/", 1)[0]
            kept_media |= _collect_rels_targets(zin, drp, base)

        deleted_media_candidates: set = set()
        for drp in drawing_rels_paths:
            drawing_file = drp.replace("/_rels/", "/").removesuffix(".rels")
            if drawing_file in first_degree_orphans:
                base = drp.rsplit("/_rels/", 1)[0]
                deleted_media_candidates |= _collect_rels_targets(zin, drp, base)

        orphan_media = deleted_media_candidates - kept_media
        orphan_media = {m for m in orphan_media if m.startswith("xl/media/")}
        paths_to_delete |= orphan_media
        deleted_part_paths |= orphan_media

    new_ct = modify_content_types(ct_xml, deleted_part_paths)
    paths_to_delete.add("xl/calcChain.xml")
    new_ct = modify_content_types(new_ct, {"xl/calcChain.xml"})

    hidden_sheet_rels_paths = {
        sp.replace("xl/worksheets/", "xl/worksheets/_rels/") + ".rels"
        for sp in hidden_sheet_paths
    }

    with zipfile.ZipFile(template, "r") as zin, zipfile.ZipFile(
        staging, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.infolist():
            if item.filename in paths_to_delete:
                continue
            if item.filename == "xl/workbook.xml":
                zout.writestr(item, new_wb.encode("utf-8"))
            elif item.filename == "xl/_rels/workbook.xml.rels":
                zout.writestr(item, new_rels.encode("utf-8"))
            elif item.filename == "[Content_Types].xml":
                zout.writestr(item, new_ct.encode("utf-8"))
            elif item.filename.startswith("xl/worksheets/sheet") and item.filename.endswith(".xml"):
                raw = zin.read(item.filename)
                if item.filename in hidden_sheet_paths:
                    raw = strip_drawings_from_sheet(raw)
                cropped = crop_empty_rows(raw)
                zout.writestr(item, cropped)
            elif item.filename in hidden_sheet_rels_paths:
                raw = zin.read(item.filename)
                zout.writestr(item, strip_drawings_from_sheet_rels(raw))
            else:
                zout.writestr(item, zin.read(item.filename))

    if dest.exists():
        dest.unlink()
    shutil.move(str(staging), str(dest))
    return dest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--dest-root", type=Path, default=DEFAULT_DEST_ROOT)
    args = parser.parse_args(argv)

    if not args.template.exists():
        print(f"ERROR: template não encontrado: {args.template}", file=sys.stderr)
        return 2

    print(f"Template: {args.template}")
    print(f"Destino:  {args.dest_root}")
    print()

    for folder, files in EXTRACTIONS.items():
        for fname, visible in files.items():
            dest = args.dest_root / folder / fname
            print(f"[{folder}/{fname}] visíveis: {visible}", flush=True)
            try:
                out = extract_xlsx(args.template, dest, visible)
                print(f"  ✓ {out.stat().st_size/1024/1024:.2f} MB", flush=True)
            except Exception as e:
                print(f"  ✗ ERRO: {type(e).__name__}: {e}", flush=True)
            print()
    print("done.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
