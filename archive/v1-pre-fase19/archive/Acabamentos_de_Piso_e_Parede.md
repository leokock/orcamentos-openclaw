# Aba: Acabamentos de Piso e Parede
Dimensão: A1:K73 | Linhas: 73 | Colunas: 11

## Conteúdo Completo

### Células Mescladas: 6
  - A24:F24
  - A2:A4
  - A23:F23
  - D14:E14
  - B14:C14
  - A26:F26

**Linha 2:** [A2] ORÇAMENTO PARAMÉTRICO
GERENCIAMENTO EXECUTIVO
**Linha 7:** [A7] Cliente
**Linha 8:** [A8] Obra
**Linha 9:** [A9] Data | [B9] 2024-06-28 00:00:00
**Linha 10:** [A10] Revisão | [B10] R00
**Linha 12:** [A12] ACABAMENTOS EM PISO E PAREDE
**Linha 14:** [A14] Descrição | [B14] Quantidade | [D14] Parâmetro | [F14] Referência | [G14] Valor total
**Linha 15:** [A15] Porcelanato  | [B15] 📐 `='Rev. Internos Piso e Parede'!B17` | [C15] m²  | [D15] 📐 `=50*1.1+2.25+11*0.5+75` | [E15] R$ / m² | [F15] Média | [G15] 📐 `=+D15*B15*1.1`
**Linha 16:** [A16] Vinilico | [C16] m²  | [D16] 125 | [E16] R$ / m² | [F16] Média | [G16] 📐 `=+D16*B16*1.1`
**Linha 17:** [A17] Piscina | [B17] 📐 `=10*4+2.5*3+10*2+4*2+2.5*2+3*2` | [C17] m²  | [D17] 📐 `=110*1.1+2.25+11*0.5+75` | [E17] R$ / m² | [F17] Média | [G17] 📐 `=+D17*B17*1.1`
**Linha 18:** [A18] Grama sintetica | [C18] m²  | [D18] 210 | [E18] R$ / m² | [F18] Média | [G18] 📐 `=+D18*B18*1.1`
**Linha 19:** [A19] Paver | [B19] 📐 `=25*5` | [C19] m²  | [D19] 60 | [E19] R$ / m² | [F19] Média | [G19] 📐 `=+D19*B19*1.1`
**Linha 20:** [A20] Rodapés | [B20] 1 | [C20] vb | [D20] 30 | [E20] R$ / AC | [F20] Média | [G20] 📐 `=D20*DADOS_INICIAIS!$E$9*1.1`
**Linha 21:** [A21] Soleiras e peitoris | [B21] 1 | [C21] vb | [D21] 20 | [E21] R$ / AC | [F21] Média | [G21] 📐 `=D21*DADOS_INICIAIS!$E$9*1.1`
**Linha 22:** [A22] Revestimentos de Parede | [B22] 1 | [C22] vb | [D22] 45 | [E22] R$ / AC | [F22] Média | [G22] 📐 `=D22*DADOS_INICIAIS!$E$9*1.1`
**Linha 23:** [A23] 📐 `=20*40` | [G23] 📐 `=SUM(G15:G22)`
**Linha 26:** [A26] TOTAL ACABAMENTOS | [G26] 📐 `=G23` | [H26] 📐 `=G26/DADOS_INICIAIS!E9`
**Linha 28:** [H28] 📐 `=H26/1.1`

## Fórmulas Extraídas

- `B15`: `='Rev. Internos Piso e Parede'!B17`
- `D15`: `=50*1.1+2.25+11*0.5+75`
- `G15`: `=+D15*B15*1.1`
- `G16`: `=+D16*B16*1.1`
- `B17`: `=10*4+2.5*3+10*2+4*2+2.5*2+3*2`
- `D17`: `=110*1.1+2.25+11*0.5+75`
- `G17`: `=+D17*B17*1.1`
- `G18`: `=+D18*B18*1.1`
- `B19`: `=25*5`
- `G19`: `=+D19*B19*1.1`
- `G20`: `=D20*DADOS_INICIAIS!$E$9*1.1`
- `G21`: `=D21*DADOS_INICIAIS!$E$9*1.1`
- `G22`: `=D22*DADOS_INICIAIS!$E$9*1.1`
- `A23`: `=20*40`
- `G23`: `=SUM(G15:G22)`
- `G26`: `=G23`
- `H26`: `=G26/DADOS_INICIAIS!E9`
- `H28`: `=H26/1.1`