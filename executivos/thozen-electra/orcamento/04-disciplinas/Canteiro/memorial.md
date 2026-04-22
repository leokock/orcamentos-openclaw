# Memorial — Canteiro

> Regras de extração dos quantitativos da aba **CANTEIRO** + origem de cada número.
> Serve de referência pra Claude seguir o mesmo padrão em próximas obras.

## Escopo

Esta aba cobre o **dimensionamento e custo do canteiro de obra**:

- **Mão-de-obra**: número de operários (calculado por produtividade), equipe administrativa (estimada)
- **EPIs e ferramentas**: alocação per capita
- **Barracão de obra** (refeitório, vestiário, almoxarifado, escritório, baias, sala do cliente)
- **Mobiliário de canteiro** (cadeiras, mesas, ar-condicionado, armário, escrivaninhas)
- **Equipamentos eletrônicos** (computadores, impressora, roteador)

**Não cobre** (vai em outras disciplinas):
- Tapume e fechamento perimetral (vai em **EPCs**)
- EPCs propriamente ditos: bandejas, guarda-corpo (vai em **EPCs**)
- Controle tecnológico de materiais (vai em **Controle tecnológico**)
- Equipamentos especiais (gerador, elevador) (vai em **Equipamentos especiais**)
- Insumos de consumo da obra (vai diluído nas composições das demais disciplinas)

**Natureza:** aba é majoritariamente **paramétrica** — calcula quantitativos a partir de:
- Área construída total (`CAPA!C10`)
- Prazo da obra em meses (`CAPA!C6`)
- Produtividade média da equipe (`Pm = h/m²`, constante 47-49)

---

## Fontes de dados

| Fonte | Onde está | O que fornece |
|---|---|---|
| **CAPA!C2-C4** | aba CAPA (hidden) | Cabeçalho (Obra, Empresa, Revisão) |
| **CAPA!C10** | aba CAPA (hidden) | Área construída total (m²) — driver do dimensionamento |
| **CAPA!C6** | aba CAPA (hidden) | Prazo da obra em meses |
| **Bloco auxiliar O3:T8** | mesma aba | Cálculo derivado: NF (número de funcionários), A.C/prazo, produtividade |
| **Bloco auxiliar O11:Q46** | mesma aba | Dimensionamento NR-18 do barracão (refeitório, lavatório, chuveiros, sanitários) por funcionário |

**Constantes paramétricas** (Cartesian R00):
- **Pm = 47-49 h/m²** — produtividade média da equipe (varia entre células — D9=47, T5=49 — divergência a investigar)
- **180** — divisor (provavelmente horas-mês de 1 funcionário: 22 dias × 8h ≈ 176h, arredondado pra 180)
- **EPI = R$ 750/funcionário**
- **Ferramentas = R$ 600/funcionário**
- **Equipe administrativa = 9 pessoas** (constante)

---

## Estrutura interna da aba

A aba tem **dois blocos paralelos**:

### Bloco principal (colunas A-G, linhas 1-41)
Quantitativos e custos das instalações.

### Bloco auxiliar lateral (colunas O-T, linhas 3-46)
Cálculos paramétricos NR-18 e dimensionamento de equipe (não vão pro orçamento direto, são "memória de cálculo").

---

## Itens — regras de extração

### Bloco 1 — Instalações de canteiro / dimensionamento (B7:E14)

#### D8 — Produtividade média (m²/mês)
- **Fórmula:** `=CAPA!C10/CAPA!C6`
- **Regra:** área construída ÷ prazo da obra em meses
- **Resultado Electra:** 37.893,89 / 48 = **789,46 m²/mês**
- **Origem:** indicador derivado pra justificar dimensionamento de equipe

#### D9 — Pm (Produtividade da equipe) (h/m²)
- **Valor constante:** `47`
- **Regra:** índice Cartesian (homem-hora por m² construído). **Divergência:** célula T5 (bloco auxiliar) usa `49` pro mesmo cálculo. Confirmar qual é o oficial e padronizar.

