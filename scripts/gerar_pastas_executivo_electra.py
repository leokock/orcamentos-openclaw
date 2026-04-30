"""Gera uma pasta por disciplina em orcamento/, com xlsx enxuto + memorial.md.

Iteração 1 (pragmática, zipfile + string-surgery):
- Copia o template completo pra cada pasta
- Deleta as abas de disciplinas NÃO-alvo direto na estrutura .zip do xlsx
- Esconde abas de infra (PROJETOS, Orçamento, Composições, Insumos, CPU, Ger_*)
- Mantém visíveis: CAPA, EAP, abas da disciplina
- Reordena (visíveis primeiro) e define activeTab pra aba da disciplina
- Deleta xl/calcChain.xml (Excel recalcula ao abrir)
- Gera memorial.md stub (write-once)

Por que string-surgery em vez de ElementTree:
- Template usa namespaces MS-específicos (xr, xr6, xr10, xr2, x15, mc:Ignorable).
- ElementTree desfigura prefixos ao re-serializar → Excel rejeita "arquivo corrompido".
- Surgery direto no texto preserva o XML byte-a-byte, modificando só o que precisamos.

Uso:
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_pastas_executivo_electra.py
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_pastas_executivo_electra.py --only EPCs
    py -3.10 -X utf8 ~/orcamentos-openclaw/scripts/gerar_pastas_executivo_electra.py --dry-run
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

SCRIPT_DIR = Path(__file__).parent
MAPPING_PATH = (
    SCRIPT_DIR.parent / "base" / "pacotes" / "thozen-electra" / "mapping-disciplinas.json"
)
LOCAL_STAGING = Path(tempfile.gettempdir()) / "electra_executivo_staging"


# ------------------------------- XML surgery -------------------------------

SHEET_RE = re.compile(
    r'<sheet\s+(?P<attrs>[^>]*?)\s*/>',
    re.DOTALL,
)
ATTR_RE = re.compile(r'(\w+(?::\w+)?)="([^"]*)"')


def parse_sheet_attrs(attrs_str: str) -> dict[str, str]:
    out = {}
    for m in ATTR_RE.finditer(attrs_str):
        out[m.group(1)] = m.group(2)
    return out


def build_sheet_tag(attrs: dict[str, str]) -> str:
    """Reconstrói `<sheet ... />` preservando ordem convencional dos attrs."""
    # ordem típica do Excel: name, sheetId, state (se presente), r:id
    ordered_keys = ["name", "sheetId", "state", "r:id"]
    parts = []
    for k in ordered_keys:
        if k in attrs:
            parts.append(f'{k}="{attrs[k]}"')
    # atributos restantes (fallback)
    for k, v in attrs.items():
        if k not in ordered_keys:
            parts.append(f'{k}="{v}"')
    return "<sheet " + " ".join(parts) + "/>"


def modify_workbook_xml(
    wb_xml: str,
    target_disc_tabs: list[str],
    keep_visible: list[str],
    hidden_sheets: list[str],
) -> tuple[str, set[str], set[str]]:
    """Reescreve workbook.xml: remove sheets não desejadas, esconde infra, reordena,
    atualiza activeTab, remove definedNames órfãs.

    Retorna (novo_xml, nomes_deletados, rIds_deletados).
    """
    # 1) Localizar bloco <sheets>...</sheets>
    sheets_block_re = re.compile(r'<sheets>(.*?)</sheets>', re.DOTALL)
    m = sheets_block_re.search(wb_xml)
    if not m:
        raise RuntimeError("workbook.xml sem bloco <sheets>")
    sheets_inner = m.group(1)

    # 2) Extrair <sheet .../> individuais
    sheet_tags = list(SHEET_RE.finditer(sheets_inner))
    if not sheet_tags:
        raise RuntimeError("workbook.xml sem <sheet> entries")

    parsed = []  # lista de dicts: {attrs, original_idx}
    for idx, tag in enumerate(sheet_tags):
        attrs = parse_sheet_attrs(tag.group("attrs"))
        attrs["_idx"] = idx  # usado pra rastrear ordem original
        parsed.append(attrs)

    # 3) Decidir deletar / esconder / manter
    keep_set = set(keep_visible) | set(hidden_sheets) | set(target_disc_tabs)
    target_set = set(target_disc_tabs)
    hidden_set = set(hidden_sheets)

    kept = []
    deleted_names: set[str] = set()
    deleted_rids: set[str] = set()
    for p in parsed:
        name = p["name"]
        if name not in keep_set:
            deleted_names.add(name)
            if "r:id" in p:
                deleted_rids.add(p["r:id"])
            continue
        # ajustar state
        if name in target_set or name in set(keep_visible):
            p.pop("state", None)  # visível
        elif name in hidden_set:
            p["state"] = "hidden"
        kept.append(p)

    # 4) Reordenar: CAPA, EAP, target_disc_tabs (nessa ordem), depois hidden
    visible_priority = {"CAPA": 0, "EAP": 1}
    for i, t in enumerate(target_disc_tabs):
        visible_priority[t] = 2 + i

    def order_key(p: dict) -> tuple:
        name = p["name"]
        if name in visible_priority:
            return (0, visible_priority[name])
        return (1, p["_idx"])

    kept_ordered = sorted(kept, key=order_key)

    # 5) Reconstruir bloco <sheets>
    new_sheet_tags = []
    for p in kept_ordered:
        clean = {k: v for k, v in p.items() if not k.startswith("_")}
        new_sheet_tags.append(build_sheet_tag(clean))
    new_sheets_block = "<sheets>" + "".join(new_sheet_tags) + "</sheets>"

    new_wb = wb_xml[: m.start()] + new_sheets_block + wb_xml[m.end():]

    # 6) Atualizar activeTab (dentro de <workbookView ... activeTab="..."/>)
    active_idx = 0
    for i, p in enumerate(kept_ordered):
        if p["name"] in target_set:
            active_idx = i
            break

    def _replace_active_tab(match: re.Match) -> str:
        return match.group(1) + str(active_idx) + match.group(3)

    new_wb = re.sub(
        r'(activeTab=")(\d+)(")',
        _replace_active_tab,
        new_wb,
        count=1,
    )
    # firstSheet também — se apontar pra índice >= len(kept), clamp
    def _replace_first_sheet(match: re.Match) -> str:
        orig = int(match.group(2))
        new_val = min(orig, len(kept_ordered) - 1)
        # se apontava pra sheet deletada, forçar 0
        return match.group(1) + str(new_val) + match.group(3)

    new_wb = re.sub(r'(firstSheet=")(\d+)(")', _replace_first_sheet, new_wb, count=1)

    # 7) Remover <definedName>s órfãs (referenciam sheet deletada)
    #    Também remove TODAS com localSheetId (seria reindex complexo).
    def _should_drop_defined_name(full_match: str, inner_text: str, attrs_str: str) -> bool:
        attrs = parse_sheet_attrs(attrs_str)
        if "localSheetId" in attrs:
            return True
        for dname in deleted_names:
            # match `SheetName!` ou `'SheetName'!`
            if re.search(rf"(?:'?{re.escape(dname)}'?)!", inner_text):
                return True
        return False

    defined_name_re = re.compile(
        r'<definedName\s+(?P<attrs>[^>]*)>(?P<text>.*?)</definedName>',
        re.DOTALL,
    )

    def _dn_sub(match: re.Match) -> str:
        if _should_drop_defined_name(match.group(0), match.group("text"), match.group("attrs")):
            return ""
        return match.group(0)

    new_wb = defined_name_re.sub(_dn_sub, new_wb)

    # se <definedNames> ficou vazio, remove
    new_wb = re.sub(r'<definedNames>\s*</definedNames>', "", new_wb)

    return new_wb, deleted_names, deleted_rids


def modify_workbook_rels(rels_xml: str, deleted_rids: set[str]) -> tuple[str, set[str]]:
    """Remove <Relationship Id="rIdN" .../> das rIds deletadas.

    Retorna (novo_xml, targets_deletados).
    """
    rel_re = re.compile(
        r'<Relationship\s+(?P<attrs>[^>]*?)\s*/>',
        re.DOTALL,
    )
    deleted_targets = set()

    def _sub(m: re.Match) -> str:
        attrs = parse_sheet_attrs(m.group("attrs"))
        if attrs.get("Id") in deleted_rids:
            deleted_targets.add(attrs.get("Target", ""))
            return ""
        return m.group(0)

    return rel_re.sub(_sub, rels_xml), deleted_targets


def replace_cell_value(sheet_xml: str, coord: str, new_value, preserve_style: bool = True) -> tuple[str, bool]:
    """Substitui o valor de uma célula específica (ex: 'C2') no sheet XML.

    Regex localiza o elemento `<c r="COORD" .../>` ou `<c r="COORD" ...>...</c>` e
    substitui por um novo elemento inline com o valor novo. Preserva `s="N"` (estilo).

    Retorna (novo_xml, flag_encontrou).
    """
    # Regex genérica pra pegar o elemento inteiro (self-closing ou com filhos)
    pat = re.compile(
        rf'<c\s+r="{re.escape(coord)}"(?P<attrs>[^>]*?)(?:/>|>(?P<content>[^<]*(?:<[^>]+>[^<]*)*?)</c>)',
        re.DOTALL,
    )
    m = pat.search(sheet_xml)
    if not m:
        return sheet_xml, False

    # extrai style "s=..." se existir
    style_m = re.search(r's="(\d+)"', m.group("attrs") or "")
    style_attr = f' s="{style_m.group(1)}"' if (preserve_style and style_m) else ""

    # construir novo elemento
    if isinstance(new_value, (int, float)):
        replacement = f'<c r="{coord}"{style_attr}><v>{new_value}</v></c>'
    elif new_value is None:
        replacement = f'<c r="{coord}"{style_attr}/>'
    else:
        # string — usar inlineStr (não precisa mexer em sharedStrings)
        # escapar XML
        s = str(new_value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        replacement = f'<c r="{coord}"{style_attr} t="inlineStr"><is><t>{s}</t></is></c>'

    return sheet_xml[: m.start()] + replacement + sheet_xml[m.end():], True


# Mapa: coord CAPA → chave no projeto.json (caminho dotted)
# Adaptado das células vistas no template Elizabeth II
CAPA_CELL_MAP = {
    "C2": "projeto.nome",
    "C3": "projeto.cliente",
    "C4": "revisao",
    "F2": "__endereco_compacto__",  # computado: "Rua X, Num, Bairro, Cidade, UF"
    "F3": "__cidade_uf__",          # "Cidade, UF"
    "F4": "projeto.cnpj_proprietario",
    "C6": "projeto.prazo_obra_meses",
    "F6": "apartamentos.total_unidades",
    "C8": "areas.terreno_m2",
    "F8": "salas_comerciais.total",
    "C10": "areas.construida_total_m2",
    "F10": "pavimentos_total_fisicos",       # computado: soma quantidades
    "C12": "areas.privativa_total_m2",
    "F12": "apartamentos.total_dormitorios",
    "C14": "areas.lazer_m2",
    "F14": "__subsolos__",           # 0 pra Electra
    "C16": "areas.comercial_m2",
    "F16": "vagas.total_geral",
}


def resolve_dotted(data: dict, path: str):
    """Pega valor de data seguindo 'a.b.c' → data['a']['b']['c']. None se não existir."""
    cur = data
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def compute_capa_values(projeto: dict) -> dict[str, object]:
    """Computa o dict coord→valor pra CAPA a partir do projeto.json."""
    out: dict[str, object] = {}
    for coord, path in CAPA_CELL_MAP.items():
        if path == "__endereco_compacto__":
            e = (projeto.get("projeto") or {}).get("endereco") or {}
            out[coord] = f"{e.get('rua','')}, {e.get('numero','')}, {e.get('bairro','')}, {e.get('cidade','')}/{e.get('uf','')}".strip(", /")
        elif path == "__cidade_uf__":
            e = (projeto.get("projeto") or {}).get("endereco") or {}
            out[coord] = f"{e.get('cidade','')}, {e.get('uf','')}"
        elif path == "pavimentos_total_fisicos":
            pavs = projeto.get("pavimentos") or []
            total = sum(p.get("quantidade", 1) for p in pavs if isinstance(p, dict))
            out[coord] = total
        elif path == "__subsolos__":
            # Electra tem 0 subsolos (garagens acima do solo)
            out[coord] = 0
        else:
            v = resolve_dotted(projeto, path)
            if v is not None:
                out[coord] = v
    return out


def update_capa_cells(sheet_xml_bytes: bytes, capa_values: dict[str, object]) -> bytes:
    """Aplica substituições de células na sheet XML (CAPA)."""
    s = sheet_xml_bytes.decode("utf-8")
    applied = 0
    for coord, value in capa_values.items():
        s, ok = replace_cell_value(s, coord, value)
        if ok:
            applied += 1
    return s.encode("utf-8")


def build_capa_pavimentos_rows(projeto: dict) -> list[dict]:
    """Constrói linhas da tabela CAPA!B19:G35 a partir do projeto.json.

    Cada linha: {B: Torre, C: Pavimento, D: Área, E: Área Privativa, F: Perímetro, G: Pé-direito}
    """
    pavimentos = projeto.get("pavimentos") or []
    tipologias = (projeto.get("apartamentos") or {}).get("tipologias") or []

    # agrupar privativa por torre (A/B)
    priv_by_torre = {}
    for t in tipologias:
        torre = t.get("torre")
        if torre:
            priv_by_torre.setdefault(torre, 0.0)
            priv_by_torre[torre] += t.get("area_privativa_m2", 0) * t.get("quantidade", 1)

    rows = []
    for p in pavimentos:
        if not isinstance(p, dict):
            continue
        nome = p.get("nome", "")
        tipo = p.get("tipo", "")
        qtd = p.get("quantidade", 1)
        torre_id = p.get("torre", "")
        pe = p.get("pe_direito_m")

        if tipo == "tipo" and torre_id:
            torre_label = f"Torre {torre_id}"
            nome_pavto = f"{nome} (×{qtd})"
            area = p.get("area_total_m2") or (p.get("area_pavto_m2", 0) * qtd)
            # área privativa total da torre, distribuída nesta linha (agregada)
            area_priv = priv_by_torre.get(torre_id, 0)
        elif tipo in ("embasamento", "garagem", "lazer"):
            torre_label = "Embasamento"
            nome_pavto = nome
            area = p.get("area_m2", 0) * qtd
            area_priv = 0
        elif tipo == "tecnico":
            torre_label = "Cobertura"
            nome_pavto = nome
            area = p.get("area_m2", 0) * qtd
            area_priv = 0
        else:
            torre_label = ""
            nome_pavto = nome
            area = p.get("area_m2") or p.get("area_total_m2") or 0
            area_priv = 0

        rows.append({
            "B": torre_label,
            "C": nome_pavto,
            "D": round(area, 2) if area else None,
            "E": round(area_priv, 2) if area_priv else 0,
            "F": None,  # perímetro não disponível no projeto.json
            "G": round(pe, 2) if pe else None,
        })

    return rows


def update_capa_pavimentos_table(sheet_xml_bytes: bytes, rows: list[dict]) -> bytes:
    """Escreve a tabela em B19:G35.

    Primeiro apaga valores das 17 linhas (B19..G35), depois escreve as `rows` novas
    começando em B19. Se rows tiver menos que 17 linhas, as demais ficam vazias.
    """
    s = sheet_xml_bytes.decode("utf-8")
    COLS = ["B", "C", "D", "E", "F", "G"]
    START_ROW = 19
    END_ROW = 35  # capacidade máxima

    # limpar todas as 17 linhas
    for r in range(START_ROW, END_ROW + 1):
        for col in COLS:
            s, _ = replace_cell_value(s, f"{col}{r}", None)

    # escrever novas linhas
    for i, row_data in enumerate(rows):
        r = START_ROW + i
        if r > END_ROW:
            print(f"  [warn] capacity overflow: linha {r} excede limite {END_ROW} — ignorando")
            break
        for col in COLS:
            val = row_data.get(col)
            if val is not None and val != "":
                s, _ = replace_cell_value(s, f"{col}{r}", val)

    return s.encode("utf-8")


def sheet_entries_from_wb(wb_xml: str) -> list[dict[str, str]]:
    m = re.search(r'<sheets>(.*?)</sheets>', wb_xml, re.DOTALL)
    if not m:
        return []
    out = []
    for tag in SHEET_RE.finditer(m.group(1)):
        out.append(parse_sheet_attrs(tag.group("attrs")))
    return out


def strip_drawings_from_sheet(sheet_xml_bytes: bytes) -> bytes:
    """Remove <drawing r:id="..."/> e <legacyDrawing r:id="..."/> do sheet XML.

    Usado em abas HIDDEN, onde não faz sentido carregar a imagem (invisível pro Leo).
    """
    s = sheet_xml_bytes.decode("utf-8")
    s = re.sub(r'<drawing\s+[^/>]*?/>', '', s)
    s = re.sub(r'<legacyDrawing\s+[^/>]*?/>', '', s)
    s = re.sub(r'<oleObjects>.*?</oleObjects>', '', s, flags=re.DOTALL)
    return s.encode("utf-8")


def strip_drawings_from_sheet_rels(rels_bytes: bytes) -> bytes:
    """Remove relationships de tipo /drawing e /vmlDrawing."""
    s = rels_bytes.decode("utf-8")

    def _sub(m: re.Match) -> str:
        attrs = parse_sheet_attrs(m.group(1))
        t = attrs.get("Type", "")
        if t.endswith("/drawing") or t.endswith("/vmlDrawing") or "vmlDrawing" in t:
            return ""
        return m.group(0)

    s = re.sub(r'<Relationship\s+([^>]*?)/>', _sub, s, flags=re.DOTALL)
    return s.encode("utf-8")


def crop_empty_rows(sheet_xml_bytes: bytes) -> bytes:
    """Remove `<row>` elements que não têm nenhum `<c>` filho (linhas-fantasma
    com styles mas sem conteúdo). Template tem sheets com 1M+ linhas dessas.

    Preserva rows com ao menos um `<c>`. Atualiza `<dimension ref="A1:XXn">`
    pra refletir o último `r=` remanescente.

    É byte-level string surgery; conservadora o suficiente pra não quebrar
    integridade (só remove tags que não têm valor semântico em Excel).
    """
    s = sheet_xml_bytes.decode("utf-8")

    # Contar e remover <row .../> self-closing (100% vazias, só com atributos)
    # Padrão: <row r="N" ... /> (não seguido de </row>)
    s = re.sub(r'<row\s[^/>]*?/>', '', s)

    # Remover <row ...></row> sem filhos `<c` (possui conteúdo como <cols>? — sheets têm só <c>)
    # Usar re.sub com função pra lookup de <c dentro do bloco
    def _maybe_drop_row(match: re.Match) -> str:
        inner = match.group("inner")
        if "<c" in inner:
            return match.group(0)
        return ""

    row_full_re = re.compile(
        r'<row\s(?P<attrs>[^>]*?)>(?P<inner>.*?)</row>',
        re.DOTALL,
    )
    s = row_full_re.sub(_maybe_drop_row, s)

    # Atualizar dimension pro último r= remanescente
    # encontrar último <c r="..."> pra inferir última célula
    last_cells = re.findall(r'<c\s+r="([A-Z]+)(\d+)"', s)
    if last_cells:
        max_row = max(int(r) for _, r in last_cells)
        max_col_letters = max(
            (col for col, _ in last_cells),
            key=lambda c: (len(c), c),
        )
        new_dim = f'{_first_cell_col_letter(last_cells)}1:{max_col_letters}{max_row}'
        s = re.sub(r'<dimension\s+ref="[^"]*"\s*/>', f'<dimension ref="{new_dim}"/>', s, count=1)

    return s.encode("utf-8")


def _first_cell_col_letter(cells: list[tuple[str, str]]) -> str:
    """Retorna 'A' (assume-se que dimension parte de A1)."""
    return "A"


def modify_content_types(ct_xml: str, deleted_part_paths: set[str]) -> str:
    """Remove <Override PartName="/xl/worksheets/sheetN.xml" .../>."""
    override_re = re.compile(r'<Override\s+(?P<attrs>[^>]*?)\s*/>', re.DOTALL)

    def _sub(m: re.Match) -> str:
        attrs = parse_sheet_attrs(m.group("attrs"))
        if attrs.get("PartName", "").lstrip("/") in deleted_part_paths:
            return ""
        return m.group(0)

    return override_re.sub(_sub, ct_xml)


# --------------------------- Main build routine ---------------------------

def build_discipline_xlsx(
    template_path: Path,
    dest_folder: Path,
    disc: dict,
    keep_visible_sheets: list[str],
    hidden_sheets: list[str],
    filename_prefix: str,
    dry_run: bool,
    xlsx_filename: str | None = None,
    capa_values: dict | None = None,
    capa_pavimentos_rows: list[dict] | None = None,
) -> Path:
    dest_folder.mkdir(parents=True, exist_ok=True)
    out_name = xlsx_filename if xlsx_filename else f"{filename_prefix}{disc['slug']}.xlsx"
    final_path = dest_folder / out_name

    if dry_run:
        print(f"  [dry-run] would write {final_path}")
        return final_path

    LOCAL_STAGING.mkdir(parents=True, exist_ok=True)
    # staging usa slug + prefixo pra evitar colisão entre disciplinas em paralelo
    staging_path = LOCAL_STAGING / f"{filename_prefix}{disc['slug']}.xlsx"
    if staging_path.exists():
        staging_path.unlink()

    with zipfile.ZipFile(template_path, "r") as zin:
        wb_xml = zin.read("xl/workbook.xml").decode("utf-8")
        rels_xml = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        ct_xml = zin.read("[Content_Types].xml").decode("utf-8")

    new_wb, deleted_names, deleted_rids = modify_workbook_xml(
        wb_xml,
        target_disc_tabs=disc["source_tabs"],
        keep_visible=keep_visible_sheets,
        hidden_sheets=hidden_sheets,
    )
    new_rels, deleted_targets = modify_workbook_rels(rels_xml, deleted_rids)

    # Paths dos sheet XMLs a deletar + rels deles + arrastar drawings/media
    # que só são referenciados por sheets deletadas (reachability pass)
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

    # Descobrir drawings, printerSettings, etc. referenciados pelos sheets
    # (kept e deleted). Orfãos de kept = deletáveis.
    def _collect_rels_targets(zin: zipfile.ZipFile, rels_path: str, base_prefix: str) -> set[str]:
        """Retorna set de paths absolutos dentro do zip referenciados por um .rels."""
        try:
            content = zin.read(rels_path).decode("utf-8")
        except KeyError:
            return set()
        out = set()
        for m in re.finditer(r'<Relationship\s+([^>]*?)/>', content, re.DOTALL):
            attrs = parse_sheet_attrs(m.group(1))
            target = attrs.get("Target", "")
            if not target or target.startswith("http"):
                continue
            # target pode ser relativo ao rels — resolver
            if target.startswith("/"):
                resolved = target.lstrip("/")
            else:
                # juntar com base_prefix
                parts = (base_prefix + "/" + target).split("/")
                stack = []
                for p in parts:
                    if p == "..":
                        if stack:
                            stack.pop()
                    elif p and p != ".":
                        stack.append(p)
                resolved = "/".join(stack)
            out.add(resolved)
        return out

    # Identificar quais sheets ficam hidden — drawings delas vão pra órfãos
    # (otimização: não faz sentido carregar logos de abas que Leo não vê)
    hidden_target_files: set[str] = set()
    for p_entry in sheet_entries_from_wb(wb_xml):
        nm = p_entry["name"]
        if nm in deleted_names:
            continue
        if nm in hidden_sheets and nm not in disc["source_tabs"] and nm not in keep_visible_sheets:
            tgt = p_entry.get("r:id")
            # mapear rId → target path via rels
            # (reler rels do template é barato)
            pass  # faremos abaixo com acesso ao zin

    with zipfile.ZipFile(template_path, "r") as zin:
        # Construir rId → target lookup a partir do rels original
        rels_str = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid_to_sheet_path: dict[str, str] = {}
        for m in re.finditer(r'<Relationship\s+([^>]*?)/>', rels_str, re.DOTALL):
            a = parse_sheet_attrs(m.group(1))
            if a.get("Type", "").endswith("/worksheet"):
                rid_to_sheet_path[a["Id"]] = "xl/" + a["Target"].lstrip("/")

        # Sheet paths de infra hidden
        hidden_sheet_paths: set[str] = set()
        for p_entry in sheet_entries_from_wb(wb_xml):
            nm = p_entry["name"]
            if nm in deleted_names:
                continue
            if nm in hidden_sheets and nm not in disc["source_tabs"] and nm not in keep_visible_sheets:
                sp = rid_to_sheet_path.get(p_entry.get("r:id"))
                if sp:
                    hidden_sheet_paths.add(sp)

        all_sheet_rels = [n for n in zin.namelist() if n.startswith("xl/worksheets/_rels/")]
        kept_sheet_rels = [r for r in all_sheet_rels if r not in paths_to_delete]
        deleted_sheet_rels = [r for r in all_sheet_rels if r in paths_to_delete]

        # kept_targets: arquivos referenciados por sheets VISÍVEIS + não-drawings de hidden
        # hidden_sheet_drawing_targets: APENAS drawings/vml de sheets hidden (órfãos potenciais)
        kept_targets: set[str] = set()
        hidden_sheet_drawing_targets: set[str] = set()
        for rels_path in kept_sheet_rels:
            base = rels_path.rsplit("/_rels/", 1)[0]
            sheet_xml_path = rels_path.replace("/_rels/", "/").removesuffix(".rels")
            if sheet_xml_path.endswith(".xml") is False:
                sheet_xml_path = rels_path.replace("_rels/", "").replace(".rels", "")
            targets = _collect_rels_targets(zin, rels_path, base)
            if sheet_xml_path in hidden_sheet_paths:
                # separar drawings (podem ser stripped) de outros (comments, printerSettings — manter)
                for t in targets:
                    if "/drawings/" in t or "vmlDrawing" in t.lower():
                        hidden_sheet_drawing_targets.add(t)
                    else:
                        kept_targets.add(t)
            else:
                kept_targets |= targets

        deleted_targets_from_sheets: set[str] = set()
        for rels_path in deleted_sheet_rels:
            base = rels_path.rsplit("/_rels/", 1)[0]
            deleted_targets_from_sheets |= _collect_rels_targets(zin, rels_path, base)

        # orfãos: drawings só referenciados por sheets deletadas OU por sheets hidden
        first_degree_orphans = (deleted_targets_from_sheets | hidden_sheet_drawing_targets) - kept_targets
        paths_to_delete |= first_degree_orphans
        deleted_part_paths |= first_degree_orphans

        # Segundo grau: drawings → media
        drawing_rels_paths = [
            p for p in zin.namelist()
            if p.startswith("xl/drawings/_rels/") and p.endswith(".rels")
        ]
        kept_media: set[str] = set()
        for drp in drawing_rels_paths:
            drawing_file = drp.replace("/_rels/", "/").removesuffix(".rels")  # xl/drawings/drawingN.xml
            if drawing_file in first_degree_orphans:
                # rels do drawing também morre
                paths_to_delete.add(drp)
                deleted_part_paths.add(drp)
                continue
            if drawing_file not in kept_targets:
                # drawing não é referenciado por sheet kept nem deleted explicitly
                # (edge case raro; conservador: manter)
                continue
            base = drp.rsplit("/_rels/", 1)[0]  # xl/drawings
            kept_media |= _collect_rels_targets(zin, drp, base)

        # Para orfãos drawings (do deletado), também walk de suas rels pra mídia
        deleted_media_candidates: set[str] = set()
        for drp in drawing_rels_paths:
            drawing_file = drp.replace("/_rels/", "/").removesuffix(".rels")
            if drawing_file in first_degree_orphans:
                base = drp.rsplit("/_rels/", 1)[0]
                deleted_media_candidates |= _collect_rels_targets(zin, drp, base)

        # Mídia órfã = candidata do deletado - kept
        orphan_media = deleted_media_candidates - kept_media
        # só deletar de fato se estiver em xl/media/
        orphan_media = {m for m in orphan_media if m.startswith("xl/media/")}
        paths_to_delete |= orphan_media
        deleted_part_paths |= orphan_media

    new_ct = modify_content_types(ct_xml, deleted_part_paths)

    # calcChain pode referenciar sheets por sheetId → deletar (Excel regenera)
    paths_to_delete.add("xl/calcChain.xml")
    # Override do calcChain no content-types
    new_ct = modify_content_types(new_ct, {"xl/calcChain.xml"})

    # Copiar todos os outros files do zip, substituindo os 3 XMLs modificados
    # e cropando rows vazias nas worksheets preservadas; strippar drawings
    # das hidden sheets
    hidden_sheet_rels_paths = {
        sp.replace("xl/worksheets/", "xl/worksheets/_rels/") + ".rels"
        for sp in hidden_sheet_paths
    }

    # descobrir qual sheetN.xml é a CAPA (pra aplicar capa_values)
    capa_sheet_path: str | None = None
    if capa_values:
        for p_entry in sheet_entries_from_wb(wb_xml):
            if p_entry["name"] == "CAPA":
                capa_sheet_path = rid_to_sheet_path.get(p_entry.get("r:id"))
                break

    with zipfile.ZipFile(template_path, "r") as zin, zipfile.ZipFile(
        staging_path, "w", zipfile.ZIP_DEFLATED
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
                # strippar drawings de sheets hidden (não tem pq carregar imagem)
                if item.filename in hidden_sheet_paths:
                    raw = strip_drawings_from_sheet(raw)
                # aplicar valores novos na CAPA
                if capa_values and item.filename == capa_sheet_path:
                    raw = update_capa_cells(raw, capa_values)
                    if capa_pavimentos_rows is not None:
                        raw = update_capa_pavimentos_table(raw, capa_pavimentos_rows)
                cropped = crop_empty_rows(raw)
                zout.writestr(item, cropped)
            elif item.filename in hidden_sheet_rels_paths:
                raw = zin.read(item.filename)
                zout.writestr(item, strip_drawings_from_sheet_rels(raw))
            else:
                zout.writestr(item, zin.read(item.filename))

    # Move staging → Drive (evita corrupção Drive sync)
    if final_path.exists():
        final_path.unlink()
    shutil.move(str(staging_path), str(final_path))

    kept_count = len(disc["source_tabs"]) + 2 + (len(hidden_sheets))
    size_mb = final_path.stat().st_size / 1024 / 1024
    print(
        f"  wrote xlsx: {final_path.name} "
        f"({size_mb:.2f} MB, deletadas: {len(deleted_names)}, preservadas aprox.: {kept_count})"
    )
    return final_path


# --------------------------- Memorial ---------------------------

MEMORIAL_TEMPLATE = """# Memorial — {disciplina}

