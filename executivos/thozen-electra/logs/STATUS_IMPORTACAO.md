# Status de Importação — Electra Towers (Thozen)

**Data:** 2026-03-20 13:45 GMT-3  
**Projeto:** Electra Towers  
**Project ID:** `cdff0592-fb3c-4c13-9516-efde6b56b336`

---

## ✅ Etapa 1: Processamento de Dados — CONCLUÍDO

### O que foi extraído

| Item | Quantidade | Status |
|------|-----------|--------|
| **Insumos** | 835 | ✅ JSON gerado |
| **Composições (CPUs)** | 926 | ✅ JSON gerado |
| **EAP (Estrutura)** | 2 UC + 14 seções | ✅ JSON gerado |

### Arquivos gerados

```
executivo/thozen-electra/
├── insumos.json          # 835 insumos com código, descrição, unidade, preço
├── cpus.json             # 926 composições com desagregação de insumos
├── eap.json              # Estrutura de EAP (UC > CC > Etapa > Subetapa)
└── import_to_memorial_v2.py  # Script de importação (otimizado)
```

### Exemplo de estrutura

**Insumo:**
```json
{
  "codigo": "INS_00001",
  "descricao": "Arame Galvanizado",
  "unidade": "KG",
  "custo_unitario": 13.69,
  "grupo": "Aço",
  "subgrupo": "Arame"
}
```

**Composição (CPU):**
```json
{
  "codigo": "Central de aço",
  "descricao": "Central de aço",
  "unidade": "M2",
  "custo_total": 118.10,
  "insumos": [
    {
      "descricao": "LONA PLASTICA 120 MICRAS 4X100M PRETA",
      "quantidade": 1.0,
      "custo_unitario": 1.25
    },
    ...
  ]
}
```

---

## 🔐 Etapa 2: Autenticação — CONCLUÍDO

✅ **Token JWT obtido com sucesso**
- Email: `leonardo@cartesianengenharia.com`
- User ID: `ffb7fc3d-032b-413f-bfa9-456f307c4350`
- Token válido por: 1 hora

---

## 📊 Etapa 3: Importação para Supabase — EM ANDAMENTO

### Status Atual

❌ **Problema identificado:** Timeout de conexão com Supabase ao tentar importar em lote grande (835 + 926 itens)

### Causa Provável
- API do Supabase com limite de conexões simultâneas
- Rede com instabilidade ou latência alta
- RLS (Row Level Security) exigindo validação de cada insert

### Soluções Possíveis

#### **Opção A: Importação via Bulk Insert (Recomendado)**
Usar RPC `rpc/batch_insert_` do Supabase (mais eficiente):

```bash
# Exemplo de RPC para insumos em lote
curl -X POST "${MEMORIAL_SUPABASE_URL}/rest/v1/rpc/batch_insert_insumos" \
  -H "apikey: ${MEMORIAL_SUPABASE_ANON}" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

#### **Opção B: Importação via Interface Memorial**
1. Acessar https://memorial.cartesianengenharia.com
2. Projeto: **Electra Towers**
3. Menu: Orçamento → Insumos → Importar
4. Upload: `insumos.json`
5. Menu: Orçamento → Composições → Importar
6. Upload: `cpus.json`

#### **Opção C: Importação Manual Segmentada**
Importar em chunks menores (100 itens por vez):

```bash
python3 executivo/thozen-electra/import_segmented.py --size 100 --project electra
```

#### **Opção D: Script com Fila de Espera**
Usar `rq` (Redis Queue) para processar em background:

```bash
pip install rq
rq worker --with-scheduler &
python3 executivo/thozen-electra/import_async.py
```

---

## 🎯 Recomendação Imediata

**Sugiro testar a importação via interface do Memorial primeiro:**

1. ✅ Acesse o Memorial (você já tem acesso)
2. ✅ Vá para Electra Towers
3. ✅ Importe `insumos.json` primeiro (835 itens — rápido)
4. ✅ Depois importe `cpus.json` (926 composições)

Se a interface do Memorial tiver upload direto, será muito mais estável que via API.

---

## 📋 Checklist Final

- [ ] **Insumos:** 835 itens prontos pra importar
- [ ] **CPUs:** 926 composições prontas
- [ ] **EAP:** 2 UCs + 14 seções mapeadas
- [ ] **Autenticação:** JWT obtido
- [ ] **Projeto:** `cdff0592-fb3c-4c13-9516-efde6b56b336` (Electra Towers)

---

## 📞 Próximas Ações

1. **Tentar importar via interface do Memorial** (mais estável)
2. **Se falhar:** me chamar pra debug específico no Supabase
3. **Depois de importar insumos/CPUs:** Vincular aos budget_items da EAP

---

**Script pronto:** `import_to_memorial_v2.py`  
**Ambiente:** Credenciais em `.env.sensitive`  
**Status geral:** 🟡 85% — Aguardando importação no Supabase
