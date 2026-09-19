#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""fonte_memorial.py — fonte Memorial Cartesiano -> staging custos_historica.

Lê (somente leitura) o Supabase do Memorial (projeto `specifications`) e escreve
o MESMO staging que `carregar_fato_supabase.py` já sobe pro indices-cartesian:

    _local/base-custos-historica/staging/<slug>/projeto.json
    _local/base-custos-historica/staging/<slug>/itens.jsonl

Duas fontes, dois rótulos de leva (chave de upsert junto com slug):
    memorial-referencia-cliente   <- budget_client_reference_imports/items (lote = import_batch_id)
    memorial-versao-cartesian     <- budget_versions.snapshot (lote = version_id)

Identidade e data-base são decididas ANTES da carga (arquivo de overrides no
repo do CUB); AC entra como candidatas e é confirmada no app de revisão.
SPEC: C:\Apps\cub-cartesian\docs\superpowers\specs\2026-09-18-base-viva-memorial-design.md

Uso:
    py -3.10 scripts/custos_historica/fonte_memorial.py listar
    py -3.10 scripts/custos_historica/fonte_memorial.py coletar --dry-run
    py -3.10 scripts/custos_historica/fonte_memorial.py coletar --apply
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ----------------------------------------------------------------------------
# Constantes (SPEC §5–§6)
# ----------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = REPO_ROOT / ".env.memorial"
STAGING_ROOT = Path(r"C:\Users\leona\openclaw\_local\base-custos-historica\staging")
SNAPSHOT_ROOT = Path(r"C:\Users\leona\openclaw\_local\base-custos-historica\snapshots\memorial")
CUB_OVERRIDES_DIR = Path(r"C:\Apps\cub-cartesian\data\overrides")

FONTE_CLIENTE = "memorial-referencia-cliente"
FONTE_CARTESIAN = "memorial-versao-cartesian"
MEMORIAL_MIN_FOLHAS = 50
RECONCILIACAO_TOL = 0.02
DATA_BASE_MIN = date(2015, 1, 1)
AC_CONCORDANCIA_PCT = 5.0
IMPORT_FLOW_ELEGIVEL = "referencia_cliente_completa"
SCRIPT_VERSION = "fonte_memorial.py@v1"

_PREFIXO_NUMERICO = re.compile(r"^\s*(?:item\s*)?\d+(?:[.\-\s]+\d+)*[.\-\s)]*\s*", re.IGNORECASE)


# ----------------------------------------------------------------------------
# Modelo
# ----------------------------------------------------------------------------
@dataclass
class Lote:
    fonte: str
    lote_id: str
    project_id: str
    client_id: str | None
    projeto_nome: str
    cliente_nome: str | None
    cidade: str | None
    is_reference_template: bool
    itens: list[dict]
    data_base: str | None
    data_base_origem: str | None
    data_base_confianca: str | None
    total_declarado: Decimal | None
    revisao: str | None
    ac: dict | None
    quarentena: str | None
    # ordenação entre lotes concorrentes do mesmo (slug, fonte, vintage) — ruling C1
    version_number: int | None = None
    criado_em: str | None = None


# ----------------------------------------------------------------------------
# Utilidades puras
# ----------------------------------------------------------------------------
def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", str(text)) if not unicodedata.combining(c))


def slugify(text: str) -> str:
    t = strip_accents(text or "").lower()
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


def slug_memorial(cliente: str, projeto: str) -> str:
    return f"memorial-{slugify(cliente)}-{slugify(projeto)}"


def to_decimal(value: Any) -> Decimal | None:
    if value is None or value == "":
        return None
    try:
        return Decimal(str(value).replace(",", "."))
    except (InvalidOperation, ValueError):
        return None


def _dec_str(v: Decimal | None) -> str | None:
    """Mesmo contrato do loader/CUB (`decimal_to_str`): sem zeros à direita, sem notação científica."""
    if v is None:
        return None
    return format(v.normalize(), "f")


def vintage_de(data_base_iso: str | None) -> str | None:
    """Trimestre da data-base, MESMA regra do loader (`vintage_from_data_base`):
    `YYYY` + `Q` + trimestre. Ex.: 2026-05-18 -> '2026Q2'."""
    if not data_base_iso:
        return None
    try:
        d = date.fromisoformat(str(data_base_iso)[:10])
    except ValueError:
        return None
    return f"{d.year}Q{(d.month - 1) // 3 + 1}"


def fonte_leva_com_vintage(fonte: str, data_base_iso: str | None) -> str:
    """Rótulo de leva com o trimestre embutido (ruling C1): a chave de upsert do
    loader é `(slug, fonte_leva)`, então safras diferentes da MESMA obra e da
    MESMA fonte precisam de rótulos diferentes pra não colidirem."""
    v = vintage_de(data_base_iso)
    return f"{fonte}@{v}" if v else fonte


