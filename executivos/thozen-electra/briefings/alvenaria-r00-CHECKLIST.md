# CHECKLIST TÉCNICO — Extração de Alvenaria | Thozen Electra

**Objetivo:** Guia passo a passo para preenchimento do briefing `alvenaria-r00.md` quando os arquivos DWG forem processados.

---

## 🔧 Pré-requisitos

### Ferramentas Necessárias
- [ ] **ODA File Converter** instalado (ou AutoCAD/BricsCAD)
- [ ] **Python 3.11+** com bibliotecas:
  - [ ] `ezdxf` (para processar DXF)
  - [ ] `openpyxl` (para gerar planilhas)
  - [ ] `ifcopenshell` (se houver IFCs complementares)

### Instalação Rápida
```bash
# ODA File Converter (macOS)
brew install --cask oda-file-converter

# Python libraries
pip3.11 install ezdxf openpyxl ifcopenshell
```

---

## 📋 Passo a Passo

### ETAPA 1 — Converter DWG para DXF

**Objetivo:** Converter os 18 arquivos DWG de alvenaria para formato DXF processável.

#### Comando (via ODA File Converter):
```bash
# Criar pasta de destino
mkdir -p "projetos/thozen-electra/projetos/03 ALVENARIA/dxf"

# Converter todos os DWGs
oda-file-converter \
  --input "projetos/thozen-electra/projetos/03 ALVENARIA/" \
  --output "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/" \
  --format DXF \
  --version R2018
```

#### Verificar Conversão:
- [ ] 18 arquivos DXF gerados em `projetos/thozen-electra/projetos/03 ALVENARIA/dxf/`
- [ ] Tamanho dos DXFs similar aos DWGs originais (±10%)
- [ ] Nenhum erro de conversão reportado

---

### ETAPA 2 — Extrair Legendas e Especificações

**Objetivo:** Identificar tipos de blocos, espessuras, e padrões de representação nas pranchas.

#### Ação Manual (abrir 1 prancha exemplo no AutoCAD/BricsCAD):
1. Abrir `RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dwg` (pavimento tipo)
2. Verificar **legenda** na prancha:
   - [ ] Tipo de blocos especificados (ex: "Bloco cerâmico 09×19×19")
   - [ ] Cores/hatches de cada tipo de bloco
   - [ ] Espessuras de paredes (cotas)
3. Verificar **símbolos** utilizados:
   - [ ] Vergas (símbolo típico: linha tracejada sobre vão)
   - [ ] Contravergas (símbolo típico: linha tracejada sob vão)
   - [ ] Juntas de dilatação (símbolo típico: "JD" ou linha dupla)

#### Registrar no Briefing:
Editar `alvenaria-r00.md`, seção **2.2 Tipos de Alvenaria Esperados**, substituir por dados reais.

---

### ETAPA 3 — Processar DXF com Script Python

**Objetivo:** Extrair áreas de alvenaria, comprimentos de paredes, vãos de portas/janelas.

#### Script Base (salvar como `scripts/extrair_alvenaria_dxf.py`):
```python
import ezdxf
import sys

def extrair_alvenaria(dxf_path):
    """Extrai áreas de alvenaria de um arquivo DXF."""
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    # Inicializar contadores
    areas_hatch = {}
    comprimentos_polyline = {}
    
    # Processar HATCHs (áreas de alvenaria)
    for hatch in msp.query('HATCH'):
        layer = hatch.dxf.layer
        area = hatch.dxf.get('area', 0)  # Área do hatch (se disponível)
        if area > 0:
            if layer not in areas_hatch:
                areas_hatch[layer] = 0
            areas_hatch[layer] += area
    
    # Processar POLYLINEs (comprimentos de paredes)
    for polyline in msp.query('LWPOLYLINE'):
        layer = polyline.dxf.layer
        comprimento = polyline.get_length()
        if layer not in comprimentos_polyline:
            comprimentos_polyline[layer] = 0
        comprimentos_polyline[layer] += comprimento
    
    return areas_hatch, comprimentos_polyline

if __name__ == "__main__":
    dxf_file = sys.argv[1]
    areas, comps = extrair_alvenaria(dxf_file)
    
    print(f"\n=== ANÁLISE: {dxf_file} ===\n")
    print("ÁREAS (por layer):")
    for layer, area in sorted(areas.items()):
        print(f"  {layer}: {area:.2f} m²")
    
    print("\nCOMPRIMENTOS (por layer):")
    for layer, comp in sorted(comps.items()):
        print(f"  {layer}: {comp:.2f} m")
```

#### Executar para cada pavimento:
```bash
# Térreo
python3.11 scripts/extrair_alvenaria_dxf.py "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dxf"

# G1
python3.11 scripts/extrair_alvenaria_dxf.py "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dxf"

# ... (repetir para todos os 9 pavimentos distintos)
```

#### Registrar Resultados:
- [ ] Preencher tabela **3.1 Alvenaria por Pavimento** em `alvenaria-r00.md`
- [ ] Validar áreas (comparar pavimentos similares, ex: G1 vs G2)

