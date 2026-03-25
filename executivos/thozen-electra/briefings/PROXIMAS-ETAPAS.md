# 🔧 Próximas Etapas — PCI Thozen Electra

## Status Atual
✅ Extração automatizada de IFCs concluída (R00)  
⚠️ Dados insuficientes para orçamento completo  
❌ Equipamentos críticos não identificados

---

## 1️⃣ Validação de Dados (URGENTE)

### Perguntar ao Leo/Cliente:

1. **Arquivos adicionais:**
   - [ ] Existe arquivo IFC de equipamentos PCI separado?
   - [ ] Existe memorial descritivo do sistema de incêndio?
   - [ ] Projeto foi aprovado pelo corpo de bombeiros? (se sim, solicitar cópia)
   - [ ] Existem pranchas de casa de bombas / reservatórios?

2. **Sistema de sprinklers:**
   - [ ] O edifício exige sprinklers? (altura, uso, código local)
   - [ ] Se sim, onde está o projeto de sprinklers? (IFC separado? DWG? Memorial?)

3. **Equipamentos hidromecânicos:**
   - [ ] Especificação de bombas disponível? (vazão, potência, pressão)
   - [ ] Capacidade dos reservatórios definida? (inferior/superior)
   - [ ] Fornecedor/fabricante já especificado?

---

## 2️⃣ Análise Manual de Pranchas DWG

### Objetivo: Validar metragens e extrair dados faltantes

**Pranchas a processar:**
- `348 - IGC 01 [08] rev.00 - 01° PAVTO. TÉRREO (T.A).dwg`
- `348 - IGC 02 [08] rev.00 - 01° PAVTO. TÉRREO (T.B).dwg`
- `348 - IGC 03 [08] rev.00 - 02°~06° PAVTO. GARAGEM 01~05 (T.A).dwg`
- `348 - IGC 04 [08] rev.00 - 02°~06° PAVTO. GARAGEM 01~05 (T.B).dwg`
- `348 - IGC 05 [08] rev.00 - 07° PAVTO. LAZER (T.A).dwg`
- `348 - IGC 06 [08] rev.00 - 07° PAVTO. LAZER (T.B).dwg`
- `348 - IGC 07 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.A).dwg`
- `348 - IGC 08 [08] rev.00 - 08º~31° PAVTO. TIPO (24x) (T.B).dwg`

**Dados a extrair:**
1. **Metragens de tubulação por diâmetro:**
   - Verificar se toda rede é Ø150mm ou se há variações
   - Quantificar prumadas, ramais, anéis
   - Confirmar comprimentos totais (espera-se >> 67m)

2. **Detalhes dos abrigos:**
   - Comprimento de mangueira (25m ou 30m)
   - Tipo de esguicho (regulável, agulheta)
   - Componentes do kit (engate rápido, chave, adaptador)

3. **Equipamentos:**
   - Identificar casa de bombas na prancha
   - Verificar se há indicação de reservatórios
   - Buscar notas de especificação de equipamentos

4. **Sinalização:**
   - Placas de "Hidrante"
   - Placas de saída de emergência
   - Rotas de fuga, faixas fotoluminescentes

**Método:**
- Abrir DWGs em AutoCAD/LibreCAD/DraftSight
- Buscar layers: HIDRANTE, PCI, INCENDIO, SPRINKLER
- Verificar blocos: abrigos, extintores, sprinklers, bombas
- Conferir legenda e notas nas pranchas
- Se houver tabela de quantitativos, extrair

---

## 3️⃣ Buscar Memorial Descritivo

### O que procurar:

1. **Memorial de Cálculo:**
   - Vazão de projeto (l/min)
   - Número de hidrantes simultâneos
   - Pressão mínima (mca)
   - Reserva técnica de incêndio (m³)

2. **Especificações de Equipamentos:**
   - Bomba principal: marca, modelo, vazão, potência, altura manométrica
   - Bomba jockey: idem
   - Reservatório: material (concreto, metálico), capacidade, localização
   - Tubulação: norma ASTM, schedule, classe de pressão

3. **Normas de Referência:**
   - NBR 13714 (hidrantes e mangotinhos)
   - IT/CB específica (Instrução Técnica do Corpo de Bombeiros local)
   - Outras normas aplicáveis

4. **Sistemas Adicionais:**
   - Sprinklers (se houver)
   - Detecção e alarme (se houver)
   - Iluminação de emergência (se for do escopo PCI)

