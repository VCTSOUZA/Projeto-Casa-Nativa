# Casa Nativa — Design System e Arquitetura Visual (Fase 02)

## 1. Princípios visuais

Casa Nativa é **natural, acolhedora, elegante e contemporânea**. A interface deve ter ritmo editorial, espaço negativo generoso e detalhes discretos. A sensação pretendida é: *“Entre, fique à vontade.”*

Evitar visual de vitrine agressiva, luxo distante, rusticidade genérica, dashboards e excesso de ornamentos. A cor terracota é um acento, não uma segunda cor de interface concorrente.

## 2. Paleta e tokens de cor

| Token | Nome | HEX | Função |
| --- | --- | --- | --- |
| `--color-primary` | Verde sálvia profundo | `#526A52` | CTA primário, links e identidade |
| `--color-primary-hover` | Verde sálvia intenso | `#405641` | Hover e estado ativo do primário |
| `--color-primary-dark` | Verde floresta | `#334535` | Texto sobre fundo claro e áreas escuras |
| `--color-secondary` | Terracota | `#A34F38` | Acentos, badges e detalhes pontuais |
| `--color-secondary-hover` | Terracota profundo | `#853C2B` | Hover de elementos secundários |
| `--color-background` | Creme | `#FAF7F0` | Fundo principal |
| `--color-background-secondary` | Bege areia | `#EFE8DC` | Blocos alternados e áreas de respiro |
| `--color-surface` | Marfim claro | `#FFFDF8` | Cards e superfícies elevadas |
| `--color-text-primary` | Verde carvão | `#243028` | Títulos e texto principal |
| `--color-text-secondary` | Verde acinzentado | `#4E5A51` | Texto auxiliar legível |
| `--color-text-muted` | Taupe profundo | `#6E7068` | Legendas e metadados não essenciais |
| `--color-border` | Areia sombreada | `#D5CDBF` | Divisórias e contornos discretos |
| `--color-success` | Verde folha | `#2F6B4F` | Estados de sucesso futuros |
| `--color-error` | Argila escura | `#A33D35` | Erros e alertas futuros |
| `--color-focus` | Mel dourado | `#B8792E` | Anel visível de foco |

### Contraste e aplicação

- `--color-text-primary` em `--color-background` é o padrão para conteúdo longo.
- Texto branco só deve ser usado sobre `--color-primary`, `--color-primary-dark`, `--color-secondary`, `--color-success` ou `--color-error`.
- Não usar `--color-text-muted` para texto essencial ou controles; ele é reservado a informações suplementares.
- Combinações de texto e fundo devem ser validadas antes da implementação para atender WCAG 2.2 AA: contraste mínimo 4.5:1 para texto normal e 3:1 para texto grande ou componentes de interface.

```css
:root {
  --color-primary: #526A52;
  --color-primary-hover: #405641;
  --color-primary-dark: #334535;
  --color-secondary: #A34F38;
  --color-secondary-hover: #853C2B;
  --color-background: #FAF7F0;
  --color-background-secondary: #EFE8DC;
  --color-surface: #FFFDF8;
  --color-text-primary: #243028;
  --color-text-secondary: #4E5A51;
  --color-text-muted: #6E7068;
  --color-border: #D5CDBF;
  --color-success: #2F6B4F;
  --color-error: #A33D35;
  --color-focus: #B8792E;
}
```

## 3. Tipografia

- **Display e títulos:** `Fraunces`, `Georgia`, serif. Pesos 500 e 600; uso editorial, com parcimônia.
- **Texto e interface:** `Manrope`, `Arial`, sans-serif. Pesos 400, 500, 600 e 700; uso em navegação, corpo e controles.

Na implementação, preferir hospedar os arquivos de fonte no projeto. Se a aprovação permitir Google Fonts, carregar somente os pesos usados, com `font-display: swap`, `preconnect` e fallback local. Não adicionar scripts de terceiros para fontes.

