#!/usr/bin/env python3
"""Public-safe template harness for research/audit skills."""

import json

REQUIRED_SECTIONS = ["Scope", "Findings", "Recommendations", "Evidence", "Limitations"]


def score_report(text: str) -> dict:
    lower = text.lower()
    checks = [
        {"name": "required_sections", "pass": all(s.lower() in lower for s in REQUIRED_SECTIONS)},
        {"name": "has_evidence_language", "pass": "evidence" in lower or "example" in lower},
        {"name": "avoids_invented_certainty", "pass": "guaranteed" not in lower},
        {"name": "prioritizes_recommendations", "pass": "priority" in lower or "quick wins" in lower or "high" in lower},
        {"name": "acknowledges_limits", "pass": "limitation" in lower or "data unavailable" in lower},
    ]
    score = sum(1 for c in checks if c["pass"])
    return {"score": score, "max_score": len(checks), "checks": checks}


if __name__ == "__main__":
    sample = "Scope\nFindings\nRecommendations\nEvidence\nLimitations"
    print(json.dumps(score_report(sample), indent=2))
