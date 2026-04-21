# Briefing Técnico - Sistema de Exaustão (Churrasqueiras)
## Thozen Electra | Rev. R00

---

## ⚠️ LIMITAÇÃO DA EXTRAÇÃO

**Fonte disponível:** RA_CHU_EXE_PROJETO_R00.dwg (3.2 MB)  
**Status:** Arquivo DWG não conversível para formato legível (DXF/IFC)

**Métodos tentados:**
1. Extração de strings ASCII → Dados binários codificados
2. Análise heurística de padrões → Sem especificações técnicas legíveis
3. Busca de palavras-chave → Fragmentos sem contexto

**Resultado:** Os quantitativos abaixo são baseados em **premissas técnicas padrão** para edifícios residenciais de alto padrão similares ao Thozen Electra. **TODOS os valores precisam ser validados com base no DWG** após conversão para formato legível ou revisão manual.

**Ferramentas necessárias para extração completa:**
- Conversor DWG→DXF (ODA File Converter, AutoCAD, DraftSight)
- Ou acesso ao projeto em software CAD (AutoCAD, BricsCAD)
- Ou PDF plotado do projeto executivo

---

## 1. Resumo Executivo

### 1.1 Escopo
Sistema de exaustão mecânica para churrasqueiras localizadas no **pavimento Lazer (7º pavimento)** do edifício residencial Thozen Electra.

**Função:** Extração de fumaça, vapores e odores gerados pelas churrasqueiras de uso comum dos moradores.

**Normas aplicáveis:**
- NBR 14518 - Sistemas de ventilação para cozinhas profissionais
- NBR 16401-1 - Instalações de ar-condicionado - Parte 1: Projetos
- IT 46 - CBPMESP - Proteção contra incêndio para líquidos e gases combustíveis e inflamáveis (se aplicável)
- Código Sanitário Municipal de São Paulo (CSMSP)

---

### 1.2 Configuração Estimada do Sistema

⚠️ **PREMISSAS (A CONFIRMAR COM DWG):**

| Item | Quantidade Estimada | Unidade | Observação |
|------|---------------------|---------|------------|
| Churrasqueiras atendidas | 2-4 | UN | Típico para edifício de 24 pavtos tipo |
| Exaustores centrífugos | 1-2 | UN | Pode ser 1 exaustor para todas ou 1 por churrasqueira |
| Coifas de captação | 2-4 | UN | 1 por churrasqueira |
| Dutos de exaustão (vertical) | 50-80 | m | Do lazer até cobertura/casa de máquinas |
| Grelhas de ventilação | 4-8 | UN | Admissão de ar de compensação |

---

## 2. Premissas de Projeto

### 2.1 Localização
- **Pavimento:** Lazer (7º pavimento)
- **Ambiente:** Área de churrasqueiras (provavelmente aberta/semi-aberta)
- **Descarga:** Cobertura ou Casa de Máquinas (acima do 31º pavimento)

### 2.2 Dimensionamento (Típico NBR 14518)

**Vazão de exaustão por churrasqueira:**
- Churrasqueira pequena (até 1,0 m²): 1.000-1.500 m³/h
- Churrasqueira média (1,0-2,0 m²): 1.500-2.500 m³/h
- Churrasqueira grande (> 2,0 m²): 2.500-4.000 m³/h

**Velocidade de captação na coifa:**
- Mínimo: 0,25 m/s (NBR 14518)
- Recomendado: 0,30-0,50 m/s

**Velocidade nos dutos:**
- Duto principal: 8-12 m/s
- Trecho final (descarga): 10-15 m/s

### 2.3 Materiais Típicos

**Dutos:**
- Chapa de aço galvanizado #24 (0,6 mm) ou #22 (0,75 mm)
- Alternativa: Aço inox AISI 304 (ambientes agressivos)
- Isolamento térmico: Lã de vidro 25 mm (se duto passar por área climatizada)

**Coifas:**
- Aço inox AISI 304, acabamento escovado
- Filtros tipo labirinto (alumínio ou inox)
- Iluminação LED integrada

---

## 3. Quantitativos Detalhados

### 3.1 Equipamentos Principais

⚠️ **TODOS OS VALORES A CONFIRMAR COM DWG**

#### 3.1.1 Exaustores Centrífugos

**Cenário 1: Sistema centralizado (1 exaustor para todas as churrasqueiras)**

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Exaustor centrífugo de média pressão | Vazão: 8.000-12.000 m³/h<br>Pressão estática: 40-60 mmCA<br>Motor: 5-7,5 CV (trifásico 220/380V)<br>Rotação: 1750 rpm<br>Material: rotor em aço carbono com pintura epóxi<br>Nível de ruído: < 75 dB(A) a 1,5m | UN | 1 | ⚠️ Confirmar vazão total e perda de carga |

