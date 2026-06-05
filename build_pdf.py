# -*- coding: utf-8 -*-
import json, base64, pathlib

FB = json.load(open("/home/claude/fonts_b64.json"))
LINK = "https://hiddenrio.gumroad.com/l/liveriolikealocal"

def font_face(name, key, weight="normal", style="normal"):
    return (f"@font-face{{font-family:'{name}';font-style:{style};"
            f"font-weight:{weight};src:url(data:font/ttf;base64,{FB[key]}) format('truetype');}}")

FONTS = "".join([
    font_face("Alfa Slab One","AlfaSlabOne","400"),
    font_face("Patrick Hand","PatrickHand","400"),
    font_face("Lato","LatoRegular","400"),
    font_face("Lato","LatoBold","700"),
    font_face("Lato","LatoBlack","900"),
])

# ---------- reusable visual components ----------
BUNTING_COLORS = ["var(--green)","var(--yellow)","var(--red)","var(--blue)","var(--orange)","var(--pink)"]
def bunting(n=22, cls="bunting"):
    flags = "".join(
        f'<span class="flag" style="--fc:{BUNTING_COLORS[i%len(BUNTING_COLORS)]}"></span>'
        for i in range(n))
    return f'<div class="{cls}"><div class="bline"></div><div class="flags">{flags}</div></div>'

BONFIRE = '''<svg class="bonfire" viewBox="0 0 120 150" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="fg" cx="50%" cy="70%" r="60%">
    <stop offset="0%" stop-color="#fff3b0"/><stop offset="35%" stop-color="#ffce1f"/>
    <stop offset="70%" stop-color="#ff7a18"/><stop offset="100%" stop-color="#ff4d2e"/></radialGradient></defs>
  <path d="M60 18 C44 50 30 60 34 92 C36 122 52 134 60 138 C68 134 84 122 86 92 C90 60 76 50 60 18 Z" fill="url(#fg)"/>
  <path d="M60 56 C52 74 46 82 50 100 C52 116 56 124 60 128 C64 124 68 116 70 100 C74 82 68 74 60 56 Z" fill="#fff3b0" opacity="0.85"/>
  <g stroke="#7a4a22" stroke-width="7" stroke-linecap="round">
    <line x1="26" y1="142" x2="94" y2="120"/><line x1="94" y1="142" x2="26" y2="120"/>
    <line x1="38" y1="146" x2="82" y2="146"/></g>
</svg>'''

BALLOON = '''<svg class="balloon" viewBox="0 0 80 120" xmlns="http://www.w3.org/2000/svg">
  <path d="M40 4 C16 4 6 26 6 44 C6 66 28 78 40 96 C52 78 74 66 74 44 C74 26 64 4 40 4 Z" fill="var(--red)"/>
  <path d="M40 4 C30 4 24 26 24 50 C24 70 32 84 40 96 C48 84 56 70 56 50 C56 26 50 4 40 4 Z" fill="var(--yellow)"/>
  <path d="M40 4 C36 4 34 26 34 52 C34 72 37 86 40 96 C43 86 46 72 46 52 C46 26 44 4 40 4 Z" fill="var(--green)"/>
  <rect x="34" y="100" width="12" height="9" rx="2" fill="#7a4a22"/>
  <g stroke="#caa15a" stroke-width="1.4"><line x1="30" y1="92" x2="35" y2="100"/><line x1="50" y1="92" x2="45" y2="100"/></g>
</svg>'''

HAT = '''<svg viewBox="0 0 120 90" xmlns="http://www.w3.org/2000/svg" class="ic">
  <ellipse cx="60" cy="68" rx="54" ry="16" fill="#caa15a"/><ellipse cx="60" cy="64" rx="54" ry="14" fill="#e0bd77"/>
  <path d="M30 64 C30 30 44 16 60 16 C76 16 90 30 90 64 Z" fill="#e0bd77"/>
  <path d="M30 64 C30 30 44 16 60 16 C76 16 90 30 90 64" fill="none" stroke="#b7913f" stroke-width="3"/>
  <rect x="30" y="52" width="60" height="9" fill="#b7913f"/></svg>'''
CORN = '''<svg viewBox="0 0 60 110" xmlns="http://www.w3.org/2000/svg" class="ic">
  <path d="M30 8 C12 8 10 40 14 70 C16 90 24 102 30 102 C36 102 44 90 46 70 C50 40 48 8 30 8Z" fill="#ffce1f"/>
  <g fill="#e8a200"><circle cx="24" cy="30" r="3"/><circle cx="36" cy="30" r="3"/><circle cx="30" cy="40" r="3"/><circle cx="22" cy="48" r="3"/><circle cx="38" cy="48" r="3"/><circle cx="30" cy="58" r="3"/><circle cx="24" cy="68" r="3"/><circle cx="36" cy="68" r="3"/><circle cx="30" cy="78" r="3"/></g>
  <path d="M30 8 C18 -2 4 4 10 24 C20 22 28 18 30 8Z" fill="#0a7d36"/>
  <path d="M30 8 C42 -2 56 4 50 24 C40 22 32 18 30 8Z" fill="#0a9d44"/></svg>'''
NOTE_GUITAR = '''<svg viewBox="0 0 80 110" xmlns="http://www.w3.org/2000/svg" class="ic">
  <ellipse cx="40" cy="78" rx="26" ry="28" fill="#c47a2b"/><ellipse cx="40" cy="56" rx="18" ry="18" fill="#c47a2b"/>
  <circle cx="40" cy="74" r="9" fill="#5a3414"/><rect x="36" y="8" width="8" height="48" rx="3" fill="#7a4a22"/>
  <rect x="30" y="6" width="20" height="10" rx="3" fill="#5a3414"/></svg>'''

