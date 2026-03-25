# Briefing - Esquadrias
## Projeto: Thozen Electra - Rubens Alves
**Disciplina:** Esquadrias  
**Revisão:** R00  
**Data:** 2026-03-20

---

## 1. RESUMO EXECUTIVO

Este briefing apresenta o quantitativo completo de esquadrias extraído dos modelos BIM de arquitetura do projeto Thozen Electra - Rubens Alves.

**Principais números:**

- **Portas de madeira:** 2111 UN
- **Portas de vidro temperado:** 0 UN
- **Portas de alumínio/veneziana:** 238 UN
- **Portas de elevador:** 186 UN
- **Janelas basculantes:** 552 UN
- **Janelas de correr:** 889 UN
- **Vidros fixos:** 17 UN
- **Venezianas:** 0 UN

**Área total estimada de vidro:** 2129.80 m²

---

## 2. PREMISSAS E OBSERVAÇÕES

### 2.1 Fontes de Dados
- `RA_ARQ_EXE_MODELAGEM TIPO_R07.ifc`
- `RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc`

### 2.2 Metodologia de Extração
- Extração automatizada via processamento de arquivos IFC (IfcDoor, IfcWindow)
- Classificação por tipo de material e sistema de abertura
- Agrupamento por código e dimensões

### 2.3 Premissas Técnicas
- **Portas de madeira:** Incluem portas internas, portas de correr de madeira, portões
- **Portas de vidro:** Portas mão-amiga em vidro temperado 10mm (áreas sociais)
- **Portas de alumínio:** Venezianas sem peitoril (áreas técnicas/serviço)
- **Janelas:** Todas em alumínio branco com persiana integrada (exceto venezianas)
- **Vidros:** Considerar espessura 6mm para janelas, 10mm para portas de vidro, vidros fixos conforme projeto

### 2.4 Observações Importantes
- ⚠️ **Ferragens, batentes e guarnições NÃO estão quantificados** - precisam ser extraídos de cadernos de especificações ou planilhas técnicas
- ⚠️ Vidros fixos: apenas 17 UN identificadas no IFC - verificar se há mais elementos em DWGs específicos (RA_ESQ_EXE_05_VIDRO FIXO PRÉ-EXECUTIVO_R01.dwg)
- ⚠️ Peles de vidro: não identificadas no IFC de arquitetura - verificar DWG específico (RA_ESQ_EXE_04_PELES DE VIDRO PRÉ-EXECUTIVO_R01.dwg)
- Venezianas: alguns itens com dimensões atípicas (ex: 1000x840cm, 60x1500cm) - **VALIDAR com projeto**

---

## 3. QUANTITATIVOS DETALHADOS

### 3.1 PORTAS DE MADEIRA

**Total: 2111 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| PM | DALLO-PORTA INTERNA | 80x210 | UN | 984 |  |
| PM | DALLO-PORTA INTERNA | 70x210 | UN | 553 |  |
| PM | DALLO-PORTA INTERNA | 90x210 | UN | 210 |  |
| PM | DALLO-PORTA INTERNA | 60x210 | UN | 155 |  |
| PMC | DALLO-PORTA DE CORRER DE MADEIRA | 70x210 | UN | 72 |  |
| PM | DALLO-PORTA CORTA-FOGO | 100x210 | UN | 72 |  |
| PMC | DALLO-PORTA DE CORRER DE MADEIRA | 90x210 | UN | 48 |  |
| PM | DALLO-PORTA INTERNA | 70x140 | UN | 4 |  |
| PM | DALLO-PORTA INTERNA - 2 FOLHAS GIRO | 160x210 | UN | 3 |  |
| PM | DALLO-PORTA INTERNA - 2 FOLHAS GIRO | 220x210 | UN | 2 |  |
| PO | DALLO-PORT\X\C3O COM VENTILA\X\C7\X\C3O SUPERIOR | 350x270 | UN | 2 |  |
| PM | PORTA CORTA-FOGO - 2 FOLHAS GIRO | 140x210 | UN | 2 |  |
| PM | DALLO-PORTA INTERNA | 70x180 | UN | 2 |  |
| PM | PORTA DE ALUM\X\CDNIO - 2 FOLHAS GIRO | 150x210 | UN | 1 |  |
| PM | DALLO-PORTA INTERNA - 2 FOLHAS GIRO | 200x210 | UN | 1 |  |

### 3.2 PORTAS DE VIDRO TEMPERADO

**Total: 0 UN**

_(Nenhum item encontrado)_

### 3.3 PORTAS DE ALUMÍNIO/VENEZIANA

**Total: 238 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 60x100 | UN | 188 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 70x229 | UN | 24 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 80x210 | UN | 12 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 60x210 | UN | 9 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 270x210 | UN | 2 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 220x210 | UN | 2 | Veneziana s/ peitoril |
| PAV | DALLO-PORTA DE ALUM\X\CDNIO VENEZIANA SEM PEITORIL | 70x210 | UN | 1 | Veneziana s/ peitoril |

### 3.4 PORTAS DE ELEVADOR

**Total: 186 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| PE | DALLO-PORTA DO ELEVADOR | 80x210 | UN | 186 |  |

### 3.5 JANELAS BASCULANTES

**Total: 552 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| JA | DALLO-JAN. BASC. 1F  S. PERS. ALUM. BRANCO | 60x75 | UN | 552 | Alumínio branco + persiana |

