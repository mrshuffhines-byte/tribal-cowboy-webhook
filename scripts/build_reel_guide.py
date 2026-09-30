import base64, re, subprocess, sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from reel_guide_pages import PAGES, LOOP

OUT_DIR = Path.home() / "Documents/Claude Yap Edits ready to edit/Yap Edits files"
OUT = OUT_DIR / "How to make a reel.pdf"
TMP = Path("/tmp/reel-guide"); TMP.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def logo_b64():
    skill = next(Path.home().glob(".claude/skills/synced/*/tribal-cowboy-brand/SKILL.md"))
    m = re.search(r'TRIBAL_COWBOY_LOGO_B64 = "([^"]+)"', skill.read_text())
    return m.group(1)

# ---------- SVG pictures: simplified drawings of the real screens ----------
GOLD, CREAM, TIMBER, TEAL, LEATHER, MUTED = "#D4A843", "#F3EDE3", "#2C2520", "#1A7A6B", "#C8A96E", "#8A7560"

def svg(inner, w=520, h=300):
    return f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Montserrat, sans-serif">{inner}</svg>'

def window(x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFCF7" stroke="#E0D6C8"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="8" fill="#EDE5D8"/>'
            f'<circle cx="{x+14}" cy="{y+13}" r="4" fill="#E06B5B"/><circle cx="{x+28}" cy="{y+13}" r="4" fill="#E9B94E"/><circle cx="{x+42}" cy="{y+13}" r="4" fill="#6CC070"/>'
            f'<text x="{x+w/2}" y="{y+17}" font-size="10" fill="{MUTED}" text-anchor="middle">{title}</text>')

def pic_film():
    return svg(
        f'<rect x="200" y="30" width="120" height="240" rx="18" fill="{TIMBER}"/>'
        f'<rect x="210" y="45" width="100" height="210" rx="8" fill="#5A4A3A"/>'
        f'<circle cx="260" cy="120" r="26" fill="{LEATHER}"/><path d="M225 200 Q260 150 295 200 Z" fill="{LEATHER}"/>'
        f'<line x1="260" y1="60" x2="260" y2="88" stroke="{GOLD}" stroke-width="3" stroke-dasharray="4 3"/>'
        f'<text x="335" y="70" font-size="12" fill="{TIMBER}">a hand of space</text><text x="335" y="88" font-size="12" fill="{TIMBER}">above your head</text>'
        f'<text x="40" y="150" font-size="12" fill="{TIMBER}">window or open sky</text><text x="40" y="168" font-size="12" fill="{TIMBER}">on this side of you</text>'
        f'<path d="M150 155 L195 140" stroke="{GOLD}" stroke-width="3" fill="none"/><path d="M185 133 L197 139 L188 147" stroke="{GOLD}" stroke-width="3" fill="none"/>'
        f'<text x="335" y="230" font-size="12" fill="{TIMBER}">say the hook first</text><text x="335" y="248" font-size="12" fill="{TIMBER}">keep rolling if you mess up</text>')

def pic_folder():
    rows = [("Assets", True), ("Edited", True), ("Yap Edits files", True), ("IMG_8795.mov  ← talking reel", False), ("belle-birthday  ← voice over subfolder", True)]
    items = "".join(
        f'<rect x="70" y="{70+i*36}" width="26" height="20" rx="3" fill="{"#7FB3D5" if f else "#BFB3A3"}"/>'
        f'<text x="108" y="{85+i*36}" font-size="13" fill="{TIMBER}">{t}</text>' for i, (t, f) in enumerate(rows))
    return svg(window(40, 20, 440, 260, "Claude Yap Edits ready to edit") + items +
               f'<text x="465" y="258" font-size="11" text-anchor="end" fill="{TEAL}">inside belle-birthday: 5 clips + voice.m4a</text>')

