-- ============================================================================
-- Schema: base de índices Cartesian no Supabase
-- Projeto: indices-cartesian (nzyyptcfiqalhpybklfd, sa-east-1)
-- Criado: 2026-04-20
-- Fonte de migração: ~/orcamentos-openclaw/base/INDICES-CATALOGO.xlsx (10 abas, 6.667 linhas)
-- ============================================================================
-- Cobertura fase 1 (migração 1:1 do xlsx atual):
--   9 tabelas de dados + 1 enum extensível pra tipos de obra
--   RLS ligado com policies: authenticated SELECT only / service_role full
--   Indexes pros padrões de query B (filtro/similaridade) e C (agregação analítica)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 0. Extensões
-- ----------------------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- pra busca parcial nos descricao/nome

-- ----------------------------------------------------------------------------
-- 1. Enum: tipos de obra (extensível conforme Cartesian ingere novos tipos)
-- ----------------------------------------------------------------------------
CREATE TYPE tipo_obra_enum AS ENUM (
    'residencial_vertical',    -- todos os 126 projetos atuais
    'residencial_horizontal',
    'industrial',
    'comercial',
    'galpao',
    'reforma',
    'infraestrutura',
    'misto',
    'outro'
);

CREATE TYPE padrao_gemma_enum AS ENUM (
    'economico',
    'medio',
    'medio-alto',
    'alto',
    'luxo',
    'nao_classificado'
);

