# -*- coding: utf-8 -*-
"""Placon Hermann — gera PREMISSAS-ORIGEM.md e JUSTIFICATIVA md (VERSAO FINAL), converte p/ docx.
Numeros = tabela de macrogrupos VALIDADA (v05): parametrico v01 + validacao BIM de arquitetura
+ parede diafragma na infraestrutura. AC/UR confirmados no projeto legal R05 (prancha 02)."""
import os, sys, json, datetime
sys.path.insert(0, r"C:\Users\leona\openclaw\data\scripts-orcamento")
from md_to_docx_arboris import convert

BRT = datetime.timezone(datetime.timedelta(hours=-3))
def now(): return datetime.datetime.now(BRT).isoformat(timespec="seconds")
PKG = r"C:\Users\leona\openclaw\data\base\pacotes\placon-hermann-blumenau"
cfg = json.load(open(os.path.join(PKG,"parametrico-v2-config.json"),encoding="utf-8"))
ac = cfg["ac"]; ur = cfg["ur"]

# ---- tabela de macrogrupos VALIDADA (ordem CUSTOS_MACROGRUPO) — totais em R$ ----
MG_TOTAL = [
 ("Gerenciamento", 3434040.00), ("Mov. Terra", 188095.00), ("Infraestrutura", 1721124.00),
 ("Supraestrutura", 4617414.00), ("Alvenaria", 570416.00), ("Impermeabilização", 470100.00),
 ("Instalações", 2229040.00), ("Sist. Especiais", 1088450.00), ("Climatização", 376680.00),
 ("Rev. Int. Parede", 757070.00), ("Teto", 569195.00), ("Pisos", 1142738.00),
 ("Pintura", 893057.00), ("Esquadrias", 1910337.00), ("Louças e Metais", 117600.00),
 ("Fachada", 1227978.00), ("Complementares", 1383101.00), ("Imprevistos", 340446.00),
]
total = sum(v for _,v in MG_TOTAL); rm2 = total/ac
mg = [(n, t/ac, t/total, t) for n,t in MG_TOTAL]  # (nome, R$/m2, frac, total)

def brl(v): return f"R$ {v:,.2f}".replace(",","X").replace(".",",").replace("X",".")

FONTE = {
 "Gerenciamento":"Estimativa Cartesian (equipe enxuta ~R$31 mil/mes; projetos R$380k e grua+cremalheira R$400k a preco de mercado; 30 meses, centro confinado)",
 "Mov. Terra":"Projeto (1 subsolo, centro confinado) + Estimativa",
 "Infraestrutura":"Projeto estrutural (estacas+blocos; contencao por PAREDE DIAFRAGMA) + estimativa de fundacao",
 "Supraestrutura":"Projeto estrutural (laje nao protendida; fck 40 MPa, agressividade III) — revisao estrutural pendente",
 "Alvenaria":"Validacao BIM (100% bloco ceramico, sem drywall; area real do modelo OSPA)",
 "Impermeabilização":"Estimativa Cartesian (~0,45 m2/m2 AC, 1 subsolo)",
 "Instalações":"Projeto (eletrico Premiere: BT 400A, medicao centralizada; hidro; gas natural SCGas) + Estimativa",
 "Sist. Especiais":"Projeto (2 elevadores TKE; escada enclausurada ventilada, sem pressurizacao) + allowance gerador 12 kVA",
 "Climatização":"Estimativa Cartesian (split individual M-A)",
 "Rev. Int. Parede":"Validacao BIM (area de parede revestida ~11.534 m2)",
 "Teto":"Validacao BIM (forro gesso ~5.334 m2 + ripado de madeira ~980 m2)",
 "Pisos":"Validacao BIM (area-base de piso ~10.684 m2; acabamento M-A estimado)",
 "Pintura":"Validacao BIM (area pintada de parede ~18.040 m2)",
 "Esquadrias":"Estimativa Cartesian (aluminio + vidro M-A; quadro de esquadrias a detalhar)",
 "Louças e Metais":"Estimativa Cartesian (M-A)",
 "Fachada":"Validacao BIM (envelope real ~8.026 m2; textura/pintura acrilica, ~70 m balancim)",
 "Complementares":"Estimativa Cartesian (lazer de cobertura: piscina + salao + academia + rooftop)",
 "Imprevistos":"Padrao Cartesian 1,5%",
}

