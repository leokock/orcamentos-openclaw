# Instruções de Extração — AR-CONDICIONADO Thozen Electra

**Data:** 20/03/2026  
**Arquivo fonte:** `projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg`  
**Status:** 🚧 PENDENTE — Aguardando conversão DWG → DXF

---

## Problema Identificado

O arquivo DWG está em formato binário nativo do AutoCAD, que não é suportado por ferramentas open-source de leitura (ezdxf, dxfgrabber). Tentativa de leitura resultou em:

```
❌ Erro: File 'RA_ARC_EXE_00_TODAS CAD_R05.dwg' is not a DXF file.
```

---

## Soluções Disponíveis

### Solução 1: Converter DWG → DXF (RECOMENDADO)

#### Opção 1.1: ODA File Converter (gratuito, mais confiável)

**Download:** https://www.opendesign.com/guestfiles/oda_file_converter

**Instalação (macOS):**
```bash
# Baixar o instalador .dmg
# Montar e instalar normalmente
# Executar via linha de comando:
/Applications/ODAFileConverter.app/Contents/MacOS/ODAFileConverter \
  "projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg" \
  "output" \
  "ACAD2018" \
  "DXF" \
  "0" \
  "1"
```

**Instalação (Linux/VPS):**
```bash
# Baixar versão Linux
wget https://download.opendesign.com/guestfiles/ODAFileConverter/ODAFileConverter_QT6_lnxX64_8.3dll_25.12.tar.gz
tar -xzf ODAFileConverter_QT6_lnxX64_8.3dll_25.12.tar.gz
cd ODAFileConverter_*/

# Executar
./ODAFileConverter \
  "/caminho/para/RA_ARC_EXE_00_TODAS CAD_R05.dwg" \
  "/caminho/output" \
  "ACAD2018" \
  "DXF" \
  "0" \
  "1"
```

#### Opção 1.2: LibreCAD (open-source)

```bash
# Instalar (macOS)
brew install --cask librecad

# Abrir arquivo
open -a LibreCAD "projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg"

# Menu: File → Export → DXF
# Salvar como: RA_ARC_EXE_00_TODAS CAD_R05.dxf
```

#### Opção 1.3: AutoCAD (comercial)

```bash
# Abrir no AutoCAD
# File → Save As → AutoCAD DXF (*.dxf)
# Versão: AutoCAD 2018 DXF
```

---

### Solução 2: Solicitar Arquivo ao Projetista

**Email sugerido:**

```
Assunto: Thozen Electra — Solicitação de arquivo DXF (Ar-Condicionado)

Olá [Nome do Projetista],

Estamos orçando o projeto Thozen Electra e precisamos processar o arquivo de 
ar-condicionado (RA_ARC_EXE_00_TODAS CAD_R05.dwg) para extração automatizada 
de quantitativos.

Nosso sistema de processamento trabalha com arquivos DXF. Poderia nos enviar 
o arquivo nesse formato?

Alternativamente, se tiver uma planilha de quantitativos ou memorial descritivo 
com lista de equipamentos, também seria muito útil.

Obrigado!
```

---

### Solução 3: Solicitar Planilha de Quantitativos

Se o projetista já tiver levantamento pronto:

**Informações necessárias:**
1. **Equipamentos:**
   - Lista de condensadoras (potência BTU/h, local de instalação)
   - Lista de evaporadoras (potência BTU/h, ambiente, pavimento)
   - Sistemas VRF (se aplicável)

