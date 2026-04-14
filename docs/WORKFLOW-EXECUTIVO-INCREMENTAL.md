# Workflow de Orçamento Executivo Incremental — Por Disciplina

> **Objetivo:** Construir orçamentos executivos de forma incremental, disciplina por disciplina, com validação paramétrica contínua.
> 
> **Projeto piloto:** Electra Towers (Thozen)
> **Criado:** 21/03/2026
> **Atualizado:** 13/04/2026 (adicionada consulta à camada qualitativa Gemma)

---

## ⭐ Base Enriquecida — Consulta a cada disciplina (v0.4)

A cada disciplina trabalhada no executivo, **antes de preencher**, consultar as fontes enriquecidas:

### 1. PUs cross-projeto (Fase 10)

Consulta direta dos PUs medianos da base de 4.210 clusters cross-projeto:

```python
import json
pus = json.load(open("base/itens-pus-agregados.json"))

# Buscar PU mediano de um insumo específico
for p in pus["pus_agregados"]:
    if "concreto usinado" in p["desc"].lower() and "30" in p["desc"]:
        print(f"{p['desc'][:60]}")
        print(f"  mediana: R$ {p['pu_mediana']}")
        print(f"  P10-P90: R$ {p['pu_p10']} - R$ {p['pu_p90']}")
        print(f"  CV: {p['cv']*100:.0f}%  ({p['n_observacoes']} observações)")
```

### 2. Índices derivados (Fase 13)

Usar os 29 novos índices para validar valores do macrogrupo:

```python
idx = json.load(open("base/indices-derivados-v2.json"))["indices"]

# Exemplo: validar total de Esquadrias
esq = idx["custo_esquadrias_rsm2"]
ac_projeto = 36000  # AC do projeto
esperado_mediano = esq["mediana"] * ac_projeto
esperado_p25 = esq["p25"] * ac_projeto
esperado_p75 = esq["p75"] * ac_projeto
print(f"Esquadrias esperado: R$ {esperado_mediano:,.0f} ")
print(f"  faixa P25-P75: R$ {esperado_p25:,.0f} - R$ {esperado_p75:,.0f}")
```

### 3. Sub-disciplinas dos similares (Fase 2/6)

```python
from pathlib import Path
BASE = Path.home() / "orcamentos-openclaw" / "base" / "indices-executivo"

def consultar_macrogrupo(macrogrupo, ac_alvo, n=5):
    todos = [json.loads(p.read_text(encoding="utf-8")) for p in BASE.glob("*.json")]
    sims = [p for p in todos
            if p.get("ac") and abs(p["ac"] - ac_alvo) < ac_alvo * 0.25
            and p.get("qualitative", {}).get("sub_disciplinas")]
    out = []
    for p in sims[:n]:
        for sd in p["qualitative"]["sub_disciplinas"]:
            if macrogrupo.lower() in sd.get("macrogrupo", "").lower():
                out.append((p["projeto"], sd))
    return out
```

### 4. Base master tudo-em-um (Fase 15)

```python
master = json.load(open("base/base-indices-master-2026-04-13.json"))
# Acessa TUDO: indices V2 + derivados + PUs + curvas ABC + cross-insights
```

**O que reaproveitar ao trabalhar cada disciplina:**
- **Sub-disciplinas** → como detalhar a aba do macrogrupo
- **PUs cross-projeto** → validar que PUs usados batem com P10-P90
- **Índices derivados** → total esperado do macrogrupo vs total no executivo
- **Observações de orçamentista** → reutilizar como texto de justificativa no log
- **Premissas técnicas** → premissas que costumam aparecer (perdas, prazos, fundação)
- **Padrões identificados** → o que se repete cross-aba
- **Análise de composição** (Fase 4) → distribuição material/MO/equipamento por item

**Script pronto pra revisão:**
```bash
python scripts/revisar_pacotes_pus.py  # compara PUs com faixa P10-P90
python scripts/gerar_audit_v2.py       # audit detalhado com 29 índices
```

**Documentação canônica:** `~/orcamentos-openclaw/base/CAMADA-QUALITATIVA-GEMMA.md`
**Cobertura atual:**
- 126 projetos com sub_disciplinas completas
- 58 com PDF analisado
- 22 com composições unitárias (Fase 4)
- 4.210 PUs cross-projeto (Fase 10)
- 29 índices derivados (Fase 13)

---

## 🎯 Visão Geral

### Problema
Orçamentos executivos completos exigem informações de **todas as disciplinas** simultaneamente. Isso cria:
- Gargalos de coordenação (esperar todos os projetistas)
- Retrabalho (mudanças em uma disciplina afetam outras)
- Incerteza prolongada (cliente não tem noção de custo até tudo estar pronto)

### Solução
**Orçamento incremental:**
1. Leo escolhe a **disciplina a orçar** (ex: "Esquadrias")
2. Jarvis/Cartesiano indica **o que é necessário** (quantitativos, especificações)
3. Leo preenche na planilha Excel (ou entrega fonte de dados)
4. Sistema **valida com índices paramétricos** (benchmark com 66 obras)
5. Leo tem **custo parcial validado** e pode avançar para próxima disciplina

**Benefícios:**
- **Progressivo:** Cliente vê custo evoluir em tempo real
- **Rastreável:** Cada disciplina tem fonte, data, responsável
- **Validado:** Comparação imediata com base histórica (58+ projetos)
- **Flexível:** Pode começar pelas disciplinas críticas (estrutura, instalações)

---

## 📋 Estrutura da Planilha Executiva

### Hierarquia de Custos
```
Unidade Construtiva (ex: Gerenciamento, Executivo)
  └─ Célula Construtiva (ex: Técnico, Administrativo)
      └─ Etapa (ex: Estudos, Projetos)
          └─ Subetapa (ex: Memorial descritivo, Sondagem)
              └─ Serviço (ex: Sondagem SPT, Levantamento topo)
                  └─ Composição (CPU) → Insumos
```

### Abas da Planilha

| Aba | Função | Quem Preenche |
|-----|--------|---------------|
| **CAPA** | Dados gerais (AC, UR, pavimentos) | Coordenação (início) |
| **EAP** | Estrutura de custos (hierarquia) | Sistema (template) |
| **EAP Análise** | Resumo R$/m² por macrogrupo | Sistema (fórmulas) |
| **CPU** | Composições de preços unitários | Orçamentista |
| **Insumos** | Catálogo de insumos (R$ unitário) | Orçamentista |
| **BASES** | Parâmetros de cálculo (CUB, índices) | Coordenação |
| **[Disciplina]** | Quantitativos por disciplina | Orçamentista (incremental) |

---

## 🔄 Fluxo de Interação — Passo a Passo

### Fase 1: Escolha da Disciplina
**Leo diz:** "Vamos orçar Esquadrias" (via Slack ou direto)

