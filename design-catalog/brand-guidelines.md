# Brand Guidelines: The Sisu Way

**Version:** 0.1, 2026-09-23. Proposal by Summit Software Solutions, pending Angus Peacock's approval.
**Live version:** [`specimen.html`](../specimen.html) renders every token, pair and component below.

## Principle

Unlike Roses or Meantime, The Sisu Way has no brand surfaces to measure yet. The name is new, thesisuway.com is not public, and the concept was built without access to the current app or the Wix site. So this system is **proposed, not extracted**. Every choice is argued from what is publicly known about the project, and every value is tested for contrast. When Angus supplies a logo, colors or type he already uses, those win, and this document gets revised.

What the brand has to carry, from public sources:

| Fact | Source |
|---|---|
| *Sisu* is the Finnish concept of stubborn resolve and resilience under adversity, the "second wind" | Common usage; Angus's book |
| Angus Peacock's book *SISU: A Series of Epic Adventures* (Tactical 16) is a true account crossing the French Alps, Moscow, Beijing and Mongolia by rail and on foot | Tactical 16, Amazon listing |
| Angus is a rugby coach and coach educator, Royal Navy veteran, life coach | Public coaching profiles, blackdragonenterprises.com |
| The Notion workspace is titled "🏉 SISU Way — Project Command Centre" | Notion share email, 2026-09-22 |
| Investors want the app on iOS and Android | Kincaid, 2026-09-23 |

**The idea: fire in the cold.** A northern landscape at dusk (snow, granite, deep fjord water) with one warm color that stands for the second wind. That warm color is spent only on the single action that matters on each screen.

## Color

### Tokens

```css
:root {
  /* Core */
  --snow:        #F4F2ED;  /* page field */
  --mist:        #DDE4E4;  /* tint sections, panels */
  --granite:     #1B1F23;  /* body text, headings on light */
  --fjord:       #1D4A5C;  /* the brand color: links, rules, secondary buttons */
  --fjord-deep:  #0F2B37;  /* dark sections, footer, concept bar */
  --aurora:      #E3A33B;  /* primary CTA fill, the mark's sun, labels on dark */
  /* Support */
  --aurora-deep: #8A5A0F;  /* aurora's text-safe form on light */
  --slate:       #56616B;  /* secondary text on snow and mist only */
}
```

### Roles

| Token | Use for | Never use for |
|---|---|---|
| `--snow` | Default page background, text on dark | Text on aurora |
| `--mist` | Alternate sections, store panel, muted text on dark | Text on snow (1.15:1) |
| `--granite` | All body text and headings on light, text on aurora buttons | Large fills (use fjord-deep) |
| `--fjord` | Links, secondary buttons, hairlines, the word "Sisu" in the wordmark | Text on fjord-deep |
| `--fjord-deep` | Hero, dark sections, footer, concept bar | Text anywhere |
| `--aurora` | Primary button fill, the sun, labels and accents on dark | Text on light backgrounds |
| `--aurora-deep` | Amber text on light: card numbers, placeholder notes | Large fills |
| `--slate` | Captions and secondary text on snow or mist | Anything on dark |

**Proportion.** Roughly 60% snow and mist, 30% fjord-deep and granite, under 10% aurora. If a screen has two aurora buttons, one of them is wrong.

### WCAG contrast, every pair in use

Computed to WCAG 2.1 relative luminance. AA needs 4.5:1 for normal text, 3:1 for large text (≥24px, or ≥18.66px bold).

| Text | Background | Ratio | AA | AAA |
|---|---|---|---|---|
| `--granite` | `--snow` | **14.82** | pass | pass |
| `--granite` | `--mist` | **12.86** | pass | pass |
| `--fjord` | `--snow` | **8.59** | pass | pass |
| `--fjord` | `--mist` | **7.45** | pass | pass |
| `--snow` | `--fjord` | **8.59** | pass | pass |
| `--snow` | `--fjord-deep` | **13.21** | pass | pass |
| `--mist` | `--fjord-deep` | **11.46** | pass | pass |
| `--aurora` | `--fjord-deep` | **6.73** | pass | — |
| `--granite` | `--aurora` | **7.55** | pass | pass |
| `--aurora-deep` | `--snow` | **5.29** | pass | — |
| `--aurora-deep` | `--mist` | **4.59** | pass | — |
| `--slate` | `--snow` | **5.66** | pass | — |
| `--slate` | `--mist` | **4.91** | pass | — |
| `--snow` | `--granite` | **14.82** | pass | pass |

### Forbidden pairs

| Text | Background | Ratio | Rule |
|---|---|---|---|
| `--snow` | `--aurora` | 1.96 | **Never.** Aurora buttons take granite text |
| `--aurora` | `--snow` | 1.96 | **Never as text.** Use `--aurora-deep` |
| `--aurora` | `--mist` | 1.70 | **Never as text** |
| `--fjord` | `--aurora` | 4.38 | Large text only. Avoid |
| `--slate` | `--fjord-deep` | 2.33 | **Never.** Muted text on dark uses `--mist` |
| `--fjord` | `--fjord-deep` | 1.54 | **Never as text** |

## Typography

```css
--font-display: "Barlow Condensed", "Arial Narrow", system-ui, sans-serif;  /* headings, labels, buttons, nav */
--font-body:    "Source Serif 4", Georgia, "Times New Roman", serif;          /* everything you read slowly */
```

**Why.** Condensed uppercase reads like trail signage and team kit: direct, physical, built for a glance, and it fits long words like "RESILIENCE" on a phone. The serif keeps the book in the brand. The Sisu Way starts as a story, and body copy should read like one. Both are free on Google Fonts and can be self-hosted.

### Scale