def carregar_regras_quarentena(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def motivo_quarentena(lote: Lote, regras: dict) -> str | None:
    if lote.is_reference_template:
        return "is_reference_template"
    clientes = {strip_accents(c).lower().strip() for c in regras.get("clientes", [])}
    if lote.cliente_nome and strip_accents(lote.cliente_nome).lower().strip() in clientes:
        return "cliente_em_quarentena"
    rx = re.compile(regras.get("regex_nome", "$^"), re.IGNORECASE)
    for nome in (lote.projeto_nome, lote.cliente_nome or ""):
        if rx.search(strip_accents(nome)):
            return "nome_casa_regex"
    return None


def _data_valida(iso: str | None, hoje: date) -> bool:
    if not iso:
        return False
    try:
        d = date.fromisoformat(str(iso)[:10])
    except ValueError:
        return False
    return DATA_BASE_MIN <= d <= hoje


def escolher_data_base(
    candidatas: list[tuple[str | None, str]],
    fallback: tuple[str, str],
    hoje: date,
) -> tuple[str, str, str]:
    """Primeira candidata válida (2015 <= d <= hoje) é 'alta'; senão fallback 'baixa'."""
    for iso, origem in candidatas:
        if _data_valida(iso, hoje):
            return str(iso)[:10], origem, "alta"
    iso, origem = fallback
    return str(iso)[:10], origem, "baixa"


def _id_do_item(row: dict, chaves: tuple[str, ...], mensagem: str) -> str:
    """Primeira chave de id presente; sem nenhuma, erro claro (C4) em vez de KeyError."""
    for chave in chaves:
        valor = row.get(chave)
        if valor not in (None, ""):
            return str(valor)
    raise ValueError(mensagem)


def _id_snapshot(item: dict, version_id: str | None) -> str:
    return _id_do_item(item, ("item_id", "id"), f"snapshot.items sem chave de id (item_id/id) — versão {version_id}")


def normalizar_itens_cliente(rows: list[dict]) -> list[dict]:
    return [
        {
            "item_id": _id_do_item(r, ("id", "item_id"),
                                   "budget_client_reference_items sem chave de id (id/item_id)"),
            "parent_id": str(r["parent_id"]) if r.get("parent_id") else None,
            "level": int(r["level"]) if r.get("level") is not None else None,
            "seq": int(r["sort_order"]) if r.get("sort_order") is not None else None,
            "codigo": r.get("line_code"),
            "descricao": r.get("description") or "",
            "unidade": r.get("unit"),
            "qtd": to_decimal(r.get("quantity")),
            "pu": to_decimal(r.get("client_unit_cost")),
            "total": to_decimal(r.get("client_total_price")),
            "is_leaf": False,
        }
        for r in rows
    ]


def normalizar_itens_snapshot(items: list[dict], version_id: str | None = None) -> list[dict]:
    return [
        {
            "item_id": _id_snapshot(i, version_id),
            "parent_id": str(i["parent_id"]) if i.get("parent_id") else None,
            "level": int(i["level"]) if i.get("level") is not None else None,
            "seq": int(i["sequence"]) if i.get("sequence") is not None else None,
            "codigo": i.get("code"),
            "descricao": i.get("description") or i.get("name") or "",
            "unidade": i.get("unit"),
            "qtd": to_decimal(i.get("quantity")),
            "pu": to_decimal(i.get("unit_price")),
            "total": to_decimal(i.get("total_price")),
            "is_leaf": bool(i.get("is_leaf")),
        }
        for i in items
    ]


def folhas(itens: list[dict], modo: str) -> list[dict]:
    if modo == "is_leaf":
        return [i for i in itens if i.get("is_leaf")]
    if modo == "nivel_max":
        niveis = [i["level"] for i in itens if i.get("level") is not None]
        if not niveis:
            return []
        lmax = max(niveis)
        return [i for i in itens if i.get("level") == lmax]
    raise ValueError(f"modo invalido: {modo}")


def atribuir_macrogrupo(itens: list[dict]) -> list[dict]:
    """aba = descrição do ancestral nível 0; macrogrupo = ancestral nível 1 sem prefixo 'NN.'."""
    by_id = {i["item_id"]: i for i in itens}
    out = []
    for item in itens:
        aba = None
        macro = None
        cur = item
        visitados = set()
        while cur is not None and cur["item_id"] not in visitados:
            visitados.add(cur["item_id"])
            if cur.get("level") == 0:
                aba = cur.get("descricao") or None
            if cur.get("level") == 1:
                macro = _PREFIXO_NUMERICO.sub("", cur.get("descricao") or "").strip() or None
            cur = by_id.get(cur["parent_id"]) if cur.get("parent_id") else None
        novo = dict(item)
        novo["aba"] = aba
        novo["macrogrupo"] = macro
        out.append(novo)
    return out


def reconciliar(soma_folhas: Decimal, soma_referencia: Decimal | None, tol: float = RECONCILIACAO_TOL) -> tuple[Decimal | None, bool]:
    if soma_referencia is None or soma_referencia == 0:
        return None, False
    pct = (soma_folhas - soma_referencia) / soma_referencia * Decimal(100)
    return pct.quantize(Decimal("0.01")), abs(pct) <= Decimal(str(tol * 100))


def ac_candidatas(
    area_pavimentos: Decimal | None,
    n_pavimentos: int,
    n_torres: int,
    area_empreendimento: Decimal | None,
    ac_cub_atual: Decimal | None,
) -> dict:
    out: dict[str, Any] = {}
    if area_pavimentos:
        out["pavimentos"] = {"valor": _dec_str(area_pavimentos), "n_pavimentos": n_pavimentos, "n_torres": n_torres,
                             "origem": "sum(tower_floors.floor_area)"}
    if area_empreendimento:
        out["empreendimento"] = {"valor": _dec_str(area_empreendimento), "origem": "project_building_data.enterprise_area"}
    if ac_cub_atual:
        out["cub_atual"] = {"valor": _dec_str(ac_cub_atual), "origem": "fato_projetos.ac_m2"}
    valores = [Decimal(v["valor"]) for v in out.values()]
    concordam = len(valores) >= 2 and (max(valores) - min(valores)) / max(valores) * 100 <= Decimal(str(AC_CONCORDANCIA_PCT))
    out["concordam"] = bool(concordam)
    return out


# ----------------------------------------------------------------------------
# Snapshot content-addressed (SPEC v0.2 §6.3)
# ----------------------------------------------------------------------------
def _json_default(o: Any):
    if isinstance(o, Decimal):
        return _dec_str(o)
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    raise TypeError(f"nao serializavel: {type(o)!r}")


def canonical_jsonl(rows: list[dict]) -> bytes:
    linhas = sorted(json.dumps(r, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=_json_default) for r in rows)
    return ("\n".join(linhas) + ("\n" if linhas else "")).encode("utf-8")


def conteudo_por_dataset(extratos: dict[str, list[dict]]) -> dict[str, tuple[bytes, str]]:
    """`{dataset: (bytes canônicos, sha256)}` — uma única passada de `canonical_jsonl`
    por dataset (I5: antes era recalculado 3x: id, arquivo e content_hashes)."""
    out: dict[str, tuple[bytes, str]] = {}
    for ds, rows in extratos.items():
        blob = canonical_jsonl(rows)
        out[ds] = (blob, hashlib.sha256(blob).hexdigest())
    return out


def _snapshot_id_de(conteudo: dict[str, tuple[bytes, str]]) -> str:
    manifest = {ds: sha for ds, (_blob, sha) in conteudo.items()}
    canon = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(canon).hexdigest()


def snapshot_id(extratos: dict[str, list[dict]]) -> str:
    return _snapshot_id_de(conteudo_por_dataset(extratos))


_MANIFEST_CHAVES_RESERVADAS = frozenset({
    "source_snapshot_id", "source_system", "adapter_version",
    "extracted_at", "contagens", "content_hashes", "params",
})


def gravar_snapshot(root: Path, extratos: dict[str, list[dict]], meta: dict) -> tuple[str, Path]:
    conflitos = _MANIFEST_CHAVES_RESERVADAS & set(meta)
    if conflitos:
        raise ValueError(f"meta nao pode usar chave(s) reservada(s) do manifesto: {sorted(conflitos)}")

    conteudo = conteudo_por_dataset(extratos)
    sid = _snapshot_id_de(conteudo)
    content_root = Path(root) / "content"
    content_dir = content_root / sid
    if not content_dir.exists():
        # escreve num diretorio temporario irmao e so entao renomeia atomicamente:
        # uma interrupcao no meio da escrita nunca deixa content/<sid> parcial, e
        # "create-once" nao pode ficar preso lendo um conteudo corrompido.
        content_root.mkdir(parents=True, exist_ok=True)
        tmp_dir = Path(tempfile.mkdtemp(prefix=f".tmp-{sid}-", dir=content_root))
        try:
            for ds, (blob, _sha) in conteudo.items():
                (tmp_dir / f"{ds}.jsonl").write_bytes(blob)
            if content_dir.exists():
                # corrida: outra chamada concluiu primeiro; descarta o tmp e segue create-once
                shutil.rmtree(tmp_dir, ignore_errors=True)
            else:
                os.replace(tmp_dir, content_dir)
        except BaseException:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            raise

    manifest = {
        "source_snapshot_id": sid,
        "source_system": "memorial-cartesiano",
        "adapter_version": SCRIPT_VERSION,
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "contagens": {ds: len(rows) for ds, rows in extratos.items()},
        "content_hashes": {ds: sha for ds, (_blob, sha) in conteudo.items()},
        "params": meta,
    }
    manifests_dir = Path(root) / "manifests"
    manifests_dir.mkdir(parents=True, exist_ok=True)
    mchk = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode("utf-8")).hexdigest()
    mpath = manifests_dir / f"{mchk}.json"
    if not mpath.exists():
        mpath.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return sid, mpath


