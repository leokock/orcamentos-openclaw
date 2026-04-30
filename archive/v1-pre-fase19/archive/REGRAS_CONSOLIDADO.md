# Orçamento Paramétrico — Regras de Negócio Consolidadas

> Extraído de: CTN-IVC-LRJ Gerenciamento Executivo R00
> 19 abas | 602 fórmulas | Gerado em 04/03/2026

---

## Arquitetura do Modelo

```
OBRA (dados brutos) → DADOS_INICIAIS (dicionário de variáveis) → 17 ABAS DE CUSTO
                                                                 → AUXILIAR (quantitativo esquadrias)
```

### Fórmula Universal
```
Valor Total = Quantidade × Preço Unitário × BDI (1.1)
```
Exceções: concreto adiciona fator de perda (×1.05 fundação rasa, ×1.30 estacas)

---

## Variáveis de Entrada (DADOS_INICIAIS)

| Sigla | Descrição | Unidade | Mais usada em |
|-------|-----------|---------|---------------|
| **AC** | Área Total Construída | m² | TODAS as abas (driver principal) |
| **APE** | Área de Projeção do Embasamento | m² | Fundações, Contenções, Mov. Terra |
| **APT** | Área de Projeção da Torre | m² | Supraestrutura, Alvenaria |
| **NP** | Nº Total de Pavimentos | un | Esquadrias, Supraestrutura |
| **NPT** | Nº Pavimentos Tipo | un | Supraestrutura, Alvenaria |
| **AL** | Área de Lazer | m² | Complementares |
| **UR** | Unidades Residenciais | un | Esquadrias, Sistemas Especiais |
| **CHU** | Churrasqueiras | un | Alvenaria, Sistemas Especiais |
| **PPT** | Perímetro Projeção Torre | m | Fachada |

---

## Índices Paramétricos por Grupo

### Fundações e Infraestrutura
| Serviço | Índice | Unidade | Base |
|---------|--------|---------|------|
| Nº estacas (fundação) | 0,14 | un/m² | APE |
| Nº estacas (cortina) | 0,15 | un/m² | APE |
| Forma blocos/baldrames | 1,1 | m²/m² | APE |
| Concreto blocos/baldrames | 0,6 | m³/m² | APE |
| Armação blocos/baldrames | 70 | kg/m³ | Vol. concreto |
| Forma parede contenção | 2,1 | m²/m² | APE |
| Concreto parede contenção | 0,65 | m³/m² | APE |
| Lastro concreto magro | 0,8 | m²/m² | APE |
| Escavação valas | 1,3 | m³/m³ | Vol. infra |

### Supraestrutura (5 variantes)
| Parâmetro | Maciça | Cubetas | Cub.Protend. | Treliçada | Protendida |
|-----------|--------|---------|--------------|-----------|------------|
| Jogos fôrma | 1 | 3 | 3 | 2 | 3 |
| Montagem (m²/AC) | 1,2 | 1,1 | 1,1 | 2,1 | 2,1 |
| Concreto (m³/AC) | 0,22 | 0,23 | 0,25 | 0,25 | 0,25 |
| Armadura (kg/m³) | 78 | 78 | 100 | 110 | 90 |
| MO (R$/AC) | 240 | 290 | 280 | 240 | 240 |

### Vedação e Acabamentos
| Serviço | Índice | Unidade | Base |
|---------|--------|---------|------|
| Alvenaria externa | 0,6 | m²/AC | AC |
| Alvenaria interna | 0,8 | m²/AC | AC |
| Contrapiso | ~0,62 | m²/AC | AC |
| Manta acústica | 80% | do contrapiso | Contrapiso |
| Forro (total) | 0,6 | m²/AC | AC |
| Estucamento | 0,2 | m²/AC | AC |
| Esquadrias alumínio | 0,15 | m²/AC | AC |
| PCF | 2 | un/NP | NP |
| Corrimão | 11 | m/NP | NP |

