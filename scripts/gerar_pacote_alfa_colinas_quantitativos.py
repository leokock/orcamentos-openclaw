from pathlib import Path
import csv, re, unicodedata, datetime
from collections import defaultdict, Counter
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

SRC = Path('G:/Drives compartilhados/03 CTN Projetos/2. Projetos em Andamento/Alfa Incorporadora/Arquivos recebidos/01. PROJETOS/Instalações Atualizadas/Quantitativos fornecidos')
OUT = Path('executivos/alfa-colinas')
DISC = {
    'pci': {'ord':'01', 'src': SRC/'PCI', 'plan': SRC/'PCI'/'QUANTITATIVO PCI.xlsx', 'title':'PCI'},
    'sanitario': {'ord':'02', 'src': SRC/'Sanitário', 'plan': SRC/'Sanitário'/'12-ALF-DC-SAN-R00-QUANTITATIVOS.xlsx', 'title':'Sanitário'},
    'telecom': {'ord':'03', 'src': SRC/'Telecomunicações', 'plan': SRC/'Telecomunicações'/'12-ALF-DC-TEL-R00-QUANTITATIVOS.xlsx', 'title':'Telecom'},
}
HEAD = ['disciplina','grupo','sistema','item','unidade','quantidade','pavimento','fonte','status','observacao']

def norm(s):
    s='' if s is None else str(s)
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower().strip()

def clean(s): return '' if s is None else str(s).strip()

def is_num(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool)

def classify_file(p):
    n=norm(p.name); ext=p.suffix.lower()
    if ext=='.xlsx': return 'planilha projetista' if 'quantitativo' in n else 'planilha apoio/referência'
    if ext=='.ifc': return 'modelo IFC'
    if ext=='.rvt': return 'modelo RVT'
    if ext=='.pdf': return 'prancha PDF' if any(t in n for t in ['plb','pav','subsolo','terreo','cobertura','detalh','implantacao','esquema','corte']) else 'memorial/licença'
    if ext=='.dwg': return 'DWG'
    return 'apoio/obsoleto'

