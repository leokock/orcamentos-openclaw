# Briefing Técnico - Instalações de Ar-Condicionado
## Projeto: Thozen Electra
**Revisão:** R00  
**Data:** 20/03/2026  
**Disciplina:** 14 AR-CONDICIONADO  
**Memorial Cartesiano:** N1 14.02 Climatização

---

## 1. Resumo Executivo

⚠️ **STATUS ATUAL: EXTRAÇÃO PENDENTE**

Este briefing documenta a estrutura do projeto de climatização do empreendimento Thozen Electra, edifício residencial com duas torres (T.A e T.B), 31 pavimentos tipo, pavimentos de garagem (G1 a G5), pavimento de lazer e casa de máquinas.

**Arquivo fonte disponível:**
- `projetos/thozen-electra/projetos/14 AR-CONDICIONADO/DWG/RA_ARC_EXE_00_TODAS CAD_R05.dwg` (5,0 MB)

**Limitação técnica:**
- Arquivo em formato DWG nativo (binário) — requer conversão para DXF ou processamento via AutoCAD/LibreCAD
- Ferramentas disponíveis (ezdxf) não suportam leitura direta de DWG

**Próximas ações necessárias:**
1. Converter DWG para DXF usando ODAFileConverter ou AutoCAD
2. Processar DXF para extrair:
   - Equipamentos (splits, VRF, condensadoras, evaporadoras)
   - Tubulações frigoríficas (diâmetros, metragens)
   - Linhas de dreno
   - Instalações elétricas associadas
   - Suportes e acessórios
3. Organizar dados por sistema, pavimento e ambiente
4. Atualizar este briefing com quantitativos reais

---

## 2. Premissas e Observações

### 2.1 Fonte dos Dados
- **Arquivo recebido:** `RA_ARC_EXE_00_TODAS CAD_R05.dwg` (revisão R05)
- **Formato:** DWG binário (AutoCAD)
- **Projetista responsável:** [a confirmar]
- **Data do projeto:** [a confirmar no arquivo]
- **Pavimentos esperados no projeto:**
  - 01° Pavto. Térreo
  - 02° a 06° Pavto. (G1 a G5 — garagens)
  - 07° Pavto. Lazer
  - 08° a 31° Pavto. Tipo (24 pavimentos)
  - Casa de Máquinas

### 2.2 Tipologia do Edifício
- **Uso:** Residencial multifamiliar
- **Torres:** 2 torres (Torre A e Torre B)
- **Pavimentos por torre:** 34 níveis
- **Área construída total:** [a confirmar — estimativa ~20.000-30.000 m²]
- **Climatização esperada:**
  - **Áreas privativas (apartamentos):** Infraestrutura para split (prumadas, drenos, pontos elétricos)
  - **Áreas comuns (lazer):** Sistema central ou splits
  - **Áreas técnicas:** Ventilação mecânica ou exaustão
  - **Garagens:** Ventilação mecânica (ver disciplina 12 ESCADA VENTILACAO MECANICA)

### 2.3 Sistemas Típicos em Edifícios Residenciais

Baseado em projetos similares, o sistema de climatização provavelmente inclui:

#### 2.3.1 Infraestrutura para Splits Individuais (Apartamentos)
- **Prumadas de tubulação frigoríficas** (cobre):
  - Linha de gás (maior diâmetro): 1/2", 5/8", 3/4"
  - Linha de líquido (menor diâmetro): 1/4", 3/8"
- **Prumadas de dreno** (PVC DN20/DN25):
  - Dreno condensado das evaporadoras
  - Interligação com sistema de águas pluviais ou esgoto
- **Pontos elétricos**:
  - Alimentação condensadoras (varanda/fachada): 220V, 16-32A
  - Alimentação evaporadoras (ambientes): 220V, 10-16A
  - Disjuntores individuais por equipamento

#### 2.3.2 Sistema Central ou VRF (Áreas Comuns)
- **Condensadoras** (instalação em casa de máquinas ou cobertura):
  - Potência típica: 10-60 TR por unidade
  - Alimentação: 220V/380V trifásico
- **Evaporadoras** (instalação nos ambientes climatizados):
  - Tipo: cassete, piso-teto, duto
  - Potência típica: 12.000-60.000 BTU/h por unidade
