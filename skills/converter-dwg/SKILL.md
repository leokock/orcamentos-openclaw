---
name: converter-dwg
description: Use quando precisar converter arquivos DWG para DXF para processamento. Trigger quando mencionarem "converte os DWGs", "preciso dos DXFs", "nao consigo ler o DWG", ou quando um fluxo de extracao falhar por formato binario DWG.
---

# Converter DWG para DXF

Converte arquivos DWG (binario AutoCAD) para DXF (texto, processavel por ezdxf) usando ODA File Converter.

## Quando Usar

- DWGs nao podem ser lidos diretamente por Python (formato binario)
- Extracao de quantitativos precisa de DXF
- Equipe enviou DWGs e precisa processar

## Fluxo

### 1. Verificar ODA File Converter

```bash
which ODAFileConverter 2>/dev/null || echo "NAO INSTALADO"
# Se nao instalado: brew install --cask oda-file-converter
```

### 2. Converter batch

```bash
# Converter pasta inteira de DWGs para DXFs
ODAFileConverter \
  "projetos/[projeto]/projetos/[disciplina]/DWG" \
  "projetos/[projeto]/projetos/[disciplina]/DXF" \
  "ACAD2018" "DXF" "0" "1"
```

Parametros: input_dir output_dir version format recurse audit
- version: ACAD2018 (compativel com a maioria)
- format: DXF
- recurse: 0 (nao recursivo) ou 1 (recursivo)
- audit: 1 (corrigir erros)

### 3. Verificar resultado

```bash
ls projetos/[projeto]/projetos/[disciplina]/DXF/*.dxf | wc -l
# Comparar com quantidade de DWGs originais
```

### 4. Teste de leitura

```python
import ezdxf
doc = ezdxf.readfile("caminho/arquivo.dxf")
msp = doc.modelspace()
print(f"Entidades: {len(list(msp))}")
```

## Resolucao de Problemas

| Erro | Solucao |
|------|---------|
| ODAFileConverter nao encontrado | `brew install --cask oda-file-converter` |
| DXF vazio (0 entidades) | DWG pode ter so layout, tentar com recurse=1 |
| Encoding errado | Adicionar `encoding='utf-8'` no ezdxf.readfile |
| Resource deadlock (Drive) | Copiar DWG pra temp/ antes: `cp projetos/.../*.dwg temp/` |

## Regra

Apos converter, informar quantos arquivos foram convertidos e confirmar que sao legiveis com ezdxf.
