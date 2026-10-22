---
name: Editorial Precision
colors:
  surface: '#f9f9f7'
  surface-dim: '#dadad8'
  surface-bright: '#f9f9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f2'
  surface-container: '#eeeeec'
  surface-container-high: '#e8e8e6'
  surface-container-highest: '#e2e3e1'
  on-surface: '#1a1c1b'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#4b41e1'
  on-secondary: '#ffffff'
  secondary-container: '#645efb'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1b1c1c'
  on-tertiary-container: '#848484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e2dfff'
  secondary-fixed-dim: '#c3c0ff'
  on-secondary-fixed: '#0f0069'
  on-secondary-fixed-variant: '#3323cc'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#f9f9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e2e3e1'
typography:
  display:
    fontFamily: Geist
    fontSize: 4.5rem
    fontWeight: '600'
    lineHeight: 4.75rem
    letterSpacing: -0.04em
  display-mobile:
    fontFamily: Geist
    fontSize: 2.75rem
    fontWeight: '600'
    lineHeight: 3rem
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Geist
    fontSize: 3rem
    fontWeight: '500'
    lineHeight: 3.25rem
    letterSpacing: -0.03em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 2rem
    fontWeight: '500'
    lineHeight: 2.25rem
    letterSpacing: -0.025em
  headline-md:
    fontFamily: Geist
    fontSize: 2rem
    fontWeight: '500'
    lineHeight: 2.35rem
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Geist
    fontSize: 1.375rem
    fontWeight: '500'
    lineHeight: 1.75rem
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Geist
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.8rem
    letterSpacing: -0.01em
  body-md:
    fontFamily: Geist
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.6rem
    letterSpacing: -0.005em
  body-sm:
    fontFamily: Geist
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.45rem
    letterSpacing: 0em
  label-technical:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: 0.04em
  metric-display:
    fontFamily: Geist
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: 2.75rem
    letterSpacing: -0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-desktop: 2.5rem
  margin: 1.25rem
  margin-desktop: 3.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.75rem
  space-xl: 3rem
---

## Brand & Style

This design system reflects the convergence of rigorous analytical intelligence and disciplined Swiss graphic design. Built specifically for a senior data analyst portfolio, it eschews loud techno-futurist tropes, neon accents, and heavy decorative visual clutter. Instead, it embraces high-order compositional balance, absolute clarity, asymmetric rhythm, and editorial restraint.

The aesthetic fuses International Typographic Style (Swiss Grid) with modern digital product minimalism:
- **Tone & Atmosphere:** Calm, deliberate, hyper-competent, architectural. The interface recedes to let case studies, methodology, and empirical evidence command full attention.
- **Visual Mechanics:** Hairline horizontal rules, structured asymmetrical layout alignments, deliberate density shifts, monospaced metadata labels, and expansive, restful negative space.
- **Target Audience:** Engineering leads, executive stakeholders, data directors, and product teams seeking a candidate who values structured thinking, intellectual clarity, and precision execution over superficial aesthetics.

## Colors

The palette is rooted in print-inspired restraint, engineered to eliminate eye fatigue while maintaining strict semantic contrast.

- **Canvas & Surfaces:**
  - Base canvas is a warm, unbleached tactile off-white (`#F7F7F5`).
  - Elevated surfaces and cards use stark white (`#FFFFFF`) to introduce subtle, natural contrast against the warmer ground.
  - Subdued structural fills and code blocks use `#EFEFEA`.
- **Text & Structure:**
  - Primary text and structural grid lines leverage an uncompromising deep charcoal `#111111` for high-precision readability.
  - Secondary typography, supporting narratives, and metadata rely on balanced neutral gray `#6F6F6F`.
  - Grid borders, data table dividers, and hairline structural dividers use a crisp `#DCDCDC`.
- **Accent Application:**
  - Restrained accent indigo (`#4F46E5`) is deployed selectively: key interactive hover states, active metrics, primary action targets, and analytical highlights. It must never coat large background areas.

## Typography

The typographic hierarchy draws inspiration from classic Swiss poster design and modern engineering journals:

- **Primary Typeface (`Geist`):** Selected for its crisp geometric terminals, exact kerning, and neutral Swiss modernist voice. Used across all editorial headlines, subheadings, and running prose.
- **Technical Metadata Typeface (`JetBrains Mono`):** Applied exclusively to functional counters, dataset specs, publication dates, SQL/query snippets, category pills, and tabular indices.
- **Typographic Rules:**
  - Tight negative letter spacing is applied to large editorial headlines to create density and graphic authority.
  - Body copy maintains generous line height (1.6–1.8×) to facilitate long-form analytical study reading.
  - Numbers in data tables and metadata must always use tabular figures (`font-variant-numeric: tabular-nums`).

## Layout & Spacing

Layout in this system is driven by a rigid, Swiss-inspired 12-column structural grid system that enforces mathematical discipline and asymmetric editorial layouts.

