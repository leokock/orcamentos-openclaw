# ✅ Checklist — AR-CONDICIONADO Thozen Electra R00

**Data criação:** 20/03/2026  
**Status geral:** 🚧 EM ANDAMENTO — Aguardando extração de dados

---

## 📥 Recebimento de Arquivos

- [x] Arquivo DWG recebido
  - `RA_ARC_EXE_00_TODAS CAD_R05.dwg` (5,0 MB)
  - Localização: `projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/`
- [ ] Arquivo DXF (conversão necessária)
- [ ] Memorial descritivo do sistema
- [ ] Planilha de quantitativos do projetista
- [ ] Especificações de equipamentos (marcas, modelos)

---

## 🔧 Processamento de Arquivos

### Conversão DWG → DXF
- [ ] Instalar ODA File Converter
- [ ] Converter arquivo para DXF
- [ ] Validar arquivo DXF gerado

### Extração Automatizada
- [x] Script de extração criado (`extrair_ar_condicionado_dwg.py`)
- [ ] Executar script sobre DXF
- [ ] Validar layers identificados
- [ ] Validar blocos extraídos
- [ ] Validar textos com especificações
- [ ] Validar metragens de tubulações

### Alternativa: Extração Manual
- [ ] Abrir DWG em visualizador (LibreCAD/DraftSight)
- [ ] Identificar layers relevantes
- [ ] Contar equipamentos manualmente
- [ ] Medir tubulações manualmente
- [ ] Extrair especificações de textos

---

## 📋 Documentação

### Briefing
- [x] Estrutura completa criada (`ar-condicionado-r00.md`)
- [x] Resumo executivo criado (`ar-condicionado-r00-RESUMO.md`)
- [x] Instruções de extração criadas (`ar-condicionado-r00-INSTRUCOES-EXTRACAO.md`)
- [ ] Seção 3.1 preenchida (Equipamentos)
- [ ] Seção 3.2 preenchida (Tubulações frigoríficas)
- [ ] Seção 3.3 preenchida (Drenos)
- [ ] Seção 3.4 preenchida (Elétrica)
- [ ] Seção 3.5 preenchida (Suportes e acessórios)
- [ ] Seção 4 preenchida (Quantitativos por pavimento)

### Integração
- [x] PROJETO.md atualizado
- [x] Relatório de extração gerado (`output/relatorio-extracao-ar-condicionado-thozen.md`)

---

## 🔍 Quantitativos — Equipamentos

### Condensadoras (Unidades Externas)
- [ ] Quantidade total identificada
- [ ] Potências catalogadas (BTU/h ou TR)
- [ ] Localização por pavimento definida
- [ ] Especificações técnicas (marca, modelo)

### Evaporadoras (Unidades Internas)
- [ ] Quantidade total identificada
- [ ] Potências catalogadas (BTU/h)
- [ ] Distribuição por ambiente mapeada
- [ ] Tipos identificados (split, cassete, piso-teto, duto)

### Sistema VRF (se aplicável)
- [ ] Sistema VRF identificado
- [ ] Capacidade total (TR)
- [ ] Quantidade de condensadoras VRF
- [ ] Quantidade de evaporadoras VRF
- [ ] Áreas atendidas (lazer, áreas comuns)

---

## 🔍 Quantitativos — Tubulações

### Tubulações Frigoríficas (Cobre)
- [ ] Linha de gás 1/2" (metragem)
- [ ] Linha de gás 5/8" (metragem)
- [ ] Linha de gás 3/4" (metragem)
- [ ] Linha de líquido 1/4" (metragem)
- [ ] Linha de líquido 3/8" (metragem)
- [ ] Isolamento térmico (metragem)

### Linhas de Dreno
- [ ] Tubo PVC DN20 (metragem)
- [ ] Tubo PVC DN25 (metragem)
- [ ] Sifões (quantidade)

### Validações
- [ ] Metragem linha gás ≈ metragem linha líquido?
- [ ] Metragem dreno ≈ 80-100% tubulação frigorífica?
- [ ] Prumadas: ~3m/pavto × 34 pavtos × qtd prumadas?

---

## 🔍 Quantitativos — Elétrica

### Alimentação de Equipamentos
- [ ] Cabos 3×1,5mm² (metragem)
- [ ] Cabos 3×2,5mm² (metragem)
- [ ] Cabos 3×4,0mm² (metragem — se houver)
- [ ] Disjuntores 10A (quantidade)
- [ ] Disjuntores 20A (quantidade)
- [ ] Disjuntores 32A (quantidade — se houver)

### Infraestrutura
- [ ] Eletrodutos PVC 3/4" (metragem)
- [ ] Eletrodutos PVC 1" (metragem)
- [ ] Caixas de passagem 4×2 (quantidade)
- [ ] Caixas de passagem 4×4 (quantidade)

### Validações
- [ ] Quantidade de circuitos = quantidade de equipamentos?
- [ ] Bitola de cabo compatível com potência?

---

## 🔍 Quantitativos — Acessórios

### Suportes e Fixações
- [ ] Suportes para condensadoras (parede)
- [ ] Suportes para condensadoras (laje)
- [ ] Suportes para evaporadoras (teto)
- [ ] Abraçadeiras para tubulação (quantidade)

### Acessórios Hidráulicos
- [ ] Registros de esfera (linha líquido)
- [ ] Registros de esfera (linha gás)
- [ ] Grelhas de ventilação

### Validações
- [ ] Abraçadeiras: 1 a cada 1,5m de tubulação?
- [ ] Registros: 2 por evaporadora (gás + líquido)?

---

## 📊 Organização por Pavimento

### Térreo (01° Pavto.)
- [ ] Ambientes climatizados identificados
- [ ] Equipamentos quantificados
- [ ] Tubulações medidas
- [ ] Elétrica levantada

