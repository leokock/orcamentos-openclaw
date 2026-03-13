#!/usr/bin/env python3
"""
Extrai volumes de concreto usando cálculo geométrico direto (ifcopenshell.geom)
Para resolver o problema de vigas e pilares com volume = 0
"""

import ifcopenshell
import ifcopenshell.geom
from collections import defaultdict

print("🔧 Extraindo volumes por cálculo geométrico...")

# Configurações
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)

# Carregar IFC
ifc_path = "/Users/leokock/orcamentos/projetos/mussi-oxford/02. PROJETO ESTRUTURAL/EST 260305/IFC 260305/EST_OXFORD600.12.11.2025.ifc"
print(f"📂 Carregando: {ifc_path}")
ifc = ifcopenshell.open(ifc_path)

# Processar amostra (vigas, pilares, lajes)
tipos = {
    'IfcBeam': 'Vigas',
    'IfcColumn': 'Pilares',
    'IfcSlab': 'Lajes'
}

resultados = defaultdict(lambda: {'count': 0, 'volume_total': 0, 'com_volume': 0, 'sem_volume': 0})

for ifc_type, nome in tipos.items():
    print(f"\n📊 Processando {nome} ({ifc_type})...")
    elementos = ifc.by_type(ifc_type)
    
    # Processar amostra (primeiros 50 para não demorar muito)
    amostra = elementos[:50] if len(elementos) > 50 else elementos
    
    for idx, elem in enumerate(amostra):
        try:
            # Tentar criar geometria
            shape = ifcopenshell.geom.create_shape(settings, elem)
            
            # Extrair volume da geometria
            # O volume está em unidades do IFC (normalmente metros cúbicos)
            geometry = shape.geometry
            
            # ifcopenshell.geom retorna volume em verts/faces, precisamos calcular
            # Tentar pegar do solid diretamente se disponível
            if hasattr(geometry, 'volume'):
                volume = geometry.volume
            else:
                # Alternativa: calcular bounding box aproximado
                verts = geometry.verts
                if len(verts) >= 3:
                    # Pegar min/max de cada coordenada
                    xs = [verts[i] for i in range(0, len(verts), 3)]
                    ys = [verts[i+1] for i in range(0, len(verts), 3)]
                    zs = [verts[i+2] for i in range(0, len(verts), 3)]
                    
                    # Volume aproximado do bounding box
                    width = max(xs) - min(xs)
                    depth = max(ys) - min(ys)
                    height = max(zs) - min(zs)
                    volume = width * depth * height
                else:
                    volume = 0
            
            if volume > 0:
                resultados[ifc_type]['volume_total'] += volume
                resultados[ifc_type]['com_volume'] += 1
            else:
                resultados[ifc_type]['sem_volume'] += 1
            
            resultados[ifc_type]['count'] += 1
            
            if (idx + 1) % 10 == 0:
                print(f"  Processados: {idx+1}/{len(amostra)}")
        
        except Exception as e:
            resultados[ifc_type]['sem_volume'] += 1
            resultados[ifc_type]['count'] += 1
    
    # Resumo
    res = resultados[ifc_type]
    print(f"  ✓ Total amostra: {res['count']}")
    print(f"    Com volume: {res['com_volume']} ({res['volume_total']:.2f} m³)")
    print(f"    Sem volume: {res['sem_volume']}")
    
    if res['com_volume'] > 0:
        media = res['volume_total'] / res['com_volume']
        total_elementos = len(elementos)
        projecao_total = media * total_elementos
        print(f"    → Média: {media:.4f} m³/elemento")
        print(f"    → Projeção total ({total_elementos} elementos): {projecao_total:.2f} m³")

print("\n✅ Análise geométrica concluída!")
