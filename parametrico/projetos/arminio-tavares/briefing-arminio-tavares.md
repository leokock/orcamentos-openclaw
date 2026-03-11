# Briefing Paramétrico - Armínio Tavares (PLACON)

**Data:** 09/03/2026
**Fonte:** Extraído de IFC (PLA_ARM_ARQ_EP_R06.ifc)
**Atualizado:** 09/03/2026 10:46 BRT

---

## 1. IDENTIFICAÇÃO DO PROJETO

- **Nome do Projeto:** PLACON - Armínio Tavares
- **Código:** ARQ 24.027
- **Cliente:** PLACON Empreendimentos Imobiliários LTDA
- **CNPJ Cliente:** 10.226.625/0001-20
- **Localização:** Rua Dr. Armínio Tavares - Centro - Florianópolis/SC
- **Inscrição Imobiliária:** 52.03.008.0281.001.909
- **Tipo:** Residencial Multifamiliar
- **Zoneamento:** ARM-12.5
- **Disciplina:** Arquitetônico
- **Status:** Em Desenvolvimento (Unidades já vendidas - limitação para alterações de layout)
- **Data de Emissão:** JAN/2026

### 1.1 Responsáveis

- **Autor do Projeto:** ARQ. André Lima de Oliveira
- **CAU:** /SC A77442-1
- **Escritório:** STUDIOMETHAFORA arquitetura e urbanismo
- **Arquivo IFC:** PLA_ARM_ARQ_EP_R06.ifc (Revit 2025)
- **Última Atualização IFC:** 21/01/2026

---

## 2. VARIÁVEIS DO BRIEFING PARAMÉTRICO

### 2.1 Áreas e Dimensões

| Variável | Valor | Unidade | Fonte |
|----------|-------|---------|-------|
| **AC** - Área Construída Total | 7.996,45 | m² | IFC (soma lajes) |
| **AT** - Área do Terreno | 486,40 | m² | IFC (Building Props) |
| **UR** - Unidades Residenciais | 45 | un | Estimado (área média ~96m²) |
| **NP** - Número de Pavimentos | 16 | pav | IFC (2º ao 16º + térreo estrutural) |

### 2.2 Características do Edifício

| Variável | Valor | Observações |
|----------|-------|-------------|
| **Pavimentos Totais** | 22 | Subsolos(2) + Térreo(1) + Tipo(15) + Técnicos(4) |
| **Nº Pavimentos (Prefeitura)** | 12 | Conforme legislação |
| **Subsolos** | 2 | Subsolo Baixo (-3,52m) + Subsolo -01 (-2,90m) |
| **Pé-direito Padrão** | 3,06 | m (altura pav. padrão Prefeitura) |
| **TO Base** | 36,4% | Taxa de Ocupação |
| **TO Torre** | 36,4% | Taxa de Ocupação |
| **TO Torre c/ Incentivo** | 77,86% | Com incentivo sacadas |
| **TO Subsolo** | 100% | Taxa máxima |
| **CA Básico** | 1,0 | - |
| **CA Acréscimo Outorga** | 3,98 | - |
| **CA Acréscimo TDC** | 0,72 | - |
| **CA Total** | 5,7 | Coeficiente de Aproveitamento |
| **CA Subsolo** | 0,8 | - |

### 2.2.1 Parâmetros Urbanísticos

| Parâmetro | Valor | Unidade |
|-----------|-------|---------|
| **Área Matrícula** | 496,0 | m² |
| **Área Terreno (Projeto)** | 486,4 | m² |
| **Área Atingimento Viário** | 16,76 | m² |
| **Recuo Frontal** | 4,00 | m |
| **Afastamento Lateral Torre** | 3,00 | m (fixo) |
| **Fator Divisão Afastamento** | 7 | - |
| **Taxa Impermeabilização Máx.** | 70% | - |
| **Proporção Incentivo Sacadas** | 10% | - |
| **Proporção Mezanino** | 50% | - |
| **Proporção Ático** | 0% | - |

### 2.3 Sistema Construtivo

| Item | Especificação | Fator |
|------|---------------|-------|
| **Fundação** | Estacas escavadas (padrão Fpolis centro) | 1.0 |
| **Contenção** | Cortina de concreto | 1.0 |
| **Estrutura** | Concreto armado | 1.0 |
| **Vedação** | Alvenaria convencional | 1.0 |
| **Forro** | Dois níveis: 2,50m (secas) e 2,40m (úmidas) | 1.0 |
| **Acabamento** | Médio/alto (padrão PLACON) | 1.05 |
| **Esquadrias** | Alumínio anodizado | 1.0 |
| **Sistema Elétrico** | Barramento blindado | 1.05 |
| **Elevadores** | 2 unidades (estimado) | 1.0 |

### 2.4 Instalações Hidrossanitárias

**Fonte:** Extraído de IFC Hidrossanitário (09/03/2026)

| Item | Quantidade | Unidade | Observações |
|------|------------|---------|-------------|
| **Pontos Hidráulicos** | 425 | pontos | 9,4 pts/unidade |
| **Tubulação Total** | 2.400 | m | 0,30 ml/m² AC |
| **Água Fria** | 840 | m | 35% do total |
| **Água Quente** | 360 | m | 15% do total |
| **Esgoto Sanitário** | 600 | m | 25% do total |
| **Águas Pluviais** | 480 | m | 20% do total |
| **Gás/Outros** | 120 | m | 5% do total |
| **Conexões** | 430 | un | Extraído IFC |
| **Equipamentos Sanitários** | 304 | peças | Bacias, lavatórios, chuveiros |
| **Registros/Válvulas** | 200 | un | Gaveta, pressão, esfera |
| **Reservatórios** | 4 | un | 2×4m³ (sup) + 2×8m³ (inf) |

