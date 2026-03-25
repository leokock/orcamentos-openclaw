# Design: Processo de Orçamento Executivo com IA Copiloto

> **Objetivo:** Entregar orçamentos executivos com rastreabilidade total, usando IA como copiloto para velocidade e qualidade
> **Entrega tripla:** Excel (fórmulas vivas) + Memorial App (navegação visual) + Memorial Word (narrativa técnica)
> **Criado:** 23/mar/2026
> **Projeto piloto:** Thozen Electra (14 disciplinas, 197 arquivos de projeto)

---

## 1. Visao Geral

### O Problema

Orçamentos executivos completos exigem extração de quantitativos de dezenas de projetos (IFC, DWG, PDF), preenchimento de planilhas com centenas de itens por disciplina, validação de cada número, e documentação de onde veio cada valor. Feito manualmente, cada disciplina leva dias.

### A Solucao

**Discipline Packs** — o Cartesiano processa uma disciplina por vez e entrega um pacote completo:

```
DISCIPLINE PACK = Planilha .xlsx + Memorial .md + Relatório de Confiança
```

Leo valida focando nos pontos de atenção, incorpora na planilha grande, e o memorial acumula até virar o documento final.

### Cadeia de Rastreabilidade

```
Projeto (IFC/DWG/PDF)
  → Extração de quantitativos (script + IA)
    → Planilha da disciplina (quantidades + PU + total)
      → Fórmula na EAP (=SOMA da aba)
        → Memorial Word (fonte + premissa + decisão)
          → Memorial App (espelho visual pro cliente)
```

Cada número na EAP puxa da aba da disciplina. Cada número na aba tem fonte rastreável no memorial.

---

## 2. A Entrega Final

### 2.1 Excel — Orçamento Completo

Planilha grande (~34 abas) com fórmulas vivas:

| Camada | Exemplo | Função |
|--------|---------|--------|
| **CAPA** | Dados do empreendimento | AC, UR, pavimentos, áreas |
| **EAP Análise** | Resumo por macrogrupo | R$/m², %, comparativo entre revisões |
| **Ger_Executivo** | EAP hierárquica | CC.Etapa.Subetapa.Serviço (3000+ linhas) |
| **Abas de disciplina** | ELÉTRICO, HIDRO, etc. | Quantitativos detalhados com PU |

**Regra:** O valor na EAP nunca é digitado — sempre é fórmula que puxa da aba de quantitativos.

**Regra de detalhamento (Leo, 23/mar/2026):** Quantitativos SEMPRE abertos por pavimento. Pavimentos tipo repetidos podem ser agrupados (ex: "8° ao 31° Tipo — x24"), mas cada pavimento diferente (Térreo, Garagens, Lazer, Casa de Máquinas) tem linha própria. Estrutura: TORRE → PAVIMENTO → GRUPO → SUBGRUPO → item.

### 2.2 Memorial Word — Narrativa Técnica

Documento complementar (~50-100 páginas) com:

- **Por disciplina:** fontes usadas, revisão dos projetos, premissas adotadas, metodologia de extração
- **Relatório de confiança:** quais números são exatos, quais são estimados
- **Comparativo paramétrico:** R$/m² vs base histórica

Estrutura do documento:

```
1. Dados do Empreendimento
2. Metodologia
3. Resumo Executivo (tabela com todos os macrogrupos)
4. Disciplinas
   4.1 Movimentação de Terra
   4.2 Infraestrutura (Fundações)
   4.3 Contenção
   4.4 Supraestrutura
   ...
   4.N Imprevistos
5. Validação Paramétrica
6. Anexos (lista de projetos, versões, datas)
```

Cada seção de disciplina segue o template:

```markdown
### 4.8 Instalações Elétricas

**Valor total:** R$ 3.569.163,72
**R$/m²:** R$ 213,09
**Benchmark:** R$ 187-220/m² (base Cartesian, alto padrão) — DENTRO DA FAIXA

#### Fontes
- IFC: 9 arquivos (EL_R.Rubens Alves, rev.01, out/2025)
- DWG: 18 pranchas (mesma revisão)
- Memorial descritivo: não disponível

#### Premissas
- Pavimento tipo (8°~31°): multiplicado por 24 pavimentos
- Subestação: conforme projeto específico (transformador 500kVA + 300kVA)
- Preços unitários: base SINAPI mar/2026 + cotações fornecedores

#### Confiança
- 🟢 Subestação, gerador, entrada de energia (projeto detalhado)
- 🟡 Cabeamento por pavimento (metragem extraída de IFC, bitola dos DWGs)
- 🔴 Automação residencial (sem projeto específico, estimado por índice)

#### Observações
- IFCs em schema IFC2X3: geometria completa mas sem propriedades elétricas
- Quantitativos de tomadas/pontos de força complementados via DWG
```

