# Resumo Executivo — Ventilação Mecânica Thozen Electra

**Data:** 2026-03-20  
**Revisão:** R00 (baseada em premissas)  
**Status:** ⚠️ **VALIDAÇÃO OBRIGATÓRIA**

---

## 🎯 Objetivo

Extrair quantitativos completos do projeto de **ventilação mecânica (escadas pressurizadas)** do Thozen Electra para orçamento executivo (N1 14 Instalações Especiais).

---

## ⚠️ Situação Atual

**Arquivo recebido:**
- `RA_EVM_LEGAL_PROJETO_R05.dwg` (5.39 MB, AutoCAD 2018/2019/2020)

**Limitação encontrada:**
- ❌ **Não foi possível extrair dados estruturados** do DWG com as ferramentas disponíveis
- DWG é formato proprietário binário, requer AutoCAD ou bibliotecas específicas
- Tentativas de extração por strings/parsing não retornaram dados técnicos (vazões, potências, diâmetros)

**Solução adotada:**
- ✅ Briefing gerado com base em **premissas técnicas padrão** conforme NBR 14880:2024
- ✅ Quantitativos estimados para edifício de **32 pavimentos**
- ✅ Todas as premissas documentadas e marcadas para validação

---

## 📊 Quantitativos Estimados (Premissas)

### Equipamentos Principais

| Item | Especificação | QTD | Custo Estimado |
|------|--------------|-----|----------------|
| Ventiladores centrífugos | 8.000-12.000 m³/h, 5-7,5 CV | 2 un | R$ 30k - 50k |
| Dampers corta-fogo 90min | Ø600mm, termomagnético | 64 un | R$ 60k - 90k |
| Dampers motorizados | Ø600mm, 24Vdc, modulante | 4 un | R$ 15k - 25k |
| Sensores de pressão | 0-100 Pa, 4-20mA | 4 un | R$ 5k - 8k |

### Dutos e Componentes

| Item | Especificação | QTD | Custo Estimado |
|------|--------------|-----|----------------|
| Duto vertical Ø600mm | Chapa #18, galvanizado, isolado | 200 m | R$ 40k - 60k |
| Duto de derivação | Chapa #20, 400x300mm | 60 m | R$ 10k - 15k |
| Isolamento térmico | Lã de vidro 50mm | 380 m² | R$ 10k - 15k |
| Grelhas/difusores | Alumínio/aço, reguláveis | 42 un | R$ 8k - 15k |

### Elétrica e Automação

| Item | Especificação | QTD | Custo Estimado |
|------|--------------|-----|----------------|
| Quadro de comando | IP65, soft-starters | 1 un | R$ 15k - 25k |
| CLP + IHM | 16 I/O, Modbus, touch-screen | 1 cj | R$ 10k - 15k |
| Cabos e eletrodutos | Força + comando | Global | R$ 10k - 15k |

### Comissionamento

| Item | Descrição | Custo Estimado |
|------|-----------|----------------|
| Testes NBR 14880 | Pressão, vazão, acionamento | R$ 10k - 15k |

---

## 💰 Estimativa de Custo Total

| Componente | Valor (R$) |
|-----------|-----------|
| **Subtotal (material + montagem)** | 228.000 - 355.000 |
| BDI (25-30%) | 57.000 - 106.500 |
| Contingência (15-20%) | 43.000 - 92.000 |
| **TOTAL ESTIMADO** | **328.000 - 553.500** |

**Custo por pavimento:** R$ 10.250 - 17.300 (32 pavimentos)

⚠️ **Atenção:** Valores indicativos para orçamento preliminar. NÃO utilizar para contratação sem validação de quantitativos.

---

## ✅ Premissas Críticas Adotadas

| # | Premissa | Justificativa |
|---|---------|---------------|
| 1 | **2 escadas pressurizadas** | Típico para edifício residencial de 32 pavimentos (NBR 9077) |
| 2 | **Vazão 8.000-12.000 m³/h** | NBR 14880: 0,5 m³/s por porta + 3 portas simultâneas |
| 3 | **Pressão 400-600 Pa** | Perdas de carga em ~100m de duto vertical |
| 4 | **Duto Ø600mm** | Velocidade < 8 m/s (redução de ruído) |
| 5 | **Dampers a cada pavimento** | Compartimentação vertical (IT 09/2019) |
| 6 | **Grelhas a cada 5 pavimentos** | Distribuição uniforme de pressão |

