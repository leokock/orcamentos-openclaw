# ANÁLISE PROJETO PARADOR AG7 — ORÇAMENTO EXECUTIVO

**Data da Análise:** 10/03/2026  
**Projeto:** PARADOR | AG7  
**Localização:** Balneário Camboriú - SC (Estaleirinho)  
**Objetivo:** Identificar documentação útil, extrair dados de programa e apontar lacunas para orçamento executivo

---

## 1. ARQUIVOS-CHAVE ENCONTRADOS

### 1.1 Coordenação (Pasta 03. AG7 - Coordenacao)
- **Premissas:**
  - `PAR-AG7-SE-0000-SL-SNE-R00.pdf` — Selo/sumário executivo
- **Geral — PDFs:**
  - Briefing de engenharia (R02)
  - Especificações tipo, garden, rooftop (R00)
  - Cronograma pré-executivo (R00)
- **Geral — Planilhas:**
  - `Parador ELV-BRIEFING-R01.xlsx` ✅ — **Detalhamento completo dos 7 elevadores**

### 1.2 Arquitetura (Pasta 08. Arquitetura)
**Executivo — PDFs (146 arquivos):**
- ✅ `PAR-ARQ-EX-0001-SL-GER-R04.pdf` — Folha geral (dados resumo)
- ✅ `PAR-ARQ-EX-0010-IM-IMP-R01.pdf` — Implantação
- ✅ `PAR-ARQ-EX-0011-PG-SUB-R06.pdf` — Planta subsolo
- ✅ `PAR-ARQ-EX-0020-PG-N00-R06.pdf` — Planta térreo/nível 00
- ✅ `PAR-ARQ-EX-0030-PG-N01-R03.pdf` — Planta nível 01
- ✅ `PAR-ARQ-EX-0040-PG-DUI-R03.pdf` — Planta duplex inferior
- ✅ `PAR-ARQ-EX-0050-PG-ROO-R03.pdf` — Planta rooftop
- ✅ Plantas por bloco: 0021-BA (A), 0022-AC (B), 0023-BC (C), 0024-BD (D), 0025-BE (E), 0026-BF (F), 0027-BG (G)
- ✅ Plantas subsolo por bloco: 0012-SB, 0013-SB, 0014-SB (vários)
- ✅ Cortes e detalhes: séries 1000 (cortes), 2000 (elevações), 3000 (tabelas esquadrias/portas)
- ✅ Plantas gerais tipo: 3002A/B, 3003A/B, 3010-3023 (plantas baixas tipo por bloco/tipologia)
- ❌ Quadro de áreas consolidado: **NÃO ENCONTRADO em PDF** (citado como recebido em 10/06/25, possivelmente em planilha separada)

**Sustentabilidade:**
- ✅ `PAR_SUS_REV_PDVArquitetura_R00.pdf` — Revisão sustentabilidade arquitetura

### 1.3 Análise Operacional (Pasta 05. Analise Operacional)
**Pré-Executivo — PDFs:**
- ✅ `PAR-OPE-PE-0001-RELT-R00.pdf` — **Relatório operacional** (dados consolidados de programa)
- ✅ `PAR-OPE-PE-0002-PG-N00-R00.pdf` — Planta operacional N00
- ✅ `PAR-OPE-PE-0003-AC-N00-R00.pdf` — Áreas comuns N00
- ✅ `PAR-OPE-PE-0001-PG-SUB-R00.pdf` — Planta operacional subsolo

---

## 2. DADOS EXTRAÍDOS — PROGRAMA DO EMPREENDIMENTO

### 2.1 Dados Básicos
| Item | Valor | Fonte |
|------|-------|-------|
| **Área do Terreno (AT)** | 10.933,48 m² | Briefing engenharia |
| **Total de Unidades (UR)** | 36 unidades | Relatório operacional |
| **Blocos** | A, B, C, D, E, F, G (7 blocos) | Plantas arquitetura |
| **Nº Elevadores (ELEV)** | 7 elevadores | Planilha ELV-BRIEFING ✅ |
| **Nº Subsolos** | 1 subsolo (SS) | Plantas + briefing elevadores ✅ |
| **Nº Pavimentos Tipo (NPT)** | 1 pavimento tipo | Plantas arquitetura |
| **Nº Total Pavimentos (NP)** | 4 pavimentos (SS, Térreo, Nível 01, Duplex/Rooftop) | Esquema vertical elevadores ✅ |
| **Vagas (VAG)** | ~173 vagas | Inferido da numeração (não consolidado oficialmente) ⚠️ |
| **Área Construída Total (AC)** | **NÃO IDENTIFICADA** ❌ | — |
| **Início da Obra** | out/26 | Briefing engenharia |
| **Lançamento** | ago/26 | Briefing engenharia |

