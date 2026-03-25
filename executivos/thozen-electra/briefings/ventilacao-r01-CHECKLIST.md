# CHECKLIST DE VALIDAÇÃO — VENTILAÇÃO MECÂNICA — Thozen Electra — R01

## Metadados
- **Projeto:** Thozen Electra
- **Cliente:** Thozen
- **Disciplina:** Ventilação Mecânica — Pressurização de Escadas
- **Revisão:** R01 (tentativa de extração automática)
- **Data:** 2026-03-20
- **Status:** ❌ **EXTRAÇÃO AUTOMÁTICA FALHOU**

---

## 🔴 STATUS DA EXTRAÇÃO

### Arquivo Recebido
- ✅ **Arquivo fonte:** RA_EVM_LEGAL_PROJETO_R05.dwg (5.39 MB)
- ✅ **Formato:** AutoCAD 2018/2019/2020
- ✅ **Localização:** `executivo/thozen-electra/fontes/`

### Tentativas de Extração

| # | Método | Status | Resultado |
|---|--------|--------|-----------|
| 1 | Conversão DWG → DXF (ODA File Converter) | ❌ Conversor não instalado | N/A |
| 2 | Conversão DWG → DXF (dwg2dxf) | ❌ Conversor não instalado | N/A |
| 3 | Conversão DWG → DXF (LibreCAD CLI) | ❌ Conversor não instalado | N/A |
| 4 | Extração via strings (fallback) | ❌ Texto codificado/binário | 72.678 strings, 0 relevantes |
| 5 | Busca por palavras-chave (ventilador, pressão, vazão) | ❌ Não encontrado | Arquivo binário |
| 6 | Busca por especificações numéricas (m³/h, Pa, CV) | ❌ Não encontrado | Arquivo binário |

### Conclusão
**O arquivo DWG NÃO pode ser processado automaticamente sem conversão para DXF.**

---

## 📋 CHECKLIST DE DADOS — Status de Validação

### 1. SISTEMA GERAL

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 1.1 | Número de escadas pressurizadas | 2 un | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 1.2 | Tipo de escada (PF1, PF2, PF3) | PF2 | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 1.3 | Número de pavimentos atendidos | 32 (Térreo + G1-G5 + Lazer + 24 Tipos + CM) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 1.4 | Há antecâmaras pressurizadas? | Não informado | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 1.5 | Projetista responsável | Rubens Alves | ⚠️ Não validado | 🔴 PENDENTE | Confirmar em carimbo |

### 2. VENTILADORES

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 2.1 | Quantidade de ventiladores | 2 un (1 por escada) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF/memorial |
| 2.2 | Vazão (m³/h) | 8.000-12.000 m³/h | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 2.3 | Pressão (Pa) | 400-600 Pa | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 2.4 | Potência (CV ou kW) | 5-7,5 CV | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 2.5 | Rotação (RPM) | Não informado | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 2.6 | Marca/modelo preferencial | Não informado | ⚠️ Não validado | 🔴 PENDENTE | Aguardando especificação |
| 2.7 | Localização (casa de máquinas/cobertura) | Casa de máquinas | ⚠️ Não validado | 🔴 PENDENTE | Aguardando planta |

### 3. DUTOS

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 3.1 | Metragem de dutos verticais (m) | 200 m (100m x 2 escadas) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (POLYLINEs) |
| 3.2 | Metragem de dutos horizontais/derivações (m) | 60 m | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (POLYLINEs) |
| 3.3 | Diâmetro/seção do duto principal | Ø600mm | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 3.4 | Espessura da chapa (gauge) | #18 (1,2mm) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 3.5 | Material | Aço galvanizado | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 3.6 | Isolamento térmico | Lã de vidro 50mm + alumínio | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 3.7 | Área de isolamento (m²) | 380 m² | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |

### 4. GRELHAS E DIFUSORES

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 4.1 | Grelhas de insuflamento (escada) | 12 un (6 por escada) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (blocos) |
| 4.2 | Difusores (antecâmaras) | 30 un (15 por escada) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (blocos) |
| 4.3 | Dimensões das grelhas | 600x400mm | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 4.4 | Tipo de grelha | Alumínio anodizado, regulável | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |

### 5. DAMPERS

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 5.1 | Dampers corta-fogo (un) | 64 un (32 pav x 2 escadas) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (blocos) |
| 5.2 | Resistência ao fogo | 90 minutos | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 5.3 | Dampers motorizados (sobrepressão) | 4 un (2 por escada) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (blocos) |
| 5.4 | Dampers de balanceamento | 12 un | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF (blocos) |
| 5.5 | Diâmetro/seção dos dampers | Ø600mm | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |

