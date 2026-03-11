#!/usr/bin/env python3
"""
Análise completa das disciplinas na pasta 'completo'
"""

import os
import json
from pathlib import Path

base_path = Path("completo")

# Disciplinas que já processamos
processadas = {
    "06. Ancoragem": "✅ Completo",
    "08. Arquitetura": "✅ Completo (pisos/forros)",
    "17. Esquadrias": "✅ Completo",
    "18. Estrutura": "✅ Completo (fundações + concreto/forma/aço)",
    "19. Gas": "✅ Completo",
    "20. Hidrossanitario": "✅ Completo (água fria/quente, esgoto, pluvial)",
    "21. Impermeabilizacao": "✅ Completo (subsolo + rooftop)",
    "26. Piscinas e Saunas": "✅ Completo",
    "31. Vedacoes": "✅ Completo",
    "33. Telecomunicacoes": "✅ Completo"
}

parciais = {
    "15. Eletrico": "⚠️ Parcial (29% - 69 PDFs falharam)",
    "24. Paisagismo": "⚠️ Parcial (15 espécies - 5 PDFs bloqueados)",
    "27. Prevencao a Incendio": "⚠️ Estimativas (PDFs sem texto)"
}

resultado = {
    "total_disciplinas": 0,
    "processadas": 0,
    "parciais": 0,
    "nao_processadas": 0,
    "disciplinas": {}
}

print("=== ANÁLISE COMPLETA DAS DISCIPLINAS ===\n")
print(f"Pasta base: {base_path}\n")

for disciplina_dir in sorted(base_path.iterdir()):
    if disciplina_dir.is_dir():
        nome = disciplina_dir.name
        resultado["total_disciplinas"] += 1
        
        # Contar arquivos por tipo
        pdfs = list(disciplina_dir.rglob("*.pdf"))
        dwgs = list(disciplina_dir.rglob("*.dwg"))
        excels = list(disciplina_dir.rglob("*.xls*"))
        ifcs = list(disciplina_dir.rglob("*.ifc"))
        
        total_arquivos = len(pdfs) + len(dwgs) + len(excels) + len(ifcs)
        
        # Determinar status
        if nome in processadas:
            status = processadas[nome]
            resultado["processadas"] += 1
        elif nome in parciais:
            status = parciais[nome]
            resultado["parciais"] += 1
        else:
            status = "❌ Não processado"
            resultado["nao_processadas"] += 1
        
        resultado["disciplinas"][nome] = {
            "status": status,
            "pdfs": len(pdfs),
            "dwgs": len(dwgs),
            "excels": len(excels),
            "ifcs": len(ifcs),
            "total": total_arquivos
        }
        
        print(f"{status:50} | {nome:35} | {total_arquivos:3} arquivos ({len(pdfs)} PDFs, {len(dwgs)} DWGs, {len(excels)} Excel, {len(ifcs)} IFC)")

print(f"\n=== RESUMO ===")
print(f"Total de disciplinas: {resultado['total_disciplinas']}")
print(f"  ✅ Completas: {resultado['processadas']} ({resultado['processadas']/resultado['total_disciplinas']*100:.1f}%)")
print(f"  ⚠️ Parciais: {resultado['parciais']} ({resultado['parciais']/resultado['total_disciplinas']*100:.1f}%)")
print(f"  ❌ Não processadas: {resultado['nao_processadas']} ({resultado['nao_processadas']/resultado['total_disciplinas']*100:.1f}%)")

# Salvar JSON
with open("disciplinas/analise-disciplinas-completas.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=2, ensure_ascii=False)

print(f"\n✅ JSON salvo: disciplinas/analise-disciplinas-completas.json")

# Listar disciplinas não processadas com mais de 10 arquivos
print(f"\n=== DISCIPLINAS NÃO PROCESSADAS COM POTENCIAL ===")
print("(disciplinas com >10 arquivos que podem ter quantitativos importantes)\n")

for nome, dados in sorted(resultado["disciplinas"].items(), key=lambda x: -x[1]["total"]):
    if dados["status"] == "❌ Não processado" and dados["total"] > 10:
        print(f"  {nome:35} | {dados['total']:3} arquivos ({dados['pdfs']} PDFs, {dados['dwgs']} DWGs, {dados['excels']} Excel)")
