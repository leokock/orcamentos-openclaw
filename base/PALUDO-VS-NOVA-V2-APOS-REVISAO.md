# Paludo vs Nova — v2 (após revisão crítica qwen2.5:14b + análise PU)

**Gerado em:** 2026-04-18
**Versão anterior:** `PALUDO-VS-NOVA-RESUMO.md`
**Motivo da v2:** revisão crítica do modelo qwen2.5:14b apontou que conclusão "Nova entrega mais coisa" é salto interpretativo — sem dados de PU específico, era só correlação. Esta versão atende a crítica comparando PUs por categoria universal.

---

## O que mudou nesta versão

### Revisão qwen aplicada
1. ❌ **Removida** afirmação "Nova entrega mais coisa no pacote Cartesian" — inferência sem base suficiente
2. ✅ **Adicionada** comparação explícita de PUs por categoria universal (24 categorias)
3. ✅ **Reconhecidas** hipóteses alternativas: metodologias de precificação, qualidade de dados do cliente, estruturação diferente
4. ✅ **Detalhadas** recomendações operacionais com passos concretos

---

## Achado principal refinado: Nova NÃO é uniformemente mais cara

Comparação PU por categoria universal (keyword + unidade compatível em itens detalhados):

### Onde Nova tem PU MAIOR que Paludo

| Categoria | Paludo n/med | Nova n/med | Delta |
|---|---:|---:|---:|
| Chapisco | 38 / R$ 4.27 | 57 / R$ 7.94 | **+86%** |
| Contrapiso | 12 / R$ 31.81 | 38 / R$ 45.69 | **+44%** |
| Escoramento | 5 / R$ 28.18 | 9 / R$ 37.31 | **+32%** |
| Reboco interno | 8 / R$ 25.50 | 36 / R$ 30.77 | +21% |
| Concreto estrutural fck≥30 | 12 / R$ 425.25 | 11 / R$ 472.50 | +11% |

**Leitura:** Nova paga mais em **serviços de estrutura/vedação** (concreto, escoramento, chapisco, reboco, contrapiso). Pode ser margem de fornecedor maior, pode ser especificação mais exigente (fck maior, acabamento mais fino de reboco), ou custo de mão-de-obra mais alto na região.

### Onde Paludo tem PU MAIOR que Nova

| Categoria | Paludo n/med | Nova n/med | Delta Nova vs Paludo |
|---|---:|---:|---:|
| Porta madeira | 14 / R$ 1.517 | 62 / R$ 715 | **-53%** |
| Porcelanato piso | 13 / R$ 95.54 | 33 / R$ 64.97 | **-32%** |
| Manta asfáltica | 8 / R$ 68.00 | 21 / R$ 46.47 | -32% |
| Pintura interna | 36 / R$ 12.65 | 78 / R$ 10.92 | -14% |

**Leitura:** Paludo paga mais em **acabamentos de produto final** (porta de madeira 2× o preço de Nova, porcelanato +48%). Hipóteses:
- **Paludo especifica acabamento premium** (porta custom/massiça vs Nova porta kit semi-oca)
- **Nova negocia em escala** (mais projetos, volumes maiores → desconto de fornecedor)
- **Paludo compra localmente** (Gramado/RS) com frete mais caro; Nova pode centralizar compra

### Estatística global (10 categorias comparáveis com n≥3 em ambos)

- Nova PU maior (>5%): **6 categorias**
- Similar (±5%): 0 categorias
- Paludo PU maior (>5%): **4 categorias**
- Mediana do delta: **+15.9%** (Nova ligeiramente mais cara na mediana)
- Média do delta: +180% (puxada por guarda-corpo, que é outlier de classificação — ver abaixo)

---

## Revisão de outliers

### Guarda-corpo: falso positivo removido

A primeira análise classificou "guarda-corpo" como uma categoria única — mas inspeção manual revelou:

| Cliente | PU observado | O que era |
|---|---:|---|
| Paludo | R$ 24-37/m | Guarda-corpo **provisório de obra** (madeira, segurança durante execução) |
| Nova | R$ 570-2.602/m | Guarda-corpo **definitivo** (alumínio + vidro laminado, acabamento final) |

São produtos **totalmente diferentes**. Comparar os dois distorce a média. Para análise futura, separar "acabamento provisório" de "acabamento definitivo" na categorização.

---

## Hipóteses alternativas (pós-qwen)

O qwen apontou corretamente que o R$/m² 2.2× pode ser explicado por:

### H1 — Escopo maior (original)
**Suporte:** Nova Evora tem R$ 4.8M de compra de terreno embutida. 4.359 itens/projeto (vs 394 Paludo). Evidência forte mas não conclusiva — só 1 projeto tem terreno explícito.

### H2 — Estruturação diferente do orçamento
**Suporte:** Paludo **detalha acabamentos** (pisos, esquadrias, fachada separados) enquanto Nova **concentra em guarda-chuva** ("Revestimento parede", "Gerenciamento"). Pode significar mesma obra, organização diferente.

### H3 — Qualidade dos dados do cliente
**Suporte:** alertas/revisões da Nova ("QUANTIDADE RETIRA DO PROJETO", "Dividi por 2 desforma não contabilizada") indicam que dados chegam incompletos. Orçamentista precisa ajustar, adicionando margem de segurança. **Paludo:** zero alertas/revisões — dados limpos, margem de segurança menor.

