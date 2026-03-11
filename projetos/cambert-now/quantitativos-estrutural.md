# Quantitativos Estruturais - Now Residence

**Projeto:** Now Residence (Cambert)  
**Arquivo IFC:** 216NOW-EST-PE-001-GERAL-R07.ifc  
**Data de Processamento:** 11/03/2026  
**Área Construída Total:** 13.054 m²  
**Status:** ⚠️ **Extração não concluída - IFC sem quantidades**

---

## ⚠️ Diagnóstico

O arquivo IFC **216NOW-EST-PE-001-GERAL-R07.ifc** foi analisado utilizando ifcopenshell (Python 3.11) mas **não contém dados de quantitativos estruturais**.

### O que foi encontrado:

✅ **Elementos modelados:**
- **227 lajes** (IfcSlab)
- **319 vigas** (IfcBeam)
- **526 pilares** (IfcColumn)
- **32 pavimentos** (IfcBuildingStorey)
- **3 materiais** definidos

❌ **O que NÃO foi encontrado:**
- Quantidades de volume (IfcQuantityVolume)
- Quantidades de área (IfcQuantityArea)
- Quantidades de comprimento (IfcQuantityLength)
- Dados de armadura (IfcReinforcingBar)
- Geometria processável para cálculo de volumes

---

## 🔍 Análise Técnica

### Schema IFC
- **Versão:** IFC2X3
- **Total de entidades:** 37.704
- **Representação geométrica:** Presente, mas não processável via ifcopenshell.geom

### Exemplos de Elementos

**Laje:**
- Nome: `Piso:TQS h=21:296500`
- Tipo: `Piso:TQS h=21`
- PropertySets: Pset_QuantityTakeOff, Pset_SlabCommon (sem quantidades)

**Viga:**
- Nome: `TQS - Viga retangular:30,0 x 60,0:295255`
- Tipo: `TQS - Viga retangular:30,0 x 60,0`
- Dimensões no nome: 30cm x 60cm

**Pilar:**
- Nome: `TQS - Pilar retangular:20,0 x 120,0:292849`
- Tipo: `TQS - Pilar retangular:20,0 x 120,0`
- Dimensões no nome: 20cm x 120cm

### Pavimentos Identificados

1. Sapata B.O. (cota: -460)
2. Sapata T.O. (cota: -430)
3. Laje T.O. (cota: -400)
4. Parede da fundação T.O. (cota: -30)
5. Nível 1 (cota: 0)
6. Fundação (cota: 70)
7. Nível 2 (cota: 400)
8. G1 (cota: 430)
9. G2 (cota: 700)
10. G3 (cota: 970)
11. ... (continua até 32 pavimentos)

---

## 🎯 Recomendações

### 1️⃣ **Solicitar Relatórios Nativos do TQS** (MAIS RÁPIDO)

Pedir ao projetista estrutural para gerar os seguintes relatórios diretamente do TQS:

**Concreto:**
- Volume total por pavimento
- Volume por tipo de elemento (lajes, vigas, pilares, fundações)
- Índice m³/m² AC

**Formas:**
- Área total por pavimento
- Área por tipo de elemento
- Índice m²/m² AC

**Armadura:**
- Peso total de aço (kg ou toneladas)
- Distribuição por pavimento
- Distribuição por elemento
- Índice kg/m³ concreto

### 2️⃣ **Reexportar IFC com Quantidades** (RECOMENDADO)

Solicitar novo export do TQS com as seguintes configurações:
- ✅ Incluir quantidades (IfcElementQuantity)
- ✅ Incluir dados de armadura (IfcReinforcingBar)
- ✅ Geometria completa
- Schema: IFC2X3 ou IFC4 (preferencialmente IFC4)

### 3️⃣ **Usar Software BIM Específico**

Processar o IFC atual em:
- Autodesk Navisworks Manage
- Solibri Model Checker
- Tekla BIMsight
- BIM Vision (gratuito)

### 4️⃣ **Quantificação Manual**

Como último recurso, quantificar manualmente com base em:
- Pranchas 2D do projeto executivo
- Tabelas de vigas, pilares e lajes
- Detalhamentos estruturais

---

## 📋 Dados do Projeto (Referência)

- **AC Total:** 13.054 m²
- **Estrutura:** Mista (concreto armado + protendido)
- **Configuração:** 3 garagens + térreo + lazer + 17 pavimentos tipo + ático + cobertura
- **Pé-direito tipo:** 3,06 m

---

## 🔧 Processo Técnico Executado

1. Abertura do arquivo IFC via ifcopenshell v0.8.4
2. Busca por IfcElementQuantity → **0 encontrados**
3. Busca por IfcReinforcingBar → **0 encontrados**
4. Tentativa de extração via ifcopenshell.geom.create_shape() → **Falha em 100% dos elementos**
5. Tentativa de extração via ifcopenshell.geom.iterator() → **Objeto Triangulation sem atributo volume**
6. Análise de PropertySets → **Propriedades genéricas, sem quantidades**

---

## ✅ Próximos Passos

1. **Contatar projetista estrutural** solicitando:
   - Relatório de quantitativos do TQS (formato PDF ou Excel)
   - Novo export IFC com quantidades ativadas

2. **Aguardar arquivo correto** antes de prosseguir com orçamento paramétrico

3. **Alternativa imediata:** Usar índices paramétricos da base Cartesian:
   - Concreto: ~0,18 m³/m² AC (mediana residencial vertical)
   - Formas: ~1,20 m²/m² AC
   - Aço: ~85 kg/m³ concreto

   **Estimativa preliminar (não precisa):**
   - Concreto: 13.054 × 0,18 = **~2.350 m³**
   - Formas: 13.054 × 1,20 = **~15.650 m²**
   - Aço: 2.350 × 85 = **~200 ton**

---

## 📞 Contato

Para obter os quantitativos corretos, contatar:

**Projetista Estrutural:** [inserir nome/empresa]  
**Responsável técnico:** [inserir nome]  
**Solicitação:** Relatório de quantitativos TQS (concreto + formas + aço) do projeto Now Residence (R07)

---

**Relatório gerado por:** Jarvis (IA Cartesian)  
**Ferramenta:** ifcopenshell v0.8.4 + Python 3.11  
**Conclusão:** Arquivo IFC válido estruturalmente, mas sem dados quantitativos extraíveis.