### 2.3 Memorial App — Espelho Visual

Mesma estrutura do Excel, alimentado em paralelo. O cliente navega visualmente pela EAP e vê os mesmos números do Excel.

---

## 3. Fluxo de Trabalho — Ciclo de Uma Disciplina

### Passo 1: Leo Inicia a Disciplina

```
Leo: "Vamos fazer Instalações Elétricas"
```

O Cartesiano:
1. Identifica os arquivos disponíveis (IFC + DWG na pasta `projetos/09 ELÉTRICO/`)
2. Verifica se já existe briefing anterior (ex: `eletrico-r00.md`)
3. Lista o que vai processar e o que falta

### Passo 2: Extração de Quantitativos

O Cartesiano processa os arquivos em 3 camadas:

**Camada 1 — IFC (automatizado):**
- Script ifcopenshell extrai entidades por tipo (IfcFlowTerminal, IfcFlowSegment, etc.)
- Consolida por pavimento
- Aplica multiplicação de pavimentos tipo

**Camada 2 — DWG/DXF (semi-automatizado):**
- Converte DWG → DXF (ODA File Converter)
- Script ezdxf extrai informações das pranchas (tabelas, textos, blocos)
- Complementa o que faltou no IFC (bitolas, diâmetros, especificações)

**Camada 3 — Referência cruzada:**
- Compara quantidades IFC vs DWG (se ambos disponíveis)
- Flagga divergências significativas (>15%)
- Aplica preços unitários da base de referência

### Passo 3: Geração do Discipline Pack

O Cartesiano gera 3 arquivos:

**a) Planilha da disciplina** (`eletrico-r01.xlsx`):
- Mesma estrutura da planilha grande (Torre / Pavimento / Grupo / Subgrupo / Descrição / Qtd / Repetição / Perda / Unidade / PU / Total)
- Aba de resumo com total e R$/m²
- Pronta pra copy-paste na planilha grande

**b) Memorial da disciplina** (`eletrico-r01-memorial.md`):
- Fontes, premissas, metodologia, confiança, observações
- Cada seção referencia os arquivos de projeto específicos

**c) Relatório de confiança** (`eletrico-r01-confianca.md`):
- 🟢 Verde: número com fonte direta e verificável
- 🟡 Amarelo: número calculado/multiplicado (conferir lógica)
- 🔴 Vermelho: número estimado ou sem fonte (requer decisão do Leo)

### Passo 4: Leo Valida

Leo recebe o pack e:
1. **Revisa o vermelho** (~5-10 itens): decide, corrige ou confirma
2. **Confere o amarelo** (~10-20 itens): valida a lógica de multiplicação
3. **Confia no verde** (~80% dos itens): fonte rastreável, sem ação

Tempo estimado de revisão: **20-40 minutos** por disciplina (vs 3-4 horas manual)

### Passo 5: Consolidação

Leo incorpora na planilha grande:
1. Copy-paste dos valores da planilha da disciplina
2. Fórmulas na EAP já puxam automaticamente
3. Memorial acumula (append da seção)

### Passo 6: Validação Paramétrica

O Cartesiano valida o R$/m² da disciplina contra a base de 58+ projetos:
- Se dentro da faixa P10-P90: aprovado
- Se fora: alerta com possíveis causas e sugestões

---

## 4. Base de Preços Unitários

### Fontes de PU (ordem de prioridade)

1. **Cotações do projeto** — se o cliente já tem propostas de fornecedores (como o gás do Elizabeth, R$ 250k fechado)
2. **Base Cartesian** — PUs de projetos anteriores similares (Elizabeth, SOHO, Maison, etc.)
3. **SINAPI** — referência pública, atualizada mensalmente
4. **Índice paramétrico** — quando não tem PU específico, usa R$/m² do macrogrupo e distribui proporcionalmente

### Atualização monetária

```
PU Atual = PU Base × (CUB Atual / CUB Base)
```

---

## 5. Padrao de Rastreabilidade (Leo, 24/mar/2026)

### 5.1 Regra Fundamental

**Cada item do orcamento deve identificar de qual projeto e revisao veio o quantitativo e o preco unitario.** O leitor do memorial deve conseguir rastrear qualquer numero ate sua fonte sem precisar perguntar.

### 5.2 Sistema de Tags por Cor

Cada item recebe uma tag de fonte com cor correspondente:

