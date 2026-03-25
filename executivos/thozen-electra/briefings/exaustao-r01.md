# Briefing Técnico - Sistema de Exaustão (Churrasqueiras)
## Thozen Electra | Rev. R01

---

## ⚠️ STATUS DA EXTRAÇÃO

**Fonte disponível:** `RA_CHU_EXE_PROJETO_R00.dwg` (3.2 MB)  
**Formato:** AutoCAD 2018/2019/2020 (AC1032) — binário proprietário  
**Status conversão DXF:** ❌ **NÃO CONCLUÍDA**

**Tentativas realizadas:**
1. ✅ Localização do arquivo DWG original
2. ❌ Leitura com `ezdxf` (Python) — formato binário não suportado
3. ❌ Leitura com modo de recuperação `ezdxf.recover` — estrutura inválida
4. ❌ Instalação de LibreCAD via Homebrew — falha de instalação (deprecated cask)
5. ❌ Tentativa de instalação de outros conversores (qcad, draftsight) — não disponíveis

**Resultado:** Os quantitativos abaixo **permanecem como premissas técnicas** baseadas em projetos similares.

**⚠️ LIMITAÇÃO CRÍTICA:** Sem conversão DWG→DXF ou acesso a software CAD, **não é possível extrair dados reais do projeto**.

---

## 📋 AÇÕES NECESSÁRIAS PARA COMPLETAR A EXTRAÇÃO

### Opção 1: Conversão DWG → DXF (RECOMENDADA)
O time precisa converter o arquivo usando uma destas ferramentas:

