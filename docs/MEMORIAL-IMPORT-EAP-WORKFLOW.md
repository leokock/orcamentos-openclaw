# Memorial - Workflow de Importação de EAP

Guia completo para importar estruturas EAP (WBS) no Memorial Cartesiano.

---

## Contexto

O Memorial Cartesiano usa uma estrutura hierárquica de 4 níveis para orçamentos executivos:

| Nível | Nome | Exemplo de Código | Descrição |
|-------|------|-------------------|-----------|
| N1 | Unidade Construtiva (UC) | `01`, `02` | Grandes blocos (Gerenciamento, Executivo) |
| N2 | Célula | `01.01`, `02.03` | Disciplinas/sistemas dentro da UC |
| N3 | Etapa | `02.03.001`, `02.05.002` | Grupos de serviços |
| N4 | Subetapa | `02.03.001.001` | Serviços específicos (folhas da árvore) |

---

## Problema Comum: Códigos Relativos vs Qualificados

### ❌ Erro Frequente

Arquivos JSON de EAP costumam ter códigos *relativos* nos níveis filhos:

```json
{
  "unidades_construtivas": [
    {
      "codigo": "02",
      "nome": "GERENCIAMENTO EXECUTIVO",
      "celulas": [
        {"codigo": "01", "nome": "INFRAESTRUTURA"},      // ❌ Relativo!
        {"codigo": "02", "nome": "SUPRAESTRUTURA"},      // ❌ Relativo!
        {"codigo": "03", "nome": "PAREDES E PAINÉIS"}    // ❌ Relativo!
      ]
    }
  ]
}
```

Se você importar esses códigos diretamente no campo `code` do `budget_items`, vai gerar **duplicatas** e **colisões**:

- Célula "INFRAESTRUTURA" da UC 02 terá código `01`
- Célula "SERVIÇOS TÉCNICOS" da UC 01 também terá código `01`
- Resultado: códigos duplicados, hierarquia quebrada ❌

### ✅ Solução: Códigos Qualificados

Construir o código *qualificado* em runtime, concatenando o código do pai:

| Nível | Código JSON | Código Qualificado (para DB) |
|-------|-------------|------------------------------|
| UC | `"02"` | `02` |
| Célula | `"01"` | `02.01` |
| Célula | `"02"` | `02.02` |
| Etapa | `"001"` (de "01.001") | `02.01.001` |
| Subetapa | `"001"` (de "01.001.001") | `02.01.001.001` |

---

## Regras de Codificação

### N1 - UC (Unidade Construtiva)

- **Código JSON:** `"01"`, `"02"`
- **Código DB:** mesmo (`"01"`, `"02"`)
- **Parent:** `null`

### N2 - Célula

- **Código JSON:** pode ser relativo (`"01"`, `"02"`) ou qualificado (`"01.01"`)
- **Código DB:** **sempre qualificado** = `{uc_code}.{cel_seq}`
  - Ex: UC `02` + Célula `01` → código `02.01`

### N3 - Etapa

- **Código JSON:** pode vir como `"01.001"` ou só `"001"`
- **Código DB:** **sempre qualificado** = `{uc_code}.{cel_seq}.{etapa_seq}`
  - Ex: Célula `02.03` + Etapa `002` → código `02.03.002`

### N4 - Subetapa

- **Código JSON:** pode vir como `"01.001.001"` ou só `"001"`
- **Código DB:** **sempre qualificado** = `{uc_code}.{cel_seq}.{etapa_seq}.{sub_seq}`
  - Ex: Etapa `02.03.002` + Subetapa `003` → código `02.03.002.003`

---

## Campos Obrigatórios por Nível

### Todos os Níveis

```python
{
    "budget_id": "uuid",
    "code": "string (código qualificado)",
    "name": "string",
    "description": "string",
    "level": 1 | 2 | 3 | 4,  # INTEGER, não string
    "sequence": int,          # Posição entre irmãos
    "is_leaf": bool,          # true apenas para N4
    "total_price": 0          # Obrigatório
}
```

### Apenas N4 (Subetapas/Folhas)

```python
{
    "unit": "VB" | "m2" | "m3" | "un" | etc,
    "quantity": 0,
    "unit_price": 0,
    "composicao_id": "uuid ou null"  # Vincular CPU se existir
}
```

