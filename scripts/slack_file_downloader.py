#!/usr/bin/env python3.11
"""
Slack File Downloader — Baixa qualquer arquivo do Slack (canal ou thread).

Uso:
  python3.11 scripts/slack_file_downloader.py --bot cartesiano --listar
  python3.11 scripts/slack_file_downloader.py --bot cartesiano --listar --thread 1773079685.803099
  python3.11 scripts/slack_file_downloader.py --bot cartesiano --listar --tipo xlsx
  python3.11 scripts/slack_file_downloader.py --bot cartesiano --baixar --thread 1773079685.803099
  python3.11 scripts/slack_file_downloader.py --bot cartesiano --baixar --thread 1773079685.803099 --destino projetos/gsl/

Fluxo:
  1. Busca mensagens recentes no canal ou thread
  2. Lista arquivos encontrados (com filtro opcional por extensão)
  3. Baixa o arquivo mais recente (ou específico por nome) para destino
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "slack_config.json"
PROJETOS_DIR = SCRIPT_DIR.parent / "projetos"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def slack_api(method, token, params=None):
    """Chamada simples à Slack Web API."""
    url = f"https://slack.com/api/{method}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
    if not data.get("ok"):
        raise RuntimeError(f"Slack API error ({method}): {data.get('error', data)}")
    return data


def listar_arquivos(token, channel, limit=50, thread_ts=None, tipo=None):
    """Lista arquivos recentes no canal ou thread, com filtro opcional por extensão."""
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

    arquivos = []
    for msg in data.get("messages", []):
        for f in msg.get("files", []):
            name = f.get("name", "")
            ext = Path(name).suffix.lower().lstrip(".")
            if tipo and ext != tipo.lower().lstrip("."):
                continue
            arquivos.append({
                "id": f["id"],
                "name": name,
                "ext": ext,
                "size_mb": round(f.get("size", 0) / 1024 / 1024, 2),
                "url_private_download": f.get("url_private_download", ""),
                "mimetype": f.get("mimetype", ""),
                "timestamp": msg.get("ts", ""),
                "user": msg.get("user", ""),
            })
    return arquivos


def download_arquivo(file_info, token, destino=None):
    """Baixa arquivo do Slack para diretório de destino."""
    nome_arquivo = file_info["name"]

    if destino:
        dest_dir = Path(destino)
    else:
        dest_dir = PROJETOS_DIR / "downloads"
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
    print(f"Salvo: {dest_path} ({size_mb:.2f} MB)")
    return dest_path


def main():
    parser = argparse.ArgumentParser(description="Baixa arquivos do Slack")
    parser.add_argument("--bot", required=True, choices=["cartesiano", "parametrico-openai", "parametrico-gemini"],
                        help="Qual bot está executando (determina o token)")
    parser.add_argument("--channel", help="Channel ID do Slack (default: config)")
    parser.add_argument("--thread", help="Thread timestamp (ts) para buscar arquivos dentro de uma thread")
    parser.add_argument("--listar", action="store_true", help="Apenas listar arquivos disponíveis")
    parser.add_argument("--baixar", action="store_true", help="Baixar o arquivo mais recente")
    parser.add_argument("--tipo", help="Filtrar por extensão (xlsx, pdf, ifc, dwg, etc.)")
    parser.add_argument("--arquivo", help="Nome específico do arquivo para baixar")
    parser.add_argument("--destino", help="Diretório de destino para o download")
    args = parser.parse_args()

    if not args.listar and not args.baixar:
        parser.error("Use --listar ou --baixar")

    config = load_config()
    bot_config = config["bots"].get(args.bot)
    if not bot_config:
        print(f"ERRO: Bot '{args.bot}' não encontrado na config")
        sys.exit(1)

    token = bot_config["token"]
    channel = args.channel or config["channel"]

    # Listar arquivos
    arquivos = listar_arquivos(token, channel, thread_ts=args.thread, tipo=args.tipo)

    if not arquivos and args.thread:
        print(f"Nenhum arquivo na thread {args.thread}. Buscando no canal...")
        arquivos = listar_arquivos(token, channel, tipo=args.tipo)

    if not arquivos:
        tipo_msg = f" do tipo .{args.tipo}" if args.tipo else ""
        where = f"na thread {args.thread}" if args.thread else "nas últimas 50 mensagens do canal"
        print(f"Nenhum arquivo{tipo_msg} encontrado {where}.")
        sys.exit(1)

    if args.listar:
        where = f"na thread" if args.thread else "no canal"
        print(f"Arquivos encontrados {where} ({len(arquivos)}):")
        for i, arq in enumerate(arquivos, 1):
            print(f"  {i}. {arq['name']} ({arq['size_mb']} MB, .{arq['ext']}) — ts: {arq['timestamp']}")
        return

    # Baixar
    target = None
    if args.arquivo:
        for arq in arquivos:
            if args.arquivo.lower() in arq["name"].lower():
                target = arq
                break
        if not target:
            print(f"ERRO: Arquivo '{args.arquivo}' não encontrado. Disponíveis:")
            for arq in arquivos:
                print(f"  - {arq['name']}")
            sys.exit(1)
    else:
        target = arquivos[0]
        print(f"Usando arquivo mais recente: {target['name']}")

    dest_path = download_arquivo(target, token, destino=args.destino)
    print(f"\n--- Arquivo baixado ---")
    print(f"Nome: {target['name']}")
    print(f"Caminho: {dest_path}")
    print(f"Tipo: .{target['ext']} ({target['mimetype']})")
    print(f"Tamanho: {target['size_mb']} MB")


if __name__ == "__main__":
    main()