---

### ETAPA 4 — Extrair Vãos de Portas e Janelas

**Objetivo:** Contar vãos para calcular vergas e contravergas.

#### Ação Manual (ou via script):
1. Abrir prancha no AutoCAD
2. Contar **portas** (blocos/símbolos de porta):
   - [ ] Pavimento Térreo: ___ portas
   - [ ] G1 a G5: ___ portas cada
   - [ ] Lazer: ___ portas
   - [ ] Tipo (08~31): ___ portas (×24)
   - [ ] Res/Cob: ___ portas
3. Contar **janelas** (blocos/símbolos de janela):
   - [ ] Pavimento Térreo: ___ janelas
   - [ ] G1 a G5: ___ janelas cada
   - [ ] Lazer: ___ janelas
   - [ ] Tipo (08~31): ___ janelas (×24)
   - [ ] Res/Cob: ___ janelas
4. Medir **largura de cada vão** (ou usar larguras típicas):
   - Portas: 80 cm, 90 cm, 120 cm (dupla)
   - Janelas: 100 cm, 120 cm, 150 cm, etc.

#### Cálculo de Vergas/Contravergas:
```
Comprimento da verga = Largura do vão + 0,60 m (30 cm cada lado)
Comprimento da contraverga = Largura do vão + 0,60 m (30 cm cada lado)
```

#### Registrar Resultados:
- [ ] Preencher tabela **3.3 Vergas e Contravergas** em `alvenaria-r00.md`

---

### ETAPA 5 — Calcular Encunhamento

**Objetivo:** Calcular comprimento total de topo de paredes (interface alvenaria × laje).

#### Método 1 — Via DXF (perímetro de paredes):
```python
# No script extrair_alvenaria_dxf.py, adicionar:
def calcular_encunhamento(dxf_path):
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    
    comprimento_total = 0
    for polyline in msp.query('LWPOLYLINE'):
        if 'ALV' in polyline.dxf.layer.upper() or 'PAREDE' in polyline.dxf.layer.upper():
            comprimento_total += polyline.get_length()
    
    return comprimento_total
```

#### Método 2 — Estimativa (se não for possível processar):
```
Encunhamento ≈ Perímetro externo + Perímetro interno das unidades + Paredes internas
```

#### Registrar Resultados:
- [ ] Preencher tabela **3.5 Encunhamento** em `alvenaria-r00.md`

---

### ETAPA 6 — Calcular Quantidades de Blocos

**Objetivo:** Converter área de alvenaria (m²) em quantidade de blocos (un).

#### Fórmula:
```
Quantidade de blocos = (Área de alvenaria × 1.05) / Área unitária do bloco
```

Onde:
- `1.05` = fator de perdas (5%)
- Área unitária do bloco:
  - Cerâmico 09×19×19: **0,0361 m²/bloco** (19 cm × 19 cm)
  - Cerâmico 14×19×19: **0,0361 m²/bloco**
  - Concreto 09×19×39: **0,0741 m²/bloco** (19 cm × 39 cm)
  - Concreto 14×19×39: **0,0741 m²/bloco**

#### Registrar Resultados:
- [ ] Preencher tabela **3.2 Blocos Cerâmicos** em `alvenaria-r00.md`

---

### ETAPA 7 — Validar Quantitativos

**Objetivo:** Verificar coerência dos dados extraídos.

#### Checklist de Validação:
- [ ] **Pavimentos tipo (08~31)** têm áreas similares? (±5%)
- [ ] **Garagens (G1~G5)** têm áreas similares? (±10%)
- [ ] **Área total de alvenaria** é coerente com benchmark?
  - Benchmark residencial vertical: **0,8 a 1,5 m² alvenaria / m² de AC**
  - Exemplo: Se AC total = 10.000 m², espera-se 8.000 a 15.000 m² de alvenaria
- [ ] **Comprimento de vergas** ≈ **2% a 5%** do comprimento total de paredes?
- [ ] **Encunhamento** ≈ **Comprimento total de paredes** (aproximadamente)?

#### Comparar com Base Cartesian:
```bash
# Se disponível, comparar com projetos similares:
grep -r "alvenaria" parametrico/indices/*.md
```

---

### ETAPA 8 — Gerar Planilha Excel

**Objetivo:** Criar planilha executiva compatível com Memorial Cartesiano.

#### Script Base (salvar como `scripts/gerar_planilha_alvenaria.py`):
```python
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill

def gerar_planilha_alvenaria(dados, output_path):
    """Gera planilha Excel de alvenaria."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "09 ALVENARIA"
    
    # Cabeçalho
    headers = ["Código", "Descrição", "UN", "QTD", "Preço Unit.", "Total", "Observação"]
    ws.append(headers)
    
    # Estilizar cabeçalho
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    # Preencher dados (exemplo)
    ws.append(["09.01", "ALVENARIA DE VEDAÇÃO", "", "", "", "", ""])
    ws.append(["09.01.01", "Blocos Cerâmicos 09×19×19", "un", dados.get("blocos_09", 0), "", "", ""])
    ws.append(["09.01.02", "Blocos Cerâmicos 14×19×19", "un", dados.get("blocos_14", 0), "", "", ""])
    # ... (adicionar mais linhas conforme necessário)
    
    # Salvar
    wb.save(output_path)
    print(f"Planilha salva: {output_path}")

# Exemplo de uso:
dados = {
    "blocos_09": 50000,
    "blocos_14": 30000,
    # ... (adicionar mais dados)
}
gerar_planilha_alvenaria(dados, "executivo/thozen-electra/planilhas/alvenaria-r01.xlsx")
```

