# Oxford 600 Residence — Mussi Empreendimentos

**Status:** ✅ 100% Concluído  
**Data:** 12-13/março/2026  
**Duração:** ~6h30

---

## 📦 Entregáveis Finais

1. **[OXFORD-Orcamento-Parametrico-20260312.xlsx](OXFORD-Orcamento-Parametrico-20260312.xlsx)** (33 KB, 14 abas)
   - Briefing dinâmico (25 dropdowns)
   - 18 macrogrupos orçamentários
   - Sistema de validação (semáforo P10-P90)
   - Base calibrada com 75 projetos reais

2. **[OXFORD-Orcamento-Executivo-20260312.xlsx](OXFORD-Orcamento-Executivo-20260312.xlsx)** (24 KB, 8 abas)
   - Estrutura, hidro, elétrico, PPCI, vedações, acabamentos, lazer
   - BDI 25% aplicado
   - Formatação profissional
   - Custo parcial confirmado: R$ 9,5M - R$ 10M

3. **[OXFORD-Memorial-Descritivo.md](OXFORD-Memorial-Descritivo.md)** (77 KB, 1.954 linhas)
   - 14 seções estruturadas
   - **21 tabelas de rastreabilidade** (memorial ↔ orçamento)
   - Todos os sistemas consolidados
   - Pronto pra conversão DOCX

4. **[OXFORD-Briefing-Final-20260313.md](OXFORD-Briefing-Final-20260313.md)**
   - 25 perguntas com status: ✅ confirmado | ⚠️ estimado | ❌ indisponível
   - Dados adicionais confirmados
   - Lista de bloqueadores críticos

---

## 📊 Dados do Projeto

**Arquitetura:**
- 27 pavimentos (71,90m altura)
- 0 subsolos, 4 garagens (G2-G5), lazer (6º), 17 tipos (7º-23º), ático (24º), 3 técnicos
- 136+ vagas
- Lazer: 432,88 m² (piscina, fitness, coworking, 9 ambientes)
- Penthouse: 114,83 m²
- Comercial: 322,96 m²
- Unidades estimadas: 86-103

**Estrutura:**
- Concreto total: 3.345 m³ (fundação 455 m³ + lajes 2.390 m³ + vigas/pilares ~500 m³)
- Aço total: 240 toneladas (taxa 71,7 kg/m³ — validada ✅)
- Formas: ~40.000 m²
- Fundação: blocos sobre estacas hélice contínua

**Elétrico:**
- Potência instalada: 639 kW | Demandada: 431 kW
- Trafo: 500 kVA | Gerador: 200 kVA
- Quadros: ~110 | Disjuntores: ~2.220 | DRs: ~600
- SPDA: Franklin Nível II
- CFTV: 50 câmeras IP

**PPCI:**
- RTI: 21.663L | Hidrantes: 24 DN65
- Detecção: Central Tipo 3, 8 laços, ~150 detectores
- Pressurização: 2× TITAN BLD 560 (22.800 m³/h, 7,5 kW)
- Aprovação CBMSC: 24/04/2025

---

## 📁 Arquivos de Análise

**Dados Consolidados:**
- [oxford-dados-arquitetura.md](oxford-dados-arquitetura.md)
- [oxford-quantitativos-hidro.md](oxford-quantitativos-hidro.md)
- [oxford-dados-estrutura.md](oxford-dados-estrutura.md)
- [oxford-quantitativos-estrutura.md](oxford-quantitativos-estrutura.md)
- [oxford-dados-ppci.md](oxford-dados-ppci.md)
- [oxford-dados-eletrico.md](oxford-dados-eletrico.md)

**Processamento IFC:**
- [README-PROCESSAMENTO-IFC.md](README-PROCESSAMENTO-IFC.md)
- [ANALISE-FINAL-IFC.md](ANALISE-FINAL-IFC.md)
- [oxford-ifc-dados-brutos.json](oxford-ifc-dados-brutos.json) (932 KB)

**Resumos:**
- [RESUMO-ESTRUTURA-OXFORD.md](RESUMO-ESTRUTURA-OXFORD.md)
- [RESUMO-ORCAMENTO-OXFORD.md](RESUMO-ORCAMENTO-OXFORD.md)
- [RASTREABILIDADE-COMPLETA-RESUMO.md](RASTREABILIDADE-COMPLETA-RESUMO.md)

---

## 🎓 Lições Aprendidas

**[LICOES-APRENDIDAS-OXFORD.md](LICOES-APRENDIDAS-OXFORD.md)** (18 KB, 12 seções)

**⚠️ REGRA CRÍTICA (atualizada 13/mar/2026):**
Orçamento executivo SEMPRE com extração por pavimento em **TODAS as disciplinas**:
- ✅ Estrutura (por pavimento)
- ✅ Hidrossanitário (por pavimento)
- ✅ Elétrico (por pavimento)
- ✅ PPCI (por pavimento)
- ✅ Vedações (por pavimento)
- ✅ Acabamentos (por pavimento)
- ✅ Resumo Geral (consolidado)

**Nunca consolidar em linha única sem quebra por pavimento.**

Documento completo com aprendizados do projeto:
1. Estrutura de dados e documentação
2. Processamento técnico
3. Estratégia de subagentes
4. Qualidade dos entregáveis
5. Comunicação com o cliente
6. Gestão de tempo e recursos
7. Dados e validações
8. Próximos projetos — checklist otimizado
9. Ferramentas e bibliotecas validadas
10. Métricas do projeto Oxford
11. Conclusões e recomendações
12. Checklist rápido — resumo executivo

**⚠️ Consultar SEMPRE antes de iniciar novo projeto de orçamentação.**

---

## ⚙️ Scripts Gerados

- [gerar_oxford_parametrico.py](gerar_oxford_parametrico.py) (6,2 KB)
- Script de processamento IFC (temporário)

---

## 📋 Dados Faltantes / Validações Pendentes

**Bloqueadores críticos (solicitar Mussi):**
- [ ] Área Construída Total oficial (usando estimativa ~7.500 m²)
- [ ] Área do Terreno (usando estimativa ~1.200 m²)
- [ ] Data-base CUB exata (assumido março/2026)
- [ ] Número exato de unidades (estimado 86-103)

**Validar:**
- [ ] Tipo de laje (assumido cubetas — padrão regional)
- [ ] Padrão de acabamento (classificado Alto Padrão)
- [ ] Prazo de execução (estimado 36 meses)

**Ajustes finais:**
- [ ] Revisar custos unitários SINAPI março/2026
- [ ] Cotar fornecedores (gerador, ventiladores PPCI, CFTV)
- [ ] Ajustar valores conforme cotações

---

## 🔗 Navegação

**Documentação Geral:**
- [Workflow de Orçamentação](../../docs/ORCAMENTO-WORKFLOW.md)
- [Lições Aprendidas (link local)](LICOES-APRENDIDAS-OXFORD.md)
- [README Workspace Orçamentos](../../README.md)

**Workspace:**
- `~/orcamentos/` — Workspace de orçamentação
- `~/orcamentos/projetos/mussi-oxford/` — Este projeto
- `~/clawd/orcamento-parametrico/` — Sistema paramétrico

---

**Projeto de referência para futuros orçamentos.**
