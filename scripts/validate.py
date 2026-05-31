#!/usr/bin/env python3
"""Calculate weighted grade and determine pass/fail status."""
import json, sys

def calculate_grade(data):
    assignments = data.get("assignments", [])
    if not assignments:
        return {"error": "No assignments provided"}

    total_weight = sum(a.get("weight", 1) for a in assignments)
    weighted_sum = sum(a.get("score", 0) * a.get("weight", 1) for a in assignments)
    final_pct = round(weighted_sum / total_weight, 1) if total_weight else 0

    thresholds = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
    letter = next((g for t, g in thresholds if final_pct >= t), "F")

    return {
        "final_percentage": final_pct,
        "letter_grade": letter,
        "passed": final_pct >= 50,
        "assignments_counted": len(assignments),
        "missing": [a["name"] for a in assignments if a.get("score") is None]
    }

if __name__ == "__main__":
    print(json.dumps(calculate_grade(json.loads(sys.argv[1])), indent=2))
