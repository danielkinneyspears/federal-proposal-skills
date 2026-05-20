#!/usr/bin/env python3
"""Scan a text file for price and cost information.

Used by the checking-submission-compliance skill to detect price or cost
content in a volume where the solicitation requires price to be kept separate.
Run it on the extracted plain text of a non-price volume (for example, the
technical or management volume).

Every hit is a CANDIDATE. The patterns flag generously; false positives are
expected. A human, or the skill, confirms whether each match is genuinely price
information that violates the Section L volume-separation rule.

Usage:   python scan_price_leakage.py <textfile>
Output:  JSON list of matches with line numbers.
Exit:    0 on success, non-zero on usage/IO error.
"""
import sys
import os
import re
import json

# Patterns that commonly indicate price or cost content. Tuned to flag
# generously and let a human filter false positives, because a missed price
# leak can disqualify a proposal while a false positive only costs a glance.
PATTERNS = {
    "currency_amount": r"\$\s?\d[\d,]*(?:\.\d+)?",
    "price_term": (r"\b(price|pricing|priced|cost|costs|costed|fee|fees|"
                   r"labor rate|wrap rate|burdened rate|fully burdened|"
                   r"profit|margin)\b"),
    "hourly_rate": r"\$?\s?\d[\d,.]*\s?(?:/|per\s)\s?(?:hr|hour|hours)",
}


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: scan_price_leakage.py <textfile>"}))
        return 2

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(json.dumps({"error": f"file not found: {path}"}))
        return 1

    compiled = {kind: re.compile(rx, re.IGNORECASE)
                for kind, rx in PATTERNS.items()}

    matches = []
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for line_no, line in enumerate(handle, 1):
                for kind, regex in compiled.items():
                    for found in regex.finditer(line):
                        matches.append({
                            "line": line_no,
                            "kind": kind,
                            "text": found.group(0).strip(),
                        })
    except OSError as exc:
        print(json.dumps({"error": f"could not read file: {exc}"}))
        return 1

    print(json.dumps({
        "file": os.path.basename(path),
        "match_count": len(matches),
        "matches": matches,
        "note": ("Matches are candidates only. Confirm whether each is price "
                 "information that violates Section L volume separation."),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
