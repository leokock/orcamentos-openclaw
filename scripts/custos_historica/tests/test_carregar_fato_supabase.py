import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("carregar_fato_supabase", HERE / "carregar_fato_supabase.py")
loader = importlib.util.module_from_spec(spec)
sys.modules["carregar_fato_supabase"] = loader
spec.loader.exec_module(loader)


def test_build_fato_projeto_propagates_fonte_leva():
    row = loader.build_fato_projeto(
        {"slug": "obra-x", "ac": "1000", "total": "5000000", "data_base": "2026-08-15"},
        run_id=None,
        fonte_leva="memorial-referencia-cliente",
    )
    assert row["fonte_leva"] == "memorial-referencia-cliente"
    assert row["vintage"] == "2026Q3"


def test_build_fato_item_propagates_fonte_leva():
    row = loader.build_fato_item(
        {"slug": "obra-x", "source_sha1": "abc", "source_sheet": "v1", "source_row": 3,
         "descricao": "Concreto", "total": "10", "data_base": "2026-08-15"},
        {"slug": "obra-x", "data_base": "2026-08-15"},
        run_id=None,
        fonte_leva="memorial-versao-cartesian",
    )
    assert row["fonte_leva"] == "memorial-versao-cartesian"


def test_default_fonte_leva_is_drive():
    assert loader.FONTE_LEVA_DEFAULT == "drive-53-pastas-2026-06"
    row = loader.build_fato_projeto({"slug": "a", "data_base": "2026-01-01"}, None, loader.FONTE_LEVA_DEFAULT)
    assert row["fonte_leva"] == "drive-53-pastas-2026-06"


# --------------------------------------------------- C1.3: REPLACE das levas Memorial

import json


class FakeExec:
    def __init__(self, data=None, count=None):
        self.data = data if data is not None else []
        self.count = count


class FakeTable:
    def __init__(self, nome, log, select_data=None, count=0):
        self.nome = nome
        self.log = log
        self.select_data = select_data if select_data is not None else []
        self.count = count
        self._op = None
        self._eqs = []

    def delete(self):
        self._op = "delete"
        return self

    def select(self, *_a, **_kw):
        self._op = "select"
        return self

    def upsert(self, rows, **_kw):
        self._op = "upsert"
        self.log.append(("upsert", self.nome, len(rows)))
        return self

    def insert(self, rows, **_kw):
        self._op = "insert"
        self.log.append(("insert", self.nome, len(rows)))
        return self

    def eq(self, col, val):
        self._eqs.append((col, val))
        return self

    def limit(self, _n):
        return self

    def execute(self):
        if self._op == "delete":
            self.log.append(("delete", self.nome, tuple(self._eqs)))
            return FakeExec([])
        if self._op == "select":
            self.log.append(("select", self.nome, tuple(self._eqs)))
            return FakeExec(self.select_data, count=self.count)
        return FakeExec([])


class FakeClient:
    def __init__(self, count=0):
        self.log = []
        self.count = count

    def table(self, nome):
        return FakeTable(nome, self.log, count=self.count)


def _staging(tmp_path, slug):
    d = tmp_path / slug
    d.mkdir(parents=True)
    (d / "projeto.json").write_text(
        json.dumps({"slug": slug, "ac": None, "total": "100", "data_base": "2026-09-10", "fonte": "memorial:x:B1"}),
        encoding="utf-8",
    )
    (d / "itens.jsonl").write_text(
        json.dumps({"slug": slug, "source_sha1": "ab", "source_sheet": "B1", "source_row": 1,
                    "descricao": "Concreto", "total": "100", "data_base": "2026-09-10"}) + "\n",
        encoding="utf-8",
    )
    return d


