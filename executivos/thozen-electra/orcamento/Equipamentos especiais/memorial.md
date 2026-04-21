# Memorial — Equipamentos Especiais (Complementares)

> Regras de extração dos quantitativos da aba **Equipamentos Especiais** + origem de cada número.
> Serve de referência pra Claude seguir o mesmo padrão em próximas obras.

## Escopo

Esta aba cobre **equipamentos eletromecânicos complementares** de obra vertical — tudo que não é estrutura, instalação hidro/elétrica bruta ou acabamento:

- **Elevadores** (sociais, serviço/carga, casa de máquinas)
- **Grupo gerador** de emergência + infra (tanque, QTA, base, escapamento)
- **Bombas** (recalque + pressurização + booster)
- **PCI hidromecânico** (bombas de incêndio, RTI, jockey)
- **SPDA / Para-raios**
- **Exaustão** (churrasqueiras, cozinhas comuns)
- **Climatização / Ar-condicionado** (VRF condensadoras + evaporadoras + tubulação frigorífica)
- **Ventilação mecânica** (escadas pressurizadas NBR 14880)
- **Interfone / vídeo porteiro**
- **CFTV / câmeras de segurança**
- **Iluminação de emergência** (NBR 10898)
- **Automação predial (BMS/SCADA)**

**Não cobre** (vai em outras disciplinas):
- Tubulação hidráulica primária (vai em "Hidrossanitário")
- Sistemas fixos de combate sprinkler (vai em "Sprinklers")
- Fiação geral de força/iluminação da obra (vai em "Elétrico")
- Iluminação de ambientes (vai em "Iluminação")
- Automação de portão/cancela (vai em "Automação")
- Detecção de fumaça/alarme (vai em "PPCI")

**Natureza do conteúdo:** esta aba é um **catálogo de itens complementares com estimativas de custo**, não um quantitativo extraído de projeto. É uma **lista paramétrica** que consolida:
- Equipamentos com cotação de mercado (elevadores, grupo gerador)
- Estimativas por briefing R00 (bombas, PCI hidro, ventilação)
- Premissas baseadas em normas (SPDA, emergência, ventilação)
- Itens aguardando processamento de projeto (ar-condicionado VRF)

⚠ **Zero fórmulas** nessa aba — tudo é valor direto (qtd × custo unitário digitados manualmente).

---

## Fontes de dados

| Fonte | Origem | Aplicação |
|---|---|---|
| **Cotação de mercado** | Fornecedores/fabricantes | Elevadores, grupo gerador, VRF, centrais |
| **NBR 5419** (SPDA) | Norma técnica | Quantitativo de cabos, captores, hastes |
| **NBR 10898** (Emergência) | Norma técnica | Luminárias de emergência, blocos autônomos |
| **NBR 14880:2024** (Pressurização) | Norma técnica | Ventiladores centrífugos, dampers |
| **NBR 13714** (PCI) | Norma técnica | Bombas PCI, RTI |
| **Briefing R00** | Premissas da Cartesian | Qtd de câmeras, monitores, sensores BMS |
| **IFCs do projeto Electra** | `~/orcamentos/projetos/thozen-electra/` | Validação de quantitativos (quando disponível) |
| **Memorial descritivo** | Projeto arquitetônico | Especificação de sistemas (ex.: VRF vs split) |

**Referência do empreendimento (cabeçalho linhas 2-4):**
- B2:C2 = "Projeto" → "Thozen Electra Towers"
- B3:C3 = "Empresa" → "Cartesian Engenharia"
- B4:C4 = "Revisão" → "R00 — Itens Complementares"

---

## Estrutura da aba

Cabeçalho de colunas (linha 5):

| Col | Cabeçalho |
|---|---|
| A | Descrição |
| B | Unidade |
| C | Quantidade |
| D | Custo unitário |
| E | Custo Total (= C × D, digitado manualmente) |
| F | Observações |

Cada **grupo** (ELEVADORES, GRUPO GERADOR, BOMBAS, …) começa com uma linha-título só preenchendo A e E (subtotal do grupo). Em seguida vêm os itens detalhados. No final (linha 108), **TOTAL GERAL**.

