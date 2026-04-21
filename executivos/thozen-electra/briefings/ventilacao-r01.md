# Briefing: VENTILAÇÃO MECÂNICA (Escadas Pressurizadas) — Thozen Electra — R01

## Metadados
- **Projeto:** Thozen Electra
- **Cliente:** Thozen
- **Disciplina:** Ventilação Mecânica — Pressurização de Escadas
- **Revisão:** R01 (tentativa de extração automática)
- **Data:** 2026-03-20
- **Fonte dos dados:** RA_EVM_LEGAL_PROJETO_R05.dwg (tentativa de extração via strings)
- **Projetista responsável:** Rubens Alves (R. Rubens Alves)
- **Tipo de projeto:** Residencial vertical
- **Pavimentos:** 32 pavimentos (Térreo + 5 garagens + 1 lazer + 24 tipos + Casa de Máquinas)
- **Sistema:** Pressurização de escadas de emergência conforme NBR 14880

---

## 🔴 STATUS DA REVISÃO R01

**❌ EXTRAÇÃO AUTOMÁTICA FALHOU**

### Tentativas Realizadas
1. ✅ Busca por conversores DWG → DXF (ODA File Converter, dwg2dxf, LibreCAD CLI)
   - ❌ **Resultado:** Nenhum conversor disponível no sistema
2. ✅ Extração via strings do arquivo binário (72.678 strings analisadas)
   - ❌ **Resultado:** Texto codificado — 0 palavras-chave encontradas
3. ✅ Busca por especificações numéricas (m³/h, Pa, CV, RPM)
   - ❌ **Resultado:** Arquivo binário — dados inacessíveis sem conversão

### Conclusão
**O arquivo DWG NÃO pode ser processado automaticamente sem conversão para DXF.**

**Todos os dados abaixo permanecem como PREMISSAS TÉCNICAS (herdadas do Briefing R00) até que o DXF seja disponibilizado.**

Ver checklist detalhado em: `executivo/thozen-electra/briefings/ventilacao-r01-CHECKLIST.md`

---

## ⚠️ AVISO IMPORTANTE — Limitação de Extração (mantida de R00)

**Este briefing foi gerado com base em premissas técnicas padrão para sistemas de ventilação mecânica de escadas pressurizadas, conforme NBR 14880 e NBR 9077.**

**Razão (R00):** O arquivo DWG fornecido não pôde ser processado com as ferramentas disponíveis para extração automática de dados estruturados (quantidades, especificações técnicas, potências, vazões).

**Razão (R01):** Tentativa de extração automática falhou devido a:
- Falta de conversores DWG → DXF instalados no sistema
- Arquivo DWG binário (AutoCAD 2018/2019/2020) inacessível via parsing de strings
- Texto técnico codificado — não detectado via regex de palavras-chave

**Próximos passos necessários (R02):**
1. **CRÍTICO:** Obter versão DXF do arquivo (solicitar ao projetista Rubens Alves)
2. **CRÍTICO:** Obter memorial descritivo do sistema (PDF)
3. Processar DXF com ezdxf (Python) para extração de:
   - Metragem de dutos (POLYLINEs)
   - Ventiladores e especificações (blocos/textos)
   - Grelhas e difusores (blocos)
   - Dampers corta-fogo e motorizados (blocos)
   - Sensores e automação (textos/legendas)
4. Validar dados extraídos com memorial descritivo
5. Gerar briefing R02 com quantitativos reais

**Fonte das premissas:**
- NBR 14880:2024 — Saídas de emergência em edifícios — Escadas protegidas, escadas à prova de fumaça e pressurização de escadas
- NBR 9077:2022 — Saídas de emergência em edifícios
- Experiência Cartesian em projetos similares (edifícios residenciais de 25-35 pavimentos)

---

## 1. Especificações Gerais

### 1.1 Premissas de Projeto (NBR 14880)

