const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageNumber, PageBreak, LevelFormat
} = require("docx");

// === CONSTANTS ===
const AC = 36088.85;
const CUB = 3019.26;
const TOTAL = 169522402.07;
const CUB_RATIO = (TOTAL / AC / CUB).toFixed(2);

const DARK = "2C3E50";
const ACCENT = "2980B9";
const GREEN_BG = "E8F6EF";
const YELLOW_BG = "FFF8E1";
const RED_BG = "FDEDEC";
const GRAY_BG = "F5F5F5";
const WHITE = "FFFFFF";

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

function brl(v) {
  if (v >= 1e6) return "R$ " + (v/1e6).toFixed(3).replace(".", ",") + " mi";
  if (v >= 1e3) return "R$ " + Math.round(v).toLocaleString("pt-BR");
  return "R$ " + v.toFixed(2).replace(".", ",");
}

function brlFull(v) {
  return "R$ " + Math.round(v).toLocaleString("pt-BR");
}

function pct(v) { return (v * 100).toFixed(1) + "%"; }

function headerCell(text, width) {
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA },
    shading: { fill: DARK, type: ShadingType.CLEAR },
    margins: cellMargins,
    verticalAlign: "center",
    children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text, bold: true, color: WHITE, font: "Arial", size: 18 })
    ]})]
  });
}

function dataCell(text, width, opts = {}) {
  const { bold, align, shade, fontSize } = { bold: false, align: AlignmentType.LEFT, shade: null, fontSize: 18, ...opts };
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA },
    shading: shade ? { fill: shade, type: ShadingType.CLEAR } : undefined,
    margins: cellMargins,
    children: [new Paragraph({ alignment: align, children: [
      new TextRun({ text: String(text), bold, font: "Arial", size: fontSize })
    ]})]
  });
}

