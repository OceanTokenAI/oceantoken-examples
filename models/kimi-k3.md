# Kimi K3 API (Moonshot AI) on OceanToken

Model id: `moonshotai/kimi-k3`. Chat, tool calling, reasoning, 1,048,576-token context. OpenAI-compatible and Anthropic Messages APIs.

## Price (USD per million tokens, read from the public catalog on 2026-11-10)

| Input | Cached input | Output |
|---|---|---|
| $3.00 | $0.30 | $15.00 |

The catalog marks this as the maker's official price. Live prices: https://oceantoken.ai/models/moonshotai/kimi-k3

## Call it

```bash
export OCEANTOKEN_API_KEY=...
MODEL=moonshotai/kimi-k3 python ../python/chat.py
MODEL=moonshotai/kimi-k3 python ../python/tools.py
```

The same model id works on `/v1/messages` with the Anthropic SDK: `MODEL=moonshotai/kimi-k3 python ../python/claude_messages.py`.