| Estilo | Família / peso | Tamanho | Line-height | Letter-spacing |
| --- | --- | --- | --- | --- |
| Display | Fraunces 500 | `clamp(2.75rem, 6vw, 5.5rem)` | 1.02 | `-0.03em` |
| H1 | Fraunces 500 | `clamp(2.25rem, 4.5vw, 4rem)` | 1.08 | `-0.025em` |
| H2 | Fraunces 500 | `clamp(1.875rem, 3vw, 3rem)` | 1.12 | `-0.02em` |
| H3 | Fraunces 600 | `clamp(1.5rem, 2vw, 2rem)` | 1.2 | `-0.015em` |
| H4 | Manrope 700 | `1.125rem` | 1.35 | `0` |
| Body large | Manrope 400 | `1.125rem` | 1.65 | `0` |
| Body | Manrope 400 | `1rem` | 1.6 | `0` |
| Body small | Manrope 400 | `0.875rem` | 1.55 | `0` |
| Caption | Manrope 600 | `0.75rem` | 1.4 | `0.04em` |
| Button | Manrope 700 | `0.875rem` | 1 | `0.02em` |

```css
:root {
  --font-display: "Fraunces", Georgia, serif;
  --font-body: "Manrope", Arial, sans-serif;
}
```

## 4. Espaçamento, contêiner e layout

A escala usa incrementos previsíveis de 4 px. Nenhuma margem arbitrária deve ser introduzida fora desta escala.

```css
:root {
  --space-2xs: 0.25rem; /* 4px */
  --space-xs: 0.5rem;   /* 8px */
  --space-sm: 0.75rem;  /* 12px */
  --space-md: 1rem;     /* 16px */
  --space-lg: 1.5rem;   /* 24px */
  --space-xl: 2rem;     /* 32px */
  --space-2xl: 3rem;    /* 48px */
  --space-3xl: 4.5rem;  /* 72px */
  --space-4xl: 6rem;    /* 96px */
  --container-max: 75rem;
  --gutter: clamp(1.25rem, 4vw, 3rem);
}
```

- Contêiner: `max-width: var(--container-max)`, centralizado, com `padding-inline: var(--gutter)`.
- Seções: `padding-block: clamp(4rem, 9vw, 7.5rem)`; hero pode chegar a `clamp(5rem, 10vw, 9rem)`.
- Cabeçalho de seção: título e descrição separados por `--space-md`; grade começa após `--space-2xl`.
- Gaps de cards: `--space-md` em mobile e `--space-lg` em tablet/desktop.
- O texto corrido deve ter largura máxima de 65–70 caracteres.

## 5. Radius, bordas e sombras

```css
:root {
  --radius-sm: 0.375rem;
  --radius-md: 0.75rem;
  --radius-lg: 1.25rem;
  --radius-pill: 999px;
  --shadow-sm: 0 1px 2px rgb(36 48 40 / 0.06);
  --shadow-md: 0 10px 30px rgb(36 48 40 / 0.08);
  --shadow-lg: 0 18px 45px rgb(36 48 40 / 0.12);
}
```

Cards editoriais priorizam borda sutil ou ausência de borda. Sombras só comunicam elevação e devem ser quase imperceptíveis; jamais usar sombra pesada em toda a página.

## 6. Responsividade (mobile first)

| Faixa | Largura | Uso planejado |
| --- | --- | --- |
| Base/mobile | `< 640px` | Uma coluna, navegação recolhida, alvos de toque ≥ 44×44 px |
| Tablet | `≥ 640px` | Grades podem ter duas colunas; hero começa a dividir conteúdo e mídia |
| Desktop | `≥ 1024px` | Navbar completa; coleções em quatro colunas; hero em duas colunas |
| Largo | `≥ 1280px` | Maior respiro, sem ultrapassar o contêiner de 1200 px |

- Não haverá rolagem horizontal.
- Imagens usarão `width: 100%`, `height: auto` ou `aspect-ratio` com `object-fit: cover`.
- Tipografia fluida deve usar `clamp()`; nenhum texto crítico deve depender apenas da largura de tela.

## 7. Componentes planejados

### Navbar

- Altura mínima: 72 px mobile, 80 px desktop; fundo creme ou superfície opaca.
- Estrutura: marca à esquerda, links **Coleções**, **Sobre**, **Contato**, e CTA à direita.
- Em mobile, links ficam em painel acionado por um `<button>` semântico com `aria-expanded` e rótulo acessível. Não usar ícone isolado como controle sem nome.
- Hover: cor primária e sublinhado discreto; ativo: sublinhado persistente.
- Ao rolar, aplicar fundo semitransparente apenas se a legibilidade for preservada; o comportamento deve ser opcional e feito com JavaScript mínimo.

### Buttons

Todos os botões terão altura mínima de 44 px, `border-radius: var(--radius-pill)`, `padding-inline: var(--space-lg)` e transição de até 180 ms.

