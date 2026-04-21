# ✅ Checklist de Validação - PCI Elétrico Thozen Electra

**Revisão:** R00  
**Data:** 20/03/2026

---

## 📋 ANTES DE ORÇAR — AÇÕES OBRIGATÓRIAS

### 🔴 CRÍTICO — Bloqueante para orçamento executivo

- [ ] **Conferir pranchas DWG** — abrir arquivos e verificar:
  - [ ] Tabelas de quantitativos nas pranchas
  - [ ] Legendas com especificações de cabos (bitola, tipo)
  - [ ] Legendas com especificações de eletrodutos (⌀, material)
  - [ ] Diagramas unifilares das centrais
  - [ ] Detalhes de instalação

- [ ] **Validar quantidade de quadros de comando**
  - [ ] IFC extraiu 1.189 quadros (ERRADO — provável erro de modelagem)
  - [ ] Estimar realista: 40-50 quadros (1-2 por pavimento)
  - [ ] Conferir nas pranchas qual a quantidade real
  - [ ] Atualizar briefing com valor correto

- [ ] **Solicitar memorial descritivo do sistema PCI**
  - [ ] Especificações técnicas completas
  - [ ] Marca/modelo dos equipamentos
  - [ ] Topologia do sistema (loops, zonas)
  - [ ] Dimensionamento de baterias
  - [ ] Interfaces com outros sistemas

---

### 🟡 IMPORTANTE — Impacta precisão do orçamento

- [ ] **Cabos — especificações e metragens**
  - [ ] Cabo de sinal (PP 2×2,5mm² ou similar) — metragem total
  - [ ] Cabo de alimentação avisadores — metragem total
  - [ ] Cabo de alimentação central — metragem, bitola
  - [ ] Verificar se projeto especifica marca (Pirelli, Corfio, etc.)

- [ ] **Eletrodutos — diâmetros e metragens**
  - [ ] Eletroduto PVC ⌀20mm — metragem
  - [ ] Eletroduto PVC ⌀25mm — metragem
  - [ ] Eletroduto metálico ⌀20mm — metragem
  - [ ] Eletroduto metálico ⌀25mm — metragem
  - [ ] Confirmar material especificado (PVC, metálico galvanizado)

- [ ] **Marca/modelo dos equipamentos**
  - [ ] Central de alarme — marca/modelo (ex: Intelbras AMT 8000, Notifier NFS2-640)
  - [ ] Detectores de fumaça — marca/modelo (ex: Intelbras DFO 420, Notifier FST-851)
  - [ ] Acionadores manuais — marca/modelo
  - [ ] Avisadores audiovisuais — marca/modelo
  - [ ] Confirmar se é linha residencial ou comercial/industrial

---

### 🟢 DESEJÁVEL — Refinamento do orçamento

- [ ] **Interfaces com outros sistemas**
  - [ ] BMS/Automação — módulos necessários
  - [ ] Elevadores — recall automático
  - [ ] Controle de acesso — desbloqueio emergência
  - [ ] CFTV — integração (se aplicável)
  - [ ] Ventilação/exaustão garagem — acionamento

- [ ] **Acessórios e componentes**
  - [ ] Caixas de passagem 4×2" — quantidade
  - [ ] Caixas de passagem 4×4" — quantidade
  - [ ] Terminais de linha (EOL) — quantidade
  - [ ] Isoladores de curto-circuito — quantidade
  - [ ] Módulos relé de interface — quantidade

- [ ] **Mão de obra e serviços**
  - [ ] Projeto executivo/detalhamento — incluir?
  - [ ] ART/TRT do projeto — incluir?
  - [ ] Comissionamento do sistema — incluir?
  - [ ] Treinamento operação — incluir?
  - [ ] Manual as-built — incluir?

---

## 📊 VALIDAÇÃO DOS DADOS EXTRAÍDOS

### Equipamentos de Detecção

- [ ] **494 detectores de fumaça ópticos**
  - [ ] Conferir distribuição por pavimento (ver tabela briefing)
  - [ ] Validar se cobertura atende NBR 17240
  - [ ] Confirmar se são todos ópticos (não há termovelocimétricos)

### Equipamentos de Acionamento

- [ ] **72 acionadores manuais**
  - [ ] Conferir distribuição por pavimento
  - [ ] Validar distância máxima 30m (NBR 17240)
  - [ ] Confirmar se estão em rotas de fuga

### Equipamentos de Sinalização

- [ ] **102 avisadores audiovisuais**
  - [ ] Conferir distribuição por pavimento
  - [ ] Validar cobertura sonora (15dB acima ruído ambiente)
  - [ ] Confirmar se são audiovisuais (não apenas sonoros)

### Centrais e Quadros

- [ ] **3 centrais de alarme**
  - [ ] Confirmar capacidade (mín. 500 pontos cada)
  - [ ] Validar topologia (1 principal + 2 redundantes?)
  - [ ] Conferir dimensionamento de baterias (24h + 15min)

- [ ] **40-50 quadros de comando** (estimativa)
  - [ ] ⚠️ **VALIDAR URGENTE** — IFC extraiu 1.189 (erro!)
  - [ ] Conferir pranchas DWG
  - [ ] Atualizar briefing com valor correto

