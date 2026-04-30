# Aba: ALVENARIA
Dimensão: A1:J36 | Linhas: 36 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 8
  - A33:F33
  - A16:F16
  - A3:H3
  - D20:E20
  - B20:C20
  - B9:C9
  - A30:F30
  - D9:E9

**Linha 3:** [A3] PAREDES E PAINÉIS
**Linha 4:** [A4] Data | [B4] 2024-06-26 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] ALVENARIA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Alvenaria externa | [B10] 0.6 | [C10] m² / AE | [D10] 📐 `=B10*DADOS_INICIAIS!$E$9` | [E10] m² | [F10] 45 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Alvenaria internas | [B11] 0.8 | [C11] m² / AL | [D11] 📐 `=B11*DADOS_INICIAIS!$E$9` | [E11] m² | [F11] 45 | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Alvenaria escadas  | [B12] 0.18 | [C12] m² / AC | [D12] 📐 `=B12*DADOS_INICIAIS!$E$9` | [E12] m² | [F12] 75 | [G12] 📐 `=F12*D12*1.05*1.1`
**Linha 13:** [A13] Alvenaria refratárias | [B13] 1.75 | [C13] m² * CHU | [D13] 📐 `=B13*DADOS_INICIAIS!$E$14` | [E13] m² | [F13] 310 | [G13] 📐 `=F13*D13*1.1`
**Linha 14:** [A14] Serviços complementares | [B14] 12.5 | [C14] R$ / m² | [D14] 📐 `=SUM(D10:D12)` | [E14] m² | [F14] 6.5 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] Mão de obra | [C15] R$ / m² | [D15] 📐 `=SUM(D10:D12)` | [E15] m² | [F15] 48 | [G15] 📐 `=F15*D15*1.1`
**Linha 16:** [A16] TOTAL | [G16] 📐 `=SUM(G10:G15)`
**Linha 18:** [A18] ALVENARIA - DRYWALL
**Linha 20:** [A20] Descrição | [B20] Parâmetro | [D20] Quantidade | [F20] Preço unitário | [G20] Valor total | [H20] Observação
**Linha 21:** [A21] Alvenaria embasamento | [B21] 1 | [C21] m² / AE | [D21] 📐 `=B21*DADOS_INICIAIS!$E$22` | [E21] m² | [F21] 45 | [G21] 📐 `=F21*D21*1.1`
**Linha 22:** [A22] Alvenaria lazer | [B22] 0.4 | [C22] m² / AL | [D22] 📐 `=B22*DADOS_INICIAIS!$E$21` | [E22] m² | [F22] 45 | [G22] 📐 `=F22*D22*1.1`
**Linha 23:** [A23] Alvenaria tipo | [B23] 1.65 | [C23] m² / APT*(NPT+2ND) | [D23] 📐 `=B23*(DADOS_INICIAIS!$E$19*(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17))*0.4` | [E23] m² | [F23] 45 | [G23] 📐 `=F23*D23*1.1`
**Linha 24:** [A24] Drywall tipo | [B24] 1.65 | [C24] m² / APT*(NPT+2ND) | [D24] 📐 `=B24*(DADOS_INICIAIS!$E$19*(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17))*0.6` | [E24] m² | [F24] 220 | [G24] 📐 `=F24*D24*1.1` | [J24] 📐 `=D24/(D28+D24)`
**Linha 25:** [A25] Alvenaria escadas  | [B25] 0.2 | [C25] m² / AC | [D25] 📐 `=B25*DADOS_INICIAIS!$E$9` | [E25] m² | [F25] 70 | [G25] 📐 `=F25*D25*1.1` | [J25] 📐 `=1-J24`
**Linha 26:** [A26] Alvenaria cobertura / reservatório | [B26] 0.8 | [C26] m² / APT | [D26] 📐 `=B26*DADOS_INICIAIS!$E$19` | [E26] m³ | [F26] 45 | [G26] 📐 `=F26*D26*1.1`
**Linha 27:** [A27] Alvenaria refratárias | [B27] 1.75 | [C27] m² * CHU | [D27] 📐 `='SISTEMAS ESPECIAIS'!B10` | [E27] un  | [F27] 210 | [G27] 📐 `=F27*D27*1.1`
**Linha 28:** [A28] Serviços complementares | [B28] 12.5 | [C28] R$ / m² | [D28] 📐 `=D22+D23+D21+D25+D26` | [E28] m² | [F28] 📐 `=B28` | [G28] 📐 `=F28*D28*1.1`
**Linha 29:** [A29] Mão de obra | [B29] 35 | [C29] R$ / m² | [D29] 📐 `=D22+D23+D21+D25+D26` | [E29] m² | [F29] 35 | [G29] 📐 `=F29*D29*1.1`
**Linha 30:** [A30] TOTAL | [G30] 📐 `=SUM(G21:G29)`
**Linha 33:** [A33] TOTAL ALVENARIA | [G33] 📐 `=G16` | [H33] 📐 `=G33/DADOS_INICIAIS!E9`
**Linha 35:** [D35] 📐 `=SUM(D10:D12)/'Obra '!C10`
**Linha 36:** [G36] 📐 `=G33/1.1` | [H36] 📐 `=G36/DADOS_INICIAIS!E9`

## Fórmulas Extraídas

- `D10`: `=B10*DADOS_INICIAIS!$E$9`
- `G10`: `=F10*D10*1.1`
- `D11`: `=B11*DADOS_INICIAIS!$E$9`
- `G11`: `=F11*D11*1.1`
- `D12`: `=B12*DADOS_INICIAIS!$E$9`
- `G12`: `=F12*D12*1.05*1.1`
- `D13`: `=B13*DADOS_INICIAIS!$E$14`
- `G13`: `=F13*D13*1.1`
- `D14`: `=SUM(D10:D12)`
- `G14`: `=F14*D14*1.1`
- `D15`: `=SUM(D10:D12)`
- `G15`: `=F15*D15*1.1`
- `G16`: `=SUM(G10:G15)`
- `D21`: `=B21*DADOS_INICIAIS!$E$22`
- `G21`: `=F21*D21*1.1`
- `D22`: `=B22*DADOS_INICIAIS!$E$21`
- `G22`: `=F22*D22*1.1`
- `D23`: `=B23*(DADOS_INICIAIS!$E$19*(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17))*0.4`
- `G23`: `=F23*D23*1.1`
- `D24`: `=B24*(DADOS_INICIAIS!$E$19*(DADOS_INICIAIS!$E$16+DADOS_INICIAIS!$E$17))*0.6`
- `G24`: `=F24*D24*1.1`
- `J24`: `=D24/(D28+D24)`
- `D25`: `=B25*DADOS_INICIAIS!$E$9`
- `G25`: `=F25*D25*1.1`
- `J25`: `=1-J24`
- `D26`: `=B26*DADOS_INICIAIS!$E$19`
- `G26`: `=F26*D26*1.1`
- `D27`: `='SISTEMAS ESPECIAIS'!B10`
- `G27`: `=F27*D27*1.1`
- `D28`: `=D22+D23+D21+D25+D26`
- `F28`: `=B28`
- `G28`: `=F28*D28*1.1`
- `D29`: `=D22+D23+D21+D25+D26`
- `G29`: `=F29*D29*1.1`
- `G30`: `=SUM(G21:G29)`
- `G33`: `=G16`
- `H33`: `=G33/DADOS_INICIAIS!E9`
- `D35`: `=SUM(D10:D12)/'Obra '!C10`
- `G36`: `=G33/1.1`
- `H36`: `=G36/DADOS_INICIAIS!E9`