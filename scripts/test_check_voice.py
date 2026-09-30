import subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent

def run(text):
    r = subprocess.run([sys.executable, str(HERE / "check_voice.py")], input=text, capture_output=True, text=True)
    return r.returncode, r.stdout

def test_clean_text_passes():
    code, out = run("Belle had opinions about breakfast. She is 22 and has earned the right.")
    assert code == 0, out

def test_banned_phrase_flagged():
    code, out = run("Memories to last a lifetime with our herd.")
    assert code == 1 and "banned: memories to last a lifetime" in out.lower()

def test_unknown_horse_flagged():
    code, out = run("Duke pulled the wagon today.")
    assert code == 1 and "unknown horse: duke" in out.lower()

def test_two_exclamations_flagged():
    code, out = run("Big day! Belle was ready! ")
    assert code == 1 and "exclamations: 2" in out

def test_real_horse_not_flagged():
    code, out = run("Master Chief acts like he runs the mini herd.")
    assert code == 0, out