- **Tubulação frigoríficas** (cobre):
  - Distribuição do refrigerante (R410A ou R32)
  - Isolamento térmico obrigatório
- **Drenagem**:
  - Drenos individuais ou coletores
  - Bombas de condensado (se necessário)

#### 2.3.3 Sistemas Auxiliares
- **Automação e controle**:
  - Termostatos digitais
  - Controles remotos
  - Sistema BMS (Building Management System) para áreas comuns
- **Suportes e fixações**:
  - Suportes para condensadoras (vigas, lajes, paredes)
  - Suportes para evaporadoras (teto, parede)
  - Abraçadeiras para tubulações
- **Isolamento acústico e térmico**:
  - Isolamento térmico para tubulações
  - Amortecedores de vibração
  - Barreiras acústicas (se necessário)

### 2.4 Normas de Referência
- **NBR 16401** — Instalações de ar-condicionado: sistemas centrais e unitários
- **NBR 5410** — Instalações elétricas de baixa tensão (alimentação dos equipamentos)
- **NBR 15848** — Sistemas de ar-condicionado e ventilação: procedimentos e requisitos relativos às atividades de construção, reformas, operação e manutenção

---

## 3. Quantitativos Detalhados

### 3.1 Equipamentos de Climatização

⚠️ **AGUARDANDO EXTRAÇÃO DO DWG**

#### 3.1.1 Condensadoras (Unidades Externas)

| Pavimento | Ambiente | Potência (BTU/h) | Tipo | UN | QTD | Fonte | Observação |
|-----------|----------|------------------|------|-----|-----|-------|------------|
| [a preencher] | | | | | | DWG prancha X | |

**Subtotal condensadoras:** [QTD] unidades, [POTÊNCIA TOTAL] BTU/h

#### 3.1.2 Evaporadoras (Unidades Internas)

| Pavimento | Ambiente | Potência (BTU/h) | Tipo | UN | QTD | Fonte | Observação |
|-----------|----------|------------------|------|-----|-----|-------|------------|
| [a preencher] | | | | | | DWG prancha X | |

**Subtotal evaporadoras:** [QTD] unidades, [POTÊNCIA TOTAL] BTU/h

#### 3.1.3 Sistema VRF (se aplicável)

| Sistema | Condensadoras | Evaporadoras | Potência Total (TR) | UN | QTD | Fonte | Observação |
|---------|---------------|--------------|---------------------|-----|-----|-------|------------|
| [a preencher] | | | | | | DWG prancha X | |

**Subtotal VRF:** [QTD] sistemas, [CAPACIDADE TOTAL] TR

---

### 3.2 Tubulações Frigoríficas

⚠️ **AGUARDANDO EXTRAÇÃO DO DWG**

| Descrição | Material | Diâmetro | UN | Metragem (m) | Fonte | Observação |
|-----------|----------|----------|-----|--------------|-------|------------|
| Linha de gás (maior diâmetro) | Cobre | 1/2" | m | | DWG | Incluir prumadas + distribuição horizontal |
| Linha de gás (maior diâmetro) | Cobre | 5/8" | m | | DWG | |
| Linha de gás (maior diâmetro) | Cobre | 3/4" | m | | DWG | |
| Linha de líquido (menor diâmetro) | Cobre | 1/4" | m | | DWG | |
| Linha de líquido (menor diâmetro) | Cobre | 3/8" | m | | DWG | |
| Isolamento térmico | Polietileno expandido | Diversos | m | | DWG | Mesmo comprimento das tubulações |

**Subtotal tubulações frigoríficas:** [METRAGEM TOTAL] m

**Premissas para estimativa (quando não houver DWG):**
- Prumadas: ~3,0 m/pavimento × 34 pavimentos × 4-8 prumadas = 400-800 m
- Distribuição horizontal nos apartamentos: ~10-20 m/apartamento
- Áreas comuns: a ser levantado por ambiente

---

### 3.3 Linhas de Dreno

⚠️ **AGUARDANDO EXTRAÇÃO DO DWG**

