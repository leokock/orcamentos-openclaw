# 📁 Briefings — Thozen Electra

## Índice de Arquivos

### 💨 Ventilação Mecânica (Escadas Pressurizadas) — R05 ⚠️ PREMISSAS

#### 📄 Documentos Principais

1. **[ventilacao-r00-resumo.md](ventilacao-r00-resumo.md)** ⭐ **COMECE AQUI**
   - Resumo executivo (2 páginas)
   - Quantitativos estimados (PREMISSAS)
   - Estimativa de custo: R$ 328k - 554k
   - 9 pendências críticas

2. **[ventilacao-r00.md](ventilacao-r00.md)** 📋 BRIEFING COMPLETO
   - Especificações técnicas NBR 14880:2024
   - Quantitativos por subsistema (6 tabelas)
   - Premissas adotadas (10 itens críticos)
   - 15 pendências para validação
   - Mapeamento para Memorial Cartesiano
   - Observações técnicas (testes, manutenção)

3. **[ventilacao-r00-log-extracao.md](ventilacao-r00-log-extracao.md)** 🔧 LOG TÉCNICO
   - Documentação das tentativas de extração do DWG
   - Ferramentas testadas (ezdxf, strings, parsing)
   - Razão da falha (formato proprietário binário)
   - Lições aprendidas

#### ⚠️ ATENÇÃO CRÍTICA

**Status:** DWG não pôde ser processado automaticamente. Todos os quantitativos são **ESTIMATIVAS baseadas em premissas técnicas** (NBR 14880).

**Arquivos necessários ANTES de orçar:**
- ☐ Memorial descritivo do sistema (PDF)
- ☐ Prancha de detalhes (PDF ou DWG plotado)
- ☐ Planilha de equipamentos (XLSX)
- ☐ Confirmação de número de escadas pressurizadas
- ☐ Confirmação de antecâmaras

**NÃO utilizar para contratação sem validação!**

---

### 🔥 Prevenção e Combate a Incêndio (PCI) — R00

#### 📄 Documentos Principais

1. **[pci-civil-r00-RESUMO.md](pci-civil-r00-RESUMO.md)** ⭐ **COMECE AQUI**
   - Resumo executivo (2 páginas)
   - Quantitativos consolidados
   - Dados faltantes críticos
   - Status e recomendações

2. **[pci-civil-r00.md](pci-civil-r00.md)** 📋 BRIEFING COMPLETO
   - Especificações técnicas detalhadas
   - Quantitativos por subsistema (tabelas)
   - Premissas adotadas
   - Pendências e dúvidas
   - Mapeamento para Memorial Cartesiano

3. **[pci-civil-r00-anexo-pavimentos.md](pci-civil-r00-anexo-pavimentos.md)** 📊 DISTRIBUIÇÃO
   - Quantitativos por pavimento (Torre A e Torre B)
   - 68 pavimentos mapeados (34 × 2)
   - Padrões identificados
   - Pontos de atenção

4. **[PROXIMAS-ETAPAS.md](PROXIMAS-ETAPAS.md)** 🛠️ ROTEIRO DE TRABALHO
   - Checklist de validação de dados
   - Método de análise manual de DWGs
   - Estrutura da planilha executiva
   - Precificação e fontes de preço
   - Alertas de risco

---

## 📊 Quantitativos em Resumo

### Sistema de Hidrantes
- **Tubulação:** 67,26 m ⚠️ (valor subestimado — verificar DWGs)
- **Abrigos:** 67 un
- **Conexões:** 272 un (117 cotovelos + 151 tês + 4 luvas)

### Extintores
- **PQS 4kg:** 133 un
- **CO2 6kg:** 7 un
- **Outros:** 5 un

### Sinalização
- **Placas E5:** 140 un
- **Pintura piso:** 21 un

---

## ⚠️ Status Atual

**Revisão:** R00 (2026-03-20)  
**Origem:** Extração automatizada de IFCs (rev.01)  
**Status:** ⚠️ **PRELIMINAR — AGUARDANDO VALIDAÇÃO**

### ✅ O que foi extraído:
- Abrigos de hidrante, extintores, sinalização
- Tubulações e conexões (quantidade)
- Distribuição por pavimento

### ❌ O que está faltando (CRÍTICO):
- Reservatórios de incêndio (capacidade, localização)
- Bombas PCI (vazão, potência, pressão)
- Casa de bombas (detalhamento)
- Sistema de sprinklers (não encontrado)
- Metragem real de tubulação (DWG manual)
- Kit completo dos abrigos (mangueira, esguicho)

---

## 🚨 Próximas Ações Obrigatórias

**ANTES DE PRECIFICAR:**

1. ☐ Solicitar memorial descritivo do sistema PCI
2. ☐ Verificar se existe arquivo IFC de equipamentos separado
3. ☐ Analisar pranchas DWG manualmente (metragens, equipamentos)
4. ☐ Confirmar se projeto tem sistema de sprinklers
5. ☐ Especificar bombas e reservatórios (marca, modelo, potência, capacidade)

**RISCO:** Bombas e reservatórios representam 30-40% do custo total do sistema PCI. Orçar sem essas informações levará a **subprecificação crítica**.

---

## 📞 Contato

**Dúvidas sobre este briefing:**
- Consultar: [PROXIMAS-ETAPAS.md](PROXIMAS-ETAPAS.md)
- Equipe Cartesian Engenharia
- Gerado por: Cartesiano (assistente técnico IA)

---

## 📝 Histórico

| Data | Revisão | Mudanças |
|------|---------|----------|
| 2026-03-20 | R00 | Versão inicial — extração automatizada IFC. Dados insuficientes para orçamento completo. |

---

*Última atualização: 2026-03-20*