---

## Grupos — regras de extração

### Grupo 1 — ELEVADORES (linhas 6-10, subtotal E6 = R$ 2.700.000)

Equipamento mais caro da aba. Valores de cotação de mercado (não licitação formal).

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A7 | Elevador social com casa de máquinas — 8 paradas (tipo a 31°) | un | 4 | 320.000 | 1.280.000 | Cotação fabricante — 8 passageiros, 2,0 m/s |
| A8 | Elevador social sem casa de máquinas — 8 paradas | un | 2 | 280.000 | 560.000 | Cotação — 6 passageiros, 1,75 m/s |
| A9 | Elevador de serviço/carga — 34 paradas | un | 2 | 350.000 | 700.000 | Cotação — 1000 kg, 1,5 m/s |
| A10 | Mão de obra de instalação | vb | 1 | 180.000 | 180.000 | Estimativa instalação + comissionamento |

**Critério de quantidade:** 4+2 = 6 elevadores sociais + 2 de serviço = 8 total. Casa com a premissa da Cartesian de 2 torres × (3 sociais + 1 serviço).

**Cruzamento com EPCs:**
- EPCs!D33 diz "Quantidade de elevadores de carro = 2" ✓
- EPCs!D38 diz "Quantidade de elevadores sociais = 3" — mas aqui temos 6 sociais (4 c/casa + 2 s/casa). ⚠ **divergência** entre abas — conferir se EPCs conta só "pavimentos com elevador" e considera 1 por torre, ou se há inconsistência.

---

### Grupo 2 — GRUPO GERADOR DE EMERGÊNCIA (linhas 11-17, subtotal E11 = R$ 428.000)

Sistema de backup elétrico conforme NBR 14039 (aplicações prediais).

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A12 | Grupo gerador diesel 500 kVA | un | 1 | 280.000 | 280.000 | Dimensionamento R00 pra cargas essenciais (elevadores, PCI, emergência) |
| A13 | QTA (Quadro de Transferência Automática) | un | 1 | 45.000 | 45.000 | 1 por grupo gerador |
| A14 | Tanque combustível 1000L | un | 1 | 15.000 | 15.000 | Autonomia ~8h à plena carga |
| A15 | Escapamento + atenuador acústico | cj | 1 | 25.000 | 25.000 | NBR 10151 (ruído) |
| A16 | Base antivibratória | cj | 1 | 8.000 | 8.000 | 1 por equipamento |
| A17 | Mão de obra instalação | vb | 1 | 55.000 | 55.000 | Instalação elétrica + mecânica |

**Critério de dimensionamento (500 kVA):** estimativa por carga essencial ≈ 30-40% da demanda total. Revisar com projeto elétrico (aba Elétrico).

---

### Grupo 3 — BOMBAS DE RECALQUE E PRESSURIZAÇÃO (linhas 18-24, subtotal E18 = R$ 159.000)

Sistema de abastecimento de água (reservatório superior + pressurização por zonas).

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A19 | Moto-bomba 15 CV (recalque) | un | 2 | 18.000 | 36.000 | 1 principal + 1 reserva (padrão) |
| A20 | Moto-bomba 5 CV (pressurização) | un | 2 | 8.500 | 17.000 | 1 principal + 1 reserva |
| A21 | Quadro comando soft-starter | un | 2 | 12.000 | 24.000 | 1 por conjunto de bombas |
| A22 | Pressurizador booster | un | 1 | 22.000 | 22.000 | Pavimentos superiores (alta pressão) |
| A23 | Tubulação recalque/sucção | vb | 1 | 35.000 | 35.000 | Aço galvanizado + conexões |
| A24 | Mão de obra instalação | vb | 1 | 25.000 | 25.000 | |

**Critério de dimensionamento:** vazão de recalque = 40 unid. × 150 L/dia × reserva 1,5 → ~50 m³/h. Confirmar com memorial hidráulico.

---

