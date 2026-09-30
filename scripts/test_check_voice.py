import subprocess, sys, os, tempfile
from pathlib import Path
HERE = Path(__file__).parent

def run(text, env=None):
    r = subprocess.run([sys.executable, str(HERE / "check_voice.py")], input=text, capture_output=True, text=True, env=env)
    return r.returncode, r.stdout, r.stderr

def run_with_file(file_path):
    r = subprocess.run([sys.executable, str(HERE / "check_voice.py"), file_path], capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def test_clean_text_passes():
    code, out, _ = run("Belle had opinions about breakfast. She is 22 and has earned the right.")
    assert code == 0, out

def test_banned_phrase_flagged():
    code, out, _ = run("Memories to last a lifetime with our herd.")
    assert code == 1 and "banned: memories to last a lifetime" in out.lower()

def test_unknown_horse_flagged():
    code, out, _ = run("Duke pulled the wagon today.")
    assert code == 1 and "unknown horse: duke" in out.lower()

def test_two_exclamations_flagged():
    code, out, _ = run("Big day! Belle was ready! ")
    assert code == 1 and "exclamations: 2" in out

def test_real_horse_not_flagged():
    code, out, _ = run("Master Chief acts like he runs the mini herd.")
    assert code == 0, out

def test_no_false_positive_on_leveraged():
    code, out, _ = run("They leveraged the moment with Belle.")
    assert code == 0, out

def test_curly_apostrophe_detected():
    code, out, _ = run("We'd love to help with your party.")
    assert code == 1 and "banned: we'd love to help" in out.lower()

def test_suspect_without_horse_word_passes():
    code, out, _ = run("Storm clouds rolled in over the ridge.")
    assert code == 0, out

def test_suspect_with_horse_word_flagged():
    code, out, _ = run("Storm pulled the wagon.")
    assert code == 1 and "unknown horse: storm" in out.lower()

def test_file_argument_works():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Making memories with Millie.")
        temp_path = f.name
    try:
        code, out, _ = run_with_file(temp_path)
        assert code == 1 and "banned: making memories" in out.lower()
    finally:
        Path(temp_path).unlink()

def test_missing_brand_file_exits_2():
    env = os.environ.copy()
    env["BRAND_MEMORY_PATH"] = "/nonexistent/path/to/brand-memory.md"
    code, out, err = run("Some text", env=env)
    assert code == 2 and out == "" and "Error parsing brand memory" in err