**Cenário 2: Sistema individualizado (1 exaustor por churrasqueira)**

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Exaustor centrífugo de baixa/média pressão | Vazão: 2.000-3.000 m³/h<br>Pressão estática: 25-35 mmCA<br>Motor: 1,5-2,0 CV (trifásico 220/380V)<br>Rotação: 1750 rpm<br>Material: rotor em aço carbono com pintura epóxi<br>Nível de ruído: < 70 dB(A) a 1,5m | UN | 2-4 | ⚠️ Confirmar quantidade de churrasqueiras |

---

#### 3.1.2 Coifas de Captação

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Coifa de parede em aço inox AISI 304 | Dimensões típicas: 1,20 x 0,80 m (LxP)<br>Altura: 0,50-0,60 m<br>Filtros: tipo labirinto (alumínio), removíveis<br>Iluminação: LED 2x10W, 6500K<br>Acabamento: escovado | UN | 2-4 | ⚠️ Confirmar dimensões e quantidade |

---

### 3.2 Dutos e Acessórios

⚠️ **Metragens estimadas — DEPENDEM DO LAYOUT E ROTEAMENTO**

#### 3.2.1 Dutos Retos

**Premissa:** Duto vertical do 7º pav. (Lazer) até cobertura/casa de máquinas = ~25-30 pavimentos × 2,80m = **70-84m de altura**

**Premissa:** Trecho horizontal no lazer (da churrasqueira até prumada) = **5-15m por churrasqueira**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Duto retangular 400x300mm, chapa #24 galv. | Seção nominal conforme cálculo de perda de carga | m | 20-40 | ⚠️ Trechos horizontais no lazer |
| Duto retangular 500x400mm, chapa #24 galv. | Seção nominal (trecho de interligação/principal) | m | 10-20 | ⚠️ Se houver trecho comum |
| Duto circular Ø300mm, chapa #24 galv. | Duto vertical (prumada) | m | 70-90 | ⚠️ Do lazer até descarga na cobertura |
| Duto circular Ø400mm, chapa #24 galv. | Duto vertical (se sistema centralizado) | m | 70-90 | ⚠️ Alternativa para maior vazão |

---

#### 3.2.2 Conexões e Acessórios

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Curva 90° (raio longo), chapa #24 galv. | Conforme diâmetro/seção do duto | UN | 8-16 | ⚠️ Mudanças de direção |
| Joelho 90°, chapa #24 galv. | Conforme diâmetro/seção do duto | UN | 4-8 | ⚠️ Conexões |
| Transição retangular-circular | Da saída da coifa (retangular) para duto vertical (circular) | UN | 2-4 | 1 por churrasqueira |
| Damper corta-fogo 90 min, Ø300mm | Instalado na passagem entre pavimentos | UN | 2-4 | ⚠️ Se exigido por PCI |
| Registro de gaveta (damper manual) | Ø300mm, chapa #18 galv. | UN | 2-4 | 1 por ramal (isolamento/manutenção) |
| Chapéu de exaustão (tipo chinês) | Ø300-400mm, alumínio ou galv., tela contra insetos | UN | 1-2 | Descarga na cobertura |

---

#### 3.2.3 Suportes e Fixações

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Suporte tipo mão-francesa | Para dutos verticais, a cada 3,0m | UN | 25-30 | ⚠️ Conforme altura da prumada |
| Abraçadeira metálica | Ø300-400mm, com borracha anti-vibração | UN | 30-40 | Fixação de dutos circulares |
| Perfil "U" galv. para fixação de dutos retang. | 40x40x3mm | m | 40-60 | Suporte de trechos horizontais |
| Tirante roscado M10 com porcas e arruelas | Para suspensão de dutos horizontais | UN | 50-80 | Espaçamento 1,5-2,0m |

---

### 3.3 Grelhas e Ventilação de Compensação

**Premissa:** Para cada m³/h de ar exaurido, é necessário admitir aproximadamente o mesmo volume de ar externo (ventilação de compensação).

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Grelha de ventilação em alumínio anodizado | Dimensões: 600x300mm<br>Área livre: ~0,14 m²<br>Aletas fixas 45° | UN | 4-8 | ⚠️ Admissão de ar no ambiente das churrasqueiras |
| Tela mosquiteiro em alumínio | Para proteção das grelhas | m² | 2-4 | ⚠️ Conforme área total de grelhas |

---

### 3.4 Instalação Elétrica Associada

⚠️ **PREMISSAS — CONFIRMAR COM PROJETO ELÉTRICO (DISCIPLINA 09)**

#### 3.4.1 Alimentação dos Exaustores

