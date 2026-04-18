"""
Tribal Cowboy Rodeo Photography Field Guide
REDESIGNED — ADHD/PTSD Optimized | Boutique Ranch Editorial Aesthetic
Canon EOS R5 Mark II | 83801 North Idaho | 2026

Design system: calm, layered, instantly scannable
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, FrameBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import Flowable
import os

W, H = letter
OUTPUT = os.path.expanduser("~/Desktop/TribalCowboy_Guide_REDESIGNED.pdf")

# ══════════════════════════════════════════════════════════
#  DESIGN TOKENS  — the complete style system
# ══════════════════════════════════════════════════════════

class C:
    # Base
    CREAM       = colors.HexColor("#FAF6EE")
    WARM_TAN    = colors.HexColor("#EDE0C8")
    PARCHMENT   = colors.HexColor("#F2EAD8")
    WHITE       = colors.white

    # Sage family
    SAGE        = colors.HexColor("#7A9E82")
    SAGE_DARK   = colors.HexColor("#4A7255")
    SAGE_LIGHT  = colors.HexColor("#D8EAD9")
    SAGE_MID    = colors.HexColor("#B5D1B8")

    # Rose / rust family
    ROSE        = colors.HexColor("#C4887A")
    ROSE_LIGHT  = colors.HexColor("#F0DDD8")
    ROSE_MID    = colors.HexColor("#DEB8B0")
    RUST        = colors.HexColor("#A85C42")
    RUST_PALE   = colors.HexColor("#EDD5C8")

    # Brown family (headers — never black)
    BROWN_DARK  = colors.HexColor("#3D2410")
    BROWN_MID   = colors.HexColor("#7A4A28")
    BROWN_LIGHT = colors.HexColor("#C4A882")
    BROWN_PALE  = colors.HexColor("#EAD8C0")

    # Event accent colors (muted, editorial)
    BULL        = colors.HexColor("#8B3A3A")   # deep rose-red
    BULL_PALE   = colors.HexColor("#F0DADA")
    BARREL      = colors.HexColor("#3A6B5A")   # deep teal-sage
    BARREL_PALE = colors.HexColor("#D8EDEA")
    ROPE        = colors.HexColor("#7A5F28")   # warm amber-brown
    ROPE_PALE   = colors.HexColor("#EDE5C8")
    GENERAL     = colors.HexColor("#5A6B8A")   # dusty blue-grey
    GENERAL_PALE= colors.HexColor("#DAE2ED")

    # Status tags
    GREEN       = colors.HexColor("#4A7255")   # safe / default
    GREEN_BG    = colors.HexColor("#D8EAD9")
    YELLOW      = colors.HexColor("#8A6E20")   # adjust
    YELLOW_BG   = colors.HexColor("#F0E5C0")
    RED         = colors.HexColor("#8B3A3A")   # fix now
    RED_BG      = colors.HexColor("#F0DADA")

    # UI
    RULE        = colors.HexColor("#D4C4A8")
    SHADOW      = colors.HexColor("#E8DCC8")


# ══════════════════════════════════════════════════════════
#  TYPE STYLES
# ══════════════════════════════════════════════════════════

def build_styles():
    base = getSampleStyleSheet()

    def S(name, **kw):
        base.add(ParagraphStyle(name=name, **kw))

    # Page purpose line (top of every page)
    S("Purpose", fontName="Times-Italic", fontSize=11, textColor=C.BROWN_MID,
      leading=14, spaceBefore=0, spaceAfter=0, alignment=TA_CENTER)

    # Section level headers
    S("L1Head", fontName="Times-Bold", fontSize=16, textColor=C.BROWN_DARK,
      leading=20, spaceBefore=14, spaceAfter=6)
    S("L2Head", fontName="Times-Bold", fontSize=13, textColor=C.BROWN_MID,
      leading=17, spaceBefore=10, spaceAfter=4)
    S("L3Head", fontName="Times-Italic", fontSize=11, textColor=C.BROWN_LIGHT,
      leading=14, spaceBefore=8, spaceAfter=3)

    # Card content
    S("CardTitle", fontName="Helvetica-Bold", fontSize=10, textColor=C.BROWN_DARK,
      leading=13, spaceBefore=0, spaceAfter=2)
    S("CardBody",  fontName="Helvetica", fontSize=9, textColor=C.BROWN_MID,
      leading=13, spaceBefore=0, spaceAfter=1)
    S("CardValue", fontName="Helvetica-Bold", fontSize=11, textColor=C.RUST,
      leading=14, spaceBefore=0, spaceAfter=0)
    S("CardNote",  fontName="Helvetica-Oblique", fontSize=8, textColor=C.BROWN_LIGHT,
      leading=11, spaceBefore=0, spaceAfter=0)

    # Body text (max 2 lines rule)
    S("Body", fontName="Helvetica", fontSize=9, textColor=C.BROWN_MID,
      leading=14, spaceBefore=2, spaceAfter=2)
    S("BodyBold", fontName="Helvetica-Bold", fontSize=9, textColor=C.BROWN_DARK,
      leading=14, spaceBefore=2, spaceAfter=2)

    # Bullet (tight, calm)
    S("CBullet", fontName="Helvetica", fontSize=9, textColor=C.BROWN_MID,
      leading=13, leftIndent=14, firstLineIndent=-9, spaceBefore=1, spaceAfter=1)

    # Status / tag text
    S("TagGreen",  fontName="Helvetica-Bold", fontSize=7.5, textColor=C.GREEN,  leading=10)
    S("TagYellow", fontName="Helvetica-Bold", fontSize=7.5, textColor=C.YELLOW, leading=10)
    S("TagRed",    fontName="Helvetica-Bold", fontSize=7.5, textColor=C.RED,    leading=10)

    # Callout / grounding
    S("Callout", fontName="Times-Italic", fontSize=12, textColor=C.SAGE_DARK,
      leading=17, spaceBefore=6, spaceAfter=6, alignment=TA_CENTER)

    # Cover styles
    S("CoverMain",  fontName="Times-Bold",        fontSize=42, textColor=C.BROWN_DARK,
      leading=50, alignment=TA_CENTER)
    S("CoverSub",   fontName="Times-Italic",       fontSize=17, textColor=C.RUST,
      leading=22, alignment=TA_CENTER)
    S("CoverMeta",  fontName="Helvetica",          fontSize=9,  textColor=C.BROWN_MID,
      leading=13, alignment=TA_CENTER)
    S("CoverTagline", fontName="Times-Italic",     fontSize=13, textColor=C.SAGE_DARK,
      leading=17, alignment=TA_CENTER)

    # Decision tree
    S("DTStep",   fontName="Helvetica-Bold", fontSize=8.5, textColor=C.BROWN_DARK,
      leading=12, alignment=TA_CENTER)
    S("DTLabel",  fontName="Helvetica",      fontSize=7.5, textColor=C.BROWN_MID,
      leading=10, alignment=TA_CENTER)
    S("DTArrow",  fontName="Helvetica-Bold", fontSize=11,  textColor=C.BROWN_LIGHT,
      leading=14, alignment=TA_CENTER)

    # Footer
    S("Footer", fontName="Helvetica", fontSize=7, textColor=C.BROWN_LIGHT,
      leading=9, alignment=TA_CENTER)
    S("FooterEdge", fontName="Helvetica-Bold", fontSize=7, textColor=C.BROWN_MID,
      leading=9)

    # L3 expand section
    S("ExpandLabel", fontName="Helvetica-Bold", fontSize=8, textColor=C.BROWN_LIGHT,
      leading=11)
    S("ExpandBody",  fontName="Helvetica", fontSize=8, textColor=C.BROWN_LIGHT,
      leading=12)

    return base

ST = build_styles()


# ══════════════════════════════════════════════════════════
#  CORE CUSTOM FLOWABLES
# ══════════════════════════════════════════════════════════

def sp(h=8):   return Spacer(1, h)
def p(t, s="Body"):  return Paragraph(t, ST[s])
def rule(c=C.RULE, t=0.5): return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=4, spaceBefore=4)


class PagePurposeBar(Flowable):
    """Top-of-page purpose statement with level badge."""
    def __init__(self, purpose, level=1, level_label="USE THIS FIRST"):
        self.purpose   = purpose
        self.level     = level
        self.level_label = level_label
        self.width = 0
        self.height = 44

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        # Warm tan background strip
        c.setFillColor(C.WARM_TAN)
        c.roundRect(0, 4, self.width, 38, 5, fill=1, stroke=0)
        # Subtle left accent bar by level
        bar_colors = {1: C.RUST, 2: C.SAGE, 3: C.BROWN_LIGHT}
        c.setFillColor(bar_colors.get(self.level, C.SAGE))
        c.roundRect(0, 4, 5, 38, 3, fill=1, stroke=0)
        # Level pill
        pill_colors = {1: C.RUST, 2: C.SAGE, 3: C.BROWN_LIGHT}
        pc = pill_colors.get(self.level, C.SAGE)
        c.setFillColor(pc)
        pill_w = len(self.level_label) * 5.5 + 14
        c.roundRect(12, 22, pill_w, 14, 5, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(12 + pill_w/2, 27, self.level_label)
        # Purpose text
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Times-Italic", 11.5)
        c.drawString(12, 10, self.purpose)


class SettingCard(Flowable):
    """
    A calm, scannable card for one camera setting.
    Layout: accent bar | label | VALUE (large) | why (small)
    Status: green/yellow/red dot
    """
    def __init__(self, label, value, why="", status="green", accent=C.RUST, width=None):
        self.label  = label
        self.value  = value
        self.why    = why
        self.status = status
        self.accent = accent
        self._w     = width
        self.width  = 0
        self.height = 72

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Card background
        c.setFillColor(C.CREAM)
        c.roundRect(0, 0, self.width, self.height, 7, fill=1, stroke=0)
        # Accent left bar
        c.setFillColor(self.accent)
        c.roundRect(0, 0, 5, self.height, 4, fill=1, stroke=0)
        # Status dot
        dot_colors = {"green": C.GREEN, "yellow": C.YELLOW, "red": C.RED}
        dc = dot_colors.get(self.status, C.GREEN)
        c.setFillColor(dc)
        c.circle(self.width - 12, self.height - 12, 5, fill=1, stroke=0)
        # Label
        c.setFillColor(C.BROWN_LIGHT)
        c.setFont("Helvetica", 7.5)
        c.drawString(14, self.height - 16, self.label.upper())
        # Value (large, confident)
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Times-Bold", 16)
        c.drawString(14, self.height - 36, self.value)
        # Rule
        c.setStrokeColor(C.RULE)
        c.setLineWidth(0.4)
        c.line(14, self.height - 44, self.width - 14, self.height - 44)
        # Why
        c.setFillColor(C.BROWN_MID)
        c.setFont("Helvetica", 8)
        # Wrap why text if needed
        max_chars = int((self.width - 28) / 4.5)
        why_line = self.why[:max_chars] + ("…" if len(self.why) > max_chars else "")
        c.drawString(14, self.height - 56, why_line)
        if len(self.why) > max_chars:
            c.drawString(14, self.height - 67, self.why[max_chars:max_chars*2])


class EventBanner(Flowable):
    """Section banner for an event type — elegant, not loud."""
    def __init__(self, title, subtitle="", accent=C.BULL, pale=C.BULL_PALE):
        self.title    = title
        self.subtitle = subtitle
        self.accent   = accent
        self.pale     = pale
        self.width    = 0
        self.height   = 52

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.pale)
        c.roundRect(0, 0, self.width, self.height, 7, fill=1, stroke=0)
        # Bottom accent line
        c.setFillColor(self.accent)
        c.rect(0, 0, self.width, 4, fill=1, stroke=0)
        # Left thick bar
        c.setFillColor(self.accent)
        c.rect(0, 0, 8, self.height, fill=1, stroke=0)
        # Title
        c.setFillColor(self.accent)
        c.setFont("Times-Bold", 20)
        c.drawString(20, 28, self.title)
        # Subtitle
        if self.subtitle:
            c.setFillColor(C.BROWN_MID)
            c.setFont("Times-Italic", 10)
            c.drawString(20, 14, self.subtitle)


class InfoChunk(Flowable):
    """
    Calm grouped info box — max 4 bullet items.
    Replaces dense table rows.
    """
    def __init__(self, title, items, accent=C.SAGE, bg=C.SAGE_LIGHT, width=None):
        self.title  = title
        self.items  = items[:4]   # hard cap at 4
        self.accent = accent
        self.bg     = bg
        self._w     = width
        self.width  = 0
        self.height = 28 + len(self.items) * 16 + 8

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.width, self.height, 6, fill=1, stroke=0)
        c.setFillColor(self.accent)
        c.roundRect(0, self.height - 26, self.width, 26, 6, fill=1, stroke=0)
        c.rect(0, self.height - 26, self.width, 14, fill=1, stroke=0)
        # Title
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(12, self.height - 17, self.title.upper())
        # Items
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Helvetica", 8.5)
        y = self.height - 38
        for item in self.items:
            c.setFillColor(self.accent)
            c.circle(10, y + 3, 2.5, fill=1, stroke=0)
            c.setFillColor(C.BROWN_DARK)
            c.drawString(18, y, item)
            y -= 16


class StatusTag(Flowable):
    """Small inline status tag: DEFAULT / ADJUST / FIX NOW"""
    def __init__(self, label, status="green"):
        self.label  = label
        self.status = status
        self.width  = 0
        self.height = 16

    def wrap(self, aw, ah):
        self.width = len(self.label) * 6 + 18
        return self.width, self.height

    def draw(self):
        c = self.canv
        bg = {  "green": C.GREEN_BG, "yellow": C.YELLOW_BG, "red": C.RED_BG}
        fg = {"green": C.GREEN,    "yellow": C.YELLOW,    "red": C.RED}
        c.setFillColor(bg.get(self.status, C.GREEN_BG))
        c.roundRect(0, 2, self.width, 12, 4, fill=1, stroke=0)
        c.setFillColor(fg.get(self.status, C.GREEN))
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(self.width/2, 5, self.label)


class StartHereArrow(Flowable):
    """The 'start here' visual cue."""
    def __init__(self, text="START HERE", width=None):
        self.text  = text
        self._w    = width
        self.width = 0
        self.height = 26

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(C.RUST)
        # Arrow body
        c.roundRect(0, 6, 110, 16, 5, fill=1, stroke=0)
        # Arrow point
        from reportlab.graphics.shapes import Polygon
        pts = [110, 14, 122, 20, 110, 26]
        c.setFillColor(C.RUST)
        p2 = c.beginPath()
        p2.moveTo(110, 6)
        p2.lineTo(124, 14)
        p2.lineTo(110, 22)
        p2.close()
        c.drawPath(p2, fill=1, stroke=0)
        # Text
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(10, 11, self.text)


class OverwhelmedBox(Flowable):
    """'If overwhelmed → do this' grounding shortcut."""
    def __init__(self, steps):
        self.steps  = steps[:3]
        self.width  = 0
        self.height = 28 + len(self.steps) * 18 + 8

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        # Soft sage background
        c.setFillColor(C.SAGE_LIGHT)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        # Top bar
        c.setFillColor(C.SAGE)
        c.roundRect(0, self.height - 26, self.width, 26, 6, fill=1, stroke=0)
        c.rect(0, self.height - 14, self.width, 14, fill=1, stroke=0)
        # Header
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(12, self.height - 17, "IF OVERWHELMED  ->  DO THIS FIRST")
        # Steps
        c.setFillColor(C.BROWN_DARK)
        y = self.height - 40
        for i, step in enumerate(self.steps, 1):
            c.setFillColor(C.SAGE)
            c.circle(14, y + 4, 7, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(14, y + 1, str(i))
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica", 8.5)
            c.drawString(28, y, step)
            y -= 18


class DecisionTree(Flowable):
    """
    Visual decision tree for troubleshooting.
    nodes = list of (problem, checks, solution) tuples.
    """
    def __init__(self, title, nodes, width=None):
        self.title  = title
        self.nodes  = nodes
        self._w     = width
        self.width  = 0
        self.row_h  = 72
        self.height = 28 + len(nodes) * (self.row_h + 6) + 10

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(C.PARCHMENT)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
        # Header
        c.setFillColor(C.BULL)
        c.roundRect(0, self.height - 28, self.width, 28, 6, fill=1, stroke=0)
        c.rect(0, self.height - 16, self.width, 16, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(12, self.height - 19, self.title)

        col_w = self.width / 3
        y = self.height - 38

        for prob, checks, sol in self.nodes:
            box_y = y - self.row_h + 10

            # Problem box (rose)
            c.setFillColor(C.ROSE_LIGHT)
            c.roundRect(4, box_y, col_w - 12, self.row_h - 10, 5, fill=1, stroke=0)
            c.setFillColor(C.BULL)
            c.roundRect(4, box_y + self.row_h - 24, col_w - 12, 20, 5, fill=1, stroke=0)
            c.rect(4, box_y + self.row_h - 14, col_w - 12, 14, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(4 + (col_w - 12)/2, box_y + self.row_h - 18, "PROBLEM")
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica-Bold", 8)
            text_y = box_y + self.row_h - 34
            for line in self._wrap_text(prob, col_w - 20, 8):
                c.drawCentredString(4 + (col_w - 12)/2, text_y, line)
                text_y -= 11

            # Arrow 1
            ax = col_w - 4
            ay_mid = box_y + (self.row_h - 10)/2
            c.setStrokeColor(C.BROWN_LIGHT)
            c.setLineWidth(1.2)
            c.line(ax, ay_mid, ax + 14, ay_mid)
            # Arrowhead
            c.setFillColor(C.BROWN_LIGHT)
            p2 = c.beginPath()
            p2.moveTo(ax + 14, ay_mid - 4)
            p2.lineTo(ax + 22, ay_mid)
            p2.lineTo(ax + 14, ay_mid + 4)
            p2.close()
            c.drawPath(p2, fill=1, stroke=0)

            # Check box (sage)
            cx = col_w + 6
            c.setFillColor(C.SAGE_LIGHT)
            c.roundRect(cx, box_y, col_w - 12, self.row_h - 10, 5, fill=1, stroke=0)
            c.setFillColor(C.SAGE_DARK)
            c.roundRect(cx, box_y + self.row_h - 24, col_w - 12, 20, 5, fill=1, stroke=0)
            c.rect(cx, box_y + self.row_h - 14, col_w - 12, 14, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(cx + (col_w - 12)/2, box_y + self.row_h - 18, "CHECK")
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica", 8)
            text_y = box_y + self.row_h - 34
            for i, chk in enumerate(checks[:3]):
                c.setFillColor(C.SAGE_DARK)
                c.circle(cx + 10, text_y + 3, 2.5, fill=1, stroke=0)
                c.setFillColor(C.BROWN_DARK)
                c.drawString(cx + 16, text_y, chk)
                text_y -= 12

            # Arrow 2
            ax2 = col_w * 2 - 2
            c.setStrokeColor(C.BROWN_LIGHT)
            c.line(ax2, ay_mid, ax2 + 14, ay_mid)
            c.setFillColor(C.BROWN_LIGHT)
            p3 = c.beginPath()
            p3.moveTo(ax2 + 14, ay_mid - 4)
            p3.lineTo(ax2 + 22, ay_mid)
            p3.lineTo(ax2 + 14, ay_mid + 4)
            p3.close()
            c.drawPath(p3, fill=1, stroke=0)

            # Solution box (rust)
            sx = col_w * 2 + 6
            c.setFillColor(C.RUST_PALE)
            c.roundRect(sx, box_y, col_w - 12, self.row_h - 10, 5, fill=1, stroke=0)
            c.setFillColor(C.RUST)
            c.roundRect(sx, box_y + self.row_h - 24, col_w - 12, 20, 5, fill=1, stroke=0)
            c.rect(sx, box_y + self.row_h - 14, col_w - 12, 14, fill=1, stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(sx + (col_w - 12)/2, box_y + self.row_h - 18, "FIX")
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Helvetica", 8)
            text_y = box_y + self.row_h - 34
            for line in self._wrap_text(sol, col_w - 20, 8):
                c.drawString(sx + 6, text_y, line)
                text_y -= 11

            y -= (self.row_h + 6)

    def _wrap_text(self, text, max_width, fontsize):
        # Simple word wrapper
        chars_per_line = int(max_width / (fontsize * 0.52))
        words = text.split()
        lines, current = [], ""
        for w in words:
            if len(current) + len(w) + 1 <= chars_per_line:
                current = (current + " " + w).strip()
            else:
                if current: lines.append(current)
                current = w
        if current: lines.append(current)
        return lines[:3]


class ExpandSection(Flowable):
    """'Deeper info — only if needed' visual section."""
    def __init__(self, rows, width=None):
        """rows = list of (label, value) tuples"""
        self.rows  = rows
        self._w    = width
        self.width = 0
        self.height = 22 + len(rows) * 16 + 8

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Dashed border
        c.setStrokeColor(C.RULE)
        c.setLineWidth(0.5)
        c.setDash([4, 3])
        c.roundRect(0, 0, self.width, self.height, 5, stroke=1, fill=0)
        c.setDash([])
        # Label
        c.setFillColor(C.WHITE)
        c.rect(8, self.height - 12, 130, 10, fill=1, stroke=0)
        c.setFillColor(C.BROWN_LIGHT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(12, self.height - 10, "v  IF YOU NEED MORE DETAIL")
        # Rows
        y = self.height - 26
        for label, value in self.rows:
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica-Bold", 8)
            c.drawString(12, y, label + ":")
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica", 8)
            c.drawString(12 + len(label)*5.2 + 8, y, value)
            y -= 16


class TierCard(Flowable):
    """Pricing / level tier card."""
    def __init__(self, tier_name, price, items, accent=C.SAGE, highlight=False, width=None):
        self.tier   = tier_name
        self.price  = price
        self.items  = items[:4]
        self.accent = accent
        self.highlight = highlight
        self._w     = width
        self.width  = 0
        self.height = 60 + len(items) * 16 + 10

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return aw, self.height

    def draw(self):
        c = self.canv
        if self.highlight:
            c.setFillColor(self.accent)
            c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
            txt_color = C.WHITE
            sub_color = colors.HexColor("#FFFFFFAA") if False else C.CREAM
        else:
            c.setFillColor(C.CREAM)
            c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=0)
            c.setFillColor(self.accent)
            c.roundRect(0, self.height - 48, self.width, 48, 6, fill=1, stroke=0)
            c.rect(0, self.height - 30, self.width, 30, fill=1, stroke=0)
            txt_color = C.BROWN_DARK
            sub_color = C.BROWN_MID

        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(14, self.height - 18, self.tier)
        c.setFont("Times-Bold", 22)
        c.drawString(14, self.height - 40, self.price)

        c.setFillColor(sub_color if not self.highlight else C.BROWN_DARK)
        c.setFont("Helvetica", 8.5)
        y = self.height - 58
        for item in self.items:
            c.setFillColor(self.accent if not self.highlight else C.BROWN_DARK)
            c.circle(14, y + 3, 2.5, fill=1, stroke=0)
            c.setFillColor(C.BROWN_DARK if not self.highlight else C.BROWN_DARK)
            c.setFont("Helvetica", 8.5)
            c.drawString(22, y, item)
            y -= 16


class TimelineItem(Flowable):
    """Event calendar timeline row."""
    def __init__(self, month, event, location, distance, tier_color, note="", width=None):
        self.month    = month
        self.event    = event
        self.location = location
        self.distance = distance
        self.tc       = tier_color
        self.note     = note
        self._w       = width
        self.width    = 0
        self.height   = 44

    def wrap(self, aw, ah):
        self.width = self._w or aw
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Month bubble
        c.setFillColor(self.tc)
        c.roundRect(0, 8, 58, 28, 5, fill=1, stroke=0)
        c.setFillColor(C.WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(29, 19, self.month)
        # Connector line
        c.setStrokeColor(C.RULE)
        c.setLineWidth(1)
        c.line(58, 22, 76, 22)
        c.setFillColor(self.tc)
        c.circle(76, 22, 4, fill=1, stroke=0)
        # Content
        c.setFillColor(C.BROWN_DARK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(86, 28, self.event)
        c.setFillColor(C.BROWN_MID)
        c.setFont("Helvetica", 8)
        c.drawString(86, 16, f"{self.location}  |  {self.distance}")
        if self.note:
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Helvetica-Oblique", 7.5)
            c.drawString(86, 6, self.note)
        # Distance pill
        c.setFillColor(C.WARM_TAN)
        pill_x = self.width - 62
        c.roundRect(pill_x, 14, 58, 16, 5, fill=1, stroke=0)
        c.setFillColor(self.tc)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(pill_x + 29, 19, self.distance)


# ══════════════════════════════════════════════════════════
#  PAGE TEMPLATE  (header / footer on every page after 1)
# ══════════════════════════════════════════════════════════

def on_page(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        # Thin top rule
        canvas.setStrokeColor(C.RULE)
        canvas.setLineWidth(0.5)
        canvas.line(0.65*inch, H - 0.38*inch, W - 0.65*inch, H - 0.38*inch)
        # Header text
        canvas.setFillColor(C.BROWN_MID)
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.drawString(0.65*inch, H - 0.30*inch, "TRIBAL COWBOY  —  RODEO FIELD GUIDE")
        canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(W - 0.65*inch, H - 0.30*inch, f"Canon R5 Mark II  |  p.{doc.page}")
        # Bottom rule
        canvas.setStrokeColor(C.RULE)
        canvas.line(0.65*inch, 0.38*inch, W - 0.65*inch, 0.38*inch)
        canvas.setFillColor(C.BROWN_LIGHT)
        canvas.setFont("Helvetica", 7)
        canvas.drawCentredString(W/2, 0.25*inch,
            "North Idaho  /  Eastern Washington  |  83801  |  250-Mile Rodeo Radius")
    canvas.restoreState()


# ══════════════════════════════════════════════════════════
#  PAGE BUILDERS
# ══════════════════════════════════════════════════════════

# ── COVER ─────────────────────────────────────────────────
def cover(story):
    class CoverPage(Flowable):
        def wrap(self, aw, ah):
            return aw, ah
        def draw(self):
            c = self.canv
            # Cream background
            c.setFillColor(C.CREAM)
            c.rect(-0.75*inch, -inch, W + inch, H + 2*inch, fill=1, stroke=0)
            # Top tan band
            c.setFillColor(C.WARM_TAN)
            c.rect(-0.75*inch, H*0.72, W + inch, H*0.30, fill=1, stroke=0)
            # Sage bottom band
            c.setFillColor(C.SAGE_LIGHT)
            c.rect(-0.75*inch, -inch, W + inch, H*0.22, fill=1, stroke=0)
            # Rust accent lines
            c.setFillColor(C.RUST)
            c.rect(-0.75*inch, H*0.72 - 4, W + inch, 4, fill=1, stroke=0)
            c.setFillColor(C.ROSE_MID)
            c.rect(-0.75*inch, H*0.72 - 10, W + inch, 3, fill=1, stroke=0)
            c.setFillColor(C.RUST)
            c.rect(-0.75*inch, H*0.19 + 3, W + inch, 4, fill=1, stroke=0)
            c.setFillColor(C.ROSE_MID)
            c.rect(-0.75*inch, H*0.19 + 9, W + inch, 3, fill=1, stroke=0)
            # Main title
            c.setFillColor(C.BROWN_DARK)
            c.setFont("Times-Bold", 48)
            c.drawCentredString(W/2, H*0.56, "Tribal Cowboy")
            c.setFont("Times-Italic", 22)
            c.drawCentredString(W/2, H*0.49, "Rodeo Photography Field Guide")
            # Divider
            c.setFillColor(C.RUST)
            c.rect(2.2*inch, H*0.47, 3.6*inch, 2, fill=1, stroke=0)
            # Camera line
            c.setFillColor(C.RUST)
            c.setFont("Helvetica-Bold", 11)
            c.drawCentredString(W/2, H*0.43, "CANON EOS R5 MARK II  EDITION")
            # Tagline
            c.setFillColor(C.SAGE_DARK)
            c.setFont("Times-Italic", 13)
            c.drawCentredString(W/2, H*0.38,
                "Calm. Clear. Open under pressure.")
            # Meta
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica", 9)
            c.drawCentredString(W/2, H*0.12, "83801 Careywood, ID  |  250-Mile Radius  |  2026")
            # Horses
            c.setFillColor(C.BROWN_LIGHT)
            c.setFont("Times-Italic", 10)
            c.drawCentredString(W/2, H*0.08,
                "Millie  *  Abby  *  Jolene  *  Monster  *  Master Chief")
            # Level system preview (bottom right)
            for i, (txt, col) in enumerate([
                ("L1  USE FIRST", C.RUST),
                ("L2  WHEN NEEDED", C.SAGE),
                ("L3  DEEP DIVE", C.BROWN_LIGHT),
            ]):
                bx = W - 1.8*inch
                by = H*0.12 + i*20
                c.setFillColor(col)
                c.roundRect(bx, by, 120, 14, 4, fill=1, stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold", 7)
                c.drawString(bx + 8, by + 4, txt)

    story.append(CoverPage())
    story.append(PageBreak())


# ── HOW TO USE THIS GUIDE ─────────────────────────────────
def how_to_use(story):
    story.append(PagePurposeBar(
        "Understand this system once — then you never have to think about it again.",
        level=1, level_label="READ THIS FIRST"))
    story.append(sp(12))

    story.append(OverwhelmedBox([
        "Go to the Quick Reference page (next page)",
        "Find your event — set those 4 settings only",
        "Raise the camera and shoot",
    ]))
    story.append(sp(14))

    # 3-level system explanation
    story.append(p("<b>Every page in this guide has three layers.</b>", "L1Head"))
    story.append(sp(6))

    level_data = [
        [
            "L1\nUSE FIRST",
            C.RUST, C.RUST_PALE,
            "Critical. Set this before you raise the camera.",
            "3-4 items max. Big text. Always visible.",
        ],[
            "L2\nWHEN NEEDED",
            C.SAGE, C.SAGE_LIGHT,
            "Extra context. Read when something isn't working.",
            "Grouped chunks. Calm layout. Never urgent.",
        ],[
            "L3\nDEEP DIVE",
            C.BROWN_LIGHT, C.BROWN_PALE,
            "Optional detail. You may never need this.",
            "Dashed box at the bottom of the section.",
        ],
    ]

    cards = []
    for label, accent, bg, desc, note in level_data:
        class LCard(Flowable):
            def __init__(self, lbl, ac, bg_, d, n):
                self.lbl=lbl; self.ac=ac; self.bg=bg_; self.d=d; self.n=n
                self.width=0; self.height=88
            def wrap(self, aw, ah):
                self.width=aw; return aw, self.height
            def draw(self):
                c=self.canv
                c.setFillColor(self.bg)
                c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
                c.setFillColor(self.ac)
                c.roundRect(0,self.height-32,self.width,32,6,fill=1,stroke=0)
                c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold",10)
                lines=self.lbl.split("\n")
                c.drawCentredString(self.width/2,self.height-14,lines[0])
                if len(lines)>1:
                    c.setFont("Helvetica",8)
                    c.drawCentredString(self.width/2,self.height-24,lines[1])
                c.setFillColor(C.BROWN_DARK)
                c.setFont("Helvetica-Bold",8.5)
                # wrap desc
                words=self.d.split(); lines2=[]; cur=""
                cpl=int((self.width-20)/4.3)
                for w in words:
                    if len(cur)+len(w)+1<=cpl: cur=(cur+" "+w).strip()
                    else:
                        if cur: lines2.append(cur)
                        cur=w
                if cur: lines2.append(cur)
                y=self.height-44
                for l in lines2[:2]:
                    c.drawString(10,y,l); y-=12
                c.setFillColor(C.BROWN_LIGHT)
                c.setFont("Helvetica-Oblique",7.5)
                c.drawString(10,12,self.n)
        cards.append(LCard(label, accent, bg, desc, note))

    t = Table([[cards[0], sp(8), cards[1], sp(8), cards[2]]],
              colWidths=[2.25*inch, 0.1*inch, 2.25*inch, 0.1*inch, 2.25*inch])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(sp(14))

    # Color tags
    story.append(rule())
    story.append(p("<b>Status colors appear on every setting card:</b>", "BodyBold"))
    story.append(sp(6))

    tag_data = [
        ["DEFAULT — safe to leave this on", C.GREEN, C.GREEN_BG],
        ["ADJUST — only change if light or action changes", C.YELLOW, C.YELLOW_BG],
        ["FIX NOW — something is wrong, change immediately", C.RED, C.RED_BG],
    ]

    class TagRow(Flowable):
        def __init__(self, items):
            self.items=items; self.width=0; self.height=28
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            x=0
            for label,fg,bg in self.items:
                w=self.width/3-6
                c.setFillColor(bg)
                c.roundRect(x,2,w,22,5,fill=1,stroke=0)
                c.setFillColor(fg)
                c.circle(x+14,13,5,fill=1,stroke=0)
                c.setFillColor(fg)
                c.setFont("Helvetica-Bold",8)
                c.drawString(x+24,10,label)
                x+=w+8

    story.append(TagRow(tag_data))
    story.append(sp(10))
    story.append(rule())
    story.append(sp(8))
    story.append(p(
        '"Open this under pressure at a rodeo and instantly know what to do — without thinking."',
        "Callout"))
    story.append(PageBreak())


# ── QUICK REFERENCE ───────────────────────────────────────
def quick_reference(story):
    story.append(PagePurposeBar(
        "Find your settings before you raise the camera. Four settings. That's all.",
        level=1, level_label="USE THIS FIRST"))
    story.append(sp(10))

    story.append(StartHereArrow("START HERE — pick your event"))
    story.append(sp(10))

    # ── EVENT CARDS 2x2 grid ─────────────────────────────
    def event_card(title, color, pale, settings):
        """settings = list of (label, value, status) max 4"""
        class EC(Flowable):
            def __init__(self):
                self.width=0; self.height=200
            def wrap(self, aw, ah):
                self.width=aw; return aw, self.height
            def draw(self):
                c=self.canv
                c.setFillColor(pale)
                c.roundRect(0,0,self.width,self.height,8,fill=1,stroke=0)
                c.setFillColor(color)
                c.roundRect(0,self.height-32,self.width,32,6,fill=1,stroke=0)
                c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Times-Bold",14)
                c.drawString(12,self.height-22,title)
                # Settings
                y=self.height-50
                row_h=34
                for label,value,status in settings[:4]:
                    # mini card
                    c.setFillColor(C.WHITE)
                    c.roundRect(8,y,self.width-16,row_h-2,4,fill=1,stroke=0)
                    # status dot
                    dot_c={  "green":C.GREEN,"yellow":C.YELLOW,"red":C.RED}
                    c.setFillColor(dot_c.get(status,C.GREEN))
                    c.circle(self.width-18,y+row_h/2-1,4,fill=1,stroke=0)
                    c.setFillColor(C.BROWN_LIGHT)
                    c.setFont("Helvetica",7)
                    c.drawString(14,y+row_h-13,label.upper())
                    c.setFillColor(color)
                    c.setFont("Times-Bold",13)
                    c.drawString(14,y+5,value)
                    y-=row_h+2
        return EC()

    bull_card = event_card("BULL RIDING", C.BULL, C.BULL_PALE, [
        ("Shutter speed",    "1/2000–1/3200", "red"),
        ("Aperture",         "f/4",           "green"),
        ("AF Subject",       "Animals + Eye", "green"),
        ("Drive + Pre-Shot", "H+ 30fps + MAX","green"),
    ])
    barrel_card = event_card("BARREL RACING", C.BARREL, C.BARREL_PALE, [
        ("Shutter min",      "1/1600",        "red"),
        ("Aperture",         "f/2.8 – f/4",   "green"),
        ("AF Subject",       "Animals + Eye", "green"),
        ("Drive + Pre-Shot", "H+ 30fps + MED","green"),
    ])
    rope_card = event_card("CALF / TEAM ROPING", C.ROPE, C.ROPE_PALE, [
        ("Shutter speed",    "1/2000",         "red"),
        ("Aperture",         "f/5.6",          "green"),
        ("AF Subject",       "Animals + Eye",  "green"),
        ("Pre-Shot",         "MAX — 30 frames","green"),
    ])
    general_card = event_card("GENERAL / CROWD", C.GENERAL, C.GENERAL_PALE, [
        ("Shutter min",      "1/1250",         "yellow"),
        ("Aperture",         "f/4",            "green"),
        ("AF Subject",       "People + Face",  "green"),
        ("Drive",            "H 12fps",        "green"),
    ])

    grid = Table(
        [[bull_card, sp(10), barrel_card],
         [sp(10), sp(10), sp(10)],
         [rope_card, sp(10), general_card]],
        colWidths=[3.5*inch, 0.2*inch, 3.5*inch]
    )
    grid.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(grid)
    story.append(sp(12))
    story.append(rule())

    # ── SHUTTER MODE STRIP ───────────────────────────────
    story.append(p("<b>Shutter mode</b>  —  one decision, not a setting to overthink:", "BodyBold"))
    story.append(sp(6))

    class ShutterStrip(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 32
        def draw(self):
            c=self.canv
            items=[
                ("Daylight / any LED arena", "ELEC. 1ST CURTAIN", C.SAGE),
                ("Night rodeo / flickering lights", "MECHANICAL", C.BULL),
                ("Portraits / silent work", "ELECTRONIC", C.GENERAL),
            ]
            w=self.width/3-8
            x=0
            for label,mode,col in items:
                c.setFillColor(C.WARM_TAN)
                c.roundRect(x,0,w,30,5,fill=1,stroke=0)
                c.setFillColor(col)
                c.roundRect(x,0,w,30,5,fill=1,stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica",7)
                c.drawString(x+8,20,label)
                c.setFont("Helvetica-Bold",9)
                c.drawString(x+8,8,mode)
                x+=w+12

    story.append(ShutterStrip())
    story.append(sp(8))

    # ── L3 EXPAND ────────────────────────────────────────
    story.append(ExpandSection([
        ("Night ISO max",       "12800  |  Shutter: 1/1000 min  |  Mode: Manual"),
        ("Dust conditions",     "Tracking Sensitivity -> 4-5  |  +1/3 exp comp"),
        ("Animal Tracking",     "AF Menu 1 > Subject Detect: ANIMALS > Eye Detection: ON"),
        ("Pre-Shot access",     "Shooting Menu 4 > Pre-shot Burst > Enable > set level"),
    ]))
    story.append(PageBreak())


# ── BULL RIDING ───────────────────────────────────────────
def bull_riding(story):
    story.append(EventBanner(
        "Bull Riding",
        "Be ready before the gate opens — you have 8 seconds.",
        accent=C.BULL, pale=C.BULL_PALE))
    story.append(sp(8))

    story.append(PagePurposeBar(
        "Set three things. Fire at the right moments. Stay safe.",
        level=1, level_label="L1  —  USE THIS FIRST"))
    story.append(sp(10))

    story.append(StartHereArrow("SET THESE BEFORE THE GATE OPENS"))
    story.append(sp(10))

    # ── L1: 3 critical setting cards ─────────────────────
    sc1 = SettingCard("SHUTTER SPEED", "1/2000 – 1/3200",
        "Stops the spin. Never go lower. This is non-negotiable.",
        status="red", accent=C.BULL, width=2.3*inch)
    sc2 = SettingCard("AF + SUBJECT", "Animals + Eye ON",
        "Set once in AF Menu 1. Never change mid-event.",
        status="green", accent=C.SAGE_DARK, width=2.3*inch)
    sc3 = SettingCard("DRIVE + PRE-SHOT", "H+ 30fps + MAX",
        "Pre-shot captures the peak before your finger fires.",
        status="green", accent=C.RUST, width=2.3*inch)

    t = Table([[sc1, sp(6), sc2, sp(6), sc3]],
              colWidths=[2.3*inch, 0.15*inch, 2.3*inch, 0.15*inch, 2.3*inch])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(sp(12))

    # ── OVERWHELMED BOX ──────────────────────────────────
    story.append(OverwhelmedBox([
        "Set shutter to 1/2000 in Manual mode",
        "Confirm AF Subject = ANIMALS in menu",
        "Half-press to lock — wait for the gate",
    ]))
    story.append(sp(12))
    story.append(rule())

    # ── L2: TIMING GUIDE ─────────────────────────────────
    story.append(p("<b>L2  —  WHEN TO FIRE</b>  (the four moments that matter)", "L2Head"))
    story.append(sp(6))

    class TimingGuide(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 68
        def draw(self):
            c=self.canv
            moments=[
                ("Gate\nOpens",  "Half-press\nalready held",  C.BULL),
                ("First\nJump",  "Pre-shot\ncatches it",     C.RUST),
                ("Peak\nSpin",   "2-3 sec in\nBURST",        C.BULL),
                ("Buck-off\nor Ride",  "Hold through\ndismount",   C.SAGE_DARK),
            ]
            seg_w=(self.width-20)/4
            x=10
            # Timeline line
            c.setStrokeColor(C.RULE)
            c.setLineWidth(1.5)
            c.line(10, 34, self.width-10, 34)
            for i,(label,action,col) in enumerate(moments):
                cx=x+seg_w/2
                c.setFillColor(col)
                c.circle(cx,34,10,fill=1,stroke=0)
                c.setFillColor(C.WHITE)
                c.setFont("Helvetica-Bold",7)
                c.drawCentredString(cx,30,str(i+1))
                c.setFillColor(C.BROWN_DARK)
                c.setFont("Helvetica-Bold",7.5)
                for j,ln in enumerate(label.split("\n")):
                    c.drawCentredString(cx,56-j*9,ln)
                c.setFillColor(C.BROWN_LIGHT)
                c.setFont("Helvetica-Oblique",7)
                for j,ln in enumerate(action.split("\n")):
                    c.drawCentredString(cx,20-j*9,ln)
                x+=seg_w

    story.append(TimingGuide())
    story.append(sp(10))

    # ── L2: TWO INFO CHUNKS ──────────────────────────────
    chunk_l = InfoChunk(
        "WATCH THE BULL NOT THE RIDER",
        ["Bull's HEAD leads the body by 0.5 seconds",
         "Aim your AF point at the head/shoulder",
         "It tells you where the action goes next",
         "Rider follows — bull decides"],
        accent=C.BULL, bg=C.BULL_PALE, width=3.45*inch)

    chunk_r = InfoChunk(
        "AF TIPS FOR CHAOS",
        ["If tracking grabs bullfighter: tap screen",
         "Heavy dust: Tracking Sensitivity -> 4",
         "Lost lock: fall back to Zone Center",
         "Buffer: unlimited on CFexpress — hold it"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT, width=3.45*inch)

    t2 = Table([[chunk_l, sp(8), chunk_r]],
               colWidths=[3.45*inch, 0.15*inch, 3.45*inch])
    t2.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t2)
    story.append(sp(10))
    story.append(rule())

    # ── DECISION TREE ────────────────────────────────────
    story.append(p("<b>Something wrong?  Use this to fix it fast.</b>", "L2Head"))
    story.append(sp(6))

    story.append(DecisionTree("BULL RIDING — FIX IT FAST", [
        ("Shot is blurry",
         ["Shutter below 1/2000?", "IBIS set to Mode 1?", "Is subject in focus?"],
         "Raise to 1/2000+ first. Then check IBIS Mode 2 for panning."),
        ("AF lost the subject",
         ["Dust blocking view?", "Tracking Sens at 3?", "Wrong subject locked?"],
         "Raise Tracking Sens to 4-5. Tap EVF screen to reselect bull."),
        ("Missing peak moment",
         ["Pre-shot on MAX?", "Firing too late?", "Half-press before gate?"],
         "Enable pre-shot MAX. Half-press 2 seconds before the gate opens."),
    ]))
    story.append(sp(10))

    # ── L3 EXPAND ────────────────────────────────────────
    story.append(ExpandSection([
        ("Full settings",  "M + Auto ISO  |  f/4  |  Servo AF  |  Whole Area AF Zone"),
        ("Aperture",       "f/4 is the sweet spot — DOF buffer for erratic movement"),
        ("ISO max",        "12800 — R5 II sensor handles this cleanly"),
        ("Post-ride",      "Switch Subject Detect > PEOPLE for face/reaction shots"),
        ("Shutter type",   "Elec. 1st Curtain for day  |  Mechanical for night LED arenas"),
    ]))
    story.append(PageBreak())


# ── BARREL RACING ─────────────────────────────────────────
def barrel_racing(story):
    story.append(EventBanner(
        "Barrel Racing",
        "Pre-focus on the barrel. Let the horse run into your frame.",
        accent=C.BARREL, pale=C.BARREL_PALE))
    story.append(sp(8))
    story.append(PagePurposeBar(
        "You know exactly where the horse is going. Use that.",
        level=1, level_label="L1  —  USE THIS FIRST"))
    story.append(sp(10))

    sc1 = SettingCard("SHUTTER MIN", "1/1600",
        "Enforce via Auto ISO minimum shutter setting.",
        status="red", accent=C.BARREL, width=2.3*inch)
    sc2 = SettingCard("APERTURE", "f/2.8 – f/4",
        "Isolate horse from crowd background.",
        status="green", accent=C.SAGE_DARK, width=2.3*inch)
    sc3 = SettingCard("DRIVE + PRE-SHOT", "H+ 30fps + MED",
        "Medium pre-shot — turns are more predictable.",
        status="green", accent=C.RUST, width=2.3*inch)

    t = Table([[sc1, sp(6), sc2, sp(6), sc3]],
              colWidths=[2.3*inch, 0.15*inch, 2.3*inch, 0.15*inch, 2.3*inch])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(sp(10))

    chunk_l = InfoChunk(
        "THE MONEY SHOT",
        ["2 strides before barrel: start burst",
         "Through the apex: hold it",
         "1 stride after exit: stop",
         "Dirt/sand spray = the frame you want"],
        accent=C.BARREL, bg=C.BARREL_PALE, width=3.45*inch)

    chunk_r = InfoChunk(
        "SANDPOINT EXTRA",
        ["Late afternoon = lake behind the horse",
         "Position: sun behind you, lake visible",
         "Golden hour + water = unique content",
         "Worth pausing between riders to move"],
        accent=C.SAGE_DARK, bg=C.SAGE_LIGHT, width=3.45*inch)

    t2 = Table([[chunk_l, sp(8), chunk_r]],
               colWidths=[3.45*inch, 0.15*inch, 3.45*inch])
    t2.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t2)
    story.append(sp(10))
    story.append(rule())

    story.append(DecisionTree("BARREL RACING — FIX IT FAST", [
        ("Motion blur on horse",
         ["Shutter below 1/1600?", "ISO Auto forcing low shutter?", "IBIS Mode right?"],
         "Set minimum shutter 1/1600 in Auto ISO. Raise ISO before dropping shutter."),
        ("AF hunting between barrels",
         ["Tracking on wide area?", "Crowd confusing system?", "Tracking Sens OK?"],
         "Pre-focus on the barrel — let horse enter your frame. Zone AF if needed."),
    ]))
    story.append(sp(8))
    story.append(ExpandSection([
        ("Mode",       "Aperture Priority — light shifts as horse moves pattern"),
        ("ISO auto",   "100-6400 standard  |  push to 12800 evening events"),
        ("After ride", "Switch to People detect for celebration expression shots"),
        ("Tracking",   "Sensitivity 3 standard — barrel pattern is predictable"),
    ]))
    story.append(PageBreak())


# ── GEAR VISUAL KIT ───────────────────────────────────────
def gear_kit(story):
    story.append(PagePurposeBar(
        "Pick your lens kit by budget. Then don't overthink it.",
        level=2, level_label="L2  —  WHEN NEEDED"))
    story.append(sp(10))

    story.append(p("<b>Primary lens — choose one, not both</b>", "L1Head"))
    story.append(sp(6))

    lens_data = [
        ("RF 70–200mm f/2.8L", "Close rail access\nIndoor arenas\nLow light events", C.RUST, "$1,800 used"),
        ("RF 100–500mm f/4.5–7.1L", "County fairs\nLarger venues\nVersatile reach", C.BARREL, "$1,900 used"),
        ("RF 200–800mm f/6.3–9", "Large arenas\nPendleton-scale\nBest value reach", C.ROPE, "$800 new"),
        ("RF 100–400mm f/5.6–8", "Starting out\nLight carry\nBudget entry", C.SAGE_DARK, "$600 new"),
    ]

    class LensCard(Flowable):
        def __init__(self, name, use, color, price):
            self.name=name; self.use=use; self.color=color; self.price=price
            self.width=0; self.height=110
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.CREAM)
            c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
            c.setFillColor(self.color)
            c.roundRect(0,0,6,self.height,4,fill=1,stroke=0)
            c.setFillColor(self.color)
            c.setFont("Times-Bold",11)
            c.drawString(14,self.height-18,self.name)
            c.setFillColor(C.BROWN_MID)
            c.setFont("Helvetica",8.5)
            y=self.height-36
            for line in self.use.split("\n"):
                c.setFillColor(self.color)
                c.circle(18,y+3,2.5,fill=1,stroke=0)
                c.setFillColor(C.BROWN_MID)
                c.drawString(26,y,line)
                y-=14
            # Price pill
            c.setFillColor(self.color)
            pw=len(self.price)*6+16
            c.roundRect(14,8,pw,16,5,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Helvetica-Bold",8)
            c.drawString(22,13,self.price)

    lens_cards = [LensCard(*d) for d in lens_data]

    t = Table(
        [[lens_cards[0], sp(8), lens_cards[1]],
         [sp(8), sp(8), sp(8)],
         [lens_cards[2], sp(8), lens_cards[3]]],
        colWidths=[3.45*inch, 0.15*inch, 3.45*inch])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(sp(12))
    story.append(rule())

    # Budget kit boxes
    story.append(p("<b>Kit by budget — pick your tier</b>", "L2Head"))
    story.append(sp(8))

    b1 = TierCard("STARTING OUT", "$650–900",
        ["RF 100-400mm f/5.6-8 (new)",
         "Canon 50mm f/1.8 STM",
         "Covers 80% of arena situations",
         "Prove the concept first"],
        accent=C.SAGE, highlight=False, width=2.25*inch)

    b2 = TierCard("WORKING PHOTOGRAPHER", "$2,000–2,500",
        ["RF 70-200mm f/2.8L (used)",
         "RF 35mm f/1.8 IS STM",
         "Professional low-light coverage",
         "Subject isolation power"],
        accent=C.RUST, highlight=True, width=2.25*inch)

    b3 = TierCard("FULL TWO-BODY KIT", "$4,500–5,500",
        ["RF 100-500mm (used)",
         "RF 70-200 f/2.8 (used)",
         "RF 24-70 f/2.8 (used)",
         "Tier 1 through Tier 3 events"],
        accent=C.BROWN_MID, highlight=False, width=2.25*inch)

    bt = Table([[b1, sp(8), b2, sp(8), b3]],
               colWidths=[2.25*inch, 0.15*inch, 2.25*inch, 0.15*inch, 2.25*inch])
    bt.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(bt)
    story.append(sp(10))

    story.append(ExpandSection([
        ("EF lens adapter", "Canon EF-EOS R adapter (~$100) — full AF speed + animal tracking on all EF L lenses"),
        ("Do NOT buy",      "EF-S / RF-S crop lenses  |  RF 2x extender on f/5.6+  |  Manual FD mount lenses"),
        ("Sigma/Tamron RF", "Sigma 60-600mm DG DN Sport (RF)  |  Tamron 150-500mm VXD (RF) — both excellent budget options"),
    ]))
    story.append(PageBreak())


# ── EVENT CALENDAR TIMELINE ────────────────────────────────
def event_calendar(story):
    story.append(PagePurposeBar(
        "Your year at a glance. Tier 1 first — build from there.",
        level=2, level_label="L2  —  WHEN NEEDED"))
    story.append(sp(10))

    story.append(p("<b>Tier 1  —  Start Here</b>  (easiest access, best learning)", "L1Head"))
    story.append(sp(4))

    tier1 = [
        ("MAY",   "UM Spring Rodeo",              "Missoula, MT",       "~200 mi", C.SAGE, "Zero credentials needed — test your system here"),
        ("JUNE",  "Barrel Racing Jackpots",       "Region-wide",        "Varies",  C.SAGE, "No credentials — build portfolio weekly"),
        ("AUG",   "Sandpoint Bonner County Rodeo","Sandpoint, ID",      "~60 mi",  C.SAGE, "Lake backdrop — position for it"),
        ("AUG",   "North Idaho State Fair",       "Coeur d'Alene, ID",  "~40 mi",  C.SAGE, "Home turf — own this event"),
        ("SEPT",  "Latah County Fair",            "Moscow, ID",         "~100 mi", C.SAGE, "Small, accessible, great practice"),
    ]
    for item in tier1:
        story.append(TimelineItem(*item))
        story.append(sp(4))

    story.append(sp(8))
    story.append(rule())
    story.append(p("<b>Tier 2  —  Build Toward These</b>  (mid-level PRCA)", "L2Head"))
    story.append(sp(4))

    tier2 = [
        ("JULY",  "Toppenish Rodeo",          "Toppenish, WA",   "~155 mi", C.RUST, "First PRCA credential attempt"),
        ("JULY",  "Basin City Freedom Rodeo", "Basin City, WA",  "~160 mi", C.RUST, "July 4th crowd = family sales"),
        ("AUG",   "Omak Stampede",            "Omak, WA",        "~125 mi", C.RUST, "Suicide Race = unique fine art content"),
        ("AUG",   "NW Montana Fair & Rodeo",  "Kalispell, MT",   "~160 mi", C.RUST, "120-year tradition"),
        ("SEPT",  "Lewiston Roundup",         "Lewiston, ID",    "~65 mi",  C.RUST, "Apply 6+ weeks early"),
        ("SEPT",  "Walla Walla Fair",         "Walla Walla, WA", "~175 mi", C.RUST, "160th anniversary — built-in PR"),
    ]
    for item in tier2:
        story.append(TimelineItem(*item))
        story.append(sp(4))

    story.append(sp(8))
    story.append(rule())
    story.append(p("<b>Tier 3  —  Long Game</b>  (earn these)", "L3Head"))
    story.append(sp(4))

    tier3 = [
        ("LABOR DAY", "Ellensburg Rodeo",     "Ellensburg, WA", "~140 mi", C.BROWN_LIGHT, "Top 25 national — goal: Year 2"),
        ("AUG",       "Horse Heaven Round-Up","Kennewick, WA",  "~165 mi", C.BROWN_LIGHT, "Big 4 Association — 5 nights"),
        ("SEPT",      "Pendleton Round-Up",   "Pendleton, OR",  "~215 mi", C.BROWN_LIGHT, "100+ year legacy — goal: Year 2-3"),
    ]
    for item in tier3:
        story.append(TimelineItem(*item))
        story.append(sp(4))

    story.append(PageBreak())


# ── PRICING TIERS ─────────────────────────────────────────
def pricing(story):
    story.append(PagePurposeBar(
        "Simple pricing. Published rates only. No negotiating at the gate.",
        level=2, level_label="L2  —  WHEN NEEDED"))
    story.append(sp(10))

    story.append(p("<b>What you sell</b>  —  three types, that's it", "L1Head"))
    story.append(sp(8))

    # Product cards in a 2-column layout
    products = [
        ("Digital Downloads",   C.SAGE,
         [("Single image",         "$15–20"),
          ("5-image bundle",       "$55–70"),
          ("All-day package",      "$125–175"),
          ("Social media pack (5 vertical)", "$95")]),
        ("On-Site Prints",      C.RUST,
         [("4x6 print",            "$12"),
          ("8x10 print",           "$28"),
          ("16x20 canvas (45MP)", "$175–250"),
          ("Print + digital combo","$40")]),
        ("B2B / Organizer",     C.BROWN_MID,
         [("Event coverage package", "$500–1,200"),
          ("Social delivery same day","+$200"),
          ("Sponsor logo overlay",   "+$150"),
          ("Annual contract (4-6)",  "$2,500–5,000")]),
    ]

    class ProductCard(Flowable):
        def __init__(self, title, color, items):
            self.title=title; self.color=color; self.items=items
            self.width=0; self.height=130
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.CREAM)
            c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
            c.setFillColor(self.color)
            c.roundRect(0,self.height-32,self.width,32,6,fill=1,stroke=0)
            c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
            c.setFillColor(C.WHITE)
            c.setFont("Times-Bold",12)
            c.drawString(10,self.height-22,self.title)
            y=self.height-46
            for label,price in self.items:
                c.setFillColor(C.BROWN_MID)
                c.setFont("Helvetica",8)
                c.drawString(10,y,label)
                c.setFillColor(self.color)
                c.setFont("Times-Bold",11)
                c.drawRightString(self.width-10,y,price)
                c.setStrokeColor(C.RULE)
                c.setLineWidth(0.3)
                c.line(10,y-3,self.width-10,y-3)
                y-=20

    p_cards = [ProductCard(*d) for d in products]

    t = Table([[p_cards[0], sp(8), p_cards[1], sp(8), p_cards[2]]],
              colWidths=[2.25*inch, 0.15*inch, 2.25*inch, 0.15*inch, 2.25*inch])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(t)
    story.append(sp(12))
    story.append(rule())

    # Revenue strip
    story.append(p("<b>Revenue per event  —  North Idaho market</b>", "L2Head"))
    story.append(sp(6))

    class RevenueStrip(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 52
        def draw(self):
            c=self.canv
            items=[
                ("Conservative\nper event",  "$725",   C.SAGE),
                ("Optimistic\nper event",     "$2,350", C.RUST),
                ("10 events\nconservative",   "$7,250", C.BROWN_MID),
                ("10 events\noptimistic",     "$23,500+", C.BULL),
            ]
            w=self.width/4-6
            x=0
            for label,amount,col in items:
                c.setFillColor(C.WARM_TAN)
                c.roundRect(x,0,w,50,6,fill=1,stroke=0)
                c.setFillColor(col)
                c.setFont("Times-Bold",18)
                c.drawCentredString(x+w/2,28,amount)
                c.setFillColor(C.BROWN_MID)
                c.setFont("Helvetica",7.5)
                for i,ln in enumerate(label.split("\n")):
                    c.drawCentredString(x+w/2,15-i*10,ln)
                x+=w+8

    story.append(RevenueStrip())
    story.append(sp(10))

    story.append(ExpandSection([
        ("Avoid",     "Manual email delivery  |  Selling from original cards  |  3+ events per weekend solo"),
        ("Tools",     "SmugMug or Pic-Time ($15-30/mo) — auto-fulfillment, no manual labor"),
        ("B2B pitch", "Year 1: offer free coverage  ->  Year 2: lock in annual paid contract"),
    ]))
    story.append(PageBreak())


# ── STYLE GUIDE ───────────────────────────────────────────
def style_guide(story):
    story.append(PagePurposeBar(
        "The complete design system — for recreating or extending this guide.",
        level=3, level_label="L3  —  REFERENCE"))
    story.append(sp(10))

    story.append(p("<b>Color Palette</b>", "L1Head"))
    story.append(sp(8))

    class SwatchRow(Flowable):
        def __init__(self, swatches):
            self.swatches=swatches; self.width=0; self.height=52
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            n=len(self.swatches)
            w=self.width/n-6
            x=0
            for name,color,hex_val in self.swatches:
                c.setFillColor(color)
                c.roundRect(x,14,w,36,5,fill=1,stroke=0)
                c.setFillColor(C.BROWN_MID)
                c.setFont("Helvetica-Bold",7)
                c.drawCentredString(x+w/2,7,name)
                c.setFillColor(C.BROWN_LIGHT)
                c.setFont("Helvetica",6.5)
                c.drawCentredString(x+w/2,0,hex_val)
                x+=w+6

    story.append(SwatchRow([
        ("Cream Base",   C.CREAM,       "#FAF6EE"),
        ("Warm Tan",     C.WARM_TAN,    "#EDE0C8"),
        ("Sage",         C.SAGE,        "#7A9E82"),
        ("Sage Dark",    C.SAGE_DARK,   "#4A7255"),
        ("Sage Light",   C.SAGE_LIGHT,  "#D8EAD9"),
        ("Dusty Rose",   C.ROSE,        "#C4887A"),
        ("Rose Light",   C.ROSE_LIGHT,  "#F0DDD8"),
        ("Rust",         C.RUST,        "#A85C42"),
    ]))
    story.append(sp(6))
    story.append(SwatchRow([
        ("Dark Brown",   C.BROWN_DARK,  "#3D2410"),
        ("Mid Brown",    C.BROWN_MID,   "#7A4A28"),
        ("Light Brown",  C.BROWN_LIGHT, "#C4A882"),
        ("Brown Pale",   C.BROWN_PALE,  "#EAD8C0"),
        ("Bull Red",     C.BULL,        "#8B3A3A"),
        ("Barrel Teal",  C.BARREL,      "#3A6B5A"),
        ("Rope Amber",   C.ROPE,        "#7A5F28"),
        ("General Blue", C.GENERAL,     "#5A6B8A"),
    ]))
    story.append(sp(12))
    story.append(rule())

    story.append(p("<b>Typography</b>", "L1Head"))
    story.append(sp(6))

    type_data = [
        ["USE", "FONT", "SIZE", "COLOR", "EXAMPLE"],
        ["Page headers / event names", "Times-Bold", "16-20pt", "Dark Brown / Accent", "Bull Riding"],
        ["Section headers (L1)", "Times-Bold", "16pt", "Dark Brown", "Set this first"],
        ["Sub-headers (L2, L3)", "Times-Bold / Times-Italic", "11-13pt", "Mid Brown / Light", "When needed"],
        ["Setting values (cards)", "Times-Bold", "13-16pt", "Accent color", "1/2000 – 1/3200"],
        ["Body text", "Helvetica", "9pt", "Mid Brown", "Two lines maximum"],
        ["Labels / tags", "Helvetica-Bold", "7.5-8.5pt", "Varies by status", "SHUTTER SPEED"],
        ["Notes / L3 content", "Helvetica / Oblique", "7.5-8pt", "Light Brown", "Optional detail"],
        ["Callouts / grounding", "Times-Italic", "12pt", "Sage Dark", "Calm and centered"],
    ]
    tstyle = [
        ("BACKGROUND",    (0,0),(-1,0), C.BROWN_DARK),
        ("TEXTCOLOR",     (0,0),(-1,0), C.CREAM),
        ("FONTNAME",      (0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",      (0,0),(-1,-1), 7.5),
        ("FONTNAME",      (0,1),(-1,-1), "Helvetica"),
        ("TEXTCOLOR",     (0,1),(-1,-1), C.BROWN_DARK),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [C.CREAM, C.WARM_TAN]),
        ("GRID",          (0,0),(-1,-1), 0.3, C.RULE),
        ("TOPPADDING",    (0,0),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-1), 4),
        ("LEFTPADDING",   (0,0),(-1,-1), 6),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ]
    tt = Table(type_data, colWidths=[1.8*inch, 1.6*inch, 0.7*inch, 1.2*inch, 1.95*inch])
    tt.setStyle(TableStyle(tstyle))
    story.append(tt)

    story.append(sp(12))
    story.append(rule())

    story.append(p("<b>Page Template  —  Reuse This Every Time</b>", "L1Head"))
    story.append(sp(6))

    class TemplatePreview(Flowable):
        def wrap(self, aw, ah):
            self.width=aw; return aw, 3.5*inch
        def draw(self):
            c=self.canv
            W=self.width; H=3.5*inch
            c.setStrokeColor(C.RULE); c.setLineWidth(0.5)
            c.roundRect(0,0,W,H,8,fill=0,stroke=1)
            # Top purpose bar
            c.setFillColor(C.WARM_TAN)
            c.roundRect(8,H-44,W-16,36,5,fill=1,stroke=0)
            c.setFillColor(C.RUST); c.roundRect(8,H-44,5,36,3,fill=1,stroke=0)
            c.setFillColor(C.RUST); c.roundRect(12,H-30,70,12,4,fill=1,stroke=0)
            c.setFillColor(C.WHITE); c.setFont("Helvetica-Bold",6)
            c.drawString(16,H-24,"L1 — USE FIRST")
            c.setFillColor(C.BROWN_DARK); c.setFont("Times-Italic",9)
            c.drawString(90,H-24,"What this page helps you do — one clear sentence")
            # L1 zone
            c.setFillColor(C.ROSE_LIGHT)
            c.roundRect(8,H-106,W-16,54,5,fill=1,stroke=0)
            c.setFillColor(C.BULL); c.setFont("Helvetica-Bold",7)
            c.drawString(14,H-54,"L1 — CRITICAL (3-4 items max)")
            # Three card placeholders
            cw=(W-40)/3
            for i in range(3):
                cx=14+i*(cw+8)
                c.setFillColor(C.WHITE); c.roundRect(cx,H-100,cw,40,4,fill=1,stroke=0)
                c.setFillColor(C.RULE); c.roundRect(cx,H-100,4,40,3,fill=1,stroke=0)
                c.setFillColor(C.BROWN_LIGHT); c.setFont("Helvetica",6)
                c.drawString(cx+8,H-72,"SETTING"); c.drawString(cx+8,H-84,"Value")
            # L2 zone
            c.setFillColor(C.SAGE_LIGHT)
            c.roundRect(8,H-176,W-16,62,5,fill=1,stroke=0)
            c.setFillColor(C.SAGE_DARK); c.setFont("Helvetica-Bold",7)
            c.drawString(14,H-122,"L2 — WHEN NEEDED")
            cw2=(W-40)/2
            for i in range(2):
                cx=14+i*(cw2+12)
                c.setFillColor(C.WHITE); c.roundRect(cx,H-170,cw2-4,42,4,fill=1,stroke=0)
                c.setFillColor(C.SAGE); c.roundRect(cx,H-136,cw2-4,12,4,fill=1,stroke=0)
                c.rect(cx,H-130,cw2-4,6,fill=1,stroke=0)
                c.setFillColor(C.WHITE); c.setFont("Helvetica-Bold",5.5)
                c.drawString(cx+4,H-129,"CHUNK LABEL")
                for j in range(3):
                    c.setFillColor(C.BROWN_LIGHT)
                    c.circle(cx+8,H-142-j*10,2,fill=1,stroke=0)
                    c.setFillColor(C.BROWN_MID)
                    c.setFont("Helvetica",5.5)
                    c.drawString(cx+14,H-145-j*10,"Info item here")
            # L3 expand zone
            c.setDash([3,3]); c.setStrokeColor(C.RULE)
            c.roundRect(8,H-226,W-16,42,5,fill=0,stroke=1); c.setDash([])
            c.setFillColor(C.BROWN_LIGHT); c.setFont("Helvetica-Bold",6)
            c.drawString(14,H-194,"v  IF YOU NEED MORE DETAIL  (dashed = optional)")
            c.setFont("Helvetica",5.5)
            c.drawString(14,H-204,"Full setting details  |  Edge cases  |  Advanced context")

    story.append(TemplatePreview())
    story.append(sp(10))

    story.append(p("<b>Spacing system:</b>  page margins 0.75in  |  card padding 12pt  |  "
                   "section gap 12pt  |  rule after each section  |  max 4 items per chunk",
                   "ExpandBody"))
    story.append(PageBreak())


# ── OUTREACH + CHECKLIST ──────────────────────────────────
def outreach_checklist(story):
    story.append(PagePurposeBar(
        "Send the right message. Show up prepared. That's the whole system.",
        level=2, level_label="L2  —  WHEN NEEDED"))
    story.append(sp(10))

    story.append(p("<b>Outreach Template  —  Home Turf (Copy and Send)</b>", "L1Head"))
    story.append(sp(6))

    class ScriptBox(Flowable):
        def __init__(self, lines, accent=C.RUST, bg=C.RUST_PALE):
            self.lines=lines; self.accent=accent; self.bg=bg
            self.width=0; self.height=len(lines)*13+22
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(self.bg)
            c.roundRect(0,0,self.width,self.height,6,fill=1,stroke=0)
            c.setFillColor(self.accent)
            c.roundRect(0,0,5,self.height,4,fill=1,stroke=0)
            y=self.height-14
            for line in self.lines:
                if line.startswith("**"):
                    c.setFont("Helvetica-Bold",8.5); c.setFillColor(self.accent)
                    c.drawString(14,y,line.replace("**",""))
                elif line=="":
                    pass
                else:
                    c.setFont("Helvetica",8.5); c.setFillColor(C.BROWN_MID)
                    c.drawString(14,y,line)
                y-=13

    story.append(ScriptBox([
        "**Subject: Photography for [Event Name] — Tribal Cowboy",
        "",
        "Hi [Name],",
        "",
        "I'm Stacie with Tribal Cowboy, an equine experience brand based right here in",
        "North Idaho (Careywood area). We photograph rodeos for local families and riders.",
        "",
        "  -  High-resolution event images for your social media — free to you",
        "  -  Digital gallery sales to participants and families — I handle everything",
        "  -  Full credit and tags to your event in all published content",
        "",
        "No cost to you. We're local, we know your audience.",
        "",
        "Can we connect this week?   Stacie | Tribal Cowboy | [phone]",
    ]))
    story.append(sp(8))

    story.append(ScriptBox([
        "**DM Template — Barrel Racing Jackpots (no credentials needed)",
        "",
        "Hey [Name]! I'm Stacie with Tribal Cowboy — rodeo photography out of North Idaho.",
        "I'd love to come shoot the barrel racing this [date] and share the gallery",
        "so riders can grab their photos. Would that be okay with the organizers?",
    ], accent=C.SAGE_DARK, bg=C.SAGE_LIGHT))

    story.append(sp(10))
    story.append(rule())

    story.append(p("<b>Pre-Event Checklist  —  Before You Leave Home</b>", "L1Head"))
    story.append(sp(6))

    class Checklist(Flowable):
        def __init__(self, items, cols=2, accent=C.SAGE):
            self.items=items; self.cols=cols; self.accent=accent
            self.width=0
            per_col=len(items)//cols + (1 if len(items)%cols else 0)
            self.height=per_col*20+24
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(C.WARM_TAN)
            c.roundRect(0,0,self.width,self.height,6,fill=1,stroke=0)
            c.setFillColor(self.accent)
            c.roundRect(0,self.height-22,self.width,22,6,fill=1,stroke=0)
            c.rect(0,self.height-12,self.width,12,fill=1,stroke=0)
            c.setFillColor(C.WHITE); c.setFont("Helvetica-Bold",9)
            c.drawString(12,self.height-16,"BEFORE YOU LEAVE HOME")
            col_w=self.width/self.cols
            per_col=len(self.items)//self.cols+(1 if len(self.items)%self.cols else 0)
            for i,item in enumerate(self.items):
                col=i//per_col; row=i%per_col
                x=col*col_w+12; y=self.height-36-row*20
                # checkbox
                c.setStrokeColor(self.accent); c.setFillColor(C.WHITE)
                c.setLineWidth(1)
                c.roundRect(x,y+2,12,12,2,fill=1,stroke=1)
                c.setFillColor(C.BROWN_DARK)
                c.setFont("Helvetica",8.5)
                c.drawString(x+18,y+4,item)

    story.append(Checklist([
        "Written confirmation from event coordinator",
        "Know who to ask for at the gate — by name",
        "Printed confirmation + 10 business cards",
        "Flash rules, zone limits confirmed",
        "Liability waiver signed if required",
        "3x CFexpress cards formatted in-body",
        "3x LP-E6NH batteries per body, charged",
        "AF Menu: Subject Detect = ANIMALS",
        "Pre-shot: Shooting Menu 4 = ON",
        "C1=Bull  C2=Barrel  C3=General set",
        "Gallery platform ready (test login)",
        "Lens cloth in vest pocket",
    ], cols=2, accent=C.SAGE_DARK))

    story.append(sp(10))

    # Notion + print suggestions
    story.append(rule())
    story.append(p("<b>Also suggested</b>", "L2Head"))
    story.append(sp(6))

    sug_data = [
        ("Notion Version",
         C.GENERAL, C.GENERAL_PALE,
         ["Duplicate this structure as a Notion database",
          "Each event = a page with toggle blocks for L2/L3",
          "Quick reference = a Notion table view",
          "Link your SmugMug + calendar inside"]),
        ("Laminated Card",
         C.RUST, C.RUST_PALE,
         ["Print Quick Reference page at 80% scale",
          "Laminate at Staples — fits in vest pocket",
          "4 event cards + shutter mode strip",
          "This is your in-arena reference, nothing else"]),
        ("Phone Reference",
         C.SAGE_DARK, C.SAGE_LIGHT,
         ["Screenshot Quick Reference page",
          "Save to phone Photos as a pinned album",
          "Or: create a Notion mobile page",
          "3 taps to any setting from your lock screen"]),
    ]

    class SugCard(Flowable):
        def __init__(self, title, acc, bg, items):
            self.title=title; self.acc=acc; self.bg=bg; self.items=items
            self.width=0; self.height=108
        def wrap(self, aw, ah):
            self.width=aw; return aw, self.height
        def draw(self):
            c=self.canv
            c.setFillColor(self.bg); c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
            c.setFillColor(self.acc)
            c.roundRect(0,self.height-30,self.width,30,6,fill=1,stroke=0)
            c.rect(0,self.height-18,self.width,18,fill=1,stroke=0)
            c.setFillColor(C.WHITE); c.setFont("Helvetica-Bold",9)
            c.drawString(10,self.height-21,self.title)
            y=self.height-44
            for item in self.items:
                c.setFillColor(self.acc); c.circle(10,y+3,2.5,fill=1,stroke=0)
                c.setFillColor(C.BROWN_MID); c.setFont("Helvetica",8)
                c.drawString(18,y,item); y-=16

    sug_cards = [SugCard(*d) for d in sug_data]
    st = Table([[sug_cards[0], sp(8), sug_cards[1], sp(8), sug_cards[2]]],
               colWidths=[2.25*inch, 0.15*inch, 2.25*inch, 0.15*inch, 2.25*inch])
    st.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    story.append(st)
    story.append(sp(10))
    story.append(p(
        '"You don\'t need to be ready for everything. You just need to be ready for what\'s in front of you."',
        "Callout"))


# ══════════════════════════════════════════════════════════
#  ASSEMBLE
# ══════════════════════════════════════════════════════════

def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
        topMargin=0.65*inch,
        bottomMargin=0.55*inch,
        title="Tribal Cowboy Rodeo Field Guide — Redesigned",
        author="Tribal Cowboy",
        subject="ADHD-Optimized Rodeo Photography System | Canon R5 Mark II",
    )

    story = []
    cover(story)
    how_to_use(story)
    quick_reference(story)
    bull_riding(story)
    barrel_racing(story)
    gear_kit(story)
    event_calendar(story)
    pricing(story)
    style_guide(story)
    outreach_checklist(story)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    build()
