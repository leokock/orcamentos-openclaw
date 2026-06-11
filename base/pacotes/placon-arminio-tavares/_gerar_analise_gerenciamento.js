const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
        ShadingType, LevelFormat, PageBreak, PageNumber } = require('docx');

const border = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
const borders = { top: border, bottom: border, left: border, right: border };
const thBg = { fill: "1F3864", type: ShadingType.CLEAR };
const altBg = { fill: "F2F2F2", type: ShadingType.CLEAR };
const redBg = { fill: "FCE4D6", type: ShadingType.CLEAR };
const greenBg = { fill: "E2EFDA", type: ShadingType.CLEAR };
const yellowBg = { fill: "FFF2CC", type: ShadingType.CLEAR };

function P(text, opts = {}) {
  const runs = Array.isArray(text)
    ? text
    : [new TextRun({ text, ...opts })];
  return new Paragraph({ children: runs, spacing: { after: 120 }, ...(opts.paragraph || {}) });
}
function H1(t) { return new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, bold: true, size: 30 })], spacing: { before: 280, after: 160 } }); }
function H2(t) { return new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, bold: true, size: 26 })], spacing: { before: 240, after: 140 } }); }
function H3(t) { return new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: t, bold: true, size: 22 })], spacing: { before: 200, after: 120 } }); }
function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: [new TextRun(text)],
    spacing: { after: 80 },
  });
}

function cell(text, opts = {}) {
  const { w = 1800, bold = false, shading = null, align = AlignmentType.LEFT, color = "000000", bg = null } = opts;
  const runs = Array.isArray(text) ? text : [new TextRun({ text: String(text), bold, color, size: 20 })];
  return new TableCell({
    borders,
    width: { size: w, type: WidthType.DXA },
    shading: bg || shading,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({ alignment: align, children: runs })]
  });
}

function headerRow(cols, widths) {
  return new TableRow({
    tableHeader: true,
    children: cols.map((t, i) => cell(t, {
      w: widths[i], bold: true, color: "FFFFFF", shading: thBg, align: AlignmentType.CENTER
    }))
  });
}

function dataRow(cols, widths, alt = false, bgs = null) {
  return new TableRow({
    children: cols.map((t, i) => cell(t, {
      w: widths[i],
      bg: (bgs && bgs[i]) ? bgs[i] : (alt ? altBg : null),
      align: (i === 0 ? AlignmentType.LEFT : AlignmentType.RIGHT),
    }))
  });
}

function table(header, widths, rows, bgsPerRow = null) {
  const total = widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      headerRow(header, widths),
      ...rows.map((r, i) => dataRow(r, widths, i % 2 === 1, bgsPerRow ? bgsPerRow[i] : null))
    ]
  });
}

// -------- CONTEÚDO --------

const children = [];

// TÍTULO
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "ANÁLISE DE GERENCIAMENTO", bold: true, size: 36, color: "1F3864" })],
  spacing: { before: 0, after: 120 }
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "Paramétrico Placon Armínio Tavares vs Base Cartesian", bold: true, size: 26, color: "404040" })],
  spacing: { after: 60 }
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "Data: 2026-04-22  |  Base: indices-cartesian (126 projetos, 6.578 índices)", size: 20, italics: true, color: "595959" })],
  spacing: { after: 320 }
}));

// 1. RESUMO EXECUTIVO
children.push(H1("1. Resumo Executivo"));
children.push(P([
  new TextRun({ text: "Contexto. ", bold: true }),
  new TextRun("Placon Armínio Tavares — residencial vertical, 4.077,29 m² AC, 55 UR, 18 pavimentos (15 tipo), prazo 24 meses, padrão médio-alto, Florianópolis-centro. Grand Total do paramétrico = R$ 17,87M. Após overrides do Leo em 22/04, o macrogrupo "),
  new TextRun({ text: "Gerenciamento", bold: true }),
  new TextRun(" fechou em "),
  new TextRun({ text: "R$ 3.483.840 (R$ 854,45/m², 19,50% do total).", bold: true })
]));
children.push(P([
  new TextRun({ text: "Veredito. ", bold: true }),
  new TextRun("O Gerenciamento do Placon está "),
  new TextRun({ text: "acima do P75 da base (R$ 507,78/m²) ", bold: true, color: "C00000" }),
  new TextRun("e próximo do P85 geral (n=131). Quando filtramos para o nicho comparável (padrão médio-alto, n=36), fica "),
  new TextRun({ text: "entre mediana (R$ 474,74/m²) e P75 (R$ 1.223,46/m²)", bold: true }),
  new TextRun(" — não é outlier, mas está na metade superior. O problema não é preço unitário: os PUs do Placon estão dentro da faixa da base. O inflator é "),
  new TextRun({ text: "a soma de homens-mês e três itens vb (Taxas, Equipamentos, Projetos)", bold: true }),
  new TextRun(" que empurram o macrogrupo pra cima. Há margem para reduzir para ~R$ 3,09M (R$ 759/m², 17,7% do total), mantendo segurança.")
]));
children.push(P([
  new TextRun({ text: "Recomendação. ", bold: true }),
  new TextRun("Rever 3 itens (Taxas e seguros, Equipamentos grua+cremalheira, Limpeza 2x). Impacto: "),
  new TextRun({ text: "R$ 390k de economia (≈ 2,2 p.p. do Grand Total), novo Gerenciamento R$ 759/m².", bold: true, color: "00703C" })
]));

