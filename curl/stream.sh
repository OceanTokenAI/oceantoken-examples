#!/usr/bin/env bash
# Streaming with curl: Server-Sent Events, one "data: {...}" line per chunk, ending with "data: [DONE]".
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-deepseek/deepseek-v4.1-flash}"

curl -sS -N --fail-with-body "$BASE/chat/completions" \
  -H "Authorization: Bearer $OCEANTOKEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"stream\": true,
    \"messages\": [{\"role\": \"user\", \"content\": \"Count from one to five, one number per line.\"}]
  }"
