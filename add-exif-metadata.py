#!/usr/bin/env python3
"""
Tribal Cowboy — EXIF & IPTC Metadata Writer
=============================================
Writes SEO-optimized metadata into your photos so Google, Instagram,
Facebook, and other platforms can properly index and understand them.

USAGE:
1. Put your 5 photos in the same folder as this script
2. Rename them to match the filenames below (or update the filenames in the script)
3. Run: python3 add-exif-metadata.py
4. New files with metadata will be saved in a "tagged/" subfolder

The script writes:
- EXIF: Copyright, Artist, ImageDescription, UserComment
- IPTC: Title, Caption, Keywords, Copyright, Byline, City, State, Country
- Filename: SEO-optimized (rename your originals to match)
"""

import os
import sys
import struct
import piexif
from PIL import Image
from datetime import datetime

# ─── Configuration ───────────────────────────────────────────────────────────

BUSINESS = "Tribal Cowboy LLC"
ARTIST = "Tribal Cowboy LLC"
COPYRIGHT = f"© {datetime.now().year} Tribal Cowboy LLC. All rights reserved."
WEBSITE = "www.tribalcowboy.com"
CITY = "Athol"
STATE = "Idaho"
COUNTRY = "United States"

# ─── Photo Metadata Definitions ─────────────────────────────────────────────

PHOTOS = [
    {
        "input_filename": "cowgirl-cat-green-grass.jpg",
        "output_filename": "cowgirl-barn-cat-north-idaho-tribal-cowboy.jpg",
        "title": "Young Cowgirl and Barn Cat at Tribal Cowboy Ranch",
        "description": (
            "A young cowgirl in a straw hat and western tee stands on green grass "
            "with a black-and-white tuxedo barn cat weaving between her boots. "
            "Pine trees and black ranch fencing in the background. Golden hour light "
            "at Tribal Cowboy ranch in Athol, Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "cowgirl", "barn cat", "ranch life",
            "western lifestyle", "Athol Idaho", "horse ranch", "country kids",
            "golden hour photography", "farm cat", "Idaho ranch",
            "Indigenous owned business", "equine experience"
        ],
    },
    {
        "input_filename": "cowgirl-pony-native-blanket.jpg",
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
    {
        "input_filename": "cowgirl-wild-west-blanket-cat.jpg",
        "output_filename": "cowgirl-wild-west-tee-native-blanket-barn-cat-tribal-cowboy.jpg",
        "title": "Cowgirl Relaxing on Native Blanket with Barn Cat",
        "description": (
            "A smiling young cowgirl in a Wild West graphic tee and straw cowboy hat "
            "lounges on a Native geometric pattern blanket on the grass. A black tuxedo "
            "barn cat curls up beside her. Golden hour sunlight at Tribal Cowboy ranch "
            "in Athol, Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "cowgirl", "barn cat", "Native blanket",
            "Wild West", "ranch life", "golden hour", "Athol Idaho",
            "western kids", "country lifestyle", "farm life", "Idaho ranch",
            "Indigenous owned business", "equine experience"
        ],
    },
    {
        "input_filename": "cowgirl-blanket-sunset-portrait.jpg",
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
    {
        "input_filename": "cowgirl-hugging-mini-horse.jpg",
        "output_filename": "cowgirl-hugging-miniature-horse-tribal-cowboy-north-idaho.jpg",
        "title": "Cowgirl Hugging Miniature Horse at Tribal Cowboy Ranch",
        "description": (
            "A young cowgirl in a straw hat drapes herself over a gray miniature horse, "
            "hugging its neck with both arms. The mini horse stands by a black ranch "
            "fence at golden hour. Pine trees and Idaho sky in the background. "
            "Tribal Cowboy ranch in Athol, Idaho."
        ),
        "keywords": [
            "Tribal Cowboy", "North Idaho", "miniature horse", "mini horse",
            "cowgirl", "horse hug", "ranch life", "Athol Idaho",
            "pony love", "equine experience", "western lifestyle",
            "Indigenous owned", "horse photography", "golden hour",
            "kids and horses", "North Idaho horses"
        ],
    },
]

# ─── Helper Functions ────────────────────────────────────────────────────────

def encode_utf16(text):
    """Encode text as UTF-16 for EXIF UserComment field."""
    return b"UNICODE\x00" + text.encode("utf-16-le")


def build_iptc_block(title, description, keywords, artist, copyright_text, city, state, country):
    """
    Build a raw IPTC-IIM block (stored inside Photoshop 8BIM in the APP13 marker).
    This is what Google, Facebook, and stock photo sites read for keywords and captions.
    """
    def iptc_tag(record, dataset, value):
        """Create a single IPTC tag entry."""
        if isinstance(value, str):
            value = value.encode("utf-8")
        length = len(value)
        if length < 32768:
            return struct.pack("!BBBh", 0x1C, record, dataset, length) + value
        else:
            return struct.pack("!BBBi", 0x1C, record, dataset, length) + value

    blocks = []
    # 2:05 - Object Name (Title)
    blocks.append(iptc_tag(2, 5, title))
    # 2:120 - Caption/Abstract
    blocks.append(iptc_tag(2, 120, description))
    # 2:25 - Keywords (one tag per keyword)
    for kw in keywords:
        blocks.append(iptc_tag(2, 25, kw))
    # 2:116 - Copyright Notice
    blocks.append(iptc_tag(2, 116, copyright_text))
    # 2:80 - By-line (photographer/artist)
    blocks.append(iptc_tag(2, 80, artist))
    # 2:90 - City
    blocks.append(iptc_tag(2, 90, city))
    # 2:95 - Province/State
    blocks.append(iptc_tag(2, 95, state))
    # 2:101 - Country
    blocks.append(iptc_tag(2, 101, country))

    return b"".join(blocks)


def build_photoshop_app13(iptc_data):
    """Wrap IPTC data in a Photoshop 3.0 / 8BIM APP13 segment."""
    # 8BIM marker + resource type 0x0404 (IPTC-NAA)
    header = b"Photoshop 3.0\x00"
    resource_type = b"8BIM"
    resource_id = struct.pack("!H", 0x0404)
    pascal_string = b"\x00\x00"  # empty pascal string
    data_length = struct.pack("!I", len(iptc_data))
    block = resource_type + resource_id + pascal_string + data_length + iptc_data
    # Pad to even length
    if len(block) % 2 != 0:
        block += b"\x00"
    return header + block


def write_metadata(input_path, output_path, photo_meta):
    """Write EXIF and IPTC metadata to a JPEG file."""

    # Open the image
    img = Image.open(input_path)

    # ── Build EXIF data ──────────────────────────────────────────────────
    # Start fresh or load existing
    try:
        exif_dict = piexif.load(img.info.get("exif", b""))
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "Interop": {}}

    # 0th IFD (basic image info)
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = photo_meta["description"].encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Artist] = ARTIST.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Copyright] = COPYRIGHT.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.Software] = "Tribal Cowboy Media".encode("utf-8")

    # Exif IFD
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = encode_utf16(
        f"{photo_meta['title']} | {photo_meta['description']} | "
        f"Keywords: {', '.join(photo_meta['keywords'])} | {WEBSITE}"
    )

    # Generate EXIF bytes
    exif_bytes = piexif.dump(exif_dict)

    # ── Build IPTC data ──────────────────────────────────────────────────
    iptc_data = build_iptc_block(
        title=photo_meta["title"],
        description=photo_meta["description"],
        keywords=photo_meta["keywords"],
        artist=ARTIST,
        copyright_text=COPYRIGHT,
        city=CITY,
        state=STATE,
        country=COUNTRY,
    )
    app13_data = build_photoshop_app13(iptc_data)

    # ── Save with metadata ───────────────────────────────────────────────
    # Save with EXIF first
    img.save(output_path, "JPEG", quality=95, exif=exif_bytes)

    # Now inject IPTC APP13 segment into the saved file
    inject_app13(output_path, app13_data)

    print(f"  ✓ {os.path.basename(output_path)}")
    print(f"    Title: {photo_meta['title']}")
    print(f"    Keywords: {len(photo_meta['keywords'])} tags")
    print(f"    Copyright: {COPYRIGHT}")
    print()


