import importlib.util
import json
import sys
from datetime import date
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("fonte_memorial", HERE / "fonte_memorial.py")
fm = importlib.util.module_from_spec(spec)
sys.modules["fonte_memorial"] = fm
spec.loader.exec_module(fm)

REGRAS = {
    "clientes": ["Cartesian - Apresentações Comerciais", "Cartesian Engenharia (MODELO)", "Cliente Exemplo", "Construtora Teste"],
    "regex_nome": "teste|template|exemplo|apresenta",
}


def lote(**kw):
    base = dict(
        fonte=fm.FONTE_CLIENTE, lote_id="L1", project_id="P1", client_id="C1",
        projeto_nome="Florença", cliente_nome="Soles Empreendimentos", cidade="Balneário Piçarras",
        is_reference_template=False, itens=[], data_base=None, data_base_origem=None,
        data_base_confianca=None, total_declarado=None, revisao=None, ac=None, quarentena=None,
    )
    base.update(kw)
    return fm.Lote(**base)


def test_quarentena_por_cliente_nome_e_template():
    assert fm.motivo_quarentena(lote(cliente_nome="Cliente Exemplo"), REGRAS) == "cliente_em_quarentena"
    assert fm.motivo_quarentena(lote(projeto_nome="Teste Estoril"), REGRAS) == "nome_casa_regex"
    assert fm.motivo_quarentena(lote(projeto_nome="[APRESENTAÇÃO COMERCIAL]"), REGRAS) == "nome_casa_regex"
    assert fm.motivo_quarentena(lote(is_reference_template=True), REGRAS) == "is_reference_template"
    assert fm.motivo_quarentena(lote(), REGRAS) is None


def test_slug_memorial_deterministico_sem_acento():
    assert fm.slug_memorial("Soles Empreendimentos", "Florença") == "memorial-soles-empreendimentos-florenca"
    assert fm.slug_memorial("D'Lohn Empreendimentos", "Estreito") == "memorial-d-lohn-empreendimentos-estreito"


def test_escolher_data_base_prefere_effective_valida():
    hoje = date(2026, 9, 18)
    assert fm.escolher_data_base([("2026-01-26", "budgets.effective_date")], ("2026-05-05", "budget_versions.created_at"), hoje) == (
        "2026-01-26", "budgets.effective_date", "alta")
    # 1969 é inválida -> cai no fallback com confiança baixa
    assert fm.escolher_data_base([("1969-12-31", "budgets.effective_date")], ("2026-05-05", "budget_versions.created_at"), hoje) == (
        "2026-05-05", "budget_versions.created_at", "baixa")
    # futuro também é inválido
    assert fm.escolher_data_base([("2030-01-01", "x")], ("2026-05-05", "y"), hoje)[2] == "baixa"


def test_folhas_nivel_max_e_is_leaf():
    itens = [
        {"item_id": "a", "parent_id": None, "level": 1, "seq": 1, "codigo": "01", "descricao": "01. SUPRAESTRUTURA", "unidade": None, "qtd": None, "pu": None, "total": Decimal("100"), "is_leaf": False},
        {"item_id": "b", "parent_id": "a", "level": 2, "seq": 1, "codigo": "01.01", "descricao": "Concreto", "unidade": "m3", "qtd": Decimal("10"), "pu": Decimal("5"), "total": Decimal("50"), "is_leaf": True},
        {"item_id": "c", "parent_id": "a", "level": 2, "seq": 2, "codigo": "01.02", "descricao": "Aço", "unidade": "kg", "qtd": Decimal("100"), "pu": Decimal("0.5"), "total": Decimal("50"), "is_leaf": True},
    ]
    assert [i["item_id"] for i in fm.folhas(itens, "nivel_max")] == ["b", "c"]
    assert [i["item_id"] for i in fm.folhas(itens, "is_leaf")] == ["b", "c"]


def test_atribuir_macrogrupo_usa_ancestral_nivel1_sem_prefixo_numerico():
    itens = [
        {"item_id": "r", "parent_id": None, "level": 0, "descricao": "ORÇAMENTO", "total": None},
        {"item_id": "a", "parent_id": "r", "level": 1, "descricao": "03. SUPRAESTRUTURA", "total": None},
        {"item_id": "b", "parent_id": "a", "level": 2, "descricao": "Concreto", "total": Decimal("50")},
        {"item_id": "z", "parent_id": None, "level": 2, "descricao": "Órfão", "total": Decimal("1")},
    ]
    out = {i["item_id"]: i for i in fm.atribuir_macrogrupo(itens)}
    assert out["b"]["macrogrupo"] == "SUPRAESTRUTURA"
    assert out["b"]["aba"] == "ORÇAMENTO"
    assert out["z"]["macrogrupo"] is None


def test_reconciliar_tolerancia_2pct():
    pct, ok = fm.reconciliar(Decimal("1000"), Decimal("1015"))
    assert ok is True and abs(float(pct)) < 2.0
    pct, ok = fm.reconciliar(Decimal("1000"), Decimal("1100"))
    assert ok is False
    assert fm.reconciliar(Decimal("1000"), None) == (None, False)


def test_normalizar_itens_cliente_mapeia_colunas():
    rows = [{"id": "i1", "parent_id": None, "level": 1, "sort_order": 3, "line_code": "01", "description": "01. INFRA",
             "unit": None, "quantity": None, "client_unit_cost": None, "client_total_price": "1234.50"}]
    it = fm.normalizar_itens_cliente(rows)[0]
    assert it == {"item_id": "i1", "parent_id": None, "level": 1, "seq": 3, "codigo": "01", "descricao": "01. INFRA",
                  "unidade": None, "qtd": None, "pu": None, "total": Decimal("1234.50"), "is_leaf": False}


def test_normalizar_itens_snapshot_mapeia_colunas():
    items = [{"item_id": "s1", "parent_id": "p", "level": 3, "sequence": 7, "code": "01.02.03", "description": "Concreto",
              "unit": "m3", "quantity": 10, "unit_price": 500.5, "total_price": 5005, "is_leaf": True}]
    it = fm.normalizar_itens_snapshot(items)[0]
    assert it["total"] == Decimal("5005") and it["is_leaf"] is True and it["seq"] == 7 and it["codigo"] == "01.02.03"


def test_ac_candidatas_concordancia():
    c = fm.ac_candidatas(Decimal("13916"), 22, 1, Decimal("14000"), None)
    assert c["pavimentos"]["valor"] == "13916" and c["pavimentos"]["n_pavimentos"] == 22
    assert c["empreendimento"]["valor"] == "14000"
    assert c["concordam"] is True
    c2 = fm.ac_candidatas(Decimal("8840"), 10, 1, Decimal("16750"), Decimal("16750"))
    assert c2["concordam"] is False and c2["cub_atual"]["valor"] == "16750"


