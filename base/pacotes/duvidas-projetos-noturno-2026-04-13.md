# Briefing Final Noturno — 2026-04-13

**3 projetos → Pacote Paramétrico + Executivo cada**

Documento consolidado com respostas do Leo + defaults adotados + plano de execução.

---

## ✅ Pendências resolvidas

1. **Thozen AT** = **2.095,43 m²** ✓
   - Coef. de aproveitamento = 37.894 / 2.095 = **18,1** — agressivo mas coerente com lote urbano denso em Porto Belo
2. **Placon fundação** = **hélice contínua** ✓
3. **Placon piscina** = **analisar projeto arquitetônico na execução noturna** ✓
   - Adicionei um **Bloco 0 — Análise Arquitetônica** no timeline noturno que vai:
     - Ler PDFs de plantas, IFCs e memoriais da pasta de cada projeto
     - Buscar por keywords: piscina, academia, salão festas, churrasqueira, playground, sauna, quadra, spa, ofurô, brinquedoteca, coworking
     - Extrair áreas dos espaços de lazer quando possível
     - Retornar um `analise-arquitetura-{slug}.json` com a lista de itens encontrados
   - Isso vai rodar **pros 3 projetos** (Thozen, Arthen, Placon) antes do gate ser pré-populado, pra que a decisão "tem ou não tem piscina/academia/lazer" seja feita automaticamente a partir do projeto real, não de default.

---

## 📊 Briefing Final dos 3 projetos

### 🏢 Projeto 1 — Thozen Electra

**Slug:** `thozen-electra` · **Prioridade: ALTA (entrega)**

| Campo | Valor |
|---|---|
| **AC total** | **37.893,89 m²** ✓ |
| **AT terreno** | **2.095,43 m²** ✓ (coef. aprov. = 18,1) |
| **UR** | 348 |
| **Nº pavimentos** | 32 |
| **Nº pavimentos tipo** | 24 |
| **Nº torres** | 2 |
| **Nº elevadores** | 4 (2/torre: social + emergência) |
| **Nº vagas** | 522 (1.5 vaga/UR) |
| **Cidade** | **Porto Belo/SC** ✓ |
| **CUB data-base** | **Março/2026** ✓ |
| **Padrão** | Alto |
| **Tipo de laje** | Protendida |
| **Tipo de fundação** | Hélice contínua |
| **Contenção** | Cortina ou solo grampeado (se subsolo) |
| **Nº subsolos** | 1 |
| **Tipologia predominante** | 1-2 dormitórios |
| **Tipo de fachada** | Pastilha + textura |
| **Piscina** | Sim |
| **Gerador dedicado** | Sim |
| **Pressurização** | Sim (PCI obrigatório >28m) |
| **Prazo de obra** | 36 meses |
| **BDI** | 25% |
| **Similares na base** | beco-castelo, f-nogueira-wpr, fg-scenarium, colline-de-france, f-nogueira-soberano |
| **Total estimado V2** | R$ 117M (3.094 R$/m² × 37.894) |

**Sistemas especiais já quantificados do BIM (incluir no executivo):**
- AC: 138 TR (80 evaporadoras + 117 condensadoras)
- Exaustão: 195 churrasqueiras + 8 exaustores TCV 710 Berliner Luft
- 8 prumadas, ~1.400-1.720 m de dutos galvanizado
- Estimativa prévia exaustão: R$ 1,1-1,8M

---

### 🏢 Projeto 2 — Arthen Arboris

**Slug:** `arthen-arboris` · **Prioridade: Média**
**Decisão cruzada:** ✅ **Opção A — refazer paramétrico do zero** (substituir v2 atual)

| Campo | Valor |
|---|---|
| **AC total** | 12.472,98 m² |
| **AT terreno** | 1.008 m² |
| **UR residenciais** | 90 |
| **UR comerciais** | 8 |
| **UR total** | 98 |
| **Nº pavimentos** | 20 (14 tipo + 1 diferenciado + 3 garagens + térreo + cobertura) |
| **Nº pavimentos tipo** | 15 |
| **Nº pavimentos garagem** | 3 (G1, G2, G3 mezaninos) |
| **Nº torres** | 1 |
| **Nº elevadores** | 2 (1 social + 1 emergência) |
| **Nº vagas** | 99 |
| **Cidade** | Itapema/SC |
| **CUB data-base** | mar/2026 — R$ 3.028,45 |
| **Padrão** | Médio |
| **Tipo de laje** | Convencional |
| **Tipo de fundação** | Hélice contínua |
| **Nº subsolos** | 0 (garagens são mezaninos) |
| **Prazo de obra** | **36 meses** ✓ (revisado por Leo — aumenta burn rate coerente) |
| **BDI** | 25% |
| **Climatização** | ✅ **Só infra** (sem equipamentos) |
| **Louças** | ✅ **Só bacias** (sem cubas/torneiras/bancadas) |
| **Piscinas** | 2 piscinas + 1 ofurô |
| **Gerador** | 1 un ~100 kVA |
| **Tipologia** | Misto (~40% 1D, 35% 2D, 15% 3D, 10% studio) |
| **Similares na base** | viva4-barra4, xpcon-porto-cerro, fonseca-estoril, cln-porto-ruby, somauma-virginia |
| **Total estimado V2** | R$ 35M (2.813 R$/m² × 12.473) |

