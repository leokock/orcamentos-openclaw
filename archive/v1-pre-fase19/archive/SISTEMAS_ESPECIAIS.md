# Aba: SISTEMAS ESPECIAIS
Dimensão: A1:I44 | Linhas: 44 | Colunas: 9

## Conteúdo Completo

### Células Mescladas: 10
  - A42:C42
  - A36:C36
  - A11:C11
  - A44:C44
  - B15:C15
  - A2:E2
  - A21:C21
  - B40:C40
  - A12:C12
  - A20:C20

**Linha 2:** [A2] SISTEMAS ESPECIAIS
**Linha 4:** [A4] CLIMATIZAÇÃO, EXAUSTÃO MECÂNICA E PRESSURIZAÇÃO
**Linha 6:** [A6] Descrição | [B6] Quantidade | [C6] Preço Unitário | [D6] Valor total
**Linha 7:** [A7] Infraestrutura para Instalação de Ar Condicionado | [B7] 📐 `=SUM('Obra '!L21:L39)` | [C7] 1200 | [D7] 📐 `=B7*C7*1.1`
**Linha 8:** [A8] Instalação de Ar Condicionado | [B8] 📐 `=SUM('Obra '!M21:M39)` | [C8] 9000 | [D8] 📐 `=B8*C8*1.1`
**Linha 9:** [A9] Ventokit | [B9] 📐 `=SUM('Obra '!K21:K39)` | [C9] 900 | [D9] 📐 `=B9*C9*1.1`
**Linha 10:** [A10] Churrasqueiras | [B10] 📐 `=SUM('Obra '!I21:I39)` | [C10] 2600 | [D10] 📐 `=B10*C10*1.1`
**Linha 11:** [A11] TOTAL | [D11] 📐 `=SUM(D7:D10)`
**Linha 13:** [A13] COMUNICAÇÃO
**Linha 15:** [A15] Descrição | [B15] Parâmetro | [D15] Valor total
**Linha 16:** [A16] CFTV | [B16] 1.5 | [C16] R$ / AC | [D16] 📐 `=B16*DADOS_INICIAIS!$E$9*1.1`
**Linha 17:** [A17] Interfone | [B17] 1.5 | [C17] R$ / AC | [D17] 📐 `=(B17*DADOS_INICIAIS!$E$9+'Obra '!$F$6*800)*1.1` | [E17] *CONSIDERANDO PORTEIRO COM VÍDEO
**Linha 18:** [A18] TV e internet | [B18] 4 | [C18] R$ / AC | [D18] 📐 `=B18*DADOS_INICIAIS!$E$9*1.1`
**Linha 19:** [A19] Automação, telecomunicação e sistemas de segurança | [B19] 5 | [C19] R$ / AC | [D19] 📐 `=B19*DADOS_INICIAIS!$E$9*1.1`
**Linha 20:** [A20] TOTAL | [D20] 📐 `=SUM(D16:D19)`
**Linha 22:** [A22] EQUIPAMENTOS
**Linha 24:** [A24] Descrição | [B24] Quantidade | [C24] Preço Unitário | [D24] Valor total
**Linha 25:** [A25] Elevadores | [B25] 2 | [C25] 📐 `=(403672.5/21*16)/2916.12*3012.64` | [D25] 📐 `=B25*C25*1.1`
**Linha 26:** [A26] Grupo de geradores | [C26] 42000 | [D26] 📐 `=B26*C26*1.1`
**Linha 27:** [A27] Pressurização de escada | [C27] 📐 `=26.4*DADOS_INICIAIS!E9` | [D27] 📐 `=B27*C27*1.1`
**Linha 28:** [A28] Bombas | [B28] 1 | [C28] 10000 | [D28] 📐 `=B28*C28*1.1`
**Linha 29:** [A29] Infra de carro elétrico | [B29] 1 | [C29] 560 | [D29] 📐 `=B29*C29*1.1`
**Linha 30:** [A30] Equipamento de carro elétrico 23kv | [B30] 1 | [C30] 9500 | [D30] 📐 `=B30*C30*1.1`
**Linha 31:** [A31] Equipamento de piscina aquecida  | [B31] 1 | [C31] 121000 | [D31] 📐 `=B31*C31*1.1`
**Linha 32:** [A32] Sauna | [C32] 8500 | [D32] 📐 `=B32*C32*1.1`
**Linha 33:** [A33] Spa | [C33] 15000 | [D33] 📐 `=B33*C33*1.1`
**Linha 34:** [A34] Hidromassagem | [B34] 1 | [C34] 25000 | [D34] 📐 `=B34*C34*1.1`
**Linha 35:** [A35] Sistema de aquecimento | [B35] 0 | [C35] 📐 `=55*DADOS_INICIAIS!E9` | [D35] 📐 `=B35*C35`
**Linha 36:** [A36] TOTAL | [D36] 📐 `=SUM(D25:D35)`
**Linha 38:** [A38] OUTROS SISTEMAS ESPECIAIS
**Linha 40:** [A40] Descrição | [B40] Parâmetro | [D40] Valor total
**Linha 41:** [A41] Outros sistemas | [B41] 20 | [C41] R$ / AC | [D41] 📐 `=B41*DADOS_INICIAIS!E9*1.1`
**Linha 42:** [A42] TOTAL | [D42] 📐 `=SUM(D41:D41)`
**Linha 44:** [A44] TOTAL SISTEMAS ESPECIAIS | [D44] 📐 `=D11+D20+D36+D42` | [E44] 📐 `=D44/DADOS_INICIAIS!E9`

## Fórmulas Extraídas

- `B7`: `=SUM('Obra '!L21:L39)`
- `D7`: `=B7*C7*1.1`
- `B8`: `=SUM('Obra '!M21:M39)`
- `D8`: `=B8*C8*1.1`
- `B9`: `=SUM('Obra '!K21:K39)`
- `D9`: `=B9*C9*1.1`
- `B10`: `=SUM('Obra '!I21:I39)`
- `D10`: `=B10*C10*1.1`
- `D11`: `=SUM(D7:D10)`
- `D16`: `=B16*DADOS_INICIAIS!$E$9*1.1`
- `D17`: `=(B17*DADOS_INICIAIS!$E$9+'Obra '!$F$6*800)*1.1`
- `D18`: `=B18*DADOS_INICIAIS!$E$9*1.1`
- `D19`: `=B19*DADOS_INICIAIS!$E$9*1.1`
- `D20`: `=SUM(D16:D19)`
- `C25`: `=(403672.5/21*16)/2916.12*3012.64`
- `D25`: `=B25*C25*1.1`
- `D26`: `=B26*C26*1.1`
- `C27`: `=26.4*DADOS_INICIAIS!E9`
- `D27`: `=B27*C27*1.1`
- `D28`: `=B28*C28*1.1`
- `D29`: `=B29*C29*1.1`
- `D30`: `=B30*C30*1.1`
- `D31`: `=B31*C31*1.1`
- `D32`: `=B32*C32*1.1`
- `D33`: `=B33*C33*1.1`
- `D34`: `=B34*C34*1.1`
- `C35`: `=55*DADOS_INICIAIS!E9`
- `D35`: `=B35*C35`
- `D36`: `=SUM(D25:D35)`
- `D41`: `=B41*DADOS_INICIAIS!E9*1.1`
- `D42`: `=SUM(D41:D41)`
- `D44`: `=D11+D20+D36+D42`
- `E44`: `=D44/DADOS_INICIAIS!E9`