# ✅ Checklist de Próximas Ações - Exaustão Churrasqueiras

## Status Atual
- ✅ Briefing técnico gerado (com premissas)
- ✅ Estrutura de tabelas preparada
- ⚠️ Quantitativos ESTIMADOS (não extraídos do DWG)
- ❌ Planilha executiva NÃO gerada (aguardando dados reais)

---

## Etapa 1: Obter Dados Reais do DWG

### Opção A: Converter DWG → DXF (RECOMENDADO)
- [ ] Baixar ODA File Converter: https://www.opendesign.com/guestfiles/oda_file_converter
- [ ] Instalar o conversor (free, oficial)
- [ ] Converter `RA_CHU_EXE_PROJETO_R00.dwg` → DXF R2013 ou superior
- [ ] Salvar DXF em: `executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.dxf`
- [ ] Rodar script de extração:
  ```bash
  python3.11 scripts/process_dxf.py executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.dxf
  ```

### Opção B: Gerar PDF Plotado
- [ ] Abrir `RA_CHU_EXE_PROJETO_R00.dwg` em AutoCAD/BricsCAD/DraftSight
- [ ] Plotar para PDF (escala 1:50 ou 1:100, legível)
- [ ] Salvar em: `executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.pdf`
- [ ] Extrair manualmente os dados (ver lista abaixo)

### Opção C: Revisão Manual no CAD
- [ ] Abrir `RA_CHU_EXE_PROJETO_R00.dwg` em software CAD
- [ ] Extrair diretamente do projeto (ver lista de dados críticos abaixo)

---

## Etapa 2: Dados Críticos a Extrair

### Equipamentos Principais
- [ ] **Quantidade de churrasqueiras atendidas:** ___ UN
- [ ] **Dimensões de cada churrasqueira:** ___ x ___ m (LxP)
- [ ] **Quantidade de exaustores:** ___ UN
- [ ] **Vazão de cada exaustor:** ___ m³/h
- [ ] **Pressão estática de projeto:** ___ mmCA
- [ ] **Potência dos motores:** ___ CV ou ___ kW
- [ ] **Rotação:** ___ rpm
- [ ] **Tensão de alimentação:** ___ V (monofásico/trifásico)

### Coifas
- [ ] **Quantidade de coifas:** ___ UN
- [ ] **Dimensões de cada coifa:** ___ x ___ x ___ m (LxPxH)
- [ ] **Material:** Inox AISI ___ ou ___
- [ ] **Filtros:** Tipo ___ (labirinto/baffle)
- [ ] **Iluminação integrada:** Sim / Não → ___ W, ___ UN por coifa

### Dutos e Conexões
- [ ] **Metragem de duto horizontal no lazer:** ___ m
  - Diâmetro/seção: ___
  - Material: Chapa #___ galv. / inox
- [ ] **Metragem de duto vertical (prumada):** ___ m
  - Diâmetro: Ø ___ mm
  - Material: Chapa #___ galv. / inox
- [ ] **Curvas 90°:** ___ UN (Ø ___ mm)
- [ ] **Joelhos 90°:** ___ UN (Ø ___ mm)
- [ ] **Transições:** ___ UN (retangular → circular)
- [ ] **Dampers corta-fogo:** ___ UN (Ø ___ mm)
- [ ] **Registros de gaveta (damper manual):** ___ UN
- [ ] **Chapéu de exaustão:** ___ UN (Ø ___ mm)

### Grelhas de Ventilação
- [ ] **Quantidade de grelhas de admissão:** ___ UN
- [ ] **Dimensões:** ___ x ___ mm
- [ ] **Material:** Alumínio / Inox / ___
- [ ] **Área livre por grelha:** ___ m²

### Instalação Elétrica
- [ ] **Quadro de origem:** QD ___ (Lazer / Térreo / outro)
- [ ] **Circuito para cada exaustor:**
  - Disjuntor: ___ A, ___ polos
  - Cabo: ___ mm² (3F+N+T / outro)
  - Metragem: ___ m
- [ ] **Contatores:** ___ UN, ___ A
- [ ] **Relés térmicos:** ___ UN, ___ A
- [ ] **Botoeiras de comando:** ___ UN (local / remoto)
- [ ] **Automação/controle:**
  - Tipo: Manual / Automático / BMS
  - Sensores: ___ UN (temperatura / fumaça)
  - CLP: Sim / Não

---

## Etapa 3: Compatibilizações

### Cruzar com Disciplina Elétrico (09)
- [ ] Abrir: `projetos/thozen-electra/projetos/09 ELÉTRICO/`
- [ ] Verificar:
  - [ ] Alimentação elétrica dos exaustores já está prevista?
  - [ ] Quadro de origem e circuitos estão dimensionados?
  - [ ] Cabos e eletrodutos já estão quantificados?