**Importante:** Opção A = refazer o paramétrico inteiro. O v2 anterior (`arthen-arboris-parametrico-v2.xlsx`) já existe no Drive; vou preservá-lo como `-v2-backup.xlsx` antes de regenerar.

---

### 🏢 Projeto 3 — Placon Armínio Tavares

**Slug:** `placon-arminio-tavares` · **Prioridade: Média**

| Campo | Valor |
|---|---|
| **AC total** | **4.077,29 m²** ✓ (Quadro de Áreas - Projeto Legal) |
| **AT terreno** | **900 m²** ✓ |
| **UR total** | 55 (Studios + Aptos 1D) |
| **Nº pavimentos** | 17 |
| **Nº pavimentos tipo** | 9 (3-6 + 12-16) |
| **Nº pavimentos garagem** | 3 (subsolo + 1º + parte 2º) |
| **Nº torres** | 1 |
| **Nº elevadores** | 2 |
| **Nº vagas** | 55 (1/UR estimado) |
| **Cidade** | Florianópolis/SC — Centro (Rua Dr. Armínio Tavares) |
| **CUB data-base** | **mar/2026 CUB SC** ✓ |
| **Padrão NBR** | Residencial Multifamiliar NORMAL |
| **Padrão V2** | Médio |
| **Tipo de laje** | Convencional |
| **Tipo de fundação** | **Hélice contínua** ✓ |
| **Contenção** | Sim (subsolo 1) |
| **Tipologia predominante** | Studios (maioria) + Aptos 1 dormitório |
| **Piscina** | _será determinada pela análise arquitetônica no Bloco 0_ |
| **Gerador** | Sim (>12 pavimentos exige) |
| **Prazo de obra** | 24 meses |
| **BDI** | 25% |
| **Incorporador** | Placon Empreendimentos Imobiliários Ltda |
| **RT** | Luciana Balsini Francalacci (CREA-SC 041.266-8) |
| **Custo NBR** | R$ 10,58M a R$ 11,93M (referência) |
| **Similares na base** | xpcon-marena, muller-guanabara, nova-malaga, chiquetti-esmeralda, inbrasul-opus |
| **Total estimado V2** | R$ 11,5M (2.813 R$/m² × 4.077) |

**Validação:** estimativa V2 bate com NBR (R$ 11,5M vs R$ 10,58-11,93M) ± 3%. 🟢

---

## 📈 Resumo consolidado

| Projeto | AC | UR | Cidade | Total est. | R$/m² |
|---|---|---|---|---|---|
| thozen-electra | 37.894 | 348 | Porto Belo/SC | R$ 117M | 3.094 |
| arthen-arboris | 12.473 | 98 | Itapema/SC | R$ 35M | 2.813 |
| placon-arminio-tavares | 4.077 | 55 | Florianópolis/SC | R$ 11,5M | 2.813 |
| **TOTAL** | **54.444** | **501** | — | **R$ 163,5M** | — |

---

## ⏱ Plano de execução noturno

### 🌅 17h — início (sem você, dando aula)

#### Bloco 0 — Análise Arquitetônica (17h00-18h00)

Criar e rodar `scripts/analise_arquitetura.py` que, pra cada projeto, varre a pasta do Drive buscando:

**Fontes de dados:**
- PDFs de plantas, memoriais, apresentações (lidos via pypdf)
- Memoriais descritivos em .docx
- IFCs via `ifcopenshell` (se instalado) — extrai `IfcSpace` com `LongName`
- Nomes de arquivos DWG (nomes costumam ter "PLANTA_LAZER", "PISCINA", etc.)

**Keywords caçadas** (case-insensitive, com variações):
- Lazer: `piscina`, `piscina aquecida`, `ofurô`, `spa`, `sauna`, `jacuzzi`
- Esportes: `academia`, `fitness`, `quadra`, `squash`, `musculação`
- Social: `salão de festas`, `salão gourmet`, `gourmet`, `churrasqueira`, `fire place`, `pub`, `lounge`, `game room`
- Infantil: `playground`, `brinquedoteca`, `kids`, `fraldário`
- Trabalho: `coworking`, `home office`, `sala de reunião`
- Serviço: `lavanderia`, `pet place`, `bicicletário`

**Output por projeto:** `base/pacotes/{slug}/analise-arquitetura.json`
```json
{
  "projeto": "thozen-electra",
  "itens_encontrados": [
    {"tipo": "piscina", "fonte": "02-TÉRREO_R01.pdf", "count": 2},
    {"tipo": "academia", "fonte": "IFC arquitetura", "area_m2": 145},
    {"tipo": "salão de festas", "fonte": "memorial.pdf", "count": 1}
  ],
  "arquivos_lidos": 12,
  "total_keywords_hit": 23
}
```

**Alimentação do gate:** os itens encontrados vão pré-popular as decisões do gate (piscina = sim/não, academia = sim/não, etc.), e o executivo automatizado vai usá-los no macrogrupo "Sistemas Especiais" e "Complementares".

