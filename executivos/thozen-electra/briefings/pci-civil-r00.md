# Briefing: PREVENTIVO INCÊNDIO CIVIL — Thozen Electra — R00

## Metadados
- **Projeto:** Thozen Electra Towers
- **Cliente:** [a confirmar]
- **Disciplina:** Instalações Especiais - Prevenção e Combate a Incêndio (PCI)
- **Revisão:** R00
- **Data:** 2026-03-20
- **Fonte dos dados:**
  - `348 - PCI - rev.01 - ELECTRA TOWERS - TORRE A.ifc` (24 MB, IFC2X3)
  - `348 - PCI - rev.01 - ELECTRA TOWERS - TORRE B.ifc` (23 MB, IFC2X3)
  - `348 - IGC - rev.01 - ELECTRA TOWERS - TORRE A.ifc` (37 MB, IFC2X3)
  - `348 - IGC - rev.01 -ELECTRA TOWERS - TORRE B.ifc` (42 MB, IFC2X3)
  - DWGs de 11 pranchas (rev.00 e rev-00)
- **Projetista responsável:** [a confirmar nos DWGs]
- **Área total construída:** [a confirmar]
- **Pavimentos:** 
  - Torre A: 1° Térreo, 2°-6° Garagem (5 pav), 7° Lazer, 8°-31° Tipo (24 pav), Casa de Máquinas, Reservatórios, Cobertura — **34 pavimentos**
  - Torre B: 1° Térreo, 2°-6° Garagem (5 pav), 7° Lazer, 8°-31° Tipo (24 pav), Casa de Máquinas, Reservatórios, Cobertura — **34 pavimentos**

---

## 1. Especificações Gerais

### Sistema de Prevenção e Combate a Incêndio

**Sistemas identificados:**
1. **Sistema de Hidrantes** — rede de tubulação em ferro galvanizado vermelho com abrigos de hidrante
2. **Sistema de Extintores Portáteis** — extintores PQS e CO2 com sinalização
3. **Sistema de Sinalização de Emergência** — placas fotoluminescentes e pintura de piso

**Normas de referência presumidas:**
- NBR 13714 — Sistemas de hidrantes e de mangotinhos para combate a incêndio
- NBR 12693 — Sistemas de proteção por extintores de incêndio
- NBR 13434 — Sinalização de segurança contra incêndio e pânico