# ---- PREMISSAS-ORIGEM.md ----
P = [f"# Premissas de Origem — {cfg['nome']} (versao final)", "",
 f"**Cliente:** {cfg['cliente']}  ",
 f"**Local:** {cfg['endereco']}, {cfg['cidade']}/{cfg['estado']}  ",
 f"**Arquiteto:** {cfg['arquiteto']}  ",
 f"**Gerado:** {now()} BRT  ", "",
 "> Premissas validadas contra o **projeto legal R05** (quadro de areas OSPA), o **modelo BIM** (takeoff Solibri) "
 "e os **estudos de complementares** (Premiere). O empreendimento **nao possui memorial de acabamentos**; o padrao "
 "adotado e **Medio-Alto (M-A)**, estimado pela Cartesian. Itens marcados como *Estimativa Cartesian* devem ser validados com a Placon.", "",
 "## Dados fisicos (fonte: Projeto Legal R05 — quadro de areas, prancha 02)", "",
 f"- Area construida (AC): **{ac:,.2f} m2** (confirmada no quadro de areas R05)",
 f"- Area computavel: {cfg['area_computavel']:,.2f} m2 | privativa: {cfg['area_privativa']:,.2f} m2",
 f"- Terreno: {cfg['area_terreno']:,.2f} m2 (remanescente {cfg['area_terreno_remanescente']:,.2f})",
 f"- Unidades: **{ur} apartamentos + {cfg['lojas_comerciais']} loja** (quadro UNIDADES R05); apto medio ~{cfg['area_privativa_media_por_ur']:.0f} m2",
 f"- Pavimentos: {cfg['np']} (np) / {cfg['npt']} tipo; ~22 niveis estruturais",
 f"- Alturas (Corte AA, projeto legal R05): **fachada {cfg['altura_fachada']:.2f} m** · topo extracao de fumaca {cfg['altura_topo']:.2f} m · **total do empreendimento {cfg['altura_total_empreendimento']:.2f} m** (altura regulatoria de zoneamento/PCI ~51,76 m)",
 f"- Vagas: {cfg['vag']} ({cfg['vag_privativas']} resid + {cfg['vag_pcd_visitante']} PCD/visitante); infra p/ carro eletrico | 2 elevadores (TKE)",
 "- Laje: **nao protendida** (pranchas EST); validacao BIM aponta laje macica apoiada em pilares/nucleos — detalhar na revisao estrutural",
 "- Vedacao: **100% alvenaria de bloco ceramico** (sem drywall — confirmado em modelo BIM, PCI e demais docs)",
 "- Fundacao: **estacas + blocos**; contencao do subsolo por **parede diafragma** (projeto estrutural Lunardeli)",
 "- Gas: **gas natural** (SCGas); Pressurizacao de escada: **nao** (escada enclausurada ventilada); Gerador: **allowance** 12 kVA (bomba pluvial)", "",
 "## Premissas por macrogrupo (origem da informacao)", "",
 "| Macrogrupo | R$/m2 | % | Custo total | Origem |",
 "|---|---:|---:|---:|---|"]
for nome,b,c,d in mg:
    P.append(f"| {nome} | {b:,.0f} | {c*100:.1f}% | {brl(d)} | {FONTE.get(nome,'Estimativa Cartesian')} |")
P += [f"| **TOTAL** | **{rm2:,.0f}** | **100%** | **{brl(total)}** | |", "",
 f"**Custo por unidade ({ur} UR):** {brl(total/ur)}", "",
 "## Premissas comerciais e de prazo",
 f"- CUB-SC adotado: {brl(cfg['cub'])}/m2 (Residencial Medio, SINDUSCON-SC, mai/2026). Custo total {brl(total)} = ~7.519 CUB; obra = 1,28 CUB/m2.",
 f"- Prazo de obra: {cfg['prazo']} meses.", "",
 "## A validar / proximos passos",
 "- **Revisao estrutural** (em curso): laje (sistema/espessura), fck 40 MPa, altura de fachada; quantitativo da parede diafragma.",
 "- Padrao de acabamento M-A (sem memorial) — louças/metais, pisos, esquadrias.",
 "- Quadro de esquadrias para fechar o macrogrupo (hoje por estimativa).",
 "- VGV da viabilidade (R$ 16.000/m2 privativo) e premissa, nao pesquisa de mercado."]
open(os.path.join(PKG,"PREMISSAS-ORIGEM.md"),"w",encoding="utf-8").write("\n".join(P))

# ---- JUSTIFICATIVA-ITENS-ACIMA-DA-MEDIA.md ----
acima = sorted([m for m in mg if m[0] not in ("Imprevistos",)], key=lambda x:-x[1])[:6]
J = [f"# Justificativa de Itens Acima da Media — {cfg['nome']} (versao final)", "",
 "**Comparacao filtrada:** obras de padrao Medio-Alto, em Florianopolis e regiao, base Cartesian (126 projetos).  ",
 f"**Gerado:** {now()} BRT  ", "",
 "> Quantidades de arquitetura **validadas contra o modelo BIM** (takeoff Solibri); base fisica (AC/unidades) "
 "confirmada no projeto legal R05. Comparacao contra obras semelhantes, sem citar nomes. Foco nos macrogrupos de maior peso.", "",
 "## Macrogrupos de maior valor (R$/m2)", "",
 "| Macrogrupo | R$/m2 | % do total | Por que neste patamar |",
 "|---|---:|---:|---|"]
