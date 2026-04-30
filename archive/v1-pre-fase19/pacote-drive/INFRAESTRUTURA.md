# Aba: INFRAESTRUTURA
Dimensão: A1:J41 | Linhas: 41 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 12
  - A33:F33
  - A3:H3
  - A36:F36
  - A17:A18
  - A13:A14
  - A23:F23
  - D27:E27
  - A15:A16
  - B9:C9
  - B27:C27
  - D9:E9
  - A11:A12

**Linha 3:** [A3] INFRAESTRUTURA
**Linha 4:** [A4] Data | [B4] 2024-06-29 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] FUNDAÇÃO PROFUNDA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Número de Estacas | [B10] 0.14 | [C10] un / APE | [D10] 📐 `=ROUNDUP(B10*DADOS_INICIAIS!$E$25,0)` | [E10] un | [H10] Índice Passione
**Linha 11:** [A11] Estaca Hélice Continua Diâmetro 40 | [B11] 0 | [D11] 📐 `=ROUNDUP(B11*$D$10,0)` | [E11] un
**Linha 12:** [B12] 28 | [C12] m/un  | [D12] 📐 `=B12*D11` | [E12] m | [F12] 70 | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Estaca Hélice Continua Diâmetro 50 | [B13] 0.6 | [D13] 📐 `=ROUNDUP(B13*D10,0)` | [E13] un
**Linha 14:** [B14] 28 | [C14] m/un  | [D14] 📐 `=B14*D13` | [E14] m | [F14] 90 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] Estaca Hélice Continua Diâmetro 60 | [B15] 0.4 | [C15] un / APE | [D15] 📐 `=ROUNDUP(B15*$D$10,0)` | [E15] un
**Linha 16:** [B16] 📐 `=$B$14` | [C16] m/un  | [D16] 📐 `=B16*D15` | [E16] m | [F16] 105 | [G16] 📐 `=F16*D16*1.1`
**Linha 17:** [A17] Estaca Hélice Continua Diâmetro 80 | [B17] 0 | [C17] un / APE | [D17] 📐 `=ROUNDUP(B17*$D$10,0)` | [E17] un
**Linha 18:** [B18] 📐 `=$B$14` | [C18] m/un  | [D18] 📐 `=B18*D17` | [E18] m | [F18] 120 | [G18] 📐 `=F18*D18*1.1`
**Linha 19:** [A19] Concreto (40 Mpa) | [B19] 1.3 | [C19] perda | [D19] 📐 `=(PI()*((0.4^2)/4)*D12+PI()*((0.5^2)/4)*D14+PI()*((0.6^2)/4)*D16)` | [E19] m³ | [F19] 📐 `=(535+45+(1.67*0.6))*B19` | [G19] 📐 `=F19*D19*1.1`
**Linha 20:** [A20] Armação  | [B20] 12 | [C20] kg / m³ | [D20] 📐 `=B20*D19` | [E20] kg | [F20] 7.62 | [G20] 📐 `=F20*D20*1.1`
**Linha 21:** [A21] Mobilização | [B21] 1 | [C21] vb | [D21] 1 | [E21] vb | [F21] 12500 | [G21] 📐 `=F21*D21*1.1`
**Linha 22:** [A22] Apoio e arrasamento de estacas | [D22] 📐 `=D10` | [E22] un | [F22] 300 | [G22] 📐 `=F22*D22*1`
**Linha 23:** [A23] TOTAL | [G23] 📐 `=SUM(G10:G22)`
**Linha 25:** [A25] FUNDAÇÃO RASA
**Linha 27:** [A27] Descrição | [B27] Parâmetro | [D27] Quantidade | [F27] Preço unitário | [G27] Valor total | [H27] Observação
**Linha 28:** [A28] Fabricação, montagem e desmontagem de forma para blocos e baldrames resinado | [B28] 1.1 | [C28] m² / APE | [D28] 📐 `=B28*DADOS_INICIAIS!E25` | [E28] m² | [F28] 68 | [G28] 📐 `=F28*D28*1.1`
**Linha 29:** [A29] Concreto (40 Mpa) | [B29] 0.6 | [C29] m³ / APE | [D29] 📐 `=B29*DADOS_INICIAIS!E25` | [E29] m³ | [F29] 📐 `=(535+45+(1.67*0.6))*1.05` | [G29] 📐 `=F29*D29*1.1` | [H29] Indice do Passione
**Linha 30:** [A30] Armação | [B30] 70 | [C30] kg / m³ | [D30] 📐 `=B30*D29` | [E30] kg | [F30] 7.62 | [G30] 📐 `=F30*D30*1.1`
**Linha 31:** [A31] Piso de concreto armado | [B31] 1 | [C31] m² / APE | [D31] 📐 `=B31*DADOS_INICIAIS!E25` | [E31] m² | [F31] 📐 `=SUM(G39:G41)` | [G31] 📐 `=F31*D31*1.1`
**Linha 32:** [A32] Mão de obra | [B32] 📐 `=SUPRAESTRUTURA!B43*1.5` | [C32] R$ / APE | [D32] 📐 `=DADOS_INICIAIS!E25` | [E32] m² | [F32] 📐 `=B32` | [G32] 📐 `=F32*D32*1.1`
**Linha 33:** [A33] TOTAL | [G33] 📐 `=SUM(G28:G32)`
**Linha 36:** [A36] TOTAL INFRAESTRUTURA | [G36] 📐 `=G23+G33` | [H36] 📐 `=G36/DADOS_INICIAIS!E9`
**Linha 38:** [E38] Custo unit. | [F38] Indice | [G38] Custo /m2 | [H38] 📐 `=H36/1.1`
**Linha 39:** [D39] Concreto | [E39] 📐 `=$F$29` | [F39] 0.12 | [G39] 📐 `=F39*E39`
**Linha 40:** [D40] Armação  | [E40] 📐 `=$F$30` | [F40] 📐 `=110*F39` | [G40] 📐 `=F40*E40`
**Linha 41:** [D41] Forma | [E41] 📐 `=$F$28` | [F41] 📐 `=1*F39` | [G41] 📐 `=F41*E41`

