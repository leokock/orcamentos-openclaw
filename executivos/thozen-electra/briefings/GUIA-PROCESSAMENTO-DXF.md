# Guia de Processamento — DXF de Ventilação Mecânica — Thozen Electra

**Projeto:** Thozen Electra  
**Disciplina:** Ventilação Mecânica — Pressurização de Escadas  
**Objetivo:** Extrair quantitativos reais do DXF para gerar Briefing R02 validado

---

## 📋 PRÉ-REQUISITOS

### 1. Arquivos Necessários
- [ ] **DXF do projeto:** `RA_EVM_LEGAL_PROJETO_R05.dxf` (solicitar ao projetista)
- [ ] **Memorial descritivo:** Especificações técnicas em PDF
- [ ] **Planilha de equipamentos** (opcional, mas recomendado)

### 2. Ferramentas Instaladas
```bash
# Verificar se ezdxf está instalado
python3.11 -c "import ezdxf; print(ezdxf.__version__)"
# Esperado: 1.4.3 ou superior
```

---

## 🚀 WORKFLOW DE PROCESSAMENTO

### PASSO 1: Receber e Organizar Arquivos

Quando o DXF chegar (via Slack ou email):

```bash
# Baixar arquivo da thread do Slack
python3.11 scripts/slack_file_downloader.py --bot cartesiano --baixar --thread <thread_ts> --tipo dxf

# OU mover arquivo recebido manualmente
mv ~/Downloads/RA_EVM_LEGAL_PROJETO_R05.dxf executivo/thozen-electra/fontes/

# Copiar para diretório de processamento
cp executivo/thozen-electra/fontes/RA_EVM_LEGAL_PROJETO_R05.dxf \
   projetos/thozen-electra/dxf-ventilacao/
```

### PASSO 2: Inspecionar o DXF

Criar script Python para inspeção inicial:

```python
#!/usr/bin/env python3.11
"""Inspecionar DXF de ventilação mecânica."""

import ezdxf
from pathlib import Path

# Abrir DXF
dxf_path = Path("projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf")
doc = ezdxf.readfile(dxf_path)
msp = doc.modelspace()

# Listar layers
print("=== LAYERS ===")
for layer in doc.layers:
    print(f"- {layer.dxf.name} (cor: {layer.dxf.color})")

# Listar tipos de entidades
print("\n=== ENTIDADES ===")
entity_types = {}
for entity in msp:
    etype = entity.dxftype()
    entity_types[etype] = entity_types.get(etype, 0) + 1

for etype, count in sorted(entity_types.items(), key=lambda x: -x[1]):
    print(f"- {etype}: {count}")

# Listar blocos (equipamentos)
print("\n=== BLOCOS (primeiros 20) ===")
for i, block in enumerate(doc.blocks):
    if i >= 20:
        break
    print(f"- {block.name}")
```

Executar:
```bash
python3.11 scripts/inspecionar_dxf_ventilacao.py > executivo/thozen-electra/dxf-ventilacao/inspecao-inicial.txt
```

### PASSO 3: Extrair Dutos (POLYLINEs)

```python
#!/usr/bin/env python3.11
"""Extrair metragem de dutos."""

import ezdxf
from pathlib import Path

dxf_path = Path("projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf")
doc = ezdxf.readfile(dxf_path)
msp = doc.modelspace()

# Buscar POLYLINEs em layers de dutos
layers_dutos = []  # Ajustar conforme inspeção (ex: "DUTOS", "VENT", "EVM")

dutos_verticais = []
dutos_horizontais = []

for polyline in msp.query('POLYLINE'):
    layer = polyline.dxf.layer
    if any(ld in layer.upper() for ld in layers_dutos):
        # Calcular comprimento
        length = polyline.virtual_entities()[0].length if polyline.has_virtual_entities() else 0
        
        # Classificar (vertical vs horizontal)
        # Lógica: se delta_z > delta_x e delta_y → vertical
        # Ajustar conforme geometria do projeto
        
        print(f"Layer: {layer} | Comprimento: {length:.2f} m")

# Totalizar
print(f"\nTotal dutos verticais: {sum(dutos_verticais):.2f} m")
print(f"Total dutos horizontais: {sum(dutos_horizontais):.2f} m")
```

