---
name: gerar-apresentacao-orcamento
description: Use quando precisar gerar uma apresentacao pptx de orcamento (parametrico ou executivo) para apresentar ao cliente. Trigger quando mencionarem "gera a apresentacao", "faz os slides do orcamento", "preciso da apresentacao pro cliente", "monta o pptx".
---

# Gerar Apresentacao de Orcamento

Cria apresentacao .pptx de orcamento no padrao visual Cartesian para apresentacao ao cliente.

**Pre-requisito:** Ler skill `cartesian-presentation` para identidade visual, cores, fontes e estrutura de slides.

## Estrutura de Slides — Orcamento

### Slides obrigatorios:

1. **Capa** — Nome do projeto, cliente, data, logo Cartesian
2. **Dados do empreendimento** — AC, UR, pavimentos, tipologia, localizacao
3. **Resumo executivo** — Total, R$/m2, CUB ratio, comparativo com base
4. **Distribuicao por macrogrupo** — Grafico pizza ou barras (18 macrogrupos)
5. **Top macrogrupos** — 5-6 maiores com R$/m2 e % do total
6. **Benchmark** — Comparativo com projetos similares (ANONIMIZADOS)
7. **Observacoes e premissas** — O que foi assumido, fontes de dados
8. **Proximos passos** — Acoes recomendadas, validacoes pendentes
9. **Contato** — Equipe Cartesian, canais de comunicacao

### Slides opcionais (se dados disponiveis):

- **Agravantes e oportunidades** — Destaques vs base
- **Cronograma macro** — Fases da obra
- **Curva ABC** — Top insumos
- **Detalhamento por disciplina** — 1 slide por disciplina relevante

## Fluxo

### 1. Coletar dados

Ler orcamento gerado (xlsx ou json em output/):
```bash
ls output/[projeto]*.xlsx output/[projeto]*.json
```

Extrair: AC, total, R$/m2, macrogrupos, benchmark.

### 2. Gerar pptx

Usar `python-pptx` seguindo padroes da skill `cartesian-presentation`:
- Fonte: Poppins (titulos), Inter/Arial (corpo)
- Cores: Azul Cartesian #1B365D, Accent #2980B9
- Logo: `skills/cartesian-presentation/assets/logo-cartesian.png`

### 3. Regra de confidencialidade

**CRITICO:** Em QUALQUER apresentacao para cliente externo, NUNCA usar nomes reais de outros projetos no benchmark.

Substituir por tipologia + cidade:
- "Maison Beach" → "Resid. Multifamiliar Alto Padrao — Florianopolis"
- "Catena" → "Resid. Multifamiliar Medio Padrao — Florianopolis"

Header da tabela: "Tipologia" (nao "Projeto")
Subtitulo: "base de dados" (nao "base Cartesian")

### 4. Salvar e upload

```bash
# Salvar
output/[projeto]-apresentacao-orcamento.pptx

# Upload na thread do Slack
python3.11 scripts/slack_uploader.py \
  --bot cartesiano \
  --file output/[projeto]-apresentacao-orcamento.pptx \
  --thread [thread_ts] \
  --channel [channel_id] \
  --comment "Apresentacao orcamento — [projeto]"
```

**SEM UPLOAD = ENTREGA NAO FEITA**

## Regras

- SEMPRE anonimizar projetos no benchmark
- SEMPRE incluir slide de premissas (transparencia)
- SEMPRE fazer upload na thread
- NUNCA colocar dados internos da Cartesian (margens, custos operacionais)
- Preferir graficos simples e limpos — menos e mais
