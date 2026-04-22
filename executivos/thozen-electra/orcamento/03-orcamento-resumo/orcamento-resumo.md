# Orçamento Resumo — Visão consolidada

## Propósito

Esta pasta contém a **visão agregada** do orçamento executivo:
- Custo total por disciplina (consolidação dos 22 memoriais)
- Comparativo com o orçamento paramétrico inicial
- Marcos de revisão (R00, R01, …)

## Arquivos

- `orcamento.xlsx` — cópia da aba "Orçamento" do template (R00 — base Visus)
- `orcamento-resumo.md` — este arquivo (consolidação narrativa)

## Estrutura prevista quando consolidação for feita

```
custo_por_disciplina:
  EPCs: { paramétrico_pct: 1.2%, executivo_pct: ?, valor_R$: ? }
  Canteiro: { ... }
  Estrutura_Escoramento: { ... }
  ...
  Mobiliario: { ... }
  Bombeamento_extra: { ... }
custo_total_R$: ?
custo_por_m2_R$: (custo_total / 37893.89)
```

## Fluxo de consolidação

1. Memorial de cada disciplina (em `04-disciplinas/{X}/memorial.md`) tem regras de extração
2. Quantitativos extraídos vão pra `04-disciplinas/{X}/quantitativos.json`
3. Script `consolidar_orcamento.py` (a criar): pra cada disciplina, multiplica
   `quantitativos.json` × `composicoes.xlsx`/CPU = custo total da disciplina
4. Resultado vai pra `orcamento.xlsx` consolidado + atualiza este `orcamento-resumo.md`

## Comparativo paramétrico × executivo

- **Paramétrico inicial:** referenciar arquivo `~/orcamentos/parametricos/thozen-electra/` (se existir)
- **Executivo R00:** este orçamento, agregado das 22 disciplinas
- **Variância:** calcular pra cada disciplina (diferença % entre paramétrico e executivo)

## Marco de aprovação

- R00: orçamento executivo inicial — ainda em construção
- R01+: revisões posteriores conforme refinamento dos memoriais
