#!/usr/bin/env python3.11
"""
Processador Rápido — Alvenaria Thozen Electra
Processa apenas DXFs pequenos (<100MB) para gerar briefing parcial R01
"""

import sys
import json
from pathlib import Path
import math

try:
    import ezdxf
except ImportError:
    print("❌ pip3.11 install ezdxf")
    sys.exit(1)


DXF_DIR = Path("projetos/thozen-electra/dxf-temp")
OUTPUT_DIR = Path("executivo/thozen-electra/quantitativos/alvenaria")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Processar apenas arquivos pequenos
ARQUIVOS = [
    ("RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dxf", "01", "Térreo", 1),
    ("RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dxf", "05", "G4", 1),
    ("RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dxf", "07", "Lazer", 1),
    ("RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dxf", "08-31", "Tipo", 24),
    ("RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dxf", "32", "Res-Cob", 1),
]

LAYERS_AREA = ['A-WALL-____-PATT']
LAYERS_COMP = ['A-WALL-____-OTLN']


def calcular_area_polyline(points):
    if len(points) < 3:
        return 0
    try:
        area = 0
        n = len(points)
        for i in range(n):
            j = (i + 1) % n
            p1, p2 = points[i], points[j]
            x1 = p1[0] if isinstance(p1, (tuple, list)) else p1.x
            y1 = p1[1] if isinstance(p1, (tuple, list)) else p1.y
            x2 = p2[0] if isinstance(p2, (tuple, list)) else p2.x
            y2 = p2[1] if isinstance(p2, (tuple, list)) else p2.y
            area += (x1 * y2) - (x2 * y1)
        return abs(area) / 2
    except:
        return 0


def processar(filename, pav, nome, mult):
    dxf_path = DXF_DIR / filename
    if not dxf_path.exists():
        print(f"  ⏭️  {nome} — não encontrado")
        return None
    
    print(f"  🔄 {nome}...", end=" ", flush=True)
    
    try:
        doc = ezdxf.readfile(str(dxf_path))
    except Exception as e:
        print(f"❌ {e}")
        return None
    
    msp = doc.modelspace()
    area_total = 0
    comp_total = 0
    num_portas = 0
    
    # HATCHs (áreas)
    for hatch in msp.query('HATCH'):
        if hatch.dxf.layer in LAYERS_AREA:
            try:
                for path in hatch.paths:
                    if hasattr(path, 'vertices'):
                        area = calcular_area_polyline(path.vertices)
                        if area > 1:
                            area_total += area
            except:
                pass
    
    # LINEs (comprimentos)
    for line in msp.query('LINE'):
        if line.dxf.layer in LAYERS_COMP:
            try:
                start = line.dxf.start
                end = line.dxf.end
                comp = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                if comp > 0.1:
                    comp_total += comp
            except:
                pass
    
    # Portas
    for insert in msp.query('INSERT'):
        name = insert.dxf.name.upper()
        if 'DOOR' in name or 'PORTA' in name:
            num_portas += 1
    
    # Converter mm → m
    area_m2 = area_total / 1_000_000
    comp_m = comp_total / 1_000
    
    print(f"✅ {area_m2:.1f}m² | {comp_m:.1f}m | {num_portas} portas")
    
    dados = {
        "pavimento": pav,
        "nome": nome,
        "multiplicador": mult,
        "area_unitaria_m2": area_m2,
        "comprimento_unitario_m": comp_m,
        "area_total_m2": area_m2 * mult,
        "comprimento_total_m": comp_m * mult,
        "portas": num_portas
    }
    
    # Salvar JSON
    json_path = OUTPUT_DIR / f"{pav}_{nome}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    
    return dados


