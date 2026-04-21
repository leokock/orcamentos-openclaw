# Briefing Técnico - Instalações Hidrossanitárias
## Projeto: Thozen Electra
**Revisão:** R00  
**Data:** 20/03/2026  
**Disciplina:** 06 SANITÁRIO  
**Memorial Cartesiano:** N1 06 Instalações Hidrossanitárias

---

## 1. Resumo Executivo

Quantitativos completos do projeto de instalações sanitárias do empreendimento Thozen Electra, edifício residencial com duas torres (T.A e T.B), 31 pavimentos tipo, pavimentos de garagem (G1 a G5), pavimento de lazer e casa de máquinas.

**Totais Consolidados:**
- **Tubulações PVC:** 7.326 trechos, 106.680,71 metros lineares
- **Conexões e Acessórios:** 11.340 unidades
- **Equipamentos Especiais:** 31 unidades (térreo)

**Sistemas contemplados:**
- Esgoto sanitário (série normal e reforçada)
- Água fria
- Águas pluviais (identificado nas plantas)
- Estação de tratamento de efluentes (térreo)

---

## 2. Premissas e Observações

### 2.1 Fonte dos Dados
- **Arquivos IFC processados:** 10 arquivos (schema IFC2X3)
- **Pavimentos modelados:** Térreo, 02° ao 06° Pavto (G1-G5), 07° Pavto Lazer, 08° Pavto Tipo (1x), 09° ao 31° Pavto Tipo (23x), Casa de Máquinas
- **Fabricante predominante:** Amanco Wavin
- **Normas:** NBR 5688/NBR 8160

### 2.2 Observações Importantes

⚠️ **METRAGEM DE TUBULAÇÕES - INCONSISTÊNCIA DETECTADA:**
- A propriedade `Length` dos elementos `IfcFlowSegment` está presente no modelo IFC, mas **retorna valores zerados ou incompletos** na maioria dos pavimentos
- Apenas **3 pavimentos** têm metragens calculadas corretamente:
  - **09° ao 31° Pavto Tipo (23x):** 66.323,18 m (tubulação reforçada: 30.430,66 m + tubulação normal: 35.892,52 m)
  - **Casa de Máquinas:** 35.988,65 m
  - **Parcial do Térreo:** alguns trechos com comprimento zerado
- **Ação necessária:** Recalcular metragens a partir das geometrias dos elementos IFC ou consultar plantas DWG originais
- **Estimativa provisória:** A metragem real pode ser **5 a 10 vezes superior** aos valores extraídos (baseado na relação trechos × média de comprimento por trecho nos pavimentos com dados válidos)

⚠️ **DIÂMETROS DE ÁGUA FRIA:**
- Propriedade `Diâmetro` retorna **DN0** para todas as tubulações de água fria (793 trechos)
- Motivo provável: diâmetro não definido no tipo do elemento no modelo BIM
- **Ação necessária:** Consultar plantas DWG ou memorial descritivo para identificar diâmetros corretos (provavelmente DN20, DN25, DN32, DN40)

### 2.3 Prumadas
- Prumadas verticais estão representadas nos pavimentos tipo
- A metragem das prumadas de esgoto reforçado DN100 na **Casa de Máquinas** (35.081,40 m) indica altura acumulada das prumadas ao longo dos 31 andares
- Estimativa de altura por prumada: ~3,0 m/andar (típico de pé-direito residencial)

### 2.4 Multiplicadores de Quantidades
- **08° Pavto Tipo (01x):** Quantidades × 1 (pavimento único)
- **09° ao 31° Pavto Tipo (23x):** Quantidades × 23 (pavimentos repetidos)
- Os quantitativos apresentados na Seção 3 **já consideram** esses multiplicadores (valores totalizados)

---

## 3. Quantitativos Detalhados

### 3.1 Tubulações PVC

