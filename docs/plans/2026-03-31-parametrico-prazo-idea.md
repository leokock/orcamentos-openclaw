# Paramétrico de Prazo — Ideia Estratégica

**Data:** 2026-03-31
**Status:** 💡 Ideia documentada — aguardando maturação dos padrões pela equipe de planejamento
**Origem:** Análise da plataforma "Controle sua Obra" (controlesuaobra.com.br) + processo interno da Cartesian

---

## Conceito

Criar um **gerador de planejamento parametrizado** para obras — o equivalente do Paramétrico de Custo V2, mas para **prazo**.

**Fórmula conceitual:** `Duração = Índice de produtividade × Quantidade × Fatores do projeto`

Mesmo princípio do V2 de custo: dados históricos reais da Cartesian (260+ obras) alimentando um motor que gera output parametrizado.

---

## Referência de Mercado

**Controle sua Obra** (Curitiba, fundada 2022, ~9 pessoas):
- Plataforma SaaS com IA que gera cronograma em ~10 minutos
- Usuário insere dados básicos → IA cruza com banco de dados de obras → gera Gantt + Escadinha + Linha de Balanço
- Concorrente direto da Prevision no nicho de planejamento
- Diferencial: Last Planner System digitalizado + geração automática de cronograma
- Limitação: banco de dados genérico, sem profundidade de projeto real

**Alice Technologies** (mercado gringo): referência similar de AI construction scheduling.

---

## Vantagem Competitiva da Cartesian

A Cartesian já tem o processo documentado em 16 "Comandos" sequenciais:

1. **Comando 00** — Introdução aos processos do setor
2. **Comando 01** — Estudo de projeto/ambientação (análise arquitetura, estrutura, instalações, fachada)
3. **Comando 02** — Diagrama de rede padrão e atualização
4. **Comando 03** — Análise de reunião e ajustes diagrama de rede
5. **Comando 04** — Diagrama de rede final
6. **Comando 05** — Abertura de serviços (EAP planejamento)
7. **Comando 06** — Lançamento dos serviços (Prevision)
8. **Comando 07** — Linha de balanço em Excel
9. **Comando 08** — Dimensionamento de equipes
10. **Comando 09** — Lançamento de durações
11. **Comando 10** — Balanceamento e finalização
12. **Comando 11** — Extração de curvas físicas
13. **Comando 12** — Histograma de equipes
14. **Comando 13** — Desenvolvimento da apresentação
15. **Comando 14** — Validação interna
16. **Comando 15-16** — Apresentação ao cliente + envio

**Ativos existentes:**
- `_Padrões/EAP padrão - MACRO EXCEL PAVS.xlsm` — EAP padrão parametrizável
- Diagrama de rede padrão (template base)
- Notas de adaptação por projeto (ex: Gran Royal — contenção, fundação, estrutura, instalações)
- Estudo de projeto padronizado (Comando 01)
- Plataformas: Prevision + MS Project + Sienge

---

## O Que Fazer (Quando For a Hora)

### Fase 1 — Consolidar os padrões (equipe de planejamento — EM ANDAMENTO)
- Refinar Comandos 01-05 com mais projetos
- Padronizar o diagrama de rede base com variações por tipologia
- Documentar produtividades e durações reais por tipo de serviço/obra
- Criar banco de dados estruturado de parâmetros (tipo: fundação, laje, contenção, fachada, etc.)

### Fase 2 — Parametrizar
- Mapear os parâmetros do Comando 01 (estudo de projeto) como inputs do sistema
- Cruzar com EAP padrão + durações históricas = EAP sugerida com durações
- Gerar diagrama de rede automaticamente baseado nos inputs
- Similar ao V2 de custo: dropdowns → índices → output

### Fase 3 — Automatizar (gerador)
- Script/plataforma que recebe briefing → gera:
  - EAP sugerida
  - Diagrama de rede adaptado
  - Cronograma Gantt com durações parametrizadas
  - Linha de balanço preliminar
  - Dimensionamento de equipes estimado
- Engenheiro refina (mesmo modelo do CSO: "IA gera esqueleto, humano refina")

### Fase 4 — Integrar com Paramétrico de Custo
- Cronograma físico-financeiro automático: custo V2 + prazo parametrizado
- Curva S integrada (escopo + custo + prazo)
- O "santo graal" da Cartesian: gestão integrada parametrizada

---

## Pré-requisitos

- [ ] Equipe de planejamento refinar e estabilizar os padrões atuais (Comandos 01-05)
- [ ] Acumular mais projetos de planejamento documentados no novo formato
- [ ] Estruturar banco de dados de produtividades/durações reais
- [ ] Definir tipologias de obra (residencial vertical, comercial, misto, etc.) com variações

---

## Notas

- **Não implementar agora** — primeiro deixar a equipe amadurecer o processo manual
- Quando os padrões estiverem estáveis e testados em ~5-10 projetos, aí parametrizar
- A base de 260+ obras da Cartesian é o diferencial brutal vs CSO (banco genérico)
- Conversar com equipe de planejamento sobre estruturar os dados de forma que facilite a parametrização futura
