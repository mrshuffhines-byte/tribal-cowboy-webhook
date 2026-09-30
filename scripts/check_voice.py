import re, sys, os
from pathlib import Path

BRAND_PATH = os.environ.get("BRAND_MEMORY_PATH")
BRAND = Path(BRAND_PATH) if BRAND_PATH else Path(__file__).resolve().parent.parent / "memory" / "brand-memory.md"
HERD = ["Belle", "Millie", "Abby", "Jill", "Reba", "Dolly", "Lainey", "Minimus",
        "Monster", "Master Chief", "Jolene", "Rowdy", "Nash", "Monster Unicorn"]
# names that a model tends to invent for horses
SUSPECT = ["Duke", "Thunder", "Storm", "Blaze", "Shadow", "Spirit", "Maverick", "Bandit"]
# horse-related words to check for context in unknown horse detection
HORSE_WORDS = ["horse", "horses", "mare", "gelding", "pony", "ponies", "mini", "minis",
               "clydesdale", "clydesdales", "herd", "wagon", "paddock", "barn", "stallion",
               "filly", "colt", "pulled", "rode", "saddle"]

def normalize_text(text):
    """Normalize curly quotes and apostrophes to straight versions."""
    text = text.replace(''', "'")
    text = text.replace(''', "'")
    text = text.replace('"', '"')
    text = text.replace('"', '"')
    return text

def banned_phrases():
    try:
        if not BRAND.exists():
            raise FileNotFoundError(f"Brand memory file not found: {BRAND}")
        text = BRAND.read_text()
        if "## Banned Phrases" not in text:
            raise ValueError("Missing '## Banned Phrases' section in brand memory")
        block = text.split("## Banned Phrases")[1].split("## Premium Vocabulary")[0]
        phrases = []
        for line in block.splitlines():
            m = re.match(r"\d+\.\s+(.*)", line.strip())
            if not m:
                continue
            for q in re.findall(r'["""]([^""]+)["""]', m.group(1)):
                phrases.append(normalize_text(q.lower()))
        if not phrases:
            raise ValueError("No phrases parsed from '## Banned Phrases' section")
        return phrases
    except (FileNotFoundError, IndexError, ValueError) as e:
        sys.stderr.write(f"Error parsing brand memory: {e}\n")
        sys.exit(2)

def sentence_has_horse_word(sentence):
    """Check if sentence contains any horse-related word (case-insensitive)."""
    low_sent = sentence.lower()
    return any(re.search(rf"\b{word}\b", low_sent) for word in HORSE_WORDS)

def main():
    try:
        text = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    except (FileNotFoundError, IOError) as e:
        sys.stderr.write(f"Error reading input: {e}\n")
        sys.exit(2)

    norm_text = normalize_text(text)
    low = norm_text.lower()
    problems = []

    # Check banned phrases with word boundaries
    for p in banned_phrases():
        core = p.replace("...", "").strip()
        if core:
            pattern = r"\b" + re.escape(core) + r"\b"
            if re.search(pattern, low):
                problems.append(f"banned: {p}")

    # Check unknown horses only if sentence contains horse word
    sentences = re.split(r'[.!?]', text)
    for name in SUSPECT:
        for sentence in sentences:
            if re.search(rf"\b{name}\b", sentence, re.IGNORECASE) and sentence_has_horse_word(sentence):
                problems.append(f"unknown horse: {name}")
                break

    # Check exclamations
    n = text.count("!")
    if n > 1:
        problems.append(f"exclamations: {n}")

    for line in problems:
        print(line)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