def pic_claude():
    return svg(window(30, 15, 460, 270, "Claude · Yap Edits Reel Editor") +
        f'<rect x="60" y="60" width="400" height="70" rx="10" fill="#F6F1EA" stroke="#E0D6C8"/>'
        f'<text x="75" y="85" font-size="11" fill="{TIMBER}">Please request access to my folder called</text>'
        f'<text x="75" y="102" font-size="11" fill="{TIMBER}">"Claude Yap Edits ready to edit" in Documents...</text>'
        f'<rect x="60" y="145" width="400" height="80" rx="10" fill="#EEF7F5" stroke="{TEAL}"/>'
        f'<text x="75" y="168" font-size="11" fill="{TEAL}">I found IMG_8795.mov (48 s). Three questions:</text>'
        f'<text x="75" y="186" font-size="11" fill="{TIMBER}">Which type: A talking, B voice over, C highlight, D trend?</text>'
        f'<text x="75" y="202" font-size="11" fill="{TIMBER}">How long: under 30 s, 30 to 60 s, 60 to 90 s?  Setting?</text>'
        f'<rect x="60" y="238" width="60" height="22" rx="11" fill="#E8E1D6"/><text x="90" y="253" font-size="10" text-anchor="middle" fill="{MUTED}">Chat</text>'
        f'<rect x="124" y="238" width="70" height="22" rx="11" fill="{TEAL}"/><text x="159" y="253" font-size="10" text-anchor="middle" fill="#fff">Cowork ✓</text>'
        f'<text x="210" y="253" font-size="11" fill="{TIMBER}">you type:  A, under 30 s, outdoor</text>')

def pic_review():
    return svg(
        f'<rect x="60" y="20" width="130" height="260" rx="14" fill="{TIMBER}"/>'
        f'<rect x="72" y="60" width="106" height="20" rx="4" fill="{CREAM}"/><text x="125" y="74" font-size="9" text-anchor="middle" fill="{TIMBER}">Belle at 22</text>'
        f'<circle cx="125" cy="130" r="22" fill="{LEATHER}"/><path d="M95 200 Q125 160 155 200 Z" fill="{LEATHER}"/>'
        f'<rect x="80" y="175" width="34" height="12" rx="2" fill="#fff"/><text x="97" y="184" font-size="8" text-anchor="middle" fill="{TIMBER}">still</text>'
        f'<rect x="90" y="240" width="70" height="20" rx="10" fill="{GOLD}"/><text x="125" y="254" font-size="9" text-anchor="middle" fill="#1E1208">Follow along</text>'
        f'<text x="220" y="70" font-size="13" fill="{TIMBER}">Watch it twice</text>'
        f'<text x="220" y="92" font-size="12" fill="{MUTED}">1. with sound   2. muted</text>'
        f'<text x="220" y="130" font-size="13" fill="{TIMBER}">Tell Claude what to change, like a friend</text>'
        f'<text x="220" y="152" font-size="12" fill="{MUTED}">"captions a little left"  "fewer zooms"</text>'
        f'<text x="220" y="190" font-size="13" fill="{TIMBER}">Keep the good changes</text>'
        f'<text x="220" y="212" font-size="12" fill="{MUTED}">paste the rule into My Rules.md</text>')

def pic_schedule():
    return svg(window(30, 15, 460, 255, "Terminal · Claude Code · TribalCowboy Social") +
        f'<text x="55" y="60" font-size="12" fill="{TEAL}" font-family="Menlo, monospace">&gt; /schedule-reel</text>'
        f'<text x="55" y="88" font-size="11" fill="{TIMBER}">Picked Edited/2026-10-03-belle-at-22/render.mp4 (type A)</text>'
        f'<text x="55" y="108" font-size="11" fill="{TIMBER}">Caption: Belle had opinions about breakfast this morning...</text>'
        f'<text x="55" y="128" font-size="11" fill="{TIMBER}">Copied to Dropbox. Paste the Dropbox link:</text>'
        f'<text x="55" y="156" font-size="11" fill="{TIMBER}">Best hour: Saturday 6 pm (Instagram)   Networks: IG, FB, TikTok</text>'
        f'<rect x="55" y="180" width="410" height="60" rx="8" fill="#FAF4EA" stroke="{GOLD}"/>'
        f'<text x="70" y="203" font-size="12" fill="{TIMBER}">Schedule this?  yes / change something / draft only</text>'
        f'<text x="70" y="226" font-size="12" fill="{TEAL}" font-family="Menlo, monospace">&gt; yes</text>' +
        f'<rect x="30" y="288" width="300" height="30" rx="6" fill="#E8F0FA" stroke="#B7C9E2"/>'
        f'<text x="42" y="307" font-size="10.5" fill="{TIMBER}">Tribal Cowboy Reels › 2026-10-03-belle-at-22.mp4</text>'
        f'<rect x="342" y="280" width="148" height="62" rx="6" fill="#FFFFFF" stroke="#CFC5B5"/>'
        f'<text x="352" y="298" font-size="10" fill="{MUTED}">Open</text>'
        f'<rect x="344" y="306" width="144" height="18" fill="{TEAL}"/><text x="352" y="319" font-size="10" fill="#fff">Copy Dropbox Link</text>'
        f'<text x="352" y="336" font-size="10" fill="{MUTED}">Move to trash</text>', h=350)