def cta(label, sub="", big=False, theme="yellow"):
    cls = "cta big" if big else "cta"
    subhtml = f'<span class="cta-sub">{sub}</span>' if sub else ""
    return (f'<a class="{cls} t-{theme}" href="{LINK}">'
            f'<span class="cta-main">{label}</span>{subhtml}'
            f'<span class="cta-arrow">→</span></a>')

def page(inner, cls=""):
    return f'<section class="page {cls}">{inner}</section>'

# ---------- CSS ----------
CSS = """
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
html,body{margin:0;padding:0;}
:root{
 --green:#0a8a3c; --green-deep:#066026; --yellow:#ffcb1f; --yellow-deep:#f2a900;
 --blue:#0b2c7a; --blue-deep:#061a4d; --white:#fffdf6; --cream:#fff6df; --paper:#fdf1d3;
 --orange:#ff7a18; --fire:#ff4d2e; --red:#e23a3a; --pink:#e8417f;
 --ink:#34240f; --ink-soft:#5a4327; --kraft:#8a5a2b;
}
body{font-family:'Lato',sans-serif;color:var(--ink);line-height:1.5;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always;
 background:var(--cream);}
.page:last-child{page-break-after:auto;}
.pad{position:relative;z-index:5;padding:20mm 17mm 16mm;height:100%;}

/* gingham paper texture */
.gingham{background-color:var(--cream);
 background-image:
  repeating-linear-gradient(0deg, rgba(226,58,58,.05) 0 7mm, transparent 7mm 14mm),
  repeating-linear-gradient(90deg, rgba(226,58,58,.05) 0 7mm, transparent 7mm 14mm);}

/* bunting */
.bunting{position:absolute;left:0;right:0;top:0;height:34px;z-index:8;}
.bunting .bline{position:absolute;top:5px;left:-2%;right:-2%;height:3px;border-radius:3px;
 background:repeating-linear-gradient(90deg,#7a4a22 0 8px,#9a6230 8px 16px);}
.bunting .flags{display:flex;justify-content:space-between;padding:6px 6px 0;}
.flag{width:0;height:0;border-left:13px solid transparent;border-right:13px solid transparent;
 border-top:21px solid var(--fc);filter:drop-shadow(0 2px 1px rgba(0,0,0,.18));}
.bunting.b2{top:auto;bottom:0;transform:scaleY(-1);}

/* ===== COVER ===== */
.cover{background:
  radial-gradient(120% 70% at 50% 118%, rgba(255,122,24,.55) 0%, rgba(255,77,46,.0) 42%),
  radial-gradient(80% 50% at 80% 12%, rgba(255,203,31,.18) 0, transparent 60%),
  linear-gradient(180deg,#061a4d 0%, #0b2c7a 55%, #123a8f 100%);}
.stars{position:absolute;inset:0;z-index:1;}
.star{position:absolute;background:#fff;border-radius:50%;opacity:.85;}
.cover .pad{display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:18mm;}
.eyebrow{font-family:'Patrick Hand',cursive;color:var(--yellow);font-size:18pt;letter-spacing:.5px;
 background:rgba(255,255,255,.08);border:1.5px dashed rgba(255,203,31,.6);padding:5px 16px;border-radius:30px;}
.cover h1{font-family:'Alfa Slab One',serif;color:var(--yellow);font-size:54pt;line-height:.96;margin:16px 0 4px;
 text-shadow:0 4px 0 var(--fire),0 6px 14px rgba(0,0,0,.45);letter-spacing:.5px;}
.cover h1 .sm{display:block;font-size:30pt;color:#fff;text-shadow:0 3px 0 var(--green-deep),0 5px 10px rgba(0,0,0,.4);}
.cover .lead{color:#fdf1d3;font-size:13.5pt;max-width:148mm;margin:18px auto 0;line-height:1.55;}
.cover .lead b{color:var(--yellow);}
.ribbon{margin-top:22px;display:inline-flex;align-items:center;gap:10px;background:var(--green);
 color:#fff;font-weight:900;padding:9px 22px;border-radius:8px;font-size:13pt;
 box-shadow:0 6px 0 var(--green-deep);letter-spacing:.5px;}
.cover-scene{position:absolute;left:0;right:0;bottom:0;height:120mm;z-index:2;pointer-events:none;}
.bonfire{position:absolute;bottom:14mm;left:50%;transform:translateX(-50%);width:70mm;
 filter:drop-shadow(0 0 30px rgba(255,140,30,.7));}
.balloon{position:absolute;width:24mm;}
.balloon.b1{top:30mm;left:18mm;transform:rotate(-6deg);}
.balloon.b2{top:48mm;right:16mm;width:18mm;transform:rotate(7deg);}
.cover-foot{position:absolute;bottom:8mm;left:0;right:0;text-align:center;color:#cfd8ef;
 font-size:9.5pt;z-index:6;letter-spacing:1px;}

/* headings */
.kicker{font-family:'Patrick Hand',cursive;color:var(--red);font-size:16pt;margin:0 0 2px;}
h2.sec{font-family:'Alfa Slab One',serif;font-size:30pt;line-height:1;color:var(--blue);margin:0 0 10px;
 text-shadow:2px 2px 0 var(--yellow);}
h2.sec.alt{color:var(--green-deep);text-shadow:2px 2px 0 var(--yellow);}
p{margin:0 0 9px;font-size:11.3pt;color:var(--ink-soft);}
p.big{font-size:12.5pt;color:var(--ink);}
.lead2{font-size:12pt;color:var(--ink);}
b,strong{color:var(--ink);}
.hl{background:linear-gradient(transparent 55%, var(--yellow) 55%);padding:0 2px;font-weight:700;color:var(--ink);}

/* note / handwritten sticky */
.note{font-family:'Patrick Hand',cursive;font-size:14pt;color:#3a2a12;background:#fff7cf;
 border:2px solid #ffcb1f;border-radius:10px;padding:12px 16px;position:relative;line-height:1.35;
 box-shadow:3px 4px 0 rgba(0,0,0,.08);transform:rotate(-.8deg);}
.note:before{content:"📌";position:absolute;top:-14px;left:-8px;font-size:20pt;}
.note .tip{color:var(--red);font-weight:700;}

/* CTA button */
.cta{display:flex;align-items:center;gap:12px;text-decoration:none;border-radius:14px;
 padding:15px 22px;margin:6px 0;box-shadow:0 6px 0 rgba(0,0,0,.18),0 10px 18px rgba(0,0,0,.18);}
.cta .cta-main{font-family:'Lato';font-weight:900;font-size:14pt;line-height:1.1;flex:1;}
.cta .cta-sub{font-size:9.5pt;font-weight:700;opacity:.92;display:block;}
.cta .cta-arrow{font-size:20pt;font-weight:900;}
.cta.big{padding:20px 26px;}
.cta.big .cta-main{font-size:17pt;}
.cta.big .cta-sub{font-size:10.5pt;}
.t-yellow{background:linear-gradient(180deg,#ffd83a,#f2a900);color:#3a2400;}
.t-yellow .cta-arrow{color:#7a3b00;}
.t-green{background:linear-gradient(180deg,#13a64a,#066026);color:#fff;}
.t-red{background:linear-gradient(180deg,#ff5a4a,#d12626);color:#fff;}
.cta-wrap{display:flex;flex-direction:column;}
.cta-foot{font-family:'Patrick Hand',cursive;color:var(--ink-soft);font-size:11.5pt;margin-top:2px;text-align:center;}

/* cards */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:11px;}
.card{background:#fff;border:2px solid #f0d99a;border-radius:14px;padding:13px 15px;
 box-shadow:0 4px 0 rgba(0,0,0,.05);}
.card h3{font-family:'Lato';font-weight:900;color:var(--green-deep);font-size:12pt;margin:0 0 4px;display:flex;align-items:center;gap:7px;}
.card p{font-size:10pt;margin:0;color:var(--ink-soft);line-height:1.4;}
.emoji{font-size:14pt;}

/* festa feature block */
.festa{background:#fff;border-radius:18px;border:2px solid #f0d99a;overflow:hidden;
 box-shadow:0 8px 0 rgba(0,0,0,.05);}
.festa .top{padding:16px 20px;color:#fff;position:relative;}
.festa .num{font-family:'Alfa Slab One',serif;font-size:30pt;opacity:.32;position:absolute;right:18px;top:6px;line-height:1;}
.festa .pin{font-family:'Patrick Hand',cursive;font-size:13pt;opacity:.95;}
.festa .top h3{font-family:'Alfa Slab One',serif;font-size:21pt;margin:2px 0 0;line-height:1.02;}
.festa .body{padding:14px 20px 16px;}
.festa .body p{font-size:11pt;}
.datebar{display:inline-flex;align-items:center;gap:8px;background:var(--yellow);color:#3a2400;
 font-weight:900;border-radius:8px;padding:7px 13px;font-size:11pt;margin:2px 0 10px;box-shadow:0 3px 0 var(--yellow-deep);}
.tagrow{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0;}
.tag{background:var(--cream);border:1.5px solid #e9cf93;border-radius:20px;padding:3px 11px;font-size:9.3pt;font-weight:700;color:var(--ink-soft);}
.g1 .top{background:linear-gradient(120deg,#0b2c7a,#1747b3);}
.g2 .top{background:linear-gradient(120deg,#0a8a3c,#066026);}
.g3 .top{background:linear-gradient(120deg,#ff7a18,#d12626);}

/* dark feature pages */
.dark{background:
  radial-gradient(90% 60% at 50% 0%, rgba(255,203,31,.14),transparent 60%),
  linear-gradient(180deg,#061a4d,#0b2c7a);color:#eaf0ff;}
.dark h2.sec{color:#fff;text-shadow:2px 2px 0 var(--fire);}
.dark p{color:#d7e0f5;}
.dark .kicker{color:var(--yellow);}
.glasscard{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,203,31,.4);
 border-radius:14px;padding:15px 18px;}

/* benefit list */
.benefits{list-style:none;margin:8px 0 0;padding:0;columns:1;}
.benefits li{display:flex;gap:10px;margin:0 0 9px;font-size:10.6pt;line-height:1.35;}
.benefits li .bi{font-size:14pt;flex:0 0 auto;}
.benefits li b{color:var(--ink);}
.dark .benefits li b{color:#fff;}
.dark .benefits li{color:#dde6fa;}

/* before / after */
.ba{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.ba .col{border-radius:14px;padding:14px 16px;}
.ba .before{background:#f3e3e3;border:2px solid #e0a3a3;}
.ba .after{background:#e3f3e8;border:2px solid #92cda6;}
.ba h4{font-family:'Lato';font-weight:900;font-size:12.5pt;margin:0 0 8px;display:flex;gap:7px;align-items:center;}
.ba .before h4{color:#b5302e;} .ba .after h4{color:var(--green-deep);}
.ba p{font-size:9.7pt;margin:0 0 6px;line-height:1.35;}

/* price box */
.price{background:linear-gradient(180deg,#fff,#fff6df);border:3px solid var(--green);border-radius:18px;
 padding:18px 20px;box-shadow:0 8px 0 rgba(10,138,60,.18);text-align:center;}
.price .was{color:#b5302e;text-decoration:line-through;font-weight:700;font-size:12pt;}
.price .now{font-family:'Alfa Slab One',serif;color:var(--green-deep);font-size:38pt;line-height:1;margin:2px 0;}
.price .now small{font-size:14pt;color:var(--ink-soft);}
.price .term{font-family:'Patrick Hand',cursive;font-size:13pt;color:var(--red);}
.checks{list-style:none;padding:0;margin:10px 0 0;text-align:left;}
.checks li{font-size:9.8pt;margin:0 0 5px;color:var(--ink-soft);}
.checks li:before{content:"✅ ";}

/* faq */
.faq{margin-top:4px;}
.faq .q{font-weight:900;color:var(--blue);font-size:10.6pt;margin:9px 0 1px;}
.faq .a{font-size:9.8pt;color:var(--ink-soft);margin:0;}

/* footer */
.foot{position:absolute;bottom:7mm;left:17mm;right:17mm;display:flex;justify-content:space-between;
 align-items:center;font-size:8.4pt;color:var(--kraft);z-index:6;font-family:'Lato';font-weight:700;letter-spacing:.4px;}
.foot .brand{font-family:'Patrick Hand',cursive;font-size:11pt;color:var(--red);letter-spacing:0;}

/* misc */
.scene-row{display:flex;justify-content:center;gap:26px;align-items:flex-end;margin:6px 0 0;}
.ic{height:46px;}
.divider{height:3px;background:repeating-linear-gradient(90deg,var(--green) 0 14px,var(--yellow) 14px 28px,var(--red) 28px 42px,var(--blue) 42px 56px);
 border-radius:3px;margin:12px 0;}
.lead-q{font-family:'Patrick Hand',cursive;font-size:15pt;color:var(--blue);line-height:1.3;}
.tinycaps{font-family:'Lato';font-weight:900;letter-spacing:2px;font-size:9pt;color:var(--green-deep);text-transform:uppercase;}
"""

