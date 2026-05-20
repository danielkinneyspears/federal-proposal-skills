#!/usr/bin/env python3
"""Report the page count and key metadata of a PDF.

Used by the checking-submission-compliance skill to verify a proposal volume
against its Section L page limit. The script returns the physical page count;
applying the solicitation's "what counts toward the limit" rule remains a
judgment the skill makes.

Dependency: pypdf (install with: pip install pypdf)

Usage:   python pdf_page_count.py <file.pdf>
Output:  JSON with page_count and metadata, or a JSON error object.
Exit:    0 on success, non-zero on error.
"""
import sys
import os
import json


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: pdf_page_count.py <file.pdf>"}))
        return 2

    path = sys.argv[1]
    if not os.path.isfile(path):
        print(json.dumps({"error": f"file not found: {path}"}))
        return 1

    try:
        from pypdf import PdfReader
    except ImportError:
        print(json.dumps({
            "error": "pypdf is not installed. Install it with: pip install pypdf"
        }))
        return 1

    try:
        reader = PdfReader(path)
        meta = reader.metadata or {}
        result = {
            "file": os.path.basename(path),
            "page_count": len(reader.pages),
            "title": str(meta.get("/Title", "")),
            "author": str(meta.get("/Author", "")),
            "encrypted": bool(reader.is_encrypted),
        }
        print(json.dumps(result, indent=2))
        return 0
    except Exception as exc:  # pypdf raises a variety of errors on bad PDFs
        print(json.dumps({"error": f"could not read PDF: {exc}"}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
