# 📄 Resumo Executivo — AR-CONDICIONADO Thozen Electra

**Data:** 20/03/2026  
**Status:** 🚧 **PENDENTE — Aguardando extração de dados**

---

## 🎯 Situação Atual

✅ **Arquivo recebido:**  
`projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg` (5,0 MB)

❌ **Problema identificado:**  
Arquivo em formato DWG binário (AutoCAD) — não é possível processar com ferramentas open-source disponíveis (ezdxf).

⏸️ **Quantitativos:**  
Extração suspensa até conversão do arquivo ou recebimento de dados complementares.

---

## 🔧 Soluções Propostas

### Opção 1: Converter DWG → DXF (RECOMENDADO)

**Ferramentas disponíveis:**
- **ODA File Converter** (gratuito) → https://www.opendesign.com/guestfiles/oda_file_converter
- **LibreCAD** (open-source) → `brew install --cask librecad`
- **AutoCAD** (comercial)

**Após conversão:**
- Executar `python3.11 scripts/extrair_ar_condicionado_dwg.py arquivo.dxf`
- Script automatizado irá extrair:
  - Equipamentos (splits, VRF)
  - Tubulações frigoríficas (metragens por diâmetro)
  - Drenos
  - Elétrica associada
  - Acessórios

**Tempo estimado:** 30 minutos (conversão + extração automatizada)

---

### Opção 2: Solicitar Arquivo DXF ao Projetista

**Email sugerido:**
> Olá [Projetista],  
> Precisamos do arquivo de ar-condicionado em formato **DXF** para extração automatizada de quantitativos.  
> Arquivo atual: `RA_ARC_EXE_00_TODAS CAD_R05.dwg`  
> Pode enviar em DXF?

**Tempo estimado:** 1-3 dias (dependendo do projetista)

---

### Opção 3: Solicitar Planilha de Quantitativos

**Informações necessárias:**
- Lista de condensadoras (potência, local)
- Lista de evaporadoras (potência, ambiente, pavimento)
- Metragens de tubulação frigorífica (por diâmetro)
- Metragens de drenos
- Metragens de cabos elétricos
- Quantidade de acessórios (suportes, abraçadeiras, registros)

**Tempo estimado:** 1-3 dias (dependendo do projetista)

---

### Opção 4: Extração Manual (MENOS RECOMENDADO)

**Processo:**
1. Abrir DWG em visualizador (LibreCAD, DraftSight)
2. Contar blocos de equipamentos manualmente
3. Medir tubulações por layer
4. Preencher briefing

**Tempo estimado:** 4-8 horas de trabalho manual

---

## 📋 Estrutura do Briefing Criado

O briefing foi preparado com estrutura completa, aguardando preenchimento dos quantitativos:

### Seções Completas ✅
- Resumo executivo
- Premissas técnicas
- Organização por pavimento
- Mapeamento para Memorial Cartesiano (N1 14.02)
- Tabelas de precificação (referência)
- Normas e especificações típicas

### Seções Pendentes ⏸️
- 3.1 Equipamentos (condensadoras, evaporadoras, VRF)
- 3.2 Tubulações frigoríficas (metragens por diâmetro)
- 3.3 Linhas de dreno (metragens)
- 3.4 Instalações elétricas (cabos, eletrodutos, disjuntores)
- 3.5 Suportes e acessórios (quantidades)
- 4.1 a 4.5 Quantitativos por pavimento

---

## 📊 Estimativas Paramétricas (Enquanto Isso)

Para orçamento rápido, usar índices da base Cartesian:

| Item | Índice Típico | Base |
|------|--------------|------|
| Climatização residencial | R$ 80-150/m² AC | Projetos similares |
| Split individual (9-12k BTU) | R$ 2.000-2.500/un | Instalado |
| Split individual (18-24k BTU) | R$ 3.000-4.000/un | Instalado |
| VRF (áreas comuns) | R$ 8.000-12.000/TR | Sistema completo |

**⚠️ Premissas:**
- AC total Thozen Electra: ~20.000-30.000 m² (estimativa)
- Custo climatização (paramétrico): **R$ 1.600.000 - R$ 4.500.000**
- **Precisão:** ±30-40% (orçamento paramétrico)

**Para orçamento executivo preciso:** Necessária extração de quantitativos reais.

---

## 🎯 Recomendação Imediata

**Prioridade 1:** Instalar ODA File Converter + converter DWG → DXF  
**Prioridade 2:** Solicitar DXF ou planilha ao projetista  
**Última opção:** Extração manual (4-8h trabalho)

**Após extração:**
- Preencher briefing completo
- Gerar planilha Excel (Memorial Cartesiano N1 14.02)
- Integrar com orçamento executivo geral

---

## 📁 Arquivos Criados

1. **Briefing completo:** `executivo/thozen-electra/briefings/ar-condicionado-r00.md`
   - 20 páginas, estrutura completa
   - Tabelas prontas para preenchimento
   - Premissas técnicas documentadas

2. **Instruções de extração:** `executivo/thozen-electra/briefings/ar-condicionado-r00-INSTRUCOES-EXTRACAO.md`
   - Guia passo-a-passo
   - Comandos para conversão
   - Checklist de validação

3. **Script de extração:** `scripts/extrair_ar_condicionado_dwg.py`
   - Pronto para usar quando DXF estiver disponível
   - Extração automatizada de layers, blocos, textos, tubulações

4. **Este resumo:** `executivo/thozen-electra/briefings/ar-condicionado-r00-RESUMO.md`

---

## ⏭️ Próximos Passos

**Time comercial decide:**
1. ✅ Usar estimativa paramétrica (±30-40%) para proposta preliminar?
2. ✅ Investir tempo em conversão + extração para orçamento executivo preciso?
3. ✅ Solicitar dados ao projetista e aguardar?

**Aguardando direcionamento para prosseguir.**

---

*Resumo preparado por Cartesiano | 20/03/2026*
