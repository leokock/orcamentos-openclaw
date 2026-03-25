# 📋 Resumo Executivo - Exaustão Churrasqueiras | Thozen Electra

---

## ⚠️ STATUS DA EXTRAÇÃO

**🔴 LIMITAÇÃO CRÍTICA:** Não foi possível extrair quantitativos reais do arquivo DWG disponível.

**Arquivo fonte:** `RA_CHU_EXE_PROJETO_R00.dwg` (3.2 MB)  
**Problema:** Arquivo binário codificado — tentativas de extração via strings, parsing binário e análise heurística não retornaram dados técnicos legíveis.

---

## 📊 O QUE FOI ENTREGUE

✅ **Briefing completo** em: `executivo/thozen-electra/briefings/exaustao-r00.md`

**Conteúdo:**
1. ✅ Escopo e premissas técnicas (padrão NBR 14518)
2. ✅ Quantitativos estimados com base em projetos similares
3. ✅ Estrutura de tabelas para orçamento executivo
4. ✅ Identificação de interferências com outras disciplinas
5. ✅ Checklist de validações necessárias

**⚠️ TODOS os quantitativos estão marcados como "A CONFIRMAR COM DWG"**

---

## 🎯 PRÓXIMA AÇÃO OBRIGATÓRIA

**Para obter quantitativos reais, é necessário:**

### Opção 1: Converter DWG → DXF (RECOMENDADO)
```bash
# Usar ODA File Converter (free, oficial da Open Design Alliance)
# Download: https://www.opendesign.com/guestfiles/oda_file_converter
# Converter para DXF R2013 ou superior
```

Após conversão, rodar:
```bash
python3.11 scripts/process_dxf.py executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.dxf
```

---

### Opção 2: Gerar PDF Plotado
- Abrir DWG em AutoCAD/BricsCAD
- Plotar para PDF com escala legível
- Extrair manualmente:
  - Quantidade de churrasqueiras
  - Vazão dos exaustores
  - Diâmetros dos dutos
  - Metragens (horizontal + vertical)
  - Potências dos motores

---

### Opção 3: Revisão Manual no CAD
- Abrir `RA_CHU_EXE_PROJETO_R00.dwg` em software CAD
- Extrair diretamente do projeto:
  - Lista de materiais (se houver)
  - Tabela de quantidades
  - Especificações técnicas em blocos de texto
  - Dimensionamento de dutos e equipamentos

---

## 📦 QUANTITATIVOS ESTIMADOS (A VALIDAR)

### Principais Componentes

| Item | Estimativa | Unidade | Premissa |
|------|-----------|---------|----------|
| Churrasqueiras atendidas | 2-4 | UN | Típico para edifício de 24 pavtos |
| Exaustores centrífugos | 1-2 | UN | Depende se sistema é centralizado ou não |
| Vazão total do sistema | 8.000-12.000 | m³/h | NBR 14518: 2.000-3.000 m³/h por churrasqueira |
| Potência instalada | 5-10 | CV | Motores trifásicos 220/380V |
| Dutos (total) | 100-150 | m | 70-90m (vertical) + 20-40m (horizontal) |
| Coifas inox AISI 304 | 2-4 | UN | 1 por churrasqueira |
| Grelhas de ventilação | 4-8 | UN | Admissão de ar de compensação |

### Metragens Estimadas (⚠️ ALTO GRAU DE INCERTEZA)

| Tipo de Duto | Diâmetro/Seção | Metragem | Observação |
|--------------|---------------|----------|------------|
| Duto circular vertical | Ø300mm | 70-90m | Do lazer (7º pav) até cobertura |
| Duto retangular horizontal | 400x300mm | 20-40m | Trechos no lazer |
| Conexões (curvas, joelhos) | Vários | 8-20 UN | Mudanças de direção |

---

## 🔍 DADOS FALTANTES (CRÍTICOS)

**Não foi possível extrair do DWG:**

