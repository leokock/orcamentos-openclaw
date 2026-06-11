# Relatório de Run — Paramétrico Placon Hermann Blumenau

_Gerado: 2026-05-29 (run autônomo overnight) | RDO? não — Placon Empreendimentos | Florianópolis/Centro_

## Entregáveis gerados (6 arquivos cliente-facing)

1. **Paramétrico V2 Híbrido** — `placon-hermann-blumenau-parametrico-v00-final.xlsx`
2. **Premissas de Origem** — `placon-hermann-blumenau-PREMISSAS-ORIGEM-final.docx`
3. **Justificativa Itens Acima da Média** — `placon-hermann-blumenau-JUSTIFICATIVA-ITENS-ACIMA-MEDIA-final.docx`
4. **Apresentação (21 slides, paleta V2)** — `placon-hermann-blumenau-apresentacao-v00-final.pptx`
5. **Viabilidade Financeira (analítico)** — `viabilidade-placon-hermann-blumenau-v1.xlsx`
6. **Viabilidade (didático)** — `viabilidade-placon-hermann-blumenau-v1-didatico.xlsx`

Copiados para o Drive: `...\04. Custo\04.1 Custo - Paramétrico\Entregáveis Paramétrico\`.

## Resultados principais

- **Custo total estimado: R$ 24.445.536** | **R$/m² AC: R$ 4.158,85** (M-A, faixa sanity 3.500–6.000 ✓)
- Custo/UR: R$ 698.444 | CUB Ratio: 1,342 (CUB-SC R$ 3.100)
- AC 5.877,96 m² · 35 apt + 1 loja · 22 níveis estruturais · laje convencional
- **Viabilidade (VGV premissa R$ 16.000/m²):** VPL mediana R$ 11,42 mi · P10 R$ 7,34 mi · P90 R$ 15,55 mi · P(VPL>0) 100% · P(TIR>TMA) 100% (TMA 14%).

## Premissas assumidas (sem memorial de acabamentos)

- Padrão **Médio-Alto** estimado (decisão Leo) — louças/metais/pisos/esquadrias/fachada a validar.
- Laje **Convencional** (pranchas FORMA "ESTRUTURA NÃO PROTENDIDA", h=20/22/25).
- Fachada **textura/pintura acrílica** (PU ~R$50 mat + 30 MO + 18 balancim, altura ~46 m).
- Fundação **Hélice** (default — sem sondagem na pasta); pressurização **Não**; gerador como **allowance** (12 kVA bomba pluvial).
- CUB-SC R$ 3.100 (média residencial mai/2026 ~R$ 3.064; dentro de ~1%).
- np 20 / npt 13 (inventário FORMA = 22 pranchas, consistente).

## ⚠ Itens a validar (revisão de manhã)

1. **Gerenciamento ~16,8% do total (R$ 813/m²)** — acima do típico 8-12%. Revisar equipe/indiretos (SPEC pedia equipe enxuta; o template pode ter usado default). **Maior impacto no total.**
2. **Louças e Metais ~R$ 20/m²** — baixo para padrão M-A. Revisar PU.
3. **VGV R$ 16.000/m²** — premissa, não pesquisa de mercado. A viabilidade roda com sensibilidade; valide antes de mostrar VPL/TIR como definitivos.
4. Acabamentos em geral (sem memorial) — revisar com a Placon na reunião.

## Notas técnicas

- Recalc dos totais via `pycel`/`formulas` (sem Excel COM — não houve colisão na fila overnight).
- openpyxl só em arquivos novos; nenhum arquivo da pasta-mãe do Drive foi alterado (só cópia em Entregáveis).
- Sync para `_Parametrico_IA` **não** feito (precisa checkpoint do Leo — 1º sync de slug novo).

## Próximos passos

1. Revisar os 4 itens acima (especialmente Gerenciamento — ajustar na aba se necessário, recalcular).
2. Ajustar acabamentos com a Placon.
3. Se aprovado, sincronizar para `_Parametrico_IA/hermann-blumenau` via `sincronizar_parametrico_drive.py --slug placon-hermann-blumenau --archive-old`.