### Instalações (100% paramétrico R$/AC)
| Subgrupo | Índice Total | R$/m² AC |
|----------|-------------|----------|
| Elétrica | 153,50 | R$/AC |
| Hidrossanitária | 145,00 | R$/AC |
| Preventivas + GLP | 41,00 | R$/AC |
| **Total Instalações** | **339,50** | **R$/AC** |

### Verbas Paramétricas (R$/AC)
| Serviço | Índice | Aba |
|---------|--------|-----|
| Pintura interna geral | 75 | Pintura |
| Rev. parede (acabamento) | 45 | Acabamentos |
| Rodapés | 30 | Acabamentos |
| Textura escadas | 25 | Pintura |
| Soleiras e peitoris | 20 | Acabamentos |
| Limpeza | 15 | Complementares |
| Paisagismo | 11 | Complementares |
| Comunicação visual | 10 | Complementares |
| Serralheria | 5 | Esquadrias |
| Desmobilização | 5 | Complementares |
| Ligações definitivas | 4 | Complementares |
| Móveis/decoração | 1.500 R$/AL | Complementares |

---

## 3 Métodos de Quantificação

| Método | Descrição | Exemplos |
|--------|-----------|----------|
| **Índice × AC** | Quantidade proporcional à área construída | Forro, contrapiso, alvenaria, concreto |
| **Verba R$/AC** | Custo global proporcional | Pintura, rodapés, limpeza, instalações |
| **Levantamento direto** | Medido do projeto | Piscina, guarda-corpo, pele de vidro, fachada |

---

## Cadeia de Dependências

```
OBRA → DADOS_INICIAIS → TODAS as abas de custo
SUPRAESTRUTURA → CONTENÇÕES (MO ×1.5)
SUPRAESTRUTURA → INFRAESTRUTURA (MO ×1.5)
INFRAESTRUTURA → MOVIMENTAÇÃO DE TERRA (volumes de concreto)
ALVENARIA → REV. INTERNOS (chapisco = alvenaria×2 − fachada)
REV. INTERNOS → ACABAMENTOS PISO (porcelanato = contrapiso)
REV. INTERNOS → PINTURA INTERNA (epóxi = polimento)
ESQUADRIAS → REV. FACHADA (dedução de vãos)
SISTEMAS ESPECIAIS → ALVENARIA (nº churrasqueiras)
```

---

## Fatores de Custo

| Fator | Valor | Aplicação |
|-------|-------|-----------|
| BDI | 1,10 (10%) | **Universal** — todos os itens |
| Perda concreto (estacas) | 1,30 (30%) | Fundação profunda |
| Perda concreto (fundação rasa) | 1,05 (5%) | Blocos e baldrames |
| Perda concreto (superestrutura) | 1,05 (5%) | Todas as variantes de laje |
| Perda alvenaria escadas | 1,05 (5%) | Alvenaria convencional |
| Empolamento terra | 1,30 (30%) | Bota-fora |
| Fator dificuldade MO | 1,50 | Contenção e infraestrutura vs. supraestrutura |

---

## Obras de Referência (Calibração)

| Obra | Onde aparece | Índices calibrados |
|------|-------------|-------------------|
| **Passione** | Infraestrutura, Supraestrutura | Estacas 0,14 un/APE, montagem forma 0,98, concreto 23, armadura 93 |
| **Gran Torino** | Supraestrutura | Perfuração vigas R$ 160/un |
| **Connect Executivo** | Supraestrutura | Custos de protensão e cubetas protendidas |
| **Nova** | Supraestrutura | Perfuração vigas R$ 1.500/pav |
| **Celebration (Passe)** | Mov. Terra | Lastro concreto magro 0,8 m²/APE |

---

## Documentação Detalhada

Para regras completas de cada aba, consultar:
- `REGRAS_01_FUNDACOES.md` — Obra, Dados Iniciais, Mov. Terra, Contenções, Infraestrutura
- `REGRAS_02_ESTRUTURA_VEDACAO.md` — Supraestrutura, Alvenaria, Instalações, Sistemas Especiais, Impermeabilização
- `REGRAS_03_ACABAMENTOS.md` — Revestimentos, Teto, Acabamentos, Pintura, Esquadrias, Cobertura, Fachada, Complementares