// 2. BASE DE COMPARAÇÃO
children.push(H1("2. Base de comparação"));
children.push(P("Fonte primária: Supabase indices-cartesian (projeto nzyyptcfiqalhpybklfd), que consolida 126 projetos residenciais verticais entregues pela Cartesian. Tabelas consultadas: calibracao_global, calibracao_condicional, indices_estruturais, pus_cross_v2, indices_derivados_v2, projetos."));

children.push(H2("2.1 Distribuição de Gerenciamento na base (R$/m²)"));
children.push(table(
  ["Fatia", "n", "P10", "P25", "Mediana", "Média", "P75", "P90", "Máx"],
  [2500, 500, 950, 950, 950, 950, 950, 950, 950],
  [
    ["Geral (todos)",        "131", "60,73",   "126,25",  "224,91", "424,18", "507,78",   "942,33",   "2.996,80"],
    ["Padrão econômico",     "2",   "228,97",  "228,97",  "259,20", "259,20", "289,44",   "289,44",   "289,44"],
    ["Padrão médio",         "2",   "255,88",  "255,88",  "267,37", "267,37", "278,87",   "278,87",   "278,87"],
    ["Padrão médio-alto",    "36",  "267,88",  "339,65",  "474,74", "2.435,85","1.223,46", "10.661,12","22.210,51"],
    ["Padrão alto",          "22",  "437,54",  "535,79",  "640,41", "1.883,53","1.715,95", "3.120,05", "13.434,29"],
  ]
));
children.push(P([
  new TextRun({ text: "Leitura. ", bold: true }),
  new TextRun("A base tem cauda direita muito pesada (outliers de projetos pequenos onde gerenciamento vira % enorme do R$/m²), então média não serve. Use "),
  new TextRun({ text: "mediana e P75", bold: true }),
  new TextRun(" do padrão médio-alto como âncora: mediana R$ 474,74/m², P75 R$ 1.223/m².")
]));

children.push(H2("2.2 Posição do Placon"));
children.push(table(
  ["Métrica", "Placon", "Mediana médio-alto", "P75 médio-alto", "Posição"],
  [2600, 1300, 1800, 1600, 1900],
  [
    ["R$/m² Gerenciamento",     "854,45",  "474,74",   "1.223,46",  "≈ P65 médio-alto"],
    ["% Grand Total",           "19,50%",  "— (estrutural)", "≈ 15-16% típico", "Acima do típico"],
    ["Valor absoluto (R$)",     "3,48M",   "1,94M*",   "5,00M*",    "Acima mediana"],
  ]
));
children.push(P([new TextRun({ text: "* Estimativa: mediana R$/m² × AC 4.077 m².", italics: true, size: 18 })]));

children.push(H2("2.3 Filtro de projetos pareados (padrão médio-alto, AC 3-6k m²)"));
children.push(P("9 projetos com total_rs populado nesse filtro:"));
children.push(table(
  ["Slug", "AC (m²)", "UR", "Total (R$)", "R$/m² total"],
  [3200, 1000, 700, 1600, 1500],
  [
    ["grandezza-gran-royal",             "5.225",  "0",  "10,02M", "1.918"],
    ["pass-e-vancouver",                 "5.554",  "0",  "15,32M", "2.758"],
    ["macom-adda",                       "4.358",  "0",  "13,43M", "3.083"],
    ["muller-empreendimentos-guanabara", "4.441",  "0",  "14,34M", "3.229"],
    ["paludo-volo-ocean",                "3.264",  "0",  "11,92M", "3.650"],
    ["parkside-trindade",                "3.333",  "0",  "12,52M", "3.756"],
    ["inbrasul-opus",                    "4.411",  "0",  "16,76M", "3.799"],
    ["nova-empreendimentos-domus",       "5.009",  "0",  "38,41M", "7.668"],
    ["PLACON (este)",                    "4.077",  "55", "17,87M", "4.383"]
  ]
));
children.push(P([
  new TextRun({ text: "Observação: ", bold: true }),
  new TextRun("o Placon (R$ 4.383/m² total) é o 2º mais caro desse grupo em R$/m² depois do Domus. O Gerenciamento puxando pra cima é um dos motivos.")
]));

