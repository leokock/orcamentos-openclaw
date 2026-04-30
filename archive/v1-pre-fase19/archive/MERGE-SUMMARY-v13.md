# Template Orçamento Paramétrico v13 - Merge Summary

**Data:** 05/03/2026  
**Arquivo:** template-orcamento-parametrico-v13-merged.xlsx  
**Localização:** `~/clawd/orcamento-parametrico/` + `~/.openclaw/media/outbound/`

---

## ✅ FEATURES MERGED FROM COWORK

### 1. **NEW TAB: PAINEL** (Executive Dashboard) — Position 0

Dashboard executivo com 5 seções principais:

#### 1.1 Resumo Executivo (4 KPIs)
- **R$/m² (Custo/AC)** — Link: `=DADOS_PROJETO!B18`
- **Custo Total (R$)** — Link: `=DADOS_PROJETO!B17`
- **R$/UR** — Calculado: `=IF(DADOS_PROJETO!B8>0,DADOS_PROJETO!B17/DADOS_PROJETO!B8,0)`
- **Área Construída (m²)** — Link: `=DADOS_PROJETO!B7`

#### 1.2 Custo por Macrogrupo (17 linhas)
Tabela comparativa com:
- **Coluna B:** R$/m² Paramétrico (link para `CUSTOS_MACROGRUPO!D4:D20`)
- **Coluna C-D:** Min/Max Mercado (link para `CUSTOS_MACROGRUPO!F:G`)
- **Coluna E:** Status automático com lógica condicional:
  - ✓ OK — dentro da faixa
  - ⚠ Baixo — verificar completude
  - ✗ Alto — revisar escopo

#### 1.3 Indicadores de Produto (8 índices)
- CA (Coef. Aproveitamento)
- AC/UR (m²)
- Vagas/UR
- UR/Elevador
- Pvtos Tipo/Total
- Nº Pavimentos
- R$/m² e R$/UR

Todos com faixas benchmark e cálculos automáticos baseados em `DADOS_PROJETO`.

#### 1.4 Decisões do Briefing (5 decisões)
Principais escolhas de projeto com impacto estimado:
- Tipo de Laje
- Padrão Acabamento
- Fachada
- Pé Direito
- Sistema de Elevadores

Links diretos para `BRIEFING!B6, B8, B10, B12, B20`.

#### 1.5 Posicionamento (10 projetos referência)
Top 10 projetos calibrados da base de conhecimento (18 projetos):
- Colline (27.559 m²) — R$ 5.181,69/m²
- Catena (9.242 m²) — R$ 3.376,01/m²
- Fasolo-VdF, Cota365, Redentor, etc.

Dados importados de `calibration-data.json`.

---

### 2. **NEW TAB: ÍNDICES** (Parametric Reference) — Position 2 (after BRIEFING)

Biblioteca técnica completa com 5 seções:

#### 2.1 Índices por Tipo de Laje
6 parâmetros x 5 tipos (Maciça, Cubetas, Cub.Protendida, Treliçada, Protendida):
- Jogos de Fôrma
- Montagem Fôrma (m²/AC)
- Concreto (m³/AC)
- Armadura (kg/m³)
- MO Estrutura (R$/AC)
- Supraestrutura R$/m²

Exemplo: **Maciça** — 12-15 jogos, 0.28-0.35 m³/AC, R$ 750-950/m²

#### 2.2 Índices Gerais (10 parâmetros)
Com faixas Mín/Típico/Máx:
- Estacas (m/m²AC): 0.15 / **0.20** / 0.30
- Alvenaria (m²/m²AC): 1.8 / **2.2** / 2.8
- Contrapiso, Forro, Esquadrias (Al/PVC), Louças/Metais, Pontos (Elétrico/Hidráulico), Elevador (UR/Elev)