# ----------------------------------------------------------------------------
# Leitura do Memorial (read-only)
# ----------------------------------------------------------------------------
def carregar_env(env_file: Path = ENV_FILE) -> tuple[str, str]:
    if not Path(env_file).exists():
        raise RuntimeError(f"credencial do Memorial ausente: crie {env_file} com SUPABASE_URL e SUPABASE_SECRET_KEY (chave de leitura dedicada)")
    from dotenv import dotenv_values
    env = dotenv_values(env_file)
    url, key = env.get("SUPABASE_URL"), env.get("SUPABASE_SECRET_KEY")
    if not url or not key:
        raise RuntimeError(f"{env_file}: SUPABASE_URL/SUPABASE_SECRET_KEY nao preenchidos")
    return str(url), str(key)


class MemorialClient:
    def __init__(self, url: str, key: str, page_size: int = 1000):
        from supabase import create_client
        self.sb = create_client(url, key)
        self.page_size = page_size

    def fetch(self, table: str, select: str, order: str = "id", **filters: Any) -> list[dict]:
        out: list[dict] = []
        start = 0
        while True:
            q = self.sb.table(table).select(select)
            for col, val in filters.items():
                if col.endswith("__gte"):
                    q = q.gte(col[:-5], val)
                else:
                    q = q.eq(col, val)
            q = q.order(order).range(start, start + self.page_size - 1)
            data = q.execute().data or []
            out.extend(data)
            if len(data) < self.page_size:
                return out
            start += self.page_size


