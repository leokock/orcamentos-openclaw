// Gera COMO-FALAR-COM-CARTESIANO.docx no padrão visual Cartesian.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, WidthType, ShadingType, TabStopType, TabStopPosition,
  PageNumber, PageBreak, ExternalHyperlink, VerticalAlign,
} = require("docx");

// Paleta Cartesian V2
const AZUL = "245AE4";
const LARANJA = "FD3400";
const PRETO = "111111";
const CINZA_MEDIO = "E7E7E9";
const CINZA_CLARO = "F4F4F4";
const BRANCO = "FFFFFF";

// ---- Helpers ----
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after ?? 120 },
    alignment: opts.align,
    children: [new TextRun({ text, bold: opts.bold, italics: opts.italic, size: opts.size ?? 22, color: opts.color ?? PRETO, font: "Arial" })],
  });
}

function pRich(runs, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after ?? 120 },
    alignment: opts.align,
    children: runs.map(r => new TextRun({
      text: r.text, bold: r.bold, italics: r.italic, size: r.size ?? 22,
      color: r.color ?? PRETO, font: "Arial",
    })),
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 180 },
    children: [new TextRun({ text, bold: true, size: 36, color: AZUL, font: "Arial" })],
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 140 },
    children: [new TextRun({ text, bold: true, size: 28, color: PRETO, font: "Arial" })],
  });
}

function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 220, after: 100 },
    children: [new TextRun({ text, bold: true, size: 24, color: AZUL, font: "Arial" })],
  });
}

function bullet(text, opts = {}) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: [new TextRun({ text, size: 22, color: PRETO, font: "Arial", italics: opts.italic, bold: opts.bold })],
  });
}

function bulletRich(runs) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80 },
    children: runs.map(r => new TextRun({
      text: r.text, bold: r.bold, italics: r.italic, size: 22,
      color: r.color ?? PRETO, font: "Arial",
    })),
  });
}

function code(text) {
  // run estilizado tipo código (fundo cinza claro não dá em run-level no docx-js — usa Consolas + cor laranja)
  return new TextRun({ text, font: "Consolas", size: 20, color: LARANJA });
}

function callout(text, color = AZUL) {
  // parágrafo destacado com borda esquerda colorida
  return new Paragraph({
    spacing: { before: 120, after: 180 },
    indent: { left: 200 },
    border: { left: { style: BorderStyle.SINGLE, size: 24, color, space: 12 } },
    children: [new TextRun({ text, size: 22, color: PRETO, font: "Arial", italics: true })],
  });
}

function thinDivider() {
  return new Paragraph({
    spacing: { before: 240, after: 240 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: CINZA_MEDIO, space: 1 } },
    children: [new TextRun("")],
  });
}

// Tabela atalhos
function tableHeaderCell(text, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { fill: AZUL, type: ShadingType.CLEAR },
    margins: { top: 100, bottom: 100, left: 140, right: 140 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: AZUL },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: AZUL },
      left: { style: BorderStyle.SINGLE, size: 4, color: AZUL },
      right: { style: BorderStyle.SINGLE, size: 4, color: AZUL },
    },
    children: [new Paragraph({
      children: [new TextRun({ text, bold: true, color: BRANCO, size: 22, font: "Arial" })],
    })],
  });
}

function tableCell(text, width, opts = {}) {
  const border = { style: BorderStyle.SINGLE, size: 2, color: CINZA_MEDIO };
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { fill: opts.bg ?? BRANCO, type: ShadingType.CLEAR },
    margins: { top: 80, bottom: 80, left: 140, right: 140 },
    borders: { top: border, bottom: border, left: border, right: border },
    children: [new Paragraph({
      children: [new TextRun({
        text, size: 22, font: opts.font ?? "Arial",
        color: opts.color ?? PRETO, italics: opts.italic, bold: opts.bold,
      })],
    })],
  });
}

// ---- Conteúdo ----

const content = [];

// Título
content.push(new Paragraph({
  spacing: { after: 100 },
  children: [new TextRun({ text: "Como falar com o @Cartesiano", bold: true, size: 48, color: AZUL, font: "Arial" })],
}));
content.push(p("Guia rápido pro time da Cartesian usar o bot no Slack sem decorar comando nenhum. Fale natural — o bot entende.", { italic: true, color: "555555" }));

