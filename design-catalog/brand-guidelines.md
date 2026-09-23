# Brand Guidelines: The Sisu Way

**Version:** 0.2, 2026-09-23. Summit Software Solutions, pending Angus Peacock's approval.
**Live version:** [`specimen.html`](../specimen.html) renders every token, pair and component below.

## Principle

**The website follows the app.** The SISU app (`sisu-platform/sisu-platform`, live at sisu-way.netlify.app) already has a visual identity in its stylesheet: deep blue, maize gold, Playfair Display and DM Sans. v0.1 of this guide proposed a separate northern palette before we had access to the app; v0.2 replaces it with the app's own values so the website and the product read as one brand. The website adds only what a marketing site needs: a text-safe gold and pillar rules.

| Source in the app (`prototype.html`) | Value | Website token |
|---|---|---|
| `--white` | `#F8FAFC` | `--white` |
| `--surface` | `#EAF2FB` | `--surface` |
| `--charcoal` | `#1C2833` | `--charcoal` |
| `--blue-deep` | `#003580` | `--blue` |
| `--amber-ink` (navy text on gold) | `#0A2540` | `--navy` |
| `--blue-steel` | `#2E86C1` | `--steel` |
| `--amber` ("maize gold") | `#FFCB05` | `--maize` |
| `--slate` | `#566573` | `--slate` |
| Heart pillar color | `#C0392B` | `--heart` |
| `--gold-deep` / Soul pillar | `#B8860B` | `--gold` |
| Headings font | Playfair Display 700/900 | `--font-display` |
| Body font | DM Sans | `--font-body` |
| *(new, derived)* | `#7A5A06` | `--gold-ink`: maize family darkened until it passes AA on white |

App copy used verbatim on the site: **"Move. Endure. Thrive."**, **"Real-life resilience. Invest in yourself. Thrive forever."**, **"Momentum is magical."**, the "What is Sisu?" definition, the four pillar descriptions, and the session types and formats.

## Color

```css
:root {
  --white:    #F8FAFC;  /* page field */
  --surface:  #EAF2FB;  /* tint sections, panels */
  --charcoal: #1C2833;  /* body text */
  --blue:     #003580;  /* brand blue: links, accents, secondary buttons */
  --navy:     #0A2540;  /* dark sections, footer, concept bar */
  --steel:    #2E86C1;  /* decorative only: rules, Body pillar */
  --maize:    #FFCB05;  /* primary CTA fill, the sun, labels on dark */
  --slate:    #566573;  /* secondary text on light */
  --gold-ink: #7A5A06;  /* amber-family text on light */
  --heart:    #C0392B;  /* Heart pillar */
  --gold:     #B8860B;  /* Soul pillar, decorative only */
}
```

**Proportion.** Mostly white and surface; navy for the hero, one feature band and the footer; maize on exactly one action per view.

### WCAG contrast, every pair in use

| Text | Background | Ratio | AA | AAA |
|---|---|---|---|---|
| `--charcoal` | `--white` | **14.33** | pass | pass |
| `--charcoal` | `--surface` | **13.27** | pass | pass |
| `--blue` | `--white` | **11.02** | pass | pass |
| `--blue` | `--surface` | **10.21** | pass | pass |
| `--white` | `--blue` | **11.02** | pass | pass |
| `--white` | `--navy` | **14.85** | pass | pass |
| `--surface` | `--navy` | **13.76** | pass | pass |
| `--maize` | `--navy` | **10.21** | pass | pass |
| `--maize` | `--blue` | **7.58** | pass | pass |
| `--navy` | `--maize` | **10.21** | pass | pass |
| `--gold-ink` | `--white` | **6.10** | pass | — |
| `--gold-ink` | `--surface` | **5.65** | pass | — |
| `--slate` | `--white` | **5.73** | pass | — |
| `--slate` | `--surface` | **5.30** | pass | — |
| `--heart` | `--white` | **5.20** | pass | — |

### Forbidden pairs

| Text | Background | Ratio | Rule |
|---|---|---|---|
| `--white` | `--maize` | 1.45 | **Never.** Maize buttons take navy text |
| `--maize` | `--white` | 1.45 | **Never as text.** Use `--gold-ink` |
| `--steel` | `--white` | 3.79 | Decorative only |
| `--gold` | `--white` | 3.11 | Decorative only |
| `--slate` | `--navy` | 2.59 | **Never.** Muted text on dark uses `--surface` |

