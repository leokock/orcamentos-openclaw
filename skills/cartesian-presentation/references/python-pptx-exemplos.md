# Python-PPTX — Funções e Exemplos

## Setup Inicial

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Cm
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(16)   # Widescreen 16:9
prs.slide_height = Inches(9)

# Cores Cartesian
AZUL_PRIMARIO = RGBColor(47, 84, 235)
AZUL_ESCURO = RGBColor(15, 23, 42)
ROXO_AMPLI = RGBColor(147, 51, 234)
VERMELHO_LARANJA = RGBColor(255, 51, 0)
BRANCO = RGBColor(255, 255, 255)
CINZA_MEDIO = RGBColor(148, 163, 184)
```

## Funções de Criação

### Slide de Capa

```python
def criar_capa(prs, titulo, subtitulo):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(240, 245, 255)
    
    # Logo (se tiver arquivo)
    # slide.shapes.add_picture('logo_cartesian.png', Inches(0.5), Inches(0.5), height=Inches(1))
    
    titulo_box = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(14), Inches(2))
    titulo_frame = titulo_box.text_frame
    titulo_frame.text = titulo
    titulo_p = titulo_frame.paragraphs[0]
    titulo_p.font.size = Pt(60)
    titulo_p.font.bold = True
    titulo_p.font.color.rgb = AZUL_ESCURO
    titulo_p.alignment = PP_ALIGN.CENTER
    
    subtitulo_box = slide.shapes.add_textbox(Inches(1), Inches(5.5), Inches(14), Inches(1))
    subtitulo_frame = subtitulo_box.text_frame
    subtitulo_frame.text = subtitulo
    subtitulo_p = subtitulo_frame.paragraphs[0]
    subtitulo_p.font.size = Pt(24)
    subtitulo_p.font.color.rgb = AZUL_PRIMARIO
    subtitulo_p.alignment = PP_ALIGN.CENTER
    
    return slide
```

### Slide de Conteúdo com Bullets

```python
def criar_slide_conteudo(prs, titulo, bullet_points):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    titulo_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(14), Inches(1))
    titulo_frame = titulo_box.text_frame
    titulo_frame.text = titulo
    titulo_p = titulo_frame.paragraphs[0]
    titulo_p.font.size = Pt(40)
    titulo_p.font.bold = True
    titulo_p.font.color.rgb = AZUL_ESCURO
    
    conteudo_box = slide.shapes.add_textbox(Inches(1.5), Inches(2), Inches(13), Inches(6))
    text_frame = conteudo_box.text_frame
    
    for ponto in bullet_points:
        p = text_frame.add_paragraph()
        p.text = ponto
        p.level = 0
        p.font.size = Pt(16)
        p.font.color.rgb = AZUL_ESCURO
        p.space_before = Pt(12)
    
    return slide
```

### Slide com Cards de Números (KPIs)

```python
def criar_slide_numeros(prs, titulo, cards_data):
    """
    cards_data = [
        {'numero': '+4.000.000', 'descricao': 'M² CONSTRUÍDOS\nVIRTUALMENTE'},
        {'numero': '+260', 'descricao': 'EMPREENDIMENTOS'},
    ]
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    titulo_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(14), Inches(1))
    titulo_frame = titulo_box.text_frame
    titulo_frame.text = titulo
    titulo_p = titulo_frame.paragraphs[0]
    titulo_p.font.size = Pt(40)
    titulo_p.font.bold = True
    titulo_p.font.color.rgb = AZUL_ESCURO
    
    num_cards = len(cards_data)
    cards_por_linha = 3
    card_width = Inches(4)
    card_height = Inches(2.5)
    spacing = Inches(0.5)
    start_x = Inches(1)
    start_y = Inches(2.5)
    
    for idx, card_info in enumerate(cards_data):
        row = idx // cards_por_linha
        col = idx % cards_por_linha
        x = start_x + col * (card_width + spacing)
        y = start_y + row * (card_height + spacing)
        
        card = slide.shapes.add_shape(1, x, y, card_width, card_height)
        card.fill.solid()
        card.fill.fore_color.rgb = AZUL_PRIMARIO
        card.line.color.rgb = AZUL_PRIMARIO
        
        numero_box = slide.shapes.add_textbox(x, y + Inches(0.3), card_width, Inches(1.2))
        numero_frame = numero_box.text_frame
        numero_frame.text = card_info['numero']
        numero_p = numero_frame.paragraphs[0]
        numero_p.font.size = Pt(48)
        numero_p.font.bold = True
        numero_p.font.color.rgb = BRANCO
        numero_p.alignment = PP_ALIGN.CENTER
        
        desc_box = slide.shapes.add_textbox(x, y + Inches(1.6), card_width, Inches(0.8))
        desc_frame = desc_box.text_frame
        desc_frame.text = card_info['descricao']
        desc_p = desc_frame.paragraphs[0]
        desc_p.font.size = Pt(12)
        desc_p.font.color.rgb = BRANCO
        desc_p.alignment = PP_ALIGN.CENTER
    
    return slide
```

### Slide de Timeline/Processo

```python
def criar_slide_timeline(prs, titulo, fases):
    """
    fases = [
        {'nome': 'PRÉ-OBRA', 'itens': ['Gestão de Projetos BIM', 'Gestão de Custos']},
        {'nome': 'OBRA', 'itens': ['Monitoramento e Controle']},
    ]
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    titulo_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(14), Inches(1))
    titulo_frame = titulo_box.text_frame
    titulo_frame.text = titulo
    titulo_p = titulo_frame.paragraphs[0]
    titulo_p.font.size = Pt(40)
    titulo_p.font.bold = True
    titulo_p.font.color.rgb = AZUL_ESCURO
    
    linha_y = Inches(3)
    linha_inicio = Inches(2)
    linha_comprimento = Inches(12)
    
    connector = slide.shapes.add_connector(1, linha_inicio, linha_y, linha_inicio + linha_comprimento, linha_y)
    connector.line.color.rgb = AZUL_PRIMARIO
    connector.line.width = Pt(3)
    
    num_fases = len(fases)
    fase_width = linha_comprimento / num_fases
    
    for idx, fase in enumerate(fases):
        x = linha_inicio + (idx * fase_width)
        
        fase_box = slide.shapes.add_textbox(x, linha_y - Inches(0.8), fase_width, Inches(0.6))
        fase_frame = fase_box.text_frame
        fase_frame.text = fase['nome']
        fase_p = fase_frame.paragraphs[0]
        fase_p.font.size = Pt(18)
        fase_p.font.bold = True
        fase_p.font.color.rgb = AZUL_PRIMARIO if idx == 0 else RGBColor(255, 128, 0)
        fase_p.alignment = PP_ALIGN.CENTER
        
        itens_y = linha_y + Inches(0.5)
        for item in fase['itens']:
            item_box = slide.shapes.add_textbox(x, itens_y, fase_width, Inches(0.4))
            item_frame = item_box.text_frame
            item_frame.text = f"• {item}"
            item_p = item_frame.paragraphs[0]
            item_p.font.size = Pt(14)
            item_p.font.color.rgb = AZUL_ESCURO
            itens_y += Inches(0.5)
    
    return slide
