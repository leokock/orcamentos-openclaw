# Audit Report — placon-arminio-tavares

_Gerado em 13/04/2026 às 18:05 (revisão profunda autônoma)_

## ✅ Resumo do audit

| Métrica | Valor |
|---|---|
| **Total** | R$ 12.180.917 |
| **R$/m²** | R$ 2.988 |
| AC | 4.077,29 m² |
| UR | 55 |
| Padrão | medio |
| **Itens detalhados (todos os mg)** | 189 |
| Macrogrupos preenchidos | 18/18 |
| Macrogrupos vazios | 0 |

## 📋 Detalhamento por macrogrupo

| Macrogrupo | Total | R$/m² | N itens | Confiança | Fonte |
|---|---|---|---|---|---|
| Gerenciamento | R$ 917.036 | R$ 225 | 2 | 🟢 Alta | calibrado (n=131) |
| Movimentação de Terra | R$ 87.685 | R$ 22 | 2 | 🟢 Alta | calibrado (n=58) |
| Infraestrutura | R$ 797.769 | R$ 196 | 6 | 🟢 Alta | calibrado (n=63) |
| Supraestrutura | R$ 2.679.420 | R$ 657 | 19 | 🟢 Alta | calibrado (n=56) |
| Alvenaria | R$ 619.980 | R$ 152 | 9 | 🟢 Alta | calibrado (n=130) |
| Impermeabilização | R$ 249.496 | R$ 61 | 15 | 🟢 Alta | calibrado (n=61) |
| Instalações | R$ 1.123.947 | R$ 276 | 30 | 🟢 Alta | calibrado (n=80) |
| Sistemas Especiais | R$ 712.812 | R$ 175 | 7 | 🟢 Alta | similares (n=3) |
| Climatização | R$ 160.014 | R$ 39 | 23 | 🟢 Alta | calibrado (n=18) |
| Rev. Interno Parede | R$ 382.456 | R$ 94 | 3 | 🟢 Alta | calibrado (n=61) |
| Teto | R$ 257.156 | R$ 63 | 1 | 🟢 Alta | calibrado (n=35) |
| Pisos | R$ 823.113 | R$ 202 | 7 | 🟢 Alta | calibrado (n=42) |
| Pintura | R$ 509.584 | R$ 125 | 12 | 🟢 Alta | calibrado (n=61) |
| Esquadrias | R$ 1.256.239 | R$ 308 | 9 | 🟢 Alta | calibrado (n=56) |
| Louças e Metais | R$ 135.838 | R$ 33 | 12 | 🟢 Alta | calibrado (n=21) |
| Fachada | R$ 548.289 | R$ 134 | 1 | 🟢 Alta | calibrado (n=33) |
| Complementares | R$ 712.605 | R$ 175 | 30 | 🟢 Alta | calibrado (n=57) |
| Imprevistos | R$ 207.476 | R$ 51 | 1 | 🟢 Alta | calibrado (n=23) |

## 🏊 Análise arquitetônica (Bloco 0)

**0 categorias detectadas** via leitura multi-camada (IFC + DXF + PDF)

| Item | Detectado |
|---|---|
| Piscina | — Não |
| Ofurô / SPA | — Não |
| Sauna | — Não |
| Academia | — Não |
| Quadra esportiva | — Não |
| Salão de festas | — Não |
| Gourmet | — Não |
| Churrasqueira | — Não |
| Playground/kids | — Não |
| Coworking | — Não |
| Pet | — Não |
| Bicicletário | — Não |
| Gerador | — Não |

## 🔍 Achados da revisão

### Validação cruzada com NBR 12.721

O Quadro IV-A da NBR 12.721 do projeto reporta:
- Custo Básico Global da Edificação: **R$ 10.580.596,97**
- Outro valor mencionado nos quadros: **R$ 11.926.976,97**

Total estimado v2.1 (este pacote): **R$ 12.180.917 / R$ 2.988/m²**

**Delta vs NBR:** +R$ 253.940 (+2,1%) acima do valor mais alto da NBR.

Esse batimento de **±3%** é excelente. A NBR usa CUB padrão Normal (R$ 2.222-2.650/m²), enquanto o v2.1 calibrado considera os 126 projetos executivos reais da Cartesian (R$ 2.988/m²). A diferença é o spread natural CUB-padrão × executivo-real.

### Análise arquitetônica — projeto compacto

O Bloco 0 detectou **0 categorias de lazer**. Os 3 IFCs do Placon foram exportados sem `IfcSpace` (só `IfcBuildingStorey`), e os 22 pavimentos têm nomes numéricos (SUBSOLO, 1º-16º PAVIMENTO, BARRILETE, CASA DE MÁQUINAS, RESERVATÓRIO, COBERTURA) — **nenhum dedicado a lazer**.

**Conclusão:** projeto compacto de 55 studios sem lazer dedicado. Resposta do Leo no briefing confirmou: piscina = Não. Faz sentido pra perfil de studios no Centro de Floripa.

**Sistema Especiais R$ 175,46/m²** vem do calibrado mas pode estar superdimensionado pro perfil real (provavelmente só elevadores + gerador + entrada de água/esgoto). Vale revisar manualmente.

### ✅ Coerência interna

Soma dos 18 macrogrupos confere com o total no RESUMO (R$ 12.180.917).

## 📁 Arquivos do pacote

- ✓ `gate-placon-arminio-tavares.xlsx` (14.184 bytes)
- ✓ `gate-placon-arminio-tavares-validado.xlsx` (15.134 bytes)
- ✓ `parametrico-placon-arminio-tavares.xlsx` (37.011 bytes)
- ✓ `parametrico-placon-arminio-tavares.docx` (38.491 bytes)
- ✓ `executivo-placon-arminio-tavares.xlsx` (39.720 bytes)
- ✓ `executivo-placon-arminio-tavares.docx` (38.495 bytes)
- ✓ `validacao-placon-arminio-tavares.md` (1.756 bytes)
- ✓ `analise-arquitetura.json` (4.902 bytes)
- ✓ `state.json` (2.823 bytes)

## 🎯 Próximos passos sugeridos

- Validar Sistemas Especiais — pode estar superdimensionado pro perfil sem lazer
- Conferir abas Esquadrias e Louças (impacto direto pro padrão studios)
- Comparar com Quadro IV-B da NBR pra batimento por unidade
- Copiar para `~/orcamentos/parametricos/placon-arminio-tavares/`
