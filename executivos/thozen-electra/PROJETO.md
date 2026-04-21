# Projeto: Thozen Electra Towers

> Ver tambem: [[README]] | [[gestao-orcamento-electra]] | [[log-execucao]]

## Informações Gerais
- **Nome:** Thozen Electra Towers
- **Cliente:** [a confirmar]
- **Tipologia:** Residencial multifamiliar (2 torres)
- **Pavimentos:** 34 por torre (1° Térreo + 5 Garagens + 1 Lazer + 24 Tipo + 3 técnicos)
- **Status:** Em orçamento executivo

## ⚡ Arquivo Principal do Orçamento
- **Arquivo atualizado:** `CTN-TZN_ELT - Orçamento Executivo_R00_Leo rev01.xlsx`
- **Localização:** Raiz da pasta do projeto (acesso rápido)
- **Versões anteriores:** `orcamento/` (R00, R01, R02, R03)
- **Observação:** Versão de trabalho ativa na raiz. Revisões históricas ficam em `orcamento/`. Atualizado em 2026-04-03.

## Disciplinas em Desenvolvimento

### Instalações Especiais — Prevenção e Combate a Incêndio (PCI)
- **Revisão atual:** R00 (2026-03-20)
- **Status:** ⚠️ Preliminar — aguardando validação e dados complementares
- **Fontes:** IFC rev.01 (Torre A e B), DWGs 11 pranchas
- **Arquivos:**
  - `briefings/pci-civil-r00.md` — Briefing completo
  - `briefings/pci-civil-r00-anexo-pavimentos.md` — Distribuição por pavimento
  - `briefings/pci-civil-r00-RESUMO.md` — Resumo executivo
- **Pendências críticas:**
  - Reservatórios e bombas de incêndio (não encontrados no IFC)
  - Metragem real de tubulação (valor extraído subestimado)
  - Sistema de sprinklers (não identificado)
  - Memorial descritivo do sistema

### Instalações Telefônicas e Lógica (Cabeamento Estruturado)
- **Revisão atual:** R00 (2026-03-20)
- **Status:** ⚠️ PARCIAL — Infraestrutura passiva extraída, faltam cabos e ativos de rede
- **Fontes:** 9 IFCs rev.01 + 18 DWGs rev.01
- **Projetista:** R. Rubens Alves
- **Arquivos:**
  - `briefings/telefonico-r00.md` — Briefing completo (17.6 KB)
  - `briefings/telefonico-r00-RESUMO.md` — Resumo executivo (3.2 KB)
  - `output/thozen-electra-telefonico-consolidado.json` — Dados estruturados
  - `output/relatorio-extracao-telefonico-thozen.md` — Relatório técnico
- **Quantitativos extraídos:**
  - 46 pontos de dados (RJ45) — concentrados no Térreo
  - 44 pontos de voz (RJ11) — Térreo + Tipo
  - ~648 caixas de passagem (4x2, 4x4, octogonais)
  - ~33.400 m de eletrodutos (incluindo Tipo x24)
  - 33 m de eletrocalhas (G1 apenas — shaft vertical)
  - 3.694 acessórios de fixação
- **Pendências críticas:**
  - Metragens de cabos UTP (CAT6/CAT6A) — não modelados nos IFCs
  - Racks de telecomunicações (quantidade, localização) — não modelados
  - Patch panels (tipo, portas) — não modelados
  - DG (Distribuidor Geral) — especificação e localização
  - Diâmetros de eletrodutos (não especificados nos IFCs — buscar em DWGs)
  - Dimensões de calhas (não especificadas nos IFCs — buscar em DWGs)
  - Pontos lógicos nas garagens (não identificados — possível projeto separado)
  - Memorial descritivo do sistema (topologia, certificação)

## Localização dos Arquivos Fonte

### PCI (Prevenção e Combate a Incêndio)
- `projetos/thozen-electra/projetos/07 PREVENTIVO INCENDIO CIVIL/IFC/` — Arquivos IFC
- `projetos/thozen-electra/projetos/07 PREVENTIVO INCENDIO CIVIL/DWG/` — Pranchas DWG

### Telefônico (Cabeamento Estruturado)
- `projetos/thozen-electra/projetos/10 TELEFONICO/IFC/` — 9 arquivos IFC
- `projetos/thozen-electra/projetos/10 TELEFONICO/DWG/` — 18 arquivos DWG (Torre A e B)

### Instalações Especiais — Ventilação Mecânica (Escadas Pressurizadas)
- **Revisão atual:** R05 (projeto legal)
- **Status:** ⚠️ **PREMISSAS NÃO VALIDADAS** — DWG não pôde ser processado
- **Fontes:** RA_EVM_LEGAL_PROJETO_R05.dwg (5.39 MB, AutoCAD 2018/2019/2020)
- **Projetista:** Rubens Alves
- **Arquivos:**
  - `briefings/ventilacao-r00.md` — Briefing completo (21 KB)
  - `briefings/ventilacao-r00-resumo.md` — Resumo executivo (7 KB)
  - `briefings/ventilacao-r00-log-extracao.md` — Log de extração (9 KB)
