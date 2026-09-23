"""Sisu Way concept pages, v0.2: content and brand aligned to the live SISU app."""
import pathlib as _p; __file__ = str(_p.Path(__file__).resolve()); exec(open(_p.Path(__file__).with_name("build_sisu_head.py")).read())
import importlib.util
_s = importlib.util.spec_from_file_location("c", str(pathlib.Path(__file__).with_name("contrast_lib.py")))
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)

PILLARS = f"""
    <div class="grid grid--4" style="margin-top:var(--s-6)">
      <article class="card pillar pillar--heart"><span class="pillar__emoji" aria-hidden="true">&#10084;&#65039;</span><h3>Heart</h3><span class="pillar__sub">Connectivity</span><p>Relationships and gratitude. The people who expect you to show up.</p></article>
      <article class="card pillar pillar--body"><span class="pillar__emoji" aria-hidden="true">&#9889;</span><h3>Body</h3><span class="pillar__sub">Movement</span><p>Movement, fuel and physical resilience, built one session at a time.</p></article>
      <article class="card pillar pillar--mind"><span class="pillar__emoji" aria-hidden="true">&#129504;</span><h3>Mind</h3><span class="pillar__sub">Learning</span><p>Learning, positivity and the language you use about yourself.</p></article>
      <article class="card pillar pillar--soul"><span class="pillar__emoji" aria-hidden="true">&#128293;</span><h3>Soul</h3><span class="pillar__sub">Purpose</span><p>Purpose, meaning and the inner fire that keeps you going.</p></article>
    </div>"""

P = {}

P["index.html"] = page("index.html",
 "The Sisu Way - Move. Endure. Thrive.",
 "SISU is the Finnish reserve of inner strength that shows up at your limit. The Sisu Way app helps you build it across four pillars: Heart, Body, Mind and Soul. From coach, author and Royal Navy veteran Angus Peacock.",
 f"""
<section class="hero dark contours">
  <div class="container hero__grid">
    <div>
      <span class="label">Finnish &middot; Resilience &middot; Community</span>
      <h1 class="display">Move. Endure. <span>Thrive.</span></h1>
      <p class="lede">Real-life resilience. Invest in yourself. Thrive forever.</p>
      <div class="btnrow">
        <a class="btn btn--primary" href="{APP}">Open the app</a>
        <a class="btn btn--secondary" href="about.html">Meet Angus</a>
      </div>
    </div>
    <img class="hero__mark" src="assets/img/mark.svg" alt="" width="300" height="300">
  </div>
</section>

<section>
  <div class="container split">
    <div>
      <span class="label">What is sisu?</span>
      <h2>Not just grit. Not just resilience.</h2>
      <p class="lede">A centuries-old Finnish concept with no direct English equivalent.</p>
      <p>Sisu is the extraordinary reserve of inner strength that surfaces when you've reached your perceived limit: the moment you choose to push forward when all logic says stop.</p>
    </div>
    <blockquote class="definition">&ldquo;A state of body, mind, heart, and soul in which you will not give up, no matter what comes your way.&rdquo;<cite>The Sisu Way</cite></blockquote>
  </div>
</section>

<section class="tint">
  <div class="container">
    <span class="label">The four pillars</span>
    <h2>Heart. Body. Mind. Soul.</h2>
    <p>Every session and every reflection in the app builds one or more of the four pillars, and your Pillar Balance shows how each is trending.</p>
    {PILLARS}
  </div>
</section>

<section class="dark contours">
  <div class="container">
    <span class="label">Three ways to train</span>
    <h2>On your own, with your team, or with Angus</h2>
    <div class="grid grid--3" style="margin-top:var(--s-6)">
      <div class="format"><b>&#127939; Self-directed</b><span>Your own session</span><p>Gym, run, row or any independent movement.</p></div>
      <div class="format"><b>&#128101; Group practice</b><span>Team or coach-led</span><p>A standard practice or a SISU-informed one.</p></div>
      <div class="format"><b>&#127945; SISU with Angus</b><span>Coached</span><p>In person, in your space, or online.</p></div>
    </div>
    <h3 style="margin-top:var(--s-8)">Every session has a SISU size</h3>
    <div class="formats">
      <div class="format"><b>SISU Micro</b><span>Under 20 minutes</span><p>Short, sharp, deliberate.</p></div>
      <div class="format"><b>SISU Midi</b><span>21&ndash;44 minutes</span><p>The sweet spot.</p></div>
      <div class="format"><b>Full SISU</b><span>45+ minutes</span><p>All four pillars. Full investment.</p></div>
    </div>
    <div class="btnrow"><a class="btn btn--primary" href="{APP}">Log your first session</a><a class="btn btn--secondary" href="{BOOK}">Book a session with Angus</a></div>
  </div>
</section>

<section>
  <div class="container split">
    <div>
      <span class="label">Watch</span>
      <h2>Meet The Sisu Way</h2>
      <p>The introduction every new member sees on the app's home screen.</p>
    </div>
    <div class="video"><iframe src="{VIDEO}" title="The Sisu Way introduction video" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
  </div>
</section>

<section class="tint">
  <div class="container split">
    <div>
      <span class="label">The story</span>
      <h2>Written the hard way</h2>
      <p>Angus Peacock is a rugby coach, coach educator, Royal Navy veteran and the author of <em>SISU: A Series of Epic Adventures</em>, a true account of turning personal trauma into a journey across Europe and Asia by rail and on foot.</p>
      <p>The Sisu Way is the practice that came out of it, built for people who will never cross a steppe but still have to get up and keep going.</p>
      <div class="btnrow">
        <a class="btn btn--secondary" href="{BOOKSTORE}">Read the SISU story</a>
        <a class="btn btn--secondary" href="about.html">About Angus</a>
      </div>
    </div>
    <ul class="facts">
      <li><b>20+ years</b>Coaching across four continents</li>
      <li><b>Royal Navy</b>Commissioned officer, now a veteran</li>
      <li><b>World Rugby Level 3</b>Coach and accredited coach educator</li>
      <li><b>Author</b><em>SISU: A Series of Epic Adventures</em>, Tactical 16</li>
    </ul>
  </div>
</section>

<section class="dark contours">
  <div class="container">
    <span class="label">&ldquo;Momentum is magical.&rdquo;</span>
    <h2>Start today. Keep going tomorrow.</h2>
    <p class="lede">Use The Sisu Way in your browser now. iPhone and Android apps are on the way.</p>
    <div class="btnrow">
      <a class="btn btn--primary" href="{APP}">Open the app</a>
      <a class="btn btn--secondary" href="app.html#mobile">Get it on your phone</a>
    </div>
  </div>
</section>
""")

