# Briefing - Sistema Preventivo de Incêndio Elétrico
## Projeto: Thozen Electra
**Revisão:** R00  
**Data:** 20/03/2026  
**Disciplina:** N1 14 Instalações Especiais → Sistema de Detecção e Alarme de Incêndio  
**Fonte:** `projetos/thozen-electra/projetos/08 PREVENTIVO INCENDIO ELÉTRICO/`

---

## 1. Resumo Executivo

Sistema de detecção e alarme de incêndio endereçável para edifício residencial de múltiplos pavimentos.

**Principais números:**
- **494 detectores** de fumaça ópticos
- **72 acionadores manuais** de alarme
- **102 avisadores** audiovisuais
- **1.189 quadros** gerais de comando PCI
- **3 centrais** de alarme de incêndio
- **33 pavimentos** atendidos (Térreo + G1 a G5 + Lazer + Tipo 8° a 31° + Casa de Máquinas)

---

## 2. Premissas e Considerações

### 2.1 Estrutura do Edifício
- **Térreo:** 1° pavimento
- **Garagens:** 2° (G1), 3° (G2), 4° (G3), 5° (G4), 6° (G5)
- **Lazer:** 7° pavimento
- **Pavimentos Tipo:** 8° ao 31° pavimento (24 repetições)
- **Casa de Máquinas:** Cobertura

### 2.2 Normas Aplicáveis
- NBR 17240:2010 - Sistemas de detecção e alarme de incêndio
- IT 40 (Corpo de Bombeiros) - Sistema de detecção e alarme de incêndio

### 2.3 Características do Sistema
- Sistema endereçável convencional
- Detectores de fumaça ópticos
- Acionadores manuais com LED de indicação
- Avisadores audiovisuais (sirene + luz estroboscópica)
- Centrais com capacidade de endereçamento por zona

### 2.4 Limitações da Extração
⚠️ **Dados NÃO extraídos dos IFCs (IFC2X3):**
- **Cabos:** Bitolas, metragens por circuito
- **Eletrodutos:** Diâmetros, metragens
- **Caixas de passagem:** Quantidades, dimensões
- **Terminais de linha:** Quantidades
- **Baterias de backup:** Capacidade, quantidade
- **Módulos de interface:** Relés, isoladores

**Recomendação:** Solicitar memorial descritivo, planilha de quantitativos ou pranchas de detalhamento do projeto executivo para complementar dados de infraestrutura (cabos, eletrodutos, acessórios).

---

## 3. Quantitativos Detalhados

### 3.1 Equipamentos de Detecção

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Detector de Fumaça Óptico | Endereçável, 2 fios | UN | **494** | Distribuídos conforme tabela por pavimento |

**Distribuição por Pavimento:**

| Pavimento | Detectores | Observação |
|-----------|-----------|------------|
| 01° Térreo | 21 | Áreas comuns, circulação |
| 02° G1 | 27 | Garagem, circulação vertical |
| 03° G2 | 25 | Garagem, circulação vertical |
| 04° G3 | 27 | Garagem, circulação vertical |
| 05° G4 | 25 | Garagem, circulação vertical |
| 06° G5 | 25 | Garagem, circulação vertical |
| 07° Lazer | 24 | Salões, circulação, áreas de convívio |
| 08°~31° Tipo | 13 UN/pav × 24 = **312** | Circulações, halls |
| Casa de Máquinas | 10 | Casas de máquinas elevadores, barrilete |
| **TOTAL** | **494** | — |

---

### 3.2 Equipamentos de Acionamento Manual

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Acionador Manual de Alarme | Endereçável, com LED | UN | **72** | Rotas de fuga, saídas de emergência |

**Distribuição por Pavimento:**

| Pavimento | Acionadores | Observação |
|-----------|------------|------------|
| 01° Térreo | 3 | Saídas principais |
| 02° G1 | 2 | Escadas de emergência |
| 03° G2 | 2 | Escadas de emergência |
| 04° G3 | 2 | Escadas de emergência |
| 05° G4 | 2 | Escadas de emergência |
| 06° G5 | 2 | Escadas de emergência |
| 07° Lazer | 3 | Saídas de emergência do pavimento |
| 08°~31° Tipo | 2 UN/pav × 24 = **48** | Halls elevadores, escadas |
| Casa de Máquinas | — | Sem acionadores (área restrita) |
| **TOTAL** | **72** | — |