// 3. DECOMPOSIÇÃO ITEM A ITEM
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("3. Itens do Gerenciamento — Placon vs base"));

children.push(H2("3.1 Breakdown completo (20 linhas)"));
children.push(table(
  ["Item", "Valor (R$)", "R$/m²", "% Geren", "% Total", "Diagnóstico"],
  [2200, 1200, 900, 900, 900, 2100],
  [
    ["Projetos (Arq+compl+compat)",     "650.000", "159,4", "18,7%", "3,64%", "Acima mediana"],
    ["Consultorias (ATP+BIM)",          "180.000", "44,2",  "5,2%",  "1,01%", "OK"],
    ["Ensaios (ctrl tecnol)",           "130.000", "31,9",  "3,7%",  "0,73%", "OK"],
    ["Taxas e seguros",                 "380.000", "93,2",  "10,9%", "2,13%", "P90 da base"],
    ["Engenheiro PJ (24m)",             "252.000", "61,8",  "7,2%",  "1,41%", "OK (PU P50-P75)"],
    ["Mestre obras (24m, override 8k)", "192.000", "47,1",  "5,5%",  "1,07%", "OK (abaixo P25)"],
    ["Encarregado (24m)",               "144.000", "35,3",  "4,1%",  "0,81%", "OK"],
    ["Estagiário",                      "0",       "0,0",   "0,0%",  "0,00%", "Removido (Leo)"],
    ["Téc. segurança",                  "0",       "0,0",   "0,0%",  "0,00%", "Removido (Leo)"],
    ["Almoxarife (24m)",                "81.048",  "19,9",  "2,3%",  "0,45%", "OK"],
    ["Limpeza obra 2× (24m)",           "120.000", "29,4",  "3,4%",  "0,67%", "Excesso (2p?)"],
    ["Vigilância (24m, override 5k)",   "120.000", "29,4",  "3,4%",  "0,67%", "OK (abaixo base)"],
    ["EPCs (AC<5k)",                    "150.000", "36,8",  "4,3%",  "0,84%", "OK"],
    ["EPI (24m)",                       "21.792",  "5,3",   "0,6%",  "0,12%", "OK"],
    ["Meio ambiente (PCMAT/PCMSO)",     "45.000",  "11,0",  "1,3%",  "0,25%", "OK"],
    ["Op. inicial (mobilização)",       "55.000",  "13,5",  "1,6%",  "0,31%", "OK"],
    ["Inst. provisórias (canteiro)",    "160.000", "39,2",  "4,6%",  "0,90%", "OK"],
    ["Desp. consumo (água/en/IPTU)",    "276.000", "67,7",  "7,9%",  "1,54%", "OK"],
    ["Equipamentos (grua+cremalheira)", "480.000", "117,7", "13,8%", "2,69%", "Limite superior"],
    ["Comunic. visual (placas/tapume)", "47.000",  "11,5",  "1,3%",  "0,26%", "OK"],
    ["TOTAL",                           "3.483.840", "854,4", "100%", "19,50%", "Acima P75 geral"]
  ]
));

