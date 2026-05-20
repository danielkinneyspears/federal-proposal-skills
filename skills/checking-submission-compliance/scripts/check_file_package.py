#!/usr/bin/env python3
"""Check a directory of submission files against naming and size rules.

Used by the checking-submission-compliance skill to verify the submission
package's files against the Section L file-naming convention and any per-file
size limit.

Usage:
  python check_file_package.py <dir> [--max-mb N] [--pattern REGEX]

  --max-mb N      Flag any file larger than N megabytes (per-file size limit).
  --pattern REGEX Flag any file whose name does not match this regular
                  expression (the required naming convention).

Output: JSON listing every file with its size, plus a list of flags.
Exit:   0 on success (even if flags were raised), non-zero on usage/IO error.

The script reports facts. Deciding whether a flag is a true compliance failure
remains the skill's judgment, against the actual solicitation rules.
"""
import sys
import os
import re
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description="Check submission files.")
    parser.add_argument("directory", help="directory of submission files")
    parser.add_argument("--max-mb", type=float, default=None,
                        help="per-file size limit in megabytes")
    parser.add_argument("--pattern", default=None,
                        help="required file-name regex")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(json.dumps({"error": f"not a directory: {args.directory}"}))
        return 1

    try:
        pattern = re.compile(args.pattern) if args.pattern else None
    except re.error as exc:
        print(json.dumps({"error": f"invalid --pattern regex: {exc}"}))
        return 1

    files = []
    flags = []
    for name in sorted(os.listdir(args.directory)):
        full = os.path.join(args.directory, name)
        if not os.path.isfile(full):
            continue
        size_mb = round(os.path.getsize(full) / (1024 * 1024), 3)
        entry = {"name": name, "size_mb": size_mb}
        if args.max_mb is not None and size_mb > args.max_mb:
            entry["over_size_limit"] = True
            flags.append(f"{name}: {size_mb} MB exceeds the {args.max_mb} MB limit")
        if pattern is not None and not pattern.search(name):
            entry["name_noncompliant"] = True
            flags.append(f"{name}: name does not match the required pattern")
        files.append(entry)

    print(json.dumps(
        {"files": files, "flags": flags, "flag_count": len(flags)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
