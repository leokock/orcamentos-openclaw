# Premissas de Origem - Brickell Modern Home - Nowa v00

Gerado: 2026-06-09T20:46:14-03:00 BRT
Pacote: `C:\Users\leona\orcamentos-openclaw\base\pacotes\brickell-nowa`
Fonte dos projetos: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\Nowa\04. Custo\04.1 Custo - Paramétrico\01 - Projetos`

## Dados físicos adotados

| Campo | Valor | Fonte |
|---|---:|---|
| Área construída | 10.840,31 m² | PDFs ELE/HID/PCI - pranchas VOF |
| Unidades residenciais | 38 UR | Marcadores de tipologia em ELE/HID/PCI |
| Pavimentos | 29 níveis | IFC estrutural EST/AP R00 |
| Pavimentos tipo | 18 | IFC: Tipo 1 a Tipo 5b |
| Altura descendente PPCI | 67,32 m | PDFs ELE/HID/PCI - VOF |
| Garagens | 4 níveis | IFC: Garagem 1 a Garagem 4 |
| Subsolos | 0 | IFC não indica subsolo; Fundação abaixo do Térreo |
| Vagas | 76, a confirmar | Premissa v00: 2 vagas por UR; ARQ está em DWG |
| Elevadores | 2, a confirmar | PDFs citam elevador de emergência; torre alta |
| Gerador | Sim | PDFs DRYWALL/PCI citam sala e posicionamento do gerador |
| Pressurização / fumaça | Sim | PPCI cita escada pressurizada/exaustão e IN10/IN12 |
| Piscina | Sim | PDFs de lazer citam acesso à piscina |
| Climatização | Completa | Projeto CLI com equipamentos HW/K7/CND e condensadoras |
| Alvenaria | Mista | ALV com bloco cerâmico + DRYWALL ST/RU em várias pranchas |
| Fachada | Textura, a confirmar | Projeto de fachada não encontrado em PDF legível |
| Fundação | Hélice, a confirmar | IFC não tem IfcFooting/IfcPile; sem SPT legível |
| CUB base | R$ 3.850,00/m² | Supabase specifications.ampli_indexers, SC, 2026-05 |

## Briefing V2 adotado

| Campo | Valor |
|---|---|
| laje | Convencional |
| subsolos | 0 |
| fundacao | Hélice |
| padrao_acabamento | Alto |
| fachada | Textura |
| pressurizacao | Sim |
| n_torres | 1 |
| gerador | Sim |
| entrega | Completa |
| tipologia | Misto |
| pe_direito | Padrão (3.00) |
| n_banheiros | 2 |
| tipo_piso | Porcelanato |
| piscina | Sim |

## Macrogrupos e origem da premissa

| Macrogrupo | R$/m² | % | Total | Premissa |
|---|---:|---:|---:|---|
| Gerenciamento | 468 | 11,7% | R$ 5.078.256,00 | 36 meses, torre alta, equipe técnica e canteiro do V2; benchmark alto Supabase. |
| Mov. Terra | 17 | 0,4% | R$ 184.285,27 | Sem subsolo no IFC; movimentação de terra base por AC. |
| Infraestrutura | 154 | 3,8% | R$ 1.664.206,26 | Fundação hélice assumida por ausência de SPT/projeto de fundação legível. |
| Supraestrutura | 786 | 19,6% | R$ 8.518.891,30 | IFC estrutural com 29 níveis, 762 lajes, 1.410 vigas, 876 pilares; laje convencional v00. |
| Alvenaria | 182 | 4,5% | R$ 1.968.312,00 | Bloco cerâmico ALV + drywall ST/RU em PDFs de vedação. |
| Impermeabilização | 71 | 1,8% | R$ 770.638,98 | Índice V2 para torre com áreas molhadas, lazer e cobertura. |
| Instalações | 476 | 11,9% | R$ 5.165.299,31 | ELE/HID/PCI completos, gás, preventivo, medições e prumadas de torre alta. |
| Sist. Especiais | 221 | 5,5% | R$ 2.399.272,00 | Elevadores, gerador, piscina, pressurização, SPDA, bombas e ventilação de garagens. |
| Climatização | 90 | 2,2% | R$ 975.025,58 | Projeto CLI com equipamentos; v00 reforça quantidade e infra. |
| Rev. Int. Parede | 132 | 3,3% | R$ 1.427.377,85 | Acabamento alto com áreas molhadas e paredes internas por índice V2. |
| Teto | 73 | 1,8% | R$ 787.176,00 | DRYWALL/FORRO com gesso acartonado ST/RU e forro em áreas comuns/privativas. |
| Pisos | 204 | 5,1% | R$ 2.206.087,68 | Porcelanato como premissa v00 para padrão alto. |
| Pintura | 155 | 3,8% | R$ 1.676.382,84 | Sistema acrílico/PVA por índice V2. |
| Esquadrias | 374 | 9,3% | R$ 4.051.565,86 | Alumínio/vidro por benchmark alto; quadro não localizado em PDF. |
| Louças e Metais | 75 | 1,9% | R$ 813.023,30 | 2 banheiros/UR como premissa v00, padrão alto. |
| Fachada | 237 | 5,9% | R$ 2.570.706,00 | Textura como premissa conservadora; projeto de fachada não localizado. |
| Complementares | 245 | 6,1% | R$ 2.655.813,72 | Lazer com piscina, áreas comuns, comunicação visual e paisagismo por índice. |
| Imprevistos | 59 | 1,5% | R$ 643.685,00 | 1,5% padrão Cartesian aplicado pelo V2. |
| **TOTAL** | **4.018** | **100,0%** | **R$ 43.556.004,95** | |

## Ajustes manuais v00

| Local | Item | Ajuste | Justificativa |
|---|---|---|---|
| INDICES!C22 | Pressurização | R$ 80.000 -> R$ 180.000 | Torre alta com escada pressurizada/exaustão e controle de fumaça nos PDFs PPCI. |
| INDICES!C23 | Gerador | R$ 180.000 -> R$ 350.000 | PDFs citam sala/posicionamento do gerador; v00 adota allowance de torre alta. |
| Sist. Especiais | Elevadores | PUs ajustados para R$ 480.000/un | 2 elevadores em torre de 29 níveis, incluindo menção a elevador de emergência. |
| Sist. Especiais | Ventilação garagens | 4 pavimentos x R$ 27.318 | PDFs G1/G2/G4 citam ventilação mecânica alternativa a área natural mínima. |
| Climatização | Equipamentos e infra | 4,5 un/UR + infra R$ 18/m² | Projeto CLI traz múltiplos equipamentos HW/K7/CND; default 1,5 un/UR ficaria baixo. |
| Louças e Metais | Escopo alto sem memorial | R$ 75/m² AC | Default V2 por UR ficava artificialmente baixo para padrão alto; usa referência entre médio-alto e alto. |
| Complementares | Lazer e áreas comuns | Mobiliário/ambientação/equipamentos reforçados | PDFs indicam piscina, coworking, gourmet, festas, sala comercial e lazer de cobertura. |

## Limitações para validação v01

- Arquitetura principal está em DWG; sem conversor DWG disponível nesta sessão. A v00 usa ARQ como limitação explícita.
- Vagas, fachada e quadro de esquadrias não foram encontrados em PDF legível e devem ser validados na v01.
- Sem SPT/fundação em PDF legível; fundação hélice é premissa Cartesian de v00.
- Não houve escrita no Supabase nem sincronização ao Drive _Parametrico_IA; esta é a versão local para validação do Leo.

Validação de recálculo: `EXCEL_COM_OK`.