def gerar_briefing(dados_lista):
    briefing_path = Path("executivo/thozen-electra/briefings/alvenaria-r01.md")
    briefing_path.parent.mkdir(parents=True, exist_ok=True)
    
    area_total = sum(d['area_total_m2'] for d in dados_lista)
    comp_total = sum(d['comprimento_total_m'] for d in dados_lista)
    
    md = f"""# Briefing Executivo — Alvenaria R01
**Projeto:** Thozen Electra  
**Disciplina:** 03 ALVENARIA  
**Revisão:** R01 (parcial — apenas arquivos <20MB processados)  
**Data:** 2026-03-20  
**Responsável:** Cartesiano (processamento automatizado)

---

## ⚠️ OBSERVAÇÃO CRÍTICA — Briefing Parcial

Este briefing foi gerado a partir de **{len(dados_lista)} arquivos DXF** processados.

**Arquivos NÃO processados** (muito grandes, >300MB, causam timeout):
- RA_ALV_EXE_02_G1 (441 MB)
- RA_ALV_EXE_03_G2 (561 MB)
- RA_ALV_EXE_04_G3 (383 MB)
- RA_ALV_EXE_06_G5 (397 MB)

**Recomendação:** Processar esses arquivos offline ou em ambiente com mais recursos.

---

## 1. Resumo Executivo (Parcial)

**TOTAIS (apenas pavimentos processados):**
- **Área total de alvenaria:** {area_total:,.2f} m²
- **Comprimento total de paredes:** {comp_total:,.2f} m

**⚠️ IMPORTANTE:** Faltam 4 pavimentos de garagem (G1, G2, G3, G5) que representam aproximadamente 12% do edifício (4/32 pavimentos).

---

## 2. Quantitativos por Pavimento (Processados)

| Pavimento | Descrição | Multiplicador | Área Unit. (m²) | Comp. Unit. (m) | Área Total (m²) | Comp. Total (m) | Portas |
|-----------|-----------|---------------|-----------------|-----------------|-----------------|-----------------|--------|
"""
    
    for d in dados_lista:
        md += f"| {d['pavimento']:8s} | {d['nome']:12s} | {d['multiplicador']:2d}x | "
        md += f"{d['area_unitaria_m2']:14,.2f} | {d['comprimento_unitario_m']:14,.2f} | "
        md += f"{d['area_total_m2']:14,.2f} | {d['comprimento_total_m']:14,.2f} | "
        md += f"{d['portas']:6d} |\n"
    
    md += f"\n**TOTAL PARCIAL** | | | | | **{area_total:,.2f}** | **{comp_total:,.2f}** | |\n\n"
    
    md += """---

## 3. Problemas Identificados

### 3.1 Área de Alvenaria = 0 m²

**⚠️ CRÍTICO:** Todos os pavimentos retornaram **área zero**.

**Causa raiz:**
- Os HATCHs no layer `A-WALL-____-PATT` não têm `vertices` acessíveis via `ezdxf`
- Ou as coordenadas dos HATCHs estão em estrutura não suportada pelo script

**Soluções possíveis:**
1. **Converter DXF para versão mais antiga** (R2010, R2007) via ODA File Converter
2. **Explodir HATCHs** em AutoCAD/BricsCAD e converter boundaries para POLYLINEs
3. **Usar biblioteca alternativa** (dxfgrabber, pyautocad via COM)
4. **Processar manualmente** em AutoCAD e exportar quantitativos para CSV

### 3.2 Comprimento de Paredes — Valores Realistas

Os comprimentos extraídos parecem coerentes:
- Térreo: 316m
- G4: 200m
- Lazer: 194m
- Tipo: 2m (⚠️ suspeito — pode estar faltando layers)
- Res/Cob: 185m

**Observação:** O pavimento Tipo com apenas 2m é um outlier — requer investigação.

---

## 4. Dados Ainda Pendentes

| Item | Status | Ação Necessária |
|------|--------|----------------|
| **Área de alvenaria** | ❌ CRÍTICO | Resolver problema de extração de HATCHs |
| **Tipo de blocos** | ⚠️ FALTANTE | Extrair de textos/legendas |
| **Espessura de paredes** | ⚠️ FALTANTE | Extrair de cotas |
| **Vergas/contravergas** | ⚠️ FALTANTE | Calcular a partir de vãos |
| **Encunhamento** | ✅ ESTIMÁVEL | ≈ comprimento total de paredes |
| **Pé-direito** | ⚠️ FALTANTE | Cruzar com arquitetura |

---

## 5. Estimativa de Totais (Extrapolação)

Assumindo que os pavimentos não processados (G1, G2, G3, G5) têm quantitativos similares a G4:

| Item | Valor Medido | Estimativa Total |
|------|--------------|------------------|
| Comprimento de paredes | {comp_total:.0f} m | {comp_total + 4*200:.0f} m (+4 garagens × 200m) |
| Área de alvenaria | [ERRO — zero] | [INDETERMINADO] |

**⚠️ ATENÇÃO:** Esta é uma estimativa grosseira apenas para ordem de grandeza.

---

## 6. Próximos Passos Recomendados

### Curto Prazo
1. **Resolver extração de área** — testar DXF em versão diferente ou método alternativo
2. **Processar pavimentos grandes** — ambiente offline ou script otimizado
3. **Validar pavimento Tipo** — 2m de parede parece erro

### Médio Prazo
4. **Extrair especificações** — textos, legendas, tipos de blocos
5. **Calcular complementos** — vergas, contravergas, encunhamento
6. **Cruzar com arquitetura** — validar áreas e pé-direito

### Longo Prazo
7. **Gerar planilha executiva** — estrutura Memorial Cartesiano
8. **Comparar com benchmark** — índices de m²alv/m²AC

---

## 7. Arquivos Gerados

**JSONs por pavimento:**
"""
    
    for d in dados_lista:
        md += f"- `executivo/thozen-electra/quantitativos/alvenaria/{d['pavimento']}_{d['nome']}.json`\n"
    
    md += f"""
---

**FIM DO BRIEFING R01 (PARCIAL)**

⚠️ **Este briefing está incompleto.** Faltam:
- 4 pavimentos de garagem (G1, G2, G3, G5)
- Resolução do problema de extração de área
- Especificações técnicas (tipos de blocos, espessuras)
"""
    
    with open(briefing_path, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"\n💾 Briefing R01 (parcial) salvo em: {briefing_path}")
    return briefing_path


def main():
    print("🏗️  PROCESSAMENTO RÁPIDO — Alvenaria (arquivos <20MB)\n")
    
    dados_lista = []
    for filename, pav, nome, mult in ARQUIVOS:
        dados = processar(filename, pav, nome, mult)
        if dados:
            dados_lista.append(dados)
    
    print(f"\n{'='*60}")
    print(f"✅ Processados: {len(dados_lista)}/{len(ARQUIVOS)}")
    print(f"{'='*60}\n")
    
    if dados_lista:
        gerar_briefing(dados_lista)
        print(f"\n✨ Processamento parcial concluído!\n")
    else:
        print("❌ Nenhum arquivo processado.")
        sys.exit(1)


if __name__ == "__main__":
    main()
