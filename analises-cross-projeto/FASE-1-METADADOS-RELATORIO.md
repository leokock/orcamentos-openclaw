# Fase 1 — Enriquecimento de Metadados — Relatório

**Gerado em:** 2026-04-18
**Duração total:** 35 min de processamento Gemma + 30s enriquecimento
**Entrada:** 7 projetos `_Projetos_IA/` + 126 executivos + padrões classificados
**Saída:** `base/projetos-enriquecidos.json` (131 projetos consolidados)

---

## Cobertura alcançada

| Campo | Cobertura | Fonte principal |
|---|---:|---|
| **Padrão construtivo** | **98%** (128/131) | `padroes-classificados-consolidado.json` |
| **Cidade** | **100%** (131/131) | Mapa manual slug → cidade + Gemma + inferência |
| **UF** | **100%** (131/131) | Mapa manual + inferência |
| **CUB região** | **100%** (131/131) | Mapa manual (SC subdividido em 5 regiões) |
| Área construída (AC) | 76% (99/131) | `indices-executivo.ac` |
| Total R$ | 58% (76/131) | `indices-executivo.total` |
| Taxa aço (kg/m³) | 56% (73/131) | `indices-executivo.indices_estruturais` |
| Sistema estrutural | 53% (70/131) | Gemma de memoriais |
| Concreto m³/m² | 42% (55/131) | `indices-executivo.indices_estruturais` |
| UR | 26% (34/131) | Mix |
| Tipologia canônica | 17% (22/131) | Gemma (precisa Fase 3 dedicada) |
| N pavimentos total | 8% (11/131) | Gemma (precisa reprocessar) |

### Distribuição geográfica

**Por UF:**
- SC: 116 projetos (89%)
- SP: 5
- RS: 4
- PR: 2
- MG: 1
- outros: 3

**Por CUB região (SC subdividido):**
| Região | N projetos | % |
|---|---:|---:|
| SC-Floripa | 35 | 27% |
| SC-Vale-Itajaí | 33 | 25% |
| SC-Balneário Camboriú | 29 | 22% |
| SC-Litoral Norte | 13 | 10% |
| SC-Oeste (Chapecó) | 3 | 2% |
| SC-Outros | 3 | 2% |
| SP-Capital | 5 | 4% |
| RS-Serra | 4 | 3% |
| PR-Litoral | 1 | <1% |
| PR-Capital | 1 | <1% |
| Outros | 4 | 3% |

### Distribuição por padrão
- Alto: 57 projetos (44%)
- Médio-alto: 61 projetos (47%)
- Médio: 4 (3%)
- Econômico: 4 (3%)
- Insuficiente: 1
- Desconhecido: 3

---

## Decisões metodológicas

### 1. Mapa manual de slug → cidade/UF
Gemma extraiu cidade de apenas 19/131 (14%) a partir dos memoriais. Isso era ruim. **Decisão:** criar mapa manual dos clientes conhecidos da Cartesian (78 prefixos de slug → cidade/UF). Cobertura subiu pra 100%.

**Trade-off aceito:** mapa manual requer manutenção quando novos clientes entram. Alternativa seria Qwen inferir de contexto amplo, mas demoraria horas e teria ruído.

### 2. Booleans conservadores
Gemma tendia a marcar `tem_pele_vidro: false` por omissão (não-menção ≠ ausência). **Decisão:** só preservar `True` (evidência explícita). `False` vira `None` (não declarado). Resultado: cobertura de booleans caiu muito mas **qualidade subiu** — quando diz True, é confiável.

**Campos afetados:**
- tem_pele_vidro: 0/131 True (esperado ~10-20% em alto padrão, mas sem evidência clara dos PDFs)
- tem_piscina: 2/131 True
- tem_gerador: 6/131 True
- tem_spda: 2/131 True
- tem_climatizacao_central: 3/131 True
- tem_subsolo: 7/131 True
- tem_churrasqueira_apto: 2/131 True

