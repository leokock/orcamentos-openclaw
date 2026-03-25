# Orçamento Paramétrico — EPC Alto Ribeirão (Florianópolis/SC)
*Gerado em 04/03/2026 — Base: 25 projetos Cartesian*

---

## 1. DADOS DE ENTRADA (extraídos do EPC)

| Dado | Valor | Fonte |
|------|-------|-------|
| Localização | Alto Ribeirão, Florianópolis/SC | EPC |
| Terreno (estimado) | ~6.700 m² | EPC (calculado pelo IA) |
| Potencial Construtivo | 22.728 m² | EPC |
| Zoneamento | AMS 3.5 | EPC |
| IA Total | 3,38 (básico 1 + outorga 1,58 + subsolo 0,8) | EPC |
| TO Base | 80% | EPC |
| TO Torre | 50% + incentivos | EPC |
| Usos | Residencial multifamiliar + comércio varejista | EPC |

## 2. PREMISSAS ADOTADAS (estimativas — sem projeto arquitetônico)

| Parâmetro | Valor | Justificativa |
|-----------|-------|---------------|
| AC | 22.728 m² | Potencial construtivo máximo |
| Padrão | Médio-Alto | Contexto da pergunta do Eduardo |
| UR | ~160 | Proporção similar a Cota365 (176 UR / 17,5k m²) |
| UC | 4-6 | Comércio varejista no térreo |
| NP | 20 | Compatível com AMS 3.5 + porte |
| NPT | 14 | ~70% dos pavimentos |
| APT | ~570 m² | TO torre 50% × projeção estimada |
| AL | ~1.200 m² | ~5% da AC |
| AE | ~5.400 m² | Base + subsolo |
| NS | 1 | Subsolo permitido (IA subsolo 0,8) |
| Laje | Cubetas | Default médio-alto |
| Contenção | Sim (Floripa) | Parede diafragma ou cortina |
| Meses | 42 | Compatível com porte |
| CUB/SC | R$ 3.000 | Referência Nov/2025 |
| Elevadores | 3 | 2 sociais + 1 serviço |
| Churrasqueiras | ~80 | ~0,5 por UR |

## 3. ORÇAMENTO PARAMÉTRICO POR GRUPO

### Método: Índices calibrados pela base de 25 projetos, posicionados na faixa "Alto Padrão SC / Floripa"
### Projetos de referência principal: Cota 365 (17,5k m², Floripa), Neuhaus (14,5k m², 33 pav), D'Lohn (13k m², Floripa), Connect (13k m², Itajaí)

| # | Grupo de Custo | R$/m² | Valor (R$) | % | Ref. base | Obs |
|---|---------------|-------|-----------|---|-----------|-----|
| 1 | Movimentação de Terra | 35 | 795.480 | 1,0% | 23-85 (média 35 s/ subsolo profundo) | 1 subsolo → mov. terra moderada |
| 2 | Contenção | 150 | 3.409.200 | 4,1% | 91-207 (Floripa range) | Floripa = contenção cara, estimei no meio |
| 3 | Infraestrutura | 185 | 4.204.680 | 5,1% | 163-232 (Floripa: 173-384) | Hélice contínua ø50-60, blocos e baldrames |
| 4 | Supraestrutura | 700 | 15.909.600 | 19,3% | 599-821 (cubetas range) | Cubetas, NPT=14 → boa diluição |
| 5 | Alvenaria | 195 | 4.431.960 | 5,4% | 146-264 (média 200) | 80% alvenaria / 20% drywall |
| 6 | Instalações | 355 | 8.068.440 | 9,8% | 310-431 (sem sprinkler) | Índice mais estável da base |
| 7 | Sistemas Especiais | 230 | 5.227.440 | 6,3% | 152-311 (médio-alto sem VRF) | 3 elevadores, churrasqueiras, AC pontos |
| 8 | Impermeabilização | 70 | 1.590.960 | 1,9% | 43-94 (média 65) | 1 subsolo eleva um pouco |
| 9 | Rev. Internos Piso/Parede | 135 | 3.068.280 | 3,7% | 107-222 (média 145) | Reboco + contrapiso padrão |
| 10 | Teto | 80 | 1.818.240 | 2,2% | 48-151 (média 85) | Forro gesso + negativo básico |
| 11 | Acabamentos Piso/Parede | 200 | 4.545.600 | 5,5% | 135-293 (média 215) | Porcelanato + azulejo padrão |
| 12 | Pintura Interna | 120 | 2.727.360 | 3,3% | 95-187 (média 125) | Acrílica + textura |
| 13 | Esquadrias | 400 | 9.091.200 | 11,0% | 244-457 (médio-alto range) | Alumínio padrão, sem pele de vidro |
| 14 | Cobertura | 10 | 227.280 | 0,3% | 3-67 | Cobertura simples |
| 15 | Fachada | 180 | 4.091.040 | 5,0% | 138-361 (média 210) | Textura + pintura, sem pedra/concreto aparente |
| 16 | Complementares | 250 | 5.682.000 | 6,9% | 133-325 (média 240 s/ outliers) | Mobiliário lazer, paisagismo, limpeza |
| | **Subtotal Direto** | **3.295** | **74.938.760** | **90,8%** | | |
| 17 | Imprevistos (3%) | 99 | 2.248.163 | 2,7% | 3% padrão | |
| 18 | Gerenciamento (CI) | 430 | 9.773.040 | 11,8% | 307-496 (faixa 10-20k m²) | Equipe, equipamentos, administrativo |
| | **SUBTOTAL SEM TAXA** | **3.824** | **86.959.963** | **105,4%** | | |
| | | | | | | |
| | **TOTAL ESTIMADO** | **~3.825** | **~R$ 87,0M** | **100%** | | |
| | **CUB ratio** | **1,27** | | | CUB/SC R$ 3.000 | |