**Gratuitas:**
- **ODA File Converter** (Windows/macOS/Linux) — [https://www.opendesign.com/guestfiles/oda_file_converter](https://www.opendesign.com/guestfiles/oda_file_converter)
  - Download → Instalar → Abrir → Selecionar arquivo DWG → Output format: "DXF AutoCAD 2018" → Convert
  - Enviar DXF gerado de volta no canal

**Pagas (se disponíveis):**
- AutoCAD → Abrir DWG → "Salvar como" → DXF
- BricsCAD → Abrir DWG → Export → DXF
- DraftSight → Abrir DWG → Export → DXF

**Após conversão:**
1. Enviar DXF no canal do Slack
2. Avisar: `@Cartesiano já enviei o DXF de exaustão`
3. Bot processará automaticamente e atualizará briefing para R02

---

### Opção 2: PDF Plotado (ALTERNATIVA)
Se conversão DXF não for viável, plotar PDF com:
- Plantas baixas do pavimento lazer (churrasqueiras)
- Cortes/detalhes da prumada de exaustão
- Legendas e especificações técnicas VISÍVEIS (zoom adequado)
- Tabela de equipamentos (exaustores, coifas, dutos)

**Após gerar PDF:**
1. Enviar PDF no canal do Slack
2. Avisar: `@Cartesiano já enviei o PDF de exaustão`
3. Bot extrairá dados via OCR/análise visual

---

### Opção 3: Tabela Manual (ÚLTIMO RECURSO)
Preencher tabela abaixo e enviar no Slack:

```
EQUIPAMENTOS:
- Exaustores: <quantidade>, <vazão m³/h>, <potência CV>, <modelo/fabricante>
- Coifas: <quantidade>, <dimensões LxPxH>, <material>
- Churrasqueiras atendidas: <quantidade>, <localização>

DUTOS:
- Duto horizontal: <metragem total>, <diâmetro/seção>
- Duto vertical (prumada): <metragem total>, <diâmetro>
- Curvas/joelhos: <quantidade>, <tipo>
- Dampers corta-fogo: <quantidade>, <localização>

INSTALAÇÃO ELÉTRICA:
- Quadro de origem: <identificação>
- Cabos alimentadores: <bitola>, <metragem>
- Proteções: <disjuntores>, <contatores>
- Tipo de controle: <manual/automático>
```

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

⚠️ **TODOS OS VALORES ABAIXO SÃO PREMISSAS — AGUARDANDO DXF/PDF PARA VALIDAÇÃO**

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

⚠️ **ATENÇÃO:** Todos os quantitativos abaixo são **PREMISSAS** e precisam ser validados com base no DXF/PDF.

### 3.1 Equipamentos Principais

#### 3.1.1 Exaustores Centrífugos

**Cenário 1: Sistema centralizado (1 exaustor para todas as churrasqueiras)**

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Exaustor centrífugo de média pressão | Vazão: 8.000-12.000 m³/h<br>Pressão estática: 40-60 mmCA<br>Motor: 5-7,5 CV (trifásico 220/380V)<br>Rotação: 1750 rpm<br>Material: rotor em aço carbono com pintura epóxi<br>Nível de ruído: < 75 dB(A) a 1,5m | UN | 1 | ⚠️ A VALIDAR COM DXF |

**Cenário 2: Sistema individualizado (1 exaustor por churrasqueira)**

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Exaustor centrífugo de baixa/média pressão | Vazão: 2.000-3.000 m³/h<br>Pressão estática: 25-35 mmCA<br>Motor: 1,5-2,0 CV (trifásico 220/380V)<br>Rotação: 1750 rpm<br>Material: rotor em aço carbono com pintura epóxi<br>Nível de ruído: < 70 dB(A) a 1,5m | UN | 2-4 | ⚠️ A VALIDAR COM DXF |

---

#### 3.1.2 Coifas de Captação

| Descrição | Especificação Estimada | UN | QTD | Observação |
|-----------|------------------------|-----|-----|------------|
| Coifa de parede em aço inox AISI 304 | Dimensões típicas: 1,20 x 0,80 m (LxP)<br>Altura: 0,50-0,60 m<br>Filtros: tipo labirinto (alumínio), removíveis<br>Iluminação: LED 2x10W, 6500K<br>Acabamento: escovado | UN | 2-4 | ⚠️ A VALIDAR COM DXF |

---

### 3.2 Dutos e Acessórios

⚠️ **Metragens estimadas — DEPENDEM DO LAYOUT E ROTEAMENTO**

#### 3.2.1 Dutos Retos

**Premissa:** Duto vertical do 7º pav. (Lazer) até cobertura/casa de máquinas = ~25-30 pavimentos × 2,80m = **70-84m de altura**

**Premissa:** Trecho horizontal no lazer (da churrasqueira até prumada) = **5-15m por churrasqueira**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Duto retangular 400x300mm, chapa #24 galv. | Seção nominal conforme cálculo de perda de carga | m | 20-40 | ⚠️ A VALIDAR COM DXF |
| Duto retangular 500x400mm, chapa #24 galv. | Seção nominal (trecho de interligação/principal) | m | 10-20 | ⚠️ A VALIDAR COM DXF |
| Duto circular Ø300mm, chapa #24 galv. | Duto vertical (prumada) | m | 70-90 | ⚠️ A VALIDAR COM DXF |
| Duto circular Ø400mm, chapa #24 galv. | Duto vertical (se sistema centralizado) | m | 70-90 | ⚠️ A VALIDAR COM DXF |

---

#### 3.2.2 Conexões e Acessórios

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Curva 90° (raio longo), chapa #24 galv. | Conforme diâmetro/seção do duto | UN | 8-16 | ⚠️ A VALIDAR COM DXF |
| Joelho 90°, chapa #24 galv. | Conforme diâmetro/seção do duto | UN | 4-8 | ⚠️ A VALIDAR COM DXF |
| Transição retangular-circular | Da saída da coifa (retangular) para duto vertical (circular) | UN | 2-4 | 1 por churrasqueira |
| Damper corta-fogo 90 min, Ø300mm | Instalado na passagem entre pavimentos | UN | 2-4 | ⚠️ Verificar exigência PCI |
| Registro de gaveta (damper manual) | Ø300mm, chapa #18 galv. | UN | 2-4 | 1 por ramal |
| Chapéu de exaustão (tipo chinês) | Ø300-400mm, alumínio ou galv., tela contra insetos | UN | 1-2 | Descarga na cobertura |

---

#### 3.2.3 Suportes e Fixações

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Suporte tipo mão-francesa | Para dutos verticais, a cada 3,0m | UN | 25-30 | ⚠️ A VALIDAR COM DXF |
| Abraçadeira metálica | Ø300-400mm, com borracha anti-vibração | UN | 30-40 | Fixação de dutos circulares |
| Perfil "U" galv. para fixação de dutos retang. | 40x40x3mm | m | 40-60 | Suporte de trechos horizontais |
| Tirante roscado M10 com porcas e arruelas | Para suspensão de dutos horizontais | UN | 50-80 | Espaçamento 1,5-2,0m |

---

### 3.3 Grelhas e Ventilação de Compensação

**Premissa:** Para cada m³/h de ar exaurido, é necessário admitir aproximadamente o mesmo volume de ar externo (ventilação de compensação).

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Grelha de ventilação em alumínio anodizado | Dimensões: 600x300mm<br>Área livre: ~0,14 m²<br>Aletas fixas 45° | UN | 4-8 | ⚠️ A VALIDAR COM DXF |
| Tela mosquiteiro em alumínio | Para proteção das grelhas | m² | 2-4 | ⚠️ Conforme área total de grelhas |

---

### 3.4 Instalação Elétrica Associada

⚠️ **PREMISSAS — VERIFICAR COMPATIBILIDADE COM PROJETO ELÉTRICO (DISCIPLINA 09)**

#### 3.4.1 Alimentação dos Exaustores

**Cenário 1: 1 exaustor de 5-7,5 CV**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Cabo unipolar 6mm² (3F+N+T), 750V, anti-chama | Do quadro até exaustor | m | 80-100 | ⚠️ A VALIDAR COM DXF |
| Disjuntor tripolar 25-32A, curva D | Proteção no quadro de comando | UN | 1 | Conforme corrente nominal do motor |
| Contator tripolar 25A, bobina 220V | Acionamento do motor | UN | 1 | |
| Relé térmico 10-16A (ajustável) | Proteção contra sobrecarga | UN | 1 | |
| Botoeira liga/desliga, caixa estanque IP65 | Comando local | UN | 1 | |

**Cenário 2: 2-4 exaustores de 1,5-2,0 CV cada**

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Cabo unipolar 4mm² (3F+N+T), 750V, anti-chama | Do quadro até cada exaustor | m | 160-200 | ⚠️ A VALIDAR COM DXF |
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
| Cabo alimentador 16mm² (3F+N+T), 750V | Do QD principal do lazer até quadro de exaustão | m | 20-40 | ⚠️ A VALIDAR COM DXF |

---

#### 3.4.3 Iluminação das Coifas

| Descrição | Especificação | UN | QTD | Observação |
|-----------|--------------|-----|-----|------------|
| Luminária LED 10W, 6500K, integrada à coifa | 220V, IP54 | UN | 4-8 | 2 por coifa (típico) |
| Cabo PP 2x1,5mm² | Alimentação das luminárias | m | 10-20 | ⚠️ A VALIDAR COM DXF |
| Interruptor simples, caixa 4x2" | Comando local das luzes | UN | 2-4 | 1 por churrasqueira |

---

### 3.5 Controles e Automação (Se Houver)

⚠️ **PREMISSA: Sistema pode ter controle manual simples OU automação — VALIDAR COM DXF**

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
  - Localização: `projetos/thozen-electra/projetos/13 CHURRASQUEIRA EXAUSTAO/DWG/`
  - Formato: AutoCAD 2018/2019/2020 (AC1032)
  - Status: ❌ Não conversível para DXF com ferramentas disponíveis

### 4.2 Arquivos de Referência (Consultados)
- **PROJETO.md** - Dados gerais do Thozen Electra
  - Pavimentos: 32 (6 garagens + lazer + 24 tipos + térreo + casa de máquinas)
  - Lazer: 7º pavimento

### 4.3 Normas e Referências Técnicas
- NBR 14518:2000 - Sistemas de ventilação para cozinhas profissionais
- NBR 16401-1:2008 - Instalações de ar-condicionado - Sistemas centrais e unitários
- Catálogos de fabricantes:
  - Cia Paulista de Ventilação (exaustores)
  - Otam (coifas inox)
  - Metalflex (dutos e conexões)

---

## 5. Observações e Pendências

### 5.1 Dados Faltantes (CRÍTICOS) — ⚠️ STATUS INALTERADO DESDE R00

**Não foi possível extrair do DWG — AGUARDANDO CONVERSÃO:**

1. ❌ **Quantidade exata de churrasqueiras** → Estimado: 2-4 UN (típico)
2. ❌ **Dimensões das churrasqueiras** → Necessário para dimensionar coifas e vazão
3. ❌ **Layout das churrasqueiras no pavimento lazer** → Impacta metragem de dutos horizontais
4. ❌ **Vazão de projeto de cada exaustor** → Parâmetro crítico para seleção de equipamentos
5. ❌ **Diâmetros especificados dos dutos** → Estimado com base em vazões típicas (DN 300-400)
6. ❌ **Potência dos motores** → Estimado: 1,5-7,5 CV (conforme cenário)
7. ❌ **Roteamento vertical da prumada** → Impacta metragem total e interferências
8. ❌ **Ponto de descarga na cobertura** → Necessário para especificar chapéu de exaustão
9. ❌ **Tipo de controle** (manual/automático) → Impacta custos e especificações
10. ❌ **Integração com BMS/automação predial** → Se houver, impacta protocolos e interfaces

---

### 5.2 Interferências e Compatibilizações

⚠️ **Verificar com outras disciplinas (APÓS VALIDAÇÃO DE QUANTITATIVOS):**

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

### 5.3 Checklist de Próximas Ações

**Etapa 1: Obter dados do projeto (CRÍTICO — BLOQUEADOR)**
- [ ] **OPÇÃO A:** Converter DWG→DXF usando ODA File Converter ou AutoCAD
  - [ ] Baixar ODA File Converter (gratuito)
  - [ ] Converter `RA_CHU_EXE_PROJETO_R00.dwg` → DXF
  - [ ] Enviar DXF no Slack → `@Cartesiano já enviei o DXF de exaustão`
  - [ ] Bot processa DXF automaticamente → atualiza briefing para R02

- [ ] **OPÇÃO B:** Plotar PDF com especificações técnicas
  - [ ] Gerar PDF com: plantas, cortes, legendas, tabela de equipamentos
  - [ ] Enviar PDF no Slack → `@Cartesiano já enviei o PDF de exaustão`
  - [ ] Bot extrai dados via OCR → atualiza briefing para R02

- [ ] **OPÇÃO C:** Preencher tabela manual (último recurso)
  - [ ] Extrair dados do projeto manualmente
  - [ ] Enviar tabela preenchida no Slack (ver modelo na seção "AÇÕES NECESSÁRIAS")
  - [ ] Bot valida e incorpora ao briefing

**Etapa 2: Compatibilização com disciplinas complementares (APÓS ETAPA 1)**
- [ ] Cruzar com projeto elétrico (09) → confirmar alimentação, quadros, cabos
- [ ] Cruzar com arquitetura (02) → layout exato, interferências, acabamentos
- [ ] Cruzar com estrutura (01) → passagens, furos, reforços

**Etapa 3: Validação de premissas (APÓS ETAPA 2)**
- [ ] Confirmar com equipe de projetos:
  - Sistema centralizado (1 exaustor) OU individualizado (1 por churrasqueira)?
  - Tipo de controle (manual/automático)?
  - Integração com BMS?
- [ ] Confirmar normas aplicáveis (CSMSP, CBPMESP, condomínio)

**Etapa 4: Geração de planilha executiva (APÓS ETAPA 3)**
- [ ] Gerar planilha Excel com:
  - Código Memorial (N1 14.08 - Exaustão)
  - Descrição detalhada
  - Especificação completa
  - UN | QTD | Preço Unit. | Total
  - Observações e premissas

---

## 6. Estimativa Preliminar de Custos

⚠️ **Estimativa baseada em PREMISSAS — Margem de erro: ±30-50%**

**Faixas de custo típicas (ordem de grandeza):**

### Cenário 1: Sistema Centralizado (1 exaustor grande)
| Grupo | Descrição | Estimativa (R$) |
|-------|-----------|----------------|
| Equipamentos | Exaustor + coifas + grelhas | 25.000 - 45.000 |
| Dutos e acessórios | Dutos galv. + conexões + suportes | 15.000 - 30.000 |
| Instalação elétrica | Cabos + quadro + proteções | 8.000 - 15.000 |
| Mão de obra | Instalação + comissionamento | 10.000 - 20.000 |
| **TOTAL ESTIMADO** | | **R$ 58.000 - 110.000** |

### Cenário 2: Sistema Individualizado (2-4 exaustores pequenos)
| Grupo | Descrição | Estimativa (R$) |
|-------|-----------|----------------|
| Equipamentos | Exaustores + coifas + grelhas | 20.000 - 40.000 |
| Dutos e acessórios | Dutos galv. + conexões + suportes | 12.000 - 25.000 |
| Instalação elétrica | Cabos + quadros + proteções | 6.000 - 12.000 |
| Mão de obra | Instalação + comissionamento | 8.000 - 15.000 |
| **TOTAL ESTIMADO** | | **R$ 46.000 - 92.000** |

**⚠️ IMPORTANTE:**
- Valores são ORDEM DE GRANDEZA — NÃO usar para contratação sem validação
- Após obter quantitativos reais, margem de erro reduz para ±10-15%
- Custos podem variar conforme:
  - Fabricante e especificação dos equipamentos
  - Complexidade da instalação (interferências, acessos)
  - Prazo de execução
  - Localização (São Paulo-SP)

**Próxima ação para refinar custo:** Obter DXF/PDF → extrair quantitativos reais → gerar planilha detalhada.

---

## Histórico de Revisões

| Rev | Data | Autor | Descrição |
|-----|------|-------|-----------|
| R00 | 2026-03-20 10:30 | Cartesiano (bot) | Briefing inicial com premissas técnicas. ⚠️ Quantitativos NÃO extraídos do DWG (arquivo binário não conversível). |
| R01 | 2026-03-20 10:56 | Cartesiano (bot) | Tentativa de extração via ezdxf FALHOU (formato AC1032 não suportado). Briefing mantido como premissas. Adicionada seção de AÇÕES NECESSÁRIAS com instruções para conversão DWG→DXF. Estimativa de custo adicionada (±30-50% margem). Checklist de próximas ações atualizado. |

---

**Status atual:** ⚠️ **BLOQUEADO — AGUARDANDO CONVERSÃO DWG→DXF OU PDF PLOTADO**

**Próxima ação:** Time deve seguir uma das opções descritas na seção "AÇÕES NECESSÁRIAS" e enviar arquivo processável.