P["about.html"] = page("about.html",
 "About Angus Peacock - The Sisu Way",
 "Angus Peacock: Royal Navy veteran, rugby coach and coach educator, life coach and author of SISU: A Series of Epic Adventures.",
 f"""
<section class="hero dark contours">
  <div class="container">
    <span class="label">About</span>
    <h1 class="display">Angus <span>Peacock</span></h1>
    <p class="lede">Coach. Author. Royal Navy veteran. Two decades of learning what makes people keep going, on rugby pitches and far beyond them.</p>
  </div>
</section>

<section>
  <div class="container split">
    <div>
      <span class="label">The story</span>
      <h2>From Croydon to four continents</h2>
      <p>Angus grew up in Croydon, in south London, and found his way out through the Royal Navy, where he was commissioned as an officer. After the Navy he built a second career in coaching that has taken him through China and across North America.</p>
      <p>He has coached rugby for more than twenty years on four continents. He is a World Rugby Level 3 and USA Rugby Level 400 coach and an accredited coach educator, and has directed youth camps and led a state rugby organization in Colorado. He works in English, French and Mandarin Chinese, and mentors people well outside sport as a life coach.</p>
      <p>His book, <em>SISU: A Series of Epic Adventures</em> (Tactical 16), tells how he turned personal trauma into a journey across two continents. The Sisu Way is what he took from it. He writes on <a href="{SUBSTACK}">Substack</a> and posts on <a href="{YOUTUBE}">YouTube</a>.</p>
      <p class="placeholder"><b>To confirm</b>Assembled from public profiles and a 2023 NAAFI Break podcast interview. A portrait and Angus's own bio will replace this copy.</p>
    </div>
    <ul class="facts">
      <li><b>Coaching</b>World Rugby Level 3 &middot; USA Rugby Level 400 &middot; coach educator</li>
      <li><b>Service</b>Royal Navy, commissioned officer</li>
      <li><b>Languages</b>English, French, Mandarin Chinese</li>
      <li><b>Writing</b><em>SISU: A Series of Epic Adventures</em> (Tactical 16) &middot; <em>The Portfolio</em> newsletter</li>
    </ul>
  </div>
</section>

<section class="tint">
  <div class="container split">
    <div>
      <span class="label">Work with Angus</span>
      <h2>The SISU Way&trade;: 1:1 coaching</h2>
      <p>For leaders, founders, and people in transition: stepping into leadership, managing teams, or moving from military or service into business. Be steady under pressure, be a consistent performer and build resilience you can rely on.</p>
      <p>Angus doesn't take every client. It starts with a free 20-minute discovery call: no pitch, no pressure, just an honest assessment of whether there's a fit. Coaching runs through Black Dragon Enterprises, alongside team coaching, the ABC Movement Programme, speaking and expedition learning.</p>
      <div class="btnrow">
        <a class="btn btn--primary" href="{BDE}contact.html#book">Book a discovery call</a>
        <a class="btn btn--secondary" href="{BDE}services.html">Work with Angus</a>
      </div>
    </div>
    <div class="card">
      <span class="card__num">Two sites, one person</span>
      <h3>The Sisu Way</h3>
      <p>The practice and the app, for anyone.</p>
      <h3 style="margin-top:var(--s-5)">Black Dragon Enterprises</h3>
      <p>Angus's coaching, team programmes, speaking and expedition learning.</p>
    </div>
  </div>
</section>
""")

