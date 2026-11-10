// One client for every example. Set OCEANTOKEN_API_KEY in your environment.
import OpenAI from "openai";

if (!process.env.OCEANTOKEN_API_KEY) {
  console.error("Set OCEANTOKEN_API_KEY first (see the README).");
  process.exit(1);
}

export const BASE_URL = process.env.OCEANTOKEN_BASE_URL ?? "https://api.oceantoken.ai/v1";

export const client = new OpenAI({
  baseURL: BASE_URL,
  apiKey: process.env.OCEANTOKEN_API_KEY,
});
