# Viabilidade Financeira — Arthen Arboris

**Cliente:** Arthen Engenharia e Construções
**Projeto:** Arthen Arboris — Porto Belo/SC, bairro Perequê
**Tipologia:** Multifamiliar residencial + comercial (3-4 dorm, 98 un.)
**Prazo de obra:** 30 meses
**Gerado em:** 2026-04-14
**Fonte custo:** Paramétrico V2 híbrido (`parametrico-arthen-arboris.xlsx`, `CUSTOS_MACROGRUPO!D22`)

---

## KPIs — Cenário Base

| Indicador | Valor |
|---|---:|
| Área construída | 12.472,98 m² |
| Área privativa (70%) | 8.731,09 m² |
| Unidades | 98 |
| VGV bruto (antes permuta) | R$ 134.406.338 |
| VGV líquido (pós permuta 30%) | R$ 94.084.437 |
| Custo de obra (paramétrico) | R$ 45.460.479 |
| Receita total (horizonte) | R$ 90.739.937 |
| Despesa total (horizonte) | R$ 62.765.489 |
| **Lucro líquido** | **R$ 27.974.448** |
| **Margem líquida** | **30,8%** |
| **VPL @ TMA 14%** | **R$ 16.200.600** |
| **TIR anual** | **68,6%** |
| Payback descontado | 32 meses (após início da obra) |
| Exposição máxima de capital | R$ 15.376.903 |
| ROI sobre capital exposto | 182% |

## Monte Carlo (10.000 iterações)

| Estatística | VPL | TIR anual |
|---|---:|---:|
| Mediana | R$ 16.923.632 | ~55% |
| P10 | R$ 5.650.657 | ~25% |
| P90 | R$ 29.959.488 | ~95% |
| **P(VPL > 0)** | **98,2%** | — |
| **P(TIR > TMA)** | **98,2%** | — |

Variáveis estocásticas: VGV R$/m² (triangular 11k–15,4k–22k), custo de obra (×0,90–1,00–1,15), t50 velocidade de venda (8–14–24 meses), CUB/SC (4–7–11%). Correlação ρ=-0,4 entre VGV e t50 (preço alto ↔ venda mais lenta). Seed 42, reprodutível.

## Cenários

| Indicador | Pessimista | Base | Otimista |
|---|---:|---:|---:|
| Perturbação | vgv×0,85 custo×1,10 t50+8m | base | vgv×1,10 custo×0,95 t50−4m |
| VPL @ TMA | **-R$ 608.251** | R$ 16,2M | R$ 25,5M |
| TIR anual | 12,5% | 68,6% | 131,4% |
| Margem | 9,8% | 30,8% | 38,9% |

O pessimista bate em VPL negativo — indica que o projeto é sensível a combinações adversas. O ponto de ruptura fica próximo de: queda de ~15% no VGV + 10% de custo adicional + 8 meses de atraso de vendas.

## Tornado — sensibilidade (±20% por variável)

| Variável | Δ VPL | Impacto |
|---|---:|---|
| VGV R$/m² | R$ 21,99M | Dominante |
| Custo obra | -R$ 15,51M | Segundo maior |
| Entrada % | R$ 5,74M | |
| TMA | -R$ 3,58M | |
| t50 vendas | -R$ 2,78M | |

Conclusão: ~75% do risco de VPL vem de preço de venda e custo de obra. Velocidade e entrada importam mas são secundárias.

---

## Premissas-chave (`premissas-viabilidade.json`)

- **VGV R$/m² privativo**: R$ 15.394 — mediana Perequê abr/2026 (range R$ 9.991–25.375). Fonte: Viva Real, MySide, Imovelweb, Perequê Imóveis.
- **% área privativa / AC**: 70% (parametrizável).
- **Permuta física**: 30% das unidades para landowner — **modelagem não-monetária**: o terreno não entra como saída de caixa no mês 0; a contrapartida é a redução do VGV vendável em 30%.
- **Estrutura de recebimento**: 20% entrada no ato + 40% parcelado durante a obra corrigido CUB/SC + 40% repasse bancário no mês da entrega +2.
- **Curva de vendas**: logística cumulativa com t50=14 (50% vendido no meio da obra), k=0,18, início em t=-2 (pré-lançamento de 3 meses). 95% sold em ~36 meses. Conservador dado que Porto Belo lidera velocidade nacional em 2025.
- **Curva de desembolso**: ponderada por macrogrupo do paramétrico. Cada macrogrupo distribui seu custo uniformemente em sua janela típica (Mov. Terra 1-3, Supraestrutura 3-18, Acabamentos 18-30, Gerenciamento 1-30 linear, etc.).
- **CUB/SC (indexador)**: 7% a.a. (média histórica 2020-2025). Aplicado às parcelas obra.
- **TMA (desconto)**: 14% a.a. = Selic ~10,5% + spread 3,5% (custo de capital incorporadora média SC).
- **Comercial/Impostos/Admin**:
  - Corretagem: 6% sobre VGV contratado (paga no mês da venda)
  - Marketing: 3% sobre VGV (40% front-loaded no pré-lançamento, 60% durante obra)
  - RET: 4% sobre receita recebida (Patrimônio de Afetação, Lei 10.931/04 art. 4º)
  - Admin incorporadora: 3% sobre VGV (linear pelo horizonte)
- **Inadimplência**: 3% sobre recebido.
- **Contingência**: 5% sobre custo de obra (distribuída junto à curva).

