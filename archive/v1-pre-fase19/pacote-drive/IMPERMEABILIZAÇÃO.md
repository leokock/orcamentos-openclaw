# Aba: IMPERMEABILIZAÇÃO
Dimensão: A1:L23 | Linhas: 23 | Colunas: 12

## Conteúdo Completo

### Células Mescladas: 5
  - A3:H3
  - A20:F20
  - A18:F18
  - B9:C9
  - D9:E9

**Linha 3:** [A3] IMPERMEABILIZAÇÃO
**Linha 4:** [A4] Data | [B4] 2024-06-28 00:00:00
**Linha 5:** [A5] Arquivo base | [B5] -
**Linha 7:** [A7] ALVENARIA
**Linha 9:** [A9] Descrição | [B9] Parâmetro | [D9] Quantidade | [F9] Preço unitário | [G9] Valor total | [H9] Observação
**Linha 10:** [A10] Regularização de Superfície | [B10] 25 | [C10] R$ / m² | [D10] 📐 `=D14+D15` | [E10] m² | [F10] 22 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Poço do elevador | [B11] 45 | [C11] R$ / m² | [D11] 📐 `=(3.24+(7.2)*1.8)*2` | [E11] m² | [F11] 41 | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Baldrames | [B12] 30 | [C12] R$ / m² | [D12] 📐 `=INFRAESTRUTURA!D28` | [E12] m² | [F12] 35 | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] Ralos | [B13] 1 | [C13] R$ / AC | [D13] 📐 `=SUM('Obra '!N21:N39)` | [E13] vb | [F13] 56 | [G13] 📐 `=F13*D13*1.1`
**Linha 14:** [A14] Impermeabilizações cimenticias | [B14] 0.25 | [C14] m² / AC | [D14] 📐 `=B14*DADOS_INICIAIS!E9` | [E14] m² | [F14] 60 | [G14] 📐 `=F14*D14*1.1`
**Linha 15:** [A15] Impermeabilizações com manta asfaltica | [B15] 0.11 | [C15] m² / AC | [D15] 📐 `=B15*DADOS_INICIAIS!E9` | [E15] m² | [F15] 110 | [G15] 📐 `=F15*D15*1.1`
**Linha 16:** [A16] Impermeabilização de peitoril | [B16] 0.6 | [C16] R$ / AC | [D16] 1 | [E16] vb | [F16] 📐 `=B16*DADOS_INICIAIS!$E$9` | [G16] 📐 `=F16*D16*1.1`
**Linha 17:** [A17] Proteção Mecânica | [B17] 28 | [C17] R$ / m² | [D17] 📐 `=D15` | [E17] m² | [F17] 28 | [G17] 📐 `=F17*D17*1.1`
**Linha 18:** [A18] TOTAL | [G18] 📐 `=SUM(G10:G17)` | [K18] 📐 `=4160+1440+1120+2880+4800+91680+4000` | [L18] 📐 `=K18/21`
**Linha 20:** [A20] TOTAL IMPERMEABILIZAÇÃO | [G20] 📐 `=G18` | [H20] 📐 `=G20/DADOS_INICIAIS!E9`
**Linha 23:** [H23] 📐 `=H20/1.1`

## Fórmulas Extraídas

- `D10`: `=D14+D15`
- `G10`: `=F10*D10*1.1`
- `D11`: `=(3.24+(7.2)*1.8)*2`
- `G11`: `=F11*D11*1.1`
- `D12`: `=INFRAESTRUTURA!D28`
- `G12`: `=F12*D12*1.1`
- `D13`: `=SUM('Obra '!N21:N39)`
- `G13`: `=F13*D13*1.1`
- `D14`: `=B14*DADOS_INICIAIS!E9`
- `G14`: `=F14*D14*1.1`
- `D15`: `=B15*DADOS_INICIAIS!E9`
- `G15`: `=F15*D15*1.1`
- `F16`: `=B16*DADOS_INICIAIS!$E$9`
- `G16`: `=F16*D16*1.1`
- `D17`: `=D15`
- `G17`: `=F17*D17*1.1`
- `G18`: `=SUM(G10:G17)`
- `K18`: `=4160+1440+1120+2880+4800+91680+4000`
- `L18`: `=K18/21`
- `G20`: `=G18`
- `H20`: `=G20/DADOS_INICIAIS!E9`
- `H23`: `=H20/1.1`