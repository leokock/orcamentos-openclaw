# Comparativo — Listas de Materiais (PDFs Eletrowatts) × Base Cartesian

**Data:** 2026-04-14
**Fonte:** 7 PDFs em `_Projetos_IA/thozen-electra/projetos/15. Listas de quantitativos/`
**Extrator:** `scripts/parse_lista_materiais.py` (dual-format: Eletrowatts template A + QT-MAT template B)
**Disciplinas afetadas:** SPDA, Telecom, Elétrico

---

## Resumo das extrações

| PDF | Disciplina | Formato | Itens | Status pareamento |
|-----|-----------|---------|-------|-------------------|
| `LM - Caixas e Quadros - Electra - SPDA (1).pdf` | SPDA | A (template manual) | 1 real + 46 placeholders vazios | Manual (layout fragmentado) |
| `LM - Caixas e Quadros - Electra - Telecom (1).pdf` | Telecom | A | 28 | Pareado 100% |
| `LM - Caixas e Quadros - Electra - Elétrico Aprovativo (1).pdf` | Elétrico | A | 16 | Pareado 100% |
| `LM - Caixas e Quadros - Electra - Elétrico Executivo (1).pdf` | Elétrico | A | 113 | Parcial (produtos com ruído multi-página) |
| `LM - Caixas e Quadros - Electra - Preventivo Elétrico (1).pdf` | Elétrico | A | 49 | Parcial |
| `LM - Caixas e Quadros - Electra (1).pdf` | Elétrico | B (QT-MAT-1941) | 39 em 3 docs | Inline OK |
| `LM - Caixas e Quadros - Electra - DISJUNTORES (1).pdf` | Elétrico | B (QT-MAT ×18) | 167 em 18 CDs | Inline OK |

**Total extraído: 413 itens granulares com rastreabilidade ao PDF de origem.**

JSONs salvos em `quantitativos/listas-materiais/{eletrico,spda,telecom}/`.

---

## SPDA — R01 (primeira entrega)

### O que o PDF adicionou

| Item | Qtd | Dim | Observação |
|------|-----|-----|------------|
| Caixa de equipotencialização (BEL) alumínio pintura branca | 12 | 20×20×15 cm | Não constava no briefing R00. Classificada em `07.02.03.007` (Equipotencialização) |

> **Nota:** O PDF listou 47 linhas no template, mas apenas a linha 1 tinha dados reais. Linhas 2-47 são placeholders vazios (identificados por inspeção visual do PDF renderizado). Layout tabular fragmentou o texto, bloqueando o parser heurístico — extração manual.

### O que já tinha no briefing R00 (NBR 5419)

Mantido integralmente:
- Captação: 6 captores Franklin, 24 chumbadores (07.02.01.*)
- Descidas: 354 m cabo 50 mm² + 176 braçadeiras + 32 conectores (07.02.02.*)
- Equipotencialização: 600 m cabo 35 mm² + 100 conectores + 8 barras equipotenciais (07.02.03.*)
- Aterramento: 8 hastes + 4 caixas inspeção + 1000 m malha (07.02.04.*)
- Acessórios: conectores paralelos/cruzados + fita advertência (07.02.05.*)

### Entrega

- **`disciplinas/spda/spda-electra-r01.xlsx`** — primeira planilha formal SPDA
- **Total material + MO:** R$ 185.091,92
- **R$/m² AC:** 5,13 (AC = 36.092 m²)
- **Benchmark Cartesian (27 projetos, mediana 5,14 R$/m²):** R$ 185.512,88
- **Aderência:** Δ = −0,23 % vs mediana ✅

---

## Telecom — R03 (suplemento ao R02)

### O que o PDF adicionou

**28 caixas de passagem telecom** (infraestrutura tronco por pavimento) distribuídas:

| Bloco | Caixas | Pavimentos |
|-------|--------|------------|
| **A** | 14 caixas | Térreo (2), G1 (4+1+1), G2-G5 (1 cada), Lazer (1+1), Tipo×24 (1), C.Máq (2) |
| **B** | 14 caixas | Térreo (2), G1 (1+3), G2-G5 (1 cada), Lazer (1+1), Tipo×24 (2), C.Máq (2) |