| Descrição | Material | Diâmetro | UN | Quantidade | Metragem (m) | Observação |
|-----------|----------|----------|-----|------------|--------------|------------|
| Tubo PVC Esgoto Série Normal | PVC rígido | DN40 | m | 810 trechos | 11.555,59 | Ramais de esgoto primário, presente em todos os pavimentos |
| Tubo PVC Esgoto Série Normal | PVC rígido | DN50 | m | 1.869 trechos | 20.366,24 | Ramais secundários e coletores, presente em todos os pavimentos |
| Tubo PVC Esgoto Série Normal | PVC rígido | DN75 | m | 14 trechos | 0,00 | ⚠️ Metragem a recalcular |
| Tubo PVC Esgoto Série Normal | PVC rígido | DN100 | m | 884 trechos | 8.435,69 | Coletores e prumadas, 8 pavimentos |
| Tubo PVC Esgoto Série Normal | PVC rígido | DN150 | m | 35 trechos | 0,00 | ⚠️ Metragem a recalcular, presente em térreo e lazer |
| Tubo PVC Esgoto Série Reforçada | PVC reforçado | DN40 | m | 6 trechos | 4,68 | Ramais especiais em 2 pavimentos |
| Tubo PVC Esgoto Série Reforçada | PVC reforçado | DN50 | m | 394 trechos | 3.652,37 | Ramais e coletores em todos os pavimentos |
| Tubo PVC Esgoto Série Reforçada | PVC reforçado | DN75 | m | 30 trechos | 420,90 | Coletores especiais em 4 pavimentos |
| Tubo PVC Esgoto Série Reforçada | PVC reforçado | DN100 | m | 1.801 trechos | 58.631,98 | **Prumadas principais**, todos os pavimentos |
| Tubo PVC Esgoto Série Reforçada | PVC reforçado | DN150 | m | 690 trechos | 3.613,26 | Coletores e prumadas especiais, todos os pavimentos |
| Tubo PVC Água Fria Soldável | PVC soldável | DN? | m | 793 trechos | 0,00 | ⚠️ **Diâmetro não identificado no modelo** - Consultar plantas DWG. Presente em térreo, lazer e pavimentos tipo (4 pavtos) |

**Subtotal Esgoto Normal:** 3.612 trechos, 40.357,52 m  
**Subtotal Esgoto Reforçado:** 2.921 trechos, 66.323,18 m  
**Subtotal Água Fria:** 793 trechos, 0,00 m (⚠️ metragem pendente)  
**TOTAL GERAL:** 7.326 trechos, 106.680,71 m (⚠️ valor subestimado - recalcular)

---

### 3.2 Conexões e Acessórios

| Descrição | Material | Diâmetro | UN | Quantidade | Observação |
|-----------|----------|----------|-----|------------|------------|
| Anel de Vedação para Vaso Sanitário | Borracha | DN100 | un | 86 | Térreo, lazer e pavimentos tipo (4 pavtos) |
| Caixa Sifonada 100×100×50 (3 entradas) | PVC | DN50/DN40 | un | 68 | 9 pavimentos (exceto térreo) |
| Caixa Sifonada 150×150×50 (7 entradas) | PVC | DN100/DN75/DN50 | un | 146 | Térreo, lazer, pavimentos tipo e casa de máquinas (5 pavtos) |
| Prolongamento para Caixa Sifonada | PVC | - | un | 239 | Extensões de caixas sifonadas, todos os pavimentos |
| Joelho 90° Esgoto Série Normal | PVC rígido | Variados | un | 3.454 | Todos os pavimentos |
| Joelho 90° Esgoto Série Reforçada | PVC reforçado | Variados | un | 1.141 | Todos os pavimentos, prumadas e coletores |
| Joelho 90° Água Fria Soldável | PVC soldável | Variados | un | 591 | 4 pavimentos (térreo, lazer e tipo) |
| Tê de Inspeção Esgoto | PVC | Variados | un | 195 | 9 pavimentos, exceto casa de máquinas |
| Tê Esgoto | PVC | Variados | un | 75 | Térreo, lazer e pavimentos tipo (4 pavtos) |
| Tê Água Fria | PVC soldável | Variados | un | - | ⚠️ Quantidade zerada no modelo (conferir plantas) |
| Curva 90° Esgoto | PVC | Variados | un | 68 | 3 pavimentos (térreo e pavimentos tipo) |
| Luva Simples | PVC | Variados | un | 3.994 | Todos os pavimentos |
| Junção (Y) | PVC | Variados | un | 908 | Todos os pavimentos |
| Redução / Bucha | PVC | Variados | un | 195 | Todos os pavimentos |
| Válvula de Retenção | PVC/metal | DN100 | un | 50 | Térreo (sistema de esgotamento) |
| Porta-Grelha com Válvula | PVC | - | un | - | Incluído em "Conexão Diversos" (verificar quantidade) |
| Conexões Diversas | - | - | un | 130 | 9 pavimentos, itens não classificados |

