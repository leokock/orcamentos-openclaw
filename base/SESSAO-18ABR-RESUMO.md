# Sessão 18/abr — Evoluções em Análise de Produto

**Entregas desta sessão:**

1. ✅ Correção da canonização de macrogrupos (→ "Outros" caiu de 18% → 5%)
2. ✅ Script `comparar_param_exec.py` implementado
3. ✅ Fichas de cliente (8 clientes prioritários) em Excel
4. ✅ Todos os Excels regenerados com dados refinados

---

## 1. Canonização de MG corrigida

**Problema:** Cluster 2 tinha 18% em "Outros" — 3 nomes de MG não mapeados:
- `Pintura` (26 projetos, R$ 42M) — regra só pegava "pintura interna" e "pinturas"
- `Rev.Int.Parede` (24 projetos, R$ 48M) — abreviação não coberta
- `Instalações` (22 projetos, R$ 109M) — genérico sem breakdown

**Fix:** adicionados 3 MGs canônicos novos em `analise_avancada.py` e `analise_financeira_executivos.py`:
- **"Pintura Geral"** — captura "Pintura" genérico
- **"Instalacoes Gerais"** — captura "Instalações" sem breakdown
- **"Revestimentos Parede"** — expandida com "Rev.Int.Parede", "rev.int.parede", etc

**Resultado — Clusters recalculados:**

| Cluster | N | AC med | R$/m² | Top MG | Assinatura |
|---|---:|---:|---:|---|---|
| 0 | 32 | 5.183 | 3.542 | Supra 21% | "Construção padrão" |
| **1** | 9 | 3.972 | **5.247** | **Ger 42.5%** | Alto-gerenciamento (ex-Cluster 3) |
| 2 | 28 | 12.674 | 3.291 | Supra 17.5% + **Instalacoes Gerais 10.3%** | Grande, instalações não detalhadas |
| 3 | 7 | 7.529 | 3.761 | **Ger 27% + Supra 22%** | Híbrido |

O antigo Cluster 3 (13 projetos ger>30%) virou agora Cluster 1 (9 projetos ger 42%) + parte do Cluster 3 (7 projetos com ger menor mas ainda alto) — **refinamento**, não discrepância.

---

## 2. Script `comparar_param_exec.py` implementado

Caminho: `scripts/comparar_param_exec.py`

**Uso:**
```bash
# Par com slug idêntico
python scripts/comparar_param_exec.py --slug arthen-arboris

# Par com slugs diferentes (cross-reference manual)
python scripts/comparar_param_exec.py --slug-param thozen-electra --slug-exec thozen-mirador-de-alicante
```

**Output:**
- `base/comparacoes-param-exec/{slug}.json` — dados brutos
- `base/comparacoes-param-exec/{slug}.md` — relatório formatado

**Schema do relatório:**
- Totais lado a lado (paramétrico vs executivo)
- Delta absoluto e %
- Diagnóstico (DENTRO / ALERTA / ATENÇÃO / FORA DA FAIXA)
- Breakdown por MG canônico
- Top 5 MGs com maior alta e queda

**Tentativas de fontes do breakdown paramétrico (em ordem):**
1. `state.json` → `preliminar_result.macrogrupos`
2. `parametrico-v2-config.json`
3. Excel `parametrico-*.xlsx` → aba `CUSTOS_MACROGRUPO`

**Teste executado:** `thozen-electra` (paramétrico) vs `thozen-mirador-de-alicante` (executivo) — projetos diferentes, só pra testar pipeline. Retornou diagnóstico correto de "FORA DA FAIXA -77.8%" (esperado já que são obras distintas).

---

## 3. Fichas de cliente — entregável comercial

Arquivo: `fichas-cliente-cartesian.xlsx` (uma aba por cliente + LEIA_ME)

**8 clientes prioritários incluídos:**

| Cliente | N proj | R$/m² med | Padrão dominante |
|---|---:|---:|---|
| Nova Empreendimentos | 4 | R$ 6.107 | alto |
| Paludo | 5 | R$ 2.781 | médio-alto |
| Mussi Empreendimentos | 4 | R$ 2.949 | médio-alto |
| Pass-e | 6 | R$ 3.429 | médio-alto |
| Santa Maria | 3 | R$ 1.604 | alto |
| Amalfi | 4 | N/D | alto |
| Chiquetti & Dalvesco | 6 | N/D | alto |
| F. Nogueira | 2 | R$ 2.592 | médio-alto |

**Conteúdo de cada ficha (aba):**

1. **Métricas-chave** — N proj, AC total/mediana, R$/m² mediana+faixa, total acumulado, padrão dominante, mix de padrões
2. **Posicionamento vs mediana do padrão** — delta %, interpretação automática (premium/alinhado/eficiente/investigar)
3. **Assinatura % MG** — mediana do cliente em cada MG vs benchmark do padrão, delta pp, leitura
4. **Lista de projetos** — com padrão, AC, UR, total, R$/m²
5. **Observações qualitativas** — até 10 por projeto, com categoria/contexto/texto

**Uso operacional:** abrir a aba do cliente antes de reunião comercial. Mostra o perfil completo em 1 tela.

---

## Arquivos no Drive (`~/orcamentos/parametricos/`)

Estado atual (5 Excels + 4 MDs):

| Arquivo | Foco | Tamanho |
|---|---|---:|
| `analise-produto-cartesian.xlsx` | Indicadores físicos (18 abas) | 163 KB |
| `analise-financeira-cartesian.xlsx` | R$ e % MG (12 abas) | 35 KB |
| `analise-avancada-cartesian.xlsx` | Cliente + cluster + qualitativa (8 abas) | 26 KB |
| `cluster3-e-parametrico.xlsx` | Deep-dive + validação (5 abas) | 13 KB |
| **`fichas-cliente-cartesian.xlsx`** | 8 fichas por cliente + LEIA_ME | 33 KB |
| `ANALISE-*-RESUMO.md` (4 arquivos) | Narrativa PT-BR | — |

---

## Próximos passos sugeridos (não executados)

1. **Preencher AC dos clientes que faltam** (Amalfi, Chiquetti) — habilitaria R$/m² e posicionamento nas fichas.
2. **Comparar Paludo vs Nova em detalhe** — mesmo Cluster 1 (alto-gerenciamento) mas R$/m² muito diferente. O que Paludo faz no escopo que Nova não? Análise na estrutura de itens.
3. **Rodar `comparar_param_exec.py` quando arthen-arboris virar executivo** — primeiro par rastreável da base.
4. **Expandir fichas** pra clientes com ≥3 projetos mas ainda sem dados completos (CK, CN Brava, Grandezza, Inbrasul, Muller, Neuhaus).
5. **Integrar observações qualitativas com fichas comerciais** — extrair "alertas" e "revisões" específicos do cliente pra insight dos orçamentistas em reunião.
