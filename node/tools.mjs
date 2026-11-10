// Tool (function) calling: the model asks for a function, we run it and send the result back.
import { client } from "./client.mjs";

const model = process.env.MODEL ?? "openai/gpt-5-mini";

function getWeather({ city }) {
  // Your own code runs here.
  return { city, temperature_c: 18, sky: "cloudy" };
}

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "The current weather in a city.",
      parameters: {
        type: "object",
        properties: { city: { type: "string", description: "City name, for example Lisbon" } },
        required: ["city"],
      },
    },
  },
];

const messages = [{ role: "user", content: "What is the weather in Lisbon right now?" }];
let message = (await client.chat.completions.create({ model, messages, tools })).choices[0].message;
let called = false;

while (message.tool_calls?.length) {
  called = true;
  messages.push({ role: "assistant", content: message.content, tool_calls: message.tool_calls });
  for (const call of message.tool_calls) {
    const result = getWeather(JSON.parse(call.function.arguments));
    messages.push({ role: "tool", tool_call_id: call.id, content: JSON.stringify(result) });
  }
  message = (await client.chat.completions.create({ model, messages, tools })).choices[0].message;
}

if (!called) {
  console.error("the model answered without calling the tool");
  process.exit(1);
}
console.log(message.content);