### Grupo 4 — PCI EQUIPAMENTOS HIDROMECÂNICOS (linhas 25-31, subtotal E25 = R$ 180.000)

Bomba de incêndio + RTI + jockey, conforme NBR 13714 + IT-22 CBMSC.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A26 | Moto-bomba PCI principal 25 CV | un | 1 | 28.000 | 28.000 | Dimensionada por NBR 13714 (Q×H) |
| A27 | Moto-bomba PCI reserva (jockey) | un | 1 | 12.000 | 12.000 | Manutenção de pressão |
| A28 | Reservatório RTI 60 m³ | un | 1 | 85.000 | 85.000 | Vol. = área construída × fator NBR |
| A29 | Quadro comando PCI | un | 1 | 18.000 | 18.000 | Com sinalização remota |
| A30 | Tubulação sucção/recalque | vb | 1 | 15.000 | 15.000 | Aço galvanizado SCH40 |
| A31 | Mão de obra instalação | vb | 1 | 22.000 | 22.000 | |

⚠ **Pendência:** reservatório e bombas PCI **não identificados nos IFCs** — estimativa por briefing. Confirmar com memorial hidro-PCI.

**Cruzamento:** este grupo é complementar à aba "Sprinklers" (sistema fixo) e "PPCI" (hidrantes/extintores). O PCI hidromecânico AQUI é só a casa de bombas + RTI.

---

### Grupo 5 — SPDA (PARA-RAIOS) — linhas 32-42, subtotal E32 = R$ 120.000

Sistema de proteção contra descargas atmosféricas, NBR 5419.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A33 | Captor tipo Franklin | un | 6 | 850 | 5.100 | 2 captores × torre + 2 extras |
| A34 | Cabo cobre nu 50mm² (descidas + anéis) | m | 1.400 | 55 | 77.000 | Perímetro × nº de descidas × altura |
| A35 | Cabo cobre nu 35mm² (anéis intermediários) | m | 600 | 42 | 25.200 | Anéis a cada ~15m altura |
| A36 | Cabo cobre nu 25mm² (equipotencial) | m | 80 | 35 | 2.800 | Aterramento local |
| A37 | Haste copperweld 5/8" × 2,4m | un | 8 | 120 | 960 | Malha de aterramento |
| A38 | Caixa inspeção aterramento | un | 16 | 280 | 4.480 | 1 por haste + extras |
| A39 | Conectores bronze | un | 212 | 18 | 3.816 | Estimativa 3 × n° pontos |
| A40 | Braçadeiras fixação | un | 476 | 8 | 3.808 | Cada 3m de cabo (1400/3 ≈ 476) |
| A41 | Soldas exotérmicas | un | 48 | 45 | 2.160 | Conexões cabo-cabo e cabo-haste |
| A42 | Mão de obra instalação | vb | 1 | 25.000 | 25.000 | |

**Critério de dimensionamento (NBR 5419):**
- Cabo 50mm²: perímetro cobertura (~150m) + 4 descidas × altura (~100m cada) ≈ 1.400m
- Hastes: malha 1 haste por 20m² área aterramento (estimativa)

---

### Grupo 6 — EXAUSTÃO DE CHURRASQUEIRAS (linhas 43-52, subtotal E43 = R$ 68.000)

Exaustão mecânica de churrasqueiras em áreas comuns (salão de festas, varandas gourmet).

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A44 | Exaustor centrífugo 3.000 m³/h | un | 2 | 8.500 | 17.000 | 1 por torre (2 torres) |
| A45 | Coifa aço inox AISI 304 | un | 4 | 3.200 | 12.800 | 2 churrasqueiras × 2 torres |
| A46 | Duto circular Ø300mm | m | 80 | 185 | 14.800 | Vertical até cobertura |
| A47 | Duto retangular 400×300mm | m | 30 | 220 | 6.600 | Horizontal (ligações) |
| A48 | Curvas e conexões | cj | 1 | 4.500 | 4.500 | |
| A49 | Damper corta-fogo | un | 2 | 2.800 | 5.600 | Entre compartimentos |
| A50 | Grelha de ventilação (ar compensação) | un | 4 | 450 | 1.800 | 1 por churrasqueira |
| A51 | Painel de comando | un | 1 | 5.500 | 5.500 | |
| A52 | Mão de obra | vb | 1 | 12.000 | 12.000 | |

