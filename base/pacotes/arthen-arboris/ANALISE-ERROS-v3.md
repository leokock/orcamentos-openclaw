---
projeto: Arthen Arboris
versao: v3 Híbrido
data_analise: 2026-04-20 (r2)
autor: Coordenação de Custos Cartesian
fontes:
  - 8 projetos Cartesian comparáveis com breakdown por macrogrupo (AC 5–18k m², padrão Médio-Alto ou Alto, R$/m² 2.500–5.500)
  - calibration-condicional-padrao.json (60 MA + 57 Alto, estatística agregada)
  - base-indices-master-2026-04-13.json (índices derivados n=126)
  - CTN-ALF-SFL Orçamento Paramétrico (benchmark Amalfi indexado CUB Mar/26)
  - CSV bruto: `_dados-projetos-CONSOLIDADO.csv`
---

# Análise de Erros — Arboris Paramétrico v3 (r2 com obras nominais)

## 1. Contexto do orçamento

| Campo | Valor |
|-------|-------|
| AC | 12.472,98 m² |
| UR | 98 apartamentos |
| Pavimentos | 24 (19 tipo) |
| Padrão | Médio-Alto |
| Laje | Convencional maciça |
| Fachada | Cerâmica |
| Entrega | Completa |
| Prazo | 30 meses |
| **Total v3** | **R$ 45.460.479** |
| **R$/m² AC** | **R$ 3.645** |
| **CUB ratio** | **1,20 CUB** |

## 2. Amostra de comparação — 8 obras Cartesian

Critério: AC entre 5.000 e 18.000 m², padrão Médio-Alto ou Alto, R$/m² entre 2.500 e 5.500 (exclui atípicos), com breakdown por macrogrupo disponível.

| Obra | Padrão | AC (m²) | R$/m² (total) |
|---|:---:|---:|---:|
| pass-e-vancouver | Médio-Alto | 5.554 | R$ 2.758 |
| amalfi-maiori | Alto | 8.366 | R$ 3.010 |
| terrassa-amaro | Alto | 10.479 | R$ 3.100 |
| pass-e-celebration | Médio-Alto | 7.956 | R$ 3.148 |
| fonseca-empreendimentos-estoril | Médio-Alto | 14.492 | R$ 3.378 |
| pavcor | Médio-Alto | 14.283 | R$ 3.456 |
| pass-e-connect | Médio-Alto | 13.144 | R$ 3.710 |
| pass-e-passione | Alto | 6.682 | R$ 3.785 |
| **ARBORIS v3** | **Médio-Alto** | **12.473** | **R$ 3.645** |

> Obs: amalfi-marine (AC 4.499) e nova-empreendimentos-malta (AC 7.964) ficaram **fora** do filtro (Marine por AC, Malta por R$/m² R$ 6.091 que é alto padrão atípico). Constam no CSV completo para consulta.
>
> Valores R$/m² apresentados são **brutos** (data-base original de cada orçamento), **não indexados ao CUB Mar/2026**. Como são medianas e o range é grande, a distorção é secundária — mas na apresentação pro cliente, os valores da tabela de benchmark devem ser indexados antes de mostrar.

## 3. Tabela completa — R$/m² AC por macrogrupo

Ver `_tabela-comparativa.md` e `_dados-projetos-CONSOLIDADO.csv` para a matriz completa. Percentis da amostra de comparáveis (n varia por macrogrupo, valores em R$/m² AC):