1. ❌ Quantidade exata de churrasqueiras
2. ❌ Dimensões das churrasqueiras (área de grelha)
3. ❌ Vazão especificada de cada exaustor (m³/h)
4. ❌ Pressão estática de projeto (mmCA)
5. ❌ Potência dos motores (CV ou kW)
6. ❌ Diâmetros especificados dos dutos
7. ❌ Metragens exatas (horizontal + vertical)
8. ❌ Quantidade de curvas, joelhos, transições
9. ❌ Tipo de controle (manual/automático)
10. ❌ Integração com automação predial (BMS)

---

## 🔗 COMPATIBILIZAÇÕES NECESSÁRIAS

### Disciplinas a Cruzar:

**1. Elétrico (09)** → `projetos/thozen-electra/projetos/09 ELÉTRICO/`
- Alimentação dos exaustores (quadro, circuitos, proteções)
- Cabos: bitola, metragem, eletrodutos
- Comando: botoeiras, contatores, relés térmicos

**2. Arquitetura (02)** → `projetos/thozen-electra/projetos/02 ARQUITETURA/DWG/RA_ARQ_EXE_07_LAZER_R02.dwg`
- Localização exata das churrasqueiras no lazer
- Pé-direito (impacta altura das coifas)
- Acabamentos e detalhamento arquitetônico

**3. Estrutura (01)**
- Passagem da prumada vertical (furos em lajes)
- Reforços estruturais (se necessário)

**4. PCI Civil (07)**
- Dampers corta-fogo na prumada vertical
- Proteção passiva de dutos

**5. Ar-condicionado (14)**
- Integração da ventilação de compensação
- Evitar pressões conflitantes no ambiente

---

## 📝 CHECKLIST DE VALIDAÇÃO

Antes de gerar a planilha executiva, validar:

- [ ] Converter DWG → DXF ou gerar PDF plotado
- [ ] Extrair quantitativos reais do projeto
- [ ] Confirmar com equipe de projetos:
  - [ ] Sistema centralizado (1 exaustor) OU individualizado (N exaustores)?
  - [ ] Tipo de controle (manual/automático)?
  - [ ] Integração com BMS/automação predial?
- [ ] Cruzar com disciplina Elétrico (09) → alimentação, cabos, quadros
- [ ] Cruzar com Arquitetura (02) → layout, interferências
- [ ] Cruzar com Estrutura (01) → passagens, furos
- [ ] Verificar normas locais aplicáveis (CSMSP, CBPMESP)

---

## 💰 IMPACTO NO ORÇAMENTO

**Classificação Memorial:** N1 14.08 - Instalações Especiais > Exaustão Mecânica

**Magnitude estimada (sem custos reais):**
- Equipamentos: R$ 15.000 - 40.000 (exaustores + coifas)
- Dutos e acessórios: R$ 10.000 - 25.000
- Instalação elétrica: R$ 5.000 - 15.000
- Mão de obra: R$ 8.000 - 20.000
- **TOTAL ESTIMADO:** R$ 38.000 - 100.000 (alto grau de incerteza)

⚠️ **Valores NÃO devem ser usados para cotação** — apenas ordem de grandeza.

---

## 📌 RECOMENDAÇÃO

**Prioridade:** 🟡 MÉDIA (sistema complementar, não crítico)

**Próximo passo:**
1. Converter DWG → DXF usando ODA File Converter
2. Reprocessar com script de extração
3. Atualizar briefing com quantitativos reais
4. Gerar planilha executiva para orçamento

**Prazo estimado:** 2-4 horas (após conversão do arquivo)

---

## 📎 ARQUIVOS GERADOS

- [x] `executivo/thozen-electra/briefings/exaustao-r00.md` — Briefing completo (16 KB)
- [x] `executivo/thozen-electra/briefings/exaustao-r00-RESUMO.md` — Este arquivo
- [x] `executivo/thozen-electra/fontes/RA_CHU_EXE_PROJETO_R00.dwg` — Cópia do DWG original

---

**Gerado por:** Cartesiano (bot)  
**Data:** 2026-03-20  
**Revisão:** R00  
**Status:** ⚠️ QUANTITATIVOS NÃO EXTRAÍDOS — Aguardando conversão do DWG
