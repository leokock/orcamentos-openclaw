# -*- coding: utf-8 -*-
"""
Validação BIM × Paramétrico (ARQUITETURA) — Placon Hermann Blumenau

Lê o takeoff do Solibri (modelo arquitetônico OSPA) e classifica cada linha em
macrogrupos de arquitetura, escolhendo a métrica física correta. Compara com o
paramétrico V2 (índices calibrados) e prepara o reprice.

ESCOPO: só arquitetura. Estrutura (concreto/aço/fôrma) fica fora — revisão futura.

Cuidado-chave: o export do Solibri agrupa por classe IFC e SOMA todas as camadas de
material de cada elemento. Por isso classificamos pela TAG de material + nome do TIPO
(parede), e a "Net Area" de parede é UMA FACE (net de vãos).
"""
import openpyxl
from collections import defaultdict

SOLIBRI = r"C:\Users\leona\OneDrive\Área de Trabalho\Quantidade Hermann.xlsx"
PARAM   = r"c:\Users\leona\openclaw\data\base\pacotes\placon-hermann-blumenau\parametrico-placon-hermann-blumenau-v01.xlsx"
AC = 5877.96


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def load_solibri():
    wb = openpyxl.load_workbook(SOLIBRI, data_only=True)
    rows = list(wb["Building Element Quantities"].iter_rows(values_only=True))[3:]
    out = []
    for r in rows:
        bet = r[0]
        if not bet:
            continue
        out.append({
            "bet": str(bet),
            "type": str(r[1]) if r[1] is not None else "",
            "mat": str(r[2]) if r[2] is not None else "",
            "area": num(r[3]),
            "length": num(r[4]),
            "vol": num(r[5]),
            "count": int(num(r[6])),
        })
    return out


def classify(row):
    """Retorna (macrogrupo, subitem, metrica) ou (None, motivo, '') se fora de escopo.
    metrica indica qual número usar: 'area' | 'count' | 'vol' | 'len'."""
    bet, typ, mat = row["bet"], row["type"], row["mat"]

    # --- buckets ignorados (não são orçamento de arquitetura) ---
    if bet == "Fixed Furnishings":
        return (None, "mobiliário/equip", "")
    if bet == "Unclassified":
        return (None, "não classificado (modelo)", "")
    if ".GEN sólido (cor branco) (mobiliário)" in mat or ".GEN clearance" in mat:
        return (None, "mobiliário/clearance", "")
    if typ.startswith("GEN ") or "GEN branco" in typ:
        return (None, "genérico/mobiliário", "")

    # --- pisos / lajes (Floor Slabs) ---
    if bet == "Floor Slabs":
        if mat.startswith(".EST concreto armado"):
            return ("PISOS", "area-base laje elevada", "area")   # referência p/ totais
        if "concreto (magro)" in mat:
            return ("PISOS", "area-base piso sobre solo (magro)", "area")
        if ".VEG" in mat:
            return ("PAISAGISMO", "grama/solo", "area")
        if ".LÍQ água" in mat or "piscina" in mat.lower():
            return ("PISCINA", "lâmina d'água", "area")
        if ".RVST impermeabilização" in mat:
            return ("IMPERMEABILIZACAO", "laje impermeabilizada", "area")
        if "basalto" in mat or "granito" in mat or "porcelan" in mat or ".RVST argamassa (colante)" in mat:
            return ("PISOS", "acabamento real (comuns)", "area")
        if "meio-fio" in mat:
            return ("URBANIZACAO", "meio-fio", "len")
        return (None, "floor outro", "")

    # --- forros (Suspended Ceilings) ---
    if bet == "Suspended Ceilings":
        if ".RVST gesso acartonado" in mat:
            return ("TETO/FORRO", "forro gesso", "area")
        if "pinus" in mat:
            return ("TETO/FORRO", "forro ripado madeira", "area")
        return ("TETO/FORRO", "forro outro", "area")

    # --- esquadrias ---
    if bet == "Interior Doors":
        return ("ESQUADRIAS", "portas", "count")
    if bet == "Windows":
        return ("ESQUADRIAS", "janelas", "count")
    if bet == "Interior Railings":
        return ("ESQUADRIAS", "serralheria/guarda-corpo", "count")

    # --- estrutura: fora de escopo ---
    if bet in ("Beams", "Columns", "Stairs"):
        return (None, "estrutura (fora de escopo)", "")

    # --- paredes (tudo veio como External Walls) ---
    if bet == "External Walls":
        is_ext = ("EXT" in typ) or ("(EXT)" in mat)
        # parede de concreto pura (estrutura) — só a face arquitetônica conta
        if typ.startswith("EST CON"):
            return (None, "parede concreto estrutural (fora de escopo)", "")
        # fachada com núcleo de concreto + revestimento externo
        if typ.startswith("VED RVST") or ("RVST" in typ and "EXT" in typ):
            return ("FACHADA", "parede concreto+revest externo", "area")
        # alvenaria de bloco
        if typ.startswith("VED BCE"):
            sub = "alvenaria bloco (face externa)" if is_ext else "alvenaria bloco (interna)"
            return ("ALVENARIA", sub, "area")
        # brise ripado de madeira (fachada)
        if typ.startswith("BR RIPADO") or ("RIPADO" in typ):
            return ("FACHADA", "brise ripado madeira", "area")
        # envidraçamento (vitrine loja, hall) -> esquadria/fachada vidro
        if typ.startswith("EV "):
            return ("ESQUADRIAS", "envidraçamento (vitrine/hall)", "area")
        # parede de piscina impermeabilizada
        if "PISCINA" in typ or ".RVST impermeabilização" in mat:
            return ("IMPERMEABILIZACAO", "parede piscina/molhada", "area")
        # elementos de arquitetura "EA" (muretas/peitoris/elementos) — material None
        if typ.startswith("EA "):
            return ("ELEM_ARQ", "elemento arq (EA)", "area")
        return (None, "parede outro", "")

    return (None, "fora de escopo: " + bet, "")


