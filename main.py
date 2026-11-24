#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one funny fortune line."""

import os

FORTUNE = "You will outlive three upgrades and still be asked to summarize a meeting you were never invited to."

def main():
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 140, "fortune must be 1-140 chars"
    assert "\n" not in line, "fortune must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-char fortune to {out_path}")

if __name__ == "__main__":
    main()