**Requisitos normativos para edifício de 32 pavimentos:**
- **Tipo de escada:** Escada à prova de fumaça com pressurização positiva (PF2)
- **Diferencial de pressão:** 25 a 50 Pa entre escada e antecâmara/pavimento
- **Vazão de ar:** Mínimo 0,5 m³/s por porta aberta + compensação de infiltrações
- **Velocidade máxima nas portas abertas:** 12 m/s (limite de segurança)
- **Insuflamento:** Por ventiladores centrífugos instalados na cobertura (casa de máquinas)
- **Tomada de ar:** Externa, afastada de fontes de contaminação
- **Dutos:** Chapa de aço galvanizada, estanques, isolados termicamente
- **Controle:** Acionamento automático por detecção de incêndio + manual

### 1.2 Configuração Típica para Edifício de 32 Pavimentos

**Sistema estimado:**
- **⚠️ Escadas pressurizadas:** 2 unidades (premissa: edifício residencial típico — NÃO VALIDADO)
- **⚠️ Ventiladores:** 1 por escada (total: 2 ventiladores — NÃO VALIDADO)
- **Dutos verticais:** 1 por escada (shaft exclusivo)
- **Grelhas de insuflamento:** 1 a cada 4-6 pavimentos ou na antecâmara superior
- **Dampers corta-fogo:** Nas travessias de lajes (a cada pavimento ou conforme projeto)
- **Quadro elétrico:** Alimentação exclusiva, com fonte de emergência (gerador)

**Normas de referência:**
- NBR 14880:2024
- NBR 9077:2022
- NBR 10897:2022 (Proteção contra incêndio por chuveiro automático)
- IT 15/2019 (SP) — Controle de fumaça Parte 7: Escadas pressurizadas

---

## 2. Quantitativos Extraídos (⚠️ PREMISSAS — VALIDAR COM PROJETO)

**⚠️ ATENÇÃO R01:** Todos os quantitativos abaixo são PREMISSAS TÉCNICAS (herdadas de R00). Nenhum dado foi extraído automaticamente do DXF (conversão não disponível).

### 2.1 Ventiladores de Pressurização

⚠️ **ATENÇÃO:** Especificações abaixo são ESTIMATIVAS. Validar com memorial descritivo do projeto.

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Ventilador centrífugo de pressurização | Vazão: 8.000-12.000 m³/h, Pressão: 400-600 Pa, Potência: 5-7,5 CV | un | ⚠️ 2 | Premissa NBR 14880 | 1 por escada (NÃO VALIDADO) |
| 2 | Base antivibrante para ventilador | Concreto + amortecedores | un | ⚠️ 2 | Premissa | 1 por ventilador |
| 3 | Tomada de ar externa com veneziana | Alumínio, tela anti-insetos | un | ⚠️ 2 | Premissa | 1 por ventilador |
| 4 | Silenciador acústico | Atenuação mínima 20 dB | un | ⚠️ 2 | Premissa | Entrada dos ventiladores |

**Subtotal estimado:** R$ 30.000 - 50.000 (equipamentos + montagem)

**Premissas adotadas:**
- Vazão calculada para 3 portas abertas simultaneamente + infiltração: ~8.000-12.000 m³/h por escada
- Pressão de 400-600 Pa para vencer perdas de carga do sistema
- Ventiladores com motor trifásico 220/380V, IP55, instalados em casa de máquinas

### 2.2 Dutos de Insuflamento

⚠️ **ATENÇÃO:** Metragens estimadas com base em altura típica de pé-direito. Validar com projeto arquitetônico e DXF.

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Duto vertical principal | Chapa #18 (1,2mm), Ø600mm, galvanizado, estanque | m | ⚠️ 200 | Premissa | 100m x 2 escadas (NÃO VALIDADO — aguardar DXF) |
| 2 | Isolamento térmico de dutos | Lã de vidro 50mm + revestimento aluminizado | m² | ⚠️ 380 | Premissa | Área externa dos dutos verticais |
| 3 | Duto de derivação para antecâmaras | Chapa #20 (0,9mm), seção retangular 400x300mm | m | ⚠️ 60 | Premissa | ~2m x 15 derivações x 2 escadas |
| 4 | Curvas 90° para dutos Ø600mm | Chapa #18, raio longo, galvanizada | un | ⚠️ 6 | Premissa | 3 por sistema |
| 5 | Suportes para dutos verticais | Aço estrutural, fixação química | un | ⚠️ 64 | Premissa | A cada 3m (32 pav x 2 escadas) |
| 6 | Juntas de dilatação | Lona flexível, resistente a 300°C | un | ⚠️ 4 | Premissa | A cada 25m de duto vertical |