**Cenário 1: 1 exaustor de 5-7,5 CV**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Cabo unipolar 6mm² (3F+N+T), 750V, anti-chama | Do quadro até exaustor | m | 80-100 | ⚠️ Prumada + trecho horizontal |
| Disjuntor tripolar 25-32A, curva D | Proteção no quadro de comando | UN | 1 | Conforme corrente nominal do motor |
| Contator tripolar 25A, bobina 220V | Acionamento do motor | UN | 1 | |
| Relé térmico 10-16A (ajustável) | Proteção contra sobrecarga | UN | 1 | |
| Botoeira liga/desliga, caixa estanque IP65 | Comando local | UN | 1 | |

**Cenário 2: 2-4 exaustores de 1,5-2,0 CV cada**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Cabo unipolar 4mm² (3F+N+T), 750V, anti-chama | Do quadro até cada exaustor | m | 160-200 | ⚠️ 80-100m × 2 ou 4 exaustores |
| Disjuntor tripolar 16-20A, curva D | Proteção no quadro de comando | UN | 2-4 | 1 por exaustor |
| Contator tripolar 16A, bobina 220V | Acionamento do motor | UN | 2-4 | 1 por exaustor |
| Relé térmico 5-8A (ajustável) | Proteção contra sobrecarga | UN | 2-4 | 1 por exaustor |
| Botoeira liga/desliga, caixa estanque IP65 | Comando local | UN | 2-4 | 1 por churrasqueira |

---

#### 3.4.2 Quadro de Comando (se dedicado)

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Quadro metálico 600x800x250mm, IP55 | Com barramento, disjuntor geral, espaço para contatores | UN | 1 | ⚠️ Pode ser integrado ao QD do lazer |
| Disjuntor geral tripolar 63A, curva D | Proteção geral do quadro | UN | 1 | Se quadro dedicado |
| Cabo alimentador 16mm² (3F+N+T), 750V | Do QD principal do lazer até quadro de exaustão | m | 20-40 | ⚠️ Conforme distância |

---

#### 3.4.3 Iluminação das Coifas

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Luminária LED 10W, 6500K, integrada à coifa | 220V, IP54 | UN | 4-8 | 2 por coifa (típico) |
| Cabo PP 2x1,5mm² | Alimentação das luminárias | m | 10-20 | ⚠️ Do quadro até coifas |
| Interruptor simples, caixa 4x2" | Comando local das luzes | UN | 2-4 | 1 por churrasqueira |

---

### 3.5 Controles e Automação (Se Houver)

⚠️ **PREMISSA: Sistema pode ter controle manual simples OU automação**

#### Controle Manual (Básico)
- Botoeiras liga/desliga nos pontos de uso
- Sinalização visual (LED verde = ligado, vermelho = desligado)

#### Controle Automatizado (Opcional)
| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Sensor de temperatura | Range: 0-100°C, saída 4-20mA | UN | 2-4 | 1 por coifa |
| Sensor de fumaça (não PCI) | Óptico, 24Vdc | UN | 2-4 | 1 por churrasqueira |
| Controlador lógico (CLP ou relé programável) | 8-16 I/O, 220V | UN | 1 | Lógica de acionamento |
| IHM (interface homem-máquina) | Tela 7", touch, IP65 | UN | 1 | Comando centralizado (opcional) |

---

## 4. Fontes de Dados

### 4.1 Arquivos Processados
- **RA_CHU_EXE_PROJETO_R00.dwg** (3.2 MB)
  - Localização original: `projetos/thozen-electra/projetos/13 CHURRASQUEIRA EXAUSTAO/DWG/`
  - Cópia para análise: `executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.dwg`
  - Status: ❌ Não foi possível extrair dados técnicos (arquivo binário codificado)

### 4.2 Arquivos de Referência (Consultados)
- **PROJETO.md** - Dados gerais do Thozen Electra
  - Pavimentos: 32 (6 garagens + lazer + 24 tipos + térreo + casa de máquinas)
  - Lazer: 7º pavimento

- **RA_ARQ_EXE_07_LAZER_R02.dwg** (arquitetura do lazer)
  - Localização: `projetos/thozen-electra/projetos/02 ARQUITETURA/DWG/`
  - Status: ❌ Não processado (aguardando conversão DWG→DXF)

### 4.3 Normas e Referências Técnicas
- NBR 14518:2000 - Sistemas de ventilação para cozinhas profissionais
- NBR 16401-1:2008 - Instalações de ar-condicionado - Sistemas centrais e unitários
- Catálogos de fabricantes:
  - Cia Paulista de Ventilação (exaustores)
  - Otam (coifas inox)
  - Metalflex (dutos e conexões)

---

## 5. Observações e Pendências

### 5.1 Dados Faltantes (CRÍTICOS)

⚠️ **Não foi possível extrair do DWG:**

