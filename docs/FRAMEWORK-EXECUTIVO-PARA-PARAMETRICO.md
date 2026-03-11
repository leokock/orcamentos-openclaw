# Framework: Extração de Índices a partir de Orçamento Executivo

> Workflow padrão para converter orçamentos executivos em índices paramétricos + índices de produto + índices de consumo.
> Criado: 05/03/2026 | Atualizado: 05/03/2026
> **Template expandido:** `archive/TEMPLATE-INDICES-EXPANDIDO.md` (16 seções, ~24KB)

---

## QUANDO USAR

Sempre que Leo enviar:
- Orçamento executivo (planilha XLSX com custos diretos item a item)
- Apresentação de orçamento (PDF/PPTX com resumo, especificações, escopo)
- Ambos juntos (ideal)

---

## WORKFLOW

### Passo 1: Extração de Dados do Projeto
Identificar da apresentação/planilha:
- Localização (cidade/estado)
- Área Construída (AC)
- Unidades (UR)
- Nº Pavimentos (NP, NPT, NPG)
- Data-base do orçamento
- CUB de referência
- Prazo de obra
- Tipo de laje (cubetas, maciça, protendida)
- Padrão de acabamento

### Passo 2: Classificação nos Macrogrupos Paramétricos
Mapear cada item do executivo para os macrogrupos:

| # | Macrogrupo Paramétrico | Itens típicos do Executivo |
|---|---|---|
| 1 | Gerenciamento Técnico/Admin | Custos indiretos: projetos, taxas, equipe, EPCs, equipamentos, canteiro |
| 2 | Movimentação de Terra | Escavação, reaterro, bota-fora, lastro |
| 3 | Infraestrutura | Fundação profunda (estacas) + fundação rasa (blocos, baldrames) |
| 4 | Supraestrutura | Forma, armadura, concreto, cubetas/escoramento, MO estrutura |
| 5 | Alvenaria | Blocos cerâmicos, sical, drywall, vergas, encunhamento, churrasqueiras |
| 6 | Impermeabilização | Mantas, argamassa polimérica, proteção mecânica, regularização |
| 7 | Instalações | Hidrossanitárias + elétricas + preventivas + gás + comunicações (agrupado) |
| 8 | Sistemas Especiais | Elevadores, piscina (equipamentos), ETE |
| 9 | Climatização | Infra AC, equipamentos AC, exaustão |
| 10 | Rev. Internos Parede | Reboco (chapisco+massa), cerâmicos parede, peitoris/chapins granito |
| 11 | Teto | Forro gesso, negativo |
| 12 | Pisos e Pavimentações | Contrapiso, cerâmicos piso, laminado, rodapés, soleiras |
| 13 | Pintura | Epóxi piso, sistema parede (selador+massa+acrílica), teto |
| 14 | Esquadrias | Alumínio, guarda-corpo, pele de vidro, madeira, metálicas (PCF), brises |
| 15 | Louças e Metais | Louças, metais, bancadas granito |
| 16 | Fachada | Reboco externo, textura, pastilha, porcelanato, juntas, pintura externa |
| 17 | Complementares | Calçadas, mobiliário, paisagismo, limpeza, ligações, comunicação visual |
| 18 | Imprevistos | Contingência (% do total) |

### Passo 3: Extração de Índices Detalhados
Para cada macrogrupo, extrair:

#### Estruturais (Infra + Supra)
- Volume concreto (m³) e consumo/m² AC
- Peso aço (kg) e taxa (kg/m³)
- Área forma (m²) e índice/m² AC
- fck e preço/m³ do concreto
- Tipo e metragem de estacas
- Cubetas: tipo, quantidade/pavimento
- MO: R$/m² por tipo de laje

#### Instalações
- R$/m² AC por disciplina (hidro, elétrica, preventiva, gás, telecom)
- MO R$/m² AC por disciplina (quando disponível contrato)

#### Acabamentos (Rev. Parede, Piso, Teto, Pintura, Fachada)
- Áreas de revestimento (m²) e índice/m² AC
- Preços unitários de materiais (R$/m²)
- Preços de MO por serviço (R$/m²)
- Tipos de acabamento (porcelanato, laminado, pastilha, etc.)

#### Esquadrias
- Preço por tipo (alumínio, guarda-corpo, pele vidro, madeira, PCF, brise)
- Quantidade de portas e razão portas/UR
- Área de vidro e preço/m²

