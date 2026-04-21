# Electra Towers — Orcamento Executivo

**Cliente:** Thozen Empreendimentos
**Tipologia:** Residencial vertical — 2 torres, 34 pavimentos cada
**AC:** 36.088,85 m² | **Unidades:** 348 | **Vagas:** 305
**Planilha ativa:** `CTN-TZN_ELT - Orçamento Executivo_R00_Leo rev01.xlsx`

---

## Navegacao Rapida

| Doc | Pra que serve |
|-----|---------------|
| [[gestao-orcamento-electra]] | Checklist de preenchimento + duvidas pendentes |
| [[log-execucao]] | Historico tecnico por disciplina — vira memorial final |
| [[PROJETO]] | Dados do projeto, disciplinas, arquivos fonte |
| [[COMECE-AQUI]] | Primeiro acesso — por onde comecar |

---

## Pastas

| Pasta | Conteudo |
|-------|----------|
| `briefings/` | Briefings por disciplina (.md) — 14 disciplinas, R00 a R02 |
| `disciplinas/` | Planilhas executivas por disciplina (.xlsx) — 16 subpastas |
| `eap/` | EAP v3 definitiva (4 UCs x pavimentos) + tecnico-adm |
| `orcamento/` | Versoes consolidadas R00 a R03 + quantitativos detalhados |
| `memoriais/` | Memoriais e briefings Word (.docx) |
| `quantitativos/` | JSONs consolidados (eletrico, pci, telefonico, alvenaria) |
| `scripts/` | Scripts Python de extracao e processamento |
| `dados/` | Dados auxiliares |
| `fontes/` | Arquivos fonte referenciados |
| `logs/` | Logs de processamento |

---

## Estrategia de Extracao (10/abr/2026)

| Fonte | Itens | Responsavel |
|-------|-------|-------------|
| **BIM (Visus)** | Paredes, revestimentos, acabamentos, pisos, tetos, pintura, esquadrias, fachada (13 macrogrupos) | Leo |
| **Planilha (IA)** | Hidro, eletrico, telecom, PCI, estrutura, HVAC, loucas/metais (13 disciplinas) | Claude + Leo |
| **Indices** | Ger. Tec/Adm, canteiro, cont. tecnologico, EPCs, mobiliario (8 itens) | Claude |

Fluxo: Visus (BIM) + Planilha (IA/indices) → Excel completo → importa de volta no Visus

---

## Disciplina → N1 Memorial Cartesiano

| Disciplina | N1 Memorial |
|------------|-------------|
| 01 Estrutura | 03 Infraestrutura + 04 Supraestrutura |
| 02 Arquitetura | (Referencia — fonte de areas) |
| 03 Alvenaria | 09 Alvenaria |
| 04 Esquadria | 13 Esquadrias |
| 05 Hidraulico | 06.01 Agua Fria |
| 06 Sanitario | 06.02 Esgoto + 06.03 Aguas Pluviais |
| 07 PCI Civil | 14.01 PCI Civil |
| 08 PCI Eletrico | 14.01 PCI Eletrico |
| 09 Eletrico | 07.01 Instalacoes Eletricas |
| 10 Telefonico | 14.09 Telefonia/Dados |
| 11 SPDA | 07.02 SPDA |
| 12 Ventilacao | 14.08 Ventilacao Mecanica |
| 13 Exaustao | 14.08 Exaustao |
| 14 Ar-Condicionado | 14.02 Climatizacao |

---

*Atualizado: 10/04/2026*
