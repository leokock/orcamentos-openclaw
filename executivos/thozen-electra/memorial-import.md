# Thozen Electra - Importação Memorial Cartesiano

**Projeto:** Thozen Electra  
**ID Memorial:** `cdff0592-fb3c-4c13-9516-efde6b56b336`  
**URL:** https://cliente.cartesianengenharia.com/admin/projects/cdff0592-fb3c-4c13-9516-efde6b56b336  
**Data da Extração:** 2026-03-20

---

## 📊 Resumo da Extração

### Estrutura EAP

**Hierarquia completa extraída:**

- **2 Unidades Construtivas (UC)**
  - UC 01: GERENCIAMENTO TÉCNICO E ADMINISTRATIVO
  - UC 02: GERENCIAMENTO EXECUTIVO

- **27 Células Construtivas (CC)**
  - UC 01: 3 células (Serviços Técnicos, Serviços Iniciais, Equipamentos)
  - UC 02: 24 células (Infraestrutura, Supraestrutura, Paredes, Alvenaria, Revestimentos, Pisos, Forros, Impermeabilização, Esquadrias, Vidros, Pintura, Louças/Metais, Instalações, etc.)

- **79 Etapas**
- **372 Subetapas**
- **0 Serviços** *(nota: a planilha não possui serviços cadastrados abaixo das subetapas)*

**Observação:** A estrutura EAP está completa até o nível de **Subetapa**. Os serviços não estão detalhados na aba "EAP", mas estão presentes como CPUs na aba "CPU".

### CPUs (Composições de Preço Unitário)

**Total de CPUs extraídas:** 926 composições

**Estrutura de cada CPU:**
- Código (baseado na descrição curta)
- Descrição completa
- Unidade de medida
- Custo total da composição
- Lista de insumos (com código, descrição, unidade, quantidade e custo unitário)

**Exemplos de CPUs:**
- Central de aço (M2) - R$ 118,10
- Central de fôrmas (M2) - R$ 118,10
- Armazenamento de cerâmicas (M2) - R$ 382,10
- Diversas composições de infraestrutura, supraestrutura, acabamentos, instalações, etc.

**Média de insumos por CPU:** ~7-10 insumos

### Insumos

**Total de Insumos extraídos:** 835 insumos

**Grupos principais (top 10):**
1. Revestimentos: 145 insumos
2. Serviço Terceiros: 134 insumos
3. Pintura: 73 insumos
4. Esquadrias: 70 insumos
5. Alvenaria: 44 insumos
6. Louças e metais: 42 insumos
7. Concreto: 32 insumos
8. Materiais complementares: 32 insumos
9. Impermeabilização: 32 insumos
10. Drywall/Shaft/Forro: 30 insumos

**Estrutura de cada insumo:**
- Código (gerado sequencial: INS_00001, INS_00002, etc.)
- Descrição
- Unidade de medida
- Custo unitário (R$)
- Grupo
- Subgrupo

**Faixa de valores:**
- Insumos de R$ 0,23 (parafusos) até R$ 1.609,67 (armação de estaca)
- Maioria dos insumos: R$ 5-500

---

## 📂 Arquivos Gerados

### 1. `eap.json`
Estrutura hierárquica completa da EAP:
```json
{
  "project_id": "cdff0592-fb3c-4c13-9516-efde6b56b336",
  "unidades_construtivas": [
    {
      "codigo": "01",
      "nome": "GERENCIAMENTO TÉCNICO E ADMINISTRATIVO",
      "celulas": [
        {
          "codigo": "01",
          "nome": "SERVIÇOS TÉCNICOS",
          "etapas": [
            {
              "codigo": "01.001",
              "nome": "ESTUDOS, PROJETOS E CONSULTORIAS",
              "subetapas": [...]
            }
          ]
        }
      ]
    }
  ]
}
```

**Níveis:** UC → CC → Etapa → Subetapa → Serviço  
**Códigos preservados:** Códigos originais da planilha mantidos

