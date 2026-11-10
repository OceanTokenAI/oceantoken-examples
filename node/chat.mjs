// Chat completion. Any chat model id from https://oceantoken.ai/models works; only `model` changes.
import { client } from "./client.mjs";

const model = process.env.MODEL ?? "deepseek/deepseek-v4.1-flash";

const response = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: "Say hello in one short sentence." }],
});
console.log(response.choices[0].message.content);
console.log("tokens:", response.usage.prompt_tokens, "in /", response.usage.completion_tokens, "out");
