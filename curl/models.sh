#!/usr/bin/env bash
# The models your key can call, and the public catalog with prices (the catalog needs no key).
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"

echo "Models for this key (first 20):"
curl -sS --fail-with-body "$BASE/models" -H "Authorization: Bearer $OCEANTOKEN_API_KEY" | jq -r '.data[].id' | head -20

echo
echo "Public catalog: video models and their lowest price per second (USD):"
curl -sS --fail-with-body https://api.oceantoken.ai/public/model_hub \
  | jq -r '.[] | select(.mode=="video_generation") | "\(.model_group)\t\(.catalog_cost_per_video_second_from)"' | sort
