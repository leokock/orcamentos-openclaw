# Flow da Lagoa - Análise dos projetos v01

## Pasta analisada

`G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\AMS Empreendimentos\04. Custo\04.1 Custo - Paramétrico\01 - Projetos`

As pastas `02 - Diretos` e `03 - Indiretos` no mesmo diretório de custo estavam vazias no momento da geração. Portanto, a v01 usa projetos como fonte técnica e Supabase/Ampli/CUB como fonte de custo.

## Inventário consolidado

| Disciplina | Arquivos | MB | Extensões |
| --- | --- | --- | --- |
| ARQ | 28 | 894.4 | .dwg:19, .ifc:1, .pdf:8 |
| CLI | 29 | 36.54 | .dwg:14, .pdf:15 |
| ELETRICA | 22 | 279.09 | .dwg:10, .ifc:2, .pdf:10 |
| EST | 94 | 392.75 | .dwg:54, .ifc:6, .pdf:28, .rvt:6 |
| ETE | 5 | 15.73 | .pdf:5 |
| FUND | 16 | 4.55 | .dwg:8, .pdf:8 |
| HID | 37 | 602.41 | .dwg:17, .ifc:2, .jpg:1, .pdf:17 |
| INTERIORES | 74 | 918.71 | .dwg:42, .ifc:2, .pdf:30 |
| PAISAGISMO | 4 | 14.91 | .dwg:1, .pdf:3 |
| PCI | 24 | 107.94 | .dwg:10, .ifc:2, .pdf:12 |
| PISCINA | 5 | 25.57 | .dwg:2, .ifc:1, .pdf:2 |
| SPDA | 7 | 11.81 | .dwg:3, .ifc:1, .pdf:3 |
| TEL | 20 | 54.63 | .dwg:10, .pdf:10 |
| _Compactadas | 15 | 1167.79 | .zip:15 |

## Leitura por disciplina

- **ARQ**: Arquitetura com IFC e pranchas PDF/DWG. A prancha de cortes/tabelas forneceu áreas, níveis e vagas. O IFC não traz IfcSpace útil para contagem automática de unidades.
- **CLI**: Climatização com PDF/DWG. Entrou como climatização básica residencial/comercial.
- **ELETRICA**: Elétrica com PDF/DWG/IFC. Usado para confirmar disciplina completa; gerador dedicado não identificado na leitura inicial.
- **EST**: Estrutura com modelos RVT/IFC e pranchas. O IFC R06 possui pavimentos estruturais, lajes, vigas e pilares; usado para enquadrar laje convencional/maciça-mista.
- **ETE**: 
- **FUND**: Fundações com PDF/DWG. Sem IFC quantitativo; fundação em hélice foi mantida como premissa V1 até validar memorial/sondagem.
- **HID**: Hidrossanitário com PDF/DWG/IFC. Usado para confirmar complexidade de instalações e muitas áreas molhadas.
- **INTERIORES**: Interiores com PDF/DWG/IFC. Reforça entrega completa e padrão médio-alto.
- **PAISAGISMO**: Paisagismo com PDF/DWG. Entrou em complementares/urbanização.
- **PCI**: Prevenção contra incêndio com PDF/DWG/IFC. Entrou em sistemas/instalações e premissa de pressurização = Não por baixa altura do conjunto.
- **PISCINA**: Projeto específico de piscina presente; briefing V2 marcado como Piscina = Sim.
- **SPDA**: SPDA com PDF/DWG/IFC. Entrou em sistemas especiais.
- **TEL**: Telecom com PDF/DWG. Entrou em sistemas especiais/instalações.
- **_Compactadas**: Backups ZIP das disciplinas. Mantidos no inventário, mas não usados como fonte primária quando havia arquivos abertos.

## Enquadramento adotado

- Padrão: médio-alto.
- Tipologia: 1-2 dormitórios/compactos.
- Área construída: 15.000,62 m².
- Área privativa: 8.343,90 m².
- UR: 236, a validar.
- Pavimentos principais: 6.
- Prazo v01: 24 meses.
- Custo direto recomendado para controle: R$ 55.202.281,60.

## Limitações da leitura automática

- Não foi usado OCR externo; as principais tabelas foram lidas a partir dos renders já gerados da prancha arquitetônica.
- O IFC de arquitetura não trouxe `IfcSpace`, então não permitiu contagem automática confiável de unidades.
- DWG/PDF de disciplinas complementares foram inventariados e usados como presença/complexidade, mas a v01 ainda é paramétrica, não orçamento executivo por quantitativo.