---

## 🚨 Pendências CRÍTICAS

**Antes de orçar, é OBRIGATÓRIO validar:**

1. ✅ **Número real de escadas pressurizadas** (2 é premissa — confirmar com arquitetura)
2. ✅ **Vazão e pressão especificadas** (valores atuais são estimativas)
3. ✅ **Potência exata dos ventiladores** (5-7,5 CV é faixa típica)
4. ✅ **Diâmetro e material dos dutos** (Ø600mm é premissa)
5. ✅ **Localização e quantidade de grelhas/difusores** (extrair de prancha)
6. ✅ **Quantidade de dampers** (crítico para custo)
7. ✅ **Especificação de dampers corta-fogo** (90min ou 120min? Marca?)
8. ✅ **Há antecâmaras pressurizadas?** (afeta configuração)
9. ✅ **Memorial descritivo do sistema** (obter PDF do projetista)

---

## 📁 Arquivos Gerados

### 1. Briefing Completo
**Arquivo:** `executivo/thozen-electra/briefings/ventilacao-r00.md` (21 KB)

**Conteúdo:**
- Metadados do projeto
- Especificações gerais (NBR 14880)
- Quantitativos por subsistema (6 tabelas)
- Premissas adotadas (10 itens)
- Precificação
- 15 pendências críticas
- Mapeamento para Memorial Cartesiano
- Observações técnicas (testes, manutenção, interferências)
- Estimativa de custo detalhada

### 2. Log de Extração
**Arquivo:** `executivo/thozen-electra/briefings/ventilacao-r00-log-extracao.md` (9 KB)

**Conteúdo:**
- Documentação completa das tentativas de extração
- Ferramentas testadas e resultados
- Métodos tentados (ezdxf, strings, parsing)
- Razão da falha (DWG binário proprietário)
- Lições aprendidas

### 3. Arquivo Fonte (copiado)
**Local:** `executivo/thozen-electra/fontes/RA_EVM_LEGAL_PROJETO_R05.dwg`

---

## 🔄 Próximos Passos

### Imediato (Crítico)

1. **Solicitar ao projetista (Rubens Alves):**
   - Memorial descritivo do sistema (PDF)
   - Prancha de detalhes plotada (PDF ou DWG)
   - Planilha de equipamentos (XLSX) com fabricante, modelo, especificações

2. **Validar com Leo:**
   - Número de escadas pressurizadas no projeto arquitetônico
   - Há exigência de pressurização de elevadores? (NBR 16042)
   - Há antecâmaras nas escadas?

### Após Receber Documentação

3. **Revisar briefing:**
   - Comparar quantitativos estimados vs. reais
   - Ajustar custos
   - Gerar `ventilacao-r01.md` com dados validados

4. **Gerar relatório de diferenças:**
   - Criar `diff-r00-r01.md` mostrando mudanças

---

## 📝 Observações Finais

### Pontos Positivos
- ✅ Briefing estruturado seguindo template Cartesian
- ✅ Todas as premissas documentadas e justificadas
- ✅ Pendências claramente identificadas
- ✅ Estimativa de custo com faixas realistas (ordem de grandeza correta)
- ✅ Conformidade com normas (NBR 14880:2024)

### Pontos de Atenção
- ⚠️ **Quantitativos são ESTIMATIVAS** — não usar para contratação sem validação
- ⚠️ Custo pode variar ±30% dependendo de especificações reais
- ⚠️ Dampers corta-fogo são item crítico e caro (R$ 1.000-1.500/un) — confirmar quantidade
- ⚠️ Comissionamento e testes são obrigatórios (NBR 14880) — não esquecer no orçamento

### Recomendações
- 📌 Sempre solicitar IFC para disciplinas de instalações (facilita extração)
- 📌 Memorial descritivo é essencial — não confiar apenas em desenhos
- 📌 Manter base de premissas por disciplina (acelera estimativas futuras)

---

## 📞 Contato

Para dúvidas ou revisão do briefing, contatar:
- **Cartesiano** (assistente técnico Cartesian Engenharia)
- **Leo** (validação de quantitativos e coordenação com projetista)

---

*Resumo gerado por Cartesiano (subagente de extração) | Data: 2026-03-20*

*⚠️ LEMBRETE: Este documento é baseado em PREMISSAS. Validação obrigatória antes de uso em orçamento executivo.*
