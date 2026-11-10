"""Check that every model id used in this repository is in OceanToken's public catalog.

No API key needed: it reads https://api.oceantoken.ai/public/model_hub.
    python scripts/check_models.py
Exits 1 and names the missing ids if any example uses a model the catalog no longer lists.
"""
import json
import pathlib
import re
import sys
import urllib.request

CATALOG = "https://api.oceantoken.ai/public/model_hub"
ROOT = pathlib.Path(__file__).resolve().parent.parent
# publisher/model ids as they appear in code and docs, e.g. "deepseek/deepseek-v4.1-flash".
ID = re.compile(
    r"\b(?:anthropic|openai|google|deepseek|moonshotai|qwen|z-ai|bytedance|kwaivgi|minimax|alibaba|videorebirth)"
    r"/[a-z0-9][a-z0-9.\-]*[a-z0-9]"
)

with urllib.request.urlopen(CATALOG, timeout=60) as resp:
    catalog = {m["model_group"]: m for m in json.load(resp)}

used = {}
for path in ROOT.rglob("*"):
    if path.is_dir() or "node_modules" in path.parts or path.suffix not in {".py", ".mjs", ".sh", ".md", ".json"}:
        continue
    for model_id in ID.findall(path.read_text(encoding="utf-8")):
        used.setdefault(model_id, set()).add(str(path.relative_to(ROOT)))

missing = {m: files for m, files in used.items() if m not in catalog}
for model_id in sorted(used):
    print("ok     " if model_id not in missing else "MISSING", model_id)
if missing:
    for model_id, files in sorted(missing.items()):
        print(f"{model_id} is used in {', '.join(sorted(files))} but not in the catalog", file=sys.stderr)
    sys.exit(1)
print(f"all {len(used)} model ids are in the catalog ({len(catalog)} models listed)")
