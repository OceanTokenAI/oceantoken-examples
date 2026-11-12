#!/usr/bin/env bash
# What a video model accepts: durations, resolutions, aspect ratios, sound, input modes, reference limits.
set -euo pipefail
BASE="${OCEANTOKEN_BASE_URL:-https://api.oceantoken.ai/v1}"
MODEL="${MODEL:-bytedance/seedance-2.5}"
curl -sS --fail-with-body "${BASE%/v1}/oceantoken/video/model-spec?model=$MODEL" \
  -H "Authorization: Bearer $OCEANTOKEN_API_KEY" | jq .