def test_memorial_apaga_itens_da_mesma_leva_antes_do_upsert(tmp_path, monkeypatch):
    """C1.3 — recarregar a MESMA safra do Memorial substitui os itens (REPLACE), nao acumula."""
    slug = "memorial-soles-florenca"
    _staging(tmp_path, slug)
    monkeypatch.setattr(loader, "STAGING_ROOT", tmp_path)
    client = FakeClient()
    fonte = "memorial-referencia-cliente@2026Q3"
    loader.carregar_slug(client, slug, run_id=None, dry_run=False, fonte_leva=fonte)

    deletes = [c for c in client.log if c[0] == "delete"]
    assert ("delete", "fato_itens", (("slug", slug), ("fonte_leva", fonte))) in deletes
    assert ("delete", "fato_composicao_insumos", (("slug", slug), ("fonte_leva", fonte))) in deletes
    # o delete de itens vem ANTES do upsert de fato_itens
    ordem = [c for c in client.log if c[0] in ("delete", "upsert")]
    i_del = next(i for i, c in enumerate(ordem) if c[0] == "delete" and c[1] == "fato_itens")
    i_up = next(i for i, c in enumerate(ordem) if c[0] == "upsert" and c[1] == "fato_itens")
    assert i_del < i_up


def test_drive_nao_apaga_nada(tmp_path, monkeypatch):
    """C1.3 — comportamento do Drive inalterado: nenhum delete."""
    slug = "obra-drive"
    _staging(tmp_path, slug)
    monkeypatch.setattr(loader, "STAGING_ROOT", tmp_path)
    client = FakeClient()
    loader.carregar_slug(client, slug, run_id=None, dry_run=False, fonte_leva=loader.FONTE_LEVA_DEFAULT)
    assert [c for c in client.log if c[0] == "delete"] == []


def test_dry_run_memorial_so_anuncia_quantas_apagaria(tmp_path, monkeypatch, capsys):
    """C1.3 — dry-run nunca apaga; so conta."""
    slug = "memorial-soles-florenca"
    _staging(tmp_path, slug)
    monkeypatch.setattr(loader, "STAGING_ROOT", tmp_path)
    client = FakeClient(count=42)
    fonte = "memorial-referencia-cliente@2026Q3"
    loader.carregar_slug(client, slug, run_id=None, dry_run=True, fonte_leva=fonte)
    out = capsys.readouterr().out
    assert f"[dry-run] fato_itens: apagaria 42 linhas de ({slug}, {fonte}) antes do upsert" in out
    assert [c for c in client.log if c[0] == "delete"] == []

    loader.carregar_slug(None, slug, run_id=None, dry_run=True, fonte_leva=fonte)
    assert "apagaria N=? (sem cliente) linhas" in capsys.readouterr().out


def test_diretorio_de_staging_pode_diferir_do_slug(tmp_path, monkeypatch):
    """F2: no Memorial o diretorio e `<slug>@<fonte_leva>`; TODA operacao de banco
    por slug usa o slug do projeto.json, nao o nome do diretorio."""
    diretorio = "obra-x@memorial-versao-cartesian@2026Q3"
    d = tmp_path / diretorio
    d.mkdir(parents=True)
    (d / "projeto.json").write_text(
        json.dumps({"slug": "obra-x", "ac": None, "total": "100", "data_base": "2026-09-10",
                    "fonte": "memorial:memorial-versao-cartesian:V1"}),
        encoding="utf-8",
    )
    (d / "itens.jsonl").write_text(
        json.dumps({"slug": "obra-x", "source_sha1": "ab", "source_sheet": "V1", "source_row": 1,
                    "descricao": "Concreto", "total": "100", "data_base": "2026-09-10"}) + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(loader, "STAGING_ROOT", tmp_path)
    client = FakeClient()
    fonte = "memorial-versao-cartesian@2026Q3"
    stats = loader.carregar_slug(client, diretorio, run_id=None, dry_run=False, fonte_leva=fonte)

    deletes = [c for c in client.log if c[0] == "delete"]
    assert ("delete", "fato_itens", (("slug", "obra-x"), ("fonte_leva", fonte))) in deletes
    assert ("delete", "fato_composicao_insumos", (("slug", "obra-x"), ("fonte_leva", fonte))) in deletes
    assert all(diretorio not in str(c) for c in deletes)         # o nome do diretorio nunca vai pro banco
    assert stats["slug"] == "obra-x" and stats["staging_dir"] == diretorio