def pic_terminal_weekly():
    mono = 'font-family="Menlo, monospace"'
    return svg(window(30, 15, 460, 270, "Terminal · Claude Code · TribalCowboy Social") +
        f'<text x="55" y="58" font-size="12" fill="{TEAL}" {mono}>&gt; /reel-report</text>'
        f'<text x="55" y="80" font-size="10.5" fill="{TIMBER}">4 reels in 30 days. Top: Belle at 22 (45% held past 3 s)</text>'
        f'<text x="55" y="98" font-size="10.5" fill="{TIMBER}">Pattern: reels that open with a horse&#39;s name held better</text>'
        f'<text x="55" y="122" font-size="10.5" fill="{TIMBER}">PROPOSED: open with the horse&#39;s name in the first line.</text>'
        f'<text x="55" y="138" font-size="10.5" fill="{TIMBER}">Add it? yes / no</text>'
        f'<text x="55" y="188" font-size="12" fill="{TEAL}" {mono}>&gt; /trend-brief</text>'
        f'<text x="55" y="210" font-size="10.5" fill="{TIMBER}">3 ideas saved to content/trends.</text>'
        f'<text x="55" y="228" font-size="10.5" fill="{TIMBER}">Which one do you want to film first?</text>')

def pic_weekly():
    cx, cy, r = 260, 150, 105
    n = len(LOOP)
    dots = ""
    for i, label in enumerate(LOOP):
        a = -math.pi/2 + 2*math.pi*i/n
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="{GOLD}"/><text x="{x:.0f}" y="{y+4:.0f}" font-size="10" text-anchor="middle" fill="#1E1208" font-weight="700">{i+1}</text>'
        lx, ly = cx + (r+40)*math.cos(a), cy + (r+40)*math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < 0.3 else ("start" if math.cos(a) > 0 else "end")
        dots += f'<text x="{lx:.0f}" y="{ly+4:.0f}" font-size="12" text-anchor="{anchor}" fill="{TIMBER}">{label}</text>'
    return svg(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LEATHER}" stroke-width="3" stroke-dasharray="6 6"/>' + dots)

PICS = dict(film=pic_film, folder=pic_folder, claude=pic_claude, review=pic_review, schedule=pic_schedule, weekly=pic_weekly, terminal_weekly=pic_terminal_weekly)

