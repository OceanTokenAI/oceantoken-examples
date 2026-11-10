# Your own backup models. The gateway already retries and fails over between
# channels of the SAME model. `fallbacks` names OTHER models to try if the one
# you asked for fails on every channel. It is not in the OpenAI SDK's signature,
# so it travels in extra_body.
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

raw = client.chat.completions.with_raw_response.create(
    model="openai/gpt-5-mini",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
    extra_body={"fallbacks": ["anthropic/claude-haiku-4.5", "deepseek/deepseek-v4.1-flash"]},
)
response = raw.parse()
# You are billed at the price of the model that answered; both of these name it.
print("answered by:", response.model, "| header:", raw.headers.get("x-oceantoken-model"))
print("request id:", raw.headers.get("x-oceantoken-request-id"))
print(response.choices[0].message.content)