---

## Metodologia — VPL e TIR

- **Horizonte**: 46 meses (mês −3 a mês +42).
- **Fluxo de caixa mensal** em `FLUXO_CAIXA`: linhas de receita (entrada, parcelas CUB, repasse, inadimplência) e despesa (custo obra, contingência, corretagem, marketing, RET, admin). Cada valor é computado em Python (vetorizado numpy) e escrito como número na planilha.
- **Valor autoritativo**: Python (`numpy_financial.npv` e `irr`), escrito como valor na aba RESULTADO colunas B.
- **Fórmula Excel paralela** (auditoria): a aba RESULTADO mostra também a fórmula `=FLUXO_CAIXA!C24+NPV(tma_am,D24:AV24)` e `=IRR(C24:AV24)` — ao abrir no Excel devem bater com o valor Python dentro de ±0,01. Se divergirem é bug.
- **Conversão de TMA**: `tma_am = (1+tma_aa)^(1/12) - 1` (composição mensal equivalente), **não** `tma_aa / 12`.
- **Payback descontado**: primeiro mês em que o acumulado do fluxo descontado atinge zero.

---

## ⚠ Interpretação dos KPIs — importante

**A TIR base de 68,6% a.a. é alta para padrões de incorporação brasileira** (benchmark típico 25–40%). Vale explicar de onde ela vem neste modelo:

1. **Permuta física 30% (terreno R$ 0 monetário)** — o maior desembolso do início (terreno) está fora do fluxo. Se o cliente quiser modelar terreno monetário, basta setar `permuta_pct_unidades = 0` no JSON e adicionar o valor como saída no mês 0.
2. **Pré-lançamento com entrada 20%** — começa gerando caixa já no mês -2, antes do primeiro desembolso de obra, reduzindo a exposição máxima (R$ 15,4M) frente a um custo total de obra de R$ 45,5M.
3. **Exposição máx baixa** (16% do VGV líquido) infla o ROI sobre capital: lucro R$ 28M / R$ 15M expostos = 182%.

Em outras palavras: **o VPL (R$ 16,2M) é a métrica mais confiável pra decisão de viabilidade.** A TIR é matematicamente correta no modelo, mas interpretar como "retorno anual esperado" induz leitura otimista quando o capital exposto é pequeno frente ao VGV.

**Recomendações para reunião de viabilidade com Arthen:**
1. Apresentar VPL, margem líquida e P(VPL>0) Monte Carlo como KPIs principais.
2. Mostrar que o pessimista dá VPL negativo — o projeto é viável mas não invulnerável.
3. Se o terreno **não** for permuta (aquisição monetária real), regerar o modelo com `permuta_pct_unidades=0` e `terreno_R$` no mês 0 — a TIR vai cair para faixa mais realista.
4. Validar a curva de venda (logística k=0,18, t50=14) contra o histórico da Arthen em projetos similares.

---

## Riscos e trade-offs do modelo

1. **VPL Python vs fórmula Excel**: ambos escritos na aba RESULTADO (linhas 12-16). Abrir no Excel e verificar que os valores batem — se divergirem, há bug.
2. **S-curve logística é suave**: lançamentos reais têm saltos (feirão, campanhas). Não modelado aqui. Ajustável via `t_inicio`, `t50`, `k` no JSON.
3. **Permuta uniforme**: o modelo assume que a permuta de 30% é distribuída proporcionalmente. Se a Arthen separar unidades específicas (geralmente as de menor valor) para o landowner, o VGV remanescente sobe.
4. **Correlação VGV↔t50** (ρ=-0,4) é um palpite documentado. Sem correlação, o P90 do VPL no Monte Carlo pode inflar ~15%.
5. **Juros de financiamento à produção** **não** modelados explicitamente — assumido que o fluxo de vendas cobre o custo. Se a Arthen for captar SFH, adicionar linha específica.
6. **Inflação geral fora do CUB**: RET, admin e marketing estão em valores nominais presentes (não indexados). Para horizonte 45 meses, erro ~5-8%.
7. **Tributação além de RET**: não incluído PIS/COFINS adicional, IR sobre lucro, etc. RET 4% é regime unificado que cobre grande parte. Se for fora do Patrimônio de Afetação, recalcular.

---

## Arquivos

| Arquivo | Caminho | Função |
|---|---|---|
| **Planilha entregável** | `base/pacotes/arthen-arboris/viabilidade-arthen-arboris.xlsx` | Excel 7 abas (CAPA, PREMISSAS, FLUXO_CAIXA, RESULTADO, CENARIOS, TORNADO, MONTE_CARLO) |
| Script gerador | `openclaw/orcamento-parametrico/scripts/gerar_viabilidade_arthen_arboris.py` | Python, vetorizado, ~1000 linhas |
| Premissas versionadas | `base/pacotes/arthen-arboris/premissas-viabilidade.json` | Editar → regerar |
| Plots matplotlib | `base/pacotes/arthen-arboris/_viabilidade_plots/` | hist_vpl, hist_tir, tornado (PNGs embedded no xlsx) |
| Memorial (este arquivo) | `base/pacotes/arthen-arboris/viabilidade-arthen-arboris.md` | Metodologia, premissas, interpretação |

## Regeneração

```bash
cd ~/openclaw
python -X utf8 orcamento-parametrico/scripts/gerar_viabilidade_arthen_arboris.py
```

Após regerar, commit no git + sync pro Drive.
