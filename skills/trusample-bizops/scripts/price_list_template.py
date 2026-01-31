#!/usr/bin/env python3
"""Generate a simple price list template (text + optional CSV) for TruSample.

Draft-only. This does not set real pricing; it generates a structured template
with placeholders + suggested tiering.

Usage:
  python3 price_list_template.py --currency USD --tiers "1-9,10-49,50+" --output csv
"""

import argparse
import csv
import sys
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--currency", default="USD")
    ap.add_argument("--tiers", default="1-9,10-49,50+")
    ap.add_argument("--output", choices=["text", "csv"], default="text")
    args = ap.parse_args()

    tiers = [t.strip() for t in args.tiers.split(",") if t.strip()]

    rows = [
        {
            "SKU": "TS-URINE-001",
            "Product": "Synthetic Urine (base matrix)",
            "Format": "Aliquoted vials",
            "Fill Volume": "(e.g., 1 mL / 5 mL / 10 mL)",
            "Storage": "(e.g., -20°C)",
            "Documentation": "COA/spec per lot",
            **{f"Price ({args.currency}) {tier}": "(TBD)" for tier in tiers},
        },
        {
            "SKU": "TS-CSF-001",
            "Product": "Synthetic CSF (base matrix)",
            "Format": "Aliquoted vials",
            "Fill Volume": "(e.g., 1 mL / 5 mL / 10 mL)",
            "Storage": "(e.g., -80°C)",
            "Documentation": "COA/spec per lot",
            **{f"Price ({args.currency}) {tier}": "(TBD)" for tier in tiers},
        },
        {
            "SKU": "TS-CUSTOM-001",
            "Product": "Custom formulation (targets/concentrations)",
            "Format": "Aliquoted or bulk",
            "Fill Volume": "(TBD)",
            "Storage": "(TBD)",
            "Documentation": "COA/spec per lot",
            **{f"Price ({args.currency}) {tier}": "(quote)" for tier in tiers},
        },
    ]

    if args.output == "csv":
        fieldnames = list(rows[0].keys())
        w = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
        return

    text = dedent(
        f"""
        TRUSAMPLE PRICE LIST (TEMPLATE)
        Currency: {args.currency}
        Volume assumptions: (define per SKU)
        Tiering: {', '.join(tiers)}

        Notes / policies (fill in)
        - MOQ:
        - Lead time:
        - Shipping:
        - Storage:
        - Custom work: discovery call + feasibility + quote

        PRODUCTS
        """
    ).strip()

    print(text)
    for r in rows:
        print("\n---")
        print(f"SKU: {r['SKU']}")
        print(f"Product: {r['Product']}")
        print(f"Format: {r['Format']}")
        print(f"Fill Volume: {r['Fill Volume']}")
        print(f"Storage: {r['Storage']}")
        print(f"Documentation: {r['Documentation']}")
        for tier in tiers:
            print(f"Price {tier}: {r[f'Price ({args.currency}) {tier}']}")


if __name__ == "__main__":
    main()