## Fórmulas Extraídas

- `D10`: `=ROUNDUP(B10*DADOS_INICIAIS!$E$25,0)`
- `D11`: `=ROUNDUP(B11*$D$10,0)`
- `D12`: `=B12*D11`
- `G12`: `=F12*D12*1.1`
- `D13`: `=ROUNDUP(B13*D10,0)`
- `D14`: `=B14*D13`
- `G14`: `=F14*D14*1.1`
- `D15`: `=ROUNDUP(B15*$D$10,0)`
- `B16`: `=$B$14`
- `D16`: `=B16*D15`
- `G16`: `=F16*D16*1.1`
- `D17`: `=ROUNDUP(B17*$D$10,0)`
- `B18`: `=$B$14`
- `D18`: `=B18*D17`
- `G18`: `=F18*D18*1.1`
- `D19`: `=(PI()*((0.4^2)/4)*D12+PI()*((0.5^2)/4)*D14+PI()*((0.6^2)/4)*D16)`
- `F19`: `=(535+45+(1.67*0.6))*B19`
- `G19`: `=F19*D19*1.1`
- `D20`: `=B20*D19`
- `G20`: `=F20*D20*1.1`
- `G21`: `=F21*D21*1.1`
- `D22`: `=D10`
- `G22`: `=F22*D22*1`
- `G23`: `=SUM(G10:G22)`
- `D28`: `=B28*DADOS_INICIAIS!E25`
- `G28`: `=F28*D28*1.1`
- `D29`: `=B29*DADOS_INICIAIS!E25`
- `F29`: `=(535+45+(1.67*0.6))*1.05`
- `G29`: `=F29*D29*1.1`
- `D30`: `=B30*D29`
- `G30`: `=F30*D30*1.1`
- `D31`: `=B31*DADOS_INICIAIS!E25`
- `F31`: `=SUM(G39:G41)`
- `G31`: `=F31*D31*1.1`
- `B32`: `=SUPRAESTRUTURA!B43*1.5`
- `D32`: `=DADOS_INICIAIS!E25`
- `F32`: `=B32`
- `G32`: `=F32*D32*1.1`
- `G33`: `=SUM(G28:G32)`
- `G36`: `=G23+G33`
- `H36`: `=G36/DADOS_INICIAIS!E9`
- `H38`: `=H36/1.1`
- `E39`: `=$F$29`
- `G39`: `=F39*E39`
- `E40`: `=$F$30`
- `F40`: `=110*F39`
- `G40`: `=F40*E40`
- `E41`: `=$F$28`
- `F41`: `=1*F39`
- `G41`: `=F41*E41`