| Cor | Tag | Significado | Exemplo |
|-----|-----|-------------|---------|
| **VERDE** | `Proj. [Projetista] [tipo] [rev]` | Extraido de arquivo de projeto do empreendimento | `Proj. Franzmann IFC rev.01` |
| **VERDE** | `[Cliente] [data]` | Confirmado pelo cliente/incorporador | `Thozen 05/03/26` |
| **VERDE** | `Contrato [Projetista]` | Valor de contrato de projetista | `Contrato DMA` |
| **AMARELO** | `Param. base Cartesian` | Mediana da base de 75 executivos | `Param. base Cartesian` |
| **AMARELO** | `PU base Cartesian` | Preco unitario da base de executivos | `PU base Cartesian` |
| **AMARELO** | `Briefing [Projetista]` | Dado do briefing do projetista | `Briefing Value` |
| **AMARELO** | `SINAPI` | Referencia SINAPI | `SINAPI` |
| **VERMELHO** | `Estimado (s/ projeto)` | Sem fonte confiavel | `Estimado (s/ projeto)` |

### 5.3 Mapeamento de Projetistas

Para cada projeto, mapear qual escritorio e responsavel por qual disciplina. Exemplo (Electra):

| Disciplina | Projetista | Tipo de arquivo |
|-----------|-----------|----------------|
| Arquitetonico | Battisti | IFC |
| Interiores | Favola | DWG |
| Estrutural | DMA + Zeplin + Liberte | IFC R26 |
| Eletrico, Hidro, Telecom, PPCI, Gas | Franzmann | IFC rev.01 + DXF rev.01 |
| Climatizacao | Value | DWG |
| Impermeabilizacao | W.Thomaz | Memorial |
| Esquadrias | WM | IFC (BIM) |
| Compatibilizacao BIM | Otus | - |

**Regra:** Este mapeamento e preenchido no inicio do projeto e usado em todas as entregas.

### 5.4 Confidencialidade

**NUNCA referenciar projetos de outros clientes pelo nome** em documentos de entrega. Usar "Param. base Cartesian" ou "projeto de referencia similar" em vez de citar nomes de obras. Regra valida para xlsx, docx, apresentacoes e qualquer material externo.

### 5.5 Estrutura do Memorial Word (por disciplina)

```markdown
### 4.X [Nome da Disciplina]

**Valor total:** R$ X.XXX.XXX
**R$/m2:** R$ XXX
**Projetista:** [Nome] | **Projeto rev:** [IFC/DXF rev.XX]
**Maturidade:** Verde XX% | Amarelo XX% | Vermelho XX%

#### Itens (tabela com rastreabilidade)

| Descricao | Qtd | Unid | PU (R$) | Total (R$) | Fonte |
|-----------|-----|------|---------|------------|-------|
| Trafo 500kVA | 1 | pc | 79.000 | 79.000 | Proj. Franzmann IFC rev.01 |
| Cabeamento tipo | 604 | trecho | 5,50 | 3.322 | Proj. Franzmann IFC rev.01 |
| Gerador 500kVA | 1 | vb | 340.000 | 340.000 | Estimado (s/ projeto) |
```

---

## 6. Consolidacao: Modelo C+A (Leo, 24/mar/2026)

### Producao incremental (Modelo C)

O Cartesiano gera **discipline packs** por disciplina. Leo valida cada pack antes de incorporar na planilha grande.

### Consolidacao automatica (Modelo A)

Quando a planilha grande esta validada, um **script de consolidacao** le o xlsx finalizado e gera o docx memorial automaticamente, com rastreabilidade per-item.

### Pipeline

```
1. Cartesiano gera discipline pack (xlsx disciplina + memorial.md + confianca)
2. Leo valida (revisa vermelho, confere amarelo, confia verde)
3. Leo incorpora na planilha grande (copy-paste)
4. Repete 1-3 para cada disciplina
5. Script consolidacao: le planilha grande → gera docx memorial rastreavel
```

**Script:** `~/orcamentos/scripts/gerar_memorial_rastreavel.py`

Entrada: planilha grande (.xlsx) + mapeamento de projetistas (JSON)
Saida: memorial .docx com rastreabilidade per-item (cores + tags + projetistas)

O script:
- Le todas as abas de disciplina
- Extrai cores das celulas (verde/amarelo/vermelho)
- Mapeia cores para tags especificas usando o mapeamento de projetistas
- Gera o docx com capa, EAP resumo, mapa de maturidade, e detalhamento per-item
- Sanitiza referencias a outros clientes automaticamente

---

## 7. Geracao do Memorial Word Final

Quando todas as disciplinas estiverem prontas:

