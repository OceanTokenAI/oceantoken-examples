# Video generation is a job: create it, poll until it is done, download the MP4.
# Every video model works through the same three calls:
#   POST /v1/videos            -> job id, status "queued"
#   GET  /v1/videos/{id}       -> status; "completed" or "failed"
#   GET  /v1/videos/{id}/content -> the MP4 file
import os
import time
import uuid

import requests

BASE = os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1")
HEADERS = {"Authorization": f"Bearer {os.environ['OCEANTOKEN_API_KEY']}"}

# The cheapest Seedance model at its lowest resolution keeps a test run cheap.
MODEL = os.getenv("MODEL", "bytedance/seedance-2.0-mini")

job = requests.post(
    f"{BASE}/videos",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},
    json={
        "model": MODEL,
        "prompt": "A paper boat drifting down a rain gutter, close up, soft light",
        "seconds": "4",
        "resolution": "480p",
    },
    timeout=60,
)
if not job.ok:
    # The error body says why, for example insufficient_credits or invalid_request.
    raise SystemExit(f"{job.status_code}: {job.text}")
video_id = job.json()["id"]
dropped = job.headers.get("x-oceantoken-dropped-params")
print("submitted", video_id, f"(dropped: {dropped})" if dropped else "")

while True:
    status = requests.get(f"{BASE}/videos/{video_id}", headers=HEADERS, timeout=60).json()
    if status["status"] not in ("queued", "in_progress"):
        break
    print("  ", status["status"])
    time.sleep(15)

if status["status"] != "completed":
    raise SystemExit(f"video failed: {status.get('error')}")

content = requests.get(f"{BASE}/videos/{video_id}/content", headers=HEADERS, timeout=300)
content.raise_for_status()
with open(f"{video_id}.mp4", "wb") as f:
    f.write(content.content)
print("saved", f"{video_id}.mp4", len(content.content), "bytes")