#### Sistemas Especiais
- Preço elevador por unidade
- Equipamentos piscina
- ETE

#### Custos Indiretos
- Equipe de gestão: cargos e custo/mês
- EPCs: tipos e preços
- Equipamentos: cremalheira, grua, balancins
- Canteiro: provisórias, consumo, segurança

### Passo 4: Gerar Arquivo de Índices (Template Expandido)
Copiar `archive/TEMPLATE-INDICES-EXPANDIDO.md` para `<nome-projeto>-indices.md` e preencher todas as 16 seções:

| Seção | Conteúdo | Fonte Principal |
|---|---|---|
| 1. Dados do Projeto | Ficha técnica completa | Apresentação + Obra |
| 2. Produto Imobiliário | AC/UR, CA, vagas/UR, mix tipologias | Obra + cálculo |
| 3. Macrogrupos Paramétricos | R$, R$/m², % — 18 grupos | Obra (resumo) |
| 4. Índices Estruturais | Concreto, aço, forma detalhados | Supraestrutura, Estacas, Fund. Rasa |
| 5. Índices de Consumo | m²/m² AC para cada serviço | Arquitetura, Ger_Executivo |
| 6. Instalações (breakdown) | R$/m² por disciplina + MO | HIDRO, SANIT, TEL, CLI, Ger_Executivo |
| 7. Acabamentos (PUs e MO) | Parede, piso, teto, pintura, fachada | CPU, Ger_Executivo |
| 8. Esquadrias | Por tipo + índices/UR | Arquitetura, Ger_Executivo |
| 9. Sistemas Especiais | Elevadores, gerador, piscina | Equipamentos Especiais |
| 10. CI Detalhado | Projetos, taxas, equipe, EPCs, equip. | Ger_Tec e Adm, MO, EPCs |
| 11. Louças e Metais | Qtd/UR, PUs | LOUÇAS E METAIS |
| 12. Produtividade/Prazo | m²/mês, burn rate, cronograma fases | Apresentação |
| 13. Impermeabilização | Por sistema, PUs | Ger_Executivo |
| 14. Complementares | Ambientação, paisagismo, etc. | Ger_Executivo, Lev. Complementar |
| 15. Benchmark (ADM PRELIMINAR) | Comparativo com outros projetos CTN | ADM PRELIMINAR |
| 16. Destaques e Alertas | Acima/abaixo da média, particularidades | Análise comparativa |

O template inclui colunas de referência (Ref. KIR e Ref. ADR) que se atualizam à medida que novos projetos são processados.

### Passo 5: Registrar na Base Paramétrica
Adicionar em `BASE-CONHECIMENTO-PARAMETRICO.md`:
- Linha na tabela de projetos
- Seção com macrogrupos (R$ e R$/m²)
- Índices-chave resumidos
- Referência ao arquivo de índices detalhado

### Passo 6: Apresentar ao Leo
Responder com:
1. Classificação executivo → paramétrico (tabela resumo)
2. Comparativo rápido com projetos similares da base
3. Destaques: onde está acima/abaixo da média e por quê
4. Confirmar registro na base

---

## ENTREGÁVEIS POR PROJETO

| Entregável | Localização | Conteúdo |
|---|---|---|
| Índices expandidos | `orcamento-parametrico/<projeto>-indices.md` | 16 seções: produto + paramétrico + consumo + CI + benchmark |
| Registro na base | `BASE-CONHECIMENTO-PARAMETRICO.md` | Macrogrupos + índices-chave resumidos |
| Classificação validada | Resposta no Slack | Tabela executivo → paramétrico pra Leo validar |
| Template fonte | `archive/TEMPLATE-INDICES-EXPANDIDO.md` | Referência com campos padronizados |

---

## NOTAS

- **Mapeamento é quase 1:1** na maioria dos executivos da Cartesian (EAP padronizada)
- **Instalações** sempre agrupar os 5 subgrupos (hidro, elétrica, preventiva, gás, telecom)
- **Climatização** manter separada de Sistemas Especiais
- **Churrasqueiras** vão dentro de Alvenaria (não em complementares)
- **Piso polido garagem** vai dentro de Supraestrutura (não em pisos)
- **Pintura epóxi garagem** vai dentro de Pintura (não em supraestrutura)
- Com cada projeto processado, o "de-para" fica mais calibrado
- Após 3-4 projetos, a classificação se torna quase automática
