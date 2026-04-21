# Diretriz de Extração — Thozen Electra Towers

> Documento de referência para padronizar a extração de quantitativos em todas as disciplinas deste projeto.

---

## Projeto
- **Nome:** Electra Towers
- **Cliente:** Thozen
- **Tipologia:** Residencial multifamiliar — 2 torres
- **Localização:** Porto Belo/SC
- **AC Total:** 36.089 m²
- **Unidades:** 348

---

## Unidades Construtivas (UCs)

| UC | Nome | Pavimentos | Observação |
|----|------|-----------|------------|
| UC1 | **Embasamento** | Térreo, G1, G2, G3, G4, G5, Lazer | Compartilhado — somar T.A + T.B |
| UC2 | **Torre A** | Tipo (×24), Casa de Máquinas, Pav. Técnicos | Exclusivo Torre A |
| UC3 | **Torre B** | Tipo (×24), Casa de Máquinas, Pav. Técnicos | Exclusivo Torre B |
| UC4 | **Geral** | Casa de Bombas, Infraestrutura externa | Itens compartilhados do edifício |

---

## Regras de Extração

### 1. Embasamento é compartilhado
- Térreo até Lazer (inclusive): quantitativos das duas torres são **somados** numa UC única
- Não separar por torre no embasamento
- Repetição = 1 (cada pavimento aparece 1x com a soma)

### 2. Torres são independentes
- Do Pavimento Tipo até Cobertura: extrair **separado** por torre
- Pavimento Tipo: 1 unidade × Repetição = 24
- Casa de Máquinas: 1 unidade × Repetição = 1
- Pavimentos Técnicos (Reservatórios + Cobertura): 1 unidade × Repetição = 1

### 3. Estrutura da planilha
```
Coluna A: UC (EMBASAMENTO | TORRE A | TORRE B | GERAL)
Coluna B: Pavimento
Coluna C: Grupo/EAP
Coluna D: Subgrupo
Coluna E: Descrição
Coluna F: Quantidade (unitária)
Coluna G: Repetição
Coluna H: Perda (%)
Coluna I: Qte com perda (fórmula)
Coluna J: Unidade
Coluna K: Custo unitário
Coluna L: Custo Total (fórmula)
```

### 4. Sequência obrigatória
```
EMBASAMENTO
  Térreo → G1 → G2 → G3 → G4 → G5 → Lazer
  [Subtotal Embasamento]

TORRE A
  Pavimento Tipo (×24) → Casa de Máquinas → Pav. Técnicos
  [Subtotal Torre A]

TORRE B
  Pavimento Tipo (×24) → Casa de Máquinas → Pav. Técnicos
  [Subtotal Torre B]

GERAL
  Casa de Bombas / Infraestrutura
  [Subtotal Geral]

TOTAL GERAL
```

### 5. Sem tabela pivot lateral
- Planilhas só com colunas A-L
- Sem colunas de resumo por pavimento ao lado
- Resumo, se necessário, em aba separada

### 6. Agrupamento por grupo/EAP dentro de cada pavimento
- Dentro de cada pavimento, agrupar itens por Grupo/EAP (ex: SHP, HIDRANTE, EXTINTORES, SINALIZAÇÃO)
- Subtotal por pavimento no final de cada bloco

---

## Pavimentos — Detalhamento

| Pavimento | Piso | UC |
|-----------|------|----|
| 1° | Térreo | Embasamento |
| 2° | Garagem 01 | Embasamento |
| 3° | Garagem 02 | Embasamento |
| 4° | Garagem 03 | Embasamento |
| 5° | Garagem 04 | Embasamento |
| 6° | Garagem 05 | Embasamento |
| 7° | Lazer | Embasamento |
| 8°-31° | Tipo (24×) | Torre A / Torre B |
| 32° | Casa de Máquinas | Torre A / Torre B |
| 33° | Reservatórios | Torre A / Torre B (Pav. Técnicos) |
| 34° | Cobertura | Torre A / Torre B (Pav. Técnicos) |

---

## Fontes de Dados por Disciplina

| Disciplina | Fonte Principal | Fonte Secundária | Status |
|-----------|----------------|------------------|--------|
| Estrutura | IFC rev.01 | DWGs | ✅ Concluído |
| Elétrico | IFC rev.01 | DXFs (18 pranchas) | ✅ R02 |
| Hidrossanitário | IFC H00 rev.01 | DXFs (20 pranchas) | ✅ R00 |
| PCI Civil | IFC PCI rev.01 | DXFs IGC (11 pranchas) | 🟡 R02 |
| PCI Elétrico | IFC | DXFs PEE (18 pranchas) | 🟡 Pendente |
| Telecomunicações | IFC rev.01 | DXFs (18 pranchas) | ✅ R01 |
| Ventilação Mecânica | DWG R05 | - | ⚠️ Estimativa |
| Ar-Condicionado | DWG R05 | - | 🔴 Pendente |
| Alvenaria | IFC ARQ | - | 🔴 Pendente |
| Louças e Metais | IFC H00 | - | ✅ R00 |

---

## Observações

- **Tubulação SHP do PCI:** Metragem extraída dos IFCs (67m) é subestimada. Usar DXFs ou memorial para validar.
- **Bombeamento PCI:** Não modelado nos IFCs — dados estimados ou a confirmar com projetista.
- **Material real PCI:** Ferro galvanizado (não cobre como no template Elizabeth II).

---

*Criado em: 25/03/2026*
*Atualizado em: 25/03/2026*