def test_snapshot_id_estavel_e_sensivel_a_conteudo(tmp_path):
    a = {"imports": [{"id": "1", "x": Decimal("1.50")}, {"id": "2", "x": None}], "clients": [{"id": "c", "name": "Á"}]}
    b = {"clients": [{"id": "c", "name": "Á"}], "imports": [{"id": "2", "x": None}, {"id": "1", "x": Decimal("1.5")}]}
    assert fm.snapshot_id(a) == fm.snapshot_id(b)  # ordem de datasets/linhas e Decimal normalizado não mudam o id
    c = {"imports": [{"id": "1", "x": Decimal("1.51")}], "clients": a["clients"]}
    assert fm.snapshot_id(a) != fm.snapshot_id(c)
    sid, manifest = fm.gravar_snapshot(tmp_path, a, {"cutoff_at": "2026-09-18T00:00:00Z", "query_hash": "q"})
    assert (tmp_path / "content" / sid / "imports.jsonl").exists()
    meta = json.loads(manifest.read_text(encoding="utf-8"))
    assert meta["source_snapshot_id"] == sid and meta["contagens"]["imports"] == 2
    # create-once: segunda gravação do mesmo conteúdo não falha nem reescreve
    sid2, _ = fm.gravar_snapshot(tmp_path, a, {"cutoff_at": "2026-09-19T00:00:00Z", "query_hash": "q"})
    assert sid2 == sid


def test_gravar_snapshot_atomico_nao_deixa_conteudo_parcial_em_interrupcao(tmp_path, monkeypatch):
    import pytest
    from pathlib import Path as _Path

    a = {"imports": [{"id": "1"}], "clients": [{"id": "c"}]}
    sid = fm.snapshot_id(a)
    calls = {"n": 0}
    orig_write_bytes = _Path.write_bytes

    def fake_write_bytes(self, data):
        calls["n"] += 1
        if calls["n"] == 2:
            raise OSError("interrupcao simulada")
        return orig_write_bytes(self, data)

    with monkeypatch.context() as m:
        m.setattr(_Path, "write_bytes", fake_write_bytes)
        with pytest.raises(OSError):
            fm.gravar_snapshot(tmp_path, a, {"query_hash": "q"})

    # interrompido no meio: nenhum diretorio de conteudo parcial/temporario sobrevive
    assert not (tmp_path / "content" / sid).exists()
    content_root = tmp_path / "content"
    if content_root.exists():
        assert list(content_root.glob(".tmp-*")) == []

    # segunda chamada normal completa e cria tudo
    sid2, _ = fm.gravar_snapshot(tmp_path, a, {"query_hash": "q"})
    assert sid2 == sid
    assert (tmp_path / "content" / sid / "imports.jsonl").exists()
    assert (tmp_path / "content" / sid / "clients.jsonl").exists()


def test_gravar_snapshot_meta_vai_para_params_e_rejeita_chave_reservada(tmp_path):
    import pytest

    a = {"imports": [{"id": "1"}]}
    meta = {"cutoff_at": "2026-09-18T00:00:00Z", "query_hash": "q"}
    sid, manifest = fm.gravar_snapshot(tmp_path, a, meta)
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["params"] == meta
    assert data["source_snapshot_id"] == sid

    with pytest.raises(ValueError):
        fm.gravar_snapshot(tmp_path, a, {"source_snapshot_id": "x"})


def test_carregar_env_erro_claro(tmp_path):
    import pytest
    with pytest.raises(RuntimeError, match=r"\.env\.memorial"):
        fm.carregar_env(tmp_path / ".env.memorial")
    env = tmp_path / ".env.memorial"
    env.write_text("SUPABASE_URL=https://x.supabase.co\nSUPABASE_SECRET_KEY=sb_secret_fake\n", encoding="utf-8")
    assert fm.carregar_env(env) == ("https://x.supabase.co", "sb_secret_fake")


def test_memorial_client_pagina_por_range(monkeypatch):
    chamadas = []

    class FakeResp:
        def __init__(self, data):
            self.data = data

    class FakeQuery:
        def __init__(self, rows):
            self.rows = rows
            self.start = 0
            self.end = 0
        def select(self, *_):
            return self
        def eq(self, *_):
            return self
        def gte(self, *_):
            return self
        def order(self, *_ , **__):
            return self
        def range(self, start, end):
            self.start, self.end = start, end
            chamadas.append((start, end))
            return self
        def execute(self):
            return FakeResp(self.rows[self.start : self.end + 1])

    class FakeSupabase:
        def __init__(self, rows):
            self.rows = rows
        def table(self, _name):
            return FakeQuery(self.rows)

    client = fm.MemorialClient.__new__(fm.MemorialClient)
    client.sb = FakeSupabase([{"id": str(i)} for i in range(2500)])
    client.page_size = 1000
    rows = client.fetch("imports", "id")
    assert len(rows) == 2500 and chamadas == [(0, 999), (1000, 1999), (2000, 2999)]


def _extratos_basicos():
    return {
        "imports": [
            {"id": "i1", "budget_id": None, "budget_version_id": None, "project_id": "P1", "client_id": "C1", "import_batch_id": "B1",
             "import_flow_type": "referencia_cliente_completa", "status": "completed", "is_active": True, "imported_at": "2026-09-10T12:00:00+00:00",
             "template_version": "w", "source_file_hash": None},
            {"id": "i2", "budget_id": None, "budget_version_id": None, "project_id": "P1", "client_id": "C1", "import_batch_id": "B1",
             "import_flow_type": "referencia_cliente_completa", "status": "completed", "is_active": True, "imported_at": "2026-09-10T12:01:00+00:00",
             "template_version": "w", "source_file_hash": None},
        ],
        "import_items": [
            {"id": "a", "import_id": "i1", "parent_id": None, "level": 1, "sort_order": 1, "line_code": "01", "description": "01. SUPRAESTRUTURA", "unit": None, "quantity": None, "client_unit_cost": None, "client_total_price": "100"},
            {"id": "b", "import_id": "i1", "parent_id": "a", "level": 2, "sort_order": 1, "line_code": "01.01", "description": "Concreto", "unit": "m3", "quantity": "10", "client_unit_cost": "6", "client_total_price": "60"},
            {"id": "c", "import_id": "i2", "parent_id": None, "level": 1, "sort_order": 1, "line_code": "02", "description": "02. ESQUADRIAS", "unit": None, "quantity": None, "client_unit_cost": None, "client_total_price": "40"},
            {"id": "d", "import_id": "i2", "parent_id": "c", "level": 2, "sort_order": 1, "line_code": "02.01", "description": "Janela", "unit": "un", "quantity": "4", "client_unit_cost": "10", "client_total_price": "40"},
        ],
        "versions": [
            {"version_id": "V1", "budget_id": "BG1", "version_number": 3, "created_at": "2026-05-18T10:00:00+00:00",
             "snapshot": {"budget": {"effective_date": None, "client_name": "D'Lohn Empreendimentos", "city": None},
                          "items": [{"item_id": f"s{i}", "parent_id": "s0" if i else None, "level": 2 if i else 1, "sequence": i,
                                     "code": f"01.{i:02d}", "description": "01. SUPRAESTRUTURA" if i == 0 else f"Item {i}", "unit": "un",
                                     "quantity": 1, "unit_price": 10, "total_price": 10, "is_leaf": i > 0} for i in range(0, 61)]}},
        ],
        "budgets": [{"budget_id": "BG1", "project_id": "P2", "client_id": "C2", "name": "Estreito", "project_name": "Estreito", "client_name": "D'Lohn Empreendimentos",
                     "city": "Curitiba", "state": "PR", "effective_date": None, "total_value": "600", "version_number": 3, "is_reference_template": False, "budget_type": "executivo"}],
        "projects": [{"id": "P1", "project_name": "Florença", "client_id": "C1", "city": "Balneário Piçarras", "state": "SC", "status": "new"},
                     {"id": "P2", "project_name": "Estreito", "client_id": "C2", "city": "Curitiba", "state": "PR", "status": "new"}],
        "clients": [{"id": "C1", "name": "Soles Empreendimentos", "city": "Balneário Piçarras", "state": "SC"},
                    {"id": "C2", "name": "D'Lohn Empreendimentos", "city": "Curitiba", "state": "PR"}],
        "project_towers": [{"tower_id": "T1", "project_id": "P2", "tower_name": "Torre A"}],
        "tower_floors": [{"floor_id": f"F{i}", "tower_id": "T1", "floor_name": f"P{i}", "floor_area": "632.5"} for i in range(22)],
        "project_building_data": [{"id": "D1", "project_id": "P1", "enterprise_area": "13781.98"}],
    }