- [ ] Atualizar briefing com dados reais da elétrica

### Cruzar com Arquitetura (02)
- [ ] Abrir: `projetos/thozen-electra/projetos/02 ARQUITETURA/DWG/RA_ARQ_EXE_07_LAZER_R02.dwg`
- [ ] Verificar:
  - [ ] Localização exata das churrasqueiras no lazer
  - [ ] Pé-direito do ambiente
  - [ ] Acabamentos (coifa aparente ou embutida?)
  - [ ] Grelhas de ventilação: localização e dimensões
- [ ] Identificar interferências ou ajustes necessários

### Cruzar com Estrutura (01)
- [ ] Verificar:
  - [ ] Passagem da prumada vertical pelos pavimentos
  - [ ] Diâmetro dos furos necessários nas lajes
  - [ ] Reforços estruturais (se aplicável)
- [ ] Marcar pontos de interferência no briefing

### Cruzar com PCI Civil (07)
- [ ] Verificar:
  - [ ] Dampers corta-fogo são obrigatórios na prumada?
  - [ ] Proteção passiva de dutos (manta, tinta intumescente?)
  - [ ] Integração com sistema de detecção/alarme
- [ ] Atualizar briefing com requisitos de PCI

---

## Etapa 4: Validação com Equipe de Projetos

- [ ] Confirmar premissas técnicas:
  - [ ] Sistema é centralizado (1 exaustor para todas) OU individualizado (1 por churrasqueira)?
  - [ ] Controle é manual OU automático?
  - [ ] Há integração com BMS/automação predial?
- [ ] Revisar especificações:
  - [ ] Material dos dutos: galvanizado OU inox?
  - [ ] Acabamento das coifas: escovado, polido, outro?
  - [ ] Isolamento térmico dos dutos: necessário?
- [ ] Validar normas aplicáveis:
  - [ ] Código Sanitário Municipal de São Paulo (CSMSP)
  - [ ] Instruções Técnicas do CBPMESP (se aplicável)
  - [ ] Exigências do condomínio/síndico

---

## Etapa 5: Atualizar Briefing com Dados Reais

- [ ] Abrir: `executivo/thozen-electra/briefings/exaustao-r00.md`
- [ ] Substituir valores estimados por dados reais extraídos
- [ ] Remover marcações "⚠️ A CONFIRMAR COM DWG"
- [ ] Adicionar seção "Dados Validados" com fonte e data
- [ ] Salvar como: `exaustao-r01.md` (nova revisão)

---

## Etapa 6: Gerar Planilha Executiva

- [ ] Usar template executivo: `executivo/templates/planilha-template.xlsx`
- [ ] Preencher abas:
  - [ ] 14.08.01 - Exaustores e Equipamentos
  - [ ] 14.08.02 - Dutos e Conexões
  - [ ] 14.08.03 - Grelhas e Acessórios
  - [ ] 14.08.04 - Instalação Elétrica Associada
  - [ ] 14.08.05 - Controles e Automação (se houver)
- [ ] Colunas: Código Memorial | Descrição | Especificação | UN | QTD | Preço Unit. | Total | Observação
- [ ] Incluir subtotais e totais por subdisciplina
- [ ] Salvar em: `executivo/thozen-electra/planilhas/exaustao-r01.xlsx`

---

## Etapa 7: Upload e Apresentação ao Time

- [ ] Upload da planilha no Slack:
  ```bash
  python3.11 scripts/slack_uploader.py \
    --bot cartesiano \
    --file executivo/thozen-electra/planilhas/exaustao-r01.xlsx \
    --thread <thread_ts> \
    --channel <channel_id> \
    --comment "Planilha executiva de exaustão (churrasqueiras) - Rev. R01"
  ```
- [ ] Apresentar resumo ao time:
  - [ ] Quantitativos principais
  - [ ] Interferências identificadas
  - [ ] Premissas validadas
  - [ ] Próximos passos (se houver)

---

## Observações Importantes

### Ferramentas Necessárias
- **ODA File Converter** (free) → https://www.opendesign.com/guestfiles/oda_file_converter
- Ou **AutoCAD** / **BricsCAD** / **DraftSight** (para abrir DWG)
- Python 3.11 + openpyxl (já instalado)

### Tempo Estimado
- Converter DWG → DXF: 10-15 min
- Extrair dados manualmente (se necessário): 1-2 horas
- Cruzar com outras disciplinas: 1-2 horas
- Atualizar briefing: 30 min
- Gerar planilha executiva: 1-2 horas
- **TOTAL:** 4-6 horas

### Prioridade
🟡 **MÉDIA** — Sistema complementar (não é crítico como estrutura ou instalações principais)

---

**Data de criação:** 2026-03-20  
**Responsável:** Time Cartesian (apoio: Cartesiano bot)  
**Status:** ⏳ Aguardando conversão do DWG → DXF
