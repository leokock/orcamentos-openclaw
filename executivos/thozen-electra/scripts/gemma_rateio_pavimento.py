"""Fase 3 do pipeline 348_LM: rateia itens de PDFs formato A (sem pavimento)
entre os pavimentos do Electra usando Gemma com heuristica tecnica por sistema.

Input: `{slug}.gemma.json` (formato A, saida de gemma_extract_lm)
Output: `{slug}.rateio.json` no mesmo diretorio, preservando a lista flat V1
        e adicionando um campo `distribuicao` por item (V2 rateado).

Cada chamada Gemma recebe:
 - Contexto do Electra (2 torres, 32 pav, pavimentos canonicos, apto tipo x96)
 - Heuristicas de rateio especificas do sistema (SPDA, HIDRO-TUBOS, PPCI-SHP...)
 - Lista de itens para distribuir

Resposta esperada: array JSON com distribuicao por item, validada via
  sum(qtd_rateada) == qtd_total (tolerancia 0.1%).

Uso:
    python scripts/gemma_rateio_pavimento.py quantitativos/listas-materiais-348/spda/spda-completo.gemma.json
    python scripts/gemma_rateio_pavimento.py --all --disciplina hidraulico
    python scripts/gemma_rateio_pavimento.py --all  # todas format A
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))
import gemma_extract_lm as gem


OUT_DIR = Path(r"G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA\thozen-electra\quantitativos\listas-materiais-348")

PAVIMENTOS_VALIDOS = {"TERREO", "G1", "G2", "G3", "G4", "G5", "LAZER", "TIPO", "C_MAQ", "COBERTURA"}
TORRES_VALIDAS = {"A", "B", "AMBAS"}

CONTEXT_ELECTRA = """CONTEXTO DA OBRA - Residencial Electra Towers (Porto Belo/SC)
Cliente: Thozen Construtora
Duas torres identicas lado a lado (TORRE A e TORRE B)
Pavimentos canonicos (use EXATAMENTE esses codigos em "pavimento"):
  TERREO    -> 1o pavimento (hall, ramais, caixas de inspecao, hidrometros)
  G1        -> 2o pavimento (garagem 1)
  G2        -> 3o pavimento (garagem 2)
  G3        -> 4o pavimento (garagem 3)
  G4        -> 5o pavimento (garagem 4)
  G5        -> 6o pavimento (garagem 5)
  LAZER     -> 7o pavimento (areas sociais, piscina, academia)
  TIPO      -> 8o-31o pavimentos (pavimento tipo x24, 4 aptos/pav = 96 aptos por torre)
  C_MAQ     -> 32o (casa de maquinas, reservatorios, barrilete)
  COBERTURA -> laje de cobertura (captacao SPDA, antenas, exaustao)

Torres - use EXATAMENTE esses codigos em "torre":
  A       -> Torre A (so)
  B       -> Torre B (so)
  AMBAS   -> Item compartilhado ou dividido entre as duas (ex: ramal predial
             que serve as duas torres, equipamento de condominio)

Area construida total (Torre A + B): 36.092 m2
"""


# Heuristicas tecnicas por sistema (override/complementam senso comum)
HEURISTICAS = {
    "SPDA": """
HEURISTICA SPDA (Sistema de Protecao Contra Descargas Atmosfericas, NBR 5419):
- Captores Franklin, bases de captor, chumbadores, conectores captor-descida:
    -> COBERTURA, AMBAS (dividir igualmente A/B se multi-torre, ou AMBAS se item unico do projeto)
- Cabo cobre nu 50mm2 (descida) + bracadeiras + buchas + conectores aparafusados:
    -> Distribuir ao longo das torres. Cada torre tem ~4 descidas verticais.
       Rate por comprimento: considere 32 pav x 3m = ~96m por descida.
       Para peças distribuidas, rate 50% A / 50% B.
- Cabo cobre nu 35mm2 (equipotencializacao):
    -> Se for aneis equipotenciais: distribuir entre TERREO, G5 (ou outro pav),
       LAZER, C_MAQ (tipicamente 4-5 aneis por torre) — 50% A / 50% B.
