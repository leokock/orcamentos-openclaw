# Audit Report — thozen-electra

_Gerado em 13/04/2026 às 18:05 (revisão profunda autônoma)_

## ✅ Resumo do audit

| Métrica | Valor |
|---|---|
| **Total** | R$ 137.520.937 |
| **R$/m²** | R$ 3.629 |
| AC | 37.893,89 m² |
| UR | 348 |
| Padrão | alto |
| **Itens detalhados (todos os mg)** | 260 |
| Macrogrupos preenchidos | 18/18 |
| Macrogrupos vazios | 0 |

## 📋 Detalhamento por macrogrupo

| Macrogrupo | Total | R$/m² | N itens | Confiança | Fonte |
|---|---|---|---|---|---|
| Gerenciamento | R$ 9.375.120 | R$ 247 | 5 | 🟢 Alta | calibrado (n=131) |
| Movimentação de Terra | R$ 814.935 | R$ 22 | 6 | 🟢 Alta | calibrado (n=58) |
| Infraestrutura | R$ 7.785.102 | R$ 205 | 18 | 🟢 Alta | calibrado (n=63) |
| Supraestrutura | R$ 26.147.355 | R$ 690 | 27 | 🟢 Alta | calibrado (n=56) |
| Alvenaria | R$ 6.338.226 | R$ 167 | 10 | 🟢 Alta | calibrado (n=130) |
| Impermeabilização | R$ 2.434.731 | R$ 64 | 7 | 🟢 Alta | calibrado (n=61) |
| Instalações | R$ 12.535.014 | R$ 331 | 30 | 🟢 Alta | calibrado (n=80) |
| Sistemas Especiais | R$ 11.161.568 | R$ 295 | 30 | 🟢 Alta | similares (n=4) |
| Climatização | R$ 1.933.304 | R$ 51 | 3 | 🟢 Alta | calibrado (n=18) |
| Rev. Interno Parede | R$ 4.620.860 | R$ 122 | 5 | 🟢 Alta | calibrado (n=61) |
| Teto | R$ 2.987.474 | R$ 79 | 6 | 🟢 Alta | calibrado (n=35) |
| Pisos | R$ 10.709.893 | R$ 283 | 30 | 🟢 Alta | calibrado (n=42) |
| Pintura | R$ 5.683.220 | R$ 150 | 14 | 🟢 Alta | calibrado (n=61) |
| Esquadrias | R$ 16.345.490 | R$ 431 | 23 | 🟢 Alta | calibrado (n=56) |
| Louças e Metais | R$ 1.893.698 | R$ 50 | 11 | 🟢 Alta | calibrado (n=21) |
| Fachada | R$ 6.879.243 | R$ 182 | 4 | 🟢 Alta | calibrado (n=33) |
| Complementares | R$ 7.947.445 | R$ 210 | 30 | 🟢 Alta | calibrado (n=57) |
| Imprevistos | R$ 1.928.261 | R$ 51 | 1 | 🟢 Alta | calibrado (n=23) |

## 🏊 Análise arquitetônica (Bloco 0)

**13 categorias detectadas** via leitura multi-camada (IFC + DXF + PDF)

| Item | Detectado |
|---|---|
| Piscina | ✓ Sim |
| Ofurô / SPA | ✓ Sim |
| Sauna | ✓ Sim |
| Academia | — Não |
| Quadra esportiva | ✓ Sim |
| Salão de festas | ✓ Sim |
| Gourmet | ✓ Sim |
| Churrasqueira | ✓ Sim |
| Playground/kids | ✓ Sim |
| Coworking | — Não |
| Pet | ✓ Sim |
| Bicicletário | ✓ Sim |
| Gerador | ✓ Sim |

## 🔍 Achados da revisão

### Quantitativos BIM já extraídos do projeto

O projeto Thozen tem dois sistemas com quantitativos completos extraídos do BIM:

**Sistema de AC** (`dxf-arcondicionado/quantitativos-processados-r05.md`):
- 80 evaporadoras + 117 condensadoras = 197 equipamentos
- Potência total: 1.656.000 BTU/h ≈ **138 TR**
- Distribuição: Térreo, Lazer, Pavimentos Tipo (×24)

**Sistema de Exaustão** (`dxf-exaustao/RESUMO-EXTRACAO.md`):
- 195 churrasqueiras
- 8 exaustores TCV 710 Berliner Luft (10.600 m³/h, 3,0 kW)
- 8 prumadas, 1.400-1.720 m de duto galvanizado
- Estimativa: R$ 1,1-1,8M

**Estes dados foram adicionados ao memorial executivo (`executivo-thozen-electra.docx`) e paramétrico (`parametrico-thozen-electra.docx`)** numa seção 9 nova com tabelas detalhadas e nota de coerência com o macrogrupo Climatização.

### Análise arquitetônica rica

O Bloco 0 detectou **13 categorias de lazer** via 9 IFCs + 17 DXFs:
- Piscina (Swimming Pool, Pool club, Kids Pool)
- Ofurô / SPA (Beauty SPA, SPA interno)
- Sauna
- Quadra (Mini quadra, Estar quadra)
- Salão de festas, Gourmet (Gourmet Club, Play & Gourmet Room)
- Churrasqueira (BBQ pizza bar, Fire place, Wine & Fire place — 195 churrasqueiras quantificadas)
- Playground, Pet (Praça pet), Bicicletário, Gerador

**Não detectou 'academia'** — provável falso negativo (o projeto tem 'Beauty SPA' e 'Estar quadra' mas não literal 'academia/fitness'). **Vale conferir manualmente** se há área de musculação.

### Escala extra (>25k m²) — segmento Extra da base

Total: R$ 137.520.937 / **R$ 3.629/m²**

Posicionamento no segmento Extra (>25k m²) da base:
- P10: R$ 1.604/m²
- P25: R$ 2.549/m²
- **Mediana: R$ 2.634/m²**
- P75: R$ 4.888/m²
- P90: R$ 5.219/m²

**Delta vs mediana: +37,8%** — mas ainda dentro do P75 (R$ 4.888). Coerente com padrão **alto** + multiplicadores diferenciais aplicados em Acabamentos (Pisos, Esquadrias, Louças, Pintura, Fachada). Para projeto alto-padrão de 38k m² em Porto Belo, R$ 3.629/m² é razoável.

### ✅ Coerência interna

Soma dos 18 macrogrupos confere com o total no RESUMO (R$ 137.520.937).

## 📁 Arquivos do pacote

- ✓ `gate-thozen-electra.xlsx` (15.334 bytes)
- ✓ `gate-thozen-electra-validado.xlsx` (16.310 bytes)
- ✓ `parametrico-thozen-electra.xlsx` (37.010 bytes)
- ✓ `parametrico-thozen-electra.docx` (40.365 bytes)
- ✓ `executivo-thozen-electra.xlsx` (45.672 bytes)
- ✓ `executivo-thozen-electra.docx` (40.367 bytes)
- ✓ `validacao-thozen-electra.md` (1.796 bytes)
- ✓ `analise-arquitetura.json` (90.911 bytes)
- ✓ `state.json` (2.709 bytes)

## 🎯 Próximos passos sugeridos

- Confirmar manualmente se há academia/fitness no projeto (Bloco 0 não detectou explicitamente)
- Revisar a seção 9 do memorial executivo com os quantitativos BIM
- Ajustar Climatização manualmente se necessário (BIM diz R$ 2-3M, calibrado deu R$ 1,9M)
- Validar sistemas especiais com base nas 13 categorias detectadas
- Copiar para `~/orcamentos/parametricos/thozen-electra/`