## 4. ANÁLISE DE SENSIBILIDADE

| Cenário | R$/m² | Total (R$) | CUB ratio | Premissa alterada |
|---------|-------|-----------|-----------|-------------------|
| **Base (médio-alto)** | **3.825** | **R$ 87,0M** | **1,27** | Cenário principal |
| Médio (CKock-like) | 3.350 | R$ 76,2M | 1,12 | Acabamento simples, sem contenção pesada |
| Alto padrão | 4.150 | R$ 94,3M | 1,38 | Pele de vidro, louças premium, paisagismo elaborado |
| Sem subsolo | 3.640 | R$ 82,7M | 1,21 | Remove contenção + mov.terra + impermeab. extra |
| Protendida (em vez de cubetas) | 3.975 | R$ 90,3M | 1,33 | Supraestrutura +150 R$/m² |

## 5. COMPARATIVO COM PROJETOS SIMILARES DA BASE

| Projeto | AC m² | Cidade | Padrão | CUB ratio | R$/m² | Similaridade |
|---------|-------|--------|--------|-----------|-------|-------------|
| **Este (estimativa)** | **22.728** | **Floripa** | **Médio-Alto** | **1,27** | **3.825** | — |
| Cota 365 | 17.473 | Floripa | Alto | 1,18 | 3.367 | ⭐ Mesma cidade, porte similar |
| Neuhaus Origem | 14.516 | SC | Alto | 1,49 | 4.152 | Porte similar, mais pavimentos |
| D'Lohn Estreito | 13.148 | Floripa | Alto | 1,28 | 3.728 | ⭐ Mesma cidade |
| Connect | 13.144 | Itajaí | Alto | 1,29 | 3.584 | CUB ratio similar |
| Sisa Wave (resid) | 38.610 | SC/PR | Alto | — | 3.311 | Porte maior, escala dilui |

### Posicionamento:
- O *1,27 CUB* está na faixa inferior do Alto Padrão SC (1,28-1,39), coerente com "médio-alto"
- Comparado com Cota 365 (mesma cidade, 1,18 CUB): estamos ~8% acima — justificável pela contenção e subsolo
- Comparado com D'Lohn (mesma cidade, 1,28 CUB): estamos praticamente igual ✅

## 6. RESSALVAS

1. **Sem projeto arquitetônico** — todas as quantidades são estimadas pela tipologia
2. **Contenção é o item mais incerto** — pode variar de R$ 50 a R$ 250/m² dependendo do solo e vizinhança
3. **Alto Ribeirão é região mais periférica de Floripa** — pode ter terreno mais favorável (menos contenção)
4. **Número de UR afeta diretamente** esquadrias, instalações e acabamentos
5. **Padrão de acabamento** é a variável mais impactante — se for realmente "médio" (não médio-alto), o CUB cai para 1,10-1,15
6. **Outorga onerosa** (IA 1,58) gera custo adicional não incluído aqui — valor depende da legislação municipal vigente