# ---------- HTML ----------
CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Montserrat:wght@400;500;600;700&display=swap');
@page {{ size: 8.5in 11in; margin: 0; }}
* {{ box-sizing: border-box; }} html, body {{ margin:0; background:{CREAM}; }}
body {{ font-family:'Montserrat',sans-serif; color:#574838; font-size:11.5pt; line-height:1.75; }}
.page {{ width:8.5in; height:11in; position:relative; overflow:hidden; page-break-after:always; }}
.page:last-child {{ page-break-after:auto; }}
.header {{ background:{TIMBER}; height:0.7in; display:flex; align-items:center; justify-content:space-between; padding:0 0.6in; }}
.header img {{ height:0.55in; width:0.55in; object-fit:contain; background:#fff; border-radius:4px; }}
.header .label {{ color:{GOLD}; font-weight:700; font-size:9pt; letter-spacing:0.18em; text-transform:uppercase; }}
.body {{ padding:0.45in 0.7in 0; }}
.num {{ width:0.9in; height:0.9in; border-radius:50%; background:{GOLD}; color:#1E1208; font-weight:700; font-size:34pt; display:flex; align-items:center; justify-content:center; float:left; margin:0 0.3in 0.2in 0; }}
h1 {{ font-family:'Cormorant Garamond',serif; font-weight:500; font-size:34pt; color:{TIMBER}; margin:0.05in 0 0 0; line-height:1.05; }}
.one {{ font-family:'Cormorant Garamond',serif; font-size:17pt; color:{MUTED}; margin:0 0 0.2in 0; line-height:1.3; clear:none; }}
.pic {{ clear:both; background:#FFFCF7; border:0.5px solid #E8DFD0; border-radius:4px; box-shadow:0 4px 14px rgba(0,0,0,0.10); padding:0.15in; margin:0.1in 0 0.2in 0; }}
.checks {{ list-style:none; margin:0 0 0.15in 0; padding:0; }}
.checks li {{ position:relative; padding:0.06in 0 0.06in 0.45in; font-size:13pt; color:{TIMBER}; font-weight:500; }}
.checks li:before {{ content:''; position:absolute; left:0; top:0.13in; width:0.22in; height:0.22in; border:2px solid {GOLD}; border-radius:4px; }}
.say {{ border-left:4px solid {TEAL}; background:#EEF7F5; padding:0.15in 0.22in; font-size:11pt; color:{TIMBER}; }}
.say .lab {{ display:block; color:{TEAL}; font-weight:700; font-size:8pt; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:4px; }}
.map h1 {{ text-align:center; margin-top:0.2in; }}
.map .one {{ text-align:center; }}
.map .pic {{ margin-top:0.2in; }}
.map .legend {{ display:grid; grid-template-columns:1fr 1fr; gap:0.08in 0.4in; margin-top:0.25in; font-size:12pt; color:{TIMBER}; }}
.map .legend b {{ color:{GOLD}; font-weight:700; margin-right:6px; }}
.footer {{ position:absolute; bottom:0.3in; left:0.7in; right:0.7in; border-top:1px solid #E0D6C8; padding-top:8px; display:flex; justify-content:space-between; font-size:8.5pt; color:{MUTED}; font-weight:500; }}
"""

def page_html(logo, p):
    return f"""<div class="page"><div class="header"><img src="data:image/jpeg;base64,{logo}"><div class="label">How to make a reel · step {p['num']} of 6</div></div>
<div class="body"><div class="num">{p['num']}</div><h1>{p['title']}</h1><div class="one">{p['one']}</div>
<div class="pic">{PICS[p['picture']]()}</div>
<ul class="checks">{''.join(f'<li>{c}</li>' for c in p['checklist'])}</ul>
<div class="say"><span class="lab">What you say to Claude</span>{p['say']}</div></div>
<div class="footer"><span>www.tribalcowboy.com</span><span>From the Ranch · Yap Edits × Tribal Cowboy</span><span>info@tribalcowboy.com</span></div></div>"""

def map_html(logo):
    legend = "".join(f'<div><b>{i+1}</b>{l}</div>' for i, l in enumerate(LOOP))
    return f"""<div class="page map"><div class="header"><img src="data:image/jpeg;base64,{logo}"><div class="label">How to make a reel · the loop</div></div>
<div class="body"><h1>One loop. Seven stops.</h1><div class="one">Film it, drop it, answer three questions, watch it, say yes. Monday tells you what to film next.</div>
<div class="pic">{pic_weekly()}</div><div class="legend">{legend}</div></div>
<div class="footer"><span>www.tribalcowboy.com</span><span>From the Ranch · Yap Edits × Tribal Cowboy</span><span>info@tribalcowboy.com</span></div></div>"""

# Each .page has a fixed height with overflow hidden, so a long page never adds a PDF page.
# This script measures in the browser instead and flags any page whose content reaches its footer.
CHECK_JS = """<script>window.addEventListener('load',function(){var bad=0;
document.querySelectorAll('.page').forEach(function(pg){var b=pg.querySelector('.body').getBoundingClientRect().bottom;
var f=pg.querySelector('.footer').getBoundingClientRect().top;if(b>f-12){bad++;}});
document.body.setAttribute('data-overflow',String(bad));});</script>"""

def build():
    logo = logo_b64()
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>How to make a reel</title><style>{CSS}</style></head><body>" + map_html(logo) + "".join(page_html(logo, p) for p in PAGES) + CHECK_JS + "</body></html>"
    (TMP / "guide.html").write_text(html)
    dom = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=8000", "--dump-dom",
                          f"file://{TMP/'guide.html'}"], check=True, capture_output=True, text=True).stdout
    m = re.search(r'data-overflow="(\d+)"', dom)
    if not m or int(m.group(1)) > 0:
        raise SystemExit(f"a page overflowed: {m.group(1) if m else 'unknown'} page(s) run into the footer")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={TMP/'guide.pdf'}", f"file://{TMP/'guide.html'}"], check=True, capture_output=True)
    info = subprocess.run(["pdfinfo", str(TMP / "guide.pdf")], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    if pages != 7:
        raise SystemExit(f"expected 7 pages, got {pages}; a page overflowed")
    OUT.write_bytes((TMP / "guide.pdf").read_bytes())
    subprocess.run(["pdftoppm", "-jpeg", "-r", "70", str(OUT), str(TMP / "preview")], check=True)
    print("built", OUT, "previews in", TMP)

if __name__ == "__main__":
    build()
