# Briefing Paramétrico — Arminio Tavares (Placon)

**Data:** 09/03/2026  
**Fonte:** Extração IFC `PLA_ARM_ARQ_EP_R06.ifc`  
**Status:** Aguardando complemento de dados

---

## 1. Identificação do Projeto

| Campo | Valor |
|-------|-------|
| Nome do projeto | PLACON - ARMÍNIO TAVARES |
| Cliente/Incorporadora | PLACON EMPREENDIMENTOS IMOBILIÁRIOS LTDA |
| CNPJ | 10.226.625/0001-20 |
| Cidade/Região | Florianópolis, Centro |
| Estado | SC |
| Endereço | RUA DR. ARMÍNIO TAVARES |
| Zoneamento | ARM-12.5 |
| Inscrição Imobiliária | 52.03.008.0281.001.909 |
| Tipo | Residencial Multifamiliar |
| Data-base dos preços | mar/2026 |
| CUB referência (R$/m²) | ❓ (usar CUB SC atual) |

---

## 2. Dados do Programa

### Extraídos do IFC (📐)

| Variável | ID | Valor | Unidade | Fonte |
|----------|----|-------|---------|-------|
| Área do Terreno | AT | 486.4 | m² | Property Set "Construção" |
| Área Matrícula | — | 496.0 | m² | Property Set "Dados" |
| Área Atingimento Viário | — | 16.762 | m² | Property Set "Construção" |
| Nº Total Pavimentos | NP | 22 | un | Contagem IFC |
| Nº Pavimentos Tipo | NPT | 12 | un | Property Set "Construção" |
| Nº Subsolos | NS | 2 | un | IFC (Subsolo Baixo + Subsolo) |
| Altura Pavimento Padrão | — | 3.06 | m | Property Set "Construção" |
| Taxa de Ocupação Torre | TO | 36.4% | % | Property Set "Construção" |
| Taxa de Ocupação Subsolo | TOS | 100% | % | Property Set "Construção" |
| Coef. Aproveitamento | CA | 5.7 | × | Property Set "Construção" |
| CA Básico | — | 1.0 | × | Property Set "Dados" |
| CA Acréscimo Outorga | — | 3.98 | × | Property Set "Dados" |
| CA Acréscimo TDC | — | 0.72 | × | Property Set "Dados" |

### Cálculos Estimados

| Variável | ID | Valor | Unidade | Cálculo |
|----------|----|-------|---------|---------|
| Área Construída Total | AC | 2,772 | m² | 486.4 × 5.7 |
| Área Projeção Torre | APT | 177 | m² | 486.4 × 0.364 |
| Área Subsolo | AS | 486 | m² | 486.4 × 1.0 (por subsolo) |

### Composição do Edifício (IFC)

**Pavimentos identificados:**
- Subsolo Baixo (elev. -352mm)
- Subsolo -01 (elev. -290mm)
- 1º Pavimento (térreo, elev. 0mm)
- 2º ao 16º Pavimento (15 pav. tipo)
- Barrilete (elev. 4.356mm)
- Casa de Máquinas (elev. 4.456mm)
- Reservatório (elev. 4.756mm)
- Cobertura (elev. 5.006mm)

**Altura Total:** ~5.0m (até cobertura)

### Dados Faltantes (❓ perguntar ao Leo)

| Variável | ID | Valor | Unidade |
|----------|----|-------|---------|
| Nº Unidades Residenciais | UR | ❓ | un |
| Nº Elevadores | ELEV | ❓ | un |
| Nº Vagas | VAG | ❓ | un |
| Perímetro Projeção Torre | PPT | ❓ | m |
| Área Projeção Embasamento | APE | ❓ | m² |
| Perímetro Proj. Embasamento | PPE | ❓ | m |
| Nº Pav. Embasamento | NPE | ❓ | un |
| Prazo de Obra | — | ❓ | meses |
| Área de Lazer | AL | ❓ | m² |

---

## 3. Perguntas Decisivas

### 🔴 Alto Impacto (PERGUNTAR PRIMEIRO)

