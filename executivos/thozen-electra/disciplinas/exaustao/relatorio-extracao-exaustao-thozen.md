# Relatório de Extração - Sistema de Exaustão (Churrasqueiras)
## Thozen Electra | 20/03/2026 10:56

---

## 📊 Status da Extração

**Arquivo DWG:** `RA_CHU_EXE_PROJETO_R00.dwg` (3.2 MB)  
**Formato:** AutoCAD 2018/2019/2020 (AC1032)  
**Status:** ❌ **EXTRAÇÃO NÃO CONCLUÍDA — CONVERSÃO NECESSÁRIA**

---

## 🔴 BLOQUEADOR CRÍTICO

O arquivo DWG está em formato binário proprietário (AC1032) que **não pode ser processado** com as ferramentas disponíveis:

1. ❌ **ezdxf (Python)** — rejeita formato binário: `File is not a DXF file`
2. ❌ **ezdxf.recover** — falha na leitura da estrutura: `DXFStructureError`
3. ❌ **LibreCAD** — instalação via Homebrew falhou (cask deprecated)
4. ❌ **Outros conversores CAD** — não instalados no ambiente (macOS arm64)

**Resultado:** Sem conversão DWG→DXF, **não é possível extrair dados reais do projeto**.

---

## 📋 Próximas Ações (CRÍTICAS)

### Para o Time Cartesian:

O briefing R01 foi gerado, mas **todos os quantitativos permanecem como premissas** (idênticos ao R00).

**Para completar a extração, o time precisa:**

### ✅ OPÇÃO 1: Conversão DWG → DXF (RECOMENDADA)

**Ferramentas gratuitas:**
- **ODA File Converter** (Windows/macOS/Linux)  
  Link: https://www.opendesign.com/guestfiles/oda_file_converter
  - Download → Instalar → Abrir → Selecionar DWG → Output: DXF AutoCAD 2018 → Convert

**Ferramentas pagas (se disponíveis):**
- AutoCAD, BricsCAD, DraftSight → Abrir DWG → "Salvar como" → DXF

**Após conversão:**
1. Enviar DXF no canal do Slack
2. Avisar: `@Cartesiano já enviei o DXF de exaustão`
3. Bot processará automaticamente → gera briefing R02 com dados reais

---

### ✅ OPÇÃO 2: PDF Plotado (ALTERNATIVA)

Se conversão DXF não for viável, plotar PDF com:
- ✅ Plantas baixas do pavimento lazer (churrasqueiras)
- ✅ Cortes/detalhes da prumada de exaustão
- ✅ Legendas e especificações técnicas VISÍVEIS
- ✅ Tabela de equipamentos (exaustores, coifas, dutos)

**Após gerar PDF:**
1. Enviar no Slack
2. Avisar: `@Cartesiano já enviei o PDF de exaustão`
3. Bot extrairá dados via OCR/análise visual

---

### ✅ OPÇÃO 3: Tabela Manual (ÚLTIMO RECURSO)

Preencher e enviar no Slack:

```
EQUIPAMENTOS:
- Exaustores: <qtd>, <vazão m³/h>, <potência CV>, <modelo>
- Coifas: <qtd>, <dimensões LxPxH>, <material>
- Churrasqueiras atendidas: <qtd>, <localização>

DUTOS:
- Horizontal: <metragem>, <diâmetro>
- Vertical (prumada): <metragem>, <diâmetro>
- Curvas/joelhos: <qtd>
- Dampers corta-fogo: <qtd>, <localização>

ELÉTRICA:
- Quadro de origem: <identificação>
- Cabos: <bitola>, <metragem>
- Proteções: <disjuntores>, <contatores>
- Controle: <manual/automático>
```

---

## 📄 Documentos Gerados

### 1. Briefing Atualizado
**Arquivo:** `executivo/thozen-electra/briefings/exaustao-r01.md`

**Conteúdo:**
- ⚠️ **Limitação documentada** — explica por que a extração falhou
- 📋 **Instruções detalhadas** para conversão DWG/PDF (3 opções)
- 📊 **Quantitativos mantidos como premissas** (idênticos ao R00)
- 💰 **Estimativa de custo preliminar** adicionada:
  - Cenário 1 (sistema centralizado): **R$ 58k - 110k**
  - Cenário 2 (sistema individualizado): **R$ 46k - 92k**
  - ⚠️ Margem de erro: **±30-50%** (sem dados reais)
- ✅ **Checklist de próximas ações** atualizado com status

---

### 2. Dados JSON (Vazio)
**Arquivo:** `output/thozen-electra-exaustao-dados-r00.json`

**Status:** Arquivo gerado, mas sem dados extraídos (estrutura vazia + erro de leitura).

---

## 🔍 O Que Foi Tentado

### 1. Leitura Direta com ezdxf
```python
doc = ezdxf.readfile(arquivo_dwg)
```
**Resultado:** `OSError: File is not a DXF file`

---

### 2. Modo de Recuperação (ezdxf.recover)
```python
doc, auditor = recover.readfile(arquivo_dwg)
```
**Resultado:** `DXFStructureError: Invalid group code at line 57`

---

### 3. Instalação de Conversores
- **LibreCAD:** Tentativa via `brew install --cask librecad`
  - **Resultado:** Falha de instalação (cask deprecated, erro de overwrite)
- **Outros conversores:** Não disponíveis no ambiente (macOS arm64)

---

