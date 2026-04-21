# 🔥 RESUMO EXECUTIVO — PCI Thozen Electra — R00

**Data:** 2026-03-20  
**Status:** ⚠️ **PRELIMINAR — AGUARDANDO VALIDAÇÃO E DADOS COMPLEMENTARES**

---

## 📊 Quantitativos Consolidados (Torre A + Torre B)

### Sistema de Hidrantes

| Item | QTD | UN | Observação |
|------|-----|-----|------------|
| Tubulação FG vermelho Ø150mm (6") | 67,26 | m | ⚠️ **VALOR SUBESTIMADO** — Verificar pranchas DWG |
| Abrigos de hidrante (caixa alumínio) | 67 | un | Kit completo: mangueira + esguicho + chave |
| Cotovelo 90° FG Ø150mm | 117 | un | |
| Tê de redução FG | 151 | un | Diâmetros variados (a confirmar) |
| Luva FG | 4 | un | |
| Válvula/Registro Ø1/2" | 127 | un | |
| Válvula de retenção | 11 | un | |

### Sistema de Extintores

| Item | QTD | UN | Observação |
|------|-----|-----|------------|
| Extintor PQS 4kg classe BC | 133 | un | Confirmar se é BC ou ABC |
| Extintor CO2 6kg | 7 | un | Concentrados em Casa de Máquinas |
| Extintor (tipo não especificado) | 5 | un | A identificar nas pranchas |
| Suporte de parede p/ extintor | 135 | un | |

### Sinalização de Emergência

| Item | QTD | UN | Observação |
|------|-----|-----|------------|
| Placa E5 fotoluminescente (12m) | 140 | un | 20x30cm, "Extintor de incêndio" |
| Pintura de piso 85x85cm | 21 | un | Demarcação de extintor |

---

## ⚠️ DADOS CRÍTICOS FALTANTES

### Equipamentos Hidromecânicos (NÃO ENCONTRADOS)

| Item | Status |
|------|--------|
| Reservatório(s) de incêndio | ❌ Não identificado — capacidade, quantidade, localização |
| Bomba principal PCI | ❌ Não identificado — vazão, potência, altura manométrica |
| Bomba reserva (jockey) | ❌ Não identificado |
| Casa de bombas | ❌ Detalhamento não encontrado |
| Quadro de comando | ❌ Não especificado |
| Tubulação de sucção/recalque | ❌ Não quantificada |

### Outras Pendências

| Item | Status |
|------|--------|
| Sistema de sprinklers | ❌ Não encontrado nos IFCs fornecidos — confirmar se existe |
| Metragem real de tubulação | ⚠️ 67,26m parece muito baixo para 34 pavimentos |
| Diâmetros variados | ⚠️ Tês de redução indicam mudança de Ø — confirmar dimensões |
| Kit completo dos abrigos | ⚠️ Mangueira (25m ou 30m?), esguicho regulável, engates — não modelados |
| Sinalização complementar | ⚠️ Placas de hidrante, saída, rota de fuga — não quantificadas |

---

## 📁 Arquivos Processados

**IFCs extraídos (rev.01):**
- `348 - PCI - rev.01 - ELECTRA TOWERS - TORRE A.ifc` (24 MB, 218 trechos de tubo)
- `348 - PCI - rev.01 - ELECTRA TOWERS - TORRE B.ifc` (23 MB, 206 trechos de tubo)
- `348 - IGC - rev.01 - ELECTRA TOWERS - TORRE A.ifc` (37 MB, só gás, sem PCI)
- `348 - IGC - rev.01 -ELECTRA TOWERS - TORRE B.ifc` (42 MB, só gás, sem PCI)

**DWGs disponíveis (NÃO PROCESSADOS):**
- 11 pranchas (rev.00 e rev-00) — análise manual necessária

---

## 🚨 Próximas Etapas Obrigatórias

### 1. Validar com Leo/Cliente

- [ ] Existem arquivos IFC adicionais? (equipamentos, sprinklers)
- [ ] Existe memorial descritivo do sistema PCI?
- [ ] Projeto foi aprovado pelo corpo de bombeiros?
- [ ] Pranchas de casa de bombas / reservatórios disponíveis?

### 2. Levantamento Complementar

- [ ] Analisar DWGs manualmente para extrair metragens corretas
- [ ] Identificar reservatórios e bombas (memorial ou pranchas)
- [ ] Confirmar especificação de equipamentos hidromecânicos
- [ ] Verificar existência de sistema de sprinklers

### 3. Geração de Planilha Executiva

- [ ] Após validação, gerar Excel para Memorial Cartesiano (N1 14 Instalações Especiais)
- [ ] Incluir composições completas de abrigos
- [ ] Precificar equipamentos após confirmar specs

---

## 📂 Arquivos Gerados

1. **`pci-civil-r00.md`** — Briefing completo com especificações, quantitativos, premissas, pendências
2. **`pci-civil-r00-anexo-pavimentos.md`** — Distribuição detalhada de equipamentos por pavimento (Torre A e Torre B)
3. **`pci-civil-r00-RESUMO.md`** — Este arquivo (resumo executivo)

---

## 💡 Observações Técnicas

### Limitações da Extração Automatizada

- **Metragem de tubulação:** Apenas 67m para 34 pavimentos é claramente insuficiente → geometria IFC incompleta ou tubulações modeladas como elementos genéricos
- **Equipamentos ausentes:** Reservatórios e bombas são itens de **ALTO IMPACTO no custo** e não foram encontrados — podem estar em arquivo IFC separado ou apenas em memorial
- **Diâmetros não detalhados:** Toda tubulação foi identificada como Ø150mm, mas tês de redução indicam variação não capturada
- **Componentes de abrigos:** Mangueiras, esguichos, engates não estão modelados — adotar kit padrão NBR 13714

### Padrão Identificado

**Pavimento Tipo (8° ao 31°):**
- 1 abrigo de hidrante
- 2 extintores PQS 4kg
- 2 placas E5 fotoluminescentes

**Total de 24 pavimentos tipo × 2 torres = 48 pavimentos repetidos**

---

## 🎯 Recomendação

**NÃO AVANÇAR para precificação antes de:**
1. Confirmar metragens reais de tubulação (análise DWG ou memorial)
2. Identificar e especificar equipamentos hidromecânicos (bombas, reservatórios)
3. Confirmar se existe sistema de sprinklers (não encontrado nos IFCs)

**Risco financeiro:** Reservatórios e bombas de incêndio podem representar 30-40% do custo total do sistema PCI. Orçar sem essas informações levará a subprecificação crítica.

---

*Briefing gerado por Cartesiano (extração automatizada IFC) | Validação pendente | 2026-03-20*