**⚠️ IMPORTANTE:**  
- `level` deve ser **integer** (1, 2, 3, 4), não string ("1", "2")
- `unit`, `quantity`, `unit_price` SÓ podem existir em itens folha (`is_leaf: true`)
- Itens não-folha (N1-N3) **não devem** ter esses campos

---

## Workflow de Importação

### 1. Preparar Estrutura em Memória

```python
import json

with open('eap.json', 'r') as f:
    eap_data = json.load(f)

all_items = []

for uc_idx, uc in enumerate(eap_data['unidades_construtivas']):
    uc_code = uc['codigo'].zfill(2)  # "01", "02"
    
    # Adicionar UC
    all_items.append({
        "code": uc_code,
        "name": uc['nome'],
        "level": 1,
        "sequence": uc_idx,
        "parent_code": None
    })
    
    for cel_idx, cel in enumerate(uc.get('celulas', [])):
        # Código qualificado
        cel_code_raw = cel['codigo'].zfill(2)
        cel_code = f"{uc_code}.{cel_code_raw}"
        
        all_items.append({
            "code": cel_code,
            "name": cel['nome'],
            "level": 2,
            "sequence": cel_idx,
            "parent_code": uc_code
        })
        
        for et_idx, et in enumerate(cel.get('etapas', [])):
            # Extrair sequência da etapa
            et_parts = et['codigo'].split('.')
            et_seq = et_parts[-1]  # Último componente (ex: "001")
            et_code = f"{cel_code}.{et_seq}"
            
            all_items.append({
                "code": et_code,
                "name": et['nome'],
                "level": 3,
                "sequence": et_idx,
                "parent_code": cel_code
            })
            
            for sub_idx, sub in enumerate(et.get('subetapas', [])):
                sub_parts = sub['codigo'].split('.')
                sub_seq = sub_parts[-1]
                sub_code = f"{et_code}.{sub_seq}"
                
                all_items.append({
                    "code": sub_code,
                    "name": sub['nome'],
                    "level": 4,
                    "sequence": sub_idx,
                    "parent_code": et_code,
                    "is_leaf": True
                })
```

### 2. Vincular CPUs (Opcional)

Se você tem um catálogo de CPUs do cliente, vincule as subetapas (N4):

```python
# Buscar CPUs do cliente
cpus_resp = requests.get(
    f"{SUPABASE_URL}/rest/v1/composicoes",
    params={
        "select": "id,description",
        "client_id": f"eq.{CLIENT_ID}",
        "project_id": "is.null"
    },
    headers=headers
)
cpus_by_desc = {c['description']: c['id'] for c in cpus_resp.json()}

# Vincular subetapas
for item in all_items:
    if item['level'] == 4:  # Subetapa
        cpu_id = cpus_by_desc.get(item['name'])
        if cpu_id:
            item['composicao_id'] = cpu_id
```

### 3. Importar por Level (Batch)

**⚠️ IMPORTANTE:** Importar level por level (1 → 2 → 3 → 4) para respeitar foreign keys.

```python
# Mapear temp_id → item_id real
code_to_id = {}

for level in [1, 2, 3, 4]:
    level_items = [it for it in all_items if it['level'] == level]
    
    # Preparar payload
    batch = []
    for item in level_items:
        # Resolver parent_id
        parent_id = code_to_id.get(item['parent_code']) if item.get('parent_code') else None
        
        payload = {
            "budget_id": BUDGET_ID,
            "parent_id": parent_id,
            "code": item['code'],
            "name": item['name'],
            "description": item['name'],
            "level": level,
            "sequence": item['sequence'],
            "is_leaf": item.get('is_leaf', False),
            "total_price": 0
        }
        
        # Só folhas (N4) têm unit/quantity/unit_price
        if item.get('is_leaf'):
            payload.update({
                "unit": "VB",
                "quantity": 0,
                "unit_price": 0,
                "composicao_id": item.get('composicao_id')
            })
        
        batch.append(payload)
    
    # POST batch (dividir se > 200 itens)
    BATCH_SIZE = 200
    for i in range(0, len(batch), BATCH_SIZE):
        sub_batch = batch[i:i+BATCH_SIZE]
        
        resp = requests.post(
            f"{SUPABASE_URL}/rest/v1/budget_items",
            headers=headers,
            json=sub_batch
        )
        
        # Mapear códigos → IDs reais
        if resp.status_code in [200, 201]:
            for j, ret_item in enumerate(resp.json()):
                original_idx = i + j
                if original_idx < len(level_items):
                    code = level_items[original_idx]['code']
                    code_to_id[code] = ret_item['item_id']
```

