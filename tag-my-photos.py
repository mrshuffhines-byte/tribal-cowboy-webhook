#!/usr/bin/env python3
"""
TRIBAL COWBOY — Photo Metadata Cleaner & Tagger
=================================================

WHAT IT DOES:
  1. Strips ALL existing metadata (removes AI, Gemini, Google, Pixel traces)
  2. Writes clean Tribal Cowboy EXIF + IPTC metadata
  3. Renames files with SEO-optimized filenames
  4. Saves clean copies to ready-to-post/

HOW TO USE:
  1. Drop your photos into the "drop-photos-here" folder
  2. Name them: 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg (in this order):
       1 = girl + cat on green grass
       2 = girl + pony + Native blanket by fence
       3 = girl hugging mini horse
       4 = girl on blanket with cat, Wild West tee
       5 = girl wrapped in blanket, sunset portrait
     OR drop any .jpg/.jpeg/.png files and they'll get the base cleanup
  3. Open Terminal, run:
       cd /path/to/TribalCowboy-Social
       python3 tag-my-photos.py
  4. Grab your clean photos from "ready-to-post/"
"""

import os
import io
import struct
import sys

try:
    import piexif
except ImportError:
    print("Installing piexif...")
    os.system(f"{sys.executable} -m pip install piexif --break-system-packages -q")
    import piexif

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow...")
    os.system(f"{sys.executable} -m pip install Pillow --break-system-packages -q")
    from PIL import Image

from datetime import datetime


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

BUSINESS = "Tribal Cowboy LLC"
ARTIST = "Tribal Cowboy LLC"
COPYRIGHT = f"© {datetime.now().year} Tribal Cowboy LLC. All rights reserved."
WEBSITE = "www.tribalcowboy.com"
CITY = "Athol"
STATE = "Idaho"
COUNTRY = "United States"

# ═══════════════════════════════════════════════════════════════════════════════
# PHOTO METADATA — matched by filename (1.jpg, 2.jpg, etc.)
# ═══════════════════════════════════════════════════════════════════════════════

PHOTO_META = {
    "1": {
        "output_filename": "cowgirl-barn-cat-north-idaho-tribal-cowboy.jpg",
        "title": "Young Cowgirl and Barn Cat at Tribal Cowboy Ranch",
        "description": (
            "A young cowgirl in a straw cowboy hat and western tee stands on green grass "
            "with a black-and-white tuxedo barn cat at her feet. Pine trees and black "
            "ranch fencing in the background. Golden hour light at Tribal Cowboy ranch "
            "in Athol, North Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "cowgirl", "barn cat", "ranch life",
            "western lifestyle", "Athol Idaho", "horse ranch", "country kids",
            "golden hour photography", "farm cat", "Idaho ranch",
            "Indigenous owned business", "equine experience"
        ],
    },
    "2": {
        "output_filename": "cowgirl-pony-native-blanket-golden-hour-tribal-cowboy.jpg",
        "title": "Cowgirl with Pony and Native Pattern Blanket at Golden Hour",
        "description": (
            "A young girl in a cowboy hat draped in a Native pattern blanket leans "
            "close to a gray pony by a black fence at golden hour. Warm sunset light "
            "catches the geometric pattern of the blanket. Shot at Tribal Cowboy ranch "
            "in Athol, North Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "pony", "Native pattern blanket",
            "golden hour", "cowgirl", "western lifestyle", "Athol Idaho",
            "horse ranch", "Indigenous owned", "equine photography",
            "miniature horse", "ranch kids", "country life"
        ],
    },
    "3": {
        "output_filename": "cowgirl-hugging-miniature-horse-tribal-cowboy-north-idaho.jpg",
        "title": "Cowgirl Hugging Miniature Horse at Tribal Cowboy Ranch",
        "description": (
            "A young cowgirl in a straw hat drapes herself over a gray miniature horse, "
            "hugging its neck with both arms. The mini horse stands by a black ranch "
            "fence at golden hour. Pine trees and Idaho sky in the background. "
            "Tribal Cowboy ranch in Athol, North Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "miniature horse", "mini horse",
            "cowgirl", "horse hug", "ranch life", "Athol Idaho",
            "pony love", "equine experience", "western lifestyle",
            "Indigenous owned", "horse photography", "golden hour",
            "kids and horses", "North Idaho horses"
        ],
    },
    "4": {
        "output_filename": "cowgirl-wild-west-tee-native-blanket-barn-cat-tribal-cowboy.jpg",
        "title": "Cowgirl Relaxing on Native Blanket with Barn Cat",
        "description": (
            "A smiling young cowgirl in a Wild West graphic tee and straw cowboy hat "
            "lounges on a Native geometric pattern blanket on the grass. A black tuxedo "
            "barn cat curls up beside her. Golden hour sunlight at Tribal Cowboy ranch "
            "in Athol, North Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "cowgirl", "barn cat", "Native blanket",
            "Wild West", "ranch life", "golden hour", "Athol Idaho",
            "western kids", "country lifestyle", "farm life", "Idaho ranch",
            "Indigenous owned business", "equine experience"
        ],
    },
    "5": {
        "output_filename": "cowgirl-native-blanket-sunset-portrait-north-idaho-tribal-cowboy.jpg",
        "title": "Cowgirl Wrapped in Native Blanket at Sunset in North Idaho",
        "description": (
            "A young girl in a cowboy hat wrapped in a Native geometric pattern blanket "
            "gazes into the distance as golden sunset light backlights her hair. Ranch "
            "fencing and pine trees in the background. Portrait taken at Tribal Cowboy "
            "ranch in Athol, North Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "cowgirl portrait", "Native blanket",
            "sunset photography", "golden hour", "ranch portrait", "Athol Idaho",
            "western lifestyle", "country girl", "Idaho sunset",
            "Indigenous owned", "equine experience", "ranch life"
        ],
    },
}