### PASSO 4: Identificar Equipamentos (BLOCKs)

```python
#!/usr/bin/env python3.11
"""Extrair ventiladores, grelhas, dampers."""

import ezdxf
from pathlib import Path

dxf_path = Path("projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf")
doc = ezdxf.readfile(dxf_path)
msp = doc.modelspace()

# Dicionário de padrões de blocos
padroes_blocos = {
    "ventilador": ["VENT", "FAN", "VENTIL"],
    "grelha": ["GRELHA", "GRILL", "DIFUSOR", "DIFFUSER"],
    "damper_cf": ["DAMPER", "DCF", "CORTA-FOGO", "FIRE"],
    "damper_mot": ["DAMPER-M", "DMO", "MOTORIZADO"],
    "sensor": ["SENSOR", "PS", "PRESSURE"],
}

# Contar blocos
contadores = {k: [] for k in padroes_blocos.keys()}

for insert in msp.query('INSERT'):
    block_name = insert.dxf.name.upper()
    
    for tipo, padroes in padroes_blocos.items():
        if any(p in block_name for p in padroes):
            contadores[tipo].append({
                "nome": insert.dxf.name,
                "posicao": insert.dxf.insert,
                "layer": insert.dxf.layer
            })

# Relatório
for tipo, blocos in contadores.items():
    print(f"\n=== {tipo.upper()} ({len(blocos)}) ===")
    for bloco in blocos[:10]:  # Primeiros 10
        print(f"- {bloco['nome']} @ {bloco['posicao']} (layer: {bloco['layer']})")
```

### PASSO 5: Extrair Especificações (TEXTs)

```python
#!/usr/bin/env python3.11
"""Extrair especificações técnicas de textos."""

import ezdxf
import re
from pathlib import Path

dxf_path = Path("projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf")
doc = ezdxf.readfile(dxf_path)
msp = doc.modelspace()

# Padrões de especificações
padroes_specs = {
    "vazao": r"(\d{1,5})\s*(m3/h|m³/h|CFM)",
    "pressao": r"(\d{2,4})\s*(Pa|mmCA)",
    "potencia": r"(\d{1,2}[,.]?\d?)\s*(CV|HP|kW)",
    "diametro": r"(Ø|ø|D)\s*(\d{2,4})\s*(mm)?",
}

especificacoes_encontradas = {k: [] for k in padroes_specs.keys()}

for text in msp.query('TEXT MTEXT'):
    conteudo = text.dxf.text if hasattr(text.dxf, 'text') else text.text
    
    for tipo, padrao in padroes_specs.items():
        matches = re.findall(padrao, conteudo, re.IGNORECASE)
        if matches:
            especificacoes_encontradas[tipo].append({
                "texto": conteudo,
                "valor": matches[0],
                "layer": text.dxf.layer
            })

# Relatório
for tipo, specs in especificacoes_encontradas.items():
    print(f"\n=== {tipo.upper()} ({len(specs)}) ===")
    for spec in specs[:5]:  # Primeiras 5
        print(f"- {spec['texto']} → {spec['valor']}")
```

### PASSO 6: Consolidar Dados

Criar estrutura de dados consolidada:

