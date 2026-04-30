# Template Generator — Orçamento Executivo

Gera planilha Excel com 42 abas no formato padrão Cartesian.

## Estrutura

```
template-generator/
├── modules/
│   ├── grupo_a_overview.py      # PROJETOS, Obra, EAP Análise
│   ├── grupo_b_gerenciamento.py # EPCs → Ger_Executivo
│   ├── grupo_c_referencia.py    # CPU, Insumos
│   ├── grupo_d_quantitativos.py # 11 abas Visus/BIM
│   ├── grupo_e_estrutural.py    # Estacas → Supraestrutura
│   ├── grupo_f_instalacoes.py   # 7 abas instalações
│   └── grupo_g_acabamentos.py   # Esquadrias → Mobiliário
├── generate_template.py          # Script principal
└── README.md
```

## Uso

```bash
python3 generate_template.py --projeto "Nome" --empresa "Empresa" --output saida.xlsx
```

## Referência

- Planilha modelo: `projetos/estoril/CTN_FSN_EST-Orcamento-Executivo-REAL.xlsx`
- Estrutura extraída: `projetos/estoril/template-structure.md`
- EAP real: `projetos/estoril/eap-real-completa.md`