| Descrição | Material | Diâmetro | UN | Metragem (m) | Fonte | Observação |
|-----------|----------|----------|-----|--------------|-------|------------|
| Tubo de dreno | PVC | DN20 | m | | DWG | Drenagem de condensado |
| Tubo de dreno | PVC | DN25 | m | | DWG | Prumadas coletoras |
| Sifão para dreno de AC | PVC | DN20 | un | | DWG | Evitar retorno de odores |

**Subtotal drenos:** [METRAGEM TOTAL] m, [QTD] sifões

**Premissa:** Comprimento de dreno ~80-100% do comprimento das tubulações frigoríficas

---

### 3.4 Instalações Elétricas Associadas

⚠️ **AGUARDANDO EXTRAÇÃO DO DWG**

#### 3.4.1 Alimentação das Condensadoras

| Pavimento | Equipamento | Tensão | Corrente (A) | Cabo | Disjuntor | UN | QTD | Fonte |
|-----------|-------------|--------|--------------|------|-----------|-----|-----|-------|
| [a preencher] | | 220V | | 3×2,5mm² | 20A | un | | DWG |

#### 3.4.2 Alimentação das Evaporadoras

| Pavimento | Equipamento | Tensão | Corrente (A) | Cabo | Disjuntor | UN | QTD | Fonte |
|-----------|-------------|--------|--------------|------|-----------|-----|-----|-------|
| [a preencher] | | 220V | | 3×1,5mm² | 10A | un | | DWG |

#### 3.4.3 Eletrodutos e Infraestrutura

| Descrição | Material | Diâmetro | UN | Metragem (m) | Fonte | Observação |
|-----------|----------|----------|-----|--------------|-------|------------|
| Eletroduto rígido roscável | PVC | 3/4" | m | | DWG | Prumadas elétricas |
| Eletroduto rígido roscável | PVC | 1" | m | | DWG | Alimentadores |
| Caixa de passagem | PVC | 4×2 | un | | DWG | |
| Caixa de passagem | PVC | 4×4 | un | | DWG | |

**Subtotal elétrica:** [METRAGEM] m de eletrodutos, [QTD] caixas

---

### 3.5 Suportes e Acessórios

⚠️ **AGUARDANDO EXTRAÇÃO DO DWG**

| Descrição | Material | UN | QTD | Fonte | Observação |
|-----------|----------|-----|-----|-------|------------|
| Suporte para condensadora (parede) | Metálico | un | | DWG | Capacidade 60-100 kg |
| Suporte para condensadora (laje) | Metálico | un | | DWG | |
| Suporte para evaporadora (teto) | Metálico | un | | DWG | |
| Abraçadeira para tubulação | Metálica | un | | DWG | Espaçamento ~1,5 m |
| Grelha de ventilação | Alumínio | un | | DWG | |
| Registro de esfera (linha de líquido) | Bronze | un | | DWG | 1 por evaporadora |
| Registro de esfera (linha de gás) | Bronze | un | | DWG | 1 por evaporadora |

**Subtotal acessórios:** [QTD TOTAL] itens

---

### 3.6 Resumo Quantitativo (a preencher após extração)

| Item | UN | Quantidade | Observação |
|------|-----|------------|------------|
| **Equipamentos** | | | |
| Condensadoras | un | [QTD] | [POTÊNCIA TOTAL] BTU/h |
| Evaporadoras | un | [QTD] | [POTÊNCIA TOTAL] BTU/h |
| Sistemas VRF (se aplicável) | cj | [QTD] | [CAPACIDADE TOTAL] TR |
| **Tubulações** | | | |
| Tubulações frigoríficas (cobre) | m | [METRAGEM] | Linhas de gás + líquido |
| Isolamento térmico | m | [METRAGEM] | |
| Linhas de dreno (PVC) | m | [METRAGEM] | |
| **Elétrica** | | | |
| Cabos elétricos | m | [METRAGEM] | Diversos bitolas |
| Eletrodutos | m | [METRAGEM] | |
| Disjuntores | un | [QTD] | |
| **Acessórios** | | | |
| Suportes para equipamentos | un | [QTD] | |
| Abraçadeiras | un | [QTD] | |
| Registros | un | [QTD] | |
| Grelhas de ventilação | un | [QTD] | |

---

