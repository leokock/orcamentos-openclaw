# Aba: CONTENÇÕES
Dimensão: A1:J46 | Linhas: 46 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 14
  - D25:E25
  - A3:H3
  - A46:F46
  - B25:C25
  - A13:A14
  - A15:A16
  - A40:F40
  - D9:E9
  - B9:C9
  - A30:F30
  - A21:F21
  - B35:C35
  - A11:A12
  - D35:E35

**Linha 3:** [A3] CONTENÇÃO
**Linha 4:** [A4] Data
**Linha 5:** [A5] Arquivo base
**Linha 7:** [A7] CORTINA DE ESTACAS
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total
**Linha 10:** [A10] Número de Estacas | [B10] 0.15 | [C10] un / APE | [D10] 📐 `=B10*DADOS_INICIAIS!E25` | [E10] un
**Linha 11:** [A11] Estaca Hélice Continua Diâmetro 40 | [B11] 0.1 | [D11] 📐 `=B11*$D$10` | [E11] un
**Linha 12:** [B12] 20 | [C12] m/un  | [D12] 📐 `=B12*D11` | [E12] m | [G12] 📐 `=F12*D12`
**Linha 13:** [A13] Estaca Hélice Continua Diâmetro 50 | [B13] 0.5 | [D13] 📐 `=B13*$D$10` | [E13] un
**Linha 14:** [B14] 20 | [C14] m/un  | [D14] 📐 `=B14*D13` | [E14] m | [G14] 📐 `=F14*D14`
**Linha 15:** [A15] Estaca Hélice Continua Diâmetro 60 | [B15] 0.4 | [C15] un / APE | [D15] 📐 `=B15*$D$10` | [E15] un
**Linha 16:** [B16] 20 | [C16] m/un  | [D16] 📐 `=B16*D15` | [E16] m | [G16] 📐 `=F16*D16`
**Linha 17:** [A17] Concreto | [B17] 📐 `=(PI()*0.4^2)/4*D14+(PI()*0.5^2)/4*D16+(PI()*0.6^2)/4*D12` | [C17] un / APE | [D17] 📐 `=(PI()*0.4^2)/4*D14+(PI()*0.5^2)/4*D16+(PI()*0.6^2)/4*D12` | [E17] m³ | [G17] 📐 `=F17*D17`
**Linha 18:** [A18] Armação 6,3mm | [B18] 1.6575131198547477 | [C18] kg / m³ | [D18] 📐 `=B18*D17` | [E18] kg | [G18] 📐 `=F18*D18`
**Linha 19:** [A19] Armação 16mm | [B19] 10.1783375510674 | [C19] kg / m³ | [D19] 📐 `=B19*D17` | [E19] kg | [G19] 📐 `=F19*D19`
**Linha 20:** [A20] Mobilização | [B20] 1 | [C20] vb | [D20] 1 | [E20] vb | [G20] 📐 `=F20*D20`
**Linha 21:** [A21] TOTAL | [G21] 📐 `=SUM(G10:G20)`
**Linha 23:** [A23] PAREDE DE CONCRETO
**Linha 25:** [A25] Descrição | [B25] Parâmetro | [D25] Quantidade | [F25] Preço unitário | [G25] Valor total
**Linha 26:** [A26] Fabricação, montagem e desmontagem de forma para blocos e baldrames resinado | [B26] 2.1 | [C26] m² / APE | [D26] 📐 `=B26*DADOS_INICIAIS!E25` | [E26] m² | [G26] 📐 `=F26*D26`
**Linha 27:** [A27] Concreto | [B27] 0.65 | [C27] m³ / APE | [D27] 📐 `=B27*DADOS_INICIAIS!E25` | [E27] m³ | [G27] 📐 `=F27*D27`
**Linha 28:** [A28] Armação | [B28] 110 | [C28] kg / m³ | [D28] 📐 `=B28*D27` | [E28] kg | [G28] 📐 `=F28*D28`
**Linha 29:** [A29] Mão de obra | [B29] 📐 `=SUPRAESTRUTURA!B15*1.5` | [C29] R$ / APE | [D29] 📐 `=DADOS_INICIAIS!E25` | [E29] m² | [F29] 📐 `=B29` | [G29] 📐 `=F29*D29`
**Linha 30:** [A30] TOTAL | [G30] 📐 `=SUM(G26:G29)`
**Linha 33:** [A33] PAREDE DIAFRAGMA
**Linha 35:** [A35] Descrição | [B35] Parâmetro | [D35] Quantidade | [F35] Preço unitário | [G35] Valor total
**Linha 36:** [A36] Fabricação, montagem e desmontagem de forma para blocos e baldrames resinado | [B36] 2.1 | [C36] m² / APE | [D36] 📐 `=B36*DADOS_INICIAIS!E35` | [E36] m² | [G36] 📐 `=F36*D36`
**Linha 37:** [A37] Concreto | [B37] 0.65 | [C37] m³ / APE | [D37] 📐 `=B37*DADOS_INICIAIS!E35` | [E37] m³ | [G37] 📐 `=F37*D37`
**Linha 38:** [A38] Armação | [B38] 110 | [C38] kg / m³ | [D38] 📐 `=B38*D37` | [E38] kg | [G38] 📐 `=F38*D38`
**Linha 39:** [A39] Mão de obra | [B39] 📐 `=SUPRAESTRUTURA!B84*1.5` | [C39] R$ / APE | [D39] 📐 `=DADOS_INICIAIS!E35` | [E39] m² | [F39] 📐 `=B39` | [G39] 📐 `=F39*D39`
**Linha 40:** [A40] TOTAL | [G40] 📐 `=SUM(G36:G39)`
**Linha 46:** [A46] TOTAL INFRAESTRUTURA | [G46] 📐 `=G21+G30` | [H46] 📐 `=G46/DADOS_INICIAIS!E9`