**Subtotal estimado:** R$ 60.000 - 90.000 (material + montagem + isolamento)

**Premissas adotadas:**
- Altura total de insuflamento: ~95m (32 pavimentos x ~3m de pé-direito)
- Duto vertical único por escada, com derivações nas antecâmaras ou pontos de insuflamento
- Diâmetro Ø600mm para vazão de 8.000-12.000 m³/h com velocidade controlada (6-8 m/s)
- Isolamento térmico para evitar condensação e manter temperatura do ar

### 2.3 Grelhas de Insuflamento e Difusores

⚠️ **ATENÇÃO:** Quantidade e localização estimadas. Validar com projeto executivo e DXF.

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Grelha de insuflamento para escada | Alumínio anodizado, 600x400mm, regulável | un | ⚠️ 12 | Premissa | ~6 grelhas x 2 escadas (NÃO VALIDADO) |
| 2 | Difusor de teto para antecâmara | Aço, Ø300mm, aletas ajustáveis | un | ⚠️ 30 | Premissa | 15 pavimentos x 2 escadas (se aplicável) |
| 3 | Plenum de distribuição | Chapa #20, 800x600x400mm | un | ⚠️ 12 | Premissa | 1 por grelha principal |

**Subtotal estimado:** R$ 8.000 - 15.000

**Premissas adotadas:**
- Grelhas principais a cada 4-6 pavimentos para distribuição uniforme de pressão
- Difusores em antecâmaras (se existirem) para insuflamento direto
- Dimensionamento para velocidade máxima de 8 m/s nas grelhas

### 2.4 Dampers e Dispositivos de Controle

⚠️ **ATENÇÃO:** Especificações críticas para segurança — VALIDAR COM PROJETISTA.

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Damper corta-fogo 90min | Ø600mm, acionamento termomagnético (fusível 72°C) | un | ⚠️ 64 | Premissa | A cada pavimento x 2 escadas (NÃO VALIDADO) |
| 2 | Damper de regulagem (balanceamento) | Ø600mm, manual, com indicador de posição | un | ⚠️ 12 | Premissa | Derivações principais |
| 3 | Damper motorizado (sobrepressão) | Ø600mm, 24Vdc, modulante | un | ⚠️ 4 | Premissa | Controle de pressão (2 por escada) |
| 4 | Atuador elétrico para damper | 24Vdc, torque 10Nm, feedback analógico | un | ⚠️ 4 | Premissa | Para dampers motorizados |
| 5 | Sensor de pressão diferencial | 0-100 Pa, saída 4-20mA, display | un | ⚠️ 4 | Premissa | Monitoramento escada/antecâmara |

**Subtotal estimado:** R$ 80.000 - 120.000

**Premissas adotadas:**
- Dampers corta-fogo a cada pavimento para compartimentação vertical
- Dampers motorizados para controle automático de sobrepressão (evitar > 50 Pa)
- Sensores de pressão para monitoramento e ajuste em tempo real

### 2.5 Instalações Elétricas Associadas

⚠️ **ATENÇÃO:** Coordenar com projeto elétrico principal (disciplina 09).

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Quadro de comando (QC-VENT) | Metálico, IP65, disjuntores termomagnéticos | un | ⚠️ 1 | Premissa | Centralizado na casa de máquinas |
| 2 | Soft-starter para ventilador | 7,5 CV, 220/380V, 3F, bypass | un | ⚠️ 2 | Premissa | 1 por ventilador |
| 3 | Cabo alimentação ventiladores | 4x6mm², 750V, anti-chama | m | ⚠️ 50 | Premissa | Quadro → ventiladores |
| 4 | Cabo de comando dampers/sensores | 2x2,5mm², 300V, blindado | m | ⚠️ 250 | Premissa | Interligação QC → campo |
| 5 | Eletroduto rígido PVC Ø1" | Anti-chama, fixação em shaft | m | ⚠️ 250 | Premissa | Passagem de cabos |
| 6 | Botoeira de acionamento manual | Emergência, com sinalização luminosa | un | ⚠️ 4 | Premissa | Térreo + casa de máquinas (2 por local) |
| 7 | Sinalização luminosa (em operação) | LED verde, 220V | un | ⚠️ 4 | Premissa | Indicação de sistema ativo |