1. **Quantidade exata de churrasqueiras** → Estimado: 2-4 UN (típico para edifício de 24 pavtos)
2. **Dimensões das churrasqueiras** → Necessário para dimensionar coifas e vazão
3. **Layout das churrasqueiras no pavimento lazer** → Impacta metragem de dutos horizontais
4. **Vazão de projeto de cada exaustor** → Parâmetro crítico para seleção de equipamentos
5. **Diâmetros especificados dos dutos** → Estimado com base em vazões típicas (DN 300-400)
6. **Potência dos motores** → Estimado: 1,5-7,5 CV (conforme cenário)
7. **Roteamento vertical da prumada** → Impacta metragem total e interferências
8. **Ponto de descarga na cobertura** → Necessário para especificar chapéu de exaustão
9. **Tipo de controle** (manual/automático) → Impacta custos e especificações
10. **Integração com BMS/automação predial** → Se houver, impacta protocolos e interfaces

---

### 5.2 Interferências e Compatibilizações

⚠️ **Verificar com outras disciplinas:**

1. **Estrutura (01):**
   - Passagem da prumada vertical pelos pavimentos
   - Furos em lajes (tipicamente Ø400-500mm para duto Ø300-400mm)
   - Reforços estruturais se necessário

2. **Arquitetura (02):**
   - Localização exata das churrasqueiras no lazer
   - Alturas de pé-direito (impacta dimensionamento de coifas)
   - Acabamentos (coifa aparente ou embutida?)
   - Grelhas de ventilação: localização, tamanho, acabamento

3. **Elétrico (09):**
   - Alimentação dos exaustores (quadro de origem, circuitos, proteções)
   - Cabos e eletrodutos já considerados no projeto elétrico?
   - Ponto de força para comando/automação

4. **PCI Civil (07):**
   - Dampers corta-fogo na prumada vertical?
   - Proteção passiva de dutos (se atravessar compartimentos)
   - Integração com sistema de detecção/alarme

5. **Hidráulico (05):**
   - Ponto de água para limpeza de coifas/filtros
   - Drenagem de condensado (se houver)

6. **Ar-condicionado (14):**
   - Integração da ventilação de compensação com sistema de climatização do lazer
   - Evitar sobrepressão/subpressão no ambiente

---

### 5.3 Recomendações para Próximas Etapas

**Etapa 1: Extração completa de dados do DWG**
- [ ] Converter DWG para DXF usando ODA File Converter (free) ou AutoCAD
- [ ] Ou gerar PDF plotado com especificações visíveis
- [ ] Ou abrir em software CAD e extrair:
  - Quantidade e dimensões das churrasqueiras
  - Vazão especificada de cada exaustor
  - Diâmetros dos dutos
  - Potências dos motores
  - Metragens exatas de dutos (horizontal + vertical)
  - Quantidade de curvas, joelhos, dampers
  - Detalhes de fixação e suporte

**Etapa 2: Compatibilização com disciplinas complementares**
- [ ] Cruzar com projeto elétrico (09) → confirmar alimentação, quadros, cabos
- [ ] Cruzar com arquitetura (02) → layout exato, interferências, acabamentos
- [ ] Cruzar com estrutura (01) → passagens, furos, reforços

**Etapa 3: Validação de premissas**
- [ ] Confirmar com equipe de projetos:
  - Sistema centralizado (1 exaustor) OU individualizado (1 por churrasqueira)?
  - Tipo de controle (manual/automático)?
  - Integração com BMS?
- [ ] Confirmar normas aplicáveis (CSMSP, CBPMESP, condomínio)

**Etapa 4: Geração de planilha executiva**
- [ ] Após validação dos quantitativos, gerar planilha Excel com:
  - Código Memorial (N1 14.08 - Exaustão)
  - Descrição detalhada
  - Especificação completa
  - UN | QTD | Preço Unit. | Total
  - Observações e premissas

---

## 6. Estimativa Preliminar de Custos

⚠️ **Valores NÃO considerados nesta versão** — aguardando quantitativos reais do DWG.

**Após extração dos dados, a planilha de custos incluirá:**
- Equipamentos (exaustores, coifas)
- Dutos e conexões (por metragem e tipo)
- Suportes e fixações
- Instalação elétrica associada
- Controles e automação (se houver)
- Mão de obra de instalação
- Comissionamento e balanceamento

---

## Histórico de Revisões

| Rev | Data | Autor | Descrição |
|-----|------|-------|-----------|
| R00 | 2026-03-20 | Cartesiano (bot) | Briefing inicial com premissas técnicas. ⚠️ Quantitativos NÃO extraídos do DWG (arquivo binário não conversível). Todos os valores são estimativas baseadas em projetos similares. |

---

**Próxima ação:** Converter DWG para formato legível (DXF/PDF) e atualizar este briefing com quantitativos reais.
