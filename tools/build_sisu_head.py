"""One-off generator for the Sisu Way concept pages. Output is plain static HTML."""
import pathlib, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "https://ryankolean.github.io/thesisuway/"
BDE = "https://ryankolean.github.io/blackdragonenterprises/"
YOUTUBE = "https://www.youtube.com/@bytheblackdragon"
SUBSTACK = "https://substack.com/@sisublackdragon"
APP = "https://sisu-way.netlify.app/"
BOOK = "https://calendar.app.google/LoMbzd8xpjeCvdap7"
BOOKSTORE = "https://tactical16.com/angus-peacock-author/"
VIDEO = "https://www.youtube-nocookie.com/embed/k57IVP7CYto"

MARK = '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><circle cx="32" cy="32" r="30" fill="#0A2540"/><circle cx="42" cy="21" r="6.5" fill="#FFCB05"/><path d="M9.6 52 L24 42 L34 48 L46 40 L54.4 52" fill="none" stroke="#2E86C1" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/><path d="M5.5 46 L19 30 L26.5 37.5 L37 25 L58.5 46" fill="none" stroke="#F8FAFC" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="6" y="2" width="12" height="20" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 18h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

NAV = [("index.html", "Home"), ("about.html", "About"), ("app.html", "The App")]


def page(slug, title, desc, body, extra_head=""):
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'        <li><a href="{href}"{cur if href == slug else ""}>{label}</a></li>'
        for href, label in NAV
    )
    url = BASE + ("" if slug == "index.html" else slug)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Sisu Way">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#0A2540">
<meta property="og:image" content="{BASE}assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/main.js" defer></script>{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="concept-bar" role="note" aria-label="Concept preview notice">
  <div class="container">
    <p><strong>Concept preview</strong>Designed and built by <a href="https://summitsoftwaresolutions.dev/">Summit Software Solutions</a> for The Sisu Way. Not a live site; placeholder content is marked.</p>
  </div>
</div>

<header class="site-header">
  <div class="container site-header__inner">
    <a class="wordmark" href="index.html" aria-label="The Sisu Way, home">{MARK}<span class="wordmark__text">The <span>Sisu</span> Way</span></a>
    <nav class="site-nav" aria-label="Main">
      <ul>
{nav}
        <li><a class="btn btn--primary" href="app.html">Open the app</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="main">
{textwrap.dedent(body).strip()}
</main>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a class="wordmark" href="index.html" aria-label="The Sisu Way, home">{MARK}<span class="wordmark__text">The <span>Sisu</span> Way</span></a>
        <p style="margin-top:var(--s-4)">Real-life resilience. Invest in yourself. Thrive forever.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Angus</a></li>
          <li><a href="app.html">The app</a></li>
          <li><a href="privacy.html">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h2>Work with Angus</h2>
        <ul>
          <li><a href="{BDE}services.html">The SISU Way&trade; 1:1 coaching</a></li>
          <li><a href="{BDE}contact.html#book">Book a discovery call</a></li>
          <li><a href="{YOUTUBE}">YouTube</a> &middot; <a href="{SUBSTACK}">Substack</a></li>
          <li><a href="mailto:angus@blackdragonenterprises.com">angus@blackdragonenterprises.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__base">
      <span>&copy; 2026 The Sisu Way. All rights reserved.</span>
      <span>Concept by <a href="https://summitsoftwaresolutions.dev/">Summit Software Solutions</a> &middot; <a href="specimen.html">Brand system</a></span>
    </div>
  </div>
</footer>
</body>
</html>
"""


