#!/usr/bin/env bash
# Tool calling, first turn: the answer's choices[0].message.tool_calls asks for get_weather.
# Your code would run it and send a {"role":"tool"} message back (see python/tools.py for the full loop).
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-openai/gpt-5-mini}"

curl -sS --fail-with-body "$BASE/chat/completions" \
  -H "Authorization: Bearer $OCEANTOKEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"messages\": [{\"role\": \"user\", \"content\": \"What is the weather in Lisbon right now?\"}],
    \"tools\": [{
      \"type\": \"function\",
      \"function\": {
        \"name\": \"get_weather\",
        \"description\": \"The current weather in a city.\",
        \"parameters\": {
          \"type\": \"object\",
          \"properties\": {\"city\": {\"type\": \"string\"}},
          \"required\": [\"city\"]
        }
      }
    }]
  }"
echo
