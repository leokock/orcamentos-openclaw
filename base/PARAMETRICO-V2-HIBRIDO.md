# Paramétrico V2 Híbrido — Referência Canônica

_Formalizado em 2026-04-14. Versão atual do gerador paramétrico da Cartesian._

## O que é

Sistema de geração de orçamento paramétrico **bottom-up** (Qtd × PU = Total) com **dropdowns interativos** no BRIEFING que reagem automaticamente aos índices calibrados **+** **coluna de override manual** na aba INDICES que permite ao orçamentista sobrescrever qualquer índice durante reunião com cliente.

**Script autoritativo:** `scripts/gerar_template_dinamico_v2.py`

**Status:** fonte única de geração de paramétricos (V1 deprecated, V2 pre-híbrido arquivado em `_antigo-parametrico/` dentro de cada pacote).

## Por que existe

Antes da Fase 19 (2026-04-14), o orçamentista só conseguia ajustar índices **indiretamente** via dropdowns do BRIEFING — qualquer índice específico que não encaixasse numa das opções ficava travado ("NÃO EDITAR"). Em reuniões com cliente, era comum precisar calibrar um valor muito específico do projeto (ex: "esse empreendimento tem laje mais pesada que o padrão protendida, quero 0,35 m³/m² em vez de 0,22") e não ter como fazer sem editar fórmulas manualmente.

O **híbrido** resolve: BRIEFING continua sendo a fonte primária (dropdowns de alto nível), MAS qualquer índice pode ser overrido caso a caso na aba INDICES sem quebrar a cascata de cálculo.

## Arquitetura da aba INDICES

```
| A                   | B                  | C          | D              | E        | F              |
| Índice              | Valor calc         | Override   | Efetivo        | Unidade  | Fonte          |
| (nome)              | (fórmula BRIEFING) | (input)    | (=IF(C="",B,C))| (un)     | (ref + nota)   |
|---------------------|--------------------|------------|----------------|----------|----------------|
| Concreto (m³/m² AC) | =IF(B4="Prot"...)  | _(vazio)_  | =IF(C5="",B5,C5)| m³/m²   | Master 7p exec |
| Aço (kg/m³)         | =IF(B4="Prot"...)  | _(vazio)_  | =IF(C6="",B6,C6)| kg/m³   | Master 7p+narr |
| ...                 | ...                | ...        | ...            | ...      | ...            |
```

**Regras:**
- **Col B (Valor calculado):** fórmula `IF()` que reage aos 14 dropdowns do BRIEFING. Permanece "não editar" — é o valor-base estatístico.
- **Col C (Override):** célula vazia por default, estilo input laranja. Orçamentista digita aqui pra sobrescrever.
- **Col D (Efetivo):** `=IF(C{n}="",B{n},C{n})`. É a célula que **todas as abas de macrogrupo consomem**.
- **Col E/F:** unidade e fonte/fórmula original (info).

**Comportamento na prática:**
1. Sem override: D = B (valor calculado via BRIEFING)
2. Com override: D = C (valor manual do orçamentista)
3. Apagar C: D volta pra B automaticamente
4. Toda cascata bottom-up (Qtd × PU em cada aba de macrogrupo) usa `INDICES!D{n}`, então o override propaga pra todos os cálculos de um MG inteiro

## Aba BRIEFING — 14 dropdowns + pré-preenchimento

| Row | Pergunta | Opções | Default | Config key |
|---|---|---|---|---|
| 4 | Tipo de Laje | Convencional / Protendida / Nervurada | Convencional | `laje` |
| 5 | Subsolos | 0 / 1 / 2 / 3 | 0 | `subsolos` |
| 6 | Fundação | Hélice / Tubulão / Sapata | Hélice | `fundacao` |
| 7 | Padrão Acabamento | Médio / Médio-Alto / Alto / Luxo | Médio-Alto | `padrao_acabamento` |
| 8 | Fachada | Textura / Cerâmica / Pele de vidro / ACM | Textura | `fachada` |
| 9 | Pressurização | Sim / Não | Não | `pressurizacao` |
| 10 | Nº Torres | 1 / 2 / 3 | 1 | `n_torres` |
| 11 | Gerador Dedicado | Sim / Não | Sim | `gerador` |
| 12 | Entrega | Completa / Shell | Completa | `entrega` |
| 13 | Tipologia | Studios / 1-2 Dormitórios / 3-4 Dormitórios / Misto | Misto | `tipologia` |
| 14 | Pé-Direito | Baixo (2.80) / Padrão (3.00) / Alto (3.20) / Duplo | Padrão (3.00) | `pe_direito` |
| 15 | Nº Banheiros/Apto | 1 / 2 / 3 / 4 | 2 | `n_banheiros` |
| 16 | Tipo Piso | Porcelanato / Laminado / Misto | Misto | `tipo_piso` |
| 17 | Piscina | Sim / Não / Aquecida | Sim | `piscina` |

