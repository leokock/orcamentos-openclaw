# Briefing de Orçamento Paramétrico — Cartesian Engenharia

> **Instruções:** Preencher antes de gerar o paramétrico. Se não preenchido, o Jarvis pergunta ao Leo por prioridade de impacto.
> Campos 📐 = extraídos automaticamente do PDF/quadro de áreas.
> Campos ❓ = precisam de resposta humana (impactam >10% no resultado).
> **Template Excel:** `template-orcamento-parametrico.xlsx` — preencher abas DADOS_PROJETO e BRIEFING.

---

## 1. Identificação do Projeto

| Campo | Valor |
|-------|-------|
| Nome do projeto | |
| Cliente/Incorporadora | |
| Cidade/Região | |
| Estado | |
| Data-base dos preços (mês/ano) | |
| CUB referência (R$/m²) | |

---

## 2. Dados do Programa (📐 extraídos do PDF)

### Essenciais (sem esses não roda)

| Variável | ID | Valor | Unidade | Onde encontrar |
|----------|----|-------|---------|---------------|
| Área Construída Total | AC | | m² | Quadro de áreas — "Área Total Construída" |
| Nº Unidades Residenciais | UR | | un | Memorial / plantas tipo |
| Nº Total Pavimentos | NP | | un | Corte / memorial |
| Nº Pavimentos Tipo | NPT | | un | Plantas tipo |
| Nº Elevadores | ELEV | | un | Memorial / planta subsolo |
| Nº Vagas | VAG | | un | Quadro de áreas / planta subsolo |
| Área do Terreno | AT | | m² | Implantação |

### Importantes (melhoram precisão ~15%)

| Variável | ID | Valor | Unidade | Onde encontrar |
|----------|----|-------|---------|---------------|
| Área Projeção Torre | APT | | m² | Implantação — contorno da torre |
| Perímetro Projeção Torre | PPT | | m | Implantação — perímetro da torre |
| Área Projeção Embasamento | APE | | m² | Implantação — contorno total |
| Perímetro Proj. Embasamento | PPE | | m | Implantação — perímetro total |
| Nº Subsolos | NS | | un | Corte |
| Nº Pav. Embasamento | NPE | | un | Corte (subsolo + térreo + mezanino) |
| Prazo de Obra | — | | meses | Briefing com o cliente |

### Opcionais (enriquecem análise)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Pav. Tipo Diferenciados | NPD | | un |
| Nº Pavimentos Duplex | ND | | un |
| Churrasqueiras | CHU | | un |
| Área de Lazer | AL | | m² |
| Área de Subsolos | AS | | m² |
| Área Embasamento | AE | | m² |
| Locação da Obra | LC | | m |
| BDI aplicado | — | | × |

---

## 3. Perguntas Decisivas (❓ resposta humana)

> Ordenadas por impacto no custo. As 5 primeiras definem ~70% da variação.

### 🔴 Alto Impacto (perguntar PRIMEIRO)

**Q2. Tipo de Laje** ❓
> Impacto: ~15% na supraestrutura (maior macrogrupo)
- [ ] Cubetas (laje nervurada com cubetas plásticas) — *referência*
- [ ] Protendida — menor espessura, mais aço protendido
- [ ] Maciça — mais concreto, menos forma
- [ ] Cub. Protendida — cubetas + protensão
- [ ] Treliçada — mais forma, menos concreto
- [ ] Não definido → usar Cubetas como padrão

**Q5. Padrão de Acabamento** ❓
> Impacto: 30-40% em acabamentos e esquadrias
- [ ] Econômico (cerâmica, esquadrias simples)
- [ ] Standard (porcelanato padrão, alumínio anodizado)
- [ ] Alto Padrão (porcelanato retificado, pintura eletrostática)
- [ ] Super Alto Padrão (porcelanato 60×120+, pele de vidro, brises)
- [ ] Luxo (mármore, esquadrias importadas, automação completa)

**Q3. Contenção** ❓
> Impacto: 5-8% do custo total quando presente
- [ ] Não (terreno plano, sem vizinhos críticos)
- [ ] Cortina de estacas
- [ ] Muro de arrimo
- [ ] Solo grampeado
- [ ] Tirantes
- Se sim: extensão aprox. _______ m

