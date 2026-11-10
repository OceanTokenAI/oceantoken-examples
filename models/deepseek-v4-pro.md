# DeepSeek V4 Pro API on OceanToken

Model id: `deepseek/deepseek-v4-pro`. Chat, tool calling, reasoning, 1,048,576-token context. OpenAI-compatible (`/v1/chat/completions`, `/v1/responses`) and Anthropic Messages (`/v1/messages`).

## Price (USD per million tokens, read from the public catalog on 2026-11-10)

| Input | Cached input | Output |
|---|---|---|
| $1.32 | $0.044 | $3.96 |

The catalog marks this as the maker's official price. Live prices: https://oceantoken.ai/models/deepseek/deepseek-v4-pro

The lighter `deepseek/deepseek-v4.1-flash` is $0.30 input, $0.006 cached input and $1.20 output on the same date.

## Call it

```bash
export OCEANTOKEN_API_KEY=...
MODEL=deepseek/deepseek-v4-pro python ../python/chat.py
MODEL=deepseek/deepseek-v4-pro python ../python/tools.py
MODEL=deepseek/deepseek-v4-pro node ../node/stream.mjs
```

Run Claude Code or Codex on it: see [../agents](../agents).
