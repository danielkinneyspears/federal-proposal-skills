#!/usr/bin/env python3
"""Deterministic scan of a proposal draft for the obligations it creates.

Reports commitment verbs, absolutes, numbers carrying a unit, and filler that
scores nothing. Standard library only.

The scan deliberately over-matches. A checker that misses obligations is worse
than no checker, because it grants false confidence; this one flags candidates and
leaves the judgement to the person reading. Finding the verb is mechanical.
Deciding whether the promise is affordable is not.

Usage:
    scan_commitments.py <file> [--json] [--context N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Modal and performative verbs that create obligations. "Will" and "shall" are
# the classic pair; the rest bind just as hard once the proposal is incorporated.
COMMIT = [
    "will", "shall", "guarantee", "guarantees", "guaranteed", "ensure", "ensures",
    "ensured", "maintain", "maintains", "provide", "provides", "deliver",
    "delivers", "commit", "commits", "committed", "warrant", "warrants",
    "assure", "assures", "achieve", "achieves", "exceed", "exceeds",
]

# Uninsurable by construction. One ordinary bad day is a documented failure.
ABSOLUTE = [
    "100%", "zero", "never", "always", "all times", "24/7", "24x7",
    "fully compliant", "no downtime", "any and all", "unlimited", "every single",
    "at all times", "without exception",
]

# Reads as a commitment to an evaluator, promises nothing, costs page count.
FILLER = [
    "strive", "strives", "endeavor", "endeavors", "endeavour", "endeavours",
    "aim to", "aims to", "seek to", "seeks to", "work to", "best effort",
    "best efforts", "world-class", "best-in-class", "cutting-edge", "seamless",
    "robust", "leverage", "leverages", "state-of-the-art", "industry-leading",
    "unparalleled", "second to none",
]

UNITS = (
    r"%|percent|hours?|hrs?|days?|weeks?|months?|years?|minutes?|mins?|seconds?"
    r"|secs?|FTEs?|MWh?|kWh?|km|miles?|meters?|metres?|business\sdays?|m\b|ft\b"
)
SPELLED = (
    r"one|two|three|four|five|six|seven|eight|nine|ten|twelve|fifteen|twenty"
    r"|thirty|sixty|ninety"
)

CATS = ("obligation", "absolute", "number", "filler")

LABEL = {
    "obligation": "Candidate obligations",
    "absolute": "Absolutes",
    "number": "Numbers carrying a unit",
    "filler": "Filler that scores nothing",
}

NOTE = {
    "obligation": "Each is a promise performed at your own cost if it survives into "
                  "the contract. Find the requirement behind every one.",
    "absolute": "The most expensive words available to you. One ordinary bad day "
                "turns each into a documented failure.",
    "number": "A commitment with a measurement attached. Confirm it is staffed and "
              "funded exactly as written, and that the conditions it depends on "
              "are stated.",
    "filler": "No metric, no obligation, no score. Costing you page count in a "
              "page-limited volume.",
}


def _grp(words: list[str]) -> str:
    """Longest-first, or 'will' swallows 'world-class'."""
    return "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))


def build_pattern() -> re.Pattern[str]:
    return re.compile(
        rf"(?P<absolute>{_grp(ABSOLUTE)})"
        rf"|(?P<obligation>\b(?:{_grp(COMMIT)})\b)"
        rf"|(?P<filler>\b(?:{_grp(FILLER)})\b)"
        # A number counts only when it carries a unit, a percent or a currency;
        # bare figures are usually section and paragraph references. The separator
        # must allow a hyphen: "15-minute response" and "72-hour turnaround" are
        # the normal way proposals write these, and missing them misses the most
        # common form.
        rf"|(?P<number>(?:\$\s?[\d,]+(?:\.\d+)?)"
        rf"|(?:\b\d[\d,]*(?:\.\d+)?[\s-]?(?:{UNITS}))"
        rf"|(?:\b(?:{SPELLED})[\s-](?:{UNITS})))",
        re.IGNORECASE,
    )


def scan(text: str) -> dict:
    pattern = build_pattern()
    hits: list[dict] = []
    counts = dict.fromkeys(CATS, 0)

    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in pattern.finditer(line):
            kind = next(k for k in CATS if m.lastgroup == k or m.groupdict().get(k))
            # lastgroup is the reliable signal; the comprehension above guards
            # against a None lastgroup on some Python builds.
            kind = m.lastgroup or kind
            counts[kind] += 1
            hits.append(
                {
                    "line": lineno,
                    "kind": kind,
                    "text": m.group(0),
                    "context": line.strip()[:160],
                }
            )

    words = len(text.split())
    binding = counts["obligation"] + counts["absolute"]
    # Per 250 words so a full volume and a single section are comparable.
    # Meaningless under 60 words, so it is reported as None rather than a number
    # that would swing into the dozens on a two-sentence paste.
    density = round(binding / (words / 250), 1) if words >= 60 else None

    return {
        "words": words,
        "counts": counts,
        "total": sum(counts.values()),
        "binding": binding,
        "density_per_250w": density,
        "hits": hits,
    }


def verdict(density: float | None) -> str:
    if density is None:
        return "Too short to rate. Scan a full section for a meaningful density."
    if density >= 12:
        return "High. Read every obligation before this goes out."
    if density >= 6:
        return "Normal for a technical volume. Still run the audit."
    return "Low. Confirm you have actually answered Section L."


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", type=Path)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--context", type=int, default=0,
                    help="show N hits per category with their line context")
    args = ap.parse_args()

    if not args.file.is_file():
        print(f"error: {args.file} is not a file", file=sys.stderr)
        return 2

    text = args.file.read_text(encoding="utf-8", errors="replace")
    result = scan(text)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"\n{args.file.name} — {result['words']:,} words\n")
    for kind in CATS:
        print(f"  {result['counts'][kind]:>5}  {LABEL[kind]}")
    print(f"\n  {result['binding']:>5}  binding items (obligations + absolutes)")
    d = result["density_per_250w"]
    print(f"  {'—' if d is None else d:>5}  per 250 words — {verdict(d)}\n")

    for kind in CATS:
        if not result["counts"][kind]:
            continue
        print(f"{LABEL[kind]} — {NOTE[kind]}")
        shown = [h for h in result["hits"] if h["kind"] == kind]
        limit = args.context if args.context else 0
        for h in shown[:limit]:
            print(f"  line {h['line']:>4}  {h['text']!r}")
            print(f"            {h['context']}")
        if not limit:
            uniq: dict[str, int] = {}
            for h in shown:
                uniq[h["text"].lower()] = uniq.get(h["text"].lower(), 0) + 1
            terms = ", ".join(
                f"{t} ({n})" for t, n in sorted(uniq.items(), key=lambda kv: -kv[1])
            )
            print(f"  {terms}")
        elif len(shown) > limit:
            print(f"  … and {len(shown) - limit} more (raise --context)")
        print()

    print("Every hit is a candidate, not a finding. For each one: did the")
    print("solicitation require it, can you staff and fund it exactly as written,")
    print("and will an evaluator reward it?\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
