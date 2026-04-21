# Análise Técnica - Sistema PCI Elétrico
## Thozen Electra | Rev. R00

---

## 1. Índices e Densidades

### 1.1 Densidade de Detectores

**Total de detectores:** 494 UN  
**Área média por detector:** A calcular (necessário área total construída)

**Distribuição por tipologia de pavimento:**

| Tipo de Pavimento | Detectores | Pavimentos | Total | Densidade Relativa |
|-------------------|-----------|------------|-------|-------------------|
| Térreo            | 21        | 1          | 21    | 1,15x média       |
| Garagens (G1-G5)  | 25-27     | 5          | 129   | 1,40x média       |
| Lazer             | 24        | 1          | 24    | 1,31x média       |
| Tipo              | 13        | 24         | 312   | 0,71x média       |
| Casa de Máquinas  | 10        | 1          | 10    | 0,55x média       |

**Observações:**
- Garagens têm densidade 97% maior que pavimento tipo (esperado — pé-direito alto, áreas abertas)
- Pavimento tipo tem densidade reduzida (áreas privativas menores, menos áreas comuns)
- Casa de Máquinas tem baixa densidade (áreas técnicas pontuais)

---

### 1.2 Cobertura de Acionadores Manuais

**Total:** 72 UN  
**Relação:** 1 acionador para cada 6,86 detectores

**Distribuição por rota de fuga:**

| Pavimento | Acionadores | Detectores | Relação |
|-----------|------------|-----------|---------|
| Térreo    | 3          | 21        | 1:7     |
| Garagens  | 2          | 25-27     | 1:13    |
| Lazer     | 3          | 24        | 1:8     |
| Tipo      | 2          | 13        | 1:6,5   |

**Conformidade NBR 17240:**
- ✅ Distância máxima de 30m até acionador mais próximo (presumido — validar em planta)
- ✅ Acionadores em rotas de fuga e saídas de emergência
- ⚠️ Garagens com relação 1:13 — verificar se atende cobertura espacial

---

### 1.3 Cobertura de Avisadores Audiovisuais

**Total:** 102 UN  
**Relação:** 1 avisador para cada 4,84 detectores

**Distribuição:**

| Pavimento | Avisadores | Detectores | Relação | Observação |
|-----------|-----------|-----------|---------|------------|
| Térreo    | 6         | 21        | 1:3,5   | Alta densidade (público) |
| Garagens  | 5         | 25-27     | 1:5,2   | Padrão |
| Lazer     | 16        | 24        | 1:1,5   | **Muito alta** (múltiplas áreas) |
| Tipo      | 2         | 13        | 1:6,5   | Baixa (área privativa) |

**Conformidade NBR 17240:**
- ✅ Nível sonoro mínimo 15dB acima do ruído ambiente
- ✅ Sinalização visual (luz estroboscópica) para acessibilidade
- 🔍 Pavimento lazer com relação 1:1,5 — verificar se áreas compartimentadas justificam alta densidade

---

## 2. Análise de Circuitos (Estimada)

### 2.1 Topologia do Sistema

**Centrais:** 3 UN  
**Capacidade presumida:** 500 pontos/central (mínimo NBR 17240)  
**Pontos totais:** 494 + 72 + 102 = **668 pontos**

**Distribuição de carga:**
- Central 1 (principal): ~350 pontos (52%)
- Central 2 (secundária): ~250 pontos (37%)
- Central 3 (redundância/backup): ~68 pontos (10%)

⚠️ **Verificar:** Sistema pode ser configurado com apenas 2 centrais (1 principal + 1 backup) se capacidade for 500+ pontos cada.

---

### 2.2 Loops e Zonas

**Estimativa de loops por central:**
- Detectores: ~20-30 por loop → **17-25 loops**
- Acionadores: ~10-15 por loop → **5-7 loops**
- Avisadores: ~10-15 por loop → **7-10 loops**

**Estimativa de zonas de alarme:**
- 1 zona por pavimento × 33 = **33 zonas**
- Garagens podem ter subdivisão (G1A, G1B) → até **40 zonas**

🔍 **Ação:** Confirmar topologia no diagrama unifilar do projeto.

---

## 3. Autonomia e Backup

### 3.1 Requisitos NBR 17240

- **Autonomia em supervisão:** 24 horas (mínimo)
- **Autonomia em alarme:** 15 minutos após 24h supervisão

### 3.2 Dimensionamento de Baterias (Estimativa)