P["app.html"] = page("app.html",
 "The App - The Sisu Way",
 "Open The Sisu Way in your browser today. Log sessions, reflect across Heart, Body, Mind and Soul, and train with your community. iPhone and Android apps are coming soon.",
 f"""
<section class="hero dark contours">
  <div class="container">
    <span class="label">The app</span>
    <h1 class="display">Train your <span>sisu.</span></h1>
    <p class="lede">Log a session, reflect, and watch your four pillars grow. In your browser today; on your phone soon.</p>
  </div>
</section>

<section>
  <div class="container portal">
    <div class="portal__panel portal__panel--web">
      <span class="label">On the web</span>
      <h2>Use it in your browser</h2>
      <p>No download. Sign in with your email on any computer, tablet or phone.</p>
      <div class="btnrow"><a class="btn btn--primary" href="{APP}">Open the web app</a></div>
      <p class="placeholder" style="margin-top:var(--s-5)"><b>Preview</b>Links to the live pilot at sisu-way.netlify.app. Moves to app.thesisuway.com when the domain does.</p>
    </div>
    <div class="portal__panel portal__panel--stores" id="mobile">
      <span class="label">On your phone</span>
      <h2>iPhone and Android</h2>
      <p><span class="pill">Coming soon</span></p>
      <p>Native apps for iPhone and Android are in development. The download links will appear here the day they go live.</p>
      <div class="store-badges">
        <a class="store-badge" href="#" aria-disabled="true">{PHONE}<span><small>Coming soon to the</small><strong>App Store</strong></span></a>
        <a class="store-badge" href="#" aria-disabled="true">{PHONE}<span><small>Coming soon to</small><strong>Google Play</strong></span></a>
      </div>
      <p class="mute" style="margin-top:var(--s-5);font-size:16px">Want to know when they launch? <a href="mailto:angus@blackdragonenterprises.com?subject=The%20Sisu%20Way%20app">Email Angus</a>.</p>
    </div>
  </div>
</section>

<section class="tint">
  <div class="container">
    <span class="label">What's inside</span>
    <h2>Built around the four pillars</h2>
    <div class="grid grid--3" style="margin-top:var(--s-6)">
      <article class="card"><span class="card__num">Log</span><h3>Daily check-in</h3><p>Log each session: self-directed, group practice or SISU with Angus, sized Micro, Midi or Full SISU, with a few quick measures of how you are.</p></article>
      <article class="card"><span class="card__num">Reflect</span><h3>Heart, Body, Mind, Soul</h3><p>A short reflection after each session. Your Pillar Balance shows a 0&ndash;10 score for each pillar and which way it is trending.</p></article>
      <article class="card"><span class="card__num">Together</span><h3>Community</h3><p>Session streaks, buddy check-ins when someone goes quiet, and your group's weekly averages.</p></article>
    </div>
    <h3 style="margin-top:var(--s-8)">Private by default</h3>
    <ul class="checklist" style="max-width:62ch">
      <li>Your coach sees only anonymous group trends: never your name, reflections, email or location.</li>
      <li>You choose whether your coach can see your name next to your check-in trend, and can turn it off any time.</li>
      <li>Pillar scores are provisional, in development and non-clinical.</li>
    </ul>
  </div>
</section>
""")