### 2.2 Tipologias (Distribuição por Faixa de Área)
| Faixa | Quantidade | Área (m²) |
|-------|------------|-----------|
| Tipo 1 | 6 unidades | 508,27 a 575,42 m² |
| Tipo 2 | 11 unidades | 327,14 a 333,53 m² |
| Tipo 3 | 15 unidades | 622,04 a 663,57 m² |
| Tipo 4 | 2 unidades | 449,21 a 482,20 m² |
| Tipo 5 | 2 unidades | 278,00 a 263,57 m² |
| **Total** | **36 unidades** | — |

**Observação:** Dados extraídos do relatório operacional, mas **sem quadro-resumo consolidado** por bloco/pavimento.

### 2.3 Elevadores — Detalhamento Técnico ✅

| Elevador | Paradas | Entradas | Percurso (m) | Capacidade | Velocidade | Tipo | Controle Acesso |
|----------|---------|----------|--------------|------------|------------|------|-----------------|
| **ELEV. 1** | 4 | 7 | 9,60 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 2** | 4 | 6 | 9,60 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 3** | 7 | 7 | 10,45 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 4** | 7 | 7 | 10,45 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 5** | 4 | 7 | 9,60 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 6** | 7 | 7 | 10,45 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |
| **ELEV. 7** | 4 | 4 | 9,60 | 12 pax / 900 kg | 1 m/s | Sem casa máquinas | Reconhecimento facial + senha |

**Acabamento:**
- Interno: Aço inoxidável Lucerne Brushed
- Externo: Aço inoxidável Lucerne Brushed
- Subteto: Aço inoxidável Lucerne Brushed
- Piso: Rebaixado 25mm (revestimento responsabilidade construtora)

**Observações críticas:**
- Poço de molas: 1.100 mm
- Última parada: 4.060 mm (elevs 1,2,4,5,6,7) / 4.000 mm (elev 3)
- Caixa de corrida: ~2.000 x 1.940 mm
- Cabina: 1.400 x 1.500 x 2.400 mm
- Portas: 2.100 x 900 mm (abertura central, 2 folhas)
- Tomada 20A por chegada (backup gerador)

### 2.4 Áreas Comuns (Térreo/N00) — Resumo
- Salão de festas / restaurante: 101,28 m²
- Academia: 74,64 m²
- Espaço gourmet: 46,11 m²
- Estar: 35,98 m²
- Minimarket: 30,91 m²
- Brinquedoteca (kids): 25,44 m²
- Sala infanto-juvenil: 24,95 m²
- Guarda-volumes/maleiro: 14,83 m²
- Sala de massagem: 11,93 m²
- Sala multiuso/exercício solo: 11,93 m²
- DML apoio: 10,79 m²
- Administração: 9,21 m²
- Depósito reciclagem: 7,50 m²
- Depósito geral: 7,15 m²
- Depósito privativo (exemplo): 3,56 m²

**Lazer:** Piscina externa, piscina interna coberta, spa, saunas (seca/úmida), bar piscina, parrilla, firepit, playground, deck yoga/kneipp, redário, bicicletário (10 vagas).

**Técnicas:** Casa de máquinas, reservatórios água potável, central resíduos/PEVs, lavanderia, casa pressurização, salas segurança, tanque reuso, poços exaustão, casa de máquinas piscina.

---

## 3. PADRÃO DE ACABAMENTO E SISTEMAS

### 3.1 Certificações (IMPACTO CUSTO ALTO)
- **GBC GOLD** ✅
- **FITWELL 3 estrelas** ✅
- **GBC BIODIVERSIDADE** ✅

### 3.2 Estrutura e Vedações
- **Laje:** 20 cm convencional com vigas
- **Paredes externas:** Bloco cerâmico 19 cm + reboco 3,5 cm (externo) + 2,5 cm (interno)
- **Abas:** Concreto aparente pigmentado com textura
- **Paredes internas apartamentos:** Parede dupla com 3 cm espaçamento + lã de rocha/PET (acústica)
- **Contrapiso apartamentos:** 8 cm (7+3 cm acabamento pedra)
- **Sacada:** Rebaixo 24 cm (impermeabilização + deck)
- **Rooftop:** Rebaixo 35 cm

