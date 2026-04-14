# ORCAMENTO-WORKFLOW.md — Workflow Completo de Orçamentação

**Última atualização:** 13/abril/2026  
**Baseado em:** Projeto Oxford 600 Residence (Mussi Empreendimentos)

---

## Base Enriquecida (atualizada 14/04/2026)

Antes de iniciar qualquer paramétrico ou executivo novo, **consultar a base de índices master** que consolida TUDO:

**`base/base-indices-master-YYYY-MM-DD.json`** (322 KB, consolidado) — contém:

- **Índices V2 originais** (produto, estruturais, instalações, CI, macrogrupo, segmento)
- **29 novos índices derivados cross-projeto** (PU concreto, PU aço, custo esquadrias/m² AC, etc.)
- **Top 500 PUs cross-projeto** agregados de 4.210 clusters (Fase 10)
- **Curva ABC master** (126 projetos)
- **5 cross-insights Gemma** (famílias, outliers, padrões, novos índices, lacunas)
- **Camada qualitativa** em cada `indices-executivo/[projeto].json` → chave `qualitative`

### Como usar antes de gerar um orçamento

1. **Consulta PU de um item específico**:
   ```python
   import json
   master = json.load(open("base/base-indices-master-2026-04-13.json"))
   for pu in master["pus_agregados_top_500"]:
       if "concreto fck 30" in pu["desc"].lower():
           print(pu["desc"], "mediana R$", pu["pu_mediana"], "±", pu["cv"]*100, "%")
   ```

2. **Consulta índice derivado** (custo esquadrias/m² AC, etc.):
   ```python
   idx = master["indices_derivados_v2"]["custo_esquadrias_rsm2"]
   print(f"mediana R$ {idx['mediana']}/m² AC, n={idx['n']} projetos")
   # Para projeto com AC 15000: valor esperado = idx['mediana'] * 15000
   ```

3. **Buscar projetos similares** (sub-disciplinas + premissas):
   ```python
   # Ver: scripts/consulta_similares.py -> projetos_similares()
   # Já usado automaticamente pelo gerar_pacote.py
   ```

**Documentação canônica:** `~/orcamentos-openclaw/base/CAMADA-QUALITATIVA-GEMMA.md`
**Roadmap:** `~/orcamentos-openclaw/base/FASES-FUTURAS.md`

**Estatísticas da base (14/04/2026):**
- 126 projetos com camada qualitativa completa
- 4.210 PUs cross-projeto medianos (Fase 10)
- 29 novos índices derivados (Fase 13)
- 333k itens detalhados (Fase 1)
- ~1.200 comentários + ~150k textos livres (Fase 8)
- 35.147 composições unitárias classificadas (Fase 4)

---

## Visão Geral

Este documento descreve o processo completo de orçamentação da Cartesian Engenharia, desde o recebimento do projeto até a entrega dos orçamentos paramétrico e executivo.

**Tempo estimado:** 4-6 horas (otimizado após lições do Oxford)

**Entregáveis:**
1. Orçamento Paramétrico (Excel 14 abas)
2. Orçamento Executivo (Excel 8 abas)
3. Memorial Descritivo (Markdown → DOCX)
4. Briefing Final (consolidação de dados)

---

## Lições Aprendidas — LEIA PRIMEIRO

**Documento obrigatório:** [LICOES-APRENDIDAS-OXFORD.md](LICOES-APRENDIDAS-OXFORD.md)

Antes de iniciar qualquer orçamento, consulte as lições aprendidas do projeto Oxford (12 seções, 18 KB). Este documento contém:
- Armadilhas identificadas e como evitá-las
- Boas práticas validadas
- Checklist otimizado (4 fases)
- Stack técnico validado

**Principais alertas:**
⚠️ Solicitar dados críticos NO DIA 0 (quadro de áreas, memorial, especificações)  
⚠️ Validar completude do IFC antes de confiar 100%  
⚠️ Usar timeout realista (15-20 min para processamento pesado)  
⚠️ Sempre incluir rastreabilidade memorial ↔ orçamento

---

## Fase 1: Recebimento do Projeto (Dia 0)

### 1.1 Solicitar ao Cliente