### 2. `cpus.json`
Array de 926 composições de preço unitário:
```json
[
  {
    "codigo": "Central de aço",
    "descricao": "Central de aço",
    "unidade": "M2",
    "custo_total": 118.10,
    "insumos": [
      {
        "codigo": "Central de aço",
        "descricao": "LONA PLASTICA 120 MICRAS 4X100M PRETA",
        "unidade": "M2",
        "quantidade": 1.0,
        "custo_unitario": 1.25,
        "custo_total": 1.25
      },
      ...
    ]
  },
  ...
]
```

**Informações por CPU:**
- Código, descrição, unidade
- Custo total da composição
- Insumos detalhados (quantidade × custo unitário)

### 3. `insumos.json`
Array de 835 insumos catalogados:
```json
[
  {
    "codigo": "INS_00001",
    "descricao": "Arame Galvanizado",
    "unidade": "KG",
    "custo_unitario": 13.69,
    "grupo": "Aço",
    "subgrupo": "Arame"
  },
  ...
]
```

**Informações por insumo:**
- Código único gerado (INS_XXXXX)
- Descrição, unidade, custo unitário
- Grupo e subgrupo para categorização

---

## ✅ Próximos Passos para Importação no Memorial

### 1. Cadastrar Unidades Construtivas (Torres + Embasamento)

**Pendente no Memorial:**
- Torre A
- Torre B
- Embasamento

**Ação no Memorial:**
1. Acessar projeto: https://cliente.cartesianengenharia.com/admin/projects/cdff0592-fb3c-4c13-9516-efde6b56b336
2. Criar 3 Unidades Construtivas (se ainda não cadastradas)
3. Anotar os IDs das UCs criadas

### 2. Importar EAP

**Opções de importação:**

**Opção A - Upload via API:**
- Enviar `eap.json` via endpoint de importação do Memorial
- Validar mapeamento de códigos

**Opção B - Cadastro manual estruturado:**
- Usar `eap.json` como referência
- Cadastrar hierarquia no admin do Memorial
- Níveis: UC → CC → Etapa → Subetapa
- **Importante:** Os serviços não estão detalhados na EAP — eles virão das CPUs

### 3. Importar Insumos

**Antes de importar CPUs:**
1. Importar a base de insumos (`insumos.json`)
2. Validar códigos duplicados (se já existem insumos cadastrados)
3. Criar mapeamento de códigos: INS_XXXXX → ID do Memorial

**Grupos a revisar:**
- Revestimentos (145 itens) — verificar se há duplicatas
- Serviço Terceiros (134 itens) — validar descrições
- Esquadrias (70 itens) — conferir especificações

### 4. Importar CPUs

**Após importar insumos:**
1. Importar `cpus.json`
2. Mapear insumos das composições para os IDs do Memorial
3. Validar cálculos de custo total (soma dos insumos)
4. Associar cada CPU à respectiva Subetapa da EAP

**Validações importantes:**
- Conferir se todas as CPUs têm insumos cadastrados
- Verificar unidades de medida (M2, M3, UN, KG, etc.)
- Conferir cálculo: `custo_total` da CPU = soma dos `custo_total` dos insumos

### 5. Vincular CPUs às Subetapas

**Estratégia de vinculação:**

A aba "CPU" não possui mapeamento direto com a EAP. Será necessário:

1. **Análise semântica:** Comparar descrições das CPUs com as subetapas
2. **Validação manual:** Revisar e confirmar vinculações propostas
3. **Cadastro no Memorial:** Associar cada CPU à subetapa correta

**Exemplo de vinculação:**
- CPU "Central de aço" → Subetapa "01.002.001 - Mobilização e Desmobilização"
- CPU "Escavação manual terreno 1ª categoria" → Subetapa "01.001.001 - Escavação"

### 6. Ajustar Estrutura de Torres/Embasamento

**Pendente:**
- Duplicar estrutura EAP para Torre A, Torre B e Embasamento
- Ajustar quantitativos por unidade construtiva
- Validar custos totais por torre

---

