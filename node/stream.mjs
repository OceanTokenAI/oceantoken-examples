// Streaming: print tokens as they arrive.
import { client } from "./client.mjs";

const model = process.env.MODEL ?? "deepseek/deepseek-v4.1-flash";

const stream = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: "Count from one to five, one number per line." }],
  stream: true,
});

let finishReason = null;
for await (const chunk of stream) {
  const choice = chunk.choices?.[0];
  if (!choice) continue;
  if (choice.delta?.content) process.stdout.write(choice.delta.content);
  finishReason = choice.finish_reason ?? finishReason;
}
process.stdout.write("\n");

// A stream that ends without a finish reason is incomplete: retry it.
if (!finishReason) {
  console.error("stream ended without a finish_reason");
  process.exit(1);
}