DRAFT_NOTE = '<p class="placeholder"><b>Draft for legal review</b>Not in effect. Written from how the pilot app works today, for Angus and a lawyer to review before launch. Items in [brackets] are decisions still to make. Both app stores require a public privacy policy and terms.</p>'

P["privacy.html"] = page("privacy.html",
 "Privacy - The Sisu Way",
 "How The Sisu Way collects, uses and protects your information.",
 f"""
<section>
  <div class="container prose">
    <span class="label">Legal</span>
    <h1>Privacy policy</h1>
    {DRAFT_NOTE}
    <p class="mute">Last updated: [date]</p>

    <h2>Who we are</h2>
    <p>The Sisu Way app and this website are run by [Angus Peacock / legal entity name], Colorado, USA ("we"). This policy explains what we collect when you use the app, why, and the choices you have.</p>

    <h2>What we collect</h2>
    <ul>
      <li><strong>Account details:</strong> your email address (to sign you in), your name, and your birth year.</li>
      <li><strong>Your baseline:</strong> answers to a starting questionnaire about wellbeing, mood, stress, sleep, connection and purpose. It includes widely used screening questions about symptoms of low mood and anxiety. These answers are sensitive, and we treat them that way.</li>
      <li><strong>Session check-ins:</strong> the sessions you log and the measures you enter, such as sleep, energy and how hard a session felt.</li>
      <li><strong>Reflections:</strong> what you write after a session, and the pillar scores calculated from it.</li>
      <li><strong>Groups:</strong> which groups you belong to, if any, and whether you share your name with your coach.</li>
      <li><strong>Technical data:</strong> basic logs our hosting and database providers keep to run the service securely.</li>
    </ul>
    <p>We don't sell your information, and we don't use it for advertising.</p>

    <h2>How we use it</h2>
    <ul>
      <li>To run the app: sign-in, logging sessions, and showing your progress across the four pillars.</li>
      <li>To show group trends to a coach, as described below.</li>
      <li>To keep the service secure and fix problems.</li>
      <li>[If applicable: to improve the programme using de-identified, aggregated results. Say so plainly, and ask for consent where required.]</li>
    </ul>

    <h2>How your reflections are scored</h2>
    <p>Your written reflections are sent to an AI service, [Anthropic], to score them against the four pillars. We send the text of the reflection and your effort rating, not your name or email. Scores are provisional and not clinical. [Confirm the provider's data terms, including that API data is not used to train its models, and its retention period.] You'll be told about this in the app before your first reflection is scored.</p>

    <h2>What your coach sees</h2>
    <p>By default a coach sees only group trends, never your individual answers or your reflections. Your name appears next to your check-in trend only if you opt in, and you can turn that off at any time. Averages are only shown for groups large enough that no one can be singled out. [Set the minimum group size.]</p>

    <h2>Who we share it with</h2>
    <p>Only the service providers that run the app for us, under contracts that limit how they can use it:</p>
    <ul>
      <li>[Supabase]: database and sign-in, [region].</li>
      <li>[Hosting provider]: serves the app and this website.</li>
      <li>[Anthropic]: scores reflections, as described above.</li>
    </ul>
    <p>We'll share information if the law requires it. If the business is sold or reorganized, your information would move only under this policy or with your consent.</p>

    <h2>How long we keep it</h2>
    <p>While your account is open. When you delete your account we delete your information, including your baseline answers and reflections, within [30] days, apart from anything we're legally required to keep. Backups roll off within [X] days.</p>

    <h2>Your choices and rights</h2>
    <ul>
      <li>See, download or correct your information.</li>
      <li>Delete your account and data from inside the app.</li>
      <li>Withdraw consent to optional uses at any time.</li>
      <li>Depending on where you live (for example Colorado, California, the UK or the EU), you may have further rights. Contact us to use them.</li>
    </ul>

    <h2>Age</h2>
    <p>The Sisu Way is for people aged [16 / 18] and over. We don't knowingly collect information from anyone younger. If you believe a child has signed up, contact us and we'll delete the account.</p>

    <h2>Not medical care</h2>
    <p>The Sisu Way supports everyday resilience. It isn't a medical or mental-health service, and it doesn't monitor your answers for emergencies. If you're struggling, talk to a doctor or a mental-health professional. In the US, call or text <strong>988</strong> (Suicide &amp; Crisis Lifeline); elsewhere, contact your local emergency number.</p>

    <h2>Security</h2>
    <p>Data is encrypted in transit and stored with access controls so each person can see only their own records. No system is perfectly secure; if a breach affects you, we'll tell you as the law requires.</p>

    <h2>Changes</h2>
    <p>If we make material changes, we'll tell you in the app before they take effect.</p>

    <h2>Contact</h2>
    <p>[privacy@thesisuway.com] or <a href="mailto:angus@blackdragonenterprises.com">angus@blackdragonenterprises.com</a>.</p>
  </div>
</section>
""")