## ⚠️ Pontos de Atenção

### 1. Serviços não detalhados na EAP
A planilha possui **372 subetapas** mas **0 serviços** cadastrados na aba "EAP". Os serviços estão implícitos nas **926 CPUs** da aba "CPU". Será necessário associar as CPUs às subetapas durante a importação.

### 2. Códigos de Insumos gerados
Os insumos da planilha original **não possuem códigos únicos**. Foram gerados códigos sequenciais (INS_00001 a INS_00835). Se o Memorial já possui insumos cadastrados, será necessário mapear para evitar duplicatas.

### 3. Vinculação CPU ↔ EAP
A aba "CPU" não possui coluna de mapeamento explícito para a EAP. Será necessário vincular manualmente (ou via script de análise semântica) cada uma das 926 CPUs às 372 subetapas.

### 4. Unidades Construtivas repetidas
A planilha contém apenas a estrutura genérica de UCs. Para cadastrar **Torre A, Torre B e Embasamento**, será necessário:
- Replicar a UC "02 - GERENCIAMENTO EXECUTIVO" 3 vezes
- Ajustar quantitativos por unidade
- Ou importar uma estrutura única e diferenciar via planilhas de quantitativo

### 5. Custos e quantitativos
Os custos nas CPUs são **unitários** (R$/M2, R$/M3, etc.). Será necessário:
- Levantar quantitativos totais por subetapa
- Calcular custo total = custo_unitário × quantidade
- Validar com orçamento global do projeto

---

## 🔧 Recomendações Técnicas

### Script de Vinculação Automática (CPU ↔ EAP)

Criar um script Python para:
1. Ler `eap.json` e `cpus.json`
2. Analisar descrições das CPUs
3. Propor vinculação com subetapas (via matching de palavras-chave)
4. Gerar arquivo de mapeamento para revisão manual

**Exemplo de lógica:**
```python
# Buscar "escavação" nas CPUs e vincular à subetapa "01.001.001 - Escavação"
# Buscar "concreto" + "laje" → vincular a subetapas de supraestrutura
```

### Validação de Duplicatas de Insumos

Antes de importar 835 insumos:
1. Exportar base de insumos do Memorial
2. Comparar descrições e grupos
3. Mapear insumos existentes para reutilizar IDs
4. Importar apenas insumos novos

### Importação Incremental

Estratégia recomendada:
1. **Fase 1:** Importar apenas a EAP (estrutura vazia)
2. **Fase 2:** Importar insumos (validar duplicatas)
3. **Fase 3:** Importar CPUs (testar com 10-20 composições primeiro)
4. **Fase 4:** Vincular CPUs às subetapas (por lote, revisando manualmente)
5. **Fase 5:** Cadastrar quantitativos por torre/embasamento

---

## 📌 Checklist de Importação

- [ ] Cadastrar UCs no Memorial (Torre A, Torre B, Embasamento)
- [ ] Importar estrutura EAP (27 células, 79 etapas, 372 subetapas)
- [ ] Validar códigos da EAP no Memorial
- [ ] Exportar insumos existentes do Memorial
- [ ] Comparar e mapear insumos (evitar duplicatas)
- [ ] Importar novos insumos (835 itens)
- [ ] Testar importação de 10 CPUs (validação)
- [ ] Importar todas as CPUs (926 composições)
- [ ] Vincular CPUs às subetapas da EAP
- [ ] Cadastrar quantitativos por UC (Torre A, B, Embasamento)
- [ ] Validar custo total do projeto
- [ ] Revisar estrutura no Memorial (navegação, relatórios)

---

**Arquivos gerados:**
- `executivo/thozen-electra/eap.json` (estrutura hierárquica)
- `executivo/thozen-electra/cpus.json` (926 composições)
- `executivo/thozen-electra/insumos.json` (835 insumos)
- `executivo/thozen-electra/memorial-import.md` (este arquivo)

**Próxima ação sugerida:**  
Revisar os JSONs gerados e definir estratégia de importação (manual, API ou script customizado).
