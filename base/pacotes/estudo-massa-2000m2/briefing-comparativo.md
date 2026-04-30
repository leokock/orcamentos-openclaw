# Briefing — Estudo de Massa 2.000 m² (Vertical × Horizontal)

> Estudo interno gerado por Leo em 30/04/2026 pra entender qual decisão de produto
> impacta mais no custo num multifamiliar pequeno: **verticalizar** ou **alongar**.

## Pergunta de negócio

Pra um terreno hipotético no interior SC (Brusque/Blumenau) com programa fechado de
**2.000 m² AC, 24 apartamentos de ~55 m² privativa, padrão médio, térreo pilotis**,
qual configuração de produto é mais econômica e *onde está o dinheiro*?

- **Cenário V (Vertical):** 3 aptos/pav × 8 pavs tipo + térreo = 9 pavs, torre esbelta
- **Cenário H (Horizontal):** 4 aptos/pav × 6 pavs tipo + térreo = 7 pavs, torre mais baixa

## Premissas comuns (idênticas nos 2 cenários)

| Categoria | Valor |
|---|---|
| AC total | 2.000 m² |
| UR | 24 aptos |
| Área privativa média | 55 m² |
| Padrão | Médio |
| Cidade | Brusque/SC (Norte SC) |
| CUB referência | R$ 2.870/m² (data-base abr/26, ajuste -5% vs Floripa) |
| Laje | Convencional |
| Fundação | Hélice contínua |
| Subsolos | 0 (térreo pilotis garagem) |
| Fachada | Textura + pintura |
| Vedação | Alvenaria |
| Esquadrias | Alumínio anodizado |
| Lazer | Básico (salão + churrasqueira) |
| Prazo | 18 meses |
| Pé-direito | 2.80m |
| Banheiros/apto | 1 |
| Piso | Porcelanato |
| Tipologia | 1-2 Dormitórios |
| 1 torre, sem gerador, sem subestação, sem fotovoltaica, sem pressurização, sem piscina | |

## Variáveis dos cenários (o que muda)

| Campo | Cenário V | Cenário H |
|---|---|---|
| Aptos/pav | 3 | 4 |
| Pavs tipo (NPT) | 8 | 6 |
| Pavs total (NP) | 9 | 7 |
| Footprint torre | ~235 m² | ~315 m² |
| Perímetro torre | ~62 m | ~71 m |
| Altura aprox. | ~26 m | ~20 m |
| Elevadores | 2 | 1 |
| Vagas modeladas no pilotis | 8 | 11 |
| Área terreno (estimada) | 600 m² | 800 m² |
| Área fachada total | ~1.395 m² | ~1.213 m² |
| Fachada/m² AC | 0.74 | 0.64 |
| Cobertura/m² AC | 0.13 | 0.17 |

## Disclaimer crítico — vagas

24 aptos × 1 vaga = 24 vagas. Em ambos os cenários, **o térreo pilotis único não comporta 24 vagas** (cabem ~8-11 dependendo do footprint). Em projeto real, isso exigiria:

- 1 subsolo (+R$ 200-400/m² no macro fundação/contenção/movimento de terra) **ou**
- pilotis duplo (térreo + 1° pavimento garagem, perde-se 1 pav residencial) **ou**
- aceitar < 1 vaga/apto (compactos populares, ~12 vagas)

Esse estudo **não dimensiona a garagem** — foco é isolar o efeito da geometria
(verticalização × horizontalização) sobre o custo. Antes de decidir produto real,
precisa definir solução de garagem porque o impacto é grande (R$ 250-500k em
projeto desse porte).

## Hipótese a confirmar

Macrogrupos onde **V perde** (vertical mais caro):
- Fachada/m² AC — torre esbelta tem mais perímetro:área (+10-15%)
- Elevadores — 2 vs 1 (+R$ 80-120k)
- Estrutura — pilares maiores no térreo, mais aço/m² (+5%)
- Canteiro — torre alta exige grua, andaimes mais altos (+3%)

Macrogrupos onde **H perde** (horizontal mais caro):
- Cobertura/m² AC — maior footprint = mais cobertura (+3-5%)
- Fundação — talvez (mais perímetro de estaca)

**Saldo esperado:** H sai 5-10% mais barato em valor absoluto (~R$ 250-500k em
projeto de R$ 6-7M). Mas o aprendizado real é qual macrogrupo domina o delta.

## Overrides manuais aplicados na aba INDICES

Os 3 índices abaixo são *geométricos* — o pipeline V2 default calcula em função
do AC, mas o efeito da geometria (perímetro, altura, footprint) precisa ser
forçado via Col C (Override manual) na aba INDICES de cada xlsx:

| Índice | Vertical | Horizontal | Justificativa |
|---|---|---|---|
| `area_fachada_por_m2_ac` | 0.74 | 0.64 | Calc geométrico: torre V tem 1.395 m² fachada / 1.880 m² AC tipo; torre H tem 1.213 m² / 1.890 m² AC tipo |
| `area_cobertura_por_m2_ac` | 0.13 | 0.17 | Cobertura = footprint do último pav. V: 235 m² / 1.880 = 0.125; H: 315 m² / 1.890 = 0.167 |
| `n_elevadores` | 2 | 1 | NBR 13994: ≥7 paradas exige 2 elevadores. V tem 9 pavs (9 paradas). H tem 7 pavs (7 paradas — limite, considerado 1 com tolerância de tráfego baixo p/ 24 aptos) |

## Pipeline

```bash
cd ~/orcamentos-openclaw

# Passo 1: gerar 2 xlsx
py -3.10 scripts/gerar_template_dinamico_v2.py \
  --config base/pacotes/estudo-massa-2000m2/parametrico-v2-config-vertical.json \
  -o base/pacotes/estudo-massa-2000m2/parametrico-estudo-massa-2000m2-vertical.xlsx

py -3.10 scripts/gerar_template_dinamico_v2.py \
  --config base/pacotes/estudo-massa-2000m2/parametrico-v2-config-horizontal.json \
  -o base/pacotes/estudo-massa-2000m2/parametrico-estudo-massa-2000m2-horizontal.xlsx

# Passo 2: aplicar overrides + comparar
py -3.10 scripts/comparar_cenarios_estudo_massa.py
```