def stars_html(n=70):
    import random
    random.seed(7)
    s=[]
    for _ in range(n):
        x=random.uniform(0,100); y=random.uniform(0,62); sz=random.choice([1,1,1.5,2,2.5])
        op=random.uniform(.4,1)
        s.append(f'<div class="star" style="left:{x:.1f}%;top:{y:.1f}%;width:{sz}px;height:{sz}px;opacity:{op:.2f}"></div>')
    return '<div class="stars">'+''.join(s)+'</div>'

def foot(pg):
    return (f'<div class="foot"><span class="brand">Real Cariocas in Your Pocket 🇧🇷</span>'
            f'<span>RIO FESTA JUNINA INSIDER GUIDE · JUNE 2026</span><span>{pg}</span></div>')

# =================== PAGES ===================
pages = []

# ---- COVER ----
cover = f'''{stars_html()}
{bunting(20)}
<div class="cover-scene">{BONFIRE}
 <div style="position:absolute">{BALLOON}</div></div>
<div class="balloon b1">{BALLOON}</div>
<div class="balloon b2">{BALLOON}</div>
<div class="pad">
  <div class="eyebrow">Real Cariocas in Your Pocket presents</div>
  <h1>ARRAIÁ<br>DO RIO<span class="sm">Festa Junina Insider Guide</span></h1>
  <p class="lead">You commented <b>“JUNE PARTY”</b> — so here it is. Your born-and-raised local’s
   <b>TOP&nbsp;3 São João parties in Rio</b>, what a festa junina actually <i>is</i>,
   the traditions, the food, and how to live June like a true carioca. 🌽🔥</p>
  <div class="ribbon">🎉 TOP 3 FESTAS · TRADITIONS · INSIDER TIPS</div>
</div>
<div class="cover-foot">RIO DE JANEIRO · JUNE 2026 · feito com carinho por Vitor &amp; Isha</div>'''
pages.append(page(cover,"cover"))

