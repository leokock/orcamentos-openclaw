# Orçamento Executivo — Thozen Electra

Este diretório contém o **orçamento executivo completo** do empreendimento Electra Towers,
estruturado como template reutilizável pra orçamentos futuros da Cartesian.

> **📊 Painel mestre de progresso:** ver [Estrutura do orçamento.md](Estrutura%20do%20orçamento.md)
> (atualizado automaticamente, mostra status de cada disciplina)

## Estrutura

```
orcamento/
├── README.md                          ← este arquivo
├── Estrutura do orçamento.md          ← idea original + checklist de progresso
│
├── 00-projeto/                        IDENTIDADE DA OBRA (humano edita)
│   ├── projeto.md                     metadados: cliente, endereço, proprietário, RT
│   ├── areas.md                       quadro de áreas + índices urbanísticos
│   ├── pavimentos.md                  tabela de pavimentos (por torre)
│   ├── apartamentos.md                tipologias + vagas/dorm por apto
│   ├── lazer.md                       áreas comuns detalhadas + elevadores
│   ├── vagas.md                       quadro de vagas (simples/duplas)
│   └── projeto.json                   ⚙ consolidado machine-readable (gerado)
│
├── 01-eap/                            ESTRUTURA ANALÍTICA DO PROJETO
│   ├── eap.md                         critério de WBS Cartesian
│   └── eap.xlsx                       vista Excel (cópia da aba EAP do template)
│
├── 02-composicoes-insumos/            CATÁLOGO DE CUSTOS (do Visus)
│   ├── composicoes.md                 o que é composição + critério de preço
│   ├── composicoes.xlsx               cópia aba Composições
│   ├── insumos.md                     o que é insumo + hierarquia de preço
│   ├── insumos.xlsx                   catálogo de insumos com preço
│   └── cpu.xlsx                       Custo Por Unidade pré-calculado
│
├── 03-orcamento-resumo/               VISÃO CONSOLIDADA
│   ├── orcamento-resumo.md            comparativo paramétrico × executivo
│   └── orcamento.xlsx                 aba Orçamento do template
│
├── 04-disciplinas/                    22 PASTAS DE TRABALHO
│   ├── EPCs/
│   │   ├── memorial.md                regras de extração + fontes
│   │   ├── extracao.xlsx              planilha enxuta (Dados Base + EAP + extração)
│   │   └── quantitativos.json         ⚙ dados extraídos (a gerar)
│   ├── Canteiro/
│   ├── Controle tecnológico/
│   ├── Esquadrias/
│   ├── Estacas/
│   ├── Fund. Rasa e Contenção/
│   ├── Estrutura e Escoramento/
│   ├── Impermeabilização/
│   ├── Louças e metais/
│   ├── Piscina/
│   ├── Equipamentos especiais/
│   ├── Elétrico/
│   ├── Hidrossanitário/
│   ├── PPCI/
│   ├── Sprinklers/
│   ├── Telecomunicação/
│   ├── Gás/
│   ├── Automação/
│   ├── Climatização/
│   ├── Iluminação/
│   └── Mobiliário/
│
└── 05-extras/
    └── Bombeamento/
```

## Convenções

- **`.md`** = humano edita; Claude lê pra contexto narrativo
- **`.json`** = machine-readable (consumo direto por scripts/Claude)
- **`.xlsx`** = vistas e planilhas operacionais

## Workflow

### Ao iniciar nova obra (clonar template)
1. Copiar toda estrutura `00-*/` `01-*/` `02-*/` `03-*/` `04-*/` `05-*/` pra pasta nova
2. Preencher os 6 mds em `00-projeto/` com dados da obra
3. Rodar `consolidar_projeto.py` → gera `00-projeto/projeto.json`
4. Importar do Visus: `eap.xlsx`, `composicoes.xlsx`, `insumos.xlsx`, `cpu.xlsx`, `orcamento.xlsx`
5. Rodar `gerar_planilhas_executivo.py` → popula 22 planilhas em `04-disciplinas/`
6. Trabalhar disciplina por disciplina seguindo memorial.md de cada