// === EAP DATA with full traceability ===
const eap = [
  {
    etapa: "GERENCIAMENTO TECNICO E ADMINISTRATIVO",
    valor: 17841244.77,
    rsm2: 494.37,
    origem: "Parametrico",
    fonte_qtd: "Mediana de 7 projetos similares (base Cartesian, 75 executivos calibrados)",
    fonte_pu: "Mediana R$/m2 da base parametrica, atualizada para CUB SC fev/2026",
    ref_projetos: "Base 75 exec: Elizabeth II, Chateau Versailles, Meraki, Porto Ruby, Cielo, Virginia, Barra4",
    aba: "Ger_Tec e Adm",
    maturidade: "amarelo",
    obs: "Inclui projetos, taxas, equipe ADM, EPCs, ensaios. Estrutura replicada do Elizabeth II (Gessele) com ajuste de area."
  },
  {
    etapa: "MOVIMENTACAO DE TERRA",
    valor: 1549294.33,
    rsm2: 42.93,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC aplicado sobre 36.089 m2",
    fonte_pu: "Mediana de 7 projetos similares",
    ref_projetos: "Base parametrica Cartesian (75 exec)",
    aba: "-",
    maturidade: "amarelo",
    obs: "Sem projeto de terraplanagem detalhado nesta revisao."
  },
  {
    etapa: "INFRAESTRUTURA",
    valor: 8935057.93,
    rsm2: 247.59,
    origem: "IFC R26",
    fonte_qtd: "Modelo IFC R26 - quantitativos extraidos: estacas, blocos, baldrame",
    fonte_pu: "PUs da base Cartesian (75 exec) + cotacoes fornecedores",
    ref_projetos: "IFC R26 (DMA + Zeplin + Liberte) - ver aba Resumo Estrutura",
    aba: "Estacas + Resumo Estrutura",
    maturidade: "verde",
    obs: "Estaca helice continua diametro 60cm, 180 pecas x 30m = 5.400 m perfuracao."
  },
  {
    etapa: "CONTENCAO",
    valor: 1496965.50,
    rsm2: 41.48,
    origem: "Estimado",
    fonte_qtd: "Estimativa sem projeto de contencao",
    fonte_pu: "Referencia Elizabeth II x 0.90",
    ref_projetos: "Elizabeth II Royal Home (Gessele) como referencia, fator 0.90",
    aba: "-",
    maturidade: "vermelho",
    obs: "Sem projeto de contencao. Estimado com base no Elizabeth II com reducao de 10% pela diferenca de porte."
  },
  {
    etapa: "SUPRAESTRUTURA",
    valor: 28886959.09,
    rsm2: 800.44,
    origem: "IFC R26",
    fonte_qtd: "Modelo IFC R26 - 12.784 m3 concreto (pilares + vigas + lajes), por pavimento",
    fonte_pu: "Concreto fck30 R$ 590/m3 (usina), fck40 R$ 690/m3 (tipo). Aco CA-50 R$ 7,50/kg. Forma R$ 95/m2.",
    ref_projetos: "IFC R26 (DMA + Zeplin + Liberte)",
    aba: "Resumo Estrutura",
    maturidade: "verde",
    obs: "Quantitativos por pavimento: Terreo 720m3, G1-G5 ~210m3/pav, Lazer 350m3, Tipo (x24) 495m3/pav, Telhado 164m3, CMaq 24m3."
  },
  {
    etapa: "ALVENARIA",
    valor: 7770290.29,
    rsm2: 215.31,
    origem: "Parametrico + briefing R00",
    fonte_qtd: "Indice parametrico m2 alvenaria/m2 AC ajustado pelo briefing (tipologia studios + comercial)",
    fonte_pu: "Bloco ceramico 14cm R$ 3,80/un + argamassa + MO. Reboco R$ 7,00/m2 (base 37 exec).",
    ref_projetos: "Base parametrica + briefing R00 do cliente",
    aba: "DRYWALL",
    maturidade: "amarelo",
    obs: "Inclui drywall nas areas comuns. MO alvenaria + reboco ~40% do material."
  },
  {
    etapa: "SIST. E INST. ELETRICAS",
    valor: 7482260.32,
    rsm2: 207.33,
    origem: "IFC + DXF rev.01",
    fonte_qtd: "227 itens extraidos dos IFCs e DXFs eletricos (rev.01). Qtds por pavimento com repeticao.",
    fonte_pu: "PUs referenciados: Elizabeth II (Gessele) + SINAPI + cotacoes",
    ref_projetos: "IFC rev.01 + DXF rev.01 + Ref. Elizabeth II. Piloto IA 23/03/2026.",
    aba: "ELETRICO",
    maturidade: "verde",
    obs: "R02 detalhado. Subestacao: 2 trafos (500kVA + 300kVA). Gerador 500kVA R$ 340k. LEGENDA na aba: Verde=IFC/DXF, Amarelo=PU ref (EII/SINAPI), Vermelho=estimado."
  },
  {
    etapa: "SIST. E INST. HIDROSSANITARIAS",
    valor: 8208115.67,
    rsm2: 227.44,
    origem: "IFC rev.01 + briefings R00",
    fonte_qtd: "1 IFC hidraulico + 10 IFCs sanitarios processados. Qtds por pavimento.",
    fonte_pu: "PUs referencia: Elizabeth II + base 37 executivos Cartesian",
    ref_projetos: "IFC rev.01 (hidro + sanitario) + briefings R00",
    aba: "HIDROSSANITARIO",
    maturidade: "verde",
    obs: "R01 detalhado. LEGENDA: Verde=IFCs, Amarelo=PU ref (EII/base 37), Vermelho=estimado (MO, pluviais)."
  },
  {
    etapa: "INSTALACOES PREVENTIVAS (PPCI)",
    valor: 1188641.23,
    rsm2: 32.94,
    origem: "IFC + DXF + briefings R00",
    fonte_qtd: "Detectores, acionadores, avisadores, extintores extraidos por pavimento do IFC/DXF.",
    fonte_pu: "PUs referencia Elizabeth II + SINAPI. Cabos/eletrodutos por indice.",
    ref_projetos: "IFC + DXF + Briefings R00",
    aba: "PPCI",
    maturidade: "amarelo",
    obs: "R01 parcial. Verde=dados IFC/DXF, Amarelo=indice (cabos, eletrodutos), Vermelho=sem fonte (bomba PCI, reservatorio, sprinklers, MO)."
  },
  {
    etapa: "INSTALACOES DE GAS",
    valor: 485034.14,
    rsm2: 13.44,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Base 37 executivos + Elizabeth II como referencia",
    ref_projetos: "Base parametrica 37 exec + Elizabeth II",
    aba: "GAS",
    maturidade: "amarelo",
    obs: "Sem projeto de gas detalhado. MO ~30% do material."
  },
  {
    etapa: "LOUCAS E METAIS",
    valor: 1804442.50,
    rsm2: 50.00,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC (R$ 50/m2 = mediana base)",
    fonte_pu: "Base 37 executivos + Elizabeth II",
    ref_projetos: "Base parametrica 37 exec + Elizabeth II",
    aba: "LOUCAS E METAIS",
    maturidade: "amarelo",
    obs: "Aba detalhada tem itens unitarios (vaso, cuba, bancada) mas valor total ajustado pela mediana parametrica."
  },
  {
    etapa: "CLIMATIZACAO, EXAUSTAO MECANICA",
    valor: 1810216.72,
    rsm2: 50.16,
    origem: "Parametrico + briefings NBR",
    fonte_qtd: "Ventilacao/exaustao: premissas NBR. Infraestrutura AR: indice parametrico.",
    fonte_pu: "Base 37 executivos (infraestrutura AR). Demais: premissa NBR sem projeto.",
    ref_projetos: "Briefings R00 (premissas NBR) + base 37 exec",
    aba: "CLIMATIZACAO",
    maturidade: "amarelo",
    obs: "DWGs disponiveis mas nao processados nesta revisao. Amarelo=infra AR (PU ref base), Vermelho=premissa NBR."
  },
  {
    etapa: "INST. E EQUIP. ESPECIAIS",
    valor: 7864843.08,
    rsm2: 217.93,
    origem: "Parametrico",
    fonte_qtd: "Elevadores: 3un (cotacao). Automacao, CFTV, pressurizacao: parametrico.",
    fonte_pu: "Elevadores: cotacao fornecedor. Demais: Elizabeth II + base 37 exec.",
    ref_projetos: "Parametrico + Elizabeth II + cotacoes",
    aba: "Equipamentos Especiais + AUTOMACAO",
    maturidade: "amarelo",
    obs: "Elevadores R$ 950k (3x ThyssenKrupp). Automacao R$ 145k. Bombeamento R$ 140k. CFTV R$ 120k."
  },
  {
    etapa: "REV. ARGAMASSADOS PISO",
    valor: 8043843.78,
    rsm2: 222.89,
    origem: "Parametrico + PU base",
    fonte_qtd: "Area de piso por pavimento (indice parametrico)",
    fonte_pu: "Contrapiso R$ 12,10/m2 (mediana base 37 exec)",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: "PU-chave: contrapiso autonivelante R$ 12,10/m2."
  },
  {
    etapa: "REV. ARGAMASSADOS PAREDE",
    valor: 4705444.71,
    rsm2: 130.39,
    origem: "Parametrico + PU base",
    fonte_qtd: "Area de parede interna (indice parametrico)",
    fonte_pu: "Reboco massa unica R$ 7,00/m2 (mediana base 37 exec)",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: "PU-chave: reboco interno R$ 7,00/m2."
  },
  {
    etapa: "REV. ARGAMASSADOS TETO",
    valor: 221585.54,
    rsm2: 6.14,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Mediana base parametrica",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: ""
  },
  {
    etapa: "IMPERMEABILIZACAO",
    valor: 2578367.89,
    rsm2: 71.45,
    origem: "Parametrico + PU base",
    fonte_qtd: "Areas impermeabilizaveis por pavimento (indice parametrico)",
    fonte_pu: "Manta asfaltica R$ 82,15/m2 (mediana base 37 exec). MO R$ 72/m2.",
    ref_projetos: "Base parametrica 37 exec",
    aba: "IMPERMEABILIZACAO",
    maturidade: "amarelo",
    obs: "Aba detalhada: terreo, garagens, lazer, banheiros tipo, cobertura. PU-chave: manta R$ 82,15/m2."
  },
  {
    etapa: "ACABAMENTOS INT. PAREDE",
    valor: 5633830.37,
    rsm2: 156.11,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Mediana base parametrica",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: ""
  },
  {
    etapa: "ACABAMENTOS PISOS E PAVIMENTACOES",
    valor: 8043843.78,
    rsm2: 222.89,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Mediana base parametrica",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: ""
  },
  {
    etapa: "ACABAMENTOS INT. TETO",
    valor: 3041207.39,
    rsm2: 84.27,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Mediana base parametrica",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: ""
  },
  {
    etapa: "PINTURA INTERNA",
    valor: 5236853.02,
    rsm2: 145.11,
    origem: "Parametrico + PU base",
    fonte_qtd: "Area de pintura (indice parametrico: paredes + teto)",
    fonte_pu: "Acrilica R$ 15,00/m2, textura R$ 8,74/m2 (mediana base 37 exec)",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: "PU-chave: pintura acrilica R$ 15/m2, textura R$ 8,74/m2."
  },
  {
    etapa: "REV. E ACABAMENTOS FACHADA",
    valor: 6865001.49,
    rsm2: 190.23,
    origem: "Parametrico + PU base",
    fonte_qtd: "Area de fachada (perimetro x pe-direito x pavimentos)",
    fonte_pu: "Reboco externo R$ 15,25/m2 (mediana base). Demais: parametrico.",
    ref_projetos: "Base parametrica + briefing R00 (fachada definida pelo cliente)",
    aba: "-",
    maturidade: "amarelo",
    obs: "PU-chave: reboco externo R$ 15,25/m2."
  },
  {
    etapa: "ESQUADRIAS, VIDROS E FERRAGENS",
    valor: 14374910.73,
    rsm2: 398.32,
    origem: "Parametrico + briefing R00",
    fonte_qtd: "IFC Arquitetura (briefing R00) - quantitativos BIM de portas, janelas, vidros.",
    fonte_pu: "PUs parametricos + briefing. MO instalacao ~25%.",
    ref_projetos: "IFC Arquitetura (briefing R00) + base parametrica",
    aba: "ESQUADRIAS",
    maturidade: "amarelo",
    obs: "Portas de madeira, esquadrias aluminio, pele de vidro. MO ~25% do material."
  },
  {
    etapa: "COBERTURA",
    valor: 2429862.27,
    rsm2: 67.33,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC",
    fonte_pu: "Mediana base parametrica",
    ref_projetos: "Base parametrica Cartesian",
    aba: "-",
    maturidade: "amarelo",
    obs: ""
  },
  {
    etapa: "SERVICOS COMPLEMENTARES",
    valor: 10793453.26,
    rsm2: 299.08,
    origem: "Parametrico",
    fonte_qtd: "Indice parametrico R$/m2 AC (mobiliario, paisagismo, limpeza final)",
    fonte_pu: "Mediana base parametrica. Paisagismo R$ 180k (ref Elizabeth II). Limpeza R$ 54k.",
    ref_projetos: "Base parametrica + Elizabeth II",
    aba: "MOBILIARIO + PISCINA",
    maturidade: "amarelo",
    obs: "Mobiliario areas comuns R$ 500k (ref EII). Piscina R$ 256k. Paisagismo R$ 180k."
  },
  {
    etapa: "IMPREVISTOS",
    valor: 2230832.26,
    rsm2: 61.82,
    origem: "Percentual do total",
    fonte_qtd: "~1,3% do custo total",
    fonte_pu: "Percentual aplicado sobre o total das demais disciplinas",
    ref_projetos: "-",
    aba: "-",
    maturidade: "amarelo",
    obs: "Padrao Cartesian: 1-2% para imprevistos em fase de orcamento executivo."
  }
];

