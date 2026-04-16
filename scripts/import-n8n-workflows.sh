#!/bin/bash
# Tribal Cowboy — n8n Workflow Importer
# Run this from the tribal-cowboy-webhook directory on your Mac.
# It imports all 9 workflows into n8n.cloud and activates them.

N8N_API_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkODhkYjUxMS0xZThkLTQ2NjctOTI3ZC1kMzdhMDc3M2Y5MzkiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiMWFkZGQ0MTctYmE4Yi00YWU0LTg2NTQtZjcyYjY4MjZhYTYxIiwiaWF0IjoxNzc2MzgxMTE5fQ.IMZRd_my04VRJfL6Bt8BSxYt_xNxr81-IgYIS_OmRwQ"
N8N_BASE_URL="https://stacieh.app.n8n.cloud/api/v1"
WORKFLOWS_DIR="$(dirname "$0")/../n8n-workflows"

WORKFLOWS=(
  "01-social.json"
  "02-get-paid.json"
  "03-council.json"
  "04-booking-closer.json"
  "05-email-writer.json"
  "06-brand-design.json"
  "07-community.json"
  "08-brand-voice.json"
  "09-daily-brief.json"
)

echo "========================================"
echo "  Tribal Cowboy — n8n Workflow Importer"
echo "========================================"
echo ""

