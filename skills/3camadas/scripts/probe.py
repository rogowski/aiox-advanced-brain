#!/usr/bin/env python3
"""List disk hits for the 21b sondas. Does not score. Read the files before marking true."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".next",
    "coverage",
    "__pycache__",
    "vendor",
    ".turbo",
    ".cache",
    ".obsidian",
}

SKIP_PARTS = {"outputs/decoded"}

EXTS = {".md", ".py", ".ts", ".tsx", ".js", ".mjs", ".cjs", ".json", ".yml", ".yaml", ".toml", ".go", ".rs"}

MAX_BYTES = 200_000

PATTERNS = {
    "modelo": [
        r"\bgpt-4\b",
        r"\bgpt-5\b",
        r"\bclaude-",
        r"\bopenai\b",
        r"\banthropic\b",
        r"\blite?llm\b",
        r"model[_-]?id",
        r"model[_-]?name",
        r"\badapter\b",
    ],
    "harness": [
        r"canary",
        r"\bshadow\b",
        r"rollback",
        r"idempoten",
        r"approval[_-]?gate",
        r"deny-by-default",
        r"tool[_-]?permission",
    ],
    "brain": [
        r"retriev",
        r"embedd",
        r"\brag\b",
        r"vector[_-]?store",
        r"valid_from",
        r"supersed",
        r"write[_-]?back",
        r"\bacl\b",
    ],
}

NAME_FILES = {
    "harness": {"claude.md", "agents.md"},
}

NAME_PARTS = {
    "modelo": {"adapter", "adapters", "router", "llm"},
    "harness": {"hooks"},
    "brain": {"memory", "brain", "retrieve"},
}

DOC_NOISE = {
    "readme.md",
    "changelog.md",
    "mission.md",
    "resources.md",
    "index.html",
}


def _skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    if path.name.startswith("architecture-review-") or path.name.endswith(".scorecard.json"):
        return True
    rendered = path.as_posix()
    return any(token in rendered for token in SKIP_PARTS)


def _name_pillar(rel: str) -> str | None:
    path = Path(rel)
    name = path.name.lower()
    parts = {part.lower() for part in path.parts}
    for pillar, files in NAME_FILES.items():
        if name in files:
            return pillar
    for pillar, tokens in NAME_PARTS.items():
        if parts & tokens:
            return pillar
    return None


def probe(root: Path) -> dict:
    compiled = {pillar: [re.compile(pat, re.I) for pat in pats] for pillar, pats in PATTERNS.items()}
    hits: dict[str, list[dict]] = {k: [] for k in PATTERNS}
    seen: set[tuple[str, str]] = set()

    for path in root.rglob("*"):
        if not path.is_file() or _skip(path):
            continue
        rel = str(path.relative_to(root))
        if path.name.lower() in DOC_NOISE and path.parent == root:
            continue
        name_pillar = _name_pillar(rel)
        if name_pillar:
            key = (name_pillar, rel)
            if key not in seen:
                hits[name_pillar].append({"path": rel, "via": "name"})
                seen.add(key)
        if path.suffix.lower() not in EXTS:
            continue
        try:
            if path.stat().st_size > MAX_BYTES:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pillar, regexes in compiled.items():
            if any(rx.search(text) for rx in regexes):
                key = (pillar, rel)
                if key in seen:
                    continue
                hits[pillar].append({"path": rel, "via": "content"})
                seen.add(key)

    for pillar in hits:
        hits[pillar] = hits[pillar][:20]
    return {"root": str(root), "hits": hits}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("uso: probe.py <SOURCE_PATH>", file=sys.stderr)
        return 2
    root = Path(argv[1]).resolve()
    if not root.exists():
        print(f"SOURCE_PATH inexistente: {root}", file=sys.stderr)
        return 2
    print(json.dumps(probe(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