#### 2.3 Verbas Paramétricas (10 itens, R$/m² AC)
Standard / Alto / Super Alto:
- **Pintura Interna:** 35-45 / 50-65 / 75-95
- **Rev. Parede Interna:** 120-150 / 180-230 / 280-350
- **Paisagismo:** 15-25 / 35-50 / 65-90
- Etc. (Pintura Externa, Rodapés, Soleiras, Sinalização, Playground, Deck)

#### 2.4 Fatores de Custo (8 fatores)
- **BDI:** 1.10 (faixa 1.08-1.15)
- **Perdas Concreto:** 1.05 (1.03-1.08)
- **Perdas Argamassa:** 1.15 (1.10-1.25)
- Empolamento Terra, Fator Dificuldade, Ajuste Localização, Produtividade MO, Fator Prazo

#### 2.5 Ajustes por Padrão (11 macrogrupos)
Multiplicadores sobre base Standard:
- **Instalações:** 1.00 / 1.25 / 1.60 — Impacto **Alto** (automação, CFTV)
- **Fachada:** 1.00 / 1.60 / 2.40 — Impacto **Alto** (ACM, vidro especial)
- **Sist. Especiais:** 1.00 / 1.40 / 2.00 — Impacto **Alto** (ar central, gerador)

---

### 3. **DADOS_PROJETO EXPANSION** (7 new fields)

Adicionada seção "DADOS COMPLEMENTARES" (rows 22-28):

| Campo | Valor (Maison Beach) | Descrição |
|-------|---------------------|-----------|
| **APT** | 1.795 m² | Área Projeção Torre |
| **PPT** | 191,4 m | Perímetro Projeção Torre |
| **APE** | 2.400 m² | Área Projeção Embasamento |
| **PPE** | 208 m | Perímetro Projeção Embasamento |
| **NPD** | 1 | Nº Pav. Tipo Diferenciados |
| **Área de Lazer** | (input) | Área de Lazer (m²) |
| **BDI** | 1.10 | Bonificação e Despesas Indiretas |

Todos com **fundo azul** (input cells) e formatação numérica `#,##0.00`.

---

### 4. **BRIEFING QUESTIONS** (5 new questions)

Inseridas após row 29 (antes do RESUMO):

| Pergunta | Default | Impacta |
|----------|---------|---------|
| **Gerador?** | Não | Sist. Especiais |
| **Subestação?** | Não | Sist. Especiais |
| **Placas Fotovoltaicas?** | Não | Sist. Especiais |
| **Infra Carro Elétrico?** | Não | Instalações |
| **Pressurização Escada?** | Sim | Instalações |

---

## 📊 FINAL STRUCTURE

| # | Sheet Name | Rows | Status |
|---|-----------|------|--------|
| 0 | **PAINEL** | 59 | ✅ NEW |
| 1 | BRIEFING | 54 | ✅ UPDATED (+5 questions) |
| 2 | **ÍNDICES** | 61 | ✅ NEW |
| 3 | ANÁLISE_PRODUTO | 33 | ⚪ Preserved |
| 4 | DADOS_PROJETO | 28 | ✅ UPDATED (+7 fields) |
| 5 | CUSTOS_MACROGRUPO | 23 | ⚪ Preserved |
| 6 | ESTRUTURAL | 28 | ⚪ Preserved |
| 7 | INSTALACOES | 13 | ⚪ Preserved |
| 8 | ACABAMENTOS | 56 | ⚪ Preserved |
| 9 | CI_DETALHADO | 73 | ⚪ Preserved |
| 10 | BENCHMARK | 45 | ⚪ Preserved |
| 11 | ALERTAS | 29 | ⚪ Preserved |
| 12 | PRODUTO | 53 | ⚪ Preserved |
| 13 | ANÁLISE_ÍNDICE_PRODUTO | 58 | ⚪ Preserved |

**Total:** 14 sheets (2 new, 2 updated, 10 preserved)

---

## ✅ VERIFICATION CHECKLIST