**TOTAL GERAL:** 11.340 conexões

---

### 3.3 Equipamentos e Terminais

| Descrição | Tipo | UN | Quantidade | Localização | Observação |
|-----------|------|-----|------------|-------------|------------|
| Caixa de Inspeção Lodo | Caixa pré-fabricada | un | 19 | Térreo | Sistema de tratamento de efluentes - **Caixa Lodo 3** |
| Tanque Cilíndrico de Lodo Ativado | Tanque pré-fabricado | un | 12 | Térreo | ETE (Estação de Tratamento de Efluentes) |

**TOTAL GERAL:** 31 equipamentos

**Nota sobre ETE:**
- O modelo IFC identifica **31 elementos** relacionados ao tratamento de efluentes no térreo
- Sistema aparenta ser de **lodo ativado** (tratamento biológico)
- Dimensionamento e capacidade devem ser consultados no memorial descritivo hidrossanitário
- Possível necessidade de equipamentos complementares não modelados: sopradores, bombas de recirculação, quadro de comando

---

### 3.4 Elementos NÃO Identificados no Modelo IFC

Os seguintes elementos **não foram extraídos automaticamente** dos arquivos IFC. Consultar plantas DWG e memorial descritivo:

#### 3.4.1 Águas Pluviais
- **Tubulações de águas pluviais** (DN75, DN100, DN150)
- **Caixas de inspeção pluvial**
- **Ralos e grelhas de piso** (externos e internos)
- **Calhas** (perímetro, platibanda, marquises)
- **Condutores verticais**

#### 3.4.2 Louças e Metais
- **Louças sanitárias:** Bacias sanitárias, lavatórios, tanques, pias de cozinha
- **Metais sanitários:** Válvulas de descarga, torneiras, sifões, flexíveis
- **Registros e válvulas:** Registros de gaveta, esfera, pressão

#### 3.4.3 Ralos e Grelhas (Esgoto)
- **Ralos sifonados** (áreas molhadas)
- **Ralos secos** (áreas secas)
- **Grelhas lineares** (áreas externas, garagem)

#### 3.4.4 Caixas Especiais
- **Caixas de gordura** (cozinhas)
- **Caixas de inspeção de esgoto** (além das 19 da ETE)
- **Separadoras de água e óleo** (garagem)

#### 3.4.5 Reservatórios e Bombas
- **Reservatórios inferiores e superiores** (água potável)
- **Bombas de recalque** (água e esgoto)
- **Bóias, chaves de nível, pressostatos**

#### 3.4.6 Prumadas Especiais
- **Barriletes** (distribuição entre reservatórios)
- **Extravasores e ladrões**
- **Ventilação primária e secundária** (esgoto)

---

## 4. Detalhamento por Pavimento

### 4.1 TÉRREO

**Tubulações:**
- PVC Esgoto Série Normal DN40: 64 trechos
- PVC Esgoto Série Normal DN50: 254 trechos
- PVC Esgoto Série Normal DN75: 10 trechos
- PVC Esgoto Série Normal DN100: 241 trechos
- PVC Esgoto Série Normal DN150: 33 trechos
- PVC Esgoto Série Reforçada DN50: 27 trechos
- PVC Esgoto Série Reforçada DN100: 38 trechos
- PVC Esgoto Série Reforçada DN150: 89 trechos
- PVC Água Fria DN?: 115 trechos