# Fallback for any photo not numbered 1-5
DEFAULT_META = {
    "title": "Tribal Cowboy Ranch — North Idaho",
    "description": (
        "Life at Tribal Cowboy ranch in Athol, North Idaho. "
        "Indigenous-owned equine experience featuring Clydesdales, ponies, "
        "and horse photography."
    ),
    "keywords": [
        "Tribal Cowboy", "North Idaho", "Athol Idaho", "horse ranch",
        "equine experience", "Indigenous owned", "western lifestyle",
        "ranch life", "Idaho horses"
    ],
}

# ═══════════════════════════════════════════════════════════════════════════════
# AI / GEMINI / GOOGLE METADATA TAGS TO STRIP
# ═══════════════════════════════════════════════════════════════════════════════

# These are byte sequences found in EXIF/XMP that identify AI editing,
# Google Pixel phones, Gemini processing, and other AI tools.
AI_FINGERPRINTS = [
    # Google / Pixel / Gemini identifiers
    b"Google",
    b"Pixel",
    b"Gemini",
    b"GCamera",
    b"Google Photos",
    b"Google:SoftwareAgent",
    b"HDRPlusEnhanced",
    b"SpecialTypeID",
    b"MicroVideo",
    b"MotionPhoto",
    b"Gcam",
    # Adobe AI
    b"Adobe Firefly",
    b"Generative AI",
    b"ai_generated",
    b"AIGenerated",
    # Generic AI markers
    b"artificial intelligence",
    b"machine learning",
    b"neural",
    b"StableDiffusion",
    b"Midjourney",
    b"DALL-E",
    b"dalle",
    # Samsung AI
    b"Samsung AI",
    b"AIPhoto",
    # Apple AI
    b"Apple Neural",
]


# ═══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def strip_all_metadata(img):
    """
    Nuclear option: Remove ALL existing metadata from the image.
    This guarantees no AI/Gemini/Google traces survive.
    Returns a clean PIL Image with zero metadata.
    """
    # Create a brand new image with just the pixel data
    clean = Image.new(img.mode, img.size)
    clean.putdata(list(img.getdata()))

    # Preserve ICC color profile if it exists (this is NOT metadata,
    # it's color accuracy data — stripping it can shift colors)
    icc = img.info.get("icc_profile")
    if icc:
        clean.info["icc_profile"] = icc

    return clean