---

## 🏗️ DADOS COMPLEMENTARES

### Área Construída
- [ ] Confirmar área total construída (necessário para R$/m²)
- [ ] Confirmar área por pavimento
- [ ] Área estimada: ~18.000 m² (assumido 550m²/pav × 33)

### Pé-direito
- [ ] Confirmar pé-direito dos pavimentos
  - [ ] Garagens: ___ m
  - [ ] Tipo: ___ m
  - [ ] Lazer: ___ m
- [ ] Impacta comprimento de prumadas verticais

### Compartimentação
- [ ] Verificar se há compartimentação corta-fogo
- [ ] Confirmar se detectores atendem áreas compartimentadas
- [ ] Validar cobertura de avisadores em áreas isoladas

---

## 📁 DOCUMENTAÇÃO NECESSÁRIA

### Do Projetista
- [ ] Memorial descritivo do sistema PCI
- [ ] Planilha de quantitativos (se disponível)
- [ ] Especificação técnica de equipamentos
- [ ] ART do projeto

### Das Pranchas DWG
- [ ] Lista de pranchas disponíveis:
  - [ ] 18 pranchas DWG (Torre A + Torre B)
  - [ ] Organizar por: Planta baixa, Unifilar, Detalhes
- [ ] Extrair tabelas e legendas
- [ ] Capturar esquemas unifilares

### Do Cliente/Construtora
- [ ] Cronograma de obra (impacta prazo fornecimento)
- [ ] Interfaces com outros projetos (elétrico, automação, etc.)
- [ ] Requisitos de marca/fornecedor
- [ ] Prazo para entrega do orçamento

---

## 💰 ORÇAMENTO — DEFINIÇÕES

### Escopo do Orçamento
- [ ] **Fornecimento:** Equipamentos + materiais
- [ ] **Instalação:** Mão de obra executiva
- [ ] **Projeto:** Detalhamento executivo (se necessário)
- [ ] **Comissionamento:** Testes e ajustes finais
- [ ] **Treinamento:** Operação do sistema
- [ ] **Garantia:** Período e termos

### Premissas de Custo
- [ ] Definir índice R$/m² de referência (base Cartesian)
- [ ] Confirmar se BDI está incluso
- [ ] Definir prazo de validade da proposta
- [ ] Definir forma de reajuste (se aplicável)

### Composição de Preços
- [ ] Equipamentos: marca definida ou equivalente?
- [ ] Cabos: marca especificada ou padrão NBR?
- [ ] Mão de obra: própria ou terceirizada?
- [ ] Impostos: regime tributário (Simples, LP, etc.)

---

## ⚠️ RISCOS IDENTIFICADOS

### Riscos Técnicos
- [ ] **ALTO:** Quadros superestimados (1.189 vs. real 40-50)
  - **Ação:** Conferir pranchas antes de orçar
  - **Impacto:** Distorção de ~2.400% no custo de quadros

- [ ] **ALTO:** Cabos/eletrodutos não quantificados
  - **Ação:** Extrair das pranchas ou usar índice paramétrico
  - **Impacto:** ~40-50% do custo total do sistema

- [ ] **MÉDIO:** Especificação de marca não definida
  - **Ação:** Definir com cliente ou adotar padrão mercado
  - **Impacto:** Variação de 30-50% entre marcas

### Riscos de Prazo
- [ ] Fornecimento de equipamentos (lead time 30-60 dias)
- [ ] Interfaces com outros sistemas (depende cronograma)
- [ ] Comissionamento (depende conclusão obras civis)

### Riscos Comerciais
- [ ] Variação cambial (equipamentos importados)
- [ ] Reajuste de materiais (cobre, PVC)
- [ ] Disponibilidade de estoque (centrais específicas)

---

## ✅ APROVAÇÃO FINAL

Antes de gerar orçamento executivo, conferir:

- [ ] **Briefing validado** — dados conferidos e atualizados
- [ ] **Quantitativos completos** — sem estimativas críticas pendentes
- [ ] **Especificações definidas** — marca/modelo confirmados
- [ ] **Escopo alinhado** — cliente ciente de inclusões/exclusões
- [ ] **Prazo acordado** — cronograma compatível com obra

---

## 📝 OBSERVAÇÕES

**Espaço para anotações durante validação:**

```
___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________

___________________________________________________________________________
```

---

**Responsável pela validação:** _____________________  
**Data:** ___/___/______  
**Assinatura:** _____________________

---

## 📎 ANEXOS

1. **Briefing principal:** `pci-eletrico-r00.md`
2. **Análise técnica:** `pci-eletrico-r00-analise.md`
3. **Quantitativos CSV:** `pci-eletrico-r00-quantitativos.csv`
4. **Resumo visual:** `pci-eletrico-r00-RESUMO.txt`
5. **Arquivos IFC processados:** `projetos/thozen-electra/projetos/08 PREVENTIVO INCENDIO ELÉTRICO/IFC/`
6. **Arquivos DWG disponíveis:** `projetos/thozen-electra/projetos/08 PREVENTIVO INCENDIO ELÉTRICO/DWG/`