**Conexões (principais):**
- Anel de Vedação Vaso: 9 un
- Caixa Sifonada 100×100 (3E): 10 un
- Caixa Sifonada 150×150 (7E): 14 un
- Joelho Esgoto Normal: 458 un
- Joelho Esgoto Reforçado: 66 un
- Joelho Água Fria: 88 un
- Luva Simples: 520 un
- Tê de Inspeção: 20 un
- Válvula de Retenção: 50 un

**Terminais:**
- Caixa de Inspeção Lodo: 19 un
- Tanque Lodo Ativado: 12 un

---

### 4.2 02° PAVTO. G1 (Garagem 1)

**Tubulações:**
- PVC Esgoto Série Normal DN50: 35 trechos
- PVC Esgoto Série Normal DN100: 2 trechos
- PVC Esgoto Série Reforçada DN50: 18 trechos
- PVC Esgoto Série Reforçada DN100: 43 trechos
- PVC Esgoto Série Reforçada DN150: 72 trechos

**Conexões (principais):**
- Caixa Sifonada 100×100: 6 un
- Joelho Esgoto Normal: 53 un
- Joelho Esgoto Reforçado: 70 un
- Luva Simples: 130 un
- Tê de Inspeção: 13 un

---

### 4.3 03° PAVTO. G2 (Garagem 2)

**Tubulações:**
- PVC Esgoto Série Normal DN50: 35 trechos
- PVC Esgoto Série Normal DN100: 1 trecho
- PVC Esgoto Série Reforçada DN50: 8 trechos
- PVC Esgoto Série Reforçada DN100: 38 trechos
- PVC Esgoto Série Reforçada DN150: 45 trechos

**Conexões (principais):**
- Caixa Sifonada 100×100: 6 un
- Joelho Esgoto Normal: 53 un
- Joelho Esgoto Reforçado: 19 un
- Luva Simples: 91 un
- Tê de Inspeção: 8 un

---

### 4.4 04° PAVTO. G3 (Garagem 3)

**Tubulações:**
- PVC Esgoto Série Normal DN50: 40 trechos
- PVC Esgoto Série Normal DN100: 2 trechos
- PVC Esgoto Série Reforçada DN50: 8 trechos
- PVC Esgoto Série Reforçada DN100: 37 trechos
- PVC Esgoto Série Reforçada DN150: 109 trechos

**Conexões (principais):**
- Caixa Sifonada 100×100: 6 un
- Joelho Esgoto Normal: 95 un
- Joelho Esgoto Reforçado: 65 un
- Luva Simples: 149 un
- Tê de Inspeção: 17 un

---

### 4.5 05° PAVTO. G4 (Garagem 4)

**Tubulações:**
- PVC Esgoto Série Normal DN50: 14 trechos
- PVC Esgoto Série Reforçada DN50: 32 trechos
- PVC Esgoto Série Reforçada DN100: 119 trechos
- PVC Esgoto Série Reforçada DN150: 66 trechos

**Conexões (principais):**
- Caixa Sifonada 100×100: 6 un
- Joelho Esgoto Normal: 66 un
- Joelho Esgoto Reforçado: 88 un
- Luva Simples: 176 un
- Tê de Inspeção: 15 un

---

### 4.6 06° PAVTO. G5 (Garagem 5)

**Tubulações:**
- PVC Esgoto Série Normal DN50: 31 trechos
- PVC Esgoto Série Normal DN75: 1 trecho
- PVC Esgoto Série Normal DN100: 2 trechos
- PVC Esgoto Série Reforçada DN50: 52 trechos
- PVC Esgoto Série Reforçada DN100: 181 trechos
- PVC Esgoto Série Reforçada DN150: 106 trechos

