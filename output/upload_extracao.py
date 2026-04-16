#!/usr/bin/env python3.11
import subprocess
import sys
from pathlib import Path

BASE = str(Path.home() / "orcamentos")

result = subprocess.run([
    'python3.11', 'scripts/slack_uploader.py',
    '--bot', 'cartesiano',
    '--file', 'output/CTN-Senna-Extracao-IFC-09-11.xlsx',
    '--thread', '1776262563.000759',
    '--channel', 'C0AL0KV1R1N',
    '--comment', 'Extração detalhada dos IFCs 09 e 11 - Quantitativos por elemento'
], cwd=BASE)
sys.exit(result.returncode)
