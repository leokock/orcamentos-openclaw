from pathlib import Path
import csv, re, unicodedata
from collections import Counter, defaultdict
import ifcopenshell

SRC = Path('G:/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/Alfa Incorporadora/Arquivos recebidos/01. PROJETOS/Instalações Atualizadas/Quantitativos fornecidos')
OUT = Path('executivos/alfa-colinas')
FILES = {
  'sanitario': (SRC/'Sanitário'/'11_MOT-SAN-V01-EX-R01.ifc', OUT/'02-sanitario'/'extracao-ifc-por-pavimento.csv'),
  'telecom': (SRC/'Telecomunicações'/'12_ALF-TEL-EX-V01-R00.ifc', OUT/'03-telecom'/'extracao-ifc-por-pavimento.csv'),
}

def clean(s): return '' if s is None else str(s).strip()

def get_storey(obj):
    try:
        rels = getattr(obj, 'ContainedInStructure', None) or []
        for rel in rels:
            st = getattr(rel, 'RelatingStructure', None)
            if st and st.is_a('IfcBuildingStorey'):
                return clean(getattr(st,'Name',''))
    except Exception: pass
    # fallback: decompose nesting
    try:
        for rel in getattr(obj,'Decomposes',[]) or []:
            parent=getattr(rel,'RelatingObject',None)
            if parent and parent.is_a('IfcBuildingStorey'):
                return clean(getattr(parent,'Name',''))
    except Exception: pass
    return 'sem_pavimento'

def type_name(obj):
    t=''
    try:
        for rel in getattr(obj,'IsTypedBy',[]) or []:
            tt=getattr(rel,'RelatingType',None)
            if tt: t=clean(getattr(tt,'Name','')) or clean(getattr(tt,'ObjectType',''))
    except Exception: pass
    return t or clean(getattr(obj,'Name','')) or obj.is_a()

def system(obj):
    # lightweight classification by class/type/name
    txt=' '.join([obj.is_a(), type_name(obj), clean(getattr(obj,'Name','')), clean(getattr(obj,'ObjectType',''))]).lower()
    if any(x in txt for x in ['pipe','tubo','sanit','esgoto','agua','pluvial','ralo','caixa gordura','caixa']): return 'tubos/conexões/caixas'
    if any(x in txt for x in ['cable','cabo','tray','eletrocalha','eletroduto','conduit']): return 'cabeamento/infraestrutura'
    if any(x in txt for x in ['terminal','outlet','tomada','rj45','caixa']): return 'pontos/terminais'
    return 'outros elementos'

def extract(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    model=ifcopenshell.open(str(src))
    rows=[]; total=0
    skip={'IfcProject','IfcSite','IfcBuilding','IfcBuildingStorey','IfcSpace','IfcOpeningElement','IfcAnnotation','IfcGrid','IfcBuildingElementProxy'}
    for obj in model.by_type('IfcProduct'):
        if obj.is_a() in skip: continue
        total+=1
        rows.append((get_storey(obj), system(obj), obj.is_a(), type_name(obj)))
    cnt=Counter(rows)
    with open(dst,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['pavimento','sistema','classe_ifc','tipo_nome','quantidade','fonte','status','observacao'])
        for (pav,sis,cls,typ),q in sorted(cnt.items()):
            w.writerow([pav,sis,cls,typ,q,src.name,'ok_ifc','contagem de IfcProduct por pavimento; validar unidade/escala antes de usar como quantitativo absoluto'])
    return total, len(cnt), len(set(r[0] for r in rows))

for disc,(src,dst) in FILES.items():
    if src.exists(): print(disc, extract(src,dst))
