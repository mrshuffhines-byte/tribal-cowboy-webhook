from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, ListFlowable, ListItem
)

GOLD = HexColor("#b08d57")
DARK = HexColor("#28231e")
MUTED = HexColor("#6e6964")
CREAM = HexColor("#f5f1ea")
LINE = HexColor("#b4afaa")

OUT = "/home/user/tribal-cowboy-webhook/Camp-Ka-Mee-Lin-Call-Sheet.pdf"

styles = getSampleStyleSheet()

eyebrow = ParagraphStyle("eyebrow", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
    spaceAfter=2, leading=11)
title = ParagraphStyle("title", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=22, textColor=DARK,
    spaceAfter=2, leading=26)
subhead = ParagraphStyle("subhead", parent=styles["Normal"],
    fontName="Helvetica", fontSize=11, textColor=MUTED,
    spaceAfter=12, leading=14)
h2 = ParagraphStyle("h2", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=11, textColor=GOLD,
    spaceBefore=14, spaceAfter=4, leading=14)
body = ParagraphStyle("body", parent=styles["Normal"],
    fontName="Helvetica", fontSize=10.5, textColor=DARK,
    leading=14, spaceAfter=4)
body_bold = ParagraphStyle("bodyb", parent=body,
    fontName="Helvetica-Bold")
script = ParagraphStyle("script", parent=body,
    fontName="Helvetica-Oblique", leftIndent=10, rightIndent=10,
    borderColor=GOLD, borderPadding=8, borderWidth=0,
    backColor=HexColor("#f8f4ec"),
    spaceBefore=4, spaceAfter=8, leading=14, textColor=DARK)
q_label = ParagraphStyle("qlabel", parent=body,
    fontName="Helvetica-Bold", spaceBefore=6, spaceAfter=2)
bullet_style = ParagraphStyle("bullet", parent=body,
    leftIndent=14, bulletIndent=2, spaceAfter=2)


def fill_line(c_width=6.9*inch):
    """Returns a flowable that draws a single fill-in line."""
    return HRFlowable(width="100%", thickness=0.5, color=LINE,
                      spaceBefore=10, spaceAfter=0)


def q_block(label, lines=2, story=None):
    story.append(Paragraph(label, q_label))
    for _ in range(lines):
        story.append(Spacer(1, 6))
        story.append(HRFlowable(width="100%", thickness=0.5, color=LINE))
    story.append(Spacer(1, 4))


def draw_page_footer(c, doc):
    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    c.drawCentredString(LETTER[0] / 2, 0.4 * inch, f"Page {doc.page}")
    if doc.page > 1:
        c.setFont("Helvetica", 8)
        c.setFillColor(MUTED)
        c.drawString(0.7*inch, LETTER[1] - 0.4*inch,
                     "Tribal Cowboy  |  Camp Ka-Mee-Lin Call Sheet")
    c.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=LETTER,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch,
    title="Camp Ka-Mee-Lin Call Sheet")

story = []

# COVER / PAGE 1
story.append(Paragraph("TRIBAL COWBOY  &nbsp;|&nbsp;  CALL SHEET", eyebrow))
story.append(Paragraph("Camp Ka-Mee-Lin Callback", title))
story.append(Paragraph("Post Falls Parks &amp; Recreation  &nbsp;|&nbsp;  Summer 2026", subhead))

# Contact box
contact_data = [
    [Paragraph("<b>CONTACT:</b>", body), Paragraph("Greg Chambers, Director", body)],
    [Paragraph("<b>PHONE:</b>", body), Paragraph("208-262-7352", body)],
    [Paragraph("<b>DATE OF CALL:</b>", body), ""],
    [Paragraph("<b>TIME:</b>", body), ""],
]
contact_tbl = Table(contact_data, colWidths=[1.4*inch, 5.5*inch])
contact_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LINEBELOW", (1, 2), (1, 2), 0.5, LINE),
    ("LINEBELOW", (1, 3), (1, 3), 0.5, LINE),
]))
story.append(contact_tbl)
story.append(Spacer(1, 12))

story.append(Paragraph("QUICK INTEL (YOU ALREADY KNOW THIS)", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=6))
intel = [
    "Camp Ka-Mee-Lin has run since 1995 &mdash; celebrated 30th anniversary in 2025.",
    "Day camp, Kindergarten &ndash; 6th grade. Kiwanis Park, Post Falls.",
    "120+ kids per week. 11 weeks. Families pay $190/week per child.",
    "Post Falls Parks &amp; Rec runs on a $9.2M annual budget.",
    "They have a FORMAL sponsorship program &mdash; Greg is used to receiving money, not paying it.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=14) for x in intel],
    bulletType="bullet", start="-", leftIndent=12))

story.append(Paragraph("OPENING LINE", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=6))
story.append(Paragraph(
    "&ldquo;Hey Greg, thanks for reaching out &mdash; got your message about Camp "
    "Ka-Mee-Lin. Tell me a bit about the program and what you had in mind for Tribal Cowboy.&rdquo;",
    script))
story.append(Paragraph("Let him talk first. Listen. Take notes below.", body_bold))

# PAGE 2 - Questions
story.append(PageBreak())
story.append(Paragraph("QUESTIONS TO ASK GREG", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8))

