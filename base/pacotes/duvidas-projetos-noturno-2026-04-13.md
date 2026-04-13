# Dúvidas — Noite de geração 2026-04-13

**3 projetos a serem gerados como Pacote Paramétrico → Executivo**

Cada projeto tem sua seção. Todas as perguntas têm **default sugerido** (entre parênteses). Basta responder apenas as que discordar do default. As que não responder eu uso o default.

Pode responder ao longo do dia — só preciso de tudo antes das 23h.

---

## 📊 Resumo dos 3 projetos

| Projeto | AC (est.) | UR (est.) | Padrão | Cidade | Total est. (cal.) | R$/m² |
|---|---|---|---|---|---|---|
| thozen-electra | 36.000 | 348 | alto | ? | R$ 111M | 3.094 |
| arthen-arboris | 12.472 | 98 | médio | Itapema/SC | R$ 35M | 2.813 |
| placon-arminio-tavares | ~4.500 | 55 | médio | Florianópolis/SC | R$ 12.7M | 2.813 |

**Total estimado dos 3 pacotes:** ~R$ 158.7M

---

## ⚠️ 3 decisões cruzadas antes das perguntas específicas

### D1. Arthen Arboris — refazer paramétrico ou só executivo?

O Arthen já tem um paramétrico V2 gerado (`arthen-arboris-parametrico-v2.xlsx`) e análise completa (10 sheets). Opções:

- **(a)** Rodar o pacote completo (paramétrico novo + executivo) — **substitui** o v2 existente pelo novo v2.1 enriquecido com camada qualitativa
- **(b)** Manter paramétrico atual, gerar só o executivo
- **(c)** Gerar paramétrico novo mas preservar o anterior como `-v2-backup.xlsx`

**Default sugerido:** **(c)** — melhor dos dois mundos. Backup e versão nova.

### D2. Thozen Electra — escala grande, cabe no fluxo?

Thozen tem 36.000 m², 348 UR, 2 torres, 32 pavimentos. É o maior projeto da base Cartesian. O pacote vai rodar normalmente, mas a execução humana (validação do gate, revisão do output) vai demandar **mais tempo** pra Thozen do que os outros 2 juntos.

**Default sugerido:** **seguir com os 3**. Se ficar apertado na madrugada, Thozen tem prioridade 2 (depois dos outros 2 que são menores).

### D3. Placon — estimativa de AC e UR

Do Quadro NBR I eu consegui extrair **55 unidades** e **17 pavimentos** confirmados. Mas a AC total está como estimativa (~4500 m²) porque pypdf quebrou a estrutura tabular.

**Defaults sugeridos** baseados na soma parcial dos pavimentos visíveis:
- AC = 4.500 m²
- UR = 55 (confirmado)
- NP = 17 (confirmado)
- NPT = 9 (dedução: pavimentos tipo são 3-6 + 12-16, e alguns singles; total ~9)

**Precisa confirmar:** AC total real. Posso re-extrair dos quadros se tiver um memorial com o número explícito, ou você me passa.

---

## 🏢 Projeto 1 — Thozen Electra

**Slug:** `thozen-electra`
**Pasta:** `G:\...\_Projetos_IA\thozen-electra`
**Arquivos encontrados:** 14 disciplinas, ~1.8 GB (DWG + IFC completos), NO memorial descritivo
**Similares identificados:** beco-castelo-chateau-de-versailes (32.5k), f-nogueira-wpr (37k), fg-scenarium (42k), colline-de-france (27.5k), f-nogueira-soberano (27.2k)

### Dados básicos

| # | Pergunta | Default sugerido |
|---|---|---|
| 1 | AC total (m²) confirmada? | **36.000** |
| 2 | UR (unidades residenciais) | **348** |
| 3 | Nº total de pavimentos | **32** |
| 4 | Nº pavimentos tipo | **24** |
| 5 | Nº de torres/blocos | **2** |
| 6 | Nº elevadores total | **4** (2 por torre: social + emergência) |
| 7 | Nº vagas de garagem | **522** (1.5 vaga/UR) |
| 8 | Área do terreno (AT m²) | **?** — não achei quadro de áreas, me passa |
| 9 | Cidade / estado | **Itajaí/SC ou Balneário Camboriú/SC** |
| 10 | CUB data-base | **CUB SC abr/2026** (R$ ? — usar atual) |

### Decisões técnicas