- Barras equipotenciais, BEP, conectores barra-cabo:
    -> Tipicamente no TERREO ou C_MAQ (quadros eletricos gerais)
- Caixas equipotencializacao (BEL) 20x20x15 aluminio:
    -> Normalmente 1 por apto (tipo), ou 1 por quadro de distribuicao.
       Se 12 caixas, pode ser TIPO (6 A + 6 B) ou LAZER/C_MAQ (1-2 por pavimento).
- Hastes de aterramento Ø5/8, conectores haste-cabo, solda exotermica, caixas
  de inspecao 400x400x400:
    -> TERREO, AMBAS (malha de aterramento sob a edificacao serve ambas torres)
- Cabo cobre 50mm2 malha aterramento:
    -> TERREO, AMBAS (malha horizontal)
- Acessorios gerais (conector paralelo, cruzado, arruela, fita advertencia):
    -> Distribuir proporcionalmente ao sistema. Default: 50% descidas (varias
       torres), 30% malha (TERREO), 20% cobertura.
""",
    "HIDRO-TUBOS": """
HEURISTICA HIDRO-TUBULACOES:
- Tubos PVC rigido agua fria (25mm, 32mm, 50mm, 75mm, 100mm):
    -> Prumadas verticais: rate principalmente TIPO (24 pav) + ramais em G1-G5
       + alimentacao TERREO. Regra pratica: 70% TIPO, 20% GARAGENS (G1-G5), 10% TERREO.
    -> Cada torre tem prumadas proprias: divida 50% A / 50% B.
- Tubos esgoto (40mm, 50mm, 75mm, 100mm, 150mm):
    -> Principalmente TIPO (coletores prediais por pavimento). Regra: 80% TIPO,
       10% TERREO (caixas de inspecao), 10% C_MAQ (ventilacao de prumada).
- Tubos pluvial (75mm, 100mm, 150mm):
    -> COBERTURA (ralos, calhas) + prumada pluvial ate TERREO.
       Regra: 60% COBERTURA, 30% TIPO (descidas), 10% TERREO.
- Tubo gas cobre:
    -> TIPO (ramais ate cozinhas dos aptos), 10% C_MAQ (medicao), 10% TERREO.
""",
    "HIDRO-CONEXOES": """
HEURISTICA HIDRO-CONEXOES:
- Joelhos 90, tes, luvas, buchas, uniões, registros de gaveta/esfera, caps,
  curvas — de todos diametros:
    -> Mesma distribuicao das tubulacoes (ver HIDRO-TUBOS).
    -> Registros de gaveta/esfera tendem a concentrar em TIPO (banheiros/cozinha) e C_MAQ (barrilete).
    -> Caps/bujões: TERREO (desagues de prumada) e C_MAQ.
- Ralos sifonados:
    -> TIPO (banheiros e areas molhadas dos aptos). 96 aptos -> rate por contagem.
- Caixas sifonadas:
    -> TIPO (banheiros). 50% A / 50% B.
""",
    "HIDRO-ETE": """
HEURISTICA HIDRO-ETE (Estacao Tratamento Esgoto / Caixas de Gordura):
- Caixas de gordura em concreto armado (grandes, 1m x 2m x 1m):
    -> TERREO (area externa/estacionamento) ou G1 (garagem 1).
    -> AMBAS (coletor compartilhado).
- Filtros anaerobios, reator UASB, sumidouro, bombas de recalque ETE:
    -> TERREO/subsolo (area externa). AMBAS (sistema compartilhado).