**Subtotal estimado:** R$ 25.000 - 40.000

**Premissas adotadas:**
- Alimentação trifásica 220/380V, circuito exclusivo, protegido por gerador
- Soft-starter para partida suave dos ventiladores (redução de pico de corrente)
- Interface com central de detecção de incêndio (contato seco)

### 2.6 Automação e Controle

⚠️ **ATENÇÃO:** Sistema crítico de segurança — especificação detalhada obrigatória.

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Controlador lógico programável (CLP) | 16 I/O, comunicação Modbus, fonte redundante | un | ⚠️ 1 | Premissa | Gerenciamento central |
| 2 | Interface com central de incêndio | Módulo de entrada (contato seco) | un | ⚠️ 1 | Premissa | Acionamento automático |
| 3 | IHM (Interface Homem-Máquina) | Touch-screen 7", IP65 | un | ⚠️ 1 | Premissa | Monitoramento em casa de máquinas |
| 4 | Software de supervisão (SCADA) | Licença, configuração, histórico de alarmes | un | ⚠️ 1 | Premissa | Registro de eventos |
| 5 | Sirene de alarme (falha sistema) | 220V, 110dB, estroboscópica | un | ⚠️ 2 | Premissa | Casa de máquinas + guarita |

**Subtotal estimado:** R$ 15.000 - 25.000

**Premissas adotadas:**
- Acionamento automático via central de detecção de incêndio
- Acionamento manual por botoeiras de emergência
- Controle de pressão com ajuste automático (dampers modulantes)
- Registro de eventos e falhas para manutenção/perícia

---

## 3. Resumo de Quantitativos Principais

⚠️ **TODOS os valores abaixo são PREMISSAS (NÃO VALIDADOS — aguardando DXF)**

### Equipamentos
- **⚠️ Ventiladores centrífugos:** 2 un (5-7,5 CV cada)
- **⚠️ Dampers corta-fogo 90min:** 64 un
- **⚠️ Dampers motorizados:** 4 un
- **⚠️ Sensores de pressão:** 4 un
- **⚠️ Grelhas/difusores:** 42 un

### Dutos e Componentes
- **⚠️ Duto vertical principal Ø600mm:** 200 m
- **⚠️ Duto de derivação:** 60 m
- **⚠️ Isolamento térmico:** 380 m²
- **⚠️ Suportes:** 64 un

### Elétrica
- **⚠️ Cabos de força:** 50 m
- **⚠️ Cabos de comando:** 250 m
- **⚠️ Eletrodutos:** 250 m
- **⚠️ Quadro de comando:** 1 un
- **⚠️ Soft-starters:** 2 un

### Automação
- **⚠️ CLP:** 1 un
- **⚠️ IHM:** 1 un
- **⚠️ Módulos de interface:** diversos

---

## 4. Premissas Adotadas (CRÍTICO — VALIDAR COM PROJETO)