### 3.3 Forros
- Apartamentos: Drywall ST
- Banheiros/lavanderias: Drywall RU
- Piscina/sauna: GLASROC PLACO (alta umidade)

### 3.4 Instalações Hidrossanitárias
- **Água fria/quente:** PPR ou CPVC
- **Esgoto:** PVC rígido + tubo mineralizado (áreas acústicas)
- **Pluvial:** PVC + tratamento acústico (lã PET + REDUX Tigre)
- **Mangotinho:** Cobre Classe E (NBR 13.206) — **avaliar ferro fundido** ⚠️
- **Reservatórios:** Concreto (cisterna + reuso)
- **Medição:** Hidrômetro individual + telemetria

### 3.5 Aquecimento
- **Piso aquecido:** Sim (BWC Master + Suítes) / Não (BWC Suíte Serviço)
- **Aquecedores unidades:** Passagem + recirculador Smart Starter Rinnai (**NÃO fornecido AG7**)
- **Piscina externa:** Bomba calor + previsão gás
- **Piscina interna:** Bomba calor + complemento gás

### 3.6 Sistema Elétrico
- **Gerador:** Segurança, incêndio, CFTV, elevadores, bombas, rotas fuga, salão festas
- **Carregadores elétricos:** 1 por unidade (7,4 kW) — **INFRA SECA** + distribuição por demanda
- **Tensão:** 220V (elevadores, iluminação, AC, gerador, chuveiro, bombas, aquecedores, fogão/forno/coifa)
- **Tomadas 20A:** Secador (banheiro), cozinha, área serviço, toalheiro térmico, subsolo (chegada elevadores)

### 3.7 Automação e Sistemas
- **Controle acesso veículos:** Câmera leitura placa (2 portões + porteiro)
- **Interfone:** Vídeo porteiro apartamentos + central guarita + speakers halls + eclusa
- **CFTV:** Sistema completo (**NÃO analógico**, limite 16 telas/monitor)
- **Internet:** Cabeada (guarita) + Wireless (academia, piscina, spa, salões, lobbys, subsolo, paisagismo)
- **Áudio/vídeo:** Som + TV em múltiplas áreas — **Caixas Bowers & Wilkins** ✅
- **Unidades:** Infra seca (sala estar) + blackout suítes (acionamento cabeceira)
- **Áreas comuns:** Automação iluminação + climatização + som

### 3.8 Climatização
- **Unidades:** VRF — **SOMENTE INFRAESTRUTURA** (sala cassete 1 via, suítes cassete, quarto serviço high-wall)
- **Condomínio:** VRF COMPLETO (dutado: academia, massagem, brinquedoteca, salões / high-wall: sala descanso, administração, lavanderia, copa, segurança, mini market)
- **Exaustão:** Mecânica em banheiros enclausurados (unidades + condomínio) + timer + desumidificação piscina interna
- **Renovação:** Academia, spa, salão festas, lobbys, brinquedoteca, sala multiuso, guarita, refeitório, administração (GBC/FITWELL)

### 3.9 Gás
- **Tubulação:** Cobre (áreas comuns) + PEX multicamada (apartamentos)
- **Medição condomínio:** ERP (rateio moradores)
- **Medição unidades:** Individualizada (hall área serviço)
- **Atendimento:** Piscinas, vestiários, salões, spa (condomínio) / forno/fogão + 2 aquecedores passagem (unidades)

---

## 4. PRINCIPAIS DRIVERS DE CUSTO

### 4.1 Alto Padrão (TOP 10)
1. ✅ **Certificações triplas:** GBC Gold + Fitwell 3★ + GBC Biodiversidade
2. ✅ **Automação completa** áreas comuns + infra unidades
3. ✅ **Áudio/vídeo Bowers & Wilkins** em múltiplas áreas
4. ✅ **VRF completo** áreas comuns
5. ✅ **Aquecimento de piso** banheiros suítes
6. ✅ **Elevadores com reconhecimento facial** (7 unidades)
7. ✅ **Concreto aparente pigmentado** com textura (abas)
8. ✅ **Paredes duplas acústicas** (lã rocha/PET + 3 cm espaçamento)
9. ✅ **Tratamento acústico completo** (tubos mineralizados + linha REDUX)
10. ✅ **Sistema reuso** água + contenção cheias