## The four pillars

Each pillar keeps its color from the app, used only as a 5px top rule on pillar cards and in charts, never as text.

| Pillar | Emoji | Subtitle | Description (from the app) | Color |
|---|---|---|---|---|
| Heart | ❤️ | Connectivity | Relationships & gratitude | `--heart` `#C0392B` |
| Body | ⚡ | Movement | Movement, fuel & physical resilience | `--steel` `#2E86C1` |
| Mind | 🧠 | Learning | Learning, positivity & language | `--blue` `#003580` |
| Soul | 🔥 | Purpose | Purpose, meaning & inner fire | `--gold` `#B8860B` |

## Typography

```css
--font-display: "Playfair Display", Georgia, serif;   /* headings, quotes, wordmark */
--font-body:    "DM Sans", system-ui, sans-serif;     /* everything else */
```

Both are the app's own fonts, self-hosted from `assets/fonts/` (SIL OFL).

| Element | Family | Size | Weight | Line height |
|---|---|---|---|---|
| Display | Playfair Display | clamp(46px, 8vw, 92px) | 900 | 1.0 |
| H1 | Playfair Display | clamp(38px, 5.5vw, 64px) | 700 | 1.08 |
| H2 | Playfair Display | clamp(30px, 4vw, 46px) | 700 | 1.08 |
| H3 | Playfair Display | clamp(21px, 2.4vw, 26px) | 700 | 1.2 |
| Label | DM Sans | 13px, uppercase, 0.18em | 700 | 1.2 |
| Button / nav | DM Sans | 15px, uppercase, 0.06em / 15px | 700 / 600 | 1.1 |
| Lede | DM Sans | clamp(18px, 2.1vw, 22px) | 400 | 1.55 |
| Body | DM Sans | 18px (17px < 640px) | 400 | 1.65 |

Headings in sentence case. Uppercase only for labels and buttons.

## Mark

The app has no logo. The concept mark (`assets/img/mark.svg`) is a white ridge in front of a steel ridge with the maize sun rising behind the peak, on a navy disc. Drawn for the concept; refine after the trademark search. Wordmark: mark + "The **Sisu** Way" in Playfair 900, with "Sisu" in blue on light and maize on dark.

## Components

- **Buttons**: pill-shaped like the app. Primary maize with navy text; secondary blue outline (white outline on dark). 48px minimum height.
- **Pillar cards**: white, hairline border, 12px radius, 5px pillar-color top rule, emoji, Playfair name, uppercase subtitle.
- **Session types and formats**: translucent tiles on navy (Self-directed, Group practice, SISU with Angus; Micro under 20 min, Midi 21–44, Full 45+).
- **Video**: 16:9, 12px radius, YouTube privacy-enhanced (`youtube-nocookie.com`) embed of the app's intro video.
- **Store badges**: concept stand-ins, replaced by Apple's and Google's official badges at launch.
- **Placeholder marker**: dashed gold-ink box on every unconfirmed item.
- **Concept bar**: navy strip above the header on every page. Removed at launch.

## Motif

Topographic contour lines behind navy sections at 20%, inverted; behind light sections at 12%.

## Voice

Use the app's own lines: short, physical, no hype. "Move. Endure. Thrive." "Invest in yourself." "Momentum is magical." Explain what sisu means the first time it appears on a page.

## Trademark note (important)

"Sisu" is crowded, including in rugby: **SISU mouthguards** (a major rugby mouthguard brand), **SISU Collective** (wellness), and **sisu-thebrand.com**. A proper USPTO and app store search on "The Sisu Way" must happen before the mark is finalized or anything goes public. Tracked in Jira SUMMIT-206.

## Changelog

- **v0.2 (2026-09-23)**: aligned to the live SISU app: palette, fonts, pillars, taglines and features. v0.1's northern palette (fjord blue and aurora amber, Barlow Condensed and Source Serif 4) is retired.
- **v0.1 (2026-09-23)**: first proposal, made before we had app access.