def extrair(client: MemorialClient, desde: str | None = None) -> dict[str, list[dict]]:
    imports = client.fetch(
        "budget_client_reference_imports",
        "id,budget_id,budget_version_id,project_id,client_id,import_batch_id,import_flow_type,status,is_active,imported_at,template_version,source_file_hash",
        status="completed", is_active=True, import_flow_type=IMPORT_FLOW_ELEGIVEL,
        **({"imported_at__gte": desde} if desde else {}),
    )
    import_items: list[dict] = []
    for im in imports:
        import_items.extend(client.fetch(
            "budget_client_reference_items",
            "id,import_id,parent_id,level,sort_order,line_code,description,unit,quantity,client_unit_cost,client_total_price",
            # I2: `sort_order` repete dentro do lote -> paginação por range ficaria instável.
            # A ordem de leitura é por `id` (único); `sort_order` segue virando o `seq` do staging.
            order="id", import_id=im["id"],
        ))
    versions = client.fetch("budget_versions", "version_id,budget_id,version_number,created_at,snapshot", order="version_id",
                            **({"created_at__gte": desde} if desde else {}))
    budgets = client.fetch("budgets", "budget_id,project_id,client_id,name,project_name,client_name,city,state,effective_date,total_value,version_number,is_reference_template,budget_type", order="budget_id")
    projects = client.fetch("projects", "id,project_name,client_id,city,state,status")
    clients = client.fetch("clients", "id,name,city,state")
    towers = client.fetch("project_towers", "tower_id,project_id,tower_name", order="tower_id")
    floors = client.fetch("tower_floors", "floor_id,tower_id,floor_name,floor_area", order="floor_id")
    building = client.fetch("project_building_data", "id,project_id,enterprise_area")
    return {
        "imports": imports, "import_items": import_items, "versions": versions, "budgets": budgets,
        "projects": projects, "clients": clients, "project_towers": towers, "tower_floors": floors,
        "project_building_data": building,
    }


def filtrar_por_projeto(extratos: dict[str, list[dict]], project_id: str) -> dict[str, list[dict]]:
    """`--projeto <uuid>` (I8): recorta os extratos a um projeto só, DEPOIS da extração
    (a extração continua simples) e ANTES de montar lotes. `versions` vem por
    `budgets.project_id`, que é onde a versão sabe de que projeto é."""
    ex = dict(extratos)
    alvo = str(project_id)
    imports = [im for im in ex.get("imports", []) if str(im.get("project_id") or "") == alvo]
    ids_import = {im.get("id") for im in imports}
    budgets_do_projeto = {b.get("budget_id") for b in ex.get("budgets", []) if str(b.get("project_id") or "") == alvo}
    ex["imports"] = imports
    ex["import_items"] = [it for it in ex.get("import_items", []) if it.get("import_id") in ids_import]
    ex["versions"] = [v for v in ex.get("versions", []) if v.get("budget_id") in budgets_do_projeto]
    return ex


# ----------------------------------------------------------------------------
# Similaridade (cópia de cub.validacao.join_realizado — manter idêntica)
# ----------------------------------------------------------------------------
NOISE_TOKENS = {"empreendimentos", "empreendimento", "construtora", "construcoes", "incorporadora", "incorporacoes",
                "engenharia", "ltda", "residencial", "residence", "e", "de", "da", "do", "dos", "das"}
_DATE_TOKEN_RE = re.compile(r"^\d{1,4}$")


def normalize_empreendimento(nome: str) -> str:
    text = strip_accents(str(nome)).lower()
    text = text.replace("_", "-").replace("/", "-").replace(".", "-")
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    tokens = [tok for tok in text.replace("-", " ").split() if tok]
    kept = [tok for tok in tokens if tok not in NOISE_TOKENS and not _DATE_TOKEN_RE.match(tok)]
    return " ".join(kept)


def extract_empreendimento_from_slug(slug: str) -> str:
    tokens = str(slug).split("-")
    last_numeric_idx = None
    for idx, tok in enumerate(tokens):
        if _DATE_TOKEN_RE.match(tok):
            last_numeric_idx = idx
    if last_numeric_idx is not None and last_numeric_idx + 1 < len(tokens):
        remainder = tokens[last_numeric_idx + 1:]
    else:
        remainder = tokens[-2:] if len(tokens) >= 2 else tokens
    return " ".join(remainder)


def _trigrams(text: str) -> set[str]:
    if len(text) < 3:
        return {text} if text else set()
    return {text[i:i + 3] for i in range(len(text) - 2)}


def trigram_similarity(a: str, b: str) -> float:
    a_norm = strip_accents(str(a)).lower().strip()
    b_norm = strip_accents(str(b)).lower().strip()
    if not a_norm or not b_norm:
        return 0.0
    if a_norm == b_norm:
        return 1.0
    ga, gb = _trigrams(a_norm), _trigrams(b_norm)
    if not ga or not gb:
        return 0.0
    return (2.0 * len(ga & gb)) / (len(ga) + len(gb))


# ----------------------------------------------------------------------------
# Lotes (SPEC §5)
# ----------------------------------------------------------------------------
def _soma(itens: Iterable[dict]) -> Decimal:
    return sum((i["total"] for i in itens if i.get("total") is not None), Decimal(0))


def _ac_do_projeto(project_id: str, ex: dict[str, list[dict]], ac_cub_atual: Decimal | None = None) -> dict:
    torres = [t for t in ex["project_towers"] if t["project_id"] == project_id]
    tower_ids = {t["tower_id"] for t in torres}
    pisos = [f for f in ex["tower_floors"] if f["tower_id"] in tower_ids]
    area_pav = sum((to_decimal(f["floor_area"]) or Decimal(0) for f in pisos), Decimal(0)) if pisos else None
    emp = next((to_decimal(d["enterprise_area"]) for d in ex["project_building_data"] if d["project_id"] == project_id), None)
    return ac_candidatas(area_pav, len(pisos), len(torres), emp, ac_cub_atual)


