# Tool (function) calling: the model asks for a function, your code runs it and
# sends the result back, and the model answers with it. Works with every chat
# model whose page lists tool calling.
import json
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("OCEANTOKEN_BASE_URL", "https://api.oceantoken.ai/v1"),
    api_key=os.environ["OCEANTOKEN_API_KEY"],
)

MODEL = os.getenv("MODEL", "openai/gpt-5-mini")


def get_weather(city: str) -> dict:
    # Your own code runs here: a database, an internal API, anything.
    return {"city": city, "temperature_c": 18, "sky": "cloudy"}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "The current weather in a city.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "description": "City name, for example Lisbon"}},
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What is the weather in Lisbon right now?"}]
message = client.chat.completions.create(model=MODEL, messages=messages, tools=tools).choices[0].message
called = False

# While the model asks for tools, run each one and send the results back.
while message.tool_calls:
    called = True
    messages.append(
        {
            "role": "assistant",
            "content": message.content,
            "tool_calls": [call.model_dump() for call in message.tool_calls],
        }
    )
    for call in message.tool_calls:
        result = get_weather(**json.loads(call.function.arguments))
        messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})
    message = client.chat.completions.create(model=MODEL, messages=messages, tools=tools).choices[0].message

if not called:
    raise SystemExit("the model answered without calling the tool")
print(message.content)
