# Orçamento Paramétrico — Cartesian Engenharia

> ⚠️ **ATENÇÃO: Os arquivos neste pacote podem estar desatualizados.**
> Fonte atualizada: `orcamento-parametrico/` no workspace principal (`~/clawd/orcamento-parametrico/`).
> Para sincronizar, execute: `bash orcamento-parametrico/scripts/sync-pacote-drive.sh`

> Pasta autocontida para geração de orçamentos paramétricos e processamento de orçamentos executivos.
> Usar com Claude Code ou Claude Cowork. Abrir esta pasta como projeto.

---

## O Que É

Sistema de orçamentação paramétrica calibrado com **250 projetos extraídos** (75 calibrados, 131 com AC válido) de construção civil — edifícios residenciais multifamiliares. Gera estimativas de custo baseadas em dados estatísticos reais da Cartesian.

**Dois produtos:**
1. **Paramétrico Cartesian** — para cidades com base consolidada (3+ executivos). Entrega preço médio de mercado baseado em amostra real
2. **Paramétrico Estrutural** — para cidades sem base consolidada. Usa índices percentuais calibrados + preços unitários captados localmente

---

## Estrutura da Pasta

```
orcamento-parametrico/
├── indices/                ← arquivos *-indices.md (65 projetos indexados)
├── executivos/             ← planilhas e PDFs dos orçamentos originais recebidos
├── parametricos/           ← planilhas e apresentações geradas (paramétricos)
├── docs/                   ← documentação auxiliar e estudos
├── scripts/                ← scripts Python ativos
├── archive/                ← versões antigas, templates obsoletos, duplicatas
├── pacote-drive/           ← ESTA PASTA — versão autocontida para o Drive
├── calibration-data.json   ← base de calibração (75 projetos)
├── calibration-stats.json  ← estatísticas calculadas (medianas, médias, min/max)
├── BASE-CONHECIMENTO-PARAMETRICO.md  ← registro textual de todos os projetos
└── BRIEFING-PARAMETRICO.md           ← 25 perguntas ordenadas por impacto
```

---

## Arquivos Importantes (nesta pasta)

| Arquivo | O que é |
|---------|---------|
| `gerar_template_dinamico.py` | Script Python que gera a planilha Excel (.xlsx) com 14 abas |
| `calibration-data.json` | Base de calibração (75 projetos com macrogrupos, R$/m², CUB ratio) |
| `calibration-stats.json` | Estatísticas calculadas (medianas, médias, min/max por macrogrupo) |
| `BRIEFING-PARAMETRICO.md` | 25 perguntas do briefing ordenadas por impacto no custo |
| `BASE-CONHECIMENTO-PARAMETRICO.md` | Registro textual de todos os projetos com índices resumidos |
| `FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` | Workflow para converter executivo real em índices paramétricos |
| `TEMPLATE-INDICES-EXPANDIDO.md` | Template com 16 seções para extrair índices de executivos |
| `MAPA-COBERTURA.md` | Cidades com base consolidada (verde/amarelo/vermelho) |
| `ESTRATEGIA-DOIS-TIERS.md` | Documentação dos dois tiers de produto paramétrico |

Os MDs por categoria (ALVENARIA.md, INSTALAÇÕES.md, etc.) contêm detalhamento de classificação de itens por macrogrupo — úteis como referência ao processar executivos.

---

## Comandos

```bash
# Gerar planilha paramétrica (requer Python 3.11 + openpyxl)
python3.11 gerar_template_dinamico.py

# Instalar dependência (se necessário)
pip3.11 install openpyxl
```

---

## Fluxo 1 — Gerar Paramétrico Novo (projeto sem executivo)

1. Receber PDF/plantas do projeto
2. Extrair dados do programa (ver seção 2 do `BRIEFING-PARAMETRICO.md`)
3. Responder as perguntas do briefing (ordenadas por impacto: laje → padrão → contenção → prazo → subsolos)
4. Verificar em `MAPA-COBERTURA.md` se a cidade tem base consolidada
   - 🟢 Base consolidada → gerar paramétrico padrão
   - 🟡/🔴 Sem base → usar Paramétrico Estrutural (ver `ESTRATEGIA-DOIS-TIERS.md`)