**Material predominante:**
- Tubulação: Ferro galvanizado vermelho (pintura vermelha), rosca BSP
- Diâmetro predominante: Ø150mm (aproximadamente 6")
- Conexões: Ferro galvanizado (cotovelos 90°, tês de redução, luvas)

**⚠️ Observações importantes:**
- **NÃO foram identificados sprinklers/chuveiros automáticos** nos arquivos IFC fornecidos
- **NÃO foram identificados reservatórios, bombas de incêndio ou casa de bombas** nos metadados IFC (equipamentos podem estar em arquivos separados não fornecidos)
- Sistema parece ser voltado para hidrantes prediais de recalque

---

## 2. Quantitativos Extraídos

### 2.1 Sistema de Hidrantes — Tubulação e Distribuição

| # | Item | Material | Diâmetro | UN | QTD | Fonte | Observação |
|---|------|----------|----------|-----|-----|-------|------------|
| 1 | Tubulação FG vermelho BSP | Ferro galvanizado pintado vermelho | Ø150mm (6") | m | 67.255 | IFC PCI rev.01 (geometria 3D) | 424 trechos (218 Torre A + 206 Torre B) |
| 2 | Cotovelo 90° | Ferro galvanizado | Ø150mm | un | 117 | IFC PCI rev.01 | 65 Torre A + 52 Torre B |
| 3 | Tê de redução | Ferro galvanizado | Variado | un | 151 | IFC PCI rev.01 | 75 Torre A + 76 Torre B |
| 4 | Luva de união | Ferro galvanizado | Ø150mm | un | 4 | IFC PCI rev.01 | 2 Torre A + 2 Torre B |

**Subtotal estimado tubulação:** [a precificar]

**⚠️ ATENÇÃO — Metragem parece subestimada:**
- A metragem de 67,26m para um edifício de 34 pavimentos parece muito baixa
- Provavelmente há erro na extração de comprimentos do IFC (geometria não padronizada)
- **RECOMENDAÇÃO:** Validar metragens diretamente nas pranchas DWG ou solicitar memorial descritivo

---

### 2.2 Sistema de Hidrantes — Dispositivos e Abrigos

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 5 | Abrigo de hidrante | Caixa de alumínio | un | 67 | IFC PCI rev.01 | 33 Torre A + 34 Torre B |
| 6 | Válvula/Registro | Ø1/2" | un | 127 | IFC PCI rev.01 | 63 Torre A + 64 Torre B |
| 7 | Válvula de retenção | - | un | 11 | IFC PCI rev.01 | 6 Torre A + 5 Torre B |

**Componentes do abrigo (NÃO quantificados no IFC — verificar memorial):**
- [ ] Mangueira de incêndio (25m ou 30m) — **QTD: [a definir]**
- [ ] Esguicho regulável — **QTD: [a definir]**
- [ ] Chave de mangueira — **QTD: [a definir]**
- [ ] Adaptador de engate rápido — **QTD: [a definir]**

**Subtotal estimado abrigos:** [a precificar]

---

### 2.3 Sistema de Extintores Portáteis

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 8 | Extintor PQS 4kg classe BC | Pó químico seco, 4kg | un | 133 | IFC PCI rev.01 | 66 Torre A + 67 Torre B |
| 9 | Extintor CO2 6kg | Gás carbônico, 6kg | un | 7 | IFC PCI rev.01 | 3 Torre A + 4 Torre B |
| 10 | Extintor (tipo não especificado) | - | un | 5 | IFC PCI rev.01 | Tipo a confirmar nas pranchas |
| 11 | Suporte de parede p/ extintor | Metálico | un | 135 | IFC PCI rev.01 | 66 Torre A + 69 Torre B |

**Total de extintores:** 145 unidades

**Subtotal estimado extintores:** [a precificar]

---

### 2.4 Sistema de Sinalização de Emergência

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 12 | Placa fotoluminescente E5 | "Extintor de incêndio", 12 metros | un | 140 | IFC PCI rev.01 | 69 Torre A + 71 Torre B |
| 13 | Pintura de piso | Quadrado 85x85cm (sinalização extintor) | un | 21 | IFC PCI rev.01 | 11 Torre A + 10 Torre B |

**Sinalização adicional (NÃO quantificada — verificar pranchas):**
- [ ] Placa "Hidrante" — **QTD: [a definir, provavelmente 67]**
- [ ] Placa "Saída de emergência" — **QTD: [a definir]**
- [ ] Placa "Rota de fuga" — **QTD: [a definir]**
- [ ] Faixa fotoluminescente para escadas — **QTD: [a definir, m]**

**Subtotal estimado sinalização:** [a precificar]

---

### 2.5 Equipamentos de Bombeamento e Reservação (NÃO IDENTIFICADOS)

**⚠️ DADOS FALTANTES — Equipamentos críticos não encontrados nos IFCs:**

| # | Item | Especificação | UN | QTD | Fonte | Status |
|---|------|--------------|-----|-----|-------|--------|
| - | Reservatório inferior PCI | Capacidade [m³] | un | ? | - | ❌ Não encontrado |
| - | Reservatório superior PCI | Capacidade [m³] | un | ? | - | ❌ Não encontrado |
| - | Bomba principal PCI | Vazão [l/min], Altura [mca], Potência [CV] | un | ? | - | ❌ Não encontrado |
| - | Bomba reserva (jockey) | Vazão [l/min], Altura [mca], Potência [CV] | un | ? | - | ❌ Não encontrado |
| - | Quadro de comando bombas | - | un | ? | - | ❌ Não encontrado |
| - | Tubulação de sucção | Material, Ø | m | ? | - | ❌ Não encontrado |
| - | Tubulação de recalque | Material, Ø | m | ? | - | ❌ Não encontrado |
| - | Manômetros | - | un | ? | - | ❌ Não encontrado |
| - | Pressostatos | - | un | ? | - | ❌ Não encontrado |

**AÇÃO NECESSÁRIA:** Solicitar:
1. Memorial descritivo do sistema PCI
2. Prancha de detalhamento da casa de bombas
3. Especificação dos equipamentos hidromecânicos
4. Projeto hidráulico completo (se existir arquivo separado)

---

## 3. Resumo de Quantitativos Principais

### Sistema de Hidrantes
- **Tubulação total:** 67,26m ⚠️ (verificar — valor parece subestimado)
- **Abrigos de hidrante:** 67 un
- **Conexões totais:** 272 un (117 cotovelos + 151 tês + 4 luvas)
- **Válvulas/Registros:** 138 un

### Sistema de Extintores
- **Extintores PQS 4kg:** 133 un
- **Extintores CO2 6kg:** 7 un
- **Extintores (outros):** 5 un
- **Suportes de parede:** 135 un

### Sinalização
- **Placas fotoluminescentes E5:** 140 un
- **Pintura de piso:** 21 un

### Equipamentos (NÃO QUANTIFICADOS)
- Reservatórios: **[a definir]**
- Bombas: **[a definir]**
- Outros equipamentos: **[a definir]**

---

## 4. Premissas Adotadas

| # | Premissa | Justificativa |
|---|---------|---------------|
| 1 | Todos os tubos identificados como Ø150mm | Diâmetros extraídos do perfil de extrusão da geometria IFC (aproximação para DN comercial) |
| 2 | Metragem de tubulação baseada em comprimento de extrusão 3D | IFC não possui propriedade "Length" populada — usado dimensão da geometria |
| 3 | Abrigos incluem apenas caixa de alumínio | Componentes internos (mangueira, esguicho) não estão modelados no IFC — precisam ser confirmados |
| 4 | Extintores PQS 4kg classe BC | Especificação extraída do ObjectType do IFC — confirmar classe (ABC vs BC) nas pranchas |
| 5 | Placa E5 de 12 metros | Informação extraída do nome do elemento IFC — confirmar significado ("12 metros" pode ser distância máxima de visualização) |
| 6 | Reservatórios e bombas não modelados | Arquivos IFC fornecidos não contêm equipamentos — podem estar em arquivo separado ou em memorial apenas |

---

## 5. Precificação

| # | Tipo de Insumo/Serviço | Fonte do Preço | Data-base | Observação |
|---|----------------------|---------------|-----------|------------|
| 1 | Tubo FG Ø6" (150mm) sch40 c/ rosca BSP | SINAPI / Cotação | [a definir] | Inclui pintura vermelha |
| 2 | Conexões FG Ø6" | SINAPI / Cotação | [a definir] | Cotovelos, tês, luvas |
| 3 | Abrigo de hidrante (caixa alumínio + kit completo) | Cotação fornecedor | [a definir] | Incluir mangueira 30m, esguicho, chave |
| 4 | Extintor PQS 4kg BC c/ suporte | SINAPI | [a definir] | |
| 5 | Extintor CO2 6kg c/ suporte | SINAPI | [a definir] | |
| 6 | Placa fotoluminescente E5 20x30cm | SINAPI | [a definir] | |
| 7 | Pintura demarcação piso (tinta acrílica) | SINAPI | [a definir] | Vermelho e branco |
| 8 | Reservatório PCI | Cotação | [a definir] | **Pendente especificação** |
| 9 | Bomba PCI (principal + reserva) | Cotação | [a definir] | **Pendente especificação** |
| 10 | Mão de obra instalação hidráulica | SINAPI | [a definir] | |

---

## 6. Pendências / Dúvidas

**Dados faltantes críticos:**

- [ ] **Metragem real de tubulação** — Os 67,26m extraídos parecem muito baixos para 34 pavimentos. Verificar pranchas DWG ou solicitar memorial.
- [ ] **Diâmetros variados** — Confirmar se toda rede é Ø150mm ou se há reduções (tês de redução indicam mudança de diâmetro).
- [ ] **Especificação completa dos abrigos** — Confirmar quantidade de mangueiras, comprimento (25m ou 30m), tipo de esguicho (regulável, agulheta).
- [ ] **Reservatórios de incêndio** — Capacidade, quantidade (inferior/superior), localização.
- [ ] **Bombas de incêndio** — Vazão, altura manométrica, potência, quantidade (principal + reserva).
- [ ] **Casa de bombas** — Dimensões, detalhamento hidráulico, quadro de comando.
- [ ] **Sistema de sprinklers** — Confirmar se NÃO existe ou se está em arquivo separado (não foi encontrado nos IFCs fornecidos).
- [ ] **Sinalização complementar** — Placas de hidrante, saída de emergência, rotas de fuga, faixas fotoluminescentes.
- [ ] **Classe dos extintores PQS** — Confirmar se são classe BC ou ABC.
- [ ] **Projeto executivo completo** — Solicitar memorial descritivo, detalhes isométricos, especificações de equipamentos.
- [ ] **Normas específicas** — Confirmar exigências do corpo de bombeiros local (projeto aprovado?).

**Arquivos adicionais necessários:**
- [ ] Memorial descritivo do sistema PCI
- [ ] Prancha de casa de bombas / reservatórios
- [ ] Especificação técnica de equipamentos (bombas, válvulas especiais)
- [ ] Projeto hidráulico detalhado (isométricos, detalhes construtivos)
- [ ] Projeto de sprinklers (se existir)

---

## 7. Mapeamento para Memorial Cartesiano

| Subsistema do Briefing | Código Memorial (N2/N3) | Observação |
|----------------------|------------------------|------------|
| Tubulação de hidrantes | 14.004.001 | Instalações Especiais > Sistema PCI > Tubulação |
| Abrigos de hidrante | 14.004.002 | Instalações Especiais > Sistema PCI > Abrigos |
| Extintores portáteis | 14.004.003 | Instalações Especiais > Sistema PCI > Extintores |
| Sinalização de emergência | 14.004.004 | Instalações Especiais > Sistema PCI > Sinalização |
| Reservatórios PCI | 14.004.005 | Instalações Especiais > Sistema PCI > Reservação |
| Bombas de incêndio | 14.004.006 | Instalações Especiais > Sistema PCI > Bombeamento |
| Casa de bombas | 14.004.007 | Instalações Especiais > Sistema PCI > Casa de Bombas |

**Referência:** Memorial Cartesiano — N1 14 Instalações Especiais

---

## 8. Histórico de Revisões

| Revisão | Data | Arquivos Recebidos | Mudanças |
|---------|------|--------------------|----------|
| R00 | 2026-03-20 | IFC PCI rev.01 Torre A e B, IFC IGC rev.01 Torre A e B, DWGs 11 pranchas | Versão inicial — extração automatizada via IFC. **ATENÇÃO:** Diversos dados faltantes (reservatórios, bombas, metragem completa). Necessário complementar com memorial descritivo e pranchas DWG. |

---

## 9. Observações Finais

### ⚠️ Limitações da Extração Automatizada

Este briefing foi gerado por **extração automatizada de arquivos IFC** fornecidos. Os seguintes problemas foram identificados:

1. **Metragem de tubulação subestimada** — Apenas 67,26m para um edifício de 34 pavimentos é claramente insuficiente. Isso indica:
   - Geometria IFC incompleta ou não padronizada
   - Tubulações podem estar modeladas como objetos genéricos (BuildingElementProxy) não processados
   - Necessário levantamento manual nas pranchas DWG

2. **Equipamentos hidromecânicos ausentes** — Reservatórios e bombas são itens de **alto impacto no custo** e não foram encontrados nos IFCs:
   - Podem estar em arquivo IFC separado (ex: "348 - EQUIPAMENTOS PCI.ifc")
   - Podem estar apenas em memorial descritivo
   - Podem estar detalhados em pranchas específicas não fornecidas

3. **Diâmetros não detalhados** — Toda tubulação foi identificada como Ø150mm, mas a presença de "tês de redução" indica variação de diâmetros não capturada.

4. **Componentes de abrigos não quantificados** — Mangueiras, esguichos, engates não estão modelados.

5. **Sprinklers não encontrados** — Se o edifício exigir sistema de sprinklers, ele NÃO está nos arquivos fornecidos.

### 📋 Próximas Etapas

1. **Validar com Leo:**
   - Existem arquivos IFC adicionais (equipamentos, sprinklers)?
   - Existe memorial descritivo do sistema PCI?
   - Projeto foi aprovado pelo corpo de bombeiros?

2. **Levantamento complementar:**
   - Analisar pranchas DWG para extrair metragens corretas
   - Identificar reservatórios e bombas nas pranchas ou memorial
   - Confirmar especificações de equipamentos

3. **Gerar planilha executiva:**
   - Após validação dos dados, gerar planilha Excel para Memorial Cartesiano
   - Incluir composições detalhadas de abrigos (kit completo)
   - Precificar equipamentos após confirmar especificações

---

*Briefing gerado por Cartesiano (subagent extração-pci-civil-electra) | Data: 2026-03-20 | Status: **PRELIMINAR — AGUARDANDO VALIDAÇÃO***
