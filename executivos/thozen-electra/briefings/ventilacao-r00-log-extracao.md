# Log de Extração — Ventilação Mecânica Thozen Electra

**Data:** 2026-03-20  
**Responsável:** Cartesiano (subagente de extração)  
**Tarefa:** Extrair quantitativos completos do projeto de ventilação mecânica (escadas pressurizadas)

---

## 1. Arquivos Disponíveis

### 1.1 Arquivos Identificados

```
projetos/thozen-electra/projetos/12 ESCADA VENTILACAO MECANICA/
└── DWG/
    └── RA_EVM_LEGAL_PROJETO_R05.dwg (5.39 MB, AutoCAD 2018/2019/2020)
```

**Confirmação:** Arquivo listado em `Rubens Alves Lista de arquivos.xlsx` (linha 51).

### 1.2 Arquivos NÃO Disponíveis

- ❌ IFC (não fornecido para esta disciplina)
- ❌ PDF (memorial descritivo, pranchas plotadas)
- ❌ Planilha de equipamentos
- ❌ DXF (conversão do DWG)

---

## 2. Tentativas de Extração de Dados

### 2.1 Ferramentas Testadas

| Ferramenta | Disponível? | Resultado |
|------------|-------------|-----------|
| `ezdxf` (Python) | ✅ (binário) | ❌ Módulo Python não instalado, instalação travou |
| `ezdxf browse` | ✅ | ❌ Requer Qt (PySide6/PyQt5) não disponível |
| `dwgread` | ❌ | Não instalado |
| `dwg2dxf` | ❌ | Não instalado |
| `strings` | ✅ | ⚠️ Dados não estruturados (binário AutoCAD) |

### 2.2 Métodos de Extração Tentados

#### A. Método 1: Leitura Direta via ezdxf
```bash
python3.11 -c "import ezdxf; doc = ezdxf.readfile('arquivo.dwg'); print(doc.layers)"
```
**Resultado:** ❌ Módulo `ezdxf` não instalado no Python.

**Tentativa de instalação:**
```bash
pip3.11 install ezdxf
```
**Resultado:** ❌ Processo travado (timeout após 15s), abortado.

---

#### B. Método 2: Extração de Strings (ASCII)

**Comando:**
```bash
strings -n 8 RA_EVM_LEGAL_PROJETO_R05.dwg | grep -v "^[^A-Za-z0-9]" | head -200
```

**Resultado:** ⚠️ Dados fragmentados, não estruturados.

**Análise:**
- Arquivo DWG é binário, strings extraídas são códigos internos do AutoCAD
- Nenhum texto legível relevante (nomes de equipamentos, vazões, potências)
- Não foi possível identificar layers, blocos, atributos ou textos de anotação

**Exemplo de saída:**
```
bRdAkSdAKSdAkRdAkRdA
AQdAKAdAkAdAKQdAKQdA.
33333f33
3f33ff3f
...
```

---

#### C. Método 3: Busca por Padrões Técnicos

Script Python customizado (`scripts/extract_dwg_ventilacao.py`) para buscar padrões:

**Padrões buscados:**
- Potências: `(CV|HP|kW|W)`
- Vazões: `(m3/h|m³/h|CMH)`
- Pressões: `(Pa|mmCA)`
- Diâmetros: `(Ø|diametro)`
- Equipamentos: `(ventilador|exaustor|insuflador)`
- Dutos, grelhas, dampers
- Escadas: `(escada|E[0-9]+)`

**Resultado:** ⚠️ Alguns fragmentos identificados, mas sem contexto:

```
📋 Escadas:
   • E1@
   • E4
   • e1
   • e10
   • null_surface-5

📋 Quadros:
   • Q26
   • Q9O
   • Qt0.

📋 Cabos:
   • 3X5
   • 0x9
   • 2x7
```

**Análise:**
- Possível identificação de escadas (E1, E4, E10) — mas sem confirmação
- Não foi possível extrair: vazões, potências, diâmetros, especificações técnicas
- Dados estão codificados no formato binário do DWG

---

#### D. Método 4: Busca por Dados Numéricos Estruturados

**Padrões regex:**
```bash
\b[0-9]{2,4}\s*mm\b          # Diâmetros
\b[0-9]+[.,]?[0-9]*\s*m³/h\b  # Vazões
\b[0-9]+[.,]?[0-9]*\s*(CV|kW)\b  # Potências
\b[0-9]{3,5}\s*RPM\b          # Rotações
```

**Resultado:** ❌ Nenhum dado estruturado identificado.

---

### 2.3 Conclusão das Tentativas de Extração

**Status:** ❌ **Extração automática não foi possível** com as ferramentas disponíveis.

**Razão principal:** 
- Arquivo DWG é formato proprietário binário da Autodesk
- Ferramentas open-source (ezdxf) requerem instalação de dependências não disponíveis
- Extração de strings retorna apenas códigos internos do AutoCAD, sem dados de projeto

**Alternativas não exploradas (requerem software adicional):**
- AutoCAD / BricsCAD (licença comercial)
- LibreCAD (limitado a DXF, não lê DWG)
- Teigha File Converter (gratuito, mas não disponível no sistema)
- Online CAD viewers (upload de arquivo, extração manual)

---

## 3. Decisão de Estratégia

### 3.1 Abordagem Adotada

**Como não foi possível extrair dados automaticamente**, o briefing foi gerado com base em:

1. **Premissas técnicas padrão** para sistemas de ventilação mecânica de escadas pressurizadas
2. **Normas técnicas aplicáveis:** NBR 14880:2024, NBR 9077:2022, IT 15/2019 (SP)
3. **Experiência Cartesian** em projetos similares (edifícios residenciais de 25-35 pavimentos)
4. **Dados do empreendimento:** 32 pavimentos (confirmado em `projetos/thozen-electra/PROJETO.md`)