| # | Premissa | Justificativa | Status R01 |
|---|---------|---------------|------------|
| 1 | **2 escadas pressurizadas** | Típico para edifício residencial de 32 pavimentos conforme NBR 9077 (população > 300 pessoas) | ⚠️ NÃO VALIDADO |
| 2 | **Vazão 8.000-12.000 m³/h por escada** | NBR 14880: 0,5 m³/s por porta aberta + 3 portas simultâneas + infiltrações | ⚠️ NÃO VALIDADO |
| 3 | **Pressão 400-600 Pa nos ventiladores** | Compensação de perdas de carga em dutos verticais de ~100m + singularidades | ⚠️ NÃO VALIDADO |
| 4 | **Diferencial de pressão 25-50 Pa** | Faixa normativa NBR 14880 para escadas PF2 | ⚠️ NÃO VALIDADO |
| 5 | **Dampers corta-fogo a cada pavimento** | Compartimentação vertical conforme IT 09/2019 (SP) | ⚠️ NÃO VALIDADO |
| 6 | **Grelhas a cada 5 pavimentos** | Distribuição uniforme de pressão ao longo do shaft | ⚠️ NÃO VALIDADO |
| 7 | **Duto Ø600mm** | Dimensionamento para vazão máxima com velocidade < 8 m/s (redução de ruído) | ⚠️ NÃO VALIDADO |
| 8 | **Isolamento térmico 50mm** | Prevenção de condensação e manutenção de temperatura de insuflamento | ⚠️ NÃO VALIDADO |
| 9 | **Alimentação por gerador** | Requisito de emergência NBR 14880 (sistema operante durante incêndio) | ⚠️ NÃO VALIDADO |
| 10 | **Controle via CLP com interface para central de incêndio** | Acionamento automático obrigatório por norma | ⚠️ NÃO VALIDADO |

---

## 5. Precificação

| # | Tipo de Insumo/Serviço | Fonte do Preço | Data-base | Observação |
|---|----------------------|---------------|-----------|------------|
| 1 | Ventilador centrífugo 5-7,5 CV | Cotação fabricante (Otam, Cia. Minas, etc.) | Março/2026 | Incluir transporte e montagem |
| 2 | Dutos galvanizados #18 | Cotação (m² de chapa + fabricação) | Março/2026 | Considerar perda de 10% |
| 3 | Dampers corta-fogo 90min | Cotação especializada (Metalfire, Iberica) | Março/2026 | Com certificação INMETRO |
| 4 | Isolamento térmico (lã de vidro) | SINAPI ou cotação (Isover, Rockwool) | Março/2026 | Incluir revestimento |
| 5 | CLP e automação | Cotação (Siemens, WEG, Schneider) | Março/2026 | Incluir programação e comissionamento |
| 6 | Cabos e eletrodutos | SINAPI | Março/2026 | Composições padrão |
| 7 | Mão de obra montagem | Base Cartesian ou SINAPI adaptado | Março/2026 | Considerar trabalho em altura |
| 8 | Comissionamento e testes | Especializado (empresa com ART) | Março/2026 | NBR 14880 exige ensaios de aceitação |

**Observação crítica:** 
- Dampers corta-fogo e ventiladores são itens críticos de segurança — exigir certificação e garantia
- Testes de aceitação são obrigatórios (NBR 14880): medição de pressão diferencial, vazão, velocidade, acionamento automático
- Prever BDI + contingência para revisões de projeto (comum em sistemas de pressurização)

---

## 6. Pendências / Dúvidas (CRÍTICAS — Resolver ANTES de orçar)

**PENDÊNCIAS BLOQUEADORAS (R01):**

- [ ] **🔴 Obter versão DXF do arquivo RA_EVM_LEGAL_PROJETO_R05.dwg** (solicitar ao projetista)
- [ ] **🔴 Obter memorial descritivo do sistema** (PDF com especificações técnicas)
- [ ] **🔴 Instalar conversor DWG → DXF** (ODA File Converter) OU processar em máquina com AutoCAD

**PENDÊNCIAS DE VALIDAÇÃO (aguardam DXF):**

- [ ] **Número real de escadas pressurizadas** (2 é premissa — confirmar com arquitetura)
- [ ] **Vazão e pressão especificadas pelo projetista** (valores atuais são estimativas)
- [ ] **Potência exata dos ventiladores** (5-7,5 CV é faixa típica — pode variar)
- [ ] **Diâmetro e material dos dutos** (Ø600mm é premissa — validar memorial)
- [ ] **Localização e quantidade de grelhas/difusores** (extrair de DXF)
- [ ] **Quantidade e localização de dampers** (crítico para custo)
- [ ] **Especificação de dampers corta-fogo** (90min ou 120min? Marca preferencial?)
- [ ] **Há antecâmaras pressurizadas?** (afeta configuração e vazão total)
- [ ] **Interface com central de incêndio** (endereçável? protocolo de comunicação?)
- [ ] **Ponto de instalação dos ventiladores** (casa de máquinas ou cobertura técnica?)
- [ ] **Tomada de ar externa: localização e afastamento** (afastamento de escape de garagem?)
- [ ] **Requisitos de nível de ruído** (limites NBR 10151 para área residencial)
- [ ] **Fonte de alimentação de emergência** (gerador exclusivo ou compartilhado?)