> Regras de extração de quantitativos e origem das informações.
> Edite este arquivo pra documentar como cada quantitativo é calculado.
> Isto vira a "regra" que Claude segue em próximas obras.

## Escopo

<!-- O que essa disciplina cobre e NÃO cobre -->

## Fontes de dados

- **Projeto (IFC/DWG/PDF):**
- **Visus (aba):**
- **Memorial descritivo (seção):**
- **Índices base / cross-projeto:**

## Regras de extração por item

### Item 1 — <descrição>

- **Célula na aba {aba}:** <célula>
- **Unidade:**
- **Regra:** <como calcular; qual dado de qual fonte; qual fórmula>
- **Origem:** <projeto específico, pavimento, elemento BIM, etc.>
- **Observações:**

### Item 2 — <descrição>

- **Célula na aba {aba}:** <célula>
- **Unidade:**
- **Regra:**
- **Origem:**

## Pendências / decisões em aberto

- [ ]
"""


def write_memorial_stub(folder: Path, disc: dict, dry_run: bool) -> None:
    mem_path = folder / "memorial.md"
    if mem_path.exists():
        print(f"  memorial.md já existe — preservando ({mem_path.name})")
        return
    if dry_run:
        print(f"  [dry-run] would write {mem_path}")
        return
    first_tab = disc["source_tabs"][0]
    content = MEMORIAL_TEMPLATE.format(disciplina=disc["folder"], aba=first_tab)
    mem_path.write_text(content, encoding="utf-8")
    print(f"  wrote memorial: {mem_path.name}")


# --------------------------- CLI ---------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Slug ou folder da disciplina única a gerar")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-extras", action="store_true", default=False)
    args = parser.parse_args(argv)

    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    template_path = Path(mapping["template_rel"])
    dest_root = Path(mapping["destination_rel"])
    extras_dest_root = Path(mapping.get("extras_destination_rel", mapping["destination_rel"]))
    infra_tabs = mapping["infra_tabs"]
    prefix = mapping["filename_prefix"]
    xlsx_filename = mapping.get("xlsx_filename")

    # carregar projeto.json (dados do empreendimento) pra popular CAPA
    capa_values = None
    capa_pavimentos_rows = None
    projeto_json_path = mapping.get("projeto_json")
    if projeto_json_path:
        p = Path(projeto_json_path)
        if p.exists():
            projeto = json.loads(p.read_text(encoding="utf-8"))
            capa_values = compute_capa_values(projeto)
            capa_pavimentos_rows = build_capa_pavimentos_rows(projeto)
            print(f"projeto.json carregado: {len(capa_values)} células base + {len(capa_pavimentos_rows)} linhas pavimentos")
        else:
            print(f"[warn] projeto.json não encontrado em {p} — CAPA mantém valores do template", file=sys.stderr)

    keep_visible = ["CAPA", "EAP"]
    hidden = infra_tabs

    if not template_path.exists():
        print(f"ERROR: template não encontrado: {template_path}", file=sys.stderr)
        return 2

    all_disc = [("disc", d) for d in mapping["disciplinas"]]
    if not args.skip_extras:
        all_disc += [("extra", d) for d in mapping.get("extras", [])]

    if args.only:
        all_disc = [(t, d) for (t, d) in all_disc if d["slug"] == args.only or d["folder"] == args.only]
        if not all_disc:
            print(f"ERROR: --only {args.only!r} não casou com nenhuma disciplina", file=sys.stderr)
            return 2

    print(f"Template:    {template_path}")
    print(f"Destino:     {dest_root}")
    print(f"Extras em:   {extras_dest_root}")
    print(f"Disciplinas: {len(all_disc)}")
    print()

    for kind, disc in all_disc:
        folder_name = disc["folder"]
        root = extras_dest_root if kind == "extra" else dest_root
        print(f"[{disc['order']:02d}] {folder_name}  (abas: {', '.join(disc['source_tabs'])})", flush=True)
        dest_folder = root / folder_name
        build_discipline_xlsx(
            template_path=template_path,
            dest_folder=dest_folder,
            disc=disc,
            keep_visible_sheets=keep_visible,
            hidden_sheets=hidden,
            filename_prefix=prefix,
            dry_run=args.dry_run,
            xlsx_filename=xlsx_filename,
            capa_values=capa_values,
            capa_pavimentos_rows=capa_pavimentos_rows,
        )
        write_memorial_stub(dest_folder, disc, args.dry_run)
        print(flush=True)

    print("done.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
