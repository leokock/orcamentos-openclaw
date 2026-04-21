"""Normalizador de pavimento e torre para Thozen Electra.

Estrutura Electra (ordem de pavimentos):
    TERREO   -> 1º pav
    G1..G5   -> 2º-6º pav (garagens)
    LAZER    -> 7º pav
    TIPO     -> 8º-31º pav (repetido 24×, apartamentos)
    C_MAQ    -> 32º/cobertura (casa de maquinas)
    COBERTURA-> laje cobertura

Torres: A, B, AMBAS (quando PDF cita duas), NA (nao especificada)

A funcao `normalizar(texto)` recebe uma string livre (pode vir de especificacao_local
do formato A ou de metadata.localizacao do formato B) e retorna um dict com:
    {"pavimento": "TERREO"|"G1"|..., "torre": "A"|"B"|"AMBAS"|"NA", "original": ...}
"""
import re

PAVIMENTOS_ORDER = ["TERREO", "G1", "G2", "G3", "G4", "G5", "LAZER", "TIPO", "C_MAQ", "COBERTURA", "NA"]

PAVIMENTO_LABEL = {
    "TERREO":    "01º Térreo",
    "G1":        "02º G1",
    "G2":        "03º G2",
    "G3":        "04º G3",
    "G4":        "05º G4",
    "G5":        "06º G5",
    "LAZER":     "07º Lazer",
    "TIPO":      "08º-31º Tipo (×24)",
    "C_MAQ":     "Casa de Máquinas",
    "COBERTURA": "Cobertura",
    "NA":        "Sem pavimento / Quadro geral",
}

# Regras em ordem de prioridade — a primeira que matchea vence.
# Cada regra: (regex, pavimento, torre_override=None)
_PAV_REGEXES = [
    # Formato B (QT-MAT): "A) 01º PAVTO. - TÉRREO"
    (r"01[ºo°]?\s*PAVTO\.?\s*-?\s*T[EÉ]RREO", "TERREO"),
    (r"02[ºo°]?\s*PAVTO\.?\s*-?\s*G\s*1", "G1"),
    (r"03[ºo°]?\s*PAVTO\.?\s*-?\s*G\s*2", "G2"),
    (r"04[ºo°]?\s*PAVTO\.?\s*-?\s*G\s*3", "G3"),
    (r"05[ºo°]?\s*PAVTO\.?\s*-?\s*G\s*4", "G4"),
    (r"06[ºo°]?\s*PAVTO\.?\s*-?\s*G\s*5", "G5"),
    (r"07[ºo°]?\s*PAVTO\.?\s*-?\s*LAZER", "LAZER"),
    (r"0?8[ºo°]?\s*AO\s*31[ºo°]?\s*PAVTO\.?\s*-?\s*TIPO", "TIPO"),
    # Formato A livre — termos comuns
    (r"\bC\.?\s*M[AÁ]Q(UINAS)?\b", "C_MAQ"),
    (r"\bCASA\s+DE\s+M[AÁ]Q", "C_MAQ"),
    (r"\bCOBERTURA\b", "COBERTURA"),
    (r"\bPAVTO\.?\s*TIPOS?\b", "TIPO"),
    (r"\bTIPO\s*24\s*x\b", "TIPO"),
    (r"\bAPTOS?\s+\d", "TIPO"),  # "APTOS 01 & 02"
    (r"\bLAZER\b", "LAZER"),
    (r"\bGARAGEM\s*G\s*1\b", "G1"),
    (r"\bGARAGEM\s*G\s*2\b", "G2"),
    (r"\bGARAGEM\s*G\s*3\b", "G3"),
    (r"\bGARAGEM\s*G\s*4\b", "G4"),
    (r"\bGARAGEM\s*G\s*5\b", "G5"),
    (r"\bG\s*1\b", "G1"),
    (r"\bG\s*2\b", "G2"),
    (r"\bG\s*3\b", "G3"),
    (r"\bG\s*4\b", "G4"),
    (r"\bG\s*5\b", "G5"),
    (r"\bT[EÉ]RREO\b", "TERREO"),
    # Specific Electra: QGC G. TERREO => TERREO
    (r"\bG\.\s*T[EÉ]RREO", "TERREO"),
]

_TORRE_REGEXES = [
    (r"\bBLOCO[\s-]*A\b", "A"),
    (r"\bBLOCA\s*A\b", "A"),  # typo observado no PDF "DISJUNTORES QGC G1 (BLOCA A)"
    (r"\bBLOCO[\s-]*B\b", "B"),
    (r"\bTORRE[\s-]*A\b", "A"),
    (r"\bTORRE[\s-]*B\b", "B"),
    (r"\bT\s*\.?\s*A\b", "A"),
    (r"\bT\s*\.?\s*B\b", "B"),
    (r"\bTORR?EA?S?\s*A\s*[&E]\s*B\b", "AMBAS"),
    (r"\bBLOCOS?\s*A\s*[&E]\s*B\b", "AMBAS"),
]


def normalizar(texto: str | None) -> dict:
    if not texto:
        return {"pavimento": "NA", "torre": "NA", "original": "", "pavimento_label": PAVIMENTO_LABEL["NA"]}
    t = texto.strip().upper()

    pav = "NA"
    for pattern, p in _PAV_REGEXES:
        if re.search(pattern, t, re.IGNORECASE):
            pav = p
            break

    torre = "NA"
    for pattern, to in _TORRE_REGEXES:
        if re.search(pattern, t, re.IGNORECASE):
            torre = to
            break

    return {
        "pavimento": pav,
        "torre": torre,
        "original": texto,
        "pavimento_label": PAVIMENTO_LABEL[pav],
    }


def ordem_pavimento(pav: str) -> int:
    try:
        return PAVIMENTOS_ORDER.index(pav)
    except ValueError:
        return 999


if __name__ == "__main__":
    # Testes rapidos com exemplos reais
    casos = [
        "C.P. TÉRREO - BLOCO-A",
        "C.P. G1 - BLOCO-A",
        "C.P. TIPO 24x - BLOCO-B",
        "C.P. C. MÁQ - BLOCO-A",
        "01° PV. TÉRREO - TORRE A",
        "GARAGEM G1 - TORRE A",
        "LAZER - TORRE B",
        "PAVTO. TIPOS - TORRE A",
        "C. MÁQUINAS - TORRE B",
        "APTOS 01 & 02 - TORRE A",
        "A) 01º PAVTO. - TÉRREO",
        "B) 02º PAVTO. - G1",
        "H) 08º AO 31º PAVTO. - TIPO (X24) [TORRE A]",
        "I) 08º AO 31º PAVTO. - TIPO (X24) [TORRE B]",
        "G) 07º PAVTO. - LAZER",
        "VERIFICAR DIAGRAMA",
        "",
    ]
    for c in casos:
        r = normalizar(c)
        print(f"{c[:55]:55s} -> pav={r['pavimento']:8s} torre={r['torre']:5s}")
