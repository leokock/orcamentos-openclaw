# Estratégia Dois Tiers — Orçamento Paramétrico Cartesian

> Documentação dos dois produtos paramétricos e suas diferenças.
> Criado: 06/mar/2026

---

## Visão Geral

A Cartesian oferece dois níveis de orçamento paramétrico, conforme a disponibilidade de base de dados na região do projeto:

| | Paramétrico Cartesian | Paramétrico Estrutural |
|---|---|---|
| **Quando usar** | Cidades com base consolidada (🟢 no mapa) | Cidades sem base (🔴) ou base inicial (🟡) |
| **Base de preço** | Preço médio real de mercado (mediana de executivos reais da região) | Índices percentuais calibrados + PUs captados localmente |
| **Inteligência** | Amostra estatística real → preço absoluto confiável | Estrutura de distribuição calibrada → proporções confiáveis |
| **Confiança** | Alta (validada com +2% vs executivo real) | Média (depende da qualidade dos PUs informados) |
| **Ressalvas** | Nenhuma especial | PUs dependem de input externo; particularidades regionais não capturadas |

---

## Tier 1 — Paramétrico Cartesian (base consolidada)

**O que entrega:** Estimativa de custo baseada em preço médio de mercado real. "Na nossa base, empreendimentos parecidos com o seu na região de [cidade] custam R$ X por m²."

**Como funciona:**
1. Dados do projeto (área, pavimentos, unidades, etc.)
2. Briefing (25 perguntas, ordenadas por impacto)
3. Modelo calcula: Base R$/m² × Fator CUB × Fator Briefing
4. Benchmark automático com projetos similares da base

**Confiança:** Alta. Validada com diferença de +2% vs executivo real (teste Domus). Mediana calibrada com 33+ projetos.

**Onde funciona:** Ver `MAPA-COBERTURA.md` — cidades 🟢

---

## Tier 2 — Paramétrico Estrutural (sem base consolidada)

**O que entrega:** Modelo de distribuição de custos calibrado. "Sabemos quanto cada sistema construtivo representa do custo total, e aplicamos isso aos preços unitários da sua região."

**Como funciona:**
1. Dados do projeto (igual ao Tier 1)
2. Briefing (igual ao Tier 1)
3. Modelo aplica índices percentuais da base Cartesian (distribuição entre macrogrupos)
4. PUs de referência são captados externamente:
   - Do cliente (se tiver orçamentos anteriores na região)
   - De SINAPI/TCPO regionais
   - De fornecedores locais (cotações)
   - Do CUB estadual como referência macro

**O que é confiável:**
- Distribuição percentual entre macrogrupos (física da construção é similar entre regiões)
- CUB ratio (atemporal e regional-agnostic — alto padrão ≈ 1,2-1,5 CUB em qualquer lugar)
- Fatores do briefing (nº pavimentos, subsolo, padrão acabamento funcionam independente da cidade)

**O que NÃO é confiável sem base local:**
- Preço absoluto de mão de obra (varia muito entre regiões)
- Custos logísticos (frete, disponibilidade de materiais)
- Exigências municipais específicas (ex: CINDACTA em Navegantes, ETE em Bombinhas)
- Custos indiretos regionais (taxas, projetos, canteiro)

---

## Ressalvas Obrigatórias (Tier 2)

Ao entregar um Paramétrico Estrutural, SEMPRE incluir:

1. "Este paramétrico utiliza modelo de distribuição calibrado com 50+ projetos da Cartesian, porém os preços unitários de referência para [cidade/estado] foram captados externamente e não são baseados em executivos reais da região."
2. "A precisão depende da qualidade dos preços unitários de referência informados. Recomendamos validar com orçamentos locais."
3. "Conforme a Cartesian processar orçamentos executivos nesta região, o modelo será recalibrado com dados reais, aumentando a confiabilidade."
4. "Para máxima precisão, recomendamos o orçamento executivo completo."

---

## Fluxo de Captação de PUs (Tier 2)

### Opção A — PUs do Cliente
1. Solicitar ao cliente: "Você tem orçamentos executivos de projetos anteriores na região?"
2. Se sim: extrair PUs médios por macrogrupo → usar como base
3. Vantagem: dados reais da região, cliente se sente dono do input

### Opção B — PUs de Referência Pública
1. Consultar SINAPI do estado (preços de insumos e composições)
2. Consultar CUB estadual (referência macro)
3. Montar PUs estimados por macrogrupo
4. ⚠️ SINAPI é referência de obras públicas — ajustar para mercado privado

### Opção C — Cotações Diretas
1. Solicitar cotações de fornecedores/empreiteiros da região
2. Focar nos macrogrupos de maior impacto: Supraestrutura, Instalações, Acabamentos, Esquadrias
3. Mais trabalhoso, mas mais preciso

### Recomendação
- Combinar Opção A (se disponível) + Opção B (complemento)
- Sempre validar CUB ratio final contra benchmark Cartesian

---

## Evolução Natural

```
Cidade nova (🔴) → 1º executivo processado (🟡) → 3º executivo (🟢)
     Tier 2                    Tier 2                     Tier 1
```

Conforme projetos forem entregues em novas regiões:
1. Cada executivo vira dado de calibração local
2. O mapa de cobertura é atualizado
3. A cidade migra de tier progressivamente
4. Os PUs captados são substituídos por PUs reais

---

## Nomenclatura Interna

Para evitar ambiguidade:
- **"Paramétrico"** (sem qualificar) = sempre Tier 1 (base consolidada)
- **"Paramétrico Estrutural"** = Tier 2 (índices + PUs captados)
- Nunca usar um quando significa o outro

---

*Decisão: 06/mar/2026 (Leo aprovou a estratégia de dois tiers)*
*Status: Documentado, não comercializado ainda. Amadurecer antes de oferecer.*
