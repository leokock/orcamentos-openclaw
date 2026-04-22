---
projeto:
  nome: "Electra Towers"
  codigo: "CTN-TZN_ELT"
  tipo: "Residencial multifamiliar e comercial"
  cliente: "Thozen Empreendimentos"
  proprietario: "Rubens Alves Empreendimentos Imobiliários LTDA"
  cnpj_proprietario: "43.339.082/0001-06"
  endereco:
    rua: "Rua 254"
    numero: "215"
    bairro: "Meia Praia"
    cidade: "Itapema"
    municipio_legal: "Porto Belo"
    uf: "SC"
  arquitetas:
    - nome: "Grayce Suelen de Lima"
      cau: "A66076-0"
    - nome: "Anne Elza Geremias"
      cau: "A115914-3"
  rrts:
    - "11610153"
    - "14044074"
  prazo_obra_meses: 48
  numero_torres: 2
  torres:
    - id: "A"
      nome: "Torre A"
    - id: "B"
      nome: "Torre B"
revisao: "R00"
data_atualizacao: "2026-04-21"
fontes:
  - "IFC arquitetura RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc (IFCPOSTALADDRESS)"
  - "DXF ventilação RA_EVM_LEGAL_PROJETO_R05.dxf (ANEXO I Projeto Legal)"
  - "Quadro de áreas oficial (print enviado pelo Leo em 2026-04-21)"
---

# Projeto Electra Towers

## Identidade

Empreendimento **residencial multifamiliar e comercial** localizado em Meia Praia (Itapema/SC),
com município legal de **Porto Belo**. Composto por **2 torres (A e B)**, cada uma com
**24 pavimentos tipo**, totalizando 192 unidades residenciais e 7 salas comerciais.

## Endereço

Rua 254, nº 215, Meia Praia — Itapema/SC
*Município legal:* Porto Belo (a inscrição predial pertence a Porto Belo, embora o bairro Meia Praia faça fronteira com Itapema)

## Cliente e Proprietário

- **Cliente do orçamento (Cartesian):** Thozen Empreendimentos
- **Proprietário registrado (5 lotes):** Rubens Alves Empreendimentos Imobiliários LTDA
- **CNPJ:** 43.339.082/0001-06

## Responsáveis técnicas (RT)

| Profissional | Registro CAU/SC | RRT |
|---|---|---|
| Arq. Grayce Suelen de Lima | A66076-0 | 11610153 |
| Arq. Anne Elza Geremias | A115914-3 | 14044074 |

## Histórico de revisões

| Revisão | Data | Mudanças |
|---|---|---|
| R00 | 2026-04-21 | Primeira versão consolidada com dados oficiais (substitui template Elizabeth II) |

## Documentos-fonte

- **Projetos:** `~/orcamentos/projetos/thozen-electra/projetos/` (DWG + IFC por disciplina)
- **DXFs convertidos via ODA:** `~/openclaw/temp/arq_oda/` (todos os pavimentos arquitetura)
- **DXFs ventilação legal:** `~/orcamentos/projetos/thozen-electra/dxf-ventilacao/`
- **Quadro de áreas oficial:** ver `areas.md`
