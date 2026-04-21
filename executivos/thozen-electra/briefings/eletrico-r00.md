# Briefing de Orçamento Executivo - Instalações Elétricas
**Projeto:** Thozen Electra  
**Disciplina:** 09 ELÉTRICO  
**Revisão:** R00  
**Data de Extração:** 2026-03-20  
**Responsável:** Cartesiano (Bot de extração de quantitativos)

---

## 1. Resumo Executivo

Este briefing consolida os quantitativos extraídos dos **arquivos IFC** do projeto elétrico do empreendimento Thozen Electra, um edifício residencial de múltiplos pavimentos (Térreo + 31 pavimentos + Casa de Máquinas).

**Totais Extraídos dos IFCs:**
- **💡 Luminárias:** 837 unidades
- **🚰 Eletrodutos:** 18.967 trechos modelados (geometria 3D)
- **🔋 Cabos:** 1.014 trechos modelados (geometria 3D)
- **🔌 Tomadas/Pontos de Força:** Dados não disponíveis nos IFCs (ver DWGs)
- **⚡ Quadros Elétricos:** Dados não disponíveis nos IFCs (ver DWGs)

⚠️ **LIMITAÇÃO CRÍTICA:** Os arquivos IFC processados (schema IFC2X3) contêm **geometria 3D detalhada** mas **não incluem propriedades técnicas essenciais** como diâmetros de eletrodutos, bitolas de cabos, potências de luminárias, tipos de tomadas ou configuração de quadros elétricos. **Os DWGs devem ser consultados para completar o levantamento.**

---

## 2. Premissas de Orçamento

### 2.1 Fontes de Dados
- **IFCs processados:** 9 arquivos (01° Térreo até 08°~31° Tipo + Casa de Máquinas)
- **DWGs disponíveis (não processados neste levantamento):** 18 arquivos em `projetos/09 ELÉTRICO/DWG/`
- **Memoriais descritivos:** ❌ Não disponíveis na pasta do projeto
- **Pranchas técnicas:** ✅ Disponíveis nos DWGs (não extraídas)

### 2.2 Escopo do Levantamento
Este levantamento extraiu:
- ✅ **Contagem de luminárias por pavimento** (geometria 3D)
- ✅ **Metragem de eletrodutos** (quantidade de trechos — metragem linear deve ser calculada)
- ✅ **Metragem de cabos** (quantidade de trechos — metragem linear deve ser calculada)
- ❌ **Especificações técnicas** (potências, bitolas, diâmetros) — **NÃO extraídas** (exigem DWG)
- ❌ **Quadros elétricos e disjuntores** — **NÃO modelados** nos IFCs
- ❌ **Entrada de energia, transformadores, geradores** — **NÃO modelados** nos IFCs
- ❌ **Pontos de força/tomadas** — **NÃO modelados** nos IFCs (ou classificados sem identificação clara)

### 2.3 Metodologia
1. **Processamento IFC:** Script Python com `ifcopenshell` para leitura de entidades IFC2X3:
   - `IfcFlowTerminal` → luminárias, tomadas (potencial), quadros (potencial)
   - `IfcFlowSegment` → eletrodutos, cabos
2. **Consolidação por pavimento:** Cada IFC representa um pavimento/nível
3. **Classificação por keywords:** Busca em `Name` e `ObjectType` por termos-chave

---

## 3. Quantitativos Extraídos

### 3.1 Luminárias por Pavimento

| Pavimento | Luminárias (un) | Observação |
|-----------|-----------------|------------|
| 01° TÉRREO | 140 | Incluindo áreas comuns |
| 02° G1 | 77 | Garagem nível 1 |
| 03° G2 | 80 | Garagem nível 2 |
| 04° G3 | 80 | Garagem nível 3 |
| 05° G4 | 78 | Garagem nível 4 |
| 06° G5 | 97 | Garagem nível 5 |
| 07° LAZER | 119 | Pavimento de lazer |
| 08°~31° TIPO (24 pavimentos) | 166 | **Multiplicar por 24 pavimentos** |
| Casa de Máquinas | 0 | Não modeladas |
| **TOTAL** | **837 un (modelo)** | **Real ≈ 4.661 un** (837 - 166 + 166×24) |

### 3.2 Eletrodutos