| Macrogrupo | Arboris | Min | P25 | Mediana | P75 | Max | n | Posição Arboris |
|---|---:|---:|---:|---:|---:|---:|:---:|---|
| Gerenciamento | 372 | 288 | 397 | 532 | 580 | 682 | 8 | 🔴 abaixo do P25 |
| Mov. Terra | 32 | 7 | 12 | 20 | 31 | 40 | 7 | ⚠️ > P75 (2º maior) |
| Infraestrutura | 191 | 140 | 171 | 196 | 237 | 245 | 8 | ✅ mediana |
| Supraestrutura | 786 | 592 | 650 | 710 | 736 | 762 | 8 | 🔴 **acima do máximo** |
| Alvenaria | 182 | 114 | 155 | 168 | 197 | 241 | 8 | ✅ dentro P25-P75 |
| Instalações | 394 | 274 | 310 | 330 | 445 | 460 | 8 | ✅ mediana |
| Sist. Especiais | 102 | 96 | 111 | 204 | 241 | 255 | 7 | 🔴 abaixo do P25 |
| Climatização | 67 | 28 | 28 | 42 | 86 | 86 | 3 | ✅ mediana (n baixo) |
| Impermeabilização | 80 | 17 | 35 | 57 | 64 | 71 | 7 | 🔴 **acima do máximo** |
| Rev. Int. Parede | 128 | 48 | 196 | 238 | 496 | 496 | 4 | 🔴 abaixo do P25 (n baixo) |
| Teto | 73 | 38 | 47 | 61 | 88 | 92 | 8 | ⚠️ P75 |
| Pisos | 191 | 100 | 134 | 284 | 327 | 365 | 7 | ⚠️ abaixo P25 |
| Pintura | 155 | 102 | 137 | 145 | 178 | 197 | 8 | ✅ mediana |
| Esquadrias | 325 | 246 | 265 | 279 | 312 | 334 | 8 | ⚠️ P75 |
| **Louças e Metais** | **32** | **23** | **24** | **27** | **28** | **28** | **4** | ⚠️ **acima do máximo** |
| Fachada | 361 | 94 | 110 | 149 | 259 | 300 | 7 | 🔴 **acima do máximo** |
| Complementares | 122 | 52 | 104 | 145 | 197 | 197 | 8 | ✅ P25 |
| Imprevistos | 54 | 40 | 42 | 48 | 120 | 158 | 6 | ✅ mediana |

### Observação importante sobre **Louças e Metais**

Na primeira versão desta análise, concluí que Louças estava **subdimensionado** (Arboris R$ 32/m² vs mediana R$ 60 da calibração condicional agregada). **Isso estava errado.**

Cruzando com os **4 projetos executivos** que têm breakdown de "Louças e Metais" no mesmo sentido estrito (Maiori, Terrassa, Estoril, Pavcor), **todos têm R$ 23–28/m²** — a mediana calibrada condicional puxa pra cima porque provavelmente conta granito/mármore/acessórios junto com louças em alguns projetos. **No sentido estrito (só bacia+cuba+torneira+ducha), Arboris em R$ 32/m² está no topo da amostra, e portanto está OK ou até um pouco alto.**

Correção: **Louças e Metais NÃO é erro**. É consistente com os executivos comparáveis.

## 4. Erros críticos confirmados

### 🔴 ERRO-01: Sistemas Especiais — elevadores drasticamente subdimensionados

**Confirma-se como erro principal.**

- **Arboris:** R$ 288.450 pra 2 elevadores (social R$ 192k + serviço R$ 96k) → R$ 102/m² AC total Sist. Especiais
- **Amostra comparável (7 obras):** min R$ 96, P25 R$ 111, mediana R$ 204, P75 R$ 241, max R$ 255
- **Arboris é o mínimo** da amostra — 2º lugar muito próximo ao menor (Pavcor R$ 96)

**Mercado Itajaí/SC 2026 pra 19 paradas:**
- Elevador social alto padrão (13+ paradas): R$ 700k–1,2M
- Elevador de serviço (idem): R$ 500k–800k
- **2 elevadores juntos: R$ 1,2–2,0 M** (apenas equipamento)

**Checagem adicional — índice derivado `custo_elevador_rsm2` (n=70):** mediana R$ 213/m² AC → Arboris deveria ter R$ 2,66M só em elevadores.

**Valor esperado Sist. Especiais ajustado:** R$ 2,2–2,8M → R$ 175–220/m² AC (alinhado com amostra).

**Gap estimado:** R$ 1,2–2,0 M.

