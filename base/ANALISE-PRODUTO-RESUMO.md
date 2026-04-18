# Análise de Produto Cartesian — Resumo Executivo

**Gerado em:** 2026-04-17
**Base:** 126 projetos executivos entregues
**Indicadores extraídos:** 49
**Método:** classificador local keyword-based + indices-executivo (estruturais validados)

---

## O que a base nos diz

### 1. Padrões construtivos são bem diferentes do que se imagina

A mediana de **concreto/m² AC** varia pouco entre `alto` (0.333) e `médio-alto` (0.361) — diferença de ~8% na mediana. **Sugere** que, em alto e médio-alto (os padrões com amostra robusta, n=35 e n=26), a estrutura tem comportamento próximo ao comoditizado. **Ressalva (qwen):** isso não significa que "padrão é só acabamento" — apenas que a variação estrutural entre esses dois padrões é menor que a variação em indicadores de acabamento. Padrões extremos (econômico, alto-luxo) podem ter estrutura muito diferente, mas amostra insuficiente pra testar.

**Ratio medianas max/min entre padrões — top 10:**

| Indicador | Ratio | Leitura |
|---|---:|---|
| Louças total/UR | 45× | Alto padrão tem ~5 louças/UR; médio só 0.17. |
| Revestimento fachada m²/m² AC | 33× | Variação enorme — depende de pele de vidro vs reboco+pintura. |
| Cubas/UR | 22× | Lavabo extra + cozinha gourmet vira cuba a mais. |
| Tomadas/UR | 12× | Alto padrão tem 35/UR; médio apenas 3/UR. |
| Chuveiros/UR | 11× | Alto padrão tem 1 chuveiro/UR; médio-alto só 0.1. |
| Lavatórios/UR | 11× | |
| Ralos/caixas sifonadas/UR | 8× | Inversamente: médio padrão registrou 55/UR (acho que overcount) |
| Eletroduto m/m² AC | 6× | Infra elétrica aumenta com padrão. |
| Drywall divisória m²/m² AC | 6× | Alto usa mais drywall (layouts flexíveis). |
| Vidros m²/m² AC | 5× | Pele de vidro é marcador de alto padrão. |

**Implicação comercial:** quando prospectar padrão alto, enfatizar expertise em **acabamento/instalação** (louças, tomadas, drywall, fachada envidraçada), não estrutura.

### 2. Indicadores estruturais têm benchmarks estáveis

| Indicador | Alto | Médio-alto | Esperado SBC |
|---|---:|---:|---|
| Concreto m³/m² AC | 0.33 | 0.36 | 0.25–0.45 |
| Aço kg/m² AC | 25.6 | 24.8 | 15–30 |
| Taxa aço kg/m³ | 77.6 | 67.0 | 60–100 |
| Alvenaria m²/m² AC | 1.49 | 1.33 | 1.2–2.0 |
| Porcelanato m²/m² AC | 1.03 | 1.07 | 0.8–1.5 |
| Pintura interna m²/m² AC | 4.76 | 4.61 | 4–7 |
| Rodapé m/m² AC | 0.54 | 0.58 | 0.4–0.8 |

Todos dentro do esperado SBC. **Dá pra usar esses valores como sanity check em orçamento novo** — se paramétrico/executivo sai fora dessa faixa, tem algo errado.

### 3. Correlações fortes que confirmam a estrutura do orçamento

```
alvenaria   ~ porcelanato     r=1.00  (onde tem parede, tem piso — trivial mas valida extração)
pintura_int ~ porcelanato     r=0.98  (áreas acabadas crescem juntas)
fachada_ext ~ pintura_externa r=0.83  (fachada pintada = mais pintura externa, óbvio)
contrapiso  ~ manta_asfalt    r=0.67  (impermeabilização pede contrapiso)
contrapiso  ~ chapisco        r=0.61  (mesma grandeza física)
```

Use essas correlações pra **validar consistência**: se um projeto mostra muito contrapiso mas pouca manta, revisar.

### 4. Curva ABC: onde tá a grana

Top 3 custos agregados cross-projeto (alguns MGs):

- **Supraestrutura**: Armadura (R$ 14.4M em 6 projetos) > Concreto (R$ 11M) > MO (R$ 6.1M)
- **Infraestrutura**: Armação (R$ 3.3M em 8 projetos) > MO (R$ 3M) > Concreto (R$ 2M)
- **Fachada**: Pele de vidro - área (R$ 20M em 2 projetos) — isso é outlier de projetos com fachada envidraçada total
- **Alvenaria**: Blocos cerâmicos furados (R$ 1.38M em 46 projetos — é o item mais universal)
- **Impermeabilização**: Manta asfáltica (aparece em 28 projetos) é quase 100% do MG