**Documentos obrigatórios:**
- [ ] Quadro de áreas geral (AC total, AT, áreas por pavimento)
- [ ] Projeto de implantação (com AT, projeções, cortes)
- [ ] Memorial descritivo (se existir)
- [ ] Especificações de acabamento
- [ ] Data-base de preços/CUB
- [ ] Arquivo IFC (se disponível)
- [ ] Quantitativos executivos (se disponíveis)

**Por que isso é crítico:**
Dados faltantes (AC, AT, CUB) bloqueiam orçamento paramétrico preciso. No Oxford, usamos estimativas mas geraram bloqueadores. Solicitar no Dia 0 evita retrabalho.

### 1.2 Análise Preliminar

**Inventário de arquivos:**
```bash
cd ~/orcamentos/projetos/<nome-projeto>
find . -name "*.pdf" | wc -l     # Contar PDFs
find . -name "*.xlsx" | wc -l    # Contar planilhas
find . -name "*.ifc" | wc -l     # Verificar IFC
ls -lh *.ifc                      # Tamanho do IFC
```

**Classificar por disciplina:**
- Arquitetura: quantos PDFs?
- Estrutura: quantos PDFs? Tem IFC?
- Hidrossanitário: PDFs ou XLSX?
- Elétrico: quantos PDFs? Tem quadro de cargas?
- PPCI: PDFs ou memoriais descritivos?

**Estimar tempo:**
- Regra geral: ~2 min por PDF pesado
- Se >50 PDFs numa disciplina: usar amostragem inteligente
- IFC estrutural: ~15 min de processamento

**Identificar bloqueadores:**
- Dados faltantes críticos (AC, AT, memorial)
- Disciplinas sem documentação
- Qualidade dos arquivos (PDFs escaneados vs nativos)

---

## Fase 2: Análise por Disciplina (Dias 1-2)

### 2.1 Onda 1: Arquitetura (SEMPRE PRIMEIRO)

**Objetivo:** Extrair estrutura geral do projeto

**Processar:**
- Plantas baixas de todos os pavimentos
- Cortes e fachadas
- Quadro de áreas (se disponível)

**Extrair:**
- Número de pavimentos
- Altura total
- Distribuição de pavimentos (garagens, tipos, lazer, técnicos)
- Tipologias (identificar pavimentos tipo idênticos)
- Áreas por pavimento
- Número de vagas
- Áreas de lazer
- Número de unidades (estimado se necessário)

**⚠️ IDENTIFICAR BLOQUEADORES AQUI**

Se faltar AC, AT, ou outros dados críticos → **AVISAR CLIENTE IMEDIATAMENTE**

**Output:** `<projeto>-dados-arquitetura.md`

**Timeout subagente:** 10 min

---

### 2.2 Onda 2: IFC Estrutural (se disponível)

**⚠️ VALIDAR COMPLETUDE PRIMEIRO**

Antes de confiar no IFC, verificar:
```python
import ifcopenshell
ifc = ifcopenshell.open('estrutura.ifc')

# Verificar lajes
slabs = ifc.by_type('IfcSlab')
print(f"Lajes: {len(slabs)}")
# Verificar se têm volume
for slab in slabs[:5]:
    for prop in slab.IsDefinedBy:
        # Verificar se 'Volume' está preenchido
        
# Verificar vigas
beams = ifc.by_type('IfcBeam')
print(f"Vigas: {len(beams)}")

# Verificar pilares
columns = ifc.by_type('IfcColumn')
print(f"Pilares: {len(columns)}")

# Verificar fundação
footings = ifc.by_type('IfcFooting')
print(f"Fundação: {len(footings)}")
```

**IFC estrutural comum:**
- ✅ Lajes: geralmente OK (volumes preenchidos)
- ⚠️ Vigas/pilares: muitas vezes sem volumes
- ❌ Fundação: raramente modelada
- ❌ Aço/formas: quase nunca modelados

**Se IFC incompleto:** Complementar com PDFs (próxima onda)

**Output:** 
- `<projeto>-ifc-dados-brutos.json` (JSON completo)
- `<projeto>-quantitativos-estrutura.md` (consolidado)

**Timeout subagente:** 15 min

