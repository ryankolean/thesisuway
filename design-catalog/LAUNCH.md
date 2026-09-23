# Launch checklist: thesisuway.com

The preview on GitHub Pages is the concept. Launch builds the same pages without the concept bar or `noindex`, with production URLs, and serves them from Cloudflare Pages at thesisuway.com.

## Blockers to clear first
- [ ] **Name and domain.** A preliminary screen found *The Sisu Way* podcast (Scott McGee) using the same name, with search results tying it to thesisuway.com and @thesisuway accounts. Confirm Angus holds thesisuway.com, and get a trademark attorney's clearance search before launch (Jira SUMMIT-206).
- [ ] **Privacy.** `privacy.html` is a placeholder. The app collects wellbeing and mental-health questionnaire answers and sends reflections to an AI service, so the policy must say so, and it needs legal review (SUMMIT-200).
- [ ] Angus signs off the copy, portrait and app screenshots; real App Store and Google Play links replace the concept badges (or the badges are hidden until the apps exist).

## Build
```bash
git checkout -b launch origin/launch-prep
SITE_ENV=production python3 tools/build_sisu_pages.py
```
This removes the concept bar and `noindex`, points canonicals and share images at https://thesisuway.com/, rewrites the 404 page and manifest for the root path, and writes `robots.txt` (allow) and `sitemap.xml`. Decide whether `specimen.html` stays public; it isn't in the sitemap.

## Deploy
- [ ] Porkbun account in Angus's name; thesisuway.com transferred (60-day lock rule applies). Copy any existing DNS records first.
- [ ] Cloudflare Pages project connected to this repo (production branch `launch`), no build command, output directory `/`. Custom domain added; HTTPS on `www` and apex.
- [ ] `app.thesisuway.com` points at the web app once it moves (estimate section 5); until then the "Open the app" links go to sisu-way.netlify.app.
- [ ] Cookieless analytics added; no cookie banner needed for the marketing site.

## After
- [ ] Test at 375, 768 and 1280 px: no horizontal scroll, no console errors, video and links work.
- [ ] Submit the sitemap in Google Search Console.