**Pré-preenchimento via config JSON:**
```json
{
  "nome": "Projeto X",
  "ac": 13000,
  "ur": 120,
  "np": 24,
  "briefing": {
    "laje": "Protendida",
    "padrao_acabamento": "Alto",
    "fachada": "ACM",
    "piscina": "Aquecida"
  }
}
```

Valores ausentes no `briefing` caem no default. Valores inválidos (não batem com as opções) geram warning e caem no default também.

## Fluxo de uso

### Geração inicial

```bash
# Via config JSON (recomendado)
python scripts/gerar_template_dinamico_v2.py \
  --config base/pacotes/{slug}/parametrico-v2-config.json \
  -o base/pacotes/{slug}/parametrico-{slug}.xlsx

# Ou via CLI args individuais
python scripts/gerar_template_dinamico_v2.py \
  --nome "Projeto X" --ac 13000 --ur 120 --np 24 \
  --cidade "Itajaí" \
  -o projeto.xlsx
```

O script cria: PAINEL + DADOS_PROJETO + BRIEFING + **INDICES** (6 colunas) + CUSTOS_MACROGRUPO + 18 abas de macrogrupo + PREMISSAS.

### Geração do pacote completo (inclui docx + pdf)

Via orquestrador existente:
```bash
python scripts/gerar_pacote.py --continue --slug {slug}
```

Ou manualmente:
```bash
# 1. xlsx
python scripts/gerar_template_dinamico_v2.py --config base/pacotes/{slug}/parametrico-v2-config.json -o base/pacotes/{slug}/parametrico-{slug}.xlsx

# 2. docx
python scripts/gerar_memorial_pacote.py --slug {slug} --tipo parametrico

# 3. pdf
python -c "from docx2pdf import convert; convert('base/pacotes/{slug}/parametrico-{slug}.docx', 'base/pacotes/{slug}/parametrico-{slug}.pdf')"
```

### Entrega no Drive (obrigatório)

**Regra:** após gerar `parametrico-{slug}.{xlsx,docx,pdf}` no git, é **obrigatório** sincronizar pro Google Drive compartilhado. O git é o repo técnico (versioning), mas a equipe Cartesian acessa as entregas pelo Drive em `_Parametrico_IA/`.

**Script autoritativo:** `scripts/sincronizar_parametrico_drive.py`

```bash
# Sync de um projeto (com arquivamento de versões antigas)
python scripts/sincronizar_parametrico_drive.py --slug arthen-arboris --archive-old

# Sync de todos (dry-run pra conferir antes)
python scripts/sincronizar_parametrico_drive.py --all --dry-run
python scripts/sincronizar_parametrico_drive.py --all --archive-old
```

**Nomenclatura no Drive:** `{drive_prefix}-parametrico-v3-hibrido.{xlsx,docx,pdf}` + `{drive_prefix}-parametrico-v3-config.json` (alinha com o padrão histórico Cartesian `*-parametrico-v2.xlsx`).

**Mapeamento git_slug → drive_folder:** em `scripts/drive-mapping.json`. **Nem sempre bate com o slug** — exemplos:

| Git slug | Drive folder | Drive prefix |
|---|---|---|
| arthen-arboris | arthen-arboris | arthen-arboris |
| placon-arminio-tavares | arminio-tavares | arminio-tavares |
| thozen-electra | thozen-electra | thozen-electra |

Ao criar projeto novo, **primeiro adicionar entrada no drive-mapping.json**, depois rodar o script.

**Flag `--archive-old`:** move `{prefix}-parametrico-v*.xlsx` e `{prefix}-analise-v*.xlsx` antigos pra subpasta `_antigo/` antes de copiar os novos. Preserva histórico sem poluir a pasta principal.

