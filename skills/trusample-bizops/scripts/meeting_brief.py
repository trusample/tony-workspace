#!/usr/bin/env python3
"""Generate a pre-call brief + agenda + next steps for a sales/distributor call.

Draft-only.

Usage:
  python3 meeting_brief.py --with "Acme Distributor" --goal "Explore distribution" --products "Synthetic Urine, Synthetic CSF" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--with", dest="with_company", default="(Company / person)")
    ap.add_argument("--goal", default="(Goal)")
    ap.add_argument("--products", default="Synthetic Urine; Synthetic CSF")
    ap.add_argument("--duration", default="15 minutes")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    args = ap.parse_args()

    brief = dedent(f"""
    MEETING BRIEF
    With: {args.with_company}
    Goal: {args.goal}
    Duration: {args.duration}

    TruSample positioning (one-liner)
    - {args.from_company} manufactures consistent synthetic reference materials ({args.products}) for assay validation, method development, and PT workflows.

    Agenda
    1) Quick intros + context (2 min)
    2) Their current catalog + customer demand (5 min)
    3) Our lineup + differentiation (ISO/traceability/custom) (5 min)
    4) Commercials: regions, MOQ, lead time, pricing structure (2 min)
    5) Next steps + timelines (1 min)

    Discovery questions
    - What matrices/analytes do customers request most?
    - Typical order size and frequency?
    - Regions served and import constraints?
    - Required docs (COA/spec/SDS) and formatting?
    - Are they open to stocking vs. drop-ship vs. custom programs?

    Next steps (default)
    - Send product list + price list (if available)
    - Send sample COA/spec example
    - Schedule follow-up with procurement/technical lead
    """).strip()

    print(brief)


if __name__ == "__main__":
    main()
