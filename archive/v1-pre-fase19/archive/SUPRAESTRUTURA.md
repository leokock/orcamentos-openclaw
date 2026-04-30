# Aba: SUPRAESTRUTURA
Dimensão: A1:L79 | Linhas: 79 | Colunas: 12

## Conteúdo Completo

### Células Mescladas: 17
  - B21:C21
  - A3:H3
  - D49:E49
  - A45:F45
  - D63:E63
  - B34:C34
  - D34:E34
  - A77:F77
  - A74:F74
  - A17:F17
  - B63:C63
  - B9:C9
  - A30:F30
  - D9:E9
  - B49:C49
  - A59:F59
  - D21:E21

**Linha 3:** [A3] SUPRAESTRUTURA
**Linha 4:** [A4] Data | [B4] 2024-06-29 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] SUPRAESTRUTURA - LAJE MACIÇA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Fabricação forma | [B10] 1 | [C10] Jogos | [D10] 📐 `=(D11/1)*B10` | [E10] m² | [F10] 110 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Montagem de forma | [B11] 1.2 | [C11] m² / AC | [D11] 📐 `=B11*'Obra '!D36` | [E11] m² | [F11] 2.5 | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Escoramento | [B12] 4 | [C12] un / AE | [E12] un | [F12] 📐 `=17` | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Concreto  | [B13] 0.22 | [C13] m³ / AC | [D13] 📐 `=B13*'Obra '!D36` | [E13] m³ | [F13] 📐 `=535+45` | [G13] 📐 `=F13*D13*1.05*1.1`
**Linha 14:** [A14] Armadura Convencional para Estrutura | [B14] 78 | [C14] kg / m³ | [D14] 📐 `=D13*B14` | [E14] kg | [F14] 7.62 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] Mão de obra - estrutura em concreto armado | [B15] 240 | [C15] R$ / AC | [E15] m² | [F15] 📐 `=B15` | [G15] 📐 `=F15*D15*1.1`
**Linha 16:** [A16] Perfuração de vigas | [B16] 5300 | [C16] R$ / NP | [E16] vb | [F16] 📐 `=B16*DADOS_INICIAIS!$E$15` | [G16] 📐 `=F16*D16*1.1` | [H16] Coeficiente originário do Gran Torino (R$ 160,00/un) | [I16] Nova utiliza a verba de 1.500,00 por pav
**Linha 17:** [A17] TOTAL | [G17] 📐 `=SUM(G10:G16)` | [K17] 📐 `=4160+1440+1120+2880+4800+91680+4000` | [L17] 📐 `=K17/21`
**Linha 19:** [A19] SUPRAESTRUTURA - LAJE CUBETAS
**Linha 21:** [A21] Descrição | [B21] Parâmetro | [D21] Quantidade | [F21] Preço unitário | [G21] Valor total | [H21] Observação
**Linha 22:** [A22] Fabricação forma | [B22] 3 | [C22] Jogos | [D22] 📐 `=(D23/DADOS_INICIAIS!$E$15)*B22` | [E22] m² | [F22] 110 | [G22] 📐 `=F22*D22*1.1`
**Linha 23:** [A23] Montagem de forma | [B23] 1.1 | [C23] m² / AC | [D23] 📐 `=B23*SUM('Obra '!D21:D35)` | [E23] m² | [F23] 2.5 | [G23] 📐 `=F23*D23*1.1` | [H23] índice Passione 0,98
**Linha 24:** [A24] Escoramento | [C24] un / APT*NPT | [D24] 📐 `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25` | [E24] m² | [F24] 22 | [G24] 📐 `=F24*D24*1.1`
**Linha 25:** [A25] Cubetas | [B25] 25 | [C25] R$ / AC | [D25] 📐 `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25` | [E25] m² | [F25] 15 | [G25] 📐 `=F25*D25*1.1`
**Linha 26:** [A26] Concreto  | [B26] 0.23 | [C26] m³ / AC | [D26] 📐 `=1450-D13` | [E26] m³ | [F26] 📐 `=(535+45+(1.67*0.6))*1.05` | [G26] 📐 `=F26*D26*1.1` | [H26] ìndice passione 23
**Linha 27:** [A27] Armadura Convencional para Estrutura | [B27] 78 | [C27] kg / m³ | [D27] 📐 `=121000-D14` | [E27] kg | [F27] 7.62 | [G27] 📐 `=F27*D27*1.1` | [H27] ìndice passione 93
**Linha 28:** [A28] Mão de obra - estrutura em concreto armado | [B28] 290 | [C28] R$ / AC | [D28] 📐 `=DADOS_INICIAIS!$E$9` | [E28] m² | [F28] 📐 `=B28` | [G28] 📐 `=F28*D28*1.1`
**Linha 29:** [A29] Perfuração de vigas | [B29] 2300 | [C29] R$ / NP | [D29] 1 | [E29] vb | [F29] 📐 `=B29*DADOS_INICIAIS!$E$15` | [G29] 📐 `=F29*D29*1.1` | [H29] Coeficiente originário do Gran Torino (R$ 160,00/un)
**Linha 30:** [A30] TOTAL | [G30] 📐 `=SUM(G22:G29)`
**Linha 32:** [A32] SUPRAESTRUTURA - LAJE CUBETAS PROTENDIDAS
**Linha 34:** [A34] Descrição | [B34] Parâmetro | [D34] Quantidade | [F34] Preço unitário | [G34] Valor total | [H34] Observação
**Linha 35:** [A35] Fabricação forma | [B35] 3 | [C35] Jogos | [D35] 📐 `=(D36/DADOS_INICIAIS!$E$15)*B35` | [E35] m² | [F35] 110 | [G35] 📐 `=F35*D35*1.1`
**Linha 36:** [A36] Montagem de forma | [B36] 1.1 | [C36] m² / AC | [D36] 📐 `=B36*DADOS_INICIAIS!$E$9` | [E36] m² | [F36] 2.5 | [G36] 📐 `=F36*D36*1.1`
**Linha 37:** [A37] Escoramento | [C37] un / APT*NPT | [D37] 📐 `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25` | [E37] m² | [F37] 22 | [G37] 📐 `=F37*D37*1.1` | [I37] Custos connect executivo
**Linha 38:** [A38] Cubetas | [B38] 25 | [C38] R$ / AC | [D38] 📐 `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25` | [E38] m² | [F38] 15 | [G38] 📐 `=F38*D38*1.1` | [H38] 📐 `=ROUNDUP(DADOS_INICIAIS!E19*B35,0)` | [I38] Custos connect executivo
**Linha 39:** [A39] Protensão - lajes - materiais | [D39] 📐 `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25-48.02-23.98` | [E39] m² | [F39] 11.5 | [G39] 📐 `=F39*D39*1.1` | [I39] Custos connect executivo
**Linha 40:** [A40] Protensão - lajes - serviços | [D40] 📐 `=D39` | [E40] m² | [F40] 11.5 | [G40] 📐 `=F40*D40*1.1` | [I40] Custos connect executivo
**Linha 41:** [A41] Concreto  | [B41] 0.25 | [C41] m³ / AC | [D41] 📐 `=B41*DADOS_INICIAIS!$E$9` | [E41] m³ | [F41] 📐 `=(535+45+(1.67*0.6))*1.05` | [G41] 📐 `=F41*D41*1.1`
**Linha 42:** [A42] Armadura Convencional para Estrutura | [B42] 100 | [C42] kg / m³ | [D42] 📐 `=D41*B42` | [E42] kg | [F42] 7.62 | [G42] 📐 `=F42*D42*1.1`
**Linha 43:** [A43] Mão de obra - estrutura em concreto armado | [B43] 280 | [C43] R$ / AC | [D43] 📐 `=DADOS_INICIAIS!$E$9` | [E43] m² | [F43] 📐 `=B43` | [G43] 📐 `=F43*D43*1.1`
**Linha 44:** [A44] Perfuração de vigas | [B44] 2300 | [C44] R$ / NP | [D44] 1 | [E44] vb | [F44] 📐 `=B44*DADOS_INICIAIS!$E$15` | [G44] 📐 `=F44*D44*1.1` | [H44] Coeficiente originário do Gran Torino (R$ 160,00/un)
**Linha 45:** [A45] TOTAL | [G45] 📐 `=SUM(G35:G44)`
**Linha 47:** [A47] SUPRAESTRUTURA - LAJE TRELIÇADA
**Linha 49:** [A49] Descrição | [B49] Parâmetro | [D49] Quantidade | [F49] Preço unitário | [G49] Valor total | [H49] Observação
**Linha 50:** [A50] Fabricação forma | [B50] 2 | [C50] Jogos | [D50] 📐 `=(D51/DADOS_INICIAIS!$E$15)*B50` | [E50] m² | [F50] 85 | [G50] 📐 `=F50*D50*1.1`
**Linha 51:** [A51] Montagem de forma | [B51] 2.1 | [C51] m² / AC | [D51] 📐 `=B51*DADOS_INICIAIS!E38` | [E51] m² | [F51] 1.5 | [G51] 📐 `=F51*D51*1.1`
**Linha 52:** [A52] Escoramento - Torre | [B52] 2 | [C52] un / APT*NPT | [D52] 📐 `=B52*DADOS_INICIAIS!E47*DADOS_INICIAIS!E44` | [E52] un | [F52] 17 | [G52] 📐 `=F52*D52*1.1`
**Linha 53:** [A53] Escoramento - Embasamento | [B53] 2 | [C53] un / AE | [D53] 📐 `=B53*DADOS_INICIAIS!E50` | [E53] un | [F53] 17 | [G53] 📐 `=F53*D53*1.1`
**Linha 54:** [A54] Cubetas | [B54] 25 | [C54] R$ / AC | [D54] 📐 `=B54*DADOS_INICIAIS!E38` | [E54] m³ | [F54] 📐 `=B54` | [G54] 📐 `=F54*D54*1.1`
**Linha 55:** [A55] Concreto  | [B55] 0.25 | [C55] m³ / AC | [D55] 📐 `=B55*DADOS_INICIAIS!E38` | [E55] m³ | [F55] 📐 `=575` | [G55] 📐 `=F55*D55*1.05*1.1`
**Linha 56:** [A56] Armadura Convencional para Estrutura | [B56] 110 | [C56] kg / m³ | [D56] 📐 `=D55*B56` | [E56] kg | [F56] 7.25 | [G56] 📐 `=F56*D56*1.1`
**Linha 57:** [A57] Mão de obra - estrutura em concreto armado | [B57] 240 | [C57] R$ / AC | [D57] 📐 `=DADOS_INICIAIS!E38` | [E57] m² | [F57] 📐 `=B57` | [G57] 📐 `=F57*D57*1.1`
**Linha 58:** [A58] Perfuração de vigas | [B58] 5300 | [C58] R$ / NP | [D58] 1 | [E58] vb | [F58] 📐 `=B58*DADOS_INICIAIS!E43` | [G58] 📐 `=F58*D58*1.1` | [H58] Coeficiente originário do Gran Torino (R$ 160,00/un)
**Linha 59:** [A59] TOTAL | [G59] 📐 `=SUM(G50:G58)`
**Linha 61:** [A61] SUPRAESTRUTURA - LAJE PROTENDIDA
**Linha 63:** [A63] Descrição | [B63] Parâmetro | [D63] Quantidade | [F63] Preço unitário | [G63] Valor total | [H63] Observação
**Linha 64:** [A64] Fabricação forma | [B64] 3 | [C64] Jogos | [D64] 📐 `=(D65/DADOS_INICIAIS!$E$15)*B64` | [E64] m² | [F64] 110 | [G64] 📐 `=F64*D64*1.1`
**Linha 65:** [A65] Montagem de forma | [B65] 2.1 | [C65] m² / AC | [D65] 📐 `=B65*DADOS_INICIAIS!$E$9` | [E65] m² | [F65] 2.5 | [G65] 📐 `=F65*D65*1.1`
**Linha 66:** [A66] Escoramento | [B66] 3 | [C66] un / AE | [D66] 📐 `=ROUNDUP(B66*DADOS_INICIAIS!$E$25*B64,0)` | [E66] un | [F66] 17 | [G66] 📐 `=F66*D66*1.1`
**Linha 67:** [A67] Protensão - lajes - materiais | [B67] 12.3 | [C67] RS / m² | [D67] 📐 `=(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17)*DADOS_INICIAIS!$E$19+DADOS_INICIAIS!$E$22` | [E67] m² | [F67] 📐 `=B67` | [G67] 📐 `=F67*D67*1.1`
**Linha 68:** [A68] Protensão - lajes - cabos | [B68] 2.83 | [C68] kg / m² | [D68] 📐 `=B68*D67` | [E68] kg | [F68] 12.3 | [G68] 📐 `=F68*D68*1.1`
**Linha 69:** [A69] Protensão - lajes - serviços | [B69] 9000 | [C69] und / pav | [D69] 📐 `=DADOS_INICIAIS!E15` | [E69] pav | [F69] 📐 `=B69` | [G69] 📐 `=F69*D69*1.1`
**Linha 70:** [A70] Concreto  | [B70] 0.25 | [C70] m³ / AC | [D70] 📐 `=B70*DADOS_INICIAIS!$E$9` | [E70] m³ | [F70] 📐 `=535+45` | [G70] 📐 `=F70*D70*1.05*1.1`
**Linha 71:** [A71] Armadura Convencional para Estrutura | [B71] 90 | [C71] kg / m³ | [D71] 📐 `=D70*B71` | [E71] kg | [F71] 7.62 | [G71] 📐 `=F71*D71*1.1`
**Linha 72:** [A72] Mão de obra - estrutura em concreto armado | [B72] 240 | [C72] R$ / AC | [D72] 📐 `=DADOS_INICIAIS!$E$9` | [E72] m² | [F72] 📐 `=B72` | [G72] 📐 `=F72*D72*1.1`
**Linha 73:** [A73] Perfuração de vigas | [B73] 5300 | [C73] R$ / NP | [D73] 1 | [E73] vb | [F73] 📐 `=B73*DADOS_INICIAIS!$E$15` | [G73] 📐 `=F73*D73*1.1` | [H73] Coeficiente originário do Gran Torino (R$ 160,00/un)
**Linha 74:** [A74] TOTAL | [G74] 📐 `=SUM(G64:G73)`
**Linha 77:** [A77] TOTAL SUPRAESTRUTURA | [G77] 📐 `=G30+G17` | [H77] 📐 `=G77/DADOS_INICIAIS!E9`
**Linha 79:** [H79] 📐 `=H77/1.1`

