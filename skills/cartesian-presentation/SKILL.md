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

1. Entender objetivo (comercial, projeto, institucional, pitch)
2. Escolher estrutura pré-definida ou customizada (ver `estrutura-slides.md`)
3. Gerar .pptx usando as funções de `python-pptx-exemplos.md`, aplicando:
   - Paleta oficial: azul `#2F54EB`, preto `#231F20`, branco, vermelho-laranja `#FF3300`
   - Fonte Poppins (fallback: Montserrat, Open Sans)
   - Grafismo 3D (linhas de perspectiva) como decoração
   - Slide 16:9 widescreen
4. Validar contra checklist (ver `estrutura-slides.md`)
5. Salvar e disponibilizar

## Regras Essenciais

- Máx 5-6 bullets por slide (regra 6-6-6)
- Um conceito por slide
- Números KPI em 48pt bold, títulos 40pt, corpo 16pt
- Cards com bordas arredondadas e sombra suave
- Espaçamento generoso — slides limpos
- Logo Cartesian na capa (usar asset de `assets/` se disponível)

## Limitações

- Logos/imagens: precisam ser fornecidos como arquivo ou adicionados manualmente
- Fotos de contato: referenciadas mas não incluídas automaticamente
- Animações: python-pptx não suporta (slides estáticos)

## Dependência

```bash
pip install python-pptx
```