P["terms.html"] = page("terms.html",
 "Terms of use - The Sisu Way",
 "The terms for using The Sisu Way app and website.",
 f"""
<section>
  <div class="container prose">
    <span class="label">Legal</span>
    <h1>Terms of use</h1>
    {DRAFT_NOTE}
    <p class="mute">Last updated: [date]</p>

    <h2>The agreement</h2>
    <p>These terms are between you and [Angus Peacock / legal entity name] ("we"). By creating an account or using the app you agree to them and to our <a href="privacy.html">privacy policy</a>.</p>

    <h2>Who can use it</h2>
    <p>You must be [16 / 18] or older, and able to agree to these terms. One account per person; keep your sign-in secure.</p>

    <h2>What The Sisu Way is, and isn't</h2>
    <p>A resilience practice: sessions, check-ins, reflections and coaching across Heart, Body, Mind and Soul. It is <strong>not</strong> medical, psychological or emergency care, and pillar scores are not a diagnosis. Check with a doctor before starting a new physical routine, especially if you have a health condition. If you're in crisis, call <strong>988</strong> in the US or your local emergency number.</p>

    <h2>Your content</h2>
    <p>Your reflections and answers stay yours. You give us permission to store and process them only to run the app for you, as described in the privacy policy.</p>

    <h2>Fair use</h2>
    <p>Don't misuse the app: no attempts to access other people's data, disrupt the service, or copy or resell the programme content. We may suspend accounts that do.</p>

    <h2>Coaching sessions</h2>
    <p>Sessions with Angus are booked and run separately, through Black Dragon Enterprises, under their own terms.</p>

    <h2>Our content</h2>
    <p>The Sisu Way name, programme, text and design belong to [Angus Peacock / entity]. You may use them for your own practice, not to republish or sell.</p>

    <h2>Changes and availability</h2>
    <p>The app is in active development. Features may change, and we may pause or end the service; if we end it, we'll give notice and a way to download your data.</p>

    <h2>Liability</h2>
    <p>The app is provided "as is". To the extent the law allows, we aren't liable for indirect losses, and our total liability is limited to [the amount you paid us in the past 12 months / $100]. Nothing here limits rights you have under consumer law.</p>

    <h2>Ending your account</h2>
    <p>You can delete your account at any time from inside the app. We may close accounts that break these terms.</p>

    <h2>Law</h2>
    <p>These terms are governed by the laws of the State of Colorado, USA, [unless your local consumer law says otherwise].</p>

    <h2>Contact</h2>
    <p><a href="mailto:angus@blackdragonenterprises.com">angus@blackdragonenterprises.com</a></p>
  </div>
</section>
""")

for n, h in P.items():
    (ROOT / n).write_text(h); print("wrote", n)