Dimensões variam: 20×20×12 cm até 60×120×20 cm. Todas são "CX. DE PASSAGEM TELECOM C/ PORTA + VISTA, FUNDO DE MADEIRA /BRANCA".

### O que já tinha no R02

O R02 (30/mar, R$ 424k) cobria:
- **IFC:** 648 caixas 4×2 / 4×4 / octogonais (tomadas telecom/dados)
- **DWG:** 4.414 cotovelos + 415 conectores + 324 trechos cabos + 222 pontos ativos (interfones/CFTV/controle acesso)
- **Eletrodutos:** ~33,4 km (IFC)

### Conclusão da comparação

✅ **Os 28 itens do PDF SÃO NOVOS** (não havia no IFC/DWG) — são caixas de passagem TRONCO (não caixas de tomada). Adicionam ao escopo existente sem duplicar.

### Entrega

- **`disciplinas/telefonico/telecomunicacoes-electra-r03.xlsx`** — suplemento ao R02
- **Aba 1 (CAIXAS PASSAGEM PDF):** 28 itens com PU por faixa de volume (SINAPI adapt. + mercado SC)
- **Aba 2 (RESUMO R03):** total R02 + total suplemento + consolidado
- **Suplemento material + MO (20 %):** R$ 39.012,00 (R$ 1,08/m² AC)
- **Total consolidado R03 (R02 + suplemento):** R$ 463.012,00 (R$ 12,83/m² AC)

---

## Elétrico — R03 (suplemento multi-aba ao R02)

### O que os 5 PDFs adicionaram

**Aba 1 — QUADROS PRINCIPAIS (16 itens do Aprovativo):**

| # | Tipo | Qtd | Exemplo |
|---|------|-----|---------|
| 1-2, 15-16 | QGBT (Quadro Geral BT) | 4 | QGBT 01, 02, 03 + outro |
| 3-4 | QM Convencional | 2 | QM 01, 02 Bloco A/B |
| 5-6 | QM Bus Way | 2 | QM-03 AO 26 (Bloco A), QM-27 AO 50 (Bloco B) — 24 medidores cada |
| 7-10 | Telemedição concentradora | 4 | Concentradora e c/ medição local, Bloco A/B |
| 11 | Banco de capacitores | 1 | Condomínio |
| 12 | BEP | 1 | Barra equipotencialização central |
| 13-14 | Caixa porta-fusíveis / Armário docs | 2 | |

**Total quadros: R$ 623.600 (100% com PU cadastrado)**

**Aba 2 — CAIXAS DE PASSAGEM (162 itens: 113 Executivo + 49 Preventivo):**

Distribuição por local:
- Térreo (Torres A e B): ~18 caixas
- Garagens G1-G5: ~70 caixas (15×15×10 a 60×40×20)
- Lazer: ~15 caixas
- Pavimentos tipo ×24: ~15 caixas
- Casa de Máquinas: ~22 caixas

**Total caixas de passagem: R$ 129.045 (89 fallbacks em amarelo no xlsx — dimensão "VERIFICAR DIAGRAMA" não parseável)**

⚠️ Os 89 fallbacks são itens do Executivo/Preventivo cujas "dimensões" no PDF dizem "VERIFICAR DIAGRAMA" ou "VER PROJETO APROVAT." — o projetista remete ao desenho. Para esses, usei PU default de R$ 150 (destacado em amarelo). **Leo precisa revisar manualmente ou vir com decisão de PU médio para esses casos.**

**Aba 3 — MATERIAL INTERNO CD (39 itens do QT-MAT-1941):**

Um CD de apartamento tipo (8º ao 31º pavto) precisa internamente:
- Barramentos (neutro azul, terra verde, pente trifásico 12P/18P)
- Cabos flexíveis 10/6/4/2,5 mm²
- Terminais pré-isolados tipo tubo (ilhós) — duplo e simples
- **Multiplicação: este PDF cobre 1 CD tipo; a obra tem 96 unidades (24 pav × 4 aptos × 1 CD = 96 repetidas no QT-MAT)**

**Total material interno CD: R$ 79.133 (5 fallbacks)**

> Observação: o QT-MAT-1941 já aplica multiplicador ×96/192/480/960 (ver coluna QTD). Portanto o total já está escalado pra toda a obra — não somar de novo.