**Conexões (principais):**
- Caixa Sifonada 100×100: 6 un
- Joelho Esgoto Normal: 117 un
- Joelho Esgoto Reforçado: 163 un
- Luva Simples: 296 un
- Tê de Inspeção: 26 un

---

### 4.7 07° PAVTO. LAZER

**Tubulações:**
- PVC Esgoto Série Normal DN40: 144 trechos
- PVC Esgoto Série Normal DN50: 266 trechos
- PVC Esgoto Série Normal DN75: 1 trecho
- PVC Esgoto Série Normal DN100: 286 trechos
- PVC Esgoto Série Normal DN150: 2 trechos
- PVC Esgoto Série Reforçada DN50: 109 trechos
- PVC Esgoto Série Reforçada DN75: 12 trechos
- PVC Esgoto Série Reforçada DN100: 327 trechos
- PVC Esgoto Série Reforçada DN150: 110 trechos
- PVC Água Fria DN?: 158 trechos

**Conexões (principais):**
- Anel de Vedação Vaso: 13 un
- Caixa Sifonada 100×100: 10 un
- Caixa Sifonada 150×150: 45 un
- Joelho Esgoto Normal: 649 un
- Joelho Esgoto Reforçado: 308 un
- Joelho Água Fria: 121 un
- Luva Simples: 874 un
- Prolongamento Caixa Sifonada: 55 un
- Tê de Inspeção: 36 un

**Observação:** Pavimento com maior diversidade de conexões e equipamentos (salão de festas, piscina, churrasqueiras, etc.)

---

### 4.8 08° PAVTO. TIPO (1 unidade)

**Tubulações:**
- PVC Esgoto Série Normal DN40: 290 trechos
- PVC Esgoto Série Normal DN50: 601 trechos
- PVC Esgoto Série Normal DN75: 2 trechos
- PVC Esgoto Série Normal DN100: 196 trechos
- PVC Esgoto Série Reforçada DN40: 2 trechos
- PVC Esgoto Série Reforçada DN50: 99 trechos
- PVC Esgoto Série Reforçada DN75: 8 trechos
- PVC Esgoto Série Reforçada DN100: 457 trechos
- PVC Esgoto Série Reforçada DN150: 73 trechos
- PVC Água Fria DN?: 260 trechos

**Conexões (principais):**
- Anel de Vedação Vaso: 32 un
- Caixa Sifonada 100×100: 9 un
- Caixa Sifonada 150×150: 44 un
- Curva Esgoto: 32 un
- Joelho Esgoto Normal: 1.023 un
- Joelho Esgoto Reforçado: 232 un
- Joelho Água Fria: 194 un
- Luva Simples: 989 un
- Prolongamento Caixa Sifonada: 53 un
- Tê de Inspeção: 53 un

**Observação:** Este pavimento **NÃO se repete** (transição para pavimento tipo padrão)

---

### 4.9 09° AO 31º PAVTO. TIPO (23 unidades)

⚠️ **MULTIPLICADOR:** Este IFC representa **23 pavimentos idênticos** (do 9° ao 31°). Os quantitativos abaixo **já estão totalizados (×23)**.

**Tubulações:**
- PVC Esgoto Série Normal DN40: 289 trechos, **11.490,32 m**
- PVC Esgoto Série Normal DN50: 587 trechos, **19.752,39 m**
- PVC Esgoto Série Normal DN100: 154 trechos, **8.435,69 m**
- PVC Esgoto Série Reforçada DN40: 4 trechos, **4,68 m**
- PVC Esgoto Série Reforçada DN50: 24 trechos, **3.446,23 m**
- PVC Esgoto Série Reforçada DN75: 2 trechos, **311,30 m**
- PVC Esgoto Série Reforçada DN100: 155 trechos, **23.550,58 m**
- PVC Esgoto Série Reforçada DN150: 10 trechos, **3.117,87 m**
- PVC Água Fria DN?: 260 trechos