children.push(H2("3.2 Benchmark por PU (pus_cross_v2, n clusters)"));
children.push(table(
  ["Cluster da base", "Unid", "n_proj", "P25", "Mediana", "P75", "PU Placon"],
  [3200, 700, 1000, 1000, 1000, 1000, 1300],
  [
    ["Mestre 1",                     "mês",  "29", "4.550", "6.500",  "6.500",  "8.000 (ok)"],
    ["MESTRE DE OBRAS*",             "mês",  "34", "9.500", "10.000", "12.000", "8.000 (abaixo)"],
    ["Engenheiro Civil *",           "mês",  "40", "5.650", "6.900",  "12.000", "10.500 (ok)"],
    ["Engenheiro - PJ",              "mês",  "23", "5.000", "8.750",  "12.000", "10.500 (ok)"],
    ["Locação Elevador Cremalheira", "mês",  "30", "7.500", "9.000",  "15.000", "parte dos 480k"],
    ["Locação mini-grua",            "mês",  "14", "7.500", "7.750",  "12.000", "parte dos 480k"],
    ["Operador de Grua",             "mês",  "9",  "15.600","15.600", "15.600", "não itemizado"],
    ["Projeto arquitetônico",        "m²",   "9",  "9,96",  "10,50",  "30.000*","160/m² no vb"],
  ]
));
children.push(P([new TextRun({ text: "* Cluster com contaminação de unidade (m² vs vb) — usar com cautela.", italics: true, size: 18 })]));

// 4. ITENS SUSPEITOS
children.push(H1("4. Itens suspeitos — análise"));

children.push(H3("4.1 Taxas e seguros: R$ 380.000 (2,13% do total) — ALTO"));
children.push(P([
  new TextRun({ text: "Base: ", bold: true }),
  new TextRun("taxas_licencas_pct_total (n=17) — mediana 0,54%, P75 1,13%, P90 3,43%. Em R$ 17,87M: mediana = R$ 96k, P75 = R$ 202k, P90 = R$ 613k.")
]));
children.push(P([
  new TextRun({ text: "Placon R$ 380k = 2,13%, entre P75 e P90. ", bold: true }),
  new TextRun("Em Florianópolis centro faz sentido ser mais alto (habite-se, bombeiros, CRF, incorporação com patrimônio de afetação, alvará). Em uma incorporação pesada com SPE, essa linha inclui também seguro de performance e seguro garantia, que elevam.")
]));
children.push(P([
  new TextRun({ text: "Recomendação: ", bold: true, color: "C00000" }),
  new TextRun("segregar em R$ 180k taxas + R$ 100k seguros = "),
  new TextRun({ text: "R$ 280k ", bold: true }),
  new TextRun("(1,57%, próximo P75). "),
  new TextRun({ text: "Ajuste: -R$ 100k.", bold: true })
]));

children.push(H3("4.2 Equipamentos grua + cremalheira: R$ 480.000 — LIMITE SUPERIOR"));
children.push(P([
  new TextRun({ text: "Contexto do Placon: ", bold: true }),
  new TextRun("18 pavimentos, 15 pav tipo, altura ≈ 50m. Esse porte exige grua-torre operada + elevador cremalheira.")
]));
children.push(P([
  new TextRun({ text: "Base: ", bold: true }),
  new TextRun("Locação cremalheira mediana R$ 9k/mês (n=30); mini-grua mediana R$ 7,75k/mês (n=14); operador de grua R$ 15,6k/mês (n=9). Assumindo 14 meses de estrutura + 4 meses finalização da cremalheira (18m total):")
]));
children.push(bullet("Grua torre (operada, com operador): R$ 25.000/mês × 14 meses = R$ 350k"));
children.push(bullet("Cremalheira: R$ 9.000/mês × 18 meses = R$ 162k"));
children.push(bullet("Mob+desmob grua+cremalheira: R$ 40k"));
children.push(bullet("Subtotal 'correto': R$ 552k — Placon R$ 480k está DENTRO e até um pouco abaixo do esperado pra obra de 50m. Defensável."));
children.push(P([
  new TextRun({ text: "Porém ", bold: true }),
  new TextRun("se o planejamento usar mini-grua em vez de grua-torre (obra 4.077m² com laje protendida aceita), substitui R$ 350k por R$ 140k (R$ 7,75k × 18m) = "),
  new TextRun({ text: "-R$ 210k potenciais.", bold: true, color: "C00000" }),
  new TextRun(" Decisão do planejador.")
]));
children.push(P([
  new TextRun({ text: "Recomendação: ", bold: true, color: "C00000" }),
  new TextRun("validar com planejamento. Se mini-grua ok → "),
  new TextRun({ text: "R$ 300k ", bold: true }),
  new TextRun("(abatimento R$ 180k). Se grua-torre for necessária, manter R$ 480k e só ajustar com cotação real.")
]));

