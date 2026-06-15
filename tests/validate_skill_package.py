#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "references/workspace-subject-index.md",
    "schemas/input.schema.json",
    "schemas/output.schema.json",
    "examples/demo-transcript.md",
    "SUBMISSION.md",
]

for rel in required_files:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"missing required file: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    raise SystemExit("SKILL.md missing YAML frontmatter")
frontmatter = skill.split("---\n", 2)[1]
for key in ["name", "description"]:
    if not re.search(rf"^{key}:", frontmatter, re.M):
        raise SystemExit(f"SKILL.md frontmatter missing {key}")

for rel in ["schemas/input.schema.json", "schemas/output.schema.json"]:
    data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    if data.get("type") != "object":
        raise SystemExit(f"{rel} must define an object schema")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for phrase in ["Pharos Agent Carnival Alignment", "Callable Actions", "Differentiators"]:
    if phrase not in readme:
        raise SystemExit(f"README missing section: {phrase}")

print("skill package valid")