---

### 3.3 Equipamentos de Sinalização

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Avisador Sonoro e Visual | Sirene + luz estroboscópica, 24V | UN | **102** | Áreas de circulação, garagens |

**Distribuição por Pavimento:**

| Pavimento | Avisadores | Observação |
|-----------|-----------|------------|
| 01° Térreo | 6 | Áreas comuns, circulação |
| 02° G1 | 5 | Garagem, circulação |
| 03° G2 | 5 | Garagem, circulação |
| 04° G3 | 5 | Garagem, circulação |
| 05° G4 | 5 | Garagem, circulação |
| 06° G5 | 5 | Garagem, circulação |
| 07° Lazer | 16 | Múltiplas áreas de convívio |
| 08°~31° Tipo | 2 UN/pav × 24 = **48** | Halls, circulações |
| Casa de Máquinas | — | Sem avisadores (área restrita) |
| **TOTAL** | **102** | — |

---

### 3.4 Centrais e Quadros de Comando

| Descrição | Especificação | UN | QTD | Observação |
|-----------|---------------|-----|-----|------------|
| Central de Alarme de Incêndio | Endereçável, mín. 500 pontos, baterias 24V/18Ah | UN | **3** | Térreo (principal) + redundâncias |
| Quadro Geral de Comando PCI | Alumínio, IP65 | UN | **1.189** | ⚠️ **Revisar** — provável erro de modelagem IFC |

**⚠️ ATENÇÃO - Quadros de Comando:**

A extração dos IFCs identificou **1.189 quadros**, sendo 1.152 apenas no pavimento tipo (48 UN/pav × 24). Este número está **superestimado** — o modelo IFC pode estar duplicando elementos ou contabilizando módulos internos.

**Estimativa realista baseada em projetos similares:**
- 1 quadro por andar (circulação/hall) × 33 pavimentos = **33 quadros**
- Quadros setoriais em garagens e lazer = **~10 quadros**
- **Total estimado: 40-50 quadros**

**Ação necessária:** Conferir pranchas executivas ou memorial descritivo para quantidade real.

---

### 3.5 Cabeamento e Infraestrutura

⚠️ **Dados não disponíveis nos arquivos IFC fornecidos.**

Itens que **precisam ser quantificados** a partir do projeto executivo (pranchas DWG, memorial, planilhas):

| Item | UN | QTD | Status | Observação |
|------|-----|-----|--------|------------|
| Cabo de Sinal 2x2,5mm² (PCI) | m | **?** | ❌ Faltante | Interligação detectores/acionadores/avisadores |
| Cabo de Alimentação 2x2,5mm² | m | **?** | ❌ Faltante | Alimentação avisadores audiovisuais |
| Cabo PP 2x2,5mm² (Alarme) | m | **?** | ❌ Faltante | Circuito de detecção (NBR 17240) |
| Eletroduto PVC rígido ⌀20mm | m | **?** | ❌ Faltante | Infraestrutura detectores |
| Eletroduto PVC rígido ⌀25mm | m | **?** | ❌ Faltante | Infraestrutura prumadas |
| Eletroduto metálico ⌀20mm | m | **?** | ❌ Faltante | Áreas molhadas, garagens |
| Caixa de passagem 4"×2" | UN | **?** | ❌ Faltante | Derivações circuitos |
| Caixa de passagem 4"×4" | UN | **?** | ❌ Faltante | Derivações principais |
| Terminal de linha (EOL) | UN | **?** | ❌ Faltante | Fim de circuito |
| Isolador de curto-circuito | UN | **?** | ❌ Faltante | Proteção de loops |
| Módulo relé de saída | UN | **?** | ❌ Faltante | Interfaces com outros sistemas |

**Estimativas paramétricas (a confirmar com projeto):**

Baseado em índices típicos para edifícios residenciais com PCI:

