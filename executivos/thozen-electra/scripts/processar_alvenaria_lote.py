#!/usr/bin/env python3.11
"""
Processador em Lote — Alvenaria Thozen Electra
Processa todos os DXFs disponíveis e gera briefing R01

Uso: python3.11 scripts/processar_alvenaria_lote.py
"""

import sys
import json
from pathlib import Path
from collections import defaultdict
import math

try:
    import ezdxf
except ImportError:
    print("❌ pip3.11 install ezdxf")
    sys.exit(1)


# Configuração
DXF_DIR = Path("projetos/thozen-electra/dxf-temp")
OUTPUT_DIR = Path("executivo/thozen-electra/quantitativos/alvenaria")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Mapeamento arquivo → pavimento
MAPA_PAVIMENTOS = {
    "RA_ALV_EXE_01_ TÉRREO PRÉ-EXECUTIVO_R01.dxf": {"pav": "01", "nome": "Térreo", "mult": 1},
    "RA_ALV_EXE_02_G1 PRÉ-EXECUTIVO_R01.dxf": {"pav": "02", "nome": "G1", "mult": 1},
    "RA_ALV_EXE_03_G2 PRÉ-EXECUTIVO_R01.dxf": {"pav": "03", "nome": "G2", "mult": 1},
    "RA_ALV_EXE_04_G3 PRÉ-EXECUTIVO_R01.dxf": {"pav": "04", "nome": "G3", "mult": 1},
    "RA_ALV_EXE_05_G4 PRÉ-EXECUTIVO_R01.dxf": {"pav": "05", "nome": "G4", "mult": 1},
    "RA_ALV_EXE_06_G5 PRÉ-EXECUTIVO_R01.dxf": {"pav": "06", "nome": "G5", "mult": 1},
    "RA_ALV_EXE_07_ LAZER PRÉ EXECUTIVO_R01.dxf": {"pav": "07", "nome": "Lazer", "mult": 1},
    "RA_ALV_EXE_08_ TIPOS PRÉ EXECUTIVO_R01.dxf": {"pav": "08-31", "nome": "Tipo", "mult": 24},
    "RA_ALV_EXE_09_ RES E COB PRÉ-EXECUTIVO_R01.dxf": {"pav": "32", "nome": "Res/Cob", "mult": 1},
}

# Layers relevantes
LAYERS_AREA = ['A-WALL-____-PATT', 'A-WALL-____-IDEN']  # HATCHs de alvenaria
LAYERS_COMP = ['A-WALL-____-OTLN']  # Contornos de paredes


def calcular_area_polyline(points) -> float:
    """Calcula área via Shoelace."""
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


def processar_dxf(dxf_path: Path, info_pav: dict) -> dict:
    """Processa um arquivo DXF e retorna quantitativos."""
    print(f"  🔄 {info_pav['nome']}...", end=" ", flush=True)
    
    try:
        doc = ezdxf.readfile(str(dxf_path))
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None
    
    msp = doc.modelspace()
    
    area_total = 0
    comp_total = 0
    num_portas = 0
    num_janelas = 0
    
    # HATCHs (áreas)
    for hatch in msp.query('HATCH'):
        if hatch.dxf.layer not in LAYERS_AREA:
            continue
        try:
            for path in hatch.paths:
                if hasattr(path, 'vertices'):
                    area = calcular_area_polyline(path.vertices)
                    if area > 1:  # Filtrar hatchs pequenos (legendas, etc.)
                        area_total += area
        except:
            pass
    
    # LINEs (comprimentos)
    for line in msp.query('LINE'):
        if line.dxf.layer not in LAYERS_COMP:
            continue
        try:
            start = line.dxf.start
            end = line.dxf.end
            comp = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            if comp > 0.1:  # Filtrar linhas minúsculas
                comp_total += comp
        except:
            pass
    
    # INSERTs (vãos)
    for insert in msp.query('INSERT'):
        name = insert.dxf.name.upper()
        if 'DOOR' in name or 'PORTA' in name:
            num_portas += 1
        elif 'WINDOW' in name or 'JANELA' in name or 'GLAZ' in name:
            num_janelas += 1
    
    # Converter unidades (assumir que DXF está em mm)
    area_m2 = area_total / 1_000_000  # mm² → m²
    comp_m = comp_total / 1_000        # mm → m
    
    print(f"✅ {area_m2:.1f}m² | {comp_m:.1f}m")
    
    return {
        "pavimento": info_pav['pav'],
        "nome": info_pav['nome'],
        "multiplicador": info_pav['mult'],
        "area_unitaria_m2": area_m2,
        "comprimento_unitario_m": comp_m,
        "area_total_m2": area_m2 * info_pav['mult'],
        "comprimento_total_m": comp_m * info_pav['mult'],
        "portas": num_portas,
        "janelas": num_janelas
    }


