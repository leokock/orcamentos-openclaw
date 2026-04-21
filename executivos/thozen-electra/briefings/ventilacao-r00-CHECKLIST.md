# ✅ CHECKLIST — Ventilação Mecânica Thozen Electra

**Revisão:** R00 (baseado em premissas)  
**Data:** 2026-03-20  
**Status:** ⚠️ **VALIDAÇÃO PENDENTE**

---

## 📋 FASE 1: OBTENÇÃO DE DOCUMENTAÇÃO (CRÍTICO)

### Solicitar ao Projetista (Rubens Alves)

- [ ] **Memorial descritivo do sistema** (PDF)
  - Vazões especificadas
  - Pressões de trabalho
  - Potências dos ventiladores
  - Especificação de dampers corta-fogo
  - Critérios de dimensionamento

- [ ] **Prancha de detalhes** (PDF ou DWG plotado)
  - Planta de localização de equipamentos
  - Isométrico de dutos
  - Detalhes de montagem
  - Cortes esquemáticos

- [ ] **Planilha de equipamentos** (XLSX)
  - Fabricante / modelo
  - Vazão / pressão / potência
  - Diâmetro de dutos
  - Especificação de dampers
  - Grelhas / difusores

### Validar com Arquitetura (Leo)

- [ ] **Número de escadas pressurizadas** (premissa atual: 2)
- [ ] **Existência de antecâmaras** (sim/não)
- [ ] **Localização das escadas** (quais prumadas?)
- [ ] **Espaço em casa de máquinas** (dimensões disponíveis)

---

## 📋 FASE 2: VALIDAÇÃO DE QUANTITATIVOS

### Ventiladores

- [ ] Quantidade: ____ un (premissa: 2)
- [ ] Vazão: ____ m³/h (premissa: 8.000-12.000)
- [ ] Pressão: ____ Pa (premissa: 400-600)
- [ ] Potência: ____ CV (premissa: 5-7,5)
- [ ] Fabricante: ________________
- [ ] Modelo: ________________

### Dutos