#### D10 — Número de funcionários (un) — **ENTREGÁVEL CHAVE**
- **Fórmula:** `=ROUNDUP((D9*CAPA!C10)/CAPA!C6/180,)`
- **Regra:** `(Pm × Área construída) ÷ Prazo ÷ 180h-mês` arredondado pra cima
- **Cálculo Electra:** ROUNDUP((47 × 37.893,89) ÷ 48 ÷ 180, 0) = **ROUNDUP(206,18) = 207 funcionários**
- **Origem:** dimensionamento paramétrico (não vem do projeto BIM)
- **Driver de quase tudo nessa aba** — alterar D10 cascateia em ferramentas, EPI, banheiros, refeitório, vestiário, escritório

#### D11 — Equipe administrativa (un)
- **Valor constante:** `9` (provavelmente padronizado: 1 engenheiro + 1 mestre + 1 estagiário + 1 técnico segurança + 4 administrativo + 1 cliente?)
- **Obs:** O bloco auxiliar lateral em P8 mostra `5` como "equipe administrativa" — divergência. Confirmar valor real

#### D12 — Ferramentas (R$)
- **Fórmula:** `=600*D10`
- **Regra:** R$ 600 por funcionário operário
- **Cálculo Electra:** 600 × 207 = **R$ 124.200**

#### D13 — EPI (R$)
- **Fórmula:** `=750*D10`
- **Regra:** R$ 750 por funcionário operário
- **Cálculo Electra:** 750 × 207 = **R$ 155.250**

#### D14 — Banheiro (un)
- **Fórmula:** `=ROUNDUP($D$10/20,0)`
- **Regra:** 1 banheiro a cada 20 funcionários (NR-18)
- **Cálculo Electra:** ROUNDUP(207/20) = **11 banheiros**

---

### Bloco 2 — Barracão de obra (B18:G27)

Dimensionamento e custo das instalações fixas do canteiro.

| Cell | Item | Unid | Fórmula Quant. (D) | Custo Unit. (E) | Critério |
|---|---|---|---|---|---|
| L19 | **Refeitório** | m² | `=ROUNDUP((D10+D11)*1,2)` | `=266.76*1.1` | 1 m²/funcionário (operário+admin) |
| L20 | **Vestiário/banheiro** | m² | `=ROUNDUP((D10+D11)*1.5,2)` | `=322.87*1.1` | 1,5 m²/func (vestiário) + lavatório/chuveiro NR-18 |
| L21 | **Almoxarifado** | m² | `=IF(CAPA!C10<20000, 100, 100+((CAPA!C10-20000)/1000)*5)` | `=272.88*1.1` | 100 m² base + 5 m² a cada 1.000 m² acima de 20.000 |
| L22 | **Escritório** | m² | `=ROUNDUP((D11)*8,2)` | `=274.01*1.1` | 8 m²/func administrativo |
| L23 | **Baias de material** | m² | `5` (constante) | `=115.48*1.1` | 5 m² por bloco de material |
| L24 | **Sala do cliente** | m² | `2` (constante) | `=E22+(200*10)/12+1200` | Container c/ mobiliário, decoração e EPIs |
| **L25** | **TOTAL** | R$ | — | — | `=SUM(F19:F24)` |

#### Cálculos Electra (com D10=207, D11=9, área=37.893,89 m²):
- **Refeitório:** ROUNDUP((207+9)×1, 2) = **216 m²** × R$ 293,44 = **R$ 63.382**
- **Vestiário:** ROUNDUP((207+9)×1,5, 2) = **324 m²** × R$ 355,16 = **R$ 115.072**
- **Almoxarifado:** 100 + ((37.894-20.000)/1.000)×5 = 100 + 89,47 = **189,47 m²** × R$ 300,17 = **R$ 56.873**
- **Escritório:** ROUNDUP(9×8, 2) = **72 m²** × R$ 301,41 = **R$ 21.702**
- **Baias:** 5 m² × R$ 127,03 = **R$ 635**
- **Sala cliente:** 2 m² × (R$ 301,41 + R$ 166,67 + R$ 1.200) = 2 × R$ 1.668 = **R$ 3.336**
- **TOTAL barracão:** ~**R$ 261.000**

#### Notas
- **L21 (Almoxarifado):** fórmula com IF — obra ≤ 20.000 m² fica em 100 m² fixo; acima escala linear
- **L24 (Sala do cliente):** `E24 = E22 + (200*10)/12 + 1200` é uma fórmula híbrida que pega custo do escritório + diluição de mobiliário/decoração (R$ 200×10 itens/12 meses) + R$ 1.200 fixo
- **B27** tem nota: "* Central de armazenamento entre pavimentos" — não está orçado, é só lembrete