def build_clean_exif(title, description, keywords):
    """Build fresh EXIF data with only Tribal Cowboy metadata."""
    exif_dict = {
        "0th": {},
        "Exif": {},
        "GPS": {},
        "1st": {},
        "Interop": {},
    }

    # Basic image info
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = description.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Artist] = ARTIST.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Copyright] = COPYRIGHT.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Software] = "Tribal Cowboy Media".encode("utf-8")

    # UserComment with full SEO payload
    comment = (
        f"{title} | {description} | "
        f"Keywords: {', '.join(keywords)} | {WEBSITE}"
    )
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = (
        b"UNICODE\x00" + comment.encode("utf-16-le")
    )

    return piexif.dump(exif_dict)


def build_iptc_segment(title, description, keywords):
    """Build IPTC APP13 segment for keyword/caption indexing."""

    def iptc_tag(record, dataset, value):
        if isinstance(value, str):
            value = value.encode("utf-8")
        length = len(value)
        return struct.pack("!BBBh", 0x1C, record, dataset, length) + value

    blocks = []
    blocks.append(iptc_tag(2, 5, title))           # Object Name
    blocks.append(iptc_tag(2, 120, description))    # Caption
    for kw in keywords:
        blocks.append(iptc_tag(2, 25, kw))          # Keywords (one per tag)
    blocks.append(iptc_tag(2, 116, COPYRIGHT))       # Copyright
    blocks.append(iptc_tag(2, 80, ARTIST))           # By-line
    blocks.append(iptc_tag(2, 90, CITY))             # City
    blocks.append(iptc_tag(2, 95, STATE))            # State
    blocks.append(iptc_tag(2, 101, COUNTRY))         # Country

    iptc_data = b"".join(blocks)

    # Wrap in Photoshop 8BIM APP13 container
    header = b"Photoshop 3.0\x00"
    resource = b"8BIM" + struct.pack("!H", 0x0404) + b"\x00\x00"
    resource += struct.pack("!I", len(iptc_data)) + iptc_data
    if len(resource) % 2 != 0:
        resource += b"\x00"

    return header + resource


def inject_app13(filepath, app13_data):
    """Inject IPTC APP13 segment into a JPEG file."""
    with open(filepath, "rb") as f:
        data = f.read()

    if data[:2] != b"\xff\xd8":
        return  # Not a JPEG

    marker = b"\xff\xed"
    length = struct.pack("!H", len(app13_data) + 2)
    segment = marker + length + app13_data

    new_data = data[:2] + segment + data[2:]
    with open(filepath, "wb") as f:
        f.write(new_data)


def verify_clean(filepath):
    """Scan the output file to confirm no AI fingerprints remain."""
    with open(filepath, "rb") as f:
        data = f.read()

    found = []
    data_lower = data.lower()
    for fingerprint in AI_FINGERPRINTS:
        if fingerprint.lower() in data_lower:
            found.append(fingerprint.decode("utf-8", errors="replace"))

    return found


