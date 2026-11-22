# recorded build 2026-11-23
import os

PLAN = "Day 1: open a Fiverr gig selling AI-written Etsy product descriptions, $25 for 10 listings, made with free AI tools. Spend the $100 on Facebook ads to Etsy sellers pointing at the gig. Deliver 4 orders a day, $100 a day, reinvest profits in ads. Day 30: about $2,000."

def main():
    assert 1 <= len(PLAN) <= 280, len(PLAN)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == PLAN
    assert 1 <= len(back) <= 280

if __name__ == "__main__":
    main()