```

### Slide de Contato

```python
def criar_slide_contato(prs, nome, cargo, telefone, email, endereco):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    nome_box = slide.shapes.add_textbox(Inches(6), Inches(3), Inches(10), Inches(0.8))
    nome_frame = nome_box.text_frame
    nome_frame.text = nome
    nome_p = nome_frame.paragraphs[0]
    nome_p.font.size = Pt(36)
    nome_p.font.bold = True
    nome_p.font.color.rgb = AZUL_PRIMARIO
    
    cargo_box = slide.shapes.add_textbox(Inches(6), Inches(3.9), Inches(10), Inches(0.5))
    cargo_frame = cargo_box.text_frame
    cargo_frame.text = cargo
    cargo_p = cargo_frame.paragraphs[0]
    cargo_p.font.size = Pt(18)
    cargo_p.font.color.rgb = AZUL_ESCURO
    
    tel_box = slide.shapes.add_textbox(Inches(6), Inches(4.7), Inches(10), Inches(0.4))
    tel_frame = tel_box.text_frame
    tel_frame.text = telefone
    tel_p = tel_frame.paragraphs[0]
    tel_p.font.size = Pt(16)
    tel_p.font.color.rgb = AZUL_ESCURO
    
    email_box = slide.shapes.add_textbox(Inches(6), Inches(5.2), Inches(10), Inches(0.4))
    email_frame = email_box.text_frame
    email_frame.text = email
    email_p = email_frame.paragraphs[0]
    email_p.font.size = Pt(16)
    email_p.font.color.rgb = AZUL_PRIMARIO
    
    end_box = slide.shapes.add_textbox(Inches(1), Inches(7.8), Inches(14), Inches(0.8))
    end_frame = end_box.text_frame
    end_frame.text = endereco + "\ncontato@cartesianengenharia.com"
    for p in end_frame.paragraphs:
        p.font.size = Pt(12)
        p.font.color.rgb = CINZA_MEDIO
        p.alignment = PP_ALIGN.CENTER
    
    return slide
```

---

## Exemplo Completo — Apresentação Comercial

```python
prs = Presentation()
prs.slide_width = Inches(16)
prs.slide_height = Inches(9)

criar_capa(prs, "Cartesian Engenharia", "Engenharia que apoia a gestão de obra")

criar_slide_numeros(prs, "QUEM SOMOS", [
    {'numero': '+4.000.000 m²', 'descricao': 'CONSTRUÍDOS\nVIRTUALMENTE'},
    {'numero': '+260', 'descricao': 'EMPREENDIMENTOS'},
    {'numero': '+135', 'descricao': 'CLIENTES'},
    {'numero': '11 + DF', 'descricao': 'ESTADOS'},
    {'numero': '+30', 'descricao': 'COLABORADORES'},
])

criar_slide_timeline(prs, "SOLUÇÕES INTEGRADAS", [
    {'nome': 'PRÉ-OBRA', 'itens': ['Gestão de Projetos BIM', 'Gestão de Custos', 'Gestão de Tempo']},
    {'nome': 'OBRA', 'itens': ['Monitoramento e Controle']},
])

criar_slide_contato(prs, "Leonardo Kock", "Sócio Diretor Comercial e Inovação",
    "(47) 9 9245-6794", "leonardo@cartesianengenharia.com",
    "Rua Dr. Pedro Ferreira, n° 333, sala 2002 - box 36, Centro, Itajaí/SC - CEP 88.301-030")

prs.save('apresentacao_cartesian.pptx')
```

---

## Atalhos Úteis

```python
# Forma com bordas arredondadas
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)

# Imagem (height proporcional)
slide.shapes.add_picture('imagem.png', left, top, width=Inches(5))

# Tabela
table = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Hyperlink
run = paragraph.runs[0]
run.hyperlink.address = 'https://www.cartesianengenharia.com'

# Converter pixels para inches (96 DPI)
def px_to_inches(px): return px / 96
```

---

## Troubleshooting

- **Fonte não aparece:** Verificar se instalada no sistema. Fallback: Arial, Calibri
- **Imagens distorcidas:** Especificar só width OU height (não ambos)
- **Textos cortados:** Aumentar text box ou reduzir fonte
- **Cores erradas:** Usar RGBColor exato, não nomes
