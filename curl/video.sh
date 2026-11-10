#!/usr/bin/env bash
# Video job with curl: create, poll, download. Needs jq.
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-bytedance/seedance-2.0-mini}"
AUTH="Authorization: Bearer $OCEANTOKEN_API_KEY"

ID=$(curl -sS --fail-with-body "$BASE/videos" \
  -H "$AUTH" -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen 2>/dev/null || date +%s%N)" \
  -d "{
    \"model\": \"$MODEL\",
    \"prompt\": \"A paper boat drifting down a rain gutter, close up, soft light\",
    \"seconds\": \"4\",
    \"resolution\": \"480p\"
  }" | jq -r .id)
echo "submitted $ID"

while :; do
  JOB=$(curl -sS "$BASE/videos/$ID" -H "$AUTH")
  STATUS=$(echo "$JOB" | jq -r .status)
  case "$STATUS" in
    queued|in_progress) echo "  $STATUS"; sleep 15 ;;
    completed) break ;;
    *) echo "video failed: $(echo "$JOB" | jq -c .error)"; exit 1 ;;
  esac
done

curl -sS --fail-with-body -o "$ID.mp4" "$BASE/videos/$ID/content" -H "$AUTH"
echo "saved $ID.mp4"