| Element | Family | Size | Weight | Line height | Case / tracking |
|---|---|---|---|---|---|
| Display | Barlow Condensed | clamp(48px, 9vw, 100px) | 700 | 0.95 | Uppercase, 0.01em |
| H1 | Barlow Condensed | clamp(40px, 6vw, 68px) | 700 | 1.02 | Uppercase |
| H2 | Barlow Condensed | clamp(32px, 4.5vw, 48px) | 700 | 1.02 | Uppercase |
| H3 | Barlow Condensed | clamp(22px, 2.6vw, 28px) | 700 | 1.1 | Uppercase, 0.02em |
| Label | Barlow Condensed | 15px | 600 | 1.2 | Uppercase, **0.18em** |
| Button / nav | Barlow Condensed | 18px | 700 / 600 | 1.1 | Uppercase, 0.1em |
| Lede | Source Serif 4 | clamp(18px, 2.2vw, 22px) | 400 | 1.55 | Sentence case |
| Body | Source Serif 4 | 19px (18px < 640px) | 400 | 1.65 | Sentence case |
| Quote | Source Serif 4 italic | clamp(18px, 2.4vw, 24px) | 400 | 1.5 | Sentence case |

### Rules

- Condensed caps for anything scanned; serif for anything read. Never set a paragraph in Barlow Condensed.
- Headings are uppercase by CSS, written in sentence case in the HTML so screen readers don't spell them out.
- Measure is capped at 62ch.
- Use the word *sisu* in italics in running text the first time it appears on a page, with a plain-English gloss.

## Mark

A snow ridge line in front of a lower fjord ridge, with the aurora sun rising behind the peak. It is the moment the second wind arrives. Files: `assets/img/mark.svg`, `favicon.svg`.

- **Placeholder quality.** Drawn for the concept. A designer should refine it after the name clears a trademark search (see below).
- Minimum 24px for the mark alone, 120px wide for the lockup.
- Clear space equal to the diameter of the sun on all sides.
- Lockup: mark + "THE SISU WAY" in Barlow Condensed 700, 0.06em tracking. "Sisu" alone takes the brand color: fjord on light, aurora on dark.
- Never recolor the sun, stretch the mark, add effects, or place it on aurora.

## Motif

**Contour lines.** A journey drawn as elevation (`assets/img/contours.svg`). Behind dark sections at 22% opacity, inverted to light; behind light sections at 14%. Never in color, never behind long body text on a light section.

## Style guide

### Spacing

8-point scale: `4 8 12 16 24 32 48 64 96 128`. Sections are 96px tall padding on desktop, 64px on phones. The container is 1120px with 32px gutters, 16px under 640px.

### Radii, borders, shadows

- Buttons 3px, cards and panels 8px, pills fully rounded.
- Borders are a 1px fjord hairline at 22% opacity. Solid fjord for emphasis only.
- **No drop shadows.** Depth comes from the snow / mist / fjord-deep bands.

### Buttons

| Variant | Fill | Text | Border | Hover |
|---|---|---|---|---|
| Primary | aurora | granite | none | `#CF8F27` fill |
| Secondary (light) | none | fjord | 2px fjord | fjord fill, snow text |
| Secondary (dark) | none | snow | 2px snow | snow fill, fjord-deep text |
| Disabled / not yet live | none | slate (mist on dark) | 2px dashed | none |

All buttons are at least 48px tall (44px on the header's compact variant), uppercase condensed 18px.

### Components on the concept

- **Card**: snow, hairline border, 8px radius, number in aurora-deep, H3, serif body.
- **Facts list**: condensed bold term above a serif description, hairline between.
- **Store badges**: dark granite pill with a phone glyph. These are **stand-ins**. At launch they are replaced with Apple's and Google's official badges, which come with their own usage rules.
- **Placeholder marker**: dashed aurora-deep box. Every unconfirmed piece of content carries it.
- **Concept bar**: fjord-deep strip above the header on every page, reading "CONCEPT PREVIEW — Designed and built by Summit Software Solutions for The Sisu Way." Removed at launch.

### Motion

Hover transitions only, 150ms ease-out. `prefers-reduced-motion` disables them.

## Voice and tone

Write like a good coach talks at half-time: short sentences, no hype, no exclamation marks. Name the hard thing, then the next step.

| Say | Don't say |
|---|---|
| Keep going. Find the second wind. | Unleash your potential! |
| Train your sisu. | Crush your goals. Beast mode. |
| It's hard. Here's the next step. | Transform your life in 30 days. |

## Photography direction

Nothing is shot yet. When it is: real places over stock, cold light, wide landscapes with a small human figure, rugby and training in bad weather, hands and faces mid-effort rather than triumphant poses. Treat photos with no filters; let the fjord-deep bands carry the mood.

## Trademark note (important)

"Sisu" is crowded, **including in rugby**:

- **SISU mouthguards** are a well-known rugby brand sold by World Rugby Shop and others.
- A wellness company trades as **SISU Collective**, and **sisu-thebrand.com** runs a "SISU Collective" community.

A trademark search on "The Sisu Way" (USPTO and app store names) must happen before the brand is finalized, the mark is redrawn, or anything goes on a public URL. Tracked in Jira SUMMIT-206.

## Traceability

| Decision | Reason |
|---|---|
| Northern palette | Sisu is Finnish; the book's journey crosses the Alps, Russia and Mongolia |
| One warm accent | "Second wind" as a single point of warmth; keeps CTAs unmistakable |
| Barlow Condensed | Rugby kit and trail signage; long words fit on phones |
| Source Serif 4 | The brand begins as a book |
| Contour motif | A journey measured in elevation |
| Granite text on aurora | Snow on aurora fails at 1.96:1 |