| Pavimento | Trechos Modelados | Especificação | Metragem Estimada |
|-----------|-------------------|---------------|-------------------|
| 01° TÉRREO | 2.100 | PVC Corrugado (diâmetro não especificado) | A calcular* |
| 02° G1 | 1.285 | PVC Corrugado | A calcular* |
| 03° G2 | 988 | PVC Corrugado | A calcular* |
| 04° G3 | 826 | PVC Corrugado | A calcular* |
| 05° G4 | 1.028 | PVC Corrugado | A calcular* |
| 06° G5 | 1.148 | PVC Corrugado | A calcular* |
| 07° LAZER | 2.753 | PVC Corrugado | A calcular* |
| 08°~31° TIPO | 8.110 | PVC Corrugado | A calcular* (×24) |
| Casa de Máquinas | 729 | PVC Corrugado | A calcular* |
| **TOTAL** | **18.967 trechos** | **Diâmetros: consultar DWGs** | **Extrair comprimentos do IFC ou DWG** |

**\*Nota:** Cada trecho tem comprimento variável. A metragem linear total deve ser extraída lendo a propriedade `Length` de cada `IfcFlowSegment` ou medindo nos DWGs.

**Diâmetros típicos esperados (a confirmar via DWG):**
- Ø 3/4" (20mm) — circuitos de iluminação
- Ø 1" (25mm) — circuitos de força (tomadas)
- Ø 1 1/4" (32mm) — prumadas e alimentadores
- Ø 2" (50mm) ou maiores — alimentação geral, entrada

### 3.3 Cabos e Fios

| Pavimento | Trechos Modelados | Especificação | Metragem Estimada |
|-----------|-------------------|---------------|-------------------|
| 01° TÉRREO | 92 | Bitola não especificada | A calcular* |
| 02° G1 | 147 | Bitola não especificada | A calcular* |
| 03° G2 | 82 | Bitola não especificada | A calcular* |
| 04° G3 | 79 | Bitola não especificada | A calcular* |
| 05° G4 | 77 | Bitola não especificada | A calcular* |
| 06° G5 | 68 | Bitola não especificada | A calcular* |
| 07° LAZER | 51 | Bitola não especificada | A calcular* |
| 08°~31° TIPO | 388 | Bitola não especificada | A calcular* (×24) |
| Casa de Máquinas | 30 | Bitola não especificada | A calcular* |
| **TOTAL** | **1.014 trechos** | **Bitolas: consultar DWGs/memorial** | **Extrair comprimentos do IFC ou DWG** |

**Bitolas típicas esperadas (a confirmar via DWG ou memorial):**
- **Iluminação:** 1,5mm² (predominante) / 2,5mm² (circuitos mais carregados)
- **Tomadas de uso geral:** 2,5mm²
- **Tomadas de uso específico:** 4mm² ou 6mm² (dependendo da potência)
- **Alimentadores/prumadas:** 10mm², 16mm², 25mm², 35mm², 50mm² ou maiores
- **Entrada de energia:** Cabos de média tensão (se aplicável) — especificação no projeto de entrada

### 3.4 Quadros Elétricos

❌ **DADOS NÃO DISPONÍVEIS NOS IFCs PROCESSADOS**

Os quadros elétricos não foram modelados como entidades identificáveis no IFC2X3. **Consultar DWGs para:**
- Quantidade e localização de quadros por pavimento
- Tipo de quadro (QD, QDL, QDF, QGBT, QGE, etc.)
- Número e especificação de disjuntores (amperagem, curva, n° polos)
- Dimensões e potências instaladas

**Estimativa preliminar (a validar via DWG):**
- **Pavimento tipo:** 1 QD por apartamento + QDL comum
- **Garagens:** QDL por nível + quadros de bombas/ventilação
- **Térreo/Lazer:** QD áreas comuns + QDL piscina/sauna + QDF portaria
- **Casa de Máquinas:** QGBT + painéis de automação elevadores/pressurização

### 3.5 Pontos de Força (Tomadas)

❌ **DADOS NÃO DISPONÍVEIS NOS IFCs PROCESSADOS**

Tomadas não foram modeladas ou não foram classificadas como `IfcFlowTerminal` identificável. **Consultar DWGs para:**
- Quantidade de pontos de força por pavimento e ambiente
- Tipo de tomada (TUG — uso geral, TUE — uso específico)
- Potência e circuito associado
- Altura de instalação

**Estimativa preliminar (baseada em tipologia residencial padrão):**
- **Apartamento tipo:** 20~30 pontos de força/apartamento
- **Garagens:** Tomadas de serviço e recarga (se houver)
- **Áreas comuns:** Pontos de força para limpeza, manutenção, equipamentos

### 3.6 Entrada de Energia e Infraestrutura Geral

❌ **DADOS NÃO DISPONÍVEIS NOS IFCs PROCESSADOS**

