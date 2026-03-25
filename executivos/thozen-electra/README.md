# Thozen Electra — Orçamento Executivo

**Cliente:** Thozen  
**Empreendimento:** Electra  
**Tipo:** Residencial vertical (32 pavimentos)

---

## 📁 Estrutura de Arquivos

```
executivo/thozen-electra/
├── README.md                  # Este arquivo
├── briefings/                 # Briefings por disciplina
│   ├── alvenaria-r00.md       # Briefing de alvenaria (estrutura)
│   ├── alvenaria-r00-RESUMO.md
│   └── alvenaria-r00-CHECKLIST.md
├── planilhas/                 # Planilhas Excel geradas (futuro)
│   └── alvenaria-r01.xlsx
└── quantitativos/             # JSONs de quantitativos extraídos
    └── alvenaria/
        ├── 01-Terreo.json
        ├── 02-G1.json
        ├── ...
        └── relatorio-consolidado.md
```

---

## 🏗️ Disciplinas Disponíveis

### ✅ 03 ALVENARIA (Em Progresso)

**Status:** Briefing estruturado gerado (R00)  
**Fontes:** 18 DWG (R01)  
**Próximo passo:** Conversão DWG → DXF e extração de quantitativos

**Arquivos:**
- **Briefing:** `briefings/alvenaria-r00.md`
- **Resumo:** `briefings/alvenaria-r00-RESUMO.md`
- **Checklist:** `briefings/alvenaria-r00-CHECKLIST.md`

**Scripts de processamento:**
- `scripts/extrair_alvenaria_dxf.py` — Extração de quantitativos de DXF
- `scripts/processar_todos_alvenaria.sh` — Processamento em lote

**Limitação atual:** Arquivos em formato DWG — requer conversão via ODA File Converter.

---

### ⏳ Próximas Disciplinas (Planejadas)

#### 01 ESTRUTURA
- **Fonte:** DWG + IFC ✅
- **Objetivo:** N1 03 Infraestrutura + N1 04 Supraestrutura
- **Prioridade:** 🔴 ALTA

#### 02 ARQUITETURA
- **Fonte:** DWG + IFC ✅
- **Objetivo:** Quantitativos gerais (AC, áreas, pés-direitos)
- **Prioridade:** 🔴 ALTA

#### 05 HIDRÁULICO + 06 SANITÁRIO
- **Fonte:** DWG + IFC ✅
- **Objetivo:** N1 06 Instalações Hidrossanitárias
- **Prioridade:** 🔴 ALTA

#### 09 ELÉTRICO + 10 TELEFONIA + 11 SPDA
- **Fonte:** DWG + IFC (exceto SPDA: só DWG)
- **Objetivo:** N1 07 Instalações Elétricas
- **Prioridade:** 🟡 MÉDIA

#### 04 ESQUADRIA
- **Fonte:** DWG
- **Objetivo:** N1 13 Esquadrias
- **Prioridade:** 🟡 MÉDIA

#### 07 PCI CIVIL + 08 PCI ELÉTRICO
- **Fonte:** DWG + IFC ✅
- **Objetivo:** N1 14.01 PCI
- **Prioridade:** 🟡 MÉDIA

#### 12 VENTILAÇÃO + 13 EXAUSTÃO + 14 AR-CONDICIONADO
- **Fonte:** DWG
- **Objetivo:** N1 14 Instalações Especiais
- **Prioridade:** 🟢 BAIXA

---

## 🛠️ Workflow de Processamento

### Passo 1 — Conversão de DWG para DXF (quando necessário)

Disciplinas com apenas DWG (Alvenaria, Esquadria, SPDA, etc.) requerem conversão:

```bash
# Instalar ODA File Converter (macOS)
brew install --cask oda-file-converter

# Converter DWG → DXF
oda-file-converter \
  --input "projetos/thozen-electra/projetos/03 ALVENARIA/" \
  --output "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/" \
  --format DXF \
  --version R2018
```

### Passo 2 — Extração de Quantitativos

#### Para DXF (Alvenaria, Esquadria, etc.):
```bash
# Processar um arquivo
python3.11 scripts/extrair_alvenaria_dxf.py \
  "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/RA_ALV_EXE_01_TERREO.dxf" \
  --pavimento "Térreo" \
  --output "executivo/thozen-electra/quantitativos/alvenaria/01-Terreo.json"

# Processar todos (em lote)
./scripts/processar_todos_alvenaria.sh
```

#### Para IFC (Estrutura, Arquitetura, Hidráulico, etc.):
```bash
# Processar IFC com ifcopenshell (script a criar)
python3.11 scripts/extrair_ifc.py \
  "projetos/thozen-electra/projetos/01 ESTRUTURA/arquivo.ifc" \
  --disciplina "estrutura" \
  --output "executivo/thozen-electra/quantitativos/estrutura/quantitativos.json"
```

