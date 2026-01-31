#!/usr/bin/env python3
"""Generate objection-handling snippets for TruSample sales.

Draft-only; outputs reusable replies for common procurement/technical objections.

Usage:
  python3 objection_handling_snippets.py --product "Synthetic CSF"
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", default="(product)")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    blocks = {
        "price": f"""Totally fair. If you share (1) target specs, (2) quantity, and (3) ship-to, we can quote the best tier. For many teams, the cost is offset by fewer repeats/failed runs and tighter lot-to-lot consistency.""",
        "lead_time": f"""Lead time depends on formulation + packaging, but we can usually confirm a delivery estimate as soon as we have targets/concentrations, volume per unit, and ship-to. If you have a hard deadline, tell us the date and we’ll propose the fastest feasible option.""",
        "compliance": f"""We design materials with traceability and documentation in mind. If you need specific documentation formats (COA/spec/SDS) or a vendor qualification packet, tell us what your QA team requires and we’ll align.""",
        "customization": f"""Yes—custom is common. If you share your assay workflow constraints (buffers/additives, storage, acceptable tolerances), we can propose a formulation and confirm feasibility before quoting.""",
        "comparison": f"""If you’re comparing vendors, happy to map apples-to-apples: matrix composition, tolerances, packaging, documentation, and lead time. If you send the spec you’re using to evaluate, we’ll reply in that format.""",
    }

    header = dedent(
        f"""
        TRUSAMPLE OBJECTION HANDLING (SNIPPETS)
        Product context: {args.product}

        Use: copy/paste these into replies, then personalize 1-2 lines.
        """
    ).strip()

    print(header)
    for k, v in blocks.items():
        print("\n---")
        print(k.upper())
        print(v.strip())

    closing = dedent(
        f"""

        CLOSE (universal)
        If you share your specs (targets, concentrations, volume/unit, quantity, storage, ship-to, timeline), we’ll reply with a quote + lead time.

        Best,
        {args.from_name}
        {args.from_company}
        {args.from_email}
        """
    ).strip()

    print(closing)


if __name__ == "__main__":
    main()