### 3.6 JANELAS DE CORRER

**Total: 889 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 170x110 | UN | 192 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 140x214 | UN | 144 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. B... | 120x110 | UN | 74 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 120x214 | UN | 72 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 120x120 | UN | 72 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. COM PEIT. DE VIDR... | 200x200 | UN | 48 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 130x214 | UN | 48 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. B... | 100x110 | UN | 47 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 150x209 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 140x120 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 200x110 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 150x120 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. B... | 80x110 | UN | 24 | Alumínio branco + persiana |
| JA | JAN. CORRER 2F S. PERS. COM PEIT. DE VIDRO ALUM... | 70x124 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F C VENT PERMAMENTE. ALUM. B... | 90x110 | UN | 24 | Alumínio branco + persiana |
| JA | DALLO-JAN. CORRER 2F S. PERS. ALUM. BRANCO | 100x209 | UN | 24 | Alumínio branco + persiana |

### 3.7 VIDROS FIXOS

**Total: 17 UN**

| Código | Descrição | Dimensões (cm) | UN | QTD | Observação |
|--------|-----------|----------------|----|----- |------------|
| VF | VIDRO FIXO | 2.35x2.40 | UN | 2 |  |
| VF | VIDRO FIXO | 3.00x1.80 | UN | 1 |  |
| VF | VIDRO FIXO | 8.55x1.90 | UN | 1 |  |
| VF | VIDRO FIXO | 1.20x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 3.00x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 1.30x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 3.00x1.90 | UN | 1 |  |
| VF | VIDRO FIXO | 2.00x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 1.70x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 2.91x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 4.00x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 5.85x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 5.90x2.40 | UN | 1 |  |
| VF | VIDRO FIXO | 3.35x1.70 | UN | 1 |  |
| VF | VIDRO FIXO | 2.74x1.80 | UN | 1 |  |
| VF | VIDRO FIXO | 1.45x1.25 | UN | 1 |  |

### 3.8 VENEZIANAS

**Total: 0 UN**

_(Nenhum item encontrado)_

---

## 4. DADOS FALTANTES E PRÓXIMOS PASSOS

### 4.1 Dados NÃO Extraídos (ainda)
Os seguintes dados **NÃO** foram extraídos neste briefing e precisam de análise complementar:

1. **Peles de vidro** (fachada-cortina)
   - Fonte: `RA_ESQ_EXE_04_PELES DE VIDRO PRÉ-EXECUTIVO_R01.dwg`
   - Ação: Converter DWG → DXF → extrair geometrias

2. **Vidros fixos adicionais**
   - Fonte: `RA_ESQ_EXE_05_VIDRO FIXO PRÉ-EXECUTIVO_R01.dwg`
   - Observação: IFC contém apenas 17 UN - provavelmente há mais no DWG específico

3. **Ferragens e acessórios**
   - Dobradiças, fechaduras, puxadores, trincos
   - Batentes, contramarcos, guarnições
   - Fonte: Memorial descritivo ou planilha de especificações

4. **Especificações de vidros**
   - Espessuras por tipo de esquadria
   - Tratamentos (temperado, laminado, insulado)
   - Película de controle solar

### 4.2 Validações Necessárias
- [ ] Confirmar dimensões de venezianas atípicas (1000x840cm, 60x1500cm)
- [ ] Validar se todas as portas de vidro temperado têm espessura 10mm
- [ ] Verificar se há esquadrias de PVC (título menciona, mas não foram encontradas no IFC)
- [ ] Confirmar se todos os vidros de janelas são 6mm

### 4.3 Próximas Etapas
1. Processar DWGs de peles de vidro e vidros fixos (conversão para DXF ou uso de biblioteca DWG)
2. Extrair especificações técnicas de memorial descritivo
3. Gerar planilha Excel de orçamento executivo (formato Memorial Cartesiano)
4. Comparar com eventuais planilhas do fornecedor/fabricante

---

## 5. ARQUIVOS FONTE

### IFCs Processados
- `projetos/thozen-electra/projetos/02 ARQUITETURA/IFC/RA_ARQ_EXE_MODELAGEM TIPO_R07.ifc`
- `projetos/thozen-electra/projetos/02 ARQUITETURA/IFC/RA_ARQ_EXE_MODELAGEM EMBASAMENTO + COBERTURA_R08.ifc`

### DWGs Disponíveis (não processados)
- `projetos/thozen-electra/projetos/04 ESQUADRIA/RA_ESQ_EXE_01_PORTAS PRÉ-EXECUTIVO_R01.dwg`
- `projetos/thozen-electra/projetos/04 ESQUADRIA/RA_ESQ_EXE_02_JANELAS PRÉ-EXECUTIVO_R01.dwg`
- `projetos/thozen-electra/projetos/04 ESQUADRIA/RA_ESQ_EXE_04_PELES DE VIDRO PRÉ-EXECUTIVO_R01.dwg`
- `projetos/thozen-electra/projetos/04 ESQUADRIA/RA_ESQ_EXE_05_VIDRO FIXO PRÉ-EXECUTIVO_R01.dwg`

---

**Briefing gerado automaticamente em:** 2026-03-20 10:36 BRT  
**Ferramenta:** Cartesiano - Assistente Técnico Cartesian Engenharia  
**Arquivo JSON completo:** `/tmp/briefing_completo.json`
