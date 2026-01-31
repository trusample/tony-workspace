#!/usr/bin/env python3
"""Generate an invoice / payment request email draft.

Draft-only. Designed for when you need to request payment details, PO, billing address,
or send an invoice link/PDF.

Usage:
  python3 invoice_request_draft.py --customer "Acme Lab" --project "Synthetic CSF" --amount "$1,250" --terms "Net 15" --deliverable "20 units, 10 mL each" 
"""

import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--project", default="(Project / Product)")
    ap.add_argument("--deliverable", default="(Deliverable)")
    ap.add_argument("--amount", default="(Amount)")
    ap.add_argument("--terms", default="Net 15")
    ap.add_argument("--po", default="")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    hi = f"Hi {args.contact}," if args.contact else f"Hi {args.customer},"

    subject = f"Invoice / payment details — {args.project}".strip()

    po_line = f"If you’d like us to reference a PO, we can include PO #{args.po}." if args.po else "If you’d like us to reference a PO number, share it and we’ll include it on the invoice."

    body = f"""{hi}

To proceed with {args.project}, we can issue the invoice for:
- Deliverable: {args.deliverable}
- Amount: {args.amount}
- Terms: {args.terms}

Please confirm the following so we can send the invoice in the format you prefer:
1) Billing contact + billing address
2) Preferred invoice delivery method (PDF attachment vs invoice link)
3) Tax/VAT details (if applicable)

{po_line}

Once confirmed, we’ll send the invoice and schedule fulfillment.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    print("SUBJECT:\n" + subject)
    print("\nEMAIL DRAFT:\n" + body.strip())


if __name__ == "__main__":
    main()