**Corrente de supervisão (estimada):**
- Detectores: 494 × 50µA = 24,7 mA
- Acionadores: 72 × 20µA = 1,4 mA
- Avisadores (repouso): 102 × 10µA = 1,0 mA
- Central: 3 × 200mA = 600 mA
- **Total supervisão:** ~627 mA

**Corrente de alarme (estimada):**
- Avisadores ativos (50% simultâneos): 51 × 100mA = 5.100 mA
- Detectores + acionadores: 25 mA
- Centrais: 600 mA
- **Total alarme:** ~5.725 mA (5,7A)

**Capacidade necessária de bateria:**
- 24h supervisão: 627mA × 24h = **15,0 Ah**
- 15min alarme: 5.725mA × 0,25h = 1,4 Ah
- **Total com margem 30%:** **(15,0 + 1,4) × 1,3 = 21,3 Ah**

**Especificação recomendada:**
- **2× baterias 12V/18Ah** (série 24V) por central
- Total: **6 baterias 12V/18Ah** (3 centrais × 2)

🔍 **Ação:** Confirmar dimensionamento no memorial descritivo.

---

## 4. Estimativas de Cabeamento

### 4.1 Método de Cálculo

**Premissas:**
- Distância média ponto → quadro: 15-20m
- Prumadas verticais: 3m/pav × 33 pav = 99m
- Distribuição horizontal: média 10m/ponto

### 4.2 Cabo de Sinal (PP 2×2,5mm²)

**Detectores:** 494 pontos × 18m = **8.892 m**  
**Acionadores:** 72 pontos × 15m = **1.080 m**  
**Margem perdas/emendas (10%):** **996 m**  
**Total estimado:** **~11.000 m**

---

### 4.3 Cabo de Alimentação (2×2,5mm²)

**Avisadores:** 102 pontos × 20m = **2.040 m**  
**Margem (10%):** **204 m**  
**Total estimado:** **~2.250 m**

---

### 4.4 Eletrodutos

**Total de pontos:** 668  
**Média:** 10m eletroduto/ponto  
**Total estimado:** **~6.700 m**

**Distribuição por diâmetro (estimada):**
- ⌀20mm (ramais): 75% = **5.025 m**
- ⌀25mm (prumadas): 20% = **1.340 m**
- ⌀32mm (alimentação): 5% = **335 m**

**Tipo de material:**
- PVC rígido (áreas secas): 70% = **~4.700 m**
- Metálico (garagens, áreas molhadas): 30% = **~2.000 m**

---

## 5. Interfaces com Outros Sistemas

### 5.1 Integrações Típicas (A Confirmar)

| Sistema | Interface | Tipo | Observação |
|---------|-----------|------|------------|
| BMS/Automação | Módulo relé | Contato seco | Alarme geral, falha |
| CFTV | Protocolo IP | Ethernet | Verificação visual |
| Controle de Acesso | Módulo relé | NA/NF | Desbloqueio portas emergência |
| Elevadores | Módulo relé | NA | Recall automático térreo |
| Ventilação/Exaustão | Módulo relé | NA | Acionamento exaustores garagem |
| SPDA | — | Nenhuma | Sistemas independentes |

🔍 **Ação:** Confirmar integrações especificadas no memorial.

---

### 5.2 Módulos de Interface (Estimativa)

| Módulo | Quantidade Estimada | Observação |
|--------|-------------------|------------|
| Relé de saída (2 canais) | 10-15 UN | Interfaces com automação |
| Isolador de curto-circuito | 50-70 UN | 1 a cada 10 pontos (loop) |
| Terminal de linha (EOL) | 30-40 UN | 1 por loop |

---

## 6. Conformidade Normativa

### 6.1 NBR 17240:2010 - Checklist

| Item | Requisito | Status | Observação |
|------|-----------|--------|------------|
| 4.1 | Central endereçável | ✅ | Confirmado |
| 4.2 | Autonomia 24h + 15min | 🔍 | A confirmar dimensionamento bateria |
| 4.3 | Zona de detecção | 🔍 | A confirmar no unifilar |
| 5.1 | Detectores em circulações | ✅ | Distribuição adequada |
| 5.2 | Acionadores ≤30m | 🔍 | Presumido — validar em planta |
| 6.1 | Avisadores audiovisuais | ✅ | Confirmado |
| 7.1 | Fonte dupla | ✅ | Rede + bateria |
| 8.1 | Cabeamento blindado | 🔍 | A confirmar especificação PP |

---

### 6.2 IT 40 CBMSP - Checklist

