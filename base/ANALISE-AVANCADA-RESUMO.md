# Análise Avançada Cartesian — Cliente, Cluster, Qualitativa

**Gerado em:** 2026-04-18
**Base:** 126 orçamentos executivos
**Foco:** quem é o cliente, que tipologia o projeto tem, o que o orçamentista registrou

---

## 1. Quem paga mais/menos? (Análise por cliente)

**Clientes com 3+ projetos na base** (ordenado por R$/m² mediana dos projetos válidos):

### Top EFICIENTES (R$/m² baixo — benchmark interno)

| Cliente | N proj | N válidos | R$/m² mediana | AC total | Padrão dominante |
|---|---:|---:|---:|---:|---|
| **Santa Maria** | 3 | 1 | **R$ 1.604** | 52.914 m² | alto |
| **Paludo** | 5 | 3 | **R$ 2.781** | 17.408 m² | médio-alto |
| **Mussi Empreendimentos** | 4 | 2 | **R$ 2.949** | 40.149 m² | médio-alto |
| **Pass-e** | 6 | 4 | **R$ 3.429** | 54.980 m² | médio-alto |

### Top CAROS (R$/m² alto — investigação caso-a-caso necessária)

**⚠ Ressalva:** classificação baseada em **1-2 projetos válidos por cliente** — interpretar como sinal de atenção, não conclusão. A análise Paludo vs Nova v2 (gerada em 18/abr) mostrou que, mesmo com R$/m² 2× maior, Nova não é uniformemente mais cara no PU — diferença vem de escopo, especificação e qualidade de dados. **Valor alto ≠ margem inflada automaticamente.**

| Cliente | N proj | N válidos | R$/m² mediana | AC total | Padrão dominante |
|---|---:|---:|---:|---:|---|
| **ALL** | 2 | 1 | **R$ 7.160** | 8.999 m² | médio-alto |
| **Nova Empreendimentos** | 4 | 2 | **R$ 6.107** | 20.881 m² | alto |

**Leitura:** Nova Empreendimentos paga **46% acima da mediana alto padrão** (R$ 4.188). Se o escopo justifica, ótimo. Se for margem inflada, pode estar perdendo competitividade.

### Clientes com muitos projetos mas sem R$/m² válido (AC incompleto)

- **CK** (8 projetos, 0 válidos) — importante cliente mas dados de AC faltam
- **Chiquetti & Dalvesco** (6 projetos) — mesmo problema
- **Amalfi** (4 projetos) — AC de unidades individuais, não do empreendimento

**Ação sugerida:** preencher AC desses projetos prioritários no reprocessamento pra habilitar análise cross-cliente.

---

## 2. Tipologias descobertas (4 clusters)

K-means sobre % MG revelou **4 tipos de projeto**, independentes do padrão construtivo:

### Cluster 3 — "Projetos Alto-Gerenciamento" (13 projetos, R$/m² 3.799)

**Assinatura:**
- Gerenciamento: **39.5%** do total (3× a média)
- Supraestrutura: 15.3%
- Esquadrias: 7.2%

**Mix de padrões:** 9 médio-alto, 4 alto.

**Interpretação:** projetos com **MUITA consultoria/projetos/administração**. Pode ser:
- Alto padrão com consultorias especializadas (retrofit, certificação LEED, BIM avançado)
- Projetos com sobrecarga de custo indireto mal alocado
- Projetos com escopo de desenvolvimento de projeto + obra

**Membros:** ver aba CLUSTER_MEMBROS no Excel.

### Cluster 0 — "Construção Padrão" (27 projetos, R$/m² 3.378)

**Assinatura:**
- Supraestrutura: 22%
- Hidrossanitárias: 11.4%
- Gerenciamento: 10.4%
- Pisos: 9.9%
- Esquadrias: 9.1%

Perfil clássico, distribuição equilibrada. Mix: 18 médio-alto + 7 alto + 2 econômico. **É o "projeto típico" da Cartesian.**

### Cluster 2 — "Grandes com Complementares" (27 projetos, R$/m² 3.296)

**Assinatura:**
- Supraestrutura: 19%
- **Outros: 18.3%** (?)
- Gerenciamento: 11.4%
- Esquadrias: 9.9%
- Serviços Complementares: 7.5%

**AC mediano: 12.519 m²** (maior entre clusters). "Outros" domina — ou é categoria que não foi canonizada bem, ou projetos com serviços especiais não padronizados.