### 4. Análise Binária do Arquivo
```bash
file RA_CHU_EXE_PROJETO_R00.dwg
# DWG AutoDesk AutoCAD 2018/2019/2020

head -c 100 RA_CHU_EXE_PROJETO_R00.dwg | od -c
# AC1032 (header identificado)
```

**Conclusão:** Formato proprietário binário — requer software CAD oficial para leitura.

---

## ❌ Dados NÃO Extraídos (Lista Completa)

1. ❌ Quantidade exata de churrasqueiras (estimativa: 2-4)
2. ❌ Dimensões das churrasqueiras
3. ❌ Layout das churrasqueiras no pavimento lazer
4. ❌ Vazão de projeto dos exaustores (estimativa: 8k-12k m³/h)
5. ❌ Potência dos motores (estimativa: 1,5-7,5 CV)
6. ❌ Diâmetros especificados dos dutos (estimativa: DN 300-400)
7. ❌ Metragem real de dutos horizontal (estimativa: 20-40m)
8. ❌ Metragem real de dutos vertical (estimativa: 70-90m)
9. ❌ Quantidade de curvas/joelhos/conexões
10. ❌ Tipo de controle (manual/automático)
11. ❌ Especificações elétricas detalhadas
12. ❌ Roteamento da prumada vertical
13. ❌ Ponto de descarga na cobertura
14. ❌ Integração com BMS/automação

---

## 📊 Dados Mantidos Como Premissas (R00 → R01)

Como não foi possível extrair dados reais, o briefing R01 **mantém as mesmas premissas** do R00:

### Equipamentos (Estimado):
- **Exaustores:** 1-2 UN (5-7,5 CV se centralizado, 1,5-2 CV se individual)
- **Coifas:** 2-4 UN (inox AISI 304, 1,20 x 0,80m)
- **Churrasqueiras atendidas:** 2-4 UN

### Dutos (Estimado):
- **Horizontal:** 20-40 m
- **Vertical:** 70-90 m
- **Diâmetro:** DN 300-400mm (galvanizado #24)

### Instalação Elétrica (Estimado):
- **Cabos:** 4-6mm², 80-200m
- **Proteções:** Disjuntores 16-32A, contatores, relés térmicos
- **Quadro:** Possível integração ao QD do lazer

### Controles (Estimado):
- **Básico:** Botoeiras liga/desliga
- **Opcional:** Sensores de temperatura/fumaça + CLP

---

## 💰 Estimativa de Custo (Preliminar)

**⚠️ Baseada em premissas — Margem de erro: ±30-50%**

| Cenário | Sistema | Estimativa (R$) |
|---------|---------|----------------|
| 1 | Centralizado (1 exaustor grande) | **58.000 - 110.000** |
| 2 | Individualizado (2-4 exaustores) | **46.000 - 92.000** |

**Após obter dados reais:** Margem de erro reduz para **±10-15%**

---

## ✅ Checklist de Próximas Ações

### Etapa 1: Obter Dados (BLOQUEADOR)
- [ ] **OPÇÃO A:** Converter DWG→DXF (ODA File Converter ou AutoCAD)
- [ ] **OPÇÃO B:** Plotar PDF com especificações técnicas
- [ ] **OPÇÃO C:** Preencher tabela manual com dados do projeto
- [ ] Enviar arquivo/dados no Slack → `@Cartesiano já enviei`
- [ ] Bot processa → atualiza briefing para R02

### Etapa 2: Compatibilização (Após Etapa 1)
- [ ] Cruzar com projeto elétrico (09) → alimentação, quadros, cabos
- [ ] Cruzar com arquitetura (02) → layout, interferências, acabamentos
- [ ] Cruzar com estrutura (01) → passagens, furos, reforços

### Etapa 3: Validação (Após Etapa 2)
- [ ] Confirmar: Sistema centralizado OU individualizado?
- [ ] Confirmar: Controle manual OU automático?
- [ ] Confirmar: Integração com BMS?

### Etapa 4: Planilha Executiva (Após Etapa 3)
- [ ] Gerar Excel com código Memorial (N1 14.08)
- [ ] Precificar com base em quantitativos reais
- [ ] Entregar ao time via Slack

---

## 🎯 Resumo para o Agente Principal

**Status:** ⚠️ **BLOQUEADO — Aguardando conversão DWG→DXF ou PDF plotado**

**O que foi feito:**
1. ✅ Localizado arquivo DWG original (3.2 MB)
2. ✅ Identificado formato AC1032 (AutoCAD 2018/2019/2020)
3. ✅ Tentado processamento com ezdxf (falhou — formato binário)
4. ✅ Tentado instalação de conversores (LibreCAD falhou)
5. ✅ Gerado briefing R01 com instruções detalhadas para o time
6. ✅ Documentado limitação e próximas ações
7. ✅ Adicionado estimativa preliminar de custo (±30-50%)

**O que falta:**
- 🔴 **Conversão DWG→DXF** (ou PDF plotado, ou tabela manual)
- 🟡 Extração de quantitativos reais
- 🟡 Validação de premissas com time de projetos
- 🟡 Geração de planilha executiva final

**Próximo passo:**
- Informar o time no canal Slack sobre a limitação
- Instruir: seguir opções descritas em `exaustao-r01.md`
- Aguardar envio de DXF/PDF/dados
- Processar quando arquivo estiver disponível

---

**Data:** 2026-03-20 10:56  
**Processado por:** Cartesiano (subagente)  
**Briefing atualizado:** `executivo/thozen-electra/briefings/exaustao-r01.md`