### Quando dado da obra muda (revisão R01)
- Leo edita md afetado em `00-projeto/`
- Roda `consolidar_projeto.py` → projeto.json atualizado
- Roda `gerar_planilhas_executivo.py` → planilhas regeneradas
- Memoriais.md preservados (write-once)

## Scripts

Localizados em `C:\Users\leona\openclaw\orcamento-parametrico\scripts\`:

| Script | Função |
|---|---|
| `consolidar_projeto.py` | 6 mds → projeto.json + validação schema |
| `projeto-schema.json` | schema de validação |
| `extrair_abas_template.py` | extrai abas do template pra xlsx standalone em 01-*/02-*/03-* |
| `gerar_pastas_executivo_electra.py` | gera as 22 planilhas em 04-disciplinas/ (a refatorar p/ ler de projeto.json) |
| `mapping-disciplinas-electra.json` | mapping disciplina → abas fonte |

## Status (atualizado 2026-04-21)

### ✅ Fase 1 — Doc central concluída
- `00-projeto/` com 6 mds preenchidos (dados oficiais Electra)
- `projeto.json` consolidado e validado contra schema
- `01-eap/`, `02-composicoes-insumos/`, `03-orcamento-resumo/` com xlsx extraídos do template

### ✅ Fase 2 — Planilhas regeneradas concluída
- 22 disciplinas em `04-disciplinas/` + 1 extra em `05-extras/`
- Cada pasta com `extracao.xlsx` + `memorial.md`
- CAPA de todas as 22 planilhas com dados oficiais Electra (projeto, áreas, pavimentos, vagas, etc.)
- Scripts antigos removidos (`CTN-TZN_ELT_*.xlsx` → lixeira)

### ✅ Fase 2b — Tabela pavimentos + JSONs auxiliares concluída
- Tabela CAPA!B19:G29 populada com 11 linhas da Electra (2 torres + embasamento + cobertura)
- `01-eap/eap.json` gerado (372 subetapas, 68.8 KB)
- `02-composicoes-insumos/insumos-precos.json` gerado (992 insumos, 278.7 KB)
- Script `converter_auxiliares_json.py` criado pra conversão xlsx→JSON

### 🚧 Fase 3+ — Pendente
- Memoriais detalhados: 2/22 (EPCs ✅, Equipamentos Especiais ✅)
- Composições xlsx → JSON (ainda não convertido — esquema das composições é mais complexo, deixar pra quando precisar consumir)
- Skill `~/clawd/skills/orcamento-executivo/` — só destilar após 5-6 disciplinas trabalhadas

## Como usar

### Regenerar planilhas depois de alterar dados do projeto

```bash
# 1. Editar md afetado em 00-projeto/
# 2. Consolidar
cd ~/openclaw
python -X utf8 orcamento-parametrico/scripts/consolidar_projeto.py

# 3. Regenerar planilhas
python -X utf8 orcamento-parametrico/scripts/gerar_pastas_executivo_electra.py
```

### Regenerar só uma disciplina

```bash
python -X utf8 orcamento-parametrico/scripts/gerar_pastas_executivo_electra.py --only EPCs
```

### Re-extrair EAP/composições/insumos do template

```bash
python -X utf8 orcamento-parametrico/scripts/extrair_abas_template.py
```

### Regenerar JSONs machine-readable (eap.json, insumos-precos.json)

```bash
python -X utf8 orcamento-parametrico/scripts/converter_auxiliares_json.py
```

### Atualizar painel mestre (`Estrutura do orçamento.md`)

```bash
python -X utf8 orcamento-parametrico/scripts/atualizar_painel.py
```

### Gerar quantitativos finais de uma disciplina

```bash
# Exemplo: Canteiro
python -X utf8 orcamento-parametrico/scripts/gerar_quantitativos_canteiro.py
# Depois atualizar o painel:
python -X utf8 orcamento-parametrico/scripts/atualizar_painel.py
```

## Referência

Ver plano: `~/.claude/plans/g-drives-compartilhados-03-ctn-projetos-rippling-axolotl.md`