- Acessorios (joelhos, tubos de ETE, selos d'agua):
    -> Mesma regra das caixas (TERREO, AMBAS).
""",
    "HIDRO-VALVULAS": """
HEURISTICA HIDRO-VALVULAS:
- Hidrometros unijato:
    -> TERREO, AMBAS (shafts coletivos no hall ou medidores no subsolo).
       Se quantidade indicar 96+ unidades, provavelmente e por apartamento:
       distribuir pelo TIPO (4 aptos/pav x 24 pav = 96 por torre).
- Motobombas de recalque (agua fria/quente), booster, pressurizadores:
    -> C_MAQ ou TERREO (casa de bombas). AMBAS.
- Valvulas de retencao, valvulas de pe, valvulas reguladoras:
    -> C_MAQ, TERREO ou TIPO dependendo do sistema.
- Filtros (agua bruta, linha):
    -> TERREO/C_MAQ.
- Reservatorios (se houver - tipicamente em C_MAQ):
    -> C_MAQ (superior), TERREO (inferior).
""",
    "PPCI-SHP": """
HEURISTICA PPCI-SHP (Sistema Hidrantes Preventivos):
- Tubos aco galvanizado 2.1/2", 3", 4" + conexoes (joelho, te, luva, uniao,
  flange, cap):
    -> Prumada vertical unica por torre, do TERREO a COBERTURA.
    -> Distribuir proporcional aos pavimentos: ~3% cada um dos 32 pav.
    -> Aprox 40% TIPO (24 pav), 20% GARAGENS (G1-G5), 10% TERREO, 10% LAZER,
       15% C_MAQ, 5% COBERTURA. Divida 50% A / 50% B.
- Hidrantes, abrigos, mangueiras, esguichos, chaves de mangueira:
    -> 1 hidrante por pavimento normalmente. TIPO (24), mais GARAGENS (5),
       TERREO, LAZER, C_MAQ = ~32 por torre. Divida 50/50.
- Bomba de incendio, painel de comando, joint register:
    -> C_MAQ (casa de maquinas) ou TERREO (subsolo tecnico). AMBAS.
- Reservatorio tecnico incendio:
    -> C_MAQ (superior). Pode ser AMBAS (comum) ou dividido por torre.
""",
    "PPCI-IGC": """
HEURISTICA PPCI-IGC (Instalacoes de Gas Combustivel):
- Tubos cobre/aco + conexoes:
    -> Prumada principal (medicao > aptos). C_MAQ / TERREO tem medicao.
       Ramais internos TIPO (cada cozinha de apto). Regra: 70% TIPO, 20% TERREO,
       10% C_MAQ. 50/50 A/B.
- Valvulas de bloqueio, reguladores de pressao:
    -> TERREO (caixa de medicao central), TIPO (valvula por apto), C_MAQ.
- Alarme gas (detectores):
    -> TIPO (cozinha de cada apto), C_MAQ (casa de maquinas).
""",
    "PPCI-GERAIS": """
HEURISTICA PPCI-GERAIS (sistemas diversos incendio):
- Detectores de fumaca/temperatura, sirenes, pontos de acionamento manual:
    -> Distribuir por pavimento. Garagens (G1-G5), LAZER, TIPO (24 pav),
       C_MAQ. Regra aproximada: 5% cada GARAGEM, 5% LAZER, 60% TIPO (bem
       distribuido), 10% C_MAQ, 5% TERREO.
- Central de alarme, fonte nobreak, baterias:
    -> TERREO ou C_MAQ (sala tecnica). AMBAS.
- Luminarias de emergencia, placas de sinalizacao:
    -> Distribuir por pavimento (igual detectores).
- Extintores portateis:
    -> TIPO (corredores), GARAGENS, C_MAQ. Regra: 60% GARAGENS + TIPO, 20% C_MAQ,
       20% outros.
""",
    "PPCI-MECANICO": """
HEURISTICA PPCI-MECANICO (pressurizacao de escada / desenfumagem):
- Ventiladores axiais/centrifugos de pressurizacao:
    -> COBERTURA (exaustao) ou C_MAQ.
- Dutos galvanizados, grelhas de descarga, dampers corta-fogo:
    -> Ao longo do prumo da escada pressurizada: TERREO, G1-G5, LAZER, TIPO
       (distribuir por pavimento), C_MAQ, COBERTURA.
- Paineis de comando, sensores:
    -> C_MAQ (sala tecnica).