### 4.2 Sistemas Complexos
11. ⚠️ **Tubulação cobre Classe E** mangotinho (avaliar ferro fundido)
12. ✅ **Telemetria** todas medições (água + gás)
13. ✅ **Carregadores elétricos** individualizados (infra 7,4 kW/apto)
14. ✅ **Gerador dimensionado** para conforto (não só emergência)
15. ✅ **CFTV não analógico** (limite 16 telas/monitor)
16. ✅ **Piscinas aquecidas** (bomba calor + gás)
17. ✅ **Desumidificação** piscina interna
18. ✅ **Forro GLASROC** sauna/piscina
19. ✅ **Ralos especiais:** linear mármore/inox
20. ✅ **Rebaixos generosos:** rooftop 35 cm, sacada 24 cm

---

## 5. LACUNAS CRÍTICAS — IMPEDEM ORÇAMENTO EXECUTIVO

### 5.1 Dados de Programa (CRÍTICO)
| Item | Status | Impacto |
|------|--------|---------|
| **Área Construída Total (AC)** | ❌ NÃO IDENTIFICADA | **CRÍTICO** — impede cálculo R$/m² |
| **Quadro de áreas consolidado** | ❌ NÃO ENCONTRADO (citado recebido 10/06/25) | **CRÍTICO** — necessário para breakdown por tipologia |
| **Vagas totais (oficial)** | ⚠️ Inferido ~173 (não consolidado) | **ALTO** — necessário confirmar |
| **Memorial descritivo completo** | ⚠️ Parcial (briefing + especificações) | **MÉDIO** — necessário consolidar |

### 5.2 Definições de Projeto (ALTO IMPACTO)
| Item | Status | Impacto Custo |
|------|--------|---------------|
| **Projetista vedações** | ❌ Não definido | **ALTO** |
| **Fundações** | ❌ "A definir" | **CRÍTICO** |
| **Retorno AC** | ⚠️ "Projeto climatização confirmar" | **MÉDIO** |
| **Ventilação garagens** | ⚠️ Mecânica vs permanente | **ALTO** |
| **Mangotinho** | ⚠️ Cobre vs ferro fundido | **MÉDIO** |
| **Contenção cheias** | ⚠️ Confirmar cálculo área permeável | **ALTO** |
| **Volume cisterna** | ❌ Não especificado (m³) | **MÉDIO** |
| **Capacidade aquecedores** | ❌ Não especificado (kW) | **MÉDIO** |
| **Potência gerador** | ❌ Não especificado | **ALTO** |
| **Dimensionamento reservatório reuso** | ❌ Não especificado | **MÉDIO** |

### 5.3 Compatibilizações Pendentes
- Distribuição energia torres (barramento vs cabeamento)
- Local ERP gás (compatibilizar ARQ/PSG)
- Unificação quadros telefonia + automação
- Extintores/hidrantes (interiores + arquitetura)
- Escada (níveis circulação + apartamento)

### 5.4 Fornecimentos — Exclusões AG7
- ❌ Aquecedor passagem unidades
- ❌ Recirculador Smart Starter
- ❌ Equipamentos VRF unidades (só infra)

---

## 6. DOCUMENTAÇÃO DISPONÍVEL vs NECESSÁRIA

### 6.1 Disponível ✅
- Plantas arquitetura executivo (146 PDFs — completas até R06)
- Briefing de engenharia (R02)
- Especificações acabamento (tipo/garden/rooftop R00)
- Detalhamento completo elevadores (planilha R01)
- Relatório análise operacional (R00)
- Plantas operacionais (subsolo + N00)
- Esquema vertical elevadores
- Cronograma pré-executivo

### 6.2 Necessária (NÃO ENCONTRADA) ❌
- **Quadro de áreas consolidado** (AC total + breakdown por tipologia/bloco)
- **Projeto estrutural** (fundações, lajes, vigas, pilares, quantitativos)
- **Projeto hidrossanitário** (prumadas, reservatórios dimensionados, quantitativos)
- **Projeto elétrico** (quadros, cargas, cabeamento, gerador dimensionado)
- **Projeto climatização** (carga térmica, equipamentos, dutos)
- **Projeto gás** (dimensionamento tubulação, ERP, consumo)
- **Projeto SPDA** (detalhamento embutido estrutura)
- **Projeto CFTV** (quantidade câmeras, layout, central)
- **Projeto automação** (central, interface, equipamentos)
- **Memorial descritivo consolidado** (todos sistemas)
- **Orçamento de referência** (se existir)
- **Cronograma executivo** (se existir)

