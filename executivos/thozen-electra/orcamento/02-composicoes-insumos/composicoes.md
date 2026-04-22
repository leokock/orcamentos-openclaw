# Composições de Custo — Visus

## O que é

Uma **composição** representa o custo unitário de um serviço (ex.: "1 m² de alvenaria
de bloco cerâmico"), construído a partir dos insumos que o compõem (bloco, argamassa,
mão de obra de pedreiro, etc.) e suas respectivas quantidades por unidade.

## Origem

Composições são exportadas do **Visus** (software paramétrico Cartesian). Cada
composição tem:

- **Código** (chave única no Visus)
- **Descrição**
- **Unidade** (m², m³, un, vb, etc.)
- **Insumos** (lista de insumo + quantidade)
- **Custo unitário total** (calculado por preço × quantidade dos insumos)

## Arquivos nesta pasta

- `composicoes.xlsx` — cópia da aba "Composições" do template R00 (~3.200 linhas estimadas)
- `insumos.xlsx` — cópia da aba "Insumos" (catálogo de itens individuais com preço)
- `cpu.xlsx` — cópia da aba "CPU" (Custo Por Unidade — pré-calculados por composição)
- `insumos-precos.json` — *a gerar*: insumo → preço atualizado (machine-readable pra Claude)
- `composicoes.md`, `insumos.md` — explicações

## Critério de preço

- Preços base: catálogo Cartesian R00 (mercado SC/Itapema)
- Atualização: **CUB/SC** (Sinduscon) — não INCC
- Revisar a cada 3-6 meses ou em revisão R01

## Cruzamento com EAP

Cada serviço da EAP (folha) referencia 1 ou mais composições. O orçamento final
é montado multiplicando **quantidade extraída** (do projeto) × **custo unitário**
(da composição).

## Workflow

1. Receber Composições/Insumos/CPU atualizados do Visus
2. Substituir os 3 xlsx desta pasta
3. Rodar conversor pra gerar `insumos-precos.json`
4. Memorial de cada disciplina cita as composições usadas (ex.: `cod_composicao: "ALV-001"`)
