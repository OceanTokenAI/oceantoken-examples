#!/usr/bin/env bash
# Generate an image. data[0].url in the answer works for 24 hours.
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-openai/gpt-image-2}"

curl -sS --fail-with-body "$BASE/images/generations" \
  -H "Authorization: Bearer $OCEANTOKEN_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen 2>/dev/null || date +%s%N)" \
  -d "{
    \"model\": \"$MODEL\",
    \"prompt\": \"A small lighthouse on a calm sea at dawn, watercolor\",
    \"size\": \"1024x1024\",
    \"n\": 1
  }"
echo
