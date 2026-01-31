#!/usr/bin/env python3
"""Generate a one-page product/spec sheet (text) for a TruSample material.

Draft-only; outputs a structured sheet you can paste into a doc/Notion/web page.

Usage:
  python3 product_spec_sheet.py --product "Synthetic CSF" --intended_use "Assay validation" --storage "-80C" --format "Aliquoted vials" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", default="(Product name)")
    ap.add_argument("--sku", default="(SKU)")
    ap.add_argument("--intended_use", default="Assay validation / method development / PT")
    ap.add_argument("--matrix", default="(Matrix description)")
    ap.add_argument("--analytes", default="(Analytes/targets)")
    ap.add_argument("--concentrations", default="(Concentration options)")
    ap.add_argument("--format", default="Aliquoted vials")
    ap.add_argument("--fill_volume", default="(e.g., 1 mL / 5 mL / 10 mL)")
    ap.add_argument("--storage", default="-20°C (default; confirm)")
    ap.add_argument("--stability", default="(stability statement / to be confirmed)")
    ap.add_argument("--documentation", default="COA / Spec Sheet available per lot")
    ap.add_argument("--compliance", default="ISO 13485 (confirm scope)")

    args = ap.parse_args()

    sheet = dedent(f"""
    {args.product}

    SKU: {args.sku}

    Overview
    - Intended use: {args.intended_use}
    - Matrix: {args.matrix}

    Composition
    - Targets/analytes: {args.analytes}
    - Concentrations: {args.concentrations}

    Packaging
    - Format: {args.format}
    - Fill volume: {args.fill_volume}

    Handling
    - Storage: {args.storage}
    - Stability: {args.stability}

    Documentation / Traceability
    - {args.documentation}

    Quality
    - {args.compliance}

    Notes
    - Custom formulations and packaging options available on request.
    """).strip()

    print(sheet)


if __name__ == "__main__":
    main()
