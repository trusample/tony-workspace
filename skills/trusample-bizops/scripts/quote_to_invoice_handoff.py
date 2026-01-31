#!/usr/bin/env python3
"""Convert a quote summary into an invoice-ready fulfillment checklist + email draft.

Draft-only.

Usage:
  python3 quote_to_invoice_handoff.py --customer "Acme Lab" --items "Synthetic CSF x20 (10 mL)" --ship_to "Miami, FL" --timeline "2 weeks" --amount "$1,250" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--items", default="(Items / SKUs / quantities)")
    ap.add_argument("--ship_to", default="(Ship-to)")
    ap.add_argument("--timeline", default="(Timeline)")
    ap.add_argument("--amount", default="(Amount)")
    ap.add_argument("--terms", default="Net 15")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    hi = f"Hi {args.contact}," if args.contact else f"Hi {args.customer},"

    email = f"""{hi}

Great — based on the confirmed specs, here’s the next step to proceed:

Order summary
- Items: {args.items}
- Ship-to: {args.ship_to}
- Timeline: {args.timeline}
- Total: {args.amount}
- Terms: {args.terms}

To issue the invoice, please confirm:
1) Billing contact + billing address
2) Preferred invoice delivery method (PDF vs link)
3) PO number (if you’d like it referenced)

Once confirmed, we’ll send the invoice and schedule fulfillment.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    checklist = dedent(
        f"""
        FULFILLMENT CHECKLIST (internal)
        - Confirm final specs: items/SKUs, targets, concentrations, volume/unit
        - Confirm packaging: aliquoted vs bulk, labeling format
        - Confirm storage + shipping: temp control, ice/dry ice, transit time
        - Confirm documentation: COA/spec/SDS needed
        - Create invoice / receive PO
        - Schedule production (if custom)
        - QA release + lot IDs recorded
        - Pack + ship + tracking sent
        - Close loop: delivery confirmation + feedback
        """
    ).strip()

    print("EMAIL DRAFT:\n" + email.strip())
    print("\n" + checklist)


if __name__ == "__main__":
    main()