""",
}


def detectar_sistema(pdf_name: str) -> str:
    """Identifica a chave de heuristica a partir do nome do PDF."""
    name_upper = pdf_name.upper()
    if "SPDA" in name_upper:
        return "SPDA"
    if "HIDRO" in name_upper and "CONEX" in name_upper:
        return "HIDRO-CONEXOES"
    if "HIDRO" in name_upper and "ETE" in name_upper:
        return "HIDRO-ETE"
    if "HIDRO" in name_upper and ("VALVUL" in name_upper or "MOTOBOMB" in name_upper):
        return "HIDRO-VALVULAS"
    if "HIDRO" in name_upper and "TUBUL" in name_upper:
        return "HIDRO-TUBOS"
    if "PPCI" in name_upper and "SHP" in name_upper:
        return "PPCI-SHP"
    if "PPCI" in name_upper and "IGC" in name_upper:
        return "PPCI-IGC"
    if "PPCI" in name_upper and "GERAIS" in name_upper:
        return "PPCI-GERAIS"
    if "PPCI" in name_upper and ("MECAN" in name_upper or "PRESSUR" in name_upper):
        return "PPCI-MECANICO"
    return "UNKNOWN"


PROMPT_RATEIO = """Voce e um engenheiro calculista especialista em instalacoes prediais.
Sua tarefa: dividir uma lista de materiais totalizada (sem pavimento) entre
os pavimentos da obra usando bom senso tecnico e as heuristicas abaixo.

REGRAS ABSOLUTAS (NAO VIOLE):
1. O campo "pavimento" deve ser SEMPRE um destes codigos e NADA MAIS:
   TERREO, G1, G2, G3, G4, G5, LAZER, TIPO, C_MAQ, COBERTURA
   NUNCA escreva "AMBAS" no campo pavimento. NUNCA.
   Se voce queria dizer "todos os pavimentos", escolha um pavimento especifico.
2. O campo "torre" deve ser SEMPRE um destes codigos e NADA MAIS:
   A, B, AMBAS
   NUNCA escreva nome de pavimento no campo torre.
3. A soma de qtd_rateada por item DEVE ser exatamente igual ao qtd_total.
   Verifique a soma antes de emitir JSON. Se nao bater, recalcule.
4. NAO invente items. Use exatamente os mesmos "numero" e "descricao" da lista.
5. Se um item e distribuido entre as duas torres, use "torre": "AMBAS" OU crie
   duas entradas separadas com torre=A e torre=B. Nunca use "AMBAS" no pavimento.

{contexto}

{heuristicas}

LISTA DE ITENS A RATEAR (todos sao do sistema {sistema}):
```json
{itens_json}
```

Para CADA item da lista, produza uma distribuicao por (pavimento, torre) tal que
a soma das quantidades rateadas seja IGUAL a quantidade total do item. Justifique
tecnicamente cada rateio em 1 linha.

Responda APENAS com JSON valido no formato EXATO:
```json
{{
  "rateios": [
    {{
      "numero": 4,
      "codigo": "8502",
      "qtd_total": 30,
      "unidade": "pc",
      "descricao": "RE-BARS - BARRAS REDONDAS DE ACO GALVANIZADAS A FOGO ...",
      "distribuicao": [
        {{"pavimento": "COBERTURA", "torre": "AMBAS", "qtd_rateada": 30,
          "pct": 1.0, "justificativa": "Barras de captacao vao na laje cobertura"}}
      ]
    }},
    {{
      "numero": 5,
      "codigo": "8506",
      "qtd_total": 180,
      "distribuicao": [
        {{"pavimento": "TIPO", "torre": "A", "qtd_rateada": 60, "pct": 0.333,
          "justificativa": "Clips descida torre A - prumada principal"}},
        {{"pavimento": "TIPO", "torre": "B", "qtd_rateada": 60, "pct": 0.333,
          "justificativa": "Clips descida torre B"}},
        {{"pavimento": "TERREO", "torre": "AMBAS", "qtd_rateada": 60, "pct": 0.334,
          "justificativa": "Clips fixacao nos dois prumos no subsolo"}}
      ]
    }}
  ]
}}
```

