# Memorial — EPCs (Equipamentos de Proteção Coletiva)

> Regras de extração dos quantitativos da aba **EPCs** + origem de cada número.
> Serve de referência pra Claude seguir o mesmo padrão em próximas obras.

## Escopo

Esta aba cobre os EPCs de **obra vertical** (torre residencial/comercial):

- **Bandejas de proteção** (primária e secundária)
- **Guarda-corpo de vãos** (fachada/sacadas)
- **Guarda-corpo de desforma** (proteção periférica pós-desforma de torre)
- **Fechamento removível de vãos em madeira** (portas de elevadores — carro e social)
- **Tela fachadeira**
- **SLQA** (Sistema Limitador de Quedas em Altura)
- **Tapume** (fechamento perimetral do canteiro)
- **Linha de Vida**

**Não cobre** (fica em outras disciplinas):
- EPIs individuais (pertence a "Canteiro" / encargos)
- Sinalização provisória (pertence a "Canteiro")
- Proteções fixas estruturais (ex.: guarda-corpo definitivo — vai em "Serralheria" se houver)

---

## Fontes de dados

| Fonte | Onde está | O que fornece |
|---|---|---|
| **CAPA!B18:G35** | aba CAPA (hidden) | Lista de pavimentos da Torre 1: nº, nome, área, área privativa, perímetro, pé-direito |
| **CAPA!C2:C4** | aba CAPA (hidden) | Cabeçalho (Obra, Empresa, Revisão) |
| **Tabela expandida EPCs!K5:N48** | mesma aba | Pavimentos *expandidos por repetição* (tipo 7º-14° ocupa 8 linhas, tipo 15º-35° ocupa 21 linhas, etc.) — serve de vetor pra SUMPRODUCT e COUNTA |
| **CPU!I4116** | aba CPU (hidden) | Comprimento de vãos de sacadas (valor importado de composição "Guarda Corpo de Vidro e Alumínio") — **ATUALMENTE RETORNA `#REF!`** (ver Pendências) |
| **Ger_Executivo_Cartesian / Ger_Tec e Adm** | hidden | WBS do orçamento — referenciada em outras disciplinas, não diretamente em EPCs |

**Projeto (fonte primária a cruzar):**
- Arquitetônico + Estrutural da Torre 1 (`~/orcamentos/projetos/thozen-electra/`)
- Memorial descritivo (dimensões de lote, pé-direito por pavimento, repetições de tipo)

---

## Estrutura interna da aba

### Tabela auxiliar — pavimentos expandidos (`K5:N48`)

Linhas 5 a 48 **replicam CAPA!B19:G35** com expansão de repetições. Cada coluna:

| Coluna | Conteúdo | Fonte |
|---|---|---|
| K | `"Torre X - nome do pavimento"` | Concat de `CAPA!Bn & " - " & CAPA!Cn` (ou só `CAPA!Cn` quando a Torre é implícita) |
| L | Área (m²) | `CAPA!Dn` |
| M | Perímetro (m) | `CAPA!Fn` |
| N | Pé-direito (m) | `CAPA!Gn` |

**Expansão de ranges:**
- `CAPA!C28` = "ÁREA – 7º AO 14° PAVIMENTO TIPO - X8" → aparece em **K14:K21** (8× linhas idênticas)
- `CAPA!C29` = "15º AO 35° PAVIMENTO TIPO - X21" → aparece em **K22:K42** (21× linhas)
- Demais pavimentos (térreo, mezaninos, lazer, duplexes, casa de máquinas, barrilete, reservatório) ocupam 1 linha cada

Essa tabela expandida é o **vetor base** pra somas ponderadas (área × pé-direito) e contagens (COUNTA).

---

## Itens — regras de extração

### Bloco 1 — Bandejas de proteção (B5:D13)

Proteção contra queda de materiais nos perímetros primário e secundário do prédio, durante execução.

#### D8 — Perímetro de projeção embasamento Primária (m)
- **Fórmula:** `=M6`
- **Regra:** copia o perímetro do **Mezanino do 1º Pavto** (`CAPA!F20 = 151.72 m`)
- **Origem:** `CAPA!F20` (via tabela K:N — linha 6 da expandida = Mezanino 1º)
- **Obs:** no template a nomenclatura diz "embasamento" mas puxa do Mezanino 1º. Revisar se essa é a intenção ou se deveria ser `M5` (1º Pavto/Térreo).

