#!/usr/bin/env python3.11
"""
Slack IFC Processor — Baixa arquivos IFC do Slack e extrai dados para orçamento paramétrico.

Uso:
  python3.11 scripts/slack_ifc_processor.py --bot cartesiano
  python3.11 scripts/slack_ifc_processor.py --bot cartesiano --projeto arminio-tavares
  python3.11 scripts/slack_ifc_processor.py --bot cartesiano --listar
  python3.11 scripts/slack_ifc_processor.py --bot cartesiano --thread 1773062813.776419

Fluxo:
  1. Busca mensagens recentes no canal #custos-ia-parametrico
  2. Encontra arquivos .ifc anexados
  3. Baixa o arquivo para projetos/<nome>/
  4. Extrai dados com ifcopenshell (pavimentos, áreas, elementos)
  5. Imprime resumo estruturado
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "slack_config.json"
PROJETOS_DIR = SCRIPT_DIR.parent / "projetos"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def slack_api(method, token, params=None):
    """Chamada simples à Slack Web API (sem dependência de slack_sdk)."""
    url = f"https://slack.com/api/{method}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
    if not data.get("ok"):
        raise RuntimeError(f"Slack API error ({method}): {data.get('error', data)}")
    return data


def listar_ifcs(token, channel, limit=50, thread_ts=None):
    """Lista arquivos IFC recentes no canal ou em uma thread específica."""
    if thread_ts:
        try:
            data = slack_api("conversations.replies", token, {
                "channel": channel,
                "ts": thread_ts,
                "limit": str(limit),
            })
        except RuntimeError as e:
            if "thread_not_found" in str(e):
                print(f"Thread {thread_ts} não encontrada. Buscando no canal...")
                data = slack_api("conversations.history", token, {"channel": channel, "limit": str(limit)})
            else:
                raise
    else:
        data = slack_api("conversations.history", token, {"channel": channel, "limit": str(limit)})
    ifcs = []
    for msg in data.get("messages", []):
        for f in msg.get("files", []):
            name = f.get("name", "")
            if name.lower().endswith(".ifc"):
                ifcs.append({
                    "id": f["id"],
                    "name": name,
                    "size_mb": round(f.get("size", 0) / 1024 / 1024, 1),
                    "url_private_download": f.get("url_private_download", ""),
                    "timestamp": msg.get("ts", ""),
                    "user": msg.get("user", ""),
                })
    return ifcs


def download_ifc(file_info, token, projeto_nome=None):
    """Baixa o IFC do Slack para projetos/<nome>/."""
    nome_arquivo = file_info["name"]
    if not projeto_nome:
        # Derivar nome do projeto a partir do nome do arquivo
        projeto_nome = Path(nome_arquivo).stem.lower()
        # Limpar caracteres especiais
        projeto_nome = projeto_nome.replace(" ", "-").replace("_", "-")
        # Remover sufixos comuns como (1), -r06, etc
        for suffix in ["-(1)", "-(2)", "-(3)"]:
            projeto_nome = projeto_nome.replace(suffix, "")

    dest_dir = PROJETOS_DIR / projeto_nome
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / nome_arquivo

    if dest_path.exists():
        print(f"Arquivo já existe: {dest_path}")
        return dest_path

    url = file_info["url_private_download"]
    if not url:
        raise RuntimeError(f"Arquivo {nome_arquivo} não tem URL de download")

    print(f"Baixando {nome_arquivo} ({file_info['size_mb']} MB)...")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        with open(dest_path, "wb") as out:
            while True:
                chunk = resp.read(8192)
                if not chunk:
                    break
                out.write(chunk)

    size_mb = dest_path.stat().st_size / 1024 / 1024
    print(f"Salvo: {dest_path} ({size_mb:.1f} MB)")
    return dest_path


def extrair_dados_ifc(caminho_ifc):
    """Extrai dados relevantes do IFC usando ifcopenshell."""
    try:
        import ifcopenshell
    except ImportError:
        print("ERRO: ifcopenshell não instalado. Instale com: pip3.11 install ifcopenshell")
        sys.exit(1)

    print(f"\nAnalisando IFC: {caminho_ifc}")
    ifc = ifcopenshell.open(str(caminho_ifc))

    # Projeto
    project = ifc.by_type('IfcProject')[0]
    schema = ifc.schema

    # Pavimentos
    pavimentos = ifc.by_type('IfcBuildingStorey')
    dados_pavimentos = []
    for pav in sorted(pavimentos, key=lambda p: p.Elevation or 0):
        nome = pav.Name or "Sem nome"
        elevacao = pav.Elevation or 0
        dados_pavimentos.append({'nome': nome, 'elevacao': elevacao / 100.0})

    # Lajes e áreas
    lajes = ifc.by_type('IfcSlab')
    areas_lajes_por_pav = defaultdict(list)

    for laje in lajes:
        pavimento_nome = "Sem pavimento"
        for rel in laje.ContainedInStructure:
            if rel.is_a('IfcRelContainedInSpatialStructure'):
                relating = rel.RelatingStructure
                if relating.is_a('IfcBuildingStorey'):
                    pavimento_nome = relating.Name or "Sem nome"
                    break

        area = 0.0
        for rel in laje.IsDefinedBy:
            if rel.is_a('IfcRelDefinesByProperties'):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a('IfcElementQuantity'):
                    for quantity in prop_def.Quantities:
                        if quantity.is_a('IfcQuantityArea'):
                            area = quantity.AreaValue
                            break
                elif prop_def.is_a('IfcPropertySet'):
                    for prop in prop_def.HasProperties:
                        if prop.Name in ['Area', 'NetArea', 'GrossArea']:
                            if hasattr(prop, 'NominalValue'):
                                area = float(prop.NominalValue.wrappedValue)
                                break
            if area > 0:
                break

        if area > 0:
            areas_lajes_por_pav[pavimento_nome].append(area)

    # Consolidar áreas
    areas_por_pavimento = {}
    area_total_lajes = 0.0
    for pav, areas in sorted(areas_lajes_por_pav.items()):
        area_pav = sum(areas)
        areas_por_pavimento[pav] = round(area_pav, 2)
        area_total_lajes += area_pav

    # Elementos
    paredes = ifc.by_type('IfcWall')
    portas = ifc.by_type('IfcDoor')
    janelas = ifc.by_type('IfcWindow')
    colunas = ifc.by_type('IfcColumn')
    vigas = ifc.by_type('IfcBeam')

    # Pavimentos tipo
    pavimentos_tipo = [p for p in dados_pavimentos
                       if any(x in p['nome'] for x in ['PAVIMENTO', 'Pavimento', 'pavimento', 'PAV', 'Pav'])
                       and not any(x in p['nome'].upper() for x in ['SUBSOLO', 'BARRILETE', 'COBERTURA', 'CASA', 'RESERV', 'TERREO', 'TÉRREO'])]

    # Pé-direito estimado (entre pavimentos consecutivos)
    pe_direitos = []
    elevacoes = sorted(set(p['elevacao'] for p in dados_pavimentos))
    for i in range(1, len(elevacoes)):
        diff = elevacoes[i] - elevacoes[i-1]
        if 2.0 < diff < 6.0:  # Faixa razoável
            pe_direitos.append(round(diff, 2))

    pe_direito_medio = round(sum(pe_direitos) / len(pe_direitos), 2) if pe_direitos else None

    resultado = {
        'nome_projeto': project.Name,
        'schema': schema,
        'num_entidades': len(list(ifc)),
        'num_pavimentos_total': len(pavimentos),
        'num_pavimentos_tipo': len(pavimentos_tipo),
        'pavimentos': dados_pavimentos,
        'area_total_lajes': round(area_total_lajes, 2),
        'areas_por_pavimento': areas_por_pavimento,
        'pe_direito_medio': pe_direito_medio,
        'elementos': {
            'paredes': len(paredes),
            'portas': len(portas),
            'janelas': len(janelas),
            'colunas': len(colunas),
            'vigas': len(vigas),
            'lajes': len(lajes),
        }
    }

    return resultado


def imprimir_resumo(dados):
    """Imprime resumo formatado para o bot usar."""
    print(f"\n{'='*60}")
    print(f"DADOS EXTRAÍDOS DO IFC")
    print(f"{'='*60}")
    print(f"Projeto: {dados['nome_projeto']}")
    print(f"Schema: {dados['schema']}")
    print(f"Entidades: {dados['num_entidades']:,}")
    print(f"")
    print(f"PAVIMENTOS: {dados['num_pavimentos_total']} total, {dados['num_pavimentos_tipo']} tipo")
    if dados['pe_direito_medio']:
        print(f"Pé-direito médio estimado: {dados['pe_direito_medio']}m")
    print(f"")
    print(f"ÁREAS (baseado em lajes):")
    for pav, area in dados['areas_por_pavimento'].items():
        print(f"  {pav}: {area:.2f} m²")
    print(f"  TOTAL: {dados['area_total_lajes']:.2f} m²")
    print(f"")
    print(f"ELEMENTOS:")
    for elem, qtd in dados['elementos'].items():
        print(f"  {elem}: {qtd}")
    print(f"")
    print(f"LISTA DE PAVIMENTOS:")
    for pav in dados['pavimentos']:
        print(f"  {pav['nome']} (elevação: {pav['elevacao']:.2f}m)")
    print(f"{'='*60}")

    # JSON para processamento programático
    print(f"\n--- JSON ---")
    print(json.dumps(dados, ensure_ascii=False, indent=2, default=str))


def main():
    parser = argparse.ArgumentParser(description="Baixa e processa arquivos IFC do Slack")
    parser.add_argument("--bot", required=True, choices=["cartesiano", "parametrico-openai", "parametrico-gemini"],
                        help="Qual bot está executando (determina o token)")
    parser.add_argument("--channel", help="Channel ID do Slack (default: config)")
    parser.add_argument("--projeto", help="Nome do projeto (pasta de destino)")
    parser.add_argument("--listar", action="store_true", help="Apenas listar IFCs disponíveis no canal")
    parser.add_argument("--arquivo", help="Nome específico do arquivo IFC para baixar")
    parser.add_argument("--thread", help="Thread timestamp (ts) para buscar IFC dentro de uma thread")
    parser.add_argument("--local", help="Caminho local de um IFC já baixado (pula download)")
    args = parser.parse_args()

    config = load_config()
    bot_config = config["bots"].get(args.bot)
    if not bot_config:
        print(f"ERRO: Bot '{args.bot}' não encontrado na config")
        sys.exit(1)

    token = bot_config["token"]
    channel = args.channel or config["channel"]

    # Modo: processar arquivo local
    if args.local:
        local_path = Path(args.local)
        if not local_path.exists():
            print(f"ERRO: Arquivo não encontrado: {args.local}")
            sys.exit(1)
        dados = extrair_dados_ifc(local_path)
        imprimir_resumo(dados)
        return

    thread_ts = args.thread if hasattr(args, 'thread') else None

    # Modo: listar IFCs
    if args.listar:
        ifcs = listar_ifcs(token, channel, thread_ts=thread_ts)
        if not ifcs:
            where = f"na thread {thread_ts}" if thread_ts else "nas últimas 50 mensagens do canal"
            print(f"Nenhum arquivo IFC encontrado {where}.")
            if thread_ts:
                print("Tentando buscar no canal principal...")
                ifcs = listar_ifcs(token, channel)
                if ifcs:
                    print(f"Arquivos IFC encontrados no canal ({len(ifcs)}):")
                    for i, ifc in enumerate(ifcs, 1):
                        print(f"  {i}. {ifc['name']} ({ifc['size_mb']} MB) — ts: {ifc['timestamp']}")
            return
        where = f"na thread" if thread_ts else ""
        print(f"Arquivos IFC encontrados {where} ({len(ifcs)}):")
        for i, ifc in enumerate(ifcs, 1):
            print(f"  {i}. {ifc['name']} ({ifc['size_mb']} MB) — ts: {ifc['timestamp']}")
        return

    # Modo: baixar e processar
    ifcs = listar_ifcs(token, channel, thread_ts=thread_ts)
    if not ifcs and thread_ts:
        # Fallback: se não achou na thread, tenta no canal principal
        print(f"Nenhum IFC na thread {thread_ts}. Buscando no canal...")
        ifcs = listar_ifcs(token, channel)
    if not ifcs:
        print("Nenhum arquivo IFC encontrado nas últimas 50 mensagens do canal.")
        print("Dica: o usuário deve enviar o arquivo .ifc no canal antes de pedir processamento.")
        sys.exit(1)

    # Selecionar arquivo
    target = None
    if args.arquivo:
        for ifc in ifcs:
            if args.arquivo.lower() in ifc["name"].lower():
                target = ifc
                break
        if not target:
            print(f"ERRO: Arquivo '{args.arquivo}' não encontrado. Disponíveis:")
            for ifc in ifcs:
                print(f"  - {ifc['name']}")
            sys.exit(1)
    else:
        target = ifcs[0]  # Mais recente
        print(f"Usando arquivo mais recente: {target['name']}")

    # Download
    dest_path = download_ifc(target, token, projeto_nome=args.projeto)

    # Extrair dados
    dados = extrair_dados_ifc(dest_path)
    imprimir_resumo(dados)


if __name__ == "__main__":
    main()
