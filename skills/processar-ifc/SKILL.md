---
name: processar-ifc
description: Use quando precisar extrair quantitativos de arquivos IFC (BIM). Trigger quando mencionarem "processa o IFC", "extrai quantitativos do IFC", "analisa o modelo BIM", ou quando receber arquivos .ifc para extracao de dados de estrutura, instalacoes, arquitetura.
---

# Processar IFC — Extracao de Quantitativos

Extrai quantitativos de arquivos IFC usando ifcopenshell para alimentar orcamentos.

## Fluxo

### 1. Localizar IFCs

```bash
ls projetos/[projeto]/projetos/[disciplina]/IFC/*.ifc
```

### 2. Extrair com ifcopenshell

```python
import ifcopenshell

ifc = ifcopenshell.open("caminho/arquivo.ifc")
print(f"Schema: {ifc.schema}")
print(f"Elementos: {len(ifc.by_type('IfcProduct'))}")

# Contar por tipo
for tipo in ['IfcWall', 'IfcColumn', 'IfcBeam', 'IfcSlab', 'IfcFlowSegment', 'IfcFlowTerminal']:
    elementos = ifc.by_type(tipo)
    if elementos:
        print(f"  {tipo}: {len(elementos)}")
```

### 3. Dados por disciplina

**Estrutura (IfcColumn, IfcBeam, IfcSlab, IfcFooting):**
- Volume de concreto por elemento
- Contagem por pavimento (storey)
- Dimensoes (secao de pilares, vao de vigas, espessura de lajes)

**Eletrico (IfcFlowSegment, IfcFlowTerminal):**
- Eletrodutos: contagem por diametro (ObjectType ou PropertySet "Tamanho")
- Luminarias: contagem por pavimento
- Caixas, tomadas, interruptores

**Hidrossanitario (IfcPipeSegment, IfcPipeFitting):**
- Tubulacoes: metragem por diametro e material
- Conexoes: contagem por tipo
- Equipamentos: bombas, reservatorios, pressurizadores

**Telecomunicacoes (IfcFlowSegment com classificacao telecom):**
- Eletrodutos, caixas de passagem, pontos de dados/voz

### 4. Separar por torre (quando 2+ torres)

```python
# Usar coordenada X do midpoint para separar torres
import ifcopenshell.util.placement as placement

for elem in ifc.by_type('IfcFlowSegment'):
    matrix = placement.get_local_placement(elem.ObjectPlacement)
    x = matrix[0][3]  # coordenada X
    torre = 'A' if x < midpoint_x else 'B'
```

Calcular midpoint: media das coordenadas X de todos os elementos.

### 5. Multiplicar pavimento tipo

Se o IFC tem 1 arquivo por pavimento (ex: E08 = Tipo x24):
- Quantitativos do tipo multiplicados por N pavimentos tipo
- Pavimentos unicos (Terreo, Lazer, Casa Maq) contam x1

### 6. Salvar resultados

```python
import json
resultado = {
    "projeto": "[nome]",
    "disciplina": "[disciplina]",
    "fonte": "[nome_arquivo.ifc]",
    "schema": ifc.schema,
    "quantitativos": { ... },
    "por_pavimento": { ... },
    "por_torre": { ... }
}
with open("output/[projeto]-[disciplina]-quantitativos.json", "w") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)
```

### 7. Gerar briefing MD

Resumo com tabelas de quantitativos, fontes, pendencias.
Salvar em `executivos/[projeto]/briefings/[disciplina]-r00.md`

## Limitacoes comuns de IFC

| Dado | Disponivel? | Alternativa |
|------|-------------|-------------|
| Metragens lineares | Raro (geometria complexa) | Estimar por indice ou DWG |
| Bitolas de cabo | Nao (IFC2X3) | Processar DWGs |
| Especificacoes tecnicas | Limitado | Memorial descritivo |
| Quadros eletricos | Raro | DWGs unifilares |
| Diametros eletroduto | As vezes (PropertySet) | DWGs |

## Regra

SEMPRE informar o que foi extraido E o que NAO foi encontrado no IFC. Pendencias devem ser listadas explicitamente.
