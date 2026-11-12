# Run Codex on OceanToken

Codex talks to an OpenAI-compatible Responses API. Point it at OceanToken and every Codex request runs on your OceanToken key and balance, with GPT models or any other chat model that handles tools well.

## With one command

```bash
export OCEANTOKEN_API_KEY=...
npx -y @oceantoken/cli@latest use codex --use-env-key
```

Needs Node.js 18.17+. It adds a `[model_providers.oceantoken]` table to `~/.codex/config.toml`, makes it the default with `openai/gpt-5.5`, and backs the file up first. With `--use-env-key` the key stays out of the file. `npx -y @oceantoken/cli@latest unuse codex` puts your own lines back.

## By hand (Codex 0.135 and later)

Back up `~/.codex/config.toml`, then append:

```toml
[model_providers.oceantoken]
name = "OceanToken"
base_url = "https://api.oceantoken.ai/v1"
env_key = "OCEANTOKEN_API_KEY"
wire_api = "responses"
```

Create `~/.codex/oceantoken.config.toml` with two lines and no table header:

```toml
model_provider = "oceantoken"
model = "openai/gpt-5.5"
```

Run `codex --profile oceantoken`. Plain `codex` keeps your usual setup.

## Check it

```bash
codex exec --skip-git-repo-check --profile oceantoken -m deepseek/deepseek-v4.1-flash "Reply with the single word OK"
```

With a model that is not OpenAI's, Codex prints `Model metadata for ... not found. Defaulting to fallback metadata`. It is harmless.

## Choosing a model

Codex sends roughly 12,000 to 16,000 tokens of its own instructions with each request, so the per-request floor depends on the input price. Prices on 2026-11-10, per million tokens, from the public catalog:

| Model | Input | Cached input | Output |
|---|---|---|---|
| `openai/gpt-5.5` | $5.00 | $0.50 | $30.00 |
| `openai/gpt-5.4-mini` | $0.75 | $0.075 | $4.50 |
| `deepseek/deepseek-v4.1-flash` | $0.30 | $0.006 | $1.20 |
| `qwen/qwen3.8-max-0902` | $2.00 | $0.25 | $6.00 |

These are the makers' official list prices. For the two GPT models here, input and output are billed at 90% of them (`list_discount_factor` `0.9`); cached input stays at the official price. Switch for one run with `-m <model id>`.
