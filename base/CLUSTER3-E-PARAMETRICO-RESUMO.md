# Cluster 3 Deep-Dive + Validação Paramétrico

**Gerado em:** 2026-04-18
**Escopo:** investigação dos 13 projetos do Cluster 3 + cross-reference paramétrico ↔ executivo

---

## Parte 1 — Cluster 3: o segmento "Gerenciamento concentrado"

### Os 13 projetos

Agrupados por cliente, com % do total alocado em Gerenciamento:

| Cliente | N | Projetos | Ger % (faixa) | R$/m² | Observação |
|---|---:|---|---|---:|---|
| **Nova Empreendimentos** | 4 | Domus, Évora, Málaga, Malta | **32.7% → 64.0%** | R$ 5.2k–7.7k | Todos os 4 projetos da Nova na base caem aqui. Os mais caros. |
| **Paludo** | 4 | Barbados, Nassau, Volo Home, Volo Ocean | **33.8% → 37.5%** | R$ 2.7k–3.7k | Todos os 4 da Paludo aqui, mas R$/m² eficiente. |
| **Inbrasul** | 2 | Águas de Março, Opus | **32.2%** (idêntico!) | R$ 3.7k–3.8k | Ger % exatamente igual — mesmo contrato? |
| **ALL** | 1 | Lago di Garda | **58.1%** | R$ 7.2k | Maior Ger % absoluto. R$ 29M em gerenciamento. |
| **GDI** | 1 | Playa Negra | 33.2% | R$ 4.3k | — |
| **Grandezza** | 1 | Gran Royal | 34.3% | R$ 1.9k | Ger % alto + R$/m² baixo = projeto simples |

### Confirmação matemática: Cluster 3 vs Resto da base (63 projetos)

| Macrogrupo | Cluster 3 % | Resto % | Diferença |
|---|---:|---:|---:|
| **Gerenciamento** | **35.4%** | 12.4% | **+23.0 pp** ⚠ |
| Supraestrutura | 14.0% | 20.0% | -6.0 pp |
| Hidrossanitária | 2.7% | 6.3% | -3.6 pp |
| Pisos | 4.4% | 7.9% | -3.5 pp |
| Sistemas especiais | 2.7% | 5.4% | -2.7 pp |
| Infraestrutura | 3.9% | 6.0% | -2.1 pp |
| Alvenaria | 2.3% | 4.4% | -2.1 pp |
| _Todos os demais MGs_ | _reduzidos_ | _normais_ | _-1 a -2 pp_ |

**Padrão claro:** Gerenciamento absorve 23pp que em projetos normais se distribuem em custos diretos.

### Interpretação

**Hipótese mais forte:** Cluster 3 é a **assinatura de projetos EPCM/fee-based** da Cartesian — onde a empresa é remunerada com fee de gerenciamento (pacote executivo + gestão de obra), e esse fee é alocado integralmente em "Gerenciamento". Os custos diretos (material + MO direta) ficam com construtora/fornecedores ou em linhas macro.

**Duas evidências:**

1. **Nova Empreendimentos: 4/4 projetos no cluster**. Essa consistência sugere padrão de contratação próprio do cliente — talvez Cartesian atenda Nova com escopo fechado ou gestão completa.
2. **Inbrasul tem dois projetos com Ger% = 32.2% exatamente igual**. Quase certamente mesmo modelo de contrato, replicado.

**Contraste dentro do cluster:**
- **Nova + ALL + GDI** estão caros (R$ 4.3k–7.7k). Fee alto + escopo detalhado.
- **Paludo** está eficiente (R$ 2.7k–3.7k). Mesma estrutura contratual, escopo mais enxuto.
- **Grandezza Gran Royal** R$ 1.9k/m² com Ger 34% — projeto simples ou mal capturado.

### Ações comerciais recomendadas

1. **Criar linha de produto "EPCM Cartesian"** reconhecível internamente — 13 projetos já mostram demanda sistemática.
2. **Ficha "Nova Empreendimentos"**: padrão de contratação 40–64% em gerenciamento, R$/m² 5k–7.7k (alto+), 4 projetos registrados. Cliente fiel ao modelo.
3. **Ficha "Paludo"**: mesmo modelo EPCM, mas R$/m² 2.7k–3.7k. **Projetos menores (AC 1.4k–4k m²).** Paludo é referência de eficiência no modelo.
4. **Validar com Inbrasul** o motivo do 32.2% exato em dois projetos — pode ser contrato-padrão replicável com outros clientes.
5. **Revisar Grandezza Gran Royal** — R$ 1.9k/m² é muito baixo pra médio-alto; ou escopo foi parcial ou algo saiu fora.

---

## Parte 2 — Cross-reference paramétrico ↔ executivo

### Situação atual: 0 pares diretos

| Pacote paramétrico | Match em executivo | Motivo |
|---|---|---|
| arthen-arboris | ❌ | Cliente novo, sem executivo anterior |
| pacote-piloto | ❌ | Projeto sintético de teste |
| placon-arminio-tavares | ❌ | Cliente novo |
| thozen-electra | ⚠ parcial | thozen-mirador-de-alicante existe em executivo, mas é outro empreendimento |