def test_montar_lotes_agrupa_batch_e_versao():
    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    por_fonte = {l.fonte: l for l in lotes}
    a = por_fonte[fm.FONTE_CLIENTE]
    assert a.lote_id == "B1" and a.projeto_nome == "Florença" and a.cliente_nome == "Soles Empreendimentos"
    assert sorted(i["descricao"] for i in a.itens) == ["Concreto", "Janela"]          # só folhas (nível máx = 2)
    assert {i["macrogrupo"] for i in a.itens} == {"SUPRAESTRUTURA", "ESQUADRIAS"}
    assert a.total_declarado == Decimal("140")                                          # soma do nível 1
    assert (a.data_base, a.data_base_confianca) == ("2026-09-10", "baixa")
    assert a.ac["empreendimento"]["valor"] == "13781.98"
    b = por_fonte[fm.FONTE_CARTESIAN]
    assert b.lote_id == "V1" and len(b.itens) == 60 and b.revisao == "3"
    assert (b.data_base, b.data_base_origem, b.data_base_confianca) == ("2026-05-18", "budget_versions.created_at", "baixa")
    assert b.ac["pavimentos"]["valor"] == "13915" and b.ac["pavimentos"]["n_pavimentos"] == 22
    assert {i["macrogrupo"] for i in b.itens} == {"SUPRAESTRUTURA"}


def test_montar_lotes_quarentena_poucas_folhas():
    ex = _extratos_basicos()
    ex["versions"][0]["snapshot"]["items"] = ex["versions"][0]["snapshot"]["items"][:10]
    lotes = fm.montar_lotes(ex, hoje=date(2026, 9, 18))
    b = [l for l in lotes if l.fonte == fm.FONTE_CARTESIAN][0]
    assert b.quarentena == "poucas_folhas"


def test_montar_lotes_sem_project_id_vai_para_quarentena():
    ex = _extratos_basicos()
    ex["budgets"][0]["project_id"] = None
    lotes = fm.montar_lotes(ex, hoje=date(2026, 9, 18))
    b = [l for l in lotes if l.fonte == fm.FONTE_CARTESIAN][0]
    assert b.quarentena == "sem_project_id" and b.project_id == ""


def test_propor_candidatos_e_resolver_identidade(tmp_path):
    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    b = [l for l in lotes if l.fonte == fm.FONTE_CARTESIAN][0]
    existentes = {"d-lohn-empreendimentos": {"ac_m2": "13855"}, "alfa-incorporadora": {"ac_m2": "8846"}}
    cands = fm.propor_candidatos(b, existentes)
    assert cands[0]["slug"] == "d-lohn-empreendimentos" and cands[0]["score"] > 0.5
    # sem decisão -> pendente
    assert fm.resolver_identidade(b, {}) == (None, "sem_decisao_de_slug")
    # decisão de slug mas data-base baixa sem confirmação -> pendente
    ov = {"P2": {"slug_cub": "d-lohn-empreendimentos"}}
    assert fm.resolver_identidade(b, ov) == (None, "data_base_nao_confirmada")
    ov = {"P2": {"slug_cub": "d-lohn-empreendimentos", "data_base_confirmada": "2026-04-01"}}
    assert fm.resolver_identidade(b, ov) == ("d-lohn-empreendimentos", None)
    assert b.data_base == "2026-04-01" and b.data_base_confianca == "confirmada"
    ov = {"P2": {"slug_cub": "NOVO", "data_base_confirmada": "2026-04-01"}}
    assert fm.resolver_identidade(b, ov)[0] == "memorial-d-lohn-empreendimentos-estreito"
    p = fm.escrever_pendentes(tmp_path, [{"memorial_project_id": "P2", "candidatos": cands}])
    assert p.parent.name == "_pendentes" and json.loads(p.read_text(encoding="utf-8"))[0]["memorial_project_id"] == "P2"


def test_similaridade_identica_ao_cub():
    """I6 — a paridade com o CUB nao pode se autodesligar quando a branch for mergeada:
    procura o worktree e, depois, o checkout principal; se nenhum existir, FALHA."""

    candidatos = [
        Path(r"C:\Apps\cub-cartesian\.claude\worktrees\base-viva-memorial\src\cub\validacao\join_realizado.py"),
        Path(r"C:\Apps\cub-cartesian\src\cub\validacao\join_realizado.py"),
    ]
    join_path = next((p for p in candidatos if p.exists()), None)
    assert join_path is not None, f"join_realizado.py do CUB nao encontrado em nenhum de: {candidatos}"
    cub_src = join_path.parent.parent.parent

    inserted = str(cub_src) not in sys.path
    if inserted:
        sys.path.insert(0, str(cub_src))
    try:
        spec2 = importlib.util.spec_from_file_location("join_realizado_cub", join_path)
        cub_jr = importlib.util.module_from_spec(spec2)
        sys.modules["join_realizado_cub"] = cub_jr
        spec2.loader.exec_module(cub_jr)

        assert fm.NOISE_TOKENS == set(cub_jr.NOISE_TOKENS)
        assert fm._DATE_TOKEN_RE.pattern == cub_jr._DATE_TOKEN_RE.pattern

        for nome in ["D'Lohn Empreendimentos", "Alfa Incorporadora S.A.", "Residencial das Torres 2024"]:
            assert fm.normalize_empreendimento(nome) == cub_jr.normalize_empreendimento(nome)
        for slug in ["d-lohn-empreendimentos", "alfa-incorporadora", "obra-2021-jardins"]:
            assert fm.extract_empreendimento_from_slug(slug) == cub_jr.extract_empreendimento_from_slug(slug)
        for a, b_ in [("d lohn", "d lohn"), ("estreito", "lohn"), ("residencial jardins", "jardins residence")]:
            assert fm.trigram_similarity(a, b_) == cub_jr.trigram_similarity(a, b_)
    finally:
        sys.modules.pop("join_realizado_cub", None)
        if inserted:
            try:
                sys.path.remove(str(cub_src))
            except ValueError:
                pass


