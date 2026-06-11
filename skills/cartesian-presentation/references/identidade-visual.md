# Guia de Identidade Visual Cartesian
## Baseado no Manual de Marca Kugnharski Studio (Set/2021) — atualizado com Brand Guide V2

> **🎨 Padrão obrigatório** — sempre que produzir documento institucional Cartesian (ata, proposta, planilha, slide, dashboard, relatório, peça de marketing), aplicar esta paleta. Não inventar tons aproximados; usar os hex exatos abaixo.
>
> **Fonte oficial V2:** `Kg-Apresentação-CARTESIAN-V2.pdf` (156 páginas, distribuído internamente). Cópia local em `referencias/cartesian/branding/cartesian-brand-guide-v2.pdf` quando disponível.
>
> **Última atualização:** 13/05/2026 — paleta V2 oficial extraída direto do PDF (página 7 "PALETA DE CORES"). Substituiu valores aproximados que vinham do manual V1 de 2021.

---

## Paleta Oficial V2 (USAR ESTA)

Extraída direto dos retângulos da página 7 do brand guide V2 — são os valores RGB exatos que a Kugnharski Studio definiu.

| Cor | Hex | RGB | Uso |
|---|---|---|---|
| **Azul Cartesian** | `#245AE4` | (36, 90, 228) | Cor principal da marca — headers, títulos, destaques, fundos chamativos |
| **Laranja Cartesian** | `#FD3400` | (253, 52, 0) | Acentos, KPIs, alertas, CTAs |
| **Preto** | `#111111` | (17, 17, 17) | Texto principal, headers escuros |
| **Preto puro** | `#000000` | (0, 0, 0) | Quando precisa máximo contraste |
| **Cinza claro** | `#F4F4F4` | (244, 244, 244) | Fundos neutros, divisores |
| **Cinza médio** | `#E7E7E9` | (231, 231, 233) | Linhas sutis, bordas suaves |
| **Branco** | `#FFFFFF` | (255, 255, 255) | Texto sobre azul/preto, fundos limpos |

### Snippet Python (openpyxl/python-pptx/matplotlib)

```python
CORES_CARTESIAN_V2 = {
    'azul':         '245AE4',  # cor principal
    'laranja':      'FD3400',
    'preto':        '111111',
    'preto_puro':   '000000',
    'cinza_claro':  'F4F4F4',
    'cinza_medio':  'E7E7E9',
    'branco':       'FFFFFF',
}

# RGB tuple version
CORES_CARTESIAN_V2_RGB = {
    'azul':         (36, 90, 228),
    'laranja':      (253, 52, 0),
    'preto':        (17, 17, 17),
    'preto_puro':   (0, 0, 0),
    'cinza_claro':  (244, 244, 244),
    'cinza_medio':  (231, 231, 233),
    'branco':       (255, 255, 255),
}
```

### Exemplo de aplicação — tabela formal (atas, relatórios)

- Header da tabela: fundo `#245AE4` + texto branco bold
- Labels meta (REUNIÃO, OBRA, etc.): fundo `#245AE4` + texto branco bold
- Bordas das células: `#808080` finas
- Texto do corpo: `#111111` regular
- Fundo das linhas: branco

Veja referência prática em `~/clawd/clientes/thozen/atas/2026-04-30_entrega-parcial-orcamento.md` (ata Electra Towers, gerada 13/05/2026).

---

## Paleta V1 — Legado (NÃO USAR em documentos novos)

Mantida só pra rastreabilidade de documentos antigos. Valores estavam próximos da V2 mas não eram os hex exatos do brand guide.

```python
# DEPRECATED — use CORES_CARTESIAN_V2
CORES_PRIMARIAS_V1 = {
    'azul_primario':    '#2F54EB',  # V2 oficial: #245AE4
    'vermelho_laranja': '#FF3300',  # V2 oficial: #FD3400
    'preto':            '#231F20',  # V2 oficial: #111111
    'cinza_claro':      '#E6E6E6',  # V2 oficial: #E7E7E9
}
```

