# Relatório Final Noturno — 2026-04-13/14

_Loop autônomo overnight: Fases 14, 16 e 17 + revisão dos 3 pacotes reais._

## Sumário executivo

Conclusão de **TODAS as 17 fases** do roadmap. A base paramétrica V2 agora tem 3 camadas:

1. **Numérica** — calibration-indices.json + base-pus-cartesian.json + 29 índices derivados (já existia)
2. **Qualitativa Gemma** — sub-disciplinas, premissas, BDI, e (NOVO) observações completas das células
3. **Quantitativos físicos** — BIM/DXF/PDF extraídos diretamente do projeto, cross-referenciados aos PUs

## Fase 14 — Gemma sobre observações completas (NOVO)

- **Status:** 126/126 projetos concluídos
- **Tempo:** 170 min (10.206 s)
- **Modelo:** gemma4:e4b local
- **Output:** `base/observacoes-insights/[projeto].json` (126 arquivos, 824 KB)

| Métrica | Total | Média/projeto |
|---|---|---|
| Temas | 883 | 7.0 |
| Justificativas técnicas | 646 | 5.1 |
| Flags de risco | 179 | 1.4 |

Esta camada explica **por que** itens fugiram da mediana — é a fonte primária pra revisão de novos orçamentos contra a base.

## Fases 16a-d — Quantitativos físicos (NOVO)

Pipeline novo que extrai quantitativos físicos diretamente do projeto (independente do orçamento):

| Fase | Fonte | Lib | Status |
|---|---|---|---|
| **16a** | IFC (BIM) | ifcopenshell.geom (bbox 3D) | ✅ 3 projetos |
| **16b** | DXF | ezdxf | ✅ thozen 21 DXFs |
| **16c** | PDF | pypdf | ✅ placon 14 PDFs |
| **16d** | Consolidação | merge | ✅ 3 projetos |

**Inovação BIM v2:** ao detectar que os IFCs vinham com Pset_QuantityTakeOff vazios, troquei pra extração geométrica via `ifcopenshell.geom.create_shape` com bounding box. ~3ms por elemento, 0 dependência de QTOs.

**Output:**
- `quantitativos-bim/[projeto].json` (3 arquivos, 120 KB)
- `quantitativos-dxf/[projeto].json` (1 arquivo)
- `quantitativos-pdf/[projeto].json` (1 arquivo)
- `quantitativos-consolidados/[projeto].json` (3 arquivos, 40 KB)

## Fase 17 — Memoriais de extração (NOVO)

`gerar_memorial_extracao.py` consolida **tudo** num único memorial por projeto, fazendo cross-reference de cada item BIM/DXF/PDF contra os 4.210 PUs cross-projeto + 29 índices derivados.

| Projeto | Linhas | Arquivo |
|---|---|---|
| arthen-arboris | 425 | `base/pacotes/arthen-arboris/memorial-extracao-arthen-arboris.md` |
| placon-arminio-tavares | 375 | `base/pacotes/placon-arminio-tavares/memorial-extracao-placon-arminio-tavares.md` |
| thozen-electra | 421 | `base/pacotes/thozen-electra/memorial-extracao-thozen-electra.md` |

Cada memorial documenta: BIM (alvenaria/estrutura/esquadrias/ambientes/acabamentos), DXF/PDF complementar, e a lógica de extração de cada quantitativo. É a entrega final pedida: lista detalhada + memorial rastreável.

## Highlights por projeto

### Arthen Arboris
- **BIM:** 6.387 paredes (36.213 m² de bloco_ceramico_14cm), 10.746 reboco_2cm (60.096 m²)
- **Estrutura:** lajes/vigas/pilares com volumes capturados via bbox
- **Cross-ref:** todos os top itens da curva ABC mapeados contra PUs medianos da base

### Placon Armínio Tavares
- **PDF:** 14 documentos relevantes lidos (memoriais, NBR 12.721, quadros de áreas)
- **BIM + PDF combinados** validam áreas por pavimento

### Thozen Electra
- **DXF:** 21 arquivos lidos (1147 s) — texts/layers extraídos
- **BIM:** 9 IFCs (1.8 GB) processados em 193 s com bbox

## Estado dos 3 pacotes paramétricos

| Projeto | Total v2 | Audit bugs | Status |
|---|---|---|---|
| arthen-arboris | R$ 36,5 M (v2.1) | 2 (legítimos) | OK |
| placon-arminio-tavares | (calculado) | 0 | OK |
| thozen-electra | (calculado) | 0 | OK |

Bugs caíram de 19→2 após filtro `is_verba()` em `consulta_similares.enriquecer_executivo()`. Os 2 restantes são variações legítimas (qtd=1 + un=vb).

## Arquivos novos pra commit

- `base/observacoes-insights/*.json` (126 arquivos, Fase 14)
- `base/quantitativos-bim/*.json` (3 arquivos, Fase 16a)
- `base/quantitativos-dxf/*.json` (1 arquivo, Fase 16b)
- `base/quantitativos-pdf/*.json` (1 arquivo, Fase 16c)
- `base/quantitativos-consolidados/*.json` (3 arquivos, Fase 16d)
- `base/pacotes/{slug}/memorial-extracao-{slug}.md` (3 arquivos, Fase 17)
- `base/phase14-pipeline.log.jsonl`
- `base/FASES-FUTURAS.md` (atualizado)
- `base/CAMADA-QUALITATIVA-GEMMA.md` (atualizado)
- Este relatório

## Próximos passos sugeridos

1. **Validar memoriais** lendo Arthen/Placon/Thozen e marcando itens duvidosos
2. **Rodar 16a-d nos outros 123 projetos** (batch overnight, ~5h estimado)
3. **Revisão Arthen v2 vs v2.1** ainda pendente (R$ 42,6M → R$ 36,5M)
4. **Cópia pra Drive** dos 3 pacotes via `copiar_pacotes_drive.py --confirm`