content.push(callout(
  "Onde falar: #custos-ia-paramétrico (canal principal) ou qualquer DM/canal onde o bot esteja. " +
  "Como chamar: @Cartesiano [pedido]. " +
  "Resposta: geralmente em 30 segundos a 5 minutos, dependendo do que foi pedido.",
  AZUL,
));

content.push(thinDivider());

// ===== 1. Quantitativos =====
content.push(h1("1. Análise de pastas e extração de quantitativos"));
content.push(pRich([
  { text: "Use quando: ", bold: true },
  { text: "você tem pastas com projetos (planilhas + IFC + DWG + PDFs) e quer saber " },
  { text: "quanto material/peças tem", bold: true },
  { text: ", organizadas pra orçamento." },
]));

content.push(h3("Exemplos de pedido (qualquer um funciona)"));
[
  '@Cartesiano analisa essas pastas: G:\\Drives compartilhados\\...\\Quantitativos fornecidos. Tem PCI, sanitária e telecom.',
  '@Cartesiano extrai os quantitativos do Alfa Colinas',
  '@Cartesiano levanta os quantitativos de hidráulica e elétrica desse projeto: [caminho]',
  '@Cartesiano olha o que dá pra extrair dessas pastas: [caminho]',
  '@Cartesiano monta o pacote de extração de [projeto]',
].forEach(t => content.push(bulletRich([{ text: t, font: "Consolas", color: "333333" }])));

content.push(h3("O que o bot entrega"));
content.push(p("Pasta em _Executivo_IA/[slug]/ com:"));
content.push(bullet("00-projeto/ — análise estratégica + inventário dos arquivos"));
content.push(bullet("01-[disciplina]/, 02-[disciplina]/, etc — uma pasta por disciplina, cada uma com:"));
content.push(bullet("    quantitativos-[disc].xlsx — planilha consolidada com quantidades por pavimento"));
content.push(bullet("    audit-planilha-projetista.md — auditoria da planilha do projetista (totais, divergências)"));
content.push(bullet("    extracao-ifc-por-pavimento.csv — extração do BIM quando tem IFC"));
content.push(bullet("    gap-[tema].md — onde tem informação faltando"));

content.push(h3("O que o bot precisa"));
content.push(bulletRich([
  { text: "Caminho da pasta ", bold: true },
  { text: "(no Drive, do tipo " },
  { text: "G:\\Drives compartilhados\\03 CTN Projetos\\...", font: "Consolas", color: "333333" },
  { text: ") — pode colar do Windows Explorer" },
]));
content.push(bulletRich([
  { text: "(opcional) ", italic: true },
  { text: "Quais disciplinas ", bold: true },
  { text: "olhar — se não disser, ele detecta sozinho" },
]));

content.push(thinDivider());

// ===== 2. Precificação =====
content.push(h1("2. Precificação 3 fontes"));
content.push(pRich([
  { text: "Use quando: ", bold: true },
  { text: "os quantitativos já existem (você ou alguém já pediu a extração antes) e agora quer " },
  { text: "valores em R$", bold: true },
  { text: " com 3 referências de preço diferentes." },
]));

content.push(h3("Exemplos de pedido"));
[
  '@Cartesiano precifica o Alfa Colinas',
  '@Cartesiano põe os preços no Bela Vida',
  '@Cartesiano monta a precificação de [projeto]',
  '@Cartesiano compara o [projeto] com Aquos',
  '@Cartesiano quanto custa o sanitário do [projeto]?',
  '@Cartesiano puxa preço da base Cartesian pro [projeto]',
  '@Cartesiano orça isso aí (em thread onde os quantitativos já foram entregues)',
].forEach(t => content.push(bulletRich([{ text: t, font: "Consolas", color: "333333" }])));

