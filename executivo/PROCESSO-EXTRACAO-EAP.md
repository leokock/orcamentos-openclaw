# Processo de Extração de Quantitativos — EAP Aberta vs Fechada

*Documentação criada em: 11/mar/2025*

---

## Contexto

A extração de quantitativos de orçamentos executivos pode seguir dois fluxos distintos, dependendo da estrutura da planilha recebida:

- **EAP ABERTA:** Planilha com abas separadas por disciplina/macrogrupo (ex: Estrutura, Instalações, Esquadrias, etc.)
- **EAP FECHADA:** Planilha consolidada em uma única aba com estrutura hierárquica (ex: Ger_Executivo do projeto Estoril)

---

## FLUXO 1: EAP Aberta

### Características
- Planilha com **múltiplas abas**, uma por disciplina ou subdisciplina
- Exemplos de abas: "Supraestrutura", "INSTALAÇÕES", "ESQUADRIAS", "Visus-Alvenaria"
- Cada aba contém os itens daquela disciplina específica
- **Extração direta** — não precisa filtrar ou quebrar estrutura

### Processo (passo a passo)

#### 1. Receber Arquivo
- Time envia planilha `.xlsx` no Slack (canal ou thread)
- Time avisa: "já enviei o arquivo" ou similar
- **AÇÃO:** Executar imediatamente:
```bash
python3.11 scripts/slack_file_downloader.py --bot cartesiano --baixar --thread <thread_ts>
```

#### 2. Identificar Tipo de EAP
- Abrir planilha com openpyxl
- Listar nomes das abas
- Se tem abas tipo "Supraestrutura", "INSTALAÇÕES", "ESQUADRIAS" → **EAP ABERTA**
- Se tem apenas "Ger_Executivo" ou similar → **EAP FECHADA** (ir para FLUXO 2)

#### 3. Mapear Abas → Macrogrupos
Usar mapeamento da EAP Base (executivo/EAP-BASE.md):
- "Supraestrutura" → N1 05 Supraestrutura
- "INSTALAÇÕES", "HIDROSSANITÁRIO", "ELÉTRICO", "PCI" → N1 07 Instalações E/H/GLP/PCI
- "ESQUADRIAS" → N1 22 Esquadrias
- etc.

#### 4. Extrair Quantitativos por Aba
Para cada aba relevante:
1. Ler todas as linhas
2. Identificar estrutura de colunas (Descrição, UN, QTD, Preço Unit., Total)
3. Extrair itens folha (linhas com quantidade)
4. Calcular subtotais por seção
5. Gerar lista de itens com:
   - Código (se houver)
   - Descrição
   - Unidade
   - Quantidade
   - Observações relevantes (tipo de material, especificação, etc.)

#### 5. Organizar por Pavimento (se aplicável)
Se a planilha tiver quebra por pavimento dentro das abas:
- Identificar seções (Subsolo, Térreo, Tipo, Cobertura, etc.)
- Agrupar quantidades por célula construtiva
- Exemplo: "Concreto 30MPa — Laje Tipo (14 pav.) — 420m³"

#### 6. Gerar Planilha de Saída
Criar planilha Excel com abas por pavimento ou por disciplina, contendo:
- Uma aba "RESUMO" com totais por macrogrupo
- Abas por pavimento (se houver quebra) ou por disciplina
- Colunas: Macrogrupo | Disciplina | Descrição | UN | QTD | Observação

#### 7. Upload e Apresentação
```bash
python3.11 scripts/slack_uploader.py --bot cartesiano --file output/<arquivo>.xlsx --thread <thread_ts> --comment "Quantitativos extraídos — EAP Aberta"
```

Apresentar resumo no Slack:
- Total de itens extraídos
- Macrogrupos identificados
- Totais principais (ex: Concreto total, Aço total, Forma total)

---

## FLUXO 2: EAP Fechada

### Características
- Planilha com **uma única aba** consolidada (ex: "Ger_Executivo")
- Estrutura hierárquica com 5 níveis de endereçamento (ex: 3.5.4.3)
- Todos os macrogrupos, disciplinas e pavimentos na mesma aba
- **Extração complexa** — precisa filtrar e quebrar por critérios

### Estrutura de Níveis (padrão Estoril/Ger_Executivo)
- **Nível 1:** Unidade Construtiva (ex: Torre, Embasamento)
- **Nível 2:** Célula Construtiva (ex: Subsolo 1, Tipo 1...14, Cobertura)
- **Nível 3:** Etapa (corresponde ao N1 da EAP — Macrogrupo)
- **Nível 4:** Subetapa (corresponde ao N2/N3 — Disciplina/Subdisciplina)
- **Nível 5:** Serviço (item folha)

Exemplo de endereçamento: **3.5.4.3** = Unidade 3 → Célula 5 → Etapa 4 → Subetapa 3