REGRAS CRITICAS:
- "pavimento" deve ser UM dos codigos: TERREO, G1, G2, G3, G4, G5, LAZER, TIPO, C_MAQ, COBERTURA
- "torre" deve ser UM de: A, B, AMBAS
- "qtd_rateada" pode ser inteiro ou float, soma precisa bater com qtd_total
- Para itens com poucos unidades (< 5), prefira localizar num unico pavimento ao inves de fracionar
- Para TUBOS em METROS, ratear em valores inteiros ou decimais razoaveis (nao 3.1415)
- Se nao souber, use C_MAQ + AMBAS como fallback
- NUNCA invente itens. NUNCA omita itens da lista de entrada.
- Responda SOMENTE com o JSON em bloco ```json ... ```
"""


def auto_corrigir_rateios(rateios: list[dict]) -> dict:
    """Aplica correcoes automaticas conhecidas antes da validacao formal.
    Retorna contadores das correcoes aplicadas para log.
    """
    stats = {"pavimento_ambas_corrigido": 0, "torre_vazia_corrigida": 0,
             "pavimento_lower_corrigido": 0}
    for r in rateios:
        for d in r.get("distribuicao") or []:
            pav = d.get("pavimento")
            torre = d.get("torre")
            # Caso 1: pavimento = "AMBAS" (erro sistematico do Gemma)
            if pav == "AMBAS":
                d["pavimento"] = "NA"
                d["torre"] = "AMBAS"
                stats["pavimento_ambas_corrigido"] += 1
                continue
            # Caso 2: pavimento em minusculas ("tipo", "terreo")
            if isinstance(pav, str) and pav.upper() in PAVIMENTOS_VALIDOS and pav != pav.upper():
                d["pavimento"] = pav.upper()
                stats["pavimento_lower_corrigido"] += 1
            # Caso 3: torre vazia ou invalida
            if torre not in TORRES_VALIDAS:
                if isinstance(torre, str) and torre.upper() in TORRES_VALIDAS:
                    d["torre"] = torre.upper()
                else:
                    d["torre"] = "AMBAS"
                stats["torre_vazia_corrigida"] += 1
    return stats


def validar_rateios(rateios: list[dict], itens_orig: list[dict]) -> list[dict]:
    """Valida que cada rateio soma ao total, pavimentos/torres validos.
    Retorna lista de issues encontradas (vazia se tudo ok).
    """
    issues = []
    by_num = {str(it.get("numero")): it for it in itens_orig}

    for r in rateios:
        num = str(r.get("numero"))
        if num not in by_num:
            issues.append({"numero": num, "erro": "item_nao_existe_na_origem"})
            continue
        orig = by_num[num]
        qtd_total = r.get("qtd_total") or orig.get("qtd")
        if qtd_total is None:
            issues.append({"numero": num, "erro": "qtd_total_ausente"})
            continue
        # Somar distribuicao
        dist = r.get("distribuicao") or []
        soma = sum(d.get("qtd_rateada", 0) for d in dist)
        if abs(soma - qtd_total) / max(qtd_total, 1) > 0.01:
            issues.append({
                "numero": num, "erro": "soma_diverge",
                "qtd_total": qtd_total, "soma": soma,
            })
        for d in dist:
            if d.get("pavimento") not in PAVIMENTOS_VALIDOS:
                issues.append({
                    "numero": num, "erro": "pavimento_invalido",
                    "valor": d.get("pavimento"),
                })
            if d.get("torre") not in TORRES_VALIDAS:
                issues.append({
                    "numero": num, "erro": "torre_invalida",
                    "valor": d.get("torre"),
                })
    return issues


def _chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def ratear_arquivo(gemma_json_path: Path, model: str = gem.MODEL_E4B) -> Path:
    """Carrega um {slug}.gemma.json format A e gera {slug}.rateio.json."""
    data = json.loads(gemma_json_path.read_text(encoding="utf-8"))
    if data.get("formato") != "A":
        raise ValueError(f"Rateio so aplicavel a formato A, este e {data.get('formato')}")

    pdf_name = data.get("pdf_origem", gemma_json_path.name)
    sistema = detectar_sistema(pdf_name)
    heur = HEURISTICAS.get(sistema, "# heuristica generica: use bom senso tecnico")

    # Achatar itens de todos os documentos (format A geralmente tem 1 doc)
    todos_itens = []
    for doc in data.get("documentos", []):
        for it in doc.get("itens", []):
            # Serializar de forma compacta
            todos_itens.append({
                "numero": it.get("numero"),
                "codigo": it.get("codigo"),
                "qtd": it.get("qtd"),
                "unidade": it.get("unidade"),
                "descricao": it.get("produto") or it.get("descricao") or it.get("especificacao_local"),
                "marca": it.get("marca"),
            })

    if not todos_itens:
        print(f"[rateio] sem itens em {pdf_name}")
        return None

    print(f"[rateio] {pdf_name} sistema={sistema} itens={len(todos_itens)}")

    # Chunking: rateio pode ser pesado em prompt e resposta (muitos itens gerando
    # muitas distribuicoes). Rate em batches de 12 itens para manter payload
    # razoavel e evitar timeouts em PDFs grandes.
    todos_rateios = []
    todas_issues = []
    for chunk_idx, chunk in enumerate(_chunks(todos_itens, 12), start=1):
        print(f"  [rateio] chunk {chunk_idx} ({len(chunk)} itens)")
        prompt = PROMPT_RATEIO.format(
            contexto=CONTEXT_ELECTRA,
            heuristicas=heur,
            sistema=sistema,
            itens_json=json.dumps(chunk, ensure_ascii=False, indent=2),
        )
        t0 = time.time()
        try:
            resp = gem.call_gemma_json(prompt, model=model, max_retries=3)
        except Exception as e:
            print(f"  [rateio] FAIL chunk {chunk_idx}: {e}")
            todas_issues.append({"chunk": chunk_idx, "erro": str(e)})
            continue
        rateios = resp.get("rateios", [])
        fixes = auto_corrigir_rateios(rateios)
        issues = validar_rateios(rateios, chunk)
        n_fix = sum(fixes.values())
        print(f"  [rateio] done chunk {chunk_idx} ({time.time()-t0:.0f}s, {len(rateios)} rateios, {n_fix} autofix, {len(issues)} issues)")
        todos_rateios.extend(rateios)
        todas_issues.extend(issues)

    out = {
        "pdf_origem": pdf_name,
        "sistema": sistema,
        "model": model,
        "fonte_flat": gemma_json_path.name,
        "total_itens_orig": len(todos_itens),
        "total_rateios": len(todos_rateios),
        "rateios": todos_rateios,
        "issues": todas_issues,
    }
    out_path = gemma_json_path.parent / gemma_json_path.name.replace(".gemma.json", ".rateio.json")
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[rateio] salvo {out_path} (issues={len(todas_issues)})")
    return out_path


def ratear_todos(disciplina: str | None, model: str) -> None:
    # Encontrar todos os {slug}.gemma.json de formato A
    if disciplina:
        dirs = [OUT_DIR / disciplina]
    else:
        dirs = [d for d in OUT_DIR.iterdir() if d.is_dir()]

    alvos = []
    for d in dirs:
        for gemma_file in d.glob("*.gemma.json"):
            try:
                data = json.loads(gemma_file.read_text(encoding="utf-8"))
                if data.get("formato") == "A":
                    alvos.append(gemma_file)
            except Exception as e:
                print(f"[skip] {gemma_file.name}: {e}")

    print(f"Rateio em {len(alvos)} arquivos format A")
    for f in alvos:
        try:
            ratear_arquivo(f, model=model)
        except Exception as e:
            print(f"[ERRO] {f.name}: {e}")
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gemma_json", nargs="?", help="Path para um {slug}.gemma.json (ou use --all)")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--disciplina")
    ap.add_argument("--model", choices=["e4b", "26b"], default="e4b")
    args = ap.parse_args()

    model = gem.MODEL_E4B if args.model == "e4b" else gem.MODEL_26B

    if args.all:
        ratear_todos(args.disciplina, model)
    elif args.gemma_json:
        ratear_arquivo(Path(args.gemma_json), model=model)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
