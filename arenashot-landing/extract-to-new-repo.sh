#!/usr/bin/env bash
# Extract arenashot-landing/ to a standalone repo.
# Usage: ./extract-to-new-repo.sh [target-path]
#   target-path defaults to ../arenashot
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-${SOURCE_DIR}/../arenashot}"

if [ -e "$TARGET" ]; then
  echo "Target $TARGET already exists. Aborting."
  exit 1
fi

echo "Extracting $SOURCE_DIR → $TARGET"
mkdir -p "$TARGET"
cp -R "$SOURCE_DIR/." "$TARGET/"
# Don't carry over the extraction script itself into the new repo
rm -f "$TARGET/extract-to-new-repo.sh"

cd "$TARGET"
git init -q
git add .
git commit -q -m "Initial commit — ArenaShot landing + waitlist"

cat <<EOF

Done. Next steps:

  cd $TARGET
  gh repo create arenashot --private --source=. --remote=origin --push

Then deploy to Render:
  - New Web Service → connect the arenashot repo
  - Build: npm install
  - Start: npm start
  - Add env vars from .env.example (optional Twilio for SMS notifications)

Buy the domain:
  - arenashot.com   (check Namecheap / Cloudflare Registrar)
  - Point CNAME to your Render URL

EOF