---

## Moodboard e Conceito

### Inspirações Visuais
- **Arquitetura moderna** — linhas limpas, vidro, geometria
- **Tecnologia** — grids, dados, conexões, redes
- **Precisão** — planos cartesianos, medidas exatas
- **Construção** — estruturas, camadas, sobreposições

### Palavras-Chave
Transparência, Agilidade, Tecnologia, Gestão, Modelagem, Construção, Precisão, Integração

### Valores da Marca
- Transparência & Agilidade
- Tecnologia & Gestão
- Modelagem & Construção

---

## Paleta de Cores

### Cores Primárias (Manual Original)

```python
CORES_PRIMARIAS = {
    'branco':           ((255, 255, 255), '#FFFFFF', 'Fundos, texto sobre escuro'),
    'cinza_claro':      ((230, 230, 230), '#E6E6E6', 'Fundos neutros'),           # Pantone Cool Gray 1C
    'preto':            ((35, 31, 32),    '#231F20', 'Texto principal'),            # Process Black
    'azul_primario':    ((47, 84, 235),   '#2F54EB', 'Cor principal da marca'),     # Pantone 2726C
    'vermelho_laranja': ((255, 51, 0),    '#FF3300', 'Destaques e acentos'),        # Pantone 172C
}
```

### Cores Expandidas (Apresentações Comerciais)

```python
CORES_EXPANDIDAS = {
    'azul_escuro':    ((15, 23, 42),    '#0F172A', 'Textos e fundos escuros'),
    'roxo_ampli':     ((147, 51, 234),  '#9333EA', 'Branding AMPLI'),
    'laranja_obra':   ((255, 128, 0),   '#FF8000', 'Fase OBRA em timelines'),
    'cinza_medio':    ((148, 163, 184), '#94A3B8', 'Textos secundários'),
    'amarelo':        ((255, 193, 7),   '#FFC107', 'Destaques pontuais'),
    'gradiente_claro_inicio': ((230, 240, 255), '#E6F0FF', 'Azul muito claro'),
    'gradiente_claro_fim':    ((255, 245, 255), '#FFF5FF', 'Roxo muito claro'),
}
```

### Combinações Recomendadas

**Apresentações Corporativas:**
- Fundo: Branco ou Cinza Claro
- Títulos: Preto ou Azul
- Destaques: Vermelho-Laranja
- Grafismo: Azul com 10-20% opacidade

**Apresentações de Impacto:**
- Fundo: Azul ou Preto
- Títulos: Branco
- Destaques: Vermelho-Laranja ou Roxo AMPLI
- Grafismo: Branco com 20-30% opacidade

**AMPLI (Plataforma):**
- Primária: Roxo `#9333EA`
- Secundária: Azul `#2F54EB`
- Fundo: Branco
- Grafismo: Roxo ou Azul com baixa opacidade

---

## Tipografia

### Poppins — Fonte Oficial

Família geométrica sans-serif (Indian Type Foundry). Moderna, geométrica, amigável.

**Pesos:**
- Thin (100), ExtraLight (200), Light (300), Regular (400), Medium (500)
- SemiBold (600), Bold (700), ExtraBold (800), Black (900)

**Hierarquia Tipográfica:**

| Nível | Peso | Tamanho | Cor | Tracking |
|-------|------|---------|-----|----------|
| Títulos capas | ExtraBold/Bold | 48-72pt | Azul/Preto/Branco | -2% a 0% |
| Títulos slides | Bold | 32-44pt | Azul/Preto | 0% |
| Subtítulos | SemiBold | 20-28pt | Azul/Preto/Cinza Médio | — |
| Corpo | Regular | 14-18pt | Preto/Cinza Escuro | line-height 1.5 |
| Legendas/notas | Regular/Light | 10-12pt | Cinza Médio | — |
| Números KPI | Bold/ExtraBold | 48-72pt | Azul/Vermelho-Laranja | — |

