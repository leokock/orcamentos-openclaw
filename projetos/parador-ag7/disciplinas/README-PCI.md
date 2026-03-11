# Extração de Quantitativos PCI - Parador AG7

## Status: ⚠️ PENDENTE EXTRAÇÃO MANUAL

### Problema Encontrado

Tentativa de extração automática dos arquivos DWG e PDF falhou devido a **erro de sincronização do Google Drive** (`Resource deadlock avoided`).

**Arquivos identificados mas não acessíveis:**
- 15 pranchas DWG na pasta: `27. Prevencao a Incendio/04. Executivo/DWG/`
- 15 pranchas PDF correspondentes na pasta: `27. Prevencao a Incendio/04. Executivo/PDF/`

---

## Arquivos do Projeto

### Organização dos Pavimentos

| Prancha | Pavimento | Arquivo |
|---------|-----------|---------|
| 0000 | Subnível | PAR-INC-EX-0000-TO-SNIV-R00.dwg |
| 0101 | Subsolo 1 | PAR-INC-EX-0101-TO-SUB-R00.dwg |
| 0102 | Subsolo 2 | PAR-INC-EX-0102-TO-SUB-R00.dwg |
| 0103 | Subsolo 3 | PAR-INC-EX-0103-TO-SUB-R00.dwg |
| 0104-0106 | Térreo (3 variações) | PAR-INC-EX-010[4-6]-TO-N00-R00.dwg |
| 0107-0109 | Pav. Tipo 1 (3 variações) | PAR-INC-EX-010[7-9]-TO-N01-R00.dwg |
| 0110-0112 | Duplex (3 variações) | PAR-INC-EX-011[0-2]-TO-DUI-R00.dwg |
| 0113 | Cobertura | PAR-INC-EX-0113-TO-ROO-R00.dwg |

**Nota:** Arquivos terminados em `_1.dwg` são duplicatas (ignorados)

---

## Alternativas de Extração

### Opção 1: Extração Manual no AutoCAD/BricsCAD

**Passos:**
1. Abrir cada prancha DWG
2. Executar comandos:
   - `LIST` em cada bloco de equipamento
   - `FILTER` para selecionar blocos por nome
   - `QSELECT` para filtrar por tipo
3. Usar layers típicos de PCI:
   - `INC-HIDRANTE`
   - `INC-EXTINTOR`
   - `INC-SPRINKLER`
   - `INC-DETECTOR`
   - `INC-ALARME`
4. Medir tubulações com `MEASUREGEOM` → `LENGTH`

### Opção 2: Usar Tabelas de Quantidades do Projeto

Se o projeto possui tabelas/legendas de quantidades:
1. Verificar selo/carimbo das pranchas
2. Procurar por "QUADRO DE QUANTIDADES" ou similar
3. Somar quantidades por pavimento

### Opção 3: Exportar DWG Localmente

1. Pausar Google Drive File Stream
2. Copiar pasta inteira para disco local (ex: `~/Downloads/PCI_Parador/`)
3. Reexecutar script de extração automática:
   ```bash
   cd /tmp
   source pci_venv/bin/activate
   python3 extrair_pci.py
   ```

### Opção 4: Utilizar Plugin BIM

Se projeto possui IFC ou modelo BIM:
1. Verificar pasta `Modelos/` (identificada no projeto)
2. Abrir IFC no Revit/Archicad/Navisworks
3. Usar ferramentas de quantificação nativas
4. Exportar Schedule/Lista de Quantidades

---

## Categorias a Levantar

### 1. Hidrantes (UN)
- Abrigo de hidrante com mangueira 30m
- Hidrante de recalque (fachada)
- Registro de gaveta
- Esguicho regulável

### 2. Sprinklers (UN)
- Sprinkler pendente (teto)
- Sprinkler lateral (parede)
- Válvula de governo e alarme
- Alarme de fluxo d'água

### 3. Extintores (UN)
- Extintor PQS 6kg (classe ABC)
- Extintor CO2 6kg
- Extintor AP 10L (água pressurizada)
- Suporte de parede para extintor

### 4. Detectores de Fumaça (UN)
- Detector endereçável
- Detector convencional
- Base de detector

### 5. Alarme e Sinalização (UN)
- Central de alarme endereçável
- Acionador manual
- Sirene audiovisual
- Luz de emergência
- Placa fotoluminescente (tipos diversos)

### 6. Tubulações (m)
Por diâmetro:
- Ø 2½" (hidrantes - linha principal)
- Ø 2" (hidrantes - ramais)
- Ø 1¼" (sprinklers - linha principal)
- Ø 1" (sprinklers - ramais)

**Material típico:** Aço galvanizado Schedule 40

---

## Formato de Saída

Atualizar o arquivo `pci.json` seguindo o formato:

```json
{
  "categorias": [
    {
      "nome": "Hidrantes",
      "items": [
        {
          "descricao": "Abrigo de hidrante completo com mangueira 30m, esguicho e registro",
          "quantidade": 8,
          "unidade": "UN",
          "observacao": "Conforme NBR 13714"
        }
      ]
    }
  ]
}
```

---

## Validação

Após extração, **validar com:**
1. Memorial descritivo do projeto
2. Responsável técnico pela disciplina PCI
3. Normas aplicáveis:
   - NBR 13714 (Hidrantes)
   - NBR 10897 (Sprinklers)
   - NBR 12693 (Extintores)
   - NBR 17240 (Detecção e alarme)

---

## Contato

**Dúvidas sobre o projeto:** Consultar projetista responsável pela disciplina PCI na AG7 Incorporadora.

**Problemas técnicos (Google Drive):** Equipe de TI Cartesian.

---

*Documento gerado automaticamente em 2026-03-11*
*Subagente: parador-pci*
