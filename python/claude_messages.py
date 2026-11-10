# The Anthropic Messages API, with the official Anthropic SDK.
# The SDK adds /v1 itself, so it takes the host without /v1.
import os

import anthropic

client = anthropic.Anthropic(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1").removesuffix("/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

MODEL = os.getenv("MODEL", "anthropic/claude-haiku-4.5")

message = client.messages.create(
    model=MODEL,
    max_tokens=128,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)
print(message.content[0].text)