## 4. Organização por Pavimento

### 4.1 Térreo (01° Pavto.)
**Ambientes climatizados esperados:**
- Hall de entrada
- Recepção/portaria
- Salão de festas
- Áreas de serviço

**Quantitativos:**
- [a preencher após extração]

### 4.2 Garagens (02° a 06° Pavto. — G1 a G5)
**Sistema:**
- Ventilação mecânica (ver disciplina 12 ESCADA VENTILACAO MECANICA)
- Climatização: não aplicável (garagens abertas/ventiladas naturalmente)

### 4.3 Lazer (07° Pavto.)
**Ambientes climatizados esperados:**
- Academia
- Salão de jogos
- Spa/sauna
- Lounge
- Áreas de convivência

**Quantitativos:**
- [a preencher após extração]

### 4.4 Pavimentos Tipo (08° a 31° Pavto. — 24 pavimentos)
**Infraestrutura para splits individuais por apartamento:**
- Prumadas de tubulação frigorífica
- Prumadas de dreno
- Alimentação elétrica (pontos nas varandas/fachadas)

**Multiplicador de quantidades:**
- **08° Pavto. Tipo (1×):** Quantidades × 1
- **09° a 31° Pavto. Tipo (23×):** Quantidades × 23

**Quantitativos por pavimento tipo (a preencher):**
- [a preencher após extração]

**Total pavimentos tipo (×24):**
- [a preencher após extração]

### 4.5 Casa de Máquinas (Cobertura)
**Equipamentos esperados:**
- Condensadoras de VRF (se aplicável)
- Quadros elétricos de comando
- Sistema de automação

**Quantitativos:**
- [a preencher após extração]

---

## 5. Premissas Adotadas

### 5.1 Premissas Técnicas

| # | Premissa | Justificativa |
|---|---------|---------------|
| 1 | Apartamentos possuem infraestrutura para splits individuais | Padrão de mercado para edifícios residenciais de médio-alto padrão |
| 2 | Áreas comuns (lazer) com sistema central ou VRF | Eficiência energética e manutenção centralizada |
| 3 | Garagens com ventilação mecânica (não climatizadas) | NBR 15.575 — Edifícios habitacionais |
| 4 | Tubulações frigoríficas em cobre | Material padrão da indústria |
| 5 | Refrigerante R410A ou R32 | Fluidos frigoríficos mais comuns em sistemas modernos |
| 6 | Isolamento térmico com polietileno expandido | Material padrão para tubulações frigoríficas |
| 7 | Drenos em PVC, interligados ao sistema de águas pluviais | Facilita manutenção e evita infiltrações |

### 5.2 Premissas de Quantificação

| # | Premissa | Valor Adotado | Justificativa |
|---|---------|---------------|---------------|
| 1 | Pé-direito médio por pavimento | 3,0 m | Padrão residencial (estrutura + revestimentos) |
| 2 | Comprimento de prumada por pavimento | 3,0-3,5 m | Inclui travessia de laje + conexões |
| 3 | Comprimento de tubulação horizontal por split | 10-20 m | Distribuição no apartamento (sala, quartos) |
| 4 | Perda de material (tubulações) | 10% | Perdas, conexões, ajustes de campo |
| 5 | Espaçamento de abraçadeiras | 1,5 m | NBR 16401 |
| 6 | Registros por evaporadora | 2 un (linha gás + líquido) | Facilita manutenção |

---

## 6. Precificação (Base de Referência)

### 6.1 Equipamentos

| Item | UN | Preço Referência (R$) | Fonte | Data-base | Observação |
|------|-----|----------------------|-------|-----------|------------|
| Split 9.000 BTU/h | un | 1.500-2.000 | Cotação mercado | Mar/2026 | Instalado |
| Split 12.000 BTU/h | un | 2.000-2.500 | Cotação mercado | Mar/2026 | Instalado |
| Split 18.000 BTU/h | un | 2.800-3.500 | Cotação mercado | Mar/2026 | Instalado |
| Split 24.000 BTU/h | un | 3.500-4.500 | Cotação mercado | Mar/2026 | Instalado |
| VRF (sistema completo) | TR | 8.000-12.000 | Cotação mercado | Mar/2026 | Inclui condensadora + evaporadoras |

