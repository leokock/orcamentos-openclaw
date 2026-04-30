# Aba: ESQUADRIAS
Dimensão: A1:L46 | Linhas: 46 | Colunas: 12

## Conteúdo Completo

### Células Mescladas: 5
  - A3:H3
  - B9:C9
  - A22:F22
  - A20:F20
  - D9:E9

**Linha 3:** [A3] ESQUADRIAS
**Linha 4:** [A4] Data | [B4] 2024-06-17 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] ESQUADRIAS
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Esquadrias de Alumínio | [B10] 0.15 | [C10]  m² / AC | [D10] 📐 `=B10*DADOS_INICIAIS!E9` | [E10] m² | [F10] 1250 | [G10] 📐 `=F10*D10*1.1` | [H10] 📐 `=G10/DADOS_INICIAIS!E9` | [I10] *Médias do BySeasons e Colin
**Linha 11:** [A11] Pele de vidro | [D11] 📐 `=D46` | [E11] m² | [F11] 1050 | [G11] 📐 `=F11*D11*1.1` | [H11] lojas
**Linha 12:** [A12] Portão de alumínio | [D12] 1 | [E12] un | [F12] 16000 | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Guarda-corpo - vidro | [D13] 📐 `=C46` | [E13] m | [F13] 📐 `=750*1.1` | [G13] 📐 `=F13*D13*1.1`
**Linha 14:** [A14] Gradil  | [E14] m² | [F14] 610 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] Serralherias | [B15] 5 | [C15] R$ / AC | [D15] 1 | [E15] vb | [F15] 📐 `=B15*DADOS_INICIAIS!$E$9` | [G15] 📐 `=F15*D15*1.1`
**Linha 16:** [A16] PCF | [D16] 📐 `=2*DADOS_INICIAIS!E15` | [E16] un | [F16] 1750 | [G16] 📐 `=F16*D16*1.1`
**Linha 17:** [A17] Corrimão madeira | [D17] 📐 `=(11*DADOS_INICIAIS!E15)` | [E17] m | [F17] 85 | [G17] 📐 `=F17*D17*1.1`
**Linha 18:** [A18] Fechadura Biometrica | [D18] 📐 `=DADOS_INICIAIS!E10*0` | [E18] un | [F18] 1500 | [G18] 📐 `=F18*D18*1.1`
**Linha 19:** [A19] Esquadrias de Madeira | [D19] 📐 `=2+(6*DADOS_INICIAIS!E10)*0+(7+6*2+5)*10+7` | [E19] un | [F19] 2100 | [G19] 📐 `=F19*D19*1.1`
**Linha 20:** [A20] TOTAL | [G20] 📐 `=SUM(G10:G19)` | [K20] 📐 `=4160+1440+1120+2880+4800+91680+4000` | [L20] 📐 `=K20/21`
**Linha 22:** [A22] TOTAL ESQUADRIAS | [G22] 📐 `=G20` | [H22] 📐 `=G22/DADOS_INICIAIS!E9`
**Linha 27:** [B27] Pavimento | [C27] Guarda corpo | [D27] Pele de Vidro
**Linha 28:** [B28] 1º PAV-TÉRREO | [D28] 📐 `=13.4*4.5`
**Linha 29:** [B29] 2º PAV. - GARAGEM | [D29] 📐 `=13.4*3`
**Linha 30:** [B30] 3º PAV. - GARAGEM
**Linha 31:** [B31] 4º PAV. - GARAGEM
**Linha 32:** [B32] 5º PAV. - TIPO DIF | [C32] 📐 `=13.49+2.74+3.14`
**Linha 33:** [B33] 6º PAV. - TIPO 01 | [C33] 📐 `=3.59+3.44+3.7*2`
**Linha 34:** [B34] 7º PAV. - TIPO 02 | [C34] 📐 `=3.59+3.44+3.7*2`
**Linha 35:** [B35] 8º PAV. - TIPO 03 | [C35] 📐 `=3.59+3.44+3.7*2`
**Linha 36:** [B36] 9º PAV. - TIPO 04 | [C36] 📐 `=3.59+3.44+3.7*2`
**Linha 37:** [B37] 10º PAV. - TIPO 05 | [C37] 📐 `=3.59+3.44+3.7*2`
**Linha 38:** [B38] 11º PAV. - TIPO 06 | [C38] 📐 `=3.59+3.44+3.7*2`
**Linha 39:** [B39] 12º PAV. - TIPO 07 | [C39] 📐 `=3.59+3.44+3.7*2`
**Linha 40:** [B40] 13º PAV. - TIPO 08 | [C40] 📐 `=3.59+3.44+3.7*2`
**Linha 41:** [B41] 11º PAV. - TIPO 09 | [C41] 📐 `=3.59+3.44+3.7*2`
**Linha 42:** [B42] 15º PAV. - TIPO 10 | [C42] 📐 `=3.59+3.44+3.7*2`
**Linha 43:** [B43] 16º PAV. - TIPO 11 - LAZER | [C43] 📐 `=18.42+6.74`
**Linha 44:** [B44] CASA DE MÁQUINAS
**Linha 45:** [B45] RESERVATÓRIO
**Linha 46:** [B46] Total | [C46] 📐 `=SUM(C28:C45)` | [D46] 📐 `=SUM(D28:D45)`

## Fórmulas Extraídas

- `D10`: `=B10*DADOS_INICIAIS!E9`
- `G10`: `=F10*D10*1.1`
- `H10`: `=G10/DADOS_INICIAIS!E9`
- `D11`: `=D46`
- `G11`: `=F11*D11*1.1`
- `G12`: `=F12*D12*1.1`
- `D13`: `=C46`
- `F13`: `=750*1.1`
- `G13`: `=F13*D13*1.1`
- `G14`: `=F14*D14*1.1`
- `F15`: `=B15*DADOS_INICIAIS!$E$9`
- `G15`: `=F15*D15*1.1`
- `D16`: `=2*DADOS_INICIAIS!E15`
- `G16`: `=F16*D16*1.1`
- `D17`: `=(11*DADOS_INICIAIS!E15)`
- `G17`: `=F17*D17*1.1`
- `D18`: `=DADOS_INICIAIS!E10*0`
- `G18`: `=F18*D18*1.1`
- `D19`: `=2+(6*DADOS_INICIAIS!E10)*0+(7+6*2+5)*10+7`
- `G19`: `=F19*D19*1.1`
- `G20`: `=SUM(G10:G19)`
- `K20`: `=4160+1440+1120+2880+4800+91680+4000`
- `L20`: `=K20/21`
- `G22`: `=G20`
- `H22`: `=G22/DADOS_INICIAIS!E9`
- `D28`: `=13.4*4.5`
- `D29`: `=13.4*3`
- `C32`: `=13.49+2.74+3.14`
- `C33`: `=3.59+3.44+3.7*2`
- `C34`: `=3.59+3.44+3.7*2`
- `C35`: `=3.59+3.44+3.7*2`
- `C36`: `=3.59+3.44+3.7*2`
- `C37`: `=3.59+3.44+3.7*2`
- `C38`: `=3.59+3.44+3.7*2`
- `C39`: `=3.59+3.44+3.7*2`
- `C40`: `=3.59+3.44+3.7*2`
- `C41`: `=3.59+3.44+3.7*2`
- `C42`: `=3.59+3.44+3.7*2`
- `C43`: `=18.42+6.74`
- `C46`: `=SUM(C28:C45)`
- `D46`: `=SUM(D28:D45)`