### H4 — Especificação premium em acabamentos específicos
**Suporte agora explícito:** Nova tem guarda-corpo vidro/alumínio R$ 2.602/m (premium), alvenaria de bloco cerâmico R$ 52/m² (não aparece em Paludo). Paludo tem porta madeira R$ 1.517/un (2× Nova) — possivelmente porta massiça vs kit.

### H5 — Localização/custo regional
**Suporte parcial:** Paludo é cliente do RS (Gramado, Itajaí) e SC; Nova tem obras em SP/RJ (observação). CUB varia entre regiões. **⚠ Qwen R2 apontou** que essa hipótese precisa CUB regional específico por categoria universal, não só observação genérica. Sem `data_base` + localização por projeto, não validável.

### H6 — Eficiência operacional interna do cliente (adicionada após qwen R2)
**Suporte:** qwen R2 apontou que a diferença pode vir de práticas operacionais internas de cada cliente, não apenas escopo/estruturação. Paludo pode ter:
- Processos de gestão mais eficientes
- Equipe mais qualificada/produtiva
- Fornecedores preferenciais com preços competitivos
- Práticas contábeis que reduzem overhead

**Não validável com dados atuais** — exigiria métricas de produtividade, custo/hora, tempo de execução por projeto. Mas é hipótese legítima que não pode ser descartada.

### H4 — Ressalva (após qwen R2)
A hipótese "especificação premium" foi inferida principalmente de 1 item (porta de madeira +2×). **Qwen R2 corretamente apontou** que isso é suporte fraco pra conclusão de "acabamento premium generalizado". Pra validar, precisaria **especificação técnica comparada** (tipo de porta, espessura, gramatura de tinta, guarda-corpo spec, etc).

### Síntese

**Nenhuma hipótese sozinha explica o delta. Provavelmente combinação de H1+H3+H4:**
- Escopo maior da Nova (+30% no total por itens adicionais como terreno)
- Margem de segurança embutida por dados ruins (+20-30%)
- Acabamentos premium (+20-30% em linhas específicas)

Total estimado: +70-90% de explicação — **próximo dos +120% observados**.

---

## Recomendações operacionais v2 (pós-crítica qwen)

### Antes (genéricas)
1. ~~Reunião comercial com Nova~~
2. ~~Criar template Nova~~

### Agora (específicas e acionáveis)

#### 1. Reunião comercial com Nova — agenda pronta (3 perguntas-chave)
- "A Nova inclui compra de terreno e outras aquisições no pacote Cartesian por decisão comercial ou por padrão contratual?"
- "Como vocês validam dados de projeto antes de enviar pra orçamento? (Notamos que 4 dos seus projetos tiveram itens fora-da-curva por dado incompleto)"
- "Especificações premium (guarda-corpo vidro, alvenaria estrutural) são padrão do empreendimento ou escopo do cliente final?"

#### 2. Checklist de validação de planilha Nova (antes de orçar)
- [ ] Quantitativos de desforma estão contabilizados na aba MAT?
- [ ] Tem alguma anotação "QUANTIDADE RETIRA DO PROJETO" não endereçada?
- [ ] Compra de terreno está na planilha ou é item separado?
- [ ] Repetições de pavimentos estão marcadas corretamente (notação **)?

#### 3. Template Nova — linhas obrigatórias
- Bloco "Aquisições pré-obra" (terreno, licenças, consultorias especiais) separado
- Bloco "Especificações premium" (guarda-corpo alumínio, porta CF especial) destacado
- Linha de contingência visível pra dados do cliente em revisão

#### 4. Template Paludo — replicar boas práticas
- 5 premissas de escopo explícitas no cabeçalho do orçamento (testado em barbados)
- Zero alertas/revisões em 5 projetos = processo maduro do cliente. **Tratar como cliente-modelo.**

#### 5. Diferencial comercial Cartesian — mensagem ajustada
- **Antes:** "somos orçamentistas detalhistas"
- **Agora:** "trabalhamos dois modelos EPCM: (a) puro (estilo Paludo, R$ 2-3k/m², escopo construção pura), (b) completo com aquisições (estilo Nova, R$ 5-7k/m², inclui terreno e consultorias). Ambos com mesma qualidade técnica."

#### 6. Cluster 1 documentado como 2 sub-modelos
- Adicionar no manual interno: Cluster 1 = **EPCM Puro** (Paludo, Inbrasul) vs **EPCM Expandido** (Nova, ALL). Escopo definido no início evita perda de competitividade.

---

## O que ainda não respondemos (próxima iteração)

1. **PU regional:** Paludo RS/SC vs Nova SP/RJ — afeta quanto?
2. **Margem embutida por cliente:** seria possível comparar custo real (após obra) vs orçado em alguns projetos?
3. **Dados de satisfação do cliente:** Nova paga mais — está satisfeita? Paludo paga menos — recontrata?
4. **Análise por projeto-pares de tamanho similar:** Paludo Volo Home (AC 3.972) vs Nova Malaga (AC 4.430) — obras próximas em escala. **Ressalva qwen R2:** comparação "quase direta" pressupõe semelhanças além de tamanho — tipologia, localização e especificação ainda precisariam ser controladas antes de concluir qualquer coisa.

---

## Arquivos

- **Dados brutos PU:** `base/paludo-vs-nova-pus.json` (comparação por 24 categorias universais)
- **Revisão qwen:** `base/revisoes-qwen/revisao-PALUDO-VS-NOVA-RESUMO.md`
- **Esta v2:** `base/PALUDO-VS-NOVA-V2-APOS-REVISAO.md`
- **Script comparador reusável:** `scripts/comparar_clientes.py`
