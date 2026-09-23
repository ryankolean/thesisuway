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
| `index.html` | Landing: what sisu is, the four-pillar practice, Angus and the book, the app |
| `about.html` | Angus Peacock, with links to Black Dragon Enterprises |
| `app.html` | Portal to the web app, plus App Store and Google Play links ("coming soon" until the apps ship) |
| `privacy.html` | Section skeleton for the privacy policy both app stores require |
| `specimen.html` | The brand system, rendered |

## Brand system

Proposed rather than measured: the brand has no existing surfaces to sample yet. Full rationale, contrast tables and rules in [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md).

| Token | Value | Role |
|---|---|---|
| `--snow` | `#F4F2ED` | Page field |
| `--mist` | `#DDE4E4` | Tint sections |
| `--granite` | `#1B1F23` | Text |
| `--fjord` | `#1D4A5C` | Brand color, links |
| `--fjord-deep` | `#0F2B37` | Dark sections, footer, concept bar |
| `--aurora` | `#E3A33B` | Primary action only |
| `--aurora-deep` | `#8A5A0F` | Amber text on light |
| `--slate` | `#56616B` | Secondary text on light |

Type is **Barlow Condensed** (headings, labels, buttons) and **Source Serif 4** (reading text). Every text and background pair in use passes WCAG AA; the forbidden pairs are listed in the guidelines.

## Research

| Path | What |
|---|---|
| [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md) | Palette, contrast, type, mark, motif, components, voice, trademark note |
| [`design-catalog/site-plan.md`](design-catalog/site-plan.md) | Pages, domain plan, relationship to Black Dragon |
| [`design-catalog/assets-needed.md`](design-catalog/assets-needed.md) | Everything we need from Angus, in one list |

## Known placeholders

- **The mark** is drawn for the concept and waits on a trademark search: "SISU" is already a rugby mouthguard brand.
- **Pillars and app features** are proposed from Angus's published work, not from the app itself.
- **"Open the web app"** and the store badges are deliberately not linked yet.
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
