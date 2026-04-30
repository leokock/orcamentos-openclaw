# Aba: MOVIMENTAÇÃO_DE_TERRA
Dimensão: A1:K33 | Linhas: 33 | Colunas: 11

## Conteúdo Completo

### Células Mescladas: 10
  - B29:C29
  - A16:E16
  - A10:E10
  - B20:C20
  - A25:E25
  - A33:E33
  - A11:E11
  - A2:G2
  - A31:E31
  - A17:E17

**Linha 2:** [A2] MOVIMENTAÇÃO DE TERRA
**Linha 3:** [A3] Data
**Linha 4:** [A4] Arquivo base
**Linha 6:** [A6] ESCAVAÇÃO VERTICAL DE SUBSOLO
**Linha 8:** [A8] Descrição | [B8] Área de subsolo (m) | [C8] Altura do subsolo (m) | [D8] Volume total de escavação (m3) | [E8] Preço unitário de escavação (R$ / m3) | [F8] Valor total | [G8] Observação
**Linha 9:** [A9] Escavação | [B9] 📐 `=DADOS_INICIAIS!E23` | [D9] 📐 `=C9*B9` | [E9] 0 | [F9] 📐 `=E9*D9*1.1`
**Linha 10:** [A10] TOTAL | [F10] 📐 `=SUM(F9:F9)`
**Linha 12:** [A12] REBAIXAMENTO DE LENÇOL FREÁTICO
**Linha 14:** [A14] Descrição | [B14] Quantidade (dias) | [E14] Preço unitário de rebaixamento (R$ / dias) | [F14] Valor total | [G14] Observação
**Linha 15:** [A15] Rebaixamento de lençol | [B15] 📐 `=4*30` | [E15] 200 | [F15] 📐 `=B15*E15*1.1` | [G15] 4 meses
**Linha 16:** [A16] TOTAL | [F16] 📐 `=SUM(F15:F15)`
**Linha 18:** [A18] ESCAVAÇÃO E REATERRO DE VALAS
**Linha 20:** [A20] Descrição | [B20] Parâmetro | [D20] Volume total de escavação (m3) | [E20] Preço unitário (R$ / m3) | [F20] Valor total | [G20] Observação
**Linha 21:** [A21] Escavação mecanizada para blocos e baldrames | [B21] 1.3 | [C21] m³ / Vol infra | [D21] 📐 `=B21*INFRAESTRUTURA!D29` | [E21] 36.36 | [F21] 📐 `=E21*D21*1.1`
**Linha 22:** [A22] Reaterro para blocos e baldrames | [B22] 0.6 | [C22] m³ / Vol Escavação | [D22] 📐 `=D21-INFRAESTRUTURA!D29` | [E22] 14.55 | [F22] 📐 `=E22*D22*1.1`
**Linha 23:** [A23] Movimentação de bota-fora | [B23] 1.3 | [D23] 📐 `=(D21-D22)*B23` | [E23] 45.45 | [F23] 📐 `=E23*D23*1.1`
**Linha 24:** [A24] Movimentação de terra das estacas | [B24] 1 | [C24] m³ | [D24] 📐 `=INFRAESTRUTURA!D19` | [E24] 68.18 | [F24] 📐 `=E24*D24*1.1`
**Linha 25:** [A25] TOTAL | [F25] 📐 `=SUM(F21:F24)`
**Linha 27:** [A27] REGULARIZAÇÃO E APILOAMENTO DE FUNDO DE VALAS
**Linha 29:** [A29] Descrição | [B29] Parâmetro | [D29] Área de lastro (m²) | [E29] Preço unitário (R$ / m2) | [F29] Valor total | [G29] Observação
**Linha 30:** [A30] Lastro de concreto magto e=5cm | [B30] 0.8 | [C30] m² / APE | [D30] 📐 `=B30*DADOS_INICIAIS!E25` | [E30] 📐 `=370*0.1` | [F30] 📐 `=E30*D30*1.1` | [G30] Definição trazida do Celebration da Passe | [H30] 📐 `=F30/DADOS_INICIAIS!E25`
**Linha 31:** [A31] TOTAL | [F31] 📐 `=SUM(F30:F30)`
**Linha 33:** [A33] TOTAL MOVIMENTAÇÃO DE TERRA | [F33] 📐 `=F10+F16+F25+F31` | [G33] 📐 `=F33/DADOS_INICIAIS!E9`

## Fórmulas Extraídas

- `B9`: `=DADOS_INICIAIS!E23`
- `D9`: `=C9*B9`
- `F9`: `=E9*D9*1.1`
- `F10`: `=SUM(F9:F9)`
- `B15`: `=4*30`
- `F15`: `=B15*E15*1.1`
- `F16`: `=SUM(F15:F15)`
- `D21`: `=B21*INFRAESTRUTURA!D29`
- `F21`: `=E21*D21*1.1`
- `D22`: `=D21-INFRAESTRUTURA!D29`
- `F22`: `=E22*D22*1.1`
- `D23`: `=(D21-D22)*B23`
- `F23`: `=E23*D23*1.1`
- `D24`: `=INFRAESTRUTURA!D19`
- `F24`: `=E24*D24*1.1`
- `F25`: `=SUM(F21:F24)`
- `D30`: `=B30*DADOS_INICIAIS!E25`
- `E30`: `=370*0.1`
- `F30`: `=E30*D30*1.1`
- `H30`: `=F30/DADOS_INICIAIS!E25`
- `F31`: `=SUM(F30:F30)`
- `F33`: `=F10+F16+F25+F31`
- `G33`: `=F33/DADOS_INICIAIS!E9`