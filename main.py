import os
import sys

PLAN = "Charge shops $30 for a speed audit. Day 1: Lighthouse 100 sites, email the 20 slowest a sample + $30 audit. Put $25 of the $100 into a domain + email sender. The audit is code, so each order takes minutes. Land 15 orders in 30 days for $450. Scale no human team can match."


def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