def montar_lotes(extratos: dict[str, list[dict]], hoje: date) -> list[Lote]:
    ex = extratos
    projects = {p["id"]: p for p in ex["projects"]}
    clients = {c["id"]: c for c in ex["clients"]}
    lotes: list[Lote] = []

    # Fonte A — orçamento de referência do cliente, agrupado por lote de importação
    grupos: dict[str, list[dict]] = {}
    for im in ex["imports"]:
        chave = im.get("import_batch_id") or f"{im['project_id']}|{str(im['imported_at'])[:10]}"
        grupos.setdefault(chave, []).append(im)
    itens_por_import: dict[str, list[dict]] = {}
    for it in ex["import_items"]:
        itens_por_import.setdefault(it["import_id"], []).append(it)
    for chave, ims in sorted(grupos.items()):
        proj = projects.get(ims[0]["project_id"], {})
        cli = clients.get(ims[0].get("client_id") or proj.get("client_id"), {})
        brutos: list[dict] = []
        for im in ims:
            brutos.extend(normalizar_itens_cliente(itens_por_import.get(im["id"], [])))
        com_macro = atribuir_macrogrupo(brutos)
        nivel1 = [i for i in com_macro if i.get("level") == 1]
        folhas_a = folhas(com_macro, "nivel_max")
        imported_at = min(str(im["imported_at"])[:10] for im in ims)
        data_base, origem, conf = escolher_data_base([], (imported_at, "budget_client_reference_imports.imported_at"), hoje)
        project_id_a = ims[0].get("project_id") or ""
        # I1: espelha a guarda da fonte B — sem project_id não há chave de identidade confiável.
        lotes.append(Lote(
            fonte=FONTE_CLIENTE, lote_id=chave, project_id=project_id_a, client_id=cli.get("id"),
            projeto_nome=proj.get("project_name") or "", cliente_nome=cli.get("name"), cidade=proj.get("city") or cli.get("city"),
            is_reference_template=False, itens=folhas_a, data_base=data_base, data_base_origem=origem, data_base_confianca=conf,
            total_declarado=_soma(nivel1) or None, revisao=None, ac=_ac_do_projeto(project_id_a, ex),
            quarentena=None if project_id_a else "sem_project_id",
            version_number=None, criado_em=max(str(im["imported_at"]) for im in ims),
        ))

    # Fonte B — versão precificada pela Cartesian
    budgets = {b["budget_id"]: b for b in ex["budgets"]}
    for v in ex["versions"]:
        snap = v.get("snapshot") or {}
        bud = budgets.get(v["budget_id"], {})
        proj = projects.get(bud.get("project_id"), {})
        cli = clients.get(bud.get("client_id") or proj.get("client_id"), {})
        itens_b = atribuir_macrogrupo(normalizar_itens_snapshot(snap.get("items") or [], version_id=v.get("version_id")))
        folhas_b = [i for i in folhas(itens_b, "is_leaf") if i.get("total")]
        if not bud.get("project_id"):
            # sem project_id nao ha chave de identidade confiavel: nunca elegivel, mesmo com folhas suficientes
            quarentena = "sem_project_id"
        else:
            quarentena = "poucas_folhas" if len(folhas_b) < MEMORIAL_MIN_FOLHAS else None
        data_base, origem, conf = escolher_data_base(
            [(bud.get("effective_date"), "budgets.effective_date"), ((snap.get("budget") or {}).get("effective_date"), "snapshot.budget.effective_date")],
            (str(v["created_at"])[:10], "budget_versions.created_at"), hoje,
        )
        lotes.append(Lote(
            fonte=FONTE_CARTESIAN, lote_id=str(v["version_id"]), project_id=bud.get("project_id") or "", client_id=cli.get("id"),
            projeto_nome=bud.get("project_name") or proj.get("project_name") or bud.get("name") or "",
            cliente_nome=bud.get("client_name") or cli.get("name"), cidade=bud.get("city") or proj.get("city"),
            is_reference_template=bool(bud.get("is_reference_template")), itens=folhas_b, data_base=data_base, data_base_origem=origem,
            data_base_confianca=conf, total_declarado=to_decimal(bud.get("total_value")) or _soma(i for i in itens_b if i.get("level") == 1) or None,
            revisao=str(v.get("version_number")) if v.get("version_number") is not None else None,
            ac=_ac_do_projeto(bud.get("project_id") or "", ex), quarentena=quarentena,
            version_number=int(v["version_number"]) if v.get("version_number") is not None else None,
            criado_em=str(v.get("created_at") or ""),
        ))
    return lotes


def _ordem_lote(lote: Lote) -> tuple[int, str]:
    """Qual lote vence entre concorrentes do mesmo (slug, fonte, vintage): maior
    `version_number` (fonte B) e, no empate, o mais recente (`created_at` /
    `imported_at` do lote, fonte A)."""
    vn = lote.version_number if lote.version_number is not None else -1
    return (vn, str(lote.criado_em or ""))