- **Grid Architecture:**
  - **Desktop (>= 1024px):** 12-column layout with 40px gutters (`gutter-desktop`) and 56px margins (`margin-desktop`). Asymmetric compositions are encouraged (e.g., a 4-column sticky meta/index sidebar paired with an 8-column analytical deep-dive stream).
  - **Tablet (768px - 1023px):** 8-column layout with 24px gutters and 32px margins. Sidebars shift to top or modular block layouts.
  - **Mobile (< 768px):** 4-column layout with 16px gutters and 20px outer margin.
- **Rhythm & Cadence:**
  - Vertical spacing adheres to a strict 8px base rhythm.
  - Macro-spacing between project sections and editorial blocks uses `space-xl` (48px) and multi-tier multiples (e.g., 96px, 120px) to establish confident breathing room.
  - Hairline dividers (`1px solid #DCDCDC`) are actively integrated into the grid structure to delineate content boundaries without visual heaviness.

## Elevation & Depth

This design system deliberately rejects heavy skeuomorphism, ambient multi-layered drop shadows, and dramatic blurs. Depth is achieved via **tonal architecture and razor-sharp hairline separation**:

- **Surface Tiers:**
  - **Floor (Tier 0):** The foundational tactile background (`#F7F7F5`).
  - **Surface (Tier 1):** Clean canvas panels, data cards, and content blocks (`#FFFFFF`) framed with a subtle 1px border in `#DCDCDC`.
  - **Inset / Tooling (Tier 2):** Code windows, data query playgrounds, and metric tiles inset with `#EFEFEA` or framed with crisp borders.
- **Elevation Cues:**
  - Shadows are avoided in passive states.
  - **Interactive Hover:** Elements indicate affordance not through soft shadows, but through subtle outline darkening (`#111111`), crisp 1px offset shift, or high-contrast background inversion.
  - Floating items (e.g., sticky top index, floating modal data views) use a pure white surface with a singular crisp border (`1px solid #DCDCDC`) and a minimal, ultra-fine drop shadow: `0 4px 16px rgba(17, 17, 17, 0.04)`.

## Shapes

The design system enforces architectural sharpness with only the faintest softening to maintain technical warmth:

- Base corner radius is strictly `0.25rem` (4px).
- Internal containers, buttons, inputs, data cards, and preview frames all observe this compact radius.
- System tags, metadata counters, and code badges maintain this exact geometry to evoke stamped index cards and technical ledger entries.
- Pill buttons and deeply circular interfaces are forbidden, as they undermine the analytical, structured Swiss grid geometry.

## Components

### Buttons
- **Primary:** Deep charcoal background (`#111111`), white text (`#FFFFFF`), 4px border radius. Monospaced or sharp sans label with subtle horizontal padding (`1rem` vertical, `1.5rem` horizontal). On hover: transitions background to `#4F46E5`.
- **Secondary / Ghost:** Transparent background with a 1px border (`#DCDCDC`) and `#111111` text. On hover: border transitions to `#111111` with an interior fill of `#FFFFFF`.
- **Action Links:** Underlined baseline or monospaced string paired with an arrow glyph (`→`), transitioning color to `#4F46E5` on focus/hover.

### Data Cards & Case Study Teasers
- **Structure:** Solid `#FFFFFF` fill with a continuous `1px solid #DCDCDC` perimeter border and 4px radius.
- **Card Header:** Technical metadata lockup using `label-technical` (`#6F6F6F`) showcasing taxonomy, dataset size, or completion dates separated by hairline dividers.
- **Card Body:** Crisp headline in `Geist Medium`, followed by concise analytical findings.
- **Hover Behavior:** Border shifts from `#DCDCDC` to `#111111`. No dramatic vertical lifting; subtle cursor feedback and headline tint to `#4F46E5`.

### Metric Counters & Stat Tiles
- Compact grid modules displaying high-leverage business and analytical impact.
- Primary number rendered via `metric-display` in `#111111`.
- Secondary unit descriptor or delta indicator (e.g., `+34.2% YoY`) positioned directly beneath or inline using `JetBrains Mono` at `0.75rem`.

### Chips & Metadata Tags
- Minimalist indicators built with `JetBrains Mono` (0.75rem, uppercase or lowercase with tight leading).
- Flat styling: `#FFFFFF` or `#EFEFEA` background with a hairline border (`#DCDCDC`), `#111111` text, and zero ambient shadow. Padding is disciplined: `0.25rem` vertical by `0.5rem` horizontal.

### Lists & Case Indexes
- Designed like an indexical ledger. Rows separated by `1px solid #DCDCDC` border lines.
- Columns align strictly with the grid: `[01. Index]`, `[Client/Project]`, `[Domain/Stack]`, `[Year]`.
- Row hover triggers an immediate soft fill shift to `#FFFFFF` with typography darkening to `#111111`.

### Inputs & Search Fields
- Form inputs feature an unstyled or `#FFFFFF` fill with a 1px `#DCDCDC` boundary.
- Placeholder text in `#6F6F6F`.
- On focus: border sharply transitions to `1px solid #111111` with no glowing outer halos or blurry focus rings.

### Technical Data Tables & Code Snippets
- Zero zebra-striping by default; distinction is made entirely with alternating white/off-white blocks or 1px hairline horizontal grids.
- Headers are all-caps `label-technical` in `#6F6F6F`.
- Cells are right-aligned for quantitative metrics, left-aligned for qualitative dimensions.