```python
dados_extraidos = {
    "sistema_geral": {
        "num_escadas": 0,  # Contar no DXF
        "tipo_escada": "PF2",  # Confirmar em legenda
        "num_pavimentos": 32,  # Confirmar com arquitetura
    },
    "ventiladores": [
        {
            "id": 1,
            "vazao": 0,  # Extrair de TEXT
            "pressao": 0,  # Extrair de TEXT
            "potencia": 0,  # Extrair de TEXT
            "localizacao": "",  # Extrair de INSERT.position
        }
    ],
    "dutos": {
        "vertical": {
            "metragem": 0,  # Somar POLYLINEs
            "diametro": 0,  # Extrair de TEXT/legenda
        },
        "horizontal": {
            "metragem": 0,  # Somar POLYLINEs
            "secao": "",  # Extrair de TEXT/legenda
        }
    },
    "grelhas": {
        "escada": 0,  # Contar INSERTs
        "antecamara": 0,  # Contar INSERTs
    },
    "dampers": {
        "corta_fogo": 0,  # Contar INSERTs
        "motorizados": 0,  # Contar INSERTs
        "balanceamento": 0,  # Contar INSERTs
    },
    "automacao": {
        "sensores_pressao": 0,  # Contar INSERTs
    }
}

# Salvar JSON
import json
with open("executivo/thozen-electra/dxf-ventilacao/dados-extraidos.json", "w") as f:
    json.dump(dados_extraidos, f, indent=2, ensure_ascii=False)
```

---

## 📊 VALIDAÇÃO DOS DADOS

### Checklist de Validação

| # | Item | Fonte | Validação |
|---|------|-------|-----------|
| 1 | Número de escadas | DXF (contar eixos/shafts) | Cruzar com planta arquitetônica |
| 2 | Vazão ventiladores | DXF (textos) ou memorial | Conferir unidade (m³/h vs CFM) |
| 3 | Pressão ventiladores | DXF (textos) ou memorial | Conferir unidade (Pa vs mmCA) |
| 4 | Potência ventiladores | DXF (textos) ou memorial | Conferir unidade (CV vs kW) |
| 5 | Metragem dutos | DXF (POLYLINEs) | Conferir com isométrico (se houver) |
| 6 | Diâmetro dutos | DXF (textos/legenda) | Conferir se único ou múltiplos |
| 7 | Grelhas/difusores | DXF (blocos) | Conferir localização (pav, eixo) |
| 8 | Dampers CF | DXF (blocos) | Conferir certificação 90min/120min |
| 9 | Dampers motorizados | DXF (blocos) | Conferir tipo (modulante vs on/off) |
| 10 | Sensores | DXF (blocos) | Conferir faixa (0-100 Pa) |

---

## 🔧 SCRIPT COMPLETO (TEMPLATE)

Salvar em: `scripts/processar_dxf_ventilacao.py`

```python
#!/usr/bin/env python3.11
"""
Processar DXF de ventilação mecânica — Thozen Electra.
Extrair quantitativos completos para Briefing R02.
"""

import ezdxf
import json
import re
from pathlib import Path
from collections import defaultdict

# Configurações
DXF_PATH = Path("projetos/thozen-electra/dxf-ventilacao/RA_EVM_LEGAL_PROJETO_R05.dxf")
OUTPUT_JSON = Path("executivo/thozen-electra/dxf-ventilacao/dados-extraidos.json")
OUTPUT_REPORT = Path("executivo/thozen-electra/dxf-ventilacao/relatorio-extracao.md")

def main():
    print("=" * 70)
    print("PROCESSAMENTO DE DXF — VENTILAÇÃO MECÂNICA — THOZEN ELECTRA")
    print("=" * 70)
    
    # Abrir DXF
    if not DXF_PATH.exists():
        print(f"❌ Arquivo não encontrado: {DXF_PATH}")
        print("\n💡 Certifique-se de que o DXF foi salvo em:")
        print(f"   {DXF_PATH}")
        return
    
    print(f"\n📄 Abrindo: {DXF_PATH.name}")
    doc = ezdxf.readfile(DXF_PATH)
    msp = doc.modelspace()
    
    # Estrutura de dados
    dados = {
        "sistema_geral": {},
        "ventiladores": [],
        "dutos": {},
        "grelhas": {},
        "dampers": {},
        "automacao": {},
        "eletrica": {},
    }
    
    # TODO: Implementar extração (ver passos 3-5 acima)
    
    # Salvar JSON
    OUTPUT_JSON.parent.mkdir(exist_ok=True, parents=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Dados salvos em: {OUTPUT_JSON}")
    
    # Gerar relatório Markdown
    # TODO: Implementar geração de relatório
    
    print("\n" + "=" * 70)
    print("PRÓXIMO PASSO: Gerar Briefing R02 com dados validados")
    print("=" * 70)

if __name__ == "__main__":
    main()
```