def test_montar_staging_no_contrato_do_loader(tmp_path):
    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    projeto, itens = fm.montar_staging(a, "memorial-soles-empreendimentos-florenca", "deadbeef" * 8)
    assert projeto["slug"] == "memorial-soles-empreendimentos-florenca"
    assert projeto["ac"] is None                                   # AC só depois da confirmação
    assert projeto["total"] == "100.00" or projeto["total"] == "100"  # soma das folhas (60 + 40)
    assert projeto["data_base"] == "2026-09-10"
    assert projeto["memorial"]["fonte_leva"] == f"{fm.FONTE_CLIENTE}@2026Q3"   # C1: rótulo com trimestre
    assert projeto["memorial"]["fonte_base"] == fm.FONTE_CLIENTE
    assert projeto["memorial"]["reconciliacao_ok"] is False        # folhas 100 vs nível 1 = 140 -> fora de 2 %
    it = itens[0]
    assert set(it) >= {"slug", "source_sha1", "source_sheet", "source_row", "codigo", "descricao", "unidade", "qtd", "pu", "total",
                       "aba", "macrogrupo", "data_base", "data_base_origem", "data_base_confianca", "revisao"}
    assert it["source_sha1"] == "deadbeef" * 8 and it["source_sheet"] == "B1"


def test_contrato_com_loader_dry_run(tmp_path, capsys):
    """A saída do adaptador passa no carregar_fato_supabase.py --dry-run sem tocar rede."""
    import importlib.util as ilu
    spec2 = ilu.spec_from_file_location("carregar_fato_supabase", HERE / "carregar_fato_supabase.py")
    loader = ilu.module_from_spec(spec2)
    spec2.loader.exec_module(loader)

    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    slug = "memorial-soles-empreendimentos-florenca"
    projeto, itens = fm.montar_staging(a, slug, "ab" * 32)
    fm.escrever_staging(tmp_path, slug, projeto, itens)

    loader.STAGING_ROOT = tmp_path
    stats = loader.carregar_slug(client=None, slug=slug, run_id=None, dry_run=True, fonte_leva=fm.FONTE_CLIENTE)
    assert stats["itens_lidos"] == 2
    out = capsys.readouterr().out
    assert "fato_projetos upsert" in out and fm.FONTE_CLIENTE in out


def test_run_listar_e_coletar_dry_run(tmp_path, monkeypatch):
    ex = _extratos_basicos()
    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P1", "slug_cub": "NOVO", "data_base_confirmada": "2026-09-01"}]}), encoding="utf-8")
    slugs_existentes = tmp_path / "slugs.json"
    slugs_existentes.write_text(json.dumps({"d-lohn-empreendimentos": {"ac_m2": "13855"}}), encoding="utf-8")

    rc = fm.run(["listar", "--quarentena", str(regras), "--overrides", str(ov), "--slugs-existentes", str(slugs_existentes)])
    assert rc == 0
    rc = fm.run(["coletar", "--dry-run", "--quarentena", str(regras), "--overrides", str(ov), "--slugs-existentes", str(slugs_existentes)])
    assert rc == 0
    # F2: o diretorio de staging e <slug>@<fonte_leva com trimestre>, nao so <slug>
    assert (tmp_path / "staging" / "memorial-soles-empreendimentos-florenca@memorial-referencia-cliente@2026Q3"
            / "projeto.json").exists()   # P1 decidido
    assert not any((tmp_path / "staging").glob("*estreito*"))                                                # P2 pendente
    pend = list((tmp_path / "staging" / "_pendentes").glob("depara_memorial_*.json"))
    assert len(pend) == 1 and json.loads(pend[0].read_text(encoding="utf-8"))[0]["memorial_project_id"] == "P2"
    obras = json.loads((tmp_path / "staging" / "_memorial" / "memorial_obras.json").read_text(encoding="utf-8"))
    assert obras[0]["slug"] == "memorial-soles-empreendimentos-florenca" and "ac_candidatas" in obras[0]
    # --apply --strict com pendência recusa (3) sem chamar loader
    rc = fm.run(["coletar", "--apply", "--strict", "--quarentena", str(regras), "--overrides", str(ov), "--slugs-existentes", str(slugs_existentes)])
    assert rc == 3


def test_apply_strict_nao_bloqueia_por_quarentena(tmp_path, monkeypatch):
    """Quarentena é informativa (SPEC: 'listado com motivo; nunca carregado; nunca
    apagado') e não pode bloquear --apply --strict — só pendente de identidade/data-base
    bloqueia. Cenário: P1 (fonte cliente) decidido no De-Para -> pronto; P2 (fonte
    Cartesian) cai em quarentena por poucas_folhas (sem decisão nenhuma pendente)."""
    ex = _extratos_basicos()
    ex["versions"][0]["snapshot"]["items"] = ex["versions"][0]["snapshot"]["items"][:10]  # força poucas_folhas em P2
    chamadas = []
    import subprocess

    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    monkeypatch.setattr(subprocess, "call", lambda cmd: chamadas.append(cmd) or 0)
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P1", "slug_cub": "NOVO",
                                        "data_base_confirmada": "2026-09-01"}]}), encoding="utf-8")

    rc = fm.run(["coletar", "--apply", "--strict", "--quarentena", str(regras), "--overrides", str(ov)])
    assert rc == 0
    assert len(chamadas) == 1        # loader chamado uma vez (só a fonte pronta, P1)


def test_coletar_zero_prontos_sobrescreve_memorial_obras_com_lista_vazia(tmp_path, monkeypatch):
    """Fix round 1 (Important): memorial_obras.json não pode ficar stale quando um `coletar`
    não resulta em nenhum lote pronto (override removido / nova regra de quarentena) — a aba
    "Novas do Memorial" (Task 8) lê esse arquivo e não pode enxergar obras de um run anterior."""
    ex = _extratos_basicos()
    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    staging_root = tmp_path / "staging"
    monkeypatch.setattr(fm, "STAGING_ROOT", staging_root)
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": []}), encoding="utf-8")  # sem nenhuma decisão -> zero prontos

    # simula estado "stale" de um coletar anterior bem-sucedido
    memorial_dir = staging_root / "_memorial"
    memorial_dir.mkdir(parents=True)
    (memorial_dir / "memorial_obras.json").write_text(json.dumps([{"slug": "obra-antiga-stale"}]), encoding="utf-8")

    rc = fm.run(["coletar", "--dry-run", "--quarentena", str(regras), "--overrides", str(ov)])
    assert rc == 0
    obras = json.loads((memorial_dir / "memorial_obras.json").read_text(encoding="utf-8"))
    assert obras == []