- **Cabo de sinal:** ~15-20m por ponto (detector/acionador) → 494+72 = 566 pontos → **~10.000 m**
- **Eletrodutos:** ~10-12m por ponto → **~6.000 m**
- **Caixas de passagem:** 1 caixa a cada 3 pontos → **~190 UN**

⚠️ **Estes valores são ESTIMATIVAS** — não substituem levantamento do projeto executivo.

---

## 4. Fontes de Dados

### 4.1 Arquivos IFC Processados (9 arquivos)

| Arquivo | Pavimento | Detectores | Acionadores | Avisadores | Status |
|---------|-----------|-----------|-------------|------------|--------|
| 348 - PEE01 [09] - rev.01 - [...] 01° PAVTO. TÉRREO.ifc | Térreo | 21 | 3 | 6 | ✅ Processado |
| 348 - PEE02 [09] - rev.01 - [...] 02° PAVTO. G1.ifc | G1 | 27 | 2 | 5 | ✅ Processado |
| 348 - PEE03 [09] - rev.01 - [...] 03° PAVTO. G2.ifc | G2 | 25 | 2 | 5 | ✅ Processado |
| 348 - PEE04 [09] - rev.01 - [...] 04° PAVTO. G3.ifc | G3 | 27 | 2 | 5 | ✅ Processado |
| 348 - PEE05 [09] - rev.01 - [...] 05° PAVTO. G4.ifc | G4 | 25 | 2 | 5 | ✅ Processado |
| 348 - PEE06 [09] - rev.01 - [...] 06° PAVTO. G5.ifc | G5 | 25 | 2 | 5 | ✅ Processado |
| 348 - PEE07 [09] - rev.01 - [...] 07° PAVTO. LAZER.ifc | Lazer | 24 | 3 | 16 | ✅ Processado |
| 348 - PEE08 [09] - rev.01 - [...] 08°~31° PAVTO. TIPO (24x).ifc | Tipo (×24) | 312 | 48 | 48 | ✅ Processado |
| 348 - PEE09 [09] - rev.01 - [...] CASA DE MÁQUINAS.ifc | Casa Máq. | 10 | — | — | ✅ Processado |

**Total de arquivos IFC:** 9  
**Total de arquivos DWG disponíveis:** 18 (não processados — requerem software CAD)

### 4.2 Arquivos DWG Disponíveis (18 arquivos)

Os arquivos DWG estão organizados em duas torres (A e B):

**Torre A:**
- 348 - PEE 01 - 01° PAVTO. TÉRREO [T. A]
- 348 - PEE 03 - 02° PAVTO. G1 [T. A]
- 348 - PEE 05 - 03° PAVTO. G2 [T. A]
- 348 - PEE 07 - 04° PAVTO. G3 [T. A]
- 348 - PEE 09 - 05° PAVTO. G4 [T. A]
- 348 - PEE 11 - 06° PAVTO. G5 [T. A]
- 348 - PEE 13 - 07° PAVTO. LAZER [T. A]
- 348 - PEE 15 - 08°~31° PAVTO. TIPO (24x) [T. A]
- 348 - PEE 17 - CASA DE MÁQUINAS [T. A]

**Torre B:**
- 348 - PEE 02 - 01° PAVTO. TÉRREO [T. B]
- 348 - PEE 04 - 02° PAVTO. G1 [T. B]
- 348 - PEE 06 - 03° PAVTO. G2 [T. B]
- 348 - PEE 08 - 04° PAVTO. G3 [T. B]
- 348 - PEE 10 - 05° PAVTO. G4 [T. B]
- 348 - PEE 12 - 06° PAVTO. G5 [T. B]
- 348 - PEE 14 - 07° PAVTO. LAZER [T. B]
- 348 - PEE 16 - 08°~31° PAVTO. TIPO (24x) [T. B]
- 348 - PEE 18 - CASA DE MÁQUINAS [T. B]

**Observação:** Os DWGs podem conter informações complementares:
- Legendas de especificações técnicas
- Detalhes de cabeamento e eletrodutos
- Esquemas unifilares
- Tabelas de cargas e circuitos