**Ação:** investigar quais MGs foram pra "Outros" nesse cluster — pode revelar necessidade de nova categoria canônica.

### Cluster 1 — "Convencionais Grandes" (9 projetos, R$/m² 3.456)

Mix equilibrado, AC mediana 10.479 m². "Projeto grande sem peculiaridade" — sem dominância de nenhum MG específico.

---

## 3. Complexidade por padrão

| Padrão | Abas med | Itens med | MGs med | N amostra |
|---|---:|---:|---:|---:|
| Alto | 3 | **1.736** | 17 | 57 |
| Médio-alto | 3.5 | **796** | 17 | 60 |
| Médio | 4.5 | **2.602** | 15.5 | 4 |
| Econômico | 1.5 | **38** | 17 | 4 |

**Observações:**
- **Número de macrogrupos é universal (~17)** — a estrutura do orçamento é padronizada.
- **Detalhamento de itens varia enormemente**: alto padrão tem 1.736 itens vs econômico 38.
- **Médio tem 2.602 itens** na mediana (só 4 amostras) — pode ser atípico.

**Hipóteses para a variação (qwen apontou que não consideramos causas):**
- **Maturidade do cliente** — clientes alto padrão cobram orçamento detalhado; econômicos aceitam estimativa
- **Escopo** — projetos grandes têm mais subdisciplinas, inerentemente mais itens
- **Ferramenta usada** — orçamentos em Sienge/Vero geram mais itens que planilha Excel manual
- **Estágio do pacote** — paramétrico tem poucos itens; executivo detalhado tem milhares

**Ressalva:** Médio tem apenas n=4 amostras, a mediana 2.602 itens pode ser atípica (puxada por 1-2 projetos grandes). **Econômico com 38 itens (n=4) provavelmente são orçamentos parciais ou paramétricos** — não comparável com executivos de outros padrões.

**Implicação (cautelosa):** parece haver relação escala/detalhamento com padrão, mas *não é linear* — mais amostras de médio e econômico necessárias.

---

## 4. Camada qualitativa — a sabedoria dos orçamentistas

**544 observações categorizadas** em 126 projetos (média 4.3 por projeto):

| Categoria | N | % |
|---|---:|---:|
| outro | 181 | 33% |
| premissa | 169 | 31% |
| justificativa | 140 | 26% |
| revisão | 27 | 5% |
| alerta | 21 | 4% |
| contexto | 6 | 1% |

**Insights:**

- **"Premissas" (31%)** são observações sobre escopo/limites — "valor repassado pelo cliente", "considerado conforme cliente X". Oportunidade: formalizar essas premissas em template de orçamento.
- **"Justificativas" (26%)** explicam escolhas técnicas. Bom material pra alimentar base de conhecimento Cartesian (prompts Gemma/Claude).
- **"Alertas" (4%)** — risco/atenção. **Baixo volume sugere subreporte. Encorajar equipe a registrar mais alertas.**
- **"Outro" (33%)** — categoria genérica. **Sugere refinar taxonomia**: criar categorias "escopo_externo", "metodologia", "fornecedor".

### Itens identificados como padrão em múltiplos projetos

| Item | N projetos |
|---|---:|
| ACABAMENTOS EM PISO E PAREDE | 7 |
| ESQUADRIAS, VIDROS E FERRAGENS | 6 |
| GERENCIAMENTO TÉCNICO E ADMINISTRATIVO | 4 |
| Esquadrias de Alumínio - fornecimento e instalação | 3 |
| Imprevistos e Contingências | 2 |
| Mão de obra para execução de supraestrutura | 2 |
| Concreto usinado bombeável | 2 |
| Repetição do item 'Mão de obra supraestrutura' | 2 |

**Leitura:** orçamentistas marcam esses itens como "padrão identificado" — são pontos onde se repete lógica ou referência. Candidatos a **padronização em template Cartesian**.

### Itens recorrentes em "fora da curva"

Top 10 (cada aparece em 1 projeto):
- Mão de obra supraestrutura, Mão de obra infraestrutura
- Etapa fora do escopo da Cartesian
- PROJETOS, GERENCIAMENTO TÉCNICO
- Margem de segurança
- MOBILIÁRIO E DECORAÇÃO
- MESTRE DE OBRAS
- IMPREVISTOS E CONTINGÊNCIAS