#### D9 — Perímetro de projeção embasamento Secundária (m)
- **Fórmula:** `=M9+M12`
- **Regra:** soma perímetro do **3º Pavto** (M9) + perímetro do **5º Pavto Lazer** (M12)
- **Origem:** `CAPA!F23 + CAPA!F26` = 151.72 + 151.72 = **303.44 m**

#### D10 — Perímetro de projeção tipo 1 Primária (m)
- **Fórmula:** `=M13`
- **Regra:** copia perímetro do **6º Pavto Tipo Diferenciado** (primeira torre-tipo)
- **Origem:** `CAPA!F27 = 108.2 m`

#### D11 — Perímetro de projeção tipo 1 Secundária (m)
- **Fórmula:** `=M14*(30/3)`
- **Regra:** perímetro do 7º-14° tipo (M14 = 108.2) **vezes 10** (constante `30/3`)
- **Resultado:** 108.2 × 10 = **1082 m**
- **Obs:** o fator 30/3 parece representar expansão das repetições de tipo (30 pavimentos tipo com 3 reutilizações de bandeja). Revisar se ainda é válido pra Electra — no original era pra outra obra (Elizabeth II Royal Home).

#### D12 — Bandeja de proteção primária (m) — **ENTREGÁVEL**
- **Fórmula:** `=D8+D10`
- **Regra:** soma dos perímetros primários (embasamento + tipo) = **259.92 m**

#### D13 — Bandeja de proteção secundária (m) — **ENTREGÁVEL**
- **Fórmula:** `=D11+D9`
- **Regra:** soma dos perímetros secundários (tipo + embasamento) = 1082 + 303.44 = **1385.44 m**

---

### Bloco 2 — Guarda-corpo de vãos (B14:D19)

Proteção provisória de vãos de fachada/sacadas durante execução.

#### D17 — Perímetro de vãos (m)
- **Fórmula:** `=M19`
- **Regra:** copia perímetro do 7º-14° tipo (M19 = 108.2 m, 5ª linha expandida do range "7º AO 14°")
- **Origem:** `CAPA!F28 = 108.2`

#### D18 — Comprimento de vãos sacadas (m)
- **Fórmula:** `=CPU!I4116`
- **Regra:** referência cruzada pra aba CPU, linha 4116 coluna I — "Guarda Corpo de Vidro e Alumínio - fornecimento e instalação"
- **⚠ Status atual: `#REF!`** — a fórmula em `CPU!I4116` está quebrada no template. Precisa ser corrigida ou substituída por valor direto.

#### D19 — Guarda-corpo de vãos (m) — **ENTREGÁVEL**
- **Fórmula:** `=D17+D18`
- **Regra:** soma perímetro dos vãos + comprimento sacadas
- **Depende de D18** — hoje retorna erro por causa do `#REF!`

---

### Bloco 3 — Guarda-corpo de desforma (B21:D26)

Proteção periférica instalada logo após desforma de laje — impede queda enquanto a alvenaria/fechamento definitivo não chega.

#### D24 — Perímetro de projeção da torre (m)
- **Fórmula:** `=M20`
- **Regra:** copia perímetro da linha 20 (`7º AO 14°`, 6ª linha expandida) = 108.2 m

#### D25 — Repetições de pavimentos ** (un)
- **Fórmula:** `=COUNTA(K6:K48)`
- **Regra:** conta linhas não vazias de K6 a K48 na tabela expandida = **43 pavimentos** (Torre 1 inteira, com tipos expandidos)

#### D26 — Proteção de periferia pós desforma torre (m) — **ENTREGÁVEL**
- **Fórmula:** `=D24*D25`
- **Regra:** perímetro × total de repetições = 108.2 × 43 = **4652.6 m lineares** acumulados de guarda-corpo por repetição

---

### Bloco 4 — Fechamento removível de vãos em madeira (B28:D40)

Tapume provisório dos vãos de elevadores (portas + caixa) durante execução, removível pra montagem do elevador.

#### Sub-bloco 4a — Elevador "De Carro" (B31:D35)