**Consultar DWGs e/ou memorial descritivo para:**
- **Padrão de entrada:** Aéreo ou subterrâneo / BT ou MT
- **Transformador:** Potência (kVA), tipo (seco/óleo), localização
- **Gerador de emergência:** Potência (kVA), tipo (diesel/gás), localização, tanque de combustível
- **SPDA (Para-raios):** Sistema de proteção contra descargas atmosféricas
- **Aterramen to:** Hastes, malha, especificação
- **Infraestrutura de dados/telefonia:** Eletrodutos exclusivos, racks, fibra óptica (se incluído no projeto elétrico)

---

## 4. Fontes Consultadas

### Arquivos Processados (IFCs)

| Arquivo | Pavimento | Status |
|---------|-----------|--------|
| `348 - E01 [09] - rev.01 - EL_R.Rubens Alves - 01° PAVTO. TÉRREO.ifc` | Térreo | ✅ Processado |
| `348 - E02 [09] - rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1.ifc` | Garagem 1 | ✅ Processado |
| `348 - E03 [09] - rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2.ifc` | Garagem 2 | ✅ Processado |
| `348 - E04 [09] - rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3.ifc` | Garagem 3 | ✅ Processado |
| `348 - E05 [09] - rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4.ifc` | Garagem 4 | ✅ Processado |
| `348 - E06 [09] - rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5.ifc` | Garagem 5 | ✅ Processado |
| `348 - E07 [09] - rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER.ifc` | Lazer | ✅ Processado |
| `348 - E08 [09] - rev.01 - EL_R.Rubens Alves - 08°~31° PAVTO. TIPO (24x).ifc` | Tipo (×24) | ✅ Processado |
| `348 - E09 [09] - rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS.ifc` | Casa Máq. | ✅ Processado |

### Arquivos Disponíveis Não Processados (DWGs)

18 arquivos DWG disponíveis em `projetos/09 ELÉTRICO/DWG/` — **não processados neste levantamento**. Recomenda-se processamento futuro para:
- Extrair especificações técnicas (bitolas, diâmetros, potências)
- Identificar quadros elétricos e diagramas unifilares
- Validar quantitativos de tomadas e pontos de força
- Extrair legendas e notas técnicas

---

## 5. Observações e Recomendações

### 5.1 Limitações do Levantamento Atual

1. **IFCs incompletos tecnicamente:**
   - Schema IFC2X3 (antigo) — sem propriedades elétricas avançadas
   - Geometria 3D detalhada, mas sem `IfcPropertySet` com dados técnicos
   - Tomadas e quadros não modelados ou não identificáveis

2. **Dados faltantes críticos para orçamento:**
   - ❌ Diâmetros de eletrodutos (necessário para precificação)
   - ❌ Bitolas de cabos (necessário para precificação)
   - ❌ Potências e tipos de luminárias (LED? Fluorescente? Halogêneo?)
   - ❌ Quantidade de disjuntores e especificação de quadros
   - ❌ Entrada de energia e transformação (BT/MT)
   - ❌ Gerador de emergência

3. **Metragens lineares não calculadas:**
   - Os IFCs contêm a geometria 3D de cada trecho de eletroduto/cabo
   - É possível extrair comprimentos lendo a propriedade `Length` de cada segmento
   - Recomenda-se script adicional para totalizar metragens por diâmetro/bitola

### 5.2 Próximos Passos Recomendados

#### Prioridade ALTA (Necessário para orçamento executivo)
1. **Processar DWGs** para extrair:
   - Legendas com especificações técnicas
   - Diagramas unifilares dos quadros elétricos
   - Tabelas de cargas e dimensionamentos
   - Detalhes de entrada de energia e gerador
   - Prumadas e alimentadores principais

2. **Obter memorial descritivo** do projeto elétrico (PDF) para:
   - Confirmar premissas de cálculo
   - Validar especificações de materiais
   - Identificar normas aplicadas (NBR 5410, etc.)

3. **Calcular metragens lineares** dos IFCs:
   - Iterar sobre `IfcFlowSegment` e somar `Length` por tipo
   - Separar eletrodutos por diâmetro (se identificável via propriedades)
   - Separar cabos por bitola (se identificável via propriedades)

#### Prioridade MÉDIA (Refinamento do orçamento)
4. **Validar quantitativos de luminárias** via DWGs:
   - Confirmar potências e tipos (LED, fluorescente, etc.)
   - Verificar altura de instalação (teto/parede/piso)
   - Identificar luminárias de emergência

