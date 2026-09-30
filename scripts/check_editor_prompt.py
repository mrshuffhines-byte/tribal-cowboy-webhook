import sys
from docx import Document
P = "/Users/staciehuffhines/Documents/Claude Yap Edits ready to edit/Yap Edits files/Yap_Edits_Editor_Prompt.docx"
text = "\n".join(p.text for p in Document(P).paragraphs)
required = [
    "10. VIDEO TYPES",
    "Type A",
    "Type B",
    "Type C",
    "Type D",
    "Which type",
    ".m4a, .mp3, .caf, .wav, .aac",
    "type.txt",
    "bottom third",
    "highlight-01.mp4",
]
missing = [r for r in required if r not in text]
print("missing:", missing)
sys.exit(1 if missing else 0)