### Processo (passo a passo)

#### 1. Receber Arquivo
Mesmo fluxo da EAP Aberta (baixar via slack_file_downloader.py)

#### 2. Identificar Tipo de EAP
- Abrir planilha
- Verificar estrutura de colunas
- Se tem coluna "Endereço" ou "Código" com padrão X.X.X.X → **EAP FECHADA**

#### 3. Mapear Níveis
Ler a planilha e identificar:
- Qual coluna contém o endereço hierárquico
- Qual coluna tem descrição, unidade, quantidade
- Identificar linhas de cabeçalho vs itens folha

#### 4. Extrair Estrutura Hierárquica
Criar árvore de navegação:
```
Torre (N1=3)
  ├─ Subsolo 1 (N2=1)
  │   ├─ 05 Supraestrutura (N3=5)
  │   │   ├─ Concreto (N4=1)
  │   │   │   └─ Concreto 30MPa Laje — 120m³ (N5)
  │   │   ├─ Forma (N4=2)
  │   │   └─ Aço (N4=3)
  ├─ Tipo 1...14 (N2=5)
  └─ Cobertura (N2=18)
```

#### 5. Filtrar por Critério
Dependendo da solicitação do time:

**a) Extração por Pavimento:**
- Filtrar todos os itens onde N2 = célula específica (ex: Tipo 1...14)
- Agrupar por macrogrupo (N3)
- Gerar planilha com quantitativos daquele pavimento

**b) Extração por Macrogrupo:**
- Filtrar todos os itens onde N3 = macrogrupo específico (ex: 05 Supraestrutura)
- Quebrar por pavimento (N2)
- Gerar planilha com quantitativos daquele macrogrupo

**c) Extração por Disciplina:**
- Filtrar por N3 (macrogrupo) + N4 (subdisciplina)
- Ex: N3=07 (Instalações) + N4=02 (Hidrossanitário)

#### 6. Agregação e Totalização
- Somar quantidades iguais (mesmo serviço em múltiplos pavimentos)
- Calcular subtotais por seção
- Identificar itens principais (top 10 por valor ou volume)

#### 7. Gerar Planilha de Saída
Estrutura similar à EAP Aberta, mas com colunas adicionais:
- Endereço Original (ex: 3.5.4.3)
- Unidade Construtiva
- Célula Construtiva (Pavimento)
- Macrogrupo
- Disciplina
- Descrição | UN | QTD | Observação

#### 8. Upload e Apresentação
```bash
python3.11 scripts/slack_uploader.py --bot cartesiano --file output/<arquivo>.xlsx --thread <thread_ts> --comment "Quantitativos extraídos — EAP Fechada (filtro: [critério])"
```

Apresentar resumo:
- Critério de filtro aplicado (ex: "Pavimento Tipo 1...14", "Macrogrupo 05 Supraestrutura")
- Total de itens extraídos
- Principais quantitativos
- Observações sobre a estrutura (ex: "14 pavimentos tipo agrupados")

---

## Comparação: Quando Usar Cada Fluxo

| Aspecto | EAP Aberta | EAP Fechada |
|---------|-----------|-------------|
| Estrutura do arquivo | Múltiplas abas por disciplina | Uma aba única hierárquica |
| Complexidade | Baixa — extração direta | Alta — precisa filtrar e quebrar |
| Tempo de processamento | Rápido (minutos) | Moderado (pode precisar validação manual) |
| Tipo de análise | Por disciplina → depois agregar por pavimento | Por pavimento → depois agregar por disciplina |
| Exemplo | Planilhas de projetos executivos por disciplina | Ger_Executivo consolidado (cronograma físico-financeiro) |

---

## Checklist de Validação (aplicável a ambos os fluxos)

Antes de entregar a planilha final:

1. ✅ Quantidades batem com o total da planilha original?
2. ✅ Unidades de medida corretas? (m³, m², kg, un)
3. ✅ Descrições preservam especificações importantes? (fck do concreto, bitola do aço, etc.)
4. ✅ Estrutura de pavimentos clara? (Subsolo, Térreo, Tipo, Cobertura, Barrilete)
5. ✅ Subtotais e totais conferem?
6. ✅ Observações relevantes documentadas? (repetições, agrupamentos, premissas)

---

## Próximos Passos

### Para EAP Aberta
✅ Processo documentado e validado

### Para EAP Fechada
⏳ Desenvolver script de extração com filtros configuráveis
⏳ Testar com planilha Ger_Executivo do Estoril
⏳ Validar mapeamento de níveis hierárquicos
⏳ Criar templates de saída por tipo de critério (pavimento, macrogrupo, disciplina)

---

*Documentação viva — será atualizada conforme novos casos de uso surgirem*