**Causa:** o PU base do script `calibration-indices.json` para elevador trabalha com torre de 8–13 paradas. Não está escalando com número de paradas.

---

### 🔴 ERRO-02 (revisado): Supraestrutura acima do máximo da amostra

**Novo achado com a análise nominal.**

- **Arboris:** R$ 786/m² AC — **acima do máximo** da amostra (pass-e-celebration 762, pass-e-connect 736)
- **Estrutura Arboris:**
  - Concreto: 3.024 m³ × R$ 590/m³ = R$ 1,78M
  - Aço: 330.534 kg × R$ 8,67/kg = R$ 2,87M
  - Forma: 22.202 m² × R$ 88/m² = R$ 1,96M
  - MO empreitada 32,6%: R$ 3,19M
- **Índices vs base master (n=64-69):**
  - Concreto 0,25 m³/m² — mediana base
  - Aço 106 kg/m² — mediana base
  - Forma 7,12 m²/m² — mediana base
  - Razão aço/concreto 0,0134 — exatamente mediana

Os **índices físicos estão normais**. O problema provável é a **soma MO empreitada (R$ 3,19M) em cima de PUs que já incluem MO**.

**Checagem rápida:**
- PU concreto R$ 590 — mediana Cartesian `pu_concreto_usinado_mediano` = R$ 517 (só material bombeado). R$ 590 está R$ 73/m³ acima — pode ser lançamento/vibração/acabamento.
- PU aço R$ 8,67 — mediana `pu_aco_ca50_mediano` = R$ 6,80. R$ 8,67 está R$ 1,87/kg acima — pode ser armação/montagem.
- PU forma R$ 88 — mediana `pu_forma_madeira_mediano` = R$ 16 (compensado plastif. só material) ou R$ 165 em serviço completo. R$ 88 está em meio do caminho.

**Leitura:** os PUs Arboris já incluem MO parcial, mas a linha "MO Estrutura empreitada 32,6%" está somando OUTRA VEZ 32,6% do total material como MO. Provavelmente há **duplicação de ~R$ 800 k–1,2 M**.

**Ação:** rodar composição de 2-3 executivos (Maiori, Celebration, Connect) pra ver como a MO estrutural está compondo — se está em PU ou separada.

**Impacto esperado após correção:** supra cai pra R$ 650–720/m² AC (dentro da amostra).

---

### 🔴 ERRO-03 (novo): Fachada acima do máximo da amostra

- **Arboris:** R$ 361/m² AC
- **Amostra (n=7):** min R$ 94, mediana R$ 149, max R$ 300 (pass-e-connect)
- **Arboris R$ 361 > R$ 300 máximo da amostra**

**Composição Arboris:**
- Revestimento cerâmico: 19.333 m² × R$ 180 = R$ 3,48M
- MO fachada: R$ 35/m² = R$ 677k
- Balancim: R$ 18/m² = R$ 348k
- **Total fachada: R$ 233/m² de fachada × índice 1,55 = R$ 361/m² AC**

**Comparação com fachada cerâmica real:**
- pass-e-connect (fachada cerâmica): R$ 300/m² AC — 20% abaixo de Arboris
- estoril: R$ 259 — 28% abaixo
- Os demais usam textura/pele de vidro e variam R$ 94–197/m² AC

**Diagnóstico:** mesmo admitindo cerâmica, Arboris está **R$ 61/m² AC acima** do projeto mais parecido (Connect). Possível sobreposição:
- PU R$ 180/m² pode já incluir MO parcial → duplicação com linha MO R$ 35
- OU índice fachada/AC 1,55 está alto (Connect provavelmente opera em ~1,3–1,4 para prédio similar)

**Impacto estimado:** ajustando pra R$ 300/m² AC (top da amostra), reduz ~R$ 760 k.

**Ação:** validar composição com Patricia — se cerâmica Arboris é premium (formato grande, assentamento duplo ancorado), manter. Caso contrário, alinhar com Connect.

---

### 🔴 ERRO-04 (novo): Impermeabilização acima do máximo