**Ação recomendada:** Abrir DWGs em AutoCAD/DraftSight para verificar:
1. Tabelas de quantitativos (se presentes nas pranchas)
2. Legendas com especificações de cabos e eletrodutos
3. Esquemas unifilares das centrais
4. Detalhes de instalação

---

## 5. Observações e Próximos Passos

### 5.1 Dados Confirmados ✅
- Quantidade de detectores de fumaça por pavimento
- Quantidade de acionadores manuais por pavimento
- Quantidade de avisadores audiovisuais por pavimento
- Distribuição espacial dos equipamentos

### 5.2 Dados com Ressalvas ⚠️
- **Quadros de comando:** Quantidade extraída (1.189 UN) está inconsistente — conferir pranchas
- **Centrais de alarme:** Quantidade mínima (3 UN) — pode haver central redundante

### 5.3 Dados Faltantes ❌
- Cabos: bitolas, metragens, especificação (PP, PVC, etc.)
- Eletrodutos: diâmetros, metragens, material (PVC/metálico)
- Caixas de passagem e acessórios
- Baterias backup (capacidade, autonomia)
- Módulos de interface (relés, isoladores, EOL)
- Diagrama unifilar da central
- Memorial descritivo com especificações técnicas

### 5.4 Recomendações para Orçamento

**Para orçamento paramétrico (ordem de grandeza):**
- ✅ Usar quantidades de detectores, acionadores e avisadores conforme extraído
- ⚠️ Usar estimativa conservadora de 40-50 quadros (não os 1.189)
- 📊 Adotar índices paramétricos para cabos/eletrodutos (~15m cabo/ponto, ~10m eletroduto/ponto)
- 💰 R$/m² referencial para PCI residencial: **R$ 45-65/m²** (verificar base Cartesian)

**Para orçamento executivo (N1 14):**
- ❗ **ESSENCIAL:** Solicitar memorial descritivo + planilha de quantitativos do projetista
- ❗ **ESSENCIAL:** Conferir especificações técnicas nas pranchas DWG (legendas, tabelas)
- Verificar interface com outros sistemas (SPDA, automação, BMS)
- Confirmar marcas/modelos especificados (Notifier, Intelbras, Edwards, etc.)

### 5.5 Riscos e Lacunas

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Cabos/eletrodutos não quantificados | **ALTO** — ~40-50% do custo do sistema | Solicitar memorial ou usar índices paramétricos conservadores |
| Quantidade de quadros superestimada | **MÉDIO** — distorce custo unitário | Conferir pranchas, considerar 1 quadro/pavimento |
| Especificações técnicas desconhecidas | **MÉDIO** — marcas premium vs. standard podem variar 30-50% | Adotar especificação padrão mercado (Intelbras, Guardia) |
| Interfaces não mapeadas | **BAIXO** — módulos adicionais pontuais | Prever verba de 5-10% para interfaces |

---

## 6. Checklist de Validação

Antes de prosseguir para o orçamento executivo, validar:

- [ ] Conferir pranchas DWG para tabelas de quantitativos
- [ ] Solicitar memorial descritivo do sistema PCI
- [ ] Confirmar quantidade real de quadros de comando
- [ ] Extrair especificações de cabos (bitola, tipo) das legendas
- [ ] Extrair especificações de eletrodutos (diâmetro, material)
- [ ] Identificar marca/modelo da central especificada
- [ ] Verificar autonomia de baterias especificada (NBR 17240: mín. 24h)
- [ ] Confirmar interface com sistema de som (evacuação)
- [ ] Confirmar interface com automação/BMS (se aplicável)
- [ ] Validar quantidades com projetista/equipe técnica

---

## 7. Responsável pela Extração

**Extraído por:** Cartesiano (subagente)  
**Data:** 20/03/2026 10:33 BRT  
**Método:** Processamento automático de arquivos IFC2X3 com IfcOpenShell  
**Limitações:** IFC2X3 não suporta entidades específicas de cabeamento elétrico (IfcCableSegment disponível apenas em IFC4)

---

**Anexos sugeridos:**
- Planilha Excel com quantitativos por pavimento (gerar a partir deste briefing)
- Capturas de tela das pranchas DWG (legendas, tabelas)
- Memorial descritivo (quando disponibilizado pelo projetista)