---

### Bloco 3 — Mobiliário de canteiro (B30:F36)

Móveis para a equipe administrativa.

| Cell | Item | Unid | Quant. | Custo Unit. | Total |
|---|---|---|---|---|---|
| L31 | **Cadeira** | un | `=ROUNDUP(D11*1.5,)` | R$ 200 | `=D31*E31` |
| L32 | **Mesa** | un | 1 (constante) | R$ 850 | `=E32*D32` |
| L33 | **Ar-condicionado** | un | 1 (constante) | R$ 3.000 | `=E33*D33` |
| L34 | **Armário** | m | 4 (constante) | R$ 900 | `=E34*D34` |
| L35 | **Escrivaninha** | un | `=D11` | R$ 800 | `=E35*D35` |
| **L36** | **TOTAL** | R$ | — | — | `=F33+F34+F35+F32+F31` |

#### Cálculos Electra (com D11=9 admin):
- **Cadeira:** ROUNDUP(9×1,5) = **14 cadeiras** × R$ 200 = **R$ 2.800**
- **Mesa:** 1 × R$ 850 = **R$ 850**
- **Ar-condicionado:** 1 × R$ 3.000 = **R$ 3.000**
- **Armário:** 4 m × R$ 900 = **R$ 3.600**
- **Escrivaninha:** 9 × R$ 800 = **R$ 7.200**
- **TOTAL mobiliário:** **R$ 17.450**

---

### Bloco 4 — Equipamentos eletrônicos (B37:F41)

| Cell | Item | Unid | Quant. | Custo Unit. | Total |
|---|---|---|---|---|---|
| L38 | **Computador pessoal** | un | `=D11` | R$ 3.500 | `=D38*E38` |
| L39 | **Impressora** | un | 1 | R$ 900 | `=E39*D39` |
| L40 | **Roteador** | un | 2 | R$ 500 | `=E40*D40` |
| **L41** | **TOTAL** | R$ | — | — | `=+F38+F39+F40` |

#### Cálculos Electra (com D11=9 admin):
- **Computador:** 9 × R$ 3.500 = **R$ 31.500**
- **Impressora:** 1 × R$ 900 = **R$ 900**
- **Roteador:** 2 × R$ 500 = **R$ 1.000**
- **TOTAL eletrônicos:** **R$ 33.400**

---

## Bloco auxiliar lateral (O3:T46) — memória de cálculo NR-18

Esse bloco **não gera entregáveis** — é cálculo paramétrico de dimensionamento NR-18 que poderia substituir os valores constantes do bloco principal mas hoje é só referência.

### Sub-bloco — Dimensionamento de funcionários (O3:T8)
- **P4 — Área construída:** `=CAPA!C10` = 37.893,89
- **P5 — Prazo da obra:** `=CAPA!C6` = 48 meses
- **T4 — A.C/prazo:** `=P4/P5` = 789,46 m²/mês
- **T5 — Pm:** 49 h/m² (⚠ DIVERGE de D9=47)
- **P6 — NF (Nº funcionários):** `=ROUNDUP((P4*T5)/P5/180,)` = 215 (com Pm=49) ⚠ diverge de D10=207 (com Pm=47)
- **P7 — Pavimentos:** 10 (⚠ Electra tem 53 — desatualizado)
- **P8 — Equipe administrativa:** 5 (⚠ DIVERGE de D11=9)

### Sub-bloco — Barracão NR-18 (O11:Q14)
- **P11 — Barracão interno:** `=450+(P4-13000)/1000*16` = 450 + (37.894-13.000)/1.000 × 16 = **848 m²** (paramétrico baseado em escala)
- **P12 — SUM(P11:P11):** = 848 m² (parece um TODO inacabado — soma só uma célula)

### Sub-bloco — Refeitório/lavatório (O14:Q17)
- **P14 — Área refeitório:** `1` m²/funcionário
- **P15 — Total refeitório:** `=P14*P6` = **215 m²** (NR-18 estrito)
- **P16 — Área lavatório:** `=0.6*ROUNDUP(P6/20,)` = 0,6 × ROUNDUP(215/20) = 0,6 × 11 = **6,6 m²**
- **P17 — Área de chuveiros:** `=0.8*ROUNDUP(P6/10,)` = 0,8 × ROUNDUP(215/10) = 0,8 × 22 = **17,6 m²**

