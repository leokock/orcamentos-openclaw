# EAP — Estrutura Analítica do Projeto

## O que é

A **EAP** (Estrutura Analítica do Projeto) organiza o orçamento numa árvore hierárquica
que parte de unidades construtivas grandes e desce até serviços específicos. É a espinha
dorsal de rastreabilidade do orçamento executivo Cartesian.

## Hierarquia

| Nível | Nome | Exemplo |
|---|---|---|
| 1 | **Unidade Construtiva** | Gerenciamento Técnico e Administrativo, Infraestrutura, Supraestrutura |
| 2 | **Célula Construtiva** | Serviços Técnicos, Topografia, Sondagem |
| 3 | **Etapa** | Estudos, Projetos e Consultorias |
| 4 | **Subetapa** | Estudos preliminares, Projeto legal, Projeto executivo |
| 5+ | **Serviço** | (Folha do orçamento — vem das composições) |

## Codificação

- **Unidade:** 1 dígito (1, 2, 3, …)
- **Célula:** 1-2 dígitos (1, 2, …)
- **Etapa:** N.NNN (ex.: 1.001, 1.002)
- **Subetapa:** NN.NNN.NNN (ex.: 01.001.001)

## Arquivos nesta pasta

- `eap.xlsx` — vista Excel pra navegação humana (cópia da aba EAP do template R00)
- `eap.json` — versão estruturada (a gerar — ver script `eap_xlsx_to_json.py`)
- `eap.md` — este arquivo

## Workflow

1. Ao receber a EAP nova do Visus, substituir `eap.xlsx`
2. Rodar conversor → atualizar `eap.json`
3. Memoriais das disciplinas referenciam IDs de subetapa (ex.: `subetapa: "07.003.012"`) pra rastrear de onde sai cada quantitativo na árvore