def reduzir_lotes(prontos: list[tuple[Lote, str]]) -> list[tuple[Lote, str]]:
    """Um lote por (slug, fonte, vintage) — ruling C1. Sem isso, dois lotes da mesma
    obra/safra escreveriam o MESMO `staging/<slug>` e o slug apareceria duas vezes
    em `memorial_obras.json` (e os itens acumulariam no CUB)."""
    melhor: dict[tuple[str, str, str], tuple[Lote, str]] = {}
    for lote, slug in prontos:
        chave = (slug, lote.fonte, vintage_de(lote.data_base) or "")
        atual = melhor.get(chave)
        if atual is None or _ordem_lote(lote) > _ordem_lote(atual[0]):
            melhor[chave] = (lote, slug)
    return [melhor[k] for k in sorted(melhor)]


# ----------------------------------------------------------------------------
# Identidade (SPEC §6.1–§6.2, §6.4)
# ----------------------------------------------------------------------------
def propor_candidatos(lote: Lote, slugs_existentes: dict[str, dict]) -> list[dict]:
    alvo = normalize_empreendimento(f"{lote.cliente_nome or ''} {lote.projeto_nome}")
    alvo_proj = normalize_empreendimento(lote.projeto_nome)
    alvo_cli = normalize_empreendimento(lote.cliente_nome or "")
    scored = []
    for slug in slugs_existentes:
        core = normalize_empreendimento(extract_empreendimento_from_slug(slug))
        cheio = normalize_empreendimento(slug.replace("-", " "))
        # muitos slugs do CUB sao so a construtora (sem o empreendimento) -> compara cliente x slug inteiro tambem
        score = max(
            trigram_similarity(alvo_proj, core),
            trigram_similarity(alvo, cheio),
            trigram_similarity(alvo_cli, cheio) if alvo_cli else 0.0,
        )
        scored.append({"slug": slug, "score": round(score, 4)})
    scored.sort(key=lambda c: (-c["score"], c["slug"]))
    return scored[:3]


def carregar_slug_overrides(path: Path) -> dict[str, dict]:
    if not Path(path).exists():
        return {}
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return {str(r["memorial_project_id"]): r for r in payload.get("rows", [])}


def resolver_identidade(lote: Lote, overrides: dict[str, dict]) -> tuple[str | None, str | None]:
    ov = overrides.get(lote.project_id)
    if not ov or not ov.get("slug_cub"):
        return None, "sem_decisao_de_slug"
    if lote.data_base_confianca == "baixa":
        confirmada = ov.get("data_base_confirmada")
        if not confirmada:
            return None, "data_base_nao_confirmada"
        lote.data_base = str(confirmada)[:10]
        lote.data_base_origem = "override.data_base_confirmada"
        lote.data_base_confianca = "confirmada"
    slug = slug_memorial(lote.cliente_nome or "sem-cliente", lote.projeto_nome) if ov["slug_cub"] == "NOVO" else str(ov["slug_cub"])
    return slug, None


def escrever_pendentes(staging_root: Path, pendentes: list[dict]) -> Path:
    d = Path(staging_root) / "_pendentes"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"depara_memorial_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    p.write_text(json.dumps(pendentes, ensure_ascii=False, indent=2, default=_json_default), encoding="utf-8")
    return p


# ----------------------------------------------------------------------------
# Staging (contrato do carregar_fato_supabase.py)
#
# CONTRATO DO DIRETÓRIO (F2): o loader recebe como argumento posicional o NOME DO
# DIRETÓRIO de staging, não o slug. No Drive os dois coincidem; no Memorial o
# diretório é `<slug>@<fonte_leva com trimestre>` — a mesma obra pode ter, na mesma
# safra, um lote da fonte cliente e um da fonte Cartesian, e eles são registros
# datados distintos que não podem dividir (nem sobrescrever) a mesma pasta. O slug
# real continua em `projeto.json["slug"]` e em cada linha de `itens.jsonl`, que é
# o que vai pro banco.
# ----------------------------------------------------------------------------
def diretorio_staging(slug: str, fonte_leva: str) -> str:
    """Nome da pasta de staging de um lote: `<slug>@<fonte_leva>` (F2)."""
    return f"{slug}@{fonte_leva}"


def montar_staging(lote: Lote, slug: str, sid: str) -> tuple[dict, list[dict]]:
    soma_folhas = _soma(lote.itens)
    pct, ok = reconciliar(soma_folhas, lote.total_declarado)
    projeto = {
        "slug": slug,
        "ac": None,
        "total": _dec_str(soma_folhas),
        "data_base": lote.data_base,
        "cidade": lote.cidade,
        "fonte": f"memorial:{lote.fonte}:{lote.lote_id}",
        "memorial": {
            # C1: o rótulo de leva leva o trimestre (chave de upsert = slug + fonte_leva).
            "fonte_leva": fonte_leva_com_vintage(lote.fonte, lote.data_base),
            "fonte_base": lote.fonte, "vintage": vintage_de(lote.data_base),
            "lote_id": lote.lote_id, "project_id": lote.project_id, "client_id": lote.client_id,
            "projeto": lote.projeto_nome, "cliente": lote.cliente_nome, "revisao": lote.revisao,
            "source_snapshot_id": sid, "total_declarado": _dec_str(lote.total_declarado),
            "reconciliacao_pct": _dec_str(pct), "reconciliacao_ok": ok,
            "data_base_origem": lote.data_base_origem, "data_base_confianca": lote.data_base_confianca,
            "ac_candidatas": lote.ac or {}, "quarentena": lote.quarentena,
        },
    }
    itens = [
        {
            "slug": slug, "source_sha1": sid, "source_sheet": lote.lote_id, "source_row": it.get("seq") if it.get("seq") is not None else idx,
            "codigo": it.get("codigo"), "descricao": it.get("descricao"), "unidade": it.get("unidade"),
            "qtd": _dec_str(it.get("qtd")), "pu": _dec_str(it.get("pu")), "total": _dec_str(it.get("total")),
            "aba": it.get("aba"), "macrogrupo": it.get("macrogrupo"),
            "data_base": lote.data_base, "data_base_origem": lote.data_base_origem, "data_base_confianca": lote.data_base_confianca,
            "revisao": lote.revisao,
        }
        for idx, it in enumerate(lote.itens)
    ]
    # source_row precisa ser único dentro do (sha1, sheet): desempata por posição quando seq repete
    vistos: set = set()
    for idx, row in enumerate(itens):
        if row["source_row"] in vistos:
            candidato = 100000 + idx
            while candidato in vistos:
                candidato += 1
            row["source_row"] = candidato
        vistos.add(row["source_row"])
    return projeto, itens