### 6.2 Tubulações e Materiais

| Item | UN | Preço Referência (R$) | Fonte | Data-base | Observação |
|------|-----|----------------------|-------|-----------|------------|
| Tubo de cobre 1/4" | m | 15-20 | SINAPI/Cotação | Mar/2026 | |
| Tubo de cobre 3/8" | m | 25-30 | SINAPI/Cotação | Mar/2026 | |
| Tubo de cobre 1/2" | m | 35-45 | SINAPI/Cotação | Mar/2026 | |
| Tubo de cobre 5/8" | m | 50-65 | SINAPI/Cotação | Mar/2026 | |
| Isolamento térmico | m | 8-12 | Cotação | Mar/2026 | |
| Tubo PVC DN20 (dreno) | m | 5-8 | SINAPI | Mar/2026 | |
| Tubo PVC DN25 (dreno) | m | 8-12 | SINAPI | Mar/2026 | |

### 6.3 Elétrica

| Item | UN | Preço Referência (R$) | Fonte | Data-base | Observação |
|------|-----|----------------------|-------|-----------|------------|
| Cabo 3×1,5mm² | m | 3-5 | SINAPI | Mar/2026 | |
| Cabo 3×2,5mm² | m | 5-8 | SINAPI | Mar/2026 | |
| Disjuntor 10A | un | 15-25 | SINAPI | Mar/2026 | |
| Disjuntor 20A | un | 20-30 | SINAPI | Mar/2026 | |
| Eletroduto PVC 3/4" | m | 8-12 | SINAPI | Mar/2026 | |

### 6.4 Mão de Obra

| Item | UN | Preço Referência (R$) | Fonte | Data-base | Observação |
|------|-----|----------------------|-------|-----------|------------|
| Instalação de split (até 18.000 BTU) | un | 500-800 | Cotação mercado | Mar/2026 | Inclui tubulação até 5m |
| Instalação de split (acima 18.000 BTU) | un | 800-1.200 | Cotação mercado | Mar/2026 | |
| Tubulação frigorífica adicional | m | 50-80 | Cotação | Mar/2026 | Além dos 5m inclusos |
| Instalação elétrica (alimentação) | pt | 150-250 | SINAPI | Mar/2026 | Por ponto de AC |

---

## 7. Pendências / Dúvidas

### 7.1 Extração de Dados

- [ ] **CRÍTICO:** Converter DWG para DXF para permitir extração automatizada
- [ ] Extrair lista completa de equipamentos (condensadoras e evaporadoras)
- [ ] Extrair metragens de tubulações frigoríficas por diâmetro
- [ ] Extrair metragens de drenos
- [ ] Extrair pontos elétricos e especificações de cabos
- [ ] Identificar sistema VRF (se aplicável) nas áreas comuns
- [ ] Quantificar suportes e acessórios

### 7.2 Informações do Projetista

- [ ] Nome do projetista responsável
- [ ] Data da última revisão (R05)
- [ ] Memorial descritivo do sistema de climatização
- [ ] Especificações dos equipamentos (marcas, modelos)
- [ ] Carga térmica calculada por ambiente
- [ ] Detalhes de instalação (alturas, distâncias mínimas)

### 7.3 Validações

- [ ] Confirmar tipologia do sistema (split individual vs. VRF)
- [ ] Confirmar se há climatização nas garagens
- [ ] Validar pontos de dreno (interligação com sistema de esgoto ou pluvial)
- [ ] Confirmar alimentação elétrica disponível (tensão, disjuntores)
- [ ] Verificar compatibilidade com projeto elétrico (disciplina 09)

---

## 8. Mapeamento para Memorial Cartesiano

| Subsistema do Briefing | Código Memorial (N2/N3) | Observação |
|----------------------|------------------------|------------|
| Equipamentos de Climatização | 14.02.001 | Splits, VRF, condensadoras |
| Tubulações Frigoríficas | 14.02.002 | Cobre + isolamento |
| Linhas de Dreno | 14.02.003 | PVC + sifões |
| Instalações Elétricas | 14.02.004 | Cabos, eletrodutos, disjuntores |
| Suportes e Acessórios | 14.02.005 | Suportes, abraçadeiras, registros |
| Automação e Controle | 14.02.006 | Termostatos, controles (se aplicável) |