---

### 2.3 Onda 3: Estrutura Complementar (PDFs)

**Se IFC incompleto ou inexistente:**

**Estratégia — Amostragem Inteligente:**

1. **Identificar pavimentos tipo** (da análise arquitetura)
   - Ex: Oxford tinha 17 pavimentos tipo idênticos (7º-23º)

2. **Processar amostra representativa:**
   - 1 pavimento tipo completo
   - 1 pavimento garagem completo
   - 1 pavimento térreo/lazer
   - Fundação completa
   - Cobertura/técnico

3. **Aplicar multiplicadores validados:**
   - Pavimentos tipo: ×N (N = número de pavimentos idênticos)
   - Garagens: ×M (se idênticas)

**Exemplo Oxford:**
- 170 PDFs estruturais total
- Processados: 27 PDFs (16% do total)
- Cobertura: 100% via multiplicadores (×4 garagens, ×16 tipos)

**Validação:**
- Taxa de aço: 70-90 kg/m³ concreto (padrão mercado)
- Se fora da faixa: revisar quantitativos

**Output:** `<projeto>-quantitativos-estrutura.md` (atualizado)

**Timeout subagente:** 20 min (processamento pesado)

---

### 2.4 Onda 4: Hidrossanitário

**Prioridade: Planilhas XLSX > PDFs**

Se cliente forneceu planilhas de quantitativos (ideal):
```python
import pandas as pd

# Consolidar múltiplas planilhas
dfs = []
for xlsx in ['hidro_pav1.xlsx', 'hidro_pav2.xlsx', ...]:
    df = pd.read_excel(xlsx)
    dfs.append(df)

df_consolidado = pd.concat(dfs)
# Agrupar por material/diâmetro
```

Se só PDFs:
- Aplicar amostragem inteligente (mesmo princípio da estrutura)
- Multiplicadores por pavimento tipo

**Subsistemas a consolidar:**
1. Água Fria (tubulação, reservatórios, conexões)
2. Esgoto Sanitário (tubulação, caixas, conexões)
3. Águas Pluviais (calhas, condutores, caixas)
4. Gás (central, tubulação, medidores)
5. Louças e Metais (estimativa por tipologia)

**Output:** `<projeto>-quantitativos-hidro.md`

**Timeout subagente:** 10-15 min (depende se XLSX ou PDF)

---

### 2.5 Onda 5: Elétrico

**Buscar quadro de cargas consolidado** (prancha específica)

**Extrair:**
- Potência instalada total (kW)
- Potência demandada (kW)
- Fator de demanda
- Transformador (kVA)
- Gerador (kVA, se houver)
- Número de quadros elétricos
- Distribuição por pavimento
- SPDA (tipo, número de captores)
- CFTV/Automação (câmeras, pontos de rede)

**Validações:**
- Potência demandada vs capacidade do transformador (margem 10-20%)
- Dimensionamento do gerador (se houver)

**Se dados incompletos:**
- Estimar com base em NBR 5410
- Padrões de mercado por tipologia/área

**Output:** `<projeto>-dados-eletrico.md`

**Timeout subagente:** 15 min

---

### 2.6 Onda 6: PPCI

**Priorizar memoriais descritivos** (mais confiáveis que plantas)

**Sistemas obrigatórios (conforme COE):**
1. Hidrantes (RTI, hidrantes internos, bombas)
2. Extintores (tipos, quantidades)
3. Detecção e Alarme (central, detectores, acionadores)
4. Iluminação de Emergência (blocos autônomos)
5. Sinalização (placas fotoluminescentes)
6. Pressurização de Escadas (ventiladores, dampers)
7. Desenfumagem (exaustores, dampers)
8. Elevador de Emergência (se aplicável)
9. Central de Gás (se aplicável)

**Validar aprovação CBMSC:**
- Data de aprovação
- Responsável técnico
- Número do processo (se disponível)

**Output:** `<projeto>-dados-ppci.md`

**Timeout subagente:** 15 min

---

## Fase 3: Geração de Entregáveis (Dia 3)

### 3.1 Briefing Final

**Consolidar dados confirmados vs estimados vs indisponíveis**