content.push(h3("O que o bot entrega"));
content.push(p("Pasta XX-precificacao-banco-de-dados/ dentro de _Executivo_IA/[slug]/ com:"));
content.push(bulletRich([
  { text: "1 xlsx por disciplina", bold: true },
  { text: " com " },
  { text: "3 colunas de preço lado a lado:", bold: true },
]));
content.push(bulletRich([
  { text: "    Azul ", color: AZUL, bold: true },
  { text: "— preço de um empreendimento Cartesian similar (você escolhe qual no Slack)" },
]));
content.push(bulletRich([
  { text: "    Verde ", color: "008000", bold: true },
  { text: "— preço de varejo BR pesquisado na internet" },
]));
content.push(bulletRich([
  { text: "    Laranja ", color: "D86A00", bold: true },
  { text: "— preço pago em obras Cartesian anteriores (banco MongoDB)" },
]));
content.push(bullet("Subtotal calculado por linha (você pode mexer na quantidade que o Excel recalcula)"));
content.push(bulletRich([
  { text: "Confiança ", bold: true },
  { text: "de cada match: alta / média / baixa (linhas " },
  { text: "baixa", bold: true },
  { text: " ficam com fundo amarelo pra você revisar)" },
]));
content.push(bullet("README explicando metodologia, cobertura e subtotais por fonte"));

content.push(h3("Fluxo (você só responde 1 coisa)"));
const fluxo = [
  "Você pede a precificação",
  'Bot pergunta: "Achei 3 obras como referência: Aquos, Malta, Atlantia. Qual usar?"',
  'Você responde com o nome (ex: "Aquos")',
  "Bot faz tudo (3–5 minutos)",
  "Bot entrega o pacote pronto na thread",
];
fluxo.forEach((t, i) => content.push(new Paragraph({
  numbering: { reference: "numbers", level: 0 },
  spacing: { after: 80 },
  children: [new TextRun({ text: t, size: 22, color: PRETO, font: "Arial" })],
})));

content.push(h3("O que o bot precisa"));
content.push(bulletRich([
  { text: "Nome do projeto ", bold: true },
  { text: "(slug — geralmente o nome da pasta, tipo " },
  { text: "alfa-colinas", font: "Consolas", color: "333333" },
  { text: ")" },
]));
content.push(bulletRich([
  { text: "Qual obra usar como referência ", bold: true },
  { text: "(o bot pergunta se não disser)" },
]));
content.push(bullet("Quantitativos já extraídos (se não tem, ele faz a extração primeiro)"));

content.push(thinDivider());

// ===== 3. Outros =====
content.push(h1("3. Outros pedidos comuns"));

content.push(h3("Paramétrico (estimativa rápida pré-projeto)"));
[
  '@Cartesiano monta um paramétrico pra esse projeto: [dados básicos]',
  '@Cartesiano qual o R$/m² médio pra prédio de 20 andares?',
  '@Cartesiano compara o paramétrico do Catena com o Connect',
].forEach(t => content.push(bulletRich([{ text: t, font: "Consolas", color: "333333" }])));

content.push(h3("Consultar base Cartesian"));
[
  '@Cartesiano qual o custo médio de supraestrutura na nossa base?',
  '@Cartesiano qual a mediana de hidráulica em prédio residencial?',
  '@Cartesiano me mostra projetos similares ao [X] na base',
].forEach(t => content.push(bulletRich([{ text: t, font: "Consolas", color: "333333" }])));

content.push(h3("Analisar planilha recebida do cliente"));
content.push(bulletRich([{ text: '@Cartesiano já enviei a planilha aqui na thread, analisa pra mim', font: "Consolas", color: "333333" }]));
content.push(callout(
  "Importante: mande primeiro o arquivo na thread, depois mande a mensagem de texto puro avisando. " +
  "Não chame o bot na MESMA mensagem do upload — ele trava silenciosamente.",
  LARANJA,
));
content.push(bulletRich([{ text: '@Cartesiano dá uma olhada nesse orçamento que recebi', font: "Consolas", color: "333333" }]));

content.push(thinDivider());

// ===== Regras =====
content.push(h1("Regras importantes pro time"));

content.push(h3("Como mandar arquivo"));
content.push(new Paragraph({
  numbering: { reference: "numbers2", level: 0 },
  spacing: { after: 80 },
  children: [
    new TextRun({ text: "Primeiro ", bold: true, size: 22, font: "Arial" }),
    new TextRun({ text: "faça upload do arquivo na thread (xlsx, pdf, ifc, etc)", size: 22, font: "Arial" }),
  ],
}));
content.push(new Paragraph({
  numbering: { reference: "numbers2", level: 0 },
  spacing: { after: 80 },
  children: [
    new TextRun({ text: "Depois ", bold: true, size: 22, font: "Arial" }),
    new TextRun({ text: "mande uma mensagem de TEXTO PURO: ", size: 22, font: "Arial" }),
    new TextRun({ text: "@Cartesiano já enviei o arquivo", font: "Consolas", size: 20, color: LARANJA }),
  ],
}));
content.push(new Paragraph({
  numbering: { reference: "numbers2", level: 0 },
  spacing: { after: 80 },
  children: [new TextRun({ text: "Não chame o bot na MESMA mensagem do upload — ele trava silenciosamente", size: 22, font: "Arial" })],
}));
content.push(new Paragraph({
  numbering: { reference: "numbers2", level: 0 },
  spacing: { after: 80 },
  children: [new TextRun({ text: "Arquivo grande (>100MB)? Suba no Drive e mande o link", size: 22, font: "Arial" })],
}));