### 3. CUB regional como proxy de custo local
CUB do Sinduscon varia entre regiões. Criei mapeamento (UF, cidade) → região CUB canônica (ex: SC subdivido em Floripa/Vale Itajaí/BC/Litoral Norte/Oeste). Pra análise regressional, `cub_regiao` é feature mais útil que UF pura.

### 4. Dados estruturais vêm de `indices-executivo`, não Gemma
Gemma cobria só 6% de n_pavimentos e similar baixo pra fck. Mas `indices-executivo.indices_estruturais` já tem concreto_m3_m2, taxa_aco, forma, estacas pra muitos projetos. **Decisão:** preferir `indices-executivo`; Gemma só complementa quando falta.

---

## Projeto individual enriquecido — exemplo

`base/projetos-enriquecidos/thozen-electra.json`:
```json
{
  "slug": "thozen-electra",
  "cliente_inferido": "thozen",
  "padrao": "alto",
  "tipologia_gemma": "residencial_multifamiliar",
  "cidade": "Balneário Camboriú",
  "uf": "SC",
  "cub_regiao": "SC-BC",
  "ac_m2": 37893.89,
  "ur": null,
  "concreto_m3_m2_ac": ...,
  "n_pavimentos_total": 32,
  "tem_metadados_gemma": true,
  ...
}
```

---

## Limitações conhecidas da Fase 1

1. **16 projetos sem fontes textuais** (fontes vazias) — principalmente projetos com `_Projetos_IA/` vazio e `qualitative` mínimo. Afeta `tem_metadados_gemma=false` pra esses.
2. **N pavimentos cobertura 8%** — PDFs escaneados de plantas não foram lidos como texto. Melhoria futura: usar OCR em DWG/PDF de plantas.
3. **Tipologia fina (17%)** — Fase 3 atacará isso com prompt dedicado + controle por padrão.
4. **Cidade com heurística** — mapa manual pode errar em clientes novos. Validar com Patricia ou Leo antes de usar em decisão comercial.

---

## Impacto para próximas fases

### Fase 2 — Normalização Localização
Objetivo original: 100% cobertura. **Atingido** via mapa manual. ✓ Pode pular pra Fase 3.

### Fase 3 — Classificação Tipologia
Apenas 17% têm tipologia Gemma. Rodar script dedicado com prompt:
```
Dado cliente + padrão + AC + UR + observações, classifique em:
- residencial_vertical_economico|medio|medio_alto|alto|luxo
- residencial_misto|comercial|lajes_corporativas|casa_condominio|industrial
```

### Fase 4 — Re-rodar análises
Com `cub_regiao` e `tipologia` por projeto, os benchmarks atuais (só por padrão) ganham 2 dimensões extras. Análise fica muito mais útil:
- "R$/m² alto padrão em Balneário Camboriú" vs em Florianópolis
- "Distribuição MG tipologia A vs B no mesmo padrão"

### Fase 5 — Correlações
Agora com CUB região podemos testar: `r(rsm2, ac | cub_regiao)` — correlação controlada. Antes era impossível.

### Fase 6 — Decomposição R$/m²
Agora temos 4 variáveis independentes: AC, padrão, cub_regiao, tipologia. Regressão multivariada viável.

---

## Próximos passos concretos

1. **Próxima noite**: rodar Fase 3 (classificar tipologia) — script dedicado
2. **Depois**: Fase 4 (re-rodar 3 análises principais com enriquecimento)
3. **Decisão pendente**: vale investir OCR em PDFs de planta pra n_pavimentos? Ou extrair de IFC direto?

---

## Arquivos gerados

- `base/projetos-enriquecidos.json` — 131 projetos consolidados + stats
- `base/projetos-enriquecidos/{slug}.json` — 131 arquivos individuais
- `base/metadados-projeto/{slug}.json` — 117 projetos com extração Gemma
- `base/metadados-queue.json` — fila de processamento
- `base/metadados-extracao.log.jsonl` — log append-only
- `scripts/extrair_metadados_projeto.py` — pipeline Gemma
- `scripts/enriquecer_metadados.py` — consolidador + inferência cidade