**Estrutura:**
```markdown
# BRIEFING FINAL — <PROJETO>

## 1. DADOS CONFIRMADOS ✅
(dados extraídos com alta confiança)

## 2. DADOS ESTIMADOS ⚠️
(estimativas técnicas — validar com cliente)

## 3. DADOS INDISPONÍVEIS ❌
(bloqueadores críticos)

## 4. DADOS ADICIONAIS
(informações complementares fora das 25 perguntas)

## 5. PRÓXIMOS PASSOS
(o que solicitar ao cliente)
```

**25 perguntas do sistema paramétrico:**
Ver `~/clawd/orcamento-parametrico/scripts/gerar_template_dinamico.py`

**Output:** `<projeto>-Briefing-Final-<data>.md`

**Timeout subagente:** 10 min

---

### 3.2 Orçamento Paramétrico

**Script:** `~/clawd/orcamento-parametrico/scripts/gerar_template_dinamico.py`

**Parâmetros obrigatórios:**
```python
parametros = {
    'nome_projeto': 'Oxford 600 Residence',
    'data_base': 'mar/2026',
    'area_total': 7500,  # m² (AC total)
    'area_terreno': 1200,  # m² (AT)
    # ... (25 parâmetros do briefing)
}
```

**Sistema de validação:**
- Semáforo P10-P90 automático (verde/amarelo/vermelho)
- Aba "ALERTAS" destacando dados fora da faixa
- Ressalvas sobre estimativas

**Output:** `<PROJETO>-Orcamento-Parametrico-<data>.xlsx` (14 abas)

**Timeout subagente:** 10 min

---

### 3.3 Orçamento Executivo

**Consolidar quantitativos de todas as disciplinas**

**Estrutura (8 abas):**
1. RESUMO (totais por sistema + BDI)
2. ESTRUTURA (fundação, lajes, vigas, pilares, formas)
3. HIDROSSANITÁRIO (água, esgoto, pluvial, gás, louças)
4. ELÉTRICO (entrada, distribuição, iluminação, SPDA, CFTV)
5. PPCI (todos os 9 sistemas)
6. VEDAÇÕES (alvenaria, drywall)
7. ACABAMENTOS (pisos, paredes, forros, esquadrias)
8. LAZER (piscina, fitness, paisagismo, equipamentos)

**Formatação profissional:**
- Bordas em todas as células
- Cabeçalhos com cor de fundo
- Hierarquia clara (grupo > subgrupo > item)
- Subtotais por grupo
- BDI 25% (padrão Cartesian)
- Total geral destacado

**Custos unitários:**
- SINAPI (data-base atualizada)
- Cotações de fornecedores (quando aplicável)

**Output:** `<PROJETO>-Orcamento-Executivo-<data>.xlsx` (8 abas)

**Timeout subagente:** 10-15 min

---

### 3.4 Memorial Descritivo

**⚠️ INCLUIR RASTREABILIDADE DESDE O INÍCIO**

**Estrutura (14 seções):**
1. Identificação do Empreendimento
2. Características Gerais
3. Sistema Estrutural
4. Vedações e Divisórias
5. Instalações Hidrossanitárias
6. Instalações Elétricas
7. PPCI (Prevenção Contra Incêndio)
8. Esquadrias
9. Revestimentos e Acabamentos
10. Cobertura
11. Elevadores
12. Áreas de Lazer
13. Normas Técnicas
14. Observações Finais

**EM CADA SISTEMA: Tabelas de Rastreabilidade**

Formato obrigatório:
```markdown
**Tabela X.Y — <Nome do Sistema>**

| Item | Especificação | Unidade | Quantidade | Ref. Orçamento |
|------|---------------|---------|------------|----------------|
| ... | ... | ... | ... | Aba ESTRUTURA, Item 1.1 |
```

**Número de tabelas esperado:** ~20-25

**Rastreabilidade = Memorial útil**
- Cliente consegue entender de onde vêm os custos
- Memorial vira ferramenta de gestão (não só documento burocrático)
- Facilita validação técnica

**Output:** `<PROJETO>-Memorial-Descritivo.md` (pronto pra conversão DOCX)

**Timeout subagente:** 15 min

---

