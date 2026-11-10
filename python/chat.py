# Chat completion with the official OpenAI Python SDK.
#   pip install -r requirements.txt
#   export OCEANTOKEN_API_KEY=...   (create one at https://app.oceantoken.ai)
#   python chat.py
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

# Any chat model id from https://oceantoken.ai/models works here; only `model` changes.
MODEL = os.getenv("MODEL", "deepseek/deepseek-v4.1-flash")

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)
print(response.choices[0].message.content)
print("tokens:", response.usage.prompt_tokens, "in /", response.usage.completion_tokens, "out")