| # | Pergunta | Default sugerido |
|---|---|---|
| 11 | Tipo de laje | **Protendida** (típico em torres altas 32 pav com 2 torres) |
| 12 | Tipo de fundação | **Hélice contínua** (padrão litoral norte SC) |
| 13 | Contenção (se tiver subsolo) | **Cortina ou solo grampeado** |
| 14 | Nº de subsolos | **1** (há 6 pavs de garagem G1-G5 + subsolo — verificar) |
| 15 | Padrão de acabamento | **Alto** (348 UR, 2 torres = empreendimento médio-alto padrão) |
| 16 | Tipologia predominante | **1-2 dormitórios** (348 UR em 36k m² ≈ 103 m²/UR) |
| 17 | Tipo de fachada | **Pastilha + textura** |
| 18 | Piscina | **Sim** (lazer 2 torres quase sempre tem) |
| 19 | Gerador dedicado | **Sim** (obrigatório em escala) |
| 20 | Pressurização | **Sim** (PCI obrigatório >28 m) |
| 21 | Prazo de obra | **36 meses** (escala, 2 torres) |
| 22 | BDI | **25%** |

### Sistemas especiais já extraídos do BIM

- **138 TR de AC** (80 evaporadoras + 117 condensadoras)
- **195 churrasqueiras** (8 exaustores TCV 710 Berliner Luft)
- 8 prumadas de dutos (~1.400-1.720 m galvanizado)
- Custo estimado exaustão: R$ 1,1-1,8M (R02)

**Decisão 23:** Incluir esses sistemas como já quantificados ou deixar o auto estimar?
**Default:** **Incluir** — são números do BIM, precisos.

---

## 🏢 Projeto 2 — Arthen Arboris

**Slug:** `arthen-arboris`
**Pasta:** `G:\...\_Projetos_IA\arthen-arboris`
**Contexto:** Já tem paramétrico V2 + memorial completo + análise v2 (10 sheets). Memorial validado.
**Similares identificados:** viva4-barra4 (13.2k), xpcon-porto-cerro (13.2k), fonseca-estoril (14.5k), cln-porto-ruby (13k), somauma-virginia (10.1k)

### Dados básicos (do memorial)

| # | Pergunta | Default do memorial |
|---|---|---|
| 1 | AC total (m²) | **12.472,98** ✓ |
| 2 | UR residenciais | **90** |
| 3 | UR comerciais | **8** |
| 4 | Nº total de pavimentos | **20** (14 tipo + 1 dif + garagens + térreo + cobertura) |
| 5 | Nº pavimentos tipo | **15** |
| 6 | Nº pavimentos garagem | **3** (G1, G2, G3 = mezaninos) |
| 7 | Nº torres | **1** |
| 8 | Nº elevadores | **2** (1 social + 1 emergência) |
| 9 | Nº vagas | **99** |
| 10 | AT (terreno) | **1.008 m²** |
| 11 | Cidade | **Itapema/SC** |
| 12 | CUB data-base | **mar/2026 R$ 3.028,45** |

### Decisões técnicas (do memorial)

| # | Pergunta | Default do memorial |
|---|---|---|
| 13 | Tipo de laje | **Convencional** |
| 14 | Tipo de fundação | **Hélice contínua** |
| 15 | Padrão acabamento | **Médio** |
| 16 | Prazo | **30 meses** |
| 17 | Subsolos | **0** (garagens são mezaninos, não subsolos) |

### Dúvidas específicas (do paramétrico v2 existente)

| # | Pergunta | Default sugerido |
|---|---|---|
| 18 | Climatização: só infra ou + equipamentos? | **Só infra** (memorial diz "AC split infra" = -R$ 515k) |
| 19 | Louças: só bacias ou + cubas/torneiras/bancadas? | **Só bacias** (conforme memorial = -R$ 200k) |
| 20 | **2 piscinas** + ofurô confirmados? (paramétrico estima 1) | **Sim, 2 piscinas + ofurô** (+R$ 130-200k) |
| 21 | Tipologia detalhada das 90 UR | **Misto** (~40% 1D, 35% 2D, 15% 3D, 10% studio) |
| 22 | Burn rate alto (+38% vs mediana): justifica aumentar prazo? | **Manter 30 meses** (memorial validou) |
| 23 | Gerador | **1 un ~100 kVA** (R$ 180k) |

### D1 (cruzada): Qual opção?
- [a] Refazer paramétrico novo substituindo o v2
- [b] Manter v2, só fazer executivo
- [c] Gerar v2.1 preservando v2 como backup ← **default**