**DÚVIDAS TÉCNICAS:**

- [ ] Há necessidade de pressurização de elevadores de emergência? (NBR 16042)
- [ ] Sistema prevê modo de teste/manutenção?
- [ ] Qual o regime de manutenção especificado? (mensal/trimestral/semestral?)
- [ ] Há exigência de monitoramento remoto (BMS/BIM)?

---

## 7. Mapeamento para Memorial Cartesiano

| Subsistema do Briefing | Código Memorial (N2/N3) | Observação |
|------------------------|------------------------|------------|
| Ventiladores de Pressurização | 14.08.001 | Ventilação Mecânica — Equipamentos |
| Dutos e Isolamento | 14.08.002 | Ventilação Mecânica — Dutos |
| Grelhas e Difusores | 14.08.003 | Ventilação Mecânica — Distribuição de Ar |
| Dampers Corta-Fogo | 14.08.004 | Ventilação Mecânica — Proteção Passiva |
| Dampers Motorizados e Atuadores | 14.08.005 | Ventilação Mecânica — Controle |
| Sensores e Instrumentação | 14.08.006 | Ventilação Mecânica — Monitoramento |
| Instalações Elétricas Associadas | 14.08.007 | Ventilação Mecânica — Elétrica |
| Automação (CLP, IHM, SCADA) | 14.08.008 | Ventilação Mecânica — Automação |
| Comissionamento e Testes | 14.08.009 | Ventilação Mecânica — Testes NBR 14880 |

**Nota:** Mapeamento preliminar — ajustar conforme estrutura do Memorial Cartesiano em vigor.

---

## 8. Observações Técnicas Adicionais

### 8.1 Testes de Aceitação Obrigatórios (NBR 14880)

Antes da liberação para uso, o sistema deve ser testado e aprovado, incluindo:

1. **Teste de pressão diferencial:**
   - Com todas as portas fechadas: 25-50 Pa (escada vs. pavimento)
   - Com portas críticas abertas: pressão mínima mantida

2. **Teste de vazão:**
   - Vazão de insuflamento medida e comparada com projeto
   - Velocidade nas portas abertas < 12 m/s (NBR 14880)

3. **Teste de acionamento:**
   - Automático (via central de incêndio)
   - Manual (botoeiras)
   - Tempo de resposta < 30s (partida do ventilador)

4. **Teste de failsafe:**
   - Simulação de falta de energia → gerador → sistema OK
   - Simulação de falha de CLP → modo manual OK

5. **Teste de dampers:**
   - Fechamento de dampers corta-fogo em caso de incêndio
   - Abertura/fechamento de dampers motorizados

**Responsável:** Empresa especializada com ART de instalação e comissionamento.

### 8.2 Manutenção Preventiva

Sistema de segurança requer manutenção rigorosa conforme IT 15/2019 (SP):

| Frequência | Atividade | Responsável |
|------------|-----------|-------------|
| **Mensal** | Inspeção visual, teste de botoeiras, limpeza de filtros | Equipe predial |
| **Trimestral** | Teste de acionamento completo (automático + manual) | Empresa especializada |
| **Semestral** | Teste de pressão diferencial, calibração de sensores | Empresa especializada |
| **Anual** | Teste completo conforme NBR 14880, emissão de laudo | Empresa certificada com ART |

**Custo estimado de manutenção anual:** R$ 8.000 - 12.000

### 8.3 Interferências e Coordenação com Outras Disciplinas