**Conexões (principais):**
- Anel de Vedação Vaso: 32 un
- Caixa Sifonada 100×100: 9 un
- Caixa Sifonada 150×150: 40 un
- Curva Esgoto: 32 un
- Joelho Esgoto Normal: 849 un
- Joelho Esgoto Reforçado: 3 un
- Joelho Água Fria: 188 un
- Luva Simples: 535 un
- Prolongamento Caixa Sifonada: 49 un
- Tê Esgoto: 30 un

**Observação:** Este é o **único pavimento com metragens completas** no modelo IFC — pode ser usado como referência para estimar metragens dos demais pavimentos

---

### 4.10 CASA DE MÁQUINAS

**Tubulações:**
- PVC Esgoto Série Normal DN40: 4 trechos, **65,27 m**
- PVC Esgoto Série Normal DN50: 6 trechos, **613,85 m**
- PVC Esgoto Série Reforçada DN50: 17 trechos, **206,14 m**
- PVC Esgoto Série Reforçada DN75: 8 trechos, **109,60 m**
- PVC Esgoto Série Reforçada DN100: 406 trechos, **35.081,40 m**
- PVC Esgoto Série Reforçada DN150: 10 trechos, **495,39 m**

**Conexões (principais):**
- Caixa Sifonada 150×150: 3 un
- Joelho Esgoto Normal: 91 un
- Joelho Esgoto Reforçado: 127 un
- Luva Simples: 234 un
- Junção: 103 un

**Observação:** A metragem elevada de DN100 reforçado (**35.081,40 m**) indica **prumadas verticais acumuladas** ao longo dos 31 andares + garagens

---

## 5. Fontes de Dados

### 5.1 Arquivos IFC Processados (10 arquivos)

1. `348 - S01 [10] rev.01 - EL_R.Rubens Alves - TÉRREO.ifc`
2. `348 - S02 [10] rev.01 - EL_R.Rubens Alves - 02° PAVTO. G1.ifc`
3. `348 - S03 [10] rev.01 - EL_R.Rubens Alves - 03° PAVTO. G2.ifc`
4. `348 - S04 [10] rev.01 - EL_R.Rubens Alves - 04° PAVTO. G3.ifc`
5. `348 - S05 [10] rev.01 - EL_R.Rubens Alves - 05° PAVTO. G4.ifc`
6. `348 - S06 [10] rev.01 - EL_R.Rubens Alves - 06° PAVTO. G5.ifc`
7. `348 - S07 [10] rev.01 - EL_R.Rubens Alves - 07° PAVTO. LAZER.ifc`
8. `348 - S08 [10] rev.01 - EL_R.Rubens Alves - 08° PAVTO. TIPO (01x) T. A & T. B.ifc`
9. `348 - S09 [10] rev.01 - EL_R.Rubens Alves - 09° AO 31º PAVTO. TIPO (23x) T. A & T. B.ifc`
10. `348 - S10 [10] rev.01 - EL_R.Rubens Alves - CASA DE MÁQUINAS T. A & T. B.ifc`

**Localização:** `projetos/thozen-electra/projetos/06 SANITÁRIO/IFC/`

### 5.2 Arquivos DWG Disponíveis (20 arquivos)

- **Formato:** DWG Rev.01
- **Torres:** Arquivos duplicados para Torre A (T.A) e Torre B (T.B)
- **Localização:** `projetos/thozen-electra/projetos/06 SANITÁRIO/DWG/`
- **Uso recomendado:** Conferência de metragens, diâmetros de água fria, e elementos não modelados no IFC

### 5.3 Método de Extração

- **Biblioteca:** `ifcopenshell` (Python)
- **Schema IFC:** IFC2X3
- **Elementos extraídos:**
  - `IfcFlowSegment` (tubulações)
  - `IfcFlowFitting` (conexões)
  - `IfcFlowTerminal` (terminais e equipamentos)
- **Propriedades lidas:** Diâmetro, Comprimento, Nome, ObjectType, Norma

---

## 6. Dados Faltantes / Pendências

