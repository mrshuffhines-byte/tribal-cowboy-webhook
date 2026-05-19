# Tribal Cowboy — Remotion Reels

Programmatic video compositions for Tribal Cowboy LLC, built with [Remotion](https://www.remotion.dev/).

## Compositions

| ID | Description | Spec |
|---|---|---|
| `PonyPostReel` | The Pony Post — 30s vertical Instagram Reel introducing the 4-week classroom reading sprint | 1080×1920, 30fps, 30s |

## Setup

```bash
cd remotion
npm install
```

## Preview in browser

```bash
npm start
```

Opens Remotion Studio at http://localhost:3000 — scrub the timeline, tweak code, hot-reload.

## Render to MP4 (Instagram-ready)

```bash
npm run build
```

Output: `remotion/out/pony-post-reel.mp4`

The file is a 1080×1920 H.264 MP4 — drop it straight into Instagram, TikTok, or Facebook Reels.

## Render to GIF (for previews)

```bash
npm run build:gif
```

## Story outline — PonyPostReel

| Frames | Time | Scene | Beat |
|---|---|---|---|
| 0–90 | 0–3s | Hook | "Imagine a pony writes your class a letter." |
| 90–240 | 3–8s | Title | THE PONY POST · "Where the pony writes back." |
| 240–420 | 8–14s | Letters | 4 visits · 3 real letters · hand-folded, hoof-stamped |
| 420–600 | 14–20s | SyllablePaw | She paws out syllables — Ap·pa·loo·sa |
| 600–780 | 20–26s | AbbyReveal | Pony shrinks. Abby (1,800-lb Clydesdale) arrives. |
| 780–900 | 26–30s | CTA | Free to schools. tribalcowboy.com |

## Editing notes

- **Theme tokens** live in `src/theme.ts` — colors, fonts, video dimensions
- **Scenes** are in `src/scenes/` — one component per beat
- **Sequencing** happens in `src/PonyPostReel.tsx`
- Brand fonts (Playfair Display + Lato) load via `@remotion/google-fonts`

To swap a scene, edit the matching file in `src/scenes/`. To add a new composition (e.g. a square Facebook version), register it in `src/Root.tsx`.

## Render with audio

Drop an audio file in `remotion/public/` and reference it in a scene with `<Audio src={staticFile("filename.mp3")} />`. Suggested sources for the Pony Post Reel:
- Light upright piano or acoustic guitar bed (~30s)
- One real "clip-clop" hoof sound layered on each syllable beat in `SyllablePaw`