def test_montar_staging_source_row_dedup_nao_colide_com_valor_ja_usado():
    """Fix round 1 (Minor): a reatribuição `100000 + idx` precisa checar `vistos` antes de
    gravar, senão pode colidir com um source_row já usado por outro item do mesmo lote."""
    itens = [
        {"seq": 100002, "codigo": "T", "descricao": "terceiro", "unidade": None, "qtd": None, "pu": None,
         "total": Decimal("1"), "aba": None, "macrogrupo": None},
        {"seq": 7, "codigo": "A", "descricao": "dup1", "unidade": None, "qtd": None, "pu": None,
         "total": Decimal("1"), "aba": None, "macrogrupo": None},
        {"seq": 7, "codigo": "B", "descricao": "dup2", "unidade": None, "qtd": None, "pu": None,
         "total": Decimal("1"), "aba": None, "macrogrupo": None},
    ]
    l = lote(itens=itens, total_declarado=Decimal("3"))
    _, rows = fm.montar_staging(l, "slug-x", "sid" * 20)
    source_rows = [r["source_row"] for r in rows]
    assert len(source_rows) == len(set(source_rows))


# ---------------------------------------------------------------- onda de fixes


def test_vintage_de_e_fonte_leva_com_vintage():
    """C1.1 — o rótulo de leva carrega o trimestre (mesma regra do loader)."""
    assert fm.vintage_de("2026-09-10") == "2026Q3"
    assert fm.vintage_de("2026-01-01T12:00:00+00:00") == "2026Q1"
    assert fm.vintage_de("2026-12-31") == "2026Q4"
    assert fm.vintage_de(None) is None
    assert fm.vintage_de("nao-e-data") is None
    assert fm.fonte_leva_com_vintage(fm.FONTE_CARTESIAN, "2026-05-18") == "memorial-versao-cartesian@2026Q2"
    assert fm.fonte_leva_com_vintage(fm.FONTE_CLIENTE, "2026-09-10") == "memorial-referencia-cliente@2026Q3"
    assert fm.fonte_leva_com_vintage(fm.FONTE_CLIENTE, None) == fm.FONTE_CLIENTE


def test_vintage_de_igual_ao_loader():
    """C1.1 — mesma regra do `vintage_from_data_base` do loader, sem drift."""
    import importlib.util as ilu

    spec2 = ilu.spec_from_file_location("carregar_fato_supabase", HERE / "carregar_fato_supabase.py")
    loader = ilu.module_from_spec(spec2)
    spec2.loader.exec_module(loader)
    for iso in ("2026-01-01", "2026-03-31", "2026-04-01", "2026-09-10", "2026-12-31", "2024-10-05"):
        assert fm.vintage_de(iso) == loader.vintage_from_data_base(iso)


def test_montar_staging_grava_fonte_leva_com_trimestre():
    """C1.1 — staging/<slug>/projeto.json leva o rótulo sufixado."""
    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    projeto, _ = fm.montar_staging(a, "memorial-soles-empreendimentos-florenca", "ab" * 32)
    assert projeto["memorial"]["fonte_leva"] == "memorial-referencia-cliente@2026Q3"
    assert projeto["memorial"]["vintage"] == "2026Q3"


def test_reduzir_lotes_mantem_um_por_slug_fonte_vintage():
    """C1.2 — três versões do mesmo orçamento na mesma safra viram um lote (maior version_number)."""
    v1 = lote(fonte=fm.FONTE_CARTESIAN, lote_id="V1", data_base="2026-05-18", revisao="1",
              version_number=1, criado_em="2026-05-18T10:00:00+00:00")
    v2 = lote(fonte=fm.FONTE_CARTESIAN, lote_id="V2", data_base="2026-05-20", revisao="3",
              version_number=3, criado_em="2026-05-20T10:00:00+00:00")
    v3 = lote(fonte=fm.FONTE_CARTESIAN, lote_id="V3", data_base="2026-06-01", revisao="2",
              version_number=2, criado_em="2026-06-01T10:00:00+00:00")
    out = fm.reduzir_lotes([(v1, "obra-x"), (v2, "obra-x"), (v3, "obra-x")])
    assert len(out) == 1 and out[0][0].lote_id == "V2"


def test_reduzir_lotes_nao_mistura_vintages_nem_fontes():
    """C1.2 — safras diferentes (ou fontes diferentes) continuam sendo registros distintos."""
    q2 = lote(fonte=fm.FONTE_CARTESIAN, lote_id="V1", data_base="2026-05-18", version_number=1,
              criado_em="2026-05-18T10:00:00+00:00")
    q3 = lote(fonte=fm.FONTE_CARTESIAN, lote_id="V2", data_base="2026-08-18", version_number=1,
              criado_em="2026-08-18T10:00:00+00:00")
    cli = lote(fonte=fm.FONTE_CLIENTE, lote_id="B1", data_base="2026-05-18", criado_em="2026-05-18T10:00:00+00:00")
    out = fm.reduzir_lotes([(q2, "obra-x"), (q3, "obra-x"), (cli, "obra-x")])
    assert sorted(l.lote_id for l, _ in out) == ["B1", "V1", "V2"]


def test_reduzir_lotes_fonte_cliente_fica_com_o_lote_mais_recente():
    """C1.2 — fonte A: desempate pelo `imported_at` mais recente do lote."""
    antigo = lote(fonte=fm.FONTE_CLIENTE, lote_id="B1", data_base="2026-09-01", criado_em="2026-09-01T08:00:00+00:00")
    novo = lote(fonte=fm.FONTE_CLIENTE, lote_id="B2", data_base="2026-09-10", criado_em="2026-09-10T08:00:00+00:00")
    out = fm.reduzir_lotes([(antigo, "obra-x"), (novo, "obra-x")])
    assert len(out) == 1 and out[0][0].lote_id == "B2"


def test_montar_lotes_guarda_ordenacao_de_lote():
    """C1.2 — montar_lotes precisa alimentar version_number/criado_em pra reducao ser deterministica."""
    lotes = fm.montar_lotes(_extratos_basicos(), hoje=date(2026, 9, 18))
    b = [l for l in lotes if l.fonte == fm.FONTE_CARTESIAN][0]
    assert b.version_number == 3 and str(b.criado_em).startswith("2026-05-18")
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    assert a.version_number is None and str(a.criado_em).startswith("2026-09-10")


