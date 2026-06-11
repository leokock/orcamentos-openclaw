# Flow da Lagoa - Premissas de origem do orçamento paramétrico v01

Gerado em 2026-06-09.

## Fonte principal

- Pasta: `G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\AMS Empreendimentos\04. Custo\04.1 Custo - Paramétrico\01 - Projetos`
- Cliente/empreendimento identificado em prancha: AMS Empreendimentos Lagoa SPE Ltda.
- Método: Paramétrico V2 Híbrido, com briefing do projeto, base de índices Supabase `indices-cartesian`, referências Ampli e CUB-SC residencial médio.
- CUB usado: R$ 3.096,25/m², referência maio/2026 para uso em junho/2026.

## Dados de projeto usados

| Campo | Valor | Fonte |
| --- | --- | --- |
| Área construída | 15.000,62 m² | ARQ AP 008 CORTE/TABELAS R12, quadro Área Total a Construir |
| Área computável | 8.122,55 m² | ARQ AP 008 CORTE/TABELAS R12, quadro Área Total a Construir |
| Área privativa | 8.343,90 m² | ARQ AP 008 CORTE/TABELAS R12, quadro Área Privativa |
| Pavimentos principais | NA01 a NA06 | ARQ AP 008 CORTE/TABELAS R12 e cortes |
| Níveis técnicos | NA07 Barrilete, NA08 Reservatório Superior, NA09 Tampa | ARQ AP 008 CORTE/TABELAS R12 |
| Vagas automóveis | 161 | Quadro de vagas: 4 comerciais + 149 privativas + 8 visitantes |
| Vagas bicicleta | 213 | Quadro de vagas: 5 comerciais + 198 privativas + 10 visitantes |
| Núcleos verticais | 4 | Leitura visual das plantas e cortes; elevadores a validar |
| Unidades residenciais | 236 | Premissa por área privativa média de 35,36 m²/UR; quadro de unidades não encontrado |
| Estrutura | Lajes maciças/mistas e=20 cm | IFC estrutural R06: slabs, beams e columns; sem indício de protensão |
| Piscina | Sim | Há disciplina PISCINA com DWG/PDF/IFC |

## Premissas críticas v01

- UR = 236 é premissa de contagem por área privativa média: 35,36 m² privativos/UR. O quadro oficial de unidades não apareceu legível nos arquivos analisados.
- Vagas para parâmetro de orçamento = 161 automóveis. As 213 vagas de bicicleta foram registradas separadamente para não inflar a fórmula de garagem.
- Projeto com 4 blocos/núcleos verticais. O template V2 aceita até 3 torres no dropdown; por isso usei `Nº Torres = 3` e registrei o ajuste em notas.
- Elevadores = 4 por leitura visual dos núcleos. Validar com projeto de transporte vertical.
- Fundação = Hélice é premissa inicial. A disciplina FUND existe em PDF/DWG, mas não havia IFC quantitativo ou memorial consolidado para cravar o tipo sem revisão humana.
- Fachada = Textura é premissa inicial. Ajustar para cerâmica/ACM/pele de vidro se o memorial arquitetônico confirmar outro acabamento.
- BDI: tratado como cenário de validação em aba própria. O custo direto recomendado v01 é R$ 55.202.281,60, equivalente a R$ 3.680,00/m².

## Inventário por disciplina

| Disciplina | Arquivos | MB | Extensões | Leitura v01 |
| --- | --- | --- | --- | --- |
| ARQ | 28 | 894.4 | .dwg:19, .ifc:1, .pdf:8 | Arquitetura com IFC e pranchas PDF/DWG. A prancha de cortes/tabelas forneceu áreas, níveis e vagas. O IFC não traz IfcSpace útil para contagem automática de unidades. |
| CLI | 29 | 36.54 | .dwg:14, .pdf:15 | Climatização com PDF/DWG. Entrou como climatização básica residencial/comercial. |
| ELETRICA | 22 | 279.09 | .dwg:10, .ifc:2, .pdf:10 | Elétrica com PDF/DWG/IFC. Usado para confirmar disciplina completa; gerador dedicado não identificado na leitura inicial. |
| EST | 94 | 392.75 | .dwg:54, .ifc:6, .pdf:28, .rvt:6 | Estrutura com modelos RVT/IFC e pranchas. O IFC R06 possui pavimentos estruturais, lajes, vigas e pilares; usado para enquadrar laje convencional/maciça-mista. |
| ETE | 5 | 15.73 | .pdf:5 |  |
| FUND | 16 | 4.55 | .dwg:8, .pdf:8 | Fundações com PDF/DWG. Sem IFC quantitativo; fundação em hélice foi mantida como premissa V1 até validar memorial/sondagem. |
| HID | 37 | 602.41 | .dwg:17, .ifc:2, .jpg:1, .pdf:17 | Hidrossanitário com PDF/DWG/IFC. Usado para confirmar complexidade de instalações e muitas áreas molhadas. |
| INTERIORES | 74 | 918.71 | .dwg:42, .ifc:2, .pdf:30 | Interiores com PDF/DWG/IFC. Reforça entrega completa e padrão médio-alto. |
| PAISAGISMO | 4 | 14.91 | .dwg:1, .pdf:3 | Paisagismo com PDF/DWG. Entrou em complementares/urbanização. |
| PCI | 24 | 107.94 | .dwg:10, .ifc:2, .pdf:12 | Prevenção contra incêndio com PDF/DWG/IFC. Entrou em sistemas/instalações e premissa de pressurização = Não por baixa altura do conjunto. |
| PISCINA | 5 | 25.57 | .dwg:2, .ifc:1, .pdf:2 | Projeto específico de piscina presente; briefing V2 marcado como Piscina = Sim. |
| SPDA | 7 | 11.81 | .dwg:3, .ifc:1, .pdf:3 | SPDA com PDF/DWG/IFC. Entrou em sistemas especiais. |
| TEL | 20 | 54.63 | .dwg:10, .pdf:10 | Telecom com PDF/DWG. Entrou em sistemas especiais/instalações. |
| _Compactadas | 15 | 1167.79 | .zip:15 | Backups ZIP das disciplinas. Mantidos no inventário, mas não usados como fonte primária quando havia arquivos abertos. |

## Arquivos gerados

- `parametrico-flow-da-lagoa-v01.xlsx`
- `parametrico-flow-da-lagoa.xlsx`
- `PREMISSAS-ORIGEM.md`
- `JUSTIFICATIVA-ITENS-ACIMA-DA-MEDIA.md`
- `ANALISE-PROJETOS-FLOW-DA-LAGOA.md`
- `inventario-arquivos-flow-da-lagoa.csv`
