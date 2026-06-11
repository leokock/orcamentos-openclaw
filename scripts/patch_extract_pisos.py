"""
Cria extract_colinas_pisos.py - versao filtrada so para PISOS E PAVIMENTACOES
"""
import os

src = r'C:\Users\leona\orcamentos\planejamento\OBRA - Colinas\06. Dimensionamento de recursos\extract_colinas.py'
dst = r'C:\Users\leona\orcamentos\planejamento\OBRA - Colinas\06. Dimensionamento de recursos\extract_colinas_pisos.py'

with open(src, encoding='utf-8') as f:
    content = f.read()

# Patch 1: change output file name
old_out = 'OUTPUT_FILE = "COL_Extracao_Quantidades.xlsx"'
new_out = 'OUTPUT_FILE = "COL_Extracao_PisosPavimentacoes.xlsx"\nCC_FILTER = {"PISOS E PAVIMENTA\u00c7\u00d5ES"}'
assert old_out in content, f"Nao encontrou: {old_out}"
content = content.replace(old_out, new_out, 1)

# Patch 2: add CC filter in output loop
old_loop = 'for cc_name, svc_list in cc_groups.items():\n        visus_svcs'
new_loop = 'for cc_name, svc_list in cc_groups.items():\n        if cc_name not in CC_FILTER:\n            continue\n        visus_svcs'
assert old_loop in content, f"Nao encontrou loop: {repr(old_loop[:60])}"
content = content.replace(old_loop, new_loop, 1)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Salvo: {dst}")
