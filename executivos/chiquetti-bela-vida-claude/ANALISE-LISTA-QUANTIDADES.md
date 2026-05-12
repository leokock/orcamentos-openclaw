# Análise — Lista de Quantidades / Bela Vida (Chiquetti)

> Fase 1 do plano `g-drives-compartilhados-03-ctn-projetos-pure-iverson.md`.
> Diagnóstico dos 5 arquivos de QTO antes de gerar `extracao_{disc}.xlsx`.

## Contexto rápido

- **Projeto:** Bela Vida — Chiquetti & Dal Vesco, Florianópolis/SC
- **Pasta-fonte (Drive):** `03 CTN Projetos\2. Projetos em Andamento\Chiquetti e Dal Vesco\2024 - Bela Vida\04. Custo\Lista de Quantidades\`
- **Destino dos extracoes:** `_Executivo_IA\chiquetti-bela-vida-claude\extracao\`
- **Momento:** assembleia 19/05/2026; aporte sensível pra defender 10.797 CUB. Esta extração serve de base técnica pra evolução do executivo R02.
- **Decisões já tomadas:** 5 disciplinas (CLI/ELE/HID/SAN/TEL — sem PCI), 5 arquivos individuais, Pavimento = `"Não Identificado"` em tudo (Pati distribui depois).

---

## Síntese — 5 disciplinas

| # | Disc | Arquivo | Rev | Macro | Itens-folha | Categorias | Estado |
|---|---|---|---|---|---|---|---|
| 1 | **CLI** Climatização | `CDV_BLV_CLI_EX_000_GER_QTV_R02.xlsx` | EX **R02** | 08 | **96** (92 main + 4 dutos churrasqueira) | 14 | ✅ EAP numerada pronta; ignoradas 3 linhas "TOTAL"/"CLIMATIZAÇÃO" |
| 2 | **ELE** Elétrica | `CDV_BLV_ELE_EP_000_GER_QNT_R00.xlsx` | **EP R00** | 07 | **183** brutos → **181** após dedupe | 24 | ⚠️ 2 grupos duplicados (caixas de luz) → somados |
| 3 | **HID** Hidráulica | `CDV_BLV_HID_EX_000_DOC_QUANTITATIVO_R00.xlsx` | EX R00 | 07 | **125** | 5 sistemas Revit | ⚠️ 11 itens em "Não definido" (sistema vazio) |
| 4 | **SAN** Sanitária | `CDV_BLV_SAN_EX_000_DOC_QUANTITATIVO_R00.xlsx` | EX R00 | 07 | **89** | 4 subcat inferidas (Esgoto/AF/Mat./Conex.) | ⚠️ Sem coluna Sistema na fonte; subcategoria inferida do nome da família |
| 5 | **TEL** Telecom | `CDV_BLV_TEL_EP_000_GER_QNT_R00.xls` | **EP R00** | 07 | **52** | 11 | ✅ Sem duplicações; mesmo estilo da ELE só que mais enxuto |
| | | | | **TOTAL** | **543 itens-folha** (após dedupe ELE) | | |

⚠️ = exige tratamento antes da extração; ✅ = pronto.

**Macrogrupos da EAP Cartesian alinhados** (`templates/EAP-BASE.md`):
- **N1 07** Inst. Elétricas, Hidráulicas, GLP e Preventivas → ELE, HID, SAN, TEL
- **N1 08** Climatização, Exaustão e Pressurização → CLI

---

## 1. CLI Climatização — R02 (executivo)

**Estado:** ✅ pronto pra import. Já tem EAP numerada estilo `1.1.1`, descrição, unidade e quantidade. Custos zerados (esperado — quantitativo puro). Vamos preservar a EAP da fonte como `Código fonte`.

### Estrutura de categorias (14 detectadas)

| Itens | Categoria fonte |
|---:|---|
| 32 | `1.2 DUTOS` |
| 15 | `2.1 DUTOS` |
|  6 | `2.2. DIFUSORES, GRADES E GRELHAS E ACESSÓRIOS` |
|  5 | `1.1.EQUIPAMENTOS` |
|  5 | `1.1. VENTILADORES` |
|  4 | `2.1. TUBULAÇÃO DE COBRE P/ SPLIT INVERTER` |
|  4 | `2.2. ISOLAMENTO P/ TUBULAÇÕES DE COBRE SPLIT INVERTER` |
|  4 | `2.4. CAIXAS DE PASSAGEM` |
|  4 | `1.1 EQUIPAMENTOS` |
|  4 | `1.3 GRELHAS` |
|  3 | `2.3.ELÉTRICA` |
|  3 | `3.1.CALÇOS. AMORTECEDORES DE VIBRAÇÃO, e SUPORTES` |
|  3 | `1.3 COIFAS E ACESSÓRIOS` |
|  1 | `?` (item antes do primeiro header válido — investigar na extração) |

**Observação CLI:** existem duas grafias parecidas para "EQUIPAMENTOS" (`1.1.EQUIPAMENTOS` e `1.1 EQUIPAMENTOS`) e dois "DUTOS" (`1.2 DUTOS` e `2.1 DUTOS`). Vamos preservar a grafia original como `Categoria fonte`, sem consolidar — quem decide consolidação é a Pati.

### Sheet auxiliar "Sheet1" — Dutos Churrasqueira

4 itens separados, todos com `System Type = "churrasqueira"`:
- Colarinho redondo de alumínio Ø200 — **40 un**
- Curva 1,0 R 45° Ø200 — **33 un**
- Curva 1,0 R 90° Ø200 — **12 un**
- Transição redondo→retangular Ø200 — **1 un**

Vai como `Categoria fonte = "Dutos churrasqueira (Sheet1)"` no extracao.

### Top 5 por quantidade

|  Qtd  | Un | Categoria | Descrição |
|---:|---|---|---|
| 1026 | m | 2.3.ELÉTRICA | ELETRODUTO FLEXÍVEL CORRUGADO Ø3/4" |
| 997 | m | 2.3.ELÉTRICA | CABO COMUNICAÇÃO PP 4x1,50 mm² |
| 772 | m | 2.1. TUB COBRE SPLIT | Tubulação cobre AC split |
| 772 | m | 2.2. ISOLAMENTO | Isolamento térmico polietileno |
| 575 | m | 2.1. TUB COBRE SPLIT | Tubulação cobre AC split (outro diâm.) |

---

## 2. ELE Elétrica — **EP R00** (estudo preliminar)

**Estado:** ⚠️ requer **dedupe + soma**. É a maior planilha em volume mas está em estudo preliminar — números vão evoluir.

### Categorias (24, top 15)

| Itens | Categoria |
|---:|---|
| 40 | Cabos |
| 28 | DISJUNTORES |
| 12 | Quadro de distribuição |
| 12 | Eletrodutos |
| 11 | Caixas de Embutir |
| 11 | Derivações de Eletrocalhas |
| 11 | Derivações de Eletrodutos |
|  9 | Tomadas |
|  8 | Fixações Elétricas |
|  8 | Interruptores |
|  4 | Caixas de Passagem Elétrica |
|  4 | Conduletes de PVC |
|  4 | Derivações para Eletrodutos de PVC Rígido |
|  4 | Interruptores + Tomadas |
|  3 | Aterramento |
| … | (mais 9 categorias) |

### Duplicações detectadas (2 grupos)

Mesma `(Categoria, Descrição, Unidade)` aparecendo em linhas diferentes:

1. **Caixas de Embutir / "Caixa de Luz 4''x2''" / pç** — 2 ocorrências (linhas 9 e 16 — primeiro bloco bate com segundo)
2. **Caixas de Embutir / "Caixa de Luz 4''x4''" / pç** — 2 ocorrências

**Tratamento na extração:** somar e marcar em `Observação = "merged: 2 ocorrências"`. Após dedupe: **181 itens únicos** (de 183 originais).

### Top 5 por quantidade

|  Qtd  | Un | Categoria | Descrição |
|---:|---|---|---|
| 10613 | m | Eletrodutos | Eletroduto flexível corrugado Reforçado PVC laranja |
| 6426 | m | Cabos | Cabo cobre PVC 750V — 2,5 mm² azul claro |
| 4550 | m | Cabos | Cabo cobre PVC 750V — 2,5 mm² verde |
| 3382 | m | Cabos | Cabo cobre PVC 750V — 2,5 mm² amarelo |
| 2848 | m | Eletrodutos | Eletroduto corrugado (outro diâm.) |

---

## 3. HID Hidráulica — R00 (executivo)

**Estado:** ✅ items extraíveis, mas **estrutura em 4 sheets** exige normalização. Já tem coluna `Tipo de sistema` (AA/AF/AQ) que ajuda a segregar Água Fria vs Quente vs Aproveitamento.

### Distribuição por sistema Revit

| Itens | Sistema | Significado |
|---:|---|---|
| 66 | BE HS HID AF | Água Fria |
| 15 | BE HS HID AQ | Água Quente |
|  9 | BE HS HID AA | Água de Aproveitamento (pluvial reutilizada) |
| 11 | **Não definido** | ⚠️ Sistema vazio na fonte — investigar/alertar |
|  2 | Água fria doméstica | (legado nomenclatura) |

### Distribuição por sheet de origem

| Itens | Sheet |
|---:|---|
| 79 | Tigre - Conexões |
| 22 | Quant de material hidráulico |
| 16 | Tabela de acessório de tubo |
|  8 | Quant de tubos (vai como unidade `m`) |

### Top 5 por quantidade

|  Qtd  | Un | Sistema | Descrição |
|---:|---|---|---|
| 1750 | m | AQ | Tubo PPR PN20 Água Fria/Quente DN 25 |
| 1669 | m | AF | Tubo Marrom Água Fria Soldável DN 25 |
| 1302 | un | AQ | Joelho 90° 22 mm PPR Tigre |
| 1297 | un | AF | Joelho 90° Soldável 25 mm PVC Marrom |
| 1024 | m | AF | Tubo Marrom Água Fria Soldável DN 32 |

**Tratamento na extração:** consolidar 4 sheets em 1 aba `EXTRACAO`, preservando `Tipo de Sistema (Revit)` e `Sheet origem` em colunas próprias. Normalizar descrição (remover prefixo `"Tipos de tubos:"` etc).

---

## 4. SAN Sanitária — R00 (executivo)

**Estado:** ✅ items extraíveis. **Não tem coluna Sistema** (diferente do HID), então subcategoria foi inferida do nome da família.

### Subcategorias inferidas

| Itens | Subcategoria | Inferido a partir de |
|---:|---|---|
| 55 | Esgoto | "Esgoto" / "Série Normal" no nome |
| 20 | Materiais/Equipamentos | sheet `Quant de material hidráulico` |
| 11 | Conexões | sheet `Quant de conexão de tubo` sem palavra "Esgoto"/"Marrom" |
|  3 | Água Fria | "Marrom" / "Água Fria" no nome |

### Distribuição por sheet

| Itens | Sheet |
|---:|---|
| 60 | Quant de conexão de tubo |
| 20 | Quant de material hidráulico |
|  9 | Quant de tubos |

### Top 5 por quantidade

|  Qtd  | Un | Subcat | Descrição |
|---:|---|---|---|
| 1928 | un | Esgoto | Luva Simples 50 mm Esgoto Série Normal Tigre |
| 1863 | m | Esgoto | Tubo Esgoto Série Normal DN 100 |
| 1360 | un | Esgoto | Luva Simples 100 mm Esgoto Série Normal Tigre |
| 1129 | m | Esgoto | Tubo Esgoto Série Normal DN 75 |
|  968 | un | Esgoto | Luva Simples 75 mm Esgoto Série Normal Tigre |

### Alerta — sobreposição com HID

3 itens SAN são "Tubo Marrom - Água Fria" (mesmo SKU que aparece em HID com sistema BE HS HID AF). Itens são preservados em ambos os arquivos com `Observação` apontando — Pati decide consolidação no executivo.

---

## 5. TEL Telecom — **EP R00** (estudo preliminar)

**Estado:** ✅ enxuto e sem duplicações. 1 sheet `CABEAMENTO`, mesmo formato da ELE (Descrição/Un/Qtd com cabeçalhos de categoria).

### Categorias (11)

| Itens | Categoria |
|---:|---|
|  9 | Derivações de Eletrocalhas |
|  8 | Fixações Elétricas |
|  7 | Tomadas para Telefone e Antena de TV |
|  6 | Derivações de Eletrodutos |
|  6 | Quadros |
|  6 | Caixas de passagem, eletrodutos e eletrocalhas |
|  3 | Conduletes de PVC |
|  3 | Cabeamento |
|  2 | Caixas de Embutir |
|  1 | Derivações de Eletrodutos com Rosca BSP |
|  1 | Tomadas para Conduletes de PVC |

### Top 5 por quantidade

|  Qtd  | Un | Categoria | Descrição |
|---:|---|---|---|
| 4500 | m | Cabeamento | Cabo UTP 4 pares Cat6 |
| 3715 | m | Caixas/eletrodutos | Eletroduto corrugado Reforçado PVC laranja |
|  520 | m | Cabeamento | Cabo Coaxial RG06 |
|  499 | pç | Caixas de Embutir | Caixa de Luz 4''x2'' |
|  397 | m | Caixas/eletrodutos | Eletroduto corrugado (outro diâm.) |

---

## Mapeamento → EAP Cartesian

| Disciplina | N1 Macrogrupo | Subdisciplina (sugerida) |
|---|---|---|
| CLI | 08 Climatização, Exaustão e Pressurização | Climatização |
| ELE | 07 Inst. Elétricas, Hidráulicas, GLP e Preventivas | Elétrico |
| HID | 07 Inst. Elétricas, Hidráulicas, GLP e Preventivas | Hidráulico |
| SAN | 07 Inst. Elétricas, Hidráulicas, GLP e Preventivas | Sanitário |
| TEL | 07 Inst. Elétricas, Hidráulicas, GLP e Preventivas | Telecom |

Referência: `~/orcamentos/executivos/templates/EAP-BASE.md`.

---

## Estratégia de extração — `extracao_{disc}.xlsx`

### Colunas comuns (aba `EXTRACAO`)

1. `Macrogrupo` (07 ou 08, fixo por arquivo)
2. `Disciplina`
3. `Categoria fonte` (cabeçalho da seção da planilha)
4. `Subcategoria` (apenas HID/SAN: Sistema Revit ou subcat inferida)
5. `Código fonte` (preservado se CLI; sequencial pros outros)
6. `Descrição` (normalizada)
7. `Unidade`
8. `Quantidade`
9. `Pavimento` (`"Não Identificado"` em 100% das linhas)
10. `Sheet origem`
11. `Arquivo fonte`
12. `Revisão fonte`
13. `Observação` (duplicações tratadas, sistema vazio, sobreposição com outra disciplina)

### Cores de cabeçalho (regra extracao colorida Cartesian)

| Disc | Cor (Excel) | Hex |
|---|---|---|
| CLI | laranja claro | `FFE0B2` |
| ELE | amarelo claro | `FFF59D` |
| HID | azul claro | `BBDEFB` |
| SAN | verde claro | `C8E6C9` |
| TEL | roxo claro | `D1C4E9` |

### Aba `RESUMO` (cada arquivo)

- Subtotal por `Categoria fonte` (e por `Subcategoria` quando HID/SAN)
- Linha "Total de itens"
- Linha "Total de unidades distintas" (depois de dedupe ELE)
- Notas: revisão, data fonte, alertas

### Saídas

```
chiquetti-bela-vida-claude/
├── ANALISE-LISTA-QUANTIDADES.md           ← este arquivo
├── extracao/
│   ├── extracao_cli_climatizacao.xlsx     ← 96 itens (92 + 4 dutos), 14 cat
│   ├── extracao_ele_eletrica.xlsx         ← 181 itens (dedupe 183→181), 24 cat
│   ├── extracao_hid_hidraulica.xlsx       ← 125 itens, 5 sistemas Revit
│   ├── extracao_san_sanitaria.xlsx        ← 89 itens, 4 subcat
│   └── extracao_tel_telecom.xlsx          ← 52 itens, 11 cat
└── scripts/
    └── extrair_qto_belavida.py            ← regenera os 5 .xlsx