**Premissa:** 4 churrasqueiras totais (2 por torre) em áreas comuns — confirmar com projeto arquitetônico / memorial de lazer.

---

### Grupo 7 — AR-CONDICIONADO / CLIMATIZAÇÃO (linhas 53-60, subtotal E53 = R$ 2.300.000)

**Maior incerteza da aba** — VRF multi-split com qtd genérica `cj = 1` em todos os itens e valor em bloco.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A54 | Condensadoras VRF | cj | 1 | 850.000 | 850.000 | ⚠ Estimativa paramétrica — DWG ainda não processado |
| A55 | Evaporadoras (cassete/hi-wall/duto) | cj | 1 | 450.000 | 450.000 | ⚠ Estimativa paramétrica |
| A56 | Tubulação frigorífica (cobre isolado) | vb | 1 | 380.000 | 380.000 | 1/4" a 3/4" |
| A57 | Linha de dreno | vb | 1 | 85.000 | 85.000 | DN20/DN25 |
| A58 | Cabos e eletrodutos | vb | 1 | 120.000 | 120.000 | Alimentação |
| A59 | Suportes, acessórios, fixações | vb | 1 | 65.000 | 65.000 | |
| A60 | Mão de obra instalação | vb | 1 | 350.000 | 350.000 | Vácuo + carga de gás |

⚠ **Pendência crítica:** valores paramétricos (~R$ 137/m² considerando 16.749 m² construídos). Quando o DWG HVAC chegar, detalhar por equipamento. Hoje é o **maior risco de imprecisão** da aba.

---

### Grupo 8 — VENTILAÇÃO MECÂNICA (escadas pressurizadas) — linhas 61-73, subtotal E61 = R$ 440.000

Sistema de pressurização de escadas de emergência — obrigatório NBR 14880:2024.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A62 | Ventilador centrífugo 10.000 m³/h, 7,5 CV | un | 2 | 25.000 | 50.000 | 1 por torre (2 torres) |
| A63 | Damper corta-fogo 90min Ø600mm | un | 64 | 1.400 | 89.600 | ~1 damper por pavto × 2 torres × 34 pavtos |
| A64 | Damper motorizado Ø600mm | un | 4 | 5.500 | 22.000 | Comando de zona |
| A65 | Duto vertical Ø600mm | m | 200 | 320 | 64.000 | Altura torre × 2 torres |
| A66 | Duto de derivação 400×300mm | m | 60 | 250 | 15.000 | Conexões |
| A67 | Isolamento térmico (lã de vidro 50mm) | m² | 380 | 45 | 17.100 | Superfície total dos dutos |
| A68 | Grelhas/difusores | un | 42 | 280 | 11.760 | Tomadas nas zonas |
| A69 | Sensor pressão diferencial | un | 4 | 2.200 | 8.800 | 4-20mA, 0-100Pa |
| A70 | Quadro comando IP65 + soft-starters | un | 1 | 20.000 | 20.000 | 1 central |
| A71 | CLP + IHM + automação | cj | 1 | 12.000 | 12.000 | Modbus |
| A72 | Cabos e eletrodutos | vb | 1 | 12.000 | 12.000 | |
| A73 | Mão de obra instalação | vb | 1 | 45.000 | 45.000 | |

**Critério:** 1 damper por pavimento × 34 pavtos × ~2 dutos/pavto = 64 (faz sentido com 2 torres).

---