-- ----------------------------------------------------------------------------
-- 2. Função utilitária pra updated_at automático
-- ----------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- 3. Tabelas
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 3.1. projetos (aba PROJETOS: 126 projetos da base Cartesian)
-- ----------------------------------------------------------------------------
CREATE TABLE projetos (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug text UNIQUE NOT NULL,
    tipo_obra tipo_obra_enum NOT NULL DEFAULT 'residencial_vertical',
    padrao_gemma padrao_gemma_enum,
    confianca text,                         -- 'alta', 'media', 'baixa' (texto livre do xlsx)
    ac_m2 numeric,                          -- área construída (m²)
    ur integer,                             -- unidades residenciais
    total_rs numeric,                       -- custo total (R$)
    rsm2 numeric,                           -- R$/m²
    m2_por_ur numeric,                      -- m² por UR
    rs_por_ur numeric,                      -- R$ por UR
    cidade text,
    regiao text,                            -- derivado de cidade (UF) quando possível
    fonte text,                             -- origem do dado (ex: gemma_semantico)
    fonte_xlsx_linha integer,               -- rastreabilidade com linha do xlsx
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE TRIGGER trg_projetos_updated_at
    BEFORE UPDATE ON projetos
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_projetos_tipo_padrao_regiao ON projetos (tipo_obra, padrao_gemma, regiao);
CREATE INDEX idx_projetos_cidade ON projetos (cidade);
CREATE INDEX idx_projetos_slug_trgm ON projetos USING gin (slug gin_trgm_ops);

COMMENT ON TABLE projetos IS 'Metadados dos projetos que compõem a base. 126 projetos atuais, todos residencial_vertical. Fonte: aba PROJETOS do INDICES-CATALOGO.xlsx.';

-- ----------------------------------------------------------------------------
-- 3.2. calibracao_global (aba CALIBRACAO_GLOBAL: 18 macrogrupos sem segmentação)
-- ----------------------------------------------------------------------------
CREATE TABLE calibracao_global (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    macrogrupo text NOT NULL,
    n integer,
    min_val numeric,
    p10 numeric,
    p25 numeric,
    mediana numeric,
    media numeric,
    p75 numeric,
    p90 numeric,
    max_val numeric,
    unidade text,
    fonte text,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    UNIQUE (macrogrupo, fonte)
);

CREATE TRIGGER trg_calibracao_global_updated_at
    BEFORE UPDATE ON calibracao_global
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_calibracao_global_macrogrupo ON calibracao_global (macrogrupo);

COMMENT ON TABLE calibracao_global IS 'Calibração V2 global por macrogrupo (18), stats agregadas dos 126 projetos.';

-- ----------------------------------------------------------------------------
-- 3.3. calibracao_condicional (aba CALIBRACAO_CONDICIONAL: 68 linhas por padrão Gemma)
-- ----------------------------------------------------------------------------
CREATE TABLE calibracao_condicional (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    padrao padrao_gemma_enum NOT NULL,
    macrogrupo text NOT NULL,
    n integer,
    min_val numeric,
    p10 numeric,
    p25 numeric,
    mediana numeric,
    media numeric,
    p75 numeric,
    p90 numeric,
    max_val numeric,
    unidade text,
    fonte text,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    UNIQUE (padrao, macrogrupo, fonte)
);

CREATE TRIGGER trg_calibracao_condicional_updated_at
    BEFORE UPDATE ON calibracao_condicional
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_calibracao_condicional_padrao_macrogrupo ON calibracao_condicional (padrao, macrogrupo);

COMMENT ON TABLE calibracao_condicional IS 'Calibração V2 condicional por padrão Gemma (Fase 18b). Medianas por macrogrupo × classe semântica.';

-- ----------------------------------------------------------------------------
-- 3.4. indices_derivados_v2 (aba INDICES_DERIVADOS_V2: 29 índices derivados V2)
-- ----------------------------------------------------------------------------
CREATE TABLE indices_derivados_v2 (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    nome text UNIQUE NOT NULL,
    descricao text,
    tipo_obra tipo_obra_enum NOT NULL DEFAULT 'residencial_vertical',
    n integer,
    min_val numeric,
    p10 numeric,
    p25 numeric,
    mediana numeric,
    media numeric,
    p75 numeric,
    p90 numeric,
    max_val numeric,
    cv numeric,                             -- coeficiente de variação
    unidade text,
    fonte text,
    premissa_md_path text,                  -- ponteiro pra premissa narrativa (D)
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE TRIGGER trg_indices_derivados_v2_updated_at
    BEFORE UPDATE ON indices_derivados_v2
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_indices_derivados_tipo_obra ON indices_derivados_v2 (tipo_obra);
CREATE INDEX idx_indices_derivados_nome_trgm ON indices_derivados_v2 USING gin (nome gin_trgm_ops);

COMMENT ON TABLE indices_derivados_v2 IS '29 índices derivados V2 (PUs de insumos, custos por MG, splits). Ponteiro opcional pra premissa em .md.';

-- ----------------------------------------------------------------------------
-- 3.5. indices_estruturais (aba INDICES_ESTRUTURAIS: estruturais, produto, instalações)
-- ----------------------------------------------------------------------------
CREATE TABLE indices_estruturais (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    categoria text NOT NULL,                -- 'Estruturais', 'Produto', 'Instalações', 'CI', 'Segmentos'
    nome text NOT NULL,
    tipo_obra tipo_obra_enum NOT NULL DEFAULT 'residencial_vertical',
    n integer,
    min_val numeric,
    p10 numeric,
    p25 numeric,
    mediana numeric,
    media numeric,
    p75 numeric,
    p90 numeric,
    max_val numeric,
    unidade text,
    fonte text,
    premissa_md_path text,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    UNIQUE (categoria, nome, tipo_obra)
);

CREATE TRIGGER trg_indices_estruturais_updated_at
    BEFORE UPDATE ON indices_estruturais
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_indices_estruturais_categoria_tipo ON indices_estruturais (categoria, tipo_obra);
CREATE INDEX idx_indices_estruturais_nome_trgm ON indices_estruturais USING gin (nome gin_trgm_ops);

COMMENT ON TABLE indices_estruturais IS 'Consumos físicos (concreto m³/m², aço kg/m²), índices de produto, instalações, CI, segmentos.';

-- ----------------------------------------------------------------------------
-- 3.6. pus_cross_v1 (aba PUS_CROSS_V1: 1.740 clusters com lista de obras fonte)
-- ----------------------------------------------------------------------------
CREATE TABLE pus_cross_v1 (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    categoria text NOT NULL,
    chave text NOT NULL,
    descricao text,
    unidade text,
    n_proj integer,
    n_obs integer,
    min_val numeric,
    p25 numeric,
    mediana numeric,
    p75 numeric,
    max_val numeric,
    cv numeric,
    projetos_fonte text,                    -- lista "; " separada de slugs
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    UNIQUE (categoria, chave)
);

CREATE TRIGGER trg_pus_cross_v1_updated_at
    BEFORE UPDATE ON pus_cross_v1
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_pus_cross_v1_categoria ON pus_cross_v1 (categoria);
CREATE INDEX idx_pus_cross_v1_chave_trgm ON pus_cross_v1 USING gin (chave gin_trgm_ops);
CREATE INDEX idx_pus_cross_v1_descricao_trgm ON pus_cross_v1 USING gin (descricao gin_trgm_ops);

COMMENT ON TABLE pus_cross_v1 IS 'PUs cross-projeto V1 (Fase 10 v1) — 1.740 clusters COM lista de obras fonte.';

-- ----------------------------------------------------------------------------
-- 3.7. pus_cross_v2 (aba PUS_CROSS_V2: 4.210 clusters — GROSSO DA BASE)
-- ----------------------------------------------------------------------------
CREATE TABLE pus_cross_v2 (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    cluster_id integer UNIQUE NOT NULL,
    key_tokens text,                        -- ex: 'infraestrutura', 'complementares|servicos'
    descricao text,
    unidades text,                          -- unidades encontradas nos itens (pode ser múltiplas)
    tipo_obra tipo_obra_enum NOT NULL DEFAULT 'residencial_vertical',
    n_proj integer,
    n_obs integer,
    pu_min numeric,
    pu_p10 numeric,
    pu_p25 numeric,
    pu_mediana numeric,
    pu_p75 numeric,
    pu_p90 numeric,
    pu_max numeric,
    pu_media numeric,
    cv numeric,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE TRIGGER trg_pus_cross_v2_updated_at
    BEFORE UPDATE ON pus_cross_v2
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- Indexes pros padrões B (filtro) e C (agregação) mais comuns
CREATE INDEX idx_pus_cross_v2_tipo_obra ON pus_cross_v2 (tipo_obra);
CREATE INDEX idx_pus_cross_v2_key_tokens ON pus_cross_v2 (key_tokens);
CREATE INDEX idx_pus_cross_v2_key_trgm ON pus_cross_v2 USING gin (key_tokens gin_trgm_ops);
CREATE INDEX idx_pus_cross_v2_descricao_trgm ON pus_cross_v2 USING gin (descricao gin_trgm_ops);

COMMENT ON TABLE pus_cross_v2 IS 'PUs cross-projeto V2 (Fase 10 v2) — 4.210 clusters por hash semântico. Grosso da base de consulta.';

-- ----------------------------------------------------------------------------
-- 3.8. curva_abc_master (aba CURVA_ABC_MASTER: 126 projetos consolidados)
-- ----------------------------------------------------------------------------
CREATE TABLE curva_abc_master (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug text NOT NULL,
    status text,                            -- 'done', 'pending'
    n_itens integer,
    n_a integer,                            -- itens que representam 80% do custo
    pct_a numeric,                          -- proporção desses itens
    valor_total_rs numeric,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    UNIQUE (slug),
    FOREIGN KEY (slug) REFERENCES projetos (slug) ON DELETE CASCADE
);

CREATE TRIGGER trg_curva_abc_master_updated_at
    BEFORE UPDATE ON curva_abc_master
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_curva_abc_slug ON curva_abc_master (slug);

COMMENT ON TABLE curva_abc_master IS 'Curva ABC por projeto. n_a = quantos itens representam 80% do custo. Baixo pct_a = projeto concentrado.';

-- ----------------------------------------------------------------------------
-- 3.9. cross_insights_gemma (aba CROSS_INSIGHTS_GEMMA: análises cross-projeto)
-- ----------------------------------------------------------------------------
CREATE TABLE cross_insights_gemma (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    secao text NOT NULL,                    -- ex: 'familias'
    tipo text,
    campo text,
    conteudo text NOT NULL,
    conteudo_tsv tsvector GENERATED ALWAYS AS (to_tsvector('portuguese', coalesce(conteudo, ''))) STORED,
    fonte_xlsx_linha integer,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW()
);

CREATE TRIGGER trg_cross_insights_gemma_updated_at
    BEFORE UPDATE ON cross_insights_gemma
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE INDEX idx_cross_insights_secao ON cross_insights_gemma (secao);
CREATE INDEX idx_cross_insights_tsv ON cross_insights_gemma USING gin (conteudo_tsv);

COMMENT ON TABLE cross_insights_gemma IS 'Insights qualitativos Gemma cross-projeto. Busca full-text em portuguese via conteudo_tsv.';

-- ============================================================================
-- 4. Row Level Security (RLS)
-- ============================================================================
-- RLS automático já está ligado nesse projeto, mas explicitamos aqui
-- pra garantir reprodutibilidade e documentar as policies.
-- ============================================================================

-- Helper: ativa RLS em uma tabela
ALTER TABLE projetos ENABLE ROW LEVEL SECURITY;
ALTER TABLE calibracao_global ENABLE ROW LEVEL SECURITY;
ALTER TABLE calibracao_condicional ENABLE ROW LEVEL SECURITY;
ALTER TABLE indices_derivados_v2 ENABLE ROW LEVEL SECURITY;
ALTER TABLE indices_estruturais ENABLE ROW LEVEL SECURITY;
ALTER TABLE pus_cross_v1 ENABLE ROW LEVEL SECURITY;
ALTER TABLE pus_cross_v2 ENABLE ROW LEVEL SECURITY;
ALTER TABLE curva_abc_master ENABLE ROW LEVEL SECURITY;
ALTER TABLE cross_insights_gemma ENABLE ROW LEVEL SECURITY;

-- Policies: authenticated SELECT (pra MCP via anon/publishable key + bot Slack futuro)
CREATE POLICY "authenticated_read_projetos" ON projetos FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_calibracao_global" ON calibracao_global FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_calibracao_condicional" ON calibracao_condicional FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_indices_derivados_v2" ON indices_derivados_v2 FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_indices_estruturais" ON indices_estruturais FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_pus_cross_v1" ON pus_cross_v1 FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_pus_cross_v2" ON pus_cross_v2 FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_curva_abc_master" ON curva_abc_master FOR SELECT TO authenticated USING (true);
CREATE POLICY "authenticated_read_cross_insights_gemma" ON cross_insights_gemma FOR SELECT TO authenticated USING (true);

-- Nota: service_role bypassa RLS nativamente. Scripts Python de ingestão usam service_role.
-- Nota: anonymous (sem auth) fica sem acesso — nenhuma policy pra role 'anon'.

-- ============================================================================
-- 5. View de conveniência pra query analítica (C) cross-macrogrupo
-- ============================================================================
CREATE OR REPLACE VIEW v_calibracao_por_padrao AS
SELECT
    cc.padrao,
    cc.macrogrupo,
    cc.mediana AS mediana_condicional,
    cg.mediana AS mediana_global,
    ROUND(((cc.mediana - cg.mediana) / NULLIF(cg.mediana, 0) * 100)::numeric, 2) AS delta_pct,
    cc.unidade,
    cc.n AS n_condicional,
    cg.n AS n_global
FROM calibracao_condicional cc
LEFT JOIN calibracao_global cg ON cg.macrogrupo = cc.macrogrupo AND cg.fonte = cc.fonte;

COMMENT ON VIEW v_calibracao_por_padrao IS 'Comparativo rápido: mediana condicional por padrão vs mediana global de cada macrogrupo.';

-- ============================================================================
-- FIM
-- ============================================================================