- **Quantitativos estimados (premissas):**
  - 2 ventiladores centrífugos (8.000-12.000 m³/h, 5-7,5 CV)
  - 64 dampers corta-fogo 90min
  - 4 dampers motorizados
  - 200 m de duto vertical Ø600mm
  - 60 m de duto de derivação
  - 380 m² de isolamento térmico
  - 42 grelhas/difusores
  - Sistema de automação (CLP + IHM)
- **Custo estimado:** R$ 328k - 554k (com BDI 25-30% + contingência 15-20%)
- **Pendências críticas:**
  - ⚠️ **Extração automática do DWG falhou** — ferramentas indisponíveis
  - Todos os quantitativos são estimativas baseadas em NBR 14880:2024
  - Memorial descritivo obrigatório (vazões, pressões, potências reais)
  - Prancha de detalhes (isométricos, localização de equipamentos)
  - Planilha de equipamentos (fabricante, modelo, especificações)
  - Confirmação de número de escadas pressurizadas (premissa: 2)
  - Existência de antecâmaras pressurizadas

### Instalações Especiais — Ar-Condicionado e Climatização
- **Revisão atual:** R05
- **Status:** 🚧 **EXTRAÇÃO PENDENTE** — DWG não pôde ser processado (formato binário)
- **Fontes:** RA_ARC_EXE_00_TODAS CAD_R05.dwg (5.0 MB, AutoCAD nativo)
- **Projetista:** [a confirmar]
- **Arquivos:**
  - `briefings/ar-condicionado-r00.md` — Briefing completo (20 KB, estrutura pronta)
  - `briefings/ar-condicionado-r00-RESUMO.md` — Resumo executivo (5 KB)
  - `briefings/ar-condicionado-r00-INSTRUCOES-EXTRACAO.md` — Guia de processamento (9 KB)
  - `scripts/extrair_ar_condicionado_dwg.py` — Script de extração (pronto)
- **Quantitativos:** ⏸️ Aguardando conversão DWG → DXF ou recebimento de dados do projetista
- **Estimativa paramétrica (provisória):**
  - Climatização residencial: R$ 80-150/m² AC
  - Custo total estimado: R$ 1,6M - 4,5M (±30-40% precisão)
- **Pendências críticas:**
  - ⚠️ **Conversão DWG → DXF necessária** — ferramentas não disponíveis (ODA File Converter, AutoCAD, LibreCAD)
  - Equipamentos (condensadoras, evaporadoras, VRF) — quantidade e potências
  - Tubulações frigoríficas (metragens por diâmetro 1/4", 3/8", 1/2", 5/8", 3/4")
  - Linhas de dreno (metragens DN20, DN25)
  - Instalações elétricas associadas (cabos, eletrodutos, disjuntores)
  - Suportes e acessórios (quantidades)
  - Memorial descritivo do sistema
  - Planilha de quantitativos do projetista (alternativa à extração)

## Localização dos Arquivos Fonte

### PCI (Prevenção e Combate a Incêndio)
- `projetos/thozen-electra/projetos/07 PREVENTIVO INCENDIO CIVIL/IFC/` — Arquivos IFC
- `projetos/thozen-electra/projetos/07 PREVENTIVO INCENDIO CIVIL/DWG/` — Pranchas DWG

### Telefônico (Cabeamento Estruturado)
- `projetos/thozen-electra/projetos/10 TELEFONICO/IFC/` — 9 arquivos IFC
- `projetos/thozen-electra/projetos/10 TELEFONICO/DWG/` — 18 arquivos DWG (Torre A e B)

### Ventilação Mecânica (Escadas Pressurizadas)
- `projetos/thozen-electra/projetos/12 ESCADA VENTILACAO MECANICA/DWG/` — RA_EVM_LEGAL_PROJETO_R05.dwg

### Ar-Condicionado e Climatização
- `projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/` — RA_ARC_EXE_00_TODAS CAD_R05.dwg

## Estrategia de Preenchimento (10/abr/2026)

- **BIM (Visus):** 13 macrogrupos de arquitetura/acabamentos — Leo extrai do modelo
- **Planilha (IA):** Instalacoes tecnicas — dados de IFC/DWG ja processados
- **Indices:** Ger. Tec/Adm, canteiro, EPCs — medias de executivos entregues
- **Fluxo:** Visus + Planilha → Excel completo → importa de volta no Visus
- Ver detalhes em [[gestao-orcamento-electra]] e [[log-execucao]]

## Histórico
- **2026-04-10:** Definida estrategia BIM (Visus) vs Planilha vs Indices
- **2026-03-27:** Definido arquivo principal do orçamento: `CTN-TZN_ELT - Orçamento Executivo_R00_Leo.xlsx` (Google Drive)
- **2026-03-20:** Criação do briefing Ar-Condicionado R00 (estrutura completa, aguardando extração de dados)
- **2026-03-20:** Criação do briefing Ventilação Mecânica R00 (baseado em premissas NBR 14880)
- **2026-03-20:** Criação do briefing Telefônico R00 (extração IFC — infraestrutura passiva)
- **2026-03-20:** Criação do briefing PCI R00 (extração automatizada IFC)

---

*Última atualização: 2026-03-27*