def process_photo(input_path, output_path, meta):
    """Full pipeline: strip → rebuild → save → verify."""

    # Open original
    img = Image.open(input_path)

    # Convert to RGB if needed (handles PNG with alpha, etc.)
    if img.mode in ("RGBA", "P", "LA"):
        img = img.convert("RGB")

    # STEP 1: Strip ALL metadata (nuclear clean)
    clean_img = strip_all_metadata(img)

    # STEP 2: Build fresh EXIF
    exif_bytes = build_clean_exif(
        meta["title"], meta["description"], meta["keywords"]
    )

    # STEP 3: Save with clean EXIF only
    save_kwargs = {"quality": 95, "exif": exif_bytes}
    if "icc_profile" in clean_img.info:
        save_kwargs["icc_profile"] = clean_img.info["icc_profile"]

    clean_img.save(output_path, "JPEG", **save_kwargs)

    # STEP 4: Inject IPTC keywords
    app13 = build_iptc_segment(
        meta["title"], meta["description"], meta["keywords"]
    )
    inject_app13(output_path, app13)

    # STEP 5: Verify no AI traces
    remaining = verify_clean(output_path)

    return remaining


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, "drop-photos-here")
    output_dir = os.path.join(script_dir, "ready-to-post")

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    print()
    print("=" * 60)
    print("  TRIBAL COWBOY — Photo Cleaner & Tagger")
    print("  Strips AI/Gemini/Google → Writes clean metadata")
    print("=" * 60)
    print()

    # Find all image files in drop-photos-here/
    valid_ext = {".jpg", ".jpeg", ".png", ".heic", ".webp"}
    photos = []
    for f in sorted(os.listdir(input_dir)):
        ext = os.path.splitext(f)[1].lower()
        if ext in valid_ext:
            photos.append(f)

    if not photos:
        print("  No photos found in drop-photos-here/")
        print()
        print("  Drop your photos there and name them:")
        print("    1.jpg = girl + cat on green grass")
        print("    2.jpg = girl + pony + Native blanket by fence")
        print("    3.jpg = girl hugging mini horse")
        print("    4.jpg = girl on blanket with cat, Wild West tee")
        print("    5.jpg = girl wrapped in blanket, sunset portrait")
        print()
        print("  Or drop ANY photos — they'll get cleaned and tagged")
        print("  with base Tribal Cowboy metadata.")
        print("=" * 60)
        return

    print(f"  Found {len(photos)} photo(s) in drop-photos-here/")
    print()

    processed = 0
    for filename in photos:
        input_path = os.path.join(input_dir, filename)

        # Match numbered photos to their specific metadata
        name_no_ext = os.path.splitext(filename)[0]
        if name_no_ext in PHOTO_META:
            meta = PHOTO_META[name_no_ext]
            output_filename = meta["output_filename"]
        else:
            # Use default Tribal Cowboy metadata for unmatched photos
            meta = {
                "title": DEFAULT_META["title"],
                "description": DEFAULT_META["description"],
                "keywords": DEFAULT_META["keywords"],
            }
            # Clean up the filename for SEO
            clean_name = name_no_ext.lower().replace(" ", "-").replace("_", "-")
            clean_name = ''.join(c for c in clean_name if c.isalnum() or c == '-')
            output_filename = f"{clean_name}-tribal-cowboy-north-idaho.jpg"

        output_path = os.path.join(output_dir, output_filename)

        print(f"  [{processed + 1}/{len(photos)}] {filename}")
        print(f"       → {output_filename}")

        try:
            remaining_ai = process_photo(input_path, output_path, meta)

            if remaining_ai:
                print(f"       ⚠ Warning: found traces of: {', '.join(remaining_ai)}")
                print(f"         (These may be false positives from pixel data)")
            else:
                print(f"       ✓ Clean — no AI/Gemini traces")

            print(f"       ✓ EXIF: {meta['title']}")
            print(f"       ✓ IPTC: {len(meta['keywords'])} keywords")
            print(f"       ✓ Copyright: {COPYRIGHT}")
            processed += 1

        except Exception as e:
            print(f"       ✗ Error: {e}")

        print()

    print("-" * 60)
    print(f"  Done! {processed}/{len(photos)} photos cleaned and tagged.")
    print()
    print(f"  Your clean photos are in: ready-to-post/")
    print()
    print("  WHAT WAS REMOVED:")
    print("    ✗ All Google/Pixel device info")
    print("    ✗ All Gemini/AI processing markers")
    print("    ✗ All software/app traces")
    print("    ✗ All GPS/location data")
    print("    ✗ All XMP metadata")
    print()
    print("  WHAT WAS ADDED:")
    print(f"    ✓ Copyright: {COPYRIGHT}")
    print(f"    ✓ Artist: {ARTIST}")
    print("    ✓ SEO descriptions for Google Image Search")
    print("    ✓ IPTC keywords for platform indexing")
    print("    ✓ SEO-optimized filenames")
    print()
    print("  Upload the files from ready-to-post/ — not the originals.")
    print("=" * 60)


if __name__ == "__main__":
    main()