def escrever_staging(staging_root: Path, destino: str, projeto: dict, itens: list[dict]) -> Path:
    """`destino` é o NOME DO DIRETÓRIO (ver contrato acima), não necessariamente o slug."""
    d = Path(staging_root) / destino
    d.mkdir(parents=True, exist_ok=True)
    (d / "projeto.json").write_text(json.dumps(projeto, ensure_ascii=False, indent=2, default=_json_default), encoding="utf-8")
    with (d / "itens.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for it in itens:
            f.write(json.dumps(it, ensure_ascii=False, sort_keys=True, default=_json_default) + "\n")
    return d


def hash_do_plano(slugs_por_fonte: dict[str, list[str]], registros: list[dict]) -> str:
    """Impressão digital do que ESTE `--apply` enviaria (F1): os diretórios por
    rótulo de leva e, por lote, o snapshot de origem e a data-base final.

    Só o `source_snapshot_id` não basta: resolver o De-Para em
    `memorial_slug_overrides.json` libera lotes novos sem que nada tenha mudado no
    Memorial — o snapshot é o mesmo e o plano não."""
    payload = {
        "fontes": {fonte: sorted(dirs) for fonte, dirs in sorted(slugs_por_fonte.items())},
        "lotes": sorted(
            [
                {
                    "slug": str(r.get("slug")),
                    "source_snapshot_id": str(r.get("snapshot_id")),
                    "data_base": str(r.get("data_base")),
                }
                for r in registros
            ],
            key=lambda r: (r["slug"], r["source_snapshot_id"], r["data_base"]),
        ),
    }
    canon = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canon).hexdigest()


def ler_ultimo_apply(staging_root: Path) -> dict:
    """Registro do último `coletar --apply` bem-sucedido (I8/F1): snapshot + plano."""
    p = Path(staging_root) / "_memorial" / "ultimo_apply.json"
    if not p.exists():
        return {}
    try:
        payload = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return payload if isinstance(payload, dict) else {}


