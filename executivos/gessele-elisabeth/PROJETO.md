# Elizabeth II Royal Home - Gessele Empreendimentos

## Informações Gerais

- **Cliente:** Gessele Empreendimentos
- **Projeto:** Elizabeth II Royal Home
- **Sistema de gestão:** Memorial Cartesiano (Ampli)
- **Escopo Cartesian:** Orçamento executivo, composições, importação no sistema

---

## Orçamento Executivo

### Estrutura do orçamento (planilha original: `orçamento elisabeth.xlsx`)
- **Planilha:** `Ger_Executivo_Cartesian`
- **23 Células Construtivas** (N1): Movimentação de Terra, Contenção, Infraestrutura, Supraestrutura, Alvenarias, Instalações Elétricas, Hidrossanitárias, etc.
- **185 Etapas** (N2)
- **781 Subetapas** (N3)
- **1.489 Serviços** (N4)

### Composições

**Importação inicial (27/fev/2026):**
- Planilha original da Gessele (`Gessele composição.xlsx`) convertida para formato hierárquico do sistema
- Formato: sheet CPU com Etapa/Subetapa/Serviço/Insumo → convertido para SERVIÇO + INSUMO com Grupo
- 717 composições importadas na primeira leva

**Segunda importação (27/fev/2026):**
- Cruzamento identificou 60 serviços únicos sem composição (366 ocorrências)
- Gerado `composicoes-faltantes-elisabeth.xlsx` com composições simplificadas (1 insumo = mesmo nome, qtd 1, valor = preço unitário do orçamento)
- 56 das 60 composições importadas com sucesso

**Status final das composições:**
- **773 composições cadastradas** no sistema (arquivo: `composicoes (1).xlsx`)
- **1.472 serviços** do orçamento com composição vinculada
- **4 composições pendentes** (valor R$ 0 na origem, não importadas)

### Composições pendentes de cadastro

| Serviço | EAPs | Grupo | Motivo pendente |
|---------|------|-------|-----------------|
| Cisterna | 07.001.003.001 | Instalações Hidrossanitárias | Valor R$ 0 na origem |
| Reservatórios | 07.001.005.001 | Instalações Hidrossanitárias | Valor R$ 0 na origem |
| Tampo de Granito | 19.001 a 19.014.003.001 (14 ocorrências) | Louças e Metais | Valor R$ 0 na origem |
| Mobiliário e decoração | 22.002.002.001 | Serviços Complementares | Valor R$ 0 na origem |

**Ação necessária:** Levantar valores reais desses 4 serviços, criar composições e adicionar manualmente no sistema.

### Orçamento para importação

- **Arquivo gerado:** `orcamento-elisabeth-importacao.xlsx`
- **2.461 linhas** (excluídas as 17 ocorrências dos 4 serviços pendentes)
- **Todos os 1.472 serviços com código** de composição preenchido
- Formato: modelo hierárquico do sistema (Cód. referência, Nível, Código, Descrição, Quant., Und, Preço unit., Preço total)

---

## Arquivos Gerados

| Arquivo | Descrição | Data |
|---------|-----------|------|
| `composicoes-gessele-hierarquico.xlsx` | Conversão inicial das composições Gessele | 27/fev/2026 |
| `composicoes-faltantes-elisabeth.xlsx` | 60 composições faltantes (formato importação) | 27/fev/2026 |
| `composicoes-faltantes-4.xlsx` | 4 composições com valor 0 (não importadas) | 27/fev/2026 |
| `orcamento-elisabeth-importacao.xlsx` | Orçamento completo para importação no sistema | 27/fev/2026 |

---

## Próximos Passos

- [ ] Cadastrar as 4 composições pendentes (Cisterna, Reservatórios, Tampo de Granito, Mobiliário e decoração) com valores reais
- [ ] Importar orçamento no sistema (`orcamento-elisabeth-importacao.xlsx`)
- [ ] Após importar as 4 composições, adicionar os 17 serviços faltantes ao orçamento no sistema

---

*Última atualização: 27/fev/2026*