**Jarvis/Cartesiano responde:**
```
✅ Disciplina selecionada: ESQUADRIAS

📋 Checklist de informações necessárias:
1. Projeto arquitetônico (plantas de esquadrias) — revisar mais recente
2. Caderno de especificações (material, acabamento, padrão)
3. Quantidades por tipologia:
   - Portas (madeira, alumínio, corta-fogo)
   - Janelas (alumínio, vidro, sistema)
   - Vidros especiais (temperado, laminado, serigrafado)
   - Ferragens (fechaduras, dobradiças, puxadores)

📂 Onde preencher: aba "ESQUADRIAS" (planilha R00)

🎯 Índices de referência (benchmark):
   - SOHO 538: R$ 212,88/m² (alto padrão, 2021)
   - For Seasons: ~R$ 180-220/m² (alto padrão, 2024)
   - Eliat: ~R$ 200/m² (alto padrão, 2023)

⏱ Tempo estimado de preenchimento: 3-4h (dependendo da complexidade)
```

---

### Fase 2: Levantamento de Dados
**Leo (ou orçamentista) coleta:**
1. Projeto de esquadrias (DWGs, IFCs ou planilha do projetista)
2. Especificações técnicas (caderno, memorial descritivo)
3. Padrão de acabamento (linha de esquadrias, cor, vidros)

**Jarvis/Cartesiano pode ajudar:**
- Extrair quantidades de IFCs (via `ifcopenshell` ou análise manual de DWG)
- Consolidar dados de múltiplas fontes
- Criar resumo por tipologia de unidade

---

### Fase 3: Preenchimento na Planilha
**Leo abre:** `CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx` → aba **ESQUADRIAS**

**Estrutura da aba:**
| Aplicação | Descrição | Largura | Altura | Total m² | Total un | Térreo | Tipo | Cobertura |
|-----------|-----------|---------|--------|----------|----------|--------|------|-----------|
| Porta Madeira | P1 - 90×210cm | 0.9 | 2.1 | 15.12 | 8 | 2 | 6 | 0 |
| Janela Alumínio | J1 - Maxim-ar 100×120 | 1.0 | 1.2 | 288 | 240 | 0 | 240 | 0 |

**Dicas de preenchimento:**
- **Repetição de pavimentos:** Se Tipo se repete 24×, multiplicar quantidade
- **Unidades consistentes:** m² para área, un para peças
- **Descrição clara:** Código (P1, J1) + descrição completa

---

### Fase 4: Validação Paramétrica
**Jarvis/Cartesiano calcula:**
1. **Custo total da disciplina** (soma de todas as linhas)
2. **R$/m²** (custo total ÷ área construída)
3. **Comparação com índices de referência:**

```
📊 VALIDAÇÃO — ESQUADRIAS

Custo total: R$ 7.234.560,00
R$/m²: R$ 200,45

🔍 Benchmark (obras similares):
   SOHO 538 (2021):      R$ 212,88/m²  → Diferença: -5,8% ✅
   For Seasons (2024):   R$ 210,00/m²  → Diferença: -4,5% ✅
   Eliat (2023):         R$ 200,12/m²  → Diferença: +0,2% ✅

✅ STATUS: DENTRO DA FAIXA ESPERADA (alto padrão)

💡 Observações:
   - Valor alinhado com padrão alto (R$ 200-220/m²)
   - Esquadrias alumínio linha Suprema/equivalente
   - Vidros temperados/laminados confirmados
```

**Se valor estiver fora da faixa:**
```
⚠️ ATENÇÃO — VALOR ACIMA DO ESPERADO

Custo total: R$ 10.234.560,00
R$/m²: R$ 283,54

🔍 Benchmark (obras similares):
   SOHO 538 (2021):      R$ 212,88/m²  → Diferença: +33,2% ⚠️
   For Seasons (2024):   R$ 210,00/m²  → Diferença: +35,0% ⚠️

🔎 Possíveis causas:
   1. Esquadrias especiais (portas pivotantes, vidros curvos)
   2. Erro de quantidades (pavimentos multiplicados incorretamente)
   3. Preços unitários acima do mercado (revisar fornecedor)
   4. Padrão excepcional (acima do típico alto padrão)

📝 Ações sugeridas:
   - Revisar quantidades (checar multiplicação de pavimentos)
   - Validar preços unitários (comparar com 3 fornecedores)
   - Confirmar especificações (pode ser intencional se padrão premium)
```

---

### Fase 5: Consolidação no EAP
**Jarvis/Cartesiano atualiza:**
1. **Aba "EAP Análise"** → linha "Esquadrias" recebe o valor total
2. **R$/m² atualizado** na coluna de índice
3. **% sobre total** recalculado (quando mais disciplinas estiverem prontas)

**Leo visualiza:**
- Progresso do orçamento (quais disciplinas estão prontas)
- Distribuição de custos (qual disciplina pesa mais)
- Comparação com base histórica

---

## 🗂️ Disciplinas — Ordem Sugerida de Preenchimento

### Prioridade Alta (Impacto > R$ 400/m²)
**1. Estrutura — Supraestrutura** ⚠️ CRÍTICO
- **Por quê:** Representa ~25-30% do custo total
- **O que precisa:**
  - Projeto estrutural (plantas de fôrma, armação)
  - Volume de concreto por elemento (pilares, vigas, lajes)
  - Quantidade de aço (kg por elemento)
  - Tipo de laje (maciça, nervurada, cubetas)
  - fck do concreto (25, 30, 40 MPa)
- **Índices de referência:**
  - SOHO 538: R$ 499,91/m²
  - Estimativa Electra: R$ 450-550/m² (2 torres, 24 pavimentos tipo)
- **Aba:** `Resumo Estrutura` + detalhamento em outras abas
- **Tempo estimado:** 6-8h (depende do detalhamento do projeto)

**2. Instalações Elétricas** ⚠️ CRÍTICO
- **Por quê:** Representa ~8-12% do custo total
- **O que precisa:**
  - Projeto elétrico (plantas baixas, quadros)
  - Pontos por tipo de unidade (tomadas, iluminação, ar-cond)
  - Quadros elétricos (quantidade, capacidade)
  - Cabeamento (metragens por seção mm²)
  - Entrada de energia (padrão concessionária)
- **Índices de referência:**
  - Típico: R$ 120-180/m² (depende do padrão)
  - Estimativa Electra: R$ 140-160/m² (348 unidades)
- **Aba:** `Ger_Executivo` (seção Instalações Elétricas)
- **Tempo estimado:** 5-6h

**3. Esquadrias** 🔵 ALTO IMPACTO
- **Por quê:** Padrão alto, área grande de fachada
- **O que precisa:** (ver detalhamento acima)
- **Índices de referência:** R$ 200-220/m²
- **Aba:** `ESQUADRIAS`
- **Tempo estimado:** 3-4h

