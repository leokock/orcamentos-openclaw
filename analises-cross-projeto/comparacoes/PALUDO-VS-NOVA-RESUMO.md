# Paludo vs Nova Empreendimentos — Análise comparativa

**Gerado em:** 2026-04-18
**Contexto:** ambos pertencem ao **Cluster 1 (EPCM/alto-gerenciamento)** mas têm R$/m² **2.2× diferente** (R$ 2.781 vs R$ 6.107). Esta análise investiga o porquê.

---

## Sumário executivo

| Métrica | Paludo | Nova | Delta |
|---|---:|---:|---:|
| N projetos | 5 | 4 | — |
| AC total | 17.407 m² | 20.880 m² | +20% |
| AC mediana | 3.264 m² | 4.720 m² | +45% |
| Total acumulado | R$ 51.388.412 | R$ 131.457.479 | **+156%** |
| R$/m² mediana | R$ 2.781 | R$ 6.107 | **+120%** |
| N itens/projeto (mediana) | 394 | 4.359 | **+1.008%** |

**Leitura rápida:** Nova fatura 2.6× mais com AC só 20% maior. Os projetos da Nova são **11× mais detalhados** em número de itens (4.359 vs 394) — orçamentos mais minuciosos.

---

## Distribuição % Macrogrupo (onde vai a grana)

| MG | Paludo % | Nova % | Diff pp | Leitura |
|---|---:|---:|---:|---|
| **Gerenciamento** | 35.4% | **42.4%** | **+7.0pp** | Nova concentra ainda mais em ger (ja alto em Paludo) |
| Sist Especiais | 5.6% | 1.3% | -4.3pp | Paludo aloca MAIS em sist especiais (elevador, gerador) |
| Pisos | 7.0% | 3.0% | -4.1pp | Paludo detalha pisos, Nova nao |
| Pintura Geral | 4.4% | 0.7% | -3.8pp | Paludo detalha pintura, Nova nao (deve estar em Rev Parede) |
| Elétrica | 0.0% | 3.8% | +3.8pp | Nova tem eletrica separada, Paludo usa Instal Geral |
| Esquadrias | 10.3% | 6.6% | -3.6pp | Paludo aloca MAIS em esquadrias |
| Rev Parede | 3.4% | 6.9% | +3.4pp | Nova concentra revestimento parede |
| Fachada | 3.2% | 0.7% | -2.5pp | Paludo detalha fachada, Nova quase nada |
| Supraestrutura | 14.6% | 12.3% | -2.3pp | Paludo um pouco mais |
| Hidrossanitária | 5.5% | 3.3% | -2.2pp | Paludo detalha hidro |
| Pint Interna | 4.2% | 2.1% | -2.2pp | Paludo detalha pint interna |

**Padrão:** Paludo **detalha mais os acabamentos e disciplinas** (sist especiais, pisos, pintura, esquadrias, fachada, hidro, pint interna). Nova **concentra em gerenciamento e rev parede** (categorias guarda-chuva).

---

## Padrão de detalhamento

- **Paludo**: ~394 itens/projeto mediana. Escopo documentado em premissas explícitas (5 premissas em barbados sobre revestimentos, esquadrias, fachada). Orçamentos **"enxutos mas claros"**.
- **Nova**: ~4.359 itens/projeto mediana. Presença de itens como **"Valor Compra do Terreno R$ 4.820.633"** embutido no projeto (evora) — sinal de escopo expandido.

### Itens fora da curva da Nova (4 instâncias)

| Projeto | Item | Motivo |
|---|---|---|
| **evora** | **Valor Compra do Terreno** | R$ 4.820.633 embutido — muito maior que demais itens orçamentários |
| evora | Repetições de pavimentos** | Item marcado com ** (notação de atenção Cartesian) |
| malaga | Piso tátil Bolinha Alerta Inox | Alerta (revisao de escopo) |
| malta | QUANTIDADE RETIRA DO PROJETO | Instrução manual de retirada de quantidade |