def registrar_ultimo_apply(staging_root: Path, sid: str, plan_hash: str) -> Path:
    d = Path(staging_root) / "_memorial"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "ultimo_apply.json"
    p.write_text(
        json.dumps({"source_snapshot_id": sid, "plan_hash": plan_hash,
                    "applied_at": datetime.now(timezone.utc).isoformat()},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return p


def escrever_obras_memorial(staging_root: Path, registros: list[dict]) -> Path:
    d = Path(staging_root) / "_memorial"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "memorial_obras.json"
    p.write_text(json.dumps(sorted(registros, key=lambda r: (r["slug"], r["fonte_leva"])), ensure_ascii=False, indent=2, default=_json_default), encoding="utf-8")
    return p


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for nome in ("listar", "coletar"):
        s = sub.add_parser(nome)
        s.add_argument("--desde", default=None, help="YYYY-MM-DD: só lotes/versões a partir desta data")
        s.add_argument("--quarentena", default=str(CUB_OVERRIDES_DIR / "memorial_quarentena.json"))
        s.add_argument("--overrides", default=str(CUB_OVERRIDES_DIR / "memorial_slug_overrides.json"))
        s.add_argument("--slugs-existentes", default=None,
                       help="JSON {slug: {ac_m2}} dos slugs já no CUB (gerado por `cub` ou exportado do banco); sem ele, candidatos ficam vazios")
        s.add_argument("--env-file", default=str(ENV_FILE))
        s.add_argument("--projeto", default=None, help="UUID de um projeto do Memorial: coleta só ele")
        if nome == "coletar":
            g = s.add_mutually_exclusive_group()
            g.add_argument("--dry-run", action="store_true", default=True)
            g.add_argument("--apply", action="store_true")
            s.add_argument("--strict", action="store_true", help="com --apply: recusa (exit 3) se houver pendência ou quarentena")
    return p


def run(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        url, key = carregar_env(Path(args.env_file))
    except RuntimeError as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2
    regras = carregar_regras_quarentena(Path(args.quarentena))
    overrides = carregar_slug_overrides(Path(args.overrides))
    slugs_existentes = json.loads(Path(args.slugs_existentes).read_text(encoding="utf-8")) if args.slugs_existentes else {}

    client = MemorialClient(url, key)
    extratos = extrair(client, args.desde)
    if getattr(args, "projeto", None):
        extratos = filtrar_por_projeto(extratos, args.projeto)
    hoje = datetime.now(timezone.utc).date()
    sid, manifest_path = gravar_snapshot(
        SNAPSHOT_ROOT, extratos,
        {"cutoff_at": hoje.isoformat(), "desde": args.desde, "projeto": getattr(args, "projeto", None)},
    )
    lotes = montar_lotes(extratos, hoje)

    prontos: list[tuple[Lote, str]] = []
    pendentes: list[dict] = []
    quarentena: list[tuple[Lote, str]] = []
    for lote in lotes:
        motivo = lote.quarentena or motivo_quarentena(lote, regras)
        if motivo:
            lote.quarentena = motivo
            quarentena.append((lote, motivo))
            continue
        slug, pend = resolver_identidade(lote, overrides)
        if pend:
            pendentes.append({
                "memorial_project_id": lote.project_id, "memorial_client_id": lote.client_id, "projeto": lote.projeto_nome,
                "cliente": lote.cliente_nome, "fonte_leva": lote.fonte, "lote_id": lote.lote_id, "pendencia": pend,
                "data_base_sugerida": lote.data_base, "data_base_origem": lote.data_base_origem,
                "candidatos": propor_candidatos(lote, slugs_existentes), "slug_se_novo": slug_memorial(lote.cliente_nome or "sem-cliente", lote.projeto_nome),
            })
            continue
        # I3: se a obra já existe no CUB, a AC registrada entra como candidata (`cub_atual`).
        ac_atual = (slugs_existentes.get(slug) or {}).get("ac_m2") if isinstance(slugs_existentes, dict) else None
        if ac_atual not in (None, ""):
            valor = to_decimal(ac_atual)
            if valor:
                lote.ac = _ac_do_projeto(lote.project_id, extratos, ac_cub_atual=valor)
        prontos.append((lote, slug))

    # C1: um lote por (slug, fonte, vintage) — senão dois lotes escrevem o mesmo staging.
    prontos = reduzir_lotes(prontos)

    print(f"> snapshot {sid[:12]}… manifesto {manifest_path.name}")
    print(f"> lotes: {len(lotes)} · prontos {len(prontos)} · pendentes {len(pendentes)} · quarentena {len(quarentena)}")
    for lote, motivo in quarentena:
        print(f"  [quarentena] {lote.fonte} {lote.lote_id} {lote.cliente_nome!r}/{lote.projeto_nome!r}: {motivo}")
    for p in pendentes:
        print(f"  [pendente]   {p['fonte_leva']} {p['lote_id']} {p['cliente']!r}/{p['projeto']!r}: {p['pendencia']} · candidatos {[c['slug'] for c in p['candidatos']]}")
    for lote, slug in prontos:
        print(f"  [pronto]     {lote.fonte} {lote.lote_id} -> {slug} · {len(lote.itens)} folhas · data-base {lote.data_base} ({lote.data_base_confianca})")

    if args.cmd == "listar":
        return 0

    if pendentes:
        escrever_pendentes(STAGING_ROOT, pendentes)
    registros: list[dict] = []
    slugs_por_fonte: dict[str, list[str]] = {}
    for lote, slug in prontos:
        projeto, itens = montar_staging(lote, slug, sid)
        rotulo = projeto["memorial"]["fonte_leva"]          # com o trimestre (C1)
        destino = diretorio_staging(slug, rotulo)           # F2: uma pasta por (obra, fonte, safra)
        escrever_staging(STAGING_ROOT, destino, projeto, itens)
        slugs_por_fonte.setdefault(rotulo, []).append(destino)
        registros.append({
            "slug": slug, "fonte_leva": rotulo, "vintage": projeto["memorial"]["vintage"],
            "staging_dir": destino,
            "projeto": lote.projeto_nome, "cliente": lote.cliente_nome, "cidade": lote.cidade,
            "data_base": lote.data_base, "data_base_confianca": lote.data_base_confianca, "total": projeto["total"], "n_folhas": len(itens),
            "ac_candidatas": lote.ac or {}, "reconciliacao_pct": projeto["memorial"]["reconciliacao_pct"],
            "reconciliacao_ok": projeto["memorial"]["reconciliacao_ok"], "snapshot_id": sid,
        })
    # sempre reescreve (mesmo com [] quando zero prontos): senão memorial_obras.json fica
    # stale e a aba "Novas do Memorial" (Task 8) lê estado de um `coletar` anterior.
    escrever_obras_memorial(STAGING_ROOT, registros)

    if not args.apply:
        print("> dry-run: staging escrito; nada enviado ao Supabase do CUB.")
        return 0
    if args.strict and (pendentes or quarentena):
        print("RECUSADO (--strict): há pendências/quarentena; resolva antes de --apply.", file=sys.stderr)
        return 3

    # I8/F1: mesmo snapshot E mesmo plano já aplicados -> no-op (o equivalente local
    # do `skipped_same_snapshot`; não escreve em ingest_runs, que é do loader).
    plano = hash_do_plano(slugs_por_fonte, registros)
    anterior = ler_ultimo_apply(STAGING_ROOT)
    if anterior.get("source_snapshot_id") == sid and anterior.get("plan_hash") == plano:
        print(f"> snapshot idêntico ao último aplicado ({sid[:12]}) — nada a enviar")
        return 0

    import subprocess
    rc_total = 0
    for fonte, destinos in sorted(slugs_por_fonte.items()):
        cmd = [sys.executable, str(Path(__file__).with_name("carregar_fato_supabase.py")),
               "--fonte-leva", fonte, *sorted(destinos)]
        rc = subprocess.call(cmd)
        rc_total = max(rc_total, rc)
    if rc_total == 0:
        registrar_ultimo_apply(STAGING_ROOT, sid, plano)
    return 1 if rc_total else 0


if __name__ == "__main__":
    sys.exit(run())