---

### Prioridade Média (Impacto R$ 100-200/m²)

**4. Instalações Hidrossanitárias**
- **O que precisa:**
  - Projeto hidrossanitário (água fria, quente, esgoto, pluvial)
  - Pontos por tipo de unidade
  - Tubulações (metragens por diâmetro DN20, DN25, DN32, etc)
  - Reservatórios (capacidade, tipo)
  - Bombas (vazão, potência)
  - Louças e metais (quantidade por tipologia) → separar em disciplina própria
- **Índices de referência:** R$ 100-150/m² (sem louças)
- **Aba:** `Ger_Executivo` (seção Hidrossanitárias)
- **Tempo estimado:** 4-5h

**5. Alvenaria**
- **O que precisa:**
  - Projeto arquitetônico (plantas de alvenaria)
  - Área de parede por espessura (9cm, 14cm, 19cm)
  - Tipo de bloco (concreto, cerâmico)
  - Área por pavimento (separar embasamento, tipo, cobertura)
- **Índices de referência:**
  - SOHO 538: R$ 82,28/m²
  - Estimativa Electra: R$ 70-90/m²
- **Aba:** `ARQUITETURA` (seção Alvenaria)
- **Tempo estimado:** 3-4h
- **⚠️ Status Electra:** Térreo e 1º Subsolo já preenchidos (continuar)

**6. Revestimentos Internos (Piso + Parede)**
- **O que precisa:**
  - Caderno de acabamentos (especificação por ambiente)
  - Área de piso por tipo (porcelanato, vinílico, deck)
  - Área de parede por tipo (azulejo, porcelanato, pintura)
  - Áreas por tipologia de unidade
- **Índices de referência:** R$ 120-180/m² (agregado piso + parede)
- **Aba:** `Ger_Executivo` (seções Revestimentos)
- **Tempo estimado:** 4-5h

**7. Pintura**
- **O que precisa:**
  - Caderno de acabamentos (tipo de tinta, nº demãos)
  - Área de parede interna (m²)
  - Área de teto (m²)
  - Área de fachada (se pintura sobre reboco)
- **Índices de referência:**
  - SOHO 538: R$ 77,96/m² (interna + externa)
  - Estimativa Electra: R$ 60-80/m²
- **Aba:** `Ger_Executivo` (Pintura Interna)
- **Tempo estimado:** 2-3h

---

### Prioridade Baixa (Impacto < R$ 100/m² ou Complementar)

**8. Louças e Metais**
- **O que precisa:**
  - Caderno de acabamentos (especificação por ambiente)
  - Quantidade por tipo de unidade:
    - Bacias sanitárias
    - Cubas (banheiro, cozinha, área de serviço)
    - Chuveiros, torneiras, registros
    - Acessórios (papeleira, saboneteira, cabideiro)
- **Índices de referência:**
  - SOHO 538: R$ 29,46/m²
  - Estimativa Electra: R$ 25-35/m² (348 unidades)
- **Aba:** `LOUÇAS E METAIS`
- **Tempo estimado:** 2-3h

**9. Climatização**
- **O que precisa:**
  - Projeto de ar-condicionado (se houver sistema central)
  - Equipamentos (splits, VRF, fan-coils)
  - Tubulações frigoríficas (metragens)
  - Linhas de dreno
  - Instalações elétricas dedicadas
- **Índices de referência:**
  - SOHO 538: R$ 31,87/m²
  - Estimativa Electra: R$ 40-60/m² (padrão alto, 2 torres)
- **Aba:** `Exaustão e Climatização`
- **Tempo estimado:** 4-5h
- **⚠️ Status Electra:** DWG pendente de conversão (ver PROJETO.md)

**10. Impermeabilização**
- **O que precisa:**
  - Projeto de impermeabilização (ou plantas com indicação)
  - Áreas por tipo:
    - Lajes de cobertura (manta, cristalizante)
    - Banheiros/WCs (argamassa polimérica)
    - Reservatórios (cristalizante)
    - Subsolos (manta asfáltica)
- **Índices de referência:**
  - SOHO 538: R$ 38,67/m²
  - Estimativa Electra: R$ 35-50/m²
- **Aba:** `Ger_Executivo` (Impermeabilização)
- **Tempo estimado:** 2-3h
- **⚠️ Status Electra:** #REF! na EAP Análise (corrigir fórmula)

**11. Fachada**
- **O que precisa:**
  - Projeto de fachada (elevações, detalhes)
  - Sistema (ACM, porcelanato, textura, pintura)
  - Áreas por tipo de revestimento
  - Elementos especiais (brises, cobogós, painéis)
  - Estrutura de fixação (perfis, suportes)
- **Índices de referência:**
  - SOHO 538: R$ 61,10/m²
  - Estimativa Electra: R$ 50-80/m² (dependendo do sistema)
- **Aba:** `Ger_Executivo` (Fachada)
- **Tempo estimado:** 3-4h

**12. Equipamentos Especiais**
- **O que precisa:**
  - Elevadores (quantidade, capacidade, velocidade, paradas)
  - Portão automático (garagem)
  - Ar-condicionado central (se houver)
  - Geradores (potência)
  - Sistema de automação (BMS)
  - Equipamentos de lazer (piscina, academia)
- **Índices de referência:**
  - SOHO 538: R$ 111,15/m²
  - Estimativa Electra: R$ 100-130/m² (2 torres, equipamentos de lazer)
- **Aba:** `Equipamentos Especiais`
- **Tempo estimado:** 2-3h

---

### Disciplinas de Infraestrutura (Preencher no Início)

**13. Fundação — Estacas**
- **Status:** ✅ JÁ PREENCHIDO (Electra)
- **O que tem:**
  - Torre 1: Ø50cm (17 un × 25m) + Ø60cm (406 un × 25m)
- **Validação:** Aguardar fundação rasa + contenção para validação completa

**14. Fundação Rasa + Contenção**
- **O que precisa:**
  - Projeto de fundação (plantas de fôrma, blocos)
  - Blocos (dimensões, quantidade de concreto/aço)
  - Vigas baldrames (metragens, seções)
  - Contenção (parede diafragma, cortina atirantada)
- **Índices de referência:**
  - SOHO 538: R$ 136,66/m² (infra completa)
  - Estimativa Electra: R$ 120-150/m²
- **Aba:** `Fund. Rasa | Contenção`
- **Tempo estimado:** 3-4h

**15. Movimentação de Terra**
- **O que precisa:**
  - Volume de escavação (m³)
  - Volume de aterro (m³)
  - Transporte de terra (distância)
  - Contenção provisória (se houver)
- **Índices de referência:**
  - SOHO 538: R$ 3,32/m²
  - Estimativa Electra: R$ 2-5/m²
