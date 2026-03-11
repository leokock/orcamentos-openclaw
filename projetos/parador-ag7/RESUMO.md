# Orçamento Executivo — Parador AG7 (R01)

**Data da extração:** 11/03/2026 06:36 BRT  
**Fonte:** `CTN-AG7_PRD - Orçamento Executivo_R01.xlsx` (Google Drive AG7)

---

## 💰 Resumo Financeiro

| Métrica | Valor |
|---------|-------|
| **Valor Total da Obra** | **R$ 165.636.402,99** |
| **Total de Items** | 251 serviços |
| **Versão** | R01 |

---

## 🔝 Top 10 Itens Mais Caros

1. **Taxa de Administração** — R$ 19.406.743,70
2. **Mobiliário e decoração** — R$ 14.073.380,30
3. **Esquadrias de Alumínio** (fornecimento + instalação) — R$ 9.689.331,96
4. **Mão de obra supraestrutura** — R$ 7.393.300,60
5. **Paisagismo** — R$ 7.393.300,60
6. **Textura Signature Fine Sto** (parede externa) — R$ 5.739.266,09
7. **Concreto Usinado FCK 45MPa** (bombeável supraest.) — R$ 4.788.691,06
8. **Revestimento Madeira Quaruba Atelier** (piso) — R$ 4.367.112,75
9. **Concreto Usinado 45MPa** (infraestrutura) — R$ 3.499.451,49
10. **Mão de obra fundação** — R$ 3.209.110,36

---

## 📊 Composição do Orçamento

Todos os 251 items foram classificados como **SERVIÇO**.

**Macrogrupos principais identificados:**
- Movimentação de Terra
- Fundação
- Estrutura (supra + infra)
- Esquadrias
- Revestimentos
- Instalações
- Acabamentos
- Paisagismo
- Administração

---

## 📁 Arquivos Gerados

### Orçamento Principal
- `ger-executivo.json` (103.6 KB) — Orçamento consolidado com hierarquia completa

### Quantitativos Complementares (extraídos de planilhas Visus)
- `quantitativos/arq-visus1.json` (38 KB)
- `quantitativos/arq-visus2.json` (101 KB)
- `memoriais/arquitetura.md` (9.1 KB)

---

## 🏗️ Estrutura de Dados (ger-executivo.json)

Cada item contém:
- `celula`, `etapa`, `subetapa`, `servico` (níveis hierárquicos)
- `macrogrupo` (categoria principal)
- `tipo` (SERVIÇO, ETAPA, etc)
- `codigo` (código do item)
- `descricao` (nome do serviço)
- `unidade` (M2, M3, UN, etc)
- `quantidade`, `preco_unitario`, `preco_total`
- `observacoes`, `status` (Finalizado, Em andamento, etc)

---

## 🎯 Próximos Passos Sugeridos

1. **Validar valor total** — R$ 165,6M está correto vs expectativa?
2. **Analisar distribuição** — Administração (11,7% do total) está dentro do padrão?
3. **Revisar top items** — Mobiliário (R$ 14M) e Esquadrias (R$ 9,7M) estão dimensionados?
4. **Processar disciplinas específicas** — Elétrico, Hidrossanitário, Climatização (se necessário)
5. **Gerar cronograma** — Vincular orçamento a planejamento físico-financeiro

---

_Processado via OpenClaw | Jarvis_