# ---- PAGE 2: welcome + open loop + CTA 1 ----
p2 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">Olá, gringo amigo! 👋</div>
  <h2 class="sec">WELCOME TO THE MOST<br>CARIOCA MONTH OF<br>THE YEAR.</h2>
  <p class="big">In Brazil, June isn’t just a month — it’s a <b>whole season</b>. While the rest of the
   world thinks of Rio as beaches and Carnival, locals know that June belongs to the
   <span class="hl">Festa Junina</span>: bonfires, forró, corn everything, and the warmest, most
   joyful street energy of the year. And you’re here for it. 🔥</p>
  <p>You asked for the good stuff, so we over-delivered. Here’s what’s inside this guide:</p>
  <div class="grid2" style="margin:8px 0 12px;">
    <div class="card"><h3><span class="emoji">🌽</span>What a festa junina <i>really</i> is</h3><p>The history, the saints, the caipira culture — explained for a first-timer.</p></div>
    <div class="card"><h3><span class="emoji">💃</span>Every tradition, decoded</h3><p>Quadrilha, the bonfire, the food, the drinks, the costumes, the games.</p></div>
    <div class="card"><h3><span class="emoji">📍</span>The TOP 3 festas in Rio</h3><p>With exact dates, what to expect, and an honest “is it worth it?” call.</p></div>
    <div class="card"><h3><span class="emoji">🤙</span>Insider tips you can’t Google</h3><p>What to eat, when to go, and how to get home safe — local-style.</p></div>
  </div>
  <div class="note">📍 <span class="tip">Open loop:</span> on the <u>very last page</u> I’ll show you the
   <b>one thing</b> that separates tourists who just <i>survive</i> June in Rio from the ones who actually
   <i>live</i> it — and how to keep a real carioca in your pocket for less than the price of one wrong Uber.
   Read to the end. ✍️ (Underline that — you’ll thank me later.)</p></div>
  <div class="cta-wrap" style="margin-top:14px;">
    {cta("Get a real local in your pocket — 24/7","Rio VIP Insider Support · $19.99 for 30 days (opening price)",theme="green")}
    <div class="cta-foot">↑ Tap the button — it opens our private VIP. More on this later. 😉</div>
  </div>
