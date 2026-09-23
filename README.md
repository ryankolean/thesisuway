# The Sisu Way

Concept website for **The Sisu Way**, Angus Peacock's resilience practice and app, built by [Summit Software Solutions](https://summitsoftwaresolutions.dev/) as part of a proposal. Destined for **thesisuway.com**.

**This is a preview, not the live site.** Every page carries a concept banner, is marked `noindex, nofollow`, and `robots.txt` disallows crawling. Unconfirmed content is marked on the page with a dashed *Placeholder* box.

- **Concept site:** https://ryankolean.github.io/thesisuway/
- **Brand system:** https://ryankolean.github.io/thesisuway/specimen.html
- **Sister concept:** [`ryankolean/blackdragonenterprises`](https://github.com/ryankolean/blackdragonenterprises), Angus's coaching and consulting site
- **Tickets:** [SUMMIT-197](https://ryan-kolean.atlassian.net/browse/SUMMIT-197) (epic), [SUMMIT-205](https://ryan-kolean.atlassian.net/browse/SUMMIT-205) (this site)

## The site

Static HTML, no framework, no build step.

| Page | What |
|---|---|
| `index.html` | Landing: what sisu is, the four pillars (Heart, Body, Mind, Soul), ways to train, intro video, Angus and the book |
| `about.html` | Angus Peacock, with links to Black Dragon Enterprises |
| `app.html` | Portal to the live web app, plus App Store and Google Play links ("coming soon" until the apps ship) |
| `privacy.html` | Draft privacy policy built from how the pilot app handles data |
| `specimen.html` | The brand system, rendered |

## Brand system

Matched to the live SISU app (`sisu-platform/sisu-platform`), so the site and the product are one brand. Full tokens, contrast tables and rules in [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md).

| Token | Value | Role |
|---|---|---|
| `--white` | `#F8FAFC` | Page field |
| `--surface` | `#EAF2FB` | Tint sections |
| `--charcoal` | `#1C2833` | Text |
| `--blue` | `#003580` | Brand blue, links |
| `--navy` | `#0A2540` | Dark sections, footer, concept bar |
| `--maize` | `#FFCB05` | Primary action only |
| `--gold-ink` | `#7A5A06` | Amber text on light |
| `--slate` | `#566573` | Secondary text on light |

Pillar colors: Heart `#C0392B`, Body `#2E86C1`, Mind `#003580`, Soul `#B8860B`. Type is **Playfair Display** (headings) and **DM Sans** (everything else), the app's own pair, self-hosted. Every text and background pair in use passes WCAG AA.

## Research

| Path | What |
|---|---|
| [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md) | Palette, contrast, type, mark, motif, components, voice, trademark note |
| [`design-catalog/site-plan.md`](design-catalog/site-plan.md) | Pages, domain plan, relationship to Black Dragon |
| [`design-catalog/assets-needed.md`](design-catalog/assets-needed.md) | Everything we need from Angus, in one list |

## Known placeholders

- **The mark** is drawn for the concept and waits on a trademark search: "SISU" is already a rugby mouthguard brand.
- **"Open the web app"** links to the live pilot at sisu-way.netlify.app until the domain moves.
- **Store badges** are stand-ins until the iPhone and Android apps ship.
- **Angus's portrait and own bio** are still needed; the About copy is from public profiles.
- **Privacy policy** is a section skeleton only.
- **No photography.** Nothing has been supplied, and stock would misrepresent the brand.

## Local preview

```bash
python3 -m http.server 4331
```

Then `http://localhost:4331/`.

## Deploy

GitHub Pages from Actions (`.github/workflows/pages.yml`). One-time setup: **Settings → Pages → Source: GitHub Actions**.

## Precedent

Mirrors [`ryankolean/roses`](https://github.com/ryankolean/roses) and [`ryankolean/meantime`](https://github.com/ryankolean/meantime): static multi-page HTML on GitHub Pages with a concept banner and a documented brand system.