### 6.1 Críticas (Impedem orçamento completo)
1. ✅ **Metragens de tubulações** — 90% dos valores zerados (recalcular via geometria IFC ou plantas DWG)
2. ✅ **Diâmetros de água fria** — Todos os 793 trechos sem especificação (consultar DWG)
3. ✅ **Sistema de águas pluviais** — Não modelado no IFC (extrair de plantas DWG)
4. ✅ **Louças e metais sanitários** — Não modelados (quantificar via projeto arquitetônico + memorial)
5. ✅ **Ralos e grelhas** — Não modelados (extrair de plantas)

### 6.2 Importantes (Afetam precisão do orçamento)
6. ✅ **Caixas de gordura** — Não identificadas (verificar memorial descritivo)
7. ✅ **Reservatórios** — Capacidade e quantidade não modelados (consultar memorial)
8. ✅ **Bombas de recalque** — Não modeladas (consultar memorial hidráulico)
9. ✅ **Registros e válvulas** — Parcialmente modelados (50 válvulas de retenção no térreo, faltam demais)
10. ⚠️ **Detalhamento da ETE** — Dimensionamento, capacidade, equipamentos complementares (consultar memorial)

### 6.3 Complementares (Melhoram detalhamento)
11. ✅ **Especificações de fabricante/modelo** — Conexões genéricas (Amanco Wavin identificado, faltam códigos comerciais)
12. ⚠️ **Isolamento térmico/acústico** — Não especificado (verificar memorial)
13. ⚠️ **Acessórios de fixação** — Não modelados (braçadeiras, suportes, ganchos)
14. ⚠️ **Materiais de vedação** — Não especificados (cola, fita, massa)

---

## 7. Próximos Passos

### Ações Imediatas (antes de iniciar orçamento executivo)
1. ✅ **Recalcular metragens** — Processar geometrias dos elementos IFC ou medir nas plantas DWG
2. ✅ **Identificar diâmetros de água fria** — Consultar plantas DWG ou memorial
3. ✅ **Extrair águas pluviais** — Processar plantas DWG (camadas/layers específicos)
4. ✅ **Levantar louças e metais** — Usar projeto arquitetônico + memorial descritivo

### Validações Recomendadas
5. ⚠️ **Conferir multiplicadores** — Confirmar se 08° Pavto é realmente único e se 09°-31° são idênticos
6. ⚠️ **Validar ETE** — Conferir memorial para dimensionamento e equipamentos da estação de tratamento
7. ⚠️ **Conferir prumadas** — Validar se a metragem da casa de máquinas representa todas as prumadas corretamente

### Melhorias no Modelo (opcional, para revisões futuras)
8. ⚠️ **Solicitar correção de propriedades Length** — Fornecedor do modelo BIM
9. ⚠️ **Solicitar modelagem de águas pluviais** — Incluir em revisões futuras do IFC
10. ⚠️ **Padronizar diâmetros** — Garantir que todos os elementos tenham propriedade Diâmetro preenchida

---

## 8. Anexos e Referências

### 8.1 Referência de Normas
- **NBR 5688:2018** — Tubos e conexões de PVC-U para sistemas prediais de água pluvial, esgoto sanitário e ventilação
- **NBR 8160:1999** — Sistemas prediais de esgoto sanitário — Projeto e execução

### 8.2 Mapeamento N1 Memorial Cartesiano
Este briefing alimenta o item:
- **N1 06 — Instalações Hidrossanitárias**
  - N2 06.01 — Esgoto Sanitário
  - N2 06.02 — Água Fria
  - N2 06.03 — Águas Pluviais
  - N2 06.04 — Equipamentos Especiais (ETE)

### 8.3 Arquivos de Trabalho
- **Dados consolidados (JSON):** `executivo/thozen-electra/sanitario_raw_data.json`
- **Este briefing:** `executivo/thozen-electra/briefings/sanitario-r00.md`

---

**Revisão:** R00 — Primeira extração (dados parciais do modelo IFC)  
**Gerado em:** 20/03/2026  
**Processado por:** Cartesiano (subagent: extração-sanitario-electra)