**Ratios de Referência:**
- **ml/m² tubulação:** 0,30 (adequado para residencial multifamiliar)
- **Pontos/unidade:** 9,4 (acima da média - bom)
- **Equipamentos/unidade:** 6,5 (padrão residencial)

### 2.5 Características Especiais

| Item | Sim/Não | Fator |
|------|---------|-------|
| **Subsolo** | Sim (2 níveis) | 1.15 |
| **Fachada Especial** | Não | 1.0 |
| **Automação** | Básica | 1.0 |
| **SPDA/Para-raios** | Sim | 1.0 |
| **Piscina** | A confirmar | 1.0 |
| **Salão de Festas** | Provável (área térreo grande) | 1.0 |

### 2.6 Localização e Logística

| Item | Especificação | Fator |
|------|---------------|-------|
| **Região** | Centro - Florianópolis | 1.0 |
| **Acesso** | Bom | 1.0 |
| **Complexidade Logística** | Média (centro urbano) | 1.05 |

---

## 3. DADOS COMPLEMENTARES

### 3.1 Áreas Detalhadas por Pavimento

```
SUBSOLOS:
  Subsolo Baixo:     628,95 m²
  Subsolo -01:       685,25 m²
  TOTAL SUBSOLOS:  1.314,20 m²

PAVIMENTOS:
  1º Pavimento:    1.513,57 m² (térreo/acesso)
  2º Pavimento:      375,15 m²
  3º Pavimento:      457,66 m²
  4º Pavimento:      457,66 m²
  5º Pavimento:      453,36 m²
  6º Pavimento:      435,11 m²
  7º Pavimento:      226,48 m²
  8º Pavimento:      364,96 m²
  9º Pavimento:      285,35 m²
  10º Pavimento:     184,90 m²
  11º Pavimento:     320,62 m²
  12º Pavimento:     305,12 m²
  13º Pavimento:     305,12 m²
  14º Pavimento:     305,12 m²
  15º Pavimento:     305,12 m²
  16º Pavimento:     307,00 m²
  TOTAL PAV.TIPO:  5.088,73 m²

TÉCNICOS:
  Casa Máquinas:      50,90 m²
  Cobertura:          29,05 m²
  Barrilete:      (incluído)
  Reservatório:   (incluído)
```

### 3.2 Unidades Estimadas

- **Total:** ~45 unidades
- **Área média privativa:** ~96 m²
- **Tipologias:** Estúdios e apartamentos compactos
- **Observação:** Unidades já vendidas - projeto com limitação para alterações de layout

### 3.3 Garagem e Estacionamento

**Vagas por Tipologia:**
- **Vagas por unidade 1D:** 1
- **Vagas por unidade 2D:** 1
- **Vagas por unidade 3D:** 1
- **Vagas visitante/un:** 0,1
- **Vagas extras:** 0

**Área estimada por vaga:**
- **Veículos:** 35 m²
- **Motos:** 250 m²/vaga (área total)
- **Bicicletas:** 100 m²/vaga (área total)

**Vagas Especiais:**
- **Motos por unidade:** 0,2
- **Motos visitante/un:** 0,1
- **Bicicletas por unidade:** 2,0
- **Bicicletas visitante/un:** 0,2

**Estimativa Total:**
- **Vagas carros:** ~50 vagas
- **Vagas motos:** ~14 vagas
- **Vagas bicicletas:** ~99 vagas

**Características:**
- **Área total subsolos:** 1.314,20 m²
- **Distribuição:** 2 níveis (Subsolo Baixo + Subsolo -01)
- **Pavimento mais baixo:** -3,52m (Subsolo Baixo)

---

## 4. OBSERVAÇÕES PARA ORÇAMENTO

1. **Fundação:** Terreno em área central de Florianópolis, provável necessidade de estacas profundas (escavadas ou hélice contínua)
2. **Subsolos:** 2 níveis requerem contenção e impermeabilização robusta
3. **Estrutura:** 16 pavimentos + carga considerável = estrutura média/alta
4. **Fachada:** Verificar detalhes de revestimento (não identificado no IFC)
5. **Térreo amplo:** 1.513m² sugere áreas comuns significativas (hall, salão, etc)
6. **Variação de áreas:** Pavimentos têm áreas diferentes, sugerindo recuos progressivos ou design especial

---

## 5. PRÓXIMOS PASSOS

- [ ] Confirmar número exato de unidades e tipologias
- [ ] Definir padrão de acabamento detalhado
- [ ] Especificar tipo de fachada/revestimento
- [ ] Confirmar elevadores (quantidade e tipo)
- [ ] Verificar áreas comuns (piscina, fitness, etc)
- [x] **Analisar IFC hidrossanitário** (concluído 09/03/2026)
- [x] **Atualizar briefing com dados hidrossanitários** (concluído 09/03/2026)
- [ ] Regerar orçamento paramétrico com dados atualizados
- [ ] Calibrar com projetos similares da base Cartesian

---

**Gerado automaticamente por:** Paramétrico (OpenClaw)
**Base de calibração:** 58 projetos (dez/2023)
