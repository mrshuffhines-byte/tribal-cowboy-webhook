# Tribal Cowboy — Photo Metadata Guide

## What This Does

When you upload a photo to Instagram, Facebook, Google (via your website), or anywhere else, the platform reads hidden data baked into the file. This is called **EXIF** and **IPTC** metadata. It tells them:

- **Who owns the photo** (copyright)
- **What's in the photo** (description, title)
- **What keywords apply** (so Google can index it)
- **Where it was taken** (city, state)

If your photos have no metadata, platforms treat them as generic unnamed images. If they're tagged properly, Google can surface them in image search, and platforms index them correctly.

---

## How to Use the Script

### Step 1: Rename Your Photos

Put the 5 photos into your `TribalCowboy-Social` folder with these filenames:

| Photo | Rename To |
|-------|-----------|
| Girl + cat on grass | `cowgirl-cat-green-grass.jpg` |
| Girl + pony + Native blanket by fence | `cowgirl-pony-native-blanket.jpg` |
| Girl on blanket + cat, Wild West tee | `cowgirl-wild-west-blanket-cat.jpg` |
| Girl wrapped in blanket, sunset | `cowgirl-blanket-sunset-portrait.jpg` |
| Girl hugging mini horse | `cowgirl-hugging-mini-horse.jpg` |

### Step 2: Run the Script

Open Terminal and run:
```
cd ~/path/to/TribalCowboy-Social
python3 add-exif-metadata.py
```

### Step 3: Use the Tagged Photos

Your new photos will be in the `tagged/` folder with SEO-optimized filenames like:
- `cowgirl-barn-cat-north-idaho-tribal-cowboy.jpg`
- `cowgirl-hugging-miniature-horse-tribal-cowboy-north-idaho.jpg`

Upload THESE files instead of the originals.

---

## What Gets Written Into Each Photo

### Photo 1: Cowgirl + Barn Cat on Green Grass
- **Output filename:** `cowgirl-barn-cat-north-idaho-tribal-cowboy.jpg`
- **Title:** Young Cowgirl and Barn Cat at Tribal Cowboy Ranch
- **Description:** A young cowgirl in a straw hat and western tee stands on green grass with a black-and-white tuxedo barn cat weaving between her boots. Pine trees and black ranch fencing in the background. Golden hour light at Tribal Cowboy ranch in Athol, Idaho.
- **Keywords:** Tribal Cowboy, North Idaho, cowgirl, barn cat, ranch life, western lifestyle, Athol Idaho, horse ranch, country kids, golden hour photography, farm cat, Idaho ranch, Indigenous owned business, equine experience

### Photo 2: Cowgirl + Pony + Native Blanket
- **Output filename:** `cowgirl-pony-native-blanket-golden-hour-tribal-cowboy.jpg`
- **Title:** Cowgirl with Pony and Native Pattern Blanket at Golden Hour
- **Description:** A young girl in a cowboy hat draped in a Native pattern blanket leans close to a gray pony by a black fence at golden hour. Warm sunset light catches the geometric pattern of the blanket. Shot at Tribal Cowboy ranch in Athol, North Idaho.
- **Keywords:** Tribal Cowboy, North Idaho, pony, Native pattern blanket, golden hour, cowgirl, western lifestyle, Athol Idaho, horse ranch, Indigenous owned, equine photography, miniature horse, ranch kids, country life

### Photo 3: Wild West Tee + Blanket + Cat
- **Output filename:** `cowgirl-wild-west-tee-native-blanket-barn-cat-tribal-cowboy.jpg`
- **Title:** Cowgirl Relaxing on Native Blanket with Barn Cat
- **Description:** A smiling young cowgirl in a Wild West graphic tee and straw cowboy hat lounges on a Native geometric pattern blanket on the grass. A black tuxedo barn cat curls up beside her. Golden hour sunlight at Tribal Cowboy ranch in Athol, Idaho.
- **Keywords:** Tribal Cowboy, North Idaho, cowgirl, barn cat, Native blanket, Wild West, ranch life, golden hour, Athol Idaho, western kids, country lifestyle, farm life, Idaho ranch, Indigenous owned business, equine experience

### Photo 4: Blanket Sunset Portrait
- **Output filename:** `cowgirl-native-blanket-sunset-portrait-north-idaho-tribal-cowboy.jpg`
- **Title:** Cowgirl Wrapped in Native Blanket at Sunset in North Idaho
- **Description:** A young girl in a cowboy hat wrapped in a Native geometric pattern blanket gazes into the distance as golden sunset light backlights her hair. Ranch fencing and pine trees in the background. Portrait taken at Tribal Cowboy ranch in Athol, North Idaho.
- **Keywords:** Tribal Cowboy, North Idaho, cowgirl portrait, Native blanket, sunset photography, golden hour, ranch portrait, Athol Idaho, western lifestyle, country girl, Idaho sunset, Indigenous owned, equine experience, ranch life

### Photo 5: Hugging Mini Horse
- **Output filename:** `cowgirl-hugging-miniature-horse-tribal-cowboy-north-idaho.jpg`
- **Title:** Cowgirl Hugging Miniature Horse at Tribal Cowboy Ranch
- **Description:** A young cowgirl in a straw hat drapes herself over a gray miniature horse, hugging its neck with both arms. The mini horse stands by a black ranch fence at golden hour. Pine trees and Idaho sky in the background. Tribal Cowboy ranch in Athol, Idaho.
- **Keywords:** Tribal Cowboy, North Idaho, miniature horse, mini horse, cowgirl, horse hug, ranch life, Athol Idaho, pony love, equine experience, western lifestyle, Indigenous owned, horse photography, golden hour, kids and horses, North Idaho horses

---

## What Each Platform Does With This Data

**Google (website/SEO):** Reads the filename, IPTC keywords, title, and description. This is how your photos show up in Google Image Search for "North Idaho horse photography" or "Tribal Cowboy pony party."

**Instagram:** Strips most EXIF on upload BUT reads it first for content classification. The real win is using the SEO filename and description as your alt text when posting.

**Facebook:** Reads IPTC data including keywords and copyright. Helps with content discovery and protects your ownership.

**Squarespace/Website:** Uses the filename for the image URL slug. `cowgirl-barn-cat-north-idaho-tribal-cowboy.jpg` is infinitely better than `IMG_4582.jpg` for SEO.

---

## Alt Text Cheat Sheet

When you upload these to your website or Instagram, copy-paste the **Description** field as the alt text. That's the single biggest SEO move you can make with photos.
