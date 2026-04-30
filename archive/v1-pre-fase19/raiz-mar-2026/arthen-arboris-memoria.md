# Memória de Projeto — Arthen Arboris

> Registro de rastreabilidade: documentos recebidos, premissas adotadas, dados extraídos.
> Criado: 09/04/2026

---

## 1. IDENTIFICAÇÃO

| Campo | Valor |
|-------|-------|
| Projeto | Arthen Arboris |
| Cliente/Incorporador | Arthen Engenharia e Construções LTDA |
| Localização | Ruas 418 e 420, Bairro Morretes, Itapema/SC |
| Tipo | Edifício Residencial Multifamiliar e Comercial (Interesse Social) |
| Padrão | Médio |
| Status | Paramétrico V2 gerado |

---

## 2. DOCUMENTOS RECEBIDOS

| # | Arquivo | O que foi extraído |
|---|---------|-------------------|
| 1 | MORRETES - RUA 418 - MEMORIAL DESCRITIVO.pdf | AC, UR, VAG, ELEV, pavimentos, laje, fundação, acabamentos |
| 2 | 8 PDFs arquitetônicos (pré-executivo R01, 16/03/2026) | Plantas tipo, cortes, rooftop |
| 3 | IFC Modelo Federado R02 (16/03/2026) | Modelo 3D |

---

## 3. DADOS DO PROGRAMA

| Variável | ID | Valor | Fonte |
|----------|----|-------|-------|
| Área Construída Total | AC | 12.472,98 m² | Memorial p.1 |
| Área do Terreno | AT | 1.008,00 m² | Memorial p.1 |
| Unid. Residenciais | UR_H | 90 | Memorial p.1 |
| Unid. Comerciais | UR_C | 8 | Memorial p.1 |
| Total Unidades | UR | 98 | Memorial p.1 |
| Nº Total Pavimentos | NP | 20 | Memorial p.1-2 (contagem) |
| Nº Pavimentos Tipo | NPT | 15 (14 tipo + 1 diferenciado) | Memorial p.2 |
| Nº Pav. Garagem | NPG | 3 (G1, G2, G3) | Memorial p.1-2 |
| Elevadores | ELEV | 2 (1 social + 1 emergência) | Memorial p.1 |
| Vagas | VAG | 99 | Memorial p.1 |
| Nº Torres | — | 1 | Memorial p.1 |
| Prazo de Obra | — | 30 meses | Definido com Leo (09/04/2026) |

---

## 4. BRIEFING RESPONDIDO

| # | Pergunta | Resposta | Fonte |
|---|----------|----------|-------|
| Q1 | Fundação | Hélice contínua | Memorial p.3 |
| Q2 | Tipo de Laje | Mista (concreto armado) | Memorial p.3 |
| Q3 | Contenção | Não mencionada | — |
| Q4 | Subsolos | 0 (garagens = mezaninos) | Memorial p.1-2 |
| Q5 | Padrão Acabamento | Médio | Memorial p.1 |
| Q6 | Esquadrias | Alumínio pintura eletrostática | Memorial p.4 |
| Q7 | Pisos | Porcelanato 60x60 + Laminado | Memorial p.4 |
| Q8 | Vedação | Alvenaria convencional | Memorial p.3 |
| Q9 | Forro | Gesso acartonado c/ negativo | Memorial p.3-4 |
| Q10 | Fachada | Textura + pintura acrílica | Memorial p.6 |
| Q16 | Lazer | Completo (piscina×2, academia, coworking, gourmet×2, ofurô, kids) | Memorial p.2 |
| Q25 | Pressurização | Sim (escada enclausurada) | Memorial p.1-2 |

### Dados adicionais:
- Concreto: fck min 20 MPa, aço CA-50/CA-60, formas pinho+compensado 17mm
- Hidro: PVC Tigre/Amanco, tanque séptico + filtro anaeróbio, medição individual
- Elevadores: 2 un, 8 pessoas (Atlas/Thyssen/Otis)
- GLP: central com medidores individuais (comodato)
- AC Split: só infra (dreno + ponto elétrico)
- Louças: apenas bacias sanitárias (sem cubas, torneiras, bancadas)

---

## 5. PARÂMETROS DO PARAMÉTRICO

| Parâmetro | Valor |
|-----------|-------|
| CUB/SC R-8N | R$ 3.028,45 (mar/2026) |
| Data-base | abr/2026 |
| Modelo | V2 bottom-up (126 projetos, 1.740 PUs) |
| Segmento | Médio 8-15k m² (12.473 m²) |

---

## 6. ENTREGÁVEIS

| Arquivo | Localização |
|---------|-------------|
| arthen-arboris-parametrico-v2.xlsx | `_Parametrico_IA/arthen-arboris/` (Drive) |
| arthen-arboris-memoria.md | `~/clawd/orcamento-parametrico/` (git) |

---

*Gerado em 09/04/2026 por Jarvis (Claude Code)*