### Sub-bloco — Vestiário/sanitários (O26:Q46)
- **P26 — área lavatório (P31?):** `=0.6*ROUNDUP(P31/20,)` — referencia P31 que está vazia (bug)
- **P29 — Área de vestiário:** `1.5` m²/funcionário
- **P30 — Total vestiário:** `=P29*P6` = 1,5 × 215 = **322,5 m²**
- **P41 — Área sanitários:** `=1*ROUNDUP(P6/20,)` = 11 m²
- **P45-P46 — Banheiro:** 1 a cada 20 pessoas → ROUNDUP(P6/R45,) = 11 banheiros

---

## Resumo dos entregáveis

| Bloco | Item | Cell | Cálculo Electra |
|---|---|---|---:|
| Pessoas | Nº funcionários (operários) | D10 | **207** |
| Pessoas | Equipe administrativa | D11 | 9 (constante) |
| Pessoas | Banheiros (NR-18) | D14 | 11 |
| Custos | Ferramentas | D12 | R$ 124.200 |
| Custos | EPI | D13 | R$ 155.250 |
| Custos | **Barracão TOTAL** | F25 | **R$ ~261.000** |
| Custos | **Mobiliário TOTAL** | F36 | **R$ 17.450** |
| Custos | **Eletrônicos TOTAL** | F41 | **R$ 33.400** |
| **TOTAL CANTEIRO** | | | **R$ ~591.300** |

---

## Workflow de preenchimento (próxima obra)

1. **Confirmar `CAPA!C10` (área construída)** e **`CAPA!C6` (prazo)** — drivers principais
2. **Validar Pm (Produtividade)**: 47 h/m² (D9) é o índice Cartesian R00. Verificar se obra precisa ajustar (ex.: obras complexas pedem 50-60 h/m²)
3. **Resolver divergências do bloco auxiliar lateral**:
   - D9=47 vs T5=49 (Pm) → padronizar
   - D11=9 vs P8=5 (equipe admin) → padronizar
   - P7=10 (pavimentos) → atualizar
4. **Revisar custos unitários** (E19-E24) → atualizar com CUB/SC mais recente. Hoje multiplica `×1,1` (10% acréscimo) — verificar se é margem do custo unitário ou outro fator
5. **Custo do container "Sala do cliente" (E24)**: fórmula derivada complexa — revisar se ainda faz sentido pra Electra
6. **Corrigir P12** (`=SUM(P11:P11)`) — provavelmente queria somar mais blocos do barracão

---

## Pendências / decisões em aberto

- [ ] **Padronizar Pm**: D9 usa 47 h/m², T5 usa 49 h/m². Qual é o oficial Cartesian R00?
- [ ] **Padronizar equipe administrativa**: D11=9 vs P8=5. Confirmar tamanho real da equipe Electra (provavelmente 9 inclui cliente, fiscal, etc.)
- [ ] **Atualizar P7 (pavimentos)**: hoje está 10 (template Elizabeth II). Electra tem 53 pavtos físicos
- [ ] **Bloco auxiliar lateral está inconsistente** com o principal (Pm/admin/pavimentos). Decidir se mantém como "memória de cálculo paralela" ou refatora pra ser usado pelo bloco principal
- [ ] **P12 (SUM(P11:P11))** — fórmula incompleta, provavelmente faltam termos do barracão completo
- [ ] **Custos unitários (E19-E24)**: validar se `× 1.1` é fator de mercado regional Itapema/Porto Belo (pode estar muito alto/baixo pra 2026)
- [ ] **"Central de armazenamento entre pavimentos" (B27)** — está listada como nota mas sem orçamento. Verificar se Electra precisa (relevante pra obra de 24 pavtos × 2 torres)
- [ ] **NR-18 oficial vs constantes do bloco principal**: D14 segue NR-18 (1 banheiro/20), mas refeitório/vestiário usam constantes (1 e 1,5 m²/func) que batem com NR-18 mas poderiam vir do bloco lateral. Refatorar pra usar P15, P30, P41 (que já calculam NR-18)
- [ ] **Cruzamento com EPCs**: confirmar que tapume e proteções estão SÓ em EPCs (não duplicar aqui)
