#!/usr/bin/env python3
"""Structural checks for study-guide pages. Does not read the novel."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

REQUIRED_HEADINGS = [
    "## Summary",
    "## Difficult vocabulary",
    "## Difficult phrases",
]
MAX_QUOTE_WORDS = 12


def quoted_spans(text: str) -> list[str]:
    return re.findall(r"[“\"]([^”\"]+)[”\"]", text)


def main() -> int:
    files = sorted(PAGES.glob("page-*.md"))
    if not files:
        print("No page files found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        name = path.name
        m = re.match(r"page-(\d{3})\.md$", name)
        if not m:
            errors.append(f"{name}: unexpected filename")
            continue
        num = int(m.group(1))
        if f"**PDF page:** {num}" not in text and f"**PDF page:** {num:03d}" not in text:
            # allow unpadded integer
            if f"**PDF page:** {num}" not in text:
                errors.append(f"{name}: missing PDF page {num} marker")
        if "**Location:**" not in text:
            errors.append(f"{name}: missing Location")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{name}: missing {heading}")
        for quote in quoted_spans(text):
            words = re.findall(r"[A-Za-z0-9']+", quote)
            if len(words) > MAX_QUOTE_WORDS:
                errors.append(
                    f"{name}: quoted phrase too long ({len(words)} words): {quote[:80]}"
                )

    expected = {f"page-{i:03d}.md" for i in range(1, 66)}
    present = {p.name for p in files}
    missing = sorted(expected - present)
    extra_ok = present - expected
    if missing:
        errors.append("missing expected files: " + ", ".join(missing))

    print(f"Checked {len(files)} page files (expected 001–065 present).")
    if extra_ok:
        print("Additional pages beyond 065:", ", ".join(sorted(extra_ok)))
    if errors:
        print("FAILED")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: required sections present; no long quoted phrases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