def inject_app13(filepath, app13_data):
    """Inject an APP13 (IPTC) segment into an existing JPEG file."""
    with open(filepath, "rb") as f:
        data = f.read()

    # Find the position after the SOI marker (first 2 bytes: FF D8)
    if data[:2] != b"\xff\xd8":
        print(f"    ⚠ Not a valid JPEG, skipping IPTC injection")
        return

    # Build APP13 marker segment
    marker = b"\xff\xed"
    length = struct.pack("!H", len(app13_data) + 2)
    app13_segment = marker + length + app13_data

    # Insert after SOI (position 2)
    new_data = data[:2] + app13_segment + data[2:]

    with open(filepath, "wb") as f:
        f.write(new_data)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "tagged")
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 60)
    print("  TRIBAL COWBOY — Photo Metadata Writer")
    print("=" * 60)
    print()
    print(f"  Looking for photos in: {script_dir}")
    print(f"  Saving tagged photos to: {output_dir}")
    print()

    found = 0
    missing = []

    for photo in PHOTOS:
        input_path = os.path.join(script_dir, photo["input_filename"])
        output_path = os.path.join(output_dir, photo["output_filename"])

        if os.path.exists(input_path):
            found += 1
            print(f"  Processing: {photo['input_filename']}")
            try:
                write_metadata(input_path, output_path, photo)
            except Exception as e:
                print(f"    ✗ Error: {e}")
                print()
        else:
            missing.append(photo["input_filename"])

    print("-" * 60)
    print(f"  Done! {found} photos tagged.")

    if missing:
        print()
        print("  Missing files (rename your photos to match):")
        for m in missing:
            print(f"    - {m}")

    print()
    print("  Your tagged photos are in the 'tagged/' folder.")
    print("  Upload THOSE files (not the originals) to get")
    print("  the SEO benefits on Google, Instagram, and Facebook.")
    print("=" * 60)


if __name__ == "__main__":
    main()