### Garagens (02° a 06° Pavto. — G1 a G5)
- [x] Confirmado: sem climatização (só ventilação mecânica)

### Lazer (07° Pavto.)
- [ ] Ambientes climatizados identificados
- [ ] Sistema definido (VRF ou splits)
- [ ] Equipamentos quantificados
- [ ] Tubulações medidas
- [ ] Elétrica levantada

### Pavimentos Tipo (08° a 31° Pavto. — 24 pavimentos)
- [ ] Infraestrutura por apartamento levantada
- [ ] Prumadas medidas
- [ ] Pontos elétricos quantificados
- [ ] Multiplicador aplicado (×1 para 08°, ×23 para 09°-31°)

### Casa de Máquinas (Cobertura)
- [ ] Condensadoras identificadas
- [ ] Equipamentos auxiliares levantados
- [ ] Quadros elétricos identificados

---

## 💰 Precificação

### Base de Preços
- [x] Tabela de referência criada (equipamentos)
- [x] Tabela de referência criada (tubulações)
- [x] Tabela de referência criada (elétrica)
- [x] Tabela de referência criada (mão de obra)
- [ ] Preços atualizados com cotações reais
- [ ] Data-base confirmada (Mar/2026)

### Composições
- [ ] Custo unitário por equipamento calculado
- [ ] Custo por metro de tubulação calculado
- [ ] Custo por ponto elétrico calculado
- [ ] BDI aplicado (%)
- [ ] Contingência aplicada (%)

### Validações
- [ ] Custo total dentro da faixa paramétrica (R$ 1,6M - 4,5M)?
- [ ] Custo/m² AC razoável (R$ 80-150/m²)?

---

## ✅ Validações Técnicas

### Compatibilidade com Outros Projetos
- [ ] Verificado com projeto elétrico (disciplina 09)
  - Alimentação disponível nos quadros?
  - Disjuntores compatíveis?
  - Circuitos dedicados previstos?
- [ ] Verificado com projeto hidrossanitário (disciplina 06)
  - Interligação de drenos com águas pluviais ou esgoto?
  - Sifões corretamente posicionados?
- [ ] Verificado com projeto arquitetônico (disciplina 02)
  - Localização de equipamentos compatível?
  - Espaços técnicos previstos?
  - Shafts dimensionados para prumadas?

### Normas e Especificações
- [ ] NBR 16401 atendida (instalações de ar-condicionado)
- [ ] NBR 5410 atendida (instalações elétricas)
- [ ] NBR 15848 verificada (manutenção de sistemas)
- [ ] Memorial descritivo revisado

---

## 📝 Pendências Críticas

### Com o Projetista
- [ ] Nome do projetista confirmado
- [ ] Data da revisão R05 confirmada
- [ ] Memorial descritivo recebido
- [ ] Planilha de equipamentos recebida
- [ ] Especificações técnicas (marcas, modelos)
- [ ] Carga térmica calculada por ambiente

### Decisões de Projeto
- [ ] Tipologia do sistema confirmada (split individual vs. VRF)
- [ ] Climatização nas garagens confirmada (provável: não)
- [ ] Pontos de dreno validados (destino: pluvial ou esgoto)
- [ ] Alimentação elétrica disponível confirmada

### Extração de Dados
- [ ] **CRÍTICO:** Conversão DWG → DXF realizada
- [ ] Lista completa de equipamentos extraída
- [ ] Metragens de tubulações extraídas
- [ ] Metragens de drenos extraídas
- [ ] Pontos elétricos e especificações extraídos
- [ ] Suportes e acessórios quantificados

---

## 📤 Entregáveis Finais

### Documentação
- [x] Briefing completo R00
- [x] Resumo executivo
- [x] Instruções de extração
- [ ] Briefing atualizado com quantitativos reais

### Planilhas
- [ ] Planilha Excel Memorial Cartesiano (N1 14.02)
  - Aba: Equipamentos
  - Aba: Tubulações
  - Aba: Drenos
  - Aba: Elétrica
  - Aba: Acessórios
  - Aba: Resumo

### Integração
- [x] PROJETO.md atualizado
- [ ] Orçamento executivo consolidado
- [ ] Cronograma de instalação (se solicitado)

---

## 🎯 Status Geral por Seção

| Seção | Status | Completude | Bloqueio |
|-------|--------|------------|----------|
| Documentação base | ✅ Concluído | 100% | Nenhum |
| Conversão DWG → DXF | ⏸️ Pendente | 0% | Ferramentas não disponíveis |
| Extração de quantitativos | ⏸️ Pendente | 0% | Aguardando conversão |
| Equipamentos | ⏸️ Pendente | 0% | Aguardando extração |
| Tubulações | ⏸️ Pendente | 0% | Aguardando extração |
| Drenos | ⏸️ Pendente | 0% | Aguardando extração |
| Elétrica | ⏸️ Pendente | 0% | Aguardando extração |
| Acessórios | ⏸️ Pendente | 0% | Aguardando extração |
| Precificação | ⏸️ Parcial | 30% | Aguardando quantitativos |
| Planilha Excel | ⏸️ Pendente | 0% | Aguardando quantitativos |

---

## ⏭️ Próxima Ação

**Aguardando decisão do time:**

- [ ] Instalar ODA File Converter e processar DWG?
- [ ] Solicitar DXF ao projetista?
- [ ] Solicitar planilha de quantitativos ao projetista?
- [ ] Prosseguir com estimativa paramétrica?

**Responsável pela decisão:** [a definir]  
**Prazo para decisão:** [a definir]

---

*Checklist criado por Cartesiano | 20/03/2026 | Atualizar após cada etapa concluída*