children.push(H3("4.3 Limpeza obra 2× R$ 2.500 × 24 meses = R$ 120.000"));
children.push(P([
  new TextRun({ text: "Premissa Placon: ", bold: true }),
  new TextRun("2 ajudantes de limpeza × 24 meses. Obra de 4.077m² AC, ritmo de ~170m²/mês, com 1 mestre + 1 encarregado + 1 almoxarife. ")
]));
children.push(P([
  new TextRun({ text: "Prática típica: ", bold: true }),
  new TextRun("1 ajudante até fase de acabamento (últimos 8-10 meses de obra), depois 2 nas duas últimas fases de limpeza fina (entrega). Média ponderada: ~1,3 ajudante × 24m × R$ 2,5k = R$ 78k.")
]));
children.push(P([
  new TextRun({ text: "Recomendação: ", bold: true, color: "C00000" }),
  new TextRun("ajustar de 2x para 1x contínuo + 2× nos últimos 6 meses = "),
  new TextRun({ text: "R$ 90k (ajuste -R$ 30k).", bold: true })
]));

children.push(H3("4.4 Projetos R$ 650k (3,64% do total) — ACIMA MEDIANA"));
children.push(P([
  new TextRun({ text: "Base: ", bold: true }),
  new TextRun("projetos_consultorias_pct_total (n=27) — mediana 2,44%, P75 12,07%, P90 16,05%. A mediana em R$ 17,87M = R$ 436k; P75 = R$ 2,16M. Placon R$ 650k + consultorias R$ 180k = R$ 830k (4,64%) — acima mediana mas bem abaixo P75.")
]));
children.push(P([
  new TextRun({ text: "Contexto: ", bold: true }),
  new TextRun("18 pav com cremalheira+grua exige complementares completos (estrutural protendido, hidro/sanitário, elétrico, incêndio, gás, cabeamento, ATP, BIM, compatibilização). R$ 159/m² pra projetos é razoável para médio-alto em SC. "),
  new TextRun({ text: "Manter.", bold: true })
]));

// 5. RECOMENDAÇÕES
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("5. Recomendações consolidadas"));

children.push(H2("5.1 Overrides sugeridos"));
const bgsRow = [
  [null, null, redBg, null, null],
  [null, null, redBg, null, null],
  [null, null, redBg, null, null],
  [null, null, greenBg, greenBg, greenBg]
];
children.push(table(
  ["Item", "Valor atual", "Valor proposto", "Impacto (R$)", "Justificativa"],
  [2200, 1300, 1300, 1200, 3000],
  [
    ["Taxas e seguros",        "380.000", "280.000", "-100.000", "Entre P75 e P90; segregar seguros"],
    ["Equipamentos grua+crem", "480.000", "300.000", "-180.000", "Se mini-grua viável (validar plan.)"],
    ["Limpeza obra",           "120.000", "90.000",  "-30.000",  "1 ajudante + reforço fim"],
    ["TOTAL AJUSTE",           "—",       "—",       "-310.000", "≈ 1,7 p.p. do Grand Total"]
  ],
  bgsRow
));

children.push(H2("5.2 Gerenciamento-alvo"));
children.push(table(
  ["Cenário", "Total (R$)", "R$/m²", "% Grand Total", "Posição base"],
  [2400, 1400, 1200, 1600, 2600],
  [
    ["Atual (overrides 22/04)",         "3.483.840", "854,45", "19,50%", "P85 geral / P65 médio-alto"],
    ["Conservador (só taxas+limpeza)",  "3.353.840", "822,57", "18,99%", "Idem, pouco abaixo"],
    ["Proposto (3 itens ajustados)",    "3.173.840", "778,43", "17,96%", "≈ P60 geral / P55 médio-alto"],
    ["Agressivo (mini-grua validada)",  "3.093.840", "758,81", "17,70%", "≈ P55 geral"]
  ]
));
children.push(P([
  new TextRun({ text: "Alvo recomendado: R$ 3,17M (R$ 778/m², 17,96% do total). ", bold: true, color: "00703C" }),
  new TextRun("Mantém segurança (não corta nenhum item estrutural), alinha com P60 da base e com o P25 do nicho médio-alto (R$ 339/m² é piso, muita obra pequena).")
]));

children.push(H2("5.3 Impacto no Grand Total"));
children.push(table(
  ["Métrica", "Antes", "Depois", "Delta"],
  [3200, 2200, 2200, 1800],
  [
    ["Gerenciamento",     "R$ 3.483.840", "R$ 3.173.840", "-R$ 310.000"],
    ["Grand Total obra",  "R$ 17.870.000","R$ 17.560.000","-R$ 310.000"],
    ["R$/m² total",       "R$ 4.383",     "R$ 4.307",     "-R$ 76"],
    ["% Gerenciamento",   "19,50%",       "18,07%",       "-1,43 p.p."]
  ]
));