#### Bloco 1 — Melhorias 7.x (18h00-22h30)

```
18h00-18h20  [7.6] Memorial Word do paramétrico no pacote (~20 min)
18h20-19h20  [7.4] Granularização via Gemma sub-disciplinas (~1h) ⭐ alta prioridade
19h20-20h05  [7.2] Memorial Word do executivo (~45 min)
20h05-20h35  [7.5] Validação por segmento (~30 min)
20h35-21h05  [7.3] Aba RESUMO mais expressiva (~30 min)
21h05-21h35  [7.1] Multiplicador diferencial por macrogrupo (~30 min)
21h35-22h00  Testes end-to-end no pacote piloto, commit incremental a cada 7.x
22h00-22h30  Pré-população dos 3 gates com respostas + análise arquitetônica
```

**Commits incrementais** a cada bloco terminado. Se alguma melhoria der problema, rollback isolado e sigo.

**Relatório contínuo:** atualizo `~/orcamentos-openclaw/base/pacotes/noturno-progresso.md` a cada hora — você pode abrir quando chegar e ver o estado.

### 🌙 22h30 — você volta

```
22h30-22h50  Você janta/descansa
             Eu atualizo o progresso e faço pull final dos commits
22h50-23h00  Disparo os 3 pacotes em sequência (arthen → placon → thozen)
             Gera parametrico, executivo, memorial, validação pra cada
             ~10-15 min no total
```

### 🌃 23h — revisão em sequência

**Ordem sugerida:** dos menores/mais simples pros maiores. Isso garante que se a noite ficar longa, os 2 mais fáceis já estão prontos.

```
23h00-00h00  REVISA: placon-arminio-tavares (menor, ~R$ 11.5M, estrutura simples)
             Você abre os 4 arquivos gerados + validação.md
             Feedback por chat, eu itero ajustes em tempo real
00h00-01h30  REVISA: arthen-arboris (12k m², Opção A = regeneração completa)
             Compara com v2 anterior se quiser, eu gero diff
01h30-03h30  REVISA: thozen-electra (o grande, 38k m², 2 torres)
             Mais tempo porque é maior e tem sistemas especiais do BIM
             Incluo na revisão os quantitativos BIM (138 TR AC, 195 churrasqueiras)
```

### 🌄 03h30 — fechamento

```
03h30-04h30  Ajustes finais nos 3 baseados nos feedbacks
04h30-05h30  Regeneração final de cada, validação cruzada, commit/push
05h30-06h30  Relatório consolidado da noite + cópia pros Drives dos 3 projetos
06h30-07h00  Buffer de descanso
```

### 📊 Entregáveis por projeto (12 arquivos no total)

Cada projeto vai gerar em `~/orcamentos-openclaw/base/pacotes/{slug}/`:

1. `gate-{slug}-validado.xlsx` — gate pré-populado com as respostas deste briefing
2. `parametrico-{slug}.xlsx` — paramétrico V2 calibrado
3. `parametrico-{slug}.docx` — memorial Word do paramétrico (após 7.6)
4. `executivo-{slug}.xlsx` — executivo automatizado com 18 macrogrupos + sub-disciplinas reais + confidence tags
5. `executivo-{slug}.docx` — memorial Word do executivo (após 7.2)
6. `validacao-{slug}.md` — relatório de coerência

**Total de artefatos noturnos:** 18 arquivos (6 × 3 projetos) + 3 relatórios finais.

---

## ⚠️ Riscos identificados e mitigação

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Bloco 0 não consegue ler IFCs (ifcopenshell não instalado) | Média | Fallback para PDFs + nomes de arquivo; instalar ifcopenshell durante o bloco se precisar |
| Keywords do Bloco 0 falham em identificar piscina | Baixa | Se Placon não tiver hit claro, mostro no relatório como "indeterminado" e mantenho default sim |
| Melhoria 7.4 (granularização) dá regressão | Média | Rollback isolado dessa, sigo com as outras |
| Thozen muito grande, tempo de revisão estoura | Média | Prioridade 1 é placon+arthen, Thozen tem folga até 05h30 |
| Gemma local trava (Ollama crash) | Baixa | Phase 7.4 é a única que usa Gemma; tudo mais é Python puro |
| Drive G: fica offline | Baixa | Gates pré-populados salvos em git; geração ainda funciona |

---

## 📁 Localização

- **Briefing (este):** `~/orcamentos-openclaw/base/pacotes/duvidas-projetos-noturno-2026-04-13.md`
- **Progresso noturno:** `~/orcamentos-openclaw/base/pacotes/noturno-progresso.md` (criado às 17h)
- **Pacotes gerados:** `~/orcamentos-openclaw/base/pacotes/{slug}/`
- **Backup Arthen v2 anterior:** `~/orcamentos-openclaw/base/pacotes/arthen-arboris/parametrico-arthen-arboris-v2-backup.xlsx`

---

## ✍️ Quando responder

Até **17h** idealmente. Se não responder as 3 pendências, uso os defaults entre parênteses.

**Canais:** edite este arquivo inline ou me manda no chat. Ambos funcionam.
