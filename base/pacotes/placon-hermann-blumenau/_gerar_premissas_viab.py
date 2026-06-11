# -*- coding: utf-8 -*-
"""Gera premissas-viabilidade.json do Hermann adaptado do Arminio (32 meses, VGV 16k, TMA 14%)."""
import json, math, os
PKG = r"C:\Users\leona\openclaw\data\base\pacotes\placon-hermann-blumenau"
cfg = json.load(open(os.path.join(PKG,"parametrico-v2-config.json"),encoding="utf-8"))
N = cfg["prazo"]  # 32 meses

# S-curve mensal somando 1.0 (logistica derivada, normalizada)
k=0.28; t50=N/2
cum=[1/(1+math.exp(-k*(t-t50))) for t in range(1,N+2)]
vals=[cum[i+1]-cum[i] for i in range(N)]
s=sum(vals); vals=[round(v/s,5) for v in vals]
# ajustar arredondamento p/ somar exatamente 1.0
diff=round(1.0-sum(vals),5); vals[len(vals)//2]=round(vals[len(vals)//2]+diff,5)

def win(a,b):  # escala janela do arminio (24mo) p/ N meses
    f=N/24.0
    return [max(1,round(a*f)), min(N,round(b*f))]

prem = {
 "_gerado_em":"2026-05-29",
 "_descricao":f"Premissas viabilidade Placon Hermann Blumenau - adaptado do Arminio. Obra {N} meses, {cfg['ur']} UR, AC {cfg['ac']} m2 (privativa {cfg['area_privativa']} m2). Custo base lido em runtime do parametrico (Grand Total ~R$ 24,45 mi).",
 "projeto":{
   "nome":cfg["nome"],"cidade":cfg["cidade"],"bairro":"Centro","estado":cfg["estado"],
   "cliente":cfg["cliente"],
   "area_construida_m2":cfg["ac"],"area_privativa_m2":cfg["area_privativa"],
   "n_unidades":cfg["ur"],"prazo_obra_meses":N,"prazo_pre_lancamento_meses":3,"prazo_pos_obra_meses":12,
   "pct_area_privativa":round(cfg["area_privativa"]/cfg["ac"],4),
   "_pct_area_privativa_fonte":f"{cfg['area_privativa']}/{cfg['ac']} (PL R05; inclui vagas na privativa pela definicao PMF).",
   "permuta_pct_unidades":0.0,
   "_permuta_nota":"Sem permuta fisica assumida - ajustar se contrato final tiver permuta."
 },
 "custo":{"_fonte":"parametrico-placon-hermann-blumenau.xlsx CUSTOS_MACROGRUPO!D22 (runtime) ~R$ 24.445.536; RSM2 ~R$ 4.159.","contingencia_pct":0.05},
 "receita":{
   "vgv_m2_base":cfg["viabilidade"]["vgv_m2_privativo"],
   "_vgv_m2_fonte":"PREMISSA Leo R$ 16.000/m2 (centro Floripa M-A, apto ~82 m2). VALIDAR com Placon/pesquisa. Sensibilidade -15%/+10%.",
   "entrada_pct":0.20,"obra_pct":0.40,"repasse_pct":0.40,"inadimplencia_pct":0.03
 },
 "financeiras":{
   "cub_aa":0.07,"_cub_fonte":"CUB/SC indexador padrao SC ~7% a.a.",
   "tma_aa":cfg["viabilidade"]["tma_aa"],"_tma_fonte":"custo de capital incorporadora media porte SC 2026 (~14%)."
 },
 "comercial":{
   "corretagem_pct":0.05,"marketing_pct":0.03,"marketing_front_pct":0.0,
   "ret_pct":0.04,"_ret_fonte":"RET Patrimonio de Afetacao 4%.","adm_incorporadora_pct":0.02
 },
 "curva_vendas":{"_modelo":"logistica cumulativa","t_inicio":-2,"t50":round(N/2),"k":0.16,
   "_t50_nota":f"t50={round(N/2)} (~metade da obra de {N} meses)."},
 "curva_obra_por_macrogrupo":{
   "Gerenciamento":[1,N],"Mov. Terra":win(1,3),"Infraestrutura":win(1,7),"Supraestrutura":win(3,15),
   "Alvenaria":win(7,17),"Impermeabilização":win(4,20),"Instalações":win(8,23),"Sist. Especiais":win(15,23),
   "Climatização":win(16,23),"Rev. Int. Parede":win(12,21),"Teto":win(15,23),"Pisos":win(16,23),
   "Pintura":win(17,24),"Esquadrias":win(15,23),"Louças e Metais":win(17,23),"Fachada":win(12,21),
   "Complementares":win(19,24),"Imprevistos":[1,N]
 },
 "curva_mensal_obra_pct":{"_descricao":f"Curva S {N} meses, soma 1.0.","_soma":"100%","valores":vals},
 "monte_carlo":{
   "n_iter":10000,"seed":42,
   "_base_nota":"Base MC = Grand Total parametrico V2 (~R$ 24,45 mi). Range estreito (V2 calibrado ~+/-10%).",
   "vgv_m2_tri":[13600,16000,19000],
   "_vgv_tri_nota":"Pessimista R$13,6k (-15%), base R$16k, otimista R$19k.",
   "custo_obra_fator_tri":[0.95,1.00,1.12],
   "t50_vendas_tri":[round(N*0.3),round(N/2),round(N*0.85)],
   "cub_aa_tri":[0.04,0.07,0.11],"corr_vgv_t50":-0.4
 },
 "tornado":{"variacao_pct":0.20,"variaveis":["vgv_m2_base","custo_obra_fator","t50_vendas","entrada_pct","corretagem_pct","ret_pct","cub_aa","tma_aa"]},
 "cenarios":{"pessimista":{"vgv_fator":0.85,"custo_fator":1.10,"t50_delta":6},
   "base":{"vgv_fator":1.00,"custo_fator":1.00,"t50_delta":0},
   "otimista":{"vgv_fator":1.10,"custo_fator":0.95,"t50_delta":-3}}
}
json.dump(prem,open(os.path.join(PKG,"premissas-viabilidade.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("PREMISSAS_VIAB_OK soma_curva=%.4f n_meses=%d pct_priv=%.4f"%(sum(vals),N,prem["projeto"]["pct_area_privativa"]))
