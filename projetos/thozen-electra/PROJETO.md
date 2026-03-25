# Thozen Electra - Orçamento Executivo

## Informações do Projeto
- **Cliente:** Thozen
- **Empreendimento:** Electra
- **Tipo:** Residencial vertical
- **Status:** Projetos executivos disponíveis (R01)

## Estrutura de Pavimentos (identificado nos arquivos)
- 01° Pavto. Térreo
- 02° Pavto. G1 (garagem)
- 03° Pavto. G2 (garagem)
- 04° Pavto. G3 (garagem)
- 05° Pavto. G4 (garagem)
- 06° Pavto. G5 (garagem)
- 07° Pavto. Lazer
- 08° a 31° Pavto. Tipo (24 pavimentos tipo)
- Casa de Máquinas

**Total:** 32 pavimentos (6 garagens + 1 lazer + 24 tipos + térreo + casa de máquinas)

## Disciplinas Disponíveis

### 01 ESTRUTURA
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 02 ARQUITETURA
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 03 ALVENARIA
- Formatos: DWG
- Status: ✅ Disponível

### 04 ESQUADRIA
- Formatos: DWG
- Status: ✅ Disponível

### 05 HIDRÁULICO
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 06 SANITÁRIO
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 07 PREVENTIVO INCENDIO CIVIL
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 08 PREVENTIVO INCENDIO ELÉTRICO
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 09 ELÉTRICO
- Formatos: DWG + IFC
- Status: ✅ Disponível
- Responsável: R.Rubens Alves

### 10 TELEFONICO
- Formatos: DWG + IFC
- Status: ✅ Disponível

### 11 SPDA
- Formatos: DWG
- Status: ✅ Disponível
- Responsável: R.Rubens Alves

### 12 ESCADA VENTILACAO MECANICA
- Formatos: DWG
- Status: ✅ Disponível

### 13 CHURRASQUEIRA EXAUSTAO
- Formatos: DWG
- Status: ✅ Disponível

### 14 AR-CONDICIONADO
- Formatos: DWG
- Status: ✅ Disponível
- Arquivo: RA_ARC_EXE_00_TODAS CAD_R05.dwg

## Estratégia de Orçamentação

### Fase 1 — Disciplinas Estruturais (Prioridade Alta)
1. **01 ESTRUTURA** → N1 03 Infraestrutura + N1 04 Supraestrutura
   - Extração: fundações, pilares, vigas, lajes, aço
   - Fonte: IFC

2. **02 ARQUITETURA** → Quantitativos gerais (AC, áreas, pés-direitos)
   - Extração: áreas por pavimento, esquema de repetição
   - Fonte: IFC

### Fase 2 — Instalações Hidráulicas (Prioridade Alta)
3. **05 HIDRÁULICO** → N1 06.01 Água Fria
   - Fonte: IFC
   
4. **06 SANITÁRIO** → N1 06.02 Esgoto + 06.03 Águas Pluviais
   - Fonte: IFC

### Fase 3 — Instalações Elétricas e Especiais (Prioridade Média)
5. **09 ELÉTRICO** → N1 07.01 Instalações Elétricas
   - Fonte: IFC

6. **10 TELEFONICO** → N1 14.09 Telefonia/Dados
   - Fonte: IFC

7. **11 SPDA** → N1 07.02 SPDA
   - Fonte: DWG (não tem IFC)

8. **08 PREVENTIVO INCENDIO ELÉTRICO** → N1 14.01 PCI Elétrico
   - Fonte: IFC

### Fase 4 — Complementares (Prioridade Média)
9. **03 ALVENARIA** → N1 09 Alvenaria
   - Fonte: DWG

10. **04 ESQUADRIA** → N1 13 Esquadrias
    - Fonte: DWG

11. **07 PREVENTIVO INCENDIO CIVIL** → N1 14.01 PCI Civil
    - Fonte: IFC

### Fase 5 — Instalações Especiais (Prioridade Baixa)
12. **14 AR-CONDICIONADO** → N1 14.02 Climatização
    - Fonte: DWG

13. **12 ESCADA VENTILACAO MECANICA** → N1 14.08 Ventilação Mecânica
    - Fonte: DWG

14. **13 CHURRASQUEIRA EXAUSTAO** → N1 14.08 Exaustão
    - Fonte: DWG

## Próximos Passos
1. Criar estrutura de pastas executivo/thozen-electra/
2. Definir ordem de prioridade com o time
3. Iniciar pela disciplina escolhida (sugestão: ESTRUTURA ou HIDRÁULICO)
