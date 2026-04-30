# Aba: PINTURA INTERNA
Dimensão: A1:L18 | Linhas: 18 | Colunas: 12

## Conteúdo Completo

### Células Mescladas: 5
  - A16:F16
  - A3:H3
  - A14:F14
  - B9:C9
  - D9:E9

**Linha 3:** [A3] PINTURA INTERNA
**Linha 4:** [A4] Data | [B4] 2024-06-14 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] ALVENARIA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Pintura piso epoxi | [B10] 110 | [C10] R$ / m² | [D10] 📐 `='Rev. Internos Piso e Parede'!B15` | [E10] m² | [F10] 110 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Pintura acrílica antiderrapante | [B11] 65 | [C11] R$ / m² | [D11] 📐 `='Rev. Internos Piso e Parede'!B16` | [E11] m² | [F11] 65 | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Textura escadas  | [B12] 25 | [C12] R$ / AC | [D12] 1 | [E12] vb | [F12] 📐 `=B12*DADOS_INICIAIS!$E$9` | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Pintura Interna | [B13] 75 | [C13] R$ / AC | [D13] 1 | [E13] vb | [F13] 📐 `=B13*DADOS_INICIAIS!$E$9` | [G13] 📐 `=F13*D13*1.1`
**Linha 14:** [A14] TOTAL | [G14] 📐 `=SUM(G10:G13)` | [K14] 📐 `=4160+1440+1120+2880+4800+91680+4000` | [L14] 📐 `=K14/21`
**Linha 16:** [A16] TOTAL IMPERMEABILIZAÇÃO | [G16] 📐 `=G14` | [H16] 📐 `=G16/DADOS_INICIAIS!E9`
**Linha 18:** [H18] 📐 `=H16/1.1`

## Fórmulas Extraídas

- `D10`: `='Rev. Internos Piso e Parede'!B15`
- `G10`: `=F10*D10*1.1`
- `D11`: `='Rev. Internos Piso e Parede'!B16`
- `G11`: `=F11*D11*1.1`
- `F12`: `=B12*DADOS_INICIAIS!$E$9`
- `G12`: `=F12*D12*1.1`
- `F13`: `=B13*DADOS_INICIAIS!$E$9`
- `G13`: `=F13*D13*1.1`
- `G14`: `=SUM(G10:G13)`
- `K14`: `=4160+1440+1120+2880+4800+91680+4000`
- `L14`: `=K14/21`
- `G16`: `=G14`
- `H16`: `=G16/DADOS_INICIAIS!E9`
- `H18`: `=H16/1.1`