**Razões:**
1. **Slug diverge** entre paramétrico e executivo quando mesmo projeto passa por ambos os fluxos.
2. Paramétricos atuais são **projetos novos em andamento** (nenhum virou executivo ainda).
3. Executivos antigos **não tiveram paramétrico** (base parametrica é posterior).

### Validação estatística possível (paramétrico vs nuvem de executivos do mesmo padrão)

| Pacote | AC | Padrão | R$/m² Param. | Mediana Exec | Desvio | Diagnóstico |
|---|---:|---|---:|---:|---:|---|
| arthen-arboris | 12.473 | médio-alto | R$ 3.349 | R$ 3.443 | **-2.7%** | 🟢 DENTRO da faixa |
| thozen-electra | 37.894 | alto | R$ 4.156 | R$ 4.188 | **-0.8%** | 🟢 DENTRO da faixa |
| pacote-piloto | 15.000 | alto | R$ 3.446 | R$ 4.188 | **-17.7%** | 🟡 ATENÇÃO (subestimado?) |
| placon-arminio-tavares | 4.090 | médio | R$ 2.976 | R$ 2.534 | **+17.4%** | 🟡 ATENÇÃO (superestimado?) |

**Leitura:**
- **arthen e thozen** estão quase exatamente na mediana do padrão — paramétrico está bem calibrado pra esses casos.
- **pacote-piloto** está 17.7% abaixo da mediana alto. Duas possibilidades: (a) o projeto piloto é intencionalmente simples dentro do padrão alto; (b) calibração V2 subestima alto padrão em projetos de ~15k m².
- **placon-arminio-tavares** está 17.4% acima da mediana médio. **Amostra de médio é pequena (n=2)** na base de executivos — baixa confiança no benchmark.

### Protocolo proposto para habilitar medição de erro

**Problema central:** sem pares diretos, só dá pra validar estatisticamente. Medir o erro real exige fechar o loop paramétrico → executivo com slug consistente.

**Protocolo operacional:**

| Etapa | Ação | Output |
|---|---|---|
| 1. Fechamento do paramétrico | Definir slug canônico no state.json (ex: `arthen-arboris`) | state.json estável |
| 2. Início do executivo | Reutilizar **o mesmo slug** em indices-executivo | `indices-executivo/arthen-arboris.json` |
| 3. Entrega do executivo | Rodar `scripts/comparar_param_exec.py --slug X` | Relatório de desvio por MG |
| 4. Registro git | Commit em `orcamentos-openclaw` mantendo pares rastreáveis | Histórico versionado |
| 5. Recalibração | A cada 5 pares, re-rodar `calibration-indices` | `indices-catalogo.xlsx` atualizado |

**Metas de cobertura:**

| N pares | Prazo | Critério |
|---:|---|---|
| 5 | 12 meses | Desvio médio < 15%, dp < 20% |
| 10 | 18 meses | Calibração confiável por padrão |
| 20 | 24 meses | Modelo preditivo de erro por MG |

**Script a criar:** `scripts/comparar_param_exec.py --slug X`
- Lê `base/pacotes/{slug}/state.json` (paramétrico)
- Lê `base/indices-executivo/{slug}.json` (executivo)
- Gera relatório MD com desvio por MG, itens a mais/menos, classificação DENTRO/ATENÇÃO/FORA

---

## Consolidado: insights deste documento

1. **Cluster 3 não é sobre tipo de obra — é sobre modo de contratação.** +23pp em gerenciamento = assinatura de EPCM/fee-based. Cartesian já tem 13 projetos nesse segmento, incluindo 100% dos projetos da Nova Empreendimentos.

2. **Paludo é o benchmark de eficiência dentro do EPCM.** Mesma estrutura de contrato, R$/m² 2.7k–3.7k vs 5k–7.7k da Nova.

3. **Paramétrico atual está bem calibrado para médio-alto e alto com projetos grandes** (arthen-arboris -2.7%, thozen-electra -0.8%). Ótimo sinal.

4. **Alerta pra médio padrão**: base estatística é fraca (n=2), cálibracao do placon pode estar enviesada.

5. **Sem par direto paramétrico↔executivo hoje.** Não dá pra medir erro real. Precisa protocolo de slug consistente.

6. **Recomendação imediata:** próximo paramétrico→executivo (arthen-arboris será o primeiro candidato natural) manter slug idêntico pra criar o primeiro par rastreável.

---

## Arquivos desta entrega

- **Excel:** `base/cluster3-e-parametrico.xlsx` (5 abas)
- **JSON:** `base/cluster3-e-parametrico-validacao.json`
- **Este resumo:** `base/CLUSTER3-E-PARAMETRICO-RESUMO.md`
- **Scripts:** `scripts/gerar_planilha_cluster3_parametrico.py`