### 6.3 Necessária (PARCIAL) ⚠️
- Memorial acabamentos: existem especificações, falta consolidação
- Quantitativos: plantas disponíveis, falta extração (CAD/Revit necessário)
- Tabelas esquadrias/portas: plantas série 3000 existem, falta extração

---

## 7. RECOMENDAÇÕES PARA ORÇAMENTO EXECUTIVO

### 7.1 Ações Imediatas (CRÍTICO)
1. ✅ **Solicitar quadro de áreas consolidado** (AC total + breakdown tipologias)
2. ✅ **Confirmar número oficial de vagas** (validar ~173 inferido)
3. ✅ **Definir tipo de fundação** (antes de orçar infraestrutura)
4. ✅ **Confirmar projetista vedações** (impacta cronograma + custo alvenaria)
5. ✅ **Solicitar projetos complementares** (estrutural, hidro, elétrico, climatização, gás)

### 7.2 Dados para Parametrização (SE NÃO HOUVER EXECUTIVO)
**Com as lacunas atuais, é possível gerar orçamento paramétrico assumindo:**
- AC estimada: ~18.000–22.000 m² (baseado em 36 unidades x 400–600 m²/un médio + áreas comuns ~3.000 m²) — **NECESSITA VALIDAÇÃO**
- Padrão: **SUPER ALTO** (certificações triplas + automação completa + acabamentos premium)
- Laje: **CONVENCIONAL** (20 cm com vigas)
- Contenção: **SIM** (terreno declive, 1 subsolo)
- Elevadores: **7 unidades** ✅
- Vagas: **~173** ⚠️
- Prazo: **24–30 meses** (inferido do cronograma pré-executivo)

**Briefing paramétrico (5 perguntas críticas):**
- Q2 (Laje): Convencional
- Q5 (Padrão): Super Alto
- Q3 (Contenção): Sim (cortina ou muro)
- Q19 (Prazo): 24–30 meses
- Q4 (Subsolos): 1 subsolo

### 7.3 Próximos Passos
1. Validar dados com Leo/AG7
2. Solicitar documentação faltante
3. Se não houver executivo: gerar paramétrico com AC estimada + alertar sobre incerteza
4. Se houver executivo: processar conforme Fluxo 2 da skill `orcamento-parametrico`

---

## 8. RESUMO EXECUTIVO

### Projeto
- **36 unidades** em **7 blocos** (A–G)
- **4 pavimentos** (SS, Térreo, Nível 01, Duplex/Rooftop)
- **7 elevadores** (reconhecimento facial + inox premium)
- **~173 vagas** (inferido, não confirmado)
- **Certificações triplas** (GBC Gold + Fitwell 3★ + Biodiversidade)

### Documentação
- ✅ **Plantas arquitetura completas** (146 PDFs executivo até R06)
- ✅ **Briefing engenharia + especificações** (tipo/garden/rooftop)
- ✅ **Detalhamento elevadores** (planilha completa R01)
- ❌ **Quadro de áreas consolidado** (CRÍTICO — não encontrado)
- ❌ **Projetos complementares** (estrutural, hidro, elétrico, climatização, gás)

### Padrão
- **SUPER ALTO:** Automação completa, áudio Bowers & Wilkins, VRF, aquecimento piso, paredes duplas acústicas, concreto aparente pigmentado, certificações triplas

### Lacunas Críticas
1. ❌ **AC total** — impede cálculo R$/m²
2. ❌ **Fundações** — impede orçamento infraestrutura
3. ❌ **Projetista vedações** — impede cronograma alvenaria
4. ⚠️ **Vagas confirmadas** — necessário validar ~173
5. ❌ **Projetos complementares** — necessários para executivo detalhado

### Viabilidade Orçamento
- **Paramétrico:** VIÁVEL (com AC estimada + alertas de incerteza)
- **Executivo:** INVIÁVEL (faltam projetos complementares + quantitativos)

---

**Análise realizada por:** Jarvis (subagent)  
**Fonte:** Google Drive AG7 (pastas Coordenação + Arquitetura + Análise Operacional)  
**Método:** Extração via drive.js + análise PDF + planilha Excel