## Fórmulas Extraídas

- `D10`: `=(D11/1)*B10`
- `G10`: `=F10*D10*1.1`
- `D11`: `=B11*'Obra '!D36`
- `G11`: `=F11*D11*1.1`
- `F12`: `=17`
- `G12`: `=F12*D12*1.1`
- `D13`: `=B13*'Obra '!D36`
- `F13`: `=535+45`
- `G13`: `=F13*D13*1.05*1.1`
- `D14`: `=D13*B14`
- `G14`: `=F14*D14*1.1`
- `F15`: `=B15`
- `G15`: `=F15*D15*1.1`
- `F16`: `=B16*DADOS_INICIAIS!$E$15`
- `G16`: `=F16*D16*1.1`
- `G17`: `=SUM(G10:G16)`
- `K17`: `=4160+1440+1120+2880+4800+91680+4000`
- `L17`: `=K17/21`
- `D22`: `=(D23/DADOS_INICIAIS!$E$15)*B22`
- `G22`: `=F22*D22*1.1`
- `D23`: `=B23*SUM('Obra '!D21:D35)`
- `G23`: `=F23*D23*1.1`
- `D24`: `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25`
- `G24`: `=F24*D24*1.1`
- `D25`: `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25`
- `G25`: `=F25*D25*1.1`
- `D26`: `=1450-D13`
- `F26`: `=(535+45+(1.67*0.6))*1.05`
- `G26`: `=F26*D26*1.1`
- `D27`: `=121000-D14`
- `G27`: `=F27*D27*1.1`
- `D28`: `=DADOS_INICIAIS!$E$9`
- `F28`: `=B28`
- `G28`: `=F28*D28*1.1`
- `F29`: `=B29*DADOS_INICIAIS!$E$15`
- `G29`: `=F29*D29*1.1`
- `G30`: `=SUM(G22:G29)`
- `D35`: `=(D36/DADOS_INICIAIS!$E$15)*B35`
- `G35`: `=F35*D35*1.1`
- `D36`: `=B36*DADOS_INICIAIS!$E$9`
- `G36`: `=F36*D36*1.1`
- `D37`: `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25`
- `G37`: `=F37*D37*1.1`
- `D38`: `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25`
- `G38`: `=F38*D38*1.1`
- `H38`: `=ROUNDUP(DADOS_INICIAIS!E19*B35,0)`
- `D39`: `=DADOS_INICIAIS!$E$9-DADOS_INICIAIS!$E$25-48.02-23.98`
- `G39`: `=F39*D39*1.1`
- `D40`: `=D39`
- `G40`: `=F40*D40*1.1`
- `D41`: `=B41*DADOS_INICIAIS!$E$9`
- `F41`: `=(535+45+(1.67*0.6))*1.05`
- `G41`: `=F41*D41*1.1`
- `D42`: `=D41*B42`
- `G42`: `=F42*D42*1.1`
- `D43`: `=DADOS_INICIAIS!$E$9`
- `F43`: `=B43`
- `G43`: `=F43*D43*1.1`
- `F44`: `=B44*DADOS_INICIAIS!$E$15`
- `G44`: `=F44*D44*1.1`
- `G45`: `=SUM(G35:G44)`
- `D50`: `=(D51/DADOS_INICIAIS!$E$15)*B50`
- `G50`: `=F50*D50*1.1`
- `D51`: `=B51*DADOS_INICIAIS!E38`
- `G51`: `=F51*D51*1.1`
- `D52`: `=B52*DADOS_INICIAIS!E47*DADOS_INICIAIS!E44`
- `G52`: `=F52*D52*1.1`
- `D53`: `=B53*DADOS_INICIAIS!E50`
- `G53`: `=F53*D53*1.1`
- `D54`: `=B54*DADOS_INICIAIS!E38`
- `F54`: `=B54`
- `G54`: `=F54*D54*1.1`
- `D55`: `=B55*DADOS_INICIAIS!E38`
- `F55`: `=575`
- `G55`: `=F55*D55*1.05*1.1`
- `D56`: `=D55*B56`
- `G56`: `=F56*D56*1.1`
- `D57`: `=DADOS_INICIAIS!E38`
- `F57`: `=B57`
- `G57`: `=F57*D57*1.1`
- `F58`: `=B58*DADOS_INICIAIS!E43`
- `G58`: `=F58*D58*1.1`
- `G59`: `=SUM(G50:G58)`
- `D64`: `=(D65/DADOS_INICIAIS!$E$15)*B64`
- `G64`: `=F64*D64*1.1`
- `D65`: `=B65*DADOS_INICIAIS!$E$9`
- `G65`: `=F65*D65*1.1`
- `D66`: `=ROUNDUP(B66*DADOS_INICIAIS!$E$25*B64,0)`
- `G66`: `=F66*D66*1.1`
- `D67`: `=(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17)*DADOS_INICIAIS!$E$19+DADOS_INICIAIS!$E$22`
- `F67`: `=B67`
- `G67`: `=F67*D67*1.1`
- `D68`: `=B68*D67`
- `G68`: `=F68*D68*1.1`
- `D69`: `=DADOS_INICIAIS!E15`
- `F69`: `=B69`
- `G69`: `=F69*D69*1.1`
- `D70`: `=B70*DADOS_INICIAIS!$E$9`
- `F70`: `=535+45`
- `G70`: `=F70*D70*1.05*1.1`
- `D71`: `=D70*B71`
- `G71`: `=F71*D71*1.1`
- `D72`: `=DADOS_INICIAIS!$E$9`
- `F72`: `=B72`
- `G72`: `=F72*D72*1.1`
- `F73`: `=B73*DADOS_INICIAIS!$E$15`
- `G73`: `=F73*D73*1.1`
- `G74`: `=SUM(G64:G73)`
- `G77`: `=G30+G17`
- `H77`: `=G77/DADOS_INICIAIS!E9`
- `H79`: `=H77/1.1`