- [ ] Duto vertical — Diâmetro: ____ mm (premissa: Ø600)
- [ ] Duto vertical — Metragem: ____ m (premissa: 200)
- [ ] Duto derivação — Metragem: ____ m (premissa: 60)
- [ ] Material: ________________ (premissa: chapa galvanizada #18)
- [ ] Isolamento: ________________ (premissa: lã de vidro 50mm)

### Dampers

- [ ] Dampers corta-fogo — Quantidade: ____ (premissa: 64)
- [ ] Dampers corta-fogo — Resistência: ____ min (premissa: 90)
- [ ] Dampers motorizados — Quantidade: ____ (premissa: 4)
- [ ] Fabricante CF: ________________
- [ ] Certificação: ________________

### Grelhas e Difusores

- [ ] Grelhas de insuflamento — Quantidade: ____ (premissa: 12)
- [ ] Difusores — Quantidade: ____ (premissa: 30)
- [ ] Localização: a cada ____ pavimentos (premissa: 5)

### Sensores e Instrumentação

- [ ] Sensores de pressão — Quantidade: ____ (premissa: 4)
- [ ] Faixa de medição: ____ Pa (premissa: 0-100)

---

## 📋 FASE 3: VALIDAÇÃO ELÉTRICA E AUTOMAÇÃO

### Alimentação

- [ ] Tensão: ____ V (premissa: 220/380V trifásico)
- [ ] Potência instalada: ____ kW (calcular: 2 × 5,5 CV ≈ 8 kW)
- [ ] Alimentação por gerador? [ ] Sim [ ] Não (premissa: sim)
- [ ] Circuito exclusivo? [ ] Sim [ ] Não

### Automação

- [ ] CLP especificado? [ ] Sim [ ] Não (premissa: sim)
- [ ] Interface com central de incêndio? [ ] Sim [ ] Não (premissa: sim)
- [ ] Protocolo de comunicação: ________________ (premissa: contato seco)
- [ ] IHM especificado? [ ] Sim [ ] Não (premissa: sim)

---

## 📋 FASE 4: PRECIFICAÇÃO

### Cotações Necessárias

- [ ] **Ventiladores centrífugos** (2 un)
  - Fornecedor 1: ________________ | R$ ________
  - Fornecedor 2: ________________ | R$ ________
  - Fornecedor 3: ________________ | R$ ________

- [ ] **Dampers corta-fogo** (64 un)
  - Fornecedor 1: ________________ | R$ ________ /un
  - Fornecedor 2: ________________ | R$ ________ /un
  - Fornecedor 3: ________________ | R$ ________ /un

- [ ] **Dutos galvanizados** (260 m)
  - Fornecedor 1: ________________ | R$ ________ /m
  - Fornecedor 2: ________________ | R$ ________ /m

- [ ] **CLP + IHM**
  - Fornecedor 1: ________________ | R$ ________
  - Fornecedor 2: ________________ | R$ ________

- [ ] **Comissionamento e testes**
  - Empresa 1: ________________ | R$ ________
  - Empresa 2: ________________ | R$ ________

### Fontes de Preço

- [ ] SINAPI (mês/ano): ________
- [ ] Base Cartesian (atualização): ________
- [ ] Cotações diretas (data): ________

---

## 📋 FASE 5: REVISÃO DO BRIEFING

### Após Validar Dados

- [ ] Atualizar `ventilacao-r00.md` → criar `ventilacao-r01.md`
- [ ] Gerar relatório de diferenças: `diff-r00-r01.md`
- [ ] Atualizar estimativa de custo
- [ ] Atualizar mapeamento Memorial Cartesiano
- [ ] Marcar pendências como resolvidas

### Checklist de Qualidade

- [ ] Todos os quantitativos validados com projeto executivo
- [ ] Memorial descritivo consultado
- [ ] Premissas removidas / substituídas por dados reais
- [ ] Custo ajustado com cotações reais
- [ ] Pendências críticas resolvidas (mínimo 9/15)

---

## 📋 FASE 6: GERAÇÃO DE PLANILHA EXECUTIVA

- [ ] Estrutura conforme Memorial Cartesiano (N1 14.08)
- [ ] Códigos N2/N3 mapeados
- [ ] Quantitativos por subsistema
- [ ] Preços unitários inseridos
- [ ] BDI aplicado (25-30%)
- [ ] Contingência aplicada (15-20%)
- [ ] Totais calculados
- [ ] Revisão de QA/QC

---

## 📋 FASE 7: TESTES E COMISSIONAMENTO (PÓS-OBRA)

- [ ] Empresa de comissionamento contratada
- [ ] ART emitida
- [ ] Teste de pressão diferencial (25-50 Pa)
- [ ] Teste de vazão (velocidade < 12 m/s nas portas)
- [ ] Teste de acionamento (automático + manual)
- [ ] Teste de failsafe (falta de energia → gerador)
- [ ] Laudo técnico emitido
- [ ] Aprovação Corpo de Bombeiros

---

## 🚨 STATUS ATUAL (R00)

### ✅ Concluído
- [x] Estrutura de briefing criada
- [x] Premissas técnicas documentadas (NBR 14880)
- [x] Quantitativos estimados
- [x] Estimativa de custo (ordem de grandeza)
- [x] Pendências identificadas

### ⏳ Aguardando
- [ ] Memorial descritivo do projetista
- [ ] Prancha de detalhes
- [ ] Planilha de equipamentos
- [ ] Validação com arquitetura

### ⚠️ Bloqueadores
- Extração automática do DWG falhou (formato proprietário)
- Dados técnicos não disponíveis para validação

---

## 📊 PROGRESSO

**Fase 1:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Documentação pendente  
**Fase 2:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Validação pendente  
**Fase 3:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Validação pendente  
**Fase 4:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Precificação pendente  
**Fase 5:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Revisão pendente  
**Fase 6:** ⬜⬜⬜⬜⬜ 0/5 (0%) — Planilha não iniciada  

**TOTAL:** ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0/30 (0%)

---

## 📝 OBSERVAÇÕES

**Data de início:** 2026-03-20  
**Prazo estimado:** ________________  
**Responsável validação:** ________________  
**Última atualização:** 2026-03-20

---

*Checklist gerado por Cartesiano | Atualizar após cada validação*
