"""
Tribal Cowboy Rodeo Photography Field Guide
Canon R5 Mark II Edition — ADHD-Friendly PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas as pdfcanvas
import os

# ─────────────────────────────────────────────
# COLOR PALETTE  (western-inspired)
# ─────────────────────────────────────────────
DARK_BROWN   = colors.HexColor("#2C1A0E")
BURNT_ORANGE = colors.HexColor("#C4520A")
GOLD         = colors.HexColor("#D4A017")
CREAM        = colors.HexColor("#FAF3E0")
TEAL         = colors.HexColor("#1A7A6E")
CRIMSON      = colors.HexColor("#8B1A1A")
DUSTY_BLUE   = colors.HexColor("#2B5F8E")
SAGE         = colors.HexColor("#5C7A4E")
LIGHT_CREAM  = colors.HexColor("#FDF8F0")
MID_BROWN    = colors.HexColor("#6B3F1F")
PALE_ORANGE  = colors.HexColor("#FDEBD0")
PALE_TEAL    = colors.HexColor("#D0EFEB")
PALE_CRIMSON = colors.HexColor("#F5D5D5")
PALE_GOLD    = colors.HexColor("#FDF3C8")
PALE_BLUE    = colors.HexColor("#D0E4F5")
PALE_SAGE    = colors.HexColor("#D8EAD4")
WHITE        = colors.white
BLACK        = colors.black

W, H = letter

OUTPUT_PATH = os.path.expanduser("~/Desktop/TribalCowboy_Rodeo_Guide_R5II.pdf")

# ─────────────────────────────────────────────
# CUSTOM FLOWABLES
# ─────────────────────────────────────────────
class ColorBar(Flowable):
    """Full-width colored header bar with text."""
    def __init__(self, text, bg=BURNT_ORANGE, fg=WHITE, height=36, fontsize=16):
        self.text = text
        self.bg = bg
        self.fg = fg
        self.bar_height = height
        self.fontsize = fontsize
        self.width = 0
        self.height = height + 4

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.rect(0, 0, self.width, self.bar_height, fill=1, stroke=0)
        c.setFillColor(self.fg)
        c.setFont("Helvetica-Bold", self.fontsize)
        c.drawString(10, self.bar_height / 2 - self.fontsize / 3, self.text)


class SectionBox(Flowable):
    """Colored rounded-corner info box."""
    def __init__(self, label, items, bg=PALE_ORANGE, accent=BURNT_ORANGE, width=None):
        self.label = label
        self.items = items  # list of strings
        self.bg = bg
        self.accent = accent
        self._width = width
        self.width = 0
        self.height = 0

    def wrap(self, availWidth, availHeight):
        self.width = self._width or availWidth
        line_h = 14
        self.height = 26 + len(self.items) * line_h + 8
        return self.width, self.height

    def draw(self):
        c = self.canv
        # background
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.width, self.height, 6, fill=1, stroke=0)
        # accent left bar
        c.setFillColor(self.accent)
        c.rect(0, 0, 5, self.height, fill=1, stroke=0)
        # label
        c.setFillColor(self.accent)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(12, self.height - 18, self.label)
        # items
        c.setFillColor(DARK_BROWN)
        c.setFont("Helvetica", 9)
        y = self.height - 30
        for item in self.items:
            c.drawString(16, y, item)
            y -= 14


class Pill(Flowable):
    """Small colored pill badge."""
    def __init__(self, text, bg=TEAL, fg=WHITE):
        self.text = text
        self.bg = bg
        self.fg = fg
        self.width = 0
        self.height = 18

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return self.width, self.height

    def draw(self):
        c = self.canv
        tw = len(self.text) * 6.5 + 16
        c.setFillColor(self.bg)
        c.roundRect(0, 2, tw, 14, 7, fill=1, stroke=0)
        c.setFillColor(self.fg)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(8, 5, self.text)


# ─────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────
def build_styles():
    s = getSampleStyleSheet()

    def add(name, **kw):
        s.add(ParagraphStyle(name=name, **kw))

    add("TCTitle",    fontName="Helvetica-Bold",  fontSize=36, textColor=WHITE,
        alignment=TA_CENTER, leading=42, spaceAfter=6)
    add("TCSubtitle", fontName="Helvetica",        fontSize=14, textColor=GOLD,
        alignment=TA_CENTER, leading=18, spaceAfter=4)
    add("TCTagline",  fontName="Helvetica-Oblique",fontSize=11, textColor=CREAM,
        alignment=TA_CENTER, leading=14)

    add("SectionHead", fontName="Helvetica-Bold", fontSize=18,
        textColor=BURNT_ORANGE, leading=22, spaceBefore=14, spaceAfter=4)
    add("SubHead",     fontName="Helvetica-Bold", fontSize=13,
        textColor=DARK_BROWN,   leading=16, spaceBefore=8,  spaceAfter=3)
    add("SubHead2",    fontName="Helvetica-Bold", fontSize=11,
        textColor=MID_BROWN,    leading=14, spaceBefore=6,  spaceAfter=2)

    add("Body",   fontName="Helvetica", fontSize=9, textColor=DARK_BROWN,
        leading=13, spaceAfter=3)
    add("TCBullet", fontName="Helvetica", fontSize=9, textColor=DARK_BROWN,
        leading=13, spaceAfter=2, leftIndent=14, firstLineIndent=-10)
    add("BulletBold", fontName="Helvetica-Bold", fontSize=9, textColor=DARK_BROWN,
        leading=13, spaceAfter=2, leftIndent=14, firstLineIndent=-10)
    add("Note",   fontName="Helvetica-Oblique", fontSize=8, textColor=MID_BROWN,
        leading=11, spaceAfter=2)
    add("CenterSmall", fontName="Helvetica", fontSize=8, textColor=MID_BROWN,
        alignment=TA_CENTER, leading=10)
    add("TableHead", fontName="Helvetica-Bold", fontSize=8.5, textColor=WHITE,
        alignment=TA_CENTER, leading=11)
    add("TableCell", fontName="Helvetica", fontSize=8, textColor=DARK_BROWN,
        leading=11)
    add("TableCellBold", fontName="Helvetica-Bold", fontSize=8, textColor=DARK_BROWN,
        leading=11)
    add("WhiteBold", fontName="Helvetica-Bold", fontSize=9, textColor=WHITE,
        leading=12)
    add("EventTier", fontName="Helvetica-Bold", fontSize=10, textColor=WHITE,
        alignment=TA_CENTER, leading=13)
    add("BigStat", fontName="Helvetica-Bold", fontSize=22, textColor=BURNT_ORANGE,
        alignment=TA_CENTER, leading=26)
    add("StatLabel", fontName="Helvetica", fontSize=8, textColor=MID_BROWN,
        alignment=TA_CENTER, leading=10)
    add("FooterText", fontName="Helvetica", fontSize=7, textColor=MID_BROWN,
        alignment=TA_CENTER, leading=9)

    return s

ST = build_styles()

# ─────────────────────────────────────────────
# HELPER BUILDERS
# ─────────────────────────────────────────────
def hr(color=BURNT_ORANGE, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=4)

def sp(h=6):
    return Spacer(1, h)

def p(text, style="Body"):
    return Paragraph(text, ST[style])

def bullet(text, bold=False):
    return Paragraph(f"&#x2022; {text}", ST["BulletBold" if bold else "TCBullet"])

def head(text, level=1):
    styles = {1: "SectionHead", 2: "SubHead", 3: "SubHead2"}
    return Paragraph(text, ST[styles.get(level, "SubHead")])

def make_table(data, col_widths, header_bg=DARK_BROWN, row_colors=None, font_size=8):
    """Build a styled table."""
    if row_colors is None:
        row_colors = [LIGHT_CREAM, CREAM]

    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR",  (0, 0), (-1, 0), WHITE),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0), font_size),
        ("FONTNAME",   (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",   (0, 1), (-1, -1), font_size),
        ("TEXTCOLOR",  (0, 1), (-1, -1), DARK_BROWN),
        ("ALIGN",      (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), row_colors),
        ("GRID",       (0, 0), (-1, -1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle(style_cmds))
    return t


def event_settings_table(rows, accent):
    """Setting | Value | Why table."""
    data = [["SETTING", "VALUE", "WHY"]] + rows
    widths = [1.7*inch, 1.8*inch, 3.0*inch]
    style_cmds = [
        ("BACKGROUND",    (0, 0), (-1, 0), accent),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8.5),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8),
        ("FONTNAME",      (0, 1), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0, 1), (-1, -1), DARK_BROWN),
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [LIGHT_CREAM, CREAM]),
        ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("BACKGROUND",    (1, 1), (1, -1), colors.HexColor("#FDEBD0")),
        ("FONTNAME",      (1, 1), (1, -1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (1, 1), (1, -1), accent),
    ]
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle(style_cmds))
    return t


# ─────────────────────────────────────────────
# PAGE TEMPLATES (header/footer)
# ─────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        # top strip
        canvas.setFillColor(DARK_BROWN)
        canvas.rect(0, H - 28, W, 28, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawString(0.5*inch, H - 18, "TRIBAL COWBOY  |  RODEO FIELD GUIDE")
        canvas.setFillColor(CREAM)
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(W - 0.5*inch, H - 18, f"Canon R5 Mark II  |  Page {doc.page}")
        # bottom strip
        canvas.setFillColor(DARK_BROWN)
        canvas.rect(0, 0, W, 20, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.setFont("Helvetica", 7)
        canvas.drawCentredString(W/2, 6, "tribalcowboy.com  |  North Idaho / Eastern Washington  |  250-Mile Rodeo Radius")
    canvas.restoreState()


# ─────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────
def cover_page(story):
    # Full bleed background via a full-page colored rectangle
    class CoverBG(Flowable):
        def wrap(self, aw, ah):
            return aw, ah
        def draw(self):
            c = self.canv
            # Sky/gradient feel: dark brown top, warm cream bottom
            c.setFillColor(DARK_BROWN)
            c.rect(-0.75*inch, -1*inch, W + inch, H + inch, fill=1, stroke=0)
            # decorative band
            c.setFillColor(BURNT_ORANGE)
            c.rect(-0.75*inch, 3.2*inch, W + inch, 0.18*inch, fill=1, stroke=0)
            c.setFillColor(GOLD)
            c.rect(-0.75*inch, 3.0*inch, W + inch, 0.08*inch, fill=1, stroke=0)
            # bottom band
            c.setFillColor(BURNT_ORANGE)
            c.rect(-0.75*inch, 0.9*inch, W + inch, 0.18*inch, fill=1, stroke=0)
            c.setFillColor(GOLD)
            c.rect(-0.75*inch, 0.78*inch, W + inch, 0.08*inch, fill=1, stroke=0)

    story.append(CoverBG())

    story.append(sp(60))
    story.append(Paragraph("TRIBAL COWBOY", ST["TCTitle"]))
    story.append(Paragraph("RODEO PHOTOGRAPHY", ST["TCTitle"]))
    story.append(sp(8))

    class GoldBar(Flowable):
        def wrap(self, aw, ah):
            return aw, 6
        def draw(self):
            c = self.canv
            c.setFillColor(GOLD)
            c.rect(1*inch, 0, W - 2.5*inch, 4, fill=1, stroke=0)

    story.append(GoldBar())
    story.append(sp(12))
    story.append(Paragraph("CANON EOS R5 MARK II  |  FIELD GUIDE", ST["TCSubtitle"]))
    story.append(sp(6))
    story.append(Paragraph("83801 Careywood, ID  |  250-Mile Radius  |  2026 Edition", ST["TCTagline"]))
    story.append(sp(28))

    # Stats row
    stats = [
        ["5\nEvents\nTier 1", "12+\nRegional\nRodeos", "30fps\nBurst\nRate", "Animal\nAF\nTracking"],
    ]
    stat_style = [
        ("ALIGN",      (0,0), (-1,-1), "CENTER"),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), 15),
        ("TEXTCOLOR",  (0,0), (-1,-1), GOLD),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LINEBEFORE", (1,0), (-1,-1), 1, BURNT_ORANGE),
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#3D2210")),
    ]
    st_t = Table(stats, colWidths=[1.5*inch]*4)
    st_t.setStyle(TableStyle(stat_style))
    story.append(st_t)

    story.append(sp(30))
    story.append(Paragraph(
        "Bull Riding  |  Barrel Racing  |  Calf Roping  |  Team Roping",
        ST["TCTagline"]))
    story.append(sp(4))
    story.append(Paragraph(
        "Lenses  |  Settings  |  Positioning  |  Event Calendar  |  Monetization",
        ST["TCTagline"]))

    story.append(sp(40))
    story.append(Paragraph("Millie  *  Abby  *  Jolene  *  Monster  *  Master Chief", ST["TCTagline"]))
    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 2: QUICK REFERENCE CARD (laminate-style)
# ─────────────────────────────────────────────
def quick_ref_page(story):
    story.append(sp(8))
    story.append(ColorBar("  QUICK REFERENCE  —  GRAB THIS FIRST", bg=DARK_BROWN, fontsize=15))
    story.append(sp(8))

    story.append(p(
        "<b>Before every event:</b> Custom Mode dial  C1 = Bull  |  C2 = Barrel  |  C3 = Crowd/General",
        "Body"))
    story.append(sp(4))

    # Master settings strip
    quick_data = [
        ["EVENT", "SHUTTER", "APERTURE", "ISO AUTO", "AF MODE", "DRIVE", "PRE-SHOT"],
        ["Bull Riding",     "1/2000-3200", "f/4",      "to 12800", "Animal Track", "H+ 30fps", "ON - Max"],
        ["Barrel Racing",   "1/1600 min",  "f/2.8-4",  "to 6400",  "Animal Track", "H+ 30fps", "ON - Med"],
        ["Calf/Team Roping","1/2000",      "f/5.6",    "to 3200",  "Animal Track", "H+ 30fps", "ON - Max"],
        ["General/Crowd",   "1/1250 min",  "f/4",      "to 6400",  "People/Auto",  "H 12fps",  "OFF"],
        ["Night Rodeo",     "1/1000 min",  "f/2.8-4",  "to 12800", "Animal Track", "H 12fps",  "ON"],
    ]
    qstyle = [
        ("BACKGROUND",    (0,0), (-1,0), DARK_BROWN),
        ("TEXTCOLOR",     (0,0), (-1,0), GOLD),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,0), 8),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), DARK_BROWN),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (1,1), (-1,-1), 8),
        ("TEXTCOLOR",     (1,1), (1,-1), CRIMSON),
        ("TEXTCOLOR",     (2,1), (2,-1), DUSTY_BLUE),
        ("TEXTCOLOR",     (3,1), (3,-1), MID_BROWN),
        ("TEXTCOLOR",     (4,1), (4,-1), TEAL),
        ("TEXTCOLOR",     (5,1), (5,-1), SAGE),
        ("TEXTCOLOR",     (6,1), (6,-1), BURNT_ORANGE),
        ("FONTNAME",      (1,1), (6,-1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_ORANGE]),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]
    qt = Table(quick_data, colWidths=[1.3*inch, 0.9*inch, 0.85*inch, 0.8*inch, 1.0*inch, 0.85*inch, 0.8*inch])
    qt.setStyle(TableStyle(qstyle))
    story.append(qt)

    story.append(sp(10))
    story.append(hr(GOLD, 1))

    # Two-column: Night mode warning + shutter mode
    col_l = [
        [ColorBar("  SHUTTER MODE — WHEN", bg=CRIMSON, fontsize=10, height=24)],
        [make_table(
            [["CONDITION", "USE"],
             ["Daylight / LED arena", "Elec. 1st Curtain"],
             ["Night / LED flickering", "MECHANICAL"],
             ["Silent (portraits)", "Electronic"],
             ["Flash use", "Mechanical"],
             ["Not sure", "Mechanical"],],
            [2.2*inch, 1.6*inch], header_bg=CRIMSON,
            row_colors=[LIGHT_CREAM, PALE_CRIMSON])],
    ]
    col_r = [
        [ColorBar("  PRE-SHOT — HOW TO USE", bg=TEAL, fontsize=10, height=24)],
        [make_table(
            [["MOMENT", "PRE-SHOT"],
             ["Bull jump peak", "MAX (30 frames)"],
             ["Rope throw release", "MAX (30 frames)"],
             ["Buck-off", "MAX (30 frames)"],
             ["Barrel turn apex", "MED (15 frames)"],
             ["Crowd / portraits", "OFF"],],
            [2.2*inch, 1.6*inch], header_bg=TEAL,
            row_colors=[LIGHT_CREAM, PALE_TEAL])],
    ]
    two_col = Table([[col_l, col_r]], colWidths=[3.9*inch, 3.9*inch])
    two_col.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("INNERGRID", (0,0), (-1,-1), 0, WHITE),
        ("LINEBETWEEN", (0,0), (0,-1), 0.5, GOLD),
    ]))
    story.append(two_col)

    story.append(sp(8))
    story.append(hr(GOLD, 1))

    # Animal tracking note
    story.append(ColorBar("  ANIMAL TRACKING — THE GAME CHANGER", bg=TEAL, fontsize=11, height=26))
    story.append(sp(4))
    atk = [
        ["SET THIS ONCE AND LEAVE IT", "AF Menu 1 > Subject to Detect > ANIMALS  |  Eye Detection: ENABLE"],
        ["What it does", "Locks onto the horse — eyes, body, movement — through dust and partial occlusion"],
        ["If it grabs wrong animal", "Tap the correct subject on the EVF touchscreen to confirm"],
        ["Tracking sensitivity", "3 = standard  |  4-5 = heavy dust conditions  |  2 = calm predictable runs"],
        ["Works at night?", "YES — Dual Pixel CMOS AF II works down to EV -6"],
    ]
    atk_style = [
        ("BACKGROUND",    (0,0), (0,-1), TEAL),
        ("TEXTCOLOR",     (0,0), (0,-1), WHITE),
        ("FONTNAME",      (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",      (1,0), (1,0), "Helvetica-Bold"),
        ("TEXTCOLOR",     (1,0), (1,0), TEAL),
        ("FONTSIZE",      (0,0), (-1,-1), 8.5),
        ("FONTNAME",      (1,1), (1,-1), "Helvetica"),
        ("TEXTCOLOR",     (1,1), (1,-1), DARK_BROWN),
        ("ALIGN",         (0,0), (0,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,0), (-1,-1), [PALE_TEAL, LIGHT_CREAM]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#AACCCC")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]
    atkt = Table(atk, colWidths=[1.8*inch, 5.9*inch])
    atkt.setStyle(TableStyle(atk_style))
    story.append(atkt)

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 3: BULL RIDING + BARREL RACING SETTINGS
# ─────────────────────────────────────────────
def event_settings_page(story):
    # ── BULL RIDING ──────────────────────────
    story.append(sp(8))
    story.append(ColorBar("  BULL RIDING", bg=CRIMSON, fontsize=16))
    story.append(sp(6))

    br_rows = [
        ["Mode",             "M + Auto ISO",         "Consistent arena light = lock shutter + aperture manually"],
        ["Shutter",          "1/2000 - 1/3200",      "1/3200 for extreme jumps and spins — never go below 1/2000"],
        ["Aperture",         "f/4",                  "DOF buffer for erratic unpredictable movement"],
        ["ISO Auto Max",     "12800",                "Push it — R5 II handles high ISO cleanly"],
        ["AF Operation",     "Servo AF",             "ALWAYS — never One Shot in the arena"],
        ["Subject Detect",   "ANIMALS",              "Locks on the bull — tracks through dust and spin"],
        ["Eye Detection",    "ENABLE",               "Will find the bull's eye through haze"],
        ["Tracking Sens.",   "3-4",                  "Bump to 4 in heavy dust to hold lock"],
        ["AF Zone",          "Whole Area",           "Let subject detection find the bull — don't override"],
        ["Drive Mode",       "H+ (30fps Electronic)","More frames = more peak moments captured"],
        ["Pre-Shot",         "ON — MAX (30 frames)", "Captures the jump before your brain fires the shutter"],
        ["Shutter Type",     "Elec. 1st Curtain",    "Fast, silent, no shutter shock"],
    ]
    story.append(event_settings_table(br_rows, CRIMSON))

    story.append(sp(6))

    # Tips box
    bull_tips = [
        "  * Fire at: gate open  ->  first jump (pre-shot gets it)  ->  peak spin at 2-3 sec  ->  buck-off",
        "  * Watch the bull's HEAD — it leads the body by 0.5 seconds. Aim there.",
        "  * If animal tracking grabs the bullfighter: switch to Zone AF large center, reacquire on bull",
        "  * Buffer is unlimited with CFexpress — hold the shutter without fear",
        "  * After the ride: switch Subject Detect to PEOPLE for face/reaction shots",
    ]
    story.append(SectionBox("BULL RIDING TIPS", bull_tips, bg=PALE_CRIMSON, accent=CRIMSON))
    story.append(sp(12))

    # ── BARREL RACING ─────────────────────────
    story.append(ColorBar("  BARREL RACING", bg=TEAL, fontsize=16))
    story.append(sp(6))

    barrel_rows = [
        ["Mode",             "Av (Aperture Priority)","Light shifts as horse moves around the pattern"],
        ["Aperture",         "f/2.8 - f/4",          "Isolate horse + rider from crowd background"],
        ["Shutter Min",      "1/1600 (via Auto ISO)", "Set minimum shutter in ISO Auto — enforce this"],
        ["ISO Auto Max",     "6400",                  "Bright arenas stay lower, evening events push higher"],
        ["AF Operation",     "Servo AF",              "Always"],
        ["Subject Detect",   "ANIMALS",               "Tracks the horse at full speed through the full pattern"],
        ["Eye Detection",    "ENABLE",                "Locks on horse eye at entry — stays through the turn"],
        ["Tracking Sens.",   "3",                     "Standard — barrel pattern is predictable movement"],
        ["AF Zone",          "Whole Area",            "Subject detection handles placement"],
        ["Drive Mode",       "H+ (30fps)",            "Burst at turn entry + apex + exit"],
        ["Pre-Shot",         "ON — Medium (15 frames)","Catches the exact lean and commit into the turn"],
        ["Shutter Type",     "Elec. 1st Curtain",    "Silent, no vibration"],
    ]
    story.append(event_settings_table(barrel_rows, TEAL))

    story.append(sp(6))
    barrel_tips = [
        "  * THE MONEY SHOT: burst from 2 strides before the barrel through 1 stride after exit",
        "  * Pre-focus on the barrel — let the horse run INTO your frame (great for fast entry shots)",
        "  * Between barrels = full stride shots — horse airborne = editorial-level images",
        "  * Sandpoint event: late afternoon = golden hour on the lake BEHIND the horse — position for this",
        "  * After last barrel: capture celebration expression — switch to People eye tracking",
    ]
    story.append(SectionBox("BARREL RACING TIPS", barrel_tips, bg=PALE_TEAL, accent=TEAL))

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 4: ROPING + GENERAL + LIGHTING
# ─────────────────────────────────────────────
def roping_lighting_page(story):
    story.append(sp(8))
    # ── ROPING ───────────────────────────────
    story.append(ColorBar("  CALF ROPING  /  TEAM ROPING", bg=GOLD, fg=DARK_BROWN, fontsize=14))
    story.append(sp(6))

    rope_rows = [
        ["Mode",            "M + Auto ISO",          "Predictable action — lock it in manually"],
        ["Shutter",         "1/2000",                "Freezes rope mid-air — the hero shot"],
        ["Aperture",        "f/5.6",                 "You are shooting across the arena — need the DOF"],
        ["ISO Auto Max",    "3200",                  "Daytime roping allows lower ISO"],
        ["AF Operation",    "Servo AF",              "Always"],
        ["Subject Detect",  "ANIMALS",               "Horse + roper combo — tracks both"],
        ["Eye Detection",   "ENABLE",                "Horse eye tracking at cross-arena distance"],
        ["Tracking Sens.",  "2-3",                   "Slightly lower — horse runs predictable straight line"],
        ["Drive Mode",      "H+ 30fps",              "Hold burst at rope throw window"],
        ["Pre-Shot",        "ON — MAX (30 frames)",  "Rope-over-head to release = under 0.5 seconds"],
    ]
    story.append(event_settings_table(rope_rows, colors.HexColor("#A07800")))

    story.append(sp(6))
    rope_tips = [
        "  * Watch the CALF, not the rope — calf trajectory tells you where action goes",
        "  * Rope loop overhead = fire in 1 second — pre-shot handles the miss window",
        "  * AF may shift to the calf as dominant animal — this produces great calf reaction shots, keep it",
        "  * Team roping: cover the header -> rotate slightly for heeler after first loop connects",
        "  * Calf tie-down has 3 distinct shots: catch -> scramble -> tie. Burst all three.",
    ]
    story.append(SectionBox("ROPING TIPS", rope_tips, bg=PALE_GOLD, accent=colors.HexColor("#A07800")))

    story.append(sp(10))

    # ── GENERAL / CROWD ────────────────────────
    story.append(ColorBar("  GENERAL ARENA  /  CROWD  /  FAMILY", bg=SAGE, fontsize=14))
    story.append(sp(6))

    gen_rows = [
        ["Mode",         "Av (Aperture Priority)", "Light changes as you move around the arena"],
        ["Aperture",     "f/4",                   "Balanced DOF for groups and candids"],
        ["Shutter Min",  "1/1250 via Auto ISO",    "Enforce this — action can pop up anywhere"],
        ["ISO Auto Max", "6400",                   ""],
        ["AF",           "Servo, Subject: People", "Face + Eye tracking for crowd portraits"],
        ["Drive",        "H (12fps Mechanical)",   "Most crowd shots don't need 30fps"],
        ["Pre-Shot",     "OFF",                    "Not needed for stationary subjects"],
    ]
    story.append(event_settings_table(gen_rows, SAGE))

    story.append(sp(10))

    # ── LIGHTING CONDITIONS ────────────────────
    story.append(ColorBar("  LIGHTING CONDITIONS — QUICK FIX", bg=DUSTY_BLUE, fontsize=14))
    story.append(sp(4))

    light_data = [
        ["CONDITION", "PROBLEM", "FIX IT"],
        ["Harsh Midday Sun",      "Blown highlights on white horses/hats",   "-2/3 stop exp. comp  |  Spot meter off mid-tones"],
        ["Dust + Haze",           "Meter underexposes, AF hunts",            "+1/3 stop exp comp  |  Tracking Sens -> 4-5  |  Embrace the haze"],
        ["Night / LED Arena",     "Banding / rolling shutter",               "Switch to MECHANICAL shutter  |  ISO 6400-12800  |  WB: 3200K"],
        ["Golden Hour (Sandpoint)","Blown sky, dark subject",                "Expose for subject  |  -1/3 comp  |  Shoot with lake as background"],
        ["Indoor Arena Mixed",    "Color cast, uneven light",                "Manual WB 3500-4200K  |  Meter each position  |  RAW fixes the rest"],
    ]
    ltstyle = [
        ("BACKGROUND",    (0,0), (-1,0), DUSTY_BLUE),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), DUSTY_BLUE),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("TEXTCOLOR",     (1,1), (-1,-1), DARK_BROWN),
        ("ALIGN",         (0,0), (-1,-1), "LEFT"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_BLUE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#AABBCC")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    ltt = Table(light_data, colWidths=[1.5*inch, 2.0*inch, 4.2*inch])
    ltt.setStyle(TableStyle(ltstyle))
    story.append(ltt)

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 5: LENS GUIDE
# ─────────────────────────────────────────────
def lens_page(story):
    story.append(sp(8))
    story.append(ColorBar("  LENS GUIDE  —  CANON RF MOUNT", bg=MID_BROWN, fontsize=15))
    story.append(sp(8))

    story.append(head("PICK YOUR PRIMARY — ONE LENS TO RULE THE ARENA", 2))
    story.append(sp(4))

    primary_data = [
        ["LENS", "RANGE", "BEST FOR", "USED PRICE", "VERDICT"],
        ["RF 70-200mm f/2.8L IS USM",   "70-200mm",  "Close rail access, indoor arenas",     "$1,800-2,200", "BEST ALL-AROUND"],
        ["RF 100-500mm f/4.5-7.1L IS",  "100-500mm", "County fairs, large venues, reach",    "$1,900-2,400", "BEST REACH+VERSATILE"],
        ["RF 200-800mm f/6.3-9 IS USM", "200-800mm", "Huge arenas, Pendleton-scale events",  "$700-850",     "BEST VALUE REACH"],
        ["RF 100-400mm f/5.6-8 IS USM", "100-400mm", "Starting out, light carry, budget",    "$550-650",     "BEST ENTRY POINT"],
    ]
    pstyle = [
        ("BACKGROUND",    (0,0), (-1,0), MID_BROWN),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,0), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), DARK_BROWN),
        ("FONTNAME",      (1,1), (3,-1), "Helvetica"),
        ("FONTSIZE",      (1,0), (-1,-1), 8),
        ("FONTNAME",      (4,1), (4,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (4,1), (4,-1), BURNT_ORANGE),
        ("ALIGN",         (3,0), (4,-1), "CENTER"),
        ("ALIGN",         (0,0), (0,-1), "LEFT"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_ORANGE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    pt = Table(primary_data, colWidths=[2.3*inch, 0.85*inch, 1.7*inch, 1.0*inch, 1.85*inch])
    pt.setStyle(TableStyle(pstyle))
    story.append(pt)

    story.append(sp(8))
    story.append(head("SECONDARY LENS — ADD THIS WHEN YOU RUN TWO BODIES", 2))
    story.append(sp(4))

    sec_data = [
        ["LENS", "RANGE", "USE", "USED PRICE"],
        ["RF 24-70mm f/2.8L IS USM",  "24-70mm",  "Crowd, family, behind-chutes access, environmental portraits", "$1,600-1,900"],
        ["RF 35mm f/1.8 IS STM",      "35mm",     "Budget option for crowd/portrait secondary",                   "$400-499"],
        ["Canon 50mm f/1.8 STM",      "50mm",     "Cheapest capable secondary — $130 new",                       "$80-130"],
    ]
    st_s = [
        ("BACKGROUND",    (0,0), (-1,0), colors.HexColor("#4A6741")),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR",     (1,1), (-1,-1), DARK_BROWN),
        ("ALIGN",         (0,0), (-1,-1), "LEFT"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_SAGE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#AABB99")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    sst = Table(sec_data, colWidths=[2.3*inch, 0.75*inch, 3.2*inch, 1.45*inch])
    sst.setStyle(TableStyle(st_s))
    story.append(sst)

    story.append(sp(8))
    story.append(head("KIT BY BUDGET", 2))
    story.append(sp(4))

    budget_data = [
        ["BUDGET", "BUY THIS", "COVERS"],
        ["$650-900\nStarting Out",
         "RF 100-400mm f/5.6-8\n+ Canon 50mm f/1.8",
         "80% of arena situations  |  Prove the concept before investing more"],
        ["$2,000-2,500\nWorking Photographer",
         "RF 70-200mm f/2.8L (used)\n+ RF 35mm f/1.8",
         "Professional coverage  |  Low-light events  |  Subject isolation"],
        ["$4,500-5,500\nFull Two-Body Kit",
         "RF 100-500mm (used)\n+ RF 70-200 f/2.8 (used)\n+ RF 24-70 f/2.8 (used)",
         "Tier 1 through Tier 3 events  |  Everything from Sandpoint to Pendleton"],
    ]
    bstyle = [
        ("BACKGROUND",    (0,0), (-1,0), BURNT_ORANGE),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), BURNT_ORANGE),
        ("ALIGN",         (0,0), (0,-1), "CENTER"),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR",     (1,1), (-1,-1), DARK_BROWN),
        ("FONTNAME",      (1,1), (1,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (1,1), (1,-1), DARK_BROWN),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_ORANGE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    bt = Table(budget_data, colWidths=[1.2*inch, 2.3*inch, 4.25*inch])
    bt.setStyle(TableStyle(bstyle))
    story.append(bt)

    story.append(sp(8))

    # DO NOT BUY + EF adapter side by side
    dnb = [
        ["DO NOT BUY", "WHY"],
        ["EF-S or RF-S crop lenses",    "R5 II is full-frame — crop lenses vignette"],
        ["RF 2x extender on f/5.6+",    "AF won't work — min f/8 required and tracking degrades"],
        ["Manual FD mount lenses",      "No AF = missed shots. Don't romanticize it at rodeos."],
        ["Unknown third-party RF",      "No animal tracking support — defeats the whole system"],
    ]
    dstyle = [
        ("BACKGROUND",    (0,0), (-1,0), CRIMSON),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), CRIMSON),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR",     (1,1), (-1,-1), DARK_BROWN),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_CRIMSON]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCAAAA")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    dt = Table(dnb, colWidths=[1.9*inch, 1.9*inch])
    dt.setStyle(TableStyle(dstyle))

    ef_data = [
        ["EF LENSES VIA ADAPTER (FULL COMPAT.)", "USED PRICE"],
        ["EF 70-200mm f/2.8L IS III",   "$1,200-1,600"],
        ["EF 100-400mm f/4.5-5.6L IS II", "$1,400-1,800"],
        ["Sigma 150-600mm Sport (EF)",  "$900-1,300"],
        ["Tamron 150-600mm G2 (EF)",    "$700-1,000"],
    ]
    efstyle = [
        ("BACKGROUND",    (0,0), (-1,0), DUSTY_BLUE),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), DARK_BROWN),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (1,1), (-1,-1), DUSTY_BLUE),
        ("ALIGN",         (1,0), (1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_BLUE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#AABBCC")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    eft = Table(ef_data, colWidths=[2.5*inch, 1.3*inch])
    eft.setStyle(TableStyle(efstyle))

    two = Table([[dt, sp(8), eft]], colWidths=[3.9*inch, 0.1*inch, 3.9*inch])
    two.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(two)

    story.append(sp(6))
    story.append(p(
        "<b>EF Adapter note:</b> Canon EF-EOS R Mount Adapter (~$100) gives full AF speed and "
        "animal tracking on ALL Canon EF L-series lenses. Adapted EF glass on the R5 Mark II "
        "works extremely well — Canon engineered the adapter to maintain full AF functionality.",
        "Note"))

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 6: POSITIONING MAPS
# ─────────────────────────────────────────────
def positioning_page(story):
    story.append(sp(8))
    story.append(ColorBar("  ARENA POSITIONING — WHERE TO STAND", bg=DARK_BROWN, fontsize=15))
    story.append(sp(8))

    pos_data = [
        ["EVENT",         "DEFAULT POSITION",                          "MONEY SHOT POSITION",                   "NEVER STAND HERE"],
        ["BULL RIDING",
         "Opposite the chutes, inside corner rail.\nFacing chute so bull exits toward you.\nCrouch or sit — low angle.",
         "Chute-side gate position.\nCaptures bull exit burst + rider face.\nConfirm with arena director first.",
         "Behind chutes  |  Center arena\nDirectly in front of any chute\nHigh in stands"],
        ["BARREL RACING",
         "Perpendicular to Barrel 1 inside the arena.\nShoots approach + turn simultaneously.\n20-40 feet from barrel if permitted.",
         "Opposite Barrel 2 for tightest turn shot.\nOR far end for full run-in + stride shots.",
         "Behind the timer gates at entrance\nInside the barrel pattern\nDirectly behind any barrel"],
        ["CALF / TEAM ROPING",
         "Header side, mid-arena.\nShoots the chase, throw, and tie-down.\nUse 300-500mm to compress distance.",
         "Far end corner — rope overhead + calf\nreaction simultaneously.\nBest rope-mid-air angle.",
         "In the box area (where horses back in)\nBehind the calf chute\nDirectly behind any chute gate"],
        ["GENERAL FLOW",
         "Rail position, inside curve of any turn.\nAccess to most events.\nQuick movement options.",
         "Move during announcements (2-3 min window).\nAlways tell arena director before moving.\nNever cross arena between events.",
         "Anywhere without explicit permission\nCenter of arena during action\nBehind unsecured gates"],
    ]
    pstyle = [
        ("BACKGROUND",    (0,0), (-1,0), DARK_BROWN),
        ("TEXTCOLOR",     (0,0), (-1,0), GOLD),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,0), 8.5),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("FONTSIZE",      (0,1), (0,-1), 8),
        ("TEXTCOLOR",     (0,1), (0,-1), WHITE),
        ("BACKGROUND",    (0,1), (0,1), CRIMSON),
        ("BACKGROUND",    (0,2), (0,2), TEAL),
        ("BACKGROUND",    (0,3), (0,3), colors.HexColor("#A07800")),
        ("BACKGROUND",    (0,4), (0,4), SAGE),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (1,1), (-1,-1), 7.5),
        ("TEXTCOLOR",     (1,1), (1,-1), DARK_BROWN),
        ("TEXTCOLOR",     (2,1), (2,-1), colors.HexColor("#1A5A50")),
        ("FONTNAME",      (2,1), (2,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (3,1), (3,-1), CRIMSON),
        ("FONTNAME",      (3,1), (3,-1), "Helvetica-Bold"),
        ("ALIGN",         (0,0), (0,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, CREAM]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    pt = Table(pos_data, colWidths=[0.9*inch, 2.3*inch, 2.3*inch, 2.25*inch])
    pt.setStyle(TableStyle(pstyle))
    story.append(pt)

    story.append(sp(10))

    # Arena diagram (text-based)
    story.append(ColorBar("  ARENA LAYOUT — MID-SIZE COUNTY FAIR (Stateline / North Idaho Style)",
                          bg=colors.HexColor("#3D2210"), fontsize=11, height=24))
    story.append(sp(6))

    class ArenaDiagram(Flowable):
        def __init__(self, width):
            self.width = width
            self.height = 3.2*inch

        def wrap(self, aw, ah):
            return self.width, self.height

        def draw(self):
            c = self.canv
            W = self.width
            H = self.height

            # Arena outline
            c.setStrokeColor(MID_BROWN)
            c.setFillColor(colors.HexColor("#F5EDD8"))
            c.setLineWidth(2)
            c.roundRect(0.4*inch, 0.3*inch, W - 0.8*inch, H - 0.6*inch, 12, fill=1, stroke=1)

            # Dirt texture dots (simple)
            c.setFillColor(colors.HexColor("#E8D9B5"))
            for x in range(6):
                for y in range(4):
                    c.circle(0.9*inch + x*0.9*inch, 0.7*inch + y*0.55*inch, 2, fill=1, stroke=0)

            # Chutes
            c.setFillColor(MID_BROWN)
            c.rect(0, H*0.55, 0.5*inch, 0.5*inch, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 7)
            c.drawCentredString(0.25*inch, H*0.6 + 0.15*inch, "CHUTES")

            # Barrel positions
            barrel_pos = [
                (W*0.35, H*0.72, "B1"),
                (W*0.65, H*0.72, "B2"),
                (W*0.5,  H*0.35, "B3"),
            ]
            for bx, by, lbl in barrel_pos:
                c.setFillColor(BURNT_ORANGE)
                c.circle(bx, by, 10, fill=1, stroke=0)
                c.setFillColor(WHITE)
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(bx, by - 3, lbl)

            # Zone labels
            zones = [
                (W*0.82, H*0.5,  CRIMSON,      "ZONE A\nDefault\n(bull+barrels)"),
                (W*0.18, H*0.65, TEAL,         "ZONE B\nChute-side\n(bull exit)"),
                (W*0.5,  H*0.15, DUSTY_BLUE,   "ZONE C\nFar end\n(roping)"),
            ]
            for zx, zy, zc, ztxt in zones:
                c.setFillColor(zc)
                c.roundRect(zx - 38, zy - 18, 76, 42, 5, fill=1, stroke=0)
                c.setFillColor(WHITE)
                c.setFont("Helvetica-Bold", 6.5)
                for i, line in enumerate(ztxt.split("\n")):
                    c.drawCentredString(zx, zy + 16 - i*12, line)

            # Star = best default
            c.setFillColor(GOLD)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(W*0.73, H*0.48, "<-- START HERE")

            # Entry gate
            c.setFillColor(DARK_BROWN)
            c.rect(W*0.42, 0, 0.18*W, 0.25*inch, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 6)
            c.drawCentredString(W*0.5, 0.06*inch, "ENTRY GATE / TIMER")

    story.append(ArenaDiagram(7.5*inch))

    story.append(sp(6))
    story.append(p(
        "<b>Zone A (opposite chutes, low rail):</b> Your default 80% of the time — bull exits, barrel turns, calf chase.  "
        "<b>Zone B (chute-side gate):</b> Bull riding exit shots — confirm with arena director.  "
        "<b>Zone C (far end):</b> Roping compression shots and rope-mid-air hero images.", "Note"))

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 7: EVENT CALENDAR
# ─────────────────────────────────────────────
def event_calendar_page(story):
    story.append(sp(8))
    story.append(ColorBar("  250-MILE EVENT CALENDAR  —  83801 CAREYWOOD, ID", bg=DARK_BROWN, fontsize=14))
    story.append(sp(8))

    story.append(head("TIER 1 — START HERE (County Fairs + Small PRCA = Easy Access)", 2))
    story.append(sp(4))

    t1_data = [
        ["EVENT", "LOCATION", "DIST.", "MONTH", "ACCESS TIP"],
        ["North Idaho State Fair & Rodeo", "Coeur d'Alene, ID", "~40 mi", "August",     "Home turf — email coordinator directly"],
        ["Sandpoint Bonner County Rodeo",  "Sandpoint, ID",     "~60 mi", "August",     "Lake Pend Oreille backdrop — position for it"],
        ["Spokane County Interstate Fair",  "Spokane, WA",       "~55 mi", "September",  "County fair = open doors, familiar market"],
        ["Lewiston Roundup",               "Lewiston, ID",      "~65 mi", "September",  "92nd year — apply 6+ weeks early"],
        ["Latah County Fair",              "Moscow, ID",        "~100 mi","September",  "Small and accessible"],
        ["UM Spring Rodeo (Collegiate)",   "Missoula, MT",      "~200 mi","May",        "ZERO credentialing friction — start here"],
        ["Barrel Racing Jackpots",         "Region-wide",       "Varies", "Year-round", "No credentials needed — best practice events"],
    ]
    story.append(make_table(t1_data,
        [2.1*inch, 1.3*inch, 0.6*inch, 0.75*inch, 2.9*inch],
        header_bg=SAGE, row_colors=[LIGHT_CREAM, PALE_SAGE]))

    story.append(sp(10))
    story.append(head("TIER 2 — BUILD TOWARD THESE (Mid-Level PRCA + Unique Events)", 2))
    story.append(sp(4))

    t2_data = [
        ["EVENT", "LOCATION", "DIST.", "MONTH", "WHY GO"],
        ["Omak Stampede",              "Omak, WA",        "~125 mi","August",    "Suicide Race = UNIQUE fine art print content"],
        ["Toppenish Rodeo",            "Toppenish, WA",   "~155 mi","July 4th",  "Columbia River Circuit PRCA"],
        ["Moses Lake Round-Up",        "Moses Lake, WA",  "~150 mi","August",    "CINCH Playoff Series — apply 6+ weeks out"],
        ["NW Montana Fair & Rodeo",    "Kalispell, MT",   "~160 mi","August",    "120-year fair — county fair access rules"],
        ["Basin City Freedom Rodeo",   "Basin City, WA",  "~160 mi","July 4th",  "July 4th crowd = family sales goldmine"],
        ["Walla Walla Fair & Frontier","Walla Walla, WA", "~175 mi","September", "160th anniversary — great PR hook"],
    ]
    story.append(make_table(t2_data,
        [2.1*inch, 1.3*inch, 0.6*inch, 0.75*inch, 2.9*inch],
        header_bg=DUSTY_BLUE, row_colors=[LIGHT_CREAM, PALE_BLUE]))

    story.append(sp(10))
    story.append(head("TIER 3 — EARN THESE (Major PRCA — Requires Established Credentials)", 2))
    story.append(sp(4))

    t3_data = [
        ["EVENT", "LOCATION", "DIST.", "MONTH", "WHAT YOU NEED"],
        ["Ellensburg Rodeo",     "Ellensburg, WA", "~140 mi","Labor Day", "Top 25 national — PRCA press credentials"],
        ["Horse Heaven Round-Up","Kennewick, WA",  "~165 mi","August",    "Big 4 Association — 5 nights, major purse"],
        ["Missoula Stampede",    "Missoula, MT",   "~200 mi","August",    "Western Montana Fair — grow into this"],
        ["Pendleton Round-Up",   "Pendleton, OR",  "~215 mi","September", "100+ year legacy — media affiliation required"],
    ]
    story.append(make_table(t3_data,
        [2.1*inch, 1.3*inch, 0.6*inch, 0.75*inch, 2.9*inch],
        header_bg=CRIMSON, row_colors=[LIGHT_CREAM, PALE_CRIMSON]))

    story.append(sp(10))

    # Year roadmap
    story.append(ColorBar("  YOUR FIRST-YEAR ROADMAP", bg=BURNT_ORANGE, fontsize=12, height=26))
    story.append(sp(4))

    roadmap = [
        ["MAY",       "UM Collegiate Rodeo (Missoula)",      "Zero pressure — test animal tracking system"],
        ["JUNE",      "Local jackpot barrel racing",          "Push AF to its limit weekly — build portfolio"],
        ["JULY",      "Toppenish OR Basin City",              "First PRCA credential attempt"],
        ["AUGUST",    "Sandpoint + North Idaho Fair",         "Own your home events — build relationships"],
        ["AUGUST",    "Omak Stampede",                        "Suicide Race = unique fine art print content"],
        ["SEPTEMBER", "Lewiston Roundup",                     "Deepen local circuit relationships"],
        ["SEPTEMBER", "Walla Walla Fair & Frontier Days",     "160th anniversary = built-in PR story"],
        ["LABOR DAY", "Ellensburg Rodeo (goal: Year 2)",      "Top 25 national prestige credential"],
        ["SEPTEMBER", "Pendleton Round-Up (goal: Year 2-3)", "The bucket list credential"],
    ]
    rdstyle = [
        ("BACKGROUND",    (0,0), (-1,0), BURNT_ORANGE),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,0), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,0), (0,-1), WHITE),
        ("BACKGROUND",    (0,0), (0,-1), BURNT_ORANGE),
        ("FONTNAME",      (1,0), (1,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (1,0), (1,-1), DARK_BROWN),
        ("FONTNAME",      (2,0), (2,-1), "Helvetica"),
        ("TEXTCOLOR",     (2,0), (2,-1), MID_BROWN),
        ("ALIGN",         (0,0), (0,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,0), (-1,-1), [PALE_ORANGE, LIGHT_CREAM]),
        ("BACKGROUND",    (0,0), (0,-1), BURNT_ORANGE),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    rdt = Table(roadmap, colWidths=[0.85*inch, 2.8*inch, 4.1*inch])
    rdt.setStyle(TableStyle(rdstyle))
    story.append(rdt)

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 8: TROUBLESHOOTING
# ─────────────────────────────────────────────
def troubleshooting_page(story):
    story.append(sp(8))
    story.append(ColorBar("  TROUBLESHOOTING — SOMETHING WENT WRONG?", bg=CRIMSON, fontsize=14))
    story.append(sp(8))

    trouble_data = [
        ["PROBLEM", "CAUSE", "FIX IT NOW"],
        ["AF hunting — not locking",         "Dust obscured subject",               "Tracking Sens -> 4-5  |  Switch to Zone AF Large Center"],
        ["Locked on wrong animal",           "Multiple animals in frame",           "TAP the correct subject on EVF touchscreen to confirm"],
        ["Blurry despite fast shutter",      "IBIS fighting panning motion",        "Switch to IBIS Mode 2 (panning)  |  Check shutter is actually set"],
        ["Rolling shutter banding at night", "Electronic shutter + LED lights",     "SWITCH TO MECHANICAL SHUTTER immediately"],
        ["Pre-shot not catching peak",       "Buffer too short setting",            "Set pre-shot to MAX (30 frames) in Shooting Menu 4"],
        ["Massive file drain from 30fps",    "Too many frames at H+ continuously",  "Drop to H (12fps) for predictable action  |  Cull fast"],
        ["Clipped highlights on white horse","Evaluative metering blown",           "-2/3 exp. comp  |  Spot meter on mid-tone horse body"],
        ["EVF blackout during burst",        "H+ mode or display setting off",      "Confirm H+ selected  |  Enable High Speed Display in menu"],
        ["AF hunting on rope not rider",     "Rope is high contrast thin element",  "Single center point  |  Aim at horse shoulder"],
        ["Animal tracking follows rider",    "People detect competing with Animals", "Confirm Subject Detect = ANIMALS (not Auto)"],
        ["CFexpress card not recognized",    "Card not formatted in-body",          "FORMAT in R5 II body — do not trust computer formatting"],
        ["IBIS ghosting in EVF",             "IBIS + panning combined",             "Use IBIS Mode 2  |  Or disable for stationary shots"],
        ["Low hit rate on bull riding",      "Anticipating wrong moment",           "Fire EARLIER  |  Cull later — pre-shot handles the miss"],
        ["Dark muddy images in dust",        "Meter overexposing for haze",         "+1/3 stop comp  |  Dust reads bright — boost exposure"],
        ["AF drops mid-burst in dust",       "Subject detect loses subject",        "Tracking Sensitivity 5  |  Fall back to Zone AF Center"],
        ["Overexposed at night arena",       "Auto ISO pegged low for bright spots","Manual mode: set 1/1000, f/2.8, ISO 6400 and adjust"],
    ]

    trstyle = [
        ("BACKGROUND",    (0,0), (-1,0), CRIMSON),
        ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,0), 8),
        ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-1), CRIMSON),
        ("FONTNAME",      (1,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (1,0), (-1,-1), 7.5),
        ("TEXTCOLOR",     (1,1), (-1,-1), DARK_BROWN),
        ("FONTNAME",      (2,1), (2,-1), "Helvetica-Bold"),
        ("TEXTCOLOR",     (2,1), (2,-1), colors.HexColor("#1A5A50")),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT_CREAM, PALE_CRIMSON]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCAAAA")),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 5),
    ]
    trt = Table(trouble_data, colWidths=[1.8*inch, 1.9*inch, 4.05*inch])
    trt.setStyle(TableStyle(trstyle))
    story.append(trt)

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 9: GEAR + CARDS + MONETIZATION
# ─────────────────────────────────────────────
def gear_money_page(story):
    story.append(sp(8))
    story.append(ColorBar("  GEAR SURVIVAL — DUST, CARDS, BATTERIES", bg=MID_BROWN, fontsize=14))
    story.append(sp(8))

    # 3-column row
    gear_l = [
        [ColorBar("  CARDS", bg=DUSTY_BLUE, height=22, fontsize=10)],
        [make_table(
            [["SLOT", "WHAT TO USE"],
             ["Slot 1 (CFexpress)", "ProGrade or Sony Tough\n256-512GB — don't cheap out"],
             ["Slot 2 (SD UHS-II)", "Set to MIRROR/BACKUP\nEvery shot on both cards"],
             ["How many", "3x CFexpress cards\nper full event day"],
             ["Format", "In-body ONLY — never\ntrust computer formatting"],],
            [1.0*inch, 1.5*inch], header_bg=DUSTY_BLUE,
            row_colors=[LIGHT_CREAM, PALE_BLUE])],
    ]

    gear_m = [
        [ColorBar("  BATTERIES", bg=SAGE, height=22, fontsize=10)],
        [make_table(
            [["ITEM", "RULE"],
             ["Battery type", "LP-E6NH — R5 II native"],
             ["Per event", "3 minimum per body"],
             ["Cold Idaho mornings", "Keep 1 in your vest\nagainst your body"],
             ["Battery grip", "BG-R10 = double life\n+ better balance on long tele"],],
            [1.0*inch, 1.5*inch], header_bg=SAGE,
            row_colors=[LIGHT_CREAM, PALE_SAGE])],
    ]

    gear_r = [
        [ColorBar("  DUST PROTECTION", bg=MID_BROWN, height=22, fontsize=10)],
        [make_table(
            [["ITEM", "HOW"],
             ["R5 II body", "Weather sealed — trust it\nweak points: ports + hotshoe"],
             ["Front element", "Lens hood ON always\n(dust + flare dual duty)"],
             ["Cards", "Sealed zipper bags\nfor spare cards"],
             ["Bag", "Silica gel in every pocket\nwipe lens every 30 min"],],
            [1.05*inch, 1.45*inch], header_bg=MID_BROWN,
            row_colors=[LIGHT_CREAM, PALE_ORANGE])],
    ]

    gear_row = Table([[gear_l, gear_m, gear_r]], colWidths=[2.6*inch, 2.6*inch, 2.6*inch])
    gear_row.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(gear_row)

    story.append(sp(8))

    # IBIS modes
    story.append(ColorBar("  IBIS MODES — USE THE RIGHT ONE", bg=TEAL, height=24, fontsize=11))
    story.append(sp(4))
    ibis_data = [
        ["IBIS MODE", "WHEN TO USE", "WHY"],
        ["Mode 1 (All-Axis)",  "Stationary shooting, crowd, portraits, environmental", "Stabilizes all directions — maximum steadiness"],
        ["Mode 2 (Panning)",   "Following horse through barrel turn or full-stride run", "Compensates vertical only — allows smooth horizontal pan"],
        ["IBIS OFF",           "Monopod or tripod use", "IBIS can fight a stable platform and cause ghosting"],
    ]
    story.append(make_table(ibis_data, [1.2*inch, 3.1*inch, 3.45*inch],
                            header_bg=TEAL, row_colors=[LIGHT_CREAM, PALE_TEAL]))

    story.append(sp(10))
    story.append(hr(GOLD))

    # ── MONETIZATION ─────────────────────────
    story.append(ColorBar("  MONETIZATION — 3 REVENUE STREAMS THAT SCALE", bg=BURNT_ORANGE, fontsize=13))
    story.append(sp(8))

    # Pricing table
    story.append(head("PRICING (North Idaho Market)", 2))
    story.append(sp(4))

    price_data = [
        ["PRODUCT", "PRICE", "NOTES"],
        ["Single digital download",         "$15-20",    "Price for local family market"],
        ["5-image digital bundle",           "$55-70",    "Drives multi-image purchase — most popular"],
        ["All-day digital package",          "$125-175",  "Best value — event-specific"],
        ["4x6 print on-site",               "$12",       "Impulse buy at the gate exit"],
        ["8x10 print on-site",              "$28",       ""],
        ["16x20 canvas (45MP R5 II only)",  "$175-250",  "Only possible with this camera's file size"],
        ["Social media promo pack",          "$95",       "5 vertical-cropped, edited images"],
        ["Season rider package (3 events)", "$350",      "Repeat business anchor — pitch this hard"],
        ["Event organizer package",          "$500-1,200","B2B highest margin — year 2: annual contract"],
        ["Event highlight reel (video)",     "$200-400",  "Optional year 2+ — R5 II shoots 8K RAW"],
    ]
    story.append(make_table(price_data, [2.5*inch, 1.0*inch, 4.25*inch],
                            header_bg=BURNT_ORANGE, row_colors=[LIGHT_CREAM, PALE_ORANGE]))

    story.append(sp(8))

    # Revenue per event box
    story.append(ColorBar("  REVENUE PER EVENT — NORTH IDAHO MARKET", bg=DARK_BROWN, height=24, fontsize=11))
    story.append(sp(4))

    rev_data = [
        ["SOURCE", "CONSERVATIVE", "OPTIMISTIC"],
        ["Individual digital sales",   "$150",  "$450"],
        ["On-site prints",             "$75",   "$300"],
        ["Pre-booked rider packages",  "$100",  "$350"],
        ["Organizer package",          "$400",  "$1,000"],
        ["Sponsor overlay add-on",     "$0",    "$250"],
        ["TOTAL PER EVENT",            "$725",  "$2,350"],
        ["10 EVENTS / YEAR",           "$7,250","$23,500+"],
    ]
    rstyle = [
        ("BACKGROUND",    (0,0), (-1,0), DARK_BROWN),
        ("TEXTCOLOR",     (0,0), (-1,0), GOLD),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("FONTNAME",      (0,-2), (-1,-1), "Helvetica-Bold"),
        ("BACKGROUND",    (0,-2), (-1,-2), colors.HexColor("#3D2210")),
        ("BACKGROUND",    (0,-1), (-1,-1), BURNT_ORANGE),
        ("TEXTCOLOR",     (0,-2), (-1,-2), GOLD),
        ("TEXTCOLOR",     (0,-1), (-1,-1), WHITE),
        ("FONTNAME",      (0,1), (0,-3), "Helvetica-Bold"),
        ("TEXTCOLOR",     (0,1), (0,-3), DARK_BROWN),
        ("TEXTCOLOR",     (1,1), (1,-3), MID_BROWN),
        ("TEXTCOLOR",     (2,1), (2,-3), SAGE),
        ("FONTNAME",      (2,1), (2,-3), "Helvetica-Bold"),
        ("ALIGN",         (1,0), (-1,-1), "CENTER"),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS",(0,1), (-1,-3), [LIGHT_CREAM, PALE_ORANGE]),
        ("GRID",          (0,0), (-1,-1), 0.3, colors.HexColor("#CCBBA0")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]
    rt = Table(rev_data, colWidths=[3.5*inch, 1.75*inch, 2.5*inch])
    rt.setStyle(TableStyle(rstyle))
    story.append(rt)

    story.append(sp(8))

    # Labor traps
    story.append(ColorBar("  AVOID THESE LABOR TRAPS", bg=CRIMSON, height=24, fontsize=11))
    story.append(sp(4))

    trap_data = [
        ["TRAP", "FIX"],
        ["Manually emailing photos to buyers",           "SmugMug / Pic-Time auto-fulfillment ONLY"],
        ["Selling from original CFexpress cards",        "Import to 2 drives before selling anything"],
        ["Shooting 3+ events per weekend solo",          "2 events max — quality and energy degrade fast"],
        ["Printing everything on-site without help",     "Hire day-of assistant OR skip prints until year 2"],
        ["Custom pricing per person in the moment",      "Published package prices only — no negotiation"],
        ["Editing every image before uploading gallery", "Upload JPEG previews fast — edit selects later"],
    ]
    story.append(make_table(trap_data, [3.2*inch, 4.55*inch],
                            header_bg=CRIMSON, row_colors=[LIGHT_CREAM, PALE_CRIMSON]))

    story.append(PageBreak())


# ─────────────────────────────────────────────
# PAGE 10: OUTREACH + BACK COVER
# ─────────────────────────────────────────────
def outreach_backcover_page(story):
    story.append(sp(8))
    story.append(ColorBar("  OUTREACH SCRIPTS — COPY AND SEND", bg=DARK_BROWN, fontsize=14))
    story.append(sp(8))

    story.append(head("TEMPLATE A — County Fair / Home Turf (Email)", 2))
    story.append(sp(4))

    class ScriptBox(Flowable):
        def __init__(self, lines, accent=BURNT_ORANGE, bg=PALE_ORANGE):
            self.lines = lines
            self.accent = accent
            self.bg = bg
            self.width = 0
            self.height = 0

        def wrap(self, aw, ah):
            self.width = aw
            self.height = len(self.lines) * 13 + 20
            return self.width, self.height

        def draw(self):
            c = self.canv
            c.setFillColor(self.bg)
            c.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=0)
            c.setFillColor(self.accent)
            c.rect(0, 0, 4, self.height, fill=1, stroke=0)
            c.setFillColor(DARK_BROWN)
            c.setFont("Helvetica", 8.5)
            y = self.height - 14
            for line in self.lines:
                if line.startswith("**"):
                    c.setFont("Helvetica-Bold", 8.5)
                    c.drawString(12, y, line.replace("**", ""))
                else:
                    c.setFont("Helvetica", 8.5)
                    c.drawString(12, y, line)
                y -= 13

    story.append(ScriptBox([
        "**Subject: Photography for [Event Name] — Tribal Cowboy",
        "",
        "Hi [Name],",
        "",
        "I'm Stacie with Tribal Cowboy, an equine experience brand based right here in North Idaho",
        "(Careywood area). We specialize in rodeo and ranch photography for local families and riders.",
        "",
        "I'd love to offer photography coverage for [event] this year. What I bring:",
        "  - High-resolution event images for your social media and promos (free to you)",
        "  - On-site or fast digital gallery sales to participants and families — I handle everything",
        "  - Full credit and tags to your event in all published content",
        "",
        "No cost to you. We're local, we know your audience, and we'll make your event look incredible.",
        "",
        "Can we connect this week?",
        "",
        "Stacie | Tribal Cowboy | [phone] | [Instagram]",
    ], accent=BURNT_ORANGE, bg=PALE_ORANGE))

    story.append(sp(8))
    story.append(head("TEMPLATE B — Washington / Montana Events (Outside Home Base)", 2))
    story.append(sp(4))

    story.append(ScriptBox([
        "**Subject: Media Coverage Request — [Event Name] 2026",
        "",
        "Hi [Name],",
        "",
        "I'm reaching out from Tribal Cowboy, a North Idaho-based equine and rodeo photography brand.",
        "We cover events from Spokane to Missoula and we're building our 2026 calendar.",
        "",
        "We'd like to request photography credentials for [event]. We offer:",
        "  - Professional rodeo coverage (bull riding, barrel racing, roping, family moments)",
        "  - Fast gallery delivery for rider/family digital sales",
        "  - No cost to the event — all revenue comes from participant photo sales",
        "",
        "Portfolio available on request. Happy to jump on a call.",
        "",
        "Stacie Huffhines | Tribal Cowboy Photography | [phone]",
    ], accent=DUSTY_BLUE, bg=PALE_BLUE))

    story.append(sp(8))
    story.append(head("TEMPLATE C — Barrel Racing Jackpot (Facebook DM / Text)", 2))
    story.append(sp(4))

    story.append(ScriptBox([
        "Hey [Name/Group admin]!",
        "",
        "I'm Stacie with Tribal Cowboy — we do rodeo and equine photography out of North Idaho.",
        "I'd love to come out and capture the barrel racing this [date] and get some great shots",
        "for the riders. I'll post a few previews and share the full gallery so everyone can grab",
        "their photos. Would that be okay with the organizers?",
    ], accent=TEAL, bg=PALE_TEAL))

    story.append(sp(8))

    # Checklist
    story.append(ColorBar("  PRE-EVENT CHECKLIST — BEFORE YOU SHOW UP AT THE GATE", bg=SAGE, fontsize=12, height=26))
    story.append(sp(4))

    checks = [
        ("Written confirmation (email/text) from the event coordinator",                  True),
        ("Know who to ask for at the gate — by name",                                     True),
        ("Carry printed confirmation + 10 business cards",                                True),
        ("Know flash rules, zone limits, when to clear the arena",                        True),
        ("Liability waiver signed if required — ask in advance",                          True),
        ("3x CFexpress cards formatted in-body",                                          True),
        ("3x LP-E6NH batteries per body, all charged",                                    True),
        ("Lens cloth in vest pocket",                                                      True),
        ("Gallery platform ready (SmugMug / Pic-Time) — test login",                     True),
        ("Custom shooting modes set: C1=Bull, C2=Barrel, C3=General",                    True),
        ("Animal tracking confirmed: AF Menu > Subject Detect = ANIMALS, Eye Det = ON",   True),
        ("Pre-shot set: Shooting Menu 4 > Pre-shot Burst = ON, Medium or Max",           True),
    ]

    check_data = [[("[ ]  " if not done else "[ ]  ") + txt, ""] for txt, done in checks]
    # Make it a simple styled list
    for txt, _ in checks:
        story.append(p(f"<b>[ ]</b>  {txt}", "Body"))

    story.append(sp(10))

    # Back cover flavor
    story.append(hr(GOLD, 2))
    story.append(sp(6))
    story.append(p(
        "<b>The R5 Mark II removes the mechanical excuses.</b> The camera will track the horse, "
        "capture the peak before your brain reacts, and deliver files that print large enough to "
        "hang in a barn or a living room. What it cannot do is get you access, build relationships "
        "with committees, or show up consistently. <b>That part is still on you.</b>",
        "Body"))
    story.append(sp(6))
    story.append(p(
        "Millie  *  Abby  *  Jolene  *  Monster  *  Master Chief",
        "CenterSmall"))
    story.append(p(
        "Tribal Cowboy  |  North Idaho / Eastern Washington  |  tribalcowboy.com",
        "CenterSmall"))


# ─────────────────────────────────────────────
# BUILD THE PDF
# ─────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        leftMargin=0.6*inch,
        rightMargin=0.6*inch,
        topMargin=0.55*inch,
        bottomMargin=0.45*inch,
        title="Tribal Cowboy Rodeo Photography Field Guide — Canon R5 Mark II",
        author="Tribal Cowboy",
        subject="Rodeo Photography — 83801 North Idaho 250-Mile Radius",
    )

    story = []

    cover_page(story)
    quick_ref_page(story)
    event_settings_page(story)
    roping_lighting_page(story)
    lens_page(story)
    positioning_page(story)
    event_calendar_page(story)
    troubleshooting_page(story)
    gear_money_page(story)
    outreach_backcover_page(story)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF created: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