### Grupo 9 — INTERFONE / VÍDEO PORTEIRO (linhas 74-81, subtotal E74 = R$ 120.000)

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A75 | Central portaria IP | un | 1 | 15.000 | 15.000 | 1 central única |
| A76 | Monitor interno apto | un | 96 | 650 | 62.400 | 24 aptos × 2 torres × 2 (estimativa) |
| A77 | Câmera entrada/hall | un | 4 | 1.800 | 7.200 | 2 halls × 2 torres |
| A78 | Fechadura eletromagnética | un | 6 | 900 | 5.400 | Portas de acesso |
| A79 | Servidor/switch rede | un | 2 | 5.000 | 10.000 | 1 por torre |
| A80 | Cabeamento + infra | vb | 1 | 20.000 | 20.000 | CAT6 |
| A81 | Mão de obra | vb | 1 | 15.000 | 15.000 | |

⚠ **Qtd de monitores (96)** tem comentário "24 aptos × 2 torres × 2" = 96 (2 monitores por apto — entrada + social). Confirmar se é premissa correta ou 1 monitor/apto (nesse caso ficaria 48).

---

### Grupo 10 — CFTV / CÂMERAS DE SEGURANÇA (linhas 82-90, subtotal E82 = R$ 103.000)

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A83 | Câmera IP dome 2MP | un | 30 | 1.200 | 36.000 | Garagens, halls, lazer, acessos |
| A84 | Câmera IP bullet 4MP | un | 8 | 2.500 | 20.000 | Perímetro externo |
| A85 | NVR 64 canais | un | 1 | 12.000 | 12.000 | 1 central (cabe 30+8+margem) |
| A86 | Switch PoE 24 portas | un | 3 | 3.500 | 10.500 | Distribuição câmeras |
| A87 | Monitor monitoramento 32" | un | 2 | 3.000 | 6.000 | Portaria |
| A88 | Rack + patch panel | cj | 1 | 8.000 | 8.000 | |
| A89 | Cabeamento CAT6 + infra | vb | 1 | 15.000 | 15.000 | |
| A90 | Mão de obra | vb | 1 | 12.000 | 12.000 | |

---

### Grupo 11 — ILUMINAÇÃO DE EMERGÊNCIA (linhas 91-97, subtotal E91 = R$ 87.000)

Conforme NBR 10898.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A92 | Luminária emergência LED 30W | un | 200 | 180 | 36.000 | Rotas de fuga — 1 a cada ~10m corredor |
| A93 | Luminária emergência LED 60W | un | 50 | 350 | 17.500 | Garagens + áreas técnicas |
| A94 | Bloco sinalização | un | 120 | 95 | 11.400 | Placas fotoluminescentes |
| A95 | Central iluminação emergência | un | 2 | 8.000 | 16.000 | 1 por torre — 24Vdc |
| A96 | Cabeamento + infra | vb | 1 | 12.000 | 12.000 | |
| A97 | Mão de obra | vb | 1 | 10.000 | 10.000 | |

**Critério NBR 10898:**
- Rotas de fuga: 1 luminária a cada ~10m linear
- Garagens: 1 cada ~30m²
- Blocos de sinalização: nas saídas, mudanças de direção, portas

---

### Grupo 12 — AUTOMAÇÃO PREDIAL / BMS (linhas 98-106, subtotal E98 = R$ 210.000)

Sistema de supervisão que integra todos os subsistemas.

| # | Item | Un | Qtd | Custo Unit. | Total | Regra / Origem |
|---|---|---|---|---|---|---|
| A99 | Controladora central BMS | un | 1 | 45.000 | 45.000 | Hardware + firmware |
| A100 | Módulos de campo (I/O) | un | 10 | 3.500 | 35.000 | Distribuído por sistema |
| A101 | Software SCADA | un | 1 | 30.000 | 30.000 | Licença + parametrização |
| A102 | Sensores diversos | cj | 1 | 15.000 | 15.000 | Temp, nível, pressão |
| A103 | Integração elevadores | vb | 1 | 12.000 | 12.000 | Modbus/BACnet |
| A104 | Integração PCI + bombas + ventilação | vb | 1 | 18.000 | 18.000 | |
| A105 | Cabeamento controle + infra | vb | 1 | 20.000 | 20.000 | |
| A106 | Mão de obra + comissionamento | vb | 1 | 35.000 | 35.000 | |

---

## Total geral

**E108 = R$ 6.915.000** (valor digitado, sem fórmula — soma dos 12 subtotais)

