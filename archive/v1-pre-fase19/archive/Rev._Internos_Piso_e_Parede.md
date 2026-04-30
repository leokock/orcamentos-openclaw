# Aba: Rev. Internos Piso e Parede
Dimensão: A1:J26 | Linhas: 26 | Colunas: 10

## Conteúdo Completo

### Células Mescladas: 6
  - A24:F24
  - A2:A4
  - D14:E14
  - A22:F22
  - B14:C14
  - A21:F21

**Linha 2:** [A2] ORÇAMENTO PARAMÉTRICO
GERENCIAMENTO EXECUTIVO
**Linha 7:** [A7] Cliente
**Linha 8:** [A8] Obra
**Linha 9:** [A9] Data | [B9] 2024-06-28 00:00:00
**Linha 10:** [A10] Revisão | [B10] R00
**Linha 12:** [A12] REVESTIMENTOS INTERNOS EM PISO E PAREDE
**Linha 14:** [A14] Descrição | [B14] Quantidade | [D14] Parâmetro | [F14] Referência | [G14] Valor total
**Linha 15:** [A15] Polimento de concreto | [B15] 📐 `=(556.79-(11.99+4.57+1.7*2+2.56*2+5.47))*3+527.99-(11.99+4.57+1.69*2+5.47+2.56*2)` | [C15] m² | [D15] 16.5 | [E15] R$ / m² | [F15] Média | [G15] 📐 `=D15*B15*1.1` | [J15] 📐 `=556.79-(11.99+1.7*2+2.56*2+5.47)+(329.6-(11.99+1.7*2+2.56*2+5.47))*11`
**Linha 16:** [A16] Piso alisado | [B16] 📐 `=11.99*16` | [C16] m² | [D16] 25 | [E16] R$ / m² | [F16] Média | [G16] 📐 `=D16*B16*1.1`
**Linha 17:** [A17] Contrapiso | [B17] 📐 `=DADOS_INICIAIS!E9*0.62*0+556.79-(11.99+1.7*2+2.56*2+5.47)+(329.6-(11.99+1.7*2+2.56*2+5.47))*11` | [C17] m² | [D17] 📐 `=B17/DADOS_INICIAIS!E9` | [E17] m² / AC | [F17] Média | [G17] 📐 `=+B17*65*1.1`
**Linha 18:** [A18] Manta acústica | [B18] 📐 `=B17*0.8` | [C18] m² | [D18] 📐 `=B18/DADOS_INICIAIS!E9` | [E18] m² / AC | [F18] Média | [G18] 📐 `=+B18*27*1.1`
**Linha 19:** [A19] Chapisco | [B19] 📐 `=ALVENARIA!D15*2-'Rev. Fachada'!B15` | [C19] m² | [D19] 📐 `=B19/DADOS_INICIAIS!E9` | [E19] m² / AC | [F19] Média | [G19] 📐 `=+B19*5*1.1`
**Linha 20:** [A20] Reboco | [B20] 📐 `=B19` | [C20] m² | [D20] 📐 `=B20/DADOS_INICIAIS!E9` | [E20] m² / AC | [F20] Média | [G20] 📐 `=50*B20*1.1`
**Linha 21:** [A21] TOTAL | [G21] 📐 `=SUM(G15:G20)`
**Linha 24:** [A24] TOTAL REVESTIMENTOS | [G24] 📐 `=G21` | [H24] 📐 `=G24/DADOS_INICIAIS!E9`
**Linha 26:** [H26] 📐 `=H24/1.1`

## Fórmulas Extraídas

- `B15`: `=(556.79-(11.99+4.57+1.7*2+2.56*2+5.47))*3+527.99-(11.99+4.57+1.69*2+5.47+2.56*2)`
- `G15`: `=D15*B15*1.1`
- `J15`: `=556.79-(11.99+1.7*2+2.56*2+5.47)+(329.6-(11.99+1.7*2+2.56*2+5.47))*11`
- `B16`: `=11.99*16`
- `G16`: `=D16*B16*1.1`
- `B17`: `=DADOS_INICIAIS!E9*0.62*0+556.79-(11.99+1.7*2+2.56*2+5.47)+(329.6-(11.99+1.7*2+2.56*2+5.47))*11`
- `D17`: `=B17/DADOS_INICIAIS!E9`
- `G17`: `=+B17*65*1.1`
- `B18`: `=B17*0.8`
- `D18`: `=B18/DADOS_INICIAIS!E9`
- `G18`: `=+B18*27*1.1`
- `B19`: `=ALVENARIA!D15*2-'Rev. Fachada'!B15`
- `D19`: `=B19/DADOS_INICIAIS!E9`
- `G19`: `=+B19*5*1.1`
- `B20`: `=B19`
- `D20`: `=B20/DADOS_INICIAIS!E9`
- `G20`: `=50*B20*1.1`
- `G21`: `=SUM(G15:G20)`
- `G24`: `=G21`
- `H24`: `=G24/DADOS_INICIAIS!E9`
- `H26`: `=H24/1.1`