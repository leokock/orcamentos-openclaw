# Orçamento Paramétrico Cartesian

> Sistema de orçamentação paramétrica calibrado com 75 projetos reais (recalibrada 11/mar/2026). Extração de índices: 205 projetos em 5 formatos. Validação: +2% de diferença vs executivo real (Domus).

---

## Visão Geral

O sistema gera planilhas Excel com **14 abas totalmente preenchidas**, com briefing dinâmico (25 dropdowns) que recalculam automaticamente todos os custos para 18 macrogrupos.

**Output:** Planilha `.xlsx` pronta para entregar ao cliente, com dashboard executivo, detalhamento técnico e benchmark comparativo.

---

## Estrutura de Arquivos

```
orcamento-parametrico/
├── indices/                          # Arquivos *-indices.md (205 projetos extraídos)
├── executivos/                       # Planilhas e PDFs dos orçamentos originais
├── parametricos/                     # Planilhas e apresentações geradas
├── docs/                             # Documentação auxiliar e estudos
│   ├── README.md                     # ← Este arquivo (porta de entrada)
│   └── FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md  # Workflow de extração de executivos
├── scripts/
│   ├── gerar_template_dinamico.py    # Gera planilha .xlsx paramétrica (14 abas, briefing dinâmico, dropdowns)
│   └── sync-pacote-drive.sh          # Copia template + calibração para pacote-drive/ (versão offline pro Drive)
├── archive/                          # Versões antigas, templates obsoletos
├── pacote-drive/                     # Versão autocontida para Drive (pode estar desatualizada)
├── calibration-data.json             # Base: 75 projetos normalizados para CUB dez/2023
├── calibration-stats.json            # Medianas, P10, P90 por macrogrupo
├── BRIEFING-PARAMETRICO.md           # 25 perguntas ordenadas por impacto
├── TEMPLATE-INDICES-EXPANDIDO.md     # Template 16 seções para extrair executivos
└── BASE-CONHECIMENTO-PARAMETRICO.md  # Registro textual com índices resumidos
```

---

## Quick Start

### Gerar Paramétrico Novo

```bash
cd ~/clawd/orcamento-parametrico
python3 scripts/gerar_template_dinamico.py
```

**Output:** `<nome-projeto>-parametrico-v1.xlsx` (14 abas, ~2MB)

### Processar Executivo (calibração)

1. Extrair dados do XLSX/PDF
2. Gerar `<nome>-indices.md` (usar `TEMPLATE-INDICES-EXPANDIDO.md`)
3. Atualizar `calibration-data.json`
4. Recalibrar `calibration-stats.json`

### Sincronizar pacote-drive

```bash
bash orcamento-parametrico/scripts/sync-pacote-drive.sh
```

---

## Checklist Rápido — Paramétrico Novo

- [ ] Dados do projeto: AC, UR, NP, NPT, ELEV, VAG, AT
- [ ] Briefing: 9 perguntas críticas respondidas (ver `BRIEFING-PARAMETRICO.md`)
- [ ] Script rodado: `python3 scripts/gerar_template_dinamico.py`
- [ ] 14 abas preenchidas com fórmulas (nenhuma vazia)
- [ ] BRIEFING com dropdowns funcionais
- [ ] BENCHMARK com projetos comparáveis
- [ ] Nenhuma fórmula IFS() (apenas IF aninhado — Excel 2016+)
- [ ] CUB Data-base = data do projeto (NÃO dez/2023)

---

## Checklist Rápido — Novo Executivo (Recalibração)

**Passo a passo para adicionar um novo projeto à base de calibração:**

1. **Extrair dados do executivo** (XLSX ou PDF):
   - AC (área construída), CUB na data-base, total R$
   - Breakdown por macrogrupo (18 MGs)
   - Estrutura de custos: direto vs ADM vs MOE

2. **Gerar arquivo de índices:**
   ```bash
   # Usar template como base
   cp TEMPLATE-INDICES-EXPANDIDO.md indices/<nome>-indices.md
   # Preencher as 16 seções com dados extraídos
   ```

3. **Normalizar valores para CUB dez/2023:**
   ```
   Valor_normalizado = (Valor_original / CUB_projeto) × 2752.67
   ```

4. **Atualizar calibration-data.json:**
   - Adicionar entrada do novo projeto com 18 MGs normalizados
   - Verificar que AC, CUB e total estão corretos

5. **Recalibrar medianas:**
   - Atualizar `calibration-stats.json` (medianas, P10, P90)
   - **Recalibrar IMEDIATAMENTE** — não acumular projetos sem recalibrar

6. **Atualizar contadores:**
   - `BASE-CONHECIMENTO-PARAMETRICO.md` (adicionar registro textual)
   - `BRIEFING-PARAMETRICO.md` (atualizar contagem de projetos calibrados)
   - Este README (contagem na linha 3)

7. **Commit + push:**
   ```bash
   cd ~/orcamentos && git add -A && git commit -m "calibração: adiciona <nome> (N projetos)" && git push
   ```

---

## Documentação Detalhada

| Documento | Conteúdo |
|-----------|----------|
| **`~/clawd/docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`** | Workflow completo (3 fluxos), modelo de cálculo, regras técnicas, lições aprendidas, anomalias |
| **`docs/FRAMEWORK-EXECUTIVO-PARA-PARAMETRICO.md`** | Mapeamento detalhado de macrogrupos, workflow de extração item a item |
| **`BRIEFING-PARAMETRICO.md`** | 25 perguntas do briefing ordenadas por impacto |
| **`TEMPLATE-INDICES-EXPANDIDO.md`** | Template 16 seções para documentar cada executivo |
| **`BASE-CONHECIMENTO-PARAMETRICO.md`** | Registro textual de projetos com índices e PUs |

---

## Regras Críticas (resumo)

- **CUB Data-base** = data informada pelo Leo, NÃO dez/2023
- **Fórmulas:** IF() aninhado, nunca IFS() (compatibilidade Excel 2016+)
- **Recalibração:** sempre após cada novo executivo (não acumular)
- **ADM incorporadora:** não misturar com custos diretos de obra

> Para modelo de cálculo completo, regras técnicas e lições aprendidas: ver `~/clawd/docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md`

---

*Última atualização: 11/03/2026 — v7 (contagens atualizadas: 75 calibrados, 205 extraídos)*