</div>
{foot("01")}'''
pages.append(page(p2,"gingham"))

# ---- PAGE 3: what is festa junina ----
p3 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">First things first…</div>
  <h2 class="sec">SO… WHAT IS A<br>FESTA JUNINA?</h2>
  <p class="big">A <b>Festa Junina</b> (“June Festival”, also called <i>festa de São João</i> or simply
   <i>arraiá</i>) is Brazil’s big midwinter countryside celebration — and after Carnival, it’s the
   <span class="hl">second most popular party in the whole country.</span></p>
  <p>It started centuries ago as European midsummer harvest festivals brought over by the Portuguese,
   then fused with Brazilian rural life into something completely its own. Officially, it honors three
   Catholic saints: <b>Santo Antônio</b> (June 13), <b>São João</b> (June 24) and <b>São Pedro</b> (June 29).</p>
  <p>But at its heart, it’s a loving celebration of <b>caipira</b> (countryside) culture and the harvest —
   especially <b>corn</b>, which shows up in basically every dish. People dress up as friendly “country folk,”
   light a bonfire, dance in pairs, eat until they can’t move, and sip something warm. It’s cozy, communal,
   a little silly, and deeply Brazilian.</p>
  <div class="divider"></div>
  <p class="lead2"><b>In Rio specifically?</b> The Northeast of Brazil does festa junina on a legendary
   scale — but Rio brings its own warm, neighborhood-meets-party energy. You’ll find everything from a
   massive, authentic Northeastern culture hall to chic lakeside arraiás with a postcard view of the
   mountains. There’s a perfect one for every kind of traveler — and you’ll meet all three in a moment.</p>
  <div class="scene-row">{HAT}{CORN}{NOTE_GUITAR}</div>
  <div class="note" style="margin-top:14px;">🗣️ <span class="tip">Say it like a local:</span> an
   <b>“arraiá”</b> (ah-ha-YÁ) is the festa junina party itself. Walk up, say “bora pro arraiá!” and
   watch a carioca smile. ✍️ <i>Mentally note one word to try tonight.</i></p></div>
</div>
{foot("02")}'''
pages.append(page(p3))

# ---- PAGE 4: traditions ----
def tc(emoji,title,body):
    return f'<div class="card"><h3><span class="emoji">{emoji}</span>{title}</h3><p>{body}</p></div>'
trad_cards = "".join([
 tc("💃","Quadrilha","A joyful group square-dance acting out a comic “country wedding,” led by a caller. Lots of twirling, laughing and zero pressure to be good at it."),
 tc("🔥","A Fogueira","The bonfire, lit in honor of São João — the glowing heart of every festa. People gather around it to talk, warm up and watch the sparks."),
 tc("👒","Trajes Caipiras","The costumes: plaid shirts, straw hats, patched dresses, braids and painted-on freckles. Dressing up is half the fun — nobody’s watching, everybody’s in."),
 tc("🌽","Comida de Milho","Corn is king: pamonha, canjica/curau, grilled & boiled corn, plus paçoca, pé de moleque, bolo de fubá, cocada and the candy-apple maçã do amor."),
 tc("🍷","Quentão","The signature drink: a hot, sweet, spiced brew of cachaça (or wine) with ginger, cinnamon and cloves. Perfect for Rio’s cooler June nights."),
 tc("🎯","Brincadeiras","Carnival-style games: pescaria (fishing), ring toss, “correio elegante” (the flirty mail game) and the mock casamento caipira. Easy wins, big laughs."),
 tc("🪗","Forró & Baião","The soundtrack: forró, xote and baião. The patron saint of the genre is Luiz Gonzaga, the legendary “King of Baião” — remember that name for festa #1."),
 tc("🎈","Balões & Fogos","Festive décor balloons, paper lanterns and fireworks light up the night sky and give the whole arraiá its magical, glowing atmosphere."),
]
)
p4 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">The full flavor 🌽</div>
  <h2 class="sec alt">THE TRADITIONS,<br>DECODED.</h2>
  <p>Walk into any arraiá and you’ll meet these eight things. Now you’ll know exactly what’s going on —
   and how to join in like you’ve done it your whole life.</p>
  <div class="grid2" style="margin-top:10px;">{trad_cards}</div>
  <div class="note" style="margin-top:13px;">📌 <span class="tip">Insider move:</span> don’t just watch the
   quadrilha — accept when someone waves you in. Looking a little lost while smiling is the most
   authentic festa junina experience there is. 😄</p></div>
