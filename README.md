# OceanToken API examples

Runnable examples for [OceanToken](https://oceantoken.ai): one API key and one prepaid USD balance for nearly 500 AI models (chat, image, video, speech, embeddings), behind an OpenAI-compatible API and the Anthropic Messages API. Prices are at or below each maker's official price; Claude, GPT and Gemini models are billed at 10% below official.

- Base URL: `https://api.oceantoken.ai/v1`
- Auth: `Authorization: Bearer $OCEANTOKEN_API_KEY`
- Models and prices: https://oceantoken.ai/models (machine-readable: `https://api.oceantoken.ai/public/model_hub`, no key needed)
- Docs: https://docs.oceantoken.ai

## Setup

1. Create an account and an API key: https://docs.oceantoken.ai/get-started/create-api-key. Add a few dollars of credit.
2. Put the key in your environment. Never commit it.

```bash
export OCEANTOKEN_API_KEY=...
```

Every example reads only `OCEANTOKEN_API_KEY` (and optionally `MODEL` to try another model, `OCEANTOKEN_BASE_URL` to point elsewhere).

## Examples

| Task | Python | Node.js | curl |
|---|---|---|---|
| Chat | [python/chat.py](python/chat.py) | [node/chat.mjs](node/chat.mjs) | [curl/chat.sh](curl/chat.sh) |
| Streaming | [python/stream.py](python/stream.py) | [node/stream.mjs](node/stream.mjs) | [curl/stream.sh](curl/stream.sh) |
| Tool calling | [python/tools.py](python/tools.py) | [node/tools.mjs](node/tools.mjs) | [curl/tools.sh](curl/tools.sh) |
| Image generation | [python/image.py](python/image.py) | [node/image.mjs](node/image.mjs) | [curl/image.sh](curl/image.sh) |
| Video job (create, poll, download) | [python/video.py](python/video.py) | [node/video.mjs](node/video.mjs) | [curl/video.sh](curl/video.sh) |
| Anthropic Messages API | [python/claude_messages.py](python/claude_messages.py) | | |
| Backup models (`fallbacks`) | [python/fallbacks.py](python/fallbacks.py) | | |
| List models and prices | | | [curl/models.sh](curl/models.sh) |
| A video model's options | | | [curl/video-options.sh](curl/video-options.sh) |

### Python

```bash
cd python
pip install -r requirements.txt
python chat.py
MODEL=anthropic/claude-sonnet-5.5 python chat.py   # same code, another model
```

### Node.js (18.17+)

```bash
cd node
npm install
node chat.mjs
```

### curl

```bash
cd curl
./chat.sh          # video.sh and models.sh also need jq
```

## Coding agents

- [Run Claude Code on OceanToken](agents/claude-code.md)
- [Run Codex on OceanToken](agents/codex.md)

## Popular models

- [Seedance 2.5 (video)](models/seedance-2.5.md)
- [DeepSeek V4 Pro](models/deepseek-v4-pro.md)
- [Kimi K3](models/kimi-k3.md)

## What things cost

Each response carries its cost in the `x-oceantoken-cost` header, and the console's **Logs** page lists every request. The defaults in these examples are chosen to be cheap: `deepseek/deepseek-v4.1-flash` for chat, `openai/gpt-5-mini` for tools, a 4-second 480p clip on `bytedance/seedance-2.0-mini` for video. A model page on https://oceantoken.ai/models has the current price before you switch `MODEL`.

## Reliability

Many models have more than one channel. If one fails, the gateway retries and moves the request to the next channel of the same model, at the same price. `fallbacks` (see [python/fallbacks.py](python/fallbacks.py)) names other models to try after that. Details: https://docs.oceantoken.ai/reliability

## Keep model ids current

```bash
python scripts/check_models.py
```

checks every model id used in this repository against the public catalog (no key needed).

## Support

support@oceantoken.ai. Please include the `x-oceantoken-request-id` header of a failed request.

## License

MIT, see [LICENSE](LICENSE).
