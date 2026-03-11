#!/usr/bin/env python3.11
"""
Slack File Uploader — Faz upload de arquivos para o Slack.

Uso:
  python3.11 scripts/slack_uploader.py --bot cartesiano --file output/projeto.xlsx
  python3.11 scripts/slack_uploader.py --bot cartesiano --file output/projeto.xlsx --comment "Orçamento gerado"
  python3.11 scripts/slack_uploader.py --bot cartesiano --file output/projeto.xlsx --thread 1773063410.804809

Fluxo:
  1. Lê config do bot (token + channel) de slack_config.json
  2. Faz upload via files.getUploadURLExternal + files.completeUploadExternal (Slack v2 API)
  3. Compartilha no canal/thread especificado
"""
import argparse
import json
import mimetypes
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "slack_config.json"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def slack_api_post(method, token, data=None):
    """POST JSON à Slack Web API."""
    url = f"https://slack.com/api/{method}"
    body = json.dumps(data or {}).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
    if not result.get("ok"):
        error = result.get("error", "unknown")
        detail = result.get("response_metadata", {}).get("messages", [])
        raise RuntimeError(f"Slack API error ({method}): {error} {detail}")
    return result


def upload_file(token, channel, filepath, thread_ts=None, comment=None, title=None):
    """Upload de arquivo usando Slack v2 upload API (files.getUploadURLExternal + completeUploadExternal)."""
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    file_size = filepath.stat().st_size
    filename = filepath.name
    if title is None:
        title = filename

    # Passo 1: Obter URL de upload
    get_url_params = {
        "filename": filename,
        "length": file_size,
    }
    url = "https://slack.com/api/files.getUploadURLExternal"
    query = "&".join(f"{k}={v}" for k, v in get_url_params.items())
    req = urllib.request.Request(
        f"{url}?{query}",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
    if not result.get("ok"):
        error = result.get("error", "unknown")
        if error == "missing_scope":
            print("ERRO: O bot não tem o scope 'files:write'.", file=sys.stderr)
            print("Adicione 'files:write' em api.slack.com/apps → OAuth & Permissions → Bot Token Scopes", file=sys.stderr)
            sys.exit(1)
        raise RuntimeError(f"files.getUploadURLExternal: {error}")

    upload_url = result["upload_url"]
    file_id = result["file_id"]

    # Passo 2: Upload do arquivo para a URL fornecida
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    with open(filepath, "rb") as f:
        file_data = f.read()

    req = urllib.request.Request(
        upload_url,
        data=file_data,
        headers={"Content-Type": content_type},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        resp.read()  # Consumir resposta

    # Passo 3: Completar upload e compartilhar no canal
    complete_data = {
        "files": [{"id": file_id, "title": title}],
        "channel_id": channel,
    }
    if comment:
        complete_data["initial_comment"] = comment
    if thread_ts:
        complete_data["thread_ts"] = thread_ts

    slack_api_post("files.completeUploadExternal", token, complete_data)

    print(f"Upload concluído: {filename}")
    print(f"  Canal: {channel}")
    if thread_ts:
        print(f"  Thread: {thread_ts}")
    if comment:
        print(f"  Comentário: {comment}")
    return file_id


def main():
    parser = argparse.ArgumentParser(description="Upload de arquivo para o Slack")
    parser.add_argument("--bot", required=True, choices=["cartesiano", "parametrico-openai", "parametrico-gemini"],
                        help="Nome do bot (define qual token usar)")
    parser.add_argument("--file", required=True, help="Caminho do arquivo para upload")
    parser.add_argument("--channel", help="Channel ID (default: slack_config.json)")
    parser.add_argument("--thread", help="Thread timestamp para enviar na thread")
    parser.add_argument("--comment", help="Mensagem acompanhando o arquivo")
    parser.add_argument("--title", help="Título do arquivo no Slack")
    args = parser.parse_args()

    config = load_config()

    bot_config = config["bots"].get(args.bot)
    if not bot_config:
        print(f"ERRO: Bot '{args.bot}' não encontrado em slack_config.json", file=sys.stderr)
        sys.exit(1)

    token = bot_config["token"]
    channel = args.channel or config.get("channel")
    if not channel:
        print("ERRO: Channel não especificado (nem via --channel nem em slack_config.json)", file=sys.stderr)
        sys.exit(1)

    upload_file(
        token=token,
        channel=channel,
        filepath=args.file,
        thread_ts=args.thread,
        comment=args.comment,
        title=args.title,
    )


if __name__ == "__main__":
    main()