**Drive path (Windows):** `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Parametrico_IA\`. No Mac usa `~/Library/CloudStorage/GoogleDrive-.../Drives compartilhados/...`. O script auto-detecta.

**Log:** cada sync é registrado em `base/drive-sync.log.jsonl` (append-only).

**Checkpoint humano:** confirmar com Leo antes do primeiro sync de um slug novo (afeta Drive compartilhado que a equipe usa).

### Cenário de uso real — reunião com cliente

Orçamentista Cartesian abre o paramétrico `.xlsx` numa reunião. Cliente questiona a estrutura:
> "Mas esse projeto tem laje protendida mais pesada que o normal, vocês usaram 0,22 m³/m² mas eu diria 0,28"

Orçamentista navega:
1. Aba BRIEFING → confirma "Tipo de Laje" = Protendida (dropdown)
2. Aba INDICES → linha 5 (Concreto m³/m² AC):
   - Col B: `0,22` (calculado via BRIEFING)
   - Col C: *vazio*
3. Digita `0,28` na célula C5
4. Col D5 muda de 0,22 pra 0,28 instantaneamente
5. Aba Supraestrutura recalcula todas as quantidades de concreto (pilar, viga, laje, escada, blocos, aço, cordoalha, forma)
6. CUSTOS_MACROGRUPO e PAINEL atualizam total

Se cliente aceitar: orçamentista salva. Se não: apaga C5, volta pro calculado.

**Também funciona pros 3 fatores ocultos** (novos na Fase 19):
- Row 33: Fator viga protendida (0,08 vs 0,30)
- Row 34: Fator laje protendida (0,60 vs 0,35)
- Row 35: Fator hidro BWC (1,15 vs 1,0)

Antes da Fase 19 esses eram hardcoded dentro das fórmulas. Agora estão na aba INDICES e podem ser overridden.

## Modelo de cálculo

```
Para cada item i em cada aba de macrogrupo:
  Qtd_i    = INDICES!D{idx_row} × AC × fator_especifico
  PU_i     = PU_base_cartesian (ou referência calibrada)
  Total_i  = Qtd_i × PU_i
  