**Q19. Prazo de Obra** ❓
> Impacto: direto nos custos indiretos (~R$ 50-80k/mês)
- [ ] 18 meses | [ ] 24 | [ ] 30 | [ ] 36 | [ ] 42 | [ ] 48

**Q4. Nº de Subsolos** ❓
> Impacto: +R$ 200-400/m² por subsolo (mov. terra + infra + impermeab.)
- [ ] 0 | [ ] 1 | [ ] 2 | [ ] 3 ou mais

### 🟡 Médio Impacto

**Q1. Tipo de Fundação**
- [ ] Hélice contínua (*referência*) | [ ] Estaca Franki | [ ] Tubulão | [ ] Sapata/Radier | [ ] Estaca raiz

**Q6. Tipo de Esquadria**
- [ ] Alumínio anodizado (*referência*) | [ ] Pintura eletrostática | [ ] PVC | [ ] Alto desempenho

**Q10. Tipo de Fachada**
- [ ] Textura + pintura (*referência*) | [ ] Cerâmica/Pastilha | [ ] ACM | [ ] Pele de vidro | [ ] Misto

**Q11. MO Fachada**
- [ ] Equipe própria (*referência*) | [ ] Empreitada (+20%)

**Q8. Vedação Interna**
- [ ] Alvenaria (*referência*) | [ ] Drywall (+80%) | [ ] Misto

**Q16. Nível de Lazer**
- [ ] Básico (salão + churrasqueira) | [ ] Completo (+ piscina, academia) | [ ] Premium (+ spa, rooftop)

### 🟢 Baixo Impacto (mas refinam o resultado)

**Q7. Piso** — Porcelanato | Cerâmica | Vinílico | Importado | Mármore
**Q9. Forro** — Estucamento | Gesso liso | Gesso negativo | Gesso sanca | Mineral
**Q12. Cobertura Habitável** — Não | Básica | Completa
**Q13. Aquecimento** — Gás indiv. | Central | Solar | Bomba calor | Sem
**Q14. Automação** — Mínimo | Básico | Completo | Premium
**Q15. Energia** — Sem | Solar comum | Solar completo
**Q17. Paisagismo** — Sem | Básico | Elaborado | Premium
**Q18. Mobiliário** — Sem | Básico | Completo | Decorado
**Q20. Região** — Interior SC | Litoral SC | Capital Floripa | Litoral SP | Capital SP-RJ

### ⚡ Infraestrutura Técnica (Sim/Não)

**Q21. Gerador?** → +15% em Sist. Especiais
**Q22. Subestação?** → +10% em Sist. Especiais
**Q23. Placas Fotovoltaicas?** → +10% em Sist. Especiais
**Q24. Infra Carro Elétrico?** → +5% em Instalações
**Q25. Pressurização Escada?** → +8% em Instalações

---

## 4. Workflow do Jarvis

### Ao receber pedido de paramétrico novo:
1. Extrair dados do programa (bloco 2) do PDF/planta
2. Preencher DADOS_PROJETO no template
3. Se briefing não veio: perguntar ao Leo na ordem de impacto (laje → padrão → contenção → prazo → subsolos)
4. Preencher BRIEFING no template
5. Template calcula automaticamente (3 camadas: Base × CUB × Briefing)
6. Enviar .xlsx + resumo no Slack

### Ao receber orçamento executivo real:
1. Extrair dados completos (ver ORCAMENTO-PARAMETRICO-WORKFLOW.md Fluxo 2)
2. Documentar em `<nome>-indices.md` (16 seções)
3. Registrar na base paramétrica
4. Atualizar `calibration-data.json`
5. Recalibrar após cada novo executivo processado (regra Leo 05/mar/2026)

---

## 5. Base Atual

- **18 projetos calibrados** no `calibration-data.json`
- **40+ projetos** na `BASE-CONHECIMENTO-PARAMETRICO.md` (alguns só parciais)
- **Faixas benchmark**: P10-P90 por macrogrupo, atualizadas com cada calibração
- **Quadrante**: 🟢3 Econômico, 🔵5 Médio, 🟡5 Alto, 🔴4 Luxo

---

*Template v2.0 — Atualizado: 05/03/2026 (25 perguntas, 14 abas, 18 projetos calibrados)*