- **Arboris:** R$ 80/m² AC
- **Amostra (n=7):** min R$ 17, mediana R$ 57, max R$ 71 (pavcor com infraestrutura de piscina+terraços)
- **Arboris R$ 80 > R$ 71 máximo**

**Composição:**
- Manta 4mm: 5.613 m² × R$ 82,11 = R$ 461k
- Argamassa polimérica BWC: 1.684 m² × R$ 8,50 = R$ 14k
- Regularização: 5.613 m² × R$ 5,57 = R$ 31k
- MO imperm. + regul. (split 56,5%): R$ 491k
- **Total R$ 997 k**

**Índice impermeab./AC = 0,45** — topo da faixa base (0,30–0,45). Justificado por 1 subsolo + 98 BWCs + piscina.

**Porém os comparáveis com piscina também têm R$ 57–71/m² AC**. Arboris pode estar:
- Com PU manta alto (R$ 82 vs base P50 R$ 40 + MO → total R$ 90–150/m² de impermeab.). Arboris total por m² impermeab. = R$ 170/m² — no topo.
- Ou com MO duplicada (similar ao caso de Supra)

**Ação:** verificar se a linha "MO imper. + MO regul. (split 56,5%)" está adicionada em cima de PUs que já embutiam MO.

---

## 5. Achados que NÃO são erros (revisão vs r1)

### ✅ Louças e Metais — não é erro

Conforme seção 3 acima: Arboris R$ 32/m² AC é **o maior da amostra** de 4 projetos comparáveis com breakdown específico. A mediana condicional agregada (R$ 60/m²) é inflada por projetos que agrupam outros itens sob "Louças".

### ✅ Movimentação de Terra — coerente com 1 subsolo

- Arboris R$ 32/m² AC
- Amostra: min 7, mediana 20, max 40
- **Arboris 2º maior, dentro do P75** — consistente com subsolo 1 nível em solo típico litoral norte SC.
- Na primeira versão concluí subdimensionado olhando só a mediana condicional (R$ 115 — puxada por projetos com 2–3 subsolos). **Correção: está OK.**

### ✅ Complementares — na P25 da amostra

- Arboris R$ 122/m² AC
- Amostra: min 52 (pass-e-passione), P25 104, mediana 145, P75 197
- **Dentro do P25–mediana** — não é erro.

A análise anterior apontou R$ 201/m² como "mediana Médio-Alto agregada", mas os comparáveis executivos reais ficam em R$ 72–197. Arboris está **na faixa normal**.

## 6. Pontos de atenção (decisão, não erro)

### 🟠 Gerenciamento — abaixo do P25

- Arboris R$ 372/m² AC
- Amostra: min 288 (Vancouver), P25 397, mediana 532, max 682
- **Arboris 2º menor** — plausível pelo prazo curto (30 meses) vs prazo médio dos comparáveis (~36–42 meses)
- Por mês: R$ 372 / 30 = **R$ 12,40/m²·mês** — alinhado com padrão Cartesian (R$ 11–13/m²·mês)
- **Decisão:** aceitar o valor se o prazo de 30 meses for realista pra 24 pavimentos. Se o prazo for otimista, aumentar. 30 meses pra 98 unidades + 19 pav. tipo é **agressivo** — referência comum é 34–38 meses.

### 🟠 Rev. Interno Parede — abaixo do P25 (amostra pequena)

- Arboris R$ 128/m² AC
- Amostra (n=4): min 48, P25 196, mediana 238, max 496 (terrassa)
- **Arboris abaixo** do P25 mas a amostra é pequena e os valores dos comparáveis que abrem esse macrogrupo talvez agrupem outras coisas (rev. parede + piso + bancadas)
- **Decisão:** validar com Patricia — se o projeto Arboris tem porcelanato em área comum mais a cerâmica de BWC/cozinha, o valor deve subir. Estrutura atual (R$ 1,6M) parece razoável pra entrega Médio-Alto padrão.

### 🟠 Climatização — avaliar se inclui split de apto