## Fórmulas Extraídas

- `D10`: `=B10*DADOS_INICIAIS!E25`
- `D11`: `=B11*$D$10`
- `D12`: `=B12*D11`
- `G12`: `=F12*D12`
- `D13`: `=B13*$D$10`
- `D14`: `=B14*D13`
- `G14`: `=F14*D14`
- `D15`: `=B15*$D$10`
- `D16`: `=B16*D15`
- `G16`: `=F16*D16`
- `B17`: `=(PI()*0.4^2)/4*D14+(PI()*0.5^2)/4*D16+(PI()*0.6^2)/4*D12`
- `D17`: `=(PI()*0.4^2)/4*D14+(PI()*0.5^2)/4*D16+(PI()*0.6^2)/4*D12`
- `G17`: `=F17*D17`
- `D18`: `=B18*D17`
- `G18`: `=F18*D18`
- `D19`: `=B19*D17`
- `G19`: `=F19*D19`
- `G20`: `=F20*D20`
- `G21`: `=SUM(G10:G20)`
- `D26`: `=B26*DADOS_INICIAIS!E25`
- `G26`: `=F26*D26`
- `D27`: `=B27*DADOS_INICIAIS!E25`
- `G27`: `=F27*D27`
- `D28`: `=B28*D27`
- `G28`: `=F28*D28`
- `B29`: `=SUPRAESTRUTURA!B15*1.5`
- `D29`: `=DADOS_INICIAIS!E25`
- `F29`: `=B29`
- `G29`: `=F29*D29`
- `G30`: `=SUM(G26:G29)`
- `D36`: `=B36*DADOS_INICIAIS!E35`
- `G36`: `=F36*D36`
- `D37`: `=B37*DADOS_INICIAIS!E35`
- `G37`: `=F37*D37`
- `D38`: `=B38*D37`
- `G38`: `=F38*D38`
- `B39`: `=SUPRAESTRUTURA!B84*1.5`
- `D39`: `=DADOS_INICIAIS!E35`
- `F39`: `=B39`
- `G39`: `=F39*D39`
- `G40`: `=SUM(G36:G39)`
- `G46`: `=G21+G30`
- `H46`: `=G46/DADOS_INICIAIS!E9`