**Fontes Alternativas (quando Poppins não disponível):**
1. Montserrat (similaridade geométrica alta)
2. Gotham (alternativa profissional)
3. Proxima Nova (boa legibilidade)
4. Arial Rounded (fallback seguro)

---

## Elementos da Marca

### Símbolo
- **Forma:** Dois quadrados arredondados sobrepostos
- **Conceito:** Interseção = transparência e integração
- **Uso:** Sempre com logotipo, exceto em aplicações muito pequenas

### Logotipo
- Tipografia customizada baseada em Poppins
- Estilo geométrico, moderno, clean
- Letra 'a' minúsculo com design único

### Versões do Logo
1. Preto sobre branco (uso principal)
2. Branco sobre azul (fundos azuis)
3. Branco sobre preto (fundos escuros)
4. Azul sobre branco (variação digital)
5. Branco sobre vermelho-laranja (destaque)
6. Vermelho-laranja sobre branco (especial)

### Regras de Uso do Logo
- **Área de proteção:** altura do símbolo em todos os lados
- **Tamanho mínimo:** 15mm impresso / 120px digital
- **Abaixo do mínimo:** usar apenas símbolo sem logotipo
- **NÃO:** alterar proporções, rotacionar, mudar cores, adicionar efeitos, distorcer

---

## Grafismo 3D — Elemento Principal

Linhas de perspectiva 3D representando os eixos X, Y, Z do plano cartesiano.

**Variações:**
1. Linhas sólidas — aplicações com mais destaque
2. Linhas pontilhadas — fundos sutis
3. Grade completa — backgrounds complexos
4. Padrão radiante — linhas emanando do centro

**Cores do Grafismo:**
- Branco sobre azul (mais comum)
- Azul sobre branco
- Cinza claro sobre cinza escuro
- Vermelho-laranja sobre preto
- Sempre com opacidade ajustável (10-50%)

**Aplicações:** Fundos de slides, capas, envelopes, papelaria, cadernos, website, sinalização, material promocional.

---

## Imagens

- Fotos de obras/construção com filtro azulado quando apropriado
- Imagens de alta qualidade (mínimo 1920x1080 para fullscreen)
- Overlay escuro (60-80% opacidade) quando texto sobreposto
- Mockups de telas da plataforma AMPLI

### Mood Board — Elementos Aprovados
✅ Arquitetura moderna em vidro e concreto
✅ Linhas de construção e estruturas
✅ Grids e planos cartesianos
✅ Redes e conexões (tech)
✅ Padrões geométricos
✅ Fotografia arquitetônica clean

### Mood Board — Evitar
❌ Ilustrações muito coloridas/infantis
❌ Fotos de banco genéricas
❌ Gradientes excessivos
❌ Efeitos 3D artificial
❌ Texturas pesadas
❌ Fontes decorativas/script

---

## Tom de Voz

**Personalidade:** Profissional mas não distante. Técnica mas acessível. Inovadora mas confiável. Precisa mas humana.

**Mensagens-Chave:**
1. "Transformamos dados em decisões"
2. "Integramos todo o ciclo: da pré-obra à entrega"
3. "Engenharia com transparência e agilidade"
4. "BIM além da modelagem — gestão integrada"
5. "Não vendemos software, entregamos resultados"

---

## Checklist de Qualidade de Marca

- [ ] Logo na versão correta para o fundo
- [ ] Área de proteção do logo respeitada
- [ ] Cores da paleta oficial
- [ ] Tipografia Poppins (ou alternativa aprovada)
- [ ] Hierarquia tipográfica clara
- [ ] Grafismo 3D presente e bem aplicado
- [ ] Contraste garante legibilidade
- [ ] Mensagem alinhada com tom de voz
- [ ] Informações de contato corretas