Total_macrogrupo = SUM(Total_i)
Total_projeto    = SUM(Total_macrogrupos)
R$/m² AC        = Total_projeto / AC
CUB Ratio       = R$/m² / CUB
```

**Índices** (18 nativos + 3 novos = 21 overridable):
- Estrutura (5-10): concreto, aço, cordoalha, forma, escoramento, fck
- Fundação (11-12): nº estacas, comp. estaca
- Acabamentos (13-19): alvenaria, pisos, rev. parede, forro, pintura, fachada, impermeab
- Fatores ajuste (20-32): padrão, fachada PU, pressurização, gerador, contenção, mov. terra, tipologia louças, tipologia elétrica, entrega, PU piso, piscina, pé-direito, BWC louças
- Fatores novos (33-35): viga protendida, laje protendida, hidro BWC

## Integração com Fase 18b (calibração condicional Gemma)

O paramétrico V2 e o preliminar (calibração condicional Gemma) são **produtos complementares**, não concorrentes:

| | Paramétrico V2 Híbrido | Preliminar (Fase 18b) |
|---|---|---|
| Método | Bottom-up (Qtd × PU por item) | Top-down (R$/m² calibrado × AC por MG) |
| Granularidade | 200+ itens × 18 MGs | 18 MGs agregados |
| Fonte | calibration-indices + base-pus-cartesian + briefing interativo | calibration-condicional-padrao.json (labels Gemma) |
| Editabilidade | Índices overridable + dropdowns BRIEFING | Padrão Gemma + config |
| Uso ideal | Justificar custo com cliente técnico | Entrega rápida, validação cross-projeto |

**Recomendação:** gerar os dois e comparar os totais. Se divergência > 15%, investigar qual das duas fontes tá mais aderente ao projeto real.

## Schema do config JSON

```json
{
  "_gerado_em": "YYYY-MM-DD",
  "_fonte": "descrição das fontes de dados",
  "_descricao": "comentário livre",

  "nome": "Nome do Projeto",
  "cidade": "Itajaí",
  "estado": "SC",
  "regiao": "Litoral Norte SC",

  "ac": 12473.0,
  "ur": 98,
  "np": 24,
  "npt": 19,
  "elev": 2,
  "vag": 120,
  "prazo": 30,
  "cub": 3028.45,

  "briefing": {
    "laje": "Convencional",
    "subsolos": "1",
    "fundacao": "Hélice",
    "padrao_acabamento": "Médio-Alto",
    "fachada": "Cerâmica",
    "pressurizacao": "Não",
    "n_torres": "1",
    "gerador": "Sim",
    "entrega": "Completa",
    "tipologia": "3-4 Dormitórios",
    "pe_direito": "Padrão (3.00)",
    "n_banheiros": "2",
    "tipo_piso": "Porcelanato",
    "piscina": "Sim"
  }
}
```

Campos obrigatórios: `nome`, `ac`, `ur`. Todos os outros têm defaults no script.

**Encoding obrigatório: UTF-8.** O script lê com `encoding='utf-8'` explícito pra evitar corrupção de acentos no Windows (onde default é cp1252).

## Cuidados

- **Override zerado:** se o usuário digitar `0` na Col C, `D` retorna 0 (zero é um valor válido). Pra "limpar" override, apagar a célula (Delete) — NÃO digitar 0.
- **Dropdowns continuam ativos:** mesmo com override, o BRIEFING continua editável. Se o orçamentista muda o dropdown depois de overridar, o valor Col B muda mas Col D continua usando Col C. Pra voltar a reagir ao BRIEFING: apagar C.
- **Fórmulas dentro da INDICES self-reference:** a linha 29 (PU piso predominante) usa `INDICES!D20` (fator padrão efetivo) pra respeitar override do padrão — isso é intencional.
- **Válidação de briefing preset:** se o config tem um valor que não está nas opções do dropdown (ex: `"tipologia": "2-3 Dormitórios"` sem hífen específico), o script avisa e usa o default. Sempre conferir os warnings do script.

## Arquivos relacionados

| Arquivo | Função |
|---|---|
| `scripts/gerar_template_dinamico_v2.py` | **Gerador autoritativo** (812 linhas) |
| `scripts/gerar_pacote.py` | Orquestrador: gate → paramétrico → preliminar → validação |
| `scripts/gerar_memorial_pacote.py` | Gera `.docx` a partir do `.xlsx` |
| `base/calibration-indices.json` | Índices master globais |
| `base/calibration-condicional-padrao.json` | Calibração condicional Gemma (Fase 18b, usado no preliminar) |
| `base/base-pus-cartesian.json` | PUs cross-projeto |
| `base/itens-pus-agregados.json` | 4.210 clusters PU (PU sanity filter) |
| `base/pacotes/{slug}/parametrico-v2-config.json` | Config por projeto (briefing pré-preenchido) |
| `base/pacotes/{slug}/parametrico-{slug}.xlsx` | Output: planilha interativa |
| `base/pacotes/{slug}/_antigo-parametrico/` | Versões anteriores arquivadas |
| `scripts/sincronizar_parametrico_drive.py` | **Sync pro Drive compartilhado (obrigatório após geração)** |
| `scripts/drive-mapping.json` | Mapeamento git_slug → drive_folder/drive_prefix |
| `base/drive-sync.log.jsonl` | Log append-only dos syncs pro Drive |

## Histórico

- **V1** (`gerar_template_dinamico.py`): deprecated — problema de PUs absurdos e briefing sem cascata (Patricia, mar/2026)
- **V2 pré-híbrido** (até 2026-04-13): bottom-up 18 MGs + BRIEFING 14 dropdowns. Índices travados "NÃO EDITAR".
- **V2 Híbrido** (2026-04-14, Fase 19): adição da coluna Override, 3 novos índices, pré-preenchimento do BRIEFING via config, fix encoding UTF-8.

## Exemplos reais (pacotes 2026-04-14)

| Projeto | Padrão Gemma | AC | UR | Config |
|---|---|---|---|---|
| arthen-arboris | medio-alto | 12.473 | 98 | [parametrico-v2-config.json](pacotes/arthen-arboris/parametrico-v2-config.json) |
| placon-arminio-tavares | medio | 4.090 | 55 | [parametrico-v2-config.json](pacotes/placon-arminio-tavares/parametrico-v2-config.json) |
| thozen-electra | alto | 37.894 | 348 | [parametrico-v2-config.json](pacotes/thozen-electra/parametrico-v2-config.json) |

Todos em `base/pacotes/{slug}/` com `parametrico-{slug}.{xlsx,docx,pdf}`.
