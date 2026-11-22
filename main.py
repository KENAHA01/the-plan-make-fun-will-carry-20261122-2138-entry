# recorded build 2026-11-23
"""Write the 30-day plan to /output/entry.txt."""

import os

PLAN = "Day 1: open a Fiverr gig selling AI-written Etsy product descriptions, $25 for 10 listings, made with free AI tools. Spend the $100 on Facebook ads to Etsy sellers pointing at the gig. Deliver 4 orders a day, $100 a day, reinvest profits in ads. Day 30: about $2,000."

OUTPUT_FILE = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(PLAN) <= 280, f"PLAN is {len(PLAN)} chars, must be 1-280"
    path = os.path.join(out_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == PLAN, f"entry.txt is {len(back)} chars, must be 1-280"
    print(f"Wrote {path} ({len(back)} chars)")


if __name__ == "__main__":
    main()