### 6. AUTOMAÇÃO E CONTROLE

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 6.1 | CLP (Controlador Lógico Programável) | 1 un (16 I/O) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 6.2 | Sensores de pressão diferencial | 4 un (0-100 Pa) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF/memorial |
| 6.3 | Interface com central de incêndio | Módulo de entrada (contato seco) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 6.4 | IHM (Interface Homem-Máquina) | 1 un (touch 7") | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 6.5 | Software SCADA | 1 licença | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |

### 7. INSTALAÇÕES ELÉTRICAS

| # | Item | Premissa R00 | Valor Real | Status | Fonte |
|---|------|-------------|-----------|--------|-------|
| 7.1 | Quadro de comando (QC-VENT) | 1 un (IP65) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 7.2 | Soft-starters | 2 un (7,5 CV) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |
| 7.3 | Cabo alimentação (m) | 50 m (4x6mm²) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 7.4 | Cabo de comando (m) | 250 m (2x2,5mm²) | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 7.5 | Eletrodutos (m) | 250 m (Ø1") | ⚠️ Não validado | 🔴 PENDENTE | Aguardando DXF |
| 7.6 | Botoeiras de emergência | 4 un | ⚠️ Não validado | 🔴 PENDENTE | Aguardando memorial |

---

## 🚨 BLOQUEADORES CRÍTICOS

### 1. Conversão DWG → DXF
- ❌ **Nenhum conversor disponível no sistema**
- ❌ **Arquivo DWG binário não processável via strings**
- ❌ **Bibliotecas Python (ezdxf) não lêem DWG nativo**

### 2. Alternativas para Desbloqueio

| # | Solução | Responsável | Prazo | Status |
|---|---------|-------------|-------|--------|
| A | Solicitar versão DXF ao projetista (Rubens Alves) | Time Cartesian | Imediato | 🔴 Não iniciado |
| B | Instalar ODA File Converter no sistema | DevOps/TI | 1 dia | 🔴 Não iniciado |
| C | Exportar manualmente via AutoCAD/LibreCAD | Projetista externo | 1-2 dias | 🔴 Não iniciado |
| D | Processar o DWG em máquina com AutoCAD (Windows) | Time Cartesian | 1 dia | 🔴 Não iniciado |

**Recomendação:** Solicitar a versão DXF ao projetista (solução A) — é o caminho mais rápido.

---

## 📊 ESTATÍSTICAS DE VALIDAÇÃO

### Resumo Geral
- ✅ **Dados validados:** 0 / 46 (0%)
- ⚠️ **Dados com premissa:** 46 / 46 (100%)
- 🔴 **Dados pendentes:** 46 / 46 (100%)

### Incerteza Estimada
- **Briefing R00:** ±30-50% (apenas premissas)
- **Briefing R01:** ±30-50% (extração falhou — mantém premissas)
- **Meta para R02:** ±5-10% (após DXF + memorial)

### Impacto no Orçamento
- **Custo total estimado R00:** R$ 330.000 - 520.000
- **Custo total estimado R01:** R$ 330.000 - 520.000 (sem mudança — sem dados novos)
- **Margem de contingência recomendada:** 20-25% (devido à alta incerteza)

---

## 📝 OBSERVAÇÕES FINAIS

### O que foi feito (R01)
1. ✅ Tentativa de conversão DWG → DXF (falhou — conversor não disponível)
2. ✅ Extração via strings do arquivo binário (falhou — texto codificado)
3. ✅ Busca por palavras-chave técnicas (falhou — arquivo binário)
4. ✅ Documentação completa dos bloqueadores e alternativas

### O que NÃO foi possível fazer
- ❌ Extrair quantitativos reais de dutos (POLYLINEs)
- ❌ Identificar ventiladores e especificações (blocos/textos)
- ❌ Localizar grelhas e difusores (blocos)
- ❌ Mapear dampers corta-fogo (blocos)
- ❌ Extrair memorial descritivo do projeto (se houver no DWG)

### Próximos Passos (Briefing R02)
1. 🔴 **CRÍTICO:** Obter versão DXF do arquivo RA_EVM_LEGAL_PROJETO_R05
2. 🔴 **CRÍTICO:** Obter memorial descritivo do sistema (PDF)
3. Processar DXF com ezdxf (Python)
4. Extrair quantitativos reais (dutos, equipamentos, dampers)
5. Validar especificações técnicas (vazão, pressão, potência)
6. Gerar briefing R02 com dados validados
7. Reduzir incerteza de ±30% para ±5-10%

---

## 📅 HISTÓRICO DE TENTATIVAS

| Data | Revisão | Ação | Resultado |
|------|---------|------|-----------|
| 2026-03-20 | R00 | Briefing gerado com premissas técnicas (sem DXF) | Incerteza ±30% |
| 2026-03-20 | R01 | Tentativa de extração automática do DWG | ❌ Falhou — arquivo binário |
| 2026-03-20 | R01 | Busca por conversores DWG → DXF | ❌ Nenhum instalado |
| 2026-03-20 | R01 | Extração via strings (fallback) | ❌ Texto codificado |
| 2026-03-20 | R01 | Documentação de bloqueadores e checklist | ✅ Concluído |

---

*Checklist gerado por Cartesiano (subagente) | Data: 2026-03-20*

*⚠️ STATUS: Briefing R01 BLOQUEADO — aguardando conversão DWG → DXF para prosseguir com extração de quantitativos.*