</div>
{foot("03")}'''
pages.append(page(p4,"gingham"))

# ---- PAGE 5: TOP3 intro + Festa 1 ----
p5 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">The part you commented for 👇</div>
  <h2 class="sec">RIO’S TOP 3<br>FESTAS JUNINAS</h2>
  <p class="big">Three festas, three completely different vibes — picked so there’s a perfect one for
   you whether you want <b>the real-deal Northeast experience</b>, a <b>chic lakeside arraiá</b>, or an
   <b>easy, comfortable family party.</b> Let’s go. 🎉</p>
  <div class="festa g1" style="margin-top:14px;">
    <div class="top"><span class="num">01</span>
      <div class="pin">📍 Centro Luiz Gonzaga · São Cristóvão</div>
      <h3>São João da Feira<br>de São Cristóvão</h3>
    </div>
    <div class="body">
      <span class="datebar">🗓️ Select days · May 29 → June 27</span>
      <p>The most <b>authentic</b> festa in Rio — a giant covered pavilion entirely dedicated to
       Northeastern Brazilian culture, named after <b>Luiz Gonzaga</b>, the King of Baião. Walking in
       feels like stepping straight into the Nordeste: real forró bands on multiple stages, food
       stalls serving carne de sol, baião de dois and tapioca, cordel poetry, repente, dancing till
       very late. This is where you feel the <span class="hl">true soul</span> of festa junina.</p>
      <div class="tagrow">
        <span class="tag">🪗 Live forró pé-de-serra</span><span class="tag">🍢 Northeastern food</span>
        <span class="tag">💃 Dancing till late</span><span class="tag">🎭 Cordel & repente</span></div>
      <p style="margin:0;"><b>Official programming:</b> June 5, 6, 12, 13, 19, 20, 26 &amp; 27 — with the
       season stretching across June and July (sometimes into August).</p>
      <div class="note" style="margin-top:11px;">📌 <span class="tip">Our tip:</span> go Friday or
       Saturday night for the fullest forró; the food’s incredible any day. Take an official ride and
       ask us the smart late-night route home. 🚕</p></div>
    </div>
  </div>
</div>
{foot("04")}'''
pages.append(page(p5))

# ---- PAGE 6: Festa 2 + Festa 3 ----
p6 = f'''{bunting(18)}
<div class="pad">
  <div class="festa g2">
    <div class="top"><span class="num">02</span>
      <div class="pin">📍 Parque das Figueiras · Lagoa</div>
      <h3>Junina da Lagoa</h3>
    </div>
    <div class="body">
      <span class="datebar">🗓️ June 6 &amp; 7</span>
      <p>A curated, modern, <b>carioca-chic</b> arraiá right by the Lagoa Rodrigo de Freitas — one of
       Rio’s most beautiful postcards, with the mountains and Christ the Redeemer in the backdrop.
       Think gourmet festa junina food, craft drinks, live music, family-friendly daytime and a lively
       evening, all wrapped in gorgeous, photogenic décor. <span class="hl">Perfect for first-timers</span>
       who want festa vibes <i>and</i> a stunning Rio view.</p>
      <div class="tagrow"><span class="tag">🌅 Postcard lakeside setting</span><span class="tag">🍽️ Gourmet festa food</span><span class="tag">📸 Very photogenic</span><span class="tag">👨‍👩‍👧 Family-friendly</span></div>
      <div class="note" style="margin-top:6px;">📌 <span class="tip">Our tip:</span> arrive around 5pm —
       sunset over the Lagoa is unreal. Pair it with a stroll or bike loop around the lake. 🚲</p></div>
    </div>
  </div>

  <div class="festa g3" style="margin-top:13px;">
    <div class="top"><span class="num">03</span>
      <div class="pin">📍 Shopping Nova América · Del Castilho</div>
      <h3>Arraiá Raiz</h3>
    </div>
    <div class="body">
      <span class="datebar">🗓️ June 3 → 7</span>
      <p>The easy, comfortable, <b>weather-proof</b> option at Shopping Nova América in the North Zone.
       Covered and family-friendly, with loads of food stalls, quadrilha shows, kids’ activities and
       live forró. <span class="hl">Ideal if it rains</span>, if you’re travelling with kids, or if you
       just want all the festa fun with easy metro access (Del Castilho station).</p>
      <div class="tagrow"><span class="tag">☔ Covered / rain-proof</span><span class="tag">🚇 Easy metro access</span><span class="tag">🧒 Great with kids</span><span class="tag">🍢 Lots of food stalls</span></div>
      <div class="note" style="margin-top:6px;">📌 <span class="tip">Our tip:</span> the most relaxed of
       the three — metro Del Castilho drops you right by it. A safe, simple win on a rainy June day. ✍️
       <i>Mark which festa is YOUR #1.</i></p></div>
    </div>
  </div>
</div>
{foot("05")}'''
pages.append(page(p6,"gingham"))