5. **Extrair pontos de força** via DWGs:
   - Contar TUGs e TUEs por pavimento
   - Identificar circuitos dedicados (ar-condicionado, chuveiro, etc.)

#### Prioridade BAIXA (Detalhamento pós-orçamento)
6. **Extrair coordenadas 3D** para BIM 5D (se necessário):
   - Posicionamento de luminárias para mapa de iluminação
   - Traçado de eletrodutos para clash detection
   - Integração com modelo arquitetônico

---

## 6. Estrutura de Dados para Planilha de Orçamento

### Macrogrupo N1 07 — Instalações Elétricas

#### N2 07.01 — Entrada de Energia
- Padrão de entrada (aéreo/subterrâneo)
- Transformador (se MT)
- Cabine primária
- Medição

#### N2 07.02 — Quadros Elétricos e Distribuição
- QGBT (Quadro Geral de Baixa Tensão)
- QD (Quadros de Distribuição) por pavimento
- QDL (Quadros de Luz) áreas comuns
- Disjuntores (por tipo e amperagem)

#### N2 07.03 — Circuitos de Iluminação
- Luminárias (LED, fluorescente, etc.) por tipo
- Eletrodutos para iluminação (Ø 3/4" ou menor)
- Cabos 1,5mm² e 2,5mm² para iluminação
- Interruptores e dimmers

#### N2 07.04 — Circuitos de Força (Tomadas)
- TUGs (Tomadas de Uso Geral) — 2,5mm²
- TUEs (Tomadas de Uso Específico) — 4mm² ou maior
- Eletrodutos para força (Ø 1" ou maior)
- Caixas de passagem e conduítes

#### N2 07.05 — Alimentadores e Prumadas
- Cabos alimentadores principais (10mm² a 50mm²)
- Eletrodutos de grande diâmetro (2" ou maior)
- Barramento blindado (se houver)

#### N2 07.06 — Gerador de Emergência (se aplicável)
- Grupo gerador (kVA)
- Tanque de combustível
- QTA (Quadro de Transferência Automática)
- Eletrodutos e cabos dedicados

#### N2 07.07 — SPDA e Aterramento
- Para-raios (tipo Franklin, gaiola de Faraday, etc.)
- Descidas e captores
- Malha de aterramento
- Hastes de aterramento

#### N2 07.08 — Infraestrutura de Dados/Telefonia (se incluído)
- Eletrodutos exclusivos para cabeamento estruturado
- Caixas de passagem de dados
- Racks e patch panels (se no escopo elétrico)

---

## 7. Resumo de Pendências

| Item | Status | Ação Necessária |
|------|--------|-----------------|
| Diâmetros de eletrodutos | ❌ Faltante | Extrair dos DWGs (legenda) |
| Bitolas de cabos | ❌ Faltante | Extrair dos DWGs (legenda) ou memorial |
| Metragens lineares (eletrodutos) | ⚠️ Parcial | Calcular via script IFC ou medir DWGs |
| Metragens lineares (cabos) | ⚠️ Parcial | Calcular via script IFC ou medir DWGs |
| Potências de luminárias | ❌ Faltante | Extrair dos DWGs (legenda) |
| Quadros elétricos (quantidade) | ❌ Faltante | Contar nos DWGs + ler diagramas unifilares |
| Disjuntores (quantidade/tipo) | ❌ Faltante | Ler diagramas unifilares nos DWGs |
| Pontos de força/tomadas | ❌ Faltante | Contar nos DWGs |
| Entrada de energia (especificação) | ❌ Faltante | Consultar memorial ou prancha de entrada |
| Gerador (especificação) | ❌ Faltante | Consultar memorial ou prancha específica |
| SPDA (detalhes) | ❌ Faltante | Consultar memorial ou prancha específica |
| Interruptores | ❌ Faltante | Contar nos DWGs |

---

## 8. Contato e Próximos Passos

**Responsável pela extração:** Cartesiano (Bot)  
**Data:** 2026-03-20  
**Revisão:** R00  

**Próximo passo imediato:**  
Processar os **18 arquivos DWG** disponíveis para extrair as especificações técnicas faltantes e gerar o **briefing R01 (completo)**.

**Arquivos de entrada para R01:**
- `projetos/09 ELÉTRICO/DWG/*.dwg` (18 arquivos)
- Memorial descritivo (se disponível)

**Saída esperada R01:**
- Planilha de quantitativos completa (Excel)
- Briefing atualizado com todas as especificações
- Mapeamento de cada item aos códigos do Memorial Cartesiano (N1 07.xx.xxx)

---

**Fim do Briefing R00**