(ROOT / "404.html").write_text(page("404.html", "Page not found - The Sisu Way", "This page does not exist.", """
<section class="hero dark contours">
  <div class="container">
    <span class="label">404</span>
    <h1 class="display">Wrong trail. <span>Keep going.</span></h1>
    <p class="lede">This page doesn't exist. Head back to the start and pick up the path.</p>
    <div class="btnrow"><a class="btn btn--primary" href="index.html">Back to home</a><a class="btn btn--secondary" href="app.html">The app</a></div>
  </div>
</section>
""").replace('href="index.html"', 'href="/thesisuway/index.html"').replace('href="about.html"', 'href="/thesisuway/about.html"').replace('href="app.html', 'href="/thesisuway/app.html').replace('href="privacy.html"', 'href="/thesisuway/privacy.html"').replace('href="specimen.html"', 'href="/thesisuway/specimen.html"').replace('href="assets/', 'href="/thesisuway/assets/').replace('src="assets/', 'src="/thesisuway/assets/').replace('href="favicon.svg"', 'href="/thesisuway/favicon.svg"').replace('href="site.webmanifest"', 'href="/thesisuway/site.webmanifest"'))
print("wrote 404.html")

# ---------------------------------------------------------------- specimen
TOK = {
 "white":("#F8FAFC","Page field. App --white."),
 "surface":("#EAF2FB","Tint sections and panels. App --surface."),
 "charcoal":("#1C2833","Body text. App --charcoal."),
 "blue":("#003580","Brand blue: links, accents, secondary buttons. App --blue-deep."),
 "navy":("#0A2540","Dark sections, footer, concept bar. App --amber-ink."),
 "maize":("#FFCB05","Primary button fill, the sun, labels on dark. App --amber."),
 "steel":("#2E86C1","Decorative only: rules, the Body pillar. App --blue-steel."),
 "slate":("#566573","Secondary text on white and surface. App --slate."),
 "gold-ink":("#7A5A06","Derived: maize family, safe as text on light."),
 "heart":("#C0392B","Heart pillar. From the app."),
 "gold":("#B8860B","Soul pillar, decorative only. App --gold-deep."),
}
OK=[("charcoal","white"),("charcoal","surface"),("blue","white"),("blue","surface"),("white","blue"),("white","navy"),("surface","navy"),("maize","navy"),("maize","blue"),("navy","maize"),("gold-ink","white"),("gold-ink","surface"),("slate","white"),("slate","surface"),("heart","white"),("white","charcoal")]
BAD=[("white","maize","Never. Maize buttons take navy text."),("maize","white","Never as text. Use gold-ink."),("steel","white","Decorative only. Never text."),("gold","white","Decorative only. Never text."),("slate","navy","Never. Muted text on dark uses surface.")]
def row(fg,bg,note=None):
    r=C.cr(TOK[fg][0],TOK[bg][0]); s=f'<span class="pairbox" style="color:{TOK[fg][0]};background:{TOK[bg][0]}">Sisu</span>'
    if note: return f"<tr><td>{s}</td><td><code>--{fg}</code></td><td><code>--{bg}</code></td><td class='ratio fail'>{r:.2f}</td><td>{note}</td></tr>"
    return f"<tr><td>{s}</td><td><code>--{fg}</code></td><td><code>--{bg}</code></td><td class='ratio'>{r:.2f}</td><td class='pass'>{'pass' if r>=4.5 else 'large only'}</td><td>{'pass' if r>=7 else '&mdash;'}</td></tr>"