RAZ = {
 "Supraestrutura":"Taxa de aco de obra alta (106 kg/m3) pelos 22 niveis — o aco e o maior item (29% da Supra). 'Convencional' aqui e laje macica grossa (h 20-25 cm), robusta e concreto-intensiva: quem baixaria o custo seria a protensao, nao o contrario. fck 40 MPa (revisao estrutural).",
 "Gerenciamento":"Equipe tecnica ENXUTA (~R$31 mil/mes: 1 eng, 1 mestre, 1 encarregado). O R$/m2 sobe por GEOMETRIA, nao por gordura: custos fixos (projetos, taxas, grua) diluidos num footprint pequeno + 30 meses de torre. Projetos (R$380k) e equipamentos (R$400k) ja a preco de mercado.",
 "Instalações":"Eletrica (Premiere: BT 400A, medicao centralizada) + hidro completos; gas natural; 2 elevadores e prumadas de torre alta.",
 "Esquadrias":"Padrao M-A: aluminio + vidro de qualidade, sacadas/Garden, grandes vaos (patamar mercado-premium).",
 "Infraestrutura":"Contencao do subsolo por PAREDE DIAFRAGMA (projeto estrutural) em terreno de centro confinado entre vizinhos — mais robusta e cara que cortina convencional. Estimativa a ajustar com o quantitativo estrutural.",
 "Complementares":"Lazer completo de cobertura: piscina + salao + academia + rooftop.",
 "Fachada":"Area ajustada pela validacao BIM (abaixo da estimativa inicial); permanece no topo do premium pela altura (~70 m, balancim) e padrao M-A.",
 "Pisos":"Area-base validada pelo BIM; porcelanato M-A em areas privativas + comuns.",
}
for nome,b,c,d in acima:
    J.append(f"| {nome} | {b:,.0f} | {c*100:.1f}% | {RAZ.get(nome,'Padrao M-A da tipologia.')} |")
J += ["", "## Efeito da validacao BIM + projeto legal (vs estimativa inicial)",
 "- **Alvenaria −R$ 497 mil:** modelo e 100% bloco ceramico (sem drywall que a estimativa inicial assumia) — item entrou abaixo do mercado.",
 "- **Fachada −R$ 166 mil:** envelope real do modelo menor que a estimativa por indice.",
 "- **Forro +R$ 176 mil:** apareceu forro ripado de madeira (~980 m2) nao previsto.",
 "- **Infraestrutura +R$ 493 mil:** contencao generica trocada por parede diafragma (projeto estrutural).",
 "- **Gerenciamento −R$ 200 mil:** projetos (R$380k) e equipamentos/grua (R$400k) a preco de mercado; equipe tecnica mantida enxuta.",
 "- **AC e unidades confirmadas no projeto legal R05** (5.877,96 m2; 35 aptos + 1 loja) — base inalterada.",
 f"- **Total final:** {brl(total)} ({rm2:,.0f}/m2; {brl(total/ur)}/UR) — vs R$ 23,28 mi da estimativa inicial.", "",
 "## Estrutura vs obras reais (base Cartesian)",
 "A Supraestrutura escala com a altura — confirmado em executivos reais. Base **material** (concreto+aco+forma, R$/m2): Obra 6 pav R$345 / Obra 4 pav R$433 / Obra 12 pav R$514 / **Hermann 22 niveis R$530**. Base **material + MO**: Obra 9 pav R$670 / **Hermann R$786** / Obra 18 pav (protendida) R$801. O Hermann e o mais alto da lista, logo no topo natural da curva — nao e sobrepreco. (Parte das obras lanca a mao de obra numa linha 'empreitada global'; por isso a base material e comparada a parte — a MO da estrutura do Hermann e R$256/m2.)",
 "",
 "## Notas de metodo",
 "- Revestimento de parede dividido em argamassado + ceramico (padrao M-A); area total casou com o BIM (~1,5%).",
 "- Itens de instalacoes/estrutura permanecem por indice/projeto; nao validaveis pelo modelo arquitetonico.",
 "- Valores sao referencia de viabilidade (ordem de grandeza, margem +-25%), nao orcamento executivo."]
open(os.path.join(PKG,"JUSTIFICATIVA-ITENS-ACIMA-DA-MEDIA.md"),"w",encoding="utf-8").write("\n".join(J))

# converter
d1 = convert(os.path.join(PKG,"PREMISSAS-ORIGEM.md"), os.path.join(PKG,"placon-hermann-blumenau-PREMISSAS-ORIGEM-final.docx"))
d2 = convert(os.path.join(PKG,"JUSTIFICATIVA-ITENS-ACIMA-DA-MEDIA.md"), os.path.join(PKG,"placon-hermann-blumenau-JUSTIFICATIVA-ITENS-ACIMA-MEDIA-final.docx"))
print("DOCS_OK  premissas:", os.path.exists(d1), "| justificativa:", os.path.exists(d2))
print(f"total={brl(total)} rm2={rm2:.0f} custo/UR={brl(total/ur)}")