---

## 4️⃣ Geração da Planilha Executiva

### Após validação dos dados:

**Estrutura da planilha:**
- Aba 1: N1 14.004.001 — Tubulação de Hidrantes
- Aba 2: N1 14.004.002 — Abrigos e Componentes
- Aba 3: N1 14.004.003 — Extintores Portáteis
- Aba 4: N1 14.004.004 — Sinalização de Emergência
- Aba 5: N1 14.004.005 — Reservatórios
- Aba 6: N1 14.004.006 — Bombas e Equipamentos
- Aba 7: N1 14.004.007 — Casa de Bombas (civil)
- Aba 8: (se houver) N1 14.004.008 — Sistema de Sprinklers

**Colunas padrão:**
- Código Memorial (N2/N3)
- Descrição
- Especificação Técnica
- UN
- QTD
- Preço Unitário
- Total
- Observação

**Formatação:**
- Separação visual por N2 (cor de fundo)
- Subtotais por N3
- Total geral por aba
- Resumo final consolidado

---

## 5️⃣ Precificação

### Fontes de preço sugeridas:

**Itens de construção civil:**
- SINAPI (tubos, conexões, mão de obra)
- SICRO (se for obra pública)

**Equipamentos especializados:**
- Cotação com 3 fornecedores:
  - Fornecedor A: [nome]
  - Fornecedor B: [nome]
  - Fornecedor C: [nome]
- Usar média ou menor preço (documentar critério)

**Serviços especializados:**
- Instalação de bombas: composição SINAPI + taxa de especialização
- Teste hidrostático: composição específica
- Comissionamento: % sobre equipamentos

**Itens críticos para cotar:**
- Kit completo de abrigo de hidrante (mangueira + esguicho + chave + caixa)
- Bomba principal PCI c/ motor elétrico
- Bomba jockey c/ pressostato
- Quadro de comando automático
- Reservatório (se metálico)

---

## 6️⃣ Revisão e Entrega

### Checklist final:

- [ ] Metragens validadas (comparar IFC vs DWG vs memorial)
- [ ] Todos os equipamentos especificados (marca, modelo, potência)
- [ ] Reservatórios dimensionados (capacidade, localização)
- [ ] Bombas especificadas (vazão, pressão, potência)
- [ ] Sprinklers incluídos (se existir)
- [ ] Sinalização completa (hidrantes, saídas, rotas)
- [ ] Preços atualizados (data-base, índice de reajuste)
- [ ] Planilha formatada (padrão Memorial Cartesiano)
- [ ] BDI aplicado (se for o caso)
- [ ] Revisão técnica (engenheiro responsável)

### Arquivos a entregar:

1. Planilha Excel executiva (N1 14 Instalações Especiais)
2. Briefing técnico completo (este documento + anexos)
3. Memorial de cálculo (se elaborado)
4. Cotações de fornecedores (anexo)
5. Cronograma de execução (se solicitado)

---

## 🚨 Alertas de Risco

### Riscos técnicos identificados:

⚠️ **Metragem de tubulação:** 67m é claramente insuficiente — orçar com esse valor levará a **subprecificação crítica**

⚠️ **Bombas e reservatórios:** Representam 30-40% do custo total do sistema PCI — **NÃO orçar sem especificação**

⚠️ **Sprinklers:** Se obrigatório por norma/código e não foi identificado, **projeto pode estar incompleto**

⚠️ **Aprovação corpo de bombeiros:** Se projeto não foi aprovado, pode haver revisões futuras que alteram quantitativos

### Recomendação:

**NÃO AVANÇAR para precificação final sem:**
1. Confirmar metragens reais (análise DWG manual)
2. Especificar bombas e reservatórios (memorial ou pranchas)
3. Confirmar se existe sistema de sprinklers

**Comunicar ao Leo:** "Dados insuficientes para orçamento completo. Necessário memorial descritivo ou pranchas de casa de bombas."

---

## 📞 Contatos Úteis

**Fornecedores PCI sugeridos:**
- [Nome Fornecedor 1] — Bombas e equipamentos
- [Nome Fornecedor 2] — Abrigos e mangueiras
- [Nome Fornecedor 3] — Sprinklers (se houver)

**Projetista responsável:**
- Nome: [a identificar nas pranchas]
- Empresa: [a identificar]
- Contato: [a obter]

---

*Documento gerado por Cartesiano | Atualizar conforme progresso | 2026-03-20*
