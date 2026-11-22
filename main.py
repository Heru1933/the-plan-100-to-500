#!/usr/bin/env python3
"""Write the plan to /output/entry.txt (1-280 Unicode chars)."""
import hashlib
import os
import sys

PLAN = "Sell $30 speed audits to shops. Day 1: run Lighthouse on 100 sites, email the 20 slowest a teaser + $30 report. Spend $25 of the $100 on a domain + email tool. The audit is a script; each sale costs minutes. Expect 15 sales in 30 days = $450. No human audits at this scale."


def main():
    if not (1 <= len(PLAN) <= 280):
        print(f"plan length {len(PLAN)} out of range", file=sys.stderr)
        return 1
    if not PLAN.strip():
        print("plan is whitespace-only", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    if back != PLAN:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote /output/entry.txt: {len(PLAN)} chars (read-back verified)")
    print("sha256:", hashlib.sha256(PLAN.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
