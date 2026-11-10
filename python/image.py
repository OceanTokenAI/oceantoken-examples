# Generate an image with the OpenAI SDK's Images API and save it.
# The response carries a URL that works for 24 hours, so download it right away.
import os
import uuid

import requests
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

MODEL = os.getenv("MODEL", "openai/gpt-image-2")

result = client.images.generate(
    model=MODEL,
    prompt="A small lighthouse on a calm sea at dawn, watercolor",
    size="1024x1024",
    n=1,
    # A retry with the same Idempotency-Key returns the first image instead of
    # making (and charging for) a second one.
    extra_headers={"Idempotency-Key": str(uuid.uuid4())},
)

url = result.data[0].url
image = requests.get(url, timeout=120)
image.raise_for_status()
with open("image.png", "wb") as f:
    f.write(image.content)
print("saved image.png,", len(image.content), "bytes")