def test_normalizar_itens_snapshot_aceita_id_ou_item_id_e_falha_sem_chave():
    """C4 — snapshot.items pode vir com `id` em vez de `item_id`; sem nenhum dos dois, erro claro."""
    import pytest

    com_id = fm.normalizar_itens_snapshot([{"id": "s9", "parent_id": "p1", "level": 2, "total_price": 5}])
    assert com_id[0]["item_id"] == "s9" and com_id[0]["parent_id"] == "p1"
    com_item_id = fm.normalizar_itens_snapshot([{"item_id": "s9", "level": 2, "total_price": 5}])
    assert com_item_id[0]["item_id"] == "s9" and com_item_id[0]["parent_id"] is None
    with pytest.raises(ValueError, match=r"sem chave de id .*V42"):
        fm.normalizar_itens_snapshot([{"level": 2, "total_price": 5}], version_id="V42")


def test_normalizar_itens_cliente_aceita_id_ou_item_id_e_falha_sem_chave():
    """C4 — mesma defesa na fonte A."""
    import pytest

    it = fm.normalizar_itens_cliente([{"item_id": "i9", "level": 1, "client_total_price": "1"}])[0]
    assert it["item_id"] == "i9"
    with pytest.raises(ValueError, match="sem chave de id"):
        fm.normalizar_itens_cliente([{"level": 1, "client_total_price": "1"}])


def test_montar_lotes_fonte_a_sem_project_id_vai_para_quarentena():
    """I1 — fonte A espelha a guarda da fonte B."""
    ex = _extratos_basicos()
    for im in ex["imports"]:
        im["project_id"] = None
    lotes = fm.montar_lotes(ex, hoje=date(2026, 9, 18))
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    assert a.quarentena == "sem_project_id" and a.project_id == ""


def test_extrair_pagina_itens_por_id_e_nao_por_sort_order():
    """I2 — `sort_order` não é único no lote; a paginação tem que ordenar por `id`."""
    chamadas = []

    class FakeClient:
        def fetch(self, table, select, order="id", **filters):
            chamadas.append((table, order, filters))
            if table == "budget_client_reference_imports":
                return [{"id": "i1"}]
            return []

    fm.extrair(FakeClient())
    itens = [c for c in chamadas if c[0] == "budget_client_reference_items"]
    assert itens and all(c[1] == "id" for c in itens)


def test_ac_candidatas_recebe_cub_atual_do_slug_existente(tmp_path, monkeypatch):
    """I3 — obra que já existe no CUB traz `cub_atual` entre as candidatas de AC."""
    ex = _extratos_basicos()
    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P2", "slug_cub": "d-lohn-empreendimentos",
                                        "data_base_confirmada": "2026-04-01"}]}), encoding="utf-8")
    existentes = tmp_path / "slugs.json"
    existentes.write_text(json.dumps({"d-lohn-empreendimentos": {"ac_m2": "13855"}}), encoding="utf-8")

    rc = fm.run(["coletar", "--dry-run", "--quarentena", str(regras), "--overrides", str(ov),
                 "--slugs-existentes", str(existentes)])
    assert rc == 0
    destino = tmp_path / "staging" / "d-lohn-empreendimentos@memorial-versao-cartesian@2026Q2"
    projeto = json.loads((destino / "projeto.json").read_text(encoding="utf-8"))
    cands = projeto["memorial"]["ac_candidatas"]
    assert cands["cub_atual"]["valor"] == "13855"
    assert cands["concordam"] is True          # 13915 x 13855 -> dentro de 5 %


def test_conteudo_por_dataset_calcula_bytes_uma_vez():
    """I5 — canonical_jsonl era chamado 3x por dataset (id, arquivo, content_hashes)."""
    extratos = {"imports": [{"id": "1"}], "clients": [{"id": "c"}]}
    conteudo = fm.conteudo_por_dataset(extratos)
    assert set(conteudo) == {"imports", "clients"}
    for _ds, (blob, sha) in conteudo.items():
        assert isinstance(blob, bytes) and len(sha) == 64


def test_gravar_snapshot_nao_recalcula_canonical_jsonl(tmp_path, monkeypatch):
    """I5 — uma passada de canonical_jsonl por dataset em todo o gravar_snapshot."""
    extratos = {"imports": [{"id": "1"}], "clients": [{"id": "c"}], "budgets": [{"budget_id": "b"}]}
    chamadas = {"n": 0}
    orig = fm.canonical_jsonl

    def contando(rows):
        chamadas["n"] += 1
        return orig(rows)

    monkeypatch.setattr(fm, "canonical_jsonl", contando)
    fm.gravar_snapshot(tmp_path, extratos, {"query_hash": "q"})
    assert chamadas["n"] == len(extratos)


def test_filtrar_por_projeto():
    """I8 — `--projeto <uuid>` corta imports (project_id) e versions (via budgets.project_id)."""
    ex = fm.filtrar_por_projeto(_extratos_basicos(), "P1")
    assert {im["project_id"] for im in ex["imports"]} == {"P1"}
    assert ex["versions"] == []                                   # BG1 é do projeto P2
    assert {it["import_id"] for it in ex["import_items"]} <= {"i1", "i2"}
    ex2 = fm.filtrar_por_projeto(_extratos_basicos(), "P2")
    assert ex2["imports"] == [] and ex2["import_items"] == []
    assert [v["version_id"] for v in ex2["versions"]] == ["V1"]


def _run_apply(tmp_path, monkeypatch, ex, chamadas):
    import subprocess

    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    monkeypatch.setattr(subprocess, "call", lambda cmd: chamadas.append(cmd) or 0)
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P1", "slug_cub": "NOVO",
                                        "data_base_confirmada": "2026-09-01"}]}), encoding="utf-8")
    return fm.run(["coletar", "--apply", "--quarentena", str(regras), "--overrides", str(ov)])


def test_apply_pula_loader_quando_snapshot_identico(tmp_path, monkeypatch, capsys):
    """I8 — segundo `coletar --apply` do mesmo snapshot é no-op (skipped_same_snapshot local)."""
    ex = _extratos_basicos()
    chamadas = []
    assert _run_apply(tmp_path, monkeypatch, ex, chamadas) == 0
    assert len(chamadas) == 1
    assert "--fonte-leva" in chamadas[0]
    fonte_arg = chamadas[0][chamadas[0].index("--fonte-leva") + 1]
    assert fonte_arg == "memorial-referencia-cliente@2026Q3"      # C1.1: rótulo com trimestre
    ultimo = json.loads((tmp_path / "staging" / "_memorial" / "ultimo_apply.json").read_text(encoding="utf-8"))
    assert len(ultimo["source_snapshot_id"]) == 64 and ultimo["applied_at"]
    assert len(ultimo["plan_hash"]) == 64

    capsys.readouterr()
    assert _run_apply(tmp_path, monkeypatch, ex, chamadas) == 0
    assert len(chamadas) == 1                                      # loader NAO foi chamado de novo
    assert "nada a enviar" in capsys.readouterr().out


