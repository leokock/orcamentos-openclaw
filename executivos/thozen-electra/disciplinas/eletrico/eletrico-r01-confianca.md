# Relatorio de Confianca — Instalacoes Eletricas R01

**Projeto:** Thozen Electra Towers
**Data:** 23/03/2026

---

## Verde — Dados com fonte direta verificavel

| Item | Quantidade | Fonte |
|------|-----------|-------|
| Luminarias por pavimento | 4.655 un | IFC (9 arquivos, contagem direta IfcFlowTerminal) |
| Eletrodutos — contagem de trechos | ~213.000 | IFC (IfcFlowSegment, classificado por ObjectType) |
| Eletrodutos — diametros | 7 faixas (3/4" a 4") | IFC (propriedade "Tamanho" nos PropertySets) |
| Distribuicao por pavimento | 9 pavimentos mapeados | IFC (1 arquivo por pavimento) |
| Multiplicador tipo | x24 pavimentos | IFC (arquivo E08 cobre 8~31 pav) |

**Acao:** Confiar. Dados rastreaveis ate o arquivo IFC de origem.

---

## Amarelo — Dados calculados ou referenciados (conferir logica)

| Item | Valor | Logica | Verificar |
|------|-------|--------|-----------|
| R$/m2 total | R$ 190,00 | Referencia Elizabeth II (R$ 213) ajustado pra medio-alto padrao | Se padrao do Electra justifica desconto de 10% |
| Distribuicao % por subgrupo | 13 subgrupos | Proporcional ao Elizabeth II R01 | Se o Electra tem diferenca significativa de escopo (ex: sem gerador) |
| Subestacao (R$ 1,23M) | 18% do total | Elizabeth II teve 18% em subestacao | Confirmar com cotacao — subestacao depende muito de potencia |
| Barramento (R$ 466k) | 6,8% do total | Elizabeth II como ref | Confirmar tipo de barramento (blindado?) |
| Entrada de energia (R$ 850k) | 12,4% do total | Elizabeth II como ref | Confirmar padrao de entrada (MT/BT) com concessionaria |

**Acao:** Revisar a logica, confirmar premissas com equipe tecnica.

---

## Vermelho — Dados estimados sem fonte (requer decisao)

| Item | Valor Estimado | Por que nao tem fonte | Acao necessaria |
|------|---------------|----------------------|-----------------|
| Mao de obra eletrica (R$ 2,80M) | 41% do total | Nenhum orcamento de MO recebido | Solicitar proposta de empreiteira eletrica |
| Gerador (R$ 480k) | 7% do total | Nao ha projeto de gerador na pasta | Confirmar se o Electra tera gerador e qual potencia |
| Quadros eletricos (quantidade) | Nao quantificado | Nao modelados no IFC | Processar DWGs ou solicitar lista de quadros |
| Tomadas e interruptores | Nao quantificado | Nao modelados no IFC | Processar DWGs — essencial pra detalhar |
| Cabos — bitolas e metragens | Nao detalhado | IFC sem propriedades de bitola | Processar DWGs para tabela de cabos |
| Comprimentos de eletrodutos | Nao calculado | Geometria IFC complexa | Processar DWGs ou script geometrico dedicado |

**Acao:** Estes itens impedem detalhamento abaixo do nivel de subgrupo. Priorizar processamento dos DWGs.

---

## Resumo de Confianca

| Nivel | Itens | % do Orcamento | Interpretacao |
|-------|-------|----------------|---------------|
| Verde | 5 itens quantitativos | ~3% (eletrodutos + luminarias) | Confiar, rastreavel |
| Amarelo | 5 premissas de calculo | ~56% (subgrupos com ref) | Revisar logica, validar |
| Vermelho | 6 gaps criticos | ~41% (MO + itens sem fonte) | Requer decisao/dados |

**Conclusao:** Esta e uma estimativa de nivel parametrico com ancoragem em dados IFC reais. Para evoluir pra orcamento executivo completo (R02), e necessario processar os DWGs e obter cotacoes de MO, subestacao e gerador.

---

*Gerado em 23/03/2026*