**Padrão:** na parte "pesada" (infra/supra) MO e material dividem relevância em peso igual; nas disciplinas finais (impermeabilização, alvenaria) o material domina.

### 5. Outliers destacados

**10 projetos com mais desvios vs mediana do próprio padrão:**

| Projeto | Padrão | Flags |
|---|---|---:|
| santo-andre-belle-ville | médio-alto | 15 |
| adore-cacupe | alto | 13 |
| amalfi-tramonti | médio-alto | 11 |
| nova-empreendimentos-domus | médio-alto | 11 |
| pavcor | médio-alto | 10 |
| homeset-homeset | alto | 9 |
| etr-zion-meridian-tower | alto | 8 |
| hacasa-brisa-da-armacao | médio-alto | 8 |
| nova-empreendimentos-malta | alto | 8 |
| grupo-duo-colin | alto | 7 |

**santo-andre-belle-ville** tem 15 desvios vs mediana do médio-alto — **merece análise dedicada** (qwen apontou corretamente que a v1 não fazia diagnóstico profundo). Hipóteses a investigar:
- Classificação de padrão incorreta (pode ser alto ou econômico misclassificado)
- Escopo parcial (só algumas disciplinas orçadas, distorcendo indicadores físicos)
- Especificação não-convencional (uso de sistema construtivo diferente)
- Erro de extração (aba do orçamento mal lida pelo pipeline)
- Projeto de obra existente / retrofit (diferente de obra nova)
- **Ação:** abrir o orçamento original do santo-andre-belle-ville, comparar com espelho de médio-alto tradicional, classificar.

### 6. Indicadores descobertos novos (não estavam na calibração V2)

- **Carro elétrico**: 26 projetos já registram ponto de recarga. Mediana 1/vaga em alto e médio-alto.
- **Piscina (acessórios)**: 26 projetos com bocais/coadeira/gerador cloro.
- **Portão automação**: 20 projetos.
- **Piso vinílico**: 56 projetos — substituto comum de porcelanato em áreas privativas padrão médio-alto.
- **Estucamento** (teto/parede): 44 projetos — acabamento estrutural visível.
- **Ar condicionado**: 31 projetos com infraestrutura dedicada.
- **Contramarco**: 67 projetos (praticamente universal).
- **Rodapé**: 77 projetos — mediana 0.54 m/m² AC.

Esses entram no catálogo de indicadores pra próxima iteração do paramétrico.

---

## Próximas iterações sugeridas

1. **Validar `santo-andre-belle-ville`**: 15 desvios é muito. Ou classificação de padrão errada, ou escopo atípico.
2. **Refinar regra de louças**: bacias/UR=54 na agregação está alto — investigar se tá pegando parte de composição. Mas valor único por projeto está razoável.
3. **Adicionar janelas do aluminio_pu_m2** (já temos R$ 980/m² de referência). Útil pro paramétrico.
4. **Cross-check com indices_consumo existente**: meus indicadores estruturais casam com indices_executivo.indices_estruturais — validar via script.
5. **Aba "projeto individual"**: selecionar um projeto e ver benchmark completo dele (radar chart) — upgrade pro Excel.

---

## Arquivos desta entrega

- **Excel:** `base/analise-produto-cartesian.xlsx` (18 abas) + cópia em `~/orcamentos/parametricos/`
- **Dados JSON:** `base/indicadores-produto/{slug}.json` (126 arquivos)
- **Agregado:** `base/indicadores-produto-agregados.json`
- **Scripts:**
  - `scripts/extrair_indicadores_produto.py` (pipeline de extração)
  - `scripts/agregar_indicadores_produto.py` (agregador v2)
  - `scripts/gerar_planilha_analise_produto.py` (Excel v2)
- **Este resumo:** `base/ANALISE-PRODUTO-RESUMO.md`

---

## Limitações conhecidas

1. **Gemma4 local** não produziu narrativas em PT-BR (retornou vazio em PT, funciona em EN). Para insights qualitativos vamos precisar de outro modelo (Claude API, ou Gemma em inglês + tradução).
2. **42 projetos têm AC/UR incompletos** — cobertura de indicadores fica limitada nesses (economico: 4, insuficiente: 1 não geraram indicadores agregados).
3. **Correlação alvenaria ~ porcelanato = 1.00** é artefato: ambos usam mesma fonte (aba ARQUITETURA). Não é correlação causal, é mesma grandeza vista em duas colunas.
4. **Overcount residual** em bacias/lavatórios/cubas pode existir em projetos com múltiplas abas de louças+metais. Checar via amostra manual.
