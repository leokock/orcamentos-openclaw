#!/bin/bash
cd "$(dirname "$0")/.."
python3.11 scripts/gerar_template_dinamico_v2.py \
  --nome "San Felice" \
  --ac 7435 \
  --ur 54 \
  --np 14 \
  --npt 8 \
  --elev 2 \
  --vag 70 \
  --cidade "Navegantes" \
  --estado "SC" \
  -o output/san-fellice-parametrico-v2.xlsx