def inventory():
    rows=[]
    for disc, cfg in DISC.items():
        for p in sorted(cfg['src'].rglob('*')):
            if p.is_file():
                st=p.stat(); rows.append({
                    'disciplina': disc, 'tipo': p.suffix.lower().lstrip('.') or 'arquivo', 'arquivo': p.name,
                    'caminho_relativo': str(p.relative_to(SRC)).replace('\\','/'), 'bytes': st.st_size,
                    'data_modificacao': datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds'),
                    'papel': classify_file(p)})
    for p in sorted(SRC.glob('*.xlsx')):
        st=p.stat(); rows.append({'disciplina':'referencia-aquos','tipo':'xlsx','arquivo':p.name,'caminho_relativo':str(p.relative_to(SRC)).replace('\\','/'),'bytes':st.st_size,'data_modificacao':datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds'),'papel':'planilha apoio/referência Aquos (fora das 3 pastas)'})
    (OUT/'00-projeto').mkdir(parents=True, exist_ok=True)
    with open(OUT/'00-projeto'/'inventario-arquivos.csv','w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f, fieldnames=['disciplina','tipo','arquivo','caminho_relativo','bytes','data_modificacao','papel'])
        w.writeheader(); w.writerows(rows)
    return rows

def parse_pci(path):
    wb=openpyxl.load_workbook(path, data_only=True)
    out=[]; sheet_stats={}
    for ws in wb.worksheets:
        grupo=ws.title; pav=''; n=0
        for row in ws.iter_rows(values_only=True):
            vals=[v for v in row if v not in (None,'')]
            if not vals: continue
            first=clean(vals[0]); nfirst=norm(first)
            if nfirst.startswith('pavimento') or nfirst in ['tubulacao aco galvanizado 2.1/2','tubulacao aco galvanizado 2']:
                if len(vals)==1 or not is_num(vals[0]): pav=first
            # table rows: [N, ITEM, UNIDADE, QUANTIDADE] or [ITEM, unidade, quantidade]
            if len(row)>=4 and is_num(row[0]) and clean(row[1]) and clean(row[2]) and is_num(row[3]):
                out.append({'disciplina':'pci','grupo':grupo,'sistema':grupo,'item':clean(row[1]),'unidade':clean(row[2]),'quantidade':row[3],'pavimento':pav,'fonte':path.name+' / '+ws.title,'status':'ok_planilha','observacao':'quantitativo por pavimento/agrupamento conforme planilha PCI'}) ; n+=1
            elif len(row)>=3 and clean(row[0]) and clean(row[1]) and is_num(row[2]) and not is_num(row[0]):
                out.append({'disciplina':'pci','grupo':grupo,'sistema':grupo,'item':clean(row[0]),'unidade':clean(row[1]),'quantidade':row[2],'pavimento':pav,'fonte':path.name+' / '+ws.title,'status':'ok_planilha','observacao':'linha sem número sequencial na planilha original'}) ; n+=1
        sheet_stats[ws.title]=n
    return out, {'abas':len(wb.sheetnames),'sheet_stats':sheet_stats,'itens':len(out)}

def parse_lista_materiais(path, disc):
    wb=openpyxl.load_workbook(path, data_only=True)
    ws=wb.active
    out=[]; grupo=''; sistema=''; headers=0
    for row in ws.iter_rows(values_only=True):
        vals=[v for v in row if v not in (None,'')]
        if not vals: continue
        nvals=[norm(v) for v in vals]
        if len(vals)==1 and not is_num(vals[0]):
            txt=clean(vals[0])
            if norm(txt) not in ['obra','lista de materiais']:
                grupo=txt; sistema=txt
            continue
        if len(vals)>=5 and norm(vals[0]) in ['no','n','nº']:
            headers+=1; continue
        if len(row)>=5 and is_num(row[0]) and clean(row[1]) and clean(row[2]) and is_num(row[3]):
            sistema=grupo or 'Lista de Materiais'
            out.append({'disciplina':disc,'grupo':grupo or 'Lista de Materiais','sistema':sistema,'item':clean(row[2]),'unidade':clean(row[4]),'quantidade':row[3],'pavimento':'','fonte':path.name+' / Lista de Materiais','status':'ok_planilha','observacao':'quantitativo consolidado sem pavimento na planilha projetista'})
    return out, {'abas':len(wb.sheetnames),'sheet_stats':{ws.title:len(out)},'itens':len(out),'headers':headers}

def summary(rows):
    c=defaultdict(float)
    for r in rows:
        try: c[(r['grupo'],r['unidade'])]+=float(r['quantidade'])
        except Exception: pass
    return [{'grupo':g,'unidade':u,'quantidade_total':q} for (g,u),q in sorted(c.items())]

def write_wb(disc, rows, stats, ifc_csv=None):
    folder=OUT/f"{DISC[disc]['ord']}-{disc}"; folder.mkdir(parents=True, exist_ok=True)
    wb=Workbook(); ws=wb.active; ws.title='Consolidado'; ws.append(HEAD)
    for r in rows: ws.append([r.get(h,'') for h in HEAD])
    style_sheet(ws)
    ws2=wb.create_sheet('Resumo por Grupo'); ws2.append(['grupo','unidade','quantidade_total'])
    for r in summary(rows): ws2.append([r['grupo'],r['unidade'],r['quantidade_total']])
    style_sheet(ws2)
    if ifc_csv and Path(ifc_csv).exists():
        ws3=wb.create_sheet('Por Pavimento (IFC)')
        with open(ifc_csv, encoding='utf-8-sig') as f:
            for row in csv.reader(f): ws3.append(row)
        style_sheet(ws3)
    ws4=wb.create_sheet('Notas IFC')
    notes=[]
    if ifc_csv and Path(ifc_csv).exists():
        notes=[['status','IFC processado com ifcopenshell; usar distribuição por pavimento como apoio e validar famílias/unidades antes de usar comprimentos/áreas.'],['arquivo',Path(ifc_csv).name]]
    else:
        notes=[['status','Não havia IFC útil nesta disciplina ou não foi fornecido IFC na pasta.'],['impacto','Pavimento vem apenas da planilha/projetos em PDF/DWG; distribuição fina pode exigir conferência manual.']]
    for r in notes: ws4.append(r)
    style_sheet(ws4)
    ws5=wb.create_sheet('Totais'); ws5.append(['métrica','valor'])
    ws5.append(['linhas consolidadas',len(rows)]); ws5.append(['grupos',len(set(r['grupo'] for r in rows))]); ws5.append(['abas origem',stats.get('abas','')])
    style_sheet(ws5)
    wb.save(folder/f'quantitativos-{disc}.xlsx')

def style_sheet(ws):
    for c in ws[1]: c.font=Font(bold=True, color='FFFFFF'); c.fill=PatternFill('solid', fgColor='1F4E78'); c.alignment=Alignment(horizontal='center')
    ws.freeze_panes='A2'
    for col in range(1, min(ws.max_column, 12)+1): ws.column_dimensions[get_column_letter(col)].width=22

def audit_md(disc, rows, stats, inv, ifc_exists):
    folder=OUT/f"{DISC[disc]['ord']}-{disc}"; folder.mkdir(parents=True, exist_ok=True)
    src=DISC[disc]['plan']
    files=[r for r in inv if r['disciplina']==disc]
    by_papel=Counter(r['papel'] for r in files)
    pav_count=sum(1 for r in rows if r.get('pavimento'))
    groups=Counter(r['grupo'] for r in rows)
    total_qty=sum(float(r['quantidade']) for r in rows if isinstance(r['quantidade'],(int,float)))
    lines=[]
    lines += [f"# Auditoria — {DISC[disc]['title']}","",f"Fonte principal: `{src}`",f"Revisão identificada: R00 / quantitativo fornecido pelo projetista.",""]
    lines += ["## Estrutura da planilha",f"- Abas: {stats.get('abas')}",f"- Linhas normalizadas: {len(rows)}",f"- Grupos/sistemas: {len(groups)}",f"- Linhas com pavimento explícito: {pav_count}",f"- Soma bruta de quantidades (unidades mistas, só controle): {total_qty:,.2f}",""]
    lines += ["## Grupos principais"]
    for g,n in groups.most_common(12): lines.append(f"- {g}: {n} linhas")
    lines += ["", "## Material complementar encontrado"]
    for papel,n in by_papel.items(): lines.append(f"- {papel}: {n} arquivo(s)")
    lines += ["", "## Totais declarados vs soma calculada", "- A planilha não traz um quadro final único auditável por unidade; o workbook entregue consolida por grupo e unidade na aba `Resumo por Grupo`."]
    if disc=='pci': lines.append("- PCI possui pavimentos/agrupamentos na própria planilha, mas vários itens são por pavimento-tipo; conferir multiplicadores antes de orçamento fechado.")
    else: lines.append("- Sanitário/Telecom têm lista de materiais consolidada sem pavimento na planilha; distribuição por pavimento depende do IFC/DWG.")
    lines += ["", "## IFC",]
    lines.append("- IFC útil encontrado e extraído para `extracao-ifc-por-pavimento.csv`. Usar como apoio de distribuição, não como medição absoluta sem validação de unidade/escala." if ifc_exists else "- Não há IFC na pasta desta disciplina; sem extração por pavimento.")
    lines += ["", "## Inconsistências / atenção",]
    if disc=='pci': lines += ["- Sem IFC PCI para conferência espacial; existem PDFs por pavimento e planilha própria.", "- O arquivo PCI inclui `GÁS`; manter em PCI somente se o escopo de orçamento tratar gás junto com prevenção/incêndio."]
    if disc=='sanitario': lines += ["- Planilha consolidada não informa pavimento por item; IFC sanitário deve ser usado para distribuição auxiliar.", "- Há PDFs/DWGs por pavimento, inclusive furação de subsolo; conferir interferências e pontos não materializados no quantitativo."]
    if disc=='telecom': lines += ["- Planilha consolidada não informa pavimento por item; IFC telecom deve ser usado para distribuição auxiliar.", "- Cabeamento e infraestrutura podem exigir validação manual de rotas/metros no DWG/IFC."]
    lines += ["", "## Recomendação objetiva", "- Usar `quantitativos-"+disc+".xlsx` como base normalizada de orçamento.", "- Usar IFC apenas para rateio/checagem de cobertura por pavimento quando presente.", "- Antes de fechar custo, confirmar lacunas documentadas nos arquivos `gap-*.md`."]
    (folder/'audit-planilha-projetista.md').write_text('\n'.join(lines), encoding='utf-8')

def gap_files():
    gaps={
      'pci': {'gap-ifc-pci.md': ['PCI sem IFC','Existem planilha e PDFs por pavimento, mas não foi fornecido modelo IFC PCI.','Risco de divergência de distribuição por pavimento e retrabalho em itens lineares/rotas.','Recomendação: usar planilha como quantitativo base e PDFs para conferência; pedir IFC PCI se for necessário rateio fino por pavimento.']},
      'sanitario': {'gap-pavimento-planilha.md': ['Sanitário sem pavimento na planilha','A planilha ALF-DC-SAN consolida itens sem coluna de pavimento. Há IFC e DWGs para apoio.','Risco de dificuldade na ligação Visus↔Excel por pavimento e alocação de compras/medição.','Recomendação: usar o CSV do IFC para distribuição auxiliar e confirmar itens críticos com projetista.']},
      'telecom': {'gap-cabeamento-pavimento.md': ['Telecom sem pavimento na planilha','A planilha ALF-DC-TEL consolida lista de materiais, inclusive cabeamento/caixas, sem pavimento por item. Há IFC e DWGs.','Risco de sub/superalocação de cabos e infraestrutura em pavimentos-tipo.','Recomendação: validar comprimentos de cabos/eletrodutos no DWG/IFC antes do orçamento fechado.']}
    }
    for disc, fs in gaps.items():
        folder=OUT/f"{DISC[disc]['ord']}-{disc}"; folder.mkdir(parents=True, exist_ok=True)
        for fn, parts in fs.items():
            title, existe, risco, rec=parts
            txt=f"# {title}\n\n## Conclusão\n{title}.\n\n## O que existe\n{existe}\n\n## O que falta\nComplemento/validação para distribuição por pavimento ou escopo específico.\n\n## Risco para orçamento\n{risco}\n\n## Opções\n- Orçar provisoriamente com a planilha normalizada.\n- Validar contra PDF/DWG/IFC.\n- Solicitar complemento ao projetista.\n\n## Recomendação\n{rec}\n\n## Texto sugerido ao projetista\nFavor enviar complemento de quantitativos por pavimento e/ou modelo IFC da disciplina para conferência de distribuição e rastreabilidade do orçamento executivo.\n"
            (folder/fn).write_text(txt, encoding='utf-8')

def strategy_md(inv, counts):
    lines=["# Alfa Colinas — Análise e estratégia de quantitativos", "", "Pacote montado no padrão `00-projeto + 01-pci + 02-sanitario + 03-telecom`.", "", "## Entregáveis", "- `00-projeto/inventario-arquivos.csv` — inventário de arquivos recebidos.", "- `01-pci/quantitativos-pci.xlsx` + auditoria + gap IFC.", "- `02-sanitario/quantitativos-sanitario.xlsx` + auditoria + extração IFC por pavimento.", "- `03-telecom/quantitativos-telecom.xlsx` + auditoria + extração IFC por pavimento.", "", "## Estratégia por disciplina"]
    lines += [f"- PCI: {counts['pci']} linhas normalizadas a partir da planilha do projetista; sem IFC, usar PDFs por pavimento para conferência.", f"- Sanitário: {counts['sanitario']} linhas normalizadas; planilha sem pavimento, IFC/DWG usados para distribuição auxiliar.", f"- Telecom: {counts['telecom']} linhas normalizadas; planilha sem pavimento, IFC/DWG usados para distribuição auxiliar.", "", "## Gaps principais", "- PCI: ausência de IFC PCI (`01-pci/gap-ifc-pci.md`).", "- Sanitário: planilha sem coluna de pavimento (`02-sanitario/gap-pavimento-planilha.md`).", "- Telecom: cabeamento/infra sem coluna de pavimento (`03-telecom/gap-cabeamento-pavimento.md`).", "", "## Observação", "As planilhas `CTN-BLH-AQS` na raiz foram inventariadas como apoio/referência Aquos, mas os quantitativos normalizados usam as fontes ALFA dentro das três pastas solicitadas."]
    (OUT/'00-projeto'/'ANALISE-ESTRATEGIA.md').write_text('\n'.join(lines), encoding='utf-8')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    inv=inventory()
    counts={}; data={}; stats={}
    data['pci'], stats['pci']=parse_pci(DISC['pci']['plan'])
    data['sanitario'], stats['sanitario']=parse_lista_materiais(DISC['sanitario']['plan'],'sanitario')
    data['telecom'], stats['telecom']=parse_lista_materiais(DISC['telecom']['plan'],'telecom')
    for disc in DISC:
        ifc=OUT/f"{DISC[disc]['ord']}-{disc}"/'extracao-ifc-por-pavimento.csv'
        write_wb(disc, data[disc], stats[disc], ifc if ifc.exists() else None)
        audit_md(disc, data[disc], stats[disc], inv, ifc.exists())
        counts[disc]=len(data[disc])
    gap_files(); strategy_md(inv, counts)
    print(counts)

if __name__=='__main__': main()
