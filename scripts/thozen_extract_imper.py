#!/usr/bin/env python3
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def col_to_idx(ref):
    letters = "".join(ch for ch in ref if ch.isalpha())
    idx = 0
    for ch in letters:
        idx = idx * 26 + ord(ch.upper()) - 64
    return idx


def load_xlsx(path):
    zf = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in zf.namelist():
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
        for si in root.iter(NS_MAIN + "si"):
            shared.append("".join(t.text or "" for t in si.iter(NS_MAIN + "t")))

    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rels = {el.attrib["Id"]: el.attrib["Target"] for el in rels_root}
    sheets = {}
    for sheet in wb.find(NS_MAIN + "sheets"):
        name = sheet.attrib["name"]
        rid = sheet.attrib[NS_REL + "id"]
        target = rels[rid]
        if not target.startswith("xl/"):
            target = "xl/" + target
        sheets[name] = target
    return zf, shared, sheets


def cell_value(cell, shared):
    value = cell.find(NS_MAIN + "v")
    inline = cell.find(NS_MAIN + "is")
    if inline is not None:
        return "".join(t.text or "" for t in inline.iter(NS_MAIN + "t"))
    if value is None or value.text is None:
        return ""
    if cell.attrib.get("t") == "s":
        return shared[int(value.text)]
    return value.text


def read_sheet(zf, shared, path):
    root = ET.fromstring(zf.read(path))
    rows = []
    for row in root.iter(NS_MAIN + "row"):
        vals = {}
        max_col = 0
        for cell in row.findall(NS_MAIN + "c"):
            idx = col_to_idx(cell.attrib.get("r", "A"))
            vals[idx] = cell_value(cell, shared)
            max_col = max(max_col, idx)
        rows.append([vals.get(i, "") for i in range(1, max_col + 1)])
    return rows


def norm(text):
    return re.sub(r"\s+", " ", str(text or "").strip())


def nonempty(row):
    return [norm(v) for v in row if norm(v)]


def inspect(path, sheet_filter=None):
    zf, shared, sheets = load_xlsx(path)
    result = {"sheets": list(sheets), "matches": {}}
    for name in sheets:
        if sheet_filter and name != sheet_filter:
            continue
        rows = read_sheet(zf, shared, sheets[name])
        matches = []
        for i, row in enumerate(rows, 1):
            text = " | ".join(nonempty(row)).upper()
            if any(
                k in text
                for k in (
                    "IMPER",
                    "MANTA",
                    "ASFALT",
                    "POLIMER",
                    "RALO",
                    "PEITOR",
                    "BALDRAME",
                    "CISTERNA",
                    "RESERVAT",
                    "FLOREIRA",
                    "PISCINA",
                    "PISO",
                    "PAREDE",
                )
            ):
                matches.append({"row": i, "values": nonempty(row)[:24]})
        if matches:
            result["matches"][name] = matches[:120]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    inspect(Path(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else None)
