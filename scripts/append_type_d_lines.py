from docx import Document
P = "/Users/staciehuffhines/Documents/Claude Yap Edits ready to edit/Yap Edits files/Yap_Edits_Editor_Prompt.docx"
ADD = " For type D, overlay-plan.md starts with two lines copied from the brief entry I paste: `Hook: <hook>` and `Sound: <audio>`."
d = Document(P)
p = next(x for x in d.paragraphs if x.text.startswith("- Type D, trend remix"))
if ADD.strip() in p.text:
    raise SystemExit("already present; nothing to do")
p.runs[-1].text += ADD
d.save(P)
print("type D lines added")
