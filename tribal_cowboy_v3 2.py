"""
Tribal Cowboy Rodeo Photography Field Guide
VERSION 3 — REFINED (not rebuilt)
Improvements: icons, grounding lines, micro-flows, fast-fix rows, arena card
Canon EOS R5 Mark II | 83801 North Idaho | 2026
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
import os

W, H = letter
OUTPUT = os.path.expanduser("~/Desktop/TribalCowboy_Guide_V3_REFINED.pdf")

# ══════════════════════════════════════════════════════════════════
#  COLOR TOKENS
# ══════════════════════════════════════════════════════════════════

class C:
    CREAM        = colors.HexColor("#FAF6EE")
    WARM_TAN     = colors.HexColor("#EDE0C8")
    PARCHMENT    = colors.HexColor("#F5EDE0")
    WHITE        = colors.white

    SAGE         = colors.HexColor("#7A9E82")
    SAGE_DARK    = colors.HexColor("#4A7255")
    SAGE_LIGHT   = colors.HexColor("#D8EAD9")

    ROSE         = colors.HexColor("#C4887A")
    ROSE_LIGHT   = colors.HexColor("#F0DDD8")
    RUST         = colors.HexColor("#A85C42")
    RUST_PALE    = colors.HexColor("#EDD5C8")

    BROWN_DARK   = colors.HexColor("#3D2410")
    BROWN_MID    = colors.HexColor("#7A4A28")
    BROWN_LIGHT  = colors.HexColor("#C4A882")
    BROWN_PALE   = colors.HexColor("#EAD8C0")

    BULL         = colors.HexColor("#8B3A3A")
    BULL_PALE    = colors.HexColor("#F0DADA")
    BARREL       = colors.HexColor("#3A6B5A")
    BARREL_PALE  = colors.HexColor("#D8EDEA")
    ROPE         = colors.HexColor("#7A5F28")
    ROPE_PALE    = colors.HexColor("#EDE5C8")
    GENERAL      = colors.HexColor("#5A6B8A")
    GENERAL_PALE = colors.HexColor("#DAE2ED")

    GREEN        = colors.HexColor("#4A7255")
    GREEN_BG     = colors.HexColor("#D8EAD9")
    YELLOW       = colors.HexColor("#8A6E20")
    YELLOW_BG    = colors.HexColor("#F0E5C0")
    RED          = colors.HexColor("#8B3A3A")
    RED_BG       = colors.HexColor("#F0DADA")

    RULE         = colors.HexColor("#D4C4A8")
    SHADOW       = colors.HexColor("#E8DCC8")


# ══════════════════════════════════════════════════════════════════
#  ICON DRAWING  — editorial shapes, no external fonts
# ══════════════════════════════════════════════════════════════════

def draw_icon(c, cx, cy, size, icon, color):
    """
    Draw simple editorial icons at center (cx, cy).
    icon: 'shutter' | 'af' | 'burst' | 'animal' | 'preshot' | 'light' | 'eye'
    """
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.setLineWidth(1.0)

    if icon == "shutter":
        # Aperture ring: outer circle + inner dot
        c.circle(cx, cy, size, fill=0, stroke=1)
        c.circle(cx, cy, size * 0.38, fill=1, stroke=0)
        # 4 blades
        for ang in [45, 135, 225, 315]:
            import math
            r = math.radians(ang)
            x1 = cx + math.cos(r) * size * 0.45
            y1 = cy + math.sin(r) * size * 0.45
            x2 = cx + math.cos(r) * size * 0.85
            y2 = cy + math.sin(r) * size * 0.85
            c.line(x1, y1, x2, y2)

    elif icon == "af":
        # Four corner brackets
        b = size * 0.55
        t = size * 0.22
        lw = 1.3
        c.setLineWidth(lw)
        for sx, sy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            x, y = cx + sx * b, cy + sy * b
            c.line(x, y, x + sx * (-t), y)
            c.line(x, y, x, y + sy * (-t))

    elif icon == "burst":
        # Three vertical bars side by side
        bw = size * 0.28
        bh = size * 0.9
        gap = size * 0.18
        for i in range(3):
            bx = cx - size * 0.55 + i * (bw + gap)
            c.roundRect(bx, cy - bh / 2, bw, bh, 1.5, fill=1, stroke=0)

    elif icon == "animal":
        # Simple horse silhouette: oval body + oval head
        import math
        c.saveState()
        c.translate(cx, cy)
        # Body
        c.ellipse(-size*0.55, -size*0.25, size*0.55, size*0.22, fill=1, stroke=0)
        # Head (offset up-right)
        c.ellipse(size*0.15, size*0.1, size*0.7, size*0.55, fill=1, stroke=0)
        # Ear (small triangle)
        p = c.beginPath()
        p.moveTo(size*0.35, size*0.52)
        p.lineTo(size*0.5, size*0.78)
        p.lineTo(size*0.62, size*0.52)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        # Leg stubs
        for lx in [-size*0.35, -size*0.1, size*0.15, size*0.4]:
            c.rect(lx, -size*0.62, size*0.12, size*0.38, fill=1, stroke=0)
        c.restoreState()

    elif icon == "preshot":
        # Clock circle with a back-arrow
        c.circle(cx, cy, size, fill=0, stroke=1)
        import math
        # Clock hand pointing up-left (back in time)
        c.setLineWidth(1.4)
        c.line(cx, cy, cx - size * 0.5, cy + size * 0.5)
        c.line(cx, cy, cx + size * 0.1, cy + size * 0.65)
        # Small arrow at tip
        r = math.radians(135)
        ax = cx - size * 0.5
        ay = cy + size * 0.5
        c.line(ax, ay, ax + size*0.2, ay)
        c.line(ax, ay, ax, ay - size*0.2)

    elif icon == "light":
        # Sun: circle + 6 rays
        c.circle(cx, cy, size * 0.42, fill=1, stroke=0)
        import math
        for i in range(6):
            r = math.radians(i * 60)
            x1 = cx + math.cos(r) * size * 0.56
            y1 = cy + math.sin(r) * size * 0.56
            x2 = cx + math.cos(r) * size * 0.9
            y2 = cy + math.sin(r) * size * 0.9
            c.setLineWidth(1.2)
            c.line(x1, y1, x2, y2)

    elif icon == "eye":
        # Eye: almond shape + pupil
        c.setLineWidth(1.0)
        import math
        # Almond using bezier approximation via lines
        pts = 16
        top_pts = [(cx + size * math.cos(math.radians(i * 180 / pts)),
                    cy + size * 0.45 * math.sin(math.radians(i * 180 / pts)))
                   for i in range(pts + 1)]
        bot_pts = [(cx + size * math.cos(math.radians(180 + i * 180 / pts)),
                    cy - size * 0.45 * math.sin(math.radians(180 + i * 180 / pts)))
                   for i in range(pts + 1)]
        p = c.beginPath()
        p.moveTo(*top_pts[0])
        for pt in top_pts[1:]: p.lineTo(*pt)
        for pt in bot_pts[1:]: p.lineTo(*pt)
        p.close()
        c.drawPath(p, fill=0, stroke=1)
        c.circle(cx, cy, size * 0.28, fill=1, stroke=0)


# ══════════════════════════════════════════════════════════════════
#  TYPE STYLES
# ══════════════════════════════════════════════════════════════════

def build_styles():
    base = getSampleStyleSheet()
    def S(name, **kw):
        base.add(ParagraphStyle(name=name, **kw))

    S("Purpose",      fontName="Times-Italic",     fontSize=11, textColor=C.BROWN_MID,
      leading=14, spaceAfter=0, alignment=TA_CENTER)
    S("L1Head",       fontName="Times-Bold",        fontSize=15, textColor=C.BROWN_DARK,
      leading=19, spaceBefore=12, spaceAfter=4)
    S("L2Head",       fontName="Times-Bold",        fontSize=12, textColor=C.BROWN_MID,
      leading=16, spaceBefore=10, spaceAfter=3)
    S("L3Head",       fontName="Times-Italic",      fontSize=10, textColor=C.BROWN_LIGHT,
      leading=13, spaceBefore=6, spaceAfter=2)
    S("Body",         fontName="Helvetica",         fontSize=9,  textColor=C.BROWN_MID,
      leading=14, spaceAfter=2)
    S("BodyBold",     fontName="Helvetica-Bold",    fontSize=9,  textColor=C.BROWN_DARK,
      leading=14, spaceAfter=2)
    S("CBullet",      fontName="Helvetica",         fontSize=9,  textColor=C.BROWN_MID,
      leading=13, leftIndent=12, firstLineIndent=-8, spaceAfter=1)
    S("Grounding",    fontName="Times-Italic",      fontSize=11, textColor=C.SAGE_DARK,
      leading=16, spaceAfter=4, alignment=TA_CENTER)
    S("GroundingSmall", fontName="Times-Italic",    fontSize=9,  textColor=C.SAGE_DARK,
      leading=12, spaceAfter=2, alignment=TA_CENTER)
    S("CardTitle",    fontName="Helvetica-Bold",    fontSize=8,  textColor=C.BROWN_LIGHT,
      leading=11)
    S("CardValue",    fontName="Times-Bold",        fontSize=18, textColor=C.BROWN_DARK,
      leading=22)
    S("CardWhy",      fontName="Helvetica",         fontSize=8,  textColor=C.BROWN_MID,
      leading=11)
    S("Footer",       fontName="Helvetica",         fontSize=7,  textColor=C.BROWN_LIGHT,
      leading=9, alignment=TA_CENTER)
    S("MicroStep",    fontName="Helvetica-Bold",    fontSize=8,  textColor=C.BROWN_DARK,
      leading=11, alignment=TA_CENTER)
    S("MicroLabel",   fontName="Helvetica",         fontSize=7,  textColor=C.BROWN_LIGHT,
      leading=10, alignment=TA_CENTER)
    S("ExpandBody",   fontName="Helvetica",         fontSize=8,  textColor=C.BROWN_LIGHT,
      leading=12)
    S("CoverMain",    fontName="Times-Bold",        fontSize=44, textColor=C.BROWN_DARK,
      leading=52, alignment=TA_CENTER)
    S("CoverSub",     fontName="Times-Italic",      fontSize=18, textColor=C.RUST,
      leading=24, alignment=TA_CENTER)
    S("CoverMeta",    fontName="Helvetica",         fontSize=9,  textColor=C.BROWN_MID,
      leading=13, alignment=TA_CENTER)
    return base

ST = build_styles()


# ══════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════

def sp(h=8):
    return Spacer(1, h)

def p(t, s="Body"):
    return Paragraph(t, ST[s])

def rule(c=C.RULE, t=0.5):
    return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=4, spaceBefore=4)

def grounding(text):
    """Calm, centred, italic line — 'you only need these 3 settings'"""
    return Paragraph(text, ST["Grounding"])

def grounding_sm(text):
    return Paragraph(text, ST["GroundingSmall"])


# ══════════════════════════════════════════════════════════════════
#  CORE FLOWABLES (refined)
# ══════════════════════════════════════════════════════════════════

class PagePurposeBar(Flowable):
    """Top-of-page banner with level pill + purpose statement."""
    def __init__(self, purpose, level=1, label="USE THIS FIRST"):
        self.purpose = purpose
        self.level   = level
        self.label   = label
        self.height  = 46

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(C.WARM_TAN)
        c.roundRect(0, 4, self.width, 40, 6, fill=1, stroke=0)
        bar_c = {1: C.RUST, 2: C.SAGE, 3: C.BROWN_LIGHT}[self.level]
        c.setFillColor(bar_c)
        c.roundRect(0, 4, 6, 40, 4, fill=1, stroke=0)
        # Level pill
        pill_w = len(self.label) * 5.6 + 16
        c.roundRect(14, 28, pill_w, 13, 4, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(14 + pill_w / 2, 32, self.label)
        # Purpose text
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Times-Italic", 11)
        c.drawString(14, 10, self.purpose)


class IconSettingCard(Flowable):
    """
    REFINED setting card:
    - Icon top-right (drawn)
    - Label small + grey (verb-first)
    - Value LARGE + bold
    - Status dot prominent
    - Why text trimmed to one line
    """
    def __init__(self, label, value, why, status="green",
                 accent=C.RUST, icon="shutter", width=None):
        self.label  = label
        self.value  = value
        self.why    = why
        self.status = status
        self.accent = accent
        self.icon   = icon
        self._w     = width
        self.height = 78

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(C.CREAM)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        # Left accent bar — thicker for L1
        c.setFillColor(self.accent)
        c.roundRect(0, 0, 6, self.height, 5, fill=1, stroke=0)
        # Status dot (larger, top-right)
        dot_c = {"green": C.GREEN, "yellow": C.YELLOW, "red": C.RED}[self.status]
        c.setFillColor(dot_c)
        c.circle(self.width - 14, self.height - 14, 7, fill=1, stroke=0)
        # Icon (bottom-right, subtle)
        draw_icon(c, self.width - 14, 14, 6, self.icon, C.BROWN_PALE)
        # Label (verb-first, small, grey)
        c.setFillColor(C.BROWN_LIGHT)
        c.setFont("Helvetica", 7)
        c.drawString(14, self.height - 14, self.label.upper())
        # Value (large, confident)
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Times-Bold", 17)
        c.drawString(14, self.height - 36, self.value)
        # Thin divider
        c.setStrokeColor(C.RULE)
        c.setLineWidth(0.4)
        c.line(14, self.height - 44, self.width - 14, self.height - 44)
        # Why — one tight line
        c.setFillColor(C.BROWN_MID)
        c.setFont("Helvetica", 8)
        max_c = int((self.width - 28) / 4.4)
        txt = self.why[:max_c] + ("…" if len(self.why) > max_c else "")
        c.drawString(14, self.height - 56, txt)
        # Bottom grounding note (verb-first micro-instruction)
        c.setFillColor(dot_c)
        c.setFont("Helvetica-Bold", 7)
        status_txt = {"green": "DEFAULT — leave it", "yellow": "ADJUST if needed", "red": "SET THIS NOW"}[self.status]
        c.drawString(14, 6, status_txt)


class GroundingBar(Flowable):
    """Full-width calm grounding statement — sage, italic, centred."""
    def __init__(self, text, height=30):
        self.text   = text
        self.height = height

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(C.SAGE_LIGHT)
        c.roundRect(0, 2, self.width, self.height - 2, 6, fill=1, stroke=0)
        c.setFillColor(C.SAGE_DARK)
        c.setFont("Times-Italic", 10.5)
        c.drawCentredString(self.width / 2, self.height / 2 - 4, self.text)


class OverwhelmedBox(Flowable):
    """'If overwhelmed → do this' grounding shortcut — sage."""
    def __init__(self, steps):
        self.steps  = steps[:3]
        self.height = 26 + len(self.steps) * 19 + 8

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(C.SAGE_LIGHT)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        c.setFillColor(C.SAGE_DARK)
        c.roundRect(0, self.height - 24, self.width, 24, 6, fill=1, stroke=0)
        c.rect(0, self.height - 14, self.width, 14, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(12, self.height - 17, "IF OVERWHELMED  ->  START HERE")
        y = self.height - 40
        for i, step in enumerate(self.steps, 1):
            c.setFillColor(C.SAGE)
            c.circle(14, y + 5, 8, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(14, y + 2, str(i))
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica", 9)
            c.drawString(30, y + 1, step)
            y -= 19


class MicroFlow(Flowable):
    """
    NEW: Inline 3-5 step decision chain.
    Reads left-to-right in under 3 seconds.
    steps = list of (label, sublabel) tuples
    """
    def __init__(self, steps, accent=C.BULL):
        self.steps  = steps[:5]
        self.accent = accent
        self.height = 52

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c  = self.canv
        n  = len(self.steps)
        aw = self.width
        # node width and gap
        node_w = min(110, (aw - (n - 1) * 18) / n)
        arrow_w = 18
        total_w = n * node_w + (n - 1) * arrow_w
        x_start = (aw - total_w) / 2
        cy = self.height / 2

        for i, (label, sub) in enumerate(self.steps):
            x = x_start + i * (node_w + arrow_w)
            # Alternate shading: first = accent, rest = pale
            bg = self.accent if i == 0 else C.CREAM
            fg = C.WHITE if i == 0 else C.BROWN_DARK
            sub_c = C.CREAM if i == 0 else C.BROWN_LIGHT
            c.setFillColor(bg)
            c.roundRect(x, cy - 17, node_w, 34, 5, fill=1, stroke=0)
            # Subtle border on non-accent cards
            if i != 0:
                c.setStrokeColor(C.RULE)
                c.setLineWidth(0.5)
                c.roundRect(x, cy - 17, node_w, 34, 5, fill=0, stroke=1)
            c.setFillColor(fg)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(x + node_w / 2, cy + 4, label)
            c.setFillColor(sub_c)
            c.setFont("Helvetica", 7)
            c.drawCentredString(x + node_w / 2, cy - 10, sub)
            # Arrow (not after last)
            if i < n - 1:
                ax = x + node_w + 2
                c.setFillColor(C.BROWN_LIGHT)
                p2 = c.beginPath()
                p2.moveTo(ax, cy - 5)
                p2.lineTo(ax + arrow_w - 5, cy)
                p2.lineTo(ax, cy + 5)
                p2.close()
                c.drawPath(p2, fill=1, stroke=0)


class FastFixTable(Flowable):
    """
    NEW: Two-column problem/action table.
    Left = problem (rose), Right = action (cream).
    Scannable in 1-2 seconds per row.
    """
    def __init__(self, rows, accent=C.BULL):
        self.rows   = rows   # list of (problem, action)
        self.accent = accent
        self.row_h  = 22
        self.height = 28 + len(rows) * self.row_h

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        lw = self.width * 0.38
        rw = self.width - lw
        # Header
        c.setFillColor(self.accent)
        c.roundRect(0, self.height - 26, self.width, 26, 6, fill=1, stroke=0)
        c.rect(0, self.height - 16, self.width, 16, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(10, self.height - 18, "IF THIS HAPPENS")
        c.setFont("Helvetica-Bold", 8)
        c.drawString(lw + 10, self.height - 18, "DO THIS")

        for i, (prob, action) in enumerate(self.rows):
            y = self.height - 28 - i * self.row_h
            bg = C.ROSE_LIGHT if i % 2 == 0 else C.CREAM
            # Left cell
            c.setFillColor(bg)
            c.rect(0, y - self.row_h + 4, lw, self.row_h, fill=1, stroke=0)
            c.setFillColor(C.BULL)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(10, y - self.row_h + 9, prob)
            # Right cell
            c.setFillColor(C.CREAM if i % 2 == 0 else C.PARCHMENT)
            c.rect(lw, y - self.row_h + 4, rw, self.row_h, fill=1, stroke=0)
            c.setFillColor(C.SAGE_DARK)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(lw + 10, y - self.row_h + 9, action)
            # Divider line
            c.setStrokeColor(C.RULE)
            c.setLineWidth(0.3)
            c.line(0, y - self.row_h + 4, self.width, y - self.row_h + 4)

        # Outer border
        c.setStrokeColor(C.RULE)
        c.setLineWidth(0.5)
        c.roundRect(0, 0, self.width, self.height, 6, fill=0, stroke=1)


class InfoChunk(Flowable):
    """Calm grouped info — max 4 items, soft background, never urgent."""
    def __init__(self, title, items, accent=C.SAGE, bg=C.SAGE_LIGHT, width=None):
        self.title  = title
        self.items  = items[:4]
        self.accent = accent
        self.bg     = bg
        self._w     = width
        self.height = 30 + len(self.items) * 17 + 8

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.width, self.height, 7, fill=1, stroke=0)
        c.setFillColor(self.accent)
        c.roundRect(0, self.height - 24, self.width, 24, 6, fill=1, stroke=0)
        c.rect(0, self.height - 14, self.width, 14, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(10, self.height - 18, self.title.upper())
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Helvetica", 8.5)
        y = self.height - 38
        for item in self.items:
            c.setFillColor(self.accent)
            c.circle(10, y + 4, 2.5, fill=1, stroke=0)
            c.setFillColor(C.BROWN_DARK)
            c.drawString(18, y, item)
            y -= 17


class ExpandSection(Flowable):
    """L3 optional detail — dashed border, faded look."""
    def __init__(self, rows):
        self.rows   = rows
        self.height = 22 + len(rows) * 16 + 6

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(C.RULE)
        c.setLineWidth(0.5)
        c.setDash([4, 3])
        c.roundRect(0, 0, self.width, self.height, 5, fill=0, stroke=1)
        c.setDash([])
        c.setFillColor(C.WHITE)
        c.rect(8, self.height - 12, 145, 10, fill=1, stroke=0)
        c.setFillColor(C.BROWN_LIGHT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(12, self.height - 10, "v  ONLY IF YOU NEED MORE")
        y = self.height - 26
        for label, val in self.rows:
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica-Bold", 7.5)
            c.drawString(12, y, label + ":")
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica", 7.5)
            c.drawString(12 + len(label) * 4.8 + 10, y, val)
            y -= 16


class EventBanner(Flowable):
    """Section event banner — elegant, not loud."""
    def __init__(self, title, subtitle="", accent=C.BULL, pale=C.BULL_PALE):
        self.title    = title
        self.subtitle = subtitle
        self.accent   = accent
        self.pale     = pale
        self.height   = 54

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.pale)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        c.setFillColor(self.accent)
        c.rect(0, 0, self.width, 4, fill=1, stroke=0)
        c.rect(0, 0, 8, self.height, fill=1, stroke=0)
        c.setFillColor(self.accent)
        c.setFont("Times-Bold", 21)
        c.drawString(20, 30, self.title)
        if self.subtitle:
            c.setFillColor(C.BROWN_MID)
            c.setFont("Times-Italic", 9.5)
            c.drawString(20, 14, self.subtitle)


class StartHereArrow(Flowable):
    def __init__(self, text="START HERE"):
        self.text   = text
        self.height = 26

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        tw = len(self.text) * 6.5 + 24
        c.setFillColor(C.RUST)
        c.roundRect(0, 4, tw, 18, 5, fill=1, stroke=0)
        p2 = c.beginPath()
        p2.moveTo(tw, 4)
        p2.lineTo(tw + 14, 13)
        p2.lineTo(tw, 22)
        p2.close()
        c.drawPath(p2, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(10, 10, self.text)


def two_col(left, right, lw=3.45*inch, rw=3.45*inch):
    t = Table([[left, sp(8), right]], colWidths=[lw, 0.15*inch, rw])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return t

def three_col(a, b, cc, w=2.3*inch):
    t = Table([[a, sp(6), b, sp(6), cc]], colWidths=[w, 0.1*inch, w, 0.1*inch, w])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return t


# ══════════════════════════════════════════════════════════════════
#  PAGE TEMPLATE
# ══════════════════════════════════════════════════════════════════

def on_page(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(C.RULE)
        canvas.setLineWidth(0.4)
        canvas.line(0.65*inch, H - 0.38*inch, W - 0.65*inch, H - 0.38*inch)
        canvas.setFillColor(C.BROWN_MID)
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.drawString(0.65*inch, H - 0.30*inch, "TRIBAL COWBOY  —  RODEO FIELD GUIDE")
        canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(W - 0.65*inch, H - 0.30*inch, f"Canon R5 Mark II  |  p.{doc.page}")
        canvas.setStrokeColor(C.RULE)
        canvas.line(0.65*inch, 0.38*inch, W - 0.65*inch, 0.38*inch)
        canvas.setFillColor(C.BROWN_LIGHT)
        canvas.setFont("Helvetica", 7)
        canvas.drawCentredString(W/2, 0.24*inch,
            "North Idaho  /  Eastern Washington  |  83801  |  250-Mile Radius")
    canvas.restoreState()


# ══════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════

def cover(story):
    class CoverPage(Flowable):
        def wrap(self, aw, ah): return aw, ah
        def draw(self):
            c = self.canv
            c.setFillColor(C.CREAM)
            c.rect(-inch, -inch, W + 2*inch, H + 2*inch, fill=1, stroke=0)
            c.setFillColor(C.WARM_TAN)
            c.rect(-inch, H * 0.70, W + 2*inch, H * 0.33, fill=1, stroke=0)
            c.setFillColor(C.SAGE_LIGHT)
            c.rect(-inch, -inch, W + 2*inch, H * 0.22, fill=1, stroke=0)
            c.setFillColor(C.RUST)
            c.rect(-inch, H * 0.70 - 4, W + 2*inch, 4, fill=1, stroke=0)
            c.setFillColor(C.ROSE_LIGHT)
            c.rect(-inch, H * 0.70 - 9, W + 2*inch, 3, fill=1, stroke=0)
            c.setFillColor(C.RUST)
            c.rect(-inch, H * 0.19 + 3, W + 2*inch, 4, fill=1, stroke=0)
            c.setFillColor(C.ROSE_LIGHT)
            c.rect(-inch, H * 0.19 + 9, W + 2*inch, 3, fill=1, stroke=0)
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Times-Bold", 48)
            c.drawCentredString(W/2, H * 0.55, "Tribal Cowboy")
            c.setFillColor(C.RUST)
            c.setFont("Times-Italic", 21)
            c.drawCentredString(W/2, H * 0.475, "Rodeo Photography Field Guide")
            c.setFillColor(C.RUST)
            c.rect(2.0*inch, H * 0.455, 4.0*inch, 2, fill=1, stroke=0)
            c.setFillColor(C.RUST)
            c.setFont("Helvetica-Bold", 10.5)
            c.drawCentredString(W/2, H * 0.415, "CANON EOS R5 MARK II  —  VERSION 3  REFINED")
            c.setFillColor(C.SAGE_DARK)
            c.setFont("Times-Italic", 13)
            c.drawCentredString(W/2, H * 0.365,
                "Open it under pressure. Know what to do. Without thinking.")
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica", 9)
            c.drawCentredString(W/2, H * 0.115,
                "83801 Careywood, ID  |  250-Mile Radius  |  2026")
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Times-Italic", 10)
            c.drawCentredString(W/2, H * 0.075,
                "Millie  *  Abby  *  Jolene  *  Monster  *  Master Chief")
            # Level system pills (bottom right)
            for i, (lbl, col) in enumerate([
                ("L1  SET THIS NOW",  C.RUST),
                ("L2  WHEN NEEDED",   C.SAGE_DARK),
                ("L3  DEEP DIVE",     C.BROWN_LIGHT),
            ]):
                bx = W - 1.7*inch
                by = H * 0.115 + i * 20
                c.setFillColor(col)
                c.roundRect(bx, by, 112, 14, 4, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold", 7)
                c.drawString(bx + 8, by + 4, lbl)

    story.append(CoverPage())
    story.append(PageBreak())


# ─── HOW TO USE ───────────────────────────────────────────────────
def how_to_use(story):
    story.append(PagePurposeBar(
        "Understand the system once. Then never think about it again.",
        level=1, label="READ THIS FIRST"))
    story.append(sp(10))

    story.append(OverwhelmedBox([
        "Open Quick Reference (next page)",
        "Find your event — set those 3 settings only",
        "Raise the camera. Shoot.",
    ]))
    story.append(sp(12))
    story.append(GroundingBar("You do not need to read all of this. Start with L1. That's enough."))
    story.append(sp(12))

    # 3-level system visual
    story.append(p("<b>Three layers. Pick the one you need.</b>", "L1Head"))
    story.append(sp(8))

    class LevelCard(Flowable):
        def __init__(self, n, tag, desc, note, col):
            self.n=n; self.tag=tag; self.desc=desc; self.note=note; self.col=col
            self.height = 92
        def wrap(self, aw, ah):
            self.width = aw; return aw, self.height
        def draw(self):
            c = self.canv
            c.setFillColor(C.CREAM)
            c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
            c.setFillColor(self.col)
            c.roundRect(0,self.height-34,self.width,34,6,fill=1,stroke=0)
            c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Times-Bold",14)
            c.drawCentredString(self.width/2, self.height-14, self.n)
            c.setFont("Helvetica-Bold",8)
            c.drawCentredString(self.width/2, self.height-27, self.tag)
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica-Bold",8.5)
            y = self.height-46
            for ln in self.desc.split("|"):
                c.drawCentredString(self.width/2, y, ln.strip()); y-=12
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica-Oblique",7.5)
            c.drawCentredString(self.width/2, 8, self.note)

    cards = [
        LevelCard("L1","SET THIS NOW",
                  "3 settings max.|Big text. Red status dot.",
                  "Can't miss it.", C.RUST),
        LevelCard("L2","WHEN NEEDED",
                  "More context.|Only when something's wrong.",
                  "Calm. Not urgent.", C.SAGE_DARK),
        LevelCard("L3","DEEP DIVE",
                  "Optional detail.|Dashed border = skip it.",
                  "You may never need this.", C.BROWN_LIGHT),
    ]
    story.append(three_col(*cards))
    story.append(sp(12))
    story.append(rule())
    story.append(sp(6))

    # Status dot legend
    story.append(p("<b>Status dots on every card:</b>", "BodyBold"))
    story.append(sp(6))

    class DotLegend(Flowable):
        def wrap(self, aw, ah):
            self.width = aw; return aw, 26
        def draw(self):
            c = self.canv
            items = [
                (C.GREEN,  C.GREEN_BG,  "DEFAULT — leave it"),
                (C.YELLOW, C.YELLOW_BG, "ADJUST — only if conditions change"),
                (C.RED,    C.RED_BG,    "SET THIS NOW — non-negotiable"),
            ]
            x = 0
            w = self.width / 3 - 6
            for fg, bg, label in items:
                c.setFillColor(bg)
                c.roundRect(x, 2, w, 22, 5, fill=1, stroke=0)
                c.setFillColor(fg)
                c.circle(x+14, 13, 6, fill=1, stroke=0)
                c.setFont("Helvetica-Bold", 8)
                c.drawString(x+26, 9, label)
                x += w + 8

    story.append(DotLegend())
    story.append(sp(12))
    story.append(GroundingBar(
        '"Open it. Find your event. Set the three things. Shoot."'))
    story.append(PageBreak())


# ─── QUICK REFERENCE (REFINED) ───────────────────────────────────
def quick_reference(story):
    story.append(PagePurposeBar(
        "Four events. Three settings each. Find yours in under 5 seconds.",
        level=1, label="L1 — USE THIS FIRST"))
    story.append(sp(8))
    story.append(StartHereArrow("PICK YOUR EVENT BELOW"))
    story.append(sp(8))

    # Grounding statement
    story.append(GroundingBar("You only need these settings. Ignore everything else."))
    story.append(sp(10))

    # ── 4 event cards 2x2 ──────────────────────────────────────
    def event_qr_card(title, color, pale, settings, icon_set):
        """settings = [(label, value, status, icon), ...] max 3"""
        class EC(Flowable):
            def __init__(self):
                self.height = 218
            def wrap(self, aw, ah):
                self.width = aw; return aw, self.height
            def draw(self):
                c = self.canv
                # Card bg
                c.setFillColor(pale)
                c.roundRect(0,0,self.width,self.height,9,fill=1,stroke=0)
                # Header
                c.setFillColor(color)
                c.roundRect(0,self.height-36,self.width,36,8,fill=1,stroke=0)
                c.rect(0,self.height-20,self.width,20,fill=1,stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Times-Bold",15)
                c.drawString(12,self.height-26,title)
                # 3 setting sub-cards
                y = self.height-50
                rh = 50
                for i,(lbl,val,sts,icn) in enumerate(settings[:3]):
                    bg = C.WHITE
                    c.setFillColor(bg)
                    c.roundRect(8,y,self.width-16,rh-2,5,fill=1,stroke=0)
                    # Left bar = status color
                    dot_c = {"green":C.GREEN,"yellow":C.YELLOW,"red":C.RED}[sts]
                    c.setFillColor(dot_c)
                    c.roundRect(8,y,4,rh-2,3,fill=1,stroke=0)
                    # Icon (small, top-right of sub-card)
                    draw_icon(c, self.width-22, y+rh-14, 5, icn, C.BROWN_PALE)
                    # Label
                    c.setFillColor(C.BROWN_LIGHT)
                    c.setFont("Helvetica",7)
                    c.drawString(18,y+rh-15,lbl.upper())
                    # Value
                    c.setFillColor(color)
                    c.setFont("Times-Bold",14)
                    c.drawString(18,y+8,val)
                    y -= rh + 4
        return EC()

    bull_c  = event_qr_card("BULL RIDING",   C.BULL,    C.BULL_PALE,  [
        ("Set shutter",    "1/2000–3200",  "red",    "shutter"),
        ("AF subject",     "Animals + Eye","green",  "animal"),
        ("Drive + pre-shot","H+ 30fps MAX","green",  "preshot"),
    ], None)
    barrel_c= event_qr_card("BARREL RACING", C.BARREL,  C.BARREL_PALE,[
        ("Set shutter min","1/1600",       "red",    "shutter"),
        ("Aperture",       "f/2.8–f/4",   "green",  "light"),
        ("Drive + pre-shot","H+ 30fps MED","green",  "preshot"),
    ], None)
    rope_c  = event_qr_card("ROPING",        C.ROPE,    C.ROPE_PALE,  [
        ("Set shutter",    "1/2000",       "red",    "shutter"),
        ("Aperture",       "f/5.6",        "green",  "light"),
        ("Pre-shot",       "MAX — 30fr",   "green",  "preshot"),
    ], None)
    gen_c   = event_qr_card("GENERAL/CROWD", C.GENERAL, C.GENERAL_PALE,[
        ("Shutter min",    "1/1250",       "yellow", "shutter"),
        ("AF subject",     "People + Face","green",  "eye"),
        ("Drive",          "H 12fps",      "green",  "burst"),
    ], None)

    grid = Table(
        [[bull_c,  sp(10), barrel_c],
         [sp(6),   sp(10), sp(6)],
         [rope_c,  sp(10), gen_c]],
        colWidths=[3.5*inch, 0.2*inch, 3.5*inch])
    grid.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(grid)
    story.append(sp(10))
    story.append(rule())

    # Shutter mode strip — verb first, short
    story.append(p("<b>Shutter mode</b> — one decision:", "BodyBold"))
    story.append(sp(6))

    class ShutterStrip(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 32
        def draw(self):
            c = self.canv
            items = [
                ("Daylight or LED",        "ELEC. 1ST CURTAIN", C.SAGE_DARK),
                ("Night / flickering LED", "MECHANICAL",        C.BULL),
                ("Silent portraits",       "ELECTRONIC",        C.GENERAL),
            ]
            w = (self.width - 16) / 3
            x = 0
            for label, mode, col in items:
                c.setFillColor(col)
                c.roundRect(x, 2, w, 28, 5, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica",7)
                c.drawString(x+8, 22, label)
                c.setFont("Helvetica-Bold",9.5)
                c.drawString(x+8, 9, mode)
                x += w + 8

    story.append(ShutterStrip())
    story.append(sp(8))
    story.append(ExpandSection([
        ("Night ISO",     "12800  |  1/1000 min shutter  |  Manual mode"),
        ("Animal Track",  "AF Menu 1 > Subject Detect: ANIMALS > Eye Detection: ON"),
        ("Pre-Shot",      "Shooting Menu 4 > Pre-shot Burst > ON > set level"),
        ("Dust",          "Tracking Sensitivity 4-5  |  +1/3 exp comp"),
    ]))
    story.append(PageBreak())


# ─── BULL RIDING (REFINED) ────────────────────────────────────────
def bull_riding(story):
    story.append(EventBanner(
        "Bull Riding",
        "Gate opens. You have 8 seconds. These 3 settings. That's it.",
        accent=C.BULL, pale=C.BULL_PALE))
    story.append(sp(8))
    story.append(PagePurposeBar(
        "Set before the gate opens. Fire at the right moment. Stay behind the rail.",
        level=1, label="L1 — SET THIS NOW"))
    story.append(sp(10))

    story.append(StartHereArrow("SET THESE 3 BEFORE THE CHUTE OPENS"))
    story.append(sp(8))
    story.append(GroundingBar("Three settings. Everything else is already set. You're ready."))
    story.append(sp(10))

    # 3 icon setting cards
    sc1 = IconSettingCard("Set shutter", "1/2000–1/3200",
        "Never lower. Stops the spin cold.",
        status="red", accent=C.BULL, icon="shutter", width=2.3*inch)
    sc2 = IconSettingCard("AF subject", "Animals + Eye ON",
        "Set once. Leave it.",
        status="green", accent=C.SAGE_DARK, icon="animal", width=2.3*inch)
    sc3 = IconSettingCard("Drive + pre-shot", "H+ 30fps  MAX",
        "Pre-shot catches the peak before you react.",
        status="green", accent=C.RUST, icon="preshot", width=2.3*inch)

    story.append(three_col(sc1, sc2, sc3))
    story.append(sp(12))
    story.append(OverwhelmedBox([
        "Set shutter to 1/2000 in Manual mode",
        "Confirm AF Menu > Subject Detect = ANIMALS",
        "Half-press to lock. Wait for the gate.",
    ]))
    story.append(sp(12))
    story.append(rule())

    # L2 — TIMING (micro flow)
    story.append(p("<b>When to fire</b> — four moments that matter", "L2Head"))
    story.append(sp(6))
    story.append(MicroFlow([
        ("Half-press", "before gate opens"),
        ("Gate opens", "pre-shot fires"),
        ("2-3 sec in", "BURST — peak spin"),
        ("Buck-off", "hold through fall"),
    ], accent=C.BULL))
    story.append(sp(10))

    # Two info chunks
    chunk_l = InfoChunk(
        "WATCH THE BULL NOT THE RIDER",
        ["Bull's head leads body by 0.5 sec",
         "Aim AF at head / shoulder",
         "Rider follows — bull decides",
         "Buffer is unlimited — hold the shutter"],
        accent=C.BULL, bg=C.BULL_PALE, width=3.45*inch)

    chunk_r = InfoChunk(
        "IF AF MISBEHAVES",
        ["Wrong subject: tap EVF screen",
         "Dust confusing: Tracking Sens -> 4",
         "Still hunting: Zone Center AF",
         "Post-ride: switch to People detect"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT, width=3.45*inch)

    story.append(two_col(chunk_l, chunk_r))
    story.append(sp(10))
    story.append(rule())

    # Fast Fix table (REFINED — replaces complex decision tree)
    story.append(p("<b>Fix it fast</b>", "L2Head"))
    story.append(sp(6))
    story.append(FastFixTable([
        ("Shot is blurry",          "Raise shutter to 1/2000 minimum"),
        ("Blurry + shutter OK",     "Switch IBIS to Mode 2 (panning)"),
        ("AF lost the subject",     "Tracking Sens -> 4  then tap EVF screen"),
        ("Locked on bullfighter",   "Zone Center AF  then reacquire on bull"),
        ("Missing peak moment",     "Pre-shot -> MAX  half-press 2 sec early"),
        ("Banding at night",        "Switch to Mechanical shutter immediately"),
        ("Buffer filling up",       "Already unlimited on CFexpress — ignore this"),
    ], accent=C.BULL))
    story.append(sp(10))

    story.append(ExpandSection([
        ("Full settings",   "Manual + Auto ISO  |  f/4  |  Servo AF  |  Whole Area"),
        ("Aperture",        "f/4 — DOF buffer for erratic movement"),
        ("Shutter type",    "Elec. 1st Curtain (day)  |  Mechanical (night LED)"),
        ("ISO max",         "12800 — R5 II handles this cleanly"),
        ("After the ride",  "Subject Detect -> PEOPLE for reaction shots"),
    ]))
    story.append(PageBreak())


# ─── BARREL RACING ────────────────────────────────────────────────
def barrel_racing(story):
    story.append(EventBanner(
        "Barrel Racing",
        "Pre-focus on the barrel. Let the horse run into your frame.",
        accent=C.BARREL, pale=C.BARREL_PALE))
    story.append(sp(8))
    story.append(PagePurposeBar(
        "You know exactly where the horse is going. Use that advantage.",
        level=1, label="L1 — SET THIS NOW"))
    story.append(sp(10))

    story.append(GroundingBar("The turn is the shot. Everything else is bonus."))
    story.append(sp(10))

    sc1 = IconSettingCard("Set shutter min", "1/1600",
        "Enforce via Auto ISO minimum shutter.",
        status="red", accent=C.BARREL, icon="shutter", width=2.3*inch)
    sc2 = IconSettingCard("Aperture", "f/2.8 – f/4",
        "Isolates horse from crowd. Leave it here.",
        status="green", accent=C.SAGE_DARK, icon="light", width=2.3*inch)
    sc3 = IconSettingCard("Drive + pre-shot", "H+ 30fps  MED",
        "Burst from 2 strides out through exit.",
        status="green", accent=C.RUST, icon="preshot", width=2.3*inch)

    story.append(three_col(sc1, sc2, sc3))
    story.append(sp(10))

    story.append(MicroFlow([
        ("2 strides out", "start burst"),
        ("Barrel entry", "pre-shot fires"),
        ("Apex turn", "hold burst"),
        ("Exit stride", "stop burst"),
        ("Celebration", "People detect"),
    ], accent=C.BARREL))
    story.append(sp(10))

    chunk_l = InfoChunk(
        "THE MONEY SHOT",
        ["2 strides before: start burst",
         "Through apex: hold it",
         "Dirt/sand spray = the frame to keep",
         "Exit stride = horse power shot"],
        accent=C.BARREL, bg=C.BARREL_PALE, width=3.45*inch)
    chunk_r = InfoChunk(
        "SANDPOINT EXTRA",
        ["Late afternoon: lake behind horse",
         "Position: sun behind you",
         "Golden hour + water = unique content",
         "Pause between riders to reposition"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT, width=3.45*inch)

    story.append(two_col(chunk_l, chunk_r))
    story.append(sp(10))
    story.append(rule())
    story.append(p("<b>Fix it fast</b>", "L2Head"))
    story.append(sp(6))
    story.append(FastFixTable([
        ("Motion blur on horse",      "Set ISO Auto min shutter to 1/1600"),
        ("Blur at f/2.8",             "ISO is forcing slow shutter — raise ISO max"),
        ("AF hunting between barrels","Pre-focus on the barrel — let horse enter frame"),
        ("Tracking losing horse",     "Tracking Sens stays at 3 — pattern is predictable"),
    ], accent=C.BARREL))
    story.append(sp(8))
    story.append(ExpandSection([
        ("Mode",       "Aperture Priority — light shifts as horse moves around pattern"),
        ("ISO max",    "6400 standard  |  12800 evening events"),
        ("After ride", "Switch to People detect for expression shots"),
    ]))
    story.append(PageBreak())


# ─── ROPING ───────────────────────────────────────────────────────
def roping(story):
    story.append(EventBanner(
        "Calf / Team Roping",
        "Watch the rope loop overhead. That's your cue. Fire in 0.5 seconds.",
        accent=C.ROPE, pale=C.ROPE_PALE))
    story.append(sp(8))
    story.append(PagePurposeBar(
        "Pre-shot MAX handles the window you can't see coming.",
        level=1, label="L1 — SET THIS NOW"))
    story.append(sp(10))

    story.append(GroundingBar("Watch the calf, not the rope. The calf tells you where it goes."))
    story.append(sp(10))

    sc1 = IconSettingCard("Set shutter", "1/2000",
        "Freezes rope mid-air. The hero shot.",
        status="red", accent=C.ROPE, icon="shutter", width=2.3*inch)
    sc2 = IconSettingCard("Aperture", "f/5.6",
        "Cross-arena distance needs the depth.",
        status="green", accent=C.SAGE_DARK, icon="light", width=2.3*inch)
    sc3 = IconSettingCard("Pre-shot", "MAX — 30 frames",
        "Rope-to-release = under 0.5 sec. Let pre-shot catch it.",
        status="green", accent=C.RUST, icon="preshot", width=2.3*inch)

    story.append(three_col(sc1, sc2, sc3))
    story.append(sp(10))

    story.append(MicroFlow([
        ("Loop overhead", "half-press held"),
        ("Release", "pre-shot fires"),
        ("Catch", "burst — calf scramble"),
        ("Tie-down", "3 distinct shots"),
    ], accent=C.ROPE))
    story.append(sp(10))

    chunk_l = InfoChunk(
        "THREE SHOTS IN ONE RUN",
        ["Catch — horse sliding, rope tight",
         "Scramble — calf reaction",
         "Tie-down — cowboy on the ground",
         "Burst all three separately"],
        accent=C.ROPE, bg=C.ROPE_PALE, width=3.45*inch)
    chunk_r = InfoChunk(
        "TEAM ROPING NOTE",
        ["Cover header first",
         "Rotate slightly for heeler",
         "After first loop: shift position",
         "AF may lock calf — keep it, good shot"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT, width=3.45*inch)

    story.append(two_col(chunk_l, chunk_r))
    story.append(sp(10))
    story.append(rule())
    story.append(p("<b>Fix it fast</b>", "L2Head"))
    story.append(sp(6))
    story.append(FastFixTable([
        ("AF locks on rope not rider",  "Single center point — aim at horse shoulder"),
        ("Missing the throw",           "Pre-shot already on MAX — fire earlier"),
        ("Rope not sharp",              "Shutter at exactly 1/2000 — not lower"),
        ("AF shifts to calf",           "Keep it — produces great reaction shots"),
    ], accent=C.ROPE))
    story.append(PageBreak())


# ─── GEAR KIT ─────────────────────────────────────────────────────
def gear_kit(story):
    story.append(PagePurposeBar(
        "Pick your lens kit by budget. One primary. One secondary. Done.",
        level=2, label="L2 — WHEN NEEDED"))
    story.append(sp(10))
    story.append(GroundingBar("Start with one primary lens. The rest can wait."))
    story.append(sp(10))

    story.append(p("<b>Primary lens — pick one</b>", "L1Head"))
    story.append(sp(6))

    lens_rows = [
        ("RF 70–200mm f/2.8L IS USM",    C.RUST,      "Close rail  |  Indoor  |  Low light",       "$1,800 used",  "BEST ALL-ROUND"),
        ("RF 100–500mm f/4.5–7.1L IS USM",C.BARREL,   "County fairs  |  Reach  |  Versatile",      "$1,900 used",  "BEST REACH"),
        ("RF 200–800mm f/6.3–9 IS USM",  C.ROPE,      "Large arenas  |  Budget reach",              "$800 new",     "BEST VALUE"),
        ("RF 100–400mm f/5.6–8 IS USM",  C.SAGE_DARK, "Starting out  |  Lightweight",               "$600 new",     "ENTRY POINT"),
    ]

    class LensRow(Flowable):
        def __init__(self, name, col, use, price, badge):
            self.name=name; self.col=col; self.use=use
            self.price=price; self.badge=badge; self.height=36
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.CREAM)
            c.roundRect(0,2,self.width,32,5,fill=1,stroke=0)
            c.setFillColor(self.col)
            c.roundRect(0,2,6,32,4,fill=1,stroke=0)
            c.setFillColor(self.col)
            c.setFont("Helvetica-Bold",9)
            c.drawString(14,21,self.name)
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica",8)
            c.drawString(14,9,self.use)
            bw=len(self.badge)*5.8+14
            c.setFillColor(self.col)
            c.roundRect(self.width-bw-10,12,bw,14,4,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold",7)
            c.drawString(self.width-bw-4,17,self.badge)
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica-Bold",8)
            c.drawRightString(self.width-bw-18,17,self.price)

    for lr in lens_rows:
        story.append(LensRow(*lr))
        story.append(sp(2))

    story.append(sp(10))
    story.append(rule())
    story.append(p("<b>Kit by budget</b> — three tiers", "L2Head"))
    story.append(sp(8))

    class BudgetCard(Flowable):
        def __init__(self, tier, price, items, col, highlight=False):
            self.tier=tier; self.price=price; self.items=items
            self.col=col; self.hl=highlight; self.height=110
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            if self.hl:
                c.setFillColor(self.col)
                c.roundRect(0,0,self.width,self.height,8,fill=1,stroke=0)
                tc=C.WHITE; sc=C.CREAM
            else:
                c.setFillColor(C.CREAM)
                c.roundRect(0,0,self.width,self.height,8,fill=1,stroke=0)
                c.setFillColor(self.col)
                c.roundRect(0,self.height-36,self.width,36,6,fill=1,stroke=0)
                c.rect(0,self.height-20,self.width,20,fill=1,stroke=0)
                tc=C.BROWN_DARK; sc=C.BROWN_MID
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold",9); c.drawString(10,self.height-14,self.tier)
            c.setFont("Times-Bold",20); c.drawString(10,self.height-32,self.price)
            c.setFillColor(sc if not self.hl else C.CREAM)
            y=self.height-50
            for item in self.items:
                c.setFillColor(self.col if not self.hl else C.CREAM)
                c.circle(10,y+4,2.5,fill=1,stroke=0)
                c.setFillColor(tc); c.setFont("Helvetica",8)
                c.drawString(18,y,item); y-=16

    b1 = BudgetCard("STARTING OUT", "$650–900",
        ["RF 100-400mm f/5.6-8","Canon 50mm f/1.8","80% of situations covered"],
        C.SAGE_DARK, False)
    b2 = BudgetCard("WORKING PHOTOGRAPHER", "$2,000–2,500",
        ["RF 70-200mm f/2.8L (used)","RF 35mm f/1.8","Low-light + isolation"],
        C.RUST, True)
    b3 = BudgetCard("FULL KIT", "$4,500–5,500",
        ["RF 100-500mm (used)","RF 70-200 f/2.8 (used)","RF 24-70 f/2.8 (used)"],
        C.BROWN_MID, False)

    story.append(three_col(b1, b2, b3))
    story.append(sp(10))
    story.append(ExpandSection([
        ("EF adapter",    "Canon EF-EOS R (~$100) — full AF + animal tracking on all EF L lenses"),
        ("Do NOT buy",    "EF-S/RF-S crop lenses  |  RF 2x extender on f/5.6+  |  Manual FD lenses"),
        ("Budget option", "Sigma 60-600mm DG DN Sport RF  |  Tamron 150-500mm VXD RF"),
    ]))
    story.append(PageBreak())


# ─── EVENT CALENDAR ───────────────────────────────────────────────
def event_calendar(story):
    story.append(PagePurposeBar(
        "Your year at a glance. Start with Tier 1. Build from there.",
        level=2, label="L2 — WHEN NEEDED"))
    story.append(sp(10))
    story.append(GroundingBar("One event at a time. Tier 1 first. Everything else is optional."))
    story.append(sp(10))

    class TimelineRow(Flowable):
        def __init__(self, month, event, loc, dist, col, note=""):
            self.month=month; self.event=event; self.loc=loc
            self.dist=dist; self.col=col; self.note=note; self.height=42
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(self.col)
            c.roundRect(0,8,62,26,5,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold",9)
            c.drawCentredString(31,18,self.month)
            c.setStrokeColor(C.RULE); c.setLineWidth(1)
            c.line(62,21,76,21)
            c.setFillColor(self.col)
            c.circle(76,21,4,fill=1,stroke=0)
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica-Bold",9.5)
            c.drawString(86,27,self.event)
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica",8)
            c.drawString(86,15,f"{self.loc}  |  {self.dist}")
            if self.note:
                c.setFillColor(C.BROWN_LIGHT)
                c.setFont("Helvetica-Oblique",7.5)
                c.drawString(86,5,self.note)
            # Dist pill
            pw=len(self.dist)*6+16
            px=self.width-pw-4
            c.setFillColor(C.WARM_TAN)
            c.roundRect(px,12,pw,16,4,fill=1,stroke=0)
            c.setFillColor(self.col)
            c.setFont("Helvetica-Bold",8)
            c.drawCentredString(px+pw/2,18,self.dist)

    story.append(p("<b>Tier 1  —  Start here</b>  (no pressure, easiest access)", "L1Head"))
    story.append(sp(4))
    for m,ev,loc,dist,note in [
        ("MAY",  "UM Spring Rodeo",              "Missoula, MT",       "~200 mi","No credentials needed — test everything here"),
        ("JUNE", "Barrel Racing Jackpots",        "Region-wide",        "Varies", "No credentials — build portfolio weekly"),
        ("AUG",  "Sandpoint Bonner County Rodeo", "Sandpoint, ID",      "~60 mi", "Lake backdrop — position for golden hour"),
        ("AUG",  "North Idaho State Fair",        "Coeur d'Alene, ID",  "~40 mi", "Home turf — own this event"),
        ("SEPT", "Latah County Fair",             "Moscow, ID",         "~100 mi","Small, accessible, great practice"),
    ]:
        story.append(TimelineRow(m,ev,loc,dist,C.SAGE_DARK,note))
        story.append(sp(3))

    story.append(sp(8)); story.append(rule())
    story.append(p("<b>Tier 2  —  Build toward these</b>  (mid-level PRCA)", "L2Head"))
    story.append(sp(4))
    for m,ev,loc,dist,note in [
        ("JULY", "Toppenish Rodeo",          "Toppenish, WA",   "~155 mi","First PRCA credential attempt"),
        ("JULY", "Basin City Freedom Rodeo", "Basin City, WA",  "~160 mi","July 4th crowd = family sales"),
        ("AUG",  "Omak Stampede",            "Omak, WA",        "~125 mi","Suicide Race = unique fine art content"),
        ("AUG",  "NW Montana Fair & Rodeo",  "Kalispell, MT",   "~160 mi","120-year tradition"),
        ("SEPT", "Lewiston Roundup",         "Lewiston, ID",    "~65 mi", "Apply 6+ weeks early"),
        ("SEPT", "Walla Walla Fair",         "Walla Walla, WA", "~175 mi","160th anniversary"),
    ]:
        story.append(TimelineRow(m,ev,loc,dist,C.RUST,note))
        story.append(sp(3))

    story.append(sp(8)); story.append(rule())
    story.append(p("<b>Tier 3  —  Long game</b>  (earn these)", "L3Head"))
    story.append(sp(4))
    for m,ev,loc,dist,note in [
        ("LABOR DAY","Ellensburg Rodeo",    "Ellensburg, WA","~140 mi","Top 25 national — goal: Year 2"),
        ("AUG",      "Horse Heaven Round-Up","Kennewick, WA","~165 mi","Big 4 — 5 nights"),
        ("SEPT",     "Pendleton Round-Up",  "Pendleton, OR", "~215 mi","100+ year legacy — goal: Year 2-3"),
    ]:
        story.append(TimelineRow(m,ev,loc,dist,C.BROWN_LIGHT,note))
        story.append(sp(3))

    story.append(PageBreak())


# ─── PRICING ──────────────────────────────────────────────────────
def pricing(story):
    story.append(PagePurposeBar(
        "Published rates only. No negotiating at the gate.",
        level=2, label="L2 — WHEN NEEDED"))
    story.append(sp(10))
    story.append(GroundingBar("Three revenue streams. Pick the one that fits today's event."))
    story.append(sp(10))

    class PriceCard(Flowable):
        def __init__(self, title, col, items):
            self.title=title; self.col=col; self.items=items; self.height=130
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.CREAM)
            c.roundRect(0,0,self.width,self.height,8,fill=1,stroke=0)
            c.setFillColor(self.col)
            c.roundRect(0,self.height-32,self.width,32,6,fill=1,stroke=0)
            c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Times-Bold",12)
            c.drawString(10,self.height-22,self.title)
            y=self.height-46
            for label,price in self.items:
                c.setFillColor(C.BROWN_MID); c.setFont("Helvetica",8.5)
                c.drawString(10,y,label)
                c.setFillColor(self.col); c.setFont("Times-Bold",12)
                c.drawRightString(self.width-10,y,price)
                c.setStrokeColor(C.RULE); c.setLineWidth(0.3)
                c.line(10,y-3,self.width-10,y-3)
                y-=20

    pc1=PriceCard("Digital Downloads", C.SAGE_DARK,[
        ("Single image","$15–20"),
        ("5-image bundle","$55–70"),
        ("All-day package","$125–175"),
        ("Social media pack (5)","$95"),
    ])
    pc2=PriceCard("On-Site Prints", C.RUST,[
        ("4x6 print","$12"),
        ("8x10 print","$28"),
        ("16x20 canvas (45MP)","$175–250"),
        ("Print + digital combo","$40"),
    ])
    pc3=PriceCard("Event Organizer", C.BROWN_MID,[
        ("Event coverage","$500–1,200"),
        ("Social delivery same-day","+$200"),
        ("Sponsor logo overlay","+$150"),
        ("Annual contract (4-6 events)","$2,500–5K"),
    ])
    story.append(three_col(pc1,pc2,pc3))
    story.append(sp(10)); story.append(rule())

    story.append(p("<b>Revenue per event  —  North Idaho market</b>", "L2Head"))
    story.append(sp(6))

    class RevStrip(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 50
        def draw(self):
            c=self.canv
            items=[
                ("Conservative / event","$725",   C.SAGE_DARK),
                ("Optimistic / event",  "$2,350", C.RUST),
                ("10 events conservative","$7,250",  C.BROWN_MID),
                ("10 events optimistic", "$23,500+", C.BULL),
            ]
            w=(self.width-18)/4
            x=0
            for label,amt,col in items:
                c.setFillColor(C.WARM_TAN)
                c.roundRect(x,0,w,48,6,fill=1,stroke=0)
                c.setFillColor(col); c.setFont("Times-Bold",18)
                c.drawCentredString(x+w/2,28,amt)
                c.setFillColor(C.BROWN_MID); c.setFont("Helvetica",7.5)
                c.drawCentredString(x+w/2,14,label)
                x+=w+6

    story.append(RevStrip())
    story.append(sp(8))
    story.append(ExpandSection([
        ("Tools",     "SmugMug or Pic-Time ($15-30/mo) — auto-fulfillment, zero manual labor"),
        ("Avoid",     "Manual email delivery  |  Selling from original cards  |  3+ events/weekend solo"),
        ("B2B",       "Year 1: free coverage  ->  Year 2: lock in annual paid contract"),
    ]))
    story.append(PageBreak())


# ─── OUTREACH + CHECKLIST ─────────────────────────────────────────
def outreach(story):
    story.append(PagePurposeBar(
        "Send the right message. Show up prepared.",
        level=2, label="L2 — WHEN NEEDED"))
    story.append(sp(10))

    class ScriptBox(Flowable):
        def __init__(self, lines, acc=C.RUST, bg=C.RUST_PALE):
            self.lines=lines; self.acc=acc; self.bg=bg
            self.height=len([l for l in lines if l])*13+30
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(self.bg)
            c.roundRect(0,0,self.width,self.height,6,fill=1,stroke=0)
            c.setFillColor(self.acc)
            c.roundRect(0,0,5,self.height,4,fill=1,stroke=0)
            y=self.height-14
            for line in self.lines:
                if line.startswith("**"):
                    c.setFont("Helvetica-Bold",8.5); c.setFillColor(self.acc)
                    c.drawString(14,y,line.replace("**",""))
                elif line=="":
                    y+=4
                else:
                    c.setFont("Helvetica",8.5); c.setFillColor(C.BROWN_MID)
                    c.drawString(14,y,line)
                y-=13

    story.append(p("<b>Email template  —  home turf</b>  (copy, fill brackets, send)", "L1Head"))
    story.append(sp(6))
    story.append(ScriptBox([
        "**Subject: Photography for [Event Name] — Tribal Cowboy",
        "","Hi [Name],",
        "","I'm Stacie with Tribal Cowboy — equine experience and photography, Careywood, North Idaho.",
        "","  - Event images for your social media — free to you",
        "  - Digital gallery sales to participants — I handle everything",
        "  - Full credit and tags in all published content",
        "","No cost to you. Local brand. We know your audience.",
        "","Can we connect this week?   Stacie | Tribal Cowboy | [phone]",
    ]))
    story.append(sp(8))

    story.append(p("<b>DM template  —  barrel racing jackpots</b>  (no credentials needed)", "L2Head"))
    story.append(sp(4))
    story.append(ScriptBox([
        "Hey [Name]! Stacie here — Tribal Cowboy photography out of North Idaho.",
        "I'd love to shoot the barrel racing this [date] and share the gallery",
        "so riders can grab their photos. OK with the organizers?",
    ], acc=C.SAGE_DARK, bg=C.SAGE_LIGHT))
    story.append(sp(10)); story.append(rule())

    story.append(p("<b>Pre-event checklist</b>", "L1Head"))
    story.append(sp(6))

    class Checklist(Flowable):
        def __init__(self, items, acc=C.SAGE_DARK):
            self.items=items; self.acc=acc
            per=(len(items)+1)//2
            self.height=per*20+28
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.WARM_TAN)
            c.roundRect(0,0,self.width,self.height,6,fill=1,stroke=0)
            c.setFillColor(self.acc)
            c.roundRect(0,self.height-24,self.width,24,6,fill=1,stroke=0)
            c.rect(0,self.height-14,self.width,14,fill=1,stroke=0)
            c.setFillColor(C.WHITE); c.setFont("Helvetica-Bold",9)
            c.drawString(12,self.height-17,"BEFORE YOU LEAVE HOME")
            per=(len(self.items)+1)//2
            cw=self.width/2
            for i,item in enumerate(self.items):
                col=i//per; row=i%per
                x=col*cw+12; y=self.height-38-row*20
                c.setStrokeColor(self.acc); c.setFillColor(C.WHITE)
                c.setLineWidth(1); c.roundRect(x,y+2,12,12,2,fill=1,stroke=1)
                c.setFillColor(C.BROWN_DARK); c.setFont("Helvetica",8.5)
                c.drawString(x+16,y+4,item)

    story.append(Checklist([
        "Written confirmation + coordinator name",
        "Printed confirmation + 10 business cards",
        "Flash rules, zone limits confirmed",
        "3x CFexpress cards formatted in-body",
        "3x LP-E6NH batteries charged",
        "AF Menu: Subject Detect = ANIMALS",
        "Pre-shot: Shooting Menu 4 = ON + MAX",
        "C1=Bull  C2=Barrel  C3=General set",
        "Gallery platform ready — test login",
        "Lens cloth in vest pocket",
    ]))
    story.append(PageBreak())


# ─── ARENA CARD (ULTRA MINIMAL — PRINT + LAMINATE) ────────────────
def arena_card(story):
    """
    One page. Ultra minimal. Print this. Laminate it. Bring it.
    No headers, no footer, just the essentials.
    """
    class ArenaCardPage(Flowable):
        def wrap(self, aw, ah):
            self.width = aw
            return aw, ah

        def draw(self):
            c = self.canv
            W2 = self.width
            H2 = 9.5 * inch   # approximate usable height

            # Cream background
            c.setFillColor(C.CREAM)
            c.roundRect(0, 0, W2, H2, 10, fill=1, stroke=0)

            # Title strip
            c.setFillColor(C.BROWN_DARK)
            c.roundRect(0, H2 - 38, W2, 38, 8, fill=1, stroke=0)
            c.rect(0, H2 - 22, W2, 22, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Times-Bold", 14)
            c.drawString(14, H2 - 24, "TRIBAL COWBOY  —  ARENA CARD")
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica", 8)
            c.drawRightString(W2 - 14, H2 - 24,
                "Print  |  Laminate  |  Vest pocket")

            # 4 event columns
            events = [
                ("BULL",    "BULL RIDING",    C.BULL,    C.BULL_PALE,
                 [("SHUTTER", "1/2000+", "red"),
                  ("AF",      "Animals", "green"),
                  ("DRIVE",   "H+ MAX",  "green")]),
                ("BARREL",  "BARREL RACING",  C.BARREL,  C.BARREL_PALE,
                 [("SHUTTER", "1/1600+", "red"),
                  ("APERTURE","f/2.8-4", "green"),
                  ("DRIVE",   "H+ MED",  "green")]),
                ("ROPING",  "ROPING",         C.ROPE,    C.ROPE_PALE,
                 [("SHUTTER", "1/2000", "red"),
                  ("APERTURE","f/5.6",  "green"),
                  ("PRESHOT", "MAX",    "green")]),
                ("GENERAL", "GENERAL",        C.GENERAL, C.GENERAL_PALE,
                 [("SHUTTER", "1/1250+", "yellow"),
                  ("AF",      "People",  "green"),
                  ("DRIVE",   "H 12fps", "green")]),
            ]

            card_w = (W2 - 16) / 4
            card_h = 5.2 * inch
            card_y = H2 - 42 - card_h
            x = 4

            for abbr, title, col, pale, settings in events:
                # Card bg
                c.setFillColor(pale)
                c.roundRect(x, card_y, card_w - 4, card_h, 6, fill=1, stroke=0)
                # Header
                c.setFillColor(col)
                c.roundRect(x, card_y + card_h - 30,
                            card_w - 4, 30, 5, fill=1, stroke=0)
                c.rect(x, card_y + card_h - 16,
                       card_w - 4, 16, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Times-Bold", 11)
                c.drawCentredString(x + (card_w-4)/2,
                                    card_y + card_h - 22, title)
                # Settings
                sy = card_y + card_h - 44
                for lbl, val, sts in settings:
                    dot_c = {
                        "green":  C.GREEN,
                        "yellow": C.YELLOW,
                        "red":    C.RED
                    }[sts]
                    # Mini sub-card
                    c.setFillColor(C.WHITE)
                    c.roundRect(x + 5, sy, card_w - 14, 48, 4, fill=1, stroke=0)
                    c.setFillColor(dot_c)
                    c.roundRect(x + 5, sy, 4, 48, 3, fill=1, stroke=0)
                    c.setFillColor(C.BROWN_LIGHT)
                    c.setFont("Helvetica", 7)
                    c.drawString(x + 14, sy + 36, lbl)
                    c.setFillColor(col)
                    c.setFont("Times-Bold", 15)
                    c.drawString(x + 14, sy + 14, val)
                    sy -= 56

                x += card_w

            # SHUTTER MODE BAR
            bar_y = card_y - 46
            c.setFillColor(C.WARM_TAN)
            c.roundRect(0, bar_y, W2, 40, 6, fill=1, stroke=0)
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(10, bar_y + 26, "SHUTTER MODE:")
            modes = [
                ("Daylight / LED", "ELEC. 1ST CURTAIN", C.SAGE_DARK),
                ("Night / flickering", "MECHANICAL", C.BULL),
                ("Flash use", "MECHANICAL", C.BULL),
            ]
            mx = 120
            for label, mode, col2 in modes:
                c.setFillColor(col2)
                c.roundRect(mx, bar_y + 8, len(mode)*6.5+16, 20, 4, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold", 8)
                c.drawString(mx + 8, bar_y + 14, mode)
                c.setFillColor(C.BROWN_MID)
                c.setFont("Helvetica", 7)
                c.drawString(mx + len(mode)*6.5 + 22, bar_y + 14, "= " + label)
                mx += len(mode)*6.5 + len(label)*4.5 + 42

            # IF OVERWHELMED strip
            ov_y = bar_y - 38
            c.setFillColor(C.SAGE_LIGHT)
            c.roundRect(0, ov_y, W2, 32, 6, fill=1, stroke=0)
            c.setFillColor(C.SAGE_DARK)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(10, ov_y + 19, "IF OVERWHELMED:")
            steps = [
                "1  Set shutter to 1/2000",
                "2  Confirm AF = Animals",
                "3  Pre-shot = MAX",
                "4  Raise camera. Shoot.",
            ]
            sx = 145
            for step in steps:
                c.setFillColor(C.BROWN_DARK)
                c.setFont("Helvetica-Bold", 8)
                c.drawString(sx, ov_y + 19, step)
                sx += len(step) * 5.2 + 18
                if sx < W2 - 20:
                    c.setFillColor(C.RULE)
                    c.circle(sx - 8, ov_y + 22, 2, fill=1, stroke=0)

            # Fix it fast (compact)
            fix_y = ov_y - 10
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(8, fix_y, "FIX IT FAST:")
            fixes = [
                ("Blurry", "Shutter up"),
                ("AF lost", "Tap screen"),
                ("Night banding", "Mech. shutter"),
                ("Pre-shot miss", "MAX + earlier"),
            ]
            fx = 90
            for prob, fix in fixes:
                c.setFillColor(C.BULL_PALE)
                pw = len(prob)*5.5 + 10
                c.roundRect(fx, fix_y - 4, pw, 14, 3, fill=1, stroke=0)
                c.setFillColor(C.BULL)
                c.setFont("Helvetica-Bold", 7)
                c.drawString(fx + 5, fix_y + 1, prob)
                c.setFillColor(C.BROWN_LIGHT)
                c.setFont("Helvetica", 6)
                c.drawString(fx + pw + 4, fix_y + 1, "->")
                c.setFillColor(C.SAGE_DARK)
                c.setFont("Helvetica-Bold", 7)
                c.drawString(fx + pw + 14, fix_y + 1, fix)
                fx += pw + len(fix)*5 + 30

            # Footer
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Times-Italic", 8)
            c.drawCentredString(W2/2, 6,
                "Tribal Cowboy  *  Canon R5 Mark II  *  tribalcowboy.com")

    story.append(ArenaCardPage())
    story.append(PageBreak())


# ─── MICRO-EDIT RULES PAGE ────────────────────────────────────────
def micro_edit_rules(story):
    story.append(PagePurposeBar(
        "Follow these rules to update any remaining sections yourself.",
        level=3, label="L3 — REFERENCE"))
    story.append(sp(10))

    story.append(p("<b>Micro-edit rules — the checklist</b>", "L1Head"))
    story.append(sp(8))

    rules = [
        ("COPY",    "Verb first",             "Set shutter, not 'The shutter speed should be set to'"),
        ("COPY",    "Shorter",                "'Set once. Leave it.'  not  'Set once in AF Menu 1 and do not change'"),
        ("COPY",    "Remove 'should'",        "'Set to 1/2000' not 'You should set to 1/2000'"),
        ("COPY",    "No long why",            "One-line reason max. Trim the rest to L3."),
        ("GROUPS",  "Max 4 items",            "If a chunk has 5+, split it into two chunks"),
        ("GROUPS",  "Add grounding line",     "Before every L1 section: one sage italic line"),
        ("GROUPS",  "Breathing room",         "Add sp(8) between every section, sp(12) between L levels"),
        ("STATUS",  "Red = non-negotiable",   "Only shutter speed gets red. AF and Drive = green."),
        ("STATUS",  "Yellow = adjust",        "Only when conditions change the setting (dust, night)"),
        ("TABLES",  "Replace with FastFix",   "Any troubleshooting table -> FastFixTable (left/right, no boxes)"),
        ("TABLES",  "Replace with MicroFlow", "Any 'timing' or 'sequence' text -> MicroFlow chain"),
        ("L3",      "Dashed border only",     "L3 = ExpandSection only. Never a table. Never a chart."),
        ("L3",      "Italic + faded",         "L3 content = BROWN_LIGHT color only. Never accent colors."),
        ("TONE",    "No urgency words",       "Remove: critical, important, must, always, never — keep calm"),
        ("TONE",    "Add grounding",          "Every page: one GroundingBar. One OverwhelmedBox if action-heavy."),
        ("ICONS",   "One icon per card",      "shutter / af / burst / animal / preshot / light / eye"),
    ]

    class RulesTable(Flowable):
        def __init__(self, rows):
            self.rows = rows
            self.row_h = 20
            self.height = 28 + len(rows) * self.row_h

        def wrap(self, aw, ah):
            self.width = aw
            return aw, self.height

        def draw(self):
            c = self.canv
            # Header
            c.setFillColor(C.BROWN_DARK)
            c.roundRect(0, self.height - 26, self.width, 26, 6, fill=1, stroke=0)
            c.rect(0, self.height - 14, self.width, 14, fill=1, stroke=0)
            c.setFillColor(C.CREAM)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(10, self.height - 18, "CATEGORY")
            c.drawString(90, self.height - 18, "RULE")
            c.drawString(200, self.height - 18, "EXAMPLE")

            cat_colors = {
                "COPY":   C.RUST,
                "GROUPS": C.SAGE_DARK,
                "STATUS": C.BULL,
                "TABLES": C.BARREL,
                "L3":     C.BROWN_LIGHT,
                "TONE":   C.SAGE,
                "ICONS":  C.ROPE,
            }
            for i, (cat, rule_txt, example) in enumerate(self.rows):
                y = self.height - 28 - i * self.row_h
                bg = C.CREAM if i % 2 == 0 else C.PARCHMENT
                c.setFillColor(bg)
                c.rect(0, y - self.row_h + 4, self.width, self.row_h, fill=1, stroke=0)
                # Cat pill
                col = cat_colors.get(cat, C.BROWN_LIGHT)
                c.setFillColor(col)
                c.roundRect(6, y - self.row_h + 8, 68, 12, 3, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold", 7)
                c.drawCentredString(40, y - self.row_h + 13, cat)
                # Rule
                c.setFillColor(C.BROWN_DARK)
                c.setFont("Helvetica-Bold", 8)
                c.drawString(84, y - self.row_h + 10, rule_txt)
                # Example
                c.setFillColor(C.BROWN_MID)
                c.setFont("Helvetica", 7.5)
                c.drawString(200, y - self.row_h + 10, example)
                # Divider
                c.setStrokeColor(C.RULE)
                c.setLineWidth(0.3)
                c.line(0, y - self.row_h + 4, self.width, y - self.row_h + 4)

    story.append(RulesTable(rules))
    story.append(sp(10))
    story.append(rule())

    story.append(p("<b>Phone version — 3-tap access</b>", "L2Head"))
    story.append(sp(6))
    story.append(InfoChunk(
        "HOW TO SET UP",
        ["Screenshot the Quick Reference page",
         "Screenshot this Arena Card page (last page)",
         "Save both to a pinned album in Photos",
         "Or: duplicate this as a Notion mobile page"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT))
    story.append(sp(8))
    story.append(GroundingBar(
        '"Three settings. Any event. You already know what to do."'))


# ══════════════════════════════════════════════════════════════════
#  ASSEMBLE
# ══════════════════════════════════════════════════════════════════

def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=0.72*inch,
        rightMargin=0.72*inch,
        topMargin=0.62*inch,
        bottomMargin=0.52*inch,
        title="Tribal Cowboy Rodeo Field Guide — V3 Refined",
        author="Tribal Cowboy",
        subject="ADHD/PTSD Optimized | Canon R5 Mark II | 83801 North Idaho",
    )

    story = []
    cover(story)
    how_to_use(story)
    quick_reference(story)
    bull_riding(story)
    barrel_racing(story)
    roping(story)
    gear_kit(story)
    event_calendar(story)
    pricing(story)
    outreach(story)
    micro_edit_rules(story)
    arena_card(story)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"Done: {OUTPUT}")


if __name__ == "__main__":
    build()