**Q2. Tipo de Laje** ❓
- [ ] Cubetas (laje nervurada com cubetas plásticas) — *referência*
- [ ] Protendida
- [ ] Maciça
- [ ] Cub. Protendida
- [ ] Treliçada
- [ ] Não definido → usar Cubetas

**Q5. Padrão de Acabamento** ❓
- [ ] Econômico
- [ ] Standard
- [ ] Alto Padrão
- [ ] Super Alto Padrão
- [ ] Luxo

**Q3. Contenção** ❓
- [ ] Não
- [ ] Cortina de estacas
- [ ] Muro de arrimo
- [ ] Solo grampeado
- [ ] Tirantes
- Extensão: _______ m

**Q19. Prazo de Obra** ❓
- [ ] 18 meses | [ ] 24 | [ ] 30 | [ ] 36 | [ ] 42 | [ ] 48

**Q4. Nº de Subsolos** ✓ **2 subsolos** (já extraído do IFC)

### 🟡 Médio Impacto

**Q1. Tipo de Fundação** ❓
- [ ] Hélice contínua | [ ] Estaca Franki | [ ] Tubulão | [ ] Sapata/Radier | [ ] Estaca raiz

**Q6. Tipo de Esquadria** ❓
- [ ] Alumínio anodizado | [ ] Pintura eletrostática | [ ] PVC | [ ] Alto desempenho

**Q10. Tipo de Fachada** ❓
- [ ] Textura + pintura | [ ] Cerâmica/Pastilha | [ ] ACM | [ ] Pele de vidro | [ ] Misto

**Q11. MO Fachada** ❓
- [ ] Equipe própria | [ ] Empreitada

**Q8. Vedação Interna** ❓
- [ ] Alvenaria | [ ] Drywall | [ ] Misto

**Q16. Nível de Lazer** ❓
- [ ] Básico | [ ] Completo | [ ] Premium

### 🟢 Baixo Impacto

**Q7. Piso** ❓ — Porcelanato | Cerâmica | Vinílico | Importado | Mármore

**Q9. Forro** ❓ — Estucamento | Gesso liso | Gesso negativo | Sanca | Mineral

**Q12. Cobertura Habitável** ❓ — Não | Básica | Completa

**Q13. Aquecimento** ❓ — Gás indiv. | Central | Solar | Bomba calor | Sem

**Q14. Automação** ❓ — Mínimo | Básico | Completo | Premium

**Q15. Energia** ❓ — Sem | Solar comum | Solar completo

**Q17. Paisagismo** ❓ — Sem | Básico | Elaborado | Premium

**Q18. Mobiliário** ❓ — Sem | Básico | Completo | Decorado

**Q20. Região** ✓ **Litoral SC, Capital Floripa**

### ⚡ Infraestrutura Técnica

**Q21. Gerador?** ❓ → Sim | Não

**Q22. Subestação?** ❓ → Sim | Não

**Q23. Placas Fotovoltaicas?** ❓ → Sim | Não

**Q24. Infra Carro Elétrico?** ❓ → Sim | Não

**Q25. Pressurização Escada?** ❓ → Sim | Não

---

## Elementos Construtivos Identificados no IFC

- **759** Members (vigas/pilares)
- **664** WallStandardCase + **509** Wall = **1,173 paredes**
- **345** Portas
- **218** Janelas
- **158** Lajes
- **93** Curtain Walls (fachadas cortina)
- **84** Railings (guarda-corpos)
- **31** StairFlights (lances de escada)
- **16** Stairs (escadas)

---

## Próximos Passos

1. ✓ Extração de dados do IFC
2. ❓ **Leo: responder perguntas de alto impacto (Q2, Q5, Q3, Q19)**
3. ❓ **Leo: fornecer dados faltantes (UR, ELEV, VAG)**
4. Gerar planilha paramétrica com `python3.11 scripts/gerar_template_dinamico.py`
5. Entregar orçamento

---

*Gerado automaticamente por Paramétrico em 09/03/2026*