### Alertas / Revisões da Nova

- **Malta — Revisão:** "Ajuste de cálculo: Dividi por 2, pois a Desforma não estava contabilizada na planilha MAT" (dado do cliente veio errado/incompleto)
- **Malta — Alerta:** "QUANTIDADE RETIRA DO PROJETO"
- **Evora — Revisão:** "Valor preenchido em formulário (custo apropriado de R$ 5.000,00)"

### Paludo — zero alertas, zero revisões, zero fora-da-curva

Documentação de escopo via premissas. Orçamentos "sem sobressaltos".

---

## Hipótese para o delta 2× em R$/m²

1. **Escopo da Nova é mais amplo** — inclui terreno (evora), mais detalhamento de itens. O R$/m² alto reflete **escopo maior**, não margem maior.
2. **Modelo de contratação EPCM idêntico** (ambos alto-gerenciamento) mas Nova trata o projeto como **"pacote completo"**, incluindo aquisições que normalmente ficam fora.
3. **Paludo é benchmark de eficiência EPCM puro** — só construção + gerenciamento.
4. **Orçamentos da Nova requerem mais atenção** (alertas, revisões, fora-da-curva) — dados do cliente precisam de ajuste antes de precificar.

### Não é só margem — é escopo

Se fosse pura margem inflada, não esperaríamos:
- 11× mais itens nos projetos da Nova
- Compra de terreno embutida
- Observações de ajuste/revisão de dados do cliente

A diferença é **composição de escopo + detalhamento**. Nova entrega "mais coisa" no pacote Cartesian.

---

## Recomendações operacionais

1. **Reunião comercial com Nova**: apresentar que sabemos que orçamentos da Nova incluem escopo expandido (terreno, infraestrutura). Posicionar como diferencial Cartesian.

2. **Se pretende fazer comparação Nova → Paludo pra Nova reduzir custo**: isolar a parte "compra de terreno + aquisições" antes de comparar. Sem isolar, Paludo parecerá 2× mais barato de forma enganosa.

3. **Template de orçamento Nova**: escopo inclui terreno + consultorias extras + repetições de pavimento marcadas com **. Formalizar isso acelera próximos orçamentos.

4. **Template de orçamento Paludo**: 5 premissas de escopo (revestimento, teto, acabamentos, esquadrias, fachada) explicitadas na aba qualitative. Isso é boa prática — replicar pra outros clientes.

5. **Alertas da Nova sinalizam dado ruim do cliente**. Criar checklist de validação de planilha recebida antes de precificar.

6. **Cross-reference Cluster 1 (EPCM) documentado**: Paludo = "EPCM puro" (R$ 2-3k/m²), Nova = "EPCM completo com aquisições" (R$ 5-7k/m²). São dois sub-modelos do mesmo cluster.

---

## Script reusável

`scripts/comparar_clientes.py` — comparador de 2 clientes arbitrários:

```bash
python scripts/comparar_clientes.py --a paludo --b nova-empreendimentos \
    --nome-a Paludo --nome-b "Nova Empreendimentos"
```

Gera automaticamente o MD + JSON com todas as tabelas acima. Use pra:
- Mussi vs Pass-e (ambos médio-alto, R$/m² 2.949 vs 3.429 — pouco diferente, diagnóstico esperado "ALINHADOS")
- Santa Maria vs qualquer — Santa Maria tem R$/m² 1.604, outliers extremo de eficiência
- Novas investigações à medida que base cresce

---

## Arquivos desta entrega

- **Script:** `scripts/comparar_clientes.py`
- **Output JSON:** `base/comparacoes-clientes/paludo-vs-nova-empreendimentos.json`
- **Output MD detalhado:** `base/comparacoes-clientes/paludo-vs-nova-empreendimentos.md`
- **Este resumo:** `base/PALUDO-VS-NOVA-RESUMO.md`
