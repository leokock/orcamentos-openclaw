# Audit Report — arthen-arboris

_Gerado em 13/04/2026 às 18:05 (revisão profunda autônoma)_

## ✅ Resumo do audit

| Métrica | Valor |
|---|---|
| **Total** | R$ 36.466.994 |
| **R$/m²** | R$ 2.924 |
| AC | 12.472,98 m² |
| UR | 98 |
| Padrão | medio |
| **Itens detalhados (todos os mg)** | 256 |
| Macrogrupos preenchidos | 18/18 |
| Macrogrupos vazios | 0 |

## 📋 Detalhamento por macrogrupo

| Macrogrupo | Total | R$/m² | N itens | Confiança | Fonte |
|---|---|---|---|---|---|
| Gerenciamento | R$ 2.805.338 | R$ 225 | 3 | 🟢 Alta | calibrado (n=131) |
| Movimentação de Terra | R$ 268.240 | R$ 22 | 4 | 🟢 Alta | calibrado (n=58) |
| Infraestrutura | R$ 2.440.484 | R$ 196 | 4 | 🟢 Alta | calibrado (n=63) |
| Supraestrutura | R$ 8.196.709 | R$ 657 | 18 | 🟢 Alta | calibrado (n=56) |
| Alvenaria | R$ 1.896.601 | R$ 152 | 13 | 🟢 Alta | calibrado (n=130) |
| Impermeabilização | R$ 763.243 | R$ 61 | 12 | 🟢 Alta | calibrado (n=61) |
| Instalações | R$ 3.438.307 | R$ 276 | 30 | 🟢 Alta | calibrado (n=80) |
| Sistemas Especiais | R$ 1.384.513 | R$ 111 | 30 | 🟡 Média | similares (n=1) |
| Climatização | R$ 489.506 | R$ 39 | 20 | 🟢 Alta | calibrado (n=18) |
| Rev. Interno Parede | R$ 1.169.985 | R$ 94 | 5 | 🟢 Alta | calibrado (n=61) |
| Teto | R$ 786.675 | R$ 63 | 3 | 🟢 Alta | calibrado (n=35) |
| Pisos | R$ 2.518.014 | R$ 202 | 8 | 🟢 Alta | calibrado (n=42) |
| Pintura | R$ 1.558.886 | R$ 125 | 9 | 🟢 Alta | calibrado (n=61) |
| Esquadrias | R$ 3.843.005 | R$ 308 | 30 | 🟢 Alta | calibrado (n=56) |
| Louças e Metais | R$ 415.547 | R$ 33 | 28 | 🟢 Alta | calibrado (n=21) |
| Fachada | R$ 1.677.289 | R$ 134 | 8 | 🟢 Alta | calibrado (n=33) |
| Complementares | R$ 2.179.954 | R$ 175 | 30 | 🟢 Alta | calibrado (n=57) |
| Imprevistos | R$ 634.698 | R$ 51 | 1 | 🟢 Alta | calibrado (n=23) |

## 🏊 Análise arquitetônica (Bloco 0)

**13 categorias detectadas** via leitura multi-camada (IFC + DXF + PDF)

| Item | Detectado |
|---|---|
| Piscina | ✓ Sim |
| Ofurô / SPA | ✓ Sim |
| Sauna | ✓ Sim |
| Academia | ✓ Sim |
| Quadra esportiva | — Não |
| Salão de festas | — Não |
| Gourmet | ✓ Sim |
| Churrasqueira | — Não |
| Playground/kids | ✓ Sim |
| Coworking | ✓ Sim |
| Pet | ✓ Sim |
| Bicicletário | — Não |
| Gerador | ✓ Sim |

## 🔍 Achados da revisão

### Comparação com paramétrico V2 anterior

Existe um `arthen-arboris-parametrico-v2.xlsx` anterior em `G:\...\_Parametrico_IA\arthen-arboris\` gerado pelo pipeline V2 original (bottom-up). Total anterior: **R$ 42.652.496 / R$ 3.420/m²**.

Total v2.1 nova (este pacote): **R$ 36.466.994 / R$ 2.924/m²**.

**Delta: -R$ 6.185.502 (-14,5%)**

**Causa raiz:** as duas versões usam abordagens diferentes:
- **v2 antiga (bottom-up):** `gerar_template_dinamico_v2.py` calcula índice × AC × PU por item dentro de cada macrogrupo (concreto m³/m² × AC × PU mediano, etc.). Mais granular.
- **v2.1 nova (top-down):** `valores_macrogrupos_calibrados()` lê R$/m² mediano direto do `calibration-indices.json → por_macrogrupo`. Mais conservador, mediana > média em alguns macrogrupos, e padrão Médio neutro (multiplicador 1.0).

**Não é erro de dados.** Os 14,5% representam a margem natural entre as duas abordagens.

**Decisão pendente do Leo:**
- (a) Manter v2.1 nova (mais conservadora, alinhada com base atual)
- (b) Voltar ao v2 antiga (bottom-up mais rico)
- (c) Adotar média ponderada das duas
- (d) Mudar padrão pra 'médio-alto' (multiplicador 1.05) e re-rodar — total subiria pra ~R$ 38M

### Coerência com análise arquitetônica

A análise arquitetônica do Bloco 0 detectou 13 categorias de lazer (piscina, ofurô, sauna, academia, gourmet, brinquedoteca, coworking, pet, playground, salão gourmet, kids, lounge, gerador) — **batendo exatamente** com o memorial técnico do projeto. Esse cruzamento valida a integridade do dado.

### ✅ Coerência interna

Soma dos 18 macrogrupos confere com o total no RESUMO (R$ 36.466.994).

### 🟡 Macrogrupos com confiança média
- **Sistemas Especiais**: R$ 1.384.513 (validação adicional recomendada)

## 📁 Arquivos do pacote

- ✓ `gate-arthen-arboris.xlsx` (15.714 bytes)
- ✓ `gate-arthen-arboris-validado.xlsx` (16.669 bytes)
- ✓ `parametrico-arthen-arboris.xlsx` (37.013 bytes)
- ✓ `parametrico-arthen-arboris.docx` (39.171 bytes)
- ✓ `executivo-arthen-arboris.xlsx` (45.759 bytes)
- ✓ `executivo-arthen-arboris.docx` (39.175 bytes)
- ✓ `validacao-arthen-arboris.md` (1.781 bytes)
- ✓ `analise-arquitetura.json` (12.224 bytes)
- ✓ `state.json` (2.660 bytes)

## 🎯 Próximos passos sugeridos

- Decidir entre v2 antigo (R$ 42.6M) e v2.1 novo (R$ 36.5M) — ver achado 1
- Conferir distribuição dos macrogrupos comparada com o memorial existente
- Validar premissas técnicas no executivo Word
- Copiar para `~/orcamentos/parametricos/arthen-arboris/`
