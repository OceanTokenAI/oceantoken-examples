# Run Claude Code on OceanToken

Claude Code speaks the Anthropic Messages API. OceanToken serves that API for every chat model, so Claude Code runs on your OceanToken key and balance with Claude models, or with any other chat model that handles tools well.

## 1. A key with a spending cap

Create an API key in the console and give it a **Credit limit**: an agent sends many requests, and the limit caps what this key can spend. Keep it in an environment variable, never in a file in your repository:

```bash
export OCEANTOKEN_API_KEY=...        # put this in your shell profile
```

## 2a. Environment variables only (the key never touches a file)

```bash
export ANTHROPIC_BASE_URL=https://api.oceantoken.ai     # no /v1: Claude Code adds it
export ANTHROPIC_AUTH_TOKEN="$OCEANTOKEN_API_KEY"
export ANTHROPIC_MODEL=anthropic/claude-sonnet-5.5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=anthropic/claude-haiku-4.5
claude
```

## 2b. Or a settings file

For one project, `.claude/settings.local.json` (git ignores it); for every project, `~/.claude/settings.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.oceantoken.ai",
    "ANTHROPIC_AUTH_TOKEN": "<your OceanToken key>",
    "ANTHROPIC_MODEL": "anthropic/claude-sonnet-5.5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "anthropic/claude-haiku-4.5"
  }
}
```

This file holds the key in plain text. Prefer 2a, or keep the file out of git.

## 3. Check it

```bash
claude -p "Reply with the single word OK"
```

## Choosing a model

Use model ids exactly as https://oceantoken.ai/models lists them. Claude Code resends a long prompt on every turn, so the **cached input** price matters as much as the input price. Prices on 2026-11-10, per million tokens, from the public catalog (`https://api.oceantoken.ai/public/model_hub`):

| Model | Input | Cached input | Output |
|---|---|---|---|
| `anthropic/claude-sonnet-5.5` | $2.00 | $0.10 | $10.00 |
| `anthropic/claude-opus-5.5` | $4.00 | $0.20 | $20.00 |
| `anthropic/claude-haiku-4.5` | $1.00 | $0.10 | $5.00 |
| `deepseek/deepseek-v4.1-flash` | $0.30 | $0.006 | $1.20 |

These are the makers' official list prices. Claude models are billed at 90% of them (the catalog's `list_discount_factor` is `0.9`). Prices change; check the catalog or the model page before you rely on a number.

## Switching back

Unset the variables (or delete the `env` block) and start a new session.