- **Aba:** `Ger_Executivo` (Movimentação de Terra)
- **Tempo estimado:** 1-2h

---

## 📊 Checklist por Disciplina — Detalhado

### 1. ESTRUTURA — SUPRAESTRUTURA

**Informações obrigatórias:**
- [ ] Projeto estrutural completo (plantas de fôrma, armação)
- [ ] Revisão do projeto (ex: R01, R02)
- [ ] Sistema estrutural (concreto armado, protendido, pré-moldado)
- [ ] Tipo de laje (maciça, nervurada, cubetas, steel deck)

**Quantitativos por elemento:**

**Pilares:**
- [ ] Volume de concreto por pavimento (m³)
- [ ] Quantidade de aço por pavimento (kg)
- [ ] fck do concreto (25, 30, 40 MPa)
- [ ] Seções típicas (cm × cm)

**Vigas:**
- [ ] Volume de concreto por pavimento (m³)
- [ ] Quantidade de aço por pavimento (kg)
- [ ] fck do concreto
- [ ] Metragem linear (m)

**Lajes:**
- [ ] Volume de concreto por pavimento (m³)
- [ ] Quantidade de aço por pavimento (kg)
- [ ] Área de fôrma (m²)
- [ ] fck do concreto
- [ ] Espessura (cm)
- [ ] Tipo (maciça, nervurada, cubeta — especificar sistema)

**Escadas:**
- [ ] Volume de concreto (m³)
- [ ] Quantidade de aço (kg)
- [ ] Área de fôrma (m²)

**Reservatórios (se em concreto):**
- [ ] Volume de concreto (m³)
- [ ] Quantidade de aço (kg)
- [ ] Capacidade (m³ de água)

**Validação:**
- [ ] Volume total de concreto (m³) — conferir com somatório de pilares + vigas + lajes
- [ ] Consumo de aço (kg/m³ concreto) — típico 80-120 kg/m³ (residencial alto padrão)
- [ ] Consumo de fôrma (m²/m³ concreto) — típico 4-6 m²/m³
- [ ] R$/m² supraestrutura — comparar com índices (R$ 450-550/m²)

**Índices de referência:**
| Obra | Volume Concreto | Consumo Aço | R$/m² Supra |
|------|-----------------|-------------|-------------|
| SOHO 538 | N/D | N/D | R$ 499,91 |
| For Seasons | N/D | N/D | ~R$ 500-550 |
| Estimativa Electra | ~12.000 m³ | ~1.000 ton | R$ 450-550 |

**Onde preencher:**
- **Aba:** `Resumo Estrutura` (resumo por pavimento)
- **Detalhamento:** Outras abas estrutura (se houver)

---

### 2. INSTALAÇÕES ELÉTRICAS

**Informações obrigatórias:**
- [ ] Projeto elétrico completo (plantas baixas, unifilar, quadros)
- [ ] Revisão do projeto
- [ ] Padrão de entrada (concessionária, potência)
- [ ] Subestação (se houver) — transformador, cabine

**Quantitativos por tipo de unidade:**

**Pontos elétricos (apto tipo):**
- [ ] Tomadas 2P+T (un)
- [ ] Tomadas especiais (ar-cond, chuveiro) (un)
- [ ] Pontos de iluminação (un)
- [ ] Interruptores (un)

**Quadros elétricos:**
- [ ] Quadro de distribuição (QD) por unidade (un)
- [ ] Quadro geral (QG) por torre (un)
- [ ] Quadro de luz/força áreas comuns (un)

**Cabeamento (metragens totais):**
- [ ] Cabo 1,5 mm² (m)
- [ ] Cabo 2,5 mm² (m)
- [ ] Cabo 4,0 mm² (m)
- [ ] Cabo 6,0 mm² (m)
- [ ] Cabo 10,0 mm² (m)
- [ ] Cabos especiais (25mm², 35mm², 50mm²) (m)

**Eletrodutos:**
- [ ] Eletroduto Ø20mm (m)
- [ ] Eletroduto Ø25mm (m)
- [ ] Eletroduto Ø32mm (m)
- [ ] Eletrocalhas (m)

**Luminárias (áreas comuns):**
- [ ] LED embutida (un)
- [ ] LED sobrepor (un)
- [ ] Arandela (un)
- [ ] Balizador (un)

**Validação:**
- [ ] Pontos por unidade — conferir com projeto arquitetônico
- [ ] Carga instalada (kW) — conferir com dimensionamento
- [ ] R$/m² instalações elétricas — comparar com índices (R$ 120-180/m²)

**Índices de referência:**
- Típico residencial alto padrão: R$ 140-160/m²
- Estimativa Electra (348 un): R$ 5,0M - 5,8M (R$ 140-160/m²)

**Onde preencher:**
- **Aba:** `Ger_Executivo` (seção Instalações Elétricas)

---

### 3. ESQUADRIAS

**Informações obrigatórias:**
- [ ] Projeto arquitetônico (plantas de esquadrias, elevações)
- [ ] Caderno de especificações (linha, cor, acabamento)
- [ ] Padrão de vidros (temperado, laminado, espessuras)

**Quantitativos por tipo:**

**Portas Madeira:**
- [ ] P1 - 90×210cm (un) — porta principal apto
- [ ] P2 - 80×210cm (un) — portas internas
- [ ] P3 - 70×210cm (un) — banheiros
- [ ] Porta de correr (un)
- [ ] Especificação: madeira maciça, semi-oca, laqueada, natural

**Portas Alumínio:**
- [ ] Porta de enrolar (un) — garagem
- [ ] Porta de abrir (un) — áreas técnicas
- [ ] Linha: Suprema, padrão equivalente

**Janelas Alumínio:**
- [ ] J1 - Maxim-ar (un)
- [ ] J2 - Basculante (un)
- [ ] J3 - De correr (un)
- [ ] J4 - Fixa (un)
- [ ] Dimensões (cm × cm) por tipo
- [ ] Linha: Suprema, padrão equivalente
- [ ] Cor: branco, preto, fosco, etc

**Portas de Vidro:**
- [ ] Porta pivotante (un)
- [ ] Porta de correr (un)
- [ ] Espessura: 10mm, 12mm
- [ ] Tipo: temperado, laminado

**Vidros Especiais:**
- [ ] Guarda-corpo vidro (m²)
- [ ] Divisória vidro (m²)
- [ ] Espelho (m²)

**Ferragens:**
- [ ] Fechadura externa (un)
- [ ] Fechadura interna (un)
- [ ] Dobradiças (un)
- [ ] Puxadores (un)
- [ ] Trilhos (m) — portas de correr

**Corrimãos:**
- [ ] Corrimão madeira (m)
- [ ] Corrimão alumínio (m)
- [ ] Corrimão inox (m)

