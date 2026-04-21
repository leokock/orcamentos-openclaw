# Análise DXF — PCI Electra Towers (Civil + Elétrico)

**Data:** 25/03/2026
**Fontes:** 8 DXFs IGC (PCI Civil) + 18 DXFs PEE (PCI Elétrico)

---

## 1. PCI Civil (IGC) — Tubulação e Equipamentos

### Comparação IFC vs DXF

| Dado | IFC (R00) | DXF (novo) | Diferença |
|------|-----------|------------|-----------|
| **Tubulação total** | 67,3m | **10.550m** | 157× maior |
| **Hidrantes/abrigos** | 67 un | 110 un | +64% |
| **Válvulas** | 138 un | 1.489 un | +979% |
| **Conexões** | 272 un | 6.008 un | +2.109% |

⚠️ **ATENÇÃO:** Os DXFs IGC são de *gás canalizado* (Instalação de Gás Canalizado, não Incêndio Civil). Os blocos identificados são tubos de cobre A'Melo (gás) e cotovelos/válvulas de gás. A metragem de 10.550m é do **sistema de gás**, não do incêndio.

A tubulação real de PCI (ferro galvanizado vermelho) está nos IFCs PCI (não IGC). Os 67m do IFC continuam sendo a única fonte de tubulação de incêndio — e continua subestimada.

### Quantitativos DXF por UC — Sistema de Gás (IGC)

| UC | Tubulação (m) | Válvulas | Hidrantes/Reg | Conexões |
|----|--------------|----------|---------------|----------|
| **Embasamento** | 726,6 | 145 | 14 | 104 |
| - Térreo | 187,0 | 57 | 10 | 16 |
| - Garagem (×5) | 54,6/piso | 12/piso | - | - |
| - Lazer | 266,7 | 28 | 4 | 88 |
| **Torre A (Tipo ×24)** | 4.230,0 | 696 | 48 | 2.976 |
| - Por piso tipo | 176,2 | 29 | 2 | 124 |
| **Torre B (Tipo ×24)** | 5.594,1 | 648 | 48 | 2.928 |
| - Por piso tipo | 233,1 | 27 | 2 | 122 |
| **TOTAL** | **10.550,7** | **1.489** | **110** | **6.008** |

---

## 2. PCI Elétrico (PEE) — Alarme e Emergência

Dados extraídos dos 18 DXFs PEE (R. Rubens Alves, rev.01).

### Quantitativos por UC

| UC / Pavimento | Ilum. Emergência | Sirene Alarme | Sinalização | Detector Fumaça | Acionador Manual |
|----------------|-----------------|---------------|-------------|-----------------|-----------------|
| **EMBASAMENTO** | **257** | **54** | **42** | **23** | **0** |
| - Térreo | 41 | 13 | 11 | - | - |
| - G1 | 37 | 5 | 2 | - | - |
| - G2 | 36 | 5 | 2 | - | - |
| - G3 | 36 | 5 | 2 | - | - |
| - G4 | 33 | 5 | 2 | - | - |
| - G5 | 33 | 5 | 2 | 23 | - |
| - Lazer | 41 | 16 | 21 | - | - |
| **TORRE A** | | | | | |
| - Tipo (×1) | 5 | 1 | 1 | - | 1 |
| - Tipo (×24) | **120** | **24** | **24** | - | **24** |
| - Casa de Máquinas | 7 | - | 2 | - | - |
| - *Subtotal T.A* | *127* | *24* | *26* | *-* | *24* |
| **TORRE B** | | | | | |
| - Tipo (×1) | 6 | 1 | 1 | - | - |
| - Tipo (×24) | **144** | **24** | **24** | - | - |
| - Casa de Máquinas | 7 | - | 2 | - | - |
| - *Subtotal T.B* | *151* | *24* | *26* | *-* | *-* |
| **TOTAL GERAL** | **535** | **102** | **94** | **23** | **24** |

### Observações PCI Elétrico
- **Detectores de fumaça** só na G5 (23un) — provavelmente próximo a lixeira/depósito
- **Acionadores manuais** só na Torre A Tipo (1/piso) — verificar se Torre B não tem mesmo ou se é erro na prancha
- **Iluminação de emergência** é o item mais numeroso (535 total)

---

## 3. Conclusões e Recomendações

### O que os DXFs confirmaram
✅ Dados detalhados de PCI Elétrico (alarme, iluminação, sinalização) — não estavam disponíveis antes
✅ Estrutura por pavimento/torre — confirma padrão de repetição

### O que NÃO resolveu
❌ Tubulação de incêndio — os DXFs IGC são de gás, não de PCI
❌ Metragem real de tubulação FG — continua com 67m do IFC (subestimado)
❌ Bombas e reservatórios — não aparecem em nenhuma fonte

### Recomendação
1. **Para tubulação PCI real:** Solicitar memorial descritivo do projetista ou processar os IFCs PCI com script mais robusto (validar geometria)
2. **Para planilha R03:** Incorporar dados de PCI Elétrico (alarme, iluminação, sinalização, detectores) que agora temos completos
3. **Para bombas:** Estimar com base em NBR 13714 ou solicitar especificação

---

*Análise gerada em 25/03/2026*
