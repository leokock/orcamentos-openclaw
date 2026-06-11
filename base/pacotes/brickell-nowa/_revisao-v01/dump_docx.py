import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from docx import Document
for name in ['brickell-nowa-PREMISSAS-ORIGEM-v00-final.docx','brickell-nowa-JUSTIFICATIVA-ITENS-ACIMA-MEDIA-v00-final.docx','brickell-nowa-ANALISE-DETALHADA-COMPARATIVO-SIMILARES-v00.docx']:
    print(f"\n########## {name} ##########")
    d = Document(name)
    for el in d.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            from docx.text.paragraph import Paragraph
            t = Paragraph(el, d).text.strip()
            if t: print("P:", t)
        elif tag == 'tbl':
            from docx.table import Table
            tb = Table(el, d)
            for row in tb.rows:
                print("T:", " | ".join(c.text.strip() for c in row.cells))