2. **Tubulações:**
   - Metragem de tubulação frigorífica por diâmetro (1/4", 3/8", 1/2", 5/8", 3/4")
   - Metragem de linhas de dreno (DN20, DN25)

3. **Elétrica:**
   - Metragem de cabos por bitola
   - Quantidade de disjuntores
   - Metragem de eletrodutos

4. **Acessórios:**
   - Quantidade de suportes
   - Quantidade de abraçadeiras
   - Quantidade de registros, grelhas, etc.

---

## Após Conversão: Extração Automatizada

### Passo 1: Executar Script de Extração

```bash
# Com o arquivo DXF disponível:
python3.11 scripts/extrair_ar_condicionado_dwg.py "caminho/para/arquivo.dxf"
```

**Saída esperada:**
- Lista de layers do arquivo
- Blocos encontrados (equipamentos) com quantidade
- Textos relevantes (especificações, potências)
- Metragem de tubulações por layer
- Relatório consolidado

### Passo 2: Analisar Layers

O script irá listar todos os layers. Layers típicos de ar-condicionado:

| Layer Típico | Conteúdo Esperado |
|--------------|-------------------|
| `AC_EQUIPAMENTOS` | Blocos de condensadoras e evaporadoras |
| `AC_TUBULACAO`, `AC_FRIGORIFICA` | Linhas de tubulação frigorífica (cobre) |
| `AC_DRENO` | Linhas de drenagem (PVC) |
| `AC_ELETRICA` | Alimentação elétrica |
| `AC_TEXTOS`, `AC_COTAS` | Especificações técnicas |
| `AC_SIMBOLOS` | Legendas, símbolos |

**⚠️ Importante:** Os nomes de layers variam por escritório. Procurar por:
- Palavras-chave: `AC`, `COND`, `CLIMA`, `HVAC`, `AR`, `FRIG`, `DRENO`
- Prefixos: `14_` (número da disciplina)

### Passo 3: Extrair Blocos (Equipamentos)

O script identifica blocos automaticamente. Blocos típicos:

| Nome do Bloco | Equipamento |
|---------------|-------------|
| `SPLIT_9000`, `COND_9K` | Condensadora 9.000 BTU/h |
| `EVAP_12000`, `SPLIT_12K` | Evaporadora 12.000 BTU/h |
| `VRF_COND`, `VRF_OUTDOOR` | Condensadora VRF |
| `VRF_EVAP`, `CASSETE`, `PISO_TETO` | Evaporadora VRF |

**Ação:** Correlacionar nome do bloco → potência → tipo de equipamento

### Passo 4: Extrair Textos (Especificações)

O script filtra textos com palavras-chave:
- `BTU`, `KW`, `TR` → Potências
- `SPLIT`, `VRF`, `COND`, `EVAP` → Tipos de equipamento
- Números (especialmente 4-5 dígitos) → Podem ser potências

**Ação:** Correlacionar textos → blocos próximos → confirmar especificações

### Passo 5: Calcular Metragens de Tubulações

O script calcula automaticamente comprimento de:
- Linhas (`LINE`)
- Polilinhas (`LWPOLYLINE`, `POLYLINE`)

**Filtragem por layer:**
- Tubulações frigoríficas: layers com `AC`, `FRIG`, `TUB`, `COND`
- Drenos: layers com `DRENO`, `DRAIN`

**⚠️ Atenção:** 
- Valores em unidades do DWG (geralmente mm)
- Converter para metros: `valor_mm / 1000`

### Passo 6: Preencher Briefing

Com os dados extraídos, preencher as tabelas em:
- `executivo/thozen-electra/briefings/ar-condicionado-r00.md`

**Seções a preencher:**
- 3.1 Equipamentos de Climatização
- 3.2 Tubulações Frigoríficas
- 3.3 Linhas de Dreno
- 3.4 Instalações Elétricas Associadas
- 3.5 Suportes e Acessórios
- 4.1 a 4.5 Organização por Pavimento

---

## Extração Manual (Se Script Falhar)

### 1. Abrir DXF em Visualizador

```bash
# LibreCAD (gratuito)
brew install --cask librecad
open -a LibreCAD "arquivo.dxf"

# OU DraftSight (gratuito, mais completo)
# Download: https://www.draftsight.com/
```

### 2. Habilitar Todos os Layers

**LibreCAD:**
- Menu: View → Layer List
- Clicar nos ícones de "olho" para mostrar todos os layers

**DraftSight:**
- Menu: Tools → Layers → Layer Manager
- Marcar todos como "On" e "Thawed"

### 3. Identificar Equipamentos (Blocos)

**Contar blocos manualmente:**
1. Ativar layer de equipamentos (ex: `AC_EQUIPAMENTOS`)
2. Usar ferramenta de seleção (Select)
3. Filtrar por tipo de bloco: `Tools → Quick Select → Block Name`
4. Contar quantidade selecionada

**Ler especificações:**
- Clicar duas vezes no bloco → ver atributos
- OU ler textos próximos aos blocos

### 4. Medir Tubulações

**LibreCAD:**
```
Tools → Measure → Distance
# OU
Tools → Measure → Total Length (selecionar todas as linhas)
```

**DraftSight:**
```
Tools → Inquiry → Distance
# OU
Tools → Inquiry → List (selecionar linha → ver Length)
```

**Para medir todas as tubulações de um layer:**
1. Isolar o layer (deixar só ele visível)
2. Selecionar todas as linhas: `Edit → Select All` (Ctrl+A)
3. Usar comando `LIST` ou ferramenta de medição
4. Somar comprimentos manualmente OU exportar lista para Excel

### 5. Extrair Tabelas (Se Houver Legenda)

Alguns projetos incluem tabela de equipamentos na prancha:
- Procurar por bloco de título ou legenda
- Copiar manualmente para Excel
- Conferir com contagem de blocos no desenho

---

## Checklist de Validação

Após extração (automatizada ou manual), validar:

- [ ] **Equipamentos:**
  - [ ] Quantidade de condensadoras bate com total de evaporadoras?
  - [ ] Potências fazem sentido? (9k, 12k, 18k, 24k, 30k BTU/h são comuns)
  - [ ] Localização por pavimento está correta?

- [ ] **Tubulações:**
  - [ ] Metragem de linha de gás ≈ metragem de linha de líquido?
  - [ ] Comprimento de dreno ≈ 80-100% do comprimento de tubulação frigorífica?
  - [ ] Prumadas: ~3m/pavimento × 34 pavimentos × qtd prumadas?

- [ ] **Elétrica:**
  - [ ] Quantidade de circuitos elétricos = quantidade de equipamentos?
  - [ ] Bitola de cabo compatível com potência do equipamento?

- [ ] **Organização:**
  - [ ] Quantitativos separados por pavimento?
  - [ ] Multiplicador aplicado para pavimentos tipo (×24)?
  - [ ] Térreo + Lazer + Casa de Máquinas separados?

---

## Estimativa de Tempo

| Método | Tempo Estimado | Complexidade |
|--------|----------------|--------------|
| Conversão DWG→DXF + Script automatizado | 30 min | Baixa |
| Extração manual (LibreCAD/DraftSight) | 4-8 horas | Média-Alta |
| Solicitar planilha ao projetista | 1-3 dias (prazo) | Baixa |

**Recomendação:** Priorizar conversão + script automatizado.

---

## Contato com Projetista

Se nenhuma solução técnica funcionar, solicitar ao projetista:

**Opção 1: Arquivo DXF**
- Mais rápido de processar
- Script automatizado funciona

**Opção 2: Planilha de quantitativos**
- Já consolidada pelo projetista
- Copiar direto para briefing

**Opção 3: Memorial descritivo**
- Especificações técnicas
- Premissas de projeto
- Ajuda a validar extração

---

## Arquivos Relacionados

- 📄 Briefing principal: `executivo/thozen-electra/briefings/ar-condicionado-r00.md`
- 🔧 Script de extração: `scripts/extrair_ar_condicionado_dwg.py`
- 📁 Arquivo fonte: `projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg`

---

*Instruções preparadas por Cartesiano | Atualizado: 20/03/2026*