// 6. APÊNDICE
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("6. Apêndice — Queries SQL & fontes"));

children.push(H2("6.1 Fontes consultadas"));
children.push(bullet("Supabase indices-cartesian: calibracao_global (18 rows, 1 p/ macrogrupo)"));
children.push(bullet("Supabase indices-cartesian: calibracao_condicional (64 rows, 4 padrões × 16 macrogrupos)"));
children.push(bullet("Supabase indices-cartesian: indices_estruturais (23 rows; categoria 'Custos Indiretos %' = 6 itens)"));
children.push(bullet("Supabase indices-cartesian: pus_cross_v2 (4.210 clusters semânticos)"));
children.push(bullet("Supabase indices-cartesian: indices_derivados_v2 (29 rows; ci_total_rsm2 n=55)"));
children.push(bullet("Supabase indices-cartesian: projetos (126 rows; 60 médio-alto, 57 alto, 4 médio, 4 econômico)"));
children.push(bullet("Local: base/indices-derivados-v2.json, base/base-indices-master-2026-04-13.json, base/itens-pus-agregados.json"));
children.push(bullet("Local: parametrico-placon-arminio-tavares.xlsx (abas Gerenciamento, BRIEFING, DADOS_PROJETO, CUSTOS_MACROGRUPO)"));

children.push(H2("6.2 Queries-chave"));
children.push(P([new TextRun({ text: "-- Distribuição Gerenciamento (geral)", bold: true, font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "SELECT n, p10, p25, mediana, p75, p90, max_val FROM calibracao_global WHERE macrogrupo='Gerenciamento' AND unidade='R$/m²';", font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "-- Condicional por padrão", bold: true, font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "SELECT padrao, n, p25, mediana, p75 FROM calibracao_condicional WHERE macrogrupo='Gerenciamento' AND unidade='R$/m²';", font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "-- Projetos pareados", bold: true, font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "SELECT slug, ac_m2, total_rs, rsm2 FROM projetos WHERE padrao_gemma='medio-alto' AND ac_m2 BETWEEN 3000 AND 6000 AND total_rs>0 ORDER BY rsm2;", font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "-- Indicadores indiretos % total", bold: true, font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "SELECT nome, n, p25, mediana, p75, p90 FROM indices_estruturais WHERE categoria='Custos Indiretos %';", font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "-- PUs de gerenciamento", bold: true, font: "Consolas", size: 18 })]));
children.push(P([new TextRun({ text: "SELECT descricao, unidades, n_proj, pu_p25, pu_mediana, pu_p75 FROM pus_cross_v2 WHERE descricao ILIKE '%grua%' OR descricao ILIKE '%mestre%' OR descricao ILIKE '%engenheiro%';", font: "Consolas", size: 18 })]));

children.push(H2("6.3 Limitações"));
children.push(bullet("UR=0 na maioria dos projetos comparados — mapeamento não populado; filtro de UR fica por conta da semelhança de AC."));
children.push(bullet("Cauda pesada em calibracao_condicional médio-alto (máx R$ 22k/m²) indica projetos tiny classificados errado; percentis (mediana, P25, P75) não são afetados."));
children.push(bullet("cross_insights_gemma tem pouca cobertura de gerenciamento: apenas labels semânticos, sem decomposição quantitativa item-a-item."));
children.push(bullet("Equipamentos (grua/cremalheira): decisão mini-grua vs torre precisa vir do planejamento, não do paramétrico."));
children.push(bullet("Premissa de R$ 17,87M do Grand Total usada é aproximação (valor informado no briefing do Leo); ao recalcular planilha, atualizar % total reais."));

// DOC
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Arial", color: "1F3864" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "2F5496" },
        paragraph: { spacing: { before: 240, after: 140 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Arial", color: "404040" },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Cartesian Engenharia — Análise Gerenciamento Placon — 2026-04-22", size: 18, color: "808080" })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Página ", size: 18, color: "808080" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "808080" }),
            new TextRun({ text: " — Fonte: Supabase indices-cartesian (126 projetos)", size: 18, color: "808080" })
          ]
        })]
      })
    },
    children
  }]
});

const outPath = path.resolve(__dirname, 'analise-gerenciamento-placon.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outPath, buf);
  console.log('OK:', outPath, '(' + buf.length + ' bytes)');
});
