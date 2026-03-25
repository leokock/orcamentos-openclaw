# Guia Rápido — Extração de Alvenaria | Thozen Electra

**Para:** Time Cartesian Engenharia  
**Objetivo:** Instruções práticas para processar os quantitativos de alvenaria

---

## 🚀 Como Processar os Arquivos de Alvenaria

### Opção 1 — Instalação de Ferramentas + Processamento Automático (RECOMENDADO)

#### Passo 1: Instalar ODA File Converter
```bash
# macOS (via Homebrew)
brew install --cask oda-file-converter

# Ou baixe manualmente de:
# https://www.opendesign.com/guestfiles/oda_file_converter
```

#### Passo 2: Converter DWG → DXF
```bash
oda-file-converter \
  --input "projetos/thozen-electra/projetos/03 ALVENARIA/" \
  --output "projetos/thozen-electra/projetos/03 ALVENARIA/dxf/" \
  --format DXF \
  --version R2018
```

#### Passo 3: Processar DXFs Automaticamente
```bash
./scripts/processar_todos_alvenaria.sh
```

#### Passo 4: Revisar Resultados
- **JSONs de quantitativos:** `executivo/thozen-electra/quantitativos/alvenaria/*.json`
- **Relatório consolidado:** `executivo/thozen-electra/quantitativos/alvenaria/relatorio-consolidado.md`

---

### Opção 2 — Processar Manualmente no AutoCAD

Se preferir extrair os dados manualmente:

#### A. Abrir Prancha no AutoCAD
1. Abrir `projetos/thozen-electra/projetos/03 ALVENARIA/RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dwg`
2. Verificar legendas e tipos de blocos

#### B. Extrair Áreas de Alvenaria
1. Selecionar hatches de alvenaria
2. Usar comando `LIST` ou `PROPERTIES` para ver área total
3. Anotar áreas por tipo de bloco

#### C. Contar Vãos (Portas/Janelas)
1. Contar blocos de portas e janelas
2. Medir largura de cada vão
3. Calcular:
   - Verga = Largura do vão + 0,60 m
   - Contraverga = Largura do vão + 0,60 m

#### D. Preencher Planilha Manual
Use o template: `executivo/thozen-electra/briefings/alvenaria-r00.md`  
Preencha as tabelas substituindo `[A EXTRAIR]` pelos valores.

---

### Opção 3 — Solicitar Arquivos DXF ou IFC

Mais simples: pedir ao projetista para exportar os DWGs em formato DXF ou IFC.

**Vantagens:**
- Não precisa instalar ferramentas
- DXF/IFC são processáveis automaticamente
- Reduz risco de erro de conversão

**Como pedir:**
> "Olá! Para facilitar a extração de quantitativos, poderia exportar as pranchas de alvenaria em formato DXF ou IFC? Isso acelera o processo de orçamentação. Obrigado!"

---

## 📋 Checklist de Dados a Extrair

### ✅ Obrigatórios (Prioridade ALTA)
- [ ] **Área total de alvenaria por pavimento** (m²)
- [ ] **Tipo de blocos especificados** (cerâmico 9×19, 14×19, etc.)
- [ ] **Espessura das paredes** (cm)

### 🟡 Importantes (Prioridade MÉDIA)
- [ ] **Quantidade de vãos** (portas + janelas)
- [ ] **Comprimento de vergas e contravergas** (m)
- [ ] **Encunhamento** (perímetro de topo de paredes)

### 🟢 Complementares (Prioridade BAIXA)
- [ ] **Juntas de dilatação** (se indicadas)
- [ ] **Drywall/divisórias** (se houver)
- [ ] **Especificações de argamassa** (memorial descritivo)

---

## 📊 Como Validar os Dados Extraídos

### 1. Comparar Pavimentos Similares
- **Garagens (G1 a G5)** devem ter áreas semelhantes (±10%)
- **Tipos (08 a 31)** são idênticos — área deve ser exatamente igual

### 2. Benchmark Residencial
```
Área de alvenaria ≈ 0,8 a 1,5 m² / m² de AC
```

**Exemplo:**  
- AC total do empreendimento = 10.000 m²
- Área de alvenaria esperada = 8.000 a 15.000 m²

### 3. Coerência de Vergas/Contravergas
```
Comprimento de vergas ≈ 2% a 5% do comprimento total de paredes
```

---

## 🎯 Pavimentos do Projeto

| Código | Pavimento | Repetições | Arquivo Base |
|--------|-----------|-----------|--------------|
| 01 | Térreo | 1x | RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dwg |
| 02 | G1 | 1x | RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dwg |
| 03 | G2 | 1x | RA_ALV_EXE_03_G2 PRÉ-EXECUTIVO_R01.dwg |
| 04 | G3 | 1x | RA_ALV_EXE_04_G3 PRÉ-EXECUTIVO_R01.dwg |
| 05 | G4 | 1x | RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dwg |
| 06 | G5 | 1x | RA_ALV_EXE_06_G5 PRÉ-EXECUTIVO_R01.dwg |
| 07 | Lazer | 1x | RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dwg |
| 08~31 | Tipo | **24x** | RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dwg |
| 32 | Res/Cob | 1x | RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dwg |

**⚠️ ATENÇÃO:** Pavimentos 08 a 31 são **24 repetições** do mesmo layout!

---

## 📁 Arquivos Importantes

| Arquivo | Descrição |
|---------|-----------|
| `briefings/alvenaria-r00.md` | Briefing completo — estrutura de tabelas a preencher |
| `briefings/alvenaria-r00-RESUMO.md` | Resumo executivo — limitações e próximos passos |
| `briefings/alvenaria-r00-CHECKLIST.md` | Checklist detalhado — passo a passo técnico |
| `scripts/extrair_alvenaria_dxf.py` | Script Python para processar DXF |
| `scripts/processar_todos_alvenaria.sh` | Script Bash para processar todos DXFs |

---

## 🆘 Problemas Comuns

### Erro: "ezdxf not found"
**Solução:**
```bash
pip3.11 install ezdxf
```

### Erro: "ODA File Converter not found"
**Solução:**
```bash
# macOS
brew install --cask oda-file-converter

# Ou baixe de https://www.opendesign.com/guestfiles/oda_file_converter
```

### Erro: "Nenhum arquivo DXF encontrado"
**Solução:**  
Execute primeiro a conversão DWG → DXF (Passo 2 da Opção 1)

### Arquivos DWG não abrem
**Solução:**  
Versão do AutoCAD pode ser incompatível. Use ODA File Converter para converter para versão mais antiga (R2018).

---

## 📞 Contato

Dúvidas ou problemas? Entre em contato:

- **Slack:** #custos-ia-paramétrico ou #ctn-team-comercial
- **Menção:** `@Cartesiano`

---

**TL;DR (Resumo Ultra Rápido):**

1. Instale ODA File Converter
2. Converta DWG → DXF
3. Execute `./scripts/processar_todos_alvenaria.sh`
4. Revise JSONs em `executivo/thozen-electra/quantitativos/alvenaria/`
5. Preencha briefing e gere planilha Excel

**Tempo estimado:** 30-60 minutos (após instalação das ferramentas)

---

**Última atualização:** 2026-03-20 10:33 BRT  
**Responsável:** Cartesiano (Cartesian Engenharia)
