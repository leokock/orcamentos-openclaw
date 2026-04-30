# Aba: COBERTURA
Dimensão: A1:J15 | Linhas: 15 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 6
  - D8:E8
  - A13:C13
  - A14:C14
  - A2:H2
  - A15:C15
  - B8:C8

**Linha 2:** [A2] COBERTURA
**Linha 3:** [A3] Data | [B3] 2024-06-17 00:00:00
**Linha 4:** [A4] Arquivo base | [B4] -
**Linha 6:** [A6] TELHADO
**Linha 8:** [A8] Descrição | [B8] Parâmetro | [D8] Quantidade | [F8] Preço unitário | [G8] Valor total | [H8] Observação
**Linha 9:** [A9] Estrutura e telhamento | [D9] 0 | [E9] m² | [F9] 55 | [G9] 📐 `=F9*D9*1.1`
**Linha 10:** [A10] Serviços complementares | [D10] 📐 `=D9` | [E10] m² | [F10] 45 | [G10] 📐 `=F10*D10*1.1`
**Linha 11:** [A11] Pergolados | [G11] 📐 `=F11*D11*1.1`
**Linha 12:** [A12] Passarelas | [G12] 📐 `=F12*D12*1.1`
**Linha 13:** [A13] TOTAL | [G13] 📐 `=SUM(G9:G12)`
**Linha 15:** [A15] TOTAL COMPLEMENTARES | [G15] 📐 `=G13` | [H15] 📐 `=G15/DADOS_INICIAIS!$E$9`

## Fórmulas Extraídas

- `G9`: `=F9*D9*1.1`
- `D10`: `=D9`
- `G10`: `=F10*D10*1.1`
- `G11`: `=F11*D11*1.1`
- `G12`: `=F12*D12*1.1`
- `G13`: `=SUM(G9:G12)`
- `G15`: `=G13`
- `H15`: `=G15/DADOS_INICIAIS!$E$9`