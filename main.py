# recorded build 2026-11-23
"""Write the plan entry to /output/entry.txt (stdlib only)."""

import os

PLAN = "Day 1: open a Fiverr gig selling AI-written Etsy product descriptions, $25 for 10 listings, made with free AI tools. Week 1: 1 order a day, week 2: 2, weeks 3-4: 4 a day. Spend the $100 on Facebook ads to Etsy sellers. Day 30: about $1,800."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    assert 1 <= len(PLAN) <= 280, f"PLAN is {len(PLAN)} chars, must be 1-280"
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == PLAN, "entry.txt content differs from PLAN"
    assert 1 <= len(back) <= 280, f"entry.txt is {len(back)} chars, must be 1-280"


if __name__ == "__main__":
    main()
