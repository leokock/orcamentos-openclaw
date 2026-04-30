# Aba: INSTALAÇÕES
Dimensão: A1:I37 | Linhas: 37 | Colunas: 9

## Conteúdo Completo

### Células Mescladas: 10
  - A25:C25
  - B6:C6
  - A33:C33
  - B29:C29
  - A2:E2
  - A14:C14
  - A35:C35
  - A26:C26
  - B18:C18
  - A15:C15

**Linha 2:** [A2] INSTALAÇÕES
**Linha 4:** [A4] INSTALAÇÕES ELÉTRICAS
**Linha 6:** [A6] Descrição | [B6] Parâmetro | [D6] Valor total
**Linha 7:** [A7] Entrada de Energia | [B7] 5.5 | [C7] R$ / AC | [D7] 📐 `=B7*DADOS_INICIAIS!$E$9*1.1`
**Linha 8:** [A8] Eletrodutos e Eletrocalhas | [B8] 10 | [C8] R$ / AC | [D8] 📐 `=B8*DADOS_INICIAIS!$E$9*1.1`
**Linha 9:** [A9] Cabos e Fiações | [B9] 30 | [C9] R$ / AC | [D9] 📐 `=B9*DADOS_INICIAIS!$E$9*1.1`
**Linha 10:** [A10] Quadros e Disjuntores | [B10] 18 | [C10] R$ / AC | [D10] 📐 `=B10*DADOS_INICIAIS!$E$9*1.1`
**Linha 11:** [A11] Acabamentos Elétricos | [B11] 15 | [C11] R$ / AC | [D11] 📐 `=B11*DADOS_INICIAIS!$E$9*1.1`
**Linha 12:** [A12] Equipamentos e Iluminação | [B12] 15 | [C12] R$ / AC | [D12] 📐 `=B12*DADOS_INICIAIS!$E$9*1.1`
**Linha 13:** [A13] Mão de Obra para Instalações Elétricas | [B13] 60 | [C13] R$ / AC | [D13] 📐 `=B13*DADOS_INICIAIS!$E$9*1.1`
**Linha 14:** [A14] TOTAL | [D14] 📐 `=SUM(D7:D13)`
**Linha 16:** [A16] INSTALAÇÕES HIDROSSANITÁRIAS
**Linha 18:** [A18] Descrição | [B18] Parâmetro | [D18] Valor total
**Linha 19:** [A19] Instalações de Água Fria | [B19] 25 | [C19] R$ / AC | [D19] 📐 `=B19*DADOS_INICIAIS!$E$9*1.1`
**Linha 20:** [A20] Instalações de Água Quente | [B20] 20 | [C20] R$ / AC | [D20] 📐 `=B20*DADOS_INICIAIS!$E$9*1.1`
**Linha 21:** [A21] Instalações de Águas Pluviais | [B21] 10 | [C21] R$ / AC | [D21] 📐 `=B21*DADOS_INICIAIS!$E$9*1.1`
**Linha 22:** [A22] Instalações Sanitárias | [B22] 15 | [C22] R$ / AC | [D22] 📐 `=B22*DADOS_INICIAIS!$E$9*1.1`
**Linha 23:** [A23] Louças e Metais | [B23] 20 | [C23] R$ / AC | [D23] 📐 `=B23*DADOS_INICIAIS!$E$9*1.1`
**Linha 24:** [A24] Mão de Obra para Instalações Hidráulicas | [B24] 55 | [C24] R$ / AC | [D24] 📐 `=B24*DADOS_INICIAIS!$E$9*1.1`
**Linha 25:** [A25] TOTAL | [D25] 📐 `=SUM(D19:D24)`
**Linha 27:** [A27] INSTALAÇÕES PREVENTIVAS E GLP
**Linha 29:** [A29] Descrição | [B29] Parâmetro | [D29] Valor total
**Linha 30:** [A30] Instalações Preventivas | [B30] 20 | [C30] R$ / AC | [D30] 📐 `=B30*DADOS_INICIAIS!$E$9*1.1`
**Linha 31:** [A31] Instalações de GLP | [B31] 13 | [C31] R$ / AC | [D31] 📐 `=B31*DADOS_INICIAIS!$E$9*1.1`
**Linha 32:** [A32] Instalações de Proteção e Aterramento - SPDA | [B32] 8 | [C32] R$ / AC | [D32] 📐 `=B32*DADOS_INICIAIS!$E$9*1.1`
**Linha 33:** [A33] TOTAL | [D33] 📐 `=SUM(D30:D32)`
**Linha 35:** [A35] TOTAL INSTALAÇÕES | [D35] 📐 `=D14+D25+D33` | [E35] 📐 `=D35/DADOS_INICIAIS!E9`
**Linha 37:** [E37] 📐 `=E35/1.1`

## Fórmulas Extraídas

- `D7`: `=B7*DADOS_INICIAIS!$E$9*1.1`
- `D8`: `=B8*DADOS_INICIAIS!$E$9*1.1`
- `D9`: `=B9*DADOS_INICIAIS!$E$9*1.1`
- `D10`: `=B10*DADOS_INICIAIS!$E$9*1.1`
- `D11`: `=B11*DADOS_INICIAIS!$E$9*1.1`
- `D12`: `=B12*DADOS_INICIAIS!$E$9*1.1`
- `D13`: `=B13*DADOS_INICIAIS!$E$9*1.1`
- `D14`: `=SUM(D7:D13)`
- `D19`: `=B19*DADOS_INICIAIS!$E$9*1.1`
- `D20`: `=B20*DADOS_INICIAIS!$E$9*1.1`
- `D21`: `=B21*DADOS_INICIAIS!$E$9*1.1`
- `D22`: `=B22*DADOS_INICIAIS!$E$9*1.1`
- `D23`: `=B23*DADOS_INICIAIS!$E$9*1.1`
- `D24`: `=B24*DADOS_INICIAIS!$E$9*1.1`
- `D25`: `=SUM(D19:D24)`
- `D30`: `=B30*DADOS_INICIAIS!$E$9*1.1`
- `D31`: `=B31*DADOS_INICIAIS!$E$9*1.1`
- `D32`: `=B32*DADOS_INICIAIS!$E$9*1.1`
- `D33`: `=SUM(D30:D32)`
- `D35`: `=D14+D25+D33`
- `E35`: `=D35/DADOS_INICIAIS!E9`
- `E37`: `=E35/1.1`