| Variante | Visual | Estados |
| --- | --- | --- |
| Primário | Fundo `--color-primary`, texto branco | Hover verde intenso; active escurece; disabled com opacidade e cursor apropriado |
| Secundário | Fundo transparente, borda primária, texto verde | Hover com fundo verde muito sutil; mantém contraste |
| Texto | Sem caixa, texto primário ou verde com sublinhado | Hover reforça sublinhado; reservado a ações de baixa ênfase |

Foco para todos: `outline: 3px solid var(--color-focus)` com `outline-offset: 3px`. Nunca remover foco sem substituição equivalente.

### SectionHeader

Componente textual reutilizável: rótulo opcional em `Caption`, título H2 e descrição em `Body large`. Deve receber apenas um H2 por seção, seguindo a ordem semântica da página.

### CategoryCard

- Imagem 4:5, bordas `--radius-lg`, `object-fit: cover`.
- Título sobreposto em gradiente escuro leve ou abaixo da imagem; escolher a solução que mantenha contraste AA com a fotografia escolhida.
- Desktop: quatro cards; tablet: dois; mobile: uma coluna ou carrossel acessível somente se houver necessidade comprovada.
- Hover em dispositivos com ponteiro: escala máxima de imagem `1.03`; não deslocar layout.

### ProductCard

- Estrutura futura: imagem 1:1, categoria/caption, H3 com nome, preço, badge opcional e CTA textual.
- Sem borda pesada; superfície clara e espaçamento interno `--space-md`.
- Desktop: quatro colunas quando houver espaço; tablet: duas; mobile: duas compactas ou uma coluna, conforme legibilidade do nome e preço.

### Conteúdo editorial, essência e CTA

- Blocos textuais devem usar superfície, fundo bege ou verde profundo para quebrar a sequência de grades.
- Imagens editoriais podem usar proporção 4:5 ou 3:4; texto não deve ser sobreposto se a foto prejudicar o contraste.

### Footer

Fundo `--color-primary-dark`, texto branco/creme, `padding-block: --space-3xl`. Prevê marca, descrição breve, navegação, contato e redes sociais; dados inexistentes devem ser placeholders identificados e links não funcionais não devem ser publicados como reais.

## 8. Arquitetura da landing page

| Seção | Objetivo e conteúdo | Desktop | Mobile | Interações |
| --- | --- | --- | --- | --- |
| Navbar | Orientar e apresentar a marca | Linha única com CTA | Marca + acionador de menu | Hover/foco; menu acessível; fundo pode mudar no scroll |
| Hero | Comunicar a promessa: **“Um espaço que tem a sua essência.”**; subheadline, CTA “Conheça as coleções” e link secundário “Nossa história” | Duas colunas equilibradas, texto à esquerda e imagem 4:5 à direita | Texto primeiro; imagem abaixo; CTAs empilhados quando necessário | CTA e leve revelação apenas se não houver redução de movimento |
| Coleções | Apresentar Sala, Quarto, Cozinha e Decoração | Grade de quatro cards | Uma coluna ou duas, conforme largura | Hover de imagem, foco no link do card |
| Produtos em destaque | Título, breve descrição, grade e CTA “Ver coleções” | Quatro cards | Uma ou duas colunas legíveis | Estados de link/CTA; nenhum carrinho nesta fase |
| Nossa essência | Comunicar que a casa conta histórias, natureza e bem-estar | Composição assimétrica de mídia e texto, com espaço negativo | Mídia e texto em fluxo vertical | Sem interação obrigatória |
| CTA final | Converter de modo calmo: **“Encontre o que faz sua casa ser sua.”** | Bloco central generoso, contraste alto | Mesmo conteúdo e botão de largura adequada | Foco e estados de botão |
| Footer | Fechar navegação e dados institucionais | Colunas organizadas | Blocos empilhados | Links com foco e rótulo claro |

O `main` conterá as seções na ordem acima. Haverá somente um H1, no hero; os títulos de seção serão H2 e títulos de cards serão H3.

## 9. Direção fotográfica e tom

### Fotografia

Fotografias devem mostrar ambientes reais, luz natural suave, madeira, linho, cerâmica, fibras naturais e plantas. A prioridade é o produto contextualizado em uma casa possível, não o recorte de catálogo em fundo branco. Preferir tons quentes, baixa saturação e composição respirada. Evitar imagens artificiais, excessivamente saturadas, poluídas ou com texto embutido.