// === BUILD DOCUMENT ===
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: DARK },
        paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: ACCENT },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Arial", color: DARK },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ]
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
    }]
  },
  sections: [
    // === COVER PAGE ===
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1440, right: 1200, bottom: 1440, left: 1200 }
        }
      },
      children: [
        new Paragraph({ spacing: { before: 2000 } }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "CARTESIAN ENGENHARIA", bold: true, size: 20, color: DARK, font: "Arial" })
        ]}),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "Consultoria em Custos e Orcamentos", size: 18, color: "666666", font: "Arial" })
        ]}),
        new Paragraph({ spacing: { before: 600 } }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "ORCAMENTO EXECUTIVO", bold: true, size: 36, color: DARK, font: "Arial" })
        ]}),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, children: [
          new TextRun({ text: "ELECTRA TOWERS", bold: true, size: 30, color: ACCENT, font: "Arial" })
        ]}),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 100 }, children: [
          new TextRun({ text: "Revisao R02 \u2014 Formato EII", size: 22, color: "666666", font: "Arial" })
        ]}),
        new Paragraph({ spacing: { before: 600 } }),
        // Project data table
        new Table({
          width: { size: 6000, type: WidthType.DXA },
          columnWidths: [3000, 3000],
          rows: [
            ["Empresa", "Thozen"],
            ["Endereco", "Rua Rubens Alves, Bal. Pereque"],
            ["Cidade/UF", "Porto Belo, SC"],
            ["Area Construida", "36.088,85 m2"],
            ["Prazo de Obra", "36 meses"],
            ["Unid. Residenciais", "342"],
            ["Unid. Comerciais", "6"],
            ["Pavimentos", "35"],
            ["Subsolos", "1"],
            ["Vagas", "305"],
            ["Area de Lazer", "2.253,40 m2"],
            ["Area do Terreno", "824,72 m2"],
          ].map(([k, v], i) => new TableRow({ children: [
            dataCell(k, 3000, { bold: true, shade: i % 2 === 0 ? GRAY_BG : undefined }),
            dataCell(v, 3000, { align: AlignmentType.RIGHT, shade: i % 2 === 0 ? GRAY_BG : undefined })
          ]}))
        }),
        new Paragraph({ spacing: { before: 800 }, alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "Marco 2026", size: 20, color: "666666", font: "Arial" })
        ]}),
      ]
    },
    // === CONTENT ===
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1200, right: 1000, bottom: 1200, left: 1000 }
        }
      },
      headers: {
        default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
          new TextRun({ text: "Electra Towers \u2014 Orcamento Executivo R02", size: 16, color: "999999", font: "Arial" })
        ]})] })
      },
      footers: {
        default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "Cartesian Engenharia \u2014 Pag. ", size: 16, color: "999999", font: "Arial" }),
          new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "999999", font: "Arial" })
        ]})] })
      },
      children: [
        // === 1. INDICADORES ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. Indicadores-Chave")] }),
        new Table({
          width: { size: 9906, type: WidthType.DXA },
          columnWidths: [3302, 3302, 3302],
          rows: [
            new TableRow({ children: [
              headerCell("Indicador", 3302), headerCell("Valor", 3302), headerCell("Origem", 3302)
            ]}),
            ...([
              ["Valor Total", brlFull(TOTAL), "Soma de 26 disciplinas (EAP)"],
              ["R$/m2 AC", "R$ 4.697/m2", `${brlFull(TOTAL)} / 36.089 m2`],
              ["CUB/SC (fev/2026)", "R$ 3.019,26", "Sinduscon-SC, serie historica"],
              ["CUB Ratio", CUB_RATIO, `R$/m2 (4.697) / CUB (3.019) = ${CUB_RATIO}`],
              ["Area Construida", "36.088,85 m2", "Projeto arquitetonico (CAPA xlsx)"],
              ["Prazo", "36 meses", "Premissa do cliente"],
            ]).map(([ind, val, orig], i) => new TableRow({ children: [
              dataCell(ind, 3302, { bold: true, shade: i % 2 === 0 ? GRAY_BG : undefined }),
              dataCell(val, 3302, { align: AlignmentType.CENTER, shade: i % 2 === 0 ? GRAY_BG : undefined }),
              dataCell(orig, 3302, { shade: i % 2 === 0 ? GRAY_BG : undefined, fontSize: 16 }),
            ]}))
          ]
        }),

        new Paragraph({ spacing: { before: 300 } }),

        // === 2. MAPA DE MATURIDADE ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. Mapa de Maturidade das Fontes")] }),
        new Paragraph({ children: [new TextRun({ text: "Classificacao de cada disciplina conforme a origem dos dados:", size: 20, color: "666666" })] }),
        new Paragraph({ spacing: { before: 100 } }),

        new Table({
          width: { size: 9906, type: WidthType.DXA },
          columnWidths: [1200, 5506, 3200],
          rows: [
            new TableRow({ children: [
              headerCell("Nivel", 1200), headerCell("Significado", 5506), headerCell("% do Total", 3200)
            ]}),
            new TableRow({ children: [
              dataCell("VERDE", 1200, { bold: true, shade: GREEN_BG, align: AlignmentType.CENTER }),
              dataCell("Quantitativos extraidos de IFC/DXF (fonte direta do projeto)", 5506, { shade: GREEN_BG }),
              dataCell(pct(eap.filter(e => e.maturidade === "verde").reduce((s, e) => s + e.valor, 0) / TOTAL), 3200, { align: AlignmentType.CENTER, shade: GREEN_BG, bold: true }),
            ]}),
            new TableRow({ children: [
              dataCell("AMARELO", 1200, { bold: true, shade: YELLOW_BG, align: AlignmentType.CENTER }),
              dataCell("Mediana de projetos similares (base Cartesian, 75 executivos) ou PU de referencia", 5506, { shade: YELLOW_BG }),
              dataCell(pct(eap.filter(e => e.maturidade === "amarelo").reduce((s, e) => s + e.valor, 0) / TOTAL), 3200, { align: AlignmentType.CENTER, shade: YELLOW_BG, bold: true }),
            ]}),
            new TableRow({ children: [
              dataCell("VERMELHO", 1200, { bold: true, shade: RED_BG, align: AlignmentType.CENTER }),
              dataCell("Estimado sem projeto (referencia Elizabeth II x fator ou indice)", 5506, { shade: RED_BG }),
              dataCell(pct(eap.filter(e => e.maturidade === "vermelho").reduce((s, e) => s + e.valor, 0) / TOTAL), 3200, { align: AlignmentType.CENTER, shade: RED_BG, bold: true }),
            ]}),
          ]
        }),

        new Paragraph({ spacing: { before: 300 } }),

        // === 3. EAP COM RASTREABILIDADE ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("3. EAP com Rastreabilidade")] }),
        new Paragraph({ children: [new TextRun({ text: "Cada disciplina com valor, fonte dos quantitativos e fonte dos precos unitarios.", size: 20, color: "666666" })] }),
        new Paragraph({ spacing: { before: 100 } }),

        new Table({
          width: { size: 9906, type: WidthType.DXA },
          columnWidths: [3200, 1600, 1200, 1200, 2706],
          rows: [
            new TableRow({ children: [
              headerCell("Etapa", 3200), headerCell("Valor (R$)", 1600), headerCell("R$/m2", 1200),
              headerCell("%", 1200), headerCell("Origem", 2706)
            ]}),
            ...eap.map((e, i) => {
              const shade = e.maturidade === "verde" ? GREEN_BG : e.maturidade === "vermelho" ? RED_BG : i % 2 === 0 ? YELLOW_BG : GRAY_BG;
              return new TableRow({ children: [
                dataCell(e.etapa, 3200, { fontSize: 16, shade }),
                dataCell(brl(e.valor), 1600, { align: AlignmentType.RIGHT, fontSize: 16, shade }),
                dataCell(e.rsm2.toFixed(0), 1200, { align: AlignmentType.CENTER, fontSize: 16, shade }),
                dataCell(pct(e.valor / TOTAL), 1200, { align: AlignmentType.CENTER, fontSize: 16, shade }),
                dataCell(e.origem, 2706, { fontSize: 16, shade }),
              ]});
            }),
            new TableRow({ children: [
              dataCell("TOTAL", 3200, { bold: true, shade: DARK }),
              dataCell(brl(TOTAL), 1600, { bold: true, align: AlignmentType.RIGHT, shade: DARK }),
              dataCell("4.697", 1200, { bold: true, align: AlignmentType.CENTER, shade: DARK }),
              dataCell("100%", 1200, { bold: true, align: AlignmentType.CENTER, shade: DARK }),
              dataCell("", 2706, { shade: DARK }),
            ].map(c => {
              // Override to white text for total row
              return new TableCell({
                borders, width: c._properties?.width,
                shading: { fill: DARK, type: ShadingType.CLEAR },
                margins: cellMargins,
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
                  new TextRun({ text: "", bold: true, color: WHITE, font: "Arial", size: 18 })
                ]})]
              });
            })
            }),
          ]
        }),

        // Fix: proper total row
        new Paragraph({ spacing: { before: 60 }, children: [
          new TextRun({ text: "TOTAL: ", bold: true, size: 22, font: "Arial" }),
          new TextRun({ text: `${brlFull(TOTAL)} | R$/m2: 4.697 | CUB Ratio: ${CUB_RATIO}`, size: 22, font: "Arial" }),
        ]}),

        new Paragraph({ spacing: { before: 400 } }),

        // === 4. DETALHAMENTO DA RASTREABILIDADE ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("4. Rastreabilidade por Disciplina")] }),
        new Paragraph({ children: [new TextRun({ text: "Para cada disciplina: de onde veio cada quantitativo e cada preco unitario.", size: 20, color: "666666" })] }),

        ...eap.flatMap((e) => {
          const shade = e.maturidade === "verde" ? GREEN_BG : e.maturidade === "vermelho" ? RED_BG : YELLOW_BG;
          const items = [
            new Paragraph({ spacing: { before: 250 }, heading: HeadingLevel.HEADING_2, children: [
              new TextRun(`${e.etapa}`)
            ]}),
            new Table({
              width: { size: 9906, type: WidthType.DXA },
              columnWidths: [2800, 7106],
              rows: [
                new TableRow({ children: [
                  dataCell("Valor", 2800, { bold: true, shade: GRAY_BG }),
                  dataCell(`${brlFull(e.valor)} (R$ ${e.rsm2.toFixed(2)}/m2 | ${pct(e.valor / TOTAL)} do total)`, 7106, { shade: GRAY_BG }),
                ]}),
                new TableRow({ children: [
                  dataCell("Maturidade", 2800, { bold: true, shade }),
                  dataCell(e.maturidade.toUpperCase() + " \u2014 " + e.origem, 7106, { shade }),
                ]}),
                new TableRow({ children: [
                  dataCell("Fonte dos Qtds", 2800, { bold: true }),
                  dataCell(e.fonte_qtd, 7106),
                ]}),
                new TableRow({ children: [
                  dataCell("Fonte dos PUs", 2800, { bold: true }),
                  dataCell(e.fonte_pu, 7106),
                ]}),
                new TableRow({ children: [
                  dataCell("Ref. Projetos", 2800, { bold: true }),
                  dataCell(e.ref_projetos, 7106),
                ]}),
                new TableRow({ children: [
                  dataCell("Aba na Planilha", 2800, { bold: true }),
                  dataCell(e.aba, 7106),
                ]}),
                ...(e.obs ? [new TableRow({ children: [
                  dataCell("Observacoes", 2800, { bold: true }),
                  dataCell(e.obs, 7106, { fontSize: 16 }),
                ]})] : []),
              ]
            }),
          ];
          return items;
        }),

        new Paragraph({ spacing: { before: 400 } }),

        // === 5. PUs-CHAVE ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("5. Precos Unitarios de Referencia")] }),
        new Paragraph({ children: [new TextRun({ text: "PUs mais relevantes utilizados no orcamento e suas fontes.", size: 20, color: "666666" })] }),
        new Paragraph({ spacing: { before: 100 } }),

        new Table({
          width: { size: 9906, type: WidthType.DXA },
          columnWidths: [3500, 1600, 4806],
          rows: [
            new TableRow({ children: [
              headerCell("Item", 3500), headerCell("PU (R$)", 1600), headerCell("Fonte", 4806)
            ]}),
            ...([
              ["Concreto fck30 (usinado)", "R$ 590/m3", "Cotacao fornecedor local (Porto Belo/SC)"],
              ["Concreto fck40 (usinado)", "R$ 690/m3", "Cotacao fornecedor local (pavtos tipo)"],
              ["Aco CA-50", "R$ 7,50/kg", "Cotacao fornecedor + base Cartesian"],
              ["Forma (madeira)", "R$ 95/m2", "Indice base Cartesian (75 exec)"],
              ["Contrapiso autonivelante", "R$ 12,10/m2", "Mediana base 37 executivos"],
              ["Reboco massa unica interno", "R$ 7,00/m2", "Mediana base 37 executivos"],
              ["Reboco externo fachada", "R$ 15,25/m2", "Mediana base 37 executivos"],
              ["Manta asfaltica (material)", "R$ 82,15/m2", "Mediana base 37 executivos"],
              ["MO impermeabilizacao", "R$ 72,00/m2", "Base Cartesian"],
              ["Pintura acrilica", "R$ 15,00/m2", "Mediana base 37 executivos"],
              ["Pintura textura", "R$ 8,74/m2", "Mediana base 37 executivos"],
              ["Bloco ceramico 14cm", "R$ 3,80/un", "Cotacao + base Cartesian"],
              ["Elevador (ThyssenKrupp)", "~R$ 317k/un", "Cotacao fornecedor (3 unidades)"],
              ["Gerador 500kVA", "R$ 340.000", "Cotacao fornecedor"],
              ["Transformador 500kVA seco", "R$ 79.000", "Cotacao fornecedor (aba ELETRICO)"],
            ]).map(([item, pu, fonte], i) => new TableRow({ children: [
              dataCell(item, 3500, { shade: i % 2 === 0 ? GRAY_BG : undefined }),
              dataCell(pu, 1600, { align: AlignmentType.CENTER, bold: true, shade: i % 2 === 0 ? GRAY_BG : undefined }),
              dataCell(fonte, 4806, { fontSize: 16, shade: i % 2 === 0 ? GRAY_BG : undefined }),
            ]}))
          ]
        }),

        new Paragraph({ spacing: { before: 400 } }),

        // === 6. PREMISSAS ===
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("6. Premissas e Limitacoes")] }),
        ...([
          "CUB referencia: R$ 3.019,26 (SC, fevereiro/2026) - fonte Sinduscon-SC",
          "Area construida: 36.088,85 m2 (projeto arquitetonico, CAPA do xlsx)",
          "Disciplinas com IFC/DXF (verde): Eletrico R02, Hidrossanitario R01, PPCI R01, Estrutura R26",
          "Disciplinas parametricas (amarelo): mediana de 7 projetos similares extraida da base Cartesian (75 executivos)",
          "Projeto de referencia principal: Elizabeth II Royal Home (Gessele) - mesmo porte e padrao",
          "Contencao estimada sem projeto (vermelho) - requer projeto especifico para R03",
          "Abas vazias na planilha: EPCs, Canteiro, Cont.Tecnol., Fund. Rasa, Calculo de apoio, Escoramento, MO Estrutura - a preencher nas proximas revisoes",
          "Valores nao incluem terreno, incorporacao, marketing ou despesas financeiras",
          "Para proxima revisao (R03): processar DWGs de climatizacao, detalhar MO eletrica e hidro, obter projeto de contencao",
        ]).map(t => new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 60 },
          children: [new TextRun({ text: t, size: 20, font: "Arial" })]
        })),

        new Paragraph({ spacing: { before: 600 }, alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "Cartesian Engenharia", bold: true, size: 22, color: DARK, font: "Arial" })
        ]}),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [
          new TextRun({ text: "Integracao de escopo, custo e prazo", size: 18, color: "666666", font: "Arial" })
        ]}),
      ]
    }
  ]
});

const OUTPUT = "/Users/leokock/orcamentos/executivos/thozen-electra/entregas/CTN-TZN_ELT-Orcamento-Executivo-R02-DOC-RASTREAVEL.docx";

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUTPUT, buf);
  console.log("Gerado: " + OUTPUT);
}).catch(err => console.error("ERRO:", err));