# First, get list of existing workflows to avoid duplicates
echo "Checking existing workflows..."
EXISTING=$(curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_BASE_URL/workflows?limit=50")

if echo "$EXISTING" | grep -q "Host not in allowlist"; then
  echo "ERROR: Your n8n instance is blocking requests from this machine."
  echo "Check your n8n Cloud settings or try from a different network."
  exit 1
fi

if echo "$EXISTING" | grep -q "Unauthorized"; then
  echo "ERROR: Invalid API key. Update N8N_API_KEY in this script."
  exit 1
fi

echo "Connected to n8n successfully."
echo ""

# Track results
IMPORTED=()
UPDATED=()
FAILED=()

for FILE in "${WORKFLOWS[@]}"; do
  FILEPATH="$WORKFLOWS_DIR/$FILE"

  if [ ! -f "$FILEPATH" ]; then
    echo "SKIP: $FILE not found"
    FAILED+=("$FILE (not found)")
    continue
  fi

  WORKFLOW_NAME=$(python3 -c "import json,sys; print(json.load(open('$FILEPATH'))['name'])" 2>/dev/null)
  echo "Processing: $WORKFLOW_NAME ($FILE)..."

  # Check if workflow with this name already exists
  EXISTING_ID=$(echo "$EXISTING" | python3 -c "
import json, sys
data = json.load(sys.stdin)
workflows = data.get('data', [])
name = '$WORKFLOW_NAME'
match = next((w for w in workflows if w.get('name') == name), None)
print(match['id'] if match else '')
" 2>/dev/null)

  # Build the payload — n8n API expects nodes, connections, settings, name
  PAYLOAD=$(python3 -c "
import json, sys
with open('$FILEPATH') as f:
    wf = json.load(f)
# n8n API create/update payload
out = {
    'name': wf.get('name', ''),
    'nodes': wf.get('nodes', []),
    'connections': wf.get('connections', {}),
    'settings': wf.get('settings', {}),
    'staticData': wf.get('staticData', None)
}
print(json.dumps(out))
" 2>/dev/null)

  if [ -z "$PAYLOAD" ]; then
    echo "  ERROR: Could not parse $FILE"
    FAILED+=("$FILE (parse error)")
    continue
  fi

  if [ -n "$EXISTING_ID" ]; then
    # Update existing workflow
    RESPONSE=$(curl -s -w "\n%{http_code}" \
      -X PUT "$N8N_BASE_URL/workflows/$EXISTING_ID" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d "$PAYLOAD")
    HTTP_CODE=$(echo "$RESPONSE" | tail -1)

    if [ "$HTTP_CODE" = "200" ]; then
      echo "  Updated (id: $EXISTING_ID)"
      UPDATED+=("$WORKFLOW_NAME")

      # Activate it
      curl -s -X PATCH "$N8N_BASE_URL/workflows/$EXISTING_ID" \
        -H "X-N8N-API-KEY: $N8N_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"active": true}' > /dev/null
      echo "  Activated"
    else
      echo "  ERROR updating (HTTP $HTTP_CODE)"
      FAILED+=("$WORKFLOW_NAME (update failed $HTTP_CODE)")
    fi
  else
    # Create new workflow
    RESPONSE=$(curl -s -w "\n%{http_code}" \
      -X POST "$N8N_BASE_URL/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d "$PAYLOAD")
    HTTP_CODE=$(echo "$RESPONSE" | tail -1)
    BODY=$(echo "$RESPONSE" | head -n -1)

    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
      NEW_ID=$(echo "$BODY" | python3 -c "import json,sys; print(json.load(sys.stdin).get('id',''))" 2>/dev/null)
      echo "  Created (id: $NEW_ID)"
      IMPORTED+=("$WORKFLOW_NAME")

      # Activate it
      if [ -n "$NEW_ID" ]; then
        curl -s -X PATCH "$N8N_BASE_URL/workflows/$NEW_ID" \
          -H "X-N8N-API-KEY: $N8N_API_KEY" \
          -H "Content-Type: application/json" \
          -d '{"active": true}' > /dev/null
        echo "  Activated"
      fi
    else
      echo "  ERROR creating (HTTP $HTTP_CODE)"
      echo "  Response: $(echo "$BODY" | head -c 200)"
      FAILED+=("$WORKFLOW_NAME (create failed $HTTP_CODE)")
    fi
  fi

  echo ""
done

echo "========================================"
echo "  RESULTS"
echo "========================================"
echo ""
echo "Imported (${#IMPORTED[@]}):"
for w in "${IMPORTED[@]}"; do echo "  ✓ $w"; done

echo ""
echo "Updated (${#UPDATED[@]}):"
for w in "${UPDATED[@]}"; do echo "  ↺ $w"; done

echo ""
if [ ${#FAILED[@]} -gt 0 ]; then
  echo "Failed (${#FAILED[@]}):"
  for w in "${FAILED[@]}"; do echo "  ✗ $w"; done
  echo ""
fi

echo "========================================"
echo "  NEXT STEPS (required in browser)"
echo "========================================"
echo ""
echo "Workflows that use Gmail need credentials connected:"
echo "  1. Go to: https://stacieh.app.n8n.cloud"
echo "  2. Credentials → New → Gmail OAuth2"
echo "  3. Sign in as info@tribalcowboy.com"
echo "  4. Open each workflow → click Gmail node → select the credential"
echo ""
echo "Social workflow needs Google Sheets credential:"
echo "  1. Credentials → New → Google Sheets OAuth2"
echo "  2. Open '01-social' → click Google Sheets node → select it"
echo ""
echo "Anthropic credential (if not already set):"
echo "  1. Credentials → New → Anthropic"
echo "  2. Paste your Anthropic API key"
echo "  3. Open each workflow → Anthropic Chat Model node → select it"
echo ""
echo "Done! Form URLs after activation:"
echo "  Get Paid:     https://stacieh.app.n8n.cloud/form/tribal-cowboy-get-paid"
echo "  Council:      https://stacieh.app.n8n.cloud/form/tribal-cowboy-council"
echo "  Email Writer: https://stacieh.app.n8n.cloud/form/tribal-cowboy-email"
echo "  Brand Design: https://stacieh.app.n8n.cloud/form/tribal-cowboy-design"
echo "  Community:    https://stacieh.app.n8n.cloud/form/tribal-cowboy-community"
echo "  Brand Voice:  https://stacieh.app.n8n.cloud/form/tribal-cowboy-brand-voice"