def main():
    rows = load_solibri()
    grp = defaultdict(lambda: defaultdict(lambda: {"area": 0.0, "vol": 0.0, "count": 0, "len": 0.0, "n": 0}))
    ignored = defaultdict(lambda: {"area": 0.0, "vol": 0.0, "count": 0, "n": 0})

    tot_area = tot_vol = tot_count = 0.0
    for r in rows:
        tot_area += r["area"]; tot_vol += r["vol"]; tot_count += r["count"]
        mg, sub, metric = classify(r)
        if mg is None:
            b = ignored[sub]
            b["area"] += r["area"]; b["vol"] += r["vol"]; b["count"] += r["count"]; b["n"] += 1
            continue
        c = grp[mg][sub]
        c["area"] += r["area"]; c["vol"] += r["vol"]; c["count"] += r["count"]
        c["len"] += r["length"]; c["n"] += 1

    print("=" * 78)
    print("CLASSIFICAÇÃO BIM (modelo arquitetônico OSPA) — Placon Hermann Blumenau")
    print(f"AC = {AC:,.2f} m²  |  totais brutos: area={tot_area:,.1f} m²  vol={tot_vol:,.1f} m³  count={int(tot_count)}")
    print("=" * 78)
    for mg in sorted(grp):
        print(f"\n### {mg}")
        ta = 0.0
        for sub, v in sorted(grp[mg].items(), key=lambda x: -x[1]["area"]):
            extra = ""
            if v["count"]:
                extra += f"  count={v['count']}"
            if v["len"] > 1:
                extra += f"  len={v['len']:.0f}m"
            print(f"   - {sub:38s} area={v['area']:9.1f} m²  vol={v['vol']:8.1f} m³{extra}  ({v['n']} linhas)")
            ta += v["area"]
        print(f"     >> subtotal área = {ta:,.1f} m²  ({ta/AC:.3f} m²/m² AC)")

    print("\n" + "-" * 78)
    print("IGNORADO / FORA DE ESCOPO (auditável):")
    ia = 0.0
    for sub, v in sorted(ignored.items(), key=lambda x: -x[1]["area"]):
        print(f"   - {sub:42s} area={v['area']:9.1f} m²  vol={v['vol']:8.1f} m³  ({v['n']} linhas)")
        ia += v["area"]
    print(f"     >> área ignorada = {ia:,.1f} m²")

    # reconciliação
    class_area = sum(v["area"] for mg in grp for v in grp[mg].values())
    print("\n" + "-" * 78)
    print(f"RECONCILIAÇÃO ÁREA: classificada {class_area:,.1f} + ignorada {ia:,.1f} = {class_area+ia:,.1f}  (bruto {tot_area:,.1f})")


if __name__ == "__main__":
    main()