---

## 🏢 Projeto 3 — Placon Armínio Tavares

**Slug:** `placon-arminio-tavares`
**Pasta:** `G:\...\_Projetos_IA\placon-arminio-tavares`
**Contexto:** 560 arquivos em 15 disciplinas BIM. Projeto em fase pré-executivo / início de obra.
**Similares identificados:** xpcon-marena (4.1k), muller-guanabara (4.4k), nova-malaga (4.4k), chiquetti-esmeralda (5.6k), inbrasul-opus (4.4k)

### Dados extraídos do Quadro NBR 12.721

| Campo | Valor | Fonte |
|---|---|---|
| Incorporador | Placon Empreendimentos Imobiliários Ltda | Quadro info |
| Endereço | Rua Dr. Armínio Tavares, Centro, Florianópolis/SC | Quadro info |
| Responsável Técnico | Luciana Balsini Francalacci (CREA-SC 041.266-8) | Quadro info |
| Nº unidades autônomas | **55** ✓ | Quadro info |
| Nº pavimentos | **17** ✓ | Quadro info |
| Padrão NBR | **Residencial Multifamiliar NORMAL** | Quadro III |
| Data-base CUB | **Janeiro 2026** | Quadro III |
| Tipologia | Studios + Aptos 1 dormitório | Quadro II |
| Custo Básico Global (NBR) | **R$ 10.580.596,97 a R$ 11.926.976,97** | Quadro IVA |

### Dúvidas

| # | Pergunta | Default sugerido |
|---|---|---|
| 1 | AC total real (área construída total) | **~4.500 m²** (a confirmar — estimativa de soma parcial) |
| 2 | AT (área do terreno) | **?** — me passa |
| 3 | Nº pavimentos tipo | **9** (3-6 + 12-16 = 9) |
| 4 | Nº pavimentos garagem | **3** (subsolo + 1º + parte do 2º) |
| 5 | Nº elevadores | **2** |
| 6 | Nº vagas | **55** (1 vaga/UR estimado) |
| 7 | Tipo de laje | **Convencional** (padrão Normal) |
| 8 | Tipo de fundação | **Sapata ou hélice** (Centro Floripa, solo varia) |
| 9 | Contenção / subsolo | **Subsolo 1, com contenção** |
| 10 | Padrão real | **Médio** (NBR diz Normal = Médio no V2) |
| 11 | Tipologia predominante | **Studios** (Quadro II mostra maioria studios) |
| 12 | Piscina | **Provavelmente sim** (central Floripa, mercado) |
| 13 | Gerador | **Sim** (>12 pav exige) |
| 14 | Prazo | **24 meses** (4.500 m², projeto menor) |
| 15 | BDI | **25%** |
| 16 | CUB data-base | **Jan/2026 CUB SC** (R$ ? — usar referência NBR) |

**Checagem com NBR:** se AC = 4.500 e custo NBR = R$ 10-12M, R$/m² NBR = R$ 2.222-2.650. O V2 calibrado estima R$ 2.813/m² → **20% acima do NBR** (que usa CUB padrão Normal, mais conservador). Faz sentido.

---

## 📋 Checklist antes da noite

- [ ] D1 — Arthen: qual opção (a/b/c)?
- [ ] D2 — Thozen: confirmar que cabe (ou substituir por outro projeto menor)
- [ ] D3 — Placon: confirmar AC total (~4.500 m²?) ou me passar valor real
- [ ] Thozen P8: AT m²?
- [ ] Thozen P9: cidade
- [ ] Thozen P10: CUB data-base
- [ ] Placon P1: AC exata
- [ ] Placon P2: AT m²
- [ ] Demais perguntas: responder só as que discordar do default

---

## 📁 Localização dos arquivos

- Este arquivo: `~/orcamentos-openclaw/base/pacotes/duvidas-projetos-noturno-2026-04-13.md`
- Pode responder editando este mesmo arquivo (append no final ou inline) ou por chat
- Gates pré-populados vão ser salvos em `~/orcamentos-openclaw/base/pacotes/{slug}/gate-{slug}.xlsx`

---

## ⏱ Timeline

- **Agora até 17h:** você responde conforme disponível
- **17h-22h30:** eu rodo as 6 melhorias 7.x (sem bloqueio de você)
- **22h30+:** você volta, eu disparo os 3 pacotes, começamos a revisão