- Arboris R$ 67/m² AC
- Amostra (n=3): R$ 28, 42, 86 — Arboris entre P50 e P75
- **Decisão pendente com Arthen:** se entrega NÃO inclui splits dentro dos apartamentos, descontar R$ 514k (147 splits × R$ 3.500) → cai pra R$ 25/m² AC (perto do min).

### 🟠 Imprevistos 1,5%

- Arboris: 1,5% do subtotal = R$ 671 k → R$ 54/m² AC
- Amostra (n=6): min 40, mediana 48, max 158 (pass-e-connect com 4,3%) — Arboris na mediana
- **Padrão da amostra Cartesian = 1,3–2% na prática**. Os projetos com Imprev > R$ 100/m² (Connect 158, Passione 120) estão com 3-4%, mais adequado pra paramétrico pré-executivo.
- **Decisão:** manter 1,5% é consistente com a prática Cartesian, mas aumentar pra 3% pro paramétrico (pré-executivo) é mais conservador. Ponto de política com Leo/Patricia.

## 7. Resumo executivo — decisões pendentes

| # | Item | Impacto estimado | Status |
|---|------|-----------------:|---|
| 1 | **Elevadores (Sist. Especiais)** — subdimensionados | **+R$ 1,2–2,0 Mi** | 🔴 AJUSTAR |
| 2 | **Supraestrutura** — possível duplicação de MO | **-R$ 0,8–1,2 Mi** | 🔴 VERIFICAR composição |
| 3 | **Fachada** — acima do máximo da amostra | **-R$ 0,6–0,8 Mi** | 🔴 VALIDAR PU vs MO |
| 4 | **Impermeabilização** — acima do máximo | **-R$ 0,2 Mi** | 🔴 VERIFICAR MO |
| 5 | Climatização (split de apto?) | -R$ 514 k ou OK | 🟠 VALIDAR com Arthen |
| 6 | Gerenciamento (prazo 30 meses?) | +R$ 0–0,8 Mi | 🟠 VALIDAR prazo |
| 7 | Imprevistos (3% em vez de 1,5%?) | +R$ 0–670 k | 🟠 DECIDIR política |

**Cenário ajustado provável** (corrigindo 1+2+3+4): **R$ 44,5–46,5 Mi (R$ 3.570–3.720/m²)** — similar ao atual, mas com **redistribuição**: elevadores sobem, supra/fachada/imper descem. Valor total quase igual, mas **perfil por macrogrupo fica dentro da amostra**.

## 8. Observações sobre a amostra

- **8 obras são um bom tamanho** pra conclusões diretas nos macrogrupos grandes (Supra, Instal, Pintura, Esquad, Ger). Pros macrogrupos menores (Louças, Climat, RevP), a amostra cai pra 3–4 e as conclusões ficam menos robustas.
- **Todas as obras da amostra** são residenciais multifamiliares de torre única, altura comparável. Mistura de Médio-Alto (5) e Alto (3) — a diferença entre os dois padrões afeta acabamentos (pisos, esquadrias, louças) mas não muito estrutura/gerenciamento/fundação.
- **A amostra total disponível era maior** (22 obras passaram no filtro R$/m² plausível), mas o filtro final removeu economico/atípicos pra dar uma comparação homogênea.
- **A amostra NÃO está indexada ao CUB Mar/2026** — para apresentação pro cliente, indexar antes de mostrar a tabela.

## 9. Arquivos gerados

- `_dados-126-projetos.csv` — **todos** os projetos processados (54 com R$/m² plausível)
- `_dados-projetos-comparaveis.csv` — 22 projetos com AC + breakdown
- `_dados-projetos-CONSOLIDADO.csv` — mesma lista com macrogrupos canonicalizados
- `_tabela-comparativa.md` — tabela Markdown com os 8 comparáveis
- `ANALISE-ERROS-v3.md` (este)
- `JUSTIFICATIVA-MACROGRUPOS.md` (atualizado em r2)
- `ESTRUTURA-APRESENTACAO-ARBORIS.md` (inalterado)