## Fase 4: Validação e Entrega (Dia 4)

### 4.1 Validações Técnicas

**Estrutura:**
- [ ] Taxa de aço: 70-90 kg/m³ concreto
- [ ] Volumes de concreto coerentes com área/pavimentos
- [ ] fck apropriado por elemento

**Elétrico:**
- [ ] Potência demandada vs transformador (margem 10-20%)
- [ ] Gerador dimensionado corretamente (se houver)
- [ ] SPDA conforme NBR 5419

**Hidro:**
- [ ] Reservatórios vs população/demanda
- [ ] RTI vs número de hidrantes (NBR 13714)

**Geral:**
- [ ] Custo/m² vs CUB da região (±20%)
- [ ] Todos os dados estimados claramente marcados
- [ ] Referências cruzadas memorial ↔ orçamento funcionando

### 4.2 Documentação Final

**Criar README no projeto:**
```markdown
# <NOME DO PROJETO>

## Entregáveis
1. [Orçamento Paramétrico](link)
2. [Orçamento Executivo](link)
3. [Memorial Descritivo](link)
4. [Briefing Final](link)

## Dados Faltantes / Validações Pendentes
- [ ] Item 1
- [ ] Item 2

## Próximos Passos
1. ...
2. ...
```

**Backup antes de enviar:**
```bash
cd ~/orcamentos/projetos/<projeto>
tar -czf backup-entregaveis-$(date +%Y%m%d).tar.gz *.xlsx *.md
```

---

## Stack Técnico Validado

**Python:**
- `ifcopenshell` → IFC estrutural ✅
- `pandas` + `openpyxl` → Excel (leitura/escrita) ✅
- `pdfplumber` → Extração de PDFs ✅

**Comandos shell úteis:**
- `find . -name "*.pdf" | wc -l` → contar PDFs
- `ls -lh` → verificar tamanho de arquivos
- `grep -c "padrão"` → validar conteúdo

**Formatação:**
- Markdown → documentação (fácil conversão pra DOCX)
- Excel → orçamentos (openpyxl com formatação profissional)

---

## Métricas de Referência (Projeto Oxford)

**Inputs:**
- 779 arquivos processados
- 1 IFC estrutural (21 MB)

**Processamento:**
- 15 ondas de análise/geração
- 13 subagents lançados
- ~6h30 de trabalho total

**Outputs:**
- 4 entregáveis principais
- 10 arquivos de análise intermediária
- 1 documento de lições aprendidas

**Precisão alcançada:**
- Estrutura: alta (IFC + PDFs)
- Hidro: alta (planilhas executivas)
- Elétrico: média (estimativas calibradas)
- PPCI: alta (memoriais completos)

---

## Checklist Rápido — Resumo Executivo

### ✅ SEMPRE FAZER

- [ ] Solicitar dados críticos no Dia 0
- [ ] Validar completude do IFC antes de confiar
- [ ] Usar timeout mínimo 15 min para processamento pesado
- [ ] Aplicar amostragem inteligente + multiplicadores
- [ ] Incluir rastreabilidade memorial ↔ orçamento
- [ ] Marcar estimativas claramente (✅ ⚠️ ❌)
- [ ] Validar dados críticos (taxa aço, potência vs trafo, etc.)
- [ ] Fazer backup antes de enviar

### ⛔ NUNCA FAZER

- [ ] Confiar 100% em IFC sem validar completude
- [ ] Usar timeout otimista (<15 min) para >20 PDFs
- [ ] Tentar processar centenas de PDFs sem amostragem
- [ ] Entregar estimativas sem marcar claramente
- [ ] Pular validações cruzadas
- [ ] Assumir tipo de laje sem validar

---

## Referências

- **Lições Aprendidas:** [LICOES-APRENDIDAS-OXFORD.md](LICOES-APRENDIDAS-OXFORD.md)
- **Sistema Paramétrico:** `~/clawd/orcamento-parametrico/`
- **Scripts IFC:** `~/orcamentos/scripts/`
- **Projetos Anteriores:** `~/orcamentos/projetos/`

---

**FIM DO DOCUMENTO**

*Este workflow deve ser consultado no início de TODOS os projetos de orçamentação.*