### Tom textual

Calmo, próximo, humano e preciso. Falar de viver o espaço e dos detalhes, não de urgência comercial. Evitar caixa alta, exclamações promocionais e promessas exageradas. CTAs preferidos: “Conheça as coleções”, “Descubra os detalhes”, “Ver peças em destaque”.

## 10. Microinterações e movimento

- Transições de cor, sombra e escala: 150–200 ms, `ease-out`.
- Hover de imagens: escala máxima 1.03, com `overflow: hidden` no contêiner.
- Não usar animações contínuas, parallax obrigatório ou movimentos que alterem o conteúdo durante leitura.
- Elementos que surgem na tela serão opcionais e não escondem conteúdo de leitores de tela.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 11. Acessibilidade obrigatória

- Validar contraste WCAG 2.2 AA antes de aprovar cada combinação de texto, estado e fotografia.
- Usar HTML semântico: `header`, `nav`, `main`, `section`, `footer`, listas e headings em sequência.
- Usar `<a>` para navegação e `<button>` para ações; não simular controles com `div` ou `span`.
- Garantir navegação completa por teclado, foco visível e ordem de foco lógica.
- Links e botões em mobile terão área mínima de 44×44 px.
- Imagens informativas terão `alt` descritivo e contextual; imagens decorativas terão `alt=""` e não repetirão conteúdo.
- O menu mobile informará estado com `aria-expanded`, controlará seu painel por ID e fechará com `Escape`.
- Respeitar `prefers-reduced-motion`; não depender de cor como único indicador de estado.

## 12. Performance e segurança da futura implementação

- Servir imagens em dimensões adequadas, preferencialmente AVIF/WebP com fallback quando necessário; definir `width` e `height` para reduzir layout shift.
- Usar `loading="lazy"` para imagens fora da dobra; a mídia principal do hero não deve ser lazy-loaded se for o LCP.
- Não carregar bibliotecas de UI, animação ou carrossel sem necessidade demonstrada.
- Manter CSS e JavaScript locais, organizados e mínimos; scripts externos exigem justificativa e revisão.
- Evitar JavaScript e estilos inline para preservar futura adoção de CSP. Usar os arquivos estáticos existentes.
- Não inserir dados de usuário com `innerHTML`; futuras entradas devem ser tratadas e escapadas no backend.

## 13. SEO inicial para a próxima fase

- Definir `<title>` descritivo por página e meta description concisa.
- Manter `lang="pt-BR"`, um único H1 e hierarquia de headings correta.
- Incluir favicon e URLs semânticas quando as novas páginas existirem.
- Adicionar Open Graph básico somente com imagem, URL e descrição reais e revisadas.
- Usar texto alternativo de qualidade e links com rótulo compreensível fora de contexto.
- Não usar texto relevante apenas dentro de imagens.

## 14. Plano de implementação da próxima fase

1. Integrar tokens deste documento no CSS global, sem incluir frameworks.
2. Atualizar `base.html` com metadados básicos, fontes aprovadas e estrutura semântica; manter CSS/JS externos.
3. Implementar a navbar e o hero em HTML acessível, começando pelo layout mobile.
4. Construir `SectionHeader`, botões, cards e as seções na ordem definida, reutilizando classes previsíveis.
5. Adicionar imagens somente após seleção conforme a direção fotográfica, otimizadas e com `alt` adequado.
6. Implementar menu mobile e microinterações com JavaScript vanilla mínimo.
7. Validar em 320 px, 640 px, 1024 px e 1280 px; testar teclado, contraste, redução de movimento e desempenho.

## 15. Decisões registradas

- A paleta usa verde sálvia profundo como cor funcional principal; terracota fica reservada a acentos para evitar uma aparência pesada.
- `Fraunces` e `Manrope` foram escolhidas pela combinação editorial e legível, com fallbacks de sistema e preferência futura por auto-hospedagem.
- O contêiner máximo de 1200 px preserva conforto de leitura e evita um layout excessivamente largo.
- O menu mobile será tratado como diálogo/painel de navegação acessível apenas na fase de implementação, quando sua estrutura HTML existir.

## 16. Fora do escopo desta fase

Este documento não implementa a landing page, imagens, modelos, banco de dados, autenticação, CRUD, carrinho, pagamentos, bibliotecas de interface, bibliotecas de animação ou novas dependências.