- [x] **PAINEL tab** criado na posição 0 (antes de BRIEFING)
- [x] **ÍNDICES tab** criado na posição 2 (depois de BRIEFING)
- [x] **DADOS_PROJETO** expandido com 7 novos campos
- [x] **BRIEFING** atualizado com 5 novas perguntas
- [x] Todas as fórmulas referenciam sheets corretos
- [x] Estilo consistente (headers azul escuro, inputs azul claro, calc cinza)
- [x] Bordas finas (thin, #BDC3C7) aplicadas
- [x] Formatação numérica correta (#,##0.00 para valores, 0.0% para %)
- [x] Projetos de calibração (top 10) importados corretamente
- [x] Sem células mescladas em linhas de dados (apenas títulos)
- [x] Todas as fórmulas em inglês (IF, SUM, AVERAGE)
- [x] Arquivo salvo em ambos os locais (working + outbound)

---

## 🔗 KEY FORMULAS

### PAINEL → DADOS_PROJETO
- `PAINEL!B4` → `=DADOS_PROJETO!B18` (R$/m²)
- `PAINEL!B5` → `=DADOS_PROJETO!B17` (Custo Total)
- `PAINEL!B6` → `=IF(DADOS_PROJETO!B8>0,DADOS_PROJETO!B17/DADOS_PROJETO!B8,0)` (R$/UR)

### PAINEL → CUSTOS_MACROGRUPO
- `PAINEL!B12:B28` → `=CUSTOS_MACROGRUPO!D4:D20` (R$/m² por macrogrupo)
- `PAINEL!C12:C28` → `=CUSTOS_MACROGRUPO!F4:F20` (Min mercado)
- `PAINEL!D12:D28` → `=CUSTOS_MACROGRUPO!G4:G20` (Max mercado)

### PAINEL → BRIEFING
- `PAINEL!B44:B48` → `=BRIEFING!B6, B8, B10, B12, B20` (Decisões principais)

### Status Condicional (PAINEL!E12:E28)
```excel
=IF(B12=0,"—",
  IF(B12>D12,"✗ Alto - Revisar escopo",
    IF(B12<C12,"⚠ Baixo - Verificar completude",
      "✓ OK - Dentro da faixa")))
```

---

## 📁 FILES GENERATED

1. **Working file (updated):**  
   `~/clawd/orcamento-parametrico/template-orcamento-parametrico.xlsx`

2. **Outbound copy (delivery):**  
   `~/.openclaw/media/outbound/template-orcamento-parametrico-v13-merged.xlsx`

3. **Merge script (preserved):**  
   `~/clawd/orcamento-parametrico/merge_cowork.py`

4. **This summary:**  
   `~/clawd/orcamento-parametrico/MERGE-SUMMARY-v13.md`

---

## 📚 DATA SOURCES

- **Calibration data:** `calibration-data.json` (18 projects)
- **Reference file:** Cowork template (46bc353d-09f1-45b8-ada0-80129c809266.xlsx)
- **Existing template:** template-orcamento-parametrico.xlsx (v12)

---

## 🎯 NEXT STEPS (Recommendations)

1. **Abrir o arquivo** e validar visualmente as seções do PAINEL
2. **Testar fórmulas** alterando valores em DADOS_PROJETO e verificando PAINEL
3. **Revisar faixas benchmark** na aba ÍNDICES (ajustar se necessário baseado na base real)
4. **Calibrar STATUS** da aba PAINEL se as faixas Min/Max do CUSTOS_MACROGRUPO estiverem desatualizadas
5. **Expandir POSICIONAMENTO** se quiser incluir mais projetos (atualmente top 10 por tamanho)
6. **Integrar com outros projetos** — copiar PAINEL e ÍNDICES para templates de projetos específicos

---

**✅ MERGE COMPLETED SUCCESSFULLY — 05/03/2026 16:38 BRT**