5. Rodar `python3.11 gerar_template_dinamico.py`
6. Revisar planilha gerada e validar com benchmark

---

## Fluxo 2 — Processar Orçamento Executivo (calibração)

1. Receber planilha XLSX do orçamento executivo + apresentação PDF/PPTX
2. Seguir o `FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md` passo a passo
3. Classificar itens nos 18 macrogrupos paramétricos
4. Gerar arquivo `<nome-projeto>-indices.md` usando o `TEMPLATE-INDICES-EXPANDIDO.md`
5. Registrar na `BASE-CONHECIMENTO-PARAMETRICO.md`
6. Atualizar `calibration-data.json` com os dados do novo projeto
7. Recalibrar `calibration-stats.json` (recalcular medianas)
8. Salvar os arquivos atualizados na subpasta `atualizacoes/` para consolidação posterior no Drive

---

## Modelo de Cálculo

```
Valor Final = Base R$/m² (mediana dez/23) × Fator CUB × Fator Briefing
```

- **Base R$/m²**: mediana da base de calibração por macrogrupo (referência dez/2023)
- **Fator CUB**: CUB Atual / CUB Base (2.752,67) — atualização monetária uniforme
- **Fator Briefing**: multiplicadores das respostas do briefing (laje, padrão, contenção, etc.)
- Sub-itens nas abas de detalhe = distribuição percentual do macrogrupo (não têm preço independente)
- PUs calculados automaticamente: `PU = Total / Qtd`

---

## 18 Macrogrupos Paramétricos

1. Gerenciamento Técnico/Admin
2. Movimentação de Terra
3. Infraestrutura (fundações)
4. Supraestrutura (forma + aço + concreto)
5. Alvenaria
6. Impermeabilização
7. Instalações (hidro + elétrica + preventiva + gás + telecom)
8. Sistemas Especiais (elevadores, piscina, ETE)
9. Climatização
10. Revestimentos Internos de Parede
11. Teto (forro)
12. Pisos e Pavimentações
13. Pintura
14. Esquadrias
15. Louças e Metais
16. Fachada
17. Complementares
18. Imprevistos

---

## Regras Críticas

- **CUB Data-base** = data informada pelo usuário (ex: "fev/2026"), NÃO dez/2023
- **Nenhuma fórmula IFS()** — usar apenas IF() aninhado (compatibilidade Excel 2016+)
- **Churrasqueiras** → Alvenaria (não Complementares)
- **Piso polido garagem** → Supraestrutura (não Pisos)
- **Pintura epóxi garagem** → Pintura (não Supraestrutura)
- **Instalações** = SEMPRE agrupar 5 subgrupos (hidro, elétrica, preventiva, gás, telecom)
- **Climatização** separada de Sistemas Especiais

---

## Entrega Padrão (checklist)

- [ ] 14 abas (todas preenchidas com fórmulas, nunca vazias)
- [ ] BRIEFING com dropdowns que recalculam a planilha toda
- [ ] Abas de detalhe (ESTRUTURAL, INSTALAÇÕES, ACABAMENTOS, CI) com itens, quantidades e PUs conectados
- [ ] BENCHMARK com projetos comparáveis — CUB Ratio (atemporal) + R$/m² Atual (convertido)

---

## Atualização

Esta pasta é sincronizada periodicamente com o Drive. Sempre verificar se há versão mais recente antes de iniciar um trabalho.

Ao processar um executivo novo, salvar o arquivo `<nome>-indices.md` e o `calibration-data.json` atualizado na subpasta `atualizacoes/` para consolidação posterior.

---

*Versão: 11/mar/2026 | Base: 250 projetos extraídos (5 formatos) | Calibração: 75 projetos em calibration-data.json | 508 índices únicos*
