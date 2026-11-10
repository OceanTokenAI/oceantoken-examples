// Generate an image and save it. The URL in the response works for 24 hours.
import { randomUUID } from "node:crypto";
import { writeFile } from "node:fs/promises";
import { client } from "./client.mjs";

const model = process.env.MODEL ?? "openai/gpt-image-2";

const result = await client.images.generate(
  {
    model,
    prompt: "A small lighthouse on a calm sea at dawn, watercolor",
    size: "1024x1024",
    n: 1,
  },
  // A retry with the same Idempotency-Key returns the first image instead of charging for a second one.
  { headers: { "Idempotency-Key": randomUUID() } },
);

const res = await fetch(result.data[0].url);
if (!res.ok) throw new Error(`download failed: ${res.status}`);
const bytes = Buffer.from(await res.arrayBuffer());
await writeFile("image.png", bytes);
console.log("saved image.png,", bytes.length, "bytes");
