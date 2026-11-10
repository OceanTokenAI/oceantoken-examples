// Video is a job: create, poll, download. Uses fetch (built into Node 18+), no SDK needed.
import { randomUUID } from "node:crypto";
import { writeFile } from "node:fs/promises";
import { BASE_URL } from "./client.mjs";

const headers = { Authorization: `Bearer ${process.env.OCEANTOKEN_API_KEY}` };
const model = process.env.MODEL ?? "bytedance/seedance-2.0-mini";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const create = await fetch(`${BASE_URL}/videos`, {
  method: "POST",
  headers: { ...headers, "Content-Type": "application/json", "Idempotency-Key": randomUUID() },
  body: JSON.stringify({
    model,
    prompt: "A paper boat drifting down a rain gutter, close up, soft light",
    seconds: "4",
    resolution: "480p",
  }),
});
if (!create.ok) {
  console.error(create.status, await create.text());
  process.exit(1);
}
const { id } = await create.json();
console.log("submitted", id);

let job;
for (;;) {
  job = await (await fetch(`${BASE_URL}/videos/${id}`, { headers })).json();
  if (!["queued", "in_progress"].includes(job.status)) break;
  console.log("  ", job.status);
  await sleep(15000);
}
if (job.status !== "completed") {
  console.error("video failed:", job.error);
  process.exit(1);
}

const file = await fetch(`${BASE_URL}/videos/${id}/content`, { headers });
if (!file.ok) throw new Error(`download failed: ${file.status}`);
const bytes = Buffer.from(await file.arrayBuffer());
await writeFile(`${id}.mp4`, bytes);
console.log("saved", `${id}.mp4`, bytes.length, "bytes");