def gerar_briefing_r01(dados_pavimentos: list):
    """Gera briefing R01 com quantitativos extraídos."""
    briefing_path = Path("executivo/thozen-electra/briefings/alvenaria-r01.md")
    briefing_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Calcular totais
    area_total = sum(d['area_total_m2'] for d in dados_pavimentos)
    comp_total = sum(d['comprimento_total_m'] for d in dados_pavimentos)
    
    # Gerar markdown
    md = f"""# Briefing Executivo — Alvenaria R01
**Projeto:** Thozen Electra  
**Disciplina:** 03 ALVENARIA  
**Revisão:** R01 (quantitativos extraídos de DXF)  
**Data:** 2026-03-20  
**Responsável:** Cartesiano (processamento automatizado)

---

## 1. Resumo Executivo

Quantitativos extraídos de **{len(dados_pavimentos)} arquivos DXF** processados com sucesso.

**TOTAIS GLOBAIS:**
- **Área total de alvenaria:** {area_total:,.2f} m²
- **Comprimento total de paredes:** {comp_total:,.2f} m

---

## 2. Quantitativos por Pavimento

| Pavimento | Descrição | Multiplicador | Área Unit. (m²) | Comp. Unit. (m) | Área Total (m²) | Comp. Total (m) | Portas | Janelas |
|-----------|-----------|---------------|-----------------|-----------------|-----------------|-----------------|--------|---------|
"""
    
    for d in dados_pavimentos:
        md += f"| {d['pavimento']:8s} | {d['nome']:12s} | {d['multiplicador']:2d}x | "
        md += f"{d['area_unitaria_m2']:14,.2f} | {d['comprimento_unitario_m']:14,.2f} | "
        md += f"{d['area_total_m2']:14,.2f} | {d['comprimento_total_m']:14,.2f} | "
        md += f"{d['portas']:6d} | {d['janelas']:7d} |\n"
    
    md += f"\n**TOTAL** | | | | | **{area_total:,.2f}** | **{comp_total:,.2f}** | | |\n\n"
    
    md += """---

## 3. Observações

### 3.1 Dados Extraídos com Sucesso
- ✅ Área de alvenaria por pavimento (via HATCHs no layer `A-WALL-____-PATT`)
- ✅ Comprimento de paredes (via LINEs no layer `A-WALL-____-OTLN`)
- ✅ Contagem de portas e janelas (via blocos INSERTs)

### 3.2 Dados Ainda Pendentes
- ⚠️ **Tipo de blocos especificados** — requer análise de legendas/textos
- ⚠️ **Espessura de paredes** — requer análise de cotas
- ⚠️ **Vergas e contravergas** — calcular com base em vãos (comprimento vão + 60cm)
- ⚠️ **Encunhamento** — calcular perímetro de paredes (≈ comprimento total)
- ⚠️ **Pé-direito** — requer cruzamento com projeto arquitetônico

### 3.3 Validação de Dados

#### Comparação Garagens (G1~G5)
Esperado: pavimentos similares devem ter quantitativos próximos.

#### Multiplicador de Tipos
- Pavimento **Tipo** (08-31) foi multiplicado por **24** (8° ao 31° pavimento)
- Confirmar se todos os 24 pavimentos são idênticos

#### Ordem de Grandeza
- Área total: **{area_total:,.0f} m²** — verificar se está coerente com área construída total
- Comp. médio por pav.: **{comp_total/32:,.0f} m/pav** (média dos 32 pavimentos)

---

## 4. Próximos Passos

1. **Analisar legendas/textos** para extrair tipos de blocos e espessuras
2. **Calcular vergas/contravergas** — comprimento = Σ(vãos) × 1.6 (vão + 30cm cada lado)
3. **Calcular encunhamento** — comprimento ≈ comprimento total de paredes
4. **Cruzar com arquitetura** — validar pé-direito e área total
5. **Gerar planilha Excel** — estrutura Memorial Cartesiano (N1 09 Alvenaria)

---

**FIM DO BRIEFING R01**
"""
    
    with open(briefing_path, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"\n💾 Briefing R01 salvo em: {briefing_path}")
    return briefing_path


def main():
    print("🏗️  PROCESSAMENTO EM LOTE — Alvenaria Thozen Electra\n")
    
    # Verificar diretório
    if not DXF_DIR.exists():
        print(f"❌ Diretório não encontrado: {DXF_DIR}")
        sys.exit(1)
    
    # Processar DXFs
    dados_pavimentos = []
    processados = 0
    erros = 0
    
    for filename, info_pav in MAPA_PAVIMENTOS.items():
        dxf_path = DXF_DIR / filename
        
        if not dxf_path.exists():
            print(f"  ⏭️  {info_pav['nome']} — arquivo não encontrado")
            erros += 1
            continue
        
        dados = processar_dxf(dxf_path, info_pav)
        if dados:
            dados_pavimentos.append(dados)
            processados += 1
            
            # Salvar JSON individual
            nome_safe = info_pav['nome'].replace('/', '-')
            json_path = OUTPUT_DIR / f"{info_pav['pav']}_{nome_safe}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        else:
            erros += 1
    
    # Resumo
    print(f"\n{'='*60}")
    print(f"✅ Processados: {processados}/{len(MAPA_PAVIMENTOS)}")
    if erros > 0:
        print(f"❌ Erros/não encontrados: {erros}")
    print(f"{'='*60}\n")
    
    # Gerar briefing R01
    if dados_pavimentos:
        briefing_path = gerar_briefing_r01(dados_pavimentos)
        print(f"\n✨ Processamento concluído! Briefing R01 disponível em:\n   {briefing_path}\n")
    else:
        print("❌ Nenhum DXF foi processado com sucesso.")
        sys.exit(1)


if __name__ == "__main__":
    main()