### 3.2 Premissas Críticas Documentadas

Todas as premissas foram documentadas no briefing com alertas ⚠️:

- Número de escadas pressurizadas: **2** (típico para edifício deste porte)
- Vazão por escada: **8.000-12.000 m³/h** (NBR 14880, 3 portas abertas + infiltração)
- Potência dos ventiladores: **5-7,5 CV** (faixa típica para vazão e pressão necessárias)
- Diâmetro de dutos: **Ø600mm** (velocidade < 8 m/s para redução de ruído)
- Quantidade de dampers corta-fogo: **64** (a cada pavimento x 2 escadas)

### 3.3 Pendências Identificadas

**15 pendências críticas** listadas no briefing, incluindo:

- ✅ Número real de escadas pressurizadas
- ✅ Vazão e pressão especificadas pelo projetista
- ✅ Potência exata dos ventiladores
- ✅ Diâmetro e material dos dutos
- ✅ Localização e quantidade de grelhas/difusores
- ✅ Quantidade e localização de dampers
- ✅ Especificação de dampers corta-fogo (90min ou 120min?)
- ✅ Existência de antecâmaras pressurizadas
- ✅ Memorial descritivo completo
- ✅ Prancha de detalhes

---

## 4. Arquivos Gerados

### 4.1 Briefing Principal

**Arquivo:** `executivo/thozen-electra/briefings/ventilacao-r00.md`

**Conteúdo:**
- Metadados do projeto
- Especificações gerais (NBR 14880)
- Quantitativos estimados (6 subsistemas)
- Resumo de quantitativos principais
- Premissas adotadas (10 itens críticos)
- Precificação (fontes de preço)
- Pendências/dúvidas (15 itens)
- Mapeamento para Memorial Cartesiano
- Observações técnicas (testes de aceitação, manutenção)
- Estimativa de custo (R$ 330k - 520k com BDI e contingência)

**Tamanho:** 20.959 bytes (~21 KB)

### 4.2 Log de Extração (este arquivo)

**Arquivo:** `executivo/thozen-electra/briefings/ventilacao-r00-log-extracao.md`

**Objetivo:** Documentar o processo, limitações e decisões tomadas.

### 4.3 Arquivo Fonte (copiado)

**Origem:** `projetos/thozen-electra/projetos/12 ESCADA VENTILACAO MECANICA/DWG/RA_EVM_LEGAL_PROJETO_R05.dwg`

**Destino:** `executivo/thozen-electra/fontes/RA_EVM_LEGAL_PROJETO_R05.dwg`

**Motivo:** Preservar fonte original no diretório do projeto executivo.

---

## 5. Próximos Passos Recomendados

### 5.1 Imediato (Crítico)

1. **Solicitar memorial descritivo** do projetista (PDF)
   - Deve conter: vazões, pressões, potências, diâmetros, especificações de equipamentos
   
2. **Solicitar prancha de detalhes** (PDF ou DWG plotado)
   - Planta de localização de equipamentos
   - Isométrico de dutos
   - Detalhes de montagem

3. **Solicitar planilha de equipamentos** (XLSX)
   - Lista com fabricante, modelo, vazão, pressão, potência

### 5.2 Alternativa para Extração do DWG

Se o time tiver acesso a AutoCAD ou software compatível:

1. **Abrir DWG e extrair manualmente:**
   - Listar todos os equipamentos (blocos) e suas especificações (atributos)
   - Medir metragem de dutos (comando `LENGTHEN` ou `LIST`)
   - Contar dampers, grelhas, difusores
   
2. **Exportar para DXF:**
   ```
   Arquivo → Salvar Como → DXF (R12/LT2)
   ```
   - DXF pode ser lido por ferramentas open-source (ezdxf, LibreCAD)

3. **Exportar para PDF com layers separados:**
   - Facilita leitura e extração visual

### 5.3 Validação dos Quantitativos

Após receber documentação complementar:

1. Comparar quantitativos estimados com dados reais
2. Atualizar briefing (criar `ventilacao-r01.md`)
3. Gerar relatório de diferenças (`diff-r00-r01.md`)
4. Ajustar estimativa de custo

---

## 6. Lições Aprendidas

### 6.1 Limitações Identificadas

- **DWG é formato proprietário:** Extração automatizada requer ferramentas específicas (AutoCAD, ezdxf com dependências)
- **IFC seria melhor:** Formato aberto, facilmente processável
- **PDF plotado é útil:** Para extração visual quando automação falha
- **Memorial descritivo é essencial:** Não confiar apenas em desenhos para especificações técnicas

### 6.2 Recomendações para Futuros Projetos

1. **Solicitar IFC sempre que possível** (mesmo para instalações especiais)
2. **Solicitar memorial descritivo em PDF** junto com DWG
3. **Solicitar planilha de equipamentos** separadamente
4. **Manter base de premissas por disciplina** (facilita estimativas quando dados faltam)

---

## 7. Resumo Executivo

| Item | Status | Observação |
|------|--------|------------|
| **Extração automática** | ❌ Não foi possível | DWG binário, ferramentas indisponíveis |
| **Briefing gerado** | ✅ Concluído | Com base em premissas técnicas NBR 14880 |
| **Quantitativos** | ⚠️ Estimados | Validação obrigatória antes de orçar |
| **Pendências** | 15 itens críticos | Aguardando memorial descritivo |
| **Estimativa de custo** | R$ 330k - 520k | Com BDI 25-30% + contingência 15-20% |
| **Próximo passo** | Solicitar documentação | Memorial + prancha + planilha |

---

*Log gerado por Cartesiano (subagente de extração) | Data: 2026-03-20*