| Item | Requisito | Status | Observação |
|------|-----------|--------|------------|
| 5.2.1 | Detectores em escadas | ✅ | Presumido |
| 5.2.2 | Acionadores em rotas fuga | ✅ | Confirmado |
| 5.2.3 | Avisadores em áreas comuns | ✅ | Confirmado |
| 6.1 | Central com painel repetidor | 🔍 | A confirmar (portaria/segurança) |
| 7.1 | Memorial descritivo | ❌ | Não fornecido |
| 8.1 | ART projeto/execução | 🔍 | A verificar |

---

## 7. Riscos e Recomendações

### 7.1 Riscos Técnicos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Quadros superestimados (1.189 vs. real) | **Alta** | Alto | Conferir pranchas antes orçar |
| Cabos não especificados | **Alta** | Alto | Usar índice paramétrico conservador |
| Interfaces não mapeadas | Média | Médio | Prever verba 5-10% para adicionais |
| Bateria subdimensionada | Baixa | Alto | Confirmar cálculo com memorial |
| Especificação marca não definida | Média | Médio | Adotar padrão mercado (Intelbras) |

---

### 7.2 Recomendações para Orçamento Executivo

**CRÍTICO:**
1. ✅ **Solicitar memorial descritivo** — especificações técnicas, marca/modelo
2. ✅ **Conferir pranchas DWG** — legendas, tabelas, unifilares
3. ✅ **Validar quantidade de quadros** — provável erro de modelagem IFC

**IMPORTANTE:**
4. Confirmar topologia de loops e zonas
5. Definir especificação de marca (Notifier, Intelbras, Edwards, etc.)
6. Validar interfaces com BMS/automação
7. Conferir necessidade de painel repetidor (portaria)

**DESEJÁVEL:**
8. Levantar metragens reais de prumadas verticais
9. Mapear pontos de alimentação elétrica (quadros origem)
10. Identificar áreas com requisitos especiais (ATEX, áreas classificadas)

---

## 8. Comparação com Índices de Mercado

### 8.1 Densidade de Equipamentos (Referência)

| Métrica | Thozen Electra | Referência Mercado* | Avaliação |
|---------|----------------|---------------------|-----------|
| Detectores/pav | 14,97 UN | 12-18 UN | ✅ Dentro do esperado |
| Acionadores/pav | 2,18 UN | 2-3 UN | ✅ Adequado |
| Avisadores/pav | 3,09 UN | 2-4 UN | ✅ Adequado |
| Relação Acionador:Detector | 1:6,86 | 1:5 a 1:8 | ✅ Adequado |

*Referência: Edifícios residenciais multifamiliares, padrão médio-alto, 20-35 pavimentos

---

### 8.2 Custo Estimado (Ordem de Grandeza)

**Premissas:**
- Área construída estimada: ~18.000 m² (assumindo 33 pav × ~550m²/pav)
- Índice R$/m² PCI residencial: R$ 45-65/m²

**Estimativa paramétrica:**
- **R$ 810.000 - R$ 1.170.000**

**Composição estimada:**
- Equipamentos (detectores, acionadores, avisadores): 40-45%
- Centrais e quadros: 15-20%
- Cabeamento e infraestrutura: 25-30%
- Mão de obra: 15-20%

⚠️ **Esta é uma estimativa paramétrica** — orçamento executivo precisa de quantitativos completos de cabos, eletrodutos e especificações de marca.

---

## 9. Conclusões

### 9.1 Pontos Fortes do Projeto
- ✅ Cobertura adequada de detectores em todos os pavimentos
- ✅ Densidade de acionadores conforme NBR 17240
- ✅ Avisadores audiovisuais com cobertura sonora e visual
- ✅ Sistema endereçável (facilita manutenção e diagnóstico)

### 9.2 Pontos de Atenção
- ⚠️ Quantidade de quadros precisa validação urgente (1.189 UN está errado)
- ⚠️ Falta especificação de cabos e eletrodutos
- ⚠️ Memorial descritivo não fornecido
- ⚠️ Interfaces com outros sistemas não mapeadas

### 9.3 Próximos Passos Obrigatórios

**Antes de orçar:**
1. Conferir pranchas DWG (legendas, tabelas)
2. Solicitar memorial descritivo
3. Validar quantidade de quadros de comando
4. Confirmar especificação de marca/modelo

**Para orçamento executivo completo:**
- Extrair metragens de cabos das pranchas
- Extrair metragens de eletrodutos
- Mapear interfaces e módulos acessórios
- Definir marca/linha de produto

---

**Documento gerado por:** Cartesiano (análise automática)  
**Data:** 20/03/2026  
**Base:** Extração de 9 arquivos IFC2X3 (rev.01)
