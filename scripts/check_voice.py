import re, sys
from pathlib import Path

BRAND = Path(__file__).resolve().parent.parent / "memory" / "brand-memory.md"
HERD = ["Belle", "Millie", "Abby", "Jill", "Reba", "Dolly", "Lainey", "Minimus",
        "Monster", "Master Chief", "Jolene", "Rowdy", "Nash", "Monster Unicorn"]
# names that a model tends to invent for horses
SUSPECT = ["Duke", "Thunder", "Storm", "Blaze", "Shadow", "Spirit", "Maverick", "Bandit"]

def banned_phrases():
    text = BRAND.read_text()
    block = text.split("## Banned Phrases")[1].split("## Premium Vocabulary")[0]
    phrases = []
    for line in block.splitlines():
        m = re.match(r"\d+\.\s+(.*)", line.strip())
        if not m:
            continue
        for q in re.findall(r'"([^"]+)"', m.group(1)):
            phrases.append(q.lower())
    return phrases

def main():
    text = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    low = text.lower()
    problems = []
    for p in banned_phrases():
        core = p.replace("...", "").strip()
        if core and core in low:
            problems.append(f"banned: {p}")
    for name in SUSPECT:
        if re.search(rf"\b{name}\b", text) and name not in HERD:
            problems.append(f"unknown horse: {name}")
    n = text.count("!")
    if n > 1:
        problems.append(f"exclamations: {n}")
    for line in problems:
        print(line)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
