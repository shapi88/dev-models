#!/usr/bin/env python3
"""
generate-index.py (stub)

Walks the repo and prints a simple Markdown table of discovered models.
Future improvement: auto-update README sections.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def find_models() -> list[tuple[str, str, str, str]]:
    """Return list of (lang_or_tool, model, version, path)"""
    results = []
    for lang_dir in sorted(ROOT.iterdir()):
        if not lang_dir.is_dir() or lang_dir.name.startswith("."):
            continue
        models_dir = lang_dir / "models"
        if not models_dir.exists():
            continue
        for model_dir in sorted(p for p in models_dir.iterdir() if p.is_dir()):
            for ver_dir in sorted(p for p in model_dir.iterdir() if p.is_dir() and p.name.startswith("v")):
                rel = ver_dir.relative_to(ROOT)
                results.append((lang_dir.name, model_dir.name, ver_dir.name, str(rel)))
    return results

def main() -> None:
    models = find_models()
    if not models:
        print("No models found.")
        return

    print("| Language/Tool | Model | Version | Path |")
    print("|---------------|-------|---------|------|")
    for lang, model, ver, path in models:
        print(f"| {lang} | {model} | {ver} | `{path}/` |")

if __name__ == "__main__":
    main()