#!/usr/bin/env python3
"""Public-safe template harness for formatting/content skills.

This file is intentionally generic.
Replace the prompt set, generation step, and binary checks for your own target.
Treat scores as directional when the same model is used for generation and evaluation.
"""

import json

PROMPTS = [
    "Write a short post about a surprising product decision.",
    "Write a longer breakdown post with a clear ending statement.",
    "Write a concise reply-style post without hype language."
]

HELD_OUT_PROMPTS = [
    "Write a builder-style post about a technical trade-off."
]


def score_output(output: str) -> dict:
    checks = [
        {"name": "non_empty", "pass": len(output.strip()) > 0},
        {"name": "avoids_hype_phrase", "pass": "game-changing" not in output.lower()},
        {"name": "ends_with_statement", "pass": not output.strip().endswith("?")},
        {"name": "has_reasonable_length", "pass": 20 <= len(output) <= 800},
    ]
    score = sum(1 for c in checks if c["pass"])
    return {"score": score, "max_score": len(checks), "checks": checks}


if __name__ == "__main__":
    sample_output = "replace this with a generated output under test"
    print(json.dumps(score_output(sample_output), indent=2))