```

---

## Alertas / decisões pendentes

1. **Revisões assimétricas** — ELE e TEL ainda são **EP R00** (estudo preliminar). Os 235 itens dessas 2 disciplinas vão evoluir. A revisão fica registrada na coluna `Revisão fonte` de cada item.
2. **HID com 11 itens "Não definido"** — verificar com Pati se são Águas Pluviais ou erro de mapeamento Revit. Preservados com `Observação = "Sistema Revit vazio na fonte"`.
3. **SAN sem coluna Sistema** — inferência heurística pelo nome da família. Pati pode ajustar manualmente.
4. **Sobreposição HID×SAN** — 3 SKUs (Tubo Marrom AF) aparecem nos dois. Preservados com `Observação`.
5. **CLI custos zerados** — coluna `Custo Total` e `Custo unit.` ignoradas; só quantitativo.
6. ~~**CLI item órfão (1)**~~ — resolvido. Era a linha 9 do CLI (cabeçalho "Item/Especificação/Unid.") sendo capturada como item; ajustado no script (filtro `r_idx <= 9`).
7. **Pavimento** — todos `"Não Identificado"`. Próxima rodada: cruzar com IFC `CDV_BLV_PCI_EX_000_GER_MODELO_R04.ifc` e/ou pranchas pra distribuir.

---

*Análise gerada em 2026-05-12 — Fase 1 do plano de extração.*

---

## Resumo da execução (Fase 2 — extração)

Script `scripts/extrair_qto_belavida.py` rodado em 2026-05-12. Os 5 arquivos foram gerados em `extracao/`.

### Contagens finais

| Arquivo | Itens | Notas |
|---|---:|---|
| `extracao_cli_climatizacao.xlsx` | 96 | 92 main + 4 dutos churrasqueira |
| `extracao_ele_eletrica.xlsx` | 181 | dedupe somou 2 grupos (4 linhas → 2) |
| `extracao_hid_hidraulica.xlsx` | 125 | preserva sistema Revit AF/AQ/AA/Não definido |
| `extracao_san_sanitaria.xlsx` | 89 | subcategoria inferida do nome da família |
| `extracao_tel_telecom.xlsx` | 52 | sem dedupe necessário |
| **TOTAL** | **543** | |

### Verificação rápida (passou)

- ✅ Todos os 5 arquivos têm 2 abas: `EXTRACAO` + `RESUMO`
- ✅ Todos têm 13 colunas conforme estratégia (Macrogrupo … Observação)
- ✅ `Pavimento` = `"Nao Identificado"` em 100% das linhas
- ✅ Cores de cabeçalho aplicadas por disciplina (CLI laranja, ELE amarelo, HID azul, SAN verde, TEL roxo)
- ✅ Header freeze pane ativo (linha 1 fixa)
- ✅ Aba `RESUMO` com totais por categoria fonte + subcategoria (quando aplicável) + alertas agrupados por mensagem
- ✅ CLI: bug de captura do header de coluna (linha 9) corrigido — passou de 97 → 96 itens reais
- ✅ ELE: 2 grupos de duplicação consolidados (183 → 181) com `Observacao` marcando

### Como reprocessar

```powershell
cd ~/orcamentos/executivos/chiquetti-bela-vida-claude
python scripts/extrair_qto_belavida.py           # regenera os 5 .xlsx
python scripts/extrair_qto_belavida.py --check   # dry-run só com contagens
```

---

*Atualizado em 2026-05-12 com resumo da execução da Fase 2.*
