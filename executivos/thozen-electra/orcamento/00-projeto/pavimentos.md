---
pavimentos:
  - id: "TERREO"
    nome: "Térreo"
    quantidade: 1
    area_m2: 1565.91
    tipo: "embasamento"
    computada: false
    pe_direito_m: 4.30
    notas: "Térreo + garagem + salas comerciais + halls"
  - id: "G1"
    nome: "Garagem 01"
    quantidade: 1
    area_m2: 1736.27
    tipo: "garagem"
    computada: false
    pe_direito_m: null
  - id: "G2"
    nome: "Garagem 02"
    quantidade: 1
    area_m2: 1736.27
    tipo: "garagem"
    computada: false
    pe_direito_m: null
  - id: "G3"
    nome: "Garagem 03"
    quantidade: 1
    area_m2: 1736.27
    tipo: "garagem"
    computada: false
    pe_direito_m: null
  - id: "G4"
    nome: "Garagem 04"
    quantidade: 1
    area_m2: 1736.27
    tipo: "garagem"
    computada: false
    pe_direito_m: null
  - id: "G5"
    nome: "Garagem 05"
    quantidade: 1
    area_m2: 1736.27
    tipo: "garagem"
    computada: false
    pe_direito_m: null
  - id: "LAZER"
    nome: "Pavimento diferenciado — Lazer"
    quantidade: 1
    area_m2: 1736.27
    tipo: "lazer"
    computada: false
    pe_direito_m: 3.60
  - id: "TIPO_A"
    nome: "Pavimento tipo — Torre A"
    torre: "A"
    quantidade: 24
    area_pavto_m2: 530.02
    area_total_m2: 12720.48
    tipo: "tipo"
    computada: true
    pe_direito_m: 3.24
  - id: "TIPO_B"
    nome: "Pavimento tipo — Torre B"
    torre: "B"
    quantidade: 24
    area_pavto_m2: 537.18
    area_total_m2: 12892.32
    tipo: "tipo"
    computada: true
    pe_direito_m: 3.24
  - id: "CASA_MAQ"
    nome: "Casa de Máquinas"
    quantidade: 1
    area_m2: 176.26
    tipo: "tecnico"
    computada: false
    pe_direito_m: null
  - id: "RESERVATORIO"
    nome: "Reservatórios"
    quantidade: 1
    area_m2: 121.30
    tipo: "tecnico"
    computada: false
    pe_direito_m: null

resumo:
  total_pavtos_distintos: 11
  total_pavtos_fisicos: 53
  total_area_construida_m2: 37893.89
  pavtos_computados: 48
  pavtos_nao_computados: 5

fontes:
  - "Quadro de Áreas oficial (print 2026-04-21)"
  - "IFC arquitetura (storeys)"
  - "PROJETO.md de ~/orcamentos/projetos/thozen-electra/"
---

# Pavimentos — Electra Towers

## Visão geral

O empreendimento tem **53 pavimentos físicos** organizados em 11 tipos distintos:

- **Embasamento** (não computado): Térreo + 5 Garagens + Lazer = 7 pavtos
- **Pavimentos Tipo Torre A** (computados): 24 pavtos × 530,02 m²
- **Pavimentos Tipo Torre B** (computados): 24 pavtos × 537,18 m²
- **Cobertura técnica** (não computada): Casa de Máquinas + Reservatórios = 2 pavtos

## Tabela completa

| Pavimento | Qtd | Área pavto | Área total | Computada | Pé-direito |
|---|---:|---:|---:|:---:|---:|
| Térreo | 1 | 1.565,91 m² | 1.565,91 m² | ❌ | 4,30 m |
| Garagem 01 | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | — |
| Garagem 02 | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | — |
| Garagem 03 | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | — |
| Garagem 04 | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | — |
| Garagem 05 | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | — |
| Pavimento diferenciado Lazer | 1 | 1.736,27 m² | 1.736,27 m² | ❌ | 3,60 m |
| **Pavimento tipo — Torre A** | **24** | **530,02 m²** | **12.720,48 m²** | ✅ | 3,24 m |
| **Pavimento tipo — Torre B** | **24** | **537,18 m²** | **12.892,32 m²** | ✅ | 3,24 m |
| Casa de Máquinas | 1 | 176,26 m² | 176,26 m² | ❌ | — |
| Reservatórios | 1 | 121,30 m² | 121,30 m² | ❌ | — |
| **TOTAL** | **53** | — | **37.893,89 m²** | | |

## Notas

- **Subsolos:** 0 (todas garagens são acima do nível do solo, em pavimentos elevados)
- **Diferença de área entre Torre A (530,02) e Torre B (537,18):** ~7 m² por pavto. Verificar se é intencional (provavelmente compensação de geometria do lote)
- **Embasamento compartilhado:** Térreo + Garagens + Lazer atendem as 2 torres