Distribuição por grupo:

| Grupo | Subtotal | % do total |
|---|---:|---:|
| Ar-condicionado | 2.300.000 | 33,3% |
| Elevadores | 2.700.000 | 39,0% |
| Ventilação mecânica | 440.000 | 6,4% |
| Grupo gerador | 428.000 | 6,2% |
| Automação BMS | 210.000 | 3,0% |
| PCI hidromecânico | 180.000 | 2,6% |
| Bombas recalque | 159.000 | 2,3% |
| Interfone | 120.000 | 1,7% |
| SPDA | 120.000 | 1,7% |
| CFTV | 103.000 | 1,5% |
| Iluminação emergência | 87.000 | 1,3% |
| Exaustão churrasqueiras | 68.000 | 1,0% |
| **Total** | **6.915.000** | 100% |

**Elevadores + Ar-condicionado = 72,3% do custo** — concentração de risco nesses dois grupos.

---

## Workflow de preenchimento (próxima obra)

1. **Atualizar cabeçalho** (C2, C3, C4) com projeto/empresa/revisão
2. **Revisar Grupo 1 (Elevadores)**:
   - Qtd elevadores sociais e de carga (depende de nº torres, nº pavtos, briefing)
   - Cotar com ao menos 2 fabricantes (ThyssenKrupp, Otis, Atlas, etc.)
3. **Revisar Grupo 7 (Ar-condicionado)** — aguardar DWG HVAC + detalhar item-a-item
4. **Revisar Grupo 4 (PCI)** — validar com memorial hidro-PCI + Corpo de Bombeiros
5. **Revisar Grupo 8 (Ventilação)** — qtd dampers varia conforme nº pavtos (regra ~1/pavto/torre × 2 dutos)
6. **Revisar quantitativos paramétricos** que dependem do nº de apartamentos:
   - Monitor vídeo-porteiro: N aptos × N monitores por apto
   - Câmeras: depende do layout das áreas comuns
   - Iluminação emergência: área construída × critério NBR
7. **Revisar Grupo 5 (SPDA)** — cabeamento varia com altura da torre e perímetro de cobertura
8. **Cruzar com outras disciplinas** pra evitar double-count:
   - Elevadores: bate com EPCs (D33, D38)?
   - Grupo gerador: dimensionamento casa com demanda em Elétrico
   - PCI: não sobrepor com abas Sprinklers e PPCI

---

## Pendências / decisões em aberto

- [ ] **Ar-condicionado (R$ 2,3M)** está totalmente em `cj=1` sem detalhamento — aguarda DWG HVAC pra discriminar condensadoras, evaporadoras, tubulação por pavto/apto
- [ ] **PCI hidromecânico** não identificado nos IFCs — confirmar reservatório RTI e bombas com memorial hidro
- [ ] **Divergência elevadores sociais** entre esta aba (6 unid.) e EPCs!D38 (3 elev.) — resolver qual é o dado real
- [ ] **Monitores vídeo-porteiro (96 unid.)** baseado em estimativa "24 aptos × 2 torres × 2 monitores/apto" — confirmar nº real de aptos e se tem 2 monitores por unid.
- [ ] **Qtd de dampers de ventilação (64)** baseada em premissa "1/pavto × 2 dutos × 2 torres × 16 pavtos equiv" — confirmar com projeto arq (nº de pavtos com escada pressurizada)
- [ ] **Capacidade grupo gerador (500 kVA)** — cruzar com demanda do projeto Elétrico
- [ ] **Sem fórmulas na aba** — alterar qtd não atualiza total. Considerar converter para fórmulas `=C×D` na iteração 2 + subtotais `=SUMIF` por grupo
- [ ] **Referência projeto:** "2 torres, 34 pavimentos (Térreo+5G+Lazer+24Tipo+3Técnicos)" vs CAPA que lista 35 linhas de pavimentos (Torre 1 só) — entender discrepância
- [ ] Itens de **observação (F)** parcialmente preenchidos — completar pra todos os itens críticos (especificação mínima pro orçamentista validar fornecedor)