**Aba 4 — DISJUNTORES (167 itens em 18 CDs):**

18 CDs diferentes, cada um com sua lista de proteção:
- CD COND. (Condomínio, com e sem gerador) — Bloco A e B
- CD APTO (por tipo, Bloco A e B)
- CD Específicos (outros tipos)

Tipos de proteção cobertos:
- Minidisjuntores monofásicos (6A-63A) e trifásicos (6A-63A)
- IDRs bipolares (25A-63A) e tetrapolares (40A-100A)
- DPS monopolares e tripolares (275V classe II)
- Disjuntores caixa moldada (70A-250A, 10 kA)
- Timers digitais + Contatores (10A-40A)

**Total disjuntores: R$ 497.048 (9 fallbacks)**

### Comparação com R02

**R02 (25/mar, R$ 6.444.152 = R$ 178,56/m²):**
- 3 % verde (rastreável) — luminárias e eletrodutos do IFC
- 56 % amarelo (referência Elizabeth II Royal Home)
- **41 % vermelho (sem fonte) — aqui entram os quadros/disjuntores/material interno que agora os PDFs rastreiam**

**R03 suplemento = R$ 1.328.826 (R$ 36,82/m²)**

> ⚠️ **IMPORTANTE: R03 não soma ao R02.** O R03 substitui os itens "vermelhos" do R02 pelos itens rastreáveis do PDF. A ação pra Leo é:
> 1. Abrir R02 e identificar linhas "vermelhas" de quadros/disjuntores/material interno CD
> 2. Substituir pelos valores do R03 (que agora têm fonte PDF)
> 3. Manter no R02 as partes "verdes" (IFC) e "amarelas" (referência) intactas
> 4. Total final ≈ R02 ajustado para R03 rastreável

### Pendências R02 não cobertas pelos PDFs

Os PDFs cobrem "caixas e quadros", mas NÃO resolvem:
1. Comprimento médio dos trechos de eletroduto (IFC não tem Length)
2. Fator cabos vs eletrodutos (1:1? 1,5×?)
3. Subestação/gerador/barramento — compartilhados entre torres?
4. MO elétrica — R02 tinha R$ 170/m² vs mediana base R$ 26/m²
5. Cabos de força metragem
6. Luminárias (qtd ok, PU pendente)

### Entrega

- **`disciplinas/eletrico/eletrico-electra-r03.xlsx`** — 5 abas (RESUMO + 4 temáticas)
- **Total suplemento:** R$ 1.328.826 (R$ 36,82/m² AC)
- **Itens rastreáveis agregados (destravam "vermelho" do R02):** 16 quadros + 162 caixas + 39 material interno + 167 disjuntores = **384 itens**

---

## Itens em amarelo (fallback PU — revisão Leo)

| Aba | Itens fallback | Motivo | Ação |
|-----|----------------|--------|------|
| Elétrico CAIXAS PASSAGEM | 89/162 (55%) | Dimensão "VERIFICAR DIAGRAMA" no PDF | Leo define PU médio ou abre DWG pra ver dimensões |
| Elétrico MATERIAL INTERNO | 5/39 (13%) | Item sem keyword na tabela PU | Leo cota ou adiciona keyword |
| Elétrico DISJUNTORES | 9/167 (5%) | Item sem keyword na tabela PU | Leo cota ou adiciona keyword |
| Elétrico QUADROS | 0/16 | — | ✅ todos cobertos |
| SPDA | 0/28 | — | ✅ todos cobertos |
| Telecom | 0/28 | — | ✅ todos cobertos |

---

## Próximos passos recomendados

1. **Leo valida os 3 xlsx** (SPDA R01, Telecom R03, Elétrico R03) — olha top 10 itens por valor em cada, confere se o PU é razoável
2. **Para Elétrico:** decidir PU médio dos 89 itens fallback "VERIFICAR DIAGRAMA" ou processar DWGs para dimensões reais
3. **Consolidar no master:** colar os totais do R03 nas abas corretas do `CTN-TZN_ELT - Orçamento Executivo_R00_Leo rev01.xlsx`
4. **Registrar no log-execucao.md** (seção 27 appended)
5. **Atualizar checklist `gestao-orcamento-electra.md`**: marcar `[x]` nos itens destravados