content.push(h3("O que o bot NÃO faz"));
content.push(bullet("Não responde sobre agenda, emails ou tarefas pessoais"));
content.push(bullet("Não inventa valores — se não tem na base, ele avisa"));
content.push(bullet("Não mexe em pastas/projetos sem o nome explícito"));
content.push(bullet("Não posta erros técnicos ou stack traces no canal (resolve internamente)"));

content.push(h3("O bot enrolou ou travou?"));
content.push(bullet("Aguarde 1–2 minutos (operações IFC/MongoDB demoram)"));
content.push(bullet("Se passou de 10 minutos sem resposta: tente reformular o pedido em outra thread"));
content.push(bulletRich([
  { text: "Avise o Leo " },
  { text: "(@Leo Kock)", font: "Consolas", color: "333333" },
  { text: " com link da thread" },
]));

content.push(thinDivider());

// ===== Atalhos =====
content.push(h1("Atalhos pelo nome do projeto"));
content.push(p("O time costuma usar atalhos pra projetos. O bot reconhece:"));

const atalhos = [
  ['"alfa" / "Alfa Colinas"', "executivos/alfa-colinas/"],
  ['"bela vida" / "Chiquetti"', "executivos/chiquetti-bela-vida-claude/"],
  ['"electra" / "Thozen"', "executivos/thozen-electra/"],
  ['"senna"', "executivos/senna-tower/"],
  ['"gessele"', "executivos/gessele-elisabeth/"],
];

content.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [3600, 5760],
  rows: [
    new TableRow({
      tableHeader: true,
      children: [
        tableHeaderCell("Você fala", 3600),
        tableHeaderCell("Bot entende", 5760),
      ],
    }),
    ...atalhos.map(([fala, entende], i) => new TableRow({
      children: [
        tableCell(fala, 3600, { bg: i % 2 ? CINZA_CLARO : BRANCO }),
        tableCell(entende, 5760, { bg: i % 2 ? CINZA_CLARO : BRANCO, font: "Consolas", color: "333333" }),
      ],
    })),
  ],
}));

content.push(p("Se mencionar um nome que o bot não conhece, ele pergunta o caminho.", { italic: true, color: "555555", after: 200 }));

content.push(thinDivider());

// ===== Em dúvida =====
content.push(h1("Em dúvida?"));
content.push(p("Mande no chat:"));
content.push(new Paragraph({
  spacing: { before: 100, after: 200 },
  indent: { left: 200 },
  border: { left: { style: BorderStyle.SINGLE, size: 24, color: AZUL, space: 12 } },
  children: [new TextRun({ text: "@Cartesiano o que você consegue fazer?", font: "Consolas", size: 24, color: AZUL, bold: true })],
}));
content.push(p("Ele lista os domínios e dá exemplos.", { italic: true, color: "555555" }));

// ---- Doc ----
const doc = new Document({
  creator: "Cartesian Engenharia",
  title: "Como falar com o @Cartesiano",
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, color: AZUL, font: "Arial" },
        paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, color: PRETO, font: "Arial" },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, color: AZUL, font: "Arial" },
        paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers2",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4 (mercado BR)
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Cartesian Engenharia · Como falar com o @Cartesiano", color: "999999", size: 18, font: "Arial" })],
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: AZUL, space: 4 } },
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Página ", color: "999999", size: 18, font: "Arial" }),
            new TextRun({ children: [PageNumber.CURRENT], color: "999999", size: 18, font: "Arial" }),
          ],
        })],
      }),
    },
    children: content,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const outPath = path.join(__dirname, "COMO-FALAR-COM-CARTESIANO.docx");
  fs.writeFileSync(outPath, buf);
  console.log("Wrote", outPath, "(", buf.length, "bytes)");
});
