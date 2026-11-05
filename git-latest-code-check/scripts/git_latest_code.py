#!/usr/bin/env python3
"""Temporary CLI forwarding path; canonical implementation lives in the new Skill."""

from pathlib import Path
import runpy


def main() -> None:
    target = (
        Path(__file__).resolve().parents[2]
        / "git-safe-collaboration" / "scripts" / "git_safe_collaboration.py"
    )
    if not target.is_file():
        print("STATUS ERROR")
        print("message: install the adjacent git-safe-collaboration Skill before using this legacy CLI")
        raise SystemExit(2)
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()