**Padrão:** **MO (mão de obra)** domina os itens fora da curva. A precificação de MO varia muito entre projetos — motivo comum: "cliente informou outro valor", "empreitada difere do unitário da planilha base".

**Implicação:** criar **rotina de alerta sistemático** quando MO supraestrutura/infraestrutura difere >20% de projetos similares. Ajuda orçamentista a justificar ou corrigir.

---

## 5. Paramétrico × Executivo (limitado)

**Pacotes paramétricos ativos:** arthen-arboris, pacote-piloto, placon-arminio-tavares, thozen-electra.

**Match com executivo:** 0/4 (slugs não batem — `thozen-electra` no paramétrico ≠ `thozen-mirador-de-alicante` em `indices-executivo`). 

**Ação sugerida:** quando fechar um executivo baseado em paramétrico, manter slug consistente nas duas bases (ou criar tabela de cross-reference). Sem isso, não dá pra medir **erro real do paramétrico** sistematicamente.

---

## 6. Recomendações acionáveis

1. **Ficha de cliente Cartesian** — pra Nova, Paludo, Pass-e, Mussi, Santa Maria, F. Nogueira — com: padrão típico, R$/m² mediana histórica, top 3 peculiaridades dos orçamentos. **Usa em reunião comercial.**

2. **Validar Nova Empreendimentos** — 46% acima da mediana alto padrão. Conversar com Patrícia ou quem atende: é escopo diferenciado ou margem?

3. **Template "Cluster 3"** — projetos alto-gerenciamento (40% em gerenciamento) têm assinatura distinta. Criar template de orçamento pra essa tipologia, com consultorias pré-especificadas.

4. **Investigar "Outros" no Cluster 2** — categoria consumindo 18% do total é sintoma de classificação ruim. Mapear o que vai pra lá e criar MGs canônicos.

5. **Preencher AC — em ordem de prioridade:**
   1. CK (8 projetos sem AC válido) — **fazer primeiro**, maior impacto na amostra
   2. Chiquetti & Dalvesco (6 projetos)
   3. Amalfi (4 projetos), CN Brava (3 projetos)
   4. Demais clientes com projetos sem AC (Cambert, Blue Heaven, Brasin, Eze)
   - **Método sugerido:** extrair AC do memorial descritivo ou do formulário de briefing quando disponível. Não extrapolar a partir de UR × área média — introduz ruído.

6. **Encorajar registro de "alertas" — plano concreto:**
   - Template de briefing com campo obrigatório "principais riscos/alertas" (min 2 itens)
   - Reunião mensal de orçamentistas com leitura dos alertas da base — cria consciência coletiva
   - Meta: dobrar em 3 meses (de 21 → 40 alertas, ainda razoavelmente baixo em 126 projetos)
   - **Não inflar artificialmente** — qualidade > volume

7. **Cross-reference paramétrico ↔ executivo** — tabela mantida no git mapeando slugs equivalentes. Habilita análise de erro paramétrico.

8. **Padronizar precificação de MO supraestrutura/infraestrutura** — domina fora-da-curva. Criar banda de referência por padrão com alerta automático.

9. **Aumentar amostra médio/econômico** — só 4 projetos cada. Enviesa análise cross-padrão.

10. **Capturar "data_base" em todos os projetos** — hoje só 14 têm. Impede análise de inflação orçamentária.

---

## Arquivos desta entrega

- **Excel:** `base/analise-avancada-cartesian.xlsx` (8 abas)
- **JSON:** `base/analise-avancada-agregada.json`
- **Este resumo:** `base/ANALISE-AVANCADA-RESUMO.md`
- **Scripts:** `scripts/analise_avancada.py` + `scripts/gerar_planilha_avancada.py`

---

## Visão consolidada — 3 planilhas, papéis distintos

| Planilha | Foco | Pergunta respondida |
|---|---|---|
| `analise-produto-cartesian.xlsx` | **Indicadores físicos** | Quantos pontos/un/m² o projeto tem? Dentro da faixa? |
| `analise-financeira-cartesian.xlsx` | **$$ / Distribuição %** | Quanto custa por padrão? Onde está a grana? |
| `analise-avancada-cartesian.xlsx` | **Perfil + Qualitativa** | Quem é o cliente? Qual tipologia? O que o orçamentista anotou? |

Todas no Drive em `~/orcamentos/parametricos/`.