---

## 📝 GERAR BRIEFING R02

Após extrair os dados, atualizar o briefing:

```bash
# 1. Processar DXF
python3.11 scripts/processar_dxf_ventilacao.py

# 2. Revisar dados extraídos
cat executivo/thozen-electra/dxf-ventilacao/dados-extraidos.json

# 3. Gerar briefing R02 (substituir premissas por valores reais)
# TODO: Implementar script de geração de briefing
```

### Template de Atualização (R01 → R02)

```markdown
# Briefing: VENTILAÇÃO MECÂNICA — Thozen Electra — R02

## Metadados
- **Revisão:** R02 (dados extraídos de DXF + memorial validado)
- **Data:** <DATA_ATUAL>
- **Fonte dos dados:** RA_EVM_LEGAL_PROJETO_R05.dxf + memorial descritivo

## ✅ STATUS DA REVISÃO R02

**✅ EXTRAÇÃO AUTOMÁTICA CONCLUÍDA**

### Dados Extraídos
1. ✅ Metragem de dutos (POLYLINEs): XXX m (vertical) + XXX m (horizontal)
2. ✅ Ventiladores identificados: X un (vazão: XXX m³/h, pressão: XXX Pa, potência: XX CV)
3. ✅ Grelhas/difusores: XX un
4. ✅ Dampers corta-fogo: XX un
5. ✅ Dampers motorizados: XX un
6. ✅ Sensores de pressão: XX un

### Mudanças em relação a R01 (PREMISSAS → VALORES REAIS)

| Item | Premissa R01 | Valor Real R02 | Mudança |
|------|-------------|---------------|---------|
| Escadas pressurizadas | ⚠️ 2 un (estimativa) | ✅ X un (DXF) | +/- X |
| Vazão ventiladores | ⚠️ 8.000-12.000 m³/h | ✅ X.XXX m³/h (memorial) | Confirmado |
| Dutos verticais | ⚠️ 200 m (estimativa) | ✅ XXX m (DXF) | +/- X% |
| ...

### Incerteza Reduzida
- **R01:** ±30-50% (premissas)
- **R02:** ±5-10% (dados validados)

## 2. Quantitativos Extraídos (✅ VALIDADOS)

### 2.1 Ventiladores de Pressurização

| # | Item | Especificação | UN | QTD | Fonte | Observação |
|---|------|--------------|-----|-----|-------|------------|
| 1 | Ventilador centrífugo | Vazão: X.XXX m³/h, Pressão: XXX Pa, Potência: XX CV | un | ✅ X | DXF + memorial | Marca: XXXX, Modelo: XXXX |
...
```

---

## 📞 CONTATOS

### Projetista
- **Nome:** Rubens Alves
- **Disciplina:** Ventilação Mecânica
- **Arquivos a solicitar:**
  - RA_EVM_LEGAL_PROJETO_R05.dxf
  - Memorial descritivo (PDF)
  - Planilha de equipamentos (XLSX)

### Time Cartesian
- **Responsável pelo orçamento:** <NOME>
- **Canal Slack:** #custos-ia-paramétrico

---

## 🔄 HISTÓRICO DE PROCESSAMENTO

| Data | Ação | Resultado |
|------|------|-----------|
| 2026-03-20 | R00: Briefing com premissas (sem DXF) | Incerteza ±30% |
| 2026-03-20 | R01: Tentativa de extração automática do DWG | ❌ Falhou (arquivo binário) |
| TBD | R02: Processamento do DXF | ✅ A fazer (aguardando DXF) |

---

*Guia criado por Cartesiano (subagent) | 2026-03-20*

*💡 Este guia será executado automaticamente quando o DXF estiver disponível em `projetos/thozen-electra/dxf-ventilacao/`.*