def test_run_reduz_lotes_duplicados_da_mesma_safra(tmp_path, monkeypatch):
    """C1.2 — duas versões do mesmo orçamento na mesma safra escrevem um staging só."""
    ex = _extratos_basicos()
    v2 = json.loads(json.dumps(ex["versions"][0]))
    v2["version_id"] = "V2"
    v2["version_number"] = 7
    v2["created_at"] = "2026-05-25T10:00:00+00:00"
    ex["versions"].append(v2)
    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P2", "slug_cub": "d-lohn-empreendimentos",
                                        "data_base_confirmada": "2026-04-01"}]}), encoding="utf-8")

    assert fm.run(["coletar", "--dry-run", "--quarentena", str(regras), "--overrides", str(ov)]) == 0
    obras = json.loads((tmp_path / "staging" / "_memorial" / "memorial_obras.json").read_text(encoding="utf-8"))
    assert len(obras) == 1
    assert obras[0]["fonte_leva"] == "memorial-versao-cartesian@2026Q2" and obras[0]["vintage"] == "2026Q2"
    destino = tmp_path / "staging" / "d-lohn-empreendimentos@memorial-versao-cartesian@2026Q2"
    itens = (destino / "itens.jsonl").read_text(encoding="utf-8").splitlines()
    assert all('"source_sheet": "V2"' in l or '"source_sheet":"V2"' in l for l in itens)


# ------------------------------------------------------------------ fix round 2


def _cenario_apply(tmp_path, monkeypatch, ex, chamadas):
    """Ambiente comum dos testes de --apply: sem rede, staging/snapshot no tmp,
    loader substituido por um registrador de chamadas. Devolve o path do arquivo
    de overrides pra cada teste reescrever entre as rodadas."""
    import subprocess

    monkeypatch.setattr(fm, "carregar_env", lambda env_file=None: ("https://x", "k"))
    monkeypatch.setattr(fm, "MemorialClient", lambda url, key: object())
    monkeypatch.setattr(fm, "extrair", lambda client, desde=None: ex)
    monkeypatch.setattr(fm, "STAGING_ROOT", tmp_path / "staging")
    monkeypatch.setattr(fm, "SNAPSHOT_ROOT", tmp_path / "snap")
    monkeypatch.setattr(subprocess, "call", lambda cmd: chamadas.append(cmd) or 0)
    regras = tmp_path / "q.json"
    regras.write_text(json.dumps(REGRAS), encoding="utf-8")
    ov = tmp_path / "ov.json"
    return regras, ov


def test_hash_do_plano_muda_quando_o_plano_muda():
    """F1: o plano é o que vai ser enviado — fontes/diretórios e, por lote,
    snapshot e data-base final."""
    fontes = {"memorial-referencia-cliente@2026Q3": ["obra-a@memorial-referencia-cliente@2026Q3"]}
    registros = [{"slug": "obra-a", "data_base": "2026-09-01", "snapshot_id": "ab" * 32}]
    h1 = fm.hash_do_plano(fontes, registros)
    assert len(h1) == 64
    assert fm.hash_do_plano(fontes, registros) == h1                       # determinístico
    fontes2 = dict(fontes)
    fontes2["memorial-versao-cartesian@2026Q2"] = ["obra-b@memorial-versao-cartesian@2026Q2"]
    assert fm.hash_do_plano(fontes2, registros + [{"slug": "obra-b", "data_base": "2026-05-01",
                                                   "snapshot_id": "ab" * 32}]) != h1
    # mesma lista de slugs, data-base confirmada diferente -> outro plano
    assert fm.hash_do_plano(fontes, [{"slug": "obra-a", "data_base": "2026-06-01", "snapshot_id": "ab" * 32}]) != h1


def test_apply_reenvia_quando_o_de_para_libera_um_lote_novo(tmp_path, monkeypatch, capsys):
    """F1: o no-op não pode ser chaveado só no snapshot — resolver o De-Para libera
    lotes NOVOS sem que nada tenha mudado no Memorial."""
    ex = _extratos_basicos()
    chamadas = []
    regras, ov = _cenario_apply(tmp_path, monkeypatch, ex, chamadas)
    argv = ["coletar", "--apply", "--quarentena", str(regras), "--overrides", str(ov)]

    ov.write_text(json.dumps({"rows": [{"memorial_project_id": "P1", "slug_cub": "NOVO",
                                        "data_base_confirmada": "2026-09-01"}]}), encoding="utf-8")
    assert fm.run(argv) == 0
    assert len(chamadas) == 1

    # Leo decide o De-Para do P2; o Memorial não mudou (mesmo snapshot)
    ov.write_text(json.dumps({"rows": [
        {"memorial_project_id": "P1", "slug_cub": "NOVO", "data_base_confirmada": "2026-09-01"},
        {"memorial_project_id": "P2", "slug_cub": "d-lohn-empreendimentos", "data_base_confirmada": "2026-04-01"},
    ]}), encoding="utf-8")
    capsys.readouterr()
    assert fm.run(argv) == 0
    # plano mudou -> reenvia o plano inteiro (upsert idempotente + REPLACE por safra),
    # agora com as duas fontes: a chamada nova e a do lote liberado pelo De-Para
    assert len(chamadas) == 3, "o lote novo do De-Para tem que ser enviado"
    assert "nada a enviar" not in capsys.readouterr().out
    fontes_da_rodada = {c[c.index("--fonte-leva") + 1]: c[c.index("--fonte-leva") + 2:] for c in chamadas[1:]}
    assert fontes_da_rodada["memorial-versao-cartesian@2026Q2"] == [
        "d-lohn-empreendimentos@memorial-versao-cartesian@2026Q2"]

    # terceira rodada, nada mudou -> no-op
    capsys.readouterr()
    assert fm.run(argv) == 0
    assert len(chamadas) == 3
    assert "nada a enviar" in capsys.readouterr().out


