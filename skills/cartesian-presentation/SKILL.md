---
name: cartesian-presentation
description: Cria apresentações PowerPoint no padrão visual da Cartesian Engenharia, usando python-pptx para gerar arquivos .pptx com a identidade visual, estrutura e melhores práticas observadas nas apresentações da empresa. Use quando precisar criar apresentações comerciais, pitch decks, apresentações de projetos, materiais institucionais ou relatórios executivos em slides para a Cartesian.
---

# Cartesian Presentation Builder

Gera apresentações .pptx profissionais no padrão Cartesian Engenharia usando `python-pptx`.

## Referências (ler antes de gerar)

- `references/identidade-visual.md` — cores, fontes, grafismos, manual de marca, regras do logo
- `references/estrutura-slides.md` — 8 tipos de slide, regras de composição, estruturas pré-definidas
- `references/python-pptx-exemplos.md` — funções prontas (capa, bullets, KPIs, timeline, contato) + exemplo completo
- `references/dados-empresa.md` — números, contatos comerciais, taglines, endereço

## Workflow

### 1. Entender Objetivo

Identificar o tipo de apresentação: comercial (proposta), projeto (kick-off, status), institucional (quem somos), ou pitch (investidor, parceiro). Isso define estrutura e tom.

### 2. Ler Referências

- `references/identidade-visual.md` — cores, fontes, grafismos, regras do logo
- `references/dados-empresa.md` — números atualizados, contatos, taglines
- `references/estrutura-slides.md` — 8 tipos de slide e regras de composição

### 3. Escolher Estrutura

Consultar `estrutura-slides.md` para estruturas pré-definidas por tipo:
- Proposta comercial (6-8 slides)
- Apresentação institucional (5-7 slides)
- Kick-off de projeto (8-10 slides)
- Pitch deck (10-12 slides)

### 4. Gerar Código python-pptx

Usar funções prontas de `references/python-pptx-exemplos.md`, aplicando:
- Paleta oficial: azul `#2F54EB`, preto `#231F20`, branco, vermelho-laranja `#FF3300`
- Fonte Poppins (fallback: Montserrat, Open Sans)
- Grafismo 3D (linhas de perspectiva) como decoração
- Slide 16:9 widescreen

### 5. Validar Contra Checklist

Conferir regras de `estrutura-slides.md` — máx bullets, tamanhos de fonte, espaçamento, logo.

### 6. Salvar e Disponibilizar

Salvar em `documentos/` e enviar via Telegram ou disponibilizar no workspace.

## Regras Essenciais

- Máx 5-6 bullets por slide (regra 6-6-6)
- Um conceito por slide
- Números KPI em 48pt bold, títulos 40pt, corpo 16pt
- Cards com bordas arredondadas e sombra suave
- Espaçamento generoso — slides limpos
- Logo Cartesian na capa (usar asset de `assets/` se disponível)

## Exemplo de Output

Apresentação "Proposta Comercial — Residencial Aquos" (6 slides):
1. **Capa:** Logo Cartesian + título projeto + dados-chave (AC, UR, CUB)
2. **Sobre a Cartesian:** Tagline + números (X projetos, Y m² orçados)
3. **Escopo:** 3 cards (Paramétrico, Executivo, Planejamento)
4. **Metodologia:** Timeline 4 fases com ícones
5. **KPIs do Projeto:** 4 cards com números grandes (R$/m², CUB Ratio, Prazo, Vagas)
6. **Contato:** Foto + nome + email + telefone

Arquivo: `documentos/proposta-aquos.pptx` (16:9, Poppins, paleta Cartesian)

## Mistakes to Avoid

- Usar fonte diferente de Poppins (fallback: Montserrat, Open Sans)
- Mais de 6 bullets por slide (regra 6-6-6)
- Esquecer de aplicar paleta oficial (`#2F54EB`, `#231F20`, `#FFFFFF`, `#FF3300`)
- Colocar logo com proporção errada ou em posição não-padrão
- Slides com texto denso sem espaçamento generoso
- Usar animações (python-pptx não suporta — slides estáticos)
- Gerar sem consultar dados-empresa.md (números e contatos desatualizados)

## Limitações

- Logos/imagens: precisam ser fornecidos como arquivo ou adicionados manualmente
- Fotos de contato: referenciadas mas não incluídas automaticamente
- Animações: python-pptx não suporta (slides estáticos)

## Dependência

```bash
pip install python-pptx
```