---

## 9. Estratégia de Processamento

### 9.1 Conversão do Arquivo DWG

**Opção 1: ODA File Converter (gratuito)**
```bash
# Baixar: https://www.opendesign.com/guestfiles/oda_file_converter
# Instalar e executar:
ODAFileConverter "RA_ARC_EXE_00_TODAS CAD_R05.dwg" "output" "ACAD2018" "DXF" "0" "1"
```

**Opção 2: LibreCAD (código aberto)**
```bash
# Abrir o DWG no LibreCAD
# File → Export → DXF
```

**Opção 3: AutoCAD (comercial)**
```bash
# Abrir o DWG no AutoCAD
# File → Save As → AutoCAD DXF (*.dxf)
```

### 9.2 Extração Automatizada

Após conversão para DXF, utilizar o script Python criado:

```bash
python3.11 scripts/extrair_ar_condicionado_dwg.py "caminho/para/arquivo.dxf"
```

O script irá:
1. Listar layers disponíveis no arquivo
2. Identificar blocos (equipamentos)
3. Extrair textos com especificações (potências, modelos)
4. Calcular metragens de tubulações por layer
5. Gerar relatório detalhado para preenchimento deste briefing

### 9.3 Processamento Manual (alternativo)

Se a conversão não for viável, processar manualmente:

1. **Abrir DWG em visualizador** (AutoCAD, LibreCAD, DraftSight)
2. **Identificar layers relevantes:**
   - `AC_EQUIPAMENTOS` ou similar (condensadoras, evaporadoras)
   - `AC_TUBULACAO` ou `AC_FRIGORIFICA` (linhas de gás/líquido)
   - `AC_DRENO` (linhas de drenagem)
   - `AC_ELETRICA` (alimentação)
3. **Extrair dados manualmente:**
   - Fazer contagem de blocos (equipamentos)
   - Ler textos com especificações
   - Medir comprimentos de linhas (comando `LIST` ou `MEASUREGEOM`)
4. **Preencher as tabelas deste briefing**

---

## 10. Histórico de Revisões

| Revisão | Data | Arquivos Recebidos | Mudanças |
|---------|------|--------------------|----------|
| R00 | 20/03/2026 | `RA_ARC_EXE_00_TODAS CAD_R05.dwg` (5,0 MB) | Versão inicial — estrutura do briefing criada, aguardando extração de dados |

---

## 11. Observações Finais

### 11.1 Limitações Técnicas Identificadas

1. **Formato DWG nativo:** O arquivo está em formato binário AutoCAD, que não é legível por bibliotecas Python abertas (ezdxf)
2. **Conversores não disponíveis:** O sistema atual não possui ODA File Converter, AutoCAD ou LibreCAD instalados
3. **Processamento manual necessário:** Até que a conversão seja realizada, os quantitativos precisam ser extraídos manualmente

### 11.2 Recomendações

1. **Curto prazo (urgente):**
   - Solicitar ao projetista o arquivo em formato DXF (mais fácil de processar)
   - OU solicitar planilha de quantitativos do projetista
   - OU solicitar memorial descritivo com lista de equipamentos

2. **Médio prazo:**
   - Instalar ODA File Converter no sistema para conversões futuras
   - Criar biblioteca de arquivos DXF de referência para calibrar extração automatizada

3. **Longo prazo:**
   - Padronizar recebimento de projetos em formato IFC (disciplinas compatíveis com BIM)
   - Treinar projetistas para incluir propriedades estruturadas nos modelos

### 11.3 Impacto no Orçamento

Até que os quantitativos sejam extraídos:
- **Orçamento paramétrico:** Usar índices de R$/m² para climatização (base de calibração Cartesian)
- **Orçamento executivo:** Pausado até extração ou recebimento de dados complementares
- **Prazo estimado:** Depende da disponibilidade do projetista ou ferramentas de conversão

---

*Briefing gerado por Cartesiano | Status: PRELIMINAR — Aguardando extração de dados*  
*Próxima ação: Converter DWG → DXF e executar script de extração automatizada*