def test_staging_separa_fontes_distintas_da_mesma_obra(tmp_path, monkeypatch):
    """F2: fonte A e fonte B da MESMA obra são dois registros datados distintos —
    não podem dividir o diretório `staging/<slug>` (o segundo sobrescrevia o primeiro
    e o loader subia o total errado na linha do cliente)."""
    ex = _extratos_basicos()
    chamadas = []
    regras, ov = _cenario_apply(tmp_path, monkeypatch, ex, chamadas)
    ov.write_text(json.dumps({"rows": [
        {"memorial_project_id": "P1", "slug_cub": "obra-x", "data_base_confirmada": "2026-09-01"},
        {"memorial_project_id": "P2", "slug_cub": "obra-x", "data_base_confirmada": "2026-09-01"},
    ]}), encoding="utf-8")

    assert fm.run(["coletar", "--apply", "--quarentena", str(regras), "--overrides", str(ov)]) == 0

    staging = tmp_path / "staging"
    dir_a = staging / "obra-x@memorial-referencia-cliente@2026Q3"
    dir_b = staging / "obra-x@memorial-versao-cartesian@2026Q3"
    assert dir_a.is_dir() and dir_b.is_dir()
    assert not (staging / "obra-x").exists()
    for d, fonte in ((dir_a, "memorial-referencia-cliente@2026Q3"), (dir_b, "memorial-versao-cartesian@2026Q3")):
        projeto = json.loads((d / "projeto.json").read_text(encoding="utf-8"))
        assert projeto["slug"] == "obra-x"                       # o slug real continua no projeto.json
        assert projeto["memorial"]["fonte_leva"] == fonte
    # totais distintos preservados (era esse o dado que se perdia)
    total_a = json.loads((dir_a / "projeto.json").read_text(encoding="utf-8"))["total"]
    total_b = json.loads((dir_b / "projeto.json").read_text(encoding="utf-8"))["total"]
    assert total_a != total_b

    obras = json.loads((staging / "_memorial" / "memorial_obras.json").read_text(encoding="utf-8"))
    assert [o["slug"] for o in obras] == ["obra-x", "obra-x"]
    assert sorted(o["fonte_leva"] for o in obras) == ["memorial-referencia-cliente@2026Q3",
                                                      "memorial-versao-cartesian@2026Q3"]
    assert sorted(o["staging_dir"] for o in obras) == [dir_a.name, dir_b.name]

    # uma chamada de loader por fonte, cada uma com o diretorio certo
    assert len(chamadas) == 2
    por_fonte = {c[c.index("--fonte-leva") + 1]: c[c.index("--fonte-leva") + 2:] for c in chamadas}
    assert por_fonte["memorial-referencia-cliente@2026Q3"] == [dir_a.name]
    assert por_fonte["memorial-versao-cartesian@2026Q3"] == [dir_b.name]


# ------------------------------------------------------------------ fix round 3 (folha = sem filhos)


def test_folhas_sem_filhos_mistura_de_profundidades():
    """Bug real (Estreito, 2026-09-18): um lote fonte A junta workbooks de profundidades
    diferentes. `nivel_max` olha o nível máximo do LOTE INTEIRO e descarta as folhas do
    workbook mais raso — `sem_filhos` não depende do nível, só de não ter filho no lote."""
    itens = [
        {"item_id": "a", "parent_id": None, "level": 1, "descricao": "workbook 1", "total": None},
        {"item_id": "b", "parent_id": "a", "level": 2, "descricao": "folha rasa 1", "total": Decimal("10")},
        {"item_id": "c", "parent_id": "a", "level": 2, "descricao": "folha rasa 2", "total": Decimal("20")},
        {"item_id": "x", "parent_id": None, "level": 1, "descricao": "workbook 2", "total": None},
        {"item_id": "y", "parent_id": "x", "level": 2, "descricao": "intermediario", "total": None},
        {"item_id": "z1", "parent_id": "y", "level": 3, "descricao": "folha funda 1", "total": Decimal("5")},
        {"item_id": "z2", "parent_id": "y", "level": 3, "descricao": "folha funda 2", "total": Decimal("5")},
    ]
    assert [i["item_id"] for i in fm.folhas(itens, "sem_filhos")] == ["b", "c", "z1", "z2"]
    # documenta o bug antigo: nivel_max só pega o nível mais fundo do lote inteiro
    assert [i["item_id"] for i in fm.folhas(itens, "nivel_max")] == ["z1", "z2"]


def test_montar_lotes_fonte_a_usa_sem_filhos():
    """Mesma mistura de profundidades, agora dentro de um lote fonte A de verdade
    (dois imports do mesmo import_batch_id): a soma das folhas tem que reconciliar
    com a soma do nível 1 — o que falhava com `nivel_max` (Estreito: R$153,2 M vs R$201,3 M)."""
    ex = {
        "imports": [
            {"id": "i1", "project_id": "P1", "client_id": "C1", "import_batch_id": "BX",
             "imported_at": "2026-09-10T12:00:00+00:00"},
            {"id": "i2", "project_id": "P1", "client_id": "C1", "import_batch_id": "BX",
             "imported_at": "2026-09-10T12:01:00+00:00"},
        ],
        "import_items": [
            # workbook 1: raso (level1 'a' -> folhas level2 'b','c')
            {"id": "a", "import_id": "i1", "parent_id": None, "level": 1, "sort_order": 1, "line_code": "01",
             "description": "01. SUPRAESTRUTURA", "unit": None, "quantity": None, "client_unit_cost": None,
             "client_total_price": "100"},
            {"id": "b", "import_id": "i1", "parent_id": "a", "level": 2, "sort_order": 1, "line_code": "01.01",
             "description": "Concreto", "unit": "m3", "quantity": "10", "client_unit_cost": "6",
             "client_total_price": "60"},
            {"id": "c", "import_id": "i1", "parent_id": "a", "level": 2, "sort_order": 2, "line_code": "01.02",
             "description": "Aço", "unit": "kg", "quantity": "100", "client_unit_cost": "0.4",
             "client_total_price": "40"},
            # workbook 2: fundo (level1 'x' -> level2 'y' -> folhas level3 'z1','z2')
            {"id": "x", "import_id": "i2", "parent_id": None, "level": 1, "sort_order": 1, "line_code": "02",
             "description": "02. ESQUADRIAS", "unit": None, "quantity": None, "client_unit_cost": None,
             "client_total_price": "40"},
            {"id": "y", "import_id": "i2", "parent_id": "x", "level": 2, "sort_order": 1, "line_code": "02.01",
             "description": "Janelas", "unit": None, "quantity": None, "client_unit_cost": None,
             "client_total_price": "40"},
            {"id": "z1", "import_id": "i2", "parent_id": "y", "level": 3, "sort_order": 1, "line_code": "02.01.01",
             "description": "Vidro", "unit": "m2", "quantity": "10", "client_unit_cost": "3",
             "client_total_price": "30"},
            {"id": "z2", "import_id": "i2", "parent_id": "y", "level": 3, "sort_order": 2, "line_code": "02.01.02",
             "description": "Esquadria", "unit": "un", "quantity": "5", "client_unit_cost": "2",
             "client_total_price": "10"},
        ],
        "versions": [],
        "budgets": [],
        "projects": [{"id": "P1", "project_name": "Teste", "client_id": "C1", "city": "Itajaí", "state": "SC", "status": "new"}],
        "clients": [{"id": "C1", "name": "Cliente X", "city": "Itajaí", "state": "SC"}],
        "project_towers": [], "tower_floors": [], "project_building_data": [],
    }
    lotes = fm.montar_lotes(ex, hoje=date(2026, 9, 18))
    a = [l for l in lotes if l.fonte == fm.FONTE_CLIENTE][0]
    assert sorted(i["item_id"] for i in a.itens) == ["b", "c", "z1", "z2"]           # não perde as folhas rasas
    assert fm._soma(a.itens) == a.total_declarado == Decimal("140")                  # reconcilia com o nível 1
    pct, ok = fm.reconciliar(fm._soma(a.itens), a.total_declarado)
    assert ok is True