sw="".join(f'<div class="sw"><div class="chip" style="background:{v[0]}"></div><div class="meta"><code>--{k}</code> {v[0]}<span class="src">{v[1]}</span></div></div>' for k,v in TOK.items())
STYLE="""
<style>
.swatches{display:grid;gap:var(--s-4);grid-template-columns:repeat(auto-fill,minmax(200px,1fr));margin-top:var(--s-6)}
.sw{border:var(--border-hair);border-radius:var(--radius);overflow:hidden;background:var(--white)}
.sw .chip{height:96px;border-bottom:var(--border-hair)}
.sw .meta{padding:var(--s-3) var(--s-4) var(--s-4);font-size:15px;line-height:1.45}
.sw code{font-weight:700}
.sw .src{display:block;margin-top:var(--s-1);color:var(--slate);font-size:14px}
.table-wrap{overflow-x:auto;margin-top:var(--s-5)}
table{width:100%;border-collapse:collapse;font-size:15px;min-width:560px}
th,td{text-align:left;padding:var(--s-3) var(--s-3) var(--s-3) 0;border-bottom:var(--border-hair);vertical-align:middle}
th{font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:12px}
.ratio{font-variant-numeric:tabular-nums}.pass{font-weight:700}.fail{font-weight:700;color:#8A1C1C}
.pairbox{display:inline-block;padding:2px var(--s-3);border-radius:var(--radius-sm);font-family:var(--font-display);font-weight:700;border:1px solid rgba(0,0,0,.08)}
.spec{border-bottom:var(--border-hair);padding:var(--s-5) 0;display:grid;gap:var(--s-2) var(--s-5);grid-template-columns:1fr}
@media (min-width:720px){.spec{grid-template-columns:200px 1fr;align-items:baseline}}
.spec__meta{font-size:14px;color:var(--slate)}
.spec__sample{min-width:0;overflow-wrap:break-word}
.logo-row{display:flex;flex-wrap:wrap;gap:var(--s-5);align-items:center;margin-top:var(--s-5)}
.logo-tile{border-radius:var(--radius);padding:var(--s-6);display:flex;align-items:center;justify-content:center;min-width:180px}
</style>"""
BODY=f"""
<section class="hero dark contours">
  <div class="container">
    <span class="label">Brand system &middot; v0.2</span>
    <h1 class="display">The Sisu Way <span>style guide</span></h1>
    <p class="lede">Palette, type, mark and components for thesisuway.com, matched to the live SISU app so the site and the app are one brand.</p>
  </div>
</section>
<section>
  <div class="container">
    <span class="label">Source</span>
    <h2>Taken from the app, not invented</h2>
    <p class="lede">Every core color and both typefaces come straight from the SISU app's stylesheet. Deep blue and maize gold, Playfair Display for headings and DM Sans for everything else. The website adds only a text-safe gold and the pillar rules.</p>
  </div>
</section>
<section class="tint"><div class="container"><span class="label">Color</span><h2>Palette</h2><div class="swatches">{sw}</div></div></section>
<section><div class="container"><span class="label">Accessibility</span><h2>Every pair in use passes WCAG AA</h2><p>Ratios computed from WCAG 2.1 relative luminance.</p>
<div class="table-wrap"><table><thead><tr><th>Sample</th><th>Text</th><th>Background</th><th>Ratio</th><th>AA</th><th>AAA</th></tr></thead><tbody>{"".join(row(a,b) for a,b in OK)}</tbody></table></div>
<h3 style="margin-top:var(--s-8)">Forbidden pairs</h3>
<div class="table-wrap"><table><thead><tr><th>Sample</th><th>Text</th><th>Background</th><th>Ratio</th><th>Rule</th></tr></thead><tbody>{"".join(row(a,b,n) for a,b,n in BAD)}</tbody></table></div></div></section>
<section class="tint"><div class="container"><span class="label">Pillars</span><h2>Each pillar keeps its app color</h2><p>Used only as a top rule on pillar cards and in charts, never as text.</p>{PILLARS}</div></section>
<section><div class="container"><span class="label">Type</span><h2>Playfair Display &amp; DM Sans</h2><p>The app's own pairing: a high-contrast display serif for headings, a clean geometric sans for everything you read and tap.</p>
<div class="spec"><div class="spec__meta">Display &middot; Playfair 900 &middot; clamp(46&ndash;92px)</div><div class="spec__sample display" style="margin:0">Move. Endure.</div></div>
<div class="spec"><div class="spec__meta">H1 &middot; Playfair 700 &middot; clamp(38&ndash;64px)</div><div class="spec__sample"><h1 style="margin:0">Train your sisu</h1></div></div>
<div class="spec"><div class="spec__meta">H2 &middot; Playfair 700 &middot; clamp(30&ndash;46px)</div><div class="spec__sample"><h2 style="margin:0">Heart. Body. Mind. Soul.</h2></div></div>
<div class="spec"><div class="spec__meta">H3 &middot; Playfair 700 &middot; clamp(21&ndash;26px)</div><div class="spec__sample"><h3 style="margin:0">Daily check-in</h3></div></div>
<div class="spec"><div class="spec__meta">Label &middot; DM Sans 700 &middot; 13px &middot; 0.18em</div><div class="spec__sample"><span class="label" style="margin:0">The four pillars</span></div></div>
<div class="spec"><div class="spec__meta">Lede &middot; DM Sans 400 &middot; clamp(18&ndash;22px)</div><div class="spec__sample"><p class="lede" style="margin:0">Real-life resilience. Invest in yourself. Thrive forever.</p></div></div>
<div class="spec"><div class="spec__meta">Body &middot; DM Sans 400 &middot; 18px (17px mobile) / 1.65</div><div class="spec__sample"><p style="margin:0">Every session and every reflection builds one or more of the four pillars.</p></div></div>
<div class="spec"><div class="spec__meta">Quote &middot; Playfair 700</div><div class="spec__sample"><blockquote class="definition" style="margin:0">&ldquo;Momentum is magical.&rdquo;</blockquote></div></div></div></section>
<section class="tint"><div class="container"><span class="label">Mark</span><h2>Sun behind the ridge</h2><p>The app has no logo yet. This mark was drawn for the concept in the app's colors: a white ridge in front of a steel ridge, with the maize sun rising behind the peak. Refine after the trademark search.</p>
<div class="logo-row"><div class="logo-tile" style="background:var(--white);border:var(--border-hair)"><img src="assets/img/mark.svg" alt="The Sisu Way mark" width="120" height="120"></div>
<div class="logo-tile" style="background:var(--navy)"><span class="wordmark" style="color:var(--white)">{MARK}<span class="wordmark__text">The <span style="color:var(--maize)">Sisu</span> Way</span></span></div>
<div class="logo-tile" style="background:var(--white);border:var(--border-hair)"><span class="wordmark">{MARK}<span class="wordmark__text">The <span>Sisu</span> Way</span></span></div></div></div></section>
<section><div class="container"><span class="label">Components</span><h2>Buttons</h2>
<div class="btnrow"><a class="btn btn--primary" href="#">Open the app</a><a class="btn btn--secondary" href="#">Meet Angus</a><a class="btn" href="#" aria-disabled="true">Not yet live</a></div>
<p class="mute" style="margin-top:var(--s-4)">Pill-shaped like the app. One primary per view. Navy text on maize, never white.</p>
<h2 style="margin-top:var(--s-8)">App store badges</h2>
<div class="store-badges"><a class="store-badge" href="#">{PHONE}<span><small>Download on the</small><strong>App Store</strong></span></a><a class="store-badge" href="#" aria-disabled="true">{PHONE}<span><small>Coming soon to</small><strong>Google Play</strong></span></a></div>
<p class="mute" style="margin-top:var(--s-4)">Concept stand-ins. Replace with Apple's and Google's official badges at launch.</p>
<h2 style="margin-top:var(--s-8)">Placeholder marker</h2><p class="placeholder"><b>Placeholder</b>Every unconfirmed item on the concept carries this marker.</p></div></section>
<section class="dark contours"><div class="container split"><div><span class="label">Voice</span><h2>Plain, steady, earned</h2><p>Use the app's own lines: short, physical, no hype. &ldquo;Momentum is magical.&rdquo; &ldquo;Invest in yourself.&rdquo;</p></div>
<ul class="facts"><li><b>Say</b>Move. Endure. Thrive. Log your session. Keep going.</li><li><b>Don't say</b>Unleash your potential! Crush your goals! Beast mode.</li><li><b>Always</b>Explain what sisu means the first time it appears on a page.</li></ul></div></section>
"""
(ROOT/"specimen.html").write_text(page("specimen.html","Brand system - The Sisu Way","Palette, typography, mark and components for The Sisu Way, matched to the SISU app.",BODY,STYLE))
print("wrote specimen.html")


# ---------------------------------------------------------------- launch files
PAGES = ['index.html', 'about.html', 'app.html', 'privacy.html', 'terms.html']
if PROD:
    _p = ROOT / "404.html"; _p.write_text(_p.read_text().replace('"/thesisuway/', '"/'))
    _m = ROOT / "site.webmanifest"; _m.write_text(_m.read_text().replace('"/thesisuway/', '"/'))
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{BASE}{'' if p == 'index.html' else p.replace('.html', '')}</loc></url>\n" for p in PAGES) + "</urlset>\n")
    print("wrote production robots.txt and sitemap.xml")
else:
    (ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
