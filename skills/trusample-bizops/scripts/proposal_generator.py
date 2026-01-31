#!/usr/bin/env python3
"""Generate a 1–2 page proposal/quote draft from a structured spec.

Draft-only. Outputs Markdown you can paste into a doc/Notion/email.

Usage:
  python3 proposal_generator.py \
    --customer "Acme Lab" --project "Synthetic CSF" \
    --matrix "Synthetic CSF" --analytes "Aβ42, t-tau" --concentrations "100 pg/mL" \
    --volume "10 mL" --units "20 vials" --ship_to "Miami, FL 33101" --timeline "2 weeks" \
    --price "$1,250" --terms "Net 15" --validity "14 days"
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--project", default="(Project name)")

    ap.add_argument("--matrix", default="(Matrix)")
    ap.add_argument("--analytes", default="(Targets/analytes)")
    ap.add_argument("--concentrations", default="(Target concentrations)")
    ap.add_argument("--volume", default="(Fill volume per unit)")
    ap.add_argument("--units", default="(Quantity)")

    ap.add_argument("--ship_to", default="(Ship-to)")
    ap.add_argument("--timeline", default="(Lead time / delivery window)")
    ap.add_argument("--storage", default="(Storage)")
    ap.add_argument("--shipping_temp", default="(Ambient / cold pack / dry ice)")
    ap.add_argument("--documentation", default="COA / spec sheet per lot (if applicable)")

    ap.add_argument("--price", default="(Total price)")
    ap.add_argument("--terms", default="Net 15")
    ap.add_argument("--validity", default="14 days")

    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")

    args = ap.parse_args()

    attn = f"Attn: {args.contact}\n" if args.contact else ""

    md = dedent(
        f"""# Quote / Proposal — {args.project}

**Customer:** {args.customer}  
{attn}**Prepared by:** {args.from_company} ({args.from_email})  
**Validity:** {args.validity}

## 1) Scope of supply
We will provide the following synthetic reference material(s) per the specifications below.

**Material specification**
- Matrix: {args.matrix}
- Targets/analytes: {args.analytes}
- Target concentrations: {args.concentrations}
- Fill volume per unit: {args.volume}
- Quantity: {args.units}

**Handling & logistics**
- Storage: {args.storage}
- Shipping temperature: {args.shipping_temp}
- Ship-to: {args.ship_to}
- Estimated lead time / delivery window: {args.timeline}

**Documentation**
- {args.documentation}

## 2) Pricing
**Total:** {args.price}  
**Payment terms:** {args.terms}

## 3) Assumptions / exclusions
- Pricing and lead time are contingent on final confirmed specifications.
- Any regulatory/vendor qualification packet requirements should be specified in advance.
- Shipping costs/taxes may be added depending on destination and temperature control.

## 4) Next steps
1) Confirm billing contact + billing address + PO (if applicable)
2) Confirm ship-to address and required shipping temperature
3) Invoice issuance and scheduling of fulfillment
"""
    ).strip()

    print(md)


if __name__ == "__main__":
    main()
