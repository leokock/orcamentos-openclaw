# 🚀 Comece Aqui - Thozen Electra

**Novo no projeto?** Este guia orienta por onde começar.

---

## 📖 Documentação Disponível

### Para leitura rápida (5 min):
👉 **`briefings/RESUMO-ESTRUTURA.md`**  
Números principais, status dos dados, próximos passos.

### Para análise detalhada (20 min):
📋 **`briefings/estrutura-r00.md`**  
Briefing completo: quantitativos por elemento, tabelas, observações.

### Para contexto técnico (15 min):
🔍 **`briefings/OBSERVACOES-TECNICAS.md`**  
Metodologia de extração, limitações, alertas, benchmarks.

### Para processamento automatizado:
💾 **`briefings/estrutura-r00.json`**  
Dados estruturados em JSON (para scripts/análises).

---

## ⚡ Início Rápido

### Consulta de dados:
```bash
# Ver resumo executivo
cat executivo/thozen-electra/briefings/RESUMO-ESTRUTURA.md

# Ver briefing completo
cat executivo/thozen-electra/briefings/estrutura-r00.md

# Processar JSON (exemplo Python)
python3 -c "
import json
with open('executivo/thozen-electra/briefings/estrutura-r00.json') as f:
    data = json.load(f)
print(f\"Concreto total: {data['quantitativos']['resumo_geral']['total_concreto_m3_estimado']} m³\")
"
```

---

## 🎯 O Que Você Precisa Saber

### ✅ Dados Disponíveis (R00)
- Volume estimado de concreto: ~12.784 m³
- Contagem de elementos: 1.531 pilares, 3.531 vigas, 1.527 lajes, 70 infra
- Distribuição por pavimento
- Principais tipos de elementos (seções, espessuras)

### ⚠️ Dados Faltantes (Urgente)
- **Estacas** (tipo, diâmetro, comprimento, quantidade)
- **Classes de concreto** (fck por elemento)
- **Armação** (taxa de aço, bitolas)
- **Áreas de forma** (m²)

### 📅 Próximos Passos
1. Solicitar memorial descritivo estrutural
2. Solicitar prancha de fundações
3. Validar volumes com projetista
4. Complementar com dados de armação
5. Gerar planilha executiva Excel

---

## 🗂️ Estrutura de Arquivos

```
executivo/thozen-electra/
├── COMECE-AQUI.md              ← Você está aqui!
├── README.md                    ← Índice geral do projeto
└── briefings/
    ├── RESUMO-ESTRUTURA.md     ← Início recomendado
    ├── estrutura-r00.md        ← Briefing completo
    ├── estrutura-r00.json      ← Dados estruturados
    └── OBSERVACOES-TECNICAS.md ← Metodologia e limitações
```

---

## 🔗 Fontes de Dados

**IFC Processado:**  
`projetos/thozen-electra/projetos/01 ESTRUTURA/IFC/1203 - THOZEN - RUBENS ALVES - BLOCOS+RAMPAS DE ACESSO - R26.ifc`

**DWG Disponível:**  
`projetos/thozen-electra/projetos/01 ESTRUTURA/DWG/1203 - PREFORMAS - R20.DWG`

---

## ❓ Perguntas Frequentes

### Os volumes são definitivos?
**NÃO.** São estimativas baseadas em dimensões nominais (±30-40% de precisão).  
**Aguardando validação do projetista estrutural.**

### Posso usar para orçamento final?
**NÃO.** Faltam dados críticos: estacas, aço, áreas de forma, classes de concreto.  
**Usar apenas como estimativa preliminar.**

### Onde estão os dados de aço (armação)?
**Não disponíveis no IFC.** Aguardando pranchas de detalhamento ou planilha do calculista.

### As lajes são maciças ou nervuradas?
**A confirmar.** Espessura de 28 cm sugere maciças, mas pode ser altura total (nervurada + capa).  
**Impacta volume de concreto em 30-50%.**

### Há 1 ou 2 torres?
**A confirmar.** IFC contém duplicações aparentes (80 storeys para 35 pavimentos nomeados).

---

## 📞 Contato

**Dúvidas ou solicitações:**
- Slack: `@Cartesiano` no canal `#custos-ia-paramétrico`
- Time: Orçamentos - Cartesian Engenharia

---

## 🔄 Histórico

- **R00 (20/03/2026):** Extração inicial via IFC - dados incompletos
- **R01 (futuro):** Complementação com memorial + fundações

---

**Boa leitura! 📚**
