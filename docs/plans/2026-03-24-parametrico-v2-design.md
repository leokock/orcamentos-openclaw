# Design: Parametrico V2 — Calculo Bottom-Up com PUs Reais

> **Objetivo:** Reformular o script parametrico para calcular Qtd x PU (bottom-up) em vez de distribuir por % (top-down), mantendo o macro como benchmark
> **Origem:** Revisao da Patricia (coordenadora custos) no parametrico do Now (Cambert)
> **Criado:** 24/mar/2026
> **Status:** Now V2 FINAL gerado (R$ 3.389/m², 18/18 BU). Calibracao completa (75 exec + 79 narrativos + IFC). Proximo: script generico.
> **Validacao:** Now V2 vs Patricia (~R$ 3.500): -3.2% | vs Connect (R$ 3.420): -0.9% | vs seg 8-15k (R$ 3.217): +5.3%
> **Arquivo de calibracao:** ~/orcamentos/base/calibration-indices.json (75 exec, 2.199 insumos ABC, 13 indices master)

---

## 1. Problema Atual

O `gerar_template_dinamico.py` calcula detalhes TOP-DOWN:
```
Macrogrupo Total (Base x CUB x Briefing)
  -> Distribui por % fixo pros sub-itens
    -> PU = Total / Qtd (calculado pra tras)
```

Problemas identificados pela Patricia:
1. PUs absurdos (R$ 1.600/m3 concreto — embute MO invisivel)
2. Briefing nao cascateia (protensao nao muda forma/aco/escoramento)
3. Itens faltantes (~15 itens de gerenciamento, piscina, serralheria)
4. EPCs como % (15%) em vez de valor fixo (~R$ 300k)
5. Equipe ADM com custos irreais (engenheiro R$ 20k CLT vs R$ 12-15k PJ)
6. MO misturada com material
7. Dados de entrada sem validacao (subsolo inventado no Now)

Resultado: R$ 4.400/m2 (fora do benchmark) vs R$ 3.500/m2 (Patricia, alinhado)

---

## 2. Modelo Hibrido (2 Camadas)

### Camada 1 — MACRO (mantem como esta)
```
Base (mediana 75 exec, dez/23) x Fator CUB x Fator Briefing = Total Macrogrupo
```
Serve como BENCHMARK de sanidade. Nao muda.

### Camada 2 — DETALHE (muda pra bottom-up)
```
Qtd = Indice x AC (mantem os indices atuais)
PU = valor de mercado (base PUs Cartesian, 1.504 itens)
Total = Qtd x PU
Soma itens = Total da disciplina
```

### Validacao automatica
```
Se |Camada1 - Camada2| > 15% -> alerta amarelo na aba ALERTAS
Se |Camada1 - Camada2| > 30% -> alerta vermelho
```
O usuario decide qual usar. Default: Camada 2 (bottom-up).

---

## 3. Briefing com Perfis de Detalhe

Cada resposta do briefing, alem de mudar o FATOR do macrogrupo, seleciona um PERFIL de detalhe.

### Exemplo: Laje

| Parametro | Convencional | Protendida |
|-----------|-------------|------------|
| Forma vigas | 30% da forma total | 5% da forma total |
| Forma lajes | 35% | 60% |
| Aco convenc. | 100 kg/m3 | 45 kg/m3 |
| Cordoalha | 0 | 8 kg/m2 laje |
| Escoramento | nao | sim (R$/m2 laje) |
| PU concreto | fck30 R$ 590/m3 | fck40 R$ 690/m3 |

### Exemplo: Contencao

| Parametro | Sem subsolo | Com subsolo |
|-----------|------------|-------------|
| Contencao | R$ 0 | R$/m2 x profundidade |
| Fundacao | so fundacao | fundacao + contencao |
| Impermeab. | normal | + pesada |
| Mov. Terra | minimo | escavacao profunda |

### Exemplo: Climatizacao (novo — Patricia abriu por pontos)

| Parametro | Valor |
|-----------|-------|
| Split por apto | ~2 un/apto x UR |
| Exaustao banheiro | banheiros enclausurados x pav |
| Exaustao churrasqueira | churrasqueiras/pav + lazer |
| Pressurizacao | sim/nao (briefing) |
| Piscina aquecimento | se houver |

Perfis extraidos dos 75 executivos ja processados.

---

## 4. Itens Faltantes

### Gerenciamento (adicionar)
- Estagiario (~R$ 2k/mes)
- Encarregado (~R$ 5-6k/mes)
- Equipe de limpeza (~R$ 3k/mes)
- Meio ambiente
- Operacao inicial / limpeza inicial
- Instalacoes provisorias
- Despesas de consumo
- Demolicao (se aplicavel)

### EPCs — valor FIXO por porte
| Porte | AC | EPCs |
|-------|-----|------|
| Pequeno | <5.000 m2 | ~R$ 150k |
| Medio | 5-15.000 m2 | ~R$ 300k |
| Grande | >15.000 m2 | ~R$ 500k |

### Equipe ADM — calculo por cargo
```
Custo = Qtd pessoas x Custo/mes x Prazo (meses)
```
PJ (realidade de mercado), nao CLT.

### Sistemas Especiais (adicionar)
- Piscina / equipamentos
- Gerador proporcional ao porte (nao fixo R$ 500k)
- Serralheria (nas esquadrias)

---