# ---- PAGE 7: MIDDLE CTA / bridge ----
p7 = f'''{stars_html(55)}
{bunting(18)}
<div class="pad">
  <div class="kicker">Now here’s the catch… 🤔</div>
  <h2 class="sec">YOU’VE GOT THE<br>WHERE. BUT NOT<br>THE WHEN, THE HOW,<br>OR THE “TONIGHT”.</h2>
  <p>Knowing a festa <i>exists</i> is step one. But the questions that actually make or break your
   night don’t live in a PDF:</p>
  <ul class="benefits" style="margin:6px 0 10px;">
    <li><span class="bi">🌧️</span><span>Did today’s weather just kill the Lagoa plan — or is it perfect?</span></li>
    <li><span class="bi">🌙</span><span>Which night at São Cristóvão actually has the best forró this week?</span></li>
    <li><span class="bi">👕</span><span>What do I wear so I fit in instead of standing out?</span></li>
    <li><span class="bi">🚕</span><span>How do I get home safe at 1am — and not overpay for it?</span></li>
    <li><span class="bi">🍢</span><span>What do I order, and what’s a tourist trap dressed up as “authentic”?</span></li>
  </ul>
  <p class="big">That’s <b>real-time local context</b> — and Google, TikTok and a blog from 2019 simply
   can’t give it to you while you’re standing there deciding. <span class="hl">But a real carioca can.</span></p>
  <div class="glasscard" style="margin:14px 0;">
    <p style="color:#fff;margin:0;font-size:11.5pt;">That’s literally what we do, every single day — a
    born-and-raised carioca and his wife, answering your questions in English, in real time, so you make
    the right call <i>before</i> the mistake, not after.</p>
  </div>
  {cta("Keep us in your pocket all June — $19.99","Real-time Rio guidance · 30 days · normally $35",big=True,theme="yellow")}
  <div class="cta-foot" style="color:#cfd8ef;">↑ This is your halfway nudge. The full story’s on the next pages. 👇</div>
</div>
{foot("06")}'''
pages.append(page(p7,"dark"))

# ---- PAGE 8: meet the couple ----
p8 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">Quem é que tá falando? 👋</div>
  <h2 class="sec alt">MEET VITOR<br>&amp; ISHA</h2>
  <p class="big">We’re a real Rio couple — and Rio is our actual home, not a backdrop.</p>
  <div class="card" style="margin:6px 0 12px;border-color:#bfe0c9;">
    <h3><span class="emoji">🇧🇷</span>Vitor — born &amp; raised carioca</h3>
    <p>I was born and raised in Rio and studied Social Sciences at UFF, with a background in
     anthropology. So I don’t just know this city — I understand how it <i>works</i>: its
     neighborhoods, its rhythms, and the unwritten rules tourists never get told. Reading a culture
     from the inside is literally what I was trained to do.</p>
  </div>
  <div class="card" style="margin:0 0 14px;border-color:#bfe0c9;">
    <h3><span class="emoji">🍀</span>Isha — Irish, and once a newcomer too</h3>
    <p>My wife is Irish and spent years exploring Rio and researching its local culture. She knows
     exactly where the city confuses foreigners — because she once arrived as one. She’s the bridge
     between “real carioca knowledge” and “what a visitor actually needs to hear.”</p>
  </div>
  <p>That mix is the whole point: a carioca who reads Rio like a researcher, plus an insider-outsider
   who speaks your language and remembers what it’s like to land here without the codes.</p>
  <div class="note" style="margin-top:8px;">✨ <span class="tip">This is not</span> a static PDF, a generic
   guide, or influencer hype. It’s <b>real-time Rio guidance in English</b>, inside a private VIP group
   where we drop daily updates and answer your private questions anytime. <b>Real locals. Real Rio.
   Real-time support.</b></p></div>
</div>
{foot("07")}'''
pages.append(page(p8,"gingham"))

# ---- PAGE 9: what you get + seasonal bonus ----
benefits = "".join([
 '<li><span class="bi">🥳</span><span><b>Never waste a night on a dead party.</b> We tell you which parties are worth it tonight — and which “famous” ones aren’t.</span></li>',
 '<li><span class="bi">🏖️</span><span><b>The right beach, every time.</b> Copa, Ipanema, Leblon, Barra, Prainha, hidden corners — chosen for the weather, crowd, safety and your style.</span></li>',
 '<li><span class="bi">🛟</span><span><b>Real safety orientation</b> — not paranoia. Practical local context so you move smart, not scared.</span></li>',
 '<li><span class="bi">🚕</span><span><b>Stop overpaying &amp; getting lost.</b> Uber vs metro vs walking, smart nightlife return routes, the assumptions that cost tourists money.</span></li>',
 '<li><span class="bi">🍽️</span><span><b>Eat where locals eat.</b> Skip tourist prices for average food — get the real spots.</span></li>',
 '<li><span class="bi">🌅</span><span><b>Sunsets, hikes &amp; viewpoints worth it.</b> What to see, when to go, what to skip.</span></li>',
 '<li><span class="bi">🎉</span><span><b>Free events, festivals &amp; culture.</b> Rio always has something on — we tell you what’s actually worth your time.</span></li>',
 '<li><span class="bi">🇧🇷</span><span><b>Basic Portuguese, when you need it,</b> plus 🚨 emergency orientation and 🔥 24/7 private support — ask anything, anytime.</span></li>',
]
)
p9 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">Here’s what you actually get 🎁</div>
  <h2 class="sec">INSIDE THE VIP</h2>
  <ul class="benefits">{benefits}</ul>
  <div class="price" style="margin-top:8px;border-color:var(--orange);box-shadow:0 8px 0 rgba(255,122,24,.18);background:linear-gradient(180deg,#fff,#fff1cf);">
    <div class="tinycaps" style="color:var(--fire);">⭐ Limited seasonal bonus · now → August ⭐</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;text-align:left;margin-top:8px;">
      <div><div style="font-weight:900;color:var(--green-deep);font-size:11pt;">🌽 Festa Junina</div>
        <p style="font-size:9.4pt;margin:3px 0 0;">June is festival season (Santo Antônio, São João, São Pedro). We show you where the <i>real</i> festas are, what to eat, what to wear, and how to live it like a carioca — not a confused tourist on the outside.</p></div>
      <div><div style="font-weight:900;color:var(--blue);font-size:11pt;">⚽ The World Cup, Rio-style</div>
        <p style="font-size:9.4pt;margin:3px 0 0;">Matches are in North America — but the party is right here. When Brazil plays (Jun 13 vs Morocco, Jun 19 vs Haiti, Jun 24 vs Scotland &amp; beyond), the city turns green &amp; gold. We tell you exactly where to watch for the best atmosphere.</p></div>
    </div>
    <p style="font-size:9pt;margin:9px 0 0;color:var(--fire);font-weight:700;">These two topics close in August. Join now to get them included — at no extra cost.</p>
  </div>
  {cta("Join now &amp; unlock both bonus topics — $19.99","Festa Junina 🌽 + World Cup ⚽ included until August",theme="green")}
</div>
{foot("08")}'''
pages.append(page(p9))

