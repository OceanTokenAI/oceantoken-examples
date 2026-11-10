# Streaming: tokens arrive as they are generated. Use it for anything a person
# waits on, and for long answers (a non-streamed request is closed after 240 s).
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

MODEL = os.getenv("MODEL", "deepseek/deepseek-v4.1-flash")

finish_reason = None
with client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Count from one to five, one number per line."}],
    stream=True,
) as stream:
    for chunk in stream:
        if not chunk.choices:
            continue
        choice = chunk.choices[0]
        if choice.delta.content:
            print(choice.delta.content, end="", flush=True)
        finish_reason = choice.finish_reason or finish_reason
print()

# A stream that ends without a finish reason is incomplete: retry it.
if finish_reason is None:
    raise SystemExit("stream ended without a finish_reason")