q_block('1. What does "sponsorship" mean to you specifically &mdash; cash, services, or performance?', 2, story)
q_block("2. How many kids attend per week? Age range?", 2, story)
q_block("3. Are parents present during programming, or drop-off only?", 2, story)
q_block("4. What dates/weeks are you looking at? Day of week? Time of day?", 2, story)
q_block('5. What would "coming to camp" actually look like &mdash; performance, workshop, demo?', 2, story)
q_block("6. How long are you envisioning &mdash; 1 hour, half day, full day?", 2, story)

# PAGE 3
story.append(PageBreak())
story.append(Paragraph("QUESTIONS TO ASK GREG (CONTINUED)", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8))

q_block("7. Do you have a programming or enrichment budget for outside vendors?", 2, story)
q_block("8. Have you worked with paid performers/vendors before? What did that look like?", 2, story)
q_block("9. What gets produced for sponsors/partners &mdash; Activity Guide? T-shirts? Social posts?", 2, story)
q_block("10. Who has final sign-off on the budget &mdash; you, or someone else in the department?", 2, story)
q_block("11. What's your timeline &mdash; when do you need a decision?", 2, story)
q_block("12. Anything else you want me to know before we talk pricing?", 2, story)

# PAGE 4 - Pricing
story.append(PageBreak())
story.append(Paragraph("YOUR PRICING CHEAT SHEET", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8))

price_data = [
    ["TIER", "RATE", "WHEN TO USE"],
    ["Anchor / Opening", "$900 / visit", "Large group (40+) published rate"],
    ["Community Rate", "$600 / visit", "If he pushes back on price"],
    ["Walk-Away Floor", "$600", "Below this = losing money. Stop."],
    ["Multi-Visit Package", "$2,500\u20133,500", "4 visits across summer"],
]
price_tbl = Table(price_data, colWidths=[2.0*inch, 1.6*inch, 3.3*inch])
price_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CREAM),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (1, 1), (1, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("TEXTCOLOR", (0, 0), (-1, -1), DARK),
    ("GRID", (0, 0), (-1, -1), 0.5, GOLD),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(price_tbl)
story.append(Spacer(1, 10))

story.append(Paragraph("How to deliver the number:", body_bold))
story.append(Paragraph(
    "&ldquo;For a camp your size &mdash; 120 kids &mdash; we&rsquo;d be looking at our large "
    "group rate, which starts at $900 for a single camp day. That includes multiple stations, "
    "skill-building, and the cultural components. If you want us out there a few times across "
    "the summer, we can put together a package rate that&rsquo;s better per visit. What does "
    "your programming budget look like on your end?&rdquo;", script))
story.append(Paragraph("After you give the number &mdash; STOP TALKING. Let him respond.", body_bold))

story.append(Paragraph("IF HE PUSHES BACK ON PRICE", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=6))
story.append(Paragraph(
    "&ldquo;I hear you. For city and municipal programs we offer a community rate of $600 per "
    "visit. That&rsquo;s a real discount and it&rsquo;s the lowest we can go and still do right "
    "by our team. If your budget can work with that, we can make this happen this summer.&rdquo;",
    script))

story.append(Paragraph("IF HE WANTS FREE / SPONSORSHIP ONLY", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=6))
story.append(Paragraph(
    "&ldquo;Greg, I appreciate the ask, but sponsorship isn&rsquo;t the model we can work with "
    "&mdash; we&rsquo;re a working business and every visit is a job. If programming dollars "
    "open up on your end, we&rsquo;d love to be on your list. And if you know of other Parks "
    "&amp; Rec or school programs with budgets, send them our way.&rdquo;", script))

story.append(Paragraph("EXTRAS TO ASK FOR (AT ANY PRICE POINT)", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=6))
extras = [
    "Permission to photograph/film the visit for Tribal Cowboy&rsquo;s content.",
    "Listing in the Post Falls Activity Guide as a featured program partner.",
    "Tagged social post from Post Falls Parks &amp; Rec Facebook page.",
    "City letter acknowledging the engagement (good for future grant apps).",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=14) for x in extras],
    bulletType="bullet", start="-", leftIndent=12))

# PAGE 5 - Notes
story.append(PageBreak())
story.append(Paragraph("NOTES DURING CALL", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))
for _ in range(16):
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE))

# PAGE 6 - Decision
story.append(PageBreak())
story.append(Paragraph("POST-CALL DECISION", h2))
story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))

q_block("Quoted price:", 1, story)
q_block("Scope agreed on (hours, date, # of kids):", 2, story)
q_block("Extras secured (Activity Guide, social, letter, photos):", 2, story)
q_block("Next step (proposal due by, follow-up date):", 2, story)

story.append(Spacer(1, 12))
story.append(Paragraph("Decision:", body_bold))
story.append(Spacer(1, 4))
decision_data = [[
    "\u25A1  Booked",
    "\u25A1  Needs proposal",
    "\u25A1  Follow-up scheduled",
    "\u25A1  Passed",
]]
dec_tbl = Table(decision_data, colWidths=[1.7*inch]*4)
dec_tbl.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 11),
    ("TEXTCOLOR", (0, 0), (-1, -1), DARK),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
]))
story.append(dec_tbl)

doc.build(story, onFirstPage=draw_page_footer, onLaterPages=draw_page_footer)
print(f"PDF built: {OUT}")