#### Executar:
```bash
python3.11 scripts/gerar_planilha_alvenaria.py
```

#### Registrar:
- [ ] Planilha salva em `executivo/thozen-electra/planilhas/alvenaria-r01.xlsx`
- [ ] Upload no Slack via `slack_uploader.py`

---

### ETAPA 9 — Atualizar Briefing para R01

**Objetivo:** Revisar briefing com dados reais e marcar como R01 (validado).

#### Ações:
- [ ] Substituir todos os `[A EXTRAIR]` por valores reais
- [ ] Substituir todos os `[A CALCULAR]` por totais calculados
- [ ] Atualizar seção **7. Changelog** com nova entrada R01
- [ ] Atualizar seção **4.1 Arquivos Processados** com status ✅ PROCESSADO
- [ ] Revisar seção **5. Observações** — remover itens faltantes que foram resolvidos

#### Renomear Arquivo:
```bash
# Opcional: manter R00 como histórico
cp executivo/thozen-electra/briefings/alvenaria-r00.md executivo/thozen-electra/briefings/alvenaria-r00-ORIGINAL.md

# Atualizar para R01
mv executivo/thozen-electra/briefings/alvenaria-r00.md executivo/thozen-electra/briefings/alvenaria-r01.md
```

---

### ETAPA 10 — Upload e Apresentação no Slack

**Objetivo:** Entregar planilha e briefing atualizado ao time.

#### Comando de Upload:
```bash
# Upload da planilha (LEMBRAR: --thread E --channel são OBRIGATÓRIOS)
python3.11 scripts/slack_uploader.py \
  --bot cartesiano \
  --file executivo/thozen-electra/planilhas/alvenaria-r01.xlsx \
  --thread <thread_ts> \
  --channel <channel_id> \
  --comment "Planilha executiva de alvenaria — Thozen Electra R01"

# Upload do briefing atualizado (opcional)
python3.11 scripts/slack_uploader.py \
  --bot cartesiano \
  --file executivo/thozen-electra/briefings/alvenaria-r01.md \
  --thread <thread_ts> \
  --channel <channel_id> \
  --comment "Briefing atualizado — Alvenaria R01"
```

#### Mensagem de Apresentação (copiar para o Slack):
```
🏗️ *Planilha de Alvenaria — Thozen Electra R01*

*Quantitativos principais:*
• Área total de alvenaria: XXX.XXX m²
• Blocos cerâmicos 09×19: XXX.XXX un
• Blocos cerâmicos 14×19: XXX.XXX un
• Vergas: XXX m
• Contravergas: XXX m
• Encunhamento: XXX m

*Fontes:*
• 18 pranchas DWG processadas (R01)
• Cruzamento com arquitetura para pé-direito

*Próximos passos:*
• Validação do time
• Incorporação ao Memorial Cartesiano
• Precificação via base Cartesian
```

---

## ✅ Checklist Final

Antes de considerar a extração completa:

- [ ] **ETAPA 1** — DWG convertidos para DXF
- [ ] **ETAPA 2** — Legendas e especificações identificadas
- [ ] **ETAPA 3** — Áreas de alvenaria extraídas por pavimento
- [ ] **ETAPA 4** — Vãos contados, vergas/contravergas calculadas
- [ ] **ETAPA 5** — Encunhamento calculado
- [ ] **ETAPA 6** — Quantidade de blocos calculada
- [ ] **ETAPA 7** — Quantitativos validados (benchmarks, coerência)
- [ ] **ETAPA 8** — Planilha Excel gerada
- [ ] **ETAPA 9** — Briefing atualizado para R01
- [ ] **ETAPA 10** — Upload no Slack e apresentação ao time

---

## 🔗 Arquivos de Referência

- **Briefing original:** `executivo/thozen-electra/briefings/alvenaria-r00.md`
- **Resumo:** `executivo/thozen-electra/briefings/alvenaria-r00-RESUMO.md`
- **Checklist (este arquivo):** `executivo/thozen-electra/briefings/alvenaria-r00-CHECKLIST.md`
- **Script de extração:** `scripts/extrair_alvenaria_dxf.py` (a criar)
- **Script de planilha:** `scripts/gerar_planilha_alvenaria.py` (a criar)

---

**FIM DO CHECKLIST**

---

**Responsável:** Cartesiano (subagent `extração-alvenaria-electra`)  
**Data:** 2026-03-20 10:33 BRT