- **D31 — Área das portas (m²):** `=2.5*2.4` = **6 m²** — dimensões fixas da porta (2.5 m largura × 2.4 m altura)
- **D32 — Área do piso do elevador (m²):** `=33.7+27.4` = **61.1 m²** — soma de duas áreas medidas (provavelmente piso de cabine + antecâmara)
- **D33 — Quantidade de elevadores (un):** `2` (constante)
- **D34 — Quantidade de pavimentos com elevadores (un):** `7` (constante)
- **D35 — Fechamento (m²) — ENTREGÁVEL:** `=D31*D34*D33+D32*D34`
  - = 6 × 7 × 2 + 61.1 × 7 = 84 + 427.7 = **511.7 m²**
  - *Portas (área × pavimentos × elevadores) + Piso (área × pavimentos)*

#### Sub-bloco 4b — Elevador social (B36:D40)

- **D36 — Área das portas (m²):** `=2.1*1.2` = **2.52 m²** (2.1 m × 1.2 m)
- **D37 — Área do piso (m²):** `=3.78+3.83*2` = 3.78 + 7.66 = **11.44 m²**
- **D38 — Quantidade de elevadores (un):** `3` (constante)
- **D39 — Quantidade de pavimentos com elevadores (un):** `=COUNTA(K6:K45)` — conta pavimentos na tabela expandida até a linha 45 (40 pavimentos, excluindo os 3 últimos do topo)
- **D40 — Fechamento (m²) — ENTREGÁVEL:** `=D36*D39*D38+D37*D39`
  - Estrutura idêntica ao 4a: portas × pavimentos × elevadores + piso × pavimentos

---

### Bloco 5 — Tela fachadeira (B42:D46)

Tela de proteção instalada no perímetro da torre em todo o pé-direito durante execução.

#### D45 — Área da fachada (m²)
- **Fórmula:** `=SUMPRODUCT($M$5:$M$48, $N$5:$N$48)`
- **Regra:** soma ponderada **perímetro × pé-direito** de cada pavimento da tabela expandida. Resulta na área lateral total da torre (incluindo todas as repetições de tipo).
- **Origem:** efetivamente `Σ (CAPA!Fn × CAPA!Gn)` pra todos os pavimentos, com tipos já multiplicados pela repetição

#### D46 — Tela fachadeira (m²) — **ENTREGÁVEL**
- **Fórmula:** `=D45` (rótulo: `=A42` = "Tela fachadeira")
- **Regra:** mesma área da fachada — 1:1 com o bloco 5

---

### Bloco 6 — SLQA (Sistema Limitador de Quedas em Altura) (B48:D53)

Sistema de linha de vida/guarda específico pra trabalho em altura em planos inclinados (cobertura, telhado).

#### D51 — Perímetro de projeção da torre 1 (m)
- **Fórmula:** `=M25*1+M10*30`
- **Regra:** perímetro da linha 25 da expandida (15°-35° tipo, = 108.2) × 1 + perímetro da linha 10 (3º Pavto Mezanino, = 151.72) × 30
- **Resultado:** 108.2 + 4551.6 = **4659.8 m**
- **Obs:** o fator × 30 representa as 30 repetições do tipo padrão. Revisar se aplicável à Electra.

#### D52 — Altura de cobrimento da tela (un)
- **Valor constante:** `1`
- **Obs:** unidade é "un" mas o rótulo fala de "altura". Provavelmente é fator de 1 (sem modificação). Revisar.

#### D53 — SLQA (m) — **ENTREGÁVEL**
- **Fórmula:** `=D51*D52`
- **Regra:** perímetro × fator = 4659.8 × 1 = **4659.8 m**

---

### Bloco 7 — Tapume (B56:D61)

Fechamento perimetral do canteiro de obras (H=2.40 m padrão NR-18).

#### D59 — Perímetro de encontro com pavimentação (m)
- **Fórmula:** `=(65+15)*2`
- **Regra:** perímetro do lote = 2 × (lado maior + lado menor) = 2 × (65+15) = **160 m**
- **Origem:** dimensões do terreno (conferir com levantamento topográfico da Electra — no template eram dimensões do lote Elizabeth II)

#### D60 — Altura do tapume (m)
- **Valor constante:** `2.4` (padrão NR-18)

#### D61 — Tapume (m²) — **ENTREGÁVEL**
- **Fórmula:** `=D60*D59`
- **Regra:** altura × perímetro = 2.4 × 160 = **384 m²**