1. **Rodar script de consolidacao** (`gerar_memorial_rastreavel.py`) sobre a planilha grande
2. O script gera automaticamente: capa, indicadores, mapa de maturidade, EAP, detalhamento por disciplina, PUs-chave, premissas
3. **Revisar** o docx gerado (conferir tags, premissas, formatacao)
4. **Anexar** lista completa de projetos usados (arquivo, revisao, projetista, data)

---

## 8. Ordem Sugerida de Disciplinas

Baseado no impacto no custo total e na disponibilidade de dados:

| Prioridade | Disciplina | % do Total | Dados Disponíveis |
|------------|-----------|------------|-------------------|
| 1 | Supraestrutura | ~19% | IFC + DWG |
| 2 | Fachada | ~10% | DWG |
| 3 | Esquadrias | ~10% | DWG |
| 4 | Acabamentos pisos | ~7% | DWG |
| 5 | Instalações Elétricas | ~3% | IFC + DWG |
| 6 | Hidrossanitário | ~3% | IFC + DWG |
| 7 | PCI (Civil + Elétrico) | ~2% | IFC + DWG |
| 8 | Alvenaria | ~5% | DWG |
| 9 | Climatização | ~1% | DWG |
| 10 | Demais | ~10% | Variado |

*Gerenciamento, custos indiretos e imprevistos são preenchidos por índice/decisão, não por extração.*

---

## 9. Limitacoes e Riscos

### IFC2X3 vs IFC4
Os IFCs do Electra são schema IFC2X3 — contêm geometria 3D mas frequentemente faltam propriedades técnicas (diâmetros, bitolas, potências). IFC4 é mais rico. Para projetos futuros, pedir IFC4 quando possível.

### DWG como fonte complementar
DWGs contêm informações nas pranchas (tabelas, textos, cotas) que não estão no IFC. O processamento é semi-automatizado (conversão DXF + parsing). Algumas informações precisam de leitura visual.

### Preços unitários
Sem uma base de PUs atualizada e centralizada, o Cartesiano vai usar referências de projetos anteriores ou SINAPI. Idealmente, montar uma base de PUs Cartesian que se atualiza a cada projeto.

### Planilha grande (55MB)
O Cartesiano não edita a planilha grande diretamente. A consolidação é manual (copy-paste). Isso é intencional — preserva fórmulas, formatação e macros.

---

## 10. Infraestrutura Necessaria

### Ja existe
- [x] ifcopenshell (extracao IFC)
- [x] ezdxf (extracao DXF)
- [x] ODA File Converter (DWG → DXF)
- [x] openpyxl (geracao de planilhas)
- [x] python-docx (geracao de Word)
- [x] Base parametrica (75 projetos calibrados)
- [x] Scripts de extracao por disciplina
- [x] Briefings R00 de todas as 14 disciplinas
- [x] Base de PUs Cartesian (1.504 itens, 75 executivos)
- [x] Script de consolidacao xlsx→docx (`gerar_memorial_rastreavel.py`) — validado no Electra R02

### A criar
- [ ] Template padronizado de planilha por disciplina
- [ ] Template de memorial por disciplina (.md)
- [ ] Template de relatorio de confianca
- [ ] Mapeamento de projetistas JSON por projeto (template)

---

## 11. Exemplo Pratico — Ciclo Completo (Eletrico)

```
1. Leo: "Vamos fazer elétrico"

2. Cartesiano verifica:
   - 9 IFCs (246MB) + 18 DWGs (27MB) disponíveis
   - Briefing eletrico-r00.md existe (336 linhas)
   - Limitação: IFCs sem propriedades elétricas

3. Cartesiano processa:
   - IFC → 837 luminárias, 18.967 eletrodutos, 1.014 cabos
   - DWG → converte e extrai tabelas de quadros, bitolas, tomadas
   - Cruza IFC × DWG → consolida quantitativos

4. Cartesiano gera pack:
   - eletrico-r01.xlsx (planilha com ~850 linhas)
   - eletrico-r01-memorial.md (5 páginas)
   - eletrico-r01-confianca.md (1 página)

5. Leo valida:
   - 🔴 Automação (3 itens) → decide escopo
   - 🟡 Cabeamento tipo (12 itens) → confirma multiplicação 24x
   - 🟢 Subestação (45 itens) → OK, fonte direta

6. Leo consolida:
   - Cola na planilha grande, aba ELÉTRICO
   - EAP atualiza automaticamente (fórmulas)
   - Memorial acumula
```

---

*Este documento é a referência do processo. Atualizar conforme o fluxo for refinado com o projeto piloto (Electra).*
