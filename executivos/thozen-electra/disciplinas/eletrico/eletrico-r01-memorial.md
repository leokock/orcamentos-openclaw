# Memorial Descritivo — Instalacoes Eletricas

**Projeto:** Thozen Electra Towers
**Disciplina:** 09 ELETRICO
**Revisao:** R01 (Piloto IA)
**Data:** 23/03/2026
**Responsavel:** Cartesiano + Claude Code (piloto de processo)

---

## 1. Dados do Empreendimento

| Item | Valor |
|------|-------|
| Area Construida | 36.088,85 m2 |
| Unidades Residenciais | 342 |
| Unidades Comerciais | 6 |
| Pavimentos | 24 (Terreo + Garagens + Lazer + 24 Tipos + Casa de Maquinas) |
| Subsolos | 1 |
| Vagas | 305 |
| Prazo de Obra | 36 meses |
| CUB/SC Referencia | R$ 3.019,26 (fev/2026) |

---

## 2. Valor Total e Benchmark

| Item | Valor |
|------|-------|
| **Total Instalacoes Eletricas** | **R$ 6.856.881,50** |
| **R$/m2** | **R$ 190,00** |

### Validacao Parametrica

| Referencia | R$/m2 | Comparacao |
|-----------|-------|------------|
| Electra (este orcamento) | R$ 190,00 | — |
| Elizabeth II R01 (alto padrao, Itapema) | R$ 213,09 | -10,8% |
| Faixa parametrica (alto padrao vertical) | R$ 150-250 | DENTRO DA FAIXA |

**Analise:** O valor de R$ 190/m2 esta dentro da faixa esperada para empreendimento residencial vertical de medio-alto padrao em Porto Belo/SC. O valor abaixo do Elizabeth II (R$ 213/m2) se justifica por:
- Elizabeth II tem padrao mais alto (Itapema, fachada premium)
- Electra tem maior area (36k vs 17k m2), gerando economia de escala em infraestrutura fixa (subestacao, gerador, entrada)

---

## 3. Fontes de Dados

### 3.1 Arquivos IFC Processados (fonte primaria para quantitativos)

| Arquivo | Pavimento | Status |
|---------|-----------|--------|
| 348 - E01 rev.01 - 01 PAVTO. TERREO.ifc | Terreo | Processado |
| 348 - E02 rev.01 - 02 PAVTO. G1.ifc | Garagem 1 | Processado |
| 348 - E03 rev.01 - 03 PAVTO. G2.ifc | Garagem 2 | Processado |
| 348 - E04 rev.01 - 04 PAVTO. G3.ifc | Garagem 3 | Processado |
| 348 - E05 rev.01 - 05 PAVTO. G4.ifc | Garagem 4 | Processado |
| 348 - E06 rev.01 - 06 PAVTO. G5.ifc | Garagem 5 | Processado |
| 348 - E07 rev.01 - 07 PAVTO. LAZER.ifc | Lazer | Processado |
| 348 - E08 rev.01 - 08~31 PAVTO. TIPO (24x).ifc | Tipo (x24) | Processado |
| 348 - E09 rev.01 - CASA DE MAQUINAS.ifc | Casa Maq. | Processado |

**Schema:** IFC2X3 (geometria 3D completa, propriedades tecnicas limitadas)
**Projetista:** R. Rubens Alves
**Revisao dos arquivos:** rev.01

### 3.2 Arquivos DWG Disponiveis (nao processados nesta revisao)

18 pranchas DWG em `projetos/09 ELETRICO/DWG/` — contendo diagramas unifilares, tabelas de quadros, especificacoes tecnicas. Processamento recomendado para R02.

### 3.3 Referencia de Precos

- **Base primaria:** Elizabeth II Royal Home (Gessele, Itapema) — R01, fev/2026
- **Ajuste:** Distribuicao percentual por subgrupo calibrada com Elizabeth II
- **CUB:** R$ 3.019,26/m2 (SC, fev/2026)

---

## 4. Distribuicao por Subgrupo

