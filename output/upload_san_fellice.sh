#!/bin/bash
cd "$(dirname "$0")/.."
python3.11 scripts/slack_uploader.py --bot cartesiano --file output/san-fellice-parametrico-v2.xlsx --thread 1775558957.950219 --channel C0AL0KV1R1N --comment "Orçamento paramétrico San Felice — Navegantes/SC"