---

### Bloco 8 — Linha de Vida (B63:D67)

Linha de vida aérea instalada em cada pavimento da torre pra ancoragem de trabalhadores.

#### D66 — Perímetro de pavimentos (m)
- **Fórmula:** `=D26`
- **Regra:** reusa o valor calculado no Bloco 3 (perímetro × repetições) = **4652.6 m**

#### D67 — Linha de Vida (m) — **ENTREGÁVEL**
- **Fórmula:** `=D66` (rótulo: `=A63` = "Linha de Vida")
- **Regra:** = D66 = 4652.6 m

---

## Resumo dos entregáveis (o que vai pro orçamento)

| Bloco | Item | Unidade | Célula | Depende de |
|---|---|---|---|---|
| Bandejas | Bandeja primária | m | D12 | D8, D10 → CAPA!F20, F27 |
| Bandejas | Bandeja secundária | m | D13 | D9, D11 → CAPA!F23, F26, F28 |
| Guarda-corpo vãos | Guarda-corpo de vãos | m | D19 | D17, **CPU!I4116 (#REF!)** |
| Desforma | Proteção periferia pós desforma | m | D26 | D24, D25 (COUNTA K6:K48) |
| Fechamento | Fech. madeira elevador de carro | m² | D35 | dimensões + 2 elev × 7 pavtos |
| Fechamento | Fech. madeira elevador social | m² | D40 | dimensões + 3 elev × COUNTA(K6:K45) |
| Tela fachadeira | Tela fachadeira | m² | D46 | SUMPRODUCT(M×N) da tabela K:N |
| SLQA | SLQA | m | D53 | M25 + M10×30 |
| Tapume | Tapume | m² | D61 | (65+15)×2 × 2.4 |
| Linha de Vida | Linha de Vida | m | D67 | = D26 |

---

## Workflow de preenchimento (próxima obra)

1. **Atualizar CAPA!B18:G35** com os pavimentos da nova obra (Torre, nome, área, área privativa, perímetro, pé-direito)
2. **Regenerar tabela expandida K5:N48** seguindo o padrão: 1 linha por pavimento único, repetir N vezes pra pavimentos-tipo
3. **Conferir fatores hard-coded** que vieram da Electra/Elizabeth II e ajustar:
   - `D11 = M14*(30/3)` → fator 10 de expansão de tipo
   - `D51 = M25*1 + M10*30` → fator 30 de repetição
   - `D31, D32` → dimensões do elevador de carro (2.5×2.4 e 33.7+27.4)
   - `D36, D37` → dimensões do elevador social (2.1×1.2 e 3.78+3.83×2)
   - `D33, D34, D38` → qtd elevadores e pavimentos com elevador
   - `D59 = (65+15)*2` → dimensões do lote
   - `D52 = 1` → altura/fator SLQA (revisar o que representa)
4. **Resolver CPU!I4116** antes de confiar em D18/D19

---

## Pendências / decisões em aberto

- [ ] **CPU!I4116 retorna `#REF!`** — fórmula quebrada no template. Precisa:
  - (a) substituir por valor direto (comprimento medido no projeto de sacadas da Electra), OU
  - (b) consertar a composição CPU de "Guarda Corpo de Vidro e Alumínio" pra ela referenciar a célula correta
- [ ] Validar **D8** puxa do Mezanino 1º (M6) e não do 1º Pavto (M5) — confirmar com equipe se é intencional
- [ ] Revisar **constantes da Electra**: hoje os valores são os da obra Elizabeth II Royal Home. Substituir:
  - Lote: (65+15)×2 → dimensões reais da Electra
  - Elevadores: capacidade, dimensões de cabine, nº pavimentos
  - Fatores de repetição (×30, ×10)
- [ ] **D52 = 1** (constante "altura de cobrimento") — entender se é placeholder ou já é o valor final
- [ ] **D25 vs D39** usam ranges diferentes (K6:K48 vs K6:K45) — confirmar se é intencional ou erro
- [ ] Cruzar com **memorial descritivo** da Electra pra confirmar dimensões e repetições dos pavimentos-tipo
- [ ] Definir se "Bandeja primária/secundária" mapeia 1:1 com os perímetros extraídos ou se precisa de fator multiplicador adicional (ex.: reutilização da bandeja ao longo da obra)