**Validação:**
- [ ] Quantidade de portas/janelas — conferir com nº de unidades × tipologia
- [ ] Área total de esquadrias (m²) — típico 12-18% da AC
- [ ] R$/m² esquadrias — comparar com índices (R$ 200-220/m² alto padrão)

**Índices de referência:**
| Obra | R$/m² Esquadrias | Obs |
|------|------------------|-----|
| SOHO 538 | R$ 212,88 | Alumínio Suprema, alto padrão |
| For Seasons | R$ 210 (est.) | Alumínio, alto padrão |
| Eliat | R$ 200 (est.) | Alumínio Suprema, alto padrão |

**Onde preencher:**
- **Aba:** `ESQUADRIAS`

---

### 4. INSTALAÇÕES HIDROSSANITÁRIAS

**Informações obrigatórias:**
- [ ] Projeto hidrossanitário completo (água fria, quente, esgoto, pluvial)
- [ ] Revisão do projeto
- [ ] Sistema de água quente (boiler individual, central, solar)
- [ ] Reservatórios (capacidade, localização)

**Quantitativos por tipo de unidade:**

**Pontos hidráulicos (apto tipo):**
- [ ] Pontos de água fria (un)
- [ ] Pontos de água quente (un)
- [ ] Pontos de esgoto (un)
- [ ] Caixas sifonadas (un)
- [ ] Ralos (un)

