# Aba: COMPLEMENTARES
Dimensão: A1:J17 | Linhas: 17 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 6
  - D8:E8
  - A17:C17
  - A2:G2
  - A15:C15
  - B8:C8
  - A16:C16

**Linha 2:** [A2] COMPLEMENTARES
**Linha 3:** [A3] Data | [B3] 2024-06-17 00:00:00
**Linha 4:** [A4] Arquivo base | [B4] -
**Linha 6:** [A6] SERVIÇOS COMPLEMENTARES
**Linha 8:** [A8] Descrição | [B8] Parâmetro | [D8] Quantidade | [F8] Valor total
**Linha 9:** [A9] Móveis e decoração | [B9] 1500 | [C9] R$ / AL | [D9] 📐 `=DADOS_INICIAIS!E21` | [E9] m² | [F9] 📐 `=D9*B9*1.1`
**Linha 10:** [A10] Comunicação visual | [B10] 10 | [C10] R$ / AC | [D10] 📐 `=B10*DADOS_INICIAIS!$E$9` | [E10] vb | [F10] 📐 `=D10*1.1`
**Linha 11:** [A11] Paisagismo | [B11] 11 | [C11] R$ / AC | [D11] 📐 `=B11*DADOS_INICIAIS!$E$9` | [E11] vb | [F11] 📐 `=D11*1.1`
**Linha 12:** [A12] Ligações definitivas | [B12] 4 | [C12] R$ / AC | [D12] 📐 `=B12*DADOS_INICIAIS!$E$9` | [E12] vb | [F12] 📐 `=D12*1.1`
**Linha 13:** [A13] Desmobilização | [B13] 5 | [C13] R$ / AC | [D13] 📐 `=B13*DADOS_INICIAIS!$E$9` | [E13] vb | [F13] 📐 `=D13*1.1`
**Linha 14:** [A14] Limpeza | [B14] 15 | [C14] R$ / AC | [D14] 📐 `=B14*DADOS_INICIAIS!$E$9` | [E14] vb | [F14] 📐 `=D14*1.1`
**Linha 15:** [A15] TOTAL | [F15] 📐 `=SUM(F9:F14)`
**Linha 17:** [A17] TOTAL COMPLEMENTARES | [F17] 📐 `=F15` | [G17] 📐 `=F17/DADOS_INICIAIS!$E$9`

## Fórmulas Extraídas

- `D9`: `=DADOS_INICIAIS!E21`
- `F9`: `=D9*B9*1.1`
- `D10`: `=B10*DADOS_INICIAIS!$E$9`
- `F10`: `=D10*1.1`
- `D11`: `=B11*DADOS_INICIAIS!$E$9`
- `F11`: `=D11*1.1`
- `D12`: `=B12*DADOS_INICIAIS!$E$9`
- `F12`: `=D12*1.1`
- `D13`: `=B13*DADOS_INICIAIS!$E$9`
- `F13`: `=D13*1.1`
- `D14`: `=B14*DADOS_INICIAIS!$E$9`
- `F14`: `=D14*1.1`
- `F15`: `=SUM(F9:F14)`
- `F17`: `=F15`
- `G17`: `=F17/DADOS_INICIAIS!$E$9`