| Subgrupo | Valor (R$) | % | R$/m2 |
|----------|-----------|---|-------|
| SUBESTACAO | 1.234.238,67 | 18,0% | 34,20 |
| BARRAMENTO | 466.267,94 | 6,8% | 12,92 |
| GERADOR | 479.981,71 | 7,0% | 13,30 |
| ENTRADA DE ENERGIA | 850.253,31 | 12,4% | 23,56 |
| ELETRODUTOS | 164.565,16 | 2,4% | 4,56 |
| CABO UNIPOLAR | 452.554,18 | 6,6% | 12,54 |
| DISPOSITIVOS DE PROTECAO | 123.423,87 | 1,8% | 3,42 |
| CAIXAS 4x2" E 4x4" | 116.566,99 | 1,7% | 3,23 |
| MODULOS | 109.710,10 | 1,6% | 3,04 |
| QUADROS DE DISTRIBUICAO | 34.284,41 | 0,5% | 0,95 |
| CAIXA OCTOGONAL | 20.570,64 | 0,3% | 0,57 |
| SENSORES | 6.856,88 | 0,1% | 0,19 |
| MAO DE OBRA ELETRICA | 2.797.607,65 | 40,8% | 77,52 |
| **TOTAL** | **6.856.881,50** | **100%** | **190,00** |

---

## 5. Quantitativos Extraidos dos IFCs

### 5.1 Luminarias

**Total estimado: 4.655 unidades**

| Pavimento | Luminarias (modelo) | Multiplicador | Total |
|-----------|-------------------|---------------|-------|
| Terreo | 140 | x1 | 140 |
| Garagem G1 | 77 | x1 | 77 |
| Garagem G2 | 80 | x1 | 80 |
| Garagem G3 | 80 | x1 | 80 |
| Garagem G4 | 78 | x1 | 78 |
| Garagem G5 | 97 | x1 | 97 |
| Lazer | 119 | x1 | 119 |
| Tipo (8~31) | 166 | x24 | 3.984 |
| Casa de Maquinas | 0 | x1 | 0 |
| **Total** | **837** | — | **4.655** |

### 5.2 Eletrodutos por Diametro

**Total estimado: ~213.000 trechos** (com multiplicacao tipo x24)

| Diametro | Aplicacao Tipica | Trechos Estimados |
|----------|-----------------|-------------------|
| 3/4" (20mm) | Iluminacao | ~168.000 |
| 1" (25mm) | Forca/Tomadas | ~13.000 |
| 1 1/4" (32mm) | Alimentadores | ~11.600 |
| 1 1/2" (40mm) | Prumadas | ~11.100 |
| 2" (50mm) | Alimentacao geral | ~220 |
| 3" (75mm) | Entrada/Barramento | ~2.340 |
| 4" (100mm) | Infraestrutura principal | ~15 |

**Nota:** Comprimentos lineares nao foram extraidos (geometria IFC2X3 complexa). Metragens devem ser estimadas por indice ou extraidas dos DWGs.

---

## 6. Premissas Adotadas

1. **R$/m2 de referencia:** R$ 190,00/m2 (conservador, abaixo do Elizabeth II que e alto padrao puro)
2. **Distribuicao por subgrupo:** Proporcional ao Elizabeth II R01
3. **Mao de obra:** Estimada em ~41% do total (padrao Elizabeth II)
4. **Pavimento tipo:** Multiplicado por 24 pavimentos (conforme IFC E08)
5. **Precos unitarios:** Nao detalhados nesta revisao — usar PUs do Elizabeth II como referencia ate obter cotacoes especificas
6. **Gerador:** Considerado (empreendimento >300 UR requer gerador)
7. **Subestacao:** Considerada entrada em MT (porte >300 UR)

---

## 7. Limitacoes e Proximos Passos

### Limitacoes desta revisao (R01)
- Comprimentos lineares de eletrodutos e cabos nao calculados
- Especificacoes tecnicas (potencias, bitolas) nao extraidas dos IFCs
- Quadros eletricos, tomadas e interruptores nao modelados nos IFCs
- PUs nao detalhados por item (apenas distribuicao parametrica)

### Acoes para R02
1. Processar 18 DWGs para extrair especificacoes tecnicas
2. Detalhar itens por subgrupo com PUs especificos
3. Obter cotacoes de subestacao e gerador
4. Calcular metragens lineares de eletrodutos e cabos
5. Detalhar quadros eletricos por pavimento

---

*Gerado por Cartesiano + Claude Code em 23/03/2026 — Piloto de processo de orcamento executivo com IA*
