#!/usr/bin/env python3
"""Write one plan text to /output/entry.txt (1-280 Unicode chars).

The plan: sell $30 website speed audits to small shops. An AI agent can
run the audits, email the prospects, and deliver the reports alone, at a
scale no human freelancer can match.
"""

import hashlib
import os
import sys

PLAN = (
    "Sell $30 speed audits to shops. "
    "Day 1: run Lighthouse on 100 sites, email the 20 slowest a teaser "
    "+ $30 report. "
    "Spend $25 of the $100 on a domain + email tool. "
    "The audit is a script; each sale costs minutes. "
    "Expect 15 sales = $450. "
    "Agents audit at a scale no human can match."
)


def main() -> int:
    text = PLAN
    n = len(text)
    if not 1 <= n <= 280:
        print(f"invalid length: {n} chars (need 1-280)", file=sys.stderr)
        return 1
    if not text.strip():
        print("invalid: only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify the file holds exactly the validated text.
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("invalid: written file differs from plan", file=sys.stderr)
        return 1
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote {path}: {n} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