**Tubulações — Água Fria:**
- [ ] DN20 (3/4") (m)
- [ ] DN25 (1") (m)
- [ ] DN32 (1.1/4") (m)
- [ ] DN40 (1.1/2") (m)
- [ ] DN50 (2") (m)
- [ ] Material: PVC, PPR, cobre

**Tubulações — Esgoto:**
- [ ] DN40 (m)
- [ ] DN50 (m)
- [ ] DN75 (m)
- [ ] DN100 (m)
- [ ] DN150 (m)
- [ ] Material: PVC esgoto série normal/reforçada

**Tubulações — Água Pluvial:**
- [ ] DN75 (m)
- [ ] DN100 (m)
- [ ] DN150 (m)
- [ ] DN200 (m)

**Reservatórios:**
- [ ] Reservatório superior (capacidade m³, material)
- [ ] Reservatório inferior (capacidade m³, material)
- [ ] Cisterna (capacidade m³)

**Bombas:**
- [ ] Bomba de recalque (vazão m³/h, potência CV)
- [ ] Bomba de incêndio (vazão m³/h, potência CV)
- [ ] Bomba de esgoto/drenagem (un)

**Validação:**
- [ ] Pontos por unidade — conferir com projeto arquitetônico
- [ ] Capacidade de reservatório — NBR 5626 (150-200 L/pessoa/dia)
- [ ] R$/m² hidrossanitárias — comparar com índices (R$ 100-150/m² sem louças)

**Índices de referência:**
- Típico residencial alto padrão: R$ 120-140/m² (sem louças)
- Estimativa Electra: R$ 4,3M - 5,4M

**Onde preencher:**
- **Aba:** `Ger_Executivo` (seção Hidrossanitárias)

---

### 5. LOUÇAS E METAIS

**Informações obrigatórias:**
- [ ] Caderno de acabamentos (linha, marca, modelo)
- [ ] Padrão: econômico, médio, alto, premium

**Quantitativos por tipo de unidade:**

**Louças — Banheiro:**
- [ ] Bacia sanitária com caixa acoplada (un)
- [ ] Bacia sanitária PNE (un)
- [ ] Cuba de sobrepor (un)
- [ ] Cuba de embutir (un)
- [ ] Lavatório suspenso (un)
- [ ] Lavatório de coluna (un)
- [ ] Mictório (un) — se houver

**Louças — Cozinha/Área de Serviço:**
- [ ] Cuba inox (un)
- [ ] Cuba dupla inox (un)
- [ ] Tanque louça (un)
- [ ] Tanque granito sintético (un)

**Metais — Banheiro:**
- [ ] Torneira lavatório (un)
- [ ] Torneira banheira (un) — se houver
- [ ] Ducha higiênica (un)
- [ ] Registro de gaveta (un)
- [ ] Registro de pressão (un)
- [ ] Válvula de descarga (un)
- [ ] Chuveiro elétrico (un) — se houver
- [ ] Ducha (un)

**Metais — Cozinha/Área de Serviço:**
- [ ] Torneira cozinha (un)
- [ ] Torneira área de serviço (un)
- [ ] Torneira jardim (un)

**Acessórios:**
- [ ] Papeleira (un)
- [ ] Saboneteira (un)
- [ ] Toalheiro (un)
- [ ] Cabideiro (un)
- [ ] Porta-shampoo (un)
- [ ] Barra de apoio PNE (un)

**Validação:**
- [ ] Quantidade de bacias — conferir com nº banheiros × nº unidades
- [ ] Quantidade de cubas — conferir com nº banheiros + cozinhas
- [ ] R$/m² louças e metais — comparar com índices (R$ 25-35/m²)

**Índices de referência:**
| Obra | R$/m² Louças | Obs |
|------|--------------|-----|
| SOHO 538 | R$ 29,46 | Alto padrão |
| Estimativa Electra | R$ 25-35 | 348 unidades |

**Onde preencher:**
- **Aba:** `LOUÇAS E METAIS`

---

### 6. REVESTIMENTOS INTERNOS

**Informações obrigatórias:**
- [ ] Caderno de acabamentos completo (especificação por ambiente)
- [ ] Padrão de acabamento (econômico, médio, alto, premium)

**Quantitativos — Pisos:**

**Por tipo de revestimento:**
- [ ] Porcelanato 60×60 (m²)
- [ ] Porcelanato 90×90 (m²)
- [ ] Porcelanato 120×120 (m²)
- [ ] Vinílico (m²)
- [ ] Carpete (m²)
- [ ] Deck madeira (m²)
- [ ] Cerâmica (m²)
- [ ] Granito (m²)
- [ ] Piso intertravado (m²) — áreas externas

**Rodapés:**
- [ ] Rodapé porcelanato (m)
- [ ] Rodapé madeira (m)
- [ ] Rodapé PVC (m)

**Quantitativos — Paredes:**

**Por tipo de revestimento:**
- [ ] Azulejo 30×60 (m²)
- [ ] Porcelanato 60×120 (m²)
- [ ] Pastilha vidro (m²)
- [ ] Mármore (m²)
- [ ] Granito (m²)
- [ ] Reboco + pintura (m²) — ver disciplina Pintura
- [ ] Papel de parede (m²)
- [ ] Lambri madeira (m²)

**Validação:**
- [ ] Área de piso — conferir com AC (área construída)
- [ ] Área de parede — típico 2,5-3× AC (depende do pé-direito)
- [ ] R$/m² revestimentos — comparar com índices (R$ 120-180/m² agregado)

**Índices de referência:**
- Típico alto padrão: R$ 140-160/m² (piso + parede)
- Estimativa Electra: R$ 5,0M - 6,5M

**Onde preencher:**
- **Aba:** `Ger_Executivo` (seções Revestimentos Piso e Parede)

---

### 7. ALVENARIA

**Informações obrigatórias:**
- [ ] Projeto arquitetônico (plantas de alvenaria/vedação)
- [ ] Revisão do projeto
- [ ] Tipo de bloco (concreto, cerâmico)

**Quantitativos por espessura:**

**Blocos de Concreto:**
- [ ] Bloco 9cm (m²)
- [ ] Bloco 14cm (m²)
- [ ] Bloco 19cm (m²)

**Blocos Cerâmicos (se houver):**
- [ ] Bloco 9cm (m²)
- [ ] Bloco 14cm (m²)
- [ ] Bloco 19cm (m²)

**Outros:**
- [ ] Verga pré-moldada (m)
- [ ] Contra-verga pré-moldada (m)
- [ ] Cinta de amarração (m)

**Validação:**
- [ ] Área de alvenaria — típico 1,5-2× AC (depende da tipologia)
- [ ] R$/m² alvenaria — comparar com índices (R$ 70-90/m²)

**Índices de referência:**
| Obra | R$/m² Alvenaria | Obs |
|------|-----------------|-----|
| SOHO 538 | R$ 82,28 | Blocos concreto |
| Estimativa Electra | R$ 70-90 | Blocos concreto 9/14/19cm |

**Onde preencher:**
- **Aba:** `ARQUITETURA` (seção Alvenaria)
- **Status Electra:** Térreo e 1º Subsolo já preenchidos — continuar para pavimentos tipo

---

### 8. CLIMATIZAÇÃO

**Informações obrigatórias:**
- [ ] Projeto de ar-condicionado completo (se houver sistema central)
- [ ] Revisão do projeto
- [ ] Sistema: splits individuais, VRF, chiller, fan-coils

**Quantitativos — Sistema Individual (Splits):**

**Por tipo de unidade:**
- [ ] Split 9.000 BTU (un)
- [ ] Split 12.000 BTU (un)
- [ ] Split 18.000 BTU (un)
- [ ] Split 24.000 BTU (un)
- [ ] Split cassete (un)

**Infraestrutura:**
- [ ] Tubulação frigorífica 1/4" + 3/8" (m)
- [ ] Tubulação frigorífica 1/4" + 1/2" (m)
- [ ] Tubulação frigorífica 3/8" + 5/8" (m)
- [ ] Linha de dreno DN20 (m)
- [ ] Suportes condensadora (un)

**Quantitativos — Sistema Central (se houver):**

**Equipamentos:**
- [ ] Chiller (TR, tipo)
- [ ] Fan-coil (TR, un)
- [ ] Torre de resfriamento (TR)
- [ ] Bombas (vazão m³/h, potência CV)

**Tubulações:**
- [ ] Tubulação água gelada DN50 (m)
- [ ] Tubulação água gelada DN75 (m)
- [ ] Tubulação água gelada DN100 (m)
- [ ] Isolamento térmico (m²)

**Validação:**
- [ ] Capacidade total (BTU ou TR) — conferir com carga térmica
- [ ] R$/m² climatização — comparar com índices (R$ 40-60/m²)

**Índices de referência:**
| Obra | R$/m² Climatização | Obs |
|------|---------------------|-----|
| SOHO 538 | R$ 31,87 | Sistema misto |
| Estimativa Electra | R$ 40-60 | Padrão alto, 2 torres |

**Onde preencher:**
- **Aba:** `Exaustão e Climatização`
- **Status Electra:** DWG pendente de conversão (aguardando dados do projetista)

---

### 9. IMPERMEABILIZAÇÃO

**Informações obrigatórias:**
- [ ] Projeto de impermeabilização (ou plantas com indicação)
- [ ] Sistema por tipo de área (manta, cristalizante, argamassa)

**Quantitativos por tipo:**

**Lajes de Cobertura:**
- [ ] Manta asfáltica 3mm (m²)
- [ ] Manta asfáltica 4mm (m²)
- [ ] Impermeabilizante cristalizante (m²)

**Banheiros/WCs:**
- [ ] Argamassa polimérica (m²)
- [ ] Manta líquida (m²)

**Reservatórios:**
- [ ] Cristalizante (m²)
- [ ] Epóxi (m²)

**Subsolos:**
- [ ] Manta asfáltica 4mm (m²)
- [ ] Impermeabilizante cristalizante (m²)

**Piscinas:**
- [ ] Impermeabilizante específico (m²)
- [ ] Revestimento vítreo (m²)

**Validação:**
- [ ] Área total de impermeabilização — conferir com áreas molhadas
- [ ] R$/m² impermeabilização — comparar com índices (R$ 35-50/m²)

**Índices de referência:**
| Obra | R$/m² Impermeab. | Obs |
|------|------------------|-----|
| SOHO 538 | R$ 38,67 | Múltiplos sistemas |
| Estimativa Electra | R$ 35-50 | Alto padrão |

**Onde preencher:**
- **Aba:** `Ger_Executivo` (Impermeabilização)
- **Status Electra:** #REF! na EAP Análise — corrigir fórmula antes de preencher

---

### 10. FACHADA

**Informações obrigatórias:**
- [ ] Projeto de fachada completo (elevações, cortes, detalhes)
- [ ] Revisão do projeto
- [ ] Sistema: ACM, porcelanato, textura, pintura, vidro

**Quantitativos por tipo:**

**Revestimentos:**
- [ ] ACM (m²)
- [ ] Porcelanato 60×120 (m²)
- [ ] Porcelanato 90×180 (m²)
- [ ] Textura acrílica (m²)
- [ ] Pintura sobre reboco (m²)
- [ ] Pastilha vidro (m²)
- [ ] Pedra natural (m²)

**Elementos Especiais:**
- [ ] Brise alumínio (m²)
- [ ] Brise madeira (m²)
- [ ] Cobogó cerâmico (m²)
- [ ] Painéis decorativos (m²)

**Estrutura de Fixação:**
- [ ] Perfis alumínio (m)
- [ ] Suportes metálicos (un)
- [ ] Ancoragens químicas (un)

**Vidros:**
- [ ] Pele de vidro (m²)
- [ ] Guarda-corpo vidro (m)

**Validação:**
- [ ] Área total de fachada — conferir com perímetro × altura
- [ ] R$/m² fachada — comparar com índices (R$ 50-80/m²)

**Índices de referência:**
| Obra | R$/m² Fachada | Obs |
|------|---------------|-----|
| SOHO 538 | R$ 61,10 | ACM + porcelanato |
| Estimativa Electra | R$ 50-80 | Depende do sistema |

**Onde preencher:**
- **Aba:** `Ger_Executivo` (Fachada)

---

### 11. EQUIPAMENTOS ESPECIAIS

**Informações obrigatórias:**
- [ ] Memorial descritivo dos equipamentos
- [ ] Especificações técnicas (capacidade, potência, marca)

**Quantitativos:**

**Elevadores:**
- [ ] Elevador social (un)
  - Capacidade: 8, 10, 13 pessoas
  - Velocidade: 1,0 m/s, 1,5 m/s, 2,0 m/s
  - Paradas: quantidade de andares
  - Marca/linha: Atlas Schindler, Otis, Thyssenkrupp
- [ ] Elevador de serviço (un)

**Automação:**
- [ ] Portão automático garagem (un)
- [ ] Cancela automática (un)
- [ ] Controle de acesso (un)
- [ ] CFTV (câmeras, DVR)
- [ ] BMS (Building Management System) — se houver

**Gerador:**
- [ ] Gerador diesel (kVA)
- [ ] QTA (Quadro de Transferência Automática)
- [ ] Tanque de combustível (L)

**Equipamentos de Lazer:**
- [ ] Aquecedor piscina (un)
- [ ] Filtro piscina (un)
- [ ] Bomba piscina (un)
- [ ] Equipamentos academia (vb)
- [ ] Sauna (vb)
- [ ] Churrasqueira industrial (un)

**Aspiração Central (se houver):**
- [ ] Central de vácuo (un)
- [ ] Pontos de tomada (un)
- [ ] Tubulação (m)

**Validação:**
- [ ] Quantidade de elevadores — típico 1 para cada 20-30 unidades
- [ ] Capacidade gerador — típico 15-25% da carga instalada
- [ ] R$/m² equipamentos especiais — comparar com índices (R$ 100-130/m²)

**Índices de referência:**
| Obra | R$/m² Equip. Especiais | Obs |
|------|------------------------|-----|
| SOHO 538 | R$ 111,15 | 3 elevadores, automação |
| Estimativa Electra | R$ 100-130 | 2 torres, equipamentos de lazer |

**Onde preencher:**
- **Aba:** `Equipamentos Especiais`

---

## 🔁 Processo de Trabalho — Interação com @Cartesiano no Slack

### Para o Time da Cartesian

**Como replicar o workflow via Slack:**

#### 1. Iniciar Orçamento de Disciplina
**Orçamentista envia no `#custos-ia-paramétrico`:**
```
@Cartesiano quero orçar [DISCIPLINA] do [PROJETO]
Exemplo: @Cartesiano quero orçar Esquadrias do Electra Towers
```

**@Cartesiano responde:**
- ✅ Checklist de informações necessárias
- 📂 Aba da planilha onde preencher
- 🎯 Índices de referência (benchmark)
- ⏱ Tempo estimado

#### 2. Tirar Dúvidas
**Orçamentista pergunta:**
```
@Cartesiano onde encontro [INFORMAÇÃO]?
Exemplo: @Cartesiano onde encontro as metragens de tubulação elétrica?
```

**@Cartesiano responde:**
- Fonte típica (projeto elétrico, memorial, planilha projetista)
- Como extrair (manual, IFC, script)
- Alternativas se dado não disponível

#### 3. Validar Preenchimento
**Orçamentista envia planilha atualizada:**
```
@Cartesiano validar [DISCIPLINA] do [PROJETO]
[anexar planilha .xlsx ou indicar caminho]
```

**@Cartesiano:**
1. Lê a planilha
2. Calcula R$/m² da disciplina
3. Compara com índices de referência
4. Retorna validação:
   - ✅ Dentro da faixa esperada
   - ⚠️ Acima/abaixo — possíveis causas
   - 📝 Ações sugeridas

#### 4. Atualizar EAP Consolidado
**Após validação OK:**
```
@Cartesiano consolidar [DISCIPLINA] no EAP do [PROJETO]
```

**@Cartesiano:**
1. Atualiza aba "EAP Análise"
2. Recalcula percentuais
3. Mostra progresso do orçamento (% disciplinas preenchidas)

---

## 📈 Acompanhamento de Progresso

### Dashboard de Progresso (EAP Análise)

**Exemplo — Electra Towers (21/03/2026):**

| Disciplina | Status | R$/m² | % do Total | Benchmark |
|------------|--------|-------|-----------|-----------|
| Gerenciamento | ✅ | R$ 285,96 | 13,2% | ✅ Dentro |
| Mov. Terra | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |
| Infraestrutura | 🟡 | R$ 14,05 | 0,6% | ⚠️ Incompleto |
| Supraestrutura | 🟡 | R$ 4,22 | 0,2% | ⚠️ Incompleto |
| Alvenaria | 🟡 | R$ 0,00 | 0,0% | ⚠️ Parcial |
| Instalações Elétricas | ✅ | R$ 270,66 | 12,5% | ✅ Dentro |
| Louças e Metais | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |
| Climatização | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |
| Equipamentos Especiais | ✅ | R$ 109,43 | 5,1% | ✅ Dentro |
| Revestimentos | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |
| Impermeabilização | ❌ | #REF! | #REF! | ⚠️ Erro |
| Pintura | ✅ | R$ 0,60 | 0,0% | ⚠️ Baixo |
| Fachada | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |
| Esquadrias | ⏸️ | R$ 0,00 | 0,0% | ⚠️ Falta |

**Progresso:** 30% preenchido (6 de 18 disciplinas)
**Total orçado:** R$ 24.695.327,70
**R$/m² Total:** R$ 684,48 (⚠️ incompleto)

**Próximas disciplinas prioritárias:**
1. 🔴 Estrutura (Supraestrutura completa) — alto impacto
2. 🔴 Alvenaria — estrutura já iniciada
3. 🟡 Esquadrias — alto padrão, impacto significativo
4. 🟡 Louças e Metais — 348 unidades
5. 🟡 Revestimentos — área grande

---

## 🎓 Boas Práticas

### 1. Ordem de Preenchimento
**Recomendado:**
- Iniciar pelas disciplinas de **maior impacto** (estrutura, instalações)
- Deixar acabamentos para o final (dependem de definições de padrão)
- Preencher fundação antes de estrutura (para validar carga)

### 2. Fontes de Dados
**Prioridade:**
1. Projeto executivo (DWG, IFC, PDF)
2. Planilha de quantitativos do projetista
3. Memorial descritivo
4. Orçamento preliminar (validar com executivo)
5. Estimativa paramétrica (última opção)

### 3. Validação Cruzada
**Sempre conferir:**
- Quantidades de alvenaria × área de revestimento
- Pontos elétricos × pontos hidráulicos (coerência por ambiente)
- Esquadrias × vãos em planta arquitetônica
- Louças × nº de banheiros × nº de unidades

### 4. Documentação
**Para cada disciplina, registrar:**
- Fonte de dados (projeto rev. X, planilha projetista, etc)
- Data de preenchimento
- Responsável
- Premissas adotadas (se houver estimativa)
- Pendências (dados faltantes, validações necessárias)

### 5. Revisão
**Ao concluir disciplina:**
- Validar com índices paramétricos
- Revisar com outro orçamentista (4 olhos)
- Aprovar com coordenação antes de consolidar no EAP

---

## 🛠️ Ferramentas de Apoio

### Extração de Quantitativos
- **IFC:** `ifcopenshell` (Python) — extração automatizada
- **DWG:** Conversão para DXF → extração manual ou script
- **PDF:** Extração manual com conferência

### Validação Paramétrica
- **Base de índices:** `~/orcamentos/parametrico-backup-20260311/indices/` (66 obras)
- **Script de comparação:** (a desenvolver — @Cartesiano pode fazer)

### Comunicação
- **Slack:** `#custos-ia-paramétrico` — interação com @Cartesiano
- **Planilha:** Excel (compartilhada via OneDrive/Dropbox/pasta local)

---

## 📝 Exemplos de Interação

### Exemplo 1: Iniciar Disciplina
```
Orçamentista: @Cartesiano quero orçar Alvenaria do Electra Towers

@Cartesiano:
✅ Disciplina selecionada: ALVENARIA

📋 Checklist de informações necessárias:
1. Projeto arquitetônico (plantas de alvenaria/vedação)
2. Área de parede por espessura (9cm, 14cm, 19cm)
3. Tipo de bloco (concreto, cerâmico)
4. Vergas, contra-vergas, cintas de amarração

📂 Onde preencher: aba "ARQUITETURA" (seção Alvenaria)

🎯 Índices de referência (benchmark):
   - SOHO 538: R$ 82,28/m² (blocos concreto, alto padrão)
   - Estimativa Electra: R$ 70-90/m² (36.088 m² AC)

⏱ Tempo estimado de preenchimento: 3-4h

⚠️ Status atual: Térreo e 1º Subsolo já preenchidos
   → Continuar para pavimentos tipo (24 repetições)
```

---

### Exemplo 2: Validação de Disciplina
```
Orçamentista: @Cartesiano validar Alvenaria do Electra Towers
[anexa planilha atualizada]

@Cartesiano:
📊 VALIDAÇÃO — ALVENARIA

Custo total: R$ 2.854.320,00
R$/m²: R$ 79,09

🔍 Benchmark (obras similares):
   SOHO 538 (2021):      R$ 82,28/m²  → Diferença: -3,9% ✅
   Estimativa prevista:  R$ 70-90/m²  → Dentro da faixa ✅

✅ STATUS: VALIDADO

📋 Resumo quantitativo:
   - Bloco 9cm:  2.340 m² (6,5% do total)
   - Bloco 14cm: 24.680 m² (68,4% do total)
   - Bloco 19cm: 9.060 m² (25,1% do total)
   - Total: 36.080 m² (1,00× AC — típico para residencial vertical)

💡 Observações:
   - Distribuição de espessuras coerente (14cm predominante)
   - Consumo de vergas/contra-vergas dentro do esperado
   - Pronto para consolidar no EAP

Deseja consolidar no EAP? (responda "sim" para continuar)
```

---

### Exemplo 3: Consulta de Referência
```
Orçamentista: @Cartesiano qual o R$/m² típico de Louças e Metais em alto padrão?

@Cartesiano:
🎯 ÍNDICES DE REFERÊNCIA — LOUÇAS E METAIS (Alto Padrão)

📊 Base de dados (66 obras):
   - SOHO 538 (2021): R$ 29,46/m²
   - For Seasons (2024): ~R$ 32,00/m² (estimado)
   - Eliat (2023): ~R$ 28,50/m² (estimado)

   **Faixa típica:** R$ 25-35/m² (alto padrão)

💡 Fatores que influenciam:
   - Linha de louças (Deca, Incepa, Celite premium)
   - Metais (cromados standard vs. monocomando premium)
   - Quantidade de banheiros por unidade
   - Áreas comuns (vestiários, lavabos)

📝 Para 36.088 m² AC (Electra):
   - Estimativa: R$ 902k - 1,26M
   - R$/unidade: R$ 2.600 - 3.600 (para 348 unidades)
```

---

## 🚀 Próximos Passos — Implementação

### Fase 1: Estruturação (Concluída)
- [x] Criar workflow incremental (este documento)
- [x] Revisar planilha R00 do Electra
- [x] Identificar índices de referência

### Fase 2: Piloto (Próxima)
- [ ] Escolher 3 disciplinas para testar workflow:
  1. Alvenaria (já iniciada)
  2. Esquadrias (impacto alto)
  3. Louças e Metais (simples, rápida)
- [ ] Preencher disciplinas seguindo checklist
- [ ] Validar com @Cartesiano
- [ ] Consolidar no EAP
- [ ] Documentar lições aprendidas

### Fase 3: Expansão
- [ ] Replicar para todas as disciplinas do Electra
- [ ] Treinar time da Cartesian no workflow
- [ ] Criar templates de checklist por disciplina
- [ ] Automatizar validação paramétrica (script)

### Fase 4: Escala
- [ ] Aplicar workflow em novos projetos
- [ ] Medir ganhos de eficiência (tempo, precisão)
- [ ] Refinar processo com feedback do time
- [ ] Criar biblioteca de índices (atualização contínua)

---

## 📚 Referências

### Documentos Relacionados
- `REVISAO-ELECTRA-R00.md` — Análise completa da planilha executiva R00
- `~/orcamentos/executivo/thozen-electra/PROJETO.md` — Informações do projeto Electra
- `~/orcamentos/parametrico-backup-20260311/indices/` — Base de índices (66 obras)
- `~/orcamentos/docs/ORCAMENTO-PARAMETRICO-WORKFLOW.md` — Workflow paramétrico (complementar)

### Planilhas
- `~/orcamentos/executivo/thozen-electra/CTN-TZN_ELT_Orcamento_Executivo_R00.xlsx`

### Índices de Referência (Top 5)
1. `soho-538-indices.md` — SOHO 538 Art Residences (13.632 m², alto padrão, 2021)
2. `byseasons-forseasons-indices.md` — For Seasons (6.348 m², fundação igual Electra, 2024)
3. `eze-eilat-indices.md` — Edifício Eliat (1.767 m², alto padrão, 2023)
4. `amalfi-marine-indices.md` — Amalfi Marine (litoral SC, alto padrão)
5. `arv-ingleses-spot-indices.md` — ARV Ingleses Spot (grande porte, vertical)

---

*Última atualização: 2026-03-21*
*Versão: 1.0*
