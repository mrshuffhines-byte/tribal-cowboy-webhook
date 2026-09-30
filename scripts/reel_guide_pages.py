# Copy for each page. Short sentences. No paragraphs over two sentences.
PAGES = [
    dict(
        num="1", title="Film", one="Point the phone at the ranch and talk.",
        checklist=["Lens wiped, phone at eye level", "A hand of space above your head", "Say the hook first, keep rolling through mistakes"],
        say="Nothing yet. Just film.",
        picture="film",
    ),
    dict(
        num="2", title="Drop", one="Move the clip into the Yap Edits folder.",
        checklist=["AirDrop the clip to this Mac", "Talking reel: main folder", "Voice over: a new subfolder with clips and your voice memo"],
        say="Nothing yet. Just drop.",
        picture="folder",
    ),
    dict(
        num="3", title="Ask and edit", one="Open the Claude app, send the message, answer three questions.",
        checklist=["Project: Yap Edits Reel Editor", "Cowork switched on", "Answer: type, length, setting"],
        say='Please request access to my folder called "Claude Yap Edits ready to edit" in Documents. Look at what is new in it, ask me the three questions, then edit using my Yap Edits Editor Prompt, the Playbook, and My Rules.md. Save the draft to the Edited subfolder.',
        picture="claude",
    ),
    dict(
        num="4", title="Review", one="Watch the draft twice. Once with sound, once muted.",
        checklist=["Captions clear of your mouth", "Nothing cut off at the edges", "Ends on the Follow click"],
        say="Move the captions a little left and use fewer zooms. Give me that as a rule for My Rules.md.",
        picture="review",
    ),
    dict(
        num="5", title="Schedule", one="Open Claude Code in TribalCowboy Social and run one command.",
        checklist=["Type /schedule-reel", "Paste the Dropbox link when asked", "Say yes to the plan"],
        say="/schedule-reel",
        picture="schedule",
    ),
    dict(
        num="6", title="Weekly", one="Two commands on Monday. Ten minutes.",
        checklist=["/reel-report shows what held attention", "/trend-brief gives you 3 to 5 things to film", "/hooks before a talking reel"],
        say="/reel-report   then   /trend-brief",
        picture="weekly",
    ),
]
LOOP = ["Film", "Drop", "Ask and edit", "Review", "Schedule", "Report", "Next idea"]