# ---- PAGE 10: before/after + price + faq ----
p10 = f'''{bunting(18)}
<div class="pad">
  <div class="kicker">Same city. Different trip. 🔁</div>
  <h2 class="sec alt" style="font-size:26pt;">BEFORE vs AFTER</h2>
  <div class="ba">
    <div class="col before"><h4>😵‍💫 Before</h4>
      <p>You guess. You overthink.</p><p>You ask random people.</p>
      <p>You trust outdated advice.</p><p>You worry if an area is okay.</p>
      <p>You choose based on TikTok.</p><p>You move like a tourist — reacting too late.</p></div>
    <div class="col after"><h4>😎 After</h4>
      <p>You ask <i>before</i> the mistake.</p><p>You know what’s happening today.</p>
      <p>You feel the vibe before you go.</p><p>You skip the obvious traps.</p>
      <p>You make clearer transport calls.</p><p>You move with real local advantage.</p></div>
  </div>
  <div class="price" style="margin-top:14px;">
    <div class="tinycaps">Today’s opening offer</div>
    <div class="was">normally $35 / month</div>
    <div class="now">$19.99 <small>/ 30 days</small></div>
    <div class="term">Opening price — limited spots</div>
    <ul class="checks" style="columns:2;">
      <li>30 days inside the VIP support</li><li>Daily Rio updates</li>
      <li>Questions answered in English</li><li>Beach, nightlife &amp; food guidance</li>
      <li>Safety &amp; transport context</li><li>🌽 Festa Junina + ⚽ World Cup bonus</li>
      <li>No hidden subscription</li><li>No automatic card renewal</li>
    </ul>
  </div>
  <div class="faq">
    <div class="q">Is it really all in English?</div><p class="a">Yes — everything, every day.</p>
    <div class="q">What platform is it?</div><p class="a">A private Telegram group. You get instant access right after checkout.</p>
    <div class="q">Will I be charged again automatically?</div><p class="a">No. There’s no auto-renewal — we notify you before your 30 days end, and continuing is your choice.</p>
  </div>
</div>
{foot("09")}'''
pages.append(page(p10,"gingham"))

# ---- PAGE 11: FINAL CTA ----
p11 = f'''{stars_html(60)}
{bunting(20)}
<div class="cover-scene" style="height:80mm;">{BONFIRE}</div>
<div class="pad" style="text-align:center;display:flex;flex-direction:column;align-items:center;">
  <div class="kicker" style="color:var(--yellow);">The one thing I promised you… 🔑</div>
  <h2 class="sec" style="color:#fff;text-shadow:2px 2px 0 var(--fire);font-size:30pt;">STOP GUESSING.<br>START LIVING RIO<br>THE RIGHT WAY.</h2>
  <p style="color:#e7eefc;max-width:150mm;font-size:12pt;">Here it is — the thing that separates surviving
   Rio from living it: <b style="color:#fff;">having real locals guiding you while you’re actually here.</b>
   Not fear. Not generic advice. Not bots. Just two real cariocas, in your pocket, every day of your trip.</p>
  <div class="glasscard" style="margin:10px 0 6px;max-width:150mm;">
    <p style="color:#fff;margin:0;font-size:11pt;">Be rational for one second: <b>$19.99 is less than one
     average dinner.</b> One wrong Uber. One overpriced tourist drink. One bad party entrance. But this
     support protects your <i>entire</i> trip — with clarity, local context and real humans.</p>
  </div>
  <div style="width:100%;max-width:150mm;">
    {cta("👉 JOIN RIO VIP INSIDER SUPPORT","Instant Telegram access · $19.99 for 30 days · 48h no-drama refund",big=True,theme="yellow")}
  </div>
  <div class="cta-foot" style="color:#cfd8ef;font-size:12pt;margin-top:6px;">
    Instant access · Real support · Better decisions · Peace of mind</div>
  <p style="color:#fff;font-family:'Patrick Hand',cursive;font-size:18pt;margin-top:14px;">See you inside. 🇧🇷✨</p>
  <p style="color:#9fb0d8;font-size:8.6pt;margin-top:2px;">Try it with zero risk — if it’s not for you in your
   first 48 hours, message us and we’ll refund you. Spots are capped so we can answer personally;
   seasonal bonuses close in August.</p>
</div>
<div class="cover-foot">Real Cariocas in Your Pocket 🇧🇷 · hiddenrio.gumroad.com/l/liveriolikealocal</div>'''
pages.append(page(p11,"dark"))

HTML = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<style>{FONTS}{CSS}</style></head><body>{''.join(pages)}</body></html>"""

pathlib.Path("/home/claude/festa.html").write_text(HTML, encoding="utf-8")
print("HTML written:", len(HTML), "bytes;", len(pages), "pages")