## 5. Separacao MO / Material

Toda aba de detalhe tem 3 colunas:
- **Material (R$)** — PU de mercado
- **MO (R$)** — R$/m2 ou % do material
- **Total (R$)** — Material + MO

Ratios MO/Material por disciplina (extrair da base):
| Disciplina | MO% | Material% |
|-----------|-----|-----------|
| Estrutura | 35-40% | 60-65% |
| Instalacoes | 55% | 45% |
| Acabamentos | 40-50% | 50-60% |
| Pintura | 60% | 40% |
| Impermeabilizacao | ~45% | ~55% |

---

## 6. Validacao de Dados de Entrada

Antes de gerar, apresentar dados para confirmacao:
- AC Total (priorizar quadro de areas oficial)
- UR, pavimentos, subsolos (default 0)
- Elevadores, vagas, prazo
- Fonte dos dados

Regras:
- Subsolos = 0 como default
- Se dados vem de RVT/IFC, marcar "extraido — confirmar"
- Flag se AC diverge >5% de outra fonte

---

## 7. Calibracao Realizada (24/mar/2026)

### Passos executados:
1. **Curva ABC**: 2.199 insumos extraidos de 38 projetos detalhados (3.760 entradas)
2. **Executivos**: 75/75 processados (0 pendentes)
3. **Narrativos**: 79 arquivos .md parseados (custos equipe, indices estruturais)
4. **SINAPI**: Pulado (dados internos suficientes)
5. **IFC real**: Electra Towers (concreto 0,396 m³/m², eletrico R$ 207/m²)

### Indices Master Calibrados:
| Disciplina | Indice | Valor | Fonte (n projetos) |
|---|---|---|---|
| Supraestrutura | concreto m³/m² AC | 0,22 (prot) / 0,25 (conv) | 7 exec + 9 narrativos |
| Supraestrutura | aco kg/m³ | 70 (prot) / 106 (conv) | 7 exec + 11 narrativos |
| Supraestrutura | forma m²/m³ | 6,05 (prot) / 7,12 (conv) | 7 exec |
| Inst. Eletricas | eletroduto m/m² AC | 1,77 | 9 exec |
| Inst. Eletricas | pontos/UR | 39,05 | 12 exec |
| Inst. Hidro | tubulacao m/m² AC | 1,075 | 8 exec |
| Pisos | area piso/m² AC | 1,70 | derivado seg 8-15k |
| Rev. Parede | area parede/m² AC | 2,85 | derivado |
| Teto | area forro/m² AC | 1,16 | derivado |
| Pintura | area superfície/m² AC | 5,65 | derivado |
| Fachada | area fachada/m² AC | 1,55 | derivado seg 8-15k |
| Impermeab. | area/m² AC | 0,37 | derivado |
| Alvenaria | area/m² AC | 2,25 | derivado |

### Equipe ADM (79 narrativos):
| Cargo | Mediana R$/mes | N projetos |
|---|---|---|
| Engenheiro PJ | 10.500 | 5 |
| Mestre | 9.940 | 4 |
| Almoxarife | 3.377 | 4 |
| Estagiario | 1.580 | 3 |
| EPCs fixo medio | 300.000 | 75 |

### Split MO/Material (38 exec):
| Disciplina | MO% | N |
|---|---|---|
| Supraestrutura | 32,6% | 10 |
| Alvenaria | 35,7% | 9 |
| Inst. Eletricas | 38,2% | 11 |
| Inst. Hidro | 34,0% | 7 |
| Pintura | 66,2% | 7 |
| Revestimentos | 54,4% | 7 |
| Impermeab. | 56,5% | 6 |
| Esquadrias | 10,5% | 7 |

---

## 8. Resultado — Now Residence (Cambert)

| Metrica | Valor |
|---|---|
| R$/m² | 3.389 |
| CUB Ratio | 1,12 |
| Total | R$ 44,7M |
| Itens | 124 |
| Macrogrupos BU | 18/18 |
| vs Patricia (~3.500) | -3,2% |
| vs Connect (3.420) | -0,9% |
| vs Seg 8-15k (3.217) | +5,3% |

Validacao: 14 macrogrupos ✓ (<20%), 3 ⚠ (20-35%), 1 ✗ intencional (climatizacao +40% por pontos Patricia)

---

## 9. Ordem de Implementacao do Script Generico

| Prioridade | Mudanca | Status |
|-----------|---------|--------|
| 1 | Inverter calculo (Qtd x PU) | ✅ Validado no Now |
| 2 | Conectar base de PUs (calibration-indices.json) | ✅ Arquivo pronto |
| 3 | Perfis de briefing (convencional vs protendida) | ✅ Indices definidos |
| 4 | Itens faltantes + EPCs fixo + equipe calibrada | ✅ Validado no Now |
| 5 | Separacao MO/material (splits reais) | ✅ 18 disciplinas calibradas |
| 6 | Validacao de entrada (AC, subsolos, UR) | Pendente |
| 7 | Segmentacao por porte (4 faixas) | ✅ Dados prontos |

Proximo passo: transformar o script do Now num template generico (gerar_template_dinamico_v2.py).

---

*Baseado na revisao da Patricia (coordenadora custos Cartesian).*
*Calibracao completa: 75 exec + 79 narrativos + IFC + curva ABC.*
*Aprovado por Leo em 24/mar/2026.*