---

## Script de Referência

Ver: `~/orcamentos/scripts/memorial_import_eap_batch.py`

Este script:
1. Limpa o orçamento (se já existir)
2. Carrega o JSON da EAP
3. Constrói códigos qualificados
4. Importa em batch (por level)
5. Vincula CPUs automaticamente

**Uso:**
```bash
cd ~/orcamentos
python3.11 scripts/memorial_import_eap_batch.py
```

---

## Checklist de Validação

Após importar, verificar:

- [ ] Códigos qualificados corretos (ex: `02.03.002.001`, não `02`)
- [ ] UCs sem duplicatas (cada código único no level 1)
- [ ] Células com prefixo da UC (ex: `02.01`, `02.02`)
- [ ] Hierarchy correta (parent_id aponta pro pai certo)
- [ ] Subetapas (N4) com `is_leaf: true`
- [ ] Subetapas com `unit`, `quantity`, `unit_price` preenchidos
- [ ] Níveis N1-N3 **sem** `unit`/`quantity`/`unit_price`

---

## Troubleshooting

### Erro: "código duplicado" / itens duplicados no app

- **Causa:** Códigos relativos sendo importados direto (ex: Célula com código "02" colide com UC "02")
- **Fix:** Construir códigos qualificados em runtime
- **Sintoma no app:** UCs duplicadas, Células duplicadas com mesmo nome

### Erro: "FK violation" ou "parent not found"

- **Causa:** Tentativa de importar filhos antes dos pais
- **Fix:** Importar level por level (1 → 2 → 3 → 4), batch por level

### Erro: "campo 'unit' não permitido para nível X" / constraint `budget_items_level_4_cost_only_check`

- **Causa:** Campos de folha (unit/quantity/unit_price) em itens não-folha, OU `is_leaf: true` em nível < 4
- **Fix:** Só adicionar `unit`, `quantity`, `unit_price` quando `level == 4` E `is_leaf == true`
- **⚠️ ATENÇÃO:** Mesmo `is_leaf: false` com `total_price: 0` funciona para N1-N3

### Erro: "level deve ser integer" / `level` como string

- **Causa:** Enviando `"level": "unidade_construtiva"` (string/enum) em vez de `"level": 1` (int)
- **Fix:** `level` é SEMPRE integer: 1=UC, 2=Célula, 3=Etapa, 4=Subetapa

### Erro: "valor maior que 50 caracteres" / campo `code` VARCHAR(50)

- **Causa:** Usando a descrição inteira como código (ex: "Central de aço" ou hash longo)
- **Fix:** Códigos hierárquicos curtos (ex: "02.03.001.002" — máximo ~15 chars)

### Timeout / processo morre

- **Causa:** Loop de POSTs individuais (500+ requests) é lento demais
- **Fix:** Importação em BATCH — preparar todos os itens em memória e POST por level (3-4 requests no total)
- **Script otimizado:** `scripts/memorial_import_eap_batch.py`

---

## Exemplo de JSON Correto (Resumo)

```json
{
  "project_id": "uuid-do-projeto",
  "unidades_construtivas": [
    {
      "codigo": "02",
      "nome": "GERENCIAMENTO EXECUTIVO",
      "celulas": [
        {
          "codigo": "01",  
          "nome": "INFRAESTRUTURA",
          "etapas": [
            {
              "codigo": "01.001",
              "nome": "MOVIMENTAÇÃO DE TERRA",
              "subetapas": [
                {"codigo": "01.001.001", "nome": "Corte e aterro"},
                {"codigo": "01.001.002", "nome": "Rebaixamento de lençol"}
              ]
            }
          ]
        },
        {
          "codigo": "02",
          "nome": "SUPRAESTRUTURA",
          "etapas": [...]
        }
      ]
    }
  ]
}
```

**Códigos qualificados gerados:**
- UC: `02`
- Células: `02.01`, `02.02`
- Etapas: `02.01.001`, `02.02.001`
- Subetapas: `02.01.001.001`, `02.01.001.002`

---

_Última atualização: 20/03/2026 (fix estrutural Electra Towers)_
