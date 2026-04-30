# Aba: TETO
Dimensão: A1:L20 | Linhas: 20 | Colunas: 12

## Conteúdo Completo

### Células Mescladas: 5
  - A3:H3
  - A17:F17
  - B9:C9
  - D9:E9
  - A15:F15

**Linha 3:** [A3] REVESTIMENTOS E ACABAMENTOS DE TETO
**Linha 4:** [A4] Data | [B4] 2024-06-28 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] ALVENARIA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Forro gesso Acartonado ST | [B10] 0.6 | [C10] m² / AC | [D10] 📐 `=B10*DADOS_INICIAIS!E9*0.8` | [E10] m² | [F10] 105 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Forro gesso Acartonado RU | [B11] 0.6 | [C11] m² / AC | [D11] 📐 `=B11*DADOS_INICIAIS!E9*0.2` | [E11] m² | [F11] 125 | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Forro gesso mineral | [B12] 0.6 | [C12] m² / AC | [D12] 📐 `=B12*DADOS_INICIAIS!E9*0` | [E12] m² | [F12] 65 | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Negativo | [B13] 1.2 | [C13] m / FORRO | [D13] 📐 `=(D12)*B13` | [E13] m² | [F13] 22 | [G13] 📐 `=F13*D13*1.1`
**Linha 14:** [A14] Estucamento | [B14] 0.2 | [C14] m² / AC | [D14] 📐 `=(556.79-(11.99+4.57+1.7*2+2.56*2+5.47))*3+527.99-(11.99+4.57+1.69*2+5.47+2.56*2)` | [E14] m² | [F14] 24 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] TOTAL | [G15] 📐 `=SUM(G10:G14)` | [K15] 📐 `=4160+1440+1120+2880+4800+91680+4000` | [L15] 📐 `=K15/21`
**Linha 17:** [A17] TOTAL FORRO | [G17] 📐 `=G15` | [H17] 📐 `=G17/DADOS_INICIAIS!E9`
**Linha 20:** [H20] 📐 `=H17/1.1`

## Fórmulas Extraídas

- `D10`: `=B10*DADOS_INICIAIS!E9*0.8`
- `G10`: `=F10*D10*1.1`
- `D11`: `=B11*DADOS_INICIAIS!E9*0.2`
- `G11`: `=F11*D11*1.1`
- `D12`: `=B12*DADOS_INICIAIS!E9*0`
- `G12`: `=F12*D12*1.1`
- `D13`: `=(D12)*B13`
- `G13`: `=F13*D13*1.1`
- `D14`: `=(556.79-(11.99+4.57+1.7*2+2.56*2+5.47))*3+527.99-(11.99+4.57+1.69*2+5.47+2.56*2)`
- `G14`: `=F14*D14*1.1`
- `G15`: `=SUM(G10:G14)`
- `K15`: `=4160+1440+1120+2880+4800+91680+4000`
- `L15`: `=K15/21`
- `G17`: `=G15`
- `H17`: `=G17/DADOS_INICIAIS!E9`
- `H20`: `=H17/1.1`