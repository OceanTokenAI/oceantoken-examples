#!/usr/bin/env bash
# Chat completion with curl. Needs OCEANTOKEN_API_KEY in the environment.
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-deepseek/deepseek-v4.1-flash}"

curl -sS --fail-with-body "$BASE/chat/completions" \
  -H "Authorization: Bearer $OCEANTOKEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"messages\": [{\"role\": \"user\", \"content\": \"Say hello in one short sentence.\"}]
  }"
echo