### Passo 3 — Gerar Briefing

Os briefings seguem a estrutura:
1. **Resumo Executivo** — Visão geral do projeto
2. **Premissas de Projeto** — Especificações, padrões, normas
3. **Quantitativos** — Tabelas detalhadas (estrutura preparada)
4. **Fontes de Dados** — Arquivos processados, referências
5. **Observações e Dados Faltantes** — Identificação de gaps

### Passo 4 — Preencher Quantitativos

Com os JSONs gerados, preencher as tabelas do briefing:
- Substituir `[A EXTRAIR]` por valores reais
- Substituir `[A CALCULAR]` por totais calculados
- Atualizar seção de fontes (marcar arquivos como ✅ PROCESSADO)

### Passo 5 — Gerar Planilha Excel

```bash
# Gerar planilha compatível com Memorial Cartesiano
python3.11 scripts/gerar_planilha_alvenaria.py \
  --input "executivo/thozen-electra/quantitativos/alvenaria/" \
  --output "executivo/thozen-electra/planilhas/alvenaria-r01.xlsx"
```

### Passo 6 — Upload no Slack

```bash
# Upload da planilha (SEMPRE com --thread e --channel)
python3.11 scripts/slack_uploader.py \
  --bot cartesiano \
  --file executivo/thozen-electra/planilhas/alvenaria-r01.xlsx \
  --thread <thread_ts> \
  --channel <channel_id> \
  --comment "Planilha executiva de alvenaria — Thozen Electra R01"
```

---

## 📊 Estrutura do Memorial Cartesiano

As planilhas geradas seguem a hierarquia:

- **N1** — Macrogrupo (ex: 09 Alvenaria)
  - **N2** — Subgrupo (ex: 09.01 Alvenaria de Vedação)
    - **N3** — Item (ex: 09.01.01 Blocos Cerâmicos)

### Mapeamento Disciplina → N1 Memorial

| Disciplina | N1 Memorial | Observação |
|------------|-------------|------------|
| 01 ESTRUTURA | 03 Infraestrutura + 04 Supraestrutura | Separar fundações de estrutura |
| 02 ARQUITETURA | (Referência) | Não gera N1 direto — fonte de áreas |
| 03 ALVENARIA | 09 Alvenaria | |
| 04 ESQUADRIA | 13 Esquadrias | |
| 05 HIDRÁULICO | 06.01 Água Fria | |
| 06 SANITÁRIO | 06.02 Esgoto + 06.03 Águas Pluviais | |
| 07 PCI CIVIL | 14.01 PCI Civil | |
| 08 PCI ELÉTRICO | 14.01 PCI Elétrico | |
| 09 ELÉTRICO | 07.01 Instalações Elétricas | |
| 10 TELEFÔNICO | 14.09 Telefonia/Dados | |
| 11 SPDA | 07.02 SPDA | |
| 12 VENTILAÇÃO | 14.08 Ventilação Mecânica | |
| 13 EXAUSTÃO | 14.08 Exaustão | |
| 14 AR-CONDICIONADO | 14.02 Climatização | |

---

## 🎯 Status Atual (2026-03-20)

### ✅ Concluído
- [x] Mapeamento de arquivos disponíveis (todas as disciplinas)
- [x] Estrutura de pastas criada (`executivo/thozen-electra/`)
- [x] Briefing de alvenaria estruturado (R00)
- [x] Scripts de processamento criados:
  - `extrair_alvenaria_dxf.py`
  - `processar_todos_alvenaria.sh`

### ⏳ Em Andamento
- [ ] Conversão DWG → DXF (alvenaria)
- [ ] Extração de quantitativos (alvenaria)
- [ ] Validação de dados

### 📅 Próximos Passos
1. Converter DWGs de alvenaria para DXF (ODA File Converter)
2. Processar DXFs e gerar JSONs de quantitativos
3. Preencher briefing de alvenaria (R01)
4. Gerar planilha executiva de alvenaria
5. Iniciar próxima disciplina (sugestão: ESTRUTURA ou HIDRÁULICO)

---

## 📞 Suporte

**Subagent:** `extração-alvenaria-electra` (Cartesiano)  
**Canal:** Slack — #custos-ia-paramétrico ou #ctn-team-comercial  
**Documentação:** Este README + briefings em `briefings/`

Para dúvidas ou problemas:
1. Verificar briefing da disciplina (`briefings/<disciplina>-r00.md`)
2. Verificar checklist (`briefings/<disciplina>-r00-CHECKLIST.md`)
3. Consultar `scripts/` para exemplos de processamento

---

**Última atualização:** 2026-03-20 10:33 BRT  
**Responsável:** Cartesiano (Cartesian Engenharia)