| Disciplina | Interferência | Coordenação Necessária |
|-----------|---------------|------------------------|
| **Estrutura** | Shafts para dutos verticais, furos em lajes | Definir dimensões de shafts e passagens |
| **Arquitetura** | Espaço em casa de máquinas, grelhas aparentes | Compatibilizar ventiladores com layout |
| **Elétrica** | Alimentação, gerador, central de incêndio | Definir potência, bitola de cabos, interface |
| **PCI** | Interface com central de detecção | Protocolo de comunicação (contato seco, Modbus) |
| **Hidráulica** | Drenagem de condensado (se aplicável) | Ponto de descarte em casa de máquinas |
| **Elevadores** | Pressurização de elevadores de emergência (se aplicável) | Verificar se há exigência normativa |

---

## 9. Arquivos de Referência

### 9.1 Arquivos Recebidos

| Arquivo | Tipo | Tamanho | Data | Local |
|---------|------|---------|------|-------|
| RA_EVM_LEGAL_PROJETO_R05.dwg | DWG (AutoCAD 2018/2019/2020) | 5.39 MB | Out/2023 | executivo/thozen-electra/fontes/ |

### 9.2 Arquivos Necessários (SOLICITAR — CRÍTICO)

- [ ] **🔴 RA_EVM_LEGAL_PROJETO_R05.dxf** (versão DXF do projeto)
- [ ] Memorial descritivo do sistema de ventilação mecânica (PDF)
- [ ] Prancha de planta de localização de equipamentos
- [ ] Prancha de detalhes de montagem (dutos, suportes, fixações)
- [ ] Planilha de equipamentos (marca, modelo, especificações)
- [ ] Isométrico de dutos (para conferência de metragens)
- [ ] Esquema elétrico (alimentação, comando, automação)
- [ ] Especificação de dampers corta-fogo (marca, certificação)

---

## 10. Histórico de Revisões

| Revisão | Data | Ação | Resultado |
|---------|------|------|-----------|
| R00 | 2026-03-20 | Briefing gerado com premissas técnicas (sem DXF) | Incerteza ±30% |
| R01 | 2026-03-20 | Tentativa de extração automática do DWG | ❌ Falhou — arquivo binário não processável |
| R01 | 2026-03-20 | Documentação de bloqueadores e checklist | ✅ Concluído |

**Próxima revisão (R02):**
- Aguardar conversão DWG → DXF
- Processar DXF com ezdxf (Python)
- Extrair quantitativos reais
- Validar especificações técnicas
- Gerar briefing R02 com dados validados

---

## 11. Estimativa de Custo Total (Ordem de Grandeza)

⚠️ **ATENÇÃO R01:** Valores MANTIDOS de R00 (sem mudança — extração falhou). NÃO utilizar para contratação sem validação de quantitativos.

| Grupo | Subtotal (R$) |
|-------|---------------|
| Ventiladores e equipamentos principais | 30.000 - 50.000 |
| Dutos, isolamento e suportes | 60.000 - 90.000 |
| Grelhas e difusores | 8.000 - 15.000 |
| Dampers (corta-fogo + motorizados) | 80.000 - 120.000 |
| Instalações elétricas | 25.000 - 40.000 |
| Automação e controle | 15.000 - 25.000 |
| Comissionamento e testes | 10.000 - 15.000 |
| **TOTAL ESTIMADO** | **228.000 - 355.000** |

**BDI sugerido:** 25-30% (sistema especializado)

**Contingência sugerida:** 20-25% (⚠️ AUMENTADA devido à alta incerteza — dados não validados)

**TOTAL COM BDI E CONTINGÊNCIA:** R$ 342.000 - 545.000 (⚠️ faixa ampliada)

**Custo por pavimento:** R$ 10.700 - 17.000 (32 pavimentos)

**Incerteza estimada:** ±30-50% (mantida de R00 — aguardando DXF para reduzir)

---

*Briefing R01 gerado por Cartesiano (subagente de extração) | Data: 2026-03-20*

*⚠️ VALIDAÇÃO OBRIGATÓRIA: Este documento foi gerado com base em premissas técnicas padrão devido à impossibilidade de extração automática do arquivo DWG. Todos os quantitativos e especificações devem ser validados com o projeto executivo (DXF + memorial descritivo) antes de utilização em orçamento.*

*📋 Ver checklist detalhado em: `executivo/thozen-electra/briefings/ventilacao-r01-CHECKLIST.md`*
